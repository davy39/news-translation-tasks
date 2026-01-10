---
title: 'ES8: What’s new in the JavaScript language in 2017'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-15T08:54:55.000Z'
originalURL: https://freecodecamp.org/news/es8-the-new-features-of-javascript-7506210a1a22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9yuM4oWXT1Wfo0Cx5jkMwA.png
tags:
- name: es8
  slug: es8
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Flavio H. Freitas

  ES8 is live! Released earlier this summer, ES8 (also called ES2017) offers new ways
  of coding with JavaScript. Let''s explore them.

  If you have the latest version of Chrome, open the console and let''s code together.


  How to access...'
---

By Flavio H. Freitas

ES8 is live! Released earlier this summer, ES8 (also called ES2017) offers new ways of coding with JavaScript. Let's explore them.

If you have the latest version of Chrome, open the console and let's code together.

![Image](https://cdn-media-1.freecodecamp.org/images/IA-BH2UVyy--TrnW3x4zwQuxEMfW47VTVb5F align="left")

*How to access the JavaScript console in Chrome: View &gt; Developer &gt; JavaScript Console*

## Object.values()

Access all the values of our object without any complication. Here’s an example:

```javascript
const countries = {
    BR: 'Brazil',
    DE: 'Germany',
    RO: 'Romania',
    US: 'United States of America'
};

Object.values(countries); // ['Brazil', 'Germany', 'Romania', 'United States of America']
```

## Object.entries()

Turn your **object** attribute in an **array** of attributes:

```javascript
const countries = {
    BR: 'Brazil',
    DE: 'Germany',
    RO: 'Romania',
    US: 'United States of America'
};

Object.entries(countries); 
// [['BR', 'Brazil'], ['DE', 'Germany'], ['RO', 'Romania'], ['US','United States of America']]
```

## String padding (padStart and padEnd)

This returns the passed string adding the pad and the beginning or in the end of it. The function definition is:

```javascript
'string'.padStart(targetLength, padString)
'string'.padEnd(targetLength, padString)
```

We can make:

```javascript
'0.10'.padStart(10); // it return a string of length 10, padding empty spaces in the beginning
'hi'.padStart(1);            // 'hi'
'hi'.padStart(5);            // '   hi'
'hi'.padStart(5, 'abcd');    // 'abchi'
'hi'.padStart(10, 'abcd');   // 'abcdabcdhi'
'loading'.padEnd(10, '.');   // 'loading...'

// useful example making things easier to read
'0.10'.padStart(12);         // '       0.10'
'23.10'.padStart(12);        // '      23.10'
'12,330.10'.padStart(12);    // '  12,330.10'
```

## Object.getOwnPropertyDescriptors()

It returns all own (non-inherited) property descriptors of an object. The attributes of the return object can be: `value`, `writable`, `get`, `set`, `configurable` and `enumerable`.

```javascript
const obj = {
    name: 'Pablo',
    get foo() { return 42; }
};

Object.getOwnPropertyDescriptors(obj);
//
// {
//  "name": {
//     "value": "Pablo",
//     "writable":true,
//     "enumerable":true,
//     "configurable":true
//  },
//  "foo":{
//     "enumerable":true,
//     "configurable":true,
//     "get": function foo()
//     "set": undefined
//  }
// }
```

One practical example is: JavaScript has a method to copy properties `Object.assign()`. It copies the property whose key is `key`. Like this:

```javascript
const value = source[key]; // get
target[key] = value;       // set
```

And in some cases it fails because it doesn't properly copy the properties with non-default attributes such as getters, setters and non-writable properties.

For example:

```javascript
const objTarget = {};
const objSource = {
    set greet(name) { console.log('hey, ' + name); }
};

Object.assign(objTarget, objSource);
objTarget.greet = 'love';     // trying to set fails, sets greet = 'love'
```

Solving:

```javascript
const objTarget = {};
const objSource = {
    set greet(name) { console.log('hey, ' + name); }
};

Object.defineProperties(objTarget,          
           Object.getOwnPropertyDescriptors(objSource));

objTarget.greet = 'love'; // prints 'hey, love'
```

## Trailing commas in function parameter lists and calls

This is a syntax change. It allows us to write a valid function declaration with comma in the end.

```javascript
getDescription(name, age,) { ... }
```

## Async functions (async and await)

This makes it much easier to work with asynchronous functions:

```javascript
function loadExternalContent() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('hello');
        }, 3000);
    });
}

async function getContent() {
    const text = await loadExternalContent();
    console.log(text);
}

console.log('it will call function');
getContent();
console.log('it called function');

// it prints:
'it will call function' // synchronous
'it called function'    // synchronous
'hello'                 // asynchronous (after 3 seconds)
```

## Shared memory and atomics

According to the [specification](https://tc39.github.io/ecmascript_sharedmem/shmem.html):

> "Shared memory is being exposed in the form of a new SharedArrayBuffer type; The new global Atomics object provides atomic operations on shared memory locations, including operations that can be used to create blocking synchronization primitives."

This means:

Shared memory: we can allow multiple threads read and write the same data with the new `SharedArrayBuffer` constructor.

Atomics: We can use the `Atomics` object to make sure nothing that is being written or read will be interrupted in the middle of the process. So the operations are finished before a the next one starts.

If you enjoyed this article, be sure to like it give me a lot of claps — it means the world to the writer ? And f[ollow me](https://medium.com/@flaviohfreitas) if you want to read more articles about Culture, Technology and Startups.

**Flávio H. de Freitas** is an Entrepreneur, Engineer, Tech lover, Dreamer and Traveler. Has worked as **CTO** in **Brazil**, **Silicon Valley and Europe**.
