---
title: How to Maintain Scalability in Your Python Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-20T17:51:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-scalable-apps-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/python-coding.jpg
tags:
- name: Productivity
  slug: productivity
- name: Python
  slug: python
- name: scalability
  slug: scalability
seo_title: null
seo_desc: "By Shifa Martin\nAny application that processes data can start to perform\
  \ slowly or even start to corrupt or break. It is better if developers are able\
  \ to program quickly and add more value to coding. \nAs developers, we should have\
  \ tools to prototype ..."
---

By Shifa Martin

Any application that processes data can start to perform slowly or even start to corrupt or break. It is better if developers are able to program quickly and add more value to coding. 

As developers, we should have tools to prototype quickly. That’s why we should invest effort in making an app that is scalable. Broadly, building a substantial and scalable application is possible with the Python programming language.

Python is a high-level programming language that is also object-oriented. With its qualities such as built-in data structures, dynamic binding, and dynamic typing, we can use it to develop applications as rapidly as possible. 

Python can also be used as a glued scripting language that integrates the existing components and helps us build scalable applications.

Python is one of the pioneers of programming languages that developers can use to do all the scaling work. 

Here are some tips you can check out for developing scalable apps in Python.

## Learn to Cleverly Use ‘Collections’

Python support rich and powerful data structures/containers for ‘collections’ such as [dict](https://docs.python.org/3.6/library/stdtypes.html#dict), [list](https://docs.python.org/3.6/library/stdtypes.html#list), [set](https://docs.python.org/3.6/library/stdtypes.html#set), and [tuple](https://docs.python.org/3.6/library/stdtypes.html#tuple). They are so valuable in building scalable apps. However, overusing them can impact code scalability. It's easy to spot when collections have been overused. 

```python2
# notebooks.csv holds meta information on a collection of notebooks:
# heading, writer, year of pub, etc.


# load_from_file returns a list of dicts.


notebooks = load_from_file('notebooks.csv')


notebook_summaries = dict()
for notebook in notebooks:


   notebook_summaries[notebook["heading"]] = notebook["summary"]


for heading, summary in notebook_summaries.items():


   # Do something interesting with the summary.


   print(heading, summary)

```

From the above code, you can clearly see it creates table mapping titles after reading notebook data from the CSV file. If you see it from the memory-usage viewpoint, there is nothing wrong if notebooks.csv has hundreds of titles. 

However, it is not right if it is related to the inventory of entire notebook stores with dozens of titles. You can have either one or two issues with your coding which also depends on what version you are using, Python 2 or Python 3.

This creates a bottleneck issue with the scalability of code memory. Creating a data structure called notebook_summaries is unnecessary here but it improves the readability. The “for” line helps you immediately know that a loop is running here through the summaries. 

The new data structure contains the full summary of every notebook that is likely to consume more memory than all the other fields. Suppose if a notebook consumes N bytes of memory, then the complete block will consume at least 1.5 * N bytes. 

**This will scale better in Python 3**

```python
notebooks = load_from_file('notebooks.csv')


for notebook in notebooks.items():


   print(notebook["title"], notebook["summary"])

```

I recommend that you create variables that are well-named as it helps boost the maintainability of your Python code.

## Intelligent Iterating of Python Codes

While developing large-size applications with Python, scalability is not the only thing you should consider. You can face several other problems. For example, the iteration issue is the most common one. 

Sometimes the for line in your coding iterates over notebook_summaries.items() and creates another copy of notebooks. This iteration of code can be responsible for low code performance in which Python code starts to hang before initiating the for loop.      
This happens because the notebook_summaries.items() forms a very large list that consumes more memory. Also it is because the Python code executes the bytecode after the forloop. 

It will start allocating more memory for this list. Again the iterating issue affects Python 2 as well as Python 3's items() and makes an extra copy of notebooks_summaries' contents. Developers can use iteritems instead of items in Python 2:

**In Python 2, use "iteritems" instead of "items"**

```python
notebooks = load_from_file('notebooks.csv')


    for notebook in notebooks.iteritems():


      print(notebook["title"], notebook["summary"])
```

So, the point here is to notice the difference between using an iterator in all Python versions and creating a list. It is the developer’s responsibility to justify the right pattern according to the coding context.

## Using ‘Generators’ For Scalability in Python Code

The generator function allows you to create iterators in a simpler manner.  Imagine you are working on building a software program as Grammarly that takes in text, analyze the sentences, and perform some kind of grammar analysis. Each line of sentence will be split by a period followed by one or more characters.

**See the coding** 

```python
import re
text = '''Full body of text. It has many sentences.
 
Some have grammatical errors and some are correct.'''
 
sentences = re.analyzed(r'\.\s+', text)
 
for sentence in sentences:
 
   print(sentence)
```

**Run the listing**

```python
This is a body of text
It has many sentences
 
Some have grammatical errors and some are correct.
```

```python
import random
def weathermaker(volatility, days):
    '''
    Yield a series of messages giving the day's weather and occasional commentary
    volatility ‑ a float between 0 and 1; the greater this number the greater
  the likelihood that the weather will change on each given day
    days ‑ number of days for which to generate weather
    '''
    #Always start as if yesterday were sunny
    current_weather = 'sunny'
    #First item is the probability that the weather will stay the same
    #Second item is the probability that the weather will change
    #The higher the volatility the greater the likelihood of change
    weights = 1.0‑volatility, volatility    #For fun track how many sunny days in a row there have been
    sunny_run = 1
    #How many rainy days in a row there have been
    rainy_run = 0
    for day in range(days):
        #Figure out the opposite of the current weather
        other_weather = 'rainy' if current_weather == 'sunny' else 'sunny'
        #Set up to choose the next day's weather. First set up the choices
        choose_from = current_weather, other_weather        #random.choices returns a list of random choices based on the weights
        #By default a list of 1 item, so we grab that first and only item with 0 current_weather = random.choices(choose_from, weights)0        yield 'today it is ' + current_weather
        if current_weather == 'sunny':
            #Check for runs of three or more sunny days
            sunny_run += 1
            rainy_run = 0
            if sunny_run >= 3:
                yield "Uh oh! We're getting thirsty!"
        else:
            #Check for runs of three or more rainy days
            rainy_run += 1
            sunny_run = 0
            if rainy_run >= 3:
                yield "Rain, rain go away!"
    return
 
#Create a generator object and print its series of messages
for msg in weathermaker(0.2, 10):
    print(msg)

```

**Output**

```python
$ python weathermaker.py
today it is sunny
today it is sunny
Uh oh! We're getting thirsty!
today it is sunny
Uh oh! We're getting thirsty!
today it is sunny
Uh oh! We're getting thirsty!
today it is rainy
today it is sunny
today it is rainy
today it is rainy
today it is rainy
Rain, rain go away!
today it is rainy
Rain, rain go away!
```

From the above code it’s clear that [Python generators](https://wiki.python.org/moin/Generators) are a great way to quickly create iterators. They have many benefits, and they allocate memory for each sentence one at a time. They also make it easier for developers to modify the code without screwing up. 

Another benefit generators provide is the [encapsulation](https://pythonspot.com/encapsulation/) that provides new and useful ways for you to package and isolate the internal code dependencies. This is why you can use generators in for loops.

**You can add multiple yield statements in a generator**

```python
def nums3():
   n = 0
 
   while n < 6:
 
  yield n
       n += 1
   yield 63 # Second yield
for num in nums3():
   print(num
```

**Output**

```python
0
1
2
3
63
```

**Explanation of the code above**

Here the second yield is completed after the whileloop exits. When the function reaches the implicit return at the end, the iteration stops.

## Final Words

So, if you don’t use generators in your python code yet, learn to do so. I know you will be glad you did it. They are the core part of Python coding and can be useful for your next application development on Python.

No doubt, Python is a very useful, diverse, and well-maintained language, and there is no bound to the features. However, I have shared the ideas which I use in my day to day coding process to make things simple. 

**ValueCoders is an experienced [software development company](https://www.valuecoders.com/). In case you need the Python development services, feel free to [get in touch](https://www.valuecoders.com/contact)_._**

  


  




  

