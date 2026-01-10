---
title: Python Split String – Comment diviser une chaîne en une liste ou un tableau
  en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-04T20:24:05.000Z'
originalURL: https://freecodecamp.org/news/python-split-string-how-to-split-a-string-into-a-list-or-array-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Split-String
seo_title: Python Split String – Comment diviser une chaîne en une liste ou un tableau
  en Python
---

How-to-Split-a-String-into-a-List-or-Array-in-Python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nDans cet article, nous allons parcourir un guide complet\
  \ sur la façon de diviser une chaîne en Python et de la convertir en une liste ou un tableau.\
  \ \nNous commencerons par présenter le type de données chaîne en Python et expliquer ses\
  \ propriétés. Ensuite, nous discuterons des différentes façons de diviser une chaîne en utilisant des méthodes Python intégrées telles que `split()`, `splitlines()`, et `partition()`."
---

Par Shittu Olumide

Dans cet article, nous allons parcourir un guide complet sur la façon de diviser une chaîne en Python et de la convertir en une liste ou un tableau. 

Nous commencerons par présenter le type de données chaîne en Python et expliquer ses propriétés. Ensuite, nous discuterons des différentes façons de diviser une chaîne en utilisant des méthodes Python intégrées telles que `split()`, `splitlines()`, et `partition()`.

Dans l'ensemble, cet article devrait être une ressource utile pour toute personne cherchant à diviser une chaîne en une liste en Python, des débutants aux programmeurs expérimentés.

## Qu'est-ce qu'une chaîne en Python ?

Une chaîne est un groupe de caractères en Python qui sont encadrés par des guillemets simples (`' '`) ou des guillemets doubles (`" "`). Ce type de données intégré de Python est fréquemment utilisé pour représenter des données textuelles. 

Puisque les chaînes sont immuables, elles ne peuvent pas être modifiées une fois qu'elles ont été créées. Toute action qui semble modifier une chaîne produit en réalité une nouvelle chaîne.  
  
La concaténation, le découpage et le formatage ne sont que quelques-unes des nombreuses opérations que vous pouvez effectuer sur les chaînes en Python. Vous pouvez également utiliser des chaînes avec un certain nombre de modules et de fonctions intégrés, y compris `re`, `str()`, et `len()`. 

Il existe également une large gamme d'opérations sur les chaînes, y compris `split()`, `replace()`, et `strip()`, qui sont disponibles en Python. Vous pouvez les utiliser pour manipuler les chaînes de différentes manières.

```py
myString = "Hello world"

```

Apprenons maintenant comment diviser une chaîne en une liste en Python.

## Comment diviser une chaîne en une liste en utilisant la méthode `split()`

La méthode `split()` est la manière la plus courante de diviser une chaîne en une liste en Python. Cette méthode divise une chaîne en sous-chaînes en fonction d'un délimiteur et retourne une liste de ces sous-chaînes.

```py
myString = "Hello world"
myList = myString.split()

print(myList)

```

Sortie :

```bash
['Hello', 'world']

```

Dans cet exemple, nous divisons la chaîne `"Hello world"` en une liste de deux éléments, `"Hello"` et `"world"`, en utilisant la méthode `split()`.

## Comment diviser une chaîne en une liste en utilisant la méthode `splitlines()`

La méthode `splitlines()` est utilisée pour diviser une chaîne en une liste de lignes, en fonction du caractère de nouvelle ligne `(\n)`.

```py
myString = "hello\nworld"
myList = myString.splitlines()

print(myList)

```

Sortie :

```bash
['hello', 'world']

```

Dans cet exemple, nous divisons la chaîne `"hello\nworld"` en une liste de deux éléments, `"hello"` et `"world"`, en utilisant la méthode `splitlines()`.

## Comment diviser une chaîne en une liste en utilisant des expressions régulières avec le module `re`

Le module `re` en Python fournit un moyen puissant de diviser des chaînes en fonction d'expressions régulières.

```py
import re

myString = "hello world"
myList = re.split('\s', myString)

print(myList)

```

Sortie :

```bash
['hello', 'world']

```

Dans cet exemple, nous divisons la chaîne `"hello world"` en une liste de deux éléments, `"hello"` et `"world"`, en utilisant une expression régulière qui correspond à tout caractère d'espace blanc `(\s)`.

## Comment diviser une chaîne en une liste en utilisant la méthode `partition()`

La méthode `partition()` divise une chaîne en trois parties en fonction d'un séparateur et retourne un tuple contenant ces parties. Le séparateur lui-même est également inclus dans le tuple.

```py
myString = "hello:world"
myList = myString.partition(':')

print(myList)

```

Sortie :

```bash
('hello', ':', 'world')

```

Dans cet exemple, nous divisons la chaîne `"hello:world"` en un tuple de trois éléments, `"hello"`, `":"`, et `"world"`, en utilisant la méthode `partition()`.

Note : La méthode la plus courante pour diviser une chaîne en une liste ou un tableau en Python est d'utiliser la méthode `split()`. Cette méthode est disponible pour tout objet chaîne en Python et divise la chaîne en une liste de sous-chaînes en fonction d'un délimiteur spécifié.

## Quand utiliser chaque méthode

Voici un aperçu de ces méthodes et quand utiliser chacune d'entre elles pour une référence rapide :

1. `split()` : Il s'agit de la méthode la plus courante pour diviser un texte en une liste. Vous pouvez utiliser cette méthode lorsque vous souhaitez diviser le texte en mots ou en sous-chaînes en fonction d'un délimiteur spécifique, tel qu'un espace, une virgule ou une tabulation.
2. `partition()` : Cette méthode divise un texte en trois parties en fonction de la première occurrence d'un délimiteur. Vous pouvez utiliser cette méthode lorsque vous souhaitez diviser le texte en deux parties et conserver le délimiteur. Par exemple, vous pourriez utiliser `partition()` pour diviser une URL en ses composants de protocole, de domaine et de chemin. La méthode `partition()` retourne un tuple de trois chaînes.
3. `splitlines()` : Cette méthode divise un texte en une liste de chaînes en fonction des caractères de nouvelle ligne (`\n`). Vous pouvez utiliser cette méthode lorsque vous souhaitez diviser un texte en lignes de texte. Par exemple, vous pourriez utiliser `splitlines()` pour diviser une chaîne multiline en lignes individuelles.
4. Expressions régulières : Il s'agit d'une méthode plus puissante pour diviser un texte en une liste, car elle vous permet de diviser le texte en fonction de motifs plus complexes. Par exemple, vous pourriez utiliser des expressions régulières pour diviser un texte en phrases, en fonction de la présence de marques de ponctuation. Le module `re` en Python fournit une gamme de fonctions pour travailler avec des expressions régulières.

## Conclusion

Ce sont quelques-unes des méthodes les plus courantes pour diviser une chaîne en une liste ou un tableau en Python. Selon votre cas d'utilisation spécifique, une méthode peut être plus appropriée que les autres.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !