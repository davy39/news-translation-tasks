---
title: How to Set Up a Django Development Environment
subtitle: ''
author: Victoria (Burah) Poromon
co_authors: []
series: null
date: '2023-12-12T15:52:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-django-development-environment
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/DDE-cover.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
- name: virtualenv
  slug: virtualenv
seo_title: null
seo_desc: 'Django is a high-level web framework written in Python that encourages
  a rapid and realistic functional design. The Django web framework is free and open-source
  and is widely used to create both small and large web applications.

  In this tutorial, you...'
---

Django is a high-level web framework written in Python that encourages a rapid and realistic functional design. The Django web framework is free and open-source and is widely used to create both small and large web applications.

In this tutorial, you will learn the following:

* What a development environment is,
* What a virtual environment is,
* How to create a Python virtual environment, and
* How to install Django in your virtual environment.

To get the most out of this tutorial, you'll need to have a basic knowledge of using a terminal/command line and have the latest stable version of Python installed on your computer.

## What is a Development Environment?

A development environment is an installation of Django on your local computer. Setting up your environment is an important step in your website’s development process. It provides an isolated and controlled space for you to write, test, and debug your code before deploying to a production environment.

## What is a Virtual Environment?

A virtual environment is a space that allows you to isolate the dependencies and configurations of one project from another. This way, you can create different projects with different versions of libraries, and they won’t interfere with each other.

Note that there are various types of virtual environments, but in this tutorial we'll focus on creating a Python environment.

## How to Create a Python Virtual Environment

In Python, there are several tools available for creating and managing virtual environments. Here are two commonly used ones:

### The `venv` tool:

`venv` is an in-built module that comes with Python versions 3.3 and later. It's a simple and lightweight way to create a virtual environment.

Here's how to create a virtual environment using `venv`:

```bash
python -m venv myenv

```

`myenv` is the name of your virtual environment. You can use any other name, but always use lowercase letters and add no spaces. 

Also, keep the name short so it is easy to remember. Dashes are allowed and commonly used. For example, `my-env` instead of `myenv`.

### The `virtualenv` tool:

`virtualenv` is a third-party tool for creating a virtual environment. Its features allow you to create an environment with a different version of Python than the one used to execute the `virtualenv` command.

Here's how to create a virtual environment using `virtualenv`:

```bash
# For macOS and Linux
pip install virtualenv
virtualenv myenv

# For windows
pip install virtualenv
python -m virtualenv myenv

```

`pip install virtualenv` is a command that uses the Python package manager `pip` to install `virtualenv` globally in your computer. After installation, `virtualenv myenv` creates a new virtual environment named `myenv`. 

Just like when using the `venv` tool, you can change the name of the environment. But always remember to keep them short, use lowercase letters, and add no spaces. You can use dashes, too.

## Django Installation

Django provides you with a set of Python scripts for creating and working with Django projects. It is very flexible in terms of where and how you can install it. But for this tutorial, you will be installing Django in the virtual environment you just created.

Here's how you can install Django in your virtual environment, for Linux and macOS:

```bash
# Activate your virtual environment
source myenv/bin/activate

# Install Django
pip install django

# Or use this to specify the version
pip install django==4.2.7

```

For Windows:

```bash
# Activate your virtual environment
myenv\Scripts\activate

# Install Django
pip install django

# Or use this to specify the version
pip install django==4.2.7

```

`pip` is a package installer for Python that is recommended for installing Django. The command `pip install django` downloads the latest version of Django and installs it in your Python environment.

After working on your project, you can deactivate your virtual environment by typing the following command into your terminal or command line:

```bash
deactivate

```

### How to verify your Django installation

After installation, you should verify that Django is correctly installed in your virtual environment. Always ensure to activate your virtual environment before verifying your installation.

Verify your Django installation with the following command:

```bash
python -m django --version

```

The above command will display the Django version installed in your virtual environment.

Congratulations! Your Django development environment is now active on your computer.

## Conclusion

Django facilitates the development of web applications by providing a solid foundation, reducing repetition, and promoting best practices.

Installing Django is the first step in creating an environment for your web projects. After this process, you can now set up your Django project, define its structure, configure your databases, create your applications, and start building your web application. Happy Coding.

