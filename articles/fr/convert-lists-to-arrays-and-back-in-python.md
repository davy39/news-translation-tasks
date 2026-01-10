---
title: Comment convertir une liste en tableau et vice versa en Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-04-12T00:04:30.000Z'
originalURL: https://freecodecamp.org/news/convert-lists-to-arrays-and-back-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/dare.JPG
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: Comment convertir une liste en tableau et vice versa en Python
seo_desc: 'Arrays and lists are two of the most commonly used data structures in Python.

  You can use both arrays and lists to store collections of values, but they have
  some key differences.

  For example, arrays are more efficient than lists for certain operatio...'
---

Les tableaux et les listes sont deux des structures de données les plus couramment utilisées en Python.

Vous pouvez utiliser à la fois des tableaux et des listes pour stocker des collections de valeurs, mais ils présentent quelques différences clés.

Par exemple, les tableaux sont plus efficaces que les listes pour certaines opérations, telles que les opérations mathématiques sur de grandes collections de données numériques. Mais les listes sont plus flexibles et plus faciles à utiliser dans de nombreux cas.

Parfois, vous devrez peut-être convertir des tableaux et des listes en Python. Par exemple, vous pouvez avoir des données stockées dans une liste que vous devez passer à une fonction qui nécessite un tableau. Ou vous pouvez avoir un tableau que vous devez manipuler en utilisant des opérations de liste.

Dans cet article, nous allons explorer comment convertir des listes en tableaux et des tableaux en listes en Python.

## Comment convertir une liste en tableau en Python

Pour convertir une liste en tableau en Python, vous pouvez utiliser le module `array` qui fait partie de la bibliothèque standard de Python. Le module `array` fournit un moyen de créer des tableaux de divers types, tels que des entiers signés, des nombres à virgule flottante et même des caractères.

Voici un exemple de la façon de convertir une liste en tableau en Python :

```python
import array

my_list = [1, 2, 3, 4, 5]
my_array = array.array('i', my_list)

print(my_array)
```

Dans ce code, nous importons d'abord le module `array`. Nous créons ensuite une liste appelée `my_list` contenant les valeurs de 1 à 5.

Ensuite, nous créons un tableau appelé `my_array` en appelant la fonction `array()` et en lui passant deux arguments : le code de type `'i'`, qui spécifie que nous voulons un tableau d'entiers signés, et `my_list`, qui est la liste que nous voulons convertir.

Lorsque nous imprimons `my_array`, nous devrions voir la sortie suivante :

```python
array('i', [1, 2, 3, 4, 5])
```

Cela montre que `my_array` est maintenant un tableau contenant les mêmes valeurs que `my_list`.

## Comment convertir un tableau en liste en Python

Pour convertir un tableau en liste, nous pouvons utiliser la fonction intégrée `list()` de Python. Voici un exemple de la façon de convertir un tableau en liste en Python :

```python
import array

my_array = array.array('i', [1, 2, 3, 4, 5])
my_list = list(my_array)

print(my_list)
```

Dans ce code, nous créons d'abord un tableau appelé `my_array` contenant les valeurs de 1 à 5. Ensuite, nous créons une liste appelée `my_list` en appelant la fonction `list()` et en lui passant `my_array`.

Lorsque nous imprimons `my_list`, nous devrions voir la sortie suivante :

```python
[1, 2, 3, 4, 5]
```

Cela montre que `my_list` est maintenant une liste contenant les mêmes valeurs que `my_array`.

## Conclusion

Dans cet article, nous avons exploré comment convertir des tableaux et des listes en Python. Vous avez appris que vous pouvez utiliser le module `array` pour créer des tableaux de divers types et la fonction `list()` pour convertir des tableaux en listes.

La conversion entre tableaux et listes peut être utile dans de nombreuses situations, par exemple lorsque vous devez passer des données entre des fonctions ou lorsque vous devez manipuler des données en utilisant des opérations de liste. En comprenant comment convertir des tableaux et des listes, vous pouvez travailler plus efficacement avec des données en Python.

Restons en contact sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).