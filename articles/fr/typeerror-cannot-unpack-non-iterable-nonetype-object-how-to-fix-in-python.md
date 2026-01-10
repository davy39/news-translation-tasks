---
title: 'Typeerror: cannot unpack non-iterable nonetype object – Comment le corriger
  en Python'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-18T19:50:05.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cannot-unpack-non-iterable-nonetype-object-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/markus-spiske-iar-afB0QQw-unsplash.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'Typeerror: cannot unpack non-iterable nonetype object – Comment le corriger
  en Python'
seo_desc: "When you're working with iterable objects like Lists, Sets, and Tuples\
  \ in Python, you might want to assign the items in these objects to individual variables.\
  \ This is a process known as unpacking. \nDuring the process of unpacking items\
  \ in iterable ob..."
---

Lorsque vous travaillez avec des objets itérables comme les listes, les ensembles et les tuples en Python, vous pouvez souhaiter assigner les éléments de ces objets à des variables individuelles. Ce processus est connu sous le nom de dépaquetage. 

Lors du processus de dépaquetage des éléments dans des objets itérables, vous pouvez obtenir une erreur qui dit : "TypeError: cannot unpack non-iterable NoneType object".

Cette erreur se produit principalement lorsque vous essayez d'assigner un objet de type `None` à un ensemble de variables individuelles. Cela peut sembler confus pour le moment, mais cela sera beaucoup plus clair une fois que nous verrons quelques exemples. 

Avant cela, parlons de certains des termes clés vus dans le message d'erreur. Nous discuterons des termes suivants : TypeError, unpacking et NoneType.

## Qu'est-ce qu'un TypeError en Python ?

Un TypeError en Python se produit lorsque des types de données incompatibles sont utilisés dans une opération. 

Un exemple de TypeError, comme vous le verrez dans les exemples des sections suivantes, est l'utilisation d'un type de données `None` et d'un objet itérable dans une opération. 

## Qu'est-ce que le dépaquetage en Python ?

Pour expliquer le dépaquetage, vous devez comprendre ce que signifie l'emballage. 

Lorsque vous créez une liste avec des éléments en Python, vous avez "emballé" ces éléments dans une seule structure de données. Voici un exemple :

```python
noms = ["John", "Jane", "Doe"]
```

Dans le code ci-dessus, nous avons emballé "John", "Jane" et "Doe" dans une liste appelée `noms`. 

Pour dépaqueter ces éléments, nous devons assigner chaque élément à une variable individuelle. Voici comment :

```python
noms = ["John", "Jane", "Doe"]

a, b, c = noms

print(a, b, c)
# John Jane Doe
```

Puisque nous avons créé la liste `noms`, nous pouvons facilement dépaqueter la liste en créant de nouvelles variables et en les assignant à la liste : `a, b, c = noms`.

Ainsi, `a` prendra le premier élément de la liste, `b` le deuxième et `c` le troisième. C'est-à-dire :

`a` = "John"  
`b` = "Jane"  
`c` = "Doe"

## Qu'est-ce que NoneType en Python ?

NoneType en Python est un type de données qui indique simplement qu'un objet n'a pas de valeur/une valeur de `None`. 

Vous pouvez assigner la valeur `None` à une variable, mais il existe également des méthodes qui retournent `None`. 

Nous allons traiter la méthode `sort()` en Python car elle est le plus souvent associée à l'erreur "TypeError: cannot unpack non-iterable NoneType object". Cela est dû au fait que la méthode retourne une valeur de `None`. 

Ensuite, nous verrons un exemple qui déclenche l'erreur "TypeError: cannot unpack non-iterable NoneType object".

## Exemple d'erreur "TypeError: cannot unpack non-iterable NoneType object"

Dans cette section, vous comprendrez pourquoi nous obtenons une erreur en utilisant la méthode `sort()` incorrectement avant de dépaqueter une liste.

```python
noms = ["John", "Jane", "Doe"]

noms = noms.sort()

a, b, c = noms

print(a, b, c)
# TypeError: cannot unpack non-iterable NoneType object
```

Dans l'exemple ci-dessus, nous avons essayé de trier la liste `noms` par ordre croissant en utilisant la méthode `sort()`.

Après cela, nous avons continué à dépaqueter la liste. Mais lorsque nous avons imprimé les nouvelles variables, nous avons obtenu une erreur. 

Cela nous amène au dernier terme important du message d'erreur : `non-iterable`. Après le tri, la liste `noms` est devenue un objet `None` et non une liste (un objet itérable).

Cette erreur a été déclenchée parce que nous avons assigné `noms.sort()` à `noms`. Puisque `noms.sort()` retourne `None`, nous avons écrasé et assigné `None` à une variable qui était auparavant une liste. C'est-à-dire :

`noms` = `noms.sort()`   
mais `noms.sort()` = `None`  
donc `noms` = `None`

Ainsi, le message d'erreur essaie de vous dire qu'il n'y a rien à l'intérieur d'un objet `None` à dépaqueter. 

Cela est assez facile à corriger. Nous le ferons dans la section suivante.

## Comment corriger l'erreur "TypeError: Cannot Unpack Non-iterable NoneType Object" en Python

Cette erreur a été déclenchée parce que nous avons essayé de dépaqueter un objet `None`. La solution la plus simple est de ne pas assigner `noms.sort()` comme nouvelle valeur de votre liste. 

En Python, vous pouvez utiliser la méthode `sort()` sur une collection de variables sans avoir besoin de réassigner le résultat de l'opération à la collection triée. 

Voici une solution au problème :

```python
noms = ["John", "Jane", "Doe"]

noms.sort()

a, b, c = noms

print(a, b, c)
Doe Jane John
```

Tout fonctionne parfaitement maintenant. La liste a été triée et dépaquetée. 

Tout ce que nous avons changé est `noms.sort()` au lieu d'utiliser `noms` = `noms.sort()`.

Maintenant, lorsque la liste est dépaquetée, `a, b, c` seront assignés aux éléments de `noms` par ordre croissant. C'est-à-dire :

`a` = "Doe"  
`b` = "Jane"  
`c` = "John"

## Résumé

Dans cet article, nous avons parlé de l'erreur "TypeError: cannot unpack non-iterable NoneType object" en Python. 

Nous avons expliqué les termes clés vus dans le message d'erreur : TypeError, unpacking, NoneType et non-iterable.

Nous avons ensuite vu quelques exemples. Le premier exemple a montré comment l'erreur pouvait être déclenchée en utilisant `sort()` incorrectement, tandis que le deuxième exemple a montré comment corriger l'erreur.

Bien que la correction de l'erreur "TypeError: cannot unpack non-iterable NoneType object" ait été facile, comprendre les termes importants du message d'erreur est crucial. Cela aide non seulement à résoudre cette erreur particulière, mais aussi à comprendre et à résoudre des erreurs avec des termes similaires. 

Bon codage !