pyinstaller --onefile --noupx --icon=public/logo.png --distpath ./ source/compiler.py & pyinstaller --onefile --noupx --icon=public/logo.png --distpath ./ source/builder.py & pyinstaller --onefile --noupx --icon=public/logo.png --distpath ./ source/jpg2png.py & pyinstaller --onefile --noupx --icon=public/logo.png --distpath ./ source/versioning.py & rmdir "build/" /s /q & del builder.spec & del compiler.spec & del jpg2png.spec & del versioning.spec

vsce package

del builder.exe & del compiler.exe & del jpg2png.exe & del versioning.exe & del README.md & del changelog.md & del website\cheatsheet.pdf