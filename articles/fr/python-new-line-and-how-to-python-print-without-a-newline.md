---
title: Nouvelle ligne Python et comment imprimer sans sauter de ligne
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-06-20T23:20:47.000Z'
originalURL: https://freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/New-Line.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: Nouvelle ligne Python et comment imprimer sans sauter de ligne
seo_desc: 'Welcome! The new line character in Python is used to mark the end of a
  line and the beginning of a new line. Knowing how to use it is essential if you
  want to print output to the console and work with files.

  In this article, you will learn:


  How to i...'
---

**Bienvenue !** Le caractère de nouvelle ligne en Python est utilisé pour marquer la fin d'une ligne et le début d'une nouvelle ligne. Savoir comment l'utiliser est essentiel si vous souhaitez imprimer du texte dans la console et travailler avec des fichiers.

**Dans cet article, vous apprendrez :**

* Comment identifier le caractère de nouvelle ligne en Python.
* Comment le caractère de nouvelle ligne peut être utilisé dans les chaînes de caractères et les instructions d'impression.
* Comment écrire des instructions d'impression qui n'ajoutent pas de caractère de nouvelle ligne à la fin de la chaîne.

**Commençons ! ✨**

## 📹 Le caractère de nouvelle ligne

Le caractère de nouvelle ligne en Python est :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-142.png)

**Il est composé de deux caractères :**

* Une barre oblique inverse.
* La lettre `n`.

Si vous voyez ce caractère dans une chaîne, cela signifie que la ligne actuelle se termine à cet endroit et qu'une nouvelle ligne commence juste après :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-224.png)

Vous pouvez également utiliser ce caractère dans les **f-strings** :

```python
>>> print(f"Bonjour\nMonde !")
```

## 📸 Le caractère de nouvelle ligne dans les instructions d'impression

Par défaut, les instructions d'impression ajoutent un caractère de nouvelle ligne "en coulisses" à la fin de la chaîne.

Comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-145.png)

Cela se produit parce que, selon la [Documentation Python](https://docs.python.org/3/library/functions.html#print) :

La valeur par défaut du paramètre `end` de la fonction intégrée `print` est `\n`, donc un caractère de nouvelle ligne est ajouté à la chaîne.

**💡 Astuce :** Append signifie "ajouter à la fin".

Voici la définition de la fonction :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-146.png)

Remarquez que la valeur de `end` est `\n`, donc cela sera ajouté à la fin de la chaîne.

Si vous n'utilisez qu'une seule instruction d'impression, vous ne remarquerez pas cela car une seule ligne sera imprimée :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-147.png)

Mais si vous utilisez plusieurs instructions d'impression les unes après les autres dans un script Python :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-214.png)

Le résultat sera imprimé sur des lignes séparées car `\n` a été ajouté "en coulisses" à la fin de chaque ligne :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-218.png)

## 📹 Comment imprimer sans nouvelle ligne

Nous pouvons changer ce comportement par défaut en personnalisant la valeur du paramètre `end` de la fonction `print`.

Si nous utilisons la valeur par défaut dans cet exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-219.png)

Nous voyons le résultat imprimé sur deux lignes :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-221.png)

Mais si nous personnalisons la valeur de `end` et la définissons sur `" "`

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-222.png)

Un espace sera ajouté à la fin de la chaîne au lieu du caractère de nouvelle ligne `\n`, donc le résultat des deux instructions d'impression sera affiché sur la même ligne :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-223.png)

Vous pouvez utiliser cela pour imprimer une séquence de valeurs sur une seule ligne, comme dans cet exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-210.png)

Le résultat est :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-211.png)

**💡 Astuce :** Nous ajoutons une instruction conditionnelle pour nous assurer que la virgule ne sera pas ajoutée au dernier nombre de la séquence.

De même, nous pouvons utiliser cela pour imprimer les valeurs d'un itérable sur la même ligne :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-225.png)

Le résultat est :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-213.png)

## 📸 Le caractère de nouvelle ligne dans les fichiers

Le caractère de nouvelle ligne `\n` se trouve également dans les fichiers, mais il est "caché". Lorsque vous voyez une nouvelle ligne dans un fichier texte, un caractère de nouvelle ligne `\n` a été inséré.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-150.png)

Vous pouvez vérifier cela en lisant le fichier avec `<fichier>.readlines()`, comme ceci :

```python
with open("noms.txt", "r") as f:
    print(f.readlines())
```

Le résultat est :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-207.png)

Comme vous pouvez le voir, les trois premières lignes du fichier texte se terminent par un caractère de nouvelle ligne `\n` qui fonctionne "en coulisses".

**💡 Astuce :** Remarquez que seule la dernière ligne du fichier ne se termine pas par un caractère de nouvelle ligne.

## 📹 En résumé

* Le caractère de nouvelle ligne en Python est `\n`. Il est utilisé pour indiquer la fin d'une ligne de texte.
* Vous pouvez imprimer des chaînes sans ajouter de nouvelle ligne avec `end = <caractère>`, où `<caractère>` est le caractère qui sera utilisé pour séparer les lignes.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous pouvez travailler avec le caractère de nouvelle ligne en Python.

[Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐️