---
title: 'ModuleNotFoundError: aucun module nommé Python Error [Résolu]'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-12T14:17:11.000Z'
originalURL: https://freecodecamp.org/news/module-not-found-error-in-python-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/module-not-found-error.png
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: 'ModuleNotFoundError: aucun module nommé Python Error [Résolu]'
seo_desc: 'By Dillion Megida

  When you try to import a module in a Python file, Python tries to resolve this module
  in several ways. Sometimes, Python throws the ModuleNotFoundError afterward. What
  does this error mean in Python?

  As the name implies, this error ...'
---

Par Dillion Megida

Lorsque vous essayez d'importer un module dans un fichier Python, Python tente de résoudre ce module de plusieurs manières. Parfois, Python génère l'erreur **ModuleNotFoundError**. Que signifie cette erreur en Python ?

Comme son nom l'indique, cette erreur se produit lorsque vous essayez d'accéder ou d'utiliser un module qui ne peut pas être trouvé. Dans le cas du titre, le "module nommé **Python**" ne peut pas être trouvé.

*Python* ici peut être n'importe quel module. Voici une erreur lorsque j'essaie d'importer un module `numpys` qui ne peut pas être trouvé :

```python
import numpys as np
```

Voici à quoi ressemble l'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-341.png)

Voici quelques raisons pour lesquelles un module peut ne pas être trouvé :

- vous n'avez pas le module que vous avez essayé d'importer installé sur votre ordinateur
- vous avez mal orthographié un module (ce qui revient toujours au point précédent, à savoir que le module mal orthographié n'est pas installé)...par exemple, orthographier `numpy` comme `numpys` lors de l'importation
- vous utilisez une casse incorrecte pour un module (ce qui revient toujours au premier point)...par exemple, orthographier `numpy` comme `NumPy` lors de l'importation générera l'erreur de module non trouvé car les deux modules sont "différents"
- vous importez un module en utilisant le mauvais chemin

## Comment corriger le ModuleNotFoundError en Python

Comme je l'ai mentionné dans la section précédente, il y a plusieurs raisons pour lesquelles un module peut ne pas être trouvé. Voici quelques solutions.

### 1. Assurez-vous que les modules importés sont installés

Prenons par exemple, `numpy`. Vous utilisez ce module dans votre code dans un fichier appelé "test.py" comme ceci :

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

Si vous essayez d'exécuter ce code avec `python test.py` et que vous obtenez cette erreur :

```bash
ModuleNotFoundError: No module named "numpy"
```

Alors il est très probable que le module `numpy` ne soit pas installé sur votre appareil. Vous pouvez installer le module comme ceci :

```python
python -m pip install numpy
```

Une fois installé, le code précédent fonctionnera correctement et vous obtiendrez le résultat imprimé dans votre terminal :

```bash
[1, 2, 3]
```

### 2. Assurez-vous que les modules sont orthographiés correctement

Dans certains cas, vous avez peut-être installé le module dont vous avez besoin, mais l'utiliser génère toujours l'erreur ModuleNotFound. Dans de tels cas, il se peut que vous l'ayez mal orthographié. Prenons par exemple ce code :

```python
import nompy as np

arr = np.array([1, 2, 3])

print(arr)
```

Ici, vous avez installé `numpy` mais l'exécution du code ci-dessus génère cette erreur :

```bash
ModuleNotFoundError: No module named "nompy"
```

Cette erreur est due à la mauvaise orthographe du module `numpy` en `nompy` (avec la lettre **o** au lieu de **u**). Vous pouvez corriger cette erreur en orthographiant correctement le module.

### 3. Assurez-vous que les modules sont dans la bonne casse

Similaire au problème d'orthographe pour les erreurs de module non trouvé, il pourrait également s'agir d'une orthographe correcte du module, mais avec une mauvaise casse. Voici un exemple :

```python
import Numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

Pour ce code, vous avez `numpy` installé mais l'exécution du code ci-dessus générera cette erreur :

```bash
ModuleNotFoundError: No module named 'Numpy'
```

En raison des différences de casse, `numpy` et `Numpy` sont des modules différents. Vous pouvez corriger cette erreur en orthographiant le module avec la bonne casse.

### 4. Assurez-vous d'utiliser les bons chemins

En Python, vous pouvez importer des modules à partir d'autres fichiers en utilisant des chemins **absolus** ou **relatifs**. Pour cet exemple, je vais me concentrer sur les chemins absolus.

Lorsque vous essayez d'accéder à un module à partir du mauvais chemin, vous obtiendrez également l'erreur de module non trouvé ici. Voici un exemple :

Disons que vous avez un dossier de projet appelé **test**. Dans celui-ci, vous avez deux dossiers **demoA** et **demoB**.

**demoA** contient un fichier `__init__.py` (pour montrer qu'il s'agit d'un package Python) et un module `test1.py`.

**demoA** contient également un fichier `__init__.py` et un module `test2.py`.

Voici la structure :

```bash
 test
     demoA
         __init__.py
        test1.py
     demoB
         __init__.py
         test2.py
```

Voici le contenu de `test1.py` :

```python
def hello():
  print("hello")
```

Et disons que vous voulez utiliser cette fonction `hello` déclarée dans `test2.py`. Le code suivant générera une erreur de module non trouvé :

```python
import demoA.test as test1

test1.hello()
```

Ce code générera l'erreur suivante :

```bash
ModuleNotFoundError: No module named 'demoA.test'
```

La raison en est que nous avons utilisé le mauvais chemin pour accéder au module `test1`. Le bon chemin devrait être `demoA.test1`. Lorsque vous corrigez cela, le code fonctionne :

```python
import demoA.test1 as test1

test1.hello()
# hello
```

## Conclusion

Pour résoudre un module importé, Python vérifie des endroits comme la bibliothèque intégrée, les modules installés et les modules dans le projet actuel. S'il est incapable de résoudre ce module, il génère l'erreur **ModuleNotFoundError**.

Parfois, vous n'avez pas ce module installé, vous devez donc l'installer. Parfois, il s'agit d'un module mal orthographié, ou d'une mauvaise casse, ou d'un mauvais chemin. Dans cet article, j'ai montré quatre façons possibles de corriger cette erreur si vous la rencontrez.

J'espère que vous avez appris quelque chose :)