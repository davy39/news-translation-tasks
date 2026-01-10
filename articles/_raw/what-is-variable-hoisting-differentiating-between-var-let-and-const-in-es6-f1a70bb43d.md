---
title: A guide to JavaScript variable hoisting ? with let and const
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-19T17:28:14.000Z'
originalURL: https://freecodecamp.org/news/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0hfm3TfurQboq6KlJrG56g.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Bhuvan Malik

  New JavaScript developers often have a hard time understanding the unique behaviour
  of variable/function hoisting.

  Since we’re going to be talking about var, let and const declarations later on,
  it’s important to understand variable h...'
---

By Bhuvan Malik

New JavaScript developers often have a hard time understanding the unique behaviour of variable/function _hoisting_.

Since we’re going to be talking about `var`, `let` and `const` declarations later on, it’s important to understand _variable hoisting_ rather than _function hoisting_. Let’s dive in!

![Image](https://cdn-media-1.freecodecamp.org/images/qtdiMnLrgBGImBAMbanGKSmux1n-jjX3wOKH)

### **What is variable hoisting?**

The JavaScript engine treats all variable declarations using “`_var_`” as if they are declared at the top of a functional scope(if declared inside a function) or global scope(if declared outside of a function) regardless of where the actual declaration occurs. This essentially is “_hoisting_”.

So variables might actually be available before their declaration.

![Image](https://cdn-media-1.freecodecamp.org/images/kdtsq45xrgSooJlUgu3ArT4FiRvuzItcwqlX)

Let’s see it in action..

```
// OUTPUT : undefinedconsole.log(shape);
```

```
var shape = "square";
```

```
// OUTPUT : "square"console.log(shape);
```

If you’re coming from C-based languages, you’d expect an error to be thrown when the first `console.log` is called since the variable `shape` hadn’t been defined at that point. But the JavaScript interpreter looks ahead and “hoists” all variable declarations to the top, and the initialization remains in the same spot.

Here’s what is happening behind the scenes:

```
//declaration getting hoisted at the topvar shape;
```

```
// OUTPUT : undefinedconsole.log(shape);
```

```
shape = "square";
```

```
// OUTPUT : "square"console.log(shape);
```

Here is another example this time in a functional scope to make things more clear:

```
function getShape(condition) {    // shape exists here with a value of undefined
```

```
    // OUTPUT : undefined    console.log(shape);
```

```
    if (condition) {        var shape = "square";        // some other code        return shape;    } else {        // shape exists here with a value of undefined        return false;    }}
```

You can see in the above example how `shape`’s declaration is hoisted at the top of `getShape()` function. This is because if/else blocks don’t create a local scope as seen in other languages. A local scope is essentially function scope in JavaScript. Therefore, shape is accessible everywhere outside the `if` block and within the function with an ‘_undefined’_ value.

This default behaviour of JavaScript has its fair share of advantages and disadvantages. Not fully understanding these can lead to subtle but dangerous bugs in our code.

### **Enter Block-Level Declarations!**

![Image](https://cdn-media-1.freecodecamp.org/images/dboQXJ3XAiw2IMLMsf8tfhv4SeXXnQaE3FOX)

ES6 introduced block-level scoping options to provide developers with more control and flexibility over a variable’s lifecycle.

Block-level declarations are made in block/lexical scopes that are created inside a block “{ }”.

#### let Declarations

This syntax is similar to `var`, just replace `var` with `let` to declare a variable with its scope being only that code block.

Place your `let` declarations at the top in a block so they’ll be available within that entire block.

For example:

```
function getShape(condition) {// shape doesn't exist here
```

```
// console.log(shape); =&gt; ReferenceError: shape is not defined
```

```
if (condition) {        let shape = "square";        // some other code        return shape;    } else {        // shape doesn't exist here as well        return false;    }}
```

Notice how shape exists only inside the `if` block, and throws an error when accessed outside of it instead of outputting `undefined` like our previous case with `var` declarations.

**NOTE** : If an identifier has already been defined inside a scope with `var`, using that same identifier in a `let` declaration inside the same scope throws an error.  
Also, no error is thrown if a `let` declaration creates a variable with the same name as that of a variable in it’s outer scope. (This case is same with `const` declarations which we’ll talk about shortly.)

For example:

```
var shape = "square";let shape = "rectangle";
```

```
// SyntaxError: Identifier 'shape' has already been declared
```

and:

```
var shape = "square";if (condition) {    // doesn't throw an error    let shape = "rectangle";    // more code }// No error
```

### const Declarations

The declaration syntax is similar to `let` & `var` , lifecycle is the same as `let`. But you have to follow some rules.

Bindings declared using `const` are treated as **constants**, and therefore **they cannot be re-assigned values once defined**. Due to this, every `const` declaration **must be initialized** at the time of declaration.

For example:

```
// valid const shape = "triangle";
```

```
// syntax error: missing initializationconst color;
```

```
// TypeError: Assignment to constant variableshape = "square"
```

**However**, an object’s properties can be modified!

```
const shape = {    name: "triangle",    sides: 3}
```

```
// WORKSshape.name = "square";shape.sides = 4;
```

```
// SyntaxError: Invalid shorthand property initializershape = {    name: "hexagon",    sides: 6}
```

In the above example we can see that only the properties of the `shape` object could be changed because we are only changing what `shape` contains, not what it’s bound to.

We can summarize by saying that `const` prevents modification of the binding as a whole — not the value that it’s bound to.

Note: Properties can be mutated. So for true immutability, use Immutable.js or Mori.

### The Temporal Dead Zone

We now know that accessing `let` or `const` variables before they’re declared will throw a `ReferenceError`. This period between entering scope and being declared where they cannot be accessed is called the Temporal Dead Zone.

Note that “Temporal Dead Zone” isn’t formally mentioned in the ECMAScript specification. It’s just a popular term amongst programmers.

![Image](https://cdn-media-1.freecodecamp.org/images/VGX7QSdndFKi23EHHNbrYUD4LDtTPMwxn4bf)

I personally recommend you always use `const`, as it leads to fewer bugs. I have yet to encounter a situation where I needed to use `var`.

As a general rule, use `let` only for loop counters or only if you really need reassignment. Everywhere else, use `const`. Personally I’ve ditched loops for filter(), map() & reduce(). You should too.

**Be sure to check out the part 2 for this on Function Hoisting and important interview questions related to the topic of hoisting in JS.**

[**Function Hoisting & Hoisting Interview Questions**](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)  
[_This is a part 2 for my previous article on Variable Hoisting titled “A guide to JavaScript variable hoisting ? with…m_edium.freecodecamp.org](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)

Click [here](https://medium.com/@bhuvanmalik/es6-functions-9f61c72b1e86) for my article on some of the useful new features in ES6 related to functions.

See you next time. Peace! ✌️️

