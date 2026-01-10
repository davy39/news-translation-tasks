---
title: What is Type Erasure in TypeScript?
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-12-06T19:21:41.000Z'
originalURL: https://freecodecamp.org/news/what-is-type-erasure-in-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/TypeErasure--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'TypeScript is a transpiled language, and there is a step in the process
  called type erasure.

  So what exactly is transpiling, and what is type erasure?

  Higher Level vs Lower Level Programming Languages

  Before we explain further, we have to understand ...'
---

TypeScript is a **transpiled** language, and there is a step in the process called **type erasure**.

So what exactly is **transpiling**, and what is **type erasure**?

# Higher Level vs Lower Level Programming Languages

Before we explain further, we have to understand higher and lower level languages.

Higher level languages are more abstracted than lower level languages. By abstracted I mean they're easier for humans to understand. 

For example, you would say machine code (binary) is lower level and closer to the computer than JavaScript. Higher level languages generally are more simple to write and understand than writing lower level languages (Assembly for example) where you have to understand and deal with memory addresses directly, and so on.

**Compilation** and **transpilation** are very similar steps, but they're not identical. I'll explain both so you know the difference.

## What is Compiling?

Compiling is a catch-all term for turning code that you've written into some lower-level executable for the computer (generally machine code). 

An example of some compiled languages are Java, C# or C. Sometimes it's compiled in multiple steps, each step optimising the code and getting it closer to machine code with each "pass" it does. 

Through this process, a high level, closer to human readable language ends up "lower" or closer to binary.

## What is Transpiling?

Transpilers are sometimes referred to as "source to source compilers" – so, a short hand way of saying "source code to source code". Transpiling means converting one higher level language to another higher level language. 

For example, TypeScript is a high level language but after it's transpiled it's turned into JavaScript (another high level language). Or Babel for example can transpile ES6 JavaScript code into ES5 JavaScript. 

The benefits of transpiling are that you can write one high level language and still end up with another high level language.

# Type Erasure in TypeScript

Part of this **transpiling** process is called **type erasure**.

**Type erasure** is quite simply when all the types get removed from the TypeScript code as it is transpiled to JavaScript.

The types you use in TypeScript can't be inspected at run-time, when JavaScript is being executed. The **types** are only accessible during the compilation/transpilation step. 

TypeScript code that looks like this:

`let name: string = 'Kealan';`

Eventually gets compiled/transpiled to this:

`let name = 'Kealan'`

The output might vary depending on your specific build steps (the variable may be renamed, or inlined) but the example of **type erasure** still stands true.

This isn't just with primitive types like `number` or `string` – but even with your own custom types you may create:

```
type StringType = string;

const firstName: StringType = "Kealan";
```

## Type Erasure in practice

More than just conceptually understanding what **type erasure** is, this concept explains an important step in the transpiling process where types are thrown away and aren't used in the source code you generate.

It also means that pieces of your code aren't even "used" in JavaScript during the transpiling step – and the code is just completely removed. So your 100 line interface you create just gets removed, and the code sent to the user is smaller.

You can look at an example of this in the [TypeScript playground](https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgApQPYHMpwLZ7TIDeAUMhciPhAFzIDOYUoWANOZQDbADWEDekxYh2nCpAQALEF2wBPAKoMIAEyHNWAbQC6pAL6lSCDCCbJ+cLnBD102XASIBeEuKo16AcgDSEKzZeHJTIPPyCyF4AwlICDEHukjJyWEoq6shaXgBScABucADKCCwADmBBkQAq8qUQxWUVbJEASv4ITZEAchiqEF46yAZAA), where an interface used in the TypeScript code is absent in the transpiled JavaScript.

# Conclusion

I hope some of the steps TypeScript takes to turn your code into JavaScript are a little clearer, and that you have a good overview of the differences between **compiling** and **transpiling**.

I tweet my articles [here](https://twitter.com/kealanparr) if you would like to read more.

