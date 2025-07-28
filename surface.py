import meshio
import numpy as np
import pysplashsurf
import glob
from os import path as osp
import os
import json
import shutil


CONFIG_PATH = "datagenerator.json"
with open(CONFIG_PATH, 'r') as f:
    config_mesh = json.load(f)["MeshProperties"]

RUST_BACKTRACE=config_mesh["rust_backtrace"]
START_FRAME=config_mesh["start_frame"]
END_FRAME=config_mesh["end_frame"]

main_dir = sorted(glob.glob(osp.join("export", "sim_*")))
config_repo = "configs"

for dataset in main_dir:
    name = osp.basename(osp.normpath(dataset))
    config = glob.glob(osp.join(dataset, "*.json"))[0]

    output_repo = osp.join("final_mesh", name)
    output_dir = osp.join(output_repo, "mesh")
    os.makedirs(output_dir, exist_ok=True)

    shutil.copy(config, osp.join(output_repo, f"{name}.json"))
    shutil.copy(config, osp.join(config_repo, f"{name}.json"))

    # rename the vtk_files
    vtk_files = sorted(glob.glob(osp.join(dataset, "vtk", "*.vtk")))
    for file_path in vtk_files:
        base = os.path.basename(file_path)
        dir_name = os.path.dirname(file_path)
        number_part = base.split('_')[-1].replace('.vtk', '')
        if number_part.isdigit():
            padded_number = f"{int(number_part):03d}"
            new_base = '_'.join(base.split('_')[:-1]) + f"_{padded_number}.vtk"
            new_path = os.path.join(dir_name, new_base)
            if base != new_base:
                if not os.path.exists(new_path):
                    os.rename(file_path, new_path)

    imp_files = sorted(glob.glob(osp.join(dataset, "obj", "rb_data_1_*.obj")))
    idx = 1
    for file_path in imp_files:
        base = os.path.basename(file_path)
        number_part = base.split('_')[-1].replace('.obj', '')

        if number_part.isdigit():
            frame_idx = int(number_part)
            if START_FRAME <= frame_idx <= END_FRAME:
                des_name = str.replace(os.path.dirname(file_path), "export", "final_mesh")
                print(des_name)
                os.makedirs(des_name, exist_ok=True)
                shutil.copy(file_path, os.path.join(des_name, base))

    vtk_files = sorted(glob.glob(osp.join(dataset, "vtk", "*.vtk")))
    idx = 1
    for file in vtk_files:
        if START_FRAME <= idx and END_FRAME >= idx:
            mesh = meshio.read(file)
            nan_mask = np.isnan(mesh.points)
            nan_indices = np.argwhere(nan_mask)
            print("NaN found at indices:", nan_indices)
            print("Full row(s):", mesh.points[nan_mask.any(axis=1)])

            particles = np.array(mesh.points, dtype=np.float32)

            if np.isnan(particles).any():
                print(f"{file} is corrupted")
                continue
            output_name, _ = osp.splitext(osp.basename(file))
            output_file = osp.join(output_dir, f"{output_name}.obj")

            mesh_with_data, reconstruction = pysplashsurf.reconstruction_pipeline(
                particles,
                particle_radius=config_mesh["particle_radius"],
                rest_density=config_mesh["rest_density"],
                smoothing_length=config_mesh["smoothing_length"],
                cube_size=config_mesh["cube_size"],
                iso_surface_threshold=config_mesh["iso_surface_threshold"],
                mesh_smoothing_weights=config_mesh["mesh_smoothing_weights"],
                mesh_smoothing_weights_normalization=config_mesh["mesh_smoothing_weights_normalization"],
                mesh_smoothing_iters=config_mesh["mesh_smoothing_iters"],
                normals_smoothing_iters=config_mesh["normals_smoothing_iters"],
                mesh_cleanup=config_mesh["mesh_cleanup"],
                compute_normals=config_mesh["compute_normals"],
                subdomain_grid=config_mesh["subdomain_grid"],
                subdomain_num_cubes_per_dim=config_mesh["subdomain_num_cubes_per_dim"],
                output_mesh_smoothing_weights=config_mesh["output_mesh_smoothing_weights"]
            )   
            pysplashsurf.write_to_file(mesh_with_data, output_file)
        idx += 1