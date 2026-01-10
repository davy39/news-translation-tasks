---
title: How to Use Currying and Composition in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-18T22:06:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-currying-and-composition-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/lydia-tallent-SkY-jiMGYfA-unsplash.jpg
tags:
- name: composition
  slug: composition
- name: currying
  slug: currying
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Tobias Parent

  A great conversation I had this evening got me thinking about and revisiting a concept
  I''ve toyed with before – currying. But this time, I''d like to explore it with
  you all!

  The concept of currying is not a new one, but it is very us...'
---

By Tobias Parent

A great conversation I had this evening got me thinking about and revisiting a concept I've toyed with before – currying. But this time, I'd like to explore it with you all!

The concept of currying is not a new one, but it is very useful. It is also foundational for functional programming, and is sort of a gateway to thinking about functions in a more modular way. 

And the idea of composition, of combining functions to create larger, more complex, more useful ones may seem pretty intuitive, but is also a key component in functional programming. 

When we start combining them, then some fun things can happen. Let's see how this might work.

## Curry, anyone?

Curried functions are doing much the same as any other function, but the way you approach them is a bit different. 

Suppose we wanted a function that could check the distance between two points: `{x1, y1}` and `{x2, y2}`, for example. The formula for that is a little mathy, but nothing we can't handle:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/distance-formula.svg)
_The formula for distance between two points, which is an application of the Pythagorean theorem._

Ordinarily, calling our function might look something like:

```js
const distance = (start, end) => Math.sqrt( Math.pow(end.x-start.x, 2) + Math.pow(end.y-start.y, 2) );

console.log( distance( {x:2, y:2}, {x:11, y:8} );
// logs 10.816653826391969
```

Now, currying a function is forcing it to take a single parameter at a time. So rather than calling it like `distance( start, end )`, we would call it like this: `distance(start)(end)`. Each parameter is passed in individually, and each function call returns another function, until all parameters have been provided.

It might be easier to show than to explain, so let's look at the above distance function as a curried one:

```js
const distance = function(start){
  // we have a closed scope here, but we'll return a function that
  //  can access it - effectively creating a "closure".
  return function(end){
    // now, in this function, we have everything we need. we can do
    //  the calculation and return the result.
    return Math.sqrt( Math.pow(end.x-start.x, 2) + Math.pow(end.y-start.y, 2) );
  }
}

console.log( distance({x:2, y:2})({x:11, y:8});
// logs 10.816653826391969 again
```

That seems like an awful lot of work to get the same result! We _can_ shorten it some, by using ES6 arrow functions:

```js
const distancewithCurrying = 
        (start) => 
          (end) => Math.sqrt( Math.pow(end.x-start.x, 2) +
                              Math.pow(end.y-start.y, 2) );
```

But again, it seems a lot of hoopla for no real gain, unless we start thinking about our functions in a more abstract way. 

Remember, functions can only return one thing. While we might provide any number of parameters, we will only get back a single value, whether it's a number, array, object, or function. We only get one thing back. And now, with a curried function, we have a function that can receive only one thing. There may be a connection there.

As it happens, the power of curried functions comes in being able to combine and _compose_ them. 

Consider our distance formula – what if we were writing a "capture the flag" game, and it might be useful to quickly and easily calculate each player's distance from the flag. We might have an array of players, each of which contains an `{x, y}` location. With an array of `{x,y}` values, a re-usable function could come in pretty handy. Let's play with that idea for a minute:

```js
const players = [
  {
    name: 'Alice',
    color: 'aliceblue',
    position: { x: 3, y: 5}
  },{
    name: 'Benji',
    color: 'goldenrod',
    position: { x: -4, y: -4}
  },{
    name: 'Clarissa',
    color: 'firebrick',
    position: { x: -2, y: 8}
  }
];
const flag = { x:0, y:0};

```

There's our setup: we have a starting location, `flag`, and we have an array of players. We have two different functions defined to calculate the difference, let's see the difference:

```js
// Given those, let's see if we can find a way to map 
//  out those distances! Let's do it first with the first
//  distance formula.
const distances = players.map( player => distance(flag, player.position) );
/***
 * distances == [
 *   5.830951894845301, 
 *   5.656854249492381, 
 *   8.246211251235321
 * ]
 ***/

// using a curried function, we can create a function that already
//  contains our starting point.
const distanceFromFlag = distanceWithCurrying(flag);
// Now, we can map over our players to extract their position, and
//  map again with that distance formula:
const curriedDistances = players.map(player=>player.position)
                                .map(distanceFromFlag)
/***
 * curriedDistances == [
 *   5.830951894845301, 
 *   5.656854249492381, 
 *   8.246211251235321
 * ]
 ***/
```

So here, we have used our `distanceCurried` function to apply one parameter, the starting point. That returned a function which takes another parameter, the ending point. By mapping over the players, we can create a new array with _just_ the data we need, and then pass that data into our curried function!

It's a powerful tool, and one that might take some getting used to. But by creating curried functions and composing them with other functions, we can create some very complex functions from smaller, simpler parts.

## How to Compose Curried Functions

Being able to map curried functions is very useful, but you'll also find other great uses for them. This is the beginning of "Functional Programming": writing small, pure functions that perform properly as these atomic bits and then combining them like building blocks.

Let's look at how we might take curried functions, and compose them into larger ones. This next exploration will get into filter functions.

First, a little groundwork. `Array.prototype.filter()`, the ES6 filtering function, allows us to define a callback function, one that takes an input value or values and return a true or false based on that. Here's an example:

```js
// a source array,
const ages = [11, 14, 26, 9, 41, 24, 108];
// a filter function. Takes an input, and returns true/false from it.
function isEven(num){
  if(num%2===0){
    return true;
  } else {
    return false;
  }
}
// or, in ES6-style:
const isEven = (num) => num%2===0 ? true : false;
// and applied:
console.log( ages.filter(isEven) );
// [14, 26, 24, 108]
```

Now that filter function, `isEven`, is written in a very specific way: it takes a value (or values, if we want to include the array's index for example), performs some sort of internal hoojinkery, and returns a true or false. Every time. 

This is the essence of a "filter callback function," though it isn't exclusive to filters – the `Array.prototype.every` and `Array.prototype.some` use the same style. A callback is tested against each member of an array, and the callback takes in some value and returns true or false.

Let's create a few more useful filter functions, but this time a little more advanced. In this case, we might want to "abstract" our functions a bit, letting us make them more re-usable. 

For example, some useful functions might be `isEqualTo` or `isGreaterThan`. These are more advanced in that they require _two_ values: one to define as one term of a comparison (call it a `comparator`), and one coming in from the array _being_ compared (we'll call it the `value`). Here's a bit more code:

```js
// we write a function that takes in a value...
function isEqualTo(comparator){
  // and that function *returns* a function that takes a second value
  return function(value){
    // and we simply compare those two values.
    return value === comparator;
  }
}
// again, in ES6:
const isEqualTo = (comparator) => (value) => value === comparator;
```

From this point, I'm going to stick with the ES6 version, unless there is a particularly challenging reason to expand the code out to the classic version. Moving on:

```js
const isEqualTo = (comparator) => (value) => value === comparator;
const isGreaterThan = (comparator) => (value) => value > comparator;

// and in application:
const isSeven = isEqualTo(7);
const isOfLegalMajority = isGreaterThan(18);

```

So there, the first two functions are our curried functions. They expect a single parameter, and return a function that in turn also expects a single parameter.

Based on those two single parameter functions, we do a simple comparison. The second two, `isSeven` and `isOfLegalMajority`, are simply implementations of those two functions.

Thus far, we haven't gotten to complex or involved, and we can stay small for a few more:

```
// function to simply invert a value: true <=> false
const isNot = (value) => !value;

const isNotEqual = (comparator) => (value) => isNot( isEqual(comparator)(value) );
const isLessThanOrEqualTo = (comparator) => (value) => isNot( isGreaterThan(comparator)(value) );
```

Here, we have a utility function that simply inverts the _truthiness_ of a value, `isNot`. Using that, we can begin composing larger pieces: we take our comparator and value, run them through the `isEqual` function, and then we `isNot` that value to say `isNotEqual`.

This is the beginning of composition, and let's be fair – it looks absolutely silly. What possible use would there be to write all that to get this:

```js
// all of the building blocks...
const isGreaterThan = (comparator) => (value) => value > comparator;
const isNot = (value) => !value;
const isLessThanOrEqualTo = (comparator) => (value) => isNot( isGreaterThan(comparator)(value) );

// simply to get this?
const isTooYoungToRetire = isLessThanOrEqualTo(65)

// and in implementation:
const ages = [31, 24, 86, 57, 67, 19, 93, 75, 63];
console.log(ages.filter(isTooYoungToRetire)

// is that any cleaner than:
console.log(ages.filter( num => num <= 65 ) )
```

"The final result is pretty similar in this case, so it doesn't really save us anything. In fact, given the setup in those first three functions, it took a **lot** more to build than simply doing a comparison!"

And that is true. I won't argue that. But it is only seeing a small piece of a much larger puzzle. 

* First, we are writing code that is much more _self-documenting_. By using expressive function names, we are able to see at a glance that we are filtering `ages` for values `isTooYoungToRetire`. We aren't seeing the math, we are seeing the description.
* Second, by using very small atomic functions, we are able to test each piece in isolation, making sure that it performs exactly the same every time. Later on, when we reuse those small functions, we can be confident that they will work –freeing us up from testing each little piece as our function's complexity grows.
* Third, by creating abstract functions, we might find applications for them in other projects later. Building a library of functional components is a very powerful asset, and one I strongly recommend cultivating.  

With all that said, we can also take those smaller functions and begin combining them into larger and larger pieces. Let's try that now: having both an `isGreaterThan` and `isLessThan`, we can write a nice `isInRange` function!

```js
const isInRange = (minComparator) 
                 => (maxComparator)
                   => (value) => isGreaterThan(minComparator)(value)
                              && isLessThan(maxComparator)(value)

const isTwentySomething = isInRange(19)(30);
```

That is great – we now have a means to test for multiple conditions at a single go. But looking at that, it doesn't seem very self-documenting. The `&&` in the middle there isn't terrible, but we can do better. 

Perhaps if we were to write _another_ function, one we can call `and()`. The `and` function can take any number of conditions, and test them against a given value. That would be useful, and extensible.

```js
const and = (conditions) = 
             (value) => conditions.every(condition => condition(value) )

const isInRange = (min)
                 =>(max) 
                  => and([isGreaterThan(min), isLessThan(max) ])
```

So the `and` function takes any number of filter functions, and only returns true if they are all true against a given value. That `isInRange` function in the last does the exact same thing as the prior one, but it seems much more readable, and self-documenting. 

Further, it will allow us to combine any number of functions: suppose we wanted to get even numbers between 20 and 40, we would simply combine our `isEven` function from WAY up top with our `isInRange` one using an `and`, and it simply works.

## Recap

By using curried functions, we are able to compose functions together cleanly. We can wire the output of one function directly into the input of the next, as both now take a single parameter. 

By using composition, we can combine smaller functions or curried functions into much larger and more complicated structures, with the confidence that the smallest parts are working as expected.

This is a lot to digest, and it's a deep concept. But if you take the time and explore this more, I think you'll start seeing applications we haven't even touched on, and you might write the next article like this instead of me!

