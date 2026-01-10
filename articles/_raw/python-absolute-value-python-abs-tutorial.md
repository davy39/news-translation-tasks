---
title: Python Absolute Value – Python abs Tutorial
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-06-20T15:55:24.000Z'
originalURL: https://freecodecamp.org/news/python-absolute-value-python-abs-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/markus-krisetya-Vkp9wg-VAsQ-unsplash.jpg
tags:
- name: Math
  slug: math
- name: MathJax
  slug: mathjax
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you will learn all about the abs() function in Python.

  You will learn what the abs() function does and why you may want to use it.

  You will also understand how to use abs() with the help of practical examples.

  Here is what we will co...'
---

In this article, you will learn all about the `abs()` function in Python.

You will learn what the `abs()` function does and why you may want to use it.

You will also understand how to use `abs()` with the help of practical examples.

Here is what we will cover:

1. [ What is the `abs()` function in Python?](#intro)
    1. [Why are absolute values important?](#absolute-values)
    2. [How to use the `abs()` function in Python? A syntax breakdown](#usage)
2. [How to use the `abs()` function with examples](#examples)
    1. [How to use the `abs()` function with an integer argument](#integer)
    2. [How to use the `abs()` function with a floating-point number argument](#float)
    3. [How to use the `abs()` function with a complex number argument](#complex)

## What is The `abs()` Function in Python? <a name="intro"></a>

The `abs()` built-in Python function returns the absolute value of a number.

But what is an absolute value of a number in the first place?

In mathematics, the absolute value of a number refers to that number's distance from zero.

Essentially, it is how far away that number is from zero on the number line.

For example, the absolute value of the number five is five since the distance from zero to five is five units.

![Screenshot-2022-06-14-at-9.51.34-AM](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-14-at-9.51.34-AM.png)

Something to take note of is that the absolute value will always be a **positive value**. So, when it comes to calculating the absolute value of a negative number, the result will always be the positive version of that number.

For example, the absolute value of negative five is also five:

![Screenshot-2022-06-14-at-10.01.18-AM](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-14-at-10.01.18-AM.png)

### Why Are Absolute Values Important? <a name="absolute-values"></a>

Absolute values are an important concept and are commonly used in Math and Physics.

There may be times when you only need to use positive numbers and will not need to make use of any negative ones. In fact, you may need to make sure there are no negative numbers whatsoever for the calculations you are about to perform.

You will most likely use absolute values for calculating the distance of one point to another.

Some other common real-world examples could be:

- Calculating the difference between two points.
- Calculating the amount of energy used.
- Calculating the temperature, time, and speed differences between two points.

### How to Use the `abs()` Function in Python? A Syntax Breakdown for Beginners <a name="usage"></a>

The general syntax for the `abs()` function looks something like this:

```python
abs(number)
```

Let's break it down:

- The `abs()` function takes only one single argument, which is **required**.
- The argument is always a number which can have a negative or positive value.
- The number can either be:
    - An integer, such as `4`, `-15`, or `10`.
    - A floating-point number, such as `4.1`, `-15.06`, or `2.13`.
    - A complex number. A complex number is made up of two parts - a **real** part which consists of a real number such as `1` or `4`, and an **imaginary** part. In Python, the imaginary part is created by adding the letter `j` as a suffix – not the letter `i` like it is in Mathematics. You add `j` to the end of a real number, like so: `1j` or `4j`.So, an example of a complex number in Python is `2 + 4j` or `1 + 2j`.

Now, when it comes to the return value of the `abs()` function:

- For **integer numbers**, the `abs()` function returns the absolute value of the given number.
- For **floating point numbers**, the `abs()` function returns the absolute value of the given number.
- For **complex numbers**, the `abs()` function returns the magnitude of the given number.

## How to Use the `abs()` Function with Examples <a name="examples"></a>

In the following sections, you will see the `abs()` function in action and how it behaves when it has an integer, a floating-point number, and a complex number as an argument.

### How to Use the `abs()` Function with an Integer Argument <a name="integer"></a>

When you pass an integer as an argument, the `abs()` function will return its absolute value.

Below is an example of passing a positive integer as an argument:

```python
my_number = 7

abs_value = abs(my_number)

print(abs_value)

#output 

#7 
```

And below is an example of passing a negative integer as an argument. 

Remember that the absolute value will always be positive:

```python
my_number = -17

abs_value = abs(my_number)

print(abs_value)

#output

#17
```


### How to Use the `abs()` Function with a Floating-Point Number Argument <a name="float"></a>

When you pass a floating-point number as an argument, the `abs()` function will return its absolute value.

The following examples work in the same way as the examples from the previous section.

Here is a positive floating-point number as an argument:

```python
my_number = 34.05

abs_value = abs(my_number)

print(abs_value)

#output

#34.05
```

And here is a negative floating-point number as an argument:

```python
my_number = -43.2

abs_value = abs(my_number)

print(abs_value)

#output

#43.2
```

### How to Use the `abs()` Function with a Complex Number Argument <a name="complex"></a>

Complex numbers work differently from integers and floats.

When a complex number is passed as an argument to the `abs()` function, the return value is the magnitude of that number.

The magnitude of a complex number, such as `a+bj`, is the number's distance between the origin (0,0) and the point (a,b) in the complex plane. And the magnitude of a complex number is calculated with the help of the Pythagorean theorem, \\(\sqrt{a^2 + b^2}\\)

So, let's take the complex number `3 + 4j` for example. You would need to calculate the square root of the squares of the numbers from the real part (`3`) and the imaginary part `4`: \\(\sqrt{3^2 + 4^2} = 5\\)

In Python, this is how you would use a complex number with the `abs()` function:

```python
my_number = 3 + 4j

abs_value = abs(my_number)

print(abs_value)

#output

#5.0
```

## Conclusion

And there you have it – you now know the basics of how the `abs()` Python function works!

I hope you found this article helpful.

To learn more about the Python programming language, check out freeCodeCamp's [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thank you so much for reading and happy coding :)

