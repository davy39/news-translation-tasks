---
title: How to Use Loops in Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-07T21:36:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-loops-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Loops.JPG
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: null
seo_desc: 'Loops are an essential concept in programming. They allow you to execute
  a block of code repeatedly based on certain conditions.

  Python offers two types of loops: for and while loops. In this article, we will
  explore both of these loop types and prov...'
---

Loops are an essential concept in programming. They allow you to execute a block of code repeatedly based on certain conditions.

Python offers two types of loops: for and while loops. In this article, we will explore both of these loop types and provide examples of how to use them in your Python code.

## How to Use For Loops in Python

You'll use a for loop when you want to iterate over a collection of items or when you know the exact number of times you want to execute a block of code.

Here's the code for a for loop in Python:

```python
for variable in iterable:
    # code to execute
```

* variable is a variable that represents the current item in the iterable that we're iterating over.
    
* iterable is a collection of items that we want to iterate over, such as a list, tuple, string, or range.
    

For example, let's say we have a list of numbers and we want to print each number:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

Output

```python
1
2
3
4
5
```

We can also use the `range()` function to specify a range of numbers to iterate over:

```python
for num in range(1, 6):
    print(num)
```

Output:

```python
1
2
3
4
5
```

The `range()` function takes two arguments: the starting number and the ending number (exclusive). In this case, the loop will iterate over the numbers from 1 to 5.

## How to Use While Loops in Python

You'll use a while loop when you want to execute a block of code repeatedly based on a condition.

Here's the syntax for a while loop in Python:

```python
while condition:
    # code to execute
```

`condition` is a boolean expression that determines whether the loop should continue or not.

For example, let's say we want to print the numbers from 1 to 5 using a while loop:

```python
num = 1
while num <= 5:
    print(num)
    num += 1
```

In this example, we initialize the `num` variable to 1 and then execute the loop as long as `num` is less than or equal to 5. Inside the loop, we print the current value of `num` and then increment it by 1.

We can also use a while loop to keep asking the user for input until they enter a valid response:

```python
valid_response = False
while not valid_response:
    response = input("Enter 'yes' or 'no': ")
    if response.lower() == 'yes' or response.lower() == 'no':
        valid_response = True
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
```

Let's take a look at some advanced uses of loops in Python.

## How to Use Nested Loops in Python

Nested loops are loops that are contained inside other loops. They allow us to iterate over a collection of items multiple times and are useful for tasks such as generating all possible combinations of items.

Here's an example of how to use nested loops to generate all possible pairs of numbers from two lists:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

for num1 in list1:
    for num2 in list2:
        print(num1, num2)
```

Output:

```python
1 4
1 5
1 6
2 4
2 5
2 6
3 4
3 5
3 6
```

In this example, we use a nested for loop to iterate over each item in list1 and list2, and print out all possible pairs of numbers.

## List Comprehension in Python

List comprehensions are a concise way to create lists based on existing lists or other iterable objects. They use a for loop and an optional conditional statement to generate the new list.

Here's an example of how to use list comprehension to create a new list of even numbers from an existing list:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
```

Output:

```python
[2, 4, 6, 8, 10]
```

In this example, we use a list comprehension to iterate over each number in the numbers list and add it to the `even_numbers` list if it is even (that is, the remainder when divided by 2 is 0).

## How to Iterate Over a Dictionary in Python

In Python, we can iterate over the keys, values, or items (key-value pairs) of a dictionary using a for a loop.

Here's an example of how to iterate over the items of a dictionary and print out the key-value pairs:

```python
fruits = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

for fruit, color in fruits.items():
    print(f"The {fruit} is {color}.")
```

Output:

```python
The apple is red.
The banana is yellow.
The orange is orange.
```

In this example, we use the `items()` method of the `fruits` dictionary to iterate over each key-value pair, and then print out a formatted string that includes the fruit and its corresponding color.

## Conclusion

Loops are an essential part of programming in Python. They allow us to automate repetitive tasks and manipulate data in powerful ways.

By understanding the basics of for and while loops, as well as more advanced concepts such as nested loops and list comprehensions, you'll be able to write efficient and effective code in Python.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [Linkedin](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/)
