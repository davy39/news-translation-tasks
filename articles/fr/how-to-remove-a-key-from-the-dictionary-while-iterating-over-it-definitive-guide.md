---
title: Comment supprimer une clé d'un dictionnaire tout en itérant dessus
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2022-07-06T21:56:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-key-from-the-dictionary-while-iterating-over-it-definitive-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Freecodecamp_dictionary_delete_iterate.jpeg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Comment supprimer une clé d'un dictionnaire tout en itérant dessus
seo_desc: 'Python dictionaries allow you to store values in a Key and Value format.

  You can access the values using the key. You can also iterate through the complete
  dictionary to access every element.

  Sometimes while iterating through the dictionary, you may ...'
---

Les dictionnaires Python vous permettent de stocker des valeurs dans un format `Clé` et `Valeur`.

Vous pouvez accéder aux valeurs en utilisant la clé. Vous pouvez également itérer à travers le dictionnaire complet pour accéder à chaque élément.

Parfois, lors de l'itération à travers le dictionnaire, vous devrez peut-être supprimer une clé du dictionnaire.

Ce tutoriel vous apprendra à supprimer une clé d'un dictionnaire **tout en itérant dessus**.

Pour supprimer une clé directement sans itérer, lisez le tutoriel freeCodeCamp [Comment supprimer une clé d'un dictionnaire Python](https://www.freecodecamp.org/news/how-to-remove-a-key-from-a-python-dictionary-delete-key-from-dict/).

## Comment créer un dictionnaire

Commençons par créer un dictionnaire avec quelques paires clé-valeur en utilisant l'opérateur d'assignation.

Pour ajouter une clé au dictionnaire en utilisant différentes méthodes, lisez [Comment ajouter une clé à un dictionnaire](https://www.stackvidhya.com/python-add-key-to-dictionary/)

Après avoir créé le dictionnaire, vous pouvez utiliser la boucle `for` pour itérer à travers et imprimer les valeurs afin de vérifier si le dictionnaire a été créé avec succès.

**Voici le code :**

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for key in yourdict.keys():
    print(key, yourdict[key])

```

Vous pouvez imprimer les valeurs du dictionnaire comme suit.

**Sortie :**

```
    one 1
    two 2
    three 3
    four 4

```

Pour vérifier si une clé existe dans un dictionnaire sans itérer dessus, lisez [comment vérifier si une clé existe dans un dictionnaire en Python](https://www.stackvidhya.com/check-if-key-exists-in-dictionary-python/).

## Comment vérifier la version de Python

Python 2 et Python 3 fonctionnent _différemment_ lorsque vous essayez de supprimer une clé d'un dictionnaire tout en itérant.

Pour vérifier quelle version de Python vous utilisez, utilisez l'extrait de code ci-dessous.

**Voici le code :**

```python
import sys
print(sys.version)

```

**Sortie :**

```
3.8.2 (default, Sep  4 2020, 00:03:40) [MSC v.1916 32 bit (Intel)]

```

Vous verrez la version que vous avez. Et maintenant, vous savez quelle version de Python vous utilisez.

Vous pouvez suivre les méthodes appropriées expliquées ci-dessous.

## Comment supprimer une clé d'un dictionnaire en fonction de la valeur de la clé – Python 3

Cette section vous apprend à supprimer une clé d'un dictionnaire en utilisant Python 3.

Vous devez convertir les `keys` en une `list` en utilisant `list(dict.keys())` et [itérer à travers un dictionnaire](https://www.stackvidhya.com/iterate-through-dictionary-python/) en utilisant la boucle `for`.

Lors de la conversion des `keys` en une `list`, Python 3 crée une _nouvelle copie_ des clés dans la liste. Il n'y aura aucune référence au dictionnaire pendant l'itération.

Si vous ne le convertissez pas en une liste, alors la méthode [keys](https://docs.python.org/3/library/stdtypes.html#dict.keys) retourne simplement une nouvelle vue des clés avec référence au dictionnaire actuellement itéré.

Maintenant, lors de chaque itération de la liste des clés, vous pouvez vérifier si la `key` est _égale à l'élément_ que vous souhaitez _supprimer_. Si c'est `True`, vous pouvez supprimer la `key` en utilisant l'instruction `del`.

**Voici le code :**

Le code ci-dessous montre comment supprimer une clé du dictionnaire tout en itérant dessus en utilisant Python 3.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for k in list(yourdict.keys()):
    if k == "four":
        del yourdict[k]

yourdict

```

Comme vous pouvez le voir dans le code ci-dessous, la clé _four_ est supprimée du dictionnaire tout en itérant dessus.

**Sortie :**

```
    {'one': 1, 'two': 2, 'three': 3}

```

Si vous utilisez la méthode `dict.keys()` pour itérer et émettez une instruction `del`, vous verrez l'erreur ci-dessous dans Python 3.

```python
RuntimeError: dictionary changed size during iteration

```

## Comment supprimer une clé d'un dictionnaire en fonction des valeurs – Python 3

Cette section vous apprend à supprimer une clé d'un dictionnaire en fonction de la valeur de la clé tout en itérant sur le dictionnaire.

Tout d'abord, vous devez convertir les clés du dictionnaire en une `list` en utilisant la méthode `list(dict.keys())`.

Lors de chaque itération, vous pouvez vérifier si la _valeur d'une clé_ est égale à la valeur souhaitée. Si c'est `True`, vous pouvez émettre l'instruction `del` pour supprimer la clé.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for k in list(yourdict.keys()):
    if yourdict [k] == 4:
        del yourdict[k]

print(yourdict)

```

La clé _four_ est supprimée en fonction de sa valeur _4_.

**Sortie :**

```python
{'three': 3, 'two': 2, 'one': 1}

```

## Comment supprimer une clé d'un dictionnaire en fonction de la clé – Python 2

Cette section vous apprend à supprimer une clé d'un dictionnaire tout en itérant dessus en utilisant Python 2.

Vous pouvez directement [itérer à travers un dictionnaire](https://www.stackvidhya.com/iterate-through-dictionary-python/) en utilisant la méthode `dict.keys()`. Dans Python 2, la méthode `dict.keys()` crée une copie des clés et itère sur la `copie` au lieu d'itérer à travers les clés directement. Il n'y aura donc _aucune référence_ directe au dictionnaire pendant l'itération.

Maintenant, lors de chaque itération, vous pouvez vérifier si l'élément est _égal à la clé_ que vous souhaitez supprimer. Et s'il est égal, vous pouvez émettre l'instruction `del`. Cela supprimera la clé du dictionnaire.

**Voici le code :**

Le code ci-dessous montre comment supprimer une clé d'un dictionnaire tout en itérant dessus en utilisant Python 2.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for k in yourdict.keys():
    if k == "four":
        del yourdict[k]

yourdict

```

La clé _four_ est supprimée, et seuls les autres éléments sont disponibles dans le dictionnaire.

**Sortie :**

```
    {'one': 1, 'two': 2, 'three': 3}

```

C'est ainsi que vous pouvez supprimer une clé en fonction de la clé.

## Comment supprimer une clé dans un dictionnaire en fonction des valeurs – Python 2

Cette section vous apprend à supprimer une clé d'un dictionnaire en fonction de la valeur de la clé tout en itérant sur le dictionnaire.

Itérez sur le dictionnaire en utilisant la méthode `dict.items()`. Elle retournera la paire clé-valeur lors de chaque itération.

Ensuite, vous pouvez vérifier si la `value` de l'itération actuelle _est égale à la valeur souhaitée_ à supprimer. Ensuite, émettez l'instruction `del` pour supprimer la clé du dictionnaire.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for key, val in yourdict.items():
    if val == 3:
        del yourdict[key]

print(yourdict)

```

La clé _three_ est supprimée en fonction de sa valeur _3_. Tous les autres éléments sont disponibles dans le dictionnaire.

**Sortie :**

```python
{'four': 4, 'two': 2, 'one': 1}

```

## Pourquoi Python 3 et Python 2 fonctionnent-ils différemment ?

Lors de l'utilisation de la méthode `dict.keys()`, Python 3 retourne une _vue_ des clés. Cela signifie qu'il y a une référence au dictionnaire pendant l'itération.

En revanche, Python 2 retourne une _copie_ des clés, ce qui signifie qu'il n'y a AUCUNE référence au dictionnaire pendant l'itération. Cela signifie que la suppression sera réussie sans problèmes.

## Conclusion

Dans cet article, vous avez appris à supprimer une clé d'un dictionnaire tout en itérant dessus dans différentes versions de Python – Python 2 et Python 3.

Vous avez également appris à supprimer une clé en fonction d'une clé ou de la valeur d'une clé.

Si vous avez aimé cet article, n'hésitez pas à le partager.

Vous pouvez consulter mes autres [tutoriels Python ici](https://www.stackvidhya.com).