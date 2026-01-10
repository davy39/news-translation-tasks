---
title: List Comprehension in Python Explained for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T17:25:39.000Z'
originalURL: https://freecodecamp.org/news/list-comprehension-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/list-comprehension-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Buggy Programmer

  List comprehension is an easy to read, compact, and elegant way of creating a list
  from any existing iterable object. Basically, it''s a simpler way to create a new
  list from the values in a list you already have.

  It is generally a...'
---

By Buggy Programmer

List comprehension is an easy to read, compact, and elegant way of creating a list from any existing iterable object. Basically, it's a simpler way to create a new list from the values in a list you already have.

It is generally a single line of code enclosed in square brackets. You can use it to filter, format, modify, or do other small tasks on existing iterables such as strings, tuples, sets, dataframes, array lists, and so on.

In this short lesson, we will see some different ways of creating list comprehension and see some of its variants like:

* Simple list comprehension
* List comprehension with single and nested if conditions
* List comprehension with single and multiple if and else conditions
* List comprehension with nested for loops

Apart from this, we will also take a look at the following concepts:

* For loops vs list comprehension
* What are the benefits of list comprehension?
* When to use and when to avoid list comprehension. 

## What is List Comprehension in Python?

So, let’s start with the syntax of list comprehension. List comprehension is a single line of code that you write inside the square brackets. It has three components:

1. For loop
2. Condition and expression 
3. Output  


![Syntax of list comprehension, how list comprehension works](https://www.freecodecamp.org/news/content/images/2021/07/list-comprehension.png)
_**Syntax of list comprehension** -Credit [buggyprogrammer](http://buggyprogrammer.com/)_

### Example of Simple List Comprehension

The below code snippet is an example of the simplest list comprehension. Here we are just looping through the `lst` and storing all its element in the list `a`:

```python
lst = [1,2,3,4,5,6,7,8,9,10]
# simple list comprehension
a = [x for x in lst]
print(a)
 
# ouput
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

The above code is equivalent to this:

```python
for x in lst:
    a.append(x)
```

In order to achieve this, we don’t even need the append method in a list comprehension. 

Now in the above code (list comprehension), you can use any expression to modify the elements of `lst`, for example:

```python
# add any number to every elements of lst and store it in a
a = [x+1 for x in lst]
 
# subtract any number to every elements of lst and store it in a
a = [x-1 for x in lst]
 
# multiply any number to every elements of lst and store it in a
a = [x*2 for x in lst]
```

## List Comprehension with Single and Nested If Condition

In list comprehension, we can also add an `if` condition, which can help us filter data. For example, in the below code we are storing all values of `lst` in list `c` whose values are greater than 4:

```python
lst = [1,2,3,4,5,6,7,8,9,10]
# with if condition
c = [x for x in lst if x > 4]
print(c)
 
# output
[5, 6, 7, 8, 9, 10]
```

The above code is equivalent to this:

```python
for x in lst:
    if x > 4:
        a.append(x)

```

We can also add a `nested if` condition to our list comprehension. For example, in the below code we are storing all elements of `lst` in list `d` whose values are greater than 4 and divisible by 2:

```python
# with multiple if 
d = [x for x in lst if x > 4 if x%2 == 0]
 
# output
[6, 8, 10]

```

Above code is equivalent to this:

```python
for x in lst:
    if x > 4:
        if x % 2 == 0:
            a.append(x)
```

## List Comprehension with Single and Multiple If and Else Conditions

Okay so now we will take a look at how we can add `else` with `if` in list comprehension. 

Here we have created a simple list comprehension which will store all values of `lst` in list `e` whose values are greater than 4 – else if the values are less than 4 then it will store the string `“less than 4”` in its place.

```python
lst = [1,2,3,4,5,6,7,8,9,10]
# with if and else condition
e = [x if x > 4 else 'less than 4' for x in lst]
print(e)
 
# output
['less than 4', 'less than 4', 'less than 4', 'less than 4', 5, 6, 7, 8, 9, 10]
```

The above code is equivalent to this:

```python
for x in lst:
    if x > 4:
        d.append(x)
    else: 
        d.append('less than 4')
```

Now let’s see list comprehension with multiple `if and else`.

In the below example, we are storing the string `“Two”` if the value is divisible by 2. Or if the value is divisible by 3 we are storing `“Three”`, else we are storing `“not 2 & 3”`.

```python
# with more than one if and else condition
f = ['Two' if x%2 == 0 else "Three" if x%3 == 0 else 'not 2 & 3' for x in lst]
print(f)
 
# output
['not 2 & 3', 'Two', 'Three', 'Two', 'not 2 & 3', 'Two', 'not 2 & 3', 'Two', 'Three', 'Two']
```

So how does this work? To understand this, we can divide the whole condition into three parts, after every else:

```python
'Two' if x%2 == 0 else "Three" if x%3 == 0 else 'not 2 & 3'
```

Here, if the first `if` condition is true then it will take the value `“Two”` – otherwise it will move to the second `if` condition, instead of storing any other value, just like the `elif` command. 

Now in the second `if` condition, it will save `“Three”` if the statement is true. Otherwise, it will check for the next condition, which we don't have. So whatever value follows after `else` will be stored, which in our case is a string `“not 2 & 3”`.

So in the traditional way the above, we can write the whole code like this:

```python
for x in lst:
    if x%2 == 0:
        f.append('Two')
    elif x%3 == 0:
        f.append('Three')
    else: 
        f.append('not 2 & 3')
```

Do you see the power of list comprehension? It is doing the task in just one line which a traditional for loop does in 7.

**You can also read this article ➡** [Solve Python fizzbuzz challenge with list comprehension](https://buggyprogrammer.com/python-fizzbuzz/) to learn more.

## List Comprehension with a Nested For Loop

Alright! Now we will see how list comprehension works with a `nested for loop`. 

To understand what's going on here, let’s look at the below example. Here we are generating all possible combinations of [1,2,3] and [3,2,1].

```python
lst = [1,2,3]
lst_rev = [3,2,1]
g = [(x,y) for x in lst for y in lst_rev]
print(g)
 
#output
[(1, 3), (1, 2), (1, 1), (2, 3), (2, 2), (2, 1), (3, 3), (3, 2), (3, 1)]

```

The above code can also be written as:

```python
for x in lst:
    for y in lst_rev:
        f.append((x,y))
```

Okay so now as promised, let’s see the comparison between for loops and list comprehension.

## For Loops vs List Comprehension

Above we saw how list comprehension was able to complete a task in just a single line which a for loop completed in multiple lines. 

List comprehension is not only compact, but it is also easier to read and faster than for loops in terms of performance. 

In some cases, list comprehension appears to be two times faster than a for loop. If you want to know more about list comprehension's performance you can about it [here](https://switowski.com/blog/for-loop-vs-list-comprehension).

But if you want to execute more than one simple condition, list comprehension will not be able to handle it without sacrificing readability. This is the one major issue with list comprehension.

## Benefits of List Comprehension 

Apart from being simple, compact, and faster, list comprehension is also reliable in many different situations. And you can use it in a variety of circumstances. 

You can use list comprehension to map and filter in addition to basic list generation. You don't need to adopt a new strategy for each situation. That’s one of the reasons it is considered more pythonic than a for loop.

## When to Use List Comprehension (and When to Avoid it)

You can use list comprehension if you are doing simple filtering, modifications, or a formatting task on other iterative objects. It's also be a good choice if you want to keep your code compact and readable. 

Also, you can use it when even a tiny bit of performance matters to you. 

But you should avoid using list comprehension if you have too many conditions to add for filtering or modifying as it will make your code more complex and harder to read.

## Conclusion

In this article we learned what list comprehension is, what its benefits are, and when we should use it. And we saw how list comprehension is simple, easy to read, compact, and faster than a for loop. 

We also learned how to write list comprehension with or without a condition, with nested if and else, and with a nested for loop. 

If you liked this article, then you will definitely like my other blogs too. You can visit my personal site [here](http://buggyprogrammer.com/).

  


  

