---
title: Python If-Else – Exemple de Syntaxe Conditionnelle en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-15T17:43:26.000Z'
originalURL: https://freecodecamp.org/news/python-if-else-python-conditional-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/py.png
tags:
- name: Python
  slug: python
seo_title: Python If-Else – Exemple de Syntaxe Conditionnelle en Python
seo_desc: "In your applications and web projects, there might be times when a user\
  \ needs to perform an action if a certain condition is met. \nThere might also be\
  \ cases when you need to make the user perform another action if the condition is\
  \ not met.\nTo do this..."
---

Dans vos applications et projets web, il peut arriver qu'un utilisateur doive effectuer une action si une certaine condition est remplie. 

Il peut également y avoir des cas où vous devez faire effectuer une autre action à l'utilisateur si la condition n'est pas remplie.

Pour cela en Python, vous utilisez les mots-clés `if` et `else`. Ces deux mots-clés sont appelés conditionnels.

Dans cet article, je vais vous montrer comment implémenter la prise de décision dans vos applications avec les mots-clés `if` et `else`. Je vais également vous montrer comment fonctionne le mot-clé `elif`. 

J'utiliserai des opérateurs de comparaison Python tels que `>` (supérieur à), `<` (inférieur à) et (`==`) égal pour comparer des variables dans les blocs `if` et `elif`, afin que nous puissions prendre les décisions.


## Comment Utiliser le Mot-Clé `if` en Python

En Python, la syntaxe pour une instruction `if` unique ressemble à ceci :

```py
if(condition):
    bloc indenté de décision à prendre si la condition est vraie
```

Contrairement à certains autres langages de programmation qui utilisent des accolades pour déterminer un bloc ou une portée, Python utilise un deux-points (`:`) et une indentation (`4 espaces ou une tabulation`).

Ainsi, la ligne ou les lignes de code indentées après le deux-points seront exécutées si la condition spécifiée dans les parenthèses devant le mot-clé `if` est vraie.

Dans l'exemple ci-dessous, j'enregistre les points de 3 équipes de football dans 3 variables et je prends une décision avec une instruction `if`.

```py
teamAPoints = 99
teamBPoints = 89
teamCPoints = 89

if(teamAPoints > teamBPoints):
    print("L'équipe A a gagné la ligue") # Sortie : L'équipe A a gagné la ligue
```

Vous pouvez voir que le code a été exécuté parce que la condition – `teamAPoints > teamBPoints` – était remplie. C'est-à-dire, l'équipe A a gagné la ligue parce qu'elle avait 99 points contre 89 pour les équipes B et C.

Python a le mot-clé `and` qui peut nous aider à inclure l'équipe C dans la comparaison :

```py
teamAPoints = 99
teamBPoints = 89
teamCPoints = 89

if(teamAPoints > teamBPoints and teamCPoints):
    print("L'équipe A a gagné la ligue contre l'équipe B et l'équipe C") # Sortie : L'équipe A a gagné la ligue contre l'équipe B et l'équipe C
```

Le code a été exécuté à nouveau parce que la condition – `teamAPoints > teamBPoints and teamCPoints` – était remplie.

Si vous n'avez qu'un seul bloc de code à exécuter avec l'instruction `if`, vous pouvez le mettre sur une seule ligne et tout ira bien, comme montré ci-dessous :

```py
teamAPoints = 99
teamBPoints = 89
teamCPoints = 89

if(teamAPoints > teamBPoints): print("L'équipe A a gagné la ligue") # Sortie : L'équipe A a gagné la ligue
```

Ce n'est pas une règle, c'est juste une pratique courante.

Si la condition dans l'instruction `if` n'est pas remplie, rien ne se passe. 

Dans la capture d'écran ci-dessous, rien ne se passe parce que la condition spécifiée dans l'instruction if n'est pas vraie. L'équipe A a plus de points (99) que l'équipe B (89).
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/02/ss-1-4.png)
 
Au fait, vous exécutez du code Python dans le terminal en tapant Python ou Python3 suivi du nom du fichier, de l'extension .py, puis en appuyant sur `ENTRÉE` sur votre clavier. Par exemple, `python3 if_else.py`.

## Comment Utiliser le Mot-Clé `else` en Python

Puisque rien ne se passe si la condition dans une instruction `if` n'est pas remplie, vous pouvez capturer cela avec une instruction else.

Avec `else`, vous faites effectuer une action à l'utilisateur si la condition dans l'instruction `if` n'est pas vraie, ou si vous voulez ajouter plus d'options. 

La syntaxe pour `if...else` est une extension de celle de `if` : 

```py
if(condition):
    bloc indenté de décision à prendre si la condition est vraie
else:
    bloc indenté de décision à prendre si la condition n'est pas vraie
```

Dans l'extrait de code ci-dessous, le bloc de code dans la portée `else` s'exécute parce que la condition spécifiée n'est pas vraie – l'équipe C n'a pas plus de points que l'équipe A.

```py
teamAPoints = 99
teamBPoints = 89
teamCPoints = 89

if(teamCPoints > teamAPoints):
    print("L'équipe C a gagné la ligue") 
else:
    print("L'équipe A a gagné la ligue") # Sortie : L'équipe A a gagné la ligue
```

Si vous n'avez qu'un seul bloc de code à exécuter avec le `if` et un avec le `else`, vous pouvez le mettre sur une seule ligne et tout ira bien : 

```py
teamAPoints = 99
teamBPoints = 89
teamCPoints = 89

if(teamCPoints > teamAPoints): print("L'équipe C a gagné la ligue") 
else: print("L'équipe A a gagné la ligue") # Sortie : L'équipe A a gagné la ligue
```

## `if` Imbriqué en Python

Vous pouvez combiner ce que `if...else` fait en une seule instruction `if`. Cela s'appelle l'imbrication dans les langages de programmation.

La syntaxe pour imbriquer 2 ou plusieurs instructions if ressemble à ce que vous voyez dans l'extrait de code ci-dessous : 

```py
if(condition):
    if(condition):
        if(condition)
            bloc indenté de décision à prendre
```

Dans un `if` imbriqué, toutes les conditions doivent être vraies pour que le code s'exécute.

```py
teamAPoints = 99
teamBPoints = 89
teamCPoints = 88

if (teamAPoints > teamBPoints):
    if (teamAPoints >= teamBPoints):
        if (teamAPoints >= teamCPoints):
            print("L'équipe A a gagné la ligue") # L'équipe A a gagné la ligue
```

## Comment Utiliser le Mot-Clé `elif` en Python

Un autre mot-clé conditionnel en Python est `elif`, que vous pouvez placer entre un `if` et un else.

Dans l'extrait de code ci-dessous, vous pouvez voir comment fonctionne le mot-clé `elif` : 

```py
teamAPoints = 99
teamBPoints = 89
teamCPoints = 88

if (teamAPoints == 89):
    print("L'équipe B n'a pas gagné la ligue")
elif(teamAPoints == 99):
    print("L'équipe A a gagné la ligue")
else:
    print("L'équipe C a gagné la ligue") # Résultat : L'équipe A a gagné la ligue
```

La condition dans l'instruction if ne s'est pas exécutée parce que l'équipe A a 99 points

La condition dans le `elif` est vraie et s'est exécutée parce que l'équipe A a 99 points, donc le bloc `else` a été ignoré.

## Conclusion

Dans cet article, vous avez appris à utiliser `if...else` en Python afin de pouvoir implémenter des conditionnels dans vos projets.

Merci d'avoir lu, et bon codage.