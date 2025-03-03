# IMPORT MODULES
import time
import os
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
        replacement = "\n"
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
        scape = "$\\neg$"
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
        begin_scape = "/=\\lt/="
        end_scape = "/=\\gt/="
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
    while True:
        filename = input("Name of file without extension: ")
        cssc_file = f"{filename}.cssc"
        md_file = f"{filename}.md"
        if not os.path.isfile(cssc_file):
            print(f"\"{cssc_file}\" does not exist.")
        else:
            start_time = time.time()
            with open(md_file, 'w', encoding="utf-8") as file:
                converted = cssctomd(cssc_file)
                file.write(converted)
            end_time = time.time()
            print(f"Conversion done in {si_format(end_time - start_time, precision=2)}s")