---
title: A simple introduction to Test Driven Development with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-18T22:36:57.000Z'
originalURL: https://freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ak94Xh5LGvl2TgtnXPQQhQ.jpeg
tags:
- name: coding
  slug: coding
- name: Python
  slug: python
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Dmitry Rastorguev

  I am a self-taught beginning developer who is able to write simple apps. But I have
  a confession to make. It’s impossible to remember how everything is interconnected
  in my head.

  This situation is made worse if I come back to the...'
---

By Dmitry Rastorguev

I am a self-taught beginning developer who is able to write simple apps. But I have a confession to make. It’s impossible to remember how everything is interconnected in my head.

This situation is made worse if I come back to the code I’ve written after a few days. Turns out that this problem could be overcome by following a [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) methodology.

### What is TDD and why is it important?

In layman’s terms, TDD recommends writing tests that would check the functionality of your code prior to your writing the actual code. Only when you are happy with your tests and the features it tests, do you begin to write the actual code in order to satisfy the conditions imposed by the test that would allow them to pass.

Following this process ensures that you careful plan the code you write in order to pass these tests. This also prevents the possibility of writing tests being postponed to a later date, as they might not be deemed as necessary compared to additional features that could be created during that time.

Tests also give you confidence when you begin to refactor code, as you are more likely to catch bugs due to the instant feedback when tests are executed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZGakHQbCUMAyDinf-KBiw.png)
_General workflow of TDD_

### How to get started?

To begin writing tests in Python we will use the `unittest` [module](https://docs.python.org/2/library/unittest.html) that comes with Python. To do this we create a new file `mytests.py`, which will contain all our tests.

Let’s begin with the usual “hello world”:

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
```

Notice that we are importing `helloworld()` function from `mycode` file. In the file `mycode.py` we will initially just include the code below, which creates the function but doesn’t return anything at this stage:

```py
def hello_world():
    pass
```

Running `python mytests.py` will generate the following output in the command line:

```
F

====================================================================

FAIL: test_hello (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 7, in test_hello

self.assertEqual(hello_world(), 'hello world')

AssertionError: None != 'hello world'

--------------------------------------------------------------------

Ran 1 test in 0.000s

FAILED (failures=1)
```

This clearly indicates that the test failed, which was expected. Fortunately, we have already written the tests, so we know that it will always be there to check this function, which gives us confidence in spotting potential bugs in the future.

To ensure the code passes, lets change `mycode.py` to the following:

```py
def hello_world():
    return 'hello world'
```

Running `python mytests.py` again we get the following output in the command line:

```
.

--------------------------------------------------------------------

Ran 1 test in 0.000s

OK
```

Congrats! You’ve have just written your first test. Let’s now move on to a slightly more difficult challenge. We’ll create a function that would allow us to create a custom numeric [list comprehension](https://docs.python.org/2/tutorial/datastructures.html) in Python.

Let’s begin by writing a test for a function that would create a list of specific length.

In the file `mytests.py` this would be a method `test_custom_num_list`:

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
    
    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)
```

This would test that the function `create_num_list` returns a list of length 10. Let’s create function `create_num_list` in `mycode.py`:

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    pass
```

Running `python mytests.py` will generate the following output in the command line:

```
E.

====================================================================

ERROR: test_custom_num_list (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 14, in test_custom_num_list

self.assertEqual(len(create_num_list(10)), 10)

TypeError: object of type 'NoneType' has no len()

--------------------------------------------------------------------

Ran 2 tests in 0.000s

FAILED (errors=1)
```

This is as expected, so let’s go ahead and change function `create_num_list` in `mytest.py` in order to pass the test:

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]
```

Executing `python mytests.py` on the command line demonstrates that the second test has also now passed:

```
..

--------------------------------------------------------------------

Ran 2 tests in 0.000s

OK
```

Let’s now create a custom function that would transform each value in the list like this: `const * ( X ) ^ power` . First let’s write the test for this, using method `test_custom_func_` that would take value 3 as X, take it to the power of 3, and multiply by a constant of 2, resulting in the value 54:

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)
```

Let’s create the function `custom_func_x` in the file `mycode.py`:

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    pass
```

As expected, we get a fail:

```
F..

====================================================================

FAIL: test_custom_func_x (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 17, in test_custom_func_x

self.assertEqual(custom_func_x(3,2,3), 54)

AssertionError: None != 54

--------------------------------------------------------------------

Ran 3 tests in 0.000s

FAILED (failures=1)
```

Updating function `custom_func_x` to pass the test, we have the following:

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power
```

Running the tests again we get a pass:

```
...

--------------------------------------------------------------------

Ran 3 tests in 0.000s

OK
```

Finally, let’s create a new function that would incorporate `custom_func_x` function into the list comprehension. As usual, let’s begin by writing the test. Note that just to be certain, we include two different cases:

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)

def test_custom_non_lin_num_list(self):
        self.assertEqual(custom_non_lin_num_list(5,2,3)[2], 16)
        self.assertEqual(custom_non_lin_num_list(5,3,2)[4], 48)
```

Now let’s create the function `custom_non_lin_num_list` in `mycode.py`:

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power

def custom_non_lin_num_list(length, const, power):
    pass
```

As before, we get a fail:

```
.E..

====================================================================

ERROR: test_custom_non_lin_num_list (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 20, in test_custom_non_lin_num_list

self.assertEqual(custom_non_lin_num_list(5,2,3)[2], 16)

TypeError: 'NoneType' object has no attribute '__getitem__'

--------------------------------------------------------------------

Ran 4 tests in 0.000s

FAILED (errors=1)
```

In order to pass the test, let’s update the `mycode.py` file to the following:

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power

def custom_non_lin_num_list(length, const, power):
    return [custom_func_x(x, const, power) for x in range(length)]
```

Running the tests for the final time, we pass all of them!

```
....

--------------------------------------------------------------------

Ran 4 tests in 0.000s

OK
```

Congrats! This concludes this introduction to testing in Python. Make sure you check out the resources below for more information on testing in general.

The code is available here on [GitHub](https://github.com/drastorguev/python_testing).

### Useful resources for further learning!

#### Web resources

Below are links to some of the libraries focusing on testing in Python:

* [**25.3. unittest - Unit testing framework - Python 2.7.14 documentation**](https://docs.python.org/2.7/library/unittest.html)
* [**pytest: helps you write better programs - pytest documentation**](https://docs.pytest.org/en/latest/)
* [**Welcome to Hypothesis! - Hypothesis 3.45.2 documentation**](https://hypothesis.readthedocs.io/en/latest/)
* [**unittest2 1.1.0 : Python Package Index**](https://pypi.python.org/pypi/unittest2)

#### YouTube videos

If you prefer not to read, I recommend watching the following videos on YouTube.

