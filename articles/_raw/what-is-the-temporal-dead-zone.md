---
title: What is the Temporal Dead Zone (TDZ) in JavaScript?
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2020-10-06T22:36:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-temporal-dead-zone
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/What-is-the-Temporal-dead-zone_.png
tags:
- name: JavaScript
  slug: javascript
- name: variables
  slug: variables
seo_title: null
seo_desc: 'I know Temporal Dead Zone sounds like a sci-fi phrase. But it''s helpful
  to understand what the terms and concepts you work with everyday (or want to learn
  about) mean.

  Strap in, because this gets complicated.

  Are you aware that in JavaScript we can a...'
---

I know Temporal Dead Zone sounds like a sci-fi phrase. But it's helpful to understand what the terms and concepts you work with everyday (or want to learn about) mean.

Strap in, because this gets complicated.

Are you aware that in JavaScript we can add `{ }` to add a level of scope wherever we want?

So we could always do the below:

```js
{ { { { { { var madness = true } } } } } }
```

I've included this detail to make sure that the upcoming examples makes sense (as I didn't want to assume that everyone knew it).  
  
Before ES6 there was no other way to declare variables other than `var`. But ES6 brought us `let` and `const`.

`let` and `const` declarations are both block-scoped, which means they are only accessible within the `{` `}` surrounding them. `var`, on the other hand, doesn't have this restriction.

Here's an example:

```javascript
let babyAge = 1;
let isBirthday = true;

if (isBirthday) {
	let babyAge = 2; 
}

console.log(babyAge); // Hmmmm. This prints 1
```

The above has occurred because the re-declaration of `babyAge` to 2 is only available inside the `if` block. Beyond that, the first `babyAge` is used. Can you see that they are two different variables?

In contrast, the `var` declaration has no block scope:

```js
var babyAge = 1;
var isBirthday = true;

if (isBirthday) {
	var babyAge = 2; 
}

console.log(babyAge); // Ah! This prints 2
```

The final salient difference between `let` / `const` and `var` is that if you access `var` before it's declared, it is undefined. But if you do the same for `let` and `const`, they throw a `ReferenceError`.

```javascript
console.log(varNumber); // undefined
console.log(letNumber); // Doesn't log, as it throws a ReferenceError letNumber is not defined

var varNumber = 1;
let letNumber = 1;
```

They throw the error all because of the Temporal Dead Zone.

## Temporal Dead Zone explained

This is what the TDZ is: the term to describe the state where variables are un-reachable. They are in scope, but they aren't declared.

The `let` and `const` variables exist in the TDZ from the start of their enclosing scope until they are declared.

You could also say that the variables exist in the TDZ from the place they get bound (when the variable gets bound to the scope it's inside) until it is declared (when a name is reserved in memory for that variable).

```javascript
{
 	// This is the temporal dead zone for the age variable!
	// This is the temporal dead zone for the age variable!
	// This is the temporal dead zone for the age variable!
 	// This is the temporal dead zone for the age variable!
	let age = 25; // Whew, we got there! No more TDZ
	console.log(age);
}
```

You can see above that if I accessed the age variable earlier than its declaration, it would throw a `ReferenceError`. Because of the TDZ. 

But `var` won't do that. `var` is just default initialized to `undefined` unlike the other declaration.

## What's the difference between declaring and initialising?

Here is an example of declaring a variable and initialising a variable.

```javascript
function scopeExample() {

    let age; // 1
    age = 20; // 2
    let hands = 2; // 3
}
```

Declaring a variable means we reserve the name in memory at the current scope. That is labelled 1 in the comments.

Initialising a variable is setting the value of the variable. That is labelled 2 in the comments.

Or you could always do both on one line. That is labelled 3 in the comments.

Just to repeat myself again: the `let` and `const` variables exist in the TDZ from the start of their enclosing scope until they are declared.

So from the above code snippet, where is the TDZ for `age`? Also, does `hands` have a TDZ? If so, where is the start and end of the TDZ for hands?

<details>
<summary>Check your answer</summary> 
The hands and age variables both enter the TDZ.
<br> <br>
The TDZ for hands ends when it gets declared, the same line it gets set to 2. 
<br> <br>  
The TZ for age ends when it gets declared, and the name reserved in memory (in step 2, where I commented).
</details>

## Why is the TDZ created when it is?

Let's go back to our first example:

```
{
    // This is the temporal dead zone for the age variable!
    // This is the temporal dead zone for the age variable!
    // This is the temporal dead zone for the age variable!
    // This is the temporal dead zone for the age variable!
    let age = 25; // Whew, we got there! No more TDZ
    console.log(age);
}
```

If we add a `console.log` inside the TDZ you will see this error:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-5.png)

Why does the TDZ exist between the top of the scope and the variable declaration? What's the specific reason for that?

**It's because of hoisting.**

The JS engine that is parsing and executing your code has 2 steps to do:

1. Parsing of the code into an Abstract Syntax Tree/executable byte code, and
2. Run time execution.

Step 1 is where hoisting happens, and this is done by the JS engine. It essentially will move all your variable declarations to the top of their scope. So an example would be:

```js
console.log(hoistedVariable); // undefined
var hoistedVariable = 1;
```

To be clear, these variables aren't physically moving in the code. But, the result would be functionally identical to the below:

```js
var hoistedVariable;

console.log(hoistedVariable); // undefined
counter = 1;
```

The only difference between `const` and `let` is that when they are hoisted, their values don't get defaulted to `undefined`.

Just to prove `let` and `const` also hoist, here's an example:

```js
{
    // Both the below variables will be hoisted to the top of their scope!
	console.log(typeof nonsenseThatDoesntExist); // Prints undefined
	console.log(typeof name); // Throws an error, cannot access 'name' before initialization

	let name = "Kealan";
}
```

The above snippet is proof that `let` is clearly hoisted above where it was declared, as the engine alerts us to the fact. It knows `name` exists (it's declared), but we can't access it before it is initialized.

If it helps you to remember, think of it like this.

When variables get hoisted, `var` gets `undefined` initialized to its value by default in the process of hoisting. `let` and `const` also get hoisted, but don't get set to `undefined` when they get hoisted. 

And that's the sole reason we have the TDZ. Which is why it happens with `let` and `const` but not `var`.

## More examples of the TDZ

The TDZ can also be created for default function parameters. So something like this:

```js
function createTDZ(a=b, b) {
}

createTDZ(undefined, 1); 
```

throws a `ReferenceError`, because the evaluation of variable `a` tries to access variable `b` before it has been parsed by the JS engine. The function arguments are all inside the TDZ until they are parsed.

Even something as simple as `let tdzTest = tdzTest;` would throw an error due to the TDZ. But `var` here would just create `tdzTest` and set it to `undefined`.

There's one more final and [fairly advanced example](https://github.com/google/traceur-compiler/issues/1382#issuecomment-57182072) from Erik Arvindson (who's involved in evolving and maintaining the ECMAScript spec):

```javascript
let a = f(); // 1
const b = 2;
function f() { return b; } // 2, b is in the TDZ

```

You can follow the commented numbers. 

In the first line we call the `f` function, and then try to access the `b` variable (which throws a `ReferenceError` because `b` is in the TDZ).

## Why do we have the TDZ?

Dr Alex Rauschmayer has an excellent [post](https://2ality.com/2015/10/why-tdz.html) on _why_ the TDZ exists, and the main reason is this:

It helps us catch errors. 

To try and access a variable before it is declared is the wrong way round, and shouldn't be possible.

It also gives more expected and rational semantics for `const` (because `const` is hoisted, what happens if a programmer tries to use it before it is declared at runtime? What variable should it hold at the point when it gets hoisted?), and was the best approach decided by the ECMAScript spec team.

## How to avoid the issues the TDZ causes

Relatively simply, always make sure you define your `let`s and `const`s at the top of your scope.


