---
title: Python Ouvrir un Fichier – Comment Lire un Fichier Texte Ligne par Ligne
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-13T14:00:03.000Z'
originalURL: https://freecodecamp.org/news/python-open-file-how-to-read-a-text-file-line-by-line
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/alex-chumak-zGuBURGGmdY-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Ouvrir un Fichier – Comment Lire un Fichier Texte Ligne par Ligne
seo_desc: "In Python, there are a few ways you can read a text file. \nIn this article,\
  \ I will go over the open() function, the read(), readline(), readlines(), close()\
  \ methods, and the with keyword.\nWhat is the open() function in Python?\nIf you\
  \ want to read a t..."
---

En Python, il existe plusieurs façons de lire un fichier texte. 

Dans cet article, je vais passer en revue la fonction `open()`, les méthodes `read()`, `readline()`, `readlines()`, `close()`, et le mot-clé `with`.

## Qu'est-ce que la fonction open() en Python ? 

Si vous souhaitez lire un fichier texte en Python, vous devez d'abord l'ouvrir.

Voici la syntaxe de base de la fonction `open()` de Python :

```py
open("nom du fichier que vous souhaitez ouvrir", "mode optionnel")
```

### Noms de fichiers et chemins corrects

Si le fichier texte et votre fichier actuel se trouvent dans le même répertoire ("dossier"), alors vous pouvez simplement référencer le nom du fichier dans la fonction `open()`. 

```py
open("demo.txt")
```

Voici un exemple où les deux fichiers se trouvent dans le même répertoire :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-1.49.16-AM.png)

Si votre fichier texte se trouve dans un répertoire différent, vous devrez alors référencer le chemin correct pour le fichier texte. 

Dans cet exemple, le fichier `random-text` se trouve dans un dossier différent de `main.py` :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-2.00.27-AM.png)

Pour accéder à ce fichier dans `main.py`, vous devez inclure le nom du dossier avec le nom du fichier.

```py
open("text-files/random-text.txt")
```

Si vous n'avez pas le chemin correct pour le fichier, vous obtiendrez un message d'erreur comme celui-ci :

```py
open("random-text.txt")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-2.03.33-AM.png)

Il est vraiment important de garder une trace du répertoire dans lequel vous vous trouvez afin de référencer le chemin correct.

### Paramètre Mode optionnel dans `open()`

Il existe différents modes lorsque vous travaillez avec des fichiers. Le mode par défaut est le mode lecture. 

La lettre `r` signifie mode lecture. 

```py
open("demo.txt", mode="r")
```

Vous pouvez également omettre `mode=` et simplement écrire `"r"`.

```py
open("demo.txt", "r")
```

Il existe d'autres types de modes tels que `"w"` pour l'écriture ou `"a"` pour l'ajout. Je ne vais pas entrer dans les détails des autres modes car nous allons nous concentrer uniquement sur la lecture des fichiers. 

Pour une liste complète des autres modes, veuillez consulter la [documentation](https://docs.python.org/3/library/functions.html#open). 

### Paramètres supplémentaires pour la fonction `open()` en Python

La fonction `open()` peut prendre ces paramètres optionnels. 

* buffering
* encoding
* errors
* newline
* closefd
* opener

Pour en savoir plus sur ces paramètres optionnels, veuillez consulter la [documentation](https://docs.python.org/3/library/functions.html#open). 

## Qu'est-ce que la méthode readable() en Python ? 

Si vous souhaitez vérifier si un fichier peut être lu, vous pouvez utiliser la méthode `readable()`. Cela retournera `True` ou `False`.

Cet exemple retournerait `True` car nous sommes en mode lecture :

```py
file = open("demo.txt")
print(file.readable())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.36.37-AM.png)

Si je modifiais cet exemple pour utiliser le mode `"w"` (écriture), alors la méthode `readable()` retournerait `False` :

```py
file = open("demo.txt", "w")
print(file.readable())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.36.18-AM.png)

## Qu'est-ce que la méthode read() en Python ? 

La méthode `read()` va lire tout le contenu du fichier en tant qu'une seule chaîne. C'est une bonne méthode à utiliser si vous n'avez pas beaucoup de contenu dans le fichier texte. 

Dans cet exemple, j'utilise la méthode `read()` pour imprimer une liste de noms à partir du fichier `demo.txt` :

```py
file = open("demo.txt")
print(file.read())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-2.43.59-AM.png)

Cette méthode peut prendre un paramètre optionnel appelé size. Au lieu de lire le fichier entier, seule une partie de celui-ci sera lue.

Si nous modifions l'exemple précédent, nous pouvons imprimer uniquement le premier mot en ajoutant le nombre 4 comme argument pour `read()`. 

```py
file = open("demo.txt")
print(file.read(4))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.01.30-AM.png)

Si l'argument size est omis, ou si le nombre est négatif, alors le fichier entier sera lu. 

## Qu'est-ce que la méthode close() en Python ? 

Une fois que vous avez terminé de lire un fichier, il est important de le fermer. Si vous oubliez de fermer votre fichier, cela peut causer des problèmes.

Voici un exemple de la façon de fermer le fichier `demo.txt` :

```py
file = open("demo.txt")
print(file.read())
file.close()
```

### Comment utiliser le mot-clé `with` pour fermer les fichiers en Python

Une façon de s'assurer que votre fichier est fermé est d'utiliser le mot-clé `with`. Cela est considéré comme une bonne pratique, car le fichier se fermera automatiquement au lieu de devoir le fermer manuellement. 

Voici comment réécrire notre exemple en utilisant le mot-clé `with` :

```py
with open("demo.txt") as file:
    print(file.read())
```

## Qu'est-ce que la méthode readline() en Python ? 

Cette méthode va lire une ligne du fichier et la retourner.

Dans cet exemple, nous avons un fichier texte avec ces deux phrases :

```txt
This is the first line
This is the second line
```

Si nous utilisons la méthode `readline()`, elle n'imprimera que la première phrase du fichier. 

```py
with open("demo.txt") as file:
    print(file.readline())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.57.14-AM.png)

Cette méthode prend également le paramètre optionnel size. Nous pouvons modifier l'exemple pour ajouter le nombre 7 afin de ne lire et imprimer que `This is` :

```py
with open("demo.txt") as file:
    print(file.readline(7))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-4.08.03-AM.png)

## Qu'est-ce que la méthode readlines() en Python ? 

Cette méthode lira et retournera une liste de toutes les lignes du fichier. 

Dans cet exemple, nous allons imprimer nos articles d'épicerie sous forme de liste en utilisant la méthode `readlines()`. 

```py
with open("demo.txt") as file:
    print(file.readlines())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-4.19.23-AM.png)

## Comment utiliser une boucle for pour lire les lignes d'un fichier en Python

Une alternative à ces différentes méthodes de lecture serait d'utiliser une `boucle for`.

Dans cet exemple, nous pouvons imprimer tous les éléments du fichier `demo.txt` en parcourant l'objet. 

```py
with open("demo.txt") as file:
    for item in file:
        print(item)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-4.27.49-AM.png)

## Conclusion

Si vous souhaitez lire un fichier texte en Python, vous devez d'abord l'ouvrir.

```py
open("nom du fichier que vous souhaitez ouvrir", "mode optionnel")

```

Si le fichier texte et votre fichier actuel se trouvent dans le même répertoire ("dossier"), alors vous pouvez simplement référencer le nom du fichier dans la fonction `open()`. 

Si votre fichier texte se trouve dans un répertoire différent, vous devrez alors référencer le chemin correct pour le fichier texte. 

La fonction `open()` prend le paramètre mode optionnel. Le mode par défaut est le mode lecture. 

```py
open("demo.txt", "r")
```

Si vous souhaitez vérifier si un fichier peut être lu, vous pouvez utiliser la méthode `readable()`. Cela retournera `True` ou `False`.

```py
file.readable()
```

La méthode `read()` va lire tout le contenu du fichier en tant qu'une seule chaîne.

```py
file.read()
```

Une fois que vous avez terminé de lire un fichier, il est important de le fermer. Si vous oubliez de fermer votre fichier, cela peut causer des problèmes.

```py
file.close()
```

Une façon de s'assurer que votre fichier est fermé est d'utiliser le mot-clé `with`.

```py
with open("demo.txt") as file:
    print(file.read())
```

La méthode `readline()` va lire une ligne du fichier et la retourner.

```py
file.readline()
```

La méthode `readlines()` lira et retournera une liste de toutes les lignes du fichier.

```py
file.readlines()
```

Une alternative à ces différentes méthodes de lecture serait d'utiliser une `boucle for`.

```py
with open("demo.txt") as file:
    for item in file:
        print(item)
```

J'espère que vous avez apprécié cet article et bonne chance dans votre apprentissage de Python.