import os, logging, json

def load_tools_from_json(json_path):
    """Load tools from a JSON file."""
    try:
        with open(json_path, 'r') as file:
            return json.load(file)['list']
    except Exception as e:
        logging.error(f"Error loading JSON from {json_path}: {e}")
        return []


def save_tools_to_json(tools, json_path):
    """Save tools to a JSON file."""
    try:
        with open(json_path, 'w') as file:
            json.dump({"count": len(tools), "list": tools}, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving tools to JSON {json_path}: {e}")
