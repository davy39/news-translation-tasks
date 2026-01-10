---
title: How to use Promises in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-14T05:58:00.000Z'
originalURL: https://freecodecamp.org/news/promises-in-javascript-explained-277b98850de
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pkunQjHG1AknVCa_-gXJVA.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Prashant Ram

  Promises in JavaScript are a way to handle async calls. Before Promises were introduced
  in JavaScript ES6, async calls in JavaScript were handled using callback functions.
  Promises provide a cleaner, more elegant syntax and methodolog...'
---

By Prashant Ram

Promises in JavaScript are a way to handle async calls. Before Promises were introduced in JavaScript [ES6](http://es6-features.org/#Constants), async calls in JavaScript were handled using callback functions. Promises provide a cleaner, more elegant syntax and methodology to handle async calls.

### A simple Promise in JavaScript

Let us begin by looking at the syntax and structure of a simple Promise in JavaScript. You can see the JSFiddle link to the code [here](https://jsfiddle.net/prashantram/brzdg4g5/).

```
// Promise                   // A Promise structure has 2 parts 
```

```
//First part//create the Promise and define the success/not success conditionslet promise1 = new Promise( (resolve, reject) => {let dataReceivedSuccessfully = false; 
```

```
if (dataReceivedSuccessfully)   resolve('Data Available!'); 
```

```
if (!dataReceivedSuccessfully)   reject('Data Corrupted!'); 
```

```
}) 
```

```
//Second part //define the actions for when the conditions are fulfilled  promise1.then( (message) => {   console.log(message);    }).catch( (message) => {      console.log(message);})
```

A Promise consists of two parts:

1. The first part **creates the Promise** and **defines the conditions** of what is considered `successful` and `not successful`.
2. The second part **describes what to do** when the `successful` condition is met with the `resolve()` function definition, and what to do when the `not successful` condition is met with the `reject()` function definition.

Thus, in the first part of a Promise we create the Promise, using the in built `Promise()` object in JavaScript ES6:

```
let promise1 = new Promise( (resolve, reject) => { ... } );
```

In the function body, we define **when** to invoke the `resolve()` function and `reject()` function:

```
if (dataReceivedSuccessfully)   resolve('Data Available!');
```

```
if (!dataReceivedSuccessfully)   reject('Data Corrupted!');
```

In the second part of a Promise, we **define** the actual `resolve()` and `reject()` functions:

```
promise1.then(  (message) => {...do this on resolve()...})        .catch( (message) =>; {...do this on reject()....});
```

Let’s add some detailed inline comments to the code above to drive home this point:

```
// PROMISE                   /* Every Promise() structure has 2 parts */
```

```
//First Part           /* Create the Promise() and define the conditions of what is considered successful and not successful.*/
```

```
let promise1 = new Promise( (resolve, reject) => {
```

```
let dataReceivedSuccessfully = false; /* This is an arbitrary variable and is NOT part of the Promise */
```

```
if (dataReceivedSuccessfully) //This condition is considered successful, hence invoke resolve()  resolve('Data Available!');
```

```
if (!dataReceivedSuccessfully) //This condition is considered NOT successful, hence invoke reject()  reject('Data Corrupted!');
```

```
})
```

```
//Second Part/* Define what to do when the successful condition(i.e. resolve()) is / met, and what to do when the not successful condition(i.e.        / reject()) is met. */
```

```
promise1.then( (message) => {   console.log(message);/* define the resolve() function, / in other words, what to do when the promise is successful. */
```

```
}).catch( (message) => {    console.log(message);/* define the reject() function, / in other words, what to do when the promise is NOT successful.*/
```

```
})
```

Go ahead and run the code above in [JSFiddle](https://jsfiddle.net/prashantram/brzdg4g5/) using the Chrome browser and open the Inspect(Console). Notice that the `Promise()` executes, and it shows the message “Data Corrupt!” in the console.log. If you now update the boolean `dataReceivedSuccessfully=true` and run the code again, you will get “Data Received!” message in the console.log.

Note that these messages are being passed from the `resolve()` and `reject()` functions and are being executed in the `.then()` and `.catch()` section of the `Promise`.

You will also notice the `‘message’` string that is passed by the `resolve()` and `reject()` functions — `resolve(“Data Received”)` and `reject(“Data Corrupt”)`.

When the `resolve()` and `reject()` functions are invoked, they can be invoked with arguments — these can be strings, arrays, objects or nothing. More on this later.

In our simple example, the argument passed by the `resolve()` and `reject()` functions are of type **string**. The arguments from the `resolve()` function in the first part of the `Promise` are meant for the `.then()` function in the second part of the `Promise`. In the same way, the arguments from the `reject()` function in the first part of the `Promise` are meant for the `.catch()` function in the second part of the `Promise`.

Let us also take a deeper look at the part creating the `Promise`.

```
let promise1 = new Promise( (resolve, reject) => { ... } );
```

The `Promise()`object is a built-in object in JavaScript ES6. When this object is instantiated using the `new` keyword, it takes a function as an argument. This single function in turn takes two arguments, each of which are also functions — `resolve` and `reject`. So keep in mind that the `(resolve, reject)` arguments in Promises are actually callback functions.

```
let promise1 = new Promise( (fn1, fn2) => { ...} );
```

Since `fn1` and `fn2` are callback functions. This means they can be invoked within the Promise, which is exactly what happens when we call `resolve(‘Data Received!’)` and `reject(‘Data Corrupt!’)`.

### Passing Objects and Arrays in `resolve()` and `reject()`

In the previous example, we used a simple string message as an argument for the `resolve()` and `reject()` functions. It is important to note that the `resolve()` and `reject()`functions **take only a single argument**. Now what do you do if you want to pass more than one piece of information, since you are limited to using only a single argument?

The `resolve()` and `reject()` functions allow you to pass only a single argument, but that single argument can be of type string, number, boolean, array or object.

The way you can pass more than one piece of information in the `resolve()` and `reject()` functions is to **pass it as an object or an array**.

The following example illustrates how you can pass multiple pieces of information using the single argument of the `resolve()` and `reject()` functions, by passing them as part of a single large object or an array.

```
//Passing Arrays and Objects as arguments
```

```
let dataReceivedSuccessfully = true;
```

```
//define the Promisepromise1 = new Promise( (resolve, reject) => {
```

```
//construct the array or object you want to passlet some_array = [1, 2, 3, 4, 5];  let some_object = {color:'red', person:{ name: "mike", age: '35'} };
```

```
//define under what conditions to invoke resolve() and reject()  if (dataReceivedSuccessfully)     resolve(some_array);     //passing an Array as the single argument  else     reject(some_object);     //passing an Object as the single argument});
```

```
//define the executing function for resolve() and reject()  promise1.then( (message) => {     console.log(`${message}`); //if dataReceivedSuccessfully=true, console.log shows 1,2,3,4,5
```

```
}).catch( (message) => {     console.log(`error`);     console.log(`${message.color}`);//if dataReceivedSuccessfully=false, console.log shows "error" "red"
```

```
})
```

Open this example in [JSFiddle](https://jsfiddle.net/prashantram/dzwrbvp1/) and run it. Open the Inspect element in the Chrome browser and go to the Console. Here you will see that the appropriate messages are displayed based on the passing parameter.

It is also possible to leave the passing parameters **empty** in Promises.

### More than one Promise

Now that we understand the basic syntax and structure of Promises, let’s kick it up a notch by using more than one Promise.

When multiple promises are used, they can be chained together — with the `.then()` function of the **first** Promise returning the **next** Promise, and so on.

In the following example, we create multiple Promises. This might be a typical case where we want to handle multiple async calls. You can see the JSFiddle link to the code [here](https://jsfiddle.net/prashantram/5tgqtbkm/).

```
var requestComplete = true;
```

```
promise1 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("data received from 1");})
```

```
promise2 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("data received from 2");})
```

```
promise3 = new Promise((resolve, reject) => {  setTimeout( ()=>{ resolve("data received from 3");
```

```
 },2000);//We simulate a delay in data receipt by using setTimout() 
```

```
})
```

```
promise1.then((message) => {     console.log(message);     return promise2; //return promise2 when promise1 resolves.}).then((message) => {     console.log(message);     return promise3; //return promise3 when promise2 resolves.}).then((message) => {     console.log(message); //resolve promise3.})
```

Note that in the above example, Promises resolve in sequence one after another.

The `console.log` output of the above is:

```
   ‘data received from 1’   ‘data received from 2’ (....there will be a 2 second simulated delay)   ‘data received from 3’
```

### Promises in Action

In many cases, we are not interested it the sequential execution of Promises. Rather, we are interested whether all Promises were successfully executed or not. In other cases, we may be interested in whether any one Promise finished execution.

The real world cases for this may be when trying the fetch the same data from multiple CDNs. In this case, we might be interested in resolving the Promise as soon as data from any one of the CDNs becomes available.

These two cases can be handled in Promises using the `.all()` and `.race()` methods.

#### Promise.all() and Promise.race()

The `.all()` method evaluates all Promises and executes the `.then()` method when all the Promises within its `Promise` array have finished.

The `.race()` method, on the other hand, executes as soon as any one Promise from the `Promise` array has completed execution. The `.race()` method does not wait for the other Promises and resolves as soon as any one of the Promises is resolved.

The following example shows the syntax and output of each of these conditions.

```
// .all() example
```

```
var requestComplete = true;
```

```
promise1 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("data received from 1");})
```

```
promise2 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("data received from 2");})
```

```
promise3 = new Promise((resolve, reject) => {    setTimeout(()=>{  resolve("data received from 3");  }, 2000);
```

```
})
```

```
Promise.all([promise1, promise2, promise3]).then( (message) => {  console.log(message);
```

```
})
```

When you run this code, the Promise waits for all the Promises within the promise array to complete. Since the `promise3` has a delay of 2 seconds, no output is shown for 2 seconds.

Only after the 2 seconds, once all of the Promises resolve, does the `console.log` output the `message`.

In this case, the `message` is an array that contains the messages from all of the three promises:

```
0:”data received from 1"
```

```
1:”data received from 2"
```

```
2:”data received from 3"
```

```
length:3
```

The following code shows the syntax and structure of the `.race()` method:

```
// .race() example
```

```
var requestComplete = true;
```

```
promise1 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("data received from 1");})
```

```
promise2 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("data received from 2");})
```

```
promise3 = new Promise((resolve, reject) => {  setTimeout(()=>{resolve("data received from 3");}, 2000);})
```

```
Promise.race([promise1, promise2, promise3]).then( (message) => {  console.log(message);
```

```
})
```

When the `.race()` example is run, the `console.log` outputs immediately. It does not wait for the `promise3` to finish execution. It executes the `.then()` function as soon as any one of the Promises resolves.

In this case, the `message` is not an array but instead contains as its argument the arguments of the first Promise resolved — it contains only a single string in this case:

```
data received from 1
```

### A Real World example using Promises

Okay awesome! I think we are now ready for some real world implementations of Promises.

We will use Promises to asynchronously fetch data from two different websites. We will use the built-in `XMLHttpRequest()` object for this and monitor the `request.onreadystatechange()` method to watch for responses using `request.status` and `request.response`.

The first site we are accessing is the NASA API, and the second site is using the Github API. I simply chose these APIs since they were open key.

We will use the `Promise.race()` method to see which of the two sites responds faster. You can see the JSFiddle link to the code [here](https://jsfiddle.net/prashantram/p776txjk/5/).

```
promise1 = new Promise((resolve, reject) => {
```

```
  let request = new XMLHttpRequest();  let url = "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo";
```

```
  request.open('GET', url);  request.send();
```

```
  console.log("NASA " + request.readyState);
```

```
  request.onreadystatechange = () => {    console.log("NASA " + request.readyState);
```

```
if (request.readyState === 4) {      //console.log(request.response);      console.log("Response from NASA API: " + request.status);      resolve("NASA wins the race!");    }  }
```

```
})
```

```
promise2 = new Promise((resolve, reject) => {
```

```
  let request = new XMLHttpRequest();  let url = 'https://api.github.com/users/mralexgray/repos';
```

```
  request.open('GET', url);  request.send();
```

```
  console.log("GITHUB " + request.readyState);
```

```
  request.onreadystatechange = () => {    console.log("GITHUB " + request.readyState);
```

```
if (request.readyState === 4) {      //console.log(request.response);      console.log("Response from GITHUB API: " + request.status);      resolve("GITHUB wins the race!");    }  }
```

```
})
```

```
Promise.race([promise1, promise2]).then((message) => {  console.log(message);})
```

You can run this code on JSFiddle several times, and see on average which site responds faster. I found the GitHub site to be faster on average.

### Concluding Remarks

Promises are a great way to handle asynchronous calls in JavaScript. When used correctly, they allow you to elegantly manage code.

Happy Coding!

[**_Follow me on Medium_**](https://medium.com/@prashantramnyc) **_for the latest updates and posts!_**

**Other Articles:**   
[How to build a simple Sprite animation in JavaScript](https://medium.com/@prashantramnyc/how-to-build-a-simple-sprite-animation-in-javascript-b764644244aa)

[The Microservices Approach to Mobile Application Development](https://medium.com/@prashantramnyc/microservices-architecture-for-mobile-application-development-part-i-20b4f4089a24)

