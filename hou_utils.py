import hou
import os

def save_curr_scene(scene_path):
    if not os.path.exists(scene_path):
        hou.hipFile.save(scene_path)
        hou.ui.displayMessage("scene has been created!")
    else:
        hou.ui.displayMessage("scene already exists!")