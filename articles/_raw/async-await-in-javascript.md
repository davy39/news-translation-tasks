---
title: How to Use Async/Await in JavaScript with Example JS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T18:11:00.000Z'
originalURL: https://freecodecamp.org/news/async-await-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--12-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Nishant Kumar

  In this tutorial, we are going to learn how to use Async/Await in JavaScript.

  But before we get there, we should understand a few topics like:


  Event loops

  Callbacks

  Promises


  What are Event Loops in JavaScript?

  Event loops are one o...'
---

By Nishant Kumar

In this tutorial, we are going to learn how to use Async/Await in JavaScript.

But before we get there, we should understand a few topics like:

1. Event loops
2. Callbacks
3. Promises

## What are Event Loops in JavaScript?

Event loops are one of the most important aspects of JavaScript.

JavaScript is a single-threaded programming language which means that only one task can run at a time. It has a call stack and all the code is executed inside this call stack. Let’s understand with an example.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--8-.png)

In the above example, we can see that we are logging two values in the console.

When the `First()` finishes its execution, it will be popped out of the call stack and the event loop will go down to the next line. The next line will be stored in the call stack and will be flagged for execution.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--9-.png)

Our console will print the following result:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--18-.png)

To understand things better, let’s take a look at another example.

```javascript
console.log('First!');

setTimeout(function second(){
    console.log('Timed Out!')
}, 0000)

console.log('Final!');
```

As usual, our code will move into the call stack and the event loop will loop through line by line.

We will get “First!” in the console and it will be moved out of the call stack.

Now, the event loop will move to the second line and push it into the call stack. It will encounter the `setTimeout` function, which is a Macro task, and it will be executed in the next event Loop. 

And now, you might be wondering what a Macro task is. Well, it's a task that runs after all of the tasks in the Event Loop, or you might say, in the other Event Loop. The `SetTimeout` and `SetInterval` functions can be the example of a Macro task which runs after all of the other tasks are completed.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--19-.png)

Finally, the final line of code will be executed. We will get First in our console, then Final, and then Timed Out.

## How Do Callback Functions Work in JavaScript?

Callback functions are those functions that have been passed to another function as an argument.

Let’s take a look at an example.

```javascript
const movies = [
{ title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
{ title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

getMovies();
```

We have an array that contains the list of Star Wars movies and a function `getMovies()` to fetch the list.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--20-.png)

Let’s create another function called `createMovie()`. It will be used to add a new movie.

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie){
    setTimeout(() => {
        movies.push(movie)
    }, 2000);
}

getMovies();


createMovies({ title: `Return of the Jedi`, body:`Luke Skywalker attempts to bring his father back to the light side of the Force. At the same time, the rebels hatch a plan to destroy the second Death Star.` });
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--20--1.png)

But the problem here is we are not getting the third movie on the console. That is because `createMovie()` takes longer than `getMovies()`. The `createMovie()` function took two seconds but `getMovies()` took only one second.

In other words, `getMovies()` runs before `createMovies()` and the list of Movies is already displayed.

To solve this, we can use Callbacks_._

In `createPost()`, pass a function callback and call the function right after the new movie is pushed (instead of waiting two seconds).

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie, callback){
    setTimeout(() => {
        movies.push(movie);
        callback();
    }, 2000);
}


createMovies({ title: `Return of the Jedi`, 
                body:`Luke Skywalker attempts to bring his father back to the light side of the Force. 
                At the same time, the rebels hatch a plan to destroy the second Death Star.` }, getMovies);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--21--2.png)

Now we get the updated list of movies.

## How Do Promises Work in JavaScript?

A promise is a value that may produce a value in the future. That value can either be resolved or unresolved (in some error cases, like a network failure). It works like a real-life promise.

It has three states: fulfilled, rejected, or pending.

* **Fulfilled:** `onFulfilled()` will be called (for example, `resolve()` was called).
* **Rejected:** `onRejected()` will be called (for example,  `reject()` was called).
* **Pending:** not yet fulfilled or rejected.

Let’s take a look at an example.

Promise takes two parameters, resolve and reject. When something goes wrong, reject is called, or else resolve is called.

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            movies.push(movie);

            const error = false;

            if(!error){
                resolve();
            }
            else{
                reject('Error: Something went wrong!')
            }
        }, 2000);
    })
}

createMovies({ title: `Return of the Jedi`, body:`Luke Skywalker attempts to bring his father back to the light side of the Force. At the same time, the rebels hatch a plan to destroy the second Death Star.`})
.then(getMovies);
```

If we get an error, it will be something like ‘Error: Something went wrong!’, and if not, the promise will resolve.

Once the promise is resolved, it calls for the `.then()` keyword and `getMovies()`.

## Finally, How Does Async/Await Work in JavaScript

Async means asynchronous. It allows a program to run a function without freezing the entire program. This is done using the Async/Await keyword. 

Async/Await makes it easier to write promises. The keyword ‘async’ before a function makes the function return a promise, always. And the keyword await is used inside async functions, which makes the program wait until the Promise resolves.

```javascript
async function example() {

  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("done!"), 2000)
  });

  let result = await promise; // wait until the promise resolves (*)

  alert(result); // "done!"
}

example();
```

The function execution “pauses” at the `(*)` line and resumes when the promise is fulfilled, with `result` becoming its result. So the code above shows “done!” in two seconds.

Let's take a look at a practice example.

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            movies.push(movie);

            const error = false;

            if(!error){
                resolve();
            }
            else{
                reject('Error: Something went wrong!')
            }
        }, 2000);
    })
}

async function init(){
    await createMovies({ title: `Return of the Jedi`, body:`Luke Skywalker attempts to bring his father back to the light side of the Force. At the same time, the rebels hatch a plan to destroy the second Death Star.`});
    
    getMovies(); (*)
}

init();
```

In the above example, `getMovies()` at the (*) line is waiting for `createMovies()` to be executed in the async function.

In other words, `createMovies()` is async, so `getMovies()` will only run after `createMovies()` is done.

Now you know all the basics of Event Loops, Callbacks, Promises and Async/Await. These features were introduced in ECMAScript 2017, and they've made reading and writing JS code much easier and more effective. 

> _That’s all folks! Happy learning and experimenting,_

