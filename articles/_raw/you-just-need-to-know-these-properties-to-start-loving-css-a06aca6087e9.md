---
title: You just need to know these properties to start loving CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T17:06:22.000Z'
originalURL: https://freecodecamp.org/news/you-just-need-to-know-these-properties-to-start-loving-css-a06aca6087e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OtuC8-aWUupuh70uJ4r-SQ.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Henry Tabima Giraldo

  Positioning things with HTML and CSS can be a real headache when you’re new in frontend
  development. But in this post, I’m going to teach you how to solve most of the positioning
  problems. You only have to know these 3 CSS pro...'
---

By Henry Tabima Giraldo

Positioning things with HTML and CSS can be a real headache when you’re new in frontend development. But in this post, I’m going to teach you how to solve most of the positioning problems. You only have to know these 3 CSS properties.

I’m a developer with 3+ years of experience doing frontend. When I was learning, I thought what you’re thinking right now. Then I met flexbox, and positioning became easier than ever.

One of the best resources for learning flexbox is the [CSS Tricks guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). After continued use of this feature, I realized that, in most cases, you only need these three properties:

> display: flex;

> justify-content: $value;

> align-items: $value;

I’m going to borrow some images from the [above-mentioned guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). This way, I can make sure it’s easier for you to understand how properties work. Alright, let’s start.

#### Context

First of all, we need to set up a working context. When we are working with flexbox we have two kinds of elements, the **container**, and the **items inside said container,** as you can see in the images below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*uxhqPMGpDo6Z70taQXs1yQ.png)
_Image from CSS Tricks flexbox guide_

Now that you can differentiate between the container and its items, let’s make one thing clear: the three properties we are going to learn here **belong to the container**. A common mistake people make when they start with flexbox, is to set the following properties to their child elements.

#### display: flex

Alright, the first thing we need to do is set the `display` property of the container to `flex`.

With this property, you arrange the direct child elements of the container in a row (like in the images above).

#### justify-content

This property defines the alignment of the items along the main axis (horizontal axis). We can see the possible values and their results in the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*h1TPlhNbzNnAYmkpLyD-qw.png)
_Image from CSS Trick flexbox guide_

#### align-items

The third property is **align-items.** This property defines the default behaviour for the items along the cross axis (vertical axis). Now, let us see all the possible values this property has, and how they affect the elements inside the container.

![Image](https://cdn-media-1.freecodecamp.org/images/1*23_VYI-DBKGKA04Kjb3EHQ.png)
_Image from CSS Tricks flexbox guide_

With the previous properties, we were able to start positioning things right where we want them. But this post wouldn’t be complete without examples. For that reason, I’m going to show you some common use cases.

> Note: There is a property called flex-direction that swaps the direction of the main axis and the cross axis. Be aware when you’re using this property, and make sure you know what you’re doing.

#### Use Cases

As the first use case, we are going to see a simplified header navigation bar. Headers usually have an item on the left, another one on the right and sometimes one or more in the middle.

In this Codepen example, focus only on the CSS inside the selector called `.container`. All other styles are for giving a good look and feel. You should try experimenting with removing the item in the middle and then seeing what happens.

For the second use case, generally, you would want to centre an item inside its container. Now let’s see how we can accomplish that.

Again, check for the selector called `.container` and play around with the different values of those properties and see what happens.

#### Finally

Easy right? play around with these properties and see how they affect the elements, get used to them, and you will no longer have any problems while working with positioning.

Now that you have seen how to use flexbox in the most basic and useful way, I want to encourage you to learn more about this feature. You can read the [CSS tricks guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/), and play around with [Flexbox frogs](https://flexboxfroggy.com) or [Flexbox Zombies](https://mastery.games/p/flexbox-zombies). Those last two options can be an entertaining way to teach yourself the ins and outs of flexbox.

I hope this post helps you along your path. And I would love to hear from you; if you want to reach out, make sure you follow me on [Twitter as @HenryTabimaG](https://twitter.com/HenryTabimaG) and on [GitHub as @HenryTabima](https://github.com/HenryTabima). If you want any specific content for a post, feel free to ask.

Remember, if you liked this post leave some “claps”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fLar7VaMRxHzGdB3jYovVw.png)

