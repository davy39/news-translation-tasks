---
title: How to understand CSS Position Absolute once and for all
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:30:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-css-position-absolute-once-and-for-all-b71ca10cd3fd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3ydATM3NxrGI8Bz0T6NWXQ.gif
tags:
- name: code
  slug: code
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Marina Ferreira

  Stop losing your elements on the screen by understanding how an object figures where
  it is supposed to sit


  Positioning an element absolutely is more about the element''s container position
  than its own. To be able to position itsel...'
---

By Marina Ferreira

#### Stop losing your elements on the screen by understanding how an object figures where it is supposed to sit

![Image](https://cdn-media-1.freecodecamp.org/images/UiuGXOBbEzwyUMEnynyr4s8mfhpGIds2RQCo)

Positioning an element absolutely is more about the element's container position than its own. To be able to position itself, it has to know which parent div it’s going to position itself relative to.

The code below shows four nested divs. `.box-1`to `.box-3`are centered by `display: flex` and `margin: auto` only. `.box-4` doesn't have `margin` set, and it sits in its default position in the document flow.

```
<body>  <div class="box-1">    <div class="box-2">      <div class="box-3">        <div class="box-4"></div>      </div>    </div>  </div></body>
```

The `position` property is unset to all elements.

```
body {  display: flex;}
```

```
.box-1,.box-2,.box-3 {  display: flex;  margin: auto;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/u9GyvXp81914z3hJb5bSL3rcjE62v4ZKOnIn)
_.box-4 default position_

To be able to position itself, an element has to know two things:

* coordinates for its `x` and `y` position set by either `top`, `right`, `bottom`, `left`
* which parent it’s going to position itself relative to

On applying `position: absolute` to `.box-4` the element is removed from the `[normal document flow](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Normal_Flow)`. Since its coordinates are not set, it simply stays at the default position which is its parent div of upper left corner.

![Image](https://cdn-media-1.freecodecamp.org/images/fGJYLQ7rKPWPOZj3qzsp-nxyBUvTRbiSfMYe)
_.box-4 position absolute without offset._

By setting `top: 0` and `left: 0` the element then has to know which parent it will consider as a reference point. To be a reference, the element has to be positioned to the screen with `position: relative`. `.box-4` then starts asking its parent divs if they are positioned. At first, it asks `.box-3` and gets `No, I am not positioned.` as an answer. The same goes for `.box-2` and then `.box-1` , since all of them have `position: unset` .

As `.box-4` was unable to find a positioned parent, it positions itself relative to the `body`. That element is always positioned to the screen:

![Image](https://cdn-media-1.freecodecamp.org/images/tjeIL8YkyGBlzTpwCapPcQTfOptpdBXzWc2U)
_.box-4 position absolute. Parent divs position unset._

If we set `position: relative` to `.box-1` , when `.box-4` asks it: `Are you positioned?` it gets `Yes I am.` as an answer. And then `.box-4` will be positioned relative to `.box-1` :

![Image](https://cdn-media-1.freecodecamp.org/images/OgWq2g7Wm468076IPANHhE7HIYODqUQkUpAv)
_.box-4 position absolute, .box-1 position relative._

The same goes for `.box-2` and `.box-3` .

**The absolutely positioned element will position itself relative to the nearest positioned ancestor.**

As soon as it finds a positioned ancestor, the position of the elements above that one is no longer relevant. The images below show the layout on setting `position: relative` to `.box-2` and `.box-3` , respectively:

![Image](https://cdn-media-1.freecodecamp.org/images/rBN0SYpLuSJUUnxJMPu4N0TguV3gNYBQ30Vr)

![Image](https://cdn-media-1.freecodecamp.org/images/eYzaYiMTTqnqSqZHYIs3g6q6uVbOmO0GX6IN)
_.box-4 position absolute, .box-2 and .box-3 position relative, respectively._

You can also find a video explanation at [Code Sketch Channel](https://youtu.be/VFt_n4M9Vyk) ?.

Thanks for reading! ✌️

_Originally published at [marina-ferreira.github.io](https://marina-ferreira.github.io/tutorials/css/position-absolute/)._

![Image](https://cdn-media-1.freecodecamp.org/images/qKShNDloz66ZcWplME6mkPXlYDLYUhs6bxsC)

