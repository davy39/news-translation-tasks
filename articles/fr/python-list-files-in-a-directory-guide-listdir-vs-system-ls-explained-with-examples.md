---
title: Guide Python pour lister les fichiers dans un répertoire - listdir VS system("ls")
  expliqué avec des exemples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-04-06T14:10:27.000Z'
originalURL: https://freecodecamp.org/news/python-list-files-in-a-directory-guide-listdir-vs-system-ls-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/listdir-vs-system-v2.png
tags:
- name: command
  slug: command
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: Guide Python pour lister les fichiers dans un répertoire - listdir VS system("ls")
  expliqué avec des exemples
seo_desc: '🔹 Welcome

  If you want to learn how these functions work behind the scenes and how you can
  use their full power, then this article is for you.

  We will start by diving into concepts that are essential to work with listdir and
  system:


  The built-in Pyt...'
---

## 🔹 Bienvenue

Si vous voulez apprendre comment ces fonctions fonctionnent en coulisses et comment vous pouvez utiliser leur plein pouvoir, alors cet article est pour vous.

Nous allons commencer par plonger dans des concepts essentiels pour travailler avec `listdir` et `system` :

* Le module `os` intégré de Python et comment l'importer.
* Les concepts de "répertoire" et "répertoire de travail courant".
* Comment vérifier et changer votre répertoire de travail courant.
* La différence entre un chemin absolu et un chemin relatif.

Ensuite, nous plongerons dans les fonctions elles-mêmes :

* Comment travailler avec la fonction `listdir` et quand l'utiliser.
* Comment travailler avec la fonction `system("ls")` et quand l'utiliser.
* Des exemples des deux et comment elles fonctionnent en coulisses.

Commençons ! ⭐

## 🔸 Le module OS

Les deux fonctions dont nous allons discuter : `listdir()` et `system()` appartiennent au module `os`. Ce module inclut des fonctions utilisées pour interagir avec votre système d'exploitation, effectuant des actions comme :

* Créer un nouveau répertoire.
* Renommer un répertoire existant.
* Supprimer un répertoire.
* Afficher le chemin vers votre répertoire de travail courant.
* Et bien plus encore !

**💡 Conseils :**

* Un **répertoire** est ce que nous connaissons communément sous le nom de "dossier", où nous stockons généralement des fichiers liés et/ou d'autres répertoires, créant une hiérarchie de répertoires dans des répertoires appelés sous-répertoires. Un exemple de répertoire est votre dossier "Documents".
* Un **module** est un fichier qui contient du code Python lié.

### Comment importer le module OS

Pour utiliser le module `os` dans votre script, vous devez l'"importer". Importer un module signifie obtenir l'accès à toutes les fonctions et variables stockées dans le module. Nous importons un module lorsque nous voulons utiliser son code dans notre script.

Pour importer le module `os`, vous devez simplement inclure cette ligne en haut de votre script Python ou exécuter cette ligne dans l'interpréteur interactif :

```python
import os
```

Cela vous donnera accès à toutes les fonctions définies dans le module `os`.

**💡 Conseil :** ce module était déjà installé lorsque vous avez installé Python 3, donc vous pourrez l'utiliser immédiatement.

Pour pouvoir utiliser les fonctions du module `os`, vous devrez ajouter le préfixe `os.` avant le nom de la fonction que vous souhaitez appeler, comme ceci :

```python
os.<function>(<params>)
```

Par exemple :

```
os.mkdir("Nouveau Dossier")
```

### Comment importer des fonctions individuelles

Si vous allez travailler avec seulement une ou deux fonctions du module, vous pouvez les importer individuellement en utilisant cette syntaxe :

```
from <module> import <function1>, <function2>, ...
```

Par exemple :

```python
from os import listdir, system
```

Dans ce cas, vous pouvez appeler les fonctions dans votre script comme vous le feriez normalement, **sans** ajouter le préfixe `os.`, comme ceci :

```python
<function>(<params>)
```

Par exemple :

```
mkdir("Nouveau Dossier")
```

## 🔹 Répertoire de travail courant

Maintenant, voyons un concept très important que vous devez connaître avant de commencer à travailler avec `listdir` et `system`. Votre répertoire de travail courant, comme son nom l'indique, est le répertoire (dossier) où vous travaillez actuellement.

Vous pouvez vérifier votre répertoire de travail courant avec cette fonction du module `os` :

```python
os.getcwd()
```

Cela vous montrera le chemin vers votre répertoire de travail courant.

💡 **Conseil :** `cwd` signifie "répertoire de travail courant".

### Depuis l'interpréteur interactif

Si j'exécute cette commande dans l'interpréteur interactif (Windows), je vois ceci :

```python
>>> os.getcwd()
'C:\\Users\\estef\\AppData\\Local\\Programs\\Python\\Python38-32'
```

Ceci est le chemin complet vers mon répertoire de travail courant :

```python
'C:\\Users\\estef\\AppData\\Local\\Programs\\Python\\Python38-32'
```

### Depuis un script

Si j'exécute cette commande depuis un script, comme ceci :

```python
import os
print(os.getcwd())
```

Je vois :

```python
C:\Users\estef\Documents\freeCodeCamp\freeCodeCamp News\listdir vs system
```

Le chemin complet vers le script (son emplacement dans le système, dans la hiérarchie des répertoires).

💡 **Conseil :** Si vous exécutez un script (un fichier Python), votre répertoire de travail courant est le répertoire où se trouve actuellement le script.

### Comment changer votre répertoire de travail courant

Vous pouvez changer votre répertoire de travail courant avec cette commande du module `os` :

```python
os.chdir(<path>)
```

Vous devrez spécifier le chemin vers le nouveau répertoire de travail, en le passant comme argument, formaté comme une chaîne de caractères. Il peut s'agir d'un chemin absolu ou d'un chemin relatif.

💡 **Conseil :**

* Un **chemin absolu** spécifie toute la séquence de répertoires que vous devez parcourir pour atteindre votre répertoire cible. Ce chemin commence à partir du répertoire racine de votre système.

Par exemple :

```python
>>> import os
>>> os.chdir(r"C:\Users\estef\Documents\FreeCodeCamp\freeCodeCamp News\9 - listdir vs system")

# Vérification du répertoire de travail courant :
>>> os.getcwd()
'C:\\Users\\estef\\Documents\\FreeCodeCamp\\freeCodeCamp News\\9 - listdir vs system'
```

Remarquez que j'ai ajouté un `r` avant le chemin absolu pour convertir la chaîne en une chaîne brute. Si vous utilisez `\` et que vous n'ajoutez pas le `r`, vous obtiendrez une erreur car le symbole `\` sera traité comme un caractère spécial.

Alternativement, vous pourriez remplacer les barres obliques inverses `\` par des barres obliques `/` dans le chemin :

```python
>>> os.chdir("C:/Users/estef/Documents/FreeCodeCamp/freeCodeCamp News/9 - listdir vs system")

# Vérification du répertoire de travail courant
>>> os.getcwd()
'C:\\Users\\estef\\Documents\\FreeCodeCamp\\freeCodeCamp News\\9 - listdir vs system'
```

* Un **chemin relatif** spécifie le chemin que vous souhaitez suivre pour trouver le répertoire cible, mais maintenant le chemin commence à partir de votre répertoire de travail **courant**. Il est plus court et plus simple que le chemin absolu.

Par exemple, si votre répertoire de travail courant contient un sous-répertoire (dossier) `Répertoire 1`, vous pouvez vous déplacer vers ce répertoire en utilisant un chemin relatif (imaginez-le comme un dossier dans un autre dossier, et nous allons de plus en plus profond dans la hiérarchie), comme ceci :

```python
>>> import os
>>> os.chdir(".\Répertoire 1")

# Vérifier le répertoire de travail courant
>>> os.getcwd()
'C:\\Users\\estef\\Documents\\FreeCodeCamp\\freeCodeCamp News\\9 - listdir vs system\\Répertoire 1'
```

💡 **Conseil :** Le point (`.`) au début du chemin relatif `.\Répertoire 1` représente le répertoire de travail courant. Un double point (`..`) est utilisé pour remonter dans la hiérarchie, vers le répertoire "parent".

Maintenant que vous avez toutes les connaissances de base dont vous aurez besoin pour vraiment comprendre comment `listdir` et `system` fonctionnent, voyons-les en détail.

## 🔸 Listdir

Nous allons commencer par la fonction `listdir`. Révélons ses mystères. ?

### But et valeur de retour

Selon la [Documentation Python](https://docs.python.org/3/library/os.html#os.listdir), le but de cette fonction est de :

> Retourner une liste contenant les noms des entrées dans le répertoire donné par _path_.

En gros, cette fonction retourne une liste avec les noms de tous les fichiers et répertoires qui se trouvent actuellement dans un répertoire particulier que vous spécifiez lorsque vous appelez la fonction.

💡 **Conseil :** La liste n'aura pas d'ordre spécifique, même si vous triez généralement les éléments par ordre alphabétique.

### Syntaxe et paramètre

Pour appeler `listdir`, vous devrez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-9.png)

Le paramètre `path` est précisément cela, le chemin absolu ou relatif vers le répertoire que vous souhaitez visualiser. Dans Python 3.2 et versions ultérieures, ce paramètre est facultatif. Par défaut, le chemin mènera à votre répertoire de travail courant si vous ne passez pas d'argument.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-12.png)

N'oubliez pas que vous devez importer le module `os` avant d'appeler cette fonction.

💡 **Conseil :** Si vous utilisez cette instruction d'import `from os import listdir` pour importer la fonction individuellement, vous pouvez omettre le préfixe `os.`, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-10.png)

### Cas d'utilisation et avantages

La fonction `listdir` est très utile car elle fonctionne sur n'importe quel système d'exploitation où Python s'exécute, donc si Python est installé sur votre appareil, cette fonction fonctionnera correctement.

Maintenant, parlons un peu de sa valeur de retour. Puisqu'elle retourne une liste, nous pouvons stocker cette liste dans une variable et travailler avec elle dans notre programme.

Par exemple, supposons que nous voulons faire quelque chose avec tous les fichiers d'un répertoire donné, comme convertir des images en noir et blanc ou modifier leur contenu. Nous pourrions le faire en utilisant une boucle for, comme ceci :

```python
images = os.listdir(<path>)

for image in images:
	# Faire quelque chose à l'image

```

Bien sûr, vous devrez définir ce qui se passe dans la boucle, mais c'est un exemple de ce que vous pourriez faire avec cette fonction.

C'est génial, n'est-ce pas ?

Mais avoir des fichiers et des répertoires dans la même liste peut être un peu problématique si nous voulons travailler avec une boucle for, n'est-ce pas ? Nous devrions ajouter une condition pour vérifier le type de chaque élément. Comment pouvons-nous faire une liste qui ne contient que des noms de fichiers (pas de répertoires) ou vice versa ?

Voyons cela ! ✨

### Inclure uniquement les fichiers

Si vous voulez "filtrer" la liste retournée par `os.listdir()` pour inclure uniquement les **fichiers** (pas de répertoires), vous pouvez utiliser cette ligne de code :

```python
list(filter(os.path.isfile, os.listdir(<path>)))
```

💡 **Conseil :** Vous pouvez personnaliser l'argument `<path>` ou l'omettre pour utiliser votre répertoire de travail courant.

Voyons un exemple avec mon répertoire de travail courant (j'utilise Windows) :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-23.png)

Mon répertoire (dossier) contient :

* Deux sous-répertoires (dossiers dans le dossier principal)
* Un fichier PowerPoint
* Une image (fichier .png)
* Un script Python

Si j'appelle la fonction `listdir` depuis le fichier `script.py` et que j'imprime la liste retournée :

```python
print(os.listdir())
```

Voici le résultat :

```python
['Diagrams.ppt', 'Directory 1', 'Directory 2', 'listdir vs system.png', 'script.py']
```

Vous pouvez voir que tous les fichiers et répertoires de mon répertoire de travail courant ont été inclus.

Pour filtrer la liste pour qu'elle ne contienne que des fichiers, nous pouvons utiliser cette instruction :

```python
print(list(filter(os.path.isfile, os.listdir())))
```

Maintenant, le résultat est :

```python
['Diagrams.ppt', 'listdir vs system.png', 'script.py']
```

Remarquez comment les répertoires ont été "filtrés", exactement ce que nous voulions.

### Inclure uniquement les répertoires

De même, si vous voulez "filtrer" la liste pour inclure uniquement les **répertoires**, vous pouvez utiliser cette ligne de code :

```python
list(filter(os.path.isdir, os.listdir(<path>)))
```

Maintenant, le résultat est :

```
['Directory 1', 'Directory 2']
```

Exactement ce que nous voulions. Mais comment cette instruction fonctionne-t-elle en coulisses ? Voyons cela.

### Comment `filter()` fonctionne en coulisses

La fonction filter est appelée en utilisant cette syntaxe :

```
filter(<function>, <list>)
```

Elle "filtre" essentiellement les éléments du deuxième argument (la liste) en fonction de la valeur de vérité retournée par l'appel de la fonction passée en tant que premier argument (`os.path.isfile()` ou `os.path.isdir()` dans leurs commandes respectives) :

```python
print(list(filter(os.path.isfile, os.listdir())))
```

```python
list(filter(os.path.isdir, os.listdir()))
```

Ces deux fonctions :

```
os.path.isfile(<path>)

os.path.isdir(<path>)
```

Retournent `True` si l'argument est un fichier ou un répertoire, respectivement.

Sur la base de ces valeurs de vérité, les éléments de la liste seront inclus (ou non) dans la liste finale "filtrée". Les éléments de la liste retournée par `os.listdir()` sont passés un par un à ces fonctions pour vérifier s'ils sont des fichiers (ou des répertoires, respectivement).

Par exemple : Si nous avons cette ligne de code :

```python
filter(os.path.isfile, os.listdir())))
```

Et `os.listdir()` retourne cette liste :

```python
['Diagrams.ppt', 'Directory 1', 'Directory 2', 'script.py']
```

Le premier élément de la liste (`'Diagrams.ppt'`) est passé en argument à `os.path.isfile()` pour vérifier s'il s'agit d'un fichier :

```python
os.path.isfile('Diagrams.ppt') # True
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-30.png)

L'appel de fonction retourne `True`, donc c'est un fichier et il est inclus dans la liste.

Mais si l'élément est un répertoire :

```python
os.path.isfile('Directory 1') # False
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-31.png)

L'appel de fonction retourne `False`, donc il n'est pas inclus dans la liste. Ce processus continue pour chaque élément de la liste jusqu'à ce que la nouvelle liste ne contienne que des noms de fichiers.

Ensuite, puisque `filter()` retourne un itérable, nous créons une liste à partir de cet itérable en utilisant `list()` :

```python
list(filter(os.path.isfile, os.listdir()))
```

Et nous l'imprimons puisque nous travaillons avec un fichier Python (script) :

```python
print(list(filter(os.path.isfile, os.listdir())))
```

💡 **Conseil :** Vous pouvez identifier visuellement si un élément de la liste représente un fichier ou un répertoire en voyant s'il a une extension (type) après son nom. Par exemple : `Diagrams.ppt` a une extension `.ppt` qui vous indique qu'il s'agit d'un fichier PowerPoint, mais un répertoire n'a pas d'extension, comme `'Directory 1'`.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-32.png)

## 🔸 System("ls")

Maintenant que vous savez comment travailler avec `listdir`, voyons comment la fonction `system()` fonctionne en coulisses et comment vous pouvez l'utiliser.

### But

Selon la [Documentation Python](https://docs.python.org/3/library/os.html#os.system), le but de la fonction `system()` est de :

> Exécuter la commande (une chaîne) dans un sous-shell

En gros, cette fonction prend une commande (en tant que chaîne) et l'exécute.

Dans ce cas, la commande que nous passons est `'ls'`, une commande Unix utilisée sous Linux pour afficher le contenu d'un répertoire en tant que sortie standard.

Contrairement à `listdir`, la fonction `system()` **ne retournera pas une liste** si nous passons la commande `'ls'`, elle **affichera** simplement la liste des fichiers et répertoires en tant que sortie standard. Par conséquent, vous devriez l'utiliser si vous voulez simplement visualiser la liste sans réellement travailler avec elle dans votre programme.

### Syntaxe et paramètre

Pour appeler cette fonction, vous devrez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-15.png)

Son seul argument est la commande que vous voulez exécuter, formatée en tant que chaîne (entourée de guillemets doubles ou simples).

En particulier, la commande `ls` vous permet de voir le contenu de votre répertoire de travail courant.

Par exemple : si c'est mon répertoire de travail (trois fichiers Python et un sous-répertoire) :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-17.png)

Et j'appelle la fonction `system()`, comme ceci :

```python
>>> import os
>>> os.system("ls")
```

Voici le résultat :

```python
'Directory 1'  'file 1.py'  'file 2.py'   main.py
0
```

Nous pouvons voir la sortie standard dans la console (la liste des fichiers et répertoires) :

```python
'Directory 1'  'file 1.py'  'file 2.py'   main.py
```

et la valeur de retour :

```python
0
```

💡 **Note :** Pour ces exemples de la fonction `system()`, je travaille avec un outil de ligne de commande en ligne appelé Repl.it puisque mon ordinateur a Windows installé et la commande `ls` n'est pas reconnue par l'invite de commande par défaut.

### Limitations

L'une des principales limitations de cette fonction est que la commande passée en argument doit être reconnue par le système d'exploitation ou l'environnement avec lequel vous travaillez.

Par exemple, la commande `ls` ne sera pas reconnue dans Windows par défaut dans l'invite de commande. Vous verrez cette erreur si vous essayez de l'exécuter :

> 'ls' n'est pas reconnu en tant que commande interne ou externe, programme exécutable ou fichier batch.

Une commande similaire sous Windows serait la commande `'dir'` :

```python
os.system('dir')
```

**💡 Conseil :** Il existe des moyens alternatifs d'exécuter la commande `ls` sur Windows, comme l'utilisation de programmes de terminal qui reconnaissent les commandes Unix, mais par défaut Windows ne reconnaît pas la commande `'ls'`.

### Valeur de retour

Selon la [Documentation Python](https://docs.python.org/3/library/os.html#os.system) :

> Sous Unix, la valeur de retour est le statut de sortie du processus encodé dans le format spécifié pour [`wait()`](https://docs.python.org/3/library/os.html#os.wait).

et...

> Sous Windows, la valeur de retour est celle retournée par le shell système après l'exécution de _command_.

💡 **Conseil :** Notez que cette fonction ne retourne pas une liste. Elle affiche simplement la liste en tant que sortie standard, donc vous ne pouvez pas la stocker dans une variable comme vous l'avez fait avec `listdir`.

### Variations de la commande `ls`

Une caractéristique clé de `os.system('ls')` est qu'elle a de nombreuses options utiles et intéressantes pour personnaliser la présentation de la sortie. Voyons quelques-unes d'entre elles.

**Option 1 :** Nous pouvons afficher plus d'informations sur les fichiers et répertoires, comme leur taille, leur emplacement, et la date et l'heure de modification, en utilisant la commande `ls -l`.

```python
>>> import os
>>> os.system('ls -l')
total 12
drwxr-xr-x 1 runner runner  0 Apr  3 18:23 'Directory 1'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 1.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 2.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38  main.py
0
```

**Option 2 :** Pour pouvoir reconnaître visuellement les répertoires plus rapidement, nous pouvons utiliser `ls -F`, qui ajoute une barre oblique `/` à la fin de leurs noms (voir `'Directory 1/'` ci-dessous).

```python
>>> import os
>>> os.system('ls -F')
'Directory 1'/  'file 1.py'  'file 2.py'   main.py
0
```

**Option 3 :** Pour trier les fichiers par taille, nous pouvons utiliser la commande `ls -lS`.

```python
>>> import os
>>> os.system('ls -lS')
total 12
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 1.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 2.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38  main.py
drwxr-xr-x 1 runner runner  0 Apr  3 18:23 'Directory 1'
0
```

Il existe de nombreuses autres options de personnalisation qui peuvent être utiles pour votre objectif particulier. [Ici, vous pouvez trouver plus d'informations](https://en.wikipedia.org/wiki/Ls) sur la commande `-ls` et comment vous pouvez utiliser son plein pouvoir.

## 🔸 Résumé de listdir vs. system("ls")

* **But :** `listdir` retourne la liste des noms de fichiers et de répertoires dans le chemin spécifié (par défaut, le répertoire de travail courant) tandis que `system("ls")` les affiche simplement en tant que sortie standard.
* **Système d'exploitation :** `listdir` peut être utilisé indépendamment du système d'exploitation avec lequel vous travaillez. En revanche, `system('ls')` doit être exécuté dans un système d'exploitation ou un environnement qui reconnaît la commande `'ls'`.
* **Personnalisation :** vous pouvez filtrer la liste retournée par `listdir` si vous devez supprimer des fichiers ou des répertoires en utilisant la fonction `filter()` et vous pouvez passer des options pour personnaliser la sortie de `system('ls')`.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous pouvez travailler avec ces fonctions dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐️