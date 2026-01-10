---
title: Learn TypeScript Basics in this Beginner's Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-04T18:01:00.000Z'
originalURL: https://freecodecamp.org/news/learn-typescript-basics
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Typescript-Getting-Started.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Joel P. Mugalu

  TypeScript has taken the development world by storm. No wonder it has over 15 million
  weekly downloads on npm. But what is TypeScript, and what do you need to know about
  it?

  In this article, I am going answer those questions. By the...'
---

By Joel P. Mugalu

TypeScript has taken the development world by storm. No wonder it has over 15 million weekly downloads on npm. But what is TypeScript, and what do you need to know about it?

In this article, I am going answer those questions. By the end you'll have a grasp of the following:

- What TypeScript is
- Main pillars of TypeScript
- Main features of TypeScript
- Why you should use TypeScript
- TypeScript basics to get you started 

First, let's address the elephant in the room.

## What is TypeScript?
TypeScript is a programming language built and maintained by Microsoft.
It is a superset of JavaScript that adds strong type checking and is compiled into plain JavaScript code. 

Being a superset means that TypeScript has all the features of JavaScript as well as some additional features.

TypeScript comes with features such as better development-time tooling, static code analysis, compile-time type checking, and code-level documentation. 

Don't worry if you have no idea what any of this means. I'll explain all of it in this article.

All these features that come with TypeScript make it the perfect programming language for building large-scale JavaScript applications.

## Main pillars of Typescript
Typescript is built upon three main pillars – namely the language, the compiler, and the language service.

### TypeScript Language
This consists of the syntax, keywords, and type annotations of TypeScript.
TypeScript syntax is similar to but not the same as JavaScript syntax. 

### TypeScript Compiler
The compiler is responsible for compiling TypeScript code into JavaScript.
In reality, what happens is not actually compiling but transpiling.

> Compiling means that source code is transformed from a human-readable format to a  machine-readable format, whereas transpiling is transforming source code from one human-readable format to another human-readable format.

The TypeScript compiler is also responsible for erasing any information related to types at compile time. 

Types are not valid features in JavaScript. And since TypeScript has to be compiled to plain JavaScript, anything related to types has to be erased before it can become valid JavaScript ready to be executed by the browser.

The Typescript compiler also performs code analysis. It emits errors and warnings if there's reason to do so.

### Language Service
The language service is responsible for collecting type information from the source code. 

This information can then be used by development tools to provide IntelliSense, type hints, and refactoring alternatives.

## Main Features of TypeScript

### Type Annotations in TypeScript
Type annotation simply means assigning a type to a variable or function.

```js
const birthdayGreeter = (name: string, age: number): string => {
  return `Happy birthday ${name}, you are now ${age} years old!`;
};

const birthdayHero = "Jane User";
const age = 22;
console.log(birthdayGreeter(birthdayHero, 22));
```

In the above example, we define a function that accepts two parameters `name` and `age`. We assign `name` to the type _string_  `age` to the type _number_ 

We can also assign types to the return value of a function. In this case, our function returns a value of the type _string_

```js
const birthdayGreeter = (name: string, age: number): string => { };
Typescript would yield an error if we passed in arguments of different types than ones we expect
```

### Structural Typing in TypeScript
TypeScript is a structurally typed language meaning that if two elements have corresponding and identical features then they are considered to be of the same type.

### Type Inference in TypeScript
The TypeScript compiler can attempt to infer the type information if there is no specific type assigned. This means that TypeScript can assign a type to a variable or function based on its initial values or usage.

Type inference usually happens when you initialize variables, set default values, and determe function return types

```js
const platform = 'freeCodeCamp';
const add = (a: number, b: number) => a + b
```

The variable platform in the above example is assigned the type _string_ even though we didn't explicitly do so and the return value of the function `add` is inferred the type _number_.

### Type Erasure in TypeScript
TypeScript removes the type system constructs during compilation:

Input
```js
let x: someType;
```

Output
```js
let x;
```

## Why use TypeScript?

### Type checking and static code analysis

This reduces the overall errors in your code because TS will warn you when you wrongfully use a certain type.

It also reduces runtime errors and because of static code analysis, TypeScript will throw warnings about typos and such. So this means fewer errors which could potentially mean less testing.

### Type annotations can act like code documentation

Type annotations help us to understand what type of arguments a function expects, for example, and what it returns.

This makes code more readable and makes it easier for others and for us to understand what the code is supposed to do.

Another advantage of TypeScript is that IDEs can provide more specific and smarter IntelliSense when they know exactly what types of data you are processing.

## How to Get Started with TypeScript
Let's begin by installing the TypeScript package. Here we have two options: we can either install it globally so we can use it on any project in the system, or we can install it to use on the specific project we're working on.

You can install TypeScript globally by running this command:
```shell
npm install -g typescript
```

If you don't wish to install globally you can just run this:
```js
npm install --save-dev typescript 
```

In the local installation, TypeScript is installed as a dev dependency because we use it for development. It has to first compile to JavaScript before it can be used in production. The browser can't execute TypeScript.

After installing TypeScript, we need to initiate a new project. You can do that by running the following command:
```shell
tsc --init
```

This command initiates a new _tsconfig.json_ file in the root directory of the project. This config file comes with all the configuration options we have for using TypeScript in a project.

![an example of a tsconfig file](https://www.freecodecamp.org/news/content/images/2021/05/image1-1.png)

All the compile options for a particular project can be specified in the tsconfig.json file under the _compileOptions_ key. 

The file comes with some config options by default but you can add more options to the project as needed. You can comment out or delete unused compiler options.

### Built-In Types in TypeScript
Typescript comes built-in with all the primitive types in JavaScript like string, number, and boolean.

The types can then be assigned to variables to specify what data type should be assigned to the variable. This is called type annotation.

```js
const myName: string = 'Joel';
const myAge: number = 99;
```

TypeScript annotations are not always necessary because TypeScript automatically infers the type of a variable based on its initial value or usage. Therefore the following would also be valid TypeScript code:

```js
// myName is inferred type 'string'
 const myName = 'Jonathan';
```

### Arrays in TypeScript
To specify the type of an array you can use the syntax `string[]` or `number[]`. This effectively means 'array of strings or array of numbers'. 

You'll also see people use the syntax `Array<number>` or `Array<string>` which means the same thing.

### Union Types in TypeScript
Union types allow us to define several types that may be assigned to a variable. For this, we use a pipe | to specify the various types.

```js
const someValue: number | string = value; 
```

By default `null | undefined` can be assigned to any variable but TypeScript comes with the _strictNullChecks_ compiler option which does not allow assigning both to a variable.

### Functions in TypeScript
Functions can also receive type annotations. However, with TypeScript functions, they can only receive the specified parameters. Nothing more nothing less.

```js
function introduction(name: string, age: number): string {
    return `Hello, my name is ${name} and I'm {age} years old`
}
```

Function parameters receive normal type annotation.

TypeScript functions must also specify the return data type. In the case where a function returns nothing, we can use _void_ type as the return data type.

We can also use the `?` operator to specify **parameters that are optional**. In this case, Typescript won't complain if the parameter is not passed on the function call.

We can also assign default values to parameters just like we would in normal JavaScript.

```js
const introduction = (name: string, age: number, job?: string = 'developer'): string => `Hello, my name is ${name} and I'm ${age} years old. I work as a ${job}`
```

Notice that in this example I used the JavaScript [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) syntax and specified that the job parameter is optional and assigned a default value 'developer' to it.

### The `any` type in TypeScript
In TypeScript, every variable whose type cannot be inferred becomes implicitly the type _any_. 

`Any` is typically a wild card type that literally means 'whatever type'. We can also explicitly assign the type _any_ to a variable. 

However, `any` typings are usually considered to be problematic.

Typescript comes with the _noImplicitAny_ compiler option which raises an error when we assign the type _any_ to a variable or expression.

### How to Create Your Own Types in TypeScript
TypeScript offers a way for us to define and use our own types for inputs. Here we can describe the exact type that is acceptable for a particular input.

We can use the `type` keyword to define our own types.

```js
type Operator = 'multiply' | 'add' | 'divide'; 
```
Now the `Operator` type can accept either of the values. Notice how we use the OR operator `|` to create a union type. In this case, any variable assigned the type Operator can accept any of the three values.

## TypeScript Example Project

Let's now use this knowledge to create a simple calculator program. A user can only enter one of three operations - add, multiply, or divide. If you want to, take a moment and try to attempt this then you come back and follow along.

Hopefully, you tried it on your own. The program may then look something like this:
```js
type Operation = 'multiply' | 'add' | 'divide';

const calculator = (a: number, b:number, op: Operation): number => {
    switch(op) {
        case 'multiply':
            return a * b;
        case 'add':
            return a + b;
        case 'divide': 
            if (b === 0) return 'Can't divide by 0;
            return a / b;
        default:
        return 'Operation unknow';          
    }
}
```
Try to read the above code and see if you can figure out what is going on.

We can also create custom types using the `interface` keyword. Interfaces allow us to define the property and type of an object. An interface can have the ability to extend another interface.

```js
interface Employee {
    name: string,
    title: string
}

interface Manager extends Employee {
    meeting: (topic: string) => void
}
```

Here we define an interface Employee which has two properties - `name` and `title`, both of which are of the type _string_. 

We then use this interface to create another interface `Manager` which has the same properties as the Employee interface but with a meeting method.

At the outset, I mentioned that Typescript is a structurally typed language. This means that if an element has the same properties as another, they're both of the same types.

The same is true with interfaces. If an object has the properties of an interface then it has the type of the interface. Such an object can have additional properties as long as some properties match those of the interface.

We can now use our defined interface such as:

```js
const newEmployee: Employee = {
    name: 'Joel',
    title: 'FrontEnd Developer'
}
```

So far we've seen that we can create our own types using the _type_ and _interface_ keywords. But, what is the difference between the two?

The most notable difference is that defining multiple interfaces with the same name will result in a merged interface. On the other hand, defining multiple types with the same name will result in an error indicating that the name is already declared.

## Wrapping Up
Typescript has a lot of features that can't simply be exhausted in this article. I just highlighted a few of the features that may be helpful to understand in order to get started working with it. 

You can learn more about Typescript by reading the [documentation](https://www.typescriptlang.org/docs/).

If you liked this article, consider following me on [Twitter](https://twitter.com/codingknite) or connecting with me on [LinkedIn](https://linkedin.com/in/codingknite). I share content about what programming and what am learning. Feel free to get in touch.


