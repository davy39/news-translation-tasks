---
title: What is Hoisting in JavaScript | Hoisting Functions, Variables and Classes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-28T14:54:11.000Z'
originalURL: https://freecodecamp.org/news/what-is-hoisting-in-javascript-3
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/27-hoisting.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  Hoisting is a concept or behavior in JavaScript where the declaration of a function,
  variable, or class goes to the top of the scope they were defined in. What does
  this mean?

  Hoisting is a concept you may find in some programming l...'
---

By Dillion Megida

Hoisting is a concept or behavior in JavaScript where the declaration of a function, variable, or class goes to the top of the scope they were defined in. What does this mean?

Hoisting is a concept you may find in some programming languages (such as JavaScript) and not in others. It's a special behavior of the JavaScript interpreter. We'll learn about how it works in this article.

Let's start with functions.

I have a [video version of this topic](https://youtu.be/o8kXXjZdpqg) which you can check out.

## Function Hoisting

Take a look at this code example:

```js
function printHello() {
  console.log("hello")
}

printHello()
// hello
```

Here, we declare `printHello`, and we execute the function just after the line it was declared. No errors; everything works!

Now look at this example:

```js
printHello()
// hello

function printHello() {
  console.log("hello")
}
```

Here, we execute `printHello` before the line the function was declared. And everything still works without errors. What happened here? **Hoisting**.

Before the interpreter executes the whole code, it first hoists (raises, or lifts) the declared function to the top of the scope it is defined in. In this case, `printHello` is defined in the global scope, so the function is hoisted to the top of the global scope. Through hoisting, the function (including the logic) becomes accessible even before the line it was declared in the code.

Let's see another example:

```js
printHello()
// hello

printDillion()
// ReferenceError: printDillion is not defined

function printHello() {
  console.log('hello')

  function printDillion() {
    console.log("dillion")
  }
}
```

As you see here, we declare `printHello`. In this function, we first execute `console.log('hello')` then we declare another function called `printDillion` which executes `console.log('dillion')` when called.

Before `printHello` is declared in the code, we try to access it by executing `printHello()`. It's accessible (since it is hoisted to the top of the global scope), so we have "hello" printed on the console.

But then we try to access `printDillion`, and we get a reference error: **printDillion is not defined**. Does hoisting not occur on `printDillion`?

`printDillion` is hoisted, but it is only lifted to the top of the scope it was declared in. In this case, it is declared in a local scope--in `printHello`. Therefore, it would only be accessible in the function. Let's update our code:

```js
printHello()
// hello

function printHello() {
  printDillion()
  // dillion

  console.log('hello')

  function printDillion() {
    console.log("dillion")
  }
}
```

Now, we execute `printDillion` in `printHello` before the line where `printDillion` was actually declared. Since the function is hoisted to the top of the local scope, we're able to access it before the line where it was actually declared.

Hoisting makes all these possible for function declarations. But, it's also worth noting that **hoisting does not occur on function expressions**. I explained the reason for this here: [Function Declarations vs Function Expressions](https://www.freecodecamp.org/news/function-declaration-vs-function-expression/)

Now let's look at hoisting for variables.

## Variable Hoisting

You can declare variables in JavaScript with the `var`, `let`, and `const` variables. And these variable declarations would be hoisted, but behave differently. Let's start with `var`.

### Hoisting `var` variables

Take a look at this example:

```js
console.log(name)
// undefined

var name = "Dillion"
```

Here, we declare a variable called `name` with a string value of "Dillion". But, we try to access the variable before the line it was declared. But we don't get any errors. **Hoisting happened**. The `name` declaration is hoisted to the top, so the interpreter "knows" that there is a variable called `name`. If the interpreter did not know, you would get **name is not defined**. Let's try it out:

```js
console.log(name)
// ReferenceError: name is not defined

var myName = "Dillion"
```

We have a variable called `myName` but no `name`. We get the **name is not defined** error when we try to access `name`. The interpreter "does not know" about this variable.

Coming back to our example above:

```
console.log(name)
// undefined

var name = "Dillion"
```

Although hoisting happened here, the value of `name` is undefined when we access it before the line of declaration. With variables declared `var`, the variable declaration is hoisted but with a default value of `undefined`. The actual value is initialized when the declaration line is executed.

By accessing the variable after that line, we get the actual value:

```
console.log(name)
// undefined

var name = "Dillion"

console.log(name)
// Dillion
```

Let's say we declared `name` in a function:

```js
print()

console.log(name)
// ReferenceError: name is not defined

function print() {
  var name = "Dillion"
}
```

Here, we get a reference error: **name is not defined**. Remember, variables are hoisted but **only to the top of the scope they were declared in**. In this case, `name` is declared in `print`, so it will be hoisted to the top of that local scope. Let's try to access it in the function:

```js
print()

function print() {
  console.log(name)
  // undefined

  var name = "Dillion"
}
```

By trying to access `name` in the function, even though it's above the line of declaration, we do not get an error. That's because `name` is hoisted, but don't forget, **with a default value of `undefined`**.

### Hoisting `let` variables

Although variables declared with `let` are also hoisted, they have a different behavior. Let's see an example:

```js
console.log(name)
// ReferenceError: Cannot access 'name' before initialization

let name = "Dillion"
```

Here, we get a reference error: **Cannot access 'name' before initialization**. Do you notice that the error does not say **name is not defined**? That's because the interpreter is "aware" of a `name` variable because the variable is hoisted.

"Cannot access 'name' before initialization" occurs because variables declared with `let` do not have a default value when hoisted. As we saw in `var`, the variables have a default value of `undefined` until the line where the declaration/initialization is executed. But with `let`, the variables are uninitialized.

The variables are hoisted to the top of the scope they are declared in (local, global, or block), but are not accessible because they have not been initialized. This concept is also referred to as the [Temporal Dead Zone](https://dillionmegida.com/p/temporal-dead-zone-in-javascript).

They can only be accessible after the initialization line has been executed:

```js
let name = "Dillion"

console.log(name)
// Dillion
```

By accessing `name` after the line it was declared and initialized, we get no errors.

### Hoisting `const` variables

Just like `let`, variables declared with `const` are hoisted, but not accessible. For example:

```js
console.log(name)
// ReferenceError: Cannot access 'name' before initialization

const name = "Dillion"
```

The same concept of a **temporal dead zone** applies to `const` variables. Such variables are hoisted to the top of the scope they are defined in (local, global, or block), but they remain inaccessible until the variables are initialized with a value.

```js
const name = "Dillion"

console.log(name)
// Dillion
```

By accessing the variable after it has been initialized with a value (as you see above), everything works fine.

Moving onto hoisting for classes.

## Class Hoisting

Classes in JavaScript are also hoisted. Let's see an example:

```js
const Dog = new Animal("Bingo")
// ReferenceError: Cannot access 'Animal' before initialization

class Animal {
  constructor(name) {
    this.name = name
  }
}
```

Here, we declare a class called `Animal`. We try to access this class (instantiate a `Dog` object) before it was declared. We get a reference error: **Cannot access 'Animal' before initialization**. What does this error remind you of?

Just like `let` and `const` variables, classes are hoisted to the top of the scope they are defined in, but inaccessible until they are initialized. We do not get "Animal is not defined", which shows that the interpreter "knows" that there is an `Animal` class (due to hoisting). But we cannot access that class until the line of initialization is executed.

Let's update the code:

```js
class Animal {
  constructor(name) {
    this.name = name
  }
}

const Dog = new Animal("Bingo")

console.log(Dog)
// { name: 'Bingo' }
```

After `Animal` has been initialized, it becomes accessible, so we can instantiate the `Dog` object from the class without errors.

## Wrap Up

In some codebases, you may find a code similar to this:

```js
function1()
function2()
function3()

// lines of code
// lines of code

function function1() {...}
function function2() {...}
function function3() {...}
```

The three functions here are called at the top but actually declared in the code at the bottom. This is possible, due to hoisting. The functions are hoisted to the top of the global scope (which is where they were defined) together with their logic, so they become accessible/executable even before the line they were defined.

It's different for the others. `var` variables are hoisted but with a default value of `undefined`. `let` and `const` variables, and classes are hoisted but inaccessible as they do not have a default initialization.

If you enjoyed this piece, please share it with others 🙏🏾


