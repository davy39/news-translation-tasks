---
title: Python Coding Challenges For Beginner Developers – Code and Explanations
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2024-06-04T20:18:55.000Z'
originalURL: https://freecodecamp.org/news/python-coding-challenges-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/pexels-pixabay-139392.jpg
tags:
- name: coding challenge
  slug: coding-challenge
- name: Python
  slug: python
seo_title: null
seo_desc: 'Learning Python can be challenging, especially if you''re not actually
  writing enough code. As a beginner, you may go through lessons and tutorials without
  practicing on your own – and this makes it harder to learn the language.

  The truth is, you cann...'
---

Learning Python can be challenging, especially if you're not actually writing enough code. As a beginner, you may go through lessons and tutorials without practicing on your own – and this makes it harder to learn the language.

The truth is, you cannot truly learn programming without writing code. It is through this process that you learn new things and discover how small errors, like missing a quote or space, can frustrate you for hours.

No course can teach you the intricacies of Python the way finding and solving errors does.

That's why coding challenges are important if you are starting your coding journey. They help you implement your knowledge in practice and boost your confidence.

So to help you start coding more, here are eight Python challenges you can try as a beginner. 

**And here's a tip**: really try to solve the challenge on your own after reading through the question/prompt. If you get stuck, then you can look at the code below and the explanation to help you figure it out.

## Here Are the Challenges:

1. [Python Challenge #1: Check if a List is Sorted](#heading-python-challenge-1-check-if-a-list-is-sorted)
2. [Python Challenge #2: Convert Binary number to decimal](#heading-python-challenge-2-convert-binary-numbers-to-decimal)
3. [Python Challenge #3: Loves Me, Loves Me Not](#heading-python-challenge-3-loves-me-loves-me-not)
4. [Python Challenge #4: The Tribonacci Sequence Challenge](#heading-python-challenge-4-the-tribonacci-sequence-challenge)
5. [Python Challenge #5: Hide a Credit Card Number](#heading-python-challenge-5-hide-a-credit-card-number)
6. [Python Challenge #6: SpongeCase](#heading-python-challenge-6-spongecase)
7. [Python Challenge #7: Caesar Encryption](#heading-python-challenge-7-caesar-encryption)
8. [Python Challenge #8: Is the Product Divisible by the Sum?](#heading-python-challenge-8-is-the-product-divisible-by-the-sum)

All of these challenges help you in enhancing your problem-solving and algorithmic thinking skills. You'll also gain experience with writing and testing code to ensure correctness and efficiency.

## Python Challenge #1: Check if a List is Sorted

The challenge: Write a function that checks whether a given list of numbers is sorted in either ascending or descending order.

Here's the code solution:

```python
def is_sorted(lst):
    asc, desc = True, True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            asc = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            desc = False
    return asc or desc
```

### Code explanation:

In the above code, we define a function `is_sorted` that takes in a `list` as a parameter. We initialize two booleans, `asc` (for ascending) and `desc` (for descending) to `True`. 

We then iterate through the list. If the `i`th element of the list is greater than the `(i+1)`th element, the `asc` flag is set to `False`, indicating that the list is not sorted in ascending order.

Then we iterate through the list again. If the `i`th element of the list is smaller than the `i+1` th element, the `desc` flag is set to `False`, indicating that the list is not sorted in descending order.

If any element is found to be greater than the next element, the `asc` flag is set to `False`. Within the loop, we check to see if the `i`th element of the list is greater than the `i+1` th element. 

```python
for i in range(len(lst) - 1):
    if lst[i] < lst[i + 1]:
        desc = False
```

We return `True` if either `asc` or `desc` is `True`. This means that the list is sorted, either in ascending or descending order.

## Python Challenge #2: Convert Binary Numbers to Decimal

The challenge: Write a function that converts a binary number to its decimal equivalent.

Here's the code solution:

```python
def binary_to_decimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
```

### Code explanation:

In the above code, we define a function `binary_to_decimal` that takes a `binary` number as a parameter. We then initialized the variables `decimal` and `i` to `0`.

The variable `decimal` is used to store the resulting decimal value and the variable `i` represents the current position when processing a binary number, starting from `0`.

We loop through each binary digit until all digits of the binary number become `0`.

```python
while binary != 0:
```

Now, we extract the least significant digit of the current binary number using the modulus operator.

```python
dec = binary % 10
```

And then we convert the extracted digit to its decimal equivalent by multiplying it by 2 power raised to `i`.

```python
decimal = decimal + dec * pow(2, i)
```

Then we remove the processed digit:

```python
Binary = binary // 10
```

And increment the position `i` to process the next binary digit:

```python
i += 1
```

Finally, we return the calculated decimal value.

## Python Challenge #3: Loves Me, Loves Me Not

The challenge: Given an integer n, print a string that alternates between the phrases "Loves me" and "Loves me not" for each number from 1 to n.

The sequence should start with "Loves me" and alternate accordingly.

Here's the code solution:

```python
def phrase_loves_me_not(n):
    phrases = []
    for i in range(1,n+1):
        if i % 2 != 0:
            phrases.append("Loves me")
        else:
            phrases.append("Loves me not")
    return ", ".join(phrases)
```

### Code explanation:

We define a function `phrase_loves_me_not` that takes a single parameter `n`.

Then, we initialize an empty list, `phrases`, which stores the result for each number from `1` to `n`.

We iterate from `1` to `n` inclusive:

```python
for i in range(1, n+1):
```

We then check for odd indices. If the number is odd, we append “Loves me” to the list ‘phrases’.

```python
if i % 2 != 0:
    phrases.append("Loves me")
```

For even indices, we append “Loves me not” in the list ‘phrases’.

```python
else:
    phrases.append("Loves me not")
```

We then use the `join` method to concatenate all the elements in the ‘phrases’ list into a single string and return that string.

Finally we return the resulting string.

```python
return ", ".join(phrases)

```

## Python Challenge #4: The Tribonacci Sequence Challenge

The "Tribonacci sequence" challenge is a twist on the famous Fibonacci sequence, where each number is the sum of the preceding three numbers.

For example, 0, 1, 1, 2, 4, 7 …

The challenge: Write a function that returns the nth number in the Tribonacci sequence.

Here's the code solution:

```python
def find_nth_tribonacci(n):
    # Base cases for n = 0, 1, 2
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    # Initialize the first three terms of the Tribonacci sequence
    a, b, c = 0, 1, 1
    for i in range(3, n + 1):
        next_term = a + b + c
        a, b, c = b, c, next_term
    return c
```

### Code explanation:

First, we define a function named `find_nth_tribonacci` which takes a number `n` as a parameter.

We then define base cases as:

* If `n` is `0`, the function returns `0`.
* If `n` is `1` or `2`, the function returns `1`.

Note_:_ These conditions handle the starting values of the Tribonacci sequence.

We then initialize the first three values of the Tribonacci sequence, from `n` = `0` to `n` = `2`.

```python
a, b, c = 0, 1, 1
```

Then, we iterate from `3` to the number `n`, where we calculate the next term by summing the three preceding terms (`a`, `b`, and `c`). We also update the values of `a`, `b`, and `c` to the next set of three terms in the sequence.

```python
for i in range(3, n + 1):
    next_term = a + b + c
    a, b, c = b, c, next_term
```

At the end of the loop, `c` holds the value of the nth term in the Tribonacci sequence, so we return `c`.

```python
return c
```

## Python Challenge #5: Hide a Credit Card Number

Write a function that takes a credit card number and transforms it into a string where all digits except the last four are replaced with asterisks.

Here's the code solution:

```python
def mask_credit_card(card_number):
    card=str(card_number)
    return "*"*(len(card) - 4) + (card[-4:])
```

### Code explanation:

We define a function `mask_credit_card` that takes `card_number` as a parameter.

First, we convert the number into a string.

```python
card = str(card_number)
```

Then to mask the card_number, we generate a string of asterisks with a length equal to the total number of digits in the credit card minus four. This masks all digits except the last four digits.

```python
"*"*(len(card) - 4)
```

Then, we use the slice operation to retrieve the last four digits of the credit card number.

```python
card[-4:]
```

Finally, we return the concatenated result of the asterisk string and the last four digits of the card number.

```python
return "*"*(len(card) - 4) + card[-4:]
```

## Python Challenge #6: SpongeCase

SpongeCase is a style of text where letters alternately appear in lower and upper case. For example, the word in spongeCase would be sPoNgEcAsE.

The challenge: Write a function that converts the given string into spongcase.

Here's the code solution:

```python
def to_spongecase(text):
    result = []
    i = 0
    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                result.append(char.lower())
            else:
                result.append(char.upper())
            i += 1
        else:
            result.append(char)
           
    return "".join(result)

```

### Code explanation:

We define a function `to_spongecase` that takes a string `text` as a parameter.

Then we initialize an empty list result, and counter `i` to `0`.  
  
We iterate the function over each character char in the input string and check if the current character is alphabetic. 

```python
for char in text:
    if char.isalpha():
```

If the character at index `i` (adjusted for only alphabetic characters) is even, we append the result with the character converted to lowercase.

```python
if i % 2 == 0:
    result.append(char.lower())
```

If the index is odd, we append the result with the character converted to uppercase.

```python
else:
    result.append(char.upper())
```

After processing an alphabetic character, the index `i` is incremented.

In case of non-alphabetic characters, append them to the result list as they appear, without alternating their case.

After all characters have been processed, we combine them back into a string using `join` .

```python
return "".join(result)

```

## Python Challenge #7: Caesar Encryption

Caesar Encryption (also known as the Caesar Cipher) is a simple encryption technique that works by shifting the letters in the plaintext message by a certain number of positions.

The challenge: Create a function that has two parameters – a string to be encoded and an integer representing the number of positions each letter should be shifted.

Here's the code solution:

```python
def caesar_encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

```

### Code explanation:

We define a function `caesar_encryption` that takes two parameters: a string `text` and an integer `shift`.

Then we initialize an empty string to accumulate the encoded characters.

```python
result = ""
```

Next, we loop through each character in the input string text.

For alphabetic characters, we calculate the new character after applying the shift.

Then we add the non-alphabetic characters like numbers to the result unchanged.

```python
for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
    shifted = (ord(char) - start + shift) % 26 + start
```

So how do we calculate the new character?

We determine the ASCII value of 'A' for uppercase or 'a' for lowercase letters.

First, convert the character to its ASCII code, normalize to a 0-25 range by subtracting the start and adding the shift, and then wrap it around using modulo 26 to ensure it stays within alphabet bounds.

Finally, we add the start back to map it to the correct ASCII range.

Convert the shifted value back to a character using `chr()` and add to the result.

```python
result += chr(shifted)
```

After all characters are processed, return the encoded string.

```python
return result
```

## Python Challenge #8: Is the Product Divisible by the Sum?

The challenge: Create a function that takes a list of integers and returns whether the product of those integers is divisible by their sum or not.

The function should return `True` if the product of all the integers in the list is divisible by their sum and `False` otherwise.

Here's the code solution:

```python
def is_product_divisible_by_sum(numbers):
    if not numbers:
        return False
    
    product = 1
    summation = 0
    for num in numbers:
        product *= num
        summation += num

    if summation == 0:
        return False

    return product % summation == 0

```

### Code explanation:

First, we define a function `is_product_divisible_by_sum`, which takes a list of integers, `numbers`, as a parameter.

Then, we check if the input list `numbers` is empty. If it is empty, return `False`.

```python
if not numbers:
    return False
```

Else, initialize two variables: `product` to `1` and `summation` to `0`.

```python
product = 1
summation = 0
```

Iterate over each number in the list to calculate the total product and sum of all numbers in the list.

```python
for num in numbers:
    product *= num
    summation += num
```

After calculating the sum, check if the sum is zero. Dividing by zero is undefined in mathematics and would raise an error in programming, so return `False`.

```python
if summation == 0:
    return False
```

Finally, check if the product is divisible by the sum using the modulus operator `%`.

Here, if the remainder is zero, that is the product is perfectly divisible by the sum, return `True`. Otherwise, return `False`.

```python
return product % summation == 0
```

## Wrapping Up

These are just a few challenges that can help you build your problem-solving skills. I would suggest you try these challenges on your own.

If you want to solve more challenges, you can try out the following platforms:

* [Leetcode](https://leetcode.com/)
* [Programiz PRO Community Challenges](https://app.programiz.pro/community-challenges)
* Exercism

They are free and help you build your logical skills with hands-on experience.

Happy Coding!


