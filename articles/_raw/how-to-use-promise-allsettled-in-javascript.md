---
title: How to Use Promise.allSettled() in JavaScript
subtitle: ''
author: Rahul
co_authors: []
series: null
date: '2023-06-27T17:03:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-promise-allsettled-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/andrew-petrov-hopnkQoC0dg-unsplash.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: null
seo_desc: "Have you ever worked with promises in JavaScript and gotten frustrated\
  \ when one rejects and ruins everything? \nYou write some promise-based code, everything\
  \ is chugging along nicely, and then boom – one little promise rejects and the whole\
  \ chain come..."
---

Have you ever worked with promises in JavaScript and gotten frustrated when one rejects and ruins everything? 

You write some promise-based code, everything is chugging along nicely, and then boom – one little promise rejects and the whole chain comes crashing down.

Your code grinds to a halt and you're left wondering why JavaScript couldn't just ignore that one little hiccup and continue on its merry way. Well, friend, do I have good news for you.

Meet `Promise.allSettled()`, your new best friend and the promise you never knew you needed. `Promise.allSettled()` is a game-changer, allowing you to wait for all your promises to settle – either resolve or reject – and then take action based on the results.

No more ruined promise chains or unhandled rejections. Just pure, unadulterated promise bliss. Join me as we dive into this little-known but incredibly useful promise method and see just how much it can simplify your [asynchronous JavaScript](https://www.freecodecamp.org/news/asynchronous-javascript/) code.

## What Is Promise.allSettled()?

So you want to use JavaScript's Promise.allSettled() method, but aren't quite sure how it works or why you'd want to use it? No worries, I've got you covered.

`Promise.allSettled()` waits for all promises you give it to settle, meaning either resolve or reject. It then returns an array of objects with the status and value or reason for each promise. 

This is useful when you have multiple asynchronous tasks that you want to ensure have completed, but don't necessarily care if some fail.

For example, say you have three API calls that return promises, and you want to get all the data back from the successful calls, even if one fails. You could do:

```js
Promise.allSettled([apiCall1(), apiCall2(), apiCall3()]).then((results) => {});

```

This will run all three API calls, and the `.then()` callback will be called once they have all settled. The results array will have three objects: one for each promise, with either a status of 'fulfilled' and the data, or 'rejected' and the error. 

We can filter to just get the successful calls, and proceed using that data.

The key things to remember are:

* `Promise.allSettled()` waits for all input promises to settle and returns their outcomes.
* Settled means either resolved (fulfilled) or rejected.
* It returns an array of objects with status and value/reason for each input promise.
* It allows handling successful promises even when some reject.

## The problem with `Promise.all()` and the solution with `Promise.allSettled()`

`Promise.all()` is great when you want to wait for multiple promises to complete and get an array of all the resolved values. But it has one major downside: if any of the promises reject, the entire `Promise.all()` rejects immediately.

This can be problematic in some cases. For example, say you make requests to three different backend services, and you don't really care if one fails as long as the other two succeed. With `Promise.all()`, a single rejected promise would reject the entire group, and you'd miss the successful responses from the other promises.

Fortunately, there's a simple solution: `Promise.allSettled()`. This works similarly to `Promise.all()` but instead of rejecting immediately if any promise rejects, it waits for all promises to settle (either resolve or reject) and then returns an array of objects with the status and value/reason for each promise.

For example:

```js
Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("2")),
  Promise.resolve(3),
]).then((results) => {
  // results is an array of:
  // {status: "fulfilled", value: 1}
  // {status: "rejected", reason: Error}
  // {status: "fulfilled", value: 3}
});

```

As you can see, even though the second promise rejected, we still get the resolved values from the other promises. This allows you to handle rejections gracefully without missing any successful responses.

`Promise.allSettled()` provides more flexibility in these types of situations. You get the full picture of all your promises, regardless of some rejecting, so you have the opportunity to still make use of any resolved values and handle rejections appropriately.

So next time you need to wait on multiple promises but can't afford to miss any resolved values due to a rejection, be sure to reach for `Promise.allSettled()`! It's a very useful addition to the [Promise API](https://www.freecodecamp.org/news/tag/promises/).

## Common Questions About `Promise.allSettled()`

### Will `Promise.allSettled()` slow down my code?

Not really. `Promise.allSettled()` simply waits for all the promises you pass to it to settle, either by fulfilling or rejecting. It doesn’t do anything else that would impact performance.

### Can I still catch errors with `Promise.allSettled()`?

Yes, you absolutely can! `Promise.allSettled()` will give you the outcome of each promise, whether it was fulfilled or rejected. 

For any rejected promises, you'll get the reason why it rejected, usually an error. You can catch these errors in the `.catch()` handler of the `Promise.allSettled()` call.

### When should I use `Promise.allSettled()` vs `Promise.all()`?

Use `Promise.allSettled()` when you want to run multiple promises in parallel, but don’t want a single rejected promise to cause the entire group to reject. 

For example, if you're fetching data from multiple third-party APIs, a rejected promise from one API shouldn’t stop you from getting data from the other APIs.

Use `Promise.all()` when you want to run promises in parallel but need them all to successfully complete for your code to continue. 

For example, if you need to fetch data from two APIs to display on a page, you’d want both promises to fulfill before rendering the data.

### Can I get the results of the settled promises?

Yes! `Promise.allSettled()` returns an array of objects with the status and value/reason for each promise. For example:

```js
Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("2")),
  Promise.resolve(3),
]).then((results) => {
  console.log(results);
  /*
    [
      { status: "fulfilled", value: 1 },
      { status: "rejected", reason: Error: 2 },
      { status: "fulfilled", value: 3 }
    ]
    */
});

```

You'll get information on all the promises, whether they fulfilled or rejected, so you have the full picture of the parallel operations.

## Conclusion

So there you have it. `Promise.allSettled()` is a handy method you never knew you needed. 

No longer do you have to wrap `Promise.all()` in a try/catch just to handle potential rejections. You can let `Promise.allSettled()` handle all that for you and just focus on the resolved values. Your async code will be cleaner and easier to read.

Thank you for reading. I am [Rahul](https://rahul.biz), 19, and a technical writer. Here is my [proof of work](https://fueler.io/rahoool).

