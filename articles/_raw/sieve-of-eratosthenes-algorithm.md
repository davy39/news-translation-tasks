---
title: How to Use the Sieve Of Eratosthenes Algorithm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-12T18:25:20.000Z'
originalURL: https://freecodecamp.org/news/sieve-of-eratosthenes-algorithm
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Sieve-of-Eratosthenes-min.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Divine Orji

  One day, while learning algorithms in JavaScript, I found this challenge:


  Using a for loop, iterate from 0 to 100, and return an array of all prime numbers
  within that range.


  It seemed easy initially, but I couldn''t quite figure it o...'
---

By Divine Orji

One day, while learning algorithms in JavaScript, I found this challenge:

> Using a `for` loop, iterate from 0 to 100, and return an array of all prime numbers within that range.

It seemed easy initially, but I couldn't quite figure it out. So I did a google search and discovered an algorithm that does it perfectly: the **Sieve of Eratosthenes**.

## What is this _sieve_ you speak of?

The Sieve of Eratosthenes is an ancient math algorithm created by [Eratosthenes of Cyrene](https://en.wikipedia.org/wiki/Eratosthenes). It finds all prime numbers between 0 and a given limit.

## Interesting! How does the Sieve of Eratosthenes work?

Let's break it down:

* Our input is a positive number representing the limit.
* The algorithm loops through all numbers between 0 and our input.
* In each iteration, if the number is a prime, it marks all multiples of that number as non-primes.

Cool right?! Now let's solve our original challenge:

```jsx
function getPrimes(input) {
  // Create an array where each element starts as true
  const numsArr = Array.from({ length: input + 1 }, () => true);

  // Create an array to store the prime numbers
  const primeNumbers = [];

  /*
  Loop through numsArr starting from numsArr[2]
  because 0 and 1 are definitely not prime numbers
  */
  for (let i = 2; i <= input; i++) {
    // Check if numsArr[i] === true
    if (numsArr[i]) {
      // add the i to the primeNumbers array
      primeNumbers.push(i);

      /* 
      convert all elements in the numsArr 
      whose indexes are multiples of i 
      to false
      */
      for (let j = i + i; j <= input; j += i) {
        numsArr[j] = false;
      }
    }
  }

  return primeNumbers;
}

console.log(getPrimes(100));

```

In the code above, we did the following:

* Created an array of `true` elements. JavaScript arrays are zero-indexed, so we set `length: input + 1` to take advantage of that.
* Created `primeNumbers[]` to store the prime numbers.
* Used a `for` loop to iterate over each element in `numsArr[]`. If the current element is `true`, add it to `primeNumbers[]` and convert all elements in multiples of its index to `false`.
* Returned `primeNumbers[]`, which now contains all the prime numbers with 0 and our input.

So this works, but there’s a slight problem (or a major one, depending on the input size). At some point during the loop, all possible non-primes in the array are already `false`, but reaching a `true` element still triggers its nested loop. That’s redundant! 

Let’s optimize:

```jsx
// Sieve of Eratosthenes Algorithm

function getPrimes(input) {
  // Create an array where each element starts as true
  const numsArr = Array.from({ length: input + 1 }, () => true);

  // Loop through numsArr starting from numsArr[2]
  // keep running the loop until i is greater than the input's square root
  for (let i = 2; i <= Math.floor(Math.sqrt(input)); i++) {
    // Check if numsArr[i] === true
    if (numsArr[i]) {
      /* 
      convert all elements in the numsArr 
      whose indexes are multiples of i 
      to false
      */
      for (let j = i + i; j <= input; j += i) {
        numsArr[j] = false;
      }
    }
  }

  /*
  Using Array.prototype.reduce() method:
    loop through each element in numsArr[]
      if element === true, 
      add the index of that element to result[]
      return result
  */
  const primeNumbers = numsArr.reduce(
    (result, element, index) =>
      element ? (result.push(index), result) : result,
    []
  );

  // Return primeNumbers[]
  return primeNumbers;
}

console.log(getPrimes(100));

```

What’s happening in the code above?

Mathematically, it is impossible to get any new multiples past the square root of any given input. 

To put it simply, by the time we get to the square root of `input`, all possible multiples in `numsArr[]` would already be converted to `false`, so there’s no need to keep checking for multiples.

So here’s what we did:

* Updated the `for` loop to end when `i <= Math.floor(Math.sqrt(input))` is false.
* Used JavaScript’s `reduce()` method to loop through `numsArr[]` and return an array containing the `index` of all `true` elements.

**Fun fact:** This optimization will also work if we replace the first `for` loop with:

```jsx
// keep running the loop until input is less than i^2 (i squared)
for (let i = 2; i * i <= input; i++) {
  // same super-awesome code hehehe!
}

```

Try it!

## Nice! Are there any limitations to the Sieve of Eratosthenes? 👀

The Sieve of Eratosthenes works efficiently with small inputs - `n < 10 million` (_is 10 million small???_). However, larger inputs take a lot of time and memory. The [segmented sieve](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#:~:text=usually%20the%20case.-,Segmented%20sieve,-%5Bedit%5D) is a proposed solution to this issue.

## A few parting words

There are different versions of this algorithm, each tackling some of the limitations of the original. 

Learning this algorithm broadened my knowledge of nested loops, prime numbers, and time complexity. To explore these topics in-depth, Check out the resources below.

