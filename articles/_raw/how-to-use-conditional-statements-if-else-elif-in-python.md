---
title: How to Use Conditional Statements in Python – Examples of if, else, and elif
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-07T16:03:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-conditional-statements-if-else-elif-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Conditional.JPG
tags:
- name: Conditionals
  slug: conditionals
- name: Python
  slug: python
seo_title: null
seo_desc: 'Conditional statements are an essential part of programming in Python.
  They allow you to make decisions based on the values of variables or the result
  of comparisons.

  In this article, we''ll explore how to use if, else, and elif statements in Python,
  ...'
---

Conditional statements are an essential part of programming in Python. They allow you to make decisions based on the values of variables or the result of comparisons.

In this article, we'll explore how to use if, else, and elif statements in Python, along with some examples of how to use them in practice.

## How to Use the `if` Statement in Python

The `if` statement allows you to execute a block of code if a certain condition is true. Here's the basic syntax:

```python
if condition:
    # code to execute if condition is true
```

The condition can be any expression that evaluates to a Boolean value (True or False). If the condition is True, the code block indented below the if statement will be executed. If the condition is False, the code block will be skipped.

Here's an example of how to use an `if` statement to check if a number is positive:

```python
num = 5

if num > 0:
    print("The number is positive.")
```

Output:

```python
The number is positive.
```

In this example, we use the `>` operator to compare the value of `num` to 0. If `num` is greater than 0, the code block indented below the `if` statement will be executed, and the message "The number is positive." will be printed.

## How to Use the `else` Statement in Python

The `else` statement allows you to execute a different block of code if the `if` condition is False. Here's the basic syntax:

```python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

If the condition is True, the code block indented below the `if` statement will be executed, and the code block indented below the `else` statement will be skipped.

If the condition is False, the code block indented below the `else` statement will be executed, and the code block indented below the `if` statement will be skipped.

Here's an example of how to use an `if-else` statement to check if a number is positive or negative:

```python
num = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")
```

Output:

```python
The number is negative.
```

In this example, we use an `if-else` statement to check if `num` is greater than 0. If it is, the message "The number is positive." is printed. If it is not (that is, num is negative or zero), the message "The number is negative." is printed.

## How to Use the `elif` Statement in Python

The `elif` statement allows you to check multiple conditions in sequence, and execute different code blocks depending on which condition is true. Here's the basic syntax:

```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition1 is false and condition2 is true
elif condition3:
    # code to execute if condition1 and condition2 are false, and condition3 is true
else:
    # code to execute if all conditions are false
```

The `elif` statement is short for "else if", and can be used multiple times to check additional conditions.

Here's an example of how to use an `if-elif-else` statement to check if a number is positive, negative, or zero:

```python
num = 0

if num > 0:
    print("The number is positive.")
elif num <
```

## Use Cases For Conditional Statements

### Example 1: Checking if a number is even or odd.

```python
num = 4

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

Output:

```python
The number is even.
```

In this example, we use the modulus operator (%) to check if `num` is evenly divisible by 2.

If the remainder of num divided by 2 is 0, the condition num % 2 == 0 is True, and the code block indented below the `if` statement will be executed. It will print the message "The number is even."

If the remainder is not 0, the condition is False, and the code block indented below the `else` statement will be executed, printing the message "The number is odd."

### Example 2: Assigning a letter grade based on a numerical score

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
```

Output:

```python
Your grade is: B
```

In this example, we use an `if-elif-else` statement to assign a letter grade based on a numerical score.

The `if` statement checks if the score is greater than or equal to 90. If it is, the grade is set to "A". If not, the first `elif` statement checks if the score is greater than or equal to 80. If it is, the grade is set to "B". If not, the second `elif` statement checks if the score is greater than or equal to 70, and so on. If none of the conditions are met, the `else` statement assigns the grade "F".

### Example 3: Checking if a year is a leap year

```python
year = 2000

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
```

Output:

```python
2000 is a leap year.
```

In this example, we use nested `if` statements to check if a year is a leap year. A year is a leap year if it is divisible by 4, except for years that are divisible by 100 but not divisible by 400.

The outer `if` statement checks if year is divisible by 4. If it is, the inner `if` statement checks if it is also divisible by 100. If it is, the innermost `if` statement checks if it is divisible by 400. If it is, the code block indented below that statement will be executed, printing the message "is a leap year."

If it is not, the code block indented below the `else` statement inside the inner `if` statement will be executed, printing the message "is not a leap year.".

If the year is not divisible by 4, the code block indented below the `else` statement of the outer `if` statement will be executed, printing the message "is not a leap year."

### Example 4: Checking if a string contains a certain character

```python
string = "hello, world"
char = "w"

if char in string:
    print("The string contains the character", char)
else:
    print("The string does not contain the character", char)
```

**Outcome:**

```python
The string contains the character w
```

In this example, we use the `in` operator to check if the character `char` is present in the string string. If it is, the condition `char` in string is True, and the code block indented below the `if` statement will be executed, printing the message "The string contains the character" followed by the character itself.

If `char` is not present in string, the condition is False, and the code block indented below the `else` statement will be executed, printing the message "The string does not contain the character" followed by the character itself.

## Conclusion

Conditional statements (if, else, and elif) are fundamental programming constructs that allow you to control the flow of your program based on conditions that you specify. They provide a way to make decisions in your program and execute different code based on those decisions.

In this article, we have seen several examples of how to use these statements in Python, including checking if a number is even or odd, assigning a letter grade based on a numerical score, checking if a year is a leap year, and checking if a string contains a certain character.

By mastering these statements, you can create more powerful and versatile programs that can handle a wider range of tasks and scenarios.

It is important to keep in mind that proper indentation is crucial when using conditional statements in Python, as it determines which code block is executed based on the condition.

With practice, you will become proficient in using these statements to create more complex and effective Python programs.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [Linkedin](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
