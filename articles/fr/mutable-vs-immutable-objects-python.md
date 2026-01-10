---
title: Objets mutables vs immutables en Python – Un guide visuel et pratique
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2020-11-11T19:01:31.000Z'
originalURL: https://freecodecamp.org/news/mutable-vs-immutable-objects-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95a1740569d1a4ca0dd3.jpg
tags:
- name: pythonic programming
  slug: pythonic-programming
- name: immutability
  slug: immutability
- name: mutable
  slug: mutable
- name: object
  slug: object
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Objets mutables vs immutables en Python – Un guide visuel et pratique
seo_desc: "Python is an awesome language. Because of its simplicity, many people choose\
  \ it as their first programming language. \nExperienced programmers use Python all\
  \ the time as well, thanks to its wide community, abundance of packages, and clear\
  \ syntax.\nBut ..."
---

Python est un langage formidable. Grâce à sa simplicité, beaucoup de gens le choisissent comme premier langage de programmation. 

Les programmeurs expérimentés utilisent également Python tout le temps, grâce à sa large communauté, son abondance de packages et sa syntaxe claire.

Mais il y a un problème qui semble confondre les débutants ainsi que certains développeurs expérimentés : les objets Python. Plus précisément, la différence entre les objets **mutables** et **immutables**.

Dans cet article, nous allons approfondir notre connaissance des objets Python, apprendre la différence entre les objets **mutables** et **immutables**, et voir comment nous pouvons utiliser l'**interpréteur** pour mieux comprendre comment Python fonctionne. 

Nous allons utiliser des fonctions et des mots-clés importants tels que `id` et `is`, et nous comprendrons la différence entre `x == y` et `x is y`.

Êtes-vous prêt ? Commençons.

# En Python, tout est un objet

Contrairement à d'autres langages de programmation où le langage _supporte_ les objets, en Python, vraiment **tout** est un objet – y compris les entiers, les listes et même les fonctions.

Nous pouvons utiliser notre interpréteur pour vérifier cela :

```python
>>> isinstance(1, object)
True

>>> isinstance(False, object)
True

def my_func():
   return "hello"
   
>>> isinstance(my_func, object)
True
```

Python a une fonction intégrée, `id`, qui retourne l'adresse d'un objet en mémoire. Par exemple :

```python
>>> x = 1
>>> id(x)
1470416816
```

Ci-dessus, nous avons créé un **objet** nommé `x`, et nous lui avons assigné la valeur `1`. Nous avons ensuite utilisé `id(x)` et découvert que cet objet se trouve à l'adresse `1470416816` en mémoire.

Cela nous permet de vérifier des choses intéressantes sur Python. Supposons que nous créons deux variables en Python – une nommée `x`, et une autre nommée `y` – et que nous leur assignons la même valeur. Par exemple, ici :

```python
>>> x = "I love Python!"
>>> y = "I love Python!"
```

Nous pouvons utiliser l'opérateur d'égalité (`==`) pour vérifier qu'ils ont bien la même valeur aux yeux de Python :

```python
>>> x == y
True
```

Mais s'agit-il du même objet en mémoire ? En théorie, il peut y avoir deux scénarios très différents ici. 

Selon le scénario **(1)**, nous avons vraiment deux objets différents, l'un nommé `x`, et l'autre nommé `y`, qui ont simplement la même valeur. 

Pourtant, il pourrait aussi être le cas que Python ne stocke ici qu'un seul objet, qui a deux noms qui le référencent – comme le montre le scénario **(2)** :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-19.png)

Nous pouvons utiliser la fonction `id` introduite ci-dessus pour vérifier cela :

```python
>>> x = "I love Python!"
>>> y = "I love Python!"
>>> x == y
True

>>> id(x)
52889984

>>> id(y)
52889384
```

Ainsi, comme nous pouvons le voir, le comportement de Python correspond au scénario (1) décrit ci-dessus. Même si `x == y` dans cet exemple (c'est-à-dire que `x` et `y` ont les mêmes _valeurs_), ils sont des objets différents en mémoire. Cela est dû au fait que `id(x) != id(y)`, comme nous pouvons le vérifier explicitement :

```python
>>> id(x) == id(y)
False
```

Il existe une manière plus courte de faire la comparaison ci-dessus, et c'est d'utiliser l'opérateur `is` de Python. Vérifier si `x is y` est la même chose que vérifier `id(x) == id(y)`, ce qui signifie si `x` et `y` sont le même objet en mémoire :

```python
>>> x == y
True

>>> id(x) == id(y)
False

>>> x is y
False
```

Cela éclaire la différence importante entre l'opérateur d'égalité `==` et l'opérateur d'identité `is`. 

Comme vous pouvez le voir dans l'exemple ci-dessus, il est tout à fait possible que deux noms en Python (`x` et `y`) soient liés à deux objets différents (et ainsi, `x is y` est `False`), où ces deux objets ont la même valeur (donc `x == y` est `True`).

Comment pouvons-nous créer une autre variable qui pointe vers le même objet que `x` ? Nous pouvons simplement utiliser l'opérateur d'assignation `=`, comme ceci :

```python
>>> x = "I love Python!"
>>> z = x
```

Pour vérifier qu'ils pointent bien vers le même objet, nous pouvons utiliser l'opérateur `is` :

```python
>>> x is z
True
```

Bien sûr, cela signifie qu'ils ont la même adresse en mémoire, comme nous pouvons le vérifier explicitement en utilisant `id` :

```python
>>> id(x)
54221824

>>> id(z)
54221824
```

Et, bien sûr, ils ont la même valeur, donc nous nous attendons à ce que `x == z` retourne `True` également :

```python
>>> x == z
True
```

# Objets mutables et immutables en Python

Nous avons dit que tout en Python est un objet, mais il existe une distinction importante entre les objets. Certains objets sont **mutables** tandis que d'autres sont **immutables**. 

Comme je l'ai mentionné précédemment, ce fait cause de la confusion pour beaucoup de personnes qui sont nouvelles à Python, donc nous allons nous assurer que c'est clair.

## Objets immutables en Python

Pour certains types en Python, une fois que nous avons créé des instances de ces types, ils ne changent jamais. Ils sont **immutables**. 

Par exemple, les objets `int` sont immutables en Python. Que se passera-t-il si nous essayons de changer la valeur d'un objet `int` ?

```python
>>> x = 24601
>>> x
24601

>>> x = 24602
>>> x
24602
```

Eh bien, il semble que nous avons changé `x` avec succès. C'est exactement là que beaucoup de gens se trompent. Que s'est-il passé exactement sous le capot ici ? Utilisons `id` pour enquêter davantage :

```python
>>> x = 24601
>>> x
24601

>>> id(x)
1470416816

>>> x = 24602
>>> x
24602

>>> id(x)
1470416832
```

Ainsi, nous pouvons voir qu'en assignant `x = 24602`, nous n'avons pas changé la valeur de l'objet auquel `x` était lié auparavant. Plutôt, nous avons créé un nouvel objet, et lié le nom `x` à celui-ci. 

Ainsi, après avoir assigné `24601` à `x` en utilisant `x = 24601`, nous avions l'état suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-46.png)

Et après avoir utilisé `x = 24602`, nous avons créé un nouvel objet, et lié le nom `x` à ce nouvel objet. L'autre objet avec la valeur `24601` n'est plus accessible par `x` (ou tout autre nom dans ce cas) :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-47.png)

Chaque fois que nous assignons une nouvelle valeur à un nom (dans l'exemple ci-dessus - `x`) qui est lié à un objet `int`, nous changeons en réalité la liaison de ce nom à un autre objet. 

La même chose s'applique pour les `tuple`s, les chaînes de caractères (`str` objets), et les `bool`s également. En d'autres termes, les objets `int` (et autres types de nombres tels que `float`), `tuple`, `bool`, et `str` sont **immutables**. 

Testons cette hypothèse. Que se passe-t-il si nous créons un objet `tuple`, puis lui donnons une valeur différente ? 

```python
>>> my_tuple = (1, 2, 3)
>>> id(my_tuple)
54263304

>>> my_tuple = (3, 4, 5)
>>> id(my_tuple)
56898184
```

Tout comme un objet `int`, nous pouvons voir que notre assignation a en réalité changé l'objet auquel le nom `my_tuple` est lié.

Que se passe-t-il si nous essayons de changer l'un des éléments du `tuple` ?

```python
>>> my_tuple[0] = 'a new value'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Comme nous pouvons le voir, Python ne nous permet pas de modifier le contenu de `my_tuple`, car il est immutable.

## Objets mutables en Python

Certains types en Python peuvent être modifiés après leur création, et ils sont appelés **mutables**. Par exemple, nous savons que nous pouvons modifier le contenu d'un objet `list` :

```python
>>> my_list = [1, 2, 3]
>>> my_list[0] = 'a new value'
>>> my_list
['a new value', 2, 3]
```

Cela signifie-t-il que nous avons en réalité créé un nouvel objet en assignant une nouvelle valeur au premier élément de `my_list` ? Encore une fois, nous pouvons utiliser `id` pour vérifier :

```python
>>> my_list = [1, 2, 3]
>>> id(my_list)
55834760

>>> my_list
[1, 2, 3]

>>> my_list[0] = 'a new value'
>>> id(my_list)
55834760

>>> my_list
['a new value', 2, 3]
```

Ainsi, notre première assignation `my_list = [1, 2, 3]` a créé un objet à l'adresse `55834760`, avec les valeurs `1`, `2`, et `3` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-22.png)

Nous avons ensuite modifié le premier élément de cet objet `list` en utilisant `my_list[0] = 'a new value'`, c'est-à-dire sans créer un nouvel objet `list` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-23.png)

Maintenant, créons deux noms – `x` et `y`, tous deux liés au même objet `list`. Nous pouvons vérifier cela soit en utilisant `is`, soit en vérifiant explicitement leurs `id` :

```python
>>> x = y = [1, 2]
>>> x is y
True

>>> id(x)
18349096

>>> id(y)
18349096

>>> id(x) == id(y)
True
```

Que se passe-t-il maintenant si nous utilisons `x.append(3)` ? C'est-à-dire, si nous ajoutons un nouvel élément (`3`) à l'objet nommé `x` ?

Est-ce que `x` sera changé ? Est-ce que `y` sera changé ?

Eh bien, comme nous le savons déjà, ils sont essentiellement deux noms du même objet :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-28.png)

Puisque cet objet est changé, lorsque nous vérifions ses noms, nous pouvons voir la nouvelle valeur :

```python
>>> x.append(3)
>>> x
[1, 2, 3]

>>> y
[1, 2, 3]
```

Notez que `x` et `y` ont le même `id` qu'avant – car ils sont toujours liés au même objet `list` :

```python
>>> id(x)
18349096

>>> id(y)
18349096
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-27.png)

En plus des `list`, d'autres types Python qui sont mutables incluent les `set` et les `dict`.

# Implications pour les clés de dictionnaire en Python

Les dictionnaires (`dict` objets) sont couramment utilisés en Python. Pour rappel, nous les définissons comme suit :

```python
my_dict = {"name": "Omer", "number_of_pets": 1}
```

Nous pouvons ensuite accéder à un élément spécifique par son nom de clé :

```python
>>> my_dict["name"]
'Omer'
```

Les dictionnaires sont **mutables**, donc nous pouvons changer leur contenu après leur création. À tout moment, une clé dans le dictionnaire peut pointer vers un seul élément :

```python
>>> my_dict["name"] = "John"
>>> my_dict["name"]
'John'
```

Il est intéressant de noter que **les clés d'un dictionnaire doivent être immutables** :

```python
>>> my_dict = {[1,2]: "Hello"}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Pourquoi en est-il ainsi ? 

Considérons le scénario hypothétique suivant (note : l'extrait ci-dessous ne peut pas vraiment être exécuté en Python) :

```python
>>> x = [1, 2]
>>> y = [1, 2, 3]
>>> my_dict = {x: 'a', y: 'b'}
```

Jusqu'à présent, les choses ne semblent pas si mauvaises. Nous supposerions que si nous accédons à `my_dict` avec la clé `[1, 2]`, nous obtiendrons la valeur correspondante `'a'`, et si nous accédons à la clé `[1, 2, 3]`, nous obtiendrons la valeur `'b'`. 

Maintenant, que se passerait-il si nous tentions d'utiliser :

```python
>>> x.append(3)
```

Dans ce cas, `x` aurait la valeur `[1, 2, 3]`, et `y` aurait également la valeur `[1, 2, 3]`. Que devrions-nous obtenir lorsque nous demandons `my_dict[[1, 2, 3]]` ? Sera-ce `'a'` ou `'b'` ? Pour éviter de tels cas, Python n'autorise tout simplement pas les clés de dictionnaire à être mutables.

# Aller un peu plus loin

Essayons d'appliquer nos connaissances à un cas un peu plus intéressant.

Ci-dessous, nous définissons une `list` (un objet **mutable**) et un `tuple` (un objet **immutable**). La `list` inclut un `tuple`, et le `tuple` inclut une `list` :

```python
>>> my_list = [(1, 1), 2, 3]
>>> my_tuple = ([1, 1], 2, 3)
>>> type(my_list)
<class 'list'>

>>> type(my_list[0])
<class 'tuple'>

>>> type(my_tuple)
<class 'tuple'>

>>> type(my_tuple[0])
<class 'list'>
```

Jusqu'à présent, tout va bien. Maintenant, essayez de réfléchir par vous-même – que se passera-t-il lorsque nous essaierons d'exécuter chacune des instructions suivantes ?

(1) `>>> my_list[0][0] = 'Changed!'`

(2) `>>> my_tuple[0][0] = 'Changed!'`

Dans l'instruction (1), ce que nous essayons de faire est de changer le premier élément de `my_list`, c'est-à-dire un `tuple`. Puisqu'un `tuple` est **immutable**, cette tentative est vouée à l'échec :

```python
>>> my_list[0][0] = 'Changed!'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Notez que ce que nous essayions de faire n'était pas de changer la liste, mais plutôt de changer le contenu de son premier élément. 

Considérons l'instruction (2). Dans ce cas, nous accédons au premier élément de `my_tuple`, qui se trouve être une `list`, et nous le modifions. Enquêtons davantage sur ce cas et regardons les adresses de ces éléments :

```python
>>> my_tuple = ([1, 1], 2, 3)
>>> id(my_tuple)
20551816

>>> type(my_tuple[0])
<class 'list'>

>>> id(my_tuple[0])
20446248
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-29.png)

Lorsque nous changeons `my_tuple[0][0]`, nous ne changeons pas vraiment `my_tuple` du tout ! En effet, après le changement, le premier élément de `my_tuple` sera toujours l'objet dont l'adresse en mémoire est `20446248`. Cependant, nous changeons la valeur de cet objet :

```python
>>> my_tuple[0][0] = 'Changed!'
>>> id(my_tuple)
20551816

>>> id(my_tuple[0])
20446248

>>> my_tuple
(['Changed!', 1], 2, 3)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-48.png)

Puisque nous avons seulement modifié la valeur de `my_tuple[0]`, qui est un objet `list` mutable, cette opération a été autorisée par Python.

# Récapitulatif

Dans cet article, nous avons appris à propos des objets Python. Nous avons dit qu'en Python **tout est un objet**, et nous avons utilisé `id` et `is` pour approfondir notre compréhension de ce qui se passe sous le capot lorsque nous utilisons Python pour créer et modifier des objets.

Nous avons également appris la différence entre les objets **mutables**, qui peuvent être modifiés après leur création, et les objets **immutables**, qui ne le peuvent pas. 

Nous avons vu que lorsque nous demandons à Python de modifier un objet immutable qui est lié à un certain nom, nous créons en réalité un nouvel objet et lions ce nom à celui-ci.

Nous avons ensuite appris pourquoi les clés de dictionnaire doivent être **immutables** en Python.

Comprendre comment Python "voit" les objets est une clé pour devenir un meilleur programmeur Python. J'espère que cet article vous a aidé dans votre parcours pour maîtriser Python.

[_Omer Rosenbaum_](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/)_,_ [_Swimm_](https://swimm.io/)_s Chief Technology Officer. Expert en formation cybernétique et fondateur de Checkpoint Security Academy. Auteur de_ [_Computer Networks (en hébreu)_](https://data.cyber.org.il/networks/networks.pdf)_. Visitez ma_ [_Chaîne YouTube_](https://www.youtube.com/watch?v=79jlgESHzKQ&list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)_.