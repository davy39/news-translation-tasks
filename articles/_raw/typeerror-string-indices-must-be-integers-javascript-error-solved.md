---
title: TypeError String Indices Must be Integers Python Error [Solved]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-07T23:28:09.000Z'
originalURL: https://freecodecamp.org/news/typeerror-string-indices-must-be-integers-javascript-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pakata-goh-RDolnHtjVCY-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: 'If you try to access values from a dictionary or iterable object using
  the string value instead of the integer value then you will receive the following
  error message:

  TypeError: string indices must be integers

  In this article, I will show you exampl...'
---

If you try to access values from a dictionary or iterable object using the string value instead of the integer value then you will receive the following error message:

```
TypeError: string indices must be integers
```

In this article, I will show you examples of why you might receive this error message and how to fix it.

## How to Access Values from a List in Python

In this example, we have the following list of musical instruments:

```py
instruments = ['flute', 'trumpet', 'oboe', 'percussion', 'guitar']
```

If we wanted to access the third instrument in the list, we would use the numerical index value of 2:

```py
instruments[2]
```

The following line of code would correctly print out the result of `oboe`:

```py
instruments = ['flute', 'trumpet', 'oboe', 'percussion', 'guitar']
print(instruments[2])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-11.41.54-PM.png)

If I tried to access that same list but instead used the string index of `'oboe'`, then it would result in an error message:

```py
instruments = ['flute', 'trumpet', 'oboe', 'percussion', 'guitar']
print(instruments['oboe'])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-11.43.28-PM.png)

If you encounter this error message, double check to make sure you are using the numerical index value to access elements instead of a string value.

## How to Access Values from a Dictionary in Python

Let's modify our earlier example to create a dictionary of instruments and quantities. 

```py
instruments = {
    'flute': 2,
    'trumpet': 5,
    'oboe': 1,
    'percussion': 4,
    'guitar': 9
}
```

If we wanted to print out all of the values from our `instruments` dictionary, then we can use a loop with the `.values()` method.

```py
for quantity in instruments.values():
    print(quantity)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-11.59.57-PM.png)

If we removed the `.values()` method and tried to access the values using string indices, then we would receive the follow error message:

```py
for quantity in instruments:
    print(quantity['flute'])
    print(quantity['trumpet'])
    print(quantity['oboe'])
    print(quantity['percussion'])
    print(quantity['guitar'])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-07-at-12.15.23-AM.png)

If you print out `quantity`, then you will see that it is a string.

```py
for quantity in instruments:
    print(quantity)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-07-at-12.22.50-AM.png)

If you tried to write `quantity['flute']`, then it translates to `'flute'['flute']` which does not make sense in Python. 

The way to resolve this would be to reference our `instruments` dictionary instead of using `quantity`.

The following refactored code would produce the correct results:

```py
instruments = {
    'flute': 2,
    'trumpet': 5,
    'oboe': 1,
    'percussion': 4,
    'guitar': 9
}

print(instruments['flute'])
print(instruments['trumpet'])
print(instruments['oboe'])
print(instruments['percussion'])
print(instruments['guitar'])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-07-at-12.19.21-AM.png)

I hope you enjoyed this article and best of luck on your Python journey. 

