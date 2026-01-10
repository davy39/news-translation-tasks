---
title: Why you should experiment with type-checking in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T20:43:27.000Z'
originalURL: https://freecodecamp.org/news/the-incredible-hulk-ython-making-python-strong-ly-typed-adc1b6ccf686
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Awcmdb1xwSKXM7aID2TP1A.png
tags:
- name: coding
  slug: coding
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Periklis Gkolias

  Python is a wonderful dynamically typed language. But quite a few people consider
  this its biggest disadvantage.

  But why?

  Dynamically typed languages remove the headache of writing “mundane” type declarations.
  This makes writing m...'
---

By Periklis Gkolias

Python is a wonderful [dynamically typed](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages) language. But quite a few people consider this its biggest disadvantage.

### But why?

Dynamically typed languages remove the headache of writing “mundane” type declarations. This makes writing more pleasant and a little bit faster. The runtime environment of the language handles the dynamically typed language.

This means that some bugs that could have been eliminated almost immediately after they are introduced, will now remain silent until the code is invoked. And you know when this is going to happen, right?

![Image](https://cdn-media-1.freecodecamp.org/images/UaDW4hJ1lDelQm2C0Qish4GrS1fhZPaZ2LWd)

### Dealing with types

Python has added, as of version 3.5, **optional** support for type hints through the [typing](https://docs.python.org/3/library/typing.html) module.

It looks like they care to compromise for both sides. From the one side, the people who love the liberty of dynamic typing can continue ignoring the type hints. From the other side, the people who love the safety of static typing can benefit from utilizing the new functionality.

### How to use it

The way to use it, or at least to start using it, is quite simple and straightforward. It looks a lot like the TypeScript [way](https://www.typescriptlang.org/docs/handbook/basic-types.html) of static typing in case you are familiar. Here is an example:

```py
# Typing is the core module that supports type checking.
# In here we import List, which provided equivalent functionality to
# the list() function or the [] equivalent shorthand
from typing import List
# We define a function, as usually but we add the expected
# type to the args and we add a return type too
def find_files_of_type(type: str, files_types: List[str]) -> bool:
return (type in files_types)
files_types: List[str] = [‘ppt’, ‘vcf’, ‘png’]
type_to_search: str = ‘ppt’
print(‘Found files of type {} in list? {}’.format(type_to_search,
find_files_of_type(type_to_search, files_types)))
```

A bit awkward, but still clear, right? :)

### The potential trap

You might have noticed that I mentioned the word ‘optional’ a few lines above. So, at the time of writing this article, there is no enforcement on the type checking.

You might add whatever irrelevant type you want to your variables. Do the most invalid, irrelevant and “perverted” operations to them, but Python won’t bat an eye.

If you want to **enforce** the type checking, you should use a type checker like the great [mypy](http://mypy-lang.org/examples.html).

Of course, most IDEs have some functionality towards type checking. [Here](https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html) is the relevant documentation for Pycharm.

### Thinks I would like to see in the future

* Integrate a type-checking mechanism in the core of the language
* As a result of the above, more seamless type hints. For example, if the type-checking is on then, I should not have to use the class `List` or `Tuple` to do it. The `[]` and `()` shorthands should be enough

### Conclusion

Thank you for reading this article. This is by no means an extended guide to this great functionality of Python. Rather it is a primer that I hope will lead to more research.

If you are starting a new project in Python 3.5+, I would recommend experimenting with the type checking. I would love to see your suggestions and thoughts about this feature, so feel free to leave a comment.

Originally published on [my blog](http://perigk.github.io).

