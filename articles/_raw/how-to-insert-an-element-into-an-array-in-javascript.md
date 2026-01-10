---
title: Push into an Array in JavaScript – How to Insert an Element into an Array in
  JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-18T14:09:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-insert-an-element-into-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--1-.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The array datatype is one of the most commonly used datatypes when you''re
  working with an ordered list of values.

  Each value is referred to as an element with a unique id. It stores elements of
  various datatypes that you can access through a single v...'
---

The array datatype is one of the most commonly used datatypes when you're working with an ordered list of values.

Each value is referred to as an element with a unique `id`. It stores elements of various datatypes that you can access through a single variable.

In practice, an array could hold a list of users, and we might need to add an element(s) to the array after the last element, before the first element, or at any specified point in our array.

This article will show you how to insert an element into an array using JavaScript. In case you're in a hurry, here are the methods we'll be discussing in depth in this article:

```bash
// Add to the start of an array
Array.unshift(element);

// Add to the end of an array
Array.push(element);

// Add to a specified location
Array.splice(start_position, 0, new_element...);

// Add with concat method without mutating original array
let newArray = [].concat(Array, element);
```

* When you want to add an element to the end of your array, use `push()`.
    
* If you need to add an element to the beginning of your array, use `unshift()`.
    
* If you want to add an element to a particular location of your array, use `splice()`.
    
* And finally, when you want to maintain your original array, you can use the `concat()` method.
    

## How to push to the start of an array with the `unshift()` method

In JavaScript, you use the `unshift()` method to add one or more elements to the beginning of an array and it returns the array's length after the new elements have been added.

If we have an array of countries and want to add a country before "Nigeria," which is currently at the first index `0`, we can do so with the `unshift()` method, as shown below:

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

countries.unshift("Kenya");

console.log(countries); // ["Kenya","Nigeria","Ghana","Rwanda"]
```

As we said, we can also add more than one element using the `unshift()` method:

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

countries.unshift("South Africa", "Mali", "Kenya");

console.log(countries); // ["South Africa","Mali","Kenya","Nigeria","Ghana","Rwanda"]
```

In our explanation of the `unshift()` method, we also stated that it returns the length of the new array, which is true:

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

let countriesLength = countries.unshift("South Africa", "Mali", "Kenya");

console.log(countriesLength); // 6
```

## How to push to the end of an array with the `push()` method

The `push()` method is similar to the `unshift()` method as it adds an element to the end of an array rather than the beginning. It returns the length of the new array and, like the `unshift()` method, can be used to add more than one element.

Let's try the same example again, but this time add them to the end of the array using the `push()` method:

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

countries.push("Kenya");

console.log(countries); // ["Nigeria","Ghana","Rwanda","Kenya"]

countries.push("South Africa", "Mali");

console.log(countries); // ["Nigeria","Ghana","Rwanda","Kenya","South Africa","Mali"]
```

And like we said, we can use it to get the length of the new array:

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

let countriesLength = countries.push("Kenya");

console.log(countriesLength); // 4
```

## How to push to a specified location in an array with the `splice()` method

So far, we've only seen how to add an element to the beginning or end of an array. But you might wonder how to add an element to a specific location within an array. Well, you can do it with the `splice()` method.

The `splice()` method is a general-purpose method for changing the contents of an array by removing, replacing, or adding elements in specified positions of the array. This section will cover how to use this method to add an element to a specific location.

For example, consider the following array of countries, which contains three elements (countries) arranged alphabetically:

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];
```

Suppose we want to add "Kenya," which, according to alphabetical order, should be placed in the second position, index `1` (after Ghana and before Nigeria). In that case, we will use the `splice()` method with the following syntax:

```bash
Array.splice(start_position, 0, new_element...);
```

* The `start_position` specifies the index of where we want the new elements to be inserted in the array. If there are multiple elements, it specifies where the elements inserted will start.
    
* If we want to add to the array, we set the second argument to zero (`0`), instructing the `splice()` method not to delete any array elements.
    
* The following parameter(s) or element(s) may be more than one, as these are the elements we want to add to the array at the specified position.
    

For example, let's place "Kenya" after "Ghana" in our countries array:

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];

countries.splice(1, 0, 'Kenya');

console.log(countries); // ["Ghana","Kenya","Nigeria","Rwanda"]
```

![](https://paper-attachments.dropbox.com/s_8F843EE332F48B356BFA84EB69212DF653EB2859C5739E7748DB9362133DCFB7_1658069550677_illustration.jpg align="left")

Just as we did for other methods, we can also add more than one element:

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];

countries.splice(1, 0, 'Kenya', 'Mali');

console.log(countries); // ["Ghana","Kenya","Mali","Nigeria","Rwanda"]
```

Note that the previous methods returned the length of the new array, but the splice method changes the original array. It does not remove any elements, so it returns an empty array.

You can read more on [Slice vs. Splice in JavaScript and when to use them in this detailed article](https://joelolawanle.com/posts/slice-vs-splice-javascript-understanding-differences-use).

## How to push elements into an array with the `concat()` method

We can use the `concat()` method to add elements to an array without mutating or altering the original array. Instead, creating a new one is a better method if we don't want the original array to be affected.

We can use this method to add elements to both the beginning and end of the array based on where we place the elements:

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];

let newCountries = [].concat("Mali", countries, "Kenya");

console.log(newCountries); // ["Mali","Ghana","Nigeria","Rwanda","Kenya"]
```

The `concat()` method also allows us to join together two (or more) arrays into a single new array:

```bash
const africanCountries = ["Ghana", "Nigeria", "Rwanda"];
const europeanCountries = ["Germany", "France", "spain"];

let countries = [].concat(africanCountries, europeanCountries);

console.log(countries); // ["Ghana","Nigeria","Rwanda","Germany","France","spain"]
```

## Wrapping up

In this article, we learned various ways to push elements into an array to the start, end, or any position using the `splice()` method.

We also learned that the `concat()` method allows us to push elements without altering the original array.

Use any method that fits your needs.

Happy coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents) written by me. Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
