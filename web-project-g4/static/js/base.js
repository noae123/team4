function changeDisplay() {
  let audios = document.querySelectorAll("audio");
  for (let i = 0; i < audios.length; i++) {
    audios[i].pause();
  }
  document.body.classList.toggle("previewClosed");
}