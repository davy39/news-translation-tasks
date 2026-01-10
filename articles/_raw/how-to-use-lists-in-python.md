---
title: How to Use Lists in Python – Explained with Example Code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-03-01T20:02:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-lists-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-2-.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, lists are a cornerstones of data organization and manipulation\
  \ – so I think they deserve a thorough exploration. \nThis article delves into how\
  \ to create and manipulate lists in Python, some advanced functionalities, and some\
  \ practical appl..."
---

In Python, lists are a cornerstones of data organization and manipulation – so I think they deserve a thorough exploration. 

This article delves into how to create and manipulate lists in Python, some advanced functionalities, and some practical applications of lists.

You can get all the source code from [here](https://github.com/dotslashbit/fcc-article-resources/blob/main/python/python-list/main.py).

## Table of Contents

* [What is a List in Python](#heading-what-is-a-list-in-python)?
* [How to Create a List in Python](#heading-how-to-create-a-list-in-python)
* [How to Access Elements in a List in Python](#heading-how-to-access-elements-in-a-list-in-python)
* [List Operations and Methods](#heading-list-operations-and-methods)
* [Advanced List Concepts](#heading-advanced-list-concepts)
* [Conclusion](#heading-conclusion)

## What is a List in Python?

Imagine you're preparing for a grand adventure, packing your trusty backpack. In your pack, you have different compartments where you can store your items – some compartments for clothes, others for snacks, and maybe even a hidden pouch for your most precious treasures.

Now, think of Python lists as your digital backpack. A Python list is like a versatile container, but instead of compartments, it holds various pieces of information called "elements." These elements can be anything you want: numbers, words, even other lists! Just like your backpack, you can rearrange, add, remove, or update these elements as needed.

For example, let's say you're planning a trip to the grocery store. You can create a Python list called `grocery_list` to keep track of all the items you need to buy. Each item, such as "apples," "bananas," or "milk," is like an element in your list.

Here's what a simple grocery list might look like in Python:

```python
grocery_list = ["apples", "bananas", "milk"]
```

A Python list is a dynamic, mutable, ordered collection of elements enclosed within square brackets `[]`. 

These elements, called items or values, can be of different data types – numbers, strings, booleans, and even other lists (creating nested structures).

With this list, you can easily check what you need to buy, add new items as you remember them, or remove items as you get them or if you change your mind.

The beauty of Python lists lies in their flexibility and convenience. Whether you're organizing data, managing tasks, or solving complex problems, lists provide a powerful way to store and manipulate information in your Python programs. Just like your trusty backpack helps you stay organized on your adventures, Python lists help keep your code neat and efficient.

## How to Create a List in Python

Creating lists in Python is as versatile as organizing your belongings in different compartments of your backpack. Depending on what you're packing, you might choose to arrange your items differently for better organization and accessibility.

### Single line list

Think of this like tossing your favorite snacks into your backpack for a quick trip. When you're in a hurry and need to grab your essentials fast, a single line list is the way to go. It's concise and efficient, perfect for when you have a short list of items to remember.

```python
fruits = ["apple", "banana", "cherry"]

```

### Multi-line list for readability

Imagine you're packing for a long journey and want to ensure everything fits neatly into your backpack. Just like neatly folding your clothes to maximize space, a multi-line list ensures clarity and organization, especially for longer lists.

```python
numbers = [
    1,
    2,
    3,
    4,
    5,
]

```

### Mixed data type list

Sometimes, your adventures require packing a variety of items – snacks, gadgets, and maybe even a good book. Similarly, a mixed data type list accommodates different types of data, allowing you to store a diverse range of information in a single list.

```python
mixed_list = ["hello", 3.14, True]

```

By understanding when to use each type of list, you can efficiently organize your data, making your Python programs easier to read and maintain. Just like packing your backpack for different journeys, choosing the right type of list ensures you're well-prepared for any coding adventure.

## How to Access Elements in a List in Python

Imagine you have a row of jars, each containing a different type of candy. You want to grab a specific candy from one of the jars. How do you do it? You look at the labels on the jars to find the one you want, right? 

In Python lists, each item is like a piece of candy in a jar, and the label on the jar is similar to what we call an "index."

### How Indices Work

An index is like the label on each jar. It tells us the position of an item in the list. But here's the trick: in Python, we start counting from 0, not 1. So items in a Python list are labeled starting from 0, then onwards with 1, 2, and so on.

### How to Access Elements in a List

To get the candy from a specific jar, you look at the label and pick the right one. Similarly, to get an item from a list, you use its index. Here's how you do it in Python:

```python
# Let's say we have a list of fruits
fruits = ["apple", "banana", "cherry"]

# To access the first fruit (apple), which is at index 0
first_fruit = fruits[0]
print(first_fruit)  # Output: apple

# To access the second fruit (banana), which is at index 1
second_fruit = fruits[1]
print(second_fruit)  # Output: banana

```

By using the index inside square brackets after the list name, Python helps us retrieve the item stored at that position.

Knowing how to access elements in a list is super handy! It's like having a magical map that guides you directly to the candy you want. 

You can use this skill whenever you need to work with specific pieces of data in your program. Whether you're counting candies, managing scores in a game, or organizing a list of friends' names, understanding how to access elements by their indices is the key to unlocking the full potential of Python lists.

## List Operations and Methods

### How to Modify a List

Unlike strings, lists are mutable. This means you can change their content after you create them. 

Imagine your list is like a recipe book, where you can add, remove, or rearrange ingredients as you please. Here are key methods for modifying lists:

#### Append an element

Adds an element to the end of the list, like adding a new ingredient to the end of your recipe.

Here's the syntax: `list_name.append(element)`

And here's a code example:

```python
fruits.append("orange")
# Explanation: We're adding "orange" to the end of the list 'fruits'.
# Result: fruits will now be ["apple", "banana", "cherry", "orange"]

```

#### Insert an element

Inserts an element at a specific index, shifting existing elements if necessary, similar to adding a new ingredient at a specific step in your recipe.

Here's the syntax: `list_name.insert(index, element)`

And here's a code example:

```python
fruits.insert(1, "grape")
# Explanation: We're adding "grape" at index 1 in the list 'fruits', shifting other elements if needed.
# Result: fruits will now be ["apple", "grape", "banana", "cherry", "orange"]

```

#### Remove an element

Removes the first occurrence of a specific element, just like removing an ingredient you no longer need from your recipe.

Here's the syntax: `list_name.remove(element)`

And here's a code example:

```python
fruits.remove("banana")
# Explanation: We're removing the first occurrence of "banana" from the list 'fruits'.
# Result: fruits will now be ["apple", "grape", "cherry", "orange"]

```

#### Pop an element

Removes and returns the element at the given index, similar to taking out an ingredient from a specific step in your recipe.

Here's the syntax: `list_name.pop(index)`

And here's a code example:

```python
removed_item = fruits.pop(1)
# Explanation: We're removing the item at index 1 ("grape") from the list 'fruits' and storing it in 'removed_item'.
# Result: removed_item will be "grape", fruits will now be ["apple", "cherry", "orange"]

```

#### Extend a list

Extends the list by appending all elements from an iterable, like adding more ingredients to your recipe from another recipe.

Here's the syntax: `list_name.extend(iterable)`

And here's a code example:

```python
more_fruits = ["mango", "pineapple"]
fruits.extend(more_fruits)
# Explanation: We're adding all the fruits from 'more_fruits' to the end of the list 'fruits'.
# Result: fruits will now be ["apple", "cherry", "orange", "mango", "pineapple"]

```

### How to Slice a List

Slicing a list is like cutting a cake into perfectly-sized slices. Just as you choose where to start cutting, where to end, and how thick each slice should be, slicing a list lets you extract specific portions of data from your list.

Imagine you have a delicious cake, fresh out of the oven. You're tasked with cutting it into slices for your guests. Here's how slicing a list relates to cutting a cake:

#### Start and End Points

* **Start Index:** This is where you begin cutting the cake. If you start at the first layer of the cake, you might begin at the very edge. When choosing a starting index, you can pick any one you like - it doesn't have to be the first one.
* **End Index:** This is where you stop cutting the cake. If you stop at the third layer, you won't cut beyond that point.

#### Slice Thickness (Step)

* Just like you can cut thicker or thinner slices of cake, in slicing a list, you can decide how many elements to include in each slice.

Here's the syntax for slicing:

```python
list_name[start_index:end_index:step]

```

And here's a code example to show you how it works:

```python
# Let's say we have a list of cake layers
cake_layers = ["chocolate", "vanilla", "strawberry", "lemon", "red velvet"]

# Slicing the cake layers
slice_of_cake = cake_layers[1:4:2]
# Explanation: We're slicing 'cake_layers' starting from index 1 (vanilla) up to index 4 (lemon), 
#             and selecting every second element.
# Result: slice_of_cake will be ["vanilla", "lemon"]

```

* **Start Index 1 (vanilla):** This is where we begin cutting the cake.
* **End Index 4 (lemon):** We stop cutting at this layer, but we don't include lemon.
* **Step of 2:** We skip every other layer between vanilla and lemon.
* **Result:** We end up with a slice containing only vanilla and lemon layers.

By slicing lists, you can extract specific sections of data tailored to your needs, just like cutting cake slices to suit your guests' preferences.

#### Common List Methods

##### Length

Returns the length (number of elements) of the list, similar to counting the number of ingredients in your recipe.

Here's the syntax: `len(list_name)`

And here's a code example:

```python
length = len(fruits)
# Explanation: We're finding the number of elements in the list 'fruits'.
# Result: length will be 5

```

##### Sort

Sorts the list in-place, like arranging your ingredients in alphabetical order in your recipe.

Here's the syntax: `list_name.sort()`

And here's a code example:

```python
fruits.sort()
# Explanation: We're sorting the elements of 'fruits' in ascending order.
# Result: fruits will now be ["apple", "cherry", "mango", "orange", "pineapple"]

```

##### Sorted

Returns a new sorted list without modifying the original list, similar to making a copy of your recipe with ingredients arranged differently.

Here's the syntax: `sorted(list_name)`

And here's a code example:

```python
sorted_numbers = sorted(numbers)
# Explanation: We're creating a new list 'sorted_numbers' with the elements of 'numbers' sorted.
# Result: sorted_numbers will be [1, 2, 3, 4, 5], 'numbers' remains unchanged

```

Custom sorting in Python lists allows you to sort elements based on criteria other than their natural order. This is achieved using the optional `key` parameter, which specifies a function to be called on each element before sorting. Here's an explanation:

#### Custom Sorting and the Key Function

Imagine you have a collection of recipe cards, each with a list of ingredients. Now, instead of sorting these recipe cards alphabetically by their titles, you want to sort them based on the number of ingredients each recipe requires. This is where custom sorting with the key function comes into play.

Here's the syntax to do this:

```python
list_name.sort(key=function)
sorted_list = sorted(list_name, key=function)

```

Now let's look at an example:

Suppose we have a list of recipe cards, where each card is a tuple containing the recipe name and the number of ingredients required:

```python
recipes = [("Apple Pie", 9), ("Chocolate Cake", 7), ("Salad", 4), ("Pancakes", 6)]

```

If we want to sort these recipe cards based on the number of ingredients required, we can use a custom sorting function:

```python
# Define a function to extract the number of ingredients from each recipe tuple
def get_num_ingredients(recipe):
    return recipe[1]

# Sort the recipes based on the number of ingredients
recipes.sort(key=get_num_ingredients)

# Result: recipes will be [("Salad", 4), ("Pancakes", 6), ("Chocolate Cake", 7), ("Apple Pie", 9)]

```

* We define a function `get_num_ingredients` that takes a recipe tuple as input and returns the second element of the tuple (the number of ingredients).
* We then use this function as the `key` parameter in the `sort` method. Python will call this function on each recipe tuple and use the returned values for sorting.
* As a result, the recipes are sorted based on the number of ingredients required, from the smallest to the largest.

Custom sorting with the key function allows you to sort lists based on complex criteria, such as attributes of objects or calculated values, giving you greater flexibility in organizing your data.

##### Reverse

Reverses the order of elements in-place, like flipping your recipe upside down.

Here's the syntax: `list_name.reverse()`

And here's an example:

```python
fruits.reverse()
# Explanation: We're reversing the order of elements in the list 'fruits'.
# Result: fruits will now be ["pineapple", "orange", "mango", "cherry", "apple"]

```

##### Index

Returns the first index of a given element, similar to finding the page number where an ingredient is listed in your recipe book.

Here's the syntax: `list_name.index(element)`

And here's an example:

```python
index_of_cherry = fruits.index("cherry")
# Explanation: We're finding the index of the first occurrence of "cherry" in the list 'fruits'.
# Result: index_of_cherry will be 3

```

##### Check Element Existence

Checks if an element exists in the list, like verifying if an ingredient is listed in your recipe.

Here's the syntax: `element in list_name`

And here's an example:

```python
is_apple_present = "apple" in fruits
# Explanation: We're checking if "apple" exists in the list 'fruits'.
# Result: is_apple_present will be True

```

##### Count Occurrences

Returns the number of times a specific element appears in the list, similar to counting how many times an ingredient is used in your recipe.

Here's the syntax: `list_name.count(element)`

And here's an example:

```python
count_of_orange = fruits.count("orange")
# Explanation: We're counting the number of times "orange" appears in the list 'fruits'.
# Result: count_of_orange will be 1

```

## Advanced List Concepts

### List Comprehension

When it comes to working with lists in Python, there's a powerful tool at your disposal called list comprehension. This concise syntax allows you to generate lists based on existing iterables with ease, making your code more readable and efficient.

List comprehension offers a concise way to create lists by applying an expression to each item in an existing iterable, optionally with filtering conditions.

#### Example 1: Generating Squares of Numbers

In a traditional approach, you might initialize an empty list, loop through a range of numbers, calculate the square of each number, and append it to the list. With list comprehension, you achieve the same result in a single line, iterating over the range of numbers and directly creating the list of squares.

```python
# Traditional Approach:
squares = []
for x in range(5):
    squares.append(x**2)

# Explanation:
# In the traditional approach, we initialize an empty list 'squares'. 
# We then loop through numbers from 0 to 4 using the range() function.
# For each number 'x', we calculate its square (x**2) and append it to the 'squares' list.

# List Comprehension:
squares = [x**2 for x in range(5)]

# Explanation:
# With list comprehension, we achieve the same result in a single line.
# We use a compact syntax to iterate over numbers from 0 to 4 and calculate their squares directly, 
# creating the list 'squares' in one go.

```

#### Example 2: Generating Even Numbers

Similarly, when generating a list of even numbers, you can use a compact syntax with list comprehension to iterate over a range of numbers and include only those that are divisible by 2, eliminating the need for extra conditional statements.

```python
# Traditional Approach:
even_numbers = []
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)

# Explanation:
# In the traditional approach, we initialize an empty list 'even_numbers'. 
# We then loop through numbers from 0 to 9 using the range() function.
# For each number 'x', we check if it's even (divisible by 2), and if so, we append it to the 'even_numbers' list.

# List Comprehension:
even_numbers = [x for x in range(10) if x % 2 == 0]

# Explanation:
# With list comprehension, we achieve the same result more concisely.
# We use a compact syntax to iterate over numbers from 0 to 9 and include only those that are even,
# directly creating the list 'even_numbers' in one line.

```

#### Example 3: Generating a List of Strings

List comprehension isn't limited to numerical operations. You can also apply it to manipulate strings. For instance, converting a list of names to uppercase can be achieved in a single line, making your code more concise and readable.

```python
# Traditional Approach:
names = ['Alice', 'Bob', 'Charlie']
uppercase_names = []
for name in names:
    uppercase_names.append(name.upper())

# Explanation:
# In the traditional approach, we initialize an empty list 'uppercase_names'. 
# We then loop through each name in the 'names' list.
# For each name, we convert it to uppercase using the upper() method and append the result to 'uppercase_names'.

# List Comprehension:
uppercase_names = [name.upper() for name in names]

# Explanation:
# With list comprehension, we achieve the same result more succinctly.
# We use a compact syntax to iterate over each name in the 'names' list,
# applying the upper() method to convert each name to uppercase,
# directly creating the list 'uppercase_names' in one line.

```

#### Example 4: Generating a List of Tuples

Nested loops are commonly used to generate combinations of items, such as pairs of numbers. With list comprehension, you can streamline this process by using nested loops directly within the comprehension syntax, creating tuples of combinations effortlessly.

```python
# Traditional Approach:
pairs = []
for x in range(3):
    for y in range(2):
        pairs.append((x, y))

# Explanation:
# In the traditional approach, we initialize an empty list 'pairs'. 
# We then use nested loops to iterate over each possible combination of x and y values.
# For each combination, we create a tuple (x, y) and append it to the 'pairs' list.

# List Comprehension:
pairs = [(x, y) for x in range(3) for y in range(2)]

# Explanation:
# With list comprehension, we achieve the same result more compactly.
# We use a compact syntax with nested loops to iterate over each possible combination of x and y values,
# directly creating the list 'pairs' containing tuples in one line.

```

#### Example 5: Generating a List of Combinations

List comprehension also allows you to include conditional expressions, enabling you to filter out certain combinations based on specific criteria. This flexibility makes it a versatile tool for various list generation tasks.

```python
# Traditional Approach:
combinations = []
for x in range(1, 4):
    for y in range(1, 4):
        if x != y:
            combinations.append((x, y))

# Explanation:
# In the traditional approach, we initialize an empty list 'combinations'. 
# We then use nested loops to iterate over each possible combination of x and y values.
# For each combination where x is not equal to y, we create a tuple (x, y) and append it to the 'combinations' list.

# List Comprehension:
combinations = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]

# Explanation:
# With list comprehension, we achieve the same result more succinctly.
# We use a compact syntax with nested loops and a conditional expression to iterate over each possible combination of x and y values,
# including only those where x is not equal to y,
# directly creating the list 'combinations' containing tuples in one line.

```

### Nested Lists

Lists in Python can contain other lists, creating multi-dimensional structures. This feature is useful for representing matrices, tables, or hierarchical data structures. Let's explore how to work with nested lists:

#### How to Create a Nested List

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

```

In this example, we define a nested list `nested_list` containing three inner lists, each representing a row in a matrix.

#### How to Access Elements in Nested Lists

To access elements in a nested list, you use multiple indices, with each index representing the position of the element in the respective inner list. For example:

```python
print(nested_list[0][1])  # Output: 2

```

This code accesses the element at row 0 and column 1 of the nested list, yielding the value `2`.

#### How to Iterate Over Nested Lists

You can iterate over a nested list using nested loops, with an outer loop iterating over each inner list and an inner loop iterating over each element within that inner list. For example:

```python
for sublist in nested_list:
    for item in sublist:
        print(item)

```

This code iterates over each sublist in the `nested_list` and then iterates over each item within that sublist, printing each item individually.

##### Example 1: Summing Elements in a Nested List

```python
total_sum = 0
for sublist in nested_list:
    for item in sublist:
        total_sum += item
print("Total Sum:", total_sum)

```

In this example, we iterate over each sublist and each item within the sublist, summing all the elements in the nested list.

##### Example 2: Finding Maximum Value in a Nested List

```python
max_value = float('-inf')  # Initialize with negative infinity
for sublist in nested_list:
    for item in sublist:
        if item > max_value:
            max_value = item
print("Maximum Value:", max_value)

```

In this example, we find the maximum value in the nested list by iterating over each sublist and each item within the sublist, updating the `max_value` variable if a larger value is encountered.

## Conclusion

In this article, we've explored the fundamental aspects, operations, and advanced features of Python lists. You should now have a strong foundation for leveraging this versatile data structure effectively in various programming scenarios.

If you have any feedback, then DM me on [Twitter](https://twitter.com/introvertedbot) or [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).

