---
title: Python Enumerate – Python Enum For Loop Index Example
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-22T17:53:56.000Z'
originalURL: https://freecodecamp.org/news/python-enumerate-python-enum-for-loop-index-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/tine-ivanic-u2d0BPZFXOY-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When you''re coding in Python, you can use the enumerate() function and
  a for loop  to print out each value of an iterable with a counter.

  In this article, I will show you how to use Python''s enumerate() function with
  a for loop and explain why it is ...'
---

When you're coding in Python, you can use the `enumerate()` function and a `for loop`  to print out each value of an iterable with a counter.

In this article, I will show you how to use Python's `enumerate()` function with a `for loop` and explain why it is a better option than creating your own incrementing counter.

But first, let's take a look at how to accomplish this without the `enumerate()` function.

## How to use a `for loop` without the `enumerate()` function in Python

In Python, an iterable is an object where you can iterate over and return one value at a time. Examples of iterables include lists, tuples, and strings. 

In this example, we have a list of dog names and a variable called `count`. 

```py
dogs = ['Harley', 'Phantom', 'Lucky', 'Dingo']
count = 1
```

We can use a `for loop` to go through the list and print each name. We are also going to increment the `count` variable by 1 each time to keep track of how many times we have iterated over the list. 

```py
for name in dogs:
    print(count, name)
    count += 1
```

This is what the result would look like printed to the screen:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-22-at-3.12.05-AM.png)

While this approach does work, it presents a possible error. 

A common mistake would be to forget to increment the `count` variable.

If I altered the code, then this would be the new result printed to the console:

```py
dogs = ['Harley', 'Phantom', 'Lucky', 'Dingo']
count = 1
for name in dogs:
    print(count, name)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-22-at-3.15.00-AM.png)

Now the `count` variable is no longer accurately keeping track of how many times we have looped over the list. 

Instead of incrementing a `count` variable ourselves, we can use the `enumerate()` function with the `for loop`.

## What is the `enumerate()` function in Python?

Python's built in `enumerate()` function takes in an iterable and an optional start argument.

```py
enumerate(iterable, optional start argument)
```

If you omit the optional `start` argument, then the count is set to zero. 

The return value of the `enumerate()` function is an object. 

This function keeps track of the iterations so you don't have to remember to update the `count` variable. 

We can use the `enumerate()` function with a `for loop` to print out the values of an iterable with a counter. 

## How to use a `for loop` and the `enumerate()` function in Python

In this example, we want to print out a list of directions going from Times Square to the Juilliard School of Music in New York City, New York. 

We first have to create the list of `directions`:

```py
directions = [
    'Head north on Broadway toward W 48th St',
    'Turn left onto W 58th St',
    'Turn right onto 8th Ave',
    'Turn left onto Broadway',
    'Turn left onto Lincoln Center Plaza',
    'Turn right onto Jaffe Dr',
    'Turn left onto Broadway',
    'Turn left onto W 65th St'
]
```

Then in the `for loop`, we create the `count` and `direction` loop variables.

The `enumerate()` function will take in the `directions` list and `start` arguments. We want to start counting at 1 instead of the default of 0.  

```py
for count, direction in enumerate(directions, start=1):
```

Inside the loop we will print out the `count` and `direction` loop variables. 

```py
print(count, direction)
```

This is what is looks like all put together:

```py
directions = [
    'Head north on Broadway toward W 48th St',
    'Turn left onto W 58th St',
    'Turn right onto 8th Ave',
    'Turn left onto Broadway',
    'Turn left onto Lincoln Center Plaza',
    'Turn right onto Jaffe Dr',
    'Turn left onto Broadway',
    'Turn left onto W 65th St'
]

for count, direction in enumerate(directions, start=1):
    print(count, direction)
```

This is what the results look like in the console:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-22-at-3.52.27-AM.png)

As you can see the `count` variable was automatically updated with the `enumerate()` function. 

This removes the possibility for errors if we forget to increment the `count` variable. 

## Conclusion

You can use the `enumerate()` function and a `for loop`  to print out each value of an iterable with a counter. 

The `enumerate()` function takes in an iterable and an optional start argument.

```py
enumerate(iterable, optional start argument)
```

If the optional `start` argument is omitted then the count is set to zero. 

Using the `enumerate()` function is a better alternative than creating your own incrementing counter in a `for loop`.

The `enumerate()` function automatically updates the count which eliminates the possibility that you might forget to increment the counter.

I hope you enjoyed this article and best of luck on your Python journey. 


