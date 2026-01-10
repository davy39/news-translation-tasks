---
title: Infix Expressions VS Postfix Expressions, and How to Build a Better JavaScript
  Calculator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-05T03:40:19.000Z'
originalURL: https://freecodecamp.org/news/zipline-build-a-smart-javascript-calculator-65e21a8b0b0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6YO8587U_vTxqVw-OUiqsA.png
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Pramod Sripada

  If you want to make your Simple Calculator a lot smarter, this post is for you.

  You might asking, “What’s wrong with my simple calculator.” Well, it may do all
  the operations correctly, but the sequence in which it does them is prob...'
---

By Pramod Sripada

If you want to make your Simple Calculator a lot smarter, this post is for you.

You might asking, “What’s wrong with my simple calculator.” Well, it may do all the operations correctly, but the sequence in which it does them is probably wrong.

The simple calculator contains just four operations: addition, subtraction, division and multiplication. Many of us might have studied in high school about the precedence of operators: division and multiplication have the same priority, and have higher priority than addition and subtraction, which have the same priority.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R9O-cK8n4URxuGQPV1Sdfw.png)
_“Please excuse my Dear Aunt Sally” is a common mnemonic for remembering the order of operations (image credit: [oneyearlease.org](http://www.oneyearlease.org/" rel="noopener" target="_blank" title="))_

A quick recap of operator precedence can be found here: [http://www.math.utah.edu/online/1010/precedence/](http://www.math.utah.edu/online/1010/precedence/).

The reason I am stressing operator precedence is because a simple calculator performs most of the calculations wrong. For example, 1+2x3 should be equal to 7 according to a normal calculator, but the simple calculator gives a result of 9.

The reason simple calculator does it all wrong is because it just multiplies the two operands, with the operator between them, and produces the result.

We just can’t blame the simple calculator. After all, it was meant to be simple. So now you might start thinking on how to rearrange the operators, so as to get the correct result. Yes, you are on the right track. For that, we need to know about two more concepts in computer science: Infix expressions and Postfix expressions.

In simple words, the arithmetic expressions that we understand are Infix expressions and the arithmetic expression that the computer understands are Postfix expressions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uB6KUeJDoLWyLUt244Cqsw.png)

Both the infix and postfix expressions create the same results. It’s just humans are used to solving infix expressions, and computers are used to solving postfix expressions.

Another key feature in the postfix expression is that it contains operators succeeding the operands according to precedence, which makes it easy for the computer to evaluate them using stacks, and produce the correct result.

By now you must be thinking about how to convert the infix expression entered by your user into a postfix expression. There is an algorithm that converts an infix expression into a postfix expression that can be found [**_here_**](http://csis.pace.edu/~wolf/CS122/infix-postfix.htm).

Here’s what this process looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*oNj492e1yJgzrFqFS74CYg.png)
_Infix to Postfix conversion_

The postfix expression should be evaluated by an algorithm, which can be found [**_here_**](http://scriptasylum.com/tutorials/infix_postfix/algorithms/postfix-evaluation/). It is similar to the evaluation done by a simple calculator, except that the operators succeed the operands in postfix expressions.

Eventually, the primary motive of converting an infix expression into a postfix expression is to preserve the precedence of the operators while the computer evaluates the expression.

Check out my fully functional calculator that incorporates these principles [**_here_**](http://codepen.io/pramodvspk/full/RWzxgK/)**_._**

