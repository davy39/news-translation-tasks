---
title: Python Operator – Logical Operators in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-22T00:21:14.000Z'
originalURL: https://freecodecamp.org/news/operators-in-python-how-to-use-logical-operators-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pixabay-161154.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Suchandra Datta\nOperators in any programming language are the basic\
  \ building blocks using which we can construct powerful, complex statements for\
  \ problem solving. \nPython offers different types of operators, like arithmetic\
  \ operators, logical oper..."
---

By Suchandra Datta

Operators in any programming language are the basic building blocks using which we can construct powerful, complex statements for problem solving. 

Python offers different types of operators, like arithmetic operators, logical operators, relational operators and so on. In this post, let's dive into logical operators in Python and learn how we can use them.

Python offers three logical or boolean operators, "and", "or" and "not" operators. These work on one or more operands, and depending on their values, evaluate to True or False. Then decisions are made based on this. 

### Python "and" operator

The Python "and" operator is a binary operator, which means it requires two operands. The general syntax looks like this:

```
operand1 and operand2
```

The output is True if and only if both the operands are True. If any operand is False, then the output is False. Let's see some examples:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-70.png)

Here we use the "and" operator to decide if a person can be considered a player in Squid Game or not. 

The 2 operands for "and" are the variables `person_has_debt` and `person_willing_to_play`. Since the values for both are True, the output of the and expression is True and a new player object is created where we specify the player name and player number. 

Now, what if the value for `person_willing_to_play` is False?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-69.png)

We know that "and" outputs True only if both operands are True. If either one is False, the output is False and the statements in the else clause get executed. We can add as many expressions as we want using "and", for example:

```python
if person_has_debt and person_willing_to_play and proper_age and total_player_capacity_not_full:
    player_obj = SquidGamePlayer("Sae-byok", 67)
    player_obj.show_details()
else:
    print("Player not added to game")
```

The operand's truth value is evaluated from left to right and output is False if any 1 operand is False, else the output is True. 

Operands can be arithmetic or relational expressions (or any combination of the two), nested logical expressions, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-73.png)

### Python "or" operator

The "or" operator is also a binary operator and needs 2 operands. The output of the "or" expression is True if any of its operands are True, else the output is False.

```
operand1 or operand2
```

 Let's look at some simple examples:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-74.png)

Here the operands for "or" are the output of the method `has_high_traffic` with input `"some_road_name"` and `"another_road_name"`. 

For simplicity this method returns True or False at random. During the 1st execution, False is returned for both method calls and "or" evaluates to False as both operands are False. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-76.png)

During the 2nd execution, the random number is now 1 so the method call `has_high_traffic("some_road_name")` returns True. We know that if any operand of "or" is True then the final output is also True. So in this case the "or" expression is True and the statements in the if clause are executed. 

Did you notice one thing here? Only the 1st method call was executed, and `has_high_traffic("another_road_name")` did not get invoked. Why? This is due to something called **short-circuiting** which we'll learn about shortly.

### Python "not" operator

The "not" is a unary operator, which means that it works with 1 operand and returns the inverted truth value for that operand. 

```
not ( operand )
```

In simple terms, if the input is True, then the output is False and if the input is False, then the output is True. 

This is simple when the operands are directly of type `bool`. However, the inputs can be numeric types, objects, lists and so on. In such cases, the output depends on how Python calculates the truth value for that entity. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-78.png)

### How does Python calculate the truth value?

All the logical operators work with the truth value of their operands – but what exactly is a truth value? 

We know that the bool type `True` represents True and `False` represents False. Python considers zero to be False and all other numbers, irrespective if they are positive or negative, are considered to be True. 

Look at the examples shown below:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-71.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-72.png)

The truth value of entities in Python is computed on the basis of some standard rules, as defined in the "Truth value testing" portion of the documentation linked [here](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).

So, now we know how the not operator is working in the following examples:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-79.png)

An empty list `[]` has zero length, so the truth value is False. Zeroes are False, in both cases the inverted value is True and 3 is True so `not(3)` is equivalent to `not(True)` which is False. 

### Short-circuiting of logical operators

Logical "and" and "or" operators in Python are short-circuited which means they evaluate only the bare minimum required to get the correct result. For example:

```python
if expression1 and expression2 and expression3:
	#do something
else:
	#do something else	
```

If `expression1` is False, we know that the final output of `and` is False. Then does it make sense to evaluate `expression2` and `expression3`? Nope it does not make sense, and Python doesn't do it either. It starts evaluating from left to right, as soon as an expression is False, the "and" evaluates to False, skipping the execution of the remaining operands. 

The same thing happens for the "or" operator:

```
if expression1 or expression2 or expression3:
	#do something
else:
	#do something else	
```

If `expression1` is True, then immediately the output of the "or" expression becomes True, ignoring the remaining 2 operands. 

This saves spending unnecessary time on evaluating expressions whose output won't affect the final output of the expression anyway. 

### A final note on how "and" and "or" work

In the beginning of this post, I mentioned that the output of "and" is True if and only if all of its operands are True – else the output is False, like the following:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-82.png)

Now let's see a bit of what happens under the hood. `and` actually does not return a True or False value. Instead it returns one of its operands! This is mentioned in the documentation [here](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), specifically this part, quoted from the documentation:

> (Important exception: the Boolean operations `or` and `and` always return one of their operands.)

```
operand1 and operand2
```

So if `operand1` is False, `and` returns `operand1`, otherwise it returns `operand2`. If operands are of type bool, then it is easy to understand. What if we have operands like the following:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-80.png)

What's happening here? `operand1` is 12 which is True, `operand2` is 56 which is also True, so `and` returns `operand2` which is 56. 

Okay but how does this work in conditional statements like in if-else? Remember that 56 also has a truth value right? So `and` gives an output of 56, and now the truth value of 56 is used in the if-else. 56 is True so the if-clause is executed. 

Similarly we have "or" that also returns one of its operands:

```
operand1 or operand2
```

It returns `operand2` if `operand1` is False, else it returns `operand1`, as we can clearly see in the following snippet:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-81.png)

## Wrapping up

In this post, we learnt about:

1. The different logical operators in Python and how to use them with examples
2. How Python calculates the truth value of entities
3. What is short-circuiting
4. How "and" and "or" operators work under the hood

Thank you very much for reading, I hope you enjoyed the article and learnt a few interesting facts related to logical operators in Python. Take care and happy coding!

