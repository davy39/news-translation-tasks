---
title: Don’t ruin your &lt;img&gt;
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-09T12:40:54.000Z'
originalURL: https://freecodecamp.org/news/you-need-to-stop-making-these-6-mistakes-with-your-img-s-e242c02d14be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fXZTuZFmYlUNbu1OLfHm3w.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anthony Ng

  As developers and designers, it’s our duty to ensure the best user experience possible.
  And you know what one huge part of that experience is? Images.

  But many of us are too busy to give images much thought beyond adding a src property
  ...'
---

By Anthony Ng

As developers and designers, it’s our duty to ensure the best user experience possible. And you know what one huge part of that experience is? Images.

But many of us are too busy to give images much thought beyond adding a **src** property and some pixel dimensions.

This guide will show you some common problems with image usage, and how to fix them.

I also built a [website](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/) with live examples to illustrate all of these issues. Do some hard refreshes, resize your browser, and you’ll quickly see what I mean. ?

Oh, and you can find all of the source code here on [Github](https://github.com/newyork-anthonyng/tutorials/tree/master/Responsive_Responsible_Images).

Let’s get started.

### Cut images down to size

When you visit a website, an HTML page is sent to your browser. The browser then has to download any assets that the HTML page includes. Your browser has to load any JavaScript files, stylesheets — and of course, images — that the page uses. Each of these assets takes time to load. The larger the file, the longer it will take.

We minify our JavaScript files to remove unnecessary bloat and get a smaller file size. We should do the same with our images.

One way to get rid of image “bloat” is to make sure dimensions are reasonable. There’s no reason to leave images any larger than they need to be.

If the maximum width of an image on your website is going to be 960px, then there’s no need to use an image file that’s 1800px wide. The load time of your website will suffer. Especially on slower connections. And you’re forcing your user to download more bytes than they need.

When you know the dimensions of your images, use a program that can resize photos to the size you need them to be. I usually use [Sketch](https://www.sketchapp.com/) or [Affinity Designer](https://affinity.serif.com/en-us/).

In our example [here](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/image_dimension.html), the images both have a width of 960px. However, the original photo has a width of 5183px. There’s no use having an image with such large dimensions if we’re not going to use it.

After reducing the photo dimensions to have a width of 960px, we see a 90% reduction in file size, with a 6 second improvement in load time over a wifi connection.

![Image](https://cdn-media-1.freecodecamp.org/images/M-ZjRnIZizP4GvCJCfNPc1fLEhb8kLhOU6wM)
_Original image vs. Resized image_

And, of course, load times vary depending on your network speed.

If we use the Chrome Developer tool to throttle the connection to a regular 4G connection, we see a whopping 16 second improvement in load time.

![Image](https://cdn-media-1.freecodecamp.org/images/BUX-ZX0BHIz92mI78q4PfQrJvHD3wMdrzYAU)
_Original image vs. Resized image over 4G_

### Use compression

Reducing the dimensions of our image is a great start to reducing the overall file size, but we can do more. We can compress our image to further reduce the image file size, with little (if any) reduction of image quality.

Compression removes unnecessary junk from our image, such as metadata, embedded thumbnails, comments and unnecessary color profiles.

I use an application called ImageOptim to compress my images. To use it, all you need to do is drag your images into the application and…that’s it. The new compressed image will replace your old one. If you want to automate image compression, you can use a task runner, such as Grunt, to minify your images when building your project.

In our example [here](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/image_compression.html), we see a 13% reduction in file size after compression, with a 100 millisecond (12%) improvement in load time over a wifi connection.

100 milliseconds may seem small, but these savings make a difference when you have multiple images on the same page trying to battle through a weak 3G network onto an iPhone.

![Image](https://cdn-media-1.freecodecamp.org/images/oq50cJJ2RND9ObD59o4tA7Wlu8MNnEUT1183)
_Uncompress image vs. Compressed image_

### Use media queries to make images responsive

Now we have a slimmed down image file that will quickly load on your HTML page. The user experience is definitely better, but our job isn’t finished yet. We have to make sure the image looks good on displays of all sizes. It has to be responsive.

There are websites where the image doesn’t completely fit into the display. You have to scroll left and right — or even zoom out — in order to view the entire photo. This isn’t the best user experience.

Let’s use media queries to style our images when the display is a certain size. On smaller displays, we’ll use “max-width: 100%” to style our images.

In our example [here](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/responsive.html), whenever we resize the page, we can see that our responsive image will always fit entirely inside the display. The user doesn’t have to scroll or zoom to view the full image.

### Ask an art director

Our user experience is definitely improving. Our image is light and responsive. However, this scaled down image might not be exactly what we want on our website.

For example, our website might be about the Empire State Building. When the image is 960px, the Empire State Building stands majestically in the center of the skyline, recognizable at a glance. But once we resize our browser to be 360px wide, it loses some of its pizzazz. In this instance, a scaled down image isn’t what we want.

By making our image responsive, we avoid the issue of users scrolling and zooming out to view our image. But we’re replacing that problem with a new one. Users now have to zoom into the image, only to see a pixelated Empire State Building. This isn’t the best user experience.

In situations like this, our image needs to be changed more drastically. You might want to crop the image or change the image altogether. Doing this is referred to as “art direction.”

To use different images, we can use the <picture> and <source> HTML tags. This tells the browser which image to request and use based on a media query.

In our [example](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/art_direction.html), we’ll be using different images based on the size of our display. Now when you resize the website, you should be able to see the Empire State Building in all of its glory.

### Use service workers to cash in on caching

Responsive Web Design is a relatively new concept. We should design our websites to look good, no matter what display they’re on. Now there’s a new trend for websites to feel more like Native Apps. Among other things, this means that our websites should function even without an internet connection.

What does this mean for our images? For images that are static and won’t be getting updated often (such as logos), we should cache them. When caching assets, these assets are saved to the client browser.

When caching assets, these assets are saved to the client browser. The benefit of this is that when the user visits our websites in the future, it will first look for any assets in our cache before requesting from the server. Our image will load even faster, because retrieving from the cache is usually faster than making an HTTP request. Another benefit is that we can even access our image even without internet connection!

Let’s use service workers to cache our assets. Service workers are a powerful new technology that acts as a middleware between your browser and the internet. This allows us to have fully functioning webpages offline!

In our [example](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/offline.html), if you turn your internet off and refresh the page, you will see our website still functioning as it used to.

![Image](https://cdn-media-1.freecodecamp.org/images/JewcFUneXtwOMRa6i-9zUdAef4-w1MJYhtW8)
_Notice our jpeg is being fetched from the ServiceWorker_

### An accessible image is a friendly image

When using the <img> HTML tag, keep in min**d t**he alt property.

Many people with visual impairments use tools called screen readers that read all the contents of a webpage out loud to them. They will read the alt property of any images they encounters, and skip over any images that don’t have an alt property. So alt properties are crucial for these people to understand images.

By the way, every image should have an alt property, but if the image is purely for decoration (or clearly explained above), you can leave it blank.

This way, our images can be understood by everyone — even people who can’t see them.

That’s all! Have any tips for better using images? Leave a comment below!

Want to learn more about Service Workers? Check out this [introduction](https://developers.google.com/web/fundamentals/primers/service-worker/) on Google’s developer page.

Want to learn more about creating better user experiences through faster websites? Check out this [book](http://designingforperformance.com/).

