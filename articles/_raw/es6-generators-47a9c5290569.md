---
title: ES6 Generators
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-27T13:01:22.000Z'
originalURL: https://freecodecamp.org/news/es6-generators-47a9c5290569
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tBXQMulrsKL21K66SVQ5jA.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sanket Meghani

  Generators are one of the key features introduced in ES6. Contrary to normal functions
  which can only be entered at the beginning of the function, Generators are functions
  which can be exited and re-entered later with their context ...'
---

By Sanket Meghani

Generators are one of the key features introduced in ES6. Contrary to normal functions which can only be entered at the beginning of the function, Generators are functions which can be exited and re-entered later with their context (variable bindings) saved across re-entrances. In other words, Generator function could return a value midway and resume it’s execution from midway later on.

A generator can be defined using a function keyword followed by an asterisk.

The difference between calling a normal function and an iterator function is that calling a generator function does not execute the generator function immediately. It returns an iterator object for the generator instead. To execute the generator body we need to call next() method on the returned iterator.

```
let generator = myFirstGenerator(5);let output = generator.next();
```

When the iterator’s next() method is called, the generator function's body is executed until the first yield expression. Yield expression specifies the value to be returned. In the example above, calling generator.next() would execute the first console.log() statement and return output of (a + 5). The next() method returns an object in following structure.

```
{    value: 10, //Return value of yield expression. I.e 5 + 5    done: false //Weather generator has yielded it's last value}
```

We can print the returned yielded value using value property of the returned object.

```
let generator = myFirstGenerator(5);let output = generator.next(); //output = {value: 10, done: false}
```

```
console.log('Output is: ', output.value); //Output is: 10
```

Calling next() again on the iterator would continue execution of generator from last yield expression until next yield expression or a return statement is encountered.

```
output = generator.next(10); //output = {value: 15, done: true}
```

In our example, calling generator.next(10) would resume generator execution from line 4 with last yield expression value being 10 (i.e value passed to next()). Hence line 4 would be evaluated as b = 5 + 10 resulting into b = 15. On line 7 it returns the value of b and since this is the last return statement (i.e: no more yields left), done is set to true.

Calling the next() method with an argument will resume the generator function execution, replacing the yield statement where execution was paused with the argument from next().

```
output = generator.next(15); //output = {value: 20, done: true}
```

Calling generator.next(15) would resume generator execution from line 4 with last yield expression value replaced by 15. Hence line 4 would be evaluated as b = 5 + 15 resulting into b = 20.

We can use yield* to delegate to another generator function.

### **Postface**

It is quite intriguing to know how this new feature could be used in practice. [Redux-saga](http://yelouafi.github.io/redux-saga/) uses generator functions to make it easy to write asynchronous flows. We’ve just scratched the surface and there’s a lot more to them. I would love to hear your comments, suggestions or questions around ES6 generators and it’s use cases :).

