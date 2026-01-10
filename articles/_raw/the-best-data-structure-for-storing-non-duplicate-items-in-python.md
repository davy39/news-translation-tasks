---
title: The Best Data Structure For Storing Non-Duplicate Items In Python
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-08-03T15:08:47.000Z'
originalURL: https://freecodecamp.org/news/the-best-data-structure-for-storing-non-duplicate-items-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/The-Best-Data-Structure-For-Storing-Non-Duplicate-Items-In-Python.png
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
seo_title: null
seo_desc: "If you're coding in Python and you need to store non-duplicate items while\
  \ ensuring each item is unique, which data structure should you use? \nI'd recommend\
  \ the set data structure. It's an unordered collection of unique elements, meaning\
  \ it cannot co..."
---

If you're coding in Python and you need to store non-duplicate items while ensuring each item is unique, which data structure should you use? 

I'd recommend the `set` data structure. It's an unordered collection of unique elements, meaning it cannot contain any duplicate items. 

When you add elements to a set, Python automatically removes any duplicates. This makes it a perfect choice for scenarios where you need to store a collection of items while ensuring uniqueness.

## How to Use a `set` in Python

You can create a set in Python using curly braces `{}` or the built-in `set()` function. 

Suppose, you already know that you would have duplicate items but you do not want to keep the duplicate items at all. Then you can start directly entering the items in a set. Here's an example:

```python
# Creating a set
my_set = {1, 2, 3, 4, 3, 5}  # Duplicate '3' is automatically removed

print(my_set)  # Output: {1, 2, 3, 4, 5}

```

Here I have created a set in the `my_set` variable, and I have 2 duplicate items there. As you can see in the output, the duplicates have been removed.

If you have a list with potential duplicates and want to remove them to create a set, you can simply convert the list to a set using the `set()` function. 

Suppose, you already have a list containing a lot of data – let's say it contains the data of your shop's customers. Now at the end of the month, you want to know exactly how many individual customers arrived at your shop's doorstep. 

During the month, you stored the customer's unique IDs in a list and recorded it each time they visted your shop. As some customers came more than once in that month, it is highly possible that the list where you stored the customer IDs has duplicate data (which is redundant when you're trying to calculate all unique customers).

So you want a solution where you only extract the unique customer ID from that particular list – but for safety, you do not want to modify or change the original list data. 

In that case, you can simply create a new variable to extract the unique data from that list and store it there. You can use the set functionality here as well. For example:

```python
# Removing duplicates from a list and creating a set
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)

print(my_set)  # Output: {1, 2, 3, 4, 5}
```

Here, I have my list in the `my_list` variable which currently has duplicate items in it – `2` (appears twice) and `4` (also appears twice). 

But, in the second line, I have initialized a new variable named `my_set` where I store the set of `my_list`. As the set automatically removes any duplicates and keeps only a single item from the duplicates, I am storing all the unique items in my `my_set` variable.

But if I print `my_list`, I will still get the duplicate values altogether. This is because we have not changed the original list at all. We simply created a new variable named `my_set` and stored only the unique values from that list.

But if you really want to remove the duplicates from the original list and create another list, then you can remove the duplicates from the list by first changing it to a set and then back to a list again. In that way, you can get a new list with the duplicates removed.

For example:

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = list(set(my_list)) # Removing duplicates by first changing to a set and then back to a list
print(new_list) # Output: [1, 2, 3, 4, 5]
```

But if you really want to modify the original list, then you can create a set and remove the duplicates, and then you can again change that to a list and store the list data to the original list again!

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(set(my_list)) # Altering the list to remove duplicates from the earlier list data and storing the new data without duplicates in that list 
print(my_list) # Output: [1, 2, 3, 4, 5]
```

Sets provide fast membership testing and efficient operations for set theory operations (like union, intersection, and difference), which makes them a great choice for handling collections of unique elements in Python.

## **📺 Video Walkthrough**

I know that many of you like to watch a video instead of following a complete article. Fear not! I have also created a complete video tutorial for you:

%[https://www.youtube.com/watch?v=3IKzhY5jlKk]

## Conclusion

I hope you have enjoyed this short article. 

If you have any questions then please let me know by reaching out on [Twitter](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can also follow me on:  
🎁GitHub: [FahimFBA](https://github.com/FahimFBA)  
🎁YouTube: [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

If you are interested then you can also check my website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

