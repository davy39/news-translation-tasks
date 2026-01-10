---
title: Python any() and all() Functions – Explained with Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-08-10T20:26:25.000Z'
originalURL: https://freecodecamp.org/news/python-any-and-all-functions-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/POINTERS-IN-c--8-.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When coding in Python, have you ever had to check if any item or all items
  in an iterable evaluate to True? The next time you need to do so, be sure to use
  the nifty functions any() and all().

  In this tutorial, we''ll learn about Python''s any() and al...'
---

When coding in Python, have you ever had to check if _any_ item or _all_ items in an iterable evaluate to `True`? The next time you need to do so, be sure to use the nifty functions `any()` and `all()`.

In this tutorial, we'll learn about Python's `any()` and `all()` functions and use simple examples to understand how they work.

## The Boolean Data Type in Python

Before we jump into `any()` and `all()`, let's quickly revisit the Boolean data type in Python. You can call `bool()` on any Python object to get its truth value. You can run the code examples below in your favorite IDE. 

```python
# truth value of None is False
print(bool(None))
# Output
False

# truth value of an empty string ("") is False
print(bool(""))
# Output
False

# truth value of an empty list (or any iterable) is False
print(bool([]))
# Output
False

# truth value of 0 {int (0), float (0.0) and complex (0j)} is False
print(bool(0))
# Output
False
```

As shown in the snippet above,

* `None` has a truth value of `False`,
* The number zero(`0`) – integer, floating point, and complex number representations of `0` – all have a truth value of `False`, and
* All empty iterables like lists, tuples, and strings have a truth value of `False`.

That said, it's fairly intuitive that all _non-zero_ values, and _non-empty_ iterables have a truth value of `True`.

## How to Use the any() Function in Python

Let's understand the syntax of the `any()` function, look at some simple examples, and then proceed to more useful examples.

**👉 Syntax**: `any(iterable)`

* Returns `True` if `bool(x)` is `True` for any `x` in the iterable.
* Returns `False` if the iterable is empty.

Therefore, the `any()` function takes an iterable as the argument, and returns `True` so long as at least one of the items in the iterable is `True`. 

Here are a few simple examples to verify how the `any()` function works:

```python
list_1 = [0,0,0,1,0,0,0,0]
# any(a list with at least one non-zero entry) returns True
print(any(list_1))
# Output
True

list_2 = [0j,0,0,0.0,0,0,0.0,0]
# any(a list of zeros) returns False
print(any(list_2))
# Output
False

list_3 = [True, False, False]
# any(a list with at least one True value) returns True
print(any(list_3))
# Output
True

list_4 = ["","","code more"]
# any(a list with at least one non-empty string) returns True
print(any(list_4))
# Output
True

list_5 = ["","",""]
# any(a list of empty strings) returns False
print(any(list_5))
# Output
False


```

### How to Use Python's any() Function to Check for Digits in a String

Let's now use the `any()` function to check if there are _any_ digits in a string. Let's write down the steps.

* To check: Are there any digits in the string?
* Loop through the string to access each character in the string.
* Check if each character is a digit by calling the `isdigit()` method on it.
* `isdigit()` returns `True` if the character under test is a digit, else it returns `False`.

List comprehensions can be very helpful in collecting all these truth values in a list. Here's a quick recap:

```
 # List Comprehension

 [output_expression for every_item in an_iterable]
     |
     |
     V
    result of doing something on each item in the iterable
    
 # In essence, Loop through the iterable, do something on each item and
 return the result of the operation.
 
```

As shown in the code snippet below, our example string `coding**is**cool**345` contains digits. 

Therefore, calling `any()` function on the string should return `True`. We use list comprehension to get a list of `True` and `False` values depending on whether the character is a digit or not.

```python
my_string = "coding**is**cool**345"
are_there_digits = [char.isdigit() for char in my_string]
print(any(are_there_digits))

# Output
True
```

Notice how `are_there_digits` is a list with as many items as the length of the string. 

For each character in the string, there's a corresponding truth value – `True` if the character is a digit, and `False` if the character is not a digit, as shown below.

```python
print(are_there_digits)

# Output
[False, False, False, False, False, False, False, False, False, False, False,
False, False, False, False, False, False, False, True, True, True]
```

### How to Use Python's any() Function to Check for Letters in a String

Let's take another similar example. This time, let's check for the occurrence of letters in a string. 

The string under test is `***456278)))` which doesn't contain letters – calling `any()` returns `False` as expected. For each character in the string, call the `isalpha()` method to check whether or not it is a letter.

```python
my_string = "***456278)))"
num = [char.isalpha() for char in my_string]
print(any(num))

# Output
False
```

The `is_letter` is a list of `False` values, as verified below:

```python
print(is_letter)

# Output
[False, False, False, False, False, False, False, False, False, False, False, False]
```

### How to Use Python's any() Function to Combine Multiple Conditions with Logical OR

Let's say you decide to be more productive and write down the list shown below. However, you choose not to be hard on yourself and decide that you can have lots of sweets so long as one of the items in the list happens!😀

![Image](https://www.freecodecamp.org/news/content/images/2021/08/any.png)

Notice how we have multiple conditions to consider, but choose to have sweets even if one of them evaluates to `True`. 

Isn't this very similar to an `if` statement where you need to check if multiple conditions chained by the logical `or` operator evaluate to `True`? Yes, it is and the `any()` function can come in really handy in doing that.

Suppose you have `N` conditions `c1`, `c2`, `c3`, ..., `cN`. Consider the pseudocode below:

```
if c1 or c2 or ... c_(N-1) or CN:
	# DO THIS

else:
	# DO THIS
```

You can now collect all these conditions in an iterable, say, a list or a tuple, and then call `any()` on that iterable to check if one or more conditions are `True`, as shown below. Isn't this simple? 😀

```
conditions = [c1,c2,..., c_N]

if any(conditions):
	# DO THIS
else:
	# DO THIS
```

## How to Use the all() Function in Python

Let's start with the syntax of the `all()` function. 

👉 **Syntax**: `all(iterable)`

* Returns `True` if `bool(x)` is `True` for all values `x` in the iterable.
* Returns `True` if the iterable is empty.

The `all()` function takes an iterable as the argument, returns `True` only if all items in the iterable evaluate to `True` or if the iterable is empty. In all other cases, the `all()` function returns `False`.

### How to Use Python's all() Function to Check for Letters in a String

Let's take similar examples to check for certain characteristics of strings. 

The test string `coding**is**cool` contains the special character `*` in addition to letters. So, when we check if all characters in the string are letters by using the `all()` function, we should get `False`.

```python
my_string = "coding**is**cool"
are_all_letters = [char.isalpha() for char in my_string]
print(all(are_all_letters))
# Output
False

print(are_all_letters)
# Output
[True, True, True, True, True, True, False, False, True, True, False, False,
True, True, True, True]
```

Notice how the list `are_all_letters` has `False` values at all positions where the `*` is present in our string.

### How to Use Python's all() Function to Check for Digits in a String

Let's now check if all characters in the string are digits by using the `all()` function. The test string `56456278` contains only digits, so, calling `all()` should return `True` as the list comprehension gives us a list of `True` values.

```python
my_string = "56456278"
are_all_digits = [char.isdigit() for char in my_string]
print(all(are_all_digits))
# Output
True

print(are_all_digits)
# Output
[True, True, True, True, True, True, True, True]
```

### How to Use Python's all() Function to Combine Multiple Conditions with Logical AND

Let's consider the following example. This time, you're in contention for an iPad and the conditions are more stringent. You've got to complete _all_ tasks in the list to get an iPad from your cousin.😀

![Image](https://www.freecodecamp.org/news/content/images/2021/08/all.png)

Now, this is very similar to using an `if` statement to check if multiple conditions chained by the logical `and` operator evaluate to `True`, as shown below:

```
if c1 and c2 and ... c_(N-1) and CN:
	# DO THIS

else:
	# DO THIS
```

You could use the `all()` function to make this all the more concise by collecting the conditions in an iterable, and then calling the `all()` function on the iterable.

```
conditions = [c1,c2,..., c_N]

if all(conditions):
	# DO THIS
else:
	# DO THIS
```

## Conclusion

I hope this tutorial helped you understand the `any()` and `all()` functions in Python. 

See you all soon in another post. Until then, happy learning!






