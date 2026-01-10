---
title: Async and Await in JavaScript Explained by Making Pizza
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-30T20:20:59.000Z'
originalURL: https://freecodecamp.org/news/async-await-javascript-tutorial-explained-by-making-pizza
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/carissa-gan-_0JpjeqtSyg-unsplash.jpg
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous
  slug: asynchronous
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dave Gray

  Async and await might sound complicated...but they''re as easy as pizza pie once
  you dive in.

  We all use async and await in our daily routines.

  What is an async task?

  An async task lets you complete other tasks while the async task is sti...'
---

By Dave Gray

Async and await might sound complicated...but they're as easy as pizza pie once you dive in.

We all use async and await in our daily routines.

## What is an async task?

An async task lets you complete other tasks while the async task is still working towards completion. 

### Here are some day-to-day async task examples

#### Example 1:

You order food at a drive-thru which starts your food request (an async task). 

You pull forward in the drive-thru line (the next task), while your food is prepared. 

You did not have to wait for your food to be ready before you could pull forward.

You are awaiting your food and your request is fulfilled at the pick-up window.

#### Example 2:

You mop the floor in your kitchen. 

While you wait for your kitchen floor to dry, you vacuum the carpet in your bedroom. 

The original task was to clean your kitchen floor, and the task is complete when the floor is dry. 

Standing around waiting for the floor to dry is not too productive, so you vacuumed the bedroom floor while the kitchen floor dried.

*This is how Javascript handles async functions, too.*

### Example of Async/Await – Bake a Frozen Pizza

You decide to bake a pizza in your oven, and your first step is to preheat the oven. 

So you set the desired temperature and begin to preheat the oven. 

While the oven is preheating, you get the frozen pizza out of the freezer, open the box, and put it on a pizza pan. 

You've got time left! 

Maybe grab a beverage and watch some television while you wait for the oven to beep when it is ready.

Below is some code to simulate this example:

```js
// This async function simulates the oven response
const ovenReady = async () => {
  return new Promise(resolve => setTimeout(() => {
    resolve('Beep! Oven preheated!')
  }, 3000));
}

// Define preheatOven async function
const preheatOven = async () => {
  console.log('Preheating oven.');
  const response = await ovenReady();
  console.log(response);
}

// Define the other functions
const getFrozenPizza = () => console.log('Getting pizza.');
const openFrozenPizza = () => console.log('Opening pizza.');
const getPizzaPan = () => console.log('Getting pan.');
const placeFrozenPizzaOnPan = () => console.log('Putting pizza on pan.');
const grabABeverage = () => console.log('Grabbing a beverage.');
const watchTV = () => console.log('Watching television.');

// Now call the functions
preheatOven();
getFrozenPizza();
openFrozenPizza();
getPizzaPan();
placeFrozenPizzaOnPan();
grabABeverage();
watchTV();

// Output sequence in console:
Preheating oven.
Getting pizza.
Opening pizza.
Getting pan.
Putting pizza on pan.
Grabbing a beverage.
Watching television.
Beep! Oven preheated!

The process above is exactly what async and await is all about. 

While we `await` for the asynchronous `preheatOven` function to complete, we can perform synchronous tasks like `getFrozenPizza`, `openFrozenPizza`, `getPizzaPan`, `placeFrozenPizzaOnPan`, `grabABeverage` and even `watchTV`.

### We perform asynchronous tasks like this all the time

And that's how `async` Javascript works, too.

Notice that when we `await`a response from an `async` function, it needs to be called within another `async` function. That's what we see above when `ovenReady` is called inside of `preheatOven`.

### Two key points to remember:

1. Javascript will NOT wait for an `async` function like `preheatOven` to complete before it moves on to the tasks that follow like `getFrozenPizza` and `openFrozenPizza`. 
2. Javascript will `await` for an `async` function like `ovenReady` to complete and return data before moving on to the next task inside a parent async function. We see this when the `console.log(response)` statement does not execute until `ovenReady` has returned a response. 

## If the pizza example doesn't cut it...

I know everyday examples help some of us, but others may just prefer real code. 

Therefore, I'm going to provide a less abstract async and await JavaScript example below that requests data with the Fetch API:

## Code Example of Async/Await in JavaScript

```js
const getTheData = async () => {
    try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!response.ok) throw Error();
    const data = await response.json();
    // do something with this data... save to db, update the DOM, etc.
    console.log(data);
    console.log('You will see this last.')
    } catch (err) {
        console.error(err);
    }
} 

getTheData();
console.log('You will see this first.');
```




# Conclusion

I hope I have helped you understand async and await in JavaScript. 

I know it can take a while to fully grasp. 

Start preheating your oven for the pizza you're craving and look at some more async and await examples while you wait for the beep!

I'll leave you with a tutorial from my Youtube channel. The video gives a deeper explanation and more code examples including a discussion of callbacks, promises, thenables and the Fetch API along with async & await:

%[https://youtu.be/VmQ6dHvnKIM]


