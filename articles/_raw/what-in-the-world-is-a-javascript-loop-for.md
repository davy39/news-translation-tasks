---
title: What in the world is a JavaScript loop?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-07T20:33:22.000Z'
originalURL: https://freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/joanna-kosinska-1_CMoFsPfso-unsplash.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'By Syk Houdeib

  This article is a beginner''s introduction to JavaScript loops. We''ll go over why
  we need them, and how they fit into the front-end context. It’s a bird''s eye view
  of accessing data and doing things to it, covering fundamental every-day...'
---

By Syk Houdeib

This article is a beginner's introduction to JavaScript loops. We'll go over why we need them, and how they fit into the front-end context. It’s a bird's eye view of accessing data and doing things to it, covering fundamental every-day concepts for a front-end developer.

## Introduction.

_“So we take this array, we iterate over it, we process the data and shazam!”_  
When I first started learning to program, phrases like this sounded like mystical incantations. A language that looks like English but was beyond my comprehension. Coming from a non-engineering background I couldn’t for the life of me understand where a loop fit into what I was trying to do. And why exactly I needed it.

Nowadays, as a front-end developer, I use a loop for something or another all the time. But I haven't forgotten how mysterious it all was. My aim here is to give a high-level overview designed for people who have no engineering background. We will go beyond the syntax and instead focus on a real context of why we use loops and how it all fits together.

In this article, we will talk about how we access data and then how we do things to it with **loops.** More importantly, we are gonna try to answer **why** we need to do this. And **how is this relevant** to you building websites and web apps.

There’s also going to be a beginner-friendly **practical example.** You can follow along to it to practice the concepts and see them in action for yourself.

### The setup

Let’s imagine that we are working on an online platform that allows us to do our supermarket shopping from a website. That's a real-world application of the things we want to talk about here.

Take a look at [Lola Market](https://lolamarket.com/tienda), which is where I work, for an example of how this would look like.

Assume we have a bunch of products stored in our database. Our task is to take these and display them on the website as a list. It’s a simple task that mimics things we do every day in the front end.

## Loops

To talk about loops we are going to be working with arrays. If you would like a refresher on what is an array and why we need it you can check out my article about it that links up nicely to this one.

[https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/)

In short, we have taken a bunch of products that are in our database. We have packaged them in an array and made a request to bring them into our front-end code. And this is what this array looks like.

```js
['mushrooms', 'steak', 'fish', 'aubergines', 'lentils']
```

Once we have the array of products that’s where the loops come in. Simply put, a loop is a way to take our array, “open” it and take one element out. Hand it to us to do what we want to it. Then repeat with the next element all the way to the end of the array.

We use a loop when we need to repeat the same code for each one of the elements in our data.

### Get set

What we want to do is to display this list of products on the website. imagine it like this. Most websites would look more complex we hope. But this is just our first step.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/products-list-2.png)
_Products list_

To keep the example simple and accessible to beginners we are going to use **dev tools** to do all the work. This requires no setup apart from opening your browser's dev tools.

We need to take a few things into account.

*  We will not be making a call to the database to get our list of products. Instead, we will type an array by hand and use it directly in our front-end code.
* We will not be displaying the list of products on a website. Instead we are only going to log the list into the dev tools console.
* In the real world, we wouldn't be using the `console.log()` statements you see here. Instead  the logic we need to display our list on the website would be in its place.

OK, we are all set. Let's go.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-215.png)
_Photo by [Unsplash](https://unsplash.com/@vandateixeira?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Vanda Teixeira</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### For each product

First, let’s take our loop and store it in a **variable**. This is to make it easier to read and work with.

```js
const products = ['mushrooms', 'steak', 'fish', 'aubergines', 'lentils']
```

Now every time we use `products` we are actually referring to our array. This is very handy because our array could easily contain hundreds of products. 

So, on we go to the main course, let me introduce you to the `forEach()`  
loop. And here is what it looks like in action:

```js
products.forEach( product => {
	// do stuff
 })
```

We will break this down piece by piece now. To begin with, let's convert this snippet of code into **plain English**. This literally reads: “Take the products array. For each element in this array, take that element, call it `product` and _do stuff_ to it.”

Let’s take a closer look. 

```js
⬇ARRAY⬇  ⬇LOOP⬇  ⬇CURRENT⬇ ⬇FUNCTION⬇
products.forEach( product => {
	// do stuff
})
```

* `products`: This is our **array** that contains the data.
* `.forEach()` : This is our array method, the **loop**.
* `product` : This is the **currently selected** element. This is the item from the array that our loop has picked up and given to us to work with.
* `=> { }` : This is a **function** declaration, an arrow function to be specific. It roughly says “execute the following code.”
* `// do stuff` : This is where the actual code goes. Do things for each of the elements in the array.

It is important to remember two things here about the currently selected element. First, that `product` is a variable name. The name itself is ours to decide, we could have called it `food` or `x` or anything else. However, if we are dealing with an array of `products` it is customary to use the singular for an individual item of that array: `product`. If it was an array of `animals` then we would call it `animal`.

Second, `product` changes with every round the loop does. Each time the loop picks an item  `product` becomes this new currently selected item.

Basically, the loop starts by picking up the first element in the array, “mushrooms” in this case. `product` now refers to “mushroom”. The loop then executes the function and runs the code that is there. Once it’s finished it goes back to the array and picks up the next element. `product` is no longer “mushrooms”, it is “steak” now. Once again the code executes. And this repeats **for each** one of the elements in the array.

Each one of those rounds the loop makes is called an **iteration**.

### Try it yourself

So let’s try this out and see how it works. Go ahead and open the console in your browser’s dev tools. For example in Chrome it is Command + Option + J (Mac) or Control + Shift + J (Windows).

* Type out our array saved in a variable `const products = ['mushrooms', 'steak', 'fish', 'aubergines', 'lentils']`.
* Hit enter. You’ll get an `undefined`. This is normal.
* Then type out our loop and this time we will add a  `console.log()` as the code to execute:

```js
products.forEach( product => {
	console.log(product)
})
```

This is what it would look like:

![The dev tools console showing our array of products and loop](https://www.freecodecamp.org/news/content/images/2019/08/loops-1.png)
_The Chrome dev tools console_

What we want here is to print to the console the value that is `product` on each iteration. Try it for yourself. Hit enter.

Once you do, the loop will start. For each product, it will log the currently selected one to the console until it’s done with all the products in our array.

![The code executed in the console shows the name of each product from the array printed to the console](https://www.freecodecamp.org/news/content/images/2019/09/loop-results.PNG)
_The loop´s results in the console_

And That's it. We have printed our entire array to the console. And we can use the same idea to manipulate the DOM to display and modify content on a website. Or do a myriad of other things with the data.

What about if we wanted to treat some of this data differently and not execute the same code for all the products? Say for example we want to show a "(v)" only next to vegetarian items.

In the following article, I explain just that. I take our example to the next step and talk about how **conditionals** allow us to do this - check it out!

[https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-conditional-for/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-conditional-for/)

## Conclusion

To recap, a **loop** takes our data (an array in this case) and allows us to access it. It then **iterates** over each element in the array and **executes** some code for each element.

I’m hoping that the next time you encounter a loop you will find it easier to understand how it works. And that it’s clearer why you might need one in a front-end context.

In this article, we saw a `forEach()` loop. But apart from the `forEach()`, there are many more **loops** and **array methods** to learn. From the most basic `for` loop to more advanced methods like `map()` and `filter()`. These are extremely powerful tools for development that you should get familiar with. You'll find yourself using them while working on any kind of application.

### Closure

Thanks for reading. I hope you found this useful. And if you enjoyed it, sharing it around would be greatly appreciated. If you have any questions or comments I’m on [Twitter](https://twitter.com/Syknapse) [@Syknapse](https://twitter.com/Syknapse) and I would love to hear from you.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-157.png)
_Photo by [Claudia](https://twitter.com/__Santaella)_

My name is Syk and I’m a front-end developer at [Lola Market](https://twitter.com/Tech_LolaMarket) in Madrid. I career-changed into web dev from an unrelated field, so I try to create content for those on a similar journey. My DMs are always open for aspiring web developers in need of some support. You can also read about my transformation in [this article.](https://medium.com/free-code-camp/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b)

[https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/](https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/)

---

  

