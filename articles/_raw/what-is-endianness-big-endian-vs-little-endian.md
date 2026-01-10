---
title: What is Endianness? Big-Endian vs Little-Endian Explained with Examples
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-02-01T23:23:58.000Z'
originalURL: https://freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Endianness.png
tags:
- name: binary
  slug: binary
- name: Computer Science
  slug: computer-science
seo_title: null
seo_desc: 'Computers only understand binary. This means that 0''s and 1''s make up
  the language computers work with.

  One bit is one 0 or 1. 8 bits make up a byte. From these simple pieces we can build
  incredibly complex connected computer systems to render videos...'
---

Computers only understand binary. This means that `0`'s and `1`'s make up the language computers work with.

One bit is one `0` or `1`. 8 bits make up a **byte**. From these simple pieces we can build incredibly complex connected computer systems to render videos, show text from around the world, and compute extremely complex algorithms.

Some data (some English characters like a, e, i, o and u) can be represented by one byte, but some pieces of data take multiple bytes to be represented.

But **endianness** is a fundamental part of how computers read and understand bytes.

## What is Endianness?

Different languages read their text in different orders. English reads from left to right, for example, while Arabic is read right to left.

This is exactly what **endianness** is for computers.

If my computer reads **bytes** from left to right, and your computer reads from right to left, we're going to have issues when we need to communicate.

**Endianness** means that the bytes in computer memory are read in a certain order. 

We won't have any issues if we never need to share information. Each computer is internally consistent for their own data. It's just the internet has enabled us to share more data than we ever have before, and our data is not always **read** in the same order.

**Endianness** is represented two ways **Big-endian** (**BE**) and **Little-endian** (**LE**). 

* **BE** stores the **big-end** first. When reading multiple bytes the first byte (or the lowest memory address) is the biggest - so it makes the most sense to people who read left to right.
* **LE** stores the **little-end** first. When reading multiple bytes the first byte (or the lowest memory address) is the littlest -  so it makes most sense to people who read right to left.

If the above doesn't make sense, that's ok – let's look at an example.

## Example of How Endianness Works

Let's take a number that we have to use multiple bytes to represent, and show the big-endian and little-endian ways it can be represented.

We'll take a number that requires three bytes to be represented in binary.

This may slightly oversimplify it, but I hope it serves as a helpful visual explanation.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Decimal-number_--1-.png)
_A binary example where big-endian and little-endian numbers are arranged in the order they would be read._

The 0b at the beginning is just notation to let readers know it's binary. So we know the difference between binary `1100` and 1,100 as the decimal number (one thousand, one hundred). I also used colours to hopefully make it clearer.

I just want to be clear that _bit ordering_ is fine. There is no difference between the ordering of **bits**. But there is a difference in the correct ordering of **bytes**. I hope the above demonstrates the order of the `0`'s and `1`'s within a byte don't change. But the **byte** ordering does change.

If we only ever had to send one **byte** too, there'd be no issues (there aren't multiple ways to order only 1 thing). It's only an issue with a sequence of more than one **byte.**

## Most Significant Byte (MSbyte)

The terminology **Most Significant Byte** is a common way to describe **endianness** so I want to make sure I cover it thoroughly.

Before we begin explaining with **bits** and **bytes**, let's just do it with a decimal number.

If I took the decimal number 2,984, what number could you change to change the number by the smallest amount? The 4. If I change the 4 to 5, the whole number only goes up by 1.

But let's say you change the 2 in 2,984. It will change the number significantly and go up by a thousand.

This is the exact same with **bytes** and **bits**.

We refer to the **byte** holding the smallest position as the **Least Significant Byte** (**LSbyte**) and the **bit** holding the smallest position as the **Least Significant Bit** (**LSbit**).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/MSbyte.png)
_A diagram to illustrate that the byte containing the lowest position numbers is the least significant byte._

The byte that holds the most significant position is referred to as the **Most Significant Byte** (**MSbyte**) and the bit holding the most significant bit position is the **Most Significant Bit** (**MSbit**).

Now knowing this new definition, we can define **BE** and **LE** as:

* Big endian stores data **MSbyte** first
* Little endian stores data **MSbyte** last

## When might this be an issue?

Endianness has to be a consideration in computing in a few different cases.

For example Unicode characters (the character set used to render characters on your phone, PC, TV, everywhere!) have to pass a special character byte sequence (U+FEFF BYTE ORDER MARK) called the **Byte Order Mark** or **BOM**. The **BOM** serves a few purposes.

The **BOM** makes the system aware:

* That the incoming stream is Unicode.
* Of which Unicode character encoding is used.
* Of the **endian** order of the incoming stream.

Some programming languages even expect you to detail what byte order sequence is being used. So one program may use, send, and receive numbers in **BE** or **LE** depending on what you want. Swift is one example of this (the language used to do iOS development).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-206.png)
_The Apple documentation detailing how to get the little-endian representation of an Integer._

You can read some Swift code [here](https://gist.github.com/vukcevich/fa793c8bcb55b14b6e0a0700f5f7316b) for an example of byte swapping to get little and big-endian representations of `Integer`s too.

## Why is this even an issue in the first place?

It just happens that different protocols emerged and then later had to interact with one another. **BE** is the dominant order in any network protocols, and is referred to as **network order**, for example. On the other hand, most PC's are **little-endian**. 

You can run a C++ code snippet online [here](http://cpp.sh/524wi) to see what endian your machine is (mine is **little-endian**).

**Endianness** has largely ceased to matter with higher level languages and abstracting away particular pieces of implementation details we don't need to worry about.

Another part of it is processors decide whether they are little-endian or big-endian (or can handle both - called **Bi-endian**) so consumer choice has driven part of what we consider "normal" in our computer systems.

## Conclusion

I hope this article has explained what endianness is, what big-endian and little-endian are, and that you understand these concepts more clearly now.

I share my writing on [Twitter](https://twitter.com/kealanparr) if you enjoyed this article and want to see more.

