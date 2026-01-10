---
title: How to Sort an Array of Objects by Property Name in JavaScript
subtitle: ''
author: Kaushal Joshi
co_authors: []
series: null
date: '2024-01-29T14:45:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-array-of-objects-by-property-name-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/How-to-sort-an-array-of-objects-by-object-s-property-name-in-JavaScript.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In this tutorial, you''ll learn about one of the most common operations
  you''ll perform while working with JavaScript: sorting an array of objects by property
  name.

  Basic Array Concepts

  Let''s review some basic JavaScript concepts before delving deeper ...'
---

In this tutorial, you'll learn about one of the most common operations you'll perform while working with JavaScript: sorting an array of objects by property name.

## Basic Array Concepts

Let's review some basic JavaScript concepts before delving deeper into the subject so that you have the background info you need.

### JavaScript arrays and array of objects

Arrays are one of the fundamental building blocks of any programming language. They're the simplest data structure, yet they're so powerful that they're the underlying data structure of many apps we use today.

```javascript
const arr = ["apple", "banana", "orange", "mango"]
```

The most typical use of arrays is to send data from one machine to another. By machine, I mean a client, server, database server, and so on. Such data is often a collection of similar records grouped in an array. Every record is represented by an object, which is an array element.

These arrays are called arrays of objects. Here's an example of an array of objects in JavaScript:

```javascript
const response = [
    {
        id: 1,
        name: "John",
        age: 41
    },
    {
        id: 2,
        name: "Zack",
        age: 35
    },
    {
        id: 3, 
        name: "Peter",
        age: 47
    }
]
```

As you can see, it's simply an array. And every element in the array is an object. Hence the name, **array of objects**.

You can handle an array of objects like any other array and use built-in array functions. But there are some situations where using built-in functions is not feasible, and you must make certain modifications to achieve the objective.

### Keys in JavaScript objects

Objects in JavaScript are collections of key-value pairs, with each key identifying a specific value. Think of keys as the labels you assign to retrieve information from a dictionary. For instance:

```javascript
const person = {
    id: 1,
    name: "John",
    age: 41
};
```

In the above example, `id`, `name`, and `age` are keys whereas '1', 'John', and '25' are their corresponding values. When we talk about sorting an array of objects based on a key, we are referring to sorting the array elements based on the values associated with a specific property within each object.

### Determining the data type of a property

Before sorting, it's crucial to understand the data type of the property you intend to use as the sorting key. JavaScript has different sorting rules for numeric and string values. Knowing the data type helps us choose the appropriate sorting method.

If you are unsure of the data type, you can either check the data type with the `typeof` operator or convert the type into your desired one.

```xml
// Checking if the type is as expected
if(typeof obj.name === "string") {
	// Do something
}

// Converting property's type
const string = String(obj.propertyName)
const number = Number(obj.propertyName)
```

## How to Sort an Array of Objects with a Specific Key from the Object

We need to know two things before sorting an array:

1. **Data Type:** Understand the data type of the value we want to sort.
    
2. **Sort Order:** Determine whether we want to sort in ascending or descending order.
    

We will cover various use cases to get a full picture of these concepts.

### How to sort an array based on numeric values

Let's start by sorting an array based on numeric values, specifically the age property. Our goal is to have the array elements (that is, objects) sorted in ascending order based on the `age` property. The built-in `sort()` method will be our tool of choice:

```javascript
response.sort((a, b) => a.age - b.age)
```

And that's it! Objects in the array are sorted by the `age` property. You can confirm this by logging the output in the console:

```javascript
[
  { id: 2, name: 'Zack', age: 35 },
  { id: 1, name: 'John', age: 41 },
  { id: 3, name: 'Peter', age: 47 }
]
```

If you want to sort in descending order, you just need to change the position of the variables inside the function.

```javascript
response.sort((a, b) => b.age - a.age)
```

Just like that, the array will be sorted in descending order of `age`.

```javascript
[
  { id: 3, name: 'Peter', age: 47 },
  { id: 1, name: 'John', age: 41 },
  { id: 2, name: 'Zack', age: 35 }
]
```

Sorting numbers in an array is easy – so now let's try something a little bit more difficult: sorting based on string values.

### How to sort an array based on string values

I struggled a lot in my initial days to perform this operation. Eventually, I found the easiest method to do it. Similar to the previous example, here we want to sort objects based on the string values.

We will use a built-in string function `localCompare()`. It is used for comparing strings based on language-sensitive ordering. Let's write the `sort()` function with the help of this function:

```javascript
response.sort((a, b) => a.name.localeCompare(b.name));
```

```javascript
[
  { id: 1, name: 'John', age: 41 },
  { id: 3, name: 'Peter', age: 47 },
  { id: 2, name: 'Zack', age: 35 }
]
```

As expected, array elements will be sorted based on the `name` property inside each object element.

Sorting in descending order is a no-brainer as well:

```javascript
response.sort((a, b) => b.name.localeCompare(a.name));
```

The output will be like the following:

```javascript
[
  { id: 2, name: 'Zack', age: 35 },
  { id: 3, name: 'Peter', age: 47 },
  { id: 1, name: 'John', age: 41 }
]
```

## Edge Cases to Consider

While sorting arrays of objects, it's essential to address potential edge cases.

### The key must be present in all objects

Ensure that the key used for sorting exists in all objects. Even if a single object is missing the key, the original array is returned unchanged. Here's how you can handle such a case:

```javascript
if (array.every(obj => 'age' in obj)) {
    array.sort((a, b) => a.age - b.age);
} else {
    console.error("Some objects lack the 'age' key. Sorting is not feasible.");
}
```

### Null or undefined values must not be present

The key you want to use for sorting shouldn't be `null` or `undefined`. You can pass an empty string instead of the key if it is a falsy value.

```javascript
array.sort((a, b) => (a.name || "").localeCompare(b.name || ""));
```

### All values must be strings for string comparisons

While sorting objects based on a particular key, if the key is supposed to be a string, then make sure that the key has the data type String in all cases. A workaround to avoid potential bugs is to convert the key into a string in the `sort()` function.

```javascript
array.sort((a, b) => String(a.name).localeCompare(String(b.name)));
```

### Local sensitivity

When dealing with string properties, consider language and case sensitivity. Provide appropriate locales and options information for `localeCompare()`.

```javascript
array.sort((a, b) => a.title.localeCompare(b.title, 'en', { sensitivity: 'accent' }));
```

## Wrapping up

Understanding array operations will increase the efficiency of your code and improve the performance of your app. In this article, you learned how to sort arrays of objects based on a key from inside the object.

I hope you found this article helpful. If you do, don't forget to share it with your friends so others can benefit from it. If you know a better method to sort arrays, let me know! I would love to learn.

I am most active on [Twitter (Now **X**)](https://twitter.com/clumsy_coder) if you want to say hi!

### Further readings

* [JavaScript sort() function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
    
* [Intl.Collator object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
    
* [JavaScript localeCompare() function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)
    

Until next time, happy coding :)
