import os 
import sys
import shutil
import time

file_path = sys.argv[0]
dir_path = os.path.dirname(os.path.abspath(sys.argv[0]))

structure_content = """CSScribe 4.2.2


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

compiler = """# IMPORT MODULES
import time
from si_prefix import si_format

# DEFINE EXCEPTIONS
class CompilerError(Exception):
    ""\"Error compiling the file.""\"
    pass

# DEFINE AUTOMATIONS
def csimmetry(data, begin_end, source):
    amount = data.count(begin_end)
    if not (amount / 2).is_integer():
        raise CompilerError(f"{source} raised the exception in csimmetry().")
    else:
        return int(amount / 2)
def at_start(data, scope, source):
    position = data.find(scope)
    while position != -1:
        if position != 0 and data[position - 1] != "\\n":
            raise CompilerError(f"{source} raised the exception in at_start().")
        position = data.find(scope, position + 1)
def correspondence(data, scope_begin, scope_end, source):
    if data.count(scope_begin) != data.count(scope_end):
        raise CompilerError(f"{source} raised the exception in correspondence().")
def acorrespondence(data, general, restrictive, source):
    if data.count(restrictive) * 2 != data.count(general):
        raise CompilerError(f"{source} raised the exception in acorrespondence().")
def skip(counter):
    for i in counter:
        if i != 0:
            return False
    return True

# MAIN TRANSFORMER
def cssctomd(filename):
    # TRANSFORMATIONS
    # NON-STANDARD-X
    # DEFINE-D -> COUNT-T / CSIMMETRY-Y -> (AT START-S) -> (CORRESPONDENCE-C / ACORRESPONDENCE-A) -> SKIP-K -> REPLACE-R -> (SCAPE-N) -> RETURN-F
    def class_code(data):
        # DEFINE
        source = "class_code()"
        begin = "/code-"
        end = "/code"
        begin_replacement = "```"
        end_replacement = "```"
        # COUNT
        counter = [data.count(begin), data.count(end)]
        # ACORRESPONDENCE
        acorrespondence(data, end, begin, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        # RETURN
        return data, counter
    def class_comment(data):
        # DEFINE
        source = "class_comment()"
        begin = "/& "
        begin_replacement = "> "
        # COUNT
        counter = [data.count(begin)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, counter
    def class_image(data):
        # NON-STANDARD
        # DEFINE
        source = "class_image()"
        match = "/img"
        # AT START
        at_start(data, match, source)
        # COUNT AND REPLACE
        counter = [0]
        while match in data:
            data = data.replace(match, f"![Relative](/images/{counter[0] + 1}.png)", 1)
            counter[0] += 1
        # RETURN
        return data, counter
    def class_math(data):
        # DEFINE
        source = "class_math()"
        between = "/math"
        replacement = "$$"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, counter
    def editor_comment(data):
        # DEFINE
        source = "editor_comment()"
        begin = "# "
        end = " -#"
        begin_replacement = "<!-- "
        end_replacement = " -->"
        # COUNT
        counter = [data.count(begin), data.count(end)]
        # CORRESPONDENCE
        correspondence(data, begin, end, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        # RETURN
        return data, counter
    def editor_newline(data):
        # DEFINE
        source = "editor_newline()"
        match = "/n"
        replacement = "\\n"
        # COUNT
        counter = [data.count(match)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, counter
    def editor_scape(data):
        # DEFINE
        source = "editor_scape(data)"
        match = "¬"
        replacement = ""
        scape = "$\\\\neg$"
        # COUNT
        counter = [data.count(match), data.count(scape)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(match, replacement)
        # SCAPE
        data = data.replace(scape, match)
        # RETURN
        return data, counter
    def modifier_bold(data):
        # DEFINE
        source = "modifier_bold()"
        between = ":"
        replacement = "**"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # SCAPE
        data = data.replace(replacement * 2, between)
        # RETURN
        return data, counter
    def modifier_checkbox(data):
        # DEFINE
        source = "modifier_checkbox()"
        match = "/X "
        replacement = "- [X] "
        # COUNT
        counter = [data.count(match)]
        # AT START
        at_start(data, match, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, counter
    def modifier_code(data):
        # DEFINE
        source = "modifier_code()"
        between = "/_"
        replacement = "`"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, counter
    def modifier_h1(data):
        # DEFINE
        source = "modifier_h1()"
        begin = "/h1 "
        begin_replacement = "# "
        # COUNT
        counter = [data.count(begin)]
        # AT START
        at_start(data, begin, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, counter
    def modifier_h2(data):
        # DEFINE
        source = "modifier_h2()"
        begin = "/h2 "
        begin_replacement = "## "
        # COUNT
        counter = [data.count(begin)]
        # AT START
        at_start(data, begin, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, counter
    def modifier_h3(data):
        # DEFINE
        source = "modifier_h3()"
        begin = "/h3 "
        begin_replacement = "### "
        # COUNT
        counter = [data.count(begin)]
        # AT START
        at_start(data, begin, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, counter
    def modifier_italic(data):
        # DEFINE
        source = "modifier_italic()"
        between = "·"
        replacement = "*"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # SCAPE
        data = data.replace(replacement + "¬" + replacement, between)
        # RETURN
        return data, counter
    def modifier_math(data):
        # DEFINE
        source = "modifier_math()"
        between = "/="
        replacement = "$"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, counter
    def modifier_ordered(data):
        # DEFINE
        source = "modifier_ordered()"
        match = "    o "
        replacement = "1. "
        # COUNT
        counter = [data.count(match)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, counter
    def modifier_strikethrough(data):
        # DEFINE
        source = "modifier_strikethrough()"
        between = "/-"
        replacement = "~~"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # REPLACE OR SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, counter
    def modifier_subscript(data):
        # DEFINE
        source = "modifier_subscript()"
        between = "/s"
        replacement =  "~"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, counter
    def modifier_superscript(data):
        # DEFINE
        source = "modifier_superscript()"
        between = "/S"
        replacement = "^"
        # CSIMMETRY
        counter = [csimmetry(data, between, source)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, counter
    def modifier_unordered(data):
        # DEFINE
        source = "modifier_unordered()"
        match = "    u "
        replacement = "   - "
        # COUNT
        counter = [data.count(match)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, counter
    def modifier_voidbox(data):
        # DEFINE
        source = "modifier_voidbox()"
        match = "/O "
        replacement = "- [ ] "
        # COUNT
        counter = [data.count(match)]
        # AT START
        at_start(data, match, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, counter
    def tag_break(data):
        # DEFINE
        source = "tag_break()"
        match = "/br"
        replacement = "<br>"
        # COUNT
        counter = [data.count(match)]
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, counter
    def tag_html(data):
        # DEFINE
        source = "tag_html()"
        begin = "<"
        end = ">"
        begin_replacement = "<"
        end_replacement = ">"
        begin_scape = "/=\\\\lt/="
        end_scape = "/=\\\\gt/="
        # COUNT
        counter = [data.count(begin), data.count(end), data.count(begin_scape), data.count(end_scape)]
        # CORRESPONDENCE
        correspondence(data, begin, end, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        # SCAPE
        data = data.replace(begin_scape, begin)
        data = data.replace(end_scape, end)
        # RETURN
        return data, counter
    def tag_index(data):
        # DEFINE
        source = "tag_index()"
        begin = "/In"
        end = "/in"
        begin_replacement = "<index>"
        end_replacement = "</index>"
        # COUNT
        counter = [data.count(begin), data.count(end)]
        # CORRESPONDENCE
        correspondence(data, begin, end, source)
        # SKIP
        if skip(counter):
            return data, counter
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        # RETURN
        return data, counter
    
    # CONVERSION
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
    content, tag_html_count = tag_html(content) # BEFORE CLASS_COMMENT, EDITOR_COMMENT, MODIFIER_MATH (1)
    content, class_code_count = class_code(content)
    content, class_comment_count = class_comment(content)
    content, class_image_count = class_image(content)
    content, class_math_count = class_math(content)
    content, editor_comment_count = editor_comment(content)
    content, editor_newline_count = editor_newline(content)
    content, modifier_bold_count = modifier_bold(content)
    content, modifier_checkbox_count = modifier_checkbox(content)
    content, modifier_code_count = modifier_code(content)
    content, modifier_h1_count = modifier_h1(content)
    content, modifier_h2_count = modifier_h2(content)
    content, modifier_h3_count = modifier_h3(content)
    content, modifier_italic_count = modifier_italic(content)
    content, modifier_math_count =  modifier_math(content)
    content, modifier_ordered_count = modifier_ordered(content)
    content, modifier_strikethrough_count = modifier_strikethrough(content)
    content, modifier_subscript_count = modifier_subscript(content)
    content, modifier_superscript_count = modifier_superscript(content)
    content, modifier_unordered_count = modifier_unordered(content)
    content, modifier_voidbox_count = modifier_voidbox(content)
    content, tag_break_count = tag_break(content)
    content, tag_index_count = tag_index(content)
    content, editor_scape_count = editor_scape(content) # AFTER MODIFIER_MATH (24)
    return content

# ENTRY POINT
if __name__ == "__main__":
    filename = input("Name of file without extension: ")
    cssc_file = f"{filename}.cssc"
    md_file = f"{filename}.md"
    start_time = time.time()
    with open(md_file, 'w', encoding="utf-8") as file:
        converted = cssctomd(cssc_file)
        file.write(converted)
    end_time = time.time()
    print(f"Conversion done in {si_format(end_time - start_time, precision=2)}s")
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
    for filename in os.listdir(directory):
        paths = os.path.join(directory, filename)
        try:
            if os.path.isdir(paths):
                shutil.rmtree(paths)
            else:
                if paths != file_path:
                    os.remove(paths)
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