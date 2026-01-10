---
title: How to Debug Your Python Code with the Python Debugger (pdb)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-27T17:50:42.000Z'
originalURL: https://freecodecamp.org/news/debugging-in-python-using-pdb
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/paulius-andriekus-552Vm3_Ah6A-unsplash.jpg
tags:
- name: debugging
  slug: debugging
- name: Python
  slug: python
seo_title: null
seo_desc: "By Jagruti Tiwari\nDebugging tools are at the heart of any programming\
  \ language. \nAnd as a developer, it's hard to make progress and write clean code\
  \ unless you know your way around these tools. \nThis article will help you get\
  \ acquainted with one such..."
---

By Jagruti Tiwari

Debugging tools are at the heart of any programming language. 

And as a developer, it's hard to make progress and write clean code unless you know your way around these tools. 

This article will help you get acquainted with one such tool: [The Python Debugger (pdb)](https://docs.python.org/3/library/pdb.html#:~:text=The%20module%20pdb%20defines%20an,context%20of%20any%20stack%20frame)

Note that this is a debugging tutorial. I assume that you are familiar with at least one programming language, and have an idea about writing test cases.

# How to Get Started with `pdb`
There are two ways to invoke `pdb`:

## 1. Call `pdb` externally

To call `pdb` when on a terminal you can call it while executing your  `.py` file.

```
python -m pdb <test-file-name>.py
```

If you use [poetry](https://python-poetry.org/) and [pytest](https://docs.pytest.org/en/7.1.x/) you can call `pdb` using `--pdb` flag in the end.

```
poetry run python <path/to_your/test_file.py> --pdb
```

To call `pdb` with Docker, `poetry`, and `pytest` you can use the following syntax:

```
COMPOSE_PROJECT_NAME=<test_docker_image_name> docker-compose run --rm workers poetry run pytest <path/to_your/test_file.py>::<name_of_the_test_function> --pdb
```

You will always add the `--pdb` flag after the name of your test file. This will open the `pdb` console when the test breaks. But remember `--pdb` is a `pytest` flag.
 

## 2. Add a breakpoint with `pdb`

There can be cases when you get a false positive(s) in a test. Your test case might pass but you don't get the data you were expecting. 

What if you want to read the raw database query? In that case you can call `pdb` from inside the Python function.

To break into the `pdb` debugger, you need to call `import pdb; pdb.set_trace()` inside your function. 

Let's understand this with a nested function example:

``` 
# file1.py

from . import function3

def function1():
    // logic for function1
    function3()
```


``` 
# file2.py

def function2():
    // logic for function2
    // some database query
```

``` 
# file3.py

from . import function2

def function3():
    // logic for function3
    function2()
    // logic for function3 continues
```

In the above code, one function calls another. 

You want to add a breakpoint in `function2` to understand what is actually happening in the function.

You can add a breakpoint with the following statement:

`import pdb; pdb.set_trace()`

``` 
# file2.py

1. def function2():
2.     // logic for function2
3.     // line 1
4.     // line 2
5.    
6.     import pdb; pdb.set_trace();
7.    
8.     // some database query
9.     // line 3
10.    // line 4
```

`pdb` opens its console when your code breaks. Something like this:

```
(Pdb)
```

When the Python interpreter executes `line2`, it will read the breakpoint and open the `pdb` console. We use `pdb` commands to navigate the code. We will learn these commands in the next section.

# Common `pdb` Commands

`pdb` is an interactive command line debugger. You can't harness its full potential unless you are familiar with its commands. 

Like every other console log, `pdb` will tell you exactly at which line your code breaks.

### The [print](https://docs.python.org/3/library/pdb.html#pdbcommand-p) command

Let's say you have a test case with an `assert` statement. Something like this:

```
# test.py
    
def test1():
    ...
    result = function1()
    assert result.json = {'status_code':1, 'status': 'saved', 'description':'data saved'}
```

You will use the `p` command to print a value to the console.

```
(Pdb) p result.json
{'status_code':1, 'status': 'saved', 'description':'data saved'}
```

This prints the value the variable holds.

### The [up](https://docs.python.org/3/library/pdb.html#pdbcommand-up) command

The up command moves you one frame up the stack. 

In case of nested function calls, it will move you up into the function that called your function.

Let's take an example:

```
# test.py

def function1():
    print("invoking function1")
    import pdb;pdb.set_trace()
    print("function1 invoked")


def function2():
    print("invoking function2")
    function1()
    print("function2 invoked")


def function3():
    print("inside function3")
    function2()
    print("function3 invoked")

# starting the call with function2()
 
function3()
```

In `pdb` we will call it this way:

```
$ python -m pdb test.py

> test.py(1)<module>()
-> def function1():
(Pdb) n
> test.py(7)<module>()
-> def function2():
(Pdb) n
> test.py(13)<module>()
-> def function3():
(Pdb) n
> test.py(20)<module>()
-> function3()
(Pdb) n
inside function3
invoking function2
invoking function1
> test.py(4)function1()
-> print("function1 invoked")
(Pdb) n
function1 invoked
--Return--
> test.py(4)function1()->None
-> print("function1 invoked")
(Pdb) u
> test.py(9)function2()
-> function1()
(Pdb) l
  4         print("function1 invoked")
  5
  6
  7     def function2():
  8         print("invoking function2")
  9  ->     function1()
 10         print("function2 invoked")
 11
 12
 13     def function3():
 14         print("inside function3")
(Pdb) u
> test.py(15)function3()
-> function2()
(Pdb) l
 10         print("function2 invoked")
 11
 12
 13     def function3():
 14         print("inside function3")
 15  ->     function2()
 16         print("function3 invoked")
 17
 18     # starting the call with function2()
 19
 20     function3()
(Pdb) u
> test.py(20)<module>()
-> function3()
(Pdb) l
 15         function2()
 16         print("function3 invoked")
 17
 18     # starting the call with function2()
 19
 20  -> function3()
[EOF]
(Pdb) u
> <string>(1)<module>()
```

Here we start with invoking `function3()`. The execution stops when it encounters `import pdb`.

`pdb` opens the console and waits for the input. We type `u` for up, and it returns the calling function: `function2()`. On the next `u` command it returns `function3` (the function that calls `function2`).

We are using the `l` command. It is the list command. It lists exactly where the current execution line is.

### The [step](https://docs.python.org/3/library/pdb.html#pdbcommand-step) command

To understand the `step` command, let's continue with the previous example.

```
# test.py
    
1. def test1():
2.    ...
3.    result = function1()
4.    assert result.json.status_code == 1
5.    assert result.json.status == 'saved'
6.    assert result.json.description == 'data saved'
7.
```

```
# function_file.py

def function1():
    foo = ['bar']
    ...
```

You suspect that the result returned from `function1()` is incorrect. Your code beaks at line 6. How do you go step into line 3?

You will use the `up` command first and finally step into the function with the `s` command.

```
(Pdb) u
assert result.json.status == 'saved'
(Pdb) u
assert result.json.status_code == 1
(Pdb) p assert result.json.status_code
1
(Pdb) u
result = function1()
(Pdb) s
(Pdb) n
foo = ['bar']
```

When you step into `function1()`, the `pdb` console will start to print statements from that function.

# Conclusion

`pdb` is a powerful debugger. This tutorial intends to get you familiar with `pdb` basics. 

I recommend reading [its documentation](https://docs.python.org/3/library/pdb.html) to explore the full potential.


