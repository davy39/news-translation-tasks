---
title: How to Flatten a Dictionary in Python in 4 Different Ways
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-27T19:59:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-flatten-a-dictionary-in-python-in-4-different-ways
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/convert_nested_dictionary_flat_one_python.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Miguel Brito

  In this post, we’ll look at 4 different ways to flatten a dict in Python. For each
  method I’ll point out the pros and cons, and I''ll give a quick performance analysis.
  For this tutorial, I ran all examples on Python 3.7.

  Why Should Yo...'
---

By Miguel Brito

In this post, we’ll look at 4 different ways to flatten a dict in Python. For each method I’ll point out the **pros and cons**, and I'll give a quick performance analysis. For this tutorial, I ran all examples on Python 3.7.

## Why Should You Know How to Flatten a Dict in Python?

There are many reasons you would need a flattened dictionary. One is that it makes it simpler to [compare two dicts](https://miguendes.me/the-best-way-to-compare-two-dictionaries-in-python). The other is that it’s easier to navigate and manipulate it, since a flat structure is one level deep.

Python is a versatile language, meaning you can achieve the same goals in several ways. Choosing the best solution for a problem requires weighting the benefits of one solution over another. 

The goal of this post is to provide you many options for this problem and give you as much data as possible so you can make an informed decision. So, let’s go.

PS: If you don’t have Python 3.7 you can install it using `pyenv` and even have [multiple versions at the same time](https://miguendes.me/how-i-set-up-my-python-workspace) with no conflict.

## Table of Contents

1. [Using your Own Recursive Function](heading-how-to-flatten-a-dict-in-python-using-your-own-recursive-function)
2. [Using your Own Recursive Function + Generators](heading-how-to-flatten-a-dict-in-python-using-your-own-recursive-function-generators)
3. [Using pandas json_normalize](heading-how-to-flatten-a-dict-in-python-using-pandas-jsonnormalize)
4. [Using the flatdict Library](heading-how-to-flatten-a-dict-in-python-using-the-flatdict-library)
5. [Conclusion](heading-conclusion)

## How to Flatten a Dict in Python Using your Own Recursive Function

A quick look at Google leads us to [stackoverflow](https://stackoverflow.com). The [first answer](https://stackoverflow.com/a/6027615) shows a recursive function that traverses the dictionary and returns a flattened instance. I'm going to draw inspiration on that function and show a slightly improved version.

We can start by type hinting it to improve readability and make it type safe.

```python
from collections.abc import MutableMapping

def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


>>> flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
{'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}

```

### Performance Benchmark

We have quickly verified that the function returns a flat dict, but what about its performance? Is it good for production use? Let's run a quick benchmark to see how fast it is.

For this and all benchmarks in this article, I will use `IPython`'s `timeit` magic function and `memit` from the [`memory_profiler`](https://pypi.org/project/memory-profiler/) library.

PS: For `%memit` to work, you need to run `%load_ext memory_profiler` first.

```python
In [4]: %timeit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
7.28 µs ± 54.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [5]: %load_ext memory_profiler

In [6]: %memit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
peak memory: 84.94 MiB, increment: 0.29 MiB

```

**Pros:** Easy to understand, and it just works.

**Cons:** It stores the items in a list in memory that is then passed to the `dict` constructor. This is wasteful not only in terms of memory but also speed. 

Even though adding elements to a list in Python is fast, doing so repeatedly is not actually needed. In the next section, we'll see how to improve this using generators.

## How to Flatten a Dict in Python Using your Own Recursive Function + Generators

The first version works, and it's somewhat fast. However, it has a problem. 

To create a new dictionary with the flattened keys it maintains in memory a Python `list`. This is inefficient, as we have to keep an entire data structure in memory just to serve as a temporary storage.

A much better solution is to use [Python's generators](https://docs.python.org/3/glossary.html#term-generator) which is an object that can pause execution and remembers the state that can be resumed later. By using a generator, we can get rid of the temporary list with no change in behavior.

```python
from collections.abc import MutableMapping

def _flatten_dict_gen(d, parent_key, sep):
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            yield from flatten_dict(v, new_key, sep=sep).items()
        else:
            yield new_key, v


def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str = '.'):
    return dict(_flatten_dict_gen(d, parent_key, sep))

>>> flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
{'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}

```

### Performance Benchmark

```python
In [9]: %timeit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
7.39 µs ± 78.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [7]: %memit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
peak memory: 45.27 MiB, increment: 0.25 MiB

```

**Pros:** Easy to understand, it works like the previous version, and it's memory efficient. This version consumes about 50% less memory than the version using lists.

**Cons:** It might not handle edge cases very well. For example if we pass a dictionary-like object that is not an instance of `MutableMapping` then this example will fail. But this is a disadvantage of the previous version as well.

## How to Flatten a Dict in Python Using pandas `json_normalize`

The previous solutions work fine, as we can see, but writing our own solution for a common problem like this is reinventing the wheel. As an alternative, we can use popular data manipulation libraries such as [`pandas`](https://pandas.pydata.org).

`pandas` comes with a [generic function to normalize JSON objects](https://pandas.pydata.org/docs/user_guide/io.html?highlight=json_normalize#normalization) which are represented in Python as a dictionary. This is a great opportunity for us to not recreate existing solutions and use a more robust one.

Moreover, the end result looks great in just one line, and we can even hide it behind a thin interface.

```python
from collections.abc import MutableMapping
import pandas as pd

def flatten_dict(d: MutableMapping, sep: str= '.') -> MutableMapping:
    [flat_dict] = pd.json_normalize(d, sep=sep).to_dict(orient='records')
    return flat_dict


>>> flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
{'a': 1, 'd': [6, 7, 8], 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5}

```

### Performance Benchmark

```python
In [5]: %timeit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
779 µs ± 10.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [6]: %memit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
peak memory: 86.30 MiB, increment: 0.90 MiB

```

**Pros:** Easy to understand, and we reuse a well-established library.

**Cons:** Using `pandas` just to flatten a dict seems like overkill. If your project doesn't need it, then we can use a more lightweight library such as `FlatDict`. Besides, according to `timeit` this version is **100x slower** than using our own solution, which is not great.

## How to Flatten a Dict in Python Using the `flatdict` Library

[`flatdict`](https://flatdict.readthedocs.io/en/stable/index.html) is a Python library that creates a single level dict from a nested one and is available from Python 3.5 onwards.

We've seen so far that writing our custom solution may not be ideal, and using a full-blown library like `pandas` just for this purpose is not great either.

As an alternative we can use `flatdict`, which is much more lightweight and battle-tested.

The library is very versatile and also enables us to use custom separators. However, one of the best features it provides is the ability to access the newly created dictionary as before – that is, you can access values using either the new keys or the old ones.

Let's see an example.

```python
>>> import flatdict
>>> d =  flatdict.FlatDict(data, delimiter='.')

# d is a FlatDict instance
>>> d
<FlatDict id=140665244199904 {'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}>"

# and it allows accessing flat keys
>>> d['c.b.y']
4

# but also nested ones
>>> d['c']['b']['y']
4

# and can be converted to a flatten dict
>>> dict(d)
{'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}

```

As you can see, `flatdict` allows great flexibility and convenience.

### Performance Benchmark

```python
In [3]: %timeit flatdict.FlatDict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}, delimiter='.')
8.97 µs ± 21.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [4]: %memit flatdict.FlatDict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}, delimiter='.')
peak memory: 45.21 MiB, increment: 0.14 MiB

```

**Pros:** Easy to understand, and it just works, and it's a lightweight library. Allows accessing nested elements in two different ways. Just as fast and memory efficient as the solution using generators.

**Cons:** It is still an external library, and like many open-source tools, if there's a bug you need to wait for the author to fix it. And sometimes authors abandon their projects, which introduces risk to your project. Regardless, I still think the pros outweigh the cons in this case.

## Conclusion

In this post, we saw 4 different ways of flattening a dictionary in Python. Each solutions comes with pros and cons, and choosing the best one is a matter of personal taste and project constrains.

I hope you liked it and see you next time!

