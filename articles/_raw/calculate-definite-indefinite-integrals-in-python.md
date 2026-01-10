---
title: How to Calculate Definite and Indefinite Integrals in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-31T18:02:27.000Z'
originalURL: https://freecodecamp.org/news/calculate-definite-indefinite-integrals-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/calculating-integrals-python-1.png
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: "By Roy Chng\nPython is a versatile programming language that offers libraries\
  \ and tools for scientific computing and mathematical calculations. \nMany essential\
  \ mathematical operations frequently involve definite and indefinite integrals.\
  \ In this artic..."
---

By Roy Chng

Python is a versatile programming language that offers libraries and tools for scientific computing and mathematical calculations. 

Many essential mathematical operations frequently involve definite and indefinite integrals. In this article, we will explore how to perform these calculations using Python.

## How to Calculate Single Variable Definite Integrals

### Install SciPy

Before we start, we need to install the SciPy module. It provides a collection of Mathematical algorithms and functions that we'll use.

You can do this by running the following command in a terminal:

```
pip install scipy
```

To calculate single variable definite integrals, we need to first import `quad` from `scipy.integrate`. It is a general purpose function used to calculate single variable definite integrals.

```python
from scipy.integrate import quad
```

### Elementary Functions

From there, we'll need to define the integrand as a function in Python.

For example, if we wanted to calculate the integral of x-squared, we would define the integrand as a Python function like so:

```python
def integrand(x):
	return x**2
```

Once we define the integrand, we can calculate the definite integral using the quad function like this:

```python
print(quad(integrand, 0, 1))
# (0.33333333333333337, 3.700743415417189e-15)

```

In the above code, `0` represents the lower limit of integration and `1` represents the upper limit of integration. They can be any other number.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_1-4.png)
_Result of the of integral of x^2 from 0 to 1 with the associated code_

In this example, we calculate that the estimated result of the integral from 0 to 1 of x-squared is approximately 0.333 with an absolute error of roughly 3.7e-15.

The quad function returns a tuple of an estimation of the definite integral followed by the absolute error of the estimation.

What the `quad` function does is essentially evaluate the `integrand` function at multiple different values between our limits of integration to be able to calculate an estimate of the integral.

Another example would be if I wanted to calculate the integral of `(x+1)/x**2`. We would first define it as a function in Python, and pass it into the `quad` function along with the limits of integration:

```python
from scipy.integrate import quad

def integrand(x):
	return(x+1)/x**2
    
print(quad(integrand, 1, 2))
# (1.1931471805599452, 1.3246594716242401e-14)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_2-3.png)
_Result of the of integral of (x+1)/x^2 from 1 to 2 with the associated code_

In this example, we calculate that the estimated result of the integral from 1 to 2 of x +1 all over x-squared is approximately 1.19 with an absolute error of roughly 1.32e-14.

### Other Common Functions

If we wanted to use common mathematical functions such as `sin(x)` or `log(x)`, we can use another Python package for scientific computing – NumPy. You can install the package using the following command:

```
pip install numpy
```

By importing it, we have access to these common functions which we can use in our integrand:

```python
from scipy.integrate import quad
from numpy import log, sin

def integrand(x):
	return log(sin(x))
    
print(quad(integrand, 0, 2))
# (-1.1022223889049558, 1.2237126744196256e-15)


```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_3-2.png)
_Result of the of integral of log(sin(x)) from 0 to 2 with the associated code_

In this example, we calculate that the estimated result of the integral from 0 to 2 of log(sin(x)) is approximately -1.10 with an absolute error of roughly 1.22e-15.

A full list of mathematical functions that NumPy provides is [in their documentation](https://numpy.org/doc/stable/reference/routines.math.html).

### How to Use Constants

NumPy also provides useful constants such as `e` and `pi`, as well as `inf`. It's a floating point representation of positive infinity. We can use it to calculate a definite integral that converges.

```python
from scipy.integrate import quad
from numpy import inf, exp

def integrand(x):
  return exp(-x)
    
print(quad(integrand, 0, inf))
# (1.0000000000000002, 5.842606742906004e-11)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_4-4.png)
_Result of the of integral of e^x from 0 to infinity with the associated code_

In this example, we calculate that the estimated result of the integral of e raised to the negative x from 0 to infinity is approximately 1.00 with an absolute error of roughly 5.84e-11.

## How to Calculate Multi-Variable Integrals

### Double Integrals

To calculate double integrals, we need to import the `dblquad` function from `scipy.integrate`:

```
from scipy.integrate import dblquad
```

We define the integrand in a similar way to definite it with one variable, only this time we specified two arguments instead.

```python
def integrand(y, x):
	return x*y**2
```

We can then calculate the definite integral using the `dblquad` function given by `scipy`.

Note that the integrand is a function that needs to accept `y` as the first parameter and `x` as the second parameter.

```python
print(dblquad(integrand, 0, 1, 2, 4))
# (9.333333333333334, 2.0679162295394134e-13)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_5-2.png)
_Result of the integral of (xy^2) dxdy from 2 to 4 for y and integral from 0 to 1 for x with the associated code_

In this example, we calculate that the estimated result of the double integral x times y-squared from x = 0 to 1 and from y = 2 to y = 4 is approximately 9.33 with an absolute error of roughly 2.07e-13.

The function requires us to pass in the integrand, and the lower and upper limits of integration for `x`, followed by the lower and upper limits of integration for `y`.

### Variable Limits

To calculate integrals with variable limits, we'll need to define functions for the lower and upper limits of integration for y in terms of x:

```python
def upper_limit_y(x):
	return x**2
    
def lower_limit_y(x):
	return x
    
def integrand(y, x):
	return x+y
  
print(dblquad(integrand, 0, 2, lower_limit_y, upper_limit_y))
```

In this example, we calculate that the estimated result of the double integral of x+y from x = 0 to x = 2, and from y = x to y = x^2 is approximately 3.2 with an absolute error of roughly 1.10e-13.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/indefinite_integral_example_3-1.png)
_Result of the double integral (x+y) dydx from 0 to 2 for x and integral from x to x^2 for y with the associated code_

### Triple Integrals

To calculate triple integrals, we can use the `tplquad` function:

```python
from scipy.integrate import tplquad

def integrand(z, y, x):
	return z*(x+y+z)
    
print(tplquad(integrand, 0, 1, 4, 5, 0, 1))
# (2.8333333333333335, 3.6983326566167174e-14)

```

The function requires us to pass in similar arguments, being the upper and lower limits of integration in `x`, `y` and `z`.

In this example, we calculate that the estimated result of the triple integral of z multiplied by (x+y+z) from x = 0 to x = 1, y = 4 to y = 5, and z = 0 to z = 1 is approximately 2.83 with an absolute error of 3.70e-14:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_6-1.png)
_Result of the triple integral z(x+y+z) dxdydz from 0 to 1 for x, 4 to 5 for y and 0 to 1 for z with the associated code_

## How to Evaluate Single Variable Indefinite Integrals

To calculate single variable indefinite integrals with Python, we need to use the SymPy library. It's used for symbolic computation and involves exact computation using variables. To install it, install the SymPy module:

```
pip install sympy
```

Once it has been installed, we can import the `Symbol` and `integrate` methods from `sympy`:

```python
from sympy import Symbol, integrate
```

We first need to define the variables used in the integrand:

```python
x = Symbol('x')

```

After that, we can integrate the function using the `integrate` method that SymPy provides. It expects two arguments: the first is the integrand, and the second is the variable we are integrating with respect to.

For example, if we wanted to integrate x-squared with respect to `x`, we can define the integrand in Python as `x**2`:

```python
print(integrate(x**2, x))
# (x**3)/3
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/indefinite_integral_example_1-3.png)
_Result of the indefinite integral of x^2_

In this example, we calculate the integral of x-squared which is x-cubed over 3.

**Note that SymPy doesn't add the constant of integration, but it is implied.**

SymPy also provides other common functions such as `sin(x)` and `exp(x)` that we can use.

Before using them, we first need to import it from `sympy`:

```python
from sympy import Symbol, integrate, sin
```

Using the imported `sin` function, we can then evaluate the integral of `sin(x)`.

```python
x = Symbol('x')
print(integrate(sin(x), x))
# -cos(x)
```

In this example, we calculate the integral of sin(x) which is -cos(x):

![Image](https://www.freecodecamp.org/news/content/images/2023/07/indefinite_integral_example_2-1.png)
_Result of the indefinite integral of sin(x)_

Sympy provides the full list of mathematical functions you can use [in their documentation](https://docs.sympy.org/latest/modules/functions/elementary.html)

## Summary

In this tutorial, we went over the basics of how to calculate both definite and indefinite integrals in Python. We also looked at how to calculate integrals of elementary functions, ones that involved common mathematical functions, as well as using constants.

We made use of popular Python libraries for scientific comptutation and went over examples of calculating integrals.

If you enjoy my writing, consider subscribing to [my YouTube channel](https://www.youtube.com/@turbinethree).

Happy Coding!

## 




