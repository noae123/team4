const message = document.getElementById("message");
const sender = document.getElementById("sender");

function loadMessage(){
    message.classList.add("place_holder");
    sender.classList.add("place_holder");
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
    if(sender_name === ""){
        sender.innerHTML = "Sender Name";
        sender.classList.add("place_holder");
    }
    else{
        sender.innerHTML = sender_name;
        sender.classList.remove("place_holder");
    }
}

function change_message(message_txt){
    const checkText = document.getElementById("radioDir").checked;
    if(message_txt === ""){
        message.innerHTML = "Card Banner";
        message.classList.add("place_holder");
    }
    else{
        message.innerHTML = message_txt;
        message.classList.remove("place_holder");
    }
    create_text_animation(message, document.querySelector(".Audio_Title"), checkText);
}

function changTextDir(change_dir){
    let myText = [...document.querySelectorAll(".Audio_Title")];
    const Audio_Name = document.getElementById("Audio_Name");
    const Choose_Categories = document.getElementById("Choose_Categories");
    myText.push(Audio_Name);
    myText.push(Choose_Categories);
    for(let i =0; i<myText.length; i++){
        if(myText[i].getAttribute('dir')!=='rtl'){
            myText[i].setAttribute('dir', 'rtl');
        }
        else{
            myText[i].setAttribute('dir', 'ltr');
        }
    }
    create_text_animation(message, document.querySelector(".Audio_Title"), change_dir);
}