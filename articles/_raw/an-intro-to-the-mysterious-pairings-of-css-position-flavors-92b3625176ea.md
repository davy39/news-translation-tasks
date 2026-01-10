---
title: An introduction to the mysterious pairings of CSS position flavors
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-16T16:16:20.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-the-mysterious-pairings-of-css-position-flavors-92b3625176ea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LLCPNx0V3gV4bhsPgjR0Xw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anabella Spinelli

  Ever since I started learning about web development I found CSS positioning to be
  a mixture of mysterious co-dependant properties whose interactions and influences
  I never quite understood. Like most newbies, I just juggled aroun...'
---

By Anabella Spinelli

Ever since I started learning about web development I found CSS positioning to be a mixture of mysterious co-dependant properties whose interactions and influences I never quite understood. Like most newbies, I just juggled around with `position`, `display`, `float`, `clear`, and all of their possible combinations of values until it looked like what I wanted.

That’s how CSS works, right?

Now, after some years of focusing on API testing, I wanted to revisit that old vanilla CSS and try to really understand those basic layout properties, while I try to figure out what the cool kids are doing these days and jump back on the dev train.

This is my first stop: position.

#### Getting to know the properties

The `position` property can be a mysterious thing to run into when you’re starting to learn about CSS. It’s like being given a set of unknown spices that look similar, but have very different flavours and the combinations between them don't always work like expected.

This is an attempt to describe the best and most common _pairings_ between them so that you can easily apply them in your first web cooking steps. Just like we learn in the kitchen — parsley goes well with garlic, but not that much with cinnamon.

First of all, let’s define what each of the position variants tastes like:

* `static`**:** this is what every HTML element has by default. It means the element will be positioned according to the **normal document flow.** It’s basically the _salt_ of them all.
* `relative`**:** elements with relative position can be placed _relatively_ to the space they would occupy in the normal document flow. They’re still part of the document flow, but support `top, right, bottom and left` properties. Whatever values you assign to those properties will be calculated using it’s natural position and boundaries as reference. Like adding some pepper, it doesn’t do much harm.
* `absolute`**:** this one’s tricky — it’s sort of like cumin, it can be a very good addition, but you have to use it carefully. Absolute elements are **removed from the normal document flow**. This means they don’t affect and aren’t affected by other elements in the page. However, they will be placed _relatively_ (yes, I know, bear with me) to their nearest `positioned` ancestor. This means whichever parent element that has its _position explicitly set._ It can be fine tuned using `top, right, bottom and left`. So it’s similar to relative positioning, but, since it’s no longer part of the document flow, it uses a parent as the reference.
* `fixed`**:** ah, this one’s easy. Fixed elements are not part of the document flow and their position is based on the whole window, sometimes referred to as _viewport_. Also, they’re not affected by scrolling.

#### So, how can we mix them?

Use `position:` relative**;** whenever you want to offset an element a little bit from where it would normally be, but you don't want everything else to move with it. Remember that all other elements will behave as if it hasn’t moved.

Use `position: absolute**;**` when you care about where the element is in relation to its parent or wrapper with a position, in this example, `relative`. Note for this that the `position` property does not cascade, so this will use the nearest parent with an _explicit relative_ declaration. If you want to force cascading of this property, you can declare it as `position:` inherit;.

Keep in mind that this element’s position is defined by the size and shape of its relative parents, so if you change that, this element might be affected too.

Finally,`position: fixed;` is a funny thing to play around with. Normal usages include sticky navbars, footers, or side menus. Remember it’s out of the normal document flow, so this means:

* you can place it wherever you want and nothing else will break
* it also means that it won’t do anything else you don’t explicitly tell it to do, so you need to set its 2 coordinates for it to show up at all.
* these 2 coordinates (namely, `top` or `bottom`, plus `left` or `right`) will be measured from the edge of the window.

There is another option I didn’t cover: `position: sticky`. This makes elements behave and scroll normally but then stick to a certain position while the rest of the content keeps on scrolling. I decided to leave it out, because it’s still experimental and exceeds the _understand the basics_ scope of this article. But, if you’re curious, [here’s](https://alligator.io/css/position-sticky/) a link showing what it’s all about.

_I hope you enjoyed the read and learned something along the way. If you have any comments or feedback, I’d love to read them ._

