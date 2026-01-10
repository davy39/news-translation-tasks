---
title: How Number Systems Work in Java – Decimal, Binary, Octal, and Hexadecimal Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-11T21:54:41.000Z'
originalURL: https://freecodecamp.org/news/number-systems-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/number-systems.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "By Mikael Lassa\nKnowing how to work with numbers is essential in programming.\
  \ Java supports four number systems that are used for various purposes – the decimal,\
  \ binary, octal, and hexadecimal systems. \nUnderstanding what these number systems\
  \ are and..."
---

By Mikael Lassa

Knowing how to work with numbers is essential in programming. Java supports four number systems that are used for various purposes – the decimal, binary, octal, and hexadecimal systems. 

Understanding what these number systems are and when to use them is an important skill for any Java programmer. 

## How the Decimal Number System Works

The decimal number system is the most widely used number system in Java. It's also probably the easiest one to understand, as we commonly use it in everyday life. It is a base-10 system that uses ten digits (0-9) to represent numbers.

In more technical terms, the Oracle Java documentation defines an integer literal as a number represented with a sequence of ASCII digits from 0 to 9. When suffixed with the ASCII character L or l, the number is of type `long`. ([Source: Oracle Java Documentation](https://docs.oracle.com/javase/specs/jls/se12/html/jls-3.html#jls-DecimalIntegerLiteral))

As a refresher, `int` and `long` are two of the primitive data types in Java. An `int` is a 32-bit integer representing values ranging between -2,147,483,648 and 2,147,483,647. A `long` is a 64-bit integer that can hold substantially larger values, namely from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807. 

The use cases of the decimal number system in Java are naturally numerous. It is commonly used in many applications to handle numeric values such as currencies, prices and other financial data, or different types of quantities and measurements (length, time, and so on.). It is also used for most types of arithmetic calculations, as well as for counting and indexing items in arrays or lists. 

Here are some straightforward examples:

```java
int decimalInt = 15;
long decimalLong = 400L;

```

## How the Binary Number System Works

The binary number system is a base-2 system that uses two digits (0 and 1) to represent numbers. Computers are designed to process input in the form of binary numbers, as they can easily represent two states (for example, on/off) and can be combined to perform more complex operations. 

In Java, binary numbers can be used for low-level programming tasks, where there might be a need to operate closer to the inner workings of the machine. 

Binary numbers are also useful for bitwise logical operations, such as `AND`, `OR`, and `NOT`. These operations can be performed quickly and efficiently in a computer's processor using simple digital logic circuits. 

To declare a binary number in Java, you can use the prefix `0b` or `0B` followed by the binary digits. For example:

```java
int binaryInt = 0b1010; 
long binaryLong = 0B1010L;
```

## How the Octal Number System Works

The octal number system is a base-8 system that uses eight digits (0-7) to represent numbers. Octal numbers are perhaps not used as widely as the other systems described in this article, but they do find their distinct areas of application.

In Unix-based operating systems, for instance, file permissions are represented using octal numbers. This means that, when working with file permissions in Java, you may need to use octal numbers to set the permissions of a file.

To declare an octal number in Java, you use the digit `0` as a prefix, followed by the octal digits. For example:

```java
int octalInt = 0273;
long octalLong = 0273L;
```

## How the Hexadecimal Number System Works

The hexadecimal number system is a base-16 system that uses a total of 16 characters, that is ten digits (0-9) and six letters (A-F), to represent numbers. The letters represents the numbers 10 to 15.

The advantages of using the hexadecimal system are apparent whenever you need a more terse and concise way of representing numbers – for instance when dealing with low-level programming tasks. 

Computer memory addresses and color codes are indeed often represented with hexadecimal numbers, as the corresponding binary representations would be considerably harder to read for humans. 

To declare a hexadecimal number in Java, you use `0x` or `0X` as a prefix, followed by the digits. For example:

```java
int hexInt = 0x10e; 
long hexLong = 0XABC1;
```

## How to Convert between Number Systems

There are several reasons why you may need to convert between different number systems. When working with low-level programming, for example, you might need to convert between decimal and binary or hexadecimal numbers to be able to set configurations. 

One common way to translate different number systems into the decimal system is to multiply each digit, starting from the right, by the corresponding power of the base number, which is 2 for binary numbers, 8 for octal numbers, and so on. 

For example, to convert octal numbers to the decimal system, you can calculate the product of each digit, starting from the rightmost digit, to the corresponding power of the number 8. The formula can be represented as follows, where `digit0` is the rightmost digit:

```
(digit0 x 8^0) + (digit1 x 8^1) + (digit2 x 8^2) + ... + (digitn x 8^n) 
```

Based on this formula, the octal number `0273` converts to 187: starting from the right, the digit 3 is multiplied with 8 to the power of 0, then the digit 7 is multiplied with 8 to the power of 1, and so on.

```
  (3 x 8^0) + (7 x 8^1) + (2 x 8^2)
= 3 + 56 + 128
= 187
```

A similar concept applies to hexadecimal numbers, using the base of 16 for the calculation. For example, the hexadecimal number `0xABC1` can be converted to 43969 as follows:

```
 (1 x 16^0) + (C x 16^1) + (B x 16^2) + (A x 16^3) 
= 1 + 192 + 2816 + 40960       
= 43969
```

Java provides methods to convert numbers from one number system to another. These methods are available in the `Integer` and `Long` wrapper classes.

To convert a decimal number to a string representing its binary, octal, or hexadecimal correspondent, you can use the following methods:

```java
int decimalNumber = 165;

String binaryNumber = Integer.toBinaryString(decimalNumber); //10100101
String octalNumber = Integer.toOctalString(decimalNumber);  //245
String hexNumber = Integer.toHexString(decimalNumber);  //a5
```

To perform the opposite conversion, the `parseInt` method has a useful implementation that takes two arguments: the string to be parsed, and the radix, which will be 2 for binary numbers, 8 for octals, and 16 for hexadecimals.

```java
String binaryNumber = "1010";
int decimalFromBinary = Integer.parseInt(binaryNumber, 2);

String octalNumber = "10";
int decimalFromOctal = Integer.parseInt(octalNumber, 8);

String hexNumber = "A";
int decimalFromHex = Integer.parseInt(hexNumber, 16);

```

## Conclusion

This brief guide covered the four number systems supported in Java: decimal, binary, octal, and hexadecimal. It also described some simple ways to declare and convert numbers between different number systems. 

Having an understanding of these concepts is important for any Java programmer, as it allows you to implement a more flexible and efficient manipulation and calculation of data based on the specific project requirements.

If you would like to read any of my other articles, you are welcome to check out my [blog](https://medium.com/@mikael.lassa).


