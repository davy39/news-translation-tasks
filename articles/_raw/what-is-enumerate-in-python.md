---
title: What is enumerate() in Python? Enumeration Example
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-22T15:56:07.000Z'
originalURL: https://freecodecamp.org/news/what-is-enumerate-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-yan-krukov-8612931.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Suchandra Datta\nThe enumerate() function is one of the built-in functions\
  \ in Python. It provides a handy way to access each item in an iterable, along with\
  \ a count value that specifies the order in which the item was accessed. \nIn this\
  \ article you..."
---

By Suchandra Datta

The `enumerate()` function is one of the built-in functions in Python. It provides a handy way to access each item in an iterable, along with a count value that specifies the order in which the item was accessed. 

In this article you will learn all that you need to get started using `enumerate()` in your code. Namely, we will explore:

* When you'd want to use enumerate
* `enumerate()` syntax and input arguments
* different ways to invoke `enumerate()` using built-in iterables
* how to invoke `enumerate()` using a custom iterable
* how to use `enumerate()` in a for loop

Let's get started.

## When Should You Use Enumerate?

Let's take an example. Suppose we have a list of student names:

```python
names = ["Wednesday", "Enid", "Rowan", "Bianca"]
```

We want to create a list of tuples, where each tuple item contains a student ID number and student name like this:

```python
[(0, 'Wednesday'), (1, 'Enid'), (2, 'Rowan'), (3, 'Bianca')]
```

The student ID is the index of the student name in the names list. So in the tuple (3, 'Bianca') student Bianca has an ID of 3 since Bianca is at index 3 in the names list. Similarly in (0, 'Wednesday'), student Wednesday has an ID of 0 since she is at index 0 in the names list.

Whenever we come across situations when we want to use a list item as well the index of that list item together, we use `enumerate()`. `enumerate()` will automatically keep track of the order in which items are accessed, which gives us the index value without the need to maintain a separate index variable.

Here's how we can create the student ID and name list of tuples using `enumerate()`:

```python
list(enumerate(names))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-119.png)

Let's take a closer look at the syntax for this function.

## enumerate() syntax and input arguments

First, let's look at **`enumerate(iterable, start=0)`.**

Enumerate needs only two input arguments:

* an iterable, such as a list, tuple, string, dictionary or any object which has the  `__next__` and `__iter__`  methods defined (which means it supports iteration). This argument is mandatory.
* a start value for the count, which defaults to zero

`enumerate()` will return an enumerate object which essentially holds a list of tuples. Each tuple contains an item from the iterable and the item's count value.

For more details on the input arguments and variations, you can refer to the documentation [here](https://docs.python.org/3/library/functions.html#enumerate).

We can call enumerate like this:

```python
enumerate(names)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-109.png)

The output `<enumerate at 0x1d02258>` is the enumerate object. To view the elements of the enumeration, we can use a list like this:

```python
list(enumerate(names))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-120.png)

We get a list of tuples. Each tuple is of the form (count, element of names list) with the default start value of zero, so the count starts at zero. 

The 1st element of names list and count = 0 forms the 1st tuple. The second element of the names list and count = 1 forms the second tuple. Similarly, the 4th element of the names list and count = 3 forms the last tuple. 

## How to Invoke `enumerate()` Using Built-in Iterables

There are different ways to invoke `enumerate()`, such as:

* invoking `enumerate()` with a specific start value
* invoking `enumerate()` and converting the output to a list, tuple, or dictionary
* invoking `enumerate()` with a dictionary as input

Let's look at each of these with examples.

### How to invoke `enumerate()` with a specific start value

You'll want to use this option when you have a requirement that the index values must start from some specific value. For example, for this student name list:

```python
names = ["Wednesday", "Enid", "Rowan", "Bianca"]
```

We want a list of student IDs and names with the restriction that the IDs must start from 1. In that case, we can invoke enumerate with a start parameter like this:

```python
list(enumerate(names, start=1))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-121.png)

Now the count value returned by enumerate starts at 1 and not zero like in the previous output. If we have a restriction that student IDs must start from 100, then we can get the desired output by just making start=100:

```python
list(enumerate(names, start=100))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-122.png)

### How to invoke `enumerate()` and convert the output to a list, tuple, or dictionary

We can convert the output of enumeration into a list, tuple, or dictionary by calling the corresponding constructor of that type.

To get a list, we use this syntax:

```python
list(enumerate(names))
```

For a tuple, we use this syntax:

```python
tuple(enumerate(names))
```

Notice how the outputs look almost alike, except the tuples in the first one are enclosed in `[ ]`, signifying it is a list of tuples. In the second one, they're enclosed in `( )` meaning it is a tuple of tuples:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-123.png)

For a dictionary, use the constructor like this:

```python
dict(enumerate(names))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-124.png)

### How to invoke `enumerate()` with a dictionary as input

The default way enumerate treats dictionaries is a little different than how it works with lists or tuples. 

Dictionaries are a mapping type with a key value pair, and `enumerate()` only iterates over the keys and not the values by default.

 For example,

```python
names_and_special_powers = {"Wednesday":"psychic", "Enid":"werewolf", "Tyler":"normie"}
print(tuple(enumerate(names_and_special_powers)))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-112.png)

Enumerate only considers the keys of the dictionary and returns the count value. This is not useful when we want an index for both the key and the value. 

We can enumerate over both keys and values like this:

```python
names_and_special_powers = {"Wednesday":"psychic", "Enid":"werewolf", "Tyler":"normie"}
print(tuple(enumerate(names_and_special_powers.items())))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-113.png)

## How to Invoke `enumerate()` Using a Custom Iterable

We may often come across situations when we need to maintain a collection of user-defined objects and iterate over that collection. Any object is an iterable if it has the `__iter__` and `__next__` methods defined. 

In this section, we'll learn how to create our own iterable and then use enumerate with it.

Let's say we want to keep track of which students are attending a fictional school called Nevermore Academy in which year. We create a Student class to represent each student and a Nevermore class to represent the school. 

We want to perform the same task like we did previously: create a list of tuples with student ID and student name. But now, instead of a list, we have to deal with a list of objects stored in an instance variable of an object of type Nevermore. 

Here's the definition for the Student class. For each student, we have two instance variables – student name and special power of the student.

```python
#Create a class Student that has instance variables - student name, student power
class Student:
    def __init__(self, name, power):
        self.name=name
        self.power=power
```

Now let's create a few Student objects:

```python
student_1 = Student("Rowan","telekinesis")
student_2 = Student("Enid", "werewolf")
student_3 = Student("Wednesday", "psychic")
student_4 = Student("Bianca","siren")
```

Next, let's define the Nevermore class. It has 3 instance variables to store year, the list of Student objects who are attending Nevermore for that year, and an index variable i. This variable will be used for iteration in the `__next__` method.

The constructor looks like this:

```python
class Nevermore:
    def __init__(self, year):
        self.year=year
        self.students=[]
        #This variable will be the index using which we will return values from students array in the __next__ method
        self.i=-1
```

Let's add an instance method using which the `students` instance variable will be populated:

```python
 def add(self, Student):
        self.students.append(Student)
```

It takes as input a Student object and appends it to the list.

Next, we define the methods we need to make it an iterable:

```python
def __iter__(self):
        return self
    
def __next__(self):
        self.i = self.i + 1
        if self.i < len(self.students):
            return self.students[self.i].name
        else:
            raise StopIteration
```

Enumerate will be accessing the items in the iterable based on what the `__next__` method returns. 

In `__next__` we go over the list using the instance variable i as the index. So long as the index is valid we return the name of the Student object in the students array. 

Once we have gone over all students, we raise a StopIteration exception, which is a standard method to signify the end of iteration.

Here's the full class definition:

```python
#Create a class that contains batch year and a list of student objects
class Nevermore:
    def __init__(self, year):
        self.year=year
        self.students=[]
        #This variable will be the index using which we will return values from students array in the __next__ method
        self.i=-1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.i = self.i + 1
        if self.i < len(self.students):
            return self.students[self.i].name
        else:
            raise StopIteration
    def add(self, Student):
        self.students.append(Student)
```

Let's create a Nevermore object for the year 2022:

```python
batch = Nevermore("2022")
```

And now let's add some students to the 2022 batch:

```
batch.add(student_1)    
batch.add(student_2)
batch.add(student_3)
batch.add(student_4)
```

`batch` is now our custom object that has instance variables – year, a string, and students, a list of Student objects. We now invoke enumerate like this:

```
print(list(enumerate(batch)))
```

We'll get the output like this, where we have the count in which the student object is accessed, which is our student ID and the student name. We added Rowan first to the list so the count value is 0. We added Enid second so the count value is 1, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-125.png)

## How to use `enumerate()` in a for loop

In our applications, we might want to use the output from enumerate for further processing, like getting the student ID and name and then using that value to access another data structure. The most common way to utilize `enumerate()` is through a for loop.

We can unpack the output of the enumeration within a for loop like this:

```python
names = ["Wednesday", "Enid", "Rowan", "Bianca"]
for student_id, name in enumerate(names):
    print("student_id = {}\tstudent name = {}".format(student_id, name))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-126.png)

`enumerate()` returns a tuple for each iterable item. The first value in the tuple is the count value which we store in the `student_id` for loop variable. The second value in the tuple is the list item which we store in the `name` for loop variable. 

We might have a dataframe where, corresponding to each student, we have certain other information like extra curricular activities. We set the index to `student_id` so we can access any row in the `df` using the `student_id` value using `df.loc method`

```python
import pandas as pd

df = pd.DataFrame(data=[[3, "Choir"], [2, "NA"], [0, "Bee keeping"], [1, "Blogging"]], \
                  columns=["student_id", "extra_curricular"])
df = df.set_index("student_id")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-129.png)

Using the student_id and name from enumeration, we can access the dataframe like this:

```python
for student_id, name in enumerate(names):
    print("student_id = {}\tstudent name = {} \nExtra currcilar = {}\n".format(student_id, name, df.loc[student_id]["extra_curricular"]))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-128.png)

## Wrapping Up

In this article, we learnt about the enumerate method and when to use it. We looked at an example where it is useful to have index values along with iterable items together, `enumerate` input arguments, how to invoke it using lists, dictionaries, custom objects, and how to use it in a for loop. 

I hope it helped you in your Python coding and I wish you all the very best in your Python learning journey. 

