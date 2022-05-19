let myP;

function loadAnime(){
    myP = document.querySelector(".player");
    animateElement(myP, "true", "white", "circle");
}

function changeDisplay(){
    document.querySelector("audio").pause();
    document.body.classList.toggle("previewClosed")
}

function replace_music(music_file){
    let music = document.querySelector("audio");
    music.setAttribute('src', URL.createObjectURL(music_file[0]));///'../static/music/' + smthing[0].name);
}

function replace_image(img_file){
    let image = document.querySelector(".mmg");
    image.setAttribute('src', URL.createObjectURL(img_file[0]));
}

function change_sender(sender_name){
    const sender = document.getElementById("sender");
    sender.innerHTML = sender_name;
}

function change_message(message_txt){
    const message = document.getElementById("message");
    message.innerHTML = message_txt;
    create_text_animation(message, document.querySelector(".Audio_Title"));
}

function changTextDir(change_dir){
    const text = document.querySelectorAll(".Audio_Title");
    const message = document.getElementById("message");
    for(let i =0; i<text.length; i++){
        if(text[i].getAttribute('dir')!=='rtl'){
            text[i].setAttribute('dir', 'rtl');
        }
        else{
            text[i].setAttribute('dir', 'ltr');
        }
    }
    create_text_animation(message, document.querySelector(".Audio_Title"), Boolean(change_dir));
}




