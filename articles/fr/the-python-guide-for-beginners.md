---
title: Le Guide Ultime de Python pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-15T21:59:17.000Z'
originalURL: https://freecodecamp.org/news/the-python-guide-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/cover-post-smaller.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: Le Guide Ultime de Python pour Débutants
seo_desc: 'By Renan Moura Ferreira

  Python has become one of the fastest-growing programming languages over the past
  few years.

  Not only it is widely used, it is also an awesome language to tackle if you want
  to get into the world of programming.

  This Python Gui...'
---

Par Renan Moura Ferreira

Python est devenu l'un des langages de programmation à la croissance la plus rapide au cours des dernières années.

Non seulement il est largement utilisé, mais c'est aussi un langage génial à apprendre si vous voulez vous lancer dans le monde de la programmation.

Ce Guide Python pour Débutants vous permet d'apprendre les bases du langage en quelques heures au lieu de semaines.

Info rapide : [Vous pouvez télécharger une version PDF de ce Guide Python pour Débutants](https://renanmf.com/python-guide-beginners/).

Prêt à plonger ?

# Table des matières
1. [Introduction à Python](#heading-introduction-a-python)
2. [Installation de Python 3](#heading-installation-de-python-3)
3. [Exécution de Code](#heading-execution-de-code)
4. [Syntaxe](#heading-syntaxe)
5. [Commentaires](#heading-commentaires)
6. [Variables](#heading-variables)
7. [Types](#heading-types)
8. [Conversion de Types](#heading-conversion-de-types)
9. [Saisie Utilisateur](#heading-saisie-utilisateur)
10. [Opérateurs](#heading-operateurs)
11. [Conditionnelles](#heading-conditionnelles)
12. [Listes](#heading-listes)
13. [Tuples](#heading-tuples)
14. [Ensembles](#heading-ensembles)
15. [Dictionnaires](#heading-dictionnaires)
16. [Boucles while](#heading-boucles-while)
17. [Boucles for](#heading-boucles-for)
18. [Fonctions](#heading-fonctions)
19. [Portée](#heading-portee)
20. [Compréhensions de Liste](#heading-comprehensions-de-liste)
21. [Fonctions Lambda](#heading-fonctions-lambda)
22. [Modules](#heading-modules)
23. [if __name__ == '__main__'](#heading-if-name-main)
24. [Fichiers](#heading-fichiers)
25. [Classes et Objets](#heading-classes-et-objets)
26. [Héritage](#heading-heritage)
27. [Exceptions](#heading-exceptions)
28. [Conclusion](#heading-conclusion)

# Introduction à Python

Python a été créé en 1990 par Guido van Rossum aux Pays-Bas.

L'un des objectifs du langage était d'être accessible aux non-programmeurs.

Python a également été conçu pour être un deuxième langage pour les programmeurs en raison de sa faible courbe d'apprentissage et de sa facilité d'utilisation.

Python fonctionne sur Mac, Linux, Windows et de nombreuses autres plateformes.

Python est :

* Interprété : il peut s'exécuter à l'exécution, et les changements dans un programme sont instantanément perceptibles. Pour être très technique, Python a un compilateur. La différence par rapport à Java ou C++ est la transparence et l'automatisation. Avec Python, nous n'avons pas à nous soucier de l'étape de compilation car elle est effectuée en temps réel. Le compromis est que les langages interprétés sont généralement plus lents que les langages compilés.

* Dynamique sémantiquement : vous n'avez pas à spécifier les types pour les variables et il n'y a rien qui vous oblige à le faire.

* Orienté objet : tout en Python est un objet. Mais vous pouvez choisir d'écrire du code de manière orientée objet, procédurale, ou même fonctionnelle.

* De haut niveau : vous n'avez pas à gérer les détails de bas niveau de la machine.

Python a beaucoup grandi récemment en partie grâce à ses nombreuses utilisations dans les domaines suivants :

* Scripting système : c'est un excellent outil pour automatiser les tâches répétitives quotidiennes.

* Analyse de données : c'est un excellent langage pour expérimenter et dispose de tonnes de bibliothèques et d'outils pour manipuler des données, créer des modèles, visualiser des résultats et même déployer des solutions. Cela est utilisé dans des domaines comme la finance, le e-commerce et la recherche.

* Développement web : des frameworks comme Django et Flask permettent le développement d'applications web, d'API et de sites web.

* Apprentissage automatique : Tensorflow et Pytorch sont quelques-unes des bibliothèques qui permettent aux scientifiques et à l'industrie de développer et de déployer des solutions d'intelligence artificielle dans la reconnaissance d'images, la santé, les voitures autonomes et de nombreux autres domaines.

Vous pouvez facilement organiser votre code en modules et les réutiliser ou les partager avec d'autres.

Enfin, nous devons garder à l'esprit que Python a eu des changements majeurs entre les versions 2 et 3. Et puisque le support de Python 2 a pris fin en 2020, cet article est uniquement basé sur Python 3.

Alors, commençons.


# Installation de Python 3

Si vous utilisez un Mac ou Linux, vous avez déjà Python installé. Mais Windows ne vient pas avec Python installé par défaut.

Vous pourriez également avoir Python 2, et nous allons utiliser Python 3. Vous devriez donc vérifier si vous avez Python 3 d'abord.

Tapez ce qui suit dans votre terminal.

```shell
python3 -V
```

Remarquez le `V` majuscule.

Si votre résultat est quelque chose de similaire à 'Python 3.x.y', par exemple, `Python 3.8.1`, alors vous êtes prêt à partir.

Sinon, suivez les instructions suivantes selon votre système d'exploitation.

## Installation de Python 3 sur Windows
Allez sur [https://www.python.org/downloads/](https://www.python.org/downloads/).

Téléchargez la dernière version.

Après le téléchargement, double-cliquez sur l'installateur.

Sur le premier écran, cochez la case indiquant "Ajouter Python 3.x à PATH" puis cliquez sur "Installer maintenant".

Attendez que le processus d'installation se termine jusqu'à l'écran suivant avec le message "L'installation a réussi".

Cliquez sur "Fermer".

## Installation de Python 3 sur Mac
Installez [XCode](https://itunes.apple.com/br/app/xcode/id497799835) depuis l'App Store.

Installez les outils de ligne de commande en exécutant ce qui suit dans votre terminal.

```shell
xcode-select --install
```

Je recommande d'utiliser Homebrew. Allez sur [https://brew.sh/](https://brew.sh/) et suivez les instructions sur la première page pour l'installer.

Après avoir installé Homebrew, exécutez les commandes `brew` suivantes pour installer Python 3.

```shell
brew update
brew install python3
```

Homebrew ajoute déjà Python 3 au PATH, vous n'avez donc rien d'autre à faire.

## Installation de Python 3 sur Linux
Pour installer en utilisant `apt`, disponible dans Ubuntu et Debian, entrez ce qui suit :

```shell
sudo apt install python3
```

Pour installer en utilisant `yum`, disponible dans RedHat et CentOS, entrez ce qui suit :

```shell
sudo yum install python3
```


# Exécution de Code

Vous pouvez exécuter du code Python directement dans le terminal en tant que commandes ou vous pouvez sauvegarder le code dans un fichier avec l'extension `.py` et exécuter le fichier Python.

## Terminal

L'exécution de commandes directement dans le terminal est recommandée lorsque vous voulez exécuter quelque chose de simple.

Ouvrez la ligne de commande et tapez `python3`

```shell
renan@mypc:~$ python3
```

Vous devriez voir quelque chose comme ceci dans votre terminal indiquant la version (dans mon cas, Python 3.6.9), le système d'exploitation (j'utilise Linux), et quelques commandes de base pour vous aider.

Le ```>>>``` nous indique que nous sommes dans la console Python.

```shell
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Testons-le en exécutant notre premier programme pour effectuer des calculs mathématiques de base et additionner deux nombres.

```shell
>>> 2 + 2
```

Le résultat est :
```
4
```

Pour quitter la console Python, tapez simplement `exit()`.

```shell
>>> exit()
```

## Exécution de fichiers `.py`

Si vous avez un programme complexe, avec de nombreuses lignes de code, la console Python n'est pas la meilleure option.

L'alternative est simplement d'ouvrir un éditeur de texte, de taper le code, et de sauvegarder le fichier avec une extension `.py`.

Faisons cela, créez un fichier appelé `second_program.py` avec le contenu suivant.

```python
print('Second Program')
```

La fonction `print()` affiche un message à l'écran.

Le message va à l'intérieur des parenthèses avec des guillemets simples ou doubles, les deux fonctionnent de la même manière.

Pour exécuter le programme, dans votre terminal faites ce qui suit :

```shell
renan@mypc:~$ python3 second_program.py
```

Le résultat est :

```
Second Program
```


# Syntaxe

Python est connu pour sa syntaxe propre.

Le langage évite d'utiliser des caractères inutiles pour indiquer une spécificité.

## Points-virgules

Python n'utilise pas de points-virgules pour terminer les lignes. Une nouvelle ligne suffit pour indiquer à l'interpréteur qu'une nouvelle commande commence.

La méthode `print()` affichera quelque chose.

Dans cet exemple, nous avons deux commandes qui afficheront les messages à l'intérieur des guillemets simples.
```python
print('First command')
print('Second command')
```

Sortie :
```
First command
Second command
```

Mais ce qui suit est **incorrect** à cause des points-virgules à la fin :

```python
print('First command');
print('Second command');
```

## Indentation

De nombreux langages utilisent des accolades pour définir la portée. 

L'interpréteur Python utilise uniquement l'indentation pour définir quand une portée se termine et une autre commence.

Cela signifie que vous devez être conscient des espaces blancs au début de chaque ligne -- ils ont une signification et peuvent casser votre code s'ils sont mal placés.

Cette définition d'une fonction fonctionne :

```python
def my_function():
    print('First command')
```

Cela **ne fonctionne pas** parce que l'indentation de la deuxième ligne est manquante et générera une erreur :

```python
def my_function():
print('First command')
```

## Sensibilité à la casse et variables
Python est sensible à la casse. Donc les variables `name` et `Name` ne sont pas la même chose et stockent des valeurs différentes.

```python
name = 'Renan'
Name = 'Moura'
```

Comme vous pouvez le voir, les variables sont facilement créées en leur attribuant simplement des valeurs à l'aide du symbole `=`.

Cela signifie que `name` stocke 'Renan' et `Name` stocke 'Moura'.

## Commentaires

Enfin, pour commenter quelque chose dans votre code, utilisez le symbole de dièse `#`.

La partie commentée n'influence pas le flux du programme.

```python
# cette fonction imprime quelque chose
def my_function():
    print('First command')
```

Ceci n'était qu'un aperçu. Les détails de chacun de ceux-ci deviendront plus clairs dans les prochains chapitres avec des exemples et des explications plus larges.


# Commentaires
Le but des commentaires est d'expliquer ce qui se passe dans le code.

Les commentaires sont écrits avec votre code mais n'influencent pas le flux de votre programme.

Lorsque vous travaillez seul, peut-être que les commentaires ne semblent pas être quelque chose que vous devriez écrire. Après tout, à ce moment-là, vous connaissez les raisons de chaque ligne de code.

Mais que se passe-t-il si de nouvelles personnes rejoignent votre projet après un an et que le projet compte 3 modules, chacun avec 10 000 lignes de code ?

Pensez aux personnes qui ne savent rien de votre application et qui doivent soudainement la maintenir, la corriger ou ajouter de nouvelles fonctionnalités.

Rappelez-vous, il n'y a pas de solution unique pour un problème donné. Votre façon de résoudre les choses est la vôtre et la vôtre seulement. Si vous demandez à 10 personnes de résoudre le même problème, elles proposeront 10 solutions différentes.

Si vous voulez que les autres comprennent pleinement votre raisonnement, une bonne conception de code est obligatoire, mais les commentaires font partie intégrante de toute base de code.

## Comment écrire des commentaires en Python
La syntaxe des commentaires en Python est plutôt facile : utilisez simplement le symbole de dièse `#` devant le texte que vous voulez commenter.

```python
#Ceci est un commentaire et il n'influencera pas le flux de mon programme
```

Vous pouvez utiliser un commentaire pour expliquer ce que fait un morceau de code.

```python
#calcule la somme de deux nombres donnés
a + b
```

## Commentaires multilignes
Peut-être voulez-vous commenter quelque chose de très complexe ou décrire comment un processus fonctionne dans votre code.

Dans ces cas, vous pouvez utiliser des commentaires multilignes.

Pour cela, utilisez simplement un seul symbole de dièse `#` pour chaque ligne.

```python
#Tout ce qui suit le symbole de dièse # est un commentaire
#Ceci est un commentaire et il n'influencera pas le flux de mon programme

#Calcule le coût du projet donné les variables a et b
#a est le temps en mois qu'il faudra jusqu'à ce que le projet soit terminé
#b est combien d'argent cela coûtera par mois
a + b * 10 
```

# Variables
Dans tout programme, vous devez stocker et manipuler des données pour créer un flux ou une logique spécifique.

C'est à cela que servent les variables.

Vous pouvez avoir une variable pour stocker un nom, une autre pour stocker l'âge d'une personne, ou même utiliser un type plus complexe pour stocker tout cela à la fois comme un dictionnaire.

## Création, également connue sous le nom de Déclaration
Déclarer une variable est une opération basique et directe en Python

Choisissez simplement un nom et attribuez-lui une valeur en utilisant le symbole `=`.
```python
name='Bob'

age=32
```

Vous pouvez utiliser la fonction `print()` pour afficher la valeur d'une variable.
```python
print(name)

print(age)
```

```
Bob

32
```

Remarquez qu'en Python, il n'y a pas de mot spécial pour déclarer une variable.

Au moment où vous attribuez une valeur, la variable est créée en mémoire.

Python a également une typage dynamique, ce qui signifie que vous n'avez pas à lui dire si votre variable est un texte ou un nombre, par exemple.

L'interpréteur déduit le typage en fonction de la valeur attribuée.

Si vous en avez besoin, vous pouvez également redéclarer une variable simplement en changeant sa valeur.

```python
#déclaration de name comme une chaîne de caractères
name='Bob'
#redéclaration de name comme un entier
name = 32
```

Gardez à l'esprit, cependant, que cela n'est pas recommandé puisque les variables doivent avoir une signification et un contexte.

Si j'ai une variable appelée `name`, je ne m'attends pas à ce qu'elle contienne un nombre.

## Conventions de Nommage
Continuons à partir de la dernière section lorsque j'ai parlé de signification et de contexte.

N'utilisez pas de noms de variables aléatoires comme `x` ou `y`.

Disons que vous voulez stocker l'heure d'une fête, appelez-la simplement `party_time`.

Oh, avez-vous remarqué le trait de soulignement `_` ?

Par convention, si vous voulez utiliser un nom de variable composé de deux mots ou plus, vous les séparez par des traits de soulignement. Cela s'appelle le Snake Case.

Une autre option serait d'utiliser le CamelCase comme dans `partyTime`. Cela est très courant dans d'autres langages, mais ce n'est pas la convention en Python comme indiqué précédemment.

Les variables sont sensibles à la casse, donc `party_time` et `Party_time` ne sont pas les mêmes. De plus, gardez à l'esprit que la convention nous dit de toujours utiliser des minuscules.

Rappelez-vous, utilisez des noms que vous pouvez facilement rappeler dans votre programme. Un mauvais nommage peut vous coûter beaucoup de temps et causer des bugs ennuyeux.

En résumé, les noms de variables :

* Sont sensibles à la casse : `time` et `TIME` ne sont pas les mêmes
* Doivent commencer par un trait de soulignement `_` ou une lettre (NE COMMENCEZ PAS par un nombre)
* Sont autorisés à avoir uniquement des nombres, des lettres et des traits de soulignement. Aucun caractère spécial comme : #, $, &, @, etc.

Cela, par exemple, n'est **pas** autorisé : `party#time`, `10partytime`.


# Types

Pour stocker des données en Python, vous devez utiliser une variable. Et chaque variable a son type en fonction de la valeur des données stockées.

Python a un typage dynamique, ce qui signifie que vous n'avez pas à déclarer explicitement le type de votre variable -- mais si vous le souhaitez, vous pouvez.

Les listes, les tuples, les ensembles et les dictionnaires sont tous des types de données et ont des sections dédiées plus tard avec plus de détails, mais nous allons les examiner brièvement ici. 

De cette façon, je peux vous montrer les aspects les plus importants et les opérations de chacun dans leur propre section tout en gardant cette section plus concise et axée sur vous donner une vue d'ensemble des principaux types de données en Python.

## Détermination du Type
Tout d'abord, apprenons à déterminer le type de données.

Utilisez simplement la fonction `type()` et passez la variable de votre choix comme argument, comme dans l'exemple ci-dessous.

```python
print(type(my_variable))
```

## Booléen

Le type booléen est l'un des types de programmation les plus basiques.

Une variable de type booléen ne peut représenter que soit _True_ soit _False_.

```python
my_bool = True
print(type(my_bool))

my_bool = bool(1024)
print(type(my_bool))
```

```
<class 'bool'>
<class 'bool'>
```

## Nombres

Il existe trois types de types numériques : int, float et complex.

### Entier
```python
my_int = 32
print(type(my_int))

my_int = int(32)
print(type(my_int))
```

```
<class 'int'>
<class 'int'>
```

### Float
```python
my_float = 32.85
print(type(my_float))

my_float = float(32.85)
print(type(my_float))
```

```
<class 'float'>
<class 'float'>
```

### Complexe
```python
my_complex_number = 32+4j
print(type(my_complex_number))

my_complex_number = complex(32+4j)
print(type(my_complex_number))
```

```
<class 'complex'>
<class 'complex'>
```


## Chaîne de caractères

Le type texte est l'un des types les plus courants et est souvent appelé _string_ ou, en Python, simplement `str`.

```python
my_city = "New York"
print(type(my_city))

#Les guillemets simples ont exactement
#la même utilisation que les guillemets doubles
my_city = 'New York'
print(type(my_city))

#Définir explicitement le type de variable
my_city = str("New York")
print(type(my_city))
```

```
<class 'str'>
<class 'str'>
<class 'str'>
```

Vous pouvez utiliser l'opérateur `+` pour concaténer des chaînes de caractères.

La concaténation est lorsque vous avez deux chaînes de caractères ou plus et que vous souhaitez les joindre en une seule.

```python
word1 = 'New '
word2 = 'York'

print(word1 + word2)
```

```
New York
```

Le type chaîne de caractères a de nombreuses méthodes intégrées qui nous permettent de les manipuler. Je vais démontrer comment certaines de ces méthodes fonctionnent.

La fonction `len()` retourne la longueur d'une chaîne de caractères.

```python
print(len('New York'))
```

```
8
```

La méthode `replace()` remplace une partie de la chaîne de caractères par une autre. Par exemple, remplaçons 'New' par 'Old'.

```python
print('New York'.replace('New', 'Old'))
```

```
Old York
```

La méthode `upper()` retournera tous les caractères en majuscules.

```python
print('New York'.upper())
```

```
NEW YORK
```

La méthode `lower()` fait l'inverse et retourne tous les caractères en minuscules.

```python
print('New York'.lower())
```

```
new york
```

## Listes

Une liste a ses éléments ordonnés et vous pouvez ajouter le même élément autant de fois que vous le souhaitez. Un détail important est que les listes sont mutables.

La mutabilité signifie que vous pouvez modifier une liste après sa création en ajoutant des éléments, en les supprimant ou même en changeant simplement leurs valeurs. Ces opérations seront démontrées plus tard dans la section dédiée aux Listes.

```python
my_list = ["bmw", "ferrari", "maclaren"]
print(type(my_list))

my_list = list(("bmw", "ferrari", "maclaren"))
print(type(my_list))
```

```
<class 'list'>
<class 'list'>
```

## Tuples

Un tuple est similaire à une liste : ordonné et permet la répétition des éléments.

Il y a juste une différence : un tuple est immutable.

L'immuabilité signifie que vous ne pouvez pas modifier un tuple après sa création. Si vous essayez d'ajouter un élément ou de le mettre à jour, par exemple, l'interpréteur Python vous montrera une erreur. Je montrerai que ces erreurs se produisent plus tard dans la section dédiée aux Tuples.

```python
my_tuple = ("bmw", "ferrari", "maclaren")
print(type(my_tuple))

my_tuple = tuple(("bmw", "ferrari", "maclaren"))
print(type(my_tuple))
```

```
<class 'tuple'>
<class 'tuple'>
```

## Ensembles

Les ensembles ne garantissent pas l'ordre des éléments et ne sont pas indexés.

Un point clé lors de l'utilisation des ensembles : ils ne permettent pas la répétition d'un élément.


```python
my_set = {"bmw", "ferrari", "maclaren"}
print(type(my_set))


my_set = set(("bmw", "ferrari", "maclaren"))
print(type(my_set))
```

```
<class 'set'>
<class 'set'>
```
## Dictionnaires

Un dictionnaire ne garantit pas l'ordre des éléments et est mutable.

Une caractéristique importante des dictionnaires est que vous pouvez définir vos propres clés d'accès pour chaque élément.

```python
my_dict = {"country" : "France", "worldcups" : 2}
print(type(my_dict))

my_dict = dict(country="France", worldcups=2)
print(type(my_dict))
```

```
<class 'dict'>
<class 'dict'>
```


# Conversion de Types
La conversion de types vous permet de convertir entre différents types.

De cette façon, vous pouvez avoir un `int` transformé en `str`, ou un `float` transformé en `int`, par exemple.

## Conversion Explicite
Pour convertir une variable en chaîne de caractères, utilisez simplement la fonction `str()`.
```python
# ceci est juste une initialisation explicite régulière
my_str = str('32') 
print(my_str)

# int vers str
my_str = str(32) 
print(my_str)

# float vers str
my_str = str(32.0)
print(my_str)
```

```
32
32
32.0
```

Pour convertir une variable en entier, utilisez simplement la fonction `int()`.
```python
# ceci est juste une initialisation explicite régulière
my_int = int(32) 
print(my_int)

# float vers int : arrondi à 3
my_int = int(3.2) 
print(my_int)

# str vers int
my_int = int('32') 
print(my_int)
```

```
32
3
32
```

Pour convertir une variable en float, utilisez simplement la fonction `float()`.
```python
# ceci est une initialisation explicite
my_float = float(3.2)   
print(my_float)

# int vers float
my_float = float(32)     
print(my_float)

# str vers float
my_float = float('32')  
print(my_float)
```

```
3.2
32.0
32.0
```

Ce que j'ai fait ci-dessus s'appelle une conversion de type _explicite_.

Dans certains cas, vous n'avez pas besoin de faire la conversion explicitement, car Python peut le faire par lui-même.

## Conversion Implicite
L'exemple ci-dessous montre la conversion implicite lors de l'addition d'un `int` et d'un `float`.

Remarquez que `my_sum` est `float`. Python utilise `float` pour éviter la perte de données puisque le type `int` ne peut pas représenter les chiffres décimaux.
```python
my_int = 32
my_float = 3.2

my_sum = my_int + my_float

print(my_sum)

print(type(my_sum))
```

```
35.2
<class 'float'>
```

En revanche, dans cet exemple, lorsque vous ajoutez un `int` et un `str`, Python ne pourra pas faire la conversion implicite, et la conversion de type explicite est nécessaire.
```python
my_int = 32
my_str = '32'

# la conversion explicite fonctionne
my_sum = my_int + int(my_str)
print(my_sum)

# la conversion implicite génère une erreur
my_sum = my_int + my_str 
```

```
64

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

La même erreur est générée lorsque vous essayez d'ajouter des types `float` et `str` sans faire de conversion explicite.
```python
my_float = 3.2
my_str = '32'

# la conversion explicite fonctionne
my_sum = my_float + float(my_str)
print(my_sum)

# la conversion implicite génère une erreur
my_sum = my_float + my_str 
```

```
35.2

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'str'
```

# Saisie Utilisateur

Si vous devez interagir avec un utilisateur lors de l'exécution de votre programme dans la ligne de commande (par exemple, pour demander une information), vous pouvez utiliser la fonction `input()`.

```python
country = input("Quel est votre pays ? ") #l'utilisateur entre 'Brésil'

print(country)
```

```
Brésil
```

La valeur capturée est toujours `string`. N'oubliez pas que vous devrez peut-être la convertir en utilisant la conversion de types.

```python
age = input("Quel âge avez-vous ? ") #l'utilisateur entre '29'

print(age)

print(type(age))

age = int(age)

print(type(age))
```

La sortie pour chaque `print()` est :
```
29

<class 'str'>

<class 'int'>
```

Remarquez que l'âge 29 est capturé en tant que `string` puis converti explicitement en `int`.


# Opérateurs
Dans un langage de programmation, les opérateurs sont des symboles spéciaux que vous pouvez appliquer à vos variables et valeurs afin d'effectuer des opérations telles que l'arithmétique/les mathématiques et la comparaison.

Python a de nombreux opérateurs que vous pouvez appliquer à vos variables et je vais démontrer les plus utilisés.

## Opérateurs Arithmétiques

Les opérateurs arithmétiques sont le type d'opérateurs le plus courant et aussi les plus reconnaissables.

Ils vous permettent d'effectuer des opérations mathématiques simples.

Ils sont :

* `+`: Addition
* `-`: Soustraction
* `*`: Multiplication
* `/`: Division
* `**`: Exponentiation
* `//`: Division entière, arrondit le résultat d'une division
* `%`: Modulo, donne le reste d'une division

Voyons un programme qui montre comment chacun d'eux est utilisé.

```python
print('Addition:', 5 + 2)
print('Soustraction:', 5 - 2)
print('Multiplication:', 5 * 2)
print('Division:', 5 / 2)
print('Division entière:', 5 // 2)
print('Exponentiation:', 5 ** 2)
print('Modulo:', 5 % 2)
```

```
Addition: 7

Soustraction: 3

Multiplication: 10

Division: 2.5

Division entière: 2

Exponentiation: 25

Modulo: 1
```

### Concaténation
La concaténation est lorsque vous avez deux chaînes de caractères ou plus et que vous souhaitez les joindre en une seule.

Cela est utile lorsque vous avez des informations dans plusieurs variables et que vous souhaitez les combiner.

Par exemple, dans cet exemple suivant, je combine deux variables qui contiennent mon prénom et mon nom de famille respectivement pour avoir mon nom complet.

L'opérateur `+` est également utilisé pour concaténer.

```python
first_name = 'Renan '
last_name = 'Moura'

print(first_name + last_name)
```

```
Renan Moura
```

Puisque la concaténation est appliquée aux chaînes de caractères, pour concaténer des chaînes de caractères avec d'autres types, vous devez faire une conversion de type explicite en utilisant `str()`.

Je dois convertir la valeur `int` 30 en chaîne de caractères avec `str()` pour la concaténer avec le reste de la chaîne de caractères.

```python
age = 'J'ai ' + str(30) + ' ans'

print(age)
```

```
J'ai 30 ans
```
## Opérateurs de Comparaison

Utilisez les opérateurs de comparaison pour comparer deux valeurs.

Ces opérateurs retournent soit `True` soit `False`.

Ils sont :

* `==`: Égal
* `!=`: Différent
* `>`: Supérieur à
* `<`: Inférieur à
* `>=`: Supérieur ou égal à
* `<=`: Inférieur ou égal à

Voyons un programme qui montre comment chacun d'eux est utilisé.

```python
print('Égal:', 5 == 2)
print('Différent:', 5 != 2)
print('Supérieur à:', 5 > 2)
print('Inférieur à:', 5 < 2)
print('Supérieur ou égal à:', 5 >= 2)
print('Inférieur ou égal à:', 5 <= 2)
```

```
Égal: False

Différent: True

Supérieur à: True

Inférieur à: False

Supérieur ou égal à: True

Inférieur ou égal à: False
```

## Opérateurs d'Affectation
Comme le nom l'indique, ces opérateurs sont utilisés pour affecter des valeurs aux variables.

`x = 7` dans le premier exemple est une affectation directe stockant le nombre `7` dans la variable `x`.

L'opération d'affectation prend la valeur à droite et l'affecte à la variable à gauche.

Les autres opérateurs sont des raccourcis simples pour les opérateurs arithmétiques.

Dans le deuxième exemple, `x` commence avec `7` et `x += 2` est juste une autre façon d'écrire `x = x + 2`. Cela signifie que la valeur précédente de `x` est ajoutée à `2` et réaffectée à `x` qui est maintenant égale à `9`.

* `=`: affectation simple
```python
x = 7
print(x)
```
```
7
```

* `+=`: addition et affectation
```python
x = 7
x += 2
print(x)
```
```
9
```

* `-=`: soustraction et affectation
```python
x = 7
x -= 2
print(x)
```
```
5
```

* `*=`: multiplication et affectation
```python
x = 7
x *= 2
print(x)
```
```
14
```

* `/=`: division et affectation
```python
x = 7
x /= 2
print(x)
```
```
3.5
```

* `%=`: modulo et affectation
```python
x = 7
x %= 2
print(x)
```

```
1
```

* `//=`: division entière et affectation
```python
x = 7
x //= 2
print(x)
```
```
3
```

* `**=`: exponentiation et affectation
```python
x = 7
x **= 2
print(x)
```
```
49
```

## Opérateurs Logiques
Les opérateurs logiques sont utilisés pour combiner des déclarations en appliquant l'algèbre booléenne.

Ils sont :

* `and`: `True` uniquement lorsque les deux déclarations sont vraies
* `or`: `False` uniquement lorsque x et y sont faux
* `not`: L'opérateur `not` inverse simplement l'entrée, `True` devient `False` et vice versa.

Voyons un programme qui montre comment chacun est utilisé.

```python
x = 5
y = 2

print(x == 5 and y > 3) 
  
print(x == 5 or y > 3) 
  
print(not (x == 5))
```

```
False

True

False
```

## Opérateurs d'Appartenance

Ces opérateurs fournissent un moyen facile de vérifier si un certain objet est présent dans une séquence : `string`, `list`, `tuple`, `set`, et `dictionary`.

Ils sont :
* `in`: retourne `True` si l'objet est présent
* `not in`: retourne `True` si l'objet n'est pas présent

Voyons un programme qui montre comment chacun est utilisé.

```python
number_list = [1, 2, 4, 5, 6]

print( 1 in number_list)

print( 5 not in number_list)

print( 3 not in number_list)
```

```
True

False

True
```


# Conditionnelles
Les conditionnelles sont l'un des piliers de tout langage de programmation.

Elles vous permettent de contrôler le flux du programme selon des conditions spécifiques que vous pouvez vérifier.

## L'instruction `if`
La manière dont vous implémentez une conditionnelle est à travers l'instruction `if`.

La forme générale d'une instruction `if` est :

```python
if expression:
    statement
```

L'`expression` contient une logique qui retourne un booléen, et le `statement` est exécuté uniquement si le retour est `True`.

Un exemple simple :

```python
bob_age = 32
sarah_age = 29

if bob_age > sarah_age:
    print('Bob est plus âgé que Sarah')
```

```
Bob est plus âgé que Sarah
```

Nous avons deux variables indiquant les âges de Bob et Sarah. La condition en anglais simple dit "si l'âge de Bob est supérieur à l'âge de Sarah, alors imprime la phrase 'Bob est plus âgé que Sarah'".

Puisque la condition retourne `True`, la phrase sera imprimée sur la console.

## Les instructions `if else` et `elif`
Dans notre dernier exemple, le programme ne fait quelque chose que si la condition retourne `True`.

Mais nous voulons aussi qu'il fasse quelque chose si elle retourne `False` ou même vérifier une deuxième ou troisième condition si la première n'était pas remplie.

Dans cet exemple, nous avons échangé les âges de Bob et Sarah. La première condition retournera `False` puisque Sarah est plus âgée maintenant, et ensuite le programme imprimera la phrase après le `else` à la place.

```python
bob_age = 29
sarah_age = 32

if bob_age > sarah_age:
    print('Bob est plus âgé que Sarah')
else:
    print('Bob est plus jeune que Sarah')
```

```
Bob est plus jeune que Sarah
```

Maintenant, considérons l'exemple ci-dessous avec le `elif`.

```python
bob_age = 32
sarah_age = 32

if bob_age > sarah_age:
    print('Bob est plus âgé que Sarah')
elif bob_age == sarah_age:
    print('Bob et Sarah ont le même âge')
else:
    print('Bob est plus jeune que Sarah')
```

```
Bob et Sarah ont le même âge
```

Le but du `elif` est de fournir une nouvelle condition à vérifier avant que le `else` ne soit exécuté.

Une fois de plus, nous avons changé leurs âges et maintenant ils ont tous les deux 32 ans.

Ainsi, la condition dans le `elif` est remplie. Puisqu'ils ont le même âge, le programme imprimera "Bob et Sarah ont le même âge".

Remarquez que vous pouvez avoir autant de `elif` que vous le souhaitez, il suffit de les mettre en séquence.

```python
bob_age = 32
sarah_age = 32

if bob_age > sarah_age:
    print('Bob est plus âgé que Sarah')
elif bob_age < sarah_age:
    print('Bob est plus jeune que Sarah')
elif bob_age == sarah_age:
    print('Bob et Sarah ont le même âge')
else:
    print('Celui-ci n'est jamais exécuté')
```

```
Bob et Sarah ont le même âge
```

Dans cet exemple, le `else` n'est jamais exécuté car toutes les possibilités sont couvertes dans les conditions précédentes et pourrait donc être supprimé.

## Conditionnelles imbriquées
Vous pourriez avoir besoin de vérifier plus d'une conditionnelle pour que quelque chose se produise.

Dans ce cas, vous pouvez imbriquer vos instructions `if`.

Par exemple, la deuxième phrase "Bob est le plus âgé" n'est imprimée que si les deux `if` sont validés.

```python
bob_age = 32
sarah_age = 28
mary_age = 25

if bob_age > sarah_age:
    print('Bob est plus âgé que Sarah')
    if bob_age > mary_age:
        print('Bob est le plus âgé')
```

```
Bob est plus âgé que Sarah
Bob est le plus âgé
```

Ou, selon la logique, le rendre plus simple avec l'algèbre booléenne.

De cette façon, votre code est plus petit, plus lisible et plus facile à maintenir.

```python
bob_age = 32
sarah_age = 28
mary_age = 25

if bob_age > sarah_age and bob_age > mary_age:
    print('Bob est le plus âgé')
```

```
Bob est le plus âgé
```

## Opérateurs Ternaires

L'opérateur ternaire est une instruction `if` sur une seule ligne.

C'est très pratique pour des conditions simples.

Voici à quoi il ressemble :

```python
<expression> if <condition> else <expression>
```

Considérons le code Python suivant :

```python
a = 25
b = 50
x = 0
y = 1

result = x if a > b else y

print(result)
```

```
1
```

Ici, nous utilisons quatre variables, `a` et `b` sont pour la condition, tandis que `x` et `y` représentent les expressions.

`a` et `b` sont les valeurs que nous comparons pour évaluer une condition. Dans ce cas, nous vérifions si `a` est supérieur à `b`.

Si l'expression est vraie, c'est-à-dire, `a` est supérieur à `b`, alors la valeur de `x` sera attribuée à `result` qui sera égale à 0.

Cependant, si `a` est inférieur à `b`, alors nous avons la valeur de `y` assignée à `result`, et `result` contiendra la valeur `1`.

Puisque `a` est inférieur à `b`, 25 < 50, `result` aura `1` comme valeur finale de `y`.

La manière facile de se souvenir de la façon dont la condition est évaluée est de la lire en anglais simple.

Notre exemple se lirait : `result` sera `x` si `a` est supérieur à `b` sinon `y`.


# Listes
Comme promis dans la section [Types](#heading-types), cette section et les trois suivantes sur les Tuples, Ensembles et Dictionnaires auront des explications plus approfondies de chacun d'eux puisqu'ils sont très importants et largement utilisés dans Python pour organiser et traiter les données.

Une liste a ses éléments ordonnés et vous pouvez ajouter le même élément autant de fois que vous le souhaitez. 

Un détail important est que les listes sont mutables.

La mutabilité signifie que vous pouvez modifier une liste après sa création en ajoutant des éléments, en les supprimant ou même en changeant simplement leurs valeurs.

### Initialisation

#### Liste vide
```python
people = []
```

#### Liste avec des valeurs initiales
```python
people = ['Bob', 'Mary']
```

### Ajout dans une Liste
Pour ajouter un élément à la fin d'une liste, utilisez `append()`.

```python
people = ['Bob', 'Mary']
people.append('Sarah')

print(people)
```

```
['Bob', 'Mary', 'Sarah']
```

Pour spécifier la position du nouvel élément, utilisez la méthode `insert()`.
```python
people = ['Bob', 'Mary']
people.insert(0, 'Sarah')

print(people)
```

```
['Sarah', 'Bob', 'Mary']
```

### Mise à jour dans une Liste
Spécifiez la position de l'élément à mettre à jour et définissez la nouvelle valeur

```python
people = ['Bob', 'Mary']
people[1] = 'Sarah'
print(people)
```

```
['Bob', 'Sarah']
```

### Suppression dans une Liste
Utilisez la méthode `remove()` pour supprimer l'élément donné comme argument.

```python
people = ['Bob', 'Mary']
people.remove('Bob')
print(people)
```

```
['Mary']
```

Pour tout supprimer, utilisez la méthode `clear()` :

```python
people = ['Bob', 'Mary']
people.clear()
```

### Récupération dans une Liste

Utilisez l'index pour référencer l'élément.

Rappelez-vous que l'index commence à 0.

Donc pour accéder au deuxième élément, utilisez l'index 1.
```python
people = ['Bob', 'Mary']
print(people[1])
``` 

```
Mary
```

### Vérifier si un élément donné existe déjà dans une Liste

```python
people = ['Bob', 'Mary']

if 'Bob' in people:
  print('Bob existe !')
else:
  print('Il n'y a pas de Bob !')
```


# Tuples

Un tuple est similaire à une liste : il est ordonné et permet la répétition des éléments.

Il y a juste une différence : un tuple est immutable.

L'immuabilité, si vous vous souvenez, signifie que vous ne pouvez pas modifier un tuple après sa création. Si vous essayez d'ajouter un élément ou de le mettre à jour, par exemple, l'interpréteur Python vous montrera une erreur.

### Initialisation

#### Tuple vide
```python
people = ()
```

#### Tuple avec des valeurs initiales
```python
people = ('Bob', 'Mary')
```

### Ajout dans un Tuple

Les tuples sont immutables. Cela signifie que si vous essayez d'ajouter un élément, vous verrez une erreur.

```python
people = ('Bob', 'Mary')
people[2] = 'Sarah'
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

### Mise à jour dans un Tuple

La mise à jour d'un élément retournera également une erreur.

Mais il y a une astuce : vous pouvez le convertir en une liste, changer l'élément, puis le reconvertir en un tuple.

```python
people = ('Bob', 'Mary')
people_list = list(people)
people_list[1] = 'Sarah'
people = tuple(people_list)
print(people)
```

```
('Bob', 'Sarah')
```

### Suppression dans un Tuple

Pour la même raison que vous ne pouvez pas ajouter un élément, vous ne pouvez pas non plus supprimer un élément, car ils sont immutables.

### Récupération dans un Tuple

Utilisez l'index pour référencer l'élément.

```python
people = ('Bob', 'Mary')
print(people[1])
``` 

```
Mary
```

### Vérifier si un élément donné existe déjà dans un Tuple

```python
people = ('Bob', 'Mary')

if 'Bob' in people:
  print('Bob existe !')
else:
  print('Il n'y a pas de Bob !')
```


# Ensembles

Les ensembles ne garantissent pas l'ordre des éléments et ne sont pas indexés.

Un point clé lors de l'utilisation des ensembles : ils ne permettent pas la répétition d'un élément.

### Initialisation

#### Ensemble vide
```python
people = set()
```

#### Ensemble avec des valeurs initiales
```python
people = {'Bob', 'Mary'}
```

### Ajout dans un Ensemble

Utilisez la méthode `add()` pour ajouter un élément.

```python
people.add('Sarah')
```

Utilisez la méthode `update()` pour ajouter plusieurs éléments à la fois.

```python
people.update(['Carol', 'Susan'])
```

Rappelez-vous, les ensembles ne permettent pas la répétition, donc si vous ajoutez 'Mary' à nouveau, rien ne change.

```python
people = {'Bob', 'Mary'}

people.add('Mary')

print(people)
```

```
{'Bob', 'Mary'}
```

### Mise à jour dans un Ensemble

Les éléments d'un ensemble ne sont pas mutables. Vous devez soit ajouter soit supprimer un élément.

### Suppression dans un Ensemble

Pour supprimer Bob du dictionnaire :

```python
people = {'Bob', 'Mary'}
people.remove('Bob')
print(people)
```

```
{'Mary'}
```

Pour tout supprimer :

```python
people.clear()
```

### Vérifier si un élément donné existe déjà dans un ensemble

```python
people = {'Bob', 'Mary'}

if 'Bob' in people:
  print('Bob existe !')
else:
  print('Il n'y a pas de Bob !')
```


# Dictionnaires

Le dictionnaire ne garantit pas l'ordre des éléments et il est mutable.

Une caractéristique importante des dictionnaires est que vous pouvez définir vos propres clés d'accès personnalisées pour chaque élément.

### Initialisation d'un Dictionnaire

#### Dictionnaire vide
```python
people = {}
```

#### Dictionnaire avec des valeurs initiales
```python
people = {'Bob':30, 'Mary':25}
```

### Ajout dans un Dictionnaire

Si la clé n'existe pas encore, elle est ajoutée au dictionnaire.

```python
people['Sarah']=32
```

### Mise à jour d'un Dictionnaire

Si la clé existe déjà, la valeur est simplement mise à jour.
```python
#L'âge de Bob est maintenant 28
people['Bob']=28
```

Remarquez que le code est presque le même.

### Suppression dans un Dictionnaire

Pour supprimer Bob du dictionnaire :

```python
people.pop('Bob')
```

Pour tout supprimer :

```python
people.clear()
```

### Récupération dans un Dictionnaire

```python
bob_age = people['Bob']
print(bob_age)
```

```
30
```

### Vérifier si une clé donnée existe déjà dans un Dictionnaire

```python
if 'Bob' in people:
  print('Bob existe !')
else:
  print('Il n'y a pas de Bob !')
```


# Boucles `while`

Les boucles sont utilisées lorsque vous devez répéter un bloc de code un certain nombre de fois ou appliquer la même logique à chaque élément d'une collection.

Il existe deux types de boucles : `for` et `while`.

Vous apprendrez à propos des boucles `for` dans la section suivante.

## Syntaxe de base
La syntaxe de base d'une boucle `while` est la suivante.
```python
while condition:
    statement
```

La boucle continuera *tant que* la condition est `True`.

## Le carré d'un nombre est
L'exemple ci-dessous prend chaque valeur de `number` et calcule sa valeur au carré.
```python
number = 1
while number <= 5:
    print(number, 'au carré est', number**2)
    number = number + 1
```

```
1 au carré est 1
2 au carré est 4
3 au carré est 9
4 au carré est 16
5 au carré est 25
```

Vous pouvez utiliser n'importe quel nom de variable, mais j'ai choisi `number` parce que cela a du sens dans le contexte. Un choix générique courant serait simplement `i`.

La boucle continuera jusqu'à ce que `number` (initialisé avec 1) soit inférieur ou égal à 5.

Remarquez qu'après la commande `print()`, la variable `number` est incrémentée de 1 pour prendre la valeur suivante.

Si vous ne faites pas l'incrémentation, vous aurez une boucle infinie puisque `number` n'atteindra jamais une valeur supérieure à 5. C'est un détail très important !

## Bloc `else`
Lorsque la condition retourne `False`, le bloc `else` sera appelé.

```python
number = 1
while number <= 5:
    print(number, 'au carré est', number**2)
    number = number + 1
else:
    print('Plus de nombres !')
```

```
1 au carré est 1
2 au carré est 4
3 au carré est 9
4 au carré est 16
5 au carré est 25
Plus de nombres !
```

Remarquez que la phrase 'Plus de nombres !' est imprimée après la fin de la boucle, c'est-à-dire après que la condition `number <= 5` évalue à `False`.

## Comment sortir d'une boucle `while` en Python
Utilisez simplement le mot-clé `break`, et la boucle arrêtera son exécution.
```python
number = 1
while number <= 5:
    print(number, 'au carré est', number**2)
    number = number + 1
    if number == 4:
        break
```

```
1 au carré est 1
2 au carré est 4
3 au carré est 9
```

La boucle s'exécute normalement, et lorsque `number` atteint 4, l'instruction `if` évalue à `True` et la commande `break` est appelée. Cela termine la boucle avant que la valeur au carré des nombres 4 et 5 ne soit calculée.

## Comment ignorer un élément dans une boucle `while`
Le `continue` le fera pour vous.

J'ai dû inverser l'ordre de l'instruction `if` et du `print()` pour montrer comment cela fonctionne correctement.

```python
number = 0
while number < 5:
    number = number + 1
    if number == 4:
        continue
    print(number, 'au carré est', number**2)
```

```
1 au carré est 1
2 au carré est 4
3 au carré est 9
5 au carré est 25
```

Le programme vérifie toujours si 4 est la valeur actuelle de `number`. Si c'est le cas, le carré de 4 ne sera pas calculé et le `continue` passera à l'itération suivante lorsque la valeur de `number` sera 5.
* 

# Boucles `for`

Les boucles `for` sont similaires aux boucles `while` dans le sens où elles sont utilisées pour répéter des blocs de code.

La différence la plus importante est que vous pouvez facilement itérer sur des types séquentiels.

## Syntaxe de base
La syntaxe de base d'une boucle `for` est la suivante.

```python
for item in collection:
    statement
```

## Boucle sur une liste
Pour boucler sur une liste ou toute autre collection, procédez comme indiqué dans l'exemple ci-dessous.

```python
cars = ['BMW', 'Ferrari', 'McLaren']
for car in cars:
    print(car)
```

```
BMW
Ferrari
McLaren
```

La liste des `cars` contient trois éléments. La boucle `for` itérera sur la liste et stockera chaque élément dans la variable `car`, puis exécutera une instruction, dans ce cas `print(car)`, pour imprimer chaque voiture dans la console.

## Fonction `range()`
La fonction range est largement utilisée dans les boucles for car elle vous donne un moyen simple de lister des nombres.

Ce code bouclera à travers les nombres 0 à 5 et imprimera chacun d'eux.
```python
for number in range(5):
    print(number)
```

```
0
1
2
3
4
```

En revanche, sans la fonction `range()`, nous ferions quelque chose comme ceci.
```python
numbers = [0, 1, 2, 3, 4]
for number in numbers:
    print(number)
```

```
0
1
2
3
4
```

Vous pouvez également définir un `start` et un `stop` en utilisant `range()`.

Ici, nous commençons à 5 et nous arrêtons à 10. Le nombre que vous définissez pour stop n'est pas inclus.

```python
for number in range(5, 10):
    print(number)

```

```
5
6
7
8
9
```

Enfin, il est également possible de définir un pas.

Ici, nous commençons à 10 et nous incrémentons de 2 jusqu'à 20, puisque 20 est le `stop`, il n'est pas inclus.

```python
for number in range(10, 20, 2):
    print(number)
```

```
10
12
14
16
18
```

## Bloc `else`
Lorsque les éléments de la liste sont épuisés, le bloc `else` sera appelé.

```python
cars = ['BMW', 'Ferrari', 'McLaren']
for car in cars:
    print(car)
else:
    print('Plus de voitures !')
```

```
BMW
Ferrari
McLaren
Plus de voitures !
```

## Comment sortir d'une boucle for en Python
Utilisez simplement le mot-clé `break`, et la boucle arrêtera son exécution.

```python
cars = ['BMW', 'Ferrari', 'McLaren']
for car in cars:
    print(car)
    if car == 'Ferrari':
        break
```

```
BMW
Ferrari
```

La boucle itérera à travers la liste et imprimera chaque voiture.

Dans ce cas, après que la boucle atteint 'Ferrari', le `break` est appelé et 'McLaren' ne sera pas imprimé.

## Comment ignorer un élément dans une boucle for
Dans cette section, nous apprendrons comment `continue` peut le faire pour vous.

J'ai dû inverser l'ordre de l'instruction `if` et du `continue` pour montrer comment cela fonctionne correctement.

Remarquez que je vérifie toujours si 'Ferrari' est l'élément actuel. Si c'est le cas, 'Ferrari' ne sera pas imprimé, et le `continue` passera à l'élément suivant 'McLaren'.

```python
cars = ['BMW', 'Ferrari', 'McLaren']
for car in cars:
    if car == 'Ferrari':
        continue
    print(car)
```

```
BMW
McLaren
```

## Boucle dans une Boucle : Boucles Imbriquées
Parfois, vous avez des collections plus complexes, comme une liste de listes.

Pour itérer sur ces listes, vous avez besoin de boucles `for` imbriquées.

Dans ce cas, j'ai trois listes : une des modèles BMW, une autre des modèles Ferrari, et enfin une avec les modèles McLaren.

La première boucle itère sur chaque liste de marque, et la seconde itérera sur les modèles de chaque marque.

```python
car_models = [ 
['BMW I8', 'BMW X3', 
'BMW X1'], 
['Ferrari 812', 'Ferrari F8', 
'Ferrari GTC4'], 
['McLaren 570S', 'McLaren 570GT', 
'McLaren 720S']
]

for brand in car_models:
    for model in brand:
        print(model)
```

```
BMW I8
BMW X3
BMW X1
Ferrari 812
Ferrari F8
Ferrari GTC4
McLaren 570S
McLaren 570GT
McLaren 720S
```

## Boucle sur d'autres Structures de Données
La même logique qui s'applique aux boucles `for` sur une `list` peut être étendue aux autres structures de données : `tuple`, `set`, et `dictionary`.

Je vais brièvement démontrer comment faire une boucle de base sur chacune d'entre elles.

### Boucle sur un Tuple

```python
people = ('Bob', 'Mary')

for person in people:
  print(person)
```

```
Bob
Mary
```

### Boucle sur un Set

```python
people = {'Bob', 'Mary'}

for person in people:
  print(person)
```

```
Bob
Mary
```

### Boucle sur un Dictionnaire

Pour imprimer les clés :
```python
people = {'Bob':30, 'Mary':25}

for person in people:
  print(person)
```

```
Bob
Mary
```

Pour imprimer les valeurs :
```python
people = {'Bob':30, 'Mary':25}

for person in people:
  print(people[person])
```

```
30
25
```


# Fonctions

À mesure que le code grandit, la complexité grandit également. Et les fonctions aident à organiser le code.

Les fonctions sont un moyen pratique de créer des blocs de code que vous pouvez réutiliser.

## Définition et Appel

En Python, utilisez le mot-clé `def` pour définir une fonction.

Donnez-lui un nom et utilisez des parenthèses pour indiquer 0 ou plusieurs arguments.

Dans la ligne suivant la déclaration, n'oubliez pas d'indenter le bloc de code.

Voici un exemple de fonction appelée `print_first_function()` qui imprime simplement une phrase 'Ma première fonction !'.

Pour appeler la fonction, utilisez simplement son nom tel que défini.

```python
def print_first_function():
    print('Ma première fonction !')

print_first_function()
```

```-
Ma première fonction !
```

## `return` une valeur

Utilisez le mot-clé `return` pour retourner une valeur de la fonction.

Dans cet exemple, la fonction `second_function()` retourne la chaîne de caractères 'Ma deuxième fonction !'.

Remarquez que `print()` est une fonction intégrée et que notre fonction est appelée de l'intérieur.

La chaîne de caractères retournée par `second_function()` est passée comme argument à la fonction `print()`.

```python
def second_function():
    return 'Ma deuxième fonction !'

print(second_function())
```

```
Ma deuxième fonction !
```

## `return` plusieurs valeurs

Les fonctions peuvent également retourner plusieurs valeurs à la fois.

`return_numbers()` retourne deux valeurs simultanément.

```python
def return_numbers():
    return 10, 2

print(return_numbers())
```

```
(10, 2)
```


## Arguments

Vous pouvez définir des paramètres entre les parenthèses.

Lorsque vous appelez une fonction avec des paramètres, vous devez passer des arguments selon les paramètres définis.

Les exemples précédents n'avaient pas de paramètres, donc il n'y avait pas besoin d'arguments. Les parenthèses sont restées vides lorsque les fonctions étaient appelées.

### Un Argument

Pour spécifier un paramètre, définissez-le simplement à l'intérieur des parenthèses.

Dans cet exemple, la fonction `my_number` attend un nombre comme argument défini par le paramètre `num`.

La valeur de l'argument est alors accessible à l'intérieur de la fonction pour être utilisée.

```python
def my_number(num):
    return 'Mon nombre est : ' + str(num)

print(my_number(10))
```

```
Mon nombre est : 10
```

### Deux ou plusieurs Arguments

Pour définir plus de paramètres, utilisez simplement une virgule pour les séparer.

Ici, nous avons une fonction qui additionne deux nombres appelée `add`. Elle attend deux arguments définis par `first_num` et `second_num`.

Les arguments sont additionnés par l'opérateur `+` et le résultat est ensuite retourné par le `return`.

```python
def add(first_num, second_num):
    return first_num + second_num

print(add(10,2))
```

```
12
```

Cet exemple est très similaire au précédent. La seule différence est que nous avons 3 paramètres au lieu de 2.

```python
def add(first_num, second_num, third_num):
    return first_num + second_num + third_num

print(add(10,2,3))
```

```
15
```

Cette logique de définition de paramètres et de passage d'arguments est la même pour tout nombre de paramètres.

Il est important de souligner que les arguments doivent être passés dans le même ordre que les paramètres sont définis.

### Valeur par défaut.

Vous pouvez définir une valeur par défaut pour un paramètre si aucun argument n'est donné en utilisant l'opérateur `=` et une valeur de votre choix.

Dans cette fonction, si aucun argument n'est donné, le nombre 30 est supposé comme valeur attendue par défaut.

```python
def my_number(my_number = 30):
    return 'Mon nombre est : ' + str(my_number)

print(my_number(10))
print(my_number())
```

```
Mon nombre est : 10
Mon nombre est : 30
```

### Arguments par mot-clé ou nommés

Lorsque vous appelez une fonction, l'ordre des arguments doit correspondre à l'ordre des paramètres.

L'alternative est si vous utilisez des arguments par mot-clé ou nommés.

Définissez les arguments à leurs paramètres respectifs directement en utilisant le nom des paramètres et les opérateurs `=`.

Cet exemple inverse les arguments, mais la fonction fonctionne comme prévu car je lui dis quelle valeur va à quel paramètre par nom.

```python
def my_numbers(first_number, second_number):
    return 'Les nombres sont : ' + str(first_number) + ' et ' + str(second_number)

print(my_numbers(second_number=30, first_number=10))
```

```
Les nombres sont : 10 et 30
```

### Nombre quelconque d'arguments : `*args`

Si vous ne voulez pas spécifier le nombre de paramètres, utilisez simplement le `*` avant le nom du paramètre. Ensuite, la fonction prendra autant d'arguments que nécessaire.

Le nom du paramètre pourrait être n'importe quoi comme `*numbers`, mais il y a une convention en Python d'utiliser `*args` pour cette définition d'un nombre variable d'arguments.

```python
def my_numbers(*args):
    for arg in args:
        print(number)

my_numbers(10,2,3)
```

```
10
2
3
```

### Nombre quelconque d'arguments par mot-clé/nommés : `**kwargs`

Similaire à `*args`, nous pouvons utiliser `**kwargs` pour passer autant d'arguments par mot-clé que nous voulons, tant que nous utilisons `**`.

Encore une fois, le nom pourrait être n'importe quoi comme `**numbers`, mais `**kwargs` est une convention.

```python
def my_numbers(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

my_numbers(first_number=30, second_number=10)
```

```
first_number
30
second_number
10
```

### Autres types comme arguments

Les exemples précédents utilisaient principalement des nombres, mais vous pouvez passer n'importe quel type comme argument et ils seront traités comme tels à l'intérieur de la fonction.

Cet exemple prend des chaînes de caractères comme arguments.

```python
def my_sport(sport):
    print('J'aime ' + sport)

my_sport('football')
my_sport('natation')
```

```
J'aime le football
J'aime la natation
```


Cette fonction prend une liste comme argument.

```python
def my_numbers(numbers):
    for number in numbers:
        print(number)

my_numbers([30, 10, 64, 92, 105])
```

```
30
10
64
92
105
```


# Portée
L'endroit où une variable est créée définit sa disponibilité à être accessible et manipulée par le reste du code. Cela est connu sous le nom de **portée**.

Il existe deux types de portée : locale et globale.

## Portée Globale
Une portée globale vous permet d'utiliser la variable n'importe où dans votre programme.

Si votre variable est en dehors d'une fonction, elle a une portée globale par défaut.

```python
name = 'Bob'

def print_name():
  print('Mon nom est ' + name)

print_name()
```

```
Mon nom est Bob
```

Remarquez que la fonction pouvait utiliser la variable `name` et imprimer `Mon nom est Bob`.

## Portée Locale
Lorsque vous déclarez une variable à l'intérieur d'une fonction, elle n'existe qu'à l'intérieur de cette fonction et ne peut pas être accessible depuis l'extérieur.

```python
def print_name():
	name = "Bob"
	print('Mon nom est ' + name)

print_name()
```

```
Mon nom est Bob
```

La variable `name` a été déclarée à l'intérieur de la fonction, donc la sortie est la même qu'avant.

Mais cela générera une erreur :

```python
def print_name():
	name = 'Bob'
	print('Mon nom est ' + name)

print(name)
```

La sortie du code ci-dessus est :
```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
```

J'ai essayé d'imprimer la variable `name` depuis l'extérieur de la fonction, mais la portée de la variable était locale et n'a pas pu être trouvée dans une portée globale.

## Mélange des Portées
Si vous utilisez le même nom pour des variables à l'intérieur et à l'extérieur d'une fonction, la fonction utilisera celle à l'intérieur de sa portée.

Ainsi, lorsque vous appelez `print_name()`, le `name='Bob'` est utilisé pour imprimer la phrase.

D'autre part, lorsque vous appelez `print()` en dehors de la portée de la fonction, `name="Sarah"` est utilisé en raison de sa portée globale.

```python
name = "Sarah"

def print_name():
	name = 'Bob'
	print('Mon nom est ' + name)

print_name()

print(name)

```

La sortie du code ci-dessus est :
```
Mon nom est Bob

Sarah
```

# Compréhensions de Liste

Parfois, nous voulons effectuer des opérations très simples sur les éléments d'une liste.

Les compréhensions de liste nous donnent un moyen succinct de travailler sur des listes comme alternative à d'autres méthodes d'itération, telles que les boucles `for`.

## Syntaxe de base

Pour utiliser une compréhension de liste pour remplacer une boucle for régulière, nous pouvons faire :

```python
[expression for item in list]
```

Ce qui est la même chose que de faire :

```python
for item in list:
    expression
```

Si nous voulons qu'une condition s'applique à l'expression, nous avons :

```python
[expression for item in list if conditional ]
```

Ce qui est la même chose que de faire :

```python
for item in list:
    if conditional:
        expression
```

## Exemple 1 : calculer le cube d'un nombre

**Méthode régulière**

```python
numbers = [1, 2, 3, 4, 5]
new_list = []

for n in numbers:
    new_list.append(n**3)

print(new_list)
```

```
[1, 8, 27, 64, 125]
```
**Utilisation des compréhensions de liste**

```python
numbers = [1, 2, 3, 4, 5]
new_list = []

new_list = [n**3 for n in numbers]

print(new_list)
```

```
 [1, 8, 27, 64, 125]
```
## Exemple 2 : calculer le cube d'un nombre uniquement s'il est supérieur à 3

En utilisant la conditionnelle, nous pouvons filtrer uniquement les valeurs pour lesquelles nous voulons que l'expression soit appliquée.

**Méthode régulière**

```python
numbers = [1, 2, 3, 4, 5]
new_list = []

for n in numbers:
    if(n > 3):
        new_list.append(n**3)

print(new_list)
```

```
[64, 125]
```
**Utilisation des compréhensions de liste**

```python
numbers = [1, 2, 3, 4, 5]
new_list = []

new_list = [n**3 for n in numbers if n > 3]

print(new_list)
```

```
[64, 125]
```
## Exemple 3 : appel de fonctions avec des compréhensions de liste

Nous pouvons également appeler des fonctions en utilisant la syntaxe des compréhensions de liste :

```python
numbers = [1, 2, 3, 4, 5]
new_list = []

def cube(number):
    return number**3

new_list = [cube(n) for n in numbers if n > 3]

print(new_list)
```

```
[64, 125]
```


# Fonctions Lambda

Une fonction lambda en Python ne peut avoir qu'une seule expression et ne peut pas avoir plusieurs lignes.

Elle est censée faciliter la création d'une petite logique en une seule ligne au lieu d'une fonction complète comme c'est généralement fait.

Les fonctions lambda sont également anonymes, ce qui signifie qu'il n'est pas nécessaire de les nommer.

## Syntaxe de base

La syntaxe de base est très simple : utilisez simplement le mot-clé `lambda`, définissez les paramètres nécessaires et utilisez ":" pour séparer les paramètres de l'expression.

La forme générale est :

```
lambda arguments : expression
```

### Exemple avec un paramètre

Regardez cet exemple utilisant un seul paramètre

```python
cubic = lambda number : number**3
print(cubic(2))
```

```
8
```

### Exemple avec plusieurs paramètres

Si vous le souhaitez, vous pouvez également avoir plusieurs paramètres.

```python
exponential = lambda multiplier, number, exponent : multiplier * number**exponent
print(exponential(2, 2, 3))
```

```
16
```
### Appel direct de la fonction Lambda

Vous n'avez pas besoin d'utiliser une variable comme nous l'avons fait précédemment. Au lieu de cela, vous pouvez utiliser des parenthèses autour de la fonction lambda et une autre paire de parenthèses autour des arguments.

La déclaration de la fonction et l'exécution se feront sur la même ligne.

```python
(lambda multiplier, number, exponent : multiplier * number**exponent)(2, 2, 3)
```

```
16
```

## Exemples utilisant des fonctions lambda avec d'autres fonctions intégrées

### Map

La fonction Map applique l'expression à chaque élément d'une liste.

Calculons le cube de chaque nombre dans la liste.

```python
numbers = [2, 5, 10]
cubics = list(map(lambda number : number**3, numbers))
print(cubics)
```

```
[8, 125, 1000]
```

### Filter

La fonction Filter filtrera la liste en fonction de l'expression.

Filtrons pour n'avoir que les nombres supérieurs à 5.

```python
numbers = [2, 5, 10]
filtered_list = list(filter(lambda number : number > 5, numbers))
print(filtered_list)
```

```
[10]
```

# Modules

Après un certain temps, votre code commence à devenir plus complexe avec de nombreuses fonctions et variables.

Pour faciliter l'organisation du code, nous utilisons des Modules.

Un Module bien conçu a également l'avantage d'être réutilisable, vous écrivez donc le code une fois et le réutilisez partout.

Vous pouvez écrire un module avec toutes les opérations mathématiques et d'autres personnes peuvent l'utiliser.

Et, si vous en avez besoin, vous pouvez utiliser les modules de quelqu'un d'autre pour simplifier votre code, accélérant ainsi votre projet.

Dans d'autres langages de programmation, ceux-ci sont également appelés bibliothèques.

## Utilisation d'un Module

Pour utiliser un module, nous utilisons le mot-clé `import`.

Comme le nom l'indique, nous devons dire à notre programme quel module importer.

Après cela, nous pouvons utiliser n'importe quelle fonction disponible dans ce module.

Voyons un exemple en utilisant le module `math`.

Tout d'abord, voyons comment accéder à une constante, le nombre d'Euler.

```python
import math

math.e
```

```
2.718281828459045
```

Dans cet exemple, nous allons utiliser une fonction qui calcule la racine carrée d'un nombre.

Il est également possible d'utiliser le mot-clé `as` pour créer un alias.

```python
import math as m

m.sqrt(121)

m.sqrt(729)
```

```
11
27
```

Enfin, en utilisant le mot-clé `from`, nous pouvons spécifier exactement ce qu'il faut importer au lieu du module entier et utiliser la fonction directement sans le nom du module.

Cet exemple utilise la fonction `floor()` qui retourne le plus grand entier inférieur ou égal à un nombre donné.
```python
from math import floor

floor(9.8923)
```

```
9
```

## Création d'un Module

Maintenant que nous savons comment utiliser les modules, voyons comment en créer un.

Il s'agira d'un module avec les opérations mathématiques de base `add`, `subtract`, `multiply`, `divide` et il s'appellera `basic_operations`.

Créez le fichier `basic_operations.py` avec les quatre fonctions.

```python
def add(first_num, second_num):
    return first_num + second_num

def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num
```

Ensuite, importez simplement le module `basic_operations` et utilisez les fonctions.
```python
import basic_operations

basic_operations.add(10,2)
basic_operations.subtract(10,2)
basic_operations.multiply(10,2)
basic_operations.divide(10,2)
```

```
12
8
20
5.0
```


# `if __name__ == '__main__'`

Vous êtes en train de construire un module avec les opérations mathématiques de base `add`, `subtract`, `multiply`, et `divide` appelé `basic_operations` sauvegardé dans le fichier `basic_operations.py`.

Pour garantir que tout est correct, vous pouvez exécuter quelques tests.

```python
def add(first_num, second_num):
    return first_num + second_num

def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

print(add(10, 2)) 
print(subtract(10,2))
print(multiply(10,2))
print(divide(10,2))
```

Après avoir exécuté le code :

```shell
renan@pro-home:~$ python3 basic_operations.py
```

La sortie est :

```
12
8
20
5.0
```

La sortie de ces tests est ce à quoi nous nous attendions.

Notre code est correct et prêt à être partagé.

Importons le nouveau module et exécutons-le dans la console Python.

```python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import basic_operations
12
8
20
5.0
>>> 
```

Lorsque le module est importé, nos tests sont affichés à l'écran même si nous n'avons rien fait d'autre que d'importer `basic_operations`.

Pour corriger cela, nous utilisons `if __name__ == '__main__'` dans le fichier `basic_operations.py` comme ceci :

```python
def add(first_num, second_num):
    return first_num + second_num

def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

if __name__ == '__main__':
    print(add(10, 2)) 
    print(subtract(10,2))
    print(multiply(10,2))
    print(divide(10,2))
```

L'exécution du code directement sur le terminal continuera à afficher les tests. Mais lorsque vous l'importez comme un module, les tests ne s'afficheront pas et vous pourrez utiliser les fonctions comme prévu.

```python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import basic_operations
>>> basic_operations.multiply(10,2)
20
>>>
```

Maintenant que vous savez comment utiliser `if __name__ == '__main__'`, comprenons comment cela fonctionne.

La condition indique quand l'interpréteur traite le code comme un module ou comme un programme lui-même étant exécuté directement.

Python a cette variable native appelée `__name__`.

Cette variable représente le nom du module qui est le nom du fichier `.py`.

Créez un fichier `my_program.py` avec ce qui suit et exécutez-le.

```python
print(__name__)
```

La sortie sera :

```
__main__
```

Cela nous indique que lorsqu'un programme est exécuté directement, la variable `__name__` est définie comme `__main__`.


Mais lorsqu'il est importé comme un module, la valeur de `__name__` est le nom du module.

```python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import my_program
my_program
>>>
```

C'est ainsi que l'interpréteur Python différencie le comportement d'un module importé et d'un programme exécuté directement dans le terminal.


# Fichiers
Créer, supprimer, lire et de nombreuses autres fonctions appliquées aux fichiers font partie intégrante de nombreux programmes.

Ainsi, il est très important de savoir comment organiser et traiter les fichiers directement à partir de votre code.

Voyons comment gérer les fichiers en Python.

## Création de fichier

Tout d'abord, créons !

Nous allons utiliser la fonction `open()`.

Cette fonction ouvre un fichier et retourne son objet correspondant.

Le premier argument est le nom du fichier que nous traitons, le second fait référence à l'opération que nous utilisons.

Le code ci-dessous crée le fichier "people.txt", l'argument `x` est utilisé lorsque nous voulons simplement créer le fichier. Si un fichier avec le même nom existe déjà, il générera une exception.

```python
people_file = open("people.txt", "x")
```


Vous pouvez également utiliser le mode `w` pour créer un fichier. Contrairement au mode `x`, il ne générera pas d'exception puisque ce mode indique le mode _écriture_. Nous ouvrons un fichier pour y écrire des données et, si le fichier n'existe pas, il est créé.

```python
people_file = open("people.txt", "w")
```


Le dernier est le mode `a` qui signifie _ajouter_. Comme le nom l'indique, vous pouvez ajouter plus de données au fichier, tandis que le mode `w` écrase simplement toutes les données existantes.

Lors de l'ajout, si le fichier n'existe pas, il le crée également.

```python
people_file = open("people.txt", "a")
```

## Écriture dans un fichier
Pour écrire des données dans un fichier, vous ouvrez simplement un fichier avec le mode `w`.

Ensuite, pour ajouter des données, vous utilisez l'objet retourné par la fonction `open()`. Dans ce cas, l'objet s'appelle `people_file`. Ensuite, vous appelez la fonction _write()_ en passant les données comme argument.

```python
people_file = open("people.txt", "w")
people_file.write("Bob\n")
people_file.write("Mary\n")
people_file.write("Sarah\n")
people_file.close()
```

Nous utilisons `\n` à la fin pour sauter une ligne, sinon le contenu du fichier restera sur la même ligne comme "BobMarySarah".

Un autre détail est de _close()_ le fichier. Ce n'est pas seulement une bonne pratique, mais cela garantit également que vos modifications ont été appliquées au fichier.

Rappelez-vous que lorsque vous utilisez le mode `w`, les données qui existaient déjà dans le fichier seront écrasées par les nouvelles données. Pour ajouter de nouvelles données sans perdre ce qui était déjà là, nous devons utiliser le mode d'ajout.

## Ajout à un fichier

Le mode `a` ajoute de nouvelles données au fichier, en conservant les données existantes.

Dans cet exemple, après la première écriture avec le mode `w`, nous utilisons le mode `a` pour ajouter. Le résultat est que chaque nom apparaîtra deux fois dans le fichier "people.txt".

```python
#première écriture
people_file = open("people.txt", "w")
people_file.write("Bob\n")
people_file.write("Mary\n")
people_file.write("Sarah\n")
people_file.close()

#ajout de plus de données
#conservation des données existantes
people_file = open("people.txt", "a")
people_file.write("Bob\n")
people_file.write("Mary\n")
people_file.write("Sarah\n")
people_file.close()
```

## Lecture de fichier

La lecture du fichier est également très simple : utilisez simplement le mode `r` comme ceci.

Si vous lisez le fichier "people.txt" créé dans le dernier exemple, vous devriez voir 6 noms dans votre sortie.

```python 
people_file = open("people.txt", "r")
print(people_file.read())
```

```
Bob
Mary
Sarah
Bob
Mary
Sarah
```

La fonction `read()` lit le fichier entier en une seule fois. Si vous utilisez la fonction `readline()`, vous pouvez lire le fichier ligne par ligne.

```python
people_file = open("people.txt", "r")
print(people_file.readline())
print(people_file.readline())
print(people_file.readline())
```

```
Bob
Mary
Sarah
```


Vous pouvez également boucler pour lire les lignes comme dans l'exemple ci-dessous.

```python
people_file = open("people.txt", "r")
for person in people_file:
  print(person)
```

```
Bob
Mary
Sarah
Bob
Mary
Sarah
```

## Supprimer un fichier
Pour supprimer un fichier, vous avez également besoin du module `os`.

Utilisez la méthode `remove()`.
```python
import os

os.remove('my_file.txt')
```

## Vérifier si un fichier existe
Utilisez la méthode `os.path.exists()` pour vérifier l'existence d'un fichier.
```python
import os

if os.path.exists('my_file.txt'):
  os.remove('my_file.txt')
else:
  print('Il n'y a pas de tel fichier !')
```

## Copier un fichier
Pour cela, j'aime utiliser la méthode `copyfile()` du module `shutil`.
```python
from shutil import copyfile

copyfile('my_file.txt','another_file.txt')
```

Il existe quelques options pour copier un fichier, mais `copyfile()` est la plus rapide.

## Renommer et déplacer un fichier
Si vous devez déplacer ou renommer un fichier, vous pouvez utiliser la méthode `move()` du module `shutil`.
```python
from shutil import move

move('my_file.txt','another_file.txt')
```


# Classes et Objets

Les Classes et Objets sont les concepts fondamentaux de la Programmation Orientée Objet.

En Python, **tout est un objet** !

Une variable (objet) est simplement une instance de son type (classe).

C'est pourquoi lorsque vous vérifiez le type d'une variable, vous pouvez voir le mot-clé `class` juste à côté de son type (classe).

Ce snippet de code montre que `my_city` est un objet et qu'il est une instance de la classe `str`.

```python
my_city = "New York"
print(type(my_city))
```

```
<class 'str'>
```

## Différencier Classe x Objet

La classe vous donne un moyen standard de créer des objets. Une classe est comme un projet de base.

Disons que vous êtes un ingénieur travaillant pour Boeing.

Votre nouvelle mission est de construire le nouveau produit de l'entreprise, un nouveau modèle appelé 747-Space. Cet avion vole à des altitudes plus élevées que les autres modèles commerciaux.

Boeing doit construire des dizaines de ceux-ci pour les vendre aux compagnies aériennes du monde entier, et les avions doivent tous être identiques.

Pour garantir que les avions (objets) suivent les mêmes normes, vous devez avoir un projet (classe) qui peut être reproductible.

La classe est un projet, un plan pour un objet.

De cette façon, vous faites le projet une fois, et vous le réutilisez de nombreuses fois.

Dans notre exemple de code précédent, considérons que chaque chaîne de caractères a le même comportement et les mêmes attributs. Il est donc logique que les chaînes de caractères aient une classe `str` pour les définir.

## Attributs et Méthodes

Les objets ont un certain comportement qui est donné par des attributs et des méthodes.

En termes simples, dans le contexte d'un objet, les attributs sont des variables et les méthodes sont des fonctions attachées à un objet.

Par exemple, une chaîne de caractères a de nombreuses méthodes intégrées que nous pouvons utiliser.

Elles fonctionnent comme des fonctions, vous devez simplement les séparer des objets en utilisant un `.`.

Dans ce snippet de code, j'appelle la méthode `replace()` de la variable de chaîne de caractères `my_city` qui est un objet, et une instance de la classe `str`.

La méthode `replace()` remplace une partie de la chaîne de caractères par une autre et retourne une nouvelle chaîne de caractères avec le changement. La chaîne de caractères originale reste la même.

Remplaçons 'New' par 'Old' dans 'New York'.

```python
my_city = 'New York'
print(my_city.replace('New', 'Old'))
print(my_city)
```

```
Old York
New York
```

## Création d'une Classe

Nous avons utilisé de nombreux objets (instances de classes) comme des chaînes de caractères, des entiers, des listes et des dictionnaires. Tous sont des instances de classes prédéfinies en Python.

Pour créer nos propres classes, nous utilisons le mot-clé `class`.

Par convention, le nom de la classe correspond au nom du fichier `.py` et au module par conséquent. C'est également une bonne pratique d'organiser le code.

Créez un fichier `vehicle.py` avec la classe `Vehicle` suivante.

```python
class Vehicle:
    def __init__(self, year, model, plate_number, current_speed = 0):
        self.year = year
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed

    def move(self):
        self.current_speed += 1

    def accelerate(self, value):
        self.current_speed += value
    
    def stop(self):
        self.current_speed = 0
    
    def vehicle_details(self):
        return self.model + ', ' + str(self.year) + ', ' + self.plate_number
```

Décomposons la classe pour l'expliquer en parties.

Le mot-clé `class` est utilisé pour spécifier le nom de la classe `Vehicle`.

La fonction `__init__` est une fonction intégrée que toutes les classes possèdent. Elle est appelée lorsqu'un objet est créé et est souvent utilisée pour initialiser les attributs, en leur attribuant des valeurs, similaire à ce qui est fait pour les variables.

Le premier paramètre `self` dans la fonction `__init__` est une référence à l'objet (instance) lui-même. Nous l'appelons `self` par convention et il doit être le premier paramètre dans chaque méthode d'instance, comme vous pouvez le voir dans les autres définitions de méthodes `def move(self)`, `def accelerate(self, value)`, `def stop(self)`, et `def vehicle_details(self)`.

`Vehicle` a 5 attributs (y compris self) : `year`, `model`, `plate_number`, et `current_speed`.

À l'intérieur de `__init__`, chacun d'eux est initialisé avec les paramètres donnés lorsque l'objet est instancié.

Remarquez que `current_speed` est initialisé avec `0` par défaut, ce qui signifie que si aucune valeur n'est donnée, `current_speed` sera égal à 0 lorsque l'objet est instancié pour la première fois.

Enfin, nous avons trois méthodes pour manipuler notre véhicule concernant sa vitesse : `def move(self)`, `def accelerate(self, value)`, et `def stop(self)`.

Et une méthode pour donner des informations sur le véhicule : `def vehicle_details(self)`.

L'implémentation à l'intérieur des méthodes fonctionne de la même manière que dans les fonctions. Vous pouvez également avoir un `return` pour vous retourner une valeur à la fin de la méthode comme démontré par `def vehicle_details(self)`.

## Utilisation de la Classe

Pour utiliser la classe dans votre terminal, importez la classe `Vehicle` du module `vehicle`.

Créez une instance appelée `my_car`, en initialisant `year` avec 2009, `model` avec 'F8', `plate_number` avec 'ABC1234', et `current_speed` avec 100.

Le paramètre `self` n'est pas pris en compte lors de l'appel des méthodes. L'interpréteur Python infère sa valeur comme étant l'objet/instance actuel automatiquement, donc nous devons simplement passer les autres arguments lors de l'instanciation et de l'appel des méthodes.

Utilisez maintenant les méthodes pour `move()` la voiture, ce qui augmente sa `current_speed` de 1, `accelerate(10)` qui augmente sa `current_speed` de la valeur donnée dans l'argument, et `stop()` qui met la `current_speed` à 0.

N'oubliez pas d'imprimer la valeur de `current_speed` à chaque commande pour voir les changements.

Pour terminer le test, appelez `vehicle_details()` pour imprimer les informations sur notre véhicule.

```python
>>> from vehicle import Vehicle
>>>
>>> my_car = Vehicle(2009, 'F8', 'ABC1234', 100)
>>> print(my_car.current_speed)
100
>>> my_car.move()
>>> print(my_car.current_speed)
101
>>> my_car.accelerate(10)
>>> print(my_car.current_speed)
111
>>> my_car.stop()
>>> print(my_car.current_speed)
0
>>> print(my_car.vehicle_details())
F8, 2009, ABC1234
```

Si nous ne définissons pas la valeur initiale pour `current_speed`, elle sera zéro par défaut comme indiqué précédemment et démontré dans l'exemple suivant.

```python
>>> from vehicle import Vehicle
>>>
>>> my_car = Vehicle(2009, 'F8', 'ABC1234')
>>> print(my_car.current_speed)
0
>>> my_car.move()
>>> print(my_car.current_speed)
1
>>> my_car.accelerate(10)
>>> print(my_car.current_speed)
11
>>> my_car.stop()
>>> print(my_car.current_speed)
0
>>> print(my_car.vehicle_details())
F8, 2009, ABC1234
```


# Héritage

Définissons une classe générique `Vehicle` et sauvegardons-la dans le fichier `vehicle.py`.

```python
class Vehicle:
    def __init__(self, year, model, plate_number, current_speed):
        self.year = year
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed

    def move(self):
        self.current_speed += 1

    def accelerate(self, value):
        self.current_speed += value
    
    def stop(self):
        self.current_speed = 0
    
    def vehicle_details(self):
        return self.model + ', ' + str(self.year) + ', ' + self.plate_number
```

Un véhicule a les attributs `year`, `model`, `plate_number`, et `current_speed`.

La définition de véhicule dans `Vehicle` est très générique et peut ne pas convenir aux camions, par exemple, car elle devrait inclure un attribut `cargo`.

D'autre part, un attribut cargo n'a pas beaucoup de sens pour les petits véhicules comme les motos.

Pour résoudre cela, nous pouvons utiliser l'_héritage_.

Lorsque une classe (enfant) hérite d'une autre classe (parent), tous les attributs et méthodes de la classe parent sont hérités par la classe enfant.

## Parent et Enfant

Dans notre cas, nous voulons qu'une nouvelle classe `Truck` hérite de tout de la classe `Vehicle`. Ensuite, nous voulons qu'elle ajoute son propre attribut spécifique `current_cargo` pour contrôler l'ajout et le retrait de la cargaison du camion.

La classe `Truck` est appelée une classe _enfant_ qui hérite de sa classe _parent_ `Vehicle`.

Une classe _parent_ est également appelée une _superclasse_ tandis qu'une classe _enfant_ est également connue sous le nom de _sous-classe_.

Créez la classe `Truck` et sauvegardez-la dans le fichier `truck.py`.

```python
from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, year, model, plate_number, current_speed, current_cargo):
        super().__init__(year, model, plate_number, current_speed)
        self.current_cargo = current_cargo

    def add_cargo(self, cargo):
        self.current_cargo += cargo

    def remove_cargo(self, cargo):
        self.current_cargo -= cargo
```

Décomposons la classe pour l'expliquer en parties.

La classe `Vehicle` à l'intérieur des parenthèses lors de la définition de la classe `Truck` indique que le _parent_ `Vehicle` est hérité par son enfant `Truck`.

La méthode `__init__` a `self` comme premier paramètre, comme d'habitude.

Les paramètres `year`, `model`, `plate_number`, et `current_speed` sont là pour correspondre à ceux de la classe `Vehicle`.

Nous avons ajouté un nouveau paramètre `current_cargo` adapté à la classe `Truck`.

Dans la première ligne de la méthode `__init__` de la classe `Truck`, nous devons appeler la méthode `__init__` de la classe `Vehicle`.

Pour ce faire, nous utilisons `super()` pour faire référence à la _superclasse_ `Vehicle`, donc lorsque `super().__init__(year, model, plate_number, current_speed)` est appelé, nous évitons la répétition de notre code.

Après cela, nous pouvons attribuer la valeur de `current_cargo` normalement.

Enfin, nous avons deux méthodes pour gérer le `current_cargo` : `def add_cargo(self, cargo):`, et `def remove_cargo(self, cargo):`.

Rappelez-vous que `Truck` hérite des attributs et méthodes de `Vehicle`, donc nous avons également un accès implicite aux méthodes qui manipulent la vitesse : `def move(self)`, `def accelerate(self, value)`, et `def stop(self)`.

## Utilisation de la classe `Truck`

Pour utiliser la classe dans votre terminal, importez la classe `Truck` du module `truck`.

Créez une instance appelée `my_truck`, en initialisant `year` avec 2015, `model` avec 'V8', `plate_number` avec 'XYZ1234', `current_speed` avec 0, et `current_cargo` avec 0.

Utilisez `add_cargo(10)` pour augmenter `current_cargo` de 10, `remove_cargo(4)`, pour diminuer `current_cargo` de 4.

N'oubliez pas d'imprimer la valeur de `current_cargo` à chaque commande pour voir les changements.

Par héritage, nous pouvons utiliser les méthodes de la classe `Vehicle` pour `move()` le camion, ce qui augmente sa `current_speed` de 1, `accelerate(10)` qui augmente sa `current_speed` de la valeur donnée dans l'argument, et `stop()` qui met la `current_speed` à 0.

N'oubliez pas d'imprimer la valeur de `current_speed` à chaque interaction pour voir les changements.

Pour terminer le test, appelez `vehicle_details()` hérité de la classe `Vehicle` pour imprimer les informations sur notre camion.

```python
>>> from truck import Truck
>>> 
>>> my_truck = Truck(2015, 'V8', 'XYZ1234', 0, 0)
>>> print(my_truck.current_cargo)
0
>>> my_truck.add_cargo(10)
>>> print(my_truck.current_cargo)
10
>>> my_truck.remove_cargo(4)
>>> print(my_truck.current_cargo)
6
>>> print(my_truck.current_speed)
0
>>> my_truck.accelerate(10)
>>> print(my_truck.current_speed)
10
>>> my_truck.stop()
>>> print(my_truck.current_speed)
0
>>> print(my_truck.vehicle_details())
V8, 2015, XYZ1234
```


# Exceptions

Les erreurs font partie de la vie de tout programmeur, et savoir comment les gérer est une compétence en soi.

La manière dont Python gère les erreurs s'appelle 'Gestion des Exceptions'.

Si un morceau de code rencontre une erreur, l'interpréteur Python _lèvera_ une exception.

## Types d'Exceptions

Essayons de lever quelques exceptions intentionnellement et voyons les erreurs qu'elles produisent.

- `TypeError`

Tout d'abord, essayez d'ajouter une chaîne de caractères et un entier
```python
'I am a string' + 32
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

- `IndexError`

Maintenant, essayez d'accéder à un index qui n'existe pas dans une liste.

Une erreur courante est d'oublier que les séquences sont indexées à partir de 0, ce qui signifie que le premier élément a l'index 0, et non 1.

Dans cet exemple, la liste `car_brands` se termine à l'index 2.

```python
car_brands = ['ford', 'ferrari', 'bmw']
print(car_brands[3])
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

- `NameError`

Si nous essayons d'imprimer une variable qui n'existe pas :

```python
print(my_variable)
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_variable' is not defined
```

- `ZeroDivisionError`

Les mathématiques n'autorisent pas la division par zéro, donc essayer de le faire lèvera une erreur, comme prévu.

```python
32/0
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Ceci n'était qu'un échantillon des types d'exceptions que vous pourriez rencontrer lors de votre routine quotidienne et ce qui peut causer chacune d'entre elles.

## Gestion des Exceptions

Maintenant que nous savons comment causer des erreurs qui feront planter notre code et nous montrer un message indiquant que quelque chose ne va pas.

Pour gérer ces exceptions, utilisez simplement l'instruction `try/except`.

```python
try:
  32/0
except:
  print('Division par zéro !')
```

```
Division par zéro !
```

L'exemple ci-dessus montre l'utilisation de l'instruction `try`.

Placez le bloc de code qui peut causer une exception à l'intérieur de la portée `try`. Si tout se passe bien, le bloc `except` n'est pas invoqué. Mais si une exception est levée, le bloc de code à l'intérieur de `except` est exécuté.

De cette façon, le programme ne plante pas et si vous avez du code après l'exception, il continuera à s'exécuter si vous le souhaitez.

## Gestion des Exceptions Spécifiques

Dans le dernier exemple, le bloc `except` était générique, ce qui signifie qu'il attrapait tout.

La bonne pratique est de spécifier le type d'exception que nous essayons d'attraper, ce qui aide beaucoup lors du débogage du code plus tard.

Si vous savez qu'un bloc de code peut lancer une `IndexError`, spécifiez-le dans le `except` :

```python
try:
  car_brands = ['ford', 'ferrari', 'bmw']
  print(car_brands[3])
except IndexError:
  print('Il n'y a pas un tel index !')
```

```
Il n'y a pas un tel index !
```

Vous pouvez utiliser un tuple pour spécifier autant de types d'exceptions que vous le souhaitez dans un seul `except` :

```python
try:
  print('Mon code !')
except(IndexError, ZeroDivisionError, TypeError):
  print('Mon Exception !')
```

## `else`

Il est possible d'ajouter une commande `else` à la fin du `try/except`. Elle s'exécute uniquement s'il n'y a pas d'exceptions.

```python
my_variable = 'Ma variable'
try:
  print(my_variable)
except NameError:
  print('NameError attrapé !')
else:
  print('Pas de NameError')
```

```
Ma variable
Pas de NameError
```

## Lever des Exceptions

La commande `raise` vous permet de lever manuellement une exception.

Cela est particulièrement utile si vous voulez attraper une exception et faire quelque chose avec elle -- comme journaliser l'erreur de manière personnalisée, comme la rediriger vers un agrégateur de logs, ou mettre fin à l'exécution du code puisque l'erreur ne devrait pas permettre la progression du programme.

```python
try:
  raise IndexError('Cet index n'est pas autorisé')
except:
  print('Faire quelque chose avec l'exception !')
  raise
```

```
Faire quelque chose avec l'exception !
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: Cet index n'est pas autorisé
```

## `finally`

Le bloc `finally` est exécuté indépendamment du fait que des exceptions soient levées ou non.

Ils sont généralement là pour permettre au programme de nettoyer les ressources comme les fichiers, la mémoire, les connexions réseau, etc.

```python
try:
  print(my_variable)
except NameError:
  print('Bloc Except')
finally:
  print('Bloc Finally')
```

```
Bloc Except
Bloc Finally
```


# Conclusion

C'est tout !

Félicitations pour avoir atteint la fin.

Je tiens à vous remercier d'avoir lu cet article.

Si vous voulez en savoir plus, consultez mon blog [renanmf.com](https://renanmf.com).

N'oubliez pas [de télécharger une version PDF de ce Guide Python pour Débutants](https://renanmf.com/python-guide-beginners/).

Vous pouvez également me trouver sur Twitter : [@renanmouraf](https://twitter.com/renanmouraf).