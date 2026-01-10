---
title: Python Break and Python Continue – How to Skip to the Next Function
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-14T13:55:01.000Z'
originalURL: https://freecodecamp.org/news/python-break-and-python-continue-how-to-skip-to-the-next-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/thisisengineering-raeng-uyfohHiTxho-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'If you ever need to skip part of the current loop you are in or break out
  of the loop completely, then you can use the break and continue statements.

  In this article, I will cover how to use the break and continue statements in your
  Python code.

  How ...'
---

If you ever need to skip part of the current loop you are in or break out of the loop completely, then you can use the `break` and `continue` statements.

In this article, I will cover how to use the `break` and `continue` statements in your Python code.

## How to use the break statement in Python

You can use the `break` statement if you need to break out of a `for` or `while` loop and move onto the next section of code.

In this first example we have a for loop that loops through each letter of freeCodeCamp. 

```py
for letter in 'freeCodeCamp':
    print('letter :', letter)
```

This is what is printed to the console:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.46.39-PM.png)

If we wanted to stop our loop at the letter "o", then we can use an `if` statement followed by a `break` statement.

```py
for letter in 'freeCodeCamp':
    if letter == "o":
        break
    print('letter :', letter)
```

This is what is printed to the console:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.49.15-PM.png)

In this next example, we are using a `while` loop to increment `num` as long as `num` is less than 20.

```py
num = 5
while num < 20:
    print('Current number :', num)
    num = num + 1
```

This is what is printed to the console:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.54.17-PM.png)

We could add a condition inside our `while` loop that says if `num` is 9, then break out of the loop.

```py
num = 5
while num < 20:
    print('Current number :', num)
    num = num + 1
    if num == 9:
        break
```

This is what is printed to the console:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.55.38-PM.png)

## How to use the continue statement in Python

You can use the `continue` statement if you need to skip the current iteration of a `for` or `while` loop and move onto the next iteration.

In this example, we are looping through a string of my name.

```py
for letter in "Jessica":
```

Inside the `for` loop, we have a condition that says if the letter is "i" then skip that iteration and move onto the next iteration.

```py
  if letter == "i":
        continue
```

This is what the code looks like all together:

```py
for letter in "Jessica":
    if letter == "i":
        continue
    print(letter)
```

This is what is printed to the console:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-9.22.33-PM.png)

You should notice that the letter "i" was not printed to the console and the `continue` statement skipped that iteration. 

In this next example, we are going to print numbers in increments of 10 using a `while` loop. We are going to add a condition in the loop that says if the number is 50, then skip that iteration and move onto the next one.

```py
num = 10
while num < 100:
    num = num + 10
    if num == 50:
        continue
    print("Current num: ", num)
```

This is what is printed to the console:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-9.35.33-PM.png)

As you can see, the number 50 is not printed to the console because of the `continue` statement inside the `if` statement.

## Conclusion 

The `break` and `continue` statements in Python are used to skip parts of the current loop or break out of the loop completely.

The `break` statement can be used if you need to break out of a `for` or `while` loop and move onto the next section of code.

The `continue` statement can be used if you need to skip the current iteration of a `for` or `while` loop and move onto the next iteration.

I hope you enjoyed this article and best of luck on your Python journey. 




