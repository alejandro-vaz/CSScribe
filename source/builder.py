# IMPORT MODULES
import os 
import sys
import time

# DEFINE PATH
dir_path = os.getcwd()

# DEFINE VERSION
version = "4.4.13"

# DEFINE CONTENT
match sys.argv[1]:
    case "Español":
        structure_tree = """CSScribe {version}


# Fechas de finalización
{project}
├── step-0 = --/--/----
├── step-1 = --/--/----
├── step-2 = --/--/----
├── step-3 = --/--/----
└── step-4 = --/--/----


# Jerarquía de compilación
{project:raw}.pdf
└── main.pdf
    └── main.md
        └── main.cssc


# Jerarquía de encabezados


# Diagrama de árbol
https://{platform}/{username}/{project:raw}/tree/main/{images}
├── step-0/
├── step-1/
├── step-2/
├── step-3/
├── step-4/
└── structure.tree
"""
        step_0_todo = """Primero debes escribir todas las partes de tu documento final. Céntrate solo en escribir, más tarde tendrás tiempo para arreglar errores, o mejorar el estilo de tu proyecto. Al final de este paso deberás tener un boceto bastante avanzado de tu trabajo final, por lo que no harás grandes cambios en el futuro (como cambiar capítulos enteros).

1. Escribir todas las partes.
2. Actualizar constantemente structure.tree.
"""
        step_1_todo = """Ahora que has escrito todos los capítulos, tienes que unir cada documento individual en uno que los incluya todos. Cuando lo hayas hecho, introduce el archivo en el entorno, compílalo, conviértelo a PDF e imprímelo para corregir errores y parafrasear expresiones. Deberás también construir la bibliografía ahora. 

1. Unir todos los documentos en un archivo.
2. Compilar e imprimir el archivo en el entorno.
3. Arreglar errores.
4. Repetir desde 2 cuantas veces sea necesario.
5. Construir bibliografía.
"""
        step_2_todo = """Ahora arreglarás el estilo del proyecto. Añade los modificadores que quieras, como negrita, cursiva u otros. Puede que necesites volver a imprimir el archivo, aunque no es estrictamente necesario.

1. Añadir las referencias en el texto.
2. Añadir cursiva.
3. Añadir negrita.
4. Arregla todo lo demás.
"""
        step_3_todo = """Compilarás ahora la versión definitiva del proyecto. Consigue el archivo PDF. Añade también otros documentos PDF como portadas que luego unirás al tuyo.

1. Compila.
2. Añade archivos extra.
"""
        step_4_todo = """Junta ahora todos los documentos PDF con ILovePDF. A día de lanzamiento de esta versión, esta es la única aplicación que sirve para unir PDFs ya que es la única que mantiene el funcionamiento de los enlaces.
    
1. Visita https://www.ilovepdf.com/es/unir_pdf y une todo.
2. Añade otros recursos al proyecto que pueden ser de ayuda, como presentaciones.
"""
    case "English":
        structure_tree = """CSScribe {version}


# Completion dates
{project}
├── step-0 = --/--/----
├── step-1 = --/--/----
├── step-2 = --/--/----
├── step-3 = --/--/----
└── step-4 = --/--/----


# Compiling hierarchy
{project:raw}.pdf
└── main.pdf
    └── main.md
        └── main.cssc


# Headers hierarchy


# Tree diagram
https://{platform}/{username}/{project:raw}/tree/main/{images}
├── step-0/
├── step-1/
├── step-2/
├── step-3/
├── step-4/
└── structure.tree
"""
        step_0_todo = """First you must write all document parts. Focus only on writing, you'll have time to focus on error correcting, cleaning or making your project better by styling. At the end of this step you must have a fairly accurate sketch of the project you're working on, meaning major changes (like changing chapters) won't be done further.

1. Write all parts.
2. Constantly update the structure.tree file.
"""
        step_1_todo = """Now that you have written all the parts, you must join them in a single file. Once you have done that, it's time to take the file into the environment, convert it to a .pdf file and print it for error correcting and paraphrasing although that will not be the definitive version. You should also build the references now. Print and correct as many times as needed. 

1. Join all documents in a single file.
2. Add it to environment and print.
3. Fix mistakes.
4. Repeat from 2 as many times as necessary.
5. Build sources.
"""
        step_2_todo = """Now it's time to fix the style of the project. Add italic, bold, custom tags if needed, or any of the modifiers you haven't used. You might want to print the corrected version to do it again, but it's not strictly required.

1. Add citations in text.
2. Add italic.
3. Add bold.
4. Fix everything else you don't like.
"""
        step_3_todo = """Let's compile the file now for real. Run the compiler and the extension to get the PDF desired file. You might want to add extra files which will be inside the project like cover pages.

1. Compile.
2. Add extra files.
"""
        step_4_todo = """Now join all files via ILovePDF PDF joiner. As of the release date of this update, this the only valid joiner I know because it is the one which does maintain link functionality.

1. Go to https://www.ilovepdf.com/es/unir_pdf and join everything.
2. Add extra resources to the project that might be useful, like presentations.
"""

# FUNCTIONS
def tree(images):
    os.makedirs(os.path.join(dir_path, 'env'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-0'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-1'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-2'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-3'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-4'), exist_ok=True)
    if images:
        os.makedirs(os.path.join(dir_path, 'images'), exist_ok=True)

def structure(project_name, platform, username, images):
    content = structure_tree
    project_raw = (project_name.lower()).replace(" ", "-")
    content  = content.replace("{project}", project_name)
    content = content.replace("{project:raw}", project_raw)
    content = content.replace("{platform}",  platform)
    content = content.replace("{username}", username)
    content = content.replace("{version}", version)
    if images:
        content = content.replace("{images}", "\n├── images/")
    else:
        content = content.replace("{images}", "")
    with open(f"{dir_path}/structure.tree", "w", encoding="utf-8") as file: file.write(content)

def todos(i_todos):
    if i_todos:
        with open(os.path.join(dir_path, 'step-0/.todo'), 'w', encoding='utf-8') as step: step.write(step_0_todo)
        with open(os.path.join(dir_path, 'step-1/.todo'), 'w', encoding='utf-8') as step: step.write(step_1_todo)
        with open(os.path.join(dir_path, 'step-2/.todo'), 'w', encoding='utf-8') as step: step.write(step_2_todo)
        with open(os.path.join(dir_path, 'step-3/.todo'), 'w', encoding='utf-8') as step: step.write(step_3_todo)
        with open(os.path.join(dir_path, 'step-4/.todo'), 'w', encoding='utf-8') as step: step.write(step_4_todo)

if __name__ == "__main__":
    # DEFINE LINES
    match sys.argv[1]:
        case "Español":
            answer_correct = "s"
            line_greeting = "Herramienta de construcción de entornos de CSScribe. Confirma los siguientes datos."
            line_path = f"Este directorio es {dir_path}\n"
            question_path = "¿Es la ruta del directorio correcta? (s/n)                                 "
            question_image = "¿Quieres añadir soporte para imágenes? (s/n)                               "
            question_todo = "¿Quieres incluir archivos .todo de guía? (s/n):                            "
            question_project = "Introduce el nombre del proyecto:                                          "
            question_platform = "Introduce el enlace de la plataforma de almacenamiento de archivos:        "
            question_username = "Introduce tu nombre de usuario en la plataforma:                           "
        case "English":
            answer_correct = "y"
            line_greeting = "CSScribe environment builder tool. Confirm the following data."
            line_path = f"This directory is {dir_path}\n"
            question_path = "Is the path correct? (y/n):                                         "
            question_image = "Do you want image support? (y/n):                                          "
            question_todo = "Do you want to add .todo files? (y/n):                                     "
            question_project = "Enter the project name:                                                    "
            question_platform = "Enter the file-sharing platform link:                                      "
            question_username = "Enter the creator file-sharing username:                                   "
    # MAIN CODE
    print(line_greeting)
    time.sleep(0.75)
    print(line_path)
    if input(question_path).lower() != answer_correct:
        exit()
    image_support = input(question_image).lower() == answer_correct
    add_todos = input(question_todo).lower() == answer_correct
    project_name = input(question_project)
    file_platform = input(question_platform)
    username = input(question_username)
    tree(image_support)
    structure(project_name, file_platform, username, image_support)
    todos(add_todos)