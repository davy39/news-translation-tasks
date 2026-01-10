---
title: How Echo Buttons take Amazon Alexa Skills to a new level
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T23:49:51.000Z'
originalURL: https://freecodecamp.org/news/how-echo-buttons-take-amazon-alexa-skills-to-a-new-level-d4c489853b1f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F6CHpSv0t3e2ntNu0iDygw.jpeg
tags:
- name: amazon echo
  slug: amazon-echo
- name: baseball
  slug: baseball
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Terren Peterson

  I’m recognized as an Amazon Alexa Champion and have published more than twenty custom
  skills on the platform. I continue to look for new ways to stretch this technology,
  create more robust skills, and share with the community.

  Last...'
---

By Terren Peterson

I’m recognized as an Amazon [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson) and have published more than twenty custom skills on the platform. I continue to look for new ways to stretch this technology, create more robust skills, and share with the community.

Last [September](https://developer.amazon.com/blogs/alexa/post/402fd908-f8d7-4a2b-ab5e-4099222ad974/introducing-alexa-gadgets-new-tools-for-developers-to-create-fun-sign-up-to-stay-tuned), Amazon released a new product for Alexa called Echo Buttons. These hardware devices expand the capabilities for the millions of customers that already have an Alexa. They’re relatively inexpensive, right now going for [$20/2 pack](https://www.amazon.com/dp/B072C4KCQH/).

In [April](https://developer.amazon.com/blogs/alexa/post/705a0ac1-940d-4128-b35e-7085274eca6a/gadgets-skill-api-beta-is-now-available-developers-can-build-games-for-echo-buttons) of this year, Amazon opened up the platform for developers like me to begin incorporating them into custom skills. This is my experience so far programming with them.

![Image](https://cdn-media-1.freecodecamp.org/images/CyYLDlEogrNXnrYiXgOAfMnPLr-EHMGF5S87)
_Echo Button in inactive state._

### Getting Started with Echo Buttons

![Image](https://cdn-media-1.freecodecamp.org/images/rD-kqpmupIZML-HuI46qqn97rNmfe2CmT7fx)
_Network connectivity of Echo Buttons_

Buttons are paired with Alexa devices through a bluetooth connection, becoming a physical extension of the speaker. All network traffic from the button to use Amazon services goes through the paired device. Don’t buy buttons if you don’t already have an Alexa, as they don’t do anything on their own.

If you have multiple speakers associated with your account, the button will only work with the device it’s currently paired with. The pairing can be undone with just a few steps on your phone. To unpair a device, just use the Alexa companion app and go into the settings section. Select the button that has already been paired, and it will release it. Then go back through the steps to repair to another device.

![Image](https://cdn-media-1.freecodecamp.org/images/hivuzrSwuf4WcMXDB25tWOKDBXz6qIeQHMiy)
_Screenshot of Alexa App on a Mobile Device_

This makes buttons an easy add on for Alexa enthusiasts, and makes them flexible for those with multiple devices.

### How Buttons Interact with Custom Skills

Alexa is an event driven architecture. Events are created by the sounds going into the speaker that are translated through Cloud based service. Normally these events are initiated after the array of microphones picks up a command from a user. These commands are then translated by the ASR (Automated Speech Recognition) models depending on which custom skill is being used.

With buttons, a new type of event is created that follows a similar pattern. When the button is pressed, an event is created and sent to the skill that runs in the Cloud. When the button is released, a separate event is created. These events are created independently of anything being picked up by the microphones on the Echo Speaker and flow through a Cloud based service called the Game Engine.

![Image](https://cdn-media-1.freecodecamp.org/images/xn54u0QFvTYWHG-5EBh2IwBAYKiYXRMUVCAY)
_Alexa Event Architecture including Buttons_

The Lambda function that contains the logic for the custom skill needs to process these events along with the existing voice triggered ones. Translating request objects is facilitated by the Alexa SDK installed in the Lambda function. Examples of how this works are provided in the [Alexa repo](https://github.com/alexa/skill-sample-nodejs-buttons-hellobuttons).

This opens up new possibilities for gameplay, as a user can leverage both their voice and hands to interact with the skill. Engaging more senses broadens the experience, and enables more complex gaming. For example, in the [Seventh Inning Stretch skill](https://www.amazon.com/Seventh-Inning-Stretch-Baseball-Game/dp/B071FF8WCN), a user can play a baseball game listening on their speaker while pressing the button to swing the bat.

### How Skills use the Gadgets API

Using buttons within a custom skill requires the Gadgets API. Documentation is currently on this [website](https://developer.amazon.com/docs/gadget-skills/understand-gadgets-skill-api.html), and note that it is still in beta. Buttons are just a type of gadget, and provide a glimpse into what’s possible with enabled hardware.

Connectivity between systems is facilitated by interfaces across the internet. The API that buttons need is invoked by adding directive attributes to a standard Alexa response object. This enables the SDK to handle the explicit details for the HTTPS call (i.e. encoding the header, setting the attributes, error handling, etc.)

Here is an example of adding a directive to set the lights on a button at the same time that the Echo speaker reads back an introduction to the user.

```
"response": {               "shouldEndSession": false,               "outputSpeech": {                     "type": "SSML",                     "ssml": "<speak> Welcome back to Seventh Inning Stretch.<break time=\"1s\"/>We found an prior game in progress. Would you like to resume? </speak>"                 },               "reprompt": {                     "outputSpeech": {                           "type": "SSML",                           "ssml": "<speak> Say yes to resume the in-progress game, or no to delete it.  </speak>"                     }               },               "directives": [    {                           "type": "GadgetController.SetLight",                            "version": 1,                           "targetGadgets": [],                           "parameters": {                      "animations": [               {                         "repeat": 1,                            "targetLights": ["1"],              "sequence": [                          {                    "durationMs": 30000,                                                               "color": "FFFF00",                  "blend": false                                                     }              ]                      }           ],      "triggerEvent": "buttonDown",                                "triggerEventTimeMs": 0    }}
```

The Game Engine creates events just like the Echo speaker. The same taxonomy is used, and the attributes within the request identifies event details. Below is an example of a request indicating that a button was pressed.

```
“request”: {   “type”: “GameEngine.InputHandlerEvent”,   “requestId”: “amzn1.echo-api.request.xxx”,   “timestamp”: “2018–07–21T21:33:25Z”,   “locale”: “en-US”,   “originatingRequestId”: “amzn1.echo-api.request.xxx”,   “events”: [     {       “name”: “button_down_event”,       “inputEvents”: [ {         “gadgetId”: “amzn1.ask.gadget.xxxx”,         “timestamp”: “2018–07–21T21:33:25.374Z”,         “color”: “000DD6”,         “feature”: “press”,         “action”: “down”       } ]     }   ] }
```

### Save Battery Life through Roll Call

Echo Buttons are battery powered, making energy management important. When a custom skill requires a button, it must initiate a connection and wake the button. This is done through a process called ‘roll call’ within the custom skill.

To initiate a roll call in a custom skill, add a directive to the response object providing the parameters to perform the task. In parallel, audio instructions need to be included in the response object. These will encourage a user to do something with the buttons. For example, ask the user to press each button to get started.

For specifics on what a directive looks like, here is the roll call directive I use for my Seventh Inning Stretch skill. It’s a series of attributes in a large JSON object. This sets the timeout parameter for when the buttons can go back to sleep if not used (the 300,000 value is in milliseconds — this translates to five minutes), and looks for just the button down event.

```
"directives": [  {     “type”: “GameEngine.StartInputHandler”,     “timeout”: 300000,     “recognizers”: {       “button_down_recognizer”: {         “type”: “match”,         “fuzzy”: false,         “anchor”: “end”,         “pattern”: [{ “action”: “down” }]       }    },     “events”: {       “button_down_event”: {         “meets”: [“button_down_recognizer”],         “reports”: “matches”,         “shouldEndInputHandler”: false       },       “timeout”: {         “meets”: [“timed out”],         “reports”: “history”,         “shouldEndInputHandler”: true       }     }  }]
```

The buttons handle the timer for when to turn off. This minimizes the risk of battery drain when a user ends their session. Skills that use buttons should also make a request to the shut off the device if the skill is exited.

### Translating Game Engine Events

The Game Engine can create events just like the speaker after it is awake. The request uses the same taxonomy, and the attributes identify details of the event. Here is an example of a request indicating that a button was pressed.

```
“request”: {   “type”: “GameEngine.InputHandlerEvent”,   “requestId”: “amzn1.echo-api.request.xxx”,   “timestamp”: “2018–07–21T21:33:25Z”,   “locale”: “en-US”,   “originatingRequestId”: “amzn1.echo-api.request.xxx”,   “events”: [     {       “name”: “button_down_event”,       “inputEvents”: [ {         “gadgetId”: “amzn1.ask.gadget.xxxx”,         “timestamp”: “2018–07–21T21:33:25.374Z”,         “color”: “000DD6”,         “feature”: “press”,         “action”: “down”       } ]     }   ] }
```

The logic within the Lambda function for the skill will need to respond to these events, and process functionality accordingly.

### Buttons Can Change Color

Inside the buttons are a series of LED’s that can be turned off and on. They are bright and the color is very rich.

![Image](https://cdn-media-1.freecodecamp.org/images/9gmdYm6OjjrrCzjeM0DLTLJ-RDtTdnB3gfKd)

The buttons can also change colors by altering how the different LED’s are illuminated.

![Image](https://cdn-media-1.freecodecamp.org/images/fr7rACZlz0hBY5apboKduTEjVd7cK8tlXGDz)

Color changing of the buttons is also done within directives in a response object. If you start your skill using the [repo for buttons](https://github.com/alexa/skill-sample-nodejs-buttons-hellobuttons), there are helper functions that make this easy to integrate into your skill.

### Closing

If you’re interested in trying out a game that uses them, please test out my baseball simulation game on Alexa. It’s called “Seventh Inning Stretch” and is an attempt to recreate the fun of old handheld games from the 80’s. It’s a good example of what’s possible using these new accessories.

![Image](https://cdn-media-1.freecodecamp.org/images/ACXMJEoX78nZezIBRNITH7S5eSIsL0Jka5z6)
_Example of Alexa Skill that uses Buttons_

