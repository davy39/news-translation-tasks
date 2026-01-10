---
title: How to Use the JavaScript Map and Set Objects – Explained with Code Examples
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-02-21T21:39:50.000Z'
originalURL: https://freecodecamp.org/news/javascript-map-and-set-objects-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/javascript-mat-and-set-objects-introduction.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Map and Set are two JavaScript data structures you can use to store a collection\
  \ of values, similar to Objects and Arrays. They are specialized data structures\
  \ that can help you store and manipulate related values. \nIn this tutorial, we\
  \ will see how ..."
---

Map and Set are two JavaScript data structures you can use to store a collection of values, similar to Objects and Arrays. They are specialized data structures that can help you store and manipulate related values. 

In this tutorial, we will see how Map and Set work in detail and when to use them. We will also explore the Set object composition methods that were recently added to the JavaScript standard.

## Table of Contents

<ul>
  <li><a href="#the-map-object-explained">The Map Object Explained</a></li>
  <ul>
    <li><a href="#how-to-create-a-map-object">How to Create a Map Object</a></li>
    <li>
      <a href="#map-object-methods-and-properties"
        >Map Object Methods and Properties</a
      >
    </li>
    <li>
      <a href="#other-ways-to-create-a-map-object"
        >Other Ways to Create a Map Object</a
      >
    </li>
    <li>
      <a href="#iterate-over-map-object-data">Iterate Over Map Object Data</a>
    </li>
    <li>
      <a href="#when-to-use-the-map-object">When to Use the Map Object</a>
    </li>
  </ul>
  <li><a href="#set-object-explained">Set Object Explained</a></li>
  <ul>
    <li>
      <a href="#how-to-create-a-set-object">How to create a Set Object</a>
    </li>
    <li>
      <a href="#set-object-methods-and-properties"
        >Set Object Methods and Properties</a
      >
    </li>
    <li><a href="#set-composition-methods">Set Composition Methods</a></li>
    <li><a href="#iterate-over-a-set-object">Iterate Over a Set Object</a></li>
    <li>
      <a href="#when-to-use-the-set-object">When to Use the Set Object</a>
    </li>
  </ul>
  <li><a href="#conclusion">Conclusion</a></li>
</ul>


## The Map Object Explained

The `Map` object stores data in a key/value pair structure, just like an Object. The main differences between a regular object and a `Map` are:

* A `Map` can have any type of data as the key value
* A `Map` maintains the order of data added to the object

### How to Create a Map Object

To create a `Map` object, you can call the `Map()` constructor as follows:

```js
const myMap = new Map();
```

The code above creates a new empty `Map` object.

### Map Object Methods and Properties

A `Map` object has the following methods and properties:

* `set(key, value)` – Adds a key/value pair to a Map
* `get(key)` – Retrieves a value from a Map (returns `undefined` if key doesn't exist)
* `has(key)` – Checks if a Map has a specific key
* `delete(key)` – Removes a specific key from a Map
* `clear()` – Removes all items from a Map
* `keys()` – Returns all keys in a Map
* `values()` – Returns all values in a Map
* `entries()` – Returns all keys and values in a Map
* `size` – Returns the number of items in Map

To insert data into the `Map` object, you can use the `set()` method:

```js
const myMap = new Map();

myMap.set(1, 'Jack');
myMap.set(2, 'Jill');
myMap.set('animal', 'Elephant');
```

The code above creates a `Map` object with 3 entries as follows:

```txt
Map(3)
0: {1 => "Jack"}
1: {2 => "Jill"}
2: {"animal" => "Elephant"}
```

To retrieve a value from the `Map` object, you need to use the `get()` method and pass the key as its argument:

```js
console.log(myMap.get(1)); // Jack

console.log(myMap.get('animal')); // Elephant


```

 To see how many key/value pairs a `Map` has, you can access the `size` property:

```js
myMap.size; // 3
```

To see if a certain key exists in a `Map` object, you can use the `has()` method. See the example below:

```js
myMap.has(1); // true

myMap.has(10); // false
```

To remove a key/value pair from a `Map` object, you can use the `delete()` method and pass the key of the pair you want to remove as follows:

```js
myMap.delete(1);

console.log(myMap);
// 0: {2 => "Jill"}
// 1: {"animal" => "Elephant"}
```

If you want to remove all key/value pairs, you can use the `clear()` method instead:

```js
myMap.clear();

console.log(myMap); // Map(0) {size: 0}
```

### Other Ways to Create a Map Object

You can also create a `Map` object from an Array as follows:

```js
const myMap = new Map([
  [1, 'Jack'],
  [2, 'Jill'],
  ['animal', 'Elephant'],
]);
```

When creating a `Map` from an Array, you need to create a two-dimensional array and specify two elements in each array. 

The first element will be the key, the second element will be the value. Any extra value in the array will be ignored.

In the example below, the value 'Johnson' from the first array will be ignored by the `Map()` constructor:

```js
const myMap = new Map([
  [1, 'Jack', 'Johnson'], // the value 'Johnson' is ignored
  [2, 'Jill'],
  ['animal', 'Elephant'],
]);
```

Because you can create a `Map` object from an array, you can also create one from an object. You need to transform the object into an array first using the `Object.entries()` method.

The following example shows how to use an object to create a `Map`:

```js
const person = {
    'name': 'Jack',
    'age': 20,
}

const myMap = new Map(Object.entries(person));

console.log(myMap); // Map(2) { 'name' => 'Jack', 'age' => 20 }
```

### Iterate Over Map Object Data

To iterate over a `Map` object data, you can use either the `forEach()` method or the `for .. of` loop:

```js
const myMap = new Map([
  [1, 'Jack'],
  [2, 'Jill'],
  ['animal', 'Elephant'],
]);

// iterate using the forEach() method
myMap.forEach((value, key) => {
  console.log(`${key}: ${value}`);
});

// or using the for .. of loop

for (const [key, value] of myMap) {
  console.log(`${key}: ${value}`);
}
```

Both methods give the same output:

```txt
1: Jack
2: Jill
animal: Elephant
```

### When to Use the Map Object

You can think of the `Map` object as an upgraded version of the regular Object. It can use any type of data as the key value, while an object can only use string values as keys.

Under the hood, the `Map` object performs better when you need to add and remove keys, so you might consider using it when your data changes frequently.

Also, the Map object has many useful methods for data manipulation, such as `has()` to see if the Map contains a specific key, `keys()` to get all keys defined in the `Map`, `values` to get all values, and `entries()` to get all key/value pairs.

But if you only want to create an object without further manipulation, then you don't need to use the `Map` object. 

One example is when you send a network request using the `fetch()` method. You would create an object and convert it into a JSON string, so using a `Map` object won't give any benefit.

## Set Object Explained

The `Set` object allows you to store a collection of elements, just like an Array. The differences between a `Set` and an array are:

* A `Set` requires all elements to be unique
* A `Set` has fewer methods for data manipulation

### How to Create a Set Object

To create a new `Set` object, you need to call the `Set()` constructor as follows:

```js
const mySet = new Set();
```

The code above will create a new empty set.

### Set Object Methods and Properties 

A `Set` object has the following methods and properties:

* `add(value)` – Adds a value to a Set
* `has(value)` – Checks if a Set contains a specific value
* `delete(value)` – Removes a specific value from a Set
* `clear()` – Removes all items from a Set
* `keys()` – Returns all values in a Set
* `values()` – Returns all values in a Set
* `entries()` – Returns all values in a Set as `[value, value]` array
* `size` – Returns the number of items in Set

Note that the `keys()` and `values()` methods in a Set object return the same output.

There's also the `entries()` method which returns an array as follows:

```js
const mySet = new Set(['Jack', 'Jill', 'John']);

console.log(mySet.entries());
```

Output:

```txt
[Set Entries] {
  [ 'Jack', 'Jack' ],
  [ 'Jill', 'Jill' ],
  [ 'John', 'John' ]
}
```

Notice how the values are repeated once in each array above. The `entries()` method is created to make `Set` similar to the `Map` object, but you probably don't need it.

There are extra methods that you can use to interact with another `Set` object. We'll discuss them in the next section.

To add an element to the Set object, you can use the add method:

```js
const mySet = new Set();

mySet.add(1);
mySet.add(2);
mySet.add(3);

console.log(mySet); // [1, 2, 3]
```

To get all values stored in a `Set`, call the `values()` method:

```js
mySet.values(); // [Set Iterator] { 'Jack', 'Jill', 'John' }
```

To check if the `Set` has a specific value, use the `has()` method:

```js
mySet.has('Jack'); // true

mySet.has('Michael'); // false
```

To remove a single value, call the `delete()` method. To remove all values, use the `clear()` method:

```js
mySet.delete('Jill');

mySet.clear();
```

### Set Composition Methods

Aside from the regular methods above, `Set` also has composition methods that you can use to perform various set theory operations such as difference, union, and intersection.

The following table is from [MDN Set documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set_composition):

![Image](https://www.freecodecamp.org/news/content/images/2024/02/set-composition-methods.png)
_A List of Set Composition Methods_

For example, you can get a set containing the differences between two other sets as follows:

```js
const setA = new Set([1, 2, 3, 4, 5]);

const setB = new Set([4, 5, 6, 7, 8]);

const diffsA = setA.difference(setB); // Set(3) {1, 2, 3}
const diffsB = setB.difference(setA); // Set(3) {6, 7, 8}

```

Here, the `setA.difference(setB)` returns a `Set` containing values unique to the `setA` object.

The opposite values are returned when you run `setB.difference(setA)` method.

Note that these methods are new additions to the JavaScript standard, and as of this writing, only Safari 17 and Chrome 122 support these methods.

Most likely, these methods will be included in Node.js soon.

### Iterate Over a Set Object

To iterate over a `Set` object, you can use either the `forEach()` method or the `for .. of` loop:

```js
const mySet = new Set(['Jack', 'Jill', 'John']);

// iterate using the forEach() method
mySet.forEach(value => {
  console.log(value);
});

// or using the for .. of loop

for (const value of mySet) {
  console.log(value);
}
```

Output:

```txt
Jack
Jill
John
```

### When to Use the Set Object

You can think of the `Set` object as the alternative version of the regular Array.

Because a `Set` object ignores duplicate values, you can use this object to purge duplicates from an Array, then turn the `Set` object back to an Array:

```js
const myArray = [1, 1, 2, 2, 3, 3];

const uniqueArray = [...new Set(myArray)];

console.log(uniqueArray); // [ 1, 2, 3 ]
```

Another reason you may want to use a `Set` is when you need to compose multiple set objects using the composition methods, such as `union()` and `difference()`. These methods are not available in an Array.

## Conclusion

In this article, you've learned how the Map and Set objects work and when to use them in your code.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://codewithnathan.com/beginning-modern-javascript).

[![](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://codewithnathan.com/beginning-modern-javascript)

The book is designed to be easy for beginners and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic web application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

See you later!

