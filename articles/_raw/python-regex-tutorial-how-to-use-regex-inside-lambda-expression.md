---
title: Python RegEx Tutorial – How to use RegEx inside Lambda Expression
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-17T09:31:41.000Z'
originalURL: https://freecodecamp.org/news/python-regex-tutorial-how-to-use-regex-inside-lambda-expression
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/regexinlambda.png
tags:
- name: Lambda Expressions
  slug: lambda-expressions
- name: Python
  slug: python
- name: Python 3
  slug: python3
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'It’s possible to use RegEx inside a lambda function in Python. You can
  apply this to any Python method or function that takes a function as a parameter.
  Such functions and methods include filter(), map(), any(), sort(), and more.

  Keep reading as I sh...'
---

It’s possible to use RegEx inside a lambda function in Python. You can apply this to any Python method or function that takes a function as a parameter. Such functions and methods include `filter()`, `map()`, `any()`, `sort()`, and more.

Keep reading as I show you how to use regular expressions inside a lambda function.


## What We'll Cover
- [How to use RegEx inside the Expression of a Lambda Function](#heading-how-to-use-regex-inside-the-expression-of-a-lambda-function)
  - [How to use RegEx inside the Expression of a Lambda Function with the `filter()` Function](#heading-how-to-use-regex-inside-the-expression-of-a-lambda-function-with-the-filter-function)
  - [How to use RegEx inside the Expression of a Lambda Function with the `map()` Function](#heading-how-to-use-regex-inside-the-expression-of-a-lambda-function-with-the-map-function)
  - [How to use RegEx inside the Expression of a Lambda Function with the `sort()` Method](#heading-how-to-use-regex-inside-the-expression-of-a-lambda-function-with-the-sort-method)
- [Conclusion](#heading-conclusion)


## How to use RegEx inside the Expression of a Lambda Function
The syntax with which a lambda function can take a RegEx as its expression looks like this:

```py
lambda x: re.method(pattern, x)
```

Be aware that you have to use the lambda function on something. And that’s where the likes of `map()`, `sort()`, `filter()`, and others come in.


### How to use RegEx inside the Expression of a Lambda Function with the `filter()` Function
The first example I will show you use the `filter()` function:
```py
import re

fruits = ['apple', 'mango', 'banana', 'cherry', 'apricot', 'raspberry', 'avocado']
filtered_fruits = filter(lambda fruit: re.match('^a', fruit), fruits)

# convert the new fruits to another list and print it
print(list(filtered_fruits)) # ['apple', 'apricot', 'avocado']
```

In the code above:
- the `filter()` takes the lambda function as the function to execute and the `fruits` list as the iterable
- for the expression of the lambda function, it uses the `re.match()` method of Python RegEx and uses the pattern `^a` on the argument `fruit`
- the last thing I did was convert all items on the list that matches the pattern into a list


### How to use RegEx inside the Expression of a Lambda Function with the `map()` Function
To use RegEx inside a lambda function with another function like `map()`, the syntax is similar:
```py
import re

fruits2 = ['opple', 'bonono', 'cherry', 'dote', 'berry']
modified_fruits = map(lambda fruit: re.sub('o', 'a', fruit), fruits2)

# convert the new fruits to another list and print it
print(list(modified_fruits)) # ['apple', 'banana', 'cherry', 'date', 'berry']
```

In the code above:
- the `modified_fruits` is looping through the `fruits2` list with a `map()` function
- uses the `re.sub()` method of Python RegEx as the expression of the lambda function. 

The `re.sub` method lets you replace the first value with the second one. In the example, it switched all occurrences of `o` to `a`.


### How to use RegEx inside the Expression of a Lambda Function with the `sort()` Method
The last example I will show you uses the `sort()` method of lists:
```py
import re

fruits = [ 'banana', 'fig', 'grapefruit']

# sort fruits based on the number of vowels
fruits.sort(key=lambda x: len(re.findall('[aeiou]', x)))

print(fruits) #['fig', 'banana', 'grapefruit']
```

In the code, the lambda function sorts the list based on the number of vowels. It does it with the combination of the `len()` method, the `findall()` method of Python RegEx, and the pattern `[aeiou]`.

The word fruit with the lowest number of vowels comes first. If you use `reverse=True`, it arranges the fruits based on those with the highest number of vowels – descending order:
```py
import re

fruits = [ 'banana', 'fig', 'grapefruit']

# sort fruits based on the number of vowels
fruits.sort(key=lambda x: len(re.findall('[aeiou]', x)), reverse=True)

print(fruits) # ['grapefruit', 'banana', 'fig']
```


## Conclusion
In this article, we looked at how you can pass in RegEx to a lambda function by showing you examples using the `filter()`, `map()` functions, and the `sort()` method.

I hope this article gives you the knowledge you need to use RegEx inside a lambda function.

Keep coding!


