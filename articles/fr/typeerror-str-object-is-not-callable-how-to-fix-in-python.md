---
title: 'Typeerror: str object is not callable – Comment le corriger en Python'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-08T14:21:57.000Z'
originalURL: https://freecodecamp.org/news/typeerror-str-object-is-not-callable-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/brett-jordan-XWar9MbNGUY-unsplash--1-.jpg
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: 'Typeerror: str object is not callable – Comment le corriger en Python'
seo_desc: "Every programming language has certain keywords with specific, prebuilt\
  \ functionalities and meanings. \nNaming your variables or functions after these\
  \ keywords is most likely going to raise an error. We'll discuss one of these cases\
  \ in this article — ..."
---

Chaque langage de programmation possède certains mots-clés avec des fonctionnalités et des significations spécifiques et préconstruites.

Nommer vos variables ou fonctions d'après ces mots-clés soulèvera probablement une erreur. Nous allons discuter de l'un de ces cas dans cet article — l'erreur `TypeError: 'str' object is not callable` en Python.

L'erreur `TypeError: 'str' object is not callable` se produit principalement lorsque :

* Vous passez une variable nommée `str` comme paramètre à la fonction `str()`.
* Lorsque vous appelez une chaîne de caractères comme une fonction.

Dans les sections qui suivent, vous verrez des exemples de code qui provoquent l'erreur `TypeError: 'str' object is not callable`, et comment les corriger.

## Exemple #1 – Que se passe-t-il si vous utilisez `str` comme nom de variable en Python ?

Dans cette section, vous verrez ce qui se passe lorsque vous utilisez une variable nommée `str` comme paramètre de la fonction `str()`.

La fonction `str()` est utilisée pour convertir certaines valeurs en chaîne de caractères. `str(10)` convertit l'entier `10` en chaîne de caractères.

Voici le premier exemple de code :

```python
str = "Hello World"

print(str(str))
# TypeError: 'str' object is not callable
```

Dans le code ci-dessus, nous avons créé une variable `str` avec une valeur de "Hello World". Nous avons passé la variable comme paramètre à la fonction `str()`.

Le résultat a été l'erreur `TypeError: 'str' object is not callable`. Cela se produit parce que nous utilisons un nom de variable que le compilateur reconnaît déjà comme autre chose.

Pour corriger cela, vous pouvez renommer la variable en quelque chose qui n'est pas un mot-clé prédéfini en Python.

Voici une solution rapide au problème :

```python
greetings = "Hello World"

print(str(greetings))
# Hello World
```

Maintenant, le code fonctionne parfaitement.

## Exemple #2 – Que se passe-t-il si vous appelez une chaîne de caractères comme une fonction en Python ?

Appeler une chaîne de caractères comme si c'était une fonction en Python provoquera l'erreur `TypeError: 'str' object is not callable`.

Voici un exemple :

```python
greetings = "Hello World"

print(greetings())
# TypeError: 'str' object is not callable
```

Dans l'exemple ci-dessus, nous avons créé une variable appelée `greetings`.

Lors de son impression dans la console, nous avons utilisé des parenthèses après le nom de la variable — une syntaxe utilisée lors de l'invocation d'une fonction : `greetings()`.

Cela a entraîné le compilateur à lever l'erreur `TypeError: 'str' object is not callable`.

Vous pouvez facilement corriger cela en supprimant les parenthèses.

Cela s'applique à tous les autres types de données qui ne sont pas des fonctions. Ajouter des parenthèses à ceux-ci provoquera la même erreur.

Ainsi, notre code devrait fonctionner comme ceci :

```python
greetings = "Hello World"

print(greetings)
# Hello World
```

## Résumé

Dans cet article, nous avons parlé de l'erreur `TypeError: 'str' object is not callable` en Python.

Nous avons discuté des raisons pour lesquelles cette erreur peut se produire et comment la corriger.

Pour éviter cette erreur dans votre code, vous devriez :

* Éviter de nommer vos variables d'après les mots-clés intégrés de Python.
* Ne jamais appeler vos variables comme des fonctions en ajoutant des parenthèses.

Bon codage !