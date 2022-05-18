let myP;
function loadAnime(){
    myP = [...document.querySelectorAll(".player")];
    for (let i=0; i<myP.length; i++){
        animateElement(myP[i], "false", "white", "butterfly");
    }
}

function changeDisplay(){
    let myPDisplay = window.getComputedStyle(myP[0]);
    if(myPDisplay.getPropertyValue('display') == "block"){
        let music = document.querySelector("audio");
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
    let music = document.querySelector("audio");
    music.setAttribute('src', URL.createObjectURL(smthing[0]));///'../static/music/' + smthing[0].name);
}

function replace_image(smthing){
    let image = document.querySelector(".mmg");
    image.setAttribute('src', URL.createObjectURL(smthing[0]));
}


