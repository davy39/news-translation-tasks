---
title: How to deploy a complete video publishing pipeline for web and ecommerce
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-13T08:00:00.000Z'
originalURL: https://freecodecamp.org/news/short-videos-in-web-and-ecommerce-workflows
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Video-Publishing-Demo.png
tags:
- name: ecommerce
  slug: ecommerce
- name: hls
  slug: hls
- name: publishing
  slug: publishing
- name: technology
  slug: technology
- name: ' #Transcoding '
  slug: transcoding
- name: video
  slug: video
- name: Video.js
  slug: videojs
- name: VideoJS
  slug: videojs
seo_title: null
seo_desc: 'By Anton Garcia Diaz

  From ffmpeg and cloud video transcoding to HLS, delivery, players, Video.js, and
  analytics.

  After the conquest of social networks, video is spreading through web businesses.
  As a media consultant working for several of the larges...'
---

By Anton Garcia Diaz

_From ffmpeg and cloud video transcoding to HLS, delivery, players, Video.js, and analytics._

After the conquest of social networks, video is spreading through web businesses. As a media consultant working for several of the [largest fashion ecommerce sites](https://www.similarweb.com/top-websites/category/lifestyle/fashion-and-apparel) in the world, I feel safe saying the video-everywhere trend is all but unstoppable.  

In this post, I review the main aspects to consider when publishing short-format videos in a web workflow. I comment about open source resources that make an in-house solution possible for each step, like ffmpeg or Video.js. Besides, I use an example with [Abraia's video optimization and publishing demo](https://abraia.me/video/) - specially tailored to short videos for fashion ecommerce. 

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Short-Video-Publishing-Demo/Workflow/index.html]

It gives full access to the resources created: chunks, playlists, and html code for the video player. This brings quick insights on the inner workings of a complete pipeline. 

The content should be helpful either to pursue an in-house processing and publishing pipeline or to sort out the best combination of services. 

## Quality of experience (QoE) and other business related concerns.

There are two main concerns that are closely linked. The fear of bloating the bandwidth of users, which damages UX and engagement, and the fear of delivering poor visual quality, which potentially damages brand image. 

The balance between these two antagonising factors is what determines the QoE. Keeping a **high QoE** requires delivering nearly the **best possible quality, without rebuffering or stalling** effects or noticeable drops of page speed.  

Of course, there are other issues that matter

* the customisation of the viewing experience to match the branding of the business
* the cost increase of delivering higher bandwidth content 
* and the additional burden in terms of devops

...just to name a few.

## A first choice: progressive vs adaptive bitrate (ABR).

Regarding [video format selection](https://www.freecodecamp.org/news/video-formats-for-the-web/), there are two main options with important implications: progressive video and ABR.

Progressive videos may be delivered and consumed like images, using plain HTML5 code. Moreover, progressive mp4 videos with H264 encoding have universal support across browsers and systems. So, they're the straightforward approach.

However, in the likely event that QoE is a main concern we should go for ABR. More specifically for HLS -again with H264 encoding – which is a broadly supported option. 

With **HLS** we'll be able, in most cases, to keep the **bits per second - the bitrate - of the video within the connection capacity limits**. This avoids rebuffering, stalling, or blocking other content. In HLS, the video is available at different bitrates and is split in pieces. This allows the client to request the best quality affordable, based on the network speed at any time. The only caveat is that we'll need to use a player in our front-end (basically a piece of JavaScript). In apps, it's easier because both iOS and Android feature native support for the protocol. 

## The pipeline and the workflow

That said, let's see what a video optimization and delivery pipeline for web entails. The pipeline is supposed to process a master or pristine video with a high quality and make it suited to the web. It's also supposed to meet brand requirements on visualization, and to integrate the video events in the analytics of the site. 

In sum, our pipeline should address the following problems:

* Content management
* Transcoding and optimization
* Delivery
* Visualization
* Analytics

In the end, the pipeline should allow a workflow similar to that of social video platforms - where you upload a video and get a [link like this](https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Short-Video-Publishing-Demo/Video-Freecodecamp/index.html) to embed or share elsewhere - but under all the custom requirements of our business.

To keep this post short and focused, I'll skip the content management issue, which is basically the way we handle all the resources, including the collaborative media editing and approval workflows. Next, I go through the main optimization and delivery ingredients found in a video publishing pipeline.

## Transcoding and optimization

For progressive videos to be responsive, we can create versions with different resolution and quality to be consumed based on breakpoints, similar to images. 

In an in-house scheme this operation can be [easily accomplished with ffmpeg](https://medium.com/abraia/video-transcoding-and-optimization-for-web-with-ffmpeg-made-easy-511635214df0). It's an open source tool that performs resizing, compression, and many other operations very efficiently. For instance, to scale a 4K video to fullHD with good visual quality you may simply use:

```
ffmpeg -y -i input.mp4 -vf scale=1920:-2 -c:v libx264 -crf 22 -profile:v high -pix_fmt yuv420p -color_primaries 1 -color_trc 1 -colorspace 1 -movflags +faststart -an output.mp4
```

Alternatively, with a cloud platform the operation should be a no brainer, although in many cases we loose effective control of the quality settings and possible breakpoints.

Encoding for **HLS** is a bit trickier. First, **we have to define a coding ladder**. Each step of the ladder will feature a different bitrate, from a maximum to a minimum. They set respectively the maximum and minimum quality. 

For each bitrate in the ladder, we also have to set the resolution, again from maximum to minimum. Ideally, we should use bitrates specifically tuned to the video content to optimize the use of bandwidth. When done automatically, **on a per video basis**, this is called **per title encoding**. 

We have to code the video with the resolutions and bitrates defined and then cut each rendition in chunks. We also have to decide the duration of the chunk. That is, how frequently is HLS renegotiating the quality to request, based on the current network speed. We can do all of the encoding with ffmpeg or with a cloud service.

Let's see the files generated for our example. We have a folder containing all the chunks (.ts extension), and the playlists ( .m3u8 extension). 

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-7.png)

The playlists contain all the information about the renditions available. Next, we can see the content of the master playlist: the ladder - bitrates and resolutions - and the relative route to the renditions.

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=3374012,RESOLUTION=1920x1080
1080p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1836580,RESOLUTION=1280x720
720p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1002050,RESOLUTION=856x480
480p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=649329,RESOLUTION=640x360
360p.m3u8
```

That is, for each rendition we have an additional playlist containing the information about the duration and route to the corresponding chunks. We also need a poster to use as thumbnail and get covered in the event of a very slow connection or HLS compatibility issues. In our example, all the resources are in the same folder so the route to each resource is simply the name.

## Delivery

**Videos should be delivered through a CDN**. If you make a poor transcoding, many users may suffer slow page loads. But at least if you use a CDN you won't take your site down because the server is unable to handle the load. I've seen big sites that more than doubled their peak traffic the day they decided to use videos in their home page. So videos, whether progressive or HLS, should be delivered as static files cached and delivered by a CDN.

If you are using a cloud platform for video publishing, you should be covered. Any decent one offers video delivery through at least one CDN. If you need coverage in some countries like China, you need to look into each specific platform and the CDN used, since some of them do not work there.

## Visualization

While for progressive videos HTML5 is enough to ensure visualization, in the case of HLS we need a **JavaScript player with HLS support**. 

There are many commercial options, but there are also open source alternatives with very high quality. A good example is **Video.js**. It has a wide support among browsers, only limited by the dependency on the [Media Source Extensions API](https://caniuse.com/#search=media%20source). It brings a high degree of customization using skins and a flexible configuration, for instance allowing you to use autoplay or different video controls.

The player may be inserted in the page code, or it can be in an html static that is embedded as an iframe. 

Going back to our example, when we publish the video we create an [html resource](https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Tests/PexelsVideos2795392/index.html) that has a Video.js player with default settings. The content url should point to the master playlist and the thumbnail to the poster image extracted from the video.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-3.png)

In this case, the html resource also adds **oembed compatibility**. Besides directly access in the browser this html - or a different one in which we copy/paste the player's code - to play [the video](https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Tests/PexelsVideos2795392/index.html), we can embed it in a content management system (CMS). For instance, when writing this post for freeCodeCamp.

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Short-Video-Publishing-Demo/Embedding/index.html]

## Analytics

In short videos, typical analytics of interest are the **ratio of users that play the video, the ratio of those who view it in full, or the ratio of playback failures**. 

Again, there are many commercial options available. However in many cases a widespread free option like Google Analytics (GA) may be enough. If we are using Video.js, we only have to instrument the html resource with GA, like for any other web page. Going back to our example, we can see it in the editable HTML created.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-5.png)

To track the video use in GA, we just have to track the video events in the player. For instance:

```
    player.analytics({
      defaultVideoCategory: 'Video',
      events: [{
        name: 'play',
        label: 'Video-Freecodecamp',
        action: 'play',
      }, {
        name: 'pause',
        label: 'Video-Freecodecamp',
        action: 'pause',
      }, {
        name: 'ended',
        label: 'Video-Freecodecamp',
        action: 'ended',
      }, {
        name: 'error',
        label: 'Video-Freecodecamp',
        action: 'error',
      }]
    });
```

Then, in GA we can see the events taking place. This screenshot shows my own real-time activity - with two devices and browsers - on the video example created for this post.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-4.png)

## Summary

I have reviewed the main aspects involved in a video publishing pipeline, from transcoding, to delivery, visualization, and analytics. I have made reference to potential use of different resources, including two prominent open source initiatives like ffmpeg and Video.js.

I have supported the explanation with a simple example using our [video publishing demo](https://abraia.me/video/). It gives full access to the resources created. You'll be able to download, modify, and use the resources in your tests. You can freely use it to repeat the process with a short video of your choice. 

Remember to start with a high quality video. The example here is based on a 9 seconds 4k video from [@cottonbro](https://www.pexels.com/@cottonbro). Overall, I expect the post to bring a bird's eye view of what a custom deployment for video publishing entails.

