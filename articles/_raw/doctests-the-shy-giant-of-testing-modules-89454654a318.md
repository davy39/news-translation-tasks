---
title: Meet doctests, the shy giants of testing modules
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T19:08:25.000Z'
originalURL: https://freecodecamp.org/news/doctests-the-shy-giant-of-testing-modules-89454654a318
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eMH1zFW_YagZqorGErpcVg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Periklis Gkolias

  Do you use Python, even to wash your clothes? And do you find unit testing boring,
  but still have to do it, because you find value in automated testing? Then this
  article is for you.

  The idea

  If you are a Python fan, then I believ...'
---

By Periklis Gkolias

Do you use Python, even to wash your clothes? And do you find unit testing boring, but still have to do it, because you find value in automated testing? Then this article is for you.

### The idea

If you are a Python fan, then I believe you have used the Python console from time to time. Let’s assume you are writing a few inline functions like below, to experiment with stuff:

```
$ python
Python 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def addme(a):
...     return a + a
... 
>>> addme(2)
4
>>> addme(1.9)
3.8
>>> addme(0)
0
>>>
```

So, you have written an inline function, and you have made a couple test runs on it to do some basic verifications. What if Python could read the above output and do the reasoning for you, at runtime? That’s the idea behind doctests, my friend.

### Seriously?

![Image](https://cdn-media-1.freecodecamp.org/images/V3es93rVCDb3SSQnkAYWHMY1T8zo38gaupW4)
_Calm down Patrick_

Yes, totally! Python has introduced a lot of intuitive and…heartbreaking features from time to time, which are now mainstream within a few main languages. Why shouldn’t this one be, too?

### Benefits of doctests

The benefits of doctests are quite a few.

First of all, they are ridiculously easy to write. I mean, you could even outsource it to your younger cousin, who studies the anatomy of soil atoms (and not programming), because he owes you for fixing his computer.

Second, unless you find copy paste difficult, they are more joyful to write. This time you have to be familiar with the terminal environment, though.

Third, there is no need to open another file (even though you can put all doctests for your app to a single file) to read the test code for any function, as they lie right under the signature of each function.

And finally, they are executable with the doctest module and readable without knowing a bit of Python.

### What about unit tests?

Unit tests still offer great value and advanced capabilities of testing. While doctests are great for validating simple and pure functions, they are not very helpful when you have to do complex validation (or example, if a sequence of commands was called during the test).

### What about mocking?

Doctests can handle mocking gracefully with a great library called [Minimock](https://pypi.org/project/MiniMock/). I encourage you to give it a try and let me know your thoughts.

Even though I like the initiative, I prefer my tests to have separate roles. I don’t want my doctests to be heavily loaded and one-size-fits-all. But that’s really a matter of taste — and there is nothing wrong if you disagree. I am more than happy to hear your rationale, if so.

### A working example

Talk is cheap, so let’s write some code. Below is a working example using the function of the prompt above.

```py
addme(a):
    """
    This is a docstring, usually to explain the use of a function. Please do not confuse it with doctests. They both mean to provide forms of documentation, but doctests are executable too.
    >>> addme(4)
    8
    >>> addme('a')
    'aa'
    >>> addme(set())
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'set' and 'set'
    """
    return a + a

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(addme(1))
```

There are a couple of points worth noticing here:

* The doctests need to live inside a docstring. In there, just ‘copy-paste’ the output of your Python console’s quick tests.
* If you need to simulate an exception case, you only need to add the first and the last lines of the exception message. Did you expect to hardcode paths or do any weird logic to get the file’s full path and print it in full? C’mon, Python wont do that :)
* You need the doctest library to run the tests. Nose doesn’t need it though.
* You can run the above, as usual, with `python mydoctests.py`

### I need my tests to run as part of CI/CD/CT cycle. What’s in for me?

I am not here to disappoint you, am I ? :)

The [nose](http://nose.readthedocs.io/en/latest/) test runner supports running all your doctests in addition to your unit tests. Just add the flag `--with-doctest` and you are good to go.

### Nice stuff, where do I go from here?

* Read the Python [documentation](https://docs.python.org/3.6/library/doctest.html) for more twitches and cases.
* Read this fantastic [book](https://amzn.to/2sjvKoP) and especially chapter 4, which covers doctests.
* Check implementations of other languages. For example, the one for [NodeJS](https://github.com/davidchambers/doctest)
* [Doctests and nose](http://nose.readthedocs.io/en/latest/plugins/doctests.html)

Thank you for reading this article, I hope you enjoyed it and that the article triggered your interest in writing more (and less painful) tests. Please spread the love with the buttons below if so. Feel free to add your own thoughts and experiences with doctests too.

Originally published on [my blog](https://perigk.github.io).

