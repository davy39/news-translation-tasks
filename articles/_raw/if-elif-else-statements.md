---
title: If, Elif, and Else Statements in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T23:32:00.000Z'
originalURL: https://freecodecamp.org/news/if-elif-else-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e09740569d1a4ca3afe.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'If Elif Else Statements

  The if/elif/else structure is a common way to control the flow of a program, allowing
  you to execute specific blocks of code depending on the value of some data.

  if statement

  If the condition following the keyword if evaluates...'
---

## **If Elif Else Statements**

The `if`/`elif`/`else` structure is a common way to control the flow of a program, allowing you to execute specific blocks of code depending on the value of some data.

### if statement 

If the condition following the keyword `if` evaluates as `true`, the block of code will execute. Note that parentheses are not used before and after the condition check as in other languages.

```python
if True:
  print('If block will execute!')
```

```python
x = 5

if x > 4:
  print("The condition was true!") #this statement executes
```

### else statement

You can optionally add an `else` response that will execute if the condition is `false`:

```python
if not True:
  print('If statement will execute!')
else:
  print('Else statement will execute!')
```

Or you can also see this example:

```python
y = 3

if y > 4:
  print("I won't print!") #this statement does not execute
else:
  print("The condition wasn't true!") #this statement executes
```

_Note that there is no condition following the `else` keyword - it catches all situations where the condition was `false`_

### elif statement

Multiple conditions can be checked by including one or more `elif` checks after your initial `if` statement. Just keep in mind that only one condition will execute:

```python
z = 7

if z > 8:
  print("I won't print!") #this statement does not execute
elif z > 5:
  print("I will!") #this statement will execute
elif z > 6:
  print("I also won't print!") #this statement does not execute
else:
  print("Neither will I!") #this statement does not execute
```

_Note: only the first condition that evaluates as `true` will execute._ Even though `z > 6` is `true`, the `if/elif/else` block terminates after the first true condition. This means that an `else` will only execute if none of the conditions were `true`.

### Nested if statements

We can also create nested if’s for decision making. Before preceding please refer to the href=’[https://guide.freecodecamp.org/python/code-blocks-and-indentation](https://guide.freecodecamp.org/python/code-blocks-and-indentation)’ target=’_blank’ rel=‘nofollow’>indentation guide once before preceding.

Let’s take an example of finding a number which is even and also greater than 10

```text
python 
x = 34
if x %  2 == 0:  # this is how you create a comment and now, checking for even.
  if x > 10:
    print("This number is even and is greater than 10")
  else:
    print("This number is even, but not greater 10")
else:
  print ("The number is not even. So point checking further.")
```

This was just a simple example for nested if’s. Please feel free to explore more online.

While the examples above are simple, you can create complex conditions using [boolean comparisons](https://guide.freecodecamp.org/python/comparisons) and [boolean operators](https://guide.freecodecamp.org/python/boolean-operations).

### Inline python if-else statement

We can also use if-else statements inline python functions. The following example should check if the number is greater or equal than 50, if yes return True:

```text
python 
x = 89
is_greater = True if x >= 50 else False

print(is_greater)
```

Output

```text
>
True
>
```

## More info on if/elif/else statements:

* [How to get out of if/else hell](https://www.freecodecamp.org/news/so-youre-in-if-else-hell-here-s-how-to-get-out-of-it-fc6407fec0e/)
* [If/else in JavaScript](https://www.freecodecamp.org/news/javascript-essentials-how-to-make-life-decisions-with-if-else-statements-1908ff7cf5da/)


