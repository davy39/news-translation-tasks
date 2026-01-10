---
title: 'Truthy and Falsy Values in Python: A Detailed Introduction'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-01-22T12:22:00.000Z'
originalURL: https://freecodecamp.org/news/truthy-and-falsy-values-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Truthy-and-Falsy-Values.png
tags:
- name: Computer Science
  slug: computer-science
- name: learning to code
  slug: learning-to-code
- name: programming languages
  slug: programming-languages
- name: Python
  slug: python
seo_title: null
seo_desc: 'Welcome

  In this article, you will learn:


  What truthy and falsy values are.

  What makes a value truthy or falsy.

  How to use the bool() function to determine if a value is truthy or falsy.

  How to make objects from user-defined classes truthy or falsy u...'
---

## Welcome

In this article, you will learn:

* What truthy and falsy values are.
* What makes a value truthy or falsy.
* How to use the `bool()` function to determine if a value is truthy or falsy.
* How to make objects from user-defined classes truthy or falsy using the special method `__bool __`.

**Let's begin! ✨**

## 🔹 Truth Values vs. Truthy and Falsy Values

Let me introduce you to these concepts by comparing them with the values `True` and `False` that we typically work with. 

Expressions with operands and operators evaluate to either `True` or `False` and they can be used in an `if` or `while` condition to determine if a code block should run.

Here we have an example:

```python
# Expression 5 < 3
>>> if 5 < 3:
	print("True")
else:
	print("False")

# Output
False
```

In this example, everything is working as we expected because we used an expression with two operands and an operator `5 < 3`.

**But what do you think will happen if we try to run this code?**

```python
>>> a = 5

>>> if a:
	print(a)
```

Notice that now we don't have a typical expression next to the `if` keyword, only a variable:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-3.png)

Surprisingly, the output is:

```python
5
```

If we change the value of `a` to zero, like this:

```python
>>> a = 0

>>> if a:
	print(a)
```

There is no output.

I'm sure that you must be asking this right now: **what made the code run successfully?** 

The variable `a` is not a typical expression. It doesn't have operators and operands, so why did it evaluate to `True` or `False` depending on its value?

The answer lies on the concept of Truthy and Falsy values, which are not truth values themselves, but they evaluate to either `True` or `False`. 

## 🔸Truthy and Falsy Values

In Python, individual **values** can evaluate to either `True` or `False`. They do not necessarily have to be part of a larger expression to evaluate to a truth value because they already have one that has been determined by the rules of the Python language.

The basic rules are:

* Values that evaluate to **`False`** are considered `**Falsy**`. 
* Values that evaluate to **`True`** are considered `**Truthy**`. 

According to the [Python Documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing):

> Any object can be tested for truth value, for use in an [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) or [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) condition or as operand of the Boolean operations below (and, or, not).

### 🔹 Boolean Context

When we use a value as part of a larger expression, or as an `if` or `while` condition, we are using it in a **boolean context**. 

You can think of a boolean context as a particular "part" of your code that requires a value to be either `True` or `False` to make sense. 

For example, (see below) the condition after the `if` keyword or after the `while` keyword has to evaluate to either `True` or `False`:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-1.png)

💡 **Tip:** The value can be stored in a variable. We can write the name of the variable after the `if` or `while` keyword instead of the value itself. This will provide the same functionality.

Now that you know what truthy and falsy values are and how they work in a boolean context, let's see some real examples of truthy and falsy values.

### 🔸 Falsy Values

**Sequences and Collections:**

* Empty lists `[]`
* Empty tuples `()`
* Empty dictionaries `{}`
* Empty sets `set()`
* Empty strings `""`
* Empty ranges `range(0)`

**Numbers**

* Zero of any numeric type. 
* Integer: `0`
* Float: `0.0`
* Complex: `0j`

**Constants**

* `None`
* `False`

Falsy values were the reason why there was no output in our initial example when the value of `a` was zero.

The value `0` is falsy, so the `if` condition will be `False` and the conditional will not run in this example:

```python
>>> a = 0
>>> if a:
	print(a)

# No Output	
```

### 🔹 Truthy Values

According to the [Python Documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing):

> By default, an object is considered **true**.

**Truthy values include:**

* Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
* Numeric values that are not zero.
* `True`

This is why the value of `a` was printed in our initial example because its value was 5 (a truthy value):

```python
>>> a = 5

>>> if a:
	print(a)
    
 # Output
 5
```

### 🔸 The Built-in bool() Function

You can check if a value is either truthy or falsy with the built-in `bool()` function. 

According to the [Python Documentation](https://docs.python.org/3/library/functions.html#bool), this function:

> Returns a Boolean value, i.e. one of `True` or `False`. _x (the argument)_ is converted using the standard truth testing procedure.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-2.png)

You only need to pass the value as the argument, like this:

```python
>>> bool(5)
True
>>> bool(0)
False
>>> bool([])
False
>>> bool({5, 5})
True
>>> bool(-5)
True
>>> bool(0.0)
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(range(0))
False
>>> bool(set())
False
>>> bool({5, 6, 2, 5})
True
```

💡 **Tip:** You can also pass a variable as the argument to test if its value is truthy or falsy.

### 🔹 Real Examples

One of the advantages of using truthy and falsy values is that they can help you make your code more concise and readable. Here we have two real examples.

**Example:**   
We have this function `print_even()` that takes as an argument a list or tuple that contains numbers and only prints the values that are even. If the argument is empty, it prints a descriptive message:

```python
def print_even(data):
	if len(data) > 0:
		for value in data:
			if value % 2 == 0:
				print(value)
 	else:
 		print("The argument cannot be empty")
```

Notice this line:

```python
if len(data) > 0:
```

We can make the condition much more concise with truthy and falsy values:

```python
if data:
```

If the list is empty, `data` will evaluate to `False`. If it's not empty, it will evaluate to `True`. We get the same functionality with more concise code.

This would be our final function:

```python
def print_even(data):
	if data:
		for value in data:
			if value % 2 == 0:
				print(value)
 	else:
 		print("The argument cannot be empty")
```

**Example:**   
We could also use truthy and falsy values to raise an exception (error) when the argument passed to a function is not valid.

```python
>>> def print_even(data):

	if not data:
		raise ValueError("The argument data cannot be empty")

	for value in data:
		if value % 2 == 0:
			print(value)
```

In this case, by using `not data` as the condition of the `if` statement, we are getting the opposite truth value of `data` for the `if` condition. 

Let's analyze `not data` in more detail:

If `data` is empty:

* It will be a falsy value, so `data` will evaluate to `False`.
* `not data` will be equivalent to `not False`, which is `True`.
* The condition will be `True`. 
* The exception will be raised.

If `data` is not empty:

* It will be a truthy value, so it will evaluate to `True`. 
* `not data` will be equivalent to `not True`, which is `False` .
* The condition will be `False`. 
* The exception will not be raised.

## 🔸 Making Custom Objects Truthy and Falsy Values

If you are familiar with classes and Object-Oriented Programming, you can add a special method to your classes to make your objects act like truthy and falsy values.

### __bool __()

With the special method `__bool__()`, you can set a "customized" condition that will determine when an object of your class will evaluate to `True` or `False`. 

According to the [Python Documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing):

> By default, an object is considered true unless its class defines either a [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__) method that returns `False` or a [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__) method that returns zero, when called with the object.

For example, if we have this very simple class:

```python
>>> class Account:
	
	def __init__(self, balance):
		self.balance = balance
```

You can see that no special methods are defined, so all the objects that you create from this class will always evaluate to `True`:

```python
>>> account1 = Account(500)
>>> bool(account1)
True
>>> account2 = Account(0)
>>> bool(account2)
True
```

We can customize this behavior by adding the special method [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__):

```python
>>> class Account:
	def __init__(self, balance):
		self.balance = balance
		
	def __bool__(self):
		return self.balance > 0
```

Now, if the account balance is greater than zero, the object will evaluate to `True`. Otherwise, if the account balance is zero, the object will evaluate to `False`. 

```python
>>> account1 = Account(500)
>>> bool(account1)
True
>>> account2 = Account(0)
>>> bool(account2)
False
```

💡 **Tip:** If `[__bool__()](https://docs.python.org/3/reference/datamodel.html#object.__bool__)` is not defined in the class but the `__len__()` method is, the value returned by this method will determine if the object is truthy or falsy.

## 🔹 In Summary 

* Truthy values are values that evaluate to `True` in a boolean context.
* Falsy values are values that evaluate to `False` in a boolean context.
* Falsy values include empty sequences (lists, tuples, strings, dictionaries, sets), zero in every numeric type, `None`, and `False`.
* Truthy values include non-empty sequences, numbers (except `0` in every numeric type), and basically every value that is not falsy. 
* They can be used to make your code more concise. 

**I really hope you liked my article and found it helpful.** Now you can work with truthy and falsy values in your Python projects. [Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

