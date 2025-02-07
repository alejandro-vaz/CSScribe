### FastMarkDown

Este lenguaje de programación está diseñado para estandarizar el uso de MarkDown y hacer más fácil la redacción de contenido. El lenguaje de programación es capaz de crear documentos PDF a partir de código sin intervención del usuario.

Es capaz de insertar bloques de código, bloques aparte, fórmulas matemáticas, imágenes y muchos otros recursos de forma automática y estilizada por defecto.


### Dependencias

   - VSCode
   - FastMarkDown
   - Markdown Preview Enhanced

   - PrinceXML
   - `settings.json`

### Compatibilidad

- [X] Windows 10 (todas las versiones)
- [X] Windows 11 (todas las versiones)
- [ ] Linux (no comprobado)


### Guía de instalación

Primero necesitarás instalar [Visual Studio Code,](https:/```.visualstudio.com/) requisito imprescindible.

Necesitarás después instalar la extensión de FastMarkDown. Para ello, presiona Ctrl + Shift + P dentro de VSCode y busca `Developer: Install Extension from Location...`. Luego, selecciona la carpeta de la extensión FastMarkDown (`fastmarkdown-V.E.R`).

Después, acude al Marketplace de extensiones y busca `Markdown Preview Enhanced`, de Yiyi Wang. Instala la extensión.

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
                "scope": "fmd.bold.fmd",
                "settings": {
                    "foreground": "#94eb52", // Color para texto en negrita
                    "fontStyle": "bold" // Añadir estilo de negrita
                }
            },
            {
                "scope": "fmd.italic.fmd",
                "settings": {
                    "foreground": "#09acb5", // Color para texto en cursiva
                    "fontStyle": "italic" // Añadir estilo de cursiva
                }
            },
            {
                "scope": "fmd.strikethrough.fmd",
                "settings": {
                    "foreground": "#ff3c00", // Color para texto tachado
                    "fontStyle": "strikethrough" // Añadir estilo de tachado
                }
            },
            {
                "scope": "fmd.subscript.fmd",
                "settings": {
                    "foreground": "#ff0000" // Color para subíndices
                }
            },
            {
                "scope": "fmd.superscript.fmd",
                "settings": {
                    "foreground": "#00ff00" // Color para superíndices
                }
            },
            {
                "scope": "fmd.code.fmd",
                "settings": {
                    "foreground": "#9494ff" // Color para bloques de código
                }
            },
            {
                "scope": "fmd.icode.fmd",
                "settings": {
                    "foreground": "#9494ff" // Color para bloques de código
                }
            },
            {
                "scope": "fmd.comment.fmd",
                "settings": {
                    "foreground": "#6b6b6b" // Color para comentarios
                }
            },
            {
                "scope": "fmd.h1.fmd",
                "settings": {
                    "foreground": "#00ff00", // Color para encabezados de nivel 1
                    "fontStyle": "bold"
                }
            },
            {
                "scope": "fmd.h2.fmd",
                "settings": {
                    "foreground": "#00ffff", // Color para encabezados de nivel 2
                    "fontStyle": "bold"
                }
            },
                        {
                "scope": "fmd.h3.fmd",
                "settings": {
                    "foreground": "#ffff00", // Color para encabezados de nivel 2
                    "fontStyle": "bold"
                }
            },
            {
                "scope": "fmd.img.fmd",
                "settings": {
                    "foreground": "#ff00ff", // Color para imágenes
                    "fontStyle": "underline"
                }
            },
            {
                "scope": "fmd.side.fmd",
                "settings": {
                    "foreground": "#aaa" // Color para definiciones
                }
            },
            {
                "scope": "fmd.void.fmd",
                "settings": {
                    "foreground": "#05acb5" // Color para void
                }
            },
            {
                "scope": "fmd.done.fmd",
                "settings": {
                    "foreground": "#02e9f5" // Color para done
                }
            },
            {
                "scope": "fmd.ol.fmd",
                "settings": {
                    "foreground": "#ffff00" // Color para numerados
                }
            },
            {
                "scope": "fmd.ul.fmd",
                "settings": {
                    "foreground": "#ffff00" // Color para apuntados
                }
            },
            {
                "scope": "fmd.brochet.fmd", // Color para brochet
                "settings": {
                    "foreground": "#ffff00",
                }
            },
            {
                "scope": "fmd.imath.fmd", // Color para matemáticas en linea
                "settings": {
                    "foreground": "#ffffaa",
                }
            },
            {
                "scope": "fmd.math.fmd", // Color para matemáticas
                "settings": {
                    "foreground": "#ffffaa",
                }
            },
            {
                "scope": "fmd.newline.fmd", // Color para nuevo párrafo
                "settings": {
                    "foreground": "#6b6b6b" // Color para nuevo párrafo
                }
            },
            {
                "scope": "fmd.scape.fmd", // Color para scape
                "settings": {
                    "foreground": "#111111" // Color para scape
                }
            },
            {
                "scope": "fmd.index.fmd", // Color para número de página
                "settings": {
                    "foreground": "#ff0000" // Color para número de página
                }
            },
            {
                "scope": "fmd.pbba.fmd", // Color para pbba
                "settings": {
                    "foreground": "#0066aa" // Color para pbba
                }
            },
            {
                "scope": "fmd.break.fmd", // Color para break
                "settings": {
                    "foreground": "#999999" // Color para break
                }
            }
        ]
    },
```

### Guía de usuario

Los archivos FastMarkDown tienen la extensión `.fmd`. Es recomendable crear un directorio con un entorno de FastMarkDown para trabajar de forma más cómoda. Para ello, ejecuta el archivo `builder.py` en la carpeta que deseas convertir en entorno (borrará todo lo que haya ahí).

Puedes abrir `fmdcompiler.py` para ver la nomenclatura específica y cosas que puedes hacer con FastMarkDown.
