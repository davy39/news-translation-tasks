---
title: pip Command Not Found – Mac and Linux Error Solved
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-03T18:14:36.000Z'
originalURL: https://freecodecamp.org/news/pip-command-not-found-mac-and-linux-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pip.png
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "When using Python, you might need to install and use certain packages.\
  \ And there is a command available for that known as 'pip'. \nWith pip, you can\
  \ install, upgrade, and uninstall various Python packages. You'll learn how to use\
  \ it, and how to handle..."
---

When using Python, you might need to install and use certain packages. And there is a command available for that known as 'pip'. 

With pip, you can install, upgrade, and uninstall various Python packages. You'll learn how to use it, and how to handle pip errors, in this article.

## How to use pip

Pip is a command that you can use on the Linux or Mac command line. You can select a package from [here](https://pypi.org/). 

Below is an example of how you would install the `mock-open` package with `pip`. 

```python
pip3 install mock-open
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image.png)

As this package was already installed, we are getting the message that the requirement is already met.

Note that I have used pip3 because I am using Python3. We'll discuss this in detail later.

## What is the error `pip: command not found`?

Sometimes when you are installing packages, you might face the error: **`pip: command not found`**. This error could be due to the following reasons:

1. Pip is not installed.
2. Pip is installed, but it is not compatible with the current environment.

On Linux, you must install the pip package manager separately as it is an independent package. But on Mac, you do not need to install pip manually, as long as you are working with Python 3.x.

### Troubleshooting the error **`pip: command not found`**

1. **Check if pip is installed.**

On Mac and Linux, you can use the below command to check if pip is installed.

```
 python3 -m pip --version 
```

![pip installed](https://www.freecodecamp.org/news/content/images/2022/03/image-1.png)
_Here's the output if pip is installed correctly_

If pip is not installed, you can follow the install steps [here](https://pip.pypa.io/en/stable/installation/) for your respective OS.

**2. Upgrade pip to the latest version**

If pip is still not working, try to upgrade pip to the latest version:

```
python -m pip install --upgrade pip
```

![Output after upgrading pip](https://www.freecodecamp.org/news/content/images/2022/03/image-2.png)
_Output after upgrading pip_

**3. Fix environment issues**

It is possible that you are trying to use the wrong version of pip. For example, `pip3` works for `Python3`, whereas `pip` works only for `Python2`.

You can check your Python version on Linux and Mac like this: 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-3.png)
_I am using Python3_

If your code is in Python 2 and you still wish to use an older version of pip, you can follow the below steps.

Note that Python 2 has reached end of life. It is better to upgrade your code base to Python 3 and use the latest version of pip.

Follow the below steps only if you are using Python2:

1. Install pip (older version)

```
sudo easy_install pip
```

This command installs the pip command onto your system.

Now try to use the pip command – it should work without errors.

## Wrapping up

Pip is a useful command to install Python packages. We have covered some troubleshooting methods for the error **`pip: command not found`.** 

I hope you found this tutorial helpful.

Let's connect on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

