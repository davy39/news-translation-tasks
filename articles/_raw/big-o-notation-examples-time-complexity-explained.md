---
title: Big O Notation Examples – Time Complexity and Algorithm Efficiency Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T15:50:42.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation-examples-time-complexity-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60625dd39618b008528a9495.jpg
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
seo_title: null
seo_desc: "By Jeremy L Thompson\nTime complexity analysis helps us determine how much\
  \ more time our algorithm needs to solve a bigger problem. \nIn this article, I\
  \ will explain what Big O notation means in time complexity analysis. We'll look\
  \ at three different a..."
---

By Jeremy L Thompson

Time complexity analysis helps us determine how much more time our algorithm needs to solve a bigger problem. 

In this article, I will explain what Big O notation means in time complexity analysis. We'll look at three different algorithms for checking if a number is prime, and we'll use Big O notation to analyze the time complexity of these algorithms.

## What does Big O Notation Mean?

Big O notation describes how an algorithm's estimated runtime increases when we increase the size of the problem we are solving.

Let's consider some hypothetical algorithms for sorting a list of numbers.

If we have an `O(n)` algorithm for sorting a list, the amount of time we take increases linearly as we increase the size of our list. 

A list that has 10 times as many numbers will take approximately 10 times as long to sort. This means that if sorting `10` numbers takes us `4` seconds, then we would expect sorting a list of `100` numbers to take us approximately `40` seconds.

If we instead have an `O(n²)` algorithm for sorting a list, then we should expect that the amount of time we take will increase quadratically as we increase the size of our list. 

A list that has `10` times as many numbers will take approximately `100` times as long to sort! This means that if sorting `10` numbers takes us `4` seconds, then we would expect sorting a list of `100` numbers to take us approximately `400` seconds.

The fastest algorithms for sorting a list are actually `O(n log(n))`.  
With these algorithms, we can expect that a list with `10` times as many numbers will take approximately `23` times as long to sort. 

In other words, if sorting `10` numbers takes us `4` seconds, then we would expect sorting a list of `100` numbers to take us approximately `92` seconds.

## Big O Example - Prime Number Checker

Now that we know what Big O notation tells us, let's look at how we use Big O notation in time complexity analysis.

In this section, we will look at three different algorithms for checking if a number is _prime_. By the definition of a _prime_ number, `num` is _prime_ if the only numbers that divide evenly into `num` are `1` and `num` itself.

### Algorithm 1 - Check All Possible Divisors

The simplest algorithm I can think of to check if a number is _prime_ is to check for any divisors other than `1` and `num` itself. 

In the `is_prime_all()` function below, I try dividing every number between `1` and `num` into `num` and check for a remainder.

I wrote this code in Rust so I could use [criterion](https://docs.rs/criterion) to benchmark the runtime, but time complexity analysis with Big O notation works the same way with every programming language. 

If you want to run criterion with this code on your computer, you can find the Rust source code on [GitHub](https://github.com/jeremylt/time_complexity).

```rust
pub fn is_prime_all(num: i64) -> bool {
    // Check for divisors of num
    for i in 2..num {
        if num % i == 0 {
            // Any divisor other than 1 or num means num is not prime
            return false;
        }
    }
    // No other divisors found means num is prime
    return true;
}

```

We have to check `num - 2` different numbers with this algorithm before we can say that `num` is prime, so this algorithm has time complexity of `O(num)` or `O(n)`. 

You probably noticed that we removed the `-2` from our Big O notation. When we are calculating the time complexity in Big O notation for an algorithm, we only care about the biggest factor of `num` in our equation, so all smaller terms are removed.

When I tested my function, it took my computer an average of `5.9` microseconds to verify that `1,789` is prime and an average of `60.0` microseconds to verify that `17,903` is prime. 

This means that it takes approximately `10` times longer to check a number that is `10` times larger, which we expected from our time complexity analysis!

### Algorithm 2 - Check Half of the Possible Divisors

We can improve our algorithm. If our number, `num`, is not divisible by `2`, then we also know that our number can't be divisible by `num/2` or any larger number. This means we can check fewer numbers:

```rust
pub fn is_prime_half(num: i64) -> bool {
    // Check for divisors of num
    for i in 2..num / 2 {
        if num % i == 0 {
            // Any divisor other than 1 or num means num is not prime
            return false;
        }
    }
    // No other divisors found means num is prime
    return true;
}

```

This code takes half as long to run. On my computer, it only takes `3.1` microseconds to verify that `1,789` is prime. Unfortunately, it takes `31.1` microseconds to verify that `17,903` is prime, which means that the time complexity of our algorithm did not change!

This is because our largest factor of `num` was the same in the time complexity of our new algorithm. We need to check `num/2 - 1` values, which means that our algorithm is still `O(n)`.

### Algorithm 3 - Check all Possible Divisor Pairs

Let's try a third algorithm and see if we can get a smaller time complexity.

For this algorithm, we will improve upon our second algorithm. In algorithm 2, we use the fact that if `2` is not a divisor of our number, `num`, then `num/2` can't be a divisor either.

But this is not a special trick we can only do with `2`. If `3` is not a divisor of our number, then `num/3` also can't be a divisor. If `4` is not a divisor of our number, then `num/4` can't be a divisor either. 

The biggest number we need to check is `√num`, because `√num * √num = num.`

```rust
pub fn is_prime_sqrt(num: i64) -> bool {
    // Check for divisors of num
    for i in 2..=(num as f64).sqrt() as i64 {
        if num % i == 0 {
            // Any divisor other than 1 or num means num is not prime
            return false;
        }
    }
    // No other divisors found means num is prime
    return true;
}

```

We are only checking `√num - 1` different numbers, so this means that our time complexity should be `O(√n)`. When I run this on my computer, I see that it takes only `161.9` nanoseconds to check that `1,789` is prime and `555.0` nanoseconds to check that `17,903` is prime. 

This means it took approximately `3.4` times longer to check a number that is `10` times larger, and `√10 ≈ 3.2`. Our complexity analysis accurately estimates how much longer it takes to check bigger prime numbers with this algorithm.

## Summary

Time complexity analysis helps us determine how much more time our algorithm needs to solve a bigger problem. 

We looked at what Big O notation means in time complexity analysis, and we used Big O notation to analyze the time complexity of three primality checking algorithms.

