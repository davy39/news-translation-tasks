---
title: Why you should do Augmented Reality if you are a JavaScript developer — and
  how to start
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T16:43:29.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-augmented-reality-for-the-javascript-developer-with-an-example-71875ab184ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hIfbsKuXmHPb0qEKvotZ4A.jpeg
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: tools
  slug: tools
- name: Virtual Reality
  slug: virtual-reality
seo_title: null
seo_desc: 'By Evaristo Caraballo

  If you are a JavaScript coder who is still late to making up a definitive list of
  resolutions for 2019, let me give you a hand: Start figuring out how to get into
  Augmented Reality (AR).

  The Augmented/Mixed/Virtual Reality (AR/M...'
---

By Evaristo Caraballo

If you are a JavaScript coder who is still late to making up a definitive list of resolutions for 2019, let me give you a hand: Start figuring out how to get into Augmented Reality (AR).

The Augmented/Mixed/Virtual Reality (AR/MR/VR) combo has enjoyed frenetic growth since 2016, coming from a [marginal market value](https://www.statista.com/statistics/591181/global-augmented-virtual-reality-market-size/) of bit more than $6 Billion to one that might reach the $210 Billion in sales (including hardware) by 2022. Of all, [Augmented Reality](https://www.telecompetitor.com/ar-vr-forecast-bad-quarter-good-future/) is the one experiencing steady growth.

At first, a JavaScript (web) developer wanting to get into the AR boat might feel discouraged when finding [the usual required skills](https://blog.pusher.com/how-you-can-become-an-ar-vr-developer/); and then there is who ask [Machine Learning](https://medium.freecodecamp.org/8-ways-ai-makes-virtual-augmented-reality-even-more-real-25037707cfa1) or Internet of Things. However if you are mainly a JavaScript developer, consider yourself blessed: the language is [recurrently mentioned](https://www.quora.com/What-programming-language-is-used-to-create-virtual-reality-experiences-and-programs) as one you should know to enter this sector. The reason? Right now **a lot of AR development goes on the web**. And this is where JavaScript reigns.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m3EEXIiH_ZXxVzl-7-grLg.png)
_Mobile and Web were the last getting AR capabilities, and are still developing (extract from a [buildAR presentation](https://www.slideshare.net/robman/web-standards-adoption-in-the-ar-market/6" rel="noopener" target="_blank" title="))_

### Augmented Jobs for the JavaScript-fan — Really?

Maybe not too fast. There are many examples where AR/MR/VR shines on its own, specially in niche markets, but the industry hasn’t completely figured out the full value of the technology for the general consumer. Once that it solved, the industry would be certainly making more AR/MR/VR products, which would translate into more jobs.

For some analysts AR is expected to have the most pervasive impact, in part because it doesn't require [specific devices and conditions](https://www.quora.com/What-are-some-good-VR-AR-hardware-devices-that-not-many-people-know) to be implemented as VR does.

> AR has utility for almost everything, overlaying useful and relevant information on the world around you. AR can be pervasive in a way that VR cannot.

> - David McQueen -Strategy Analytics- [from an interview on Twice](https://www.twice.com/product/ces-2018-how-disruptive-can-vr-ar-become-roundtable-discussion)

It rests on the industry to find how to make AR a more every day life tech. According to some companies, particularly within the mobile phone realm, exploiting better the AR potential reduces to a well-known rule: _SIMPLICITY_.

> While Unity has become the default path for building AR apps, an increasing number need only a sprinkling of AR.

> - from an [article](https://medium.com/homestory-ar/building-an-ar-ai-furniture-app-with-react-native-1847bc1fcbaa) by [Benjamin Devine](https://www.freecodecamp.org/news/an-intro-to-augmented-reality-for-the-javascript-developer-with-an-example-71875ab184ee/undefined), Homestory AR

In many cases, resourcing onto the leading AR tools could be an overkill. Instead, a bunch of good UX-driven features over some 2D/3D assets could be more than enough to make striking products. Something a JavaScript developer regularly does.

It is then possible that any JavaScript developer will be embedding (non)standard AR/VR features as an extension of their traditional duties in the future. And if required, JavaScript is robust enough for more complex tasks. The sky is the limit.

### Becoming JavaScript-Augmented

Before starting, I would suggest to have a look at the several AR platforms and standards. The same technical constraints affecting the industry are also reflected in the AR world.

For example, there are several platforms, one for each Big Tech (Google = [ARCode](https://developers.google.com/ar/discover/), Apple = [ARKit](https://developer.apple.com/arkit/), MS = [ChakraCore](https://github.com/microsoft/chakracore), Facebook = [AR Studio](https://developers.facebook.com/blog/post/2018/05/01/ar-studio-create-distribute/), [React 360](https://facebook.github.io/react-360/), Mozilla = [aframe](https://aframe.io/)).

After having a quick look at the options, starting fully JavaScript’ed Augmented Reality projects is relatively easy. You can begin by taking any web/app dev framework like [Cordova](https://cordova.apache.org/), [Ionic](https://ionicframework.com/), [React Native](https://facebook.github.io/react-native/) or [Vue Native](https://vue-native.io/) to embed the AR framework of your choice — and deploy 3D assets on top of the real world.

If what you want is to deploy on the web using mostly marker-based AR, you could use GitHub repos like [AR.js](https://github.com/jeromeetienne/AR.js) (free), [argon.js](https://www.argonjs.io/) (free but limited) or [awe.js](https://awe.media/) (paid PaaS but with an old GitHub repository still available). There are a few tailored ones that are harder for the novice, many of them focused on things like facial/head recognition (such as [tracking.js](https://trackingjs.com/) and [headtrackr](https://github.com/auduno/headtrackr)).

Or you can boost your project capabilities if you are able to port available SDKs made by [AR-related companies](http://socialcompare.com/en/comparison/augmented-reality-sdks). There are many APIs that render as AR on browser too. For example, [Mapbox](https://www.mapbox.com/) follows that path and it is developed on JavaScript.

I would suggest you to keep it simple but interactive.

However if your ambitions point to also mastering design and animation in JavaScript, you definitively have to learn at least one [3D Javascript package](https://1stwebdesigner.com/3d-javascript-libraries/), and [THREE.js](https://threejs.org/) the most popular. Wait, though, until you have gained a good base of JavaScript and [OpenGl](https://www.opengl.org/) as well as geometry, trigonometry, linear algebra or physics. And don’t expect more help from the existing 3D JS GUIs; in particular, THREE.js has none. Challenging but exciting!

### Bonus Example

I wanted to prepare a quick demo just to explore the technology, so I took a nice CodePen and modified it to fit a marker-based web-rendered AR animation ported within a clone of [Stemkoski's](https://github.com/stemkoski/AR-Examples) [great work](https://stemkoski.github.io/AR-Examples/) with AR.js.

For you to see the example you need _a mobile device with a camera_ and internet (phone or tablet), and either a printed copy of _the marker_ or another device to show it on screen.

Ready? Now open this [link](https://evaristoc.github.io/ARexample/) using a browser in your mobile device:

[https://evaristoc.github.io/ARexample/](https://evaristoc.github.io/ARexample/)

Give authorization to use your camera, and point the camera **to a marker like below**, either printed or in another screen.

**NOTE:** works on Android and Chrome — it might not work for other devices and browsers ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7g9MciK6LR-9VRcH-LePSQ.png)
_The original animation can be found [here](https://codepen.io/rainner/details/LREdXd" rel="noopener" target="_blank" title=")._

Happy New Year!

I hope you will find this technology as fascinating as I do. If so, don't stay alone: contact us at the [freeCodeCamp forum](https://www.freecodecamp.org/forum/) and share your questions and ideas.

And if you liked this article, don't forget to give it a ? and to share it on social media.

Thanks for reading, enjoy AR and Happy Coding!!

