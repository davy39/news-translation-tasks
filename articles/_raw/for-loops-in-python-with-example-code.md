---
title: For Loops in Python – For Loop Syntax Example
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-01-18T17:25:16.000Z'
originalURL: https://freecodecamp.org/news/for-loops-in-python-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-106155.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'While coding in Python, you may need to repeat the same code several times.

  Writing the same lines of code again and again repeatedly throughout your program
  is considered a bad practice in programming – this is where loops come in handy.

  With loops,...'
---

While coding in Python, you may need to repeat the same code several times.

Writing the same lines of code again and again repeatedly throughout your program is considered a bad practice in programming – this is where loops come in handy.

With loops, you can execute a sequence of instructions over and over again for a set pre-determined number of times until a specific condition is met.

Using loops in your program will help you save time, minimize errors, and stop repeating yourself.

There are two types of loops in Python:

- `for` loops
- `while` loops.

In this article, you will learn all about `for` loops. 

If you want to also learn about `while` loops, you can check out [this other article I've written](https://www.freecodecamp.org/news/while-loops-in-python-while-true-loop-statement-example/) on the topic.

Let's get into it!

## What Is a `for` Loop in Python?

You can use a `for` loop to iterate over an iterable object a number of times.

An iterable object in Python is any object that can be used as a sequence and looped over.

There are many iterable objects in Python, with some of the most common ones being:

- [lists](https://www.freecodecamp.org/news/create-a-list-in-python-lists-in-python-syntax/)
- [tuples](https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/)
- [dictionaries](https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/) 
- [sets](https://www.freecodecamp.org/news/python-set-how-to-create-sets-in-python/) 
- and [strings](https://www.freecodecamp.org/news/python-string-manipulation-handbook/)

The `for` loop iterates over each item in the sequence in order.

And it executes the same block of code for every item.

Because of this behavior, the `for` loop is helpful when:

- You know the number of times you want to execute a block of code.
- You want to execute the same code for each item in a given sequence.

The main difference between `for` loops and `while` loops is that:

- The `for` loop carries out the instructions a set number of times.
- The `while` loop executes the same action multiple times until a condition is met.
 
### Syntax Breakdown of a `for` Loop in Python

If you have worked with other programming languages, you will notice that a `for` loop in Python looks different from `for` loops in other languages.

For example, in JavaScript, the general syntax of a `for` loop looks like this:

```javascript
for (let i = 0; i < 5; i++) {
  console.log('Hello World');
  }
```

- There is an initialization, `i = 0`, which acts as the starting point.
- A condition that needs to be met, `i < 5`, for the loop to continue to run.
- An increment operator, `i++`.
- Curly braces and the body of the `for` loop that contains the action to take.

A `for` loop in Python has a shorter, and a more readable and intuitive syntax.

The general syntax for a `for` loop in Python looks like this:

```python
for placeholder_variable in sequence:
    # code that does something
```

Let's break it down:

- To start the `for` loop, you first have to use the `for` keyword.
- The `placeholder_variable` is an arbitrary variable. It iterates over the sequence and points to each item on each iteration, one after the other. The variable could have almost any name - it doesn't have to have a specific name. 
- Following the `placeholder_variable`, you then use the `in` keyword, which tells the `placeholder_variable` to loop over the elements within the sequence.
- The `sequence` can be a Python list, tuple, dictionary, set, string, or any other kind of iterator. Make sure you don't forget the add the colon, `:` at the end!
- Next, you add a new line and need to add one level of indentation. One level of indentation in Python is `4` spaces with the spacebar.
- Lastly, you need to add the body of the `for` loop. Here you specify the action you want to perform on each item in the sequence.

## How to Loop Over a String Using a `for` Loop in Python

As mentioned earlier, strings are iterable. They are a sequence of characters, meaning you can iterate over them, character by character.

Let's take the following example:

```python
for character in "Python":
  print(character)

# output

# P
# y
# t
# h
# o
# n
```

In the example above, I looped over the string `Python` and printed its individual letters to the console.

You would get the same result if you stored the string in a variable like so:

```python
fave_language = "Python"

for character in fave_language:
  print(character)
  
# output

# P
# y
# t
# h
# o
# n
```

## How to Loop Over a List Using a `for` Loop in Python

Say you have a  list of programming languages and want to iterate through it and print each item in the sequence until you reach the end:

```python
programming_languages = ["Python", "JavaScript", "Java", "C++"]

# iterate over each item in the list
for language in programming_languages:
  print(language)


# output

# Python
# JavaScript
# Java
# C++
```

As mentioned earlier, the `iterator_variable` can be called almost anything – in this case, I named it `language`.

This `language` variable refers to each entry in the sequence.

The `in` keyword, when used with a `for` loop, indicates that it iterates over every item in the sequence.

On the first iteration of the loop, `language` points to the first item in the list, `Python`.

The code statements inside the body of the loop get executed, so the `Python` gets printed to the console.

On the second iteration, the variable gets updated and points to the second item, `JavaScript`. It executes the same code statements in the body of the loop.

The same procedure happens for all items in the list until the loop reaches the end and every item has been iterated over.

## How to Loop Over a Tuple Using a `for` Loop in Python

Let's try iterating over all the items inside of a tuple.

```python
my_info = ("John", "Doe", 26, "Software Engineer")

for data in my_info:
  print(data)
  
# output

# John
# Doe
# 26
# Software Engineer
```

As you see, the process for using a `for` loop with tuples is the same as using a `for` loop with lists.

## How to Loop Over a Dictionary Using a `for` Loop in Python

Now, let's take a dictionary and iterate over the key-value pairs:

```python
my_info = {
  'name':'John Doe',
  'job title':'software engineer',
  'country':'USA'
}

for info in my_info:
  print(info)

# name
# job title
# country
```

When I use the same syntax I used for strings, lists, tuples, and sets with a dictionary, I end up with only the keys.
 
To loop over key and value pairs in a dictionary, you need to do what is called [tuple unpacking](https://forum.freecodecamp.org/t/the-ultimate-guide-to-python-tuples-python-data-structure-tutorial-with-code-examples/19165) by specifying two variables.

You will also need to use the `.items()` method to loop over both the keys and values:

```python
my_info = {
  'name':'John Doe',
  'job title':'software engineer',
  'country':'USA'
}

for key,value in my_info.items():
  print(key,":",value)

# output

# name : John Doe
# job title : software engineer
# country : USA
```

But what happens when you don't use the `.items()` method?

```python
my_info = {
  'name':'John Doe',
  'job title':'software engineer',
  'country':'USA'
}

for key,value in my_info:
  print(key,":",value)


# output

# Traceback (most recent call last):
#  File "main.py", line 7, in <module>
#    for key,value in my_info:
# ValueError: too many values to unpack (expected 2)
```

You get a `ValueError` since Python expects key and value pairs. In Python, keys and values are not separate – they go hand in hand. 

## How to Write a `break` Statement in a `for` Loop in Python

By default, a `for` loop in Python will loop through the entire iterable object until it reaches the end.

However, there may be times when you want to have more control over the flow of the `for` loop.

For example, you may want to exit the loop prematurely if a specific condition is met.

To achieve this, you can use the `break` statement.

Let's take the following example:

```python
programming_languages = ["Python", "JavaScript", "Java", "C++"]

for language in programming_languages:
  print(language)
  if language == "Java":
    break

# output

# Python
# JavaScript
# Java
```

In the example above, I want to exit the loop when the variable `language` points to the list item `"Java"`.

When Python sees the `break` keyword, it stops executing the loop, and any code that comes after the statement doesn't run.

As you see from the output of the code, `"Java"` is printed to the console, and the loop gets terminated.

If you wanted to exit the loop when the variable `language` points to `"Java"` but not print the value to the console, then you would write the following:

```python
programming_languages = ["Python", "JavaScript", "Java", "C++"]

for language in programming_languages:
  if language == "Java":
    break
  print(language)
  
# output

# Python
# JavaScript
```

## How to Write a `continue` Statement in a `for` Loop in Python

What if you want to skip a particular item?

The `continue` statement skips the execution of the body of the loop when a condition is met.

Let's take the following example:

```python
programming_languages = ["Python", "JavaScript", "Java", "C++"]


for language in programming_languages:
  if language == "Java":
    continue
  print(language)

# output

# Python
# JavaScript
# C++
```

In the example above, I wanted to skip `"Java"` from my list.

I specified that if the `language` variable points to `"Java"`, Python should stop and skip the execution at that point and continue to the next item on the list until it reaches the end.

The difference between the `break` and `continue` statements is that the `break` statement ends the loop altogether. 

On the other hand, the `continue` statement stops the current iteration at a specific point and moves on to the next item of the iterable object – it does not exit the loop entirely.

## How to Use the `range()` Function in a `for` Loop in Python

If you want to loop through a set of code a specified number of times, you can use Python's built-in `range()` function.

By default, the `range()` function returns a sequence of numbers starting from `0`, incrementing by one, and ending at a number you specify.

The syntax for this looks like this:

```python
range(end)
```

The `end` argument is required.

Let's see the following example:

```python
for i in range(4):
  print(i)

# output

# 0
# 1
# 2
# 3
```

In this example, I specified a `range(4)`.

It means the function will start counting from `0`, increment by `1` on each iteration, and end at `3`.

Keep in mind that the range you specify is not inclusive! So, a `range(4)` will end at `3` and not `4`.

So, it will include the values of `0` to `3` and not `0` to `4`.

What if you want to iterate through a range of two numbers you specify and don't want to start from `0`?

You can pass a second optional `start` argument to specify the starting number.

The syntax for this looks like this:

```
range(start, end)
```

If you want a range of values from `10` inclusive to `20` inclusive, you write a range of `range(10,21)`, like so:

```python
for i in range(10,21):
  print(i)
  
# output

# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
```

Again, `range(10,21)` does not include `21`.

Lastly, if you don't want the default increment to be `1`, you can specify a third optional parameter, the `step` parameter.

The syntax for this looks like this:

```
range(start, end, step)
```

Something to note is that `step` can be either a negative or positive number, but it cannot be `0`.

Let's take the following example:

```python
for i in range(10,21,2):
  print(i)
  
# output

# 10
# 12
# 14
# 16
# 18
# 20
```

In this example, I wanted to include the values `10` to `20` and increment by `2`.

I achieved this by specifying an increment value of `2`.

Let's take another example.

Say you have a list of items and want to do something to the items that depend on how long the list is. 

For that, you could use `range()` and pass the length of your list as an argument to the function.

To calculate the length of a list, use the `len()` function.

```python
programming_languages = ["Python", "JavaScript", "Java", "C++"]

programming_languages_length = len(programming_languages)

for languages in range(programming_languages_length):
  print("Hello World")
  
# output

# Hello World
# Hello World
# Hello World
# Hello World
```

## Conclusion

Hopefully this article helped you understand how to use `for` loops in Python.

You learned how to write a `for` loop to iterate over strings, lists, tuples, and dictionaries.

You also saw how to use the `break` and `continue` statements to control the flow of the `for` loop.

Lastly, you saw how to specify a range of numbers to use in your `for` loop with the `range()` function.

Thank you for reading, and happy coding!


