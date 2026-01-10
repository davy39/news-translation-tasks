---
title: Python 3.9 Updates Explained with Hands-on Code Examples
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2020-10-16T16:08:47.000Z'
originalURL: https://freecodecamp.org/news/python-updates
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Frame-19--2-.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'The latest stable release of Python is out!

  Open-source enthusiasts from all over the world have been working on new, enhanced,
  and deprecated features in Python for the past year.

  Though the beta versions have been rolling out for quite some time, t...'
---

The latest stable release of Python is out!

Open-source enthusiasts from all over the world have been working on new, enhanced, and deprecated features in Python for the past year.

Though the beta versions have been rolling out for quite some time, the official release of Python 3.9.0 happened on **October 5, 2020.**

%[https://twitter.com/llanga/status/1313207780954828808] 

The official documentation contains all the details of the latest features and changelog. Throughout this post, I’ll walk you through a few cool features that may come in handy in your day-to-day programming tasks.

## We’ll check out the following:

* **Type hinting generics and flexible function and variable annotations**
    
* **Union Operators in Dictionaries**
    
* `**zoneinfo**` **— Accessing and calculating time zones**
    
* **String methods to remove prefixes and suffixes**
    
* **Other release highlights**
    

To follow along with me or to try out the new features, you should have Python 3.9 installed.

I have used an environment manager called [pyenv](https://github.com/pyenv/pyenv) (alternatively, you can use conda) to get the latest version installed alongside my current version. You can also run it using the [official docker image](https://hub.docker.com/_/python/).

# Flexible Function and Variable Annotations

Function annotations have been around since Python 3.0 and they enable us to add metadata to Python functions. So, what’s new in Python 3.9?

Python 3.9 added [**PEP 593**](https://www.python.org/dev/peps/pep-0593). It introduced a mechanism to extend the type annotations from [**PEP 484**](https://www.python.org/dev/peps/pep-0484) which provides the standard semantic for annotations and suggested that annotations be used for type hinting.

Now, there can be many other use cases for annotations besides type hinting. So PEP 593 introduced `typing.Annotated` which allows you to add more details to the metadata.

Let’s try to understand this better via an example for both Python 3.8 and 3.9.

**Python 3.8**

```javascript
def currency_exchange(eur: "euros", rate: "exchange rate") -> "euro to USD":
    """Converting Euros to USD using the exchange rate"""
    return eur * rate
```

This is a simple function that converts Euros to USD using the exchange rate. We have used the annotations to serve as documentation for the user.

**Python 3.9**

```javascript
from typing import Annotated
def currency_exchange(eur: Annotated[float, "euros"], rate: Annotated[float, "exchange rate"]) -> Annotated[float, "euro to dollars"]:
    """Converting Euros to Dollars using the exchange rate"""
    return eur * rate
```

Here, we are using the newly introduced `Annotated` that takes at least two arguments. The first argument (`float` in the example) establishes the type hint, and the rest of the arguments are arbitrary metadata of the function.

The user/developer can also check these annotations using the `__annotations__` attribute:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/1-4.png align="left")

We can also check the type using the `get_type_hint()` function:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/2-5.png align="left")

## Type Hinting Generics in Standard Collections

Basic data types like `int`, `str` or `bool` are simple to annotate.

The earlier static typing was built incrementally on top of the existing Python runtime and constrained by it. This led to a duplicated collection hierarchy in the typing module due to the generics – that is, we had both `typing.List` and the built-in list.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/3-3.png align="left")

With generics, we have the issue of parameterization due to their storage structure (which is a container). And for these reasons, we have not been able to use `list(float)` or `list[float]` as type hints directly. Instead, we needed a typing module to achieve this.

In **Python 3.9**, this duplicate hierarchy is no longer needed. We can annotate them directly:

```javascript
scores: list(float)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/4-3.png align="left")

# How to Merge and Update Dictionaries

Two of the coolest and most useful features of Python 3.9 are the merge(|) and update(|=) operators added to the built-in `dict` class.

The existing (3.8) ways of merging two dicts have many shortcomings:

**Python 3.8**

* Dict unpacking looks ugly and is not easily discoverable.
    

```javascript
python = {2000: "2.0.1", 2008: "2.6.9", 2010: "2.7.18"}
python3 = {2008: "3.0.1", 2009: "3.1.5", 2016: "3.6.12", 2020: "3.9.0"}

##merging two dictionaries
{**python, **python3}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/5-3.png align="left")

* Another method is dict.update which modifies the original dictionary in-place:
    

![Image](https://www.freecodecamp.org/news/content/images/2020/10/6-3.png align="left")

**Python 3.9**

[**PEP 584**](https://www.python.org/dev/peps/pep-0584) has introduced two new operators for dictionaries:

* **(|) union —** to merge two dictionaries. It preserves the original dictionaries.
    
* **(|=) update —** this is for in-place merging of dictionaries.
    

```javascript
python = {2000: "2.0.1", 2008: "2.6.9", 2010: "2.7.18"}
python3 = {2008: "3.0.1", 2009: "3.1.5", 2016: "3.6.12", 2020: "3.9.0"}

##merging two dictionaries
python | python3
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/7-2.png align="left")

Preserved original dicts:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/8-2.png align="left")

```javascript
python |= python3
python
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/9-2.png align="left")

The update operator merges the dictionaries and updates the dictionary on the left of the operator while **keeping the last values** for the overlapping keys in the two dicts.

# How to Work with Timezones — ZoneInfo

Dates and time play a central role in many applications. Python offers comprehensive support via the `datetime` module in the standard library. But there has always been a gap with respect to integrating time zones to these timestamps.

Up until now, we’ve had third party libraries like dateutil to implement such timezone specific rules.

But now Python 3.9 has added a new `**zoneinfo**` module that lets you access and use the entire Internet Assigned Numbers Authority (IANA) time zone database.

**Python 3.8**

Until now, we’ve been accessing time zone aware timestamps using the `tzinfo` argument as follows:

```javascript
from datetime import datetime, timezone

datetime.now(tz=timezone.utc)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/10-1.png align="left")

**Python 3.9**

But with the addition of zoneinfo, we now have access to the [IANA Time Zone Database](https://www.iana.org/time-zones).

```javascript
from zoneinfo import ZoneInfo

ZoneInfo("Asia/Kolkata")
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/11-1.png align="left")

We can do a bunch of operations with time zones, and interconversion has become very easy:

```javascript
from datetime import datetime
from zoneinfo import ZoneInfo

post_date = datetime(2020, 10, 10, 18, 10, tzinfo=ZoneInfo("America/Vancouver"))

post_date.astimezone(ZoneInfo("Asia/Kolkata"))
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/12-1.png align="left")

# **String methods to remove prefixes and suffixes**

[**PEP 616**](https://www.python.org/dev/peps/pep-0616) has introduced new methods to strip off prefixes and suffixes from strings. The new methods are:

* **removeprefix()**
    
* **removesuffix()**
    

There have been many recurring issues reported across all the major forums (like StackOverflow) around the `lstrip()` and `rstrip()` methods.

**Python 3.8**

We’ve been stripping off characters from either ends of the string using the strip() method as follows:

```javascript
"Python 3.9 is out".strip(" Python")
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/13.png align="left")

This has removed the substring present at the ends of the string. If you look carefully, this has removed the individual characters in “ python” i.e. “ ”, “p”, “y”, “t”, “h”, “o” and “n”.

**Python 3.9**

To get rid of the prefix from a string, we now have `removeprefix()`:

```javascript
"Python 3.9 is out".removeprefix("Python ")
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/14.png align="left")

You can check this out with a number of other permutations and combinations with the `removesuffix()` method as well.

# Other Release Highlights

Besides these, a number of other features have also been introduced. Here is the list along with the PEP IDs:

* [**PEP 617**](https://www.python.org/dev/peps/pep-0617)**,** C**Python now uses a new parser based on PEG —** Python now has a new parser alongside the old LL(1) parser. You can choose to run your program using any of the parsers using the command:
    

```javascript
python -X oldparser script_name.py
```

PEG parsers are more robust and powerful as per Guido van Rossum's research (he's the creator of Python). The PEG parser’s goal would be to produce the same **abstract syntax tree (AST)** as the old LL(1) parser.

* **Multiphase initialization** is now available for use in a number of python modules( `[audioop](https://docs.python.org/3/library/audioop.html#module-audioop)`, `_bz2`, `_codecs`, `_contextvars`, `_crypt`, `_functools`, `_json`, `_locale`, `[math](https://docs.python.org/3/library/math.html#module-math)`, `[operator](https://docs.python.org/3/library/operator.html#module-operator)`, `[resource](https://docs.python.org/3/library/resource.html#module-resource)`, `[time](https://docs.python.org/3/library/time.html#module-time)`, `_weakref`)
    

Here’s an example of calculating GCD/LCM of more than two numbers using the math library:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/15.png align="left")

* [**PEP 602**](https://www.python.org/dev/peps/pep-0602) **CPython now adopts a new annual release cycle** — They will be more consistent with their releases and will get new versions out every October.
    
* [**PEP 614**](https://www.python.org/dev/peps/pep-0614), relaxed grammar restrictions on decorators — a more flexible syntax is now available for people working on GUI frameworks like PyQT. This waives the limitation on decorators consisting of a dotted name. More details can be read [here](https://www.python.org/dev/peps/pep-0614/).
    

To know more about the details of each of these features, head over to the [official](https://docs.python.org/3/whatsnew/3.9.html) [documentation](https://docs.python.org/3/whatsnew/3.9.html).

# Conclusion

3.9.0 marks a big milestone in the journey of Python’s development and for the community. New enhancements are being added as we speak and 3.10 will also have promising features.

For now, you should try out these soon to be widely used features introduced in **Python 3.9.**

Try running your existing programs using Python 3.9 and see if upgrading would be worth it for you.

You should also try out the new parser, which claims to be promising. But we’ll only know for sure after considerable testing across several use cases.

## [Data Science with Harshit](https://www.youtube.com/c/DataSciencewithHarshit?sub_confirmation=1)

%[https://youtu.be/yapSsspJzAw] 

With this channel, I am planning to roll out a couple of [series covering the entire data science space](https://towardsdatascience.com/hitchhikers-guide-to-learning-data-science-2cc3d963b1a2?source=---------8------------------). Here is why you should be subscribing to the [channel](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ):

* These series would cover all the required/demanded quality tutorials on each of the topics and subtopics like [Python fundamentals for Data Science](https://towardsdatascience.com/python-fundamentals-for-data-science-6c7f9901e1c8?source=---------5------------------).
    
* Explained [Mathematics and derivations](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea?source=---------9------------------) of why we do what we do in ML and Deep Learning.
    
* [Podcasts with Data Scientists and Engineers](https://www.youtube.com/watch?v=a2pkZCleJwM&t=2s) at Google, Microsoft, Amazon, etc, and CEOs of big data-driven companies.
    
* [Projects and instructions](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb?source=---------2------------------) to implement the topics learned so far. Learn about new certifications, Bootcamp, and resources to crack those certifications like this [**TensorFlow Developer Certificate Exam by Google.**](https://youtu.be/yapSsspJzAw)
    

If this tutorial was helpful, you should check out my data science and machine learning courses on [Wiplane Academy](https://www.wiplane.com/). They are comprehensive yet compact and helps you build a solid foundation of work to showcase.
