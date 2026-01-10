---
title: Python Supprimer une Clé d'un Dictionnaire – Comment Supprimer des Clés d'un
  Dict
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-22T15:36:57.000Z'
originalURL: https://freecodecamp.org/news/python-remove-key-from-dictionary
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Python-Remove-Key-from-Dictionary
seo_title: Python Supprimer une Clé d'un Dictionnaire – Comment Supprimer des Clés
  d'un Dict
---

How-to-Delete-Keys-from-a-Dict-by-Shittu-Olumide-1.png
tags:
- name: dictionnaire
  slug: dictionnaire
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nLes dictionnaires sont un type de données utile en Python pour stocker\
  \ des données dans un format clé-valeur. Et il arrive que vous deviez supprimer\
  \ une paire clé-valeur particulière d'un dictionnaire. \nVous apprendrez quelques\
  \ bases des dictionnaires, ainsi que ..."
---

Par Shittu Olumide

Les dictionnaires sont un type de données utile en Python pour stocker des données dans un format clé-valeur. Et il arrive que vous deviez supprimer une paire clé-valeur particulière d'un dictionnaire. 

Vous apprendrez quelques bases des dictionnaires, ainsi que comment supprimer des clés, dans ce tutoriel.

## Comment Écrire un Dict en Python

Les dictionnaires sont désignés par des accolades `{}` et les paires clé-valeur sont séparées par des deux-points `:`. Par exemple, le code suivant initialise un dictionnaire avec trois paires clé-valeur :

```py
my_dict = {'apple': 2, 'banana': 3, 'orange': 5}

```

Vous pouvez également initialiser des dictionnaires en utilisant la fonction intégrée `dict()`. Par exemple :

```py
my_dict = dict(apple=2, banana=3, orange=5)

```

Maintenant, je vais vous apprendre comment supprimer des clés d'un dictionnaire Python de manière sécurisée. Lorsque je dis "de manière sécurisée", je veux dire que si la clé n'existe pas réellement dans le dictionnaire, le code ne générera pas d'erreur. 

Nous allons découvrir comment accomplir cela en utilisant le mot-clé `del`, la méthode `pop()`, et la méthode `popitem()`. Enfin, vous verrez comment utiliser Python pour supprimer plusieurs clés d'un dictionnaire.

Commençons !

## Comment Supprimer une Clé d'un Dict en Utilisant le Mot-Clé `del`

La méthode la plus populaire pour supprimer une paire clé:valeur d'un dictionnaire est d'utiliser le mot-clé `del`. Vous pouvez également l'utiliser pour éliminer un dictionnaire entier ou des mots spécifiques. 

Utilisez simplement la syntaxe montrée ci-dessous pour accéder à la valeur que vous devez supprimer :

```py
del dictionary[key]

```

Examinons un exemple :

```py
Members = {"John": "Male", "Kat": "Female", "Doe": "Female", "Clinton": "Male"}

del Members["Doe"]
print(Members)

```

Sortie :

```bash
{"John": "Male", "Kat": "Female", "Clinton": "Male"}

```

## Comment Supprimer une Clé d'un Dict en Utilisant la Méthode `pop()`

Une autre technique pour supprimer une paire clé-valeur d'un dictionnaire est d'utiliser la méthode `pop()`. La syntaxe est montrée ci-dessous :

```py
dictionary.pop(key, default_value)

```

Exemple :

```py
My_Dict = {1: "Mathew", 2: "Joe", 3: "Lizzy", 4: "Amos"}
data = My_Dict.pop(1)
print(data)
print(My_Dict)

```

Sortie :

```bash
Mathew
{2: "Joe", 3: "Lizzy", 4: "Amos"}

```

## Comment Supprimer une Clé d'un Dict en Utilisant la Fonction `popitem()`

La fonction intégrée `popitem()` élimine la dernière paire clé:valeur d'un dictionnaire. L'élément qui doit être supprimé ne peut pas être spécifié et la fonction n'accepte aucune entrée.

La syntaxe ressemble à ceci :

```py
dict.popitem()

```

Considérons un exemple pour une meilleure compréhension.

```py
# initialiser un dictionnaire
My_dict = {1: "Red", 2: "Blue", 3: "Green", 4: "Yello", 5: "Black"}

# utiliser popitem()
Deleted_key = My_dict.popitem()
print(Deleted_key)

```

Sortie :

```bash
(5, 'Black')

```

Comme vous pouvez le voir, la fonction a supprimé la dernière paire clé:valeur – `5: "Black"` – du dictionnaire.

## Comment Supprimer Plusieurs Clés d'un Dict

Vous pouvez facilement supprimer plusieurs clés d'un dictionnaire en utilisant Python. La méthode `.pop()`, utilisée dans une boucle sur une liste de clés, est l'approche la plus sûre pour faire cela.

Examinons comment nous pouvons fournir une liste de clés uniques à supprimer, y compris certaines qui ne sont pas présentes :

```py
My_dict = {'Sam': 16, 'John': 19, 'Alex': 17, 'Doe': 15}

# définir les clés à supprimer
keys = ['Sam', 'John', 'Doe']

for key in keys:
    My_dict.pop(key, None)

print(My_dict)

```

Sortie :

```bash
{'Alex': 17}

```

Une chose à noter est que dans la méthode `pop()` à l'intérieur de la boucle, nous passons `None` et la valeur par défaut, juste pour être sûr qu'aucun `KeyError` ne soit imprimé si une clé n'existe pas.

## Comment Supprimer Toutes les Clés d'un Dict en Utilisant la Méthode `clear()`

Vous pouvez utiliser la méthode `clear()` pour supprimer toutes les paires clé-valeur d'un dictionnaire. La syntaxe est la suivante :

```py
dictionary.clear()

```

Exemple :

```py
Colors = {1: "Red", 2: "Blue", 3: "Green"}
Colors.clear()
print(Colors)

```

Sortie :

```bash
{}

```

## Conclusion

Pour supprimer une paire clé-valeur ou plusieurs paires clé-valeur d'un dictionnaire, nous avons discuté de diverses méthodes Python dans cet article. 

Vous pouvez le faire en utilisant le mot-clé `del`, qui est la méthode la plus courante pour supprimer une paire clé-valeur d'un dictionnaire. La méthode `pop()` est utile lorsque nous devons supprimer une paire clé-valeur et obtenir également la valeur de la paire clé-valeur. En utilisant la fonction `popitem()`, nous pouvons supprimer la dernière paire clé-valeur d'un dictionnaire. 

De plus, si vous devez supprimer toutes les paires clé:valeur d'un dictionnaire, vous pouvez utiliser la méthode `clear()`.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon Codage !