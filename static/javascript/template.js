let myP;

function loadAnime(){
    myP = document.querySelectorAll(".player");
    for (let i = 0; i < myP.length; i++) {
        animateElement(myP[i], "ture", "red", "heart");
    }

}