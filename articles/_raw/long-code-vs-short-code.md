---
title: 'Long Code vs. Short Code: What’s Better for Your Use Case?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-24T17:05:41.000Z'
originalURL: https://freecodecamp.org/news/long-code-vs-short-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c00740569d1a4ca2f4c.jpg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Alfrick Opidi

  In order to successfully program an application, you need to make a number of small
  decisions while trying to solve a greater set of problems.

  How wisely you make those decisions, and whether you write long lines of code or
  short lin...'
---

By Alfrick Opidi

In order to successfully program an application, you need to make a number of small decisions while trying to solve a greater set of problems.

How wisely you make those decisions, and whether you write long lines of code or short lines of code, relies more on your preferences, skills, and expected outcomes.

So you might be wondering: between long code vs. short code, which is better?

Here are some factors to consider before deciding whether to use many or fewer lines of code.

## 1. Readability

[Martin Fowler](https://en.wikipedia.org/wiki/Martin_Fowler), an expert software developer, once said, “Any fool can write code that a computer can understand. Good programmers write code that humans can understand”.

Create your code with other people in mind. On the one hand, it will be processed by a machine, which doesn’t care whether you use a lot or a little code. But your source code may evolve in other people’s hands who need to understand how the code operates and what improvements they should make.

So, when programming, the readability of the source code will often be more important than the number of lines of code.

Here is an example of some JavaScript code that uses the ternary operator syntax for an `if..else` statement:

```js
const firstNumb = 100;

let secondNumb;

const secondNumb = firstNumb > 50 ? "Number is greater than 50" : "Number is less than 50";

```

Here is the same code written in the traditional long-form format:

```js
const firstNumb = 100;

let secondNumb;

if (firstNumb > 50) {
  secondNumb = "Number is greater than 50";
} else {
  secondNumb = "Number is less than 50";
}

```

The second programming style consists of many more lines of code than the first one. But you could argue that it's easier to read and interpret—especially for novice programmers.

Still, the first version with the ternary operator syntax could be a great time saver if you want to write an `if..else` statement in just a single line.

If you are working on a project with other programming teams, make sure your code is readable. Especially if you care for the long-term sustainability of the project. 

You need to consider that other developers may not be able to easily interpret your source code. So you need to make your code easily and quickly understandable.

For example, if you are collaborating with other developers in building an app that fetches [Netflix content](https://vpnpro.com/guides-and-tutorials/how-to-change-netflix-region/), then it is better to use long, clear lines of code. In that case, short lines of code may only show your peers that are you are “smart,” and their input may not be useful.

## 2. Maintainability

Short and confusing code can be difficult to maintain. It may result in problems like bugs and higher overhead costs during quality maintenance. It can also cause motivational issues and plain hullabaloo for you as a developer.

What if you write a short piece of code and discover that you are unable to interpret it six months from now? Longer, more detailed code might assist you in reacquainting yourself with what you wrote and why you wrote it in that particular style.

With longer code, [debugging](https://docs.microsoft.com/en-us/visualstudio/debugger/debugging-absolute-beginners?view=vs-2019) a program becomes much easier since you will have unrelated variables to scrutinize and more places to insert breakpoints.

On the other hand, short and unclear code can waste time and money while developers re-factor or rewrite the existing code to include new features that are [easier to maintain](https://www.freecodecamp.org/news/legacy-software-maintenance-challenges/) in the long run.

This code is shorter:

```js
let a, b, c= 50;
```

However, it is easier to maintain the code below:

```js
let a;

let b;

let c = 50;
```

## 3. Efficiency

Arguably, using shorter lines of code is more efficient than spreading the code over several lines. If you have more lines of code, there are more places for bugs to hide and finding them might be more of a hassle.

Fewer lines of code can achieve the same results (and probably better) than many lines of code. If you reduce the amount of code in a task, you will lower the bug count, especially if the source code is clear, readable, and maintainable.

Also, writing long lines of code may require you to include too many local variables, since you have to formulate names for them. All those different names can lead to confusion and inefficient programs.

If you want to build efficient apps with fewer bugs to trouble you, then using fewer code lines may be your best solution.

## 4. Expected workload

Shorthand coding enables you to achieve more with less, and therefore drastically reduces the number of hours you spend developing your apps. With sufficient training and experience, you can learn how to do more quickly and with fewer lines of code.

As you probably know, long lines of code are sometimes demanding to write and can make you put in long hours.

With short code, you can lower the amount of code needed for repetitive statements and string manipulation. This way, instead of using verbose code, you can conveniently combine many steps into single steps and greatly reduce your workload and other associated costs.

Here is some JavaScript code written using many lines:

```js
function myFunc(foo) {
  console.log("Hello World", foo);
}

setTimeout(function () {
  console.log("Upload completed");
}, 3000);

mylist.forEach(function (foo) {
  console.log(foo);
});

```

And, here is the same code in a shorter format written using the [JavaScript arrow function syntax](https://guide.freecodecamp.org/javascript/arrow-functions/):

```js
myFunc = (foo) => console.log("Hello World", foo);

setTimeout(() => console.log("Upload completed"), 3000);

mylist.forEach((foo) => console.log(foo));

```

Clearly, the first example requires more time to write than the second example.

If workload is important for you and you have sufficient programming skills, then using shorter code is probably the way to go.

## Conclusion

Ultimately, the choice whether to use long code vs. short code does not matter. Instead, what matters is writing the code in a manner suitable for its intended use. Source code that is longer than it needs to be will result in more errors, increased unnecessary load, and wasted time and resources.

On the other hand, if you are writing shorter code by replacing numerous simple lines of code with one complex line of code, or verbose statements with vague ones, or straightforward operations with strange hacks, then the loss in overall usefulness will normally outweigh the gain in conciseness.

So, when building an application, you should make sure that every line serves its intended purpose. And whether you use long lines of code or short lines of code should not be your key motivator.

Your real objective for each case should be to achieve high standards of readability, maintainability, efficiency, and cost-friendliness—normally in that order. And the number of lines of code should not have a place in that list.

