---
title: How to code a chatbot tailored for web apps like Google Maps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T08:25:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-chatbot-tailored-for-web-apps-like-google-maps-cf97fc090676
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aJhKGNE9DKAbp8YODtMfSQ.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: google maps
  slug: google-maps
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: 'By Paul Pinard

  In this article, we’ll learn how to integrate a SAP Conversational AI chatbot into
  any of your web applications and provide users with a fun and intuitive way to interact
  with the UI!

  Conversational interfaces are gaining in popularity...'
---

By Paul Pinard

_In this article, we’ll learn how to integrate a SAP Conversational AI chatbot into any of your web applications and provide users with a fun and intuitive way to interact with the UI!_

Conversational interfaces are gaining in popularity, especially for transacting with seemingly opaque backend systems. For example, we can deploy a chatbot to walk a customer through a troubleshooting process and create a ticket if they require further assistance; all without the customer having to know the ticket creation process.

This allows for a more intuitive experience for your customer, increasing customer satisfaction, while also improving efficiency by freeing employees from handling the classification and routing of tickets.

Conversational AI can handle this out of the box, but what if your users want to be able to interact with your front end application?

For example, it might be nice for your user to navigate to a certain page within your website without having to find the exact link. Or allow your user to apply a complex filter to a list of products without having to click around menus.

Though our webchat can be imbedded in any website, it does not have the contextual awareness of the UI necessary for these sorts of interactions. To demonstrate how we can accomplish this contextual awareness, we will create a simple map application with an embedded bot that has the ability to move the map and zoom in or out:

![Image](https://cdn-media-1.freecodecamp.org/images/toqt9Ke0kTZX07moBvygkjtYpv7qsRdFzxB0)

### Resources

[Create your first chatbot on SAP Conversational AI](https://cai.tools.sap/blog/build-your-first-bot-with-sap-conversational-ai/)

[Learn how to selfhost the Webchat](https://github.com/SAPConversationalAI/Webchat#self-hosted-webchat)

[Google Maps APIs](https://developers.google.com/maps/documentation/javascript/tutorial)

[Map mover bot](https://cai.tools.sap/timoteo/map-mover)

[Frontend Application source code](https://github.com/timothy-janssen/map-app)

[Final Map Application](https://map-app-demo-1.herokuapp.com/)

### Pre-requisites

* First, you will need to be comfortable building a simple bot using [SAP Conversational AI](https://cai.tools.sap/). If you are unfamiliar with the platform, head over to [this tutorial](https://cai.tools.sap/blog/build-your-first-bot-with-sap-conversational-ai/) to learn how to build a hilarious joke bot.
* You will also need to be able to host our webchat component somewhere that you control. Our [GitHub](https://github.com/SAPConversationalAI/Webchat#self-hosted-webchat) has all the information to get you started.
* It is also expected that you are at least familiar with JavaScript and front end web development basics.

### Tutorial

To start, we will need to define the interface for our bot to be able to send commands and messages to our front end. This will be accomplished by sending a stringified JSON object in the place of the normal message string we generally send to the user. Our modified webchat will be able to understand this JSON object, take the defined action and finally display a “message” to the user.

This can be accomplished fairly simply; we will send an object with an action of either “_move_” or “_zoom_” and then a message that we can show to the user. Note that we will pass this JSON object as a string, and it is our assumption that the application will parse it and display only the value of “message” to the user.

```
{ "action": "move" || "zoom", "message": "This will be displayed to the user" }
```

If our action type is “_move_”, the map will need coordinates to navigate to.   
So, we will include a location’s coordinates in our JSON object. Alternatively, if our action is _zoom_, we will need to know whether to _zoom in_ or _out_. For this, we will include a direction represented as a 1 for in or a -1 for out. With this defined, here are some examples of what our JSON objects could look like:

```
{"action": "move", "location": { "lat": -8.3405389, "Ing": 115.0919509 "message": "Going to Bali, Indonesia!" }{"action": "zoom" "direction": 1, "message": "Zooming in!"}
```

With that in mind, we can start building our bot. As always, we will start with defining the intents our user could say. In this case we have _zoom_ and _move-map_.

![Image](https://cdn-media-1.freecodecamp.org/images/NIEtf89-2sa-bqKdTwqZHGGUZHtWPWMHoF7n)

Note that we will need to tag the sentences in _@zoom_ with the entity ‘direction’, but ‘location’ is automatically recognized in _@move-map_. Luckily for us, the location gold entity comes with the longitude and latitude out of the box, so we will be able to easily pass these to the front end.

To get the 1 or -1 that represents our zooming direction, we will leverage custom enrichments. We will add the keys “name” and “direction” with the following values. Then map the correct entity values to their respective key values.

![Image](https://cdn-media-1.freecodecamp.org/images/XZ0zra0PVE06eW8KruOypINZ4675DnIY6JJB)

Now that we can recognize our move-map intent, we just need a skill that is triggered if our intent is matched:

![Image](https://cdn-media-1.freecodecamp.org/images/Zax0InkCgVVGJNFdLbbENHLmsesnwdhmnuBh)

And requires a location:

![Image](https://cdn-media-1.freecodecamp.org/images/XyP2bn7OkfeOh75b5I5CcconwlgIdZZ1PPhk)

And finally sends a message back telling the front-end where to go:

![Image](https://cdn-media-1.freecodecamp.org/images/BEwrDwYK-iaXCdAyYgT-npS2a2AJ7Fjvh1rG)

The zoom skill can be implemented in much the same way; I encourage you to try it for yourself!

Now that our bot is done, we will need to host the webchat locally so that we can modify it to understand our “unusual” responses. If you are unfamiliar with the self-hosting process, check out [this github](https://github.com/SAPConversationalAI/Webchat#self-hosted-webchat).

Finally, it’s time to build our web application. We will start by including a container div for our map, the script we will write to handle the map interactions (map_controls.js), the necessary script as described in [this tutorial from Google](https://developers.google.com/maps/documentation/javascript/tutorial), and the script tag pointing to our locally hosted bot. It should look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/e4i94mJRLa5VonQkSluAfu0GyjxAvnNc0B5Z)

To complete our simple application, we will implement our map initialization and zoom/move methods:

```
function initMap () {  window.map = new google.maps.Map(document.getElementById('map'), {    // OPTIONS    center: {lat: -34.397, lng: 150.644},    zoom: 8,    zoomControl: false,    streetViewControl: false,    mapTypeControl: false,    rotateControl: false,    scaleControl: false,    fullscreenControl: false  });}     const zoom = (direction) => {  window.map.setZoom(window.map.getZoom() + direction);}
```

```
const setCenter = (lat, lng) => {  window.map.setCenter({lat: lat, lng: lng});}
```

Once we have the chatbot successfully added to our application, we will be able to ask it to move around or zoom in/out, but it will still just display that ugly JSON string to us. To solve that, we will add the following code to Webchat/src/containers/Chat/index.js. This will search the window object for a function called applicationParse and call it if it exists.

```
const getApplicationParse =  messages  => {  return new Promise(resolve => {    if (!window.webchatMethods || !window.webchatMethods.applicationParse) {      return resolve()    }    // so that we process the message in all cases    setTimeout(resolve, MAX_GET_MEMORY_TIME)    try {      const applicationParseResponse = window.webchatMethods.applicationParse(messages)      if (!applicationParseResponse) {        return resolve()      }      if (applicationParseResponse.then && typeof applicationParseResponse.then === 'function') {        // the function returned a Promise        applicationParseResponse          .then(applicationParse => resolve())          .catch(err => {            console.error(FAILED_TO_GET_MEMORY)            console.error(err)            resolve()          })      } else {        resolve()      }    } catch (err) {      console.error(FAILED_TO_GET_MEMORY)      console.error(err)      resolve()    }  })}
```

Now, we will call getApplicationParse before the call to setState in componentWillReceiveProps. This will ensure that our application has a chance to parse the response from the bot before anything is sent back to the user.

```
componentWillReceiveProps(nextProps) {  const { messages, show } = nextProps    if (messages !== this.state.messages) {    getApplicationParse(messages)    this.setState({ messages }, () => {      const { getLastMessage } = this.props      if (getLastMessage) {        getLastMessage(messages[messages.length - 1])      }    })  }  if (show && show !== this.props.show && !this.props.sendMessagePromise && !this._isPolling) {    this.doMessagesPolling()  }}
```

Finally, we need to implement applicationParse and include it in the window object from map_controls.js. Here, we will loop through our messages, and if it is a valid action command from the bot, take the action and return only the message back to the user.

```
window.webchatMethods = {  applicationParse: (messages) => {    messages.map(message => {      try {        var obj = JSON.parse(message.attachment.content);        console.log(obj);        if(obj !== undefined &&            obj.action == 'zoom' &&            typeof obj.direction === "number"){          message.attachment.content = obj.message.toString();          zoom(obj.direction);        } else if (obj !== undefined &&                    obj.action == 'move' &&                    typeof obj.location.lat === "number" &&                    typeof obj.location.lng === "number") {          message.attachment.content = obj.message.toString();          setCenter(obj.location.lat, obj.location.lng);        }      } catch (err) {        // Invalid JSON - treat it as a regular message and pass it back to UI as is      }      message    })     return messages;       }}
```

You can now ask your bot to move or zoom the map and it will send a message that the application can interpret and act upon.

With this tool in your tool belt, you can now integrate a chatbot into any of your web applications!

_Originally published on [SAP Conversational AI blog](https://cai.tools.sap/blog/how-to-control-your-web-application-with-an-integrated-chatbot/)._

