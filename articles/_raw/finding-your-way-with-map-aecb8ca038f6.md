---
title: Finding Your Way With .Map()
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-01-24T18:01:19.000Z'
originalURL: https://freecodecamp.org/news/finding-your-way-with-map-aecb8ca038f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1m6Z6xg7J2DDFOsK_-HgBw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: The verbosity and elegance of a solution are driven by the tools we have
  to solve a particular problem. While the goal of problem-solving is to solve a problem,
  it’s methods should move towards the most elegant way possible. The journey towards
  such ...
---

The verbosity and elegance of a solution are driven by the tools we have to solve a particular problem. While the goal of problem-solving is *to solve a problem*, it’s methods should move towards the most elegant way possible. The journey towards such a solution, however, seems to lie on an asymptotic curve. Perfection gets closer and closer but forever remains out of reach.

#### The Problem

Imagine having an array and needing to change each element in the array. Maybe, for example, taking an array of heights in inches and needing to convert them to centimeters. Or possibly converting an array of temperatures in Celcius to Fahrenheit. If you are new to programming, your mind might immediately go to some form of a loop. And, guess what? I’m sure you could make it work.

However, I am here to give you one more tool — something to get you just a little closer to elegant: `Array.prototype.map()`.

The `map` method allows us to transform each element of an array, without affecting the original array. It’s considered a *higher-order function* and a functional-programming technique because it takes a function as an argument and we are performing computation without mutating the state of our application.

> `Map` is a property that is inherited from the array prototype. Prototypes provide built-in-methods that objects come with (arrays are special types of objects in the eyes of JavaScript). While `map` may be a little more foreign, this prototype is no different than, for example, the `Array.length` prototype. These are simply methods that are baked into JavaScript. Array prototypes can be added and mutated by: `Array.prototype.<someMethodHere>` = ...

By the end of this lesson, we will discover how `map` works and write our own array prototype method.

#### So what does .map() do?

Let’s say you have an array of temperatures in Celsius that you want to convert to Fahrenheit.

There are a number of ways to solve this problem. One way may be to write a `for` loop to create an array of Fahrenheit temperatures from the given Celsius temperatures.

With the `for` loop we might write:

```js
const celciusTemps = [22, 36, 71, 54];
const getFahrenheitTemps = (function(temp) {
   const fahrenheitTemps = [];
   for (let i = 0; i < celciusTemps.length; i += 1) {
      temp = celciusTemps[i] * (9/5) + 32
      fahrenheitTemps.push(temp);
   }
   console.log(fahrenheitTemps); [71.6, 96.8, 159.8, 129.2
})();
```

A couple things to note:

1. It works.
    
2. We use an Immediately Invoked Function Expression (IIFE) to avoid also having to call the function.
    
3. It’s a bit verbose and not very elegant.
    

`Map` allows us to take the above code and refactor it to the following:

```js
const fahrenheitTemps = celciusTemps.map(e => e * (9/5) + 32);
console.log(fahrenheitTemps); // [71.6, 96.8, 159.8, 129.2]
```

#### So how does map work?

`Map` takes a function and applies that function to each element in the array. We could write `map` a bit more verbose with ES5 to see this a bit more clearly.

```js
const fahrenheitTemps = celciusTemps
   
   .map(function(elementOfArray) {
      return elementOfArray * (9/5) + 32;
   });
console.log(fahrenheitTemps); // [71.6, 96.8, 159.8, 129.2]
```

If our map function could say what it is doing, it would say:

“For every element in the array, I multiply it by (9/5), then add 32. When that is done, I return the result as an element in a new array called fahrenheitTemps.”

Let’s look at a more common use case. Let’s assume we have an array of `people` objects. Each object has a `name` and `age` key-value-pair. We want to create a variable that is just the names of everyone in the array. With our `for` loop method we might write:

```js
const people = [
   {name: Steve, age: 32},
   {name: Mary, age: 28},
   {name: Bill, age: 41},
];
const getNames = (function(person) {
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // [Steve, Mary, Bill];
})();
```

With `map`:

```js
const names = people.map(e => e.name);
console.log(names) // [Steve, Mary, Bill];
```

Notice here we don’t transform anything, we simply return the key-value-pair `name`.

Again, the `for` loops works. But, it is verbose, and we have to create a new custom function every time we want to do a different transformation. A principal part of programming is writing DRY code (Don’t Repeat Yourself). These higher-order functions such as map, allows us to do more complex programming in fewer lines of code than we could without them.

#### Reinventing the wheel:

To better understand what is happening under the hood, we will make our own map function that we will attach to the array prototype.

First, to attach a prototype method to an Array, we will write:

`Array.prototype.<yourMethodHere>`

so for us:

`Array.prototype.myMap = <our code>`

But, what will our code be?

We already have the logic we need from the `for` loops above. All we need to do is refactor it a bit. Let’s refactor the last function we wrote `getNames()`.

Remember, this function took a person (in other words an element of our array), did a custom transformation to that element (with the `for` loop and some logic), and returned an array of names (or a new array).

```js
const getNames = (function(person) {
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // [Steve, Mary, Bill];
})();
```

First, let’s change the name of our function. After all, this new method doesn’t assume to know what kind of array it will be acting upon:

```js
const myMap = (function(person) { //Changed name
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // [Steve, Mary, Bill];
})();
```

Second, we are creating our own version of `.map()`. We know this will take a function that the user provides. Let’s change the parameter our function takes:

```js
// It is a bit verbose, but a very clear parameter name
const myMap = (function(userProvidedFunction) { 
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // [Steve, Mary, Bill];
})();
```

Finally, we have no idea what array this method will act on. So, we can’t refer to `people.length` but we *can* refer to `this.length`. `this`, will return the array the method is acting on. Also, let's clean up some of the other variable names:

```js
const myMap = (function(userProvidedFunction) { 
   // change variable name
   const newArr = [];
   // use "this.length"   
   for (let i = 0; i < this.length; i += 1) { 
   
      // use "this[i]", and change variable name      
      const newElement = this[i];
  
      // update the array we push into
      newArr.push(newElement); 
   }
   // Return the newly created array
   return newArr; 
})();
```

We’re almost there, but there is one thing we are forgetting. We haven’t transformed the array! All we’ve done above is return the old array. We have to apply the user-provided function to each element of the array:

```js
const myMap = (function(userProvidedFunction) { 
   const newArr = [];
   for (let i = 0; i < this.length; i += 1) {
      
      /* Transform the element by passing it into the 
       * user-provided function
       */
      const newElement = userProvidedFunction(this[i]); 
      
      newArr.push(newElement); 
   }
   return newArr;
})();
```

Finally, we can attach our new function to`Array.prototype`.

`Array.prototype.myMap = myMap;`

A final sanity check:

```js
const myArray = [1, 2, 3];
// Multiply each element x 2
const myMappedArray = myArray.myMap(e => e * 2)
console.log(myMappedArray) // [2, 4, 6];
```

#### Summary

`Map` is a prototype method offered by arrays. Behind the scenes, it iterates through the array, applying a user-provided function to each element. Ultimately, it returns a new array with the transformed values. It does this without mutating the original array. Because the parameter it takes is a function, it is considered a higher-order function. In addition, its use falls into the functional programming paradigm.

Thanks for reading!

woz
