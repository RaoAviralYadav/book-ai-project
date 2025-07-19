import json
import os
from datetime import datetime


VERSION_FILE = os.path.join(os.path.dirname(__file__), '..', 'storage', 'versions.json')

CHAPTER_DIR = os.path.join(os.path.dirname(__file__), '..', 'storage', 'chapters')


def load_versions():
    
    try:
        with open(VERSION_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_version(text, reward, chapter_name=None):
    
    os.makedirs(CHAPTER_DIR, exist_ok=True)

    
    timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    index = len(os.listdir(CHAPTER_DIR)) + 1
    safe_name = chapter_name.replace('/', '_').replace(' ', '_') if chapter_name else f'chapter_{index}'
    filename = f"{safe_name}_{timestamp}.txt"
    filepath = os.path.join(CHAPTER_DIR, filename)

    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

    
    versions = load_versions()
    entry = {
        'timestamp': timestamp,
        'filename': filename,
        'chapter': chapter_name or safe_name,
        'reward': reward
    }
    versions.append(entry)
    os.makedirs(os.path.dirname(VERSION_FILE), exist_ok=True)
    with open(VERSION_FILE, 'w', encoding='utf-8') as f:
        json.dump(versions, f, indent=2, ensure_ascii=False)

    return filename
