---
title: 'JavaScript Array Slice vs Splice: the Difference Explained with Cake'
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-08-11T16:03:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-slice-vs-splice-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/dilyara-garifullina-I48gnI1Qs5o-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "This title could have been \"how not to get confused between JavaScript's\
  \ splice and slice,\" because I can never remember the difference between the two.\
  \ \nSo I am hoping this trick will help both me and you in the future:\nS (p) lice\
  \ = Slice + (p) => S..."
---

This title could have been "how not to get confused between JavaScript's splice and slice," because I can never remember the difference between the two. 

So I am hoping this trick will help both me and you in the future:


```
S (p) lice = Slice + (p) => Slice + in (p) lace
```
 

## Array.prototype.slice()
Array.prototype.slice() is used to slice an array from the `start` point to the `end` point, excluding the `end`. 

As the name suggests, it is used to slice elements out of an array. But unlike slicing a cake, slicing an array does not cut the actual array, but keeps it unmodified (infinite cake!). 

```JS 
arr.slice(start, [end])

```

Rules
1. A new array is returned and the original array is unmodified. 
2. If `end` is omitted, end becomes the end (last element) of the array. 
3. If `start` is -ve, the elements are counted from the end.


```JS
const infiniteCake = ['?','?','?','?','?','?']

let myPieceOfCake = infiniteCake.slice(0,1) // ['?']
let yourDoublePieceOfCake = infiniteCake.slice(0,2) // (2) ["?", "?"]
console.log(infiniteCake) //['?','?','?','?','?','?']

```
As you see, `inifinteCake` is unmodified.


## Array.prototype.splice()
Splice does operations **in place**, which means it modifies the exisiting array. 

In addition to removing elements, splice is also used to add elements. Splice is the real world cake "slice":

```JS
arr.splice(start, [deleteCount, itemToInsert1, itemToInsert2, ...])
```

Rules
1. Operations are performed in place. 
2. An array is returned with the deleted items. 
3. If `start` is -ve, the elements are counted from the end.
4. If `deleteCount`is omitted,the elements until the end of the array are removed.
5. If items to insert such as `itemToInsert1` are omitted, elements are only removed.


```JS
const cake = ['?','?','?','?','?','?'];
let myPieceOfCake = cake.splice(0, 1) // ["?"]
console.log(cake) // (5) ["?", "?", "?", "?", "?"]

let yourDoublePieceOfCake = cake.splice(0,2) //(2) ["?", "?"]
console.log(cake) //(3) ["?", "?", "?"]

```
Here, `cake` is modified and reduces in size. 


## Code Examples
```JS
const myArray  = [1,2,3,4,5,6,7] 

console.log(myArray.slice(0))       // [ 1, 2, 3, 4, 5, 6, 7 ]
console.log(myArray.slice(0, 1))    // [ 1 ]
console.log(myArray.slice(1))       // [ 2, 3, 4, 5, 6, 7 ]
console.log(myArray.slice(5))       // [ 6, 7 ]
console.log(myArray.slice(-1))      // [ 7 ]
console.log(myArray)                // [ 1, 2, 3, 4, 5, 6, 7 ]



const secondArray = [10, 20, 30, 40, 50]

console.log(secondArray.splice(0, 1))   // [ 10 ] : deletes 1 element starting at index 0
console.log(secondArray.splice(-2, 1))  // [ 40 ] : deletes 1 element starting at index end-2 
console.log(secondArray)                // [ 20, 30, 50 ]
console.log(secondArray.splice(0))      // [ 20, 30, 50 ] : deletes all elements starting at index 0
console.log(secondArray)                // []
console.log(secondArray.splice(2, 0, 60, 70)) // [] : deletes 0 elements starting at index 2 (doesn't exist so defaults to 0) and then inserts 60, 70
console.log(secondArray)                // [60, 70]
```


## TL;DR
Use `splice` if the original array needs to be modified, or elements need to be added.

Use `slice` for removing elements if the original array should not be modified.

****

Interested in more tutorials and JSBytes from me? [Sign up for my newsletter.](https://tinyletter.com/shrutikapoor) or [follow me on Twitter](https://twitter.com/shrutikapoor08)


