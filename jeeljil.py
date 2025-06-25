import pysplishsplash as sph
import os
import json
import pandas as pd
import numpy as np


def rpm_to_rad_per_sec(rpm):
    return 2 * np.pi * rpm / 60

def run_sim_with_properties(density, surface_tension, viscosity, target_rpm, sim_id):
    # Load base scene
    with open("data/Scenes/Impeller.json", 'r') as f:
        scene = json.load(f)

    # Modify properties
    scene["Configuration"]["density0"] = density
    scene["Materials"][0]["surfaceTension"] = surface_tension
    scene["Materials"][0]["viscosity"] = viscosity

    # Convert rpm to angular velocity (rad/s)
    angular_velocity = -rpm_to_rad_per_sec(target_rpm)
    scene["TargetVelocityMotorHingeJoints"][0]["target"] = angular_velocity

    # Save modified scene
    tmp_scene_path = f"temp_scene_{sim_id}.json"
    with open(tmp_scene_path, 'w') as f:
        json.dump(scene, f, indent=4)

    # Output folder
    padded_id = f"{sim_id:04d}"  # e.g., "0000", "0001", ..., "0149"
    output_dir = os.path.abspath(f"./export/sim_{padded_id}")
    os.makedirs(output_dir, exist_ok=True)

    # Save config_000X.json
    config_dict = {
        "density": density,
        "surfaceTension": surface_tension,
        "viscosity": viscosity,
        "rpm": target_rpm
    }
    with open(os.path.join(output_dir, f"config_{padded_id}.json"), 'w') as f:
        json.dump(config_dict, f, indent=4)

    # Run simulation
    base = sph.Exec.SimulatorBase()
    base.init(useGui=False, outputDir=output_dir, sceneFile=os.path.abspath(tmp_scene_path))
    base.setValueFloat(base.STOP_AT, 10.0)
    base.activateExporter("VTK Exporter", True)
    base.setValueFloat(base.DATA_EXPORT_FPS, 10.0)
    base.run()

    os.remove(tmp_scene_path)


def main():
    df = pd.read_csv("./data/property/waterglycerin_50points.csv")
    rpm_values = np.linspace(325, 550, 50)  # 50 values from 10 to 20 inclusive

    sim_id = 1
    for idx, row in df.iterrows():
        density = float(row["density"])
        surface_tension = float(row["surface tension"])
        viscosity = float(row["dynamic viscosity"])

        for rpm in rpm_values:
            run_sim_with_properties(density, surface_tension, viscosity, rpm, sim_id=sim_id)
            sim_id += 1  # Keep sim_id unique for each config


if __name__ == "__main__":
    main()