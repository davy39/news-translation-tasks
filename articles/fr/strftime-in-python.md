---
title: strftime() Python – Tutoriel sur le format de date et d'heure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-15T16:55:14.000Z'
originalURL: https://freecodecamp.org/news/strftime-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/python-datetime-format-tutorial.png
tags:
- name: Python
  slug: python
seo_title: strftime() Python – Tutoriel sur le format de date et d'heure
seo_desc: 'By Dillion Megida

  In Python, you can format date objects and present them in readable form using the
  strftime function. In this article, I''ll show you how.

  What is strftime() in Python?

  strftime() is a Python date method you can use to convert dates ...'
---

Par Dillion Megida

En Python, vous pouvez formater des objets de date et les présenter sous une forme lisible en utilisant la fonction `strftime`. Dans cet article, je vais vous montrer comment faire.

## Qu'est-ce que `strftime()` en Python ?

`strftime()` est une méthode de date Python que vous pouvez utiliser pour convertir des dates en chaînes de caractères. Elle ne se contente pas de convertir en chaînes, mais permet également de formater vos dates de manière lisible.

Si vous êtes familier avec JavaScript, pensez à cette méthode comme à la fonction `format` de la bibliothèque `date-fns` qui utilise différents caractères pour formater les dates.

## Comment utiliser `strftime()` en Python

La syntaxe de la méthode `strftime` est :

```python
date.strftime(format)
```

L'argument `format` peut être une combinaison de différents caractères pour le résultat final de la chaîne. Voici quelques exemples :

```python
from datetime import datetime

current_date = datetime.now()
print(current_date)
# 2022-07-14 23:37:38.578835

string_date = current_date.strftime("%Y")
print(string_date)
# 2022
```

`datetime.now` retourne la date actuelle. En utilisant la méthode `strftime` et le caractère "%Y", la date est convertie en une chaîne affichant l'année.

Voici un autre exemple :

```python
from datetime import datetime

date = datetime.fromisoformat("2022-07-15 00:15:14.643725")

string_date = current_date.strftime("%Y-%b")
print(string_date)
# 2022-Jul
```

En utilisant `fromisoformat` de l'objet `datetime`, vous pouvez passer une chaîne de date complète pour obtenir un objet de date pour cette chaîne.

`%Y` est utilisé pour l'année complète (2022) et `%b` pour la version courte du mois (Jul).

`strftime` conserve le tiret "-" mais remplace les autres caractères par la représentation correcte de la date.

Voici un autre exemple pour formater les heures dans les dates :

```python
from datetime import datetime

date = datetime.now()

string_time = date.strftime("%X")
print(string_time)
# 00:54:20
```

Le caractère `%X` formate une chaîne de date en affichant la représentation de l'heure en `heures:minutes:secondes`.

## Conclusion

Dans ce tutoriel, nous avons vu comment formater des chaînes de date en utilisant différents caractères passés en argument à la méthode de date `strftime`.

Nous avons utilisé :

* `%Y` pour une année complète
* `%b` pour un nom de mois abrégé
* `%X` pour la représentation de l'heure

Il existe de nombreux autres caractères pour les noms de mois complets, les noms d'année abrégés et les heures. Consultez le [cheat sheet strftime Python](https://strftime.org/) pour en savoir plus sur les caractères que vous pouvez utiliser pour représenter les dates.