---
title: Awesome Python modules you probably aren’t using (but should be)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T15:35:50.000Z'
originalURL: https://freecodecamp.org/news/awesome-python-modules-you-probably-arent-using-but-should-be-ec926da27439
coverImage: https://cdn-media-1.freecodecamp.org/images/0*oG_N_s-TEk-wMau5
tags:
- name: code
  slug: code
- name: development
  slug: development
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Adam Goldschmidt


  Python is a beautiful language, and it contains many built-in modules that aim to
  help us write better, prettier code.

  Objective

  Throughout this article, we will use some lesser-known modules and methods that
  I think can improve ...'
---

By Adam Goldschmidt

![Image](https://cdn-media-1.freecodecamp.org/images/1*_qzk08ccorLRF4zS6EwBBQ.png)

**Python** is a beautiful language, and it contains many built-in modules that aim to help us write better, prettier code.

### Objective

Throughout this article, we will use some lesser-known modules and methods that I think can improve the way we code - both in visibility and in efficiency.

### NamedTuple

I believe that some of you already know the more popular `namedtuple` from the `collections` module (if you don't - [check it out](https://docs.python.org/3.6/library/collections.html#collections.namedtuple)), but since Python 3.6, a new class is available in the `typing` module: `NamedTuple`. Both are designed to help you quickly create readable immutable objects.

`NamedTuple` is actually a typed version of `namedtuple`, and in my opinion, is much more readable:

Here’s the `namedtuple` alternative:

### array.array

> _Efficient arrays of numeric values. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. — [Python docs](https://docs.python.org/3.6/library/array.html)_

When using the `array` module, we need to instantiate it with a typecode, which is the type all of its elements will use. Let's compare time efficiency with a normal list, writing many integers to a file (using `[pickle](https://docs.python.org/3.7/library/pickle.html)` module for a regular list):

![Image](https://cdn-media-1.freecodecamp.org/images/1*vPfWDCLXCikKuJOuWj5Xkg.png)
_[https://gist.github.com/AdamGold/961758c66cdfe92642eabb61d9ce9866](https://gist.github.com/AdamGold/961758c66cdfe92642eabb61d9ce9866" rel="noopener" target="_blank" title=")_

**14 times** faster. That’s a lot. Of course it also depends on the `pickle` module, but still - the array is way more compact than the list. So if you are using simple numeric values, you should consider using the `array` module.

### itertools.combinations

`itertools` is an impressive module. It has so many different time-saving methods, all of them are listed [here](https://docs.python.org/3/library/itertools.html). There's even a GitHub repository containing [more itertools](https://github.com/erikrose/more-itertools)!

I got to use the `combinations` method this week and I thought I'd share it. This method takes an iterable and an integer as arguments, and creates a generator consisting of all possible combinations of the iterable with a maximum length of the integer given, without duplication:

### dict.fromkeys

A quick and beautiful way of creating a dict with default values:

### Last but not least - the `dis` module

> _The `[dis](https://docs.python.org/3/library/dis.html#module-dis)` module supports the analysis of CPython [bytecode](https://docs.python.org/3/glossary.html#term-bytecode) by disassembling it._

As you may or may not know, Python compiles source code to a set of instructions called “bytecode”. The `dis` module helps us handle these instructions, and it's a great debugging tool.

Here’s an example from the [Fluent Python book](http://shop.oreilly.com/product/0636920032519.do):

We got an error — but the operation still succeeded. How come? Well, if we look at the bytecode (I added comments near the important parts):

### Before you go…

Thanks for reading! For more Python related articles and other cool stuff, you can follow me on [Medium](https://medium.com/@adamgoldschmidt) or [GitHub](https://github.com/AdamGold) (I star some awesome repos!).

If you enjoyed this article, please hold down the clap button ? to help others find it. The longer you hold it, the more claps you give!

And do not hesitate to share more Python hidden gems in the comments below.

