---
title: Comment supprimer une clé d'un dictionnaire Python – Supprimer une clé d'un
  dictionnaire
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-18T20:32:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-key-from-a-python-dictionary-delete-key-from-dict
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/remove-key-val.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Comment supprimer une clé d'un dictionnaire Python – Supprimer une clé
  d'un dictionnaire
seo_desc: "A dictionary is a very powerful data collection in Python. Dictionaries\
  \ help make database operations faster. \nYou can append items to an existing dictionary\
  \ and remove them as well.\nIn this blog post, we will learn how to delete \"keys\"\
  \ using two met..."
---

Un dictionnaire est une collection de données très puissante en Python. Les dictionnaires aident à rendre les opérations de base de données plus rapides. 

Vous pouvez ajouter des éléments à un dictionnaire existant et les supprimer également.

Dans cet article de blog, nous allons apprendre comment supprimer des "clés" en utilisant deux méthodes :

1. Suppression des paires `clé:valeur` en utilisant `del`.
2. Suppression des paires `clé:valeur` en utilisant `pop()`.

## Qu'est-ce qu'un dictionnaire en Python ?

Un dictionnaire est une collection non ordonnée d'éléments. Les éléments sont définis à l'aide de paires clé-valeur. Les clés mappent à leur élément correspondant dans la liste. Chaque fois qu'un élément doit être interrogé, nous pouvons le faire en utilisant sa clé.

Par exemple, `"city":"Seoul"` est une paire clé-valeur où "city" est la clé, et "Seoul" est sa valeur.

Voici la syntaxe pour déclarer un dictionnaire en Python :

```python
my_dict = {
    <clé>: <valeur>,
    <clé>: <valeur>,
      .
      .
      .
    <clé>: <valeur>
}
```

Dans nos exemples, nous utiliserons le dictionnaire suivant :

```python
>>> # Déclarer un dictionnaire
>>> my_dict = {"Fruit":"Poire", "Vegetable":"Carotte", "Pet":"Chat", "Book":"Moby Dick", "Crystal":"Améthyste"}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-61.png)

## Comment supprimer des clés d'un dictionnaire en Python

### Supprimer une clé en utilisant `del`.

Vous pouvez supprimer une clé en utilisant le mot-clé `del`. Voici la syntaxe pour cela :

```python
del dict["Clé"]
```

Supprimons une clé dans notre dictionnaire `my_dict`. Nous allons supprimer la clé : "Fruit".

```python
# Supprimer une clé - Fruit
del my_dict["Fruit"]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-62.png)

Après avoir supprimé cette clé, nous pouvons voir que la clé `Fruit` n'est plus présente dans le dictionnaire.

Mais, que se passe-t-il si vous essayez de supprimer une clé qui n'existe pas ?

Essayons de supprimer à nouveau la clé `Fruit`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-63.png)
_Supprimer une clé qui n'existe pas._

Nous avons reçu une erreur de traceback. Cela est valide car la clé n'existe pas. 

Un inconvénient de `del` est qu'il lance une exception lorsque la `clé` n'est pas trouvée. L'exception doit être gérée explicitement dans un bloc try-catch. 

Cependant, nous pouvons gérer cette exception en utilisant la deuxième méthode.

### Supprimer une clé en utilisant `pop()`

La deuxième façon de supprimer une clé est d'utiliser la méthode `pop()`. Voici sa syntaxe :

```python
data.pop("Clé", None)
```

Où,

* `clé` est la clé à supprimer.
* `None` spécifie que si la clé est trouvée, alors supprimez-la. Sinon, ne faites rien.
* Nous pouvons également spécifier un message personnalisé à la place de 'None' pour les cas où la clé n'est pas trouvée.

Maintenant, si nous essayons de supprimer `Fruit` à nouveau, aucune exception n'est lancée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-65.png)

Maintenant, essayons de supprimer une clé existante avec `pop()`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-64.png)

Ici, la clé :Book est supprimée avec succès.

Un avantage de `pop()` sur `del` est qu'il nous permet de gérer les exceptions. Il fournit un mécanisme pour retourner un message personnalisé lorsque l'exception se produit.

### Comment définir un message personnalisé :

Essayons de supprimer 'Book' à nouveau. Nous nous attendons à une erreur, alors définissons un message de retour.

Ici, `La clé n'existe pas` est le message de retour au cas où la clé n'existe pas.

```python
my_dict.pop("Book", 'La clé n'existe pas')
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-68.png)
_Comme "Book" avait déjà été supprimé, nous obtenons le message d'erreur_

Un autre avantage est qu'il retourne également la valeur de la clé en plus d'effectuer une opération de suppression. Si vous devez connaître la valeur d'une clé supprimée, alors `pop()` est l'option appropriée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-67.png)

## Conclusion

Dans ce tutoriel, nous avons appris comment créer un dictionnaire en Python. Nous nous sommes également concentrés sur la façon de supprimer des paires clé:valeur dans un dictionnaire. 

J'espère que vous avez trouvé ce tutoriel utile.

Connectons-nous sur [Twitter](https://twitter.com/hira_zaira) !

Lisez mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Discutons sur [Discord](https://discordapp.com/users/Zaira_H#2603).