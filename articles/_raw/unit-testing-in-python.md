---
title: How to Write Unit Tests in Python – with Example Test Code
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2024-06-10T16:33:04.000Z'
originalURL: https://freecodecamp.org/news/unit-testing-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/WhatsApp-Image-2024-06-10-at-10.46.58-AM.jpeg
tags:
- name: Python
  slug: python
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'Unit testing is a software testing technique in which individual components
  or units of a software application are tested independently from the rest of the
  application.

  In software development, it''s beneficial to break your application into small,
  i...'
---

Unit testing is a software testing technique in which individual components or units of a software application are tested independently from the rest of the application.

In software development, it's beneficial to break your application into small, isolated units. This approach allows you to write independent tests to check all parts of your application, ensuring that they behave as expected. Also, if a test fails, you can easily isolate and troubleshoot the area of the code that has the bug without tampering with the rest of your application.

Python provides built-in support for unit testing through the [unittest](https://docs.python.org/3/library/unittest.html) testing framework. There are also other third-party testing frameworks that you can use for your unit testing, such as [pytest](https://docs.pytest.org/en/7.1.x/contents.html).

This article focuses on how to use the `unittest` framework to write tests for your Python applications and why developers often prefer it.

To get the best out of this article, you should have a basic understanding of the Python programming language.

## Why Do Developers Prefer to Use unittest?

While there are many frameworks for unit testing in the Python ecosystem, many developers still prefer the built-in `unittest` due to its compelling advantages.

First, the `unittest` module is part of Python's standard library. This ensures immediate availability and compatibility across various environments without extra dependencies. The seamless integration with various environments makes it convenient for developers to use `unittest` without installing additional packages.

Second, as a long-standing framework within the Python ecosystem, `unittest` benefits from familiarity and longevity. Many developers are already used to its API and structure, making it a reliable choice for testing.

Third, most integrated development environments (IDEs) such as PyCharm offer built-in support for `unittest`. This improves developer productivity and streamlines the testing process, allowing for easier test management and execution.

Fourth, the framework has comprehensive and well-maintained documentation. This provides detailed guidance and examples, aiding developers in effectively using `unittest` for their testing needs.

Finally, many existing Python projects use `unittest` for testing, ensuring compatibility with legacy codebases. This widespread adoption allows developers to maintain and extend older projects without needing to introduce and adapt to a new testing framework.

## How to Write Unit Tests with unittest

Unit testing with `unittest` involves creating test cases to verify the functionality of individual units of your code. Each test case is defined by subclassing `unittest.TestCase`. This allows you to inherit the several methods provided by the [TestCase](https://docs.python.org/3/library/unittest.html#test-cases) class.

Some of the methods provided by the `TestCase` class are assert methods. These assert methods allow you to check whether the actual result of a function or operation matches the expected result, or whether certain conditions are met. If an assertion fails, the test is marked as failed, and you will receive an error message.

See [Classes and functions](https://docs.python.org/3/library/unittest.html#classes-and-functions) for detailed information about the different methods provided by the `TestCase` class.

Now, let's use two of the assert methods to write tests for a simple calculator program. First, create a new folder (directory), named `unit-testing`. Then, create a file named `calculator.py` within your `unit-testing` folder. Now, copy the following code into your `calculator.py` file:

```python
def add(x, y):
    """add numbers"""
    return x + y

def subtract(x, y):
    """subtract numbers"""
    return x - y

def divide(x, y):
    """divide numbers"""
    return x / y

def multiply(x, y):
    """multiply numbers"""
    return x * y
```

Notice that instead of having your calculator program within a single function, we broke it into four independent functions (units). This is to ensure that each part of the program is independently tested. So if any of the units gives an error during testing, you can easily identify that unit and troubleshoot it without tampering with the other parts of your program.

As earlier mentioned, testing with `unittest` involves creating a subclass of the `unittest.TestCase` class and then defining methods within the subclass to test individual units of your program.

To show how this works, let's write a test for the `add` function in your calculator program. In your `unit-testing` folder, create a new file named `test_calculator.py` and then copy the following code into it:

```python
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
```

In lines one and two of your code, you imported the `unittest` and your `calculator` modules. You then created a `TestCalculator` class, which inherits from the `TestCase` class.

In line five of your code, you defined a `test_add` method within your class. The method just like every instance methods in Python takes `self` as its first argument. Since `self` is a reference of the `TestCalculator` class, it can access the `assertEqual` method provided by the `TestCase` class, which `TestCalculator` inherits from.

The `assertEqual` method checks if two values are equal. It has the following syntax:

```python
self.assertEqual(first, second, msg=None)
```

In the preceding syntax, `first` represents the value you want to test against the `second` value. `msg` is optional and it represents a custom message that you will receive if the assertion fails. If you don't provide a value for `msg`, you will receive a default message.

Now, let's use the explanation of the syntax to explain the use of `assertEqual` in your `test_add` method. In your first assertion, `self.assertEqual(add(1, 2), 3)` checks if the result of `add(1, 2)` is equal to 3. If the function returns 3, the test passes. Otherwise, it fails and outputs a message indicating the mismatch. This explanation is the same for the rest of your assertions.

Also, notice that you tested just representative values in your `test_add` method. This ensures that your test covers a wide range of possible inputs without redundant code. Here is a breakdown of the representative values in your `test_add` method:

* The addition of two positive numbers (`self.assertEqual(calculator.add(1, 2), 3)`).
    
* The addition of a negative number and a positive number (`self.assertEqual(calculator.add(-1, 1), 0)`).
    
* The addition of two negative numbers (`self.assertEqual(calculator.add(-1, -1), -2)`).
    
* The addition of two zeros (`self.assertEqual(calculator.add(0, 0), 0)`).
    

Now, to run your test, navigate to the `unit-testing` directory in your terminal and run the following command:

```bash
python -m unittest test_calculator.py
```

Running the preceding command will give you the following message in your terminal:

```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

The output indicates that you ran a single test and it was successful.

To ensure that your test is working as expected, you go back to your `calculator.py` file and change the addition (`+`) operator in your `add` function to subtraction (`-`), like this:

```python
def add(x, y):
    """add numbers"""
    return x - y
```

Once you've made the changes, running your test again will raise an `AssertionError` showing that your test failed:

```bash
Traceback (most recent call last):
  File ".../test_calculator.py", line 6, in test_add
    self.assertEqual(calculator.add(1, 2), 3)
AssertionError: -1 != 3

----------------------------------------------------------------------
Ran 1 test in 0.000s
```

You may be wondering why you have to include the `unittest` module in your command instead of running `python test_calculator.py`. That's because you are yet to make your `test_calculator.py` file a standalone script. So running `python test_calculator.py` won't give you any output.

To make your `test_calculator.py` executable as a standalone script, you need to add the following to the bottom of your `test_calculator.py` file:

```python
if __name__ == "__main__":
    unittest.main()
```

Also, the `unittest` module requires that you start the name of your test methods with the word `test`, otherwise, your test won't run as expected.

To try this, change the name of your `test_add` method to `add_test` like this:

```python
class TestCalculator(unittest.TestCase):
    def add_test(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
```

Now, if you run the command `python test_calculator.py`, you will get a message similar to this:

```bash
----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```

Notice that the preceding output shows that zero tests ran. Now, change your method's name back to `test_add`. Also, change the operator in the `add` function of your `calculator.py` back to addition (`+`). Now, rerun the test with the command `python test_calculator.py` and compare your output to the preceding output.

It's a common practice for developers to handle invalid input by raising exceptions. So, it's important to write tests that check for these exceptions.

For example, Python will raise a `ZeroDivisionError` if you try to divide any number by zero. You can use the `unittest` module to test for such errors.

Now, modify your `test_calculator.py` file to include a test method for your `divide` function:

```python
import unittest
import calculator

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(-6, 2), -3)
        self.assertEqual(calculator.divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

In the preceding code, your new `test_divide` method tests representative values just like your `test_add` method. But there is new code at the end that uses `assertRaises`. `assertRaises` is another assert method provided by `unittest` to check if your code raises an exception. Here, you used the method to check for `ZeroDivisionError`.

So, if you run the tests now, you will get a message showing two dots (`..`) and indicating that you ran two successful tests:

```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Conclusion

This article has taught you the basics of unit testing in Python using the `unittest` testing framework.

You've learned the importance of independently testing individual units of your application and the reasons `unittest` is still a popular choice among Python developers. Also, you've learned how to write basic test cases for the `add` and `divide` functions in your simple calculator program.

With this knowledge, you can now confidently create tests that ensure your code behaves as expected, making it more robust and maintainable. I encourage you to apply these lessons by writing tests for the remaining `subtract` and `multiply` functions in your calculator program.
