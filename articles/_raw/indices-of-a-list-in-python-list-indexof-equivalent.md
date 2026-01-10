---
title: Indices of a List in Python – List IndexOf() Equivalent
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-06T07:49:00.000Z'
originalURL: https://freecodecamp.org/news/indices-of-a-list-in-python-list-indexof-equivalent
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/listIndex.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: 'Python has several methods and hacks for getting the index of an item in
  iterable data like a list, tuple, and dictionary.

  In this article, we are looking at how you can get the index of a list item with
  the index() method. I’ll also show you a funct...'
---

Python has several methods and hacks for getting the index of an item in iterable data like a list, tuple, and dictionary.

In this article, we are looking at how you can get the index of a list item with the `index()` method. I’ll also show you a function that is equivalent to the `index()` method.


## What We'll Cover
- [What is the `index()` Method of a List?](#heading-what-is-the-index-method-of-a-list)
- [How to Get the Index of a List item with the `index()` Method](#heading-how-to-get-the-index-of-a-list-item-with-the-index-method)
- [How to Use the `start` and `stop` Parameters of the `index()` Method](#heading-how-to-use-the-start-and-stop-parameters-of-the-index-method)
- [How to Get the Index of a List Item with the `enumerate()` Function](#heading-how-to-get-the-index-of-a-list-item-with-the-enumerate-function)
- [Conclusion](#heading-conclusion)


## What is the `index()` Method of a List?
The `index()` method does what the name implies – it lets you get the index of an item in a list. It takes the item you want to search for its index in the list and returns its position in that list. 

Apart from the item you want to search for, the `index()` method also takes the optional parameters `start` and `stop`. `start` is the position you want the `index()` method to start looking for the item, and `stop` is the position you want it to stop searching for the item.

Here’s what the syntax of `index()` looks like:

```py
list.index(item_to_search_for, start_position, stop_position)
```

Be aware that the items in a list are zero-indexed. So, the first item takes the index `0`, the second item takes `1`, the third takes `2`, and so on.

That doesn’t mean if `6` is the last index in a list, the length is 6. In this case, the length is `7`. If you want to start referencing a list of 7 items from the last item, the last item will be `-1`, and the first item will be `-7`.

![start-graph--9-](https://www.freecodecamp.org/news/content/images/2023/04/start-graph--9-.png)


## How to Get the Index of a List item with the `index()` Method
To get the index of an item in a list, attach the `index()` method to the list and pass in the item to the `index()` method:

```py
herbivores = ["Giraffe", "Goat", "Sheep", "Cattle", "Antelope", "Rabbit"]

print(herbivores.index("Goat")) # Output: 1
```

You can also extract the index to a separate variable this way:

```py
herbivores = ["Giraffe", "Goat", "Sheep", "Cattle", "Antelope", "Rabbit"]
index_of_goat = herbivores.index("Goat") # Output: 1

print(index_of_goat)
```

If the item is a duplicate, the `index()` method would only take the first occurrence into account and ignore the others:

```py
herbivores = ["Goat", "Giraffe", "Sheep", "Cattle", "Antelope", "Giraffe" "Rabbit"]
index_of_giraffe = herbivores.index("Giraffe") 

print(index_of_giraffe) # Output: 1

omnivores = ["Pig", "Dogs", "Duck" "Bears" "Ostrich", "Hen", "Warthog", "Bears", "Dogs"]
index_of_dogs = omnivores.index("Dogs")

print(index_of_dogs) # Output: 1
```


## How to Use the `start` and `stop` Parameters of the `index()` Method
As already pointed out, you can use the `start` and `stop` parameters to specify where the `index()` method should start searching for the item and stop searching for it.

Let's see how the `start` parameter works first. In the `omnivores` list below, let’s search for the position of the second occurrence of `Dogs`:

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]

# Since we know the first occurrence is at index `1`, we can start the searching from `index 2`
index_of_dogs = omnivores.index("Dogs", 2 )

print(index_of_dogs) # Output: 5
```

You can get the position of the first occurrence of `Dogs` by specifying `0` as the `start` and anything between `2` and `4` as the `stop`:

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]
index_of_dogs = omnivores.index("Dogs", 0, 4 )

print(index_of_dogs) # Output: 1
```

If the item is not within the range you specify, you get an `valueError` exception:

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]
index_of_dogs = omnivores.index("Dogs", 2, 4 )

print(index_of_dogs) # Output: ValueError: 'Dogs' is not in list
```


## How to Get the Index of a List Item with the `enumerate()` Function
The `enumerate()` function can keep track of the positions of items in a list, tuple, or other iterable sequences of data. So, we can also use it to get the index of an item in a list. 

This makes `enumerate()` an equivalent of the `index()` method. The difference is that `enumerate()` returns the position(s) as a list and it can return the indices of multiple occurrences of the same item.

Here’s an example:

```py
herbivores = ["Goat", "Ram", "Sheep", "Cattle", "Antelope", "Giraffe", "Rabbit"]
index_of_ram = [i for i, j in enumerate(herbivores) if j == 'Ram']

print(index_of_ram) # [1]
```

In the code above:
* I used a list comprehension to find the index of the element in the list that contains the string `Ram`
* The enumerate() function iterated over the `herbivores` list and keep track of the position of each element in the list
* The `enumerate()` function takes an iterable object (in this case, herbivores) as its argument and returns an iterator that generates pairs of the form (index, element) for each element in the iterable
* `i` represents the index of the element in the `herbivores` list and `j` represents the element itself
* The `if` statement checks if the element is equal to the string `Ram`. If it is, then the index of the element (`i`) is added to the resulting list

The `enumerate()` function would also return the indices of duplicate items:

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]
indices_of_dogs = [i for i, e in enumerate(omnivores) if e == 'Dogs']

print(indices_of_dogs) # [1, 5]
```


## Conclusion
The `index()` method of `list` is a straightforward way to get the position [or index] of an item in a list.

But unfortunately, `index()` would take care of the first item and ignore the rest if it’s a duplicate. That’s why we also looked at how to get the indices of duplicate items in a list.

 So, if what you want to do is to get the positions of multiple items in a list, then enumerate() is the right option for you. 

Happy coding!


