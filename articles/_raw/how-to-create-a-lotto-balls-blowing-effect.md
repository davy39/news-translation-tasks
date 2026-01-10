---
title: How to Create an Air Blowing Effect with JavaScript
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2020-07-02T15:36:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-lotto-balls-blowing-effect
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/ball-blower-image.png
tags:
- name: animations
  slug: animations
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: Have you ever wondered how you can create a realistic air blowing effect
  with JavaScript? Like the one shown on the evening TV shows, where multiple balls
  are being mixed up in a sphere-like object by leveraging air pressure? If you want
  to find out ...
---

Have you ever wondered how you can create a realistic air blowing effect with JavaScript? Like the one shown on the evening TV shows, where multiple balls are being mixed up in a sphere-like object by leveraging air pressure? If you want to find out how it's done, read on.

✨ If you want to skip the reading and jump straight to the code, you will find it [here](https://github.com/mihailgaberov/bingo-blower). Also, I have deployed a [live demo here](https://tender-hoover-fdc559.netlify.app/).✨

## Research

Recently I have decided to refurbish something old that I did 4 years ago for a [project of mine](https://github.com/mihailgaberov/bingo/). Here is how it looked:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-242.png align="left")

*Bingo Blower*

At that time I chose to use a library called [Paperjs](http://paperjs.org/). Back then this library let me build the closest thing to what I wanted to achieve.

As it turns out, there are many more JavaScript libraries today that let you do animations with or without physics.

Before making my final choice, which you will see below, I played around with [Anime.js](https://animejs.com/), [Velocity.js](http://velocityjs.org/), [Popmotion](https://popmotion.io/pure/), [Three.js](https://threejs.org/), [GreenSock JS](https://greensock.com/gsap/), [Mo.js](https://mojs.github.io/) and [Matter.js](https://brm.io/matter-js/). All of them have pluses and minuses, and as with everything else, your choice between them depends on the specific needs you might have. I chose Matter.js.

## Meet Matter.js

Matter.js is a 2d rigid body JavaScript physics engine. Sounds complex, but it's not. What this actually means is that this library contains all the stuff we need to create realistic 2d physics animations with JavaScript.

For detailed information on what Matter.js has to offer, you might check their [documentation](https://brm.io/matter-js/docs/). In our case, we will take advantage mainly of the [Body module](https://brm.io/matter-js/docs/classes/Body.html) and the features it has. Let's see how in the next section.

## Balls and Tube

The "tube" component is easy. It's just a background [image](https://github.com/mihailgaberov/bingo-blower/blob/master/static/images/blower.png) I am using to create an illusion that the balls are flying around inside a sphere-like glass object.

The interesting part is the code to create the animations and detect the collisions between the balls and the walls. But let's go step by step.

As I said, the "tube" is a background image I've added via the simple CSS [background property](https://developer.mozilla.org/en-US/docs/Web/CSS/background). Let's see the balls themselves. For them I had two choices - try to draw circles in canvas and make them look like balls or use simple images. I chose the latter option, as I wanted to have a more realistic view of the balls.

So, with the help of a graphic processing program, a friend of mine created [75 images](https://github.com/mihailgaberov/bingo-blower/tree/master/static/images) for me, one for each ball.

Having all the assets we need, we are now ready to go deeper and implement some physics with Matter.js.

## Implement, test, implement, test

Before going into the animation itself, we need to mention few Matter.js specific things. When creating animations with this library, we need to define, at a minimum:

* [Matter.Engine](https://brm.io/matter-js/docs/classes/Engine.html) - this is the controller that manages updates to the simulation of the world.
    
* [Matter.World](https://brm.io/matter-js/docs/classes/World.html) - contains methods for creating and manipulating the world composite.
    
* [Matter.Render](https://brm.io/matter-js/docs/classes/Render.html) - this module is a simple HTML5 canvas-based renderer for visualizing instances of `Matter.Engine`.
    

In our example we are also going to use:

* [Matter.Bodies](https://brm.io/matter-js/docs/classes/Bodies.html) for creating the different parts of the scene (the balls, the invisible boundary circle).
    
* [Matter.Body](https://brm.io/matter-js/docs/classes/Body.html) for applying forces to the bodies and thus creating a nice physics-based simulation of a blower.
    
* [Matter.Runner](https://brm.io/matter-js/docs/classes/Runner.html) to run the whole thing.
    
* [Matter.Events](https://brm.io/matter-js/docs/classes/Events.html) gives us ability to have listeners for different events that could happen during the animation. In this specific case we use it for listening for the 'tick' event, which occurs on every render tick.  
    In the event handler function we do our checking for when the balls collide with the walls and we apply the relevant forces to create a bounce effect.  
    We postpone the listening for this event with a 3 second timeout, so we can have a more lotto-like effect. Imagine a sphere where the balls are starting to move when, let's say, a button is pressed.
    

## Try and Play

In the beginning of this article I posted the link to the [GitHub repository](https://github.com/mihailgaberov/bingo-blower) with the code and the assets in it. If you want to play more, you can easily check it out and try different modifications. You might want to play with the forces being applied, or the size of the balls, and so on.

There is plenty of room for experimenting when we talk about Physics. And it's always fun, especially when we add animations to the picture.

## Conclusion

As it turns out, [Matter.js](https://brm.io/matter-js/index.html) is a great library for doing 2d realistic animations backed up by the laws of Physics. Of course, there are other options you might choose from, but as I said, this is a matter of choice and project needs.

I personally would recommend at least giving it a try and see for yourself. For someone with Flash experience or similar, Matter.js is definitely easy to start with. And if you are stubborn enough to keep trying different settings, you might achieve incredible results.

## Resources

https://brm.io/matter-js/ - The website of the library  
[https://burakkanber.com/blog/modeling-physics-in-javascript-introduction/](https://burakkanber.com/blog/modeling-physics-in-javascript-introduction/) - interesting and well explained articles related to physics in JavaScript  
[https://spicyyoghurt.com/tutorials/html5-javascript-game-development/collision-detection-physics/](https://spicyyoghurt.com/tutorials/html5-javascript-game-development/collision-detection-physics/) - collisions detection tutorial  
[https://codepen.io/AlexRA96/full/egaxVV](https://codepen.io/AlexRA96/full/egaxVV) - bouncing ball example  
[https://codepen.io/Shokeen/pen/WjKmMG?editors=1010](https://codepen.io/Shokeen/pen/WjKmMG?editors=1010) - codepen example with applying forces  
[https://code.tutsplus.com/tutorials/getting-started-with-matterjs-body-module--cms-28835](https://code.tutsplus.com/tutorials/getting-started-with-matterjs-body-module--cms-28835) - beginner tutorial to get you started with Matter.js  
[https://codepen.io/jh3y/pen/gOPmMyO?editors=0110](https://codepen.io/jh3y/pen/gOPmMyO?editors=0110) - another cool example with falling bears  
[https://codepen.io/danielgivens/pen/geKrRx](https://codepen.io/danielgivens/pen/geKrRx) - even cooler example with a circle clock and particles inside  
[https://codepen.io/dotcli/pen/NEXrQe](https://codepen.io/dotcli/pen/NEXrQe) - another example of circle bounds and particles (socks!) inside
