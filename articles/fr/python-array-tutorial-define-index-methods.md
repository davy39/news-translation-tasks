---
title: Tutoriel sur les tableaux Python – Définir, Indexer, Méthodes
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-31T18:35:31.000Z'
originalURL: https://freecodecamp.org/news/python-array-tutorial-define-index-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/sergey-zolkin-_UeY8aTI6d0-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: Tutoriel sur les tableaux Python – Définir, Indexer, Méthodes
seo_desc: 'In this article, you''ll learn how to use Python arrays. You''ll see how
  to define them and the different methods commonly used for performing operations
  on them.

  The article covers arrays that you create by importing the array module. We won''t
  cover N...'
---

Dans cet article, vous apprendrez à utiliser les tableaux Python. Vous verrez comment les définir et les différentes méthodes couramment utilisées pour effectuer des opérations sur eux.

L'article couvre les tableaux que vous créez en important le `module array`. Nous n'aborderons pas les tableaux NumPy ici.

## Table des matières

1. [Introduction aux tableaux](#introduction)
    1. [Les différences entre les listes et les tableaux](#differences)
    2. [Quand utiliser les tableaux](#usage1)
2. [Comment utiliser les tableaux](#usage2)
    1. [Définir les tableaux](#define)
    2. [Trouver la longueur des tableaux](#length)
    3. [Indexation des tableaux](#indexing)
    4. [Rechercher dans les tableaux](#search)
    5. [Parcourir les tableaux](#loop)
    6. [Découper un tableau](#slice)
3. [Méthodes de tableau pour effectuer des opérations](#methods)
    1. [Changer une valeur existante](#change)
    2. [Ajouter une nouvelle valeur](#addition)
    3. [Supprimer une valeur](#remove)
4. [Conclusion](#conclusion)


Commençons !

## Qu'est-ce que les tableaux Python ? <a name="introduction"></a>

Les tableaux sont une structure de données fondamentale et une partie importante de la plupart des langages de programmation. En Python, ce sont des conteneurs capables de stocker plus d'un élément en même temps.

Plus précisément, ils sont une collection ordonnée d'éléments où chaque valeur est du même type de données. C'est la chose la plus importante à retenir sur les tableaux Python - le fait qu'ils ne peuvent contenir qu'une séquence de plusieurs éléments qui sont du même type.


### Quelle est la différence entre les listes Python et les tableaux Python ? <a name="differences"></a>

Les listes sont l'une des structures de données les plus courantes en Python et une partie centrale du langage.

Les listes et les tableaux se comportent de manière similaire.

Tout comme les tableaux, les listes sont une séquence ordonnée d'éléments.

Elles sont également mutables et non fixes en taille, ce qui signifie qu'elles peuvent grandir et rétrécir tout au long de la vie du programme. Des éléments peuvent être ajoutés et supprimés, ce qui les rend très flexibles à utiliser.

Cependant, les listes et les tableaux ne sont **pas** la même chose.

Les **listes** stockent des éléments de **divers types de données**. Cela signifie qu'une liste peut contenir des entiers, des nombres à virgule flottante, des chaînes de caractères, ou tout autre type de données Python, en même temps. Ce n'est pas le cas avec les tableaux.

Comme mentionné dans la section précédente, les **tableaux** stockent uniquement des éléments qui sont d'un **seul et même type de données**. Il existe des tableaux qui ne contiennent que des entiers, ou uniquement des nombres à virgule flottante, ou uniquement tout autre type de données Python que vous souhaitez utiliser.

### Quand utiliser les tableaux Python <a name="usage1"></a>

Les listes sont intégrées au langage de programmation Python, alors que les tableaux ne le sont pas. Les tableaux ne sont pas une structure de données intégrée et doivent donc être importés via le `module array` afin d'être utilisés.

Les tableaux du `module array` sont une fine enveloppe autour des tableaux C et sont utiles lorsque vous souhaitez travailler avec des données homogènes.

Ils sont également plus compacts et prennent moins de mémoire et d'espace, ce qui les rend plus efficaces en termes de taille par rapport aux listes.

Si vous souhaitez effectuer des calculs mathématiques, vous devez utiliser les tableaux NumPy en important le package NumPy. Mis à part cela, vous devriez simplement utiliser les tableaux Python lorsque vous en avez vraiment besoin, car les listes fonctionnent de manière similaire et sont plus flexibles à utiliser.

## Comment utiliser les tableaux en Python <a name="usage2"></a>

Pour créer des tableaux Python, vous devrez d'abord importer le `module array` qui contient toutes les fonctions nécessaires.

Il existe trois façons d'importer le `module array` :

1) En utilisant `import array` en haut du fichier. Cela inclut le module `array`. Vous créerez ensuite un tableau en utilisant `array.array()`.

```python
import array

#comment créer un tableau
array.array()
```

2) Au lieu de devoir taper `array.array()` tout le temps, vous pourriez utiliser `import array as arr` en haut du fichier, au lieu de `import array` seul. Vous créerez ensuite un tableau en tapant `arr.array()`. Le `arr` agit comme un nom d'alias, avec le constructeur de tableau suivant immédiatement.

```python
import array as arr

#comment créer un tableau
arr.array()
```

3) Enfin, vous pourriez également utiliser `from array import *`, avec `*` important toutes les fonctionnalités disponibles. Vous créerez ensuite un tableau en écrivant simplement le constructeur `array()`.

```python
from array import *

#comment créer un tableau
array()
```

### Comment définir les tableaux en Python <a name="define"></a>

Une fois que vous avez importé le `module array`, vous pouvez ensuite définir un tableau Python.

La syntaxe générale pour créer un tableau ressemble à ceci :

```python
nom_variable = array(typecode,[éléments])
```

Décortiquons cela :

- `nom_variable` serait le nom du tableau.
- Le `typecode` spécifie quel type d'éléments serait stocké dans le tableau. Qu'il s'agisse d'un tableau d'entiers, d'un tableau de flottants ou d'un tableau de tout autre type de données Python. Rappelez-vous que tous les éléments doivent être du même type de données.
- Entre crochets, vous mentionnez les `éléments` qui seraient stockés dans le tableau, chaque élément étant séparé par une virgule. Vous pouvez également créer un tableau *vide* en écrivant simplement `nom_variable = array(typecode)` seul, sans aucun élément.

Ci-dessous se trouve un tableau de typecode, avec les différents typecodes qui peuvent être utilisés avec les différents types de données lors de la définition des tableaux Python :

| Typecode      | Type C | Type Python | Taille |
| ----------- | ----------- |----------- |----------- |
| 'b'      | signed char   | int | 1 |
| 'B'  | unsigned char        | int | 1|
| 'u' | wchar_t | Caractère Unicode | 2 |
| 'h' | signed short| int | 2 |
| 'H' | unsigned short | int| 2|
| 'i'| signed int| int| 2|
| 'I'| unsigned int| int| 2|
| 'l'| signed long | int| 4|
| 'L'| unsigned long| int| 4|
| 'q'|signed long long| int | 8|
|'Q'| unsigned long long| int| 8|
| 'f'| float| float| 4|
| 'd'| double| float| 8|

En mettant tout ensemble, voici un exemple de la façon dont vous définiriez un tableau en Python :

```python
import array as arr 

nombres = arr.array('i',[10,20,30])


print(nombres)

#sortie

#array('i', [10, 20, 30])
```

Décortiquons cela :

- Tout d'abord, nous avons inclus le module array, dans ce cas avec `import array as arr`.
- Ensuite, nous avons créé un tableau `nombres`.
- Nous avons utilisé `arr.array()` à cause de `import array as arr`.
- À l'intérieur du constructeur `array()`, nous avons d'abord inclus `i`, pour entier signé. Entier signé signifie que le tableau peut inclure des valeurs positives *et* négatives. Entier non signé, avec `H` par exemple, signifierait qu'aucune valeur négative n'est autorisée.
- Enfin, nous avons inclus les valeurs à stocker dans le tableau entre crochets.

Gardez à l'esprit que si vous essayiez d'inclure des valeurs qui n'étaient pas du typecode `i`, c'est-à-dire qu'elles n'étaient pas des valeurs entières, vous obtiendriez une erreur :

```python
import array as arr 

nombres = arr.array('i',[10.0,20,30])


print(nombres)

#sortie

#Traceback (most recent call last):
# File "/Users/dionysialemonaki/python_articles/demo.py", line 14, in <module>
#   nombres = arr.array('i',[10.0,20,30])
#TypeError: 'float' object cannot be interpreted as an integer
```

Dans l'exemple ci-dessus, j'ai essayé d'inclure un nombre à virgule flottante dans le tableau. J'ai obtenu une erreur car il s'agit d'un tableau d'entiers uniquement.

Une autre façon de créer un tableau est la suivante :

```python
from array import *

#un tableau de valeurs à virgule flottante
nombres = array('d',[10.0,20.0,30.0])

print(nombres)

#sortie

#array('d', [10.0, 20.0, 30.0])
```

L'exemple ci-dessus a importé le `module array` via `from array import *` et a créé un tableau `nombres` de type de données float. Cela signifie qu'il ne contient que des nombres à virgule flottante, ce qui est spécifié avec le typecode `'d'`.

### Comment trouver la longueur d'un tableau en Python <a name="length"></a>

Pour connaître le nombre exact d'éléments contenus dans un tableau, utilisez la méthode intégrée `len()`.

Elle retournera le nombre entier qui est égal au nombre total d'éléments dans le tableau que vous spécifiez.

```python
import array as arr 

nombres = arr.array('i',[10,20,30])


print(len(nombres))

#sortie
# 3
```

Dans l'exemple ci-dessus, le tableau contenait trois éléments – `10, 20, 30` – donc la longueur de `nombres` est `3`.

### Indexation des tableaux et comment accéder aux éléments individuels dans un tableau en Python <a name="indexing"></a>

Chaque élément dans un tableau a une adresse spécifique. Les éléments individuels sont accessibles en référençant leur *numéro d'index*.

L'indexation en Python, et dans tous les langages de programmation et l'informatique en général, commence à `0`. Il est important de se souvenir que le comptage commence à `0` et **pas** à `1`.

Pour accéder à un élément, vous écrivez d'abord le nom du tableau suivi de crochets. À l'intérieur des crochets, vous incluez le numéro d'index de l'élément.

La syntaxe générale ressemblerait à ceci :

```python
nom_tableau[valeur_index_élément]
```

Voici comment vous accéderiez à chaque élément individuel dans un tableau :

```python
import array as arr 

nombres = arr.array('i',[10,20,30])

print(nombres[0]) # obtient le 1er élément
print(nombres[1]) # obtient le 2ème élément
print(nombres[2]) # obtient le 3ème élément

#sortie

#10
#20
#30
```

Rappelez-vous que la valeur d'index du dernier élément d'un tableau est toujours un de moins que la longueur du tableau. Où `n` est la longueur du tableau, `n - 1` sera la valeur d'index du dernier élément.

Notez que vous pouvez également accéder à chaque élément individuel en utilisant l'indexation négative.

Avec l'indexation négative, le dernier élément aurait un index de `-1`, l'avant-dernier élément aurait un index de `-2`, et ainsi de suite.

Voici comment vous obtiendriez chaque élément dans un tableau en utilisant cette méthode :

```python
import array as arr 

nombres = arr.array('i',[10,20,30])

print(nombres[-1]) #obtient le dernier élément
print(nombres[-2]) #obtient l'avant-dernier élément
print(nombres[-3]) #obtient le premier élément
 
#sortie

#30
#20
#10
```

### Comment rechercher dans un tableau en Python <a name="search"></a>

Vous pouvez trouver le numéro d'index d'un élément en utilisant la méthode `index()`.

Vous passez la valeur de l'élément recherché comme argument à la méthode, et le numéro d'index de l'élément est retourné.

```python
import array as arr 

nombres = arr.array('i',[10,20,30])

#rechercher l'index de la valeur 10
print(nombres.index(10))

#sortie

#0
```

S'il y a plus d'un élément avec la même valeur, l'index de la première instance de la valeur sera retourné :

```python
import array as arr 


nombres = arr.array('i',[10,20,30,10,20,30])

#rechercher l'index de la valeur 10
#retournera le numéro d'index de la première instance de la valeur 10
print(nombres.index(10))

#sortie

#0
```

### Comment parcourir un tableau en Python <a name="loop"></a>

Vous avez vu comment accéder à chaque élément individuel dans un tableau et l'imprimer seul.

Vous avez également vu comment imprimer le tableau, en utilisant la méthode `print()`. Cette méthode donne le résultat suivant :

```python
import array as arr 

nombres = arr.array('i',[10,20,30])

print(nombres)

#sortie

#array('i', [10, 20, 30])
```

Et si vous voulez imprimer chaque valeur une par une ?

C'est là qu'une boucle est utile. Vous pouvez parcourir le tableau et imprimer chaque valeur, une par une, avec chaque itération de boucle.

Pour cela, vous pouvez utiliser une simple boucle `for` :

```python
import array as arr 

nombres = arr.array('i',[10,20,30])

for nombre in nombres:
    print(nombre)
    
#sortie
#10
#20
#30
```

Vous pourriez également utiliser la fonction `range()`, et passer la méthode `len()` comme paramètre. Cela donnerait le même résultat que ci-dessus :

```python
import array as arr  

valeurs = arr.array('i',[10,20,30])

#imprime chaque valeur individuelle dans le tableau
for valeur in range(len(valeurs)):
    print(valeurs[valeur])

#sortie

#10
#20
#30
```

### Comment découper un tableau en Python <a name="slice"></a>

Pour accéder à une plage spécifique de valeurs à l'intérieur du tableau, utilisez l'opérateur de découpage, qui est un deux-points `:`.

Lorsque vous utilisez l'opérateur de découpage et que vous n'incluez qu'une seule valeur, le comptage commence par `0` par défaut. Il obtient le premier élément et va jusqu'à, mais sans inclure, le numéro d'index que vous spécifiez.

```python

import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])

#obtenir les valeurs 10 et 20 uniquement
print(nombres[:2])  #première à deuxième position

#sortie

#array('i', [10, 20])
```

Lorsque vous passez deux nombres comme arguments, vous spécifiez une plage de nombres. Dans ce cas, le comptage commence à la position du premier nombre dans la plage, et jusqu'à, mais sans inclure, le deuxième :

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])


#obtenir les valeurs 20 et 30 uniquement
print(nombres[1:3]) #deuxième à troisième position

#sortie

#array('i', [20, 30])
```

## Méthodes pour effectuer des opérations sur les tableaux en Python <a name="methods"></a>

Les tableaux sont mutables, ce qui signifie qu'ils sont modifiables. Vous pouvez changer la valeur des différents éléments, en ajouter de nouveaux, ou supprimer ceux que vous ne voulez plus dans votre programme.

Voyons certaines des méthodes les plus couramment utilisées pour effectuer des opérations sur les tableaux.

### Comment changer la valeur d'un élément dans un tableau <a name="change"></a>

Vous pouvez changer la valeur d'un élément spécifique en spécifiant sa position et en lui attribuant une nouvelle valeur :

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])

#changer le premier élément
#changer sa valeur de 10 à 40
nombres[0] = 40

print(nombres)

#sortie

#array('i', [40, 20, 30])
```

### Comment ajouter une nouvelle valeur à un tableau <a name="addition"></a>

Pour ajouter une seule valeur à la fin d'un tableau, utilisez la méthode `append()` :

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])

#ajouter l'entier 40 à la fin de nombres
nombres.append(40)

print(nombres)

#sortie

#array('i', [10, 20, 30, 40])
```

Soyez conscient que le nouvel élément que vous ajoutez doit être du même type de données que le reste des éléments du tableau.

Regardez ce qui se passe lorsque j'essaie d'ajouter un flottant à un tableau d'entiers :

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])

#ajouter le flottant 40.0 à la fin de nombres
nombres.append(40.0)

print(nombres)

#sortie

#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 19, in <module>
#   nombres.append(40.0)
#TypeError: 'float' object cannot be interpreted as an integer
```


Mais que faire si vous voulez ajouter plus d'une valeur à la fin d'un tableau ?

Utilisez la méthode `extend()`, qui prend un itérable (comme une liste d'éléments) comme argument. Encore une fois, assurez-vous que les nouveaux éléments sont tous du même type de données.

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])

#ajouter les entiers 40,50,60 à la fin de nombres
#Les nombres doivent être enfermés dans des crochets

nombres.extend([40,50,60])

print(nombres)

#sortie

#array('i', [10, 20, 30, 40, 50, 60])
```

Et si vous ne voulez pas ajouter un élément à la fin d'un tableau ? Utilisez la méthode `insert()`, pour ajouter un élément à une position spécifique.

La fonction `insert()` prend deux arguments : le numéro d'index de la position où le nouvel élément sera inséré, et la valeur du nouvel élément.

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])

#ajouter l'entier 40 à la première position
#rappellez-vous que l'indexation commence à 0

nombres.insert(0,40)

print(nombres)

#sortie

#array('i', [40, 10, 20, 30])
```

### Comment supprimer une valeur d'un tableau <a name="remove"></a>

Pour supprimer un élément d'un tableau, utilisez la méthode `remove()` et incluez la valeur comme argument de la méthode.

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30])

nombres.remove(10)

print(nombres)

#sortie

#array('i', [20, 30])
```

Avec `remove()`, seule la première instance de la valeur que vous passez comme argument sera supprimée.

Voyez ce qui se passe lorsqu'il y a plus d'une valeur identique :

```python

import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30,10,20])

nombres.remove(10)

print(nombres)

#sortie

#array('i', [20, 30, 10, 20])
```

Seule la première occurrence de `10` est supprimée.

Vous pouvez également utiliser la méthode `pop()`, et spécifier la position de l'élément à supprimer :

```python
import array as arr 

#tableau original
nombres = arr.array('i',[10,20,30,10,20])

#supprimer la première instance de 10
nombres.pop(0)

print(nombres)

#sortie

#array('i', [20, 30, 10, 20])
```

## Conclusion <a name="conclusion"></a>

Et voilà - vous connaissez maintenant les bases de la création de tableaux en Python en utilisant le `module array`. Espérons que vous avez trouvé ce guide utile.

Pour en savoir plus sur Python, consultez la [Certification en Calcul Scientifique avec Python de freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !

Références : [Documentation Python](https://docs.python.org/3/library/array.html)