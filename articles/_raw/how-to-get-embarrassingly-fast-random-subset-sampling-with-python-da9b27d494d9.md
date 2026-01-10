---
title: How to get embarrassingly fast random subset sampling with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-11T09:48:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-embarrassingly-fast-random-subset-sampling-with-python-da9b27d494d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NZyHwP7xOOY7nNodbLbF3g.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kirill Dubovikov

  Imagine that you are developing a machine learning model to classify articles. You
  have managed to get an unreasonably large text file which contains millions of identifiers
  of similar articles that belong to the same class. You a...'
---

By Kirill Dubovikov

Imagine that you are developing a machine learning model to classify articles. You have managed to get an unreasonably large text file which contains millions of identifiers of similar articles that belong to the same class. You are unsure whether identifiers that are close to each other are independent.

For example, a parser could write identifiers of articles from a single site together. So now you want to get a large number of random samples from an array of several million elements to create a training dataset or count some empirical statistics. This situation can come up in practice more frequently than you think.

Thanks to Binder, you can [**play with the code online**](https://beta.mybinder.org/v2/gh/kdubovikov/fastsampling/master) without installing anything locally. Or you can clone the [Github repository](https://github.com/kdubovikov/fastsampling). Please note that all benchmarks may differ from machine to machine.

Well, what’s the matter? Let’s use [numpy](http://www.numpy.org)!

On Macbook Pro, this code runs for **around 1.4s per loop**. If you want to get 100,000 samples, this will take about a day and a half. Ouch!

#### Getting up to speed ☄️

What happened there? To generate a random sample, numpy.random.choice permutes the array **each time we call it.** When our sample size is only a fraction of the whole array length, we do not need to shuffle the array each time we want to take a sample. Let’s just shuffle it once and take samples from the start of the shuffled array.

When we come to the last element, we must shuffle it again. This optimization also has a very nice side effect: we will have fewer collisions (repeating samples).

Now it is time to code this up:

This time we get 21.1 µs ± 979 ns per loop, which is faster by several orders of magnitude.

#### Even faster? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*JXF21j3Z9zt16aysLEb-Tw.jpeg)

Can we do it even faster? Yes, but we need to go native. [Cython](http://cython.org) translates Python-like code to optimized native C or C++ which can be compiled and used as a friendly and familiar Python module afterwards.

You can play with Cython in Jupyter notebooks by loading the Cython extension with `%load_ext Cython` , and using `%%cython` magic as the first statement within a cell with Cython code.

Almost all Python code is valid Cython code. But to get the most of it, we need to make use of extensions provided by Cython:

* We statically annotate all types for function signatures and variable definition to use native C variables instead of slow Python objects where possible
* We use a `cdef` keyword for functions that do not need to be exported as a Python API. `cdef` calls are much faster.
* We disable negative indexing and array bounds checking with `@cython.wraparound`and `@cython.boundscheck` to get more speed

This minor refactoring is sufficient to get a reasonable speedup (2x on my laptop) compared to the Python version.

I am obliged to say that Cython is much more than an optimized Python-C translator. With this awesome tool you can also:

* Overcome limitations of [GIL](https://www.google.ru/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&cad=rja&uact=8&ved=0ahUKEwjQlqzs6eDWAhXhCJoKHW0mD0cQFghFMAU&url=https%3A%2F%2Fwiki.python.org%2Fmoin%2FGlobalInterpreterLock&usg=AOvVaw20YulOZd6sYn-anu5E4rz4)
* [Parallelize your code](http://cython.readthedocs.io/en/latest/src/userguide/parallelism.html) with high-level OpenMP wrappers (with threads, not processes!)
* Use fast arrays via [memoryviews](http://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html)
* Expose raw memory buffers to Python code via [Buffer Protocol](http://cython.readthedocs.io/en/latest/src/userguide/buffer.html)

#### What about collisions? ?

Sampling collisions occur when we get a repeating element while sampling the array. For simplicity, let’s suppose that the array does not contain duplicates.

We’ll compare the two algorithms in terms of collisions. We can collect a large number of samples from the same array for each of the algorithms, and then count up the total number of collisions.

When we repeat this process several times and record the results, we are actually collecting a random sample of collision counts for both algorithms.

Having those samples at hand, we can apply statistics to compare them. In this case, we will use a t-test (you can read more about t-distribution in my [previous post](https://medium.freecodecamp.org/the-t-distribution-a-key-statistical-concept-discovered-by-a-beer-brewery-dbfdc693184) and more about t-test [here](http://www.statisticshowto.com/probability-and-statistics/t-test/)).

The p-value we get is 0, which means that the result we got is significant.

Let’s make a plot and see the difference:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZquEFfe47SUXzzPBCFx0w.jpeg)

As you can see, we get way lower collision numbers as a bonus.

#### Conclusion

Thanks a lot for reading it to the end! Give me a few claps ? if you found this material helpful — it will help to spread the word.

