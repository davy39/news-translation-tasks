---
title: Python Itertools --- chain, isSlice, and izip Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/python-itertools-chain-isslice-and-izip-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d34740569d1a4ca367b.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Itertools is a Python module of functions that return generators, which
  are objects that only function when iterated over.

  chain()

  The chain() function takes several iterators as arguments. It goes through each
  element of each passed iterable, then r...'
---

Itertools is a Python module of functions that return generators, which are objects that only function when iterated over.

## chain()

The `chain()` function takes several iterators as arguments. It goes through each element of each passed iterable, then returns a single iterator with the contents of all passed iterators.

```py
import itertools
list(itertools.chain([1, 2], [3, 4]))

# Output
# [1, 2, 3, 4]
```

## islice()

The `islice()` function returns specific elements from the passed iterator.

It takes the same arguments as the `slice()` operator for lists: start, stop, and step. Start and stop are optional.

```py
import itertools
list(itertools.islice(count(), 5))

# Output
# [0, 1, 2, 3, 4]
```

## izip()

`izip()` returns an iterator that combines the elements of the passed iterators into tuples.

It works similarly to `zip()`, but returns an iterator instead of a list.

```py
import itertools
list(izip([1, 2, 3], ['a', 'b', 'c']))

# Output
# [(1, 'a'),(2, 'b'),(3, 'c')]
```

## More Information:

* [Learn Data Analysis with Python – A Free 4-Hour Course](https://www.freecodecamp.org/news/learn-data-analysis-with-python-course/)
* [Multithreaded Python: slithering through an I/O bottleneck ?](https://www.freecodecamp.org/news/multithreaded-python/)

