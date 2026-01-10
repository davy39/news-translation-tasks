---
title: JavaScript Key in Object – How to Check if an Object has a Key in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-25T14:24:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-an-object-has-a-key-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--3-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Objects in JavaScript are non-primitive data types that hold an unordered
  collection of key-value pairs.


  As you can see in the image above, the key is the property, and each object value
  must have a key.

  When interacting with objects, situations mig...'
---

Objects in JavaScript are non-primitive data types that hold an unordered collection of key-value pairs.

![](https://paper-attachments.dropbox.com/s_D8321C80F6574B261A5AA02D2476A50C8DDF61A6CC2583DCEE0E18EC365EF07B_1658417045591_Untitled+Diagram.jpg align="left")

As you can see in the image above, the key is the property, and each object value must have a key.

When interacting with objects, situations might arise that require you to check if a particular key exists. It is important to note that if you know a key exists that automatically means that a value exists. This value could be anything – even empty, null, or undefined.

In this article, we will learn the various methods to check if an object's key exists in JavaScript.

### Here's an Interactive Scrim about How to Check if an Object Has a Key in JavaScript

<iframe src="https://scrimba.com/scrim/cZ7y4nHv?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

In case you are in a rush, here are the two standard methods we can use to check:

```js
// Using in operator
'key' in object

// Using hasOwnProperty() method
object.hasOwnProperty('key')
```

## How to Check if an Object Has a `key` in JavaScript with the `in` Operator

You can use the JavaScript `in` operator to check if a specified property/key exists in an object. It has a straightforward syntax and returns `true` if the specified property/key exists in the specified object or its prototype chain.

The syntax when using the [`in`](https://www.freecodecamp.org/news/the-javascript-in-operator-explained-with-examples/) [operator](https://www.freecodecamp.org/news/the-javascript-in-operator-explained-with-examples/) is:

```js
'key' in object
```

Suppose we have an object which contains a user's details:

```js
let user = {
  name: "John Doe",
  age: 40
};
```

We can check if a key exists with the `in` operator as seen below:

```js
'name' in user; // Returns true
'hobby' in user; // Returns false
'age' in user; // Returns true
```

Note: The value before the `in` keyword should be of type `string` or `symbol`.

## How to Check if an Object Has a `key` in JavaScript with the `hasOwnProperty()` Method

You can use the JavaScript `hasOwnProperty()` method to check if a specified object has the given property as its property. T

his method is pretty similar to the `in` operator. It takes in a `string` and will return `true` if the `key` exists in the object and `false` otherwise.

The syntax when using the `hasOwnProperty()` method is:

```js
object.hasOwnProperty('key')
```

Suppose we have an object which contains a user's details:

```js
let user = {
  name: "John Doe",
  age: 40
};
```

We can check if a key exists with the `in` operator as seen below:

```js
user.hasOwnProperty('name'); // Returns true
user.hasOwnProperty('hobby'); // Returns false
user.hasOwnProperty('age'); // Returns true
```

Note: The value you pass into the `hasOwnProperty()` method should be of type `string` or `symbol`.

Since we now know that these methods exist, we can now use a condition to check and perform whatever operation we wish to perform:

```js
if ("name" in user) {
  console.log("the key exists on the object");
}

// Or

if (user.hasOwnProperty("name")) {
  console.log("the key exists on the object");
}
```

## Wrapping Up

In this article, we have learned how to check if an object has a key using the two standard methods. The difference between the two methods is that `Object.hasOwnProperty()` looks for a key in an object alone while the `in` operator looks for the key in the object and its prototype chain.

There are other methods you can use, but at some point they might get too elaborate and aren't that easy to understand. They also might fail when tested against certain conditions.

For example, we could use the optional chaining, so if a specified key does not exist, it will return `undefined`:

```js
let user = {
  name: "John Doe",
  age: 40
};

console.log(user?.name); // Returns John Doe
console.log(user?.hobby); // Returns undefined
console.log(user?.age); // Returns 40
```

So we could create a condition that, when it's not equal to `undefined`, it means the key exists:

```js
if (user?.hobby !== undefined) {
  console.log("The key exists on the object");
}
```

As we said earlier, these methods fail when tested against some uncommon conditions. For example, in a situation when a particular key is set to "undefined", as seen below, the condition fails:

```js
let user = {
  name: "John Doe",
  age: undefined
};

console.log(user?.age); // Returns undefined
```

Another example when it works but gets elaborate is when we use the `Object.keys()` method alongside the `some()` method. This works but isn't really easy to understand:

```js
let user = {
  name: "John Doe",
  age: undefined
};

const checkIfKeyExist = (objectName, keyName) => {
    let keyExist = Object.keys(objectName).some(key => key === keyName);
    return keyExist;
};
  
console.log(checkIfKeyExist(user, 'name')); // Returns true
```

In the code above, we retired all the keys as an array and then applied the `some()` method to test whether at least one element in the array passed the test. If it passes, it returns `true`, else `false`.

Happy coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
