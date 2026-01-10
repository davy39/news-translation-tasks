---
title: Méthodes de liste Python – append() vs extend() en Python expliquées avec des
  exemples de code
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-06-21T21:25:11.000Z'
originalURL: https://freecodecamp.org/news/python-list-methods-append-vs-extend
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/append
seo_title: Méthodes de liste Python – append() vs extend() en Python expliquées avec
  des exemples de code
---

vs-e-x-t-e-n-d--.png
étiquettes:
- nom: Python
  slug: python
seo_title: null
seo_desc: 'Lorsque vous travaillez avec des listes Python, vous devez souvent combiner des données
  provenant de plusieurs listes. Alors, comment faire ?

  Dans ce tutoriel, nous verrons les différentes façons de combiner des données provenant de plusieurs
  listes. Nous apprendrons également comment fonctionnent les méthodes de liste append() ...'
---

Lorsque vous travaillez avec des listes Python, vous devez souvent combiner des données provenant de plusieurs listes. Alors, comment faire ?

Dans ce tutoriel, nous verrons les différentes façons de combiner des données provenant de plusieurs listes. Nous apprendrons également comment fonctionnent les méthodes de liste `append()` et `extend()` à travers des exemples simples. Commençons.

## Comment utiliser l'opérateur '+' en Python

Avant de voir comment fonctionnent les méthodes `append()` et `extend()`, voyons ce que fait l'opérateur `+` pour concaténer des listes.

Considérons l'exemple suivant où nous avons deux listes, `list_1` et `list_2`, que nous aimerions concaténer (ou joindre bout à bout) :

```python
list_1 = [1,2,3,4,5]
list_2 = [6,7,8]

print(list_1 + list_2)
# Sortie
[1, 2, 3, 4, 5, 6, 7, 8]

print(list_1)
# Sortie
[1, 2, 3, 4, 5]

print(list_2)
# Sortie
[6, 7, 8]
```

Si vous lisez attentivement l'extrait de code ci-dessus, vous pouvez voir ce qui suit.

* `list_1 + list_2` n'ajoute pas les éléments de `list_2` à `list_1`.
* Au lieu de cela, il crée une _nouvelle liste_ contenant les éléments de `list_1` et `list_2`.
* Par conséquent, `list_1` et `list_2` restent inchangées.

Que faire si nous voulons modifier `list_1` au lieu de créer une nouvelle liste ? Eh bien, faisons exactement cela en utilisant les méthodes `append()` et `extend()` dans la section suivante.

## Comment utiliser la méthode append() en Python

Dans cette section, nous allons ajouter des éléments de `list_2` à `list_1` en utilisant des méthodes de liste. En considérant les mêmes listes d'exemple de la section précédente, essayons maintenant de modifier `list_1` en ajoutant des éléments de `list_2`.

L'extrait de code ci-dessous appelle la méthode `append()` sur `list_1` avec `list_2` comme argument.

```python
# Ajoutons list_2 à list_1
list_1.append(list_2)
print(list_1)

# Sortie
[1, 2, 3, 4, 5, [6, 7, 8]]


# imprimer la longueur de list_1
print(len(list_1))

# Sortie
6
```

Nous voyons que `list_2` a été ajoutée comme un _seul élément de liste à la fin de_ `list_1`.
Cela signifie que la longueur de `list_1` _augmente de 1_ après l'opération `append()`.

Que faire si nous voulons ajouter des éléments de `list_2` à `list_1` non pas comme une seule liste à la fin de `list_1`, mais comme des éléments individuels ? Faisons cela dans la section suivante.

## Comment utiliser la méthode extend() en Python

Avant de commencer à utiliser la méthode `extend()`, faisons ce qui suit.

* Parcourir `list_2`
* _Ajouter_ chaque élément de `list_2` à `list_1`

```python
for item in list_2:
  list_1.append(item)

print(list_1)

# Sortie
[1, 2, 3, 4, 5, 6, 7, 8]
```

Nous avons maintenant ajouté tous les éléments de `list_2` à `list_1` exactement comme nous le voulions. 😀
Nous pouvons faire la même chose en appelant la méthode `extend()` sur `list_1` avec `list_2` comme argument. Vous pouvez voir comment cela fonctionne dans l'extrait de code ci-dessous :

```python
# Étendons list_1 avec les éléments de list_2
list_1.extend(list_2)
print(list_1)

# Sortie
[1, 2, 3, 4, 5, 6, 7, 8]

# imprimer la longueur de list_1
print(len(list_1))

# Sortie
8
```

Ainsi, si vous étendez une liste de longueur `len1` avec une liste de longueur `len2`, la longueur de la liste sur laquelle la méthode `extend()` est appelée est `len1 + len2`.

### Y a-t-il des pièges ?

Que faire si nous voulons ajouter un seul élément et non la liste entière (ou un itérable) à notre liste existante ? Dans l'exemple suivant, ajoutons la valeur booléenne `True` à `list_1` en utilisant `append()` comme montré ci-dessous.

```python
list_1 = [1,2,3,4,5]
list_1.append(True)
print(list_1)

# Sortie
[1, 2, 3, 4, 5, True]
```

Que faire si nous essayons d'utiliser `extend()` pour faire la même chose que ci-dessus ?

```python
list_1 = [1,2,3,4,5]
list_1.extend(True)
print(list_1)

# Sortie
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-9e4e0d6da67b> in <module>()
      1 list_1 = [1,2,3,4,5]
----> 2 list_1.extend(True)
      3 print(list_1)

TypeError: 'bool' object is not iterable
```

Oh, cela génère une erreur. 😢 Essayons d'analyser le message d'erreur qui est retourné. `TypeError: 'bool' object is not iterable`. Cela signifie que notre argument était d'un _type incorrect_.

La méthode `extend()` nécessite que l'argument soit itérable. En interne, la méthode `extend()` fonctionne en parcourant l'itérable et en ajoutant chaque élément de l'itérable à la première liste. Les listes, les ensembles, les tuples et les chaînes sont tous des exemples d'itérables.

Tout objet que vous pouvez parcourir et accéder à des éléments individuels est un **itérable**. Notez que la syntaxe générale pour utiliser la méthode `extend()` est `list_name.extend(iterable)`.

## Essayons extend() et append() sur des chaînes

Les chaînes sont essentiellement une séquence de caractères et sont donc itérables. Essayons d'utiliser les méthodes `extend()` et `append()` sur `list_1` avec une chaîne comme argument.

Ajoutons la chaîne _'Happy'_ à `list_1` en utilisant la méthode `append()`.

```python
list_1 = [1,2,3,4,5]
list_1.append('Happy')
print(list_1)

# Sortie
[1, 2, 3, 4, 5, 'Happy']
```

Essayons maintenant d'ajouter la même chaîne en utilisant la méthode `extend()`. Cette fois, nous ne devrions pas obtenir d'erreur. Au lieu de cela, la méthode extend devrait parcourir la chaîne et ajouter chaque caractère à `list_1`.

Vérifions que cela fonctionne dans l'exemple de code suivant. 😊

```python
list_1 = [1,2,3,4,5]
list_1.extend('Happy')
print(list_1)

# Sortie
[1, 2, 3, 4, 5, 'H', 'a', 'p', 'p', 'y']
```

Il est assez intuitif de voir que la méthode `append()` s'exécute en _temps constant_, tandis que la méthode `extend()` devrait avoir un temps d'exécution proportionnel à la longueur de l'itérable qui est passé comme argument à la méthode.

## Conclusion

J'espère que cet article clarifie comment utiliser les méthodes `append()` et `extend()` en Python. Merci pour votre lecture, et bon apprentissage et codage !

### Articles connexes

Pour une introduction générale aux listes Python et aux méthodes de liste courantes, veuillez consulter cet article : [Lists in Python - A Comprehensive Guide.](https://www.freecodecamp.org/news/lists-in-python-comprehensive-guide/)