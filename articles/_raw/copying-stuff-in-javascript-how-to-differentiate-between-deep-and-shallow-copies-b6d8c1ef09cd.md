---
title: How to differentiate between deep and shallow copies in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-18T10:20:41.000Z'
originalURL: https://freecodecamp.org/news/copying-stuff-in-javascript-how-to-differentiate-between-deep-and-shallow-copies-b6d8c1ef09cd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CZaCLmeCWGIhvuhKnV7mVg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Lukas Gisder-Dubé

  New is always better!

  You have most certainly dealt with copies in JavaScript before, even if you didn’t
  know it. Maybe you have also heard of the paradigm in functional programming that
  you shouldn’t modify any existing data. In...'
---

By Lukas Gisder-Dubé

New is always better!

You have most certainly dealt with copies in JavaScript before, even if you didn’t know it. Maybe you have also heard of the paradigm in functional programming that you shouldn’t modify any existing data. In order to do that, you have to know how to safely copy values in JavaScript. Today, we’ll look at how to do this while avoiding the pitfalls!

First of all, what is a copy?

A copy just looks like the old thing, but isn’t. When you change the copy, you expect the original thing to stay the same, whereas the copy changes.

In programming, we store values in variables. Making a copy means that you initiate a new variable with the same value(s). However, there is a big potential pitfall to consider: **deep copying** vs. **shallow copying**. A deep copy means that all of the values of the new variable are copied and **disconnected from the original** variable. A shallow copy means that certain (sub-)values are **still connected** to the original variable.

> To really understand copying, you have to get into how JavaScript stores values.

#### Primitive data types

Primitive data types include the following:

* Number — e.g. `1`
    
* String — e.g. `'Hello'`
    
* Boolean — e.g. `true`
    
* `undefined`
    
* `null`
    

When you create these values, they are tightly coupled with the variable they are assigned to. They only exist once. That means you do not really have to worry about copying primitive data types in JavaScript. When you make a copy, it will be a real copy. Let’s see an example:

```javascript
const a = 5
let b = a // this is the copy
b = 6

console.log(b) // 6
console.log(a) // 5
```

By executing `b = a` , you make the copy. Now, when you reassign a new value to `b`, the value of `b` changes, but not of `a`.

#### Composite data types — Objects and Arrays

Technically, arrays are also objects, so they behave in the same way. I will go through both of them in detail later.

Here it gets more interesting. These values are actually stored just once when instantiated, and assigning a variable just creates **a pointer (reference) to that value**.

Now, if we make a copy `b = a` , and change some nested value in `b`, it actually changes `a`’s nested value as well, since `a` and `b` actually point to the same thing. Example:

```javascript
const a = {
  en: 'Hello',
  de: 'Hallo',
  es: 'Hola',
  pt: 'Olà'
}

let b = a
b.pt = 'Oi'

console.log(b.pt) // Oi
console.log(a.pt) // Oi
```

In the example above, we actually made a **shallow copy**. This is often times problematic, since we expect the old variable to have the original values, not the changed ones. When we access it, we sometimes get an error. It might happen that you try to debug it for a while before you find the error, since a lot of developers do not really grasp the concept and do not expect that to be the error.

![Image](https://cdn-media-1.freecodecamp.org/images/1*niSsr1dxva2RWXrvHT8hxg.jpeg align="left")

*Photo by* [*Thomas Millot*](https://unsplash.com/photos/7ocA9xwN3yQ) *on* [*Unsplash*](https://unsplash.com/s/photos/fungi)

Let’s have a look at how we can make copies of objects and arrays.

### Objects

There are multiple ways to make copies of objects, especially with the new expanding and improving JavaScript specification.

#### Spread operator

Introduced with ES2015, this operator is just great, because it is so short and simple. It ‘spreads’ out all of the values into a new object. You can use it as follows:

```javascript
const a = {
  en: 'Bye',
  de: 'Tschüss'
}

let b = {...a}
b.de = 'Ciao'

console.log(b.de) // Ciao
console.log(a.de) // Tschüss
```

You can also use it to merge two objects together, for example `const c = {...a, ...b}` .

#### Object.assign

This was mostly used before the spread operator was around, and it basically does the same thing. You have to be careful though, as the first argument in the `Object.assign()` method actually gets modified and returned. So make sure that you pass the object to copy at least as the second argument. Normally, you would just pass an empty object as the first argument to prevent modifying any existing data.

```javascript
const a = {
  en: 'Bye',
  de: 'Tschüss'
}

let b = Object.assign({}, a)
b.de = 'Ciao'

console.log(b.de) // Ciao
console.log(a.de) // Tschüss
```

#### Pitfall: Nested Objects

As mentioned before, there is one big caveat when dealing with copying objects, which applies to both methods listed above. When you have a nested object (or array) and you copy it, nested objects inside that object will not be copied, since they are only pointers / references. Therefore, if you change the nested object, you will change it for both instances, meaning you would end up doing a **shallow copy again**. Example:// BAD EXAMPLE

```javascript
const a = {
  foods: {
    dinner: 'Pasta'
  }
}

let b = {...a}
b.foods.dinner = 'Soup' // changes for both objects

console.log(b.foods.dinner) // Soup
console.log(a.foods.dinner) // Soup
```

To make a **deep copy of nested objects**, you would have to consider that. One way to prevent that is manually copying all nested objects:

```javascript
const a = {
  foods: {
    dinner: 'Pasta'
  }
}

let b = {foods: {...a.foods}}
b.foods.dinner = 'Soup'

console.log(b.foods.dinner) // Soup
console.log(a.foods.dinner) // Pasta
```

In case you were wondering what to do when the object has more keys than only `foods` , you can use the full potential of the spread operator. When passing more properties after the `...spread` , they overwrite the original values, for example `const b = {...a, foods: {...a.foods}}` .

#### Making deep copies without thinking

What if you don’t know how deep the nested structures are? It can be very tedious to manually go through big objects and copy every nested object by hand. There is a way to copy everything without thinking. You simply `stringify` your object and `parse` it right after:

```javascript
const a = {
  foods: {
    dinner: 'Pasta'
  }
}

let b = JSON.parse(JSON.stringify(a))
b.foods.dinner = 'Soup'

console.log(b.foods.dinner) // Soup
console.log(a.foods.dinner) // Pasta
```

Here, you have to consider that you will not be able to copy custom class instances, so you can only use it when you copy objects with **native JavaScript values** inside.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hepu5hNOaAqnhE60z-oicA.jpeg align="left")

*Photo by* [*Robert Zunikoff*](https://unsplash.com/photos/close-up-photo-of-goosebumps-slappy-the-dummy-ventriloquist-doll-j0vIeF69Jgc) *on* [*Unsplash*](https://unsplash.com/s/photos/dolls)

### Arrays

Copying arrays is just as common as copying objects. A lot of the logic behind it is similar, since arrays are also just objects under the hood.

#### Spread operator

As with objects, you can use the spread operator to copy an array:

```javascript
const a = [1,2,3]
let b = [...a]
b[1] = 4

console.log(b[1]) // 4
console.log(a[1]) // 2
```

#### Array functions — map, filter, reduce

These methods will return a new array with all (or some) values of the original one. While doing that, you can also modify the values, which comes in very handy:

```javascript
const a = [1,2,3]
let b = a.map(el => el)
b[1] = 4

console.log(b[1]) // 4
console.log(a[1]) // 2
```

Alternatively you can change the desired element while copying:

```javascript
const a = [1,2,3]
const b = a.map((el, index) => index === 1 ? 4 : el)

console.log(b[1]) // 4
console.log(a[1]) // 2
```

#### Array.slice

This method is normally used to return a subset of the elements, starting at a specific index and optionally ending at a specific index of the original array. When using `array.slice()` or `array.slice(0)` you will end up with a copy of the original array.

```javascript
const a = [1,2,3]
let b = a.slice(0)
b[1] = 4

console.log(b[1]) // 4
console.log(a[1]) // 2
```

#### Nested arrays

Similar to objects, using the methods above to copy an array with another array or object inside will generate a **shallow copy**. To prevent that, also use `JSON.parse(JSON.stringify(someArray))` .

#### BONUS: copying instance of custom classes

When you are already a pro in JavaScript and you deal with your custom constructor functions or classes, maybe you want to copy instances of those as well.

As mentioned before, you cannot just stringify + parse those, as you will lose your class methods. Instead, you would want to add a custom `copy` method to create a new instance with all of the old values. Let’s see how that works:

```javascript
class Counter {
  constructor() {
     this.count = 5
  }
  copy() {
    const copy = new Counter()
    copy.count = this.count
    return copy
  }
}

const originalCounter = new Counter()
const copiedCounter = originalCounter.copy()

console.log(originalCounter.count) // 5
console.log(copiedCounter.count) // 5

copiedCounter.count = 7

console.log(originalCounter.count) // 5
console.log(copiedCounter.count) // 7
```

To deal with objects and arrays that are referenced inside of your instance, you would have to apply your newly learned skills about **deep copying**! I will just add a final solution for the custom constructor `copy` method to make it more dynamic:

```javascript
class Counter {
  constructor() {
    this.count = 5

    this.add = function() {
      this.count++
    }
  }

  copy() {
    const copy = new Counter()

    Object.keys(this).forEach(key => {
      const value = this[key]

      switch(typeof value) {
        case 'function':
          break
        case 'object':
          copy[key] = JSON.stringify(JSON.parse(value))
          break
        default:
          copy[key] = value
          break
      }
    })
    
    return copy
  }
}
```

With that copy method, you can put as many values as you want in your constructor, without having to manually copy everything!

*About the Author: Lukas Gisder-Dubé co-founded and led a startup as CTO for 1 1/2 years, building the tech team and architecture. After leaving the startup, he taught coding as Lead Instructor at* [*Ironhack*](https://www.freecodecamp.org/news/copying-stuff-in-javascript-how-to-differentiate-between-deep-and-shallow-copies-b6d8c1ef09cd/undefined) *and is now building a Startup Agency & Consultancy in Berlin. Check out* [*dube.io*](https://dube.io) *to learn more.*

![Image](https://cdn-media-1.freecodecamp.org/images/1*p-l0Cee1IHvX0RQkVTOceQ.png align="left")
