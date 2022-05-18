let myP;
function loadAnime(){
    myP = [...document.querySelectorAll(".player")];
    for (let i=0; i<myP.length; i++){
        animateElement(myP[i], "false", "black");
    }
}

function changeDisplay(){
    let myPDisplay = window.getComputedStyle(myP[0]);
    if(myPDisplay.getPropertyValue('display') == "block"){
        let music = [...document.querySelectorAll("audio")][0];
        music.pause();
        myP[0].style.display = "none";
        document.getElementById('audioPreview').innerText = 'Open Preview';
    }
    else{
        myP[0].style.display = "block";
        document.getElementById('audioPreview').innerText = 'Close Preview';
    }
}

function replace_music(smthing){
    let music = [...document.querySelectorAll("audio")][0];
    music.setAttribute('src', '../static/music/' + smthing[0].name);
    if(document.getElementById("Audio_Name").value == ""){
        document.getElementById("Audio_Name").setAttribute('value',smthing[0].name);
    }
}

function replace_image(smthing){
    let image = [...document.querySelectorAll(".mmg")][0];
    image.setAttribute('src', '../static/images/' + smthing[0].name);
}

