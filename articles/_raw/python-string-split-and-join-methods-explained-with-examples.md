---
title: Python String split() and join() Methods – Explained with Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-18T22:40:12.000Z'
originalURL: https://freecodecamp.org/news/python-string-split-and-join-methods-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/split-join.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When working with strings in Python, you may have to split a string into
  substrings. Or you might need to join together smaller chunks to form a string.
  Python''s split() and join() string methods help you do these tasks easily.

  In this tutorial, you''...'
---

When working with strings in Python, you may have to split a string into substrings. Or you might need to join together smaller chunks to form a string. Python's `split()` and `join()` string methods help you do these tasks easily.

In this tutorial, you'll learn about the `split()` and `join()` string methods with plenty of example code.

As strings in Python are immutable, you can call methods on them without modifying the original strings. Let's get started.

## Python `split()` Method Syntax

When you need to split a string into substrings, you can use the `split()` method. 

The `split()` method acts on a string and _returns_ a list of substrings. The syntax is:

```python
<string>.split(sep,maxsplit)
```

In the above syntax:

* `<string>` is any valid Python string,
* `sep` is the separator that you'd like to split on. It should be specified as a _string_.

> For example, if you'd like to split `<string>` on the occurrence of a comma, you can set `sep = ","`.

* `sep` is an _optional_ argument. By default, this method splits strings on _whitespaces_. 
* `maxsplit` is an _optional_ argument indicating the number of times you'd like to split `<string>`. 
* `maxsplit` has a default value of `-1`, which splits the string on _all_ occurrences of `sep`.

> If you'd like to split `<string>` on the occurrence of the _first_ comma, you can set `maxsplit = 1`. 

And setting `maxsplit = 1` will leave you with two chunks – one with the section of `<string>` before the first comma, and another with the section of `<string>`after the first comma.

When you split a string once, you'll get 2 chunks. When you split a string twice, you'll get 3 chunks. When you split a string `k` times, you'll get `k+1` chunks.

▶ Let's take a few examples to see the `split()` method in action.

## Python `split()` Method Examples

Let's start with `my_string` shown below. 

```python
my_string = "I code for 2 hours everyday"
```

 Now, call the `split()` method on `my_string`, without the arguments `sep` and `maxsplit`.

```python
my_string.split()
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-50.png)

You can see that `my_string` has been split on all whitespaces and the list of substrings is returned, as shown above.

▶ Let's now consider the following example. Here, `my_string` has names of fruits, separated by commas.

```python
my_string = "Apples,Oranges,Pears,Bananas,Berries"
```

Let's now split `my_string` on commas – set `sep = ","` or only specify `","` in the method call.

```python
my_string.split(",")
```

As expected, the `split()` method returns a list of fruits, where each fruit in `my_string` is now a list item.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-51.png)

▶ Let's now use the optional `maxsplit` argument as well by setting it equal to 2.

```python
my_string.split(",",2)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-52.png)

Let's try to parse the returned list. 

Recall that `my_string` is `"Apples,Oranges,Pears,Bananas,Berries"`, and we decided to split on commas ( `","`).

* The first comma is after `Apples`, and after the first split you'll have 2 items,  `Apples` and `Oranges,Pears,Bananas,Berries`.
* The second comma is after `Oranges`. And you'll have 3 items, `Apples`, `Oranges`, and `Pears,Bananas,Berries` after the second split.
* At this point, you've reached the `maxsplit` count of 2, and no further splits can be made.
* This is why the portion of the string after the second comma is lumped together as a single item in the returned list.

I hope you understand how the `split()` method and the arguments `sep` and `maxsplit` work.

## Python `join()` Method Syntax

Now that you know how to split a string into substrings, it's time to learn how to use the `join()` method to form a string from substrings.

The syntax of Python's `join()` method is:

```python
<sep>.join(<iterable>)
```

Here,

* `<iterable>` is any Python iterable containing the substrings, say, a list or a tuple, and
* `<sep>` is the separator that you'd like to join the substrings on.

> In essence, the `join()` method joins all items in `<iterable>` using `<sep>` as the separator.

▶ And it's time for examples.

## Python `join()` Method Examples

In the previous section on the `split()` method, you split `my_string` into a list on the occurrences of commas. Let's call the list `my_list`.

Now, you'll form a string using the `join()` method to put together items in the returned list. The items in `my_list` are all names of fruits.

```python
my_list = my_string.split(",")

# after my_string is split my_list is:
['Apples', 'Oranges', 'Pears', 'Bananas', 'Berries']


```

📑 Note that the separator to join on should be specified as a _string_. You'll run into syntax errors if you don't do so, as shown below.

```python
,.join(my_list)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-49.png)

▶ To join the items in `my_list` using a comma as the separator, use `","` not `,`. This is shown in the code snippet below.

```python
", ".join(my_list)
```

The above line of code joins items in `my_list` using a comma followed by a space as the separator.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-53.png)

You can specify any separator of your choice. This time, you'll use 3 underscores (`___`) to join items in `my_list`.

```python
"___".join(my_list)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-54.png)

The items in `my_list` have now been joined into a single string, and have all been separated from each other by a `___`.

And you now know how you can form a Python string by putting together substrings using the `join()` method.

## Conclusion

In this tutorial, you've learned the following:

* `<string>.split(sep, maxsplit)` splits `<string>` on the occurrence of `sep`, `maxsplit` number of times,
* `<sep>.join(<iterable>)` joins substrings in `<iterable>` using `<sep>` as the separator.

Hope you found this tutorial helpful. Happy coding!

