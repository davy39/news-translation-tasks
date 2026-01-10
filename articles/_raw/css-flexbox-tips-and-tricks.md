---
title: CSS Flexbox Tips and Tricks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-30T17:55:00.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-tips-and-tricks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e5f740569d1a4ca3cc0.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
seo_title: null
seo_desc: 'CSS Flexbox allows you to easily format your HTML like you never knew was
  possible. With Flexbox you can align vertically and horizontally, easily. Like the
  sound of that? Yeah, so do I.

  Flexbox is also super useful when you''re creating the general l...'
---

CSS Flexbox allows you to easily format your HTML like you never knew was possible. With Flexbox you can align vertically and horizontally, easily. Like the sound of that? Yeah, so do I.

Flexbox is also super useful when you're creating the general layout of your website or app. It is easy to learn, well-supported (in all modern browsers) and is great to work with – not to mention it doesn’t take long to get the basics.

So let's dive right in and learn more.

## **Flexbox**

Here is a list of the Flexbox properties that can be used to position elements in CSS:

### **CSS that can be applied to a container**

```text
display: flexbox | inline-flex;
flex-direction: row | row-reverse | column | column-reverse;
flex-wrap: nowrap | wrap | wrap-reverse;
flex-flow: <‘flex-direction’> || <‘flex-wrap’>
justify-content: flex-start | flex-end | center | space-between | space-around;
align-items: flex-start | flex-end | center | baseline | stretch;
align-content: flex-start | flex-end | center | space-between | space-around | stretch;
```

### **CSS that can be applied to items/elements in a container**

```text
order: <integer>;
flex-grow: <number>; /* default 0 */
flex-shrink: <number>; /* default 1 */
flex-basis: <length> | auto; /* default auto */
flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
align-self: auto | flex-start | flex-end | center | baseline | stretch;
```

So now you have your toolkit. But you might ask “What do I do with my tools, and how do I use them?” Well, let me show you.

### **Display Flex**

`display: flex;` just tells your browser, "hey I would like to use Flexbox with this container, please." This will initialize this box as a Flex container and apply some default Flex properties.

This is what our container looks like without `display: flex;`:

![CSS playground no flex properties](https://discourse-user-assets.s3.amazonaws.com/original/2X/8/8f20f30d24cba9a7f56bf950a3f23d37d356ca51.png)

After adding `display: flex;` we get the below – you can see that the default Flex properties are applied causing it to look like this:

![CSS playground display flex default style](https://discourse-user-assets.s3.amazonaws.com/original/2X/6/66404664f9177ae748be00f769faf67d5956034d.png)

### **Flex Direction**

`flex-direction:` allows us to control how the items in the container are displayed. Do you want them left to right, right to left, top to bottom or bottom to top? You can do all this easily by setting the Flex direction of the container.

Flexbox applies rows as the default for the direction. Here is what they all look like:

`flex-direction: row;`

![flex-direction: row; example](https://discourse-user-assets.s3.amazonaws.com/original/2X/9/951cc993820547efa28e70dca905f5531a4488d5.png)

`flex-direction: row-reverse;`

![flex-direction: row-reverse example](https://discourse-user-assets.s3.amazonaws.com/original/2X/c/cf738aaf83f29eccdb461e91b775b10e41b92389.png)

`flex-direction: column;`

![flex-direction: column example](https://discourse-user-assets.s3.amazonaws.com/original/2X/7/7ef77565bc07ee86fd3033a531dd76b49709cf7e.png)

`flex-direction: column-reverse;`

![flex-direction: column-reverse example](https://discourse-user-assets.s3.amazonaws.com/original/2X/e/ec9a1ec064bf0027fa61016ca620df14d9bd47a9.png)

### **Flex Wrap**

Flexbox by default will try to fit all elements into one row. But you can change this with the flex-wrap property. This allows you to choose whether the elements will spill over or not. 

There are 3 properties for `flex-wrap:`:

`flex-wrap: nowrap` is the default and will try to fit everything in one row from left to right.

`flex-wrap: wrap` allows items to go on to create multiple rows from left to right.

`flex-wrap: wrap-reverse` allows items to be on multiple rows but displays right to left this time.

### **Flex Flow**

Flex flow combines the use of `flex-wrap` and `flex-direction` into one property. It is used by first setting the direction and then the wrap.

`flex-flow: column wrap;` is an example if how to use this.

### **Justify Content**

`justify-content` is a property that aligns items in the container along the main axis (this changes depending on how content is displayed). 

There are multiple options for this. It allows us to fill any empty space in rows but lets us define how we want to ‘justify’ it.

Here are our options when we justify our content: `flex-start | flex-end | center | space-between | space-around;`.

### **Align Items**

Align items allows us to align items along the cross-axis. This allows content to be positioned in many different ways using justify content and aligns items together.

`align-items: flex-start | flex-end | center | baseline | stretch;`

### **Align Content**

This is for aligning items with multiple lines. It is for aligning on the cross-axis and will have no effect on content that is one line.

`align-content: flex-start | flex-end | center | space-between | space-around | stretch;`

## Other resources on Flexbox and Grid

### Articles and courses

[The Ultimate CSS Flex Cheatsheet](https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/)

[Full CSS Video Course (Includes Flexbox and Grid)](https://www.freecodecamp.org/news/full-css-course-flexbox-grid/)

[A Visual Guide to CSS Flexbox](https://www.freecodecamp.org/news/do-you-even-flex-box-c16449cfca96/)

[How to Create an Image Gallery with CSS Grid](https://www.freecodecamp.org/news/how-to-create-an-image-gallery-with-css-grid-e0f0fd666a5c/)

### Games and Apps

[Flexbox Defense](http://www.flexboxdefense.com/) is a web game that teaches flexbox the fun way.

[Flexbox Froggy](http://flexboxfroggy.com/) is also a web game that teaches flexbox the fun way.

[Flexbox in 5](http://flexboxin5.com/) is a web app that allows you to be able to see how flexbox works with a few simple controls.

[Flexyboxes](http://the-echoplex.net/flexyboxes/) is an app that allows you to see code samples and change parameters to see how flexbox works visually.

[Flexbox Patters](http://www.flexboxpatterns.com/) is a website that shows off loads of flexbox examples.

### Videos

[Flexbox Essentials](https://www.youtube.com/watch?v=G7EIAgfkhmg)

[Flexbox Practical Examples](https://www.youtube.com/watch?v=H1lREysgdgc)

[What The Flexbox?!](https://www.youtube.com/watch?v=Vj7NZ6FiQvo&list=PLu8EoSxDXHP7xj_y6NIAhy0wuCd4uVdid)

