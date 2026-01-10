---
title: Tri à bulles visualisé
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-20T01:04:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-bubble-sort-visualized
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/7632653238_c9436bb80d_b-1.jpg
tags:
- name: algorithms
  slug: algorithms
- name: learning to code
  slug: learning-to-code
seo_title: Tri à bulles visualisé
seo_desc: 'By Clark Jason Ngo

  What you need:

  1) Unsorted array

  2) for loop i - number of loop is based on the number of elements in the array.
  Each loop of i would reset loop of j to index zero.

  3) for loop j - number of loop is based on number of loop i minus ...'
---

Par Clark Jason Ngo

**Ce dont vous avez besoin :**

1) Tableau non trié

2) boucle **for i** - le nombre de boucles est basé sur le nombre d'éléments dans le tableau. Chaque boucle de **i** réinitialise la boucle de **j** à l'index zéro.

3) boucle **for j** - le nombre de boucles est basé sur le nombre de boucles **i** moins 1 pour chaque boucle de **j**. Pourquoi ? nous sommes déjà sûrs que le dernier élément de chaque boucle est trié et n'a pas besoin d'être comparé dans la boucle suivante (d'où -1).

4) une variable pour échanger les nombres. vous n'en avez pas besoin en Python.

**Visualisation :**

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-56.png)

Si vous vous demandez comment j'ai fait cela, j'ai utilisé l'application **Numbers** sur mon MacBook.

### Programme Python pour l'implémentation du Tri à bulles

```py
def bubbleSort(arr):
  n = len(arr)

  # Parcourir tous les éléments du tableau 
  for i in range(n): 

	  # Les i derniers éléments sont déjà en place 
	  for j in range(0, n-i-1): 
  
  		  # parcourir le tableau de 0 à n-i-1 
		  # Échanger si l'élément trouvé est plus grand 
		  # que l'élément suivant 
		  if arr[j] > arr[j+1] : 
			  arr[j], arr[j+1] = arr[j+1], arr[j] 

```

### Code pilote pour tester ce qui précède

```py
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print ("Le tableau trié est :")

for i in range(len(arr)):
    print ("%d" %arr[i]),
```

Source du code : [https://www.geeksforgeeks.org/bubble-sort/](https://www.geeksforgeeks.org/bubble-sort/)