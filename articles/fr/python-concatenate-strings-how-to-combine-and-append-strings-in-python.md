---
title: Python Concatenation de Chaînes – Comment Combiner et Ajouter des Chaînes en
  Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-11T17:19:31.000Z'
originalURL: https://freecodecamp.org/news/python-concatenate-strings-how-to-combine-and-append-strings-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/join.jpg
tags:
- name: Python
  slug: python
seo_title: Python Concatenation de Chaînes – Comment Combiner et Ajouter des Chaînes
  en Python
seo_desc: "When you're learning a programming language, you're likely to come across\
  \ a data type called a string. A string usually contains a series of characters\
  \ nested in quotation marks that can be represented as a text. \nIn this article,\
  \ we will talk about ..."
---

Lorsque vous apprenez un langage de programmation, vous êtes susceptible de rencontrer un type de données appelé chaîne de caractères. Une chaîne contient généralement une série de caractères imbriqués entre des guillemets qui peuvent être représentés sous forme de texte.

Dans cet article, nous allons parler de la concaténation de chaînes en Python. Il s'agit du processus de jonction/ajout d'une chaîne à une autre. Par exemple, la concaténation de "freeCode" et "Camp" donne "freeCodeCamp".

La concaténation de chaînes est importante lorsque vous travaillez avec deux ou plusieurs variables distinctes (chaînes) qui sont combinées pour former une chaîne beaucoup plus grande.

Cela vous permet également d'avoir des unités séparées d'une chaîne même après les avoir combinées, au cas où vous auriez besoin d'utiliser une variable de chaîne ailleurs dans votre code et non la chaîne entière.

## Comment Concaténer des Chaînes en Python

Pour concaténer des chaînes en Python, nous utilisons l'opérateur `+` pour ajouter les chaînes les unes aux autres. Voici un exemple :

```python
x = "Happy"
y = "Coding"
z = x + y
print(z)
#HappyCoding
```

Dans le code ci-dessus, nous avons créé deux variables (`x` et `y`) contenant toutes deux des chaînes – "Happy" et "Coding" – et une troisième variable (`z`) qui combine les deux variables que nous avons créées initialement.

Nous avons pu combiner les deux variables en utilisant l'opérateur `+`. Notre sortie après cela était `HappyCoding`. Si vous inversiez l'ordre lors de la concaténation en faisant ceci : `z = y + x`, alors nous obtiendrions `CodingHappy` imprimé dans la console.

## Comment Ajouter des Espaces Entre les Chaînes Concaténées

Vous avez peut-être remarqué qu'il n'y avait pas d'espace entre les variables lors de l'impression. Voici comment nous pouvons ajouter des espaces entre les chaînes concaténées :

```python
x = "Happy"
y = "Coding"
z = x + " " + y
print(z)
# Happy Coding
```

Vous remarquerez qu'il y a un espace entre les guillemets. Si vous omettez l'espace, les chaînes seront toujours étroitement jointes.

Vous pouvez également ajouter des espaces à la fin d'une chaîne lors de sa création et cela sera appliqué lors de l'impression. Voici comment procéder :

```python
x = "Happy "
y = "Coding"
z = x + y
print(z)
#Happy Coding
```

## Comment Créer Plusieurs Copies d'une Chaîne en Utilisant l'Opérateur `*`

Lorsque nous utilisons l'opérateur `*` sur une chaîne, selon la valeur passée, nous créons et concaténons (ajoutons) des copies de la chaîne. Voici un exemple :

```python
x = "Happy"
y = x * 3
print(y)
# HappyHappyHappy
```

En utilisant l'opérateur `*`, nous avons dupliqué la valeur de la chaîne "Happy" trois fois avec les trois valeurs imprimées étroitement regroupées.

Si nous ajoutions un espace à la fin de la chaîne, alors les chaînes seraient séparées. C'est-à-dire :

```
x = "Happy "
y = x * 3
print(y)
# Happy Happy Happy
```

## Conclusion

Dans cet article, nous avons appris comment combiner des chaînes en Python par concaténation.

Merci d'avoir lu et bon codage !