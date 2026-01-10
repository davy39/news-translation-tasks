---
title: The Hexadecimal Number System Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-09T23:13:00.000Z'
originalURL: https://freecodecamp.org/news/hexadecimal-number-system
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/malte-bickel-rGYdVCMQBCY-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Hexadecimal numbers, often shortened to “hex numbers” or “hex”, are numbers
  represented in base 16 as opposed to base 10 that we use for everyday arithmetic
  and counting.

  In practical terms, this means that each column of a number written in hexadeci...'
---

Hexadecimal numbers, often shortened to “hex numbers” or “hex”, are numbers represented in base 16 as opposed to base 10 that we use for everyday arithmetic and counting.

In practical terms, this means that each column of a number written in hexadecimal can represent up to 16 values.

Digits in hexadecimal use the standard symbols 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 to represent the corresponding value, and use the first six letters of the alphabet to represent the values 10 through 15 (E.G: A, B, C, D, E, F).

In programming, we prefix hexadecimal constants with `0x`, with some exceptions.

### **Examples and explanation**

```text
0x1        ==        1
0xF        ==        15
0xFF       ==        255
0xFFF      ==        4095
0x1000     ==        4096
```

In the standard base 10 system, each column represents increasing powers of 10, while in base 16 each column represents increasing powers of 16.

As seen in the table example above, with one hex digit we can represent numbers up to and including 15. Add another column and we can represent numbers up to 255, 4095 with another column, and so on.

## **Uses of Hexadecimal in Low Level Programming**

Hexadecimal first found its use in Computer Science as a convenience feature.

Data in our computers has a lowest common storage unit, the Byte. Each byte contains 8 bits, and is able to store a number between 0 and 255 inclusive.

Hexadecimal has the advantage of being terse and having well defined boundaries.

A single byte is always represented by two hexadecimal digits from 0x00 to 0xFF, the latter being the largest per-byte value of 255.

The terseness and byte-aligned nature of hexadecimal numbers make them a popular choice for software engineers working on low-level code-bases or embedded software.

## **Uses of Hexadecimal Numbers in JavaScript**

JavaScript supports the use of hexadecimal notation in place of any integer, but not decimals.

As an example, the number 2514 in hex is 0x9D2, but there is no language-supported way of representing 25.14 as a hex number.

Using hexadecimal in your code is a personal and stylistic choice, and has no effect on the underlying logic your code implements.

## **Uses of Hexadecimal Numbers in CSS**

CSS has for a long time used hexadecimal notation to represent color values. Consider the following selector:

```css
.my-container {
    background-color: #112233;
    color: #FFFFFF;
}
```

The `background-color`’s value is in fact three hex bytes.

The CSS processor treats these as three individual bytes, representing Red, Green, and Blue.

In our example, 11 corresponds to the Red color component, 22 corresponds to the Green color component, and 33 to the Blue color component.

There is currently no way as of CSS3 to define a color with an alpha component using hex. The proposed CSS4 Draft<sup>1</sup> includes a proposal to allow for an extra byte to specify alpha values.

For now, use of the standard `rgba()` function is the recommended way to add an alpha value to your colors.

