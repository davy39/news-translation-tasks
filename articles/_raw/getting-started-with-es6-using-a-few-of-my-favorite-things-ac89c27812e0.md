---
title: Getting started with ES6 using a few of my favorite things
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T09:51:49.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-es6-using-a-few-of-my-favorite-things-ac89c27812e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TjHw7JGRxc6RQ6cG-1uEow.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Todd Palmer

  This tutorial walks you through some easy steps to get started learning the newest
  version of JavaScript: ES6.

  To get a feel for the language, we will delve into a few of my favorite features.
  Then I will provide a short list of some g...'
---

By Todd Palmer

This tutorial walks you through some easy steps to get started learning the newest version of JavaScript: **ES6.**

To get a feel for the language, we will delve into a few of my favorite features. Then I will provide a short list of some great resources for learning ES6.

### ES6 or ECMAScript 2015?

> _“What’s in a name?”_   
> _― Juliet from Shakespeare’s “Romeo and Juliet”_

The official name of the **6th Edition of ECMAScript** is **ECMAScript 2015,** as it was finalized in June, 2015. However, in general, people seem to refer to it simply as **ES6**.

Previously, you had to use a **transpiler** like [Babel](https://babeljs.io/) to even get started with ES6. Now, it seems that just about everybody except Microsoft Internet Explorer supports most of the features in ES6. To be fair, Microsoft does support ES6 in Edge. If you want more details, take a look at **kangax’s** [compatibility table](https://kangax.github.io/compat-table/es6/).

### ES6 Learning Environment

The best way to learn ES6 is to write and run ES6. There are may ways to do that. But the two that I use when I am experimenting are:

* [Node.js](https://nodejs.org)
* Babel.io’s [Try it out](https://babeljs.io/repl/) page

#### Node.js and Visual Studio Code

One of the best ways to explore the pleasantries of ES6 is to write your code in an editor like [Visual Studio Code](https://code.visualstudio.com/) and then run it in [Node.js](https://nodejs.org)

Install Visual Studio Code and create a file called `helloworld.js`. Paste the following code in:

```
console.log('Hello world');
```

Save it. It should look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qTe3mqHxVKx1TiLFQnEIwg.png)

Since version 6.5, Node.js has supported most of the ES6 standard. To run our example, open the Node.js Command Prompt to your folder where you created the `helloworld.js` file. And, just type:

```
node helloworld.js
```

Our `console.log` statement prints as output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FbpDvDA0x-1aAOapzj2WYg.png)

#### Babel.io

It isn’t as much fun as Node.js, but a convenient way to run ES6 code is the [Try it out](https://babeljs.io/repl) page on [Babel.io](https://babeljs.io/repl). Expand the **Settings** and make sure **Evaluate** is checked. Then open your browser **Console**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P23x3sFTvWnyfgLwR7kyNQ.png)
_Babel REPL_

Type the ES6 into the column on the left. Babel compiles it to plain old JavaScript. You can use `console.log` and see the output in the Web Console on the right.

### Some of My Favorite Features

> “These are a few of my favorite things.”   
> ― Maria from Rodgers and Hammerstein’s “The Sound of Music”

In this section, we will take a quick look at just a few of the new features of ES6 including:

* Using `let` and `const` instead of `var`
* Arrow functions
* Template Strings
* Destructuring

#### const and let Versus var

Now that you are coding in ES6: Stop using `var`! Seriously, never use `var` again.

From now on, use either `const` or `let`. Use `const` when you will set the value once. Use `let` when you intend to change the value.

```
let bar = { x: 'x'};const foo = { x: 'x'};
```

```
bar.x = 'other'; // This is finefoo.x = 'other'; // This is fine
```

```
bar = {}; // This is also finefoo = {}; // This will throw an error
```

Typically, I like to use `const` first. Then if it complains, I look at my code and make sure I really need to be able to modify the variable. If so, I change it to `let`.

Make sure you check out the resources later in this article for more information on `let` and `const`. You will see that they work much more intuitively than `var`.

#### Arrow Functions

Arrow functions are one of the defining features of ES6. Arrow functions are a new way to write functions. For example, the following functions work identically:

```
function oneMore(val){  return val+1;}console.log('3 and one more is:', oneMore(3));
```

```
const oneMore = (val) => val+1;console.log('3 and one more is:', oneMore(3));
```

There are a few things to remember about arrow functions:

* They automatically return the computed value.
* They have lexical `this`.

This first time I saw this I wondered, “What in the wide world is a **lexical this**? And, do I really care?” Let’s look at an example of why the lexical this is so useful and how it makes our code so much more intuitive:

In lines 1–31, we define a Class called `ThisTester`. It has two functions `thisArrowTest()` and `thisTest()` that basically do the same thing. But, one uses an arrow function and the other uses the classic function notation.

On line 33, we create an new object `myTester` based on our `ThisTester` class and call the two functions in our class.

```
const myTester = new ThisTester();console.log('TESTING: thisArrowTest');myTester.thisArrowTest();console.log('');console.log('TESTING: thisTest');myTester.thisTest();
```

In the `thisTest()` function, we see that it tries to use `this` in line 26.

```
console.log('function this fails', this.testValue);
```

But, it fails because that function gets its own `this` and it isn’t the same `this` as the class. If you think this is confusing, that’s because it is. It isn’t intuitive at all. And, new developers sometimes spend their first week fighting with `this` in callback functions and promises like I did.

Eventually, after reviewing a bunch of examples, I figured out the standard “trick” of using a variable called `self` to hold onto the `this` that we want to use. For example, in line 17:

```
let self = this;
```

However, notice how in the arrow function in line 10, we can directly access `this.testValue` and magically it works:

```
let myFunction = (x) =>console.log('arrow "this" works:', this.testValue)
```

That is **lexical this** in action. The `this` in the arrow function is the same as the `this` in the surrounding function that calls it. And hence we can intuitively use `this` to access the properties in our object like `this.testValue`.

#### Template Strings

Template Strings (sometimes called Template Literals) are an easy way to construct strings. They are great for multi line strings such as those used in Angular templates. Template Strings use the **back tick** ` instead of quote or apostrophe.

Here is an example of creating a long, multi-line string:

```
const myLongString = `This stringactually spans many lines.And, I don't even need to use any "strange"notation.`;console.log (myLongString);
```

You can easily bind variables to your string, for example:

```
const first = 'Todd', last = 'Palmer';console.log(`Hello, my name is ${first} ${last}.`)
```

Looking at that variable assignment begs the question:  
“What if I need to use the `$`, `{`, or `}` characters in my string?”

Well, the only one that needs special treatment is the sequence `${`.

```
console.log(`I can use them all separately $ { }`);console.log(`$\{ needs a backslash.`);
```

Template Strings are especially useful in [Angular](https://angular.io/) and [AngularJS](https://angularjs.org/) where you create HTML templates, because they tend to be multi-line and have a lot of quotes and apostrophes. Here is what a small example of an Angular Template leveraging the back tick looks like:

```
import { Component } from '@angular/core';
```

```
@Component({  selector: 'app-root',  template: `    <h1>{{title}}</h1>    <h2>My favorite hero is: {{myHero}}</h2>  `})export class AppComponent {  title = 'Tour of Heroes';  myHero = 'Windstorm';}
```

#### Destructuring

Destructuring lets you take parts of an object or array and assign them to your own named variables. For more information on Destructuring, check out my article on [ITNEXT](https://itnext.io/es6-destructuring-b8c50a20b46c).

### ES6 Resources

That was just a quick overview of a few of the new features in ES6. Here are some great resources for continuing your journey down the path of learning ES6:

* [Learn ES2015](https://babeljs.io/learn-es2015/) on Babel  
This is an overview of all the new features. Although it doesn’t go into much depth, this is a great page to keep as a quick reference with examples.
* [ES6 tips and tricks to make your code cleaner, shorter, and easier to read!](https://medium.freecodecamp.org/make-your-code-cleaner-shorter-and-easier-to-read-es6-tips-and-tricks-afd4ce25977c) by [Sam Williams](https://medium.freecodecamp.org/@samwsoftware)  
This is a great article in [Free Code Camp’s](https://medium.freecodecamp.org/) Medium publication.
* [MPJ](https://www.bing.com/search?q=funfunfunction)’s video series: [ES6 JavaScript Features](https://www.youtube.com/playlist?list=PL0zVEGEvSaeHJppaRLrqjeTPnCH6vw-sm)  
If you prefer videos, MPJ is your guy. Not only is he good technically, his stuff is really entertaining.
* [ES6 in Depth](https://hacks.mozilla.org/category/es6-in-depth/) series on [Mozilla Hacks](https://hacks.mozilla.org/)  
This is an excellent in depth series.
* Eric Elliott’s series [Composing Software](https://medium.com/javascript-scene/composing-software-an-introduction-27b72500d6ea)  
Read through this one for a real challenge. Be forewarned though, some of Eric’s stuff is college level Computer Science.

This article is based on a lecture I gave in March 2018.

