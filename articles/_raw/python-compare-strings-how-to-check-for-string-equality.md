---
title: Python Compare Strings – How to Check for String Equality
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-18T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/python-compare-strings-how-to-check-for-string-equality
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/compare1.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When crafting the logic in your code, you may want to execute different\
  \ commands depending on the similarities or differences between two or more strings.\
  \ \nIn this article, we'll see various operators that can help us check if strings\
  \ are equal or no..."
---

When crafting the logic in your code, you may want to execute different commands depending on the similarities or differences between two or more strings. 

In this article, we'll see various operators that can help us check if strings are equal or not. If two strings are equal, the value returned would be `True`. Otherwise, it'll return `False`.

## How to Check for String Equality in Python

In this section, we'll see examples of how we can compare strings using a few operators.

But before that, you need to have the following in mind:

* Comparisons are case sensitive. **G** is not the same as **g**.
* Each character in a string has an [ASCII value](https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/) (American Standard Code for Information Interchange) which is what operators look out for, and not the actual character. For example, **G** has an ASCII value of 71 while **g** has a value of of 103. When compared, **g** becomes greater than **G**.

### How to Compare Strings Using the `==` Operator

The `==` operator checks if two strings are equal. Here is an example:

```python
print("Hello" == "Hello")
# True
```

We got a value of `True` returned because both strings above are equal. 

Let's make it look a bit more fancy using some conditional logic:

```python
string1 = "Hello"
string2 = "Hello"

if string1 == string2:
    print("Both strings are equal")
else:
    print("Both strings are not equal")
    
# Both strings are equal
```

In the code above, we created two strings and stored them in variables. We then compared their values. If these values are the same, we would get one message printed to the console and if they aren't the same, we would have a different message printed. 

Both strings in our case were equal, so we had "Both strings are equal" printed. If we changed the first string to "hello", then we would have a different message. 

Note that using `=` would make the interpreter assume you want to assign one value to another. So make sure you use `==` for comparison.

### How to Compare Strings Using the `!=` Operator

The `!=` operator checks if two strings are **not** equal. 

```python
string1 = "Hello"
string2 = "Hello"

if string1 != string2:
    print("Both strings are not equal") # return if true
else:
    print("Both strings are equal") # return if false
    
# Both strings are equal
```

We're using the same example but with a different operator. The `!=` is saying the strings are not equal which is `False` so a message is printed based on those conditions. 

I have commented the code to help you understand better.

### How to Compare Strings Using the `<` Operator

The `<` operator checks if one string is smaller than the other. 

```python
print("Hello" < "hello")

# True
```

This returns `True` because even though every other character index in both strings is equal, **H** has a smaller (ASCII) value than **h** .

We can also use conditional statements here like we did in previous sections.

### How to Compare Strings Using the `<=` Operator

The `<=` operator checks if one string is less than or equal to another string.

```python
print("Hello" <= "Hello")

# True
```

Recall that this operator checks for two things – if one string is less or if both strings are the same – and would return `True` if either is true.

We got `True` because both strings are equal. 

### How to Compare Strings Using the `>` Operator

The `>` operator checks if one string is greater than another string. 

```python
print("Hello" > "Hello")

# False
```

Since the string on the left isn't greater than the one on the right, we got `False` returned to us.

### How to Compare Strings Using the `>=` Operator

The `>=` operator checks if one string is greater than or equal to another string. 

```python
print("Hello" >= "Hello")

# True
```

Since one of both conditions of the operator is true (both strings are equal), we got a value of `True`.

## Conclusion

In this article, we learned about the various operators you can use when checking the equality of strings in Python with examples. We also saw how case sensitivity can alter the equality of strings. 

Happy coding!

