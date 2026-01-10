---
title: A quick introduction to pipe() and compose() in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-10T02:30:12.000Z'
originalURL: https://freecodecamp.org/news/pipe-and-compose-in-javascript-5b04004ac937
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FKEc-DbmFn54VPLQmCOLRA.jpeg
tags:
- name: composition
  slug: composition
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yazeed Bzadough

  Functional programming’s been quite the eye-opening journey for me. This post, and
  posts like it, are an attempt to share my insights and perspectives as I trek new
  functional programming lands.

  Ramda’s been my go-to FP library bec...'
---

By Yazeed Bzadough

Functional programming’s been quite the eye-opening journey for me. This post, and posts like it, are an attempt to share my insights and perspectives as I trek new functional programming lands.

[Ramda’s](http://ramdajs.com/) been my go-to FP library because of how much easier it makes functional programming in JavaScript. I highly recommend it.

### Pipe

The concept of `pipe` is simple — it combines `n` functions. It’s a pipe flowing left-to-right, calling each function with the output of the last one.

Let’s write a function that returns someone’s `name`.

```js
getName = (person) => person.name;

getName({ name: 'Buckethead' });
// 'Buckethead'
```

Let’s write a function that uppercases strings.

```js
uppercase = (string) => string.toUpperCase();

uppercase('Buckethead');
// 'BUCKETHEAD'
```

So if we wanted to get and capitalize `person`'s name, we could do this:

```js
name = getName({ name: 'Buckethead' });
uppercase(name);

// 'BUCKETHEAD'
```

That’s fine but let’s eliminate that intermediate variable `name`.

```js
uppercase(getName({ name: 'Buckethead' }));
```

Better, but I’m not fond of that nesting. It can get too crowded. What if we want to add a function that gets the first 6 characters of a string?

```js
get6Characters = (string) => string.substring(0, 6);

get6Characters('Buckethead');
// 'Bucket'
```

Resulting in:

```js
get6Characters(uppercase(getName({ name: 'Buckethead' })));

// 'BUCKET';
```

Let’s get really crazy and add a function to reverse strings.

```js
reverse = (string) =>
  string
    .split('')
    .reverse()
    .join('');

reverse('Buckethead');
// 'daehtekcuB'
```

Now we have:

```js
reverse(get6Characters(uppercase(getName({ name: 'Buckethead' }))));
// 'TEKCUB'
```

It can get a bit…much.

### Pipe to the rescue!

Instead of jamming functions within functions or creating a bunch of intermediate variables, let’s `pipe` all the things!

```js
pipe(
  getName,
  uppercase,
  get6Characters,
  reverse
)({ name: 'Buckethead' });
// 'TEKCUB'
```

Pure art. It’s like a todo list!

Let’s step through it.

For demo purposes, I’ll use a `pipe` implementation from one of [Eric Elliott](https://medium.com/@_ericelliott)’s [functional programming articles](https://medium.com/javascript-scene/reduce-composing-software-fe22f0c39a1d).

```js
pipe = (...fns) => (x) => fns.reduce((v, f) => f(v), x);
```

I love this little one-liner.

Using _rest_ parameters, [see my article on that](https://medium.com/@yazeedb/how-do-javascript-rest-parameters-actually-work-227726e16cc8), we can pipe `n` functions. Each function takes the output of the previous one and it’s all _reduced_ ? to a single value.

And you can use it just like we did above.

```js
pipe(
  getName,
  uppercase,
  get6Characters,
  reverse
)({ name: 'Buckethead' });
// 'TEKCUB'
```

I’ll expand `pipe` and add some debugger statements, and we’ll go line by line.

```js
pipe = (...functions) => (value) => {
  debugger;

  return functions.reduce((currentValue, currentFunction) => {
    debugger;

    return currentFunction(currentValue);
  }, value);
};
```

![](https://cdn-media-1.freecodecamp.org/images/1*jqrKgVeO-raAUJjuN-adug.png)

Call `pipe` with our example and let the wonders unfold.

![](https://cdn-media-1.freecodecamp.org/images/1*rqi22p06rTtc2m0k1yHrRw.png)

Check out the local variables. `functions` is an array of the 4 functions, and `value` is `{ name: 'Buckethead' }`.

Since we used _rest_ parameters, `pipe` allows any number of functions to be used. It’ll just loop and call each one.

![](https://cdn-media-1.freecodecamp.org/images/1*UjM5plW8s--8chfQQg3cMg.png)

On the next debugger, we’re inside `reduce`. This is where `currentValue` is passed to `currentFunction` and returned.

We see the result is `'Buckethead'` because `currentFunction` returns the `.name` property of any object. That will be returned in `reduce`, meaning it becomes the new `currentValue` next time. Let’s hit the next debugger and see.

![](https://cdn-media-1.freecodecamp.org/images/1*sEcE5tBFSpCzJZrKz8mmEQ.png)

Now `currentValue` is `‘Buckethead’` because that’s what got returned last time. `currentFunction` is `uppercase`, so `'BUCKETHEAD'` will be the next `currentValue`.

![](https://cdn-media-1.freecodecamp.org/images/1*Va6taGFU8dSyhz1wLVMWMQ.png)

The same idea, pluck `‘BUCKETHEAD’`'s first 6 characters and hand them off to the next function.

![](https://cdn-media-1.freecodecamp.org/images/1*YaI1oxsZW5qZZUC146DYoQ.png)

`reverse(‘.aedi emaS’)`

![](https://cdn-media-1.freecodecamp.org/images/1*moIMQxr82r2Z8IuXwuZfKQ.png)

And you’re done!

### What about compose()?

It’s just `pipe` in the other direction.

So if you wanted the same result as our `pipe` above, you’d do the opposite.

```js
compose(
  reverse,
  get6Characters,
  uppercase,
  getName
)({ name: 'Buckethead' });
```

Notice how `getName` is last in the chain and `reverse` is first?

Here’s a quick implementation of `compose`, again courtesy of the Magical [Eric Elliott](https://medium.com/@_ericelliott), from [the same article](https://medium.com/javascript-scene/reduce-composing-software-fe22f0c39a1d).

```js
compose = (...fns) => (x) => fns.reduceRight((v, f) => f(v), x);
```

I’ll leave expanding this function with `debugger`s as an exercise to you. Play around with it, use it, appreciate it. And most importantly, have fun!


