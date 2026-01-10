---
title: Statement vs Expression – What's the Difference in Programming?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-08T23:44:58.000Z'
originalURL: https://freecodecamp.org/news/statement-vs-expression-whats-the-difference-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/kaleidico-7lryofJ0H9s-unsplash.jpg
tags:
- name: beginner
  slug: beginner
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: syntax
  slug: syntax
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Ogundiran Ayobami

  Learning the syntax of a programming language is key if you want to use that language
  effectively. This is true for both new and experienced developers.

  And one of the most important things to pay attention to while learning a pr...'
---

By Ogundiran Ayobami

Learning the syntax of a programming language is key if you want to use that language effectively. This is true for both new and experienced developers.

And one of the most important things to pay attention to while learning a programming language is whether the code you're dealing with is a statement or an expression.

It can sometimes be confusing to differentiate between statements and expressions in programming. So this article is meant to simplify the differences so that you can improve your programming skills and become a better developer.

## What is an Expression in Programming?

![Senior caucasian man holding blank empty banner covering mouth with hand, shocked and afraid for mistake. surprised expression ](https://images.unsplash.com/photo-1603792907191-89e55f70099a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDF8fHN1cnByaXNlZHxlbnwwfHx8fDE2NzA1MTMyNzI&ixlib=rb-4.0.3&q=80&w=2000)
_Photo by [Unsplash](https://unsplash.com/@krakenimages?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">krakenimages</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

An expression is any word or group of words or symbols that is a value. In programming, an expression is a value, or anything that executes and ends up being a value.

It is necessary to understand that a value is unique. For example, `const`, `let`, `2`, `4`, `s`, `a`, `true`, `false`, and `world` are values because each of them is unique in meaning or character.

Let's look at some code as an example:

```js
const price = 500;

```

Judging from the code above, `const`, `price`, `=`, and `500` are expressions because each of them has a definite and unique meaning or value. But if we take all of them together `const price = 500` - then we have a statement.

Let's look at another example:

```js
let multiply = function (firstNumber, secondNumber) {
    return firstNumber * secondNumber;
}

```

Looking at the code above, you can see an anonymous function is assigned to a variable. Oh, wait! You might know that any function is a statement. Can it also be an expression? 

Yes! A "function" and a "class" are both statements and expressions because they can perform actions (do or not do tasks) and still execute to a value.

This brings us to statements – so what are they?

## What is a Statement in Programming?

A statement is a group of expressions and/or statements that you design to carry out a task or an action. 

Statements are two-sided – that is, they either do tasks or don't do them. Any statement that can return a value is automatically qualified to be used as an expression. That is why a function or class is a statement and also an expression in JavaScript.

If you look at the example of the function under the section on expressions, you can see it is assigned and execute to a value passed to a variable. That is why it is an expression in that case.

## Examples of Statements in Programming

### Inline statements

```js
let amount = $2000;

```

The whole of the code above is a statement because it carries out the task of assigning `$2000` to `amount`. It is safe to say a line of code is a statement because most compilers or interpreters don't execute any standalone expression.

![Happy man portraits ](https://images.unsplash.com/photo-1625314517201-dd442445cf42?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDF8fGV4Y2l0ZWR8ZW58MHx8fHwxNjcwNTEzMzMx&ixlib=rb-4.0.3&q=80&w=2000)
_Photo by [Unsplash](https://unsplash.com/@1nimidiffa_?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Nimi Diffa</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

### Block statements

Look at the below `if` statement:

```js
if( iLoveYou ) {
    let status = "you should know I mean it"; 

    console.log(status)
}

```

The `if statement` is a statement because it helps us check whether `I love you` or not. As I have said before, it is two-sided: this code finds out whether "I love you" or not, and that is why it is a statement. Also, it doesn't return any value but it can create side effects.

Here's a `loop` statement:

```js
for( ) {
   //code block
}

while ( counter < 5 ) {
   console.log(' less than 5' );
}

```

In short, any loop is a statement because if it can only do the tasks it is meant to do or not – does loop and doesn't loop. But a loop can't execute to a value in the end. They can only have side effects in JavaScript. Once they can execute to a value in a programming language, then they can also be used as an expression.

For example, you can use forloop and if statement as expressions in Python.

```python
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# compute the sum of the numbers
total = sum([num for num in numbers])
```

There is also an "IF" expression in Python. That means that something that is a statement in one language can be an expression (or both statement and expression) in another.

```python
a = 1
result = 'even' if a % 2 == 0 else 'odd'
print(result)

```

Look at the below function statement:

```js
//we define the function as a statement
function add(firstNumber, secondNumber) {
    return firstNumber * secondNumber;
}

//we call it as a statement
add(2, 3);

```

We declare the function `add(firstNumber, secondNumber)` and it returns a value. The function is called with two arguments as in `add(2, 3)` by declaration and so it is a statement. If you pay close attention, you will realize that calling the function as a statement is useless since it has no side effect.

Hey, stop! How can we turn it into an expression? Oh yeah, we can do it like this:

```js
   const five = add(2, 3)

```

Though the function is now an expression the way it is called above, the whole of the code is still a statement.

Check out this class statement:

```js
let User = class Person {
  sayHi() {
    alert("Hi");
  }
};

```

You can see that we declare the class "Person" and **instantiate and assign** it to "User" immediately. So, it is used as an expression. 

Now, let's use it as a statement:

```js
//We write class as a statement
class Person {
  sayHi() {
    alert("Hi");
  }
}

// we instantiate it as a statement.
new Person().sayHi();

// we instantiate it as an expression
let User = Person();

```

[A class](https://www.techtarget.com/whatis/definition/class#:~:text=In%20object-oriented%20programming%20%2C%20a,ideas%20of%20object-oriented%20programming.) is similar to a function in the sense that it can be declared, assigned, or used as an operand just like a class. So, a class is a statement and/or an expression.

## The Main Differences Between an Expression and a Statement in Programming

Expressions can be assigned or used as operands, while statements can only be declared.

Statements create side effects to be useful, while expressions are values or execute to values.

Expressions are unique in meaning, while statements are two-sided in execution. For example, 1 has a certain value while `go( )` may be executed or not.

Statements are the whole structure, while expressions are the building blocks. For example, a line or a block of code is a statement.

## Why You Should Know the Difference

First of all, understanding the difference between statements and expressions should make learning new programming languages less surprising. If you're used to JavaScript, you may be surprised by Python's ability to assign an if statement as a variable which is not possible in JavaScript.

Second, it makes it easy to use programming paradigms across different programming languages. 

For example, a JavaScript "if statement" cannot be used as an expression because it can't execute to a value – it can only create side effects. Yet, you can use the ternary operator if you want to avoid the side effects of using an if statement in JavaScript. 

For this reason, you can understand why some programmers avoid if statements by using the ternary operator in JavaScript. It is because they want to avoid [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)). 

It also makes your realize why you have to be always careful about the scope of your variables whenever you use a statement. This is true because statements mostly have side effects to be useful, and it is reasonable to understand the scope of your variables and operations. For example,

```js
let counter = 0;

function addFive() {
    counter += 5
    console.log(counter)
}

function addTwo() {
    counter += 2
    console.log(counter)
}

addFive(counter);// what will this show in the console?
addTwo(counter);// what will this show in the console?
```

Hey wait! What would be logged in the console if you ran the code above? 

Tell yourself the answer first and then paste the code in the console to confirm. If you you're wrong, you need to learn more about scope and side effects. But if you're right, try to make those functions a bit better to avoid the confusion they may generate.

Knowing the difference also helps you to easily identify non-composable and composable syntaxes (functions, classes, modules, and so on) of a programming language. This makes porting your experience from one programming language to another more interesting and direct.

## **Wrapping Up**

Now that you understand the difference between expressions and statements in programming, and you know why understanding the differences is important, you can identify pieces of code as expressions or statements while coding. 

Next time, we'll go even further and help make learning a second programming language easier.

Go and get things done now! See you soon.

I am planning to share a lot about programming tips and tutorials in 2023. If you're struggling to build projects or you want to stay connected with my write-ups and videos, please join my list at [YouTooCanCode](https://youtoocancode.aweb.page) or subscribe to my YouTube channel at [You Too Can Code on YouTube](https://www.youtube.com/c/youtoocancode).

