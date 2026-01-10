---
title: Java Random Number Generator – How to Generate Numbers with Math.random() and
  Convert to Integers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-19T15:09:37.000Z'
originalURL: https://freecodecamp.org/news/java-random-number-generator-how-to-generate-with-math-random-and-convert-to-integer
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/java-number-generators.png
tags:
- name: Java
  slug: java
- name: Math
  slug: math
seo_title: null
seo_desc: "By Sebastian Sigl\nIn many applications, you need random numbers. You might\
  \ need to throw dice in video games, create a private cryptography key, or create\
  \ a user’s temporary password. \nAll these applications depend on random number\
  \ creation. It’s som..."
---

By Sebastian Sigl

In many applications, you need random numbers. You might need to throw dice in video games, create a private cryptography key, or create a user’s temporary password. 

All these applications depend on random number creation. It’s sometimes challenging to differentiate what to use when, and security is a deep topic. Without spending a few years digging into it, it’s hard to quickly understand the documentation about available implementations and pick the proper way for your use case. 

So in this tutorial, I'll summarize the prominent use cases and how to choose the best-performing implementation based on your your Java code.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/brainstorming---Frame-1--1-.jpg)

In this article, you will learn:

* How to generate integers, floats, and booleans,
* How generate random numbers for performance-critical use cases,
* How generate random numbers for security-critical use cases,
* How numbers generators work,
* The differences between pseudo random number generators and true random number generators,
* How to use a seed to your advantage.  


All the code examples are minimal, and you can find the complete [source code on GitHub](https://github.com/sesigl/random-number-generators-java).

## Constraints of Math.random()

`Math.random` did exist even before Java 6. It's easy to access and still widely used. With Java 17, a new common interface called `RandomGenerator` is available, which consolidates all random generator implementations in the current Java SDK. 

`Math.random()` nowadays simply delegates to `Random().nextFloat()`. But, it only returns a `double`. So it doesn't allow you to request different types of numbers or generate numbers between ranges. It also doesn't allow you to select from different implementations. 

In the following sections, you will learn about a more flexible number generation and learn how to generate numbers optimized for efficiency or security.

## Common Interface Since Java 17

With Java 17, a common interface is implemented by the available number generators in the Java SDK. You have methods available for all essential data types, and you can define the expected range you would like to generate numbers for:

```java
RandomGenerator randomGenerator = new Random();

// generate int between 0 - 9
randomGenerator.nextInt(10);

// generate int between 1 - 9
randomGenerator.nextInt(1, 9);

// generate long between 1 - 9
randomGenerator.nextLong(1, 9);

// generate float between 1 - 9
randomGenerator.nextFloat(1, 9);

// generate double between 1 - 9
randomGenerator.nextDouble(1, 9);

// generate random boolean
randomGenerator.nextBoolean();
```

## Performance Optimized Random Number Generation in a Single-Threaded Environment

For many non-security-relevant cases, you do not care how predictable your random number is. Usually, you just want to have a reliable distribution. 

More performant implementations than `Random` are available if your application is single-threaded. One very efficient alternative is called `SplittableRandom`:

```java
new SplittableRandom().nextInt();
```

The [benchmark executed on a MacBook Pro comparing SplittableRandom and Random](https://github.com/sesigl/random-number-generators-java/blob/main/src/test/java/org/example/BenchmarkSingleThreadedTest.java) shows the following results:

```sh
SingleThreaded.Random  116528253,100 ops/s
SingleThreaded.SplittableRandom  619630768,299  ops/s
```

`SplittableRandom` performs about 5 times faster than `Random` in a single-threaded environment. 

Additional advantages to `Random()` are deterministic behavior and splittable fork/join implementation. Summing up, you should prefer using `SplittableRandom` over `Random` in single-threaded environments.

## Performance Optimized Random Number Generation in a Multi-Threaded Environment

High throughput applications leverage multiple threads. So you want to use a number generator which is made for parallel usage. 

The implementation of `Random` is thread-safe but is relatively slow and slows down even more because of locks. Because `SplittableRandom` is not thread-safe, it’s not an alternative here. 

But, you gain better performance by using `ThreadLocalRandom` in a multi-threaded environment. It uses `SplittableRandom`, but ensures performant and secure usage in multiple threads:

```java
ThreadLocalRandom.current().nextInt();
```

The [benchmark executed on a MacBook Pro comparing ThreadLocalRandom and Random](https://github.com/sesigl/random-number-generators-java/blob/main/src/test/java/org/example/BenchmarkMultiThreadedTest.java) generating numbers in parallel using 10 threads shows the following results:

```sh
MultiThreaded   Random                      8308724,791         ops/s
MultiThreaded   ThreadLocalRandom  3537955530,922   ops/s
```

As you can see, using `ThreadLocalRandom` is 425 times faster. `ThreadLocalRandom` is lock-free and, therefore, more performant than the thread-safe `Random` class.

## Security Optimized Random Number Generation

The methods we just discussed are speedy and sufficient for most of your applications. But, they are creating so-called pseudo-random-generated numbers.

Instead of always creating a truly random number, they predict a new number based on the previously predicted number, which comes with a state and a severe problem of predictability. 

Maybe you want to create long-living secrets for encryption, and you don't want others, by any chance, to be able to predict the next generated token. 

In Java, you have `SecureRandom` for more security-relevant use cases:

```java
SecureRandom.getInstanceStrong().nextInt();
```

`SecureRandom.getInstanceStrong()` gives you a provider, which creates secure tokens. In many Linux systems, you use `/dev/random`, generating numbers based on the random noise of real devices. 

But, if you don't have enough random data being collected, so-called missing [entropy](https://en.wikipedia.org/wiki/Entropy), the execution can block and take an unexpectedly long time. Especially in machines with a lot of Docker containers, this can lead to a slow execution in practice.

As an alternative, `new SecureRandom()` does not block by default in case no entropy is available. It also uses a less secure way of number generation as a fallback.

## How to Use Seeds to Your Advantage

By default, a pseudo number generator uses a random seed, which reflects the start values used to generate values. So a seed is quite handy for testing, as it gives you control over predictions and allows you to reset how numbers are created. 

Until now, we haven't talked about anything related to seeds.

```java
@Test
   public void splittableRandomWithSeedIsDeterministic() {
   assertEquals(new SplittableRandom(9999).nextInt(), -788346102);
}

@Test
   public void randomWithSeedIsDeterministic() {
   assertEquals(new Random(9999).nextInt(), -509091100);
}
```

This makes testing a lot easier. Otherwise, you would need to always [mock dependencies](https://site.mockito.org/). 

## Why Number Generation is Hard

Understanding why number generation is hard to get a sense of security is essential. 

Engineers write code, which is eventually compiled into machine-readable code executed in a real processing unit (CPU). A CPU is built upon electronic circuits, which consist of logic gates. 

Long story short, there is no real randomness you can create with a traditional computer because output requires some input and, by definition, that can not be random. 

This means that you need some kind of true random input from the real world, like [Thermal noise](https://en.wikipedia.org/wiki/Johnson-Nyquist_noise) from a [resistor](https://en.wikipedia.org/wiki/Resistor). There are expensive [hardware number generators](https://en.wikipedia.org/wiki/Hardware_random_number_generator) that use real-world physics to give you a lot of capacity for random number creation.

## Risks of Unsafe Random Number Generation

Although many protocols are secure by design, they are not if an attacker can predict encryption keys. 

Nowadays, a lot of applications require true random number generation behind the scenes. Otherwise, attackers might be able to predict generated numbers and, by doing so, infiltrate applications. 

For example, security-related processing breakthroughs based on [quantum computing](https://en.wikipedia.org/wiki/Quantum_computing#Cryptography) can be a real threat if suddenly attackers can solve encryptions in no time.

## Summary

In this blog post, you learned how to generate numbers in Java efficiently. You also learned how to optimize towards performance or security, and you learned what a seed is and how it can be used. 

Also, you should now understand the key differences between pseudo and truely random generated numbers, and you should be able to describe why secure random number generation is important.

I hope you enjoyed the article.

If you liked it and felt the need to give me a round of applause or just want to get in touch, [follow me on Twitter](https://twitter.com/sesigl).

By the way, [we are hiring](https://www.ebay-kleinanzeigen.de/careers)!

### References

* [https://betterprogramming.pub/generating-random-numbers-is-a-lot-harder-than-you-think-b121c3e75d08](https://betterprogramming.pub/generating-random-numbers-is-a-lot-harder-than-you-think-b121c3e75d08)
* [https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html)
* [https://www.happycoders.eu/java/random-number/](https://www.happycoders.eu/java/random-number/)
* [https://www.baeldung.com/java-17-random-number-generators](https://www.baeldung.com/java-17-random-number-generators)
* [https://programmer.ink/think/61db978dde30a.html](https://programmer.ink/think/61db978dde30a.html)
* [https://www.baeldung.com/java-secure-random](https://www.baeldung.com/java-secure-random)
* [https://tersesystems.com/blog/2015/12/17/the-right-way-to-use-securerandom/](https://tersesystems.com/blog/2015/12/17/the-right-way-to-use-securerandom/)
* [https://en.wikipedia.org/wiki//dev/random](https://en.wikipedia.org/wiki//dev/random)
* [https://www.schutzwerk.com/en/43/posts/attacking_a_random_number_generator/](https://www.schutzwerk.com/en/43/posts/attacking_a_random_number_generator/)
* [https://en.wikipedia.org/wiki/Random_number_generator_attack](https://en.wikipedia.org/wiki/Random_number_generator_attack)

