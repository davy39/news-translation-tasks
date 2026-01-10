---
title: What Happens When You Freeze a Prototype in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-03T07:34:33.000Z'
originalURL: https://freecodecamp.org/news/what-happens-when-you-freeze-a-prototype
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/DSC03702.JPG
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Cristian Salcescu

  Have you wondered what happens when you freeze the prototype of an object? Let''s
  find out together.

  Objects

  In JavaScript, objects are dynamic collections of properties with a “hidden” property.
  We start by creating such an objec...'
---

By Cristian Salcescu

Have you wondered what happens when you freeze the prototype of an object? Let's find out together.

## Objects

In JavaScript, objects are dynamic collections of properties with a “hidden” property. We start by creating such an object using the object literal syntax.

```js
const counter = {
  count: 0,
  
  increment(){
    this.count += 1;
    return this.count;
  },
  
  decrement(){
    this.count -= 1;
    return this.count
  }  
}

console.log(counter.increment())
```

 `counter` is an object with a field and two methods operating on it.

## Prototypes

Objects can inherit properties from prototypes. As a matter of fact, the `counter` object already inherits from the `Object.prototype` object. 

For example we can call the `toString()` method on the `counter` object even if we haven’t defined it.

```js
counter.toString();
```

The best way to work with prototypes is to extract out the methods in the prototype and then share them between all objects having the same behavior. Let’s do that using [Object.create()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create).

```js
const counterPrototype = {
  increment(){
    this.count += 1;
    return this.count;
  },
  
  decrement(){
    this.count -= 1;
    return this.count
  }
}

const counter = Object.create(counterPrototype);
counter.count = 0;
console.log(counter.increment())
//1
```

The `Object.create()` creates a new object, using an existing object as the prototype of the new object.  `counter` has  `counterPrototype` as its prototype. 

The prototype system is flexible but has some downfalls. All properties are public and can be changed. 

For example, we can redefine the implementation of the `increment()` object in the `counter` object.

```js
const counter = Object.create(counterPrototype);
counter.count = 0;

counter.increment = function(){
  console.log('increment')
}

console.log(counter.increment());
//"increment"
```

## Freezing Prototypes

Let’s see what happens if we freeze the prototype. Freezing an object doesn’t allow us to add, remove, or change its properties.

```js
const counterPrototype = Object.freeze({
  increment(){
    this.count += 1;
    return this.count;
  },
  
  decrement(){
    this.count -= 1;
    return this.count
  }
});

counterPrototype.increment = function(){
  console.log('increment')
}
//Cannot assign to read only property 'increment' of object '#'
```

The `Object.freeze()` freezes an object. A frozen object can no longer be changed. We cannot add, edit, or remove properties from it.

Now take a look at what happens when trying to change the method in the `counter` object inheriting from `counterPrototype`.

```js
const counter = Object.create(counterPrototype);
counter.count = 0;

counter.increment = function(){
  console.log('increment')
}
//Cannot assign to read only property 'increment' of object

console.log(counter.increment());
//1
```

As you can see now that the prototype is frozen we are not able to change the `increment()` method in the `counter` object. 

## Recap

Objects have a hidden property referring their prototype.

The prototype is usually used to keep the methods that are shared between different objects.

Freezing the prototype does not allow us to change those properties in the objects inheriting from that prototype. The other properties can be changed.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best Functional Programming books**](https://bookauthority.org/books/best-functional-programming-books) by BookAuthority!

For more on applying functional programming techniques to React take a look at **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

