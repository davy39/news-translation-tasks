---
title: Bubble animation with React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-02T07:35:02.000Z'
originalURL: https://freecodecamp.org/news/bubble-animation-with-react-native-72674eab073a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TRtgLab0Tjd7bLg6.
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'By Narendra N Shetty

  Lessons learned while building a React Native App using Animated and PanResponder


  In this article, I’ll talk about how I implemented an app transition which I found
  on Dribbble by Ramotion.


  _[https://dribbble.com/shots/2694049-...'
---

By Narendra N Shetty

#### Lessons learned while building a React Native App using `Animated` and `PanResponder`

![Image](https://cdn-media-1.freecodecamp.org/images/0*TRtgLab0Tjd7bLg6.)

In this article, I’ll talk about how I implemented an app transition which I found on Dribbble by [Ramotion](https://dribbble.com/Ramotion).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GZVRK8qxfuLU4AUrUNry5g.gif)
_[https://dribbble.com/shots/2694049-Pagination-Controller-App-Interface](https://dribbble.com/shots/2694049-Pagination-Controller-App-Interface" rel="noopener" target="_blank" title=")_

This pagination controller can be used for onboarding flow or for a tutorial.

The complete version is published in Expo, and you can get it by opening the Expo app and scanning this QR code:

![Image](https://cdn-media-1.freecodecamp.org/images/1*esBhVm4dAnaXERC-coIrVQ.png)
_[https://expo.io/@narendrashetty/onboarding-blog](https://expo.io/@narendrashetty/onboarding-blog" rel="noopener" target="_blank" title=")_

### Let’s begin, shall we?

Here’s how I built the background:

I had `View` holding the background color. This includes `Animated.View` for the bubble animation. Its position was absolute so that it stayed on top of the screen. I also added some basic styles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lwk_IdAAzEKX5Hb1tj4JNQ.png)

Then, I animated the bubble by expanding from 0 to max using the CSS transform scale with `Animated.timing`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CtAMCroXo5AvBiwOZlc63Q.gif)

The above animation needed to trigger based on user interaction. First I used `TouchableWithoutFeedback`. Then I changed it with gestures.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sIcR0RdmQA7SK2fSUcu7MA.gif)

I positioned the bubble according to the gif, which animated from the bottom. I did this using `top` and `left` property.

![Image](https://cdn-media-1.freecodecamp.org/images/1*keM44KHgufeyR5s-aviqaA.gif)

Neat! Results are as expected except the color. We’ll get back to that later.

Now I restructured the code by moving the bubble logic into a separate component called `CircleTransition.` Then I triggered the animation from the parent component.

Then it was time when to tackle the color. To make the bubble animate with the new color, I passed the new color into the component. And after the transition, I hid the bubble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OF0UIS4xMaHb5vXg0k6_bQ.gif)

Can you see something weird in the above transition?

During the second bubble transition, the background color is fell back to the first color. I needed to update the background color to the new color with the bubble transitioned.

I passed a callback to the `start` method which executed when the transition completed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oo83AYeag2TPn43k6ApHXg.gif)

Voila! It’s all set. Now I had the basic animation working.

Next I got into the gesture. The bubble transitions when the user swipes left or right according to the gif.

I created a new component called `Swipe`. It contains all the logic for the gesture and replaces`TouchableWithoutFeedback`.

I used `PanResponder`which reconciles several touches into a single gesture. It makes single-touch gestures resilient to extra touches. It can also recognize simple multi-touch gestures. For more on this you can go [here](https://facebook.github.io/react-native/docs/panresponder.html) and [here](https://facebook.github.io/react-native/docs/gesture-responder-system.html).

Now for the logic of the gestures.

First I needed to figure out which direction the user is swiping. I only need to animate when the user swipes left or right. I also needed to setup some threshold to determine if it’s actually a swipe or not.

If it was a valid swipe, I triggered the appropriate action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RAoguSe8-rcAvnCx2vkCIg.gif)

Yes! You guessed it right. I have gotten what I wanted to achieve with the gesture. Then I added an action for `swipeRight`. The gesture was completed with a bit of refactoring.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ENwNGJeMT2zODhYm1-WIzg.gif)

That’s it! This was the most complex part in the app.

I won’t show my complete work on this app. The information in this post should be enough help you build your own. Fork [this](https://github.com/narendrashetty/onboarding-RN) and try to complete your app to match the above gif.

If you are stuck and need any help, final version is in `result` branch, have a peek. Also you can ping me on Twitter [@narendra_shetty](https://twitter.com/narendra_shetty) or comment below.

And when you complete, please share your Expo/GitHub link.

If this article was of any help to you, please clap for me. It will motivate me to write more :)

