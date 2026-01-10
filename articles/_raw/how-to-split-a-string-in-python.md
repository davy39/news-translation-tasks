---
title: Python .split() – Splitting a String in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-09-08T17:22:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-split-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-lukas-952354.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you will learn how to split a string in Python.

  Firstly, I''ll introduce you to the syntax of the .split() method. After that, you
  will see how to use the .split() method with and without arguments, using code examples
  along the way.

  ...'
---

In this article, you will learn how to split a string in Python.

Firstly, I'll introduce you to the syntax of the `.split()` method. After that, you will see how to use the `.split()` method with and without arguments, using code examples along the way.

Here is what we will cover:

1. [`.split()` method syntax](#syntax)
	1. [How does the `.split()` method work without any arguments?](#no-arguments)
	2. [How does the `.split()` method work with the `separator` argument?](#separator)
	3. [How does the `.split()` method work with the `maxsplit` argument?](#maxsplit)


## What Is The `.split()` Method in Python? `.split()` Method Syntax Breakdown <a name="syntax"></a>

You use the `.split()` method for splitting a string into a list.

The general syntax for the `.split()` method looks something like the following:

```python
string.split(separator, maxsplit)
```

Let's break it down:

- `string` is the string you want to split. This is the string on which you call the `.split()` method.
- The `.split()` method accepts two arguments.
- The first *optional* argument is `separator`, which specifies what kind of separator to use for splitting the string. If this argument is not provided, the default value is any whitespace, meaning the string will split whenever `.split()` encounters any whitespace.
- The second *optional* argument is `maxsplit`, which specifies the maximum number of splits the `.split()` method should perform. If this argument is not provided, the default value is `-1`, meaning there is no limit on the number of splits, and `.split()` should split the string on all the occurrences it encounters `separator`.

The `.split()` method returns a new list of substrings, and the original string is not modified in any way.


### How Does The `.split()` Method Work Without Any Arguments? <a name="no-arguments"></a>

Here is how you would split a string into a list using the `.split()` method without any arguments:

```python
coding_journey = "I am learning to code for free with freeCodecamp!"

# split string into a list and save result into a new variable
coding_journey_split = coding_journey.split()

print(coding_journey)
print(coding_journey_split)

# check the data type of coding_journey_split by using the type() function
print(type(coding_journey_split))

# output
# I am learning to code for free with freeCodecamp!
# ['I', 'am', 'learning', 'to', 'code', 'for', 'free', 'with', 'freeCodecamp!']
# <class 'list'>

```

The output shows that each word that makes up the string is now a list item, and the original string is preserved.

When you don't pass either of the two arguments that the `.split()` method accepts, then by default, it will split the string every time it encounters whitespace until the string comes to an end.

What happens when you don't pass any arguments to the `.split()` method, and it encounters consecutive whitespaces instead of just one?

```python
coding_journey = "I love   coding"

coding_journey_split = coding_journey.split()

print(coding_journey_split)

# output
# ['I', 'love', 'coding']
```

In the example above, I added consecutive whitespaces between the word `love` and the word `coding`. When this is the case, the `.split()` method treats any consecutive spaces as if they are one single whitespace.


### How Does The `.split()` Method Work With The `separator` Argument? <a name="separator"></a>

As you saw earlier, when there is no `separator` argument, the default value for it is whitespace. That said, you can set a different `separator`. 

The `separator` will break and divide the string whenever it encounters the character you specify and will return a list of substrings.

For example, you could make it so that a string splits whenever the `.split()` method encounters a dot, `.`:

```python
fave_website = "www.freecodecamp.org"

fave_website_split = fave_website.split(".")

print(fave_website_split)

# output
# ['www', 'freecodecamp', 'org']
```

In the example above, the string splits whenever `.split()` encounters a `.`

Keep in mind that I didn't specify a dot followed by a space. That wouldn't work since the string doesn't contain a dot followed by a space:

```python
fave_website = "www.freecodecamp.org"

fave_website_split = fave_website.split(". ")

print(fave_website_split)

# output
# ['www.freecodecamp.org']
```

Now, let's revisit the last example from the previous section.

When there was no `separator` argument, consecutive whitespaces were treated as if they were single whitespace.

However, when you specify a single space as the `separator`, then the string splits every time it encounters a single space character:

```python
coding_journey = "I love   coding"

coding_journey_split = coding_journey.split(" ")

print(coding_journey_split)

# output
# ['I', 'love', '', '', 'coding']
```

In the example above, each time `.split()` encountered a space character, it split the word and added the empty space as a list item.

### How Does The `.split()` Method Work With The `maxsplit` Argument? <a name="maxsplit"></a>

When there is no `maxsplit` argument, there is no specified limit for when the splitting should stop.

In the first example of the previous section, `.split()` split the string each and every time it encountered the `separator` until it reached the end of the string.

However, you can specify when you want the split to end.

For example, you could specify that the split ends after it encounters one dot:

```python
fave_website = "www.freecodecamp.org"

fave_website_split = fave_website.split(".", 1)

print(fave_website_split)

# output
# ['www', 'freecodecamp.org']
```

In the example above, I set the `maxsplit` to `1`, and a list was created with two list items.

I specified that the list should split when it encounters one dot. Once it encountered one dot, the operation would end, and the rest of the string would be a list item on its own.

## Conclusion

And there you have it! You now know how to split a string in Python using the `.split()` method.

I hope you found this tutorial helpful.

To learn more about the Python programming language, check out freeCodeCamp's [Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thank you for reading, and happy coding!


