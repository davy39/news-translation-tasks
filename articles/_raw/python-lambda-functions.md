---
title: Python Lambda Functions – How to Use Anonymous Functions with Examples
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-02-24T17:25:28.000Z'
originalURL: https://freecodecamp.org/news/python-lambda-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/lambda-1.png
tags:
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: null
seo_desc: "Lambda functions, also known as anonymous functions, are small, one-time-use\
  \ functions in Python. \nYou can define them using the lambda keyword followed by\
  \ the function's inputs, a colon, and the function's expression. The output of a\
  \ lambda function..."
---

Lambda functions, also known as anonymous functions, are small, one-time-use functions in Python. 

You can define them using the `lambda` keyword followed by the function's inputs, a colon, and the function's expression. The output of a lambda function is returned as the result of the expression, rather than a return statement.

The main purpose of lambda functions is to allow for the creation of small, throw-away functions that you can use in other parts of a program. This can be useful when you need to pass a simple function as an argument to another function, for example.

### Syntax for creating lambda functions

Here is the syntax for creating a lambda function in Python:

```python
lambda arguments: expression

```

## Lambda Functions vs Named Functions Defined Using the `def` Keyword

When compared to named functions defined using the `def` keyword, lambda functions have some key differences. 

Named functions can have multiple expressions and they use return statements. Lambda functions can only have one expression and the value of that expression is returned automatically. 

Named functions can also be reused throughout a program, while lambda functions are used only once.

```python
def greet(name):
    return "Hello " + name
print(greet("John")) 

# Output: "Hello John"

```

As you can see, the named function is defined using the `def` keyword, followed by the function name and its inputs in parentheses. The function body is indented, and the return statement is used to return the result of the expression. 

Named functions can be called multiple times, making them more flexible than lambda functions for complex operations.

Here's the equivalent code using a named function defined with the `lambda` keyword:

```python
greet = lambda name: "Hello " + name
print(greet("John")) 

# Output: "Hello John"

```

## **How to Use Lambda Functions**

This section covers the basics of how to create and use lambda functions, including their syntax and how to use them as arguments in higher-order functions such as map, filter, and reduce. 

Additionally, this section explores how you can use lambda functions in sorting and in list comprehensions. By the end, you should have a foundational understanding of the basic uses of lambda functions.

### How to use lambda functions as arguments in higher-order functions (`map`, `filter`, `reduce`)

Lambda functions are often used as arguments in higher-order functions such as `map`, `filter`, and `reduce`. These functions allow you to apply a given operation to every element of a list or other iterable.

Here's an example of using a lambda function with the `map` function:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) 

# Output: [1, 4, 9, 16, 25]

```

In this example, the lambda function takes one input `x` and returns the square of that value. The `map` function applies this operation to every element of the `numbers` list and returns a new list with the results.

Here's another example using the `filter` function:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

# Output: [2, 4]

```

In this example, the lambda function takes one input `x` and returns `True` if `x` is even, and `False` otherwise. The `filter` function applies this operation to every element of the `numbers` list and returns a new list with only the elements that returned `True`.

### How to use lambda functions to return functions as values

You can also use lambda functions to return functions as values. For example:

```python
def make_adder(x):
    return lambda y: x + y
add5 = make_adder(5)
print(add5(3)) 

# Output: 8

```

In this example, the `make_adder` function takes one input `x` and returns a lambda function that takes one input `y` and returns the sum of `x` and `y`. The `add5` variable is assigned the result of calling `make_adder(5)`, meaning it now references a lambda function that adds 5 to its input.

### How to use lambda functions in sorting

You can also use lambda functions in sorting operations to specify custom sort orders. For example:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers) 

# Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

```

In this example, the lambda function takes one input `x` and returns `-x`, meaning that the sort order will be in descending order. The `sorted` function sorts the `numbers` list based on the values returned by the lambda function.

## Limitations of Lambda Functions

While lambda functions are a convenient way to write short and simple functions, they have some limitations. 

One of the main limitations is that lambda functions are limited to a single expression, meaning that they cannot contain multiple statements or complex control flow. 

In addition, lambda functions cannot be referenced by name and can only be invoked when they are defined, which makes them less flexible than named functions.

Another limitation is that lambda functions do not have a name, which can make debugging more difficult and make it harder to understand the code. 

In general, it's a good idea to use named functions for complex operations and only use lambda functions for short and simple operations.

## **Advanced Uses of Lambda Functions**

This section covers how to use lambda functions with advanced functions such as reduce, filter, sorted, and key arguments. Additionally, this section provides information on using lambda functions to create anonymous functions for event handlers.

### How to use lambda functions with `reduce`

The `reduce` function is a higher-order function that takes a binary function (a function that takes two arguments) and a list. It returns a single value that is the result of applying the binary function to the elements of the list in a cumulative way. 

For example, to calculate the product of all elements in a list, you could use the following code:

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, numbers)
print(product) 

# Output: 120

```

In this example, the lambda function `lambda x, y: x*y` is used as the binary function in the `reduce` function. The `reduce` function starts by applying the binary function to the first two elements of the list, and then applies the result to the next element, and so on until it has processed all elements of the list.

### How to use lambda functions with `filter`

The `filter` function is another higher-order function that takes a function and a list, and returns a new list that contains only the elements of the original list for which the function returns `True`. 

For example, to filter out even numbers from a list, you could use the following code:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

# Output: [2, 4]

```

In this example, the lambda function `lambda x: x % 2 == 0` is used as the function argument in the `filter` function. The `filter` function invokes this lambda function for each element in the `numbers` list and includes the element in the result list only if the lambda function returns `True`.

### How to use lambda functions with the `sorted` function

The `sorted` function is a built-in function that sorts a list of elements. The `sorted` function can take an optional `key` argument, which is a function that takes an element of the list and returns a value that is used as the sort key. 

For example, to sort a list of dictionaries by a specific key, you could use the following code:

```python
employees = [{"name": "John", "age": 32},              {"name": "Jane", "age": 27},              {"name": "Jim", "age": 40}]
sorted_employees = sorted(employees, key=lambda x: x["age"])
print(sorted_employees)

# Output: [{"name": "Jane", "age": 27}, 
#          {"name": "John", "age": 32}, 
#          {"name": "Jim", "age": 40}]

```

In this example, the lambda function `lambda x: x["age"]` is used as the `key` argument in the `sorted` function. The `sorted` function uses this lambda function to extract the "age" value for each dictionary in the `employees` list and uses these values as the sort keys.

### How to use lambda functions in the `key` argument of various functions

In addition to the `sorted` function, many other functions in Python can take a `key` argument, including the `max`, `min`, and `sorted` functions. 

The `key` argument is a function that takes an element of the list and returns a value that is used as the sort key, as well as for comparison purposes in the case of the `max` and `min` functions.

For example, to find the employee with the highest salary in a list of employees, you could use the following code:

```python
employees = [{"name": "John", "salary": 50000}, {"name": "Jane", "salary": 55000}, {"name": "Jim", "salary": 60000}]
highest_salary_employee = max(employees, key=lambda x: x["salary"])
print(highest_salary_employee) 

# Output: {"name": "Jim", "salary": 60000}

```

In this example, the lambda function `lambda x: x["salary"]` is used as the `key` argument in the `max` function. The `max` function uses this lambda function to extract the "salary" value for each employee in the `employees` list and uses these values to compare the employees and find the one with the highest salary.

### How to use lambda functions to create anonymous functions for event handlers

You can also use lambda functions to create anonymous functions for event handlers in GUI programming or for other similar purposes. 

For example, in the following code, a button click event is handled using a lambda function in Tkinter (a GUI programming toolkit for Python):

```python
import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me!", command=lambda: print("Button clicked!"))
button.pack()
root.mainloop()

```

In this example, we use the lambda function `lambda: print("Button clicked!")` as the `command` argument of the `Button` widget in Tkinter. When the button is clicked, the lambda function is executed and the message "Button clicked!" is printed to the console.

This demonstrates the versatility and flexibility of lambda functions. You can use them in a variety of contexts where anonymous functions are required.

## **Best Practices for Using Lambda Functions**

This section covers a range of best practices, including keeping lambda functions simple and easy to understand, avoiding complex expressions and statements, choosing the appropriate type of function for the task, and documenting lambda functions for better code readability. 

We'll also highlight the importance of using descriptive variable names in lambda functions to improve the readability of your code.

### Keep lambda functions simple and easy to understand

One of the best practices for using lambda functions is to keep them simple and easy to understand. 

Lambda functions are intended to be small, anonymous, single-expression functions, and complex or multi-statement functions are better suited to be defined using the `def` keyword.

For example, the following lambda function is simple, easy to understand, and does exactly what it is intended to do:

```python
square = lambda x: x * x
print(square(5)) 

# Output: 25

```

### Avoid complex expressions and statements in lambda functions

In addition to keeping lambda functions simple, it is also important to avoid complex expressions and statements in lambda functions. 

Complex expressions and statements make the code harder to understand and maintain, and can lead to bugs.

For example, the following lambda function is too complex and difficult to understand:

```python
calculate = lambda x, y: x + y if x > y else x - y
print(calculate(5, 10)) 

# Output: -5

```

In such cases, it is better to define a named function using the `def` keyword and provide a meaningful name for the function. This makes the code more readable and easier to maintain:

```python
def calculate(x, y):
    if x > y:
        return x + y
    else:
        return x - y

print(calculate(5, 10)) 

# Output: -5

```

### When to use lambda functions and when to use named functions

Lambda functions are best used in situations where you need a small, anonymous, single-expression function. They are not well suited for complex functions with multiple expressions and statements.

For example, a good use case for a lambda function is as an argument to a higher-order function such as `map`, `filter`, or `reduce`. A bad use case for a lambda function is a complex function with multiple expressions and statements.

In general, it is better to use named functions defined using the `def` keyword for functions that are complex, multi-statement, or are used multiple times in your code.

### Document lambda functions for better code readability

Another best practice for using lambda functions is to document them for better code readability. 

While lambda functions are often intended to be simple and easy to understand, it can still be helpful to provide a brief explanation of what the function does in the form of a docstring or a comment.

For example, the following lambda function is documented for better code readability:

```python
# This lambda function returns the square of its input
square = lambda x: x * x
print(square(5)) 

# Output: 25

```

### Use descriptive variable names in lambda functions

Finally, it is important to use descriptive variable names in lambda functions, just as you would in any other function. Descriptive variable names make the code easier to understand and maintain.

For example, the following lambda function uses descriptive variable names:

```python
# This lambda function returns the sum of its inputs
sum = lambda x, y: x + y
print(sum(5, 10)) 

# Output: 15

```

By following these best practices, you can ensure that your lambda functions are clear, concise, and easy to understand, making your code more readable, maintainable, and error-free.

## **Conclusion**

In this guide, we covered the basics of lambda functions in Python, including their definition and purpose, syntax, and basic and advanced usage in various applications. 

We also discussed some best practices for using lambda functions, including keeping them simple and easy to understand, avoiding complex expressions and statements, choosing the appropriate type of function for the task, and documenting them for better code readability.

Lambda functions can be a powerful tool for writing concise, readable, and efficient code. But they have some limitations, such as being restricted to a single expression and having limited functionality compared to named functions. It's important to consider these limitations and choose the appropriate type of function for the task at hand.

In conclusion, this guide has provided an overview of lambda functions and their uses in Python, and I hope that it has been helpful in your journey to learn more about this topic. For further learning, you may want to explore the official Python documentation and practice using lambda functions in your own projects.

---

Visit my [blog](https://blog.ashutoshkrris.in) to read more articles like this. You may also choose to follow me on [Twitter](https://twitter.com/ashutoshkrris).

