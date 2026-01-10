---
title: Instruction While Loop de Python expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-21T20:10:00.000Z'
originalURL: https://freecodecamp.org/news/python-while-loop-statement-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c77740569d1a4ca3259.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Instruction While Loop de Python expliquée
seo_desc: 'While Loop Statements

  Python utilizes the while loop similarly to other popular languages. The while loop
  evaluates a condition then executes a block of code if the condition is true. The
  block of code executes repeatedly until the condition becomes ...'
---

## **Instructions While Loop**

Python utilise la boucle `while` de manière similaire à d'autres langages populaires. La boucle `while` évalue une condition puis exécute un bloc de code si la condition est vraie. Le bloc de code s'exécute de manière répétée jusqu'à ce que la condition devienne fausse.

La syntaxe de base est :

```python
compteur = 0
while compteur < 10:
   # Exécute le bloc de code ici tant que
   # compteur est inférieur à 10
```

Un exemple est montré ci-dessous :

```python
jours = 0    
semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
while jours < 7:
   print("Aujourd'hui nous sommes " + semaine[jours])
   jours += 1
```

Sortie :

```text
Aujourd'hui nous sommes Lundi
Aujourd'hui nous sommes Mardi
Aujourd'hui nous sommes Mercredi
Aujourd'hui nous sommes Jeudi
Aujourd'hui nous sommes Vendredi
Aujourd'hui nous sommes Samedi
Aujourd'hui nous sommes Dimanche
```

Explication ligne par ligne du CODE ci-dessus :

1. la variable 'jours' est définie à une valeur de 0.
2. une variable semaine est assignée à une liste contenant tous les jours de la semaine.
3. la boucle while commence
4. le bloc de code sera exécuté jusqu'à ce que la condition retourne 'vrai'.
5. la condition est 'jours<7' ce qui signifie grossièrement exécuter la boucle while jusqu'à ce que la variable jours soit inférieure à 7
6. Donc lorsque jours=7, la boucle while cesse de s'exécuter.
7. la variable jours est mise à jour à chaque itération.
8. Lorsque la boucle while s'exécute pour la première fois, la ligne 'Aujourd'hui nous sommes Lundi' est imprimée sur la console et la variable jours devient égale à 1.
9. Puisque la variable jours est égale à 1, ce qui est inférieur à 7, la boucle while est exécutée à nouveau.
10. Cela continue encore et encore et lorsque la console imprime 'Aujourd'hui nous sommes Dimanche', la variable jours est maintenant égale à 7 et la boucle while cesse de s'exécuter.

#### **Plus d'informations :**

* [Documentation de l'instruction `while` de Python](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)