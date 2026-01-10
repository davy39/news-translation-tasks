---
title: What is UTF-8? UTF-8 Character Encoding Tutorial
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-03T04:01:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-utf-8-character-encoding
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/brett-jordan-M9NVqELEtHU-unsplash--1-.jpg
tags:
- name: HTML
  slug: html
- name: typography
  slug: typography
seo_title: null
seo_desc: 'UTF-8 is a character encoding system. It lets you represent characters
  as ASCII text, while still allowing for international characters, such as Chinese
  characters.

  As of the mid 2020s, UTF-8 is one of the most popular encoding systems.

  To start usin...'
---

UTF-8 is a character encoding system. It lets you represent characters as ASCII text, while still allowing for international characters, such as Chinese characters.

As of the mid 2020s, UTF-8 is one of the most popular encoding systems.

To start using UTF-8, you will want to first familiarize yourself with the the basic ASCII character set.

### What is the ASCII Character Set?

ASCII uses 7-bit code points to represent 128 different characters. These code points are divided into 95 printable characters, which include the 26 letters of the English alphabet (A to Z, both upper- and lower-case), the 10 digits (0 through 9), and a variety of punctuation and other symbols.

There are also 33 non-printable characters, which include control characters like carriage return and line feed, as well as various other characters that are used for things like formatting text.

### UTF-8 VS ASCII – What's the Difference?

UTF-8 extends the ASCII character set to use 8-bit code points, which allows for up to 256 different characters. 

This means that UTF-8 can represent all of the printable ASCII characters, as well as the non-printable characters. 

UTF-8 also includes a variety of additional international characters, such as Chinese characters and Arabic characters.

## How to Use UTF-8 in Your Webpages – HTML UTF-8 Example

And now the easy part. You don't actually need to know how it works (though I'll tell you in a moment.) You can configure UTF-8 Character Encoding in your HTML code with a single line of HTML located in the `<head>` section of your code:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
</html>

```

With that out of the way, let me explain how UTF-8 works, and why it's such a brilliant encoding scheme.

## How UTF-8 Encoding Works, and How Much Storage Each Character Uses

When representing characters in UTF-8, each code point is represented by a sequence of one or more bytes. The number of bytes used depends on the code point being represented by the character. Here's a breakdown of the usage range:

* code points in the ASCII range (0-127) are represented by a single byte
* code points in the range (128-2047) are represented by two bytes
* code points in the range (2048-65535) are represented by three bytes
* and code points in the range (65536-1114111) are represented by four bytes. (This may seem like a lot of possible characters, but keep in mind that in Chinese alone, there are 100,000s of characters.)

The first byte of a UTF-8 sequence is called the "leader byte". The leader byte provides information about how many bytes are in the sequence, and what the code point value of the character is.

The leader byte for a single-byte sequence is always in the range (0-127). The leader byte for a two-byte sequence is in the range (194-223). The leader byte for a three-byte sequence is in the range (224-239). And the leader byte for a four-byte sequence is in the range (240-247).

The remaining bytes in the sequence are called "trailing bytes." The trailing bytes for a two-byte sequence are in the range (128-191). The trailing bytes for a three-byte sequence are in the range (128-191). And the trailing bytes for a four-byte sequence are in the range (128-191).

You can calculate the code point value of a character by looking at the leader byte and the trailing bytes. For a single-byte sequence, the code point value is equal to the value of the leader byte.

For a two-byte sequence, the code point value is equal to ((leader byte - 194) * 64) + (trailing byte - 128).

For a three-byte sequence, the code point value is equal to ((leader byte - 224) * 4096) + ((trailing byte1 - 128) * 64) + (trailing byte2 - 128).

For a four-byte sequence, the code point value is equal to ((leader byte - 240) * 262144) + ((trailing byte1 - 128) * 4096) + ((trailing byte2 - 128) * 64) + (trailing byte3 - 128).

## UTF-8 is a Sound Choice for Encoding

Again, UTF-8 is a super efficient encoding system. It can represent a wide range of characters while still being compatible with ASCII. This makes it a sound choice for use in internationalized software.

I hope you've found this helpful. If you want to learn more about programming and technology, try [freeCodeCamp's core coding curriculum](https://www.freecodecamp.org/learn). It's free.

