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
    file.write("""Project
├── step-0 = 14/01/2025
├── step-1 = 14/01/2025
├── step-2 = 13/01/2025
├── step-3 = 12/01/2025
└── step-4 = 11/01/2025


project.pdf
├── front_page.pdf
└── main.pdf
    └── main.md
        └── main.fmd
            ├── index.fmd (#index)
            ├── introduction.fmd (#introduction)
            └── conclusion.fmd (#conclusion)


project.pdf
├── Index (#index)
├── Introduction (#introduction)
│   ├── Development (#development)
│   └── Summary (#summary)
└── Conclusion (#conclusion)


https://github.com/user/project/tree/main/
├── .git
├── .structure
├── step-0/
│   ├── .todo
│   └── project.pdf
├── step-1/
│   ├── .todo
│   ├── front_page.pdf
│   └── main.pdf
├── step-2/
│   ├── .todo
│   ├── main.md
│   └── images/
│       ├── 1.png
│       ├── 2.png
│       ├── 3.png
│       └── jpegtopng.py
├── step-3/
│   ├── .todo
│   ├── main.fmd
│   └── fmdcompiler.py
└── step-4/
    ├── .todo
    ├── index.fmd
    ├── introduction.fmd
    └── conclusion.fmd

"""
    )

os.makedirs(os.path.join(dir_path, 'step-0'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-1'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-2'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-2/images'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-3'), exist_ok=True)  # Create a new directory
os.makedirs(os.path.join(dir_path, 'step-4'), exist_ok=True)  # Create a new directory

open(os.path.join(dir_path, 'step-0/.gitignore'), 'w', encoding='utf-8')  # Create a new file
open(os.path.join(dir_path, 'step-1/.gitignore'), 'w', encoding='utf-8')  # Create a new file
open(os.path.join(dir_path, 'step-2/.gitignore'), 'w', encoding='utf-8')  # Create a new file
open(os.path.join(dir_path, 'step-2/images/.gitignore'), 'w', encoding='utf-8')  # Create a new file
open(os.path.join(dir_path, 'step-3/.gitignore'), 'w', encoding='utf-8')  # Create a new file
open(os.path.join(dir_path, 'step-4/.gitignore'), 'w', encoding='utf-8')  # Create a new file

with open(os.path.join(dir_path, 'step-0/.todo'), 'w', encoding='utf-8') as step: # Create a new file
    content = """Take /step-1 pdfs and join them via ILovePDF joiner. This one is the only one valid because it maintains links functionality.
Rename the resulting pdf and place it in step-0. Additional material may be included here."""
    step.write(content)
with open(os.path.join(dir_path, 'step-1/.todo'), 'w', encoding='utf-8') as step: # Create a new file
    content = """Take step-2 document and convert it to a standalone PDF via princexml with the .less file.
You should correct all document mistakes, errors or adjustments now.
You should also create the front page."""
    step.write(content)
with open(os.path.join(dir_path, 'step-2/.todo'), 'w', encoding='utf-8') as step: # Create a new file
    content = """Add the images in the images folder. Convert then the step-3 FastMarkDown file to MarkDown format via the compiler and place it."""
    step.write(content)
with open(os.path.join(dir_path, 'step-3/.todo'), 'w', encoding='utf-8') as step: # Create a new file
    content = """Take the step-4 FastMarkDown files and join them all in a single FastMarkDown file."""
    step.write(content)
with open(os.path.join(dir_path, 'step-4/.todo'), 'w', encoding='utf-8') as step: # Create a new file
    content = """Write all the document parts first."""
    step.write(content)

with open(os.path.join(dir_path, 'step-3/fmdcompiler.py'), "w", encoding="utf-8") as comp:
    content = """def fmdtomd(filename):
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
    fmd_file = f"{filename}.fmd"
    md_file = f"{filename}.md"
    try:
        with open(md_file, 'w', encoding="utf-8") as file:
            file.write(fmdtomd(fmd_file))
        print("Conversion done!")
    except Exception as e:
        print(F"Error during conversion: \\n{e}")
    input("")
"""
    comp.write(content)
os.system(f'code "{dir_path}"')