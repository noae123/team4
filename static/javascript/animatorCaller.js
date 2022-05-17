window.onload = (event) => {
    const myP = document.querySelectorAll(".player");
    for (let i = 0; i < myP.length; i++){
        animateElement(myP[i], "false", "white");
    }
};