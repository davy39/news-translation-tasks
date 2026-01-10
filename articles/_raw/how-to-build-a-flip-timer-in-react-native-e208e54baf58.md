---
title: How to build a flip timer in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-02T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-flip-timer-in-react-native-e208e54baf58
coverImage: https://cdn-media-1.freecodecamp.org/images/0*273pYX1ym8bIxTou
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pritish Vaidya

  Introduction

  A Flip Timer is a digital time keeping device with the time indicated by numbers
  that are sequentially revealed by a split-flap display.

  This article will demonstrate the building of a Flip Timer in React Native using
  i...'
---

By Pritish Vaidya

### Introduction

A _Flip Timer_ is a digital time keeping device with the time indicated by numbers that are sequentially revealed by a split-flap display.

This article will demonstrate the building of a _Flip Timer_ in React Native using its exposed APIs and no additional dependencies.

### Challenges to overcome

* Implement `transform-origin` property using your **_College Math Course_** matrices techniques since it is not supported in React Native. Rotation around the centered origin (by default) is easy, but we need to translate origin and rotate around the edges.
* Implementation of Flip Number component.
* Overcome `overflow: hidden` issue in android since it doesn’t work with absolute positioned elements.

### Contents

1. **Implement Flip Number Component**
2. **Implement FoldView**

* Basic Layout
* Overcoming the Challenge
* Adding the Transformations
* Adding the Animations

3. **Update Timer Component**

4. **Final Result**

5. **Links**

### Implement Flip Number Component

#### Basic Layout

The Basic Layout consists of two cards — upper and lower joined together so that the view looks like a Flip Timer.

**Number Card**

It is a basic layout consisting of a wrapper and two cards — _lower_, _upper._

**Note**: Lower Card has the previous number added to it. Its use will be revealed once we reach the _FoldView_ implementation.

![Image](https://cdn-media-1.freecodecamp.org/images/uzy-CsNuZji7eCwWTu6LYYOhygfzB4uP7v68)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/number-card.js" rel="noopener" target="_blank" title=")_

**Card**

The wrapper of the card has `overflow: hidden`, and we’re translating its items (number) based on the type of the card (upper or lower).

![Image](https://cdn-media-1.freecodecamp.org/images/-1JOq61At7-JFxeyTRsn5vgtzCZYTL9UkZ-M)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/card.js" rel="noopener" target="_blank" title=")_

### Implement FoldView

#### Basic Layout

To build FoldView we need two _FlipCards_ similar to _NumberCards_ but with _absolute positioning_ so that they are above the _NumberCards_ when flip animations are applied.

**Number Card**

Adding _FlipCard_ component to the _NumberCard_ component.

![Image](https://cdn-media-1.freecodecamp.org/images/YrmnGEZBPPoxwsvskGYqHaYzPJ4VkB8viPO1)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/number-card.js" rel="noopener" target="_blank" title=")_

**Flip Card**

The FlipCard component is an animated wrapper with absolute positioning used while applying flip animation.

**Challenge (Part 2 and Part 3)**: `overflow: hidden` with absolute positioning has major issues in _android._ Using this [StackOverflow](https://stackoverflow.com/a/21684490/6606831) post, it can be solved by using an _overflow container_ inside the absolute positioned element.

![Image](https://cdn-media-1.freecodecamp.org/images/KG-NyI8-vafcBiZGWoZaD1hpCpwW0V-3ff3a)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/flip-card.js" rel="noopener" target="_blank" title=")_

#### Final Result

![Image](https://cdn-media-1.freecodecamp.org/images/qCA0sQ1vuVxxPDWMqOirMoOXtPhRh2-Rwyrl)

#### Overcoming the Challenge

Now comes the hard part. We need to add fold the FlipCard component along the edges.

Since React Native doesn’t support `transform-origin` property, we need to find some other way to shift the rotation origin on the bottom edge.

Fortunately, there is one way to overcome this issue. According to this awesome [article](https://commitocracy.com/implementing-foldview-in-react-native-e970011f98b8) and reading the [MDN](https://developer.mozilla.org/en-US/) docs for the [transform-origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) property, it can be implemented using **matrices.**

**Utils**

React Native exposes several matrix operations in the [MatrixMath.js](https://github.com/facebook/react-native/blob/master/Libraries/Utilities/MatrixMath.js). The important ones that we require are

* **Identity Matrix:** It returns a 4 * 4 identity matrix `[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]`

![Image](https://cdn-media-1.freecodecamp.org/images/J7CO8Ge-QqrmmFwuphxEwbypurpEPgQFUqeQ)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Multiply Matrix:** This utility method generates output based on the multiplication of 4*4 matrices `a` and `b` supplied as input.

![Image](https://cdn-media-1.freecodecamp.org/images/1xbhTbClhu47mEsGPa7p4T7wHsajXl3PAy0J)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Rotate Matrix:** It is a custom utility method that will take a 4*4 matrix and degree to which it will be rotated to then multiply it to the original matrix to return the generated result.

![Image](https://cdn-media-1.freecodecamp.org/images/qa2oiTgiOehlLCu4Qqfcj6zhNofoKpfA-1XL)

![Image](https://cdn-media-1.freecodecamp.org/images/q2MBhiltQRvtPmHC8r28UGvBDGPYOSTyEriN)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Perspective Matrix:** This utility method will allow us to use the perspective style to React Native and then multiply to the original 4*4 matrix.

![Image](https://cdn-media-1.freecodecamp.org/images/0HmvXN1gu3-hGoK1ydxmf-8rBmxtIJEe3PNi)

![Image](https://cdn-media-1.freecodecamp.org/images/RjIzOwoDY1-1vvH1Y9lu7RC-opK8hpS1vSoL)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Translate Matrix:** This utility method will translate the origin and modify the original 4*4 matrix

![Image](https://cdn-media-1.freecodecamp.org/images/OwRIvTNQ6f4YHisOmGSU362njvxovBFJ8JVy)

![Image](https://cdn-media-1.freecodecamp.org/images/ThtIdQR5osqzP5GMmxFGvQB5oUbuUUHMMwRv)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Un-Translate Matrix:** This utility method will un-translate the origin and modify the original 4*4 matrix

![Image](https://cdn-media-1.freecodecamp.org/images/P0Ct10em0E2zebJeY2UTdZKMW2JmWyM62xMJ)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

#### Adding the Transformations

`deg` is the degree to be rotated and `y` is the height of the component to which it will be translated.

**Challenge (Part 1)**: Combining the utils from the above, `transform-origin` is implemented successfully.

![Image](https://cdn-media-1.freecodecamp.org/images/e9M2yLlahuXIQJ03D3UdvbQSNxSLlY-Lppdk)

![Image](https://cdn-media-1.freecodecamp.org/images/2qvRlyie7oBWQUwfyOn1t7RAvnZQ-rALAyj9)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/timer.js" rel="noopener" target="_blank" title=")_

#### Adding the Animations

![Image](https://cdn-media-1.freecodecamp.org/images/GBeUP2fLLmHCcbS6gpVdXBR1DwRMuULV2t2t)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/timer.js" rel="noopener" target="_blank" title=")_

### Update Timer Component

#### Add Time Util

This util will increment the timer by one sec and adjust hours, minutes, seconds.

![Image](https://cdn-media-1.freecodecamp.org/images/3r0RZrCsJG4d0J3VNbjKaO4lPlySXO1Cxl0S)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

#### Timer Component

The timer component will call **Time Util** and update the component based on hours, minutes, seconds

![Image](https://cdn-media-1.freecodecamp.org/images/ZcNz-7U5YSbU8UYyQwKijO8cfpEE2-CL1pN4)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/timer.js" rel="noopener" target="_blank" title=")_

#### Flip Number Component

This component just splits the number into two parts based on their digit placement and calls **NumberCard** component .

![Image](https://cdn-media-1.freecodecamp.org/images/MPgjFf9b9pYxOTVO461fBB-Dqh-8O25D3z5b)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/index.js" rel="noopener" target="_blank" title=")_

### Final Result

![Image](https://cdn-media-1.freecodecamp.org/images/c93caflCfnyqBNcQed-BOGQITYP-QFngekZ8)

### Links

I’ve published a package for it that contains more customizable properties.

* npm : [react-native-flip-timer](https://www.npmjs.com/package/react-native-flip-timer)
* GitHub: [react-native-flip-timer](https://github.com/pritishvaidya/react-native-flip-timer)

More of the cool stuff can be found on my [**_StackOverflow_**](https://stackoverflow.com/users/6606831/pritish-vaidya) and [**_GitHub_**](https://github.com/pritishvaidya) profiles.

Follow me on [**_LinkedIn_**](https://www.linkedin.com/in/pritish-vaidya-506686128/), [**_Medium_**](https://medium.com/@pritishvaidya94), [**_Twitter_**](https://twitter.com/PritishVaidya) for further update new articles.

**One clap, two claps, three claps, forty?**

![Image](https://cdn-media-1.freecodecamp.org/images/6nEX6G3ucbC8JOm8KkdqSWhrwBusRHDmmQkH)

_Originally published at [blog.pritishvaidya.com](https://blog.pritishvaidya.com/posts/2019-03-02-building-a-flip-timer-in-react-native/) on March 2, 2019._

