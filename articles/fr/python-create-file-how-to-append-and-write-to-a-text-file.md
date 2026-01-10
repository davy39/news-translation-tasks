---
title: Python Créer un Fichier – Comment Ajouter et Écrire dans un Fichier Texte
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-07T16:44:25.000Z'
originalURL: https://freecodecamp.org/news/python-create-file-how-to-append-and-write-to-a-text-file
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/s-migaj-ocUAiaMTCM0-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Créer un Fichier – Comment Ajouter et Écrire dans un Fichier Texte
seo_desc: 'In coding, files are used to store data. Then you can easily access that
  data at any point.

  Reading, writing, and editing files in Python is a common task, since the language
  provides us with built-in functions that allow us to do so.

  In this article...'
---

En programmation, les fichiers sont utilisés pour stocker des données. Vous pouvez ensuite accéder facilement à ces données à tout moment.

Lire, écrire et modifier des fichiers en Python est une tâche courante, car le langage fournit des fonctions intégrées qui nous permettent de le faire.

Dans cet article, je vais créer un projet simple où j'écrirai, ajouterai et enfin lirai un fichier texte en Python pour vous montrer comment cela se fait.

Vous pouvez me suivre et suivre les mêmes étapes que moi.

C'est parti !

## Comment configurer la structure du projet

La première étape consiste à configurer la structure du répertoire du projet.

Choisissez un endroit où vous souhaitez créer un nouveau répertoire et suivez les étapes ci-dessous.

Je crée le projet dans mon répertoire personnel.

```bash
# cette commande vous déplace dans votre répertoire personnel si vous n'y êtes pas déjà
cd

# créez un nouveau répertoire et donnez-lui un nom
mkdir python_text

# déplacez-vous dans le répertoire que vous venez de créer
cd python_text

# créez deux fichiers vides dans le même répertoire : un fichier texte et un pour contenir vos scripts Python
 touch text.txt scripts.py

# ouvrez Visual Studio Code pour éditer
code .
```

Pour l'instant, le fichier texte est vide :

![Screenshot-2021-09-02-at-11.17.28-AM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-11.17.28-AM.png)

Ajoutons quelque chose.

## Comment écrire dans des fichiers texte en Python

La meilleure pratique pour écrire, ajouter et lire des fichiers texte en Python est d'utiliser le mot-clé `with`.

La syntaxe générale ressemble à ceci :

```
with open("path_to_and_name_of_file","mode") as variable_name:
    variable_name.write('Ce que je veux écrire va ici')
```

Explication :

- Vous commencez d'abord par le mot-clé `with`.
- Ensuite, vous ouvrez le fichier texte. La fonction `open()` retourne un objet fichier et prend deux paramètres : le chemin vers le fichier et le nom du fichier lui-même que vous souhaitez ouvrir. Le fichier dans cet exemple est dans le même répertoire que le script Python, donc le chemin est simple. Le deuxième paramètre est le mode dans lequel le fichier sera ouvert. Pour écrire dans les fichiers, le mode est `w` pour `write` (écrire).
- Ensuite, nous avons le mot-clé `as`.
- Ensuite, le nom de la variable sert de lieu de stockage temporaire pour le contenu textuel que vous allez stocker.
- La méthode `.write()` est utilisée pour écrire dans le fichier texte et ajouter le contenu de la chaîne que vous souhaitez.

Donc, pour ajouter du texte au fichier texte, dans `scripts.py` ajoutez :

```python
with open("text.txt","w") as file:
    file.write("J'apprends Python !\n")
    file.write("J'en profite vraiment !\n")
    file.write("Et je veux ajouter plus de lignes pour dire à quel point j'aime ça")
```

Pour ajouter le texte sur différentes lignes, comme je l'ai fait dans l'exemple ci-dessus, vous devez explicitement ajouter vous-même le caractère de nouvelle ligne, `\n`.

Ouvrez le terminal intégré dans Visual Studio Code (`Control ~`) et exécutez le code en tapant : `python3 scripts.py`.

Consultez `text.txt` et il devrait avoir ce qui suit ajouté :

![Screenshot-2021-09-02-at-6.51.51-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-6.51.51-PM.png)

Il est important de noter que chaque fois que vous utilisez la méthode `.write()` et exécutez votre code, tout texte que vous aviez précédemment sera écrasé.

Supposons que j'avais déjà du texte factice dans mon fichier `text.txt` lorsque je l'ai créé pour la première fois :

![Screenshot-2021-09-02-at-7.03.03-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.03.03-PM.png)

Si j'exécute le code précédent :

```python
with open("text.txt","w") as file:
    file.write("J'apprends Python !\n")
    file.write("J'en profite vraiment !\n")
    file.write("Et je veux ajouter plus de lignes pour dire à quel point j'aime ça")
```

Il ressemblera maintenant à ceci :

![Screenshot-2021-09-02-at-7.04.23-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.04.23-PM.png)

J'ai perdu toutes mes données précédentes.

## Comment ajouter du texte à un fichier en Python

L'ajout fonctionne de manière similaire à l'écriture.

Mais cette fois, vous ouvrez le fichier texte pour ajouter du texte, avec le paramètre pour le mode dans la fonction `open()` étant `a` pour `append` (ajouter) :

```
with open("text.txt","a") as file:
    file.write("Ce que je veux ajouter va ici")
```

Tout ce qui se trouve dans la méthode `.write()` sera ajouté à la fin du fichier texte.

Donc, pour ajouter plus de texte à `text.txt`, vous ajoutez ce qui suit :

```python
with open("text.txt","a") as file:
    file.write("J'ajoute plus de lignes\n")
    file.write("Et plus…")
```

Après avoir exécuté le code à nouveau, `text.txt` devrait maintenant ressembler à ceci :

![Screenshot-2021-09-02-at-7.15.51-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.15.51-PM.png)

L'ancien texte n'est pas effacé.

Le nouveau texte est ajouté immédiatement après l'ancien, et vous devez à nouveau ajouter explicitement un caractère de nouvelle ligne :

```python
with open("text.txt","a") as file:
    file.write("\n")
    file.write("J'ajoute plus de lignes\n")
    file.write("Et plus…")
```

![Screenshot-2021-09-02-at-7.18.15-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.18.15-PM.png)

## Comment lire un fichier en Python

Pour lire un fichier, vous utilisez à nouveau le mot-clé `with` et la fonction `open()` avec deux arguments : le premier est le chemin et le nom du fichier, et le second est le mode dans lequel le fichier sera ouvert.

Pour ouvrir des fichiers texte, le mode est `r` pour `read` (lire).

Ensuite, la fonction `print()` imprime sur la console et prend comme arguments le nom de la variable avec la fonction `read()`.

```python
with open('text.txt','r') as file:
    print(file.read())
```

Sortie :

![Screenshot-2021-09-07-at-1.44.04-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-07-at-1.44.04-PM.png)

Pour lire un fichier en Python, vous pourriez également créer une boucle `for` pour parcourir chaque ligne du fichier texte :

```python
with open("text.txt","r") as file:
    for line in file:
        print(line)
```

Sortie :

![Screenshot-2021-09-07-at-1.46.25-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-07-at-1.46.25-PM.png)

Avec cette méthode, chaque ligne est imprimée séparément.

## Conclusion

Cet article vous a montré des exemples simples de la façon d'écrire, de modifier et de lire des fichiers en Python.

Si vous souhaitez en savoir plus sur le langage de programmation Python, freeCodeCamp propose une certification gratuite [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/) où vous commencez par les bases et passez aux aspects plus complexes du langage. À la fin, vous construirez cinq projets pour mettre en pratique ce que vous avez appris.

Merci d'avoir lu et bon apprentissage !