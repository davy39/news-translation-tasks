---
title: Exécuter un Script Python – Comment Exécuter des Commandes Shell Python dans
  le Terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-14T15:24:17.000Z'
originalURL: https://freecodecamp.org/news/run-python-script-how-to-execute-python-shell-commands-in-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-jan-kopr-iva-3280908.jpg
tags:
- name: Python
  slug: python
- name: shell script
  slug: shell-script
- name: terminal
  slug: terminal
seo_title: Exécuter un Script Python – Comment Exécuter des Commandes Shell Python
  dans le Terminal
seo_desc: "By Suchandra Datta\nWhen you're starting out learning a new programming\
  \ language, your very first program is likely to be one that prints \"hello world!\"\
  . \nLet's say you want to do this in Python. There are two ways of doing it: using\
  \ the Python shell ..."
---

Par Suchandra Datta

Lorsque vous commencez à apprendre un nouveau langage de programmation, votre tout premier programme est probablement celui qui imprime "hello world!". 

Disons que vous voulez faire cela en Python. Il y a deux façons de le faire : en utilisant le shell Python ou en l'écrivant sous forme de script et en l'exécutant dans le terminal. 

## Qu'est-ce qu'un Shell ?

Un système d'exploitation est composé d'un ensemble de programmes. Ils effectuent des tâches comme la gestion de fichiers, la gestion de la mémoire et la gestion des ressources, et ils aident vos applications à fonctionner sans problème. 

Tout le travail que nous faisons sur les ordinateurs, comme l'analyse de données dans Excel ou les jeux, est facilité par le système d'exploitation. 

Les programmes du système d'exploitation sont de deux types, appelés programmes **shell** et **kernel**. 

Les programmes kernel sont ceux qui effectuent les tâches réelles, comme la création d'un fichier ou l'envoi d'interruptions. Le shell est un autre programme, dont le travail est de prendre des entrées, de décider et d'exécuter le programme kernel requis pour faire le travail et d'afficher la sortie. 

Le shell est également appelé le **processeur de commandes**. 

## Qu'est-ce qu'un Terminal ?

Le terminal est le programme qui interagit avec le shell et nous permet de communiquer avec lui via des commandes basées sur du texte. C'est pourquoi il est également appelé la ligne de commande. 

Pour accéder au terminal sur Windows, appuyez sur le logo Windows + R, tapez cmd, puis appuyez sur Entrée. 

Pour accéder au terminal sur Ubuntu, appuyez sur Ctrl + Alt + T. 

## Qu'est-ce que le Shell Python ?

Python est un langage interprété. Cela signifie que l'interpréteur Python lit une ligne de code, exécute cette ligne, puis répète ce processus s'il n'y a pas d'erreurs. 

Le shell Python vous donne une interface de ligne de commande que vous pouvez utiliser pour spécifier des commandes directement à l'interpréteur Python de manière interactive. 

Vous pouvez obtenir beaucoup d'informations détaillées concernant le shell Python dans la [documentation officielle](https://docs.python.org/3/tutorial/interpreter.html#). 

## Comment Utiliser le Shell Python

Pour démarrer le shell Python, tapez simplement `python` et appuyez sur Entrée dans le terminal :

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>print("hello world!")



```

Le shell interactif est également appelé REPL, ce qui signifie read, evaluate, print, loop. Il lira chaque commande, l'évaluera et l'exécutera, imprimera la sortie pour cette commande le cas échéant, et continuera ce même processus de manière répétée jusqu'à ce que vous quittiez le shell. 

Il existe différentes façons de quitter le shell :

* vous pouvez appuyer sur Ctrl+Z sur Windows ou Ctrl+D sur les systèmes Unix pour quitter
* utiliser la commande exit()
* utiliser la commande quit()

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("HELLO WORLD")
HELLO WORLD
>>> quit()

C:\Users\Suchandra Datta>
```

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

C:\Users\Suchandra Datta>
```

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ^Z


C:\Users\Suchandra Datta>
```

## Que Pouvez-Vous Faire dans le Shell Python ?

Vous pouvez faire presque tout ce que le langage Python permet, de l'utilisation de variables, de boucles et de conditions à la définition de fonctions et plus encore. 

Le `>>>` est l'invite du shell où vous tapez vos commandes. Si vous avez des commandes qui s'étendent sur plusieurs lignes – par exemple lorsque vous définissez des boucles – le shell imprime les caractères `...` qui signifient qu'une ligne continue. 

Voyons un exemple :

```
>>>
>>> watch_list = ["stranger_things_s1", "stranger_things_s2", "stranger_things_s3","stranger_things_s4"]
>>>
>>>
```

Ici, nous avons défini une liste avec quelques noms d'émissions de télévision via le shell Python. 

Ensuite, définissons une fonction qui accepte une liste d'émissions et retourne aléatoirement une émission :

```
>>> def weekend_party(show_list):
...     r = random.randint(0, len(show_list)-1)
...     return show_list[r]
...
```

Notez les lignes de continuation (`...`) du shell Python ici. 

Enfin, pour invoquer la fonction depuis le shell, vous appelez simplement la fonction de la manière dont vous le feriez dans un script :

```
>>> weekend_party(watch_list)
'stranger_things_s1'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s3'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s2'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s2'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s3'
>>>

```

Vous pouvez inspecter les modules Python depuis le shell, comme montré ci-dessous :

```
>>>
>>>
>>> import numpy
>>> numpy.__version__
'1.20.1'
>>>
```

Vous pouvez voir quelles méthodes et attributs un module offre en utilisant la méthode `dir()` :

```
>>>
>>> x = dir(numpy)
>>> len(x)
606
>>> x[0:3]
['ALLOW_THREADS', 'AxisError', 'BUFSIZE']
```

Ici, vous pouvez voir que Numpy a 606 méthodes et propriétés au total. 

## Comment Exécuter des Scripts Python

Le shell Python est utile pour exécuter des programmes simples ou pour déboguer des parties de programmes complexes. 

Mais les très grands programmes Python avec beaucoup de complexité sont écrits dans des fichiers avec une extension .py, typiquement appelés scripts Python. Ensuite, vous les exécutez depuis le terminal en utilisant la commande `Python`. 

La syntaxe habituelle est :

```
python filename.py
```

Toutes les commandes que nous avons exécutées précédemment via le shell, nous pouvons également les écrire dans un script et les exécuter de cette manière. 

## Conclusion

Dans cet article, nous avons appris ce qu'est un shell, un terminal, comment utiliser le shell Python. Nous avons également vu comment exécuter des scripts Python depuis la ligne de commande. 

J'espère que cet article vous aide à comprendre ce qu'est le shell Python et comment vous pouvez l'utiliser dans votre vie quotidienne. Bon apprentissage !