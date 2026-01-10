---
title: How I programmed my first Amazon Alexa Skill and won a free Echo Dot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T23:23:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-your-tech-skill-to-create-alexa-skills-a3e9f210a952
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a0cGkm-EHwR3jcHd7rpkQg.png
tags:
- name: Alexa
  slug: alexa
- name: AWS
  slug: aws
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Lorrie Pearson

  It’s been a year since I began learning to code. I became interested in coding because
  of my desire to work with others in the beauty, fashion and luxury lifestyle world.
  I wanted to create amazing websites with animated elements an...'
---

By Lorrie Pearson

It’s been a year since I began learning to code. I became interested in coding because of my desire to work with others in the beauty, fashion and luxury lifestyle world. I wanted to create amazing websites with animated elements and other digital media.

I started with an online course and a month later, I discovered freeCodeCamp. That’s when learning to code became more exciting and insightful.

There is real-time communication with fellow coders ready to help you work through interactive challenges. They provide feedback and references for further learning. This helped my confidence grow and coding skills improve.

In early June, a friend told me about an online webinar titled “Build Voice Enabled Experiences with Amazon Alexa.” The idea of the webinar increased my curiosity because at the time, I had only seen commercials, but had not used an Alexa enabled product. I signed up and was fascinated.

At the end of the webinar attendees received information about a promotion. If within 30 days you created a Skill and got it published, you were eligible to win a free Echo Dot. I didn’t know if I had enough knowledge to succeed, but I decided to give it a try to learn.

The thought of creating my first app was exciting. At that moment, my Alexa learning experience began.

![Image](https://cdn-media-1.freecodecamp.org/images/GS1YCp8IJi2QrNIMKA71Y2Zj2k-GplgIVH0Y)
_Amazon Alexa Enabled Devices_

### **What is Alexa and how does it work?**

Alexa is a cloud-based voice service that powers millions of voice experiences in the home. Devices Alexa powers includes Amazon Echo, Echo Dot, Amazon Tap and Amazon Fire TV.

A Skill is a voice-driven application for Alexa.

Alexa provides “Skills”, which allows users to interact with the devices. Skills can be created to do many things. They can answer questions, play trivia games, play music, set an alarms, tell jokes and more.

The Alexa Skills Kit (ASK) is a collection of tools, API’s, documentation, code samples and templates with links to GitHub. The ASK helps developers create Skills for Alexa enabled devices.

An Alexa Skill has two main components: a Skill Service and a Skill Interface.

Your code is written in Node.js for the Skill Service which lives in the Cloud ([Amazon AWS, Lambda](https://aws.amazon.com/), an HTTPS service). It receives instructions to determine the actions to take in response to the user requests from the Alexa enabled device.

The Skill Service implements event handlers that define how the Skill will behave. The event is triggered when the user speaks into an Alexa enabled device.

Then you configure the Skill Interface with the Skill Developer Portal. The interface processes the users’ words to trigger the events that the Skill Service handles. In this area you determine what to call your Skill so the user can invoke it by name. This also is where you define the Skill interaction model. This is so it knows how to listen to users’ spoken words and respond with the information intended.

It’s the interaction of the two components that make the Skill work.

The Amazon Team provided links to three Skill Templates. These templates are great to help you get started and to learn how Alexa interacts and responds.

* **Fact Skill template**  
to create something like a “fact” or “joke” of the day.
* **Decision Tree template**  
to create simple adventure games and quizzes
* **How To template**  
to create skills like recipes content with similar step by step processes.

Plus many more intermediate and advanced templates [available](https://developer.amazon.com/alexa-skills-kit/tutorials) .

![Image](https://cdn-media-1.freecodecamp.org/images/lEVAry9so7W9iTBCUgV0-DXV8jTfqNSqPc7i)
_My first published Alexa Skill, Makeup Facts_

I now have three published skills, [Makeup Facts](https://www.amazon.com/Lorriep-design-studio-makeup-facts/dp/B071XC158S/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1501898705&sr=1-1&keywords=makeup+facts), [Fashion Facts](https://www.amazon.com/Lorriep-design-studio-fashion-facts/dp/B073JY3H83/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1501898748&sr=1-1&keywords=fashion+facts) and [Girls Can Code](https://www.amazon.com/Lorriep-design-studio-Girls-Code/dp/B07487QL3J/ref=sr_1_14?s=digital-skills&ie=UTF8&qid=1501898636&sr=1-14&keywords=lifestyle) . I work as a freelance makeup artist and fashion stylist and decided to start with what I know best.

To create these “Fact Skills” I reviewed the topic and information on creating a Skill. Then I created my list of facts that would be integrated into the Fact Skill Template. All Skills were accepted and published within a couple of days.

### **How I created my first Skill**

Go to [Amazon Developer Portal](https://developer.amazon.com/) sign in, click Alexa at top of the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/TT4LjkFjJet75UKwzdQ1hQr2cp1vBP4WzOtu)
_Amazon Developer Console_

On the Alexa page, choose the “Get Started” for the Alexa Skills Kit.

![Image](https://cdn-media-1.freecodecamp.org/images/ohZJBwb18S7r8sWbEWBbgZH91cgV3JfvvJzN)
_Alexa Skills Kit get started button_

On the next page..select “Add New Skill.”

![Image](https://cdn-media-1.freecodecamp.org/images/3DFuU4utTQ71Xj11vR7Rt0e834fdmWDyaRO9)
_from Amazon Alexa Skill Kit Tutorial_

Then fill out the **Information** page.

Skill Type: **Custom**

Language: **English**

Name: **Makeup Facts**

Invocation Name: (what your user will need to say to start the Skill) **Makeup Facts**

![Image](https://cdn-media-1.freecodecamp.org/images/wQGWluVqdyMHNE8XWfhOJHgeukyv8opdfnAE)
_my Skill information page_

Click next to go to **Interaction Model** page. This is where you create **intents** or what users will ask Alexa to do. Then create **utterances** or possible ways the user will ask Alexa about the Skill you’ve created. I found this [GitHub repository](https://github.com/Lorrie01/alexacourse/tree/master/1_spaceGeek/speechAssets) to be helpful. The Samples include: give me a fact, tell me a fact.

![Image](https://cdn-media-1.freecodecamp.org/images/YUBk843RK0lgoRBCAm782NwTo0WVkj5OarEW)
_from Alexacourse GitHub_

My **Intents** in the **Interactive Model** for **Makeup Facts**

```
{ “intents”: [ { “intent”: “GetNewFactIntent” }, { “intent”: “AMAZON.HelpIntent” }, { “intent”: “AMAZON.StopIntent” }, { “intent”: “AMAZON.CancelIntent” } ] }
```

My **Utterances** in the **Interactive Model** for **Makeup Facts.**

```
GetNewFactIntent a factGetNewFactIntent tell me a factGetNewFactIntent tell me a makeup factGetNewFactIntent give me a factGetNewFactIntent give me a makeup factGetNewFactIntent tell me triviaGetNewFactIntent give me triviaGetNewFactIntent give me some informationGetNewFactIntent tell me somethingGetNewFactIntent give me something
```

Now it’s time to set up Lambda. Go to [https://aws.amazon.com/](https://aws.amazon.com/) and sign into the console. Then go to **services-Lambda**.

![Image](https://cdn-media-1.freecodecamp.org/images/crBOkgDgYQiljGUSDxaNIHzVUF2FzRmCoDaY)
_from Amazon Alexa Skill Kit Tutorial_

On the top right of your page, make sure your **AWS Region** is **N. Virginia**.

![Image](https://cdn-media-1.freecodecamp.org/images/H5yeHkDP00jQLrJBD0VvE7R8kCHkuAcJsNQW)
_from Amazon Alexa Skill Kit Tutorial_

Then click the blue button to create a Lamda function.

Choose the blueprint that looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/mddxNVvNk2T2m8M26n1VKTimgXoUKKwENBXF)
_from Amazon Alexa Skill Kit Tutorial_

Configure your trigger. Make sure you choose **Alexa Skills Kit** in the drop down menu.

![Image](https://cdn-media-1.freecodecamp.org/images/ro9RU5ptijwhlJOraZgjYab3ggfdHcqnEViv)
_from Amazon Alexa Skill Kit Tutorial_

Configure your function. Make sure your function name is written in camelBack. You can leave the description blank, but you are building this in Node.js.

Add your updated code.

There is an [AlexaSkill.js](https://github.com/Lorrie01/alexacourse/tree/master/1_spaceGeek/src) file written with specific event handlers. It specifies output, prompt and speech. There is also an Index.js file that you customize to meet the needs of your Skill.

```
Girls Can Code (index.js)
```

```
‘use strict’;var Alexa = require(‘alexa-sdk’);
```

```
var APP_ID = “amzn1.ask.skill.1f2c85a9-b1b6–49a8-b94d-8a795d545d98”;
```

```
var SKILL_NAME = “Girls Can Code”;var GET_FACT_MESSAGE = “Here’s your fact: “;var HELP_MESSAGE = “You can say tell me a code fact, or, you can say exit… What can I help you with?”;var HELP_REPROMPT = “What can I help you with?”;var STOP_MESSAGE = “Goodbye!”;
```

```
var data = [ “Coding is awesome.”, “You can create tools that will change the world.”, “Coding is creative.”, “Coding is like solving a puzzle.”, “Coding work can be done remotely”, “Learning code is empowering.”, “Technology and coding help create the future.”, “Girls who can code have the edge”, “Anyone can code. You’ll discover something new.”, “Coding promotes critical thinking”, “Women make great coders”, “Girls who code are role models for all women.”, “Girls who code know that technology is not just for boys.”, “Jobs in tech are in demand.”, “Coding is the language of the 21st century”, “Girls who code help close the gender gap.”, “Coding can be done anywhere, anytime”, “Working in tech can be a very lucrative career choice”, “Coding is not just about building robots and website, you learn to create things that don’t exist”, “A girl who codes could create the next new social media app”, “A girl with tech skills can change the ways businesses communicate”, “Girls who code love to learn.”];
```

```
exports.handler = function(event, context, callback) { var alexa = Alexa.handler(event, context); alexa.APP_ID = APP_ID; alexa.registerHandlers(handlers); alexa.execute();};
```

```
var handlers = { ‘LaunchRequest’: function () { this.emit(‘GetNewFactIntent’); }, ‘GetNewFactIntent’: function () { var factArr = data; var factIndex = Math.floor(Math.random() * factArr.length); var randomFact = factArr[factIndex]; var speechOutput = GET_FACT_MESSAGE + randomFact; this.emit(‘:tellWithCard’, speechOutput, SKILL_NAME, randomFact) }, ‘AMAZON.HelpIntent’: function () { var speechOutput = HELP_MESSAGE; var reprompt = HELP_REPROMPT; this.emit(‘:ask’, speechOutput, reprompt); }, ‘AMAZON.CancelIntent’: function () { this.emit(‘:tell’, STOP_MESSAGE); }, ‘AMAZON.StopIntent’: function () { this.emit(‘:tell’, STOP_MESSAGE); }};
```

Create a compressed file with the above two files and upload the zipfile into Lambda.

Skip the Advanced settings.

Copy the ARN # in the top right hand corner of your screen.

![Image](https://cdn-media-1.freecodecamp.org/images/kcR-r2rJSGnwpihGWoZOMJS4ygixgZ285t5x)
_from Amazon Alexa Skill Kit Tutorial_

Go back to the **Amazon Developer** page. Select your skill and click on the **Configuration** tab located in the left sidebar menu.

Select the **AWS Lambda** option. Check the **North America** box. Paste the **arn#** that you copied from your Lambda dashboard.

![Image](https://cdn-media-1.freecodecamp.org/images/1E2xx0KBWCGXaRMvLaOYhKqdWncQfYAkGU6u)
_my configuration page_

**Test your Skill. If necessary, update it so that it works properly.** This [GitHub Repository](https://github.com/Lorrie01/alexacourse/tree/master/1_spaceGeek/src) gives you the sample code for creating a Fact Skill. Check it, clone it and update it to write your own.

You can test your code in the Developer Console, in the Lambda functions, on your Echo and at [Echoism.io](https://echosim.io/welcome).

Enter your Publishing and Privacy information.

Congrats..you’re ready to submit for certification.

It takes a few days to hear back from the Amazon Developer Team. If your Skill is approved, then everything works and all of the information is compliant. Your Skill will be certified and published and available for others to use.

If not, you will receive feedback and suggestions on what you need to to to resolve any issues so you can re-submit.

![Image](https://cdn-media-1.freecodecamp.org/images/0-f8xzlFh9-a56n5XRPSfu6jFzvBCznqYYEU)
_My 2nd published Alexa Skill, Fashion Facts_

### **What I learned**

* It’s helpful to have some familiarity with JavaScript and Node.js.
* You will need an AWS (Amazon Web Services) account and an Amazon Developer Account to complete and submit Skills.
* Review the words you cannot use that will conflict with how Alexa responds.
* Listen to the preview of your Skill. It’s extremely helpful to know your information flows.
* It’s very different creating something that is voice activated by an end user as compared to reading on a screen.
* Pretend you are the end user when writing your Skill. It helped me understand how the user would ask Alexa for information.
* If your Skill is not accepted review the feedback from the Alexa Skills Team. They provide great information that will help you get your skill certification ready.
* If you provide improvements to one of your existing Skills, the improved Skill has to go through the same process.
* You need an icon or image for your Skill to upload with submission.
* Once your skill is accepted and certified, it is live on Amazon.

I am currently working on two Skills. One uses the “Decision Tree template” and the other uses the “How To template”. These are a little more complex to build, but I’m confident will have them published soon.

I also have my free Echo Dot. Interacting with this device has given me ideas for developing more Skills.

![Image](https://cdn-media-1.freecodecamp.org/images/ECUurYe7GuES-qtlriyhtOYaHxZ3so4Lp093)
_My 3rd published Alexa Skill, Girls Can Code_

