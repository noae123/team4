let myP;

function loadAnime(){
    myP = document.querySelectorAll(".player");
    animateElement(myP[0], false, "pink", "butterfly");
    animateElement(myP[1], false, "brown", "circle");
    animateElement(myP[2], false, "white", "heart");
    animateElement(myP[3], false, "blue", "tear");
    animateElement(myP[4], false, "brown", "heart");
}

function changeDisplay(){
    let audios = document.querySelectorAll("audio");
    for (let i = 0; i < audios.length; i++) {
        audios[i].pause();
    }
    document.body.classList.toggle("previewClosed")
}