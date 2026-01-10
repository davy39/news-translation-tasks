---
title: Python String Methods Tutorial – How to Use find() and replace() on Python
  Strings
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-09-01T15:39:30.000Z'
originalURL: https://freecodecamp.org/news/python-string-methods-tutorial-how-to-use-find-and-replace-on-python-strings
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/find---and-replace----1--1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When working with strings in Python, you may need to search through strings\
  \ for a pattern, or even replace parts of strings with another substring. \nPython\
  \ has the useful string methods find() and replace() that help us perform these\
  \ string processin..."
---

When working with strings in Python, you may need to search through strings for a pattern, or even replace parts of strings with another substring. 

Python has the useful string methods `find()` and `replace()` that help us perform these string processing tasks. 

In this tutorial, we'll learn about these two string methods with example code.

## Immutability of Python Strings

Strings in Python are _immutable_. Therefore, we cannot modify strings _in place_. 

> Strings are Python iterables that follow zero-indexing. The valid indices for a string of length `n` are `0,1,2,..,(n-1)`.  
>   
> We can also use _negative-indexing_, where the last element is at index `-1`, the second-to-last element is at index `-2` and so on.

For example, we have `my_string` that holds the string `"writer"`. Let's try to change this to `"writes"` by setting the last character to `"s"`.

```python
my_string = "writer"

```

Let's try assigning the last character to the letter `"s"` as shown below. By negative-indexing, we know that the index of the last character in `my_string` is `-1`.

```python
my_string[-1]="s"

# Output
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-670491032ba6> in <module>()
      1 my_string = "writer"
----> 2 my_string[-1]="s"

TypeError: 'str' object does not support item assignment
```

As shown in the code snippet above, we get a `TypeError`. This is because string object is _immutable_, and the assignment that we tried to perform is invalid. 

However, we may often need to modify strings. And string methods help us do it with ease. 

> String methods operate on _existing_ strings and _return new_ modified strings. The existing string is _not_ modified.

Let's head over to the next section to learn about the `find()` and `replace()` methods.

## How to Use find() to Search for Patterns in Python Strings

You can use Python's  `find()` method to search through a string for a pattern. The general syntax is shown below.

```
<this_string>.find(<this_pattern>)
```

The input string that we'd like to search through is denoted by the placeholder `this_string`. The pattern that we'd like to search for is given by the placeholder `this_pattern`.

Let's now parse the above syntax.

* The `find()` method searches through `this_string` for the occurrence of `this_pattern`.
* If `this_pattern` is present, it returns the starting index of the _first_ occurrence of `this_pattern`.
* If `this_pattern` does not occur in `this_string`, it returns `-1`.

▶ Let's look at some examples.

### Python find() Method Examples

Let's take an example string `"I enjoy coding in Python!"`.

```python
my_string = "I enjoy coding in Python!"
my_string.find("Python")

# Output
18
```

In the above example, we tried searching for `"Python"` in `"my_string"`. The `find()` method returned `18`, the starting index of the pattern `"Python"`. 

To verify if the returned index is correct, we can check  if `my_string[18]=="P"` evaluates to `True`.

▶ Now, we'll try searching for a substring that's not present in our string.

```python
my_string.find("JavaScript")

# Output
-1
```

In this example, we tried searching for `"JavaScript"` that isn't present in our string. The `find()` method has returned `-1`, as discussed earlier.

## How to Use find() to Search for Patterns in Python Substrings

We can also use the `find()` method to search for a pattern in a certain _substring_ or _slice_ of a string, instead of the whole string. 

In this case, the `find()` method call takes the following form:

```
<this_string>.find(<this_pattern>, <start_index>,<end_index>)
```

This works very similarly to the previously discussed syntax. 

> The only difference is that the search for the pattern is not over the entire string. It's only over a _slice_ of the string specified by `start_index:end_index`.

## How to Use index() to Search for Patterns in Python Strings

To search for an occurrence of a pattern in a string, we might as well use the `index()` method. The method call takes the syntax shown below.

```
<this_string>.index(<this_pattern>)
```

The `index()` method's working is very similar to that of the `find()` method. 

* If `this_pattern` is present in `this_string`, the `index()` method returns the starting index of the _first_ occurrence of `this_pattern`.
* However, it raises a `ValueError` if `this_pattern` is not found in `this_string`.

▶ Time for examples.

### Python index() Method Examples

Let's use the string `my_string = "I enjoy coding in Python!"` from our previous example.

```python
my_string.index("Python")

# Output
18

```

In this case, the output is identical to that of the `find()` method.

If we search for a substring that's not present in our string, the `index()` method raises a `ValueError`. This is shown in the code snippet below. 

```
my_string.index("JavaScript")

# Output
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-4-377f7c374e16> in <module>()
----> 1 my_string.index("JavaScript")

ValueError: substring not found
```

In the next section, we'll learn how to find and replace patterns in strings.

## How to Use replace() to Find and Replace Patterns in Python Strings

If you need to search through a string for a pattern, and replace it with another pattern, you can use the `replace()` method. The general syntax is shown below:

```
<this_string>.replace(<this>,<with_this>)
```

We'll now parse this syntax.

* The `replace()` method searches through `this_string` for `this` pattern.
* If `this` pattern is present, it returns a new string where _all_ occurrences of `this` pattern are replaced with the pattern specified by the `with_this` argument.
* If `this` pattern is not found in `this_string`, the string returned is the same as `this_string`.

> What if you'd like to replace only a certain number of occurrences instead of all occurrences of the pattern?

In that case, you can add an _optional_ argument in the method call that specifies how many occurrences of the pattern you'd like to replace.

```
<this_string>.replace(<this>,<with_this>, n_occurrences)
```

In the syntax shown above, `n_occurrences` ensures that only the first `n` occurrences of the pattern are replaced in the returned string.

▶ Let's look at some examples to understand how the `replace()` function works.

### Python replace() Method Examples

Let's now redefine `my_string` to be the following:

```
I enjoy coding in C++.
C++ is easy to learn.
I've been coding in C++ for 2 years now.:)
```

This is shown in the code snippet below:

```python
my_string = "I enjoy coding in C++.\nC++ is easy to learn.\nI've been coding in C++ for 2 years now.:)"


```

Let's now replace all occurrences of `"C++"` with `"Python"`, like this:

```python
my_string.replace("C++","Python")

# Output
'I enjoy coding in Python.\nPython is easy to learn.\nI've been coding in Python for 2 years now.:)'
```

As the `replace()` method returns a string, we see the `\n` characters in the output. For the `\n` character to introduce line breaks, we can print out the string as shown below:

```python
print(my_string.replace("C++","Python"))


# Output
I enjoy coding in Python.
Python is easy to learn.
I've been coding in Python for 2 years now.:)
```

In the above example, we see that all occurrences of `"C++"` have been replaced with `"Python"`.

▶ Now, we'll use the additional `n_occurrences` argument as well. 

The following code returns a string where the first two occurrence of `"C++"` are replaced with `"Python"`.

```python
print(my_string.replace("C++","Python",2))

# Output
I enjoy coding in Python.
Python is easy to learn.
I've been coding in C++ for 2 years now.:)
```

The following code returns a string where only the first occurrence of `"C++"` is replaced with `"Python"`:

```python
print(my_string.replace("C++","Python",1))

# Output
I enjoy coding in Python.
C++ is easy to learn.
I've been coding in C++ for 2 years now.:)
```

▶ Now, we try replacing a substring `"JavaScript"` that doesn't exist in `my_string`. Therefore, the returned string is same as `my_string`.

```python
print(my_string.replace("JavaScript","Python"))

# Output
I enjoy coding in C++.
C++ is easy to learn.
I've been coding in C++ for 2 years now.:)
```

## Conclusion

In this tutorial, we learned the following:

* How to search through strings in Python using the `find()` and the `index()` methods, and
* How to find and replace patterns or substrings using the `replace()` method

Hope you enjoyed this tutorial.

See you all soon in another post. Until then, happy learning!

