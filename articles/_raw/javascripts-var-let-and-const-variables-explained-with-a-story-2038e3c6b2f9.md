---
title: JavaScript’s var, let, and const variables explained with a story
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T23:17:21.000Z'
originalURL: https://freecodecamp.org/news/javascripts-var-let-and-const-variables-explained-with-a-story-2038e3c6b2f9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ikou8bbQjbVnRyjh
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Prarthana S. Sannamani

  In this article, we will explore the history of var in JavaScript, the need for
  let and const, and the differences between them.

  This post consists of two sections: Fictional piece and Technical explanation.

  The fictional pi...'
---

By Prarthana S. Sannamani

In this article, we will explore the history of `var` in JavaScript, the need for `let` and `const`, and the differences between them.

This post consists of two sections: Fictional piece and Technical explanation.

The fictional piece is intended to ease beginners into the concepts, but several parts are simplified and do not always present an accurate 1:1 analogy.

Let’s start!

### A tale of three variables

JavaScript town was a bustling town beside the sea with a commercial district filled with high rise buildings.

Since time immemorial, the residents of JavaScript town used `Vary` boxes to store their valuables, especially their prized gold marbles. To do so, the residents had two options:

1. They could place the gold marbles directly in the box (pass by value)
2. If they had a large number of gold marbles so that they would not fit in the box, they could place a special piece of paper in the box, which indicated where they had stored them. For example, the piece of paper could say “second drawer in the storage cabinet” (pass by reference)

Since the town prided itself on law and order, they set up several rules and procedures.

#### **_Rules for shops_**

1. To maintain the serenity of the town, shops could be built only on hills (functions create their own local scope)
2. The only exception to Rule 1 was the special shop at sea level (global scope).
3. A shop could have inner shops to help cover the rent (nested functions). However, each inner shop was required to be on a higher hill than the landlord shop’s hill (local function scope).
4. A shop could have “special offer” counters, such as “`If` you are over 20 years old, buy a special box here.” And “`For` (every) child `of` your family, buy a kid’s box here” (other blocks such as `if` and loops).
5. Each shop was required to have a “declaration-initialization” counter with a guard at the entrance, who maintained a registration log book (hoisting at the top of corresponding scope).
6. Each shop could have unlimited “assignment” counters with a shop assistant, who would place a resident’s gold marbles in the box.

#### Rules for box market regulation

1. The boxes could be purchased only from the sea level special shop or from a shop on the hills (variable can have global or local scope).
2. At the sea level or on any hill, residents could own ONLY a single colored `Vary` box (duplicate identifiers not allowed).
3. The `Vary` box could never be empty from the moment it was created. It had to contain cotton (`undefined`) or gold marbles at all times (effect of hoisting).
4. Once a resident exited a shop (and hence, descended the hill), all boxes they purchased in it disappeared (end of variable’s scope).

#### Procedure for residents to buy the `Vary` boxes

We will follow the journey of a resident, John, in this article.

1. John enters the shop and declares what color of `Vary` box he desires to buy at the “declaration-initialization” counter. The guard notes this in his registration book.
2. The guard conjures the colored `Vary` box, fills it with cotton and hands it to John.
3. John gets a ticket for his turn and when it arrives, he heads to the “assignment” counter. Until then, he can hold his box but cannot place his gold marbles in it.
4. At the counter, John hands over his box and gold marbles to the shop assistant, who removes the cotton, places the gold marbles inside and hands it back to him.

Naturally, these rules brought along peculiar problems.

1. With long waiting times for the “assignment” counter, John would forget that he had not placed his gold marbles in his box yet. He would open it to brag to his friends and find only cotton. Bummer!
2. Often, John would forget that he had already bought a certain colored box in a shop and newly register for the same colored box again. This would instantly result in the disappearance of his existing box (and gold marbles!!), followed by the guard conjuring a new box filled with cotton. No warning! This was especially prevalent at the “special offers” counters.

You can imagine how frustrating this situation was. With the residents of JavaScript town losing their marbles, the Town Council decided to take action.

In a grand Town Meeting in 2015, they proudly introduced two new boxes: `Lety` and `Consty`.

They also introduced the other major change: the removal of “special offer” counters from `Lety` and `Consty` shops. Instead, these counters were upgraded to inner shops, which were built on a hill inside the shop.

#### Rules for purchasing `Lety` and `Consty` boxes

1. John enters the shop and declares what type and color of box he desires to buy at the “declaration” counter. The guard notes this in his registration book. This information hazily appears on the huge wall clock, which can be seen, but not used, and is referred to as the “temporal dead zone”.
2. John gets a ticket for his turn. **Since the box is not created at declaration, it is not available for use.**

This is where `Lety` and `Consty` purchase rules diverge.

#### `Lety` rules:

1. Once John’s turn arrives, he heads to the “initialization” counter.
2. At the counter, John has the choice to buy an empty `Lety` box, or buy a `Lety` box and have his gold marbles placed inside it immediately.
3. Depending on his choice, the shop assistant conjures the `Lety` box, and fills it with cotton or hands it over to the “assignment” counter, where John’s gold marbles are placed inside it.

#### `Consty` rules

`Consty` boxes are **extremely** special. Lined with a layer of gold inside and sealed with a lock, these boxes are so dear to the shop assistants that they refuse to sell them without knowing what exactly will be placed in them.

1. Once John’s turn arrives, he heads to the “initialization-assignment” counter.
2. John is **required** to hand over his gold marbles to the shop assistant, who conjures the colored `Consty` box, places the gold marbles inside, and **locks the box forever**.

If you remember, John could directly place his gold marbles in the box or place a special piece of paper which indicated the location of his gold marbles.

1. If he places his gold marbles inside the `Consty` box, he cannot add or remove them anymore. They are locked forever.
2. However, if he places the special piece of paper, it is a little different. While he cannot **replace** the paper, he can add or remove his gold marbles at the location he has specified on the paper.

Let’s go back to the peculiar problems that prompted the invention of `Lety` and `Consty` boxes, and decide if they are resolved.

> With long waiting times for the “assignment” counter, John would forget that he had not placed his gold marbles in his box yet. He would open it to brag to his friends and find only cotton. Bummer!

Since `Lety` and `Consty` boxes are not created until John heads over to the “initialization” or ”initialization-assignment” counter, respectively, he knows he does not have the box, and thus, does not try to use it. Even if he does, loud alarms installed in the shops start ringing to alert him of the fact.

> Often, John would forget that he had already bought a certain colored box in a shop and newly register for same colored box again. This would instantly result in the disappearance of his existing box (and gold marbles!!), followed by the guard conjuring a new box filled with cotton. No warning! This was especially prevalent at the “special offers” counters.

This is handled by the removal of the “special offers” counters and the introduction of the below rule:

**_Once a resident registers for a certain colored box at the “declaration”desk in the `Lety` or `Consty` shops, he cannot re-register for the same colored box anymore in that shop! If he does, loud alarms will start blaring._**

These wonderful new boxes and rules bought peace and serenity to JavaScript Town once again, and everyone lived happily ever after.

### Diving into the technical details

Let’s go over the technical aspects of `var`, `let` and `const` to understand the story.

If you are unfamiliar with hoisting and scope (function-level and block-level), I recommend that you read my previous article [**here**](https://codeburst.io/hoist-your-knowledge-of-javascript-hoisting-59b73124b430)**.**

Here is an extract to understand the hills analogy I have used above:

> To increase our understanding of block level and function level scope, let us consider the analogy of hills. Assume that global scope is the land at sea level and local scopes are hills. If you stand on top of a hill, you can see (access) variables below your altitude. However, if you are sea level, you cannot see (access) variables at a higher altitude.

> In C++, every block `{}` results in the formation of a new hill (local scope), at an altitude one level higher than the one it is enclosed in. Nested blocks result in multi-level hills.

> In JavaScript, only a function results in the formation of a new hill (local scope). Other blocks such as `if` blocks are present on the same altitude.

> Therefore, if a variable is declared on a certain hill (block), it can be accessed from that hill (block) and all hills (blocks) above it.

### Life cycle of a variable

**Declaration Phase**: Registration of a variable in its scope, which can be global/function/block scope. In this phase, no memory is allocated yet.

**Initialization Phase**: Allocation of memory for the variable, where a binding is created, and the variable is initialized with `undefined`.

**Assignment Phase**: Assignment of a value to the variable.

It is important to note that variable declaration and declaration phase are not the same!

A variable declaration is a statement such as `var a`.

The declaration phase is a step carried out by the JavaScript compiler. In this step, when the compiler encounters a variable declaration, it declares/registers it in its corresponding scope (if the declaration does not already exist). Later on, the code generated by the compiler is executed by the JavaScript engine.

### var

1. global scope or function scope
2. value can be updated
3. can be re-declared
4. hoisted: registered in the scope, and initialized with `undefined`

Below is a simple example where we initialize a variable, update its value, and re-declare it.

```
// Hoistedconsole.log(a); // undefined
```

```
var a = 10;console.log(a); // 10
```

```
a = 20; // value updated: OKconsole.log(a); // 20
```

```
var a = 30; // re-declared: OKconsole.log(a); // 30
```

At the top of the scope, all variables are declared in their corresponding scope and initialized with a value of `undefined`. Registration and initialization are coupled. Thus, variable `a` is available for use from the top of the scope. So when we try to access the value of `a` before it is declared, it does not throw an error. Rather, `undefined` is printed. This is known as variable hoisting.

Below is an example that shows the function scope of `var`.

```
function outerFunc() {  var a = 10;  if (a > 5) {    var a = 20;    console.log(a); // 20  }  console.log(a); // 20}
```

Variable `a` is initially declared in the scope of `outerFunc`. Since the `if` block does not create a new scope, when we re-declare variable `a`, the earlier variable `a` gets wiped away and a new variable `a` gets created with a value of `20`.

Accidental re-declaration of `var` variables is a common mistake developers make due to silent re-declaration and confusion in understanding function scope.

### let

1. block scoped
2. value can be updated
3. cannot be re-declared
4. hoisted but not initialized

Below is a simple example where we initialize a variable, update its value, and try to re-declare it.

```
console.log(a); //   ReferenceError: a is not defined
```

```
let a = 10;console.log(a); // 10
```

```
a = 20;console.log(a); // 20
```

```
let a = 30; // SyntaxError: Identifier 'a' has already been declared
```

Updating a `let` variable is allowed. However, if you try to re-declare it, you encounter a `SyntaxError`. This protects developers from silent and accidental re-declaration of variables.

Are `let` variables hoisted?

This is a tricky question. The internet is divided on this: there are arguments for both sides. Some developers believe that `let` (and `const`) variables are not hoisted, because they cannot be accessed before their declaration statement is reached, unlike `var`. However, this answer really depends on your definition of hoisting. If hoisting is the coupling of the declaration and initialization phases of a variable at the top of its corresponding scope, then `let` and `const` variables are not hoisted.

However, after reading several opinions and not being any closer to the truth, I decided to go with MDN’s definition of hoisting.

> `let` bindings are created at the top of the (block) scope containing the declaration, commonly referred to as "hoisting". (MDN)

According to this definition, the answer to our question is yes. `let` variables are hoisted, but they are not initialized with `undefined`. Thus, they exist in a time period called the “Temporal Dead Zone” from the start of the block until their definition is evaluated. Trying to access them in TDZ throws a `ReferenceError`, as seen in the example.

Below is an example that shows block scope of `let`.

```
function outerFunc() {  let a = 10;  if (a > 5) {    let a = 20;    console.log(a); // 20  }  console.log(a); // 10}
```

The first declaration of variable `a` is in the scope of `outerFunc`. The `if` block creates a new scope, and when we make the second declaration of variable `a`, it gets registered in the new scope. This is independent from the `outerFunc` scope. Hence, a separate variable `a` is created, and we can observe that changes to the inner variable `a` do not affect the outer variable `a`.

This allows developers to easily create temporary variables inside condition and looping blocks, without having to search if the variable already exists in the function.

### const

1. block scoped
2. binding is immutable (but value may or may not be changed)
3. cannot be re-declared
4. hoisted but not initialized

Below is a simple example where we initialize a variable, try to update its value, and try to re-declare it.

```
console.log(a); //  ReferenceError: a is not defined
```

```
const a = 10;console.log(a); // 10
```

```
a = 20; // TypeError: Assignment to constant variable.
```

```
const a = 30; // SyntaxError: Identifier 'a' has already been declared
```

```
const b; // SyntaxError: Missing initializer in const declaration
```

Similar to `let` variables, `const` variables are hoisted, but not initialized with `undefined`. Trying to access them in the Temporal Dead Zone throws a `ReferenceError`.

If we try to initialize a `const` variable without an assignment, as in the example above for `const b;` , we encounter a `SyntaxError: Missing initializer in const declaration`. Similarly, we cannot re-declare `const` variables. It leads to a `SyntaxError`.

Let’s temporarily hold off our discussion of updating `const` variables.

Below is an example of block level scope of `const` variables:

```
function outerFunc() {  const a = 10;  if (a > 5) {    const a = 20;    console.log(a); // 20  }  console.log(a); // 10}
```

The above behavior is similar to `let` variables, where a new scope is created for the `if` block, and hence, changes to the inner variable `a` do not affect the outer variable `a`.

Let’s return to the discussion of updating `const` variables.

There is a common misunderstanding that `const` variables hold constant values, and cannot ever be updated. However, `const` works differently.

After the initial assignment, the **binding** of `const` variables is **immutable**., and therefore, the **reference** to what is stored inside the `const` variable cannot be modified. In the simplest terms, this means you cannot have a statement with **just** the `const` variable on the left hand side, followed by an equal sign `=` , and a new value on the right hand side.

However, whether the value can be updated depends on what is stored in it. Let’s consider the two cases:

1. Primitive data type: Boolean, Null, Undefined, Number, String, Symbol
2. Objects

If a variable is assigned a primitive data type, the data type gets passed by **value**. Hence, if we have a statement `let x = 10` , we can visualize `x` containing the Number `10`.

If a variable is assigned an object, the object is passed by **reference**. Hence, if we have a statement `let x = [1,2,3]`, `x` does not contain the array `[1,2,3]` . Instead, it contains a reference (address) of where the array `[1,2,3]` is stored in memory after its creation. Hence, we can visualize `x` containing an address such as `5274621`.

Let’s see examples from primitive and object data types:

```
// Booleanconst a = true;a = false; // TypeError: Assignment to constant variable.
```

```
// Nullconst b = null;b = 10; // TypeError: Assignment to constant variable.
```

```
// Undefinedconst c = undefined;c = 10; // TypeError: Assignment to constant variable.
```

```
// Numberconst d = 50;d = 100; // TypeError: Assignment to constant variable.
```

```
// Stringconst e = 'hello';e = 'world'; // TypeError: Assignment to constant variable.
```

```
// Symbolconst f = Symbol('foo');f = 100; // TypeError: Assignment to constant variable.
```

As we can see above, trying to update the value of any primitive data type results in a `TypeError`.

```
/* Arrays are stored by reference.Hence, although the binding is immutable, the values are not. */
```

```
const c = [1,2,3];
```

```
c.push(10); // No errorconsole.log(c); // [1,2,3,10]
```

```
c.pop(); // No errorconsole.log(c); // [1,2,3]
```

```
c = [4,5,6]; // TypeError: Assignment to constant variable.
```

As we can see above, we can push and pop items from the array since this only modifies the contents of what the `const` variable is pointing to, but does not try to overwrite the contents of the `const` variable itself. However, if we try to update the binding of the `const` variable by re-assigning it a completely new array `c = [4,5,6]`, it throws a `TypeError`.

```
/* Objects are stored by reference.Hence, although the binding is immutable, the values are not. */
```

```
const d = { name: 'John Doe', age: 35};
```

```
d.age = 40; // Modifying a property: No errorconsole.log(d); // { name: 'John Doe', age: 40};
```

```
d.zipCode = '52534'; // Adding a property: No errorconsole.log(d); // { age: 40, name: "John Doe", zipCode: '52534; }
```

```
d = { name: 'Mary Jane', age: 25}; // TypeError: Assignment to constant variable.
```

As we can see above, we can modify and add properties to the object since this only modifies the contents of what the `const` variable is pointing to, but does not try to overwrite the contents of the `const` variable itself. However, if we try to update the binding of the `const` variable by re-assigning it a completely new object `d = { name: 'Mary Jane', age: 25 };`, it throws a `TypeError`.

### When should I use what?

JavaScript now has three kinds of variables, and a natural question is wondering when to use what.

After the introduction of block-scoped `let` , the usage of `var` is generally discouraged to avoid confusion with function level scope, accidental re-declarations, and hoisting bugs with `undefined` value. Unless you have a compelling reason to use function scope of `var`, use `let`.

Use `const` to hold values that are facts, such as `const PI = 3.14`, or values that should strictly remain unmodified for the entire execution of the program.

A common programming approach consists of developers starting off by declaring all variables with `const` , and progressively converting them to `let` variables if the need arises. Personally, I start with `let` variables, and convert them to `const` variables if I see the need. There is no set approach, and you should use what works best for your code.

If you have time, I strongly suggest that you read the fictional piece again as it will cement the connections in your mind with the additional technical knowledge.

Thank you for reading! I hope you learned something new, and I would love to receive feedback.

Follow me on Twitter [here](https://twitter.com/prar_s), and LinkedIn [here](https://www.linkedin.com/in/prarthana-sannamani/).

References:

1. [_https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
2. [_https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
3. [_https://dmitripavlutin.com/variables-lifecycle-and-why-let-is-not-hoisted/_](https://dmitripavlutin.com/variables-lifecycle-and-why-let-is-not-hoisted/)
4. [_https://github.com/getify/You-Dont-Know-JS_](https://github.com/getify/You-Dont-Know-JS)

