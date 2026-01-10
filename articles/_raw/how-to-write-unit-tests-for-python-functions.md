---
title: How to Write Unit Tests for Python Functions
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2022-10-27T18:53:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-for-python-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-image-unit-tests-python.png
tags:
- name: Python
  slug: python
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'This guide will teach you how to write unit tests for Python functions.
  But why should you consider writing unit tests at all?

  Well, when working on a large project, you''ll often have to update certain modules
  and refactor code as needed. But such ch...'
---

This guide will teach you how to write unit tests for Python functions. But why should you consider writing unit tests at all?

Well, when working on a large project, you'll often have to update certain modules and refactor code as needed. But such changes can have unintended consequences on other modules that use an updated module within them. This can sometimes break existing functionality. 

As a developer, you should test your code to ensure that all modules in the application work as intended. Unit tests let you check if small isolated units of code function correctly and enable you to fix inconsistencies that arise from updates and refactoring.

This guide will help you get started with unit testing in Python. You'll learn how to use Python's built-in `unittest` module to set up and run unit tests and write test cases to test Python functions. You'll also learn how to test functions that raise exceptions.

Let's get started!

## Testing in Python – First Steps

We'll start by defining a [Python function](https://www.freecodecamp.org/news/functions-in-python-a-beginners-guide/) and write unit tests to check if it works as expected. To focus on how to set up unit tests, we'll consider a simple function `is_prime()`, that takes in a number and checks whether or not it is prime.

```python
import math

def is_prime(num):
    '''Check if num is prime or not.'''
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

```

Let’s start a Python REPL, call the function `is_prime()` with arguments, and verify the results.

```python
>>> from prime_number import is_prime
>>> is_prime(3)
True
>>> is_prime(5)
True
>>> is_prime(12)
False
>>> is_prime(8)
False
>>> assert is_prime(7) == True
```

You can also use the `assert` statement to verify that `is_prime()` returns the expected Boolean value, as shown above. If the return value from the function is different than the expected Boolean value, an `AssertionError` is raised.

This type of **manual testing** is _inefficient_ when you want to exhaustively check your function for a much larger list of arguments. You may want to set up automated testing that runs and validates the function’s output against test cases defined in the test suite. 

## How to Use Python's `unittest` Module

Python ships with the `unittest` module that lets you configure automated tests for functions and classes in your application. The generic procedure to set up unit tests in Python is as follows:

```python
# <module-name>.py

import unittest
from <module> import <function_to_test>
# all entries within <> are placeholders

class TestClass(unittest.TestCase):
	def test_<name_1>(self):
		# check function_to_test

	def test_<name_2>(self):
		# check function_to_test
	:
	:
	:

	def test_<name_n>(self):
		# check function_to_test

```

The above code snippet `<module-name>.py` does the following:

* Imports Python’s built-in `unittest` module.
* Imports the Python function to be tested, `<function_to_test>` from the module in which it’s defined, `<module>`.
* Creates a test class (`TestClass`) that inherits from `unittest.TestCase` class.
* Each of the tests that should be run should be defined as methods inside the test class.
* 💡 **Note**: For the `unittest` module to identify these methods as tests and run them, the names of these methods should start with `test_`.
* The `TestCase` class in the `unittest` module provides useful assertion methods to check if the function under test returns the expected values.

The most common assertion methods are listed below, and we’ll use some of them in this tutorial.

|Method| Description|
|-------|-----------|
|`assertEqual(expected_value,actual_value)`|Asserts that `expected_value == actual_value`|
|`assertTrue(result)`|Asserts that `bool(result)` is `True`|
|`assertFalse(result)`|Asserts that `bool(result)` is `False`|
|`assertRaises(exception, function, *args, **kwargs)`|Asserts that `function(*args, **kwargs)` raises the `exception`|

📑 For a complete list of assertion methods, refer to the [unittest docs](https://docs.python.org/3/library/unittest.html).

To run these tests, we should run unittest as the main module, using the following command:

```bash
$ python -m unittest <module-name>.py
```

We can add the `if __name__=='__main__'` conditional to run `unittest` as the main module. 

```python
if __name__=='__main__':
	unittest.main()
```

Adding the above conditional will enable us to run tests by directly running the Python module containing the tests.

```bash
$ python <module-name>.py
```

## How to Define Test Cases for Python Functions

![Image](https://www.freecodecamp.org/news/content/images/2022/10/unittesting-101.png)

  
In this section, we’ll write unit tests for the `is_prime()` function using the syntax we’ve learned.  
  
To test the `is_prime()` function that returns a Boolean, we can use the `assertTrue()` and `assertFalse()` methods. We define four test methods within the `TestPrime` class that inherits from `unittest.TestCase`.

```python
import unittest
# import the is_prime function
from prime_number import is_prime
class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertTrue(is_prime(2))
    def test_five(self):
    	self.assertTrue(is_prime(5))
    def test_nine(self):
    	self.assertFalse(is_prime(9))
    def test_eleven(self):
    	self.assertTrue(is_prime(11))
if __name__=='__main__':
	unittest.main()
```

```bash
$ python test_prime.py
```

In the output below, '.' indicates a successful test.

```
Output
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
```

In the above code, there are four test methods, each checking for a specific input. You can instead define a single test method that asserts if the output is correct, for all four inputs.

```python
import unittest
from prime_number import is_prime
class TestPrime(unittest.TestCase):
	def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
```

Upon running the `test_prime` module, we see that one test has been run successfully. If any of the assert methods throw an `AssertionError`, then the test fails.

```bash
$ python test_prime.py
```

```
Output
.
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK
```

## How to Write Unit Tests to Check for Exceptions

In the previous section, we tested the `is_prime()` function with prime and non-prime numbers as inputs. Specifically, the inputs were all positive integers.

We haven't yet enforced that the arguments in the function call to `is_prime()` should be positive integers. You can use type hinting to enforce types or raise exceptions for invalid inputs.

In testing the `is_prime()` function, we haven't accounted for the following:

* For a floating point argument, the `is_prime()` function would still run and return `True` or `False`, which is incorrect.
* For arguments of other types, say, the string 'five' instead of the number 5, the function throws a **TypeError.**
* If the argument is a negative integer, then the `math.sqrt()` function throws a **ValueError**. The squares of all real numbers (positive, negative, or zero) are always non-negative. So square root is defined only for non-negative numbers. 

Let's verify the above by running some examples in a Python REPL.

```python
>>> from prime_number import is_prime

>>> is_prime('five')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/home/bala/unit-test-1/prime_number.py", line 5, in is_prime
for i in range(2,int(math.sqrt(num))+1):
TypeError: must be real number, not str

>>> is_prime(-10)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/home/bala/unit-test-1/prime_number.py", line 5, in is_prime
for i in range(2,int(math.sqrt(num))+1):
ValueError: math domain error

>>> is_prime(2.5)
True
```

### How to Raise Exceptions for Invalid Inputs

To address the above, we'll validate the value used in the function call for `num` and raise exceptions as needed.

* Check if `num` is an integer. If yes, proceed to the next check. Else, raise a `TypeError` exception.
* Check if `num` is a negative integer. If yes, raise a `ValueError` exception.

Modifying the function definition to validate the input and raise exceptions, we have:

```python
import math
def is_prime(num):
    '''Check if num is prime or not.'''
    # raise TypeError for invalid input type
    if type(num) != int:
        raise TypeError('num is of invalid type')
    # raise ValueError for invalid input value
    if num < 0:
        raise ValueError('Check the value of num; is num a non-negative integer?')
    # for valid input, proceed to check if num is prime
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
        return False
    return True
```

Now that we've modified the function to raise ValueError and TypeError for invalid inputs, the next step is to test if these exceptions are raised.

## How to Use the `assertRaises()` Method to Test Exceptions

![Image](https://www.freecodecamp.org/news/content/images/2022/10/test-exceptions.png)

In the definition of the `TestPrime` class, let’s add methods to check if the exceptions are raised. 

We define `test_typeerror_1()` and `test_typeerror_2()` methods to check if `TypeError` exception is raised and the `test_valueerror()` method to check if `ValueError` exception is raised.

📌 To call the `assertRaises()` method, we can use the following general syntax:

```python
def test_exception(self):
    self.assertRaises(exception-name,function-name,args)
```

We can also use the following syntax using context manager (we’ll use this syntax in this example):

```python
def test_exception(self):
    with self.assertRaises(exception-name):
        function-name(args)
```

Adding the test methods to check for exceptions, we have:

```python
import unittest
from prime_number import is_prime
class TestPrime(unittest.TestCase):
    def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
        	is_prime(6.5)
    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
        	is_prime('five')
    def test_valueerror(self):
        with self.assertRaises(ValueError):
        	is_prime(-4)
            
if __name__=='__main__':
	unittest.main()
```

Let's run the `test_prime` module and observe the output:

```bash
$ python test_prime.py
```

```
Output
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s
OK
```

In the examples we’ve coded thus far, all the tests succeeded. Let’s modify one of the methods, say, `test_typeerror_2()`, to the following:

```python
def test_typeerror_2(self):
    with self.assertRaises(TypeError):
    	is_prime(5)
```

We call the function `is_prime()` with the number 5 as the argument. Here, 5 is a valid input for which the function returns `True`. Therefore, the function does not raise a `TypeError`. When we run the tests again, we’ll see that there’s one failing test.

```bash
$ python test_prime.py
```

```
Output

..F.
======================================================================
FAIL: test_typeerror_2 (__main__.TestPrime)
----------------------------------------------------------------------
Traceback (most recent call last):
File "test_prime.py", line 17, in test_typeerror_2
is_prime(5)
AssertionError: TypeError not raised
----------------------------------------------------------------------
Ran 4 tests in 0.003s
FAILED (failures=1)
```

## Conclusion

Thank you for reading this far! 😄 I hope this tutorial helped you understand the basics of unit testing in Python. 

You've learned to set up tests that check if a function works as expected or raises an exception—all using Python's built-in `unittest` module. 

Keep coding, and see you in the next tutorial!👩🏽‍💻

