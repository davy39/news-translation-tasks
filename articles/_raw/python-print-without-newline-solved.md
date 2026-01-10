---
title: Python Print Without Newline [SOLVED]
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-05-10T16:18:38.000Z'
originalURL: https://freecodecamp.org/news/python-print-without-newline-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Python-Print-Without-Newline--SOLVED-.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "If you're familiar with Python, you may have noticed that the built-in\
  \ function print() doesn't need an explicit \\n character at the end of each line.\
  \ \nThis means that the output from the following snippet of code\nprint('freeCodeCamp\
  \ Curriculum')\npri..."
---

If you're familiar with Python, you may have noticed that the built-in function `print()` doesn't need an explicit `\n` character at the end of each line. 

This means that the output from the following snippet of code

```python
print('freeCodeCamp Curriculum')
print('freeCodeCamp News')
print('freeCodeCamp YouTube Channel')
```

will be:

```shell
freeCodeCamp Curriculum
freeCodeCamp News
freeCodeCamp YouTube Channel
```

This happens because the `print()` function adds the `\n` character to the end of each printed line. Although most of the time this is a convenience, you may sometimes want to print out lines without the `\n` character.

In this article, you'll learn how to change the end of each print statement. And you'll also learn a number of other ways to modify how the built-in function behaves by default.

## How to Print Without a Newline in Python

According to the [official documentation](https://docs.python.org/3/library/functions.html#print) for the `print()` function, the function signature is as follows:

```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

As you can see the function takes five arguments in total. The first one is the object(s) that you want to print on the terminal. Then there is the separator (which you'll learn about in a later section), and the `end` parameter.

The default value of the `end` parameter is `\n`, which means a newline character will be appended to each line printed on the terminal. 

To change this behavior, you can simply override this parameter as follows:

```python
print('freeCodeCamp Curriculum', end=', ')
print('freeCodeCamp News', end=', ')
print('freeCodeCamp YouTube Channel')
```

Since, I've changed the value of `end` to a comma, the output will be `freeCodeCamp Curriculum, freeCodeCamp News, freeCodeCamp YouTube Channel` instead of the three separate lines. 

You can use any character as the value of `end`. If you'd want nothing at the end of lines, simply use an empty string.

## How to Print With a Separator in Python

Remember the `sep` argument in the function signature? In this section, you'll learn about its usage. 

You may or may not know already that the `print()` function can take multiple objects at once to print out as follows:

```python
print('freeCodeCamp Curriculum', 'freeCodeCamp News', 'freeCodeCamp YouTube Channel')
```

The output from this code will be:

```shell
freeCodeCamp Curriculum, freeCodeCamp News, freeCodeCamp YouTube Channel
```

As you can see, the function has printed the three strings in a single line separated by commas. If you want to use something else like a dash as a separator, you can do so as follows:

```python
print('freeCodeCamp Curriculum', 'freeCodeCamp News', 'freeCodeCamp YouTube Channel', sep=' - ')
```

The output from this code will be:

```shell
freeCodeCamp Curriculum - freeCodeCamp News - freeCodeCamp YouTube Channel
```

I hope you've got the idea. Like the `end` argument, you can use more or less any valid string as the value of the `sep` argument.

## How to Print to a File in Python

Instead of printing things to the terminal, you can also use the `print()` function to print stuff directly to a file. 

The `print()` function takes another argument `file` which defaults to `sys.stdout` or the standard output. It's the default file descriptor where a process can write output.

You can override this to write to a file instead as follows:

```python
with open('output.txt', 'w') as f:
    print('freeCodeCamp', file=f)
```

First, you open a file called `output.txt` as `f` and pass that as the value of the `file` argument. If you run the code a new file will be created and inside that file will be your output.

## Conclusion

The `print()` function is one of the most commonly used functions in Python. So having a good understanding of the different usages of this built-in function can increase your productivity. 

There is also another argument, `flush`, in the function. It's a boolean and setting it to `True` will flush the output on every execution.

I also have a personal blog where I write about random tech stuff, so if you're interested in something like that, checkout [https://farhan.dev](https://farhan.dev). If you have any questions or are confused about anything – or just want to get in touch – I'm available on [Twitter](https://twitter.com/frhnhsin) and [LinkedIn](https://www.linkedin.com/in/farhanhasin/).

