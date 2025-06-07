import os
import hashlib
import json

# Set the path to monitor
FOLDER_TO_MONITOR = "path/to/your/folder"  # Change this to your target directory
HASH_FILE = "file_hashes.json"

def calculate_hash(filepath):
    """Calculate SHA-256 hash of a file"""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_files(directory):
    """Scan all files in directory and return hash dictionary"""
    hash_dict = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = calculate_hash(filepath)
            if file_hash:
                hash_dict[filepath] = file_hash
    return hash_dict

def load_previous_hashes():
    """Load previous file hashes from JSON file"""
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hash_dict):
    """Save current file hashes to JSON file"""
    with open(HASH_FILE, 'w') as f:
        json.dump(hash_dict, f, indent=4)

def check_integrity():
    """Compare current and previous hashes and detect changes"""
    previous_hashes = load_previous_hashes()
    current_hashes = scan_files(FOLDER_TO_MONITOR)

    modified = []
    deleted = []
    new = []

    for filepath, hash_value in current_hashes.items():
        if filepath not in previous_hashes:
            new.append(filepath)
        elif previous_hashes[filepath] != hash_value:
            modified.append(filepath)

    for filepath in previous_hashes:
        if filepath not in current_hashes:
            deleted.append(filepath)

    print("\n🔍 Integrity Check Report:")
    if modified:
        print("📝 Modified Files:")
        for f in modified:
            print(f" - {f}")
    if new:
        print("🆕 New Files:")
        for f in new:
            print(f" - {f}")
    if deleted:
        print("❌ Deleted Files:")
        for f in deleted:
            print(f" - {f}")
    if not (modified or new or deleted):
        print("✅ No changes detected.")

    save_hashes(current_hashes)

# Run the checker
if __name__ == "__main__":
    check_integrity()
