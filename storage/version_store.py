import json
import os
from datetime import datetime

VERSION_FILE = os.path.join(os.path.dirname(__file__), '..', 'storage', 'versions.json')

def load_versions():
    """Load saved versions from JSON file."""
    try:
        with open(VERSION_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_version(text, reward):
    """Append a new version with timestamp and reward to the versions file."""
    versions = load_versions()
    entry = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'content': text,
        'reward': reward
    }
    versions.append(entry)
    os.makedirs(os.path.dirname(VERSION_FILE), exist_ok=True)
    with open(VERSION_FILE, 'w', encoding='utf-8') as f:
        json.dump(versions, f, indent=2, ensure_ascii=False)

