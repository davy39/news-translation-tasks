---
title: The difference between JavaScript’s call, apply, and bind methods
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T01:31:44.000Z'
originalURL: https://freecodecamp.org/news/the-difference-between-javascripts-call-apply-and-bind-methods-4e69917f77bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2ZGrvPwHxZnbTzABICrEAg.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Rajat Saxena

  Let’s drill it into our minds and be done with it, once and for all.


  JavaScript’s call vs apply vs bind

  I’m writing this micro post because the aforementioned question has haunted me for
  a very long time, and I knew I wasn’t the only...'
---

By Rajat Saxena

#### Let’s drill it into our minds and be done with it, once and for all.

![Image](https://cdn-media-1.freecodecamp.org/images/yOtmD6BiySaust-L9saV-u4p1HeRZUWr8sKx)
_JavaScript’s call vs apply vs bind_

I’m writing this micro post because the aforementioned question has haunted me for a very long time, and I knew I wasn’t the only one. Every single time I saw someone use any of those three methods I had to rush to [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/) in order to figure out what was going on.

Enough was enough. I knew I had to do something and I did. I supposedly have created a proverbial silver bullet which can help new JavaScript developers out.

> **Disclaimer**: This is not a theoretical solution, but a really hacky way to remember the difference.

The major cause of confusion between the `call()` and `apply()` methods is how to pass in the additional arguments besides `this`. And why do we have `bind()` anyway?

So let’s learn how to easily tell the three apart.

#### Apply()

`**apply(this [, [arg1, arg2,...]])**`**:** Calls a function with a provided `this` value. Further arguments are provided as **a single array**.

**_Way to remember_**_: “**A**pply accepts arguments as an **A**rray” or “**AA**”_

#### Call()

`call**(this [, arg1, arg2...])**`**:** Calls a function with a provided `this`. Further arguments are provided as **a comma separated list**

**_Ways to remember:_** _“Call’s arguments are separated by commas” or “**CC**”._

#### Bind()

`**bind(this)**`**:** Returns a new function whose `this` value is bound to the provided value.

**_Ways to remember:_** _bind() is the **only** method out of the three that returns a new function altogether. It does not call the function._

#### Wrap up

I hope the above explanation might help some of you out there. It certainly is helping me.

Do you have other memorization tricks related to programming? Kindly share it with the community as it will help everyone out. Especially during those interviews.

If you have any queries or doubts, hit me up on Twitter [@rajat1saxena](https://twitter.com/rajat1saxena) or write to me at [rajat@raynstudios.com](mailto:rajat@raynstudios.com). Please recommend this post, if you liked it and share it with your network.

