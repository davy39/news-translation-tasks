---
title: Parameters vs Arguments in JavaScript – What's the Difference?
subtitle: ''
author: Segun Ajibola
co_authors: []
series: null
date: '2022-09-28T21:18:15.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-difference-between-parameters-and-arguments-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Parameters-vs-Arguments.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript is one of the most popular programming languages out there for
  web development.

  The dynamic values passed in a JavaScript function can change when the function
  gets called in another location in the code. The keywords we use to name these ...'
---

JavaScript is one of the most popular programming languages out there for web development.

The dynamic values passed in a JavaScript function can change when the function gets called in another location in the code. The keywords we use to name these data are parameters and arguments, but some developers confuse them.

In this article, you will learn about parameters and arguments and what they are, along with where and when to use them.

### Table of Contents

* Introduction to JavaScript functions
* How to use Parameters and Arguments in a function
* The power of arguments
* Conclusion

## Introduction to JavaScript Functions

One of the fundamental building blocks in JavaScript programming is a function. It's a block of code designed to perform a particular task.

Functions are reusable code which you can use anywhere in your program. They eliminate the need to repeat the same code all the time.

To use functions in a powerful way, you can pass values in a function to use them.

Here is an example of a function:

```javascript
function add(){
	return 2 + 3
}

add()
```

This is a function declaration, the name of the function is `add`, and it was called after the function with `add()` . The result of the function will be 5.

Let's introduce parameters and arguments in the function.

## How to Use Parameters and Arguments in a Function

Take a look at our function code now:

```javascript
function add(x, y){
	return x + y
}

add(2, 3)
```

We have introduced x and y here and changed the location of the 2 and 3. x and y are the parameters while 2 and 3 are the arguments here.

A **parameter** is one of the variables in a function. And when a method is called, the **arguments** are the data you pass into the method's parameters.

When the function is called with `add(2, 3)` the arguments 2 and 3 are assigned to x and y, respectively. This means that in the function, x will be replaced with 2 and y will be replaced with 3.

If the function is called with a different argument, the same applies. Parameters are like placeholders for function arguments.

## The Power of Arguments

We can use arguments more efficiently when we want to make functions more re-useable, or when we want to make calling functions inside another functions more powerful.

Here is an example:

```javascript
function add(x, y){
	return x + y
}

function multiply(a, b, c){ // a = 1, b = 2, c = 3
	const num1 = add(a, b) // num1 = add(1, 2) = 3
	const num2 = add(b, c) // num2 = add(2, 3) = 5
    
	return num1 * num2 // 15
}

multiply(1, 2, 3)
// returns 15
```

The first function `add()` has two parameters, x and y. The function returns the addition of the two parameters.

The second function `multiply()` has three parameters: inside the function, two variables are declared in it, `num1` and `num2`. `num1` will store the value of the result of `add(a, b)`, and `num2` will store the value of the result of `add(b, c)`. At the end the `multiply` function will return the value of `num1` multiplied by `num2`.

`multiply` is called with three arguments which are 1, 2 and 3. `add(a, b)` will be `add(1, 2)` which will return 3. `add(b, c)` will be `add(2, 3)` which will return 5.

`num1` will have the value of 3 while `num2` will be 5. `num1 * num2` will return 15.

Arguments are passed in the `multiply` function which are also used as arguments for the `add` function.

## Conclusion

Using parameters and arguments can be confusing at times, especially if you are just learning them. But if you first properly learn what a function is and how it works, you will understand parameters and arguments easily.

Thanks for reading this article. If you enjoyed it, consider sharing it to help other developers.

You can reach me on [Twitter](https://twitter.com/iamsegunajibola), [LinkedIn](https://www.linkedin.com/in/segunajibola/) and [GitHub](https://github.com/segunajibola).

Happy Learning.

