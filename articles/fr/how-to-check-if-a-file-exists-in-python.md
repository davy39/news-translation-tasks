---
title: Comment vérifier si un fichier existe en Python avec isFile() et exists()
date: '2023-01-05T17:23:20.000Z'
author: Dionysia Lemonaki
authorURL: https://www.freecodecamp.org/news/author/dionysialemonaki/
originalURL: https://freecodecamp.org/news/how-to-check-if-a-file-exists-in-python
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-francis-seura-802412.jpg
tags:
- name: Python
  slug: python
seo_desc: 'When working with files in Python, there may be times when you need to
  check whether a file exists or not.

  But why should you check if a file exists in the first place?

  Confirming the existence of a specific file comes in handy when you want to perfo...'
---


Lorsque vous manipulez des fichiers en Python, il arrive que vous deviez vérifier si un fichier existe ou non.

<!-- more -->

Mais pourquoi devriez-vous vérifier l'existence d'un fichier en premier lieu ?

Confirmer l'existence d'un fichier spécifique est très pratique lorsque vous souhaitez effectuer des opérations particulières, comme [l'ouvrir, le lire ou y écrire][1].

Si vous tentez d'effectuer l'une des opérations mentionnées ci-dessus alors que le fichier n'existe pas, vous rencontrerez des bugs et votre programme finira par planter.

Ainsi, pour effectuer des opérations et éviter que votre programme ne s'arrête brutalement, vérifier si un fichier existe sur un chemin donné est une première étape utile.

Heureusement, Python dispose de plusieurs méthodes natives pour vérifier si un fichier existe, comme les modules intégrés `os.path` et `pathlib`.

Plus précisément, en utilisant le module `os.path`, vous avez accès à :

-   la méthode `os.path.isfile(path)` qui renvoie `True` si le `path` est un fichier ou un lien symbolique vers un fichier.
-   la méthode `os.path.exists(path)` qui renvoie `True` si le `path` est un fichier, un répertoire ou un lien symbolique vers un fichier.

Et en utilisant le module `pathlib`, vous avez accès à la fonction `pathlib.Path(path).is_file()`, qui renvoie `True` si `path` est un fichier et qu'il existe.

Dans cet article, vous apprendrez comment utiliser Python pour vérifier si un fichier existe à l'aide des modules `os.path` et `pathlib`.

C'est parti !

## Comment vérifier si un fichier existe à l'aide du module `os.path`

Le module `os` fait partie de la bibliothèque standard (également appelée `stdlib`) de Python et permet d'accéder au système d'exploitation et d'interagir avec lui.

Avec le module `os`, vous pouvez utiliser des fonctionnalités qui dépendent du système d'exploitation sous-jacent, comme la création et la suppression de fichiers et de dossiers, ainsi que la copie et le déplacement de contenus de dossiers, pour n'en citer que quelques-unes.

Puisqu'il fait partie de la bibliothèque standard, le module `os` est pré-installé lorsque vous installez Python sur votre système local. Il vous suffit de l'importer en haut de votre fichier Python à l'aide de l'instruction `import` :

```
import os
```

Le module `os.path` est un sous-module du module `os`.

Il fournit deux méthodes pour manipuler les fichiers - plus précisément les méthodes `isfile()` et `exists()` qui renvoient soit `True`, soit `False`, selon qu'un fichier existe ou non.

Puisque vous utiliserez le sous-module `os.path`, vous devrez plutôt l'importer en haut de votre fichier, comme ceci :

```
import os.path
```

### Comment vérifier si un fichier existe à l'aide de la méthode `os.path.isfile()` en Python

La syntaxe générale de la méthode `isfile()` ressemble à ceci :

```
os.path.isfile(path)
```

La méthode n'accepte qu'un seul argument, `path`, qui représente le chemin défini vers le fichier dont vous souhaitez confirmer l'existence.

L'argument `path` est une chaîne de caractères entre guillemets.

La valeur de retour de la méthode `isfile()` est une valeur booléenne - soit `True`, soit `False` selon que ce fichier existe.

Gardez à l'esprit que si le chemin se termine par un nom de répertoire et non par un fichier, elle renverra `False`.

Voyons un exemple de la méthode en action.

Je veux vérifier si un fichier `example.txt` existe dans mon répertoire de travail actuel, `python_project`.

Le fichier `example.txt` se trouve au même niveau que mon fichier Python `main.py`, j'utilise donc un chemin de fichier relatif.

Je stocke le chemin vers `example.txt` dans une variable nommée `path`.

Ensuite, j'utilise la méthode `isfile()` et je passe `path` comme argument pour vérifier si `example.txt` existe à ce chemin.

Comme le fichier existe, la valeur de retour est `True` :

```
import os.path

path = './example.txt'

check_file = os.path.isfile(path)

print(check_file)

# output

# True
```

D'accord, mais qu'en est-il des chemins absolus ?

Voici le code équivalent lors de l'utilisation d'un chemin absolu. Le fichier `example.txt` se trouve dans un répertoire `python_project`, qui est lui-même dans mon répertoire personnel, `/Users/dionysialemonaki/` :

```
import os.path

path = '/Users/dionysialemonaki/python_project/example.txt'

print(os.path.isfile(file_path))

# Output

# True
```

Et comme mentionné précédemment, la méthode `isfile()` ne fonctionne que pour les fichiers et _non_ pour les répertoires :

```
import os.path

path = '/Users/dionysialemonaki/python_project'

check_file = os.path.isfile(path)

print(check_file)

# output

# False
```

Si votre chemin se termine par un répertoire, la valeur de retour est `False`.

### Comment vérifier si un fichier existe à l'aide de la méthode `os.path.exists()` en Python

La syntaxe générale de la méthode `exists()` ressemble à ceci :

```
os.path.exists(path)
```

Comme vous pouvez le voir d'après la syntaxe ci-dessus, la méthode `exists()` est similaire à la méthode `isfile()`.

La méthode `os.path.exists()` vérifie si le chemin spécifié existe.

La principale différence entre `exists()` et `isfile()` est que `exists()` renverra `True` si le chemin donné vers un dossier ou un fichier existe, tandis que `isfile()` ne renvoie `True` que si le chemin donné est un chemin vers un fichier et non un dossier.

Gardez à l'esprit que si vous n'avez pas les accès et les permissions pour le répertoire, `exists()` renverra `False` même si le chemin existe.

Revenons à l'exemple de la section précédente et vérifions si le fichier `example.txt` existe dans le répertoire de travail actuel à l'aide de la méthode `exists()` :

```
import os.path

path = './example.txt'

check_file = os.path.exists(path)

print(check_file)

# output

# True
```

Puisque le chemin vers `example.txt` existe, la sortie est `True`.

Comme mentionné précédemment, la méthode `exists()` vérifie si le chemin vers un répertoire est valide.

Dans la section précédente, lorsque j'ai utilisé la méthode `isfile()` et que le chemin pointait vers un répertoire, la sortie était `False` même si ce répertoire existait.

Lors de l'utilisation de la méthode `exists()`, si le chemin vers un répertoire existe, la sortie sera `True` :

```
import os.path

path = '/Users/dionysialemonaki/python_project'

check_file = os.path.exists(path)

print(check_file)

# output

# True
```

La méthode `exists()` est très utile lorsque vous voulez vérifier si un fichier _ou_ un répertoire existe.

## Comment vérifier si un fichier existe à l'aide du module `pathlib`

La version 3.4 de Python a introduit le module `pathlib`.

L'utilisation du module `pathlib` pour vérifier si un fichier existe ou non est une approche [orientée objet][2] pour travailler avec les chemins du système de fichiers.

Comme pour le module `os.path` précédemment, vous devez importer le module `pathlib`.

Plus précisément, vous devez importer la classe `Path` du module `pathlib` comme ceci :

```
from pathlib import Path
```

Ensuite, créez une nouvelle instance de la classe `Path` et initialisez-la avec le chemin du fichier que vous souhaitez vérifier :

```
from pathlib import Path

# create a Path object with the path to the file
path = Path('./example.txt')
```

Vous pouvez utiliser la fonction `type()` pour vérifier le type de données :

```
from pathlib import Path

path = Path('./example.txt')

print(type(path))

# output is a pathlib object
# <class 'pathlib.PosixPath'>
```

Cela confirme que vous avez créé un objet `Path`.

Voyons comment utiliser le module `pathlib` pour vérifier si un fichier existe à l'aide de la méthode `is_file()`, l'une des méthodes intégrées disponibles avec le module `pathlib`.

### Comment vérifier si un fichier existe à l'aide de la méthode `Path.is_file()` en Python

La méthode `is_file()` vérifie si un fichier existe.

Elle renvoie `True` si l'objet `Path` pointe vers un fichier et `False` si le fichier n'existe pas.

Voyons un exemple de son fonctionnement :

```
from pathlib import Path

# create a Path object with the path to the file
path = Path('./example.txt')

print(path.is_file())

# output

# True
```

Puisque le fichier `example.txt` existe dans le chemin spécifié, la méthode `is_file()` renvoie `True`.

## Conclusion

Dans cet article, vous avez appris comment vérifier si un fichier existe en Python à l'aide des modules `os.path` et `pathlib` ainsi que de leurs méthodes associées.

Nous espérons que vous avez compris les différences entre ces modules et quand utiliser chacun d'eux.

Merci de votre lecture, et bon code !

[1]: https://www.freecodecamp.org/news/how-to-read-files-in-python/
[2]: https://www.freecodecamp.org/news/crash-course-object-oriented-programming-in-python/