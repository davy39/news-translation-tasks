---
title: Learn CSS Flexbox in 5 minutes - A tutorial for beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-13T18:21:53.000Z'
originalURL: https://freecodecamp.org/news/learn-css-flexbox-in-5-minutes-b941f0affc34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SDah34Yygu4CkLUcdsSytQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Per Harald Borgen

  A quick introduction to the popular layout module

  In this post, you’ll learn the basics of CSS Flexbox, which has become a must-have
  skill for web developers and designers in the last couple of years.

  We’ll be using a navbar as a...'
---

By Per Harald Borgen

#### A quick introduction to the popular layout module

In this post, you’ll learn the basics of CSS Flexbox, which has become a must-have skill for web developers and designers in the last couple of years.

We’ll be using a navbar as an example, as this is a very typical use case for Flexbox. This will introduce you to its most-used properties of the module while leaving out the ones which aren’t as critical.

I’ve also created a free 12-part course on Flexbox. [Check it out here](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article) if you’re interested!

Now let’s get started!

### Your first Flexbox layout

The two main components of a Flexbox layout are the **container** and the **items**.

Here’s the HTML for our example, which contains a container with three items:

```html
<nav class="container">  
  <div>Home</div>  
  <div>Search</div>  
  <div>Logout</div>  
</nav>

```

Before we turn this into a Flexbox layout, the  elements will be stacked on top of each other like this:

![I’ve added a little bit of styling, but that has nothing to do with Flexbox.](https://cdn-media-1.freecodecamp.org/images/1*egtZCVQirK8mJiacL98eBA.png)

  
I’ve added a little bit of styling, but that has nothing to do with Flexbox.

To turn this into a Flexbox layout, we’ll simply give the **container** the following CSS property:

```css
.container {  
    display: flex;  
}

```

This will automatically position the items nicely along the horizontal axis.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DMA-NUgXG15-qDBAnLu3tA.png)

If you want to check out the actual code, you can head over to [this Scrimba playground.](https://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article)

Now let’s shuffle these items around a bit.

### Justify content and Align items

**Justify-content** and **align-items** are two CSS properties which help us distribute the items in the container. They control how the items are positioned along the **main axis** and **cross axis**.

In our case (but not always) the main axis is horizontal and the cross axis is vertical:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SDah34Yygu4CkLUcdsSytQ.png)

In this article, we’ll only look at `justify-content`, as I’ve found to be using this one much more than `align-items`. However, in [my Flexbox course](https://scrimba.com/g/gflexboxhttps://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article), I explain both properties in detail.

Let’s center all the items along the **main axis** by using `justify-content`:

```css
.container {  
    display: flex;  
    justify-content: center;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*1NQGeHIcXFdlYsNwP-kuXQ.png)

Or we can set it to `space-between`, which will add space between the items, like this:

```css
.container {  
    display: flex;  
    justify-content: space-between;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rYctxBrNeO2019wscgaaQA.png)

Here are the values you can set for `justify-content:`

* flex-start (**default**)
* flex-end
* center
* space-between
* space-around
* space-evenly

I’d recommend you to play around with these and see how they play out on the page. That should give you a proper understanding of the concept.

### Controlling a single item

We can also control single **items**. Let’s say we, for example, want to keep the first two items on the left side, but move the `logout` button to the right side.

To do this we’ll use the good old technique of setting the margin to `auto`.

```css
.logout {  
    margin-left: auto;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z9GbnGBvlJdIYjiH3DQbbQ.png)

If we’d want both the `search` item and the `logout` item to be pushed to the right-hand side, we’ll simply add the `margin-left` to the `search` item instead.

```css
.search {  
    margin-left: auto;  
}

```

It’ll push the search item as far to the right-hand side as possible, which again will push the log out item with it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*C5bwvvQjhgnrufVNo4jfwA.png)

### The flex property

So far, we’ve only had fixed-width items. But what if we want them to be responsive? To achieve that we have a property called `flex`. It makes it a lot easier than the old way of using percentages.

We’ll simply target all the items and give them a `flex` value of `1`.

```css
.container > div {  
    flex: 1;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*fI8C475J2qbF5LMu82voEQ.png)

As you can see, it stretches the items to fill the entire container.

In many cases, you’d probably want one of the items to take up the extra width, and thereby only set one of them to have flexible width. We can, for example, make the `search` item take up all the extra space:

```css
.search {  
    flex: 1;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7nmqNtWDHHh7pCgsUAUXfw.png)

Before we end this article, I want to mention that the flex property is actually a shorthand three properties: **flex-grow**, **flex-shrink** and **flex-basis**. However, learning those takes more than five minutes, so it’s outside of the scope of this tutorial.

If you’re interested in learning them, though, I’m explaining all three properties thoroughly in [my free Flexbox course.](https://scrimba.com/g/gflexboxhttps://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article)

Now that you’ve learned the basics you’ll definitely be ready to take my full-length course and become a Flexbox master!

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.comhttps://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gflexbox_5_minute_article)_

