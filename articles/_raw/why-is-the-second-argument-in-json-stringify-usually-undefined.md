---
title: Why is the Second Argument in JSON.stringify() usually null?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-29T17:43:00.000Z'
originalURL: https://freecodecamp.org/news/why-is-the-second-argument-in-json-stringify-usually-undefined
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/24.-json-stringify-null.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nUsually, when developers use the JSON.stringify() method,\
  \ the second argument is usually skipped, or with a value null. But this argument\
  \ has its relevance.\nHere's a common example usage of JSON.stringify():\nconst\
  \ obj = {\n  name: \"D..."
---

By Dillion Megida

Usually, when developers use the `JSON.stringify()` method, the second argument is usually skipped, or with a value `null`. But this argument has its relevance.

Here's a common example usage of `JSON.stringify()`:

```js
const obj = {
  name: "Dillion",
  language: "JavaScript",
  age: 100,
  isEngineer: true
}

const stringifiedObj = JSON.stringify(obj, null, 2)

console.log(stringifiedObj)
// {
//   "name": "Dillion",
//   "language": "JavaScript",
//   "age": 100,
//   "isEngineer": true
// }
```

As you see here, we passed three arguments to `stringify`: the object, `null`, and 2.

In cases like this, the second argument is not needed, that's why we have `null`. But, there are cases where the second argument can be useful. I'll show you the relevance of the second argument in this article.

I have a [1-minute video on this topic](https://youtu.be/y3P17LC8rJQ) which you can also check out.

## The JSON.stringify method

The `stringify` method of the `JSON` object is used to, as the name implies, stringify a value in JavaScript. Usually, this method is used to convert an object to a JSON string, which is a recommended format for things like API responses, configuration files, etc.

Here's the syntax of the method:

```js
stringify(value, replacer, space)
```

The `value` is the object you want to stringify. The replacer specifies values of properties to be replaced while stringifying. And the space specifies whitespaces for the final output (which helps in readability).

The `replacer` is usually `null` because there's nothing to be replaced, but in cases where you want to replace some properties while stringifying, this is a good place to do that.

## The replacer argument of JSON.stringify

The `replacer` argument can either be a function that is called on every property in the object, or an array that contains keys that should exist in the final output.

### Replacer Callback Function

Using a callback function as a replacer in `JSON.stringify`, you can loop through properties and modify them for the final output. Here is an example:

```js
function replacer(key, value) {
  if (key === "age") {
    return 500
  }

  if (key === "name") {
    return `Mr. ${value}`
  }

  if (key === "isEngineer") {
    return undefined
  }

  return value
}
```

Here, we have a `replacer` function which would take each property (the key and the value) as arguments. This function checks if the key is "age" for which it would return **500** as the value. It also checks if the key is "name" for which it would return "Mr." concatenated with the value of `name`. Lastly, it checks if the key is "isEngineer" and if so, it returns `undefined`.

If the previous conditions are not met, it returns the `value`

Let's apply this to the `stringify` method:

```js
const obj = {
  name: "Dillion",
  language: "JavaScript",
  age: 100,
  isEngineer: true,
}

const stringifiedObj = JSON.stringify(
  obj,
  replacer,
  2
)

console.log(stringifiedObj)

// {
//   "name": "Mr. Dillion",
//   "language": "JavaScript",
//   "age": 500
// }
```

By applying the `replacer` function as the second argument, what do you notice in the final result?

On every property, the `key` and the `value` is passed to the replacer function. The returned value of that function becomes the value of the property. But the key does not change.

For `name`, we return "Mr." concatenated with the existing value which was "Dillion" so we have "Mr. Dillion".

For `language`, we do not do anything. We simply return the `value`.

For `age`, we returned 500 from the replacer function, so 500 replaces the previous value which was 100.

For `isEngineer`, we returned `undefined` from the replacer function. `undefined` is not a valid value in JSON strings, so that property is excluded from the final output.

As you have seen here, we have used the replacer argument (in this case, a function) to "replace" (modify) the properties of the object, before stringifying it.

### Replacer Array

A replacer can either be a function or an array. Using an array as a replacer, you cannot modify properties, but you can specify the properties that should be in the final output. Here's an example:

```js
const replacer = ["name", "isEngineer"]
```

Here we have an array of two strings: "name" and "isEngineer". Now let's use it with `stringify`:

```js
const obj = {
  name: "Dillion",
  language: "JavaScript",
  age: 100,
  isEngineer: true,
}

const stringifiedObj = JSON.stringify(
  obj,
  replacer,
  2
)

console.log(stringifiedObj)

// {
//   "name": "Dillion",
//   "isEngineer": true
// }
```

As you can see here, the only properties in the final JSON string are `name` and `isEngineer` as those are the keys we specified in the replacer array.

## So why is the second argument of JSON.stringify() usually null?

You use `null` because you do not want to replace anything. When you pass `null` as the replacer argument, it means "no replacements", so every property in the object is stringified.

But not many developers know about this. As a developer myself, I learned to always use `null` when stringified objects to JSON. I never understood why.

So I hope this article teaches you something about `JSON.stringify()`.

As a next step, you can check out my article on [Circular reference](https://www.freecodecamp.org/news/circular-reference-in-javascript-explained/). In that article, I show how the `stringify` method can be used to resolve circular reference errors.



