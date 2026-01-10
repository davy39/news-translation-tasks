---
title: How to create a video channel for the Amazon Alexa Show without YouTube
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T13:04:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-video-channel-for-the-amazon-alexa-show-without-youtube-92cea2cdcb7d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yF98uEJJ2R1z3sxd8eAZ6Q.png
tags:
- name: Alexa
  slug: alexa
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: videos
  slug: videos
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'By Terren Peterson

  I’m a software engineer that has published more than twenty custom skills on the
  Alexa platform. I’ve been recognized as an Alexa Champion, and have won multiple
  hackathons using the technology. The following highlights how I built...'
---

By Terren Peterson

I’m a software engineer that has published more than twenty custom skills on the Alexa platform. I’ve been recognized as an [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson), and have won multiple hackathons using the technology. The following highlights how I built a custom video skill for the Echo Show using native Amazon technology.

### The History of Video Consumption

Video broadcasting has been a successful medium for more than [sixty years](https://en.wikipedia.org/wiki/History_of_television). Television sets dominated the entertainment industry for decades with broadcast signals beaming directly into living rooms. In [1990,](https://www.ncta.com/cables-story) Cable Television had reached 57% of US households. This rapidly expanded the variety of content consumed by viewers.

Live streaming officially began in [1995](https://www.theguardian.com/media-network/media-network-blog/2013/mar/01/history-streaming-future-connected-tv), but it wasn’t until 2007 that internet-based streaming began to use the standard HTTP protocol. Smartphones like the iPhone were added soon after using similar communication methods. With the push to mobile, smaller screens started gaining more of our time. YouTube has been a huge success during this phase, and now plays [5 billion videos a day](https://www.bluleadz.com/blog/25-eye-opening-youtube-statistics-infographic).

In 2015, [Amazon launched](https://www.androidcentral.com/amazon-echo-now-available-everyone-buy-17999-shipments-start-july-14) the first device controlled solely by a user’s voice. Voice platforms like Alexa rapidly added another device to the home, with an [estimated 35 million](https://techcrunch.com/2017/11/08/voice-enabled-smart-speakers-to-reach-55-of-u-s-households-by-2022-says-report/) already being used in the US. In [2017](https://www.macrumors.com/2017/05/09/amazon-echo-show-june/), Amazon officially launched their first version of Alexa with a screen, called the Echo Show. The [new Amazon Fire TV](https://www.theverge.com/circuitbreaker/2017/9/11/16287812/amazon-new-fire-tv-2017-alexa) devices also have Alexa built in, enabling streaming video to a flat screen display to be controlled by your voice.

The Echo Show initially included the capability to play videos from YouTube, but lately, Google and Amazon [have been fighting](http://variety.com/2017/digital/news/amazon-echo-show-sales-down-youtube-1202582660/) about it’s availability. This impacted the popularity of the product given how big of a feature video playing was.

At the [2018 CES](https://www.cnet.com/news/google-home-assistant-smart-displays-echo-show-lenovo-lg-sony-jbl-ces-2018/), multiple consumer electronics companies announced that they were launching a Google Home compatible device with a screen. This makes the voice market even more competitive. One solution to the YouTube compatibility challenge is to host video content directly on Amazon. The following describes how to create a custom skill for the Echo Show that does just that.

### How to Create a Custom Video Skill on Alexa

Building your own video channel is surprisingly easy using Alexa and a handful of AWS services. Here is the architecture featuring a custom Alexa skill that packages content to play on an Echo Show. The AWS storage service (S3) stores the media, and streams it to the device based on instructions given by the custom skill.

![Image](https://cdn-media-1.freecodecamp.org/images/2xU4Q2AmV3qQfrKVwBMppDWKgmt1hUjJmWGz)
_Component Level Architecture for Custom Video Skill_

Producing content for this is comparable to that required for a YouTube channel. The current version of the Echo Show (as well as the Echo Spot) have specifications around the media type to follow. For example, the video should use an mp4 extension and a standard [H.264 compression](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC) format. The resolution of the video quality should be no greater than 1280x720 in pixel size. These constraints provide a high quality video stream on the Show’s seven inch display comparable to that of a HD video player.

### Building the Custom Video Skill

Creating a video channel requires authoring a custom skill for Alexa and publishing it to the public skill store. There are a number of features needed for navigating the content in the channel and playing the videos. This section will cover these steps in detail. For a working example, try out the Piano Teacher skill that is already in the [Alexa store](https://www.amazon.com/Piano-Teacher-video-Echo-Show/dp/B078M9843X/). It is a skill that contains short videos with beginner lessons on how to play the piano, as well as note-by-note video instructions on how to play simple songs. [Here](https://github.com/terrenjpeterson/pianoplayer) is the repo that contains all the source code needed, as well as detailed instructions to configure and deploy.

There are three features required to make a video channel.

1 — Render a background image when the skill is initially launched. This establishes the channel’s brand.  
2 — Build navigation controls to browse and select which video to play. This includes handling touch gestures on the Echo Show screen.  
3 — Delegate control to the device to play a video once content is selected.

#### 1 — Brand with a Background Image

To facilitate the building of custom video skills, Alexa provides a series of templates. I use the “BodyTemplate1” template to render the background image when the skill is first invoked. When generating the metadata within the Alexa Developer Console, check the second and third boxes on the global fields screen (Video App & Render Template).

![Image](https://cdn-media-1.freecodecamp.org/images/8sZgyh5SKjVkQhGa7z0VXsUsfTy40xsVyG1T)

Setting these attributes enables additional APIs within the custom skill. Additional standard intents are required to use the APIs. These are created when building the intent model in skills kit. They are as follows:

* AMAZON.NavigateSettingsIntent
* AMAZON.NextIntent
* AMAZON.PageDownIntent
* AMAZON.PageUpIntent
* AMAZON.PreviousIntent
* AMAZON.ScrollDownIntent
* AMAZON.ScrollLeftIntent
* AMAZON.ScrollRightIntent
* AMAZON.ScrollUpIntent

No coding in the Lambda function is required for these events, as the device will handle them natively. They just need to be included in your custom skills intent model.

Rendering a background image requires two utility methods that are already distributed in the standard Alexa SDK. The skill creates two identifiers to illustrate how they are used.

```js
// utility methods for creating Image and TextField objects

const makePlainText = Alexa.utils.TextUtils.makePlainText;
const makeImage     = Alexa.utils.ImageUtils.makeImage;
```

Next, I add an identifier for the location of your jpg/png file that serves as the background image. This object needs to be publicly available. The pixel size is 1024x600 based on the dimensions of the Echo Show. You don’t need to provide a separate image for the smaller Echo Spot. Alexa creates the smaller image based on the original file sized for the Show.

```js
// This is a public endpoint - the easiest way is to host in S3
// It needs to be SSL enabled (which S3 does for you)

const backgroundImage = ‘https://s3.amazonaws.com/.../image.jpg';
```

Next, add the following code to render the background image when the skill gets launched, along with any other audio messages.

```js
‘LaunchRequest’: function () { 
  const builder = new Alexa.templateBuilders.BodyTemplate1Builder();
  const template = builder.setTitle(‘Your Personal Instructor’)
      .setBackgroundImage(makeImage(backgroundImage))
      .setTextContent(makePlainText(‘Piano Teacher’)) 
      .build();
      
  // check if the device has a video screen
  if (this.event.context.System.device.supportedInterfaces.Display){      
    this.response.speak(welcomeMessage)
        .listen(repeatWelcomeMessage).renderTemplate(template);
    this.emit(‘:responseReady’);
  } else {
    // handle error of not having a video screen to play
    this.emit(‘:tell’, nonVideoMessage);
  } 
},
```

#### 2 — Content Navigation

The navigation for the content takes advantage of the flexibility of the Alexa platform. The viewer can use either their voice or fingers to navigate the content catalog, selecting exactly what they would like to view. This requires using the list template within the Alexa SDK, as well as handling events triggered from the user touching the screen.

Here are the different options that the user may request using either their voice or touching the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1DKSPxIQBKi6Zz8ile8GVUV4YzQL26Xh1Wr1)

Rendering a list of what content is available is central to the user experience. I use ‘ListTemplate1’ from the Alexa SDK to render the list of videos. Scrolling up and down can be done through either voice or touch, and is handled by the device with no coding required.

The response object that is sent to list the content contains an array listing what is available on the channel. In my skill, this list is read by the Alexa voice, and is rendered visually on the screen. Here is an example of what it looks like.

![Image](https://cdn-media-1.freecodecamp.org/images/ULRD5TKnXiNO4c35VuKDNOYhHO55e8jzUzEX)
_Screenshot of Piano Teacher Skill on an Alexa Show_

Within the code, the content is externalized into an array object (songs.json) that contains a list of videos, as well as metadata about the location of each media file. Each item in the list has a unique token assigned. Here is a sample of the layout written in standard Javascript object notation:

```json
[ 
  { “requestName”: “Silent Night”, 
    “listSong”:true, 
    “token”:”song001", 
    “difficulty”:”Moderate”, 
    “videoObject”: “SilentNight.mp4”, 
    “audioObject”: “SilentNight.mp3” 
  }, 
  { “requestName”: “Mary Had a Little Lamb”, 
    “listSong”:true, 
    “token”:”song002", 
    “difficulty”:”Easy”, 
    “videoObject”: “MaryHadLittleLamb.mp4”, 
    “audioObject”: “MaryHadLittleLamb.mp3” 
  },
...
]
```

Here is the code that converts the array into the response needed by Alexa. Included is embedding the token for each item in the array.

```js
// these are the songs that recordings have been made for
var songs = require("data/songs.json");

// create List
const itemImage = null; 
const listItemBuilder = new Alexa.templateBuilders.ListItemBuilder(); 
const listTemplateBuilder = new Alexa.templateBuilders.ListTemplate1Builder();

// build an array of all available songs 
for (i = 0; i < songs.length; i++ ) { 
  if (songs[i].listSong) { 
    // pull attributes from song array and apply to the list
    listItemBuilder.addItem(null, songs[i].token,
      makePlainText(songs[i].requestName),
      makePlainText(songs[i].difficulty)); 
     message = message + songs[i].requestName + “, “;
  } 
} 
message = message + “Just select on the screen a song, or request by saying something “ + “like, Teach me how to play “ + songs[0].requestName + “.”;

// now create the response object using the SDK
const listItems = listItemBuilder.build(); 
const imageLoc = pianoStrings; 
const listTemplate = listTemplateBuilder.setToken(‘listToken’)
  .setTitle(‘Available Song List’) .setListItems(listItems)
  .setBackgroundImage(makeImage(imageLoc)) 
  .build(); this.response.speak(message).listen(noSongRepeatMessage).renderTemplate(listTemplate); 
this.emit(‘:responseReady’);
```

The Lambda function handles the ‘ElementSelected’ event invoked by the Echo Show. The request object sent by the device to the custom skill contains the token used to translate what was selected by the user.

```js
// this function is invoked from the 'ElementSelected' event
‘ScreenSongSelected’: function() { 
  console.log(“Element Selected:” + this.event.request.token);
  var videoName = “”;
  // match token to song name and find the video object to play 
  for (i = 0; i < songs.length; i++ ) { 
    if (songs[i].token === this.event.request.token) { 
      console.log(“Play “ + songs[i].requestName);
      videoName = songs[i].videoObject;
    } 
  } 
  const videoClip = videoLoc + videoName;
  this.response.playVideo(videoClip); this.emit(‘:responseReady’); 
},
```

The Lambda function uses the token it receives and finds the media file corresponding to the unique identifier. Control is then transferred to the device with the appropriate video.

#### 3 — Delegate Control to the Video Player

Once the video that needs to be played is found, the endpoint of the media is added to the response. This requires a few lines of code within the Lambda function.

First, identify a folder in the S3 bucket where the video files will be stored.

```js
// These are the folders where the mp4 files are located

const videoLoc = ‘https://s3.amazonaws.com/…/media/';
```

Then specify the exact file based on what was identified by the user. Metadata is added that contains more information about the video.

```js
if (this.event.context.System.device.supportedInterfaces.VideoApp) {
  const videoClip = videoLoc + videoObject; // endpoint of the file
  // this will be rendered when the user selects video controls
  const metadata = { 
    ‘title’: slots.SongName.value 
  };
  this.response.playVideo(videoClip, metadata);
  this.emit(':responseReady');
} else {
  // handle error - and close the session
  this.emit(‘:tell’, nonVideoMessage);
}
```

After this code executes, the Alexa device will take over navigation of playing the video. The user can either use their voice or touch the screen to pause, rewind, fast-forward, etc. Here is what the screen looks like when playing a video, including the Metadata title at the top.

![Image](https://cdn-media-1.freecodecamp.org/images/KK4CNJ0uzgbElT7u2Lr-CJ2lWJJLWlrDkLzy)
_Screen shot of Piano Teacher Skill on an Alexa Show_

When the video playing on the device is complete, the skill can be used again to select more content.

### Summary

Building the custom skill can be done using the example above as a template in just a few hours. The Alexa certification process takes just a day or two, then the skill (and content within it) will be available for anyone with an Echo Show. As a fan of YouTube, I hope to be able to use it on my Alexa device soon, but there’s also a way for content publishers to go around it.

