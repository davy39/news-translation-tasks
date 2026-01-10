---
title: Sparse Arrays vs Dense Arrays in JavaScript — Explained with Examples
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-03-08T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/sparse-and-dense-arrays-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/UwzSmIVOo.jpeg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'I had a really interesting bug recently that, at first glance, completely
  stumped me.I saw I had an array that was empty. But the length was 31.

  Wait, what?

  What are dense arrays?

  Dense arrays are the most well known type of Array. They are the "norm...'
---

I had a really interesting bug recently that, at first glance, completely stumped me.  
I saw I had an array that was empty. But the length was 31.

Wait, what?

## What are dense arrays?

Dense arrays are the most well known type of `Array`. They are the "normal" arrays most are familiar with.

A dense array is an array where the elements are all sequential starting at index 0.

In this instance, the length property of an array accurately specifies the number of elements in the array.

```javascript
let array = [1, 2, 3, 4, 5]  
array.length // Returns 5

```

## What are sparse arrays?

A sparse array is one in which the elements are not sequential, and they don't always start at 0.

They are essentially `Array`s with "holes", or gaps in the sequence of their indices.

So an example would be:

```javascript
let array = [];
array[100] = "Holes now exist";
array.length // 101, but only 1 element
```

Normally, the length property of an `Array` accurately returns the number of elements in the array, but in sparse arrays they don't. If the array is sparse, the value of the length property is greater than the number of elements.

# Why can `Array`s be sparse?

`Array`s under the hood in JavaScript are `Object`s. Their keys are numbers, and their values are the elements.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599682873904/ByiIRL0vT.png)

```javascript
let array = [];
array[20] = {};
array[100] = {};
array[19] = {};
alert(array.length); // Logs 101

```

The `length` property on an `Array` takes the last element's index and adds one. So if you have an array with holes between index 0 through 100, and an element at index 101, the `length` will return 101, as it's the last index + 1.

The above happens regardless of how many elements are in the `Array`.

The spec specifically details this behavior if you [want to read more on the ECMAScript spec here.](http://www.ecma-international.org/ecma-262/5.1/#sec-15.4.5.2)

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599597131632/RiZ59nGj3.png)

# How do you get a sparse array?

You have seen some ways already, but there are more:

## Use the `Array` object

```javascript
let array = new Array(10); // array initialized with no elements
array.length // 10

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-53.png)

## Insert a key/value at a certain index

```javascript
array[1000] = 0; // Assignment adds one element 
array.length // But .length returns 1001

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-54.png)

## Use the `delete` operator

```javascript
let array = [1, 2, 3, 4, 5]
delete array[0]
array.length // .length returns 5

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-55.png)

## Initialize an `Array` with holes

```javascript
[,,,,] // You have created an array with nothing but holes
[1,2,3,4,,5] // Oh no, you mistyped a comma and entered a hole between 4 and 5!

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-56.png)

## Browser implementation differences

The browser you are on (as well as the version) represents sparse array's holes differently.

Chrome displays this the best (in my opinion) and shows `empty`.  


![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599687555328/dX4b8NGcj.png)

The newest version of Firefox (80.0.1 at the time of witting) shows it like so:  


![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599598536385/vfQk4COPj.png)

## Conclusion

The final solution of the bug I introduced at the beginning is to just check that the element isn't falsy before using it.  Something like:

```javascript
let array = [,,,,]
for(let i = 0; i < array.length; i++){
    if (array[i]) {
        console.log(array[i])
    }
}

```

Because the holes are falsy, it won't do the logic you are trying on any holes you have in the `Array`.

So why did my browser show it as empty?

I was using Safari and it showed nothing for the holes. So I  logged out the `Array`'s length which was 31, and when I logged out the contents it just showed me an empty array! Pretty confusing at first glance.

