function makeRequest(url) {
    window.location = url;
    return;
    httpRequest = new XMLHttpRequest();

    if (!httpRequest) {
      alert('Giving up :( Cannot create an XMLHTTP instance');
      return false;
    }
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === httpRequest.DONE){
            alert("your video was deleted");
            window.location = url;
        }
    };
    httpRequest.open('POST', url);
    httpRequest.send();
}
