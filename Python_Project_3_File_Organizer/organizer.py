import os
import shutil

# Set your source folder (e.g., Downloads folder)
source_folder = os.path.expanduser("~/Downloads")  # change if needed

# Define file type categories
file_types = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar'],
    'Scripts': ['.py', '.js', '.html']
}

# Organize files
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                dest_folder = os.path.join(source_folder, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved {filename} → {folder}")
                break

