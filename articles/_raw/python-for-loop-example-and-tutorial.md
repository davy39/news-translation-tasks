---
title: Python For Loop – Example and Tutorial
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-27T22:36:10.000Z'
originalURL: https://freecodecamp.org/news/python-for-loop-example-and-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/kevin-canlas-cFFEeHNZEqw-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Loops let you control the logic and flow structures of your programs. \n\
  Specifically, a for loop lets you execute a block of similar code operations, over\
  \ and over again, until a condition is met.\nYou repeat certain code instructions\
  \ for a set of valu..."
---

Loops let you control the logic and flow structures of your programs. 

Specifically, a `for` loop lets you execute a block of similar code operations, over and over again, until a condition is met.

You repeat certain code instructions for a set of values you determine, and you perform actions on each value for a pre-determined number of times.

## What is a for loop in Python?
 
A `for` loop can iterate over every item in a list or go through every single character in a string and won't stop until it has gone through every character.

Writing `for` loops helps reduce repetitiveness in your code, following the DRY (Don't Repeat Yourself) principle. You don't write the same block of code more than once.

In this article, we'll get to know the basics of `for` loops in the Python programming language using different examples. But first let's learn some `for` loop basics.

## How Does a for loop Work in Other Programming Languages?

Looping in most modern programming languages like JavaScript, Java, or C looks something like the example below. 

Loops in JavaScript:

```JavaScript
for (let i = 0; i < 10; i++) {
  console.log('Counting numbers');
  // prints "Counting numbers" 10 times
  // values of i from 0 to 9 
  }
```

The for loop generally keeps track of three things:

1. The initialization expression statement which is exactuted once, `let i = 0;`
2. The condition that needs to be met, `i < 10;`. This condition is evaluated as either `true` or `false`. If it is `false`, the loop is terminated.
3. If the condition is `true` the body of the loop will be executed and the initialized expression will take some action. In this case it will be incremented by 1 (`i++`), until the condition set is met. 


## for loop Syntax in Python

The for loop in Python looks quite different compared to other programming languages.

Python prides itself on readability, so its `for` loop is cleaner, simpler, and more compact.

The basic structure is this:

```
for item in sequence:
    execute expression
```

where: 

- `for` starts a `for` loop.
- `item` is an individual item during each iteration. It is given a temporary arbitary variable name.
- `in` separates each item from the other(s).
- `sequence` is what we want to iterate over.
- a colon `:` gives the instruction to execute the body of code that follows.
- A new line.
- A level of indentation. 4 spaces before writing the body of the loop, otherwise we get an `IndentationError`.
- The body with the actions that need to be taken and repeated (for example, print something to the console). It goes where the `execute experssion` line is.

### How the Python for loop works

Let's say we have a sequence, a list of stored items we want to run through – in this case a grocery list:

```Python
groceries = ["bananas","butter","cheese","toothpaste"]
```


The `in` keyword checks to see if an item is included in a sequence. When combined with the `for` keyword, it indicates iterating over every item in the sequence. 

It does something with every item on the list. In this case it prints separetely each individual item to the console until every item has been iterated over.

```Python
for grocery in groceries:
    # for each iteration print the value of grocery
    print(grocery)
```

`grocery` is a temporary variable name to refer to each item of the list.

It's an `iterator variable`, that with each succesive iteration its value gets set to each value the list includes. Essentially, it's a temporary variable with a temporary value.

We could name it whatever we want, such as `g` or `item`. But the name should be unique and not be the same as any other variable in our program.

On the first run, the first element – `bananas` – is stored in the variable `item`.

Then the expression `print(grocery)`, which essentially is how `print("bananas")` is executed. 

On the second run, the element `butter` is stored in the variable `item` and as above, it gets printed to the console. 

This process continues until all items have been iterated over.

Here's the output of that code:

```
bananas
butter
cheese
toothpaste
```


### How to use a for loop for a range of numbers

We can use the `range()` function with a given range to specify how many times in a row we want the `for` loop to iterate over. This simplifies the `for` loop.

The `range()` function creates a sequence of integers depending on the arguments we give it.

How does this work?

Take a look at the example below:

```python
for i in range(5):
    print(i)
```

The output of which is:

```
0
1
2
3
4
```

It creates a list of numbers between 0 and 4. 

By default when we give `range()` one argument, the range starts counting from `0`. 

Notice that `5` is not printed to the console.

In `range(5)`, we specify that `5` is the highest number we want, but *not inclusive*. It does not include it, it's just the stopping point. It defines  how many times we want our loop to run. We see it runs 5 times and creates a sort of list of 5 items: `0,1,2,3,4`.

If you want to see what `range()` produces for debugging purposes, you can pass it to the `list()` function.

Open the interactive Python shell in your console, typically  with the command `python3`, and type:

```python
show_numbers = list(range(5))

print(show_numbers)
```

What if we want our range to start from 1 and then to also see 5 printed to the console? We instead give `range()` two different arguments this time:

```python
for i in range(1,6):
    print(i)
```

Output:

```
1
2
3
4
5
```

The first argument (`start`) which as we saw earlier is optional, is where the sequence should begin (in this case it's 1). This argument is *inclusive* and the number is included. 
 
The second argument (`stop`) which is required, is where the sequence should end and is *not inclusive*, as mentioned earlier. In this case it's 6.
 
Lastly, you can pass in a third optional parameter: `step`.
 
This controls the *increment* between the two values in the range. The default value of `step` is 1.
 
Let's say we wanted to jump every two numbers and get the odd numbers from a sequence. We could do:
 
 ```python
 for i in range(1,10,2):
     print(i)
```

Output:

```
1
3
5
7
9
```

`1` is where we start, `10` is 1 higher than what we want (which is 9), and `2` is the amount we want to jump between numbers (in this case we jump every two numbers).
 
 
### How to use enumerate() in Python

So far we have not used any indexes when iterating. Sometimes, we need to access the index of the item we're looping through and display it.

We can loop over items with the index using `enumerate()`.

Our example from earlier:

```Python
groceries = ["bananas","butter","cheese","toothpaste"]

for grocery in groceries:
    print(grocery)
```

Can now be written like this:

```Python
groceries = ["bananas","butter","cheese","toothpaste"]

for index, grocery in enumerate(groceries):
    print(index,grocery)   
```


Output:
```
0 bananas
1 butter
2 cheese
3 toothpaste
```

Or for a bit more complex output:

```Python
groceries = ["bananas","butter","cheese","toothpaste"]
for index, grocery in enumerate(groceries):
    print(f"Grocery: {grocery} is at index: {index}.") 
```

Output:

```
Grocery: bananas is at index: 0.
Grocery: butter is at index: 1.
Grocery: cheese is at index: 2.
Grocery: toothpaste is at index: 3
```


- Instead of just writing one variable `grocery` like before, now we write two: `index,grocery`. On each iteration, `index` contains the index of the value and `grocery` the value of `groceries`.
- `index` is the index of the value being iterated.
-  Indexes in Python start counting at `0` .
-  `grocery` is the value of the item at the current iteration
- The line `enumerate(groceries)`  lets us iterate through the sequence and keep track of the index of the value and the value itself.  
  
  
## Conclusion

I hope you enjoyed this basic introduction to the `for` loop in Python.

We went over the basic syntax that makes up a `for` loop and how it works.

We then briefly explained what the two built-in python methods, `range()` and `enumerate()`, do in `for` loops.

Thanks for reading and happy coding!




