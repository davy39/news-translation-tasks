---
title: How to Make a Time Delay in Python Using the sleep() Function
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T20:07:00.000Z'
originalURL: https://freecodecamp.org/news/time-delay-python-sleep-function
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e0d740569d1a4ca3b11.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'There are times when you want your program to run immediately. But there
  are also some times when you want to delay the execution of certain pieces of code.

  That''s where Python''s time module comes in. time is part of Python''s standard
  library, and co...'
---

There are times when you want your program to run immediately. But there are also some times when you want to delay the execution of certain pieces of code.

That's where Python's `time` module comes in. `time` is part of Python's standard library, and contains the helpful `sleep()` function that suspends or pauses a program for a given number of seconds:

```text
import time

print('runs immediately')

for letter in 'hello, world!':
    time.sleep(2)  # sleep 2 seconds between each print
    print(letter)
```

**Output:**

```
runs immediately
h # each character printed after a two second delay
e
l
l
o
,

w
o
r
l
d
!
```

Floating point numbers can be given as the argument to `sleep()` for more precise sleep times. For example, the following code will delay each `print()` statement for half a second, or 500 ms:

```py
import time

for letter in 'floats work, too':
  time.sleep(0.5) # adds a 500 ms delay
  print(letter)
```

**Output:**

```
f # each character printed after a 500 ms delay
l
o
a
t
s

w
o
r
k
,

t
o
o
```

Sometimes you might need to delay for known, different increments of time. In that case you can iterate through a list of different delay periods with a `for` loop:

```py
import time

for i in [.5, 1, 2, 3, 4]:
  time.sleep(i)
  print(f"Delayed for {i} seconds")
```

**Output:**

```
Delayed for 0.5 seconds
Delayed for 1 seconds
Delayed for 2 seconds
Delayed for 3 seconds
Delayed for 4 seconds
```

As you can imagine, there's a lot that you can do with the `sleep()` function. Now go ahead and try it in your own programs – no need to sleep on it!

#### **More Information:**

Time module [documentation](https://docs.python.org/3/library/time.html#time.sleep) on the sleep function.

## More Python tutorials:

[The best Python tutorials](https://www.freecodecamp.org/news/best-python-tutorial/)

[The best Python code examples](https://www.freecodecamp.org/news/python-example/)

[Python for Everybody from Dr. Chuck](https://www.freecodecamp.org/news/python-for-everybody/)

