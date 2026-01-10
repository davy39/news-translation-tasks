---
title: TypeScript Generics – Use Case and Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-07T20:49:10.000Z'
originalURL: https://freecodecamp.org/news/typescript-generics-use-case-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-hitarth-jadhav-220357.jpg
tags:
- name: generics
  slug: generics
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Aman Kalra

  In this tutorial, you''ll learn the basics of generics in TypeScript. We''ll discuss
  how to use them and when they''re useful in your code.

  Use Case for Generics

  Let''s start with a simple example, where you want to print the value of an ar...'
---

By Aman Kalra

In this tutorial, you'll learn the basics of generics in TypeScript. We'll discuss how to use them and when they're useful in your code.

## Use Case for Generics

Let's start with a simple example, where you want to print the value of an argument passed:

```typescript
function printData(data: number) {
    console.log("data: ", data);
}

printData(2);
```

Now, let's suppose you want to make `printData` a more generic function, where you can pass any type of argument to it like: **number**/ **string**/ **boolean**. So, you might think to follow an approach like below:

```typescript
function printData(data: number | string | boolean) {
    console.log("data: ", data);
}

printData(2);
printData("hello");
printData(true);
```

But in the future, you might want to print an array of numbers using the same function. In that case the types will increase and it will become cumbersome to maintain all those different types.

This is when **Generics** come into the picture.

## How Generics Work in TS

Generics are like variables – to be precise, type variables – that store the type (for example number, string, boolean) as a value.

So, you can solve the problem we discussed above with generics as shown below:

```typescript
function printData<T>(data: T) {
    console.log("data: ", data);
}

printData(2);
printData("hello");
printData(true);
```

In the above example `printData-generics.ts`, there is a slight difference in syntax:

1. You use a type variable inside angular brackets after the function name `<T>`
2. You then assign the type variable to the parameter `data: T`

Let's explore these differences a bit more.

To use generics, you need to use angular brackets and then specify a type variable inside them. Developers generally use `T`, `X` and `Y`. But it can be anything depending upon your preference.

You can then assign the same variable name as the type to the parameter of the function.

Now, whatever argument you pass to the function, it gets inferred and there's no need to hardcode the type anywhere.

Even if you pass an array of numbers or an object to the `printData` function, everything will be displayed properly without TS complaining:

```typescript
function printData<T>(data: T) {
    console.log("data: ", data);
}

printData(2);
printData("hello");
printData(true);
printData([1, 2, 3, 4, 5, 6]);
printData([1, 2, 3, "hi"]);
printData({ name: "Ram", rollNo: 1 });
```

Let's see another example:

```typescript
function printData<X,Y>(data1: X, data2: Y) {
    console.log("Output is: ", data1, data2);
}

printData("Hello", "World");
printData(123, ["Hi", 123]);
```

In above example, we passed 2 arguments to `printData` and used `X` and `Y` to denote the types for both the parameters. `X` refers to 1st value of the argument and `Y` refers to 2nd value of the argument.

Here as well, the types of `data1` and `data2` are not specified explicitly because TypeScript handles the type inference with the help of generics.

### How to Use Generics with Interfaces

You can even use generics with interfaces. Let's see how that works with the help of a code snippet:

```typescript
interface UserData<X,Y> {
    name: X;
    rollNo: Y;
}

const user: UserData<string, number> = {
    name: "Ram",
    rollNo: 1
}
```

In above snippet, `<string, number>` are passed to the interface `UserData`. In this way, `UserData` becomes a reusable interface in which any data type can be assigned depending upon the use case.

Here in this example, `name` and `rollNo` will always be `string` and `number`, respectively. But this example was to showcase how you can use generics with interfaces in TS.

### Thanks for reading!

If you found this article useful, do share it with your friends and colleagues.

