---
title: What Choosing and Applying Eyeshadow Can Teach us About Coding
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T18:56:19.000Z'
originalURL: https://freecodecamp.org/news/eyeshadow-932b6cd5cfee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aFChFIbBTgSQq2vBAwUZtg.jpeg
tags:
- name: Codelikeagirl
  slug: codelikeagirl
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: women in tech
  slug: women-in-tech
seo_title: null
seo_desc: 'By Code Girl

  I love eyeshadow. I have over 40 eyeshadow palettes (a palette is a container with
  any number of individual eyeshadow colors), and I don’t think my obsession diminishes
  my status as a progressive woman in technology. I am known for my sp...'
---

By Code Girl

I love eyeshadow. I have over 40 eyeshadow palettes (a palette is a container with any number of individual eyeshadow colors), and I don’t think my obsession diminishes my status as a progressive woman in technology. I am known for my sparkly blue colors which represent my never-ending devotion to Ravenclaw house in Harry Potter.

The sad truth, however, is that I suck at choosing and applying eyeshadow, which might have something to do with the fact that:

1. I have too many colors to choose from, and
2. I need to take my glasses off to do it.

Yet this doesn’t stop my insatiable need for acquiring more shadow options. After I left my trusted makeup store last week — having spent over $100 in products, including a new eyeshadow palette (none of which I needed) — I thought, “If only choosing and applying eyeshadow was as easy as writing a function.”

That is the origin of this article. Using code to solve practical problems is a hallmark of the field of technology, but it takes practice. Here is my attempt at a **think-aloud** to solve my eyeshadow problem.

For those of us without a background in education, a **think-aloud** is a method of making an invisible thought process, visible. We use this technique frequently in reading instruction.

### **Function Basics and My Eyeshadow Routine**

Understanding functions is a rite of passage in programming. When you first begin your journey, you write out each and every line of code, numerous times. Enter functions. A function is nothing more than a procedure, a set of steps for completing a task.

Generally, a function will take some input data, perform the required procedure with that data, and return any resulting data. What makes functions so versatile in code is that you can call that function, or set of steps, over and over again with different inputs, hence different outputs.

Putting on eyeshadow is like following a set of steps. I stick to the same set of steps (function) for choosing and applying eyeshadow practically everyday illustrated in the below diagram.

![Image](https://cdn-media-1.freecodecamp.org/images/lV50bSeGue9ldy8Sm4HIODMZuDloLdxpuwZu)
_This image was part of a blog post on BellaBox [HERE](https://bellabox.com.au/beautyguide/9-Awesome-Eyeshadow-Hacks" rel="noopener" target="_blank" title=")_

Let’s think about this in terms of programming where we have an input, a set of steps, and an output:

* **Input**: I need to input an eyeshadow palette. Let’s say the “Sweet Peach” palette by [Too Faced Cosmetics](https://www.toofaced.com/).
* **Function**: My function needs to filter through all of the colors (18 total) and find the four key colors to use: `highlighter`, `medium`, `smokey`, and `blender`.
* **Output:** Tell me specifically which colors match which eye application area.

### **Input Eyeshadow Data**

Have you guessed the first problem here? The input data isn’t as simple as a variable with a string or number value:

![Image](https://cdn-media-1.freecodecamp.org/images/ogsP0Rg28zsy476KFN1xonARjcPlFmquj2MO)

The Sweet Peach palette has 18 colors. You might be thinking, we can write each color out in an array (or list):

![Image](https://cdn-media-1.freecodecamp.org/images/oukf2IVZIW05VLYg1H-dKDwOyjraVbZuLERq)
_Yes, that’s only 6 out of the 18, and yes, eyeshadow color names are quirky._

There is still a problem with the shape of this data. An array is just a list of the colors.

Each color needs a label to identify which type of color it is: `highlighter`, `medium`, `smokey`, and `blender`.

A better option might be an array of objects. An object is a collection of data organized by a key and a value. In each object here, we have two key value pairs, one for the type and the other for the color:

![Image](https://cdn-media-1.freecodecamp.org/images/OpBwu2sYa34C6CSYTa-NLgyqeHsFqCPSu8FH)

Perfect. Every time I use `SweetPeachCombination` as my input, I will know exactly which color to use for which part of my eye.

### **findColor Function: The Parameter and the Argument**

Now that we have some data, we can look at what the function might do. I want to be able to call this `findColor` function with any input data and know exactly what color goes where. First, I need to loop through the array. Then, I need to log the type and color. The code could look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/nSJXXiTM16cRtrAWzJA7l45UglurqOg83K5a)
_I am using ES6 template literals in the console.log._

Since this is not actual code, I’m just going to log the information to the console. On my actual website, I update the information through the DOM. See website [**HERE**](https://fwallacephd.github.io/EyeshadowApp/).

Let’s dissect the above code.

The function is called `findColor`, and it **has** one **parameter**.

Parameter, here, is a technical way of saying input placeholder — meaning, we need the `combination` information in order to run the function. Remember, though, we can use any combination we want, so the parameter is not specific.

How do I tell the function which combination to use? When we call the function:

![Image](https://cdn-media-1.freecodecamp.org/images/5fm017etuYohkDucn6X4MrWUL7Ka7gzQVUBA)

We **pass** in the specific combination. This changes the technical word. It is not a parameter anymore, it is now an **argument**. The difference being that this is the real data, not a placeholder.

You can see that clearly because the **parameter** is called `combination` while the **argument** is called `SweetPeachCombination`.

### Refactoring the Eyeshadow Inputs

Seems like a pretty lame function right now, right? I’m literally giving it the data of which color goes where and then having the function spit that information right back out (the output). But remember I have 40 palettes of eyeshadow. I honestly can’t remember each individual color or possible combination. Right now, I have just one combination for just one palette…

I bet you see where I’m going with this.

My eyeshadow input data doesn’t reflect reality — multiple palettes with multiple colors means endless possibilities.

The shape of the data does not have to change, but I need to add more information:

![Image](https://cdn-media-1.freecodecamp.org/images/1Q1QgeaiMwd7N6EtGDHqL0Fy35fxRRJ4b7bE)
_This is one of my blue combinations, so I’ve named it accordingly._

![Image](https://cdn-media-1.freecodecamp.org/images/JzvYDTHpVTRYm8MwSiZLp6corwZh8RPEgTVu)
_Can’t leave out Slytherin House and the green combination!_

Naturally, we will need to revise the function based on this new information, but that’s the easiest part:

![Image](https://cdn-media-1.freecodecamp.org/images/igGh4jRE8-mKM0wWEPcEHeQ9hosNbRQoKktC)

Theoretically, I could have 400 combinations! I don’t have that kind of time in the morning to look for the right combination. That’s why my `findColor` function works perfectly. Every time I call that function, I use a `combination` argument.

![Image](https://cdn-media-1.freecodecamp.org/images/KnRtelk6wZl5Af1WZNelDYyHXn-D3wvGbhPi)

### The Most Important Part

I say this all the time about programming. If you can dream it, you can build it.

I dreamed of an eyeshadow color picker, and I built it (screen cap below).

![Image](https://cdn-media-1.freecodecamp.org/images/O-GrgHDBDBVK3etaB7c0f6nnuql99k47csaB)
_Check it out [HERE](https://fwallacephd.github.io/EyeshadowApp/" rel="noopener" target="_blank" title="">HERE</a>. Get the code <a href="https://github.com/fwallacephd/EyeshadowApp" rel="noopener" target="_blank" title=")._

Building is the **only** way to realistically debug (find your mistakes) and refactor (make the code better). This is going to be your life as a programmer, so it’s critical that you build your muscle memory for it.

Further, I challenge you to practice everything when you build, not just the functionality (in this case JavaScript), but also your basics: HTML, CSS (and here, Bootstrap). Every time I build, I learn something new even in my basic skills.

For this project, I learned how to use CSS to make a rainbow effect on the title. I also took this opportunity to practice using a database, [Firebase](https://firebase.google.com/docs/database/). This is a free and easy-to-use database system to set and retrieve the color combination objects, but that is the topic of another post.

So what are you going to build next?

Note: If you use Too Faced Eyeshadow, and would like to help me work on building out this application and then make it a mobile application, please email me at fwallacephd[at]gmail[dot]com

