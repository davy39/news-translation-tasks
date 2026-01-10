---
title: Comment résoudre les problèmes Leetcode avec des one-liners Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-02T15:13:35.000Z'
originalURL: https://freecodecamp.org/news/solve-leetcode-problems-using-python-list-comprehension
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60640fde9618b008528aa027.jpg
tags:
- name: leetcode
  slug: leetcode
- name: Problem Solving
  slug: problem-solving
- name: Python
  slug: python
seo_title: Comment résoudre les problèmes Leetcode avec des one-liners Python
seo_desc: "By Ganesh Kumar Marimuthu\nPython is one of the most powerful programming\
  \ languages. It gives us various unique features and functionalities that make it\
  \ easy for us to write code. \nIn this article we'll solve Leetcode array problems\
  \ in one line using..."
---

Par Ganesh Kumar Marimuthu

Python est l'un des langages de programmation les plus puissants. Il nous offre diverses fonctionnalités uniques qui facilitent l'écriture de code.

Dans cet article, nous allons résoudre des problèmes de tableaux Leetcode en une ligne en utilisant l'une des fonctionnalités les plus intéressantes de Python : la **compréhension de liste**.

## Qu'est-ce que la compréhension de liste ?

Avant de nous pencher sur les problèmes, assurons-nous de bien comprendre ce qu'est la compréhension de liste.

> Une compréhension de liste est une construction syntaxique disponible dans certains langages de programmation pour créer une liste basée sur des listes existantes.
> - Wikipedia

Voyons comment fonctionne la compréhension de liste avec un exemple.

Considérons un tableau de nombres. Notre tâche consiste à ajouter 1 aux nombres aux indices impairs et à ajouter 2 aux nombres aux indices pairs.

Nous allons maintenant voir comment résoudre le problème ci-dessus en utilisant à la fois une boucle for et une compréhension de liste.

### Comment résoudre le problème avec une boucle for

```python
def addOneAndTwo(nums, n):
    for i in range(n):
        if i % 2 == 1:
            nums[i] += 1 
        else:
            nums[i] += 2 
    return nums
```

### Comment le résoudre avec la compréhension de liste

```python
def addOneAndTwo(nums, n):
    return [nums[i] + 1 if i % 2 == 1 else nums[i] + 2 for i in range(n)]
```

Vous pouvez voir comment la solution utilisant la compréhension de liste est simplifiée de 6 lignes à 1 ligne. C'est la puissance de la compréhension de liste.

## Comment résoudre les problèmes Leetcode avec la compréhension de liste

Maintenant, résolvons les problèmes Leetcode suivants en 1 ligne en utilisant la compréhension de liste.

### 1. [Melanger le tableau](https://leetcode.com/problems/shuffle-the-array/)

Voici le problème de Leetcode :

Étant donné le tableau `nums` composé de `2n` éléments sous la forme `[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]`. _Retournez le tableau sous la forme_ `[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]`.

#### Exemple

Entrée : nums = [2,5,1,3,4,7], n = 3   
Sortie : [2,3,5,4,1,7] 

Explication : Puisque x1=2, x2=5, x3=1, y1=3, y2=4, y3=7, alors la réponse est [2,3,5,4,1,7].

#### Solution

```python
def shuffle(self, nums, n):
    return reduce(lambda a, b: a + b, [[nums[i], nums[j]] for i, j in zip(range(0, n), range(n, 2 * n))])
```

### 2. [Nombre de bonnes paires](https://leetcode.com/problems/number-of-good-pairs/)

Étant donné un tableau d'entiers `nums`. Une paire `(i,j)` est appelée _bonne_ si `nums[i]` == `nums[j]` et `i` < `j`. Retournez le nombre de _bonnes_ paires.

#### Exemple

Entrée : nums = [1,2,3,1,1,3]   
Sortie : 4 

Explication : Il y a 4 bonnes paires (0,3), (0,4), (3,4), (2,5) indexées à 0.

#### Solution

```python
def numIdenticalPairs(self, nums):
    return sum([int(i != j and nums[i] == nums[j]) for i in range(0, len(nums)) for j in range(i + 1, len(nums))])
```

### 3. [Enfants avec le plus grand nombre de bonbons](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

Étant donné le tableau `candies` et l'entier `extraCandies`, où `candies[i]` représente le nombre de bonbons que le **ième** enfant possède.

Pour chaque enfant, vérifiez s'il existe un moyen de distribuer `extraCandies` parmi les enfants de sorte qu'ils puissent avoir le **plus grand** nombre de bonbons parmi eux. Notez que plusieurs enfants peuvent avoir le **plus grand** nombre de bonbons.

#### Exemple

Entrée : candies = [2,3,5,1,3], extraCandies = 3   
Sortie : [true,true,true,false,true]

Explication : L'enfant 1 a 2 bonbons, et s'il reçoit tous les bonbons supplémentaires (3), il aura 5 bonbons - le plus grand nombre de bonbons parmi les enfants. 

L'enfant 2 a 3 bonbons, et s'il reçoit au moins 2 bonbons supplémentaires, il aura le plus grand nombre de bonbons parmi les enfants. 

L'enfant 3 a 5 bonbons, et c'est déjà le plus grand nombre de bonbons parmi les enfants. 

L'enfant 4 a 1 bonbon, et même s'il reçoit tous les bonbons supplémentaires, il n'aura que 4 bonbons. 

L'enfant 5 a 3 bonbons, et s'il reçoit au moins 2 bonbons supplémentaires, il aura le plus grand nombre de bonbons parmi les enfants.

#### Solution

```python
def kidsWithCandies(self, candies, extraCandies):
    return [candy + extraCandies >= max(candies) for candy in candies]
```

### 4. [Décompresser une liste encodée par longueur de série](https://leetcode.com/problems/decompress-run-length-encoded-list/)

On nous donne une liste `nums` d'entiers représentant une liste compressée avec un encodage par longueur de série.

Considérons chaque paire d'éléments adjacents `[freq, val] = [nums[2*i], nums[2*i+1]]` (avec `i >= 0`). Pour chaque paire, il y a `freq` éléments avec la valeur `val` concaténés dans une sous-liste. Concaténez toutes les sous-listes de gauche à droite pour générer la liste décompressée.

Retournez la liste décompressée.

#### Exemple

Entrée : nums = [1,2,3,4]   
Sortie : [2,4,4,4] 

Explication : La première paire [1,2] signifie que nous avons freq = 1 et val = 2, donc nous générons le tableau [2]. 

La deuxième paire [3,4] signifie que nous avons freq = 3 et val = 4, donc nous générons [4,4,4]. À la fin, la concaténation [2] + [4,4,4] est [2,4,4,4].

#### Solution

```python
def decompressRLElist(self, nums):
    return reduce(lambda a, b: a + b, [[nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)])
```

### 5. [Riche client avec la plus grande richesse](https://leetcode.com/problems/richest-customer-wealth/)

On vous donne une grille d'entiers `accounts` de taille `m x n` où `accounts[i][j]` est le montant d'argent que le **ième** client possède dans la **jème** banque. Retournez **la richesse** que le client le plus riche possède.

La **richesse** d'un client est le montant d'argent qu'il possède dans tous ses comptes bancaires. Le client le plus riche est celui qui a la **richesse** maximale.

#### Exemple

Entrée : accounts = [[1,2,3],[3,2,1]]   
Sortie : 6 

Explication : `Le 1er client a une richesse = 1 + 2 + 3 = 6, le 2ème client a une richesse = 3 + 2 + 1 = 6`. Les deux clients sont considérés comme les plus riches avec une richesse de 6 chacun, donc retournez 6.

#### Solution

```python
def maximumWealth(self, accounts):
    return max([sum(row) for row in accounts])
```

## Conclusion

J'espère que les solutions ci-dessus ont été utiles. Vous pouvez combiner la [**compréhension de liste**](https://data-flair.training/blogs/python-list-comprehension/) avec d'autres fonctions comme [**map**, **filter** et **reduce**](https://www.freecodecamp.org/news/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f/) pour rendre les solutions plus simples et efficaces.

## Merci 🤘

[Linkedin](https://www.linkedin.com/in/ganeshkumarm1) | [Github](https://github.com/ganeshkumarm1)