// IMPORT VSCODE
const vscode = require('vscode')

// MAIN FUNCTION
function activate(context) {
    // LOG ACTIVATION
    language = "en";
    console.log(`Extension activated with language "${language}."`);
    // RUN COMPILER COMMAND
    let runCompiler = vscode.commands.registerCommand('csscribe.runCompiler', () => {
        console.log("Executed: csscribe.runCompiler");
        const compilerPath = context.asAbsolutePath("compiler.exe");
        const terminal = vscode.window.createTerminal('Compiler Terminal');
        terminal.sendText(`${compilerPath} ${language}`);
        terminal.show();
    });
    context.subscriptions.push(runCompiler);
    // RUN BUILDER COMMAND
    let runBuilder = vscode.commands.registerCommand('csscribe.runBuilder', () => {
        console.log("Executed: csscribe.runBuilder");
        const builderPath = context.asAbsolutePath('builder.exe');
        const terminal = vscode.window.createTerminal('Builder Terminal');
        terminal.sendText(`${builderPath} ${language}`);
        terminal.show();
    });
    context.subscriptions.push(runBuilder);
    // RUN JPG2PNG COMMAND
    let runJPG2PNG = vscode.commands.registerCommand('csscribe.runJPG2PNG', () => {
        console.log("Executed: csscribe.runJPG2PNG");
        const JPG2PNGpath = context.asAbsolutePath('jpg2png.exe');
        const terminal = vscode.window.createTerminal('JPG to PNG Terminal');
        terminal.sendText(`${JPG2PNGpath}`);
        terminal.show();
    });
    context.subscriptions.push(runJPG2PNG);
    // RUN VERSIONING SYSTEM
    let runVersioningSystem = vscode.commands.registerCommand("csscribe.runVersioningSystem", () => {
        console.log("Executed: csscribe.runVersioningSystem");
        const versioningSystemPath = context.asAbsolutePath("versioning.exe");
        const terminal = vscode.window.createTerminal("Versioning System Terminal");
        terminal.sendText(`${versioningSystemPath}`);
        terminal.show();
    });
    context.subscriptions.push(runVersioningSystem);
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
