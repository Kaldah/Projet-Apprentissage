import os
import shutil
import platform

def get_minecraft_saves_path():
    system = platform.system()
    home = os.path.expanduser("~")

    if system == "Windows":
        return os.path.join(home, "AppData", "Roaming", ".minecraft", "saves")
    elif system == "Darwin":  # macOS
        return os.path.join(home, "Library", "Application Support", "minecraft", "saves")
    elif system == "Linux":
        return os.path.join(home, ".minecraft", "saves")
    else:
        raise OSError("Unsupported operating system: " + system)

def copy_minecraft_map(map_name="JumpsIA", target_dir="maps"):
    try:
        source_path = os.path.join(get_minecraft_saves_path(), map_name)
    except OSError as e:
        print(f"❌ {e}")
        return

    project_root = os.path.dirname(os.path.abspath(__file__))
    dest_path = os.path.join(project_root, target_dir, map_name)

    if not os.path.exists(source_path):
        print(f"❌ Map '{map_name}' not found at: {source_path}")
        return

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    shutil.copytree(source_path, dest_path)
    print(f"✅ Map '{map_name}' successfully copied to: {dest_path}")

if __name__ == "__main__":
    copy_minecraft_map()
