import json
from pathlib import Path

def load_course_config(course_id):
    config_path = Path("courses") / f"{course_id}.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Course config '{config_path}' not found.")
    
    with open(config_path, "r") as f:
        return json.load(f)
