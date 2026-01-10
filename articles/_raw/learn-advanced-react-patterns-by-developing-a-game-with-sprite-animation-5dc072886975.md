---
title: Learn advanced React patterns by developing a game with sprite animation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-02T16:04:11.000Z'
originalURL: https://freecodecamp.org/news/learn-advanced-react-patterns-by-developing-a-game-with-sprite-animation-5dc072886975
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p6Q4wwQ2m1D_rGYvRBRPWg.png
tags:
- name: CSS
  slug: css
- name: Games
  slug: games
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pavel Vlasov

  Have you ever wanted to learn some advanced React patterns? Or build your own game
  engine? If at least one answer is yes, then this article is for you.

  In this tutorial, you’ll learn how to build basic sprite animation using React,
  st...'
---

By Pavel Vlasov

Have you ever wanted to learn some advanced React patterns? Or build your own game engine? If at least one answer is yes, then this article is for you.

In this tutorial, you’ll learn how to build basic sprite animation using [**React**](https://reactjs.org/)**, [styles-components](https://www.styled-components.com/),** and **requestAnimationFrame**. At the end you’ll be able to create characters like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ig-pwnKpjNtc2xaM0HMR6A.gif)

You may ask me _why can’t I learn it another way_? Well… There’re three reasons for that:

![Image](https://cdn-media-1.freecodecamp.org/images/1*rBqlCIMpp_nQPy2EEpB0Hw.png)

So, let’s do it! ?

### **Let’s start with a bit of a theory**

What is a sprite animation? [Wikipedia](https://en.wikipedia.org/wiki/Sprite_(computer_graphics)) says that

> In computer graphics, a **sprite** is a two-dimensional bitmap that is integrated into a larger scene.

So basically sprite animation is a repeatedly changing two-dimensional bitmap.

Sprite is usually represented like a png image with different states of the animation:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hbOGCHijQurkW40hwnocDw.png)
_Bitmap image_

We’ll start by creating a tile component that will show us one frame at a time and allow us to change frames with **state** property:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fuAsHwFdlqR1qUw2b36GlA.gif)

Basically, we’ll need to show one part of the image at a time and hide the rest. Pretty straightforward.

### Tile

First of all, we’ll create a container component to create the shape of our frame:

`width` and `height` represent the size of the tale, and `scale` increases the size of the image. `overflow: hidden` will hide the unused part of the image and `transform-origin` will make a container to keep its top and left the same when we scale it.

Now we need to adjust the position of the inner image. We’ll use the `transform: translate` CSS property for that:

Now let’s combine everything together in the tile component:

* `src` property contains a link to the image
* `tile` is the object with `width` and `height` fields, represents the size of the tile
* `state` frame index
* `scale` property to increase the size of the image (For example, `scale = 2` is 2x image)

In the next step, we’ll add some movement to our image.

### Sprite

We’ll use **requestAnimationFrame** for that. You may ask why we don’t use **setTimeout** or **setInterval.** The problem with timeouts is that the callback will fire somewhere in between frames, that may result in clunky animation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2UnyL2Wr6r2OIDvogPpNLQ.png)
_requestAnimationFrame vs setInterval_

Also, **requestAnimationFrame** allows us to synchronize animations of different objects on the screen. In the game you’ll have lots of them!

Let’s put together a Sprite component:

In the `animate` function, we should change the `state` of the frame and request a new animation frame:

We use the e`framesPerStep` property to control the number of states per frame, so our animation won’t be too fast.

### What about a gun? ?

Now the only thing we need to do is combine our sprite with the gun image:

And you should get the following result:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mi4Xn8yPVYO7nDBf5TBXdg.gif)

The best way to learn something it to build it by yourself. So I encourage you to use this [codesandbox](https://codesandbox.io/s/github/react-dev-camp/react-game-dev-course/tree/master/lessons/1_sprites/javascript?autoresize=1&hidenavigation=1):

The TypeScript version is [available here as well](https://codesandbox.io/s/github/react-dev-camp/react-game-dev-course/tree/master/lessons/1_sprites/typescript).

As a bonus, you can implement different animations using files from the assets folder.

You can find the source code [here](https://github.com/react-dev-camp/react-game-dev-course). I used game assets made by [finalbossblues](https://finalbossblues.itch.io/pixel-shooter-towers-asset-pack).

Hope you enjoyed the article! ?

Follow me on [Medium](https://medium.com/@pvlasov) and [Twitter](https://twitter.com/pvl4sov) to get more updates on new articles. Also, share this article to help others know about it. Sharing is caring ?

**Destroy this clap button if you want more.**

**You can clap up to 50 times!** ?

Some more resources about the topic:

[**Understanding JavaScript's requestAnimationFrame() method for smooth animations**](http://www.javascriptkit.com/javatutors/requestanimationframe.shtml)  
[_requestAnimationFrame() is a JavaScript method for creating smoother, less resource intensive JavaScript animations…_www.javascriptkit.com](http://www.javascriptkit.com/javatutors/requestanimationframe.shtml)

_Originally published at [react.camp](http://react.camp/posts/advanced-react-patterns-game-engine-1-sprites/)._

