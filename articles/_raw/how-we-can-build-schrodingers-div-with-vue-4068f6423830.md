---
title: How we can build Schrödinger’s div ? with Vue!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T19:26:33.000Z'
originalURL: https://freecodecamp.org/news/how-we-can-build-schrodingers-div-with-vue-4068f6423830
coverImage: https://cdn-media-1.freecodecamp.org/images/1*spoAQtMm1OBMU1iciAZmzg.png
tags: []
seo_title: null
seo_desc: 'By ZAYDEK

  There’s a 50% chance we’ll get this right…

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I created
  a short questionnaire to che...'
---

By ZAYDEK

#### There’s a 50% chance we’ll get this right…

Before I get to the article, I just want to share that I’m building a product, and I would love to collect some data about how to better serve web developers. I created a [short questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) to check out before or after reading this article. Please check it out — thanks! And now, back to our regular scheduled programming.

![Image](https://cdn-media-1.freecodecamp.org/images/JzU2vsqeYVGGDIMtAFHsrXZ9AgC0-bVH7fwi)

### Hello Internet!

You probably don’t know who I am *cough* I’m [Zaydek](https://twitter.com/username_ZAYDEK) *cough* but I know who you are! You’re an aspiring, budding web developer interested in learning some new technologies, but a bit hesitant because frameworks come and go, and JavaScript is well.. JavaScript! To put it lightly.

So please allow me a few minutes of your time to make a convincing argument for why learning Vue could be a great decision. You should learn it not only for your qualifications, but for the pure fun and glee that comes with learning a well-documented and orchestrated piece of software.

#### I also teach how this ? works and a whole lot more in the Vue course I just released. Learn Vue from the basics and how to build a few things, too! C[lick here to enroll for free!](https://scrimba.com/g/glearnvue)

![Image](https://cdn-media-1.freecodecamp.org/images/Q5mqNqLWLYLhNAOUrVSXEdB7JggDGgdVn-el)
_[Click to enroll in my free Vue course!](https://scrimba.com/g/glearnvue" rel="noopener" target="_blank" title=")_

#### [Scrimba.com](https://scrimba.com/g/glearnvue) is a new and interactive website for learning and sharing how to code. Screencasts can be interrupted and edited, making learning active and fun to experiment with!

### Hello, Felix!

[Schrödinger’s cat](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat) is a morbid thought experiment posited by Albert Einstein and Erwin Schrödinger to mock the absurdity of quantum physics. It’s an (in)conceivable experiment for which randomness at a micro-level can be measured in the macro-world we experience. Ironically, it has become a centerpiece for explaining quantum physics!

You can learn more about the experiment and its origins [here](http://nautil.us/issue/41/selection/how-einstein-and-schrdinger-conspired-to-kill-a-cat).

It goes something like this: You have a cat. You put it in a sealed box. In the box is placed some radioactive material that over an hour has a 50% chance of one if its atoms ionizing. Also placed in the box is a Geiger counter, which is a measuring device. If it detects an ionized atom, it will release a hammer that will smash a vial of poison thus killing the cat! ??

Here’s a more academic explanation of Schrödinger cat:

> The scenario presents a cat that may be simultaneously both alive and dead, a state known as a quantum superposition, as a result of being linked to a random subatomic event that may or may not occur …

> … Schrödinger did not wish to promote the idea of dead-and-alive cats as a serious possibility; on the contrary, he intended the example to illustrate the absurdity of the existing view of quantum mechanics.

> — [Wikipedia](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat#Origin_and_motivation)

And this is what we are going to build using Vue! ? It won’t be that hard, but we are sort of cheating because we’ll be relying on JavaScript’s pseudo-random facilities and not ionized atoms!

For this course, you should know some JavaScript and some HTML. But [in the course I just released](https://scrimba.com/g/glearnvue), I dedicate 10 minutes to teaching the absolute basics of JavaScript needed to get up and running with Vue! [So don’t forget to enroll!](https://scrimba.com/g/glearnvue)

### Building Schrödinger’s div

![Image](https://cdn-media-1.freecodecamp.org/images/eGCUyk4FWzRswbeA6e4YCbYCVOl8y2sFOBdE)

![Image](https://cdn-media-1.freecodecamp.org/images/fixclM1DbhaY4DQOXdmV5GwDgeTTzZUaTqao)

![Image](https://cdn-media-1.freecodecamp.org/images/NUcSEKbB1PCj4JBoAL5ZYK5pn8Ksokcd7VMv)
_Click to roll the dice.. ?_

Using Vue, we can bind a click handler to a `span` — I lied, it’s not a `div` — containing the `?,` and selects from either the ? `o`r ? `em`ojis. Clicking it calls a function that emulates throwing dice, and reveals whether our cat lived or died. And clicking again could reset the state back to the original closed-box. This can all be achieved with Vue’s v-h`tml, @`cl`ick, a`nd :cl`ass at`tributes.

![Image](https://cdn-media-1.freecodecamp.org/images/DsQgm6XM86dxM4PN93SJQYGwwTvjSojOKnJ4)

Psst.. the full code is available in the [eighth screencast](https://scrimba.com/p/pZ45Hz/ceJ3vUL).

Inside of `<div id="ap`p"> is a p that `shows Click the box! The ca`ts…?! Also inside the p `is a` span with a few attribu`tes. v`-html `and emoj`ify() are techniques I’m using to show emojis as images.

`@click="quantum_fluctuation()"` is how I’m attaching a function to the `span` being clicked, and `:class="jittering()"` — also `:class="theme()"` — make for subtle special effects.

Let’s now understand how `quantum_fluctuation()` works: when called, it invokes JavaScript’s `Math.random()` to influence the state of our cat, which is initialized to `?,` and selects from either ? `o`r ? `em`ojis.

Bear in mind, I’m obfuscating a few details for the bigger picture, that being that we have our cat’s state, for example `this.cat`, stored in data, and that a function call sets `this.cat` state, which also gets updated in the DOM.

You can of course learn more about the implementation of `this.cat`, `rand()`, `this.alive_cats`, `this.dead_cats`, `this.is_open()`, and `this.is_alive()` in the [corresponding screencast](https://scrimba.com/p/pZ45Hz/ceJ3vUL).

To touch on how the `:classes` work, these return JavaScript objects that bind normal CSS classes based on the state of our app. And this is a big deal, because it means our CSS can be thought of as alive. Whaaaaat!!

![Image](https://cdn-media-1.freecodecamp.org/images/3hm9upv14BeozAJasRDO4UwONrkjP71HClaY)

The overarching point is that it’s now conceivable — and sensible — for a sole individual to create web-based products and services that emulate the snappiness of modern native apps, all without the same technical debt. And this is a big deal because while native apps are nice, they do require extra steps and often access to dozens if not one hundred MB to download. ?

#### There’s a lot more to learning Vue, so I wrote two more articles on the subject matter. Please, after this article, have a look!

![Image](https://cdn-media-1.freecodecamp.org/images/v82fTM9hJAhq4n2RC6euR6jsEq2758k-cDzx)

![Image](https://cdn-media-1.freecodecamp.org/images/evKfsXXPPpeztne9a8Xkjs89D6zUu5MxKFkq)
_Left: “[ow to make a ? color picker with Vue!” ](https://medium.freecodecamp.org/learn-vue-js-in-our-free-course-85d5df41e47f" rel="noopener" target="_blank" title="">Learn Vue.js in this free course! ?✨”</a> Right: “H<a href="https://medium.freecodecamp.org/how-to-make-a-color-picker-with-vue-9640043b6c82" rel="noopener" target="_blank" title=")_

### Vue is a superpower disguised as a framework

I love software that creates meaningful value — and not just for the end-users, but also for the developers who choose to learn and use it. Well-documented and orchestrated software feels great to learn, and feels even greater when the developer-experience is on par with the desired user-experience. Vue is no exception here, and programming Vue has been a blissful experience, and much easier than anticipated.

I refused to learn JavaScript for a long time because, coming from high-performance, concurrent and static programming languages, I had grown comfortable with a general disregard for JavaScript. However, having learned me some Vue, what’s so appealing is that Vue provides an idiomatic guide to programming in JavaScript, therefore lessening the burden and teaching good programming practices, too.

Now is a time like no other to get into web development. With the introduction of CSS Flexbox and Grid, web design has become at least an order of magnitude easier, more fun, and more powerful. With backend languages like Go, and delightful frontend frameworks like Vue, one programmer/designer can now do what would have required entire teams or companies in the past.

#### So please, go out into the beautiful world and learn you some Vue! You can(!) make amazing things and even change people’s lives, even your own. And if it helps, [try the free course](https://scrimba.com/g/glearnvue)!

![Image](https://cdn-media-1.freecodecamp.org/images/K4EgWlAYcUSuINupYvMFrERMz5OmPnwS4J-V)

