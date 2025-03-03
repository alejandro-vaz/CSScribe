const vscode = require('vscode')

function activate(context) {
    console.log('Extension activated.');
    // Example: Register a command that shows a message.
    let disposable = vscode.commands.registerCommand('csscribe.function', () => {
        vscode.window.showInformationMessage('Hello from CSScribe!\nThis is currently under development!');
    });

    context.subscriptions.push(disposable);
}

function deactivate() {
    console.log("Extension deactivated.")
}

module.exports = {
    activate,
    deactivate
};
