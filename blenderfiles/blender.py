bpy.context.area.ui_type = 'INFO'
bpy.ops.object.delete(use_global=False, confirm=False)
Deleted 1 object(s)
bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
bpy.ops.object.editmode_toggle()
bpy.ops.transform.resize(value=(0.7, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
bpy.ops.transform.resize(value=(1, 0.7, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
bpy.ops.mesh.inset(thickness=0.07, depth=0)
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 3.55271e-15, -0.9), "orient_type":'NORMAL', "orient_matrix":((0.290285, 0.95694, -1.83245e-08), (-0.95694, 0.290285, 6.04076e-08), (6.31258e-08, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(-1.77636e-15, 7.10543e-15, -0.95), "orient_type":'NORMAL', "orient_matrix":((0.290285, 0.95694, -1.83245e-08), (-0.95694, 0.290285, 6.04076e-08), (6.31258e-08, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.params.filename = "renderstir.blend"
Saved "renderstir.blend"
bpy.ops.material.new()
bpy.ops.object.editmode_toggle()
bpy.ops.object.editmode_toggle()
bpy.data.materials["Material.001"].node_tree.nodes["Principled BSDF"].inputs[4].default_value = 1.4
bpy.data.materials["Material.001"].node_tree.nodes["Principled BSDF"].inputs[16].default_value = 1.2
bpy.data.materials["Material.001"].node_tree.nodes["Principled BSDF"].inputs[17].default_value = 0.973
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(830, 262))
bpy.context.object.active_material.name = "glass"
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(915, 258))
bpy.ops.material.new()
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(967, 166))
bpy.ops.node.add_node(use_transform=True, type="ShaderNodeTexImage")
bpy.ops.node.translate_attach_remove_on_cancel(TRANSFORM_OT_translate={"value":(-531.535, -44.5699, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":True, "view2d_edge_pan":True, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False}, NODE_OT_attach={})
bpy.ops.node.link(detach=False, drag_start=(-77.4272, 270.287))
bpy.ops.image.open(filepath="//hospital_room_2.png", directory="C:\\Users\\user\\fluidsim\\", files=[{"name":"hospital_room_2.png", "name":"hospital_room_2.png"}], relative_path=True, show_multiview=False)
bpy.ops.image.open(filepath="//whitenoise.png", directory="C:\\Users\\user\\fluidsim\\", files=[{"name":"whitenoise.png", "name":"whitenoise.png"}], show_multiview=False)
bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[16].default_value = 1.5
bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[15].default_value = 0.5
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(979, 139))
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(990, 248))
bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[15].default_value = 0.5
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(978, 253))
bpy.context.object.active_material.name = "whitenoise"
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(1012, 84))
bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[15].default_value = 0.0163636
bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[15].default_value = 0
bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[17].default_value = 0
bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[18].default_value = 0
bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0
bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[14].default_value = 0
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(861, 220))
bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[14].default_value = 0
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(887, 244))
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(847, 245))
bpy.context.space_data.shading.type = 'RENDERED'
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(447, 316))
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(473, 343))
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(867, 184))
bpy.ops.material.new()
bpy.context.object.active_material.name = "glass.001"
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(486, 292))
bpy.ops.node.hide_toggle()
bpy.ops.node.hide_toggle()
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(505, 260))
bpy.ops.node.add_node(use_transform=True, type="ShaderNodeBsdfGlass")
bpy.ops.node.translate_attach_remove_on_cancel(TRANSFORM_OT_translate={"value":(-376.875, -148.635, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":True, "view2d_edge_pan":True, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False}, NODE_OT_attach={})
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(790, 357))
bpy.ops.node.link(detach=False, drag_start=(249.042, 266.104))
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(834, 337))
bpy.ops.node.link(detach=False, drag_start=(296.693, 244.405))
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(834, 336))
bpy.ops.node.link(detach=False, drag_start=(296.693, 243.383))
bpy.context.space_data.context = 'RENDER'
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(835, 337))
bpy.ops.node.link(detach=False, drag_start=(297.776, 244.468))
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(789, 355))
bpy.ops.node.link(detach=False, drag_start=(247.959, 263.996))
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[13].default_value = 0
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(889, 160))
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[20].default_value = 0
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(942, 247))
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(975, 150))
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (0, 0, 0, 1)
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[20].default_value = 0.1
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[20].default_value = 0
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0.759091
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0.1
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0.3
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0.5
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.context.space_data.context = 'DATA'
bpy.context.object.data.energy = 5000
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 1
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[20].default_value = 0.5
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(962, 233))
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[20].default_value = 1
bpy.ops.node.select(deselect_all=True, select_passthrough=True, location=(948, 110))
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[20].default_value = 0.1
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0.7
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0.2
bpy.data.materials["glass.001"].node_tree.nodes["Principled BSDF"].inputs[21].default_value = 0.3
Saved "renderstir.blend"
