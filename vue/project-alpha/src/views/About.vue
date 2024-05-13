<template>
  <header>
    <div class="titlegrid">
      <img class="logo" src="../assets/p_logo.jpg">
      <h1 class="title">GemmaDEV</h1>
      <p class="para"><u>Why Us ?</u></p>
      <br>
      <p class="para">Interplay between the Python interpreter and an LLM, our AI agent expertly automates Python debugging procedures while seamlessly synthesizing code, presenting a refined solution for your programming needs.</p>
    </div>

  </header>
</template>

<style>

.logo{
  width:50px;
  height: 50px;
  align-self: flex-start;
}

.para{
  display: flex;
  align-items: left;
  flex-direction: column;

  justify-content: center;
  font-size: 3vmin;
  font-weight: 900;
  animation: fadeInAnimation ease-in 3s;

  color:white;

  text-shadow: 4cap;

  font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif

}

.titlegrid{
  min-height: 100vh;
  display: flex;
  align-items: center;
  flex-direction: column;
}

.title {
  color: azure;
  font-family: Arial;
  top: 50px;

  align-items: center;
  justify-content: center;
  font-size: 20vmin;
  font-weight: 900;
  animation: fadeInAnimation ease-in 3s;
}


@import url("https://fonts.googleapis.com/css?family=Raleway");

:root {
  --glow-color: hsl(0, 0%, 100%);
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

.glowing-btn {
  position: relative;
  color: var(--glow-color);
  cursor: pointer;
  padding: 0.35em 1em;
  border: 0.05em solid var(--glow-color);
  border-radius: 0.15em;
  background: none;
  perspective: 2em;
  font-family: "Raleway", sans-serif;
  font-size: 2em;
  font-weight: 900;
  letter-spacing: 1em;

  -webkit-box-shadow: inset 0px 0px 0.5em 0px var(--glow-color),
    0px 0px 0.5em 0px var(--glow-color);
  -moz-box-shadow: inset 0px 0px 0.5em 0px var(--glow-color),
    0px 0px 0.5em 0px var(--glow-color);
  box-shadow: inset 0px 0px 0.5em 0px var(--glow-color),
    0px 0px 0.5em 0px var(--glow-color);
  animation: border-flicker 2s linear infinite;
}

@keyframes fadeInAnimation {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

.glowing-txt {
  float: left;
  margin-right: -0.8em;
  -webkit-text-shadow: 0 0 0.125em hsl(0, 5%, 4%),
    0 0 0.45em var(--glow-color);
  -moz-text-shadow: 0 0 0.125em hsla(0, 0%, 6%, 0.936),
    0 0 0.45em var(--glow-color);
  text-shadow: 0 0 0.125em hsla(0, 2%, 9%, 0.974), 0 0 0.45em var(--glow-color);
  animation: text-flicker 3s linear infinite;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif
}

.faulty-letter {
  opacity: 0.5;
  animation: faulty-flicker 2s linear infinite;
}

.glowing-btn::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: 0.7;
  filter: blur(1em);
  transform: translateY(120%) rotateX(95deg) scale(1, 0.35);
  background: var(--glow-color);
  pointer-events: none;
}

.glowing-btn::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0;
  z-index: -1;
  background-color: var(--glow-color);
  box-shadow: 0 0 2em 0.2em var(--glow-color);
  transition: opacity 100ms linear;
}

.glowing-btn:hover {
  color: rgba(0, 0, 0, 0.8);
  text-shadow: none;
  animation: none;
}

.glowing-btn:hover .glowing-txt {
  animation: none;
}

.glowing-btn:hover .faulty-letter {
  animation: none;
  text-shadow: none;
  opacity: 1;
}

.glowing-btn:hover:before {
  filter: blur(1.5em);
  opacity: 1;
}

.glowing-btn:hover:after {
  opacity: 1;
}

@keyframes faulty-flicker {
  0% {
    opacity: 0.1;
  }

  2% {
    opacity: 0.1;
  }

  4% {
    opacity: 0.5;
  }

  19% {
    opacity: 0.5;
  }

  21% {
    opacity: 0.1;
  }

  23% {
    opacity: 1;
  }

  80% {
    opacity: 0.5;
  }

  83% {
    opacity: 0.4;
  }

  87% {
    opacity: 1;
  }
}

@keyframes text-flicker {
  0% {
    opacity: 0.1;
  }

  2% {
    opacity: 1;
  }

  8% {
    opacity: 0.1;
  }

  9% {
    opacity: 1;
  }

  12% {
    opacity: 0.1;
  }

  20% {
    opacity: 1;
  }

  25% {
    opacity: 0.3;
  }

  30% {
    opacity: 1;
  }

  70% {
    opacity: 0.7;
  }

  72% {
    opacity: 0.2;
  }

  77% {
    opacity: 0.9;
  }

  100% {
    opacity: 0.9;
  }
}

@keyframes border-flicker {
  0% {
    opacity: 0.1;
  }

  2% {
    opacity: 1;
  }

  4% {
    opacity: 0.1;
  }

  8% {
    opacity: 1;
  }

  70% {
    opacity: 0.7;
  }

  100% {
    opacity: 1;
  }
}

@media only screen and (max-width: 600px) {
  .glowing-btn {
    font-size: 1em;
  }
}
</style>