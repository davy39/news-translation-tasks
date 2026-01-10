---
title: My favourite line of code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T21:33:49.000Z'
originalURL: https://freecodecamp.org/news/my-favourite-line-of-code-53627668aab4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CbW_xpWGV31N6TZM4zZH2w.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sam Williams

  Every developer has their favourite patterns, functions or bits of code. This is
  mine and I use it every day.

  What is it?

  This little function takes a promise and returns an array of the error and the result
  of the promise. It’s super...'
---

By Sam Williams

Every developer has their favourite patterns, functions or bits of code. This is mine and I use it every day.

### What is it?

This little function takes a promise and returns an array of the error and the result of the promise. It’s super simple but can be used for some amazing things.

### What can it do?

#### Clean error handling with async / await

This is the main reason that I use this method every day. At work, we are trying to write all code using `async` / `await` syntax for future readability and maintainability. The problem is that awaiting a promise doesn’t tell you if the promise has succeeded or failed.

```js
let unimportantPromiseTask = () => {
    Math.random() > 0.5 ? 
        Promise.reject('random fail') : 
        Promise.resolve('random pass');
};

let data = await unimportantPromiseTask();
```

If this promise passes then `data = ‘random pass'`, but if it fails then there is an unhandled promise rejection and data is never assigned a value. This may not be what you would expect to happen when reading through the code.

Passing the promise to this `handle` function returns a very explicit result which anyone can easily understand when reading it.

```js
let [err, res] = await handle(unimportantPromiseTask());
```

You can then do what you want with the error and result. Here is a common pattern that we often use next:

```js
if (err 
 (res && !res.data)) { 
    // error handling
    return {err: 'there was an error’}
}
// continue with successful response
```

The main reason we use this instead of wrapping the awaited promise in a `try / catch` block is that we find it easier to read.

#### Stop unhandled promise rejections

This function can be used to handle promises (hence the name). Because the function chains `.catch` onto the promise, if it fails the error is caught. This means if there is a promise that you call and don’t care whether it passes or fails, just pass it into `handle`!

```js
unimportantPromiseTask(); // 50% chance of erroring
handle(unimportantPromiseTask()); // never errors
```

Without passing the promise into the `handle` function, there is going to be a chance that it fails. This is increasingly important as future versions of Node are going to terminate the process when an _unhandled promise rejection_ is encountered.

The other ways to handle promise rejections are to wrap the function in a try catch, or just to chain a `.catch` onto the promise. Whilst these are both very valid, using `handle` where we can makes our code more consistent.

Thanks for reading this quick post on my favourite line of code. If you’ve got a favourite line of code, let me know in the comments what it is and why!

