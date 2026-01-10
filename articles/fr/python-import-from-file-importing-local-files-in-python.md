---
title: Python Import depuis un Fichier – Importer des Fichiers Locaux en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-06T22:40:27.000Z'
originalURL: https://freecodecamp.org/news/python-import-from-file-importing-local-files-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Shittu-Olumide-Python-Import-from-File
seo_title: Python Import depuis un Fichier – Importer des Fichiers Locaux en Python
---

Importing-Local-Files-in-Python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nIl y a de nombreuses raisons pour lesquelles vous pourriez vouloir importer des fichiers\
  \ en Python. Peut-être faites-vous de l'analyse de données, du traitement de fichiers personnalisé, de la manipulation de fichiers,\
  \ de l'automatisation et ainsi de suite. \nHeureusement, Python offre un certain nombre de méthodes\
  \ pour vous aider à accomplir cette tâche. "
---

Par Shittu Olumide

Il y a de nombreuses raisons pour lesquelles vous pourriez vouloir importer des fichiers en Python. Peut-être faites-vous de l'analyse de données, du traitement de fichiers personnalisé, de la manipulation de fichiers, de l'automatisation et ainsi de suite. 

Heureusement, Python offre un certain nombre de méthodes pour vous aider à accomplir cette tâche. 

Dans cet article, nous examinerons certaines de ces méthodes et approches. Nous passerons en revue un exemple pour chaque méthode et discuterons des meilleures pratiques. 

## Comment Importer des Fichiers en Python en Utilisant les Fonctions Intégrées de Python

Pour lire des fichiers texte, nous pouvons utiliser la fonction `open()` pour ouvrir le fichier en mode lecture, puis lire son contenu en utilisant des méthodes comme `read()`, `readline()`, ou `readlines()`. 

Ensuite, pour écrire des données dans un fichier texte, nous pouvons ouvrir le fichier en mode écriture en utilisant `open()`, puis utiliser la méthode `write()` pour écrire des données dans le fichier.

### Comment ouvrir un fichier : 

Pour ouvrir un fichier, nous pouvons utiliser la fonction `open()`. Elle prend deux arguments : le chemin du fichier et le mode dans lequel nous voulons ouvrir le fichier (mode lecture, mode écriture, mode ajout, etc.). 

Par exemple, pour ouvrir un fichier nommé "data.txt" en mode lecture situé dans le répertoire courant, nous pouvons utiliser le code suivant :

```python
file = open("data.txt", "r")
```

### Comment lire le contenu d'un fichier : 

Après avoir ouvert le fichier, nous pouvons lire son contenu en utilisant diverses méthodes. Les méthodes les plus couramment utilisées sont :

* `read()` : Lit le contenu entier du fichier sous forme de chaîne unique.
* `readline()` : Lit une seule ligne du fichier.
* `readlines()` : Lit toutes les lignes du fichier et les retourne sous forme de liste de chaînes.

Voici un exemple qui lit et imprime le contenu d'un fichier ligne par ligne :

```python
file = open("data.txt", "r")
for line in file.readlines():
    print(line)
file.close()
```

### Comment écrire dans un fichier : 

Pour écrire des données dans un fichier, ouvrez-le en mode écriture ("w") ou en mode ajout ("a"). En mode écriture, le contenu existant du fichier est écrasé. En mode ajout, le nouveau contenu est ajouté à la fin du fichier. Après avoir ouvert le fichier, nous pouvons utiliser la méthode `write()` pour écrire des données dans le fichier.

Voici un exemple qui écrit une liste de noms dans un fichier nommé "names.txt" :

```python
names = ["John", "Alice", "Bob"]

file = open("names.txt", "w")
for name in names:
    file.write(name + "\n")
file.close()
```

_**Note** : Il est important de fermer le fichier en utilisant la méthode `close()` après avoir terminé la lecture ou l'écriture. Cela garantit que toutes les modifications apportées au fichier sont enregistrées et que les ressources sont libérées._

## Comment Importer des Fichiers en Python en Utilisant la Bibliothèque Pandas

Pour importer des fichiers CSV, nous pouvons utiliser la fonction `read_csv()` de la bibliothèque Pandas. Cette fonction charge automatiquement les données dans un DataFrame, offrant des capacités puissantes de manipulation de données. 

Pour travailler avec des fichiers Excel, Pandas fournit la fonction `read_excel()`, qui lit les données d'un fichier Excel et retourne un DataFrame.  
  
Pour importer des fichiers locaux en Python en utilisant la bibliothèque Pandas, nous pouvons suivre ces étapes :

1. Installer Pandas

```python
pip install pandas
```

2.   Importer la bibliothèque Pandas

```python
import pandas as pd
```

3.   Spécifier le chemin du fichier : Déterminer le chemin du fichier local que nous voulons importer. Il peut s'agir d'un chemin absolu (par exemple, "**C:/path/to/file.csv**") ou d'un chemin relatif (par exemple, "**data/file.csv**").

4.   Utiliser Pandas pour importer le fichier : Pandas fournit diverses fonctions pour importer différents formats de fichiers. La fonction la plus couramment utilisée est `pd.read_csv()` pour importer des fichiers CSV. Voici un exemple de la façon d'importer un fichier CSV :

```python
file_path = "data/file.csv"  # Remplacer par votre chemin de fichier
df = pd.read_csv(file_path)
```

Si nous importons un fichier Excel, nous pouvons utiliser `pd.read_excel()` à la place :

```python
file_path = "data/file.xlsx"  # Remplacer par votre chemin de fichier
df = pd.read_excel(file_path)
```

Pandas prend également en charge divers autres formats de fichiers, tels que JSON, SQL et HDF5, avec des fonctions spécifiques comme `read_json()`, `read_sql()` et `read_hdf()`.

## Comment Importer des Fichiers en Python en Utilisant la Bibliothèque NumPy

Similaire à Pandas, NumPy nous permet d'importer des fichiers locaux en Python. Il offre également des fonctionnalités pour travailler avec des données structurées et des tableaux multidimensionnels, ce qui le rend utile pour importer et manipuler des formats de données complexes.

Pour importer des fichiers locaux en Python en utilisant la bibliothèque NumPy, nous pouvons suivre ces étapes :

1. Installer NumPy

```python
pip install numpy
```

2.   Importer la bibliothèque NumPy

```python
import numpy as np
```

3.   Spécifier le chemin du fichier : Déterminer le chemin du fichier local que nous voulons importer. Nous devons nous assurer de fournir le chemin correct vers le fichier, y compris le nom du fichier et son extension.

4.   Utiliser la fonction `loadtxt()` ou `genfromtxt()` : NumPy fournit deux fonctions principales, `loadtxt()` et `genfromtxt()`, pour importer des données depuis des fichiers locaux.

Utilisation de `loadtxt()` : Si notre fichier contient une grille régulière de valeurs (par exemple, un fichier CSV), nous pouvons utiliser la fonction `loadtxt()`. Voici un exemple de la façon de l'utiliser :

```python
data = np.loadtxt('path/to/your/file.csv', delimiter=',')
```

Utilisation de `genfromtxt()` : Si notre fichier contient des données manquantes ou irrégulières (par exemple, un fichier CSV avec des valeurs manquantes), nous pouvons utiliser la fonction `genfromtxt()`. Elle offre plus de flexibilité dans la gestion de différents formats de données. Voici un exemple :

```python
data = np.genfromtxt('path/to/your/file.csv', delimiter=',', missing_values='NA', filling_values=0)
```

Dans les deux cas, nous devons simplement remplacer `'path/to/your/file.csv'` par le chemin et le nom réels de notre fichier local.

## Comment Gérer les Chemins de Fichiers et les Répertoires

Lors de l'importation de fichiers locaux en Python, il est essentiel de comprendre les chemins de fichiers et les répertoires pour localiser et accéder efficacement aux fichiers souhaités. 

La gestion des chemins de fichiers et des répertoires implique de gérer les emplacements et les structures des fichiers sur notre ordinateur ou serveur. Voici les concepts et techniques clés pour gérer les chemins de fichiers et les répertoires lors de l'importation de fichiers locaux en Python :

### Chemins de Fichiers :

* Un **chemin de fichier** est une chaîne qui représente l'emplacement d'un fichier ou d'un répertoire dans le système de fichiers. 
* Un **chemin absolu** spécifie le chemin complet en partant du répertoire racine.
* Un **chemin relatif** spécifie le chemin relatif au répertoire de travail actuel.

### Navigation dans les Répertoires :

* **Répertoire de travail actuel** : Le répertoire à partir duquel Python est actuellement en cours d'exécution.
* **Module os** : Module intégré de Python pour interagir avec le système d'exploitation.
* **os.getcwd()** : Retourne le répertoire de travail actuel.
* **os.chdir(path)** : Change le répertoire de travail actuel pour le chemin spécifié.
* **Module os.path** : Fournit des fonctions pour manipuler les chemins de fichiers.
* **os.path.join(path, *paths)** : Assemble plusieurs composants de chemin de manière intelligente.
* **os.path.abspath(path)** : Retourne le chemin absolu d'un fichier ou d'un répertoire.

**Importation de Fichiers** :

Une fois que nous avons le chemin de fichier correct, nous pouvons utiliser diverses méthodes pour importer des fichiers dans notre programme Python.

* **Fonctions intégrées** : La fonction `open()` est couramment utilisée pour lire des fichiers texte.
* **Bibliothèque Pandas** : Offre des fonctions pour charger et importer divers formats de fichiers, tels que CSV, Excel, JSON, et plus encore.
* **Bibliothèque NumPy** : Fournit des méthodes pour importer des données depuis des fichiers binaires.
* **Bibliothèques spécialisées** : Certaines bibliothèques sont conçues pour gérer des types de fichiers spécifiques, comme Pillow pour les images ou librosa pour l'audio.

## Conclusion

Tout au long de cet article, nous avons exploré diverses méthodes et bibliothèques pour importer différents types de fichiers, tels que des fichiers texte, des fichiers CSV, des fichiers Excel, des fichiers binaires et des formats de données spécialisés comme les images et l'audio.

En exploitant les capacités de Python et de ses diverses bibliothèques, les développeurs peuvent facilement importer et intégrer des fichiers locaux dans leurs projets, ouvrant un monde de possibilités pour l'exploration, l'analyse et la visualisation de données. 

La capacité à importer des fichiers locaux de manière efficace permet aux professionnels des données de tirer parti de la vaste quantité d'informations disponibles dans divers formats, ouvrant la voie à des informations précieuses et à une prise de décision éclairée.

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon Codage !