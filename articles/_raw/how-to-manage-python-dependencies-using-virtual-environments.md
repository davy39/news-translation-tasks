---
title: How to Manage Python Dependencies using Virtual Environments
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T20:39:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-python-dependencies-using-virtual-environments
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/0_T4VpXQchm1Vr05bL.jpg
tags:
- name: Python
  slug: python
- name: virtualenv
  slug: virtualenv
seo_title: null
seo_desc: "By Saransh Kataria\nWhen we start building a Python project that goes beyond\
  \ simple scripts, we tend to start using third-party dependencies. \nWhen working\
  \ on a larger project, we need to think about managing these dependencies in an\
  \ efficient manner...."
---

By Saransh Kataria

When we start building a Python project that goes beyond simple scripts, we tend to start using third-party dependencies. 

When working on a larger project, we need to think about managing these dependencies in an efficient manner. And when installing dependencies, we always want to be inside virtual environments. It helps keep things nice and clean. It also helps avoid messing up our Python environment.

# Why do we need Python Virtual Environments?

We can use Pip to install packages to our Python project. And it is common to have multiple packages installed in a single Python project. This can lead to some issues regarding the versions of the packages installed and their dependencies.

When we use `pip install <package name>` in a project, we are installing the package and its dependencies in the global Python namespace. And this will install the package for the specific Python version that we have configured Python for. 

We can find out where this directory is by using

```shell
python3.7 -c "import sys; print('\n'.join(sys.path))"

/usr/lib/python27.zip
/usr/lib/python2.7
/usr/lib/python2.7/lib-dynload
/usr/lib/python2.7/site-packages
```

And if we install the same package using `pip3 install <package name>`, it will be installed in a separate directory with the Python 3 version. We can overcome this by using the following command:

```shell
 python2.7 -m pip install <package name>
```

This still does not solve our problem of packages being installed system-wide, which can lead to the following problems:

* Different projects having different versions of the same package will conflict with one another
* A project’s dependencies can conflict with system-level dependencies which can break the system altogether
* Multi-user projects is not a possibility
* Testing code against different Python and library versions is a challenging task

To avoid those problems, Python developers use Virtual Environments. These virtual environments make use of isolated contexts (directories) for installing packages and dependencies.

# How to Create a Virtual Environment

We need a tool to make use of Python virtual environments. The tool we use to make them is known as [venv](https://docs.python.org/3/library/venv.html). It is built into the standard Python library for Python 3.3+.

If we were using Python 2, we would have had to install it manually. This is one of the few packages that we do want to install globally.

```shell
python2 -m pip install virtualenv
```

Note: We will talk more about venv in this post and Python 3 since there are a few differences between it and virtualenv. The commands are a bit different and the tools work differently under the hood.

We will start by making a new directory wherein we want to work with our project.

```shell
mkdir my-python-project && cd my-python-project
```

Then we will create a new virtual environment:

```shell
python3 -m venv virtualenv

# creates a virtual environment called virtualenv, the name can be anything we want
```

This will create a directory called virtualenv in the directory that we just created. The directory will contain a bin folder, a lib folder, an include folder, and an environment configuration file. 

All these files ensure that all Python code gets executed within the context of the current environment. This helps us achieve isolation from global environments and avoids the problems we discussed earlier.

In order to start using this environment, we need to activate it. Doing so will also change our command prompt to the current context.

```shell
$ source env/bin/activate
(virtualenv) $
```

The prompt is also an indicator that the virtual environment is active and Python code executes under that environment.

Inside our environment, system-wide packages are not accessible and any packages installed inside the environment are not available outside.

Only `pip` and `setuptools` are installed by default in a virtual environment.

After activating an environment, the path variable gets modified to achieve the concept of virtual environments.

When we are done and want to switch to the global environment, we can exit using the deactivate command:

```shell
(virtualenv) $ deactivate 
$
```

# How to Manage Dependencies Across Environments

Now that we have our virtual environments setup, we do not want to keep sharing the packages that can be installed using pip. We want to exclude our virtual environment folder, and be able to reproduce our work on a different system. 

We can do this by making use of a requirements file in the root directory of our project.

Let us assume that we installed Flask in our virtual environment. After that, if we run `pip freeze`, it will list the packages that we have installed and their version numbers.

```shell
(virtualenv) $ pip freeze
Flask==1.1.2
```

We can write this to a requirements.txt file to upload to Git, or share with other people in any other form.

```shell
(virtualenv) $ pip freeze > requirements.txt
```

This command can be used to update the file too.

And then, whenever someone wants to run our project on their computer, all they need to do is:

```shell
$ cd copied-project/
$ python3 -m venv virtualenv/
$ python3 -m pip install -r requirements.txt
```

And everything will work as it was on our system. 

## Wrapping Up

Now we can manage Python virtual environments and thus manage dependencies and packages as needed. If you have any questions regarding this, feel free to get in touch.

_You can find other articles of mine _at__ [_https://www.wisdomgeek.com_](https://www.wisdomgeek.com/development/web-development/python/managing-python-dependencies-using-virtual-environments/)_._

