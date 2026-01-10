---
title: CSS Box Model Properties – Explained With Examples ✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-07-22T17:31:57.000Z'
originalURL: https://freecodecamp.org/news/css-box-model-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/FCC-Thumbnnail--2--1.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Today we're gonna learn how to use the CSS box model with examples. This\
  \ will help you make pixel perfect websites and will teach you to use the box-sizing,\
  \ margin, padding, and border properties more accurately. \nWe're also going to\
  \ see some practic..."
---

Today we're gonna learn how to use the **CSS box model** with examples. This will help you make pixel perfect websites and will teach you to use the box-sizing, margin, padding, and border properties more accurately. 

We're also going to see some practical use cases for these properties. Let's get started 💖

## Table of Contents

* **[Why learn CSS Box Model?](#heading-why-learn-css-box-model)**
* [CSS Box-Model Diagram](#heading-css-box-model-diagram)
* [The Padding Property](#heading-the-padding-property)
* [The Border Property](#heading-the-border-property)
* [The Margin  Property](#heading-the-margin-property)
* [The **box-sizing** Property.](#heading-the-box-sizing-property)
* [Content-box **VS** Border-box](#heading-what-is-the-difference-between-content-box-and-border-box-in-css)

![Topics covered: box model diagram, padding, border, margin, box-sizing, and shorthands](https://www.freecodecamp.org/news/content/images/2021/07/Frame-7--2-.png)
_**Topics covered**_

### You can watch this tutorial on YouTube as well if you like:

%[https://youtu.be/WJ8Yoi04XvQ]

## Why learn CSS Box Model?

![Why learn CSS box model?](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail.png)

The CSS box model comprises the **box-sizing, padding** and **margin** properties. If you **don't** use them, your website will look like this 👇

![A website with no margin or padding](https://www.freecodecamp.org/news/content/images/2021/07/Page-1-1.png)
_**A website with no margin or padding**_

But if you use the box model properties correctly, your website will look like this 👇

![Same image of website with padding and good use of other box model properties](https://www.freecodecamp.org/news/content/images/2021/07/Page-1--1-.png)
_**A website using box model properties**_

Much more visually appealing, right? If you want to make your website with accurate calculations, like the one above 👆 then this topic is for you. Learning about the CSS box model is one of many ways that will help you make **pixel perfect websites.**

This article will talk about how to use these properties:

* Padding
* Margin
* Border
* box-sizing

## How to Use CSS box-model Properties

Let's look at some examples of where we can use the properties of the CSS box-model. We're gonna dissect the website shown above. 👆

Let's have a closer look at the **navbar**. You can notice the difference between the example that uses the padding property and the one that doesn't: 

![Before and after of a navbar with and without padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-47.png)
_**Navbar items using the padding property**_

Now let's have a closer look to the **content section along with the buttons**. Again, you'll notice the difference – the right one is also using the **padding** property. 

![Before and after of content with and without padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-48.png)
_**A content section using the padding property**_

## CSS Box-Model Diagram

Think of the CSS box-model like an **onion**. It has **4 Layers**:

* **1st** layer: Content
* **2nd** layer: Padding
* **3rd** layer: Border
* **4th** layer: Margin

### 1st box-model layer: Content

In HTML, **everything behaves like a box**. Let's insert some content with a kitty image. 👇

![Cute cat image to demonstrate content within the box model](https://www.freecodecamp.org/news/content/images/2021/07/Frame-1--1--1.png)
_**1st layer of the box model: content**_

### 2nd box-model layer: Padding

The next layer of the CSS box model is the **padding** layer. It wraps our content like this 👇

![Same cute cat image above with padding around it](https://www.freecodecamp.org/news/content/images/2021/07/Frame-2-2.png)
_**2nd layer of the box model: padding**_

### 3rd box-model layer: Border

The next layer of the CSS box model is the **border** layer. It wraps our content + padding like this 👇 

![A border around the cat image above](https://www.freecodecamp.org/news/content/images/2021/07/Frame-3--1-.png)
_**The black dashed line is the border**_

### 4th box-model layer: Margin

The next and final layer of the CSS box model is the **margin** layer. It wraps our content + padding + border like this 👇

![Margin outside the cat image](https://www.freecodecamp.org/news/content/images/2021/07/Margin.png)
_**Grey Region is The Margin**_

Alright, let's see how these properties work in a project.

## How to Setup the Project

![Let's code together](https://www.freecodecamp.org/news/content/images/2021/07/Frame-8.png)

This tutorial is **good for everyone including beginners.** If you want to code along, then follow these steps. 

### HTML

Open VS Code or [Codepen.io](http://codepen.io/) and write this code 👇 inside the **body tag:**

```html
<div class="box-1"> Box-1 </div>
```

### CSS

Clear the default styles of our browser 👇

```css
* {
  margin: 0px;
  padding: 0px;
  font-family: sans-serif;
}

```

Now, let's style our box 👇

```css
.box-1 {
  width: 300px;
  background-color: skyblue;
  font-size: 50px;
}
```

We're all set, let's start coding! ✨

![Dog drinking a bubble tea](https://www.freecodecamp.org/news/content/images/2021/07/Frame-9.png)

## The Padding Property

But first, let's discuss the **practical uses** of the padding property. Then, we'll see how to use this property.

Generally, I use padding to put some space between contents. Look at this **navbar** 👇

![Navbar with padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-47-1.png)
_**Navbar items using padding property**_

Here's another example for you – look at the below content, with two buttons👇

![Content with padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-48-1.png)
_**content section using padding property**_

### How to use the padding property in CSS

This is the **shorthand** of the four padding properties:

* padding-top
* padding-right
* padding-bottom
* padding-left

![Padding shorthand](https://www.freecodecamp.org/news/content/images/2021/07/Frame-10.png)
_**Shorthand of padding property**_

And remember, padding is the space you add on top of your **main content**:

![Cat image showing padding](https://www.freecodecamp.org/news/content/images/2021/07/Padding.png)
_**2nd Layer of Box-Model : Padding**_

Let's add some padding to our content. **The red colored area is the padding 👇**

![The red colored area is padding](https://www.freecodecamp.org/news/content/images/2021/07/bmnmmmmm.gif)
_**The red colored area is padding**_

In order to recreate the results above, ☝ write this code in your CSS: 👇

```css
// Padding added on top, right, left, bottom of .box-1

.box-1{
   padding : 100px;
}
```

Let's open our developer console and **go to the computed section**:

![Dev console image of the box model and padding](https://www.freecodecamp.org/news/content/images/2021/07/a.png)
_**Computed CSS Box model**_

At the very middle is our **content** which is **300px** in width. Look around our content, we have added **100px padding** all around it. 

Let's try adding padding to just 1 side of our content (only the right side):

![Image showing padding-right](https://www.freecodecamp.org/news/content/images/2021/07/Frame-11--1-.png)
_**padding-right property**_

In order to recreate the results above, ☝ write this code in your CSS: 👇

```css
.box-1{
   padding: 0 100px 0 0;
}

// Or you can use 👇

.box-1{
   padding-right: 100px;
}
```

Now, open the computed section on your developer console 👇

![Dev console image showing padding-right](https://www.freecodecamp.org/news/content/images/2021/07/s.png)
_**Computed CSS Box model**_

Look – the padding of 100px has only been added on the **right** side of our content as we specified. 

## The Border Property

You'll commonly use the border property **while making buttons**. Here's a GIF demo 👇

![Image showing showing hovering a mouse over buttons to demonstrate the border property](https://media.giphy.com/media/iUTNdCt5RVTXlD7ARq/giphy.gif)
_**Buttons using the border property**_

Notice how a **white colored border** shows around the button when I hover the mouse over the button.

### How to use the border property in CSS

And remember, the **border** is the space added on top of our **main content + padding**: **👇**

![Cat image with black dashed line is the border](https://www.freecodecamp.org/news/content/images/2021/07/Border.png)
_**The black dashed line is the border**_

There are three crucial **inputs** of the border property:

* border size
* border style : **solid / dotted/ dashed**
* border color

![Border property syntax](https://www.freecodecamp.org/news/content/images/2021/07/Frame-23.png)
_**Border property syntax**_

There are three styles of border property as I listed above. In this example, we'll use the **dashed** style:

![A box with content, padding, and a black dashed line as a border](https://www.freecodecamp.org/news/content/images/2021/07/Frame-22.png)

To recreate the results above, write this code in your CSS: 👇

```css
.box-1 {
  width: 300px;
  font-size: 50px;
  padding: 50px;
  border: 10px dashed black;
}

```

Let's open our console and see the box model calculations:

![Image of the computed box model in the dev console](https://www.freecodecamp.org/news/content/images/2021/07/dxcxcvbxc-1.png)
_**Computed CSS box model**_

Now look at the above image☝ – a 10px border is added all around our **content + padding**.

## The Margin Property

Generally, I use the **margin** property to put some **whitespace** between my content and the main screen on the desktop layout (large screens). Look at this GIF: 👇

![Adding margin to a website](https://www.freecodecamp.org/news/content/images/2021/07/rea.gif)
_**Adding margin to a website**_

Notice that I'm adding the margin to the left and right edges of my website above 👆 

Here's another sample GIF of **a use case** of the margin property: 👇

![Adding margin to a website](https://www.freecodecamp.org/news/content/images/2021/07/reammmmm.gif)
_**Adding margin to a website**_

### How to use margin property in CSS

This is the **shorthand** for the four properties of the margin property:

* margin-top
* margin-right
* margin-bottom
* margin-left

![Shorthand of the margin property](https://www.freecodecamp.org/news/content/images/2021/07/Frame-12.png)
_**Shorthand of the margin property**_

And remember, **margin** is the space added on top of our **main content + padding + border**:

![Cat image with a grey margin](https://www.freecodecamp.org/news/content/images/2021/07/Margin-1.png)
_**The grey region is the margin**_

Let's add a margin to our content. **The content is getting pushed due to the Margin** in this GIF:**👇**

![Content getting pushed due to margin](https://www.freecodecamp.org/news/content/images/2021/07/agid.gif)
_**Content getting pushed due to margin**_

To recreate the results above, write this code in your CSS: 👇

```css
.box-1 {
  padding: 50px;
  border: 10px dashed black;
  
  margin: 50px;
}
```

We can check the calculations again: 👇

![Dev console image showing a margin](https://www.freecodecamp.org/news/content/images/2021/07/klkjkj.png)
_**Computed CSS box model**_

Look, a 50px margin has been added all around our **content + padding + border**.

Let's try adding a **margin** to just 1 side of our content (only the left side):

![The margin-left property](https://www.freecodecamp.org/news/content/images/2021/07/Frame-22--2-.png)
_**The margin-left property**_

To recreate the results above, write this code in your CSS 👇

```css
.box-1 {
  padding: 50px;
  border: 10px dashed black;
  
  margin-left: 50px;
}
```

On the console, we can see that a **50px margin** got applied only on the **left side** 👇

![Dev console image showing the margin-left property](https://www.freecodecamp.org/news/content/images/2021/07/vbnvbnbnbv.png)
_**Computed CSS Box Model**_

## Take a Break!

So far so good – take a break! You deserve it 💖

![Dog drinking a bubble tea](https://www.freecodecamp.org/news/content/images/2021/07/Frame-24--1-.png)

## The Box-sizing Property

This property defines how our margin, padding, and borders will be calculated. There are three types of calculations (you can call them values):

* border-box
* padding-box
* content box

### Note:

We're not gonna discus **box-sizing: padding-box,** as only Firefox supports it and it isn't used very often.

## What is the difference between content-box and border-box in CSS?

Both border-box and content-box work in the same way. Look at these images:👇

![Boxes using the border-box value](https://www.freecodecamp.org/news/content/images/2021/07/Frame-15.png)
_**Boxes using the border-box value**_

![Boxes using the content-box value](https://www.freecodecamp.org/news/content/images/2021/07/Frame-17.png)
_**Boxes using the content-box value**_

So, what's the main difference here? The difference is noticeable when we are adding margin, border, or padding to our boxes. 

When we are using the **box-sizing: content-box**, which is the default value, it will **add** a margin, padding, and borders **outside the box**, like this: 👇

![Padding, getting applied outside the box](https://www.freecodecamp.org/news/content/images/2021/07/abcdefg.gif)
_**Padding getting applied outside the box**_

You can see the calculations here as well: 👇

![Calculations with content-box](https://www.freecodecamp.org/news/content/images/2021/07/Frame-19.png)
_**Calculations with content-box**_

Which means that things can get out of control and you'll see unexpected calculations. This means that it's **hard to make responsive websites.** Always use the **box-sizing: border-box** property instead.

But when we are using the **box-sizing: border-box** property, it will **add** a margin, padding, and borders **inside the box**, like this:👇

![Padding getting applied inside the box](https://www.freecodecamp.org/news/content/images/2021/07/c-box.gif)
_**Padding getting applied inside the box**_

The **box-sizing: border-box** property shows us the **EXACT** calculations of our HTML elements, which means that this value is **ideal for making responsive websites.**

You can experiment with the values as well – just follow along with this code: 👇

```css
* {
  box-sizing: border-box;
}

/* Or, Write 👇 */

* {
  box-sizing: content-box;
}
```

## Conclusion

Congratulations! You can now make **pixel perfect websites.** Not only that, but when you're coding, you can figure out why your content is behaving strangely.

Here's your medal for reading till the end ❤️

## Suggestions & Criticisms Are Highly Appreciated ❤️

![Clapping hands and a gold medal](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube [/ Joy Shaheb](https://youtube.com/c/joyshaheb)**

**LinkedIn [/ JoyShaheb](https://www.linkedin.com/in/joyshaheb/)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**

## Credits

* [Images from Freepik](https://www.freepik.com/collection/css-box-model-vectors/2187534)

