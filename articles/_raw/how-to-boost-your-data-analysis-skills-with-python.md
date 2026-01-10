---
title: How to Boost Your Data Analysis Skills With Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T15:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-boost-your-data-analysis-skills-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/carlos-muza-hpjSkU2UYSU-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Emma Coffinet

  If you''re learning Python, you''ve likely heard about sci-kit-learn, NumPy and
  Pandas. And these are all important libraries to learn. But there is more to them
  than you might initially realize.

  There are numerous tips and tricks in t...'
---

By Emma Coffinet

If you're learning Python, you've likely heard about sci-kit-learn, NumPy and Pandas. And these are all important libraries to learn. But there is more to them than you might initially realize.

There are numerous tips and tricks in the [world of Python](https://www.freecodecamp.org/learn) that can help you speed up your tasks in data science, improve your code, and also help you to write code more efficiently.

So I decided to compile some of the most valuable data analysis tips in this article for you.

## Profile dataframes in Pandas

The primary role or purpose of profiling is to get a clear understanding of the data. And this is what the Python package, Pandas Profiling, does. This method is straightforward and fast in performing data analysis of dataframes in Pandas.

The exploratory data analysis process includes the Pandas df.info()functions and df.describe() as the first steps. But you only get a basic data overview, which might not be very helpful if you're dealing with a large data set.

Pandas’s [profiling function](https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.kaggle.com/parulpandey/10-simple-hacks-to-speed-up-your-data-analysis&ved=2ahUKEwjJ_tzBy-LqAhVPUBUIHYomB-gQFjAMegQIARAB&usg=AOvVaw1gTlUdtw6xS0ykqe9hhU5Y) also extends the dataframe of Pandas with the df.profile_report(), which helps you quickly analyze data. It displays plenty of information in just one line of code, which also happens to be an HTML report that's interactive.

For a set of data, Pandas profiling computes these statistics:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-50.png)

![Image](file:///C:/Users/JULIA~1.LOG/AppData/Local/Temp/lu43286f6mgz.tmp/lu43286f6mi9_tmp_9f3d0f0a74210f0d.png)

## Make pandas plots more interactive

The built-in plot() function of Pandas is also one of the Dataframe classes. However, this function offers visualizations that are not very interactive, and so do not appeal much to a data science audience.

On the other hand, it is easy to plot a chart with the Pandas.DataFrame.plot() function. The question then is, how do we plot interactive charts like Plotly using Pandas and without making significant changes to the code? 

You can do this with the Cufflinks library, which binds Plotly’s power with Pandas's flexibility for plotting quickly.

You can see the result in the images below.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-51.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-52.png)

![Image](file:///C:/Users/JULIA~1.LOG/AppData/Local/Temp/lu43286f6mgz.tmp/lu43286f6mi9_tmp_95977e6b363dc6c.png)

![Image](file:///C:/Users/JULIA~1.LOG/AppData/Local/Temp/lu43286f6mgz.tmp/lu43286f6mi9_tmp_5a8ad0fe7da1045d.gif)

Both visualizations show the same things. The first visualization is a static chart, while the second one is a more interactive chart (and it also provides more details than the first one). Yet, we got this without making any significant changes to the syntax. 

## Magic commands

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-71.png)

The tag ‘Magic Commands’ refers to a set of functions in Jupyter Notebooks. They created this set of features to solve the many common problems that are experienced in standard [data analysis](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/).

There are two kinds of Magic commands. First, there are the line magics - those that have a prefix of the % character. They also operate on one line of input. 

The second kind are the cell magics - denoted by the double %% prefix. They work on more than one input line. If you set it to 1, you'll call the magic functions without needing to type the initial %.

Some of these commands might come in handy when you're doing everyday tasks in data analysis. Some of them are:

### %pastebin

This function returns the URL and also uploads the code to Pastebin. Pastebin is a content hosting service online where it's possible to store plain text (such as source code snippets) and then share the URL with other people. 

As a matter of fact, a Github gist is very similar to Pastebin, but has version control.

### %matplotlib notebook

You can use this inline function for rendering static Matplotlib plots within Jupyter notebooks. You have to try and replace the inline part with a notebook. This will get you resize-able and zoom-able plots quickly. 

But make sure you call the function before you start to import the Matplotlib library.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-72.png)

### %run

You can use this function to run a Python script in a notebook.

### %%writefile

This function writes the cell content into a file. You then write the code into another file named foo.py before saving it into the current directory.

### %%latex

This function makes the cell content appear as LaTeX. It comes in handy when writing mathematical equations and formulae in a cell.

## Find and remove errors

The function known as the [interactive debugger](https://towardsdatascience.com/10-simple-hacks-to-speed-up-your-data-analysis-in-python-ec18c6396e6b) is another magic feature. However, for this article, it has a different category all its own. 

If you are running a code cell and get an exception, type %debug under a new line and then run it. This will open up an environment for interactive debugging that takes you back to the point where the exception happened.

You can also check the values of the different variables that they assigned within the program and, at the same time, perform operations there. After that, if you want to exit the debugger, press q.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-53.png)

## Use the ‘I’ option when running Python scripts

One way to typically run a Python script from the command line is with hello.py. But if you add an -i and run the same Python script, (Python -i hello.py), you get more benefits. How?

First of all, after you get to the [program end](https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.analyticsvidhya.com/blog/2019/08/10-powerful-python-tricks-data-science/&ved=2ahUKEwjJ_tzBy-LqAhVPUBUIHYomB-gQFjAAegQIAxAB&usg=AOvVaw1H3TUawIio2d4aE_ifcaP-), Python does not close the interpreter. This means that we can check for the values of the different variables and how correct the functions defined in the program are.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Pict.jpg)

Second, it is then easy to invoke the Python debugger, especially since the interpreter is still available by:

* Import pdb
* Pdb.pm()

From here, we can quickly get to the point where the exception happened and then work on the code.

## Delete and restore

So what do you do when you mistakenly delete one cell within your Jupyter Notebook? Luckily there is a shortcut for you to undo that action. 

You can recover or undo your deleted content by hitting CTRL/CMD+Z.

If you have deleted an entire cell that you want to recover, press ESC+Z, or EDIT > Undo Delete Cells.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-74.png)

## Conclusion

This article shared some tips to boost your data analysis skills with Python. These hacks should come in handy for you at some point in your Python data analysis journey. 

  

