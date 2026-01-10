---
title: How Types Work in TypeScript – Explained with JavaScript + TypeScript Code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-20T21:05:51.000Z'
originalURL: https://freecodecamp.org/news/basic-typescript-types
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'TypeScript is a superset of JavaScript that introduces static typing to
  JavaScript. TypeScript''s enhanced type safety and code maintainability empower
  developers to write code more confidently.

  A fundamental aspect of TypeScript''s static typing syste...'
---

TypeScript is a superset of JavaScript that introduces static typing to JavaScript. TypeScript's enhanced type safety and code maintainability empower developers to write code more confidently.

A fundamental aspect of TypeScript's static typing system is its support for basic types. These provide a foundation for defining the shape and behavior of data within TypeScript applications. 

In this comprehensive guide, we'll explore TypeScript's basic types by comparing them with their JavaScript counterparts. I'll also clarify the differences and advantages offered by TypeScript's static typing features.

You can get all the JavaScript and TypeScript code from [here](https://github.com/dotslashbit/fcc-article-resources/tree/main/ts-basic-types).

## Table Of Contents

* [Understanding Type Annotations](#heading-understanding-type-annotations)
* [JavaScript vs TypeScript Basic Types](#heading-javascript-vs-typescript-basic-types)
* [Conclusion](#heading-conclusion)

## Understanding Type Annotations

Type annotation in TypeScript involves explicitly specifying the data type of variables, function parameters, and return values. This annotation enhances code clarity and enables TypeScript's static type checking to catch errors during compilation. This improves code quality and maintainability.

In TypeScript, type annotations are written using a colon (`:`) followed by the desired type. Let's explore how type annotations are applied in TypeScript basic types:

## JavaScript vs TypeScript Basic Types

### Boolean

Here's how you'd write a boolean in JavaScript:

```javascript
let isDone = false;
console.log("isDone:", isDone); // Output: isDone: false
if (!isDone) {
    console.log("Task is not done yet.");
}

```

In JavaScript, a boolean variable `isDone` is declared and initialized with the value `false`. The condition `!isDone` checks if `isDone` is `false`, and if true, logs a message indicating that the task is not done yet.

And here's how you'd declare a boolean in TypeScript:

```typescript
let isDone: boolean = false;
console.log("isDone:", isDone); // Output: isDone: false
if (!isDone) {
    console.log("Task is not done yet.");
}

```

In TypeScript, the same boolean variable `isDone` is declared with explicit type annotation `: boolean` indicating that it can only hold boolean values. The behavior and output remain the same as JavaScript.

### Number

Here's how you declare a number in JavaScript:

```javascript
let count = 42;
let totalPrice = 24.99;
let quantity = 10;
console.log("count:", count); // Output: count: 42
console.log("totalPrice:", totalPrice); // Output: totalPrice: 24.99
console.log("quantity:", quantity); // Output: quantity: 10

```

In JavaScript, numeric variables `count`, `totalPrice`, and `quantity` are declared and initialized with numeric values. Each value represents a different numeric type (integer, floating-point, integer respectively).

And in TypeScript:

```typescript
let count: number = 42;
let totalPrice: number = 24.99;
let quantity: number = 10;
console.log("count:", count); // Output: count: 42
console.log("totalPrice:", totalPrice); // Output: totalPrice: 24.99
console.log("quantity:", quantity); // Output: quantity: 10

```

In TypeScript, type annotations `: number` are added to each variable declaration, explicitly specifying that they can only hold numeric values. This provides clarity and type safety similar to JavaScript.

### String

Here's how you write a string in JavaScript:

```javascript
let message = "Hello, JavaScript!";
let firstName = "John";
let lastName = "Doe";
console.log("message:", message); // Output: message: Hello, JavaScript!
console.log("firstName:", firstName); // Output: firstName: John
console.log("lastName:", lastName); // Output: lastName: Doe

```

In JavaScript, string variables `message`, `firstName`, and `lastName` are declared and initialized with string values.

And here's how you do it in TypeScript:

```typescript
let message: string = "Hello, TypeScript!";
let firstName: string = "John";
let lastName: string = "Doe";
console.log("message:", message); // Output: message: Hello, TypeScript!
console.log("firstName:", firstName); // Output: firstName: John
console.log("lastName:", lastName); // Output: lastName: Doe

```

In TypeScript, type annotations `: string` are added to each variable declaration, explicitly specifying that they can only hold string values. This enhances code readability and maintainability.

### Array

Here's how you can declare an array in JavaScript:

```javascript
let numbers = [1, 2, 3, 4, 5];
let fruits = ["apple", "banana", "orange"];
console.log("numbers:", numbers); // Output: numbers: [1, 2, 3, 4, 5]
console.log("fruits:", fruits); // Output: fruits: ["apple", "banana", "orange"]

```

In JavaScript, arrays `numbers` and `fruits` are declared and initialized with numeric and string values respectively.

Here's how you do it in TypeScript:

```typescript
let numbers: number[] = [1, 2, 3, 4, 5];
let fruits: string[] = ["apple", "banana", "orange"];
console.log("numbers:", numbers); // Output: numbers: [1, 2, 3, 4, 5]
console.log("fruits:", fruits); // Output: fruits: ["apple", "banana", "orange"]

```

In TypeScript, type annotations are added to declare arrays with specific element types (`: number[]` and `: string[]`), ensuring that only numeric or string values can be stored in `numbers` and `fruits` arrays respectively.

### Tuple

Here's how you'd write a tuple in TypeScript:

```typescript
let person: [string, number] = ["John", 30];
console.log("person:", person); // Output: person: ["John", 30]

```

In TypeScript, a tuple `person` is declared with explicit type annotation `[string, number]`, indicating that it should contain a string followed by a number. It stores a person's name and age.

And here's the JavaScript simulation:

```javascript
// JavaScript does not have built-in support for tuples, but we can use arrays.
let person = ["John", 30];
console.log("person:", person); // Output: person: ["John", 30]

```

In JavaScript, since tuples are not supported, arrays are often used as a workaround to simulate tuple-like behavior. The array `person` stores a person's name and age, similar to the TypeScript example.

### Enum

Here's how you'd declare an enum in TypeScript:

```typescript
enum Direction {
    Up,
    Down,
    Left,
    Right
}
let direction: Direction = Direction.Up;
console.log("direction:", direction); // Output: direction: 0

```

In TypeScript, an enum `Direction` is declared with named constants `Up`, `Down`, `Left`, and `Right`, which are assigned numeric values starting from 0 by default. `direction` variable is assigned the value `Direction.Up`.

And here's the JavaScript simulation:

```javascript
// JavaScript does not have built-in support for enums, but we can use objects or constants.
const Direction = {
    Up: 0,
    Down: 1,
    Left: 2,
    Right: 3
};
let direction = Direction.Up;
console.log("direction:", direction); // Output: direction: 0

```

In JavaScript, enums are not natively supported, so objects or constants are often used to simulate enum-like behavior. Here, `Direction` object contains named constants mapped to numeric values, and `direction` variable is assigned the value of `Direction.Up`, similar to the TypeScript example.

## Conclusion

TypeScript's basic types provide significant advantages over traditional JavaScript in terms of type safety, clarity, and maintainability. 

By introducing explicit type annotations and additional type constructs such as tuples and enums, TypeScript empowers developers to write more robust and error-free code. 

Understanding the differences between JavaScript and TypeScript basic types is essential for harnessing the full potential of TypeScript's static typing capabilities in modern web development.

If you have any feedback, then you can DM me on [Twitter](https://twitter.com/introvertedbot) or [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).

