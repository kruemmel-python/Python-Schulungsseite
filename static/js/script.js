function copyToClipboard() {
    var codeBlock = document.getElementById('code-block');
    var textArea = document.createElement('textarea');
    textArea.value = codeBlock.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    alert('Code kopiert!');
}
