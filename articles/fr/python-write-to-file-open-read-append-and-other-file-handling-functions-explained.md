---
title: Écrire dans un fichier en Python – Les fonctions open, read, append et autres
  manipulations de fichiers expliquées
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-05-07T15:29:54.000Z'
originalURL: https://freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Python-File-Handling-1.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: Écrire dans un fichier en Python – Les fonctions open, read, append et
  autres manipulations de fichiers expliquées
seo_desc: "Welcome\nHi! If you want to learn how to work with files in Python, then\
  \ this article is for you. Working with files is an important skill that every Python\
  \ developer should learn, so let's get started.\nIn this article, you will learn:\
  \ \n\nHow to open a..."
---

## Bienvenue

Bonjour ! Si vous voulez apprendre à manipuler des fichiers en Python, cet article est fait pour vous. La manipulation de fichiers est une compétence importante que tout développeur Python devrait acquérir, alors commençons.

**Dans cet article, vous apprendrez :** 

* Comment ouvrir un fichier.
* Comment lire un fichier.
* Comment créer un fichier.
* Comment modifier un fichier.
* Comment fermer un fichier.
* Comment ouvrir des fichiers pour plusieurs opérations. 
* Comment travailler avec les méthodes des objets fichiers.
* Comment supprimer des fichiers.
* Comment travailler avec les gestionnaires de contexte (context managers) et pourquoi ils sont utiles.
* Comment gérer les exceptions qui pourraient être levées lors de la manipulation de fichiers.
* et bien plus encore !

**Commençons ! ✨**

## 🔹 Travailler avec des fichiers : Syntaxe de base

L'une des fonctions les plus importantes que vous devrez utiliser pour manipuler des fichiers en Python est `**open()**`**,** une fonction intégrée qui ouvre un fichier et permet à votre programme de l'utiliser et de travailler avec.

**Voici la syntaxe de base** :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-48.png)

💡 **Conseil :** Ce sont les deux arguments les plus couramment utilisés pour appeler cette fonction. Il existe six arguments optionnels supplémentaires. Pour en savoir plus, veuillez lire [cet article](https://docs.python.org/3/library/functions.html#open) dans la documentation.

### Premier paramètre : File (Fichier)

Le premier paramètre de la fonction `open()` est `**file**`, le chemin absolu ou relatif vers le fichier avec lequel vous essayez de travailler. 

Nous utilisons généralement un chemin relatif, qui indique où se trouve le fichier par rapport à l'emplacement du script (fichier Python) qui appelle la fonction `open()`. 

Par exemple, le chemin dans cet appel de fonction :

```python
open("names.txt") # Le chemin relatif est "names.txt"
```

Ne contient que le nom du fichier. Cela peut être utilisé lorsque le fichier que vous essayez d'ouvrir se trouve dans le même répertoire ou dossier que le script Python, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-7.png)

Mais si le fichier se trouve dans un dossier imbriqué, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-9.png)
_Le fichier names.txt est dans le dossier "data"_

Ensuite, nous devons utiliser un chemin spécifique pour dire à la fonction que le fichier se trouve dans un autre dossier. 

Dans cet exemple, voici quel serait le chemin :

```python
open("data/names.txt")
```

Remarquez que nous écrivons d'abord `data/` (le nom du dossier suivi d'un `/`) puis `names.txt` (le nom du fichier avec son extension).

💡 **Conseil :** Les trois lettres `.txt` qui suivent le point dans `names.txt` constituent l'"extension" du fichier, ou son type. Dans ce cas, `.txt` indique qu'il s'agit d'un fichier texte.

### Second paramètre : Mode

Le second paramètre de la fonction `open()` est le `**mode**`, une chaîne de caractères contenant un seul caractère. Ce caractère indique essentiellement à Python ce que vous prévoyez de faire avec le fichier dans votre programme.

Les modes disponibles sont :

* Lecture (`"r"`) 
* Ajout (`"a"` pour Append)
* Écriture (`"w"` pour Write)
* Création (`"x"`) 

Vous pouvez également choisir d'ouvrir le fichier en :

* Mode texte (`"t"`)
* Mode binaire (`"b"`)

Pour utiliser le mode texte ou binaire, vous devrez ajouter ces caractères au mode principal. Par exemple : `"wb"` signifie écrire en mode binaire.

💡 **Conseil :** Les modes par défaut sont lecture (`"r"`) et texte (`"t"`), ce qui signifie "ouvrir pour lire du texte" (`"rt"`). Vous n'avez donc pas besoin de les spécifier dans **`open()`** si vous souhaitez les utiliser car ils sont assignés par défaut. Vous pouvez simplement écrire `open(<file>)`.

**Pourquoi des modes ?**

Il est logique que Python n'accorde que certaines permissions en fonction de ce que vous prévoyez de faire avec le fichier, n'est-ce pas ? Pourquoi Python devrait-il permettre à votre programme d'en faire plus que nécessaire ? C'est essentiellement pour cela que les modes existent.

Réfléchissez-y — permettre à un programme d'en faire plus que nécessaire peut être problématique. Par exemple, si vous avez seulement besoin de lire le contenu d'un fichier, il peut être dangereux de permettre à votre programme de le modifier de manière inattendue, ce qui pourrait potentiellement introduire des bugs.

## 🔸 Comment lire un fichier

Maintenant que vous en savez plus sur les arguments de la fonction `**open()**`, voyons comment vous pouvez ouvrir un fichier et le stocker dans une variable pour l'utiliser dans votre programme.

Voici la syntaxe de base :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-41.png)

Nous assignons simplement la valeur retournée à une variable. Par exemple :

```python
names_file = open("data/names.txt", "r")
```

Je sais ce que vous vous demandez sûrement : quel type de valeur est retourné par `**open()**` ? 

Eh bien, **un** **objet fichier** (file object). 

Parlons-en un peu.

### Objets fichiers

Selon la [Documentation Python](https://docs.python.org/3/glossary.html#term-file-object), un **objet fichier** est :

> Un objet exposant une API orientée fichier (avec des méthodes telles que read() ou write()) vers une ressource sous-jacente.

Cela nous indique essentiellement qu'un objet fichier est un objet qui nous permet de travailler et d'interagir avec des fichiers existants dans notre programme Python. 

Les objets fichiers ont des attributs, tels que :

* **name** : le nom du fichier.
* **closed** : `True` si le fichier est fermé. `False` sinon.
* **mode** : le mode utilisé pour ouvrir le fichier.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-57.png)

Par exemple :

```python
f = open("data/names.txt", "a")
print(f.mode) # Sortie : "a"
```

Voyons maintenant comment vous pouvez accéder au contenu d'un fichier via un objet fichier.

### Méthodes pour lire un fichier

Pour que nous puissions travailler avec des objets fichiers, nous devons avoir un moyen d'"interagir" avec eux dans notre programme, et c'est exactement ce que font les méthodes. Voyons-en quelques-unes. 

### **Read()**

La première méthode que vous devez apprendre est **`read()`**, qui **renvoie l'intégralité du contenu du fichier sous forme de chaîne de caractères.**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-11.png)

Voici un exemple :

```python
f = open("data/names.txt")
print(f.read())
```

La sortie est :

```python
Nora
Gino
Timmy
William
```

Vous pouvez utiliser la fonction `type()` pour confirmer que la valeur renvoyée par `f.read()` est une chaîne de caractères :

```python
print(type(f.read()))

# Sortie
<class 'str'>
```

Oui, c'est bien une chaîne de caractères !

Dans ce cas, tout le fichier a été imprimé car nous n'avons pas spécifié de nombre maximum d'octets, mais nous pouvons aussi le faire. 

Voici un exemple :

```python
f = open("data/names.txt")
print(f.read(3))
```

La valeur renvoyée est limitée à ce nombre d'octets :

```
Nor
```

❗**Important :** Vous devez **fermer** un fichier une fois la tâche terminée pour libérer les ressources associées au fichier. Pour ce faire, vous devez appeler la méthode **`close()`**, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-22.png)

### Readline() vs Readlines()

Vous pouvez lire un fichier ligne par ligne avec ces deux méthodes. Elles sont légèrement différentes, alors voyons-les en détail.

`**readline()**` lit **une ligne** du fichier jusqu'à ce qu'elle atteigne la fin de cette ligne. Un caractère de saut de ligne final (`\n`) est conservé dans la chaîne. 

💡 **Conseil :** En option, vous pouvez passer la taille, c'est-à-dire le nombre maximum de caractères que vous souhaitez inclure dans la chaîne résultante.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-19.png)

Par exemple :

```python
f = open("data/names.txt")
print(f.readline())
f.close()
```

La sortie est :

```python
Nora

```

C'est la première ligne du fichier.

En revanche, `**readlines()**` renvoie une **liste contenant toutes les lignes** du fichier sous forme d'éléments individuels (chaînes de caractères). Voici la syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-21.png)

Par exemple :

```python
f = open("data/names.txt")
print(f.readlines())
f.close()
```

La sortie est :

```python
['Nora\n', 'Gino\n', 'Timmy\n', 'William']
```

Remarquez qu'il y a un `\n` (caractère de saut de ligne) à la fin de chaque chaîne, sauf la dernière.

💡 **Conseil :** Vous pouvez obtenir la même liste avec `list(f)`.

Vous pouvez travailler avec cette liste dans votre programme en l'assignant à une variable ou en l'utilisant dans une boucle :

```python
f = open("data/names.txt")

for line in f.readlines():
    # Faire quelque chose avec chaque ligne
    
f.close()
```

Nous pouvons également itérer directement sur `f` (l'objet fichier) dans une boucle :

```python
f = open("data/names.txt", "r")

for line in f:
	# Faire quelque chose avec chaque ligne

f.close()
```

Ce sont les principales méthodes utilisées pour lire des objets fichiers. Voyons maintenant comment vous pouvez créer des fichiers.

## 🔹 Comment créer un fichier

Si vous avez besoin de créer un fichier "dynamiquement" en utilisant Python, vous pouvez le faire avec le mode `"x"`. 

Voyons comment. Voici la syntaxe de base :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-58.png)

Voici un exemple. Voici mon répertoire de travail actuel :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-29.png)

Si j'exécute cette ligne de code :

```python
f = open("new_file.txt", "x")
```

Un nouveau fichier avec ce nom est créé :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-30.png)

Avec ce mode, vous pouvez créer un fichier puis y écrire dynamiquement en utilisant des méthodes que vous apprendrez dans quelques instants.

💡 **Conseil :** Le fichier sera initialement vide jusqu'à ce que vous le modifiiez.

Une chose curieuse est que si vous essayez d'exécuter à nouveau cette ligne et qu'un fichier portant ce nom existe déjà, vous verrez cette erreur :

```python
Traceback (most recent call last):
  File "<path>", line 8, in <module>
    f = open("new_file.txt", "x")
FileExistsError: [Errno 17] File exists: 'new_file.txt'
```

Selon la [Documentation Python](https://docs.python.org/3/library/exceptions.html#FileExistsError), cette exception (erreur d'exécution) est :

> Levée lors d'une tentative de création d'un fichier ou d'un répertoire qui existe déjà.

Maintenant que vous savez comment créer un fichier, voyons comment vous pouvez le modifier.

## 🔸 Comment modifier un fichier

Pour modifier (écrire dans) un fichier, vous devez utiliser la méthode `**write()**`. Vous avez deux façons de le faire (ajouter ou écraser) selon le mode que vous choisissez pour l'ouvrir. Voyons-les en détail.

### Ajouter (Append)

"Ajouter" signifie mettre quelque chose à la fin d'une autre chose. Le mode `"a"` vous permet d'ouvrir un fichier pour y ajouter du contenu.

Par exemple, si nous avons ce fichier :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-43.png)

Et que nous voulons y ajouter une nouvelle ligne, nous pouvons l'ouvrir en utilisant le mode `**"a"**` (append) puis appeler la méthode `**write()**`, en passant le contenu que nous voulons ajouter comme argument. 

Voici la syntaxe de base pour appeler la méthode `**write()**` :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-52.png)

Voici un exemple :

```python
f = open("data/names.txt", "a")
f.write("\nNew Line")
f.close()
```

💡 **Conseil :** Remarquez que j'ajoute `\n` avant la ligne pour indiquer que je veux que la nouvelle ligne apparaisse comme une ligne séparée, et non comme une continuation de la ligne existante.

Voici le fichier maintenant, après l'exécution du script :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-45.png)

**💡 Conseil :** La nouvelle ligne peut ne pas s'afficher dans le fichier tant que `**f.close()**` n'a pas été exécuté.

### Écrire (Write)

Parfois, vous pouvez vouloir supprimer le contenu d'un fichier et le remplacer entièrement par un nouveau contenu. Vous pouvez le faire avec la méthode `**write()**` si vous ouvrez le fichier avec le mode `**"w"**`.

Prenons ce fichier texte :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-43.png)

Si j'exécute ce script :

```python
f = open("data/names.txt", "w")
f.write("New Content")
f.close()

```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-46.png)

Comme vous pouvez le voir, ouvrir un fichier avec le mode `**"w"**` puis y écrire remplace le contenu existant.

💡 **Conseil :** La méthode **`write()`** renvoie le nombre de caractères écrits.

Si vous souhaitez écrire plusieurs lignes à la fois, vous pouvez utiliser la méthode `**writelines()**`, qui prend une liste de chaînes de caractères. Chaque chaîne représente une ligne à ajouter au fichier.

Voici un exemple. Voici le fichier initial :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-43.png)

Si nous exécutons ce script :

```python
f = open("data/names.txt", "a")
f.writelines(["\nline1", "\nline2", "\nline3"])
f.close()
```

Les lignes sont ajoutées à la fin du fichier :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-47.png)

### Ouvrir un fichier pour plusieurs opérations

Maintenant vous savez comment créer, lire et écrire dans un fichier, mais que se passe-t-il si vous voulez faire plus d'une chose dans le même programme ? Voyons ce qui se passe si nous essayons de faire cela avec les modes que vous avez appris jusqu'à présent :

Si vous ouvrez un fichier en mode `"r"` (lecture), puis essayez d'y écrire :

```python
f = open("data/names.txt")
f.write("New Content") # Tentative d'écriture
f.close()
```

Vous obtiendrez cette erreur :

```python
Traceback (most recent call last):
  File "<path>", line 9, in <module>
    f.write("New Content")
io.UnsupportedOperation: not writable
```

De même, si vous ouvrez un fichier en mode `"w"` (écriture), puis essayez de le lire :

```python
f = open("data/names.txt", "w")
print(f.readlines()) # Tentative de lecture
f.write("New Content")
f.close()
```

You will see this error:

```python
Traceback (most recent call last):
  File "<path>", line 14, in <module>
    print(f.readlines())
io.UnsupportedOperation: not readable
```

La même chose se produira avec le mode `"a"` (ajout).

Comment pouvons-nous résoudre cela ? Pour pouvoir lire un fichier et effectuer une autre opération dans le même programme, vous devez ajouter le symbole `"+"` au mode, comme ceci :

```python
f = open("data/names.txt", "w+") # Lecture + Écriture
```

```python
f = open("data/names.txt", "a+") # Lecture + Ajout
```

```python
f = open("data/names.txt", "r+") # Lecture + Écriture
```

Très utile, n'est-ce pas ? C'est probablement ce que vous utiliserez dans vos programmes, mais assurez-vous de n'inclure que les modes dont vous avez besoin pour éviter les bugs potentiels.

Parfois, les fichiers ne sont plus nécessaires. Voyons comment vous pouvez supprimer des fichiers en utilisant Python.

## 🔹 Comment supprimer des fichiers

Pour supprimer un fichier en utilisant Python, vous devez importer un module appelé `**os**` qui contient des fonctions interagissant avec votre système d'exploitation. 

**💡 Conseil :** Un **module** est un fichier Python contenant des variables, des fonctions et des classes liées entre elles. 

Plus précisément, vous avez besoin de la fonction `**remove()**`. Cette fonction prend le chemin du fichier comme argument et supprime le fichier automatiquement. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-56.png)

Voyons un exemple. Nous voulons supprimer le fichier nommé `sample_file.txt`. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-34.png)

Pour ce faire, nous écrivons ce code :

```python
import os
os.remove("sample_file.txt")
```

* La première ligne : `import os` est appelée une "instruction d'importation". Cette instruction est écrite en haut de votre fichier et vous donne accès aux fonctions définies dans le module `os`. 
* La deuxième ligne : `os.remove("sample_file.txt")` supprime le fichier spécifié. 

💡 **Conseil :** vous pouvez utiliser un chemin absolu ou relatif. 

Maintenant que vous savez comment supprimer des fichiers, voyons un outil intéressant... les gestionnaires de contexte !

## 🔸 Découvrez les gestionnaires de contexte

Les gestionnaires de contexte (Context Managers) sont des structures Python qui vous faciliteront grandement la vie. En les utilisant, vous n'avez pas besoin de vous rappeler de fermer un fichier à la fin de votre programme et vous avez accès au fichier dans la partie spécifique du programme que vous choisissez. 

### Syntaxe

Voici un exemple de gestionnaire de contexte utilisé pour travailler avec des fichiers :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-33.png)

💡 **Conseil :** Le corps du gestionnaire de contexte doit être indenté, tout comme nous indentons les boucles, les fonctions et les classes. Si le code n'est pas indenté, il ne sera pas considéré comme faisant partie du gestionnaire de contexte.

Lorsque le corps du gestionnaire de contexte est terminé, le fichier se ferme automatiquement.

```python
with open("<path>", "<mode>") as <var>:
    # Travail avec le fichier...

# Le fichier est fermé ici !
```

### Exemple

Voici un exemple :

```python
with open("data/names.txt", "r+") as f:
    print(f.readlines()) 
```

Ce gestionnaire de contexte ouvre le fichier `names.txt` pour des opérations de lecture/écriture et assigne cet objet fichier à la variable `f`. Cette variable est utilisée dans le corps du gestionnaire de contexte pour se référer à l'objet fichier.

### Tentative de lecture à nouveau

Une fois le corps terminé, le fichier est automatiquement fermé, il ne peut donc pas être lu sans être ouvert à nouveau. Mais attendez ! Nous avons une ligne qui tente de le lire à nouveau, juste ici en dessous :

```python
with open("data/names.txt", "r+") as f:
    print(f.readlines())

print(f.readlines()) # Tentative de lecture du fichier à nouveau, en dehors du gestionnaire de contexte
```

Voyons ce qui se passe :

```python
Traceback (most recent call last):
  File "<path>", line 21, in <module>
    print(f.readlines())
ValueError: I/O operation on closed file.
```

Cette erreur est déclenchée parce que nous essayons de lire un fichier fermé. Génial, non ? Le gestionnaire de contexte fait tout le travail difficile pour nous, il est lisible et concis. 

## 🔹 Comment gérer les exceptions lors de la manipulation de fichiers

Lorsque vous travaillez avec des fichiers, des erreurs peuvent survenir. Parfois, vous n'avez pas les permissions nécessaires pour modifier ou accéder à un fichier, ou un fichier peut même ne pas exister. 

En tant que programmeur, vous devez prévoir ces circonstances et les gérer dans votre programme pour éviter les plantages soudains qui pourraient affecter l'expérience utilisateur.

Voyons quelques-unes des exceptions (erreurs d'exécution) les plus courantes que vous pourriez rencontrer en travaillant avec des fichiers :

### FileNotFoundError

Selon la [Documentation Python](https://docs.python.org/3/library/exceptions.html#FileNotFoundError), cette exception est :

> Levée lorsqu'un fichier ou un répertoire est demandé mais n'existe pas.

Par exemple, si le fichier que vous essayez d'ouvrir n'existe pas dans votre répertoire de travail actuel :

```python
f = open("names.txt")
```

Vous verrez cette erreur :

```python
Traceback (most recent call last):
  File "<path>", line 8, in <module>
    f = open("names.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'names.txt'
```

Décomposons cette erreur ligne par ligne :

* `File "<path>", line 8, in <module>`. Cette ligne vous indique que l'erreur a été levée lors de l'exécution du code du fichier situé dans `<path>`. Plus précisément, lorsque la `ligne 8` a été exécutée dans `<module>`.
* `f = open("names.txt")`. C'est la ligne qui a causé l'erreur. 
* `FileNotFoundError: [Errno 2] No such file or directory: 'names.txt'` . Cette ligne indique qu'une exception `FileNotFoundError` a été levée car le fichier ou répertoire `names.txt` n'existe pas.

💡 **Conseil :** Python est très descriptif avec les messages d'erreur, n'est-ce pas ? C'est un avantage énorme lors du processus de débogage. 

### PermissionError

C'est une autre exception courante lors de la manipulation de fichiers. Selon la [Documentation Python](https://docs.python.org/3/library/exceptions.html#PermissionError), cette exception est :

> Levée lors d'une tentative d'exécution d'une opération sans les droits d'accès adéquats - par exemple les permissions du système de fichiers.

Cette exception est levée lorsque vous essayez de lire ou de modifier un fichier auquel vous n'avez pas l'autorisation d'accéder. Si vous essayez de le faire, vous verrez cette erreur :

```python
Traceback (most recent call last):
  File "<path>", line 8, in <module>
    f = open("<file_path>")
PermissionError: [Errno 13] Permission denied: 'data'
```

### IsADirectoryError

Selon la [Documentation Python](https://docs.python.org/3/library/exceptions.html#IsADirectoryError), cette exception est :

> Levée lorsqu'une opération sur un fichier est demandée sur un répertoire.

Cette exception particulière est levée lorsque vous essayez d'ouvrir ou de travailler sur un répertoire au lieu d'un fichier, soyez donc très prudent avec le chemin que vous passez en argument.

### Comment gérer les exceptions

Pour gérer ces exceptions, vous pouvez utiliser une instruction **try/except**. Avec cette instruction, vous pouvez "dire" à votre programme quoi faire au cas où quelque chose d'inattendu se produirait.

Voici la syntaxe de base :

```
try:
	# Essayer d'exécuter ce code
except <type_of_exception>:
	# Si une exception de ce type est levée, arrêter le processus et sauter à ce bloc
    
```

Ici, vous pouvez voir un exemple avec `FileNotFoundError` :

```python
try:
    f = open("names.txt")
except FileNotFoundError:
    print("Le fichier n'existe pas")
```

Cela dit essentiellement :

* Essaye d'ouvrir le fichier `names.txt`.
* Si une `FileNotFoundError` est lancée, ne plante pas ! Affiche simplement un message descriptif pour l'utilisateur. 

💡 **Conseil :** Vous pouvez choisir comment gérer la situation en écrivant le code approprié dans le bloc `except`. Vous pourriez par exemple créer un nouveau fichier s'il n'existe pas déjà.

Pour fermer le fichier automatiquement après la tâche (qu'une exception ait été levée ou non dans le bloc `try`), vous pouvez ajouter le bloc `finally`. 

```
try:
	# Essayer d'exécuter ce code
except <exception>:
	# Si cette exception est levée, arrêter le processus immédiatement et sauter à ce bloc
finally: 
	# Faire ceci après l'exécution du code, même si une exception a été levée
```

Voici un exemple :

```python
try:
    f = open("names.txt")
except FileNotFoundError:
    print("Le fichier n'existe pas")
finally:
    f.close()
```

Il existe de nombreuses façons de personnaliser l'instruction try/except/finally et vous pouvez même ajouter un bloc `else` pour exécuter un bloc de code uniquement si aucune exception n'a été levée dans le bloc `try`. 

**💡 Conseil :** Pour en savoir plus sur la gestion des exceptions en Python, vous aimerez peut-être lire mon article : ["Comment gérer les exceptions en Python : Une introduction visuelle détaillée"](https://www.freecodecamp.org/news/exception-handling-python/). 

## 🔸 En résumé

* Vous pouvez créer, lire, écrire et supprimer des fichiers en utilisant Python. 
* Les objets fichiers possèdent leur propre ensemble de méthodes que vous pouvez utiliser pour travailler avec eux dans votre programme.
* Les gestionnaires de contexte vous aident à travailler avec les fichiers et à les gérer en les fermant automatiquement lorsqu'une tâche est terminée.
* La gestion des exceptions est essentielle en Python. Les exceptions courantes lors de la manipulation de fichiers incluent `FileNotFoundError`, `PermissionError` et `IsADirectoryError`. Elles peuvent être gérées à l'aide de try/except/else/finally.

**J'espère vraiment que vous avez aimé mon article et qu'il vous a été utile.** Vous pouvez désormais manipuler des fichiers dans vos projets Python. [Consultez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐️