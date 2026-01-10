---
title: String to Char Array Java Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T23:06:14.000Z'
originalURL: https://freecodecamp.org/news/string-to-char-array-java-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/k.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: 'By Thanoshan MV

  In this article, we’ll look at how to convert a string to an array of characters
  in Java. I''ll also briefly explain to you what strings, characters, and arrays
  are.

  What is a Character in Java?

  Characters are primitive datatypes. A ch...'
---

By Thanoshan MV

In this article, we’ll look at how to convert a string to an array of characters in Java. I'll also briefly explain to you what strings, characters, and arrays are.

## What is a Character in Java?

Characters are primitive datatypes. A character is a single character enclosed inside single quotation marks. It can be a letter, a digit, a punctuation mark, a space or something similar. For example:

```java
char firstVowel = 'a';
```

## What is a String in Java?

Strings are objects (reference type). A string is made up of a string of characters. It's anything inside double quotation marks. For example: 

```java
String vowels = "aeiou";
```

## What is an Array in Java?

Arrays are fundamental data structures which can store fixed number of elements of the same data type in Java. For example, let's declare an array of characters: 

```java
char[] vowelArray = {'a', 'e', 'i', 'o', 'u'};
```

Now, we have a basic understanding about what strings, characters, and arrays are. 

## Let's Convert a String to a Character Array

### 1. Use toCharArray() Instance Method

`toCharArray()` is an instance method of the `String` class. It returns a new character array based on the current string object. 

Let's check out an example:

```java
// define a string
String vowels = "aeiou";

// create an array of characters 
char[] vowelArray = vowels.toCharArray();

// print vowelArray
System.out.println(Arrays.toString(vowelArray));
```

Output: `[a, e, i, o, u]`

When we convert a string to an array of characters, the length remains the same. Let's check the length of both `vowels` and `vowelArray` :

```java
System.out.println("Length of \'vowels\' is " + vowels.length());
System.out.println("Length of \'vowelArray\' is " + vowelArray.length);
```

Output: 

```
Length of 'vowels' is 5
Length of 'vowelArray' is 5
```

We can use various ways to print an array. I used the `toString()` static method from the `Arrays` utility class. 

You can read more about the `toCharArray()` instance method in the [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#toCharArray--).

### 2. Use charAt() Instance Method

`charAt()` is an instance method of the `String` class. It returns a character at the specified index of the current string. 

**NOTE:** a string is zero index based, similar to an array. 

Let's see how we can convert a string to an array of characters using `charAt()` :

```java
// define a string
String vowels = "aeiou";

// create an array of characters. Length is vowels' length
char[] vowelArray = new char[vowels.length()];

// loop to iterate each characters in the 'vowels' string
for (int i = 0; i < vowels.length(); i++) {
    // add each character to the character array
    vowelArray[i] = vowels.charAt(i);
}

// print the array
System.out.println(Arrays.toString(vowelArray));
```

Output: `[a, e, i, o, u]`

You can read more about the `charAt()` instance method in the [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#charAt-int-).

I just showed you another way of converting a string to a character array, but we can use the `toCharArray()` method to easily convert instead of creating loops and iterating them. 

Please feel free to let me know if you have any suggestions or questions.

Photo by [Alex Alvarez](https://unsplash.com/@a2_foto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://www.freecodecamp.org/news/s/photos/happy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

**Please support freeCodeCamp in their [Data Science Curriculum Pledge Drive](https://www.freecodecamp.org/news/building-a-data-science-curriculum-with-advanced-math-and-machine-learning/).** 

Connect with me on [Medium](https://mvthanoshan.medium.com/).

Thank you 😇

**Happy Coding ❤️**

### **More on Programming in Java**

1. [Object-Oriented Programming Principles  in Java:  OOP Concepts for Beginners](https://www.freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners/)
2. [Java Array Methods – How to Print an Array in Java](https://www.freecodecamp.org/news/java-array-methods-how-to-print-an-array-in-java/)
3. [Java String to Int – How to Convert a String to an Integer](https://www.freecodecamp.org/news/java-string-to-int-how-to-convert-a-string-to-an-integer/)
4. [Java Random Number Generator – How to Generate Integers With Math Random](https://www.freecodecamp.org/news/generate-random-numbers-java/)

  

