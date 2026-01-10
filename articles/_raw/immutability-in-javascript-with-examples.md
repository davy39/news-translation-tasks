---
title: Immutability in JavaScript – Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-12T23:21:23.000Z'
originalURL: https://freecodecamp.org/news/immutability-in-javascript-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/thumbnail.jpg
tags:
- name: immutability
  slug: immutability
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Deborah Kurata

  We often hear the terms: immutable and immutability. But what do they mean, and,
  as developers, why should we care?

  Immutable basically means something that cannot be changed. In programming, immutable
  is used to describe a value th...'
---

By Deborah Kurata

We often hear the terms: **immutable** and **immutability**. But what do they mean, and, as developers, why should we care?

Immutable basically means something that cannot be changed. In programming, immutable is used to describe a value that cannot be changed after it's been set.

But, most programs require creating, updating, and deleting data. So why would we ever want to work with data that can't be changed?

In this tutorial, we'll look at immutability of primitives, arrays, and objects with JavaScript examples. And I'll explain why immutability is important for programming.

You can also watch the associated video here:

%[https://youtu.be/DBZESPS-5mQ]

And here is a JavaScript example (which you can [also view on Stackblitz](https://stackblitz.com/edit/immutability-deborahk?file=index.js)):

```js
// Import stylesheets
import './style.css';

// Write JavaScript code!
const appDiv = document.getElementById('app');
appDiv.innerHTML = `<h1>Open the console to see results</h1>`;

class Person {
  //_name = "Nee";
  //_name = ["Nee", "Ra"];
  _name = { first: "Nee", middle: "L" };
  
  get name() {
    return this._name;
  }
  
  set name(value) {
    console.log('In setter', value);
    this._name = value;
  }
}

let p = new Person();
//p.name = "Ra";                        // Setter executes
//p.name.push("Lee");                   // Setter doesn't execute
//p.name = [...p.name, "Lee"];          // Setter executes
//p.name.middle = "Lee";                // Setter doesn't execute
p.name = { ...p.name, middle: "Lee" };  // Setter executes

```

Let's start with primitives.

## Primitives in JavaScript: Naturally Immutable

In JavaScript, primitives, like strings and numbers, are immutable by default. This means that once a primitive value is created, it can't be changed. Wait a minute, you might think – I change primitive variable values all the time!

Well, it might seem like you're modifying a value. But that's not actually the case. Here's an example.

```javascript
let greet = "Hello";
greet += ", World";  
console.log(greet);
```

The first line of this code creates the string `Hello` and assigns it to the `greet` variable. The second line appends `, World` to that string. So it looks like we're changing the `greet` string. But JavaScript does not change the string. Rather, it creates a new string.

Let's look at an illustration. Here we have a `greet` variable assigned to the `Hello` string.

![Image](https://lh7-us.googleusercontent.com/9-7QkMgYxQdlMMreWAQywiB3yy4k7xi8WkfWNeP0dbDANyNCpUVulbPOsVD06EDGLuZKH4MK_8prwlIqqV0eRVI8BrH3VV8hE7nlxH2zsVg6Fw0HSqe_TN26vGgm_99pmlWKaqGqFU1xy6t0DjpRzMg)
_Figure 1. The code creates the string `Hello` and assigns it to the `greet` variable._

When the code appends text, JavaScript creates a new string. It then assigns the `greet` variable to this new string. The original `Hello` string is not modified.

![Image](https://lh7-us.googleusercontent.com/T_KgVb_6Cy-rBP7bnxQUaosHDaFbvfh2MY8XNrEvsM0rJDgx7Qih1sH6OYL9qBLqlBIM3bNiKQ1jJKeM5UwQSurqkUr-MBztWjkFZbxtYgCL_V8PjfBhO4mYd_4lzym2xwtXjPpZ8p9cHzcCVGNuHXg)
_Figure 2. Appending text creates a new string and assigns it to the `greet` variable._

So strings and other primitives are immutable by default in JavaScript.

How about arrays?

## JavaScript Arrays are Mutable

In JavaScript, arrays are mutable by default. This means that the array can be altered after the array is created. We can modify it "in place", adding, removing, or changing elements.

Let's look at an example.

```javascript
let ages = [42, 22, 35];
ages.push(8);  
console.log(ages);
```

The first line of code defines an array and assigns a variable to that array. But in JavaScript, the variable doesn't store the array. It stores the memory address where the array resides, as illustrated in Figure 3 here:

![Image](https://lh7-us.googleusercontent.com/v7dmTur_H7PetKYQkvHGbjYPKWaZhkevFhgHO8gJxufnHN24p_h4gkAupNbqX9SqvLhjw8KFuuwSwWTMJocMX4t-D0r0vwRr6mvf-2G--SwSSuBi1mfqC31kUFzudwCB1qUJnqGPM7YDsWozqg0ZfDg)
_Figure 3. A variable doesn't store an array – it stores the memory address of the array._

In the second line of code in the prior example, we use the `push` method to modify the original array. In this case, we add 8 to the end of the array. This is shown in Figure 4:

![Image](https://lh7-us.googleusercontent.com/TCWSxZMXMh5Oz06HncXSt5OapytcOfTRKdwCAAM3mac6XFndE6p_VpMkjkQAvUqxlTdpLwQaRorROsXCIcif8KJPtQmGKY7rbSQVad_QXAJ04AIyfY3Gn28cAeO2wHPSNcv4MN0KueD1AjmhKgrzYoM)
_Figure 4. A JavaScript array is changed "in place"._

Notice that the memory address of the array doesn't change, but the array itself does change. So the array value is mutable.

This mutability provides flexibility. But mutability can lead to unintended side-effects, especially in larger applications or those involving concurrent operations.

And mutability has issues. Say you have code in a setter that should execute when the array is changed. Or you're working with a framework, such as Angular, that provides change detection. Or you're using a state library, such as Redux, that requires immutability.

As we saw in this example our array is changed...but our `ages` variable didn't actually change, since it's referencing the memory address. So the setter or change detection or state management might not be aware that the array was changed.

To avoid these pitfalls of mutability, we, as JavaScript developers, often use patterns or methods that do not alter the original array but instead return a new array. This embraces immutability.

## How to Embrace Immutability with Arrays

Let's look at an alternate example:

```javascript
let ages = [42, 22, 35];
ages = [...ages, 8];  
console.log(ages);
```

In this code, we start with the same array. But when we add an element, we use the JavaScript spread operator. The spread operator makes a copy of the existing array at a new address by "spreading" the existing array.

We then add the new element to that copy. We also reassign the `ages` variable to the address of the new array (Figure 5).

![Image](https://lh7-us.googleusercontent.com/3zRss4le02LtJWuvVAodTOv6lGDWGBkoZ6LvluPSojWfkEDWU3n6R-PAktzUMd92Ua9sNzc-kuFis6u2xOFsUkKCjxR8SdPY4-4x43hP8Wp13CbA5XHE-aXBtq2VjMPGdMXtE_XaZbDTuiWzRHGGYaQ)
_Figure 5. Using the spread operator, we create a new array at a new address and assign it to the `ages` variable._

Notice that the original array is not changed. By using the spread operator, we achieve immutability.

In addition to the spread operator, many of the array methods also create a new array and therefore treat an array as immutable. Other array methods modify the array in place and are therefore mutable. Here are some examples.

* `Map` creates a new array from the existing array, mapping each element using a function we provide. It leaves the original array unchanged. So it supports immutability.

```javascript
ages.map(x => x + 1);
```

* `Push` modifies the original array in place, mutating the array.

```javascript
ages.push(8);
```

* `Filter` creates a new array with items matching the defined criteria. It leaves the original array unchanged.

```javascript
ages.filter(x => x > 21);
```

* `Sort` sorts the array elements in place, thereby mutating the array.

```javascript
ages.sort();
```

* `Slice` creates a new array from a portion of an existing array. Here we copy the original array elements starting at index 1 through index 3 to a new array.

```javascript
ages.slice(1, 3);
```

* `Splice` changes the contents of an array in place, adding, removing, or replacing existing elements. In this example, the code starts replacing elements at index 2, only replaces 1 element, and replaces the element with "18".

```javascript
ages.splice(2, 1, 18);
```

So even though by default arrays are mutable, we can use immutability techniques to better manage our arrays.

What about objects?

## The Mutable Nature of JavaScript Objects

Objects in JavaScript are also mutable by default. We can add or delete properties and change property values "in place" after an object is created.

```javascript
let p = {name:"Nee", age: 30};
p.age = 31;
console.log(p);
```

The first line of this code example declares a person object with name and age properties. When a variable is assigned to that object, the variable doesn't store the object, but rather a memory address where the object resides.

![Image](https://lh7-us.googleusercontent.com/-z8t2kPHCLlKG5y2D8p37azjtcc-a-Na_JarvtrXgTHbcsCjpZd3pYPxSdA5NAtTfNNllVXevr71jfV6X9UymACPkr-WyeQAwi-Auc32G4q9H8WEOlm-S4c_CbEzV5FhLIjq8btJAsUr35m5wclTmtI)
_Figure 6. A variable doesn't store an object. Rather, it stores the memory address of the object._

The second line of code in the prior example modifies the value of an object property, changing the age. This modification directly alters the original person object.

![Image](https://lh7-us.googleusercontent.com/1OBvr491s67DqK4M3poTs31M5yjB2tQK9vo9QiWpLSSB-iSkC1qNKoypVC-Zhiitn56jMgfP_khoSNneCoPNJa9tp71Z3OSvgCl-jO15yaqGejOSa0WhL6VoapluQxjnxZ8SVluWcoe203m9t2nSdmU)
_Figure 7. A JavaScript object is changed "in place"._

Notice that the memory address of the object doesn't change, but the object itself changes. This is similar to array mutability, and that makes sense because arrays in JavaScript are basically objects.

Mutability provides flexibility but can lead to complex bugs if not carefully managed.

And as with an array, mutability has issues. Say you have code in a setter that should execute when the object changes. Or you're working with a framework, such as Angular, that provides change detection. Or you're using a state library, such as Redux, that requires immutability.

In this example, our object changed but our `p` variable didn't actually change, since it's referencing the memory address. So the setter or change detection or state management may not see that the object was changed.

It's often better to handle objects in an immutable manner. JavaScript provides features to aid with immutable objects.

## Immutability with Objects

Here is an alternate example:

```javascript
let p = {name:"Nee", age: 30};
p = {...p, age: 31};
console.log(p);
```

We start with the same object. But instead of changing an object's property value directly, we again use the spread operator. The spread operator makes a copy of the object by spreading it into a new object at a new address. We update the property in that new object. We then reassign the `p` variable to the address of the new object.

![Image](https://lh7-us.googleusercontent.com/_q_uW95z9GHcZi2SgUUpI1ht1P7dWqY4xF0z8P8cphnmMb_EkUwogdYQaGf1ZaqfKLxKtbWtzUDRZMtVcv8CiK3Zog5c1Wv6187x5gCeaTi8g_27x2HBRXucBbRHI9huMzh08VbE3CpM30mSlrLUiQc)
_Figure 8. Using the spread operator, we create a new object at a new address and assign it to the `p` variable._

Notice that the original object is not changed. By using the spread operator, we achieve immutability.

So we've seen how primitives are immutable by default. And that arrays and objects are mutable, but we can work with them in an immutable way.

Nice! But why do we care?

## Why Is Immutability Important?

There are several reasons that immutability is important to our everyday coding.

* Once an immutable value is set, it isn't changed. Rather a new value is created. This makes the value predictable and consistent throughout the code. So it aids in managing state throughout the application. Plus immutability is a key principle in state management frameworks, such as Redux.
* Code becomes simpler and less error-prone when data structures don't change unexpectedly. This also simplifies debugging and maintenance.
* Embracing immutability is in line with functional programming principles, leading to fewer side effects and more predictable code.

## **Wrapping Up**

Immutability is a fundamental concept in programming. An immutable value is a value that can not be changed after it has been created. 

This concept is important to functional programming and state management. It's a valuable concept, especially when dealing with concurrency and large, complex codebases.

To see these concepts with animations, check out the video here:

%[https://youtu.be/DBZESPS-5mQ]

Or try my stackblitz link: [https://stackblitz.com/edit/immutability-deborahk](https://stackblitz.com/edit/immutability-deborahk). Be sure to fork my project to try out your own changes.

While JavaScript objects and arrays are mutable by default, adopting an immutable approach to handling them can lead to cleaner, more reliable, and easier-to-maintain code.

  


  


  


  


  


  


  


  


  


  


  

