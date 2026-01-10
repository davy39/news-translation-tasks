---
title: C Operator – Logic Operators in C Programming
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-08T15:25:21.000Z'
originalURL: https://freecodecamp.org/news/c-operator-logic-operators-in-c-programming
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-mikael-blomkvist-6476587.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: "In this article, you will learn about the three logical operators in C.\n\
  I will first explain what operators are in programming and list the different types\
  \ of operators available in C. \nThen, you will learn the role logical operators\
  \ have and how to ..."
---

In this article, you will learn about the three logical operators in C.

I will first explain what operators are in programming and list the different types of operators available in C. 

Then, you will learn the role logical operators have and how to use them with the help of code examples along the way.

Let's get into it!


## What Is An Operator in Computer Programming?
In computer programing, an operator is a character, symbol, keyword, or combination of those. It determines what action gets performed on one or more operands.

An operand is an individual data item that gets manipulated by the operator.

Each high-level programming language defines these built-in characters and uses them to tell the compiler to perform arithmetic, relational or logical operations that manipulate data items and then return a final result.


### What Are The Different Types of Operators in C Programming?
In C programming, operators fall into one of three categories:

- **Unary** operators
- **Binary** operators
- **Ternary** operators

**Unary** operators operate on a single operand. Some of the unary operators in C are:
- Arithmetic operators such as the increment operator(`++`), which increments the value of the operand by `1`. And the decrement operator(`--`), which decrements the value of the operand by `1`.
- Logical operators like the NOT(`!`) operator. This operator reverses the logical value of the operand – it changes `true` to `false` and `false` to `true`.
- Bitwise operators like the NOT(`~`) operator, which changes each `0` bit to `1` and each `1` bit to `0`.

**Binary** operators operate on two operands. Some of the binary operators in C are:
- Arithmetic operators (`+, -, *, /, %`). These operators perform mathematical calculations on numerical data such as addition, subtraction, multiplication, division, and finding the remainder. 
- Equality/Relational operators (`==, !=, >, <, >=, <=`). These operators compare two values and determine if one operand is greater than, less than, equal to, or not equal to the other operand.
- Logical/Conditional operators such as the AND(`&&`) and OR(`||`) operators.
- Bitwise operators (`(&, |, ^, <<, >>`), which treat data items as a sequence of bits (that is, `0`s and `1`s).
- Assignment operators (`=, +=, -=, *=, /=, %=`), which assign a specific value to a variable.  

The **Ternary** operator (`?:`) operates on three operands. The general syntax looks something similar to the following:
```c
(condition) ? expression1 : expression2;
```

The ternary operator is a conditional operator you can use as a shorthand for an `if..else` statement. It performs comparisons and returns a result.


## What Is the Role of Logical Operators in C Programming?
You will see logical operators commonly used in conditional statements (such as `if..else` statements) since they aid in decision making – they determine what action should take place and what code should run next based on conditions you set.

You combine logical operators with one or multiple conditions to create a logical expression.

The logical operators evaluate the logical expression and return a result. 

The result is always a Boolean value. A Boolean value determines whether the expression is `true` or `false`.

There are three logical operators in C programming: logical AND(`&&`), logical OR(`||`), and logical NOT (`!`).

Let's go into more detail on each one in the following sections.


### How to Use the AND `(&&)` Logical Operator in C Programming
The logical AND(`&&`) operator checks whether **all** operands are `true` – the result is `true` only when all operands are `true`.

Here is the truth table for the AND(`&&`) operator when you are working with two operands:
| First Operand | Second Operand | Result |
| --- | --- | --- |
| true | true | true |
| true | false | false |
| false | true | false |
| false | false | false |

Something to note here is that, when the first operand is `false`, the second operand is not evaluated.

Let's look at an example:
The result of `(10 == 10) && (20 == 20)` is `true` because *both* operands are `true` – `(10 == 10)` is `true` *and* `(20 == 20)` is `true`.

Let's look at another example:
The result of `(10 == 20) && (20 == 20)` is `false` because one of the operands is `false` – in this case, the first operand is `false`, so the second operand doesn't get evaluated.

Now, let's see how you can use the `&&` operator in an `if` statement:
```c
#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 30;

  if (a > 10 && b > 10)
    printf("Both numbers are greater than 10\n");
}

// output

// Both numbers are greater than 10
```

In the example above, the output is `Both numbers are greater than 10` because the condition `a > 10 && b > 10` is satisfied.

Both `a > 10` and `b > 10` are `true`, so the result is `true`. 

If either `a` or `b` did not satisfy the condition, then there would be no output in the console since I have not specified an `else` condition.


### How to Use the OR `(||)` Logical Operator in C Programming
The logical OR(`||`) operator checks whether one of the operands is `true` – the result is `true` if *at least one* of the operands is `true`.

Here is the truth table for the OR(`||`) operator when you are working with two operands:
| First Operand | Second Operand | Result |
| --- | --- | --- |
| true | true | true |
| true | false | true |
| false | true | true |
| false | false | false |

Note that with the OR (`||`) operator, if the first operand is `true`, then the second operator is not evaluated.

Let's look at an example:
The result of `(10 == 20) || (20 == 20)` is `true` because at least one of the operands is `true`, in this case, it is the second operand, even if the first operand is `false`. 

Let's look at another example:
The result of `(20 == 20) || (10 == 20) ` is `true` because one of the operands is `true` – in this case, since the first operand is `true`, the second one is not evaluated.

Now, let's see how you can use the OR (`||`) operator in an `if` statement:
```c
#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 5;

  if (a > 10 || b > 10)
    printf("At least one of the numbers is greater than 10");
}
```

In the example above, the output is `At least one of the numbers is greater than 10` because the condition `a > 10 || b > 10` is satisfied – at least one of the operands is `true`.

The first condition, `a > 10`, is `true`, so the result is `true`.

If both `a` and `b` were `false`, there would be no output.


### How to Use the NOT `(!)` Logical Operator in C Programming
The logical NOT(`!`) operator negates the operand – that is, it returns the opposite of the operand.

If the operand is `true`, it returns `false`. 

And if it is `false`, it returns `true`.

Here is the truth table for the NOT(`!`) operator:
| Operand | Result |
| --- | --- |
| true | false |
| false | true |
 
Let's look at an example:
The result of `!(10 == 10)` is `false`. 

The condition `10 == 10` is `true`, but the `!` operator negates it.

And let's look at another example:
The result of `!(10 == 20)` is `true`. 

The condition `10 == 20` is false, but the `!` operator negates it.

Now, check the example below for how you can use the NOT(`!`) operator in an `if` statement:
```c

#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 5;

  if ( a > b)
    printf("a is greater than b\n");
}
```

The output is `a is greater than b` because the condition `a > b` is `true`.

However, if you used the NOT(`!`) operator, the condition is no longer `true`, so there would be no output:
```c

#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 5;

  if ( !(a > b))
    printf("a is greater than b\n");
}
```


## Conclusion
And there you have it! You now know how the three logical operators work in C programming.

To learn more about C, [give this C beginner's handbook a read](https://www.freecodecamp.org/news/the-c-beginners-handbook/) to become familiar with the basics of the language.

Thanks for reading, and happy coding!


