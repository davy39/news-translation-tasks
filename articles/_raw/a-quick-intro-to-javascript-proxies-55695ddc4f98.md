---
title: A quick intro to JavaScript Proxies
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-04T19:48:23.000Z'
originalURL: https://freecodecamp.org/news/a-quick-intro-to-javascript-proxies-55695ddc4f98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*angpGt6Kog97_mI5sbi7Hg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Chuks Opia

  What is a JavaScript proxy? you might ask. It is one of the features that shipped
  with ES6. Sadly, it seems not to be widely used.

  According to the MDN Web Docs:


  The Proxy object is used to define custom behavior for fundamental operat...'
---

By Chuks Opia

What is a JavaScript proxy? you might ask. It is one of the features that shipped with ES6. Sadly, it seems not to be widely used.

According to the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy):

> The **Proxy** object is used to define custom behavior for fundamental operations (e.g. property lookup, assignment, enumeration, function invocation, etc).

In simple terms, proxies are **getters** and **setters** with lots of swag. A proxy object sits between an object and the outside world. They intercept calls to the attributes and methods of an object even if those attributes and methods don’t exist.

For us to understand how proxies work, we need to define three terms used by proxies:

1. **handler**: The placeholder object which contains traps (they’re the interceptors).
2. **traps**: The methods that provide property access (they live inside the handler).
3. **target**: The object which the proxy virtualizes.

#### Syntax

```js
let myProxy = new Proxy(target, handler);
```

### Why proxies?

Since proxies are similar to **getters** and **setters**, why should we use them? Let’s see why:

```js
const staff = {
  _name: "Jane Doe",
  _age: 25,
  get name() {
    console.log(this._name);
  },
  get age() {
    console.log(this._age);
  },
  set age(newAge) {
    this._age = newAge;
    console.log(this._age)
  }
};
staff.name // => "Jane Doe"
staff.age // => 25
staff.age = 30
staff.age // => 30
staff.position // => undefined
```

Let’s write the same code with proxies:

```js
const staff = {
  name: "Jane Doe",
  age: 25
}
const handler = {
  get: (target, name) => {
    name in target ? console.log(target[name]) : console.log('404 not found');
  },
  set: (target, name, value) => {
    target[name] = value;
  }
}
const staffProxy = new Proxy(staff, handler);
staffProxy.name // => "Jane Doe"
staffProxy.age // => 25
staffProxy.age = 30
staffProxy.age // => 30
staffProxy.position // => '404 not found'
```

In the above example using **getters** and **setters**, we have to define a **getter** and **setter** for each attribute in the `staff` object. When we try to access a non-existing property, we get `undefined`.

With proxies, we only need one `get` and `set` trap to manage interactions with every property in the `staff` object. Whenever we try to access a non-existing property, we get a custom error message.

There are many other use cases for proxies. Let’s explore some:

### Validation with proxies

With proxies, we can enforce value validations in JavaScript objects. Let’s say we have a `staff` schema and would like to perform some validations before a staff can be saved:

```js
const validator = {
  set: (target, key, value) => {
    const allowedProperties = ['name', 'age', 'position'];
    if (!allowedProperties.includes(key)) {
      throw new Error(`${key} is not a valid property`)
    }
    
    if (key === 'age') {
      if (typeof value !== 'number' || Number.isNaN(value) || value <= 0) {
        throw new TypeError('Age must be a positive number')
      }
    }
    if (key === 'name' || key === 'position') {
      if (typeof value !== 'string' || value.length <= 0) {
        throw new TypeError(`${key} must be a valid string`)
      }
    }
   target[key] = value; // save the value
   return true; // indicate success
  }
}
const staff = new Proxy({}, validator);
staff.stats = "malicious code" //=> Uncaught Error: stats is not a valid property
staff.age = 0 //=> Uncaught TypeError: Age must be a positive number
staff.age = 10
staff.age //=> 10
staff.name = '' //=> Uncaught TypeError: name must be a valid string
```

In the code snippet above, we declare a `validator` handler where we have an array of `allowedProperties`. In the `set` trap, we check if the key being set is part of our `allowedProperties`. If it’s not, we throw an error. We also check if the values being set are of certain data types before we save the value.

### Revocable proxies

What if we wanted to revoke access to an object? Well, JavaScript proxies have a `Proxy.revocable()` method which creates a revocable proxy. This gives us the ability to revoke access to a proxy. Let’s see how it works:

```js
const handler = {
  get: (target, name) => {
    name in target ? console.log(target[name]) : console.log('404 not found');
    console.log(target)
  },
  
  set: (target, name, value) => {
    target[name] = value;
  }
}
const staff = {
  name: "Jane Doe",
  age: 25
}
let { proxy, revoke } = Proxy.revocable(staff, handler);
proxy.age // => 25
proxy.name // => "Jane Doe"
proxy.age = 30
proxy.age // => 30
revoke() // revoke access to the proxy
proxy.age // => Uncaught TypeError: Cannot perform 'get' on a proxy that has been revoked
proxy.age = 30 // => Uncaught TypeError: Cannot perform 'set' on a proxy that has been revoked
```

In the example above, we are using destructuring to access the`proxy` and `revoke` properties of the object returned by `Proxy.revocable()`.

After we call the `revoke` function, any operation applied to `proxy` causes a `TypeError`. With this in our code, we can prevent users from taking certain actions on certain objects.

JavaScript proxies are a powerful way to create and manage interactions between objects. Other real world applications for Proxies include:

* Extending constructors
* Manipulating DOM nodes
* Value correction and an extra property
* Tracing property accesses
* Trapping function calls

And the list goes on.

There’s more to proxies than we have covered here. You can check the [Proxy MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) to find out all the available traps and how to use them.

I hope you found this tutorial useful. Please do and share so others can find this article. Hit me up on Twitter @d[evelopia_](https://twitter.com/developia_) with questions or for a chat.

