---
title: 'HTML5 Video: How to Embed Video in Your HTML'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T00:43:00.000Z'
originalURL: https://freecodecamp.org/news/html5-video
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d71740569d1a4ca37cc.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: video
  slug: video
seo_title: null
seo_desc: 'Before HTML5, in order to have a video play on a webpage, you would need
  to use a plugin like Adobe Flash Player. With the introduction of HTML5, you can
  now place videos directly into the page itself.

  This makes it possible to have videos play on pa...'
---

Before HTML5, in order to have a video play on a webpage, you would need to use a plugin like Adobe Flash Player. With the introduction of HTML5, you can now place videos directly into the page itself.

This makes it possible to have videos play on pages that are designed for mobile devices, as plugins like Adobe Flash Player don't work on Android or iOS.

The HTML `<video>` element is used to embed video in web documents. It may contain one or more video sources, represented using the `src` attribute or the [source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) element.

To embed a video file, just add this code snippet and change the `src` to the path of your video file:

```html
<video controls>
  <source src="tutorial.ogg" type="video /ogg">
  <source src="tutorial.mp4" type="video /mpeg">
  Your browser does not support the video element. Kindly update it to latest version.
</video >
```

The `<video>` element is supported by all modern browsers. However, not all browsers support the same video file format.  MP4 files are the most widely accepted format, and other formats like WebM and Ogg are supported in Chrome, Firefox, and Opera.

To ensure your video plays in most browsers, it's best practice to encode them into both Ogg and MP4 formats, and include both in the `<video>` element like in the example above. Browsers will use the first recognized format.

If for some reason the browser doesn't recognize any of the formats, the text "Your browser does not support the video element. Kindly update it to latest version" will be displayed instead.

You also might have noticed `controls` in the `<video>` tag. This element includes a lot of useful attributes to customize the playback experience.

## `<video>` attributes

### `controls`

The `controls` attribute handles whether controls such as the play/pause button or volume slider appear. 

This is a boolean attribute, meaning it can be set to either true or false. To set it to true, simply add it to the `<video>` tag. If it's not present in the tag then it will be set to false and the controls won't appear.

#### `autoplay`

"autoplay" can be set to either true or false. You set it to true by adding it into the tag, if it is not present in the tag it is set to false. If set to true, the video will begin playing as soon as enough of the video has buffered for it to be able to play. Many people find autoplaying videos as disruptive or annoying. So use this feature sparingly. Also note, that some mobile browsers, such as Safari for iOS, ignore this attribute.

This is another boolean attribute. By including `autoplay` in the `<video>` tag, the embedded video will begin playing as soon as enough of it has buffered.

```html
<video autoplay>
  <source src="video.mp4" type="video/mp4">
</video>

```

Keep in mind that many people find autoplaying videos disruptive or annoying, so use this feature sparingly. Also note that some mobile browsers like Safari for iOS ignore this attribute entirely.

#### `poster`

The `poster` attribute is the image that shows on the video until the user clicks to play it.

```html
<video poster="poster.png">
  <source src="video.mp4" type="video/mp4">
</video>
```

### Videos can be expensive

While it's easier than ever to include videos on your page, it's often better to upload your videos to a service like YouTube, Vimeo, or Wistia and embed their code instead. This is because serving videos can be expensive, both for you in terms of server costs and for your viewers if they have limited data plans.

Hosting your own video files can also lead to problems with bandwith, which could mean stuttering of slow loading videos. On top of that, browsers tend to vary in quality when it comes to video playback, so it's hard to control exactly what your viewers will see. It's also very easy to download videos embedded with the `<video>` tag, so if you're concerned with piracy you might want to look into other options.

And with that, go forth and embed videos to your heart's content. Or not – it's your call.

