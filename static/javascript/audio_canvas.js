// let songName;
// let songSrc;
// let SongAuthor;
// let imgSrc;
// let likes;
// let UserProfile;
// let UserImg;
// let backword;

function onPlay() {
  userStartAudio();
}

function animateElement(
  /**HTMLDivElement*/ mainDiv,
  /**string*/ backwards = "{{ backwards }}"
) {
  // region element selection
  if (backwards === "{{ backwards }}") {
    // if we're not rendered by a server set this to false
    backwards = "false";
  }
  backwards = backwards === "true";
  const element = mainDiv.querySelector("div.imgbox");
  const audioNode = mainDiv.querySelector("audio");
  const titleText = mainDiv.querySelector(".scrollTitle");
  // endregion

  // region P5
  let myP5;
  element.onclick = () => {
    myP5.userStartAudio();
    audioNode[audioNode.paused ? "play" : "pause"]();
  };
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
      let mediaSource = audioContext.createMediaElementSource(audioNode);
      mediaSource.connect(sp5.soundOut);

      fft = new p5.FFT();
      wave_paused = fft.waveform();
    };

    sp5.windowResized = () => {
      sp5.resizeCanvas(element.clientWidth, element.clientHeight);
    };

    sp5.draw = () => {
      sp5.clear();
      sp5.noFill();
      sp5.strokeWeight(4);
      let wave;

      fft.analyze();
      amp = fft.getEnergy(20, [200]);
      sp5.stroke([255, 255, 255, 255]);

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
          let r = sp5.map(wave[index], -1, 1, 180, 300);
          let x = r * sp5.sin(i) * 0.5 * t;
          let y = r * sp5.cos(i) * 0.5;
          sp5.vertex(x, y);
        }
        sp5.endShape();
      }
      sp5.strokeWeight(2);
      for (let t = -1; t <= 1; t += 2) {
        sp5.beginShape();
        for (let i = 0; i <= 180; i += 1) {
          let index = Math.floor(sp5.map(i, 0, 180, 0, wave.length - 1));
          let r = sp5.map(wave[index], -1, 1, 120, 180);
          let x = r * sp5.sin(i) * 0.5 * t;
          let y = r * sp5.cos(i) * 0.5;
          sp5.vertex(x, y);
        }
        sp5.endShape();
      }

      if (!audioNode.paused) {
        let p = new Particle(amp, sp5);

        particles.push(p);
        if (amp > 180) {
          let a = new Particle(amp, sp5);
          particles.push(a);
        }
        if (amp > 220) {
          let a = new Particle(amp, sp5);
          particles.push(a);
          a = new Particle(amp, sp5);
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

  //region text animation
  let defaultDelay = 75;
  let defaultWidth = 3734;

  if (this.$refs.scrollTitle.offsetWidth > this.$refs.audioTitle.offsetWidth) {
    let width = this.$refs.scrollTitle.offsetWidth;
    this.newDelay = defaultDelay * (width / defaultWidth) * 1000;
    if (this.backword == "true") {
      this.$refs.scrollTitle.animate(
        [
          // keyframes
          { transform: "translate(-90%, 0)" },
          { transform: "translate(10%, 0)" },
        ],
        {
          // timing options
          duration: this.newDelay,
          iterations: Infinity,
        }
      );
    } else {
      this.$refs.scrollTitle.animate(
        [
          // keyframes
          { transform: "translate(0, 0)" },
          { transform: "translate(-90%, 0)" },
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
  if (this.$refs.scrollAT.offsetWidth > this.$refs.audioAT.offsetWidth) {
    let width = this.$refs.scrollAT.offsetWidth;
    this.newDelay = defaultDelay * (width / defaultWidth) * 1000;
    this.$refs.scrollAT.animate(
      [
        // keyframes
        { transform: "translate(0, 0)" },
        { transform: "translate(-90%, 0)" },
      ],
      {
        // timing options
        delay: 2000,
        duration: this.newDelay,
        iterations: Infinity,
      }
    );
  }
  // endregion
}

class Particle {
  constructor(amp, p5) {
    this.pos = window.p5.Vector.random2D().mult(126);
    this.vel = p5.createVector(p5.random(0.0002, 0.00001));
    this.acc = this.pos.copy().mult(p5.random(0.0002, 0.00001));
    this.w = p5.random(3, 10);
    this.color = [255, 255, 255, p5.random(255 - amp, 255) + 40];
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
    if (
      this.pos.x < -p5.width / 2 ||
      this.pos.x > p5.width / 2 ||
      this.pos.y < -p5.height / 2 ||
      this.pos.y > p5.height / 2
    ) {
      return true;
    }
    return false;
  }
}
