---
title: What is TypeScript?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T00:31:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/typescript.png
tags:
- name: toothbrush
  slug: toothbrush
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Frances Coronel

  TypeScript Overview

  So as you are most likely aware, JavaScript is expanding its footprint everyday.
  It is both overwhelming and amazing what you can do with the language nowadays.

  However, as more large-scale projects start to use...'
---

By Frances Coronel

## **TypeScript Overview**

So as you are most likely aware, JavaScript is expanding its footprint everyday. It is both overwhelming and amazing what you can do with the language nowadays.

However, as more large-scale projects start to use JavaScript, the process of making the code easier to write and more maintainable becomes more and more difficult.

This is a problem Microsoft recognized early on and they came up with a solution: TypeScript The first version was released on October 1st, 2012.

## **JavaScript vs TypeScript**

![Where's Waldo](https://i.imgur.com/DznuAou.jpg)

Okay so now that we have a general sense of what TypeScript is, let’s play a quick game of **Where’s Waldo**.

In the above screenshot, you can spot the differences between `JavaScript` & `TypeScript` in this very simple multiplication program that just prints out the product of two numbers I’ve pre-defined.

### **What are those differences though? ?️**

They’re **types**!

So `JavaScript` has dynamic typing in that a variable declared as a number can be turned into a string where as `TypeScript` has static typing meaning you declare beforehand what type of value the variable will hold and it doesn’t change.

In that `multiplication.ts` file, I’m declaring all these variables to be numbers so they cannot be changed to something else.

In essence, TypeScript is trying to help JavaScript reach new heights and become very scalable. It can be highlighted by the following features:

* free and open-source programming language developed and maintained by Microsoft
* strict syntactical super-set of JavaScript that compiles to plain JavaScript
* eases development of large scale applications written in JavaScript
* extends JavaScript by adding static types, classes, modules, interfaces and generics

**? FUN FACT** TypeScript turned 7 years old on October 1st, 2019.

## Version

Latest stable version available is [TypeScript 3.7](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html) (as of early 2020).

## **How to Install TypeScript**

![Installation](https://i.imgur.com/9ILjA1q.jpg)

To get started yourself, the two things you will need are the TypeScript compiler and an editor that supports TypeScript.

In the above screenshot, I’m installing both the compiler and [TSLint](https://github.com/palantir/tslint) (which is similar to [ESLint](https://eslint.org/)) using `npm` in [Visual Studio Code](https://code.visualstudio.com/)’s integrated terminal.

### **Installing TypeScript**

This command will install the TypeScript package as a dependency in your project using [`npm`](https://www.npmjs.com/) which is a popular package manager.

```bash
npm i typescript
```

_To Note_ There are [several options](https://docs.npmjs.com/cli/install) that `npm` provides depending on where you want TypeScript installed.

* `npm i -g typescript` to globally install the TypeScript package
* `npm i -D typescript` to install the TypeScript package as a dev dependency

### **Compiling a single file down to JavaScript**

```bash
tsc multiplication.ts
```

_To Note_ You can configure this TypeScript compilation process as a custom npm script in your `package.json`.

### **Configuration Options**

```bash
touch tsconfig.json
```

There’s also the option to create a [`tsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) file that specifies the root files and compiler options.

Within your [`tsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) file, for example, you could specify that you want TypeScript to compile down to ES5 instead of ES6.

### **Quick Example**

![Multiplication](https://i.imgur.com/V5nP3xj.jpg)

In the screenshot above, you can see two files - `multiplication.js` and `multiplication.ts`.

This program just prints out the product of two numbers I’ve pre-defined.

`multiplication.ts`

```typescript
let a: number = 10;
let b: number = 2;

function showProduct(first: number, second: number): void {
  console.info("Mathematical! The result is " + first * second + ".");
}

showProduct(a, b);

// Mathematical! The result is 20.
```

Once I’ve finished creating `multiplication.ts`, I can compile it down to JavaScript using the `tsc` command which stands for TypeScript compile.

`multiplication.js`

```javascript
var a = 10;
var b = 2;

function showProduct(first, second) {
    console.info("Mathematical! The result is " + first * second + ".");
}

showProduct(a, b);

// Mathematical! The result is 20.
```

Bam - we just successfully compiled TypeScript to JavaScript!

## **TSLint**

![TSLint](https://2.bp.blogspot.com/-w7oeP1geosE/V82a740bTbI/AAAAAAAAAu4/-zJxZsmmH6garbdmUplX0n5Yz5zDsvcVQCLcB/s1600/tslint.png)

A [linter](https://www.wikiwand.com/en/Lint_(software) is a tool that detects and flags errors in programming languages, including stylistic errors.

For TypeScript, [TSLint](http://palantir.github.io/tslint) is the most popular linter option.

TSLint is an extensible static analysis tool that checks TypeScript code for readability, maintainability, and functionality errors.

It is widely supported across modern editors & build systems and can be customized with your own lint rules, configurations, and formatters.

### **Installing TSLint**

This command will globally install the `TSLint` package using `npm`, a popular package manager.

```bash
npm i -g tslint
```

## Playground

![Playground](https://i.imgur.com/vlV7ZFr.png)

If you want to try out TypeScript without installing it, visit the [TypeScript Playground](http://www.typescriptlang.org/play/index.html).

The Playground has built-in auto completion and the ability to directly see the emitted JavaScript.

### **Other Resources**

To learn more about installation, see the [Installation Appendix](https://guide.freecodecamp.org/typescript/src/articles/typescript/appendix-installation/index.md).

In case you need just a type checker and don’t want to compile your program, read about [Flux](https://facebook.github.io/flux/).

* [Quick Start](http://www.typescriptlang.org/samples/index.html)
* [Documentation](http://www.typescriptlang.org/docs/home.html)
* [Source Code](https://github.com/Microsoft/TypeScript)

