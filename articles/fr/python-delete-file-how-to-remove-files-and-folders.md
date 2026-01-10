---
title: Python Supprimer un Fichier – Comment Supprimer des Fichiers et des Dossiers
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-13T12:24:56.000Z'
originalURL: https://freecodecamp.org/news/python-delete-file-how-to-remove-files-and-folders
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pyDeleteFilesAndFolders.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Python Supprimer un Fichier – Comment Supprimer des Fichiers et des Dossiers
seo_desc: 'Many programming languages have built-in functionalities for working with
  files and folders. As a rich programming language with many exciting functionalities
  built into it, Python is not an exception to that.

  Python has the OS and Pathlib modules wi...'
---

De nombreux langages de programmation disposent de fonctionnalités intégrées pour travailler avec des fichiers et des dossiers. En tant que langage de programmation riche avec de nombreuses fonctionnalités passionnantes intégrées, Python n'est pas une exception à cela.

Python dispose des modules `OS` et `Pathlib` avec lesquels vous pouvez créer des fichiers et des dossiers, modifier des fichiers et des dossiers, lire le contenu d'un fichier, et supprimer des fichiers et des dossiers.

Dans cet article, je vais vous montrer comment supprimer des fichiers et des dossiers avec le module `OS`.


## Ce que nous allons couvrir
- [Comment Supprimer des Fichiers avec le Module `OS`](#heading-comment-supprimer-des-fichiers-avec-le-module-os)
- [Comment Supprimer des Fichiers avec le Module `Pathlib`](#heading-comment-supprimer-des-fichiers-avec-le-module-pathlib)
- [Comment Supprimer des Dossiers Vides avec le Module `OS`](#heading-comment-supprimer-des-dossiers-vides-avec-le-module-os)
- [Comment Supprimer des Dossiers Vides avec le Module `Pathlib`](#heading-comment-supprimer-des-dossiers-vides-avec-le-module-pathlib)
- [Comment Supprimer un Dossier Non Vide avec le Module `shutil`](#heading-comment-supprimer-un-dossier-non-vide-avec-le-module-shutil)
- [Conclusion](#heading-conclusion)

## Comment Supprimer des Fichiers avec le Module `OS`
Pour supprimer un fichier avec le module `OS`, vous pouvez utiliser sa méthode `remove()`. Vous devez ensuite spécifier le chemin vers le fichier particulier à l'intérieur de la méthode `remove()`. Mais d'abord, vous devez importer le module `OS` :

```py
import os

os.remove('chemin-vers-le-fichier')
```

Ce code supprime le fichier `questions.py` dans le dossier courant :

```py
import os

os.remove('questions.py')
```

Si le fichier est à l'intérieur d'un autre dossier, vous devez spécifier le chemin complet incluant le nom du fichier, et non seulement le nom du fichier :

```py
import os

os.remove('dossier/nomdefichier.extension')
```

Le code ci-dessous montre comment j'ai supprimé le fichier `faq.txt` à l'intérieur du dossier `textFiles` :
```py
import os

os.remove('textFiles/faq.txt')
```

Pour améliorer les choses, vous pouvez vérifier si le fichier existe avant de le supprimer :

```py
import os

# Extraire le chemin du fichier dans une variable
file_path = 'textFiles/faq.txt'

# Vérifier si le fichier existe avec path.exists()
if os.path.exists(file_path):
    os.remove('textFiles/faq.txt')
    print('fichier supprimé')
else:
    print("Le fichier n'existe pas")
```

Vous pouvez également utiliser `try..except` pour le même but :

```py
import os

try:
    os.remove('textFiles/faq.txt')
    print('fichier supprimé')
except:
    print("Le fichier n'existe pas")
```


## Comment Supprimer des Fichiers avec le Module `Pathlib`
Le module `pathlib` est un module de la bibliothèque standard de Python qui vous fournit une approche orientée objet pour travailler avec les chemins du système de fichiers. Vous pouvez également l'utiliser pour travailler avec des fichiers.

Le module pathlib dispose d'une méthode `unlink()` que vous pouvez utiliser pour supprimer un fichier. Vous devez obtenir le chemin vers le fichier avec `pathlib.Path()`, puis appeler la méthode `unlink()` sur le chemin du fichier :

```py
import pathlib

# obtenir le chemin du fichier
try:
    file_path = pathlib.Path('textFiles/questions.txt')
    file_path.unlink()
    print('fichier supprimé')
except:
    print("Le fichier n'existe pas")
```


## Comment Supprimer des Dossiers Vides avec le Module `OS`
Le module `OS` fournit une méthode `rmdir()` avec laquelle vous pouvez supprimer un dossier.

Mais la façon dont vous supprimez un dossier vide n'est pas la même que celle dont vous supprimez un dossier contenant des fichiers ou des sous-dossiers. Voyons d'abord comment vous pouvez supprimer des dossiers vides.

Voici comment j'ai supprimé un dossier `client` vide :

```py
import os

try:
    os.rmdir('client')
    print('Dossier supprimé')
except:
    print("Le dossier n'existe pas")
```

Si vous tentez de supprimer un dossier qui contient des fichiers ou des sous-dossiers, vous obtiendrez l'erreur `Directory not empty error` :

```py
import os

os.rmdir('textFiles') # OSError: [Errno 66] Directory not empty: 'textFiles'
```


## Comment Supprimer des Dossiers Vides avec le Module `Pathlib`
Avec le module `pathlib`, vous pouvez extraire le chemin du dossier que vous souhaitez supprimer dans une variable et appeler `rmdir()` sur cette variable :

```py
import pathlib

# obtenir le chemin du dossier
try:
    folder_path = pathlib.Path('docs')
    folder_path.rmdir()
    print('Dossier supprimé')
except:
    print("Le dossier n'existe pas")
```

Pour supprimer un dossier qui contient des sous-dossiers et des fichiers, vous devez d'abord supprimer tous les fichiers, puis appeler `os.rmdir()` ou `path.rmdir()` sur le dossier maintenant vide. Mais au lieu de faire cela, vous pouvez utiliser le module `shutil`. Je vais vous montrer cela bientôt.


## Comment Supprimer un Dossier Non Vide avec le Module `shutil`
Le module `shutil` dispose d'une méthode `rmtree()` que vous pouvez utiliser pour supprimer un dossier et son contenu – même s'il contient plusieurs fichiers et sous-dossiers.

La première chose que vous devez faire est d'extraire le chemin vers le dossier dans une variable, puis appeler `rmtree()` sur cette variable.

Voici comment j'ai supprimé un dossier nommé `subTexts` à l'intérieur du dossier `textFiles` :

```py
import shutil

try:
    folder_path = 'textFiles/subTexts'
    shutil.rmtree(folder_path)
    print('Dossier et son contenu supprimés')
except:
    print('Dossier non supprimé')
```

Et voici comment j'ai supprimé le dossier entier `textFiles` (il contient plusieurs fichiers et un sous-dossier) :

```py
import shutil

try:
    folder_path = 'textFiles'
    shutil.rmtree(folder_path)
    print('Dossier et son contenu supprimés') # Dossier et son contenu supprimés
except:
    print('Dossier non supprimé')
```


## Conclusion
Cet article vous a montré comment supprimer un fichier et un dossier vide avec les modules `os` et `pathlib` de Python. Parce que vous pourriez également avoir besoin de supprimer des dossiers non vides, nous avons examiné comment vous pouvez le faire avec le module `shutil`.

Si vous avez trouvé l'article utile, n'hésitez pas à le partager avec vos amis et votre famille.