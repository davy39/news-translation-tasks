---
title: How to Use Data Types in Python – Explained with Code Examples
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2024-02-09T15:15:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-data-types-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Python-Data-Types.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In Python, a data type communicates with the interpreter about how the
  programmer intends to use the data and information stored. The classification of
  data specifies the type of value a variable can hold.

  In Python programming, you don''t need to exp...'
---

In Python, a data type communicates with the interpreter about how the programmer intends to use the data and information stored. The classification of data specifies the type of value a variable can hold.

In Python programming, you don't need to explicitly declare the data type of your variable. Instead, Python, as a dynamically typed language, determines the data type of your variable according to the assigned value.

A solid understanding of data types in Python is crucial as it allows programmers to write concise code. Python has several built-in data types like the sequence, numeric, mapping, set, none, and Boolean types of data.

This article will discuss the following topics:

* [Numeric Data Types in Python](#heading-numeric-data-types-in-python)
* [Sequence Data Types in Python](#heading-sequence-data-types-in-python)
* [Mapping Data Type in Python](#heading-mapping-data-type-in-python)
* [Set Data Type in Python](#heading-set-data-type-in-python)
* [None Data Type in Python](#heading-none-data-type-in-python)
* [Boolean Data Type in Python](#heading-boolean-data-type-in-python)
* [Wrapping Up](#heading-wrapping-up)

## Numeric Data Types in Python

Have you ever thought about working with numerical values with Python? If yes, numeric data types are used to represent any numerical values. 

There are three main numeric data types in Python: integers, floating-point numbers, and the complex numbers.

### Integer Data Type in Python

In Python, integers are known as `int`. They are a built-in data type for whole numbers. `int` can represent any size of integers without overflow errors because they can either be positive, zero, or negative.

```python
# Python Integer
a = 7
y = -1
c = 0

print(a)  # Output: 7
print(y)  # Output: -1
print(c)  # Output: 0

```

Numerous arithmetic calculations like addition, subtraction, multiplication, modulus, integer division, exponentiation, and division can be performed with integers.

```python
# Addition Operation +

addition = 8 + 3
print("Addition:", addition)  # Output: 11

# Subtraction operation -
subtraction = 9 - 4
print("Subtraction:", subtraction)  # Output: 5

# Multiplication operation *
multiplication = 10 * 2
print("Multiplication:", multiplication)  # Output: 20

# Division operation /
division = 10 / 6
print("Division:", division)  # Output: 1.6666666666666667

# Integer Division operation //
integer_division = 10 // 2
print("Integer Division:", integer_division)  # Output: 5

# Modulus operation %
modulus = 10 % 5
print("Modulus:", modulus)  # Output: 0

# Exponentiation operation **
exponentiation = 2 ** 6
print("Exponentiation:", exponentiation)  # Output: 64

```

### Floating-point Data Type in Python

In Python, `float` can represent both whole numbers and fractions. They are used for approximating real numbers. Hence, they are not precise when dealing with a very small or a very large numbers.

```python
# Python Float
b = 2.47
y = -0.1
k = 5.0

print(b)  # Output: 2.47
print(y)  # Output: -0.1
print(k)  # Output: 5.0

```

Floating-point arithmetic calculations like addition, subtraction, multiplication, modulus, integer division, exponentiation, and division are performed using floating-point numbers. The float is any number with a decimal point.

```python
# Addition Operation

a = 3.5
b = 2.1
print(a + b) # Output will be 5.3

 # Subtraction Operation
c = 5.5
d = 2.2
print(c - d) # Output will be 3.3

# Multiplication operation

e = 4.0
f = 2.5
print(e * f)  # Output will be 10.0

# Division Operation
g= 10.0
h = 7.0
print(g / h) # Output will be 1.4285714285714286

# Exponential Operation 
i = 2.0
j = 3.0
print(i * j)# Output will be 6.0

# Modulus operation
k = 10.5
l = 4.0
print(k % l) # Output will be 2.5

# integer division Operation
m = 10.5
n = 3.0
print(k // l) # Output will be 2.0
```

**Note:** In Python 3, by default, dividing two integers returns a floating-point result.

### Complex Data Type in Python

`complex` numbers are popularly used in engineering, physics, and mathematics to model the real and imaginary components. The numbers take the form of `a + bj`, where `a` and `b` are real numbers, and `j` represents the imaginary unit, defined as the square root of -1.

```python
z1 = 8 + 2j  # Creates a complex number 8 + 2j
z2 = -9 - 6j # Creates a complex number -9 - 6j

```

Python can perform various arithmetic calculations like addition, subtraction, multiplication, and division with complex number.

```python
z2 = complex(3, 2)
z4 = complex(-1, 6)

# Addition Operation
sum_z = z2 + z4  # Result: 3 - 1 + (2 + 6)j = 2 + 8j

# Subtraction
diff_z = z2 - z4  # Result: 3 - (-1) + (2 - 6)j = 4 - 4j

# Multiplication
prod_z = z2 * z4 

# Result: (3 * -1 - 2 * 6) + (3 * 6 + 2 * -1)j = (-15+16j)

# Division
div_z = z2 / z4 
# Result:(0.24324324324324323-0.5405405405405406j)



```

## Sequence Data Types in Python

In Python, there are several sequence data types used to represent data collections in a specific order. They are as follows:

### List Data Type in Python

Lists are defined using square brackets `[]` with comma-separated elements. They are a mutable, built-in data structure for storing item collections. The mutability feature of `[]` means it's modifiable after creation.

Lists are a widely used data structures in Python because they support various operations and offer flexibility.

The element inside a list can be of any data type, list included.

```python
# List creation

the_list = [1, 2, 4, 5]


# creating a mixed data list
multiple_data_list = [1, 'hi', 2.57, False]



print(the_list[0])   # Output: 1
print(multiple_data_list[2])  # Output:2.57


# Mutable feature of list

the_list[0] = 10          # Modify the first element
the_list.append(9)        # Append a new element
the_list.extend([5, 4])   # Extend the list with another list
the_list.remove(2)        # Remove an element by value
del the_list[0]           # Remove an element by index

```

### Tuple Data Type in Python

In Python, a tuple is an immutable built-in data type for storing an ordered collection of elements. 

Tuples are created using parentheses `()`. Just like lists, Tuples have comma-separated elements.

A tuple requires a comma after the element to differentiate it from a parenthesized expression, even if it contains single element. The immutability feature of tuples implies that you cannot change them after creation.

```python
# Empty tuple
zilch_tuple = ()   
 
 # Tuple with a single element            
single_tuple = (1,)  

 # Tuple with multiple elements 
multiple_tuple = (1,8,9,3, 5) 

# Tuple immutability

single_slice[0] = 5

print(tuple_slice) # TypeError: 'tuple' object does not support item assignment


# Different elements tuples 
mixed_tuple = (1, 'hello', 3.14, True) 

 # Nested tuple 

nested_tuple = ('Orange', ('banana', 'Pineapple'), ["he", 'she', 'them']) 


 # Concatenate tuples

add_tuple = multiple_tuple + (6, 7, 8)  # Output: (1, 8, 9, 4, 3, 5, 7, 8)

# Create a slice of the tuple
tuple_slice = add_tuple[1:3]     # Output: (8, 9)

```

### String Data Type in Python

A string enclosed in either single `(')` or a double quote `(")` is an immutable sequence of characters used to represent textual data.

Python allows you to perform operations like, indexing, slicing, and concatenation on strings.

```python
# Creaating a String with both single and double quote

single_string = 'Hello!'
double_string = "Python Programming!"

# Outputting the result 

print(single_string[0])    # Output: 'H'
print(double_string[-1])   # Output: '!'


print(single_string[0:5])    # Output: 'Hello'
print(double_string[::2])    # Output: 'Pto rgamn!'

# Concatenate the two strings

concatenate_string = single_string + ' ' + double_string
print(concatenate_string)   # Output: 'Hello! Python Programming'


# Some popular string methods like the upper,lower,find,replace, split and strip.

print(single_string.upper())              # Output: 'HELLO!'
print(double_string.lower())              # Output: 'python programming!'
print(single_string.find('World'))        # Output: -1
print(double_string.replace('Python', 'Java'))  # Output: 'Java Programming'
print(single_string.split(','))           # Output: ['Hello!']
print(double_string.strip())              # Output: 'Python Programming!'

```

### Range Data Type in Python

The `range` function is used to iterate over elements in a list. By executing a task repeatedly, the `range` generates indices for the data structure.

The syntax for a `range` function is as follows:

```python
range(start, stop, step)

```

The `start` represents a starting value if, when omitted, the range starts from 0, while `stop` is the number that indicates that the range should stop generating numbers.

The `step` being the last value, specifies the increment or step between each different number in the sequence. The default value for this parameter is 1.

The `range` function returns an immutable series of numbers.

```python
# Generating a number from 0 to 10
for i in range(11):
    print(i)  # OUTPUT..... 0,1,2,3,4,5,6,7,8,9,10


# Generate a number from 1 to 19.
for i in range(1, 20):
    print(i) # OUTPUT.....1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
    
    
# Generating numbers from 0 to 10 with a step of 2:

for i in range(0, 21, 2):
    print(i)  # OUTPUT.... 0,2,4,6,8,10,12,14,16,18,20


# Generate a list of numbers using the list function in conjuction with range:

new_list = list(range(15))
print(new_list)  # Output: [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14]

```

## Mapping Data Type in Python

In Python, the dictionary `dict` is the primary data type for storing a collection of key-value pairs. 

The `dict` is widely used in Python for different functions, such as mapping between related information, representing a set of data records, and storing configurations. 

We can create a `dict` in Python with either the curly braces `{}` or the `dict()` constructor.

Some of the characteristics of a dictionary are as follows:

* **Key-Value Pairs**: A `dict` consists of a key associated with a specific value in a key-value pair. The function of the key is to look up the corresponding value in the dictionary.
* **Uniqueness**: Duplicate keys are not allowed in `dict`. Assigning a new value to an existing key will only replace the old value associated with that key.
* **Key Immutability**: The immutability nature of the keys ensures that keys remain "hashable" and consistent. Hence, keys in dictionary must be immutable. Some examples of immutable data types include integers, strings, and tuples.
* **Flexible Values**: Any data type including but not limited to lists, tuples, strings, numbers and even dictionaries can be associated with keys in a dictionary.

```python
person = {
    "name": "Kamaldeen",
    "age": 32,
    "city": "Nigeria"
}

```

In the code above, the keys are  the `"name"`, `"age"`, and `"city"`  while their corresponding values are  `"kamaldeen"`, `32`, and `"Nigeria"`.

```python
# Accessing values by key:

print(person["name"])  # Output: Kamaldeen

# Modifying values

person["age"] = 35  # Output: {'name': 'Kamaldeen', 'age': 35, 'city':
'Nigeria'}

# Adding a new key-value paie

person["job"] = "Engineer"  # Output: {'name': 'Kamaldeen', 'age': 32, 'city': 'Nigeria', 'job': 'Engineer'}

# Check if name is in person dictionary

if "name" in person:
    print("Name is present in the dictionary.") # Output:Name is present in the dictionary





```

## Set Data Type in Python

In Python, a `set` is a built-in data type that represents a collection of unique elements with no particular order. 

The elements in the `set` are immutable, but the `set` itself  is mutable. Sets can be defined using curly braces `{}` with comma-separated elements or by the `set()` constructor. They gets used for mathematical operations like unions, intersections, and differences.

```python
# Creating curly braces set
curly_set = {1, 2, 6, 4, 9}

# Creating  set() function set
func_set = set([1, 2, 6, 9, 5])

```

Some of the characteristics are:

* **No defined order**: In a `set`, there's no defined order because the elements are unordered.
* **Uniqueness**: Sets are unique in nature, because they do not allow duplicate elements.
* **Mutability**: Sets allow you to update either by adding or removing elements after creation.
* **Elements Immutability**: Mutable elements like `lists` cannot be an element of a set, because elements within a set must be immutable. Therefore, immutable data types like floats, integers , tuples and string can be used instead.

### Set Operation

Python supports mathematical operations like union, intersection, difference, and more for sets.

#### Union Operation Using Sets in Python

The union mathematical operation of two sets joins all unique elements from both sets.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

union_set = first_set | second_set  # Using the '|' operator
# Output: {1, 2, 3, 4, 5}

# or

union_method = first_set.union(second_set)  # Using the union() method

# Output: {1, 2, 3, 4, 5}

```

The union can be created with either the `|` or the `union()` method.

#### Intersection Operation using Sets in Python

In Python, the intersection is a mathematical operation of two sets that prints the common elements only.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

union_set = first_set & second_set  # Using the '&' operator
# Output: {3}

# or

union_method = first_set.intersection(second_set)  # Using the union() method
# Output: {3}

print(union_set)
print(union_method)
```

The intersection can be created with either the `&` or the `intersection()` method.

#### Difference Operation using Sets in Python

In Python, the difference mathematical operation between two sets occurs when an element is present in the first, but not in the second.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

union_set = first_set - second_set  # Using the '-' operator

# or

union_method = first_set.difference(second_set)  # Using the difference() method


print(union_set)
print(union_method)
```

The difference can be created with either by the `-` or the `difference()`method.

#### Add Operation using Sets in Python

The `add()` method of sets is used to add a single element to the set collection, while the `update()` method is for adding multiple element.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

# Add with add method
first_set.add(4)

# Update with update method 
second_set.update({4,8,9,7})

print(first_set) # Output: {1, 2, 3, 4}
print(second_set)  # OUtput: {3, 4, 5, 7, 8, 9}

```

#### Remove Operation using Sets in Python

In Python, the function of the `remove()` method in sets is to remove a specific element if it exists. The `discard()` method is also used  for removing an element if it exists.

The only difference is that `discard()` won't raise an error if the element doesn't exist, but `remove()` will raise a `KeyError`.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

first_set.remove(5) # Output:KeyError: 5
second_set.discard(4)  # Output:KeyError: {3, 5}

print(first_set)
print(second_set)

```

#### Frozenset Operation using Sets in Python

The `frozenset` is a built-in immutable set. It gets defined like a regular set with `{}`, but its element cannot be changed or modified after creation.

```python
# Creating a frozenset

frozen_set = frozenset([7, 2, 3, 1, 5])

# Frozensets are immutable.

 frozen_set.add(6)  # An AttributeError will be raised

# Elements of a frozenset cannot be changed once it's created

frozen_set[0] = 10  # TypeError will  be raised

# You can perform set operations like union, intersection, and difference on the frozenset
```

## None Data Type in Python

In Python, the `None` data type represents the absence of a value or a null value.

It indicates the function does not a have a return value or the expression lacks a meaningful value.

Some key takeaways from the None data type:

* **Type**: `None` is called the `NoneType` data type in Python.
* **Return Value**: `None` is the default return value for a function without a value.
* **Default Value**: We can use `None` as a default argument in the function definition.

```python
# Initializing z with None, indicating that it does not currently hold any meaningful value.

z = None
print(z)  # Output: None


y = None
if y is None:
    print("The Value of y is:" "x is None")

# Output: The Value of y is :y is None


def pair(y=None):
    if y is None:
        print("y is None")

pair()  # Output: y is None


# The greeting() function prints a message if a name is provided, otherwise it greets a stranger, but since the function does not return any value explicitly, it returns None by default.

def greeting(name):
    if name:
        print("Hi, " + name)
    else:
        print("Hi, Stranger")

result = greeting("Kamaldeen")  # Output: Hello, Kamaldeen
print(result)  # Output: None

```

## Boolean Data Type in Python

In Python, there are only two values used for comparisons and logical operation when using the `boolean` data type. They are the `True` and `False` values.

The `boolean` values are the result that arises from the comparison operators such as the equal (`==`), the not equal (`!=`), the greater than (`>`), the less than (`<`), the greater than or equal to (`>=`), and the less than or equal to (`<=`).

```python
a = 10
b = 15

# Comparison operators

print(a == b)  # False
print(a < b)   # True

# Logical operators

print(a < 10 and b > 5)  # False
print(a < 3 or b> 20)   # False
print(not(a == b))        # True

# Control Flow

age = 75

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Functions return

def is_even(number):
    return number % 2 == 0

print(is_even(10))  # True
print(is_even(7))  # False

```

## Wrapping Up

In this tutorial, you learned about the various data types in Python.

We talked about several built-in data types like the sequence, mapping, set, none, and Boolean types.

Happy reading!

