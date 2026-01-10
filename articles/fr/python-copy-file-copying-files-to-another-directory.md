---
title: Python Copier un Fichier – Copier des Fichiers vers un Autre Répertoire
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-04-20T14:16:43.000Z'
originalURL: https://freecodecamp.org/news/python-copy-file-copying-files-to-another-directory
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/maksym-kaharlytskyi-Q9y3LRuuxmg-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Copier un Fichier – Copier des Fichiers vers un Autre Répertoire
seo_desc: 'When working with Python, there may be times when you need to copy a file.
  Copying files comes in handy when you need to create a backup.

  In this article, you will learn how to copy a file in Python using the shutil module
  and its different methods.

  ...'
---

Lorsque vous travaillez avec Python, il peut arriver que vous ayez besoin de copier un fichier. Copier des fichiers est utile lorsque vous devez créer une sauvegarde.

Dans cet article, vous apprendrez comment copier un fichier en Python en utilisant le module `shutil` et ses différentes méthodes.

Le module `shutil` (abréviation de shell utility) en Python vous permet de manipuler des fichiers et des répertoires et d'effectuer des opérations sur les fichiers et les répertoires.

Commençons !


## Comment Copier un Fichier en Utilisant la Méthode `shutil.copyfile()` en Python
Pour copier le contenu d'un fichier dans un autre fichier, utilisez la méthode `shutil.copyfile()`.

Examinons l'exemple suivant :

```python
# importer le module
import shutil

# copier le contenu du fichier demo.py dans un nouveau fichier appelé demo1.py
shutil.copyfile('./demo.py', './demo1.py')
```

J'importe d'abord le module avec l'instruction `import shutil`.

Ensuite, j'utilise la méthode `shutil.copyfile()` qui a la syntaxe suivante :

```python
shutil.copyfile('fichier_source', 'fichier_destination')
```

Décomposons cela :

- `fichier_source` est le chemin vers le fichier que je veux copier – dans ce cas, le fichier est le fichier `demo.py` dans mon répertoire de travail actuel (`./`).
- `fichier_destination` est le chemin vers le nouveau fichier que je veux créer. Dans ce cas, je veux copier le contenu du fichier source dans un nouveau fichier, `demo1.py`, dans mon répertoire de travail actuel. La destination ne peut pas être un répertoire – elle doit être un nom de fichier.

Lorsque j'exécute le code de l'exemple ci-dessus, un nouveau fichier nommé `demo1.py` est créé dans mon répertoire de travail actuel avec une copie du contenu de `demo.py`. Si le fichier de destination existe déjà, il est remplacé.

Notez que la méthode `shutil.copyfile()` ne copie que le contenu du fichier source. 

Aucune métadonnée de fichier (comme les dates de création et les heures de modification) ou permissions de fichier ne sont copiées vers le fichier de destination spécifié. 

Ainsi, la méthode `shutil.copyfile()` est utile lorsque vous souhaitez renommer le fichier que vous copiez et que vous ne vous souciez pas de sauvegarder les permissions et les métadonnées du fichier.


## Comment Copier un Fichier en Utilisant la Méthode `shutil.copy()` en Python
Pour copier un fichier vers un autre répertoire, utilisez la méthode `shutil.copy()`.

Examinons l'exemple suivant :

```python
# importer le module
import shutil

# Spécifier le chemin du fichier que vous souhaitez copier
fichier_a_copier = './demo.py'

# Spécifier le chemin du répertoire de destination où vous souhaitez copier
repertoire_destination = './projects'

# Utiliser la méthode shutil.copy() pour copier le fichier vers le répertoire de destination
shutil.copy(fichier_a_copier, repertoire_destination)
```

J'importe d'abord le module en utilisant l'instruction `import shutil`.

Ensuite, je spécifie le chemin du fichier que je veux copier et je le sauvegarde dans une variable nommée `fichier_a_copier`. Dans ce cas, je veux copier le fichier `demo.py` dans mon répertoire de travail actuel.

Ensuite, je spécifie le répertoire où je veux copier le fichier et je le sauvegarde dans une variable nommée `repertoire_destination`. Dans ce cas, je veux sauvegarder le fichier dans le répertoire `projects` dans mon répertoire de travail actuel.

Enfin, j'utilise la méthode `shutil.copy()` qui prend deux arguments : 

- Le chemin du fichier que vous souhaitez copier – dans ce cas, la variable `fichier_a_copier`.
- Le fichier ou répertoire dans lequel vous souhaitez copier le fichier – dans ce cas, la variable `repertoire_destination`.

Lorsque j'exécute le code de l'exemple ci-dessus, la méthode `shutil.copy()` crée une copie du fichier `demo.py` dans le répertoire `projects`.

Gardez à l'esprit que si un fichier avec le même nom existe déjà dans le répertoire de destination, le fichier existant est écrasé par le nouveau fichier.

Une autre chose à garder à l'esprit est que la méthode `shutil.copy()` copie les permissions de fichier, mais elle ne copie pas les métadonnées vers le répertoire de destination.


## Comment Copier un Fichier en Utilisant la Méthode `shutil.copy2()` en Python
La méthode `shutil.copy2()` fonctionne de manière similaire à la méthode `shutil.copy()`. 

La seule différence entre `shutil.copy()` et `shutil.copy2()` est que `shutil.copy2()` préserve les métadonnées du fichier original lors de la copie.

```python
# importer le module
import shutil

# Spécifier le chemin du fichier que vous souhaitez copier
fichier_a_copier = './demo.py'

# Spécifier le chemin du répertoire de destination où vous souhaitez copier le fichier
repertoire_destination = './projects'

# Utiliser la méthode shutil.copy2() pour copier le fichier vers le répertoire de destination
shutil.copy2(fichier_a_copier, repertoire_destination)
```


## Comment Copier un Fichier en Utilisant la Méthode `shutil.copyfileobj()` en Python
Pour copier le contenu d'un objet fichier vers un autre objet fichier de destination spécifié, utilisez la méthode `shutil.copyfileobj()`. Cette méthode prend deux objets fichier comme arguments – un objet fichier source et un objet fichier destination. La destination ne peut pas être un répertoire.

Prenons l'exemple suivant :

```python
# importer le module
import shutil

# vous devez ouvrir le fichier source en mode binaire avec 'rb'
fichier_source =  open('demo.py', 'rb')

# vous devez ouvrir le fichier de destination en mode binaire avec 'wb'
fichier_destination = open('project.py', 'wb')

# utiliser la méthode shutil.copyobj() pour copier le contenu de fichier_source vers fichier_destination
shutil.copyfileobj(fichier_source, fichier_destination)
```

Dans l'exemple ci-dessus, la méthode `shutil.copyobj()` copie le contenu de `demo.py` vers le fichier `project.py`.

Gardez à l'esprit que cette méthode ne préserve pas les permissions de fichier et ne copie pas les métadonnées.


## Conclusion
Et voilà ! Vous savez maintenant comment copier des fichiers en Python en utilisant le module `shutil` et les méthodes qu'il offre.

Pour vous aider à choisir quelle méthode utiliser, reportez-vous au tableau suivant qui résume ce que fait chaque méthode.

| Méthode  | Préserve les permissions ?  | Copie les métadonnées ?  | La destination peut-elle être un répertoire ?  | Accepte un objet fichier ?
|---|---|---|---|---|
| `shutil.copyfile()`  |  Non | Non  | Non  | Non |
|  `shutil.copy()` | Oui  | Non  | Oui  | Non |
| `shutil.copy2()`  | Oui  | Oui  | Oui  | Non|
| `shutil.copyfileobj()`  |  Non | Non  | Non  | Oui |


Pour en savoir plus sur Python, consultez le cours [Python pour débutants](https://www.freecodecamp.org/news/python-programming-course/) de freeCodeCamp.

Merci d'avoir lu, et bon codage !