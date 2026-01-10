---
title: Type Error vs Reference Error in JavaScript – What's the Difference?
subtitle: ''
author: Tejan Singh
co_authors: []
series: null
date: '2023-02-15T17:12:30.000Z'
originalURL: https://freecodecamp.org/news/type-error-vs-reference-error-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-kim-stiver-909256.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'As a JavaScript developer, you''ve likely encountered different types of
  errors while coding. Most of the time these will be type errors or reference errors.
  But have you ever wondered what they mean?

  Have you ever tried reading about the error type s...'
---

As a JavaScript developer, you've likely encountered different types of errors while coding. Most of the time these will be type errors or reference errors. But have you ever wondered what they mean?

Have you ever tried reading about the error type specified by the interpreter before solving these errors? If not, you should, since knowing about these errors can help you solve your problems.

For example, when you encounter an error, you probably Google it. You copy and paste the whole error and try to find out the solution, by visiting various websites and forums. It's a trial and error method of finding and solving bugs.

But what if you already knew why the error generally occurs? This would save you time you'd otherwise spend searching for solutions online. Instead, you could start looking for solutions on your own just by looking at the error type.

In this guide, you will learn about the two mostly encountered error types, which are type error and reference error. You'll learn why they occur, the difference between them, and how to avoid getting these errors.

Note: There are other types of errors in JavaScript like syntax errors, internal errors, range errors, and eval errors. But the scope of this article is limited to the two most commonly occurring errors.

## What is a Type Error?

Type errors occur when you use something that is not intended to be used in that particular way. For example, using a screwdriver to hammer in a nail, instead of using a hammer.

Let's understand this using an example:

```javascript
let a = 1
console.log(a()) 

//output
Uncaught TypeError: a is not a function
```

Here `a` is a variable initialized with a value. You encountered an error because you tried to call a function with the variable name. A variable cannot be called as a function. Functions and variables work differently. So in this case, you got a type error. You used the `let` variable differently from its _type._ 

This gives us a type error.

Solution: To resolve this error, you must refer to the variable in the console, as it is intended to be used. In this case, you pass `a` as a variable instead of a function.

```javascript
let a = 1
console.log(a)

//output
1
```

Let's take another example:

```javascript
const a = 1
a = 2 // you reassign a const type variable again

//output
TypeError: Assignment to constant variable.

```

Here, we reassigned the `const` type variable `a` to a new value. But you can't change const variables like this, so in this case you get a type error

Solution: never reassign a `const` type variable once you've defined it.

```javascript
const a = 1
const b = 2
console.log(a, b)

//output
1 2
```

Here's another example using an array:

```javascript
const myArray = [1,2,3,4]
myArray = myArray.push(5) // reassign array

//output
TypeError: Assignment to constant variable.
```

In this case, we reassigned the `const` type `myArray`. This gives us a type error because again, this kind of reassignment is against the properties of `const`. 

Solution:

```javascript
const myArray = [1,2,3,4]
myArray.push(5) // you can push new values

//output
[1,2,3,4,5]
```

You can easily push new values to the array without reassigning it. This will not give you any error. Pushing values into an array is allowed. This way you can avoid getting the error.

### How to avoid getting a type error

The easiest way to prevent type errors is to avoid using the same names for different variables and functions. 

If you use different names, you will not get confused or replace one with another, and you can easily avoid getting this error.

Another way is to make sure you use variables as they're intended to be used. Instead of using `const` when you need to reassign a value, use `let` (which allows this kind of change).

## What is a Reference Error?

Reference errors occur when you are trying to refer to or use something that does not exist. For example, looking for a screwdriver in your toolbox, but it's not there.

Let's understand this using an example:

```javascript
let a = 1
console.log(b) // undefined variable used

//output
Uncaught ReferenceError: b is not defined
```

Here, `a` is a variable initialized with a value. We encountered an error because we tried to console log the variable `b` that does not exist. We hadn't yet declared any such variable, so we got a reference error here.

Solution: only use a variable that you've declared to avoid getting an error.

```javascript
let a = 1
console.log(a) // used defined variable

//output
1
```

Here's another example:

```javascript
if(true){
    let a = 1
}

console.log(a)

//output
ReferenceError: a is not defined
```

In this example, we're trying to access the `a` variable of type `let` outside its block. The interpreter cannot find it outside the block. This gives us an error.

Solution:

```javascript
if(true){
    let a = 1
    console.log(a)
}


//output
1
```

Using the variable inside its block or scope will not give you any error.

Let's take one more example, but this one can be difficult to understand.

```javascript
if(true){
	console.log(a)
    let a = 1
}


//output
ReferenceError: Cannot access 'a' before initialization
```

`a` is still inside its scope. But we get an error. Why? Because we're trying to use the variable before we've defined it. This is not allowed and goes against the properties of the `let` variable. 

Solution: use the `let` variable only after defining it. 

```javascript
if(true){
	let a = 1
	console.log(a)
    
}

//output
1
```

### How to avoid getting a reference error

The easiest way to avoid getting reference errors is to refer to or access only defined variables. Only use variables that exist. 

You can also use conditional statements and error handling to avoid running code if a variable or a function does not exist.

## Conclusion

You can easily debug your code when you already know how to resolve your errors. It's good to know commonly occurring errors and how to avoid them. This will save you time searching for solutions online and wasting hours trying to find a solution when a little bit of knowledge and awareness about these things can help.


