---
title: The Differences Between forEach() and map() that Every Developer Should Know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-21T17:50:37.000Z'
originalURL: https://freecodecamp.org/news/4-main-differences-between-foreach-and-map
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/cover4.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Ibrahima Ndaw\nJavaScript has some handy methods which help us iterate\
  \ through our arrays. The two most commonly used for iteration are Array.prototype.map()\
  \ and Array.prototype.forEach(). \nBut I think that they remain a little bit unclear,\
  \ especia..."
---

By Ibrahima Ndaw

JavaScript has some handy methods which help us iterate through our arrays. The two most commonly used for iteration are `Array.prototype.map()` and `Array.prototype.forEach()`. 

But I think that they remain a little bit unclear, especially for a beginner. Because they both do an iteration and output something. So, what is the difference?

In this article, we'll look at the following:

* Definitions
* The returning value
* Ability to chain other methods
* Mutability
* Performance Speed
* Final Thoughts

## Definitions

The `map` method receives a function as a parameter. Then it applies it on each element and returns an entirely new array populated with the results of calling the provided function. 

This means that it returns a new array that contains an image of each element of the array. It will always return the same number of items.

```javascript

const myAwesomeArray = [5, 4, 3, 2, 1]

myAwesomeArray.map(x => x * x)

// >>>>>>>>>>>>>>>>> Output: [25, 16, 9, 4, 1]
```

Like `map` , the `forEach()` method receives a function as an argument and executes it once for each array element. However, instead of returning a new array like `map`, it returns `undefined`.

```javascript
const myAwesomeArray = [
  { id: 1, name: "john" },
  { id: 2, name: "Ali" },
  { id: 3, name: "Mass" },
]

myAwesomeArray.forEach(element => console.log(element.name))
// >>>>>>>>> Output : john
//                    Ali
//                    Mass
```

## 1. The returning value

The first difference between `map()` and `forEach()` is the returning value. The `forEach()` method returns `undefined` and `map()` returns a new array with the transformed elements. Even if they do the same job, the returning value remains different.

```javascript
const myAwesomeArray = [1, 2, 3, 4, 5]
myAwesomeArray.forEach(x => x * x)
//>>>>>>>>>>>>>return value: undefined

myAwesomeArray.map(x => x * x)
//>>>>>>>>>>>>>return value: [1, 4, 9, 16, 25]

```

## 2. Ability to chain other methods

The second difference between these array methods is the fact that `map()` is chainable. This means that you can attach `reduce()`, `sort()`, `filter()` and so on after performing a `map()` method on an array. 

That's something you can't do with `forEach()` because, as you might guess, it returns `undefined`.

```javascript
const myAwesomeArray = [1, 2, 3, 4, 5]
myAwesomeArray.forEach(x => x * x).reduce((total, value) => total + value)
//>>>>>>>>>>>>> Uncaught TypeError: Cannot read property 'reduce' of undefined
myAwesomeArray.map(x => x * x).reduce((total, value) => total + value)
//>>>>>>>>>>>>>return value: 55

```

## 3. Mutability

In general, the word "mutate" means change, alternate, modify or transform. And in the JavaScript world it has the same meaning. 

A mutable object is an object whose state can be modified after it is created. So, what about `forEach` and `map` regarding mutability?

Well, according to the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript):

`forEach()` does not mutate the array on which it is called. (However, `callback` may do so).

`map()` does not mutate the array on which it is called (although `callback`, if invoked, may do so).

_JavaScript is weird_.

![Gif](https://media.giphy.com/media/KWn5YHuCzP3FK/giphy.gif)

Here, we see a very similar definition, and we all know that they both receive a `callback` as an argument. So, which one relies on immutability?

Well, in my opinion, this definition is not clear though. And to know which does not mutate the original array, we first have to check how these two methods work.

The `map()` method returns an entirely new array with transformed elements and the same amount of data. In the case of `forEach()`, even if it returns `undefined`, it will mutate the original array with the `callback`.

Therefore, we see clearly that `map()` relies on immutability and `forEach()` is a mutator method.

## 4. Performance Speed

Regarding performance speed, they are a little bit different. But, does it matter? Well, it depends on various things like your computer, the amount of data you're dealing with, and so on. 

You can check it out on your own with this example below or with [jsPerf](https://jsperf.com/) to see which is faster.

```javascript
const myAwesomeArray = [1, 2, 3, 4, 5]

const startForEach = performance.now()
myAwesomeArray.forEach(x => (x + x) * 10000000000)
const endForEach = performance.now()
console.log(`Speed [forEach]: ${endForEach - startForEach} miliseconds`)

const startMap = performance.now()
myAwesomeArray.map(x => (x + x) * 10000000000)
const endMap = performance.now()
console.log(`Speed [map]: ${endMap - startMap} miliseconds`)

```

# Final Thoughts

As always, the choice between `map()` and `forEach()` will depend on your use case. If you plan to change, alternate, or use the data, you should pick `map()`, because it returns a new array with the transformed data. 

But, if you won't need the returned array, don't use `map()` - instead use `forEach()` or even a `for` loop.

Hopefully, this post clears up the differences between these two methods. If there are more differences, please share them in the comment section, otherwise thanks for reading it.

Read more of my articles on [my blog](https://www.ibrahima-ndaw.com)

Photo by [Franck V.](https://unsplash.com/@franckinjapan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/different?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

