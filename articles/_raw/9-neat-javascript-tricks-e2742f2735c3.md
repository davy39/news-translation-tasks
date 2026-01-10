---
title: Learn these neat JavaScript tricks in less than 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-22T18:07:10.000Z'
originalURL: https://freecodecamp.org/news/9-neat-javascript-tricks-e2742f2735c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nhDglPZmEcmo2KDg7u4gxw.png
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Alcides Queiroz

  Time-saving techniques used by pros


  1. Clearing or truncating an array

  An easy way of clearing or truncating an array without reassigning it is by changing
  its length property value:

  const arr = [11, 22, 33, 44, 55, 66];

  // trunca...'
---

By Alcides Queiroz

#### Time-saving techniques used by pros

![Image](https://cdn-media-1.freecodecamp.org/images/QuQa8vSRsqE3AzHx-lx1Sdxf4jKSObxgHKqd)

#### 1. Clearing or truncating an array

An easy way of clearing or truncating an array without reassigning it is by changing its `length` property value:

```
const arr = [11, 22, 33, 44, 55, 66];
```

```
// truncantingarr.length = 3;console.log(arr); //=> [11, 22, 33]
```

```
// clearingarr.length = 0;console.log(arr); //=> []console.log(arr[2]); //=> undefined
```

#### 2. Simulating named parameters with object destructuring

Chances are high that you’re already using configuration objects when you need to pass a variable set of options to some function, like this:

```
doSomething({ foo: 'Hello', bar: 'Hey!', baz: 42 });
```

```
function doSomething(config) {  const foo = config.foo !== undefined ? config.foo : 'Hi';  const bar = config.bar !== undefined ? config.bar : 'Yo!';  const baz = config.baz !== undefined ? config.baz : 13;  // ...}
```

This is an old but effective pattern, which tries to simulate named parameters in JavaScript. The function calling looks fine. On the other hand, the config object handling logic is unnecessarily verbose. With ES2015 object destructuring, you can circumvent this downside:

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 }) {  // ...}
```

And if you need to make the config object optional, it’s very simple, too:

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 } = {}) {  // ...}
```

#### 3. Object destructuring for array items

Assign array items to individual variables with object destructuring:

```
const csvFileLine = '1997,John Doe,US,john@doe.com,New York';
```

```
const { 2: country, 4: state } = csvFileLine.split(',');
```

#### 4. Switch with ranges

> **NOTE:** After some thought, I’ve decided to differentiate this trick from the others in this article. This is **NOT** a time-saving technique, **NOR** is it suitable for real life code. **Keep in mind:** “If”s are always better in such situations.   
> Differently from the other tips in this post, it is more a curiosity than something to really use.   
> Anyway, **I’ll keep it in this article for historical reasons.**

Here’s a simple trick to use ranges in switch statements:

```
function getWaterState(tempInCelsius) {  let state;    switch (true) {    case (tempInCelsius <= 0):       state = 'Solid';      break;    case (tempInCelsius > 0 && tempInCelsius < 100):       state = 'Liquid';      break;    default:       state = 'Gas';  }
```

```
  return state;}
```

#### 5. Await multiple async functions with async/await

It’s possible to `await` multiple async functions to finish by using `Promise.all`:

```
await Promise.all([anAsyncCall(), thisIsAlsoAsync(), oneMore()])
```

#### 6. Creating pure objects

You can create a 100% pure object, which won’t inherit any property or method from `Object` (for example, `constructor`, `toString()` and so on).

```
const pureObject = Object.create(null);
```

```
console.log(pureObject); //=> {}console.log(pureObject.constructor); //=> undefinedconsole.log(pureObject.toString); //=> undefinedconsole.log(pureObject.hasOwnProperty); //=> undefined
```

#### 7. Formatting JSON code

`JSON.stringify` can do more than simply stringify an object. You can also beautify your JSON output with it:

```
const obj = {   foo: { bar: [11, 22, 33, 44], baz: { bing: true, boom: 'Hello' } } };
```

```
// The third parameter is the number of spaces used to // beautify the JSON output.JSON.stringify(obj, null, 4); // =>"{// =>    "foo": {// =>        "bar": [// =>            11,// =>            22,// =>            33,// =>            44// =>        ],// =>        "baz": {// =>            "bing": true,// =>            "boom": "Hello"// =>        }// =>    }// =>}"
```

#### 8. Removing duplicate items from an array

By using ES2015 Sets along with the Spread operator, you can easily remove duplicate items from an array:

```
const removeDuplicateItems = arr => [...new Set(arr)];
```

```
removeDuplicateItems([42, 'foo', 42, 'foo', true, true]);//=> [42, "foo", true]
```

#### 9. Flattening multidimensional arrays

Flattening arrays is trivial with Spread operator:

```
const arr = [11, [22, 33], [44, 55], 66];
```

```
const flatArr = [].concat(...arr); //=> [11, 22, 33, 44, 55, 66]
```

Unfortunately, the above trick will only work with bidimensional arrays. But with recursive calls, we can make it suitable for arrays with more than 2 dimensions:

```
function flattenArray(arr) {  const flattened = [].concat(...arr);  return flattened.some(item => Array.isArray(item)) ?     flattenArray(flattened) : flattened;}
```

```
const arr = [11, [22, 33], [44, [55, 66, [77, [88]], 99]]];
```

```
const flatArr = flattenArray(arr); //=> [11, 22, 33, 44, 55, 66, 77, 88, 99]
```

And there you have it! I hope these neat little tricks help you write better and more beautiful JavaScript.

