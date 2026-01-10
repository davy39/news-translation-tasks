---
title: Learn Python Basics – A Guide for Beginners
subtitle: ''
author: Chepkirui Dorothy
co_authors: []
series: null
date: '2024-02-20T19:04:56.000Z'
originalURL: https://freecodecamp.org/news/learn-python-basics
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/learn-python-image.png
tags:
- name: beginner
  slug: beginner
- name: Python
  slug: python
seo_title: null
seo_desc: "Are you eager to dive into the world of programming but unsure where to\
  \ begin? Look no further – Python is an excellent starting point for both newcomers\
  \ and seasoned developers. \nIn this guide, I'll take you through the basics so\
  \ you can get started..."
---

Are you eager to dive into the world of programming but unsure where to begin? Look no further – Python is an excellent starting point for both newcomers and seasoned developers. 

In this guide, I'll take you through the basics so you can get started on your Python journey.

## Table of Contents

<ul>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#why-learn-python">Why Learn Python?</a></li>
    <li><a href="#key-characteristics-of-python">Key Characteristics of Python</a></li>
    <li><a href="#practical-uses-of-python">Practical Uses of Python</a></li>
    <li><a href="#how-to-write-hello-world-in-python">How to Write "Hello, World" in Python</a></li>
    <li><a href="#python-variables-and-data-types">Python Variables and Data Types</a>
        <ul>
            <li><a href="#primitive-fundamental-data-types-">Primitive (Fundamental) Data Types</a>
                <ul>
                    <li><a href="#characteristics-of-primitive-data-types-">Characteristics of Primitive Data Types</a></li>
                    <li><a href="#use-cases-for-primitive-data-types-">Use Cases for Primitive Data Types</a></li>
                </ul>
            </li>
            <li><a href="#non-primitive-composite-data-types-in-python">Non-Primitive (Composite) Data Types in Python</a>
                <ul>
                    <li><a href="#characteristics-of-non-primitive-data-types-">Characteristics of Non-Primitive Data Types</a></li>
                    <li><a href="#use-cases-for-non-primitive-data-types-">Use Cases for Non-Primitive Data Types</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><a href="#operators-in-python">Operators in Python</a>
        <ul>
            <li><a href="#arithmetic-operators-">Arithmetic Operators</a></li>
            <li><a href="#comparison-operators">Comparison Operators</a></li>
        </ul>
    </li>
    <li><a href="#statements-in-python">Statements in Python</a>
        <ul>
            <li><a href="#assignment-statements">Assignment Statements</a> </li>
                
             <li><a href="#print-statement">Print Statement</a></li>
               
            
            <li><a href="#conditional-statements-if-elif-else-">Conditional Statements (if, elif, else)</a>
    
                    <li><a href="#loops-for-and-while-">Loops (for and while)</a>
                        <ul>
                            <li><a href="#for-loop-">For Loop</a></li>
                            <li><a href="#while-loop-">While Loop</a></li>
                        
                    </li></ul> </li>
                    <li><a href="#break-and-continue-statements">Break and Continue Statements</a></li>
                
           
        </ul>
    </li>
    <li><a href="#functions-in-python">Functions in Python</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
</ul>


### Prerequisites

Before you embark on this coding adventure, make sure you have the following:

* [Python installed](https://www.python.org/downloads/).
* A code editor like [VSCode](https://code.visualstudio.com/download), [Vim](https://www.vim.org/download.php), or [Sublime](https://www.sublimetext.com/3).

Now, let's explore the advantages of using Python.

## Why Learn Python?

If you're wondering why Python is an excellent choice for beginners and seasoned developers alike, here are some of the reasons:

* **Readability and Simplicity:** Python's clean syntax enhances code readability, reducing development time and making it beginner-friendly.
* **Versatility:** You can use Python to build a diverse range of applications, from web development to data science and AI. It also has an extensive standard library and many helpful third-party packages.
* **Community and Documentation:** Python has a robust community and comprehensive documentation that provides ample support, fostering the language's popularity and growth.
* **Cross-Platform Compatibility:** Ensures seamless execution across Windows, macOS, and Linux.
* **Extensive Libraries and Frameworks:** A rich ecosystem simplifies complex tasks, saving time and effort for developers.

Hopefully, you're intrigued by Python's perks – so let's delve into its key characteristics.

## Key Characteristics of Python

Understanding the key characteristics of Python will give you insights into its strengths and why it's a popular choice among developers:

* **Interpreted Language:** Your code is not directly translated by the target machine. Instead, a special program called the interpreter reads and executes the code, allowing for cross-platform execution of your code.
* **Dynamically Typed:** Dynamic typing eliminates the need for explicit data type declarations, enhancing simplicity and flexibility.
* **Object-Oriented:** Python supports object-oriented principles, promoting code modularity and reusability.
* **Indentation-based Syntax:** Indentation-based syntax enforces code readability and maintains a consistent coding style.
* **Memory Management:** Automatic memory management through garbage collection simplifies memory handling for developers.

## Practical Uses of Python

Python's versatility and readability make it suitable for a wide array of applications. Here are some practical uses:

* **Web Development:** Python, with frameworks like Django and Flask, powers back-end development for robust web applications.
* **Data Science and Machine Learning:** Widely used in data science, Python's libraries like NumPy and Pandas support data analysis and machine learning.
* **Automation and Scripting:** Python excels in automating tasks and scripting, simplifying repetitive operations.
* **AI and NLP:** Python, with libraries like TensorFlow, dominates in AI and natural language processing applications.
* **Game Development:** Python, combined with Pygame, facilitates 2D game development for hobbyists and indie developers.
* **Scientific Computing:** Python is a valuable tool in scientific computing, chosen by scientists and researchers for its extensive libraries.

Python is pre-installed in most Linux distributions. Follow [this article](https://www.datacamp.com/blog/how-to-install-python) on how to install Python on Windows and MacOS.

## How to Write "Hello, World" in Python

This is usually the first achievement when starting to code in any language: having your code say 'Hello world'. Open any code editor of your choice, and create a file named `project.py`. Inside the file, type the following:

```python
     print("Hello, World!")  
     
```

To run this code, open the command line interface (CLI). Follow [this article](https://www.freecodecamp.org/news/command-line-for-beginners/) to understand more about CLI.

Make sure to open the directory where the file is saved, and run the following:

```bash
 python3 project.py 
```

When you run this program, you'll see the timeless greeting displayed in your command line interface.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-01-30-11-59-12.png)
_hello world displayed in the CLI_

‌Congratulations! You've just executed your first Python script. Now that you've printed a simple message, let's dive deeper into Python.

## **Python Variables and Data Types**

The primary purpose of computers is to process data into useful information, for that to happen, the data needs to be stored in its memory. This is achieved using a programming language's variables and data types.

Data types in Python are particular kinds of data items, as defined by the value they can take. Variables, on the other hand, are like labeled containers that store this data. They enable you to manage and modify information using specific identifiers.

Data types are generally classified into two types:

### Primitive (Fundamental) Data Types:

Primitive data types represent simple values. These data types are the most basic and essential units used to store and manipulate information in a program. They translate directly into low-level machine code. 

Primitive data types include:

* **String (`str`):** Represents sequences of characters. Should be enclosed in quotes. Example: `"Hello, Python!"`
* **Integer (`int`):** Represents whole numbers without decimals. Example: `42`
* **Float (`float`):** Represents numbers with decimals. Example: `3.14`
* **Boolean (`bool`):** Represents either `True` or `False`.

#### Characteristics of Primitive Data Types:

* **Immutability:** Primitive data types are immutable, meaning their values cannot be changed after they are created. Any operation that appears to modify a primitive value creates a new value.
* **Direct Representation:** Each primitive data type directly corresponds to a specific low-level machine code representation.
* **Atomic Values:** Primitive data types represent individual, atomic values. They are not composed of other types or structures.

#### Use Cases for Primitive Data Types:

* Strings are used for text manipulation and representation.
* Integers and floats are essential for numerical calculations.
* Booleans are employed in logical operations and decision-making.

Let's see how these work by continuing to write some Python code.

Modify your `project.py` file to include the following:

```python
# String Example 
name = "John"
# Integer Example
age = 25 
# Float Example 
height = 1.75 
# Boolean Example
is_student = True
# Print variable values 
print("Name:", name) 
print("Age:", age) 
print("Height:", height)
print("Is student?", is_student)
```

In this snippet, you've introduced variables with different data types. Run the program and observe how Python handles these data types.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-01-30-12-02-11.png)
_primitive data types_

The output reveals the values assigned to the variables in the Python script. The `print` statements display the contents of the `name`, `age`, `height`, and `is_student` variables. 

### ‌‌Non-Primitive (Composite) Data Types in Python

Non-primitive data types are structures that can hold multiple values and are composed of other data types, including both primitive and other composite types. Unlike primitive data types, non-primitive types allow for more complex and structured representations of data.

Non-primitive data types include:

* **List (`list`):** Represents an ordered and mutable collection of values. Example: `fruits = ["apple", "banana", "cherry"]`
* **Tuple (`tuple`):** Represents an ordered and immutable collection of values. Example: `coordinates = (3, 7)`
* **Dictionary (`dict`):** Represents an unordered collection of key-value pairs. Example: `person = {"name": "Alice", "age": 25, "is_student": True}`

#### Characteristics of Non-Primitive Data Types:

* **Mutability:** Lists are mutable, meaning their elements can be modified after creation. Tuples, on the other hand, are immutable – their elements cannot be changed. Dictionaries are mutable – you can add, modify, or remove key-value pairs.
* **Collection of Values:** Non-primitive data types allow the grouping of multiple values into a single structure, enabling the creation of more sophisticated data representations.
* **Ordered (Lists and Tuples):** Lists and tuples maintain the order of elements, allowing for predictable indexing.
* **Key-Value Mapping (Dictionary):** Dictionaries map keys to values, providing a way to organize and retrieve data based on specific identifiers.

#### Use Cases for Non-Primitive Data Types:

* **Lists:** Useful when you need a collection that can be altered during the program's execution, such as maintaining a list of items that may change over time.
* **Tuples:** Suitable when you want to ensure that the data remains constant and cannot be accidentally modified. Often used for representing fixed sets of values.
* **Dictionaries:** Ideal for scenarios where data needs to be associated with specific labels or keys. They offer efficient data retrieval based on these identifiers.

Alright, continuing with our Python code – modify the `project.py` file as shown below:

```python
# List Example
fruits = ["apple", "banana", "cherry"]
print("List Example:", fruits)

# Tuple Example
coordinates = (3, 7)
print("Tuple Example:", coordinates)

# Dictionary Example
person = {"name": "Alice", "age": 25, "is_student": True}
print("Dictionary Example:", person)

```

Run the program to see how lists and tuples allow you to organize and store data. In this code snippet:

* The `fruits` variable is a list containing strings representing different fruits.
* The `coordinates` variable is a tuple with two integers representing coordinates.
* The `person` variable is a dictionary associating keys ("name," "age," "is_student") with corresponding values.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-01-31-11-19-39.png)
_non-primitive data types_

You can perform various operations on these structures, such as adding elements to a list or accessing individual items in a tuple.

Data types are crucial for several reasons:

* **Memory Allocation:** Different data types require different amounts of memory. Knowing the data type allows the computer to allocate the appropriate amount of memory for a variable.
* **Operations:** Each data type supports specific operations. For example, you can add two `integer` numbers, concatenate two `strings`, or compare two `boolean` values.
* **Error Prevention:** Using the wrong data type in an operation can lead to errors. Data types help prevent unintended consequences by enforcing rules on how different types can interact.

## Operators in Python

Operators in Python are symbols that perform operations on variables and values.   
An operand refers to the inputs or objects on which an operation is performed.

Let's explore some of the essential operators in Python:

### Arithmetic Operators:

Arithmetic operators are fundamental components of any programming language, allowing developers to perform basic mathematical operations on numerical values. 

In Python, several arithmetic operators enable you to carry out calculations efficiently. Let's explore these operators:

* Addition (+): Adds two operands.
* Subtraction (-): Subtracts the right operand from the left operand.
* Multiplication (*): Multiplies two operands.
* Division (/): Divides the left operand by the right operand (always returns a float).
* Modulus (%): Returns the remainder of the division of the left operand by the right operand.
* Exponentiation (**): Raises the left operand to the power of the right operand.

Modify your `project.py` file to include examples of these operators:

```python
 # Arithmetic Operators
 num1 = 10 
 num2 = 3 
 add_result = num1 + num2 
 sub_result = num1 - num2 
 mul_result = num1 * num2 
 div_result = num1 / num2 
 mod_result = num1 % num2 
 exp_result = num1 ** num2 
 print("Addition:", add_result) 
 print("Subtraction:", sub_result)
 print("Multiplication:", mul_result) 
 print("Division:", div_result) 
 print("Modulus:", mod_result) 
 print("Exponentiation:", exp_result)  
```

The code above initializes two variables, `num1` and `num2`, with the values `10` and `3` respectively, representing two numerical operands.

Then, arithmetic operations are performed using these operands:

* `add_result` stores the result of adding `num1` and `num2`.
* `sub_result` stores the result of subtracting `num2` from `num1`.
* `mul_result` stores the result of multiplying `num1` and `num2`.
* `div_result` stores the result of dividing `num1` by `num2`.
* `mod_result` stores the remainder of dividing `num1` by `num2`.
* `exp_result` stores the result of raising `num1` to the power of `num2`.

Finally, the results of these arithmetic operations are printed using `print()` statements, each labeled appropriately, such as "Addition:", "Subtraction:", and so on, followed by the corresponding result.

 Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/arithmetic.png)
_arithmetic operations_

### Comparison Operators

Comparison operators in Python are essential tools for evaluating and comparing values. They enable you to express conditions and make decisions based on the relationship between different values.  They return either `True` or `False` based on the comparison result.

Here are the common comparison operators:

* Equal to (==): Checks if two operands are equal.
* Not equal to (!=): Checks if two operands are not equal.
* Greater than (>): Checks if the left operand is greater than the right operand.
* Less than (<): Checks if the left operand is less than the right operand.
* Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
* Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.

Extend your `project.py` file to include examples of comparison operators:

```python
 # Comparison Operators 
 age = 25
 is_adult = age >= 18
 is_teenager = age >= 13 and age < 18
 print("Is adult?", is_adult)
 print("Is teenager?", is_teenager)       
```

The variable `age` is initialized with the value `25`, representing a person's age.

Then, the comparison operator `>=` is used to evaluate whether `age` is greater than or equal to `18`. The result of this comparison determines the boolean value stored in the variable `is_adult`. If the age is `18` or older, `is_adult` will be `True`, indicating adulthood.

Then the logical operator `and` is utilized to combine two comparison operations. The first comparison, `age >= 13`, checks if the age is `13` or older. The second comparison, `age < 18`, ensures the age is less than `18`. If both conditions are true, `is_teenager` will be `True`, signifying teenage years.

Finally, the results are printed using `print()` statements, indicating whether the person is classified as an adult (`True` or `False`) and whether they are identified as a teenager (`True` or `False`).

Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/is-adult.png)

## Statements in Python

Statements instruct the interpreter to perform specific actions or operations. These actions can range from simple assignments of values to variables to more complex control flow structures and iterations. 

Understanding different types of statements is essential for writing effective and expressive Python code.

### Assignment Statements

Assignment statements are the most basic type of statement in Python. They are used to assign values to variables, creating a named reference to data. 

Here's an example:

```python
x = 10 
name = "Alice" 
```

In this snippet, `x` is assigned the integer value `10`, and the `name` is assigned the string `"Alice"`. These assignments create variables that can be used throughout the program.

### Print Statement

The print statement is used to display output in the console. It is a crucial tool for debugging and providing information to users. Example:

```python
print("Hello, Python!")  
```

This code prints the string "Hello, Python!" to the console.

### Conditional Statements (if, elif, else)

Conditional statements are used when you want to execute different blocks of code based on certain conditions. 

Suppose you wanted to determine if a person has reached the legal age for drinking.  Modify the `project.py` file with the following code:

```python
# Conditional Statement Example 
age = 20
if age < 18:
    print("You are a minor.")
elif 18 <= age < 21:
    print("You are an adult, but not yet allowed to drink.")
else:
    print("You are a legal adult.")

```

In this example:

* The `if` statement checks if `age` is less than 18.
* The `elif` statement (shorthand for else if) checks if `age` is between 18 (inclusive) and 21 (exclusive).
* The `else` statement is executed if none of the above conditions are met.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/drinking.png)
_if else statement_

A person aged 20 is not allowed to drink.

### Loops (for and while) 

Loops are used to repeat a block of code multiple times. There are two main types of loops in Python: `for` loops and `while` loops.

#### For Loop:

A `for` loop is used when you know the number of iterations in advance. Suppose you had a list containing the names of fruits, and you wanted to print each fruit. In this case, a `for` loop is an ideal choice for iterating over the elements of the list. 

Here's an example using Python:

```python
# for loop Example 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

‌In this example, the `for` loop iterates over each element in the `fruits` list and prints each fruit.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/apple.png)
_list of fruits in the for loop_

#### While Loop:

A `while` statement is a control flow statement that allows you to execute a block of code repeatedly as long as a specified condition is true.  

Suppose you want to simulate counting until a certain threshold is reached. Modify your `project.py` and add the following code:

```python
# While Loop Example 
count = 0
while count < 5:
    print("Count:", count)
    count += 1

```

In this scenario, the `while` loop continues executing as long as the `count` variable is less than 5. The code inside the loop increments the count and prints the current count in each iteration. 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/count.png)
_output of while loop_

### Break and Continue Statements

Break and continue statements are used within loops.

* `break`: Exits the loop.
* `continue`: Skips the rest of the code inside the loop for the current iteration, then continues the loop.

 Examples:

```python
‌# Break Statement Example 
print("Output with 'break':")
for i in range(5):
    if i == 3:
        print(f"Encountered 'break' at i={i}") 
        break
    print(i)

# Continue Statement Example 
print("\nOutput with 'continue':")
for i in range(5):
    if i == 2:
        print(f"Skipped iteration with 'continue' at i={i}")
        continue
    print(i)

```

‌In the `break` example, the loop stops when `i` is equal to 3, and the numbers 0, 1, and 2 are printed. 

In the `continue` example, when `i` is equal to 2, the `continue` statement skips the `print(i)` statement for that iteration, resulting in the omission of the number 2 from the output.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/break1.png)
_break and continue statements output_

## Functions in Python

Functions are reusable blocks of code, enhancing modularity by enclosing functionality into separate, organized units. This approach helps avoid code duplication and significantly improves code readability. 

Inside the `project.py` file, write the following code:

```python
def greet():
    print("Hello, World!")

# Call the function to execute
greet()

```

The code above contains a simple Python function called `greet()`. When 'called' or 'invoked', this function prints "Hello, World!" to the console. It's a basic example illustrating how functions work in Python.

You can take this a step further by including parameters. Parameters serve as placeholders for values passed to a function during its invocation, allowing functions to accept input and perform operations based on that input.

Modify the previous example on `if elif else` statement to include functions:

```python
def check_age(age):
    if age < 18:
        print("You are a minor.")
    elif 18 <= age < 21:
        print("You are an adult, but not yet allowed to drink.")
    else:
        print("You are a legal adult.")

# Call the function with a specific age
check_age(20)


```

In this example, the `check_age` function takes an `age` parameter and performs the same conditional check as the original code. The function allows you to reuse this logic for different age values by simply calling the function with the desired age.

You can call `check_age` function with any age value, and it will print the appropriate message based on the age provided.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-02-07-13-03-23.png)
_functions_

## Conclusion

‌‌‌‌Embarking on your Python learning journey, this guide introduces the benefits of learning Python, its key characteristics, and practical use cases. 

Starting with the iconic "Hello, World!" and progressing through variables, data types, statements, and functions, you've gained some hands-on experience with basic Python. We also talked about primitive and non-primitive data types, conditional statements, and loops.

As your journey progresses, delve into advanced topics like object-oriented programming, file handling, and real-world projects. Armed with foundational knowledge, you can now embrace coding challenges that come your way. Stay curious, and relish the rewarding process of coding with Python. Happy coding!

‌‌

‌‌

