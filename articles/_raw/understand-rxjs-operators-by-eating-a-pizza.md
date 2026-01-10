---
title: 'How to Understand RxJS Operators by Eating a Pizza: zip, forkJoin, & combineLatest
  Explained with Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T18:44:45.000Z'
originalURL: https://freecodecamp.org/news/understand-rxjs-operators-by-eating-a-pizza
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/download.jpeg
tags:
- name: Reactive Programming
  slug: reactive-programming
- name: RxJS
  slug: rxjs
seo_title: null
seo_desc: 'By Samuel Teboul

  What is RxJS?


  Reactive programming is an asynchronous programming paradigm concerned with data
  streams and the propagation of change - Wikipedia

  RxJS is a library for reactive programming using observables that makes it easier
  to co...'
---

By Samuel Teboul

# What is RxJS?

> _Reactive programming is an asynchronous programming paradigm concerned with data streams and the propagation of change_ - **Wikipedia**

> RxJS is a library for reactive programming using observables that makes it easier to compose asynchronous or callback-based code - **RxJS docs**

The essential concepts in RxJS are

* **An Observable** is a stream of data
* **Observers** can register up to 3 callbacks:

1. _next_ is called 1:M time to push new values to the observer
2. _error_ is called at most 1 time when an error occurred
3. _complete_ is called at most 1 time on completion

* **Subscription** "kicks off" the observable stream

Without subscribing the stream won't start emitting values. This is what we call a **cold** **observable.** 

It's similar to subscribing to a newspaper or magazine... you won't start getting them until you subscribe. Then, it creates a 1 to 1 relationship between the producer (observable) and the consumer (observer).

![Image](https://lh3.googleusercontent.com/_ro6f-oBp5o-e98sRUYOhfC6T_j79UOqNyfzLse5MfSs4WItSaYoHHK6TS7MlN1O5pSZsN98hA6af6L0j_MHh5F7bL8_Vm3fiya9Vw3Xwr4E0DI9IijKqN6VivRX__bkw7ze30EnzjY)

# What are RxJS operators?

Operators are pure functions that enable a functional programming style of dealing with collections with operations. There are two kinds of operators:

* Creation operators
* Pipeable operators: transformation, filtering, rate limiting, flattening

Subjects are a special type of Observable that allows values to be **multicast** to many Observers. While plain Observables are **unicast** (each subscribed Observer owns an independent execution of the Observable), Subjects are multicast. This is what we call a **hot** **observable.**

In this article, I will focus on the `zip`, `combineLatest` and `forkJoin` operators. These are RxJS combination operators, which means that they enable us to join information from multiple observables. Order, time, and structure of emitted values are the primary differences among them.

Let's look at each one individually.

# zip()

* `zip` doesn’t start to emit until each inner observable emits at least one value
* `zip` emits as long as emitted values can be collected from all inner observables
* `zip` emits values as an array

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_oY4pB5RbNeloyauM1tpWmg.png)

Let’s imagine that you are with Mario and Luigi, two of your best friends, at the best Italian restaurant in Rome. Each one of you orders a drink, a pizza, and a dessert. You specify to the waiter to bring the drinks first, then the pizzas, and finally the desserts.

This situation can be represented with 3 different observables, representing the 3 different orders. In this specific situation, the waiter can use the `zip` operator to bring (emit) the different order items by category.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_ve5RtSu2eH7b3pe8lJQ9rg.png)

**❗️❗️❗️Warning❗️❗️❗️**

If you go back to the same Italian restaurant with your girlfriend, but she doesn’t want to eat, this is what will happen:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_8g5NLq3fTBekvu6gvnfJcw.png)

If the `waiter$` uses the `zip` operator, you will only get your drink!

Why?

Because, when the `waiter$` emits the drinks, the `girlfriend$` observable is complete and no more value can be collected from it. Hopefully, the `waiter$` can use another operator for us so we don't break up with our girlfriend ?

# combineLatest()

* `combineLatest` doesn’t start to emit until each inner observable emits at least one value
* When any inner observable emits a value, emit the last emitted value from each

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_TrJG2NP6PgA0HJMj598lpQ.png)

At the exact same restaurant, the smart `waiter$` now decide to use `combineLatest` operator.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_GHNM2srLwN4Wihm7U8bcQg.png)

**❗️❗️❗️Warning❗️❗️❗️**

With `combineLatest`, the **order** of the provided inner observables does matter.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/4.png)

If `you$` is provided first to `waiter$`, it will emit only one value `["Tiramisu", "Sprite"]`. 

This is happening because `combineLatest` doesn’t start to emit until each inner observable emits at least one value. `girlfriend$` starts emitting when the first inner observable emits its last value. Then, `combineLatest` emits the last values collected from both inner observables.

# forkJoin()

* `forkJoin` emits the last emitted value from each inner observables after they **all** complete
* `forkJoin` will never emit if one of the observables doesn’t complete

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_O-Uis5OrgaeUrh6JSgHkTg.png)

When you go to the restaurant and order for a pizza, you don’t want to know all the steps about how the pizza is prepared. If the cheese is added before the tomatoes or the opposite. You just want to get your pizza! This is where `forkJoin` comes into play.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_tB1kiVeQ2kpicnNjFnN_dA.png)

**❗️❗️❗️Warning❗️❗️❗️**

* If one of the inner observables throws an error, all values are lost
* `forkJoin` doesn’t complete

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_zLaN2lzWlASOC3X7f-k3kA.png)

* If you are only concerned when **all** inner observables complete successfully, you can catch the error from the **outside**
* Then, `forkJoin` completes

![Image](https://www.freecodecamp.org/news/content/images/2020/05/2.png)

* If you don’t care that inner observables complete successfully or not, you must catch errors from every single inner observable
* Then, `forkJoin` completes

![Image](https://www.freecodecamp.org/news/content/images/2020/05/3.png)

Personally, when I go to a restaurant with friends, I don’t care if one of them receives a burnt pizza. I just want mine ? so I will ask the `waiter$` to catch the errors from inner observables individually.

# Wrap up

We covered a lot in this article! Good examples are important to better understand RxJS operators and how to choose them wisely. 

For combination operators like `zip`, `combineLatest`, and `forkJoin` the order of inner observables that you provide is also critical, as it can drives you to unexpected behaviours.

There is much more to cover within RxJS and I will do it in further articles.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_RHYpi9BEvKatE0NRsHfnOw.gif)

I hope you enjoyed this article! ?

? You can [follow me on Twitter](https://twitter.com/tSamoss) to get notified about new Angular/RxJS blog posts and cool tips!

