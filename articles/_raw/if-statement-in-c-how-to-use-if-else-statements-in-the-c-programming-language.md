---
title: If Statement in C – How to use If-Else Statements in the C Programming Language
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-06-13T13:47:00.000Z'
originalURL: https://freecodecamp.org/news/if-statement-in-c-how-to-use-if-else-statements-in-the-c-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/christin-hume-mfB1B1s4sMc-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'In the C programming language, you have the ability to control the flow
  of a program.

  In particular, the program is able to make decisions on what it should do next.
  And those decisions are based on the state of certain pre-defined conditions you
  set...'
---

In the C programming language, you have the ability to control the flow of a program.

In particular, the program is able to make decisions on what it should do next. And those decisions are based on the state of certain pre-defined conditions you set.

The program will decide what the next steps should be based on whether the conditions are met or not.

The act of doing one thing if a particular condition is met and a different thing if that particular condition is not met is called *control flow*.

For example, you may want to perform an action under only a specific condition. And you may want to perform another action under an entirely different condition. Or, you may want to perform another, completely different action when that specific condition you set is *not* met.

To be able to do all of the above, and control the flow of a program, you will need to use an `if` statement.

In this article, you will learn all about the `if` statement – its syntax and examples of how to use it so you can understand how it works.

You will also learn about the `if else` statement – that is the `else` statement that is added to the `if` statement for additional program flexibility.

In addition, you will learn about the `else if` statement for when you want to add more choices to your conditions.

Here is what we will cover:

1. [What is an `if` statement in C?](#intro)
    1. [How to create an `if` statement in C](#syntax)
    2. [What is an example of an `if` statement?](#example)
2. [What Is An `if else` Statement in C?](#else)
    1. [What is an example of an `if else` statement?](#else-example)
3. [What is an `else if` statement?](#else-if)
    1. [What is an example of an `else if` statement?](#example-else-if)

## What Is An `if` Statement In C? <a name="intro"></a>

An `if` statement is also known as a conditional statement and is used for decision-making. It acts as a fork in the road or a branch.

A conditional statement takes a specific action based on the result of a check or comparison that takes place.

So, all in all, the `if` statement makes a decision based on a condition.

The condition is a Boolean expression. A Boolean expression can only be one of two values – true or false.

If the given condition evaluates to `true` only then is the code inside the `if` block executed.

If the given condition evaluates to `false`, the code inside the `if` block is ignored and skipped.

### How To Create An `if` statement In C – A Syntax Breakdown For Beginners <a name="syntax"></a>

The general syntax for an `if` statement in C is the following:

```c
if (condition) {
  // run this code if condition is true
}
```

Let's break it down:

- You start an `if` statement using the `if` keyword.
- Inside parentheses, you include a condition that needs checking and evaluating, which is always a Boolean expression. This condition will only evaluate as either `true` or `false`.
- The `if` block is denoted by a set of curly braces, `{}`.
- Inside the `if` block, there are lines of code – make sure the code is indented so it is easier to read.

### What Is An Example Of An `if` Statement? <a name="example"></a>

Next, let’s see a practical example of an `if` statement.

I will create a variable named `age` that will hold an integer value.

I will then prompt the user to enter their age and store the answer in the variable `age`.

Then, I will create a condition that checks whether the value contained in the variable `age` is *less than* 18. 

If so, I want a message printed to the console letting the user know that to proceed, the user should be at least 18 years of age.

```c
#include <stdio.h>

int main(void) {
    // variable age
   int age;

   // prompt user to enter their age
   printf("Please enter your age: ");

   // store user's answer in the variable
   scanf("%i", &age);

    // check if age is less than 18
    // if it is, then and only then, print a message to the console
    
   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   }
}
```

I compile the code using `gcc conditionals.c`, where `gcc` is the name of the C compiler and `conditionals.c` is the name of the file containing the C source code.

Then, to run the code I type `./a.out`.

When asked for my age I enter `16` and get the following output:

```
#output

Please enter your age: 16
You need to be over 18 years old to continue
```

The condition (`age < 18`) evaluates to `true` so the code in the `if` block executes.

Then, I re-compile and re-run the program.

This time, when asked for my age, I enter `28` and get the following output:

```
#output

Please enter your age: 28
```

Well... There is no output. 

This is because the condition evaluates to `false` and therefore the body of the `if` block is skipped.

I have also not specified what should happen in the case that the user's age is *greater than* 18.

I could write another `if` statement that will print a message to the console if the user's age is greater than 18 so the code is a bit clearer:

```c
#include <stdio.h>

int main(void) {
    // variable age
   int age;

   // prompt user to enter their age
   printf("Please enter your age: ");

   // store user's answer in the variable
   scanf("%i", &age);

    // check if age is less than 18
    // if it is, print a message to the console
    
   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   }
   
   // check if age is greater than 18
   // if it is, print a message to the console
   
  if (age > 18) {
      printf("You are over 18 so you can continue \n");
  }
  
   }
```

I compile and run the code, and when prompted for my age I enter again 28:

```
#output

Please enter your age: 28
You are over 18 so you can continue 
```

This code works. That said, there is a better way to write it and you will see how to do that in the following section.

## What Is An `if else` Statement in C? <a name="else"></a>

Multiple `if` statements on their own are not helpful – especially as the programs grow larger and larger.

So, for that reason, an  `if` statement is accompanied by an `else` statement.

The `if else` statement essentially means that "`if` this condition is true do the following thing, `else` do this thing instead". 

If the condition inside the parentheses evaluates to `true`, the code inside the `if` block will execute. However, if that condition evaluates to `false`, the code inside the `else` block will execute.

The `else` keyword is the solution for when the `if` condition is false and the code inside the `if` block doesn't run. It provides an alternative.

The general syntax looks something like the following:

```c
if (condition) {
  // run this code if condition is true
} else {
  // if the condition above is false run this code
}
```


### What Is An Example Of An `if else` Statement? <a name="else-example"></a>

Now, let's revisit the example with the two separate `if` statements from earlier on:

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Please enter your age: ");


   scanf("%i", &age);

   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   }
  if (age > 18) {
      printf("You are over 18 so you can continue \n");
  }
  
   }
```

Let's re-write it using an `if else` statement instead:

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Please enter your age: ");

   scanf("%i", &age);

 
    // if the condition in the parentheses is true the code inside the curly braces will execute
    // otherwise it is skipped
    // and the code in the else block will execute
    
   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   } else {
      printf("You are over 18 so you can continue \n");
  }
  
   }
```

If the condition is `true` the code in the `if` block runs:

```
#output

Please enter your age: 14
You need to be over 18 years old to continue
```

If the condition is `false` the code in the `if` block is skipped and the code in the `else` block runs instead:

```
#output

Please enter your age: 45
You are over 18 so you can continue 
```

## What Is An `else if` Statement? <a name="else-if"></a>

But what happens when you want to have more than one condition to choose from?

If you wish to chose between more than one option and want to have a greater variety in actions, then you can introduce an `else if` statement.

An `else if` statement essentially means that "If this condition is true, do the following. If it isn't, do this instead. However, if none of the above is true and all else fails, finally do this."

The general syntax looks something like the following:

```c
if (condition) {
   // if condition is true run this code
} else if(another_condition) {
   // if the above condition was false and this condition is true,
   // run the code in this block
} else {
   // if the two above conditions are false run this code
}
```


### What Is An Example Of An `else if` Statement? <a name="example-else-if"></a>

Let's see how an `else if` statement works.

Say you have the following example:

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Please enter your age: ");

   scanf("%i", &age);

   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   }  else if (age < 21) {
       printf("You need to be over 21\n");
   } else {
      printf("You are over 18 and older than 21 so you can continue \n");
  }
  
   }
```

If the first `if` statement is true, the rest of the block will not run:

```
#output

Please enter your age: 17
You need to be over 18 years old to continue
```

If the first `if` statement is false, then the program moves on to the next condition.

If that is true the code inside the `else if` block executes and the rest of the block doesn't run:

```
#output

Please enter your age: 20
You are need to be over 21
```

If both of the previous conditions are all false, then the last resort is the `else` block which is the one to execute:

```
#output

Please enter your age: 22
You are over 18 and older than 21 so you can continue 
```

## Conclusion

And there you have it – you now know the basics of `if`, `if else`, and `else if` statements in C!

I hope you found this article helpful.

To learn more about the C programming language, check out the following free resources:

- [C Programming Tutorial for Beginners](https://www.youtube.com/watch?v=KJgsSFOSQv0)
- [What is The C Programming Language? A Tutorial for Beginners](https://www.freecodecamp.org/news/what-is-the-c-programming-language-beginner-tutorial/)
- [The C Beginner's Handbook: Learn C Programming Language basics in just a few hours](https://www.freecodecamp.org/news/the-c-beginners-handbook/)

Thank you so much for reading and happy coding :)


