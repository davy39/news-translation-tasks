---
title: The Python Sort List Array Method – Ascending and Descending Explained with
  Examples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-04-12T12:57:47.000Z'
originalURL: https://freecodecamp.org/news/the-python-sort-list-array-method-ascending-and-descending-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/sort-method.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'If you want to learn how to work with the sort() method in your Python
  projects, then this article is for you. This method is very powerful and you can
  customize it to fit your needs, so let''s see how it works in detail.

  You will learn:


  How to use t...'
---

If you want to learn how to work with the `sort()` method in your Python projects, then this article is for you. This method is very powerful and you can customize it to fit your needs, so let's see how it works in detail.

**You will learn:**

* How to use this method and customize its functionality.
* When to use it and when not to use it.
* How to call it passing different combinations of arguments.
* How to sort a list in ascending and descending order. 
* How to compare the elements of a list based on intermediate values.
* How you can pass lambda functions to this method.
* How this method compares to the `sorted()` function.
* Why the `sort()` method performs a stable sort.
* How the process of mutation works behind the scenes.

Are you ready? Let's begin! ⭐

## 🔹 Purpose and Use Cases

With the `sort()` method, you can sort a list in either:

* Ascending Order
* Descending Order

This method is used to sort a list in place, which means that it **mutates** it or modifies it directly without creating additional copies, so remember:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-113.png)

You will learn more about mutation in this article (I promise!), but for now it's very important that you know that the `sort()` method modifies the list, so its original version is lost.

Because of this, you should only use this method if:

* You want to modify (sort) the list permanently. 
* You don't need to keep the original version of the list. 

If this fits your needs, then the `.sort()` method is exactly what you are looking for.

## 🔸 Syntax and Arguments

Let's see how you can call `.sort()` to take advantage of its full power. 

This is the most basic call (with no arguments):

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-41.png)

If you don't pass any arguments, by default:

* The list will be sorted in ascending order.
* The elements of the list will be compared directly using their values with the `<` operator.

For example:

```python
>>> b = [6, 3, 8, 2, 7, 3, 9]
>>> b.sort()
>>> b
[2, 3, 3, 6, 7, 8, 9] # Sorted!
```

### Custom Arguments  

To customize how the `sort()` method works, you can pass two optional arguments: 

* Key 
* Reverse

Let's see how they change the behavior of this method. Here we have a method call with these two arguments:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-42.png)

Before explaining how they work, I would like to explain something that you probably noticed in the diagram above – in the method call, the names of the parameters have to be included before their corresponding values, like this:

* `key=<f>`
* `reverse=<value>`

This is because they are [**keyword-only arguments**](https://docs.python.org/3/glossary.html#keyword-only-parameter). If you are passing a custom value for them, their **names** have to be specified in the method call, followed by an equal sign `=` and their corresponding values, like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-46.png)

Otherwise, if you try to pass the arguments directly as we normally do for positional parameters, you will see this error because the function will not know which argument corresponds to which parameter:

```python
TypeError: sort() takes no positional arguments
```

### Reverse

Now that you know what keyword-only arguments are, let's start with `reverse`.

The value of `reverse` can be either `True` or `False`:

* `False` means that the list will be sorted in ascending order.
* `True` means that the list will be sorted in descending (reverse) order.

**💡 Tip:** By default, its value is `False` – if you don't pass any arguments for this parameter, the list is sorted in ascending order.

Here we have a few examples:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-123.png)
_By default, reverse is False_

```python
# List of Integers
>>> b = [6, 3, 8, 2, 7, 3, 9]
>>> b.sort()
>>> b
[2, 3, 3, 6, 7, 8, 9]

# List of Strings
>>> c = ["A", "Z", "D", "T", "U"]
>>> c.sort()
>>> c
['A', 'D', 'T', 'U', 'Z']

```

💡 **Tip:** If the elements of the list are strings, they are sorted alphabetically.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-117.png)
_To specify that reverse is True, so the list has to be sorted in descending (reverse) order._

```python
# List of Integers
>>> b = [6, 3, 8, 2, 7, 3, 9]
>>> b.sort(reverse=True)
>>> b
[9, 8, 7, 6, 3, 3, 2]

# List of Strings
>>> c = ["A", "Z", "D", "T", "U"]
>>> c.sort(reverse=True)
>>> c
['Z', 'U', 'T', 'D', 'A']
```

💡 **Tip:** Notice how the list is sorted in descending order if `reverse` is `True`.

### Key

Now that you know how to work with the `reverse` parameter, let's see the `key` parameter. 

This parameter is a little bit more detailed because it determines how the elements of the list are be compared during the sorting process.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-120.png)
_Basic Syntax_

The value of `key` is either:

* `None`, which means that the elements of the list will be compared directly. For example, in a list of integers, the integers themselves can be used for the comparison.
* **A** **function** of one argument that generates an intermediate value for each element. This intermediate value is calculated only once and it's used to make the comparisons during the entire sorting process. We use this when we don't want to compare the elements directly, for example, when we want to compare strings based on their length (the intermediate value). 

💡 **Tip:** By default, the value of `key` is `None`, so the elements are compared directly.

**For example:** 

Let's say that we want to sort a list of strings based on their length, from the shortest string to the longest string. We can pass the function `len` as the value of `key`, like this:

```python
>>> d = ["aaa", "bb", "c"]
>>> d.sort(key=len)
>>> d
['c', 'bb', 'aaa']
```

💡 **Tip:** Notice that we are only passing the name of the function (`len`) without parenthesis because we are not calling the function. This is very important.

Notice the difference between comparing the elements directly and comparing their length (see below). Using the default value of `key` (`None`) would have sorted the strings alphabetically (left), but now we are sorting them based on their length (right):

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-49.png)

What happens behind the scenes? Each element is passed as an argument to the `len()` function, and the value returned by this function call is used to perform the comparisons during the sorting process:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-122.png)

This results in a list with a different sorting criteria: length.

**Here we have another example:**

Another interesting example is sorting a list of strings as if they were all written in lowercase letters (for example, making "Aa" equivalent to "aa").

According to lexicographical order, capital letters come before lowercase letters:

```python
>>> "E" < "e"
True
```

So the string `"Emma"` would come before `"emily"` in a sorted list, even if their lowercase versions would be in the opposite order:

```
>>> "Emma" < "emily"
True
>>> "emma" < "emily"
False
```

To avoid distinguishing between capital and lowercase letters, we can pass the function `str.lower` as `key`. This will generate a lowercase version of the strings that will be used for the comparisons:

```python
>>> e = ["Emma", "emily", "Amy", "Jason"]
>>> e.sort(key=str.lower)
>>> e
['Amy', 'emily', 'Emma', 'Jason']
```

Notice that now, `"emily"` comes before `"Emma"` in the sorted list, which is exactly what we wanted.

💡 **Tip:** if we had used the default sorting process, all the strings that started with an uppercase letter would have come before all the strings that started with a lowercase letter:

```python
>>> e = ["Emma", "emily", "Amy", "Jason"]
>>> e.sort()
>>> e
['Amy', 'Emma', 'Jason', 'emily']
```

**Here is an example using Object-Oriented Programming (OOP):**

If we have this very simple Python class:

```python
>>> class Client:
	def __init__(self, age):
		self.age = age
```

And we create four instances:

```python
>>> client1 = Client(67)
>>> client2 = Client(23)
>>> client3 = Client(13)
>>> client4 = Client(35)
```

We can make a list that references them:

```python
>>> clients = [client1, client2, client3, client4]
```

Then, if we define a function to get the `age` of these instances:

```python
>>> def get_age(client):
	return client.age
```

We can sort the list based on their age by passing the `get_age` function an an argument:

```python
>>> clients.sort(key=get_age)
```

This is the final, sorted version of the list. We use a for loop to print the age of the instances in the order that they appear in the list:

```python
>>> for client in clients:
	print(client.age)

	
13
23
35
67
```

Exactly what we wanted – now the list is sorted in ascending order based on the age of the instances. 

💡 **Tip:** Instead of defining a `get_age` function, we could have used a lambda function to get the age of each instance, like this:

```python
>>> clients.sort(key=lambda x: x.age)
```

**Lambda functions** are small and simple anonymous functions, which means that they don't have a name. They are very helpful for these scenarios when we only want to use them in particular places for a very short period of time. 

This is the basic structure of the lambda function that we are using to sort the list:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-90.png)
_Basic Structure of a Lambda Function_

### Passing Both Arguments

Awesome! Now you know to customize the functionality of the `sort()` method. But you can take your skills to a whole new level by combining the effect of `key` and `reverse` in the same method call:

```python
>>> f = ["A", "a", "B", "b", "C", "c"]
>>> f.sort(key=str.lower, reverse=True)
>>> f
['C', 'c', 'B', 'b', 'A', 'a']
```

These are the different combinations of the arguments and their effect:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-124.png)

### The Order of Keyword-Only Arguments Doesn't Matter

Since we are specifying the names of the arguments, we already know which value corresponds to which parameter, so we can include either `key` or `reverse` first in the list and the effect will be exactly the same.

So this method call:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-53.png)

Is equivalent to:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-54.png)

This is an example:

```python
>>> a = ["Zz", "c", "y", "o", "F"]
>>> a.sort(key=str.lower, reverse=True)
>>> a
['Zz', 'y', 'o', 'F', 'c']
```

If we change the order of the arguments, we get the exact same result:

```python
>>> a = ["Zz", "c", "y", "o", "F"]
>>> a.sort(reverse=True, key=str.lower)
>>> a
['Zz', 'y', 'o', 'F', 'c']
```

## 🔹 Return Value

Now let's talk a little bit about the return value of this method. The `sort()` method returns `None` – it does **not** return a sorted version of the list, like we might intuitively expect. 

According to the [Python Documentation](https://docs.python.org/3/library/stdtypes.html#list.sort):

> To remind users that it operates by side effect, it does not return the sorted sequence.

Basically, this is used to remind us that we are modifying the original list in memory, not generating a new copy of the list.

This is an example of the return value of `sort()`:

```python
>>> nums = [6.5, 2.4, 7.3, 3.5, 2.6, 7.4]

# Assign the return value to this variable:
>>> val = nums.sort()

# Check the return value:
>>> print(val)
None
```

See? `None` was returned by the method call.

**💡 Tip:** It is very important not to confuse the `sort()` method with the `sorted()` function, which is a function that works very similarly, but **doesn't** modify the original list. Instead `sorted()` generates and returns a new copy of the list, already sorted.

This is an example that we can use to compare them:

```python
# The sort() method returns None
>>> nums = [6.5, 2.4, 7.3, 3.5, 2.6, 7.4]
>>> val = nums.sort()
>>> print(val)
None
```

```python
# sorted() returns a new sorted copy of the original list
>>> nums = [6.5, 2.4, 7.3, 3.5, 2.6, 7.4]
>>> val = sorted(nums)
>>> val
[2.4, 2.6, 3.5, 6.5, 7.3, 7.4]

# But it doesn't modify the original list
>>> nums
[6.5, 2.4, 7.3, 3.5, 2.6, 7.4]
```

This is very important because their effect is very different. Using the `sort()` method when you intended to use `sorted()` can introduce serious bugs into your program because you might not realize that the list is being mutated.

## 🔸 The sort() Method Performs a Stable Sort

Now let's talk a little bit about the characteristics of the sorting algorithm used by `sort()`.

This method performs a stable sort because it works with an implementation of [TimSort](https://en.wikipedia.org/wiki/Timsort), a very efficient and stable sorting algorithm.

According to the [Python Documentation](https://docs.python.org/3/library/stdtypes.html#list.sort):

> A sort is stable if it guarantees **not to change the relative order of elements that compare equal** — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).

This means that if two elements have the same value or intermediate value (key), they are guaranteed to stay in the same order relative to each other. 

Let's see what I mean with this. Please take a look at this example for a few moments:

```python
>>> d = ["BB", "AA", "CC", "A", "B", "AAA", "BBB"]
>>> d.sort(key=len)
>>> d
['A', 'B', 'BB', 'AA', 'CC', 'AAA', 'BBB']
```

We are comparing the elements based on their **length** because we passed the `len` function as the argument for `key`. 

We can see that there are three elements with length 2: `"BB"`, `"AA"`, and `"CC"` in that order. 

Now, notice that these three elements are in the same relative order in the final sorted list:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-92.png)

This is because the algorithm is guaranteed to be stable and the three of them had the same intermediate value (key) during the sorting process (their length was 2, so their key was 2). 

💡 **Tip:** The same happened with `"A"` and `"B"` (length 1) and `"AAA"` and `"BBB"` (length 3), their original order relative to each other was preserved.

Now you know how the `sort()` method works, so let's dive into mutation and how it can affect your program.

## 🔹 Mutation and Risks

As promised, let's see how the process of mutation works behind the scenes:

When you define a list in Python, like this:

```python
a = [1, 2, 3, 4]
```

You create an object at a specific memory location. This location is called the "memory address" of the object, represented by a unique integer called an **id**. 

You can think of an id as a "tag" used to identify a specific place in memory:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-40.png)

You can access a list's id using the `id()` function, passing the list as argument:

```python
>>> a = [1, 2, 3, 4]
>>> id(a)
60501512
```

When you **mutate** the list, you change it directly in memory. You may ask, why is this so risky?

It's risky because it affects every single line of code that uses the list after the mutation, so you may be writing code to work with a list that is completely different from the actual list that exists in memory after the mutation.

This is why you need to be very careful with methods that cause mutation.

In particular, the `sort()` method **mutates** the list. This is an example of its effect:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-94.png)

Here is an example:

```python
# Define a list
>>> a = [7, 3, 5, 1]

# Check its id
>>> id(a)
67091624

# Sort the list using .sort()
>>> a.sort()

# Check its id (it's the same, so the list is the same object in memory)
>>> id(a)
67091624

# Now the list is sorted. It has been mutated!
>>> a
[1, 3, 5, 7]
```

The list was mutated after calling `.sort()`.

Every single line of code that works with list `a` after the mutation has occurred will use the new, sorted version of the list. If this was not what you intended, you may not realize that other parts of your program are working with the new version of the list.

Here is another example of the risks of mutation within a function:

```python
# List 
>>> a = [7, 3, 5, 1]

# Function that prints the elements of the list in ascending order.
>>> def print_sorted(x):
	x.sort()
	for elem in x:
		print(elem)

# Call the function passing 'a' as argument	
>>> print_sorted(a)
1
3
5
7

# Oops! The original list was mutated.
>>> a
[1, 3, 5, 7]
```

The list `a` that was passed as argument was mutated, even if that wasn't what you intended when you initially wrote the function. 

**💡 Tip:** If a function mutates an argument, it should be clearly stated to avoid introducing bugs into other parts of your program.

## 🔸 Summary of the sort() Method

* The `sort()` method lets you sort a list in ascending or descending order.
* It takes two keyword-only arguments: `key` and `reverse`. 
* `reverse` determines if the list is sorted in ascending or descending order.
* `key` is a function that generates an intermediate value for each element, and this value is used to do the comparisons during the sorting process. 
* The `sort()` method mutates the list, causing permanent changes. You need to be very careful and only use it if you do not need the original version of the list.

**I really hope that you liked my article and found it helpful.** Now you can work with the `sort()` method in your Python projects. [Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

