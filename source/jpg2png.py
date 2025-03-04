# NOT TRANSCRIBED YET
# IMPORT MODULES
import os
from PIL import Image

# FIND FUNCTION
def find_jpg_files(start_dir):
    jpg_files = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                full_path = os.path.join(root, file)
                jpg_files.append(full_path)
    return jpg_files

# CONVERT FUNCTION
def convert_file(file_path):
    try:
        img = Image.open(file_path)
        new_file = os.path.splitext(file_path)[0] + '.png'
        img.save(new_file, 'PNG')
        img.close()
        os.remove(file_path)
        print(f"Converted and deleted: {file_path}")
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")

# ENTRY POINT
if __name__ == "__main__":
    start_directory = os.getcwd()
    jpg_files = find_jpg_files(start_directory)
    
    if not jpg_files:
        print("No .jpg or .jpeg files found.")
    else:
        print("Found the following .jpg/.jpeg files:")
        for file in jpg_files:
            print(file)
        
        confirmation = input("Do you want to proceed with conversion? (y/n): ")
        if confirmation.lower() == 'y':
            for file in jpg_files:
                convert_file(file)
            print("Process complete.")
        else:
            print("Conversion cancelled.")
