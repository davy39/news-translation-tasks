---
title: How you can hear both “Yanny” and “Laurel” using the Web Audio API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T16:11:04.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-hear-both-yanny-and-laurel-using-the-web-audio-api-306051cfcede
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mXeOkNmfZwMkcgUcv8_yhw.jpeg
tags:
- name: audio
  slug: audio
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By _haochuan

  Recently an audio clip asking listeners whether they hear the word “Yanny” or “Laurel”
  has been completely puzzling the world and pitting friend against friend in the
  online debate.

  The clip and the “Yanny or Laurel” poll were posted on ...'
---

By _haochuan

Recently an audio clip asking listeners whether they hear the word “Yanny” or “Laurel” has been completely puzzling the world and pitting friend against friend in the online debate.

The clip and the “Yanny or Laurel” poll were posted on Instagram, Reddit, and other sites by high school students who said that it had been recorded from a vocabulary website playing through the speakers on a computer. Now hundreds of thousands of people are engaged in a debate over what they hear. It’s been driving people crazy and leading to passionate defenses on both side.

However, the magic behind this debate is quite simple. **Different ears have different sensitive frequency zones for the same audio clip.** Also, different speakers have different responses to different audio frequencies.

This tutorial will go through the details about how to use the Web Audio API and simple JavaScript to create to tool that will help you hear both “Yanny” **and** “Laurel.” Then you’ll be able to win any of those debates. :)

If you just want to try the tool, it is live [HERE](https://haochuan.github.io/yanny-vs-laurel/static/). Just open your browser, play the audio, and try to find the sweet spots for “Yanny” and “Laurel” while moving the frequency slider.

### How it works

Let’s talk about the key part first. In order to hear the different word, you need to somehow increase the volume for a specific frequency range which depends on your ears. Luckily the Web Audio API already has something ready for us: `BiquadFilterNode`.

There are different types of `[BiquadFilterNode](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode)` you can use. For this case, we will just go with the `bandpass` filter.

> _A bandpass filter is an electronic device or circuit that allows signals between two specific frequencies to pass, but that discriminates against signals at other frequencies. ([source](https://whatis.techtarget.com/definition/bandpass-filter))_

And for a bandpass filter, most of the time we just need to define the center frequency value we want to boost or cut, instead of the start and the end of the frequency range. We use a `Q` value to control the width of the frequency range. The larger the `Q` is, the narrower the frequency range will be. [Check out Wikipedia](https://en.wikipedia.org/wiki/Q_factor) for more details.

That’s all the knowledge we need to know at this point. Now, let’s write the code.

### Web Audio API Initialization

```
const AudioContext = window.AudioContext || window.webkitAudioContext;
```

```
const audioContext = new AudioContext();
```

#### Create Audio Nodes along with setup and signal chain

```
// the audio tag in HTML, where holds the original audio clipconst audioTag = document.getElementById('audioTag');
```

```
// create audio source in web audio apiconst sourceNode = 
```

```
audioContext.createMediaElementSource(audioTag);
```

```
const filterNode = audioContext.createBiquadFilter();
```

```
filterNode.type = 'bandpass'; // bandpass filterfilterNode.frequency.value = 1000 // set the center frequency
```

```
// set the gain to the frequency rangefilterNode.gain.value = 100;
```

```
// set Q value, 5 will make a fair band width for this casefilterNode.Q.value = 5;
```

```
// connect nodessourceNode.connect(filterNode);filterNode.connect(gainNode);gainNode.connect(audioContext.destination);
```

#### Sample HTML file

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Yanny vs Laurel Web Audio API</title></head><body>  <div id="container">    <audio id='audioTag' crossorigin="anonymous" src="yanny-laurel.wav" controls loop></audio>    <hr>    <input type="range" min="20" max="10000" value="20" step="1" class="slider" id="freqSlider">  </div>  <script src='script.js'></script></body></html>
```

#### Adding frequency slider UI

To make it easier to adjust the center frequency of our bandpass filter, we should add a slider to control the value.

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Yanny vs Laurel Web Audio API</title></head><body>  <div id="container">    <audio id='audioTag' src="yanny-laurel.wav" controls loop></audio>    <hr>    <input type="range" min="50" max="4000" value="1000" step="1" class="slider" id="freqSlider">    <br>    <p id="freqLabel" >Frequency: 1000 Hz</p>  </div>  <script>;    // add event listener for slider to change frequency value    slider.addEventListener('input', e => {
```

```
      filterNode.frequency.value = e.target.value;      label.innerHTML = `Frequency: ${e.target.value}Hz`;
```

```
    }, false);  <script src='script.js'></script><;/body></html>
```

### createMediaElementSource bug in iOS Safari

I found that `createMediaElementSource` won't work in iOS Safari and Chrome. To solve this, you have to use `createBufferSource` to create an AudioBufferNode to store and play the audio instead of the HTML audio tag.  
Please see [the code here](https://github.com/haochuan/yanny-vs-laurel/blob/master/static/script.js) for more detail.

Now you made yourself a tool so you can hear both “Yanny” and “Laurel.” Just open your browser, play the audio, and try to find the sweet spot while moving the frequency slider.

If you want to just try the tool, it is live [HERE](https://haochuan.github.io/yanny-vs-laurel/static/).

I write code for audio and web, and play guitar on YouTube. If you want to see more stuff from me or know more about me, you can always find me on:

Website:  
[https://haochuan.io/](https://haochuan.io/)

GitHub:  
[https://github.com/haochuan](https://github.com/haochuan)

Medium:  
[https://medium.com/@haochuan](https://medium.com/@haochuan)

YouTube: [https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g](https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g)

