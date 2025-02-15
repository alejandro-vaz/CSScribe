### CSScribe

Este lenguaje de programación está diseñado para estandarizar el uso de MarkDown y hacer más fácil la redacción de contenido mediante CSS. El lenguaje de programación es capaz de crear documentos PDF a partir de código sin intervención del usuario.

Es capaz de insertar bloques de código, bloques aparte, fórmulas matemáticas, imágenes y muchos otros recursos de forma automática y estilizada por defecto.


### Dependencias

   - VSCode
   - Markdown Preview Enhanced
   - PrinceXML

### Compatibilidad

- [X] Windows 10 (todas las versiones)
- [X] Windows 11 (todas las versiones)
- [ ] Linux (no comprobado)


### Guía de instalación

Primero necesitarás instalar [Visual Studio Code,](https:/```.visualstudio.com/) como requisito imprescindible.

Necesitarás después instalar la extensión de CSScribe. Para ello, presiona Ctrl + Shift + P dentro de VSCode y busca `Developer: Install Extension from Location...`. Luego, selecciona la carpeta de la extensión (`CSScribe-X.Y.Z`).

Después, acude al Marketplace de extensiones y busca `Markdown Preview Enhanced`, hecha por Yiyi Wang. Instala la extensión.

Finalmente, necesitarás instalar [PrinceXML](https://www.princexml.com/) y hacer unos cambios. Una vez hayas instalado Prince, añade a PATH (en variables de entorno de Windows) la ruta de la siguiente carpeta:

```
C:\Program Files (x86)\Prince\engine\bin
```
Además, duplica el archivo `prince.exe` en esa carpeta y renómbralo a `princexml.exe`.

Otra vez de vuelta en VSCode, copia este argumento en `settings.json`, puedes acceder a este documento presionando Ctrl + Shift + P y buscando Preferences: Open User Settings (JSON):
```json
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "class-code.cssc",
                "settings": {
                    "foreground": "#9494ff" // Color para bloques de código
                }
            },
            {
                "scope": "class-comment.cssc",
                "settings": {
                    "foreground": "#aaa" // Color para definiciones
                }
            },
            {
                "scope": "class-image.cssc",
                "settings": {
                    "foreground": "#ff00ff", // Color para imágenes
                    "fontStyle": "underline"
                }
            },
            {
                "scope": "class-math.cssc", // Color para matemáticas
                "settings": {
                    "foreground": "#ffffaa",
                }
            },
            {
                "scope": "editor-comment.cssc",
                "settings": {
                    "foreground": "#6b6b6b" // Color para comentarios
                }
            },
            {
                "scope": "editor-newline.cssc", // Color para nuevo párrafo
                "settings": {
                    "foreground": "#6b6b6b" // Color para nuevo párrafo
                }
            },
            {
                "scope": "editor-scape.cssc", // Color para scape
                "settings": {
                    "foreground": "#111111" // Color para scape
                }
            },
            {
                "scope": "modifier-bold.cssc",
                "settings": {
                    "foreground": "#94eb52", // Color para texto en negrita
                    "fontStyle": "bold" // Añadir estilo de negrita
                }
            },
            {
                "scope": "modifier-brochet.cssc", // Color para brochet
                "settings": {
                    "foreground": "#ffff00",
                }
            },
            {
                "scope": "modifier-checkbox.cssc",
                "settings": {
                    "foreground": "#02e9f5" // Color para done
                }
            },
            {
                "scope": "modifier-code.cssc",
                "settings": {
                    "foreground": "#9494ff" // Color para bloques de código
                }
            },
            {
                "scope": "modifier-h1.cssc",
                "settings": {
                    "foreground": "#00ff00", // Color para encabezados de nivel 1
                    "fontStyle": "bold"
                }
            },
            {
                "scope": "modifier-h2.cssc",
                "settings": {
                    "foreground": "#00ffff", // Color para encabezados de nivel 2
                    "fontStyle": "bold"
                }
            },
                        {
                "scope": "modifier-h3.cssc",
                "settings": {
                    "foreground": "#ffff00", // Color para encabezados de nivel 2
                    "fontStyle": "bold"
                }
            },
            {
                "scope": "modifier-italic.cssc",
                "settings": {
                    "foreground": "#09acb5", // Color para texto en cursiva
                    "fontStyle": "italic" // Añadir estilo de cursiva
                }
            },
            {
                "scope": "modifier-math.cssc", // Color para matemáticas en linea
                "settings": {
                    "foreground": "#ffffaa",
                }
            },
            {
                "scope": "modifier-ordered.cssc",
                "settings": {
                    "foreground": "#ffff00" // Color para numerados
                }
            },
            {
                "scope": "modifier-strikethrough.cssc",
                "settings": {
                    "foreground": "#ff3c00", // Color para texto tachado
                    "fontStyle": "strikethrough" // Añadir estilo de tachado
                }
            },
            {
                "scope": "modifier-subscript.cssc",
                "settings": {
                    "foreground": "#ff0000" // Color para subíndices
                }
            },
            {
                "scope": "modifier-superscript.cssc",
                "settings": {
                    "foreground": "#00ff00" // Color para superíndices
                }
            },
            {
                "scope": "modifier-unordered.cssc",
                "settings": {
                    "foreground": "#ffff00" // Color para apuntados
                }
            },
            {
                "scope": "modifier-voidbox.cssc",
                "settings": {
                    "foreground": "#05acb5" // Color para void
                }
            },
            {
                "scope": "tag-break.cssc", // Color para break
                "settings": {
                    "foreground": "#999999" // Color para break
                }
            },
            {
                "scope": "tag-index.cssc", // Color para número de página
                "settings": {
                    "foreground": "#ff0000" // Color para número de página
                }
            },
            {
                "scope": "tag-pbba.cssc", // Color para pbba
                "settings": {
                    "foreground": "#0066aa" // Color para pbba
                }
            },
        ]
    },
```

### Guía de usuario

Los archivos CSScribe tienen la extensión `.cssc`. Es recomendable crear un directorio con un entorno de CSScribe para trabajar de forma más cómoda. Para ello, ejecuta el archivo `builder.py` en la carpeta que deseas convertir en entorno (borrará todo lo que haya ahí).


