---
title: Python List .append() – How to Add an Item to a List in Python
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-04-14T20:03:38.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-how-to-add-an-item-to-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/python-append--1-.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Lists are one of the most useful and versatile data types available in
  Python. Lists are a collection of arbitrary objects, just like arrays in other programming
  languages.

  In this tutorial you will learn:


  An overview of lists and how they are defin...'
---

Lists are one of the most useful and versatile data types available in Python. Lists are a collection of arbitrary objects, just like arrays in other programming languages.

In this tutorial you will learn:

* An overview of lists and how they are defined.
* Methods to insert data in a list using: `list.append()`, `list.extend` and `list.insert()`.
* Syntax, code examples, and output for each data insertion method. 
* How to implement a stack using list insertion and deletion methods.

### Prerequisites

For this tutorial, you need:

* Python 3.
* A code editor of your choice.

## Lists in Python

Lists have the following properties that make them powerful and flexible:

* Lists are ordered.
* Lists are accessed using the index. The first index starts at `0`.
* Lists are mutable and dynamic which means they can be modified after their creation.

### How to create a list in Python

You create a list using square brackets in Python. 

We can leave them empty and supply values later in the program:

```python
# Create an empty list

programming_lang = []
```

We can also provide values while creating a list:

```python
# Create a filled list

programming_lang = ['P','Y','T','H','O','N']
```

This would create a list as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-63.png)
_List items against indexes_

### How to access items in a list

As list items are ordered, you can access them using their index. 

Syntax: `list[index]`.

In the image below, "P" is at index "0" whereas "H" is at index "3".

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-63.png)

Let's write a short program to define a list and access its items:

```python
programming_lang = ['P','Y','T','H','O','N']

print(programming_lang)

print("At index 0:", programming_lang[0])
print("At index 3:",programming_lang[3])
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-65.png)

You can also access items using a negative index, where `-1` represents the last list item. If we wanted to access the last item from the list above, we could also use index `-1`:

```python
programming_lang = ['P','Y','T','H','O','N']

print(programming_lang)

print("At index -1:", programming_lang[-1])
print("At index -5:",programming_lang[-5])
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-66.png)

### How to find the length of a list

We can easily find the length of a list using the `len()` method.

```
programming_lang = ['P','Y','T','H','O','N']

print("Length of List: ",len(programming_lang))
```

**Output:**

![Finding a list's length.](https://www.freecodecamp.org/news/content/images/2022/04/image-67.png)
_Finding a list's length._

## Methods to Add Items to a List

We can extend a list using any of the below methods:

* `list.insert()` – inserts a single element anywhere in the list.
* `list.append()` – always adds items (strings, numbers, lists) at the end of the list.
* `list.extend()` – adds iterable items (lists, tuples, strings) to the end of the list.

### How to insert items in a list with `insert()`

You can insert items in a list at any index using the `insert()` method. There are more insertion methods and we will look at them later in this post.

Syntax of insert: `insert(index, element)`.

**Example of insert():**

```
# create a list of odd numbers
odd_n = [1,3,5,7,9]

# '21' is inserted at index 3 (4th position)
odd_n.insert(3, 21)


print('List of odd #:', odd_n)


```

Before insertion:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-76.png)

After insertion:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-77.png)

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-69.png)

### How to append an item to a list using `list.append()`

We can add a **single item** at the end of the list using `list.append()`.

**Syntax**: `list.append(item)`.

**Example:**

```python
# crops list
crops = ['corn', 'wheat', 'cotton']

# Add 'cane' to the list
crops.append('cane')

print('Updated crops list: ', crops)
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-71.png)

⚠️Note that trying to append more than one item gives an exception, as `list.append()` takes only a single argument. 

![Unable to add multiple items using list.append().](https://www.freecodecamp.org/news/content/images/2022/04/image-70.png)
_Unable to add multiple items using `list.append()`._

### How to add multiple items in a list using `list.extend()`

We can add multiple items to a list using the `extend()` method.

The below example combines two lists into a single list.

```python
# create a list
even_numbers = [2, 4, 8]

# create another list
more_even_numers = [100, 400]

# add all elements of even_numbers to more_even_numbers
even_numbers.extend(more_even_numers)


print('List after extend():', even_numbers)

```

**Output:**

![Extending a list using extend().](https://www.freecodecamp.org/news/content/images/2022/04/image-72.png)
_Extending a list using `extend()`._

### Other ways to extend lists in Python:

#### List slicing

Slicing allows us to select a range of values in a list.

The syntax is shown below:

`list[starting index:upto index]`

For example,

* list[1:3] would return items starting from index 1 up to (not including) index 3.
* Missing left index implies starting from index 0. 
    * `list[:len(list)]` means start from index 0 and continue until the end.
* Missing right index implies until the last index.
    * `list[0:]` implies to start from index 0 until the last item.

Let's see how we can add lists using slicing.

**Example**:

```python
A = [99, 100, 101]
B = [103, 104, 105]

# starting from last index +1, add items from list B

A[len(A):] = B

print('A =', A)
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-78.png)

#### Combining arrays using the + operator

Let's combine two arrays `odd` and `even` into a single list using the `+` operator.

**Example:**

```python
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]

odd += even    # odd = odd + even


# Output: [1, 2, 3, 4]
print('odd and even combined =', odd)
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-79.png)

### How to populate an empty list using `for loop` and `append()`

There are two ways to populate empty lists: using a `for` loop with `append()` and using list comprehension.

Let's first use `for` loop with `append()`.

**Example:**

In this example, we are calculating area of a square and appending the result in an array.

```python
# Return area of square
# Area of square = length x length

def square_area(side_length):
     result = []
     for length in side_length:
         result.append(length*length)
     return result


lengths = [1, 4, 9, 20]
print(square_area(lengths))

```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-80.png)

We can make the above code efficient by completely skipping the `for loop - append()` combination and using list comprehension instead. Let's see how in the next section.

### How to populate an empty list using list comprehension

List comprehension makes the code simple and readable by combining the `for` loop and `append()` into a single line.

We can modify our previous example to achieve list comprehension. Notice the commented out lines here:

```python
# Return area of square
# Area of square = length x length

def square_area(side_length):
     #result = []
     #for length in side_length:
     #    result.append(length*length)
     return [length*length for length in side_length]


lengths = [1, 4, 9, 20]
print(square_area(lengths))

```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-81.png)

Both of the methods for filling an empty list are valid and suitable in different scenarios. 

## `Append()` vs `Insert()` vs `Extend()`

`Append()` always adds a single item at the end of a list. It is useful when only a single item needs to be inserted. 

But if you need to make multiple additions, `extend()` is a better option as it adds iterable items in one batch. 

You should use `Insert()` when insertion is required at a specific index or range of indexes.

## How to Implement a Stack (LIFO)

### What is a stack (LIFO)?

Stack is an arrangement of items that follows a last-in-first-out order. The item that goes last is the one that comes out first. An example of a stack would be the undo/redo stack in photo editing apps.

The diagram below visually explains a stack.

You can add an item by using `append()`.

You can remove an item by using `pop()`. See details of the `pop()` method [here](https://docs.python.org/3/tutorial/datastructures.html#:~:text=no%20such%20item.-,list.pop(%5Bi%5D),-Remove%20the%20item).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-83.png)
_Queue visualization_

### Coding stacks

Let's create a stack class where we first declare an empty list in the `init` method.

The `push()` method appends an item to the list.

The `pop()` method deletes the last item of the list using `pop()`. If there is no item in the list, an exception will be thrown.

The __`len`__ method determines the length of the stack.

Lastly, __`repr`**__**  returns the output in a readable format.

**Class definition:**

```python
class Stack:
    def __init__(stack_t):
        stack_t._items = []

    def push(stack_t, item):
        stack_t._items.append(item)

    def pop(stack_t):
        try:
            return stack_t._items.pop()
        except IndexError:
            print("Stack is empty, all items deleted")

    def __len__(stack_t):
        return len(stack_t._items)

    def __repr__(stack_t):
        return f"stack ({stack_t._items})"


```

**Code body:**

Let's call the class functions and see the output in action.

```python
stack = Stack()

# Push items onto the top of the stack
stack.push(3)
stack.push(5)
stack.push(8)
stack.push(99)

 # Print stack

print(stack)

# Find the length of the stack
print("Length of stack is:" ,len(stack))


# Pop items from the stack
print("popping last item")
stack.pop()
print(stack)

print("popping last item again")
stack.pop()
print(stack)

print("finally the stack is")

print(stack)
```

**Output:**

We have added 3, 5, 8, 99 to the stack. Next we printed the stack and its length. Afterwards, we popped two items and printed the stack each time.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-82.png)

## Wrapping up

In this tutorial, we learned list creation methods. We also looked at some examples along with a practical implementation of stacks to see how it all works.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

