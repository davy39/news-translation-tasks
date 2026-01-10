---
title: Python If Else Statement – Conditional Statements Explained
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-29T15:32:30.000Z'
originalURL: https://freecodecamp.org/news/python-if-else-statement-conditional-statements-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/clement-helardot-95YRwf6CNw8-unsplash.jpg
tags:
- name: Conditionals
  slug: conditionals
- name: Python
  slug: python
seo_title: null
seo_desc: 'There are many cases where you don''t want all of your code to be executed
  in your programs.

  Instead, you might want certain code to run only when a specific condition is met,
  and a different set of code to run when the condition is not satisified.

  Th...'
---

There are many cases where you don't want all of your code to be executed in your programs.


Instead, you might want certain code to run only when a specific condition is met, and a different set of code to run when the condition is not satisified.

That's where conditional statements come in handy.

Conditional statements allow you to control the logical flow of programs in a clean and compact way.

They are branches – like forks in the road – that modify how code is executed and handle decision making.

This tutorial goes over the basics of `if`, `if..else`, and `elif`  statements in the Python programming language, using examples along the way.

Let's get started!

## The syntax of a basic `if` statement

An `if` statement in Python essentially says:

"If this expression evaluates to True, then run once the code that follows  the exprerssion. If it isn't True, then don't run the block of code that follows."

The general syntax for a basic `if` statement looks something like this:

```
if condition:
    execute statement
```

An `if` statement consists of:

- The `if` keyword, which starts the `if` statement.
- Then comes a condition. A condition can evaluate to either True or False.   Parentheses (`()`) surrounding the condition are optional, but they do help improve the readability of the code when more than one condition is present.
-  A colon `:` that separates the condition from the executable statement that follows.
-  A new line.
-  A level of indentation of **4** spaces, which is a Python convention. The level of indentation is associated with the body of the statement that follows.
-  Lastly comes the body of the statement. This is the code that will run only if the statement evaluated to True. We can have multiple lines in the body that can be executed, and in that case we need to be careful they all have the same level of indentation. 

Let's take the following example:

```python
a = 1
b = 2

if b > a:
    print(" b is in fact bigger than a")
```

Output:

```
b is in fact bigger than a
```

In the example above, we created two variables, `a` and `b`, and assigned them the values `1` and `2`, respectively.

The phrase in the print statement does in fact get printed to the console because the condition `b > a` evaluated to True, so the code that followed it ran. If it wasn't True, nothing would have happend. No code would have run.

If we had instead done this:

```python
a = 1
b = 2

if a > b
    print("a is in fact bigger than b")
```

No code would have been executed and nothing would have been printed to the console.

## How do Python `if..else` statements work?

An `if` statement runs code only when a condition is met. Nothing happens otherwise. 

What if we also want code to run when the condition is not met? That's where the `else` part comes in.

The syntax of an `if..else` statement looks like this:

```
if condition:
    execute statement if condition is True
else:
     execute statement if condition is False
```

An `if..else` statement in Python means: 

"When the `if` expression evaluates to True, then execute the code that follows it. But if it evalates to False, then run the code that follows the `else` statement"

The `else` statement is written on a new line after the last line of indented code and it *can't* be written by itself. An `else` statement is part of an `if` statement. 

The code following it also needs to be indented with **4** spaces to show it is part of the `else` clause.

The code following the `else` statement gets executed *if and only if* the `if` statement is False. If your `if` statement is True and therefore the code ran, then the code in the `else` block will never run.

```python
a = 1
b = 2

if a < b:
    print(" b is in fact bigger than a")
else:
    print("a is in fact bigger than b")
```

Here, the line of code following the `else` statement, `print("a is in fact bigger than b")`, will never run. The `if` statement that came before it is True so only that code runs instead.

The `else` block runs when:

```python
a = 1
b = 2

if a > b:
    print(" a is in fact bigger than b")
else:
    print("b is in fact bigger than a")
```

Output:
```
b is in fact bigger than a
```

Be aware that you can't write any other code between `if` and `else`. You'll get a `SyntaxError` if you do so:

```python
if 1 > 2:
   print("1 is bigger than 2")
print("hello world")
else:
   print("1 is less than 2")
```


Output:

```
File "<stdin>", line 3
print("hello world")
^
SyntaxError: invalid syntax
```

## How does `elif` work in Python?

What if we want to have more than just two options? 

Instead of saying: "If the first condition is true do this, otherwise do that instead", now we say "If this isn't True, try this instead, and if all conditions fail to be True, resort to doing this".

`elif` stands for else, if.

The basic syntax looks like this:

```
if first_condition:
    execute statement
elif second_condition:
    execute statement
else:
    alternative executable statement if all previous conditions are False
```

We can use more than one `elif` statement. This gives us more conditions and more options. 

For example:

```python
x = 1

if x > 10:
    print(" x is greater than 10!")
elif x < 10:
      print("x is less than 10!")
elif x < 20 :
      print("x is less than 20!")
else:
     print("x is equal to 10")
```

Output:

```
x is less than 10!
```

In this example, the `if` statement tests a specific condition, the `elif` blocks are two alternatives, and the `else` block is the last solution when  all the previous conditions have not been met.

Be aware of the order in which you write your `elif` statements.

In the previous example, if you had written:

```python
x = 1

if x > 10:
    print(" x is greater than 10!")
elif x < 20 :
      print("x is less than 20!")
elif x < 10:
      print("x is less than 10!")
else:
     print("x is equal to 10")
```

The line `x is less than 20!` would have been executed because it came first.

The `elif` statement makes code easier to write. You can use it instead of keeping track of `if..else` statements as programs get more complex and  grow in size.

If all the `elif` statements are not considered and are False, then and only then as the last resort will the code following the `else` statement run.

For example, here's a case when the `else` statement would run:

```python
x = 10

if x > 10:
    print(" x is greater than 10!")
elif x < 10:
      print("x is less than 10!")
elif x > 20 :
      print("x is greater than 20!")
else:
     print("x is equal to 10")
```

Output

```
x is equal to 10
```


## Conclusion

And that's it! 

Those are the basic principles of `if`,`if..else` and `elif` in Python to get you started with conditional statements.

From here the statements can get more advanced and complex.

Conditional statements can be nested inside of other conditional statements, depending on the problem you're trying to solve and the logic behind the solution. 

Thanks for reading and happy coding!



