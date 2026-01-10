---
title: Learn Bulma CSS in 5 minutes - A tutorial for beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T10:00:36.000Z'
originalURL: https://freecodecamp.org/news/learn-bulma-in-5-minutes-ec5188c53e83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-rRVJ7pa3DUFN4Bul4e_CA.png
tags:
- name: CSS
  slug: css
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  Bulma is a simple, elegant, and modern CSS framework that a lot of developers prefer
  over Bootstrap. Personally, I think Bulma has a better design by default, and it
  also feels more light-weight.

  In this tutorial, I’ll give you a...'
---

By Per Harald Borgen

Bulma is a simple, elegant, and modern CSS framework that a lot of developers prefer over Bootstrap. Personally, I think Bulma has a better design by default, and it also feels more light-weight.

In this tutorial, I’ll give you a super quick introduction to the library.

We’ve also created a free Bulma course. [Click here to check it out!](https://scrimba.com/g/gbulma?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbulma_5_minute_article)

![You can click the image to get to the course](https://cdn-media-1.freecodecamp.org/images/1*5XEOKibPcmV1oPB4ZFxNsg.png)
_[You can here to get to the course.](https://scrimba.com/g/gbulma?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbulma_5_minute_article)_

### The setup

Setting up Bulma is super easy, and you can do it in several different ways, whether you prefer [NPM](https://www.npmjs.com/package/bulma), downloading it directly [from the docs](https://bulma.io/), or using a [CDN](https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css). We’re just going to link to a CDN from our HTML file, like this:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css">

```

This will give us access to the Bulma classes. And that’s actually all Bulma is - a collection of classes.

### Modifiers

The first thing you should learn about Bulma is the modifier classes. These allow you to set alternative styles to almost all of the Bulma elements. They all start with `is-*` or `has-*`, and then you replace the `*` with the style you want.

To understand this concept properly, let’s start off by looking at buttons.

### Buttons

To turn a normal button into a Bulma button, we’ll simply give it the class of `button`.

```html
<button class="button">Click here</button>

```

Which results in the following style:

![Image](https://cdn-media-1.freecodecamp.org/images/1*03TOy6dVBDCPvrlardUBHw.png)

As you can see, it has a nice flat design by default. To change the styling, we’ll use Bulma modifiers. Let’s start off by making the button bigger, green, and with rounded corners:

```html
<button class="button **is-large is-success is-rounded**">Click here</button>

```

This result is a pleasant-looking button:

![Image](https://cdn-media-1.freecodecamp.org/images/1*3p5bTMdQbPYx_DeNQo7sgA.png)

You can also use modifiers to control the state of buttons. Let’s, for example, add the class `is-focused`, which adds a border around it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*mk04rubImZHTpMNPhsn-TQ.png)

Finally, let’s also use one of the `has-*` modifiers. These typically control what’s inside the element. In our case, the text. Let’s add `has-text-weight-bold`.

Here’s the result:

![Image](https://cdn-media-1.freecodecamp.org/images/1*H30F0Q92eL_IGipfEE3lWg.png)

I’d recommend that you play around with combinations of the various classes in order to understand how flexible this system is. The combinations are almost endless. Check out the [buttons section](https://bulma.io/documentation/elements/button/) in the docs for more info.

### Columns

At the core of any CSS framework is how they solve columns, as that’s relevant for almost every website you’ll ever build. Bulma is based on Flexbox, so it’s really simple to create columns. Let’s create a row with four columns.

```html
<div class="columns">  
  <div class="column">First column</div>
  <div class="column">Second column</div>
  <div class="column">Third column</div>
  <div class="column">Fourth column</div>
</div>

```

First, we’re creating a container `<div>` with a class of `columns`, and then we give each of the children a class of `column`. It results in the following:

![I’ve also added a border around the columns to make them more apparent.](https://cdn-media-1.freecodecamp.org/images/1*p0XiWjzp00GGdgrmrCtwYA.png)

  
I’ve also added a border around the columns to make them more apparent.

Note that you can add as many columns as you want. Flexbox takes care of dividing the space up equally between them.

To give the columns colours, we can replace the text inside them with a `<p>` tag, and give it the `notification` class and an `is-*` modifier. Like this for example:

First column

Let’s do this using the `is-info`, `is-success`, `is-warning` and `is-danger` modifiers, which results in the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*7c9Ygeq5NbrBYQfnVUFDwA.png)

The `notification` class is actually meant for alerting users about something, as it allows you to fill the background with a colour using the `is-*` modifiers. Here it works well for separating the columns.

We can also easily control the width of a column. Let’s add the `is-half` modifier to the green column.

```html
<div class="column is-half">    

```

Which results in the second column now occupying half the width, while the three other takes up a third of the remaining half each.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2oogxdeNyRZ7Y9oxLXNqBg.png)

Here are the options you can use for controlling the width of columns:

* `is-three-quarters`
* `is-two-thirds`
* `is-half`
* `is-one-third`
* `is-one-quarter`
* `is-four-fifths`
* `is-three-fifths`
* `is-two-fifths`
* `is-one-fifth`

### Hero

Finally, let’s also learn how to create a hero in Bulma. We’ll use the semantic `<section>`, and give it a class of `hero` and `is-info` to give it some colour. We also need to add a `<div>` child with the class `hero-body`.

```html
<section class="hero is-success">  

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*mRUKo5nMrlRmNRlFhFxXqA.png)

In order to make this hero do something meaningful, we’re going to add a container element inside the body and add a title and subtitle.

```html
<div class="container">
  <h1 class="title">Primary title</h1>
  <h2 class="subtitle">Primary subtitle</h2>
</div>

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*zgiaCn1QmbMn-r4d-p9exA.png)

Now it’s starting to look good! If we want it to be bigger, we can simply add `is-medium` on the `<section>` tag itself.

```html
<section class="hero is-info is-medium">  ...</section>

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7jJFSeUFbzSuavVUpVV7Zw.png)

And that’s it!

You’ve now gotten a basic taste of how Bulma works. And the best part is, the rest of the library is as intuitive and easy as the concepts you’ve seen up until now. So if you understand this, you’ll understand the rest of it without trouble.

Be sure to check out the [free Bulma course on Scrimba](https://scrimba.com/g/gbulma?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbulma_5_minute_article) if you want to learn more!

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbulma_5_minute_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbulma_5_minute_article)_

