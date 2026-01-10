---
title: 'The Riddle of Sphinx: How to Document Your Code Easily'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-19T11:10:16.000Z'
originalURL: https://freecodecamp.org/news/the-riddle-of-sphinx-how-to-document-your-code-easily-bf09a9a1804c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca90e740569d1a4ca821e.jpg
tags:
- name: documentation
  slug: documentation
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dalya Gartzman

  Why Am I Here?

  You, the reader, are here because you wrote some awesome tool in Python, and you
  want to make it accessible and easy to use.

  I, the writer, am here because I was right where you are a few months ago. I wanted
  to use t...'
---

By Dalya Gartzman

### Why Am I Here?

You, the reader, are here because you wrote some awesome tool in Python, and you want to make it accessible and easy to use.

I, the writer, am here because I was right where you are a few months ago. I wanted to use the [Sphinx](http://www.sphinx-doc.org/en/master/) package to make a ReadTheDocs-style documentation for my project.

I found the onboarding of Sphinx nontrivial, which is why I made [this GitHub repo](https://github.com/DalyaG/Sphinx185) that can be used as a template for **your** project.

**Before we start, some basic assumptions, to make sure we are on the same page:**

* You are writing in Python.
* You wrote [docstrings](https://en.wikipedia.org/wiki/Docstring#Python) for the pieces of code you wish to document.
* Your goal is to make a [ReadTheDocs](https://docs.readthedocs.io/en/latest/)-style documentation that, at least partially, will automagically generate itself.
* You are aware that in **10 minutes you could publish the first version** of your documentation, that is going to look something like [this](https://dalyag.github.io/Sphinx185/index.html):

![Image](https://cdn-media-1.freecodecamp.org/images/g8g3D4mCEhXpqKyjDM2RjySgqLlo4gZcViku)

### Part 1 - Setting the Stage

* Install Sphinx: `pip install sphinx`
* Go to [github.com/DalyaG/Sphinx185](https://github.com/DalyaG/Sphinx185):
* Download the folder `documentation_template_for_your_next_project`
* Copy to your project
* Rename the folder `documentation`

![Image](https://cdn-media-1.freecodecamp.org/images/CYOS9MopVTLHOshtpGkqwYFcddBNWui4WMNx)

### Part 2 - Personalize

* Open the file `<your_project>/documentation/c`onf.py in your favorite editor. Search for the pa`ttern #CHN`AGEME# and follow the instructions.
* Similarly, edit the file `<your_project>/documentation/ind`ex.rst and follow the inline instructions.

![Image](https://cdn-media-1.freecodecamp.org/images/zx3u0k2vQCGT5NKfSvks3flwgONlK4vi72U8)

![Image](https://cdn-media-1.freecodecamp.org/images/n6a72jLWaFOwE1Dc0ip6CT2K-3Bqp9gD43B0)

![Image](https://cdn-media-1.freecodecamp.org/images/36Kf81INhsKdDkppxQCbETPtFzbUI2C07dFn)

### Part 3 - Add the Content You Wish to Document

* Let’s say you have a python file called `my_amazing_class.py` that includes a class you wish to document.
* **In the same folder** as the `conf.py` and `index.rst` files, create a new file called `my_amazing_class.rst` and copy-paste-personalize this template:

```
This is a template for including classes========================================|.. autoclass:: my_amazing_class.MyAmazingClass|:ref:`Return Home <mastertoc>`
```

> TIP: make sure the folder containing your amazing class is in your `PYTHONPATH` and that it includes an init file`__init__.py`

* In the `index.rst` file, edit the Table Of Contents to include the name of the `.rst` file:

```
.. toctree::   :maxdepth: 1   :name: mastertoc
```

```
   my_amazing_class
```

### Part 4 - “Compile”

* In the terminal, inside the `documentation` folder, run `make clean html`.
* **That’s it!** You have your first version of your documentation ready to view!
* Open the file `documentation/_build/html/index.html` in your browser, and see for yourself :)

![Image](https://cdn-media-1.freecodecamp.org/images/fX7yeyvLr8pcpDbciN9zlmsDcBmm2A36Z96L)

![Image](https://cdn-media-1.freecodecamp.org/images/SGc77JLWj9RwwUjzNO1RfZSd-UF5wL-QlWza)

### Part 5 - Host on GitHub Pages

* Under the root of your project, open a new folder called `docs` and copy inside it the content of `<your_project>/documentation/_build`/html/
* Inside this new `docs` folder, create an empty file called `.nojekyll`   
(This tells GitHub Pages to bypass the default `Jekyll` themes and use the `HTML` and `CSS` in your project)
* Push your changes to `master` branch.
* In your repository on GitHub, go to `Settings->GitHub Pages->`Source   
and s`elect master branch/docs` folder

![Image](https://cdn-media-1.freecodecamp.org/images/kSaqUUJTnKIHrE3BKjT42cy0rAfCpo1uDObI)

![Image](https://cdn-media-1.freecodecamp.org/images/q1pwJyawKnwyds3ilJqlwj-4nA2eALjAgqov)

### Part 6 - Share!

Yup. That’s it. Wait a couple of minutes for GitHub to update. Share your beautiful documentation site at

`https://<your_git_usrname>.github.io/<proje`ct_name>/

> TIP: When updating documentation, you need to delete the `docs` folder and create it again. See more details [here](https://dalyag.github.io/Sphinx185/how_to_use_this_for_your_next_project.html).

### Epilogue

This is the part where I say something thoughtful about how wonderful it is to create new content in the world. And what a wonderful person you are for choosing to make your original content available, accessible, and easy to use.

But hey, you made it all the way here, so you already know this stuff.

So if there is something else that you still feel you don’t know, I invite you to explore the [documentation website](https://dalyag.github.io/Sphinx185/index.html) I made for this tutorial. You can watch the [talk I gave](https://www.youtube.com/watch?v=3OAAL78PES8) about Sphinx. Hopefully these will answer some riddles you have left about Sphinx.

