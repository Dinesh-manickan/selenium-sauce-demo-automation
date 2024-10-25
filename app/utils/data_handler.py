import json
import os


def save_json(filepath, data):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving JSON to {filepath}: {e}")


def read_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filepath}.")
    except Exception as e:
        print(f"Error reading JSON from {filepath}: {e}")
    return {}
