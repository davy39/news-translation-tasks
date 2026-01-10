---
title: Python lower() – How to Lowercase a Python String with the tolower Function
  Equivalent
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2022-11-03T16:16:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-lowercase-python-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-pixabay-278881.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'A string is a datatype that consists of characters wrapped in quotation
  marks. These characters can be letters, symbols, or numbers.

  In Python, there are different ways of working with strings. These methods are built-in
  functions that change the res...'
---

A string is a datatype that consists of characters wrapped in quotation marks. These characters can be letters, symbols, or numbers.

In Python, there are different ways of working with strings. These methods are built-in functions that change the results of the string.

For instance, if I want to print out my name with its first letter capitalized, I use the `.title()` method to capitalize the first letter.

In this article, we will learn how to convert uppercase letters to lowercase letters without using the built-in method.

## How to Convert a String to Lowercase using `.lower()`

Strings can consist of different characters – one of those characters being letters of the alphabet. You can write the English alphabet as uppercase or lowercase letters. When changing a string to lowercase, it only applies to the letters.

In Python, there is a built-in method that can change a string that is in uppercase to lowercase. It also applies to strings that have letters both in uppercase and lowercase. The “.lower() “ method changes the strings to lowercase.

```python
name = "BOB STONE"
print(name.lower()) # >> bob stone
name1 = "Ruby Roundhouse"
print(name1.lower()) # >> ruby roundhouse
name2 = "joHN Wick"
print(name2.lower()) # >> john wick
name3 = "charlieNew"
print(name3.lower()) # >> charlienew
```

We can see in the above code block that the variables that store each string have uppercase letters. Then with the `.lower()` method, it converts those letters to lowercase.

## Other Ways to Convert a Python String to Lowercase

Apart from the inbuilt method “.lower()”, there are different ways of converting uppercase letters to lowercase letters in Python. In this article, we will look at two different ways.

There are two ways of accessing letters:

* copying them manually into a list or
    
* making use of Unicode standard
    

### How to Access Letters from a List

The idea is to loop through a list of letters and replace the uppercase letters in a string with lowercase letters.

First, create a variable that stores an input that accepts a string with uppercase letters.

Then, create another variable that stores a list of uppercase letters and lowercase letters.

Last, create the final variable that stores an empty string, which is where the lowercase letters will be stored.

```python
word = str(input("Enter a word: ” ))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowercase_letters = ''
```

In the list above, we see that it has lowercase letters and uppercase letters. There are 26 letters in the English alphabet, but the index in a list starts from 0, so the count of the alphabet is 51 (for both upper and lowercase letters).

We can also see that the lowercase letters are written first (left side), and the uppercase letters are written second (right side). The indexes of the lowercase letters range from 0 - 25, while the indexes of the upper case letters ranges from 26 - 51.

Next, we loop through each character in the string.

```python
for char in word:
```

`<char>` is the new variable name that stores all the characters from the `<word>` variable.

There are two cases of strings we are going to convert. The first case is the strings with only uppercase letters and the second has strings with special symbols, numerals, some lowercase, and some uppercase letters.

**CASE I**: strings with uppercase only

To convert the uppercase letters to lowercase, we have to find the index of each letter stored by the variable `<char>` from the list. To find an index we use the ".index()" method:

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
word = str(input("Enter a word: " ))
for char in word:
    print(alphabet.index(char))

# Results
# Enter a word: GIRL
# 32
# 34
# 43
# 37
```

In the above code, the indexes of the letters in the "GIRL" are printed.

In the list, the lowercase letters have indexes from 0-25 and uppercase letters have indexes from 26 - 51. When setting the condition ("if" statement) we start checking if the index of the letter is greater than '25' because the first uppercase index starts from '26' .

To get the corresponding lowercase letters, we substract 26 from each uppercase index. When we get the indexes of the lowercase numbers, we use indexing (variable\_name\[index\_number\]) to find the corresponding letters. The lowercase letters are now added to the variable name &lt;lower\_case\_letters&gt; that stores an empty string.

We return the variable &lt;lowercase\_letters&gt; by printing it outside the loop.

```python
for char in word:
      if alphabet.index(char) > 25:
          lowercase_letters += alphabet[alphabet.index(char)-26]
  print(lowercase_letters)
```

This is what the code looks like when we bring it all together:

```python
def change_to_lowercase(word):
    
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lowercase_letters = ''
  
  for char in word:
      if alphabet.index(char) > 25:
          lowercase_letters += alphabet[alphabet.index(char)-26]
      
  return lowercase_letters

word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Results
# Enter a word: FERE
# fere
# Enter a word: PYTHONISFUN
# pythonisfun
```

**CASE II**: strings with special symbols, numerals, lowercase letters alongside uppercase letters.

Before converting the uppercase letters to lowercase, there are some conditions we need to check. The conditions will check if each character `<char>` from the word:

* is not a letter
    
* has both uppercase and lowercase letters in the word. If some letters in the word are lowercase, they will be left unchanged.
    

After these checks, it assumes the remaining characters are uppercase letters.

To check if a character is not a letter, we use the “not in” keyword. To check if a character is lowercase, we find the index and compare it to the last count of the lowercase letters in the list.

Again, lowercase letters have indexes from 0-25, and the index of the last lowercase letter is 25. These characters are added to the variable name &lt;lower\_case\_letters&gt; that stores an empty string.

```python
for char in word:
    if char not in alphabet or alphabet.index(char)<=25:
        lowercase_letters += char
```

In the above code block, we used the `.index()` method to find the position of letters in the alphabet.

For the remaining characters that we assume are uppercase letters, in the list of letters, the indexes of those letters are from 26 - 51. To find their corresponding lowercase letter indexes, we subtract by 26, and use the `.index()` method to find the letter.

Indexing = variable\_name\[index\_number\]. We add the final result to the variable storing the empty string.

```python
for char in word:
    if char not in alphabet or alphabet.index(char)<=25:
        lowercase_letters += char
    else:
        lowercase_letters += alphabet[alphabet.index(char)-26]
```

Then we print lowercase\_letters outside the loop:

```python
for char in word:
    if char not in alphabet or alphabet.index(char)<=25:
        lowercase_letters += char
    else:
        lowercase_letters += alphabet[alphabet.index(char)-26]
print(lowercase_letters)
```

This is what the code looks like when we bring it all together:

```python
def change_to_lowercase(word):
    
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lowercase_letters = ''
  
  for char in word:
      if char not in alphabet or alphabet.index(char)<=25:
          lowercase_letters += char
      else:
          lowercase_letters += alphabet[alphabet.index(char)-26]
  return lowercase_letters

word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Results
# Enter a word: 2022BlackADAM&&
# 2022blackadam&&
# Enter a word: Weasle2@3568QQQAJHGB
# weasle2@3568qqqajhgb
```

## How to Access Letters using the Unicode Standard

Unicode means universal character encoding standard. According to unicode.org,

> "Unicode standard provides a unique number for every character, no matter what platform, device, application or language."

In simple terms, all letters from different languages have a unique number representing every character present in Unicode.

We use two methods when working with Unicode in Python: `ord()` and `chr()`.

* ord(): this function accepts characters (letters in any language) and returns the unique number under the Unicode standard.
    
* chr(): this function accepts integers and returns the character equivalent under the Unicode standard.
    

Before diving into the code explanation, here is a chart containing all the unique numbers for the English alphabet, both lowercase and uppercase letters.

![Image](https://lh5.googleusercontent.com/BaC12Gudvtl2Wu1uAaFqqNudQKHi0mwoF5H2JT_GtrELW-sPK5IzoybnhL426kPy_4XXas-7MU3PVsmzNQJEJZqoWrq-xhApaoYFZjBuDnA5ugnJFaoBaCb2EcvAVDV5tHJyS2wbi5Wp2Iw8Gka5YWYjVTPVkxbMIwM0Uc86Ude9YNf2FQjxq4xBgQ align="left")

[*ASCII Chart representing the unique numbers of english alphabets*](https://linuxhint.com/understanding-ascii-table/)

Now that we are familiar with what Unicode is and how to access the values in Python, let’s dive in.

First, create a variable that stores an input that accepts a string with uppercase letters.

Then, create the final variable that stores an empty string, which is where the lowercase letters will be stored.

```python
word = str(input("Enter a word: ” ))
lowercase_letters = ''
```

Then we loop through each character in the string.

```python
for char in word:
```

`<char>` is the new variable name that stores all the characters from the `<word>` variable.

**CASE I**: strings containing uppercase letters only.

Before converting the uppercase letters to lowercase, we need to check if each character from the word is in uppercase.

According to the Unicode chart, the capital letter A has the number “65”, and the capital letter Z has the number “90”. We check if each character `<char>` in `<word>` has numbers between 65 and 90. If they do, they are uppercase letters.

```python
print((ord('A')))
# RESULT
# 65
print((ord('Z')))
# RESULT
# 90
print((ord('F')))
# RESULT
# 70
```

The `ord()` function returns the unique number of each letter in uppercase.

To convert uppercase letters to lowercase letters, we add the difference between both cases, “32”, to each number from the uppercase to get the lower case letters.

For example:

```python
number_for_A = ord('A')
number_for_a = ord('a')
difference_a = number_for_a - number_for_A
print("Differences in letters" , difference_a)
print("The unique number for A", number_for_A)
print("The unique number for a", number_for_a)

 # Results
# The unique number for A 65
# The unique number for a 97
# Differences in letters 32

number_for_F = ord('F')
number_for_f = ord('f')
difference_f = number_for_f - number_for_F
print("The unique number for F", number_for_F)
print("The unique number for f", number_for_f)
print("Differences in letters" , difference_f)
# Results
# The unique number for F 70
# The unique number for f 102
# Differences in letters 32
```

In the above code, ‘a” is 97 on the unicode chart and ‘A’ is 65. The difference between them is 32. If we want to get the value of “a” on the chart, we add 32 to the value of A “65” and get “97”.

So to convert to lowercase, we have to add 32 to each of the numbers of the uppercase letters to get their corresponding lowercase letters.

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char) + 32
    print(char)
# Results
# Enter a word: REAL
# 114
# 101
# 97
# 108
```

In the above code, we loop through the variable `<word>` to get access to each character.

Then we check if each character in the variable `<word>` has a unique number between 65 and 90. If it does, it consists of uppercase letters.

To get the corresponding lowercase letters, we add 32. The result above prints the unique numbers of lowercase letters.

We can match the numbers with their letters by using the `chr()` function.

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char) + 32
        to_letters = chr(char)
    print(to_letters) 
    
    
# Result
# Enter a word: REAL
# r
# e
# a
# l
```

Now we see that the letters returned are in lowercase. To get the letters in one line, we add it to the variable that stores the empty string and return the variable.

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char) + 32
        to_letters = chr(char)
        lowercase_letters += to_letters
print(lowercase_letters)
# Result
# Enter a word: FERE
# fere
```

Here's what it looks like when we bring it all together:

```python
def change_to_lowercase(word):
    lowercase_letters = ''
    for char in word:
        if ord(char) >= 65 and ord(char) <= 90:
            char = ord(char)+32
            to_letters = chr(char)
            lowercase_letters += to_letters
    return lowercase_letters
word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Results
# Enter a word: HARDWORKPAYS
# hardworkpays
# Enter a word: PYTHONISFUN
# pythonisfun
```

**CASE II:** strings with special symbols, numerals, lowercase alongside uppercase letters.

For strings that have non-letters and some lowercase letters, we add an 'else' statement to return the values as they appear in the string. The uppercase letters are then converted to lowercase:

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char)+32
        to_letters = chr(char)
        lowercase_letters += to_letters
    else:
        lowercase_letters += char
print(lowercase_letters)

# Result
# Enter a word: @#&YEAERS09=
# @#&yeaers09=
```

Here's what it looks like when we bring it all together:

```python
def change_to_lowercase(word):
    lowercase_letters = ''
    for char in word:
        if ord(char) >= 65 and ord(char) <= 90:
            char = ord(char)+32
            to_letters = chr(char)
            lowercase_letters += to_letters
        else:
            lowercase_letters += char
    return lowercase_letters
word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Enter a word: YOUGOT#$^
# yougot#$
# Enter a word: BuLLettrAIn@2022
# bullettrain@2022
```

I know the second method is a lot take in but it also gets you the result, just as the first method does.

## Summary

In this article, you've learnt about how to convert characters and strings from one case to another. We also took a look at the ASCII table.

The second method is more efficient and straightforward once you know how to use the two important functions. The indexes of the letters are built-in in Python, so there's no need to memorize them.

Thank you for reading!
