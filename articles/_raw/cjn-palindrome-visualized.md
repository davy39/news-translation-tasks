---
title: What Exactly is a Palindrome - a  Visual Explanation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T22:56:49.000Z'
originalURL: https://freecodecamp.org/news/cjn-palindrome-visualized
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca1a4740569d1a4ca4fd2.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Clark Jason Ngo

  What is a palindrome?

  A Palindrome is a word, phrase, or sequence that reads the same backward as forward.

  Why do developers need to know what a palindrome is, and why should they learn this?


  Palindromes are a commonly asked strin...'
---

By Clark Jason Ngo

### What is a palindrome?

A Palindrome is a word, phrase, or sequence that reads the same backward as forward.

### Why do developers need to know what a palindrome is, and why should they learn this?

* Palindromes are a commonly asked string manipulation / algorithm problem
* The example below is the easiest one. 
* There are tons of palindrome questions ranging from easy to hard (see links at the end).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-5.png)

### A Quick Palindrome Checking Method:

```python3
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)

    if (s == rev):
        return True
    return False

#
s = "racecar"
ans = isPalindrome(s)

if ans == 1:
    print("Yes")
else:
    print("No")
```

Source: [https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/](https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/)

### Quicker Palindrome Check:

```python3
str(n) == str(n)[::-1]
```

Source: [https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic/17331328](https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic/17331328)

### Learning materials

Wikipedia: [https://en.wikipedia.org/wiki/Palindrome](https://en.wikipedia.org/wiki/Palindrome)

GeeksForGeeks: [https://www.geeksforgeeks.org/string-palindrome/](https://www.geeksforgeeks.org/string-palindrome/)

### Solve palindrome challenges

Leetcode: [https://leetcode.com/problemset/all/?search=palindrome](https://leetcode.com/problemset/all/?search=palindrome)

Codewars: [https://www.codewars.com/kata/search/my-languages?q=palindrome&beta=false](https://www.codewars.com/kata/search/my-languages?q=palindrome&beta=false)

### Other visualizations

[Bubble Sort](https://www.freecodecamp.org/news/cjn-bubble-sort-visualized/)

