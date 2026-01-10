---
title: Should You Learn TypeScript? Pros and Cons of TS Explained
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2024-05-10T14:50:13.000Z'
originalURL: https://freecodecamp.org/news/should-you-learn-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/typescript-worth-1.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'In this article, we''ll explore the question: is TypeScript worth learning?
  Before we try finding the answer together, let me tell you why I''m suddenly asking
  this.

  I come from a Java background where writing code demands that you be type-aware.
  This ...'
---

In this article, we'll explore the question: is TypeScript worth learning? Before we try finding the answer together, let me tell you why I'm suddenly asking this.

I come from a Java background where writing code demands that you be type-aware. This means that if you are declaring a string, you would have to write its type as `String` explicitly, like this:

```java
// Declaring a String in Java

String greeting = "Is TypeScript Worth Learning?"
```

After developing software products with Java for 8 long years, when I shifted to `JavaScript`, the developer inside me was thrilled – so much so that it felt like, "Oh man! I finally got a fresh breath of air”. 

I didn't have to worry about types and declaring them beforehand. I seemed to be writing less code, and the world was suddenly a paradise of freedom for me to build, test, and ship.

Another enjoyable 4 years passed with JavaScript and I grew up to become a senior developer. Then I got my formal introduction to `TypeScript`. 

So here is my opportunity to tell you what I think, and whether TypeScript is worth learning. I am going to share the experience I've earned over the years. If you agree/disagree/want to know more, my socials are mentioned at the bottom of this article. I would love to connect and discuss. Keep reading. 

If you would also like to check out the video version of this article, here it is: 😊

%[https://www.youtube.com/watch?v=whGzNBqdNS0]

## **Table of Contents**

* [What is TypeScript?](#heading-what-is-typescript)			
* [Getting Started with TypeScript – The Challenges](#heading-getting-started-with-typescript-the-challenges)
* [Learning More About TypeScript – The Benefits](#heading-learning-more-about-typescript-the-benefits)
* [Baby Steps to Start Coding in TypeScript](#heading-baby-steps-to-start-coding-in-typescript)
* [So What's The Verdict: Is TypeScript Worth It or Not?](#heading-so-whats-the-verdict-is-typescript-worth-it-or-not)
* [Before We End...](#heading-before-we-end)

## What is TypeScript?

`TypeScript` is JavaScript at its core with additional syntax for types. Traditionally, JavaScript is a loosely typed language. Its flexibility in allowing developers to use (or misuse) random type assignments may lead to unwanted bugs in their applications. 

That's where TypeScript comes in handy as a strongly typed programming language. It helps safe-guard devs from breaking applications at runtime by helping with type checks at code compilation time. You can learn more about TypeScript and its Type Safety from [the official TypeScript site](https://www.typescriptlang.org/).

TypeScript helps JavaScript developers catch errors early in their code editor. The experience of being aware of the possible errors as you code can help you and your team trust the final output the code will produce. 

If you know JavaScript, you do not have to learn any additional programming fundamentals to code in TypeScript. You just need to be aware of its type system and related syntax to apply them on your JavaScript code.

Personally, TypeScript has changed the way I used to code and ship my products. But it was not a cake walk to get into the mindset of using TypeScript by sacrificing all the flexibility you get with JavaScript. I had my own challenges and ways to overcome them.

This article is for every developer who comes across those challenges when they start coding in TypeScript. And it's meant to help you with the mindset you'll need to appreciate TypeScript's strictness, and how to identify biased (and false) information related to TypeScript to make the right choice for your projects.

Remember, TypeScript is not for everyone or every occasion. But it'll be easier for you to make the choice if you are aware of  its qualities, where it fits in, and where it doesn't. I hope you this article helps you start understanding TypeScript's benefits and limitations, and that you enjoy the process of selecting or rejecting TypeScript for your upcoming projects. 

## Getting Started with TypeScript – The Challenges

To be honest, starting with TypeScript was a shock for me, and it proved to be a bit of a nightmare. This was primarily because of the following challenges:

### Project Setup and Tools Needed

It was not as simple as opening up the browser DevTool's Console tab, and starting to write code to see the output. This works great with JavaScript, and I – like many other beginners – had started gaining confidence coding in JavaScript by writing the code in the browser directly. 

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-12.png)
_Writing JavaScript in the browser DevTool's console tab_

With TypeScript, though, the browser doesn't understand its syntax. And you might be left wondering...what's next?

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-13.png)
_You can't run the TypeScript program the same way - you'll get an error_

You may start realizing that you need additional tools and build systems to print a “Hello World” on the console.

### The TypeScript Compiler

So, is there a compiler, too? Also, are you saying that the TypeScript Compiler (tsc) compiles the TypeScript code to create equivalent JavaScript code which we will run eventually? That’s weird. Then why not code in JavaScript directly? This thought baffles many developers starting with TypeScript.

### The “One and Only” `tsconfig.json` File

TypeScript projects need explicit configurations to work in an environment that you define. You provide the configurations using the `tsconfig.json` file. It allows you to configure the output file path, type strictness, how to handle TypeScript related-features like `any`, and how you want TypeScript to treat `null`, `undefined`, and so on.

The good news is, it works great once you've configure things correctly. But the bad news is, as a newbie, you may be clueless about an error like the one you see below in the `tsconfig.json` file, even when you haven't touched the file at all.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-14.png)
_The curious case of the tsconfig file._

### The Sense of Slowing You Down

As a beginner to TypeScript (especially when you have already spent a good amount of time working with JavaScript), you may feel like you're being slowed down. The feeling comes from the need to always be defining your types. 

That's when you start thinking:

* I'm writing extra code.
* Extra code means extra hours of work.
* That's extra brain power and maintenance.
* Am I overcomplicating some of the simple patterns of JavaScript?

![Image](https://www.freecodecamp.org/news/content/images/2024/05/clock.gif)
_After a few days..._

## Learning More About TypeScript – The Benefits

If you haven't given up yet, and you're still in exploration mode, your perspective of TypeScript may start changing. Here are some of the benefits of coding in TypeScript:

### Type Safety

TypeScript is a superset of JavaScript. It has everything that JavaScript has, plus it ensures `Type Safety`. 

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-15.png)
_TypeScript as a superset of JavaScript_

Type safety is a mechanism to ensure you are using the right types of values in your code. It helps safeguard your applications from breaking something at runtime (in production when your users are using the application). TypeScript also ensures type safety at compile time, much before you push any code changes to other developers or to your users.

Here is an example of some type-safe code in TypeScript. The function `sumOfTwo` accepts two parameters of `number` type and returns a value that is also of `number` type. 

```js
function sumOfTwo(a: number, b: number): number {
    return a + b;
}

```

If the caller of the function doesn't adhere to the types defined, the code will not compile and produces compilation errors.

```js
console.log(sumOfTwo(1,2)); // 3
console.log(sumOfTwo(1,-1)); // 0

console.log(sumOfTwo("tapas", 1)); // TypeError
```

This behaviour of TypeScript safe-guards your code so it doesn't fail in production from any type-related errors.

### Easier Learning Curve

Type Safety is fine. How about the learning curve? If you know JavaScript already, your learning curve for TypeScript will be smaller. 

If you do not know JavaScript, you can consider starting with TypeScript straightway, as learning JavaScript is equally challenging.

### The Tooling Problem

Fortunately, there are ways to handle the initial tooling and build system problem we discussed before. Developers around the world have been using TypeScript for a while now and there are existing resources to get the help you need and set everything up. 

If you have prior knowledge of Node and the JavaScript ecosystem, it may take half a day to set things up. If you do not have either Node or JavaScript or both, it may take a couple days max.

I have been through a similar phase, and now I have my own environment to use for all my TypeScript projects. You can [check it out on my GitHub](https://github.com/tapascript/ts-gyan) and feel free to start using it. If you want to create something similar and customize it to create your own, [this guide](https://www.youtube.com/watch?v=P3unJiZxfkI) will help you with that.

Also, the best part is, all this setup is a one-time job. You do it once, and you can replicate or reuse it for all your future projects. 

You will also understand the power of VS Code IntelliSense while coding in TypeScript. It prompts you with code completion to make your coding experience even better.

### How about the tsconfig thingy?

Undoubtedly, you'll need some time to learn about the configuration properties in the `tsconfig.json` file and what they do. But the positive thing is you do not need to know them all. 

When you are getting started, just make sure you know what is minimally needed for your project and learn about those things. Rest assured that you can learn other things as and when you need them.

## Baby Steps to Start Coding in TypeScript

After the initial struggle with tooling, building, and configuration, you may be itching to write your first line of TypeScript code (assuming you haven't started blaming TypeScript for your lack of productivity yet!). 

Let's look at some scenario-based comparisons between the flexible world of JavaScript and the strict world of TypeScript.

### JavaScript vs TypeScript Examples

A simple sum of two numbers in JavaScript would look like this:

```jsx
function sumOfTwo(a, b) {
  return a + b;
}

console.log(sumOfTwo(1,2)); // 3
console.log(sumOfTwo(1,-1)); // 0

```

But doing the same thing with TypeScript would require an extra bit of code to tell the TypeScript compiler about the type of the parameters and the return type:

```tsx
function sumOfTwo(a: number, b: number): number {
  return a + b;
}

console.log(sumOfTwo(1,2)); // 3
console.log(sumOfTwo(1,-1)); // 0

```

Hmm! That seems to be more work than necessary. But it's really more helpful than you can imagine. It guards your code against considering unacceptable inputs instead of what the more "flexible" JavaScript would allow:

```jsx
function sumOfTwo(a, b) {
  return a + b;
}

console.log(sumOfTwo(1, true)); // The output is 2
console.log(sumOfTwo(1, [])); // Believe or not, it will result 1

```

Trying out the above code in TypeScript wouuld result in compilation errors. If you are running the TypeScript compiler in watch mode (with the command `tsc -w`), you can catch these errors while writing the code itself!

```tsx
function sumOfTwo(a: number, b: number): number {
  return a + b;
}

console.log(sumOfTwo(1, true)); // Error
console.log(sumOfTwo(1, [])); // Error

```

That's not all. Let’s take another example. Consider an employee array with the details of a few employees in your JavaScript code:

```jsx
// Employee Object

const employees = [
    {
        id: '01',
        name: 'Alex',
        age: 23,
        married: false
    },
    {
        id: '02',
        name: 'Bob',
        age: 3,
        married: false
    },
    {
        id: '03',
        name: 'Clara',
        age: 28,
        married: true
    }
];

```

Now, let's say you want to filter out the married employees. 

```js
// Filter the married employees

employees.filter(emp => emp.married) // Clara
```

It works great! But imagine if some of the employee data is incorrect somewhere. What if you are getting the employee object as an API response where the `married` property value of the employee `Bob` is set to `3` by mistake!

```jsx
const employees = [
    {
        id: '01',
        name: 'Alex',
        age: 23,
        married: false
    },
    {
        id: '02',
        name: 'Bob',
        age: 3,
        married: 3
    },
    {
        id: '03',
        name: 'Clara',
        age: 28,
        married: true
    }
];
```

Now, your same logic of filtering the married employees would result in saying both Bob and Clara are the married employees – but Bob may not be married at all.

```js
// Filter the married employees

employees.filter(emp => emp.married) // Bob and Clara

```

Hold on! You can still safe-guard the above situation with some lines of extra logic in your JavaScript code. How about you check the type of the value of each employee's `married` property in the array and throw an error if it's not a `boolean`?

```jsx
employees.filter((employee) => {
  if (typeof employee.married  === 'boolean') {
      return employee.married && employee;
  } else {
      throw new Error("The employee.married type is not of boolean type.")
  }
});

```

This fixes the problem. But hang on, isn’t that:

* Extra lines of code you have written to safe guard your code from failing?
* Extra hours of work?
* Extra brain power and maintenance? What if similar value mistakes happen in other properties of the employee object? Would you keep adding conditions in the filter callback?
* Overcomplicating some of the simple patterns of JavaScript?

A better and safer situation is to use TypeScript and type safe each of the properties of the employee object either by defining a [type or using interfaces](https://youtu.be/VE5SOoP2Y74?list=PLIJrr73KDmRy_ufvq5m_4KwnxUdx9Sq3d).

```ts
type Employee = {
	id: string,
    name: string,
    age: number,
    married: boolean
}
```

## So What's The Verdict: Is TypeScript Worth It or Not?

If you are coming to this section following the previous sections of this article, then the following points will make sense to you:

* You may not like TypeScript just by looking into it, what it promises, and the code written with it. You need to spend some time with TypeScript by writing code, and building projects with it.
* The complexity of tooling, builds, and configurations shouldn't stand in your way. There are many resources to help you figure these things out. As we discussed before, these are solved problems, and you don't need to reinvent the wheel.
* For JavaScript developers, it can hard to accept TypeScript without a deeper understanding of JavaScript itself. But the more you learn about it, the more I think you'll see that TypeScript indeed has an edge that'll help safeguard you and your team from type issues.

Now the question is – is it worth it?

Absolutely yes! Especially so if:

* Your project is beyond a simple app like a TODO app.
* You want to catch type errors and mistakes at compile time while writing your code instead of in production.
* The project is being developed by a team of JavaScript developers.
* You want to debug your code efficiently.
* You are looking for a common data contract interface between client and server for data exchange.
* Last but not least, if you don't want to miss out on the job opportunities that come with knowing TypeScript. If you know JavaScript basics, getting started with TypeScript will not be hard if you get proper guidance.

## Before We End...

I want to end this article with a quote: 

> “Learning is an experience. Everything else is just information.” – Albert Einstein.

So it's up to you to decide if something is worth learning.

It should depend on why, rather than what, you want to learn. You will have limitations with how many things you can learn in your lifetime…so learn wisely.

This is also why I started my TypeScript playlist practically to make sure you don't come in with certain assumptions. I want you to learn TypeScript first so you can be a confident decision-maker when technology choices come. 

[Here is the link to my TypeScript playlist](https://www.youtube.com/watch?v=whGzNBqdNS0&list=PLIJrr73KDmRy_ufvq5m_4KwnxUdx9Sq3d) if you want to check it out. The playlist will break down each of the configurations, concepts, and project building in a beginner-friendly way to help you learn TypeScript rapidly.

That's all for now. I hope you found this article informative and insightful. I am an educator on my YouTube channel, `tapaScript`. Please [SUBSCRIBE](https://www.youtube.com/tapasadhikary?sub_confirmation=1) to the channel if you want to learn JavaScript, TypeScript, ReactJS, Next.js, Node.js, Git, and all about Web Development in a fundamental way.

Let's connect.

* [Follow me on X (Twitter](https://twitter.com/tapasadhikary)) or [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) if you don't want to miss the daily dose of Career Tips.
* Find all my public speaking talks [here](https://www.tapasadhikary.com/talks).
* Check out and follow my Open Source work on [GitHub](https://github.com/atapas).
* I regularly publish meaningful posts on my [GreenRoots Blog](https://blog.greenroots.info/), you may find them helpful, too.

See you soon with my next article. Until then, please take care of yourself, and stay happy.

