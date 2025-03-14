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

- [ ] *Linux* distributions (not supported).

### Installation

1. Install [*Visual Studio Code.*](https://code.visualstudio.com/download)

1. Install [*CSScribe*](https://marketplace.visualstudio.com/items?itemName=alejandro-vaz.csscribe)

1. Install [*PrinceXML.*](https://www.princexml.com/download/) Download the latest version of *PrinceXML.*

1. Go to the folder `C:\Program Files (x86)\Prince\engine\bin` and change the name of the file `prince.exe` to `pricexml.exe` (you might want to keep the original file).

1. Add `C:\Program Files (x86)\Prince\engine\bin` to *PATH* via system environment variables.

1. You're all done!

### User guide

Now that you have everything installed, you can start using *CSScribe.* The first step to open an empty folder and create a `.cssc` file.

Now you can start writing something. Try writing something like:

```cssc
/h2 Hello world!
---
```

You'll see that the whole line is colored orange. The `/h2` modifier is transformed into a medium header once the code is compiled.

Since this is a markup language, everything you write is converted into text, unless so-called commands. This [link](https://csscribe.ct.ws) will teach you all possible commands, learn them to exploit all the features of *CSScribe.*

Once you have the file ready, the first thing you have to do is to compile the `.cssc`. Compiling is really easy: execute `CSScribe** Run Compiler` from the command palette. Shortly after (quite literally, milliseconds), a `.md` file with the same name as the original file will appear.

To transform that file to a pretty, print-friendly file, you will have to open the `.md` file inside *VSC.* Then press `Ctrl + Shift + V` simultaneously to open the file in the *Markdown Preview Enhanced* extension.

> A `.crossnote` folder will appear the moment you run the compiler. This is made so that *Markdown Preview Enhanced* extension picks up the `style.less` file and applies it to your document. Inside the `.less` file you'll also see at the top variables you can modify, feel free to modify them but you might not want to dive deep into the `300` lines of code I barely understand (with a lot of `!important` lines because *PrinceXML* doesn't always like margins).

### Custom environments

For larger projects, you might want to use a custom environment which will help you organize your project. The `CSScribe** Run Builder` utility will do so automatically. This feature will create some structure in your directory.

### Other tools

1. Versioning System: `CSScribe** Run Versioning System` uses a random algorithm to determine the next version of your project.

1. JPG2PNG: `CSScribe** Run JPG2PNG` will convert all `.jpg` or `.jpeg` files into `.png`.

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

You're allowed to use the program code to write anything, without the need to mention me or *CSScribe* (but I'll appreciate it a lot).

### Credits

Thanks to the *PrinceXML* team and *Yiyi Wang* for the amazing software.