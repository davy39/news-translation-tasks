---
title: The CSS Box Model Explained by Living in a Boring Suburban Neighborhood
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-27T05:12:16.000Z'
originalURL: https://freecodecamp.org/news/css-box-model-explained-by-living-in-a-boring-suburban-neighborhood-9a9e692773c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HUxt-BY7c8cKk-w7_c_uzw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you’ve been to a normal suburban neighborhood, then you can understand the CSS
  Box Model.

  An experienced front-end web developer will tell you that an HTML layout is really
  just a series of boxes. These boxes stack on top of eac...'
---

By Kevin Kononenko

#### If you’ve been to a normal suburban neighborhood, then you can understand the CSS Box Model.

An experienced front-end web developer will tell you that an HTML layout is really just a series of boxes. These boxes stack on top of each other within their container boxes, and those container boxes stack on top of each other within an even larger container box, and then…

WOW. That is a lot of boxes within boxes. I don’t think I want to hear the word “box” for at least a week. Also, the box concept does not do a good job of describing margins and padding. These are the two biggest tools for creating evenly-spaced elements.

In reality, there is a little bit more nuance when it comes to arranging HTML elements. The CSS Box (gasp!) Model allows us to create well-balanced and easily readable content on our page.

The different pieces of the box model are kind of like a property in a typical suburban housing development. And if you can use them correctly, you can avoid hours of trial and error with fussy CSS.

If you are looking for a more technical explanation, the MDN has a [pretty good one](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model).

#### The Main Pieces of the Box Model

There are 5 important properties that allow you to size and distribute your HTML elements:

* Width
* Height
* Padding
* Border
* Margin

Here is what that looks like in a diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/1*t_3KFsT6HYd1Er9pEsv_1A.png)

Yikes! That is a way too many boxes for one element. Let’s take this back one step. There are actually three different zones here.

**Zone 1:** The height and width of the actual element. This is the house itself. In the diagram, this is 679 pixels by 63 pixels.

**Zone 2:** The territory around the element that is limited by the border. This is kind of like the yard and fence on your property. This is the **padding** and **border**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LnzBO4qp7vUuemk3wAu50g.png)

**Zone 3:** The empty space that separates this element from the surrounding elements. This is similar to the trees that are still technically part of your property, but give you some privacy from the neighbors and are just meant to give you a buffer. This is the **margin**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T9PFj7v8hFovBOR2qW0JYg.png)

Remember that every div, paragraph and header has these properties. It can get confusing pretty quickly when you have a series of elements stacked on top of one another, and you have no idea which elements contain the buffer space.

The difference between the margin and the padding is perhaps the **most challenging part**. The two are used for different reasons. As you can see with the green grass, the padding will still have a background color, if you choose to set it. This is also the property you want to change if you want to change the distance between the **border** and the **content.**

Let’s say you want to have a massive yard on the right side of the house, that would make the right border far away. You could change this with the **padding-right** property.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ftk23jdL-2RleJunow_l2w.png)

The **margin** property affects the space between elements. This is that empty space that is a sort of “no man’s land” where no development occurs. It is strictly meant for spacing out elements. Here are a couple houses in a row, some of which have larger or smaller margins.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YTc5r6C7lPX7NnhF8mFyJQ.png)

NOTE: Each of these stacked houses must have a display with a value of “inline-block”. Prevents [margin-collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing).

#### Some Real Examples

Alright, let’s use some real CSS! Imagine that you have a lot with the following attributes:

Here is what that would look like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*D-OE3BPohmmwIBVbZQpI7A.png)

A couple observations:

1. Notice how the background color only affects the pixels within the border. The margins are not affected by this property
2. When you declare margin and padding with one value, like 4px, CSS automatically applies the number to the top, bottom, left and right of the element.

Here is one last example. In this one, we will use two values when declaring padding and margin. The first value determines the top/bottom, and the second value determines the left/right value.

And here is the diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/1*7iDlw63sVwefTQqMzNzQSg.png)

If you enjoyed this post, you may also enjoy my [other explanations](https://www.rtfmanual.io/guides/) of challenging CSS, JavaScript and SQL topics, such as positioning, Model-View-Controller, and callbacks.

And if you think this might help other people in the same position as you, give it a “heart”!

