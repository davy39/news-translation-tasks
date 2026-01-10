---
title: How to Write Unit Tests for Instance Methods in Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2023-01-31T00:13:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-for-instance-methods-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/instance-methods-python.png
tags:
- name: Python
  slug: python
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'This tutorial will teach you how to write unit tests for instance methods
  in Python.

  In a previous tutorial, we covered how to write unit tests for Python functions.
  While unit testing for instance methods works similarly, you may have some challenge...'
---

This tutorial will teach you how to write unit tests for instance methods in Python.

In a [previous tutorial](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/), we covered how to write unit tests for Python functions. While unit testing for instance methods works similarly, you may have some challenges creating and managing objects (instances of a class). 

This tutorial will teach you how to use such methods for setting up and tearing down resources efficiently. 

Let's begin!

## Classes and Objects in Python – A Quick Review

If you're familiar with object-oriented programming, you know that classes let you group related **data** and **behavior** together. You can then use these classes as templates to create instances of the class. If a Python class is a cookie-cutter, then each instance is a cookie. 🍪

The data and behavior are described by the **attributes** and **methods** in the definition of the class, respectively. We'll look at an example to understad these better.

I know this section should have been named classes and objects explained for the impatient. 🙂 To brush up your Python OOP skills, you may check out [this course](https://www.youtube.com/watch?v=Ej_02ICOIgs) on freeCodeCamp's YouTube channel.

%[https://www.youtube.com/watch?v=Ej_02ICOIgs]

## How to Test the Instance Methods of a Python Class

Now, we'll learn how to set up unit tests for instances of Python classes. We'll write unit tests to check the functionality of the `Book` class shown below:

```python
class Book:
    def __init__(self,title,author,pages,price,discount):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.discount = discount
    def get_reading_time(self):
        return f"{self.pages*1.5} minutes"
    def apply_discount(self):
        discounted_price = self.price - (self.discount*self.price)
        return f"${discounted_price}"
```

The `Book` class serves as a template or a blueprint with attributes: title, author, pages, price, and discount. `get_reading_time()` and `apply_discount()` are the instance methods that use the above attributes. 

So we can create book objects from the `Book` class, each with their own attributes.

![Image](https://lh6.googleusercontent.com/JRAfU2HbOIqGFPPEqBi1Wj0Uttbn_TBLgnl0CqnGaqonBaa2KYpBmcJu2aXywtT9eoFJb3H5q4AD8r3ce8oB8sTKX1Y9qkjIiCT4f0A5HHFblsZjtUiPF0kyTLDooVpQnH8HKtX-6joRG7JJTWm-L9Ss-nFBtOxQjHN8Y7LqCtNoR-jMl7rQrAPJ6g)
_Illustration of book class and book objects_

To test the instance methods `get_reading_time()` and `apply_discount()`, we can create two instances of the `Book` class inside the test methods. We can use the assertion method `assertEqual()` to check if the return values of the instance methods are correct.

```python
from book import Book
import unittest

class TestBook(unittest.TestCase):
    def test_reading_time(self):
        book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
        self.assertEqual(book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
        self.assertEqual(book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(book_2.apply_discount(),f"${16 - 16*0.15}" )
        
if __name__=='__main__':
	unittest.main()
```

## How to Set Up and Tear Down Resources During Unit Tests

When setting up tests for instance methods, we instantiate two book objects, then verify if the instance methods work as expected. And we need to do this for each of the methods.

But this is repetitive and suboptimal when you need to test a large number of instance methods. 

In this case, it'll be more convenient if we can define a method that instantiates these objects for us before running each test. This is where the `setUp()` method comes into play. 

### How the `setUp()` and `tearDown()` Methods Work

The `setUp()` and `tearDown()` methods are typically used for the complementary tasks of allocating and deallocating resources, before and after every unit test, respectively. 

* The `setUp()` method runs before every test, and
* The `tearDown()` method runs after every test.

Here, we can use the `setUp()` method to instantiate the book objects. Sometimes, you'll need to use the `tearDown()` method as well. 

For example, if each test adds files to a directory or creates multiple objects in memory, you may want to free up the directory and delete the created objects after each test. We'll add the `tearDown()` method to verify that it runs after each test.

To understand this better, let's add explanatory `print()` statements, as shown in the code below:

```python
from book import Book
import unittest
class TestBook(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        self.book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
    def tearDown(self):
        print("Running tearDown method...")
    def test_reading_time(self):
        print("Running test_reading_time...")
        self.assertEqual(self.book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(self.book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        print("Running test_discount...")
        self.assertEqual(self.book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(self.book_2.apply_discount(),f"${16 - 16*0.15}" )
if __name__=='__main__':
	unittest.main()
```

Now, run the `test_book` module. Here's the output:

```
Output
Running setUp method...
Running test_discount...
Running tearDown method...
.
Running setUp method...
Running test_reading_time...
Running tearDown method...
.
----------------------------------------------------------------------
Ran 2 tests in 0.003s
OK
```

## How to Use the `setUpClass()` and `tearDownClass()` Methods

In addition to the above methods, you can also use the class methods: `setUpClass()` and `tearDownClass()`. 

In Python, class methods bind to a class and not to a particular instance. To define a method as a class method, you can use the `@classmethod` decorator. 

So when should we use these class methods?

Instantiating objects, as in the above example, is a simple task and not computationally expensive. But you may sometimes have tasks that are too expensive to be performed before every test: for instance, spinning up an in-memory database.

If all subsequent tests in the test class only read in some data from the database, we can use the `setUpClass()` class method to spin up the database and the `tearDownClass()` class method to tear down the database after all tests have run.

Putting it all together:

* The `setUpClass()` class method is executed **before** _any_ of the tests are run.
* The `tearDownClass()` class method is executed **after** _all_ the tests have run.
* The `setUp()` and `tearDown()` methods are executed **before** and **after** _each_ test, respectively. 

Let’s add the `setUpClass()` and `tearDownClass()` class methods to the `TestBook` class. 

```python
from book import Book
import unittest
class TestBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        self.book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
    def tearDown(self):
        print("Running tearDown method...")
    def test_reading_time(self):
        print("Running test_reading_time...")
        self.assertEqual(self.book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(self.book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        print("Running test_discount...")
        self.assertEqual(self.book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(self.book_2.apply_discount(),f"${16 - 16*0.15}" )
    @classmethod
    def tearDownClass(cls):
    	print("\ntearDownClass method: Runs after all tests...")
        
if __name__=='__main__':
	unittest.main()
```

Now, rerun `test_book.py`.

From the output below, we see that the `setUpClass()` and `tearDownClass()` methods run before and after all the tests, respectively.

```
Output
setUpClass method: Runs before all tests...
Running setUp method...
Running test_discount...
Running tearDown method...
.
Running setUp method...
Running test_reading_time...
Running tearDown method...
.
tearDownClass method: Runs after all tests...
----------------------------------------------------------------------
Ran 2 tests in 0.010s
OK
```

## Conclusion

I hope this tutorial helped you learn how to set up unit tests for instance methods in Python. 

If you're interested in learning more about the need for unit testing with a focus on doing it for Python functions, consider reading the article [How to Write Unit Tests for Python Functions](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/).

Happy coding!

