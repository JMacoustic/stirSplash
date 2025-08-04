import bpy
import math, sys, os
import json
import random
import string
from typing import Optional
from dataclasses import dataclass, field
import copy
import logging


@dataclass
class Material:
    basecolor: tuple
    roughness: float
    transmission: float
    IOR: float
    metallic: Optional[float] = None

water = Material(
    basecolor = (1, 1, 1, 1),
    roughness = 0.08,
    transmission = 1,
    IOR = 1.5)

glass = Material(
    basecolor = (1, 1, 1, 1),
    roughness = 0,
    transmission = 0.99,
    IOR = 1.2)

stainless = Material(
    basecolor = (0.35, 0.35, 0.35, 1),
    roughness = None,
    transmission = None,
    IOR = None,
    metallic = 0.91)

@dataclass
class RenderOptions:
    glass: Material = field(default_factory=lambda: copy.deepcopy(glass))
    water: Material = field(default_factory=lambda: copy.deepcopy(water))
    stainless: Material = field(default_factory=lambda: copy.deepcopy(stainless))
    light1pos: tuple = (0, 0.33, 1.32)
    light1rot: tuple = (0, math.radians(20), math.radians(90))
    light1power: int = 10
    light2pos: tuple = (0, 0.42, 1.28)
    light2rot: tuple = (0, math.radians(20), math.radians(90))
    light2power: int = 10
    campos: tuple = (0, -0.3, 1.5)
    camrot: tuple = (0, 0, 0)


def fluctuate(vec: tuple, err_range: tuple, seed: int = 10) -> tuple:
    if len(vec) != len(err_range):
        raise ValueError("vector and range dimension should be same")

    return tuple(val + random.uniform(-err, err) for val, err in zip(vec, err_range))

def generate_options(num, seed = 10):
    random.seed(seed)
    optionlist = []
    for _ in range(num):
        render = RenderOptions()
        # render.water.basecolor = fluctuate(water.basecolor, (-0.1, -0.1, -0.1, 0))
        render.water.roughness = water.roughness + random.uniform(-0.02, 0.0)
        render.water.transmission = water.transmission + random.uniform(0, -0.01)
        render.water.IOR = water.IOR + random.uniform(-0.1, 0.1)

        render.stainless.basecolor = fluctuate(stainless.basecolor, (0.1, 0.1, 0.1, 0))
        render.stainless.metallic = stainless.metallic + random.uniform(-0.1, 0.09)

        render.light1pos = fluctuate((0, 0.33, 1.32), (0.05, 0.05, 0.05))
        render.light1power = 10 + random.uniform(-3, 3)
        render.light1rot = fluctuate((0, math.radians(20), math.radians(90)),  (math.radians(10), math.radians(10), math.radians(10)))

        render.light2pos = fluctuate((0, 0.42, 1.28), (0.05, 0.05, 0.05))
        render.light2power = 10 + random.uniform(-3, 3)
        render.light2rot = fluctuate((0, math.radians(20), math.radians(90)), (math.radians(10), math.radians(10), math.radians(10)))

        render.campos = fluctuate((0, -0.3, 1.5), (0.01, 0.01, 0))
        render.camrot = fluctuate((0, 0, 0), (math.radians(2), math.radians(2), math.radians(2)))

        optionlist.append(render)
    
    return optionlist

def generate_prefixes(n):
    alphabet = string.ascii_uppercase
    result = []
    i = 0
    while len(result) < n:
        prefix = ""
        temp = i
        while True:
            prefix = alphabet[temp % 26] + prefix
            temp = temp // 26 - 1
            if temp < 0:
                break
        result.append(prefix)
        i += 1
    return result

# Set up logging
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_log.txt")
logging.basicConfig(
    filename=log_path,
    filemode='w',  # or 'a' to append
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

################################################# RENDERER #################################################

CONFIG_PATH = "datagenerator.json"
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)["RenderProperties"]

option_num = config["RenderNum"]
optionlist = generate_options(option_num)
prefixlist = generate_prefixes(option_num)

sequence_path, out_fp, out_name = sys.argv[-3], sys.argv[-2], sys.argv[-1]

### Path Setting
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
plask_path = os.path.join(base_path, "models/plask.obj")
noise_path = os.path.join(base_path, "background/whitenoise.png")
world_path = os.path.join(base_path, "background/hospital_room_2.png")
fluid_path = os.path.join(sequence_path, "mesh")
impeller_path = os.path.join(sequence_path, "obj")


for prefix, option in zip(prefixlist, optionlist):
    # Log RenderOptions
    logging.info(f"Render prefix: {prefix}")
    logging.info(f"RenderOptions: {option}")

    # output path and name
    final_fp = os.path.join(out_fp, prefix + out_name)

    # empty file
    blend_fp = "blend/empty.blend"
    bpy.ops.wm.open_mainfile(filepath=blend_fp)

    # add on initiate
    bpy.ops.preferences.addon_enable(module="sequence_loader")

    #### Materials
    stainless = bpy.data.materials.new(name='stainless_1')
    stainless.use_nodes = True
    nodes = stainless.node_tree.nodes
    links = stainless.node_tree.links
    nodes.clear()
        # === Output ===
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    output_node.location = (600, 0)
        # === Principled BSDF ===
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf.location = (400, 0)
    bsdf.inputs['Base Color'].default_value = option.stainless.basecolor  # C0C0C0FF
    bsdf.inputs['Metallic'].default_value = option.stainless.metallic
        # === Color Ramp ===
    color_ramp = nodes.new(type='ShaderNodeValToRGB')
    color_ramp.location = (200, 0)
    color_ramp.color_ramp.elements[0].position = 0.472
    color_ramp.color_ramp.elements[0].color = (0, 0, 0, 1)
    color_ramp.color_ramp.elements[1].position = 0.91
    color_ramp.color_ramp.elements[1].color = (1, 1, 1, 1)
        # === Noise Texture 1 ===
    noise1 = nodes.new(type='ShaderNodeTexNoise')
    noise1.location = (-100, 100)
    noise1.inputs['Scale'].default_value = 4
    noise1.inputs['Detail'].default_value = 10
    noise1.inputs['Roughness'].default_value = 0.7
    noise1.inputs['Lacunarity'].default_value = 2
        # === Linear Light ===
    linear_light = nodes.new(type='ShaderNodeMixRGB')
    linear_light.location = (-400, 0)
    linear_light.blend_type = 'LINEAR_LIGHT'
    linear_light.inputs['Fac'].default_value = 0.5
    linear_light.use_clamp = True
        # === Noise Texture 2 ===
    noise2 = nodes.new(type='ShaderNodeTexNoise')
    noise2.location = (-600, -100)
    noise2.inputs['Scale'].default_value = 3
    noise2.inputs['Detail'].default_value = 10
    noise2.inputs['Roughness'].default_value = 0.5
    noise2.inputs['Lacunarity'].default_value = 2
        # === Mapping ===
    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.location = (-800, 0)
        # === Texture Coordinate ===
    tex_coord = nodes.new(type='ShaderNodeTexCoord')
    tex_coord.location = (-1000, 0)
        # === Links ===
    links.new(bsdf.outputs['BSDF'], output_node.inputs['Surface'])
    links.new(color_ramp.outputs['Color'], bsdf.inputs['Roughness'])
    links.new(noise1.outputs['Fac'], color_ramp.inputs['Fac'])
    links.new(linear_light.outputs['Color'], noise1.inputs['Vector'])
    links.new(mapping.outputs['Vector'], linear_light.inputs['Color1'])  # A
    links.new(noise2.outputs['Color'], linear_light.inputs['Color2'])    # B
    links.new(tex_coord.outputs['Object'], mapping.inputs['Vector'])

    glass = bpy.data.materials.new(name='glass_1')
    glass.use_nodes = True
    bsdf_glass = glass.node_tree.nodes["Principled BSDF"]
    bsdf_glass.inputs[0].default_value = option.glass.basecolor # Base Color
    bsdf_glass.inputs["IOR"].default_value = option.glass.IOR # IOR
    bsdf_glass.inputs["Roughness"].default_value = option.glass.roughness # Roughness
    bsdf_glass.inputs["Transmission Weight"].default_value = option.glass.transmission # Transmission Weight

    water = bpy.data.materials.new(name='water_1')
    water.use_nodes = True
    bsdf_water = water.node_tree.nodes["Principled BSDF"]
    bsdf_water.inputs[0].default_value = option.water.basecolor # Base Color
    bsdf_water.inputs["IOR"].default_value = option.water.IOR # IOR
    bsdf_water.inputs["Roughness"].default_value = option.water.roughness # Roughness
    bsdf_water.inputs["Transmission Weight"].default_value = option.water.transmission # Transmission

    whitenoise = bpy.data.materials.new(name='whitenoise_1')
    whitenoise.use_nodes = True
    image = bpy.data.images.load(noise_path)
    nodes = whitenoise.node_tree.nodes
    links = whitenoise.node_tree.links
    tex_image = nodes.new('ShaderNodeTexImage')
    tex_image.image = image
    bsdf = nodes["Principled BSDF"]
    links.new(tex_image.outputs['Color'], bsdf.inputs['Base Color'])
    bsdf.inputs[3].default_value = 1
    whitenoise.node_tree.nodes["Image Texture"].interpolation = 'Closest'


    #### World background setting
    if bpy.context.scene.world is None:
        bpy.context.scene.world = bpy.data.worlds.new("World")

    world = bpy.context.scene.world
    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links
    nodes.clear()
    bg_node = nodes.new(type='ShaderNodeBackground')
    env_tex_node = nodes.new(type='ShaderNodeTexEnvironment')
    output_node = nodes.new(type='ShaderNodeOutputWorld')
    env_tex_node.image = bpy.data.images.load(world_path)

    links.new(env_tex_node.outputs['Color'], bg_node.inputs['Color'])
    links.new(bg_node.outputs['Background'], output_node.inputs['Surface'])

    #### plask setting
    bpy.ops.wm.obj_import(filepath=plask_path)
    plask = bpy.context.active_object

    plask.data.materials.clear()
    plask.data.materials.append(glass)

    plask.rotation_euler = (0, 0, math.radians(90))
    plask.scale = (0.1, 0.1, 0.1)

    #### plane setting
    bpy.ops.mesh.primitive_plane_add(
        size=1,
        location=(0, 0, -0.05)
    )
    plane = bpy.context.active_object
    plane.scale = (2, 2, 2)

    plane.data.materials.clear()
    plane.data.materials.append(whitenoise)

    #### Camera setting
    bpy.ops.object.camera_add(location=option.campos, rotation=option.camrot)
    camera = bpy.context.active_object
    camera.data.lens = 80
    bpy.context.scene.camera = camera

    #### Light setting
    bpy.ops.object.light_add(type='SPOT', location=(0.74, 0.22, 4.0))
    light0 = bpy.context.active_object
    light0.data.energy = 100
    light0.rotation_euler = (math.radians(-14), math.radians(12), math.radians(1.52))
    light0.data.spot_size = math.radians(60)
    light0.data.cycles.max_bounces = 512

    bpy.ops.object.light_add(type='AREA', location=option.light1pos)
    light1 = bpy.context.active_object
    light1.data.shape = 'RECTANGLE'
    light1.rotation_euler = option.light1rot
    light1.data.size = 0.06
    light1.data.size_y = 0.258
    light1.data.energy = option.light1power
    light1.data.cycles.max_bounces = 512

    bpy.ops.object.light_add(type='AREA', location=option.light2pos)
    light2 = bpy.context.active_object
    light2.data.shape = 'RECTANGLE'
    light2.rotation_euler = option.light2rot
    light2.data.size = 0.06
    light2.data.size_y = 0.258
    light2.data.energy = option.light2power
    light2.data.cycles.max_bounces = 512

    ### Load fluid sequence
    bpy.context.scene.BSEQ.path = fluid_path
    bpy.context.scene.BSEQ.use_relative = False # or True if relative to .blend file
    bpy.context.scene.BSEQ.use_pattern = True
    bpy.context.scene.BSEQ.pattern = "ParticleData_Fluid_@.obj" # '@' is placeholder for frame numbers
    bpy.ops.sequence.load()

    fluid = bpy.context.view_layer.objects.active
    fluid.data.materials.append(water)
    fluid.rotation_euler = (math.radians(90), 0, 0)
    fluid.scale = (10, 10, 10)

    ### Load impeller sequence
    bpy.context.scene.BSEQ.path = impeller_path
    bpy.context.scene.BSEQ.use_relative = False # or True if relative to .blend file
    bpy.context.scene.BSEQ.use_pattern = True
    bpy.context.scene.BSEQ.pattern = "rb_data_1_@.obj" # '@' is placeholder for frame numbers
    bpy.ops.sequence.load()

    impeller = bpy.context.view_layer.objects.active
    impeller.data.materials.append(stainless)
    impeller.rotation_euler = (math.radians(90), 0, 0)
    impeller.scale = (10, 10, 10)

    #### Render Settings
    bpy.context.scene.render.engine = 'CYCLES'
    prefs = bpy.context.preferences
    cycles_prefs = prefs.addons["cycles"].preferences
    cycles_prefs.compute_device_type = "CUDA"
    cycles_prefs.get_devices()
    for dev in cycles_prefs.devices:
        dev.use = True
    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.filepath = final_fp
    bpy.context.scene.render.ffmpeg.codec  = 'H264'
    bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
    bpy.context.scene.render.ffmpeg.audio_codec = 'NONE'
    bpy.context.scene.cycles.use_progressive_refine = True
    bpy.context.scene.render.use_motion_blur = True
    bpy.context.scene.cycles.samples        = 32
    bpy.context.scene.render.resolution_x   = 224
    bpy.context.scene.render.resolution_y   = 224
    bpy.context.scene.frame_start           = 0
    bpy.context.scene.frame_end             = 32
    bpy.context.scene.frame_step            = 1
    bpy.context.scene.render.fps            = 10

    print(f"[INFO] Loading OBJ file for frame {bpy.context.scene.frame_current}")

    try:
        bpy.ops.render.render(animation=True)
        print(f"[INFO] Rendering completed, output to '{out_fp}'")
    except Exception as e:
        print(f"[ERROR] Render failed: {e}")




