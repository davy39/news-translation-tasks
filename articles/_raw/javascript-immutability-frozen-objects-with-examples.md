---
title: JavaScript Immutability – Frozen Objects in JS Explained with Examples
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-07-27T15:49:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-immutability-frozen-objects-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/freeCodeCamp-Cover-5.png
tags:
- name: immutability
  slug: immutability
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: null
seo_desc: "In JavaScript, we use an Object to store multiple values as a complex data\
  \ structure. You create an object with a pair of curly braces {}. \nAn object can\
  \ have one or more properties. Each of the properties is a key-value pair separated\
  \ by a colon(:)...."
---

In JavaScript, we use an `Object` to store multiple values as a complex data structure. You create an object with a pair of curly braces `{}`. 

An object can have one or more properties. Each of the properties is a key-value pair separated by a `colon(:)`. The key must be a string or JavaScript symbol type. The value can be of any type, including another object.

With that explanation of an object, let's create one to see how it works:

```js
const user = {
 'name': 'Bob',
 'age': 27   
}
```

Here we have created an object with two properties (name, age) and their respective values. We have created a variable called `user` with the `const` keyword and we've assigned the object to it as a value.

By default, objects are `mutable`. This means once they're created, you can add a new property to them, modify the value of an existing property, or delete a property.

In my early years of programming, I found the terms `mutable` and `immutable` very confusing. Let me try explaining it in simple English. 

Mutable is something you can change. Immutable is just the opposite of that. So, `mutability` is the ability to change over time. `Immutability` means something is unchanging over time.

There could be situations where you may not want an object to change programmatically. Therefore you'll want to make it immutable. 

When an object is immutable, you can't add a new property to it, modify it, or delete an existing property. There is no way even to extend it. 

This is what a `Frozen Object` is, which we'll learn about, practice with, and understand in this article.

I discussed frozen objects in a Twitter thread recently. Please feel free to have a look. This article will expand on the thread with more details and examples.

%[https://twitter.com/tapasadhikary/status/1416995389169971200]

# How to Create a Frozen Object in JavaScript

You can freeze (make immutable) an object using the function `Object.freeze(obj)`. The object passed to the `freeze` method will become immutable. The `freeze()` method also returns the same object.

Let's create an object of supported languages:

```js
const supportedLanguages = {
  'af': 'Afrikaans',
  'bn': 'Bengali',
  'de': 'German',
  'en': 'English',
  'fr': 'French'
}

```

If you don't want this object to change after it is created, just use the `freeze` method to make it immutable.

```js
const frozenSupportedLanguages = Object.freeze(supportedLanguages);

// The supportedLanguages and frozenSupportedLanguages are same

frozenSupportedLanguages === supportedLanguages; // returns true

```

Now let's try changing either of the objects and see what happens:

```js
// Add a new property
supportedLanguages['kn'] = 'Kannada';

// Modify an existing property
supportedLanguages["af"] = 'something else';

// Delete a property
delete supportedLanguages.bn; // returns false

// log the object to the console
console.log(supportedLanguages); // Unchanged => {af: "Afrikaans", bn: "Bengali", en: "English", fr: "French"}

```

You'll get errors when you try changing a frozen object (immutable object) in the JavaScript `strict` environment.

# Hold On – doesn't the `const` keyword do the same thing?

Ah, not quite. The `const` keyword and `Object.freeze()` are not the same things. When you assign an object to a variable created with the const keyword, you can not reassign another value. However, you can modify the assigned objects in whatever way you want.

Let's understand the difference with an example. This time, we will take the same `supportedLanguages` object but will not freeze it.

```js
const supportedLanguages = {
  'af': 'Afrikaans',
  'bn': 'Bengali',
  'de': 'German',
  'en': 'English',
  'fr': 'French'
}
```

Now you can modify it like this:

```js
// Add a new property
supportedLanguages['kn'] = 'Kannada';

// Modify an existing property
supportedLanguages["af"] = 'something else';

// Delete a property
delete supportedLanguages.bn; // returns true

// log the object to the console
console.log(supportedLanguages);
```

Now the `supportedLanguages` object is changed to the following:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-78.png)

So, this change is allowed. But if you try to assign a new object to the `supportedLanguages` variable:

```js
supportedLanguages = {'id': 'Indonesian'};
```

You will get this error:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-79.png)

I hope the difference is clear now – it's also a frequently asked interview question.

# Why Do We Need Frozen Objects in JavaScript?

Again, we need frozen objects when we need immutability. In object-oriented programming, it is common to have APIs that we can not extend or modify outside the current context. 

Do you remember the `final` keyword in Java? Or how in the Kotlin programming language, lists are immutable by default? Trying to mutate them at run time causes errors. Immutability is an essential concept to use in functional programming.

Immutability is often important in the JavaScript programming language as well. You may want a configuration object to be immutable, a fixed set of supported language for your applications, or anything else that you don't want to change at the run time.

# You Can Freeze an Array, Too

In JavaScript, `Arrays` are objects under the hood. So you can also apply `Object.freeze()`to arrays to make them immutable.

Let's take an array of human senses:

```js
const senses = ['touch', 'sight', 'hearing', 'smell', 'taste'];
```

We can now make it immutable like this:

```js
Object.freeze(senses);
```

Now, try to push an element to that array. It's not possible.

```js
senses.push('walking');
```

The output will be the following error:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-80.png)

Try to remove an element from the array:

```js
senses.pop();
```

You'll get this error:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-81.png)

Please notice the error in both the cases. It clearly says, the add and delete property is not allowed as the underlying object is not extensible.

# Object Freeze is Shallow

A JavaScript object property can have another object as its value. It can go to a deeper level down. 

When we freeze an object, it is a `shallow` freeze. This means that only the top-level properties are frozen. If any of the property's values are another object, that inner object is not frozen. You can still make changes to it.

Let's understand this with the example of a configuration object:

```js
const config = {
  'db': 'postgresql',
  'host': 'acme-ind.com',
  'password': 'fake-password',
  'port': 512,
  'admin': {
    'name': 'Tapas',
    'rights': ['create', 'update', 'delete']
  }
}
```

The config object has properties like db, host, password, and port with simple string types values. However, the admin property has an object as the value. Now, let's freeze the config object.

```js
Object.freeze(config);
```

Now, let's try to change the db name.

```js
config.db = 'redis';
```

It is not allowed as the object is frozen. However, you can do this:

```js
config.admin.name = 'atapas';
```

Here we have changed the property of the nested object. As the object freezing is shallow in nature, it is not going to stop us from changing the nested object. So, if you log the object in the console, this is what you'll get:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-82.png)

# How to Deep Freeze an Object in JavaScript

But how do you deep freeze an object if you need or want to? You may want to freeze all the properties of the object to the deepest level possible, right? We can do that using recursion.

In programming, recursion is a methodology that uses a procedure, function, or algorithm to call itself. [Check out this article](https://www.freecodecamp.org/news/understanding-recursion-in-programming/) for an in-depth understanding.

So, we can iterate through every property and recursively apply the freeze method to everything. It will make sure that the nested objects are also frozen. 

To do that, you can write a simple function like this:

```js
const deepFreeze = obj => {
  Object.keys(obj).forEach(prop => {
    if (typeof obj[prop] === 'object') deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};

deepFreeze(config);
```

# What's the Diffecrence Between freeze(), seal(), and preventExtentions()?

With Object.freeze we achieve full immutability. But there are two other methods that provide object immutability, only partially.

* `Object.seal` – We can not add a new property or delete existing properties of an object sealed with this method. But we can still update the value of existing properties.
* `Object.preventExtensions` – This method prevents new property creation. But you can update and delete existing properties.

Here is a table to compare them:

|                   | Create | Read | Update | Delete |
|-------------------|--------|------|--------|--------|
| freeze            |    ❌    |  ✔️   | ❌        | ❌       |
| seal              |    ❌   |  ✔️    |   ✔️     |  ❌      |
| preventExtensions |    ❌    |  ✔️   |    ✔️    |   ✔️     |



# How to UnFreeze a Frozen Object

There is no straightforward ways to unfreeze a frozen object in JavaScript. 

You can probably simulate an unfreeze by making a copy of the object maintaining the prototype. 

[Here is an NPM](https://www.npmjs.com/package/object-unfreeze) package that does the same with a shallow copy.

# In Summary

To Summarize,

* We can freeze an object to make it immutable.
* You use the method `Object.freeze` to freeze an object.
* You can not create a new property, modify or delete an existing property, or extend the object when a freeze is applied.
* Declaring a variable with the `const` keyword with an object value is not same as freezing the object.
* You can freeze an array using the same `freeze` method.
* The freeze method does a shallow freeze. Use recursion to do a deep freeze.
* The `seal()` and `preventExtentions()` methods provide partial immutability.
* Unfreezing is not supported in the language (yet).

# Before We End...

That's all for now. I hope you've found this article insightful, and that it helps you understand object immutability more clearly.

Let's connect. You will find me active on [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). Feel free to give a follow. I've also started sharing knowledge using my [YouTube channel](https://youtube.com/c/TapasAdhikary?sub_confirmation=1), so you can check it out, too.

You may also like these articles:

* [The JavaScript Array Handbook – JS Array Methods Explained with Examples](https://www.freecodecamp.org/news/the-javascript-array-handbook/)
* [A practical guide to object destructuring in JavaScript](https://blog.greenroots.info/a-practical-guide-to-object-destructuring-in-javascript)
* [JavaScript: Equality comparison with ==, === and Object.is](https://blog.greenroots.info/javascript-equality-comparison-with-and-objectis)
* [How NOT to use Git in Practice. Ten Git usages, you should know to avoid.](https://blog.greenroots.info/how-not-to-use-git-in-practice-ten-git-usages-you-should-know-to-avoid)




