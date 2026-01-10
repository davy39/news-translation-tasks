---
title: Manuel d'exemples de code Python – Tutoriel de codage de scripts d'exemple
  pour débutants
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2021-04-27T19:55:23.000Z'
originalURL: https://freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Python-Code-Examples-Mockup.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: handbook
  slug: handbook
- name: Python
  slug: python
seo_title: Manuel d'exemples de code Python – Tutoriel de codage de scripts d'exemple
  pour débutants
seo_desc: "Hi! Welcome. If you are learning Python, then this article is for you.\
  \ You will find a thorough description of Python syntax and lots of code examples\
  \ to guide you during your coding journey. \nWhat we will cover:\n\nVariable Definitions\
  \ in Python\nHello..."
---

Salut ! Bienvenue. Si vous apprenez Python, alors cet article est pour vous. Vous y trouverez une description approfondie de la syntaxe Python et de nombreux exemples de code pour vous guider tout au long de votre parcours de programmation.

### Ce que nous allons couvrir :

* [Définitions de variables en Python](#heading-definitions-de-variables-en-python)
* [Programme Hello, World ! en Python](#heading-programme-hello-world-en-python)
* [Types de données et structures de données intégrées en Python](#heading-types-de-donnees-et-structures-de-donnees-integrees-en-python)
* [Opérateurs Python](#heading-operateurs-python)
* [Conditionnels en Python](#heading-conditionnels-en-python)
* [Boucles For en Python](#heading-boucles-for-en-python)
* [Boucles While en Python](#heading-boucles-while-en-python)
* [Boucles imbriquées en Python](#heading-boucles-imbriquees-en-python)
* [Fonctions en Python](#heading-fonctions-en-python)
* [Récursion en Python](#heading-recursion-en-python)
* [Gestion des exceptions en Python](#heading-gestion-des-exceptions-en-python)
* [Programmation Orientée Objet en Python](#heading-programmation-orientee-objet-en-python)
* [Comment travailler avec des fichiers en Python](#heading-comment-travailler-avec-des-fichiers-en-python)
* [Instructions d'importation en Python](#heading-instructions-dimportation-en-python)
* [Compréhension de listes et de dictionnaires en Python](#heading-comprehension-de-listes-et-de-dictionnaires-en-python)
* et plus encore...

Êtes-vous prêt ? Commençons ! 💡

💡 **Conseil :** tout au long de cet article, j'utiliserai `<>` pour indiquer que cette partie de la syntaxe sera remplacée par l'élément décrit par le texte. Par exemple, `<var>` signifie que cela sera remplacé par une variable lorsque nous écrirons le code.

## 🔹 Définitions de variables en Python

Le bloc de construction le plus basique de tout langage de programmation est le concept de variable, un nom et un emplacement en mémoire que nous réservons pour une valeur.

En Python, nous utilisons cette syntaxe pour créer une variable et lui assigner une valeur :

```python
<nom_variable> = <valeur>
```

Par exemple :

```
age = 56
```

```
name = "Nora"
```

```
color = "Bleu"
```

```
grades = [67, 100, 87, 56]
```

Si le nom d'une variable comporte plus d'un mot, le [Guide de style pour le code Python](https://www.python.org/dev/peps/pep-0008/) recommande de séparer les mots par un tiret bas (underscore) "selon les besoins pour améliorer la lisibilité."

Par exemple :

```
ma_liste = [1, 2, 3, 4, 5]
```

💡 **Conseil :** Le Guide de style pour le code Python (PEP 8) contient d'excellentes suggestions que vous devriez suivre pour écrire un code Python propre.

#### Voici un scrim interactif pour vous aider à comprendre les définitions de variables en Python :

<iframe src="https://scrimba.com/scrim/cy4gdpcK?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

Notez que ce scrim et les autres de ce manuel ont été narrés par un membre de l'équipe Scrimba et ont été ajoutés pour illustrer certains concepts clés de Python.

## 🔸 Programme Hello, World ! en Python

Avant de plonger dans les types de données et les structures de données que vous pouvez utiliser en Python, voyons comment écrire votre premier programme Python.

Il vous suffit d'appeler la fonction `print()` et d'écrire `"Hello, World!"` entre parenthèses :

```python
print("Hello, World!")
```

Vous verrez ce message après avoir exécuté le programme :

```
"Hello, World!"
```

💡 **Conseil :** Écrire un programme `"Hello, World!"` est une tradition dans la communauté des développeurs. La plupart des développeurs commencent à apprendre à coder en écrivant ce programme.

Génial. Vous venez d'écrire votre premier programme Python. Apprenons maintenant les types de données et les structures de données intégrées que vous pouvez utiliser en Python.

## 🔹 Types de données et structures de données intégrées en Python

Nous avons plusieurs types de données de base et structures de données intégrées avec lesquels nous pouvons travailler dans nos programmes. Chacun a ses propres applications particulières. Voyons-les en détail.

### Types de données numériques en Python : Entiers, Flottants et Complexes

Voici les types numériques avec lesquels vous pouvez travailler en Python :

#### Entiers (Integers)

Les entiers sont des nombres sans décimales. Vous pouvez vérifier si un nombre est un entier avec la fonction `type()`. Si la sortie est `<class 'int'>`, alors le nombre est un entier.

Par exemple :

```python
>>> type(1)
<class 'int'>

>>> type(15)
<class 'int'>

>>> type(0)
<class 'int'>

>>> type(-46)
<class 'int'>
```

#### Flottants (Floats)

Les flottants sont des nombres avec des décimales. Vous pouvez les détecter visuellement en localisant le point décimal. Si nous appelons `type()` pour vérifier le type de données de ces valeurs, nous verrons ceci en sortie :

```
<class 'float'>
```

Voici quelques exemples :

```python
>>> type(4.5)
<class 'float'>

>>> type(5.8)
<class 'float'>

>>> type(2342423424.3)
<class 'float'>

>>> type(4.0)
<class 'float'>

>>> type(0.0)
<class 'float'>

>>> type(-23.5)
<class 'float'>
```

#### Complexes

Les nombres complexes ont une partie réelle et une partie imaginaire notée avec `j`. Vous pouvez créer des nombres complexes en Python avec `complex()`. Le premier argument sera la partie réelle et le second argument sera la partie imaginaire.

Voici quelques exemples :

```python
>>> complex(4, 5)
(4+5j)

>>> complex(6, 8)
(6+8j)

>>> complex(3.4, 3.4)
(3.4+3.4j)

>>> complex(0, 0)
0j

>>> complex(5)
(5+0j)

>>> complex(0, 4)
4j
```

### Chaînes de caractères (Strings) en Python

Les chaînes de caractères sont incroyablement utiles en Python. Elles contiennent une séquence de caractères et sont généralement utilisées pour représenter du texte dans le code.

Par exemple :

```
"Hello, World!"
```

```
'Hello, World!'
```

Nous pouvons utiliser des guillemets simples `''` ou des guillemets doubles `""` pour définir une chaîne. Ils sont tous deux valides et équivalents, mais vous devriez en choisir un et l'utiliser de manière cohérente tout au long du programme.

**💡 Conseil :** Oui ! Vous avez utilisé une chaîne de caractères lorsque vous avez écrit le programme `"Hello, World!"`. Chaque fois que vous voyez une valeur entourée de guillemets simples ou doubles en Python, il s'agit d'une chaîne.

Les chaînes peuvent contenir n'importe quel caractère que nous pouvons taper sur notre clavier, y compris des chiffres, des symboles et d'autres caractères spéciaux.

Par exemple :

```
"45678"
```

```
"mon_email@email.com"
```

```
"#JadorePython"
```

**💡 Conseil :** Les espaces sont également comptés comme des caractères dans une chaîne.

#### Guillemets à l'intérieur des chaînes

Si nous définissons une chaîne avec des guillemets doubles `""`, nous pouvons utiliser des guillemets simples à l'intérieur de la chaîne. Par exemple :

```
"J'ai 20 ans"
```

Si nous définissons une chaîne avec des guillemets simples `''`, nous pouvons utiliser des guillemets doubles à l'intérieur de la chaîne. Par exemple :

```
'Mon livre préféré est "Raison et Sentiments"'
```

#### Indexation de chaînes

Nous pouvons utiliser des indices pour accéder aux caractères d'une chaîne dans notre programme Python. Un indice est un entier qui représente une position spécifique dans la chaîne. Ils sont associés au caractère à cette position.

Voici un diagramme de la chaîne `"Hello"` :

```
Chaîne :  H e l l o
Indice :  0 1 2 3 4
```

**💡 Conseil :** Les indices commencent à `0` et sont incrémentés de `1` pour chaque caractère vers la droite.

Par exemple :

```python
>>> ma_chaine = "Hello"

>>> ma_chaine[0]
'H'

>>> ma_chaine[1]
'e'

>>> ma_chaine[2]
'l'

>>> ma_chaine[3]
'l'

>>> ma_chaine[4]
'o'
```

Nous pouvons également utiliser des indices négatifs pour accéder à ces caractères :

```python
>>> ma_chaine = "Hello"

>>> ma_chaine[-1]
'o'

>>> ma_chaine[-2]
'l'

>>> ma_chaine[-3]
'l'

>>> ma_chaine[-4]
'e'

>>> ma_chaine[-5]
'H'
```

**💡 Conseil :** nous utilisons couramment `-1` pour accéder au dernier caractère d'une chaîne.

#### Slicing de chaînes

Nous pouvons également avoir besoin d'obtenir une tranche (slice) d'une chaîne ou un sous-ensemble de ses caractères. Nous pouvons le faire avec le slicing de chaînes.

Voici la syntaxe générale :

```python
<variable_chaine>[start:stop:step]
```

* `start` est l'indice du premier caractère qui sera inclus dans la tranche. Par défaut, c'est `0`.
* `stop` est l'indice du dernier caractère de la tranche (ce caractère ne sera **pas** inclus). Par défaut, c'est le dernier caractère de la chaîne (si nous omettons cette valeur, le dernier caractère sera également inclus).
* `step` est la valeur que nous allons ajouter à l'indice actuel pour atteindre l'indice suivant.

Nous pouvons spécifier deux paramètres pour utiliser la valeur par défaut de `step`, qui est `1`. Cela inclura tous les caractères entre `start` et `stop` (non inclus) :

```python
<variable_chaine>[start:stop]
```

Par exemple :

```python
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp[2:8]
'eeCode'

>>> freecodecamp[0:3]
'fre'

>>> freecodecamp[0:4]
'free'

>>> freecodecamp[4:7]
'Cod'

>>> freecodecamp[4:8]
'Code'

>>> freecodecamp[8:11]
'Cam'

>>> freecodecamp[8:12]
'Camp'

>>> freecodecamp[8:13]
'Camp'
```

**💡 Conseil :** Remarquez que si la valeur d'un paramètre dépasse la plage valide d'indices, la tranche sera toujours présentée. C'est ainsi que les créateurs de Python ont implémenté cette fonctionnalité de slicing.

Si nous personnalisons le `step`, nous "sauterons" d'un indice à l'autre selon cette valeur.

Par exemple :

```python
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp[0:9:2]
'feCdC'

>>> freecodecamp[2:10:3]
'eoC'

>>> freecodecamp[1:12:4]
'roa'

>>> freecodecamp[4:8:2]
'Cd'

>>> freecodecamp[3:9:2]
'eoe'

>>> freecodecamp[1:10:5]
'rd'
```

Nous pouvons également utiliser un pas **négatif** pour aller de droite à gauche :

```python
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp[10:2:-1]
'maCedoCe'

>>> freecodecamp[11:4:-2]
'paeo'

>>> freecodecamp[5:2:-4]
'o'
```

Et nous pouvons omettre un paramètre pour utiliser sa valeur par défaut. Il suffit d'inclure les deux-points correspondants (`:`) si nous omettons `start`, `stop` ou les deux :

```python
>>> freecodecamp = "freeCodeCamp"

# Début et pas par défaut
>>> freecodecamp[:8]
'freeCode'

# Fin et pas par défaut
>>> freecodecamp[4:]
'CodeCamp'

# Début par défaut
>>> freecodecamp[:8:2]
'feCd'

# Fin par défaut
>>> freecodecamp[4::3]
'Cem'

# Début et fin par défaut
>>> freecodecamp[::-2]
'paeoer'

# Début et fin par défaut
>>> freecodecamp[::-1]
'pmaCedoCeerf'
```

**💡 Conseil :** Le dernier exemple est l'un des moyens les plus courants d'inverser une chaîne.

#### f-Strings

Dans Python 3.6 et les versions plus récentes, nous pouvons utiliser un type de chaîne appelé f-string qui nous aide à formater nos chaînes beaucoup plus facilement.

Pour définir une f-string, nous ajoutons simplement un `f` avant les guillemets simples ou doubles. Ensuite, à l'intérieur de la chaîne, nous entourons les variables ou expressions d'accolades `{}`. Cela remplace leur valeur dans la chaîne lors de l'exécution du programme.

Par exemple :

```python
first_name = "Nora"
favorite_language = "Python"

print(f"Salut, je suis {first_name}. J'apprends {favorite_language}.")

```

La sortie est :

```
Salut, je suis Nora. J'apprends Python.
```

Voici un exemple où nous calculons la valeur d'une expression et remplaçons le résultat dans la chaîne :

```python
value = 5

print(f"{value} multiplié par 2 donne : {value * 2}")
```

Les valeurs sont remplacées dans la sortie :

```python
5 multiplié par 2 donne : 10
```

Nous pouvons également appeler des méthodes à l'intérieur des accolades et la valeur retournée sera remplacée dans la chaîne lors de l'exécution du programme :

```python
freecodecamp = "FREECODECAMP"

print(f"{freecodecamp.lower()}")
```

La sortie est :

```python
freecodecamp
```

#### Méthodes de chaînes

Les chaînes ont des méthodes, qui représentent des fonctionnalités communes implémentées par les développeurs Python, afin que nous puissions les utiliser directement dans nos programmes. Elles sont très utiles pour effectuer des opérations courantes.

Voici la syntaxe générale pour appeler une méthode de chaîne :

```python
<variable_chaine>.<nom_methode>(<arguments>)
```

Par exemple :

```python
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp.capitalize()
'Freecodecamp'

>>> freecodecamp.count("C")
2

>>> freecodecamp.find("e")
2

>>> freecodecamp.index("p")
11

>>> freecodecamp.isalnum()
True

>>> freecodecamp.isalpha()
True

>>> freecodecamp.isdecimal()
False

>>> freecodecamp.isdigit()
False

>>> freecodecamp.isidentifier()
True

>>> freecodecamp.islower()
False

>>> freecodecamp.isnumeric()
False

>>> freecodecamp.isprintable()
True

>>> freecodecamp.isspace()
False

>>> freecodecamp.istitle()
False

>>> freecodecamp.isupper()
False

>>> freecodecamp.lower()
'freecodecamp'

>>> freecodecamp.lstrip("f")
'reeCodeCamp'

>>> freecodecamp.rstrip("p")
'freeCodeCam'

>>> freecodecamp.replace("e", "a")
'fraaCodaCamp'

>>> freecodecamp.split("C")
['free', 'ode', 'amp']

>>> freecodecamp.swapcase()
'FREEcODEcAMP'

>>> freecodecamp.title()
'Freecodecamp'

>>> freecodecamp.upper()
'FREECODECAMP'
```

Pour en savoir plus sur les méthodes Python, je vous recommande de lire [cet article](https://docs.python.org/3/library/stdtypes.html#string-methods) de la documentation Python.

💡 **Conseil :** Toutes les méthodes de chaînes renvoient des copies de la chaîne. Elles ne modifient pas la chaîne d'origine car les chaînes sont immuables en Python.

### Booléens en Python

Les valeurs booléennes sont `True` et `False` en Python. Elles doivent commencer par une majuscule pour être reconnues comme une valeur booléenne.

Par exemple :

```python
>>> type(True)
<class 'bool'>

>>> type(False)
<class 'bool'>
```

Si nous les écrivons en minuscules, nous obtiendrons une erreur :

```python
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined

>>> type(false)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    type(false)
NameError: name 'false' is not defined
```

### Listes en Python

Maintenant que nous avons couvert les types de données de base en Python, commençons à couvrir les structures de données intégrées. Tout d'abord, nous avons les listes.

Pour définir une liste, nous utilisons des crochets `[]` avec les éléments séparés par une virgule.

**💡 Conseil :** Il est recommandé d'ajouter un espace après chaque virgule pour rendre le code plus lisible.

Par exemple, voici des exemples de listes :

```
[1, 2, 3, 4, 5]
```

```
["a", "b", "c", "d"]
```

```
[3.4, 2.4, 2.6, 3.5]
```

Les listes peuvent contenir des valeurs de différents types de données, donc ceci serait une liste valide en Python :

```
[1, "Emily", 3.4]
```

Nous pouvons également assigner une liste à une variable :

```python
ma_liste = [1, 2, 3, 4, 5]
```

```python
lettres = ["a", "b", "c", "d"]
```

#### Listes imbriquées

Les listes peuvent contenir des valeurs de n'importe quel type de données, même d'autres listes. Ces listes internes sont appelées **listes imbriquées**.

```python
[[1, 2, 3], [4, 5, 6]]
```

Dans cet exemple, `[1, 2, 3]` et `[4, 5, 6]` sont des listes imbriquées.

Voici d'autres exemples valides :

```python
[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
```

```python
[1, [2, 3, 4], [5, 6, 7], 3.4]
```

Nous pouvons accéder aux listes imbriquées en utilisant leur indice correspondant :

```python
>>> ma_liste = [[1, 2, 3], [4, 5, 6]]

>>> ma_liste[0]
[1, 2, 3]

>>> ma_liste[1]
[4, 5, 6]
```

Les listes imbriquées pourraient être utilisées pour représenter, par exemple, la structure d'un plateau de jeu 2D simple où chaque nombre pourrait représenter un élément ou une tuile différente :

```python
# Exemple de plateau où :
# 0 = Case vide
# 1 = Pièce
# 2 = Ennemi
# 3 = Objectif
board = [[0, 0, 1],
         [0, 2, 0],
         [1, 0, 3]]
```

#### Longueur de liste

Nous pouvons utiliser la fonction `len()` pour obtenir la longueur d'une liste (le nombre d'éléments qu'elle contient).

Par exemple :

```python
>>> ma_liste = [1, 2, 3, 4]

>>> len(ma_liste)
4
```

#### Mettre à jour une valeur dans une liste

Nous pouvons mettre à jour la valeur à un indice particulier avec cette syntaxe :

```python
<variable_liste>[<indice>] = <valeur>
```

Par exemple :

```python
>>> lettres = ["a", "b", "c", "d"]

>>> lettres[0] = "z"

>>> lettres
['z', 'b', 'c', 'd']
```

#### Ajouter une valeur à une liste

Nous pouvons ajouter une nouvelle valeur à la fin d'une liste avec la méthode `.append()`.

Par exemple :

```python
>>> ma_liste = [1, 2, 3, 4]

>>> ma_liste.append(5)

>>> ma_liste
[1, 2, 3, 4, 5]
```

#### Supprimer une valeur d'une liste

Nous pouvons supprimer une valeur d'une liste avec la méthode `.remove()`.

Par exemple :

```python
>>> ma_liste = [1, 2, 3, 4]

>>> ma_liste.remove(3)

>>> ma_liste
[1, 2, 4]
```

💡 **Conseil :** Cela ne supprimera que la première occurrence de l'élément. Par exemple, si nous essayons de supprimer le chiffre 3 d'une liste qui contient deux chiffres 3, le second chiffre ne sera pas supprimé :

```python
>>> ma_liste = [1, 2, 3, 3, 4]

>>> ma_liste.remove(3)

>>> ma_liste
[1, 2, 3, 4]
```

#### Indexation de liste

Nous pouvons indexer une liste tout comme nous indexons les chaînes, avec des indices qui commencent à `0` :

```python
>>> lettres = ["a", "b", "c", "d"]

>>> lettres[0]
'a'

>>> lettres[1]
'b'

>>> lettres[2]
'c'

>>> lettres[3]
'd'
```

#### Slicing de liste

Nous pouvons également obtenir une tranche d'une liste en utilisant la même syntaxe que celle utilisée avec les chaînes et nous pouvons omettre les paramètres pour utiliser leurs valeurs par défaut. Maintenant, au lieu d'ajouter des caractères à la tranche, nous ajouterons les éléments de la liste.

```python
<variable_liste>[start:stop:step]
```

Par exemple :

```python
>>> ma_liste = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

>>> ma_liste[2:6:2]
['c', 'e']

>>> ma_liste[2:8]
['c', 'd', 'e', 'f', 'g', 'h']

>>> ma_liste[1:10]
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

>>> ma_liste[4:8:2]
['e', 'g']

>>> ma_liste[::-1]
['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

>>> ma_liste[::-2]
['i', 'g', 'e', 'c', 'a']

>>> ma_liste[8:1:-1]
['i', 'h', 'g', 'f', 'e', 'd', 'c']
```

#### Méthodes de liste

Python possède également des méthodes de liste déjà implémentées pour nous aider à effectuer des opérations courantes sur les listes. Voici quelques exemples des méthodes de liste les plus couramment utilisées :

```python
>>> ma_liste = [1, 2, 3, 3, 4]

>>> ma_liste.append(5)
>>> ma_liste
[1, 2, 3, 3, 4, 5]

>>> ma_liste.extend([6, 7, 8])
>>> ma_liste
[1, 2, 3, 3, 4, 5, 6, 7, 8]

>>> ma_liste.insert(2, 15)
>>> ma_liste
[1, 2, 15, 3, 3, 4, 5, 6, 7, 8, 2, 2]

>>> ma_liste.remove(2)
>>> ma_liste
[1, 15, 3, 3, 4, 5, 6, 7, 8, 2, 2]

>>> ma_liste.pop()
2

>>> ma_liste.index(6)
6

>>> ma_liste.count(2)
1

>>> ma_liste.sort()
>>> ma_liste
[1, 2, 3, 3, 4, 5, 6, 7, 8, 15]

>>> ma_liste.reverse()
>>> ma_liste
[15, 8, 7, 6, 5, 4, 3, 3, 2, 1]

>>> ma_liste.clear()
>>> ma_liste
[]
```

Pour en savoir plus sur les méthodes de liste, je vous recommande de lire [cet article](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) de la documentation Python.

### Voici un scrim interactif pour vous aider à en savoir plus sur les listes en Python :

<iframe src="https://scrimba.com/scrim/cWNwLacR?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

### Tuples en Python

Pour définir un tuple en Python, nous utilisons des parenthèses `()` et séparons les éléments par une virgule. Il est recommandé d'ajouter un espace après chaque virgule pour rendre le code plus lisible.

```python
(1, 2, 3, 4, 5)
```

```python
("a", "b", "c", "d")
```

```python
(3.4, 2.4, 2.6, 3.5)
```

Nous pouvons assigner des tuples à des variables :

```python
mon_tuple = (1, 2, 3, 4, 5)
```

#### Indexation de tuple

Nous pouvons accéder à chaque élément d'un tuple avec son indice correspondant :

```python
>>> mon_tuple = (1, 2, 3, 4)

>>> mon_tuple[0]
1

>>> mon_tuple[1]
2

>>> mon_tuple[2]
3

>>> mon_tuple[3]
4
```

Nous pouvons également utiliser des indices négatifs :

```python
>>> mon_tuple = (1, 2, 3, 4)

>>> mon_tuple[-1]
4

>>> mon_tuple[-2]
3

>>> mon_tuple[-3]
2

>>> mon_tuple[-4]
1
```

#### Longueur de tuple

Pour trouver la longueur d'un tuple, nous utilisons la fonction `len()`, en passant le tuple comme argument :

```python
>>> mon_tuple = (1, 2, 3, 4)

>>> len(mon_tuple)
4
```

#### Tuples imbriqués

Les tuples peuvent contenir des valeurs de n'importe quel type de données, même des listes et d'autres tuples. Ces tuples internes sont appelés **tuples imbriqués**.

```python
([1, 2, 3], (4, 5, 6))
```

Dans cet exemple, nous avons un tuple imbriqué `(4, 5, 6)` et une liste. Vous pouvez accéder à ces structures de données imbriquées avec leur indice correspondant.

Par exemple :

```python
>>> mon_tuple = ([1, 2, 3], (4, 5, 6))

>>> mon_tuple[0]
[1, 2, 3]

>>> mon_tuple[1]
(4, 5, 6)
```

#### Slicing de tuple

Nous pouvons découper un tuple tout comme nous avons découpé les listes et les chaînes. Le même principe et les mêmes règles s'appliquent.

Voici la syntaxe générale :

```python
<variable_tuple>[start:stop:step]
```

Par exemple :

```python
>>> mon_tuple = (4, 5, 6, 7, 8, 9, 10)

>>> mon_tuple[3:8]
(7, 8, 9, 10)

>>> mon_tuple[2:9:2]
(6, 8, 10)

>>> mon_tuple[:8]
(4, 5, 6, 7, 8, 9, 10)

>>> mon_tuple[:6]
(4, 5, 6, 7, 8, 9)

>>> mon_tuple[:4]
(4, 5, 6, 7)

>>> mon_tuple[3:]
(7, 8, 9, 10)

>>> mon_tuple[2:5:2]
(6, 8)

>>> mon_tuple[::2]
(4, 6, 8, 10)

>>> mon_tuple[::-1]
(10, 9, 8, 7, 6, 5, 4)

>>> mon_tuple[4:1:-1]
(8, 7, 6)
```

#### Méthodes de tuple

Il existe deux méthodes de tuple intégrées en Python :

```python
>>> mon_tuple = (4, 4, 5, 6, 6, 7, 8, 9, 10)

>>> mon_tuple.count(6)
2

>>> mon_tuple.index(7)
5
```

💡 **Conseil :** les tuples sont immuables. Ils ne peuvent pas être modifiés, nous ne pouvons donc pas ajouter, mettre à jour ou supprimer des éléments du tuple. Si nous devons le faire, nous devons créer une nouvelle copie du tuple.

#### Affectation de tuple

En Python, nous avons une fonctionnalité très cool appelée l'affectation de tuple (Tuple Assignment). Avec ce type d'affectation, nous pouvons assigner des valeurs à plusieurs variables sur la même ligne.

Les valeurs sont assignées à leurs variables correspondantes dans l'ordre où elles apparaissent. Par exemple, dans `a, b = 1, 2`, la valeur `1` est assignée à la variable `a` et la valeur `2` est assignée à la variable `b`.

Par exemple :

```python
# Affectation de tuple
>>> a, b = 1, 2

>>> a
1

>>> b
2
```

**💡 Conseil :** L'affectation de tuple est couramment utilisée pour échanger les valeurs de deux variables :

```python
>>> a = 1

>>> b = 2

# Échanger les valeurs
>>> a, b = b, a

>>> a
2

>>> b
1
```

### Dictionnaires en Python

Plongeons maintenant dans les dictionnaires. Cette structure de données intégrée nous permet de créer des paires de valeurs où une valeur est associée à une autre.

Pour définir un dictionnaire en Python, nous utilisons des accolades `{}` avec les paires clé-valeur séparées par une virgule.

La clé est séparée de la valeur par deux-points `:`, comme ceci :

```python
{"a": 1, "b": 2, "c": 3}
```

Vous pouvez assigner le dictionnaire à une variable :

```python
mon_dict = {"a": 1, "b": 2, "c": 3}
```

Les clés d'un dictionnaire doivent être d'un type de données immuable. Par exemple, elles peuvent être des chaînes, des nombres ou des tuples, mais pas des listes puisque les listes sont mutables.

* Chaînes : `{"Ville 1": 456, "Ville 2": 577, "Ville 3": 678}`
* Nombres : `{1: "Aller à gauche", 2: "Aller à droite", 3: "Aller en haut", 4: "Aller en bas"}`
* Tuples : `{(0, 0): "Départ", (2, 4): "Objectif"}`

Les valeurs d'un dictionnaire peuvent être de n'importe quel type de données, nous pouvons donc assigner des chaînes, des nombres, des listes, des tuples, des ensembles et même d'autres dictionnaires comme valeurs. Voici quelques exemples :

```
{"product_id": 4556, "ingredients": ["tomate", "fromage", "champignons"], "price": 10.67}
```

```python
{"product_id": 4556, "ingredients": ("tomate", "fromage", "champignons"), "price": 10.67}
```

```python
{"id": 567, "name": "Emily", "grades": {"Mathématiques": 80, "Biologie": 74, "Anglais": 97}}
```

#### Longueur de dictionnaire

Pour obtenir le nombre de paires clé-valeur, nous utilisons la fonction `len()` :

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> len(mon_dict)
4
```

#### Obtenir une valeur dans un dictionnaire

Pour obtenir une valeur dans un dictionnaire, nous utilisons sa clé avec cette syntaxe :

```python
<variable_avec_dictionnaire>[<cle>]
```

Cette expression sera remplacée par la valeur qui correspond à la clé.

Par exemple :

```python
mon_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

print(mon_dict["a"])
```

La sortie est la valeur associée à `"a"` :

```
1
```

#### Mettre à jour une valeur dans un dictionnaire

Pour mettre à jour la valeur associée à une clé existante, nous utilisons la même syntaxe mais nous ajoutons maintenant un opérateur d'affectation et la valeur :

```python
<variable_avec_dictionnaire>[<cle>] = <valeur>
```

Par exemple :

```
>>> mon_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> mon_dict["b"] = 6
```

Maintenant le dictionnaire est :

```python
{'a': 1, 'b': 6, 'c': 3, 'd': 4}
```

#### Ajouter une paire clé-valeur à un dictionnaire

Les clés d'un dictionnaire doivent être uniques. Pour ajouter une nouvelle paire clé-valeur, nous utilisons la même syntaxe que celle utilisée pour mettre à jour une valeur, mais maintenant la clé doit être nouvelle.

```python
<variable_avec_dictionnaire>[<nouvelle_cle>] = <valeur>
```

Par exemple :

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> mon_dict["e"] = 5
```

Maintenant le dictionnaire a une nouvelle paire clé-valeur :

```python
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

#### Supprimer une paire clé-valeur dans un dictionnaire

Pour supprimer une paire clé-valeur, nous utilisons l'instruction `del` :

```python
del <variable_dictionnaire>[<cle>]

```

Par exemple :

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> del mon_dict["c"]
```

Maintenant le dictionnaire est :

```python
{'a': 1, 'b': 2, 'd': 4}
```

#### Méthodes de dictionnaire

Voici quelques exemples des méthodes de dictionnaire les plus couramment utilisées :

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> mon_dict.get("c")
3

>>> mon_dict.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

>>> mon_dict.keys()
dict_keys(['a', 'b', 'c', 'd'])

>>> mon_dict.pop("d")
4

>>> mon_dict.popitem()
('c', 3)

>>> mon_dict.setdefault("a", 15)
1

>>> mon_dict
{'a': 1, 'b': 2}

>>> mon_dict.setdefault("f", 25)
25

>>> mon_dict
{'a': 1, 'b': 2, 'f': 25}

>>> mon_dict.update({"c": 3, "d": 4, "e": 5})

>>> mon_dict.values()
dict_values([1, 2, 25, 3, 4, 5])

>>> mon_dict.clear()

>>> mon_dict
{}
```

Pour en savoir plus sur les méthodes de dictionnaire, je recommande de [lire cet article](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) de la documentation.

### Et voici un scrim interactif pour vous aider à en savoir plus sur les types de données en Python :

<iframe src="https://scrimba.com/scrim/c42DGyH8?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

## 🔸 Opérateurs Python

Génial. Maintenant vous connaissez la syntaxe des types de données de base et des structures de données intégrées en Python, alors commençons à explorer les opérateurs en Python. Ils sont essentiels pour effectuer des opérations et former des expressions.

### Opérateurs arithmétiques en Python

Ces opérateurs sont :

#### Addition : +

```python
>>> 5 + 6
11

>>> 0 + 6
6

>>> 3.4 + 5.7
9.1

>>> "Hello" + ", " + "World"
'Hello, World'

>>> True + False
1
```

💡 **Conseil :** Les deux derniers exemples sont curieux, n'est-ce pas ? Cet opérateur se comporte différemment selon le type de données des opérandes.

Lorsqu'il s'agit de chaînes, cet opérateur les concatène, et lorsqu'il s'agit de valeurs booléennes, il effectue une opération particulière.

En Python, `True` équivaut à `1` et `False` équivaut à `0`. C'est pourquoi le résultat est `1 + 0 = 1`.

#### Soustraction : -

```python
>>> 5 - 6
-1

>>> 10 - 3
7

>>> 5 - 6
-1

>>> 4.5 - 5.6 - 2.3
-3.3999999999999995

>>> 4.5 - 7
-2.5

>>> - 7.8 - 6.2
-14.0
```

#### Multiplication : *

```python
>>> 5 * 6
30

>>> 6 * 7
42

>>> 10 * 100
1000

>>> 4 * 0
0

>>> 3.4 * 6.8
23.119999999999997

>>> 4 * (-6)
-24

>>> (-6) * (-8)
48

>>> "Hello" * 4
'HelloHelloHelloHello'

>>> "Hello" * 0
''

>>> "Hello" * -1
''
```

**💡 Conseil :** vous pouvez "multiplier" une chaîne par un entier pour répéter la chaîne un nombre donné de fois.

#### Exposant : **

```python
>>> 6 ** 8
1679616

>>> 5 ** 2
25

>>> 4 ** 0
1

>>> 16 ** (1/2)
4.0

>>> 16 ** (0.5)
4.0

>>> 125 ** (1/3)
4.999999999999999

>>> 4.5 ** 2.3
31.7971929089206

>>> 3 ** (-1)
0.3333333333333333
```

#### Division : /

```python
>>> 25 / 5
5.0

>>> 3 / 6
0.5

>>> 0 / 5
0.0

>>> 2467 / 4673
0.5279263856195163

>>> 1 / 2
0.5

>>> 4.5 / 3.5
1.2857142857142858

>>> 6 / 7
0.8571428571428571

>>> -3 / -4
0.75

>>> 3 / -4
-0.75

>>> -3 / 4
-0.75
```

💡 **Conseil :** cet opérateur renvoie un `float` comme résultat, même si la partie décimale est `.0`.

Si vous essayez de diviser par `0`, vous obtiendrez une erreur `ZeroDivisionError` :

```python
>>> 5 / 0
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
```

#### Division entière : //

Cet opérateur renvoie un entier si les opérandes sont des entiers. S'il s'agit de flottants, le résultat sera un flottant avec `.0` comme partie décimale car il tronque la partie décimale.

```python
>>> 5 // 6
0

>>> 8 // 2
4

>>> -4 // -5
0

>>> -5 // 8
-1

>>> 0 // 5
0

>>> 156773 // 356
440
```

#### Modulo : %

```
>>> 1 % 5
1

>>> 2 % 5
2

>>> 3 % 5
3

>>> 4 % 5
4

>>> 5 % 5
0

>>> 5 % 8
5

>>> 3 % 1
0

>>> 15 % 3
0

>>> 17 % 8
1

>>> 2568 % 4
0

>>> 245 % 15
5

>>> 0 % 6
0

>>> 3.5 % 2.4
1.1

>>> 6.7 % -7.8
-1.0999999999999996

>>> 2.3 % 7.5
2.3
```

#### Opérateurs de comparaison

Ces opérateurs sont :

* Supérieur à : `>`
* Supérieur ou égal à : `>=` 
* Inférieur à : `<` 
* Inférieur ou égal à : `<=` 
* Égal à : `==` 
* Différent de : `!=` 

Ces opérateurs de comparaison créent des expressions qui s'évaluent soit à `True`, soit à `False`. Voici quelques exemples :

```
>>> 5 > 6
False

>>> 10 > 8
True

>>> 8 > 8
False

>>> 8 >= 5
True

>>> 8 >= 8
True

>>> 5 < 6
True

>>> 10 < 8
False

>>> 8 < 8
False

>>> 8 <= 5
False

>>> 8 <= 8
True

>>> 8 <= 10
True

>>> 56 == 56
True

>>> 56 == 78
False

>>> 34 != 59
True

>>> 67 != 67
False
```

Nous pouvons également les utiliser pour comparer des chaînes en fonction de leur ordre alphabétique :

```python
>>> "Hello" > "World"
False
>>> "Hello" >= "World"
False
>>> "Hello" < "World"
True
>>> "Hello" <= "World"
True
>>> "Hello" == "World"
False
>>> "Hello" != "World"
True
```

Nous les utilisons généralement pour comparer les valeurs de deux variables ou plus :

```python
>>> a = 1
>>> b = 2

>>> a < b
True

>>> a <= b
True

>>> a > b
False

>>> a >= b
False

>>> a == b
False

>>> a != b
True
```

💡 **Conseil :** remarquez que l'opérateur de comparaison est `==` alors que l'opérateur d'affectation est `=`. Leur effet est différent. `==` renvoie `True` ou `False` tandis que `=` assigne une valeur à une variable.

#### Enchaînement d'opérateurs de comparaison

En Python, nous pouvons utiliser ce qu'on appelle l'"enchaînement d'opérateurs de comparaison" (comparison operator chaining) dans lequel nous enchaînons les opérateurs de comparaison pour effectuer plus d'une comparaison de manière plus concise.

Par exemple, ceci vérifie si `a` est inférieur à `b` et si `b` est inférieur à `c` :

```
a < b < c
```

Voici quelques exemples :

```
>>> a = 1
>>> b = 2
>>> c = 3

>>> a < b < c
True

>>> a > b > c
False

>>> a <= b <= c
True

>>> a >= b >= c
False

>>> a >= b > c
False

>>> a <= b < c
True
```

#### Opérateurs logiques

Il existe trois opérateurs logiques en Python : `and`, `or` et `not`. Chacun de ces opérateurs a sa propre table de vérité et ils sont essentiels pour travailler avec les conditionnels.

L'opérateur `and` :

```python
>>> True and True
True

>>> True and False
False

>>> False and True
False

>>> False and False
False
```

L'opérateur `or` :

```python
>>> True or True
True

>>> True or False
True

>>> False or True
True

>>> False or False
False
```

L'opérateur `not` :

```python
>>> not True
False

>>> not False
True
```

Ces opérateurs sont utilisés pour former des expressions plus complexes combinant différents opérateurs et variables.

Par exemple :

```python
>>> a = 6
>>> b = 3

>>> a < 6 or b > 2
True

>>> a >= 3 and b >= 1
True

>>> (a + b) == 9 and b > 1
True

>>> ((a % 3) < 2) and ((a + b) == 3)
False
```

#### Opérateurs d'affectation

Les opérateurs d'affectation sont utilisés pour assigner une valeur à une variable.

Ce sont : `=`, `+=`, `-=`, `*=`, `%=`, `/=`, `//=`, `**=`

* L'opérateur `=` assigne la valeur à la variable.
* Les autres opérateurs effectuent une opération avec la valeur actuelle de la variable et la nouvelle valeur, puis assignent le résultat à cette même variable.

Par exemple :

```python
>>> x = 3
>>> x
3

>>> x += 15
>>> x
18

>>> x -= 2
>>> x
16

>>> x *= 2
>>> x
32

>>> x %= 5
>>> x
2

>>> x /= 1
>>> x
2.0

>>> x //= 2
>>> x
1.0

>>> x **= 5
>>> x
1.0
```

💡 **Conseils :** ces opérateurs effectuent des opérations bit à bit avant d'assigner le résultat à la variable : `&=`, `|=`, `^=`, `>>=`, `<<=`.

#### Opérateurs d'appartenance

Vous pouvez vérifier si un élément se trouve dans une séquence ou non avec les opérateurs : `in` et `not in`. Le résultat sera soit `True`, soit `False`.

Par exemple :

```python
>>> 5 in [1, 2, 3, 4, 5]
True

>>> 8 in [1, 2, 3, 4, 5]
False

>>> 5 in (1, 2, 3, 4, 5)
True

>>> 8 in (1, 2, 3, 4, 5)
False

>>> "a" in {"a": 1, "b": 2}
True

>>> "c" in {"a": 1, "b": 2}
False

>>> "h" in "Hello"
False

>>> "H" in "Hello"
True

>>> 5 not in [1, 2, 3, 4, 5]
False

>>> 8 not in (1, 2, 3, 4, 5)
True

>>> "a" not in {"a": 1, "b": 2}
False

>>> "c" not in {"a": 1, "b": 2}
True

>>> "h" not in "Hello"
True

>>> "H" not in "Hello"
False
```

Nous les utilisons généralement avec des variables qui stockent des séquences, comme dans cet exemple :

```python
>>> message = "Hello, World!"

>>> "e" in message
True
```

## 🔹 Conditionnels en Python

Voyons maintenant comment nous pouvons écrire des conditionnels pour exécuter (ou non) certaines parties de notre code selon qu'une condition est `True` ou `False`.

### Instructions `if` en Python

Voici la syntaxe d'une instruction `if` de base :

```
if <condition>:
    <code>
```

Si la condition est `True`, le code s'exécutera. Sinon, si elle est `False`, le code ne s'exécutera pas.

**💡 Conseil :** il y a deux-points (`:`) à la fin de la première ligne et le code est indenté. C'est essentiel en Python pour que le code appartienne au conditionnel.

Voici quelques exemples :

#### Condition fausse

```python
x = 5

if x > 9:
    print("Hello, World!")
```

La condition est `x > 9` et le code est `print("Hello, World!")`.

Dans ce cas, la condition est `False`, il n'y a donc pas de sortie.

#### Condition vraie

Voici un autre exemple. Maintenant la condition est `True` :

```python
color = "Bleu"

if color == "Bleu":
    print("C'est ma couleur préférée")
```

La sortie est :

```
"C'est ma couleur préférée"
```

#### Code après le conditionnel

Voici un exemple avec du code qui s'exécute après la fin du conditionnel. Remarquez que la dernière ligne n'est pas indentée, ce qui signifie qu'elle n'appartient pas au conditionnel.

```python
x = 5

if x > 9:
    print("Hello!")

print("Fin")
```

Dans cet exemple, la condition `x > 9` est `False`, donc la première instruction `print` ne s'exécute pas, mais la dernière instruction `print` s'exécute car elle ne fait pas partie du conditionnel. La sortie est donc :

```python
Fin
```

Cependant, si la condition est `True`, comme dans cet exemple :

```python
x = 15

if x > 9:
    print("Hello!")

print("Fin")
```

La sortie sera :

```
Hello!
Fin
```

#### Exemples de conditionnels

Ceci est un autre exemple de conditionnel :

```python
favorite_season = "Été"

if favorite_season == "Été":
    print("C'est aussi ma saison préférée !")
```

Dans ce cas, la sortie sera :

```python
C'est aussi ma saison préférée !
```

Mais si nous changeons la valeur de `favorite_season` :

```python
favorite_season = "Hiver"

if favorite_season == "Été":
    print("C'est aussi ma saison préférée !")
```

Il n'y aura pas de sortie car la condition sera `False`.

### Instructions `if/else` en Python

Nous pouvons ajouter une clause `else` au conditionnel si nous devons spécifier ce qui doit se passer lorsque la condition est `False`.

Voici la syntaxe générale :

```python
if <condition>:
    <code>
else:
    <code>
```

**💡 Conseil :** remarquez que les deux blocs de code sont indentés (`if` et `else`). C'est essentiel pour que Python puisse différencier le code qui appartient au programme principal de celui qui appartient au conditionnel.

Voyons un exemple avec la clause `else` :

#### Condition vraie

```python
x = 15

if x > 9:
    print("Hello!")
else:
    print("Bye!")

print("Fin")
```

La sortie est :

```
Hello!
Fin
```

Lorsque la condition de la clause `if` est `True`, cette clause s'exécute. La clause `else` ne s'exécute pas.

#### Condition fausse

Maintenant, la clause `else` s'exécute car la condition est `False`.

```python
x = 5

if x > 9:
    print("Hello!")
else:
    print("Bye!")

print("Fin")
```

Maintenant la sortie est :

```
Bye!
Fin
```

### Instructions `if/elif/else` en Python

Pour personnaliser encore plus nos conditionnels, nous pouvons ajouter une ou plusieurs clauses `elif` pour vérifier et gérer plusieurs conditions. Seul le code de la première condition qui s'évalue à `True` s'exécutera.

**💡 Conseil :** `elif` doit être écrit après `if` et avant `else`.

#### Première condition vraie

```python
x = 5

if x < 9:
    print("Hello!")
elif x < 15:
    print("C'est super de vous voir")
else:
    print("Bye!")

print("Fin")
```

Nous avons deux conditions `x < 9` et `x < 15`. Seul le bloc de code de la première condition qui est `True` de haut en bas sera exécuté.

Dans ce cas, la sortie est :

```
Hello!
Fin
```

Parce que la première condition est `True` : `x < 9`.

#### Deuxième condition vraie

Si la première condition est `False`, alors la deuxième condition sera vérifiée.

Dans cet exemple, la première condition `x < 9` est `False` mais la deuxième condition `x < 15` est `True`, donc le code qui appartient à cette clause s'exécutera.

```python
x = 13

if x < 9:
    print("Hello!")
elif x < 15:
    print("C'est super de vous voir")
else:
    print("Bye!")

print("Fin")
```

La sortie est :

```
C'est super de vous voir
Fin
```

#### Toutes les conditions sont fausses

Si toutes les conditions sont `False`, alors la clause `else` s'exécutera :

```python
x = 25

if x < 9:
    print("Hello!")
elif x < 15:
    print("C'est super de vous voir")
else:
    print("Bye!")

print("Fin")
```

La sortie sera :

```
Bye!
Fin
```

#### Clauses elif multiples

Nous pouvons ajouter autant de clauses `elif` que nécessaire. Voici un exemple de conditionnel avec deux clauses `elif` :

```python
if favorite_season == "Hiver":
    print("C'est aussi ma saison préférée")
elif favorite_season == "Été":
    print("L'été est incroyable")
elif favorite_season == "Printemps":
    print("J'adore le printemps")
else:
    print("L'automne est la saison préférée de ma mère")
```

Chaque condition sera vérifiée et seul le bloc de code de la première condition qui s'évalue à `True` s'exécutera. Si aucune d'entre elles n'est `True`, la clause `else` s'exécutera.

### Voici un scrim interactif pour vous aider à en savoir plus sur les conditionnels en Python :

<iframe src="https://scrimba.com/scrim/cPm7ZGTk?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

## 🔸 Boucles For en Python

Maintenant que vous savez comment écrire des conditionnels en Python, commençons à explorer les boucles. Les boucles For sont des structures de programmation incroyables que vous pouvez utiliser pour répéter un bloc de code un nombre spécifique de fois.

Voici la syntaxe de base pour écrire une boucle for en Python :

```
for <variable_boucle> in <iterable>:
    <code>
```

L'itérable peut être une liste, un tuple, un dictionnaire, une chaîne, la séquence renvoyée par range, un fichier ou tout autre type d'itérable en Python. Nous allons commencer par `range()`.

### La fonction `range()` en Python

Cette fonction renvoie une séquence d'entiers que nous pouvons utiliser pour déterminer combien d'itérations (répétitions) de la boucle seront effectuées. La boucle effectuera une itération par entier.

**💡 Conseil :** Chaque entier est assigné à la variable de boucle un par un par itération.

Voici la syntaxe générale pour écrire une boucle for avec `range()` :

```
for <variable_boucle> in range(<start>, <stop>, <step>):
    <code>
```

Comme vous pouvez le voir, la fonction range a trois paramètres :

* `start` : où la séquence d'entiers commencera. Par défaut, c'est `0`.
* `stop` : où la séquence d'entiers s'arrêtera (sans inclure cette valeur).
* `step` : la valeur qui sera ajoutée à chaque élément pour obtenir l'élément suivant de la séquence. Par défaut, c'est `1`.

Vous pouvez passer 1, 2 ou 3 arguments à `range()` :

* Avec 1 argument, la valeur est assignée au paramètre `stop` et les valeurs par défaut pour les deux autres paramètres sont utilisées.
* Avec 2 arguments, les valeurs sont assignées aux paramètres `start` et `stop` et la valeur par défaut pour `step` est utilisée.
* Avec 3 arguments, les valeurs sont assignées aux paramètres `start`, `stop` et `step` (dans l'ordre).

Voici quelques exemples avec **un paramètre** :

```python
for i in range(5):
    print(i)
```

Sortie :

```
0
1
2
3
4
```

💡 **Conseil :** la variable de boucle est mise à jour automatiquement.

```python
>>> for j in range(15):
    print(j * 2)
```

Sortie :

```python
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
```

Dans l'exemple ci-dessous, nous répétons une chaîne autant de fois que l'indique la valeur de la variable de boucle :

```python
>>> for num in range(8):
	print("Hello" * num)
```

Sortie :

```python
Hello
HelloHello
HelloHelloHello
HelloHelloHelloHello
HelloHelloHelloHelloHello
HelloHelloHelloHelloHelloHello
HelloHelloHelloHelloHelloHelloHello
```

Nous pouvons également utiliser des boucles for avec des structures de données intégrées telles que les listes :

```python
>>> ma_liste = ["a", "b", "c", "d"]

>>> for i in range(len(ma_liste)):
	print(ma_liste[i])

```

Sortie :

```
a
b
c
d
```

💡 **Conseil :** lorsque vous utilisez `range(len(<seq>))`, vous obtenez une séquence de nombres qui va de `0` jusqu'à `len(<seq>)-1`. Cela représente la séquence d'indices valides.

Voici quelques exemples avec **deux paramètres** :

```python
>>> for i in range(2, 10):
	print(i)
```

Sortie :

```python
2
3
4
5
6
7
8
9
```

**Code :**

```python
>>> for j in range(2, 5):
	print("Python" * j)
```

Sortie :

```python
PythonPython
PythonPythonPython
PythonPythonPythonPython
```

**Code :**

```python
>>> ma_liste = ["a", "b", "c", "d"]

>>> for i in range(2, len(ma_liste)):
	print(ma_liste[i])
```

Sortie :

```python
c
d
```

**Code :**

```python
>>> ma_liste = ["a", "b", "c", "d"]

>>> for i in range(2, len(ma_liste)-1):
	ma_liste[i] *= i
```

Maintenant la liste est : `['a', 'b', 'cc', 'd']`

Voici quelques exemples avec **trois paramètres** :

```python
>>> for i in range(3, 16, 2):
	print(i)
```

Sortie :

```python
3
5
7
9
11
13
15
```

**Code :**

```
>>> for j in range(10, 5, -1):
	print(j)
```

Sortie :

```python
10
9
8
7
6
```

**Code :**

```python
>>> ma_liste = ["a", "b", "c", "d", "e", "f", "g"]

>>> for i in range(len(ma_liste)-1, 2, -1):
	print(ma_liste[i])
```

Sortie :

```python
g
f
e
d
```

### Comment itérer sur des itérables en Python

Nous pouvons itérer directement sur des itérables tels que des listes, des tuples, des dictionnaires, des chaînes et des fichiers en utilisant des boucles for. Nous obtiendrons chacun de leurs éléments un par un par itération. C'est très utile pour travailler directement avec eux.

Voyons quelques exemples :

#### Itérer sur une chaîne

Si nous itérons sur une chaîne, ses caractères seront assignés à la variable de boucle un par un (y compris les espaces et les symboles).

```python
>>> message = "Hello, World!"

>>> for char in message:
	print(char)

	
H
e
l
l
o
,
 
W
o
r
l
d
!
```

Nous pouvons également itérer sur des copies modifiées de la chaîne en appelant une méthode de chaîne où nous spécifions l'itérable dans la boucle for. Cela assignera la copie de la chaîne comme itérable qui sera utilisé pour les itérations, comme ceci :

```python
>>> word = "Hello"

>>> for char in word.lower(): # appel de la méthode de chaîne
	print(char)

	
h
e
l
l
o
```

```python
>>> word = "Hello"

>>> for char in word.upper(): # appel de la méthode de chaîne
	print(char)

	
H
E
L
L
O
```

#### Itérer sur des listes et des tuples

```python
>>> ma_liste = [2, 3, 4, 5]

>>> for num in ma_liste:
	print(num)
```

La sortie est :

```python
2
3
4
5
```

**Code :**

```python
>>> mon_tuple = (2, 3, 4, 5)

>>> for num in mon_tuple:
	if num % 2 == 0:
		print("Pair")
	else:
		print("Impair")
```

Sortie :

```python
Pair
Impair
Pair
Impair
```

### Itérer sur les clés, les valeurs et les paires clé-valeur des dictionnaires

Nous pouvons itérer sur les clés, les valeurs et les paires clé-valeur d'un dictionnaire en appelant des méthodes de dictionnaire spécifiques. Voyons comment.

Pour **itérer sur les clés**, nous écrivons :

```python
for <var> in <variable_dictionnaire>:
    <code>
```

Nous écrivons simplement le nom de la variable qui stocke le dictionnaire comme itérable.

**💡 Conseil :** vous pouvez également écrire `<variable_dictionnaire>.keys()` mais écrire le nom de la variable directement est plus concis et fonctionne exactement de la même manière.

Par exemple :

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3}

>>> for key in mon_dict:
	print(key)

	
a
b
c
```

**💡 Conseil :** vous pouvez assigner n'importe quel nom valide à la variable de boucle.

Pour **itérer sur les valeurs**, nous utilisons :

```python
for <var> in <variable_dictionnaire>.values():
    <code>
```

Par exemple :

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3}

>>> for value in mon_dict.values():
	print(value)

	
1
2
3
```

Pour **itérer sur les paires clé-valeur**, nous utilisons :

```python
for <key>, <value> in <variable_dictionnaire>.items():
    <code>
```

💡 **Conseil :** nous définissons deux variables de boucle car nous voulons assigner la clé et la valeur à des variables que nous pouvons utiliser dans la boucle.

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3}

>>> for key, value in mon_dict.items():
	print(key, value)

	
a 1
b 2
c 3
```

Si nous ne définissons qu'une seule variable de boucle, cette variable contiendra un tuple avec la paire clé-valeur :

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3}
>>> for pair in mon_dict.items():
	print(pair)

	
('a', 1)
('b', 2)
('c', 3)
```

### Break et Continue en Python

Maintenant vous savez comment itérer sur des séquences en Python. Nous avons également des instructions de contrôle de boucle pour personnaliser ce qui se passe lorsque la boucle s'exécute : `break` et `continue`.

#### L'instruction Break

L'instruction `break` est utilisée pour arrêter la boucle immédiatement.

Lorsqu'une instruction `break` est rencontrée, la boucle s'arrête et le programme reprend son exécution normale après la boucle.

Dans l'exemple ci-dessous, nous arrêtons la boucle lorsqu'un élément pair est trouvé.

```python
>>> ma_liste = [1, 2, 3, 4, 5]

>>> for elem in ma_liste:
	if elem % 2 == 0:
		print("Pair :", elem)
		print("break")
		break
	else:
		print("Impair :", elem)

		
Impair : 1
Pair : 2
break
```

#### L'instruction Continue

L'instruction `continue` est utilisée pour ignorer le reste de l'itération actuelle.

Lorsqu'elle est rencontrée pendant l'exécution de la boucle, l'itération actuelle s'arrête et une nouvelle commence avec la valeur mise à jour de la variable de boucle.

Dans l'exemple ci-dessous, nous ignorons l'itération actuelle si l'élément est pair et nous n'imprimons la valeur que si l'élément est impair :

```python
>>> ma_liste = [1, 2, 3, 4, 5]

>>> for elem in ma_liste:
	if elem % 2 == 0:
		print("continue")
		continue
	print("Impair :", elem)

	
Impair : 1
continue
Impair : 3
continue
Impair : 5
```

### La fonction zip() en Python

`zip()` est une fonction intégrée incroyable que nous pouvons utiliser en Python pour itérer sur plusieurs séquences à la fois, en obtenant leurs éléments correspondants à chaque itération.

Il nous suffit de passer les séquences comme arguments à la fonction `zip()` et d'utiliser ce résultat dans la boucle.

Par exemple :

```python
>>> ma_liste1 = [1, 2, 3, 4]
>>> ma_liste2 = [5, 6, 7, 8]

>>> for elem1, elem2 in zip(ma_liste1, ma_liste2):
	print(elem1, elem2)

	
1 5
2 6
3 7
4 8
```

### La fonction enumerate() en Python

Vous pouvez également suivre un compteur pendant que la boucle s'exécute avec la fonction `enumerate()`. Elle est couramment utilisée pour itérer sur une séquence et obtenir l'indice correspondant.

**💡 Conseil :** Par défaut, le compteur commence à `0`.

Par exemple :

```python
>>> ma_liste = [5, 6, 7, 8]

>>> for i, elem in enumerate(ma_liste):
	print(i, elem)

	
0 5
1 6
2 7
3 8
```

```python
>>> word = "Hello"

>>> for i, char in enumerate(word):
	print(i, char)

	
0 H
1 e
2 l
3 l
4 o
```

Si vous commencez le compteur à `0`, vous pouvez utiliser l'indice et la valeur actuelle dans la même itération pour modifier la séquence :

```python
>>> ma_liste = [5, 6, 7, 8]

>>> for index, num in enumerate(ma_liste):
	ma_liste[index] = num * 3

>>> ma_liste
[15, 18, 21, 24]
```

Vous pouvez faire commencer le compteur à un nombre différent en passant un deuxième argument à `enumerate()` :

```python
>>> word = "Hello"

>>> for i, char in enumerate(word, 2):
	print(i, char)

	
2 H
3 e
4 l
5 l
6 o
```

#### La clause else

Les boucles for ont également une clause `else`. Vous pouvez ajouter cette clause à la boucle si vous souhaitez exécuter un bloc de code spécifique lorsque la boucle termine toutes ses itérations sans rencontrer l'instruction `break`.

**💡 Conseil :** si `break` est trouvé, la clause `else` ne s'exécute pas, et si `break` n'est pas trouvé, la clause `else` s'exécute.

Dans l'exemple ci-dessous, nous essayons de trouver un élément supérieur à 6 dans la liste. Cet élément n'est pas trouvé, donc `break` ne s'exécute pas et la clause `else` s'exécute.

```python
ma_liste = [1, 2, 3, 4, 5]

for elem in ma_liste:
    if elem > 6:
        print("Trouvé")
        break
else:
    print("Non trouvé")
```

La sortie est :

```
Non trouvé
```

Cependant, si l'instruction `break` s'exécute, la clause `else` ne s'exécute pas. Nous pouvons le voir dans l'exemple ci-dessous :

```python
ma_liste = [1, 2, 3, 4, 5, 8] # Maintenant la liste contient la valeur 8

for elem in ma_liste:
    if elem > 6:
        print("Trouvé")
        break
else:
    print("Non trouvé")
```

La sortie est :

```
Trouvé
```

## 🔹 Boucles While en Python

Les boucles while sont similaires aux boucles for en ce qu'elles nous permettent de répéter un bloc de code. La différence est que les boucles while s'exécutent tant qu'une condition est `True`.

Dans une boucle while, nous définissons la condition, pas le nombre d'itérations. La boucle s'arrête lorsque la condition est `False`.

Voici la syntaxe générale d'une boucle while :

```python
while <condition>:
    <code>
```

💡 **Conseil :** dans les boucles while, vous devez mettre à jour les variables qui font partie de la condition pour vous assurer que la condition finira par devenir `False`.

Par exemple :

```python
>>> x = 6

>>> while x < 15:
	print(x)
	x += 1

	
6
7
8
9
10
11
12
13
14
```

```python
>>> x = 4

>>> while x >= 0:
	print("Hello" * x)
	x -= 1

	
HelloHelloHelloHello
HelloHelloHello
HelloHello
Hello
```

```python
>>> num = 5

>>> while num >= 1:
	print("*" * num)
	num -= 2

	
*****
***
*
```

#### Break et Continue

Nous pouvons également utiliser `break` et `continue` avec les boucles while et ils fonctionnent exactement de la même manière :

* `break` arrête immédiatement la boucle while.
* `continue` arrête l'itération actuelle et commence la suivante.

Par exemple :

```python
>>> x = 5

>>> while x < 15:
	if x % 2 == 0:
		print("Pair :", x)
		break
	print(x)
	x += 1
    

5
Pair : 6
```

```python
>>> x = 5

>>> while x < 15:
	if x % 2 == 0:
		x += 1
		continue
	print("Impair :", x)
	x += 1

	
Impair : 5
Impair : 7
Impair : 9
Impair : 11
Impair : 13
```

#### La clause `else`

Nous pouvons également ajouter une clause `else` à une boucle while. Si `break` est trouvé, la clause `else` ne s'exécute pas, mais si l'instruction `break` n'est pas trouvée, la clause `else` s'exécute.

Dans l'exemple ci-dessous, l'instruction `break` n'est pas trouvée car aucun des nombres n'est pair avant que la condition ne devienne `False`, donc la clause `else` s'exécute.

```python
x = 5

while x < 15:
	if x % 2 == 0:
		print("Nombre pair trouvé")
		break
	print(x)
	x += 2
else:
	print("Tous les nombres étaient impairs")
```

Voici la sortie :

```python
5
7
9
11
13
Tous les nombres étaient impairs
```

Mais dans cette version de l'exemple, l'instruction `break` est trouvée et la clause `else` ne s'exécute pas :

```python
x = 5

while x < 15:
	if x % 2 == 0:
		print("Nombre pair trouvé")
		break
	print(x)
	x += 1 # Maintenant nous incrémentons la valeur de 1
else:
	print("Tous les nombres étaient impairs")
```

La sortie est :

```python
5
Nombre pair trouvé
```

#### Boucles While infinies

Lorsque nous écrivons et travaillons avec des boucles while, nous pouvons avoir ce qu'on appelle une "boucle infinie". Si la condition n'est jamais `False`, la boucle ne s'arrêtera jamais sans intervention externe.

Cela se produit généralement lorsque les variables de la condition ne sont pas mises à jour correctement pendant l'exécution de la boucle.

**💡 Conseil :** vous devez effectuer les mises à jour nécessaires de ces variables pour vous assurer que la condition finira par s'évaluer à `False`.

Par exemple :

```python
>>> x = 5

>>> while x > 2:
	print(x)

	
5
5
5
5
5
5
5
5
5
.
.
.
# La sortie continue indéfiniment
```

💡 **Conseil :** pour arrêter ce processus, tapez `CTRL + C`. Vous devriez voir un message `KeyboardInterrupt`.

## 🔸 Boucles imbriquées en Python

Nous pouvons écrire des boucles for à l'intérieur de boucles for et des boucles while à l'intérieur de boucles while. Ces boucles internes sont appelées boucles imbriquées.

💡 **Conseil :** la boucle interne s'exécute pour chaque itération de la boucle externe.

### Boucles For imbriquées en Python

```python
>>> for i in range(3):
	for j in range(2):
		print(i, j)

		
0 0
0 1
1 0
1 1
2 0
2 1
```

Si nous ajoutons des instructions print, nous pouvons voir ce qui se passe dans les coulisses :

```python
>>> for i in range(3):
	print("===> Boucle externe")
	print(f"i = {i}")
	for j in range(2):
		print("Boucle interne")
		print(f"j = {j}")

		
===> Boucle externe
i = 0
Boucle interne
j = 0
Boucle interne
j = 1
===> Boucle externe
i = 1
Boucle interne
j = 0
Boucle interne
j = 1
===> Boucle externe
i = 2
Boucle interne
j = 0
Boucle interne
j = 1
```

La boucle interne effectue deux itérations par itération de la boucle externe. Les variables de boucle sont mises à jour lorsqu'une nouvelle itération commence.

Voici un autre exemple :

```python
>>> num_rows = 5

>>> for i in range(5):
	for num_cols in range(num_rows-i):
		print("*", end="")
	print()

	
*****
****
***
**
*
```

### Boucles While imbriquées en Python

Voici un exemple de boucles while imbriquées. Dans ce cas, nous devons mettre à jour les variables qui font partie de chaque condition pour garantir que les boucles s'arrêteront.

```python
>>> i = 5

>>> while i > 0:
	j = 0
	while j < 2:
		print(i, j)
		j += 1
	i -= 1

	
5 0
5 1
4 0
4 1
3 0
3 1
2 0
2 1
1 0
1 1
```

💡 **Conseil :** nous pouvons également avoir des boucles for à l'intérieur de boucles while et des boucles while à l'intérieur de boucles for.

## 🔹 Fonctions en Python

En Python, nous pouvons définir des fonctions pour rendre notre code réutilisable, plus lisible et organisé. Voici la syntaxe de base d'une fonction Python :

```python
def <nom_fonction>(<param1>, <param2>, ...):
    <code>
```

**💡 Conseil :** une fonction peut avoir zéro, un ou plusieurs paramètres.

### Fonction sans paramètres en Python

Une fonction sans paramètres possède une paire de parenthèses vide après son nom dans la définition de la fonction. Par exemple :

```python
def print_pattern():
    size = 4
    for i in range(size):
        print("*" * size)
```

Voici la sortie lorsque nous appelons la fonction :

```python
>>> print_pattern()
****
****
****
****
```

**💡 Conseil :** Vous devez écrire une paire de parenthèses vide après le nom de la fonction pour l'appeler.

### Fonction avec un paramètre en Python

Une fonction avec un ou plusieurs paramètres possède une liste de paramètres entourée de parenthèses après son nom dans la définition de la fonction :

```python
def welcome_student(name):
    print(f"Salut, {name} ! Bienvenue en classe.")
```

Lorsque nous appelons la fonction, il nous suffit de passer une valeur comme argument et cette valeur sera remplacée là où nous utilisons le paramètre dans la définition de la fonction :

```python
>>> welcome_student("Nora")
Salut, Nora ! Bienvenue en classe.
```

Voici un autre exemple – une fonction qui imprime un motif fait d'astérisques. Vous devez spécifier combien de lignes vous souhaitez imprimer :

```python
def print_pattern(num_rows):
    for i in range(num_rows):
        for num_cols in range(num_rows-i):
            print("*", end="")
        print()
```

Vous pouvez voir les différentes sorties pour différentes valeurs de `num_rows` :

```
>>> print_pattern(3)
***
**
*

>>> print_pattern(5)
*****
****
***
**
*

>>> print_pattern(8)
********
*******
******
*****
****
***
**
*
```

### Fonctions avec deux paramètres ou plus en Python

Pour définir deux paramètres ou plus, nous les séparons simplement par une virgule :

```python
def print_sum(a, b):
    print(a + b)

```

Maintenant, lorsque nous appelons la fonction, nous devons passer deux arguments :

```python
>>> print_sum(4, 5)
9

>>> print_sum(8, 9)
17

>>> print_sum(0, 0)
0

>>> print_sum(3, 5)
8
```

Nous pouvons adapter la fonction que nous venons de voir avec un paramètre pour qu'elle fonctionne avec deux paramètres et imprime un motif avec un caractère personnalisé :

```python
def print_pattern(num_rows, char):
	for i in range(num_rows):
		for num_cols in range(num_rows-i):
			print(char, end="")
		print()
```

Vous pouvez voir que la sortie avec le caractère personnalisé est obtenue en appelant la fonction et en passant les deux arguments :

```
>>> print_pattern(5, "A")
AAAAA
AAAA
AAA
AA
A

>>> print_pattern(8, "%")
%%%%%%%%
%%%%%%%
%%%%%%
%%%%%
%%%%
%%%
%%
%

>>> print_pattern(10, "#")
##########
#########
########
#######
######
#####
####
###
##
#
```

### Comment retourner une valeur en Python

Génial. Maintenant vous savez comment définir une fonction, voyons comment vous pouvez travailler avec les instructions return.

Nous aurons souvent besoin de retourner une valeur d'une fonction. Nous pouvons le faire avec l'instruction `return` en Python. Il nous suffit d'écrire ceci dans la définition de la fonction :

```python
return <valeur_a_retourner>
```

**💡 Conseil :** la fonction s'arrête immédiatement lorsque `return` est rencontré et la valeur est renvoyée.

Voici un exemple :

```python
def get_rectangle_area(length, width):
    return length * width
```

Maintenant, nous pouvons appeler la fonction et assigner le résultat à une variable car le résultat est retourné par la fonction :

```python
>>> area = get_rectangle_area(4, 5)
>>> area
20
```

Nous pouvons également utiliser `return` avec un conditionnel pour retourner une valeur selon qu'une condition est `True` ou `False`.

Dans cet exemple, la fonction retourne le premier élément pair trouvé dans la séquence :

```python
def get_first_even(seq):
    for elem in seq:
        if elem % 2 == 0:
            return elem
    else:
        return None
```

Si nous appelons la fonction, nous pouvons voir les résultats attendus :

```python
>>> value1 = get_first_even([2, 3, 4, 5])
>>> value1
2
```

```python
>>> value2 = get_first_even([3, 5, 7, 9])
>>> print(value2)
None
```

💡 **Conseil :** si une fonction n'a pas d'instruction `return` ou n'en trouve pas pendant son exécution, elle retourne `None` par défaut.

Le [Guide de style pour le code Python](https://www.python.org/dev/peps/pep-0008/#programming-recommendations) recommande d'utiliser les instructions return de manière cohérente. Il mentionne que nous devrions :

> Être cohérent dans les instructions return. Soit toutes les instructions return d'une fonction doivent retourner une expression, soit aucune ne le doit. Si une instruction return retourne une expression, toute instruction return où aucune valeur n'est retournée doit explicitement l'indiquer par return None, et une instruction return explicite doit être présente à la fin de la fonction (si elle est accessible).

### Arguments par défaut en Python

Nous pouvons assigner des arguments par défaut pour les paramètres de notre fonction. Pour ce faire, il nous suffit d'écrire `<parametre>=<valeur>` dans la liste des paramètres.

**💡 Conseil :** Le [Guide de style pour le code Python](https://www.python.org/dev/peps/pep-0008/#other-recommendations) mentionne que nous ne devrions pas "utiliser d'espaces autour du signe = lorsqu'il est utilisé pour indiquer un argument mot-clé."

Dans cet exemple, nous assignons la valeur par défaut 5 au paramètre `b`. Si nous omettons cette valeur lors de l'appel de la fonction, la valeur par défaut sera utilisée.

```python
def print_product(a, b=5):
    print(a * b)
```

Si nous appelons la fonction sans cet argument, vous pouvez voir la sortie :

```python
>>> print_product(4)
20
```

Nous confirmons que l'argument par défaut 5 a été utilisé dans l'opération.

Mais nous pouvons également assigner une valeur personnalisée pour `b` en passant un deuxième argument :

```python
>>> print_product(3, 4)
12
```

💡 **Conseil :** les paramètres avec des arguments par défaut doivent être définis à la fin de la liste des paramètres. Sinon, vous verrez cette erreur : `SyntaxError: non-default argument follows default argument`.

Voici un autre exemple avec la fonction que nous avons écrite pour imprimer un motif. Nous assignons la valeur par défaut `"*"` au paramètre `char`.

```python
def print_pattern(num_rows, char="*"):
	for i in range(num_rows):
		for num_cols in range(num_rows-i):
			print(char, end="")
		print()
```

Maintenant, nous avons la possibilité d'utiliser la valeur par défaut ou de la personnaliser :

```python
>>> print_pattern(5)
*****
****
***
**
*

>>> print_pattern(6, "&")
&&&&&&
&&&&&
&&&&
&&&
&&
&
```

### Voici un scrim interactif pour vous aider à en savoir plus sur les fonctions en Python :

<iframe src="https://scrimba.com/scrim/c6BnQesr?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

## 🔸 Récursion en Python

Une fonction récursive est une fonction qui s'appelle elle-même. Ces fonctions ont un cas de base qui arrête le processus récursif et un cas récursif qui continue le processus récursif en effectuant un autre appel récursif.

Voici quelques exemples en Python :

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

```python
def find_power(a, b):
    if b == 0:
        return 1
    else:
        return a * find_power(a, b-1)
```

## 🔹 Gestion des exceptions en Python

Une erreur ou un événement inattendu qui se produit pendant l'exécution d'un programme est appelé une **exception**. Grâce aux éléments que nous allons voir dans un instant, nous pouvons éviter de terminer le programme brusquement lorsque cela se produit.

Voyons les types d'exceptions en Python et comment nous pouvons les gérer.

### Exceptions courantes en Python

Voici une liste d'exceptions courantes en Python et pourquoi elles se produisent :

* **ZeroDivisionError :** levée lorsque le deuxième argument d'une opération de division ou de modulo est zéro.

```python
>>> 5 / 0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero

>>> 7 // 0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    7 // 0
ZeroDivisionError: integer division or modulo by zero

>>> 8 % 0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    8 % 0
ZeroDivisionError: integer division or modulo by zero
```

* **IndexError :** levée lorsque nous essayons d'utiliser un indice invalide pour accéder à un élément d'une séquence.

```python
>>> ma_liste = [3, 4, 5, 6]

>>> ma_liste[15]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ma_liste[15]
IndexError: list index out of range
```

* **KeyError :** levée lorsque nous essayons d'accéder à une paire clé-valeur qui n'existe pas parce que la clé n'est pas dans le dictionnaire.

```python
>>> mon_dict = {"a": 1, "b": 2, "c": 3}

>>> mon_dict["d"]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mon_dict["d"]
KeyError: 'd'
```

* **NameError :** levée lorsque nous utilisons une variable qui n'a pas été définie précédemment.

```python
>>> b
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b
NameError: name 'b' is not defined

```

* **RecursionError :** levée lorsque l'interpréteur détecte que la profondeur de récursion maximale est dépassée. Cela se produit généralement lorsque le processus n'atteint jamais le cas de base.

Dans l'exemple ci-dessous, nous obtiendrons une `RecursionError`. La fonction `factorial` est implémentée de manière récursive mais l'argument passé à l'appel récursif est `n` au lieu de `n-1`. À moins que la valeur ne soit déjà `0` ou `1`, le cas de base ne sera pas atteint car l'argument n'est pas décrémenté, le processus continuera donc et nous obtiendrons cette erreur.

```python
>>> def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n)

	
>>> factorial(5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    factorial(5)
  File "<pyshell#5>", line 5, in factorial
    return n * factorial(n)
  File "<pyshell#5>", line 5, in factorial
    return n * factorial(n)
  File "<pyshell#5>", line 5, in factorial
    return n * factorial(n)
  [Previous line repeated 1021 more times]
  File "<pyshell#5>", line 2, in factorial
    if n == 0 or n == 1:
RecursionError: maximum recursion depth exceeded in comparison
```

💡 **Conseil :** pour en savoir plus sur ces exceptions, je recommande de lire [cet article](https://docs.python.org/3/library/exceptions.html) de la documentation.

### `try` / `except` en Python

Nous pouvons utiliser try/except en Python pour intercepter les exceptions lorsqu'elles se produisent et les gérer de manière appropriée. De cette façon, le programme peut se terminer correctement ou même se remettre de l'exception.

Voici la syntaxe de base :

```python
try:
    <code_qui_peut_lever_une_exception>
except:
    <code_pour_gerer_lexception_si_elle_se_produit>

```

Par exemple, si nous prenons une entrée utilisateur pour accéder à un élément dans une liste, l'entrée pourrait ne pas être un indice valide, donc une exception pourrait être levée :

```python
index = int(input("Entrez l'indice : "))

try:
    ma_liste = [1, 2, 3, 4]
    print(ma_liste[index])
except:
    print("Veuillez entrer un indice valide.")
```

Si nous entrons une valeur invalide comme 15, la sortie sera :

```python
Veuillez entrer un indice valide.
```

Parce que la clause `except` s'exécute. Cependant, si la valeur est valide, le code dans `try` s'exécutera comme prévu.

Voici un autre exemple :

```python
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))

try:
    division = a / b
    print(division)
except:
    print("Veuillez entrer des valeurs valides.")
```

La sortie est :

```
Entrez a : 5
Entrez b : 0

Veuillez entrer des valeurs valides.
```

### Comment intercepter un type spécifique d'exception en Python

Au lieu d'intercepter et de gérer toutes les exceptions possibles qui pourraient se produire dans la clause `try`, nous pourrions intercepter et gérer un type spécifique d'exception. Il nous suffit de spécifier le type de l'exception après le mot-clé `except` :

```python
try:
    <code_qui_peut_lever_une_exception>
except <type_exception>:
    <code_pour_gerer_une_exception_si_elle_se_produit>

```

Par exemple :

```python
index = int(input("Entrez l'indice : "))

try:
    ma_liste = [1, 2, 3, 4]
    print(ma_liste[index])
except IndexError: # spécifier le type
    print("Veuillez entrer un indice valide.")
```

```python
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))

try:
    division = a / b
    print(division)
except ZeroDivisionError: # spécifier le type
    print("Veuillez entrer des valeurs valides.")
```

### Comment assigner un nom à l'objet exception en Python

Nous pouvons spécifier un nom pour l'objet exception en l'assignant à une variable que nous pouvons utiliser dans la clause `except`. Cela nous permettra d'accéder à sa description et à ses attributs.

Il nous suffit d'ajouter `as <nom>`, comme ceci :

```python
try:
    <code_qui_peut_lever_une_exception>
except <type_exception> as <nom>:
    <code_pour_gerer_une_exception_si_elle_se_produit>

```

Par exemple :

```python
index = int(input("Entrez l'indice : "))

try:
    ma_liste = [1, 2, 3, 4]
    print(ma_liste[index])
except IndexError as e:
    print("Exception levée :", e)
```

Voici la sortie si nous entrons `15` comme indice :

```
Entrez l'indice : 15
Exception levée : list index out of range
```

Voici un autre exemple :

```python
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as err:
    print("Veuillez entrer des valeurs valides.", err)

```

Voici la sortie si nous entrons la valeur `0` pour `b` :

```python
Veuillez entrer des valeurs valides. division by zero
```

### `try` / `except` / `else` en Python

Nous pouvons ajouter une clause `else` à cette structure après `except` si nous voulons choisir ce qui se passe lorsqu'aucune exception ne se produit pendant l'exécution de la clause `try` :

```python
try:
    <code_qui_peut_lever_une_exception>
except:
    <code_pour_gerer_une_exception_si_elle_se_produit>
else:
    <code_qui_ne_sexecute_que_si_aucune_exception_dans_try>

```

Par exemple :

```python
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as err:
    print("Veuillez entrer des valeurs valides.", err)
else:
    print("Les deux valeurs étaient valides.")
```

Si nous entrons les valeurs `5` et `0` pour `a` et `b` respectivement, la sortie est :

```
Veuillez entrer des valeurs valides. division by zero
```

Mais si les deux valeurs sont valides, par exemple `5` et `4` pour `a` et `b` respectivement, la clause `else` s'exécute après que `try` est terminé et nous voyons :

```python
1.25
Les deux valeurs étaient valides.
```

### `try` / `except` / `else` / `finally` en Python

Nous pouvons également ajouter une clause `finally` si nous devons exécuter du code qui doit toujours s'exécuter, même si une exception est levée dans `try`.

Par exemple :

```python
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as err:
    print("Veuillez entrer des valeurs valides.", err)
else:
    print("Les deux valeurs étaient valides.")
finally:
    print("Enfin !")
```

Si les deux valeurs sont valides, la sortie est le résultat de la division et :

```
Les deux valeurs étaient valides.
Enfin !
```

Et si une exception est levée parce que `b` est `0`, nous voyons :

```python
Veuillez entrer des valeurs valides. division by zero
Enfin !
```

La clause `finally` s'exécute toujours.

💡 **Conseil :** cette clause peut être utilisée, par exemple, pour fermer des fichiers même si le code lève une exception.

## 🔸 Programmation Orientée Objet en Python

Dans la Programmation Orientée Objet (POO), nous définissons des classes qui agissent comme des plans (blueprints) pour créer des objets en Python avec des attributs et des méthodes (fonctionnalités associées aux objets).

Voici une syntaxe générale pour définir une classe :

```python
class <NomClasse>:

    <nom_attribut_classe> = <valeur>

    def __init__(self, <param1>, <param2>, ...):
        self.<attr1> = <param1>
        self.<attr2> = <param2>
        .
        .
        .
        # Autant d'attributs que nécessaire
    
   def <nom_methode>(self, <param1>, ...):
       <code>
       
   # Autant de méthodes que nécessaire
```

**💡 Conseil :** `self` fait référence à une instance de la classe (un objet créé avec le plan de la classe).

Comme vous pouvez le voir, une classe peut avoir de nombreux éléments différents, analysons-les en détail :

### En-tête de classe

La première ligne de la définition de la classe contient le mot-clé `class` et le nom de la classe :

```python
class Dog:
```

```python
class House:

```

```python
class Ball:
```

**💡 Conseil :** Si la classe hérite d'attributs et de méthodes d'une autre classe, nous verrons le nom de cette classe entre parenthèses :

```python
class Poodle(Dog):
```

```python
class Truck(Vehicle):
```

```python
class Mom(FamilyMember):
```

En Python, nous écrivons le nom de la classe en Upper Camel Case (également connu sous le nom de Pascal Case), dans lequel chaque mot commence par une majuscule. Par exemple : `FamilyMember`.

### `__init__` et attributs d'instance

Nous allons utiliser la classe pour créer des objets en Python, tout comme nous construisons de vraies maisons à partir de plans.

Les objets auront des attributs que nous définissons dans la classe. Généralement, nous initialisons ces attributs dans `__init__`. C'est une méthode qui s'exécute lorsque nous créons une instance de la classe.

Voici la syntaxe générale :

```python
def __init__(self, <parametre1>, <parametre2>, ...):
        self.<attribut1> = <parametre1>  # Attribut d'instance
        self.<attribut2> = <parametre2>  # Attribut d'instance
        .
        .
        .
        # Autant d'attributs d'instance que nécessaire
```

Nous spécifions autant de paramètres que nécessaire pour personnaliser les valeurs des attributs de l'objet qui sera créé.

Voici un exemple d'une classe `Dog` avec cette méthode :

```python
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

💡 **Conseil :** remarquez le double tiret bas au début et à la fin du nom `__init__`.

### Comment créer une instance

Pour créer une instance de `Dog`, nous devons spécifier le nom et l'âge de l'instance de chien pour assigner ces valeurs aux attributs :

```python
mon_chien = Dog("Nora", 10)
```

Génial. Maintenant nous avons notre instance prête à être utilisée dans le programme.

Certaines classes ne nécessiteront aucun argument pour créer une instance. Dans ce cas, nous écrivons simplement des parenthèses vides. Par exemple :

```python
class Circle:

    def __init__(self):
        self.radius = 1
```

Pour créer une instance :

```python
>>> mon_cercle = Circle()
```

💡 **Conseil :** `self` est comme un paramètre qui agit "dans les coulisses", donc même si vous le voyez dans la définition de la méthode, vous ne devriez pas le prendre en compte lorsque vous passez les arguments.

### Arguments par défaut

Nous pouvons également assigner des valeurs par défaut pour les attributs et donner la possibilité à l'utilisateur de personnaliser la valeur s'il le souhaite.

Dans ce cas, nous écririons `<attribut>=<valeur>` dans la liste des paramètres.

Voici un exemple :

```python
class Circle:

    def __init__(self, radius=1):
        self.radius = radius
```

Maintenant, nous pouvons créer une instance de `Circle` avec la valeur par défaut pour le rayon en omettant la valeur, ou la personnaliser en passant une valeur :

```python
# Valeur par défaut
>>> mon_cercle1 = Circle()

# Valeur personnalisée
>>> mon_cercle2 = Circle(5)
```

### Comment obtenir un attribut d'instance

Pour accéder à un attribut d'instance, nous utilisons cette syntaxe :

```python
<variable_objet>.<attribut>
```

Par exemple :

```python
# Définition de la classe
>>> class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Créer une instance
>>> mon_chien = Dog("Nora", 10)

# Obtenir les attributs
>>> mon_chien.name
'Nora'

>>> mon_chien.age
10
```

### Comment mettre à jour un attribut d'instance

Pour mettre à jour un attribut d'instance, nous utilisons cette syntaxe :

```python
<variable_objet>.<attribut> = <nouvelle_valeur>
```

Par exemple :

```python
>>> class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        
>>> mon_chien = Dog("Nora", 10)

>>> mon_chien.name
'Nora'

# Mettre à jour l'attribut
>>> mon_chien.name = "Norita"

>>> mon_chien.name
'Norita'
```

### Comment supprimer un attribut d'instance

Pour supprimer un attribut d'instance, nous utilisons cette syntaxe :

```python
del <variable_objet>.<attribut>
```

Par exemple :

```python
>>> class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        
>>> mon_chien = Dog("Nora", 10)

>>> mon_chien.name
'Nora'

# Supprimer cet attribut
>>> del mon_chien.name

>>> mon_chien.name
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    mon_chien.name
AttributeError: 'Dog' object has no attribute 'name'
```

### Comment supprimer une instance

De même, nous pouvons supprimer une instance en utilisant `del` :

```python
>>> class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        
>>> mon_chien = Dog("Nora", 10)

>>> mon_chien.name
'Nora'

# Supprimer l'instance
>>> del mon_chien

>>> mon_chien
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    mon_chien
NameError: name 'mon_chien' is not defined
```

### Attributs publics vs non publics en Python

En Python, nous n'avons pas de modificateurs d'accès pour restreindre fonctionnellement l'accès aux attributs d'instance, nous nous appuyons donc sur des conventions de nommage pour spécifier cela.

Par exemple, en ajoutant un tiret bas au début, nous pouvons signaler aux autres développeurs qu'un attribut est censé être non public.

Par exemple :

```python
class Dog:

    def __init__(self, name, age):
        self.name = name  # Attribut public
        self._age = age   # Attribut non public
```

La documentation Python mentionne :

> N'utilisez un tiret bas au début que pour les méthodes et les variables d'instance non publiques.
>
> Décidez toujours si les méthodes et les variables d'instance d'une classe (collectivement : "attributs") doivent être publiques ou non publiques. En cas de doute, choisissez non public ; il est plus facile de rendre un attribut public plus tard que de rendre un attribut public non public.
>
> Les attributs non publics sont ceux qui ne sont pas destinés à être utilisés par des tiers ; vous ne donnez aucune garantie que les attributs non publics ne changeront pas ou ne seront pas supprimés. - [source](https://www.python.org/dev/peps/pep-0008/#designing-for-inheritance)

Cependant, comme la documentation le mentionne également :

> Nous n'utilisons pas le terme "privé" ici, car aucun attribut n'est réellement privé en Python (sans une quantité de travail généralement inutile). - [source](https://www.python.org/dev/peps/pep-0008/#designing-for-inheritance)

**💡 Conseil :** techniquement, nous pouvons toujours accéder à l'attribut et le modifier si nous ajoutons le tiret bas au début de son nom, mais nous ne devrions pas le faire.

### Attributs de classe en Python

Les attributs de classe sont partagés par toutes les instances de la classe. Elles ont toutes accès à cet attribut et seront également affectées par tout changement apporté à ces attributs.

```python
class Dog:

    # Attributs de classe
    kingdom = "Animalia"
    species = "Canis lupus"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**💡 Conseil :** généralement, ils sont écrits avant la méthode `__init__`.

### Comment obtenir un attribut de classe

Pour obtenir la valeur d'un attribut de classe, nous utilisons cette syntaxe :

```python
<nom_classe>.<attribut>
```

Par exemple :

```python
>>> class Dog:

    kingdom = "Animalia"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        
>>> Dog.kingdom
'Animalia'
```

**💡 Conseil :** Vous pouvez également utiliser cette syntaxe à l'intérieur de la classe.

### Comment mettre à jour un attribut de classe

Pour mettre à jour un attribut de classe, nous utilisons cette syntaxe :

```python
<nom_classe>.<attribut> = <valeur>
```

Par exemple :

```python
>>> class Dog:

    kingdom = "Animalia"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        
>>> Dog.kingdom
'Animalia'

>>> Dog.kingdom = "Nouveau Royaume"

>>> Dog.kingdom
'Nouveau Royaume'
```

### Comment supprimer un attribut de classe

Nous utilisons `del` pour supprimer un attribut de classe. Par exemple :

```python
>>> class Dog:

    kingdom = "Animalia"

    def __init__(self, name, age):
        self.name = name
        self.age = age

>>> Dog.kingdom
'Animalia'
        
# Supprimer l'attribut de classe
>>> del Dog.kingdom

>>> Dog.kingdom
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    Dog.kingdom
AttributeError: type object 'Dog' has no attribute 'kingdom'
```

### Comment définir des méthodes

Les méthodes représentent la fonctionnalité des instances de la classe.

**💡 Conseil :** Les méthodes d'instance peuvent travailler avec les attributs de l'instance qui appelle la méthode si nous écrivons `self.<attribut>` dans la définition de la méthode.

Voici la syntaxe de base d'une méthode dans une classe. Elles sont généralement situées en dessous de `__init__` :

```python
class <NomClasse>:

    # Attributs de classe

    # __init__

    def <nom_methode>(self, <param1>, ...):
        <code>
```

Elles peuvent avoir zéro, un ou plusieurs paramètres si nécessaire (tout comme les fonctions !) mais les méthodes d'instance doivent toujours avoir `self` comme premier paramètre.

Par exemple, voici une méthode `bark` sans paramètres (en plus de `self`) :

```python
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"ouaf-ouaf. Je suis {self.name}")
```

Pour appeler cette méthode, nous utilisons cette syntaxe :

```python
<variable_objet>.<methode>(<arguments>)
```

Par exemple :

```python
# Créer l'instance
>>> mon_chien = Dog("Nora", 10)

# Appeler la méthode
>>> mon_chien.bark()
ouaf-ouaf. Je suis Nora
```

Voici une classe `Player` avec une méthode `increment_speed` possédant un paramètre :

```python
class Player:

    def __init__(self, name):
        self.name = name
        self.speed = 50

    def increment_speed(self, value):
        self.speed += value
```

Pour appeler la méthode :

```python
# Créer une instance
>>> mon_joueur = Player("Nora")

# Vérifier la vitesse initiale pour voir le changement
>>> mon_joueur.speed
50

# Incrémenter la vitesse
>>> mon_joueur.increment_speed(5)

# Confirmer le changement
>>> mon_joueur.speed
55
```

💡 **Conseil :** pour ajouter plus de paramètres, séparez-les simplement par une virgule. Il est recommandé d'ajouter un espace après la virgule.

### Propriétés, Getters et Setters en Python

Les getters et setters sont des méthodes que nous pouvons définir pour obtenir et définir la valeur d'un attribut d'instance, respectivement. Ils fonctionnent comme des intermédiaires pour "protéger" les attributs des modifications directes.

En Python, nous utilisons généralement des propriétés au lieu des getters et setters. Voyons comment nous pouvons les utiliser.

Pour définir une propriété, nous écrivons une méthode avec cette syntaxe :

```python
@property
def <nom_propriete>(self):
    return self.<attribut>
```

Cette méthode agira comme un getter, elle sera donc appelée lorsque nous essaierons d'accéder à la valeur de l'attribut.

Maintenant, nous pourrions également vouloir définir un setter :

```python
@<nom_propriete>.setter
def <nom_propriete>(self, <param>):
    self.<attribut> = <param>
```

Et un deleter pour supprimer l'attribut :

```python
@<nom_propriete>.deleter
def <nom_propriete>(self):
    del self.<attribut>
```

**💡 Conseil :** vous pouvez écrire n'importe quel code dont vous avez besoin dans ces méthodes pour obtenir, définir et supprimer un attribut. Il est recommandé de les garder aussi simples que possible.

Voici un exemple :

```python
class Dog:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name
```

Si nous ajoutons des instructions print descriptives, nous pouvons voir qu'elles sont appelées lorsque nous effectuons leur opération :

```python
>>> class Dog:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Appel du getter")
        return self._name

    @name.setter
    def name(self, new_name):
        print("Appel du setter")
        self._name = new_name

    @name.deleter
    def name(self):
        print("Appel du deleter")
        del self._name

        
>>> mon_chien = Dog("Nora")

>>> mon_chien.name
Appel du getter
'Nora'

>>> mon_chien.name = "Norita"
Appel du setter

>>> mon_chien.name
Appel du getter
'Norita'

>>> del mon_chien.name
Appel du deleter
```

## 🔹 Comment travailler avec des fichiers en Python

Travailler avec des fichiers est très important pour créer des programmes puissants. Voyons comment vous pouvez faire cela en Python.

### Comment lire des fichiers en Python

En Python, il est recommandé d'utiliser une instruction `with` pour travailler avec des fichiers car elle ne les ouvre que pendant que nous en avons besoin et les ferme automatiquement lorsque le processus est terminé.

Pour lire un fichier, nous utilisons cette syntaxe :

```python
with open("<chemin_fichier>") as <variable_fichier>:
    <code>
```

Nous pouvons également spécifier que nous voulons ouvrir le fichier en mode lecture avec un `"r"` :

```python
with open("<chemin_fichier>", "r") as <variable_fichier>:
    <code>
```

Mais c'est déjà le mode par défaut pour ouvrir un fichier, nous pouvons donc l'omettre comme dans le premier exemple.

Voici un exemple :

```python
with open("famous_quotes.txt") as file:
    for line in file:
        print(line)
```

ou...

```python
with open("famous_quotes.txt", "r") as file:
    for line in file:
        print(line)
```

**💡 Conseil :** c'est exact ! Nous pouvons itérer sur les lignes du fichier en utilisant une boucle for. Le chemin du fichier peut être relatif au script Python que nous exécutons ou il peut s'agir d'un chemin absolu.

### Comment écrire dans un fichier en Python

Il existe deux façons d'écrire dans un fichier. Vous pouvez soit remplacer tout le contenu du fichier avant d'ajouter le nouveau contenu, soit l'ajouter au contenu existant.

```python
with open("<chemin_fichier>", "w") as <variable_fichier>:
    <code>
```

Pour remplacer complètement le contenu, nous utilisons le mode `"w"`, nous passons donc cette chaîne comme deuxième argument à `open()`. Nous appelons la méthode `.write()` sur l'objet fichier en passant le contenu que nous voulons écrire comme argument.

Par exemple :

```python
words = ["Amazing", "Green", "Python", "Code"]

with open("famous_quotes.txt", "w") as file:
    for word in words:
        file.write(word + "\n")
```

Lorsque vous exécutez le programme, un nouveau fichier sera créé s'il n'existe pas déjà dans le chemin que nous avons spécifié.

Voici quel sera le contenu du fichier :

```python
Amazing
Green
Python
Code
```

### Comment ajouter du contenu à un fichier en Python

Cependant, si vous souhaitez ajouter du contenu à la fin, vous devez utiliser le mode `"a"` (append) :

```python
with open("<chemin_fichier>", "a") as <variable_fichier>:
    <code>

```

Par exemple :

```python
words = ["Amazing", "Green", "Python", "Code"]

with open("famous_quotes.txt", "a") as file:
    for word in words:
        file.write(word + "\n")
```

Ce petit changement conservera le contenu existant du fichier et ajoutera le nouveau contenu à la fin.

Si nous exécutons à nouveau le programme, ces chaînes seront ajoutées à la fin du fichier :

```python
Amazing
Green
Python
Code
Amazing
Green
Python
Code

```

### Comment supprimer un fichier en Python

Pour supprimer un fichier avec notre script, nous pouvons utiliser le module `os`. Il est recommandé de vérifier avec un conditionnel si le fichier existe avant d'appeler la fonction `remove()` de ce module :

```python
import os

if os.path.exists("<chemin_fichier>"):
  os.remove("<chemin_fichier>")
else:
  <code>
```

Par exemple :

```python
import os

if os.path.exists("famous_quotes.txt"):
  os.remove("famous_quotes.txt")
else:
  print("Ce fichier n'existe pas")
```

Vous avez peut-être remarqué la première ligne qui dit `import os`. Il s'agit d'une instruction d'importation. Voyons pourquoi elles sont utiles et comment vous pouvez travailler avec elles.

## 🔸 Instructions d'importation en Python

Organiser votre code en plusieurs fichiers au fur et à mesure que votre programme gagne en taille et en complexité est une bonne pratique. Mais nous devons trouver un moyen de combiner ces fichiers pour que le programme fonctionne correctement, et c'est exactement ce que font les instructions d'importation.

En écrivant une instruction d'importation, nous pouvons importer un module (un fichier qui contient des définitions et des instructions Python) dans un autre fichier.

Voici plusieurs alternatives pour les instructions d'importation :

### Première alternative :

```
import <nom_module>
```

Par exemple :

```
import math
```

💡 **Conseil :** `math` est un module Python intégré.

Si nous utilisons cette instruction d'importation, nous devrons ajouter le nom du module avant le nom de la fonction ou de l'élément auquel nous nous référons dans notre code :

```python
>>> import math
>>> math.sqrt(25)
5.0
```

Nous mentionnons explicitement dans notre code le module auquel l'élément appartient.

### Deuxième alternative :

```
import <module> as <nouveau_nom>
```

Par exemple :

```
import math as m
```

Dans notre code, nous pouvons utiliser le nouveau nom que nous avons assigné au lieu du nom original du module :

```python
>>> import math as m
>>> m.sqrt(25)
5.0
```

### Troisième alternative :

```
from <nom_module> import <element>
```

Par exemple :

```
from math import sqrt
```

Avec cette instruction d'importation, nous pouvons appeler la fonction directement sans spécifier le nom du module :

```python
>>> from math import sqrt
>>> sqrt(25)
5.0
```

### Quatrième alternative :

```
from <nom_module> import <element> as <nouveau_nom>
```

Par exemple :

```python
from math import sqrt as square_root
```

Avec cette instruction d'importation, nous pouvons assigner un nouveau nom à l'élément importé du module :

```python
>>> from math import sqrt as square_root
>>> square_root(25)
5.0
```

### Cinquième alternative :

```
from <nom_module> import *
```

Cette instruction importe tous les éléments du module et vous pouvez vous y référer directement par leur nom sans spécifier le nom du module.

Par exemple :

```python
>>> from math import *

>>> sqrt(25)
5.0

>>> factorial(5)
120

>>> floor(4.6)
4

>>> gcd(5, 8)
1
```

💡 **Conseil :** ce type d'instruction d'importation peut nous empêcher de savoir quels éléments appartiennent à quel module, particulièrement lorsque nous importons des éléments de plusieurs modules.

Selon le [Guide de style pour le code Python](https://www.python.org/dev/peps/pep-0008/#imports) :

> Les **importations génériques** (from <module> import *) devraient être évitées, car elles rendent peu clair quels noms sont présents dans l'espace de noms, ce qui sème la confusion chez les lecteurs et pour de nombreux outils automatisés.

## 🔹 Compréhension de listes et de dictionnaires en Python

Une fonctionnalité vraiment sympa de Python que vous devriez connaître est la compréhension de listes et de dictionnaires. C'est simplement une façon de créer des listes et des dictionnaires de manière plus compacte.

### Compréhension de liste en Python

La syntaxe utilisée pour définir les compréhensions de liste suit généralement l'un de ces quatre modèles :

```python
[<valeur_a_inclure> for <var> in <sequence>]
```

```python
[<valeur_a_inclure> for <var1> in <sequence1> for <var2> in <sequence2>]
```

```python
[<valeur_a_inclure> for <var> in <sequence> if <condition>]
```

```python
[<valeur> for <var1> in <sequence1> for <var2> in <sequence2> if <condition>]
```

**💡 Conseil :** vous ne devriez les utiliser que lorsqu'elles ne rendent pas votre code plus difficile à lire et à comprendre.

Voici quelques exemples :

```python
>>> [i for i in range(4, 15)]
[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

>>> [chr(i) for i in range(67, 80)]
['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

>>> [i**3 for i in range(2, 5)]
[8, 27, 64]

>>> [i + j for i in range(5, 8) for j in range(3, 6)]
[8, 9, 10, 9, 10, 11, 10, 11, 12]

>>> [k for k in range(3, 35) if k % 2 == 0]
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]

>>> [i * j for i in range(2, 6) for j in range(3, 7) if i % j == 0]
[9, 16, 25]
```

### Compréhensions de liste vs expressions génératrices en Python

Les compréhensions de liste sont définies avec des crochets `[]`. C'est différent des expressions génératrices, qui sont définies avec des parenthèses `()`. Elles se ressemblent mais sont assez différentes. Voyons pourquoi.

* Les **compréhensions de liste** génèrent la séquence entière d'un coup et la stockent en mémoire.
* Les **expressions génératrices** produisent les éléments un par un lorsqu'ils sont demandés.

Nous pouvons vérifier cela avec le module `sys`. Dans l'exemple ci-dessous, vous pouvez voir que leur taille en mémoire est très différente :

```python
>>> import sys
>>> sys.getsizeof([i for i in range(500)])
2132
>>> sys.getsizeof((i for i in range(500)))
56
```

Nous pouvons utiliser des expressions génératrices pour itérer dans une boucle for et obtenir les éléments un par un. Mais si nous avons besoin de stocker les éléments dans une liste, nous devrions utiliser la compréhension de liste.

### Compréhension de dictionnaire en Python

Plongeons maintenant dans la compréhension de dictionnaire. La syntaxe de base que nous devons utiliser pour définir une compréhension de dictionnaire est :

```python
{<cle_valeur>: <valeur> for <var> in <sequence>}
```

```python
{<cle_valeur>: <valeur> for <var> in <sequence> if <condition>}
```

Voici quelques exemples de compréhension de dictionnaire :

```python
>>> {num: num**3 for num in range(3, 15)}
{3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331, 12: 1728, 13: 2197, 14: 2744}

>>> {x: x + y for x in range(4, 8) for y in range(3, 7)}
{4: 10, 5: 11, 6: 12, 7: 13}
```

Voici un exemple avec un conditionnel où nous prenons un dictionnaire existant et créons un nouveau dictionnaire avec seulement les étudiants qui ont obtenu une note de passage supérieure ou égale à 60 :

```python
>>> grades = {"Nora": 78, "Gino": 100, "Talina": 56, "Elizabeth": 45, "Lulu": 67}

>>> approved_students = {student: grade for (student, grade) in grades.items() if grade >= 60}

>>> approved_students
{'Nora': 78, 'Gino': 100, 'Lulu': 67}
```

**J'espère vraiment que vous avez aimé cet article et qu'il vous a été utile.** Maintenant vous savez comment écrire et travailler avec les éléments les plus importants de Python.

⭐ [Abonnez-vous à ma chaîne YouTube](https://www.youtube.com/channel/UCng0h8WiHLmT57JJ8At4LfQ) et suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN) pour trouver plus de tutoriels et de conseils de codage. Découvrez mon cours en ligne [Python Exercises for Beginners: Solve 100+ Coding Challenges](https://www.udemy.com/course/python-exercises-for-beginners-solve-coding-challenges/?referralCode=804D1EFAF779D07914D2)