import os
import shutil
import platform
from pathlib import Path

def get_minecraft_saves_path():
    system = platform.system()
    user_home = Path.home()

    if system == "Windows":
        return user_home / "AppData" / "Roaming" / ".minecraft" / "saves"
    elif system == "Darwin":  # macOS
        return user_home / "Library" / "Application Support" / "minecraft" / "saves"
    elif system == "Linux":
        return user_home / ".minecraft" / "saves"
    else:
        raise OSError("Unsupported OS")

def export_map(map_name="JumpsIA", target_dir="maps"):
    saves_path = get_minecraft_saves_path()
    source_map_path = saves_path / map_name
    dest_map_path = Path(target_dir) / map_name

    if not source_map_path.exists():
        print(f"Error: Map '{map_name}' not found at {source_map_path}")
        return

    if dest_map_path.exists():
        print(f"Overwriting existing map at {dest_map_path}...")
        shutil.rmtree(dest_map_path)

    shutil.copytree(source_map_path, dest_map_path)
    print(f"Map '{map_name}' successfully exported to '{dest_map_path}'.")

if __name__ == "__main__":
    export_map()
