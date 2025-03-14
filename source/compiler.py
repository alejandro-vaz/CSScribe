# IMPORT COMMON MODULES
import time
import os
import sys
import re

# IMPORT THIRD-PARTY MODULES
from si_prefix import si_format

# IMPORT SOURCE MODULES
import compiler_conversion

# MAIN TRANSFORMER
def cssctomd(filename, language):
    # OPEN
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        
    # GENERAL COUNTING
    words = len(re.findall(r'\b\w+\b', content))
    lines = len(content.split("\n")) + 1
    
    # CONVERSION
    content, modifier_html_count = compiler_conversion.modifier_html(content, language) # BEFORE CLASS_COMMENT, EDITOR_COMMENT, MODIFIER_MATH (1)
    content, class_ad_count = compiler_conversion.class_ad(content, language) # BEFORE CLASS_COMMENT, MODIFIER_REFERENCE (2)
    content, class_code_count = compiler_conversion.class_code(content, language)
    content, class_comment_count = compiler_conversion.class_comment(content, language)
    content, editor_comment_count = compiler_conversion.editor_comment(content, language) 
    content, class_h1_count = compiler_conversion.class_h1(content, language) # AFTER EDITOR_COMMENT
    content, class_h2_count = compiler_conversion.class_h2(content, language) # AFTER EDITOR_COMMENT
    content, class_h3_count = compiler_conversion.class_h3(content, language) # AFTER EDITOR_COMMENT
    content, class_h4_count = compiler_conversion.class_h4(content, language) # AFTER EDITOR_COMMENT
    content, class_image_count = compiler_conversion.class_image(content, language)
    content, class_math_count = compiler_conversion.class_math(content, language)
    content, modifier_bold_count = compiler_conversion.modifier_bold(content, language)
    content, modifier_checkbox_count = compiler_conversion.modifier_checkbox(content, language)
    content, modifier_code_count = compiler_conversion.modifier_code(content, language)
    content, modifier_highlight_count = compiler_conversion.modifier_highlight(content, language)
    content, modifier_italic_count = compiler_conversion.modifier_italic(content, language)
    content, modifier_math_count =  compiler_conversion.modifier_math(content, language)
    content, modifier_ordered_count = compiler_conversion.modifier_ordered(content, language)
    content, modifier_reference_count = compiler_conversion.modifier_reference(content, language)
    content, modifier_strikethrough_count = compiler_conversion.modifier_strikethrough(content, language)
    content, modifier_subscript_count = compiler_conversion.modifier_subscript(content, language)
    content, modifier_superscript_count = compiler_conversion.modifier_superscript(content, language)
    content, modifier_index_count = compiler_conversion.modifier_index(content, language) # BEFORE MODIFIER_UNDERLINE
    content, modifier_underline_count = compiler_conversion.modifier_underline(content, language)
    content, modifier_unordered_count = compiler_conversion.modifier_unordered(content, language)
    content, modifier_voidbox_count = compiler_conversion.modifier_voidbox(content, language)
    content, modifier_break_count = compiler_conversion.modifier_break(content, language)
    
    # POLISHING
    content = content.replace("\n", "\n\n")
    
    # SCAPE
    content, editor_scape_count = compiler_conversion.editor_scape(content, language) # AFTER EVERYTHING
    
    # DEFINE MESSAGE LANGUAGE
    messages = []
    indent = "    > "
    match language:
        case "Español":
            line0 = "¡Gracias por incluir el anuncio de CSScribe!"
            line1 = "Hacer un encabezado h1 no está recomendado para documentos grandes. Sería mejor que añadieses una portada."
            line2 = "La etiqueta HTML ha sido inyectada en el documento y los estilos personalizables de CSS están disponibles."
            line3 = f"{modifier_html_count[0]} etiqueta{"s" if modifier_html_count[0] > 1 else ""} de HTML ha{"n" if modifier_html_count[0] > 1 else ""} sido inyectada{"s" if modifier_html_count[0] > 1 else ""} en el documento y está{"n" if modifier_html_count[0] > 1 else ""} lista{"s" if modifier_html_count > 1 else ""} para los estilos de CSS personalizables."
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
        case "English" | _:
            line0 = "Thanks for including the CSScribe advertisement!"
            line1 = "Making an h1 header is not recommended for large documents. It'd better if you added a cover page."
            line2 = "The HTML tag has been passed to the document and custom CSS styling is available."
            line3 = f"{modifier_html_count[0]} HTML tag{"s" if modifier_html_count[0] > 1 else ""} ha{"ve" if modifier_html_count[0] > 1 else "s"} been passed to the document and {"are" if modifier_html_count[0] > 1 else "is"} ready for custom CSS styling."
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
    
    # MESSAGE LOGIC
    if class_ad_count[0] >= 1:
        messages.append(indent + line0)
    if words >= 1500 or lines >= 200:
        messages.append(indent + line1)
    if modifier_html_count[0] == 1:
        messages.append(indent + line2)
    if modifier_html_count[0] > 1:
        messages.append(indent + line3)
    match (class_h1_count[0], class_h2_count[0], class_h3_count[0], class_h4_count[0]):
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