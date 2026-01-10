---
title: How to Use Your Linux Terminal as a Calculator – Mathematical Expression Solver
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-12-15T17:40:54.000Z'
originalURL: https://freecodecamp.org/news/solve-your-math-equation-on-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/FreeCodeCamp---Evaluate-expression-on-Terminal.png
tags:
- name: Linux
  slug: linux
- name: Math
  slug: math
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'Can you solve the below math expression on your own without using any device?
  Take as much time as you need – but no tools allowed:

  ( ( 11 + 97 ) + ( 2 * 63 ) - ( 7 / 93 ) * ( 8 - 25 ) / ( 9 * 64 ) ) * ( ( 64 / 34
  ) + ( 94 - 20 ) - ( 23 + 98 ) * ( 19...'
---

Can you solve the below math expression on your own without using any device? Take as much time as you need – but no tools allowed:

```bash
( ( 11 + 97 ) + ( 2 * 63 ) - ( 7 / 93 ) * ( 8 - 25 ) / ( 9 * 64 ) ) * ( ( 64 / 34 ) + ( 94 - 20 ) - ( 23 + 98 ) * ( 199 * 928 ) / ( 92 * 26 ) ) * ( ( ( 2 * 1 ) / 2 ) - 1 )
```

Kudos to you if you solved it on your own. I'm sure you'll be angry with me, though, after discovering that the result of this long expression just evaluated to zero. 

So what if you used your browser to find the answer? How long would that take?

Searching this expression on Google took less than a second to get the answer (using a 500MBPS connection) along with 5,21,00,000 results. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-25.png)
_Search results by Google for the given expression_

Yahoo gave us the answer in less than 500 ms along with 1,480,000,000 search results. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-26.png)
_Search results by Yahoo for the given expression_

Bing didn't even return anything.

But my terminal and system calculator were almost instant in finding the answer (took < 10 ms). 

Using the terminal is one of the quickest ways to evaluate a mathematical expression. But many developers are unaware that you can solve mathematical expressions using your terminal. 

In this article, you'll learn how to solve math problems in the Linux terminal. 

## How to Evaluate a Mathematical Expression in the Linux Terminal

You can use the `expr` command to evaluate mathematical expression in your terminal. Basic mathematical operations such as addition, subtraction, multiplication, division and modulus all work using the `expr` command. 

Let's have a quick look at each of these operations:

```bash
expr 12 + 8   # Addition

expr 20 - 10  # Subtraction

expr 5 \* 2   # Multiplication

expr 8 \/ 4   # Division

expr 5 \% 3   # Modulus
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-64.png)
_Using the `expr` terminal command to find answers to arithmetic operations_

Running each of those commands in the terminal evaluates and returns the answer of that expression (as you can verify in the attached screenshot). 

You might be thinking, "Why is there a backward slash (\) for the last 3 operations (Multiplication, Division, and Modulus)?"

A backward slash in programming is basically used to escape characters. Let's take the example of the Multiplication symbol (*). "*" is used in regular expressions which basically means to include all files and folders. 

Here's a quick example:

```bash
cp ./* ../backup/
```

Running the above command will copy all the files and folders in the current directory to the backup directory. 

Similarly, each symbol has their own meaning. Using a backward slash (\) will escape its regular usage pattern. This is the reason that most symbols are prefixed with a backward slash. 

But, you may wonder, is this all this command can do? 

The answer is no. I've shared a sample of the expressions, but we could use any others and get the results in a fraction of a second. 

## How to Evaluate a Logical Expression in the Terminal

In addition to finding the results of a mathematical expression, you can use this command to evaluate a logical expression. 

Logical expressions containing <, <=, >, >=, =, != can be evaluated with this command. 

Let's have a quick look at how it works:

```bash
expr 2 \< 1

expr 29320 \> 23820

expr 29320 \>= 29320

expr 29320 \< 29320

expr 29320 \<= 29320

expr 293202 \= 293203

expr 293202 \!= 293203
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-65.png)
_Evaluate logical expressions with `expr` command_

The command returns "1" if the expression evaluates to true and "0" if it evaluates to false. 

From the above commands you can notice that all the logical operators are escaped with a backward slash (\). 

## What Do the Special Logical Operators Do? 

I read your mind. You're thinking, "I know about logical operators. What are the special logical operators?". 

Well, the special logical operators are:

* AND (&)
* OR (|)

From a programming perspective, the AND operator evaluates to true if both sides of the operator evaluates to true. The OR operator evaluates to true if either of the sides evaluates to true. 

Here's the table for your reference. Some people may be familiar with `1` and `0`. For those people, replace FALSE with `0` and TRUE with `1`. 

<table>
    <tr>
    	<td>X</td>
    	<td>Y</td>
    	<td>X OR Y</td>
    	<td>X AND Y</td>
    </tr>
	<tr>
        <td>FALSE</td>
        <td>FALSE</td>
        <td>FALSE</td>
        <td>FALSE</td>
	</tr>
	<tr>
        <td>FALSE</td>
        <td>TRUE</td>
        <td>TRUE</td>
        <td>FALSE</td>
	</tr>
	<tr>
        <td>TRUE</td>
        <td>FALSE</td>
        <td>TRUE</td>
        <td>FALSE</td>
	</tr>
	<tr>
        <td>TRUE</td>
        <td>TRUE</td>
        <td>TRUE</td>
        <td>TRUE</td>
	</tr>
</table>

But they have a completely different usage with the `expr` command. Let's have a quick look at it. 

The `expr` command works similar to the above table. But there's an exception for a particular case. This command will never return `1` if an expression evaluates to true – instead it returns an argument. 

Evaluating `expr ARG1 | ARG2` returns ARG1 if ARG1 is neither `null` nor `0`, otherwise it'll return ARG2. On the other hand, evaluating `expr ARG1 & ARG2` returns ARG1 if neither of the arguments are `null` or `0` . It returns `0` otherwise. 

Let's examine few examples with the logical OR operator:

```bash
expr 1 \| 2     # Returns first argument (1)

expr 0 \| 2     # Returns second argument (2) as first argument is 0

expr "" \| 2    # Returns second argument (2) as first argument is null 
                  (Empty string [""] is considered as null in terminal)

expr 100 \| 78	# Returns first argument 100

expr "" \| ""   # Returns 0 as both arguments are null ("")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-68.png)
_Evaluating logical OR expressions with `expr` command_

The above screenshot represents operations with logical OR operator (|). Reading that you may still have a couple of questions:

### What's the purpose of using empty double quotes ("") in the expression? 

Empty double quotes represent a `null` value in bash. So, as said earlier, if the first argument is null, the second argument is returned. 

### What if both the arguments are null? 

When evaluating both arguments with null values, both the Logical OR and AND operators return `0`. 

Let's examine a few examples with the logical AND operator:

```bash
expr 1 \& 2     # Returns first argument (1)

expr 1 \& 0     # Returns 0 as one (second) argument is 0

expr 0 \& 1     # Returns 0 as one (first) argument is 0

expr "" \& 1	# Returns 0 as one (first) argument is null ("")

expr 1 \& ""	# Returns 0 as one (second) argument is null ("")

expr "" \| ""   # Returns 0 as both arguments are null ("")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-69.png)
_Evaluating logical AND expressions with `expr` command_

## How to Perform String Operations with the `expr` Command

The `expr` command is not limited to mathematical and logical operations. It can perform string operations, too. 

### Pattern Matching with Regex

The `expr` command can verify if a text matches with a regex pattern. It returns the matched pattern of the text if it exists or else returns an empty line. 

The syntax to verify the regex is:

```bash
expr STRING : REGEXP

or

expr match STRING REGEXP
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-71.png)
_`expr` command evaluates regex pattern match with the given text_

You can achieve this either by using the `match` keyword or by using a semicolon (`:`) between the string and the regex pattern. 

Alternatively, you can use the semicolon to find the number of characters matching between the two texts. 

Here's an example:

```bash
expr Remember : Remo    # Returns 0

expr Remember : Rem     # Returns 3
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-75.png)
_`expr` command to find the number of characters matching the given text_

### Find the length of a text

You can use the `expr length` command to find the length of the given text. 

```bash
expr length Linux

expr length "Learning Linux is fun"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-72.png)
_`expr length` command showing the number of characters in the given text_

You can enter the text directly after the `expr length` command if it does not have any spaces. If the text has spaces, enclose them within double quotes (""), or else you'll get an error. 

### Find a character in a text

You can find a particular character from a given text using the `expr index` command. It returns the place where the character exists. 

```bash
expr index STRING CHAR
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-74.png)
_`expr index` to find a character from a text_

Remember that the `expr index` command performs a case-sensitive search and returns the first matching index of a character from the text. 

### Extract a substring from a string

Extracting a substring from a string is simple using `expr` command. Entering the string, start index, and number of characters to be clipped after the start index will return the expected substring. 

```bash
expr substr Carpenter 4 3      # Returns pen
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-76.png)
_`expr substr` command to find a substring from a string_

## Conclusion

In this article, you have learnt the use cases of the `expr` command.

If you enjoyed my tutorial, you can subscribe to my newsletter on my [personal site](https://5minslearn.gogosoon.com/) to receive more such insightful articles straight to your inbox. You'll also find a consolidated list of all my blog posts. 


