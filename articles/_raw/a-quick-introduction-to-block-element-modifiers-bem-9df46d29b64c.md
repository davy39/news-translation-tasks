---
title: A quick introduction to Block Element Modifiers (BEM)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T15:31:39.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-block-element-modifiers-bem-9df46d29b64c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-ffATZSCMSAXm82epzuzxA.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Michael Ozoemena

  Hi there! So you want to gain a better understanding of BEM? I guess if you are
  reading this, you may not know what BEM stands for. In case you don’t, it’s an abbreviation
  for Block Element and Modifier.

  What is BEM?


  BEM is a des...'
---

By Michael Ozoemena

Hi there! So you want to gain a better understanding of BEM? I guess if you are reading this, you may not know what BEM stands for. In case you don’t, it’s an abbreviation for [**B**lock **E**lement and **M**odifier](http://getbem.com/).

#### **What is BEM?**

> _BEM is a design methodology that helps you to create reusable components and code sharing in front-end development._ — getbem.com

This means that BEM is a system of methods that helps you write your HTML and CSS code so that it is simple to reuse and share with other parts of your code.

### **BEM in action.**

So now you know the definition of BEM, but you might not know how it looks or how it works. As I stated earlier, BEM is an abbreviation, so let’s take a look at each of those words and what they mean.

#### **Block**

A “block” refers to any entity that can stand alone and still make sense. Examples of blocks are `header`, `input`, and `checkbox`. Examples of things that are **not** blocks are header titles, an item in a list, or a label for a checkbox.

If we should remove the text that labels a radio input and put it on its own, it’ll no longer make sense.

Look at this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Buz2ehP8ELECMdgo4xbKUg.png)

If the part that’s outlined becomes separated into individual blocks, they would no longer make any sense to the user.

This is a true separation into blocks:

![Image](https://cdn-media-1.freecodecamp.org/images/1*KANbx3IJWy-IzffvXIzRnQ.png)

If I removed any one of these blocks and threw it away, the other block will still make some sense to the user. Though, in this case, it won’t be useful to the user because it’s a radio button instead of a checkbox.

It’s important to look at a block as any combination (or a single HTML tag) of several elements (or other blocks) in a way that it _makes sense to the user when placed alone._

#### **Elements**

An Element should be a little easier to understand now, since I explained it when I talked about **Blocks**. Those parts of a block which have no semantic meaning outside of the block are elements.

Let’s look at the this again:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Buz2ehP8ELECMdgo4xbKUg.png)

The highlighted parts are elements, because they help define what the block is.

The code for the screen-shot above would look something like this:

We have three elements that make up the `option` block: `option__text`, `option__radio-button`, `option__note`. Yet we could change one of these elements into a block of its own:

The element `option__note` is now a block `note`. That means that we could find `note` outside of the `option` block in a way that is useful to the user.

#### **Modifier**

A modifier is a flag that changes how a block or an element looks or behaves. For example:

![Image](https://cdn-media-1.freecodecamp.org/images/1*KQSkWS77mlkLqQTAspoUBA.png)

The two buttons are the same block, but they look different. The power BEM gives us lets us use the same block twice and still have them look very different.

Let’s see how the code for that looks:

By default, the button is white with a blue text. To get a variation, we add a `button--green` flag, which then makes the button green with a white text.

According to BEM rules, our flag `button--green` is having a “side-effect” that might lead to confusion which is the `box-shadow` property. Our flag does something that its name doesn’t tell us about. But that’s okay, because, in our little project, we will never have a green button with a `box-shadow`. If we ever do, we can break up the flag:

Now, when we need a green button with a box shadow, we’ll only add the `button--green` flag. The same thing applies to the `color` property.

### **Conclusion**

BEM is a very nice way to write and structure your HTML and CSS code. This guide doesn’t cover 100% of everything BEM, but it should be enough to give you a solid understanding of the methodology. You can [read more about BEM here.](http://getbem.com/)

I hope you learned something from this and that you have a better understanding of BEM and how it looks in the real world. If you do, don’t hesitate to leave a comment and a few claps.

Have any questions? You can send me a DM on twitter [@THEozmic](https://twitter.com/THEozmic).

