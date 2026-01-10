---
title: How to Flatten an Array in JavaScript Using Recursion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-18T15:11:05.000Z'
originalURL: https://freecodecamp.org/news/flatten-array-recursion
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-damon-hall-1705254.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: null
seo_desc: 'By Adwaith KS

  In this tutorial, we''ll go through a common coding problem that interviewers love
  to ask candidates. Hopefully this will help you understand how to think through
  it and solve it.

  Let''s begin by understanding the problem. You are given a...'
---

By Adwaith KS

In this tutorial, we'll go through a common coding problem that interviewers love to ask candidates. Hopefully this will help you understand how to think through it and solve it.

Let's begin by understanding the problem. You are given an array which contains numbers and nested arrays of numbers. Your job is to return a new array which contains all the numbers in a linear fashion without any nesting. Keep in mind that the nesting can be any level deep. 

Here's an example:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Dribbble-shot---1-2.png)
_Example input and output_



Now, what comes to your mind when you hear the word **nesting**? Well, a concept which should come to your mind is **Recursion**. 

## **What is Recursion?**

Recursion simply means a function that calls itself. Immediately, you might ask if a function keeps on calling itself, will it be an infinite loop? Yes – you are right! 

To deal with that, we use some **conditions** (most probably an if condition) to stop the recursive function calls, once we are done with our task. These conditions are called **Base Cases**.

Let's start with an example. Suppose I want to print the numbers from 1 to N (inclusive). Typically, you'd write a for loop for it, right? Something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-1.svg)
_Function to print 1 to N (Iterative solution)_

What if I want to write the code to print 1 to N using recursion?

To write a recursive function for the above, we have to ask the following two questions:

1. When should our recursive function stop? Answer: On reaching N + 1, since we have to print from 1 to N **inclusive**.
2. What is the actual work that our recursive function should do? Answer: Printing values to console.

So in short, **keep on printing values until we reach N + 1.**

According to the second question we just discussed now, our code should look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-3-2.svg)

Above piece of code also prints 1 to N (5), right? The actual work that this piece of code does is to print values to the console.  

Now, instead of calling the same function manually, let's make the code do it for us. Something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-6.svg)

If you carefully observe the above code, line 6 `print1ToNo(currentValue + 1)` is calling the same function with a new value (whatever the currentValue was, plus 1, i.e currentValue + 1). And it keeps doing it, **until the currentValue goes past N**, because that's when we told it to **return**. Now, this is what recursion means. 

## How to Think the Recursive Way

Now, let's get back to our main problem – we need to **flatten an Array**. Assume that we have just one level of nesting (of course, we can have multiple nestings, but for now we'll deal with one). The array should look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Dribbble-shot---1-4.png)
_Example input - 1 level nesting_

We will walk through the input array index by index.

### Index 0, Value = 1

Index 0 contains a number (value = 1). It is just a number and not an array. Do we need to flatten numbers? No! They are going to be part of the output array as such. That is, we don't need to do anything special to numbers, we only pay special attention to arrays. 

So, our rule is, if it's a number, push it to the output array and move on to the next index (that is index 1 here).

### Index 1, Value = 2

Index 1 also contains a number (value = 2).  Do we need to flatten numbers? No! They are going to be part of the output array as such. 

So, following our rule, if it's a number, push it to the output array and move on to the next index (index 2 here).

### Index 2, Value = [ 3, 4 ]

Now, **index 2 is an array ([ 3, 4 ])** and not a number. So now we will have to think of some way to flatten it. 

What if I gave you an array [3, 4] and told you to flatten it? You would start going through the array elements index by index like we did previously. Then you might realize that 3 is just a number, so push it to the output array and move on to the next index. 

Well in the next index, 4 is also just a number, so push it to the output array. And we're done! Well, why don't you do that same on `**index 2 ( [ 3, 4 ] )**` of our input array, then?

You must be wondering, well it's easy to say that! How are going to do that in code!? **This is where recursion comes into the picture.** Whenever we encounter an array, we will tell the recursive function to take that array as a new input and solve it for us. 

Putting everything into context, if it's just a number, don't do anything, just push that number to our output array and move on to the next index. 

If it's an array, then take that array as a new input and start doing what we did previously. (We'll do this part using recursion)

## Solution to the Problem

Alright, just as a reminder, here's our problem:

You are given an array which contains numbers and nested arrays of numbers. Your job is to return a new array which contains all the numbers in a linear fashion without any nesting. Keep in mind that the nesting can be any level deep. 

Here's the solution to our problem using recursion:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-3.svg)
_Solution - Code_

If you carefully look at the function named **recursion** in the above code snippet, we are checking if the array element that we are currently at is an array or not. The variable named **`index`** is used to represent current index we are on, in the `**inputArray**`. 

If it's not an array, we just push that element into our output array and move on to next index. Otherwise, we start a new function call (recurse) with the array pointed by the index variable.

This piece of code works for any level of nesting, not just 1 level of nesting! And why is that? Whenever we find an array and not a number, we initiate a new recursive call with that array as our input to the recursive call. 

So, no matter how many nested arrays we have, recursion will keep on going until we find a number, so that we start pushing it to the output array!

This is how the recursion works behind the scenes (for the previous example): 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Dribbble-shot---1.svg)
_How things are getting done!_

## Conclusion

Now, you know how to flatten an array using recursion. Recursion is an expensive approach when it comes to time and space complexity. 

For example, the only extra space we're using in our solution is the `**outputArray**`, that we are using to store the answer of our problem. 

But, that's not the only space we are using! There is always an auxiliary stack space that we are using when we use recursion. 

How big is this auxiliary stack space? Well, recursive functions are called over and over again until the base condition is met, right? These repeated function calls are placed inside the call stack and popped when each function is completed. So, the maximum height of the stack (represents how deep our recursive calls went) is what comprises of the auxiliary stack space. Something like **`O(h) space, where h is the maximum height of the stack`**. 

Now, when it comes to time complexity, it depends on the input. For example: `**[1 , 2, 3, 4, 5]**`**.** An input like this doesn't need any flattening, but still we traverse the whole array once. So, time complexity is `**O(n) where n is the number of elements**`. 

Now what about for this example? `**[ [ 1, 2 ], 3, 4, [ 4, [ 5 ] ] ]**` Here we have 2 options: If it's an array, call the recursive function with that array, as our new input array. If it's a number, push it to our output array and then recurse to the next index. 

So, the time complexity is going to be nearly exponential. Recursion is rarely used in production environments. But you'll see it in technical interviews a lot :)

