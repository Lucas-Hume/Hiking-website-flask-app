import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "trails.json")

def get_upcoming_trails():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
