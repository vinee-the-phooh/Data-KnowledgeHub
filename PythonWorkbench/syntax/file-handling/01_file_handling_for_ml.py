#create_directory : ensures folder exists
#generate_timestamped_filename : avoids overwriting
#create_timestamped_file : creates uniquely named file
#create_if_missing : safe file creation

import os
import json
import csv
import pickle
import pandas as pd
from datetime import datetime

#1. Create directory if it doesn't exist
def create_directory(path):
    """Creates a folder if it doesn't already exist."""
    os.makedirs(path, exist_ok=True)

#2. Generate timestamped filename
def generate_timestamped_filename(prefix="file", extension=".txt"):
    """Returns a filename like 'file_2025-04-13_21-18-00.txt'."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{prefix}_{timestamp}{extension}"

#3. Create file with timestamped name
def create_timestamped_file(directory, prefix="file", extension=".txt", content=""):
    """Creates a new file with a timestamped name inside a given folder."""
    create_directory(directory)
    filename = generate_timestamped_filename(prefix, extension)
    path = os.path.join(directory, filename)
    with open(path, "w") as f:
        f.write(content)
    return path  # Return full path for reference

#4. Create file if missing
def create_if_missing(path, content=""):
    """Creates a file only if it doesn't exist."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(content)

#5. Read file
def read_file(path):
    """Reads and returns the content of a text file."""
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return None

#6. Append to file
def append_to_file(path, content):
    """Appends content to an existing file."""
    with open(path, "a") as f:
        f.write(content)

#7. Check file existence
def file_exists(path):
    """Checks if a file exists at the given path."""
    return os.path.exists(path)

#8. Delete file
def delete_file(path):
    """Deletes a file if it exists."""
    if os.path.exists(path):
        os.remove(path)

#9. Rename file
def rename_file(old_path, new_path):
    """Renames a file from old_path to new_path."""
    if os.path.exists(old_path):
        os.rename(old_path, new_path)

#10. Read CSV
def read_csv(path):
    """Reads a CSV file into a DataFrame."""
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

#11. Write CSV
def write_csv(path, data, headers=None):
    """Writes rows of data to a CSV file."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)

#12. Save JSON
def save_json(path, obj):
    """Saves a dictionary or list to a JSON file."""
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

#13. Load JSON
def load_json(path):
    """Loads and returns data from a JSON file."""
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None


# What I have learned:
#I use timestamped filenames to avoid overwriting logs or outputs. I also make sure directories exist before saving files, which makes my code robust and reusable.