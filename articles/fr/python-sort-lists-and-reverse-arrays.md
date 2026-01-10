---
title: Liste triée en Python – Et comment trier ou inverser un tableau en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-24T17:24:10.000Z'
originalURL: https://freecodecamp.org/news/python-sort-lists-and-reverse-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Python-Sorted-List
seo_title: Liste triée en Python – Et comment trier ou inverser un tableau en Python
---

And-How-to-Sort-or-Reverse-an-Array-in-Python--by-Shittu-Olumide-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nLes tableaux et les listes en Python sont des structures de données très intéressantes. \n\nLes listes et les tableaux sont constitués d'éléments ordonnés et mutables – mais les tableaux contiennent des éléments de même type, tandis que les listes peuvent stocker plusieurs types d'éléments. \n\nDans cet article, ..."
---

Par Shittu Olumide

Les tableaux et les listes en Python sont des structures de données très intéressantes. 

Les listes et les tableaux sont constitués d'éléments ordonnés et mutables – mais les tableaux contiennent des éléments de même type, tandis que les listes peuvent stocker plusieurs types d'éléments. 

Dans cet article, nous allons apprendre comment inverser un tableau en utilisant le découpage et la méthode `reverse()`. Nous parlerons également de comment trier des listes en Python en utilisant la méthode `sort()`, la fonction `sorted()` et le module `heapq`. 

## Plan

1. Comment inverser un tableau en Python.  
- En utilisant le découpage.  
- En utilisant la méthode `reverse()`.
2. Comment trier une liste en Python.  
- En utilisant la méthode `sort()`.  
- En utilisant la fonction `sorted()`.  
- En utilisant le module `heapq`.

## Comment inverser un tableau en Python

Inverser un tableau est souvent une approche de force brute plus efficace pour une variété de problèmes. Et parfois, nous pourrions avoir besoin de parcourir un tableau en commençant par la fin.

### Comment inverser un tableau en utilisant le découpage

Le découpage nous permet d'accéder à une plage spécifique d'éléments dans une séquence, telle qu'un tableau, une liste ou une chaîne. Nous pouvons spécifier la plage que nous voulons accéder en utilisant deux indices séparés par un deux-points. 

Pour inverser le tableau, nous pouvons spécifier une valeur de pas de `-1`, ce qui signifie que nous commencerons par la fin du tableau et nous déplacerons vers le début, dans l'ordre inverse. 

La syntaxe du découpage pour inverser un tableau en Python ressemble à ceci:

```py
arrayName[::-1]

```

Voici le code pour inverser un tableau en utilisant le découpage:

```py
# importer le module array
import array
    
# déclarer un tableau
x = array.array("i", [1, 2, 3, 4, 5])

# découper le tableau
print('Le tableau inversé est ', x[::-1])

```

Sortie:

```bash
Le tableau inversé est  array('i', [5, 4, 3, 2, 1])

```

### Comment inverser un tableau en utilisant la méthode `reverse()`

Python fournit également une méthode `reversed()` pour les tableaux. Le tableau n'est pas dupliqué par la méthode `reversed()`, ni le tableau original n'est altéré de quelque manière que ce soit. 

Au lieu de cela, un itérateur est retourné. Le but de cette méthode est de simplifier l'itération inverse sur les séquences.

```py
import array as arr

# initialiser le tableau avec des entiers
x = arr.array("i", [1, 2, 3, 4, 5])

# passer le tableau dans reversed()
reversed(x)

print("Le tableau inversé: ", x)

```

Sortie:

```bash
Le tableau inversé:  array('i', [1, 2, 3, 4, 5])

```

Notez que l'ordre du tableau sera également inversé s'il contient des éléments mutables comme des dictionnaires, des listes ou d'autres tableaux. Afin de prévenir cela, nous pouvons d'abord utiliser la méthode `copy()` pour faire une copie superficielle du tableau.

## Comment trier une liste en Python

Une liste triée est une liste qui maintient ses éléments dans l'ordre, généralement dans l'ordre croissant. Une liste triée est une structure de données qui nous permet de maintenir l'ordre original des éléments tout en les triant, contrairement à la fonction `sorted()`. Parce qu'une nouvelle liste triée n'est pas créée, la liste originale est modifiée sur place.

Considérons les méthodes que nous pouvons utiliser pour trier une liste en Python.

### Comment trier une liste en utilisant la méthode `sort()`

La méthode `sort()` est une fonction intégrée de la classe liste qui trie les éléments de la liste dans l'ordre croissant. La syntaxe de la méthode `sort()` est la suivante:

```py
list.sort(key=None, reverse=False)

```

La fonction d'un argument pour extraire une clé de comparaison de chaque élément dans la liste est spécifiée par le paramètre key. Nous pouvons spécifier si nous voulons trier la liste dans l'ordre croissant ou décroissant en utilisant le paramètre reverse.

Exemple:

```py
# Créer une liste de nombres
num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Trier la liste dans l'ordre croissant
num.sort()

print(num)

```

Sortie:

```bash
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

```

Comme nous pouvons le voir, la liste est triée de 1 à 9 sans aucune erreur, bien que certains des éléments de la liste soient imprimés deux fois.

### Comment trier une liste en utilisant la fonction `sorted()`

La fonction `sorted()` est une fonction intégrée qui retourne une nouvelle liste triée à partir de l'itérable donné. La syntaxe de la fonction `sorted()` est la suivante:

```py
sorted(iterable, key=None, reverse=False)

```

La séquence d'éléments qui doivent être triés constitue le paramètre iterable. Une fonction d'un argument est spécifiée par le paramètre key afin d'extraire une clé de comparaison de chaque élément de la liste. Vous pouvez trier une liste dans l'ordre croissant ou décroissant en utilisant le paramètre reverse.

Voici un exemple:

```py
# Créer une liste de nombres
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Créer une nouvelle liste triée
sorted_nums = sorted(nums)

print(sorted_nums)

```

Sortie:

```bash
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

```

### Comment trier une liste en utilisant le module `heapq`

Le module heapq de Python offre des fonctions pour travailler avec des files d'attente de tas. Une fonction appelée `heappushpop()` dans le module `heapq` nous permet de pousser un élément sur un tas, de le retirer, puis de retourner le plus petit élément de celui-ci.

Voici une illustration de la façon d'utiliser `heappushpop()` pour ordonner une liste de nombres dans l'ordre croissant:

```py
import heapq

# définir une fonction qui prend une liste
def sort_list(lst):
    heap = []
    for item in lst:
        heapq.heappush(heap, item)

    sorted_lst = []
    for i in range(len(heap)):
        sorted_lst.append(heapq.heappop(heap))

    return sorted_lst

# Exemple d'utilisation:
lst = [5, 2, 9, 1, 5, 6]
sorted_lst = sort_list(lst)
print(sorted_lst)

```

Sortie:

```bash
[1, 2, 5, 5, 6, 9]

```

Voici un autre exemple:

```py
import heapq

my_list = [3, 5, 2, 7, 1]

# Convertir la liste en un tas
heapq.heapify(my_list)

# Créer une liste vide pour stocker les valeurs triées
sorted_list = []

# Retirer la plus petite valeur du tas et l'ajouter à la liste triée jusqu'à ce que le tas soit vide
while my_list:
    sorted_list.append(heapq.heappop(my_list))

print(sorted_list)

```

Sortie:

```bash
[1, 2, 3, 5, 7]

```

## Conclusion

Trier et inverser une liste ou un tableau sont des tâches courantes en Python, et il existe plusieurs façons d'accomplir ces tâches. Nous avons discuté de trois approches populaires pour trier des listes en Python – en utilisant la méthode intégrée `sort()` et la fonction `sorted()`, ainsi que le module `heapq`.

De plus, nous avons exploré comment inverser un tableau en utilisant à la fois la fonction intégrée `reverse()` et le découpage. 

Trier et inverser des listes et des tableaux peut être une partie importante du traitement et de l'analyse des données, et il est essentiel de comprendre comment implémenter ces tâches efficacement en Python.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage!