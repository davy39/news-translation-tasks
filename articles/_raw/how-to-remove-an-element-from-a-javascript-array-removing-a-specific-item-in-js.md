---
title: How to Remove an Element from a JavaScript Array – Removing a Specific Item
  in JS
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-08-31T17:00:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-an-element-from-a-javascript-array-removing-a-specific-item-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/vinicius-amnx-amano-dbOV1qSiL-c-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'You will often need to remove an element from an array in JavaScript, whether
  it''s for a queue data structure, or maybe from your React State.

  In the first half of this article you will learn all the methods that allow you
  to remove an element from a...'
---

You will often need to remove an element from an array in JavaScript, whether it's for a queue data structure, or maybe from your React State.

In the first half of this article you will learn all the methods that allow you to remove an element from an array without mutating the original array. In fact, this is what you will want to do most often. For example, if you don't want to mutate your React State. Or the array is used in other parts of your code, and mutating it would cause unexpected issues.

Always better to avoid mutations!

But, for completeness, the second half of the article will list methods to remove an item from an array in place. These methods do mutate the array itself.

Here you can find a handy summary of the article content, if you want to navigate to a section in particular.

- [How to remove an element from an array without mutating the array](#heading-how-to-remove-an-element-from-an-array-without-mutating-the-array)
    - [Remove the first element of an array with `slice`](#heading-remove-the-first-element-of-an-array-with-slice)
    - [Remove the last element of an array with `slice`](#heading-remove-the-last-element-of-an-array-with-slice)
    - [Remove an element at any position of an array with `slice` and `concat`](#heading-remove-an-element-at-any-position-of-an-array-with-slice-and-concat)
    - [Remove an element of a certain value with `filter`](#heading-remove-an-element-of-a-certain-value-with-filter)
    - [Remove an element from an array with a `for` loop and `push`](#heading-remove-an-element-from-an-array-with-a-for-loop-and-push)
    - [Remove the first element of an array with destructuring and the rest operator](#heading-remove-the-first-element-of-an-array-with-destructuring-and-the-rest-operator)
- [How to remove an element from an array while mutating the array](#heading-how-to-remove-an-element-from-an-array-while-mutating-the-array)
    - [Remove the last element of an array with `pop`](#heading-remove-the-last-element-of-an-array-with-pop)
    - [Remove the first element of an array with `shift`](#heading-remove-the-first-element-of-an-array-with-shift)
    - [Remove an element at any index with `splice`](#heading-remove-an-element-at-any-index-with-splice)
- [Conclusion](#heading-conclusion)


## How to remove an element from an array without mutating the array

If you have an input array, like as a function parameter, best practices dictate that you should not mutate the array. Instead you should create a new one.

There are a few methods you can use to remove a specific item from an array without mutating the array.

To avoid mutating the array, a new array will be created without the element you want to remove.

You could use methods like:

* `Array.prototype.slice()`
* `Array.prototype.slice()` together with `Array.prototype.concat()`
* `Array.prototype.filter()`
* A `for` loop and `Array.prototype.push()`

Let's see in detail how you could use each one of these to remove an element from an array without mutating the original one.

### Remove the first element of an array with `slice`

If you want to remove the first element in an array, you can use `Array.prototype.slice()` on an array named `arr` like this: `arr.slice(1)`.

Here is a complete example, in which you want to remove the first element from an array containing the first 6 letters of the alphabet.

```javascript
// the starting array
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

// here the array is copied, without the first element
const copyWithoutFirstElement = arrayOfLetters.slice(1);

// arrayOfLetters is unchanged
console.log(arrayOfLetters) // ['a', 'b', 'c', 'd', 'e', 'f']

// and copyWithoutFirstElement contains the letters from b to f
console.log(copyWithoutFirstElement) // ['b', 'c', 'd', 'e', 'f']
```

The `slice` method can take a single number as argument, and in this case it copies from that index to the end of the array. So using `arrayOfLetters.slice(1)` will create a copy of the `arrayOfLetters` array that excludes the first element.

### Remove the last element of an array with `slice`

If the element you want to remove is the last element of the array, you can use `Array.prototype.slice()` on an array named `arr` in this way: `arr.slice(0, -1)`.

Here is a complete example using the same alphabet array from above, starting with an array of the first 6 alphabet letters.

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];
const copyWithoutLastElement = arrayOfLetters.slice(0, -1);

// arrayOfLetters is unchanged
console.log(arrayOfLetters) // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(copyWithoutLastElement) // ['a', 'b', 'c', 'd', 'e']
```

The `slice` method takes up to two parameters. The first index of `slice` indicates from which index to start the copy, and the second argument says up to which element to copy – but it's not inclusive.

`slice` accepts a negative index to count from the end. This means that writing `-1` would mean the last index. So from `0` to `-1` means to create a copy from index `0` up to (but not including) the last index. The end result is that the last element is not included in the copy.

### Remove an element at any position of an array with `slice` and `concat`

If you want to create a copy that is missing an element at any index you can use `Array.prototype.slice` and `Array.prototype.concat` together in this way: `arrayOfLetters.slice(0, n).concat(arrayOfLetters.slice(n+1))` where `n` is the index of the element you want to remove.

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

const halfBeforeTheUnwantedElement = arrayOfLetters.slice(0, 2)

const halfAfterTheUnwantedElement = arrayOfLetters(3);

const copyWithoutThirdElement = halfBeforeTheUnwantedElement.concat(halfAfterTheUnwantedElement);

// arrayOfLetters is unchanged
console.log(arrayOfLetters) // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(copyWithoutFifthElement) // ['a', 'b', 'd', 'e', 'f']
```

This use of `slice` is a way to put together the two previous uses.

The first use of `slice` will create an array from the beginning to just before the element you want to remove.

The second use of `slice` creates an array from after the element you want to remove to the end of the array.

The two arrays are concatenated together with `concat` to form an array that is similar to the starting one, but without a particular element.

### Remove an element of a certain value with `filter`

If you want to remove an element with a certain value, you can use `Array.prototype.filter()`. Let's take the same `arrayOfLetters` and create a copy without the `d`.

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

const arrayWithoutD = arrayOfLetters.filter(function (letter) {
    return letter !== 'd';
});

// arrayOfLetters is unchanged
console.log(arrayOfLetters); // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(arrayWithoutD); // ['a', 'b', 'c', 'e', 'f']
```

`filter` takes a callback, and tests all the elements of the array with that callback. It keeps the elements for which the callback returns `true` (or a truthy value) and excludes the elements for which the callback returns `false` (or a falsy value).

In this case, the callback checks `letter !== "d"` so it returns `false` for the letter `d` and `true` for all others, resulting in an array that doesn't include the letter `d`.

The callback to `filter` is passed three arguments, in order: the element itself, the index of the element, and the whole array.

You can create more complex conditions than this example, as complex as you need.

### Remove an element from an array with a `for` loop and `push`

A final method to remove an element from an array without mutating the original array is by using the `push` method.

With these simple steps:

1. Create an empty array
2. Loop through the original array
3. Push to the empty array the elements you want to keep

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

const arrayWithoutB = [];

for (let i = 0; i < arrayOfLetters.length; i++) {
    if (arrayOfLetters[i] !== 'b') {
        arrayWithoutH.push(arrayOfLetters[i]);
    }
}

// arrayOfLetters is unchanged
console.log(arrayOfLetters); // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(arrayWithoutB); // ['a', 'c', 'd', 'e', 'f']
```

The condition of the `if` statement can check both the index (`i`) and the value of the element for more complex statements.

### Remove the first element of an array with destructuring and the rest operator

Array destructuring and the rest operator are two concepts that are a bit confusing.

I suggest this article that covers [how to destructure an array](https://www.freecodecamp.org/news/array-and-object-destructuring-in-javascript/) if you want to go deeper on this topic.

You can remove the first element using destructuring – let's say of an array named `arr` – and create a new array named `newArr` in this way: `const [ , ...newarr] = arr;`.

Now, let's see a practical example on how to use destructuring and the rest operator.

```
const arrayOfFruits = ['olive', 'apricot', 'cherry', 'peach', 'plum', 'mango'];

const [ , ...arrayOfCulinaryFruits] = arrayOfFruits;

// arrayOfFruits is unchanged
console.log(arrayOfFruits); // ['olive', 'apricot', 'cherry', 'peach', 'plum', 'mango']

console.log(arrayOfCulinaryFruits); // ['apricot', 'cherry', 'peach', 'plum', 'mango']
```

Putting a comma before the rest operator says to avoid the first element in the array, and all the others are copied in the `arrayOfCulinaryFruits` array.

## How to remove an element from an array while mutating the array

In some cases it might be appropriate to mutate the original array. In these cases you can also use one of the following mutating methods.

* `Array.prototype.pop()`
* `Array.prototype.shift()`
* `Array.prototype.splice()`

### Remove the last element of an array with `pop`

You can remove the last item of an array with `Array.prototype.pop()`.

If you have an array named `arr`, it looks like `arr.pop()`.

```javascript
const arrayOfNumbers = [1, 2, 3, 4];

const previousLastElementOfTheArray = arrayOfNumbers.pop();

console.log(arrayOfNumbers); // [1, 2, 3]

console.log(previousLastElementOfTheArray); // 4
```

The `pop` method is used on the array, and it changes the array by removing the last item of the array.

The `pop` method also returns the removed element.

### Remove the first element of an array with `shift`

The `shift` method can be used on an array to remove the first element of an array.

If you have an array named `arr` it can be used in this way: `arr.shift()`.

```javascript
const arrayOfNumbers = [1, 2, 3, 4];

const previousFirstElementOfTheArray = arrayOfNumbers.shift();

console.log(arrayOfNumbers); // [2, 3, 4]

console.log(previousFirstElementOfTheArray); // 1
```

The `shift` method removes the first item of the array.

It also returns the removed element.

### Remove an element at any index with `splice`

You can remove the element at any index by using the `splice` method.

If you have an array named `arr` it can be used in this way to remove an element at any index: `arr.splice(n, 1)`, with `n` being the index of the element to remove.

```javascript
const arrayOfNumbers = [1, 2, 3, 4];

const previousSecondElementOfTheArray = arrayOfNumbers.splice(1, 1);

console.log(arrayOfNumbers); // [1, 3, 4]

console.log(previousSecondElementOfTheArray); // [2]
```

The `splice` method can accept many arguments.

To remove an element at any index, you need to give `splice` two arguments: the first argument is the index of the element to remove, the second argument is the number of elements to remove.

So, if you have an array named `arr`, in order to remove an element at index 4, the way to use the `splice` method would be: `arr.splice(4, 1)`.

The `splice` method then returns an array containing the removed elements.

## Conclusion

There are many different ways to do the same thing in JavaScript. 

In this article you have learned nine different methods to remove an element from an array. Six of them do not mutate the original array, and three of them do. 

You will probably use all of them at one point or an other, and maybe you will learn even more methods to do this same thing.

Have fun!

