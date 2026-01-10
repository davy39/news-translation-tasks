---
title: How to Declare Variables in JavaScript – var, let, and const Explained
subtitle: ''
author: Furkan Emin Can
co_authors: []
series: null
date: '2023-11-07T22:16:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-variables-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: variables
  slug: variables
seo_title: null
seo_desc: 'Declaring variables is something you''ll do all the time in JavaScript.
  And if you know the variable declaration process inside and out, you''ll have the
  confidence to start writing great JS code.

  Through this article, you will learn how to declare and...'
---

Declaring variables is something you'll do all the time in JavaScript. And if you know the variable declaration process inside and out, you'll have the confidence to start writing great JS code.

Through this article, you will learn how to declare and mutate variables using `var`, `let`, and `const`, and you'll get a better understanding of the differences between them.

I will explain each concept in two parts:

* Before ES6 (`var` statement)
* After ES6 (`let` and `const` statements)

Let's dive into these different ways of declaring variables in JavaScript so you know how they work and when to use each one.

## How to Declare Variables in JavaScript

When you declare variables in your app, the interpreter moves them to the top of their scope and allocates places in the memory before the execution starts. This process is called **Hoisting**.

### 1. How to declare variables with `var` in JavaScript:

When you declare a variable with `var`, it is hoisted and initialized in the memory as `undefined` before the code execution. So, you can access the variable before declaring it, but it returns `undefined`. This is sometimes called **Declaration hoisting**.

When the execution starts and reaches the line where the variable is declared, it replaces the value in memory with the value of the variable.

```javascript
console.log(strawberry); // undefined

var strawberry = '🍓';

console.log(strawberry); // 🍓

```

Under the hood, the code above behaves like this:

```javascript
var strawberry;

console.log(strawberry); // undefined

strawberry = '🍓';

console.log(strawberry); // 🍓

```

So we can use the `strawberry` variable before the declaration, but it returns `undefined`.

With this behavior, the program runs without errors. But in some cases, this can lead to unexpected results. We are only human, and on a busy day you might try to access a variable before declaring it. In a complex program, it can be hard to figure out where a strange `undefined` comes from.

### 2. How to declare variables with `let` and `const` in JavaScript:

When you declare a variable with `let` or `const`, it is also hoisted but it's allocated in the memory as **uninitialized** in the [temporal dead zone](https://www.freecodecamp.org/news/what-is-the-temporal-dead-zone/). You cannot access variables in the temporal dead zone before you've declared them. So, if you try to access a variable before declaring it, the program throws a `ReferenceError`.

When the program reaches the line where the variable is declared, it initializes it with that value.

```javascript
console.log(cherry); // ReferenceError

const cherry = "🍒";

console.log(cherry); // 🍒

```

If you try to run this code snippet, you will see an error similar to the following one because we tried to access a variable in the temporal dead zone. 

![ReferenceError: Cannot access 'cherry' before initialization](https://www.freecodecamp.org/news/content/images/2023/10/error-1.png)
_"ReferenceError: Cannot access 'cherry' before initialization"_

This is a more predictable behavior than the behavior of the `var` statement.



### So what do `var`, `let`, and `const` have in common?

In the previous two sections, you learned the process for declaring `var`, `let`, and `const`. In this section, we will look at the common concepts.

* You can declare a variable with `let` and `var` without a value. In this case, the default value will be `undefined`.

```javascript
var tomato;
let potato;

console.log(tomato); // undefined
console.log(potato); // undefined

```

This behavior is not valid for `const` because an initial value is required for it. If there is no initial value, the program throws a `SyntaxError`.

```javascript
const avocado; // SyntaxError
```

For the code above, an error gets thrown  like this one:

!["SyntaxError: Missing initializer in const declaration"](https://www.freecodecamp.org/news/content/images/2023/11/image-4.png)
_SyntaxError: Missing initializer in const declaration_

* You can declare a chain of variables using the same statement. Put the statement at the beginning and separate each variable with a comma. This is valid for `var`, `let`, and `const`.

```javascript
let number1 = 2, number2 = 23, number3 = 99;

console.log(number1); // 2
console.log(number2); // 23
console.log(number3); // 99

```

Nowadays, to declare variables, you'll want to use the ES6 statements `let` and `const`. You can think of `var` as the legacy method of doing this.

My recommendation is:

* Use `const` as the default.
* Use `let` if the variable will change in the future.
* Don't use `var` if there is no particular use case.

## JavaScript Variables and Scope

According to [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Scope):

> The **scope** is the current context of execution in which values and expressions are "visible" or can be referenced.

In terms of variables, the scope is where certain variables are available. We can access variables that have been declared in a parent scope in a child scope, but it doesn't work the other way around.

### Global Scope

**Global Scope** is the main scope that covers all the scopes in a script. Variables declared in the global scope are available in all scopes.

```javascript
// Global Scope

const grapes = "🍇";

// Functional Scope
function logGrapes() {
  console.log(grapes); // 🍇

  // Block Scope in a Functional Scope
  {
    console.log(grapes); // 🍇
  }
}

// Block Scope
{
  console.log(grapes); // 🍇
}

```

In the example above, we can access the `grapes` variable from all child scopes because it is declared in the global scope.

### Functional Scope

**Functional scope** is the scope created with a function declaration. Variables declared in a functional scope are only available in that scope and cannot be accessed outside of it. The behavior of `var`, `let`, and `const` are the same in this case. 

Here's an example:

```javascript
// Global Scope

// Functional Scope
function createVariables() {
  var apple = "🍎";
  const cherry = "🍒";
  let strawberry = "🍓";
}

console.log(apple); // ReferenceError
console.log(cherry); // ReferenceError
console.log(strawberry); // ReferenceError

```

In the example above, all three variables are only accessible in the functional scope of the `createVariables` function. If you try to access them outside of the functional scope the program throws a `ReferenceError`.

### Block Scope

**Block scope** is the scope that is created with a pair of curly braces. Block scope is only valid for `let` and `const`, not `var`. When you declare a variable with `var` it is moved to the global scope or the nearest functional scope if it exists.

```javascript
// Block Scope
{
  const banana = "🍌";

  // Block Scope in a Block Scope
  {
    console.log(banana); // 🍌

    var carrot = "🥕";
    let lemon = "🍋";
  }

  console.log(carrot); // 🥕
  console.log(lemon); // ReferenceError
}

```

In the example above:

* We can access the `banana` variable that we declared with `const` in the parent scope in the child scope.
* We can access the `carrot` variable declared with `var` in the child scope in the parent scope because the program moves it to the global scope.
* We can't access the `lemon` variable declared with `let` in the child scope in the parent scope because it cannot be accessed outside of the scope in which it's declared. If try to do that, the program throws a `ReferenceError`.

## How to Mutate Variables in JavaScript

In this section, we'll talk about the `var` and `let` statements together, and then discuss how the `const` statement behaves. This is because the variables declared with `var` and `let` are mutable (that is, they can be changed), while variables declared with `const` are immutable.

### 1. Mutation in `var` and `let` statements

As I said, the variables declared with `var` and `let` are mutable, which means that you can assign new values to them. Here's what I mean:

```javascript
var pepper = "🌶️";
let apple = "🍏";

pepper = "🫑";
apple = "🍎";

console.log(pepper); // 🫑
console.log(apple); // 🍎

```

In the example above, we mutated the `pepper` and `apple` variables, and they were assigned new values.

### 2. Mutation in `const` statement

Variables declared with `const` are immutable. So you cannot assign new values to them once you've declared them.

```javascript
const strawberry = "🍓";

strawberry = "🍉"; // TypeError

```

If you try to run the code snippet above, the program throws an error like this:

![TypeError: Assignment to constant variable.](https://www.freecodecamp.org/news/content/images/2023/10/error-3.png)
_"TypeError: Assignment to constant variable."_

Objects are an exception for the immutability of the `const` statement because they have properties and methods, unlike [primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive).

You cannot mutate them via assignment but can mutate them via their methods and property assignment. Here's an example:

```javascript
const fruits = ["🍎", "🍐"];
const fruitEmojiMap = {
  apple: "🍎",
  pear: "🍐",
};

fruits[2] = "🍒"; // [ '🍎', '🍐', '🍒' ]
fruits.push("🍌"); // [ '🍎', '🍐', '🍒', '🍌' ]

fruitEmojiMap.cherry = "🍒"; // { apple: '🍎', pear: '🍐', cherry: '🍒' }

```

In the code example above,

* We added two new fruits to the `fruits` array via property assignment, and used the `push` method of the `Array` object.
* We added a new fruit to the `fruitEmojiMap` object via property assignment.

A little note: you can use the `[Object.freeze()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)` method to achieve complete immutability for objects.

## How to Redeclare Variables in JavaScript

Redeclaring a variable with the same name in the same scope is likely something you don't want to do intentionally, and I've never found a real use case for it.

But strangely, we can redeclare variables declared with `var` using the same name in the same scope. This is another error-prone characteristic of the `var` statement. Fortunately, this behavior was changed with the `let` and `const` statements.

### **1.** How to redeclare variables with `var`

You can redeclare a variable declared with `var` in the same scope or child-parent scopes. The variable will be affected in the global scope, or functional scope if it is declared in a function.

So even if you redeclare a variable in the child scope, the variable will change in all scopes where that variable is available.

```javascript
// Global Scope
var pepper = "🌶️";

console.log(pepper); // 🌶️

// Block Scope
{
  var pepper = "🥦";

  console.log(pepper); // 🥦
}

console.log(pepper); // 🥦

```

In the example above, we declared a new `pepper` variable in the block scope and assigned it a different value. This affects the variable in the global scope and we lose access to the previous variable.

This behavior tends to cause big problems. Because someone working in the same codebase may unintentionally declare a variable using the same name used before.

The process is a bit different if you make the redeclaration in a function. The variable outside of the function remains the same and the variable inside the function cannot affect it. As I said, variables declared with `var` in a function are in functional scope and don't affect the outside.

```javascript
// Global Scope
var onion = "🧅";

// Functional Scope
function redeclareOnion() {
  var onion = "🧄";

  console.log(onion); // 🧄
}

console.log(onion); // 🧅

```

In the example above, even though we declared a new variable using the same name as the `onion` variable inside a function, the `onion` variable declared in the global scope remained the same.

### 2. How to redeclare variables with `let` and `const`

You cannot redeclare variables declared with `let` or `const` in the same scope. If you try to do so, the program throws a `SyntaxError`.

```javascript
let eggplant = "🍆";

let eggplant = "🥔"; // SyntaxError

```

In the example above, we tried to redeclare the `eggplant` variable in the same scope, and the program threw the following error:

![SyntaxError: Identifier 'eggplant' has already been declared](https://www.freecodecamp.org/news/content/images/2023/11/image-17.png)
_"SyntaxError: Identifier 'eggplant' has already been declared"_

But you can redeclare variables using `let` and `const` in child scopes. Because the variables declared with `let` and `const` are block scope and don't affect the parent scopes.

```javascript
// Global Scope
const carrot = "🥕";

// Block Scope
{
  const carrot = "🍒";

  console.log(carrot); // 🍒
}

console.log(carrot); // 🥕

```

In the example above, we declared two `carrot` variables. The first one is in the global scope and the second one is in the block scope with a different value. The variable in the global scope remains the same and the variable in the block scope is a standalone new variable.

The downside is that we lost access to the `carrot` variable declared in the global scope, in the block scope. If we need this variable in the future we can't access the variable.

So, most of the time, it is better to declare a variable with a unique name.

### 3. How to Redeclare Variables by Mixing Statements

Briefly, you shouldn't mix statements. This section is intended to give you information rather than really show you how the process is done.

You cannot create variables by mixing statements using the same name in the same scope. If you try it, the program throws a `SyntaxError`.

```javascript
const banana = "🍌";

var banana = "🍋"; // SyntaxError

```

In the example above, we tried to redeclare the `banana` variable declared with `const` with `var`, but the program threw an error similar to the one below:

![SyntaxError: Identifier 'banana' has already been declared](https://www.freecodecamp.org/news/content/images/2023/11/image-16.png)
_"SyntaxError: Identifier 'banana' has already been declared"_

Also, you cannot declare a variable with `var` using the same name as one already declared in a parent scope using `let` or `const`. As I said, `var` is global scope and affects the variable declared in parent scopes unless it is inside a function.

```javascript
// Global Scope
let pineapple = "🍍";

// Functional Scope
function declarePineapple() {
  var pineapple = "🍏"; // This is okay
}

// Block Scope
{
  var pineapple = "🍎"; // SyntaxError
}

```

In the example above, we tried to redeclare the `pineapple` variable in two places:

* In the function, which we did successfully.
* But in the child block scope, the program threw the following error:

![SyntaxError: Identifier 'pineapple' has already been declared](https://www.freecodecamp.org/news/content/images/2023/11/image-19.png)
_"SyntaxError: Identifier 'pineapple' has already been declared"_

## Conclusion

These days, `let` and `const` are the default choice for variable declaration in JavaScript. But you might still encounter the `var` statement, especially in older apps. So you'll need to know how to handle it.

In this guide, you have learned the differences between `var`, `let`, and `const`. We also talked about hoisting and scope in variable declaration.

See you in the next one!

### Stay in Touch

You can connect with me on [Twitter](https://twitter.com/femincan), and you can read more tutorials like this one [on my blog here](https://femincan.dev).

