---
title: How to Use Supercharged Sorts in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-23T16:14:34.000Z'
originalURL: https://freecodecamp.org/news/supercharged-sorts-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6054e9bf687d62084bf682b9.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Tobias Parent

  I was asked a great question recently about filtering and sorting arrays. At first,
  it seemed trivial:


  If I have an array of objects, and I want to be able to filter() by multiple properties,
  can I do that?


  And the answer is, of co...'
---

By Tobias Parent

I was asked a great question recently about filtering and sorting arrays. At first, it seemed trivial:

> If I have an array of objects, and I want to be able to `filter()` by multiple properties, can I do that?

And the answer is, of course, sure. Absolutely. The way `Array.filter()` works in JavaScript, it's chainable. That means, when the first `.filter()` function returns, it can be fed straight into a second `.filter()`, and to as many filters as you like.

But if we want to _sort_ by more than one property, that seems a little trickier. After all, if we sort by one property, then sort by a second, we've lost the first.

How about if we use something like `.reduce()` instead? We could use that to reduce the array to an object whose properties are the first sort values, then set each of those properties to an array of items _containing_ those values, and sort them!

And just like that, we're down the rabbit hole. There has to be an easier way.

As it happens, there is. It's good old `Array.sort()` all over again.

## Second verse, same as the first

Here's where we need to start: Think about the values that `Array.sort()` expects its callback function to return, given a callback with `(a, b)` as its parameters:

* If the returned value is less than zero, `a` will remain before `b` in the sort order.
* If the returned value is greater than zero, `b` will swap places with `a` in the sort order.
* _If the returned value is equal to zero, `a` and `b` have the same weight, and thus will remain unchanged._

Now, something else to note: in those three cases, we have three values: 0, -1, and 1. Here's how JavaScript will coerce them, as Boolean (true/false) values:

```js
Boolean(-1) === true; 
Boolean(1) === true; 
// But:
Boolean(0) === false;
```

Now, how does that help us? We have some great information here: first, if a sort is performed between two properties, and the properties are the same, the comparison should return 0 or a Boolean `false`. As zero is the only number to coerce to a false value, any equal values will give a false comparison.

Second, we can use that `true` or `false` to determine if we need to drill deeper.

Here's the last page, for those who are already seeing where this is going:‌

```js
return <the value of the first comparator, if it coerces to a Boolean true> 
    || <the value of a second one>;
```

## Wait, What?

Lol Yup. What just happened? What exactly are we returning there?

Using the inline OR, `||`, tells the return statement to evaluate the value to be returned. Is the first comparator Boolean `true`? If not, then work through the `||` tree to the first comparison that does, or if none does, return the result of that last comparison.

Let's work it through with a practical example (run the code **[here](https://tech.io/snippet/oJ0Ueod)** on Tech.io). Consider an array of four members:

```js
const myArray = [
  {
    firstName: 'Bob',
    lastName: 'Francis', 
    age: 34,
    city: 'Holland', 
    state: 'Massachusetts', 
    country: 'USA', 
    online: true
  }, {
    firstName: 'Janet',
    lastName: 'Francis',
    age: 41,
    city: 'Holland',
    state: 'Massachusetts',
    country: 'USA',
    online: false 
  },{
    firstName: 'Alexia',
    lastName: 'Francis',
    age: 39,
    city: 'Paris',
    state: 'Ile de France',
    country: 'France',
    online: true,
  },{
    firstName: 'Lucille',
    lastName: 'Boure',
    age: 29,
    city: 'Paris',
    state: 'Ile de France',
    country: 'France',
    online: true,
  }
];
```

We have these four users, and we wish to sort them by their last name:

```js
const sortByLastName = function(a, b){
  return a.lastName.localeCompare(b.lastName)
};

console.log(myArray.sort(sortByLastName) );
```

That first line defines our sorting function, which we'll pass into `myArray.sort(...)`. The `localeCompare()` function is a handy JavaScript function for comparing one string to another, sidestepping differences of case, and so on. It is made to work with `sort()`, returning 1, 0, or -1, depending on how each pair of records match.

So, the result of this sort function (and this is a pretty trivial example) sorts the array by lastName:

```js
[
  {
    firstName: 'Lucille',
    lastName: 'Boure',
    // ... 
  },{
    firstName: 'Bob',
    lastName: 'Francis'
    //... 
  },{
    firstName: 'Janet',
    lastName: 'Francis',
    // ... 
  },{
    firstName: 'Alexia',
    lastName: 'Francis',
    // ... 
  }
]
```

Not all that impressive, really – we've sorted by last name, but what about last AND first? Can we do THAT?

## We have the power!

The answer is, of course, yes. If you've read this far, it would be silly of me to bait you along and not give you a good answer.

The trick to remember is, if the first comparison returns a falsy value (in this case, `0`), then we can fall into a second one. And, if we want, a third or fourth or...

Here's how the comparator function might look, to sort by `lastName`, then by `firstName`:

```js
const sortByLastAndFirst = function(a, b){
  return (a.lastName.localeCompare(b.lastName) ) 
      || (a.firstName.localeCompare(b.firstName) )
};
```

And here's a **[runnable](https://tech.io/snippet/udV2Qfx)** of that one. The parentheses in that return are simply to make things a little more readable, but here's the logic going on:

```
comparing a and b in a sort function, return:

* if a.lastName comes before or after b.lastName,
  : return the value of that comparison.
  
* if a.lastName and b.lastName are the same, we get a false value, so 
  : go on to the next comparison, a.firstName and b.firstName
```

## Recap before moving on

So, at this point, we know we can string sort `return` clauses together. And that's powerful. It gives us some depth, and makes our sorts a little more flexible. We can make it more readable, and more "plug-and-play", as well.

Now I'm going to change it up a little, I'll be using ES6 _fat-arrow functions_:

```js
// Let's put together some smaller building blocks...
const byLast = (a, b)=>a.last.localeCompare(b.last);
const byFirst = (a, b)=>a.first.localeCompare(b.first);

// And then we can combine (or compose) them! 
const byLastAndFirst = (a, b) => byLast(a, b) || byFirst(a, b);
```

That does the same thing as the one we just did, but it's a bit more understandable. Reading that `byLastAndFirst` function, we can see that it's sorting by last, then by first.

But that's a bit of a pain – we have to write the same code each time? Look at `byLast` and `byFirst` in that last example. They are the same, other than the property name. Can we fix it so we don't have to write the same functions over and over?

## Third verse, same as... never mind.

Of course! Let's start by trying to make a generic `sortByProp` function. That will take a property name, and two objects, and compare them.

```js
const sortByProp = function(prop, a, b){
  if (typeof a[prop] === 'number')
    return a[prop]-b[prop];
    
  // implied else - if we're here, then we didn't return above 
  // This is simplified, I'm only expecting a number or a string.
  return a[prop].localeCompare(b[prop]); };
```

So that we can use in our sort function as a comparator:

```js
myArray.sort((a, b)=> sortByProp('lastName', a,b) 
                   || sortByProp('firstName', a, b) );
```

And that looks pretty great, right? I mean, we now only have one function, and we can compare by any property. And hey, it includes a check for comparing numbers vs strings, for the win!

Yeah, but it bothers me. I like to be able to take those smaller functions (the `byLast` and `byFirst`), and know they will still work with `sort` – but with the parameter signature on our `byProp(prop, a, b)`, we can't use that! Sort doesn't know about our `prop` function.

## What's a dev to do?

Well, what we do here is, we write a function that returns a function. These are known as **higher-order functions**, and they're a powerful feature of JavaScript.

We want to create a function (we'll still call it `sortByProp()`) that we can pass in a property name. In return, we get back a function that remembers our property name in its internal scope, but that can accept the sort function's `(a, b)` parameter signature.

What this pattern is doing is creating a "closure". The property is passed into the outer function as a parameter, so it solely exists within the scope of that outer function.

But within that, we return a function that can reference values in there. A closure needs two parts: a private scope, and some access methods into that private scope. It's a powerful technique, and one I'll be exploring more in the future.

Here's where we'll start: First, we need to redefine our `sortByProp` function. We know it needs to take a property, and it needs to return a function. Further, that function being returned should take the two properties that `sort()` will be passing in:

```js
const sortByProp = function(prop){
  return function(a,b){
    /* here, we'll have something going on */ 
  } 
}
```

Now, when we call this one, we will get back a function. So we can assign it to a variable in order to be able to call it again later:

```js
const byLast = sortByProp('lastName');
```

In that line, we've caught the function that's been returned, and stored it into `byLast`. Further, we've just created a _closure_, a reference into a closed scope that stores our `prop` variable, and that we can use later, whenever we call our `byLast` function.

Now, we need to revisit that `sortByProp` function and fill in what happens inside. It's the same as what we did in the first `sortByProp` function, but now it's enclosed with a function signature we can use:

```js
const sortByProp = function(prop){
  return function(a,b){
    if(typeof a[prop] === 'number')
      return a[prop]-b[prop];

    return a[prop].localeCompare(b[prop]); 
  } 
}
```

And to use it, we can simply:

```js
const byLast = sortByProp('lastName'); 
const byFirst = sortByProp('firstName'); 
// we can now combine, or "compose" these two: 
const byLastAndFirst = function(a, b){
  return byLast(a, b) 
      || byFirst(a, b); 
} 

console.log( myArray.sort(byLastAndFirst) );
```

And note that we can extend that to whatever depth we want:

```js
const byLast = sortByProp('lastName'); 
const byFirst = sortByProp('firstName'); 
const byCountry = sortByProp('country'); 
const byState = sortByProp('state'); 
const byCity = sortByProp('city'); 
const byAll = (a, b)=> byCountry(a, b) || byState(a, b) || byCity(a, b) || byLast(a, b) || byFirst(a, b); 

console.log(myArray.sort(byAll) );
```

That last example was painfully deep. And it was done on purpose. My next post will be an alternative way to do that same thing, without having to hand-code all the comparisons like that.

For those who like to see the complete picture, I fully expect questions about an ES6 version of that same `sortByProp` function, just because they're pretty. And they are pretty, sure, between an implicit return and the lovely ternary. Here it is, and here's the **[Tech.io](https://tech.io/snippet/imU4elI)** for that one:

```js
const byProp = (prop) => (a, b) => typeof(a[prop])==='number'
             ? a[prop]-b[prop] 
             : a[prop].localeCompare(b[prop]);
```

Do note that this version is no better or worse than the other. It looks sleek, and it leverages some great ES6 functionality, but it sacrifices readability. A junior developer might look at that one and throw up their hands. Please, don't sacrifice maintainability for cleverness.

Thanks for reading, everyone!

