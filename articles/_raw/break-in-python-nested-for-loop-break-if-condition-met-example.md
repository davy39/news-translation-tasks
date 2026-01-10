---
title: Break in Python – Nested For Loop Break if Condition Met Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-17T15:05:36.000Z'
originalURL: https://freecodecamp.org/news/break-in-python-nested-for-loop-break-if-condition-met-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/henry-co-1qlMnKfql5c-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Loops in programming let us execute a set of instructions/block of code\
  \ continuously until a certain condition is met. \nWe can also use loops to iterate\
  \ over a collection of data and perform a similar operation on each item in the\
  \ data set.\nnames = [..."
---

Loops in programming let us execute a set of instructions/block of code continuously until a certain condition is met. 

We can also use loops to iterate over a collection of data and perform a similar operation on each item in the data set.

```python
names = ["John", "Jane", "Doe"]
for i in names:
    print(i)
    
"""
John
Jane
Doe
"""
```

Above is a Python `for` loop that iterates over a list of names and prints all the names. 

In situations where we want to stop the iteration before getting to the last item or before a given condition is met, we can use the `break` statement. The `break` statement will have its own condition – this tells it when to "break" the loop.

In this article, we'll first see how to use the `break` statement in `for` and `while` loops. Then we'll look at some of the methods we can use to break nested loops in Python.

## How Do You Write a `break` Statement in Python?

You define the `break` statement in the loop you want it to terminate. In this section, we'll see how to use the `break` statement in `for` and `while` loops.

### How to Use the `break` Statement in a `for` Loop

Here's an example:

```python
names = ["John", "Jane", "Doe"]
for i in names:
    print(i)
    if i == "Jane":
        break
```

In the code above, we are printing a list of names:

```python
for i in names:
    print(i)
```

We then created a new condition which checks when the `i` variable gets to a name equal to "Jane". When that condition is met, the loop is required to stop. It stops because the `break` statement stops the loop when `i` is "Jane":

```python
if i == "Jane":
        break
```

This is the same as saying: "print all the names and stop once you get to Jane". So in our console, out of the three names — `["John", "Jane", "Doe"]` – only "John" and "Jane" will be printed. 

We can also do this with numbers:

```python
for i in range(10):
  print(i)
```

The code above prints a range of numbers from 0 to 9. But we can stop this loop from printing all the numbers – we can stop at a particular number instead. Here's how:

```python
for i in range(10):
  print(i)
  if i == 5:
      break
```

Now the loops stops at 5. So we'll only see 0, 1, 2, 3, 4 and 5 in the console.

### How to Use the `break` Statement in a `while` Loop

The example in this section will  be similar to the last section's. We'll be using a `while` loop instead.

```python
i = 0
while i < 10:
  print(i)
  i += 1
```

The code above prints a range of numbers from 0 to 9. We're going to use the `break` to stop printing numbers when we get to 5. 

```python
i = 1
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1
```

Just like we did in the last section, we created a new condition: `if i == 5` and when this condition is met, the loop is terminated instead of printing all the way to 9. 

### How to Use the `break` Statement in a Nested Loop

In this section, we'll see how to use the `break` statement in nested loops.

Here is what a nested loop looks like:

```python
for x in range(4):
    for y in range(4):
        print(x, y)

"""
0 0
0 1
0 2
0 3
1 0
1 1
1 2
1 3
2 0
2 1
2 2
2 3
3 0
3 1
3 2
3 3
"""
```

Nested loops can often be confusing to beginners. So if you're wondering how we got the output above (commented out in the code), here's a brief explanation:

`range(4)` will give us a range of numbers from 0 to  3. 

Printing only `for x in range(4):` will give us 0, 1, 2, 3. But we're nesting another range of numbers in the loop: `for y in range(4):`

What the second loop does is duplicate each number of `x` by the the number of integers it has (in the `y` range). We have four numbers in the `y` range – 0, 1, 2, 3. 

So for the `x` range, the first number is 0 and it will appear four times. Each time it appears, it takes one number from the `y` range; that is: 0 and 0, 0 and 1, 0 and 2, 0 and 3. This applies to the other numbers in the `x` range.

If you still find this difficult to understand, then try running the code yourself. Try changing the range of each loop to see what happens with the output.

Let's break the loop using the `break` statement:

```python
for x in range(4):
    for y in range(4):
        if x == 1:
            break
    print(x, y)
    
"""
0 3
1 3
2 0
3 3
"""
```

Although the loop in the example above seems to have stopped, having a closer look at the output (commented out above), you'll realize that the outer loop is still printing out all of its values which isn't what was intended.

So just using the `break` statement doesn't actually break a nested loop. Let's see some of the workarounds for achieving our desired result.

#### Using a Boolean Variable

```python
force_break_loop = False
for x in range(5):
    for y in range(5):
        if x == 2:
            force_break_loop = True
            break
    if force_break_loop:
        break
    print(x, y)

"""
0 4
1 4
"""
```

In the example above, we are using a boolean variable whose initial value is `False`. When the loop gets to the intended break point, we set this boolean as `True`, but that's not all. We check when the variable is `True` and then assign the `break` statement. 

#### Using the Break Statement Twice

```python
for x in range(5):
    for y in range(5):
        if x == 3:
            break
    if x == 3:
        break
    print(x, y)
    
"""
0 4
1 4
2 4
"""
```

In this example, we define two `if` statements – both returning a `break` statement to force the loop to break. 

While these workarounds may have terminated the loop at a given instance, you'll notice that the value of the inner loop remains the same every time the loop breaks. 

This does not mean that nested loops are bad. But make sure you really need them before implementing them in your logic.

## Conclusion

In this article, we saw how to use the `break` statement to terminate a loop before the loop's initial condition is met or before an iteration over the items in a data set is complete.

We saw some examples of how you can use the `break` statement in both `for` and `while` loops.

Lastly, we talked about nested loops. We found out that a `break` statement doesn't actually stop the loop. This led us to seeing some examples of some of the methods we can use to break a nested loop in Python.

Happy coding!

