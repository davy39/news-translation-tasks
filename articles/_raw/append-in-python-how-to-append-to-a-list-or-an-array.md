---
title: Append in Python – How to Append to a List or an Array
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-07T17:41:31.000Z'
originalURL: https://freecodecamp.org/news/append-in-python-how-to-append-to-a-list-or-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/nordwood-themes-EZSm8xRjnX0-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you''ll learn about the .append() method in Python.  You''ll
  also see how .append() differs from other methods used to add elements to lists.

  Let''s get started!

  What are lists in Python? A definition for beginners

  An array in programmi...'
---

In this article, you'll learn about the `.append()` method in Python.  You'll also see how `.append()` differs from other methods used to add elements to lists.

Let's get started!

## What are lists in Python? A definition for beginners

An array in programming is an ordered collection of items, and all items need to be of the same data type.

However, unlike other programming languages, arrays aren't a built-in data structure in Python. Instead of traditional arrays, Python uses lists. 

Lists are essentially dynamic arrays and are one of the most common and powerful data structures in Python.

You can think of them as ordered containers. They store and organize similar kind of related data together.

The elements stored in a list can be of any data type.

There can be lists of integers (whole numbers), lists of floats (floating point numbers), lists of strings (text), and lists of any other built-in Python data type.

Although it is possible for lists to hold items of only the same data type, they are more flexible than traditional arrays. This means that there can be a variety of different data types inside the same list.

Lists have 0 or more items, meaning there can also be empty lists. Inside a list there can also be duplicate values.

Values are separated by a comma and enclosed in square brackets, `[]`.

### How to create lists in Python

To create a new list, first give the list a name. Then add the assignment operator(`=`) and a pair of opening and closing square brackets. Inside the brackets add the values you want the list to contain.

```python
#create a new list of names
names = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#print the list to the console
print(names)

#output
#['Jimmy', 'Timmy', 'Kenny', 'Lenny']
```

### How lists are indexed in Python

Lists maintain an order for each item.

Each item in the collection has an its own index number, which you can use to access the item itself.

Indexes in Python (and every other modern programming language) start at 0 and increase for every item in the list.

For example, the list created earlier on had 4 values:

```python
names = ["Jimmy", "Timmy", "Kenny", "Lenny"]
```

The first value in the list, "Jimmy", has an index of 0.

The second value in the list, "Timmy", has an index of 1.

The third value in the list, "Kenny", has an index of 2.

The fourth value in the list, "Lenny", has an index of 3.

To access an element in the list by its index number, first write the name of the list, then in square brackets write the integer of the element's index.

For example, if you wanted to access the element that has an index of 2, you'd do:

```python
names = ["Jimmy", "Timmy", "Kenny", "Lenny"]

print(names[2])

#output
#Kenny
```

## Lists in Python are mutable

In Python, when objects are *mutable*, it means that their values can be changed once they've been created.

Lists are mutable objects, so you can update and change them after they have been created.

Lists are also dynamic, meaning they can grow and shrink throughout the life of a program.

Items can be removed from an existing list, and new items can be added to an existing list.

There are built-in methods for both adding and removing items from lists.

For example, to **add** items, there are the `.append()`, `.insert()` and `.extend()` methods.

To  **remove** items, there are the `.remove()`, `.pop()` and `.pop(index)` methods.


### What does the `.append()` method do?

The `.append()` method adds an additional element to the **end** of an already existing list.

The general syntax looks something like this:

```python
list_name.append(item)
```

Let's break it down:

- `list_name` is the name you've given the list.
- `.append()` is the list method for adding an item to the end of `list_name`.
- `item` is the specified individual item you want to add.

When using `.append()`, the original list gets modified. No new list gets created.

If you wanted to add an extra name to the list created from earlier on, you would do the following:

```python
names = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#add the name Dylan to the end of the list
names.append("Dylan")

print(names)

#output
#['Jimmy', 'Timmy', 'Kenny', 'Lenny', 'Dylan']
```

### What's the difference between the `.append()` and `.insert()` methods?

The difference between the two methods is that `.append()` adds an item to the **end** of a list, whereas `.insert()` inserts and item **in a specified position** in the list.

As you saw in the previous section, `.append()` will add the item you pass as the argument to the function always to the end of the list.

If you don't want to just add items to the end of a list, you can specify the position you want to add them with `.insert()`.

The general syntax looks like this:

```python
list_name.insert(position,item)
```

Let's break it down:

- `list_name` is the name of the list.
- `.insert()` is the list method for inserting an item in a list.
- `position` is the first argument to the method. It's always an integer - specifically it's the index number of the position where you want the new item to be placed. 
- `item` is the second argument to the method. Here you specify the new item you want to add to the list.

For example, say you had the following list of programming languages:

```python
programming_languages = ["JavaScript", "Java", "C++"]

print(programming_languages)

#output
#['JavaScript', 'Java', 'C++']
```

If you wanted to insert "Python" at the start of the list, as a new item to the list, you would use the `.insert()` method and specify the position as `0`. (Remember that the first value in a list always has an index of 0.)

```python
programming_languages = ["JavaScript", "Java", "C++"]

programming_languages.insert(0, "Python")

print(programming_languages)

#output
#['Python', 'JavaScript', 'Java', 'C++']
```

If you instead had wanted "JavaScript" to be the first item in the list, and *then* add "Python" as the new item, you would specify the position as `1`:

```python
programming_languages = ["JavaScript", "Java", "C++"]

programming_languages.insert(1,"Python")

print(programming_languages)

#output
#['JavaScript', 'Python', 'Java', 'C++']
```

The `.insert()` method gives you a bit more flexibility compared to the `.append()` method which only adds a new item to the end of the list.

### What's the difference between the `.append()` and `.extend()` methods?

What if you want to add more than one item to a list at once, instead of adding them one at a time?

You can use the `.append()` method to add more than one item to the end of a list.

Say you have one list that contains only two programming languages:

```python
programming_languages = ["JavaScript", "Java"]

print(programming_languages)

#output
#['JavaScript', 'Java']
```

You then want to add two more languages, at the end of it.

In that case, you pass a list containing the two new values you want to add, as an argument to `.append()`:

```python
programming_languages = ["JavaScript", "Java"]

#add two new items to the end of the list
programming_languages.append(["Python","C++"])

print(programming_languages)

#output
#['JavaScript', 'Java', ['Python', 'C++']]
```

If you take a closer look at the output from above, `['JavaScript', 'Java', ['Python', 'C++']]`, you'll see that a new list got added to the end of the  already existing list.

So, `.append()` **adds a list inside of a list**.

Lists are objects, and when you use `.append()` to add another list into a list, the new items will be added as a single object (item).

Say you already had two lists, like so:

```python
names = ["Jimmy", "Timmy"]
more_names = ["Kenny", "Lenny"]
```

What if wanted to combine the contents of both lists into one, by adding the contents of `more_names` to `names`?

When the `.append()` method is used for this purpose, another list gets created inside of `names`:

```python
names = ["Jimmy", "Timmy"]
more_names = ["Kenny", "Lenny"]

#add contents of more_names to names
names.append(more_names)

print(names)

#output
#['Jimmy', 'Timmy', ['Kenny', 'Lenny']]
```

So, `.append()` adds the new elements as another list, by appending the object to the end.

To actually concatenate (add) lists together, and **combine all items from one list to another**, you need to use the `.extend()` method.

The general syntax looks like this:

```python
list_name.extend(iterable/other_list_name)
```

Let's break it down:

- `list_name` is the name of one of the lists.
- `.extend()` is the method for adding all contents of one list to another.
- `iterable` can be any iterable such as another list, for example, `another_list_name`. In that case, `another_list_name` is a list that will be concatenated with `list_name`, and its contents will be added one by one to the end of `list_name`, as separate items.

So, taking the example from earlier on, when `.append()` is replaced with `.extend()`, the output will look like this:

```python
names = ["Jimmy", "Timmy"]
more_names = ["Kenny", "Lenny"]

names.extend(more_names)

print(names)

#output
#['Jimmy', 'Timmy', 'Kenny', 'Lenny']
```

When we used `.extend()`, the `names` list got extended and its length increased by 2.

The way `.extend()` works is that it takes a list (or other iterable) as an argument, iterates over each element, and then each element in the iterable gets added to the list.

There is another difference between `.append()` and `.extend()`.

When you want to add a string, as seen earlier, `.append()` adds the whole, single item to the end of the list:

```python
names = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#add the name Dylan to the end of the list
names.append("Dylan")

print(names)

#output
#['Jimmy', 'Timmy', 'Kenny', 'Lenny', 'Dylan']
```

If you used `.extend()` instead to add a string to the end of a list ,each character in the string would be added as an individual item to the list. 

This is because strings are an iterable, and `.extend()` iterates over the iterable argument passed to it.

So, the example from above would look like this:

```python
names = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#pass a string(iterable) to .extend()
names.extend("Dylan")

print(names)

#output
#['Jimmy', 'Timmy', 'Kenny', 'Lenny', 'D', 'y', 'l', 'a', 'n']
```

## Conclusion

To sum up, the `.append()` method is used for adding an item to the end of an existing list, without creating a new list. 

When it is used for adding a list to another list, it creates a list within a list.

If you want to learn more about Python, check out freeCodeCamp's [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/). You'll start learning in an interacitve and beginner-friendly way. You'll also build five projects at the end to put into practice what you learned.

Thanks for reading and happy coding!


