import os 
import sys
import shutil
import time

file_path = sys.argv[0]
dir_path = os.path.dirname(os.path.abspath(sys.argv[0]))

structure_content = """CSScribe 3.1.3


# Factual completion dates
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
https://{platform}/{username}/{project:raw}/tree/main/
├── step-0/
├── step-1/
├── step-2/
├── step-3/
├── step-4/
└── .structure

"""

step_0_todo = """First you must write all document parts. Focus only on writing, you'll have time to focus on error correcting, cleaning or making your project better by styling. At the end of this step you must have a fairly accurate sketch of the project you're working on, meaning major changes (like changing chapters) won't be done further.

1. Write all parts.
2. Constantly update the .structure file."""

step_1_todo = """Now that you have written all the parts, you must join them in a single file. Once you have done that, it's time to take the file into the environment, convert it to a .pdf file and print it for error correcting and paraphrasing. You should also build the sources now. Print and correct as many times as needed. 

1. Join all documents in a single file.
2. Add it to environment and print.
3. Fix mistakes.
4. Repeat from 2 as many times as necessary.
5. Build sources."""

step_2_todo = """Now it's time to fix the style of the project. Add italic, bold, custom tags if needed, or any of the modifiers you haven't used. You might want to print the corrected version to do it again, but it's not strictly required.

1. Add citations.
2. Add italic.
3. Add bold.
4. Fix everything else you don't like."""

step_3_todo = """Let's compile the file now for real. Run the compiler and the extension to get the PDF desired file. You might want to add extra files which will be inside the project like cover pages.

1. Compile.
2. Add extra files."""

step_4_todo = """Now join all files via ILovePDF PDF joiner. As of the release date of this update, this the only valid joiner I know because it is the one which does maintain link functionality.

1. Go to https://www.ilovepdf.com/es/unir_pdf and join everything.
2. Add extra resources to the project that might be useful, like presentations or related projects."""

compiler = """import time
from si_prefix import si_format
def cssctomd(filename):
    def format_power(data):
        data = data.replace("#>", "<!--") # Comment start
        data = data.replace("<#", "-->") # Comment end
        data = data.replace("/h1", "#") # Header
        data = data.replace("/h2", "##") # Chapter
        data = data.replace("/h3", "###") # Section
        return data 
    def format_list(data):
        data = data.replace("    o ", "1. ") # Ordered list
        data = data.replace("    u ", "   - ") # Unordered list
        return data
    def replace_definition(data):
        data = data.replace("/>", ">") # Side comment
        return data
    def include_checkbox(data):
        data = data.replace("/O", "- [ ]") # Void checkbox
        data = data.replace("/X", "- [X]") # Done checkbox
        return data
    def convert_code(data):
        data = data.replace("/code-", "```") # Code start
        data = data.replace("/code", "```") # Code end
        data = data.replace("/cd", "`") # Inline code
        data = data.replace("/math", "$$") # Math block
        data = data.replace("/_", "$") # Inline math
        return data
    def add_images(data):
        count = 1
        while "/img" in data:
            data = data.replace("/img", f"![Relative](/images/{count}.png)", 1) # Add image
            count += 1
        return data
    def replace_style(data):
        data = data.replace("/n", "\\n") # New paragraph
        data = data.replace("·", "*") # Italic
        data = data.replace("/-", "~~") # Strikethrough
        data = data.replace("/s", "~") # Subscript
        data = data.replace("/S", "^") # Superscript
        data = data.replace("\\'", "**") # Bold
        data = data.replace("****", "\\'") # Double single-quote scape
        return data
    def replace_ctags(data):
        data = data.replace("/pbba", "<pbba></pbba>") # page-break-before: avoid
        data = data.replace("/In", "<index>") # Index page number start
        data = data.replace("/in", "</index>") # Index page number end
        data = data.replace("/br", "<br>") # Line break
        data = data.replace("¬", "") # Scape character
        return data
    
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        content = format_power(content)
        content = format_list(content)
        content = replace_definition(content)
        content = include_checkbox(content)
        content = convert_code(content)
        content = add_images(content)
        content = replace_style(content)
        content = replace_ctags(content)
    return content

if __name__ == "__main__":
    filename = input("Name of file without extension: ")
    cssc_file = f"{filename}.cssc"
    md_file = f"{filename}.md"
    start_time = time.time()
    try:
        with open(md_file, 'w', encoding="utf-8") as file:
            file.write(cssctomd(cssc_file))
        end_time = time.time()
        print(f"Conversion done in {si_format(end_time - start_time, precision=2)}s")
    except Exception as e:
        print(F"Error during conversion: \\n{e}")
    input("")
"""

jpegtopng = """import os
from PIL import Image

# Change the working directory to the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Get the list of all files in the current directory
files = os.listdir()

# Loop through each file in the directory
for file_name in files:
    # Check if the file is a JPEG file
    if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
        try:
            # Open the image using PIL
            img = Image.open(file_name)
            
            # Convert the file name to PNG format
            png_file_name = file_name.rsplit('.', 1)[0] + '.png'
            
            # Save the image in PNG format
            img.save(png_file_name, 'PNG')
            
            # Close the image file
            img.close()
            
            # Delete the original JPEG file
            os.remove(file_name)
            
            print(f"Converted and deleted: {file_name}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")

print("Process complete.")
input()"""

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

def init():
    print("CSScribe environment builder tool. Confirm the following data:")
    time.sleep(1)
    print(f"This file path is {file_path}")
    time.sleep(0.25)
    print(f"This directory path is {dir_path}")
    if input("Is this correct? (y/n): ").lower() != "y":
        exit()

def restructure(i_environment, i_images):
    delete_directory_contents(dir_path)
    if i_environment:
        os.makedirs(os.path.join(dir_path, 'env'), exist_ok=True)  # Create a new directory
        if i_images:
            os.makedirs(os.path.join(dir_path, 'env/images'), exist_ok=True)  # Create a new directory
    os.makedirs(os.path.join(dir_path, 'step-0'), exist_ok=True)  # Create a new directory
    os.makedirs(os.path.join(dir_path, 'step-1'), exist_ok=True)  # Create a new directory
    os.makedirs(os.path.join(dir_path, 'step-2'), exist_ok=True)  # Create a new directory
    if i_images:
        os.makedirs(os.path.join(dir_path, 'step-3/images'), exist_ok=True)  # Create a new directory
    os.makedirs(os.path.join(dir_path, 'step-3'), exist_ok=True)  # Create a new directory
    os.makedirs(os.path.join(dir_path, 'step-4'), exist_ok=True)  # Create a new directory

def structure(i_estpname, i_estplatform, i_estusername):
    content = structure_content
    i_estpnameraw = (i_estpname.lower()).replace(" ", "-")
    content  = content.replace("{project}", i_estpname)
    content = content.replace("{project:raw}", i_estpnameraw)
    content = content.replace("{platform}", i_estplatform)
    content = content.replace("{username}", i_estusername)
    with open(f"{dir_path}/.structure", "w", encoding="utf-8") as file: file.write(content)

def todos(i_todos):
    if i_todos:
        with open(os.path.join(dir_path, 'step-0/.todo'), 'w', encoding='utf-8') as step: step.write(step_0_todo)
        with open(os.path.join(dir_path, 'step-1/.todo'), 'w', encoding='utf-8') as step: step.write(step_1_todo)
        with open(os.path.join(dir_path, 'step-2/.todo'), 'w', encoding='utf-8') as step: step.write(step_2_todo)
        with open(os.path.join(dir_path, 'step-3/.todo'), 'w', encoding='utf-8') as step: step.write(step_3_todo)
        with open(os.path.join(dir_path, 'step-4/.todo'), 'w', encoding='utf-8') as step: step.write(step_4_todo)

def compilers(i_environment):
    with open(os.path.join(dir_path, 'step-3/compiler.py'), "w", encoding="utf-8") as step: step.write(compiler)
    if i_environment:
        with open(os.path.join(dir_path, 'env/compiler.py'), "w", encoding="utf-8") as step: step.write(compiler)

def converters(i_environment):
    with open(os.path.join(dir_path, 'step-3/images/jpegtopng.py'), "w", encoding='utf-8') as step: step.write(jpegtopng)
    if i_environment:
        with open(os.path.join(dir_path, 'env/images/jpegtopng.py'), "w", encoding='utf-8') as step: step.write(jpegtopng)

def end():
    os.system(f'code "{dir_path}"')

if __name__ == "__main__":
    init()
    f_environment = input("Do you want to include a testing environment? (y/n): ").lower() == "y"
    f_images = input("Do you want image support? (y/n): ").lower() == "y"
    f_todos = input("Do you want to add .todo guide files? (y/n): ").lower() == "y"
    f_estpname = input("Enter the project name: ")
    f_estplatform = input("Enter the file-sharing platform link: ")
    f_estusername = input("Enter the creator's file-sharing username: ")
    restructure(f_environment, f_images)
    structure(f_estpname, f_estplatform, f_estusername)
    todos(f_todos)
    compilers(f_environment)
    converters(f_environment)
    end()