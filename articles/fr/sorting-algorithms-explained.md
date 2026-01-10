---
title: Algorithmes de tri expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T19:05:00.000Z'
originalURL: https://freecodecamp.org/news/sorting-algorithms-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc5740569d1a4ca3988.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: Algorithmes de tri expliqués
seo_desc: 'Sorting algorithms are a set of instructions that take an array or list
  as an input and arrange the items into a particular order.

  Sorts are most commonly in numerical or a form of alphabetical (called lexicographical)
  order, and can be in ascending ...'
---

Les algorithmes de tri sont un ensemble d'instructions qui prennent un tableau ou une liste en entrée et organisent les éléments dans un ordre particulier.

Les tris sont le plus souvent numériques ou sous une forme alphabétique (appelée ordre lexicographique), et peuvent être en ordre croissant (A-Z, 0-9) ou décroissant (Z-A, 9-0).

### **Pourquoi les algorithmes de tri sont importants**

Puisque le tri peut souvent réduire la complexité d'un problème, c'est un algorithme important en informatique. Ces algorithmes ont des applications directes dans les algorithmes de recherche, les algorithmes de base de données, les méthodes de division et de conquête, les algorithmes de structure de données, et bien d'autres.

### **Quelques algorithmes de tri courants**

Certains des algorithmes de tri les plus courants sont :

* Tri par sélection
* Tri à bulles
* Tri par insertion
* Tri fusion
* Tri rapide
* Tri par tas
* Tri par comptage
* Tri par base
* Tri par compartiment

### **Classification des algorithmes de tri**

Les algorithmes de tri peuvent être classés en fonction des paramètres suivants :

1. Basé sur le nombre d'échanges ou d'inversions : il s'agit du nombre de fois où l'algorithme échange des éléments pour trier l'entrée. Le `Tri par sélection` nécessite le nombre minimal d'échanges.
2. Basé sur le nombre de comparaisons : il s'agit du nombre de fois où l'algorithme compare des éléments pour trier l'entrée. En utilisant la [notation Big-O](https://guide.freecodecamp.org/computer-science/notation/big-o-notation/), les exemples d'algorithmes de tri listés ci-dessus nécessitent au moins `O(nlogn)` comparaisons dans le meilleur des cas et `O(n^2)` comparaisons dans le pire des cas pour la plupart des résultats.
3. Basé sur la récursivité ou la non-récursivité : certains algorithmes de tri, comme le `Tri rapide`, utilisent des techniques récursives pour trier l'entrée. D'autres algorithmes de tri, comme le `Tri par sélection` ou le `Tri par insertion`, utilisent des techniques non récursives. Enfin, certains algorithmes de tri, comme le `Tri fusion`, utilisent à la fois des techniques récursives et non récursives pour trier l'entrée.
4. Basé sur la stabilité : les algorithmes de tri sont dits `stables` si l'algorithme maintient l'ordre relatif des éléments avec des clés égales. En d'autres termes, deux éléments équivalents restent dans le même ordre dans la sortie triée qu'ils étaient dans l'entrée.
5. Le `Tri par insertion`, le `Tri fusion` et le `Tri à bulles` sont stables.
6. Le `Tri par tas` et le `Tri rapide` ne sont pas stables.
7. Basé sur l'exigence d'espace supplémentaire : les algorithmes de tri sont dits `en place` s'ils nécessitent un espace supplémentaire constant `O(1)` pour le tri.
8. Le `Tri par insertion` et le `Tri rapide` sont des tris `en place` car nous déplaçons les éléments autour du pivot et n'utilisons pas réellement un tableau séparé, ce qui n'est PAS le cas dans le tri fusion où la taille de l'entrée doit être allouée au préalable pour stocker la sortie pendant le tri.
9. Le `Tri fusion` est un exemple de tri `hors place` car il nécessite un espace mémoire supplémentaire pour ses opérations.

### **Meilleure complexité temporelle possible pour tout tri basé sur la comparaison**

Tout algorithme de tri basé sur la comparaison doit effectuer au moins nLog2n comparaisons pour trier le tableau d'entrée, et le tri par tas et le tri fusion sont des tris par comparaison asymptotiquement optimaux. Cela peut être facilement prouvé en dessinant le diagramme de l'arbre de décision.