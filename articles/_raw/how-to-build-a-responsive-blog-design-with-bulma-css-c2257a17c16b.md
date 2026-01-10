---
title: How To Build A ? Responsive Blog Design With Bulma CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T19:56:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-blog-design-with-bulma-css-c2257a17c16b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FnvTa_zYybCdqG0dKQLq4Q.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By ZAYDEK


  Ooooooh

  How To Build A ? Responsive Blog Design With Bulma CSS

  ?‍‍ Thanks, Bulma!

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers...'
---

By ZAYDEK

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ZQC1eAhNoto4nw_R3PZvw.gif)

#### Ooooooh

# How To Build A ? Responsive Blog Design With Bulma CSS

#### ?‍‍ Thanks, Bulma!

Before I get to the article, I just want to share that I’m building a product, and I would love to collect some data about how to better serve web developers. I created a [short questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) to check out before or after reading this article. Please check it out — thanks! And now, back to our regular scheduled programming.

### Hello internet!

I’m here to disabuse you of the belief that building websites has to be hard. Furthermore, in mere minutes we mere mortals will learn how to build a beautiful and(!) responsive blog design using Bulma.

#### **Bulma?!** [Bulma](https://bulma.io/) is a CSS framework and brainchild of [@jgthms](https://jgthms.com/). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQHwKzcZaWbWrew33_bV4A.png)

#### I also taught a free, full-length Bulma CSS course on Scrimba.com, where we build these ️? designs. C[lick here to enroll for free!](https://scrimba.com/g/gbulma) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*MkSQUnosnWEuIIvoiUxadA.png)

#### [Scrimba.com](https://scrimba.com/g/gbulma) is a next-generation platform for front-end developers to record and share their websites as interactive screencasts! ?

### Bulma? ¯\_(ツ)_/¯

Bulma solves a lot of problems—a lot. Whether you need a visual component, or you want to understand [how a component might be codified](https://github.com/jgthms/bulma/tree/master/sass), with best practices and [best-in-class documentation](https://bulma.io/documentation/), Bulma’s here to help! ?‍?

Bulma’s not even version 1.0, and has major adoption with [150K+ downloads](https://github.com/jgthms/bulma/) a month and [26K+ stars](https://github.com/jgthms/bulma) on GitHub. Think of Bulma as a competitor to Bootstrap, despite the fact that it’s *just* CSS. ? Look ma, no Y[avaScript!](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript)

### How does Bulma work?

Bulma uses several techniques to create a cohesive interface for developers. We need just be concerned with describing our website’s design using semantic classes — not elements — or in other words, [idiomatic templates](https://bulma.io/documentation/overview/start).

These semantic templates can be thought of as interconnecting building-blocks we use to build websites fast! ⚡️ These components are also responsive out-of-the-box, meaning we can focus more on our content than the code.

#### Confused? Start ? h[ere](https://medium.freecodecamp.org/free-course-level-up-with-bulma-css-d82dcb4b980a) to first learn the fundamentals of Bulma.

### What about that ? design?

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ZQC1eAhNoto4nw_R3PZvw.gif)
_Want to learn how to build this 3D graphic in HTML and CSS? ? L[et me know! ](http://bit.do/subscribe-d82dcb4b980a" rel="noopener" target="_blank" title=")?_

This design can be better understood as **three** **parts**:

**☝️CSS Grid**  
**✌️ Bulma components**  
**? Content**

The [**CSS Grid**](https://en.wikipedia.org/wiki/CSS_grid_layout) spec is how we’re going to create a custom responsive design, where **Bulma components** give us useful templates and sections to compartmentalize our content, and **content** is…our content, of course! ?

### ☝️ CSS Grid

Despite that [Bulma is responsive](https://bulma.io/documentation/overview/responsiveness/) out-of-the-box, we’re going to instead opt for CSS Grid so that we maintain complete control of the responsive design. Afraid? Don’t be! Here’s a secret; it’s just 8 lines of human-readable code! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*wqj11kB213Tv71KbL8GYVw.png)

It goes like this: we create an opt-in `.grid` class for general-use, wherefore specific circumstances, where we want our content to stand out and be wider, we create a special `.grid-xl` class we can use on a per-element basis:

![Image](https://cdn-media-1.freecodecamp.org/images/1*eW7qDO0PdmJOUJvcLIgD8g.png)
_Whoa…that’s it? CSS Grid *is* magical! ??_

First, we template a responsive 5-column grid with identifiers `xl` and `md`. Then we tell `.grid *` to span the `md` column, e.g. the content column, and `.grid-xl` to span columns `xl`, e.g. all columns. ?️

Now, imagine creating various `.grid-sm`, `.grid-lg`, and etc. classes to extend different caveat widths. Think about it…this isn’t just concise or cool, it’s 100% modern responsive design. Look ma, no media queries!

#### Confused? You can learn more about CSS Grid ? h[ere](https://scrimba.com/g/gR8PTE) with Per!

### ✌️ Bulma components

[**Bulma components**](https://bulma.io/documentation/) are at the core of our design. Despite that it can be fun, we don’t have to write CSS from *scratch* to create a beautiful design. Instead, we can lean into successful frameworks to arbitrate components.

Now, because Bulma can be terse or difficult to understand at first blush, ? I’ve recreated the design using ASCII art to demonstrate how we might model the design using different Bulma components:

![Image](https://cdn-media-1.freecodecamp.org/images/1*WN-brZSHX68U0B8D_QeBJA.png)
_What if we could write code like this…??_

The truth is, Bulma is more terse, but that’s understandable given it’s HTML. Note I’m also obfuscating a few details to better emphasize how Bulma works. You can, however, [view this interactive screencast](https://scrimba.com/p/pV5eHk/cdkVWhq) to see the full code. ?

Take a second look; notice `.container (.grid)` and `.columns (.grid-xl)`? The first one, for example, would translate to `<div class="container gri`d">. This is *how* we can interpolate our grid with Bulma’s components!

You can learn more about Bulma’s components ? h[ere.](http://placeholder) In this blog design, we used s[ection,](https://bulma.io/documentation/layout/section/) c[ontainer,](https://bulma.io/documentation/layout/container/) b[readcrumb,](https://bulma.io/documentation/components/breadcrumb/) m[edia,](https://bulma.io/documentation/layout/media-object/) i[mage,](https://bulma.io/documentation/elements/image/) c[olumns,](https://bulma.io/documentation/columns/) and c[ontent.](https://bulma.io/documentation/elements/content/) And, despite that I’ve obfuscated it, we used m[odifiers,](https://bulma.io/documentation/modifiers/helpers/) too! ?

#### **Think of HTML as plastic, CSS as paint, and Bulma as LEGO. ?**

### ? Content

As promised, last is the **content** of our website. Of which belongs inside our `.content` component. Remember I said Bulma relies on opt-in classes? Well––that’s 99% of the time; inside `.content`, Bulma applies CSS to:

• `p` paragraphs  
• `ul`, `ol`, `dl` lists  
• `h1` to `h6` headings  
• `blockquote` quotes  
• `em` and `strong`  
• `table`, `tr`, `th`, `td` tables  
• [etc.](https://bulma.io/documentation/elements/content/)

And where Bulma shine️s ✨ is that `.content` can be paired with modifiers. These include `.is-small`, `.is-medium`, and `.is-large` to change `.content`’s children’s `font-size`! You can learn more about `.content` [here](https://bulma.io/documentation/elements/content/).

### Congratz! Thanks for reading! 6(^ω^)9

Now is a phenomenal time like no other to get into front-end development. With the introduction of CSS specs like [Flexbox](https://en.wikipedia.org/wiki/CSS_flex-box_layout) and [CSS Grid](https://en.wikipedia.org/wiki/CSS_grid_layout), and frameworks like [Bulma](https://bulma.io/), building for the web has never been more accessible!

#### Like this article?! There’s one more article just like it! Click ? h[ere!](https://medium.freecodecamp.org/how-to-build-a-responsive-tesla-launch-page-with-bulma-css-2bf484057349)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zQKHJaZS8s5iXvBBYP3FOg.png)

