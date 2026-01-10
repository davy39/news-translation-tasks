---
title: How to Use the JavaScript Fullscreen API
subtitle: ''
author: Gideon Akinsanmi
co_authors: []
series: null
date: '2023-07-10T21:02:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-javascript-fullscreen-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/js_fullscreen_png.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'The Fullscreen API is a browser web API that allows you to enable fullscreen
  mode for HTML elements. It saves you the stress of using CSS and JavaScript to implement
  fullscreen functionality.

  The use cases of fullscreen API are numerous because of th...'
---

The Fullscreen API is a browser web API that allows you to enable fullscreen mode for HTML elements. It saves you the stress of using CSS and JavaScript to implement fullscreen functionality.

The use cases of fullscreen API are numerous because of the increased complexity of today's websites. In this article I'll be giving you a comprehensive guide to using the Fullscreen API.

## Prerequisites

You should have basic knowledge of how to use HTML, DOM and JavaScript to create webpages. Specifically, you should know how to use HTML elements, DOM selector methods, event listeners, and JavaScript objects.

## Fullscreen API Basics

The Fullscreen API has functionalities that let you display your elements (mostly images, media, and graphic elements) in fullscreen mode. Without it, you'd need to get your hands dirty with some long lines of CSS and JavaScript code.

Have you ever visited a website where the images and videos go fullscreen when you interact with them? What about online games?

Let me explain some 3 real-world projects that use fullscreen mode. Although they might not be using the Fullscreen API under the hood, I'm trying to give you a practical view of the use cases of this functionality and how using the Fullscreen API can simplify the process. They include: the Twitter web app, an online gaming website, and YouTube video embeds.

An example of a project that uses fullscreen mode is the [Twitter web app](https://twitter.com). Whenever you log in to your Twitter account and click on any image that interests you, it goes fullscreen. This functionality could have been implemented with hundreds of lines of code. But with fFullscreen API, you wouldn't need that much code.‌

The same goes for online gaming websites. Whenever you visit a gaming website like [crazygames.com](https://crazygames.com) and click on any game you feel like playing, the canvas element that stores the game source code goes fullscreen.‌

‌Another example is the YouTube video embeds. If you are trying to embed a YouTube video on your website by using the iframe element with the `allow='fullscreen'`  attribute present, it allows your YouTube video go fullscreen when a user clicks on the fullscreen icon. Check out my [codepen link](https://codepen.io/gid-droid/pen/JjerqPg) and click on the fullscreen icon to observe the behavior.

Natively, the video element is the only HTML element that has capabilities by default. Whenever you create a video element with a controls attribute, it automatically gets a fullscreen control icon that allows you to toggle your video between fullscreen and normal mode. You can try it yourself.

Although the fullscreen API can be used on all major desktop and mobile browsers, sometimes it’s best practice to use multiple prefixed versions of some properties (for document.fullscreenElement there's `mozFullScreenElement` for Mozilla Firefox, or `webkitIsFullScreen`). If you have any doubts, you can check the prefix table on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API/Guide#prefixing).

## Fullscreen API Properties and Methods

To successfully use the Fullscreen API, ‌ need to be familiar with its properties and methods. They include:

* `**element.requestFullscreen()**`: This method tells the web browser to set a specified element in fullscreen mode.
* `**document.exitFullscreen()**`: This method tells the web browser to exit an element from fullscreen mode and return to normal mode.
* **`document.fullscreenElement`**: This property returns the element that is in fullscreen or checks if fullscreen mode is active. A value of null means no element is in fullscreen mode.
* `**document.fullscreenEnabled**`: This property checks whether the fullscreen mode is supported. It returns `true` if fullscreen mode is supported and `false` if it isn’t.
* `**fullscreenchange**` event: This event is used for detecting changes in the fullscreen mode. It can be used to create some functionality when fullscreen mode is activated and exited.

## How to Request Fullscreen Mode

The first step in implementing this functionality is to request fullscreen mode. You can do this with the `requestFullscreen()` method.

Here is the code to request fullscreen mode:

```js
let image = document.querySelector('image.img'); 

image.requestFullscreen();
```

‌The above code will return an error because fullscreen can only be activated through user interactions such as clicks, double clicks, and so on.

In the code below, we’ll use a click event to activate the fullscreen mode.

```js
let image = document.querySelector('img.image');

image.addEventListener('click', function(e){
      image.requestFullscreen();
})
```

‌In the code above, I used a `querySelector()` method to select an img element. Then I attached a click event listener to make the image go fullscreen when clicked.

## How to Exit Fullscreen Mode

After the fullscreen mode has been activated, you'll need an `exitFullscreen()` method to exit the fullscreen mode.

Here’s the code for exiting fullscreen mode:

`document.exitFullscreen();`

In a real-world project, you'll need a user to interact with the web page in order to exit fullscreen. You'll need an event listener that listens to user interactions like clicks, double clicks, keydown, and so on.

Here’s how you use an event listener with the `exitFullscreen()` function:

```js
let image = document.querySelector('img.image'); 

image.addEventListener('click', function(e){ 
     image.requestFullscreen(); 
 }) 
 
 image.addEventListener('dblclick', function(e){ 
      document.exitFullscreen(); 
})
```

From the code above, when a user clicks on the image, the fullscreen mode gets activated. When you double-click on the image, it gets deactivated.

## How to Check Fullscreen State

To check if an element is in fullscreen mode or not, we’ll use the `fullscreenElement` property.

A value of `null` means it's not in fullscreen mode.

From the example above, you can modify the code to activate and exit fullscreen mode based on the value of the `fullscreenElement` property.

Here’s how to use this property:

```js
image.addEventListener('click', function(e){ 

   if(document.fullscreenElement){ 
      document.exitFullscreen() 
   } else { 
     image.requestFullscreen();
   } 

})
```

From the above code, you’ve instructed the browser to toggle between full-screen and normal mode when the image is clicked.

## Event handling and Fullscreen State

Sometimes you might want to make some changes (such as alerting the user) when fullscreen mode is activated or exited.

Instead of using the document.fullscreenElement and multiple event handlers to check if an element is in fullscreen, you can use the ‘fullscreenchange’ event .

Here’s the code:

```js
document.addEventListener('fullscreenchange', function(e){ 

   if(document.fullscreenElement){ 
      console.log('fullscreen mode activated');
   } else { 
      console.log('fullscreen mode deactivated'); 
   } 
   
})
```

From the code above, anytime fullscreen mode is activated or exited from any element, a console.log() message is displayed in the developers tool.

## How to Apply Fullscreen to Various Element Types

Although fullscreen can be applied to all elements, it’s best used on media and interactive elements such as img, video, iframe, and canvas.

Although the use cases are numerous, I'll be explaining a few.

For your canvas element, if you are building an online game, it can be used to make your games fullscreen. Also, if you are building a dashboard with a canvas-based charting library, it can be used to make individual charts in your dashboard go fullscreen when the user clicks on them.

For your video element, if you are building a custom video player for your project, you can use it to implement fullscreen functionality.

For your image element, if you're building a web app (such as a social media platform) that supports image and video upload, you can use this API to implement fullscreen mode on the elements.

For iframe, embed and object element, if you are building an image-to-pdf converter website, you can use this API to make your converted PDF go fullscreen for reviewal by your users.

## Fullscreen API Best Practices and Tips

Here are the best practices and tips for fullscreen API:

1. Provide user-friendly controls for entry and exit: if you are implementing fullscreen on images, you should activate it when the user clicks on the image and exit when the user double tab or presses the backspace button. Similar user-friendly methods can be used on video and canvas elements. Also, make sure you notify the user when they enter and exit fullscreen.
2. Ensure fallback options for non-supported browsers: If a user is trying to activate fullscreen from an unsupported browser, you should alert them of this incompatibility.
3. If you are using fullscreen on iframes that links to external sources, don’t forget to set the `allow = 'fullscreen'` attribute.

```
<button>fullscreen</button>
<iframe allow='fullscreen' src='https://external.com/content' width='500' height='300'> </iframe> 
 
<script> 
    let button = document.querySelector('button'); 
    let iframe = document.querySelector('iframe'); 
    
    button.addEventListener('click', function (){  
       iframe.requestFullscreen();
    }) 
</script>
```

4. Mouse events (like mouseover) and alert() function might behave unexpectedly, so you shouldn't use them within fullscreen API.

## Conclusion

In this tutorial, you’ve learned what fullscreen API is, how to implement it, and the best practices to follow.

 I hope that you're now able to utilize the fullscreen API capabilities in your web projects

Feel free to check the MDN website for further learning. You can also follow me on Twitter (@GidtheCoder) to connect with me. Cheers.


