---
title: A Basic Intro to Image Optimization for the Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-30T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/image-optimization
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/image-breakpoints-2.png
tags:
- name: 'image optimization '
  slug: image-optimization
- name: Web Development
  slug: web-development
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'By Anton Garcia Diaz

  Images are an essential ingredient of most websites. The visual quality of pictures
  has a direct impact on the brand image and the message those images convey. And
  the weight of images usually accounts for a 40-60% of the data tr...'
---

By Anton Garcia Diaz

Images are an essential ingredient of most websites. The visual quality of pictures has a direct impact on the brand image and the message those images convey. And the weight of images usually accounts for a 40-60% of the data transferred on the web. 

This usually has the largest impact on loading time over other resources like JavaScript. So, whether we're creating or running a website, we should put in place an image transformation and optimization pipeline.

There are many options to do this, from in-house developments based on open source libraries and suites – like ImageMagick – to cloud-based tools and APIs. 

Whatever tool we use in our deployment, there are four main tasks that, at the very least, any pipeline should accomplish.

### Resize images. 

Image resizing is the first and most important step. It brings a big impact on weight with no visual quality penalty, as long as we don't make it smaller than the displaying resolution. 

We should always set and enforce a maximum image resolution in our website, for instance 2000 px width. Ideally, we'd make our website responsive by setting different breakpoints and delivering images that fit in our users' displays. 

If you need help on choosing your breakpoints, check out this article on the [best image sizes for web](https://abraia.me/docs/best-image-sizes-for-web/).

### Convert to the right format. 

JPEG is the default format in the web. PNG may work better with graphic designs featuring solid colors, but in these cases it may yield lower weight with better quality. 

You may consider offering WEBP for Chrome, Edge, Firefox and Android users, keeping JPEG as fallback for Safari and iOS. It may save 10-30% of image weight with very similar quality, perhaps some more blur and less ringing. 

For an up to date revision you may check out this article on [image formats for web](https://abraia.me/docs/best-image-formats-for-web/).

### Compress images properly. 

We can do this with a powerful open source suite like [ImageMagick](https://imagemagick.org/index.php) and simply set a quality factor (typically 75 to 85) for JPEG (and WEBP) images. You can still use a perceptual metric to better protect quality and further squeeze weight – this is an option available in some cloud [image optimization tools](https://abraia.me/docs/image-optimization/#automatic-image-optimization-for-web).

### Get rid of metadata. 

From shooting to editing, images accumulate metadata, like [exif data](https://abraia.me/docs/exif-data-orientation/). While they may be useful for editing and management purposes, they have no impact on how images show in our web. Their weight can easily get 20 KB or more per image. 

We should get rid of metadata before publishing on the web. We only have to make sure that images are coded with the proper orientation and with a sRGB profile, adhering to good [color management](https://abraia.me/docs/color-management-for-web/) practices.

