---
title: Break en Python – Exemple de rupture de boucle for imbriquée si condition remplie
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-17T15:05:36.000Z'
originalURL: https://freecodecamp.org/news/break-in-python-nested-for-loop-break-if-condition-met-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/henry-co-1qlMnKfql5c-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Break en Python – Exemple de rupture de boucle for imbriquée si condition
  remplie
seo_desc: "Loops in programming let us execute a set of instructions/block of code\
  \ continuously until a certain condition is met. \nWe can also use loops to iterate\
  \ over a collection of data and perform a similar operation on each item in the\
  \ data set.\nnames = [..."
---

Les boucles en programmation nous permettent d'exécuter un ensemble d'instructions/bloc de code en continu jusqu'à ce qu'une certaine condition soit remplie. 

Nous pouvons également utiliser des boucles pour itérer sur une collection de données et effectuer une opération similaire sur chaque élément de l'ensemble de données.

```python
names = ["John", "Jane", "Doe"]
for i in names:
    print(i)
    
"""
John
Jane
Doe
"""
```

Ci-dessus se trouve une boucle `for` Python qui itère sur une liste de noms et imprime tous les noms. 

Dans les situations où nous voulons arrêter l'itération avant d'atteindre le dernier élément ou avant qu'une condition donnée soit remplie, nous pouvons utiliser l'instruction `break`. L'instruction `break` aura sa propre condition – cela lui indique quand "rompre" la boucle.

Dans cet article, nous verrons d'abord comment utiliser l'instruction `break` dans les boucles `for` et `while`. Ensuite, nous examinerons certaines des méthodes que nous pouvons utiliser pour rompre les boucles imbriquées en Python.

## Comment écrire une instruction `break` en Python ?

Vous définissez l'instruction `break` dans la boucle que vous souhaitez terminer. Dans cette section, nous verrons comment utiliser l'instruction `break` dans les boucles `for` et `while`.

### Comment utiliser l'instruction `break` dans une boucle `for`

Voici un exemple :

```python
names = ["John", "Jane", "Doe"]
for i in names:
    print(i)
    if i == "Jane":
        break
```

Dans le code ci-dessus, nous imprimons une liste de noms :

```python
for i in names:
    print(i)
```

Nous avons ensuite créé une nouvelle condition qui vérifie lorsque la variable `i` atteint un nom égal à "Jane". Lorsque cette condition est remplie, la boucle doit s'arrêter. Elle s'arrête parce que l'instruction `break` arrête la boucle lorsque `i` est "Jane" :

```python
if i == "Jane":
        break
```

Cela revient à dire : "imprime tous les noms et arrête-toi une fois que tu arrives à Jane". Donc dans notre console, sur les trois noms — `["John", "Jane", "Doe"]` — seuls "John" et "Jane" seront imprimés. 

Nous pouvons aussi faire cela avec des nombres :

```python
for i in range(10):
  print(i)
```

Le code ci-dessus imprime une série de nombres de 0 à 9. Mais nous pouvons arrêter cette boucle d'imprimer tous les nombres — nous pouvons nous arrêter à un nombre particulier à la place. Voici comment :

```python
for i in range(10):
  print(i)
  if i == 5:
      break
```

Maintenant, la boucle s'arrête à 5. Donc nous ne verrons que 0, 1, 2, 3, 4 et 5 dans la console.

### Comment utiliser l'instruction `break` dans une boucle `while`

L'exemple de cette section sera similaire à celui de la section précédente. Nous utiliserons une boucle `while` à la place.

```python
i = 0
while i < 10:
  print(i)
  i += 1
```

Le code ci-dessus imprime une série de nombres de 0 à 9. Nous allons utiliser `break` pour arrêter l'impression des nombres lorsque nous arrivons à 5. 

```python
i = 1
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1
```

Tout comme nous l'avons fait dans la section précédente, nous avons créé une nouvelle condition : `if i == 5` et lorsque cette condition est remplie, la boucle est terminée au lieu d'imprimer jusqu'à 9. 

### Comment utiliser l'instruction `break` dans une boucle imbriquée

Dans cette section, nous verrons comment utiliser l'instruction `break` dans les boucles imbriquées.

Voici à quoi ressemble une boucle imbriquée :

```python
for x in range(4):
    for y in range(4):
        print(x, y)

"""
0 0
0 1
0 2
0 3
1 0
1 1
1 2
1 3
2 0
2 1
2 2
2 3
3 0
3 1
3 2
3 3
"""
```

Les boucles imbriquées peuvent souvent être déroutantes pour les débutants. Donc, si vous vous demandez comment nous avons obtenu la sortie ci-dessus (commentée dans le code), voici une brève explication :

`range(4)` nous donnera une série de nombres de 0 à 3. 

L'impression de `for x in range(4):` seule nous donnera 0, 1, 2, 3. Mais nous imbriquons une autre série de nombres dans la boucle : `for y in range(4):`

Ce que fait la deuxième boucle, c'est dupliquer chaque nombre de `x` par le nombre d'entiers qu'il possède (dans la série `y`). Nous avons quatre nombres dans la série `y` – 0, 1, 2, 3. 

Donc pour la série `x`, le premier nombre est 0 et il apparaîtra quatre fois. Chaque fois qu'il apparaît, il prend un nombre de la série `y` ; c'est-à-dire : 0 et 0, 0 et 1, 0 et 2, 0 et 3. Cela s'applique aux autres nombres de la série `x`.

Si vous trouvez toujours cela difficile à comprendre, essayez d'exécuter le code vous-même. Essayez de changer la portée de chaque boucle pour voir ce qui se passe avec la sortie.

Rompons la boucle en utilisant l'instruction `break` :

```python
for x in range(4):
    for y in range(4):
        if x == 1:
            break
    print(x, y)
    
"""
0 3
1 3
2 0
3 3
"""
```

Bien que la boucle dans l'exemple ci-dessus semble s'être arrêtée, en y regardant de plus près la sortie (commentée ci-dessus), vous réaliserez que la boucle externe imprime toujours toutes ses valeurs, ce qui n'était pas l'intention.

Donc, utiliser simplement l'instruction `break` ne rompt pas réellement une boucle imbriquée. Voyons quelques-unes des solutions de contournement pour obtenir le résultat souhaité.

#### Utilisation d'une variable booléenne

```python
force_break_loop = False
for x in range(5):
    for y in range(5):
        if x == 2:
            force_break_loop = True
            break
    if force_break_loop:
        break
    print(x, y)

"""
0 4
1 4
"""
```

Dans l'exemple ci-dessus, nous utilisons une variable booléenne dont la valeur initiale est `False`. Lorsque la boucle atteint le point de rupture prévu, nous définissons ce booléen comme `True`, mais ce n'est pas tout. Nous vérifions lorsque la variable est `True` et attribuons ensuite l'instruction `break`. 

#### Utilisation de l'instruction Break deux fois

```python
for x in range(5):
    for y in range(5):
        if x == 3:
            break
    if x == 3:
        break
    print(x, y)
    
"""
0 4
1 4
2 4
"""
```

Dans cet exemple, nous définissons deux instructions `if` – toutes deux retournant une instruction `break` pour forcer la boucle à se rompre. 

Bien que ces solutions de contournement aient pu terminer la boucle à une instance donnée, vous remarquerez que la valeur de la boucle interne reste la même chaque fois que la boucle se rompt. 

Cela ne signifie pas que les boucles imbriquées sont mauvaises. Mais assurez-vous d'en avoir vraiment besoin avant de les implémenter dans votre logique.

## Conclusion

Dans cet article, nous avons vu comment utiliser l'instruction `break` pour terminer une boucle avant que la condition initiale de la boucle soit remplie ou avant qu'une itération sur les éléments d'un ensemble de données soit complète.

Nous avons vu quelques exemples de la façon dont vous pouvez utiliser l'instruction `break` dans les boucles `for` et `while`.

Enfin, nous avons parlé des boucles imbriquées. Nous avons découvert qu'une instruction `break` n'arrête pas réellement la boucle. Cela nous a conduit à voir quelques exemples de certaines des méthodes que nous pouvons utiliser pour rompre une boucle imbriquée en Python.

Bon codage !