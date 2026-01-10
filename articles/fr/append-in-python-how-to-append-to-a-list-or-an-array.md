---
title: Append en Python – Comment ajouter à une liste ou un tableau
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-07T17:41:31.000Z'
originalURL: https://freecodecamp.org/news/append-in-python-how-to-append-to-a-list-or-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/nordwood-themes-EZSm8xRjnX0-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Append en Python – Comment ajouter à une liste ou un tableau
seo_desc: 'In this article, you''ll learn about the .append() method in Python.  You''ll
  also see how .append() differs from other methods used to add elements to lists.

  Let''s get started!

  What are lists in Python? A definition for beginners

  An array in programmi...'
---

Dans cet article, vous apprendrez la méthode `.append()` en Python. Vous verrez également comment `.append()` diffère des autres méthodes utilisées pour ajouter des éléments aux listes.

Commençons !

## Que sont les listes en Python ? Une définition pour débutants

Un tableau en programmation est une collection ordonnée d'éléments, et tous les éléments doivent être du même type de données.

Cependant, contrairement à d'autres langages de programmation, les tableaux ne sont pas une structure de données intégrée en Python. Au lieu des tableaux traditionnels, Python utilise des listes.

Les listes sont essentiellement des tableaux dynamiques et sont l'une des structures de données les plus courantes et puissantes en Python.

Vous pouvez les considérer comme des conteneurs ordonnés. Ils stockent et organisent des données similaires ensemble.

Les éléments stockés dans une liste peuvent être de n'importe quel type de données.

Il peut y avoir des listes d'entiers (nombres entiers), des listes de flottants (nombres à virgule flottante), des listes de chaînes de caractères (texte), et des listes de tout autre type de données intégré en Python.

Bien qu'il soit possible pour les listes de contenir des éléments d'un seul type de données, elles sont plus flexibles que les tableaux traditionnels. Cela signifie qu'il peut y avoir une variété de différents types de données à l'intérieur de la même liste.

Les listes ont 0 ou plusieurs éléments, ce qui signifie qu'il peut également y avoir des listes vides. À l'intérieur d'une liste, il peut également y avoir des valeurs en double.

Les valeurs sont séparées par une virgule et enfermées dans des crochets, `[]`.

### Comment créer des listes en Python

Pour créer une nouvelle liste, donnez d'abord un nom à la liste. Ensuite, ajoutez l'opérateur d'assignation (`=`) et une paire de crochets ouvrants et fermants. À l'intérieur des crochets, ajoutez les valeurs que vous voulez que la liste contienne.

```python
#créer une nouvelle liste de noms
noms = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#afficher la liste dans la console
print(noms)

#sortie
#['Jimmy', 'Timmy', 'Kenny', 'Lenny']
```

### Comment les listes sont indexées en Python

Les listes maintiennent un ordre pour chaque élément.

Chaque élément dans la collection a son propre numéro d'index, que vous pouvez utiliser pour accéder à l'élément lui-même.

Les index en Python (et dans tous les autres langages de programmation modernes) commencent à 0 et augmentent pour chaque élément dans la liste.

Par exemple, la liste créée précédemment avait 4 valeurs :

```python
noms = ["Jimmy", "Timmy", "Kenny", "Lenny"]
```

La première valeur dans la liste, "Jimmy", a un index de 0.

La deuxième valeur dans la liste, "Timmy", a un index de 1.

La troisième valeur dans la liste, "Kenny", a un index de 2.

La quatrième valeur dans la liste, "Lenny", a un index de 3.

Pour accéder à un élément dans la liste par son numéro d'index, écrivez d'abord le nom de la liste, puis entre crochets, écrivez l'entier de l'index de l'élément.

Par exemple, si vous vouliez accéder à l'élément qui a un index de 2, vous feriez :

```python
noms = ["Jimmy", "Timmy", "Kenny", "Lenny"]

print(noms[2])

#sortie
#Kenny
```

## Les listes en Python sont mutables

En Python, lorsque les objets sont *mutables*, cela signifie que leurs valeurs peuvent être modifiées une fois qu'ils ont été créés.

Les listes sont des objets mutables, vous pouvez donc les mettre à jour et les modifier après leur création.

Les listes sont également dynamiques, ce qui signifie qu'elles peuvent grandir et rétrécir tout au long de la vie d'un programme.

Des éléments peuvent être supprimés d'une liste existante, et de nouveaux éléments peuvent être ajoutés à une liste existante.

Il existe des méthodes intégrées pour ajouter et supprimer des éléments des listes.

Par exemple, pour **ajouter** des éléments, il y a les méthodes `.append()`, `.insert()` et `.extend()`.

Pour **supprimer** des éléments, il y a les méthodes `.remove()`, `.pop()` et `.pop(index)`.


### Que fait la méthode `.append()` ?

La méthode `.append()` ajoute un élément supplémentaire à la **fin** d'une liste déjà existante.

La syntaxe générale ressemble à ceci :

```python
nom_liste.append(élément)
```

Décomposons cela :

- `nom_liste` est le nom que vous avez donné à la liste.
- `.append()` est la méthode de liste pour ajouter un élément à la fin de `nom_liste`.
- `élément` est l'élément individuel spécifié que vous voulez ajouter.

Lorsque vous utilisez `.append()`, la liste originale est modifiée. Aucune nouvelle liste n'est créée.

Si vous vouliez ajouter un nom supplémentaire à la liste créée précédemment, vous feriez ce qui suit :

```python
noms = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#ajouter le nom Dylan à la fin de la liste
noms.append("Dylan")

print(noms)

#sortie
#['Jimmy', 'Timmy', 'Kenny', 'Lenny', 'Dylan']
```

### Quelle est la différence entre les méthodes `.append()` et `.insert()` ?

La différence entre les deux méthodes est que `.append()` ajoute un élément à la **fin** d'une liste, alors que `.insert()` insère un élément **à une position spécifiée** dans la liste.

Comme vous l'avez vu dans la section précédente, `.append()` ajoutera l'élément que vous passez comme argument à la fonction toujours à la fin de la liste.

Si vous ne voulez pas simplement ajouter des éléments à la fin d'une liste, vous pouvez spécifier la position à laquelle vous voulez les ajouter avec `.insert()`.

La syntaxe générale ressemble à ceci :

```python
nom_liste.insert(position, élément)
```

Décomposons cela :

- `nom_liste` est le nom de la liste.
- `.insert()` est la méthode de liste pour insérer un élément dans une liste.
- `position` est le premier argument de la méthode. C'est toujours un entier - spécifiquement, c'est le numéro d'index de la position où vous voulez que le nouvel élément soit placé.
- `élément` est le deuxième argument de la méthode. Ici, vous spécifiez le nouvel élément que vous voulez ajouter à la liste.

Par exemple, supposons que vous avez la liste suivante de langages de programmation :

```python
langages_programmation = ["JavaScript", "Java", "C++"]

print(langages_programmation)

#sortie
#['JavaScript', 'Java', 'C++']
```

Si vous vouliez insérer "Python" au début de la liste, comme un nouvel élément de la liste, vous utiliseriez la méthode `.insert()` et spécifieriez la position comme `0`. (Rappelez-vous que la première valeur dans une liste a toujours un index de 0.)

```python
langages_programmation = ["JavaScript", "Java", "C++"]

langages_programmation.insert(0, "Python")

print(langages_programmation)

#sortie
#['Python', 'JavaScript', 'Java', 'C++']
```

Si vous aviez plutôt voulu que "JavaScript" soit le premier élément de la liste, et *ensuite* ajouter "Python" comme nouvel élément, vous spécifieriez la position comme `1` :

```python
langages_programmation = ["JavaScript", "Java", "C++"]

langages_programmation.insert(1, "Python")

print(langages_programmation)

#sortie
#['JavaScript', 'Python', 'Java', 'C++']
```

La méthode `.insert()` vous donne un peu plus de flexibilité par rapport à la méthode `.append()` qui ajoute simplement un nouvel élément à la fin de la liste.

### Quelle est la différence entre les méthodes `.append()` et `.extend()` ?

Et si vous voulez ajouter plus d'un élément à une liste à la fois, au lieu de les ajouter un par un ?

Vous pouvez utiliser la méthode `.append()` pour ajouter plus d'un élément à la fin d'une liste.

Supposons que vous avez une liste qui ne contient que deux langages de programmation :

```python
langages_programmation = ["JavaScript", "Java"]

print(langages_programmation)

#sortie
#['JavaScript', 'Java']
```

Vous voulez ensuite ajouter deux autres langages, à la fin de celle-ci.

Dans ce cas, vous passez une liste contenant les deux nouvelles valeurs que vous voulez ajouter, comme argument à `.append()` :

```python
langages_programmation = ["JavaScript", "Java"]

#ajouter deux nouveaux éléments à la fin de la liste
langages_programmation.append(["Python", "C++"])

print(langages_programmation)

#sortie
#['JavaScript', 'Java', ['Python', 'C++']]
```

Si vous regardez de plus près la sortie ci-dessus, `['JavaScript', 'Java', ['Python', 'C++']]`, vous verrez qu'une nouvelle liste a été ajoutée à la fin de la liste déjà existante.

Ainsi, `.append()` **ajoute une liste à l'intérieur d'une liste**.

Les listes sont des objets, et lorsque vous utilisez `.append()` pour ajouter une autre liste dans une liste, les nouveaux éléments seront ajoutés en tant qu'objet unique (élément).

Supposons que vous avez déjà deux listes, comme suit :

```python
noms = ["Jimmy", "Timmy"]
plus_noms = ["Kenny", "Lenny"]
```

Et si vous vouliez combiner le contenu des deux listes en une seule, en ajoutant le contenu de `plus_noms` à `noms` ?

Lorsque la méthode `.append()` est utilisée à cette fin, une autre liste est créée à l'intérieur de `noms` :

```python
noms = ["Jimmy", "Timmy"]
plus_noms = ["Kenny", "Lenny"]

#ajouter le contenu de plus_noms à noms
noms.append(plus_noms)

print(noms)

#sortie
#['Jimmy', 'Timmy', ['Kenny', 'Lenny']]
```

Ainsi, `.append()` ajoute les nouveaux éléments en tant qu'autre liste, en ajoutant l'objet à la fin.

Pour concaténer (ajouter) réellement des listes ensemble, et **combiner tous les éléments d'une liste à une autre**, vous devez utiliser la méthode `.extend()`.

La syntaxe générale ressemble à ceci :

```python
nom_liste.extend(itérable/autre_nom_liste)
```

Décomposons cela :

- `nom_liste` est le nom de l'une des listes.
- `.extend()` est la méthode pour ajouter tout le contenu d'une liste à une autre.
- `itérable` peut être n'importe quel itérable tel qu'une autre liste, par exemple, `autre_nom_liste`. Dans ce cas, `autre_nom_liste` est une liste qui sera concaténée avec `nom_liste`, et son contenu sera ajouté un par un à la fin de `nom_liste`, en tant qu'éléments séparés.

Ainsi, en prenant l'exemple précédent, lorsque `.append()` est remplacé par `.extend()`, la sortie ressemblera à ceci :

```python
noms = ["Jimmy", "Timmy"]
plus_noms = ["Kenny", "Lenny"]

noms.extend(plus_noms)

print(noms)

#sortie
#['Jimmy', 'Timmy', 'Kenny', 'Lenny']
```

Lorsque nous avons utilisé `.extend()`, la liste `noms` a été étendue et sa longueur a augmenté de 2.

La manière dont `.extend()` fonctionne est qu'il prend une liste (ou un autre itérable) comme argument, itère sur chaque élément, et chaque élément dans l'itérable est ajouté à la liste.

Il y a une autre différence entre `.append()` et `.extend()`.

Lorsque vous voulez ajouter une chaîne de caractères, comme vu précédemment, `.append()` ajoute l'élément entier et unique à la fin de la liste :

```python
noms = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#ajouter le nom Dylan à la fin de la liste
noms.append("Dylan")

print(noms)

#sortie
#['Jimmy', 'Timmy', 'Kenny', 'Lenny', 'Dylan']
```

Si vous utilisiez `.extend()` à la place pour ajouter une chaîne de caractères à la fin d'une liste, chaque caractère de la chaîne serait ajouté en tant qu'élément individuel à la liste.

Cela est dû au fait que les chaînes de caractères sont un itérable, et `.extend()` itère sur l'argument itérable passé.

Ainsi, l'exemple ci-dessus ressemblerait à ceci :

```python
noms = ["Jimmy", "Timmy", "Kenny", "Lenny"]

#passer une chaîne (itérable) à .extend()
noms.extend("Dylan")

print(noms)

#sortie
#['Jimmy', 'Timmy', 'Kenny', 'Lenny', 'D', 'y', 'l', 'a', 'n']
```

## Conclusion

Pour résumer, la méthode `.append()` est utilisée pour ajouter un élément à la fin d'une liste existante, sans créer de nouvelle liste.

Lorsque elle est utilisée pour ajouter une liste à une autre liste, elle crée une liste à l'intérieur d'une liste.

Si vous voulez en savoir plus sur Python, consultez la [Certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp. Vous commencerez à apprendre de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique ce que vous avez appris.

Merci d'avoir lu et bon codage !