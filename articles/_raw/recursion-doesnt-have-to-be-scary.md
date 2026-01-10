---
title: Recursion Might Seem Scary – But it Doesn't Have to Be
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-07T16:59:53.000Z'
originalURL: https://freecodecamp.org/news/recursion-doesnt-have-to-be-scary
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/recursion-image.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Recursion
  slug: recursion
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dave Gray

  Any concept that we don''t fully understand can be scary at first.

  Recursion is a topic that programming students don''t learn right away. But that
  doesn''t mean it needs to be scary or cause anxiety.

  In fact, recursion is a concept that we...'
---

By Dave Gray

Any concept that we don't fully understand can be scary at first.

Recursion is a topic that programming students don't learn right away. But that doesn't mean it needs to be scary or cause anxiety.

In fact, recursion is a concept that we can define rather simply.

According to [Wikipedia](https://en.wikipedia.org/wiki/Recursion_(computer_science)):

> In computer science, recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.

And you can apply recursion in your code by creating a function that calls itself.

## Any function with a loop can be recursive instead

Here is a function called `countToTen` that uses a while loop to log every number from one to ten:

```js
const countToTen = (num = 1) => {
    while (num <= 10) {
        console.log(num);
        num++;
    }
}

countToTen();

```

We can write the same function with recursion instead of a loop.

Notice that recursive functions have two parts:

1. The function calls itself (also known as the recursive call)
2. At least one condition to exit the recursion (also known as the base case)

```js
const countToTen = (num = 1) => {
    if (num > 10) return; //base case
    console.log(num);
    num++;
    countToTen(num); //recursive call
}

countToTen();

```

That's not to say we **should** **always** replace loops with recursion.

There are instances where using recursion is the best choice – and likewise, there are instances where it is not the best choice.

## Why Use Recursion

Let's look at some reasons to use recursion. We'll see some examples below.

### Fewer Lines of Code

Applying recursion usually results in a solution with fewer lines of code than a solution that does not utilize recursion.

### More Elegant Code

In addition to fewer lines of code, recursive solutions are typically more pleasing to look at. In other words, recursive solutions are usually considered to be elegant.

### Increased Readability

Reasons 1 and 2 typically combine to create reason 3 which is the increased readability of your code. Remember, we do not write code just for ourselves. We write code for the developers that follow us and must understand our code.

## Reasons NOT to Use Recursion

### Performance losses

Repeating function calls is not as efficient or performant as applying a loop. We do not want to simply choose recursion because we can.

### Debugging Issues

The logic of recursion is not always easy to follow. Utilizing recursion may make your code more difficult to debug.

### Is the Readability Improved?

Increased readability is not guaranteed through the use of recursion. In fact, this may by opinionated and/or situational. You should evaluate the readability, and if it's not improved recursion may not be the best answer.

## Recursion Examples

Recursion problems are interview favorites.

One such problem asks for a function that returns `x` numbers of the Fibonacci sequence.

The Fibonacci sequence adds the two previous numbers of the sequence to create the next number in the sequence. Here are the first ten numbers of the sequence:  
`[0,1,1,2,3,5,8,13,21,34]`

We can write this function without recursion:

```js
const fibonacci = (num = 2, array = [0, 1]) => {
    while (num > 2) {
        const [nextToLast, last] = array.slice(-2);
        array.push(nextToLast + last);
        num -= 1;
    }
    return array;
}

console.log(fibonacci(10));

```

And here is a recursive version of the same function:

```js
const fibonacci = (num = 2, array = [0, 1]) => {
    if (num < 2) return array.slice(0, array.length - 1);
    const [nextToLast, last] = array.slice(-2);
    return fibonacci(num - 1, [...array, nextToLast + last]);
}

console.log(fibonacci(10));

```

The recursive function does have fewer lines of code. But I am not sure if we can confidently say it is has increased elegance or readability.

Let's look at another problem where recursion has a greater impact.

Another interview favorite is asking for a function that returns the nth number in the Fibonacci sequence. Therefore, if the function receives `10` as a parameter, it should return `34`.

Without the use of recursion, a possible solution looks like this:

```js
const fibonacciPos = (pos = 1) => {
    if (pos < 2) return pos;
    const seq = [0, 1];
    for (let i = 2; i <= pos; i++) {
        const [nextToLast, last] = seq.slice(-2);
        seq.push(nextToLast + last);
    }
    return seq[pos];
}

console.log(fibonacciPos(10));

```

However, with recursion, the solution is much smaller and arguably more elegant:

```js
const fibonacciPos = (pos = 1) => {
    if (pos < 2) return pos;
    return fibonacciPos(pos - 1) + fibonacciPos(pos - 2);
}

console.log(fibonacciPos(10));

```

Wow! That made a huge difference.

Notice how the return line actually calls the function twice.

Do you understand the logic in these recursive functions? If not, spend some time experimenting with them to understand how they work. After you do, you will likely agree that the readability is improved as well.

To highlight how improved readability is opinionated, let's look at the same recursive function from above written in one line (the line may wrap in your browser, but it is one line of code):

```js
const fibonacciPos= pos => pos < 2 ? pos : fibonacciPos(pos - 1) + fibonacciPos(pos - 2);

console.log(fibonacciPos(10));

```

Our original recursive solution went from four lines of code to just one!

Is it more readable to you? Do you still follow the logic behind it?

Your response will depend on your current level of understanding. The one line solution utilizes a ternary statement, features an arrow function without parentheses which also implies a return statement, and applies recursion as before.

I do not usually write functions like the one line solution above because I frequently teach beginning web development courses. Therefore, I often break my code into deliberate steps that are easier to follow.

That's not to say there is anything wrong with the one line solution above.

In fact, the function is elegant, readable, and highly efficient if you understand the logic behind it.

If you are working on a team, your team might have a style guide. If a one line function is preferred when possible, go for it! If a more deliberate, step-by-step style is preferred, follow your guide. These decisions are completely situational.

## Conclusion

Recursion can seem scary, but it doesn't have to be.

We can break the concept of recursion down to a simple definition.

Do not wield the power of recursion just because you can.

You should base the decision to use recursion in your code upon efficiency, performance, elegance, and readability.

You may be wondering where recursion might be applied in the "real world" instead of just answering Fibonacci sequence interview questions.

I'll leave you with a tutorial from my Youtube channel. I not only take a deeper look at the examples above, but I also reveal some "real world" instances where applying recursion is the best choice:

%[https://youtu.be/Q0alTGQ-lXk]


