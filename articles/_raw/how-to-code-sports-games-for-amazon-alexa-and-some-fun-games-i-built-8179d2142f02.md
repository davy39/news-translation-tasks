---
title: How to code sports games for Amazon Alexa, plus some fun games I built
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-30T20:34:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-sports-games-for-amazon-alexa-and-some-fun-games-i-built-8179d2142f02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2MZNttNYjigeKtg43OiPZA.jpeg
tags:
- name: Alexa
  slug: alexa
- name: amazon echo
  slug: amazon-echo
- name: sports
  slug: sports
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Terren Peterson

  I’m both a sports nut and a software engineer. I’m also recognized as an Amazon
  Alexa Champion. I continue to look for new ways to stretch this technology.

  Over the past two years, I’ve won hackathons for skills on the Alexa platfo...'
---

By Terren Peterson

I’m both a sports nut and a software engineer. I’m also recognized as an Amazon [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson). I continue to look for new ways to stretch this technology.

Over the past two years, I’ve won [hackathons](https://en.wikipedia.org/wiki/Hackathon) for skills on the Alexa platform.

Skills are the part of the Alexa voice service that activates its capabilities. In Alexa, _skill_ is a term used for capabilities that make an experience more personal. You can enable or disable them as you choose. And, with the Alexa Skills Kit, You can create and customize them.

### Sports games are an enormous market

Video games are a huge market, with annual revenues projected at more than [$100B worldwide](https://newzoo.com/insights/articles/the-global-games-market-will-reach-108-9-billion-in-2017-with-mobile-taking-42/). Shooter and action games are the most popular, [followed by sports games](http://marketrealist.com/2016/06/action-and-sports-genres-dominate-the-video-gaming-space/).

Voice platforms are growing at a fantastic rate. The popular Amazon Alexa platform has grown by 4 times in the past year. There are now 20,000 custom skills on the Alexa platform. Yet no sports games are more complex than calling out trivia.

Here is a sample of my new football game called _End Zone Football_. This shows how an advanced game can work on the Alexa platform.

### Begin game design with Storyboards

Designing the skill requires writing [storyboards](https://en.wikipedia.org/wiki/Storyboard) to script the action. Start with how the game will begin. Then write the narrative for basic [gameplay](https://en.wikipedia.org/wiki/Gameplay).

Consider yourself to be a playwright or a movie director. Ask yourself: What should the native Alexa voice say? What sounds can be played that are part of the game?

Here’s what I learned from publishing a Baseball and Football game on Alexa. These tips will improve the usability of your game:

* Keep the interaction simple  
yes or no and 1/2/3/4 answers work best
* Identify sounds that can make the gameplay more exciting  
Crowd cheering, whistles, or the crack of a bat
* Simplify the game  
The Baseball game skills should include foul balls  
The Football game skills should simulate penalties  
These help keep the user engaged
* Don’t rely on visuals  
A background image for the Echo Show is nice, but the images on the companion app should be secondary
* Bound the game to 2–5 minutes  
Users can play again and again if they have time
* Create a help function that explains the game in detail  
Give examples of phrases to use to play
* Above all else  
Make it Fun!

### Learn SSML to include sounds with voice

[Speech Synthesis Markup Language](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/speech-synthesis-markup-language-ssml-reference) (SSML) integrates sound with voice. It’s used to create the audio for the Alexa device.

This is how I set the main response attribute to call the Alexa API. After splicing the strings in JavaScript, the code looks like this:

```
var speechOutput = “Welcome to End Zone Football. “ +   “<audio src=\”” + bucketLoc + “BandMusicIntro.mp3\” />” +  “The game that lets you drive the “ +   “ball down the field using just your voice. “ +   “<break time=\”1s\”/>” +   “You are in charge of the Blackbears, and are down “ +  sessionAttributes.away + “ to “ + sessionAttributes.home + “. “ +   “<break time=\”1s\”/>” + “The ball is on the “ +   yardline + “ yardline. “ +   “When you are ready, just call out the play you want to run, and the game will begin. “ +   “For a list of plays at anytime say, Read Playbook. “;
```

Here are some examples of how to use SSML in this context:

* To create a pause  
<break time=1s/>
* To insert a soundclip  
<audio src=”https://s3.amazonaws.../file.mp3">

I recommend using an [S3 bucket](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) to store the media files. This is a low-cost way of storing data. And they can be accessible to Alexa.

### State management tracks the progress of play

Alexa has the ability to store the gameplay state. Use this feature to simplify the coding and testing of your skill.

In the [Node.js SDK](https://aws.amazon.com/sdk-for-node-js/), a session attribute is passed with the request and response attributes. You can use the session attribute for the gameplay state. Store critical game information in this field. You can include anything, like the play number or recorded number of outs.

Here is an example used in the Football game

```
// save the game attributes through to the next play    if (session.attributes) {          sessionAttributes = session.attributes;    }...
```

```
// gameplay rules for passingif (offensivePlaybook[i].playType === “pass” &&    offensivePlaybook[i].playNumber.toString() ===     intent.slots.playNumber.value) {       console.log(“Matched Play Number”);       // calculate pass distance based on play selected      passDistance = Math.round(Math.random() *         (offensivePlaybook[i].maxYardage            — offensivePlaybook[i].minYardage)            + offensivePlaybook[i].minYardage);       // make sure distance of play can’t be longer than       // the remaining field       if (passDistance > sessionAttributes.yardline) {         passDistance = sessionAttributes.yardline;       }       playDesc = offensivePlaybook[i].playDesc;       speechOutput = speechOutput + playDesc + “. “;       // based on the play selected, determine relative       // completion rate       passCompletion = offensivePlaybook[i].completionRate;)...// pass back the response to Alexa, and save the gamestatecallback(sessionAttributes,                 buildSpeechletResponse(cardTitle, speechOutput,       cardOutput, repromptText, device, shouldEndSession));
```

Storing this data in a table for analytics is helpful, but is not needed in an initial version. Let the Alexa platform do this work for you.

### Advertise your skill on social media

People don’t yet realize all the things that an Alexa can do. When doing demos of these skills, I consistently get feedback that “I didn’t think Alexa could do that.”

All skills must be certified before publication on the Amazon Store. When your skill passes the certification process, take the time to record a video of it in action. It is the best way to prove what the platform is capable of.

Thank you for reading, and please enjoy these games — they’re free!

