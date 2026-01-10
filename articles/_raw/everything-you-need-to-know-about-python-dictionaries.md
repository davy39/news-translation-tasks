---
title: Python Dictionary – How to Perform CRUD Operations on dicts in Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-01-11T19:05:01.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-python-dictionaries
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/dictionary.png
tags:
- name: crud
  slug: crud
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "One of the most important composite data types in Python is the dictionary.\
  \ It's a collection you use to store data in {key:value} pairs. \nDictionaries are\
  \ ordered and mutable, and they cannot store duplicate data. Just keep in mind that\
  \ before Pytho..."
---

One of the most important composite data types in Python is the dictionary. It's a collection you use to store data in `{key:value}` pairs. 

Dictionaries are ordered and mutable, and they cannot store duplicate data. Just keep in mind that before Python 3.6, dictionaries were unordered.

Alright, let's dive in and learn more about how they work.

## How to create a dictionary in Python

As we know, a dictionary consists of a collection of `{key:value}` pairs. A colon (`:`) separates each key from its associated value.

We can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces (`{}`).

```python
my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}
```

In the above example, `Name`, `Roll`, and `Subjects` are the keys of the dictionary `my_dict`. `Ashutosh Krishna`, `23`, and `["OS", "CN", "DBMS"]` are their respective values.

We can also declare a dictionary using the built-in `dict()` function like this:

```python
my_dict = dict({
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
})

```

A list of tuples works well for this:

```python
my_dict = dict([
    ("Name", "Ashutosh Krishna"), 
    ("Roll", 23),
    ("Subjects", ["OS", "CN", "DBMS"])
])

```

They can also be specified as keyword arguments.

```python
my_dict = dict(
    Name="Ashutosh Krishna", 
    Roll=23, 
    Subjects=["OS", "CN", "DBMS"]
)

```

## How to access dictionary values in Python

You can't access dictionary values using the index.

```python
my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}

print(my_dict[1])

```

If you try to do this, it will throw a **KeyError** like this:

```bash
Traceback (most recent call last):
  File "C:\Users\ashut\Desktop\Test\hello\test.py", line 7, in <module>
    print(my_dict[1])
KeyError: 1
```

Notice that the exception is called KeyError. Does that mean the dictionary values can be accessed using the keys? Yes, you got it right!

You can get a value from a dictionary by specifying its corresponding key in square brackets (`[]`).

```repl
>>> my_dict['Name']          
'Ashutosh Krishna'
>>> my_dict['Subjects'] 
['OS', 'CN', 'DBMS']
```

If a key doesn't exist in the dictionary, we get a KeyError exception as we saw above.

```repl
>>> my_dict['College']  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'College'
```

But we can also avoid this error using the `get()` function.

```repl
>>> my_dict.get('College')
>>> 
```

If the key exists in the dictionary, it will retrieve the corresponding value. But if it doesn't exist, it won't throw an error.

## How to update a dictionary in Python

Dictionaries are mutable, which means they can be modified. We can add a new `{key:value}` pair or modify existing ones.

Adding a new item in the dictionary is quite easy using the assignment operator, like this:

```repl
>>> my_dict['College'] = 'NSEC'
>>> my_dict                    
{'Name': 'Ashutosh Krishna', 'Roll': 23, 'Subjects': ['OS', 'CN', 'DBMS'], 'College': 'NSEC'}
```

If the key is already present in the dictionary, it will update the value of that key.

```repl
>>> my_dict['Roll'] = 35
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Roll': 35, 'Subjects': ['OS', 'CN', 'DBMS'], 'College': 'NSEC'}
```

### How to update a dict using the update() method

We can also update the dictionary using the built-in `update()` method like this:

```repl
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Roll': 35, 'Subjects': ['OS', 'CN', 'DBMS'], 'College': 'NSEC'}
>>> another_dict = {'Branch': 'IT'}
>>> my_dict.update(another_dict)
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Roll': 35, 'Subjects': ['OS', 'CN', 'DBMS'], 'College': 'NSEC', 'Branch': 'IT'}
>>>
```

The `update()` method takes either a dictionary or an iterable object of key/value pairs (generally tuples).

```repl
>>> my_dict.update(Branch='CSE') 
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Roll': 35, 'Subjects': ['OS', 'CN', 'DBMS'], 'College': 'NSEC', 'Branch': 'CSE'}
```

## How to remove elements from dictionary in Python

There are several ways to remove elements from a Python dictionary.

### How to remove elements from a dict with the `pop()` method

We can remove a particular item in a dictionary by using the `pop()` method. This method removes an item with the provided `key` and returns the `value`.

```repl
>>> roll = my_dict.pop('Roll') 
>>> roll
35
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Subjects': ['OS', 'CN', 'DBMS'], 'College': 'NSEC', 'Branch': 'CSE'}
```

### How to remove an item from a dict with the `popitem()` method

The `popitem()` removes the last key-value pair and returns it as a tuple:

```repl
>>> my_dict.popitem()
('Branch', 'CSE')
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Subjects': ['OS', 'CN', 'DBMS'], 'College': 'NSEC'}
```

### How to remove an item from a dict with the `del` keyword

You can use the `del` keyword to delete a particular `{key:value}` pair or even the entire dictionary.

```repl
>>> del my_dict['Subjects'] 
>>> my_dict
{'Name': 'Ashutosh Krishna', 'College': 'NSEC'}
>>> del my_dict
>>> my_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_dict' is not defined
```

### How to remove an item from a dict with the `clear()` method

The `clear` method clears all the `{key:value}` pairs in the dictionary.

```repl
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Roll': 23, 'Subjects': ['OS', 'CN', 'DBMS']}
>>> my_dict.clear()
>>> my_dict
{}
```

Notice that after the `clear()` method is called, printing the dictionary doesn't throw an error because the `clear()` method doesn't remove the dictionary. But the `del` keyword removes the dictionary too. That's why we get a NameError in that case.

## Dictionary Operators and Built-in Functions

Let's talk about two important operators and built-in functions we can use with dictionaries.

### `len()` function

The `len()` function returns the number of key-value pairs in a dictionary:

```repl
>>> my_dict
{'Name': 'Ashutosh Krishna', 'Roll': 23, 'Subjects': ['OS', 'CN', 'DBMS']}
>>> len(my_dict)
3
```

### `sorted()` function

The `sorted()` function sorts the elements of a given iterable in a specific order (ascending or descending) and returns it as a list.

```repl
>>> sorted(my_dict)
['Name', 'Roll', 'Subjects']
```

### `in` operator

You can use the `in` operator to check whether a key is present in the dictionary or not.

```repl
>>> 'Roll' in my_dict
True
>>> 'College' in my_dict
False
```

## Built-in Dictionary Methods

There are various built-in methods available in a Python dictionary. We have discussed few of them earlier such as `clear()`, `pop()` ,and `popitem()`. Let's see some other methods too.

<table border="0" style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px !important; margin-left: 0px; padding: 0px; box-sizing: border-box; border-collapse: collapse; width: 728px; white-space: pre-wrap; background-color: rgb(248, 250, 255); border: none; color: rgb(37, 38, 94); font-family: euclid_circular_a, arial, &quot;source sans pro&quot;, &quot;helvetica neue&quot;, helvetica, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="margin: 0px; padding: 0px; box-sizing: border-box; border-top: 1px solid rgb(204, 204, 204);"><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><th style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); text-align: left; min-width: 100px; font-weight: 400;">Method</th><th style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); text-align: left; min-width: 100px; font-weight: 400;">Description</th></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">clear()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Removes all items from the dictionary.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">copy()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Returns a shallow copy of the dictionary.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">fromkeys(seq[, v])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Returns a new dictionary with keys from <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">seq</var> and value equal to <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">v</var> (defaults to <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">None</code>).</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">get(key[,d])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Returns the value of the <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var>. If the <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> does not exist, returns <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> (defaults to <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">None</code>).</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">items()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Return a new object of the dictionary's items in (key, value) format.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">keys()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Returns a new object of the dictionary's keys.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">pop(key[,d])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Removes the item with the <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> and returns its value or <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> if <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> is not found. If <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> is not provided and the <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> is not found, it raises <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">KeyError</code>.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">popitem()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Removes and returns an arbitrary item (<strong style="margin: 0px; padding: 0px; box-sizing: border-box; font-weight: bolder;">key, value</strong>). Raises <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">KeyError</code> if the dictionary is empty.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">setdefault(key[,d])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Returns the corresponding value if the <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> is in the dictionary. If not, inserts the <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> with a value of <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> and returns <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> (defaults to <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">None</code>).</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">update([other])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Updates the dictionary with the key/value pairs from <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">other</var>, overwriting existing keys.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 0px; min-width: 100px; color: rgba(37, 38, 94, 0.7);">values()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 0px; min-width: 100px; color: rgba(37, 38, 94, 0.7);">Returns a new object of the dictionary's values</td></tr></tbody></table>

## How to iterate through a dictionary

By default, when we use a for loop to iterate over a dictionary, we get the keys:

```python
my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}

for item in my_dict:
    print(item)
```

Output:

```bash
Name
Roll
Subjects
```

We can also iterate over a dictionary in the following ways:

### How to iterate through a dictionary using the `items()` method

When we use the `items()` method to iterate over a dictionary, it returns a tuple of key and value in each iteration. Thus we can directly get the key and value in this case:

```python
my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}

for key, value in my_dict.items():
    print(key, value)

```

Output:

```bash
Name Ashutosh Krishna
Roll 23
Subjects ['OS', 'CN', 'DBMS']
```

### How to iterate through a dictionary using `keys()`

In this case, we get the key in each iteration.

```python
my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}

for key in my_dict.keys():
    print(key)

```

Output:

```bash
Name
Roll
Subjects
```

### How to iterate through a dictionary using `values()`

In this case, we get the values of the dictionary directly.

```python
my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}

for value in my_dict.values():
    print(value)

```

Output:

```bash
Ashutosh Krishna
23
['OS', 'CN', 'DBMS']
```

## How to merge dictionaries in Python

We often need to merge dictionaries in Python. I've written a separate article on this topic, which you can read [here](https://iread.ga/posts/76/how-to-merge-dictionaries-in-python).

## Wrapping Up

In this article, we learned what Python dictionaries are and how to perform CRUD operations on them. We also saw several methods and functions associated with them.

I hope you enjoyed it – and thanks for reading!

<a class="cta-button" href="https://newsletter.ashutoshkrris.tk" target="_blank">Subscribe to my newsletter</a>


