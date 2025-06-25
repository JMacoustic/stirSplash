import pysplishsplash as sph
from pysplishsplash.Extras import Scenes
import os

def main():
    base = sph.Exec.SimulatorBase()
    output_dir = os.path.abspath("./export/")
    custom_scene = os.path.abspath("data/Scenes/Impeller.json")

    base.init(useGui=False, outputDir=output_dir, sceneFile=custom_scene)
    base.setValueFloat(base.STOP_AT, 10.0) # Important to have the dot to denote a float
    base.activateExporter("VTK Exporter", True)
    # Uncomment the next line to set the output FPS value (must be float)
    base.setValueFloat(base.DATA_EXPORT_FPS, 24.) 
    base.run()

if __name__ == "__main__":
    main()