---
title: How Long Should I Make My API Key?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-20T11:04:45.000Z'
originalURL: https://freecodecamp.org/news/how-long-should-i-make-my-api-key-833ebf2dc26f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BbHKX6Db55smgYEUJj-qZg.png
tags:
- name: api
  slug: api
- name: Elixir
  slug: elixir
- name: Erlang
  slug: erlang
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sam Corcos

  Calculating collision probabilities of hashed values


  Say you built an API that generates public keys, and these keys all need to be unique
  and hard to guess. The most common way to do this is to use a hash function to generate
  a random...'
---

By Sam Corcos

#### Calculating collision probabilities of hashed values

![Image](https://cdn-media-1.freecodecamp.org/images/1*BbHKX6Db55smgYEUJj-qZg.png)

Say you built an API that generates public keys, and these keys all need to be unique and hard to guess. The most common way to do this is to use a hash function to generate a random series of numbers and letters. A typical hash looks something like the text below.

> _AFGG2piXh0ht6dmXUxqv4nA1PU120r0yMAQhuc13i8_

A question that often comes up is, “How long does my hash need to be in order to ensure uniqueness?” Most people assume this is a difficult calculation. So they default to some very large number, like a 50-digit hash. The equation to approximate collision probability is actually quite simple.

### How do I calculate?

Let’s assume you’re using a good cryptographic algorithm (i.e. [not JavaScript’s Math.random](https://medium.com/@betable/tifu-by-using-math-random-f1c308c4fd9d#.1ypwox7l4)). Every language has a decent crypto package for generating random hashes. With Phoenix, you can use the Erlang **:crypto** package.

There are only two pieces of information you need to do the calculation:

1. How many possible unique hash values can you create with the given inputs? We’ll assign this to the variable _N._
2. How many values could you possibly need to generate in the lifetime of your project? We’ll assign this to the variable _k._

To calculate the first value, add up all the possible characters that can go into your hash. Raise it to the power of the length of your hash.

So for example, if your hash value contains numbers, lowercase, and uppercase letters, that adds up to 62 total characters (10 + 26 + 26) that we can use. If we are generating a hash of only 3 characters in length, then:

_N_ = 62³ = **238,328** possible values

To calculate the second value, you need to think about what your app does and make some reasonable assumptions.

Let’s say your app is generating a hash to assign to each of your customers. Let’s also say that your app is very niche. The absolute-best case scenario, your app will have 1000 customers over its lifetime. Then, for safety’s sake, we’ll multiply that by 10. We assume that you may need to generate 10,000 values over the course of your app’s life.

_k_ = **10,000** upper bound for possible values that need to be created

So now we need to calculate. There are many algorithms we can use. We’ll use one of the [simple approximations](https://en.wikipedia.org/wiki/Birthday_problem#Approximations), where _e_ is the mathematical constant (the base of the natural log), and _k_ and _N_ are the same values as above.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jET4z0dP--QnXA3AjpvEKA.png)

The base equation gives us the probability that all values are unique. Then we subtract that result from 1 to get the odds that you have a collision. If you don’t feel like writing your own equation, I’ve provided one below written in JavaScript.

So in the example above, **calculate(N, k)** yields a probability of **approximately 100%** that you will have a collision. So for that use case, you should use a hash of more than 3 characters in length.

Now, if we were to take that same example but change the length of our hash from 3 to 5, we would get an _N_ that is _much_ larger (exponentials are good like that).

_N_ = 62⁵ = ~**900,000,000**

Assuming the same value _k_, our new probability of a collision is down to only **5.4%**. What if we bumped that from 5 characters to 10?

_N_ = 62¹⁰ = **~800,000,000,000,000,000**

Yes, that’s ~800 quintillion unique hashes. Which bring your odds of a collision down to 0.000000000062%. This is about a **1-in-50-billion chance** that you have a conflict. And that’s with a hash of 10 digits — something like: BwQ1W6soXk.

For another example, let’s say you’re a data processing company that deals with lots of transactions. We’ll say you deal with 1 million processes per second and you need to generate a hash for each of them. Let’s also say that you think this company could run for the next 100 years.

_k = ~_3,000,000,000,000,000

That comes out to about **3 quadrillion** hashes that you need made that all need to be unique. That’s a lot of data! But even with this extremely large number to work with, you only need a **21-digit** hash to ensure a **1-in-10-million chance** of collision over the lifetime of the project.

So the next time you’re worried about the length of your hash in ensuring uniqueness, know that you don’t need one as long as you think you do. Plus, you can do the calculation yourself without much effort.

_Sam Corcos is the lead developer and co-founder of [Sightline Maps](http://sightlinemaps.com), the most intuitive platform for 3D printing topographical maps, as well as [LearnPhoenix.io](http://learnphoenix.io), an intermediate-advanced tutorial site for building scalable production apps with Phoenix and React._

