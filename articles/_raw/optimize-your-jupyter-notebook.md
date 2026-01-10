---
title: How to optimize your Jupyter Notebook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-19T07:44:05.000Z'
originalURL: https://freecodecamp.org/news/optimize-your-jupyter-notebook
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/1_m87_Htb_9Pstq0UcvNJ49w.png
tags:
- name: Data Science
  slug: data-science
- name: 'Jupyter Notebook '
  slug: jupyter-notebook
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "By Pier Paolo Ippolito\nIntroduction\nJupyter Notebook is nowadays probably\
  \ the most used environment for solving Machine Learning/Data Science tasks in Python.\
  \ \nJupyter Notebook is a client-server application used for running notebook documents\
  \ in the..."
---

By Pier Paolo Ippolito

## Introduction

Jupyter Notebook is nowadays probably the most used environment for solving Machine Learning/Data Science tasks in Python. 

Jupyter Notebook is a client-server application used for running notebook documents in the browser. Notebook documents are documents able to contain both code and rich text elements such as paragraphs, equations, and so on.

In this article, I will walk you through some simple tricks on how to improve your experience with Jupyter Notebook. We will start from useful shortcuts and we will end up adding themes, automatically generated table of contents, and more.

## Shortcuts

Shortcuts can be really useful to speed up writing your code. I will now walk you through some of the shortcuts I found most useful to use in Jupyter.

There are two possible way to interact with Jupyter Notebook: Command Mode and Edit Mode. Some shortcuts work only on one mode or another while others are common to both modes.

Some shortcuts which are common in both modes are:

* **Ctrl + Enter**: to run all the selected cells
* **Shift + Enter**: run the current cell and move the next one
* **Ctrl + s**: save notebook

In order to enter Jupyter command mode, we need to press Esc and then any of the following commands:

* **H**: show all the shortcuts available in Jupyter Notebook
* **Shift + Up/Down Arrow**: to select multiple notebook cells at the same time (pressing enter after selecting multiple cells will make all of them run!)
* **A**: insert a new cell above
* **B**: insert a new cell below
* **X**: cut the selected cells
* **Z**: undo the deletion of a cell
* **Y**: change the type of cell to Code
* **M**: change the type of cell to Markdown
* **Space**: scroll notebook down
* **Shift + Space**: scroll notebook up

In order to enter Jupyter edit mode instead, we need to press Enter and successively any of the following commands:

* **Tab**: code competition suggestions
* **Ctrl + ]**: indent code
* **Ctrl + [**: dedent code
* **Ctrl + z**: undo
* **Ctrl + y**: redo
* **Ctrl + a**: select all
* **Ctrl + Home**: move cursor to cell start
* **Ctrl + End**: move cursor to the end of the cell
* **Ctrl + Left**: move cursor one word left
* **Ctrl + Right**: move cursor one word right

## Shell commands and Packages installation

Not many users are aware of this, but it is possible to run shell commands in a Jupyter notebook cell by adding an exclamation mark at the beginning of the cell. For example, running a cell with **!ls** will return all the items in the current working directory. Running a cell with **!pwd** will instead print out the current directory file-path.

This same trick can also be applied to install Python packages in Jupyter notebook.

```py
!pip install numpy
```

## Jupyter Themes

If you are interested in changing how your Jupyter notebook looks, it is possible to install a package with a collection of different themes. The default Jupyter theme looks like the one in Figure 1. In Figure 2 you will see how we will be able to personalise its aspect.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/2-2.PNG)
_Figure 1: Default Jupyter Notebook Theme_



We can install our package directly in the notebook using the trick I showed you in the previous section:

```py
!pip install jupyterthemes
```

We can the run the following command to list the names of all the available themes:

```py
!jt -l

# Cell output:
# Available Themes: 
#   chesterish
#   grade3
#   gruvboxd
#   gruvboxl
#   monokai
#   oceans16
#   onedork
#   solarizedd
#   solarizedl
```

Finally, we can choose a theme using the following command (in this example I decided to use the solarized1 theme):

```py
!jt -t solarizedl
```

Once we've run this command and refreshed the page, our notebook should look like the one in Figure 2.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-1.PNG)
_Figure 2: Solarized1 notebook Theme_

In case you wish anytime to come back to the original Jupyter notebook theme, you can just run the following command and refresh your page.

```py
!jt -r
```

## Jupyter Notebook Extensions

Notebook extensions can be used to enhance the user experience and offer a wide variety of personalization techniques.

In this example, I will be using the _nbextensions_ library in order to install all the necessary widgets (this time I suggest you to first install the packages through terminal and then open the Jupyter notebook). This library makes use of different Javascript models in order to enrich the notebook frontend.

```py
! pip install jupyter_contrib_nbextensions
! jupyter contrib nbextension install --system
```

Once _nbextensions_ is installed you will notice that there is an extra tab on your Jupyter notebook homepage (Figure 3).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-128.png)
_Figure 3: Adding nbextensions to Jupyter notebook_

By clicking on the Nbextensions tab, we will be provided with a list of available widgets. In my case, I decided to enable the ones shown in Figure 4.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-129.png)
_Figure 4: nbextensions widgets options_

Some of my favourite extensions are:

1. **Table of Contents**

Auto-generate a table of contents from markdown headings (Figure 5).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/ezgif.com-optimize-1.gif)
_Figure 5: Table of Contents_

2. **Snippets**

Sample codes to load common libraries and create sample plots which you can use as a starting point for your data analysis (Figure 6).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/snippets.gif)
_Figure 6: Snippets_

3. **Hinterland**

Code autocompletion for Jupyter Notebooks (Figure 7).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/completition.gif)
_Figure 7: Code autocompletion_

The _nbextensions_ library provides many other extensions apart for these three, so I encourage you to experiment and test any other which can be of interest for you!

## Markdown Options

By default, the last output in a Jupyter Notebook cell is the only one that gets printed. If instead we want to automatically print all the commands without having to use _print()_, we can add the following lines of code at the beginning of the notebook.

```py
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

Additionally, it is possible to write LaTex in a Markdown cell by enclosing the text between dollar signs ($).

## Notebook Slides

It is possible to create a slideshow presentation of a Jupyter Notebook by going to **View -> Cell Toolbar -> Slideshow** and then selecting the slides configuration for each cell in the notebook.

Finally, by going to the terminal and typing the following commands the slideshow will be created.

```py
pip install jupyter_contrib_nbextensions

# and successively:

jupyter nbconvert my_notebook_name.ipynb --to slides --post serve
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/ezgif.com-optimize--1-.gif)

## Magic

Magics are commands which can be used to perform specific commands. Some examples are: inline plotting, printing the execution time of a cell, printing the memory consumption of running a cell, and so on.

Magic commands which start with just one _%_ apply their functionality just for one single line of a cell (where the command is placed). Magic commands which instead start with two _%%_ are applied to the whole cell.

It is possible to print out all the available magic commands by using the following command:

```py
%lsmagic
```

## Contact info

If you want to keep updated with my latest articles and projects [follow me](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) and subscribe to my [mailing list](http://eepurl.com/gwO-Dr?source=post_page---------------------------). These are some of my contact details:

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Personal Blog](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Personal Website](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Medium Profile](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Cover photo [from this article](https://gdcoder.com/how-to-create-and-add-a-conda-environment-as-jupyter-kernel/).

