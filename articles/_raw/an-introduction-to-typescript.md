---
title: How to Use TypeScript – Beginner-Friendly TS Tutorial
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-03-29T01:28:31.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-hitarth-jadhav-220357.jpg
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'Hi everyone! In this article we''ll talk about what TypeScript is, why
  is it cool, and how can you use it.

  Table of Contents


  Intro


  About Types


  Strings


  Numbers


  Booleans


  Undefined


  Null


  Objects


  Arrays


  Functions




  What''s the Deal with Types and...'
---

Hi everyone! In this article we'll talk about what TypeScript is, why is it cool, and how can you use it.

## Table of Contents

* [Intro](#heading-intro)
    
* [About Types](#heading-about-types)
    
    * [Strings](#heading-strings)
        
    * [Numbers](#heading-numbers)
        
    * [Booleans](#heading-booleans)
        
    * [Undefined](#heading-undefined)
        
    * [Null](#heading-null)
        
    * [Objects](#heading-objects)
        
    * [Arrays](#heading-arrays)
        
    * [Functions](#heading-functions)
        
* [What's the Deal with Types and JavaScript?](#heading-whats-the-deal-with-types-and-javascript)
    
* [In Comes TypeScript](#heading-in-comes-typescript)
    
* [TypeScript Basics](#heading-typescript-basics)
    
    * [Types by Inference](#heading-types-by-inference)
        
    * [Declaring Types](#heading-declaring-types)
        
        * [Interfaces](#heading-interfaces)
            
        * [Conditionals](#heading-conditionals)
            
        * [Unions](#heading-unions)
            
        * [Typing Functions](#heading-typing-functions)
            
        * [Typing Arrays](#heading-typing-arrays)
            
* [TypeScript's Compiler](#heading-typescripts-compiler)
    
* [How to Create a Typescript Project](#heading-how-to-create-a-typescript-project)
    
    * [A Comment About Libraries](#heading-a-comment-about-libraries)
        
* [Other Functionalities of TypeScript](#heading-other-functionalities-of-typescript)
    
* [Roundup](#heading-roundup)
    

# Intro

TypeScript is a **superset** of JavaScript. Superset means that it adds features on top of what JavaScript offers. TypeScript takes all the functionalities and structures JavaScript provides as a language, and adds a few things to that.

The main thing TypeScript provides is **static typing**. So to truly understand what this means, we first need to understand what types are. Let's get into that.

# About Types

In a programming language, types refer to the **kind or type of information** a given program stores. Information or data can be classified as different types depending on its content.

Programming languages usually have built in data types. In JavaScript, there are **six basic data types** which can be divided into **three main categories**:

* Primitive data types
    
* Composite data types
    
* Special data types
    

* String, Number, and Boolean are **primitive** data types.
    
* Object, Array, and Function (which are all types of objects) are **composite** data types.
    
* Whereas Undefined and Null are **special** data types.
    

**Primitive** data types can hold **only one value at a time**, whereas **composite** data types can hold **collections of values** and more complex entities.

Let's take a quick look at each of these data types.

## Strings

The string data type is used to represent textual data (that is, sequences of characters). Strings are created using single or double quotes surrounding one or more characters, as shown below:

```ts
let a = "Hi there!";
```

## Numbers

The number data type is used to represent positive or negative numbers with or without decimal place:

```ts
let a = 25;
```

The Number data type also includes some special values which are: `Infinity`, `-Infinity`, and `NaN`.

`Infinity` represents the mathematical Infinity ∞, which is greater than any number. `-Infinity` is the result of dividing a nonzero number by 0. While `NaN` represents a special Not-a-Number value. It is a result of an invalid or an undefined mathematical operation, like taking the square root of -1 or dividing 0 by 0, and so on.

## Booleans

The Boolean data type can hold only two values: `true` or `false`. It is typically used to store values like yes (true) or no (false), on (true) or off (false), and so on, as demonstrated below:

```ts
let areYouEnjoyingTheArticle = true;
```

## Undefined

The undefined data type can only have one value, the special value `undefined`. If a variable has been declared, but has not been assigned a value, it has the value undefined.

```ts
let a;

console.log(a); // Output: undefined
```

## Null

A null value means that there is no value. It is not equivalent to an empty string ("") or 0, it is simply nothing.

```ts
let thisIsEmpty = null;
```

## Objects

The object is a complex data type that allows you to store collections of data. An object contains **properties**, defined as a **key-value pair**.

A property key (name) is always a string, but the value can be any data type, like strings, numbers, booleans, or complex data types like arrays, functions, and other objects.

```ts
let car = {
  modal: "BMW X3",
  color: "white",
  doors: 5
};
```

## Arrays

An array is a type of object used for storing multiple values in a single variable. Each value (also called an element) in an array has a numeric position, known as its **index**, and it may contain data of any data type (numbers, strings, booleans, functions, objects, and even other arrays).

The array index starts from 0, so that the first array element is `arr[0]`.

```ts
let arr = ["I", "love", "freeCodeCamp"];

console.log(arr[2]); // Output: freeCodeCamp
```

## Functions

A function is a callable object that executes a block of code. You first declare the function and within it the code you'd like it to execute. And later on you just call the function whenever you want its code to execute.

Since functions are objects, it is possible to assign them to variables, as shown in the example below:

```ts
let greeting = function () {
  return "Hello World!";
};

console.log(greeting()); // Output: Hello World!
```

# What's the Deal with Types and JavaScript?

Now that we have a clear idea of what types are, we can start discussing how this works with JavaScript – and why something like TypeScript would even be needed in the first place.

The thing is that JavaScript is a **loosely typed and dynamic language**. This means that in JavaScript, variables are not directly associated with any particular value type, and any variable can be assigned (and re-assigned) values of all types.

See the following example:

```ts
let foo = 42; // foo is now a number
foo = "bar";  // foo is now a string
foo = true;   // foo is now a boolean
```

You can see how we can change the content and type of the variable with no problem at all.

This was done by design at the creation of JavaScript, since it was meant to be a scripting language friendly to both programmers and designers and used only to add functionality to websites.

But JavaScript grew a lot with the years and started to be used not only to add simple functionality to websites, but to build huge applications, too. And when building huge applications, dynamic types can lead to silly bugs in the code base.

Let's see this with a simple example. Say we have a function that receives three parameters and returns a string:

```ts
const personDescription = (name, city, age) =>
  `${name} lives in ${city}. he's ${age}. In 10 years he'll be ${age + 10}`;
```

If we call the function this way we get the correct output:

```ts
console.log(personDescription("Germán", "Buenos Aires", 29));
// Output: Germán lives in Buenos Aires. he's 29. In 10 years he'll be 39.
```

But if accidentally we pass the function the third parameter as a string, we get a wrong output:

```ts
console.log(personDescription("Germán", "Buenos Aires", "29"));
// output: Germán lives in Buenos Aires. he's 29. In 10 years he'll be **2910**.
```

JavaScript doesn't show an error because the program doesn't have a way of knowing what type of data the function should receive. It just takes the parameters we gave and performs the action we programmed, independently of the data type.

It's easy to make this error as a dev, specially when working with big code bases and being unfamiliar with parameters required by functions or APIs. And this is exactly what TypeScript comes to solve.

# In Comes TypeScript

TypeScript was launched in 2012. It was developed and is currently maintained by Microsoft.

In TypeScript, much like in other programming languages such as Java or C#, we need to declare a data type whenever we create a data structure.

By declaring its data type, we give the program information to later on evaluate if the values assigned to that data structure match the data types declared or not.

If there's a match, the program runs, and if not, we get an error. And these errors are very valuable, because as developers we can catch bugs earlier. ;)

Let's repeat the previous example but now with TypeScript.

In TypeScript, my function would look like this (see that it's exactly the same, only that besides each parameter I'm declaring its data type):

```ts
const personDescription = (name: string, city: string, age: number) =>
  `${name} lives in ${city}. he's ${age}. In 10 years he'll be ${age + 10}.`;
```

Now if I try to call the function with the wrong parameter data type, I get the following error output:

```ts
console.log(personDescription("Germán", "Buenos Aires", "29"));
// Error: TSError: ⨯ Unable to compile TypeScript: Argument of type 'string' is not assignable to parameter of type 'number'.
```

The beauty of TypeScript is that it's still as easy as JavaScript code, we only add the type declarations to it. That's why TypeScript is called a JavaScript superset, as TypeScript only **adds** certain features to JavaScript.

# TypeScript Basics

Let's take a look at TypeScript's syntax and learn how to work with it.

## Types by Inference

There are a few ways to declare types in TypeScript.

The first one we'll learn is **inference**, in which you don't declare a type at all, but TypeScript infers (guesses) it for you.

Say we declare a string variable like this:

```ts
let helloWorld = "Hello World";
```

If later on I try to reassign it to a number, I'll get the following error:

```ts
helloWorld = 20;
// Type 'number' is not assignable to type 'string'.ts(2322)
```

In creating a variable and assigning it to a particular value, TypeScript will use the value as its type.

As mentioned in the [TypeScript docs](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html):

> By understanding how JavaScript works, TypeScript can build a type-system that accepts JavaScript code but has types. This offers a type-system without needing to add extra characters to make types explicit in your code.

That’s how TypeScript "knows" that `helloWorld` is a string in the above example.

Although this is a nice feature that allows you to implement TypeScript without any extra code, it's much more readable and recommended to explicitly declare your types.

## Declaring Types

The syntax to declare types is quite simple: you just add a colon and its type to the right of whatever you're declaring.

For example, when declaring a variable:

```ts
let myName: string = "Germán";
```

If I try to reassign this to a number, I'll get the following error:

```ts
myName = 36; // Error: Type 'number' is not assignable to type 'string'.
```

### Interfaces

When working with **objects**, we have a different syntax for declaring types which is called an **interface**.

An interface looks a lot like a JavaScript object – but we use the interface keyword, we don't have an equal sign or commas, and besides each key we have its data type instead of its value.

Later on, we can declare this interface as the data type of any object:

```ts
interface myData {
  name: string;
  city: string;
  age: number;
}

let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: 29
};
```

Say again I pass the age as a string, I'll get the following error:

```ts
let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: "29" // Output: Type 'string' is not assignable to type 'number'.
};
```

### Conditionals

If for example I wanted to make a key conditional, allowing it to be present or not, we just need to add a question mark at the end of the key in the interface:

```ts
interface myData {
  name: string;
  city: string;
  age?: number;
}
```

### Unions

If I want a variable to be able to be assigned more than one different data type, I can declare so by using **unions** like this:

```ts
interface myData {
  name: string;
  city: string;
  age: number | string;
}

let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: "29" // I get no error now
};
```

### Typing Functions

When typing functions, we can type its parameters as well as its return value:

```ts
interface myData {
  name: string;
  city: string;
  age: number;
  printMsg: (message: string) => string;
}

let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: 29,
  printMsg: (message) => message
};

console.log(myData.printMsg("Hola!"));
```

### Typing Arrays

For typing arrays the syntax is the following:

```ts
let numbersArray: number[] = [1, 2, 3]; // We only accept numbers in this array
let numbersAndStringsArray: (number | string)[] = [1, "two", 3]; // Here we accept numbers and strings.
```

**Tuples** are arrays with fixed size and types for each position. They can be built like this:

```ts
let skill: [string, number];
skill = ["Programming", 5];
```

# TypeScript's Compiler

The way TypeScript checks the types we've declared is through its **compiler**. A compiler is a program that converts instructions into a machine-code or lower-level form so that they can be read and executed by a computer.

Every time we run our TypeScript file, TypeScript compiles our code and at that point it checks the types. Only if everything is ok does the program run. That's why we can get errors detected prior to program execution.

On the other hand, in JavaScript types are checked at run time. That means types are not checked until the program executes.

Something also important to mention is that TypeScript **transpiles** code into JavaScript.

> Transpiling is the process of taking source code written in one language and transforming it into another language.

Browsers don't read TypeScript, but they can execute TypeScript-written programs because the code is converted to JavaScript at build time.

We can also select to what "flavor" of JavaScript we want to transpile to, for example es4, es5, and so on. This and many other options can be configured from the `tsconfig.json` file that is generated every time we create a TypeScript project.

```ts
{
  "compilerOptions": {
    "module": "commonjs",
    "esModuleInterop": true,
    "target": "es6",
    "moduleResolution": "node",
    "sourceMap": true,
    "outDir": "dist"
  },
  "lib": ["es2015"]
}
```

We won't go in depth into TypeScript's compiler because this is meant to be an introduction. But know there're a ton of things you can configure from this and other files, and in this way adapt TypeScript to exactly what you need it to do.

# How to Create a TypeScript Project

We can start a new TypeScript project by just running a few commands in our terminal. We'll need Node and NPM installed in our system.

Once we're in the directory of our project, we first run `npm i typescript --save-dev`. This will install TypeScript and save it as a development dependency.

Then we run `npx tsc --init`. This will initialize your project by creating a `tsconfig.json` file in your directory. As mentioned, this tsconfig.json file will allow you to further configure and customize how TypeScript and the tsc compiler interact.

You will see this file comes with a set of default options and a whole lot of commented out options, so you can see all you have at your dispossal and implement it as needed.

```ts
{
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig.json to read more about this file */

    /* Projects */
    // "incremental": true,                              /* Enable incremental compilation */
    // "composite": true,                                /* Enable constraints that allow a TypeScript project to be used with project references. */
    // "tsBuildInfoFile": "./",                          /* Specify the folder for .tsbuildinfo incremental compilation files. */
    // "disableSourceOfProjectReferenceRedirect": true,  /* Disable preferring source files instead of declaration files when referencing composite projects */
    // "disableSolutionSearching": true,                 /* Opt a project out of multi-project reference checking when editing. */
    // "disableReferencedProjectLoad": true,             /* Reduce the number of projects loaded automatically by TypeScript. */

    ...
```

And that's it. We can then create a file with the `.ts` extension and start writting our TypeScript code. Whenever we need to transpile our code to vanilla JS, we can do it by running `tsc <name of the file>`.

For example, I have an `index.ts` file in my project with the following code:

```ts
const personDescription = (name: string, city: string, age: number) =>
  `${name} lives in ${city}. he's ${age}. In 10 years he'll be ${age + 10}.`;
```

After running `tsc index.ts`, a new `index.js` file is automatically created in the same directory with the following content:

```ts
var personDescription = function (name, city, age) { return name + " lives in " + city + ". he's " + age + ". In 10 years he'll be " + (age + 10) + "."; };
```

Pretty straightforward, right? =)

## A Comment About Libraries

If you're working with React, you should know [create-react-app](https://create-react-app.dev/docs/adding-typescript/) provides a TypeScript template, so you get TypeScript installed and configured for you when the project is created.

Similar templates are also available for Node-Express back end apps and for React Native apps.

Another comment to make is that when working with external libraries, normally they will provide you with specific types you can install and use to type-check those libraries.

For example, using the TypeScript template for create-react-app that I mentioned, the following dependency will be installed:

`"@types/react":`

And that will allow us to type our components in the following way:

```ts
const AboutPage: React.FC = () => {
  return (
    <h1>This is the about page</h1>
  )
}
```

We'll get a deeper look at how to use TypeScript with React in the future. But for starters, just know that this exists. ;)

# Other Functionalities of TypeScript

TypeScript can also be considered a **linter**, a tool that makes real time suggestions to the developer as code is being written. Especially when combined with VS Code, TypeScript can make some sweet suggestions based on our declared types that often save time and errors for us.

Another functionality TypeScript has is as an **automatic documentation tool**. Imagine you get a new job and you have to get to know a huge code base. Having the types declared for each function is of huge help when using them for the first time and reduces the learning curve for any project.

# Roundup

So those are the basics of TypeScript. As we've seen, it can add a bit of boilerplate to our code. But it surely pays off by preventing bugs, helping us get acquainted with our code base, and just overall improving our develpoment experience, especially when working in big and complex projects.

I hoped you enjoyed the article and learned something new. If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/germancocca/) or [Twitter](https://twitter.com/CoccaGerman).

Cheers and see you in the next one! =D
