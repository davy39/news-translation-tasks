---
title: JavaScript Destructuring and the Spread Operator – Explained with Example Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T21:46:07.000Z'
originalURL: https://freecodecamp.org/news/javascript-destructuring-and-spread-operator-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Cheers--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nishant Kumar

  JavaScript has two awesome data structures that help you write clean and efficient
  code. But handling them can get messy sometimes.

  In this blog, I am going to show you how to handle destructuring in arrays and objects
  in JavaScript....'
---

By Nishant Kumar

JavaScript has two awesome data structures that help you write clean and efficient code. But handling them can get messy sometimes.

In this blog, I am going to show you how to handle destructuring in arrays and objects in JavaScript. We'll also learn how to use the spread operator as well.

Let's dive in.

## What is Array Destructuring in JavaScript?

Let's say we have an array that contains five numbers, like this:

```
let array1 = [1, 2, 3, 4, 5]
```

To get the elements from the array, we can do something like getting the number according to its indexes:

```
array1[0];
array1[1];
array1[2];
array1[3];
array1[4];

```

But this method is old and clunky, and there is a better way to do it – using array destructuring. It looks like this:

```
let [ indexOne, indexTwo, indexThree, indexFour, indexFive ] = array1;
```

Both methods above will yield the same result:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-105209.png)

Now, we have five elements in the array, and we print those.  But what if we want to skip one element in between?

```
let [ indexOne, indexTwo, , indexFour, indexFive ] = array1;
```

Here, we have skipped `indexThird`, and there's an empty space between indexTwo and indexFour.

```
let [ indexOne, indexTwo, , indexFour, indexFive ] = array1;

console.log(indexOne);
console.log(indexTwo)
console.log(indexFour)
console.log(indexFive)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-105709.png)

You can see that we are not getting the third element because we have set it as empty.

## What is Object Destructuring in JavaScript?

This destructuring works well with objects too. Let me give you an example.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 200,
    height: '20 meters',
    weight: '70 KG'
}
```

Let's say we want the name, salary, and weight from this object to be printed out in the console.

```
console.log(object.name)
console.log(object.salary)
console.log(object.weight)
```

We can get them using the keys, which are name, salary, and weight.

But this code becomes difficult to understand sometimes. That's when destructuring comes in handy:

```
let { name, salary, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

And now, we can just log name, salary, and weight instead of using that old method.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-111356.png)

We can also use destructuring to set default values if the value is not present in the object.

```
let object = {
    name: "Nishant",
    age: 24, 
    height: '20 meters',
    weight: '70 KG'
}

let { name, salary, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

Here, we have name and weight present in the object, but not the salary:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-111659.png)

We will get an undefined value for the salary. 

To correct that issue, we can set default values when we are destructuring the object.

```
let object = {
    name: "Nishant",
    age: 24, 
    height: '20 meters',
    weight: '70 KG'
}

let { name, salary = 200, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-111907.png)

You can see that we get 200 as the Salary. This only works when we don't have that key in the object, and we want to set a default value.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

let { name, salary = 200, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

Add salary in the object, and you will get 300 as the salary.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-112128.png)

## How to Use Object Destructuring with Functions

Let's say we have a function that prints all the data in the array to the console.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

function printData(){
    
}

printData(object)

```

We are passing the object as a parameter in the function when it gets called:

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

function printData(object){
    console.log(object)
}

printData(object)
```

Normally, we would do something like this – passing the object and logging it in the console.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-115047.png)

But again, we can do the same using destructuring.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

function printData({name, age, salary, height, weight}){
    console.log(name, age, salary, height, weight)
}

printData(object)
```

Here, we are destructuring the object into name, age, salary, height and weight in the function parameters and we print everything on the same line. 

You can see how destructuring makes it so much easier to understand.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-115329.png)
_Printing object data using Destructuring_

Let's look at one last example. 

```
function sample(a, b) {
    return [a + b, a * b]
}

let example = sample(2, 5);
console.log(example)
```

We have a function here which accepts two numbers. It returns an array adding them and multiplying them and logs them into the console.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-120108.png)

Let's use destructuring here instead.

We can destructure it into addition and multiplication variables like this:

```
let [addition, multiplication] = sample(2, 5);
console.log(addition)
console.log(multiplication)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-120325.png)

And in the output, you can see we get the _addition_ and _multiplication_ of both numbers.

## What is the Spread Operator in JavaScript?

Spread means spreading or expanding. And the spread operator in JavaScript is denoted by three dots. 

This spread operator has many different uses. Let's see them one by one.

### Spread Operator Examples

Let's say we have two arrays and we want to merge them. 

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [6, 7, 8, 9, 10]

let array3 = array1.concat(array2);
console.log(array3)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-112601.png)

We are getting the combination of both arrays, which are array1 and array2.

But there is an easier way to do this:

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [6, 7, 8, 9, 10]

let array3 = [...array1, ...array2]
console.log(array3)
```

In this case, we are using the spread operator to merge both arrays.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-113020.png)

And you can see, we will get the same output.

Let's imagine another use case where we have to insert _array1_ between the elements of _array2_.

For example, we want to insert _array2_ between the second and third element of _array1_.

 So, how do we do that? We can do something like this:

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [6, 7, ...array1, 8, 9, 10]

console.log(array2);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-113502.png)

And you can see, we get the array1 elements between 7 and 8.

Now, let's merge two objects together using the spread operator.

```
let object1 = {
    firstName: "Nishant",
    age: 24, 
    salary: 300,
}

let object2 = {
    lastName: "Kumar",
    height: '20 meters',
    weight: '70 KG'
}
```

We have two objects here. One contains firstName, age, and salary. The second one contains lastName, height, and weight. 

Let's merge them together.

```
let object1 = {
    firstName: "Nishant",
    age: 24, 
    salary: 300,
}

let object2 = {
    lastName: "Kumar",
    height: '20 meters',
    weight: '70 KG'
}

let object3 = {...object1, ...object2}
console.log(object3);
```

We have now merged both objects using the spread operator, and we've logged the value in the console.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-114101.png)
_Combination of previous objects_

You can see that we are getting the combination of both objects.

Lastly, we can also copy one array into another using the spread operator. Let me show you how it works:

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [...array1]
console.log(array2);
```

Here, we are copying _array1_ into _array2_ using the spread operator.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-120757.png)

We are logging _array2_ in the console, and we are getting the items of _array1_.

## Conclusion

That's all, folks! In this article, we learned about array and object destructuring and the spread operator.

You can also watch my Youtube video on [Array and Object Destructuring and the Spread Operator](https://youtu.be/QvQ4o0K9_g0) if you want to supplement your learning.

> Happy Learning.

