# IMPORT MODULES
import time
import os
from si_prefix import si_format
import sys

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

# MAIN TRANSFORMER
def cssctomd(filename, language):
    # TRANSFORMATIONS
    # NON-STANDARD-Z
    # DEFINE-D -> COUNT-T / CSIMMETRY-Y -> (EXCLUSIVITY-X) -> (START-S) -> (CORRESPONDENCE-C / ACORRESPONDENCE-A) -> SKIP-K -> REPLACE-R -> (SCAPE-N) -> RETURN-F
    def class_ad(data, lang):
        # DEFINE
        source = "class_ad()"
        match = "/ad"
        match lang:
            case "Español":
                begin_replacement = "/& Este proyecto de investigación ha sido redactado con ·CSScribe·[(1)](#bibliografía), el lenguaje de marcado perfecto para hacer trabajos escritos. Para estandarizar la ·simbología LaTeX· del trabajo, se han utilizado los estándares matemáticos anglosajones, intercambiando las comas por los puntos."
            case "English":
                begin_replacement = "/& This project has been written with ·CSScribe·[(1)](#references), the perfect markup language for writing papers."
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
    def editor_newline(data, lang):
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
    def editor_scape(data, lang):
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
    def modifier_h1(data, lang):
        # DEFINE
        source = "modifier_h1()"
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
    def modifier_h2(data, lang):
        # DEFINE
        source = "modifier_h2()"
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
    def modifier_h3(data, lang):
        # DEFINE
        source = "modifier_h3()"
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
    def modifier_h4(data, lang):
        # DEFINE
        source = "modifier_h4()"
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
    def tag_break(data, lang):
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
    def tag_html(data, lang):
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
    def tag_index(data, lang):
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
    
    # OPEN
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        
    # GENERAL COUNTING
    words = len((content.replace("\n", " ")).split(" "))
    lines = len(content.split("\n")) + 1
    
    # CONVERSION
    content, tag_html_count = tag_html(content, language) # BEFORE CLASS_COMMENT, EDITOR_COMMENT, MODIFIER_MATH (1)
    content, class_ad_count = class_ad(content, language) # BEFORE CLASS_COMMENT (2)
    content, class_code_count = class_code(content, language)
    content, class_comment_count = class_comment(content, language)
    content, class_image_count = class_image(content, language)
    content, class_math_count = class_math(content, language)
    content, editor_comment_count = editor_comment(content, language)
    content, editor_newline_count = editor_newline(content, language)
    content, modifier_bold_count = modifier_bold(content, language)
    content, modifier_checkbox_count = modifier_checkbox(content, language)
    content, modifier_code_count = modifier_code(content, language)
    content, modifier_h1_count = modifier_h1(content, language)
    content, modifier_h2_count = modifier_h2(content, language)
    content, modifier_h3_count = modifier_h3(content, language)
    content, modifier_h4_count = modifier_h4(content, language)
    content, modifier_italic_count = modifier_italic(content, language)
    content, modifier_math_count =  modifier_math(content, language)
    content, modifier_ordered_count = modifier_ordered(content, language)
    content, modifier_strikethrough_count = modifier_strikethrough(content, language)
    content, modifier_subscript_count = modifier_subscript(content, language)
    content, modifier_superscript_count = modifier_superscript(content, language)
    content, modifier_unordered_count = modifier_unordered(content, language)
    content, modifier_voidbox_count = modifier_voidbox(content, language)
    content, tag_break_count = tag_break(content, language)
    content, tag_index_count = tag_index(content, language)
    content, editor_scape_count = editor_scape(content, language) # AFTER MODIFIER_MATH (24)
    
    # DEFINE MESSAGE LANGUAGE
    messages = []
    indent = "    > "
    match language:
        case "Español":
            line0 = "¡Gracias por incluir el anuncio de CSScribe!"
            line1 = "Hacer un encabezado h1 no está recomendado para documentos grandes. Sería mejor que añadieses una portada."
            line2 = "La etiqueta HTML ha sido inyectada en el documento y los estilos personalizables de CSS están disponibles."
            line3 = f"{tag_html_count[0]} etiquetas de HTML han sido inyectadas en el documento y están listas para los estilos de CSS personalizables."
            line4 = "No se ha detectado ningún encabezado. Utiliza al menos un encabezado h2 para el título del documento."
            line5 = "Tipos de encabezados detectados: h4. Utiliza encabezados h2 en su lugar."
            line6 = "Tipos de encabezados detectados: h3. Utiliza encabezados h2 en su lugar."
            line7 = "Tipos de encabezados detectados: h3, h4. Utiliza encabezados h2, h3 en su lugar."
            line8 = "Tipos de encabezados detectados: h2, h4. Utiliza encabezados h2, h3 en su lugar."
            line9 = "Tipos de encabezados detectados: h1. Utiliza encabezados h2 en su lugar."
            line10 = "Tipos de encabezados detectados: h1, h4. Utiliza encabezados h2, h3 en su lugar."
            line11 = "Tipos de encabezados detectados: h1, h3. Utiliza encabezados h2, h3 en su lugar."
            line12 = "Tipos de encabezados detectados: h1, h3, h4. Utiliza encabezados h2, h3, h4 en su lugar."
            line13 = "Tipos de encabezados detectados: h1, h2. Utiliza encabezados h2, h3 en su lugar."
            line14 = "Tipos de encabezados detectados: h1, h2, h4. Utiliza encabezados h2, h3, h4 en su lugar."
            line15 = "Tipos de encabezados detectados: h1, h2, h3. Utiliza encabezados h2, h3, h4 en su lugar."
            line16 = "No todas las imágenes tienen descripción. Considera añadirlas con una etiqueta break después de la imagen."
        case "English" | _:
            line0 = "Thanks for including the CSScribe advertisement!"
            line1 = "Making an h1 header is not recommended for large documents. It'd better if you added a cover page."
            line2 = "The HTML tag has been passed to the document and custom CSS styling is available."
            line3 = f"{tag_html_count[0]} HTML tags have been passed to the document and are ready for custom CSS styling."
            line4 = "No headers detected. Use at least an h2 header for the document title."
            line5 = "Types of header detected: h4. Use h2 headers instead."
            line6 = "Types of header detected: h3. Use h2 headers instead."
            line7 = "Types of header detected: h3, h4. Use h2, h3 headers instead."
            line8 = "Types of header detected: h2, h4. Use h2, h3 headers instead."
            line9 = "Types of header detected: h1. Use h2 headers instead."
            line10 = "Types of header detected: h1, h4. Use h2, h3 headers instead."
            line11 = "Types of header detected: h1, h3. Use h2, h3 headers instead."
            line12 = "Types of header detected: h1, h3, h4. Use h2, h3, h4 headers instead."
            line13 = "Types of header detected: h1, h2. Use h2, h3 headers instead."
            line14 = "Types of header detected: h1, h2, h4. Use h2, h3, h4 headers instead."
            line15 = "Types of header detected: h1, h2, h3. Use h2, h3, h4 headers instead."
            line16 = "Not all images have captions. Consider adding them with a break tag after the image."
    
    # MESSAGE LOGIC
    if class_ad_count[0] >= 1:
        messages.append(indent + line0)
    if words >= 1500 or lines >= 200:
        messages.append(indent + line1)
    if tag_html_count[0] == 1:
        messages.append(indent + line2)
    if tag_html_count[0] > 1:
        messages.append(indent + line3)
    match (modifier_h1_count[0], modifier_h2_count[0], modifier_h3_count[0], modifier_h4_count[0]):
        case (a, b, c, d) if a == 0 and b == 0 and c == 0 and d == 0:
            messages.append(indent + line4)
        case (a, b, c, d) if a == 0 and b == 0 and c == 0 and d >= 1:
            messages.append(indent + line5)
        case (a, b, c, d) if a == 0 and b == 0 and c >= 1 and d == 0:
            messages.append(indent + line6)
        case (a, b, c, d) if a == 0 and b == 0 and c >= 1 and d >= 1:
            messages.append(indent + line7)
        case (a, b, c, d) if a == 0 and b >= 1 and c == 0 and d >= 1:
            messages.append(indent + line8)
        case (a, b, c, d) if a == 1 and b == 0 and c == 0 and d == 0:
            messages.append(indent + line9)
        case (a, b, c, d) if a == 1 and b == 0 and c == 0 and d >= 1:
            messages.append(indent + line10)
        case (a, b, c, d) if a == 1 and b == 0 and c >= 1 and d == 0:
            messages.append(indent + line11)
        case (a, b, c, d) if a == 1 and b == 0 and c >= 1 and d >= 1:
            messages.append(indent + line12)
        case (a, b, c, d) if a == 1 and b >= 1 and c == 0 and d == 0:
            messages.append(indent + line13)
        case (a, b, c, d) if a == 1 and b >= 1 and c == 0 and d >= 1:
            messages.append(indent + line14)
        case (a, b, c, d) if a == 1 and b >= 1 and c >= 1 and d == 0:
            messages.append(indent + line15)
        case(a, b, c, d) if a == 1 and b >= 1 and c >= 1 and d >= 1:
            messages.append(indent + line1)
    if tag_break_count[0] < class_image_count[0]:
        messages.append(indent + line16)
    # FINISH
    return content, messages

# ENTRY POINT
if __name__ == "__main__":
    # DEFINE LANGUAGE
    match sys.argv[1]:
        case "Español":
            line_greeting = "Bienvenido al compilador de CSScribe."
            line_instructions = "Introduce el nombre de un fichero sin su extensión .cssc o \"/\" para salir."
            line_notexists = " no existe."
            line_compiled = "Compilado en "
        case "English" | _:
            line_greeting = "Welcome to the CSScribe compiler."
            line_instructions = "Type a file name without .cssc extension included or \"/\" to exit the compiler."
            line_notexists = " does not exist."
            line_compiled = "Compiled in "
    
    # MAIN PROCESS
    print(line_greeting)
    print(line_instructions)
    while True:
        filename = input(">>> ")
        if filename.strip() == "/":
            break
        cssc_file = f"{filename}.cssc"
        md_file = f"{filename}.md"
        if not os.path.isfile(cssc_file):
            print(f"\"{cssc_file}\"{line_notexists}")
        else:
            start_time = time.time()
            with open(md_file, 'w', encoding="utf-8") as file:
                converted, printable = cssctomd(cssc_file, sys.argv[1].strip())
                file.write(converted)
            end_time = time.time()
            for message in printable:
                print(message)
            print(f"    {line_compiled}{si_format(end_time - start_time, precision=2)}s.")