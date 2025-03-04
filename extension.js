/* COMMANDS 
vscode.window.showInformationMessage('Hello from CSScribe! This is currently under development!'); // Lower right information message.
const terminal = vscode.window.createTerminal('Compiler Terminal'); // Creates a terminal with a name
terminal.sendText(`${compilerPath}`); // Sends a command to terminal
terminal.show(); // Shows the terminal to the user
const compilerPath = context.asAbsolutePath('compiler.exe'); // Especify an absolute path
*/ 

// IMPORT VSCODE
const vscode = require('vscode')

// MAIN FUNCTION
function activate(context) {
    // LOG ACTIVATION
    console.log('Extension activated.');
    // RUN COMPILER COMMAND
    let runCompiler = vscode.commands.registerCommand('csscribe.runCompiler', () => {
        console.log("Executed: csscribe.runCompiler")
        const compilerPath = context.asAbsolutePath('compiler.exe');
        const terminal = vscode.window.createTerminal('Compiler Terminal');
        terminal.sendText(`${compilerPath}`);
        terminal.show();
    });
    context.subscriptions.push(runCompiler);
    // RUN BUILDER COMMAND
    let runBuilder = vscode.commands.registerCommand('csscribe.runBuilder', () => {
        console.log("Executed: csscribe.runBuilder")
        const builderPath = context.asAbsolutePath('builder.exe');
        const terminal = vscode.window.createTerminal('Builder Terminal');
        terminal.sendText(`${builderPath}`);
        terminal.show();
    });
    context.subscriptions.push(runBuilder);
    // RUN JPG2PNG COMMAND
    let runJPG2PNG = vscode.commands.registerCommand('csscribe.runJPG2PNG', () => {
        console.log("Executed: csscribe.runJPG2PNG")
        const JPG2PNGpath = context.asAbsolutePath('jpg2png.exe');
        const terminal = vscode.window.createTerminal('JPG to PNG Terminal');
        terminal.sendText(`${JPG2PNGpath}`);
        terminal.show();
    });
    context.subscriptions.push(runJPG2PNG);
}

// DEACTIVATION FUNCTION
function deactivate() {
    // LOG DEACTIVATION
    console.log("Extension deactivated.")
}

// EXPORTS FUNCTIONS
module.exports = {
    activate,
    deactivate
};
