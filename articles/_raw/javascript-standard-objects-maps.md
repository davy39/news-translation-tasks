---
title: 'JavaScript Standard Objects: Maps'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-maps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d30740569d1a4ca3660.jpg
tags:
- name: JavaScript
  slug: javascript
- name: maps
  slug: maps
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "The Map object is a relatively new standard built-in object that holds\
  \ [key, value] pairs in the order that they're inserted. \nThe keys and values in\
  \ the Map object can be any value (both objects and primitive values are valid).\n\
  Syntax\nnew Map([itera..."
---

The `Map` object is a relatively new standard built-in object that holds `[key, value]` pairs in the order that they're inserted. 

The keys and values in the `Map` object can be any value (both objects and primitive values are valid).

## **Syntax**

```javascript
new Map([iterable])
```

## **Parameters**

**iterable** An Array or other iterable object whose elements are key-value pairs.

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo', 1);
myMap.set('bar', 2);
myMap.set('baz', 3);

myMap.get('foo');   // returns 1
myMap.get('baz');   // returns 3
myMap.get('hihi');  // return undefined

myMap.size;   // 3

console.log(myMap); // Map { 'foo' => 1, 'bar' => 2, 'baz' => 3 }
```

It's easy to create a new `Map` from existing 2D arrays of key-value pairs:

```js
const myArr = [['foo', 1], ['bar', 2], ['baz', 3]];
const arrMap = new Map(myArr);

console.log(arrMap); // Map { 'foo' => 1, 'bar' => 2, 'baz' => 3 }
```

You can also convert an object into a `Map` with the help of the `Object.entries`:

```js
const myObj = {
  foo: 1,
  bar: 2,
  baz: 3
}
const objMap = new Map(Object.entries(myObj));

console.log(objMap); // Map { 'foo' => 1, 'bar' => 2, 'baz' => 3 }
```

## **Map.prototype.get**

Returns the value of the specified key from a `Map` object.

## **Syntax**

```javascript
myMap.get(key);
```

## **Parameters**

**key** Required.

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);

myMap.get('foo');   // returns 1
myMap.get('baz');   // returns 3
myMap.get('hihi');  // return undefined
```

## **Map.prototype.set**

Sets or updates an element with the specified key and value in a `Map` object. The `set()` method also returns the `Map` object.

## **Syntax**

```javascript
myMap.set(key, value);
```

## **Parameters**

* **key** Required
* **value** Required

## **Example**

```javascript
const myMap = new Map();

// sets new elements
myMap.set('foo', 1);
myMap.set('bar', 2);
myMap.set('baz', 3);

// Updates an existing element
myMap.set('foo', 100);

myMap.get('foo');   // returns 100
```

Because `set()` returns the `Map` object it operated on, the method can be easily chained. For example, the code above can be simplified to:

```js
const myMap = new Map();

// sets new elements
myMap.set('foo', 1)
  .set('bar', 2)
  .set('baz', 3)
  .set('foo', 100); // Updates an existing element

myMap.get('foo');   // returns 100
```

## **Map.prototype.size**

Returns the number of elements in a `Map` object.

## **Syntax**

```javascript
myMap.size();
```

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


myMap.size(); // 3
```

## **Map.prototype.keys**

Returns a new `Iterator` object that contains the keys for each element in the `Map` object in insertion order.

## **Syntax**

```javascript
myMap.keys()
```

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


const iterator = myMap.keys();

console.log(iterator.next().value); // 'foo'
console.log(iterator.next().value); // 'bar'
console.log(iterator.next().value); // 'baz'
```

## **Map.prototype.values**

Returns an iterator object that contains the values for each element in the `Map` object in the order they were inserted.

## **Syntax**

```javascript
myMap.values()
```

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


const iterator = myMap.values();
console.log(iterator.next().value); // 1
console.log(iterator.next().value); // 2
console.log(iterator.next().value); // 3
```

## **Map.prototype.delete**

Removes the specified element from a `Map` object. Returns whether the key was found and successfully deleted.

## **Syntax**

```javascript
myMap.delete(key);
```

## **Parameters**

**key** Required.

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


myMap.size(); // 3
myMap.has('foo'); // true;

myMap.delete('foo');  // Returns true. Successfully removed.

myMap.size(); // 2
myMap.has('foo');    // Returns false. The "foo" element is no longer present.
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


const iterator = myMap.entries();

console.log(iterator.next().value); // ['foo', 1]
console.log(iterator.next().value); // ['bar', 2]
console.log(iterator.next().value); // ['baz', 3]
```

## **Map.prototype.clear**

Removes all elements from a `Map` object and returns `undefined`.

## **Syntax**

```javascript
myMap.clear();
```

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


myMap.size(); // 3
myMap.has('foo'); // true;

myMap.clear(); 

myMap.size(); // 0
myMap.has('foo'); // false
```

## **Map.prototype.has**

Given a `Map` with elements inside, the `has()` function allows you to determine whether or not an element exists inside the Map, based on a key that you pass.

The `has()` function returns a _`Boolean` primitive_ (either `true` or `false`), which indicates that the Map contains the element or not.

You pass a `key` parameter to the `has()` function, which will be used to look for an element with that key inside the Map.

Example:

```js
// A simple Map
const campers = new Map();

// add some elements to the map
// each element's key is 'camp' and a number
campers.set('camp1', 'Bernardo');
campers.set('camp2', 'Andrea');
campers.set('camp3', 'Miguel');

// Now I want to know if there's an element
// with 'camp4' key:
campers.has('camp4');
// output is `false`
```

The `campers` Map does not currently have an element with a `'camp4'` key. Therefore, the `has('camp4')` function call will return `false`.

```js
// If we add an element with the 'camp4' key to the map
campers.set('camp4', 'Ana');

// and try looking for that key again
campers.has('camp4');
// output is `true`
```

Since the map now does have an element with a `'camp4'` key, the `has('camp4')` function call will return `true` this time!

In a more real-world scenario, you might not manually add the elements to the Map yourself, so the `has()` function would become really useful in those cases.

## **Map.prototype.forEach**

Executes the passed function on each key-value pair in the `Map` object. Returns `undefined`.

## **Syntax**

```javascript
myMap.forEach(callback, thisArg)
```

## **Parameters**

* **callback** Function to execute for each element. 
* **thisArg** Value to use as this when executing callback.

## **Example**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);

function valueLogger(value) {
  console.log(`${value}`);
}

myMap.forEach(valueLogger);
// 1
// 2
// 3
```

