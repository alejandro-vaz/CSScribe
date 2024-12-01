import os 
import sys
import shutil
import time

file_path = sys.argv[0]

def delete_directory_contents(directory):
    # Iterate over everything in the directory
    for filename in os.listdir(directory):
        paths = os.path.join(directory, filename)
        try:
            # If it's a directory, recursively delete its contents
            if os.path.isdir(paths):
                shutil.rmtree(paths)  # Deletes a directory and all its contents
            else:
                if paths != file_path:
                    os.remove(paths)  # Deletes a file
        except Exception as e:
            print(f"Error deleting {paths}: {e}")


dir_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print("FastMarkDown environment builder tool. Confirm the following data:")
time.sleep(1)
print(f"This file path is {file_path}.")
time.sleep(0.25)
print(f"This directory path is {dir_path}.")
if input("Is this correct? (y/n): ").lower() != "y":
    exit()

delete_directory_contents(dir_path)

with open(f"{dir_path}/.structure", "w", encoding="utf-8") as file:
    file.write("""project.pdf
├── portada.pdf
└── main.pdf
    └── main.md
        └── main.fmd
            ├── índice.fmd
            ├── introducción.fmd
            └── conclusión.fmd
project.pdf
├── Índice (#índice)
├── Introducción (#introducción)
│   ├── Análisis (#análisis)
│   └── Resumen (#resumen)
└── Conclusión (#conclusión)
./project/
├── .git
├── .structure
├── step-0/
│   └── project.pdf
├── step-1/
│   ├── portada.pdf
│   └── main.pdf
├── step-2/
│   ├── main.md
│   └── images/
│       ├── 1.png
│       ├── 2.png
│       ├── 3.png
│       └── jpegtopng.py
├── step-3/
│   ├── main.fmd
│   └── fmdcompiler.py
└── step-4/
    ├── índice.fmd
    ├── introducción.fmd
    └── conclusión.fmd
"""
    )

os.makedirs(os.path.join(dir_path, 'step-0'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-1'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-2'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-3'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-4'), exist_ok=True)  # Create a new directory

os.remove(file_path)