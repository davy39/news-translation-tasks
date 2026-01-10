---
title: Python RegEx – How to Import a Regular Expression in Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-01T17:28:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-import-a-regular-expression-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/regexpy.png
tags:
- name: Python
  slug: python
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'Virtually all the programming languages out there support regular expressions.
  Regex is built into languages like JavaScript and Pearl, while others like Java
  and Python have standard libraries for working with it.

  In this article, we’ll look at how ...'
---

Virtually all the programming languages out there support regular expressions. Regex is built into languages like JavaScript and Pearl, while others like Java and Python have standard libraries for working with it.

In this article, we’ll look at how you can import regular expressions in Python and use it. We’ll also look at some methods Python provides for working with regular expressions.

## What We'll Cover
- [How to Import Regular Expressions in Python](#heading-how-to-import-regular-expressions-in-python)
- [How to Use the Python `re` Module with RegEx](#heading-how-to-use-the-python-re-module-with-regex)
  - [RegEx Example with the `match()` Method](#regexexamplewiththematchmethod)
  - [RegEx Example with the `search()` Method](#regexexamplewiththesearchmethod)
  - [RegEx Example with the `findall()` Method](#regexexamplewiththefindallmethod)
  - [RegEx Example with the `split()` Method](#regexexamplewiththesplitmethod)
  - [RegEx Example with the `sub()` Method](#regexexamplewiththesubmethod)
- [Conclusion](#heading-conclusion)  

## How to Import Regular Expressions in Python

Python provides the `re` module for using regular expressions. It is a standard module built into Python, so if you have the latest version of Python, you don’t need to install it separately with package managers.

To import the `re` module in Python, you do it with the import keyword:

```py
import re
``` 

## How to Use the Python `re` Module with RegEx

Python provides some methods you can use to work with regular expressions such as `match()`, `search()`, `findall()`, `split()`, and `sub()`. 

To use those methods with RegEx, you have to prepend them with the `re` module and dot (`.`) like this:

```py
re.match(pattern, string) # to use the match method
re.findall(pattern, string) # to use the findall method 
re.sub(pattern, string) # to use the sub method
re.search(pattern, string) # to use the search method 
re.split(pattern, string) # to use the split method
``` 

The RegEx examples I’ve provided will use those methods.

### RegEx Example Using the `match()` Method

The `match()` takes a regular expression and the string and then checks if the string matches the pattern in the regular expression. 

Here’s an example:

```py
import re 

my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt)
print(res) # returns None
```

In the example above:
- I have a `my_txt` variable set to `freeCodeCamp` and a `my_regex_1` variable set to the pattern `^freecodecamp$`. That’s how you write regular expressions in Python —  you put them inside quotes.
- To check if the text matches the pattern, I used the `match()` method and put in the `my_regex_1` and `my_txt` variables.

The string is `freeCodeCamp`, and the pattern is `^freecodecamp$`, so why did the match method return `None`? It’s because it doesn’t find a match. 

There are some uppercase letters in the `my_txt` variable, but the pattern is looking for lowercase letters.

If you’re familiar with RegEx in JavaScript or Pearl, you can use the `i` flag to match all uppercase or lowercase letters in a string. 

So, what we need to do to have a match is to use the `i` flag. But using a flag with regular expressions in Python is different from how we use it in JavaScript.

To use flags with regular expressions in Python, the `re` module provides the `IGNORECASE`, `ASCII`, `MULTILINE`, `VERBOSE`, `DOTALL`, and `LOCAL` options. 

This is how you would use a flag with regular expressions in Python:

```py
re.match(pattern, string, re.ASCII) # to perform only ASCII matching 
re.findall(pattern, string, re.DOTALL) # to match any character – including a new line.
re.sub(pattern, string, re.IGNORECASE) # to perform case insensitive matching
re.search(pattern, string, re.LOCALE) # to perform case insensitive matching dependent on the current locale
re.search(pattern, string, re.VERBOSE) # to allow comments in regex
re.split(pattern, string, re.MULTILINE) # to perform multiple line matching. Commonly used with metacharacters (^ and $)
```

For our example, the flag we can use is the `IGNORECASE`. Let’s use it so we can get a match:

```py
import re 

my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt, re.IGNORECASE)
print(res) #Output: <re.Match object; span=(0, 12), match='freeCodeCamp'>
```

Now we have a match!


### RegEx Example Using the `search()` Method

The `search()` function takes a regex and a string and then returns the first occurrence in a match object. If it finds no match, it returns `None`.

```py
import re 

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

res = re.search(my_regex, my_txt, re.IGNORECASE)
print(res) # <re.Match object; span=(6, 12), match='Friday'>
```

You can see it returns the first occurrence of the text `Friday`, located between index `6` and `12`.

You can get that index with the `start()` method:

```py
res = re.search(my_regex, my_txt, re.IGNORECASE)
print("The first occurrence is located at index ", res.start()) # The first occurrence is located at index  6
```

You can get the start and end index of the occurrence like this:

```py
res = re.search(my_regex, my_txt, re.IGNORECASE)
print("The first occurrence is located between index", res.start(), "and index", res.end()) # The first occurrence is located between index 6 and index 12
```

You can also use `match()` with an `if…else` statement:

```py
import re 

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

if re.search(my_regex, my_txt, re.IGNORECASE):
    print("Found a match!") #Output: Found a match!
else:
    print("Found no match")   
res = re.search(my_regex, my_txt, re.IGNORECASE)
```


### RegEx Example Using the `findall()` Method

The `findall()` method takes a regex and a string, and then looks through the string and finds all occurrences that match the regex. It puts all those occurrences inside a list.

Here’s an example:

```py
import re 

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'
res = re.findall(my_regex, my_txt, re.IGNORECASE)

print(res) # Output: ['Friday', 'Friday', 'Friday', 'Friday']
```

Notice the regex I use contains the text `friday`, which doesn’t match any occurrence of “Friday”. The `IGNORECASE` flag was what made it match those occurrences.


### RegEx Example Using the `split()` Method

The `split()` method does what the name implies - it splits a string by the pattern passed into it. 

This method could be useful if you want to filter out some words you don’t want in a string.

```py
import re 

my_txt = "Python and JavaScript and C# and Java and Golang and F#"
my_regex = 'and'

res = re.split(my_regex, my_txt)
print(res) # ['Python ', ' JavaScript ', ' C# ', ' Java ', ' Golang ', ' F#']
```


### RegEx Example Using the `sub()` Method

The `sub()` works like JavaScript’s `replace()` method. It replaces the character that matches the regular expression passed into it. 

The `sub()` method is a little different from other methods – it takes up to 5 parameters:

```py
re.sub(pattern, replacement, string, count, flags)
```

So, if you want to specify a flag but you’re not specifying the `count`, it won’t work as expected. 

Nobody does a standup meeting on Friday, so let’s use the `sub` method on the string we used for the `search()` and `findall()` examples:

```py
import re 

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

res = re.sub(my_regex, "Monday", my_txt, 4, re.IGNORECASE)
print(res) # Output: Every Monday, we have a standup meeting. The only reason why we might not have a meeting on a Monday is public holiday. That Monday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Monday.
```

There are 4 occurrences of `Friday` in the `my_txt` string. That’s why I specified 4 as the count.

## Conclusion

In this article, we looked at how to import regular expressions through the `re` module. But we didn’t stop there, as I also took you through how to use the module with the methods for working with regular expressions in Python.

In addition, we also took a brief look at how to use flags in Python regular expressions.

If you find this article helpful, don’t hesitate to share it with your friends and family.


