---
title: Circular Reference Error in JavaScript – Meaning and How to Fix It
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-07T21:52:14.000Z'
originalURL: https://freecodecamp.org/news/circular-reference-in-javascript-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/22.-circular-reference-error.png
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nHave you ever encountered a \"circular reference\" error\
  \ when working with JSON? \nIn this tutorial, I'll explain what this error means\
  \ as well as how to fix it.\nThis error, in my experience, occurs when you try to\
  \ convert an object wi..."
---

By Dillion Megida

Have you ever encountered a "circular reference" error when working with JSON? 

In this tutorial, I'll explain what this error means as well as how to fix it.

This error, in my experience, occurs when you try to convert an object with circular references to JSON. You may have experienced this error while doing this or something else.

First, let's understand what a circular reference is in JavaScript.

## What is a Circular Reference in JS?

An object in JavaScript can have different data types for properties. Here's an example of an object:

```js
const obj = {
  name: "Dillion",
  isDev: true,
  hobbies: ["singing", "writing"],
  age: 100,
}
```

This object has properties containing values of the string, boolean, array, and number data type.

In objects, you can also have a nested object. Here's what I mean:

```js
obj.languages = {
  first: "javascript",
  second: "java",
}

console.log(obj)
// {
//   name: "Dillion",
//   isDev: true,
//   hobbies: ["singing", "writing"],
//   age: 100,
//   languages: {
//     first: "javascript",
//     second: "java"
//   }
// }
```

Here, we add a `languages` property, which holds an object value containing the `first` and `second` properties.

To access the properties of the nested object, you can use the dot notation (or [bracket notation](https://www.freecodecamp.org/news/dot-notation-vs-square-brackets-javascript/)) like this:

```js
obj.languages.first
obj.languages.second
```

I have a [video version of this topic](https://youtu.be/EaHC3QfU1NY) you can also check out.

Now, what if we have a nested object that points to the original object? Take a look at this example:

```js
obj.itself = obj
```

Here, we add an `itself` property, and assign it an object reference, which is `obj`. This is a **circular reference**. I'll show you why it is called a circular reference.

Let's try to print `obj` to the console:

```js
// {
//   name: "Dillion",
//   isDev: true,
//   hobbies: ["singing", "writing"],
//   age: 100,
//   languages: {
//     first: "javascript",
//     second: "java"
//   },
//   itself: [Circular *1]
// }
```

In the console, the value of the `itself` property shows **[Circular \*1]**. This is a notation that the property points back to the object, and trying to log the value of that property will result in an endlessly nested object.

This means that the `itself` property will look like this:

```js
{
  name: "Dillion",
  isDev: true,
  hobbies: ["singing", "writing"],
  age: 100,
  languages: {
    first: "javascript",
    second: "java"
  },
  itself: {
    name: "Dillion",
    isDev: true,
    hobbies: ["singing", "writing"],
    age: 100,
    languages: {
      first: "javascript",
      second: "java"
    },
    itself: {
      name: "Dillion",
      // ...
    }
  }
}
```

Here's a graphical illustration of this:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-54.png)
_Graphical illustration of a cyclic reference_

As you can see in this object, the `itself` property has all the properties of the object, including `itself`, which again has all the properties of the object, including `itself` and it keeps going on and on without any end.

With this circular reference of the property to the object, we can access the `first` property like this:

```js
obj.itself.itself.itself.itself.itself.itself.first
```

This many `itself`s still work due to circular reference.

We can also access the `name` property in `obj` like this:

```js
obj.itself.itself.itself.itself.name
```

Since `itself` has a reference to `obj`, we can access the `name` property from any of the nested `itself`s.

Now let's see how this circular reference pattern applies to JSON.

## JSON's Issue with Circular References

Let's look at our initial object again:

```js
const obj = {
  name: "Dillion",
  isDev: true,
  hobbies: ["singing", "writing"],
  age: 100,
}
```

When you stringify this object to fit the JSON structure, here's the result:

```js
const stringified = JSON.stringify(obj)

console.log(stringified)
// {
//   "name":"Dillion",
//   "isDev":true,
//   "hobbies":["singing","writing"],"age":100
// }
```

JSON stringify goes through the properties from the first one being "name" to the last one being "hobbies".

What if we had our nested `languages` object stringified?

```js
obj.languages = {
  first: "javascript",
  second: "java",
}

const stringified = JSON.stringify(obj)

console.log(stringified)
// {
//   "name":"Dillion",
//   "isDev":true,
//   "hobbies":["singing","writing"],"age":100,
//   "languages":{
//     "first":"javascript",
//     "second":"java"
//   }
// }
```

As you see here, the stringify method goes through the properties from the first one being "name" to the last one being "languages". When it gets to languages, it goes through the properties of the object which are `first` and `second`.

Now let's introduce a circular reference and see what happens:

```js
obj.itself = obj

const stringified = JSON.stringify(obj)

console.log(stringified)
// TypeError: Converting circular structure to JSON
```

Now we get an error: **TypeError: Converting circular structure to JSON**.

What's the problem here?

By stringifying an object with a circular reference, that's an infinite stringification process.

Let's say JSON stringify tried to go through this object, here's what happens: the stringify method goes from the first property in `obj` which is `name` to the last property `itself`. When it gets to `itself`, it stringifies the properties of this object. The value of the `itself` object is the `obj` object, so stringify goes through from `name` to `itself` again. By coming across `itself`, it has to go through again.

Here's an illustration explaining what happens:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-55.png)

As you see here, this results in an infinite loop because `stringify` doesn't know when to stop. Everytime it comes across `itself`, it has to go through this object that has `itself`. It will keep stringifying forever.

This is basically impossible. So when the stringify method comes across a circular reference in an object, it just throws an error immediately. There's no need to waste its time 😅

So if you come across this error when building applications, how do you solve it?

## How to Solve the Circular Reference Error

There are a couple of ways you can solve this problem. You can use libraries or implement a solution yourself.

One major way to solve this is by using **serialization**. This process involves serializing the object to remove some properties from an object before converting it to JSON. 

In this process, you can remove properties you are not interested in, or in our case, properties that can cause errors.

Here's a simple solution:

```js
obj.itself = obj

function replacer(key, value) {
  if(key === 'itself') {
    return null
  }

  return value
}

const stringified = JSON.stringify(obj, replacer)

console.log(stringified)
// {
//   "name":"Dillion",
//   "isDev":true,
//   "hobbies":["singing","writing"],"age":100,
//   "languages":{
//     "first":"javascript",
//     "second":"java"
//   },
//   "itself":null
// }
```

What we've done here is use the [replacer argument of JSON.stringify](https://dillionmegida.com/p/second-argument-in-json-stringify/) to modify the `itself` property.

In the replacer function, we check for the key `itself`, and return the value `null` for that key. This way, `JSON.stringify` replaces the circular reference value with `null` during stringifying, thereby avoiding infinite stringification.

## Wrapping Up

If you build applications with JavaScript, you may have come across this cyclic reference error one way or the other.

In this article, I've explained what this error is, and why it exists when converting an object to JSON.

If you enjoyed this article, please share it with others 🙏🏾


