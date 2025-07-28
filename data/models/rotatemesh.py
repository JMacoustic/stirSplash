import numpy as np
import os
import json
import trimesh

"""Export rotated impeller .obj frames based on scene file and angular velocity sequence."""
    # === Get impeller rigid body (id=1) ===
geometry_path = "data/models/impeller_rotated.obj"


    # === Load mesh ===
mesh = trimesh.load(geometry_path, force='mesh')

    # Apply translation
    

    # Apply initial rotation
R_init = trimesh.transformations.rotation_matrix(
    angle=-1.57079632,
    direction=[1, 0, 0],
    point=[0, 0, 0]
)
mesh.apply_transform(R_init)


    # Output folder
output_dir = os.path.abspath(f"data/models/rotated_temp.obj")
mesh.export(output_dir)
    # === Compute cumulative angles ===
