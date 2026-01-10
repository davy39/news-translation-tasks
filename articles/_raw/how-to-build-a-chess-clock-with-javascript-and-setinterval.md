---
title: How to Build a Chess Clock with JavaScript and setInterval
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-14T16:09:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chess-clock-with-javascript-and-setinterval
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/cover_image_1920x1005-1.png
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "By Brandon Wallace\nChess games can sometimes go on for quite some time.\
  \ I once heard a story of a chess game between two famous chess grandmasters that\
  \ went on for over eight hours, with the crowd waiting for them to make a move.\
  \ \nAfter a while one p..."
---

By Brandon Wallace

Chess games can sometimes go on for quite some time. I once heard a story of a chess game between two famous chess grandmasters that went on for over eight hours, with the crowd waiting for them to make a move. 

After a while one player said to the other "Aren't you going to move?" His opponent responded, "I thought it was your turn."

## Introduction

Chess clocks are used to limit a chess game to a certain amount of time. A chess clock can add a great deal of excitement to a chess game. Many people use these clocks in tournaments and just for fun. 

With a chess clock, the goal is to checkmate your opponent before your timer runs out. The first person that runs out of time without checkmating their opponent loses the game.

I will show you how to create a basic chess clock using JavaScript and the [setInterval](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Timeouts_and_intervals) method. `setInterval` allows you to execute a timed event repeatedly by specifying a time in milliseconds. `setInterval` can be set to an ID and stopped by calling `clearInterval` on the `setInterval` ID.

Here is a simple example of how setInterval works:

```javascript
let count = 1;

// Assign a timed event to variable timerId.

const timerId = setInterval(() => {
    
    console.log(`Executing function for ${count} seconds.`);
    
    // Increment the count variable by one.
    count++;
    
    if (count === 11) {
        
        // Stop event by calling clearInterval on timerId.
        clearInterval(timerId);
        console.log(`Timing event cleared.`);
        
    }
    
}, 1000); // Execute event every second (1000 milliseconds = 1 second).

```

![setinterval-output.png](https://i.postimg.cc/RhQQDHTk/setinterval-output.png)
_output_

Here is the blueprint for how the application will look on desktop and mobile.

![chessclockblueprint2.png](https://i.postimg.cc/4NbLXWDD/chessclockblueprint2.png)

**The programming requirements for this project are:**

* We need two clocks that countdown to zero.
* We need a start button and a reset button.
* And we need a way to toggle between the clocks as the time is counting down.

## Let's set up the project

Create the directories `css`, `js` , and `audio` to keep the project organized.

```bash
$ mkdir css js audio

```

Create the files `index.html`, `style.css`, and `script.js`.

```bash
$ touch index.html css/style.css js/script.js

```

Add this code to the `index.html` file.

```html
<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>chess clock</title>

  </head>

  <body>

    <main>
    
      <div class="player">
      
        <div class="player__tile player-1">
          <div class="player__digits">
            <span id="min1">10</span>:<span id="sec1">00</span>
          </div>
        </div>
        
        <div class="player__tile player-2">
          <div class="player__digits">
            <span id="min2">10</span>:<span id="sec2">00</span>
          </div>
        </div>
        
      </div>
      
      <div class="timer__buttons">
        <button class="timer__start-bttn bttn" type="button">START</button>
        <button class="timer__reset-bttn bttn" type="button">RESET</button>
      </div>

    </main>

    <footer>

      <p>Press spacebar or click on timer after a move to switch player's clock.</p>

    </footer>

    <script src="js/script.js"></script>

  </body>

</html>

```

This is what we have without any CSS.

![setinterval-no-css.png](https://i.postimg.cc/bJ6qH67W/setinterval-no-css.png)

## Add some CSS to style the project

Add this CSS code to the `style.css` file to style the project mobile first. 

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    height: 100%;
    background-color: #14A7FF;
}

body {
    font-size: 100%;
    font-family: monospace, monospace;
}

main {
    width: 100%;
    padding: 0 10px;
    box-sizing: border-box;
}

.player {
    margin: 1em 0 5px 0;
    display: flex;
    flex-direction: column;
}

.player__tile {
    width: 100%;
    height: 300px;
    display: flex;
    margin: 0 auto;
    color: #000000;
    max-width: 400px;
    border-radius: 8px;
    align-items: center;
    justify-content: center;
    background-color: #FFFFFF;
    box-shadow: inset 3px 3px 0 #000, 
                inset -3px 3px 0 black, 
                inset -3px -3px 0 black, 
                inset 3px -3px 0 black;
}

.player-2 {
    color: #FFFFFF;
    margin-top: 5px;
    background-color: #2D2C2C;
}

.player__digits {
    font-size: 6rem;
    font-weight: bold;
}

.timer__buttons {
    margin-bottom: 1em;
}

.timer__start-bttn, 
.timer__reset-bttn {
    width: 100%;
    display: block;
    color: #020202;
    min-height: 50px;
    max-width: 400px;
    font-size: 1.5rem;
    font-weight: bold;
    border-radius: 8px;
    letter-spacing: 2px;
    margin: 0 auto 5px auto;
    border: 4px solid #000000;
}

.timer__start-bttn {
    color: #FFFFFF;
    background-color: #0071D5;
}

.timer__start-bttn:hover {
    color: #000000;
    background-color: #FFFFFF;
}

.timer__reset-bttn:hover {
    color: #FFFFFF;
    background-color: #0071D5;
}

footer p {
    text-align: center;
}

/* Media queries for mobile first develoment. */
/* Media queries for landscape mode on mobile devices */
@media only screen and (orientation: landscape) and (max-width: 850px) {
    .player {
        max-width: 610px;
        flex-direction: row;
        margin: 5px auto 0 auto;
    }
    .player__tile {
        max-width: 300px;
        max-height: 250px;
        margin: 0 3px 5px 3px;
    }
    .player__digits {
        font-size: 5rem;
    }
    .timer__buttons {
        display: flex;
        margin: 0 auto;
        max-width: 610px;
    }
    .timer__start-bttn, 
    .timer__reset-bttn {
        display: block;
        max-width: 300px;
        margin: 0 3px 5px 3px;
    }
}

/* Media queries for portrait mode */
@media only screen and (orientation: portrait) and (min-width: 400px) {
    .player__tile {
        height: 400px;
    }
    .player__digits {
        font-size: 6rem;
    }
}

/* Screen wider than 850px wide will use these settings. */
@media only screen and (min-width: 850px) {
    .player {
        margin: 1em auto 10px auto;
        max-width: 810px;
        flex-direction: row;
    }
    .player__tile {
        height: 400px;
    }
    .player-2 {
        margin-top: 0;
    }
    .player__digits {
        font-size: 7rem;
    }
    .timer__buttons {
        display: flex;
        margin: 0 auto;
        max-width: 810px;
    }
    .timer__start-bttn, 
    .timer__reset-bttn {
        padding: .7em;
        font-size: 1.8rem;
    }
}


```

With CSS added, the project is looking better.

![setinterval-with-css.png](https://i.postimg.cc/YCVngQDR/setinterval-with-css.png)

## Add JavaScript code to make the clock run

I will first add the functions that we need to make the project work. 

Edit the `script.js` file:

```bash
$ vim js/script.js

```

And add the following ES6 arrow functions:

```javascript

// Add a leading zero to numbers less than 10.
const padZero = () => {
    // code
}

// Warn the player if time drops below thirty seconds.
const timeWarning = () => {
    // code
}

// Create a class for the timer.
class Timer {
    // code
}

// Swap player's timer after a move (player1 = 1, player2 = 2).
const swapPlayer = () => {
    // code
}

// Start timer countdown to zero.
const startTimer = () => {
    // code
    let timerId = setInterval(function() {
        // code
    }, 1000)
}
```

Now we can fill in the JavaScript functions with code to make the clock work.

We start by adding some variables to the project. If the variable `playing` is  
true, the clock runs. 

The `currentPlayer` stores the value 1 for player one or 2 for player two. We can add sounds [(from freesound.org)](https://freesound.org/) for when the clock is toggled from one player to the other and to alarm when the time has run out. 

The `padZero` function will add a leading zero to numbers that are lower than 10.

Edit the `script.js` file like this:

```bash
$ vim js/script.js
```

```javascript
let playing = false;
let currentPlayer = 1;
const panel = document.querySelector('.player');
const buttons = document.querySelectorAll('.bttn');
// Sound effects for project.
const timesUp = new Audio('audio/460133__eschwabe3__robot-affirmative.wav');
const click = new Audio('audio/561660__mattruthsound.wav');

// Add a leading zero to numbers less than 10.

const padZero = (number) => {
    if (number < 10) {
        return '0' + number;
    }
    return number;
}

```

Give each player a visual notification that the time is running out by changing the numbers to a red color.

```javascript
// Warn player if time drops below one minute and thirty seconds.

const timeWarning = (player, min, sec) => {
    // Change the numbers to red below 0 minutes and 30 seconds
    if (min < 1 && sec <= 30) {
        if (player === 1) {
            document.querySelector('.player-1 .player__digits').style.color = '#CC0000';
        } else {
            document.querySelector('.player-2 .player__digits').style.color = '#CC0000';
        }
    }
}
```

![setinterval-red-numbers.png](https://i.postimg.cc/DzwjbnTr/setinterval-red-numbers.png)

We will create a class to set up the timer for each player.

```javascript
// Create a class for the timer.

class Timer {
    constructor(player, minutes) {
        this.player = player;
        this.minutes = minutes;
    }
    getMinutes(timeId) {
        return document.getElementById(timeId).textContent;
    }
}

// Create an instance of the timer for each player.

let p1time = new Timer('min1', document.getElementById('min1').textContent);
let p2time = new Timer('min2', document.getElementById('min2').textContent);

```

The `swapPlayer` function toggles the timer between player 1 and player 2 using a ternary operator.

If the `playing` variable is false, the clocks are not running and the function exits.

```javascript
// Swap player's timer after a move (player1 = 1, player2 = 2).

const swapPlayer = () => {
    if (!playing) return;
    // Toggle the current player.
    currentPlayer = currentPlayer === 1 ? 2 : 1;
    // Play the click sound.
    click.play();
}

```

The startTimer function uses `setInterval` to countdown each timer.

The `playing` variable is set to true to get the clock running. 

The if statement checks to see which player is the current player, and then it starts counting down the timer for that player. 

If the seconds reach 60, one number is subtracted from the minutes. The HTML element is updated with the time each second. Once the seconds and minutes get to zero, `clearInterval()` is called to stop the timer.

```javascript
// Start timer countdown to zero.

const startTimer = () => {
    playing = true;
    let p1sec = 60;
    let p2sec = 60;

    let timerId = setInterval(function() {
        // Player 1.
        if (currentPlayer === 1) {
            if (playing) {
                buttons[0].disabled = true;
                p1time.minutes = parseInt(p1time.getMinutes('min1'), 10);
                if (p1sec === 60) {
                    p1time.minutes = p1time.minutes - 1;
                }
                p1sec = p1sec - 1;
                document.getElementById('sec1').textContent = padZero(p1sec);
                document.getElementById('min1').textContent = padZero(p1time.minutes);
                if (p1sec === 0) {
                    // If minutes and seconds are zero stop timer with the clearInterval method.
                    if (p1sec === 0 && p1time.minutes === 0) {
                        // Play a sound effect.
                        timesUp.play();
                        // Stop timer.
                        clearInterval(timerId);
                        playing = false;
                    }
                    p1sec = 60;
                }
            }
        } else {
            // Player 2.
            if (playing) {
                p2time.minutes = parseInt(p2time.getMinutes('min2'), 10);
                if (p2sec === 60) {
                    p2time.minutes = p2time.minutes - 1;
                }
                p2sec = p2sec - 1;
                document.getElementById('sec2').textContent = padZero(p2sec);
                document.getElementById('min2').textContent = padZero(p2time.minutes);
                if (p2sec === 0) {
                    // If minutes and seconds are zero stop timer with the clearInterval method.
                    if (p2sec === 0 && p2time.minutes === 0) {
                        // Play a sound effect.
                        timesUp.play();
                        // Stop timer.
                        clearInterval(timerId);
                        playing = false;
                    }
                    p2sec = 60;
                }
            }
        }
    }, 1000);
}

```

To get the timer running I will add an event listener to the HTML buttons. The event listener will also listen for a click or tap on the `.player` div or if someone is pressing the space bar to toggle between timers.

```javascript
// Listen for a mouse click or tap on the screen to toggle between timers.

timerPanel.addEventListener('click', swapPlayer);

// Loop through the start and reset buttons.

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', () => {
        if (buttons[i].textContent === 'START') {
            // Turn the button a gray color to signify a disabled button.
            buttons[i].style.color = '#EEEEEE';
            buttons[i].style.backgroundColor = '#606060';
            startTimer();
        } else {
            // Reset everything by reloading the page.
            location.reload(true);
        }
    });
}

// Listen for the press of the spacebar on Windows, Linux, and Mac.

document.addEventListener('keypress', event => {
    if (event.keyCode === 32 || event.which === 32) {
        swapPlayer();
    }
});
```

### Here is the final result:

![screenshot-project-complete.png](https://i.postimg.cc/SxPXhfDW/screenshot-project-complete.png)

You can see it [live here](https://chessclock.cf), and you can check out the [GitHub repository here](https://github.com/brandon-wallace/chess_clock2).

## Conclusion

This is one way of creating a basic chess clock. If you are a chess aficionado this might be a fun project to build and something you can use. 

This project shows a good way to use the setInterval method, how to use event listeners, and mobile-first development. You could add other features to the project such as a way to set the time, pausing the timer, different timer modes, and more.

Follow me on [Github](https://github.com/brandon-wallace) | [Dev.to](https://dev.to/brandonwallace)

