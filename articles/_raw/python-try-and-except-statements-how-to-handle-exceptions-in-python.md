---
title: Python Try and Except Statements – How to Handle Exceptions in Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-09-23T21:00:47.000Z'
originalURL: https://freecodecamp.org/news/python-try-and-except-statements-how-to-handle-exceptions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/try-except.png
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "When coding in Python, you can often anticipate runtime errors even in\
  \ a syntactically and logically correct program. These errors can be caused by invalid\
  \ inputs or some predictable inconsistencies. \nIn Python, you can use the try and\
  \ the except blo..."
---

When coding in Python, you can often anticipate runtime errors even in a syntactically and logically correct program. These errors can be caused by invalid inputs or some _predictable_ inconsistencies. 

In Python, you can use the `try` and the `except` blocks to handle most of these errors as _exceptions_ all the more gracefully.

In this tutorial, you'll learn the general syntax of `try` and `except`. Then we'll proceed to code simple examples, discuss what can go wrong, and provide corrective measures using `try` and `except` blocks.

## Syntax of Python Try and Except Blocks

Let's start by understanding the syntax of the `try` and `except` statements in Python. The general template is shown below:

```
try:
	# There can be errors in this block
    
except <error type>:
	# Do this to handle exception;
	# executed if the try block throws an error
    
else:
	# Do this if try block executes successfully without errors
   
finally:
	# This block is always executed

```

Let's look at what the different blocks are used for:

* The `try` block is the block of statements you'd like to try executing. However, there may be runtime errors due to an exception, and this block may fail to work as intended.
* The `except` block is triggered when the `try` block fails due to an exception. It contains a set of statements that often give you some context on what went wrong inside the `try` block.
* You should always mention the _type_ of _error_ that you intend to catch as exception inside the `except` block, denoted by the placeholder `<error type>` in the above snippet. 
* You might as well use `except` without specifying the `<error type>`. But, this is not a recommended practice as you're not accounting for the different types of errors that can occur.

> In trying to execute the code inside the `try` block, there's also a possibility for multiple errors to occur.

For example, you may be accessing a list using an index that's way out of range, using a wrong dictionary key, and trying to open a file that does not exist - all inside the `try` block.

In this case, you may run into `IndexError`, `KeyError`, and `FileNotFoundError`. And you have to add as many `except` blocks as the number of errors that you anticipate, one for each type of error.

* The `else` block is triggered only if the `try` block is executed without errors. This can be useful when you'd like to take a follow-up action when the `try` block succeeds. For example, if you try and open a file successfully, you may want to read its content.
* The `finally` block is always executed, regardless of what happens in the other blocks. This is useful when you'd like to free up resources after the execution of a particular block of code.

> **Note**: The `else` and `finally` blocks are _optional._ In most cases, you can use only the `try` block to try doing something, and catch errors as exceptions inside the `except` block.

Over the next few minutes, you'll use what you've learned thus far to handle exceptions in Python. Let's get started.

## How to Handle a `ZeroDivisionError` in Python

Consider the function `divide()` shown below. It takes two arguments – `num` and `div` – and returns the quotient of the division operation `num/div`.

```python
def divide(num,div):
  return num/div
```

▶ Calling the function with different numbers returns results as expected:

```python
res = divide(100,8)
print(res)

# Output
12.5

res = divide(568,64)
print(res)

# Output
8.875

```

This code works fine until you try dividing by zero:

```python
divide(27,0)


```

You see that the program crashes throwing a `ZeroDivisionError`:

```
# Output
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-19-932ea024ce43> in <module>()
----> 1 divide(27,0)

<ipython-input-1-c98670fd7a12> in divide(num, div)
      1 def divide(num,div):
----> 2   return num/div

ZeroDivisionError: division by zero

```

You can handle this division by zero as an exception by doing the following:

* In the `try` block, place a call to the `divide()` function. In essence, you're trying to divide `num` by `div`.
* Handle the case when `div` is `0` as an exception inside the `except` block.
* In this example, you can except `ZeroDivisionError` by printing a message informing the user that they tried dividing by zero.

This is shown in the code snippet below:

```python
try:
    res = divide(num,div)
    print(res)
except ZeroDivisionError:
    print("You tried to divide by zero :( ")

```

With a valid input, the code still works fine.

```python
divide(10,2)
# Output
5.0

```

When you try diving by zero, you're notified of the exception that occurs, and the program ends gracefully.

```python
divide(10,0)
# Output
You tried to divide by zero :(

```

## How to Handle a `TypeError` in Python

In this section, you'll see how you can use `try` and `except` to handle a `TypeError` in Python.

▶ Consider the following function `add_10()` that takes in a number as the argument, adds 10 to it, and returns the result of this addition.

```python
def add_10(num):
  return num + 10
```

You can call the function `add_10()` with any number and it'll work fine, as shown below:

```python
result = add_10(89)
print(result)

#Output
99
```

Now try calling `add_10()` with `"five"` instead of `5`.

```python
add_10("five")
```

You'll notice that your program crashes with the following error message:

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-9844e949c84e> in <module>()
----> 1 add_10("five")

<ipython-input-13-2e506d74d919> in add_10(num)
      1 def add_10(num):
----> 2   return num + 10

TypeError: can only concatenate str (not "int") to str
```

The error message `TypeError: can only concatenate str (not "int") to str` explains that you can only concatenate two strings, and not add an integer to a string.

Now, you have the following:

* Given a number `my_num`, _try_ calling the function `add_10()` with `my_num` as the argument. If the argument is of valid type, there's no exception
* Otherwise, the `except` block corresponding to the `TypeError` is triggered, notifying the user that the argument is of invalid type.

This is explained below:

```python
my_num = "five"
try:
  result = add_10(my_num)
  print(result)
except TypeError:
  print("The argument `num` should be a number")
```

Since you've now handled `TypeError` as an exception, you're only informed that the argument is of invalid type.

```
The argument `num` should be a number
```

## How to Handle an `IndexError` in Python

If you've worked with Python lists, or any Python iterable before, you'll have probably run into `IndexError`. 

This is because it's often difficult to keep track of all changes to iterables. And you may be trying to access an item at an index that's not valid.

▶ In this example, the list `my_list` has 4 items. The valid indices are 0, 1, 2, and 3, and -1, -2, -3, -4 if you use negative indexing.

As `2` is a valid index, you see that the item at index `2`, which is `C++`, is printed out:

```python
my_list = ["Python","C","C++","JavaScript"]
print(my_list[2])

#Output
C++
```

If you try accessing an item at index that's outside the range of valid indices, you'll run into an `IndexError`:

```python
print(my_list[4])
```

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-7-437bc6501dea> in <module>()
      1 my_list = ["Python","C","C++","JavaScript"]
----> 2 print(my_list[4])

IndexError: list index out of range
```

If you're familiar with the pattern, you'll now use `try` and `except` to handle index errors.

▶ In the code snippet below, you try accessing the item at the index specified by `search_idx`. 

```python
search_idx = 3
try:
  print(my_list[search_idx])
except IndexError:
  print("Sorry, the list index is out of range")
```

Here, the `search_idx` (`3`) is a valid index, and the item at the particular index is printed out:

```
JavaScript
```

If the `search_idx` is outside the valid range for indices, the except block catches the `IndexError` as an exception, and there are no more long error messages. 🙂

```python
search_idx = 4
try:
  print(my_list[search_idx])
except IndexError:
  print("Sorry, the list index is out of range")
```

Rather, the message that the `search_idx` is out of the valid range of indices is displayed:

```
Sorry, the list index is out of range
```

## How to Handle a `KeyError` in Python

You have likely run into `KeyError` when working with Python dictionaries

▶ Consider this example where you have a dictionary `my_dict`.

```python
my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
search_key = "non-existent key"
print(my_dict[search_key])
```

* The dictionary `my_dict` has 3 key-value pairs, `"key1:value1"`, `"key2:value2"`, and `"key3:value3"`
* Now, you try to tap into the dictionary and access the value corresponding to the key `"non-existent key"`.

As expected, you'll get a `KeyError`:

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-2a61d404be04> in <module>()
      1 my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
      2 search_key = "non-existent key"
----> 3 my_dict[search_key]

KeyError: 'non-existent key'
```

You can handle `KeyError` in almost the same way you handled `IndexError`.

* You can try accessing the value corresponding to the key specified by the `search_key`.
* If `search_key` is indeed a valid key, the corresponding value is printed out.
* If you run into an exception because of a non-existent key, you use the `except` block to let the user know.

This is explained in the code snippet below:

```python
try:
  print(my_dict[search_key])
except KeyError:
  print("Sorry, that's not a valid key!")
```

```
Sorry, that's not a valid key!
```

▶ If you want to provide additional context such as the name of the invalid key, you can do that too. It's possible that the key was misspelled which made it invalid. In this case, letting the user know the key used will probably help them fix the typo. 

You can do this by catching the invalid key as `<error_msg>` and use it in the message printed when the exception occurs:

```python
try:
  print(my_dict[search_key])
except KeyError as error_msg:
  print(f"Sorry,{error_msg} is not a valid key!")
```

▶ Notice how the name of the key is also printed out:

```
Sorry,'non-existent key' is not a valid key!
```

## How to Handle a `FileNotFoundError` in Python

Another common error that occurs when working with files in Python is the `FileNotFoundError`.

▶ In the following example, you're trying to open the file `my_file.txt` by specifying its path to the function `open()`. And you'd like to read the file and print out the contents of the file.

However, you haven't yet created the file in the specified location.

If you try running the code snippet below, you'll get a `FileNotFoundError`:

```python
my_file = open("/content/sample_data/my_file.txt")
contents = my_file.read()
print(contents)
```

```
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-4-4873cac1b11a> in <module>()
----> 1 my_file = open("my_file.txt")

FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
```

And using `try` and `except`, you can do the following:

* Try opening the file in the `try` block.
* Handle `FileNotFoundError` in the `except` block by letting the user know that they tried to open a file that doesn't exist.
* If the `try` block succeeds, and the file does exist, read and print out the contents of the file.
* In the `finally` block, close the file so that there's no wastage of resources. Recall how the file will be closed regardless of what happens in the file opening and reading steps.

```python
try:
  my_file = open("/content/sample_data/my_file.txt")
except FileNotFoundError:
  print(f"Sorry, the file does not exist")
else:
  contents = my_file.read()
  print(contents)
finally:
  my_file.close()
```

Notice how you've handled the error as an exception and the program ends gracefully displaying the message below:

```
Sorry, the file does not exist
```

▶ Let's consider the case in which the `else` block is triggered. The file `my_file.txt` is now present at the path mentioned earlier.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-77.png)

And here's what the file `my_file.txt` contains:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-78.png)

Now, re-running the earlier code snippet works as expected.

This time, the file `my_file.txt` is present, the `else` block is triggered and its contents are printed out, as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-80.png)

I hope this clarifies how you can handle exceptions when working with files.

## Conclusion

In this tutorial, you've learned how you can use `try` and `except` statements in Python to handle exceptions. 

You coded examples to understand what types of exception may occur and how you can use `except` to catch the most common errors.

Hope you enjoyed this tutorial. Happy coding! Until next time :)

