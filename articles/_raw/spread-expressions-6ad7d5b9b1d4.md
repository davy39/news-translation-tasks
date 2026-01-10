---
title: How to simplify your code with the spread operator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T01:49:27.000Z'
originalURL: https://freecodecamp.org/news/spread-expressions-6ad7d5b9b1d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EsKDjaX82lNdGYXSWOst_w.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Matt Granmoe

  Recently, a co-worker who is learning to love JavaScript came to me asking if there
  was a simple way to take a function like this:

  and return bar: parseBar(bar)when bar is passed. But somehow prevent returning bar
  as undefined when ba...'
---

By Matt Granmoe

Recently, a co-worker who is learning to love JavaScript came to me asking if there was a simple way to take a function like this:

and return `bar: parseBar(bar)`when `bar` is passed. But somehow prevent returning `bar` as `undefined` when `bar` is not passed, since some usages of this in the codebase don’t pass it. He was specifically looking for a way to do this that wouldn’t require any refactoring (like changing from an implicit return to a full function body, using if/else, creating a separate function to do filtering of certain values, etc).

After some hacking in the JavaScript console, I realized that the following is possible:

Here’s a condensed example to throw in the console if you want:

This is possible due to two things. First, the fact that, although the spread operator can’t _occur_ anywhere as a token, it can be applied to literally _any data type in the entire language_.

It’s commonly known that `Object`, `Array`, `Set` and similar are iterable. The fact that all _primitive_ types are also valid operands of the spread operator allows us to spread literally _any_ expression since all expressions will evaluate to some value after being executed.

If you don’t believe me, throw the following in the console:

The second thing that helps us is that spreading an “empty” value results in a no-op.

Two quick examples of how this back alley of JavaScript might be used:

* Guard expressions (à la React’s JSX, and also what was used to solve the original problem mentioned in this post): `...(foo && parseFoo(foo))`
* “Default” expressions: `...(someValue || someDefault)`

A more generic way to refer to all these things might be “spread expressions.” However, I’d now like to say “spread expressions” not as a noun but as a suggestion. Go forth with the knowledge that you can spread _all_ the expressions! ?

