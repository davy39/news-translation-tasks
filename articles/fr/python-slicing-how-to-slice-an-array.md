---
title: Découpage Python – Comment découper un tableau et que signifie [::-1] ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-08T19:13:33.000Z'
originalURL: https://freecodecamp.org/news/python-slicing-how-to-slice-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/10.-slide-array.png
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: Découpage Python – Comment découper un tableau et que signifie [::-1] ?
seo_desc: 'By Dillion Megida

  Slicing an array is the concept of cutting out – or slicing out – a part of the
  array. How do you do this in Python? I''ll show you how in this article.

  If you like watching video content to supplement your reading, here''s a video ve...'
---

Par Dillion Megida

Découper un tableau est le concept de découper – ou de trancher – une partie du tableau. Comment faire cela en Python ? Je vais vous montrer comment dans cet article.

Si vous aimez regarder du contenu vidéo pour compléter votre lecture, voici une [version vidéo](https://www.youtube.com/watch?v=sgXInOpc4Iw) de cet article également.


## Qu'est-ce qu'un tableau ?

Un tableau est une structure de données qui vous permet de stocker plusieurs éléments **du même type de données** dans l'ordre dans une variable en même temps. Vous pouvez accéder à chacun de ces éléments par leur index (emplacement dans l'ordre).

Ils sont un peu similaires aux listes en Python, sauf que les listes vous permettent de stocker plusieurs éléments **de différents types de données**. De plus, tandis que les listes sont intégrées, les tableaux ne le sont pas.

## Comment accéder aux valeurs dans un tableau en Python

Voici la syntaxe pour créer un tableau en Python :

```python
import array as arr 

nombres = arr.array(typecode, [valeurs])
```

Comme le type de données tableau n'est pas intégré par défaut dans Python, vous devez l'importer depuis le module `array`. Nous importons ce module en tant que `arr`.

En utilisant la méthode `array` de `arr`, nous pouvons créer un tableau en spécifiant un `typecode` (type de données des valeurs) et les valeurs stockées dans le tableau. 

Voici un tableau montrant les typecodes acceptables :

| Typecode  | Type C              | Type Python       | Taille en octets  |
| --------- | ------------------- | ----------------- | ----------- |
| 'b'       | char signé         | int               | 1           |
| 'B'       | char non signé       | int               | 1           |
| 'u'       | wchar_t             | Caractère Unicode | 2           |
| 'h'       | short signé        | int               | 2           |
| 'H'       | short non signé      | int               | 2           |
| 'i'       | int signé          | int               | 2           |
| 'I'       | int non signé        | int               | 2           |
| 'l'       | long signé         | int               | 4           |
| 'L'       | long non signé       | int               | 4           |
| 'q'       | long long signé    | int               | 8           |
| 'Q'       | long long non signé  | int               | 8           |
| 'f'       | float               | float             | 4           |
| 'd'       | double              | float             | 8           |


Typecodes obtenus depuis [la documentation Python](https://docs.python.org/3/library/array.html).

Voici un exemple de tableau en Python :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

print(nombres[1])
# 2
```

Nous avons créé un tableau de valeurs entières de 1 à 5 ici. Nous avons également accédé à la deuxième valeur en utilisant des crochets et son index dans l'ordre, qui est **1**.

## Comment découper un tableau en Python

Disons que vous voulez découper une portion de ce tableau et assigner la tranche à une autre variable. Vous pouvez le faire en utilisant des deux-points et des crochets. La syntaxe ressemble à ceci :

```python
tableau[début:fin:pas]
```

L'index `début` spécifie l'index à partir duquel le découpage commence. La valeur par défaut est **0**.

L'index `fin` spécifie l'index où le découpage se termine (mais en excluant la valeur à cet index). La valeur par défaut est la longueur du tableau.

L'argument `pas` spécifie le pas du découpage. La valeur par défaut est **1**.

Voyons quelques exemples qui couvrent différentes façons de découper des tableaux.


### Comment découper sans index de début ou de fin

Lorsque vous découpez sans index `début` ou `fin`, vous obtenez essentiellement une copie complète du tableau :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[:]

print(copie)
# array('i', [1, 2, 3, 4, 5])
```

Comme vous pouvez le voir ici, nous avons une copie du tableau `nombres`.

> Il est également intéressant de noter que l'action de découpage n'affecte pas le tableau original. Avec le découpage, vous "copiez une portion" du tableau original.

### Comment découper avec un index de début

Par exemple, si vous voulez découper un tableau à partir d'une valeur de début spécifique jusqu'à la fin du tableau, voici comment faire :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[2:]

print(copie)
# array('i', [3, 4, 5])
```

En passant `2:` dans les crochets, le découpage commence à l'index **2** (qui contient la valeur 3) jusqu'à la fin du tableau, comme vous pouvez le voir dans les résultats.

### Comment découper avec un index de fin

Par exemple, si vous voulez découper un tableau de la première valeur à la troisième, voici comment faire :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[:3]

print(copie)
# array('i', [1, 2, 3])
```

En passant `:3` dans les crochets, le découpage commence à l'index **0** (par défaut, puisque non spécifié) jusqu'à l'index trois que nous avons spécifié.

Comme mentionné précédemment, le découpage exclut la valeur à l'index trois. Donc dans les résultats, comme vous le trouvez dans la variable `copie`, les valeurs retournées sont de l'index **0** à l'index **2**.

### Comment découper avec un index de début et de fin

Que faire si vous voulez spécifier les points de début et de fin du découpage ? Voici comment faire :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[1:4]

print(copie)
# array('i', [2, 3, 4])
```

En utilisant un nombre, puis un deux-points, suivi d'un nombre dans des crochets, vous pouvez spécifier des index de début et de fin, respectivement. 

Dans notre cas, nous avons utilisé **1** et **4** comme dans `[1:4]`. D'après les résultats, vous voyez que le découpage commence à partir de la valeur à l'index **1** qui est `2`, jusqu'à la valeur avant l'index **4**, qui est `4` (à l'index 3).

### Comment découper avec des pas

Lorsque vous spécifiez un index `début` et `fin` de 1 et 5, respectivement, le découpage sélectionnera les valeurs à l'index **1**, l'index **2** (1 incrément à l'index précédent), l'index **3** (1 incrément à l'index précédent) et l'index **4** (et un incrément à l'index précédent). 

Dans ce découpage, un pas de **1** est utilisé par défaut. Mais vous pouvez fournir un pas différent. Voici comment :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[1:4:2]

print(copie)
# array('i', [2, 4])
```

En ajoutant un autre deux-points, vous pouvez spécifier un pas. Donc nous avons `[début:fin:pas]`. 

Dans notre exemple, le début est **1**, la fin est **4** et le pas est 2. Le découpage commence à partir de la valeur à l'index 1 qui est **2**, puis la valeur suivante sera à l'index précédent plus le pas, qui est `1 + 2` égal à 3. La valeur à l'index 3 est **4** donc celle-ci est ajoutée à la tranche. L'index suivant sera 5 (`3 + 2`) mais puisque 5 dépasse l'index de fin, il ne sera pas ajouté à la tranche.

Comme vous pouvez le voir dans le code, la copie découpée est simplement 2 et 4.

### Comment découper avec des index de début et de fin négatifs

Les index `début` ou `fin` peuvent également être négatifs. Les index négatifs comptent à partir de la fin du tableau. Cela signifie qu'un index négatif est la dernière valeur dans un tableau :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

print(nombres[-1])
# 5
```

En utilisant un négatif 1 ici, vous voyez que **5** est retourné, qui est de la fin d'un tableau.

Avec une expression de tranche comme `[-3:-1]`, cela signifie un index de début de **-3** et un index de fin de **-1**. Voyons comment cela fonctionne avec notre tableau :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[-3:-1]

print(copie)
# array('i', [3, 4])
```

La tranche commence à l'index **-3** (qui est la troisième valeur à partir de la fin du tableau, c'est-à-dire 3) et s'arrête à l'index **-1** (qui est la dernière valeur dans le tableau, c'est-à-dire 5). Le découpage n'inclut pas la dernière valeur donc nous avons 3 et 4.

> Combiner un index `début` négatif et un index `fin` positif (ou vice versa) ne fonctionnera pas car vous irez dans des directions différentes en même temps.

### Comment découper avec des pas négatifs

Vous pouvez utiliser des pas négatifs, ce qui signifie que les pas décrémentent pour le découpage. Voici un exemple :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[2::-1]

print(copie)
# array('i', [3, 2, 1])
```

Ici, nous spécifions un début à l'index **2**, pas de fin, et un pas de **-1**. Le découpage ici commencera à l'index **2** qui est 3. Les pas négatifs signifient que la valeur suivante dans la tranche sera à un index plus petit que l'index précédent de 1. Cela signifie `2 - 1` qui est **1** donc la valeur à cet index, qui est 2 sera ajoutée à la tranche. 

Cela continue à l'envers jusqu'à ce qu'il atteigne la fin du tableau qui est l'index **0**. Le tableau découpé résulte en des valeurs de 3, 2, et 1.

### Que signifie `[::-1]` ?

Avez-vous déjà vu cette expression quelque part en Python ? Eh bien, voici ce qu'elle signifie : il n'y a pas d'index `début` spécifié, ni d'index `fin`, seulement un pas négatif de **-1**. 

L'index `début` par défaut est **0**, donc en utilisant un pas de **-1**, le découpage contiendra les valeurs aux index suivants : **-1** (`0 - 1`), **-2** (`-1 - 1`), **-3** (`-2 - 1`), **-4** (`-3 - 1`) et **-5** (`-4 - 1`). Pratiquement une copie inversée du tableau.

Voici le code pour cela :

```python
import array as arr 

nombres = arr.array('i', [1, 2, 3, 4, 5])

copie = nombres[::-1]

print(copie)
# array('i', [5, 4, 3, 2, 1])
```

Comme vous pouvez le voir, c'est une façon simple d'inverser un tableau.

## Conclusion

Dans cet article, nous avons brièvement examiné comment déclarer des tableaux en Python, comment accéder aux valeurs dans un tableau, et aussi comment découper – ou trancher – une partie d'un tableau en utilisant un deux-points et des crochets. 

Nous avons également appris comment le découpage fonctionne avec des pas et des index de début et de fin positifs/négatifs.

Vous pouvez en apprendre plus sur les tableaux ici : [Tutoriel Python Array – Définir, Index, Méthodes](https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods).