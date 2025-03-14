# DEFINE EXCEPTIONS
class CompilerError(Exception):
    pass

# DEFINE AUTOMATIONS
def csimmetry(data, begin_end, source):
    amount = data.count(begin_end)
    if not (amount / 2).is_integer():
        raise CompilerError(f"{source} -> csimmetry().")
    else:
        return int(amount / 2)
def exclusivity(data, match_begin, source):
    if data.count(match_begin) > 1:
        raise CompilerError(f"{source} -> exclusivity()")
def start(data, scope, source):
    position = data.find(scope)
    while position != -1:
        if position != 0 and data[position - 1] != "\n":
            raise CompilerError(f"{source} -> start().")
        position = data.find(scope, position + 1)
def correspondence(data, scope_begin, scope_end, source):
    if data.count(scope_begin) != data.count(scope_end):
        raise CompilerError(f"{source} -> correspondence().")
def acorrespondence(data, general, restrictive, source):
    if data.count(restrictive) * 2 != data.count(general):
        raise CompilerError(f"{source} -> acorrespondence().")
def skip(counter):
    for i in counter:
        if i != 0:
            return False
    return True

# TRANSFORMATIONS
# NON-STANDARD-Z
# DEFINE-D -> COUNT-T / CSIMMETRY-Y -> (EXCLUSIVITY-X) -> (START-S) -> (CORRESPONDENCE-C / ACORRESPONDENCE-A) -> SKIP-K -> REPLACE-R -> (SCAPE-N) -> RETURN-F
def class_ad(data, lang):
    # DEFINE
    source = "class_ad()"
    match = "/ad"
    match lang:
        case "Español":
            begin_replacement = "/& Este proyecto de investigación ha sido redactado con ·CSScribe·/ft, el lenguaje de marcado perfecto para hacer trabajos escritos. Para estandarizar la ·simbología LaTeX· del trabajo, se han utilizado los estándares matemáticos anglosajones, intercambiando las comas por los puntos."
        case "English" | _:
            begin_replacement = "/& This project has been written with ·CSScribe·/ft, the perfect markup language for writing papers."
    # COUNT
    counter = [data.count(match)]
    # EXCLUSIVITY
    exclusivity(data, match, source)
    # START
    start(data, match, source)
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(match, begin_replacement)
    # RETURN
    return data, counter
def class_code(data, lang):
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
def class_comment(data, lang):
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
def class_h1(data, lang):
    # DEFINE
    source = "class_h1()"
    begin = "/h1 "
    begin_replacement = "# "
    # COUNT
    counter = [data.count(begin)]
    # EXCLUSIVITY
    exclusivity(data, begin, source)
    # START
    start(data, begin, source)
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(begin, begin_replacement)
    # RETURN
    return data, counter
def class_h2(data, lang):
    # DEFINE
    source = "class_h2()"
    begin = "/h2 "
    begin_replacement = "## "
    # COUNT
    counter = [data.count(begin)]
    # START
    start(data, begin, source)
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(begin, begin_replacement)
    # RETURN
    return data, counter
def class_h3(data, lang):
    # DEFINE
    source = "class_h3()"
    begin = "/h3 "
    begin_replacement = "### "
    # COUNT
    counter = [data.count(begin)]
    # START
    start(data, begin, source)
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(begin, begin_replacement)
    # RETURN
    return data, counter
def class_h4(data, lang):
    # DEFINE
    source = "class_h4()"
    begin = "/h4 "
    begin_replacement = "#### "
    # COUNT
    counter = [data.count(begin)]
    # START
    start(data, begin, source)
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(begin, begin_replacement)
    # RETURN
    return data, counter
def class_image(data, lang):
    # NON-STANDARD
    # DEFINE
    source = "class_image()"
    match = "/img"
    # START
    start(data, match, source)
    # COUNT AND REPLACE
    counter = [0]
    while match in data:
        data = data.replace(match, f"![Relative](/images/{counter[0] + 1}.png)", 1)
        counter[0] += 1
    # RETURN
    return data, counter
def class_math(data, lang):
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
def editor_comment(data, lang):
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
def editor_scape(data, lang):
    # DEFINE
    source = "editor_scape()"
    match = "¬"
    replacement = ""
    scape = "$\\neg$"
    # COUNT
    counter = [data.count(match), data.count(scape)]
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(match + "\n", replacement)
    data = data.replace(match, replacement)
    # SCAPE
    data = data.replace(scape, match)
    # RETURN
    return data, counter
def modifier_bold(data, lang):
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
def modifier_break(data, lang):
    # DEFINE
    source = "modifier_break()"
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
def modifier_checkbox(data, lang):
    # DEFINE
    source = "modifier_checkbox()"
    match = "/X "
    replacement = "- [X] "
    # COUNT
    counter = [data.count(match)]
    # START
    start(data, match, source)
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(match, replacement)
    # RETURN
    return data, counter
def modifier_code(data, lang):
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
def modifier_highlight(data, lang):
    # DEFINE
    source = "modifier_highlight()"
    between = ";"
    replacement_1 = "<mark>"
    replacement_2 = "</mark>"
    # CSIMMETRY
    counter = [csimmetry(data, between, source)]
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    replacement_toggle = True
    while between in data:
        if replacement_toggle:
            data = data.replace(between, replacement_1, 1)
        else:
            data = data.replace(between, replacement_2, 1)
        replacement_toggle = not replacement_toggle
    # SCAPE
    data = data.replace(replacement_1 + replacement_2, between)
    # RETURN
    return data, counter
def modifier_html(data, lang):
    # DEFINE
    source = "modifier_html()"
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
def modifier_index(data, lang):
    # DEFINE
    source = "modifier_index()"
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
def modifier_italic(data, lang):
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
def modifier_math(data, lang):
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
def modifier_ordered(data, lang):
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
def modifier_reference(data, lang):
    # NON-STANDARD
    # DEFINE
    source = "editor_reference()"
    match = "/ft"
    match lang:
        case "Español":
            replacement = "[({number})](#bibliografía)"
        case "English" | _:
            replacement = "[({number})](#references)"
    # COUNT AND REPLACE
    counter = [0]
    while match in data:
        data = data.replace(match, replacement.replace("{number}", str(counter[0] + 1)), 1)
        counter[0] += 1
    # RETURN
    return data, counter
def modifier_strikethrough(data, lang):
    # DEFINE
    source = "modifier_strikethrough()"
    between = "/-"
    replacement = "~~"
    # CSIMMETRY
    counter = [csimmetry(data, between, source)]
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(between, replacement)
    # RETURN
    return data, counter
def modifier_subscript(data, lang):
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
def modifier_superscript(data, lang):
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
def modifier_underline(data, lang):
    # DEFINE
    source = "modifier_underline()"
    between = "__"
    replacement_1 = "<ins>"
    replacement_2 = "</ins>"
    # CSYMMETRY
    counter = [csimmetry(data, between, source)]
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    replacement_toggle = True
    while between in data:
        if replacement_toggle:
            data = data.replace(between, replacement_1, 1)
        else:
            data = data.replace(between, replacement_2, 1)
        replacement_toggle = not replacement_toggle
    # RETURN
    return data, counter
def modifier_unordered(data, lang):
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
def modifier_voidbox(data, lang):
    # DEFINE
    source = "modifier_voidbox()"
    match = "/O "
    replacement = "- [ ] "
    # COUNT
    counter = [data.count(match)]
    # START
    start(data, match, source)
    # SKIP
    if skip(counter):
        return data, counter
    # REPLACE
    data = data.replace(match, replacement)
    # RETURN
    return data, counter
