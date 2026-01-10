---
title: Lambda Functions in Python – How to Use Lambdas with Map, Filter, and Reduce
subtitle: ''
author: Samyak Jain
co_authors: []
series: null
date: '2024-06-14T14:44:05.000Z'
originalURL: https://freecodecamp.org/news/lambda-functions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/python-lambda-functions.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this tutorial, we will explore the various aspects of lambda functions
  in Python, including their syntax, use cases, and limitations.

  By understanding how to effectively utilize lambda functions, you can write more
  concise and efficient Python cod...'
---

In this tutorial, we will explore the various aspects of lambda functions in Python, including their syntax, use cases, and limitations.

By understanding how to effectively utilize lambda functions, you can write more concise and efficient Python code. This will enhance your programming skills and make your codebase cleaner and easier to manage.

## **Table of Contents:**

1. [What are Lambda Functions in Python?](https://www.freecodecamp.org/news/lambda-functions-in-python/#what-are-lambda-functions-in-python)
2. [Lambda Function Syntax and Basic Uses](https://www.freecodecamp.org/news/lambda-functions-in-python/#lambda-function-syntax-and-basic-uses)
3. [Ways to Call Lambda Functions](https://www.freecodecamp.org/news/lambda-functions-in-python/#ways-to-call-lambda-functions)  
– [Assigning to a Variable](https://www.freecodecamp.org/news/lambda-functions-in-python/#1-assigning-to-a-variable)  
– [Directly Calling the Lambda Function](https://www.freecodecamp.org/news/lambda-functions-in-python/#2-directly-calling-the-lambda-function)  
– [Using as an Argument to Higher-Order Functions](https://www.freecodecamp.org/news/lambda-functions-in-python/#3-using-as-an-argument-to-higher-order-functions)
4. [Additional Use Cases](https://www.freecodecamp.org/news/lambda-functions-in-python/#additional-use-cases)
5. [Conclusion](https://www.freecodecamp.org/news/lambda-functions-in-python/#conclusion)

## **What are Lambda Functions in Python?**

In Python, a lambda function is a small, anonymous function defined using the `lambda` keyword.

These functions are typically used for short, throwaway operations where a full function definition might be overkill. They are called anonymous because they do not require a name (although they can be assigned to a variable for reuse).

Lambda functions excel in scenarios where you need a quick, simple function for a brief period, and a full function definition would be excessive. This makes them ideal for operations that are straightforward and can be written in a single line, such as simple mathematical calculations or basic data transformations.

They are particularly used in functional programming contexts with higher-order functions like `map`, `filter`, and `reduce` where they are often passed as arguments. Just remember that for more complex operations, regular functions are preferred for their readability and maintainability.

## **Lambda Function Syntax and Basic Uses**

```python
lambda arguments: expression

# to give it a name, assign it to a variable:
function_name = lambda arguments: expression

# this is equivalent to:
def function_name(arguments):
	return expression
```

Unlike regular functions defined with `def`, lambda functions are limited to a single expression due to their design for simplicity and brevity. They can take single or multiple arguments but cannot contain statements or multiple expressions.

Lambda functions are intended for short, straightforward operations that can be written in a single line.

Example:

```python
# Regular function to find the average of three numbers
def average(x, y, z):
    return (x + y + z) / 3

# Lambda function to find the average of three numbers
average = lambda x, y, z: (x + y + z) / 3
```

Although lambda functions can only contain one expression, we can still do a lot with them.

For example, here's a Lambda function to concatenate 2 strings and convert them to uppercase:

```python
concat_and_uppercase = lambda str1, str2: (f'The concatenated string is {str1 + str2}'.upper())

print(concat_and_uppercase("hello", "world"))  # Output: THE CONCATENATED STRING IS HELLOWORLD
```

## **Ways to Call Lambda Functions**

There are primarily three ways to use or call lambda functions:

### **1. Assigning to a Variable**

Assign the lambda function to a variable and then call it using that variable:

```python
multiply = lambda x, y: print(f'{x} * {y} = {x * y}')
multiply(2, 10)  # Output: 2 * 10 = 20

or 

multiply = lambda x, y: f'{x} * {y} = {x * y}'
print(multiply(2, 10))  # Output: 2 * 10 = 20
```

### **2. Directly Calling the Lambda Function**

Define and immediately invoke the lambda function by wrapping the definition in parentheses and providing the arguments directly:

```python
print((lambda x, y: f'{x} * {y} = {x * y}')(2, 10))  # Output: 2 * 10 = 20

or

(lambda x, y: print(f'{x} * {y} = {x * y}'))(2, 10)  # Output: 2 * 10 = 20
```

### **3. Using as an Argument to Higher-Order Functions**

Lambda functions are often used as arguments to higher-order functions like `map`, `filter`, and `reduce`.

These are functions that take other functions as arguments. They help in processing collections of data (like lists or tuples) in a functional programming style.

#### **Using lambda functions with `map()`**

The `map` function applies a specified function to each item in an iterable (like a list) and returns a new iterable with the updated items.

```python
# syntax

map(function, iterable)

```

* `function` here takes one argument and returns a value.
* iterable's elements (for example, `list`, `tuple`) will be passed to the function.

Example:

```python
# List of pairs of numbers
pairs = [(2, 3), (4, 5), (6, 7)]

# Using lambda function with map to multiply each pair and print the result
list(map(lambda pair: print(f'{pair[0]} * {pair[1]} = {pair[0] * pair[1]}'), pairs))
```

**Explanation:** In this code, we use a lambda function to define a small, anonymous function that takes each pair of numbers and prints their multiplication.

The `map` function applies this lambda function to each pair (tuple) in the list. Wrapping the `map` call with `list` ensures the lambda function is executed for each pair. As a result, the code prints the multiplication results for each pair in the list, showing outputs like "2 * 3 = 6", "4 * 5 = 20", and "6 * 7 = 42".

#### **Using lambda functions with `filter()`**

The `filter` function filters elements in an iterable based on a specified predicate. Only elements for which the predicate returns `True` are included in the new iterable.

```python
# syntax

filter(predicate, iterable)
```

Predicate is a function that takes one argument and returns a boolean value (True or False). Iterable elements here will be tested by the predicate.

Example:

```python
# List of ages
ages = [25, 30, 18, 42, 17, 50, 22, 19]

# Function to filter adults (age 18 and above) using filter with lambda
adults = filter(lambda age: age >= 18, ages)
print(list(adults))  # Output: [25, 30, 18, 42, 50, 22, 19]
```

**Explanation:** In this code, we start with a list of ages. We use a lambda function to define a simple condition that checks if an age is 18 or older.

The `filter` function applies this lambda function to each age in the list, filtering out any ages below 18. By converting the result of `filter` to a list, we obtain a list of ages that are 18 and above. Finally, we print this filtered list, which results in the ages `[25, 30, 18, 42, 50, 22, 19]` being displayed, as these are the ages that meet the criterion of being 18 or older.

#### **Using lambda functions with `reduce()`**

The `reduce` function applies a specified function to the elements of an iterable cumulatively to reduce them to a single value. It is part of the `functools` module.

```python
# syntax

from functools import reduce
reduce(function, iterable)

```

Here, Function takes two arguments and returns a single value. Iterable elements will be processed by the function.

Example:

```python
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce with lambda to sum the numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
```

**Explanation:** In this code, we start with a list of numbers. We use the `reduce` function from the `functools` module to compute the sum of all the numbers in the list. We use a lambda function to define a simple addition operation that takes two arguments, `x` and `y`, and returns their sum. The `reduce` function applies this lambda function cumulatively to the items in the list, starting from the first pair and continuing through the entire list, like this:

* Initially, `x` is the first element of the list (1) and `y` is the second element (2), resulting in 3.
* This sum (3) then becomes `x`, and the next element in the list (3) becomes `y`, yielding 6.
* This process continues until all elements in the list have been summed. Ultimately, the final result is 15, representing the sum of all the numbers in the list [1, 2, 3, 4, 5].

## **Additional Use Cases**

Lambda functions can also be used in sorting or other functional programming contexts. For example:

### **Sorting a List of Strings:**

```python
cities = ["India", "Germany", "America", "Japan"]
sorted_cities = sorted(cities, key=lambda city: city.lower())

print(sorted_cities)  # Output: ['America', 'Germany', 'India', 'Japan']
```

In this code, we have a list called `cities` containing the names of different cities. We use the `sorted` function to sort these city names alphabetically, ignoring case sensitivity. The `key` parameter in the `sorted` function allows us to specify a function (in this case, a lambda function) to customize the sorting order.

The lambda function `lambda city: city.lower()` converts each city name to lowercase before sorting. This ensures that the sorting is case-insensitive, so cities with different capitalization are treated the same way.

After sorting, the sorted list is assigned to the variable `sorted_cities`, and we print the result. The output shows the sorted list of cities: `['America', 'Germany', 'India', 'Japan']`, where the cities are arranged alphabetically ignoring the case of the letters.

### **Lambda Functions in List Comprehensions:**

Lambda functions can be used within list comprehensions to apply a function to each element in a list.

**Example:**

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using lambda in list comprehension to square each number
squared_numbers = [(lambda x: x ** 2)(x) for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

## **Conclusion**

Lambda functions in Python provide a quick and concise way to create small, throwaway functions. They're especially useful in functional programming with higher-order functions like `map`, `filter`, and `reduce`.

While lambda functions are powerful and concise, make sure you balance their use with code readability and maintainability. For more complex logic, regular functions defined with `def` are preferred because they support multiple expressions and statements, and you can include documentation.

By understanding and using lambda functions effectively, you can write more concise and efficient Python code.

**Thank you for reading!** If you have any comments, criticisms, or questions, feel free to tweet or reach out to me at @[OGsamyak](https://x.com/OGsamyak). Your feedback helps me improve!

