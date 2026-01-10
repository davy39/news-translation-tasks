---
title: Remove From String in Python – How to Remove Characters from a String
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-20T20:20:23.000Z'
originalURL: https://freecodecamp.org/news/remove-from-string-in-python-how-to-remove-characters-from-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/remove_char.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In Python, there are times when you might want to remove unnecessary characters
  from a string. Python provides two built-in methods you can use for that purpose
  – replace() and translate().

  So, in this article, you will learn how to remove a characte...'
---

In Python, there are times when you might want to remove unnecessary characters from a string. Python provides two built-in methods you can use for that purpose – `replace()` and `translate()`.

So, in this article, you will learn how to remove a character from a string with those two methods and even replace the characters with new ones. 

Apart from those two methods, I will also show you how to use a for loop and string slicing to remove characters from a string.


## What We’ll Cover
- [How to Remove a Character from a String with the `replace()` Method](#heading-how-to-remove-a-character-from-a-string-with-the-replace-method)
  - [How to Remove Multiple Characters from a String with the `replace()` Method](#heading-how-to-remove-multiple-characters-from-a-string-with-the-replace-method)
- [How to Remove a Character from a String with the `translate()` Method](#heading-how-to-remove-a-character-from-a-string-with-the-translate-method)
- [How to Remove a Character from a String with String Slicing](#heading-how-to-remove-a-character-from-a-string-with-string-slicing)
- [Conclusion](#heading-conclusion)


## How to Remove a Character from a String with the `replace()` Method
The `replace()` method does what the name implies. It replaces a certain character in a string with another specified character.

So, if you want to remove a character from a string with it, you can pass in an empty string as the new value.

The `replace()` method takes up to 3 parameters:

```py
str.replace(old_char, new_char, count)
```

* the old character is the character you want to replace
* the new character is the replacement for the old character
* the `count` is an optional parameter for specifying the number of occurrences of the old value you want to replace   

To remove the character, you specify an empty string for the new character. 

Here’s how the `replace()` method works in code: 

```py
str_with_num = "freeCodeCamp2"
str_without_num = str_with_num.replace("2", "")

print("Original string:", str_with_num) # Original string: freeCodeCamp2
print("The string after passing it to replace:", str_without_num) # The string after passing it to replace: freeCodeCamp
```

You can see that I specified an empty string as the new value in order to remove that `2` at the end of the `freeCodeCamp2` string.

You can also remove multiple values from a string with the `replace()` method. In the example below, I removed “don’t” from the string because I do love Python:

```py
wrong_str = "I don'tlove Python"
right_str = wrong_str.replace("don't", "")

print("Original string:", wrong_str) # Original string: I don'tlove Python
print("The string after passing it to replace:", right_str) # The string after passing it to replace: I love Python
```

In addition, the replacement value does not have to be an empty string. I’m saying the main purpose of the `replace()` method is to replace a character.

In the example below, I removed `s` from the `freeCodeCampes` string and replaced it with `r` because I’m a camper:

```py
wrong_str = "freeCodeCampes"
right_str = wrong_str.replace("s", "r")

print("Original string:", wrong_str) # Original string: freeCodeCampes
print("The string after passing it to replace:", right_str) # The string after passing it to replace: freeCodeCamper
```

### How to Remove Multiple Characters from a String with the `replace()` Method

You can chain two or more replace methods together to remove multiple characters from a string:

```py
str_with_symbols = "We! love JavaScript, &Python, and Java.?"
str_without_symbols = str_with_symbols.replace("!", "").replace("&", "").replace("?", "")

print("Original string:", str_with_symbols) # Original string: We! love JavaScript, &Python, and Java.?
print("The string after passing it to replace:", str_without_symbols) # The string after passing it to replace: We love JavaScript, Python, and Java.
```

You can also use a for loop to remove multiple characters from a string by passing the replace method into the loop:

```py
str = "freeCodeCamp! is the best, ?easiest, & coolest place to learn how to code?"
replacements = [("!", ""), ("?", ""), ("&", "and")]

for i, j in replacements:
    if i in str:
        str = str.replace(i, j)
print(str)  # freeCodeCamp is the best, easiest, and coolest place to learn how to code
```

**Here’s what I did in that loop**:
- I put the original string in a variable named `str`
- I also put the characters I want to replace and their replacements in a list of tuples I call `replacements`
- `i` represents the individual first values in those tuples and `j` represents each second value in the tuples. For example, in the last tuple, "and" would replace "&"
- I looped through the replacements with a `j` variable, passed `i` in to the `replace()` method as the old character, and `j` as the replacement character


## How to Remove a Character from a String with the `translate()` Method

The `translate()` method is a bit more complicated when you compare it to the `replace()` method. There’s a lot of caveats involved in it and you have to combine it with `ord()` or the `maketrans()` method to make it work.

You have to use `ord()` or `maketrans()` because the `translate()` method expects a translation table or the unicode character of that value to remove.

`ord()` will get you the Unicode value and you can use `maketrans()` to create a translation table – a key:value pair in a dictionary.

The `translate()` method is efficient when you want to remove many characters from a string or user input. All you need to do is create a translation table containing the characters and what you want to replace them with. 

You can also be more choosy with the characters you want to remove. That's because if the character and its replacement are not in the translation table, that character will not be removed.

This is how the `translate()` method works with the `ord()` method:

```py
str_with_num = "freeCodeCamp2"
str_without_num = str_with_num.translate({ord("2"): None})

print("Original string:", str_with_num) ## Original string: freeCodeCamp2
print("The string after passing it to translate and odd():", str_without_num)  # The string after passing it to translate and odd(): freeCodeCamp
```

And this is how it works with the `maketrans()` method:

```py
my_str = "Gython is easy to learn"
my_table = my_str.maketrans("G", "P")
replaced_str = my_str.translate(my_table)

print(replaced_str) # Python is easy to learn
```

```py
my_str = "Golang"
my_table = my_str.maketrans("Golang", "Python")
replaced_str = my_str.translate(my_table)

print(replaced_str) # Python
```


## How to Remove a Character from a String with String Slicing
You can use string slicing to extract a part of a string you want or remove a part of the string you don’t want.

In the code below, I’m specifying that I want everything after the first character:

```py
str = "ffreeCodeCamp"
new_str = str[1:]
print(new_str) # freeCodeCamp
```

And in the example below, I was able to extract some parts of the string 

`StartMiddleEnd`:
```py
my_str = "StartMiddleEnd"

# Everything before the 5th character
the_start = my_str[:5]

# Everything between the 5th and 11th character
the_mid = my_str[5:11] 

# Everything after the 11th character
the_end = my_str[11:]

print("The start:", the_start)
print("The middle:", the_mid)
print("The end:", the_end)

"""
Output:
The start: Start
The middle: Middle
The end: End
"""
```


## Conclusion
This article showed you how to remove single and multiple characters from a string with the built-in `replace()` and `translate()` methods. 

We also looked at how you can remove a character from a string with string slicing. This works because every character in a string has an index. So, you can use that indexing with slicing to extract or remove some characters from a string.

In Python, it’s also possible to remove one or more characters from a string with regular expressions. You can learn about that from this [article on how to remove characters from a string in Python](https://www.freecodecamp.org/news/how-to-remove-a-specific-character-from-a-string-in-python/#regular-expressions).  


