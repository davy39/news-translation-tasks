---
title: How TypeScript Generics Work – Explained with Examples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-27T13:45:54.000Z'
originalURL: https://freecodecamp.org/news/how-typescript-generics-work
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post.png
tags:
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'TypeScript, with its powerful type system, offers a feature called Generics,
  which enables developers to write reusable and type-safe code. Generics allow you
  to create components that can work over a variety of types rather than a single
  one.

  This a...'
---

TypeScript, with its powerful type system, offers a feature called Generics, which enables developers to write reusable and type-safe code. Generics allow you to create components that can work over a variety of types rather than a single one.

This article delves into TypeScript Generics, providing thorough explanations and code examples to illustrate their usage and benefits.

You can get all the source code from [here](https://github.com/dotslashbit/fcc-article-resources/blob/main/ts-generics/index.ts).

## Table of Contents

* [What are Generics](#heading-what-are-generics)
* [TypeScript Generics Use Cases](https://www.freecodecamp.org/news/how-typescript-generics-work/typescript-generics-use-cases)
* [Conclusion](#heading-conclusion)

## What are Generics?

Generics in TypeScript enable writing code that can work with a variety of data types while maintaining type safety. They allow the creation of reusable components, functions, and data structures without sacrificing type checking.

Generics are represented by type parameters, which act as placeholders for types. These parameters are specified within angle brackets (`<>`) and can be used throughout the code to define types of variables, function parameters, return types, and more.

## TypeScript Generics Use Cases

### Basic Usage of Generics

Let's start with a simple example of a generic function:

```typescript
function identity<T>(arg: T): T {
    return arg;
}

let output = identity<string>("hello");
console.log(output); // Output: hello

```

In this example, `identity` is a generic function that takes a type parameter `T`. The parameter `arg` is of type `T`, and the return type of the function is also `T`. When calling `identity<string>("hello")`, the type parameter `T` is inferred as `string`, ensuring type safety.

### How to Use Generic Classes

Generics are not limited to functions – they can also be used with classes. Consider the following example of a generic `Box` class:

```typescript
class Box<T> {
    private value: T;

    constructor(value: T) {
        this.value = value;
    }

    getValue(): T {
        return this.value;
    }
}

let box = new Box<number>(42);
console.log(box.getValue()); // Output: 42

```

Here, `Box` is a generic class with a type parameter `T`. The constructor takes a value of type `T`, and the `getValue` method returns a value of type `T`. When creating an instance of `Box<number>`, it can only store and return values of type `number`.

### How to Apply Constraints on Generics

Sometimes, you may want to restrict the types that can be used with generics. TypeScript allows you to specify constraints on type parameters using the `extends` keyword. Let's see an example:

```typescript
interface Lengthwise {
    length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
    console.log(arg.length);
    return arg;
}

let result = loggingIdentity("hello");
console.log(result); // Output: hello

```

In this example, the `loggingIdentity` function takes a type parameter `T` that must extend the `Lengthwise` interface, which ensures that `arg` has a `length` property. This constraint allows accessing the `length` property without causing a compilation error.

### How to Use Generics with Interfaces

Generics can also be used with interfaces to create flexible and reusable definitions. Consider the following example:

```typescript
interface Pair<T, U> {
    first: T;
    second: U;
}

let pair: Pair<number, string> = { first: 1, second: "two" };
console.log(pair); // Output: { first: 1, second: "two" }

```

Here, `Pair` is an interface with two type parameters `T` and `U`, representing the types of the `first` and `second` properties respectively. When declaring `pair` as `Pair<number, string>`, it enforces that the `first` property must be a number, and the `second` property must be a string.

### How to Use Generic Functions with an Array

```typescript
function reverse<T>(array: T[]): T[] {
    return array.reverse();
}

let numbers: number[] = [1, 2, 3, 4, 5];
let reversedNumbers: number[] = reverse(numbers);
console.log(reversedNumbers); // Output: [5, 4, 3, 2, 1]

```

In this example, the `reverse` function takes an array of type `T` and returns a reversed array of the same type. By using generics, the function can work with arrays of any type, ensuring type safety.

### How to Use Generic Constraints with `keyof`

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let person = { name: "John", age: 30, city: "New York" };
let age: number = getProperty(person, "age");
console.log(age); // Output: 30

```

Here, the `getProperty` function takes an object of type `T` and a key of type `K`, where `K` extends the keys of `T`. It then returns the corresponding property value from the object. This example demonstrates how to use generics with `keyof` to enforce type safety when accessing object properties.

### How to Use Generic Utility Functions

```typescript
function toArray<T>(value: T): T[] {
    return [value];
}

let numberArray: number[] = toArray(42);
console.log(numberArray); // Output: [42]

let stringArray: string[] = toArray("hello");
console.log(stringArray); // Output: ["hello"]

```

The `toArray` function converts a single value of type `T` into an array containing that value. This simple utility function showcases how generics can be used to create reusable code that adapts to different data types effortlessly.

### How to Use Generic Interfaces with A Function

```typescript
interface Transformer<T, U> {
    (input: T): U;
}

function uppercase(input: string): string {
    return input.toUpperCase();
}

let transform: Transformer<string, string> = uppercase;
console.log(transform("hello")); // Output: HELLO

```

In this example, we define a `Transformer` interface with two type parameters `T` and `U`, representing the input and output types respectively. We then declare a function `uppercase` and assign it to a variable `transform` of type `Transformer<string, string>`. This demonstrates how generics can be used to define flexible interfaces for functions.

## Conclusion

Whether it's functions, classes, or interfaces, generics provide a robust mechanism for building scalable and maintainable TypeScript applications. Understanding and mastering generics can significantly enhance your ability to write efficient and error-free code.

If you have any feedback, DM me on [Twitter](https://twitter.com/introvertedbot) or [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/).

