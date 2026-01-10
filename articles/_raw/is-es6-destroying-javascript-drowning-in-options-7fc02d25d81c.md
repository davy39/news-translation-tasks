---
title: ES6 gives JavaScript developers more ways to do things. But that isn’t always
  a good thing.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T07:01:01.000Z'
originalURL: https://freecodecamp.org/news/is-es6-destroying-javascript-drowning-in-options-7fc02d25d81c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JSUlDdjjA24TSCGKPkLm_w.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sam Williams

  I recently wrote an article on ES6 Tips and Tricks which has over 17,000 views and
  4,600 claps. One comment was from Bob Munck who said that:


  This article makes a very strong argument for avoiding JavaScript like the plague
  in any us...'
---

By Sam Williams

I recently wrote an article on [ES6 Tips and Tricks](https://medium.freecodecamp.org/make-your-code-cleaner-shorter-and-easier-to-read-es6-tips-and-tricks-afd4ce25977c) which has over 17,000 views and 4,600 claps. One comment was from [Bob Munck](https://www.freecodecamp.org/news/is-es6-destroying-javascript-drowning-in-options-7fc02d25d81c/undefined) who said that:

> This article makes a very strong argument for **avoiding JavaScript like the plague** in any usage where you want long-term reliability, maintainability, and modifiability.

His opinion seems to be that if the language is changing as much as it is, it’s signing its own death sentence.

### What ES6, 7, and 8 are adding to JavaScript

The newest specifications add a lot of new features to the language. Destructuring, concise object assignment, and symbols to name a few. There are some good things coming through, but this article aims to highlight the problems.

### Why is this a problem?

You want to create a function to receive an object and do some logic upon it. Simple right? But which way are you going to do it?

```
var data = { a: "print me" };
```

```
function method1(data) {    var a = data.a;    console.log(a);}
```

```
function method2(data) {    console.log(data.a);}
```

```
function method3({ a: info }) {    console.log(info);}
```

```
function method4({ a }) {    console.log(a);}
```

All these methods give you exactly the same result. This is a very trivial example but it holds true for far more complex functions.

#### How to decide what to use?

There are 3 main methods for deciding which way to do this:

* Evaluate and compare the available options.
* Just use whatever you want to.
* Have a policy about which to use where.

Each of these has its own advantages and disadvantages.

![Image](https://cdn-media-1.freecodecamp.org/images/VprwzhiI2Ve-XFhV-6YVbHMSEZhnIXk2wONE)
_Photo: [pixabay.com](https://pixabay.com/en/thought-idea-innovation-imagination-2123971/" rel="noopener" target="_blank" title=")_

#### Evaluate and compare the available options

This seems like an obvious choice, but is it the best one? Doing this every time means that you have to assess the advantages and disadvantages of each method EVERY TIME you write a function. That’s a lot of thinking power that could be used on the problem you’re trying to solve.

You and everyone you work with need to know the advantages, disadvantages, and nuances of each method. This doesn’t seem too bad, there are only 4, but then what about dealing with async behavior? Do you use callbacks, Promises, Generators, or Async/Await or a combination of them?

This means that everyone you work with needs to understand every bit of the language. I’m guessing by the number of views on my ES6 article that lots of people are still learning some of the more basic language syntax. This means there are very few who understand the complexities of async behavior (which I’m currently trying to understand well myself).

#### Just use whatever you want

This is the most common approach, for individuals and in companies. This can be great as it means that you don’t waste time and effort calculating the best choice.

The problems could arise when someone else comes to read, or fix, your code. You may be a JavaScript wiz kid and know all of the newest methods for everything. But the next person who comes to read or alter your work may not have a clue what you’ve done.

This also encourages huge style differences between companies and coworkers. It can also mean differences between yourself and a future you, when you learn a new syntax. This isn’t great and makes reading code written by multiple developers much harder.

![Image](https://cdn-media-1.freecodecamp.org/images/34VI1AbwgDW-WSK49E5slOcsguRkTQ5yhrIx)
_Photo: [pixabay.com](https://pixabay.com/en/bureaucracy-aktenordner-paperwork-2106924/" rel="noopener" target="_blank" title=")_

#### Policy

Whether it’s company policy or personal policy this eliminates a lot of the problems with the first two approaches. It doesn’t require thinking and it promotes consistency across a code base. Unfortunately, it still has a few problems.

With new versions of the ECMAScript specifications regularly coming out, there comes a dilemma. Should the company change its policy to be in keeping with the newest releases? Or write a policy and never change it — missing out on the new features? Or should it be somewhere in between?

New hires have to learn the policy and know how to use it. Yes, you could have a booklet on the policies, but it might take longer to find the spec than to write the line of code. Even if they do find the policy on async behavior, they then need to be able to use it. This could end up suppressing junior devs to simple coding as they don’t want to _break the policy_, massively restricting their growth.

### What does ES6+ really provide?

What is the real difference between the examples I gave above? Are the new syntax easier to read or do they provide any extra functionality?

> their suggestions have to {do} with reducing keystrokes and adding tricks that are “neat”.

I really can’t see much, if any, benefit to using destructuring or concise object syntax apart from saving keystrokes. There may be performance benefits or some special magic that I don’t know or understand but:

[None of this performance difference matters, at all! — YDKJS](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch6.md)

![Image](https://cdn-media-1.freecodecamp.org/images/FYwgy4oQHlGhVRzaeoIsZS96Uh9xO-DY5MYF)
_photo: [pixabay.com](https://pixabay.com/en/hourglass-time-hours-sand-clock-620397/" rel="noopener" target="_blank" title=")_

This quote is kind of taken out of context so I’ll explain. Suppose method X runs 1,000,000 operations/second and method Y runs 500,000 operations/second. That means that X is twice as fast as Y. **But** the difference in run time is only 1 microsecond. This is 100,000 times slower than what the human eye can perceive. So none of the performance difference matters at all!

The savings made by using different methods are probably going to be so tiny that it doesn’t matter. If you’re trying to write the fastest code possible, why are you writing it in JavaScript?

#### What ES6 also provides

Confusion, Complexity, and Options.

![Image](https://cdn-media-1.freecodecamp.org/images/GgQ1Bb9hQJ4YLtUmAEt8Cw6bS0mTzsQ5bkxR)

Later on in the discussion with Bob, he said this about JavaScript:

> You have to _decode it_ to understand what it’s doing. The syntax and semantics of the language are complex, intricate, convoluted. The programmers who debug, maintain, enhance, and revise your code the next day or a decade later will have trouble understanding it. They’ll find themselves wondering if something you did was incredibly clever or incredibly stupid.

This rung so true with me. I’ve found myself looking over code I’ve written, puzzling to figure out what I did and why I did it. While you can write complex and confusing code in any language, JavaScript gives you many opportunities to catch yourself out.

I did this to myself in the ES6 article. In the 4,000 people who read the whole article, only 5 managed to find my error before I corrected it. Which one of these is correct?

```
let person = {     name: "John",     age: 36,     job: { company: "Tesco", role: "Store Assistant"}}
```

```
function methodA({ name: driverName, age, job.company: company}){ ... }
```

```
function methodB({ name: driverName, age, job: { company }){ ... }
```

I used the wrong one and most people didn’t notice. Only the few that tried it out managed to find the error.

![Image](https://cdn-media-1.freecodecamp.org/images/rHzev1lGqapGQbzpEBx3HxLckNRfdTJOabk2)

What do these two methods really provide to justify the extra confusion and complexity? Many people could read, write and understand a function like this:

```
function methodC(person){    var driverName = person.name,        age = person.age,        company = person.job.company;    ...}
```

Yes I had to write 32 extra characters, but since most of programming is thinking, not typing, are we saving time typing only to spend more of it thinking?

It’s not just the extra time that the author spends thinking about it, it’s every person that reads that code after that point (often the author again). Complicated code has the “thinking tax” every time it’s read and we, as humans, only have a limited supply of thinking power each day.

#### Not all is bad

While this article seems to be slating ES6, there are some things that increase readability and maintainability. Promises, async functions and async/await all help to abstract the complexities of asynchronous behavior, making code more logical and easier to read. This is what I believe should be focused on, not keystroke saving tricks.

### Long-Term Effects

While this probably won’t make any difference to you as a developer, companies with lots of developers may feel the impact. Having to first understand what the syntax is doing before understanding what the code is doing results in unreliable and un-maintainable code.

This could result in JavaScript losing favor for anything that is large, complex, critical, or evolving. This would be a massive market for JavaScript to lose out on.

### Summary

* ES6 gives us even more ways to do the same task.
* You can calculate what is best, do what you want, or have a policy on it.
* ES6 gives us new tricks to save some keystrokes.
* These new tricks increase complexity and chances of error while reducing readability.
* There are some good bits of ES6, increasing readability.
* Could the increased complexity and reduced readability make companies less likely to use it in complex, critical, or constantly evolving solutions?

> What do you think? Let me know in the comments. If you enjoyed it give it a clap and follow me for more JavaScript articles.

![Image](https://cdn-media-1.freecodecamp.org/images/IlmT2dhqkBmqwHaLmF17l7Qm4pAqBmOnz-9c)

