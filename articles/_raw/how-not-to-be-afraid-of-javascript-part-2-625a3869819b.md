---
title: How not to be afraid of the fun parts of JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-javascript-part-2-625a3869819b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*q6gPdqvGh9U6wkAg.jpg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Neil Kakkar

  Part 2 of our series discusses iteration protocols, for loops, and generator functions

  This is Part 2 of Javascript mastery — and probably the most exciting parts of the
  language. ( Until Part 3 comes around, anyway ;) )

  Part 1 covered...'
---

By Neil Kakkar

#### Part 2 of our series discusses iteration protocols, for loops, and generator functions

This is Part 2 of Javascript mastery — and probably the most exciting parts of the language. ( Until Part 3 comes around, anyway ;) )

[Part 1 covered the language basics](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html), and here we’ll cover iteration protocol(s), their use in for loops, and generator functions.

Why generator functions in the mix? If you think that’s a random addition, read on! Generators are linked to iteration!

### For Loops

Well, you know the basic for loop, right?

`for (let i = 0; i < arr.length; i++)`

You’d use this to access elements in an array.

You’d use something similar to access the properties / values of an object:

`for ( let i = 0; i < Object.keys(obj).length; i++)`

And again, something similar for `map`, `set` and any other custom object you define. When you want just the values / properties, writing this loop can lead to mistakes. You might be using the length property wrong, you might be making off by one errors or you might think `Object.keys(obj).length` is just plain ugly (I do).

Since there ought to be one best way to do things, here we have the `for...of` and `for...in` loops! … One best thing, right?

Well, yes. They both are loops to iterate over something, but that’s where the similarity ends, as we’ll see below.

### For…of loop

Let’s start with trying to iterate over values in an object.

To access elements in an array: `for (let val of arr)`

To access values of an object: `for (let var of Object.values(obj))`

Beautiful, ain’t it? It begets the question though, why doesn’t `for (let var of obj)` simply work?

Let’s dive deeper into how this works and where all can you use the `for…of` loop. Most importantly, how can your classes / objects make use of this.

Welcome to the world of `iteration` protocols.

First, a short note about protocols.

If you’ve dealt with [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) before, then you probably know what an interface is: It’s a description of the actions that an object can do, like a contract. If you want to do `X`, you need to have a function defined in the contract which does X. For example, `doX(a,b,c)` which takes in parameters a,b,c . In the same way, protocols are interfaces in Javascript.

We have 2 iteration protocols in Javascript:

### Iterable Protocol

This protocol enables JS objects to determine their iteration behavior. It’s enabling an object to be iterated over. It also determines what exactly is iterated. The interface demands an [Symbol.iterator] method somewhere up the prototype chain.

![Image](https://cdn-media-1.freecodecamp.org/images/tzVvXusT0bOcZiXmqE6r32LjQLZ2LEjioZxh)
_MDN documentation_

### Iterator Protocol

This protocol determines the way our iterable protocol must return iterated values. Eh? An example would make this clearer.

The way I like to see it, the iterator protocol defines the class interface for an iterator. (If you look at the name again, this would seem pretty obvious, yeah? Iterator Protocol = Iterator Interface. Look ma, I can JS now.)

Going back to our dear documentation:

![Image](https://cdn-media-1.freecodecamp.org/images/Jx4mFiYHWkzInSy6Hw0ZRCFRpr6kkju6yeAJ)
_[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterator_protocol" rel="noopener" target="_blank" title=")_

So, our iterator interface is determined completely by the existence of the `next()` function on an object.

One key point to make here is, it’s considered best practice to implement both the iterator and iterable protocols, since some functions / syntax may expect the former, while some the latter. Doing so enables you to use both with your iterator. Here’s a wonderful example:

```js
const iteratorObject = {
 next() {
     const value = Math.random();
     if ( value < this.threshold ) {
         return { done: false, value}; 
     }
     return { done: true};
 },
 [Symbol.iterator]: function() {
     return this;
 },
 threshold: 0.7
}
```

The beauty lies in the `[Symbol.iterator]` part of the iterator. By defining this, we allow our iterator to be exposed to a variety of functions and syntaxes that need an iterable protocol, not just an iterator protocol. What can you do with this?

Remember the spread operator? — That accepts an iterable protocol as well!

```
>[...iteratorObject] 
[0.03085962239970308, 0.20649861146804716]
```

And of course, works with `for...of`, where this story began.

```
>for (let val of iteratorObject) {
    console.log(val);
}
0.6234680935767514
0.525812241023621
```

Under the hood, we can now understand what is happening: All these methods are using the `[Symbol.iterator]` to generate an iterator, and iterating over that using `next`!

```js
>const iter = iteratorObject[Symbol.iterator]()
undefined
>iter.next();
{done: false, value: 0.04474940944875905}
>iter.next();
{done: true}
```

Sure makes things easier when you don’t have to do that yourself. There’s one bit we haven’t touched on, that goes hand in hand with `for...of` loops, which is: `for...in`. What’s the difference? Let’s dive in, starting with our example!

### For…In Loops

```js
>for (const val in iteratorObject) {
    console.log(val);
}
next
threshold
```

On a simple glance, the difference seems obvious: `for...in` gets the properties, while `for...of` gets the values! Why is [Symbol.iterator] missing then? Well, there are 2 reasons.

There exists an enumerable property descriptor over properties. This determines whether the given property is enumerable, configurable or writable.

```js
> Object.getOwnPropertyDescriptors(iteratorObject)
{ next:
   { value: [Function: next],
     writable: true,
     enumerable: true,
     configurable: true },
  threshold:
   { value: 0.7,
     writable: true,
     enumerable: true,
     configurable: true },
  [Symbol(Symbol.iterator)]:
   { value: [Function: [Symbol.iterator]],
     writable: true,
     enumerable: true,
     configurable: true } }
```

The `for...in` loop loops over properties whose enumerable descriptor is set to true, as well as non-symbol properties. That explains it, right? Just to confirm, you could add a new property to the object, with enumerable set to false, and it wouldn’t show up in the `for...in` loop.

```js
Object.defineProperty(iteratorObject, "newHiddenProperty", {
    enumerable: false,
    value: "hidden",
})
```

Sure enough, it still isn’t there. `Object.keys()` uses the exact same methodology.

```js
>for(const val in iteratorObject) {
    console.log(val);
}
next
threshold
```

Coming back to the question that made us go down this rabbit hole — Why doesn’t `for(let val of obj)` simply work? Now you know, right? Because there doesn’t exist an iterable protocol on the Object prototype!

Why not? The simple answer is — language design choice. Why did they choose this? Because a lot of objects inherit from the base Object. Having an iterable protocol on the base Object would mean making all those objects iterable. For example: Your date objects become iterable, which doesn’t make any sense.

### ForEach Loop

This brings us to the last kind of for loops: the forEach loop. I’ve seen people get confused over why doesn’t `forEach` work everywhere ( like on Objects) and I’ll answer that question here.

Simple answer — `Array.prototype.forEach()`.

The `forEach` loop is defined only for arrays! So, you can use them only with arrays. Now, `forEach` doesn’t care where that array comes from. It could be a simple native array, or an array generated by Objects, like Object.keys().

To end the loops section, one common gotcha.

When using objects in JS as maps (or dictionaries, hashmap), you can run into issues when some key coincides with a property up the prototype chain.

Consider this example:

You have an object with certain keys you want to loop over.

```js
const baseObject = {
  a: 1,
  b: 2,
  someProperty: function() {
    return 4;
  }
}


const myObjectMap = Object.create(baseObject);

myObjectMap.c = 3; // key set in map for some reason.

for(let val in myObjectMap) { // this iterates up the chain!
  console.log(val);
}

> c
 a
 b
 someProperty
```

You probably just wanted to see `c`, the key you set. You can fix this via:

```js
for (let val in myObjectMap) {
  if (myObjectMap.hasOwnProperty(val)) {
    console.log(val);
  }
}

> c
```

Thus, two rules to avoid this problem:

1. Always use `hasOwnProperty()` to check if the key you’re looking for exists in the object ( and not up the proto chain)
2. Never use the `hasOwnProperty` as key in your dictionaries / maps.

If you have overridden `hasOwnProperty`, there is still a way to use it, since it’s a method of the Object prototype.

```
myObjectMap.hasOwnProperty = 4;

for(let val in myObjectMap) {
    if (myObjectMap.hasOwnProperty(val)) {
        console.log(val);
    }
}
> Uncaught TypeError: myObjectMap.hasOwnProperty is not a function
    at <anonymous>:4:21

// instead, we can do: 
for(let val in myObjectMap) {
    if (Object.prototype.hasOwnProperty.call(myObjectMap, val)) {
        console.log(val);
    }
}

> c
  hasOwnProperty
```

[Remember `call` and `apply` from the last part?](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html#the-new-keyword-and-apply) This is one awesome way to use them.

### Generator Functions

[Generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) allow on-demand entry and exit from a function. The entry and exit points are fixed. It’s like a multiple entry visa.

They are very powerful tools to get difficult things done.

The way I think of generator functions is this: They are useful to create a list of values on the fly, without the overhead of having an array.

Why not just iterate over an array of values? Well, generators save space. There is no array to begin with — just the computation (or I/O) necessary to get the next element from the “array”.

Let’s dive into the mechanics of it.

Calling a generator function doesn’t execute the body but returns an iterator object for the function. The body is executed when you call the iterator’s `next()` method. What about the fixed exit point? The entire body isn’t executed, but only until the next `yield` expression in the body.

This `yield` expression also specifies the value to be returned.

Let’s make this concept concrete with an example. Let’s do the tweet example from Part 1.

```js
function * generateTweets(userID, numberOfTweets) {
    for(let i=0; i< numberOfTweets; i++) {
        const tweet = randomTweetGenerator(); // assume this gives you a string of words < 280 characters.
        yield { tweet, userID, tweetID: i};
    }
}

const tweetList = generateTweets('neilkakkar', 3);
for( let tweet of tweetList) {
	  console.log(tweet);
}

> {tweet: "hi", userID: "neilkakkar", tweetID: 0}
  {tweet: "how's it going?", userID: "neilkakkar", tweetID: 1}
  {tweet: "I'm automagic", userID: "neilkakkar", tweetID: 2}


console.log(tweetList.next());
>    {value: undefined, done: true}
```

Okay, there’s a lot going on here. Let’s break it down.

First, we have the function generator, which generates tweets based on userID and number of tweets to generate. This function would return an iterator object. Thus, that’s what `tweetList` is.

```js
> tweetList
generateTweets {<suspended>}
    __proto__: Generator
    [[GeneratorLocation]]: VM2668:1
    [[GeneratorStatus]]: "suspended"
    [[GeneratorFunction]]: ƒ * generateTweets(userID, numberOfTweets)
    [[GeneratorReceiver]]: Window
    [[Scopes]]: Scopes[3]
```

Suspended means the generator isn’t closed/finished yet. So, there are values it can provide. We can access these via `tweetList.next()` - which would give us an object with two keys, `value` and `done`.

On the flip side, `for...of` loops understand the iteration protocol so they can iterate over the entire generator on their own!

That’s precisely why we can do the `for...of` on `tweetList` and get our tweets.

At this point, the generator is finished. The `for...of` loop consumes all values.

> Common gotcha: If there is a break statement inside the `for...of` loop, the generator closes too. So, you can’t reuse it again. See: [Don’t reuse generators in for..of loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#Iterating_over_generators).

We have here

```js
> tweetList
generateTweets {<closed>}
    __proto__: Generator
    [[GeneratorLocation]]: VM2668:1
    [[GeneratorStatus]]: "closed"
    [[GeneratorFunction]]: ƒ * generateTweets(userID, numberOfTweets)
    [[GeneratorReceiver]]: Window
```

Thus, when we log the next value in the next line, we get `done: true` as we’d expect - and no values.

That’s all for the example.

But, the story doesn’t end here. You can have generators yielding to generators as well! You do this via `yield *`.

```
function * generateTweetsForSomeUsers(users, numberOfTweets) {
    for(let user of users) {
        yield * generateTweets(user, numberOfTweets)
    }
}
```

Generators can also `return` instead of `yield`. This causes the generator to finish.

Well, this has gone on long enough, I think I’ll save the other cool bits for the next parts. Fun fact? We will get rid of for loops altogether. Welcome to the world of Map, Filter and Reduce.

Read more of my blog posts on [neilkakkar.com](https://neilkakkar.com/js-part-2.html).

