---
title: Python Remove Character from a String – How to Delete Characters from Strings
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-07T18:08:44.000Z'
originalURL: https://freecodecamp.org/news/python-remove-character-from-a-string-how-to-delete-characters-from-strings
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/fotis-fotopoulos-LJ9KY8pIH3E-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python you can use the replace() and translate() methods to specify\
  \ which characters you want to remove from a string and return a new modified string\
  \ result. \nIt is important to remember that the original string will not be altered\
  \ because string..."
---

In Python you can use the `replace()` and `translate()` methods to specify which characters you want to remove from a string and return a new modified string result. 

It is important to remember that the original string will not be altered because strings are immutable. 

In this article, I will show you how to work with the `replace()` and `translate()` methods through the use of code examples. 

## How to use Python's replace() method

Here is the basic syntax for the `replace()` method.

```py
str.replace(old_str, new_str[, optional_max])
```

The `old_str` parameter represents the substring you want to replace.

The `new_str` parameter represents the new substring you want to use.

The `optional_max` parameter represents the maximum count of times to replace the old substring with the new substring. 

The return value for the `replace()` method will be a copy of the original string with the old substring replaced with the new substring.

### Python replace() example

Let's take a look at some examples.

In this first example, we have a string called `developer` with my name assigned to it.

```py
developer = 'Jessica Wilkins'
```

If we wanted to remove my last name, we can use the `replace()` method like this:

```py
developer.replace('Wilkins', '')
```

This tells the computer to take the old substring of `Wilkins` and replace it with an empty string. 

If we print out the result then this is what we would get:

```py
print(developer.replace('Wilkins', ''))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-8.41.55-PM.png)

It is important to remember that the original string remains unchanged because strings are immutable. The `replace()` method will return a new string.

In this next example, we want to use the `optional_max` parameter to set the number of times we want to remove the letter `s` from my name.

```py
developer.replace('s', '', 2)
```

This line of code says to remove the letter `s` only twice from the string `Jessica Wilkins`. 

If we were to print out the result, this is what it would look like:

```py
print(developer.replace('s', '', 2))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-8.55.22-PM.png)

## How to use Python's translate() method

Another way to remove characters from a string is to use the `translate()` method. This method returns a new string where each character from the old string is mapped to a character from the translation table and translated into a new string.

Here is the basic syntax for Python's `translate()` method.

```py
str.translate(table)
```

### Python translate() example

Let's take a look at some examples to better understand the `translate()` method.

In this example, we want to remove all instances of the letter `i` from the string `Jessica Wilkins`. 

We first need to use Python's built in `ord()` function to get the Unicode code point value for the letter `i`. The `ord()` function will return a numerical value. 

```py
ord('i')
```

For our table, we need to assign the value of `None` so the computer will know to replace the letter `i` with nothing.

```py
{ord('i'): None}
```

Now we use our table inside the `translate()` method.

```py
developer.translate({ord('i'): None})
```

If we were to print out the result, this is what it would look like:

```py
developer = 'Jessica Wilkins'

print(developer.translate({ord('i'): None}))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-10.24.52-PM.png)

In this next example, we want to return a new string with the letters `e`, `s`, and `i` removed. To do this, we can use an iterator in our table parameter.

```py
{ord(letter): None for letter in 'esi'}
```

That line of code tells the computer to find all occurrences of `e`, `s`, and `i` and replace it with `None`. 

If we were to print out the result, this is what it would look like:

```py
developer = 'Jessica Wilkins'

print(developer.translate({ord(letter): None for letter in 'esi'}))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-10.37.10-PM.png)

## Conclusion

In Python you can use the `replace()` and `translate()` methods to specify which characters you want to remove from the string and return a new modified string result. 

It is important to remember that the original string will not be altered because strings are immutable. 

Here is the basic syntax for the `replace()` method.

```py
str.replace(old_str, new_str[, optional_max])
```

The return value for the `replace()` method will be a copy of the original string with the old substring replaced with the new substring.

Another way to remove characters from a string is to use the `translate()` method. This method returns a new string where each character from the old string is mapped to a character from the translation table and translated into a new string.

Here is the basic syntax for Python's `translate()` method.

```py
str.translate(table)
```

I hope you enjoyed this article and best of luck on your Python journey. 

