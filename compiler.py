# IMPORT MODULES
import time
import re
from si_prefix import si_format

# DEFINE EXCEPTIONS
class CompilerError(Exception):
    """Error compiling the file."""
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
        if position != 0 and data[position - 1] != "\n":
            raise CompilerError(f"{source} raised the exception in at_start().")
        position = data.find(scope, position + 1)
def correspondence(data, scope_begin, scope_end, source):
    if data.count(scope_begin) != data.count(scope_end):
        raise CompilerError(f"{source} raised the exception in correspondence().")
def acorrespondence(data, general, restrictive, source):
    if data.count(restrictive) * 2 != data.count(general):
        raise CompilerError(f"{source} raised the exception in acorrespondence().")

# MAIN TRANSFORMER
def cssctomd(filename):
    # TRANSFORMATIONS
    # DEFINE -> COUNT / CSIMMETRY -> (AT START) -> (CORRESPONDENCE / ACORRESPONDENCE) -> REPLACE -> RETURN
    def class_code(data):
        # DEFINE
        source = "class_code()"
        begin = "/code-"
        end = "/code"
        begin_replacement = "```"
        end_replacement = "```"
        # ACOUNT
        class_code_count = data.count(begin)
        # ACORRESPONDENCE
        acorrespondence(data, end, begin, source)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        # RETURN
        return data, class_code_count
    def class_comment(data):
        # DEFINE
        source = "class_comment()"
        begin = "/>"
        begin_replacement = ">"
        # COUNT
        class_comment_count = data.count(begin)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, class_comment_count
    def class_image(data):
        # NON-STANDARD CLASS
        # DEFINE
        source = "class_image()"
        match = "/img"
        # AT START
        at_start(data, match, source)
        # COUNT AND REPLACE
        class_image_count = 0
        while match in data:
            data = data.replace(match, f"![Relative](/images/{class_image_count + 1}.png)", 1)
            class_image_count += 1
        # RETURN
        return data, class_image_count
    def class_math(data):
        # DEFINE
        source = "class_math()"
        between = "/math"
        replacement = "$$"
        # CSIMMETRY
        class_math_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, class_math_count
    def editor_comment(data):
        # DEFINE
        source = "editor_comment()"
        begin = "#>"
        end = "<#"
        begin_replacement = "<!--"
        end_replacement = "-->"
        # COUNT
        editor_comment_count = data.count(begin)
        # CORRESPONDENCE
        correspondence(data, begin, end, source)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        # RETURN
        return data, editor_comment_count
    def editor_newline(data):
        # DEFINE
        source = "editor_newline()"
        match = "/n"
        replacement = "\n"
        # COUNT
        editor_newline_count = data.count(match)
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, editor_newline_count
    def editor_scape(data):
        # DEFINE
        source = "editor_scape(data)"
        match = "¬"
        replacement = ""
        # COUNT
        editor_scape_count = data.count(match)
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, editor_scape_count
    def modifier_bold(data):
        # DEFINE
        source = "modifier_bold()"
        between = "\'"
        replacement = "**"
        # CSIMMETRY
        modifier_bold_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(between, replacement)
        data = data.replace(replacement * 2, between)
        # RETURN
        return data, modifier_bold_count
    def modifier_checkbox(data):
        # DEFINE
        source = "modifier_checkbox()"
        match = "/X "
        replacement = "- [X] "
        # COUNT
        modifier_checkbox_count = data.count(match)
        # AT START
        at_start(data, match, source)
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, modifier_checkbox_count
    def modifier_code(data):
        # DEFINE
        source = "modifier_code()"
        between = "/cd"
        replacement = "`"
        # CSIMMETRY
        modifier_code_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, modifier_code_count
    def modifier_h1(data):
        # DEFINE
        source = "modifier_h1()"
        begin = "/h1"
        begin_replacement = "#"
        # COUNT
        modifier_h1_count = data.count(begin)
        # AT START
        at_start(data, begin, source)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, modifier_h1_count
    def modifier_h2(data):
        # DEFINE
        source = "modifier_h2()"
        begin = "/h2"
        begin_replacement = "##"
        # COUNT
        modifier_h2_count = data.count(begin)
        # AT START
        at_start(data, begin, source)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, modifier_h2_count
    def modifier_h3(data):
        # DEFINE
        source = "modifier_h3()"
        begin = "/h3"
        begin_replacement = "###"
        # COUNT
        modifier_h3_count = data.count(begin)
        # AT START
        at_start(data, begin, source)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        # RETURN
        return data, modifier_h3_count
    def modifier_italic(data):
        # DEFINE
        source = "modifier_italic()"
        between = "·"
        replacement = "*"
        # CSIMMETRY
        modifier_italic_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(between, replacement)
        data = data.replace(between + "¬" + between, between)
        # RETURN
        return data, modifier_italic_count
    def modifier_math(data):
        # DEFINE
        source = "modifier_math()"
        between = "/_"
        replacement = "$"
        # CSIMMETRY
        modifier_math_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(2 * between, "")
        data = data.replace(between, replacement)
        # RETURN
        return data, modifier_math_count
    def modifier_ordered(data):
        # DEFINE
        source = "modifier_ordered()"
        match = "    o "
        replacement = "1. "
        # COUNT
        modifier_ordered_count = data.count(match)
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, modifier_ordered_count
    def modifier_strikethrough(data):
        # DEFINE
        source = "modifier_strikethrough()"
        between = "/-"
        replacement = "~~"
        # CSIMMETRY
        modifier_strikethrough_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, modifier_strikethrough_count
    def modifier_subscript(data):
        # DEFINE
        source = "modifier_subscript()"
        between = "/s"
        replacement =  "~"
        # CSIMMETRY
        modifier_subscript_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(2 * between, "")
        data = data.replace(between, replacement)
        # RETURN
        return data, modifier_subscript_count
    def modifier_superscript(data):
        # DEFINE
        source = "modifier_superscript()"
        between = "/S"
        replacement = "^"
        # CSIMMETRY
        modifier_superscript_count = csimmetry(data, between, source)
        # REPLACE
        data = data.replace(between, replacement)
        # RETURN
        return data, modifier_superscript_count
    def modifier_unordered(data):
        # DEFINE
        source = "modifier_unordered()"
        match = "    u "
        replacement = "   - "
        # COUNT
        modifier_unordered_count = data.count(match)
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, modifier_unordered_count
    def modifier_voidbox(data):
        # DEFINE
        source = "modifier_voidbox()"
        match = "/O "
        replacement = "- [ ] "
        # COUNT
        modifier_voidbox_count = data.count(match)
        # AT START
        at_start(data, match, source)
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, modifier_voidbox_count
    def tag_break(data):
        # DEFINE
        source = "tag_break()"
        match = "/br"
        replacement = "<br>"
        # COUNT
        tag_break_count = data.count(match)
        # REPLACE
        data = data.replace(match, replacement)
        # RETURN
        return data, tag_break_count
    def tag_html(data):
        # DEFINE
        source = "tag_html()"
        begin = "<"
        end = ">"
        begin_replacement = "<"
        end_replacement = ">"
        # COUNT
        tag_html_count = data.count(begin)
        # CORRESPONDENCE
        # correspondence(data, begin, end, source)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        # RETURN
        return data, tag_html_count
    def tag_index(data):
        # DEFINE
        source = "tag_index()"
        begin = "/In"
        end = "/in"
        begin_replacement = "<index>"
        end_replacement = "</index>"
        # COUNT
        tag_index_count = data.count(begin)
        # CORRESPONDENCE
        correspondence(data, begin, end, source)
        # REPLACE
        data = data.replace(begin, begin_replacement)
        data = data.replace(end, end_replacement)
        return data, tag_index_count
    
    # CONVERSION
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
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
    content, tag_html_count = tag_html(content)
    content, tag_index_count = tag_index(content)
    content, editor_scape_count = editor_scape(content)
    return content

# ENTRY POINT
if __name__ == "__main__":
    filename = input("Name of file without extension: ")
    cssc_file = f"{filename}.cssc"
    md_file = f"{filename}.md"
    start_time = time.time()
    with open(md_file, 'w', encoding="utf-8") as file:
        file.write(cssctomd(cssc_file))
    end_time = time.time()
    print(f"Conversion done in {si_format(end_time - start_time, precision=2)}s")
    input("")
