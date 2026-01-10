---
title: The JavaScript Concepts You Should Know Before Learning React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-26T19:22:52.000Z'
originalURL: https://freecodecamp.org/news/javascript-concepts-you-should-know-before-learning-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-pixabay-417173--1-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'By Ashutosh Mishra

  React is one of the most popular JavaScript frameworks for building single page
  applications. Needless to say, as a JavaScript framework, it requires you to have
  a good knowledge of JavaScript concepts.

  In this article, we are goin...'
---

By Ashutosh Mishra

React is one of the most popular JavaScript frameworks for building single page applications. Needless to say, as a JavaScript framework, it requires you to have a good knowledge of JavaScript concepts.

In this article, we are going to take a look at some of those JavaScript concepts that you must know before learning React. A good understanding of these topics is fundamental in building large scale React applications. So without further ado, let's get started.

## 1. JavaScript Basics

React is a JS framework and you'll be using JavaScript extensively in your React code. So, it's a no-brainer that you must be aware of the basic JavaScript concepts.

By basics, I mean things like variables, data types, operators, conditionals, arrays, functions, objects, events, and so on.

Having a proper understanding of these concepts is important for you to navigate properly in React, as you'll be using them in every step while building React applications. 

So if you are unsure about these things or want to quickly revise everything again, check out [some of these free courses](https://www.freecodecamp.org/news/learn-javascript-free-js-courses-for-beginners/) or [the freeCodeCamp JavaScript curriculum](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/). The [MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript) docs and [JavaScript.info](https://javascript.info/) are also helpful quick-search references.

## 2. The Ternary Operator

[Ternary Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) is a short, one-line conditional operator to replace if/else. It's really useful when it comes to quickly checking a condition to render a component, updating state, or displaying some text.

Let's compare how the Ternary Operator works with the If/Else statement:

```javascript
// Example of Ternary Operator
condition ? 'True' : 'False'

```

```javascript
// Example of If/Else statement
if(condition) {
    'True'
}
else {
    'False'
}:

```

You can see for yourself how much cleaner and shorter using the Ternary Operator is than using If/Else. 

The way it works is that you write a condition, and if the condition is true, your program will execute the statement after `?`. If the condition is false, the program will execute the statement after `:`

Simple, isn't it?

## 3. Destructuring

[Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) helps us unpack values from arrays and objects and assign them to separate variables in a simple and smooth way. Let's understand it with some code:

```javascript
// With Destructuring
const objects = ['table', 'iPhone', 'apple']
const [furniture, mobile, fruit] = objects

// Without Destructuring
const furniture = objects[0]
const mobile = objects[1]
const fruit = objects[2]

```

In the above example, Destructuring saved us 3 lines of code and made the code cleaner. Now let's see another example of passing props in React with destructuring:

```javascript
// With Destructuring Ex-1
function Fruit({apple}) {
    return (
        <div>
            This is an {apple}
        </div>
    )
}

// With Destructuring Ex-2

function Fruit(props) {
    const {apple, iphone, car} = props
    return (
        <div>
            This is an {apple}
        </div>
    )
}

// Without Destructuring
function Fruit(props) {
    return (
        <div>
            This is an {props.apple}
        </div>
    )
}

```

Notice how you have to use `props` again and again when you don't use destructuring in your props. 

Destructuring makes our code cleaner and saves us from using the keyword **props** every time you use a prop variable. There's [more to destructuring](https://www.freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects/) and you will learn those things when you start building apps in JavaScript and React.

## 4. The Spread operator

The [Spread Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) was introduced to JavaScript in ES6. It takes an [iterable](https://www.freecodecamp.org/news/demystifying-es6-iterables-iterators-4bdd0b084082/) and expands it into individual elements.

A common use case of the spread operator in React is copying the values of an object into another object during a state update to merge the properties of both objects. Look at the below syntax:

```javascript
const [person, setPerson] = useState({
    id: '',
    name: '',
    age: ''
});

 setPerson([
            ...person,
            {
                id:"1",
                name: "Steve",
                age:"25"
            }
        ]);

```

In the above example, `...person` copies all the values of the person object in the new state object which is then further replaced by other custom values with the same properties, which updates the state object.

This was one of the many use cases of the spread operator in React. As your application becomes larger, tools like the spread operator come in handy to handle data in a better and more efficient way.

## 5. Array methods

Array methods are very common when building a medium to large scale application in React. You will always be using some sort of array method in almost every React app you build.

So, take some time to learn these methods. Some of the methods are extremely common like **map()**. You use map() every time you fetch data from an external resource to display it on the UI. 

There are other methods like filter, reduce, sort, includes, find, forEach, splice, concat, push and pop, shift and unshift and so on.

Some of them are common in usage, and some will come rarely in use. The key is to understand the common array methods very well, and just be aware of the existence of the other methods so that whenever you need them, you can quickly learn them.

[Here's a helpful handbook](https://www.freecodecamp.org/news/the-javascript-array-handbook/) on array methods and working with arrays in general in JavaScript so you can learn more.

## 6. Arrow Functions

[Arrow functions](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) allow us to create functions in a simple manner with shorter syntax.

```javascript
// Regular Functions
function hello() {
    return 'hello'
}

// Arrow Functions
let hello = () => 'hello'

```

Both functions in the above code snippet work the same, but you can see that the arrow function is much cleaner and shorter. The empty () in the above syntax are for arguments. Even if there are no arguments, these brackets should be present.

However, you can skip these brackets if there is only one argument present in the function, like this:

```javascript
let square = num => num * num

```

In one-liner arrow functions, you can skip the **return** statement. You can also declare a multiline arrow function by using curly braces {} similar to regular functions.

```javascript
let square = num => {
    return num * num
}

```

## 7. Promises

You use [promises](https://www.freecodecamp.org/news/what-is-promise-in-javascript-for-beginners/) to handle [asynchronous operations](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous) in modern JavaScript. Once you create a promise in JavaScript, it can either succeed or fail – known as being resolved or rejected in JavaScript terminology.

Promises in JavaScript, in some way, can also be compared to the promises we humans make. Just like human promises are driven by the future implementation of a certain action, promises in JavaScript are about the future implementation of the code, resulting in either it being resolved or rejected.

There are 3 states of a promise:

1. **Pending** – When the final result of the promise is yet to be determined.
2. **Resolved** – When the promise is successfully resolved
3. **Rejected** – When the promise is rejected.

Once a promise is successfully resolved or rejected, you can use a **.then()** or **.catch()** method on it.

* The **.then()** method is called when a promise is either resolved or rejected. It takes 2 callback functions as arguments. The first one is executed when the promise is resolved and the result is received, and the second one is an optional argument in case the promise is rejected.
* The **.catch()** method is used as an error handler and is called when the promise is rejected or has an error in execution.

Enough theory, let's end this section with an example of a promise, including the usage of the `.then()` and `.catch()` methods:

```javascript
let promise = new Promise((resolve, reject) => {
  const i = "Promise";
  i === "Promise" ? resolve() : reject(); // Checkout the above Ternary Operator section to better understand the syntax
  }
);

promise.
    then(() => {
        console.log('Your promise is resolved');
    }).
    catch(() => {
        console.log('Your promise is rejected');
    });

```

## 8. The Fetch API

The [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) allows us to make async requests to web servers from the browser. It returns a promise every time a request is made which is then further used to retrieve the response of the request.

A basic fetch() takes one argument, the URL of the resource you want to fetch. It then returns another promise that resolves with a `Response` object. This **Response** object is the representation of the HTTP response.

So, to get the JSON content from this promise, you have to use the **.json()** method on the Response object. This at last will return a promise that resolves with the result of the parsed JSON data from the response body.

It might be a little confusing, so pay close attention to the example below:

```javascript
fetch('http://example.com/books.json') // fetching the resource URL
  .then(response => response.json()); // calling .json() method on the promise
  .then(data => setState(data)); // updating the state with the JSON data

```

## 9. Async/Await

[Async/Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) functionality provides a better and cleaner way to deal with Promises. JavaScript is synchronous in nature and async/await helps us write promise-based functions in such a way as if they were synchronous by stopping the execution of further code until the promise is resolved or rejected.

To make it work, you have to first use the **async** keyword before declaring a function. For example, `async function promise() {}`. Putting **async** before a function means that the function will always return a promise.

Inside an async function, you can use the keyword `await` to suspend further execution of code until that promise is resolved or rejected. You can use **await** only inside of an **async** function.

Now, let's quickly finish off this section with an example:

```javascript
async function asyncFunction() {
    let promise = new Promise(resolve => {
        resolve();
    });
    let response = await promise; // further execution will be stopped until the promise is resolved or rejected
    return console.log(response);
}

```

You can learn more about async and await [in this in-depth guide](https://www.freecodecamp.org/news/javascript-async-await-tutorial-learn-callbacks-promises-async-await-by-making-icecream/).

## 10. ES modules and Import/Export

[Modules](https://www.freecodecamp.org/news/javascript-modules-beginners-guide/) were introduced in JavaScript in ES6. Each file is a module of its own. You can carry out objects, variables, arrays, functions, and so on from one file and use them in another. This is referred to as importing and exporting modules.

In React, we use the ES6 modules to create separate files for components. Each component is exported out of its module and imported to the file where it is to be rendered. Let's learn this with an example:

```javascript
function Component() {
    return(
        <div>This is a component</div>
    )
}

export default Component

```

```javascript
import Component from './Component'

function App() {
    return (
        <Component />
    )
}

```

In React, you have to render every component you declare in the App.js component. 

In the above example, we created a component called **Component** and exported it with our code `export default Component`. Next, we go to **App.js** and import the **Component** with the following code: `import Component from './Component'`.

## **Conclusion**

You've reached the end of the article! So far we have covered JavaScript basics including the Ternary Operator, Destructuring, Spread Operator, Array methods, Arrow functions, Promises, Fetch API, Async/Await, and ES6 Modules and Import/Export.

I hope you have learned a lot from this article and and understand some of the important JavaScript concepts and why you need to learn them thoroughly before jumping into React.

This article is not an alternative to learning these concepts thoroughly on your own. I have only given a general introduction to them and why are they important. Now it's up to you how you learn these things and build your knowledge from here. Best of luck with the journey!

You can use the resources throughout the article to dive deeper into these important concepts.  
  
Check out my [blog](https://fullstackstage.com) to read more quality content like this. Reach out to me on [Twitter](https://twitter.com/ashutoshmishrae) if you have a question to ask or want to say 'hi'. 

