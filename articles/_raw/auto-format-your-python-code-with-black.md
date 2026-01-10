---
title: How to Auto-Format Your Python Code with Black
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-12T17:25:57.000Z'
originalURL: https://freecodecamp.org/news/auto-format-your-python-code-with-black
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b14740569d1a4ca2991.jpg
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Davis David

  Writing Python code is one thing and writing the code in a good format is another
  thing. Junior programmers often focus on making sure their code is working and forget
  to format the code properly along the way.

  If you write a small pro...'
---

By Davis David

Writing Python code is one thing and writing the code in a good format is another thing. Junior programmers often focus on making sure their code is working and forget to format the code properly along the way.

If you write a small program (with 1000 lines of codes) you can probably get away without formatting your code. 

But as programs get more and more complex, they get harder and harder to understand. At some point (around 15,000 lines of code), it becomes harder to understand the code that you yourself wrote.

The difference between working on well-formatted code and working on badly formatted code is like the difference between living in a palace and living in a dirty house.

# **Why formatting your python code is important**

### Readability

Formatting your code will help you **read** your code **efficiently**. It looks more organized, and when someone looks at your code they'll get a good impression.

### It will help in your coding interviews

When you're in a coding interview, sometime the interviewers will care if you’re formatting your code properly. If you forget to do that formatting you might lose your job prospects, just because of your poorly formatted code.

### Team support

Formatting your code becomes more important when you are working in a **team**. Several people will likely be working on the same software project and code you write must be understood by your teammates. Otherwise it becomes harder to work together.

### It makes it easy to spot bugs

Badly formatted code can make it really, really hard to spot bugs or even to work on a program. It is also just really horrible to look at. _It’s an offense to your eyes._

# Pylint and Flake8

Most Python developers enjoy using [Pylint](https://www.pylint.org/) or [Flake8](http://flake8.pycqa.org/en/latest/) to check their code for errors and style guides.

**Pylint** is a tool that checks for errors in Python. It tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored, and can offer you details about the code’s complexity.

**Flake8** is a Python library that wraps **PyFlakes**, **pycodestyle** and **Ned Batchelder’s McCabe script**. It is a great toolkit for checking your code base against coding style **(PEP8)**, programming errors like “library imported but unused”, “Undefined name” and code which is not indented.

The problem is that these tools only report the problems they identify in the source code and leave the burden to the Python developers to fix them! 

But what if we had a tool that could identify and solve the problem at the same time? **Black** is a tool that allows you to **identify errors** and **format your python code** at the same time. Thus it makes you more productive.

# **Introduction to Black**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_bxzXidSUpkEaj7j0rC5ygg.png)
_Black Logo_

From the project README:

> _By using _Black_, you agree to cede control over minutiae of hand-formatting. In return, _Black_ gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters._

Black can reformat your entire file in place according to the Black code style. It helps your brain focus on the problem you want to solve and code solutions, rather than getting distracted by code structure and minor stylistic differences.

So let's see how to use it.

### Install Black

Black can be installed by running `pip install black`. It requires Python 3.6.0+ to run. Once Black is installed, you will have a new command-line tool called black available to you in your shell, and you’re ready to start!

To get started right away with sensible defaults, choose the python file you want to format and then write **black filename.py** in the terminal. Then Black will format your python file.

Now we'll see what Black can help us do.

### Format a Single File

Let's look at this simple example: here are my two python functions in my python file called sample_code.py.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_OKkCLUmuspv8IHiU25NVTw.png)
_sample_code.py_

You can use `black sample_code.py` in the terminal to change the format. After running Black, you will see the following output:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/d.png)

Then you can open sample_code.py to see formatted python code:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/e.png)

The Python code is now formatted and it’s more readable.

### Format Multiple Files

To format more than one python file, write `black folder_name/` in the terminal.

![Image](https://miro.medium.com/max/30/1*VLyk0_7wCnKFOEYPRBpABg.png?q=20)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/f.png)
_Format all python files inside the folder_

Three python files within the folder named python_with_black have been reformatted.

### Checking Files for Formatting

If you don’t want Black to change your file, but you want to know if Black thinks a file should be changed, you can use one of the following commands:

`black --check .`: This will check which python file(s) can be formatted in the current folder (but doesn’t actually modify the python file(s)).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/g.png)
_Check file(s) to format_

`black --check --diff file_name.py` : This shows what needs to be done to the file but doesn’t modify the file.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/h.png)
_check diff after formatting_

### Change Number of Characters per Line

Note that Black defaults to 88 characters for its line length, but you can change that using the “-l” or “- -line-length” option.

For example, to change to 60 characters: `black -l 60 python_file.py` .

# Black in Jupyter Notebook

For Jupyter notebook users, you can still auto-format your python code with this simple extension called [Jupyter Black](https://github.com/drillan/jupyter-black). This extension reformats/prettifies code in a notebook’s code cell by [black](https://black.readthedocs.io/en/stable/).

The Jupyter Black extension provides

* A toolbar button.
* A keyboard shortcut for reformatting the current code-cell (default: Ctrl-B).
* A keyboard shortcut for reformatting whole code-cells (default: Ctrl-Shift-B).

### Install Jupyter Black

First make sure you have installed [jupyter-contrib-nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) and [black](https://black.readthedocs.io/en/stable/), then run the following commands.

```
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip — user
```

Then enable the extension by running:

```
jupyter nbextension enable jupyter-black-master/jupyter-black

```

Now you can start formatting your python code in each notebook cell. 

First, select the notebook cell you want to format your python code then click the extension button called Black.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/i.png)
_Before using Jupyter Black_

Then click the Jupyter Black button:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/j.png)
_Jupyter Black Button_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/k.png)
_After using Jupyter Black_

# Editor Integration

You can integrate Black with your favorite editors. Currently Black supports PyCharm/IntelliJ IDEA, Wing IDE, Vim, Visual Studio Code, Sublime Text 3, Atom/Nuclide, Kakoune, and Thonny. Follow the instruction [here](https://black.readthedocs.io/en/latest/editor_integration.html) to integrate Black with your favorite editor.

If you want to learn more about Black, I recommend watching the [PyCon 2019 talk](https://youtu.be/esZLCuWs_2Y) by Łukasz Langa.

If you learned something new or enjoyed reading this article, please share it so that others can see it. Until then, see you in the next post! I can also be reached on Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).

