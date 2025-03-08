# IMPORT MODULES
import os
from PIL import Image
import sys

# DEFINE LANGUAGES
match sys.argv[1]:
    case "Español":
        line_converted = "Convertido y eliminado:                                                    "
        line_failed = "No se pudo convertir:                                                      "
        line_none = "Ningún archivo .jpg o .jpeg encontrado."
        line_found = "Se han encontrado los siguientes archivos:                                 "
        question_proceed = "¿Quieres continuar con la conversión? (y/n):                               "
        line_complete = "Proceso completado."
        line_cancelled = "Conversión cancelada."
    case "English":
        line_converted = "Converted and deleted:                                                     "
        line_failed = "Failed to convert:                                                         "
        line_none = "No .jpg or .jpeg files found."
        line_found = "Found the following .jpg/.jpeg files:                                      "
        question_proceed = "Do you want to proceed with conversion? (y/n):                             "
        line_complete = "Process complete."
        line_cancelled = "Conversion cancelled."

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
        print(f"{line_converted}{file_path}")
    except Exception as e:
        print(f"{line_failed}{file_path}: {e}")

# ENTRY POINT
if __name__ == "__main__":
    start_directory = os.getcwd()
    jpg_files = find_jpg_files(start_directory)
    if not jpg_files:
        print(line_none)
    else:
        print(line_found)
        for file in jpg_files:
            print(file)
        confirmation = input(question_proceed)
        if confirmation.lower() == 'y':
            for file in jpg_files:
                convert_file(file)
            print(line_complete)
        else:
            print(line_cancelled)
