---
title: Ajouter à un Dict en Python – Comment Ajouter à un Dictionnaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-28T00:17:11.000Z'
originalURL: https://freecodecamp.org/news/add-to-dict-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Shittu-Olumide-Adding-to-Dict-in-Python
seo_title: Ajouter à un Dict en Python – Comment Ajouter à un Dictionnaire
---

How-to-Append-to-a-Dictionary-1.png
tags:
- name: dictionnaire
  slug: dictionnaire
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nUn dictionnaire en Python est un groupe d'éléments non ordonnés,\
  \ chacun ayant un ensemble unique de clés et de valeurs. \nTout type de données immutable,\
  \ tel qu'une chaîne, un nombre ou un tuple, peut être utilisé comme clé. Il sert d'identifiant exclusif\
  \ pour ..."
---

Par Shittu Olumide

Un dictionnaire en Python est un groupe d'éléments non ordonnés, chacun ayant un ensemble unique de clés et de valeurs. 

Tout type de données immutable, tel qu'une chaîne, un nombre ou un tuple, peut être utilisé comme clé. Il sert d'identifiant exclusif pour la valeur dans le dictionnaire. La valeur est répétable et applicable à tous les types de données.

En Python, les dictionnaires sont désignés par des accolades `{ }`, et chaque paire clé-valeur est délimitée par un deux-points `:`. Une virgule sépare la clé et la valeur. Voici une illustration d'un dictionnaire de base :

```py
my_dict = {"pineapple": 12, "apple": 30, "orange": 5, "avocado":7}

```

Dans cet exemple, "pineapple", "apple", "orange" et "avocado" sont les clés, et 12, 30, 5 et 7 sont les valeurs correspondantes.

Nous allons voir comment ajouter une seule paire clé-valeur à un dictionnaire en utilisant la méthode `update()`, et enfin le constructeur `dict()`.

### Comment ajouter une seule paire clé-valeur à un dictionnaire

Pour ajouter une seule paire clé-valeur à un dictionnaire en Python, nous pouvons utiliser le code suivant :

```py
myDict = {'a': 1, 'b': 2}
myDict['c'] = 3

```

Le code ci-dessus créera un dictionnaire `myDict` avec deux paires clé-valeur. Ensuite, nous avons ajouté une nouvelle paire clé-valeur `'c' : 3` au dictionnaire en assignant simplement la valeur `3` à la clé `'c'`. Après l'exécution du code, le dictionnaire `myDict` contiendra maintenant la paire clé-valeur `'c': 3`.

Confirmons cela en imprimant le dictionnaire.

```py
print(myDict)

```

Sortie :

```bash
{'a': 1, 'b': 2, 'c': 3}

```

S'il y a déjà une clé `'c'` dans le dictionnaire, la valeur sera mise à jour à 3.

### Comment ajouter plusieurs paires clé-valeur avec la méthode `update()`

Plusieurs paires clé-valeur peuvent être ajoutées simultanément à un dictionnaire en utilisant la méthode `update()`. Cette méthode insère de nouvelles entrées dans le dictionnaire original à partir d'un autre dictionnaire ou d'un itérable de paires clé-valeur en entrée. La valeur d'une clé existante dans le dictionnaire original sera mise à jour avec la nouvelle valeur.

Exemple utilisant la méthode `update()` pour ajouter plusieurs entrées à un dictionnaire :

```py
myDict = {'a': 1, 'b': 2}
new_data = {'c': 3, 'd': 4}

myDict.update(new_data)

print(myDict)

```

Sortie :

```bash
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

```

Une autre chose intéressante à propos de cette méthode est que nous pouvons utiliser la méthode `update()` avec un itérable de paires clé-valeur, tel qu'une liste de tuples. Voyons cela en action.

```py
myDict = {'a': 1, 'b': 2}
new_data = [('c', 3), ('d', 4)]

myDict.update(new_data)

print(myDict)

```

La sortie est la même que dans l'exemple précédent :

```bash
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

```

### Comment mettre à jour un dictionnaire en utilisant le constructeur `dict()`

En Python, un dictionnaire peut être mis à jour ou créé à partir de zéro en utilisant le constructeur `dict()`. En passant un dictionnaire contenant la nouvelle paire clé-valeur comme argument au constructeur `dict()`, nous pouvons ajouter une seule paire clé-valeur à un dictionnaire existant.

Exemple :

```py
myDict = {'a': 1, 'b': 2, 'c': 3}
newDict = dict(myDict, d=4)

print(newDict)

```

Sortie :

```bash
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

```

Dans cet exemple, trois paires clé-valeur ont été ajoutées à un tout nouveau dictionnaire appelé `myDict`. Ensuite, nous avons créé un nouveau dictionnaire appelé `newDict` en utilisant le constructeur `dict()`, qui a également ajouté la paire clé-valeur `'d': 4'`. 

Lorsque les deux dictionnaires sont combinés par le constructeur `dict()`, toute clé présente dans les deux dictionnaires voit sa valeur écrasée par la valeur du deuxième dictionnaire (dans ce cas, `'d': 4'`).

Gardez à l'esprit qu'un nouveau dictionnaire peut également être créé en utilisant le constructeur `dict()` à partir d'une liste de paires clé-valeur, où chaque paire est représentée par un tuple.

```py
MyList = [('a', 1), ('b', 2), ('c', 3)]
MyDict = dict(MyList)

print(MyDict)

```

Sortie :

```bash
{'a': 1, 'b': 2, 'c': 3}

```

## Conclusion

En Python, les dictionnaires sont fréquemment utilisés pour stocker des données et fournir un accès rapide à celles-ci en utilisant une clé distincte. Ils sont pratiques lorsque l'on travaille avec des listes ou des tuples, où nous devons accéder aux données en utilisant un identifiant spécifique plutôt que leur position dans une séquence.

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !