---
title: What in the world is a JavaScript array?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-01T19:15:47.000Z'
originalURL: https://freecodecamp.org/news/what-in-the-world-is-a-javascript-array
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/kimberly-farmer-lUaaKCUANVI-unsplash.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Syk Houdeib

  This article is a beginner''s introduction to JavaScript arrays and data structures.
  It covers why we need them, and how they fit into the front-end context.

  Introduction

  When I first started learning to program, I would regularly encou...'
---

By Syk Houdeib

This article is a beginner's introduction to JavaScript arrays and data structures. It covers why we need them, and how they fit into the front-end context.

## Introduction

When I first started learning to program, I would regularly encounter concepts that were hard to fit into the big picture. Coming from a non-traditional background I found words like "data structures" and "arrays" often difficult to place in a context that made sense. Or why they were needed for front-end development at all.

Nowadays data and arrays are part of my daily diet as a front-end developer. But I still remember all that early confusion. My aim here is to give a high-level overview designed for people who have no engineering background. And to place it all in a realistic context.

In this article, we will talk about what **data is** and how we **organise** it. We will examine data structures focusing only on **arrays** to keep things clear. And we will look at why we need it.

### The setup

Let’s imagine that we are working on an online platform that allows us to do our supermarket shopping from a website. That's a real-world application of the things we want to talk about here.

Take a look at [Lola Market](https://lolamarket.com/tienda), which is where I work, for an example of how this would look like.

Our website is going to show a list of products. This is going to be our starting point to talk about data and organising it in a context that mimics things we do every day in the front end.

## What even is data?

Before we start talking about how we organise data, let's try to understand what data means in our context. And where this data comes from.

When you are working in the digital domain it’s helpful to remember that everything is data. Everything is bits stored in binary. 

Now while that might be interesting, it is so general that it is of no help to us. So for our purposes, we will focus on a narrow idea of what data is. The one which is most immediately relevant. Take a look at the following list:

![A list of products: Mushrooms, Steak, Fish, Aubergines, Lentils](https://www.freecodecamp.org/news/content/images/2019/08/products-list-1.png)
_List of products_

This reduced list is an example of the kind of products you can find on this website we are building. This list is our data: mushrooms, steak, fish, aubergines, and lentils.

## So where does this data come from?

Data can live directly in your app, in your front-end code. But more commonly it comes from some outside source. Usually, this data is stored in a database. 

The front end makes a request to the database and receives this data as a response. Once it has arrived into our front-end app, it is time for us to do what we need with it. For example, show the product name on the website, style it, and add any functionalities needed (such as an “add to cart” button).

Take a look at any of the popular shopping websites and you'll see the same pattern. It will have a list of products presented in a certain style with various functionalities and other information about it.

## How do we organise data?

So we have established that this list of products is our data. Now we have to package this data in some sort of a container. This will enable us to organise it, move it around, and later access it and do stuff to it.

One of the most common ways to organise data that you will work with frequently is called an **array**. Here’s what an array looks like:

```js
['mushrooms', 'steak', 'fish', 'aubergines', 'lentils']
```

The syntax looks simple enough. You create an array with the square brackets `[]`. And separate the individual elements with a comma `,`. If your data is made up of **strings** put each element inside quotes or double quotes `''`. **String** loosely means a bunch of characters representing text, like words and sentences.

And that’s it. You have just organised your data in a single package called an **array**. And we can do lots of things with this now. You can think of an array as merely a container that allows us to put data inside, organise it in a certain structure, and permits us to do things with it.

An array is one example of what we call **data structures**. These are the various ways we use to organise data. There are a lot of them, but the two most common ones in the front end are arrays and objects.

So now what do we do with this?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-216.png)
_Photo by [Unsplash](https://unsplash.com/@impatrickt?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Patrick Tomasso</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Why do we need arrays?

We need arrays and other data structures in the front end because almost everything we deal with is data. And that needs to be organised in a way that we can work with.

In our example, once we receive the products' array we can write the logic that takes each product and displays its name on our website. But how do we select each item from the array and do things to it?

In this article below, I explain just that. I take our example to the next step and talk about how **loops** come into play to start processing our data - check it out!

[https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/)

## Conclusion

So, to recap. For our online supermarket, we have a bunch of products and that's our data. We saw how we organise this data into data structures like the array. This is usually stored in a database. We can then request this data.  And once it “arrives” to our front-end app from the database we can start processing it and doing things with it. Hopefully, this has given you a better idea of why we need this in our front end.

Of course, there is more to data structures than arrays made up of strings. Below, I leave you with a little more information to expand your understanding. Things you may want to look at next to understand these concepts more comprehensively.

The first port of call to search for information for me is always [MDN](https://developer.mozilla.org). It's one of the most reliable sources of information for developers.

* **Data structures:** Apart from arrays you will quickly need to get familiar with **objects**. That’s an even more common data structure. In fact, understanding objects is essential to understanding JavaScript as a whole.
* **Data types:** The data we worked with here was made up of `strings`. But there are a few more types of data like `numbers` and `booleans` (true or false) that you will need to understand.
* **Requests:** We briefly mentioned how usually we would make a request to our database to get the data we need to use. Working with APIs, `fetch()`, making requests and handling the response is an advanced topic that you can safely leave for later. But one that’ll be essential by the time you are starting to interview for a developer job.

### Closure

Thanks for reading. I hope you found this useful. And if you enjoyed it, sharing it around would be greatly appreciated. If you have any questions or comments I’m on [Twitter](https://twitter.com/Syknapse) [@Syknapse](https://twitter.com/Syknapse) and I would love to hear from you.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-157.png)
_Photo by [Claudia](https://twitter.com/__Santaella)_

My name is Syk and I’m a front-end developer at [Lola Market](https://twitter.com/Tech_LolaMarket) in Madrid. I career-changed into web dev from an unrelated field, so I try to create content for those on a similar journey. My DMs are always open for aspiring web developers in need of some support. You can also read about my transformation in [this article.](https://medium.com/free-code-camp/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b)

[https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/](https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/)

