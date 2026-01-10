---
title: What is AVIF? How to Use AV1 Image Format Images on Your Website
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T18:14:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-avif-images-on-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/how-to-start-using-images-on-your-webistes-1.png
tags:
- name: 'image optimization '
  slug: image-optimization
seo_title: null
seo_desc: 'By Erisan Olasheni

  The AV1 Image format, or AVIF, is the latest image codec on earth. AVIF is an optimized
  image format which was created to make our images smaller while keeping the same
  quality (lossless). The file extension for AVIF is .avif.

  In t...'
---

By Erisan Olasheni

The AV1 Image format, or AVIF, is the latest image codec on earth. AVIF is an optimized image format which was created to make our images smaller while keeping the same quality (lossless). The file extension for AVIF is `.avif`.

In this article, I want to talk about its features and benefits, and why you should start using AVIF. I will also show you the safe way to include AVIF images on your website. 

## What is AVIF and How Does it Work?

AVIF is an extraction from the keyframes of the now popular video format [AV1](https://en.wikipedia.org/wiki/AV1) developed by [Alliance for Open Media (AOM)](http://aomedia.org/). 

AOM developed AVIF with the goal of providing royalty-free images with better compression efficiency and more feature support compared to the existing image formats. 

AVIF now has backers from big companies like Google, Netflix, and Apple. 


## Why is AVIF Better?

Following its predecessors (**WebP**, **JPEG-XR**, **JPEG2000**, and **PNG**, **GIF**) AVIF is compatible with high-dynamic-range imaging. It supports **10-** and **12-bit** color at full resolution, resulting in images that are up to 10 times smaller than other known formats. 

AVIF is a good choice for web developers because:

*   It is royalty-free, so you can use it for free without worrying about licensing.
*   It is currently backed by many big players in tech like Google, Amazon, Netflix, Microsoft, and more.
*   It has the most optimal compression.
*   It has more modern features packed in like transparency, HDR, wide colour gamut, and more.


## How to Start Using AVIF Images

Now we get to the fun section of this tutorial. There are two major ways you can start using AVIF images:

1. One is by converting your old images to AVIF.
2. The other is by creating AVIF images using AVIF-supported image editors.


### How to convert your old images to AVIF

Because AVIF is still in its infancy, the easiest way to create images in AVIF format is to convert your old formats. 

This can be done simply online, as there are many online AVIF image converters. The [AVIF online converter](https://avif-converter.online/) is my choice because it is simpler and seems the to be the fastest available online converter. 

Just follow these steps to convert your images to AVIF:

1. Visit [the website](https://avif-converter.online/).
2. Upload your old images (can be **PNG**, **JPEG**, **GIF **and others).
3. Wait while the website processes the conversion.
4. Save your new AVIF files.


### How to create AVIF images using AVIF-supported image editors

Image editors are adding support for AVIF image creation. These editors now fully support AVIF images:


*   Microsoft Paint – starting from the ["19H1" updates](https://www.howto-connect.com/windows-10-1903-version-support-avif-file-type/), you can now draw images on Microsoft Paint as “save as” AVIF.
*   GIMP for Windows and Linux now has AVIF support starting [from the 2.10.22 update](https://www.ghacks.net/2020/10/09/gimp-2-10-22-update-introduces-support-avif-and-heic-support/).
*   Photoshop developers are also [talking about how to support AVIF](https://feedback.photoshop.com/conversations/photoshop/when-will-avif-support-be-added-to-photoshop/5f5f46314b561a3d4278baf4). Hopefully this will soon be supported.


## How to Use AVIF on Your Website

AVIF is still a relatively new technology. But most modern browsers now support the format which means you can use it directly in the `<img>` tag. Just keep in mind that not all browsers fully support the format yet. 

The best way to go about using AVIF is with **content negotiation.** We will be using the HTML 5 `<picture>` and the `<source>` which supports content negotiation.

![Group-9how-to-use-avif-html--1-](https://www.freecodecamp.org/news/content/images/2020/11/Group-9how-to-use-avif-html--1-.png)

You can play around with [the live example here](https://lyty.dev/diy/how-to-use-avif-on-website.html).


### Which browsers support AVIF

*   The first browser to fully support AVIF is [Chrome 85](https://developers.google.com/web/updates/2020/08/nic85#more). 
*   Microsoft [Windows 10 ](https://www.howto-connect.com/windows-10-1903-version-support-avif-file-type/) also added support in the "19H1" updates.
*   Mozilla is still working on the support for the image format in Firefox.[155].


## Wrapping Up
AVIF is a game changer that will soon become the world's defacto image format. Because of its potential features, it is likely that it will soon gain full support on all platforms. 

Unlike Google's **WebP** image, which took Apple a whole of 10 years to support, AVIF has quickly attracted Apple's interest to the extent that they now contribute to the project. 

Are you ready to start using AVIF on your websites? 


