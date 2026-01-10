---
title: Les environnements virtuels Python expliqués avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/python-virtual-environments-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d12740569d1a4ca35bd.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
- name: virtualenv
  slug: virtualenv
seo_title: Les environnements virtuels Python expliqués avec des exemples
seo_desc: 'Virtual environments can be described as isolated installation directories.
  This isolation allows you to localized the installation of your project’s dependencies,
  without forcing you to install them system-wide.

  Imagine you have two applications, Ap...'
---

Les environnements virtuels peuvent être décrits comme des répertoires d'installation isolés. Cette isolation vous permet de localiser l'installation des dépendances de votre projet, sans vous forcer à les installer à l'échelle du système.

Imaginez que vous avez deux applications, App1 et App2. Les deux utilisent le package Pak, mais nécessitent des versions différentes. Si vous installez la version 2.3 de Pak pour App1, vous ne pourriez pas exécuter App2 car elle nécessite la version 3.1. 

C'est là que les environnements virtuels deviennent utiles.

Avantages :

* Vous pouvez avoir plusieurs environnements, avec plusieurs ensembles de packages, sans conflits entre eux. Ainsi, les exigences de différents projets peuvent être satisfaites simultanément.
* Vous pouvez facilement publier votre projet avec ses propres modules dépendants.

Voici deux façons de créer des environnements virtuels Python.

## **Virtualenv**

`[virtualenv](https://virtualenv.pypa.io/en/stable/)` est un outil utilisé pour créer des environnements Python isolés. Il crée un dossier qui contient tous les exécutables nécessaires pour utiliser les packages dont un projet Python aurait besoin.

Vous pouvez l'installer avec `pip` :

```text
pip install virtualenv
```

Vérifiez l'installation avec la commande suivante :

```text
virtualenv --version
```

### **Créer un environnement**

Pour créer un environnement virtuel, utilisez :

```text
virtualenv --no-site-packages my-env
```

Cela crée un dossier dans le répertoire courant avec le nom de l'environnement (`my-env/`). Ce dossier contient les répertoires pour installer les modules et les exécutables Python.

Vous pouvez également spécifier la version de Python avec laquelle vous souhaitez travailler. Utilisez simplement l'argument `--python=/chemin/vers/version/python`. Par exemple, `python2.7` :

```text
virtualenv --python=/usr/bin/python2.7 my-env
```

### **Lister les environnements**

Vous pouvez lister les environnements disponibles avec :

```text
lsvirtualenv
```

### **Activer un environnement**

Avant de pouvoir commencer à utiliser l'environnement, vous devez l'activer :

```text
source my-env/bin/activate
```

Cela garantit que seuls les packages sous `my-env/` sont utilisés.

Vous remarquerez que le nom de l'environnement est affiché à gauche de l'invite. Ainsi, vous pouvez voir quel est l'environnement actif.

### **Installer des packages**

Vous pouvez installer des packages un par un, ou en définissant un fichier `requirements.txt` pour votre projet.

```text
pip install some-package
pip install -r requirements.txt
```

Si vous souhaitez créer un fichier `requirements.txt` à partir des packages déjà installés, exécutez la commande suivante :

```text
pip freeze > requirements.txt
```

Le fichier contiendra la liste de tous les packages installés dans l'environnement actuel, ainsi que leurs versions respectives. Cela vous aidera à publier votre projet avec ses propres modules dépendants.

### **Désactiver un environnement**

Si vous avez terminé de travailler avec l'environnement virtuel, vous pouvez le désactiver avec :

```text
deactivate
```

Cela vous ramène à l'interpréteur Python par défaut du système avec toutes ses bibliothèques installées.

### **Supprimer un environnement**

Supprimez simplement le dossier de l'environnement.

## **Conda**

[`Conda`](https://conda.io/docs/index.html) est un gestionnaire de packages, de dépendances et d'environnements pour de nombreux langages, y compris Python.

Pour installer Conda, suivez ces [instructions](https://conda.io/docs/user-guide/install/index.html).

### **Créer un environnement**

Pour créer un environnement virtuel, utilisez :

```text
conda create --name my-env
```

Conda créera le dossier correspondant dans le répertoire d'installation de Conda.

Vous pouvez également spécifier la version de Python avec laquelle vous souhaitez travailler :

```text
conda create --name my-env python=3.6
```

### **Lister les environnements**

Vous pouvez lister tous les environnements disponibles avec :

```text
conda info --envs
```

### **Activer un environnement**

Avant de pouvoir commencer à utiliser l'environnement, vous devez l'activer :

```text
source activate my-env
```

### **Installer des packages**

La même chose qu'avec `virtualenv`.

### **Désactiver un environnement**

Si vous avez terminé de travailler avec l'environnement virtuel, vous pouvez le désactiver avec :

```text
source deactivate
```

### **Supprimer un environnement**

Si vous souhaitez supprimer un environnement de Conda, utilisez :

```text
conda remove --name my-env
```