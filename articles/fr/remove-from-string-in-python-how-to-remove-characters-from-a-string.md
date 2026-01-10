---
title: Supprimer d'une Chaîne en Python – Comment Supprimer des Caractères d'une Chaîne
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-20T20:20:23.000Z'
originalURL: https://freecodecamp.org/news/remove-from-string-in-python-how-to-remove-characters-from-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/remove_char.png
tags:
- name: Python
  slug: python
seo_title: Supprimer d'une Chaîne en Python – Comment Supprimer des Caractères d'une
  Chaîne
seo_desc: 'In Python, there are times when you might want to remove unnecessary characters
  from a string. Python provides two built-in methods you can use for that purpose
  – replace() and translate().

  So, in this article, you will learn how to remove a characte...'
---

En Python, il arrive que vous souhaitiez supprimer des caractères inutiles d'une chaîne. Python fournit deux méthodes intégrées que vous pouvez utiliser à cet effet – `replace()` et `translate()`.

Ainsi, dans cet article, vous apprendrez comment supprimer un caractère d'une chaîne avec ces deux méthodes et même remplacer les caractères par de nouveaux.

En plus de ces deux méthodes, je vais également vous montrer comment utiliser une boucle for et le découpage de chaîne pour supprimer des caractères d'une chaîne.


## Ce que nous allons couvrir
- [Comment Supprimer un Caractère d'une Chaîne avec la Méthode `replace()`](#heading-comment-supprimer-un-caractere-dune-chaine-avec-la-methode-replace)
  - [Comment Supprimer Plusieurs Caractères d'une Chaîne avec la Méthode `replace()`](#heading-comment-supprimer-plusieurs-caracteres-dune-chaine-avec-la-methode-replace)
- [Comment Supprimer un Caractère d'une Chaîne avec la Méthode `translate()`](#heading-comment-supprimer-un-caractere-dune-chaine-avec-la-methode-translate)
- [Comment Supprimer un Caractère d'une Chaîne avec le Découpage de Chaîne](#heading-comment-supprimer-un-caractere-dune-chaine-avec-le-decoupage-de-chaine)
- [Conclusion](#heading-conclusion)


## Comment Supprimer un Caractère d'une Chaîne avec la Méthode `replace()`
La méthode `replace()` fait ce que son nom implique. Elle remplace un certain caractère dans une chaîne par un autre caractère spécifié.

Ainsi, si vous souhaitez supprimer un caractère d'une chaîne avec elle, vous pouvez passer une chaîne vide comme nouvelle valeur.

La méthode `replace()` prend jusqu'à 3 paramètres :

```py
str.replace(old_char, new_char, count)
```

* le vieux caractère est le caractère que vous souhaitez remplacer
* le nouveau caractère est le remplacement pour le vieux caractère
* le `count` est un paramètre optionnel pour spécifier le nombre d'occurrences de l'ancienne valeur que vous souhaitez remplacer

Pour supprimer le caractère, vous spécifiez une chaîne vide pour le nouveau caractère.

Voici comment la méthode `replace()` fonctionne en code :

```py
str_with_num = "freeCodeCamp2"
str_without_num = str_with_num.replace("2", "")

print("Chaîne originale :", str_with_num) # Chaîne originale : freeCodeCamp2
print("La chaîne après l'avoir passée à replace :", str_without_num) # La chaîne après l'avoir passée à replace : freeCodeCamp
```

Vous pouvez voir que j'ai spécifié une chaîne vide comme nouvelle valeur afin de supprimer ce `2` à la fin de la chaîne `freeCodeCamp2`.

Vous pouvez également supprimer plusieurs valeurs d'une chaîne avec la méthode `replace()`. Dans l'exemple ci-dessous, j'ai supprimé "don't" de la chaîne parce que j'aime Python :

```py
wrong_str = "I don'tlove Python"
right_str = wrong_str.replace("don't", "")

print("Chaîne originale :", wrong_str) # Chaîne originale : I don'tlove Python
print("La chaîne après l'avoir passée à replace :", right_str) # La chaîne après l'avoir passée à replace : I love Python
```

De plus, la valeur de remplacement n'a pas besoin d'être une chaîne vide. Je dis que le but principal de la méthode `replace()` est de remplacer un caractère.

Dans l'exemple ci-dessous, j'ai supprimé `s` de la chaîne `freeCodeCampes` et l'ai remplacé par `r` parce que je suis un camper :

```py
wrong_str = "freeCodeCampes"
right_str = wrong_str.replace("s", "r")

print("Chaîne originale :", wrong_str) # Chaîne originale : freeCodeCampes
print("La chaîne après l'avoir passée à replace :", right_str) # La chaîne après l'avoir passée à replace : freeCodeCamper
```

### Comment Supprimer Plusieurs Caractères d'une Chaîne avec la Méthode `replace()`

Vous pouvez enchaîner deux méthodes de remplacement ou plus pour supprimer plusieurs caractères d'une chaîne :

```py
str_with_symbols = "We! love JavaScript, &Python, and Java.?"
str_without_symbols = str_with_symbols.replace("!", "").replace("&", "").replace("?", "")

print("Chaîne originale :", str_with_symbols) # Chaîne originale : We! love JavaScript, &Python, and Java.?
print("La chaîne après l'avoir passée à replace :", str_without_symbols) # La chaîne après l'avoir passée à replace : We love JavaScript, Python, and Java.
```

Vous pouvez également utiliser une boucle for pour supprimer plusieurs caractères d'une chaîne en passant la méthode de remplacement dans la boucle :

```py
str = "freeCodeCamp! is the best, ?easiest, & coolest place to learn how to code?"
replacements = [("!", ""), ("?", ""), ("&", "and")]

for i, j in replacements:
    if i in str:
        str = str.replace(i, j)
print(str)  # freeCodeCamp is the best, easiest, and coolest place to learn how to code
```

**Voici ce que j'ai fait dans cette boucle** :
- J'ai mis la chaîne originale dans une variable nommée `str`
- J'ai également mis les caractères que je veux remplacer et leurs remplacements dans une liste de tuples que j'appelle `replacements`
- `i` représente les premières valeurs individuelles dans ces tuples et `j` représente chaque deuxième valeur dans les tuples. Par exemple, dans le dernier tuple, "and" remplacerait "&"
- J'ai parcouru les remplacements avec une variable `j`, passé `i` dans la méthode `replace()` comme l'ancien caractère, et `j` comme le caractère de remplacement


## Comment Supprimer un Caractère d'une Chaîne avec la Méthode `translate()`

La méthode `translate()` est un peu plus compliquée lorsque vous la comparez à la méthode `replace()`. Il y a beaucoup de mises en garde impliquées et vous devez la combiner avec `ord()` ou la méthode `maketrans()` pour la faire fonctionner.

Vous devez utiliser `ord()` ou `maketrans()` parce que la méthode `translate()` attend une table de traduction ou le caractère unicode de cette valeur à supprimer.

`ord()` vous donnera la valeur Unicode et vous pouvez utiliser `maketrans()` pour créer une table de traduction – une paire clé:valeur dans un dictionnaire.

La méthode `translate()` est efficace lorsque vous souhaitez supprimer de nombreux caractères d'une chaîne ou d'une entrée utilisateur. Tout ce que vous avez à faire est de créer une table de traduction contenant les caractères et ce que vous voulez les remplacer.

Vous pouvez également être plus sélectif avec les caractères que vous souhaitez supprimer. C'est parce que si le caractère et son remplacement ne sont pas dans la table de traduction, ce caractère ne sera pas supprimé.

Voici comment la méthode `translate()` fonctionne avec la méthode `ord()` :

```py
str_with_num = "freeCodeCamp2"
str_without_num = str_with_num.translate({ord("2"): None})

print("Chaîne originale :", str_with_num) ## Chaîne originale : freeCodeCamp2
print("La chaîne après l'avoir passée à translate et ord() :", str_without_num)  # La chaîne après l'avoir passée à translate et ord() : freeCodeCamp
```

Et voici comment cela fonctionne avec la méthode `maketrans()` :

```py
my_str = "Gython is easy to learn"
my_table = my_str.maketrans("G", "P")
replaced_str = my_str.translate(my_table)

print(replaced_str) # Python is easy to learn
```

```py
my_str = "Golang"
my_table = my_str.maketrans("Golang", "Python")
replaced_str = my_str.translate(my_table)

print(replaced_str) # Python
```


## Comment Supprimer un Caractère d'une Chaîne avec le Découpage de Chaîne
Vous pouvez utiliser le découpage de chaîne pour extraire une partie d'une chaîne que vous voulez ou supprimer une partie de la chaîne que vous ne voulez pas.

Dans le code ci-dessous, je précise que je veux tout après le premier caractère :

```py
str = "ffreeCodeCamp"
new_str = str[1:]
print(new_str) # freeCodeCamp
```

Et dans l'exemple ci-dessous, j'ai pu extraire certaines parties de la chaîne

`StartMiddleEnd` :
```py
my_str = "StartMiddleEnd"

# Tout avant le 5ème caractère
the_start = my_str[:5]

# Tout entre le 5ème et le 11ème caractère
the_mid = my_str[5:11] 

# Tout après le 11ème caractère
the_end = my_str[11:]

print("Le début :", the_start)
print("Le milieu :", the_mid)
print("La fin :", the_end)

"""
Sortie :
Le début : Start
Le milieu : Middle
La fin : End
"""
```


## Conclusion
Cet article vous a montré comment supprimer des caractères uniques et multiples d'une chaîne avec les méthodes intégrées `replace()` et `translate()`.

Nous avons également vu comment vous pouvez supprimer un caractère d'une chaîne avec le découpage de chaîne. Cela fonctionne parce que chaque caractère dans une chaîne a un index. Ainsi, vous pouvez utiliser cet indexage avec le découpage pour extraire ou supprimer certains caractères d'une chaîne.

En Python, il est également possible de supprimer un ou plusieurs caractères d'une chaîne avec des expressions régulières. Vous pouvez en apprendre davantage à ce sujet dans cet [article sur comment supprimer des caractères d'une chaîne en Python](https://www.freecodecamp.org/news/how-to-remove-a-specific-character-from-a-string-in-python/#regular-expressions).