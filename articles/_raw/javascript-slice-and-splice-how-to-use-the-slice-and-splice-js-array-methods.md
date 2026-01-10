---
title: How to Use the slice() and splice() JavaScript Array Methods
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-13T19:17:33.000Z'
originalURL: https://freecodecamp.org/news/javascript-slice-and-splice-how-to-use-the-slice-and-splice-js-array-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "When you are first learning JavaScript, it might be difficult to know the\
  \ difference between the slice() and splice() array methods. \nIn this article,\
  \ I will walk you through how to use the slice() and splice() array methods using\
  \ code examples. \nHow..."
---

When you are first learning JavaScript, it might be difficult to know the difference between the `slice()` and `splice()` array methods. 

In this article, I will walk you through how to use the `slice()` and `splice()` array methods using code examples. 

## How to use the slice() JavaScript array method

The `slice()` method can be used to create a copy of an array or return a portion of an array. It is important to note that the `slice()` method does not alter the original array but instead creates a shallow copy. 

Here is the basic syntax:

```js
slice(optional start parameter, optional end parameter)
```

Let's take a look at some examples to better understand how the `slice()` method works. 

## How to use the slice() JavaScript method without the start and end parameters

In this first example, I have created a list of cities from around the world.

```js
const cities = ["Tokyo","Cairo","Los Angeles","Paris","Seattle"];
```

I can use the `slice()` method to create a shallow copy of that array.

```js
cities.slice()
```

When I `console.log` the result, then I will see all of the elements from my `cities` array copied into this new array.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.28.42-PM.png)

## How to use the slice() JavaScript method using the start parameter

You can use the optional start parameter to set a starting position for selecting elements from the array. It is important to remember that arrays are zero based indexed. 

In this example, we will set the start position at index 2 which will select the last three cities in the array and return them in a new array. 

```js
const newCityArr = cities.slice(2);

console.log(newCityArr)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.34.10-PM.png)

The original array was not modified as we can see here in this example. 

```js
const cities = ["Tokyo","Cairo","Los Angeles","Paris","Seattle"];

const newCityArr = cities.slice(2);

console.log("Original: ", cities)
console.log("New: ", newCityArr)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.36.59-PM.png)

You can also use negative indexes which will start extracting elements from the end of the array. 

In this example, we will set the start position at -2 which will select the last two cities in the array and return them in a new array. 

```js
const newCityArr = cities.slice(-2);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.43.34-PM.png)

If the start parameter is greater than the last index of the array, then an empty array will be returned.

```js
const newCityArr = cities.slice(5);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.45.41-PM.png)

## How to use the slice() JavaScript method using the start and end parameters

If an end position is specified, then the `slice()` method will extract elements from the start position up to the end position. The end position will not be included in the extracted elements for the new array. 

In this example, we have specified a start index of 2 and end index of 4. The new returned array will only include the cities at index 2 and 3 because the end position is not included in the extracted elements. 

```js
const cities = ["Tokyo","Cairo","Los Angeles","Paris","Seattle"];

const newCityArr = cities.slice(2,4);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.51.30-PM.png)

## How to use the splice() JavaScript array method

Unlike the `slice()` method, the `splice()` method will change the contents of the original array. The `splice()` method is used to add or remove elements of an existing array and the return value will be the removed items from the array.

If nothing was removed from the array, then the return value will just be an empty array.

Here is the basic syntax.

```js
splice(start, optional delete count, optional items to add)
```

In this example, we have an array of food items.

```js
const food = ['pizza', 'cake', 'salad', 'cookie'];
```

If we wanted to add another food item to the array at index 1, then we can use the following code:

```js
food.splice(1,0,"burrito")
```

The first number is the starting index, and the second number is the delete count. Since we are not deleting any items, our delete count is zero.

This is what the result would look like in the console.

```js
const food = ['pizza', 'cake', 'salad', 'cookie'];

food.splice(1,0,"burrito")

console.log(food)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-13-at-12.09.13-AM.png)

If we  `console.log(food.splice(1,0,"burrito"))`, then we would get back an empty array because nothing was removed from our array.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-13-at-12.11.34-AM.png)

In this next example, we want to remove "salad" from the array.  We can use the start and delete parameters to accomplish this.

```js
food.splice(2,1)
```

The number 2 is the start position and the number 1 represents the delete count. Since salad is at index 2 then it will be removed from the array. 

This is what our array looks like now:

```js
const food = ['pizza', 'cake', 'salad', 'cookie'];

food.splice(2,1)
console.log(food)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-13-at-12.21.53-AM.png)

## Conclusion

The `slice` and `splice` array methods might seem similar to each other, but there are a few key differences.

The `slice()` method can be used to create a copy of an array or return a portion of an array. It is important to note that the `slice()` method does not alter the original array but instead creates a shallow copy.

Here is the basic syntax:

```js
slice(optional start parameter, optional end parameter)
```

Unlike the `slice()` method, the `splice()` method will change the contents of the original array. The `splice()` method is used to add or remove elements of an existing array and the return value will be the removed items from the array.

If nothing was removed from the array, then the return value will just be an empty array.

Here is the basic syntax:

```js
splice(start, optional delete count, optional items to add)
```

I hope you enjoyed this JavaScript article and best of luck on your developer journey. 

