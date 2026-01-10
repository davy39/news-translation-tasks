---
title: Learn This One Weird ? Trick To Debug CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T16:53:38.000Z'
originalURL: https://freecodecamp.org/news/heres-my-favorite-weird-trick-to-debug-css-88529aa5a6a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q6ap35H37-gXdR_ENdoxVg.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By ZAYDEK

  Designers HATE him! ?

  Learn This One Weird ? Trick To Debug CSS

  Not clickbait

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I c...'
---

By ZAYDEK

#### Designers HATE him! ?

# Learn This One Weird ? Trick To Debug CSS

#### *Not clickbait*

Before I get to the article, I just want to share that I’m building a product, and I would love to collect some data about how to better serve web developers. I created a [short questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) to check out before or after reading this article. Please check it out—thanks! And now, back to our regular scheduled programming.

Hi! ? I’m Zaydek! When I first set out to learn how to make websites, it was far more painful than anticipated. After all, I’m an experienced graphic designer and programmer — how could websites be t_hat_ hard?

In this article, I detail the decisions that led me to create a CSS debugger.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Czmfge5I4FvRyB4sJZD2RQ.png)
_[Click here](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") to open in Scrimba_

#### I also taught a [free HTML/CSS course](https://scrimba.com/g/gbuildablog) on Scrimba where I teach how to build a beautiful blog from *scratch*. [Click here to enroll!](https://scrimba.com/g/gbuildablog) ?

#### [Scrimba.com](https://scrimba.com/g/gbuildablog) is an interactive front-end platform where websites are recorded as events — not videos — and can be edited! ?

### What’s a debugger?

There’s a great Donald Knuth quote about debugging. To paraphrase, it goes something like this.

> Someone: “What’s the best programming language?”

> Donald Knuth: “Which one has the best debugger?”

I didn’t come to appreciate this idea until CSS. Programming languages have this reasonableness about them, where logic exceeds opinion. But CSS is different because CSS “feels” opinionated.

So what can we do? Well, we can listen to the good advice of Donald Knuth and use a debugger!

Where a programming language is a tool, a debugger is tooling we can use to understand our tool — our code. Not all comp-sci folk like debuggers, and I understand this.

Don’t make the computer do what we don’t understand. I think there’s merit in this, but what I’m talking about here is revealing structure where it was otherwise invisible.

Take the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BMu3HJzd4RAr7VHXEonMpA.png)
_[Click here](https://scrimba.com/c/c4vW9Hg" rel="noopener" target="_blank" title=") to open in Scrimba’s playground_

What can we do to see our website’s structure? Here are two solutions I’m aware of: we can make one-off CSS rules to emphasize an element, or we can use Chrome’s, Firefox’s, or Safari’s Debugger Tools. But that’s _still_ more-or-less a one-off solution. What we need is a **general** solution.

### Our debugger

Not long ago I was designing this header, and it wasn’t simple. The intent was to hover an image over multi-line text. Should be simple, right?

Well CSS is the antagonist ? here. What would otherwise be simple in Photoshop can be a hero’s journey in CSS, and this led me to experimenting with o`utline:`

```
* { outline: solid 0.25rem hsla(210, 100%, 100%, 0.5); }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*t_WJXVnw_bjWhXZI8kvB9w.png)
_[Click here](https://scrimba.com/c/cJMVJfM" rel="noopener" target="_blank" title=") to open in Scrimba’s playground_

Nothing too special—just soft-white lines. What we do have, however, is a rule that applies to all elements as long as we use an `*` and not the name of the `id`, `class`, or `element`.

Yet the introduction of the `* { … }` was profound for me. I thought, “Where would I not want this?” So I added a few more lines and developed a more formal debugger:

```
* {    color:                    hsla(210, 100%, 100%, 0.9) !important;    background:               hsla(210, 100%,  50%, 0.5) !important;    outline:    solid 0.25rem hsla(210, 100%, 100%, 0.5) !important;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*N3174yoUIeDpy6IDjkFfkA.png)
_[Click here](https://scrimba.com/c/c9kg4fZ" rel="noopener" target="_blank" title=") to open in Scrimba’s playground_

Much improved! Here we’ve created a schematic-like feel for our website. I was careful to not use solid colors, but instead chose soft-colors or colors with an alpha channel so that nested elements appear deeper in color, with **bluer** blues and **whiter** whites. I also added `!important` because of the infamous CSS [Specificity Wars](https://en.wikipedia.org/wiki/cascading_style_sheets#specificity).

What can sometimes feel like CSS screwing with us is how and when the cascade applies. That is, “How is it that styles are sometimes applied and sometimes not?”

This isn’t Schrodinger's CSS, it’s simple math. CSS uses a [simple calculator](https://specificity.keegan.st/) to determine which rules are more specific, and the result determines whether or not CSS is applied.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S_3XEtQfi_4W_3WPf7T7Ww.png)
_An [implementation](https://specificity.keegan.st/" rel="noopener" target="_blank" title=") of CSS’s specificity calculator_

The mother of all specificity is `!important`, which overrides all inline, IDs, classes, and element rules. [It’s like the Death Star as compared to The Empire](https://stuffandnonsense.co.uk/archives/css_specificity_wars.html). Despite the fact that the use of `!important` is discouraged in general, it’s perfect for a debugger — because we won’t ship our website with it “turned on.” Instead, we use the debugger just in the design and development of our website.

The more I used the debugger, the more I realized that using `*:not(path):noth(g)` as the selector was preferred. This way, I wouldn’t get extraneous lines from vector graphics. I also noticed that disabling `box-shadow` was cleaner, as the debugger doesn’t need a sense of depth.

So, here’s the final debugger:

```
*:not(path):not(g) {    color:                    hsla(210, 100%, 100%, 0.9) !important;    background:               hsla(210, 100%,  50%, 0.5) !important;    outline:    solid 0.25rem hsla(210, 100%, 100%, 0.5) !important;
```

```
    box-shadow: none !important;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*q6ap35H37-gXdR_ENdoxVg.png)
_[Click here](https://scrimba.com/c/cRVVPSD" rel="noopener" target="_blank" title=") to open in Scrimba’s playground_

I think _we_ humans hate what we don’t understand. And CSS is no exception. It’s mischaracterized because it’s misunderstood. I propose: **think of CSS as a double-edged sword. It can be used to both construct and deconstruct websites**. Yes, CSS is not Photoshop, but that doesn’t mean it can’t do things that Photoshop can’t. Creating our own debugger _is_ one thing we _can_ do.

### **How to use this debugger ?**

1. Go to [zaydek.github.io/debug.css](https://zaydek.github.io/debug.css)
2. Bookmark “Debug CSS” ([source code here](https://gist.github.com/zaydek/6b2e55258734deabbd2b4a284321d6f6))
3. Click the bookmark to toggle it *on* and *off* ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Yr09cqoVXljecLuZxclFw.gif)

#### Don’t forget the [free HTML/CSS course](https://scrimba.com/g/gbuildablog) on Scrimba where I teach how to build a beautiful blog from *scratch*. [Click here to enroll!](https://scrimba.com/g/gbuildablog) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Czmfge5I4FvRyB4sJZD2RQ.png)

