---
title: 'JavaScript Standard Objects: assign, values, hasOwnProperty, and getOwnPropertyNames
  Methods Explained'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-assign-values-hasownproperty-and-getownpropertynames-methods-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d0c740569d1a4ca359c.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'In JavaScript, the Object data type is used to store key value pairs, and
  like the Array data type, contain many useful methods. These are some useful methods
  you''ll use while working with objects.

  Object Assign Method

  The Object.assign() method is u...'
---

In JavaScript, the `Object` data type is used to store key value pairs, and like the `Array` data type, contain many useful methods. These are some useful methods you'll use while working with objects.

## Object Assign Method

The `Object.assign()` method is used to 

1. add properties and values to an existing object
2. make a new copy of an existing object, or 
3. combine multiple existing objects into a single object. 

The `Object.assign()` method requires one `targetObject` as a parameter and can accept an unlimited number of `sourceObjects` as additional parameters.

It's important to note here is that the `targetObject` parameter will always be modified. If that parameter points to an existing object, then that object will be both modified and copied. 

If, you wish to create a copy of an object without modifying that original object, you can pass an empty object `{}` as the first (`targetObject`) parameter and the object to be copied as the second (`sourceObject`) parameter.

If objects passed as parameters into `Object.assign()` share the same properties (or keys), property values that come later in the parameters list will overwrite those which came earlier.

**Syntax**

```javascript
Object.assign(targetObject, ...sourceObject);
```

**Return Value**

`Object.assign()` returns the `targetObject`.

### Examples

Modifying and copying `targetObject`:

```javascript
let obj = {name: 'Dave', age: 30};

let objCopy = Object.assign(obj, {coder: true});

console.log(obj); // { name: 'Dave', age: 30, coder: true }
console.log(objCopy); // { name: 'Dave', age: 30, coder: true }
```

Copying `targetObject` without modification:

```javascript
let obj = {name: 'Dave', age: 30};

let objCopy = Object.assign({}, obj, {coder: true});

console.log(obj); // { name: 'Dave', age: 30 }
console.log(objCopy); // { name: 'Dave', age: 30, coder: true }
```

Objects with the same properties_:_

```javascript
let obj = {name: 'Dave', age: 30, favoriteColor: 'blue'};

let objCopy = Object.assign({}, obj, {coder: true, favoriteColor: 'red'});

console.log(obj); // { name: 'Dave', age: 30, favoriteColor: 'blue' }
console.log(objCopy); // { name: 'Dave', age: 30, favoriteColor: 'red', coder: true }
```

## Object Values Method

The `Object.values()` method takes an object as a parameter and returns an array of its values. This makes it useful for chaining with common `Array` methods like `.map()`, `.forEach()`, and `.reduce()`.

**Syntax**

```text
Object.values(targetObject);
```

**Return value**

An array of the passed object's (`targetObject`) values.

### Examples

```js
const obj = { 
  firstName: 'Quincy',
  lastName: 'Larson' 
}

const values = Object.values(obj);

console.log(values); // ["Quincy", "Larson"]
```

If the object you're passing has numbers as keys, then `Object.value()` will return the values according to the numerical order of the keys:

```js
const obj1 = { 0: 'first', 1: 'second', 2: 'third' };
const obj2 = { 100: 'apple', 12: 'banana', 29: 'pear' };

console.log(Object.values(obj1)); // ["first", "second", "third"]
console.log(Object.values(obj2)); // ["banana", "pear", "apple"]
```

If something other than an object is passed to `Object.values()`, it will be coerced into an object before being returned as an array:

```js
const str = 'hello';

console.log(Object.values(str)); // ["h", "e", "l", "l", "o"]
```

## **Object hasOwnProperty Method**

The `Object.hasOwnProperty()` method returns a [boolean](https://www.freecodecamp.org/news/p/6bce9cb3-38ff-45d1-a56b-322354699b01/www.freecodecamp.org/news/booleans-in-javascript-explained-how-to-use-booleans-in-javascript/) indicating if the object owns the specified property.

This is a convenient method to check if an object has the specified property or not since it returns true/false accordingly.

**Syntax**

`Object.hasOwnProperty(prop)`

**Return value**

```js
true
// or
false
```

### **Examples**

Using `Object.hasOwnProperty()` to test if a property exist or not in a given object:

```js
const course = {
  name: 'freeCodeCamp',
  feature: 'is awesome',
}

const student = {
  name: 'enthusiastic student',
}

course.hasOwnProperty('name');  // returns true
course.hasOwnProperty('feature');   // returns true

student.hasOwnProperty('name');  // returns true
student.hasOwnProperty('feature'); // returns false
```

## Object getOwnPropertyNames Method

The `Object.getOwnPropertyNames()` method takes an object as a parameter and returns and array of all its properties.

**Syntax**

```text
Object.getOwnPropertyNames(obj)
```

**Return value**

An array of strings of the passed object's properties.

### Examples

```js
const obj = { firstName: 'Quincy', lastName: 'Larson' }

console.log(Object.getOwnPropertyNames(obj)); // ["firstName", "lastName"]
```

If something other than an object is passed to `Object.getOwnPropertyNames()`, it will be coerced into an object before being returned as an array:

```js
const arr = ['1', '2', '3'];

console.log(Object.getOwnPropertyNames(arr)); // ["0", "1", "2", "length"]
```

## **Promise.prototype.then**

A `Promise.prototype.then` function accepts two arguments and returns a Promise.

The first argument is a required function that accepts one argument. Successful fulfillment of a Promise will trigger this function.

The second argument is an optional function that also accepts one argument of its own. A thrown Error or Rejection of a Promise will trigger this function.

```javascript
   function onResolved (resolvedValue) {
     /*
     * access to resolved values of promise
     */
   }
 
  function onRejected(rejectedReason) {
     /*
     * access to rejection reasons of promise
     */
   }

  promiseReturningFunction(paramList)
     .then( // then function
       onResolved,
       [onRejected]
     );
```

`Promise.prototype.then` allows you to perform many asynchronous activities in sequence. You do this by attaching one `then` function to another separated by a dot operator.

```javascript
   promiseReturningFunction(paramList)
   .then( // first then function
     function(arg1) {
       // ...
       return someValue;
     }
   )
   ...
   .then( // nth then function
     function(arg2) {
       // ...
       return otherValue;
     }
   )
```

## **Map.prototype.entries**

Returns a new `Iterator` object that contains the `[key, value]` pairs for each element in the `Map` object in insertion order.

## **Syntax**

```javascript
myMap.entries()
```

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


var iterator = myMap.entries();

console.log(iterator.next().value); // ['foo', 1]
console.log(iterator.next().value); // ['bar', 2]
console.log(iterator.next().value); // ['baz', 3]
```

## More info on objects in JavaScript:

* [How to create objects in JavaScript](https://www.freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8/)
* [How to loop through objects in JavaScript](https://www.freecodecamp.org/news/how-to-loop-through-objects-in-javascript-a80b7d2478ac/)

## More info about booleans:

* [Booleans in JavaScript](https://www.freecodecamp.org/news/p/6bce9cb3-38ff-45d1-a56b-322354699b01/www.freecodecamp.org/news/booleans-in-javascript-explained-how-to-use-booleans-in-javascript/)


