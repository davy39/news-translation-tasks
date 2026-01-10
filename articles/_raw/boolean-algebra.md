---
title: Boolean Algebra Truth Table Tutorial – XOR, NOR, and Logic Symbols Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T21:31:31.000Z'
originalURL: https://freecodecamp.org/news/boolean-algebra
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b45740569d1a4ca2aca.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Boolean
  slug: boolean
- name: Math
  slug: math
seo_title: null
seo_desc: "By Aditya\nWe all love computers. They can do so many amazing things. Within\
  \ a couple of decades computers have completely revolutionized almost all the aspects\
  \ of human life. \nThey can do tasks of varying degrees of sophistication, all by\
  \ just flippi..."
---

By Aditya

We all love computers. They can do so many amazing things. Within a couple of decades computers have completely revolutionized almost all the aspects of human life. 

They can do tasks of varying degrees of sophistication, all by just flipping zeros and ones. It is remarkable to see how such a simple action can lead to so much complexity.

But I'm sure you all know that such complexity cannot be achieved (practically) by just randomly flipping the numbers. There is indeed some reasoning behind it. There are rules that govern the way this should be done. In this article we will discuss those rules and we will see how they govern the way computers "think".

## What is Boolean Algebra?

The rules I mentioned above are described by a field of Mathematics called Boolean Algebra. 

In his 1854 book, British Mathematician George Boole proposed a systematic set of rules for manipulation of Truth Values. These rules gave a mathematical foundation for dealing with logical propositions. These sets of foundations led to the development of Boolean Algebra. 

To best understand Boolean Algebra, we first have to understand the similarities and differences between Boolean Algebra and other forms of Algebra. 

Algebra, in general, deals with the study of mathematical symbols and the operations that can be performed on these symbols.

These symbols do not have a meaning of their own. They represent some other quantity. It is this quantity that gives some value to these symbols and it is this quantity on which the operations are actually being performed. 

Boolean Algebra also deals with symbols and the rules that govern the operations on these symbols but the difference lies in _what these symbols represent_. 

In case of ordinary Algebra, the symbols represent the Real numbers whereas in Boolean Algebra they represent the Truth values.

The image below shows the entire set of Real numbers. The set of Real numbers includes Natural numbers(1, 2, 3, 4....), Whole numbers (all the Natural numbers and 0), Integers (.....-2, -1, 0, 1, 2, 3 ...) and so on. Ordinary Algebra deals with this entire set of numbers. 

![Image](https://www.freecodecamp.org/news/content/images/2024/08/numbersys.png)

The Truth values, in comparison, consist of a set of only two values: False and True. Here, I would like to point out the fact that we can use any other symbol to represent these values. 

For example in Computer Science we mostly represent these values using 0 and 1. 0 is used for False and 1 for True. 

You can also do it in more fancy ways by representing truth values with some other symbols such as Cats and Dogs or Bananas and Oranges. 

The point here is that the internal meaning of these symbols will remain the same irrespective of the symbol you use. But make sure that you don't change the symbols while performing the operations. 

Now the question is that if (True and False), (0 and 1) are just the representations, then what is it that they are trying to represent? 

The underlying meaning behind truth values comes from field of Logic where truth values are used to tell if a proposition is "True" or "False". Here the truth values represent the _relation of a proposition to truth,_ that is, whether  the proposition is true or false.

A proposition is just a statement like "All cats are cute."

If the above proposition is true then we assign it the truth value of "True" or "1" otherwise we assign it "False" or "0".

In Digital Electronics, truth values are used to represent the "On" and "Off" states of electronic circuits. We will discuss more about that later in this article. 

## Boolean Operations and Truth Tables

Just like Ordinary Algebra, Boolean Algebra also has operations which can be applied on the values to get some results. Although these operations are not similar to ones in ordinary algebra because, as we discussed earlier, Boolean algebra works on Truth values rather than Real Numbers.

### Boolean Algebra has three basic operations.

**OR**: Also known as _Disjunction_. This operation is performed on two Boolean variables. The output of the OR operation will be 0 when both of the operands are 0, otherwise it will be 1. 

To get a clearer picture of what this operation does we can visualize it with the help of a **Truth Table** below.

```
Truth tables give us an insightful representation of what the Boolean operations do and they also act as a handy tool for performing Boolean operations.

		OR Operation

Variable-1	Variable-2	Output
  0		0		0
  0		1		1
  1		0		1
  1		1		1
```

**AND**: Also known as _Conjunction_. This operation is performed on two Boolean variables. The output of AND operations will be 1 when both operands are 1, otherwise it will be 0. The truth table representation is as follows.

```
		AND Operation

Variable-1	Variable-2	Output
  0		0		0
  0		1		0
  1		0		0
  1		1		1
```

**NOT**: Also known as _Negation_. This operation is performed only on one variable. If the value of the variable is 1 then this operation simply converts it into 0 and if the value of the variable is 0, then it converts it into 1.

```
	Not Operation

Variable-1	Output
  0		1	
  1		0			
```

## Boolean Algebra and Digital Circuits

After its initial development, Boolean Algebra, for a very long time, remained one of those concepts in Mathematics which did not have any significant practical applications. 

In the 1930s, Claude Shannon, an American Mathematician, realised that Boolean Algebra could be used in circuits where the binary variables could represent the "low" and "high" voltage signals or "on" and "off" states.

This simple idea of making circuits with the help of Boolean Algebra led to the development of Digital Electronics which contributed heavily in the development of circuits for computers. 

Digital Circuits implement Boolean Algebra with the help of Logic Gates. Logic Gates are the circuits which represent a boolean operation. For example an OR gate will represent an OR operation. The same goes for NOT and AND gates as well. 

Alongside the basic logic gates we also have logic gates that can be created using the combination of the basic logic gates. 

**NAND**: NAND gate is formed by a combination of the NOT and AND gates. NAND gate gives an output of 0 if both inputs are 1, otherwise 1. 

NAND gate holds the property of Functional Completeness, which means that any boolean function can be implemented just by using a combination of NAND gates only.

```
		NAND Gate

Variable-1	Variable-2	Output
  0		0		1
  0		1		1
  1		0		1
  1		1		0
```

**NOR**: NOR gate is formed by a combination of NOT and OR gates. NOR gate gives an output of 1 if both inputs are 0, otherwise 0. 

NOR gate, just like NAND gate, holds the property of Functional Completeness, which means that any boolean function can be implemented just by using a combination of NOR gates only. 

```
		NOR Gate

Variable-1	Variable-2	Output
  0		0		1
  0		1		0
  1		0		0
  1		1		0
```

Most digital circuits are built using NAND or NOR gates because of their functional completeness property and also because they are easy to fabricate. 

Other than the above mentioned gates we also have some special kind of gates which serve some specific purpose. These are as follows:

**XOR**: XOR gate or Exclusive-OR gate is a special type of logic gate which gives 0 as output if both of the inputs are either 0 or 1, otherwise it gives 1. 

```
		XOR Gate

Variable-1	Variable-2	Output
  0		0		0
  0		1		1
  1		0		1
  1		1		0
```

**XNOR**: XNOR gate or Exclusive-NOR gate is a special type of logic gate which gives 1 as output when both the inputs are either 0 or 1, otherwise it gives 0.

```
		XNOR Gate

Variable-1	Variable-2	Output
  0		0		1
  0		1		0
  1		0		0
  1		1		1
```

## Conclusion

So, with all that we can now conclude our discussion on Boolean Algebra here. I hope by now you have a decent picture of what Boolean Algebra is all about. 

This is definitely not all you need to know about Boolean Algebra. Boolean Algebra has a lot of concepts and details that we were not able to discuss in this article. 

