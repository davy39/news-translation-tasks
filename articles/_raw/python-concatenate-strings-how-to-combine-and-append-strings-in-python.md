---
title: Python Concatenate Strings – How to Combine and Append Strings in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-11T17:19:31.000Z'
originalURL: https://freecodecamp.org/news/python-concatenate-strings-how-to-combine-and-append-strings-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/join.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When you're learning a programming language, you're likely to come across\
  \ a data type called a string. A string usually contains a series of characters\
  \ nested in quotation marks that can be represented as a text. \nIn this article,\
  \ we will talk about ..."
---

When you're learning a programming language, you're likely to come across a data type called a string. A string usually contains a series of characters nested in quotation marks that can be represented as a text. 

In this article, we will talk about string concatenation in Python. This is the process of joining/adding one string to another. For example, the concatenation of "freeCode" and "Camp" is "freeCodeCamp".

String concatenation is important when working with two or more separate variables (strings) that are combined to form a much larger string. 

This also enables you have separate units of a string even after combining them, just in case you need to use one string variable somewhere else in your code and not the entire string.

## How to Concatenate Strings in Python

To concatenate string in Python, we use the `+` operator to append the strings to each other. Here is an example:

```python
x = "Happy"
y = "Coding"
z = x + y
print(z) 
#HappyCoding
```

In the code above, we created two variables (`x` and `y`) both containing strings – "Happy" and "Coding" – and a third variable (`z`) which combines the two variables we created initially.

We were able to combine the two variables by using the `+` operator. Our output after this was `HappyCoding`. If you were to reverse the order during concatenation by doing this: `z = y + x` then we would get `CodingHappy` printed to the console.

## How to Add Spaces Between Concatenated Strings

You might notice that there was no space between the variables when printed. Here's how we can add spaces between concatenated strings:

```python
x = "Happy"
y = "Coding"
z = x + " " + y
print(z) 
# Happy Coding
```

You'll notice that there is a space between the quotation marks. If you omit the space then the strings will still be closely joined together.

You can also add spaces at the end of a string when it is created and it will be applied when printed. Here's how you'd do that:

```python
x = "Happy "
y = "Coding"
z = x + y
print(z) 
#Happy Coding
```

## How to Create Multiple Copies of a String Using the `*` Operator

When we use the `*` operator on a string, depending on value passed, we create and concatenate (append) copies of the string. Here is an example:

```python
x = "Happy"
y = x * 3
print(y) 
# HappyHappyHappy
```

Using the `*` operator, we duplicated the value of the string "Happy" three times with the three printed values closely packed together. 

If we were to add a space at the end of the string, then the strings will be separated. That is: 

```
x = "Happy "
y = x * 3
print(y) 
# Happy Happy Happy
```

## Conclusion

In this article, we learned how to combine strings in Python through concatenation.

Thank you for reading and happy coding!

