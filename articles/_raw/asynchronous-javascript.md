---
title: How Asynchronous JavaScript Works
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2023-02-17T18:37:03.000Z'
originalURL: https://freecodecamp.org/news/asynchronous-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-zhang-kaiyv-1168940.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In this tutorial, you''ll learn all about Asynchronous JavaScript.

  But before we dive into that, we need to make sure you understand what Synchronous
  code is and how it works.

  What is Synchronous Code?

  When we write a program in JavaScript, it execute...'
---

In this tutorial, you'll learn all about Asynchronous JavaScript.

But before we dive into that, we need to make sure you understand what Synchronous code is and how it works.

## What is Synchronous Code?

When we write a program in JavaScript, it executes line by line. When a line is completely executed, then and then only does the code move forward to execute the next line.

Let's look at an example of this:

```javascript
let greet_one = "Hello"
let greet_two = "World!!!"
console.log(greet_one)
for(let i=0;i<1000000000;i++){
}
console.log(greet_two);
```

Now if you run the above example on your machine you will notice that `greet_one` logs first. Then the program waits for a couple of seconds and then logs `greet_two`. This is because the code executes line by line. This is called synchronous code.

This creates lot of problems. For example, if a certain piece of code takes 10 seconds to execute, the code after it won't be able to execute until it's finished, causing delays.

## What is Asynchronous Code?

With asynchronous code, multiple tasks can execute at the same time while tasks in the background finish. This is what we call non-blocking code. The execution of other code won't stop while an asynchronous task finishes its work.

Let's see an example of asynchronous code:

```javascript
let greet_one = "Hello"
let greet_two = "World!!!"
console.log(greet_one)
setTimeout(function(){
    console.log("Asynchronous");
}, 10000)
console.log(greet_two);
```

In the above example, if you run the code on your machine you will see `greet_one` and `greet_two` logged even there is code in between those 2 logs.

Now, setTimeout is asynchronous so it runs in background, allowing code after it to execute while it runs. After 10 seconds, `Asynchronous` will print because we set a time of 10 seconds in setTimeout to execute it after 10 seconds.

In this tutorial, we will study asynchronous JavaScript in detail so you can learn how to write your own asynchronous code. I just wanted to give you a taste of async JavaScript using in-built functions to whet your appetite.

# How Callbacks Work in JavaScript

> ["A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action."](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function) ([MDN](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function))

Let's look at a code example to see why using callbacks instead would be helpful:

```javascript
function compute(action, x, y){
    if(action === "add"){
        return x+y
    }else if(action === "divide"){
        return x/y
    }
}

console.log(compute("add",10,5))   
console.log(compute("divide",10,5))
```

In the above example, we have two operations. But what if we want to add more operations? Then the number of if/else statements would increase. This code would be lengthy, so we use callbacks instead:

```javascript
function add(x,y){
    return x+y
}

function divide(x,y){
    return x/y
}

function compute(callBack, x, y){
    return callBack(x,y)
}

console.log(compute(add, 10, 5))    // 2
console.log(compute(divide, 10, 5))
```

Now when we call `compute` with three arguments, one of them is an operation. When we enter in the compute function, the function returns a function with a given action name. It, in response, calls that function and returns the result.

## Welcome to Callback Hell

Callbacks are great, but you don't want to use them excessively. If you do, you'll get something called "callback hell". This happens when you nest callbacks within callbacks many levels deep.

The shape of callback hell is like a pyramid and is also called the “pyramid of doom”. It makes the code very difficult to maintain and understand. Here's an example of callback hell:

```javascript
setTimeout(() =>{
    console.log("One Second");
    setTimeout(() =>{
        console.log("Two Seconds");
        setTimeout(() =>{
            console.log("Three Seconds");
            setTimeout(() =>{
                console.log("Four Seconds");
                setTimeout(() =>{
                    console.log("Five Seconds");
                }, 1000)
            }, 1000)
        }, 1000)
    }, 1000)
}, 1000)
```

When one second has passed, the code logs "one seconds". Then there's another call which runs after one more second and logs "two seconds" and it goes on and on.

We can escape this callback hell using something call `Promises` in asynchronous JavaScript.

# How Promises Work in JavaScript

A promise is placeholder for the future result of an asynchronous operation. In simple words, we can say it is a container for a future value.

When using promises, we don't need to relay on callbacks which helps us avoid callback hell.

Before showing you how promises work through code, I'll explain promises using the analogy of a lottery ticket.

Promises are like lottery ticket. When we buy a lottery ticket, it says we will get money if our outcome is right. This is like a promise. The lottery draw happens asynchronously, and if the numbers match, we receive the money which was promised.

Now let's look at a code example:

```javascript
const request = fetch('https://course-api.com/react-store-products')
console.log(request);
```

The above code is using fetch for a request from an API. It returns a promise which will get a response from the server.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1212.png align="left")

This is how a promise looks. It has a particular promise state and result. When a promise is created it runs asynchronously. When the given task is completed, then we say the promise is settled. After the promise is settled, we can have either a fulfilled or rejected promise state based on the outcome of the promise. We can handle these different states in different ways in our code.

### How to Consume Promises

We can consume a promise using the then() method on the promise. Producing code is code that can take some time to complete. Consuming code is code that must wait for the result.

So if we consume a promise, this means that when we make a request, we wait for the result. Then after result arrives, we perform some operation on those results.

Let's continue using the above example to understand how we can consume a promise.

```javascript
const request = fetch('https://course-api.com/react-store-products').then((response) =>{
    console.log(response);
    return response.json()
}).then((data) =>{
    console.log(data);
})
```

We make a request to the country API. Then, after the fetch request, we use the `then()` method to consume the promise. After that, we return a bunch of information like header, status, and so on (you can see it in the below output image).

So we specifically need data which we need to convert to JSON which returns a promise. The data which is returned when we make a API request gets returned in the form of a promise.

To handle that promise, we again use the then() method to log data from the response. Using multiple `then()` methods on a single request is called **chaining promises.**

![Image](https://www.freecodecamp.org/news/content/images/2023/01/121212.png align="left")

## How to Handle Rejected Promises

Consuming promises is good and all, but it's also very important to learn how to handle rejected promises. In real world situations, there could be times when our app crashes due to not handling rejected promises properly.

So let's take an example: we will put our promises in a function called `call()`. In HTML, we will create a button and add an event listener to it. When we click on the button it will call the `call()` function.

Here's what that looks like:

`index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Promises</title>
</head>
<body>
    
    <button class="btn">Request</button>
    <script src="./script.js"></script>
</body>
</html>
```

`script.js`:

```javascript
function call(){

    const request = fetch('https://course-api.com/react-store-products').then((response) =>{
        console.log(response);
        return response.json()
    }).then((data) =>{
        console.log(data);
    })

}

const btn = document.querySelector("button")
btn.addEventListener("click", function(){
    call();
})
```

Why are we doing this? We are setting the promise up to get rejected. Once we run this code, go to inspect and select the network tab. Set No throttling to offline and click on the button to send the request. You will get a rejected promise.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/1111.png align="left")

Once we click on the button, we will get error which is caused by no internet connection.

This situation can happen in the real world if a user's internet connection is slow. We are making an API request for which we need internet with decent speed. Sometimes the client might have an issue with their internet. This can lead to rejected promises which will throw an error which we haven't seen how to handle yet.

Now we will learn to handle this error. We used then() to consume our promises. Similar to that, we will chain the `catch()` method to that promise. Take a look at the following code:

```javascript
function call(){

    const request = fetch('https://course-api.com/react-store-products').then((response) =>{
        console.log(response);
        return response.json()
    }).then((data) =>{
        console.log(data);
    }).catch((err) =>{
        alert(err);
    })

}

const btn = document.querySelector("button")
btn.addEventListener("click", function(){
    call();
})
```

Now the `catch()` method will get an error from the rejected promise and will display the message in an alert.

We get the error because we got a rejected promise which indicates that there is some issue. We can do whatever we want in the catch() block when we encounter an error.

Along with the catch() method, there is one more helpful method called `finally()`. We can chain it to promises which will run no matter whether the promise is accepted or rejected.

```javascript
function call(){

    const request = fetch('https://course-api.com/react-store-products').then((response) =>{
        console.log(response);
        return response.json()
    }).then((data) =>{
        console.log(data);
    }).catch((err) =>{
        console.log(err);
    }).finally(() =>{
        console.log("Will always run");
    })

}

const btn = document.querySelector("button")
btn.addEventListener("click", function(){
    call();
})
```

We can use this `finally()` method for clearing things after the API call. There are many ways to use the `finally()` method.

## How to Create a Promise

We know how to consume promises, but what about creating your own promises? You can do that using `new Promise()`.

You might wonder - why do we need our own promises? Firstly, promises are asynchronous in nature. We can create any task to be asynchronous by creating our own promises. Wecan handle them using the `then()` and `catch()` methods that we learned in the above section.

Once you know how to create promises, you can make any piece of code asynchronous. Then it will not block code execution if the other code running is taking a long time to complete.

Let's see how this works using an example:

```javascript
let lottery = new Promise(function(resolve, reject){
    console.log("Lottery is happening");

    setTimeout(() => {
        if(Math.random() >= 0.5){
            resolve("You Won!!!")
        }
        else{
            reject(new Error("Better luck next time"))
        }
    }, 5000);

})
```

First we created a promise using `new Promise()`. It will have a function with two arguments, `resolve` and `reject`.

We will call `resolve` when our task is successful, and `reject` when the task is unsuccessful. We will use the lottery terminology that I used to explain the concept of promises in the above section.

Let's say if `Math.random()` gives a value below or equal to 0.5, we will win the lottery. Otherwise we will lose the lottery. If the condition is not true, the code throws a new error for better understanding of the error in the console. So we can throw our own custom errors to the user for better understanding.

In the example above, if `Math.random()` is less than 0.5, that means the user lost the lottery. So we throw our custom error `Better luck next time` so that the user understands that they lost the lottery.

Now we will try to consume the promise that we created.

```javascript
let lottery = new Promise(function(resolve, reject){
    console.log("Lottery is happening");

    setTimeout(() => {    
        if(Math.random() >= 0.5){
            resolve("You Won!!!")
        }
        else{
            reject(new Error("Better luck next time"))
        }   
    }, 5000);

})

lottery.then((response) =>{
    console.log(response);
}).catch((err) =>{
    console.log(err);
})
```

We consume the promise using the `then()` method. It will print the response that we provided in `resolve()`. If the promise is rejected we will catch the error in the `catch()` method. The error will come from the `reject()` argument that we mentioned in our own promise.

### How to Consume Promises using Async/await

Consuming promises using the then() method can become messy sometimes. So we have an alternative method to consume promises called async/await.

Just keep in mind that async/await will be using the `then()` method behind the scenes to consume promises.

Why use async/await if we have the `then()` method? We use async/await because it's easy to use. If we start chaining methods to promises using the `then()` method the chain will be very long and gets complex with the addition of multiple then() methods. So async/await is simpler.

Here's how async/await works:

```javascript
const fetchAPI = async function(){
    const res = await fetch('https://cat-fact.herokuapp.com/facts')
    const data = await res.json()
    console.log(data);
}
fetchAPI()
console.log("FIRST");
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/123123.png align="left")

In the above code, we first call the fetchAPI() to see the async behavior of the function. Then it logs "FIRST". So according to asynchronous JavaScript, fetchAPI() should be running in the background and not block the execution of the code. As a result, "FIRST" logs and then the result of fetchAPI is displayed.

Now, if you want to handle asynchronous tasks in your functions, you have to make that function asynchronous using the async keyword before the function. Wherever promises are returned we have to use await before it to consume promises.

Now you might be thinking, how should we handle errors? For that we can use try...catch() to handle errors in async/await.

# Error Handling with `try...catch()`

We can use `try...catch()` in vanilla JavaScript as well. But it can also help us handle errors in asynchronous JavaScript with async/await.

`try...catch()` is similar to the `catch()` method in `then()` using the `catch()` chaining method. Here we will try the code in the `try` block. If that runs successfully then there is no problem.

But if the code in the `try` block has an error, we can catch it in the `catch` block. We can check for errors in the try block and throw our custom error which will be caught in `catch` block. Once we catch the error in the `catch` block we can do whatever we want when we encounter an error.

Let's see how it works with the code example we've been using.

```javascript
const fetchAPI = async function(){
    try{
        const res = await fetch('https://cat-fact.herokuapp.com/fact')
        if(!res.ok){
            throw new Error("Custom Error")
        }
        const data = await res.json()
        console.log(data);
    } catch(err){
        console.log(err);
    }
}


fetchAPI()
console.log("FIRST");
```

First, we wrap the asynchronous code in a `try` block. Then in the `catch` block we log the error. In the try block, if `res.ok` is false we throw our custom error using `throw new Error` which `catch` will get. Then we log it to the console.

# How to Return Values from Async Functions

So far, we've learned about asynchronous code, the `then()` and `catch()` methods, and handling asynchronous code with async/await. But what if we want to return a value from an async function using async/await?

When you're working with asynchronous code, it's often necessary to return a value from an `async` function so that other parts of your program can use the result of the asynchronous operation.

For example, if you're making an HTTP request to fetch data from an API, you'll want to return the response data to the calling function so that it can be processed or displayed to the user.

Well, we can do that. Take a look at the below example:

```javascript
const fetchAPI = async function(){
    try{
        const res = await fetch('https://cat-fact.herokuapp.com/facts')
        if(!res.ok){
            throw new Error("Custom Error")
        }
        const data = await res.json()
        console.log(data);
        return "Done with fetchAPI"
    } catch(err){
        console.log(err);
        throw new Error("Custom Error")
    }
}


console.log(fetchAPI())
```

If we log the fetchAPI we will get back a promise which is fullfilled. You know very well how to handle these promises. We will be doing it using the `then()` method.

```javascript
const fetchAPI = async function(){
    try{
        const res = await fetch('https://cat-fact.herokuapp.com/facts')
        if(!res.ok){
            throw new Error("Custom Error")
        }
        const data = await res.json()
        console.log(data);
        return "Done with fetchAPI"
    } catch(err){
        console.log(err);
        throw new Error("Custom Error")
    }
}


fetchAPI().then((msg) =>{
    console.log(msg);
}).catch((err) =>{
    console.log(err);
})
```

Now when we run our program, we will see our returned msg from the `try` block using async/await logged in the console.

But what if there was an error in async/await? The fetchAPI with the then() method will still log it and it would be undefined.

To avoid this in the catch block again we throw a new error and use the catch() method to catch that error after the then() method.

Try changing the `then()` and `catch()` methods with async/await. This would be a good exercise for you to understand what you've learned in this article.

In JavaScript, there are two common ways to work with asynchronous operations: `then/catch` method chaining and `async/await`. Both methods can be used to handle promises, which are objects that represent the eventual completion (or failure) of an asynchronous operation.

`then/catch` method chaining is a more traditional way to handle asynchronous operations, while `async/await` is a newer syntax that provides a more concise and easier-to-read alternative.

## How to Run Promises in Parallel

Let's say we want to make three requests for three different country capitals. We can do three different fetch calls, each of which will wait for the one above to complete.

```javascript
const fetchAPI = async function(country1,country2,country3){
    try{
        const res1 = await fetch(`https://restcountries.com/v3.1/name/${country1}`)
        const res2 = await fetch(`https://restcountries.com/v3.1/name/${country2}`)
        const res3 = await fetch(`https://restcountries.com/v3.1/name/${country3}`)
        
        
        const data1 = await res1.json()
        const data2 = await res2.json()
        const data3 = await res3.json()
        console.log(data1[0].capital[0]);
        console.log(data2[0].capital[0]);
        console.log(data3[0].capital[0]);
        return "Done with fetchAPI"
    } catch(err){
        console.log(err);
        throw new Error("Custom Error")
    }
}


fetchAPI("canada", "germany", "russia")
```

In the above code, we are making three fetch calls, then converting them to json() and logging their capitals.

But if you hit inspect and see in the network tab, res2 is waiting for res1 to complete and res3 is waiting for res2 to complete.

This can negatively impact our application's performance. Because if a promise is waiting for another promise to complete it can negatively impact the performance of the website.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/321.png align="left")

To overcome this performance issue, we can use something called `**Promise.all**` . It will call three fetch requests simultaneously, which in return will reduce our fetching time and improve our application's performance.

## How to Use Promise.all()

With the help of Promise.all(), we can run multiple promises in parallel which will boost performance. The promise.all() takes an array as an argument which are promises and run them in parallel.

```javascript
let promise1 = new Promise((resolve) =>{
    setTimeout(() =>{
       resolve("First Promise")
    }, 2000)
})

let promise2 = Promise.resolve("Second Promise")

let returnedPromises = Promise.all([promise1,promise2]).then((res) =>{
    console.log(res);
})
```

The result of using promise.all() is that both promises were running in parallel.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/2121.png align="left")

# Wrapping Up

After reading this tutorial, I hope you have a better understanding of asynchronous JavaScript. Feel free to reach out to me for discussion and suggestions.

You can follow me on:

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
    
* [Instagram](https://www.instagram.com/kedar_98/)
