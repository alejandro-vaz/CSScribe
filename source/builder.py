# NEEDS TO BE RETRANSCRIBED

import os 
import sys
import shutil
import time

dir_path = os.getcwd()

structure_content = """CSScribe 4.2.6


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

def init():
    print("CSScribe environment builder tool. Confirm the following data:")
    time.sleep(0.75)
    print(f"This directory path is {dir_path}")
    if input("Is this correct? (y/n): ").lower() != "y":
        exit()

def restructure(i_environment, i_images):
    if i_environment:
        os.makedirs(os.path.join(dir_path, 'env'), exist_ok=True)
        if i_images:
            os.makedirs(os.path.join(dir_path, 'env/images'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-2'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-0'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-1'), exist_ok=True)
    if i_images:
        os.makedirs(os.path.join(dir_path, 'step-3/images'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-3'), exist_ok=True)
    os.makedirs(os.path.join(dir_path, 'step-4'), exist_ok=True)

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
    end()