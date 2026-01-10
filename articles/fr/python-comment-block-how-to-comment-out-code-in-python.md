---
title: Bloc de commentaires Python – Comment commenter du code en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-11T20:11:40.000Z'
originalURL: https://freecodecamp.org/news/python-comment-block-how-to-comment-out-code-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/comments-python.jpg
tags:
- name: Python
  slug: python
seo_title: Bloc de commentaires Python – Comment commenter du code en Python
seo_desc: "In this article, we'll talk about comments in Python, why they are important,\
  \ and how to use them effectively in your code. \nWhen to Use Comments\nIn this\
  \ section, we'll talk about some of the general use cases for comments. These aren't\
  \ only applicab..."
---

Dans cet article, nous allons parler des commentaires en Python, pourquoi ils sont importants et comment les utiliser efficacement dans votre code. 

## Quand utiliser les commentaires

Dans cette section, nous aborderons certains cas d'utilisation généraux pour les commentaires. Ceux-ci ne s'appliquent pas seulement à Python, mais à la plupart des langages de programmation. 

Voici quelques-unes des principales raisons de commenter votre code :

* **Empêcher l'exécution du code** : Dans certains cas, vous devrez empêcher une partie de votre code de s'exécuter. Cela peut être dû au fait que vous n'avez pas l'utilité de ce code pour le moment, mais que vous souhaitez tout de même l'ajouter pour une fonctionnalité future.
* **Lisibilité** : C'est très important – pas seulement pour nous-mêmes, mais aussi pour les autres développeurs. Nous pouvons utiliser des commentaires pour expliquer ce que fait chaque bloc de code. C'est utile lorsque d'autres développeurs lisent notre code, car cela permet de comprendre facilement ce que fait chaque partie du code.

## Comment commenter du code en Python

La syntaxe des commentaires diffère selon chaque langage de programmation. Dans cette section, nous verrons comment ajouter des commentaires en utilisant Python.

Les commentaires en Python commencent par le symbole `#`. Voici un exemple :

```python
# Le code ci-dessous affiche Hello World ! dans la console
print("Hello World!")
```

Dans le code ci-dessus, j'ai utilisé un commentaire pour expliquer ce que fait le code. Lorsque le code est exécuté, l'interprète ignorera le commentaire et exécutera la fonction `print()`.

Nous pouvons également commenter du code existant. Par exemple :

```python
# print("Hello World!")
print("Happy coding!")

```

Lorsque nous exécutons le code, seule la deuxième ligne sera interprétée.

Vous n'êtes pas toujours obligé de placer les commentaires au-dessus de la ligne de code à laquelle ils font référence. Vous pouvez également les placer sur la même ligne. Par exemple : 

```python
print("Hello world") # Affiche Hello World
```

## Comment écrire des commentaires multi-lignes en Python

Dans cette section, nous verrons comment écrire des commentaires qui s'étendent sur plusieurs lignes.

Contrairement à la plupart des autres langages de programmation, Python n'a pas de syntaxe intégrée pour créer des commentaires multi-lignes.

Heureusement, il existe deux façons de contourner cela. Voici la première :

```python
# Quand ce code s'exécute,
# vous verrez Hello World ! 
# dans la console. 
print("Hello world")
```

Ci-dessus, nous avons placé le symbole `#` sur chaque ligne pour continuer à écrire notre commentaire.

Dans l'exemple suivant, nous allons utiliser des chaînes de caractères multi-lignes (commençant et se terminant par trois guillemets) pour imbriquer notre commentaire. 

Lorsque vous utilisez des chaînes multi-lignes en Python sans assigner la chaîne à une variable, cette partie du code sera ignorée. 

Voici un exemple :

```python
"""
Quand ce code s'exécute,
vous verrez Hello World ! 
dans la console.
"""
print("Hello World!")
```

## Conclusion

Dans cet article, nous avons appris pourquoi il est important de commenter notre code et comment utiliser les commentaires. Nous avons également vu comment créer des commentaires multi-lignes.

Bon code !