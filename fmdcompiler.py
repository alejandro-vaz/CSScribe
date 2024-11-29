def fmdtomd(filename):
    def format_power(data):
        data = data.replace("#>", "<!--") # Comment start
        data = data.replace("<#", "-->") # Comment end
        data = data.replace("/h1", "#") # Header
        data = data.replace("/h2", "##") # Chapter
        data = data.replace("/h3", "###") # Section
        return data 
    def format_list(data):
        data = data.replace("    o ", "1. ") # Ordered list
        data = data.replace("    * ", "   - ") # Unordered list
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
        data = data.replace("/n", "\n") # New paragraph
        data = data.replace("·", "*") # Italic
        data = data.replace("/-", "~~") # Strikethrough
        data = data.replace("/s", "~") # Subscript
        data = data.replace("/S", "^") # Superscript
        data = data.replace("\'", "**") # Bold
        return data
    def replace_ctags(data):
        data = data.replace("/pbba", "<pbba>") # page-break-before: avoid
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
        print(F"Error during conversion: \n{e}")
    input("")