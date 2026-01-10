---
title: How to use Alexa Presentation Language in your skill
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T17:08:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-alexa-presentation-language-in-your-skill-3c49961825c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Yhxg6EjPOGffEe0-01U-RQ.png
tags:
- name: Alexa Skills
  slug: alexa-skills
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Garrett Vargas

  Amazon recently released the Alexa Presentation Language (APL). APL provides a richer
  display for multimodal skills. It is based on modern frameworks that separate display
  elements from data sources. It gives you the flexibility to ...'
---

By Garrett Vargas

Amazon recently released the Alexa Presentation Language (APL). APL provides a richer display for multimodal skills. It is based on modern frameworks that separate display elements from data sources. It gives you the flexibility to include many visual elements such as graphics, images, and slideshows and lets you tailor the display for different devices.

In this article, I’m going to walk through how I updated one of my skills to use APL. You can also use these tips and techniques if you are creating a new skill.

Most of my skills feature multimodal support using the [Display Interface](https://developer.amazon.com/docs/custom-skills/display-interface-reference.html). I decided to learn APL by updating one of my existing skills. I focused on my [Video Poker](https://www.amazon.com/Garrett-Vargas-Video-Poker/dp/B07465B5ZK) skill because I wasn’t happy with the existing customer experience.

Video Poker presents users with a 5-card poker hand, with an ability to hold and discard cards before drawing to complete a hand. Users can do this by voice command (“keep the first card” or “keep the pair of jacks”), or by touching cards on a visual display. **ListTemplate2** was the best way to do this with the Display Interface. However, this came with the limitation of only allowing three cards on the screen at a time and putting numbers beneath each card in the list.

![Image](https://cdn-media-1.freecodecamp.org/images/jMxKMUHlUnJBPaXP4c5kx7rCPL1WFe3DEqhJ)
_Video Poker using ListTemplate2 Display Directive_

Using APL, I modified a ListTemplate2 layout to shrink the size of list items, reduce the spacing between them, and fit a full five card hand on the screen. I was able to remove the numbers from items in the list and put text indicating which held cards in a bold, red font. I was able to optimize the layout for different screen dimensions, such as smaller displays like the Echo Spot.

![Image](https://cdn-media-1.freecodecamp.org/images/jd4xu4HhI8hhfhPXvDtzJMByErFxomzeWU6r)
_Video Poker using APL template modified from ListTemplate2_

#### APL Authoring Tool

The way I did this was through the [APL Authoring Tool](https://developer.amazon.com/alexa/console/ask/displays). This handy tool provides a list of different visual designs you can use as a baseline to create compelling visuals for your skill. It also allows you to save and upload layouts, so you can extract them to your skill code, or upload them if you make offline updates. For this use case, I started with the **Image Forward List Sample**, which is based on ListTemplate2.

![Image](https://cdn-media-1.freecodecamp.org/images/Z2PFZCT6MUCN64bPTQ9qRs4XBXem42fTGEqB)
_Selecting a visual design from the APL Authoring Tool_

Once you select this visual design in the tool, you’ll see a generic example of a list with cheese samples. You’ll see the APL document at the bottom of the screen separated into two tabs:

* “Image Forward List Sample” which provides the layout
* “Data JSON” tab which provides a view of the document data.

![Image](https://cdn-media-1.freecodecamp.org/images/AJFvDwilgG-7N3H4tH0f6tq73tvsNnr8lSGG)
_Editing your APL Document in the Authoring Tool_

Take a moment to look through the JSON on both the Image Forward List Sample tab (the layout code) and the Data JSON tab (the content code). You’ll notice in the layout that there are several references to values enclosed in `${}` such as `${payload.listTemplate2ListData.listPage.listItems.length}`. If you look in the content file, you’ll see that this is a path to a value within the content. This is how APL binds data to the presentation layer and lets you make changes.

#### Updating Data Sources

As a first step, I wanted to update the data so it would show card images and text relevant to my skill. That way, as I started to update the layout itself, I would be able to see how it would look with my actual images. The Authoring Tool shows your rendered screen images in real time, making it convenient to use as you attempt to perfect your layout. To update the data, I took the following steps:

* Click on the Data JSON tab
* In the `listTemplate2Metadata`, change the `title` and `logo` elements to something relevant to Video Poker
* In this same element, change the `url` in the `backgroundImages.sources` fields to point to the background image I wanted to use
* In `listTemplate2ListData.listPage`, I updated each of the items in the `listItems` array. Specifically, I updated this array to have 5 items (my cards), with `listItemIdentifier` and `token` set to “card.x” (where x ranged from 0–4). I removed the `secondaryText` since I only wanted one row of text (which would either be blank or say “HELD”). I updated the `image.sources` to point to URLs containing my card images. For now, I just selected some card images at random — my skill’s code will update the data during gameplay with the actual user’s hand
* Update the hint text to use a transformation. Rather than hard-coding the hint string with the Alexa keyword, you can use a transform to change a hint into one that uses the wake word associated with the device, in case the user has changed it. You do this by removing the `hintText` from listTemplate2ListData and adding the following into your lastTemplate2Metadata:

```
"properties": {    "hintText": "select number 1"},"transformers": [    {        "inputPath": "hintText",        "transformer": "textToHint"    }],
```

Once I had made these to the data sources, my image looked like this — pretty similar to the skill as it exists with the ListTemplate2 display which makes sense since at this point I’m still using the layout based on ListTemplate2 and have only made content changes.

![Image](https://cdn-media-1.freecodecamp.org/images/2w4rK8o0mL8as6gmh7utg757rRzeYHfBWjVK)
_Updated view with relevant Video Poker content_

#### Updating the Layout

Now for the fun part — updating the layout to get five images on the screen at one time. For this part, I made updates to the layout on the “Image Forward List Sample” tab. To make these changes, I clicked on the slider that lets you switch between a visual view of nested APL components to a raw JSON view. I find viewing the full document JSON easier to consume than clicking on each component and editing the JSON within the component. But you can play with it and follow whichever approach seems most natural to you.

Before talking through the changes I made, I wanted to point out some of the elements of this layout template:

* There is a `ListTemplate2` node in the JSON which provides two containers in an `items` node— one that applies to circular screens (like the Echo Spot) and the other for other screen types. In this blog, I’m going to focus on the non-Spot displays, but you should appreciate that you can also make changes specific to different screen layouts.
* Looking at the second container that we’ll be changing, you‘ll see a set of `items` including an Image (the background image), an **AlexaHeader** (the title on the screen), a **Sequence** (which is the list of cards), and an **AlexaFooter** (the hint at the bottom of the screen)
* You’ll see that the Sequence points to `HorizontalListItem`, which is another container in this JSON document. It contains items consisting of an Image and two Text elements (the primary text and the secondary text)

With this context in mind, I made the following changes to this document:

* Within the `HorizontalListItem`, I changed the Image item dimensions — specifically I set `height` to 40vh and `width` to 17vw. This sets the height of each card to 40% of the viewport height, and the width to 17% of the viewport width.
* I then updated `midWidth` to 100. This makes the width of each list item smaller and allows the five card images to appear on the screen
* I changed `paddingLeft` and `paddingRight` to 6 to reduce the amount of space between elements
* I added `paddingTop` and set it to 100 to add some separation between the header and the card images
* I got rid of the secondary Text element since I don’t have two lines of text on my display
* I changed the primary Text element so it doesn’t draw the ordinal. So `text` in this element changed from `<b>${ordinal}.</b>${data.textContent.priam`ryTe`xt.text} to <b>${data.textContent.pri`maryText.text}</b>.
* Within this same element, I wanted the text to be red and centered. I achieved this by adding a `textAlign` field with a value of “center,” and a `color` field with a value of “red.”
* In order to get the hint text from the appropriate location (now part of the metadata rather than the list data), I needed to update the AlexaFooter element to get the hint from `${payload.listTemplate2Metadata.properties.hintText}`

Finally, I needed to make the cards in my list selectable, so I could respond when the user touches one of them on the screen. To do this, I needed to change the items that were associated with the `Sequence` element from a `FullHorizontalListItem` to a `TouchWrapper` which in turn contained a `FullHorizontalListItem`. In code, that means that I changed this:

```
"item": [  {    "type": "FullHorizontalListItem",    "listLength": "${payload.listTemplate2ListData.listPage.listItems.length}"  }]
```

to this:

```
"item": [  {    "type": "TouchWrapper",    "onPress": {      "type": "SendEvent",      "arguments": [        "${data.token}"      ]    },    "item": {      "type": "FullHorizontalListItem",      "listLength": "${payload.listTemplate2ListData.listPage.listItems.length}"    }  }]
```

Note the `onPress` element in this item. Specifically, the list of arguments. You can specify an array of different arguments to send to your skill when an item is selected. Because my existing code was processing the token of the selected card, I decided to continue to do the same to minimize the amount of code I needed to change. But you could also pass in `${ordinal}` which would tell you the index of the selected item without having to process the token.

#### Updates to the Skill Code

Once you’ve made changes within the Authoring Tool, you can select the Export Code button which will package up your layout and data files into one JSON file for you. I chose to use two different JSON files in my code, one called main which I used for the layout and another called datasources which I used for the data. I like keeping the separation of layout and content in my source code as a general best practice. It was surprising that Amazon’s Authoring Tool didn’t encourage this too.

Now that we’ve downloaded the document and content, we need to make code changes to incorporate it and update the data as the user plays with our skill. We can do this by manipulating data elements and then passing them back to the skill. I used Alexa’s response interceptor functionality (which I talk about in a [separate blog post](https://medium.freecodecamp.org/how-to-improve-your-code-with-alexa-response-interceptors-2b3e73721fc)). I load the data source in from a JSON file, then update the cards and text within the structure before sending it off to Alexa. I do that with the following code:

```
const main = require('./main.json');const datasource = require('./datasource.json');
```

```
function drawTable(handlerInput) {  const event = handlerInput.requestEnvelope;  const attributes = handlerInput.attributesManager.getSessionAttributes();  const game = attributes[attributes.currentGame];  let i;  let cardText;  let url;
```

```
  // Update the images  for (i = 0; i < game.cards.length; i++) {    const card = game.cards[i];    url = GetCardURL(card);    cardText = (card.hold) ? 'HELD' : '';    datasource.listTemplate2ListData.listPage.listItems[i]      .textContent.primaryText.text = cardText;    datasource.listTemplate2ListData.listPage.listItems[i]      .image.sources[0].url = url;    datasource.listTemplate2ListData.listPage.listItems[i]      .image.sources[1].url = url;  }  // Give an appropriate hint  if (game.state === 'FIRSTDEAL') {      if (game.cards[0].hold) {        datasource.listTemplate2ListData.hintText = 'discard the first card';      } else {        datasource.listTemplate2ListData.hintText = 'hold the first card';      }      datasource.listTemplate2Metadata.title = 'Select cards to hold or say Deal';    } else {      datasource.listTemplate2ListData.hintText = 'deal';      datasource.listTemplate2Metadata.title = 'Your last hand';    }  }  return handlerInput.responseBuilder    .addDirective({      type: 'Alexa.Presentation.APL.RenderDocument',      version: '1.0',      document: main,      datasources: datasource,    });}
```

The second place I had to make a code change was to handle the user touching one of the items in my list. In my old code, I was parsing item tokens of the form “card.x” where x is the ordinal position of the card in the list. With a Display Interface, this meant looking for an `ElementSelected` request. In APL, your code will receive an `APL.Presentation.APL.UserEvent`, and you can process the request as follows to determine which card was selected:

```
module.exports = {  canHandle(handlerInput) {    const request = handlerInput.requestEnvelope.request;       // Was this a touch item selected?    if (request.type === 'Alexa.Presentation.APL.UserEvent') {      return ((request.source.type === 'TouchWrapper')        && (request.source.handler === 'Press'));    }    return false;  },  handle(handlerInput) {    let index;    const event = handlerInput.requestEnvelope;    // Was this a touch item selected?    if (event.request.type === 'Alexa.Presentation.APL.UserEvent') {      const cards = event.request.arguments[0].split('.');      if (cards.length === 2) {        index = cards[1];      }            // Do something with the selected card...
```

```
    }  },};
```

With these changes, I had a much cleaner looking Video Poker skill, which is sure to delight my customers more than the older format I was using. I’ve just started scratching the surface in terms of APL’s capabilities. But I can tell it will open up a new world of possibilities for voice-driven multimodal skills! Let me know in the comments about your own learnings with this new framework.

