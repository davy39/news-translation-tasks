---
title: How Arrays Work in Python – Array Methods Explained with Code Examples
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2023-07-12T22:19:23.000Z'
originalURL: https://freecodecamp.org/news/how-arrays-work-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-andreas-fickl-4405941.jpg
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: null
seo_desc: "In this tutorial, you'll learn what an array is in Python. You'll also\
  \ learn some possible ways to add elements to an existing array. \nIn Python, there\
  \ is no need to use a specific data type for arrays. You can simply use a list with\
  \ all the attribut..."
---

In this tutorial, you'll learn what an array is in Python. You'll also learn some possible ways to add elements to an existing array. 

In Python, there is no need to use a specific data type for arrays. You can simply use a list with all the attributes of an array. 

If you want to create an array that includes both integers and floating-point numbers, you can use Python's array module.

## What is an Array?

An array is a unique type of variable that has the capacity to store more than one value at once. 

Let's say you have a list of objects like country names. You could store the countries in separate variables as follows:

```python
Country1 = "Germany";

Country2 = "France";

Country3 = "Denmark";

```

But suppose you wanted to search through all of the countries to discover a certain one. What if you had 200 countries instead of only 3?

The alternative is to store all these values in an array.

Arrays are useful for storing and manipulating multiple values of the same data type. They act like a variable that can hold a collection of values, all of which are the same type. These values are stored together in bordering memory.

## Python Array Methods

You can use various built-in Python methods when working with lists and arrays. Below are the methods you can use on arrays and lists in Python.

### The `Append()` method

If you want to add an item to the end of a list, you can utilize the append method.

**Example:**

```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  


# Output: ['apple', 'banana', 'cherry', 'orange']

```

The `append()` method is used to add elements to the end of a list. In this case, 'orange' is appended to the `fruits` list, resulting in the list containing four elements: 'apple', 'banana', 'cherry', and 'orange'.

Here's another example for you:

Let's create an array containing the names of cars:

```python

cars = ["Lexus", "Toyota", "Mercedez"]

```

You can use the `append()` method to add a new element to an existing list/array just as seen below.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


# Output: ['apple', 'banana', 'cherry', 'orange']

```

Output:

```
["Lexus", "Toyota", "Mercedez", "Honda"]

```

### The `Clear()` method

The `clear()` method removes all the elements from the list, just as the name implies.

**Example:**

Below is an example using the `clear()` method:

```python
cars = ["Lexus", "Toyota", "Mercedez"]

cars.clear()

print(cars)

```

Output:

Based on the explanation of the `clear()` method above, the result of this expression will be [] empty because we have cleared the entire list.

### The `Copy()` method

This function creates and returns an identical copy of the original list.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()
print(fruits_copy)


# Output: ['apple', 'banana', 'cherry']

```

In the above example, the copy() method creates a new array called fruits_copy, which is a shallow copy of the fruits array. Modifying the fruits_copy array will not affect the original fruits array.

Here's another example using the `copy()` method:

```python
cars = ["Lexus", "Toyota", "Mercedez"]


x = cars.copy()


print(x)


# Output of the above using the copy () method will be:


["Lexus", "Toyota", "Mercedez"]

```

### The `Count()` method

This method returns the number of elements with the specified value.

**Example:** 

```python
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")
print(count)


# Output: 2

```

The code above creates a list called **fruits** with four elements: 'apple', 'banana', 'cherry', and another 'banana'.  The `count()` method is then used on the `fruits` list to count the number of occurrences of the element 'banana'. It returns the count, which in this case is 2, as 'banana' appears twice in the list.

Finally, the count value is printed to the console, resulting in the output: 2.

Here's another example of using the `count()` method:

```python
# Return the number of times the value "Lexus" appears in the car list.

cars = ["Lexus", "Toyota", "Mercedez", "Lexus"]

x = cars.count("Lexus")

print(x)

```

Output of this would return int "2" as the result because "Lexus" appears twice in the cars list.

### The `Extend()` method

With this method, you can add the elements of a list (or any iterable) to the end of the current list.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
additional_fruits = ["orange", "grape"]
fruits.extend(additional_fruits)
print(fruits)

# Output: ['apple', 'banana', 'cherry', 'orange', 'grape']

```

In the example above, the `extend()` method is used to add the elements from the `additional_fruits` list to the `fruits` array. The resulting array contains all the elements from both arrays.

Note that the `extend()` method modifies the original array in place and does not return a new array.

### The `index()` method

This method returns the index of the first element with the specified value.

```python
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")

print(index)

# Output: 1

```

This code above creates a list of **fruits** containing 'apple', 'banana', and 'cherry'. It then finds the index position of 'banana' in the list and assigns it to the variable 'index'. Finally, it prints the value of 'index', which in this case would be 1.

### The `insert()` method

This array method adds an element at the specified position.

```python
numbers = [1, 2, 3, 5, 6]
numbers.insert(3, 4)
print(numbers)

# Output: [1, 2, 3, 4, 5, 6]

```

From the code above, we have an array numbers with elements [1, 2, 3, 5, 6]. We want to insert the number 4 at index 3 (which is the fourth position in the array, as Python is 0-indexed). By calling insert(3, 4), we insert the element 4 at the specified index, and the existing elements are shifted to the right to make room for the new element. The resulting array is [1, 2, 3, 4, 5, 6].

### The `pop()` method

This method removes the element at the specified position.

**Example**:

```python
# To delete an item from an array/list, you can utilize the pop() method.

# Delete the second element of the car array:

cars = ["Lexus", "Toyota", "Mercedez"]

cars.pop(2)

print(cars)

```

And here's the output:

```python
['Lexus', 'Toyota']
```

This code above deletes the second element from the 'cars' array using the 'pop()' method and then prints the updated array.

Here's another example using the pop() method:

```python
# To delete an item from an array/list, you can utilize the pop() method.

# Delete the second element of the car array:

cars = ["Lexus", "Toyota", "Mercedez"]

cars.pop(2)

print(cars)

```

Output:

```

['Lexus', 'Toyota']

```

The code deletes the second element from the `cars` array using the `pop()` method and then prints the modified array. The resulting array will contain only the first and third elements: ['Lexus', 'Toyota'].

### The `remove()` method

This method removes the first item with the specified value.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# Output Below:

["apple", "cherry"]

```

The code above creates a list called `fruits` with three elements: 'apple', 'banana', and 'cherry'. The `remove()` method is then used to remove the element 'banana' from the list. 

After removing 'banana', the updated list is printed using the `print()` function. The output will be `['apple', 'cherry']`, as 'banana' is no longer present in the list.

Here's another example using the `remove()` method:

```python
cars = ["Lexus", "Toyota", "Mercedez"]

cars.remove("Toyota")

print(cars)

```

The **remove()** function may also be used to remove an element from an array, but it should be noted that it only removes the first instance of the specified value from a list.

### The `reverse()` method

This method reverses the order of the list.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)


# Output: ['cherry', 'banana', 'apple']

```

The code above creates a list called fruits with three elements: 'apple', 'banana', and 'cherry'. Then, the `reverse()` method is called on the fruits list which reverses the order of its elements. Finally, the reversed list is printed using the print() function, resulting in the output ['cherry', 'banana', 'apple']. This means that the original order of the fruits list has been reversed.

### The `sort()` method 

This method sorts the list, just as the name implies.

**Example:**

```python
numbers = [4, 2, 1, 3]

numbers.sort()

print(numbers)

# Output: [1, 2, 3, 4]

```

The code above creates a list called `numbers` with the elements `[4, 2, 1, 3]`. The `sort()` method is then called on the `numbers` list, which sorts the elements in ascending order. After sorting, the `numbers` list becomes `[1, 2, 3, 4]`. Finally, the sorted list is printed to the console using `print(numbers)`, which outputs `[1, 2, 3, 4]`.

the `sort()` method in Python sorts the elements of a list in ascending order by default. If you want to sort the list in descending order, you can pass the parameter `reverse=True` to the `sort()` method.

Here's an example of how to sort the `numbers` list in descending order:

```python
numbers = [4, 2, 1, 3]

numbers.sort(reverse=True)

print(numbers)

# Output

[4, 3, 2, 1]

```

By passing `reverse=True` as an argument to the `sort()` method, the list is sorted in descending order.

## Conclusion

Hopefully, after reading this article, you should now have a basic understanding of what an array is in Python. 

You should also know the basic Python array methods that you'll use to modify an array or a list and how to use them.

