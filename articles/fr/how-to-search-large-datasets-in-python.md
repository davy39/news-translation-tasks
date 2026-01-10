---
title: Comment rechercher efficacement de grands ensembles de données en Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-04-03T15:08:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-large-datasets-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/efffe.JPG
tags:
- name: data analysis
  slug: data-analysis
- name: Python
  slug: python
- name: search
  slug: search
seo_title: Comment rechercher efficacement de grands ensembles de données en Python
seo_desc: 'Imagine you''re trying to find a needle in a haystack, but the haystack
  is the size of a mountain. That''s what it can feel like to search for specific
  items in a massive dataset using Python.


  But fear not! With the right techniques, you can efficient...'
---

Imaginez que vous essayez de trouver une aiguille dans une botte de foin, mais que la botte de foin est de la taille d'une montagne. C'est ce que cela peut donner de rechercher des éléments spécifiques dans un ensemble de données massif en utilisant Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/raw--1-.gif align="left")

Mais n'ayez crainte ! Avec les bonnes techniques, vous pouvez rechercher et consulter efficacement des informations dans de grands ensembles de données sans avoir l'impression de gravir l'Everest.

Dans cet article, je vais vous montrer comment simplifier les opérations de recherche en Python. Nous explorerons une gamme de techniques, de l'utilisation du module bisect intégré à la réalisation d'une recherche binaire, et nous ajouterons même un peu de fun avec les ensembles et les dictionnaires.

Alors attachez votre ceinture et préparez-vous à optimiser vos opérations de recherche sur de grands ensembles de données. C'est parti !

## Méthode 1 : Recherche linéaire en Python

La manière la plus simple de rechercher un élément dans une liste est d'effectuer une recherche linéaire. Cela implique de parcourir la liste un élément à la fois jusqu'à ce que l'élément souhaité soit trouvé. Voici un exemple de recherche linéaire :

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```

Dans le code ci-dessus, nous définissons la fonction linear_search, qui accepte deux entrées : une liste arr et un élément unique x. La fonction parcourt la liste, itérant à travers chaque élément et le comparant à l'élément souhaité x. La fonction retourne l'index de l'élément dans la liste si une correspondance est trouvée. En l'absence de correspondance, la méthode retourne -1.

La recherche linéaire a une complexité temporelle de O(n), où n est la longueur de la liste. Cela indique que le temps nécessaire pour effectuer une recherche linéaire augmentera proportionnellement à mesure que la taille de la liste grandit.

## Méthode 2 : Recherche binaire en Python

Si la liste est triée, nous pouvons effectuer une recherche binaire pour trouver l'élément cible plus efficacement. La recherche binaire fonctionne en divisant répétitivement l'intervalle de recherche en deux jusqu'à ce que l'élément cible soit trouvé. Voici un exemple de recherche binaire :

```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
```

Dans le code ci-dessus, nous définissons la fonction binary_search, qui accepte en entrées une liste triée arr et un élément cible x. Les indices low et high sont utilisés par la fonction pour maintenir un intervalle de recherche.

À chaque itération de la boucle, la fonction effectue une comparaison entre l'élément cible x et l'élément du milieu de l'intervalle de recherche.

Si l'élément du milieu est inférieur à x, l'intervalle de recherche modifié omet la moitié inférieure de la liste. Si l'élément du milieu est supérieur à x, l'intervalle de recherche est modifié pour omettre la moitié supérieure de la liste. La fonction fournit l'index de l'élément dans la liste si l'élément du milieu est égal à x.

Si l'élément souhaité ne peut pas être localisé, la fonction retourne -1. La recherche binaire a une complexité temporelle de O(log n), où n est la longueur de la liste. Cela signifie que, surtout pour les grandes listes, la recherche binaire est substantiellement plus efficace que la recherche linéaire.

## Méthode 3 : Recherche en utilisant des ensembles en Python

Si l'ordre de la liste n'est pas important, nous pouvons convertir la liste en un ensemble et utiliser l'opérateur `in` pour vérifier si un élément est présent dans l'ensemble. Voici un exemple :

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_set = set(my_list)
if 5 in my_set:
    print("5 est dans la liste")
else:
    print("5 n'est pas dans la liste")
```

Dans le code ci-dessus, nous définissons une liste `my_list` et la convertissons en un ensemble `my_set`. Nous utilisons ensuite l'opérateur `in` pour vérifier si l'élément 5 est présent dans l'ensemble. Si l'élément est présent, nous imprimons un message indiquant qu'il est dans la liste. Si l'élément n'est pas présent, nous imprimons un message indiquant qu'il n'est pas dans la liste.

L'utilisation d'ensembles pour les opérations de recherche peut être très efficace pour les grandes listes, surtout si vous devez effectuer plusieurs recherches, car les ensembles ont une complexité temporelle moyenne de O(1) pour l'opérateur `in`. Mais les ensembles ne préservent pas l'ordre des éléments, et la conversion d'une liste en un ensemble entraîne un coût supplémentaire.

## Méthode 4 : Recherche en utilisant des dictionnaires en Python

Si vous devez associer chaque élément de la liste à une valeur ou à une autre information, vous pouvez utiliser un dictionnaire pour stocker les données. Les dictionnaires offrent un moyen rapide de rechercher une valeur basée sur une clé. Voici un exemple :

```python
students = {
    "John": 85,
    "Lisa": 90,
    "Mike": 76,
    "Sara": 92,
    "David": 87
}
if "Lisa" in students:
    print(f"La note de Lisa est {students['Lisa']}")
else:
    print("Lisa n'est pas dans la classe")
```

Dans le code ci-dessus, nous définissons un dictionnaire `students` qui associe le nom de chaque étudiant à sa note. Nous utilisons ensuite l'opérateur `in` pour vérifier si le nom "Lisa" est dans le dictionnaire, et si c'est le cas, nous imprimons sa note.

Les dictionnaires offrent une complexité temporelle moyenne de O(1) pour les recherches basées sur la clé, ce qui les rend très efficaces pour les grands ensembles de données. Cependant, les dictionnaires ne préservent pas l'ordre des éléments, et il y a un coût supplémentaire associé à la création du dictionnaire.

## Conclusion

Rechercher et consulter des informations dans de grands ensembles de données peut être une tâche intimidante, mais avec les bons outils et techniques, cela n'a pas à l'être. En appliquant les méthodes que nous avons couvertes dans cet article, vous pouvez naviguer efficacement dans des ensembles de données massifs avec aisance et précision.

Du module bisect intégré aux capacités puissantes des ensembles et des dictionnaires, Python offre une gamme d'options efficaces et polyvalentes pour trouver et récupérer des données. En combinant ces techniques avec des pratiques de programmation intelligentes et des stratégies d'optimisation, vous pouvez créer des opérations de recherche ultra-rapides capables de gérer même les plus grands ensembles de données.

Alors ne laissez pas les grandes données vous intimider. Avec un peu de créativité, beaucoup de persévérance et les techniques que nous avons explorées dans cet article, vous pouvez surmonter n'importe quel défi de recherche et en sortir victorieux. Bonne recherche !