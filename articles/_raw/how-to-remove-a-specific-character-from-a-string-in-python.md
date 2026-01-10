---
title: How to Remove a Specific Character from a String in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-12-07T18:43:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-specific-character-from-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-josh-sorenson-1714208.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When coding in Python, there may be times when you need to remove a character
  from a string.

  Removing characters from strings is handy if you are working with user-generated
  inputs and need to clean your data and remove unwanted characters.

  Specifica...'
---

When coding in Python, there may be times when you need to remove a character from a string.

Removing characters from strings is handy if you are working with user-generated inputs and need to clean your data and remove unwanted characters.

Specifically, you may need to remove only one instance of a character or even all occurrences of a character from a string.

Python offers many ways to help you do this.

Two of the most common ways to remove characters from strings in Python are:

- using the `replace()` string method
- using the `translate()` string method

When using either of the two methods, you can specify the character(s) you want to remove from the string. 

Both methods replace a character with a value that you specify. And if you specify an empty character instead, the character you want to remove gets deleted without a replacement.

Something to note when using these methods is that the original string doesn't get altered since strings are immutable. Instead, both methods return a new modified string that doesn't contain the characters you wanted to remove.

In this article, you will learn how to use both methods to remove a character or multiple characters from a string with the help of coding examples.

Here is what we will cover:

1. [How to remove a specific character from a String using the `replace()` method](#remove-char-replace)
2. [How to remove multiple characters from a string using the `replace()` method](#remove-chars-replace)
    1. [Remove multiple characters with method chaining ](#chaining)
    2. [Remove multiple characters with a `for` loop](#for-loop)
    3. [Remove multiple characters with regular expressions](#regular-expressions)
3. [How to remove a specific character from a string using the `translate()` method](#remove-char-translate)
4. [How to remove multiple characters from a string using the `translate()` method](#remove-chars-translate)

Let's dive in!

## How to Remove a Specific Character from a String in Python Using the `replace()` Method <a name="remove-char-replace"></a>

The general syntax for the `replace()` method looks something similar to the following:

```
string.replace( character, replacement, count)
```

Let's break it down:

- You append the `replace()` method on a `string`.
- The `replace()` method accepts three arguments:
    - `character` is a required argument and represents the specific character you want to remove from `string`.  
    - `replacement` is a required argument and represents the new string/character that will take the place of `character`.
    - `count` is an optional argument that represents the maximum number of `character` occurrences you want to remove from `string`. If you don't include `count`, then by default, the `replace()` method will remove all the occurrences of `character`. 
 
The `replace()` method doesn't modify the original string. Instead, its return value is a copy of the original string without the characters you wanted to remove.

Now, let's see `replace()` in action!

Say you have the following string, and you want to remove all of the exclamation marks:

```python
my_string = "Hi! I! Love! Python!"
```

Here is how you would remove all the occurrences of the `!` character:

```python
my_string = "Hi! I! Love! Python!"

my_new_string = my_string.replace("!", "")

print(my_new_string)

# output

# Hi I Love Python
```

In the example above, I appended the `replace()` method to `my_string`.

I then stored the result in a new variable named `my_new_string`.

Remember, strings are immutable.  The original string remains unchanged - `replace()` returns a new string and doesn't modify the original one.

I specified that I wanted to remove the `!` character and indicated that I wanted to replace `!` with an empty character. 

I also didn't use the `count` argument, so `replace()` replaced *all* occurrences of the `!` character with an empty one.

The original string stored in a variable `my_string` has four occurrences of the `!` character.

If I wanted to remove only three occurrences of the character and not all of them, I would use the `count` argument and pass a value of `3` to specify the number of times I would like to replace the character:

```python
my_string = "Hi! I! love! Python!"

my_new_string = my_string.replace("!", "", 3)

print(my_new_string)

# output

# Hi I love Python!
```

## How to Remove Multiple Characters from A String in Python Using the `replace()` Method <a name="remove-chars-replace"></a>

There may be a time when you will need to replace multiple characters from a string.

In the following sections, you will see three ways you can achieve this using the `replace()` method.

### Remove Multiple Characters With Method Chaining <a name="chaining"></a>

One way you could achieve this is by chaining the `replace()` method like so:

```python
my_string = "Hi!? I!? love!? Python!?"

my_new_string = my_string.replace("!","").replace("?","")

print(my_new_string)

# output

# Hi I love Python
```

That said, this way of removing characters can be quite difficult to read.

### Remove Multiple Characters With A `for` Loop <a name="for-loop"></a>

Another way to accomplish this is to use the `replace()` method inside a `for` loop:

```python
my_string = "Hi!? I!? love!? Python!?"

replacements = [('!', ''), ('?', '')]

for char, replacement in replacements:
    if char in my_string:
        my_string = my_string.replace(char, replacement)

print(my_string)

# output

# Hi I love Python
```

I first created a string that contains the two characters I want to remove, `!` and `?`, and stored it in the variable `my_string`.

I stored the characters I want to replace, along with their replacements, in a list of tuples with the name `replacements` - I want to replace `!` with an empty string and `?` with an empty string.

Then, I used a `for` loop to iterate over the list of tuples (if you need a refresher on `for` loops, give [this article](https://www.freecodecamp.org/news/python-for-loop-example-and-tutorial/) a read).

Inside the `for` loop, I used the `in` operator to check whether the characters are inside the string. And if they were, I used the `replace()` method to replace them.

Finally, I reassigned the variable.

### Remove Multiple Characters With Regular Expressions <a name="regular-expressions"></a>

And yet another way to accomplish this is by using the regular expression library `re` and the `sub` method.

You first need to import the library:

```python
import re
```

Then, specify the group of characters you want to remove (in this case, the `!` and `?` characters), along with the characters you want to replace them with. In this case, the replacement is an empty character:

```python
import re

my_string = "Hi!? I!? love!? Python!?"

my_new_string = re.sub('[!?]',"",my_string)

print(my_new_string)

# output

# Hi I love Python
```

## How to Remove a Specific Character from a String in Python Using the `translate()` Method <a name="remove-char-translate"></a>

Similarly to the `replace()` method, `translate()` removes characters from a string.

With that said, the `translate()` method is a bit more complicated and not the most beginner-friendly.

The `replace()` method is the most straightforward solution to use when you need to remove characters from a string.

When using the `translate()` method to replace a character in a string, you need to create a character translation table, where `translate()` uses the contents of the table to replace the characters.

A translation table is a dictionary of key-value mappings, and each key gets replaced with a value.

You can use the `ord()` function to get the character's Unicode value and then map that value to another character.

This method returns a new string where each character from the old string gets mapped to a character from the translation table. 

The return value is a new string.

Let's see an example using the same code from the previous sections:

```python
my_string = "Hi! I! love! Python!"

my_new_string = my_string.translate( { ord("!"): None } )

print(my_new_string)

# output

# Hi I love Python
```

In the example above, I used the `ord()` function to return the Unicode value associated with the character I wanted to replace, which in this case was `!`.

Then, I mapped that Unicode value to `None` - another word for nothing or empty - which makes sure to remove it. Specifically, it replaced every instance of the `!` character with a `None` value.

## How to Remove Multiple Characters from a String in Python Using the `translate()` Method <a name="remove-chars-translate"></a>

What if you need to replace more than one character using the `translate()` method? For that, you can use an iterator like so:

```python
my_string = "Hi!? I!? love!? Python!?"

my_new_string = my_string.translate( { ord(i): None for i in '!?'} )

print(my_new_string)

# output

# Hi I love Python
```

In the example above, I replaced both `!` and `?` characters with the value `None` by using an iterator that looped through the characters I wanted to remove.

The `translate()` method checks whether each character in `my_string` is equal to an exclamation point or a question mark. If it is, then it gets replaced with `None`.

## Conclusion

Hopefully, this article helped you understand how to remove characters from a string in Python using the built-in `replace()` and `translate()` string methods.

Thank you for reading, and happy coding!


