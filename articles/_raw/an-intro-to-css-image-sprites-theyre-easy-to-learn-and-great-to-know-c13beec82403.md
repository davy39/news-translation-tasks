---
title: 'An intro to CSS Image Sprites: they’re easy to learn and great to know'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T19:22:07.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-css-image-sprites-theyre-easy-to-learn-and-great-to-know-c13beec82403
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pc6EbbKjoFzSbVCMiA8OOQ.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Zlatan Bekric

  Image sprites have been here since the 1970s. They were used for the first computer
  animations on Atari and other consoles. As time went on they were used less and
  less by front-end developers who wanted more advanced (read: realisti...'
---

By Zlatan Bekric

Image sprites have been here since the 1970s. They were used for the first computer animations on Atari and other consoles. As time went on they were used less and less by front-end developers who wanted more advanced (read: realistic) graphics for 3D and virtual reality.

In recent years, however, they’ve made a comeback.

_Sprite is a computer graphics term for a two-dimensional bitmap that is integrated into a larger scene._

In the last few years, Facebook, Twitter, Instagram, and many other social media platforms grew like crazy. With growth came their need to optimize wherever possible and shrink the size of server requests. That’s when CSS image sprites went back into the mainstream.

For a platform like Facebook — which has more than 1 billion users — showing icons, images, and similar content requires multiple server requests. The requests unnecessarily overload the traffic.

### So what do you do to reduce server requests and bandwidth? Turn to CSS image sprites.

Instead of making a request for your profile image, your friend’s profile image, your album thumbnails, etc, sprites allow you to use one image, which means only one request. You can manipulate that image to show those images as portions of one larger image.

Let’s see an example involving flags :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pc6EbbKjoFzSbVCMiA8OOQ.png)
_Original image_

Now let’s see how it works:

As you can see in the code above, we have set up the base that consists of three divs, where each div will be a sprite carrier.

Firstly we picked the div with the ID of first. Our div will have a size of height and width that will be shown on our page. As the background, we will load in an image with **URL (“https://i.postimg.cc/R0N7nkH9/flags.png")**.

The next thing is to scale down/up our background image with **background-size:1400px .** (We can use actual pixel size, percentage, em or rem.) This parameter will allow us to “zoom in” an image until the point where only a certain part of the image will show.

Lastly, the two params that come after the **background:**

**URL(“https://i.postimg.cc/R0N7nkH9/flags.png"),** will move the portion of the main image, that is going to be visible along X and Y axis. Which means that in this case **background:**

**URL(“https://i.postimg.cc/R0N7nkH9/flags.png") -86px -87px;** we will be showing the part that is offset from the top of the image by 87 pixels from the top and 86 pixels from the left.

The first number (**-86px**) stands for X-axis where negative means moving from left to right and positive stands for going from the right to left. The second numbers **(-87px)** are used to offset from top to a bottom, where inverted rules apply, a positive number means going from the bottom to top, and negative of course going from top to bottom.

As you can see on the original image, the flag that we got (Bosnia) is indeed second from the top and second from the left.

Good enough? OK let’s continue.

Now let’s fill up the div with an ID of second. Same rules for setup will apply and the only change will be that in this case, we will stay on the original X-axis **(0px),** and Y direction will go from the bottom part towards the top **(89px).** Again if you check original image, you may see that (Uzbekistan) is first from the bottom, and first from the left.

And last, but not least…

Yes, lastly we are filling up the last div with an ID of third. Rules are the same, and if you guessed that we moved from the bottom toward the top, well that’s true.

Now the moment of truth ….

In the case above, we were moving along the X and Y axis to show certain portions of the image with flags. Going right to left and down we got Bosnia (X-axis), going from a bottom and left (Y-axis) we got Thailand and Uzbekistan. As you’ve seen we are using only one image, and that means only one request for an image.

It is important to know that when you are building the sprites, that base image should have the same portions of images within it, for your own convenience. Like in this case where we are moving towards left and right, top and bottom, by the size of the portion plus white space. Uzbekistan (89px) and Thailand(178px) have a difference of 89px which is their actual size (87px) plus white space (1px + 1px).

### Yep, you can make animations too.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hnEOIUREyM1xmpIxNntrcg.png)
_Original Image_

In order to make this style of sweet, cool old school animations, we only need CSS animation properties. In this case, we were moving the original image along the X-axis, and we get this old style animation. Believe me with sprites, there are no limits.

It’s as easy as that :)

I hope that you have enjoyed reading this article.

Stay tuned for more …

![Image](https://cdn-media-1.freecodecamp.org/images/1*tEK16gxQMCiapg2WWIz2Uw.png)

