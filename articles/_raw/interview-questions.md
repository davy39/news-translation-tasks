---
title: How to solve a typical interview question on repeating decimals
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-03T12:10:06.000Z'
originalURL: https://freecodecamp.org/news/interview-questions
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/photo-1515879218367-8466d910aaa4.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: interview questions
  slug: interview-questions
seo_title: null
seo_desc: "By Pier Paolo Ippolito\nIntroduction\nIn this article, I will walk you\
  \ through how to solve a typical software development interview question: Repeating\
  \ Decimals. \nIn order to solve this example, I decided to use Python (all the code\
  \ is available here)..."
---

By Pier Paolo Ippolito

## Introduction

In this article, I will walk you through how to solve a typical software development interview question: Repeating Decimals. 

In order to solve this example, I decided to use Python (all the code is available [here](https://github.com/pierpaolo28/Algorithms/tree/master/Interview%20Questions)). If you want, feel free to try to solve this same exercise using any other programming language of your choice.

## The Problem

> Create a function able to take two numbers (the numerator and denominator of a fraction) that returns the results of the fraction in decimal form, enclosing in parenthesis any repeating decimal.

```py
Examples:
1) 1/3 = 0.(3)
2) 1/4 = 0.25
3) 1/5 = 0.2
4) 1/6 = 0.1(6)
5) 1/7 = 0.(142857)
6) 1/8 = 0.125
```

I will now walk you through a simple implementation to solve this problem. If you are able to create a more time and memory efficient solution, feel free to share it in the comment section below.

## The Solution

Let's start by creating a function (_repeating_dec_sol_) and handling some simple exceptions:

1. If the numerator is zero, return zero. 
2. If the denominator is zero, return Undefined (same if both numerator and denominator are equal to zero).
3. If the remainder is zero, (the numerator is divisible by the denominator) return directly the result of the division.
4. If the numerator or denominator return a negative number when divided, add a minus sign at the beginning of the returned result (this will be done at the end of the code).

```py
def repeating_dec_sol(numerator, denominator):
    negative = False
    if denominator == 0:
        return 'Undefined'
    if numerator == 0:
        return '0'
    if numerator*denominator < 0:
        negative = True
    if numerator % denominator == 0:
        return str(numerator/denominator)
    
    num = abs(numerator)
    den = abs(denominator)
```

Now, we can simply store our output for all the digits before the decimal point by concatenating the quotient of the numerator and denominator to a string called _result_ (which will be used later on to store the entire result of the operation).

```py
    result = ""
    result += str(num // den)
    result += "."
```

In order to handle the part after the decimal point, we will now start keeping track of every new numerator and quotient (quantity produced by the division of the two numbers) after the decimal point.

As we can see from the picture below (Figure 1), every-time there is a repeating decimal, same values of the new numerators and the quotients will be repeated multiple times. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/33-1-3-percent-as-a-fraction-math-image-titled-change-a-common-fraction-into-a-decimal-step-8-mathpapa-slope.jpg)
_Figure 1: Repeating Decimals [1]_

In order to model this behaviour in Python, we can start by creating an empty list (_quotient _num_) which we are going to update with all the new numerators and quotients registered after the decimal point (using a list inside a list). 

Every time we are going to append a list containing a new numerator and quotient, we are going to check if are present in any other list the same combination of new numerator and quotient and if that's the case we will then break the execution (this flags us that we have reached a repeating decimal).

```py
    quotient_num = []
    while num:
    	# In case the remainder is equal to zero, there are no repeating
        # decimals. Therefore, we don't need to add any parenthesis and we can
        # break the while loop and return the result.
        remainder = num % den
        if remainder == 0:
            for i in quotient_num:
                result += str(i[-1])
            break
        num = remainder*10
        quotient = num // den

		# If the new numerator and quotient are not already in the list, we
        # append them to the list.
        if [num, quotient] not in quotient_num:
            quotient_num.append([num, quotient])
        # If the new numerator and quotient are instead already in the list, we 
        # break the execution and we prepare to return the final result.
        # We take track of the index position, in order to add the parenthesis 
        # at the output in the right place.
        elif [num, quotient] in quotient_num:
            index = quotient_num.index([num, quotient])
            for i in quotient_num[:index]:
                result += str(i[-1])
            result += "("
            for i in quotient_num[index:]:
                result += str(i[-1])
            result += ")"
            break
```

Finally, we can add the following code to handle the exception in case either the input numerator or denominator are negative numbers.

```py
        if negative:
            result = "-" + result

    return result
```

If we now test our function we will get the following result:

```py
NUM, DEN = 1, 6
print("The result of the fraction", NUM, "/", DEN, "is equal to: ",
       repeating_dec_sol(NUM, DEN))

# Output 
# The result of the fraction 1 / 6 is equal to:  0.1(6)
```

## Conclusion

I hope you enjoyed this article. If you have any questions, feel free to leave a comment below. If you are looking also for a video explanation on how to solve this type of problem, this [video](https://www.youtube.com/watch?v=WFd478BG4o8) by [PyLenin](https://www.youtube.com/channel/UC2HIN53hM4_ZW8IdmWrJGtw) is a great place to start.

## Contact info

If you want to keep updated with my latest articles and projects, [follow me](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) and subscribe to my [mailing list](http://eepurl.com/gwO-Dr?source=post_page---------------------------). These are some of my contacts details:

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Personal Blog](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Personal Website](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Medium Profile](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

## Bibliography

[1] 33 1 3 Percent As A Fraction Math Image Titled Change A Common Fraction Into A Decimal Step 8 Mathpapa Slope - lugezi.com. Accessed at: [http://novine.club/wp-content/uploads//2018/09/33-1-3-percent-as-a-fraction-math-image-titled-change-a-common-fraction-into-a-decimal-step-8-mathpapa-slope.jpg](http://novine.club/wp-content/uploads//2018/09/33-1-3-percent-as-a-fraction-math-image-titled-change-a-common-fraction-into-a-decimal-step-8-mathpapa-slope.jpg)

