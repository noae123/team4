let myP;

function loadAnime(){
    myP = document.querySelector(".player");
    animateElement(myP, "ture", "red", "heart");
    document.getElementById('CiteLink').value = window.location.href.split('published.html')[0]+'shared.html';
}

function changeDisplay(){
    document.querySelector("audio").pause();
    document.body.classList.toggle("previewClosed")
}

function fallbackCopyTextToClipboard(text) {
    let textArea = document.createElement("textarea");
    textArea.value = text;

    // Avoid scrolling to bottom
    textArea.style.top = "0";
    textArea.style.left = "0";
    textArea.style.position = "fixed";

    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try {
        let successful = document.execCommand('copy');
        let msg = successful ? 'successful' : 'unsuccessful';
        console.log('Fallback: Copying text command was ' + msg);
    } catch (err) {
        console.error('Fallback: Oops, unable to copy', err);
    }

    document.body.removeChild(textArea);
}

function copyTextToClipboard() {
    let text = window.location.href.split('published.html')[0]+'shared.html'
    if (!navigator.clipboard) {
        fallbackCopyTextToClipboard(text);
        return;
    }
    navigator.clipboard.writeText(text).then(function() {
        console.log('Async: Copying to clipboard was successful!');
    }, function(err) {
        console.error('Async: Could not copy text: ', err);
    });
}