---
title: Python range() Function – Explained with Code Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-06T17:21:45.000Z'
originalURL: https://freecodecamp.org/news/python-range-function-explained-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/range---function.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, can use use the range() function to get a sequence of indices\
  \ to loop through an iterable. You'll often use range() in conjunction with a for\
  \ loop. \nIn this tutorial, you'll learn about the different ways in which you can\
  \ use the range() f..."
---

In Python, can use use the `range()` function to get a sequence of indices to loop through an iterable. You'll often use `range()` in conjunction with a `for` loop. 

In this tutorial, you'll learn about the different ways in which you can use the `range()` function – with explicit start and stop indices, custom step size, and negative step size.

Let's get started.

## Understanding Python's `range()` Function

Before looking at the different ways of using the `range()` function, you've got to understand how it works.

> The `range()` function returns a range object.    
> This range object in turn returns the successive items in the sequence when you iterate over it. 

As stated above, the range function _does not return_ a list of indices. Rather, it returns a range object which returns the indices as and when you need them. This makes it memory-efficient as well.  

You can use the `range()` function with the following general syntax:

```
range(start,stop,step)
```

When you use this syntax in conjunction with a loop, you can get a sequence of indices from `start` up to but not including `stop` , in steps of `step`.

* You must specify the _required_ argument `stop`, which can be any positive integer. If you specify a floating point number instead, you'll run into a `TypeError` as shown:

```python
my_range = range(2.5)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-24.png)

* If you don't specify the `start` index, the _default_ start index of `0` is used.
* If you don't specify the `step` value, the _default_ step size of `1` is used.

In the subsequent sections, you'll learn about the different ways of using the `range()` function. 

## How to Use Python's `range()` Function to Loop Through Any Iterable

As mentioned in the previous section, you only need one positive integer to use the `range()` function. The syntax is shown below:

```
range(stop)


```

You can use the above line of code to get a sequence from `0` through `stop-1` : `0`, `1`, `2`, `3`,..., `stop-1`.  

▶ Consider the following example where you call `range()` with 5 as the argument. And you loop through the returned range object using a `for` loop to get the indices 0,1,2,3,4 as expected.

```python
for index in range(5):
  print(index)
  
#Output
0
1
2
3
4
```

If you remember, all iterables in Python follow _zero-indexing_. This is why it's convenient to use `range()` to loop through iterables. 

An iterable of length `len` has `0`, `1`, `2`, ..., `len-1` as the valid indices. So to traverse any iterable, all you need to do is to set the `stop` value to be equal to `len`. The sequence you'll get – `0`, `1`, `2`, ..., `len-1` – is the sequence of valid indices.

▶ Let's take a more helpful example. You have a list `my_list`. You can access all items in the list by knowing their indices, and you can get those indices using `range()` as shown below:

```python
my_list = ["Python","C","C++","JavaScript","Julia","Rust","Go"]
for index in range(len(my_list)):
  print(f"At index {index}, we have {my_list[index]}")
```

Remember, you can use Python's built-in function `len` to get the length of any iterable. In the above code, you use both the valid indices, and the list items at those valid indices. Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-25.png)

Notice how `my_list` is 7 items long, and the indices obtained are from 0 through 6, as expected.

Sometimes, you may need to use negative integers instead. In this case, if you use only the `stop` argument, you'll not get the desired output, though the code doesn't throw an error. 

This is because the default `start` value is assumed to be `0`, and you cannot count up from `0` to `-5`.

```python
for index in range(-5):
  print (index)
  
  
#Output
#NOTHING HERE
```

## How to Use Python's `range()` Function with Explicit Start and End Indices

You may not always want to start at zero. You can start at any arbitrary index by setting the `start` value to the index that you'd like to start from. The syntax is as follows:

```
range(start,stop)
```

In this case, you'll be able to get the sequence: `start`, `start + 1`, `start + 2`, and so on up to `stop-1`. 

▶ In the example below, you're starting at 10, count all the way up to but not including 15 in steps of 1.

```python
for index in range(10,15):
  print(index)

#Output
10
11
12
13
14
```

In the previous section, you saw how using only the `stop` argument won't work when you need negative integers. However, when you specify `start` and `stop` indices explicitly, you can as well work with negative integers.

▶ In this example, you're trying to count up from -5 in steps of 1. Always keep in  mind that the counting stops at the value that's one less than the `stop` index.

```python
for index in range(-5,0):
  print(index)
  
#Output
-5
-4
-3
-2
-1
```

## How to Use Python's `range()` Function **with** a **Custom Step Size**

Instead of traversing an iterable sequentially, you may sometimes want to stride through it, accessing every `k`-th element. This is when the optional `step` argument comes in handy. The general syntax is shown below:

```
range(start,stop,step)
```

When you use this syntax and loop through the range object, you can go from `start` to `stop-1` with strides of size `step`.

* You'll get the sequence: `start`, `start + step`, `start + 2*step`, and so on up to `start + k*step` such that  `start + k*step` < `stop` and `start + (k+1)*step` > `stop`.

▶ In the example below, you'd like to go from 0 to 20 in steps of 2. Notice how the last index printed out is 19. This is because, if you take another step, you'll be at 21 which is greater than 20. 

Always remember, the last value you get can be as close to `stop` as possible, but can never be `stop`.

```python
for index in range(1,20,2):
  print(index)

#Output
1
3
5
7
9
11
13
15
17
19
```

## How to Use Python's `range()` Function **with** a Negative Step Size

So far, you've learned to use the `range()` function with `start` and `stop` indices, and a specific step size, all the while counting up from `start` to `stop`. 

If you need to count down from an integer, you can specify a negative value for `step`. The general syntax is:

```
range(start,stop,<negative_step>)
```

* The range object can now be used to return a sequence that counts down from `start` in steps of `negative_step`, up to but not including `stop`. 
* The sequence returned is `start`, `start - negative_step`, `start - 2*negative_step`, and so on up to `start - k*negative_step` such that `start - k*negative_step` > `stop` and `start - (k+1)*negative_step` < `stop`.
* There's no default value for negative step – you must set `negative_step = -1` to count down covering each number.

▶ In this example, you'd like to count down from 20 in steps of -2. So the sequence is 20, 18, 16, all the way down to 2. If you go another 2 steps lower, you'll hit 0, which you cannot as it's smaller than the stop value of 1.

```python
for index in range(20,1,-2):
  print(index)
  
#Output
20
18
16
14
12
10
8
6
4
2
```

It's easy to see that `start` > `stop` to be able to count down. 

```python
for index in range(10,20,-1):
  print(index)
  
 #Ouput
 #Nothing is printed - the sequence is empty.
```

▶ In the above example, you try counting down from 10 to 20 which is impossible. And you don't get any output which is expected.

## How to Use Python's `range()` and `reversed()` Functions to Reverse a Sequence

If you need to access the elements of an iterable in the reverse order, you can use the `range()` function coupled with the `reversed()` function.

> Python's built-in `reversed()` function returns a reverse iterator over the values of a given sequence.

▶ Let's take our very first example, where we used `range(5)`. In the example below, we call `reversed()` on the range object. And we see that we've counted down from 4 to 0. 

```python
for index in reversed(range(5)):
  print (index)
  
#Output
4
3
2
1
0
```

As you can see, this is equivalent to using `range(4,-1,-1)`. If you prefer, you may use the `reversed()` function instead of `negative_step` argument discussed in the previous section.

## Conclusion

In this tutorial, you've learned the different ways in which you can use the `range()` function. You can try a few examples to get a different sequence each time. This practice will help you use `range()` effectively when looping through iterables.

Happy coding! Until the next tutorial.🙂

