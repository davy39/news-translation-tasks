---
title: How to wish someone Happy Birthday using Augmented Reality
subtitle: ''
author: Pratik Parmar
co_authors: []
series: null
date: '2018-06-29T17:43:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*R6c3P43LzQgB6d3khSNnRQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Augmented Reality
  slug: augmented-reality
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Virtual Reality
  slug: virtual-reality
seo_title: null
seo_desc: I have a friend who’s birthday was coming up, so I wanted to do something
  special for her. As she is a TechGeek just like me, so I couldn’t just get her a
  simple birthday present like a teddy bear or chocolates. So, I started looking for
  unique ways ...
---

I have a friend who’s birthday was coming up, so I wanted to do something special for her. As she is a TechGeek just like me, so I couldn’t just get her a simple birthday present like a teddy bear or chocolates. So, I started looking for unique ways to wish her a happy birthday on the Web.

I ended up watching a [video](https://youtu.be/O_EUnGMJtLA) where a guy was proposing to a girl using VR. So, I decided — that was it! That was how I was gonna do it. Not the proposal part though.

While I was contributing to Mozilla, I’d created few small VR projects using [**A-Frame**](https://aframe.io/) **—** Mozilla’s web-framework for building virtual reality experiences. And believe me, even if you don’t know much about VR or AR, you can easily create a VR scene using A-Frame. The only prerequisite is HTML, which you can learn easily [here](https://www.w3schools.com/Html/). For a better understanding, though, I recommend that you go through [A-Frame School](https://aframe.io/aframe-school/#/), which is a great collection of tutorials intended for beginners.

So I’d decided that I was gonna use A-Frame, but I wanted more than just a simple VR scene displaying “Happy Birthday.” In the end, I chose to create an AR scene. I found a great project called [AR.js](https://github.com/jeromeetienne/AR.js/blob/master/README.md)**.** If you wanna get started with AR.js, here is a [great article for beginners](https://medium.com/arjs/augmented-reality-in-10-lines-of-html-4e193ea9fdbf)**.**

### Building a basic AR web app

![Image](https://cdn-media-1.freecodecamp.org/images/1*R6c3P43LzQgB6d3khSNnRQ.jpeg)
_AR Scene, created using AR.js_

To watch the AR scene, you have to:

* Open this [HIRO marker image](https://jeromeetienne.github.io/AR.js/data/images/HIRO.jpg) in your desktop browser.
* Open this AR web app in your phone browser, and point it to your screen.

When you scan a marker (here, a HIRO marker), it’ll display an AR scene on your phone, just like the image above. I used a plain HIRO marker, but you can [create your own marker as well](https://medium.com/arjs/how-to-create-your-own-marker-44becbec1105).

So, after adding all these libraries, my code looked like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*VpWtY3jmzmc5ftAM23SRPA.png)
_Basic AR web app [ [Demo](https://hackyroot.github.io/A-Frame-Examples/Happy_Birthday/Basic.html" rel="noopener" target="_blank" title=") ]_

Please note that while accessing any AR web app, if you get any prompt asking permission to access the webcam, please allow it. Otherwise the app won’t work.

### Add 3D models and fonts

So, now we have simple AR web app working on our device. But what’s a birthday without **cake**?! Fortunately, A-Frame supports three types of 3D models: [glTF](https://aframe.io/docs/0.8.0/components/gltf-model.html), [OBJ](https://aframe.io/docs/0.8.0/components/obj-model.html), and [COLLADA](https://aframe.io/docs/0.8.0/components/collada-model.html). Learn more about 3D models in A-Frame [here](https://aframe.io/docs/0.8.0/introduction/models.html).

I downloaded some 3D model files of cake from [Google Poly](https://poly.google.com/)**.** You can import any asset files in A-Frame using the _<a-asse_ts> tag. You can also import separate fonts, in case you want to use a different font.

I was pretty convinced that A-Frame couldn’t be more awesome. But, wait…

### Add audio

Birthdays are also not complete without the birthday song, right? And A-Frame supports Audio files as well. You can use the _<audi_o> tag to import your files, under the <a-assets> tag.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z7Bj8EeI8PA_MfGnUzdv5w.png)
_Import asset files_

### Add particles

What’s the thing that comes to your mind when you hear about a birthday — after cake, of course? A **party,** right? So, let’s add confetti to our AR scene, using [A-Frame’s Particle System Component](https://github.com/IdeaSpaceVR/aframe-particle-system-component).

![Image](https://cdn-media-1.freecodecamp.org/images/1*WRq3LqBLvxy8aQIuH3J2zA.png)
_Add libraries for confetti and 3D text_

### Let’s put it all together

#### 3D Models

This code will display the 3D model of the cake. But as you can see, I’ve added a few values in the _rotation_ and _scale_ fields. So, let’s discuss that. According to A-frame’s [GitHub page](https://github.com/aframevr/aframe/blob/master/docs/components/rotation.md):

* **Rotation**: the rotation component defines the orientation of an entity in degrees. It takes the pitch (`x`), yaw (`y`), and roll (`z`) as three space-delimited numbers indicating degrees of rotation.
* **Scale**: the scale component defines a shrinking, stretching, or skewing transformation of an entity. It takes three scaling factors for the X, Y, and Z axes.
* **MTL:** stands for Material Library File (.**mtl**) Material library **files** contain one or more material definitions, each of which includes the color, texture, and reflection map of individual materials. These are applied to the surfaces and vertices of objects. Material **files** are stored in ASCII format and have the .**mtl** extension.
* **OBJ**: a file format that was created as a simple way to import and export geometry from different 3D applications. This is a common file type used by many 3D design solutions.
* **Suggestion**: If you don’t see your model, try scaling it down. OBJ models generally have extremely large scales in comparison to A-Frame’s scale.

If you’re wondering how I knew the exact values for rotation, well I didn’t. I used an amazing tool created by the Mozilla team called [A-Frame Inspector](https://github.com/aframevr/aframe-inspector), built for this purpose only.

To learn more about _<a-obj-model_>, visit [thi](https://aframe.io/docs/0.8.0/primitives/a-obj-model.html)s link.

![Image](https://cdn-media-1.freecodecamp.org/images/1*588pLp64QgtSVHgXeq-4rg.png)
_Display 3D model of Cake_

#### Particles

Well, this code may look overwhelming at first sight, but believe me, it’s not. We discussed Rotation earlier, but let’s talk about other fields as well:

* **Position**: places entities at certain spots in 3D space. The Position takes a coordinate value as three space-delimited numbers.
* **Preset**: preset configuration. Possible values are: `default`, `dust`, `snow`, `rain`. Here we chose default in order to display starts.
* **Color**: describes a particle’s color. This property is a “value-over-lifetime” property, meaning an array of values can be given to describe specific value changes over a particle’s lifetime.
* **Acceleration Value**: describes this emitter’s base acceleration.
* **Particle Count**: the total number of particles this emitter will hold.
* **Direction**: the direction of the emitter. If the value is `1`, the emitter will start at beginning of particle's lifecycle. If the value is `-1`, the emitter will start at end of particle's lifecycle and work it's way backward.
* **Rotation Axis**: Describes this emitter’s axis of rotation. Possible values are `x`, `y` and `z`.

To know more about A-Frame’s Particle Component System_,_ visit this [link](https://www.npmjs.com/package/aframe-particle-system-component).

![Image](https://cdn-media-1.freecodecamp.org/images/1*lryKm0DHjxWdXL2on4uiig.png)

#### Text and Audio

Well, you use can use _<a-tex_t> as well, but I decided to go [with Text Geometry Com](https://www.npmjs.com/package/aframe-text-geometry-component)ponent for more options. It’s used to generate text as a single geometry.

* **Material** : The text geometry component defines just the geometry. We can apply any three.js material to the geometry.

```html
<a-entity text="value: HELLO" material="color: red; src: #texture"></a-entity>
```

For more details, visit three.js’s [documentation](https://threejs.org/docs/).

* **Text Geometry**: string and font value. (you should edit the text in this part, otherwise you’ll end up wishing happy birthday to my friend ??)
* **Sound**: defines the entity as a source of sound or audio.
* **Autoplay**_:_ describes whether to automatically play the sound once set.
* **Loop**_:_ describes whether to loop the sound once the sound finishes playing.
* **On**: an event for the entity to listen to before playing sound.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YVFBn6QETdSUvbtRwLS5zw.png)

### Resources:

* [Source code](https://github.com/HackyRoot/A-Frame-Examples/tree/master/Happy_Birthday)
* [Demo](https://hackyroot.github.io/A-Frame-Examples/Happy_Birthday/demo.html)

Yes, you made it ? ? ?. You’ve created your fi**rst AR application. I**f you did everything correctly, you should now see something like the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zZc5N-LaMQm9iXPFOG6I5g.jpeg)
_Finally, Happy Birthday Krupa!_

If you like my work, please follow me on Medium @[Pratik Parmar](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) or add me on [LinkedIn](https://www.linkedin.com/in/pratik-parmar-8853597a/). Feel free to reach out to me on Twitter: [Pratik Parmar](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) or comment down below, in case you need any help.

Apart from Open-source contributions at Mozilla, I’m a Microsoft Student Partner and community member at GDG Baroda. I would like to thank [Mozilla](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) and the [MozillaIN](https://twitter.com/MozillaIN) community for providing me a chance and the resources to learn about VR/AR and Open Source.

This is me, **Pratik Parmar** signing off till the next tech adventure. Over and Out…

[ Edit: Thank you [Vikranth Kanumuru](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) for drawing my attention that URL of source code was broken. It’s been updated now, please go ahead and try now. Keep coding, keep rocking ]

