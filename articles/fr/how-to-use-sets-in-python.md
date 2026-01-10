---
title: Comment utiliser les ensembles en Python – Expliqué avec des exemples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-03-04T12:54:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-sets-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-3-.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Comment utiliser les ensembles en Python – Expliqué avec des exemples
seo_desc: 'In the vast landscape of Python programming, understanding data structures
  is akin to possessing a versatile toolkit. Among the essential tools in this arsenal
  is the Python set. Sets in Python offer a unique way to organize and manipulate
  data.

  Let''...'
---

Dans le vaste paysage de la programmation Python, comprendre les structures de données revient à posséder une boîte à outils polyvalente. Parmi les outils essentiels de cet arsenal se trouve l'ensemble Python. Les ensembles en Python offrent une manière unique d'organiser et de manipuler des données.

Embarquons pour un voyage afin de démêler les mystères des ensembles, en commençant par une analogie qui parallèle leur fonctionnalité à des scénarios du monde réel.

Vous pouvez obtenir tout le code source à partir d'[ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/python/python-set/main.py).

## Table des matières

* [Qu'est-ce que les ensembles en Python ?](#heading-quest-ce-que-les-ensembles-en-python)
* [Comment créer des ensembles](#heading-comment-creer-des-ensembles)
* [Opérations de base](#heading-operations-de-base)
* [Opérations sur les ensembles](#heading-operations-sur-les-ensembles)
* [Autres opérations utiles](#heading-autres-operations-utiles)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que les ensembles en Python ?

Imaginez que vous organisez une réunion d'amis issus de milieux divers, chacun avec son identité unique. Imaginez maintenant cette réunion comme un ensemble – une collection où chaque individu est distinct, tout comme les éléments d'un ensemble en Python.

Tout comme aucun des invités à votre réunion ne partage la même identité, aucun des éléments d'un ensemble n'est identique. Cette notion d'unicité est au cœur des ensembles.

## Comment créer des ensembles

En Python, vous pouvez créer un ensemble en utilisant des accolades `{}` ou le constructeur `set()`. Tout comme l'envoi d'invitations à votre réunion, la création d'un ensemble implique de spécifier les éléments uniques que vous souhaitez inclure :

```python
# Syntaxe : Création d'ensembles en utilisant des accolades

# Exemple :
ensemble_invites1 = {"Alice", "Bob", "Charlie", "David", "Eve"}

# Syntaxe : Création d'ensembles en utilisant le constructeur set()

# Exemple :
ensemble_invites2 = set(["David", "Eve", "Frank", "Grace", "Helen"])


```

## Opérations de base

### Comment ajouter des éléments à un ensemble

Ajouter des éléments à un ensemble reflète l'acte d'accueillir de nouveaux invités à votre réunion. Vous pouvez utiliser la méthode `add()` pour inclure un nouvel élément :

```python
# Syntaxe : Ajout d'éléments en utilisant la méthode add()

# Exemple :
ensemble_invites1.add("Frank")

print(ensemble_invites1)  # Sortie : {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}


```

Ici, la méthode `add()` ajoute le nom "Frank" à `ensemble_invites1`, représentant l'arrivée d'un nouvel invité nommé Frank à votre réunion.

### Comment supprimer des éléments d'un ensemble

De même, supprimer des éléments d'un ensemble symbolise le fait de dire au revoir aux invités qui partent. Vous pouvez utiliser des méthodes comme `remove()` ou `discard()` à cet effet :

```python
# Syntaxe : Suppression d'éléments en utilisant la méthode remove()

# Exemple :
ensemble_invites1.remove("Charlie")

print(ensemble_invites1)  # Sortie : {'Alice', 'Bob', 'David', 'Eve', 'Frank'}

# Syntaxe : Suppression d'éléments en utilisant la méthode discard()

# Exemple :
ensemble_invites1.discard("Bob")

print(ensemble_invites1)  # Sortie : {'Alice', 'David', 'Eve', 'Frank'}


```

Dans le premier exemple, la méthode `remove()` supprime le nom "Charlie" de `ensemble_invites1`, simulant le départ de l'invité nommé Charlie de votre réunion.

Dans le deuxième exemple, la méthode `discard()` supprime le nom "Bob" de `ensemble_invites1`, indiquant le départ d'un autre invité nommé Bob.

### Comment obtenir la longueur d'un ensemble

Tout comme vous pourriez compter le nombre d'invités à votre réunion, vous pouvez déterminer la longueur d'un ensemble en utilisant la fonction `len()` :

```python
# Syntaxe : Obtenir la longueur d'un ensemble en utilisant la fonction len()

# Exemple :
print(len(ensemble_invites1))  # Sortie : 4


```

La fonction `len()` retourne le nombre d'éléments dans `ensemble_invites1`, indiquant le nombre total d'invités présents à votre réunion.

## Opérations sur les ensembles

### Comment joindre des ensembles

L'union de deux ensembles combine les éléments des deux réunions, en veillant à ce qu'il n'y ait pas de doublons :

```python
# Syntaxe : Union d'ensembles en utilisant la méthode union()

# Exemple :
tous_les_invites = ensemble_invites1.union(ensemble_invites2)

print(tous_les_invites)  # Sortie : {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen'}

```

Ici, la méthode `union()` combine `ensemble_invites1` et `ensemble_invites2` en un nouvel ensemble nommé `tous_les_invites`, représentant la liste combinée des invités des deux réunions sans aucun doublon.

### Intersection – Comment trouver des intérêts communs

L'intersection identifie les éléments communs aux deux ensembles, tout comme trouver des intérêts partagés parmi les invités :

```python
# Syntaxe : Intersection d'ensembles en utilisant la méthode intersection()

# Exemple :
invites_communs = ensemble_invites1.intersection(ensemble_invites2)

print(invites_communs)  # Sortie : {'David', 'Eve'}


```

La méthode `intersection()` identifie les invités communs présents dans `ensemble_invites1` et `ensemble_invites2`, les stockant dans l'ensemble `invites_communs`.

### Différence – Comment trouver des attributs uniques

La différence entre les ensembles montre les éléments uniques à chaque réunion, analogues aux caractéristiques individuelles :

```python
# Syntaxe : Différence entre les ensembles en utilisant la méthode difference()

# Exemple :
uniques_a_ensemble_invites1 = ensemble_invites1.difference(ensemble_invites2)

print(uniques_a_ensemble_invites1)  # Sortie : {'Alice', 'Frank'}


```

La méthode `difference()` identifie les invités présents dans `ensemble_invites1` mais pas dans `ensemble_invites2`, les stockant dans l'ensemble `uniques_a_ensemble_invites1`.

### Différence symétrique – Comment trouver des éléments exclusifs

La différence symétrique révèle les éléments exclusifs à chaque réunion, semblables à des privilèges ou expériences uniques :

```python
# Syntaxe : Différence symétrique entre les ensembles en utilisant la méthode symmetric_difference()

# Exemple :
invites_exclusifs = ensemble_invites1.symmetric_difference(ensemble_invites2)

print(invites_exclusifs)  # Sortie : {'Bob', 'Charlie', 'Grace', 'Alice', 'Frank', 'Helen'}


```

La méthode `symmetric_difference()` identifie les invités présents exclusivement dans `ensemble_invites1` ou `ensemble_invites2`, les stockant dans l'ensemble `invites_exclusifs`.

## Autres opérations utiles

### Comment vérifier les sous-ensembles et sur-ensembles – Dynamique de groupe

Vous pouvez déterminer si un ensemble est un sous-ensemble ou un sur-ensemble d'un autre, reflétant la dynamique de groupe au sein des réunions :

```python
# Syntaxe : Vérification de sous-ensemble en utilisant la méthode issubset()

# Exemple :
print(ensemble_invites1.issubset(tous_les_invites))  # Sortie : True

# Syntaxe : Vérification de sur-ensemble en utilisant la méthode issuperset()

# Exemple :
print(tous_les_invites.issuperset(ensemble_invites1))  # Sortie : True


```

Ces méthodes vérifient si `ensemble_invites1` est un sous-ensemble de `tous_les_invites` et si `tous_les_invites` est un sur-ensemble de `ensemble_invites1`, respectivement, indiquant la relation entre les deux réunions.

### Comment vider un ensemble

Vider un ensemble supprime tous les éléments, semblables à la réinitialisation de la réunion pour un nouveau départ :

```python
# Syntaxe : Vider un ensemble en utilisant la méthode clear()

# Exemple :
ensemble_invites1.clear()

print(ensemble_invites1)  # Sortie : set()


```

La méthode `clear()` supprime tous les éléments de `ensemble_invites1`, le réinitialisant effectivement à un ensemble vide.

## Conclusion

En comprenant l'analogie et les opérations décrites dans ce guide, vous êtes équipé pour exploiter la puissance des ensembles dans votre voyage Python.

Bon codage, et que vos réunions – à la fois numériques et physiques – soient remplies d'expériences uniques et d'interactions fructueuses !

Si vous avez des commentaires, envoyez-moi un message sur [Twitter](https://twitter.com/introvertedbot) ou [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).