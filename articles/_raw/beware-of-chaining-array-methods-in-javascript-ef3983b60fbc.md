---
title: Beware of chaining array methods in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/beware-of-chaining-array-methods-in-javascript-ef3983b60fbc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1s3_FsFSnJzT2Byq.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Balaganesh Damodaran

  JavaScript’s Array class exposes quite a few methods (filter, map, reduce), which
  iterate through an array and call an iterator function to perform actions on the
  array. Chaining these methods allows you to write clean, easy t...'
---

By Balaganesh Damodaran

JavaScript’s Array class exposes quite a few methods (filter, map, reduce), which iterate through an array and call an iterator function to perform actions on the array. Chaining these methods allows you to write clean, easy to read code. But what does this convenience cost us in terms of performance, and is it worth it?

![Image](https://cdn-media-1.freecodecamp.org/images/4iKtwVSXgNmeSNOpUi2enoqqLfGHOsV8ezhB)

Javascript is a ‘functional’ language. What this means is that functions are first class objects in Javascript, and as such they can be passed on as parameters to other functions. There are quite a few built-in methods provided by the Javascript standard library, which makes use of this fact to enable us to write clean, understandable, and easy to read code.

#### Built-in Javascript Array Methods, and Chaining

One such built-in class which makes extensive use of Javascript’s functional nature is the `Array` class. `Array`s in Javascript expose a number of instance methods, which:

* accept a function as an argument,
* iterate upon the array,
* and call the function, passing along the array item as a parameter to the function.

The most popular of these are of course `forEach`, `filter`, `map` and `reduce`. Since some of these methods also return the `Array` instance as the return value of the method, they are often chained together like this:

```
const tripExpenses = [{    amount: 12.07,    currency: 'USD',    paid: true}, {    amount: 1.12,    currency: 'USD',    paid: true}, {    amount: 112.00,    currency: 'INR',    paid: false}, {    amount: 54.17,    currency: 'USD',    paid: true}, {    amount: 16.50,    currency: 'USD',    paid: true}, {    amount: 189.50,    currency: 'INR',    paid: false}];
```

```
const totalPaidExpensesInINR = tripExpenses    .filter(expense => expense.paid)    .map(expense => {        if(expense.currency == 'USD')            return expense.amount * 70;        else            return expense.amount;    })    .reduce((amountA, amountB) => amountA + amountB);
```

In this example, we are calculating the total paid expenses after converting them from USD to INR. To do this, we are:

* `filter`ing `tripExpenses` to extract only the paid expenses,
* `map`ping the expense amount from the specified currency and converting it to INR, and
* `reduce`ing the INR amounts to get the sum.

Looks like a common, very typical, valid use-case for chaining array methods right? A lot of developers who’ve been taught to write functional Javascript would come out with something similar when asked to solve this issue.

#### The Problem with Array Method Chaining

Currently, our `tripExpenses` array only has 6 items, so this is relatively fast. But what happens when we have to analyze the trip expenses for, say, an entire company of employees for the entire financial year, and our `tripExpenses` array starts to have hundreds of thousands of elements?

Thanks to JSPerf, we can visualize this cost quite easily. So let’s run a comparison test for the same code with `tripExpenses` having 10 elements, 10,000 elements, and 100,000 elements. Here's the result of the [JSPerf comparison](https://jsperf.com/array-operations-builtin-vs-foreach/1):

![Image](https://cdn-media-1.freecodecamp.org/images/oMRqEBBgNA9IHRWGLEzakbXFEMcL2Gfb2gyv)

The graph shows the number of operations per second, and higher is better. While I expected the 100,000 elements case to perform poorly, I really did not expect the 10,000 elements case to perform this poorly. Since it’s not really visible on the chart, let’s look at the numbers:

* 10 Elements — 6,142,739 ops per second
* 10,000 Elements — 2,199 ops per second
* 100,000 Elements — 223 ops per second

Yikes, that’s really bad! And while processing an array of 100,000 elements might not happen often, 10,000 elements is a very plausible use case that I’ve seen regularly in multiple applications I’ve developed (mostly on the server side).

This shows us that when we write — even what seems to be quite simple code — we really should be watching out for any performance issues that might crop up because of the way we write our code.

If, instead of chaining the `filter`, `map` and `reduce` methods together, we rewrite our code such that all the work gets done inline, in a single loop, we can gain significantly better performance.

```
let totalPaidExpensesInINR = 0;
```

```
for(let expense of tripExpenses){    if(expense.paid){        if(expense.currency == 'USD')            totalPaidExpensesInINR += (expense.amount * 70);        else            totalPaidExpensesInINR += expense.amount;    }}
```

Let’s run another [JSPerf comparison](https://jsperf.com/functional-vs-for-of-array-methods/1) to see how this performs against it’s functional counterpart, in a 10,000 element test:

![Image](https://cdn-media-1.freecodecamp.org/images/qMXDUV7I2B1K8LguRGP6BwmcPSeG59PeuxaL)

As you can see, on Chrome (and by extension Node.JS), the functional example is a whopping 77% slower than the for-of example. On Firefox, the numbers are a lot closer, but the functional example is still 16% slower than the for-of example.

#### Why Such a Large Performance Delta?

So why is the functional example so much slower than the for-of example? Well it’s a combination of factors, but the primary factors that, as a developer, we can control from user land are:

* Looping over the same array elements multiple times.
* Overhead of function calls for each iteration in the functional example.

If you see the for-of example, you’ll see that we only ever iterate through the `tripExpenses` array once. Also, we call no functions from within, instead performing our calculations inline.

One of the big performance ‘wins’ that modern Javascript engines get is by inlining function calls. What this means is that the engine will actually compile your code into a version where the compiler replaces the function call, with the function itself (i.e. inline where you call the function). This eliminates the overhead of calling the function, and provides huge performance gains.

However, we cannot always say for sure whether a Javascript engine will choose to inline a function or not, so doing it ourselves ensures that we have the best possible performance.

### Conclusion

Some developers may consider the for-of example to be less readable, and more difficult to understand than the functional example. For this particular example, I’d say both the styles are equally readable. However, in the case of the functional example, the convenience of the method chaining tends to hide the multiple iterations and function calls from the developer, thus making it easy for an inexperienced developer to write non-performant code.

I’m not saying that you should always avoid the functional way – I’m sure there are plenty of valid cases for using the functional way and for chaining the methods. But a general rule of thumb to remember when it comes to performance and iterating arrays in Javascript is that if you’re chaining methods which iterate through the entire array, you should probably stop and consider the performance impact before going ahead.

I’d love to hear your opinion on what I’ve written in this article. Do chime in with your comments below.

#### [Feb 6th, 2019] Some caveats, and things to keep in mind, as pointed out by commenters

As [pointed out](https://medium.com/@paul.beynon/thanks-for-taking-the-time-to-write-the-article-i-enjoyed-it-db916026647) by [Paul B,](https://www.freecodecamp.org/news/beware-of-chaining-array-methods-in-javascript-ef3983b60fbc/undefined) there are is a performance hit when using `for…of` in a transpiled form in browsers, but you can always use a normal for loop with an iterator variable to get around this. However, like Paul says, there are quite a few advantages to sticking with an iterator function. Do go read [his comment,](https://medium.com/@paul.beynon/thanks-for-taking-the-time-to-write-the-article-i-enjoyed-it-db916026647) it’s worthy of being an article all by itself.

In addition, a lot of folks have also been saying that this would be premature optimization or a micro optimization, and I do partially agree with them. You should in general always optimize for readability and maintainability over performance, right up until the point where poor performance actually starts impacting you. Once you’ve reached that point, then you might want to reconsider your iterators.

_Originally published at [asleepysamurai.com](https://asleepysamurai.com/articles/beware-chaining-array-methods-javascript?ref=medium) on January 8, 2019._

