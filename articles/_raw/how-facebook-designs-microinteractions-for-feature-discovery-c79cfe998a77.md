---
title: How I recreated Facebook’s microinteractions for feature discovery
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-18T10:16:28.000Z'
originalURL: https://freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1Bi1hsnhH7XnNGOyf8yGbw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Yonatan Doron

  Demo Orientation — Exampels are in a Vue.js configuration hosted at Codesandbox.io,
  in order to reach the pure HTML/SCSS logic after navigating away click the components
  folder → then click spark.vue file → the HTML is wrapped around...'
---

By Yonatan Doron

**Demo Orientation** — Exampels are in a Vue.js configuration hosted at Codesandbox.io, in order to reach the pure HTML/SCSS logic after navigating away click the `components` folder → then click `spark.vue` file → the HTML is wrapped around `<templa`te> tags → the SCSS is just a scroll away wrapped a`round &`lt;style> tags and that’s it → Enjoy! :)

_For those who just wish to head to the code example, it’s right [here](https://codesandbox.io/s/z3x7vl176m)._

_If you wish to head straight to the challange then click [here](#4c58)_

**_*A Microinteraction_** _is a single use, subtle visual queue that draws your attention to a change in status. A power light on a coffee pot, or a color change on button hover are two examples._

#### Why? Who?! What!? and some Orientation

A common UX problem designers and frontend developers occasionally encounter is the **need to introduce a new feature** or expose a “well hidden” one that for some reason maybe due to functionality clutter, poor design or some other reason the **user rarely interacts** with that area or feature of your application.

Whether it’s a new exciting feature your company would like to start getting usage data reactions and feedback from users or if it’s an already existing feature that is rarely used for some reason — this problem exists and we encounter it every now and then in our industry.

I came across this exceptional possible solution on the **Facebook Mobile App.** Interaction Designers and Frontend Developers at Facebook decided to remove a certain action from my in-app navigation bar and put a new one — the quick link to my profile. Whether it be that they studied my behavior specifically or if it’s a more robust phenomena, it is definitly a worthy cause in my opinion.

#### A First Hand UX problem — Solved

Often I find myself looking for the quickest way to navigate to my profile via the Facebook app. In most cases I shift my sight to a few areas in the app visually searching as well as clicking a few areas full of anticipation to reach my final destination until I eventually reach my profile (It varies of course in which app state or screen you are in during your session) — to conclude, a not so pleasant experience to say the least.

Facebook, and more specifically **Interaction Designers** as well as the frontend developers who together concocted this unique solution, solved this issue perfectly in my opinion.

The message they tried to convey as I perceive it is that there’s something **New, Shiny and Fun** that was gifted to us users. It’s similar to a present that signals us that the unraveling and unboxing of this new action would lead us to a **pleasant and a much desired experience.** Further, when glancing at the static screen of the Facebook mobile app, the only moving part is this wonderful shiny and sparking microinteraction — a clear signal for a call-to-action.

_Let’s go for a deep dive on how such a powerful, carefully designed Microinteraction and a Microinteraction Fanatic (like me) triggered a quest for exploration!_

![Image](https://cdn-media-1.freecodecamp.org/images/1*SqTzmKIr3XOnLPl2ngQXsQ.gif)
_Original — Facebook telling me a new option is now available in my taskbar that I often use_

![Image](https://cdn-media-1.freecodecamp.org/images/1*WqepNW9FX8d_0SHRaUJtig.gif)
_My version — or wait is this the original? I am a bit confused…_

#### Simple yet Powerful and Alluring

A seemingly simple UI element — these 3 simple blueish sparkles appearing briefly over the avatar icon — are hinting that this element is a “shiny new” gift for the user to unravel, Ohh the excitement — I can’t wait!

An allegedly simple touchup along with a minimalistic avatar icon — fused together into an elegant, clever and simple-looking microinteraction residing in a very static or idle screen of Facebook Mobile App. This immediately prompts the observing user to interact with this UI element and discover its hidden virtues — a tailor-fit, properly designed and implemented call-to-action.

#### Approaching the Challenge

A simple analysis of the microinteraction makes it pretty clear — finding a similar or exact icon would be a relatively simple task while engineering a single “spark” effect would be the rather more complex part.

I invite you to jump on board my thought process “train” and share my experience in forming ideas, experimenting, and discovering insights along my path in accomplishing the desired end result.

I also hope you learn something new like I did by utilizing the CSS `clip-path` property to addresss this challenge learn its ins-and-outs.

Without further ado, let’s start :) I stepped forward to break the effect down into smaller, more manageable and intuitive mini challenges.

#### Clip?! path!? Elaborate…

`clip-path` is a CSS property that cuts away (clips) a region that sets which part of an element will be shown while the parts outside are hidden.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8XLc3ld-Y525EXEXM0GVFw.png)
_A developer using clip-path to make an intricate shape on his HTML Element_

`clip-path` allows us to create complex shapes with CSS by clipping an element into a certain shape (like circle, triangle, ellipse, polygon and more). We can further animate between shapes freely and receive eased-in transitions and morphing effects out of the box as long as both transitioned shapes have the same number of points (coordinates x,y).

![Image](https://cdn-media-1.freecodecamp.org/images/1*YD4oQHQ2egrRzMmt5RE4Nw.jpeg)
_Me experimenting with clip-path to create some basic shapes_

#### Animations Breakdown

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-LOwkghKd9GkopMQ-87GQ.gif)
_A single “Spark” effect in the microinteraction_

Focusing my attention on a single element made it much easier to dissect each animation being activated. And so, I determined the following:

1. `transform: scale(...)` — Is easing from 0 to 1 and back to 0 along the animation life cycle.
2. `transform: rotate(180deg)` — it took a bit more time for me to realize that the rotation of this ninja-star to a square and back is a total of 180 degrees (from its appearance phase to its end position, in which the Spark also vanishes).
3. `clip-path: polygon(...)` — This part would pretty much be one of the more complex and interesting challenges within this single Spark Effect Challenge — therefore, I will discuss it further with much more detail below.

#### Scaling — A Building Block of the Spark Effect

Timing the scaling of the element has a crucial part in contributing to the “sparkliness” of the effect, as the swift appearance and vanishing of the element is pretty much what a spark is composed of — abrief shiny visit that provides a temporary pleasure to our eyes.

#### Roatation — Blurring the lines, a “Glue” for the Spark Effect

Along with the scaling transition, when the element first appears and immediately starts to rotate from left to right, the rotation makes it more lively and holistic. This forces the human eye to focus on the icon decorated by this shiny or sparkly feeling.

#### The Pure CSS way of Morphing Shapes — Clip Path: Polygon(…)

With certain limitations, this is the “Native” way of achieving a morphing effect for CSS shapes.

**Known Issue** — the first, most important limitation that has to be clear for us developers before we approach this technology is that **_the number of coordinates in the beginning shape and end shape has to be equal_** _—_turning a **square** to a **rectangle** is a perfect, simple use that works seamlessly with the technology.

#### Experimenting

To be perfectly honest, this is the pretty much the first time I’ve utilized `clip-path:Polygon()` in a real work-related use-case. So I decided to venture on with some experimenting to better understand its in-and-outs before approaching the specific challenge at hand.

#### Experiment 1 — A Naive Approach — Square → 4-Point Star

![Image](https://cdn-media-1.freecodecamp.org/images/1*38mBJrncsiHh40Fuvwx-IA.gif)
_Square → 4-Point-Star Morphing on hover_

Wow, it’s only my first experiment and I am already thrilled about `clip-path` :) although something quite peculiar had happened here… The morphing direction seems to be behaving weirdly. The reason is simple: the origin shape had a total of 8 coordinate points, 4 of them stacked on each corner coordinate, thus leading to this weird morph behavior.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oMZJ7iaRv_3SAKlFAYXjEg.png)
_2 points(coordinates) stacked on each corner → 8 equally spread points along the square sides_

A few steps further into experimenting I discovered this wonderful tool and utilized it to start working with percentages rather then pixles. I also was able to edit my shapes online with it. Overall I highly recommend giving it a try — this is [Clippy](http://bennettfeely.com/clippy/)!

#### Experiment 2 — Adjusted Morph Directions — Square → 4-Point Star

According to my plans, the following gif shows a simplified approach I took to try solving this issue with a 200px by 200px square:

![Image](https://cdn-media-1.freecodecamp.org/images/1*xwmNJXP4QN2QrxwAK2NtZA.gif)
_Planning the morphs step by step frames_

A simple coordinate tweak — spreading 4 of the stashed points equally across the square (between the corners) — would hopefully lead to a smoother morph effect and to the right direction (vertically & horizontally respectively) aiming towards the center of both shapes rather then the diagonal direction as before:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kjOmqppHr_MoMDpn1OCvcg.gif)
_Aha Success! — The Morphing effect looks decent now_

#### Experiment 3— Octagon → Square

![Image](https://cdn-media-1.freecodecamp.org/images/1*u68nanh5vvWV4dmAsQheOA.gif)
_Single Spark Element — slowed down to see the Octagon and Square Phases_

If we look carefully and repeatedly at the single spark effect above, we briefly notice that somewhere about 50% through the animation it turns to an octagon. Furthermore, in the phases before and after the Octagon, the spark morphs to a square.

Seems like quite a simple task doesn’t it? I thought I’d just use `clip-path` to morph my previous square to an octagon like the gif above. Reality was a bit different, and I had to change the initial shape and draw its `polygon(...)` a bit differently to have the square within the octagon when transitioning.

The way `clip-path` operates is it creates the desired clipping region within the element using the property and as my original square took up the entire region of its element. I could not morph outside this region with the current coordinates allocation.

A few adjustments had to be made — and I also shifted to work with percentages now to support dynamic width/height of the shapes from the parent element.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R2ql3FAJtLylpK4V2sQAxg.png)

And voilà — we made some progress and now we have an Octagon that transitions to a square and back. But wait…we are not done yet!

![Image](https://cdn-media-1.freecodecamp.org/images/1*MDva1WbMHIRuxCANGBZieg.gif)
_Breathing Octagons are real?!_

#### Experiment 4— Octagon → 4-Point Star → Back (Full Cycle)

Now that we know that the Octagon is the biggest appearance of the morphing shape, we can make our morphing shape much more accurate and transition between its actual phases of 4-point-star → Octagon → Back, as seen below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1ZtJRj1QvfFvQ-lZRx7Og.gif)
_That’s more like it_

#### Experiment 5— Scaling & Infinite Loop Animation

So I began this experiment with first moving from the hover event to an instantly triggered infinite animation that first uses the `scale(...)` transformation to make the star appear and disappear respectively as seen below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BWGVRte7rRLVrjTLBE2qHA.gif)
_Now you see me, now you don’t — demo [here](https://codesandbox.io/s/j4z7nvzwry" rel="noopener" target="_blank" title=")_

#### Experiment 6— Rotate, Begin & End Positions

A few more tweaks to make the star scale up to full size in the beginning position and determine its final position with `transform:rotate(180deg)`

![Image](https://cdn-media-1.freecodecamp.org/images/1*gpufiV_12HvEM-iPFz1xxw.gif)
_It’s-A Rotating, Mario! — demo [here](https://codesandbox.io/s/m4x0kq0l3y" rel="noopener" target="_blank" title=")_

#### The Border Challenge

After some time spent experimenting, I realized that what I had accomplished so far would not be satisfactory. In the original example, it seems that when the sparks appear above the icon in the original microinteraction, they have some sort of white border along the shape that is morphing along with the shape through each step of its `keyframes`:

![Image](https://cdn-media-1.freecodecamp.org/images/1*6wOJDPVpnvhvqKDgfiduoA.png)
_A bit enlarged — but it is clear that borders are present along the morphing_

#### Experiment 6 — Building a Border that Morphs along with the Spark

After searching for solutions across the internet, stack overflow and other suggestions in articles to approach the issue, I understood that this challenge was quite unique. I could not find any specific solutions to my problem. The fact that my border had to “stick” to the shape while it morphs complicated matters even more. So I ventured on to make a few test until I found the solution.

A “spark-clone” that is rendered just before my main sparkle element as a sibling element was the perfect solution. Both had to be `display: flex` and vertically as well as horizontally positioned to the center of their wrapper with `justify-content: center` and `align-items: center` to achieve the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NSlCryrtCHNCt0jC0IDDqQ.png)

But Johnny wait! How are you going to make sure the clone follows its brother during the morphing `keyframes` animation? After trying to animate the parent and child simultaneously and experiencing some weird browser issues or bugs, I found that the siblings approach with `flex` provided the best solution as seen below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*4osoHSZSO9invJ75Yl0meA.gif)
_Siblings animating simultaneously created a perfectly adjusting border — demo [here](https://codesandbox.io/s/q3yw5lo8zq" rel="noopener" target="_blank" title=")_

### Connecting the Dots

At this point in time, I already felt that the difficult challenges in this project had come to an end. All I had to do now was find a similar avatar icon, position 3 sparks, adjust their positions manually until I was satisfied, and adjust their width/height as well until I reached the end result.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jUA3DHCHZrCrGe-ZOFiUdw.gif)
_An enlarged version to better see how things work_

![Image](https://cdn-media-1.freecodecamp.org/images/1*YiRlChFNIRnavHfpHqO8uA.gif)
_The final Microinteraction — demo [here](https://codesandbox.io/s/z3x7vl176m" rel="noopener" target="_blank" title=")_

### Summary

To wrap things up, I enjoyed challenging myself with re-creating this microinteraction. I learned a whole lot about how a seemingly simple element in our daily lives (like a invitation to click a new icon from the developers of a software we consume) is actually much more then just a set of elements and animations perfectly timed and properly oriented.

Such a tailor-fit microinteraction is a work of art. It is a unique UI element that is carefully designed to solve a hard problem. In our case, the developers at Facebook altered my mobile app’s navigation bar, removed an icon I did not use often, and replaced it with an icon that allowed me to perform an action I had been struggling to find and desired to take many times — going back to my profile.

It is a clever decision, a masterly crafted microinteraction that resides inside a static screen. It is the only moving part of the screen, and although very minimal and relatively small in the screen, the shiny sparkling stars across the icon’s margins lured my eyes and my finger to automatically click it. Now I appreciate the work and thought behind it even a bit more — so thank you Interaction Designers and Frontend Developers in Facebook for building such awesome microinteractions!

### Conclusion

I encourage you all to dare and try solve hard UI and UX problems through ideation and experimentation. Although it is nice and might be a bit ego-enhancing to reach the end result and succeed, I think it is the less significant part of the experience.

In my eyes, the journey you venture on through, equipped with your skillset of experimenting, thinking, and consulting with others is the best part. The learning and insight gathering processes you experience are much more important, to put it simply, and mean way more then the destination.

#### Reviewers

Thanks a whole lot for the help of these great people who helped review and give feedback for my article drafts, you’re amazing! ;) — [Jared M. Spool](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined) [Yoni Weisbrod](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined) [Ofir Ovadia](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined) [Dima Vishnevetsky](https://www.freecodecamp.org/news/how-facebook-designs-microinteractions-for-feature-discovery-c79cfe998a77/undefined)

### Now What?

I would appreciate feedback, claps, shares. You can of course find all the code, demo & a live sandbox to play around with as well as organized API docs for convenience of use [right here](https://codesandbox.io/s/z3x7vl176m).

More Recommended Posts by me about **Product Design, UX & Frontend**:   
[Medium Clap Recreated in Vanilla JS](https://medium.com/@yonatandoron/how-i-implemented-the-medium-clap-from-scratch-4a16ac90ad3b) — A full Walkthrough Guide  
[Star Rating — Make SVG Great Again](https://uxdesign.cc/star-rating-make-svg-great-again-d4ce4731347e)— A step-by-step code tutorial

More **Vue Components**:  
[Vue Dynamic Dropdown](https://github.com/JonathanDn/vue-dropdown) — A Customizable, easy-to-use elegant dropdown  
[Vue Dynamic Star Rating](https://github.com/JonathanDn/vue-stars-rating)— A dynamic vue star rating component(similar to google play)

I am Jonathan Doron, a Web Developer with great passion for User Centric Frontend, and modular client architecture.

What thrills me these days is exploring the ocean of **Interaction Design** more specifically of **Micro Interactions** and their impact on our lives. I do it by recreating existing interactions as well as designing my own interactions as part of my quest to deepen my knowledge in the field.

You are welcome to follow, tweet or message me freely with any questions, feedback or suggestions!— [Twitter](https://twitter.com/jodoron)

