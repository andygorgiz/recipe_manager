import json
from config.settings import DATA_PATH

def load_recipes():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_recipes(recipes):
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(recipes, file, ensure_ascii=False)