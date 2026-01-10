---
title: How to Use the YouTube IFrame API in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-17T22:55:52.000Z'
originalURL: https://freecodecamp.org/news/use-the-youtube-iframe-api-in-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6024fe5b0a2838549dcc345f.jpg
tags:
- name: api
  slug: api
- name: React
  slug: react
- name: youtube
  slug: youtube
seo_title: null
seo_desc: "By Kevin Cunningham\nAs a digital prototyping agency, my company works\
  \ with clients to help them quickly test the core of their ideas with their clients\
  \ and investors. \nOne of our clients is a group of doctors exploring ways to help\
  \ support older pati..."
---

By Kevin Cunningham

As a digital prototyping agency, [my company](https://spin-up.io) works with clients to help them quickly test the core of their ideas with their clients and investors. 

One of our clients is a group of doctors exploring ways to help support older patients with post-operative care.

There are a number of strands to the application, but one is sharing exercises with patients and tracking their success. The exercises are hosted on YouTube and shared in a NextJS application.

Last week, we got this request from the product manager:

> Hey,  
> Can we trigger a pop-up to ask the patient if they completed the exercise? This should trigger when the video ends or is paused at more than about 95%.

Up to this point, we were embedding the YouTube player and not interacting with the API. This was going to be fun.

## Exploring the documentation

The documentation for the [YouTube Player API](https://developers.google.com/youtube/iframe_api_reference#Events) is very clear. I could see there were various event listeners and data properties available to explore. The slight issue I had was that it is written in a vanilla JavaScript paradigm whereas I was working in React.

I've done this kind of conversion before. Exploring the creation and passing of `refs`, the use of `_document.js` in NextJS to use external scripts and dealing with some of the idiosyncrasies that make themselves known as you work through a project like this.

Before I dove in, I decided to have a look for a React library that might handle all of this for me.

## react-youtube library

Sometimes it is hard to find the library you are looking for and sometimes it isn't. In this case, the description of this library seemed to be exactly what I wanted:

> Simple [React](http://facebook.github.io/react/) component acting as a thin layer over the [YouTube IFrame Player API](https://developers.google.com/youtube/iframe_api_reference)

I didn't find the documentation for the library very helpful but, since it claimed to be a thin layer, I was hoping that I could lean on the YouTube documentation itself (spoiler alert: I could!).

## Laying out the project

I was going to need:

* A modal and a way to track its state;
* A function to convert a YouTube URL to the videoid that `react-youtube` needs
* A function to test if the video was at the target point
* The `react-youtube` embed.

## react-modal

I tend to enjoy projects that are named well and this is another one of those. 

For some it may seem a bit overkill to use a library for modals, but I'm a fan. Without a library like this, I'd have to build a lot of functionality myself (keyboard events, accessibility, clicking outside of the modal). 

The documentation gives some decent default styles, so I'll add these to the top of the project.

```js
const modalStyles = {
  content: {
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)"
  }
};
```

Inside my function, I'll add a `useState` hook to handle the status of the modal.

```js
 const [modalIsOpen, setModalIsOpen] = React.useState(false);
```

Now I'm ready to add my modal. I normally add this at the bottom of the component, but in reality you can add it wherever makes sense.

```js
      <Modal
        isOpen={modalIsOpen}  
        onRequestClose={() => setModalIsOpen(false)}
        contentLabel="Exercise Completed"
        style={modalStyles}
      >
        <div>
          <h3>Completed the exercise?</h3>
          <button
            onClick={handleExerciseComplete}
          >
            Complete exercise
          </button>
        </div>
      </Modal>
```

A couple of things to notice:

* The isOpen prop takes the state value we created above.
* The onRequestClose is toggling that state value to false. You could have a separate handle function but this seems a bit overkill.
* The style prop is receiving the constant we created above.

Inside the modal then, we are asking the question and providing a button to click if the patient has indeed completed it. I'm not going to explore what we are doing with the `handleExerciseComplete` function in the live code, so for now we'll just log to the console.

```js
const handleExerciseComplete = () => console.log("Do something");
```

## Preparing the videoID

The `react-youtube` library uses the videoID rather than the URL. Our content team are more comfortable with URLs and I don't want to make life harder for them.

Normally, I'm sourcing this from a content management system, but for this example I'll add an input field with a `useState` to track the value.

```js
const [videoUrl, setVideoUrl] = React.useState("");
```

```js
<input value={videoUrl} onChange={(e) => setVideoUrl(e.target.value)} />
```

Awesome! Now, we need to be able to get the id from the URL. If you've never looked at a YouTube URL in detail, it can look something like this [https://www.youtube.com/watch?t=746&v=LRini_YIs2I&feature=youtu.be](https://www.youtube.com/watch?t=746&v=LRini_YIs2I&feature=youtu.be). The video id is the string after `v=` and before the `&`. 

A simpler form of the URL could look like this [https://www.youtube.com/watch?v=N1pIYI5JQLE](https://www.youtube.com/watch?v=N1pIYI5JQLE) and we need to be able to handle this, too.

Here's my attempt at solving that problem.

```js
  let videoCode;
  if (videoUrl) {
    videoCode = videoUrl.split("v=")[1].split("&")[0];
  }
```

## Check elapsed time

The YouTube API makes a lot of helper functions available. The two that we're going to use are `.getDuration()` and `.getCurrentTime()`.  

We're going to use those two values to check if more than 95% of the video has elapsed. If it has, we're going to trigger the modal to open.

```js
  const checkElapsedTime = (e) => {
    const duration = e.target.getDuration();
    const currentTime = e.target.getCurrentTime();
    if (currentTime / duration > 0.95) {
      setModalIsOpen(true);
    }
  };
```

The `e.target` is equivalent to the `player` in the YouTube documentation. So, you can [check out the docs](https://developers.google.com/youtube/iframe_api_reference#onStateChange) to find other ways to interact with the video for your project.

## react-youtube

Now, we can finally add the YouTube component. We're going to use the `onStateChange` prop of the wrapper and pass our function down to it.

```js
          <YouTube
            videoId={videoCode}
            onStateChange={(e) => checkElapsedTime(e)}
          />
```

It feels slightly anti-climatic to see that now but we're done. We pass the event to our `checkElapsedTime` function and, if it passes the conditional, the modal will open.

There are a lot of other ways to hook into this API. The documentation lists the following:

```js
  onReady={func}                   
  onPlay={func}                   
  onPause={func}                    
  onEnd={func}                     
  onError={func}                    
  onStateChange={func}              
  onPlaybackRateChange={func}      
  onPlaybackQualityChange={func}   
```

Each of these will accept a function like the one we have created above. 

## Try it out

I've set up a [Code Sandbox](https://codesandbox.io/s/react-youtube-demo-f6l29) with the example code from this article. Head over there and drop a YouTube URL into the input box. Test what happens as you move through the video and, in particular, when you pause or track to 95% or more.

