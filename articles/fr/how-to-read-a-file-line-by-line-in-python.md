---
title: Comment lire un fichier ligne par ligne en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-12-14T17:58:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-mateusz-dach-450035.jpg
tags:
- name: Python
  slug: python
seo_title: Comment lire un fichier ligne par ligne en Python
seo_desc: "When coding in Python, there may be times when you need to open and read\
  \ the contents of a text file.\nLuckily enough, there are several ways to do this\
  \ in Python. \nThe language has many built-in functions, methods, and keywords that\
  \ you can use to cr..."
---

Lorsque vous codez en Python, il peut arriver que vous deviez ouvrir et lire le contenu d'un fichier texte.

Heureusement, il existe plusieurs façons de le faire en Python.

Le langage dispose de nombreuses fonctions, méthodes et mots-clés intégrés que vous pouvez utiliser pour créer, écrire, lire et supprimer des fichiers texte.

Dans cet article, vous apprendrez les méthodes les plus courantes pour lire un fichier. À l'aide d'exemples de code, vous saurez comment lire un fichier texte ligne par ligne.

Voici ce que nous allons couvrir :

1. [Comment ouvrir un fichier texte en utilisant la fonction `open()`](#open-function)
2. [Comment lire un fichier texte en utilisant la méthode `read()`](#read-method)
3. [Comment lire un fichier texte en utilisant la méthode `readline()`](#readline-method)
4. [Comment lire un fichier texte en utilisant la méthode `readlines()`](#readlines-method)
5. [Comment lire un fichier texte en utilisant une boucle `for`](#for-loop)

Commençons !

## Comment ouvrir un fichier texte en utilisant la fonction `open()` en Python <a name="open-function"></a>

Avant de commencer à lire un fichier texte en Python, vous devez d'abord l'ouvrir.

Pour ouvrir un fichier texte, utilisez la fonction intégrée `open()`.

La syntaxe générale de la fonction `open()` ressemble à ceci :

```python
open("nom_du_fichier", "mode")
```

La fonction `open()` accepte plusieurs arguments, mais dans cet exemple, je me concentre uniquement sur deux : `nom_du_fichier` et `mode`.

Analysons la syntaxe.

Le premier argument requis que la fonction `open()` accepte est `nom_du_fichier`, qui représente le chemin complet du nom du fichier que vous souhaitez ouvrir.

Lorsque vous spécifiez le chemin du fichier que vous souhaitez ouvrir, vous devez savoir où ce fichier se trouve dans votre structure de dossiers.

Par exemple, si le fichier texte que vous souhaitez ouvrir et votre fichier actuel avec le code Python se trouvent dans le même dossier, vous n'avez besoin de référencer que son nom et son extension.

Supposons que vous avez un dossier nommé `projects`.

À l'intérieur, vous avez deux fichiers, `main.py`, qui est le fichier où vous écrivez votre code Python, et `example.txt`, qui est le fichier que vous souhaitez ouvrir. Ce fichier contient le contenu suivant :

```
J'adore absolument coder !
J'apprends à coder gratuitement avec freeCodeCamp !
```

Les deux fichiers sont au même niveau dans le dossier, donc voici comment vous référenceriez `example.txt` lors de l'utilisation de la fonction `open()` :

```python
open("example.txt")
```

Le deuxième argument optionnel que la fonction `open()` accepte est `mode`. Il spécifie si vous souhaitez lire (`"r"`), écrire (`"w"`) ou ajouter (`"a"`) à `nom_du_fichier`.

Le mode par défaut est le mode lecture (`"r"`).

Ainsi, pour ouvrir et lire `example.txt`, vous pourriez optionnellement utiliser `"r"` pour représenter le mode que vous souhaitez utiliser :

```python
open("example.txt", mode="r")
```

Cela dit, vous n'avez pas besoin d'écrire le mot-clé `mode`.

Au lieu de cela, vous pouvez l'omettre et n'utiliser que la lettre `"r"` - cela aurait toujours le même résultat :

```python
open("example.txt","r")
```

Enfin, vous pouvez omettre complètement la lettre `"r"` car c'est le mode par défaut :

```python
open("example.txt")
```

Lorsque vous exécutez le code de l'exemple ci-dessus, il ne se passe rien.

Vous avez terminé la première étape, qui consiste à ouvrir le fichier texte, mais vous ne l'avez pas encore lu et vu son contenu.

## Comment lire un fichier texte en utilisant la méthode `read()` en Python <a name="read-method"></a>

Pour lire le contenu de `example.txt`, commençons par stocker le code que nous avons écrit dans la section précédente dans une variable nommée `fichier` :

```python
fichier = open("example.txt")
```

Ensuite, appelons la méthode `read()` sur `fichier` et affichons le résultat dans la console :

```python
fichier = open("example.txt")

print(fichier.read())

# sortie

# J'adore absolument coder !
# J'apprends à coder gratuitement avec freeCodeCamp !
```

Maintenant, vous pouvez lire le contenu de `example.txt` !

La méthode `read()` lit tout le contenu sous forme de chaîne unique, ce qui est utile lorsque vous travaillez avec des fichiers plus petits qui n'ont pas beaucoup de contenu dans le fichier texte.

Cela dit, le code ci-dessus manque quelque chose.

Une fois que vous avez terminé de lire le fichier texte, vous devez le fermer. Pour cela, utilisez la méthode `close()`. Assurez-vous de ne pas sauter cette étape car oublier de fermer le fichier peut introduire des bugs dans votre code !

```python
fichier = open("example.txt")

print(fichier.read())

# fermer le fichier
fichier.close()
```

Maintenant, fermer le fichier texte est une bonne pratique, mais c'est quelque chose que vous pouvez facilement oublier de faire - vous ne vous souviendrez pas toujours d'appeler la méthode `close()` sur le fichier.

Il existe une alternative disponible.

Le mot-clé `with` garantit que le fichier est automatiquement fermé lors de l'exécution du code.

La syntaxe générale du mot-clé `with` lorsqu'il est utilisé avec la fonction `open()` est la suivante :

```python
with open("nom_du_fichier") as variable:
    # faire quelque chose avec la variable
```

Voici donc comment vous réécririez le code de l'exemple précédent en utilisant le mot-clé `with` au lieu de la méthode `close()` :

```python
with open("example.txt") as fichier:
  print(fichier.read())
  
# sortie

# J'adore absolument coder !
# J'apprends à coder gratuitement avec freeCodeCamp !
```

## Comment lire un fichier texte en utilisant la méthode `readline()` en Python <a name="readline-method"></a>

Si vous souhaitez lire une seule ligne individuelle d'un fichier texte, utilisez la méthode `readline()` :

```python
with open("example.txt") as fichier:
  print(fichier.readline())
  
# sortie

# J'adore absolument coder !
```

Le fichier texte `example.txt` contient deux lignes, mais la méthode `readline()` ne lit qu'une seule ligne du fichier et la retourne.

La méthode `readline()` ajoute également un caractère de nouvelle ligne à la fin de la chaîne.

Vous pouvez optionnellement passer un argument `size` à la méthode `readline()`, qui spécifie la longueur de la ligne retournée et le nombre maximum d'octets qu'elle lira.

```python
with open("example.txt") as fichier:
  print(fichier.readline(10))

# sortie

# J'absolue
```

## Comment lire un fichier texte en utilisant la méthode `readlines()` en Python <a name="readlines-method"></a>

La méthode `readlines()` lit toutes les lignes d'un fichier, en parcourant le fichier ligne par ligne.

Elle retourne ensuite une liste de chaînes :

```python
with open("example.txt") as fichier:
  print(fichier.readlines())
  
# sortie

# ['J'adore absolument coder !\n', "J'apprends à coder gratuitement avec freeCodeCamp !"]
```

La méthode `readlines()` a lu toutes les lignes en une seule fois et a stocké chaque ligne du fichier texte en tant qu'élément unique de la liste. La méthode `readlines()` a également ajouté un caractère de nouvelle ligne `\n` à la fin de chaque ligne.

## Comment lire un fichier texte en utilisant une boucle `for` en Python <a name="for-loop"></a>

Une autre façon de lire un fichier ligne par ligne en Python est d'utiliser une boucle `for`, qui est l'approche la plus Pythonique pour lire un fichier :

```python
with open("example.txt") as fichier:
  for element in fichier:
    print(element)
    
# sortie

# J'adore absolument coder !

# J'apprends à coder gratuitement avec freeCodeCamp !
```

La fonction `open()` retourne un objet itérable.

La boucle `for` est associée au mot-clé `in` - ils itèrent sur l'objet fichier itérable retourné et lisent chaque ligne à l'intérieur.

## Conclusion

Espérons que cet article vous a aidé à comprendre comment lire un fichier ligne par ligne en Python en utilisant les méthodes `read()`, `readline()` et `readlines()` ainsi qu'une boucle `for`.

Merci d'avoir lu, et bon codage !