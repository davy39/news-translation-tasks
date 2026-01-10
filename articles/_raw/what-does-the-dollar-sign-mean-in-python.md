---
title: What Does $ Mean in Python? Operator Meaning + String Formatting Examples
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-18T16:39:34.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-dollar-sign-mean-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/what-does-the-dollar-sign-mean-in-python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Operators are special symbols you can use to perform different operations\
  \ on variables (operands) in programming. \nPython has different operators like\
  \ arithmetic operators, assignment operators, logical operators, boolean operators,\
  \ comparison operat..."
---

Operators are special symbols you can use to perform different operations on variables (operands) in programming. 

Python has different operators like arithmetic operators, assignment operators, logical operators, boolean operators, comparison operators, bitwise operators, and so on. 

Although you'll not come across the dollar sign ($) operator when learning about operators in Python, you can use it to format strings using the string template class.

In this article, you'll learn how to format strings in Python using the following methods:

* The string template class.
* The `%` operator.
* The `format()` method.
* Using f-strings. 

## How to Format Strings in Python Using the String Template Class

The string template class in Python lets you substitute or inject variable values within strings. 

To make use of the template class, you must first import it from the `string` module. That is:

```python
from string import Template
```

Here's how to use it to format strings: 

```python
from string import Template

template_string = Template("My name is $name! I create content on $language")

output = template_string.substitute(name="Ihechikara", language="Python")

print(output) # My name is Ihechikara! I create content on Python
```

In the example above, we created variable called `template_string` to hold the string: "My name is $name! I create content on $language". 

The string was passed as a parameter to the template class: `Template("My name is $name! I create content on $language")`. 

You'll notice that, within the string, some character have the `$` operator before them – `$name` and `$language`. These are placeholders that can be assigned values. 

In the next line, we substituted values for those placeholders: `template_string.substitute(name="Ihechikara", language="Python")`. 

In the output, we had these substitute values replace the placeholders. 

From "My name is $name! I create content on $language" to "My name is Ihechikara! I create content on Python". 

## How to Format Strings in Python Using the `%` Operator

The `%` operator has different placeholders used for formatting strings. You can see all of them [here](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting). 

Here's an example that makes use of the `%s` and `%d` placeholders:

```python
name = "John"
age = 80
print("%s is %d years old" %(name, age)) # John is 80 years old

```

In the example above, we created two variables — `name` and `age`. 

To pass these variables into the string, we used the `%s` to substitute the string (`name`), and the `%d` placeholder to substitute the integer (`age`). That is:

```python
"%s is %d years old"
```

To make sure the variables are substituted into those positions, we provided the variable names in parenthesis: `%(name, age)`. 

Joining them together, we have this: 

```python
"%s is %d years old" %(name, age)
```

So the `%s` placeholder will look for any string stored within the parenthesis and substitute it while the `%d` placeholder will do the same for any integer value. 

## How to Format Strings in Python Using the `format()` Method

The `format()` method is pretty similar to using the `%` operator. 

Instead of using placeholders, you use curly brackets `{}` to substitute the parameters of the `format()` method. 

Here's an example:

```python
name = "John"
age = 80
print("{} is {} years old".format(name, age)) # John is 80 years old

```

In the example above, the curly brackets will be replaced by the parameters of the `format()` method — `format(name, age)`. 

From "{} is {} years old" to "John is 80 years old". 

## How to Format Strings in Python Using F-strings

The f-string method also makes use of curly brackets. In the last section, we had to attach the `format()` method using dot notation. 

With f-strings, you can pass the variable names directly into the curly brackets: 

```python
name = "John"
age = 80
print(f"{name} is {age} years old") # John is 80 years old
```

To use f-strings, just place an `f` before the opening quotation mark of the string. This allows you to pass in variables directly into the string.

You can even perform arithmetic operations within the string: 

```python
num1 = 20
num2 = 80
print(f"{num1} + {num2} = {num1 + num2}") # 20 + 80 = 100
```

## Summary

In this article, we talked about the different methods used for formatting strings in Python. 

We started by looking at the string template class which uses the `$` operator to format strings. 

We then saw how other methods like the `%` operator, `format()` method, and f-strings can be used to format strings in Python. 

Happy coding! I also write about Python on [my blog](https://ihechikara.com/). 

