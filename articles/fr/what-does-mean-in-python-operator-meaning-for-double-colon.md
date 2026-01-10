---
title: 'Que signifie :: en Python ? Signification de l''opérateur double deux-points'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-30T07:21:33.000Z'
originalURL: https://freecodecamp.org/news/what-does-mean-in-python-operator-meaning-for-double-colon
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/nikolai-chernichenko-hFBsF-CX5eQ-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: 'Que signifie :: en Python ? Signification de l''opérateur double deux-points'
seo_desc: 'You can use the double colon (::) in Python to slice or extract elements
  in a collection such as a list or string.

  In this article, you''ll learn the syntax and how to use :: to slice a list in Python.
  You''ll also learn how to use the parameters assoc...'
---

Vous pouvez utiliser les doubles deux-points (`::`) en Python pour découper ou extraire des éléments dans une collection telle qu'une liste ou une chaîne de caractères.

Dans cet article, vous apprendrez la syntaxe et comment utiliser `::` pour découper une liste en Python. Vous apprendrez également comment utiliser les paramètres associés à cette méthode de découpage.

## Syntaxe des doubles deux-points (`::`) en Python

Voici à quoi ressemble la syntaxe des doubles deux-points :

```txt
collection[début:fin:pas]
```

Dans la syntaxe ci-dessus :

* **collection** désigne la collection de données (liste, chaîne, tableau, etc.).
* **début** désigne l'endroit où l'opération de découpage doit commencer.
* **fin** désigne l'endroit où l'opération doit s'arrêter.
* **pas** désigne la séquence d'itération à travers les éléments.

Si vous regardez attentivement la syntaxe, vous pouvez voir comment les deux-points séparent chaque paramètre.

Dans la section suivante, vous verrez des exemples de fonctionnement des paramètres ci-dessus.

### Exemple #1 des doubles deux-points en Python

Dans cet exemple, nous allons nous concentrer sur le paramètre `début` :

```python
liste_de_nombres = [2,4,6,8,10,12]

print(liste_de_nombres[2:])
# [6, 8, 10, 12]
```

Dans l'exemple ci-dessus, nous avons créé une liste appelée `liste_de_nombres` avec ces éléments : [2,4,6,8,10,12].

Nous avons ensuite utilisé le paramètre `début` pour découper la liste à partir du deuxième index : `liste_de_nombres[2:]`.

Voici les index :

2 => index 0  
4 => index 1  
6 => index 2  
8 => index 3  
10 => index 4  
12 => index 5

Rappelons que nous découpons à partir de l'index 2. Ainsi, tous les éléments de l'index 2 à la fin de la liste seront retournés : `[6, 8, 10, 12]`.

Cela revient à dire : "Imprimer tous les éléments de la liste à partir de l'index spécifié." L'index spécifié sera également imprimé.

Notez que le paramètre `début` vient avant le premier deux-points.

### Exemple #2 des doubles deux-points en Python

Dans cette section, vous verrez comment utiliser le paramètre `fin`. Il vient après le premier deux-points et avant le deuxième deux-points.

Contrairement au paramètre `début`, l'index spécifié ne sera pas inclus. L'opération de découpage s'arrêtera à l'index qui précède l'index spécifié.

Voici un exemple :

```python
liste_de_nombres = [2,4,6,8,10,12]

print(liste_de_nombres[:2])
# [2, 4]
```

Similaire à la section précédente, l'index spécifié est 2. Voici les index :

2 => index 0  
4 => index 1  
6 => index 2  
8 => index 3  
10 => index 4  
12 => index 5

En utilisant le paramètre `fin`, vous obtenez tous les éléments de la liste qui viennent avant l'index spécifié.

L'index 2 dans la liste est 6. Les éléments qui viennent avant lui sont 2 et 4, donc ils sont imprimés : `[2, 4]`. Les autres éléments sont "découpés".

### Exemple #3 des doubles deux-points en Python

Le paramètre `pas` fonctionne de manière intéressante. Il est utilisé pour spécifier la séquence à suivre lors du découpage d'une collection.

Le paramètre `pas` vient après le deuxième deux-points.

Sans spécifier de valeurs pour les paramètres `début` et `fin`, vous avez accès à toute la liste. Aucun élément n'est découpé.

Puisque nous avons déjà parlé des paramètres `début` et `fin`, nous ne leur attribuerons aucune valeur. Vous comprendrez mieux le paramètre `pas` si nous travaillons avec tous les éléments de la liste.

```python
liste_de_nombres = [2,4,6,8,10,12]

print(liste_de_nombres[::2])
# [2, 6, 10]
```

Nous avons enfin les deux deux-points proches l'un de l'autre : `liste_de_nombres[::2]`.

Nous avons utilisé une valeur de `pas` de 2. Cela signifie que la liste sautera deux étapes à chaque itération.

Le premier élément est 2. Deux étapes à partir de 2 nous amènent à 6. Deux étapes à partir de 6 nous amènent à 10. Deux étapes à partir de 10 ne nous amènent nulle part car il n'y a pas d'autre élément pour compléter la deuxième étape.

Vous pouvez comparer le paramètre `pas` à monter un escalier. Avec notre exemple de code, vous vous arrêteriez et imprimeriez un élément chaque fois que vous faites deux pas.

## Résumé

Les doubles deux-points (`::`) en Python sont utilisés pour spécifier comment une opération de découpage doit fonctionner. Ils peuvent être utilisés pour découper certaines collections de données.

Dans cet article, nous avons vu comment utiliser les paramètres `début`, `fin` et `pas` pour découper une liste.

Nous avons vu un exemple pour chaque paramètre. Cela a aidé à montrer la différence entre chacun d'eux et comment ils affectent la structure d'une liste.

Bon codage !