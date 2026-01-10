---
title: How to change the color of Google Maps markers with JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T13:16:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-javascript-google-map-marker-color-8a72131d1207
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d635FJj7G3ZEAZdyLUaeSg.png
tags:
- name: google maps
  slug: google-maps
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tan Le Tian

  Make them pink, blue, green, yellow or purple!


  By default, the Google Maps marker is red in color. This article will show how to
  add different color markers to Google Maps. So, let’s get started. ?

  1. Load Google Maps

  Create an HTML f...'
---

By Tan Le Tian

#### Make them pink, blue, green, yellow or purple!

![Image](https://cdn-media-1.freecodecamp.org/images/1*d635FJj7G3ZEAZdyLUaeSg.png)

By default, the Google Maps marker is red in color. This article will show how to add different color markers to Google Maps. So, let’s get started. ?

### 1. Load Google Maps

Create an HTML file which loads Google Maps by following [Google Maps API official docs: Hello World](https://developers.google.com/maps/documentation/javascript/tutorial).

Your code will look something like the code snippet below.

**Note:** Remember to change `YOUR_API_KEY` to your actual Google Maps API key.

### 2. Add different color markers

To add a blue color marker, we need to change the icon of the marker. This is done by adding an icon property and specifying a URL for it like below.

```
icon: {                               url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"                           }
```

Note that we specify `blue-dot.png` at the end of the URL to get a blue marker. To add a green marker simply change it to `green-dot.png` so that the URL will be `[http://maps.google.com/mapfiles/ms/icons/green-dot.png](http://maps.google.com/mapfiles/ms/icons/blue-dot.png)` .

Some other colors available:

1. pink: `pink-dot.png`
2. yellow: `yellow-dot.png`
3. purple: `purple-dot.png`

To get the URL of more marker icons, please refer to [this website](https://sites.google.com/site/gmapsdevelopment/).

### 3. Wrap into add marker function

To make the code cleaner, we can define an `addMarker` function which takes in `latLng` and `color` of the marker. Note that we store the markers added in the a global `markersArray` in case we need to perform any operations on the markers later.

Open the HTML file in the browser. It should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vkqPZHbgS4iz9zOtVKvf6g.png)

You can get the full final version of the code from [here](https://gist.github.com/getsudocode/605bf60f5de40eb3f6b00addd93c913d). Please let me know how it goes in the comments below.

Feel free to check out another Google Maps tutorial I have written:  
[Implement click on JavaScript Google Map to add draggable markers with polyline](https://medium.com/@letian1997/click-javascript-google-map-add-draggable-markers-polyline-b834dd5762b2)

