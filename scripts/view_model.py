import mujoco
import mujoco.viewer
import os

# --- Configuration ---
# The name of the MJCF file you created
model_filename = '../ur3_onrobot_rg2_model/ur3_onrobot_rg2.xml'

# --- Script ---
# Get the full path to the model file
# This makes sure the script can find the file, no matter where you run it from
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, model_filename)

try:
    # Load the model
    model = mujoco.MjModel.from_xml_path(model_path)

    # Create the data object
    data = mujoco.MjData(model)

    print(f"Model '{model_filename}' loaded successfully. Launching viewer...")

    # Launch the interactive viewer
    mujoco.viewer.launch(model, data)

except Exception as e:
    print(f"Failed to load model and launch viewer: {e}")