---
title: How Do Closures Work in JavaScript? Explained with Code Examples
subtitle: ''
author: Austin Asoluka
co_authors: []
series: null
date: '2024-05-07T07:13:36.000Z'
originalURL: https://freecodecamp.org/news/understand-javascript-closures
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/hand-1222229_1280-2.jpg
tags:
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Sally and Joe are two love birds. They shared everything with each other\
  \ and soon enough it was almost impossible to think that anything could come between\
  \ them. One day, they had a quarrel which built up to a break up.   \nIt was hard\
  \ for Joe and he ..."
---

Sally and Joe are two love birds. They shared everything with each other and soon enough it was almost impossible to think that anything could come between them. One day, they had a quarrel which built up to a break up.   
   
It was hard for Joe and he wanted "closure". Although Sally already moved on, Joe found closure by taking time to think through the whole experience, recalling "shared memories" and properly introspecting. Even though the relationship had ended, Joe still had something that reminded him of Sally and he was cool with that.

The story ends.

If this is your first time hearing of the term "closure", I'll do you the honor of telling you what it means.  
  
Closure is simply the act of bringing something to an end. Closure in a relationship refers to the sense of peace and understanding you get after the relationship comes to an end. It's that feeling of "letting go" and being able to move on.  
  
For some people, getting closure involves holding on to a "shared memory" with the other party, or something (perhaps an item) that reminds them of the other.

Now that you are familiar with the term closure as it relates to humans, let's try to understand it in terms of the relationship between functions in JavaScript.

In JavaScript, a closure is said to be created when a function retains access to resource(s) declared in it's parent scope even after the parent function has been removed from the call stack.

**Note**: In JavaScript, when a function is said have been popped-off/removed from the stack, it means that the function has completed its life-span (is done executing), and all of its resources have been removed from memory and are no longer accessible.

Think of the call stack like the world, while parent and child are two entities in the world.

In this case, `parent` is the function that has completed execution and logically, everything about it should be out of reach. But because of the concept of closure, even when the relationship between the `parent` and `child` functions has ended – that is, when the parent gets popped-off the stack (removed from the world) – the child function still remembers everything they shared together.

**Note**: Everything they shared together as used above simply means the variables declared in the `parent` function which are used by the `child` function.

```js
function parent () {
	let a = "Az";
    
    return function child () {
        console.log(a);
    }
}
```

In the code snippet above, the variable `a` is what the `parent` and `child` functions shares together.  
  
So even when `parent` gets removed from the call stack, `child` still remembers the value of `a` for as long as it lives.

If you stop reading at this point, you already know what closure is conceptually. But if you want to fully understand it and never forget, we'll have to take a deep dive into the workings of JavaScript.

## Deep Dive into the Concept of Closure.

To really understand closures in JavaScript, you have to be familiar with the following concepts:

1. The concept of functions being first-class citizens in JavaScript. This means that:

* Functions can be assigned to variables as values

```js
const getName = function () {
	return 'Allice'   
};
```

Now you can simply call the function `getName` just like you would call any other function using the parenthesis like this `getName()`  
  
Think of functions as callable objects. This means, just like we can assign objects to variables and pass them around, you can do same with functions. The difference between them is that you can call a function when you need the code in it to execute.

* Functions can be passed into other functions as arguments

```js
setTimeout(getName, 5000)
```

As you can see in the code snippet above, during the invocation of the `setTimeout` function, we passed the `getName` function into it as an argument. Again, this is because functions are simply objects that are callable.   
  
Take note that when we pass the `getName` function into the `setTimeout` function, we are not calling/invoking it. We are simply passing the function as a value.   
  
If we called the function, we'd be passing its return value instead and that's a significant difference there.  
  
I'd also like to bring to your notice that mentioning the name of a function is simply referencing that function. Behind the scene, the function name gets replaced by the function itself.  
  
That is, this code `setTimeout(getName, 5000)` is equivalent to the code below;

```js
setTimeout(function () {
	return 'Allice'   
}, 5000)
```

The function name gets replaced with the function itself during execution just like a regular variable name gets replaced by its value during execution.

* Functions can be returned from other functions.

```js
function multiplyBy (numberToMultiplyBy) {
	return function (numberToMultiply) {
		return numberToMultiply * numberToMultiplyBy
    }
}
```

Taking a close look at the code snippet above, you'll notice that we have a function called `multiplyBy` which expects an argument during invocation and returns a new function.   
  
The interesting thing to notice here is that when we call the returned function, it expects an argument too, but this time, it remembers the argument passed into the original `multiplyBy` function ( `numberToMultiplyBy` ), then multiplies the value passed into itself ( `numberToMultiply` ) with the value passed into its parent function, and returns the result.  
  
Carefully observe the code below which makes use of the higher-order function `multiplyBy`:

```js
const multiplyByTwo = multiplyBy(2)
const result = multiplyByTwo(8)

console.log(result) // 16
```

2.  The concept of Higher-order functions: This is the second concept you need to be aware of to understand closure.

A higher order function is a function which:

* Accepts a function as an argument. For example: `setTimeout`, `Promise`, and so on.
* Returns a function. For example: `multiplyBy` function declared above.
* Or fulfils the first and second items above.

Now that you understand that functions are first-class citizens and you've seen implementations of a higher-order function, we can proceed to talk about closures.

Recall that a closure occurs when a child function holds reference to/remembers a value or resource which belonged to its parent function even after the parent function has been removed from the call stack.

Consider this code:

```js
function sally () {
	let age = 64;
    
    return function joe () {
        const data = {
        	name: "Joe",
            parentName: "Sally",
            parentAge: age
        }
		return data
    }
}
```

In the code snippet above, we can observe that:

* `sally` is the parent function and it declares a scope
* `age` is a variable declared within the `sally` scope
* `joe` is a function which lives in the `sally` scope and is returned by the `sally` function. You should also note that:  
- `joe` defines its own scope which is a child scope of the `sally` scope  
- within the `joe` scope, we make reference to the variable `age` which belongs to `sally` scope (this is where closure happens because `joe` is referring or holding on to a resource/variable which belongs to `sally`).

Because `joe` holds a reference to the variable `age` which belongs to `sally`, even when `sally` has been popped-off the call stack and its scope discarded, `joe` will retain access to the `age` variable because of the concept of closure.

So in the code below:

```js
const joe = sally() // sally is invoked and returns the joe function
const joeyData = joe() // joe function is invoked and returns an object

console.log(joeyData) // we log the object returned.
```

You can observe that even though `sally` is called and popped-off the stack, when you invoke `joe` and log the return value of `joe` to the console, it still remembers the `age` of sally during the execution (which we can access in the returned object like so `joeyData.parentAge`).

## Summary

When a child function refers to variables used in its parent scope, closure occurs.  
Closure is like a memory box which stores all the items of the parent scope that are referred to from the child scope.

A look at the slides below should cement the knowledge you've gained so far and hopefully everything will fall in place.

<iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/361482321f264b4aa170e04776365956" title="JavaScript Closure" allowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 432;" data-ratio="1.2962962962962963"></iframe>

Closures unlocked? Level up your JavaScript skills with more full-stack development tutorials on my [YouTube](https://www.youtube.com/@asoluka_tee) channel. Subscribe now for my next playlist on fundamental JavaScript concepts!

Thanks for reading! Happy coding!

