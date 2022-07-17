function loadAnime() {
  myP = document.querySelectorAll(".player");
  animateElement(myP[0], false, "pink", "butterfly");
}

function onPlay() {
  userStartAudio();
}

/* color mapping*/
const colorMap = {
  red: [235, 37, 19, 255],
  orange: [231, 105, 20, 255],
  yellow: [252, 204, 4, 255],
  green: [150, 209, 48, 255],
  blue: [18, 78, 120, 255],
  purple: [179, 39, 132,255],
  black: [0, 0, 0,255],
  brown: [64, 50, 51,255],
  pink: [243, 16, 102,255]
}
const colorDefault = [255, 255, 255,255];
function translateColor(colorA){
  return colorMap[colorA] || colorDefault;
}

/*shapes*/
function translateShape(shapeA, index, sp5){
  switch (shapeA){
    case("tear_M"):
      return sp5.map(index, -1, 1, 45, 60);
    case("tear_S"):
      return sp5.map(index, -1, 1, 30, 42);
    case("butterfly_S"):
      return sp5.map(index, -1, 1, 60, 130);
    case("butterfly_M"):
      return sp5.map(index, -1, 1, 110, 160);
    case ("tri_S"):
    case("square_S"):
      return sp5.map(index, -1, 1, 60, 130);
    case ("tri_M"):
    case("square_M"):
      return sp5.map(index, -1, 1, 140, 180);
    case ("circle_S"):
      return sp5.map(index, -1, 1, 120, 180);
    case ("circle_M"):
      return sp5.map(index, -1, 1, 180, 300);
    case ("heart_S"):
      return sp5.map(index, -1, 1, 3, 8);
    default :
      return sp5.map(index, -1, 1, 8, 12);
  }
}

function X_calc(shape, r, i, t, sp5){
  switch (shape){
    case('tear'):
      return r* 7 * sp5.sin(i) ** 4 * sp5.cos(i) * t;
    case('butterfly'):
      return r* 4 * sp5.sin(i) ** 2 * sp5.cos(i) ** 2 * t;
    case ("circle"):
      return r * sp5.sin(i) * 0.5 * t;
    case ("square"):
      return r * sp5.sin(i) ** 3 * t;
    case ('tri'):
      return r * sp5.sin(i) ** 2 * t;
    default:
      return r* 16 * sp5.sin(i) ** 3 * t;
  }
}

function Y_calc(shape, r, i, sp5){
  let y;
  if(shape.startsWith("circle")){
    y = r * sp5.cos(i) * 0.5;
  }
  else if (shape.startsWith("square")){
    y = r * sp5.cos(i) ** 3;
  }
  else if (shape.startsWith("tri")){
    y = -r * sp5.cos(i) ** 2 +40;
  }
  else if(shape.startsWith("tear")){
    y = -r*( 4 * sp5.sin(i) ** 2 * sp5.cos(i) ** 2 + 3*sp5.cos(2*i));
  }
  else if(shape.startsWith("butterfly")){
    y = r* 4 * sp5.sin(i) ** 4 * sp5.cos(i);
  }
  else{
    let y_move;
    if(shape === "heart_S"){
      y_move = 15;
    }
    else{
      y_move = 30;
    }
    y = -r*(13 * sp5.cos(i) - 5*sp5.cos(2*i) - 2*sp5.cos(3*i) -sp5.cos(4*i)) - y_move;
  }
  return y;
}

function getRandPos(shape, sp5){
  let r;
  switch (shape){
    case('tear'):
      r=55;
      break;
    case ("butterfly"):
      r = 140;
      break;
    case ("tri"):
    case ("square"):
      r = 170;
      break;
    default:
      r = 10.5;
  }
  if(shape === "circle"){
    return p5.Vector.random2D().mult(126);
  }
  else{
    let i = sp5.random(0,360);
    let x = X_calc(shape, r, i, 1, sp5);
    let y = Y_calc(shape+'_M', r, i, sp5);
    if(shape === "tri" || shape ==='butterfly'){
      let plusOrMinus = Math.random() < 0.5 ? -1 : 1;
      x = x * plusOrMinus;

      let p2 = Math.random() < 0.5 ? -1 : 1;
      if (p2<0 && shape === "tri"){
        y = r - 123.3;
      }
    }
    return sp5.createVector(x, y);
  }
}

function create_text_animation(titleText, audioTitle, backword){
  titleText.getAnimations().forEach(a => a.cancel());
  let defaultDelay = 75;
  let defaultWidth = 3734;
  if (titleText.offsetWidth > audioTitle.offsetWidth) {
    let width = titleText.offsetWidth;
    this.newDelay = defaultDelay * (width / defaultWidth) * 1000
    let precTrans = 90;
    precTrans = backword ? precTrans : -precTrans;
    titleText.animate(
          [
            // keyframes
            { transform: "translate(0, 0)" },
            { transform: "translate(" + precTrans + "%, 0)" },
          ],
          {
            // timing options
            delay: 2000,
            duration: this.newDelay,
            iterations: Infinity,
          }
      );
  }
}

/*main animate function*/
function animateElement_selector(
  /**string*/ mainDiv,
  /**boolean*/ backwards = false,
  /**string {{color}}*/ colorA= "{{ colorA }}",
  /**string {{color}}*/ shapeA = "{{ colorA }}"
) {
  return animateElement(document.getElementById(mainDiv), backwards, colorA, shapeA);
}

function animateElement(
  /**HTMLDivElement*/ mainDiv,
  /**boolean*/ backwards = false,
  /**string {{color}}*/ colorA= "{{ colorA }}",
  /**string {{color}}*/ shapeA = "{{ colorA }}"
) {
  const element = mainDiv.querySelector("div.imgbox");
  const audioNode = mainDiv.querySelector("audio");
  const titleText = mainDiv.querySelector(".scrollTitle");
  const audioTitle = mainDiv.querySelector(".Audio_Title");
  const colorChanger = document.querySelectorAll(".color");
  const shapeChanger = document.querySelectorAll(".shape");
  //create a color for animation to make more "cool" and "diverse" though look at this code and tell me that the client don't get an additional value
  colorA = translateColor(colorA);
  // endregion

  //region text animation
  create_text_animation(titleText, audioTitle, backwards);
  // endregion

  //region color changer
  for(let i =0; i< colorChanger.length; i++){
    colorChanger[i].onclick = theirColor;
    function theirColor(){
      let audio_mode = audioNode.paused;
      audioNode.pause();
      if (audio_mode !== true){
        setTimeout(play_pause_music, 10);
      }
      colorA = translateColor(this.id);
    }
  }
  //endregion

  //region color changer
  for(let i =0; i< shapeChanger.length; i++){
    shapeChanger[i].onclick = theirShape;
    function theirShape(){
      let audio_mode = audioNode.paused;
      audioNode.pause();
      if (audio_mode !== true){
        setTimeout(play_pause_music, 10);
      }
      shapeA = this.id;
    }
  }
  //endregion

  // region P5
  let myP5;
  function play_pause_music(){
    myP5.userStartAudio();
    let audios = document.querySelectorAll("audio");
    for (let i = 0; i < audios.length; i++) {
      if(audios[i]!==audioNode){
        audios[i].pause();
      }
    }
    audioNode[audioNode.paused ? "play" : "pause"]();
  }
  element.onclick = play_pause_music;

  const sketch = (sp5) => {
    // eslint-disable-next-line no-unused-vars
    let can, fft, amp;
    let wave_paused = null;
    let particles = [];
    sp5.mouseClicked = () => {
      sp5.userStartAudio();
    };
    sp5.setup = () => {
      //this.p5 = sp5;
      //create canvas object
      can = sp5.createCanvas(element.clientWidth, element.clientHeight);
      can.parent(element);
      can.position(0, 0);
      sp5.angleMode("degrees");

      let audioContext = sp5.getAudioContext();
      // // wire all media elements up to the p5.sound AudioContext
      let mediaSource;
      try{
        mediaSource = audioContext.createMediaElementSource(audioNode);

        mediaSource.connect(sp5.soundOut);
      }
      catch(error){
      }

      fft = new p5.FFT();
      wave_paused = fft.waveform();
    };

    sp5.windowResized = () => {
      sp5.resizeCanvas(element.clientWidth, element.clientHeight);
    };

    sp5.draw = () => {
      sp5.clear();
      sp5.noFill();
      sp5.strokeWeight(6);
      let wave;

      fft.analyze();
      amp = fft.getEnergy(20, [200]);
      sp5.stroke(colorA);

      sp5.translate(sp5.width / 2, sp5.height / 2);

      if (!audioNode.paused) {
        wave = fft.waveform();
      } else {
        wave = wave_paused;
        sp5.triangle(25, 0, -12.5, 25, -12.5, -25);
      }

      for (let t = -1; t <= 1; t += 2) {
        sp5.beginShape();
        for (let i = 0; i <= 180; i += 1) {
          let index = Math.floor(sp5.map(i, 0, 180, 0, wave.length - 1));
          let r = translateShape(shapeA + '_M', wave[index], sp5);
          let x = X_calc(shapeA, r, i,t, sp5);
          let y = Y_calc(shapeA + '_M', r, i, sp5);
          sp5.vertex(x, y);
        }
        sp5.endShape();
      }
      if (shapeA === "tri"){
        for (let t = -1; t <= 1; t += 2) {
          sp5.beginShape();
          for (let i = 0; i <= 180; i += 1) {
            let index = Math.floor(sp5.map(i, 0, 180, 0, wave.length - 1));
            let r = translateShape(shapeA + '_M', wave[index], sp5);
            let x = X_calc(shapeA, r, i,t, sp5);
            let y = r - 121.3;
            sp5.vertex(x, y);
          }
          sp5.endShape();
        }
      }
      sp5.strokeWeight(4);
      for (let t = -1; t <= 1; t += 2) {
        sp5.beginShape();
        for (let i = 0; i <= 180; i += 1) {
          let index = Math.floor(sp5.map(i, 0, 180, 0, wave.length - 1));
          let r = translateShape(shapeA + '_S', wave[index], sp5);
          let x = X_calc(shapeA, r, i,t, sp5);
          let y = Y_calc(shapeA + '_S', r, i, sp5);
          sp5.vertex(x, y);
        }
        sp5.endShape();
      }

      if (!audioNode.paused) {
        let p = new Particle(amp, sp5, colorA, shapeA);

        particles.push(p);
        if (amp > 180) {
          let a = new Particle(amp, sp5, colorA, shapeA);
          particles.push(a);
        }
        if (amp > 220) {
          let a = new Particle(amp, sp5, colorA, shapeA);
          particles.push(a);
          a = new Particle(amp, sp5, colorA, shapeA);
          particles.push(a);
        }
        for (let i = particles.length - 1; i >= 0; i--) {
          if (!particles[i].delete(sp5)) {
            particles[i].update(amp);
            particles[i].show(sp5);
          } else {
            particles.splice(i, 1);
          }
        }
      } else {
        for (let i = particles.length - 1; i >= 0; i--) {
          particles.splice(i, 1);
        }
      }
    };
  };
  myP5 = new p5(sketch);
  return myP5;
  // endregion P5
}

/* flying partical class*/
class Particle {
  constructor(amp, p5, colorA, shape) {
    this.pos = getRandPos(shape, p5);
    this.vel = p5.createVector(p5.random(0.0002, 0.00001));
    this.acc = this.pos.copy().mult(p5.random(0.0002, 0.00001));
    this.w = p5.random(3, 10);
    this.color = [...colorA];
    this.color[3] = p5.random(255 - amp, 255) + 40
  }

  update(amp) {
    if (amp > 200) {
      this.acc.mult(1 + amp / 200 / 10);
    }
    this.vel.add(this.acc);
    this.pos.add(this.vel);
  }

  show(p5) {
    p5.noStroke();
    p5.fill(this.color);
    p5.ellipse(this.pos.x, this.pos.y, this.w);
  }

  delete(p5) {
    return this.pos.x < -p5.width / 2 ||
        this.pos.x > p5.width / 2 ||
        this.pos.y < -p5.height / 2 ||
        this.pos.y > p5.height / 2;

  }
}