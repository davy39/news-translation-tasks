---
title: Python Dictionary Guide – How to Iterate Over, Copy, and Merge Dictionaries
  in Python 3.9
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-26T21:36:29.000Z'
originalURL: https://freecodecamp.org/news/python-dictionary-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/thumb.png
tags:
- name: Data Science
  slug: data-science
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "By Florian Dedov\nPython is a popular language for data science. And working\
  \ with collections is one of the most fundamental skills you need to have. \nCollections\
  \ are data structures that contain multiple elements of various different data types.\
  \ \nTod..."
---

By Florian Dedov

Python is a popular language for data science. And working with collections is one of the most fundamental skills you need to have. 

Collections are data structures that contain multiple elements of various different data types. 

Today we are going to take a detailed look at dictionaries, which are a special type of collection in Python. We will cover their basic functionality, their inner workings, and also some cutting-edge features of the latest Python version.

By the end of this tutorial, you'll know

<ul>
    <li>What dictionaries are</li>
    <li>How to work with dictionaries</li>
    <li>How to iterate over dictionaries</li>
    <li>How to copy dictionaries</li>
    <li>How to merge dictionaries in Python 3.9</li>
</ul>

## What Are Dictionaries in Python?

Before learning about something in depth, it is always good to start with a simple and basic definition. 

As I already said, dictionaries are a type of collection in Python. However, in contrast to lists, tuples and sets, you don’t store individual values but so-called _key-value pairs_. This means that instead of referring to your values through an index, you use a key, which is a unique identifier.

```python
l1 = [10, "Hello", True, 20.23] # List
t1 = (10, "Hello", True, 20.23) # Tuple
s1 = {10, "Hello", True, 20.23} # Set

d1 = {'number': 10,
      'greeting': "Hello",
      'boolean': True,
      'float': 20.23} # Dictionary

```

In the example above, you can see the difference. The individual key-value pairs are separated by commas. Each pair starts with a unique key followed by a colon and the respective value. Notice that the value doesn’t have to be unique, since we are not using it to access or identify anything. 

Also keep in mind that we can use any data type for the keys and values we want. Here we only use strings for the identifiers but we can also use integers, floats, collections or even Booleans. 

However, you should always ask yourself how reasonable this is. Most of the time a string will be the best choice.

## How to Work with Dictionaries in Python

Alright, now that we know what dictionaries are, let's take a look at how to work with them. 

First, we will go through the basic operations like accessing, adding, and removing values. After that we will look into some more advanced and more interesting topics.

You can access elements of a dictionary in Python in the same way as you access elements from any other collection. The only difference is that you pass a key rather than an index. This also goes for changing and even for appending values.

```python
person = {'name': "Mike", 'age': 25, 'weight': 80.5}

print(person['name'])
person['name'] = "Bob" # Changing existing value
print(person['name'])

person['gender'] = 'm' # Creating new key-value pair
print(person['gender'])

```

As you can see here, you just pass a key to access the value it refers to. First you print the name, then you change it. Then you print it again to make sure the changes were made. 

Notice that this doesn't only work for already existing pairs but also for new ones. In order to create a new key-value pair, just refer to a key that doesn’t exist yet and assign a value to it. The pair is then added to the dictionary automatically.

Removing values from a dictionary works differently. Here you can either use the **del** keyword or the **pop()** method. 

The main difference between those two approaches is that **del** only removes the key-value pair, whereas **pop()** also returns the removed value afterwards. Depending on your use-case you will have to decide which method fits your task better.

## How to Iterate Over Dictionaries in Python

Since dictionaries are collections, you can also iterate over them. But this is not as simple and straightforward as it is with the other collection types. 

This is because you are not dealing with individual values but with pairs. When you iterate over a dictionary, using a for loop, you are actually just iterating over the keys.

```python
names_ages = {'Bob': 50,
              'Anna': 28,
              'Max': 30,
              'John': 76}

for element in names_ages:
    print(element)
    
# Output: Bob  Anna  Max  John

```

Therefore, if you want to iterate over the values or even the whole pairs, you need to use additional methods. 

In order to access the values, you just have to call the **values()** method. It returns an iterator for all the values of the dictionary. 

To access the full pairs, you can call the **items()** method. Here you iterate over a list of tuples, where each tuple represents one key-value pair. 

Of course there is also the **keys()** method, in case you want to work with the dictionary keys outside of a for loop.

```python
print(list(names_ages.keys()))
print(list(names_ages.values()))
print(list(names_ages.items()))

# Output
# > ['Bob', 'Anna', 'Max', 'John']
# > [50, 28, 30, 76]
# > [('Bob', 50), ('Anna', 28), ('Max', 30), ('John', 76)]

```

One important thing to keep in mind here is that those methods do not return actual lists. They return objects, which you can use to iterate over the keys and values. But you can easily typecast those objects into lists by using the **list()** function.

## How to Copy Dictionaries in Python

Now we are getting into some more advanced stuff. 

You wouldn't believe how many times new and inexperienced programmers run into trouble because they copy collections the wrong way. They troubleshoot their projects for hours and are unable to find the problem. 

So pay attention here if you don’t want to experience that frustration yourself. 

Before we talk about copying collections and dictionaries, let's look at how you would usually copy primitive data types like integers.

```python
i1 = 20
i2 = i1

i2 += 10
print(i1, i2)

# Output: 20  30

```

When you want to create a new variable and copy the value of another integer into it, you just directly assign the variable. Then you can change the value of the second integer and work with it, without changing anything about the first one. 

This also works for Booleans, Floats, Strings etc. However, let’s see what happens, when we do this with a dictionary.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = d1
d2['c'] = 50

print(d1)
print(d2)

# Output
# {'a': 10, 'b': 20, 'c': 50}
# {'a': 10, 'b': 20, 'c': 50}

```

What happened here? Didn’t we do the same thing as before? Why does the first dictionary change, when we modify the second one? Isn’t it just a copy? 

The answer is a clear no. When you assign a dictionary to a new variable, you are actually passing a so-called _reference_. 

The second variable is not actually a dictionary but just another variable pointing to the same dictionary as the first one. Therefore, it doesn’t matter on which variable you apply changes, since they are all performed on the one dictionary they both are referring to.

If you want to create an actual shallow copy of a dictionary in Python, you need to either use the **dict()** function or call the **copy()** method of the dictionary. By doing that you create a new dictionary that has the same elements as the original.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = dict(d1)
d3 = d1.copy()

d2['b'] = 50
d3['a'] = -90
print(d1) # unchanged

```

Notice, however, that the objects inside the copy are still the exact same objects as in the first dictionary. Therefore, if they are more complex objects or collections, you will end up with a new separate dictionary (but the objects inside it will refer to the same objects as those in the first dictionary). 

In order to change that, you would have to make a so-called deep copy, but this is not in the scope of this article.

## How to Merge Dictionaries in Python

Last but not least, let's talk about the cutting-edge dictionary features of Python 3.9. These features are focused on merging dictionaries. 

Up until recently, programmers had to either use the **update()** method or make use of the unpacking operators.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}
d1.update(d2)
print(d1)

d1 = {'a': 10, 'b': 20, 'c': 30}
d3 = {**d1, **d2}
print(d3)

```

The main difference between those two approaches is that the **update()** method adds the values of one dictionary to another and applies the changes directly. The resulting dictionary is not returned but actually saved into the first object. 

When you use the unpacking operators, on the other hand, you create a new dictionary and put the key-value pairs of the two dictionaries into it by unpacking them.

Now you may be asking yourself what happens when you merge two dictionaries that have the same key inside them. 

You can think of that like this: The first dictionary creates the key-value pair and the second one overwrites it. So if you call the update method on the first collection and pass the second collection as an argument, the key-value pair of the second dictionary will end up in the result. 

The same goes for the unpacking. Whichever dictionary you pass last overwrites the previous ones.

So this is the old way of doing things. In Python 3.9, however, the merging and updating operators were introduced. They make joining dictionaries simpler.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}

d3 = d1 | d2  # Merging
d1 |= d2      # Updating

```

As you can see, the operator for merging is the same one that's used for the bitwise OR operation. The order of the dictionaries is important if you have identical keys in both dictionaries. The collection on the right overwrites the collection on the left. 

If you want to update the first dictionary instead of returning a new one, just combine the merging operator with the basic assignment operator. This way of merging dictionaries is the recommended method since Python 3.9.

If you are more of a visual or auditory learner, you can watch my video tutorial on merging dictionaries below.

%[https://www.youtube.com/watch?v=RWqPfsFK1eo]

## Wrapping Up

Alright, so you should now be very comfortable when working with dictionaries. You not only know what they are and how to use them but you also understand how they work on a deeper level. 

When working on a project, you will know how to copy dictionaries the right way. We even covered one of the cutting-edge features of the latest Python version. 

Make sure you go through the code snippets once again and understand how and why they work. This will make you a much better Python programmer.

If you are interested in more content like this, you can check out my YouTube channel [NeuralNine](https://www.youtube.com/c/NeuralNine/) or my website [neuralnine.com](https://www.neuralnine.com/). 

For Python enthusiasts I have a special Python book series that teaches you the language from scratch and also goes into more advanced topics like machine learning and computer vision. You can find it [here](https://www.neuralnine.com/books).

I hope you enjoyed this article and I wish you a great day! :)

