---
title: How to Build a Piano Keyboard Using Vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-11T22:35:36.000Z'
originalURL: https://freecodecamp.org/news/javascript-piano-keyboard
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/twitterCard-piano.jpg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Joe Liang

  Making a playable piano keyboard can be a great way to learn a programming language
  (besides being heaps of fun). This tutorial shows you how to code one using vanilla
  JavaScript without the need for any external libraries or frameworks....'
---

By Joe Liang

Making a playable piano keyboard can be a great way to learn a programming language (besides being heaps of fun). This tutorial shows you how to code one using vanilla JavaScript without the need for any external libraries or frameworks.

Here is the [JavaScript piano keyboard](http://1000mileworld.com/Portfolio/Piano/keyboard.html) I made if you want to check out the end product first.

This tutorial assumes you have a basic understanding of JavaScript such as functions and event handling, as well as familiarity with HTML and CSS. Otherwise, it is totally beginner friendly and geared toward those who want to improve their JavaScript skills through project-based learning (or just want to make a cool project!).

The piano keyboard we are making for this project is based on the [dynamically generated synthetic keyboard](https://keithwhor.com/music/) made by Keith William Horwood. We will extend the number of keys available to 4 octaves and set new key bindings. 

Although his keyboard can play sounds from other instruments, we will keep things simple and just stick with piano.

Here are the steps we will take to tackle this project:

1.      [Get working files](#heading-1-get-working-files)

2.      [Set up key bindings](#heading-2-set-up-key-bindings)

3.      [Generate keyboard](#heading-3-generate-keyboard)

4.      [Handle key presses](#heading-4-handle-key-presses)

Let’s get started!

<h2 id="step1">1. Get Working Files</h2>

This tutorial will use the following files:

·        [audiosynth.js](https://keithwhor.github.io/audiosynth/)

·        [playKeyboard.js](https://github.com/1000mileworld/Piano-Keyboard/blob/master/playKeyboard.js)

As mentioned, we will base our piano keyboard off the one made by Keith. Naturally, we will also borrow some of his code which he has kindly given permission with audiosynth.js.

We incorporate audiosynth.js in playKeyboard.js (my modified version of some of Keith’s code) which handles all our JavaScript. This tutorial gives a detailed explanation in the following sections on the major points of how the code in this file creates a fully working piano keyboard.

We leave the file audiosynth.js untouched as it is solely responsible for sound generation.

The code in this file distinguishes this piano keyboard from others found online by using Javascript to dynamically generate the appropriate sound when the user presses a key. Thus, the code does not have to load any external audio files.

Keith already provides an explanation of how the sound generation works on his website so we will not get into the details here. 

In a nutshell, it involves using the `Math.sin()` function in JS to create sinusoidal waveforms and transforming them so they sound more like real instruments through some fancy math.

Create an index HTML file, and let’s link to the JS files in the header:

```html 
<script src="audiosynth.js"></script>
<script src="playKeyboard.js"></script>


In the body, we can create an empty `<div>` element to serve as our keyboard “container”:

```html
<div id= “keyboard”></div>

We give it an id name so that we can reference it later when we create the keyboard using JS. We can run our JS code by calling it in the body as well:

```html
<script type="text/javascript">playKeyboard()</script>

We use playKeyboard.js as one big function. It will run as soon as the browser gets to that line of code and generate a fully working keyboard in the `<div>` element with 
`id = “keyboard”`.

The first few lines of playKeyboard.js sets up for mobile device functionality (optional) and creates a new `AudioSynth()` object. We use this object to call the methods of audiosynth.js which we linked to earlier. We use one of these methods in the beginning to set a volume for the sound.

On line 11, we set position of middle C to the 4th octave.

<h2 id="step2">2. Set Up Key Bindings</h2>

Before we generate the keyboard, we should set up our key bindings as they determine how many keys should be generated.

I originally wanted to try to play the opening notes of ‘Für Elise’ so I chose a range of 4 octaves for a total of 48 black and white keys. This required nearly every key on my (PC) keyboard and you can feel free to include fewer.

A note of warning: I do not have the best key bindings so they may feel unintuitive when you actually try to play. Maybe this is the price of trying to create a 4-octave keyboard.

To set up the key bindings, first create an object that will use keycode as its keys and the note to be played as its key values (starting line 15):

```js
var keyboard = {
	/* ~ */
	192: 'C,-2',
	/* 1 */
	49: 'C#,-2',
	/* 2 */
	50: 'D,-2',
	/* 3 */
	51: 'D#,-2',
    //...and the rest of the keys
}


The comments denote the keys that a user may press on a computer keyboard. If a user presses the tilde key, then the corresponding keycode is 192. You may get the keycode using a tool such as keycode.info.

The key value is the note to be played and written in the format of ‘note, octave modifier’ where the octave modifier represents the relative octave position from the octave containing middle C. For example, ‘C, -2’ is the C note 2 octaves below middle C.

Note that there are no ‘flat’ keys. Every note is represented by a ‘sharp’.

To make our piano keyboard functional, we have to prepare a reverse lookup table where we switch the `key: value` pairs such that the note to be played becomes the key and the keycode becomes the value.

We need such a table because we want to iterate over the musical notes to easily generate our keyboard.

Now here’s where things may get tricky: we actually need 2 reverse lookup tables.

We use one table to look up the label we want to display for the computer key we press to play a note (declared as `reverseLookupText` on line 164) and a second to look up the actual key that was pressed (declared as `reverseLookup` on line 165).

The astute may realize that both lookup tables have keycodes as the values, so what is the difference between them?

It turns out that (for reasons unknown to me) when you get a keycode that corresponds to a key and you try to use `String.fromCharCode()` method on that keycode, you don’t always get back the same string representing the pressed key.

For example, pressing left open bracket yields keycode 219 but when you actually try to convert the keycode back to a string using `String.fromCharCode(219)` it returns "Û". To get "[", you have to use key code 91. We replace the incorrect codes starting on line 168.

Getting the right keycode initially involved a bit of trial and error, but later I realized you can just use another function (`getDispStr()` on line 318) to force the correct string to be displayed.

The majority of the keys do behave properly but you can choose to start with a smaller keyboard so you don’t have to deal with incorrect keycodes.

<h2 id="step3">3. Generate Keyboard</h2>

We start the keyboard generation process by selecting our `<div>` element keyboard container with `document.getElementById(‘keyboard’)` on line 209.
    
On the next line, we declare the `selectSound` object and set the `value` property to zero to have audioSynth.js load the sound profile for piano. You may wish to enter a different value (can be 0-3) if you want to try out other instruments. See line 233 of audioSynth.js with `Synth.loadSoundProfile` for more details.

On line 216 with `var notes`, we retrieve the available notes for one octave (C, C#, D…B) from audioSynth.js.

We generate our keyboard by looping through each octave and then each note in that octave. For each note, we create a `<div>` element to represent the appropriate key using `document.createElement(‘div’)`.

To distinguish whether we need to create a black or white key, we look at the length of the note name. Adding a sharp sign makes the length of the string greater than one (ex. ‘C#’) which indicates a black key and vice versa for white.

For each key we can set a width, height, and an offset from the left based on key position. We can also set appropriate classes for use with CSS later.

Next, we label the key with the computer key we need to press to play its note and store it in another `<div>` element. This is where `reverseLookupText` comes in handy. Inside the same `<div>`, we also display the note name. We accomplish all of this by setting the label’s innerHTML property and appending the label to the key (lines 240-242).

```js
label.innerHTML = '<b class="keyLabel">' + s + '</b>' + '<br /><br />' + n.substr(0,1) + 
'<span name="OCTAVE_LABEL" value="' + i + '">' + (__octave + parseInt(i)) + '</span>' + 
(n.substr(1,1)?n.substr(1,1):'');


Similarly, we add an event listener to the key to handle mouse clicks (line 244):

```js
thisKey.addEventListener(evtListener[0], (function(_temp) { return function() { fnPlayKeyboard({keyCode:_temp}); } })(reverseLookup[n + ',' + i]));

The first parameter `evtListener[0]` is a `mousedown` event declared much earlier on line 7. The second parameter is a function that returns a function. We need `reverseLookup` to get us the correct keycode and we pass that value as a parameter _temp to the inner function. We will not need reverseLookup to handle actual `keydown` events.

This code is pre-ES2015 (aka ES6) and the updated, hopefully clearer equivalent is:

```js
const keyCode = reverseLookup[n + ',' + i];
thisKey.addEventListener('mousedown', () => {
  fnPlayKeyboard({ keyCode });
});


After creating and appending all necessary keys to our keyboard, we will need to handle the actual playing of a note.

<h2 id="step4">4. Handle Key Presses</h2>

We handle key presses the same way whether the user clicks the key or presses the corresponding computer key through use of the function `fnPlayKeyboard` on line 260. The only difference is the type of event we use in `addEventListener` to detect the key press.

We set up an array called `keysPressed` in line 206 to detect what keys are being pressed/clicked. For simplicity, we will assume that a key being pressed can include it being clicked as well.

We can divide the process of handling key presses into 3 steps: adding the keycode of the pressed key to `keysPressed`, playing the appropriate note, and removing the keycode from `keysPressed`.

The first step of adding a keycode is easy:

```js
keysPressed.push(e.keyCode);

where `e` is the event detected by `addEventListener`.

If the added keycode is one of the key bindings we assigned, then we call `fnPlayNote()` on line 304 to play the note associated with that key.

In `fnPlayNote()`, we first create a new `Audio()` element `container` for our note using the `generate()` method from audiosynth.js. When the audio loads, we can then play the note.

Lines 308-313 are legacy code and seem they can just be replaced by `container.play()`, though I have not done any extensive testing to see what the difference is.

Removing a key press is also quite straightforward, as you can just remove the key from the `keysPressed` array with the `splice` method on line 298. For more details, see the function called `fnRemoveKeyBinding()`.


The only thing we have to watch out for is when the user holds down a key or multiple keys. We have to make sure that the note only plays once while a key is held down (lines 262-267):

```js
var i = keysPressed.length;
while(i--) {
	if(keysPressed[i]==e.keyCode) {
		return false;	
    }
}


Returning `false` prevents the rest of `fnPlayKeyboard()` from executing.

<h2>Summary</h2>

We have created a fully functioning piano keyboard using vanilla JavaScript!

To recap, here are the steps we took:

1.	We set up our index HTML file to load the appropriate JS files and execute
 `playKeyboard()` in `<body>` to generate and make the keyboard functional. We have a `<div>` element with `id= "keyboard"` where the keyboard will be displayed on the page.
    
2.	In our JavaScript file playKeyboard.js, we set up our key bindings with keycodes as keys and musical notes as values. We also create two reverse lookup tables in which one is responsible for looking up the appropriate key label based on the note and the other for looking up the correct keycode.
    
3.	We dynamically generate the keyboard by looping through every note in each octave range. Each key is created as its own `<div>` element. We use the reverse lookup tables to generate the key label and correct keycode. Then an event listener on `mousedown` uses it to call `fnPlayKeyboard()` to play the note. The 
`keydown` event calls the same function but does not need a reverse lookup table to get the keycode.
    
4.	We handle key presses resulting from either mouse clicks or computer key presses in 3 steps: add keycode of the pressed key to an array, play the appropriate note, and remove keycode from that array. We must be careful not to repeatedly play a note (from the beginning) while the user continuously holds down a key.


The keyboard is now fully functional but it may look a bit dull. I will leave the CSS part to you ?

Again, here is the [JavaScript piano keyboard](http://1000mileworld.com/Portfolio/Piano/keyboard.html) I made for reference.

If you want to learn more about web development and check out some other neat projects, visit my blog at [1000 Mile World](https://www.1000mileworld.com/).

Thanks for reading and happy coding!


