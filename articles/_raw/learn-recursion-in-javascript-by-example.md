---
title: Recursion in JavaScript Explained Using a freeCodeCamp Challenge
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T20:51:53.000Z'
originalURL: https://freecodecamp.org/news/learn-recursion-in-javascript-by-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Marketing-Business-Corporate-Start-up-Facebook-Cover--1--1.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: null
seo_desc: "By Nehemiah Kivelevitz\nIn this article I will touch on a few important\
  \ ideas to help you understand Recursion in JavaScript. I’m not going to give a\
  \ full definition here, but you can take a look at what Wikipedia has to say. \n\
  Let’s agree for the purp..."
---

By Nehemiah Kivelevitz

In this article I will touch on a few important ideas to help you understand Recursion in JavaScript. I’m not going to give a full definition here, but you can take a look at what Wikipedia [has to say](https://en.wikipedia.org/wiki/Recursion_%28computer_science%29). 

Let’s agree for the purpose of this article that we are trying to solve a problem by using a function that will then call itself.

## The Challenge

At the end of the Javascript Algorithms and Data Structures — Basic Javascript section [on freeCodeCamp](https://www.freecodecamp.org/learn/), you run into an interesting problem: ‘Use Recursion to Create a Range of Numbers’, where the instructions are as follows:

> We have defined a function named rangeOfNumbers with two parameters. The function should return an array of integers which begins with a number represented by the startNum parameter and ends with a number represented by the endNum parameter. The starting number will always be less than or equal to the ending number. Your function must use recursion by calling itself and not use loops of any kind. It should also work for cases where both startNum and endNum are the same.

Sounds simple enough – if you were to run rangeOfNumbers(1, 5) it should return [1, 2, 3, 4, 5].

If you’re like me, you can sort of intuit the answer based on the previous example in this section. But it might still be a bit unclear how this all works.

**Spoiler alert:** you'll find an answer immediately below. But this isn’t much of a spoiler since the answer is easy enough to find on the internet.

## My Solution

It’s very probable that you can read through the code and understand that when it gets down to its **base case** it will return whatever the startNum is into the array. Then it will keep pushing the other values onto that array until it’s done with all of its recursive calls.

```javascript
function rangeOfNumbers(startNum, endNum) {
    if (startNum === endNum) {
        return [startNum];
    } else {       
        const numbers = rangeOfNumbers(startNum, endNum - 1);
        numbers.push(endNum);
        return numbers;
    }
}
```

What I found to be tricky was understanding exactly **how** the call stack was working and how my values were being returned.

So let's break down how this function will return its final value.

### The Call Stack

The first thing to understand is how the **call stack** works. I will refer you to Mozilla Developer Network's [explanation](https://developer.mozilla.org/en-US/docs/Glossary/Call_stack):

> When a script calls a function, the interpreter adds it to the call stack and then starts carrying out the function.  
>   
> Any functions that are called by that function are added to the call stack further up, and run where their calls are reached.  
>   
> When the current function is finished, the interpreter takes it off the stack and resumes execution where it left off in the last code listing.

Using this explanation, let’s run the code above using _rangeOfNumbers(1,5)._

First the rangeOfNumbers — Execution Context is created and executed with the following values:

![screenshot of code](https://www.freecodecamp.org/news/content/images/2020/06/numberrange.png)
_Screenshot from [http://www.pythontutor.com/javascript.html](http://www.pythontutor.com/javascript.html" data-href="http://www.pythontutor.com/javascript.html" class="markup--anchor markup--figure-anchor" rel="noopener" target="_blank)_

So we have added an unresolved _rangeOfNumbers(1,5)_ function call to our stack. Then we move on to create the execution for _rangeOfNumbers(1,4)_, and so on and so forth, adding each one of these calls to our stack until we will finally **resolve** a function call. Then the interpreter will take that function off the stack and move on to the next one.

### Examining Our Call Stack

So our stack will end up looking like this:

```
rangeOfNumbers(1,1)
rangeOfNumbers(1,2)
rangeOfNumbers(1,3)
rangeOfNumbers(1,4)
rangeOfNumbers(1,5)
```

_rangeOfNumbers(1,1)_ will be the last one in our stack because, finally, this call will **RETURN** a value allowing us to move on to our next function in the stack.

_rangeOfNumbers(1,1)_ return value is [1], as we had assumed it would be since it is our base case. Now we pop _rangeOfNumbers(1,1)_ off our stack, and go back to where _rangeOfNumbers(1,2)_ left off…

```
var numbers = rangeOfNumbers(1,2) // returns an array of [1]
```

Numbers is no longer _undefined_ and the next step is to push the _endNum_, which is 2, into the numbers array. This gives us [1,2] in numbers, and now we return the value.

```
numbers.push(endNum) //numbers now holds an array of [1,2]
return numbers; // ends our function and returns [1,2]
```

### Breaking Down The Tricky Part

So we pop off _rangeOfNumbers(1,2)_ which had a return value of [1,2]. Let’s resume with the next call in our stack _rangeOfNumbers(1,3)._ Numbers is currently [1,2] because that is the return value of _rangeOfNumbers(1,2)._ This is what we had plugged in when we called _rangeOfNumbers(1,3)_ because, again, the 3 is subtracted by 1, that is _rangeOfNumbers(1,2)_, which as we said returns [1,2]. 

Got it? Great! If you don’t get it, reread this paragraph, because this is the trickiest part to understand.

If you’re up to speed let’s continue. If that part above clicked the rest should feel pretty easy.

Back to _rangeOfNumbers(1,3)_: the numbers array is currently [1,2], so we push the _endNum_ which is 3. Now we have [1,2,3] and we return this value again. We remove _rangeOfNumbers(1,3)_ from our stack which returned the value [1,2,3]. 

How did we get rangeOfNumbers(1,3)? That’s right, from when we called _rangeOfNumbers(1,4)_ and endNumb -1, that is → 3, and we know that _rangeOfNumbers(1,3)_ gives us the return value of [1,2,3] which is exactly what we have in our array. 

Now we push the _endNum (also known as 4)_ onto the numbers array, giving us [1,2,3,4] and we return this value. Let’s again remove this function call from the stack since it gave us what we wanted.

### Bringing it all together 

Now for the call that started it all: _rangeOfNumbers(1,5)_. The first step we do is determine what value we have in numbers. When put in _rangeOfNumbers(1,4)_ we get, as we said before, [1,2,3,4]. So we can now push our _endNum_ 5 into the array and get [1,2,3,4,5] which we will return, and our stack is now empty with our last call.

So let’s quickly review which returned what value and in what order.

```
rangeOfNumbers(1,1) → returns [1]
rangeOfNumbers(1,2) → returns [1,2]
rangeOfNumbers(1,3) → returns [1,2,3]
rangeOfNumbers(1,4) → returns [1,2,3,4]
rangeOfNumbers(1,5) → returns [1,2,3,4,5]
```

If this is still confusing, firstly I understand – it’s a confusing topic. Next I would recommend typing in your code into this great tool: [http://www.pythontutor.com/javascript.html](http://www.pythontutor.com/javascript.html)

This is all able to work because we started with a small base case and we essentially built our way back up. Each time our return value is a bit bigger than it was on its previous call, much like if you were to perform this same operation with a for loop.

Have any questions? Feel free to ask me on Twitter: [@NehemiahK](https://twitter.com/NehemiahKiv)iv

