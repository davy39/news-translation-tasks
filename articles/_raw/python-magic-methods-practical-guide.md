---
title: 'How Python Magic Methods Work: A Practical Guide'
subtitle: ''
author: Vivek Sahu
co_authors: []
series: null
date: '2025-03-20T15:27:59.389Z'
originalURL: https://freecodecamp.org/news/python-magic-methods-practical-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742482738702/0b357de2-855d-47c2-960f-453e0bfd9a3d.png
tags:
- name: Python
  slug: python
- name: python magic method
  slug: python-magic-method
- name: dunder method
  slug: dunder-method
- name: Tutorial
  slug: tutorial
- name: Python advanced
  slug: python-advanced
seo_title: null
seo_desc: 'Have you ever wondered how Python makes objects work with operators like
  + or -? Or how it knows how to display objects when you print them? The answer lies
  in Python''s magic methods, also known as dunder (double under) methods.

  Magic methods are spe...'
---

Have you ever wondered how Python makes objects work with operators like `+` or `-`? Or how it knows how to display objects when you print them? The answer lies in Python's magic methods, also known as dunder (d<s>ouble</s> under) methods.

Magic methods are special methods that let you define how your objects behave in response to various operations and built-in functions. They're what makes Python's object-oriented programming so powerful and intuitive.

In this guide, you'll learn how to use magic methods to create more elegant and powerful code. You'll see practical examples that show how these methods work in real-world scenarios.

## Prerequisites

* Basic understanding of Python syntax and object-oriented programming concepts.
    
* Familiarity with classes, objects, and inheritance.
    
* Knowledge of built-in Python data types (lists, dictionaries, and so on).
    
* A working Python 3 installation is recommended to actively engage with the examples here.
    

## **Table of Contents**

1. [What are Magic Methods?](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#what-are-magic-methods)
    
2. [Object Representation](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#object-representation)
    
    * [**str** vs **repr**](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#str-vs-repr)
        
    * [Practical Example: Custom Error Class](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#practical-example-custom-error-class)
        
3. [Operator Overloading](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#operator-overloading)
    
    * [Arithmetic Operators](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#arithmetic-operators)
        
    * [Comparison Operators](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#comparison-operators)
        
    * [Practical Example: Money Class](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#practical-example-money-class)
        
4. [Container Methods](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#container-methods)
    
    * [Sequence Protocol](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#sequence-protocol)
        
    * [Mapping Protocol](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#mapping-protocol)
        
    * [Practical Example: Custom Cache](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#practical-example-custom-cache)
        
5. [Attribute Access](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#attribute-access)
    
    * [**getattr** and **getattribute**](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#getattr-and-getattribute)
        
    * [**setattr** and **delattr**](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#setattr-and-delattr)
        
    * [Practical Example: Auto-Logging Properties](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#practical-example-auto-logging-properties)
        
6. [Context Managers](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#context-managers)
    
    * [**enter** and **exit**](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#enter-and-exit)
        
    * [Practical Example: Database Connection Manager](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#practical-example-database-connection-manager)
        
7. [Callable Objects](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#callable-objects)
    
    * [**call**](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#call)
        
    * [Practical Example: Memoization Decorator](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#practical-example-memoization-decorator)
        
8. [Advanced Magic Methods](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#advanced-magic-methods)
    
    * [**new** for Object Creation](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#new-for-object-creation)
        
    * [**slots** for Memory Optimization](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#slots-for-memory-optimization)
        
    * [**missing** for Default Dictionary Values](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#missing-for-default-dictionary-values)
        
9. [Performance Considerations](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#performance-considerations)
    
10. [Best Practices](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#best-practices)
    
11. [Wrapping Up](#heading-wrapping-up)
    
12. [References](https://file+.vscode-resource.vscode-cdn.net/Users/viv1/Documents/workspace/BLOG/BLOG/viv1.github.io/_posts/2025-02-15-magic-methods-in-python.md#references)
    

## **What are Magic Methods?**

Magic methods in Python are special methods that start and end with double underscores (`__`). When you use certain operations or functions on your objects, Python automatically calls these methods.

For example, when you use the `+` operator on two objects, Python looks for the `__add__` method in the left operand. If it finds it, it calls that method with the right operand as an argument.

Here's a simple example that shows how this works:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This calls p1.__add__(p2)
print(p3.x, p3.y)  # Output: 4 6
```

Let's break down what's happening here:

1. We create a `Point` class that represents a point in 2D space
    
2. The `__init__` method initializes the x and y coordinates
    
3. The `__add__` method defines what happens when we add two points
    
4. When we write `p1 + p2`, Python automatically calls `p1.__add__(p2)`
    
5. The result is a new `Point` with coordinates (4, 6)
    

This is just the beginning. Python has many magic methods that let you customize how your objects behave in different situations. Let's explore some of the most useful ones.

## **Object Representation**

When you work with objects in Python, you often need to convert them to strings. This happens when you print an object or try to display it in the interactive console. Python provides two magic methods for this purpose: `__str__` and `__repr__`.

### **str vs repr**

The `__str__` and `__repr__` methods serve different purposes:

* `__str__`: Called by the `str()` function and by the `print()` function. It should return a string that is readable for end-users.
    
* `__repr__`: Called by the `repr()` function and used in the interactive console. It should return a string that, ideally, could be used to recreate the object.
    

Here's an example that shows the difference:

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __str__(self):
        return f"{self.celsius}°C"
    
    def __repr__(self):
        return f"Temperature({self.celsius})"

temp = Temperature(25)
print(str(temp))      # Output: 25°C
print(repr(temp))     # Output: Temperature(25)
```

In this example:

* `__str__` returns a user-friendly string showing the temperature with a degree symbol
    
* `__repr__` returns a string that shows how to create the object, which is useful for debugging
    

The difference becomes clear when you use these objects in different contexts:

* When you print the temperature, you see the user-friendly version: `25°C`
    
* When you inspect the object in the Python console, you see the detailed version: `Temperature(25)`
    

### **Practical Example: Custom Error Class**

Let's create a custom error class that provides better debugging information. This example shows how you can use `__str__` and `__repr__` to make your error messages more helpful:

```python
class ValidationError(Exception):
    def __init__(self, field, message, value=None):
        self.field = field
        self.message = message
        self.value = value
        super().__init__(self.message)
    
    def __str__(self):
        if self.value is not None:
            return f"Error in field '{self.field}': {self.message} (got: {repr(self.value)})"
        return f"Error in field '{self.field}': {self.message}"
    
    def __repr__(self):
        if self.value is not None:
            return f"ValidationError(field='{self.field}', message='{self.message}', value={repr(self.value)})"
        return f"ValidationError(field='{self.field}', message='{self.message}')"

# Usage
try:
    age = -5
    if age < 0:
        raise ValidationError("age", "Age must be positive", age)
except ValidationError as e:
    print(e)  # Output: Error in field 'age': Age must be positive (got: -5)
```

This custom error class provides several benefits:

1. It includes the field name where the error occurred
    
2. It shows the actual value that caused the error
    
3. It provides both user-friendly and detailed error messages
    
4. It makes debugging easier by including all relevant information
    

## **Operator Overloading**

Operator overloading is one of the most powerful features of Python's magic methods. It lets you define how your objects behave when used with operators like `+`, `-`, `*`, and `==`. This makes your code more intuitive and readable.

### **Arithmetic Operators**

Python provides magic methods for all basic arithmetic operations. Here's a table showing which method corresponds to which operator:

| Operator | Magic Method | Description |
| --- | --- | --- |
| `+` | `__add__` | Addition |
| `-` | `__sub__` | Subtraction |
| `*` | `__mul__` | Multiplication |
| `/` | `__truediv__` | Division |
| `//` | `__floordiv__` | Floor division |
| `%` | `__mod__` | Modulo |
| `**` | `__pow__` | Exponentiation |

### **Comparison Operators**

Similarly, you can define how your objects are compared using these magic methods:

| Operator | Magic Method | Description |
| --- | --- | --- |
| `==` | `__eq__` | Equal to |
| `!=` | `__ne__` | Not equal to |
| `<` | `__lt__` | Less than |
| `>` | `__gt__` | Greater than |
| `<=` | `__le__` | Less than or equal to |
| `>=` | `__ge__` | Greater than or equal to |

### **Practical Example: Money Class**

Let's create a `Money` class that handles currency operations correctly. This example shows how to implement multiple operators and handle edge cases:

```python
from functools import total_ordering
from decimal import Decimal

@total_ordering  # Implements all comparison methods based on __eq__ and __lt__
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = Decimal(str(amount))
        self.currency = currency
    
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Cannot add different currencies: {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract different currencies: {self.currency} and {other.currency}")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Money(self.amount * Decimal(str(other)), self.currency)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Money(self.amount / Decimal(str(other)), self.currency)
        return NotImplemented
    
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.currency == other.currency and self.amount == other.amount
    
    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Cannot compare different currencies: {self.currency} and {other.currency}")
        return self.amount < other.amount
    
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"
    
    def __repr__(self):
        return f"Money({repr(float(self.amount))}, {repr(self.currency)})"
```

Let's break down the key features of this `Money` class:

1. **Precision handling**: We use `Decimal` instead of `float` to avoid floating-point precision issues with money calculations.
    
2. **Currency safety**: The class prevents operations between different currencies to avoid errors.
    
3. **Type checking**: Each method checks if the other operand is of the correct type using `isinstance()`.
    
4. **NotImplemented**: When an operation doesn't make sense, we return `NotImplemented` to let Python try the reverse operation.
    
5. **@total\_ordering**: This decorator automatically implements all comparison methods based on `__eq__` and `__lt__`.
    

Here's how to use the `Money` class:

```python
# Basic arithmetic
wallet = Money(100, "USD")
expense = Money(20, "USD")
remaining = wallet - expense
print(remaining)  # Output: USD 80.00

# Working with different currencies
salary = Money(5000, "USD")
bonus = Money(1000, "USD")
total = salary + bonus
print(total)  # Output: USD 6000.00

# Division by scalar
weekly_pay = salary / 4
print(weekly_pay)  # Output: USD 1250.00

# Comparisons
print(Money(100, "USD") > Money(50, "USD"))  # Output: True
print(Money(100, "USD") == Money(100, "USD"))  # Output: True

# Error handling
try:
    Money(100, "USD") + Money(100, "EUR")
except ValueError as e:
    print(e)  # Output: Cannot add different currencies: USD and EUR
```

This `Money` class demonstrates several important concepts:

1. How to handle different types of operands
    
2. How to implement proper error handling
    
3. How to use the `@total_ordering` decorator
    
4. How to maintain precision in financial calculations
    
5. How to provide both string and representation methods
    

## **Container Methods**

Container methods let you make your objects behave like built-in containers such as lists, dictionaries, or sets. This is particularly useful when you need custom behavior for storing and retrieving data.

### **Sequence Protocol**

To make your object behave like a sequence (like a list or tuple), you need to implement these methods:

| Method | Description | Example Usage |
| --- | --- | --- |
| `__len__` | Returns the length of the container | `len(obj)` |
| `__getitem__` | Allows indexing with `obj[key]` | `obj[0]` |
| `__setitem__` | Allows assignment with `obj[key] = value` | `obj[0] = 42` |
| `__delitem__` | Allows deletion with `del obj[key]` | `del obj[0]` |
| `__iter__` | Returns an iterator for the container | `for item in obj:` |
| `__contains__` | Implements the `in` operator | `42 in obj` |

### **Mapping Protocol**

For dictionary-like behavior, you'll want to implement these methods:

| Method | Description | Example Usage |
| --- | --- | --- |
| `__getitem__` | Get value by key | `obj["key"]` |
| `__setitem__` | Set value by key | `obj["key"] = value` |
| `__delitem__` | Delete key-value pair | `del obj["key"]` |
| `__len__` | Get number of key-value pairs | `len(obj)` |
| `__iter__` | Iterate over keys | `for key in obj:` |
| `__contains__` | Check if key exists | `"key" in obj` |

### **Practical Example: Custom Cache**

Let's implement a time-based cache that automatically expires old entries. This example shows how to create a custom container that behaves like a dictionary but with additional functionality:

```python
import time
from collections import OrderedDict

class ExpiringCache:
    def __init__(self, max_age_seconds=60):
        self.max_age = max_age_seconds
        self._cache = OrderedDict()  # {key: (value, timestamp)}
    
    def __getitem__(self, key):
        if key not in self._cache:
            raise KeyError(key)
        
        value, timestamp = self._cache[key]
        if time.time() - timestamp > self.max_age:
            del self._cache[key]
            raise KeyError(f"Key '{key}' has expired")
        
        return value
    
    def __setitem__(self, key, value):
        self._cache[key] = (value, time.time())
        self._cache.move_to_end(key)  # Move to end to maintain insertion order
    
    def __delitem__(self, key):
        del self._cache[key]
    
    def __len__(self):
        self._clean_expired()  # Clean expired items before reporting length
        return len(self._cache)
    
    def __iter__(self):
        self._clean_expired()  # Clean expired items before iteration
        for key in self._cache:
            yield key
    
    def __contains__(self, key):
        if key not in self._cache:
            return False
        
        _, timestamp = self._cache[key]
        if time.time() - timestamp > self.max_age:
            del self._cache[key]
            return False
        
        return True
    
    def _clean_expired(self):
        """Remove all expired entries from the cache."""
        now = time.time()
        expired_keys = [
            key for key, (_, timestamp) in self._cache.items()
            if now - timestamp > self.max_age
        ]
        for key in expired_keys:
            del self._cache[key]
```

Let's break down how this cache works:

1. **Storage**: The cache uses an `OrderedDict` to store key-value pairs along with timestamps.
    
2. **Expiration**: Each value is stored as a tuple of `(value, timestamp)`. When accessing a value, we check if it has expired.
    
3. **Container methods**: The class implements all necessary methods to behave like a dictionary:
    
    * `__getitem__`: Retrieves values and checks expiration
        
    * `__setitem__`: Stores values with current timestamp
        
    * `__delitem__`: Removes entries
        
    * `__len__`: Returns number of non-expired entries
        
    * `__iter__`: Iterates over non-expired keys
        
    * `__contains__`: Checks if a key exists
        

Here's how to use the cache:

```python
# Create a cache with 2-second expiration
cache = ExpiringCache(max_age_seconds=2)

# Store some values
cache["name"] = "Vivek"
cache["age"] = 30

# Access values
print("name" in cache)  # Output: True
print(cache["name"])    # Output: Vivek
print(len(cache))       # Output: 2

# Wait for expiration
print("Waiting for expiration...")
time.sleep(3)

# Check expired values
print("name" in cache)  # Output: False
try:
    print(cache["name"])
except KeyError as e:
    print(f"KeyError: {e}")  # Output: KeyError: 'name'

print(len(cache))  # Output: 0
```

This cache implementation provides several benefits:

1. Automatic expiration of old entries
    
2. Dictionary-like interface for easy use
    
3. Memory efficiency by removing expired entries
    
4. Thread-safe operations (assuming single-threaded access)
    
5. Maintains insertion order of entries
    

## **Attribute Access**

Attribute access methods let you control how your objects handle getting, setting, and deleting attributes. This is particularly useful for implementing properties, validation, and logging.

### **getattr and getattribute**

Python provides two methods for controlling attribute access:

1. `__getattr__`: Called only when an attribute lookup fails (that is, when the attribute doesn't exist)
    
2. `__getattribute__`: Called for every attribute access, even for attributes that exist
    

The key difference is that `__getattribute__` is called for all attribute access, while `__getattr__` is only called when the attribute isn't found through normal means.

Here's a simple example showing the difference:

```python
class AttributeDemo:
    def __init__(self):
        self.name = "Vivek"
    
    def __getattr__(self, name):
        print(f"__getattr__ called for {name}")
        return f"Default value for {name}"
    
    def __getattribute__(self, name):
        print(f"__getattribute__ called for {name}")
        return super().__getattribute__(name)

demo = AttributeDemo()
print(demo.name)      # Output: __getattribute__ called for name
                      #        Vivek
print(demo.age)       # Output: __getattribute__ called for age
                      #        __getattr__ called for age
                      #        Default value for age
```

### **setattr and delattr**

Similarly, you can control how attributes are set and deleted:

1. `__setattr__`: Called when an attribute is set
    
2. `__delattr__`: Called when an attribute is deleted
    

These methods let you implement validation, logging, or custom behavior when attributes are modified.

### **Practical Example: Auto-Logging Properties**

Let's create a class that automatically logs all property changes. This is useful for debugging, auditing, or tracking object state changes:

```python
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LoggedObject:
    def __init__(self, **kwargs):
        self._data = {}
        # Initialize attributes without triggering __setattr__
        for key, value in kwargs.items():
            self._data[key] = value
    
    def __getattr__(self, name):
        if name in self._data:
            logging.debug(f"Accessing attribute {name}: {self._data[name]}")
            return self._data[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        if name == "_data":
            # Allow setting the _data attribute directly
            super().__setattr__(name, value)
        else:
            old_value = self._data.get(name, "<undefined>")
            self._data[name] = value
            logging.info(f"Changed {name}: {old_value} -> {value}")
    
    def __delattr__(self, name):
        if name in self._data:
            old_value = self._data[name]
            del self._data[name]
            logging.info(f"Deleted {name} (was: {old_value})")
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
```

Let's break down how this class works:

1. **Storage**: The class uses a private `_data` dictionary to store attribute values.
    
2. **Attribute access**:
    
    * `__getattr__`: Returns values from `_data` and logs debug messages
        
    * `__setattr__`: Stores values in `_data` and logs changes
        
    * `__delattr__`: Removes values from `_data` and logs deletions
        
3. **Special handling**: The `_data` attribute itself is handled differently to avoid infinite recursion.
    

Here's how to use the class:

```python
# Create a logged object with initial values
user = LoggedObject(name="Vivek", email="hello@wewake.dev")

# Modify attributes
user.name = "Vivek"  # Logs: Changed name: Vivek -> Vivek
user.age = 30         # Logs: Changed age: <undefined> -> 30

# Access attributes
print(user.name)      # Output: Vivek

# Delete attributes
del user.email        # Logs: Deleted email (was: hello@wewake.dev)

# Try to access deleted attribute
try:
    print(user.email)
except AttributeError as e:
    print(f"AttributeError: {e}")  # Output: AttributeError: 'LoggedObject' object has no attribute 'email'
```

This implementation provides several benefits:

1. Automatic logging of all attribute changes
    
2. Debug-level logging for attribute access
    
3. Clear error messages for missing attributes
    
4. Easy tracking of object state changes
    
5. Useful for debugging and auditing
    

## **Context Managers**

Context managers are a powerful feature in Python that helps you manage resources properly. They ensure that resources are properly acquired and released, even if an error occurs. The `with` statement is the most common way to use context managers.

### **enter and exit**

To create a context manager, you need to implement two magic methods:

1. `__enter__`: Called when entering the `with` block. It should return the resource to be managed.
    
2. `__exit__`: Called when exiting the `with` block, even if an exception occurs. It should handle cleanup.
    

The `__exit__` method receives three arguments:

* `exc_type`: The type of the exception (if any)
    
* `exc_val`: The exception instance (if any)
    
* `exc_tb`: The traceback (if any)
    

### **Practical Example: Database Connection Manager**

Let's create a context manager for database connections. This example shows how to properly manage database resources and handle transactions:

```python
import sqlite3
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        logging.info(f"Connecting to database: {self.db_path}")
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f"An error occurred: {exc_val}")
            self.connection.rollback()
            logging.info("Transaction rolled back")
        else:
            self.connection.commit()
            logging.info("Transaction committed")
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        
        logging.info("Database connection closed")
        
        # Return False to propagate exceptions, True to suppress them
        return False
```

Let's break down how this context manager works:

1. **Initialization**:
    
    * The class takes a database path
        
    * It initializes connection and cursor as None
        
2. **Enter method**:
    
    * Creates a database connection
        
    * Creates a cursor
        
    * Returns the cursor for use in the `with` block
        
3. **Exit method**:
    
    * Handles transaction management (commit/rollback)
        
    * Closes cursor and connection
        
    * Logs all operations
        
    * Returns False to propagate exceptions
        

Here's how to use the context manager:

```python
# Create a test database in memory
try:
    # Successful transaction
    with DatabaseConnection(":memory:") as cursor:
        # Create a table
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)
        
        # Insert data
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            ("Vivek", "hello@wewake.dev")
        )
        
        # Query data
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())  # Output: [(1, 'Vivek', 'hello@wewake.dev')]
    
    # Demonstrate transaction rollback on error
    with DatabaseConnection(":memory:") as cursor:
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            ("Wewake", "contact@wewake.dev")
        )
        # This will cause an error - table 'nonexistent' doesn't exist
        cursor.execute("SELECT * FROM nonexistent")
except sqlite3.OperationalError as e:
    print(f"Caught exception: {e}")
```

This context manager provides several benefits:

1. Resources are managed automatically (ex: connections are always closed).
    
2. With transaction safety, changes are committed or rolled back appropriately.
    
3. Exceptions are caught and handled gracefully
    
4. All operations are logged for debugging
    
5. The `with` statement makes the code clear and concise
    

## **Callable Objects**

The `__call__` magic method lets you make instances of your class behave like functions. This is useful for creating objects that maintain state between calls or for implementing function-like behavior with additional features.

### **call**

The `__call__` method is called when you try to call an instance of your class as if it were a function. Here's a simple example:

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Create instances that behave like functions
double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

This example shows how `__call__` lets you create objects that maintain state (the factor) while being callable like functions.

### **Practical Example: Memoization Decorator**

Let's implement a memoization decorator using `__call__`. This decorator will cache function results to avoid redundant computations:

```python
import time
import functools

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        # Preserve function metadata (name, docstring, etc.)
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        # Create a key from the arguments
        # For simplicity, we assume all arguments are hashable
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)
        
        return self.cache[key]

# Usage
@Memoize
def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Measure execution time
def time_execution(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__}({args}, {kwargs}) took {end - start:.6f} seconds")
    return result

# Without memoization, this would be extremely slow
print("Calculating fibonacci(35)...")
result = time_execution(fibonacci, 35)
print(f"Result: {result}")

# Second call is instant due to memoization
print("\nCalculating fibonacci(35) again...")
result = time_execution(fibonacci, 35)
print(f"Result: {result}")
```

Let's break down how this memoization decorator works:

1. **Initialization**:
    
    * Takes a function as an argument
        
    * Creates a cache dictionary to store results
        
    * Preserves the function's metadata using `functools.update_wrapper`
        
2. **Call method**:
    
    * Creates a unique key from the function arguments
        
    * Checks if the result is in the cache
        
    * If not, computes the result and stores it
        
    * Returns the cached result
        
3. **Usage**:
    
    * Applied as a decorator to any function
        
    * Automatically caches results for repeated calls
        
    * Preserves function metadata and behavior
        

The benefits of this implementation include:

1. Better performance, as it avoids redundant computations
    
2. Better, transparency, as it works without modifying the original function
    
3. It’s flexible, and can be used with any function
    
4. It’s memory efficient and caches results for reuse
    
5. It maintains function documentation
    

## **Advanced Magic Methods**

Now let's explore some of Python's more advanced magic methods. These methods give you fine-grained control over object creation, memory usage, and dictionary behavior.

### **new for Object Creation**

The `__new__` method is called before `__init__` and is responsible for creating and returning a new instance of the class. This is useful for implementing patterns like singletons or immutable objects.

Here's an example of a singleton pattern using `__new__`:

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name=None):
        # This will be called every time Singleton() is called
        if name is not None:
            self.name = name

# Usage
s1 = Singleton("Vivek")
s2 = Singleton("Wewake")
print(s1 is s2)  # Output: True
print(s1.name)   # Output: Wewake (the second initialization overwrote the first)
```

Let's break down how this singleton works:

1. **Class variable**: `_instance` stores the single instance of the class
    
2. **new** method:
    
    * Checks if an instance exists
        
    * Creates one if it doesn't
        
    * Returns the existing instance if it does
        
3. **init** method:
    
    * Called every time the constructor is used
        
    * Updates the instance's attributes
        

### **slots for Memory Optimization**

The `__slots__` class variable restricts which attributes an instance can have, saving memory. This is particularly useful when you have many instances of a class with a fixed set of attributes.

Here's a comparison of regular and slotted classes:

```python
import sys

class RegularPerson:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class SlottedPerson:
    __slots__ = ['name', 'age', 'email']
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Compare memory usage
regular_people = [RegularPerson("Vivek" + str(i), 30, "hello@wewake.dev") for i in range(1000)]
slotted_people = [SlottedPerson("Vivek" + str(i), 30, "hello@wewake.dev") for i in range(1000)]

print(f"Regular person size: {sys.getsizeof(regular_people[0])} bytes")  # Output: Regular person size: 48 bytes
print(f"Slotted person size: {sys.getsizeof(slotted_people[0])} bytes")  # Output: Slotted person size: 56 bytes
print(f"Memory saved per instance: {sys.getsizeof(regular_people[0]) - sys.getsizeof(slotted_people[0])} bytes")  # Output: Memory saved per instance: -8 bytes
print(f"Total memory saved for 1000 instances: {(sys.getsizeof(regular_people[0]) - sys.getsizeof(slotted_people[0])) * 1000 / 1024:.2f} KB")  # Output: Total memory saved for 1000 instances: -7.81 KB
```

Running this code produces an interesting result:

```plaintext
Regular person size: 48 bytes
Slotted person size: 56 bytes
Memory saved per instance: -8 bytes
Total memory saved for 1000 instances: -7.81 KB
```

Surprisingly, in this simple example, the slotted instance is actually 8 bytes larger than the regular instance! This seems to contradict the common advice about `__slots__` saving memory.

So what's going on here? The real memory savings from `__slots__` come from:

1. Eliminating dictionaries: Regular Python objects store their attributes in a dictionary (`__dict__`), which has overhead. The `sys.getsizeof()` function doesn't account for this dictionary's size.
    
2. Storing attributes: For small objects with few attributes, the overhead of the slot descriptors can outweigh the dictionary savings.
    
3. Scalability: The real benefit appears when:
    
    * You have many instances (thousands or millions)
        
    * Your objects have many attributes
        
    * You're adding attributes dynamically
        

Let's see a more complete comparison:

```python
# A more accurate memory measurement
import sys

def get_size(obj):
    """Get a better estimate of the object's size in bytes."""
    size = sys.getsizeof(obj)
    if hasattr(obj, '__dict__'):
        size += sys.getsizeof(obj.__dict__)
        # Add the size of the dict contents
        size += sum(sys.getsizeof(v) for v in obj.__dict__.values())
    return size

class RegularPerson:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class SlottedPerson:
    __slots__ = ['name', 'age', 'email']
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

regular = RegularPerson("Vivek", 30, "hello@wewake.dev")
slotted = SlottedPerson("Vivek", 30, "hello@wewake.dev")

print(f"Complete Regular person size: {get_size(regular)} bytes")  # Output: Complete Regular person size: 610 bytes
print(f"Complete Slotted person size: {get_size(slotted)} bytes")  # Output: Complete Slotted person size: 56 bytes
```

With this more accurate measurement, you'll see that slotted objects typically use less total memory, especially as you add more attributes.

Key points about `__slots__`:

1. **Real memory benefits**: The primary memory savings come from eliminating the instance `__dict__`
    
2. **Dynamic restrictions**: You can't add arbitrary attributes to slotted objects
    
3. **Inheritance considerations**: Using `__slots__` with inheritance requires careful planning
    
4. **Use cases**: Best for classes with many instances and fixed attributes
    
5. **Performance bonus**: Can also provide faster attribute access in some cases
    

### **missing for Default Dictionary Values**

The `__missing__` method is called by dictionary subclasses when a key is not found. This is useful for implementing dictionaries with default values or automatic key creation.

Here's an example of a dictionary that automatically creates empty lists for missing keys:

```python
class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]

# Usage
groups = AutoKeyDict()
groups["team1"].append("Vivek")
groups["team1"].append("Wewake")
groups["team2"].append("Vibha")

print(groups)  # Output: {'team1': ['Vivek', 'Wewake'], 'team2': ['Vibha']}
```

This implementation provides several benefits:

1. No need to check if a key exists, which is more convenient.
    
2. Automatic initialization creates default values as needed.
    
3. Reduces boilerplate for dictionary initialization.
    
4. It’s more flexible, and can implement any default value logic.
    
5. Only creates values when needed, making it more memory efficient.
    

## **Performance Considerations**

While magic methods are powerful, they can impact performance if you don’t use them carefully. Let's explore some common performance considerations and how to measure them.

### **Impact of Magic Methods on Performance**

Different magic methods have different performance implications:

**Attribute Access methods**:

* `__getattr__`, `__getattribute__`, `__setattr__`, and `__delattr__` are called frequently
    
* Complex operations in these methods can significantly slow down your code
    

**Container methods**:

* `__getitem__`, `__setitem__`, and `__len__` are called often in loops
    
* Inefficient implementations can make your container much slower than built-in types
    

**Operator overloading**:

* Arithmetic and comparison operators are used frequently
    
* Complex implementations can make simple operations unexpectedly slow
    

Let's measure the performance impact of `__getattr__` vs. direct attribute access:

```python
import time

class DirectAccess:
    def __init__(self):
        self.value = 42

class GetAttrAccess:
    def __init__(self):
        self._value = 42
    
    def __getattr__(self, name):
        if name == "value":
            return self._value
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

# Measure performance
direct = DirectAccess()
getattr_obj = GetAttrAccess()

def benchmark(obj, iterations=1000000):
    start = time.time()
    for _ in range(iterations):
        x = obj.value
    end = time.time()
    return end - start

direct_time = benchmark(direct)
getattr_time = benchmark(getattr_obj)

print(f"Direct access: {direct_time:.6f} seconds")
print(f"__getattr__ access: {getattr_time:.6f} seconds")
print(f"__getattr__ is {getattr_time / direct_time:.2f}x slower")
```

Running this benchmark shows significant performance differences:

```plaintext
Direct access: 0.027714 seconds
__getattr__ access: 0.060646 seconds
__getattr__ is 2.19x slower
```

As you can see, using `__getattr__` is more than twice as slow as direct attribute access. This might not matter for occasionally accessed attributes, but it can become significant in performance-critical code that accesses attributes in tight loops.

### **Optimization Strategies**

Fortunately, there are various ways you can optimize magic methods.

1. **Use slots for memory efficiency**: This reduces memory usage and improves attribute access speed. It’s best for classes with many instances.
    
2. **Cache computed values**: You can store results of expensive operations and update the cache only when necessary. Use `@property` for computed attributes.
    
3. **Minimize method calls**: Make sure you avoid unnecessary magic method calls and use direct attribute access when possible. Consider using `__slots__` for frequently accessed attributes.
    

## **Best Practices**

When using magic methods, follow these best practices to ensure your code is maintainable, efficient, and reliable.

### **1\. Be Consistent**

When implementing related magic methods, maintain consistency in behavior:

```python
from functools import total_ordering

@total_ordering
class ConsistentNumber:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, ConsistentNumber):
            return NotImplemented
        return self.value == other.value
    
    def __lt__(self, other):
        if not isinstance(other, ConsistentNumber):
            return NotImplemented
        return self.value < other.value
```

### **2\. Return NotImplemented**

When an operation doesn't make sense, return `NotImplemented` to let Python try the reverse operation:

```python
class Money:
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        # ... rest of the implementation
```

### **3\. Keep It Simple**

Magic methods should be simple and predictable. Avoid complex logic that could lead to unexpected behavior:

```python
# Good: Simple and predictable
class SimpleContainer:
    def __init__(self):
        self.items = []
    
    def __getitem__(self, index):
        return self.items[index]

# Bad: Complex and potentially confusing
class ComplexContainer:
    def __init__(self):
        self.items = []
        self.access_count = 0
    
    def __getitem__(self, index):
        self.access_count += 1
        if self.access_count > 100:
            raise RuntimeError("Too many accesses")
        return self.items[index]
```

### **4\. Document Behavior**

Clearly document how your magic methods behave, especially if they deviate from standard expectations:

```python
class CustomDict(dict):
    def __missing__(self, key):
        """
        Called when a key is not found in the dictionary.
        Creates a new list for the key and returns it.
        This allows for automatic list creation when accessing
        non-existent keys.
        """
        self[key] = []
        return self[key]
```

### **5\. Consider Performance**

Be aware of the performance implications, especially for frequently called methods:

```python
class OptimizedContainer:
    __slots__ = ['items']  # Use __slots__ for better performance
    
    def __init__(self):
        self.items = []
    
    def __getitem__(self, index):
        return self.items[index]  # Direct access is faster
```

### **6\. Handle Edge Cases**

Always consider edge cases and handle them appropriately:

```python
class SafeContainer:
    def __getitem__(self, key):
        if not isinstance(key, (int, slice)):
            raise TypeError("Index must be integer or slice")
        if key < 0:
            raise ValueError("Index cannot be negative")
        # ... rest of the implementation
```

## **Wrapping Up**

Python's magic methods provide a powerful way to make your classes behave like built-in types, enabling more intuitive and expressive code. Throughout this guide, we've explored how these methods work and how to use them effectively.

### **Key Takeaways**

1. **Object representation**:
    
    * Use `__str__` for user-friendly output
        
    * Use `__repr__` for debugging and development
        
2. **Operator overloading**:
    
    * Implement arithmetic and comparison operators
        
    * Return `NotImplemented` for unsupported operations
        
    * Use `@total_ordering` for consistent comparisons
        
3. **Container behavior**:
    
    * Implement sequence and mapping protocols
        
    * Consider performance for frequently used operations
        
    * Handle edge cases appropriately
        
4. **Resource management**:
    
    * Use context managers for proper resource handling
        
    * Implement `__enter__` and `__exit__` for cleanup
        
    * Handle exceptions in `__exit__`
        
5. **Performance optimization**:
    
    * Use `__slots__` for memory efficiency
        
    * Cache computed values when appropriate
        
    * Minimize method calls in frequently used code
        

### **When to Use Magic Methods**

Magic methods are most useful when you need to:

1. Create custom data structures
    
2. Implement domain-specific types
    
3. Manage resources properly
    
4. Add special behavior to your classes
    
5. Make your code more Pythonic
    

### **When to Avoid Magic Methods**

Avoid magic methods when:

1. Simple attribute access is sufficient
    
2. The behavior would be confusing or unexpected
    
3. Performance is critical and magic methods would add overhead
    
4. The implementation would be overly complex
    

Remember that with great power comes great responsibility. Use magic methods judiciously, keeping in mind their performance implications and the principle of least surprise. When used appropriately, magic methods can significantly enhance the readability and expressiveness of your code.

## **References and Further Reading**

### **Official Python Documentation**

1. [Python Data Model - Official Documentation](https://docs.python.org/3/reference/datamodel.html) - Comprehensive guide to Python's data model and magic methods.
    
2. [functools.total\_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering) - Documentation for the total\_ordering decorator that automatically fills in missing comparison methods.
    
3. [Python Special Method Names](https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers) - Official reference for special method identifiers in Python.
    
4. [Collections Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html) - Learn about abstract base classes for containers which define the interfaces that your container classes can implement.
    

### **Community Resources**

5. [A Guide to Python's Magic Methods - Rafe Kettler](https://rszalski.github.io/magicmethods/) - Practical examples of magic methods and common use cases.
    

### **Further Reading**

If you enjoyed this article, you might find these Python-related articles on my [personal blog](https://wewake.dev) useful:

1. [Practical Experiments for Django ORM Query Optimizations](https://wewake.dev/posts/practical-experiments-for-django-orm-query-optimizations/) - Learn how to optimize your Django ORM queries with practical examples and experiments.
    
2. [The High Cost of Synchronous uWSGI](https://wewake.dev/posts/high-cost-of-sync-uwsgi/) - Understand the performance implications of synchronous processing in uWSGI and how it affects your Python web applications.
