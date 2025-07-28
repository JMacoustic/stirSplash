import pysplishsplash as sph
import os
import json
import pandas as pd
import numpy as np
import argparse
import random

CONFIG_PATH = "datagenerator.json"
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)["SimulProperties"]

SCENE_PATH = config["scene_path"]
PROPERTY_PATH = config["property_path"]
EXPORT_FPS = config["export_fps"]
DURATION = config["duration"]
T_CUT_POWER = config["t_cut_power"]
T_STOP_MOTOR = config["t_stop_motor"]
RPM_MIN = config["rpm_min"]
RPM_MAX = config["rpm_max"]
RPM_GRID = config["rpm_grid"]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--start', metavar='s', type=int)
parser.add_argument('--interval', metavar='m', type = int)

args = parser.parse_args()
start = args.start
end = start + args.interval

def rpm_sequence(rpm):
    omega_rad = 2 * np.pi * rpm / 60
    return [0,omega_rad, T_CUT_POWER, omega_rad, T_STOP_MOTOR, 0, DURATION, 0]

def run_sim_with_properties(density, surface_tension, xsph, target_rpm, sim_id, prop_id):
    # Load base scene
    with open(SCENE_PATH, 'r') as f:
        scene = json.load(f)

    # Modify properties
    scene["Configuration"]["density0"] = density
    scene["Materials"][0]["surfaceTension"] = surface_tension
    scene["Materials"][0]["xsph"] = xsph
    scene["Materials"][0]["xsphBoundary"] = xsph
    #scene["Materials"][0]["viscosity"] = viscosity

    # Convert rpm to angular velocity (rad/s)
    sequence = rpm_sequence(target_rpm)
    scene["TargetVelocityMotorHingeJoints"][0]["targetSequence"] = sequence

    #Random initial impeller angle
    scene["RigidBodies"][1]["rotationAngle"] = random.uniform(0, 2*3.14)

    # Save modified scene
    tmp_scene_path = f"temp_scene_{prop_id}{sim_id}.json"
    with open(tmp_scene_path, 'w') as f:
        json.dump(scene, f, indent=4)

    # Output folder
    padded_id = f"{prop_id:02d}{sim_id:02d}"  # e.g., "010001", "010002", ..., "500050", ...
    output_dir = os.path.abspath(f"./export/sim_{padded_id}")
    os.makedirs(output_dir, exist_ok=True)

    # Save config_000X.json
    config_dict = {
        "density": density,
        "surfaceTension": surface_tension,
        #"viscosity": viscosity,
        "xsph": xsph,
        "rpm": target_rpm
    }
    with open(os.path.join(output_dir, f"config_{padded_id}.json"), 'w') as f:
        json.dump(config_dict, f, indent=4)

    # Run simulation
    base = sph.Exec.SimulatorBase()
    base.init(useGui=False, outputDir=output_dir, sceneFile=os.path.abspath(tmp_scene_path))
    base.setValueFloat(base.STOP_AT, DURATION)
    base.activateExporter("VTK Exporter", True)
    base.activateExporter("Rigid Body OBJ Exporter", True)
    base.setValueFloat(base.DATA_EXPORT_FPS, EXPORT_FPS)
    base.run()

    os.remove(tmp_scene_path)


def main():
    df = pd.read_csv(PROPERTY_PATH)
    filtered_df = df.loc[start-1:end-1]
    rpm_values = np.linspace(RPM_MIN, RPM_MAX, RPM_GRID)  # 50 values from 320 to 500

    sim_id = 1
    prop_id = start

    for idx, row in filtered_df.iterrows():
        density = float(row["density"])
        surface_tension = float(row["surface tension"])
        xsph = float(row["xsph"])
        #viscosity = float(row["dynamic viscosity"])

        for rpm in rpm_values:
            run_sim_with_properties(density, surface_tension, xsph, rpm, sim_id=sim_id, prop_id=prop_id)
            sim_id += 1  # Keep sim_id unique for each config
        prop_id += 1
        sim_id = 1

if __name__ == "__main__":
    main()