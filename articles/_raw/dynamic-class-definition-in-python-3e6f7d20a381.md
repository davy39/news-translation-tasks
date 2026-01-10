---
title: Dynamic class definition in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T17:49:19.000Z'
originalURL: https://freecodecamp.org/news/dynamic-class-definition-in-python-3e6f7d20a381
coverImage: https://cdn-media-1.freecodecamp.org/images/0*bJlMQkXW7FOfL5CL
tags:
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Peter Gleeson

  Here’s a neat Python trick you might just find useful one day. Let’s look at how
  you can dynamically define classes, and create instances of them as required.

  This trick makes use of Python’s object oriented programming (OOP) capabil...'
---

By Peter Gleeson

Here’s a neat Python trick you might just find useful one day. Let’s look at how you can dynamically define classes, and create instances of them as required.

This trick makes use of Python’s object oriented programming (OOP) capabilities, so we’ll review those first.

### Classes and objects

Python is an object-oriented language, meaning it lets you write code in the [object oriented paradigm](https://guide.freecodecamp.org/design-patterns/object-oriented-programming/).

The key concept in this programming paradigm is classes. In Python, these are used to create objects which can have attributes.

Objects are specific instances of a class. A class is essentially a blueprint of what an object is and how it should behave.

Classes are defined with two types of attribute:

* [Data attributes](https://docs.python.org/3/tutorial/classes.html#instance-objects) — variables available to a given instance of that class
* [Methods](https://docs.python.org/3/tutorial/classes.html#method-objects) — functions available to an instance of that class

The classic OOP example usually involves different types of animal, or food. Here, I’ve gone more practical with a simple data visualization theme.

First, define the class `BarChart`.

```python
class BarChart:
	def __init__(self, title, data):
    	self.title = title
    	self.data = data
   	def plot(self):
    	print("\n"+self.title)
        for k in self.data.keys():
        	print("-"*self.data[k]+" "+k)
```

The `__init__` method lets you set attributes upon instantiation. That is, when you create a new instance of `BarChart`, you can pass arguments that provide the chart’s title and data.

This class also has a `plot()` method. This prints a very basic bar chart to the console when it is called. It could feasibly do more interesting things in a real application.

Next, instantiate an instance of `BarChart`:

```python
data = {"a":4, "b":7, "c":8}bar = BarChart("A Simple Chart", data)
```

Now you can use the `bar` object in the rest of your code:

```python
bar.data['d'] = bar.plot()
```

```
A Simple Chart
---- a
------- b
-------- c
----- d
```

This is great, because it allows you to define a class and create instances dynamically. You can spin up instances of other bar charts in one line of code.

```python
new_data = {"x":1, "y":2, "z":3}
bar2 = BarChart("Another Chart", new_data)
bar2.plot()
```

```
Another Chart
- x
-- y
--- z
```

Say you wanted to define several classes of chart. [Inheritance](https://docs.python.org/3.7/tutorial/classes.html#inheritance) lets you define classes which “inherit” properties from base classes.

For example, you could define a base `Chart` class. Then you can define derived classes which inherit from the base.

```python
class Chart:
	def __init__(self, title, data):
    	self.title = title
        self.data = data
    def plot(self):
    	pass
```

```python
class BarChart(Chart):
	def plot(self):
    	print("\n"+self.title)
        for k in self.data.keys():
        	print("-"*self.data[k]+" "+k)
```

```python
class Scatter(Chart):
	def plot(self):
    	points = zip(data['x'],data['y'])
        y = max(self.data['y'])+1
        x = max(self.data['x'])+1
        print("\n"+self.title)
        for i in range(y,-1,-1):
        	line = str(i)+"|"
            for j in range(x):
            	if (j,i) in points:
                	line += "X"
                else:
                	line += " "
            print(line)
```

Here, the `Chart` class is a base class. The `BarChart` and `Scatter` classes inherit the `__init__()` method from `Chart.` But they have their own `plot()` methods which override the one defined in `Chart`_._

Now you can create scatter chart objects as well.

```python
data = {'x':[1,2,4,5], 'y':[1,2,3,4]}
scatter = Scatter('Scatter Chart', data)
scatter.plot()
```

```
Scatter Chart
4|     X
3|	  X 
2|  X
1| X
0|
```

This approach lets you write more abstract code, giving your application greater flexibility. Having blueprints to create countless variations of the same general object will save you unnecessarily repeating lines of code. It can also make your application code easier to understand.

You can also import classes into future projects, if you want to reuse them at a later time.

### Factory methods

Sometimes, you won’t know the specific class you want to implement before runtime. For example, perhaps the objects you create will depend on user input, or the results of another process with a variable outcome.

[Factory methods](https://en.wikipedia.org/wiki/Factory_method_pattern) offer a solution. These are methods that take a dynamic list of arguments and return an object. The arguments supplied determine the class of the object that is returned.

A simple example is illustrated below. This factory can return either a bar chart or a scatter plot object, depending on the `style` argument it receives. A smarter factory method could even guess the best class to use, by looking at the structure of the `data` argument.

```python
def chart_factory(title, data, style):
	if style == "bar":
    	return BarChart(title, data)
    if style == "scatter":
    	return Scatter(title, data)
    else:
    	raise Exception("Unrecognized chart style.")
        
    
```

```python
chart = chart_factory("New Chart", data, "bar")
chart.plot()
```

Factory methods are great when you know in advance which classes you want to return, and the conditions under which they are returned.

But what if you don’t even know this in advance?

### Dynamic definitions

Python lets you define classes dynamically, and instantiate objects with them as required.

Why might you want to do this? The short answer is yet more abstraction.

Admittedly, needing to write code at this level of abstraction is generally a rare occurrence. As always when programming, you should consider if there is an easier solution.

However, there may be times when it genuinely proves useful to define classes dynamically. We’ll cover a possible use-case below.

You may be familiar with Python’s `type()` function. With one argument, it simply returns the “type” of the object of the argument.

```python
type(1) # <type 'int'>
type('hello') # <type 'str'>
type(True) # <type 'bool'>
```

But, with three arguments, `type()` returns a whole new [type object](https://docs.python.org/3/library/stdtypes.html#bltin-type-objects). This is [equivalent to defining a new class](https://docs.python.org/3/library/functions.html#type).

```
NewClass = type('NewClass', (object,), {})
```

* The first argument is a string that gives the new class a name
* The next is a tuple, which contains any base classes the new class should inherit from
* The final argument is a dictionary of attributes specific to this class

When might you need to use something as abstract as this? Consider the following example.

[Flask Table](https://flask-table.readthedocs.io/en/stable/#flask-table) is a Python library that generates syntax for HTML tables. It can be installed via the pip package manager.

You can use Flask Table to define classes for each table you want to generate. You define a class that inherits from a base `Table` class. Its attributes are column objects, which are instances of the `Col` class.

```python
from flask_table import Table, Col
class MonthlyDownloads(Table):
	month = Col('Month')
    downloads = Col('Downloads')
    
data = [{'month':'Jun', 'downloads':700},
		{'month':'Jul', 'downloads':900},
        {'month':'Aug', 'downloads':1600},
        {'month':'Sep', 'downloads':1900},
        {'month':'Oct', 'downloads':2200}]
        
table = MonthlyDownloads(data)print(table.__html__())
```

You then create an instance of the class, passing in the data you want to display. The `__html__()` method generates the required HTML.

Now, say you’re developing a tool that uses Flask Table to generate HTML tables based on a user-provided config file. You don’t know in advance how many columns the user wants to define — it could be one, it could be a hundred! How can your code define the right class for the job?

Dynamic class definition is useful here. For each class you wish to define, you can dynamically build the `attributes` dictionary.

Say your user config is a CSV file, with the following structure:

```
Table1, column1, column2, column3
Table2, column1
Table3, column1, column2
```

You could read the CSV file line-by-line, using the first element of each row as the name of each table class. The remaining elements in that row would be used to define `Col` objects for that table class. These are added to an `attributes` dictionary, which is built up iteratively.

```
for row in csv_file:
	attributes = {}
    for column in row[1:]:
    	attributes[column] = Col(column)
        globals()[row[0]] = type(row[0], (Table,), attributes)
```

The code above defines classes for each of the tables in the CSV config file. Each class is added to the `globals` dictionary.

Of course, this is a relatively trivial example. FlaskTable is capable of generating much more sophisticated tables. A real life use-case would make better use of this! But, hopefully, you’ve seen how dynamic class definition might prove useful in some contexts.

### So now you know…

If you are new to Python, then it is worth getting up to speed with classes and objects early on. Try implementing them in your next learning project. Or, [browse open source projects on Github](https://github.com/trending/python) to see how other developers make use of them.

For those with a little more experience, it can be very rewarding to learn how things work “behind-the-scenes”. Browsing [the official docs](https://docs.python.org/3/) can be illuminating!

Have you ever found a use-case for dynamic class definition in Python? If so, it’d be great to share it in the responses below.

