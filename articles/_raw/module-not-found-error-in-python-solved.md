---
title: 'ModuleNotFoundError: no module named Python Error [Fixed]'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-12T14:17:11.000Z'
originalURL: https://freecodecamp.org/news/module-not-found-error-in-python-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/module-not-found-error.png
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  When you try to import a module in a Python file, Python tries to resolve this module
  in several ways. Sometimes, Python throws the ModuleNotFoundError afterward. What
  does this error mean in Python?

  As the name implies, this error ...'
---

By Dillion Megida

When you try to import a module in a Python file, Python tries to resolve this module in several ways. Sometimes, Python throws the **ModuleNotFoundError** afterward. What does this error mean in Python?

As the name implies, this error occurs when you're trying to access or use a module that cannot be found. In the case of the title, the "module named **Python**" cannot be found.

*Python* here can be any module. Here's an error when I try to import a `numpys` module that cannot be found:

```python
import numpys as np
```

Here's what the error looks like:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-341.png)

Here are a few reasons why a module may not be found:

- you do not have the module you tried importing installed on your computer
- you spelled a module incorrectly (which still links back to the previous point, that the misspelled module is not installed)...for example, spelling `numpy` as `numpys` during import
- you use an incorrect casing for a module (which still links back to the first point)...for example, spelling `numpy` as `NumPy` during import will throw the module not found error as both modules are "not the same"
- you are importing a module using the wrong path

## How to fix the ModuleNotFoundError in Python

As I mentioned in the previous section, there are a couple of reasons a module may not be found. Here are some solutions.

### 1. Make sure imported modules are installed

Take for example, `numpy`. You use this module in your code in a file called "test.py" like this:

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

If you try to run this code with `python test.py` and you get this error:

```bash
ModuleNotFoundError: No module named "numpy"
```

Then it's most likely possible that the `numpy` module is not installed on your device. You can install the module like this:

```python
python -m pip install numpy
```

When installed, the previous code will work correctly and you get the result printed in your terminal:

```bash
[1, 2, 3]
```

### 2. Make sure modules are spelled correctly

In some cases, you may have installed the module you need, but trying to use it still throws the ModuleNotFound error. In such cases, it could be that you spelled it incorrectly. Take, for example, this code:

```python
import nompy as np

arr = np.array([1, 2, 3])

print(arr)
```

Here, you have installed `numpy` but running the above code throws this error:

```bash
ModuleNotFoundError: No module named "nompy"
```

This error comes as a result of the misspelled `numpy` module as `nompy` (with the letter **o** instead of **u**). You can fix this error by spelling the module correctly.

### 3. Make sure modules are in the right casing

Similar to the misspelling issue for module not found errors, it could also be that you are spelling the module correctly, but in the wrong casing. Here's an example:

```python
import Numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

For this code, you have `numpy` installed but running the above code will throw this error:

```bash
ModuleNotFoundError: No module named 'Numpy'
```

Due to casing differences, `numpy` and `Numpy` are different modules. You can fix this error by spelling the module in the right casing.

### 4. Make sure you use the right paths

In Python, you can import modules from other files using **absolute** or **relative** paths. For this example, I'll focus on absolute paths.

When you try to access a module from the wrong path, you will also get the module not found here. Here's an example:

Let's say you have a project folder called **test**. In it, you have two folders **demoA** and **demoB**.

**demoA** has an `__init__.py` file (to show it's a Python package) and a `test1.py` module.

**demoA** also has an `__init__.py` file and a `test2.py` module.

Here's the structure:

```bash
└── test
    ├── demoA
        ├── __init__.py
    │   ├── test1.py
    └── demoB
        ├── __init__.py
        ├── test2.py
```

Here are the contents of `test1.py`:

```python
def hello():
  print("hello")
```

And let's say you want to use this declared `hello` function in `test2.py`. The following code will throw a module not found error:

```python
import demoA.test as test1

test1.hello()
```

This code will throw the following error:

```bash
ModuleNotFoundError: No module named 'demoA.test'
```

The reason for this is that we have used the wrong path to access the `test1` module. The right path should be `demoA.test1`. When you correct that, the code works:

```python
import demoA.test1 as test1

test1.hello()
# hello
```

## Wrapping up

For resolving an imported module, Python checks places like the inbuilt library, installed modules, and modules in the current project. If it's unable to resolve that module, it throws the **ModuleNotFoundError**.

Sometimes you do not have that module installed, so you have to install it. Sometimes it's a misspelled module, or the naming with the wrong casing, or a wrong path. In this article, I've shown four possible ways of fixing this error if you experience it.

I hope you learned from it :)



