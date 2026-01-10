---
title: How to Use JavaScript Collections – Map and Set
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-10-05T16:59:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-javascript-collections-map-and-set
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/cover-5.png
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In JavaScript, objects are used to store multiple values as a complex data
  structure.

  An object is created with curly braces {…} and a list of properties. A property
  is a key-value pair where the key must be a string and the value can be of any type....'
---

In JavaScript, `objects` are used to store multiple values as a complex data structure.

An object is created with curly braces `{…}` and a list of properties. A property is a key-value pair where the `key` must be a string and the `value` can be of any type.

On the other hand, `arrays` are an ordered collection that can hold data of any type. In JavaScript, arrays are created with square brackets `[...]` and allow duplicate elements.

Until ES6 (ECMAScript 2015), JavaScript `objects` and `arrays` were the most important data structures to handle collections of data. The developer community didn't have many choices outside of that. Even so, a combination of objects and arrays was able to handle data in many scenarios.

However, there were a few shortcomings,

* Object keys can only be of type `string`.
* Objects don't maintain the order of the elements inserted into them.
* Objects lack some useful methods, which makes them difficult to use in some situations. For example, you can't compute the size (`length`) of an object easily. Also, enumerating an object is not that straightforward.
* Arrays are collections of elements that allow duplicates. Supporting arrays that only have distinct elements requires extra logic and code.

With the introduction of ES6, we got two new data structures that address the shortcomings mentioned above: `Map` and `Set`. In this article, we will look at both closely and understand how to use them in different situations.

## Map in JavaScript

`Map` is a collection of key-value pairs where the key can be of any type. `Map` remembers the original order in which the elements were added to it, which means data can be retrieved in the same order it was inserted in.

In other words, `Map` has characteristics of both `Object` and `Array`:

* Like an object, it supports the key-value pair structure.
* Like an array, it remembers the insertion order.

### **How to Create and Initialize a Map in JavaScript**

A new `Map` can be created like this:

```js
const map = new Map();
```

Which returns an empty `Map`:

```shell
Map(0) {}
```

Another way of creating a `Map` is with initial values. Here's how to create a `Map` with three key-value pairs:

```js
const freeCodeCampBlog = new Map([
  ['name', 'freeCodeCamp'],
  ['type', 'blog'],
  ['writer', 'Tapas Adhikary'],
]);
```

Which returns a `Map` with three elements:

```shell
Map(3) {"name" => "freeCodeCamp", "type" => "blog", "writer" => "Tapas Adhikary"}
```

### **How to Add values to a Map in JavaScript**

To add value to a Map, use the `set(key, value)` method.

The `set(key, value)` method takes two parameters, `key` and `value`, where the key and value can be of any type, a primitive (`boolean`, `string`, `number`, etc.) or an object:

```js
// create a map
const map = new Map();

// Add values to the map
map.set('name', 'freeCodeCamp');
map.set('type', 'blog');
map.set('writer', 'Tapas Adhikary');
```

Output:

```shell
Map(3) {"name" => "freeCodeCamp", "type" => "blog", "writer" => "Tapas Adhikary"}
```

Please note, if you use the same key to add a value to a `Map` multiple times, it'll always replace the previous value:

```js
// Add a different writer
map.set('writer', 'Someone else!');
```

So the output would be:

```shell
Map(3) 
{"name" => "freeCodeCamp", "type" => "blog", "writer" => "Someone else!"}
```

### **How to Get values from a Map in JavaScript**

To get a value from a `Map`, use the `get(key)` method:

```js
map.get('name'); // returns freeCodeCamp
```

### **All About Map Keys in JavaScript**

`Map` keys can be of any type, a primitive, or an object. This is one of the major differences between `Map` and regular JavaScript objects where the key can only be a string:

```js
// create a Map
const funMap = new Map();

funMap.set(360, 'My House Number'); // number as key
funMap.set(true, 'I write blogs!'); // boolean as key

let obj = {'name': 'tapas'}
funMap.set(obj, true); // object as key

console.log(funMap);
```

Here is the output:

```shell
Map(3) 
{
  360 => "My House Number", 
  true => "I write blogs!", 
  {…} => true
}
```

A regular JavaScript object always treats the key as a string. Even when you pass it a primitive or object, it internally converts the key into a string:

```js
// Create an empty object
const funObj = {};

// add a property. Note, passing the key as a number.
funObj[360] = 'My House Number';

// It returns true because the number 360 got converted into the string '360' internally!
console.log(funObj[360] === funObj['360']);
```

### **Map Properties and Methods in JavaScript**

JavaScript's `Map` has in-built properties and methods that make it easy to use. Here are some of the common ones:

* Use the `size` property to know how many elements are in a `Map`:
* Search an element with the `has(key)` method:
* Remove an element with the `delete(key)` method:
* Use the `clear()` method to remove all the elements from the `Map` at once:

```js
console.log('size of the map is', map.size);
```

```js
// returns true, if map has an element with the key, 'John'
console.log(map.has('John')); 


// returns false, if map doesn't have an element with the key, 'Tapas'
console.log(map.has('Tapas')); 
```

```js
map.delete('Sam'); // removes the element with key, 'Sam'.
```

```js
// Clear the map by removing all the elements
map.clear(); 

map.size // It will return, 0

```

### **MapIterator: keys(), values(), and entries() in JavaScript**

The methods `keys()`, `values()` and `entries()` methods return a `MapIterator`, which is excellent because you can use a `for-of` or `forEach` loop directly on it.

First, create a simple `Map`:

```js
const ageMap = new Map([
  ['Jack', 20],
  ['Alan', 34],
  ['Bill', 10],
  ['Sam', 9]
]);
```

* Get all the keys:
* Get all the values:
* Get all the entries (key-value pairs):

```js
console.log(ageMap.keys());

// Output:

// MapIterator {"Jack", "Alan", "Bill", "Sam"}
```

```js
console.log(ageMap.values());

// Output

// MapIterator {20, 34, 10, 9}
```

```js
console.log(ageMap.entries());

// Output

// MapIterator {"Jack" => 20, "Alan" => 34, "Bill" => 10, "Sam" => 9}
```

### **How to Iterate Over a Map in JavaScript**

You can use either the `forEach` or `for-of` loop to iterate over a `Map`:

```js
// with forEach
ageMap.forEach((value, key) => {
   console.log(`${key} is ${value} years old!`);
});

// with for-of
for(const [key, value] of ageMap) {
  console.log(`${key} is ${value} years old!`);
}
```

The output is going to be the same in both cases:

```shell
Jack is 20 years old!
Alan is 34 years old!
Bill is 10 years old!
Sam is 9 years old!
```

### **How to Convert an Object into a Map in JavaScript**

You may encounter a situation where you need to convert an `object` to a `Map`-like structure. You can use the method `entries` of `Object` to do that:

```js
const address = {
  'Tapas': 'Bangalore',
  'James': 'Huston',
  'Selva': 'Srilanka'
};

const addressMap = new Map(Object.entries(address));
```

### **How to Convert a Map into an Object in JavaScript**

If you want to do the reverse, you can use the `fromEntries` method:

```js
Object.fromEntries(map)
```

### **How to Convert a Map into an Array in JavaScript**

There are a couple of ways to convert a map into an array:

* Using `Array.from(map)`:
* Using the spread operator:

```js
const map = new Map();
map.set('milk', 200);
map.set("tea", 300);
map.set('coffee', 500);

console.log(Array.from(map));
```

```js
console.log([...map]);
```

### **Map vs. Object: When should you use them?**

`Map` has characteristics of both `object` and `array`. However, `Map` is more like an `object` than `array` due to the nature of storing data in the `key-value` format.

The similarity with objects ends here though. As you've seen, `Map` is different in a lot of ways. So, which one should you use, and when? How do you decide?

Use `Map` when:

* Your needs are not that simple. You may want to create keys that are non-strings. Storing an object as a key is a very powerful approach. `Map` gives you this ability by default.
* You need a data structure where elements can be ordered. Regular objects do not maintain the order of their entries.
* You are looking for flexibility without relying on an external library like lodash. You may end up using a library like lodash because we do not find methods like has(), values(), delete(), or a property like size with a regular object. Map makes this easy for you by providing all these methods by default.

Use an object when:

* You do not have any of the needs listed above.
* You rely on `JSON.parse()` as a `Map` cannot be parsed with it.

## Set in JavaScript

A `Set` is a collection of unique elements that can be of any type. `Set` is also an ordered collection of elements, which means that elements will be retrieved in the same order that they were inserted in.

A `Set` in JavaScript behaves the same way as a mathematical set.

### How to Create and Initialize a Set in JavaScript

A new `Set` can be created like this:

```js
const set = new Set();
console.log(set);
```

And the output will be an empty `Set`:

```shell
Set(0) {}
```

Here's how to create a `Set` with some initial values:

```js
const fruteSet = new Set(['🍉', '🍎', '🍈', '🍏']);
console.log(fruteSet);
```

Output:

```shell
Set(4) {"🍉", "🍎", "🍈", "🍏"}
```

### **Set Properties and Methods in JavaScript**

`Set` has methods to add an element to it, delete elements from it, check if an element exists in it, and to clear it completely:

* Use the `size` property to know the size of the `Set`. It returns the number of elements in it:
* Use the `add(element)` method to add an element to the `Set`:

```js
set.size
```

```js
// Create a set - saladSet
const saladSet = new Set();

// Add some vegetables to it
saladSet.add('🍅'); // tomato
saladSet.add('🥑'); // avocado
saladSet.add('🥕'); // carrot
saladSet.add('🥒'); // cucumber

console.log(saladSet);


// Output

// Set(4) {"🍅", "🥑", "🥕", "🥒"}
```

I love cucumbers! How about adding one more?

Oh no, I can't – `Set` is a collection of _unique_ elements:

```js
saladSet.add('🥒');
console.log(saladSet);
```

The output is the same as before – nothing got added to the `saladSet`.

* Use the `has(element)` method to search if we have a carrot (🥕) or broccoli (🥦) in the `Set`:
* Use the `delete(element)` method to remove the avocado(🥑) from the `Set`:

```js
// The salad has a🥕, so returns true
console.log('Does the salad have a carrot?', saladSet.has('🥕'));

// The salad doesn't have a🥦, so returns false
console.log('Does the salad have broccoli?', saladSet.has('🥦'));
```

```js
saladSet.delete('🥑');
console.log('I do not like 🥑, remove from the salad:', saladSet);
```

Now our salad `Set` is as follows:

```shell
Set(3) {"🍅", "🥕", "🥒"}
```

* Use the `clear()` method to remove all elements from a `Set`:

```js
saladSet.clear();
```

### **How to Iterate Over a Set** in JavaScript

`Set` has a method called `values()` which returns a `SetIterator` to get all its values:

```js
// Create a Set
const houseNos = new Set([360, 567, 101]);

// Get the SetIterator using the `values()` method
console.log(houseNos.values());
```

Output:

```js
SetIterator {360, 567, 101}
```

We can use a `forEach` or `for-of` loop on this to retrieve the values.

Interestingly, JavaScript tries to make `Set` compatible with `Map`. That's why we find two of the same methods as `Map`, `keys()` and `entries()`.

As `Set` doesn't have keys, the `keys()` method returns a `SetIterator` to retrieve its values:

```js
console.log(houseNos.keys());

// Output

// console.log(houseNos.keys());
```

With `Map`, the `entries()` method returns an iterator to retrieve key-value pairs. Again there are no keys in a `Set`, so `entries()` returns a `SetIterator` to retrieve the value-value pairs:

```js
console.log(houseNos.entries());

// Output

// SetIterator {360 => 360, 567 => 567, 101 => 101}
```

### **How to Enumerate over a Set in JavaScript**

We can enumerate over a Set using `forEach` and `for-of` loops:

```js
// with forEach

houseNos.forEach((value) => {
   console.log(value);
});


// with for-of

for(const value of houseNos) {
   console.log(value);
 }
```

The output of both is:

```shell
360
567
101
```

### **Sets and Arrays in JavaScript**

An array, like a `Set`, allows you to add and remove elements. But `Set` is quite different, and is not meant to replace arrays.

The major difference between an array and a `Set` is that arrays allow you to have duplicate elements. Also, some of the `Set` operations like `delete()` are faster than array operations like `shift()` or `splice()`.

Think of `Set` as an extension of a regular array, just with more muscles. The `Set` data structure is not a replacement of the `array`. Both can solve interesting problems.

### **How to Convert a Set into an array in JavaScript**

Converting a `Set` into an array is simple:

```js
const arr = [...houseNos];
console.log(arr);
```

### **Unique values from an array using the Set in JavaScript**

Creating a `Set` is a really easy way to remove duplicate values from an array:

```js
// Create a mixedFruit array with a few duplicate fruits
const mixedFruit = ['🍉', '🍎', '🍉', '🍈', '🍏', '🍎', '🍈'];

// Pass the array to create a set of unique fruits
const mixedFruitSet = new Set(mixedFruit);

console.log(mixedFruitSet);
```

Output:

```shell
Set(4) {"🍉", "🍎", "🍈", "🍏"}
```

### **Set and Object in JavaScript**

A `Set` can have elements of any type, even objects:

```js
// Create a person object
const person = {
   'name': 'Alex',
   'age': 32
 };

// Create a set and add the object to it
const pSet = new Set();
pSet.add(person);
console.log(pSet);
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-113.png)

No surprise here – the `Set` contains one element that is an object.

Let's change a property of the object and add it to the set again:

```js
// Change the name of the person
person.name = 'Bob';

// Add the person object to the set again
pSet.add(person);
console.log(pSet);
```

What do you think the output will be? Two `person` objects or just one?

Here is the output:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-114.png)

`Set` is a collection of unique elements. By changing the property of the object, we haven't changed the object itself. Hence `Set` will not allow duplicate elements.

`Set` is a great data structure to use in addition to JavaScript arrays. It doesn't have a huge advantage over regular arrays, though.

Use `Set` when you need to maintain a distinct set of data to perform set operations on like `union`, `intersection`, `difference`, and so on.

## **In Summary**

Here is a GitHub repository to find all the source code used in this article. If you found it helpful, please show your support by giving it a star: [https://github.com/atapas/js-collections-map-set](https://github.com/atapas/js-collections-map-set)

You may also like some of my other articles:

* [My Favorite JavaScript Tips and Tricks](https://blog.greenroots.info/my-favorite-javascript-tips-and-tricks-ckd60i4cq011em8s16uobcelc)
* [JavaScript equality and similarity with ==, === and Object.is()](https://blog.greenroots.info/javascript-equality-comparison-with-and-objectis-ckdpt2ryk01vel9s186ft8cwl)

If this article was useful, please share it so others can read it as well. You can @ me on Twitter ([@tapasadhikary](https://twitter.com/tapasadhikary)) with comments, or feel free to follow me.

