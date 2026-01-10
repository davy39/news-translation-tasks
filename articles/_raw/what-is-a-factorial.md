---
title: What is a Factorial? How to Calculate Factorials with Examples
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-08-03T16:32:53.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-factorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/antoine-dautry-_zsL306fDck-unsplash.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: null
seo_desc: 'A factorial is a mathematical operation that you write like this: n!. It
  represents the multiplication of all numbers between 1 and n.

  So if you were to have 3!, for example, you''d compute 3 x 2 x 1 (which = 6). Let''s
  see how it works with some more ...'
---

A factorial is a mathematical operation that you write like this: `n!`. It represents the multiplication of all numbers between 1 and n.

So if you were to have `3!`, for example, you'd compute 3 x 2 x 1 (which = 6). Let's see how it works with some more examples.

## Definition of a Factorial

The factorial of a number is the multiplication of all the numbers between 1 and the number itself. It is written like this: `n!`. So the factorial of 2 is `2!` (= 1 × 2).

To calculate a factorial you need to know two things:

1. `0! = 1`
2. `n! = (n - 1)! × n`

The factorial of 0 has value of 1, and the factorial of a number `n` is equal to the multiplication between the number `n` and the factorial of `n-1`.

For example, `5!` is equal to `4! × 5`.

Here the first few factorial values to give you an idea of how this works:

| Factorial | Multiplication | Result |
| -- | -- | -- |
| 0! | 1 | 1 |
| 1! | 1 | 1 |
| 2! | 1 × 2 | 2 |
| 3! | 1 × 2 × 3 | 6 |
| 4! | 1 × 2 × 3 × 4 | 24 |
| 5! | 1 × 2 × 3 × 4 × 5 | 120 |
| 6! | 1 × 2 × 3 × 4 × 5 × 6 | 720 |
| 7! | 1 × 2 × 3 × 4 × 5 × 6 × 7 | 5040 |
| 8! | 1 × 2 × 3 × 4 × 5 × 6 × 7 × 8 | 40,320 |
| 9! | 1 × 2 × 3 × 4 × 5 × 6 × 7 × 8 × 9 | 362,880 |

## What is a Factorial Used For?

Practically speaking, a factorial is the number of different permutations you can have with `n` items: 3 items can be arranged in exactly 6 different ways (expressed as `3!`). 

For example, let's see all the arrangements you can have with the three items, A, B and C:

```text
ABC
ACB
BAC
BCA
CAB
CBA
```

And in fact, `3! = 6`.

### How to Calculate the Factorial of 0

Looking at the factorial from this point of view, what's the factorial of 0?

Well, how many different ways can you arrange 0 elements? 

There is exactly 1 way to arrange zero elements. And that's making a sequence of zero elements.

### Factorial Use Cases

You typically use a factorial when you have a problem related to the number of possible arrangements. Let's look at some example problems.

#### Factorial example problem 1: the letters in the word "camper"

_How many different ways can you arrange the letters of the word `camper`?_

The word `camper` has 6 letters, so the number of possible arrangements is given by the factorial of 6: `6! = 6 × 5 × 4 × 3 × 2 × 1 = 720`. That would have been a pretty big number of arrangements to find by hand, wouldn't it?

#### Factorial example problem 2: drawing colored balls from a bag

Let's say there are three balls in a bag – one green, one blue, and one yellow.

If you draw the three balls in sequence, what chance is there that you'll get the yellow first, the green one second, and the blue one last?

Maybe now you are wondering what chances have to do with factorials – well, in a moment you will see.

There are 6 possible sequences in which the balls can be drawn: 3! = 6.

There is a chance of 1 over the total number of possibilities to get the yellow-green-blue sequence, so that is `1/(3!)` or `1/6` or `16.7%` chance to get the desired outcome.

## How to Calculate a Factorial Programmatically with JavaScript

There are two ways to calculate factorials programmatically in JavaScript:

### How to calculate a factorial in JS with recursion

Let's get back to the two things to know when calculating a factorial – that is `0! = 1` and `n! = (n - 1)! × n`. We can use the first one to create the base case of the recursive function, because in that case we know the result already.

```js
function factorial(n) {
  if (n === 0) {
      return 1;
  }
}
```

The second thing to know about how to calculate a factorial, `n! = (n - 1)! × n`, can be the recursive case.

```javascript
function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return factorial(n-1) * n;
    }
}
    
```

### How to calculate a factorial with a JavaScript `while` loop

We said before that `0! = 1`. So, to calculate the factorial of a number with a loop, we can initialize a variable to `1`, and multiply the numbers from `n` to `1` by the variable inside the loop.

In this way, if the input is higher than 1, the output will easily be 1.

```javascript
function factorial(n) {
    let result = 1;
    for (n > 1) {
        result *= n;
        n--;
    }
    return result;
}
```

## Conclusion

The factorial is a pretty important operator to know if you are interested in statistics and probabilities.

In this article you have learned a how to calculate a factorial, a simple application, and you have seen how to calculate it using JavaScript.

Have fun with it!

