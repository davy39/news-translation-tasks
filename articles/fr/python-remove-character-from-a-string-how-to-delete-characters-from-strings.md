---
title: Python Supprimer un Caractère d'une Chaîne – Comment Supprimer des Caractères
  des Chaînes
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-07T18:08:44.000Z'
originalURL: https://freecodecamp.org/news/python-remove-character-from-a-string-how-to-delete-characters-from-strings
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/fotis-fotopoulos-LJ9KY8pIH3E-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Supprimer un Caractère d'une Chaîne – Comment Supprimer des Caractères
  des Chaînes
seo_desc: "In Python you can use the replace() and translate() methods to specify\
  \ which characters you want to remove from a string and return a new modified string\
  \ result. \nIt is important to remember that the original string will not be altered\
  \ because string..."
---

En Python, vous pouvez utiliser les méthodes `replace()` et `translate()` pour spécifier quels caractères vous souhaitez supprimer d'une chaîne et retourner un nouveau résultat de chaîne modifié. 

Il est important de se rappeler que la chaîne originale ne sera pas modifiée car les chaînes sont immuables. 

Dans cet article, je vais vous montrer comment travailler avec les méthodes `replace()` et `translate()` à travers l'utilisation d'exemples de code. 

## Comment utiliser la méthode replace() de Python

Voici la syntaxe de base pour la méthode `replace()`.

```py
str.replace(old_str, new_str[, optional_max])
```

Le paramètre `old_str` représente la sous-chaîne que vous souhaitez remplacer.

Le paramètre `new_str` représente la nouvelle sous-chaîne que vous souhaitez utiliser.

Le paramètre `optional_max` représente le nombre maximum de fois où remplacer l'ancienne sous-chaîne par la nouvelle sous-chaîne. 

La valeur de retour pour la méthode `replace()` sera une copie de la chaîne originale avec l'ancienne sous-chaîne remplacée par la nouvelle sous-chaîne.

### Exemple de Python replace()

Examinons quelques exemples.

Dans cet exemple, nous avons une chaîne appelée `developer` avec mon nom assigné.

```py
developer = 'Jessica Wilkins'
```

Si nous voulions supprimer mon nom de famille, nous pouvons utiliser la méthode `replace()` comme ceci :

```py
developer.replace('Wilkins', '')
```

Cela indique à l'ordinateur de prendre l'ancienne sous-chaîne `Wilkins` et de la remplacer par une chaîne vide. 

Si nous affichons le résultat, voici ce que nous obtiendrions :

```py
print(developer.replace('Wilkins', ''))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-8.41.55-PM.png)

Il est important de se rappeler que la chaîne originale reste inchangée car les chaînes sont immuables. La méthode `replace()` retournera une nouvelle chaîne.

Dans cet exemple suivant, nous voulons utiliser le paramètre `optional_max` pour définir le nombre de fois où nous voulons supprimer la lettre `s` de mon nom.

```py
developer.replace('s', '', 2)
```

Cette ligne de code indique de supprimer la lettre `s` seulement deux fois de la chaîne `Jessica Wilkins`. 

Si nous devions afficher le résultat, voici à quoi cela ressemblerait :

```py
print(developer.replace('s', '', 2))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-8.55.22-PM.png)

## Comment utiliser la méthode translate() de Python

Une autre façon de supprimer des caractères d'une chaîne est d'utiliser la méthode `translate()`. Cette méthode retourne une nouvelle chaîne où chaque caractère de l'ancienne chaîne est mappé à un caractère de la table de traduction et traduit en une nouvelle chaîne.

Voici la syntaxe de base pour la méthode `translate()` de Python.

```py
str.translate(table)
```

### Exemple de Python translate()

Examinons quelques exemples pour mieux comprendre la méthode `translate()`.

Dans cet exemple, nous voulons supprimer toutes les occurrences de la lettre `i` de la chaîne `Jessica Wilkins`. 

Nous devons d'abord utiliser la fonction intégrée `ord()` de Python pour obtenir la valeur du point de code Unicode pour la lettre `i`. La fonction `ord()` retournera une valeur numérique. 

```py
ord('i')
```

Pour notre table, nous devons assigner la valeur `None` afin que l'ordinateur sache remplacer la lettre `i` par rien.

```py
{ord('i'): None}
```

Maintenant, nous utilisons notre table à l'intérieur de la méthode `translate()`.

```py
developer.translate({ord('i'): None})
```

Si nous devions afficher le résultat, voici à quoi cela ressemblerait :

```py
developer = 'Jessica Wilkins'

print(developer.translate({ord('i'): None}))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-10.24.52-PM.png)

Dans cet exemple suivant, nous voulons retourner une nouvelle chaîne avec les lettres `e`, `s` et `i` supprimées. Pour ce faire, nous pouvons utiliser un itérateur dans notre paramètre de table.

```py
{ord(letter): None for letter in 'esi'}
```

Cette ligne de code indique à l'ordinateur de trouver toutes les occurrences de `e`, `s` et `i` et de les remplacer par `None`. 

Si nous devions afficher le résultat, voici à quoi cela ressemblerait :

```py
developer = 'Jessica Wilkins'

print(developer.translate({ord(letter): None for letter in 'esi'}))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-10.37.10-PM.png)

## Conclusion

En Python, vous pouvez utiliser les méthodes `replace()` et `translate()` pour spécifier quels caractères vous souhaitez supprimer de la chaîne et retourner un nouveau résultat de chaîne modifié. 

Il est important de se rappeler que la chaîne originale ne sera pas modifiée car les chaînes sont immuables. 

Voici la syntaxe de base pour la méthode `replace()`.

```py
str.replace(old_str, new_str[, optional_max])
```

La valeur de retour pour la méthode `replace()` sera une copie de la chaîne originale avec l'ancienne sous-chaîne remplacée par la nouvelle sous-chaîne.

Une autre façon de supprimer des caractères d'une chaîne est d'utiliser la méthode `translate()`. Cette méthode retourne une nouvelle chaîne où chaque caractère de l'ancienne chaîne est mappé à un caractère de la table de traduction et traduit en une nouvelle chaîne.

Voici la syntaxe de base pour la méthode `translate()` de Python.

```py
str.translate(table)
```

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours Python.