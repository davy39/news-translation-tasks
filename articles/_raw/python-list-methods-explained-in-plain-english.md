---
title: Python List Methods Explained in Plain English
subtitle: ''
author: Gold Agbonifo Isaac
co_authors: []
series: null
date: '2023-09-24T14:08:41.000Z'
originalURL: https://freecodecamp.org/news/python-list-methods-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/A.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: We often make plans about the things we want, what we need to do, and places
  we want to visit. These lists could go on forever! However, there are times when
  we need to build a program that requires us to organize and manipulate information
  using lis...
---

We often make plans about the things we want, what we need to do, and places we want to visit. These lists could go on forever! However, there are times when we need to build a program that requires us to organize and manipulate information using lists. 

In this article, we will explore how to create and work with lists in Python, providing simple explanations for beginners.

## Understanding Python Lists

‌‌In Python, a list is a fundamental data structure used to store specific information or objects. If you're not familiar with the concept of a data structure, think of it as a way to organize and store data so that you can easily access and manipulate it. Data structures exist to help you structure your data efficiently.

Let's delve into what you can do with a Python list and how you can achieve it.

## List Methods in Python

Python offers a wide range of functionalities for lists, and I'll introduce you to some of them.

### The `.append()` Method

This method allows you to add an item to the end of a list.

 Here's how it works:

```python

# Imagine your list contains items you need to buy 
things_i_need = ["shoes", "bags", "groceries"]

# Suddenly, you remember something else to add
things_i_need.append("toiletries") 

# Now, let's print out the updated list 
print(things_i_need)                

‌You can use the `.append()` method to add elements of any data type to a list, whether they are numbers, strings, or even contents from another list.

### The `.extend()` Method

This method does one thing and does it really well. It allows you to extend your lists by adding more items to the list.

Now, don't get it all wrong by asking yourself:  "Does this mean the `.append()` method is the same as the `.extend()` method?" Well, the answer to that is NO. 

The `.extend()` method allows you to add more items to the end of a list, while the `.append()` method is used for adding just a single item. If you need to add a lot of items to your list, then the `.extend()` method is your go-to.

The `.extend()` method takes another list (this could be called an iterable) as its argument (an argument is a piece of information you attach to a function or program to allow it to do its task efficiently), and then adds each item to the original list.

Here's a code example to further illustrate our explanation:

```python
#we'll use the same Things_I_need list 
Things_I_need =["shoes","bags","groceries"] 

#You suddenly remember that you need more stuffs 

Additional_stuffs_I_need = ["clothes","skincare","makeup"] 

#Now, you can add this new list to your previous list. Things_I_need.extend(Additional_stuffs_I_need) 


#Your list is now["shoes","bags","groceries","clothes","skincare","makeup"]

So, if you ever need to extend your list with more items, remember to use the `.extend()` method!

### The `.insert()` Method

Unlike the methods we've discussed so far, the `.insert()` method offers a unique feature. It not only lets you add items but also allows you to specify their positions! Pretty amazing, isn't it? 

Well, the `insert()` method is quite intriguing because it gives you control over the positions where your items will be inserted, and this is achieved through the use of indexes. (Remember, in computer indexing, counting typically starts from 0!)

Here's an example to demonstrate how it works:

```python
 # Using the 'things_I_need' list again
 
 things_I_need = ["shoes", "bags", "groceries"] 
 
 # Let's say you want to add something more important than shoes, bags, or groceries.
 
# You can insert such an item as the first one on the list
things_I_need.insert(0, "my_meds")

# Here, '0' represents the position you've chosen for the new item. 
# Now, let's print our final outcome 
print(things_I_need) 

# The new list would be: ['my_meds', 'shoes', 'bags', 'groceries']

The `.insert()` method is quite handy, so don't forget to use it when you need to manipulate positions!

### The `.remove()` Method

Have you ever realized that you accidentally added an item twice to your list? Well, besides the obvious solution of using your backspace, you can actually remove the first occurrence of an item from your list!

Here's an example to show you how it works:‌‌

```python
# Using the 'things_I_need' list again.
# Assume your love for shoes caused you to write it twice. 
things_I_need = ["shoes", "bags", "groceries", "shoes"] 

# You noticed the duplication and decided to remove one of the shoes. things_I_need.remove("shoes") 

# Now, print your updated list with the first occurrence of "shoes" removed. print(things_I_need) 

# The new list is ["bags", "groceries", "shoes"].

‌However, please be cautious with the `.remove()` method. Make sure never to attempt to remove an item that is not on the list, or else you'll encounter a value error. This occurs because you're trying to access an item that is out of range or bounds.

### The `.pop()` Method

‌‌‌‌Similar to the `.remove()` method, you can use the `.pop()` method to remove items from a list. 

However, there's a twist to it—the `.pop()` method provides more flexibility than the `.remove()` method. You can remove an item at a specific position in a list by specifying that position. 

What's even more interesting is that if you forget to specify what you want to remove, it will automatically help you remove the last item from your list.

Here's an example of how you can use `.pop()` to remove an item by index:

```python
# Using the 'things_I_need' list again.
things_I_need = ["shoes", "bags", "groceries"]

#Assume you wanted to be cost effective by removing shoes 
popped_list = things_I_need.pop(0) 

#now print your new cost-effective list
print(popped_list)

#The new list is ["bags","shoes"]



### The `.clear()` Method

So you made a list and decided it was redundant. You suddenly realize everything you put in your list was not important. You can use the `.clear()` method to clear your list.

Here's how to do that:

```python
#using the things_I_need list
things_I_need = ["shoes","bags","groceries"]

things_I_need = things_I_need.clear(things_I_need)
print(things_I_need)

#new list is empty []


### The `.index()` Method

The `.index()` method is a tool in Python that helps you find where the first occurrence of a specific item is in a list. It tells you the position of that item in the list, like its spot in a line of items. 

Here's an example :

```python
# Using a list of things you need
things_I_need = ["shoes", "bags", "groceries", "shoes", "bags"]

# Find the index of the first occurrence of "shoes"
shoes_index = things_I_need.index("shoes")

# Find the index of the first occurrence of "bags"
bags_index = things_I_need.index("bags")

print("Index of 'shoes':", shoes_index)
print("Index of 'bags':", bags_index)

#output: Index of 'shoes': 0
#output: Index of 'bags': 1


### The `.count()` Method

The `.count()` method in Python is handy for counting occurrences. 

Let me explain: it helps you find out how many times a specific item appears in your list. This can be really useful, especially when dealing with larger lists.

Here's an example to understand how it works:

```python

# Using a list of things you need
things_I_need = ["shoes", "bags", "groceries", "shoes", "bags"]

# Count the occurrences of "shoes"
shoes_count = things_I_need.count("shoes")

# Count the occurrences of "bags"
bags_count = things_I_need.count("bags")

print("Number of shoes:", shoes_count)
print("Number of bags:", bags_count)


### The `.reverse()` Method

`.reverse()` basically gives you an alternate version of your list by giving you a backwards list. 

For example, if you had a list of numbers 1,2,3,4,5 the reverse would be 5,4,3,2,1.

Here's how you can use the `.reverse()` method in Python :

```python
# Using a list of things you need
things_I_need = ["shoes", "bags", "groceries"]

# Reverse the order of items in the list in-place
things_I_need.reverse()

# Print the reversed list
print(things_I_need)

#output is ['groceries', 'bags', 'shoes']



### The `.copy()` Method

What does it mean to make a copy of something? To create a duplicate of the orignal, right? To have another version of something right? Well, that exactly what the `.copy()` method does!  


And here's how it does it:

```python
# Using a list of things you need
things_I_need = ["shoes", "bags", "groceries"]

# Create a copy of the list using the .copy() method
copied_list = things_I_need.copy()

# Print the copied list
print(copied_list)


## Conclusion

You have now come to the end of the tutorial. By now, I hope you have grasped the basics of how to use methods in Python lists. I enjoyed writing this, and I hope you had fun too!

