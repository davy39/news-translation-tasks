---
title: How to Find the Number of Vowels in a String with JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-18T17:27:04.000Z'
originalURL: https://freecodecamp.org/news/find-the-number-of-vowels-in-a-string-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-17-at-6.16.19-PM.png
tags:
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
- name: Problem Solving
  slug: problem-solving
seo_title: null
seo_desc: "By Madison Kanna\nIn this tutorial, we’ll learn how to find the number\
  \ of vowels in a string with JavaScript. This is a problem you might be asked in\
  \ junior developer job interviews, and it’s also a CodeWars problem. \nBefore we\
  \ get started coding, let..."
---

By Madison Kanna

In this tutorial, we’ll learn how to find the number of vowels in a string with JavaScript. This is a problem you might be asked in junior developer job interviews, and it’s also a [CodeWars](https://www.codewars.com/kata/54ff3102c1bad923760001f3) problem. 

Before we get started coding, let’s read over the problem description in full:

**Return the number (count) of vowels in a given string. We will consider a, e, i, o and u as vowels, but not y. The input string will only consist of lower case letters and/or spaces.**

## Step 1: Make a plan to solve the problem

For this problem, we’ll create a function, called `getCount`, which takes as input a string and returns as output the count of how many vowels are in that string.  
  
Let’s go over some examples.

![Image](https://lh4.googleusercontent.com/0NnD6g02UboUYJkZ0KOJMw7abNXVH-e9iuq9kv1qg-OFzJ_k8t3ZVfMzj6MkPE45fjQxVBIshpJJNxF_e6KGDWSCdwp7BWd8vVasgeiJ1nYiK-7ufFJz1XuyIXcHNApmtBhn7Kk9)

With the first example, we see that our function returns 5, which is how many times a vowel appears in the string `abracadabra`. With the string `abc`, only 1 is returned, as only one vowel (a) appears.

To solve this problem, we’ll create a `vowelsCount` variable that will keep track of how many vowels are in the string. 

We’ll also create an array, vowels, that holds all of our vowels. We’ll go through each character in our string. If the character is a vowel, we’ll increase our `vowelsCount` variable.

Finally, we’ll return the `vowelsCount` variable.  
  
Let’s get started!

## Step 2: Write the code to solve the problem

First we write our function, `getCount`. Next we’ll create a variable, `vowelsCount`, and set it to `0`.

![Image](https://lh4.googleusercontent.com/3C2OuHNi9S9SL-SUEYzM8PSodXO1bYULEd9LLec7clus1o5TEvqBBgVy1STfDUoq3hFLT85VLVGAAzL8h949fazt9_36S54Oe97U39IjJhl9LBDTWCpSFd9w9wMFpkHdfSbeFpAq)

  
We’ll create our vowels array next. This allows us to have every vowel in one place, and we can use this array later.

![Image](https://lh6.googleusercontent.com/g6F__ll7kJNmOq6c3kT6Z7X_zcslPkO8AuF5kUDYFcLcnJ9v-rpf3bm1NUSDPCAVWWnfpq9GS7cADMuN5GS3CdiTbAfun9Gth0CBUFGFl5vhviLMrKHKfQa9KPfWkujtV1_SLWHG)

  
Now we need to go through every character in our input string, `str`. We need to go through or look at every character in our string so that we can determine whether or not it is a vowel.

To do this, we can use the `for...of` statement that works on strings. You can read more on it [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of).

![Image](https://lh3.googleusercontent.com/mMSkKHhYAhJxh9F71Ccs4B9MyKpjHNlyIumJwJ9n7bTo-o6eR1YQLHsPe13VCVx7XlFU20TQHr2B5bXv52cbIHvTs2Jl2xIwBPo5hD0-ILOAW-o66sG2uyxUF5WljDTgDrsqgP7X)

  
Now inside our for loop, we have the ability to look at and go over each character in our string.   
  
Next, we want to check whether or not each character is a vowel. 

To do this, we can use the `includes` method. The `includes()` method determines whether an array includes a certain value among its entries. It returns true if so, and false if not. 

Using `includes`, we’ll check if our vowels array contains the character we’re currently iterating over in our loop.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-89.png)

We’ve created our `if statement` to check whether the current character is a vowel. If the character is a vowel, then we want to increase our `vowelsCount` variable. To do this, we can use the increment operator in JavaScript:

![Image](https://lh4.googleusercontent.com/YELFhUaEOI51eOBznA9delrQlT5_brpGzM71vXiO6S1ARcy-IAbM06mYgPr6zQVC-0eytb87eQX8_5UBcZ0rMPLfTpf3uGHbJhpTWymoXGwLMDscQbp9BR1SIzbsrQSssmH689t2)

  
At this point in our code, we’ve looked at each character in the string, determined whether it was a vowel or not, and increased the number we stored in `vowelsCount` if it was.

Lastly, all we need to do is have our function return our `vowelsCount` variable. We can do this by returning the variable outside of our loop.

![Image](https://lh6.googleusercontent.com/4U_WmVuqES_Z5Tb79te7k7nCorSGuIvsKoWVXPjV1e7dug-pSylt7GMa7MNvkDBX-1PT0EtfFmCi0n-pqN0YGpo2Rs7xntRQViCzLBEYuVi0rDJOQsQJxkgScPdGHXT8ThDLvn5I)

  
There we have it.

## That's it!

We’ve now written a function that will take as input a string and return as output the number of times a vowel appeared in the string. 

### If you enjoyed this post, join my [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), where we tackle coding challenges together every Sunday.  
  
If you have feedback or questions on this post, feel free to Tweet me @madisonkanna.

  

