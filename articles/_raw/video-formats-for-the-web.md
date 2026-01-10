---
title: Video formats for the web, a short guide  to help you choose
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T08:45:55.000Z'
originalURL: https://freecodecamp.org/news/video-formats-for-the-web
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/photo-1440404653325-ab127d49abc1-1.jpg
tags:
- name: 'tech '
  slug: tech
- name: video
  slug: video
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anton Garcia Diaz

  Video in the web will be on the rise for long. While embedding Instagram and Youtube
  videos is simple, there are more and more situations -like many ecommerce use cases-
  demanding a custom approach to video delivery.

  When it come...'
---

By Anton Garcia Diaz

Video in the web will be on the rise for long. While embedding Instagram and Youtube videos is simple, there are more and more situations -like many ecommerce use cases- demanding a custom approach to video delivery.

When it comes to setting a video processing and delivery pipeline, the first decision to take is about the video formats to serve. Aspects like UX, support (browsers and systems), compression efficiency, or coding speed are likely to be relevant to this choice.

Based on my [experience on media optimization for web businesses](https://abraia.me/), I try to highlight here the main aspects to consider. If you are looking for a simple transcoding and optimization option using ffmpeg you may also check [this article](https://medium.com/abraia/video-transcoding-and-optimization-for-web-with-ffmpeg-made-easy-511635214df0).

## Containers and codecs

In contrast to usual [image formats](https://www.freecodecamp.org/news/best-image-format-for-web-in-2019-jpeg-webp-heic-avif-41ba0c1b2789/), it is really important to be aware of the difference between container and coding standard. The file extension tells us which container, but not which codec is being used. And the standard followed to encode the clip will determine if it is supported by the browser or the system.

For instance, while the universally supported video format for web uses a mp4 container and the H264 standard for encoding, not every mp4 file is universally supported since it may be coded under a different standard, like H265.

It even gets a bit more complex with adaptive bit rate (ABR), which brings the best way to be responsive to the network and device capabilities of the user.

Let’s see the main combinations of containers  and coding and delivering standards and the differences between them in terms of support, compression efficiency, encoding speed, and user experience.

## Progressive video

### H264/AVC

The king format for video features a mp4 container with H264/AVC encoding. Sometimes you’ll find it in a m4v container (default format in Handbrake), an mp4 derivative developed by Apple for H264 videos with DRM protection.

Every browsers and systems -also native applications in both iOS and Android- support this format. It is the safe choice to avoid compatibility issues.

Moreover, almost any device from desktop to mobile, features support for hardware acceleration for H264. It’s fast to encode and decode.

In sum, encoding and delivering this format is really easy. Like for images, you can simply insert the link to the video using HTML5 and it will work with any browser out there.

The problems may appear for resolutions over VGA, good visual quality -bitrates about 2000 kbps and over- and a duration over several seconds. When viewed through a mobile network -in many regions also in home connections during peak hours- it may suffer stalls and rebufering. The alternative of reducing the quality will produce artifacts like blur, mosquito, or blockiness.

### H265/HEVC

Using the same container and H265/HEVC encoding we find a powerful video format that yield much higher compression efficiency ([about 50% lighter](https://www.bbc.co.uk/rd/blog/2016-01-h-dot-265-slash-hevc-vs-h-dot-264-slash-avc-50-percent-bit-rate-savings-verified)) and much less risk of artifacts other than blur. The problem of this format is that support is limited to Apple devices, which include the hefty royalties in their price. Almost only Safari and iOS apps will be able to use it. If you have many iPhone or Mac users you can include it with a fallback to H264. The experience for them will be better.

Even with hardware acceleration -available almost only in Apple devices- the higher complexity of this format means that encoding is significantly slower, so producing the variants for delivery takes more computing and more time.

### VP9

This is the open source royalty free reply from Google. Instead of mp4 it uses webm containers, basically a mkv container but setting the coding standard to VP8 or VP9. In [brings similar benefits to H265](https://medium.com/netflix-techblog/a-large-scale-comparison-of-x264-x265-and-libvpx-a-sneak-peek-2e81e88f8b0f), perhaps a bit less efficient but still much more compared to H264. Again, it allows to reduce the weight with much less risk of artifacts other than blur. The encoding speed is similar to H265, which is slow. The encoding speed may be something to bear in mind, specially in an inhouse transcoding pipeline.

Notice that while a previous version (VP8) exists with same support, we don't recommend it at all, since it does not add any benefits to H264, which is already universally supported. The use of webm is only justified with VP9 encoding.

Of course, support for webm is limited to Google world. That means Chrome and Android. Again, we’ll need a fallback to H264.

### AV1

A first stable version of this standard was released in march 2018, with mappings for both MP4 and MKV containers. It delivers similar or slightly higher gains in compression efficiency compared to H265, while being license free. The [last implementations have also improved the decoding speed compared to H265](https://www.bbc.co.uk/rd/blog/2019-05-av1-codec-streaming-processing-hevc-vvc), making AV1 videos a compelling alternative for web delivery.

The partners involved in the Alliance for Open Media that created the format make the case for widespread support in the near future. It promises sweeping all the other formats out there.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/imaxe.png)
_Partners of the Alliance for Open Media behind AV1_

However, the implementation currently available should be still considered experimental and its bottleneck is still encoding speed. The lack of hardware acceleration for this operation is clearly an issue, with the first solutions expected for the end of the year.

### VVC

The comittee responsible for H264 AVC and H265 HEVC has fast tracked a new standard, with a release expected for 2020. Preliminary tests on the approaches currently considered have shown remarkable gains compared to H265 and AV1.  I include it here as a futuristic notice, just to show that the video coding race seems far from over.

## Adaptive bitrate (ABR)

This is a very interesting alternative to any progressive format. It builds upon a HTTP-based media streaming communications protocol. In this approach videos are delivered as a master playlist. The playlist offers a representation or ladder, with different options of resolution and bitrate that cater to different viewport sizes, network bandwidths, and device capabilities.

Moreover, videos are split into pieces or _chunks_ so that the client may jump from one quality level to other. It is able to adapt to the conditions of the user, namely to the network speed but also to the viewport size -like switching to full screen-.

ABR brings a big advantage to optimize UX for mobile devices, avoiding stalls or re-buffering events under mobile networks. If you seek a true responsive behavior, this is clearly the approach to take. There are two main standards, HLS and MPEG-DASH.

Although there is an extended belief that ABR only makes sense for quite long videos, in my experience many situations with fairly short clips can also benefit from this approach.

### HLS

Developed by Apple, this ABR protocol relies on different renditions split in chunks in mp4 format. Originally with H264, it also supports H265 now. However, as a compromise we would recommend to stick to the H264 encoding with HLS since it brings much better compatibility across a variety of client cases.

A big point of this standard is support in recent Apple devices. For clients other than Safari or native iOS applications, you’ll need a viewer. But this is not a big problem since good open source options like videojs are available out there. Or course, you’ll need some effort to customise it and put it to work in your front-end. There are also great transcoding and delivery services doing all this work for you.

Since each rendition should be encoded at constant bitrate, I recommend combining HLS with per title encoding. That is, selecting the rendition bitrate based on the content of the video.

### MPEG-DASH

This is a codec-agnostic protocol for ABR, so it is capable to also work with VP9 encoding besides H264 and H265, or even new alternatives like AV1. The downside is its relative youth, which means enjoying much less support than HLS. This is why we don’t recommend it yet for most web businesses -even large ecommerce stores-.

## Summary

After years of predominance of H264 AVC compression, new approaches are animating the scene. The race on display sizes and resolutions is fueling the development of new formats capable to deliver greater content within the same bandwidth.

VP9 in webm provides a significant gain in compression eficiency (about 30%), is royalty free and is supported by Google solutions (Chrome, Android). Going much further, H265/HEVC has achieved a comparable or better subjective quality at half the bit rate compared to H264. Since none of them features universal support, H264 will be still needed, at least as a fallback.

Adaptive bit rate is a compelling alternative, providing unbeatable user experience. In this regard,  HLS enjoys a wide support with the help of open source viewers.  It is possibly the best option for a medium sized web. The complexity added by the need of a viewer is fairly mitigated by the availability of open source initiatives like videojs for inhouse solutions, but also of third party services to do the job at competitive prices. If you go through this last route, make sure to ask for [per-title encoding](https://abraia.me/docs/video-optimization/#per-title-encoding).




