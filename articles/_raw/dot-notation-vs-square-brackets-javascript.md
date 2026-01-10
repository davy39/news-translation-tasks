---
title: Dot Notation vs Bracket Notation for Object Properties – What's the Difference?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-17T16:55:10.000Z'
originalURL: https://freecodecamp.org/news/dot-notation-vs-square-brackets-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/19.-dot-vs-bracket-notation.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nThere are multiple ways to access object properties\
  \ in JavaScript. But two common ones are dot notation and bracket notation. \nI'll\
  \ explain the difference between these two approaches in this article.\nWith dot\
  \ and bracket notation, ..."
---

By Dillion Megida

There are multiple ways to access object properties in JavaScript. But two common ones are dot notation and bracket notation. 

I'll explain the difference between these two approaches in this article.

With dot and bracket notation, you can:

* access the value of a property by its key
* modify the value of an existing property by its key and
* add a new property to an object

But these two ways access properties differently, and there are different scenarios when one is better than the other.

## Dot Notation Property Accessor

The Dot Notation approach involves using a dot or period (`.`) and a key to access a property. Here's the syntax:

```js
object.key
```

You have the dot then the key of the property you want to access. This expression will return the value of the property. Let's see an example:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const target = obj.name
// deeecode
```

By using dot and the **name** key, `.name`, we get "deeecode" which is the value of the name property.

You can also use this notation to modify an existing property:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj.age = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript"
// }
```

Here, we modify the `age` property.

Also, you can add a new property using this approach:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj.location = "Mercury"

console.log(obj)
// {
//   name: "deeecode",
//   age: 80,
//   language: "javascript",
//   location: "Mercury"
// }
```

Here, we add the `location` property.

But this approach has limitations which we'll look at soon. Next, let's understand how the bracket notation approach works.

Here's a [video version](https://youtu.be/AzVvBO65SMc) for this topic if you're interested.

## Bracket Notation Property Accessor

The Bracket Notation approach involves using square brackets, in which you have an expression that evaluates to a value. That value serves as a key for accessing the property. Here's the syntax:

```js
object[expression]
```

The expression within the brackets evaluates to a key for the property you want to access, and this expression will return the value of the property. Let's see an example:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const target = obj["name"]
// deeecode
```

By using square brackets and a **"name"** string expression, `["name"]`, we get "deeecode" which is the value of the name property.

You can also use this approach to modify an existing property:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj["age"] = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript"
// }
```

Here, we modify the `age` property using an `"age"` string expression.

And, you can add a new property using square brackets:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj["location"] = "Mercury"

console.log(obj)
// {
//   name: "deeecode",
//   age: 80,
//   language: "javascript",
//   location: "Mercury"
// }
```

Here, we add a new `location` property using a `"location"` string expression.

The bracket notation has more capabilities than the dot notation. I'll explain.

## Differences between Dot Notation and Bracket Notation Property Accessor

Dot Notation only allows static keys while Bracket Notation accepts dynamic keys. Static key here means that the key is typed directly, while Dynamic key here means that the key is evaluated from an expression.

 Let's look at some examples.

### Using both approaches for accessing properties

Starting with dot notation:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "language"

const target = obj.myKey
// undefined
```

Here, I assigned the value "language" to a `myKey` variable. What I would expect here is that when I use the dot notation, like `obj.myKey`, "myKey", should be replaced with "language". So it would read as `obj.language` and that would return "javascript". 

But that's not what happens. Instead, the result is `undefined`.

The reason for this is that Dot Notation only accepts static keys. So when you do `obj.myKey`, JavaScript looks for the property with the key `myKey` in `obj`. But that property does not exist, so we get `undefined`.

The Bracket Notation, on the other hand, allows dynamic keys. Because this notation accepts expressions, you can use any expression that evaluates to a value. It could be:

* `hello + Hi` which evaluates to `helloHi` as a key
* `returnKey()` which evaluates to value as a key
* `isTrue ? "trueKey" : "falseKey"` which evaluates to "trueKey" or "falseKey" as a key
* `variable` which evaluates to the value of the variable as a key

Therefore, using the previous example, we can have this:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "language"

const target = obj[myKey]
// javascript
```

The expression we passed to the square brackets is `myKey` which is a variable. This expression evaluates to "language" which is the value of the variable. Using this value, the square brackets can get the value of the property, which is "javascript".

But if you pass a string expression like `"myKey"`, you get `undefined`:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "language"

const target = obj["myKey"]
// undefined
```

This is because the string expression `"myKey"` evaluates to the value `"myKey"` which serves as the key for accessing the property. Since there's no `myKey` key on `obj`, the returned value is `undefined`.

### Using both approaches for modifying properties

Starting with dot notation:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "age"

obj.myKey = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 80,
//   language: "javascript",
//   myKey: 100
// }
```

Here, we have `myKey` with the "age" value. By attempting to do `obj.myKey = 100` to modify the `age` property, it will not work. This is because the dot notation accepts a static key. So `obj.myKey` takes `myKey` as a key. Since `mykey` does not exist in `obj`, this statement adds the key. Then, `obj` has a new key, `myKey` with the value `100`.

The behavior is different with the bracket notation:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "age"

obj[myKey] = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript"
// }
```

Instead of adding a new `myKey` property to `obj`, the brackets approach modifies the `age` property. The reason is, we pass `myKey` as an expression to the square brackets. This expression, as a variable, evaluates to `"age"` which is the value of the variable. Using "age" as a key, this approach modifies the value of the `age` property to `100`.

And if we wanted to add a new property using square brackets, then we can pass an expression that returns a new key that does not exist. For example:

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "location"

obj[myKey] = "Mercury"

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript",
//   location: "Mercury"
// }
```

Here, the `myKey` variable holds a new value: `"location"`. By passing this to square brackets, and assigning a value of "Mercury", we now have a new property with key-value pair of `location` and "Mercury".

## Should You Use Dot or Bracket Notation?

So far, we've looked at how each notation works, using different examples for accessing/modifying existing properties and for adding new properties. So which should you use when writing JavaScript code?

The main factor that will help you make your decision is the key of the property you want to access. If it is a static key, use Dot Notation. But if it is a dynamic key (evaluated from an expression during runtime), use Bracket Notation.

Dot Notation is useful when you know the property ahead of time. You simply do `object.key` to read/modify an existing property or to add a new property.

Bracket Notation is useful when you want to [dynamically access a property](https://freecodecamp.org/news/how-to-set-dynamic-object-properties-using-computed-property-names/). The key of this property could come from expressions like `getKey()`, `"my" + "key"`, or `keyVariable`.

I hope you learnt something from the piece. Please share if you found it helpful :)


