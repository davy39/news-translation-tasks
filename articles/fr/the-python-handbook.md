---
title: Le manuel Python – Apprendre Python pour les débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2021-03-10T22:51:03.000Z'
originalURL: https://freecodecamp.org/news/the-python-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/book.png
tags:
- name: beginner
  slug: beginner
- name: learn to code
  slug: learn-to-code
- name: Python
  slug: python
- name: python developer
  slug: python-developer
seo_title: Le manuel Python – Apprendre Python pour les débutants
seo_desc: "The Python Handbook follows the 80/20 rule: learn 80% of the topic in 20%\
  \ of the time.\nI find this approach gives a well-rounded overview. \nThis book\
  \ does not try to cover everything under the sun related to Python. It focuses on\
  \ the core of the lang..."
---

Le manuel Python suit la règle 80/20 : apprendre 80 % du sujet en 20 % du temps.

Je trouve que cette approche donne un aperçu bien équilibré. 

Ce livre ne tente pas de couvrir tout ce qui concerne Python. Il se concentre sur le cœur du langage, en essayant de simplifier les sujets plus complexes. 

J'espère que le contenu de ce livre vous aidera à atteindre ce que vous voulez : **apprendre les bases de Python**.

> Note : Vous pouvez [obtenir une version PDF, ePub et Mobi de ce manuel Python](https://flaviocopes.com/page/python-handbook/)

Amusez-vous !

## Sommaire

- [Introduction à Python](#heading-introduction-a-python)
- [Comment installer Python](#heading-comment-installer-python)
- [Comment exécuter des programmes Python](#heading-comment-executer-des-programmes-python)
- [Python 2 vs Python 3](#heading-python-2-vs-python-3)
- [Les bases de Python](#heading-les-bases-de-python)
- [Types de données en Python](#heading-types-de-donnees-en-python)
- [Opérateurs en Python](#operators)
- [L'opérateur ternaire en Python](#heading-loperateur-ternaire-en-python)
- [Chaînes de caractères en Python](#heading-chaines-de-caracteres-en-python)
- [Booléens en Python](#heading-booleens-en-python)
- [Nombres en Python](#heading-nombres-en-python)
- [Constantes en Python](#heading-constantes-en-python)
- [Énumérations en Python](#heading-enumerations-en-python)
- [Saisie utilisateur en Python](#heading-saisie-utilisateur-en-python)
- [Instructions de contrôle en Python](#heading-instructions-de-controle-en-python)
- [Listes en Python](#heading-listes-en-python)
- [Tuples en Python](#heading-tuples-en-python)
- [Dictionnaires en Python](#heading-dictionnaires-en-python)
- [Ensembles en Python](#heading-ensembles-en-python)
- [Fonctions en Python](#heading-fonctions-en-python)
- [Objets en Python](#heading-objets-en-python)
- [Boucles en Python](#heading-boucles-en-python)
- [Classes en Python](#heading-classes-en-python)
- [Modules en Python](#heading-modules-en-python)
- [La bibliothèque standard de Python](#heading-la-bibliotheque-standard-de-python)
- [Le guide de style PEP8 pour Python](#heading-le-guide-de-style-pep8-pour-python)
- [Débogage en Python](#heading-debogage-en-python)
- [Portée des variables en Python](#heading-portee-des-variables-en-python)
- [Comment accepter des arguments de la ligne de commande en Python](#heading-comment-accepter-des-arguments-de-la-ligne-de-commande-en-python)
- [Fonctions lambda en Python](#heading-fonctions-lambda-en-python)
- [Récursivité en Python](#heading-recursivite-en-python)
- [Fonctions imbriquées en Python](#heading-fonctions-imbriquees-en-python)
- [Fermetures en Python](#heading-fermetures-en-python)
- [Décorateurs en Python](#heading-decorateurs-en-python)
- [Docstrings en Python](#heading-docstrings-en-python)
- [Introspection en Python](#heading-introspection-en-python)
- [Annotations en Python](#heading-annotations-en-python)
- [Exceptions en Python](#heading-exceptions-en-python)
- [L'instruction with en Python](#heading-linstruction-with-en-python)
- [Comment installer des packages tiers en Python en utilisant pip](#heading-comment-installer-des-packages-tiers-en-python-en-utilisant-pip)
- [Compréhensions de liste en Python](#heading-comprehensions-de-liste-en-python)
- [Polymorphisme en Python](#heading-polymorphisme-en-python)
- [Surcharge d'opérateurs en Python](#heading-surcharge-doperateurs-en-python)
- [Environnements virtuels en Python](#heading-environnements-virtuels-en-python)
- [Conclusion](#heading-conclusion)

## Introduction à Python

Python est littéralement en train de conquérir le monde de la programmation. Il gagne en popularité et en utilisation de manière pratiquement sans précédent dans l'histoire de l'informatique.

Python excelle dans une grande variété de scénarios – **scripting shell**, **automatisation de tâches**, et **développement web** ne sont que quelques exemples de base.

Python est le langage de choix pour **l'analyse de données** et **l'apprentissage automatique**, mais il peut également s'adapter pour créer des jeux et travailler avec des dispositifs embarqués.

Plus important encore, c'est le langage de choix pour les cours d'introduction à l'**informatique** dans les universités du monde entier.

De nombreux étudiants apprennent Python comme premier langage de programmation. Beaucoup l'apprennent en ce moment, et beaucoup plus l'apprendront à l'avenir. Et pour beaucoup d'entre eux, Python sera le seul langage de programmation dont ils auront besoin.

Grâce à cette position unique, Python est susceptible de croître encore plus à l'avenir.

Le langage est simple, expressif, et assez direct.

L'écosystème est énorme. Il semble y avoir une bibliothèque pour tout ce que vous pouvez imaginer.

Python est un langage de programmation de haut niveau adapté aux débutants grâce à sa syntaxe intuitive, sa grande communauté et son écosystème dynamique.

Il est également apprécié par les professionnels de nombreux domaines différents.

Techniquement parlant, Python est un langage interprété qui n'a pas de phase de compilation intermédiaire comme un langage compilé, par exemple C ou Java.

Et comme de nombreux langages interprétés, il est typé dynamiquement. Cela signifie que vous n'avez pas à indiquer les types des variables que vous utilisez, et les variables ne sont pas liées à un type spécifique.

Cela a des avantages et des inconvénients. En particulier, vous écrivez des programmes plus rapidement, mais d'un autre côté, vous avez moins d'aide de la part des outils pour prévenir les bugs possibles. Cela signifie que vous découvrirez certains problèmes uniquement en exécutant le programme au moment de l'exécution.

Python prend en charge une grande variété de différents paradigmes de programmation, y compris la programmation procédurale, la programmation orientée objet et la programmation fonctionnelle. Il est suffisamment flexible pour s'adapter à de nombreux besoins différents.

Créé en 1991 par Guido van Rossum, il n'a cessé de gagner en popularité - surtout au cours des 5 dernières années, comme le montre cette infographie Google Trends :

![Screen-Shot-2020-11-09-at-19.22.38](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-09-at-19.22.38.png)

Commencer avec Python est très facile. Tout ce dont vous avez besoin est d'installer le package officiel depuis python.org, pour Windows, macOS ou Linux, et vous êtes prêt à partir.

Si vous êtes nouveau en programmation, dans les articles suivants, je vous guiderai pour passer de zéro à devenir un programmeur Python.

Et même si vous êtes actuellement un programmeur qui se spécialise dans un autre langage, Python est un langage qui vaut la peine d'être connu car je pense qu'il ne fera que continuer à croître à partir de là.

Les langages de bas niveau comme C++ et Rust peuvent être excellents pour les programmeurs experts, mais ils sont intimidants pour commencer, et ils prennent beaucoup de temps à maîtriser. 

Python, en revanche, est un langage de programmation pour tout le monde – étudiants, personnes utilisant Excel dans leur travail quotidien, scientifiques, et plus encore.

**C'est le langage que toute personne intéressée par la programmation devrait apprendre en premier**.


## Comment installer Python

Allez sur <https://www.python.org>, choisissez le menu Téléchargements, choisissez votre système d'exploitation, et un panneau avec un lien pour télécharger le package officiel apparaîtra :

![Screen-Shot-2020-11-09-at-13.57.36-1](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-09-at-13.57.36-1.png)

Assurez-vous de suivre les instructions spécifiques pour votre système d'exploitation. Sur macOS, vous pouvez trouver un guide détaillé sur <https://flaviocopes.com/python-installation-macos/>.


## Comment exécuter des programmes Python

Il existe plusieurs façons d'exécuter des programmes Python.

En particulier, il y a une distinction entre l'utilisation de prompts interactifs, où vous tapez du code Python et il est immédiatement exécuté, et l'enregistrement d'un programme Python dans un fichier et son exécution.

Commençons par les prompts interactifs.

Si vous ouvrez votre terminal et tapez `python`, vous verrez un écran comme ceci :

![Screen-Shot-2020-11-10-at-13.44.07](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-13.44.07.png)

C'est le REPL Python (Read-Evaluate-Print-Loop).

Remarquez le symbole `>>>` et le curseur qui suit. Vous pouvez taper n'importe quel code Python ici et appuyer sur la touche `enter` pour l'exécuter.

Par exemple, essayez de définir une nouvelle variable en utilisant

```python
name = "Flavio"
```

puis imprimez sa valeur en utilisant `print()` :

```python
print(name)
```

![Screen-Shot-2020-11-10-at-14.11.57](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.11.57.png)

> Note : dans le REPL, vous pouvez également simplement taper `name`, appuyer sur la touche `enter` et vous obtiendrez la valeur en retour. Mais dans un programme, vous ne verrez aucune sortie si vous faites cela - vous devez utiliser `print()`.

Toute ligne de Python que vous écrivez ici sera exécutée immédiatement.

Tapez `quit()` pour quitter ce REPL Python.

Vous pouvez accéder au même prompt interactif en utilisant l'application IDLE qui est installée automatiquement par Python :

![Screen-Shot-2020-11-10-at-14.13.25](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.13.25.png)

Cela peut être plus pratique pour vous car avec la souris vous pouvez vous déplacer et copier/coller plus facilement que dans le terminal.

Ce sont les bases qui viennent avec Python par défaut. Cependant, je vous recommande d'installer [IPython](https://ipython.org/), probablement la meilleure application REPL en ligne de commande que vous pouvez trouver.

Installez-le avec

```sh
pip install ipython
```

Assurez-vous que les binaires pip sont dans votre path, puis exécutez `ipython` :

![Screen-Shot-2020-11-11-at-09.36.29](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-11-at-09.36.29.png)

`ipython` est une autre interface qui vous permet de travailler avec un REPL Python et fournit quelques fonctionnalités intéressantes comme la coloration syntaxique, la complétion de code, et bien plus encore.

La deuxième façon d'exécuter un programme Python est d'écrire votre code de programme Python dans un fichier, par exemple `program.py` :

![Screen-Shot-2020-11-10-at-14.01.24](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.01.24.png)

puis l'exécuter avec `python program.py` :

![Screen-Shot-2020-11-10-at-14.01.32](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.01.32.png)

> Notez que nous enregistrons les programmes Python avec l'extension `.py` - c'est une convention.

Dans ce cas, le programme est exécuté dans son ensemble, pas ligne par ligne. Et c'est généralement ainsi que nous exécutons les programmes.

Nous utilisons le REPL pour le prototypage rapide et pour l'apprentissage.

Sur Linux et macOS, un programme Python peut également être transformé en un script shell, en préfixant tout son contenu avec une ligne spéciale qui indique quel exécutable utiliser pour l'exécuter.

Sur mon système, l'exécutable Python est situé dans `/usr/bin/python3`, donc je tape `#!/usr/bin/python3` dans la première ligne :

![Screen-Shot-2020-11-10-at-14.17.26](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.17.26.png)

Ensuite, je peux définir la permission d'exécution sur le fichier :

```sh
chmod u+x program.py
```

et je peux exécuter le programme avec

```sh
./program.py
```

![Screen-Shot-2020-11-10-at-14.18.42](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.18.42.png)

Cela est particulièrement utile lorsque vous écrivez des scripts qui interagissent avec le terminal.

Nous avons de nombreuses autres façons d'exécuter des programmes Python.

L'une d'entre elles est d'utiliser VS Code, et en particulier l'extension officielle Python de Microsoft :

![Screen-Shot-2020-11-10-at-14.23.32](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.23.32.png)

Après avoir installé cette extension, vous aurez la complétion automatique du code Python et la vérification des erreurs, la mise en forme automatique et le linting du code avec `pylint`, ainsi que quelques commandes spéciales, notamment :

**Python : Démarrer le REPL** pour exécuter le REPL dans le terminal intégré :

![Screen-Shot-2020-11-10-at-14.31.36](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.31.36.png)

**Python : Exécuter le fichier Python dans le terminal** pour exécuter le fichier actuel dans le terminal :

![Screen-Shot-2020-11-10-at-14.31.06](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.31.06.png)

**Python : Exécuter le fichier actuel dans la fenêtre interactive Python** :

![Screen-Shot-2020-11-10-at-14.30.02-1](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.30.02-1.png)

et bien d'autres. Il suffit d'ouvrir la palette de commandes (Affichage -> Palette de commandes, ou Cmd-Maj-P) et de taper `python` pour voir toutes les commandes liées à Python :

![Screen-Shot-2020-11-10-at-14.30.02](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.30.02.png)

Une autre façon d'exécuter facilement du code Python est d'utiliser repl.it, un site très pratique qui fournit un environnement de codage où vous pouvez créer et exécuter vos applications, dans n'importe quel langage, y compris Python :

![Screen-Shot-2020-11-10-at-14.33.58](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.33.58.png)

Inscription (c'est gratuit), puis sous "create a repl" cliquez sur Python :

![Screen-Shot-2020-11-10-at-14.46.34](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.46.34.png)

et vous verrez immédiatement un éditeur avec un fichier `main.py`, prêt à être rempli avec beaucoup de code Python :

![Screen-Shot-2020-11-10-at-14.47.15](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.47.15.png)

Une fois que vous avez du code, cliquez sur "Run" pour l'exécuter sur le côté droit de la fenêtre :

![Screen-Shot-2020-11-10-at-14.48.09](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2020-11-10-at-14.48.09.png)

Je pense que repl.it est pratique car :

- vous pouvez facilement partager du code simplement en partageant le lien
- plusieurs personnes peuvent travailler sur le même code
- il peut héberger des programmes de longue durée
- vous pouvez installer des packages
- il vous fournit une base de données clé-valeur pour des applications plus complexes


## Python 2 vs Python 3

Un sujet clé que nous devons aborder, dès le départ, est la discussion Python 2 vs Python 3.

Python 3 a été introduit en 2008, et il est en développement comme version principale de Python, tandis que Python 2 a continué à être maintenu avec des corrections de bugs et des correctifs de sécurité jusqu'au début de l'année 2020.

À cette date, le support de Python 2 a été abandonné.

De nombreux programmes sont encore écrits en utilisant Python 2, et des organisations continuent de travailler activement sur ceux-ci, car la migration vers Python 3 n'est pas triviale et nécessiterait beaucoup de travail pour mettre à jour ces programmes. Et les grandes et importantes migrations introduisent toujours de nouveaux bugs.

Mais le nouveau code, sauf si vous devez vous conformer à des règles établies par votre organisation qui impose Python 2, doit toujours être écrit en Python 3.

> Ce livre se concentre sur Python 3. 


## Les bases de Python

### Variables en Python

Nous pouvons créer une nouvelle variable Python en attribuant une valeur à une étiquette, en utilisant l'opérateur d'affectation `=`.

Dans cet exemple, nous attribuons une chaîne avec la valeur "Roger" à l'étiquette `name` :

```python
name = "Roger"
```

Voici un exemple avec un nombre :

```python
age = 8
```

Un nom de variable peut être composé de caractères, de chiffres et du caractère de soulignement `_`. Il ne peut pas commencer par un chiffre. Ce sont tous des noms de variables **valides** :

```python
name1
AGE
aGE
a11111
my_name
_name
```

Ce sont des noms de variables **invalides** :

```python
123
test!
name%
```

Autre que cela, tout est valide sauf si c'est un **mot-clé** Python. Il y a quelques mots-clés comme `for`, `if`, `while`, `import` et plus encore.

Il n'est pas nécessaire de les mémoriser, car Python vous alertera si vous utilisez l'un d'eux comme variable, et vous les reconnaîtrez progressivement comme faisant partie de la syntaxe du langage de programmation Python.

### Expressions et instructions en Python

Nous pouvons _exprimer_ tout type de code qui retourne une valeur. Par exemple

```python
1 + 1
"Roger"
```

Une instruction, en revanche, est une opération sur une valeur. Par exemple, ce sont 2 instructions :

```python
name = "Roger"
print(name)
```

Un programme est formé par une série d'instructions. Chaque instruction est placée sur sa propre ligne, mais vous pouvez utiliser un point-virgule pour avoir plus d'une instruction sur une seule ligne :

```python
name = "Roger"; print(name)
```

### Commentaires

Dans un programme Python, tout ce qui suit un symbole de dièse est ignoré et considéré comme un commentaire :

```python
#this is a commented line

name = "Roger" # this is an inline comment
```

### Indentation en Python

L'indentation en Python est significative.

Vous ne pouvez pas indenter aléatoirement comme ceci :

```python
name = "Flavio"
    print(name)
```

Certains autres langages n'ont pas d'espaces blancs significatifs, mais en Python, l'indentation compte.

Dans ce cas, si vous essayez d'exécuter ce programme, vous obtiendrez une erreur `IndentationError: unexpected indent`, car l'indentation a une signification spéciale.

Tout ce qui est indenté appartient à un bloc, comme une instruction de contrôle ou un bloc conditionnel, ou le corps d'une fonction ou d'une classe. Nous verrons plus de détails à ce sujet plus tard.


## Types de données en Python

Python a plusieurs types intégrés.

Si vous créez la variable `name` en lui attribuant la valeur "Roger", automatiquement cette variable représente maintenant un type de données **String**.

```python
name = "Roger"
```

Vous pouvez vérifier le type d'une variable en utilisant la fonction `type()`, en passant la variable comme argument, puis en comparant le résultat à `str` :

```python
name = "Roger"
type(name) == str #True
```

Ou en utilisant `isinstance()` :

```python
name = "Roger"
isinstance(name, str) #True
```

> Remarquez que pour voir la valeur `True` en Python, en dehors d'un REPL, vous devez envelopper ce code dans `print()`, mais pour plus de clarté, je l'évite.

Nous avons utilisé la classe `str` ici, mais cela fonctionne de la même manière pour les autres types de données.

Tout d'abord, nous avons les nombres. Les nombres entiers sont représentés en utilisant la classe `int`. Les nombres à virgule flottante (fractions) sont de type `float` :

```python
age = 1
type(age) == int #True
```

```python
fraction = 0.1
type(fraction) == float #True
```

Vous avez vu comment créer un type à partir d'une valeur littérale, comme ceci :

```python
name = "Flavio"
age = 20
```

Python détecte automatiquement le type à partir du type de valeur.

Vous pouvez également créer une variable d'un type spécifique en utilisant le constructeur de classe, en passant une valeur littérale ou un nom de variable :

```python
name = str("Flavio")
anotherName = str(name)
```

Vous pouvez également convertir d'un type à un autre en utilisant le constructeur de classe. Python essaiera de déterminer la valeur correcte, par exemple en extrayant un nombre d'une chaîne :

```python
age = int("20")
print(age) #20

fraction = 0.1
intFraction = int(fraction)
print(intFraction) #0
```

Cela s'appelle le **casting**. Bien sûr, cette conversion ne fonctionne pas toujours en fonction de la valeur passée. Si vous écrivez `test` au lieu de `20` dans la chaîne ci-dessus, vous obtiendrez une erreur `ValueError: invalid literal for int() with base 10: 'test'`.

Ce ne sont là que les bases des types. Nous avons beaucoup plus de types en Python :

- `complex` pour les nombres complexes
- `bool` pour les booléens
- `list` pour les listes
- `tuple` pour les tuples
- `range` pour les plages
- `dict` pour les dictionnaires
- `set` pour les ensembles

et plus encore !

Nous allons les explorer tous bientôt.


## Opérateurs en Python

Les opérateurs Python sont des symboles que nous utilisons pour exécuter des opérations sur des valeurs et des variables.

Nous pouvons diviser les opérateurs en fonction du type d'opération qu'ils effectuent :

- opérateur d'affectation
- opérateurs arithmétiques
- opérateurs de comparaison
- opérateurs logiques
- opérateurs bit à bit

plus quelques-uns intéressants comme `is` et `in`.

### Opérateur d'affectation en Python

L'opérateur d'affectation est utilisé pour affecter une valeur à une variable :

```python
age = 8
```

Ou pour affecter la valeur d'une variable à une autre variable :

```python
age = 8
anotherVariable = age
```

Depuis Python 3.8, l'opérateur `:=` _walrus_ est utilisé pour affecter une valeur à une variable dans le cadre d'une autre opération. Par exemple à l'intérieur d'un `if` ou dans la partie conditionnelle d'une boucle. Plus d'informations à ce sujet plus tard.

### Opérateurs arithmétiques en Python

Python a un certain nombre d'opérateurs arithmétiques : `+`, `-`, `*`, `/` (division), `%` (reste), `**` (exponentiation) et `//` (division entière) :

```python
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
4 // 2 #2
```

> Notez que vous n'avez pas besoin d'espace entre les opérandes, mais c'est bon pour la lisibilité.

`-` fonctionne également comme opérateur unaire moins :

```python
print(-4) #-4
```

`+` est également utilisé pour concaténer des valeurs de type String :

```python
"Roger" + " is a good dog"
#Roger is a good dog
```

Nous pouvons combiner l'opérateur d'affectation avec les opérateurs arithmétiques :

- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
- ..et ainsi de suite

Exemple :

```python
age = 8
age += 1
# age est maintenant 9
```

### Opérateurs de comparaison en Python

Python définit quelques opérateurs de comparaison :

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Vous pouvez utiliser ces opérateurs pour obtenir une valeur booléenne (`True` ou `False`) en fonction du résultat :

```python
a = 1
b = 2

a == b #False
a != b #True
a > b #False
a <= b #True
```

### Opérateurs booléens en Python

Python nous donne les opérateurs booléens suivants :

- `not`
- `and`
- `or`

Lorsque vous travaillez avec des attributs `True` ou `False`, ceux-ci fonctionnent comme des ET, OU et NON logiques, et sont souvent utilisés dans l'évaluation de l'expression conditionnelle `if` :

```python
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True
```

Sinon, faites attention à une source possible de confusion :

`or` utilisé dans une expression retourne la valeur du premier opérande qui n'est pas une valeur fausse (`False`, `0`, `''`, `[]`..). Sinon, il retourne le dernier opérande.

```python
print(0 or 1) ## 1
print(False or 'hey') ## 'hey'
print('hi' or 'hey') ## 'hi'
print([] or False) ## 'False'
print(False or []) ## '[]'
```

La documentation Python le décrit comme `if x is false, then y, else x`.

`and` n'évalue le deuxième argument que si le premier est vrai. Donc si le premier argument est faux (`False`, `0`, `''`, `[]`..), il retourne cet argument. Sinon, il évalue le deuxième argument :

```python
print(0 and 1) ## 0
print(1 and 0) ## 0
print(False and 'hey') ## False
print('hi' and 'hey') ## 'hey'
print([] and False ) ## []
print(False and [] ) ## False
```

La documentation Python le décrit comme `if x is false, then x, else y`.

### Opérateurs bit à bit en Python

Certains opérateurs sont utilisés pour travailler sur les bits et les nombres binaires :

- `&` effectue un ET binaire
- `|` effectue un OU binaire
- `^` effectue une opération XOR binaire
- `~` effectue une opération NOT binaire
- `<<` décale à gauche
- `>>` décale à droite

Les opérateurs bit à bit sont rarement utilisés, uniquement dans des situations très spécifiques, mais ils valent la peine d'être mentionnés.

### `is` et `in` en Python

`is` est appelé l'**opérateur d'identité**. Il est utilisé pour comparer deux objets et retourne vrai si les deux sont le même objet. Plus d'informations sur les objets plus tard.

`in` est appelé l'**opérateur d'appartenance**. Il est utilisé pour indiquer si une valeur est contenue dans une liste, ou une autre séquence. Plus d'informations sur les listes et autres séquences plus tard.


## L'opérateur ternaire en Python

L'opérateur ternaire en Python vous permet de définir rapidement une condition.

Supposons que vous avez une fonction qui compare une variable `age` à la valeur `18`, et retourne True ou False en fonction du résultat.

Au lieu d'écrire :

```python
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
```

Vous pouvez l'implémenter avec l'opérateur ternaire de cette manière :

```python
def is_adult(age):
    return True if age > 18 else False
```

D'abord, vous définissez le résultat si la condition est vraie, puis vous évaluez la condition, puis vous définissez le résultat si la condition est fausse :

```python
<result_if_true> if <condition> else <result_if_false>
```


## Chaînes de caractères en Python

Une chaîne de caractères en Python est une série de caractères enfermés dans des guillemets ou des guillemets doubles :

```python
"Roger"
'Roger'
```

Vous pouvez attribuer une valeur de chaîne à une variable :

```python
name = "Roger"
```

Vous pouvez concaténer deux chaînes en utilisant l'opérateur `+` :

```python
phrase = "Roger" + " is a good dog"
```

Vous pouvez ajouter à une chaîne en utilisant `+=` :

```python
name = "Roger"
name += " is a good dog"

print(name) #Roger is a good dog
```

Vous pouvez convertir un nombre en chaîne en utilisant le constructeur de classe `str` :

```python
str(8) #"8"
```

Cela est essentiel pour concaténer un nombre à une chaîne :

```python
print("Roger is " + str(8) + " years old") #Roger is 8 years old
```

Une chaîne peut être multiline lorsqu'elle est définie avec une syntaxe spéciale, en enfermant la chaîne dans un ensemble de 3 guillemets :

```python
print("""Roger is

    8

years old
""")

#double quotes, or single quotes

print('''
Roger is

    8

years old
''')
```

Une chaîne a un ensemble de méthodes intégrées, comme :

- `isalpha()` pour vérifier si une chaîne ne contient que des caractères et n'est pas vide
- `isalnum()` pour vérifier si une chaîne contient des caractères ou des chiffres et n'est pas vide
- `isdecimal()` pour vérifier si une chaîne contient des chiffres et n'est pas vide
- `lower()` pour obtenir une version en minuscules d'une chaîne
- `islower()` pour vérifier si une chaîne est en minuscules
- `upper()` pour obtenir une version en majuscules d'une chaîne
- `isupper()` pour vérifier si une chaîne est en majuscules
- `title()` pour obtenir une version capitalisée d'une chaîne
- `startsswith()` pour vérifier si la chaîne commence par une sous-chaîne spécifique
- `endswith()` pour vérifier si la chaîne se termine par une sous-chaîne spécifique
- `replace()` pour remplacer une partie d'une chaîne
- `split()` pour diviser une chaîne sur un caractère séparateur spécifique
- `strip()` pour supprimer les espaces blancs d'une chaîne
- `join()` pour ajouter de nouvelles lettres à une chaîne
- `find()` pour trouver la position d'une sous-chaîne

et bien d'autres.

Aucune de ces méthodes ne modifie la chaîne d'origine. Elles retournent une nouvelle chaîne modifiée à la place. Par exemple :

```python
name = "Roger"
print(name.lower()) #"roger"
print(name) #"Roger"
```

Vous pouvez utiliser certaines fonctions globales pour travailler avec des chaînes, également.

En particulier, je pense à `len()`, qui vous donne la longueur d'une chaîne :

```python
name = "Roger"
print(len(name)) #5
```

L'opérateur `in` vous permet de vérifier si une chaîne contient une sous-chaîne :

```python
name = "Roger"
print("ger" in name) #True
```

L'échappement est un moyen d'ajouter des caractères spéciaux dans une chaîne.

Par exemple, comment ajouter un guillemet double dans une chaîne qui est enveloppée dans des guillemets doubles ?

```python
name = "Roger"
```

`"Ro"Ger"` ne fonctionnera pas, car Python pensera que la chaîne se termine à `"Ro"`.

La solution est d'échapper le guillemet double à l'intérieur de la chaîne, avec le caractère d'échappement `\` :

```python
name = "Ro\"ger"
```

Cela s'applique également aux guillemets simples `\'`, et pour les caractères de formatage spéciaux comme `\t` pour la tabulation, `\n` pour la nouvelle ligne et `\\` pour le backslash.

Étant donné une chaîne, vous pouvez obtenir ses caractères en utilisant des crochets pour obtenir un élément spécifique, étant donné son index, en commençant par 0 :

```python
name = "Roger"
name[0] #'R'
name[1] #'o'
name[2] #'g'
```

L'utilisation d'un nombre négatif commencera à compter à partir de la fin :

```python
name = "Roger"
name[-1] #"r"
```

Vous pouvez également utiliser une plage, en utilisant ce que nous appelons le **slicing** :

```python
name = "Roger"
name[0:2] #"Ro"
name[:2] #"Ro"
name[2:] #"ger"
```


## Booléens en Python

Python fournit le type `bool`, qui peut avoir deux valeurs : `True` et `False` (avec une majuscule).

```python
done = False
done = True
```

Les booléens sont particulièrement utiles avec des structures de contrôle conditionnelles comme les instructions `if` :

```python
done = True

if done:
    # exécuter du code ici
else:
    # exécuter un autre code
```

Lors de l'évaluation d'une valeur pour `True` ou `False`, si la valeur n'est pas un `bool`, nous avons quelques règles en fonction du type que nous vérifions :

- les nombres sont toujours `True` sauf pour le nombre `0`
- les chaînes sont `False` uniquement lorsqu'elles sont vides
- les listes, tuples, ensembles et dictionnaires sont `False` uniquement lorsqu'ils sont vides

Vous pouvez vérifier si une valeur est un booléen de cette manière :

```python
done = True
type(done) == bool #True
```

Ou en utilisant `isinstance()`, en passant 2 arguments : la variable, et la classe `bool` :

```python
done = True
isinstance(done, bool) #True
```

La fonction globale `any()` est également très utile lorsque vous travaillez avec des booléens, car elle retourne `True` si l'une des valeurs de l'itérable (liste, par exemple) passée en argument est `True` :

```python
book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
```

La fonction globale `all()` est similaire, mais retourne `True` si toutes les valeurs qui lui sont passées sont `True` :

```python
ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
```


## Nombres en Python

Les nombres en Python peuvent être de 3 types : `int`, `float` et `complex`.

### Nombres entiers en Python

Les nombres entiers sont représentés en utilisant la classe `int`. Vous pouvez définir un entier en utilisant une valeur littérale :

```python
age = 8
```

Vous pouvez également définir un nombre entier en utilisant le constructeur `int()` :

```python
age = int(8)
```

Pour vérifier si une variable est de type `int`, vous pouvez utiliser la fonction globale `type()` :

```python
type(age) == int #True
```

### Nombres à virgule flottante en Python

Les nombres à virgule flottante (fractions) sont de type `float`. Vous pouvez définir un entier en utilisant une valeur littérale :

```python
fraction = 0.1
```

Ou en utilisant le constructeur `float()` :

```python
fraction = float(0.1)
```

Pour vérifier si une variable est de type `float`, vous pouvez utiliser la fonction globale `type()` :

```python
type(fraction) == float #True
```

### Nombres complexes en Python

Les nombres complexes sont de type `complex`.

Vous pouvez les définir en utilisant une valeur littérale :

```python
complexNumber = 2+3j
```

ou en utilisant le constructeur `complex()` :

```python
complexNumber = complex(2, 3)
```

Une fois que vous avez un nombre complexe, vous pouvez obtenir sa partie réelle et imaginaire :

```python
complexNumber.real #2.0
complexNumber.imag #3.0
```

Encore une fois, pour vérifier si une variable est de type `complex`, vous pouvez utiliser la fonction globale `type()` :

```python
type(complexNumber) == complex #True
```

### Opérations arithmétiques sur les nombres en Python

Vous pouvez effectuer des opérations arithmétiques sur les nombres, en utilisant les opérateurs arithmétiques : `+`, `-`, `*`, `/` (division), `%` (reste), `**` (exponentiation) et `//` (division entière) :

```python
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
4 // 2 #2
```

et vous pouvez utiliser les opérateurs d'affectation composés

- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
- ..et ainsi de suite

pour effectuer rapidement des opérations sur des variables, également :

```python
age = 8
age += 1
```

### Fonctions intégrées en Python

Il existe 2 fonctions intégrées qui aident avec les nombres :

`abs()` retourne la valeur absolue d'un nombre.

`round()` étant donné un nombre, retourne sa valeur arrondie à l'entier le plus proche :

```python
round(0.12) #0
```

Vous pouvez spécifier un deuxième paramètre pour définir la précision du point décimal :

```python
round(0.12, 1) #0.1
```

Plusieurs autres fonctions utilitaires mathématiques et constantes sont fournies par la bibliothèque standard de Python :

- le package `math` fournit des fonctions et constantes mathématiques générales
- le package `cmath` fournit des utilitaires pour travailler avec des nombres complexes.
- le package `decimal` fournit des utilitaires pour travailler avec des décimaux et des nombres à virgule flottante.
- le package `fractions` fournit des utilitaires pour travailler avec des nombres rationnels.

Nous explorerons certains d'entre eux séparément plus tard.


## Constantes en Python

Python n'a aucun moyen de forcer une variable à être une constante.

La solution la plus proche est d'utiliser une énumération :

```Python
class Constants(Enum):
    WIDTH = 1024
    HEIGHT = 256
```

Et accéder à chaque valeur en utilisant, par exemple, `Constants.WIDTH.value`.

Personne ne peut réassigner cette valeur.

Sinon, si vous souhaitez vous fier aux conventions de nommage, vous pouvez adhérer à celle-ci : déclarer les variables qui ne devraient jamais changer en majuscules :

```python
WIDTH = 1024
```

Personne ne vous empêchera de remplacer cette valeur, et Python ne l'arrêtera pas.

C'est ce que fait la plupart du code Python que vous verrez.


## Énumérations en Python

Les énumérations sont des noms lisibles qui sont liés à une valeur constante.

Pour utiliser les énumérations, importez `Enum` depuis le module de bibliothèque standard `enum` :

```python
from enum import Enum
```

Ensuite, vous pouvez initialiser une nouvelle énumération de cette manière :

```python
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
```

Une fois que vous avez fait cela, vous pouvez référencer `State.INACTIVE` et `State.ACTIVE`, et ils servent de constantes.

Maintenant, si vous essayez d'imprimer `State.ACTIVE` par exemple :

```python
print(State.ACTIVE)
```

il ne retournera pas `1`, mais `State.ACTIVE`.

La même valeur peut être atteinte par le nombre assigné dans l'énumération : `print(State(1))` retournera `State.ACTIVE`. Même chose pour utiliser la notation entre crochets `State['ACTIVE']`.

Vous pouvez, cependant, obtenir la valeur en utilisant `State.ACTIVE.value`.

Vous pouvez lister toutes les valeurs possibles d'une énumération :

```python
list(State) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
```

Vous pouvez les compter :

```python
len(State) # 2
```


## Saisie utilisateur en Python

Dans une application en ligne de commande Python, vous pouvez afficher des informations à l'utilisateur en utilisant la fonction `print()` :

```python
name = "Roger"
print(name)
```

Nous pouvons également accepter une entrée de l'utilisateur, en utilisant `input()` :

```python
print('What is your age?')
age = input()
print('Your age is ' + age)
```

Cette approche obtient une entrée au moment de l'exécution, ce qui signifie que le programme arrêtera l'exécution et attendra jusqu'à ce que l'utilisateur tape quelque chose et appuie sur la touche `enter`.

Vous pouvez également faire un traitement d'entrée plus complexe et accepter une entrée au moment de l'invocation du programme, et nous verrons comment faire cela plus tard.

Cela fonctionne pour les applications en ligne de commande. D'autres types d'applications auront besoin d'une autre façon d'accepter une entrée.


## Instructions de contrôle en Python

Lorsque vous traitez avec des booléens, et des expressions qui retournent un booléen en particulier, nous pouvons prendre des décisions et emprunter différents chemins en fonction de leurs valeurs `True` ou `False`.

En Python, nous le faisons en utilisant l'instruction `if` :

```python
condition = True

if condition == True:
    # faire quelque chose
```

Lorsque le test de condition se résout à `True`, comme dans le cas ci-dessus, son bloc est exécuté.

Qu'est-ce qu'un bloc ? Un bloc est cette partie qui est indentée d'un niveau (4 espaces généralement) à droite :

```python
condition = True

if condition == True:
    print("La condition")
    print("était vraie")
```

Le bloc peut être formé par une seule ligne, ou plusieurs lignes également, et il se termine lorsque vous revenez au niveau d'indentation précédent :

```python
condition = True

if condition == True:
    print("La condition")
    print("était vraie")

print("En dehors du if")
```

En combinaison avec `if`, vous pouvez avoir un bloc `else` qui est exécuté si le test de condition de `if` donne `False` :

```python
condition = True

if condition == True:
    print("La condition")
    print("était vraie")
else:
    print("La condition")
    print("était fausse")
```

Et vous pouvez avoir différents `if` liés avec `elif` qui est exécuté si le contrôle précédent était `False` :

```python
condition = True
name = "Roger"

if condition == True:
    print("La condition")
    print("était vraie")
elif name == "Roger":
    print("Bonjour Roger")
else:
    print("La condition")
    print("était fausse")
```

Le deuxième bloc dans ce cas est exécuté si `condition` est `False`, et que la valeur de la variable `name` est "Roger".

Dans une instruction `if`, vous pouvez avoir un seul `if` et `else`, mais plusieurs séries de `elif` :

```python
condition = True
name = "Roger"

if condition == True:
    print("La condition")
    print("était vraie")
elif name == "Roger":
    print("Bonjour Roger")
elif name == "Syd":
    print("Bonjour Syd")
elif name == "Flavio":
    print("Bonjour Flavio")
else:
    print("La condition")
    print("était fausse")
```

`if` et `else` peuvent également être utilisés dans un format en ligne, ce qui nous permet de retourner une valeur ou une autre en fonction d'une condition.

Exemple :

```python
a = 2
result = 2 if a == 0 else 3
print(result) # 3
```


## Listes en Python

Les listes sont une structure de données essentielle en Python.

Elles vous permettent de regrouper plusieurs valeurs et de les référencer toutes avec un nom commun.

Par exemple :

```python
dogs = ["Roger", "Syd"]
```

Une liste peut contenir des valeurs de différents types :

```python
items = ["Roger", 1, "Syd", True]
```

Vous pouvez vérifier si un élément est contenu dans une liste avec l'opérateur `in` :

```python
print("Roger" in items) # True
```

Une liste peut également être définie comme vide :

```python
items = []
```

Vous pouvez référencer les éléments d'une liste par leur index, en commençant par zéro :

```python
items[0] # "Roger"
items[1] # 1
items[3] # True
```

En utilisant la même notation, vous pouvez changer la valeur stockée à un index spécifique :

```python
items[0] = "Roger"
```

Vous pouvez également utiliser la méthode `index()` :

```python
items.index(0) # "Roger"
items.index(1) # 1
```

Comme avec les chaînes, l'utilisation d'un index négatif commencera la recherche à partir de la fin :

```python
items[-1] # True
```

Vous pouvez également extraire une partie d'une liste, en utilisant des tranches :

```python
items[0:2] # ["Roger", 1]
items[2:] # ["Syd", True]
```

Obtenez le nombre d'éléments contenus dans une liste en utilisant la fonction globale `len()`, la même que nous avons utilisée pour obtenir la longueur d'une chaîne :

```python
len(items) #4
```

Vous pouvez ajouter des éléments à la liste en utilisant la méthode `append()` de la liste :

```python
items.append("Test")
```

ou la méthode extend() :

```python
items.extend(["Test"])
```

Vous pouvez également utiliser l'opérateur `+=` :

```python
items += ["Test"]

# items est ['Roger', 1, 'Syd', True, 'Test']
```

> Astuce : avec `extend()` ou `+=` n'oubliez pas les crochets. Ne faites pas `items += "Test"` ou `items.extend("Test")` ou Python ajoutera 4 caractères individuels à la liste, résultant en `['Roger', 1, 'Syd', True, 'T', 'e', 's', 't']`

Retirez un élément en utilisant la méthode `remove()` :

```python
items.remove("Test")
```

Vous pouvez ajouter plusieurs éléments en utilisant

```python
items += ["Test1", "Test2"]

#ou

items.extend(["Test1", "Test2"])
```

Celles-ci ajoutent l'élément à la fin de la liste.

Pour ajouter un élément au milieu d'une liste, à un index spécifique, utilisez la méthode `insert()` :

```python
items.insert("Test", 1) # ajoute "Test" à l'index 1
```

Pour ajouter plusieurs éléments à un index spécifique, vous devez utiliser des tranches :

```python
items[1:1] = ["Test1", "Test2"]
```

Triez une liste en utilisant la méthode `sort()` :

```python
items.sort()
```

> Astuce : sort() ne fonctionnera que si la liste contient des valeurs qui peuvent être comparées. Les chaînes et les entiers, par exemple, ne peuvent pas être comparés, et vous obtiendrez une erreur comme `TypeError: '<' not supported between instances of 'int' and 'str'` si vous essayez.

La méthode `sort()` trie d'abord les lettres majuscules, puis les lettres minuscules. Pour corriger cela, utilisez :

```python
items.sort(key=str.lower)
```

au lieu de cela.

Le tri modifie le contenu original de la liste. Pour éviter cela, vous pouvez copier le contenu de la liste en utilisant

```python
itemscopy = items[:]
```

ou utiliser la fonction globale `sorted()` :

```python
print(sorted(items, key=str.lower))
```

qui retournera une nouvelle liste, triée, au lieu de modifier la liste originale.


## Tuples en Python

Les tuples sont une autre structure de données fondamentale en Python.

Ils vous permettent de créer des groupes immuables d'objets. Cela signifie qu'une fois qu'un tuple est créé, il ne peut pas être modifié. Vous ne pouvez pas ajouter ou supprimer d'éléments.

Ils sont créés de manière similaire aux listes, mais en utilisant des parenthèses au lieu de crochets :

```python
names = ("Roger", "Syd")
```

Un tuple est ordonné, comme une liste, donc vous pouvez obtenir ses valeurs en référençant une valeur d'index :

```python
names[0] # "Roger"
names[1] # "Syd"
```

Vous pouvez également utiliser la méthode `index()` :

```python
names.index('Roger') # 0
names.index('Syd')   # 1
```

Comme avec les chaînes et les listes, l'utilisation d'un index négatif commencera la recherche à partir de la fin :

```python
names[-1] # True
```

Vous pouvez compter les éléments dans un tuple avec la fonction `len()` :

```python
len(names) # 2
```

Vous pouvez vérifier si un élément est contenu dans un tuple avec l'opérateur `in` :

```python
print("Roger" in names) # True
```

Vous pouvez également extraire une partie d'un tuple, en utilisant des tranches :

```python
names[0:2] # ('Roger', 'Syd')
names[1:] # ('Syd',)
```

Obtenez le nombre d'éléments dans un tuple en utilisant la fonction globale `len()`, la même que nous avons utilisée pour obtenir la longueur d'une chaîne :

```python
len(names) #2
```

Vous pouvez créer une version triée d'un tuple en utilisant la fonction globale `sorted()` :

```python
sorted(names)
```

Vous pouvez créer un nouveau tuple à partir de tuples existants en utilisant l'opérateur `+` :

```python
newTuple = names + ("Vanille", "Tina")
```


## Dictionnaires en Python

Les dictionnaires sont une structure de données très importante en Python.

Alors que les listes vous permettent de créer des collections de valeurs, les dictionnaires vous permettent de créer des collections de **paires clé/valeur**.

Voici un exemple de dictionnaire avec une paire clé/valeur :

```python
dog = { 'name': 'Roger' }
```

La clé peut être n'importe quelle valeur immuable comme une chaîne, un nombre ou un tuple. La valeur peut être n'importe quoi.

Un dictionnaire peut contenir plusieurs paires clé/valeur :

```python
dog = { 'name': 'Roger', 'age': 8 }
```

Vous pouvez accéder aux valeurs individuelles des clés en utilisant cette notation :

```python
dog['name'] # 'Roger'
dog['age']  # 8
```

En utilisant la même notation, vous pouvez changer la valeur stockée à un index spécifique :

```python
dog['name'] = 'Syd'
```

Et une autre façon est d'utiliser la méthode `get()`, qui a une option pour ajouter une valeur par défaut :

```python
dog.get('name') # 'Roger'
dog.get('test', 'default') # 'default'
```

La méthode `pop()` récupère la valeur d'une clé, et supprime ensuite l'élément du dictionnaire :

```python
dog.pop('name') # 'Roger'
```

La méthode `popitem()` récupère et supprime la dernière paire clé/valeur insérée dans le dictionnaire :

```python
dog.popitem()
```

Vous pouvez vérifier si une clé est contenue dans un dictionnaire avec l'opérateur `in` :

```python
'name' in dog # True
```

Obtenez une liste avec les clés dans un dictionnaire en utilisant la méthode `keys()`, en passant son résultat au constructeur `list()` :

```python
list(dog.keys()) # ['name', 'age']
```

Obtenez les valeurs en utilisant la méthode `values()`, et les paires clé/valeur en utilisant la méthode `items()` :

```python
print(list(dog.values()))
# ['Roger', 8]

print(list(dog.items()))
# [('name', 'Roger'), ('age', 8)]
```

Obtenez la longueur d'un dictionnaire en utilisant la fonction globale `len()`, la même que nous avons utilisée pour obtenir la longueur d'une chaîne ou les éléments dans une liste :

```python
len(dog) #2
```

Vous pouvez ajouter une nouvelle paire clé/valeur au dictionnaire de cette manière :

```python
dog['favorite food'] = 'Meat'
```

Vous pouvez supprimer une paire clé/valeur d'un dictionnaire en utilisant l'instruction `del` :

```python
del dog['favorite food']
```

Pour copier un dictionnaire, utilisez la méthode copy() :

```python
dogCopy = dog.copy()
```


## Ensembles en Python

Les ensembles sont une autre structure de données importante en Python.

Nous pouvons dire qu'ils fonctionnent comme des tuples, mais ils ne sont pas ordonnés, et ils sont **mutables**.

Ou nous pouvons dire qu'ils fonctionnent comme des dictionnaires, mais ils n'ont pas de clés.

Ils ont également une version immuable, appelée `frozenset`.

Vous pouvez créer un ensemble en utilisant cette syntaxe :

```python
names = {"Roger", "Syd"}
```

Les ensembles fonctionnent bien lorsque vous les considérez comme des ensembles mathématiques.

Vous pouvez intersecter deux ensembles :

```python
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2 #{'Roger'}
```

Vous pouvez créer une union de deux ensembles :

```python
set1 = {"Roger", "Syd"}
set2 = {"Luna"}

union = set1 | set2
#{'Syd', 'Luna', 'Roger'}
```

Vous pouvez obtenir la différence entre deux ensembles :

```python
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

difference = set1 - set2 #{'Syd'}
```

Vous pouvez vérifier si un ensemble est un sur-ensemble d'un autre (et bien sûr si un ensemble est un sous-ensemble d'un autre) :

```python
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

isSuperset = set1 > set2 # True
```

Vous pouvez compter les éléments dans un ensemble avec la fonction globale `len()` :

```python
names = {"Roger", "Syd"}
len(names) # 2
```

Vous pouvez obtenir une liste à partir des éléments d'un ensemble en passant l'ensemble au constructeur `list()` :

```python
names = {"Roger", "Syd"}
list(names) #['Syd', 'Roger']
```

Vous pouvez vérifier si un élément est contenu dans un ensemble avec l'opérateur `in` :

```python
print("Roger" in names) # True
```


## Fonctions en Python

Une fonction nous permet de créer un ensemble d'instructions que nous pouvons exécuter lorsque cela est nécessaire.

Les fonctions sont essentielles en Python et dans de nombreux autres langages de programmation. Elles nous aident à créer des programmes significatifs, car elles nous permettent de décomposer un programme en parties gérables, et elles favorisent la lisibilité et la réutilisation du code.

Voici un exemple de fonction appelée `hello` qui imprime "Hello!" :

```python
def hello():
    print('Hello!')
```

C'est la **définition** de la fonction. Il y a un nom (`hello`) et un corps, l'ensemble des instructions, qui est la partie qui suit le deux-points. Il est indenté d'un niveau à droite.

Pour exécuter cette fonction, nous devons l'appeler. Voici la syntaxe pour appeler la fonction :

```python
hello()
```

Nous pouvons exécuter cette fonction une fois, ou plusieurs fois.

Le nom de la fonction, `hello`, est très important. Il doit être descriptif, afin que quiconque l'appelle puisse imaginer ce que fait la fonction.

Une fonction peut accepter un ou plusieurs paramètres :

```python
def hello(name):
    print('Hello ' + name + '!')
```

Dans ce cas, nous appelons la fonction en passant l'argument

```python
hello('Roger')
```

> Nous appelons _paramètres_ les valeurs acceptées par la fonction à l'intérieur de la définition de la fonction, et _arguments_ les valeurs que nous passons à la fonction lorsque nous l'appelons. Il est courant de confondre cette distinction.

Un argument peut avoir une valeur par défaut qui est appliquée si l'argument n'est pas spécifié :

```python
def hello(name='my friend'):
    print('Hello ' + name + '!')

hello()
#Hello my friend!
```

Voici comment nous pouvons accepter plusieurs paramètres :

```python
def hello(name, age):
    print('Hello ' + name + ', you are ' + str(age) + ' years old!')
```

Dans ce cas, nous appelons la fonction en passant un ensemble d'arguments :

```python
hello('Roger', 8)
```

Les paramètres sont passés par référence. Tous les types en Python sont des objets, mais certains d'entre eux sont immuables, y compris les entiers, les booléens, les flottants, les chaînes et les tuples. Cela signifie que si vous les passez en tant que paramètres et que vous modifiez leur valeur à l'intérieur de la fonction, la nouvelle valeur n'est pas reflétée à l'extérieur de la fonction :

```python
def change(value):
    value = 2

val = 1
change(val)

print(val) #1
```

Si vous passez un objet qui n'est pas immuable, et que vous changez l'une de ses propriétés, le changement sera reflété à l'extérieur.

Une fonction peut retourner une valeur, en utilisant l'instruction `return`. Par exemple, dans ce cas, nous retournons le nom du paramètre `name` :

```python
def hello(name):
    print('Hello ' + name + '!')
    return name
```

Lorsque la fonction rencontre l'instruction `return`, la fonction se termine.

Nous pouvons omettre la valeur :

```python
def hello(name):
    print('Hello ' + name + '!')
    return
```

Nous pouvons avoir l'instruction return à l'intérieur d'une conditionnelle, ce qui est une manière courante de terminer une fonction si une condition initiale n'est pas remplie :

```python
def hello(name):
    if not name:
        return
    print('Hello ' + name + '!')
```

Si nous appelons la fonction en passant une valeur qui évalue à `False`, comme une chaîne vide, la fonction est terminée avant d'atteindre l'instruction `print()`.

Vous pouvez retourner plusieurs valeurs en utilisant des valeurs séparées par des virgules :

```python
def hello(name):
    print('Hello ' + name + '!')
    return name, 'Roger', 8
```

Dans ce cas, l'appel de `hello('Syd')` retourne une valeur qui est un tuple contenant ces 3 valeurs : `('Syd', 'Roger', 8)`.


## Objets en Python

Tout en Python est un objet.

Même les valeurs des types primitifs de base (entier, chaîne, flottant..) sont des objets. Les listes sont des objets, tout comme les tuples, les dictionnaires, tout.

Les objets ont des **attributs** et des **méthodes** qui peuvent être accessibles en utilisant la syntaxe avec un point.

Par exemple, essayez de définir une nouvelle variable de type `int` :

```python
age = 8
```

`age` a maintenant accès aux propriétés et méthodes définies pour tous les objets `int`.

Cela inclut, par exemple, l'accès à la partie réelle et imaginaire de ce nombre :

```python
print(age.real) # 8
print(age.imag) # 0

print(age.bit_length()) #4

# la méthode bit_length() retourne le nombre de bits nécessaires pour représenter ce nombre en notation binaire
```

Une variable contenant une valeur de liste a accès à un ensemble différent de méthodes :

```python
items = [1, 2]
items.append(3)
items.pop()
```

Les méthodes dépendent du type de valeur.

La fonction globale `id()` fournie par Python vous permet d'inspecter l'emplacement en mémoire pour un objet particulier.

```python
id(age) # 140170065725376
```

> Votre valeur de mémoire changera - Je ne la montre qu'à titre d'exemple.

Si vous attribuez une valeur différente à la variable, son adresse changera, car le contenu de la variable a été remplacé par une autre valeur stockée à un autre endroit en mémoire :

```python
age = 8

print(id(age)) # 140535918671808

age = 9

print(id(age)) # 140535918671840
```

Mais si vous modifiez l'objet en utilisant ses méthodes, l'adresse reste la même :

```python
items = [1, 2]

print(id(items)) # 140093713593920

items.append(3)

print(items) # [1, 2, 3]
print(id(items)) # 140093713593920
```

L'adresse ne change que si vous réattribuez une variable à une autre valeur.

Certains objets sont _mutables_, tandis que d'autres sont _immuables_. Cela dépend de l'objet lui-même. 

Si l'objet fournit des méthodes pour changer son contenu, alors il est mutable. Sinon, il est immuable. 

La plupart des types définis par Python sont immuables. Par exemple, un `int` est immuable. Il n'y a pas de méthodes pour changer sa valeur. Si vous incrémentez la valeur en utilisant

```python
age = 8
age = age + 1

#ou

age += 1
```

et vous vérifiez avec `id(age)`, vous constaterez que `age` pointe vers un emplacement mémoire différent. La valeur d'origine n'a pas muté, nous avons simplement basculé vers une autre valeur.


## Boucles en Python

Les boucles sont une partie essentielle de la programmation.

En Python, nous avons 2 types de boucles : **les boucles while** et **les boucles for**.

### Les boucles `while` en Python

Les boucles `while` sont définies en utilisant le mot-clé `while`, et elles répètent leur bloc jusqu'à ce que la condition soit évaluée à `False` :

```python
condition = True
while condition == True:
    print("La condition est vraie")
```

C'est une **boucle infinie**. Elle ne se termine jamais.

Arrêtons la boucle juste après la première itération :

```python
condition = True
while condition == True:
    print("La condition est vraie")
    condition = False

print("Après la boucle")
```

Dans ce cas, la première itération est exécutée, car le test de condition est évalué à `True`. À la deuxième itération, le test de condition est évalué à `False`, donc le contrôle passe à l'instruction suivante après la boucle.

Il est courant d'avoir un compteur pour arrêter l'itération après un certain nombre de cycles :

```python
count = 0
while count < 10:
    print("La condition est vraie")
    count = count + 1

print("Après la boucle")
```

### Les boucles `for` en Python

En utilisant les boucles `for`, nous pouvons dire à Python d'exécuter un bloc pour un nombre prédéterminé de fois, à l'avance, et sans avoir besoin d'une variable séparée et d'une conditionnelle pour vérifier sa valeur.

Par exemple, nous pouvons itérer les éléments d'une liste :

```python
items = [1, 2, 3, 4]
for item in items:
    print(item)
```

Ou, vous pouvez itérer un nombre spécifique de fois en utilisant la fonction `range()` :

```python
for item in range(04):
    print(item)
```

`range(4)` crée une séquence qui commence à 0 et contient 4 éléments : `[0, 1, 2, 3]`.

Pour obtenir l'index, vous devez envelopper la séquence dans la fonction `enumerate()` :

```python
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)
```

### Break et continue en Python

Les boucles `while` et `for` peuvent être interrompues à l'intérieur du bloc, en utilisant deux mots-clés spéciaux : `break` et `continue`.

`continue` arrête l'itération actuelle et dit à Python d'exécuter la suivante.

`break` arrête complètement la boucle, et passe à l'instruction suivante après la fin de la boucle.

Le premier exemple ici imprime `1, 3, 4`. Le deuxième exemple imprime `1` :

```python
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)
```

```python
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break
    print(item)
```


## Classes en Python

En plus d'utiliser les types fournis par Python, nous pouvons déclarer nos propres classes, et à partir des classes, nous pouvons instancier des objets.

Un objet est une instance d'une classe. Une classe est le type d'un objet.

Nous pouvons définir une classe de cette manière :

```python
class <class_name>:
    # ma classe
```

Par exemple, définissons une classe Dog

```python
class Dog:
    # la classe Dog
```

Une classe peut définir des méthodes :

```python
class Dog:
    # la classe Dog
    def bark(self):
        print('WOF!')
```

> `self` en tant qu'argument de la méthode pointe vers l'instance d'objet actuelle, et doit être spécifié lors de la définition d'une méthode.

Nous créons une instance d'une classe, un **objet**, en utilisant cette syntaxe :

```python
roger = Dog()
```

Maintenant `roger` est un nouvel objet de type Dog.

Si vous exécutez

```python
print(type(roger))
```

Vous obtiendrez `<class '__main__.Dog'>`

Un type spécial de méthode, `__init__()` est appelé constructeur, et nous pouvons l'utiliser pour initialiser une ou plusieurs propriétés lorsque nous créons un nouvel objet à partir de cette classe :

```python
class Dog:
    # la classe Dog
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('WOF!')
```

Nous l'utilisons de cette manière :

```python
roger = Dog('Roger', 8)
print(roger.name) # 'Roger'
print(roger.age)  # 8

roger.bark() # 'WOF!'
```

Une caractéristique importante des classes est l'héritage.

Nous pouvons créer une classe Animal avec une méthode `walk()` :

```python
class Animal:
    def walk(self):
        print('Walking..')
```

et la classe Dog peut hériter de Animal :

```python
class Dog(Animal):
    def bark(self):
        print('WOF!')
```

Maintenant, créer un nouvel objet de classe `Dog` aura la méthode `walk()` car celle-ci est héritée de `Animal` :

```python
roger = Dog()
roger.walk() # 'Walking..'
roger.bark() # 'WOF!'
```


## Modules en Python

Chaque fichier Python est un module.

Vous pouvez importer un module depuis d'autres fichiers, et c'est la base de tout programme de complexité modérée, car il favorise une organisation sensée et la réutilisation du code.

Dans le programme Python typique, un fichier agit comme point d'entrée. Les autres fichiers sont des modules et exposent des fonctions que nous pouvons appeler depuis d'autres fichiers.

Le fichier `dog.py` contient ce code :

```python
def bark():
    print('WOF!')
```

Nous pouvons importer cette fonction depuis un autre fichier en utilisant `import`. Et une fois que nous le faisons, nous pouvons référencer la fonction en utilisant la notation par points, `dog.bark()` :

```python
import dog

dog.bark()
```

Ou, nous pouvons utiliser la syntaxe `from .. import` et appeler la fonction directement :

```python
from dog import bark

bark()
```

La première stratégie nous permet de charger tout ce qui est défini dans un fichier.

La deuxième stratégie nous permet de choisir les choses dont nous avons besoin.

Ces modules sont spécifiques à votre programme, et l'importation dépend de l'emplacement du fichier dans le système de fichiers.

Supposons que vous mettez `dog.py` dans un sous-dossier `lib`.

Dans ce dossier, vous devez créer un fichier vide nommé `__init__.py`. Cela indique à Python que le dossier contient des modules.

Maintenant, vous pouvez choisir - vous pouvez importer `dog` depuis `lib` :

```py
from lib import dog

dog.bark()
```

ou vous pouvez référencer la fonction spécifique du module `dog` en important depuis `lib.dog` :

```py
from lib.dog import bark

bark()
```


## La bibliothèque standard de Python

Python expose beaucoup de fonctionnalités intégrées à travers sa **bibliothèque standard**.

La bibliothèque standard est une énorme collection de toutes sortes d'utilitaires, allant des utilitaires mathématiques au débogage en passant par la création d'interfaces graphiques.

Vous pouvez trouver la liste complète des modules de la bibliothèque standard ici : https://docs.python.org/3/library/index.html

Certains des modules importants sont :

- `math` pour les utilitaires mathématiques
- `re` pour les expressions régulières
- `json` pour travailler avec JSON
- `datetime` pour travailler avec les dates
- `sqlite3` pour utiliser SQLite
- `os` pour les utilitaires du système d'exploitation
- `random` pour la génération de nombres aléatoires
- `statistics` pour les utilitaires statistiques
- `requests` pour effectuer des requêtes réseau HTTP
- `http` pour créer des serveurs HTTP
- `urllib` pour gérer les URLs

Introduisons comment _utiliser_ un module de la bibliothèque standard. Vous savez déjà comment utiliser les modules que vous créez, en important depuis d'autres fichiers dans le dossier du programme.

Eh bien, c'est la même chose avec les modules fournis par la bibliothèque standard :

```python
import math

math.sqrt(4) # 2.0
```

ou

```python
from math import sqrt

sqrt(4) # 2.0
```

Nous explorerons bientôt les modules les plus importants individuellement pour comprendre ce que nous pouvons faire avec eux.


## Le guide de style PEP8 pour Python

Lorsque vous écrivez du code, vous devez vous conformer aux conventions du langage de programmation que vous utilisez.

Si vous apprenez les bonnes conventions de nommage et de formatage dès le départ, il sera plus facile de lire le code écrit par d'autres personnes, et les gens trouveront votre code plus facile à lire.

Python définit ses conventions dans le guide de style PEP8. PEP signifie _Python Enhancement Proposals_ et c'est l'endroit où toutes les améliorations et discussions sur le langage Python ont lieu. 

Il existe de nombreuses propositions PEP, toutes disponibles sur https://www.python.org/dev/peps/.

PEP8 est l'une des premières et l'une des plus importantes. Elle définit le formatage ainsi que certaines règles sur la manière d'écrire Python de manière "pythonique".

Vous pouvez lire son contenu complet ici : https://www.python.org/dev/peps/pep-0008/ mais voici un résumé rapide des points importants que vous pouvez commencer à utiliser :

- Indenter en utilisant des espaces, pas des tabulations
- Indenter en utilisant 4 espaces.
- Les fichiers Python sont encodés en UTF-8
- Utiliser un maximum de 80 colonnes pour votre code
- Écrire chaque instruction sur sa propre ligne
- Les fonctions, les noms de variables et les noms de fichiers sont en minuscules, avec des traits de soulignement entre les mots (snake_case)
- Les noms de classes sont capitalisés, les mots séparés sont également écrits avec une lettre majuscule, (CamelCase)
- Les noms de packages sont en minuscules et n'ont pas de traits de soulignement entre les mots
- Les variables qui ne devraient pas changer (constantes) sont écrites en majuscules
- Les noms de variables doivent être significatifs
- Ajouter des commentaires utiles, mais éviter les commentaires évidents
- Ajouter des espaces autour des opérateurs
- Ne pas utiliser d'espaces blancs inutiles
- Ajouter une ligne vide avant une fonction
- Ajouter une ligne vide entre les méthodes dans une classe
- À l'intérieur des fonctions/méthodes, des lignes vides peuvent être utilisées pour séparer des blocs de code liés afin d'aider à la lisibilité


## Débogage en Python

Le débogage est l'une des meilleures compétences que vous pouvez apprendre, car il vous aidera dans de nombreuses situations difficiles.

Chaque langage a son débogueur. Python a `pdb`, disponible via la bibliothèque standard.

Vous déboguez en ajoutant un point d'arrêt dans votre code :

```python
breakpoint()
```

> Vous pouvez ajouter plus de points d'arrêt si nécessaire.

Lorsque l'interpréteur Python rencontre un point d'arrêt dans votre code, il s'arrêtera et vous indiquera quelle est la prochaine instruction qu'il exécutera.

Ensuite, vous pouvez faire quelques choses.

Vous pouvez taper le nom de n'importe quelle variable pour inspecter sa valeur.

Vous pouvez appuyer sur `n` pour passer à la ligne suivante dans la fonction actuelle. Si le code appelle des fonctions, le débogueur n'y entre pas et les considère comme des "boîtes noires".

Vous pouvez appuyer sur `s` pour passer à la ligne suivante dans la fonction actuelle. Si la ligne suivante est une fonction, le débogueur y entre, et vous pouvez alors exécuter une instruction de cette fonction à la fois.

Vous pouvez appuyer sur `c` pour continuer l'exécution du programme normalement, sans avoir besoin de le faire étape par étape.

Vous pouvez appuyer sur `q` pour arrêter l'exécution du programme.

Le débogage est utile pour évaluer le résultat d'une instruction, et il est particulièrement bon de savoir comment l'utiliser lorsque vous avez des itérations ou des algorithmes complexes que vous souhaitez corriger.


## Portée des variables en Python

Lorsque vous déclarez une variable, cette variable est visible dans certaines parties de votre programme, selon l'endroit où vous la déclarez.

Si vous la déclarez en dehors de toute fonction, la variable est visible pour tout code s'exécutant après la déclaration, y compris les fonctions :

```python
age = 8

def test():
    print(age)

print(age) # 8
test() # 8
```

Nous l'appelons une **variable globale**.

Si vous définissez une variable à l'intérieur d'une fonction, cette variable est une **variable locale**, et elle n'est visible qu'à l'intérieur de cette fonction. En dehors de la fonction, elle n'est pas accessible :

```python
def test():
    age = 8
    print(age)

test() # 8

print(age)
# NameError: name 'age' is not defined
```


## Comment accepter des arguments de la ligne de commande en Python

Python offre plusieurs façons de gérer les arguments passés lorsque nous invoquons le programme depuis la ligne de commande.

Jusqu'à présent, vous avez exécuté des programmes soit depuis un REPL, soit en utilisant

```sh
python <filename>.py
```

Vous pouvez passer des arguments et des options supplémentaires lorsque vous le faites, comme ceci :

```sh
python <filename>.py <argument1>
python <filename>.py <argument1> <argument2>
```

Une façon basique de gérer ces arguments est d'utiliser le module `sys` de la bibliothèque standard.

Vous pouvez obtenir les arguments passés dans la liste `sys.argv` :

```python
import sys
print(len(sys.argv))
print(sys.argv)
```

La liste `sys.argv` contient en premier élément le nom du fichier qui a été exécuté, par exemple `['main.py']`.

C'est une méthode simple, mais vous devez faire beaucoup de travail. Vous devez valider les arguments, vous assurer que leur type est correct, et vous devez afficher un retour à l'utilisateur s'ils n'utilisent pas correctement le programme.

Python fournit un autre package dans la bibliothèque standard pour vous aider : `argparse`.

Tout d'abord, vous importez `argparse` et vous appelez `argparse.ArgumentParser()`, en passant la description de votre programme :

```python
import argparse

parser = argparse.ArgumentParser(
    description='Ce programme imprime le nom de mes chiens'
)
```

Ensuite, vous procédez à l'ajout des arguments que vous souhaitez accepter.
Par exemple, dans ce programme, nous acceptons une option `-c` pour passer une couleur, comme ceci : `python program.py -c red`

```python
import argparse

parser = argparse.ArgumentParser(
    description='Ce programme imprime une valeur HEX de couleur'
)

parser.add_argument('-c', '--color', metavar='color', required=True, help='la couleur à rechercher')

args = parser.parse_args()

print(args.color) # 'red'
```

Si l'argument n'est pas spécifié, le programme génère une erreur :

```
[31m python python program.py
usage: program.py [-h] -c color
program.py: error: the following arguments are required: -c
```

Vous pouvez définir une option pour avoir un ensemble spécifique de valeurs, en utilisant `choices` :

```python
parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red','yellow'}, help='la couleur à rechercher')
```

```
[31m python python program.py -c blue
usage: program.py [-h] -c color
program.py: error: argument -c/--color: invalid choice: 'blue' (choose from 'yellow', 'red')
```

Il existe d'autres options, mais ce sont les bases.

Et il existe des packages communautaires qui fournissent cette fonctionnalité, comme [Click](https://click.palletsprojects.com/en/7.x/) et [Python Prompt Toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/index.html).


## Fonctions Lambda en Python

Les fonctions lambda (également appelées fonctions anonymes) sont de minuscules fonctions qui n'ont pas de nom et n'ont qu'une seule expression comme corps.

En Python, elles sont définies en utilisant le mot-clé `lambda` :

```python
lambda <arguments> : <expression>
```

Le corps doit être une seule expression - une expression, pas une instruction.

> Cette différence est importante. Une expression retourne une valeur, une instruction ne le fait pas.

L'exemple le plus simple d'une fonction lambda est une fonction qui double la valeur d'un nombre :

```python
lambda num : num * 2
```

Les fonctions lambda peuvent accepter plus d'arguments :

```python
lambda a, b : a * b
```

Les fonctions lambda ne peuvent pas être appelées directement, mais vous pouvez les attribuer à des variables :

```python
multiply = lambda a, b : a * b

print(multiply(2, 2)) # 4
```

L'utilité des fonctions lambda vient lorsqu'elles sont combinées avec d'autres fonctionnalités Python, par exemple en combinaison avec `map()`, `filter()` et `reduce()`.


## Récursivité en Python

Une fonction en Python peut s'appeler elle-même. C'est ce qu'est la récursivité. Et cela peut être très utile dans de nombreux scénarios.

La manière courante d'expliquer la récursivité est d'utiliser le calcul factoriel.

La factorielle d'un nombre est le nombre `n` multiplié par `n-1`, multiplié par `n-2`... et ainsi de suite, jusqu'à atteindre le nombre `1` :

```
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2 * 1 = 120
```

En utilisant la récursivité, nous pouvons écrire une fonction qui calcule la factorielle de n'importe quel nombre :

```python
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3)) #   6
print(factorial(4)) #  24
print(factorial(5)) # 120
```

Si à l'intérieur de la fonction `factorial()` vous appelez `factorial(n)` au lieu de `factorial(n-1)`, vous allez provoquer une récursivité infinie. Python, par défaut, arrêtera les récursions à 1000 appels, et lorsque cette limite est atteinte, vous obtiendrez une erreur `RecursionError`.

La récursivité est utile dans de nombreux cas, et elle nous aide à simplifier notre code lorsqu'il n'y a pas d'autre moyen optimal de le faire, il est donc bon de connaître cette technique.


## Fonctions imbriquées en Python

Les fonctions en Python peuvent être imbriquées à l'intérieur d'autres fonctions.

Une fonction définie à l'intérieur d'une fonction n'est visible qu'à l'intérieur de cette fonction.

Cela est utile pour créer des utilitaires qui sont utiles à une fonction, mais pas utiles en dehors de celle-ci.

Vous pourriez demander : pourquoi devrais-je "cacher" cette fonction, si elle ne fait pas de mal ?

Premièrement, parce qu'il est toujours préférable de cacher la fonctionnalité qui est locale à une fonction, et qui n'est pas utile ailleurs.

De plus, parce que nous pouvons utiliser des fermetures (plus d'informations à ce sujet plus tard).

Voici un exemple :

```python
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')
```

Si vous souhaitez accéder à une variable définie dans la fonction externe depuis la fonction interne, vous devez d'abord la déclarer comme `nonlocal` :

```python
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()
```

Cela est particulièrement utile avec les fermetures, comme nous le verrons ensuite.


## Fermetures en Python

Si vous retournez une fonction imbriquée depuis une fonction, cette fonction imbriquée a accès aux variables définies dans cette fonction, même si cette fonction n'est plus active.

Voici un exemple simple de compteur.

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter()

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3
```

Nous retournons la fonction interne `increment()`, et celle-ci a toujours accès à l'état de la variable `count` même si la fonction `counter()` s'est terminée.


## Décorateurs en Python

Les décorateurs sont un moyen de modifier, d'améliorer ou d'altérer de quelque manière que ce soit le fonctionnement d'une fonction.

Les décorateurs sont définis avec le symbole `@` suivi du nom du décorateur, juste avant la définition de la fonction.

Exemple :

```python
@logtime
def hello():
    print('hello!')
```

Cette fonction `hello` a le décorateur `logtime` assigné.

Chaque fois que nous appelons `hello()`, le décorateur va être appelé.

Un décorateur est une fonction qui prend une fonction comme paramètre, enveloppe la fonction dans une fonction interne qui effectue le travail qu'elle doit faire, et retourne cette fonction interne. En d'autres termes :

```python
def logtime(func):
    def wrapper():
        # faire quelque chose avant
        val = func()
        # faire quelque chose après
        return val
    return wrapper
```


## Docstrings en Python

La documentation est extrêmement importante, non seulement pour communiquer à d'autres personnes quel est l'objectif d'une fonction/classe/méthode/module, mais elle communique également cela à vous-même.

Lorsque vous revenez à votre code 6 ou 12 mois plus tard, vous ne vous souviendrez peut-être pas de toutes les connaissances que vous avez en tête. À ce moment-là, lire votre code et comprendre ce qu'il est censé faire sera beaucoup plus difficile.

Les commentaires sont un moyen de vous aider (et d'aider les autres) :

```python
# this is a comment

num = 1 #this is another comment
```

Un autre moyen est d'utiliser les **docstrings**.

L'utilité des docstrings est qu'elles suivent des conventions. En tant que telles, elles peuvent être traitées automatiquement.

Voici comment vous définissez une docstring pour une fonction :

```python
def increment(n):
    """Incrémente un nombre"""
    return n + 1
```

Voici comment vous définissez une docstring pour une classe et une méthode :

```python
class Dog:
    """Une classe représentant un chien"""
    def __init__(self, name, age):
        """Initialise un nouveau chien"""
        self.name = name
        self.age = age

    def bark(self):
        """Fait aboyer le chien"""
        print('WOF!')
```

Documentez un module en plaçant une docstring en haut du fichier, par exemple en supposant que ceci est `dog.py` :

```python
"""Module Dog

Ce module fait ... bla bla bla et fournit les classes suivantes :

- Dog
...
"""

class Dog:
    """Une classe représentant un chien"""
    def __init__(self, name, age):
        """Initialise un nouveau chien"""
        self.name = name
        self.age = age

    def bark(self):
        """Fait aboyer le chien"""
        print('WOF!')
```

Les docstrings peuvent s'étendre sur plusieurs lignes :

```python
def increment(n):
    """Incrémente
    un nombre
    """
    return n + 1
```

Python traitera celles-ci et vous pouvez utiliser la fonction globale `help()` pour obtenir la documentation d'une classe/méthode/fonction/module.

Par exemple, appeler `help(increment)` vous donnera ceci :

```
Help on function increment in module
__main__:

increment(n)
    Incrémente
    un nombre
```

Il existe de nombreuses normes différentes pour formater les docstrings, et vous pouvez choisir d'adhérer à votre préférée.

J'aime la norme de Google : https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

Les normes permettent d'avoir des outils pour extraire les docstrings et générer automatiquement de la documentation pour votre code.


## Introspection en Python

Les fonctions, variables et objets peuvent être analysés en utilisant l'**introspection**.

Tout d'abord, en utilisant la fonction globale `help()`, nous pouvons obtenir la documentation si elle est fournie sous forme de docstrings.

Ensuite, vous pouvez utiliser print() pour obtenir des informations sur une fonction :

```python
def increment(n):
    return n + 1

print(increment)

# <function increment at 0x7f420e2973a0>
```

ou un objet :

```python
class Dog():
    def bark(self):
        print('WOF!')

roger = Dog()

print(roger)

# <__main__.Dog object at 0x7f42099d3340>
```

La fonction `type()` nous donne le type d'un objet :

```python
print(type(increment))
# <class 'function'>

print(type(roger))
# <class '__main__.Dog'>

print(type(1))
# <class 'int'>

print(type('test'))
# <class 'str'>
```

La fonction globale `dir()` nous permet de découvrir toutes les méthodes et attributs d'un objet :

```python
print(dir(roger))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bark']
```

La fonction globale `id()` nous montre l'emplacement en mémoire de n'importe quel objet :

```python
print(id(roger)) # 140227518093024
print(id(1))     # 140227521172384
```

Cela peut être utile pour vérifier si deux variables pointent vers le même objet.

Le module `inspect` de la bibliothèque standard nous donne plus d'outils pour obtenir des informations sur les objets, et vous pouvez le consulter ici : https://docs.python.org/3/library/inspect.html


## Annotations en Python

Python est typé dynamiquement. Nous n'avons pas à spécifier le type d'une variable ou d'un paramètre de fonction, ou la valeur de retour d'une fonction.

Les annotations nous permettent de le faire (optionnellement).

Voici une fonction sans annotations :

```python
def increment(n):
    return n + 1
```

Voici la même fonction avec des annotations :

```python
def increment(n: int) -> int:
    return n + 1
```

Vous pouvez également annoter des variables :

```python
count: int = 0
```

Python ignorera ces annotations. Un outil séparé appelé [`mypy`](http://mypy-lang.org/) peut être exécuté de manière autonome, ou intégré par des IDE comme VS Code ou PyCharm pour vérifier automatiquement les erreurs de type de manière statique, pendant que vous codez. Il vous aidera également à attraper les bugs de non-correspondance de type avant même d'exécuter le code.

Une grande aide surtout lorsque votre logiciel devient volumineux et que vous devez refactoriser votre code.


## Exceptions en Python

Il est important d'avoir un moyen de gérer les erreurs, et Python nous donne la gestion des exceptions pour le faire.

Si vous enveloppez des lignes de code dans un bloc `try:` :

```python
try:
    # quelques lignes de code
```

Si une erreur se produit, Python vous alertera et vous pourrez déterminer quel type d'erreur s'est produit en utilisant des blocs `except` :

```python
try:
    # quelques lignes de code
except <ERROR1>:
    # gestionnaire <ERROR1>
except <ERROR2>:
    # gestionnaire <ERROR2>
```

Pour attraper toutes les exceptions, vous pouvez utiliser `except` sans aucun type d'erreur :

```python
try:
    # quelques lignes de code
except <ERROR1>:
    # gestionnaire <ERROR1>
except:
    # attraper toutes les autres exceptions
```

Le bloc `else` est exécuté si aucune exception n'a été trouvée :

```python
try:
    # quelques lignes de code
except <ERROR1>:
    # gestionnaire <ERROR1>
except <ERROR2>:
    # gestionnaire <ERROR2>
else:
    # aucune exception n'a été levée, le code s'est exécuté avec succès
```

Un bloc `finally` vous permet d'effectuer une opération dans tous les cas, indépendamment du fait qu'une erreur se soit produite ou non :

```python
try:
    # quelques lignes de code
except <ERROR1>:
    # gestionnaire <ERROR1>
except <ERROR2>:
    # gestionnaire <ERROR2>
else:
    # aucune exception n'a été levée, le code s'est exécuté avec succès
finally:
    # faire quelque chose dans tous les cas
```

L'erreur spécifique qui va se produire dépend de l'opération que vous effectuez.

Par exemple, si vous lisez un fichier, vous pourriez obtenir une `EOFError`. Si vous divisez un nombre par zéro, vous obtiendrez une `ZeroDivisionError`. Si vous avez un problème de conversion de type, vous pourriez obtenir une `TypeError`.

Essayez ce code :

```python
result = 2 / 0
print(result)
```

Le programme se terminera avec une erreur :

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    result = 2 / 0
ZeroDivisionError: division by zero
```

et les lignes de code après l'erreur ne seront pas exécutées.

Ajouter cette opération dans un bloc `try:` nous permet de récupérer élégamment et de continuer avec le programme :

```python
try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1

print(result) # 1
```

Vous pouvez également lever des exceptions dans votre propre code, en utilisant l'instruction `raise` :

```python
raise Exception('An error occurred!')
```

Cela lève une exception générale, et vous pouvez l'intercepter en utilisant :

```python
try:
    raise Exception('An error occurred!')
except Exception as error:
    print(error)
```

Vous pouvez également définir votre propre classe d'exception, en étendant depuis Exception :

```python
class DogNotFoundException(Exception):
    pass
```

> `pass` ici signifie "rien" et nous devons l'utiliser lorsque nous définissons une classe sans méthodes, ou une fonction sans code, également.

```python
try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')
```


## L'instruction `with` en Python

L'instruction `with` est très utile pour simplifier le travail avec la gestion des exceptions.

Par exemple, lorsque vous travaillez avec des fichiers, chaque fois que vous ouvrez un fichier, vous devez vous souvenir de le fermer.

`with` rend ce processus transparent.

Au lieu d'écrire :

```python
filename = '/Users/flavio/test.txt'

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()
```

Vous pouvez écrire :

```python
filename = '/Users/flavio/test.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
```

En d'autres termes, nous avons une gestion des exceptions implicite intégrée, car `close()` sera appelé automatiquement pour nous.

`with` n'est pas seulement utile pour travailler avec des fichiers. L'exemple ci-dessus est juste destiné à introduire ses capacités.


## Comment installer des packages tiers en Python en utilisant `pip`

La bibliothèque standard de Python contient un grand nombre d'utilitaires qui simplifient nos besoins de développement Python, mais rien ne peut satisfaire _tout_.

C'est pourquoi des individus et des entreprises créent des packages, et les rendent disponibles en tant que logiciels open source pour toute la communauté.

Ces modules sont tous collectés en un seul endroit, le **Python Package Index** disponible à l'adresse https://pypi.org, et ils peuvent être installés sur votre système en utilisant `pip`.

Il y a plus de 270 000 packages librement disponibles au moment de l'écriture.

> Vous devriez avoir `pip` déjà installé si vous avez suivi les instructions d'installation de Python.

Installez n'importe quel package en utilisant la commande `pip install` :

```
pip install <package>
```

ou, si vous avez des problèmes, vous pouvez également l'exécuter via `python -m` :

```
python -m pip install <package>
```

Par exemple, vous pouvez installer le package [`requests`](https://pypi.org/project/requests/), une bibliothèque HTTP populaire :

```
pip install requests
```

et une fois que vous l'avez fait, il sera disponible pour tous vos scripts Python, car les packages sont installés globalement.

L'emplacement exact dépend de votre système d'exploitation.

Sur macOS, en exécutant Python 3.9, l'emplacement est `/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages`.

Mettez à jour un package vers sa dernière version en utilisant :

```
pip install –U <package>
```

Installez une version spécifique d'un package en utilisant :

```
pip install <package>==<version>
```

Désinstallez un package en utilisant :

```
pip uninstall <package>
```

Affichez les détails d'un package installé, y compris la version, le site web de la documentation et les informations sur l'auteur en utilisant :

```
pip show <package>
```


## Compréhensions de liste en Python

Les compréhensions de liste sont un moyen de créer des listes de manière très concise.

Supposons que vous avez une liste :

```python
numbers = [1, 2, 3, 4, 5]
```

Vous pouvez créer une nouvelle liste en utilisant une compréhension de liste, composée des éléments de la liste `numbers`, élevés au carré :

```python
numbers_power_2 = [n**2 for n in numbers]
# [1, 4, 9, 16, 25]
```

Les compréhensions de liste sont une syntaxe qui est parfois préférée aux boucles, car elle est plus lisible lorsque l'opération peut être écrite sur une seule ligne :

```python
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
```

et sur `map()` :

```python
numbers_power_2 = list(map(lambda n : n**2, numbers))
```


## Polymorphisme en Python

Le polymorphisme généralise une fonctionnalité afin qu'elle puisse fonctionner sur différents types. C'est un concept important en programmation orientée objet.

Nous pouvons définir la même méthode sur différentes classes :

```python
class Dog:
    def eat():
        print('Eating dog food')

class Cat:
    def eat():
        print('Eating cat food')
```

Ensuite, nous pouvons générer des objets et nous pouvons appeler la méthode `eat()` indépendamment de la classe à laquelle appartient l'objet, et nous obtiendrons des résultats différents :

```python
animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()
```

Nous avons construit une interface généralisée et nous n'avons plus besoin de savoir qu'un animal est un Chat ou un Chien.


## Surcharge d'opérateurs en Python

La surcharge d'opérateurs est une technique avancée que nous pouvons utiliser pour rendre les classes comparables et pour les faire fonctionner avec les opérateurs Python.

Prenons une classe Dog :

```python
class Dog:
    # la classe Dog
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Créons 2 objets Dog :

```python
roger = Dog('Roger', 8)
syd = Dog('Syd', 7)
```

Nous pouvons utiliser la surcharge d'opérateurs pour ajouter une façon de comparer ces 2 objets, basée sur la propriété `age` :

```python
class Dog:
    # la classe Dog
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
```

Maintenant, si vous essayez d'exécuter `print(roger > syd)`, vous obtiendrez le résultat `True`.

De la même manière que nous avons défini `__gt__()` (qui signifie supérieur à), nous pouvons définir les méthodes suivantes :

- `__eq__()` pour vérifier l'égalité
- `__lt__()` pour vérifier si un objet doit être considéré comme inférieur à un autre avec l'opérateur `<`
- `__le__()` pour inférieur ou égal (`<=`)
- `__ge__()` pour supérieur ou égal (`>=`)
- `__ne__()` pour différent (`!=`)

Ensuite, vous avez des méthodes pour interagir avec les opérations arithmétiques :

- `__add__()` répond à l'opérateur `+`
- `__sub__()` répond à l'opérateur `-`
- `__mul__()` répond à l'opérateur `*`
- `__truediv__()` répond à l'opérateur `/`
- `__floordiv__()` répond à l'opérateur `//`
- `__mod__()` répond à l'opérateur `%`
- `__pow__()` répond à l'opérateur `**`
- `__rshift__()` répond à l'opérateur `>>`
- `__lshift__()` répond à l'opérateur `<<`
- `__and__()` répond à l'opérateur `&`
- `__or__()` répond à l'opérateur `|`
- `__xor__()` répond à l'opérateur `^`

Il existe quelques autres méthodes pour travailler avec d'autres opérateurs, mais vous avez compris l'idée.


## Environnements virtuels en Python

Il est courant d'avoir plusieurs applications Python en cours d'exécution sur votre système.

Lorsque les applications nécessitent le même module, à un moment donné, vous atteindrez une situation délicate où une application a besoin d'une version d'un module, et une autre application a besoin d'une version différente de ce même module.

Pour résoudre ce problème, vous utilisez des **environnements virtuels**.

Nous utiliserons `venv`. D'autres outils fonctionnent de manière similaire, comme `pipenv`.

Créez un environnement virtuel en utilisant

```sh
python -m venv .venv
```

dans le dossier où vous souhaitez démarrer le projet, ou où vous avez déjà un projet existant.

Ensuite, exécutez

```sh
source .venv/bin/activate
```

> Utilisez `source .venv/bin/activate.fish` sur le shell Fish

L'exécution du programme activera l'environnement virtuel Python. Selon votre configuration, vous pourriez également voir votre prompt de terminal changer.

Le mien est passé de

`[31m folder `

à

`(.venv) [31m folder `

Maintenant, l'exécution de `pip` utilisera cet environnement virtuel au lieu de l'environnement global.


## Conclusion

Merci beaucoup d'avoir lu ce livre.

J'espère qu'il vous inspirera à en apprendre davantage sur Python.

Pour plus d'informations sur Python et les tutoriels de programmation en général, consultez mon blog [flaviocopes.com](https://flaviocopes.com).

Envoyez vos commentaires, errata ou opinions à <mailto:flavio@flaviocopes.com>, et vous pouvez me joindre sur Twitter [@flaviocopes](https://twitter.com/flaviocopes).

> Note : Vous pouvez [obtenir une version PDF, ePub et Mobi de ce manuel Python](https://flaviocopes.com/page/python-handbook/)