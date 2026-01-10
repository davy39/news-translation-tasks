---
title: Check out my visual guide to recursion (because a picture’s worth 1,000 words)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-27T20:34:35.000Z'
originalURL: https://freecodecamp.org/news/recursion-visually-explained-bec8cca14d9b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PPXnzjpCdxuMiz9OJdhe8w.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jerry Muzsik

  In this article, I will explain recursion (almost) completely with visual representations.
  I’ll show, rather than explain, how each recursive function call interacts with
  the entirety of the initial function invocation — in other word...'
---

By Jerry Muzsik

In this article, I will explain recursion (almost) completely with visual representations. I’ll show, rather than explain, how each recursive function call interacts with the entirety of the initial function invocation — in other words, how each piece connects to the whole.

A few details:

* The code is written in Python
* Blue boxes represent the current scope of the function
* Connecting lines are what a function returns

Please use the code as a reference, as I do not go over the running of it in detail.

We’ll look at three problems: finding the Anagrams of a string, Merge Sort, and The Tower of Hanoi. They progressively get a little bit more nuanced, so watch out!

I’ll discuss more details of recursion below.

### Anagrams

```python
def anagrams(s):
    if s == "":
        return [s]
    else :
        ans = []
    for w in anagrams(s[1: ]):
        for pos in range(len(w) + 1):
            ans.append(w[: pos] + s[0] + w[pos: ])
    return ans

anagrams("abc")

# returns ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z67ClqdjbnaZvkASvFOxNg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YLyylfd6hKYJ9rhW4JrBHQ.png)
_anagramursion_

The above is a good intro to the call stack. Notice how each prior call is awaiting the return value of the recursive call.

Also notice how the variable `ans` values are all appended during the initial function call (1).

### Merge Sort

```python
def merge(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        else:
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1
    
    # unequal length of lists? Check both
    while i1 < n1: 
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

def mergeSort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        mergeSort(nums1)
        mergeSort(nums2)
        merge(nums1, nums2,nums)
    
numbers = [7, 4, 6, 2, 8]
mergeSort(numbers)

print(numbers)
# returns sorted numbers (function altered underlying data structure)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*t9czQmsarojfOozmxL8yJw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nnvoyLfp3vkppsXPG0MOdg.png)
_recursamerged_

Again, notice the order in which each call runs. To understand how merge works, look closely at it. You basically have three pointers and two sorted halves of the initial list that are continually compared. The lowest number during this comparison is set at the index that is being pointed to in the initial list (starting at index 0).

Several notes if you are not used to Python. When a function returns nothing, it returns the value `None` . You can see the frequent return value of `None` in my diagrams, as there are no explicit return statements in `mergeSort`.

Also, notice how the list input into the function call is mutated, which is to say that Python did not create a copy of the list when the function was called.

### Tower of Hanoi

Here’s a quick story as a side note — I found it to be quite a poetic intro to the Tower of Hanoi:

> “Somewhere in a remote region of the world is a monastery of a very devout religious order. The monks have been charged with a sacred task that keeps time for the universe. At the beginning of all things, the monks were given a table that supports three vertical posts. On one of the posts was a stack of 64 concentric, golden disks. The disks are of varying radii and stacked in the shape of a beautiful pyramid. The monks are charged with the task of moving the disks from the first post to the third post. When the monks complete their task, all things will crumble to dust and the universe will end.” — _John Zell, Python Programming: An Introduction to Computer Science (2004)_

```python
def moveTower(n, source, dest, temp):
    if n == 1:
        print("Move disk from", source, "to", dest+".")
    else:
        moveTower(n-1, source, temp, dest)
        moveTower(1, source, dest, temp)
        moveTower(n-1, temp, dest, source)
    
 def hanoi(n):
    moveTower(n, "A", "C", "B")
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-VwEe3eLmdZ0e2fKLiZMQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*KwKjFU1KLTZun28Kvni0CQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dbkrNWmhXfpwJv2eJHINhA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IBrJOSrMZqF6Z0O5VDwPsQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*M19VyJnzn0mPfE4-CuFAcg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AKUhFf1l7tcgF88Pp5MaFA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7-1o9KOOaEKBScXEQskabA.png)
_hanoision_

The moving of the blocks is based upon a [mathematical principle](https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/).

From the [Wikipedia article](https://en.wikipedia.org/wiki/Tower_of_Hanoi):

1. Move _m_ − 1 disks from the **source** to the **temp** peg. This leaves the disk _m_ as a top disk on the source peg.
2. Move the disk _m_ from the **source** to the **dest** peg.
3. Move the _m_ − 1 disks that we have just placed on the spare from the **temp** to the **dest** peg, so they are placed on top of the disk _m_ without violating the rules.

But how does one make sense of this principle? Well, check this out.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XVjr4Ue0FtF2BUj1W2E-Tw.png)
_exactitude_

Notice this: the three rules repeat (black text) except when rule 2 (blue text) runs, because the algorithm does not reach its base case.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rt-CKWzyXM1VP-mwD8XuuA.png)
_basically_

#### A word on recursion

This article is the first step in being able to solve recursive problems. I created this to help readers understand how recursion works, and what the reality of it is. For each problem, notice how I ordered each function invocation and return value. This is the same way that the computer reads the code.

The basic underlying concept of recursion is this:

**The function in which the recursive function call was called in must wait for the recursive function call to finish before it continues its process.**

So if the recursive function calls more recursive functions, then it must also wait for those recursive functions to return. Recursion, in a way, just involves functions waiting for the functions they called to return something prior to continuing.

If you desire to grow in the realm of recursive problem solving, then you must study math. They are one and the same. But going over the math is beyond the scope of this article. This [wikipedia article](https://en.wikipedia.org/wiki/Mathematical_induction) is a nice primer to begin with.

That’s that. I must thank, absolutely and completely, [Data Structures and Algorithms Using Python and C++](https://www.amazon.com/gp/product/1590282337/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1) by David M. Reed, as well as John Zelle, since that is where that wonderful quote and the algorithms were mined from.

And here’s a nice view of space because, well, recursion feels a bit like it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PPXnzjpCdxuMiz9OJdhe8w.png)

