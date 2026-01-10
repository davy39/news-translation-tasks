---
title: How To Build A ? Responsive Tesla Launch Page With Bulma CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T19:24:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-tesla-launch-page-with-bulma-css-2bf484057349
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jEoG8kpxxBob8I_6ai4WRw.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By ZAYDEK


  0-60 in 1.9s ?

  How To Build A ? Responsive Tesla Launch Page With Bulma CSS

  To accelerate the advent of sustainable web design

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some ...'
---

By ZAYDEK

![Image](https://cdn-media-1.freecodecamp.org/images/1*nJPbo3jYDSo7JORmoMZpkQ.gif)

#### 0-60 in 1.9s ?

# How To Build A ? Responsive Tesla Launch Page With Bulma CSS

#### To accelerate **the advent of sustainable web design**

Before I get to the article, I just want to share that I’m building a product, and I would love to collect some data about how to better serve web developers. I created a [short questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) to check out before or after reading this article. Please check it out — thanks! And now, back to our regular scheduled programming.

### Hello internet! (Hi Elon!)

I’m here to disabuse you from the belief that building websites has to be hard. Furthermore, in mere minutes we mere mortals will learn how to build a beautiful and(!) responsive Tesla launch page using Bulma.

#### Bulma?! [Bulma](https://bulma.io/) is a CSS framework and brainchild of [@jgthms](https://jgthms.com/). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQHwKzcZaWbWrew33_bV4A.png)

#### I also taught a free, full-length Bulma CSS course on Scrimba.com, where we build these ️? designs. C[lick here to enroll for free!](https://scrimba.com/g/gbulma) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*MkSQUnosnWEuIIvoiUxadA.png)

#### [Scrimba.com](https://scrimba.com/g/gbulma) is a next-generation platform for front-end developers to record and share their websites as interactive screencasts! ?

### Bulma? ¯\_(ツ)_/¯

Bulma solves a lot of problems — a lot. Whether you need a visual component, or you want to understand [how a component might be codified](https://github.com/jgthms/bulma/tree/master/sass), with best practices and [best-in-class documentation](https://bulma.io/documentation/), Bulma’s here to help! ?‍?

Bulma’s not even version 1.0, and has major adoption with [150K+ downloads](https://github.com/jgthms/bulma/) a month and [26K+ stars](https://github.com/jgthms/bulma) on GitHub. Think of Bulma as a competitor to Bootstrap, despite the fact that it’s *just* CSS. ? Look ma, no Y[avaScript!](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript)

### How does Bulma work?

Bulma uses several techniques to create a cohesive interface for developers. We need just be concerned with describing our website’s design using semantic classes — not elements — or in other words, [idiomatic templates](https://bulma.io/documentation/overview/start).

These semantic templates can be thought of as interconnecting building-blocks we use to build websites fast! ⚡️ These components are also responsive out-of-the-box, meaning we can focus more on our content than the code.

#### Confused? Start ? h[ere](https://medium.freecodecamp.org/free-course-level-up-with-bulma-css-d82dcb4b980a) to first learn the fundamentals of Bulma.

### What about that ? design?

![Image](https://cdn-media-1.freecodecamp.org/images/1*MdW2WFa4Wi_rx_KLwcnLew.gif)
_Want to learn how to build this 3D graphic in HTML and CSS? ? L[et me know! ](http://bit.do/subscribe-d82dcb4b980a" rel="noopener" target="_blank" title=")?_

This design can be better understood as **three parts**:

☝️**Responsive background**  
✌️ **Bulma components + modifiers**  
? C**SS Grid**

Look a littttle closer…see something? The **background** isn’t continuous! ? This isn’t a mistake; the Tesla team optimized for desktop, tablet, and mobile. With that as our base, we’ll add B**ulma components and modifiers,** then use C**SS Grid** to achieve the intricate responsive design for the specs.

### ☝️ Responsive background

These are the **actual** background images I ??????? from tesla.c[om! ?‍☠️](https://www.tesla.com/roadster) Sooo…how do we build a responsive background? Using media queries, obvs! Media queries allow us to, given certain circumstances, override CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JzP04PS4J9ezcbeH0hlMqQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*OddPEy3sFCb-9PYQ5Y_zNQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*hPBa5yyxaI9K4ROCdJHNcg.jpeg)

And media queries are powerful; we can override CSS depending on the website’s rendered aspect ratio, the device’s aspect ratio, or simple-and-plain: the website’s rendered width. Yeah — let’s go with that.

First, we start with one of Bulma’s components, `.hero`, and use one of its modifiers, `is-fullheight`, to create a fullscreen section. Then, we assign various backgrounds for [common widths](https://bulma.io/documentation/overview/responsiveness/) using media queries:

![Image](https://cdn-media-1.freecodecamp.org/images/1*TOI29Yr3PqCc_GBkOJnVNA.png)
_1337 hax ?‍?_

Great — so now our website swaps backgrounds at `1024px` and `768px`. Sometimes when this happens, there’s a flash of white, so `black` conceals it. And `center` and `cover` just help align and focus the image.

Believe it or not, `background` is [shorthand for 8 CSS properties](https://developer.mozilla.org/en/docs/Web/CSS/background): ?

1.️ `background-clip`  
2. `background-color`  
3. `background-image`  
4. `background-origin`  
5. `background-position`  
6. `background-repeat`  
7. `background-size`  
8. `background-attachment`

We made use of `-color`, `-image`, `-position`, and `-size`!

### **✌️ Bulma components + modifiers**

This is where Bulma gets interesting. **Which one is the real launch page?!**

![Image](https://cdn-media-1.freecodecamp.org/images/1*JV4-eSj3Lqbwx-NijKOBsQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ctTD3MVhZA0i-ErZqbFMnA.png)
_Choose one; the red pill or the blue pill? ?_

…

…

…

**The left one is [authentic](https://www.tesla.com/roadster)!** ٩(;ʘ¿ʘ;)۶ Wait…how can Bulma be so versatile? Well — remember modifiers? Yeah so, with enough modifiers at our disposal, we can create a varied aesthetic, even without editing Bulma’s source.

Now, without further ado, I present the launch page as ASCII art! ??

![Image](https://cdn-media-1.freecodecamp.org/images/1*UTyZczNl2EoU6a9JjjAQ4w.png)
_What if we could write code like this…?_

You can ignore the IDs wrapped with parentheses for now. Other than that, these are a few of the available [Bulma components](https://bulma.io/documentation/). And imagine this, ? Bulma’s components are responsive, too! Whoa.

Bear in mind, this is far less terse than the actual implementation, [see here](https://scrimba.com/p/pV5eHk/c3E6PCb). I’m obfuscating modifiers and extraneous HTML to show how Bulma works; we link components together, just like LEGO, but to design a webpage!

And modifiers are how we can achieve a Tesla-like aesthetic, despite that Bulma has nothing to do with Tesla. Throughout [the code](https://scrimba.com/p/pV5eHk/c3E6PCb), notice the *extensive* use of `has-*` and `is-*`; this is what gives us a varied aesthetic.

#### You can click ? h[ere](https://bulma.io/documentation/) to learn more about Bulma’s components.

### **? CSS Grid**

Do we need CSS Grid? I’m not sure, （>﹏<） but I found programming the responsive design for the specs much easier than I anticipated using grid than some other technique. So, here’s where those IDs come into focus:

![Image](https://cdn-media-1.freecodecamp.org/images/1*6pNXOd66bj55SZJX34FkBg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fvpX6HYKnTYpuICtSixYvA.png)

Hehehe…so we have IDs `#a` through `#e`, with `#a` being some marketing, and `#e` being the “Reserve Now” button. The desired effect is that on mobile we sneak the “Reserve Now” button under `#b`, `#c`, and `#d`.

3…

2…

1… ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*7h9GZsbCFrA8yEQR1xrdbg.png)
_Huh? ? I was expecting something *harder*_

In the first slide, we assign identifiers to each of the IDs using `grid-area`. Then, we communicate to `#grid` the *shape* of our grid using ASCII art! ? This is the default grid; for desktop and tablet.

Last — remember media queries? YAS! All we need to do is to communicate the shape of our grid for mobile. Imagine this…we write a single media query to override the shape of our grid for mobile. ?⚡️

#### The full interactive code is available in the Bulma course ? h[ere.](https://scrimba.com/g/gbulma)

### Or…HOW ABOUT PORSCHE?!!? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*GY_GtCVBE0wQ0wShYBBVHA.png)
_Want to learn how to build this 3D graphic in HTML and CSS? ? L[et me know! ](http://bit.do/subscribe-d82dcb4b980a" rel="noopener" target="_blank" title=")?_

Nikita Rudenko [@rdnkta](http://twitter.com/rdnkta), who is new to #100DaysOfCode(!), created this after finishing the course, and shared it with me! Cheers! ?

### Congratz! Thanks for reading! 6(^ω^)9

Now is a phenomenal time like no other to get into front-end development. With the introduction of CSS specs like [Flexbox](https://en.wikipedia.org/wiki/CSS_flex-box_layout) and [CSS Grid](https://en.wikipedia.org/wiki/CSS_grid_layout), and frameworks like [Bulma](https://bulma.io/), building for the web has never been more accessible!

#### Like this article?! There’s one more article just like it! Click ? h[ere!](https://medium.freecodecamp.org/how-to-build-a-responsive-blog-design-with-bulma-css-c2257a17c16b)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zQKHJaZS8s5iXvBBYP3FOg.png)

