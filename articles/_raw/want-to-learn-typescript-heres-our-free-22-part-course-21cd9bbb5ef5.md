---
title: Learn TypeScript for free with this interactive Scrimba course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T14:13:21.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-typescript-heres-our-free-22-part-course-21cd9bbb5ef5
coverImage: null
tags:
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  Click on the image to go to the Scrimba course

  TypeScript has been gaining a lot of popularity amongst JavaScript developers in
  the last few years. And it’s no wonder, as TypeScript code tends to be less error-prone,
  more readabl...'
---

By Per Harald Borgen

[![TypeScript course banner](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-04-at-06.35.08.png)](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article)*Click on the image to go to the Scrimba course*

TypeScript has been gaining a lot of popularity amongst JavaScript developers in the last few years. And it’s no wonder, as TypeScript code tends to be less error-prone, more readable and easier to maintain.

So we’ve partnered up with the eminent online instructor [Dylan C. Israel](https://medium.com/u/7f21f9c02e5b) and created a [free TypeScript course on Scrimba.](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article) The course contains 22 lessons and is **for people who already know JavaScript** but who want a quick intro to TypeScript.

Take the course [for free here.](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article)

Now let’s have a look at each of the lectures in the course.

### Part #1: Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*_I4oz78IStdFL_PMkHNBpA.png)

In the introductory screencast, Dylan gives an overview of why you should learn TypeScript, and how the course is laid out. He also tells you a little bit about himself, so that you are familiar with him before jumping into the coding stuff.

### Part #2: Variable types

Compile time type-checking is one of the most important features of TypeScript. It lets us catch errors related to the types of data at compile time. This lesson explains the data types available in TypeScript.

```ts
let firstName: string;

let age: number;

let isMarried: boolean;

```

You can see how we have types attached to all the variables. If we try to put a string value in place of a number type variable, TypeScript will catch it at compile time.

### Part #3: Multiple types

In TypeScript, we keep a single type for a variable but that is not possible every time. So, instead, TypeScript provides us with the`any` type. This means we can assign multiple types of values to one variable.

```ts
let myVariable: any = 'Hello World';  
myVariable = 10;  
myVariable = false;

```

Above, we’ve declared `myVariable` with `any` type. First we assigned it a string, next a number, and finally a boolean. This is possible because of the `any` type.

### Part #4: Sub types

Sub types are used when we are unaware of the value of the variable. TypeScript provides us with two sub types: `null` and `undefined`. This lesson explains when we should use either of those.

```ts
let myVariable: number = undefined;

```

The variable `myVariable` has been assigned the value of `undefined` because, at this point in time, we don’t know what it is going to be. We can also use `null` here.

### Part #5: Implicit vs explicit typing

Part 5 talks about the difference between implicit and explicit typing. In the examples above, we saw explicit types where we set the type of the variable. Implicit typing, on other hand, is performed by the compiler without us stating the variable type.

```ts
let myVariable = 'Hello World';

```

In this example, we have not assigned any type to the variable. We can check the type of this variable using the`typeof` function. This will show that `myVariable` is of `string` type because the compiler took care of the typing.

### Part #6: Checking types

In this lesson we’ll learn how we can check the type of a variable, and catch any error or perform any operation. It uses an example in which we test if our variable is of type `Bear` (where `Bear` is a `class`). If we want to check the type of our variable, we can use the`instanceof` method.

```ts
import { Bear } from 'somefile.ts';  
let bear = new Bear(3);  
if (bear instanceof Bear) {  
   //perform some operation  
}

```

### Part #7: Type assertions

Type assertion means we can cast a variable to any particular type, and we tell TypeScript to handle that variable using that type. Let’s try to understand it with an example:

```ts
let variable1: any = 'Hello World';  
if ((variable1 as string).length) {  
   //perform some operation  
}

```

`variable1` has the type of `any` . But, if we want to check its length, it will produce an error until we tell TypeScript to handle it as a string. This lesson explains more details about this concept.

### Part #8: Arrays

This part of the course explains TypeScript arrays. In JavaScript, when we assign values to an array, we can put in different types of items. But, with TypeScript, we can declare an array with types as well.

```ts
let array1: number[] = [1, 2, 3, 4, 5];

```

In the above example, we declared an array of numbers by assigning it the `number` type. Now TypeScript will make sure the array contains only numbers.

### Part #9: Tuples

Sometimes we need to store multiple types of values in one collection. Arrays will not serve in this case. TypeScript gives us the data type of tuples. These are used to store values of multiple types.

```ts
let tuple_name = [10, 'Hello World'];

```

This example shows that we can have data items of number **and** string types in one collection. This lesson explains the concept of tuples in more detail.

### Part #10: Enums

In this lesson, we will learn about enums in TypeScript. Enums are used to define a set of named constants which can be used to document intent or to create a set of different cases.

```ts
**enum** Direction {   
   Up = "UP",       
   Down = "DOWN",       
   Left = "LEFT",      
   Right = "RIGHT"   
}

```

Here is a basic example of how enums are declared, and how different properties are created inside them. The rest of the details are explained in this section of the course.

### Part #11: Object

In JavaScript, objects have a pretty major role in how language has been defined and has evolved. This lesson talks about objects in TypeScript — how to declare an object, and which kinds of values can fit inside the object type.

### Part #12: Parameters

Using TypeScript, we can also assign types to the parameters of a function. In this section of the course, Dylan explains how we can add types to parameters. This is a very useful way to handle errors regarding data type in a function.

```ts
const multiply = (num1: number, num2: number) => {   
   return num1 * num2;  
}

```

We have declared a function `multiply` which takes two parameters and returns the value from multiplying them. We added a type of `number` to both the parameters so that no other value except a number can be passed to them.

### Part #13: Return types

Like parameters, we can also add type-checking to the return value of a function. This way we can make sure that the return value from a function has an expected type. This part of the course explains the concept in detail.

```ts
const multiply = (num1: number, num2: number): number => {   
   return num1 * num2;  
}

```

We have added a `return` type of `number` to the function. Now, if we return anything except a `number`, it will show us an error.

### Part #14: Custom types

In TypeScript, we can create a custom type using the keyword of `type.` We can then type-check objects on the basis of that type.

```ts
type person = {firstName: string};

const example3: person = {firstName: 'Dollan'};

```

This feature is almost deprecated in TypeScript, so you should rather use `interface` or `class` for this purpose. However, it’s important that you get to know it, as you might come across custom types when you start to dive into TS code.

### Part #15: Interfaces

In TypeScript, the core focus is on type-checking which enforces the use of a particular type. Interfaces are a way of naming these types. It’s basically a group of related methods and properties that describe an object. This part of the course explains how to create and use interfaces.

```ts
interface Person {  
   firstName: string,   
   lastName: string,  
   age: number  
}

```

In the example above, we have an interface `Person` which has some typed properties. Note that we don’t initiate data in interfaces, but rather define the types that the parameters will have.

### Part #16: Barrels

A barrel is a way to rollup exports from multiple modules into a single module. A barrel is, itself, a module, which is exporting multiple modules from one file. This means that a user has to import just one module instead of all the modules separately.

```ts
// Without barrel  
import { Foo } from '../demo/foo';  
import { Bar } from '../demo/bar';  
import { Baz } from '../demo/baz';`

```

Instead of using these multiple lines separately to import these modules, we can create a barrel. The barrel would export all these modules and we import only that barrel.

```
// demo/barrel.ts export * from './foo'; 
// re-export all of its exportsexport * from './bar'; 
// re-export all of its exportsexport * from './baz'; 
// re-export all of its exports

```

We can simply create a TypeScript file and export the modules from their respective file. We can then import this barrel wherever we need it.

```ts
import { Foo, Bar, Baz } from '../demo'; // demo/barrel.ts

```

### Part #17: Models

When using interfaces, we often face a number of problems. For example, interfaces can’t seem to enforce anything coming from the server side, and they can't keep the default value. To solve this issue, we use the concept of models classes. These act as an interface, and also may have default values and methods added to them.

### Part #18: Intersection types

In this section, we’ll talk about intersection types. These are the ways we can use multiple types to a single entity or class. Sometimes we need to use multiple types to map one entity and, at that time, this feature comes in very handy.

```ts
import { FastFood, ItalianFood, HealthyFood} from ‘./interfaces’;  
let food1: FastFood | HealthyFood;  
let food2: ItalianFood;  
let food3: FastFood;  
let food4: FastFood & ItalianFood;

```

In the example above, we have three interfaces and we are creating different objects from them. For example, `food1` is going to be either `FastFood` **or** `HealthyFood`. Similarly, `food4` is going to be `FastFood` **as well as** `ItalianFood`.

### Part #19: Generics

In short, generics is a way to create reusable components which can work on a variety of data types rather than a single one.

The concept of generics is actually not available in JavaScript so far, but is widely used in popular object-oriented languages such as C# or Java. In this lesson, we’ll learn how to use generics in TypeScript, and look at its key benefits.

### Part #20: Access modifiers

The idea of access modifiers is relatively new in the arena of JavaScript and TypeScript, but they have been available in other object-oriented languages for a long time. Access modifiers control the accessibility of the members of a class.

In TypeScript, there are two access modifiers: public and private. Every member of a class defaults to public until you declare it otherwise.

```ts
class Customer {  
   customerId: number;  
   public companyName: string;  
   private address: string;  
}

```

`customerId` is a default public member, so it’s always available to the outside world. We have specifically declared `companyName` as`public`, so it will also be available outside of class. `address` is marked as `private,` therefore it won’t be accessible outside the class.

### Part #21: Local setup

In this lesson, we’ll learn the steps to install and run TypeScript on local computers. Those steps generally involve installing Node and TypeScript, and then compiling “.ts” files.

![Click the image to get to the course](https://cdn-media-1.freecodecamp.org/images/1*UYc7PRwJOGev2v0n5qQJuA.png)

_Click the image to get to the course._

### Part #22: TSLint and — great job!

Yay! You’ve completed the course. In the last part of the video, Dylan will give some tips on how to take this learning further and improve the code we write today.

In this lesson, he also covers how you can use the amazing TSLint. This tool helps you write better production level code using best practices and conventions. It comes up with some basic settings which you can modify to meet your needs.

#### So go ahead and take [this free course today!](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrototypescript_launch_article)_

