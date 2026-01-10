---
title: Python String to Array – Comment convertir du texte en une liste
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-02-21T18:47:23.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-array-how-to-convert-text-to-a-list
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/steve-johnson-8VO-UxlJ-Lw-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python String to Array – Comment convertir du texte en une liste
seo_desc: 'There will be times where you need to convert one data type to another.

  Fear not, because Python offers a variety of different ways to help you do that.

  In this article, you''ll see a few of the ways in which you can convert a string
  to a list.

  Here i...'
---

Il y aura des moments où vous devrez convertir un type de données en un autre.

Ne craignez rien, car Python offre une variété de façons différentes pour vous aider à le faire.

Dans cet article, vous verrez quelques-unes des façons dont vous pouvez convertir une chaîne de caractères en une liste.

Voici ce que nous allons couvrir :

1. [Aperçu des chaînes de caractères et des listes](#introduction)
    1. [Comment vérifier le type de données d'un objet](#type)
2. [Convertir une chaîne de caractères en une liste de caractères individuels](#caracteres)
3. [Convertir une chaîne de caractères en une liste de mots](#mots)
    1. [Décomposition de la syntaxe de la méthode `split()`](#syntaxe)
    2. [Utiliser `split()` avec un séparateur](#separateur)
    3. [Utiliser `split()` avec le paramètre `maxsplit`](#maxsplit)
4. [Convertir une chaîne de nombres en une liste de nombres](#nombres)

## Qu'est-ce que les chaînes de caractères et les listes en Python ? <a name="introduction"></a>

Une **chaîne de caractères** est une séquence ordonnée de caractères. C'est une série de caractères, avec un caractère suivant l'autre.

Une chaîne de caractères est entourée soit de guillemets simples, soit de guillemets doubles :

```python
# tout ce qui suit sont des chaînes de caractères

# une chaîne de caractères enfermée dans des guillemets simples
prenom = 'John'

# une chaîne de caractères enfermée dans des guillemets doubles
nom = "Doe"
```

Si vous souhaitez créer une chaîne de caractères qui s'étend sur plusieurs lignes, ou ce que l'on appelle une chaîne de caractères multiline, utilisez des triples guillemets pour la commencer et la terminer :

```python
# une chaîne de caractères multiline enfermée dans des triples guillemets

phrase = '''J'apprends Python
et j'apprécie vraiment apprendre ce langage !
'''
```

Les chaînes de caractères sont *immuables*. Cela signifie que, une fois créées, elles ne peuvent pas changer. Les caractères individuels qui composent une chaîne de caractères ne peuvent pas être modifiés.

Par exemple, si vous essayez de changer la première lettre d'un mot de minuscule en majuscule, vous obtiendrez une erreur dans votre code :

```python
# essayer de changer le 'p' minuscule en 'P' majuscule
langage_favori = "python"
langage_favori[0] = "P"

print(langage_favori)

# la sortie sera un message d'erreur
# langage_favori[0] = "P"
# TypeError: 'str' object does not support item assignment
```

Cependant, vous pouvez réassigner une chaîne de caractères différente en mettant à jour la variable, comme ceci :

```python
langage_favori = "python"
langage_favori = "Python"

print(langage_favori)

# sortie
# Python
```

Une **liste** est une collection ordonnée de données.

Plusieurs éléments (généralement liés) sont stockés ensemble sous la même variable.

Vous pouvez créer une liste en enfermant zéro ou plusieurs éléments dans des crochets, `[]`, chacun séparé par une virgule.

Une liste peut contenir n'importe quel type de données intégré de Python.

```python
# une liste de nombres
ma_liste_de_nombres = [10, 20, 30, 40, 50]

print(ma_liste_de_nombres)

# sortie
# [10, 20, 30, 40, 50]
```

Les listes sont *mutables*.

Vous pouvez changer les éléments de la liste après que la liste a été créée. Cela signifie que vous pouvez modifier les éléments existants, ajouter de nouveaux éléments ou supprimer des éléments à tout moment pendant la durée de vie du programme.

```python
langages_de_programmation = ["Javascript", "Python", "Java"]

# mettre à jour le 1er élément de la liste
langages_de_programmation[0] = "JavaScript"

print(langages_de_programmation)

# sortie
# ['JavaScript', 'Python', 'Java']
```

### Comment déterminer le type de données d'un objet en Python <a name="type"></a>

Pour trouver le type de données d'un objet en Python, utilisez la fonction intégrée `type()`, qui a la syntaxe suivante :

```python
type(objet)

# où objet est l'objet dont vous devez trouver le type de données
```

La fonction `type()` retournera le type de l'objet qui a été passé comme argument à la fonction.

Cela est couramment utilisé à des fins de débogage.

Voyons comment utiliser `type()` avec des chaînes de caractères et des listes dans l'exemple ci-dessous :

```python
mon_nom = "John Doe"
mes_nombres_portes_bonheur = [7, 14, 33]

print(type(mon_nom))
print(type(mes_nombres_portes_bonheur))

# sortie
# <class 'str'>
# <class 'list'>
```

## Comment convertir une chaîne de caractères en une liste de caractères individuels <a name="caracteres"></a>

Vous pouvez prendre un mot et le transformer en une liste.

Chaque caractère qui compose ce mot devient un élément individuel et séparé à l'intérieur de la liste.

Par exemple, prenons le texte "Python".

Vous pouvez le convertir en une liste de caractères, où chaque élément de la liste serait chaque caractère qui compose la chaîne de caractères "Python".

Cela signifie que le caractère `P` serait un élément de la liste, le caractère `y` serait un autre élément de la liste, le caractère `t` serait un autre, et ainsi de suite.

La manière la plus simple est de transtyper la chaîne de caractères en une liste.

Le transtypage signifie convertir directement d'un type de données à un autre – dans ce cas, du type de données chaîne de caractères au type de données liste.

Vous faites cela en utilisant la fonction intégrée `list()` et en passant la chaîne de caractères donnée comme argument à la fonction.

```python
langage_de_programmation = "Python"

liste_langage_de_programmation = list(langage_de_programmation)

print(liste_langage_de_programmation)

# sortie
# ['P', 'y', 't', 'h', 'o', 'n']
```

Regardons un autre exemple :

```python
routine_actuelle = " Apprendre Python ! "

liste_routine_actuelle = list(routine_actuelle)

print(liste_routine_actuelle)

# sortie
# [' ', 'A', 'p', 'p', 'r', 'e', 'n', 'd', 'r', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '!', ' ']
```

Le texte `" Apprendre Python ! "` a des espaces en début et en fin, des espaces entre les mots "Apprendre" et "Python", et des espaces entre le mot "Python" et le point d'exclamation.

Lorsque la chaîne de caractères est convertie en une liste de caractères, chaque espace est traité comme un caractère individuel et c'est pourquoi vous voyez des espaces vides, `' '`, comme éléments de la liste.

Pour supprimer les espaces uniquement au début et à la fin de la chaîne de caractères, utilisez la méthode `strip()`.

```python
routine_actuelle = " Apprendre Python ! "

# les espaces en début et en fin ne seront plus des éléments séparés dans la liste
liste_routine_actuelle = list(routine_actuelle.strip())

print(liste_routine_actuelle)

# sortie
# ['A', 'p', 'p', 'r', 'e', 'n', 'd', 'r', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '!']
```

Pour supprimer *tous* les espaces et pas seulement ceux en début et en fin, et faire en sorte qu'aucun caractère d'espace ne soit inclus dans la nouvelle liste, utilisez plutôt la méthode `replace()` :

```python
routine_actuelle = " Apprendre Python ! "

# remplacer chaque instance d'espace par aucun espace
liste_routine_actuelle = list(routine_actuelle.replace(" ", ""))

print(liste_routine_actuelle)

# sortie
# ['A', 'p', 'p', 'r', 'e', 'n', 'd', 'r', 'e', 'P', 'y', 't', 'h', 'o', 'n', '!']
```

## Comment convertir une chaîne de caractères en une liste de mots <a name="mots"></a>

Une autre façon de convertir une chaîne de caractères en une liste est d'utiliser la méthode `split()` de Python.

La méthode `split()` divise une chaîne de caractères en une liste, où chaque élément de la liste est chaque mot qui compose la chaîne de caractères.

Chaque mot sera un élément individuel de la liste.

### Décomposition de la syntaxe de la méthode `split()` en Python <a name="syntaxe"></a>

La syntaxe générale de la méthode `split()` est la suivante :

```python
chaine.split(separateur=None, maxsplit=-1)
```

Décomposons-la :

- `chaine` est la chaîne de caractères donnée que vous souhaitez transformer en une liste.
- La méthode `split()` transforme une chaîne de caractères en une liste. Elle prend deux paramètres *optionnels*.
- `separateur` est le premier paramètre optionnel, et il détermine où la chaîne de caractères sera divisée. Par défaut, le séparateur est l'espace et la chaîne de caractères sera divisée partout où il y a un espace.
- `maxsplit` est le deuxième paramètre optionnel. Il spécifie le nombre maximum de divisions à effectuer. La valeur par défaut, `-1`, signifie qu'elle divise toute la chaîne de caractères et qu'il n'y a pas de limites à la division.

Voyons un exemple de fonctionnement.

```python
phrase = "J'apprends Python !"

print(type(phrase))

# sortie
# <class 'str'>
```

Dans la chaîne de caractères ci-dessus, chaque mot qui compose la chaîne de caractères est séparé par un espace.

Pour transformer cette chaîne de caractères en une liste de mots, utilisez la méthode `split()`.

Vous n'avez pas besoin de spécifier un séparateur ou un paramètre `maxsplit`, car nous voulons séparer tous les mots partout où il y a un espace entre eux.

```python
phrase = "J'apprends Python !"

phrase_en_liste = phrase.split()

print(phrase_en_liste)
print(type(phrase_en_liste))

# sortie
# ['J"', 'apprends', 'Python', '!']
# <class 'list'>
```

La chaîne de caractères a été divisée en fonction des espaces, et chaque mot qui composait la chaîne de caractères est devenu un élément individuel de la liste.

### Comment utiliser la méthode `split()` avec un séparateur <a name="separateur"></a>

Vous pouvez également convertir une chaîne de caractères en une liste en utilisant un séparateur avec la méthode `split()`. Le séparateur peut être n'importe quel caractère que vous spécifiez.

La chaîne de caractères sera divisée en fonction du séparateur que vous fournissez.

Par exemple, vous pouvez utiliser une virgule, `,`, comme séparateur.

La chaîne de caractères se transformera en une liste chaque fois qu'il y a une virgule, en commençant par la gauche.

Les éléments séparés par des virgules seront les éléments individuels de la liste.

Prenons la chaîne de caractères suivante :

```python
phrase = "Bonjour monde,J'apprends Python !"
```

Il y a une virgule qui sépare `Bonjour monde` de `J'apprends Python !`.

Si nous voulons utiliser cette virgule comme séparateur pour créer deux éléments individuels de la liste, nous ferions ce qui suit :

```python
phrase = "Bonjour monde,J'apprends Python !"

phrase_en_liste = phrase.split(",")

print(phrase_en_liste)

# sortie
# ['Bonjour monde', 'J"apprends Python !']
```

Deux éléments séparés ont été créés comme éléments de la liste et la séparation s'est produite là où il y avait une virgule.

Un autre exemple pourrait être de séparer un nom de domaine, chaque fois qu'il y a un point, `.`.

```python
nom_de_domaine = "www.freecodecamp.org"

liste_nom_de_domaine = nom_de_domaine.split(".")

print(liste_nom_de_domaine)

# sortie
# ['www', 'freecodecamp', 'org']
```

Chaque fois qu'il y a un point, un nouvel élément de la liste sera ajouté à la liste.

### Comment utiliser la méthode `split()` avec le paramètre `maxsplit` <a name="maxsplit"></a>

Comme mentionné précédemment, `maxsplit` est un paramètre optionnel de la méthode `split()`.

Il définit combien d'éléments de la liste seront divisés et transformés en éléments individuels de la liste. Par défaut, il est défini sur `-1`, ce qui signifie que tous les éléments qui composent la chaîne de caractères seront divisés.

Mais nous pouvons changer la valeur en un nombre spécifique.

Pour diviser seulement deux mots et non chaque mot, nous définissons `maxsplit` à deux :

```python
routine_actuelle = "J'aime apprendre Python tous les jours"

liste_routine_actuelle = routine_actuelle.split(maxsplit=2)

print(liste_routine_actuelle)

# sortie
# ['J"', 'aime', 'apprendre Python tous les jours']
```

`maxsplit` est défini sur `2`, ce qui signifie qu'un maximum de seulement deux mots sera divisé par espace et formera deux éléments individuels de la liste. Le troisième élément de la liste sera le reste des mots qui composent la chaîne de caractères initiale.

En utilisant un autre exemple de la section précédente, vous pouvez combiner un séparateur avec `maxsplit` pour faire une conversion ciblée d'une chaîne de caractères en une liste :

```python
nom_de_domaine = "www.freecodecamp.org"

liste_nom_de_domaine = nom_de_domaine.split(".", maxsplit=1)

print(liste_nom_de_domaine)

# sortie
# ['www', 'freecodecamp.org']
```

Dans cet exemple, le séparateur était un point et seul le premier élément a été divisé.

## Comment convertir une chaîne de nombres en une liste de nombres <a name="nombres"></a>

Les nombres sont considérés comme des chaînes de caractères lorsqu'ils sont enfermés dans des guillemets simples ou doubles.

Supposons que vous avez votre date de naissance stockée sous forme de chaîne de caractères, comme ceci :

```python
date_de_naissance = "19/10/1993"

print(type(date_de_naissance))

# sortie
# <class 'str'>
```

Pour supprimer les barres obliques et stocker les nombres associés au jour, au mois et à l'année de naissance comme éléments de liste séparés, vous feriez ce qui suit :

```python
date_de_naissance = "19/10/1993"

liste_date_de_naissance = date_de_naissance.split("/")

print(liste_date_de_naissance)
print(type(liste_date_de_naissance))

# sortie
# ['19', '10', '1993']
# <class 'list'>
```

Dans l'exemple, le séparateur était la barre oblique, `/`, et chaque fois qu'il y avait une barre oblique, un nouvel élément de la liste était créé.

Si vous regardez de plus près la sortie, vous verrez que les éléments de la liste sont toujours des chaînes de caractères, puisqu'ils sont entourés de guillemets simples et qu'il n'y a pas eu de conversion de type.

Pour convertir chaque élément de la liste d'une chaîne de caractères en un entier, utilisez la fonction `map`.

La fonction `map` prend deux arguments :

- Une fonction. Dans ce cas, la fonction sera la fonction `int`.
- Un itérable, qui est une séquence ou une collection d'éléments. Dans ce cas, l'itérable est la liste que nous avons créée.

```python
date_de_naissance = "19/10/1993"

liste_date_de_naissance = date_de_naissance.split("/")

str_en_int = (map(int, liste_date_de_naissance))

print(str_en_int)

# sortie
# <map object at 0x10e289960>
```

Ce n'est pas exactement la sortie que nous voulions. Lorsque nous vérifions le type de données, nous voyons que nous n'avons plus une liste :

```python
print(type(str_en_int))

# sortie
# <class 'map'>
```

Pour corriger cela, nous devons plutôt revenir en arrière et ajouter la fonction `list()` avant la conversion :

```python
date_de_naissance = "19/10/1993"

liste_date_de_naissance = date_de_naissance.split("/")

str_en_int = list(map(int, liste_date_de_naissance))

print(type(str_en_int))
print(str_en_int)

# sortie
# <class 'list'>
# [19, 10, 1993]
```

## Conclusion

Et voilà ! Vous connaissez maintenant certaines des façons de convertir une chaîne de caractères en une liste en Python.

Pour en savoir plus sur le langage de programmation Python, consultez la [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !