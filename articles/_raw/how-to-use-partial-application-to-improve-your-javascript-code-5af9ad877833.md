---
title: How to use partial application to improve your JavaScript code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:44:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-partial-application-to-improve-your-javascript-code-5af9ad877833
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wj-ZuazaL-hq_6keyoVbGA.jpeg
tags:
- name: development
  slug: development
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Rick Henry

  Making use of this functional technique can make your code more elegant


  Functional programming gives us techniques to solve problems in our code. One of
  these, partial application, is a little tricky to understand but it can allow us
  t...'
---

By Rick Henry

#### Making use of this functional technique can make your code more elegant

![Image](https://cdn-media-1.freecodecamp.org/images/YlwtX1HWYUmiNRvHck44VFmc7Ho86aQTIG54)

Functional programming gives us techniques to solve problems in our code. One of these, partial application, is a little tricky to understand but it can allow us to write less of it (sounds interesting, right?).

#### What is it?

Partial application starts with a function. We take this function and create a new one with one or more of its arguments already “set” or _partially applied_. This sounds odd, but it will reduce the number of parameters needed for our functions.

Let’s give some context around when we could use partial application:

```
const list = (lastJoin, ...items) => {  const commaSeparated = items.slice(0,-1).join(", ");  const lastItem = items.pop();  return `${commaSeparated} ${lastJoin} ${lastItem}`;}
```

This little function takes in a single word, `lastJoin`, and an arbitrary number of `items`. Initially, `list` declares a `commaSeparated` variable. This variable stores a comma separated joined array of all the elements except the last. On the next line we store the last item in `items` in a `lastItem` variable. The function then returns using a string template.

The function then returns the `items`, as a string, in list format. For example:

```
list("and", "red", "green", "blue");     // "red, green and blue"list("with", "red", "green", "blue");    // "red, green with blue"list("or", "red", "green", "blue");      // "red, green or blue"
```

Our `list` function allows us to create lists when we want. Each type of list we create, “and”, “with”, “or” is a specialisation of the general `list` function. Wouldn’t it be nice if they could be functions of their own?!

#### How to use partial application

This is where partial application can help. For example, to make a `listAnd` function, we “set” (or _partially apply_) the `lastJoin` argument to be “and”. The result of doing this means we can invoke our partially applied function like this:

```
listAnd("red", "green", "blue");    // "red, green and blue"
```

It doesn’t need to stop there either. We can make many specialised functions by _partially applying_ an argument to our list function:

```
listOr("red", "green", "blue");      // "red, green or blue"listWith("red", "green", "blue");    // "red, green with blue"
```

To do this, we need to create a `partial` utility function:

```
const partial = (fn, firstArg) => {  return (...lastArgs) => {    return fn(firstArg, ...lastArgs);  }}
```

This function takes a function `fn` as it’s first parameter and `firstArg` as its second. It returns a brand new function with one parameter, `lastArgs`. This gathers up the passed in arguments.

Now to make our `listAnd` function we invoke `partial` passing in our `list` function and our last join word:

```
const listAnd = partial(list, "and");
```

Our `listAnd` function now only takes an arbitrary list of items. This function when invoked will, in turn, invoke the passed in `list` function. We can see that it will be passed “and” as the first argument and the gathered `lastArgs` thereafter.

We’ve now created a partially applied function. We can use this specialised function over and over again in our program:

```
listAnd("red", "green", "blue");    // "red, green and blue"
```

#### **Taking it further**

The `partial` function we created is to illustrate how partial application works. There are some great functional JavaScript libraries available which have this utility built in, such as [Ramda JS](https://ramdajs.com/docs/#partial).

It’s worth noting that even if you are new to partial application as a concept there is every chance you have been using it. If you have ever used the `.bind()` method on a function this is an example of partial application. It’s common practice to pass `this` into bind to set its context. Under the hood it’s partially applying `this` and returning a new function.

