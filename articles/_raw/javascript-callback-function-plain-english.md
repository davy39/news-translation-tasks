---
title: JavaScript Callback Function –Explained in Plain English
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-10-05T17:17:28.000Z'
originalURL: https://freecodecamp.org/news/javascript-callback-function-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/freeCodeCamp-Cover-4.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Every JavaScript beginner will face this question at least once: \"What\
  \ is a callback function?\" \nWell, we can find the answer in the word callback\
  \ itself. It's all about notifying the caller after the successful completion or\
  \ failure of a task. \nIn t..."
---

Every JavaScript beginner will face this question at least once: "What is a callback function?" 

Well, we can find the answer in the word **callback** itself. It's all about notifying the caller after the successful completion or failure of a task. 

In this article, I'll focus less on the technical aspects of callbacks and will try to explain how they work in natural language. This should help you understand what a `callback function` is and why it exists. 

If you are a JavaScript beginner, then this article is definitely for you.

If you like to learn from video content as well, this article is also available as a video tutorial here: 🙂

%[https://www.youtube.com/watch?v=AUCavCH7FTw]

# First, what is a function?

A function in JavaScript is a set of statements that performs a task. This set of statements can exist without a function, but having them in a function helps us reuse the task in multiple places.

Here is an example of a function that doubles a value if the value is an even number. We pass a number as an argument to the function. The statements inside the function check if the argument is an even number. If so, it doubles it and returns the result. Otherwise, it returns the original number.

```js
function doubleEven(n) {
    if (n % 2 === 0) {
    	return n * 2;
    }
    return n;
}

```

Now you can use this function in as many places as you need to:

```js
doubleEven(10); // Output, 20
doubleEven(5); // Output, 5
```

## You can pass a function as an argument to another function

In the above example, we saw that you can pass a number as an argument to one function. Likewise, you can pass a function as an argument too. Check this out:

```js
/** 
Let's create a foo function that takes a
function as an argument. Here we invoke 
the passed function bar inside foo's body.
*/
function foo(bar) {
    bar();
}


```

Alright, so how do we now invoke foo?

```js
/**
Invoke foo by passing a function as an argument.
*/
foo(function() {
    console.log('bar');
}); // Output, bar
```

Notice that we have passed the entire function definition as an argument to `foo`. The passed function doesn't have a name. It is called an `anonymous function`.

# What is a Callback Function?

The ability of a JavaScript function to accept another function as an argument is a powerful aspect of the language. 

A caller of the function can pass another function as an argument to execute based on any trigger. Let's understand it with the `Robin and PizzaHub` story.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/pizza.png)
_Robin and the PizzaHub Story_

Robin, a  small boy from Wonderland, loves to eat pizza. One morning he picks up his mother's phone and orders pizza using the PizzaHub app. Robin selects his favorite cheese barbeque pizza and press the order button.

The PizzaHub app registers the order and informs Robin that it will `notify` him when the pizza is ready and on the way. Robin, the happy boy, waits for a while and finally gets a `notification` confirming that the pizza is on its way!

So, if we break down the story, the sequence of events goes like this:

* Robin `orders` the pizza
* The app `notes down` the order
* PizzaHub `prepares` the pizza, and it is ready after a while.
* The app `notifies` Robin, confirming the pizza is on the way.

The mechanism of notifying Robin about the pizza works by using the `callback` function.

## Let's write the story with programming language

Yeah, let's do it. The above sequence of events is a set of statements we can put logically in functions.

First Robin orders the pizza. The app registers the order by invoking a function, like this:

```js
orderPizza('Veg', 'Cheese Barbeque');
```

Now the `orderPizza()` function living somewhere on the PizzaHub server may do some of these actions (it may actually do a lot more than this but let's keep it simple):

```js
function orderPizza(type, name) {
    console.log('Pizza ordered...');
    console.log('Pizza is for preparation');
    setTimeout(function () {
        let msg = `Your ${type} ${name} Pizza is ready! The total bill is $13`;
        console.log(`On the Pizzahub server ${msg}`);
    }, 3000);
}
```

The `setTimeout` function demonstrates that the pizza preparation takes some time. We log a message in the console after the pizza is ready. However, there is a problem!

The message gets logged at the `PizzaHub` side and poor Robin doesn't have any clue about it. We need to `notify` him saying the pizza is ready.

## Introducing a callback function

We need to introduce a callback function now to let Robin know about the status of the pizza. Let's change the `orderPizza` function to pass a callback function as an argument. Also notice that we are calling the `callback` function with the message when the pizza is ready:

```js
function orderPizza(type, name, callback) {
    console.log('Pizza ordered...');
    console.log('Pizza is for preparation');
    setTimeout(function () {
        let msg = `Your ${type} ${name} Pizza is ready! The total bill is $13`;
        callback(msg);
    }, 3000);
}
```

Now, let's make changes to the invocation of the `orderPizza` function:

```js
orderPizza('Veg', 'Cheese Barbeque', function(message){
	console.log(message);
});
```

So now the caller will be notified using the callback function once the pizza is ready. Isn't that so useful?

# In Summary

To Summarize:

* A JavaScript function can accept another function as an argument.
* Passing the function as an argument is a powerful programming concept that can be used to notify a caller that something happened. It is also known as the callback function.
* You can use callback functions to notify the caller depending on a use case. Callbacks are also used to carry out certain tasks depending on the state (pass, fail) of other tasks.
* But be careful – nesting too many callback functions may not be a great idea and may create `Callback Hell`. We will learn more about this in an upcoming article.

Thanks for reading! You can learn more from this open source repository about asynchronous programming. Don't forget to try the quizzes.

%[https://github.com/atapas/promise-interview-ready]

# Before We End...

That's all for now. I hope you've found this article insightful and informative.

Let's connect. You can follow me on [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary), on my [YouTube channel](https://youtube.com/c/TapasAdhikary?sub_confirmation=1), and [GitHub (atapas)](https://github.com/atapas).

Are you interested to lean more about JavaScript asynchronous concepts? Here are a few links to help you out:

* [Synchronous vs Asynchronous JavaScript – Call Stack, Promises, and More](https://www.freecodecamp.org/news/synchronous-vs-asynchronous-in-javascript/)
* [An article series on JavaScript Promises & Async/Await](https://blog.greenroots.info/series/javascript-promises)
* [A video series on JavaScript Asynchronous programming](https://www.youtube.com/watch?v=pIjfzjsoVw4&list=PLIJrr73KDmRyCanrlIS8PEOF0kPKgI8jN)

