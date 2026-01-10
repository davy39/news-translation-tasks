---
title: Python Round to Int – How to Round Up or Round Down to the Nearest Whole Number
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-24T16:52:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-round-numbers-up-or-down-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/volkan-olmez-aG-pvyMsbis-unsplash-1.jpg
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: "When working with float values (numbers with decimal values) in our Python\
  \ program, we might want to round them up or down, or to the nearest whole number.\
  \ \nIn this article, we'll see some built-in functionalities that let us round numbers\
  \ in Python...."
---

When working with float values (numbers with decimal values) in our Python program, we might want to round them up or down, or to the nearest whole number. 

In this article, we'll see some built-in functionalities that let us round numbers in Python. And we'll see how to use them with some examples.

We'll start with the `round()` function. By default, it rounds a number to the nearest whole number. We'll also see how to use the function's parameters to change the type of result returned to us. 

We'll then talk about the `math.ceil()` and `math.floor()` methods which rounds up and rounds down a number to the nearest whole number/integer respectively. These two methods are from the built-in `math` module in Python.

## How to Use the `round()` Function to Round to the Nearest Whole Number

The `round()` function takes in two parameters. Here's what the syntax looks like:

```txt
round(number, decimal_digits)
```

The first parameter – `number` – is the number we are rounding to the nearest whole number.

The second parameter – `decimal_digits` – is the number of decimals to be returned. The default value is 0. 

Let's see some examples. 

```python
x = 2.56789

print(round(x))
# 3

```

In our first example, we're using only one parameter – the number to be rounded, which is `2.56789`. 

When we passed in the number variable to the `round()` function, it got rounded to the nearest whole number which is 3. 

That's how easy it is to use!

Now, let's work with the second parameter. 

```python
x = 2.56789

print(round(x, 2))
# 2.57
```

The code above is similar to the last example except for the second parameter.  We passed in a value of two. This will round the number to the nearest hundredth (two decimal places). 

In our case, 2.57 was returned. That is, 2.56789 to 2.57.

Let's see one last example to fully understand how the second parameter works. 

```python
x = 2.56789

print(round(x, 3))
# 2.568

```

Now, we've made the second parameter 3. We'll get the number rounded to the nearest thousandth (three decimal places). 

The initial number – 2.56789 – was rounded to 2.568. 

## How to Use the `math.ceil()` Method to Round Up a Number to the Nearest Whole Number

The `math.ceil()` method simple takes in the number to be rounded up as its parameter. Here's what the syntax looks like:

```txt
math.ceil(number)
```

Here's an example:

```python
import math

x = 5.57468465

print(math.ceil(x))
# 6

```

In the code above, you'll notice that we first imported the `math` module: `import math`. This give us access to all the methods provided by the module. 

We created an `x` variable which has 5.57468465 as its value. 

In order to round this number up to the nearest whole number, we passed in the number (in the `x` variable) to the `math.ceil()` method: `math.ceil(x)`.

The resulting value from this operation, as can be seen in the code above, is 6.

## How to Use the `math.floor()` Method to Round Down a Number to the Nearest Whole Number

Just like we did in the last section, in order to use the `math.floor()` method, we must first import the `math` module. 

Here's the syntax for `math.floor()` method:

```txt
math.floor(number)
```

Let's see an example. 

```python
import math

x = 5.57468465

print(math.floor(x))
# 5
```

As expected, we passed in the number to be rounded down to the `math.floor()` method: `math.floor(x)`. The `x` variable has the number 5.57468465 stored in it. 

This number got rounded down to 5. 

## Conclusion

In this article, we talked about three built-in functionalities in Python that let us round numbers. 

The `round()` function rounds a number to the nearest whole number. 

The `math.ceil()` method rounds a number up to the nearest whole number while the `math.floor()` method rounds a number down to the nearest whole number. These two methods are both accessible through the `math` module. 

With the examples given in each section, we were able to see how to use each functionality to obtain our desired result.

Happy coding!

