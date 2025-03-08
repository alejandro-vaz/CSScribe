// IMPORTS
const vscode = require('vscode')
const fs = require("fs")
const path = require("path")

// MAIN FUNCTION
function activate(context) {
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
