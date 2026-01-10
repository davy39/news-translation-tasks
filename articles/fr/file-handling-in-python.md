---
title: Gestion des fichiers en Python – Comment créer, lire et écrire dans un fichier
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2022-08-26T15:42:16.000Z'
originalURL: https://freecodecamp.org/news/file-handling-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Author-Share-ImageFREE--4-.jpg
tags:
- name: Python
  slug: python
seo_title: Gestion des fichiers en Python – Comment créer, lire et écrire dans un
  fichier
seo_desc: "In this tutorial, you will learn how to open a file, write to the file,\
  \ and close it. You will also learn how to read from the file using Python. \nBy\
  \ the end of this tutorial, you should know the basics of how to use files in Python.\n\
  File Handling in..."
---

Dans ce tutoriel, vous apprendrez à ouvrir un fichier, à écrire dans le fichier et à le fermer. Vous apprendrez également à lire depuis le fichier en utilisant Python.

À la fin de ce tutoriel, vous devriez connaître les bases de l'utilisation des fichiers en Python.

## **Gestion des fichiers en Python**

La gestion des fichiers est une activité importante dans chaque application web. Les types d'activités que vous pouvez effectuer sur le fichier ouvert sont contrôlés par les modes d'accès. Ceux-ci décrivent comment le fichier sera utilisé après avoir été ouvert.

Ces modes spécifient également où le handle du fichier doit être situé dans le fichier. Similaire à un pointeur, un handle de fichier indique où les données doivent être lues ou placées dans le fichier.

En Python, il existe six méthodes ou modes d'accès, qui sont :

1. **Lecture seule ('r')** : Ce mode ouvre les fichiers texte en lecture seule. Le handle est situé au début du fichier. Il lève une erreur d'E/S si le fichier n'existe pas. C'est également le mode par défaut pour ouvrir les fichiers.
2. **Lecture et écriture ('r+')** : Cette méthode ouvre le fichier pour la lecture et l'écriture. Le handle est situé au début du fichier. Si le fichier n'existe pas, une erreur d'E/S est levée.
3. **Écriture seule ('w')** : Ce mode ouvre le fichier pour l'écriture seule. Les données des fichiers existants sont modifiées et écrasées. Le handle est situé au début du fichier. Si le fichier n'existe pas encore dans le dossier, un nouveau fichier est créé.
4. **Écriture et lecture ('w+')** : Ce mode ouvre le fichier pour la lecture et l'écriture. Le texte est écrasé et supprimé d'un fichier existant. Le handle est situé au début du fichier.
5. **Ajout seul ('a')** : Ce mode permet d'ouvrir le fichier pour l'écriture. Si le fichier n'existe pas encore, un nouveau fichier est créé. Le handle est placé à la fin du fichier. Les nouvelles données écrites seront ajoutées à la fin, suivant les données précédemment écrites.
6. **Ajout et lecture ('a+')** : En utilisant cette méthode, vous pouvez lire et écrire dans le fichier. Si le fichier n'existe pas encore, un nouveau fichier est créé. Le handle est placé à la fin du fichier. Le nouveau texte écrit sera ajouté à la fin, suivant les données précédemment écrites.

Ci-dessous se trouve le code nécessaire pour créer, écrire et lire des fichiers texte en utilisant les méthodes ou modes d'accès de gestion de fichiers Python.

## Comment créer des fichiers en Python

En Python, vous utilisez la fonction `open()` avec l'une des options suivantes – "x" ou "w" – pour créer un nouveau fichier :

* **"x" – Créer** : cette commande créera un nouveau fichier si et seulement s'il n'existe pas déjà de fichier avec ce nom, sinon elle retournera une erreur.

Exemple de création d'un fichier en Python en utilisant la commande "x" :

```python
# création d'un fichier texte avec la fonction de commande "x"

f = open("myfile.txt", "x")
```

Nous avons maintenant créé un nouveau fichier texte vide ! Mais si vous réessayez le code ci-dessus – par exemple, si vous essayez de créer un nouveau fichier avec le même nom que vous avez utilisé ci-dessus (si vous voulez réutiliser le nom de fichier ci-dessus), vous obtiendrez une erreur vous notifiant que le fichier existe déjà. Cela ressemblera à l'image ci-dessous :

![IDLE Shell montrant une erreur que myfile.txt n'existe pas](https://www.freecodecamp.org/news/content/images/2023/08/idle-shell.png)

* **"w" – Écrire** : cette commande créera un nouveau fichier texte, qu'il y ait ou non un fichier en mémoire avec le nouveau nom spécifié. Elle ne retourne pas d'erreur si elle trouve un fichier existant avec le même nom – au lieu de cela, elle écrasera le fichier existant.

Exemple de création d'un fichier avec la commande "w" :

```python
# création d'un fichier texte avec la fonction de commande "w"

f = open("myfile.txt", "w")

# Cette commande "w" peut également être utilisée pour créer un nouveau fichier, mais contrairement à la commande "x", la commande "w" écrasera tout fichier existant trouvé avec le même nom de fichier.
```

Avec le code ci-dessus, que le fichier existe ou non dans la mémoire, vous pouvez toujours utiliser ce code. Gardez simplement à l'esprit qu'il écrasera le fichier s'il trouve un fichier existant avec le même nom.

## Comment écrire dans un fichier en Python

Il existe deux méthodes pour écrire dans un fichier en Python, qui sont :

### La méthode `write()` :

Cette fonction insère la chaîne dans le fichier texte sur une seule ligne.

Sur la base du fichier que nous avons créé ci-dessus, la ligne de code ci-dessous insérera la chaîne dans le fichier texte créé, qui est "myfile.txt".

```python

file.write("Hello There\n")
```

### La méthode `writelines()` :

Cette fonction insère plusieurs chaînes en même temps. Une liste d'éléments de chaîne est créée, et chaque chaîne est ensuite ajoutée au fichier texte.

En utilisant le fichier créé précédemment ci-dessus, la ligne de code ci-dessous insérera la chaîne dans le fichier texte créé, qui est "myfile.txt".

```python
f.writelines(["Hello World ", "You are welcome to Fcc\n"])
```

Exemple :

```python
# Ce programme montre comment écrire des données dans un fichier texte.

file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

# j'ai assigné ["This is Lagos \n","This is Python \n","This is Fcc \n"] à la variable L, vous pouvez utiliser n'importe quelle lettre ou mot de votre choix.
# Les variables sont des conteneurs dans lesquels des valeurs peuvent être stockées.
# Le \n est placé pour indiquer la fin de la ligne.

file.write("Hello There \n")
file.writelines(L)
file.close()

# Utilisez close() pour changer les modes d'accès au fichier
```

## Comment lire depuis un fichier texte en Python

Il existe trois méthodes pour lire des données depuis un fichier texte en Python. Elles sont :

### La méthode `read()` :

Cette fonction retourne les octets lus sous forme de chaîne. Si aucun n n'est spécifié, elle lit alors le fichier entier.

Exemple :

```python
f = open("myfiles.txt", "r")
# ('r') ouvre les fichiers texte en lecture seule
print(f.read())
# Le "f.read" imprime les données du fichier texte dans le shell lors de l'exécution.
```

### La méthode readline() :

Cette fonction lit une ligne depuis un fichier et la retourne sous forme de chaîne. Elle lit au plus n octets pour le n spécifié. Mais même si n est supérieur à la longueur de la ligne, elle ne lit pas plus d'une ligne.

```python
f = open("myfiles.txt", "r")
print(f.readline())

```

### La méthode `readlines()` :

Cette fonction lit toutes les lignes et les retourne sous forme d'éléments de chaîne dans une liste, une pour chaque ligne.

Vous pouvez lire les deux premières lignes en appelant `readline()` deux fois, lisant les deux premières lignes du fichier :

```python
f = open("myfiles.txt", "r")
print(f.readline())
print(f.readline())

```

## Comment fermer un fichier texte en Python

Il est bon de toujours fermer le fichier lorsque vous avez terminé avec lui.

### Exemple de fermeture d'un fichier texte :

Cette fonction ferme le fichier texte lorsque vous avez terminé de le modifier :

```python
f = open("myfiles.txt", "r")
print(f.readline())
f.close()

```

La fonction close() à la fin du code indique à Python que vous avez terminé avec cette section de création ou de lecture – c'est comme dire Fin.

### Exemple :

Le programme ci-dessous montre plus d'exemples de façons de lire et d'écrire des données dans un fichier texte. Chaque ligne de code contient des commentaires pour vous aider à comprendre ce qui se passe :

```python
# Programme pour montrer diverses façons de lire et
# écrire des données dans un fichier texte.

file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

# j'ai assigné ["This is Lagos \n","This is Python \n","This is Fcc \n"]
# à la variable L
  
# Le \n est placé pour indiquer la fin de la ligne

file.write("Hello There \n")
file.writelines(L)
file.close()
# utilisez close() pour changer les modes d'accès au fichier



file = open("myfile.txt","r+") 
print("Sortie de la fonction Read ")
print(file.read())
print()
  
# La fonction seek(n) place le handle du fichier au n-ième
# octet depuis le début.
file.seek(0) 
  
print( "Sortie de la fonction Readline ")
print(file.readline()) 
print()
  
file.seek(0)
  
# Pour montrer la différence entre read et readline

print("Sortie de la fonction Read(12) ") 
print(file.read(12))
print()

file.seek(0)
  
print("Sortie de la fonction Readline(8) ") 
print(file.readline(8))
  
file.seek(0)
# fonction readlines
print("Sortie de la fonction Readlines ") 
print(file.readlines()) 
print()
file.close()


```

Voici la sortie du code ci-dessus lorsqu'il est exécuté dans le shell. J'ai assigné "This is Lagos", "This is Python", et "This is Fcc" à "L" puis demandé d'imprimer en utilisant la fonction ''file.read''.

Le code ci-dessus montre que la fonction "readline()" retourne la lettre en fonction du nombre spécifié, tandis que la fonction "readlines()" retourne chaque chaîne assignée à "L" y compris le \n. C'est-à-dire que la fonction "readlines()" imprimera toutes les données du fichier.

![IDLE Shell montrant la sortie du programme](https://www.freecodecamp.org/news/content/images/2023/08/output-file.png)

## Conclusion

Espérons qu'après avoir suivi ce tutoriel, vous comprenez ce qu'est la gestion des fichiers en Python. Nous avons également appris les modes/méthodes nécessaires pour créer, écrire, lire et fermer un fichier texte en utilisant quelques exemples de base de Python.

Merci d'avoir lu !