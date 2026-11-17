import os
import shutil

folder = os.path.join(os.path.expanduser("~"), "Downloads")
print(f"Cleaning: {folder}")

types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Zips": [".zip", ".rar"]
}

for file in os.listdir(folder):
    filepath = os.path.join(folder, file)
    if os.path.isfile(filepath):
        ext = os.path.splitext(file)[1].lower()
        for category, exts in types.items():
            if ext in exts:
                new_folder = os.path.join(folder, category)
                os.makedirs(new_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(new_folder, file))
                print(f"Moved {file} -> {category}")
                break

print("Done! Folder Cleaned.")