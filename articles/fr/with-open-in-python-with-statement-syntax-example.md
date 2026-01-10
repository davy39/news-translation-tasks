---
title: Avec Open en Python – Exemple de Syntaxe de l'Instruction With
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-12T17:20:54.000Z'
originalURL: https://freecodecamp.org/news/with-open-in-python-with-statement-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/withOpen.png
tags:
- name: Python
  slug: python
seo_title: Avec Open en Python – Exemple de Syntaxe de l'Instruction With
seo_desc: 'The Python programming language has various functions and statements for
  working with a file. The with statement and open() function are two of those statements
  and functions.

  In this article, you will learn how to use both the with statement and ope...'
---

Le langage de programmation Python dispose de diverses fonctions et instructions pour travailler avec un fichier. L'instruction `with` et la fonction `open()` sont deux de ces instructions et fonctions.

Dans cet article, vous apprendrez à utiliser à la fois l'instruction `with` et la fonction `open()` pour travailler avec des fichiers en Python.


## Que Fait `Open()` en Python ?

Pour travailler avec des fichiers en Python, vous devez d'abord ouvrir le fichier. Ainsi, la fonction `open()` fait ce que le nom implique – elle ouvre un fichier pour vous afin que vous puissiez travailler avec le fichier.

Pour utiliser la fonction open, vous déclarez d'abord une variable pour celle-ci. La fonction `open()` prend jusqu'à 3 paramètres – le nom du fichier, le mode et l'encodage. Vous pouvez ensuite spécifier ce que vous voulez faire avec le fichier dans une fonction print.

```py
my_file = open("hello.txt", "r")
print(my_file.read())

# Sortie :
# Hello world
# J'espère que vous allez bien aujourd'hui
# Ceci est un fichier texte
```

Ce n'est pas tout. La fonction `open()` ne ferme pas le fichier, vous devez donc également fermer le fichier avec la méthode `close()`.

Ainsi, une manière appropriée d'utiliser la fonction open ressemble à ceci :

```py
my_file = open("hello.txt", "r")
print(my_file.read())
my_file.close()

# Sortie :
# Hello world
# J'espère que vous allez bien aujourd'hui
# Ceci est un fichier texte

```

Le mode lecture est le mode de fichier par défaut en Python, donc si vous ne spécifiez pas le mode, le code ci-dessus fonctionne toujours bien :

```py
my_file = open("hello.txt")
print(my_file.read())
my_file.close()

# Sortie :
# Hello world
# J'espère que vous allez bien aujourd'hui
# Ceci est un fichier texte
```


## Comment Fonctionne l'Instruction `With` en Python ?

L'instruction `with` fonctionne avec la fonction `open()` pour ouvrir un fichier.

Ainsi, vous pouvez réécrire le code que nous avons utilisé dans l'exemple de la fonction `open()` comme ceci :

```py
with open("hello.txt") as my_file:
    print(my_file.read())

# Sortie :
# Hello world
# J'espère que vous allez bien aujourd'hui
# Ceci est un fichier texte
```

Contrairement à `open()` où vous devez fermer le fichier avec la méthode `close()`, l'instruction `with` ferme le fichier pour vous sans que vous ayez à le lui dire.

C'est parce que l'instruction `with` appelle 2 méthodes intégrées en arrière-plan – `__enter()__` et `__exit()__`.

La méthode `__exit()__` ferme le fichier lorsque l'opération que vous spécifiez est terminée.

Avec la méthode `write()`, vous écrivez également dans le fichier comme je l'ai fait ci-dessous :

```py
with open("hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
    my_file.write("J'espère que vous allez bien aujourd'hui \n")
    my_file.write("Ceci est un fichier texte \n")
    my_file.write("Passez un bon moment \n")

with open("hello.txt") as my_file:
    print(my_file.read())

# Sortie :
# Hello world
# J'espère que vous allez bien aujourd'hui
# Ceci est un fichier texte
# Passez un bon moment
```

**Vous pouvez également parcourir le fichier et imprimer le texte ligne par ligne :**
```py
with open("hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
    my_file.write("J'espère que vous allez bien aujourd'hui \n")
    my_file.write("Ceci est un fichier texte \n")
    my_file.write("Passez un bon moment \n")

with open("hello.txt") as my_file:
    for line in my_file:
        print(line)

# Sortie :
# Hello world

# J'espère que vous allez bien aujourd'hui

# Ceci est un fichier texte

# Passez un bon moment
```


## Conclusion

Vous vous demandez peut-être quelle méthode utiliser pour travailler avec des fichiers entre la combinaison de `with` et `open()` et la simple fonction `open()`.

Je vous conseille d'utiliser la combinaison de `with` et `open()` car l'instruction `with` ferme le fichier pour vous et vous avez moins de code à écrire.

Continuez à coder :)