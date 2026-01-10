---
title: Mutable vs Immutable Objects in Python – A Visual and Hands-On Guide
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2020-11-11T19:01:31.000Z'
originalURL: https://freecodecamp.org/news/mutable-vs-immutable-objects-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95a1740569d1a4ca0dd3.jpg
tags:
- name: pythonic programming
  slug: pythonic-programming
- name: immutability
  slug: immutability
- name: mutable
  slug: mutable
- name: object
  slug: object
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: null
seo_desc: "Python is an awesome language. Because of its simplicity, many people choose\
  \ it as their first programming language. \nExperienced programmers use Python all\
  \ the time as well, thanks to its wide community, abundance of packages, and clear\
  \ syntax.\nBut ..."
---

Python is an awesome language. Because of its simplicity, many people choose it as their first programming language. 

Experienced programmers use Python all the time as well, thanks to its wide community, abundance of packages, and clear syntax.

But there's one issue that seems to confuse beginners as well as some experienced developers: Python objects. Specifically, the difference between **mutable** and **immutable** objects.

In this post we will deepen our knowledge of Python objects, learn the difference between **mutable** and **immutable** objects, and see how we can use the **interpreter** to better understand how Python operates. 

We will use important functions and keywords such as `id` and `is`, and we'll understand the difference between `x == y` and `x is y`.

Are you up for it? Let's get started.

# In Python, everything is an object

Unlike other programming languages where the language _supports_ objects, in Python really **everything** is an object – including integers, lists, and even functions.

We can use our interpreter to verify that:

```python
>>> isinstance(1, object)
True

>>> isinstance(False, object)
True

def my_func():
   return "hello"
   
>>> isinstance(my_func, object)
True
```

Python has a built-in function, `id`, which returns the address of an object in memory. For example:

```python
>>> x = 1
>>> id(x)
1470416816
```

Above, we created an **object** by the name of `x`, and assigned it the value of `1`. We then used `id(x)` and discovered that this object is found at the address `1470416816` in memory.

This allows us to check interesting things about Python. Let's say we create two variables in Python – one by the name of `x`, and one by the name of `y` – and assign them the same value. For example, here:

```python
>>> x = "I love Python!"
>>> y = "I love Python!"
```

We can use the equality operator (`==`) to verify that they indeed have the same value in Python's eyes:

```python
>>> x == y
True
```

But are these the same object in memory? In theory, there can be two very different scenarios here. 

According to scenario **(1)**, we really have two different objects, one by the name of `x`, and another by the name of `y`, that just happen to have the same value. 

Yet, it could also be the case that Python actually stores here only one object, which has two names that reference it – as shown in scenario **(2)**:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-19.png)

We can use the `id` function introduced above to check this:

```python
>>> x = "I love Python!"
>>> y = "I love Python!"
>>> x == y
True

>>> id(x)
52889984

>>> id(y)
52889384
```

So as we can see, Python's behavior matches scenario (1) described above. Even though `x == y` in this example (that is, `x` and `y` have the same _values_), they are different objects in memory. This is because `id(x) != id(y)`, as we can verify explicitly:

```python
>>> id(x) == id(y)
False
```

There is a shorter way to make the comparison above, and that is to use Python's `is` operator. Checking whether `x is y` is the same as checking `id(x) == id(y)`, which means whether `x` and `y` are the same object in memory:

```python
>>> x == y
True

>>> id(x) == id(y)
False

>>> x is y
False
```

This sheds light on the important difference between the equality operator `==` and the identity operator `is`. 

As you can see in the example above, it is completely possible for two names in Python (`x` and `y`) to be bound to two different objects (and thus, `x is y` is `False`), where these two objects have the same value (so `x == y` is `True`).

How can we create another variable that points to the same object that `x` is pointing to? We can simply use the assignment operator `=`, like so:

```python
>>> x = "I love Python!"
>>> z = x
```

To verify that they indeed point to the same object, we can use the `is` operator:

```python
>>> x is z
True
```

Of course, this means they have the same address in memory, as we can verify explicitly by using `id`:

```python
>>> id(x)
54221824

>>> id(z)
54221824
```

And, of course, they have the same value, so we expect `x == z` to return `True` as well:

```python
>>> x == z
True
```

# Mutable and immutable objects in Python

We have said that everything in Python is an object, yet there is an important distinction between objects. Some objects are **mutable** while some are **immutable**. 

As I mentioned before, this fact causes confusion for many people who are new to Python, so we are going to make sure it's clear.

## Immutable objects in Python

For some types in Python, once we have created instances of those types, they never change. They are **immutable**. 

For example, `int` objects are immutable in Python. What will happen if we try to change the value of an `int` object?

```python
>>> x = 24601
>>> x
24601

>>> x = 24602
>>> x
24602
```

Well, it seems that we changed `x` successfully. This is exactly where many people get confused. What exactly happened under the hood here? Let's use `id` to further investigate:

```python
>>> x = 24601
>>> x
24601

>>> id(x)
1470416816

>>> x = 24602
>>> x
24602

>>> id(x)
1470416832
```

So we can see that by assigning `x = 24602`, we didn't change the value of the object that `x` had been bound to before. Rather, we created a new object, and bound the name `x` to it. 

So after assigning `24601` to `x` by using `x = 24601`, we had the following state:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-46.png)

And after using `x = 24602`, we created a new object, and bound the name `x` to this new object. The other object with the value of `24601` is no longer reachable by `x` (or any other name in this case):

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-47.png)

Whenever we assign a new value to a name (in the above example - `x`) that is bound to an `int` object, we actually change the binding of that name to another object. 

The same applies for `tuple`s, strings (`str` objects), and `bool`s as well. In other words, `int` (and other number types such as `float`), `tuple`, `bool`, and `str` objects are **immutable**.

Let's test this hypothesis. What happens if we create a `tuple` object, and then give it a different value? 

```python
>>> my_tuple = (1, 2, 3)
>>> id(my_tuple)
54263304

>>> my_tuple = (3, 4, 5)
>>> id(my_tuple)
56898184
```

Just like an `int` object, we can see that our assignment actually changed the object that the name `my_tuple` is bound to.

What happens if we try to change one of the `tuple`'s elements?

```python
>>> my_tuple[0] = 'a new value'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

As we can see, Python doesn't allow us to modify `my_tuple`'s contents, as it is immutable.

## Mutable objects in Python

Some types in Python can be modified after creation, and they are called **mutable**. For example, we know that we can modify the contents of a `list` object:

```python
>>> my_list = [1, 2, 3]
>>> my_list[0] = 'a new value'
>>> my_list
['a new value', 2, 3]
```

Does that mean we actually created a new object when assigning a new value to the first element of `my_list`? Again, we can use `id` to check:

```python
>>> my_list = [1, 2, 3]
>>> id(my_list)
55834760

>>> my_list
[1, 2, 3]

>>> my_list[0] = 'a new value'
>>> id(my_list)
55834760

>>> my_list
['a new value', 2, 3]
```

So our first assignment `my_list = [1, 2, 3]` created an object in the address `55834760`, with the values of `1`, `2`, and `3`:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-22.png)

We then modified the first element of this `list` object using `my_list[0] = 'a new value'`, that is - without creating a new `list` object:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-23.png)

Now, let us create two names – `x` and `y`, both bound to the same `list` object. We can verify that either by using `is`, or by explicitly checking their `id`s:

```python
>>> x = y = [1, 2]
>>> x is y
True

>>> id(x)
18349096

>>> id(y)
18349096

>>> id(x) == id(y)
True
```

What happens now if we use `x.append(3)`? That is, if we add a new element (`3`) to the object by the name of `x`?

Will `x` by changed? Will `y`?

Well, as we already know, they are basically two names of the same object:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-28.png)

Since this object is changed, when we check its names we can see the new value:

```python
>>> x.append(3)
>>> x
[1, 2, 3]

>>> y
[1, 2, 3]
```

Note that `x` and `y` have the same `id` as before – as they are still bound to the same `list` object:

```python
>>> id(x)
18349096

>>> id(y)
18349096
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-27.png)

In addition to `list`s, other Python types that are mutable include `set`s and `dict`s.

# Implications for dictionary keys in Python

Dictionaries (`dict` objects) are commonly used in Python. As a quick reminder, we define them like so:

```python
my_dict = {"name": "Omer", "number_of_pets": 1}
```

We can then access a specific element by its key name:

```python
>>> my_dict["name"]
'Omer'
```

Dictionaries are **mutable**, so we can change their content after creation. At any given moment, a key in the dictionary can point to one element only:

```python
>>> my_dict["name"] = "John"
>>> my_dict["name"]
'John'
```

It is interesting to note that a **dictionary's keys must be immutable**:

```python
>>> my_dict = {[1,2]: "Hello"}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Why is that so? 

Let's consider the following hypothetical scenario (note: the snippet below can't really be run in Python):

```python
>>> x = [1, 2]
>>> y = [1, 2, 3]
>>> my_dict = {x: 'a', y: 'b'}
```

So far, things don't seem that bad. We'd assume that if we access `my_dict` with the key of `[1, 2]`, we will get the corresponding value of `'a'`, and if we access the key `[1, 2, 3]`, we will get the value `'b'`. 

Now, what would happen if we attempted to use:

```python
>>> x.append(3)
```

In this case, `x` would have the value of `[1, 2, 3]`, and `y` would also have the value of `[1, 2, 3]`. What should we get when we ask for `my_dict[[1, 2, 3]]`? Will it be `'a'` or `'b'`? To avoid such cases, Python simply doesn't allow dictionary keys to be mutable.

# Taking things a bit further

Let's try to apply our knowledge to a case that is a bit more interesting.

Below, we define a `list` (a **mutable** object) and a `tuple` (an **immutable** object). The `list` includes a `tuple`, and the `tuple` includes a `list`:

```python
>>> my_list = [(1, 1), 2, 3]
>>> my_tuple = ([1, 1], 2, 3)
>>> type(my_list)
<class 'list'>

>>> type(my_list[0])
<class 'tuple'>

>>> type(my_tuple)
<class 'tuple'>

>>> type(my_tuple[0])
<class 'list'>
```

So far so good. Now, try to think for yourself – what will happen when we try to execute each of the following statements?

(1) `>>> my_list[0][0] = 'Changed!'`

(2) `>>> my_tuple[0][0] = 'Changed!'`

In statement (1), what we are trying to do is change `my_list`'s first element, that is, a `tuple`. Since a `tuple` is **immutable**, this attempt is destined to fail:

```python
>>> my_list[0][0] = 'Changed!'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Note that what we were trying to do is _not_ change the list, but rather – change the contents of its first element. 

Let's consider statement (2). In this case, we are accessing `my_tuple`'s first element, which happens to be a `list`, and modify it. Let's further investigate this case and look at the addresses of these elements:

```python
>>> my_tuple = ([1, 1], 2, 3)
>>> id(my_tuple)
20551816

>>> type(my_tuple[0])
<class 'list'>

>>> id(my_tuple[0])
20446248
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-29.png)

When we change `my_tuple[0][0]`, we do not really change `my_tuple` at all! Indeed, after the change, `my_tuple`'s first element will still be the object whose address in memory is `20446248`. We do, however, change the value of that object:

```python
>>> my_tuple[0][0] = 'Changed!'
>>> id(my_tuple)
20551816

>>> id(my_tuple[0])
20446248

>>> my_tuple
(['Changed!', 1], 2, 3)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-48.png)

Since we only modified the value of `my_tuple[0]`, which is a mutable `list` object, this operation was indeed allowed by Python.

# Recap

In this post we learned about Python objects. We said that in Python **everything is an object**, and got to use `id` and `is` to deepen our understanding of what's happening under the hood when using Python to create and modify objects.

We also learned the difference between **mutable** objects, that can be modified after creation, and **immutable** objects, which cannot. 

We saw that when we ask Python to modify an immutable object that is bound to a certain name, we actually create a new object and bind that name to it.

We then learned why dictionary keys have to be **immutable** in Python.

Understanding how Python "sees" objects is a key to becoming a better Python programmer. I hope this post has helped you on your journey to mastering Python.

[_Omer Rosenbaum_](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/)_,_ [_Swimm_](https://swimm.io/)_’s Chief Technology Officer. Cyber training expert and Founder of Checkpoint Security Academy. Author of_ [_Computer Networks (in Hebrew)_](https://data.cyber.org.il/networks/networks.pdf)_. Visit My_ [_YouTube Channel_](https://www.youtube.com/watch?v=79jlgESHzKQ&list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)_._

