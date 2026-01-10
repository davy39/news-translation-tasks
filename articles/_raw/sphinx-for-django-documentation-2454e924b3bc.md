---
title: How to document your Django project using the Sphinx tool
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T06:26:25.000Z'
originalURL: https://freecodecamp.org/news/sphinx-for-django-documentation-2454e924b3bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aBjEUaDShrMB9RFqbl_saQ.jpeg
tags:
- name: Django
  slug: django
- name: documentation
  slug: documentation
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Goran Aviani

  I recently visited a company where I had a nice talk with one of its employees.
  We talked about technology and programming. Then we touched the subject of project
  documentation. Specifically how React does it automatically but Django ...'
---

By Goran Aviani

I recently visited a company where I had a nice talk with one of its employees. We talked about technology and programming. Then we touched the subject of project documentation. Specifically how React does it automatically but Django doesn’t. That made me think I should do some automatic documentation for my Django projects.

I couldn’t find any relevant documentation on how its done, so it took me a little longer than I originally planned. Not because it was hard, but because I found that the Sphinx official documentation and other resources to be outdated or obscure.

So today I have made a simple but comprehensive tutorial that explains how to make Django documentation using the Sphinx documentation tool in Ubuntu.

#### **Install Sphinx**

First you should enter the virtual environment for your Django project.

Installing Sphinx is quite straightforward using pip3 (pip for Python 3):

```bash
pip3 install sphinx
```

#### Create a documentation directory

Once you’ve installed Sphinx, you will need to create the document root folder. This folder will hold your documentation and other files you will need (images, about pages, and so on…).

Create your document root folder in your project main folder and name it /docs.

To start Sphinx, run this command inside your /docs folder:

```bash
sphinx-quickstart
```

You’ll have a lot of options now. In most cases you can simply retype the default option, but there are some options you need to pay attention to.

This is how I answered:

```
Welcome to the Sphinx 1.7.5 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory “_build” within the root path, or you separate
“source” and “build” directories within the root path.

> Separate source and build directories (y/n) [n]: n

Inside the root directory, two more directories will be created; “_templates”
for custom HTML templates and “_static” for custom stylesheets and other static
files. You can enter another prefix (such as “.”) to replace the underscore.

> Name prefix for templates and static dir [_]: _

The project name will occur in several places in the built documentation.
> Project name: Your_project_name
> Author name(s): Goran Aviani
> Project release []: 1.0

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.

> Project language [en]: en

The file name suffix for source files. Commonly, this is either “.txt”
or “.rst”. Only files with this suffix are considered documents.

> Source file suffix [.rst]: .rst

One document is special in that it is considered the top node of the
“contents tree”, that is, it is the root of the hierarchical structure
of the documents. Normally, this is “index”, but if your “index”
document is a custom template, you can also set this to another filename.

> Name of your master document (without suffix) [index]: index

Sphinx can also add configuration for epub output:

> Do you want to use the epub builder (y/n) [n]: n

Indicate which of the following Sphinx extensions should be enabled:

> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: n
> todo: write “todo” entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]: y
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: y
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: n
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
> viewcode: include links to the source code of documented Python objects (y/n) [n]: n
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n
A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html’ instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]: y
> Create Windows command file? (y/n) [y]: y

Creating file ./conf.py.
Creating file ./index.rst.
Creating file ./Makefile.
Creating file ./make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file ./index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:

make builder

where “builder” is one of the supported builders, e.g. html, latex or linkcheck.
```

#### Django connection

In your project folder, find /docs/conf.py and inside it, somewhere near the top of the file, find “#import os”. Just below it, write this:

```py
import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'Your_project_name.settings'
django.setup()
```

**Now there are two ways you can proceed:**

1. You can use _sphinx-apidoc_ to generate completely automatic documentation, or
2. You can build your own modules that will show in the documentation.

In this tutorial I am going to show you how to do it both ways.

#### 1. Sphinx-apidoc

This is the simpler method where you just need to navigate to your /docs folder and execute:

```bash
sphinx-apidoc -o . ..
```

Now you need to build your documentation by running the command:

```bash
make html
```

Navigate to _Your_project_folder/docs/_build/html_ and open _index.html._ This is the index page of your documentation.

#### 2. Building your own modules

This is the slightly more complicated way, but will give you much more freedom in organizing your documentation.

Now you’ll want to make documentation about your views, modules etc. But first let me show you an easy example, just so you understand the logic of this part:

Go in your /docs folder and create a new folder named “/modules”. Inside it create a file named all-about-me.rst:

```bash
mkdir modulesf
touch modules/all-about-me.rst
```

Inside all-about-me.rst write something like this:

```rest
############
All about me
############

I’m Goran Aviani, a Django developer.
```

Now you’ve created something to show in your documentation, but still you don’t have an actual place to show it. Go back to the /docs folder and open index.rst and just bellow this code

```rest
.. toctree::
   :maxdepth: 2
   :caption: Contents:
```

Add this:

```rest
modules/all-about-me.rst
```

Make it so there is a blank line between the upper code and the added line:

```rest
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules/all-about-me.rst
```

Now you need to build your documentation. Change the location to the folder that contains the Makefile ( that is the /docs folder). Then run in the terminal:

```bash
make html
```

You will find your documentation in

> Your_project_folder/docs/_build/html and open index.html

You can do the same for your Django views:

Inside the /modules folder, create the views.rst file.

```bash
touch views.rst
```

Inside the views.rst file write this:

```rest
Views
======

.. automodule:: yourapp.views
   :members:
   :undoc-members:
```

Inside index.rst, just under modules/all-about-me.rst, add this:

```rest
modules/views.rst
```

Now you again need to build your documentation by running “make html” inside your /docs folder:

```bash
make html
```

Get the idea? First you create the .rst file and then you put it inside index.rst so it can be displayed on index.html page.

You can make same thing for your models. Go in your /modules folder and create models.rst file.

```bash
touch models.rst
```

You can add something like this in your models.rst file:

```rest
Models
=======

.. automodule:: yourapp.models
   :members:
   :undoc-members:
```

Inside index.rst just under modules/views.rst paste:

```rest
modules/models.rst
```

Inside your /docs folder run:

```bash
make html
```

#### Documentation test

You can test your documentation by running this code inside your /docs folder:

```bash
make linkcheck
```

Voilà! You are done!

This is my first public tutorial, so give me a few claps if you like it :)

Thank you for reading! Check out more articles like this on my freeCodeCamp profile: [https://www.freecodecamp.org/news/author/goran/](https://www.freecodecamp.org/news/author/goran/) and other fun stuff I build on my GitHub page: [https://github.com/GoranAviani](https://github.com/GoranAviani)

