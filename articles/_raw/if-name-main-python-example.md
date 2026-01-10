---
title: Python if __name__ == __main__ Explained with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-03T19:48:00.000Z'
originalURL: https://freecodecamp.org/news/if-name-main-python-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99de740569d1a4ca2229.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Goran Aviani\nWhen a Python interpreter reads a Python file, it first\
  \ sets a few special variables. Then it executes the code from the file. \nOne of\
  \ those variables is called __name__.\nIf you follow this article step-by-step and\
  \ read its code snipp..."
---

By Goran Aviani

When a Python interpreter reads a Python file, it first sets a few special variables. Then it executes the code from the file. 

One of those variables is called `__name__`.

If you follow this article step-by-step and read its code snippets, you will learn how to use `if __name__ == "__main__"`, and why it's so important.

## Python Modules Explained

Python files are called modules and they are identified by the `.py` file extension. A module can define functions, classes, and variables.

So when the interpreter runs a module, the `__name__` variable will be set as  `__main__` if the module that is being run is the main program.

But if the code is importing the module from another module, then the `__name__`  variable will be set to that module’s name.

Let's take a look at an example. Create a Python module named `file_one.py` and paste this top level code inside:

```python
# Python file one module

print("File one __name__ is set to: {}" .format(__name__))
```

By running this file you will see exactly what we were talking about. The variable `__name__` for this module is set to `__main__`:

```
File one __name__ is set to: __main__
```

Now add another file named `file_two.py` and paste this code inside:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

```

Also, modify the code in `file_one.py` like this so we import the `file_two` module:

```python
# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))

```

Running our `file_one` code once again will show that the `__name__` variable in the `file_one` did not change, and still remains set to `__main__`. But now the variable `__name__` in `file_two` is set as its module name, hence `file_two`.

The result should look like this:

```
File two __name__ is set to: file_two
File one __name__ is set to: __main__

```

But run `file_two` directly and you will see that its name is set to `__main__`:

```
File two __name__ is set to: __main__


```

The variable `__name__` for the file/module that is run will be always `__main__`. But the `__name__` variable for all other modules that are being imported will be set to their module's name.

## Python File Naming Conventions

The usual way of using `__name__` and `__main__` looks like this:

```python
if __name__ == "__main__":
   Do something here


```

Let's see how this works in real life, and how to actually use these variables. 

Modify `file_one` and `file_two` to look like this:

`file_one`:

```python
# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")

```

`file_two`:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")

```

Again, when running `file_one` you will see that the program recognized which of these two modules is `__main__` and executed the code according to our first `if else` statements.

The result should look like this:

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly

```

Now run `file_two` and you will see that the `__name__` variable is set to `__main__`:

```
File two __name__ is set to: __main__
File two executed when ran directly

```

When modules like this are being imported and run, their functions will be imported, and top level code executed. 

To see this process in action, modify your files to look like this:

`file_one`:

```python
# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")

```

`file_two`:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")

```

Now the functions are loaded but not run. 

To run one of these functions modify the `if __name__ == "__main__"` part of `file_one` to look like this:

```python
if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
else:
   print("File one executed when imported")

```

When running `file_one` you should see should be like this:

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed

```

Also, you can run functions from imported files. To do that, modify the `if __name__ == “__main__”` part of `file_one` to look like this:

```python
if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   file_two.function_three()
else:
   print("File one executed when imported")

```

And you can expect a result like this:

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed
Function three is executed

```

Now let's say the `file_two` module is really big with lot of functions (two in our case), and you don't want to import all of them. Modify `file_two` to look like this:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

def function_four():
   print("Function four is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")

```

And to import the specific functions from the module, use the `from` import block in the `file_one` file:

```python
# Python module to execute
from file_two import function_three

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   function_three()
else:
   print("File one executed when imported")
```

## Conclusion

There is a really nice use case for the `__name__` variable, whether you want a file that can be run as the main program or imported by other modules. We can use an `if __name__ == "__main__"` block to allow or prevent parts of code from being run when the modules are imported.

When the Python interpreter reads a file, the `__name__` variable is set as `__main__` if the module being run, or as the module's name if it is imported. Reading the file executes all top level code, but not functions and classes (since they will only get imported).

Bra gjort! (That means "Well done" in Swedish!)

Check out more articles like this on my [freeCodeCamp profile](https://www.freecodecamp.org/news/author/goran/), [Medium profile](https://medium.com/@goranaviani), and other fun stuff I build on my [GitHub page](https://github.com/GoranAviani).

