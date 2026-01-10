---
title: ‘let’ me be a ‘const’(ant), not a ‘var’(iable)!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-28T13:51:49.000Z'
originalURL: https://freecodecamp.org/news/let-me-be-a-const-ant-not-a-var-iable-1be52d153462
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d-yr1HCiJN05bS1m4ooS0w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Srishti Gupta

  var, let and const are the keywords which are used to declare variables in JavaScript.
  var comes under the ECMAScript 5th edition (aka ES5) whereas let and const fall
  under the category of ECMAScript 6th edition (aka ES6 and ES2015)....'
---

By Srishti Gupta

`var`, `let` and `const` are the keywords which are used to declare variables in JavaScript. `var` comes under the ECMAScript 5th edition (aka ES5) whereas `let` and `const` fall under the category of ECMAScript 6th edition (aka ES6 and ES2015).

Since JavaScript does not have any type-checking, either of these keywords can be used to declare a variable of any type (datatype) in JavaScript.

_Though all the three keywords are used for the same purpose, they are different._

### ‘let’ vs. ‘const’:

#### **Change of value in future**

> Variables declared using the `let` keyword can change their values in the future.

Consider the example given below:

```
let iChange = 11;iChange = 12;
```

```
console.log(iChange);
```

**Output:**

```
12
```

On the first line, the variable `iChange` is declared using the `let` keyword and is initialized with value 11. When you come down to the next line, the variable `iChange` is again assigned a new value, which is 12. Changing the values of variables declared using the `let` keyword is allowed. When, on the last line, you try to print the value of the variable `iChange`, you correctly get the updated value 12.

> Variables declared using the `const` keyword cannot change their values in future. This is why you must always initialize the variables declared with the `const` keyword.

```
const PI = 3.14;PI = 22/7;
```

```
console.log(PI);
```

**Output:**

```
Uncaught TypeError: Assignment to constant variable
```

Here, the variable `PI` is declared using the `const` keyword and is initialized with value `3.14` on the first line. When you come down to the next line, the variable `PI` is updated with a new value `22/7`. Changing values of variables declared using the `const` keyword is not allowed. This is why the second line throws the error shown in the output because you are trying to assign a new value to a constant variable. Therefore, remember that variables declared using the `const` keyword are read-only & cannot be reassigned any value.

As mentioned earlier, it is mandatory to initialize a constant when declaring it. Let’s see the following statement of code:

```
const PI;
```

**Output:**

```
Uncaught SyntaxError: Missing initializer in const declaration
```

You know that you cannot update a constant in future. If you do not initialize a constant during its declaration, you will not be able to assign any value to it EVER! This is why you get a `SyntaxError` when you leave a constant uninitialized.

What do you think will be the output of the code given below?

```
const passengerBus = {wheels: 8, passengers: 40}passengerBus.passengers = 50;
```

```
console.log(passengerBus);
```

Do you think an error will be thrown? Let’s check the output. Here we go.

**Output:**

```
{ wheels: 8, passengers: 50 }
```

> The objects (including arrays & functions) declared using the `_const_` keyword are mutable.

So far, you’ve learned that variables declared using the `const` keyword cannot be assigned any other value. While this is true, there’s another side of the story too. Undoubtedly, you cannot assign a new value to a constant but you can manipulate the existing value if it is an object or an array.

In the code given above, you are not changing the entire value assigned to the constant `passengerBus` but you are manipulating a property inside it. You can add/delete/update a property inside an object declared using the `const` keyword.

Similar can be done with arrays too. You can add add/delete/update an element inside an array declared using a `const` keyword.

```
const android = ['Marshmallow', 'Noughat', 'Oreo'];arr[3] = 'Pie'; // adding new version
```

```
console.log(android);
```

**Output:**

```
['Marshmallow', 'Noughat', 'Oreo', 'Pie']
```

Now, considering that the keywords `let` and `const` belong to the same category, the following points enlist the differences between the variables declared using the `let`/`const` keywords and the variables declared using the `var` keyword:

### ‘let’ (or ‘const’) vs. ‘var’:

#### **Scope**

> Variables declared using the `let`/`const` keywords are **block-scoped**.

Consider the following example:

```
function foo() {   for (let i = 0; i < 3; i++) {      console.log(i); // statement 1   }   console.log(`All eyes here please: ${i}`); // statement 2}
```

```
foo();
```

**Output:**

```
012Uncaught ReferenceError: i is not defined
```

The variable _i_ is declared using the `let` keyword inside the for-loop block. This means that when the for-loop block ends, the variable _i_ loses its scope and is no longer accessible outside the curly braces of the for-loop block. Thus, when you try to access the variable _i_ and print its value on statement 2, you get a `ReferenceError: i is not defined`, as shown in the output.

Consider another example of declaring a variable using the `const` keyword:

```
function placeOrder(status) {   if (status) {      const message = "Order placed successfully!";      console.log(message); // statement 1   }   console.log(message); // statement 2}
```

```
placeOrder(true);
```

**Output:**

```
Order placed successfullyUncaught ReferenceError: message is not defined
```

The variable `message` is declared using the `const` keyword inside the if-block. This means that when the if-block ends, the variable `message` loses its scope and is no longer accessible outside the curly braces of the if-block. This is why, when you try to access variable `message` and print its value on statement 2, you get a `ReferenceError: message is not defined`, as shown in the output.

> Variables declared using the `var` keyword are **function-scoped**.

Consider the example which we’ve discussed earlier where instead of using `let`, you use the `var` keyword to declare the variable _i_:

```
function foo() {   for (var i = 0; i < 3; i++) {      console.log(i); // statement 1   }   console.log(`All eyes here please: ${i}`); // statement 2}
```

```
foo();
```

**Output:**

```
012All eyes here please: 3
```

The variable _i_ is declared using the `var` keyword inside the for-loop-block. Because the variables declared using the `var` keyword are function-scoped, the variable _i_ does not go out of scope when the for-loop-block ends and is accessible anywhere inside the scope of the function `foo`. Thus, on statement 2, when you try to access the variable _i_ and print its value, you get the correct output as `3` (incremented value of variable _i_ after the for-loop’s increment statement is executed) as shown in the output.

#### Redeclaration

> Variables declared using the `_let_`/`_const_` keywords **cannot be redeclared** in the same scope.

What do you think will be the output of the following code?

```
let avengers = 'Infinity War';let avengers = 'Endgame';
```

```
console.log(avengers);
```

**Output:**

```
Uncaught SyntaxError: Identifier 'avengers' has already been declared
```

In the above code, you declared a variable with the name `avengers` using the `let` keyword and then you declared it again on the next line. Thus, the second line throws an `SyntaxError` as mentioned in the output.

> Variables declared using the `var` keyword **can be redeclared** in the same scope.

Let’s now declare a variable already declared earlier in the same scope using the `var` keyword.

```
var avengers = 'Infinity War';var avengers = 'Endgame';
```

```
console.log(avengers);
```

**Output:**

```
Endgame
```

As evident from the output , you can redeclare variables having the same name in the same scope using the `var` keyword. The value contained in the variable will be the final value that you have assigned to it.

#### **Hoisting**

> Variables declared using the `_let_`/`_const_` keywords are **NOT hoisted**.

This is an important point which is forgotten by many and you won’t find it in all articles. To understand what this point means, consider the example given below:

```
console.log(x);let x = 10;
```

**Output:**

```
Uncaught ReferenceError: x is not defined
```

Notice that on the first line in the code given above, you are trying to access a variable _x_, which is declared and assigned a value on the next line. Essentially, you are trying to access a variable, which has not yet been allocated memory (declared). Since the variable _x_ is declared using the `let` keyword and the variables declared using the `let`/`const` keywords are not hoisted, this throws a `ReferenceError: x is not defined`, as shown in the output.

> Variables declared using the `var` keyword are **hoisted to the top of their scope**.

```
console.log(x);var x = 10;
```

**Output:**

```
undefined
```

All the declarations are moved to the top of the scope. Notice that on the first line, you are trying to access a variable _x_, which is declared and assigned a value on the next line. Now, since the variable _x_ is declared using the `var` keyword and the variables declared using the `var` keyword are hoisted to the top of their scope in JavaScript, the code gets converted to the one given below:

```
var x;console.log(x);x = 10;
```

Here, the variable _x_ is declared on line 1 and is not assigned any value. All the variables in JavaScript are initialized with the default value `undefined`, if no other value is assigned explicitly by the user. Thus, `x` is assigned the value `undefined`, which is what is printed on the second line (before x is updated to 10).

#### The Bigger Question — What to Prefer?

ES6 (aka ES2015) is supported by almost all the browsers today. If you can follow this syntax, it is recommended to use the `let` and `const` keywords for declaring all the variables in your code.

Now, which one to choose amongst `let` and `const`? The title says it all.

![Image](https://cdn-media-1.freecodecamp.org/images/rj5mGjbr0EVJzlpIYxLgMluer6heMLZSsG0i)

