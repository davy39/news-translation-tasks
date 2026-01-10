---
title: Un tour rapide mais complet des listes en Python 3 en seulement sept minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T20:29:56.000Z'
originalURL: https://freecodecamp.org/news/a-quick-yet-complete-tour-of-lists-in-python3-in-just-seven-minutes-437e615110d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mqK7gwgzJUsyuhqT
tags:
- name: Data Science
  slug: data-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Un tour rapide mais complet des listes en Python 3 en seulement sept minutes
seo_desc: 'By PALAKOLLU SRI MANIKANTA

  Python lists are not like arrays. They are bit different. When it comes to dealing
  with array’s we talk about a collection of homogeneous data elements. This is not
  true in case of a list in python. Python List can store a ...'
---

Par PALAKOLLU SRI MANIKANTA

Les listes Python ne sont pas comme les tableaux. Elles sont un peu différentes. Lorsqu'il s'agit de traiter des tableaux, nous parlons d'une collection d'éléments de données homogènes. Ce n'est pas le cas pour une liste en Python. Une liste Python peut stocker une collection hétéroclite d'éléments. Cette fonctionnalité aidera les développeurs et les programmeurs à travailler avec des listes de manière plus flexible. Une liste en Python est l'une des structures de données intégrées les plus puissantes.

Les listes en Python peuvent stocker des entiers, des valeurs flottantes, des chaînes de caractères, des valeurs booléennes et des valeurs complexes également.

#### Comment créer une liste en Python

Nous pouvons créer une liste en Python de deux manières

1. En déclarant une variable avec des crochets vides, c'est-à-dire []
2. En utilisant list().

**Exemple**

```
# Ici, je crée d'abord ma liste de tâches qui est utilisée pour stocker mes activités à faire.
```

```
myTODOList = []
```

```
# La ligne ci-dessus créera un objet liste pour moi# Je crée une autre liste qui stockera mes informations générales.
```

```
myGeneralInfo = list()
```

```
# La ligne ci-dessus créera également un objet liste pour moi# Obtenir les types d'objets liste
```

```
print(type(myTODOList))print(type(myGeneralInfo))
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/7qXRlOZ6ZFueYQAoN2P3q-CV0ardhjMRNyEc)
_Sortie pour les quelques lignes de code ci-dessus._

C'est incroyable, à ce stade, vous êtes capable de créer un nouvel objet liste avec les méthodes les plus fréquemment utilisées. Maintenant, nous allons avancer sur la manière dont nous pouvons ajouter de nouveaux éléments à notre liste et bien plus encore. Commençons.

#### Comment ajouter des données à notre liste ?

Tout d'abord, je voudrais introduire le concept de mutabilité. La mutabilité signifie la capacité à changer son comportement. Les listes Python sont mutables par nature. Nous pouvons ajouter ou supprimer des éléments de la liste. C'est l'un des plus grands avantages qui attire les programmeurs à travailler avec des listes par rapport à d'autres structures de données intégrées.

Nous pouvons ajouter des éléments à une liste de deux manières :

1. En utilisant append()
2. En utilisant insert()

**En utilisant append()**

Avec l'aide de la méthode append, nous sommes capables d'ajouter un élément à la fois. Cette méthode nous aidera à ajouter des éléments uniquement à la fin de la liste.

> La syntaxe de la fonction append est —

> listName.append(item/element)

```
# Ajout d'éléments aux listes
```

```
myTODOList.append('Se réveiller tôt le matin')myTODOList.append('Aller à la salle de sport')myTODOList.append('Jouer à quelques jeux')myTODOList.append('Se préparer pour aller à l'université')myTODOList.append('Aller à la bibliothèque')
```

```
# Impression de tous les éléments de la liste
```

```
print(myTODOList)
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/MjgtAQob6hxMqOY126H3fOOEkwzA-Yg6jN5a)
_Sortie pour la ligne de code ci-dessus._

**En utilisant insert()**

Cette méthode insert est utilisée pour ajouter les éléments à une position spécifiée dans la liste donnée.

> La syntaxe de la fonction insert est —

> listName.insert(position, item/element)

insert() utilise deux paramètres — position et élément de la liste. La position est l'endroit où l'élément doit être placé dans la liste. Ces positions sont généralement appelées index. Habituellement, l'index de la liste en Python commence à 0. (c'est-à-dire que l'index du premier élément est 0, celui du deuxième élément est 1, celui du troisième élément est 2, et ainsi de suite). De cela, nous pouvons conclure que —

> Une liste de n éléments aura au plus un numéro d'index de n-1, c'est-à-dire qu'une liste avec 5 éléments aura une valeur d'index maximale de 4.

**Exemple**

```
# Ajout d'éléments à notre liste avec l'aide de insert()
```

```
myGeneralInfo.insert(0, 'Payé les frais de bibliothèque')myGeneralInfo.insert(1, 12000)myGeneralInfo.insert(2, True)myGeneralInfo.insert(3, 14+12j)myGeneralInfo.insert(4, 3.141521)
```

```
# Impression des informations de la liste myGeneralInfo
```

```
print(myGeneralInfo)
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/18F43mmcZJKN3VZoBzfNSDdUgFmOtgBsFfcc)
_Sortie pour les quelques lignes de code ci-dessus._

> myGeneralInfo est rempli avec quelques informations aléatoires à des fins d'illustration uniquement.

#### Comment accéder aux éléments de la liste

Nous pouvons accéder à la liste des éléments en utilisant les deux méthodes suivantes :

1. En utilisant un opérateur d'index.
2. En utilisant l'opérateur de tranche

**En utilisant un opérateur d'index**

Nous pouvons accéder directement à nos éléments de liste avec l'aide de l'opérateur d'index.

**Exemple**

```
# Accéder à certaines valeurs de la liste
```

```
print(myTODOList[1])print(myTODOList[3])print(myTODOList[4])
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/WuIkO4Zsn3kDVrgF4u-Q746ADPjTcKbQE09d)
_Sortie pour le programme ci-dessus_

**En utilisant l'opérateur de tranche**

L'opérateur de tranche est l'un des opérateurs les plus couramment utilisés pour accéder efficacement aux éléments de la liste. La syntaxe de l'opérateur de tranche est :

listName[start: stop: step]

start — Il indique l'index où la tranche doit commencer. La valeur par défaut est 0.

stop — Il indique l'index où la tranche doit se terminer. La valeur par défaut est l'index maximum autorisé de la liste, c'est-à-dire la longueur de la liste.

step — Valeur d'incrément. La valeur par défaut est 1.

**Exemple**

```
# Obtenir les informations en utilisant l'opérateur de tranche
```

```
print(myTODOList[0:3])  # nous n'avons pas besoin de spécifier la valeur de step.print(myTODOList[2:4:1])print(myTODOList[0:4:2])
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/xkDOJNvzDYC4j0nSGGKAayqg2D10l5zjncW5)
_Sortie pour les quelques lignes de code ci-dessus._

Les listes Python sont des objets itérables. Pour tout objet itérable en Python, nous pouvons écrire une boucle for pour imprimer toutes les données.

**Exemple**

```
# Itération sur la liste
```

```
for item in myGeneralInfo:      print(item)
```

![Image](https://cdn-media-1.freecodecamp.org/images/dEPU2NUaTN78qTCftaX8AaTtjmCQUACG5n2-)
_Sortie pour les lignes de code ci-dessus._

#### Comment supprimer un élément de la liste

Nous pouvons supprimer les éléments de la liste de deux manières suivantes :

1. En utilisant remove()
2. En utilisant pop()

**En utilisant remove()**

remove() est utilisé pour supprimer l'élément qui lui est spécifié. La syntaxe de remove() est :

listName.remove(item/element)

```
# Suppression de l'élément de la liste
```

```
myGeneralInfo.remove(12000)myGeneralInfo.remove('Payé les frais de bibliothèque')
```

```
# impression du résultat après la suppression des éléments
```

```
print(myGeneralInfo)
```

![Image](https://cdn-media-1.freecodecamp.org/images/Yb8jVI4YWDj-MbWPHqUSqHKq0n0GIqxv3eN6)
_Après la suppression des éléments de la liste, la sortie serait la suivante_

**En utilisant pop()**

C'est une méthode d'itérateur qui est utilisée pour supprimer un ou plusieurs éléments à la fois. Elle supprime les éléments du côté arrière. La syntaxe de la méthode pop() est :

listName.pop()

```
# impression des éléments de la liste avant la suppression
```

```
print('Mes éléments de liste TODO : ',myTODOList)print('Mes éléments de liste générale : ',myGeneralInfo)
```

```
# Suppression des éléments de la liste en utilisant pop()
```

```
myTODOList.pop()myTODOList.pop()
```

```
# Suppression complète des éléments de la liste
```

```
for item in range(len(myGeneralInfo)):       myGeneralInfo.pop()
```

```
# impression des résultats
```

```
print('Mes éléments de liste TODO : ',myTODOList)print('Mes éléments de liste générale : ',myGeneralInfo)
```

![Image](https://cdn-media-1.freecodecamp.org/images/lpkTpT0NkF2ZrpzJaM61ykItaqtEfylrymIC)
_C'est ainsi que nous pouvons supprimer les éléments de la liste en utilisant pop()_

> Dans le programme ci-dessus, nous avons utilisé len() dans la boucle for. len() est utilisé pour donner la longueur de la liste, c'est-à-dire le nombre d'éléments présents dans la liste.

#### Divers attributs et fonctions sur l'objet Liste

La fonction dir() de Python est utilisée pour donner l'ensemble des attributs et méthodes intégrés qui lui sont associés.

**Exemple**

```
# Impression de tous les attributs et fonctions sur l'objet liste
```

```
print(dir(myTODOList))
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/lySJCcD9YPuSHj0xrkOd1QqM3aABCge1iCRs)
_Divers attributs et méthodes sur l'objet liste_

#### Diverses méthodes de liste et leur utilisation :

1. **append() —** Elle ajoutera un élément à la fin de la liste.
2. **clear() —** Elle est utilisée pour supprimer tous les éléments de la liste.
3. **copy() —** Elle est utilisée pour retourner une autre copie de la liste.
4. **count() —** Elle est utilisée pour retourner le compte du nombre d'éléments passés en argument.
5. **extend() —** Elle ajoutera tous les éléments d'une liste à une autre liste.
6. **index() —** Elle est utilisée pour retourner l'index du premier élément correspondant.
7. **insert() —** Elle est utilisée pour insérer un élément à l'index défini.
8. **pop() —** Elle est utilisée pour supprimer et retourner un élément à l'index donné.
9. **remove() —** Elle est utilisée pour supprimer un élément de la liste.
10. **reverse() —** Elle est utilisée pour inverser l'ordre des éléments dans la liste.
11. **sort() —** Elle est utilisée pour trier les éléments d'une liste par ordre croissant.

#### Quand utiliser la structure de données Liste ?

Si vous souhaitez stocker plusieurs objets de données, l'ordre d'insertion doit être préservé. Si vous souhaitez stocker des valeurs en double également, alors cette structure de données sera plus utile pour effectuer de telles opérations.

J'ai couvert presque tout ce qui est nécessaire pour effectuer tout type d'opération sur la structure de données de liste.

**J'espère que cela vous a aidé à apprendre les listes en Python de manière rapide et facile.**

**Si vous avez aimé cet article, veuillez cliquer sur le bouton d'applaudissements et laissez-moi un commentaire. Veuillez partager avec vos amis.**