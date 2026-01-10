---
title: Créer un répertoire en Python – Comment créer un dossier
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-23T13:39:03.000Z'
originalURL: https://freecodecamp.org/news/creating-a-directory-in-python-how-to-create-a-folder
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-51191.jpg
tags:
- name: Python
  slug: python
seo_title: Créer un répertoire en Python – Comment créer un dossier
seo_desc: "In this article, you will learn how to create new directories (which is\
  \ another name for folders) in Python. \nYou will also learn how to create a nested\
  \ directory structure. \nTo work with directories in Python, you first need to include\
  \ the os  modul..."
---

Dans cet article, vous apprendrez comment créer de nouveaux répertoires (qui est un autre nom pour les dossiers) en Python. 

Vous apprendrez également comment créer une structure de répertoires imbriqués. 

Pour travailler avec des répertoires en Python, vous devez d'abord inclure le module `os` dans votre projet, ce qui vous permet d'interagir avec votre système d'exploitation.

Le module `os` vous permet également d'utiliser les deux méthodes que nous aborderons dans cet article :

- la méthode `os.mkdir()`
- la méthode `os.makedirs()`

C'est parti !


## Comment créer un répertoire unique en utilisant la méthode `os.mkdir()` en Python
Comme mentionné précédemment, pour travailler avec des répertoires en Python, vous devez d'abord inclure le module `os`.

Pour ce faire, ajoutez la ligne de code suivante en haut de votre fichier :

```python
import os
```

Le code ci-dessus vous permettra d'utiliser la méthode `os.mkdir()` pour créer un nouveau répertoire unique.

La méthode `os.mkdir()` accepte un argument – le chemin du répertoire.

```python
import os

# spécifiez le chemin du répertoire – assurez-vous de l'entourer de guillemets
path = './projects'

# créer un nouveau répertoire unique
os.mkdir(path)
```

Le code ci-dessus créera un répertoire `projects` dans le répertoire de travail actuel.

Notez que le `./` représente le répertoire de travail actuel. Vous pouvez omettre cette partie et écrire seulement `projects` lors de la spécification du chemin – le résultat sera le même !


### Comment gérer les exceptions lors de l'utilisation de la méthode `os.mkdir` en Python
Mais que se passe-t-il lorsque le répertoire que vous essayez de créer existe déjà ? Une exception `FileExistsError` est levée :

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    os.mkdir(path)
FileExistsError: [Errno 17] File exists: './projects'
```

Une façon de gérer cette exception est de vérifier si le fichier existe déjà en utilisant un bloc `if..else` :

```python
import os

path = './projects'

# vérifier si le répertoire existe déjà
if not os.path.exists(path):
  os.mkdir(path)
  print("Dossier %s créé !" % path)
else:
  print("Le dossier %s existe déjà" % path)
```

Dans l'exemple ci-dessus, j'ai d'abord vérifié si le répertoire `./projects` existe déjà en utilisant la méthode `os.path.exists()`. 

Si c'est le cas, j'obtiendrai la sortie suivante au lieu d'une `FileExistsError` :

```
Le dossier ./projects existe déjà
```

Si le fichier n'existe pas, alors un nouveau dossier `projects` est créé dans le répertoire de travail actuel, et j'obtiens la sortie suivante :

```
Dossier ./projects créé !
```

Alternativement, vous pouvez utiliser un bloc `try/except` pour gérer les exceptions :

```python
import os

path = './projects'

try:
    os.mkdir(path)
    print("Dossier %s créé !" % path)
except FileExistsError:
    print("Le dossier %s existe déjà" % path)
```

Si un dossier `projects` existe déjà dans le répertoire de travail actuel, vous obtiendrez la sortie suivante au lieu d'un message d'erreur :

```
Le dossier ./projects existe déjà
```


## Comment créer un répertoire avec des sous-répertoires en utilisant la méthode `os.makedirs()` en Python
La méthode `os.mkdir()` ne vous permet pas de créer un sous-répertoire. Au lieu de cela, elle vous permet de créer un répertoire unique.

Pour créer une structure de répertoires imbriqués (comme un répertoire à l'intérieur d'un autre répertoire), utilisez la méthode `os.makedirs()`.
 
La méthode `os.makedirs()` accepte un argument – le chemin complet du dossier que vous souhaitez créer.

```python
import os

# définir le nom du répertoire avec ses sous-répertoires
path = './projects/games/game01'

os.makedirs(path)
```

Dans l'exemple ci-dessus, j'ai créé un répertoire `projects` dans le répertoire de travail actuel.

À l'intérieur de projects, j'ai créé un autre répertoire, `games`. Et à l'intérieur de `games`, j'ai créé encore un autre répertoire, `games01`.


## Conclusion
Et voilà ! Vous savez maintenant comment créer un répertoire unique et un répertoire avec des sous-répertoires en Python.

Pour en savoir plus sur Python, consultez le [cours Python pour débutants](https://www.freecodecamp.org/news/python-programming-course/) de freeCodeCamp.

Merci de votre lecture, et bon codage !