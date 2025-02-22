## *CSScribe*
---

This *markup language* is designed to be simple, yet powerful. It allows you to create beautiful research papers and projects with ease.

### Dependencies

   - *Visual Studio Code.*
   - *Markdown Preview Enhanced.*
   - *PrinceXML.*

### Compatibility

- [X] *Windows 10.*
- [X] *Windows 11.*
- [ ] *Linux* distributions (not tested).

### Installation

1. Install [*Visual Studio Code.*](https://code.visualstudio.com/download)
1. Install [*Markdown Preview Enhanced.*](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
1. Install [*PrinceXML.*](https://www.princexml.com/download/) Download the latest version of *PrinceXML.*
1. Go to the folder `C:\Program Files (x86)\Prince\engine\bin` and change the name of the file `prince.exe` to `pricexml.exe`.
1. Add `C:\Program Files (x86)\Prince\engine\bin` to *PATH* via system environment variables.
1. Now, search `Developer: Install Extension from Location` and select the `CSScribe-X.Y.Z` folder.
1. You're all done!

### User guide

Now that you have everything installed, you can start using *CSScribe.* The first step to open an empty folder and create a `.cssc` file.

Now you can start writing something. Try writing something like:

```cssc
/h2 Hello world!
```

You'll see that the whole line is colored blue (by the way, you can change all colors in the argument you copied to `settings.json`). The `/h2` modifier is transformed into a medium header once the code is compiled.

Since this is a markup language, everything you write is converted into text, unless so-called commands. You'll find a cheatsheet (`cheatsheet.pdf`) which includes all possible commands, learn them to exploit all the features of *CSScribe.*

Once you have the file ready, the first thing you have to do is to compile the `.cssc`. Compiling is really easy: run `compiler.py` in the same folder you're in and input the file name. Shortly after (quite literally, milliseconds), a `.md` file with the same name as the original file will appear.

To transform that file to a pretty, print-friendly file, you will have to open the `.md` file inside *VSC.* Then press `Ctrl + Shift + V` simultaneously to open the file in the *Markdown Preview Enhanced* extension. Don't worry about what you see inside there, just right-click, click on `Export` and then select `PDF (Prince)`.

The formatted *PDF* file will be created shortly after. However, it will undoubtedly be very ugly. That's because you haven't customized the *CSS.*

Don't worry, I have already done so for you. Inside the extension folder you'll find another folder named `style/`. Copy the code inside one of the many `style.less` files and paste it into `Markdown Preview Enhanced: Customize CSS (Global)` (you might be prompted to create the file).

Inside the `.less` file you'll also see at the top variables you can modify, feel free to modify them but you might not want to dive deep into the $300$ lines of code I barely understand (with a lot of `!important` lines because *PrinceXML* doesn't always like margins).

Compile it again and you'll have a beautifully looking document.

> You can access different fonts by replacing the variable value in the `.less` file. There are some font files already in the `fonts/` folder.

### Custom environments

For larger projects, you might want to use a custom environment which includes scripts and stuff which will help you organize your project. The `builder.py` utility will do so automatically. This feature is under development but it is working really well.

> Be careful when you execute `builder.py`, it will delete all files in the current folder, make sure to select a folder exclusively for the environment.

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

You're allowed to use the source code to write anything, without the need to mention me or *CSScribe* (but I'll appreciate it a lot).

### Credits

Thanks to the *PrinceXML* team and *Yiyi Wang* for the amazing software.