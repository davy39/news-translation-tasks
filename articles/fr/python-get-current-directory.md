---
title: 'Python : Obtenir le répertoire actuel – Équivalent de Print Working Directory
  PWD'
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-28T16:27:30.000Z'
originalURL: https://freecodecamp.org/news/python-get-current-directory
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-357514.jpg
tags:
- name: Python
  slug: python
seo_title: 'Python : Obtenir le répertoire actuel – Équivalent de Print Working Directory
  PWD'
seo_desc: 'In this article, you will learn how to get the current working directory
  (another name for folder) in Python, which is the equivalent of using the pwd command.

  There are a couple of ways to get the current working directory in Python:


  By using the o...'
---

Dans cet article, vous apprendrez comment obtenir le répertoire de travail actuel (un autre nom pour dossier) en Python, ce qui est l'équivalent de l'utilisation de la commande `pwd`.

Il existe plusieurs façons d'obtenir le répertoire de travail actuel en Python :

- En utilisant le module `os` et la méthode `os.getcwd()`.
- En utilisant le module `pathlib` et la méthode `Path.cwd()`.

C'est parti !


## Comment obtenir le répertoire actuel en utilisant la méthode `os.getcwd()` en Python
Le module `os`, qui fait partie de la bibliothèque standard de Python (également connue sous le nom de stdlib), vous permet d'accéder à votre système d'exploitation et d'interagir avec lui.

Pour utiliser le module `os` dans votre projet, vous devez inclure la ligne suivante en haut de votre fichier Python :

```python
import os
```

Une fois que vous avez importé le module `os`, vous avez accès à la méthode `os.getcwd()`, qui vous permet d'obtenir le chemin complet du répertoire de travail actuel. 

Regardons l'exemple suivant :

```python
import os

# obtenir le répertoire de travail actuel
current_working_directory = os.getcwd()

# afficher le résultat dans la console
print(current_working_directory)

# le résultat ressemblera à quelque chose comme ceci sur un système macOS
# /Users/dionysialemonaki/Documents/my-projects/python-project
```

Le résultat est une chaîne de caractères qui contient le chemin absolu vers le répertoire de travail actuel – dans ce cas, `python-project`. 

Pour vérifier le type de données du résultat, utilisez la fonction `type()` comme ceci :

```python
print(type(current_working_directory))

# résultat

# <class 'str'>
```

Notez que le répertoire de travail actuel n'a pas de barre oblique de fin, `/`.

Gardez également à l'esprit que le résultat variera en fonction du répertoire à partir duquel vous exécutez le script Python ainsi que de votre système d'exploitation.


## Comment obtenir le répertoire actuel en utilisant la méthode `Path.cwd()` en Python
Dans la section précédente, vous avez vu comment utiliser le module `os` pour obtenir le répertoire de travail actuel. Cependant, vous pouvez utiliser le module `pathlib` pour obtenir le même résultat.

Le module `pathlib` a été introduit dans la bibliothèque standard dans la version 3.4 de Python et offre une approche orientée objet pour travailler avec les chemins du système de fichiers et manipuler les fichiers.

Pour utiliser le module `pathlib`, vous devez d'abord l'importer en haut de votre fichier Python :

```python
from pathlib import Path
```

Une fois que vous avez importé le module `pathlib`, vous pouvez utiliser la méthode de classe `Path.cwd()`, qui vous permet d'obtenir le répertoire de travail actuel.

Regardons l'exemple suivant :

```python
from pathlib import Path

# obtenir le répertoire de travail actuel
current_working_directory = Path.cwd()

# afficher le résultat dans la console
print(current_working_directory)

# le résultat ressemblera à quelque chose comme ceci sur un système macOS
# /Users/dionysialemonaki/Documents/my-projects/python-project
```

Comme vous pouvez le voir, le résultat est le même que celui obtenu en utilisant la méthode `os.getcwd()`. La seule différence est le type de données du résultat :

```python
print(type(current_working_directory))

# résultat

# <class 'pathlib.PosixPath'>
```


## Conclusion
Et voilà ! Vous savez maintenant comment obtenir le chemin complet du répertoire actuel en Python en utilisant les modules `os` et `pathlib`.

Pour en savoir plus sur Python, consultez le [cours Python pour débutants de freeCodeCamp](https://www.freecodecamp.org/news/python-programming-course/).

Merci de votre lecture, et bon codage !