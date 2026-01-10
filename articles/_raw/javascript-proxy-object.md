---
title: How JavaScript's Proxy Object Works – Explained with Example Use Cases
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-10-31T14:56:30.000Z'
originalURL: https://freecodecamp.org/news/javascript-proxy-object
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Image-defs.001-1.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "In this tutorial, you are going to learn what a proxy object is, along\
  \ with its limitations. \nWe will also look into some of the use cases that demonstrate\
  \ how you can use proxy objects to solve various problems.\nWithout further ado,\
  \ let’s get starte..."
---

In this tutorial, you are going to learn what a proxy object is, along with its limitations. 

We will also look into some of the use cases that demonstrate how you can use proxy objects to solve various problems.

Without further ado, let’s get started.

## Table of Contents

- [Prerequisites](#heading-prerequisites)
- [What is a proxy?](#heading-what-is-a-proxy)
- [How to restrict an object to have a specific property](#heading-how-to-restrict-an-object-to-have-a-specific-property)
- [A small detour – what is the Reflect API](#heading-a-small-detour-what-is-the-reflect-api)?
- [Array slicing like Python](#heading-array-slicing-like-python)
- [Disadvantages of using proxies](#heading-disadvantages-of-using-proxies)
- [Summary](#heading-summary)


## Prerequisites

I would highly recommend going through the following topics to follow along with this tutorial:

- [Basics of JavaScript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics).
- [Object instance methods.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#instance_methods)
- How to use the [apply function in JavaScript.](https://www.freecodecamp.org/news/understand-call-apply-and-bind-in-javascript-with-examples/#how-to-use-the-apply-function-in-javascript)

## What is a proxy?

From [merriam-webster](https://www.merriam-webster.com/dictionary/proxy):

> *A proxy may refer to a person who is authorized to act for another or it may designate the function or authority of serving in another’s stead.*
> 

So a proxy is nothing but a mediator that speaks or operates on behalf of the given party. 

In terms of programming, the word proxy also means an entity that acts on behalf of an object or a system. Since we have this term sorted out, let's understand what it signifies in JavaScript. 

In JavaScript, there is a special object called a Proxy. It helps you create another object on behalf of the original object. 

This new proxy object will act as a mediator between the real world and the original object. In this way, we will have more control over the interaction with the original object. 

Using a proxy is a powerful way to interact with the object rather than interacting directly with it. 

Here is the syntax for declaring a proxy object:

```jsx
new Proxy(<object>, <handler>)
```

The `Proxy` takes two parameters:

- `<object>`: The object that needs to be proxied.
- `<handler>`: An object that defines the list of methods that can be intercepted. These are also called traps.

Let's have a look at a simple example:

```jsx
const books = {
	"Deep work": "Cal Newport",
	"Atomic Habits": "James Clear"
}
const proxyBooksObj = new Proxy(books, {
	get: (target, key) => {
		console.log(`Fetching book ${key} by ${target[key]}`);
		return target[key];
	}
})
```

Here we would like to intercept the `get` functionality of the object `books` so we can log the book name and the author of the book to the console.

To achieve this, we created a new proxy object called `proxyBooksObj`. This object is constructed using the `Proxy` function that we saw earlier. It takes `books` as the object to be proxied, and an object that consists of handler functions that need to be trapped. 

Since we need to intercept the `get` functionality, we added a `get` property that accepts a function. This handler function will accept a function that takes in `target` `key`. 

This was a pretty simple example of proxy in JavaScript. There are various use cases of a proxy – for example, it can help in validation, formatting, notification, and debugging. 

To learn more about the available handlers/traps here is the [list](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy#a_complete_traps_list_example).

Now let's look at an example that will provide us with more clarity on how proxies work.

## How to Restrict an Object to Have a Specific Property

Sometimes it can be useful to restrict users so that they only have a specific property, just like what `useRef` does in React. It only allows editing the `current` property of the object that is returned by `useRef`. 

Let's create a proxy function that will allow the user to only update the `current` property and not allow them to create any other properties.

```jsx
const data = {};

const newProxy = new Proxy(data, {
  set: function (target, key, value) {
    if (key === "current") {
      Reflect.set(target, key, value);
      return true;
    }
    return false;
  }
});

newProxy.current = 1;
newProxy.point = 1; // Throws error
```

Here, since we are dealing with assigning a new value to an existing property or creating a new property, we use the `set` trap function. We need to tap into the set’s internal behavior of the object. 

The `set` handler function will take in the `target`, `key`, and `value` where the target will be the target object, and the key and value are the property and the actual value. 

We make sure that the key is `current`. When it is, we set the value to that property and return true. 

It is important that we return `true` because this handler function expects to follow some [invariants](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#invariants). If we do not want to set the value then we should return `false`.

There is also something to note about each trap function available inside the proxy that is invariant. Invariant is nothing but a condition that needs to be followed by every trap function so that the basic functionality doesn’t change.

Quoting from MDN’s Meta-programming guide:

> [Semantics that remain unchanged when implementing custom operations are called *invariants*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#handlers_and_traps)
> 

### A small detour – what is the Reflect API?

We can also make use of the Reflect API here. JavaScript provides a built-in object that has a set of functions that can help intercept JavaScript operations. This can be operations such as `set`, `get`, `apply`, and so on. 

To know more about the methods the Reflect API provides, you can go through the following [link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect#static_methods). 

With this API, it makes it really simple to manipulate the target object present inside the proxy. A fun fact about Reflect API is that it is not an object that can be instantiated. All the methods provided by it are static.

In the previous example, we tried to return the value present at the property of the object directly by accessing the original object like this: `target[key]`. 

Instead, here we can make use of `get` method of Reflect. So now our above example will look something like this:

```jsx
const books = {
	"Deep work": "Cal Newport",
	"Atomic Habits": "James Clear"
}
const proxyBooksObj = new Proxy(books, {
	get: (target, key) => {
		console.log(`Fetching book ${key} by ${target[key]}`);
		return Reflect.get(target, key);
	}
})
```

Now we know that we can make use of Reflect, but a question arises - why use Reflect?

We use Reflect because it allows us to implement the default behavior of the functions that were present on the original object. Rephrasing in technical terms, this allows us to implement the default forwarding behavior inside the trap functions. 

Also with Reflect we can access internal functions and apply them to the proxy-wrapped object. 

So it's beneficial for us to use Reflect APIs inside our proxy.

## Array Slicing Like Python

Python is a really cool language. A really awesome feature it provides is the way you can slice your arrays. Even Python’s [NumPy](https://www.w3schools.com/python/numpy/numpy_array_slicing.asp) library provides this feature of slicing the array. 

You can simply provide a start index (optional) and end index (optional) separated by a colon. Here is the syntax for slicing an array in Python:

```python
arr[<start>:<end>]
```

From the above syntax it is clear that `start` and `end` signify the `start` and `end` (exclusive) index positions for slicing. 

Here is an example of how you can slice an array in Python:

```python
data = [1,2,3,4]
print(data[1:3]) # Output: [2, 3]
```

Here is how you can do the same in JavaScript:

```jsx
const data = [1,2,3,4]
console.log(data.slice(1,3)) // Output: [2, 3]
```

You need to use the `slice` function to slice the `data` array from index position `1` to index position `3`. 

Note that slicing an array excludes the end index provided in the slice function or in Python’s slicing mechanism.

Wouldn’t it be great if we could achieve Python’s slicing mechanism in JavaScript as well? 

We have again the Proxy object in JavaScript to the rescue. As we have established in an earlier section, proxies are a wrapper around the original object. They help you manage the interaction with the original object. 

Let's again create this proxy object – but this time so that it has the slicing mechanism. Below is the code for implementing the slicing mechanism in JavaScript:

```jsx
const arr = [1,2,3,4];

const arrProxy = new Proxy(arr, {
  get: function (target, key) {
    if (typeof key === "string" && key.includes(":")) {
      let [start, end] = key.split(":");
      if (start === "") {
        start = 0;
      } else if (end === "") {
        end = target.length;
      } else {
        start = parseInt(start, 10);
        end = parseInt(end, 10);
      }

      return Reflect.apply(Array.prototype.slice, target, [start, end]);
    }
    return Reflect.get(target, key);
  }
});

console.log(arrProxy["1:3"]) // [2,3] 
```

Ok a lot of code here, but let's take a step back and understand what’s happening:

- We created a new `proxy` object on top of the array `arr`. Since we are planning to achieve slicing by providing the start and end position separated by a colon, we need to make some modifications on how to do the get functionality of an array.
- To do this, we are going to make use of the `get` trap function that modifies the get mechanism for an array. We make sure to add this trap function as a `get` property inside the `handler` object of the `Proxy`.
- A [get](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/get) trap function accepts `target` and `key` as it arguments. We make use of this to write our logic.
- Since we are doing something like this `arrProxy["1:3"]`, in this case, the key is going to be of type string and it’s going to include`:` in it. Our main condition will be to distinguish on this same condition.
    
```jsx
if (typeof key === "string" && key.includes(":")) 
```
    
Next, we write some conditions that are requirements for the slicing mechanism in Python. Below are the requirements:

- Whenever the `start` index is not provided we should set `start` to 0.
- Whenever the `end` index is not provided we should set `end` to the original array’s length.
- If both of them are provided, then we convert them to integers.

To do this, we need to make use of the [slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) function in JavaScript.

We will be using the [Reflect API’s](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect) [apply](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/apply) method, to execute the function `slice` with this context (`target`) being the original array and arguments to the `slice` function being `[start, end]`.

In the end, if the `key` argument is of any other data type apart from a string, then we directly return the array with the help of `Reflect.get`.

## Disadvantages of Using Proxies

We now know how a proxy works along with its use cases. But it is also important to know some disadvantages of using proxies. 

First of all, while it's cool to use proxies, it is a really really bad choice in scenarios where performance is a critical factor.

Second, no operation proxy forwarding is the mechanism of forwarding all the functionality of the target using a proxy. Here is what proxy forwarding looks like:
    
```jsx
const data = {};
const newData = new Proxy(data, {}); // No trap function.
    
data.point = { x: 1, y: 2};
    
console.log(data);
```
    
This works just fine on regular objects but it won’t work for objects such as DOM nodes or objects that have internal slots. 

For example, doing something like the below will generate an error:
        
```jsx
const x = document.createElement("div")
x.className = "hello"
        
const domProxy = new Proxy(x, {});
        
console.log(domProxy.getAttribute("class")); // Throws typeError
```
        
This happens because the `this` value refers to the proxy object rather than referring to the original object. We can solve this by a get trap function that helps refer to the original object.
        
```jsx
const y = new Proxy(x, {
  get(target, key) {
    const value = Reflect.get(target, key);
    if(typeof value === "function"){
      return value.bind(target)
    }
    return value;
  }
});
        
console.log(y.getAttribute("class")); // Output: hello
```

## Summary

In this article, we learned about proxies in JavaScript along with their use cases. We also took a peek into some disadvantages of proxies.

If you like the idea of using proxies, then you can take it up a notch and try using them in various scenarios of validation or replicating some library functions such as [lodash’s get](https://lodash.com/docs/4.17.15#get) and [set](https://lodash.com/docs/4.17.15#set) functions.

That’s all. Thanks for reading.

Follow me on [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar), and [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).


