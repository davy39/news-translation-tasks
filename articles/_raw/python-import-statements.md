---
title: Python Import Statements Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-14T19:25:00.000Z'
originalURL: https://freecodecamp.org/news/python-import-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c95740569d1a4ca3304.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'While learning programming and reading some resources you’d have come across
  this word ‘abstraction’ which simply means to reduce and reuse the code as much
  as possible.

  Functions and Modules facilitate abstraction. You create functions when you want...'
---

While learning programming and reading some resources you’d have come across this word ‘abstraction’ which simply means to reduce and reuse the code as much as possible.

Functions and Modules facilitate abstraction. You create functions when you want to do something repeatedly within a file.

Modules come into picture when you want to reuse a group of functions in different source files. Modules are also useful in structuring the program well.

* Using Standard Libraries and other third party modules
* Structuring the program

## **Using Standard Libraries**

Example: You can read about the methods/functions of all the standard libraries in the official Python Docs in detail.

```text
import time
for i in range(100):
    time.sleep(1)   # Waits for 1 second and then executes the next command
    print(str(i) + ' seconds have passed')  # prints the number of seconds passed after the program was started
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/CS6C)

```text
# To calculate the execution time of a part of program
import time
start = time.time()
# code here
end = time.time()
print('Execution time:' , end-start)
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/CS6C/1)

```text
# Using math Module
import math
print(math.sqrt(100))   # prints 10
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/CS6C/2)

## **Using third party Modules**

Third party modules don’t come bundled with python , but we have to install it externally using package managers like [`pip`](https://bootstrap.pypa.io/get-pip.py) and [`easy install`](https://bootstrap.pypa.io/ez_setup.py)

```text
# To make http requests
import requests
rq = requests.get(target_url)
print(rq.status_code)
```

Find out more about python-requests module [here](http://docs.python-requests.org/en/master/)

## **To structure programs**

We want to make a program that has various functions regarding prime numbers. So lets start. We will define all the functions in `prime_functions.py`

```text
# prime_functions.py
from math import ceil, sqrt
def isPrime(a):
    if a == 2:
        return True
    elif a % 2 == 0:
        return False
    else:
        for i in range(3,ceil(sqrt(a)) + 1,2):
            if a % i == 0:
                return False
        return True

def print_n_primes(a):
    i = 0
    m = 2
    while True:
        if isPrime(m) ==True:
            print(m)
            i += 1
        m += 1
        if i == a:
            break
```

Now we want to use the functions that we just created in `prime_functions.py` so we create a new file `playground.py` to use those functions.

_Please note that this program is far too simple to make two separate files, it is just to demonstrate. But when there are large complex programs, making different files is really useful._

```text
# playground.py
import prime_functions
print(prime_functions.isPrime(29)) # returns True
```

## **Sorting Imports**

Good practice is to sort `import` modules in three groups - standard library imports, related third-party imports, and local imports. Within each group it is sensible to sort alphabetically by module name. You can find [more information in PEP8](https://www.python.org/dev/peps/pep-0008/?#imports).

One of the most important thing for Python language is legibility, and alphabetically sorting modules are quicker to read and search. Also it is easier to verify that something is imported, and avoid duplicated imports.

## From X import Y: an example

Here's an example problem:

```text
>>> from math import ceil, sqrt
>>> # here it would be
>>> sqrt(36)
<<< 6
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/CS5t/1)

Or we could use this one instead:

```text
>>> import math
>>> # here it would be
>>> math.sqrt(36)
<<< 6
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/CS5u)

Then our code would look like `math.sqrt(x)` instead of `sqrt(x)`. This happens because when we use `import x`, a namespace `x` is itself created to avoid name conflicts. You have to access every single object of the module as `x.<name>`. 

But when we use `from x import y` we agree to add `y` to the main global namespace. So while using this we have to make sure that we don’t have an object with same name in our program.

**Never use `from x import y` if an object named `y` already exists**

For example, in `os` module there’s a method `open`. But we even have a built-in function called `open`. So, here we should avoid using `from os import open`.

We can even use `form x import *`, this would import all the methods, classes of that module to the global namespace of the program. This is a bad programming practice. Please avoid it.

In general you should avoid `from x import y` simply because of the problems it may cause in large scale programs. For example, you never know if a fellow programmer might want to make a new function that happens to be the name of one of the existing functions. You also do not know whether Python will change the library that you are importing functions from. While these problems won’t exist as often for solo projects, as stated before, it is bad programming practice and should be avoided.

