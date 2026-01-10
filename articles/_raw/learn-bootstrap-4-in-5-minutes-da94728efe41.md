---
title: Learn Bootstrap 4 in 5 minutes - A quick tutorial to get you started
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-14T06:44:43.000Z'
originalURL: https://freecodecamp.org/news/learn-bootstrap-4-in-5-minutes-da94728efe41
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caf76740569d1a4caad90.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Per Harald Borgen

  Get to know the newest version of the worlds most popular front-end component library.

  In January 2018, Bootstrap 4 (aka v4) finally got released after being in alpha
  for over two years. It represents a major rewrite. Not only ar...'
---

By Per Harald Borgen

#### Get to know the newest version of the worlds most popular front-end component library.

In January 2018, Bootstrap 4 (aka v4) finally got released after being in alpha for over two years. It represents a major rewrite. Not only are there a lot of changes under the hood, but there are also a few new concepts you’ll need to wrap your head around.

So in this tutorial, I’m going to explain the most important changes from Bootstrap v3 to v4. I’m assuming that you’ve used Bootstrap previously, so I won’t explain the basics.

You can also check out our [free course on Bootstrap 4 on Scrimba.](https://scrimba.com/g/gbootstrap4?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article)

[**Want to learn Bootstrap 4? Here’s our free 10-part course. Happy Easter!**](https://medium.freecodecamp.org/want-to-learn-bootstrap-4-heres-our-free-10-part-course-happy-easter-35c004dc45a4)

Now let’s have a look at the most important changes (in no particular order):

### #1: Flatter buttons

Let’s begin with a fun and visual one! The buttons in v4 have a flatter design than they did in v3. Here are the previous buttons:

![Image](https://cdn-media-1.freecodecamp.org/images/1*i8bry1W2D-UpvXbxAMqEbg.png)

And here are some of the new ones:

![Image](https://cdn-media-1.freecodecamp.org/images/1*2-33MrQ3wRls06JBzwZyiw.png)

This is more in line with more modern design guidelines like those found in [Material Design](https://material.io/guidelines/), which has become hugely popular in the last couple of years.

### #2: The media queries are better

Bootstrap v3 had too few breakpoints for its grid, in my opinion, as the lowest one, `xs`, was at 768 px. A lot of traffic usually comes from screens narrower than that, so this has been frustrating for many developers.

So now they’ve added a new breakpoint, `xl`. This one takes the role `lg` used to have, and pushes the rest of the breakpoints downwards, making the range go all the way down to **576 px**.

```css
$grid-breakpoints: (  xs: 0,  sm: 576px,  md: 768px,  lg: 992px,  xl: 1200px) !default;

```

This makes it easier for you to construct grids which work well across _all_ screen sizes.

### #3: Flexbox support gives you more flexibility

The famous Bootstrap grids are now created with Flexbox instead of floats. At first sight, this doesn’t make a huge difference for you as a developer, as most grid layouts work exactly the same. However, it does open up a few more possibilities.

Previously, you had to define the width of each column (from 1 to 12). Now you can define the width of _one_ column, and then let the other ones be automatically set by Flexbox.

Here’s an example of doing exactly that:

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzGaj8UK6SglmB_9J4l5VQ.png)

As you can see in the markup below, we’re only setting the width of the middle column to be 6 (which equals half of the full width) and then the rest of the columns will simply take up whatever space remains.

```html
<div class="container">  
  <div class="row">    
    <div class="col">1 of 3</div>
    <div class="col-6">2 of 3 (wider)</div>    
    <div class="col">3 of 3</div>  
  </div>
</div>

```

#### Flexbox classes

Bootstrap 4 also comes with a bunch of classes you can apply to control both Flexbox containers and items. To turn an element into a Flexbox container, simply give it the class of `d-flex`.

```css
<div class="d-flex">I'm a flexbox container!</div>

```

Which will give you a Flexbox container with text inside it:

![Note: I’m only mentioning the Flexbox related styles here.](https://cdn-media-1.freecodecamp.org/images/1*UT4MqiVppkBzSaNed4EmVg.png)

  
Note: I’m only mentioning the Flexbox related styles here.

Let’s also add a few items, and add another class to control how they’ll position themselves in the container.

```html
<div class="d-flex `justify-content-center"`">  
  <div>Flex item</div>  
  <div>Flex item</div>  
  <div>Flex item</div>  
</div>

```

Which makes the items centre themselves in the container:

![Image](https://cdn-media-1.freecodecamp.org/images/1*IqLdXmIHaH2ele21hCISgA.png)

You can also add classes on the items themselves. Check the [Flex section](https://getbootstrap.com/docs/4.0/utilities/flex/) in the docs to learn more about that.

### #4: Control spacing with classes

This one is pretty cool. You can now control the padding and margins using the `p-*` and `m-*` classes. The range goes from 0.25 rem to 3 rem through applying the numbers from 0 to 5.

For example, let’s give our Flexbox container a `p-5` class, in order to create as much padding as possible:

```html
<div class="d-flex p-5">I'm a flexbox container!</div>

```

Here’s how that will look:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BFcE6XXy_x9mV8R7zBVy3A.png)

You can also add `t`, `b`, `r` og `l` if you want spacing on specific sides (top, bottom, right, left), like this:

```html
<div class="d-flex pl-5">I'm a flexbox container!</div>

```

That will only add padding on the left side, like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*QmKsaoU7zpx753Po4bFOSw.png)

Note: the original flexbox container actually had a `_p-2_` class by default.

### #5: From pixels to rems

Bootstrap 4 has swapped out pixels with relative units of measurements (rems) in all places except media queries and grid behaviours. This means more flexibility and responsiveness, as rem units aren’t absolute, which pixels are.

With `rems` all font sizes are relative to the root element (the `html` tag), and by default, `1rem` equals `16px`. However, if you change the font-size to, say, 50% in the root element, then `1rem` will equal `8px` throughout the app.

Note that this switch doesn’t mean that you need to use `rems` when you’re applying your own styles on your website.

### #6: Cards replace panels, wells, and thumbnails

Bootstrap also comes with a whole new component called cards, which replace [panels](https://getbootstrap.com/docs/3.3/components/#panels), [wells](https://getbootstrap.com/docs/3.3/components/#wells), and [thumbnails](https://getbootstrap.com/docs/3.3/components/#thumbnails). A card is a flexible and extensible content container. It includes options for headers and footers, a wide variety of content, contextual background colours, and powerful display options.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYPC0IHtsW6d6WMYYQ9_OQ.png)

### #7: Goodbye IE9

Bootstrap v4 has dropped support for IE8, IE9, and iOS 6. v4 is now only IE10+ and iOS 7+. For sites needing either of those, use v3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jnuoJeC371Sd9_ClrOiO_w.jpeg)

There are of course many more changes which didn’t make it into this article, so check out the [Migration section](https://getbootstrap.com/docs/4.0/migration/) in the docs to see all the changes.

Finally, if you want to learn Bootstrap v4 properly, be sure to [check out our free course on Scrimba.](https://scrimba.com/g/gbootstrap4?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article)

Also, when you’ve gotten this far, feel free to connect with me via Twitter:

Thanks for reading! My name is Per, I’m the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article), and I love helping people learn new skills. Follow me on [Twitter](https://twitter.com/perborgen) if you’d like to be notified about new articles and resources.

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_5_minute_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbootstrap4_5_minute_article)_

