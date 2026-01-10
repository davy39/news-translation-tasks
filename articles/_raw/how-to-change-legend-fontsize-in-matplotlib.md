---
title: How To Change Legend Font Size in Matplotlib
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-14T15:04:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-legend-fontsize-in-matplotlib
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/isaac-smith-6EnTPvPPL6I-unsplash--2-.jpg
tags:
- name: Matplotlib
  slug: matplotlib
- name: Python
  slug: python
seo_title: null
seo_desc: "You can modify different properties of a plot — color, size, label, title\
  \ and so on — when working with Matplotlib. \nIn this article, you'll learn what\
  \ a legend is in Matplotlib, and how to use some of its parameters to make your\
  \ plots more relatable..."
---

You can modify different properties of a plot — color, size, label, title and so on — when working with Matplotlib. 

In this article, you'll learn what a legend is in Matplotlib, and how to use some of its parameters to make your plots more relatable. 

You'll then learn how to change the font size of a Matplotlib legend using:

* The `fontsize` parameter. 
* The `prop` parameter.

## What Is a Legend in Matplotlib?

A legend is a Matplotlib function used to describe elements that make up a graph. 

Consider the graph below:

```python
import matplotlib.pyplot as plt

# create a plot
x = [1, 4, 6, 8]
y = [2, 5, 6, 2]

plt.plot(x, y)

plt.legend(["Data"], loc="upper right")

plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend.png)
_matplotlib graph with a legend_

In the graph above, we described the plot using a `legend`. A description of "Data" was assigned to the legend, and was placed in the upper right corner of the graph using the `upper right` value of the `loc` parameter. 

With the `legend` function, you can assign different descriptions to each line of a graph. 

Here's an example:

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
number = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(number)

plt.legend(["age", "number"], loc ="upper right")

plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend.PNG)
_two line graph with different legend descriptions_

In the graph above, we've used the `legend` function to describe each line in the plot. 

This makes it easier for anyone viewing the graph to know that the blue line denotes `age` while the orange line denotes `number` in the graph. 

You can change the position of the legend using the following values of the `loc` parameter: 

* `best`
* `upper right`
* `upper left`
* `lower left`
* `lower right`
* `right`
* `center left`
* `center right`
* `lower center`
* `upper center`
* `center`

## How To Change Legend Font Size in Matplotlib Using the `fontsize` Parameter

You can change the font size of a Matplotlib legend by specifying a font size value for the `fontsize` parameter. 

Here's what the default legend font size looks like:

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
number = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(number)

plt.legend(["age", "number"], loc ="upper right")

plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend-1.PNG)
_matplotlib graph with default legend font size_

Here's another code example with the `fontsize` parameter included:

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
number = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(number)

plt.legend(["age", "number"], fontsize="20", loc ="upper left")

plt.show()
```

Here's what the legend would look like:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend-fontsize-parameter-1.PNG)
_matplotlib legend size using fontsize parameter_

We assigned a font size of 20 to the `fontsize` parameter to get the legend size in the image above: `fontsize="20"`. 

You'd also notice the legend was placed at the upper left corner of the graph using the `loc` parameter.

## How To Change Legend Font Size in Matplotlib Using the `prop` Parameter

Another way of changing the font size of a legend is by using the `legend` function's `prop` parameter. 

Here's how to use it:

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
number = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(number)

plt.legend(["age", "number"], prop = { "size": 20 }, loc ="upper left")

plt.show()
```

Using the `prop` parameter, we specified a font size of 20: `prop = { "size": 20 }`. 

Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend-fontsize-parameter-2.PNG)
_matplotlib legend size using prop parameter_

## Summary

In this article, we talked about the `legend` function in Matplotlib. It can be used to describe the elements that maker up a graph. 

We first saw what a legend is in Matplotlib, and some examples to show its basic usage and parameters. 

We then saw how to use the `fontsize` and `prop` parameters to change the font size of a Matplotlib legend. 

Happy coding!

