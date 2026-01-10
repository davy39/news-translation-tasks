---
title: Do While Loops in C++ with Example Loop Syntax
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-15T21:27:02.000Z'
originalURL: https://freecodecamp.org/news/do-while-loops-in-c-plus-plus-example-loop-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98af740569d1a4ca1b76.jpg
tags:
- name: C++
  slug: c-2
- name: Loops
  slug: loops
seo_title: null
seo_desc: "By Patrick Loeber\nLoops are control flow statements that allow code to\
  \ be executed repeatedly based on a given condition. \nThe do while loop is a variant\
  \ of the while loop that executes the code block once before checking the condition.\
  \ Then it will ..."
---

By Patrick Loeber

Loops are control flow statements that allow code to be executed repeatedly based on a given condition. 

The `do while` loop is a variant of the `while` loop that executes the code block once before checking the condition. Then it will repeat the loop as long as the condition is true.

## Syntax

Here's the basic syntax for a do while loop:

```c++
do {
    // body of the loop
}
while (condition);
```

Note that the test of the termination condition is made after each execution of the loop. This means that the loop will always be executed at least once, even if the condition is false in the beginning.

This is in contrast to the normal `while` loop, where the condition is tested before the loop, and an execution of the code block is not guaranteed.

Now here's a regular while loop:

```c++
while (condition) {
    // body of the loop
 }
```

## Example of a do while loop

Let's look at a working example:

```c++
#include <iostream>
 
int main () {
   
    int number = 1;

    do {
        std::cout << number << std::endl;
        number++;
    }
    while (number < 5);
 
    return 0;
}
```

Output:

```
1
2
3
4
```

In this example we initialize an integer variable `number = 1`. We then repeatedly execute the loop. 

Inside the loop we print the variable and increase the variable by one. The loop is executed as long as `number` is smaller than 5. Hence, the numbers from 1-4 are printed.

## Example 2

Here's another example and its output:

```
10
```

```c++
#include <iostream>
 
int main () {
   
    int number = 10;

    do {
        std::cout << number << std::endl;
        number++;
    }
    while (number < 5);
 
    return 0;
}
```

In this example we use the same code as in the first example. But now we initalize our variable with `number = 10`. 

Since 10 is not smaller than 5, our condition is already false. The loop will still be executed once, and 10 is the only printed output.

## When Should You Use the Do While Loop?

The `do while`loop is a great tool if you need code to be executed repeatedly. As stated above, you want to use this syntax whenever you need a loop, and you also need to guarantee that at least one execution of the code block is performed.

Imagine some code like in Example 2, but we don't initialize our variable with a hard coded value. Instead we use a user input. 

We cannot guarantee that the user input is small enough, but we still want to see at least one print statement in the output console. This is a perfect use case for the `do while`loop.

```c++
// Pseudo code where do while is useful:

int number = getUserInput();

do {
    std::cout << number << std::endl;
    number = someUpdateCalculation();
}
while (number < 5);
```


