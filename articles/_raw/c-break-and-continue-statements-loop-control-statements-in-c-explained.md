---
title: C Break and Continue Statements – Loop Control Statements in C Explained
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-11-04T18:56:12.000Z'
originalURL: https://freecodecamp.org/news/c-break-and-continue-statements-loop-control-statements-in-c-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/markus-spiske-C0koz3G1I4I-unsplash--1-.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'In the C programming language, there are times when you''ll want to change
  looping behavior. And the continue and the break statements help you skip iterations,
  and exit from loops under certain conditions.

  In this tutorial, you''ll learn how break and...'
---

In the C programming language, there are times when you'll want to change looping behavior. And the `continue` and the `break` statements help you skip iterations, and exit from loops under certain conditions.

In this tutorial, you'll learn how `break` and `continue` statements alter the control flow of your program.

Let's get started.

## How to Use `break` to Exit Loops in C

In C, if you want to _exit_ a loop when a specific condition is met, you can use the `break` statement.

As with all statements in C, the `break` statement should terminate with a semicolon (`;`).

Let's take an example to understand what this means.

Consider the following code snippet. 

```c
#include<stdio.h>
int main()
{
    int count = 0;
    while(count < 100)
    {
        printf("The value of count is %d \n", count);
        count++;
    }
    return 0;
}
```

In this example, the `while` loop repeats the statements in the loop body so long as `count` is less than 100. 

The count starts at 0, and increases by 1 with every iteration.

Now, this is the normal control flow.

Let's modify this a bit.

* Read in an integer `fav_num` from the user. Let's suppose `fav_num` is the user's favorite number from the set `{0, 1, 2, ..., 99}`.
* During each pass through the loop, you've to check if the current value of `count` is equal to `fav_num`.
* You'd like to exit the loop when `count` equals `fav_num`.

So how do you do this?

Read through the following code snippet:

```c
#include<stdio.h>
int main()
{
    // Read in the user's favorite number
    int fav_num;
    printf("Enter your favorite number from 0 to 99: ");
    scanf("%d", &fav_num);
    
    int count = 0;
    while(count < 100)
    {
        printf("\nThe value of count is %d.", count);
        if (count == fav_num)
    		break;
        count++;
    }
    return 0;
}
```

* During each pass through the loop, you use `if (count == fav_num)` to check if `count` equals `fav_num`.  And you add the `break;` statement to the `if` statement's body.
* So long as `count ≠` fav_num, the control never reaches the `break;` statement.
* When `count` equals `fav_num`, the `break;` statement is triggered, and then you exit the loop.
* The control now reaches the first statement outside the loop. 

A sample output is shown below:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-1.png)

Notice how the control exits the loop once the count reaches `3`, which here is `fav_num`.

In the next section, you'll see yet another example that'll reinforce your understanding.

### C `break` Statement Example

▶ Consider the following example:

* `A[10]` is an array of 10 integers, and is initialized with zeros.
* You'd like to read in the elements of the array `A` from the user. And compute the sum of elements in the array.
* However, you require that each element of `A` is no greater than `20`.
* Once the user enters a number that's greater 20, you choose to terminate the loop. Here's where the `break;` statement comes in handy.

Now, read through the following code snippet that does exactly this.

```c
#include <stdio.h>

int main()
{
    int A[10] = {0};
    int sum = 0;
    
    for(int i = 0; i < 10; i++)
    {
        printf("Enter a number: ");
        scanf("%d",&A[i]);
        if (A[i] > 20)
            break;
        
        sum += A[i];
    }
    printf("Sum: %d",sum);
    return 0;
}

```

* Here, `sum` is initialized to `0`.
* In every pass through the loop, the user is prompted to enter a number. And the entered number is added to the current value of `sum`.
* If the user enters a number that's greater than 20, the control exits the loop.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-191.png)

Notice how the loop terminates once the user inputs a number that's greater than `20` – in this case `21`. And the sum of the other two numbers (2 and 3) is printed out.

If you've used the `switch` statement in C, you'd have likely used the `break;` statement to exit the case ladder as soon as a matching case label is found.

However, this tutorial is aimed at teaching how to use the `break;` and `continue;` statements to change looping behavior.

## How to Use `continue` to Skip Iterations in C

In C, if you want to skip iterations in which a specific condition is met, you can use the `continue` statement.

> Unlike the `break` statement, the `continue` statement does not exit the loop. Rather, it skips only those iterations in which the condition is true. 

Once the `continue;` statement is triggered, the statements in the remainder of the loop are skipped. And the loop control continues to the next iteration.

### C `continue` Statement Example

Let's use the example from the previous section, and modify it a bit.

Say you don't want to exit the loop when the user inputs a number greater than 20. Rather, you'd like to ignore those particular inputs, and compute the sum of the remaining numbers in the array `A`.

* Suppose the user inputs 10 numbers, 3 of which are greater than 20. 
* Your code should now compute and display the sum of the remaining 7 numbers.

So how do you do it?

> You can use the `continue;` statement to skip only those iterations for which the user's input was greater than 20. 🙂

And you can do it as shown in the code below:

```c
#include <stdio.h>

int main()
{
    int A[10] = {0};
    int sum = 0;
    
    for(int i = 0; i < 10; i++)
    {
        printf("Enter a number: ");
        scanf("%d",&A[i]);
        if (A[i] > 20)
            continue;
        
        sum += A[i];
    }
    printf("Sum: %d",sum);
    return 0;
}
```

In the sample output, you can see that the very first input is `21` which is greater than `20`. 

However, the loop does run 10 times. And if you're up for a quick addition exercise, you can see that the numbers other than 21 (2, 3, 5, 4, 7, 15, 14, 2, and 5) indeed add up to 57. ✅

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-192.png)

## Conclusion

In this tutorial, you've learned how you can use the `break;` and the `continue;` statements to control loops in C.

To sum up, you've learned:

* how the `break;` statement helps exit loops under specific conditions.
* how the `continue;` statement helps skip iterations under specific conditions.

Hope you found this tutorial helpful. Happy coding! 😄

