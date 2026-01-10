---
title: Python NamedTuple Examples – How to Create and Work with NamedTuples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-12T15:34:19.000Z'
originalURL: https://freecodecamp.org/news/python-namedtuple-examples-how-to-create-and-work-with-namedtuples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/named-tuple-2.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, you'll probably use a tuple to initialize a sequence that shouldn't\
  \ be modified elsewhere in the program. This is because tuples are immutable. \n\
  However, using a tuple may reduce the readability of your code as you cannot describe\
  \ what eac..."
---

In Python, you'll probably use a tuple to initialize a sequence that shouldn't be modified elsewhere in the program. This is because tuples are _immutable_. 

However, using a tuple may reduce the readability of your code as you cannot describe what each item in the tuple stands for. This is where NamedTuples can come in handy. 

A NamedTuple provides the immutability of a tuple, while also making your code easy to understand and use.

In this tutorial, you'll learn how to create and use NamedTuples effectively.

## Python Tuples – A Quick Recap

Before jumping into NamedTuples, let's quickly revisit Python tuples.

Tuples are powerful built-in data structures in Python. They're similar to Python lists in that they can hold items of different types, and in that you can slice through them. 

> However, tuples differ from lists in that they are _immutable_. This means you _cannot_ modify an existing tuple, and trying to do so will throw an error.

▶ Let's say you create the following tuple today. The tuple `house` contains five items that describe the house, namely, the city, the country, the year of construction, the area in sq. ft., and the number of rooms it has. This is shown in the code snippet below:

```python
house = ("Bangalore","India",2020,2018,4)
```

* This `house` is located in the city of Bangalore in India. 
* It was constructed in the year `2020`.
* And it has `4` rooms that collectively span an area of `2018` sq. ft.

Let's say your friend reads this line of code, or you come back a week later and read your code again. Given that you haven't added any comments as to what the values in the tuple stand for, there's certainly a problem of readability.

For example, you may have to end up guessing whether it's a house of area 2018 sq. ft. constructed in the year 2020, or if it's a house of area 2020 sq. ft. constructed in the year 2018. 🤔

You might suggest using a dictionary instead – you can specify _what_ the different values stand for as _keys_ of the dictionary, and the _actual_ values as the dictionary's _values_.

Head on to the next section for a quick recap on Python dictionaries.

## Python Dictionaries – A Quick Recap

With the motivation to improve the readability of the code, let's consider switching to Python dictionaries.

Dictionaries are built-in data structures that store value in _key-value pairs_. You can tap into a dictionary, and access its values using the keys.

So you can rewrite the tuple from the previous as a dictionary as follows:

```python
house = {"city":"Bangalore","country":"India","year":2020,"area":2018,"num_rooms":4}
```

In the code snippet above:

* `"city"`, `"country"`, `"year"`, `"area"` and `"num_rooms"` are the keys.
* And the values from the tuple, `"Bangalore"`, `"India"`, `2020`, `2018`, and `4` are used as the values corresponding to the keys.
* You can access the values using the keys: `house["city"]` to get `"Bangalore"`, `house["area"]` to get `2018`, and so on.

As you can see, using a dictionary improves the readability of the code. But, unlike tuples, you can always modify values in a dictionary. 

> All you need to do is to set the corresponding key to a different value.

In the above example, you can use `house["city"] = "Delhi"` to change the city your house is located in. Clearly, this is not allowed, as you don't want the values to be modified elsewhere in the program. 

And if you need to store descriptions for many such houses, you'll have to create as many dictionaries as the number of houses there are, repeating the names of the keys every single time. This also makes your code repetitive and not so interesting!

> With Python's NamedTuples, you can have both the immutability of tuples and the readability of dictionaries.

Head on to the next section to learn about `NamedTuple`s. 

## Python NamedTuple Syntax

To use a `NamedTuple`, you need to import it from Python's built-in collections module, as shown:

```python
from collections import namedtuple
```

The general syntax for creating a NamedTuple is as follows:

```python
namedtuple(<Name>,<[Names of Values]>)
```

* `<Name>` is a placeholder for what you'd like to call your NamedTuple, and
* `<[Names of Values]>` is a placeholder for the list containing the _names_ of the different values, or attributes.

Now that you're familiar with the syntax for creating NamedTuples, let's build on our `house` example, and try to create it as a NamedTuple.

## Python NamedTuple Example

As mentioned earlier, the first step is to import `namedtuple`.

```python
from collections import namedtuple


```

Now, you can create a NamedTuple using the syntax discussed in the previous section:

```python
House = namedtuple("House",["city","country","year","area","num_rooms"])
```

In this example,

* You choose to call the NamedTuple `House`, and
* Mention the names of the values, `"city"`, `"country"`, `"year"`, `"area"` and `"num_rooms"`  in a list.

✅ And you've created your first NamedTuple – `House`.

Now, you can create a house `house_1` with the required specifications using `House` as follows:

```python
house_1 = House("Bangalore","India",2020,2018,4)
```

You only need to pass in the actual values that the names, or attributes in your `<[Names of Values]>` should take.

To create another house, say `house_2`, all you need to do is to create a new `House` using its values.

```python
house_2 = House("Chennai","India",2018,2050,3)
```

> Notice how you can use `House` as a template to create as many houses as you'd like, without having to type out the names of the attributes each time you create a new house. 

## How to Use `dot` Notation to Access a NamedTuple's Values

Once you've created NamedTuple objects `house_1` and `house_2`, you can use the `dot` notation to access their values. The syntax is shown below:

```
<namedtuple_object>.<value_name>
```

* Here, `<namedtuple_object>` denotes the created NamedTuple object. In this example, `house_1` and `house_2`.
* `<value_name>` denotes any of the valid names used when the NamedTuple was created. In this example, `"city"`, `"country"`, `"year"`, `"area"` and `"num_rooms"` are the valid choices for `<value_name>`.

This is illustrated in the following code snippet:

```python
print(house_1.city)
print(house_1.country)
print(house_1.year)
print(house_1.area)
print(house_1.num_rooms)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-33.png)

Similarly, you can use `house_2.city`, `house_2.country`, and so on to access the values corresponding to the NamedTuple `house_2`.

## 📋Try it Yourself! NamedTuple Example

In this section, you'll create a `ProblemSet` NamedTuple. 

Please feel free to try this example in any IDE of your choice.

The `ProblemSet` NamedTuple should take the following values:

* `num_questions`: an integer representing the number of questions in a particular problem set,
* `difficulty`: a string that indicates the difficulty level of the problem set, and
* `topic`: the topic that the problem set covers, say, `"Arrays"`, `"Strings"`, `"Graphs"`, and so on.

The procedure is very similar to our previous example where we created the `House` NamedTuple.

1️⃣ Import `namedtuple` from `collections` module.

```python
from collections import namedtuple
```

2️⃣ Create a NamedTuple and call it `ProblemSet`.

```python
ProblemSet = namedtuple("ProblemSet",["num_questions","difficulty","topic"])
```

3️⃣ Now that you've created `ProblemSet`, you can create any number of problem sets using `ProblemSet` as the template.

* Here, `problem_set1` contains 5 easy questions on `Strings`.

```python
problem_set1 = ProblemSet(5,"Easy","Strings")
```

* And `problem_set2` contains 3 hard questions on `Bit Manipulation`.

```python
problem_set2 = ProblemSet(3,"Hard","Bit Manipulation")
```

4️⃣ As with the previous example, you can use the `dot` notation to access the values of the two problem sets created above.

```python
print(problem_set1.topic)

# Output
Strings
```

```python
print(problem_set2.difficulty)

# Output
Hard
```

I hope you were able to complete this exercise. 🎉

## Conclusion

In this tutorial, you've learned:

* how NamedTuples help you couple the advantages of both tuples and dictionaries,
* how to create NamedTuples, and
* how to use `dot` notation to access the values of  NamedTuples.

If you're familiar with OOP in Python, you may find this similar to how Python classes work. A class with its attributes serves as a template from which you can create as many objects, or instances – each with its own values for the attributes.

However, creating a class and defining the required attributes just to improve readability of your code can often be overkill, and it's a lot easier to create NamedTuples instead.

See you all in the next tutorial. Until then, happy coding! 

