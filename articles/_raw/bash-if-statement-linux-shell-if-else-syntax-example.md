---
title: Bash If Statement – Linux Shell If-Else Syntax Example
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-11-14T15:37:54.000Z'
originalURL: https://freecodecamp.org/news/bash-if-statement-linux-shell-if-else-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Copy-of-Copy-of-read-write-files-python--4-.png
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'When coding, you might need to make decisions based on certain conditions.
  Conditions are expressions that evaluate to a boolean expression (true or false).

  Statements that help to execute different code branches based on certain conditions
  are known...'
---

When coding, you might need to make decisions based on certain conditions. Conditions are expressions that evaluate to a boolean expression (`true` or `false`).

Statements that help to execute different code branches based on certain conditions are known as conditional statements.

`if...else` is one of the most commonly used conditional statements. Like other programming languages, Bash scripting also supports `if...else` statements. And we will study that in detail in this blog post.

## Syntax of `if` Statements

You can use `if` statements in a variety of ways. The generic structure of `if` statements is as follows:

* Using an `if` statement only: `if...then...fi` 
* Using and `if` with an `else` statement: `if...then...else...fi` statements
* Using multiple `else` statements with `if`: `if..elif..else..fi`

## 

## How to Use the `if` Statement

When you are using a single `if` statement, the syntax is as follows:

```bash
if [ condition ]
then
	statement
fi
```

> Note that the spaces are part of the syntax and should not be removed.

Let's go through an example where we are comparing two numbers to find if the first number is the smaller one.

```bash
#! /bin/sh

a=5
b=30

if [ $a -lt $b ]
then
        echo "a is less than b"
fi
```

If you run the above snippet, the condition `if [ $a -lt $b ]` evaluates to `True` , and the statement inside the if statement executes

**Output:**

```bash
a is less than b
```

## How to Use the `if .. else` Statement

When you are using an `if` statement and you want to add another condition, the syntax is as follows:

```bash
if [ condition ]
then
	statement
else
	do this by default
fi
```

Let's see an example where we want to find if the first number is greater or smaller than the second one. Here, `if [ $a -lt $b ]` evaluates to false, which causes the `else` part of the code to run. 

```bash
#! /bin/sh

a=99
b=45

if [ $a -lt $b ]
then
        echo "a is less than b"
else
        echo "a is greater than b"
fi
```

**Output:**

```bash
a is greater than b
```

## How to Use `if..elif..else` Statements

Let's say you want to add further conditions and comparisons to make the code dynamic. In this case, the syntax would look like this:

```bash
if [ condition ]
then
	statement
elif [ condition ] 
then
	statement 
else
	do this by default
fi
```

To create meaningful comparisons, we can use AND `-a` and OR `-o` as well.

In this example, we will determine the type of triangle using these conditions:

* `Scalene`:  A triangle where every side is different in length.
* `Isosceles`: A triangle where 2 sides are equal.
* `Equilateral`: A triangle where all sides are equal.

```bash
read a
read b
read c

if [ $a == $b -a $b == $c -a $a == $c ]
then
echo EQUILATERAL

elif [ $a == $b -o $b == $c -o $a == $c ]
then
echo ISOSCELES
else
echo SCALENE

fi
```

In the example above, the script would ask the user to enter the three sides of the triangle. Next, it would compare the sides and decide the triangle type.

```
3
4
5
SCALENE
```

## Conclusion

You can easily branch your code based on conditions like `if..else` and make the code more dynamic. In this tutorial, you learned the syntax of `if...else` along with some examples.  

I hope you found this tutorial helpful.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

