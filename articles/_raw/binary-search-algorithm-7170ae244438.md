---
title: Binary Search Algorithms explained using security camera footage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-17T19:22:09.000Z'
originalURL: https://freecodecamp.org/news/binary-search-algorithm-7170ae244438
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gjDukf9SgTpJOq2tFe9Iyw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Julia Geist


  Binary search, also known as half-interval search or logarithmic search, is a search
  algorithm that finds the position of a target value within a sorted array.


  Context

  I used to live in a building that had a communal kitchen for over...'
---

By Julia Geist

> Binary search, also known as half-interval search or logarithmic search, is a search algorithm that finds the position of a target value within a sorted array.

### Context

I used to live in a building that had a communal kitchen for over 100 students. As you might imagine, there were almost always dishes that weren’t washed in the sink. A group at my school pitched the idea to put up a Nest Cam to catch culprits and call them out on it using the Nest Cam feed.

To illustrate my point, let’s say you found dirty dishes at 12 pm, and you hadn’t been in the kitchen for a day.

Think about the way that you would search for the person who left the dishes. Would you watch all 24 hours of footage, from the beginning, until you found the culprit?

Probably not. Most likely you’d be hopping around the footage, checking to see if the dishes were in the sink, say, 12 hours ago — at 12 am. If they were, then you’d know that it happened before 12 am. You might flip back to 10 pm after that. If the dishes _aren’t_ there, you’ve now narrowed down the time frame from 10 pm to 12 am — in other words, you’ve ruled out any time before 10 pm. You’d continue this process until you found the culprit.

![Image](https://cdn-media-1.freecodecamp.org/images/t1WQMX7wWxGGHHyXER-9NOVgc0FZPN2WMgAT)
_Binary search for the moment the orange cup is put into the sink (Youtube video used)_

What would have taken you up to 24 hours, if you had watched the footage in its entirety, now only takes a few seconds.

Whether you knew it or not, the specific process we just went through is a binary search! A binary search is a _very specific_ way of hopping back and forth in the footage.

Namely, the footage is split at its midpoint to check for the dishes each time. Notice how the distance to the midpoint gets exponentially smaller with each click.

Binary searches are used to find elements quickly and efficiently. The catch, though, is that **binary searches only work when the structure you’re looking through is _sorted_**.

In the Nest Cam example, what is the footage sorted by? What are we looking for within that sorted arrangement?

In this case, the data we are searching is sorted by time. Time allows for a linear measurement. Therefore, it allows us to perform a binary search to find someone who doesn’t wash their dishes within a matter of seconds.

We also need something that we’re looking for. In this case, it’s the presence of unwashed dishes in the communal sink.

### Binary Search Algorithm

![Image](https://cdn-media-1.freecodecamp.org/images/d27KVv4hAnngmMMZ1rz4GjXIgsceR5H9tHzP)

While programming, a binary search can be used in a multitude of contexts. It’s an _extremely_ quick way to find elements within a sorted structure.

Binary searches can be implemented in an iterative or recursive fashion. An iterative implementation uses a `while` loop. Meanwhile, a recursive implementation will call itself from within its own body.

In code, I’ll be performing a binary search on a relatively simple, sorted set of data to highlight the core implementation of a binary search.

Given an array of sorted numbers, return `True` if 53 is an element.

```
[0, 3, 4, 5, 6, 15, 18, 22, 25, 27, 31, 33, 34, 35, 37, 42, 53, 60]
```

#### Iterative

In the iterative approach, a while loop runs until the range of possibilities is zero. This is done by changing the upper and lower bounds of where we are looking and calculating the middle index _of that range._

The range exists between the lower and upper bounds, inclusive of the bounds themselves.

![Image](https://cdn-media-1.freecodecamp.org/images/zO-GtUNZ6ezlXEHMhdvP4JjOxmmqBZCePp9L)

Before the `while` loop begins, the lower bound is zero and the upper bound is the length of the array. The upper bound changes if the number we’re looking for is in the first half of the range. The lower bound changes if the number we’re looking for is in the second half of the range.

If the `while` loop finishes, meaning there is a range of length zero, return `False`.

```
def binarySearch(array, number):   lowerBound = 0   upperBound = len(array)
```

```
while lowerBound < upperBound:        middleIndex = int(math.floor(lowerBound + (upperBound —    lowerBound) / 2))        if array[middleIndex] == number:             return True        elif array[middleIndex] < number:             lowerBound += 1        elif array[middleIndex] > number:             upperBound = middleIndex   return False
```

I’d like to elaborate on this equation:

`int(math.floor(lowerBound + (upperBound — lowerBound) / 2))`

The _length_ of the **range** is calculated by subtracting the lower bound from the upper bound. However, knowing how long the range is isn’t enough.

At this point, we don’t know which indexes to check in the array. So we are shifting up the array by the lower bound.

We then divide that by two, and round down, to get the middle index of the range. `math.floor` returns a `float`, so we also have to cast the result to an `int`.

#### Recursive

In the recursive approach, the function will call itself from within its body.

The upper bound in this function is the length of the array passed in. Again, the upper bound changes if the number we’re looking for is in the first half of the array. The lower bound changes if the number we’re looking for is in the second half of the array.

```
def binarySearch(array, number):    middleIndexOfArray = int(math.floor(len(array) / 2))    if middleIndexOfArray == 0:        return False
```

```
if array[middleIndexOfArray] == number:        return True   elif array[middleIndexOfArray] > number:        return binarySearch(array[:middleIndexOfArray], number)   elif array[middleIndexOfArray] < number:        return binarySearch(array[middleIndexOfArray:], number)
```

The function then calls itself, passing in an argument of an array half the length of the array that was its argument.

If there are zero elements in the array, return `False`.

The code is available on my [Algorithms and Data Structures](https://github.com/juliascript/Algorithms-and-Data-Structures) repo — star it to stay updated!

### Next Steps

I wrote my first binary search to implement a stochastic sampling algorithm. It generates a sentence based on the frequency of words in a corpus of text.

Feel free to try and build a similar project, which has quite a bit of prep before you can implement the binary search. Or think of your own projects and share them in the comments!

This is the second post of my algorithm and data structures series. In each post, I’ll present a problem that can be better solved with an algorithm or data structure to illustrate the algorithm/data structure itself.

Star my [algorithms repo](https://github.com/juliascript/Algorithms-and-Data-Structures) on Github and follow me on [Twitter](https://twitter.com/JuliaGeist) if you’d like to follow along!

