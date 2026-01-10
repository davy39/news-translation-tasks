---
title: Qu'est-ce qu'un Palindrome - une Explication Visuelle
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
seo_title: Qu'est-ce qu'un Palindrome - une Explication Visuelle
seo_desc: 'By Clark Jason Ngo

  What is a palindrome?

  A Palindrome is a word, phrase, or sequence that reads the same backward as forward.

  Why do developers need to know what a palindrome is, and why should they learn this?


  Palindromes are a commonly asked strin...'
---

Par Clark Jason Ngo

### Qu'est-ce qu'un palindrome ?

Un palindrome est un mot, une phrase ou une séquence qui se lit de la même manière à l'envers qu'à l'endroit.

### Pourquoi les développeurs doivent-ils savoir ce qu'est un palindrome, et pourquoi devraient-ils l'apprendre ?

* Les palindromes sont un problème courant de manipulation de chaînes / algorithme souvent posé
* L'exemple ci-dessous est le plus simple.
* Il existe de nombreuses questions sur les palindromes, allant des plus faciles aux plus difficiles (voir les liens à la fin).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-5.png)

### Une Méthode Rapide pour Vérifier un Palindrome :

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
    print("Oui")
else:
    print("Non")
```

Source : [https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/](https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/)

### Vérification Plus Rapide d'un Palindrome :

```python3
str(n) == str(n)[::-1]
```

Source : [https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic/17331328](https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic/17331328)

### Matériel d'apprentissage

Wikipedia : [https://en.wikipedia.org/wiki/Palindrome](https://en.wikipedia.org/wiki/Palindrome)

GeeksForGeeks : [https://www.geeksforgeeks.org/string-palindrome/](https://www.geeksforgeeks.org/string-palindrome/)

### Résoudre les défis de palindromes

Leetcode : [https://leetcode.com/problemset/all/?search=palindrome](https://leetcode.com/problemset/all/?search=palindrome)

Codewars : [https://www.codewars.com/kata/search/my-languages?q=palindrome&beta=false](https://www.codewars.com/kata/search/my-languages?q=palindrome&beta=false)

### Autres visualisations

[Tri à Bulles](https://www.freecodecamp.org/news/cjn-bubble-sort-visualized/)