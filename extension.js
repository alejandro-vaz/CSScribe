// IMPORTS
const vscode = require('vscode')
const fs = require("fs")
const path = require("path")

// MAIN FUNCTION
function activate(context) {
    // CONFIGURATION
    const config = vscode.workspace.getConfiguration('csscribe');
    const language = config.get('language');
    const style = config.get("style");
    console.log(`Extension activated with language ${language} and style ${style}.`);
    // RUN COMPILER COMMAND
    let runCompiler = vscode.commands.registerCommand('csscribe.runCompiler', () => {
        console.log("Executed: csscribe.runCompiler");
        const compilerPath = context.asAbsolutePath("compiler.exe");
        const terminal = vscode.window.createTerminal('Compiler Terminal');
        terminal.sendText(`${compilerPath} ${language}`);
        terminal.show();
        vscode.commands.executeCommand('csscribe.parseStyle');
    });
    context.subscriptions.push(runCompiler);
    // RUN BUILDER COMMAND
    let runBuilder = vscode.commands.registerCommand('csscribe.runBuilder', () => {
        console.log("Executed: csscribe.runBuilder");
        const builderPath = context.asAbsolutePath('builder.exe');
        const terminal = vscode.window.createTerminal('Builder Terminal');
        terminal.sendText(`${builderPath} ${language}`);
        terminal.show();
        vscode.commands.executeCommand('csscribe.parseStyle');
    });
    context.subscriptions.push(runBuilder);
    // RUN JPG2PNG COMMAND
    let runJPG2PNG = vscode.commands.registerCommand('csscribe.runJPG2PNG', () => {
        console.log("Executed: csscribe.runJPG2PNG");
        const JPG2PNGpath = context.asAbsolutePath('jpg2png.exe');
        const terminal = vscode.window.createTerminal('JPG to PNG Terminal');
        terminal.sendText(`${JPG2PNGpath} ${language}`);
        terminal.show();
    });
    context.subscriptions.push(runJPG2PNG);
    // RUN VERSIONING SYSTEM
    let runVersioningSystem = vscode.commands.registerCommand("csscribe.runVersioningSystem", () => {
        console.log("Executed: csscribe.runVersioningSystem");
        const versioningSystemPath = context.asAbsolutePath("versioning.exe");
        const terminal = vscode.window.createTerminal("Versioning System Terminal");
        terminal.sendText(`${versioningSystemPath} ${language}`);
        terminal.show();
    });
    context.subscriptions.push(runVersioningSystem);
    // PARSE STYLE
    let parseStyle = vscode.commands.registerCommand("csscribe.parseStyle", () => {
        console.log("Executed: csscribe.parseStyle");
        const stylePath = context.asAbsolutePath(`style/${style}.less`);
        const fontsPath = context.asAbsolutePath('fonts');
        const targetDir = path.join(vscode.workspace.rootPath, ".crossnote");
        const targetPath = path.join(targetDir, "style.less");
        if (!fs.existsSync(targetDir)) {
            fs.mkdirSync(targetDir);
        }
        if (fs.existsSync(targetPath)) {
            return;
        }
        fs.readFile(stylePath, "utf-8", (err, data) => {
            if (err) {
                console.log(`Error reading file from disk: ${err}`)
            } else {
                const updatedData = data.replace(/¿\?/g, fontsPath.replace(/\\/g, '/'));
                fs.writeFile(targetPath, updatedData, "utf-8", (err) => {
                    if (err) {
                        console.log(`Error writing file to disk: ${err}`);
                    } else {
                        console.log(`${style}.less pasted successfully into the workspace.`);
                    }
                });
            }
        });
    });
    context.subscriptions.push(parseStyle)

// COMPLETION ITEM PROVIDER
const completionProvider = vscode.languages.registerCompletionItemProvider('cssc', {
    provideCompletionItems(document, position, token, completionContext) {
        try {
            // DEFINE PATHS AND REQUIREMENTS
            const completionWordsPath = path.join(context.extensionPath, `language/${language}.json`);
            const completionWords = require(completionWordsPath);
            
            // INITIALIZE VARIABLES
            const linePrefix = document.lineAt(position).text.substr(0, position.character);
            const text = document.getText();
            
            // BUILD WORD FREQUENCY MAP
            const wordFrequency = {};
            const words = text.match(/\b\w+\b/g);
            if (words) {
                words.forEach(word => {
                    const lowerWord = word.toLowerCase();
                    wordFrequency[lowerWord] = (wordFrequency[lowerWord] || 0) + 1;
                });
            }
            
            // FUNCTION TO SET sortText BASED ON FREQUENCY
            const setSortText = (item, frequency) => {
                // Invert frequency for correct sorting (higher frequency = should appear first)
                // Pad with zeros to ensure proper lexicographical sorting
                const invertedFrequency = String(99999 - frequency).padStart(5, '0');
                item.sortText = invertedFrequency + item.label;
            };
            
            // FUNCTION TO CAPITALIZE FIRST LETTER
            const capitalizeFirstLetter = (word) => {
                return word.charAt(0).toUpperCase() + word.slice(1);
            };
            
            // DETERMINE IF CURRENT WORD STARTS WITH UPPERCASE
            const currentWordRange = document.getWordRangeAtPosition(position);
            const currentWord = currentWordRange ? document.getText(currentWordRange) : '';
            const isCurrentWordCapitalized = currentWord.charAt(0) === currentWord.charAt(0).toUpperCase();
            
            // CREATE COMPLETION ITEMS FROM completionWords
            let completionItems = completionWords.map(word => {
                // Skip single-letter words
                if (word.length === 1) {
                    return null;
                }
                const item = new vscode.CompletionItem(word, vscode.CompletionItemKind.Text);
                setSortText(item, wordFrequency[word.toLowerCase()] || 0);
                // Capitalize if current word starts with uppercase
                if (isCurrentWordCapitalized) {
                    item.label = capitalizeFirstLetter(item.label);
                }
                return item;
            }).filter(item => item !== null);
            
            // ADD WORDS ALREADY IN THE FILE
            const wordsInFile = new Set(words);
            wordsInFile.forEach(word => {
                // Skip single-letter words
                if (word.length === 1) {
                    return;
                }
                const item = new vscode.CompletionItem(word, vscode.CompletionItemKind.Text);
                setSortText(item, wordFrequency[word.toLowerCase()]);
                // Capitalize if current word starts with uppercase
                if (isCurrentWordCapitalized) {
                    item.label = capitalizeFirstLetter(item.label);
                }
                completionItems.push(item);
            });
            
            // REMOVE DUPLICATE ITEMS
            const uniqueItems = new Map();
            completionItems.forEach(item => {
                uniqueItems.set(item.label, item);
            });
            
            // RETURN SORTED ITEMS
            return Array.from(uniqueItems.values());
        } catch (error) {
            console.error(`Error loading completion words or commands: ${error}`);
            return [];
        }
    }
});



    context.subscriptions.push(completionProvider);
}

// DEACTIVATION FUNCTION
function deactivate() {
    // LOG DEACTIVATION
    console.log("Extension deactivated.")
}

// EXPORT FUNCTIONS
module.exports = {
    activate,
    deactivate
};
