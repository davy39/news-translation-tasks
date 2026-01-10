---
title: 'HLS Video Streaming: What it is, and When to Use it'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-18T22:59:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-hls-and-when-to-use-it
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/HLS-video.jpg
tags:
- name: Adaptive Bitrate
  slug: adaptive-bitrate
- name: hls
  slug: hls
- name: media
  slug: media
- name: video
  slug: video
- name: Video.js
  slug: videojs
- name: VideoJS
  slug: videojs
seo_title: null
seo_desc: 'By Anton Garcia Diaz

  In this short article I will focus on HLS, the most extended adaptive bitrate protocol
  for video delivery. I''ll answer some of the main questions that anyone considering
  HLS for the first time will likely ask: what it is, when to...'
---

By Anton Garcia Diaz

In this short article I will focus on HLS, the most extended adaptive bitrate protocol for video delivery. I'll answer some of the main questions that anyone considering HLS for the first time will likely ask: what it is, when to use it, and how to use it. 

To help along the way, I will show some examples using [an online video publishing tool](https://abraia.me/video/) that you can freely use to test out the performance of HLS on your own.

## What is HLS and how does it work?

HLS is a protocol defined by Apple to implement an adaptive bitrate streaming format that can be supported on their devices and software. Over the time, it has gained widespread support. 

The most important feature of HLS is its ability to adapt the bitrate of the video to the actual speed of the connection. This optimizes the quality of the experience. 

HLS videos are encoded in different renditions at different resolutions and bitrates. This is usually referred to as the bitrate ladder. When a connection gets slower, the protocol automatically adjusts the requested bitrate to the bandwidth available. 

Compared to progressive videos, HLS avoids re-buffering and stalling effects as well as bloating the client connection. We can see it at work in this video.

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/HLS-video/HLS_video-at-work/index.html]

In essence, HLS provides a much better user experience when we use video content in our apps or sites.

It has native support in iOS and Android. It is also supported by Safari, and by using some JavaScript it is supported in all the main browsers (Chrome, Firefox, Edge). While using HLS requires some effort, it's not a big deal. 

Let's see when we should use it and how.

## When should we use HLS?

There are cases where videos are not that heavy. For instance, you could have a sequence of images encoded as a 1-2 seconds video, with a weight of less than 1 MB. In this case, a progressive video – that can be consumed, like an image, using plain HTML5 – is for sure the best option. HLS does not offer any advantage here.

But, HLS does make sense when we want to deliver high resolution videos (HD or over) with a weight over 3MB. This type of content may kill our web UX when viewed on an average mobile connection. 

It's worth noting that this is the case in an increasing amount of media content, including many short videos of less than 20 seconds used in ecommerce and marketing contexts. In the example at the beginning of the post, we have a full HD video of only 9 seconds that weights in at over 6MB.

## How can we use HLS in our sites?

To use HLS we have to address a number of aspects. I'll focus on two important points:  

* the need to encode the video, and, 
* the need to embed it in our page. 

For a more comprehensive view on what a general video publishing pipeline entails, you may check out [this post](https://www.freecodecamp.org/news/short-videos-in-web-and-ecommerce-workflows/).

### HLS encoding

We can encode videos in HLS in-house or by using a third party service. To build an in-house encoder, the best option is to use FFMPEG, a powerful open source library for video processing and encoding. In this case, we should analyse the content we are going to encode and set a number of parameters. 

In HLS we should define a bitrate ladder (the bitrates and resolutions of each step) and the length of chunks. When we encode a video, we end with a set of playlists and chunks. Typically, we end the former with .m3u8 and the latter with .ts extensions. We can see an example in the next image.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/imaxe.png)

We can see one master playlist, one additional playlist per rendition, and all the chunks of each rendition. The master playlist specifies the bitrate ladder and the relative path to each rendition.

Apple makes a generic recommendation specifying the bitrate ladder and a chunk duration of 10 seconds.  However, this is not very useful for many types of content, like the short videos common in ecommerce and marketing. 

In fact, the best approach is to tune the bitrate ladder specifically to the content of the video. In this case, if you want to make the most of HLS and you're not expert in encoding, a third party service providing per-title encoding (with HLS) is likely the right choice.

## HLS players

Here, we find two main options. We can stick to the HTML5 player or we can use one implemented in JavaScript.

### HTML5 player 

Recent Safari versions support HLS. In this case, you may use HLS playlists in the same manner as progressive videos. With other browsers, you may use a tiny JavaScript library to implement the HLS protocol and again use the HTML5 player for progressive videos. 

This can be done with HLS.js. This library just implements the negotiation of renditions, based on the available bandwidth. Support is almost universal, only conditional on the support of the media element's API.

### JavaScript Player

In case we need to customise the video experience – which is pretty common in marketing and stories pages – then we need to use something other than the default HTML5 player. 

While there are many commercial options out there, Video.js is a good choice. It's an open source player that supports a high degree of customization, including different skins and controls. 

A player like Video.js also supports the tracking of video-related events (like play or pause actions) so we can include them in our own analytics. In fact, including these data in our Google Analytics is really easy.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/imaxe-2.png)
_GA data for events tracked in a video viewed with a Video.js player_

## Summary

I've tackled the first questions about HLS that most potential users will have: what it is, and when we should use it.

While a video publishing pipeline reliant on HLS can be implemented and deployed in-house with open source tools like FFMPEG and video.js, it may be a good idea to use a [video publishing service](https://abraia.me/video/) if you're not an expert in the tech. They bring advanced features like per-title encoding, take care of all the hard work, and let us focus on our customization needs.

