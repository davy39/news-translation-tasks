---
title: CSS Specificity Explained By Hopelessly Shopping for New Clothes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-15T04:52:15.000Z'
originalURL: https://freecodecamp.org/news/css-specificity-explained-by-hopelessly-shopping-for-new-clothes-92bade5f2e5b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Cmd1yXcbw-hv3lb1AEenMA.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever wandered into a department store or other clothing store, then
  you can understand how CSS selectors apply their styles.

  If you are a beginner to CSS, you have probably seen plenty of scenarios already
  where CSS sty...'
---

By Kevin Kononenko

If you have ever wandered into a department store or other clothing store, then you can understand how CSS selectors apply their styles.

If you are a beginner to CSS, you have probably seen plenty of scenarios already where **CSS styling rules conflict.** You think that you just added a new style to an element, but after refreshing the browser many times… you realize that the style is not being applied for some reason.

Here’s an example. Let’s say that you have a general rule that all paragraph tags should have a line-height of 140%, like this.

```
p{   line-height:140%; }
```

But, you also want to create a `subtitle` class that will have a line-height of 120%, which will usually apply to paragraph elements.

```
.subtitle{   line-height:120%; }
```

So, which one will apply when you assign it like so?

```
<p class="subtitle"> This is a subtitle</p>
```

The answer is the _s_`ubtitle` class styling, but I want to find a better way to explain the rules behind this logic. You don’t want to open the Inspector every time you are unsure which styling is more specific..

Here’s a scenario to help: imagine you are a salesperson in a department store or other clothing store. You get paid based on how many pieces of clothing you sell over the course of the day, so you need to spend your time with the best customers if you want to make the most money.

![Image](https://cdn-media-1.freecodecamp.org/images/0*72O7r9E5Nvxkaglc.)

The customers that look most likely to buy get **precedence**. The customers that come in with a specific idea of what they want are more likely to buy.

CSS operates in a similar way. It will give precedence to the most specific styles, which will override less-specific styles. The most common ways to add style are:

* Element level (`p` tag)
* Class level (`.subtitle`)
* ID
* In-line styling

Here is how to tell which of the selectors above are most specific. In each case, the customer is looking for a tailored suit, and you must sell as much clothing as possible.

### Element Selectors — Only Having a Vague Idea

Have you ever wandered into a department store with only a vague thought, like “I need a suit for an event next week.”?

From personal experience, I can tell you that this is a great way to get stuck in the store for hours, trying on random suits. Anyway, these types of customers will take the longest time to find something they like. They will need to talk to a few people and try on multiple suits. Their mental image of what they want looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*medgGe7inXZjhhrj.)

Yeah, they have no idea what they want. They still need to pick a style, find their price range and then have you measure them so that you can tailor it.

This is the least-specific way of looking for a suit, and it is similar to the styling for a general type of element. Like this, a `div` with a black background:

```
div{   background-color:black; }
```

### Class Selectors — At Least You Know The Brand…

Okay, the next level above a general type of clothing is a brand. So, you might say that you like Ralph Lauren clothing, so you will start at the part of the store.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JAEsVtLxAOqcfOjv.)

(**Note**: This is not a Ralph Lauren display in the photo, just the only stock photo I could get)

This is better than searching all suits in the store, but it still means the customer is going to need to take a bit of time before they are willing to buy. Here is what the CSS looks like:

```
.ralphLauren{ }
```

That is more specific than a `div`, which is what we used in the example above. But, this CSS declaration could actually get more specific. Since we know that the customer is looking for a Ralph Lauren suit, let’s combine the element and the class. After all, Ralph Lauren could be any type of clothing, from boots to pants to shirts.

```
div.ralphLauren{ }
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*hSinWUd9x-BdU2NJ.)

This styling will override:

1. All general `div` styling
2. `ralphLauren` class styling when the class is being applied to a `div`.

That is because it is more specific by involving both an element and a class. So, if we have the following:

```
.ralphLauren{   background-color: black; } 
```

```
div.ralphLauren{   background-color:grey; }
```

The second declaration is more specific, so it will take precedence for all `divs` with class `ralphLauren`.

### ID Selector — They Know The Exact Model That They Want

The ID selector is almost as specific as you can get. It is kind of like the person that has done as much shopping online as possible, and come to the store with a printed picture of the suit they want.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IviYwcuWUEVHewYL.)

Yes, people still do this. Okay, maybe they have it as a saved link so they can open it up on their phone and show you, the salesperson.

Okay, I might do that sometimes.

Anyway, if the customer already knows the specific model of suit that he/she wants, you only need to measure their dimensions and then they will be ready to buy.

The [ID selector](https://www.w3schools.com/css/css_syntax.asp) is only meant to be used for one element on the entire page, which is much more specific than class- or element-level selectors. Here is an example of suit model `RL123` that the customer picked out before even meeting you:

```
#rl123{   background-color:navy; }
```

If the default color for Ralph Navy suits is grey, this statement means that the particular model actually has a navy color.

A quick note on scalability: you do **not** want HTML elements with custom IDs and styling all over your page. This will become a giant pain to maintain. You still need to use element and class-level styling to quickly create universal styles. But, you also need to know how to override these rules in individual cases.

### In-Line Styling — Customer Knows Their Model And Dimensions

This is the most specific way to do it, and also the least scalable. You can use **in-line styling** directly within the HTML element to override styles written in CSS.

This is kind of like the customer that comes to the store and not only knows the suit they want, but also knows their dimensions. They have a very specific idea of what they want, and they are ready to order the suit and leave the store as quickly as possible. This is great for a salesperson! So, it gets the highest priority.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DxVV0_pwLyFp4DwA.)

Here is what that looks like in terms of HTML.

We will assign the `**width**` and `**height**` attributes to the `div` with class `ralphLauren:`

```
<div class="ralphLauren" style="height:100px; width:100px"></div>
```

If we had assigned width and height in the CSS, as in the examples above, it would be over-written here.

### The Wild Card — !important

There is one other way to change the priority of style rules from CSS. I am not going to talk about it, though, because it should only be used in situations where there is no other alternative. It breaks all the rules we just made…

You can [read more about !important here](https://appendto.com/2016/04/css-important-rule-how-to-use-it-correctly/).

### Final Summary

Here is the order of specificity for different ways of applying styling:

![Image](https://cdn-media-1.freecodecamp.org/images/0*0KoWiUMj7yRS4Uln.)

### Get More Visualized Coding Tutorials

Did you enjoy this tutorial? Give it a “clap” so others can discover it too.

Or sign up for my latest tutorials [here](http://www.codeanalogies.com/):

