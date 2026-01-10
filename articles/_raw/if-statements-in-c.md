---
title: If...Else Statement in C Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-21T17:07:00.000Z'
originalURL: https://freecodecamp.org/news/if-statements-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9da9740569d1a4ca38ef.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'Conditional code flow is the ability to change the way a piece of code
  behaves based on certain conditions. In such situations you can use if statements.

  The if statement is also known as a decision making statement, as it makes a decision
  on the bas...'
---

Conditional code flow is the ability to change the way a piece of code behaves based on certain conditions. In such situations you can use `if` statements.

The `if` statement is also known as a decision making statement, as it makes a decision on the basis of a given condition or expression. The block of code inside the `if` statement is executed is the condition evaluates to true. However, the code inside the curly braces is skipped if the condition evaluates to false, and the code after the `if` statement is executed.

### Syntax of an `if` statement

```text
if (testCondition) {
   // statements
}
```

### A simple example

Let’s look at an example of this in action:

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    if(true) {
        printf("Statement is True!\n");
    }

    return 0;
}
```

**Output:**

```text
Statement is True!
```

If the code inside parenthesis of the `if` statement is true, everything within the curly braces is executed. In this case, `true` evaluates to true, so the code runs the `printf` function.

### `if..else` statements

In an `if...else` statement, if the code in the parenthesis of the `if` statement is true, the code inside its brackets is executed. But if the statement inside the parenthesis is false, all the code within the `else` statement's brackets is executed instead.

Of course, the example above isn't very useful in this case because `true` always evaluates to true. Here's another that's a bit more practical:

```c
#include <stdio.h>

int main(void) {
    int n = 2;

    if(n == 3) { // comparing n with 3
        printf("Statement is True!\n");
    } 
    else { // if the first condition is not true, come to this block of code
        printf("Statement is False!\n");
    }

    return 0;
}
```

**Output:**

```text
Statement is False!
```

There are a few important differences here. First, `stdbool.h` hasn’t been included. That's okay because `true` and `false` aren't being used like in the first example. In C, like in other programming languages, you can use statements that evaluate to true or false rather than using the boolean values `true` or `false` directly.

Also notice the condition in the parenthesis of the `if` statement: `n == 3`. This condition compares `n` and the number 3. `==` is the comparison operator, and is one of several comparison operations in C.

### Nested `if...else`

The `if...else` statement allows a choice to be made between two possibilities. But sometimes you need to choose between three or more possibilities.

For example the sign function in mathematics returns -1 if the argument is less than zero, +1 if the argument is greater than zero, and returns zero if the argument is zero. 

The following code implements this function:

```c
if (x < 0)
   sign = -1;
else
   if (x == 0)
      sign = 0;
   else
      sign = 1;
```

As you can see, a second `if...else` statement is nested within `else` statement of the first `if..else`.

If `x` is less than 0, then `sign` is set to -1. However, if `x` is not less than 0, the second `if...else` statement is executed. There, if `x` is equal to 0, `sign` is also set to 0. But if `x` is greater than 0, `sign` is instead set to 1.

Rather than a nested `if...else` statement, beginners often use a string of `if` statements:

```c
if (x < 0) {
   sign = -1;
}
   
if (x == 0) {
   sign = 0;
}
   
if (x > 0) {
   sign = 1;
}
```

While this works, it's not recommended since it's unclear that only one of the assignment statements (`sign = ...`) is meant to be executed depending on the value of `x`. It's also inefficient – every time the code runs, all three conditions are tested, even if one or two don't have to be.

### else...if statements

`if...else` statements are an alternative to a string of `if` statements. Consider the following:

```c
#include <stdio.h>

int main(void) {
    int n = 5;

    if(n == 5) {
        printf("n is equal to 5!\n");
    } 
    else if (n > 5) {
        printf("n is greater than 5!\n");
    }

    return 0;
}
```

**Output:**

```text
n is equal to 5!
```

If the condition for the `if` statement evaluates to false, the condition for the `else...if` statement is checked. If that condition evaluates to true, the code inside the `else...if` statement's curly braces is run.

### Comparison Operators

|Operator name | Usage | Result|
| --- | --- | --- |
| Equal To |	`a == b` | True if `a` is equal to `b`, false otherwise |
| Not Equal To |	`a != b` | True if `a` is not equal to `b`, false otherwise |
| Greater Than | `a > b` | True if `a` is greater than `b`, false otherwise |
| Greater Than or Equal To |	`a >= b` | True if `a` is greater than or equal to `b`, false otherwise |
| Less Than | `a < b` | True if `a` is less than `b`, false otherwise |
| Less Than or Equal To | `a <= b` | True if `a` is less than or equal to `b`, false otherwise |



## **Logical Operators**

We might want a bit of code to run if something is not true, or if two things are true. For that we have logical operators:

|Operator name | Usage | Result|
| --- | --- | --- |
| Not (`!`) |	`!(a == 3)` | True if `a` is **not** equal to 3 |
| And (`&&`) |	`a == 3 && b == 6` | True if `a` is equal to 3 **and** `b` is equal to 6 |
| Or (`||`) |	`a == 2 || b == 4` | True if `a` is equal to 2 **or** `b` is equal to 4 |


For example:

```c
#include <stdio.h>

int main(void) {
    int n = 5;
    int m = 10;

    if(n > m || n == 15) {
        printf("Either n is greater than m, or n is equal to 15\n");
    } 
    else if( n == 5 && m == 10 ) {
        printf("n is equal to 5 and m is equal to 10!\n");
    } 
    else if ( !(n == 6)) {
        printf("It is not true that n is equal to 6!\n");
    }
    else if (n > 5) {
        printf("n is greater than 5!\n");
    }

    return 0;
}
```

**Output:**

```text
n is equal to 5 and m is equal to 10!
```

### An important note about C comparisons

While we mentioned earlier that each comparison is checking if something is true or false, but that's only half true. C is very light and close to the hardware it's running on. With hardware it's easy to check if something is 0 or false, but anything else is much more difficult.

Instead it's much more accurate to say that the comparisons are really checking if something is 0 / false, or if it is any other value.

For example, his if statement is true and valid:

```c
if(12452) {
    printf("This is true!\n")
}
```

By design, 0 is false, and by convention, 1 is true. In fact, here’s a look at the `stdbool.h` library:

```c
#define false   0
#define true    1
```

While there's a bit more to it, this is the core of how booleans work and how the library operates. These two lines instruct the compiler to replace the word `false` with 0, and `true` with 1.

