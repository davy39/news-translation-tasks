---
title: How I built a mood changing animation using CSS masks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-02T17:02:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-mood-changing-animation-using-css-masks-565b16ed051f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tTAVggfIn612FqCu
tags:
- name: CSS
  slug: css
- name: image masking
  slug: image-masking
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ankit Karnany

  Remember the cartoons we used to watch during our childhood? At that time they were
  the epitome of animations. Nowadays, animations aren’t just limited to cartoons
  — we come across them almost everyday when we check our phone or look...'
---

By Ankit Karnany

Remember the cartoons we used to watch during our childhood? At that time they were the epitome of animations. Nowadays, animations aren’t just limited to cartoons — we come across them almost everyday when we check our phone or look at any device which has a screen.

Today, animation is used not only to attract attention but to enhance the user experience and guide user flow. In any good design, animations are added in such a way that they blend with the common flow, thus creating a seamless user experience.

So, in this article we will build a simple animation of a face with different expressions, and we’ll learn a little bit of CSS in that process.

### Getting started

We will use a CSS technique which is somewhat rare among web developers, but that designers use quite often. It is called **masking**.

So what comes to your mind when you hear “mask?”

You’re probably picturing a cover on top of something. That’s all we need to understand.

Wait — but this article is related to coding and using CSS animation…

Don’t worry! We’ll get right to it.

### Creating the basic mask

Let say we have a `<d`iv> w`ith a background:` green; and it looks something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/2XO9bGq7nwPzRnJwEVIGM18CnBW1sMXO0Hav)

Now, say I have a `face.svg`:

![Image](https://cdn-media-1.freecodecamp.org/images/rtGKXNWrhwS0GfhGmUpb228Tu137Z4FvgMkc)

If we apply a CSS property `mask-image: url(face.svg);` on the `<d`iv>, you’ll be amazed to see what we get:

![Image](https://cdn-media-1.freecodecamp.org/images/vKQ3qFzMOVQLuHbur4KZ19hm5Rn7PMfGtmoq)

You might be thinking that something is odd here. The `face.svg` was placed over the `<d`iv>, but it took up the color o`f the back`ground. This is the opposite of what you might have expected. This happens because o`f the mas`k-type property which makes the opaque part of the svg transparent. This allows the background color to be visible.

Let’s not get deeper into that now. Just keep in mind that we can use `background-color` to change the color of the mask. If you are familiar with different ways of using `background-color`, we can also use gradients and write a simple gradient which fills red in the center and radially spreads into black outwards. The code for that is the following:

```
background-image: -webkit-radial-gradient( hsla(0, 100%, 50%, .7), hsla(0, 100%, 20%, .8), hsla(0, 100%, 10%, 1));
```

Which results in this:

![Image](https://cdn-media-1.freecodecamp.org/images/aX8BzmkSrurnCCGxBX6B1FTTfk0RA35SNVxe)

### Adding the animation

Now let’s add some animation to this empty face. For this I have `expression.svg` which looks like the below image. For simplicity, I have created all the svgs with the same width and height, so that we avoid aligning the face and expression manually.

![Image](https://cdn-media-1.freecodecamp.org/images/SOtVpTHeSekjDBcZsh2fJWOnLoYPRe6CQvNg)

Now `mask-image` has this cool option which allows multiple images to be used as masks. So we can do this: `mask-image: url(face.svg), url(expression.svg);`. This is what we have now:

![Image](https://cdn-media-1.freecodecamp.org/images/A6H-X9gCRAHHBWFo62WsClZqPbsqGgTrl0U4)

One of the most important properties of CSS masks is `mask-position`, which positions the mask from the top left corner relative to its parent. And I can position multiple masks using the property `mask-position` just like `mask-image`.

So to make the face sad, we can use something like this: `mask-position: 0 0, 0 12px;`. And the result is this:

![Image](https://cdn-media-1.freecodecamp.org/images/G3LPJQJhJulrprRLpA6-3abAq1L1-sv319pp)

The first position `0 0` is for the `face.svg`, and the second `0 12px` is for `expression.svg`. This pushes it **12px** from above and results in the above expression.

#### Applying functionality

Now let’s animate these expressions on hover. So the complete code we get after applying the hover pseudo class is the following:

```
i {  background-image: -webkit-radial-gradient(hsla(0, 100%, 50%, .7), hsla(0, 100%, 20%, .8) 60%, hsla(0, 100%, 10%, 1));    mask-image: url('face.svg'), url('expression.svg');  mask-position: 0 0, 0 12px; /* To make the sad expression */
```

```
  transition: mask-position .5s ease-out;}
```

```
i:hover {  background-image: -webkit-radial-gradient(hsla(120, 100%, 50%, .7), hsla(120, 100%, 20%, .8) 60%, hsla(120, 100%, 10%, 1));
```

```
  mask-position: 0 0, 0 0; /* To make the happy expression */
```

```
  transition: mask-position .1s linear;}
```

After playing with the CSS a bit more, we can do this:

![Image](https://cdn-media-1.freecodecamp.org/images/ipIKP8u6LWV6ikxw-HJv-1xrJWBYPYXQfqOv)

This is one of the methods we can use to build those gripping animations we come across almost daily.

#### **One Important Note**

The masking properties might not work across all the browsers. So to make them work in all the browsers, just prepend browser specific labels like `-webkit-` , `-moz-` & `-0-` .

You can look at the complete code here on [github](https://github.com/nktkarnany/mask-css) and [codepen](https://codepen.io/nktkarnany/pen/bjmZOQ).

Thanks for reading! I hope you learned something.

