---
title: Learn the CSS Box-Shadow Property by Coding a Beautiful Button ✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-06-30T18:49:49.000Z'
originalURL: https://freecodecamp.org/news/css-box-shadow-property-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/FCC-Thumbnail.png
tags:
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'Today we''re gonna learn how to use CSS''s box-shadow property to make
  beautiful website components. Along the way, we''ll create a button and get hands-on
  experience using this property. Let''s get started. 🎖️

  Table of Contents


  Why you should use the ...'
---

Today we're gonna learn how to use CSS's **box-shadow** property to make beautiful website components. Along the way, we'll **create a button** and get hands-on experience using this property. Let's get started. 🎖️

# Table of Contents 

* [**Why** you should use the CSS box-shadow property](#heading-why-should-you-use-the-css-box-shadow-property)
* [The **syntax** of the box-shadow property](#heading-the-syntax-of-the-box-shadow-property)
* [How to make a **button** using the box-shadow property](#heading-how-to-add-a-drop-shadow-to-a-button)
* [Additional Resources](#heading-additional-resources) 
* [What is **inset** in](#heading-what-is-inset-in-the-css-box-shadow-property) CSS **Box shadow property**?

## **You can watch this tutorial on YouTube as well if you like:**

%[https://youtu.be/4Clc-Bb5sY4]

# Why Should You Use The CSS box-shadow Property?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-1.png)

**Attention to small details** separates a good website from an excellent looking website. If you want to add those small details to your website, you should definitely use this property along with many other properties.

Let's took at some examples. 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Page-1--1-.png)
_**A Website Design**_

Pay close attention to the button components in the image above. You'll see that we have some drop shadows. ☝

Let's examine these buttons even further: 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-27.png)
_**Button with no box-shadow property**_

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-28.png)
_**Button using the box-shadow property**_

You can tell that the latter one looks more dynamic and interesting, as it has more **attention to detail.** This is called a **drop shadow effect**. Let's see how we can implement it in our code.

# **Project Setup**

### HTML

Write this code inside the body tag: 👇

```html
<div class="box-1"> A Button </div>
```

### CSS

Clear your default browser settings like this:

```css
*{
   margin: 0px;
   padding: 0px;
   box-sizing: border-box;
   font-family: sans-serif;
}
```

Now, let's create a button with the following code:👇

```css
.box-1{
   margin: 100px 0 0 100px;
   height: 80px;
   width: 200px;
   border: 2px solid black;
   border-radius: 8px;
   font-size: 40px;

   display: grid;
   place-content: center;
}

```

We're all set, now let's start coding!

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-2.png)

# The Syntax of the box-shadow Property

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-3-1.png)
_**All the inputs of box-shadow property**_

Here's the syntax for the box-shadow property: 👇

```css
box-shadow: offset-x | offset-y | blur-radius | spread-radius | color ;
```

Let's look at each part in more detail.

## How to Use Offset-x in the box-shadow Property

You'll use the offset-x property to move the shadow left and right along the X-Axis. Here's a demo to show you how that looks:👇

![Image](https://media.giphy.com/media/Mzxh8CdUTaxgzzj9ml/giphy.gif)
_**We can move the shadow left &amp; right**_

The recreate these results, write the following code in your CSS: 👇

```css
/* offset-x | offset-y | color */
.box-1{
   box-shadow: -50px 0px rgba(0,0,0,0.5);
}

/*Or, you can write*/

.box-1{
   box-shadow: 50px 0px rgba(0,0,0,0.5);
}
```

## How to Use Offset-y in the box-shadow Property

You'll use the offset-y property to move the shadow up and down along the Y-Axis. Here's a demo of how that looks:👇

![Image](https://media.giphy.com/media/Ss9Qnrq9PFBpAfVLk8/giphy.gif)
_**We can move the shadow top &amp; bottom**_

To recreate these results write the following in your CSS: 👇

```css
/* offset-x | offset-y | color */
.box-1{
   box-shadow: 0px -50px rgba(0,0,0,0.5);
}

/*Or, you can write*/

.box-1{
   box-shadow: 0px -50px rgba(0,0,0,0.5);
}
```

### How to Combine Both offset-x and offset-y

Write the following code in your CSS: 👇

```css
.box-1{
   box-shadow: 10px 10px rgba(0,0,0,0.5);
}
```

Here's the result with the box shadow showing on the right and bottom of the button: 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6-1.png)
_**Our button with box shadow**_

## How to Use blur-radius in the box-shadow Property

The blur-radius property will blur **the color** around our button, like this:👇

![Image](https://media.giphy.com/media/5fRA7jzOwtmXnT57Ne/giphy.gif)
_**Experimenting w/ blur radius**_

To duplicate the results, write the following in your CSS: 👇

```css
/* offset-x | offset-y | blur-radius | color */

.box-1{
/* play around with 👇 this */
   box-shadow: 0 0 50px rgba(0,0,0,0.8);
}
```

## How to Use spread-radius in the box-shadow Property

This value spreads our shadow around our button, like this: 👇

![Image](https://media.giphy.com/media/FfVw2vxOonQAjkFc7B/giphy.gif)
_**Experimenting w/ spread radius**_

Let's recreate the results with the following CSS code:

```css
/* offset-x | offset-y | blur-radius | spread-radius | color */

.box-1{
/*  play around with 👇 this */
   box-shadow: 0 0 0 50px rgba(0,0,0,0.5);
}

```

# How to Add a Drop Shadow to a Button

Let's put together what we've learned so far and add a drop shadow effect to our button: 👇

```css
.box-1{
   box-shadow: 8px 10px 10px 1px rgba(0,0,0,0.5);
}
```

The result looks like this: 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--1--1.png)
_**The result**_

# Additional Resources 

* [[GetCssScan](https://getcssscan.com/css-box-shadow-examples)] - To get readymade box shadows
* [[keyframes.app](https://keyframes.app/animate/)] - to test and practice these properties in real time
* [flatuicolors](https://flatuicolors.com/) - Beautiful color palettes

## ✨ Bonus Tip ✨

# What is Inset in the CSS box-shadow Property?

There's a keyword named `inset` that you can use with the box-shadow property. This puts the shadow inside our button instead of spreading it around the outside. Write this CSS code to experiment with it:👇

```css
.box-1{
   box-shadow: inset 8px 10px 10px 1px rgba(0,0,0,0.5);
}
```

Here's the result: 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--2--4.png)
_**Effect of the inset keyword**_

# Conclusion

Now you can confidently use the box-shadow property to add not only **drop shadows** but also to add more **attention to detail** to your projects.

Here's your medal for reading till the end. ❤️

### Suggestions and criticisms are highly appreciated ❤️

![](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

* **YouTube[ / Joy Shaheb](https://youtube.com/c/joyshaheb)**
* **LinkedIn[ / JoyShaheb](https://www.linkedin.com/in/joyshaheb/)**
* **Twitter[ / JoyShaheb](https://twitter.com/JoyShaheb)**
* **Instagram[ / JoyShaheb](https://www.instagram.com/joyshaheb/)**

# Credits

* [Young Girl](https://www.freepik.com/free-vector/young-girl-thinking-face-wondering-cartoon-illustration_11652601.htm#page=1&query=worried%20illustration&position=31)
* [Cute Kat](https://www.freepik.com/free-vector/cute-cat-playing-with-box-cartoon_13747509.htm?query=happy%20illustration), [Unicorn cat](https://www.freepik.com/free-vector/kawaii-cat-unicorn-character-collection_5481560.htm)

