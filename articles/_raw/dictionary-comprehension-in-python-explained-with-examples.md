---
title: Dictionary Comprehension in Python – Explained with Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-08-24T17:34:03.000Z'
originalURL: https://freecodecamp.org/news/dictionary-comprehension-in-python-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/dict_comprehension.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: 'Dictionaries are powerful built-in data structures in Python that store
  data as key-value pairs. Dictionary Comprehension can be super helpful in creating
  new dictionaries from existing dictionaries and iterables.

  In this tutorial, we''ll learn how di...'
---

Dictionaries are powerful built-in data structures in Python that store data as key-value pairs. Dictionary Comprehension can be super helpful in creating new dictionaries from existing dictionaries and iterables.

In this tutorial, we'll learn how dictionary comprehensions work in Python by coding some simple examples.

## What is a Dictionary in Python? 

Dictionaries in Python allow us to store a series of _mappings_ between two sets of values, namely, the _keys_ and the _values_. 

* All items in the dictionary are enclosed within a pair of curly braces`{}`.
* Each item in a dictionary is a mapping between a key and a value - called a _key-value_ pair.
* A key-value pair is often called a dictionary _item_.
* You can access these values using the respective keys.

Here's a generic example of a dictionary:

```
my_dict = {"key1":<value1>,"key2":<value2>,"key3":<value3>,"key4":<value4>}
```

In the above example,

* The dictionary `my_dict` contains 4 key-value pairs (items).
* `"key1"` through `"key4"` are the 4 keys. 
* You can use `my_dict["key1"]` to access `<value1>`, `my_dict["key2"]` to access `<value2>`, and so on.

Now that we know what a Python dictionary is, let's go ahead and learn about _Dictionary Comprehension_.

## How to Use Dictionary Comprehension to Create a Python Dictionary from an Iterable

In this section, let's use dictionary comprehension to create a Python dictionary from an iterable, say, a list or a tuple. 

We can create a new Python dictionary using only one iterable if we choose to generate either the keys or the values on the fly.

> When we choose to generate the values on the fly, we can use the items in the iterable as the keys and vice versa.

The general syntax is shown below. Please note that the names between <> are placeholders for the actual variable names.

```
<dict_name> = {<new_key>:<new_value> for <item> in <iterable>}
```

Let's parse the above syntax.

* `{}` indicates that we're populating a dictionary.
* For each item in the iterable, we generate a key-value pair in the dictionary.

▶ Time for a quick example.

## Python Dictionary Comprehension - Example 1

Let's say we have a list of customers who visit our store, and we'd like to offer a random discount to each customer. We'd like the discount value to be anywhere between $1 and $100.

> In Python, `random.randint(i,j)` returns a random integer between `i` and `j`, where both the end points are inclusive.

So, we can use the `randint()` function from Python's random module to generate a discount between $1 and $100 for every customer in our list.

The following code snippet shows how we can create `discount_dict`, a new dictionary, from the list of customers.

```python
import random
customers = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
discount_dict = {customer:random.randint(1,100) for customer in customers}
print(discount_dict)

#Output

{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}
```

The above example does the following:

* Loops through the list of customers (`customers`),
* Uses the name of each customer as the key, and
* Generates a random discount between $1 and $100 as the value against the key.

## How to Use Dictionary Comprehension to Create a Python Dictionary from Two Iterables

What if we already have pre-defined iterables that contain the keys and values? Say, you have two lists, `list_1` and `list_2` – with `list_1` containing the _keys_ and `list_2` containing the corresponding _values_.

We can now use Python's `zip()` function to zip these two lists to generate the key-value pairs.

> Note: The `zip` function takes in a sequence of iterables as the argument, and returns an iterator of tuples, as shown in the image below.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-95.png)

So, the first tuple is the first key-value pair, the second tuple is the second key-value pair, and in general, the i-th tuple is the i-th key-value pair.

In this case, the dictionary comprehension takes the following form:

```
<dict_name> = {<new_key>:<new_value> for (key,value) in zip(list1,list2)}
```

Parsing the above syntax is quite simple.

* The keys and values are available as tuples, as we've zipped them together using the `zip()` function.
* Now, we loop through this iterator of tuples to get the key-value pairs for our dictionary.

▶ Time for another quick example.

## Python Dictionary Comprehension - Example 2

Let's say we'd like to create a dictionary of weekly temperatures in our city. The days should be the keys, and the temperatures (in Celsius) corresponding to the days should be the values. 

Suppose we have the days and temperatures in two lists as shown below.

```python
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
```

We can now proceed to use dictionary comprehension to create a dictionary of weekly temperatures.

```python
# Creating a dictionary of weekly tempertaures
# from the list of temperatures and days

weekly_temp = {day:temp for (day,temp) in zip(days,temp_C)}

print(weekly_temp)

# Output
{'Sunday': 30.5, 'Monday': 32.6, 'Tuesday': 31.8, 'Wednesday': 33.4, 'Thursday': 29.8, 'Friday': 30.2, 'Saturday': 29.9}
```

In the above example, we've used the `zip()` function to zip together the lists of days and temperatures. We can now tap into the dictionary by using any day as they key to get the temperature on that day, as shown below:

```python
weekly_temp["Thursday"]
# Output
29.8
```

## How to Use the items() Method on a Python Dictionary

So far, we've seen how to use the keys to access the values. How do we access all the key-value pairs in the dictionary? 

To do this, we can call the `items()` method on the dictionary to get all the key-value pairs, as shown in the code snippet below.

```python
discount_dict.items()

# Output
dict_items([('Alex', 16), ('Bob', 26), ('Carol', 83), ('Dave', 21), ('Flow', 38), ('Katie', 47), ('Nate', 89)])
```

## How to Use Dictionary Comprehension to Create a Python Dictionary from an Existing Dictionary

Let's say we already have a Python dictionary. 📚

However, we'd like to create a _new_ dictionary that contains only the items from our dictionary that satisfy a particular condition. Dictionary Comprehension can be really handy in doing this.

```
<dict_name> = {<new_key>:<new_value> for (key,value) in <dict>.items() if <condition>}
```

Let's parse the above syntax. We use the `items()` method and get all key-value pairs in an existing dictionary.

* We access the first dictionary item, and check if the `condition` evaluates to  `True`. 
* If the condition is `True`, we add the first item to our new dictionary.
* We then repeat these steps for all items in the existing dictionary.

▶ Let's take an example to see how this works.

## Python Dictionary Comprehension - Example 3

Let's build on the earlier discount example where we created the `discount_dict` dictionary. Let's look at our `discount_dict` dictionary again.

```python
{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}

```

We see that some customers were lucky enough to get a higher discount than the others. Let's address this disparity and make all our customers happy. 😀

We'd now like to offer customers who were offered fewer than $30 discount, a 10% discount on their next purchase. ✨

In this case, we're creating a new dictionary `customer_10` from our `discount_dict` dictionary.

```python
customer_10 = {customer:discount for (customer, discount) in discount_dict.items() if discount<30}

print(customer_gifts)

# Output
{'Alex': 16, 'Bob': 26, 'Dave': 21}
```

The above code does the following:

* For each item in our `discount_dict`, it taps into the value of the discount.
* If the discount is fewer than $30, it adds the corresponding `customer:discount` pair to our new dictionary `customer_10`.

Notice how `Alex`, `Bob`, and `Dave` who got fewer than $30 discount have been added to the new dictionary. 

## Conclusion

Let's summarize what we've learned in this tutorial. We've seen how to use Dictionary Comprehension to create Python dictionaries from:

* only one iterable,
* two iterables, and
* an existing dictionary using conditions to filter through the items.

Thank you for reading. Happy learning!🎉

### Related Posts

Here's a post explaining the working of [Python's zip() function](https://www.freecodecamp.org/news/the-zip-function-in-python-explained-with-examples/).

