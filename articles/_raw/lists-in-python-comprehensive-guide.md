---
title: Lists in Python – A Comprehensive Guide
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-06-03T18:42:20.000Z'
originalURL: https://freecodecamp.org/news/lists-in-python-comprehensive-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/PYTHON-LISTS.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: null
seo_desc: "Let’s suppose you’re planning to visit your neighborhood store to stock\
  \ up on essentials. What is the first thing you’d do? \nHave the answer already?\
  \ Yes, you'd probably write down a shopping list! Python also has a built-in data\
  \ structure called Lis..."
---

Let’s suppose you’re planning to visit your neighborhood store to stock up on essentials. What is the first thing you’d do? 

Have the answer already? Yes, you'd probably write down a shopping list! Python also has a built-in data structure called `List` that’s very similar to your shopping list.

This post is a beginner-friendly tutorial on Python lists. Over the next few minutes, we'll get to know lists and cover some of the most common operations such as slicing through lists and modifying them using list methods. 

So let's go ahead and learn more about Python lists and see how they’re analogous to our shopping list. 

> Let’s hop in and shop together!

## How Lists Work in Python

It’s quite natural to write down items on a shopping list one below the other. For Python to recognize our list, we have to enclose all list items within square brackets `([ ])`, with the items _separated by commas_. 

Here’s an example where we create a list with 6 items that we’d like to buy.

```python
shopping_list = ['apples','pens','oatmeal  cookies','notepad','brushes','paint']

```

## Mutability of lists in Python

Just the way that we can always modify our shopping list by reordering items – do things like replacing `oatmeal cookies` with our favorite `candy`, for example – we can do the same with Python lists. 

For this reason, lists are **mutable**. Here’s how we can replace `oatmeal cookies` with `candy` in our list.

```python
shopping_list[2] = 'candy'
print(shopping_list)
# Output
>> ['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint']
```

### Indexing in Python Lists

Did you notice that `oatmeal cookies` is the third item in the list, but is at index `2`? Well, this is because of **zero-indexing**. In Python, **`index`** is essentially an _offset from the beginning of the list._

> This is why the first element is at index `0` (no offset), the second element is at index `1`, and so on. In general, if the list has n elements, the last element is at index `(n-1)`.

If we try to access an element at an invalid index, we'll get an `IndexError` . 

In our example, our shopping list has 6 elements (index ranges from 0 to 5). As shown in the code snippet below, if we try to access an element at `index = 6` , we'd get an error as there's no element at index `6`.

```python
print(shopping_list[6])
# Output
>> --------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-21-a9f3b9517136> in <module>()
----> 1 shopping_list[6]

IndexError: list index out of range
```

On the other hand, we can also use **negative indexing**.  The _last element_ is at index `-1`, the _second to last element_ is at index `-2` and so on. 

```python
print(shopping_list[-1])
# Output
>> paint
```

Just as our shopping list could contain items of any type such as fruits, vegetables, sweets and more, a Python list could also contain _items of any type_. 

That being said, it’s perfectly normal for a list to contain another little list as one of its elements. This process is called nesting and such lists are called nested lists. 

Here’s an example where our shopping list has two smaller lists.  
 `my_nested_list = [['apple','banana'],['paint','brushes']]`

## How to Loop Through Lists in Python

It’s quite common to read through our `shopping_list` to check if we’ve purchased all that we need. This is called traversing through the list. 

In Python, you can do this using loops and the `in` operator.

```python
for item in shopping_list:
  print(item)
# Output 
apples
pens
candy
notepad
brushes
paint
```

If we were to do some operations on the list instead, it's recommended to use `range` to get a set of indices that we can then loop through. 

## How to Slice Through Lists in Python

What if we were interested in looking at only a subset of our `shopping_list`? This would require us to slice through the list and retrieve a subset of items. 

Here's a general template: `list_name[start_index:end_index +1]`. Let's now try to parse this. 

* If we need a slice of the list up to `end_index`, specify `end_index + 1` when specifying the start and end indices. 
* The default `start_index` is `0`, and the default `end_index` is the index of the last element in the list. 
* If we do not specify the `start_index`, the slice starts from the first element in the list. 
* If we do not specify the `end_index`, the slice extends until the last element in the list.
* If we do not specify both of these indices, then the slice returned is the entire list.

The following code snippet illustrates this.

```python
print(shopping_list[2:])
# Output
>> ['candy', 'notepad', 'brushes', 'paint']

print(shopping_list[:2])
# Output
>> ['apples', 'pens']

print(shopping_list[:])
# Output
>> ['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint']
```

## How to Operate on Lists in Python

You can apply common built-in functions such as `len()`, `min()` , and `max()` on lists to get the length of the list, the minimum element, and the maximum element, respectively. 

As our `shopping_list` has only strings, `min()` returns the string that occurs first when the list is lexicographically sorted. `max()` returns the string that occurs last. 

You can see the code snippet for this section below.

```python
print(len(shopping_list))
>> 6

print(max(shopping_list))
>> pens

print(min(shopping_list))
>> apples
```

We can create a new list by concatenating existing lists, just as we can always piece together two small shopping lists to create a new list.

```python
list_2 = shopping_list + ['noodles','almonds']
print(list_2)

>> ['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint', 'noodles', 'almonds']
```

## Python List Methods

In addition to built-in functions that can operate on lists, Python has several list methods that help us perform useful operations on lists. 

Let's consider our `shopping_list`. What are the common operations that we would likely perform on our list? Let's list down a few:

* Add an item/multiple items to our `shopping_list`
* Remove an item/multiple items from our `shopping_list`
* Reorder items in our `shopping_list`

### How to add elements to a list in Python

We can add items, one at a time, to the end of list using the `append()` method. Let's add `grapes` to our `shopping_list`.

```python
shopping_list.append('grapes')
print(shopping_list)

>> ['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint', 'grapes']
```

What if we had an another list (or any other iterable) that we wanted to add to an existing list? Instead of adding the items from the new list one by one, we could use the `extend()` method to add the entire list to the first list as shown below.

```python
shopping_list.extend(['protein bars','cheese'])
print(shopping_list)

>> ['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint', 'grapes', 'protein bars', 'cheese']
```

**Note**: There's an inherent difference between the list methods `append()` and `extend()` and the '+' operator to concatenate two lists. 

While the '+' operator creates a new list by combining the lists that we specify as operands, the methods `append()` and `extend()` modify the list on which they are called (invoked) and do not return a new list.

### How to remove elements from a list in Python

We can remove elements from list, either a single element or a group, using the following methods. 

The `pop()` method returns the last item in the list and also deletes it, as shown below. `cheese` was the last item in the list, and it's removed now.

```python
last_element = shopping_list.pop()
print(shopping_list)
print(last_element)
# Output
>> ['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint', 'grapes', 'protein bars']
>> cheese
```

If we would like to remove an item from a particular index, we can specify the `index` as an argument to `pop()`.

```python
not_needed = shopping_list.pop(2)
print(not_needed)
# Output
>> candy
```

If we do not need access to the value of the removed list item, we can choose to use the `del` function instead. 

We can delete an item at a particular index by specifying that index, or we can delete all items in a list slice by slicing through the list as explained in the previous section.

```python
del shopping_list[1]
print(shopping_list)
# Output
>> ['apples', 'notepad', 'brushes', 'paint', 'grapes', 'protein bars']
```

Suppose we know the item that we no longer need to buy but do not know at which index the item is. In these cases, we can use the `remove()` method to remove an item by name. 

In our example, the item at index `1` in our most recent copy is `pens`. If we did not know the index of `pens`, we could write `shopping_list.remove('pens')` to do the same task as in the above code snippet. 

To remove all elements from a list, we can use `list_name.clear()`.

**Note**: If we try to remove an element that does not exist in the list, we'd get a `ValueError`.

## How to Sort a List in Python

We can choose to sort our `shopping_list` by calling the `sort()` method. As our list has only strings, `sort()` will sort our list in alphabetical order. If we have a list of numbers, the elements will be sorted in ascending order by default. 

If you'd like to sort in descending order, set the optional argument `reverse = True`.

**Note**: Calling the `sort()` method modifies the existing list and does not create a new one. If you'd like to have a new sorted list while keeping the existing list as is, use the `sorted()` method instead.

```python
shopping_list.sort()
print(shopping_list)
# Output
>> ['apples', 'brushes', 'grapes', 'notepad', 'paint', 'protein bars']
```

Another useful method is `count` which you can use to check how many times a specific item occurs in our list. `list_name.count(elt)` returns the number of times `elt` occurs in list `list_name`.

## Recap

⌛ It's now time for a quick recap. Look at the image below and check if you're able to recollect what we've read thus far. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/lists-recap.png)

📌Here's another useful look-up sheet that I've prepared for list methods which you could save for your reference.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/lmcc.png)

See you all in another post on Python soon.🙂 Until then, Happy learning and coding!

### References

[1] [Python for Everybody](https://www.freecodecamp.org/learn/scientific-computing-with-python/) on freeCodeCamp

[2] [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

