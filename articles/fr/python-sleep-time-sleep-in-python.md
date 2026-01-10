---
title: Python Sleep – time.sleep() en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-17T17:22:29.000Z'
originalURL: https://freecodecamp.org/news/python-sleep-time-sleep-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/sleep.png
tags:
- name: Python
  slug: python
seo_title: Python Sleep – time.sleep() en Python
seo_desc: "While running a Python program, there might be times when you'd like to\
  \ delay the execution of the program for some seconds. \nThe Python time module\
  \ has a built-in function called time.sleep() with which you can delay the execution\
  \ of a program.\nWith..."
---

Lors de l'exécution d'un programme Python, il peut arriver que vous souhaitiez retarder l'exécution du programme de quelques secondes. 

Le module `time` de Python possède une fonction intégrée appelée `time.sleep()` avec laquelle vous pouvez retarder l'exécution d'un programme.

Avec la fonction `sleep()`, vous pouvez être plus créatif dans vos projets Python car elle vous permet de créer des délais qui peuvent grandement vous aider à intégrer certaines fonctionnalités.

Dans cet article, vous apprendrez à utiliser la méthode `time.sleep()` pour créer des délais.

Notez simplement que les délais créés avec `time.sleep()` n'arrêtent pas l'exécution de l'ensemble du programme – ils ne retardent que le thread actuel.

## Syntaxe de base de `time.sleep()`

Pour utiliser `time.sleep()` dans votre programme, vous devez d'abord l'importer depuis le module `time`.

Après avoir importé la fonction `sleep()`, spécifiez le nombre de secondes pendant lesquelles vous souhaitez que le délai s'exécute à l'intérieur des parenthèses.

```py
import time
time.sleep(delayInSeconds)
```

## Exemple de base de `time.sleep()`

Dans l'extrait de code ci-dessous, j'ai mis un délai de 5 secondes entre les 2 instructions print, de sorte que la deuxième instruction print s'exécutera 5 secondes après l'exécution de la première :

```py
import time

print("Hello world")

time.sleep(5)

print("Hello campers")
```
![ss1](https://www.freecodecamp.org/news/content/images/2022/03/ss1.gif)

Vous pouvez également spécifier le délai en nombres à virgule flottante :

```py
import time

print("Hello world")

time.sleep(3.5)

print("Hello campers")
```
![ss2](https://www.freecodecamp.org/news/content/images/2022/03/ss2.gif)

## Plus d'exemples de time.sleep()

Vous pouvez être plus créatif avec les délais créés par `time.sleep()` en le combinant avec `ctime()`, une autre fonction intégrée du module `time` qui signifie « current time » (heure actuelle).

```py
import time

print("Execution started at: ", time.ctime())

time.sleep(10)
print("Hello world")

print("Execution ended at at: ", time.ctime())

# Sortie
# L'exécution a commencé à :  Thu Mar 17 10:37:55 2022
# Hello world
# L'exécution s'est terminée à :  Thu Mar 17 10:38:05 2022
```

Vous pouvez également utiliser `time.sleep()` pour créer plusieurs délais tout en parcourant des données itérables telles qu'une liste ou un tuple.

L'exemple ci-dessous montre comment je l'ai fait avec une liste :

```py
import time

# Création de la liste
legendaryFootballers = ["Okocha", "Pele", "Eusebio", "Martha", "Cruyff", "MAradona"]

for legend in legendaryFootballers:

    # Création du délai
    time.sleep(2)

    # Les légendes individuelles de la liste seront affichées après 2 secondes
    print(legend)
```

La sortie :
![ss3](https://www.freecodecamp.org/news/content/images/2022/03/ss3.gif)

## Conclusion 

Cet article vous a expliqué comment utiliser la fonction `time.sleep()` en Python. 

`time.sleep()` est une fonction intégrée passionnante qui peut être utile pour créer des délais dans vos projets Python, qu'il s'agisse de jeux, de projets Web ou de systèmes d'IA.

Bon codage !