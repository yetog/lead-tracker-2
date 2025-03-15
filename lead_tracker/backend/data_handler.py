import json
import os

DATA_FILE = "data/leads.json"

def load_leads():
    """Load leads from a JSON file."""
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        save_leads([])  # Reset to an empty list
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        save_leads([])  # Fix corrupted file
        return []

def save_leads(leads):
    """Save leads to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(leads, file, indent=4)
