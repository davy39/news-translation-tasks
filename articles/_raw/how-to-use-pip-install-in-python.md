---
title: How to Use pip install in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T21:49:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pip-install-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dba740569d1a4ca3953.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Python comes with several built-in modules, but the Python community has
  more to offer. It’s the modules that makes python so powerful!

  Third party modules add so much more functionality to Python. So it''s time to learn
  how to install these modules s...'
---

Python comes with several built-in modules, but the Python community has more to offer. It’s the modules that makes python so powerful!

Third party modules add so much more functionality to Python. So it's time to learn how to install these modules so that we can use those in our programs.

The simplest way is to use `pip`

```text
pip install <module_name>
```

If you have used `npm`, then you can think of it as _npm_ of Python.

Side note: The difference is that with npm, `npm install` by default installs packages locally to a project, whereas `pip install` by default installs globally. 

To install modules locally, you need to create and activate what is called a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/), so `pip install` installs to the folder where that virtual environment is located, instead of globally (which may require administrator privileges).

Last time, in `import-statements` wiki we used `requests` module as an example. As it is a third party module we have to install it separately after installing python.

Installing it would be as simple as `pip install requests` . You can even pass various arguments along with it. The one that you’ll come across more often is `--upgrade`. You can upgrade a python module by :

```text
pip install <module_name> --upgrade
```

For example, to upgrade the requests module to its latest version would be as simple as `pip install requests --upgrade`.

Before using `pip`, you will need to install it (it’s quite simple). You can install it from [here](https://packaging.python.org/en/latest/tutorials/installing-packages/).

Just click on the link. And save the file as`get-pip.py` _Please don’t forget the `.py` extension._ And run it.

An alternative to using pip would be to try [`easy_install`](https://bootstrap.pypa.io/ez_setup.py).

Using `easy_install` is also simple. The syntax is:

```text
easy_install <module_name>
```

However, `pip` is more popular than using `easy_install`.

**Note:** On some systems where both Python 2 & Python 3 are installed, `pip` and `pip3` will do different things. `pip` installs the Python 2 version of the package, and `pip3` will install the Python 3 version of the package. 

For more information on the difference between Python 2 & 3, see [this](https://www.freecodecamp.org/news/how-to-learn-python/#heading-python-2-vs-python-3-whats-the-difference) guide. You can check the `pip` version by doing `pip --version` and/or `pip3 --version`:

```text
pip3 --version
pip 18.0 from /usr/local/lib/python3.5/dist-packages/pip (python 3.5)
```

We can also create a txt file containing a list of modules which should be installed using pip. For example, we could create the file `requirements.txt` and its content:

```text
Kivy-Garden==0.1.4
macholib==1.5.1
idna==2.6
geoip2nation==0.1.2
docutils>=0.14
Cython
```

In this file we could also set a version for the installation. After this, by invoking pip with:

```text
 pip install -r <FILE CONTAINING MODULES>
 
          OR IN OUR CASE
 
 pip install -r requirements.txt
 
```

it should install all the modules listed on the file.

