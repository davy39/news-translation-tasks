---
title: How to Swap the Values of Two Variables Without a Temporary Variable in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-24T14:50:48.000Z'
originalURL: https://freecodecamp.org/news/swapping-values-of-two-variables-without-a-temporary-variable-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/How-To-Swap-The-Values-of-Two-Variables-Without-a-Temporary-Variable-in-python-1-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Jacob Isah \nSwapping the values of two variables is a common task in\
  \ programming. While the most straightforward approach involves using a temporary\
  \ variable, Python provides several elegant techniques to achieve the same result\
  \ without the need f..."
---

By Jacob Isah 

Swapping the values of two variables is a common task in programming. While the most straightforward approach involves using a temporary variable, Python provides several elegant techniques to achieve the same result without the need for that extra variable.   
  
In this tutorial, we will take a look at some methods to swap variable values in Python without using a temporary variable.

## Why You'd Want to Swap the Values of Two Variables Without a Temporary Variable in Python

Swapping the values of two variables without using a temporary variable is important in situations where you want to minimize memory usage or code complexity. 

While using a temporary variable is a straightforward and common method for swapping values, there are situations where you might prefer alternative techniques. 

### Advantages of Swapping Without a Temporary Variable

* **Memory Efficiency:** Swapping without a temporary variable reduces memory overhead because you don't need an extra variable to hold one of the values temporarily. In some resource-constrained environments, this can be important.
* **Conciseness:** Methods like tuple unpacking and XOR bitwise operations offer more concise and elegant solutions. They can make your code more readable and require fewer lines, which is especially beneficial for small code snippets.
* **Functional and Expressive Code:** Some developers prefer concise and expressive code. Using these methods can make the intention of the code clearer and reduce clutter.

### Advantages of Using a Temporary Variable

* **Compatibility**: Not all scenarios allow for the use of some advanced swapping techniques. For instance, the **XOR** bitwise operation method is designed for integers and doesn't work well with other data types.
* **Clarity and Readability:** It's easier to understand for developers who might not be familiar with more advanced techniques. Swapping values with a temporary variable is the most straightforward and widely recognized method. 
* **Maintainability:** Code that uses a temporary variable is often more maintainable in the long run because it's easier to understand and less prone to errors.

## How to Swap Variables in Python Using Tuple Unpacking

Python allows us to swap the values of two variables with a single line of code using tuple unpacking. (You can [read more about tuples in Python here](https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/) if you need a review.)

Tuple unpacking, also known as tuple assignment or tuple decomposition, allows developers to assign the elements of a tuple to multiple variables in a single statement. 

This technique is possible because you can assign multiple variables at once using a tuple on the right side of the assignment operator. Here's an example:

```python
a = 5
b = 10
a, b = b, a
print("a:", a)
print("b:", b)
```

In this code, `a` and `b` are swapped without a temporary variable. The values are reassigned in a single step, making this approach concise and readable.

## How to Swap Variables in Python Using Arithmetic Operations

Another approach to swapping values is by using arithmetic operations. Here we are making use of addition and subtraction to perform the swap without the need for an extra variable.

```python
a = 5
b = 10
a = a + b
b = a - b
a = a - b
print("a:", a)
print("b:", b)
```

In this method, the sum of `a` and `b`  is assigned to `a` and then `b` is updated to the difference between the new  `a` and the old  `b`. Finally,  `a` is updated to show the difference between the new  `a` and the new  `b`. The result is a successful swap of the values.

## How to Swap Variables in Python Using the XOR Bitwise Operator

For integer values, a clever method involves using the [**XOR (^)** bitwise operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR) to swap values without a temporary variable.

The XOR operator, represented by the `^` symbol, is a bitwise operator that operates on the individual bits of numbers. When applied to integers, it can be a clever way to swap variable values without a temporary variable.

```python
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print("a:", a)
print("b:", b)
```

### Here's how this method works step by step

Let's walk through what's happening in the code above:

**Initial Values:** In the beginning, `a` is set to 5, and `b` is set to 10.

* In binary, `a` is `0101`, and `b` is `1010`. 

**XORing `a` and `b` (First Line):**

* `a ^ b` is the XOR operation between `a` and `b`.
* The XOR (^) operator compares the binary representations of `a` and `b` bit by bit.
* In binary, `a` is `0101`, and `b` is `1010`. When XORed, it flips the bits that are different and leaves the bits that are the same.
* The result is `1111` in binary, which is 15 in decimal.
* Therefore, after the first line, `a` becomes 15.

**XORing `a` and the New `b` (Second Line):**

* Now that `a` has the value 15 and `b` is still 10, we XOR `a` with the new `b`.
* `a ^ b` is `15 ^ 10`. In binary, `a` is `1111`, and `b` is `1010`.
* The XOR operation flips the different bits, so the result is `0101` in binary, which is 5 in decimal.
* After this line, `b` becomes 5.

**XORing `a` and the New `b` Again (Third Line):**

* Now, with `a` being 15 and `b` being 5, we XOR `a` with the new `b` one more time.
* `a ^ b` is `15 ^ 5`. In binary, `a` is `1111`, and `b` is `0101`.
* The XOR operation again flips the different bits, so the result is `1010` in binary, which is 10 in decimal.
* After this line, `a` becomes 10.

At this point, the values of `a` and `b` have been effectively swapped. The XOR operation allowed us to perform the swap without using an additional temporary variable. 

This method works because the XOR operation between two identical numbers results in 0, and XORing any number with 0 leaves the number unchanged.

This technique is a clever way to achieve value swapping for integer variables and can be useful in scenarios where memory efficiency or code conciseness is a priority. However, it's important to remember that it's specifically designed for integer values and may not work as expected for other data types.

## How to Swap Variables in Python Using Mathematical Expressions (For Numeric Values)

Another straightforward method involves using mathematical expressions to swap values.

```python
a = 3
b = 7
a = a + b - (b := a)
print("a:", a)
print("b:", b)
```

In Python, an assignment expression `(:=)` allows you to assign a value to a variable as part of a larger expression. It's often used to both assign a value to a variable and use that assigned value in a single line. This can be particularly useful when you want to avoid repetition and write more concise code.

### Here's what's happening step by step

1. `b := a`: This part of the expression is an assignment expression. It assigns the value of `a` to `b`. So, after this assignment, `b` will have the value of `a`, and `a` remains unchanged. This assignment happens within the larger expression.
2. `a + b - (b := a)`: The rest of the expression performs mathematical operations. It calculates the sum of `a` and the original `b`, subtracting the value of `b` after it was assigned the value of `a`.

* `a + b` adds the original values of `a` and `b`.
* `(b := a)` has already updated `b` to have the value of `a`, so this part evaluates to `a`.
* Finally, the result is subtracted from the sum of `a` and the original `b`.

Effectively, this single line of code swaps the values of `a` and `b` without the need for a temporary variable. It assigns the value of `a` to `b` and the value of `b` to `a` while performing the swap operation in one line.

But you should note that while assignment expressions can make code more concise, they can also make it less readable if you're not familiar with this feature. So make sure you use assignment expressions carefully and consider readability and maintainability when deciding whether to use them.

## How to Swap Variables in Python Using a Function

If you need to swap variables in multiple places within your code, you can create a function to make the process more reusable.

```python
def swap(a, b):
	return b, a
a = 5
b = 10
a, b = swap(a, b)
print("a:", a)
print("b:", b)
```

This function hides the swapping logic and returns the swapped values, making the code more modular and readable.

## When to Use Each Method

Each method of swapping values in Python without a temporary variable has its own strengths and weaknesses. Choosing which method to use depends on the specific use case and your coding preferences. 

Here's a summary of the use cases that are best suited to each example, along with some considerations:

### Tuple Unpacking

* Use Case: Swapping two values with simplicity and readability in mind.
* Strengths: This method is concise, easy to understand, and is especially well-suited for swapping two variables in a clear and straightforward manner.
* Considerations: It works best for two variables, and it's not suitable for more complex data structures.

### Arithmetic Operations

* Use Case: A straightforward and easy-to-understand method for swapping values, suitable for a broad range of scenarios.
* Strengths: The arithmetic approach is a versatile method that works well with numeric values and is easy to apply in various contexts.
* Considerations: It requires three arithmetic operations, which might be less concise than other methods.

### XOR Bitwise Operator

* Use Case: Swapping integer values while minimizing memory usage.
* Strengths: This method is memory-efficient and concise. It's suitable for scenarios where you want to save memory and use a more advanced, efficient approach.
* Considerations: It's specific to integers and might not be as readable for developers who are not familiar with bitwise operations.

### Mathematical Expressions (Assignment Expression)

* Use Case: A concise method for swapping values while maintaining code readability.
* Strengths: This technique can be used to swap values concisely in a single line. It's particularly useful when you want a balance between conciseness and readability.
* Considerations: It relies on the use of assignment expressions (:=), which may not be familiar to all Python developers.

### Using a Function

* Use Case: When you need to swap values in multiple places within your code.
* Strengths: Creating a function for value swapping encapsulates the logic and makes it reusable. This is helpful when you need to swap values in different parts of your code.
* Considerations: It introduces a function call, which might be less concise for a simple one-time swap.

There isn't a one-size-fits-all method that works better in every situation. Your choice should be guided by factors like the specific use case, the data types involved, and the importance of memory efficiency or code readability.

In terms of ease, methods like tuple unpacking and arithmetic operations are generally easier to understand for most Python developers. The XOR bitwise method, while efficient, might be less readable and not as commonly used. The mathematical expression method with assignment expressions is concise but might be less familiar to developers who are not up to date with the latest Python features.

Ultimately, the best method depends on your specific requirements and coding style preferences. It's essential to strike a balance between efficiency, readability, and maintainability when choosing a value-swapping technique.

## Conclusion

In this article, I explained how you can swap the values of two variables in Python without a temporary variable. We looked at using several techniques, such as tuple unpacking, arithmetic operations, XOR bitwise operations, mathematical expressions, or encapsulating (hiding) the logic within a function. 

These methods provide options for different situations, from concise one-liners to reusable functions. Choose the one that best suits your specific needs, taking into consideration the data types and the context of your code. Whether you prioritize readability, performance, or conciseness, Python offers a solution for all.

