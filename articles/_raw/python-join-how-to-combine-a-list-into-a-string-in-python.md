---
title: Python join() – How to Combine a List into a String in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-03T20:11:53.000Z'
originalURL: https://freecodecamp.org/news/python-join-how-to-combine-a-list-into-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-francesco-ungaro-96081.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Suchandra Datta\njoin() is one of the built-in string functions in Python\
  \ that lets us create a new string from a list of string elements with a user-defined\
  \ separator. \nToday we'll explore join() and learn about:\n\njoin() syntax\nhow\
  \ to use join() t..."
---

By Suchandra Datta

`join()` is one of the built-in string functions in Python that lets us create a new string from a list of string elements with a user-defined separator. 

Today we'll explore `join()` and learn about:

* `join()` syntax
* how to use `join()` to combine a list into a string
* how to combine tuples into a string with `join()`
* how to use `join()` with dictionaries
* when not to use `join()` 

## `join()` Syntax

```py
str.join(iterable)
```

* it requires only one input argument, an iterable. An iterable is any object which supports iteration, meaning it has defined the `__next__` and `__iter__` methods. Examples of iterables are lists, tuples, strings, dictionaries, and sets.
* `join()` is a built-in string function so it requires a string to invoke it
* it returns one output value, a string formed by combining the elements in the iterable with the string invoking it, acting as a separator

## How to Use `join()` to Combine a List into a String

Let's look at an example:

We create a string consisting of a single occurrence of the `|` character, like this:

```python
s = "|"
```

We can use the `dir` method to see what methods we have available to invoke using the `s` string object:

```python
dir(s)
```

Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-146.png)

Among the various attributes and method names, we can see the `join()` method:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-147.png)

Let's create a list of strings:

```python
country_names = ["Brazil", "Argentina", "Spain", "France"]
```

And now join the list elements into one string with the `|` as a separator:

```python
country_names = ["Brazil", "Argentina", "Spain", "France"]
s.join(country_names)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-148.png)

Here we see that `join()` returns a single string as output. The contents of the string variable invoking `join()` is the separator, separating the list items of the iterable `country_names` which forms the output. We can use any string we like as a separator like this:

```python
s = ","
s.join(country_names)
```

or this:

```python
s = "__WC__"
s.join(country_names)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-149.png)

Using `join()` with lists of strings has lots of useful applications. For instance, we can use it to remove extra spaces between words. Suppose we have a sentence like the below where there are multiple spaces. We can use `split()` which will split on whitespace to create a list of words:

```python
paragraph = "Argentina  wins   football   world cup 2022 in a nail biting final match that led to a \
spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most\
 memorable   matches."
step1 = paragraph.split()
print(step1)
```

Now we use `join()` using a single space to recreate the original sentence without the additional spaces in between:

```python
" ".join(step1)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-156.png)

## How to Combine Tuples into a String with `join()`

Tuples are one of the built-in data types in Python which doesn't allow modifications once they're created – they're immutable. Tuples are comma separated lists of items enclosed in () like this:

```python
t = ('quarter-final', 'semi-final', 'final')
```

We can combine tuple items together in the same way we were combining list items together using `join()`:

```python
",".join(t)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-151.png)

This is useful for cases where we need to use tuples – like storing large collections of items which need to be processed only once and then displaying the items in a comma-separated string.

## How to Use `join()` with Dictionaries

Dictionaries are a mapping type in Python where we specify key value pairs for storage. Let's say we have this nested dictionary

```python
d = { "event":
     {
        "world cup":{
            "sport":"Football",
            "info":{"year":"2022", "country":"Argentina"}
        }
     }
    }
```

We can use `join()` to extract a comma separated string with the keys and values like this:

```python
column_values = ",".join(d["event"]["world cup"]["info"].keys())
row_values = ",".join(d["event"]["world cup"]["info"].values())
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-152.png)

## When Not to Use `join()`

`join()` won't work if you try to:

* combine iterables with elements that aren't strings
* combine nested iterables 

Let's look at some examples.

### Iterables with elements that aren't strings

`join()` cannot be applied on sequences that contain items other than strings. So we won't be able to combine lists with numeric type elements. It would raise a TypeError like this:

```python
names_and_numbers = ["Tom", 1234, "Harry"]
",".join(names_and_numbers)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-153.png)

### Nested iterables

If we try to combine the values of a dictionary like this:

```python
nested = ["Tom", "Harry", ["Jack", "Jill"]]
",".join(nested)
```

We'll get a TypeError, as `join()` is expecting a list of strings but received a list of a list of strings.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-154.png)

For such cases, flatten the list like this:

```python
flatten = 
[ x for x in nested if isinstance(x, list)!=True] + \
[ e for each in nested for e in each if isinstance(each, list)==True]
```

Here, this:

```python
[ x for x in nested if isinstance(x, list)!=True] 
```

checks if each item in `nested` is a list. If not, it adds it to a new list. And this:

```python
[ e for each in nested for e in each if isinstance(each, list)==True]
```

creates a new 1D list element for any item in `nested` which is a list. Now we run `join()` like this:

```python
nested = ["Tom", "Harry", ["Jack", "Jill"]]
flatten = [ x for x in nested if isinstance(x, list)!=True] + \
[ e for each in nested for e in each if isinstance(each, list)==True]
",".join(flatten)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-155.png)

## Wrapping Up

In this article, we learnt how to use the `join()` method on iterables like lists, dictionaries, and tuples. We also learned what sort of use-cases we can apply it on and situations to watch out for where `join()` would not work. 

I hope you enjoyed this article and wish you a very happy and rejuvenating week ahead. 

