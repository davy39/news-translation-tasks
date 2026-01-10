---
title: Exemples de fonctions Python – Comment les déclarer et les invoquer avec des
  paramètres
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-24T19:04:21.000Z'
originalURL: https://freecodecamp.org/news/python-function-examples-how-to-declare-and-invoke-with-parameters-2
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/david-clode-vb-3qEe3rg8-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Exemples de fonctions Python – Comment les déclarer et les invoquer avec
  des paramètres
seo_desc: "Python has a bunch of helpful built-in functions you can use to do all\
  \ sorts of stuff. And each one performs a specific task. \nBut did you know that\
  \ Python also allows you to define your own functions?\nThis article will show you\
  \ how to create and cal..."
---

Python dispose d'un ensemble de fonctions intégrées utiles que vous pouvez utiliser pour effectuer toutes sortes de tâches. Et chacune d'entre elles accomplit une tâche spécifique.

Mais saviez-vous que Python permet également de définir vos propres fonctions ?

Cet article vous montrera comment créer et appeler vos propres fonctions Python. Il vous donnera également un aperçu de la manière de passer des paramètres et des arguments d'entrée à vos fonctions.

## Qu'est-ce qu'une fonction ?

Une fonction est un bloc de code isolé qui effectue une tâche spécifique.

Les fonctions sont utiles en programmation car elles éliminent la copie et le collage inutiles et excessifs de code dans un programme.

Si une certaine action est requise souvent et à différents endroits, c'est un bon indicateur que vous pouvez écrire une fonction pour cela. Les fonctions sont destinées à être réutilisables.

Les fonctions aident également à organiser votre code.

Si vous devez apporter une modification, vous n'aurez besoin de mettre à jour que cette fonction spécifique. Cela vous évite d'avoir à rechercher différents morceaux du même code qui ont été dispersés à différents endroits dans votre programme par copie et collage.

Cela respecte le principe DRY (Don't Repeat Yourself) en développement logiciel.

Le code à l'intérieur d'une fonction ne s'exécute que lorsque la fonction est appelée.

Les fonctions peuvent accepter des arguments et des valeurs par défaut et peuvent ou non retourner des valeurs à l'appelant une fois le code exécuté.

## Comment définir une fonction en Python

La syntaxe générale pour créer une fonction en Python ressemble à ceci :

```
def nom_de_la_fonction(paramètres):
    corps de la fonction
```

Décomposons ce qui se passe ici :

- `def` est un mot-clé qui indique à Python qu'une nouvelle fonction est en cours de définition.
- Ensuite vient un nom de fonction valide de votre choix. Les noms valides commencent par une lettre ou un trait de soulignement mais peuvent inclure des chiffres. Les mots sont en minuscules et séparés par des traits de soulignement. Il est important de savoir que les noms de fonctions ne peuvent pas être un mot-clé réservé de Python.
- Ensuite, nous avons un ensemble de parenthèses ouvrantes et fermantes, `()`. À l'intérieur, il peut y avoir zéro, un ou plusieurs paramètres *optionnels* séparés par des virgules avec leurs valeurs par défaut *optionnelles*. Ceux-ci sont passés à la fonction.
- Ensuite, il y a un deux-points, `:`, qui termine la ligne de définition de la fonction.
- Ensuite, il y a une nouvelle ligne suivie d'un niveau d'indentation (vous pouvez le faire avec 4 espaces en utilisant votre clavier ou avec 1 Tab). L'indentation est importante car elle permet à Python de savoir quel code appartiendra à la fonction.
- Ensuite, nous avons le corps de la fonction. Ici se trouve le code à exécuter – le contenu avec les actions à prendre lorsque la fonction est appelée.
- Enfin, il y a une instruction de retour *optionnelle* dans le corps de la fonction, renvoyant une valeur à l'appelant lorsque la fonction est quittée.

Gardez à l'esprit que si vous oubliez les parenthèses `()` ou le deux-points `:` lors de la tentative de définition d'une nouvelle fonction, Python vous le fera savoir avec une `SyntaxError`.

## Comment définir et appeler une fonction de base en Python

Voici un exemple de fonction de base qui n'a pas d'instruction de retour et ne prend aucun paramètre.

Elle imprime simplement `hello world` chaque fois qu'elle est appelée.

```python
def hello_world_func():
    print("hello world")
```

Une fois que vous avez défini une fonction, le code ne s'exécutera pas de lui-même.

Pour exécuter le code à l'intérieur de la fonction, vous devez faire une *invocation de fonction* ou une *appel de fonction*.

Vous pouvez ensuite appeler la fonction autant de fois que vous le souhaitez.

Pour appeler une fonction, vous devez faire ceci :

```
nom_de_la_fonction(arguments)
```

Voici une décomposition du code :

- Tapez le nom de la fonction.
- Le nom de la fonction doit être suivi de parenthèses. Si des arguments sont requis, ils doivent être passés dans les parenthèses. Si la fonction ne prend aucun argument, vous avez toujours besoin des parenthèses.

Pour appeler la fonction de l'exemple ci-dessus, qui ne prend aucun argument, procédez comme suit :

```python
hello_world_func()

#Sortie
#hello world
```

## Comment définir et appeler des fonctions avec des paramètres

Jusqu'à présent, vous avez vu des fonctions simples qui ne font pas grand-chose à part imprimer quelque chose sur la console.

Que faire si vous souhaitez passer des données supplémentaires à la fonction ?

Nous avons utilisé des termes ici comme *paramètre* et *arguments*.

Quelles sont leurs définitions exactement ?

Les paramètres sont un espace réservé nommé qui transmet des informations aux fonctions.

Ils agissent comme des variables qui sont définies localement dans la ligne de définition de la fonction.

```python
def hello_to_you(nom):
    print("Hello " + nom)
```

Dans l'exemple ci-dessus, il y a un paramètre, `nom`.

Nous aurions pu utiliser le `formatage f-string` à la place – cela fonctionne de la même manière que l'exemple précédent :

```python
def hello_to_you(nom):
    print(f"Hello {nom}")
```

Il peut y avoir une liste de paramètres à l'intérieur des parenthèses, tous séparés par des virgules.

```python
def nom_et_age(nom, age):
    print(f"Je suis {nom} et j'ai {age} ans !")
```

Ici, les paramètres de la fonction sont `nom` et `age`.

Lorsque la fonction est appelée, des arguments sont passés.

Les arguments, comme les paramètres, sont des informations passées aux fonctions.

En particulier, ce sont les valeurs réelles qui correspondent aux paramètres dans la définition de la fonction.

L'appel de la fonction à partir d'un exemple précédent et le passage d'un argument ressemblerait à ceci :

```python
def hello_to_you(nom):
    print(f"Hello {nom}")

hello_to_you("Timmy")
#Sortie
# Hello Timmy
```

La fonction peut être appelée plusieurs fois, en passant différentes valeurs à chaque fois.

```python
def hello_to_you(nom):
    print(f"Hello {nom}")

hello_to_you("Timmy")
hello_to_you("Kristy")
hello_to_you("Jackie")
hello_to_you("Liv")

#Sortie :
#"Hello Timmy"
#"Hello Kristy"
#"Hello Jackie"
#"Hello Liv"
```

Les arguments présentés jusqu'à présent sont appelés **arguments positionnels**.

Tous les arguments positionnels sont très **requis**.

### Le nombre d'arguments positionnels compte

Lors de l'appel de fonctions, vous devez passer le nombre correct d'arguments, sinon il y aura une erreur.

En ce qui concerne les arguments positionnels, le nombre d'arguments passés dans l'appel de fonction doit être exactement le même que le nombre de paramètres dans la définition de la fonction.

Vous ne pouvez en omettre aucun ou en ajouter davantage.

Supposons que vous avez cette fonction qui prend deux paramètres :

```python
def hello_to_you(prenom, nom):
    print(f"Hello, {prenom} {nom}")
```

Si la fonction est appelée avec un seul argument passé, comme ceci, il y aura une erreur :

```python
def hello_to_you(prenom, nom):
    print(f"Hello, {prenom} {nom}")

hello_to_you("Timmy")
```

Sortie :

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello_to_you() missing 1 required positional argument: 'nom'
```

Si la fonction est appelée avec trois arguments passés, il y aura à nouveau une erreur :

```python
def hello_to_you(prenom, nom):
    print(f"Hello, {prenom} {nom}")

hello_to_you("Timmy", "Jones", 34)
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello_to_you() takes 2 positional arguments but 3 were given
```

Il y aura également une erreur si nous ne passons *aucun* argument.

```python
def hello_to_you(prenom, nom):
    print(f"Hello, {prenom} {nom}")

hello_to_you()
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello_to_you() missing 2 required positional arguments: 'prenom' and 'nom'
```

Au lieu de cela, nous avons besoin de deux arguments, puisque deux paramètres sont listés dans la définition de la fonction.

```python
def hello_to_you(prenom, nom):
    print(f"Hello, {prenom} {nom}")

hello_to_you("Timmy", "Jones")
#Sortie :
# Hello, Timmy Jones
```

### L'ordre des arguments positionnels compte

Outre l'inclusion du nombre *correct* d'arguments, il est important de noter que l'*ordre* dans lequel les arguments sont passés compte.

Les arguments doivent être passés dans le même ordre exact que l'ordre des paramètres qui ont été déclarés dans la définition de la fonction.

Cela fonctionne comme une affectation de variable.

Le premier argument est la valeur du premier paramètre dans la définition de la fonction. Le deuxième argument est la valeur du deuxième paramètre dans la définition de la fonction – et ainsi de suite.

```python
def hello_to_you(prenom, nom):
    print(f"Hello, {prenom} {nom}")

hello_to_you("Timmy", "Jones")
#Sortie
#Hello, Timmy Jones
#vous pouvez le visualiser comme :
#prenom = "Timmy"
#nom = "Jones"
```

Si l'ordre n'est pas correct, la sortie pourrait ne pas avoir beaucoup de sens et ne pas être ce que vous aviez prévu.

```python
def langage_prefere(nom, langage):
    print(f"Hello, je suis {nom} et mon langage de programmation préféré est {langage}")

langage_prefere("Python", "Dionysia")
#sortie :
#Hello, je suis Python et mon langage de programmation préféré est Dionysia
#c'est comme si vous aviez fait
#nom="Python"
#langage = "Dionysia"
```

### Comment utiliser les arguments de mot-clé dans les fonctions Python

Jusqu'à présent, vous avez vu un type d'argument, les arguments positionnels.

Avec les arguments positionnels, les fonctions sont appelées avec simplement les valeurs passées dans l'appel de fonction. Là, chaque valeur correspond directement au nombre, à l'ordre et à la position de chaque paramètre dans la définition de la fonction.

Cependant, les fonctions en Python peuvent accepter un autre type d'argument, à savoir les **arguments de mot-clé**.

Dans ce cas, au lieu de simplement passer des valeurs dans l'appel de fonction, vous spécifiez le nom du paramètre puis la valeur que vous souhaitez lui attribuer, sous la forme `clé = valeur`.

Chaque clé correspond à chaque paramètre dans la définition de la fonction.

Appeler explicitement le nom des paramètres et les valeurs qu'ils prennent aide à être extra clair sur ce que vous passez et évite toute confusion possible.

```python
def langage_prefere(nom, langage):
    print(f"Hello, je suis {nom} et mon langage de programmation préféré est {langage}")

langage_prefere(nom="Dionysia", langage="Python")
#sortie :
#Hello, je suis Dionysia et mon langage de programmation préféré est Python
```

Les arguments de mot-clé, comme on le voit ci-dessus, peuvent être dans un ordre particulier. Mais ils sont plus flexibles que les arguments positionnels dans le sens où l'ordre des arguments n'a maintenant plus d'importance.

Vous pourriez donc faire ceci et il n'y aurait pas d'erreurs :

```python
def langage_prefere(nom, langage):
    print(f"Hello, je suis {nom} et mon langage de programmation préféré est {langage}")

langage_prefere(langage="Python", nom="Dionysia")
#sortie :
#Hello, je suis Dionysia et mon langage de programmation préféré est Python
```

Mais vous devez toujours donner le nombre *correct* d'arguments.

Vous pouvez utiliser à la fois des arguments positionnels et des arguments de mot-clé ensemble dans un appel de fonction, comme dans l'exemple ci-dessous où il y a un argument positionnel et un argument de mot-clé :

```python
def langage_prefere(nom, langage):
    print(f"Hello, je suis {nom} et mon langage de programmation préféré est {langage}")

langage_prefere("dionysia", langage="Python")
#sortie :
#Hello, je suis dionysia et mon langage de programmation préféré est Python
```

Dans ce cas, l'ordre compte à nouveau.

Les arguments positionnels viennent toujours en premier et tous les arguments de mot-clé doivent suivre les arguments positionnels. Sinon, il y aura une erreur :

```python
def langage_prefere(nom, langage):
    print(f"Hello, je suis {nom} et mon langage de programmation préféré est {langage}")

langage_prefere(langage="Python", "dionysia")
```

### Comment définir un paramètre avec une valeur par défaut en Python

Les arguments de fonction peuvent également avoir des valeurs par défaut. Ils sont connus sous le nom d'*arguments par défaut ou optionnels*.

Pour qu'un argument de fonction ait une valeur par défaut, vous devez attribuer une valeur par défaut au paramètre dans la définition de la fonction.

Vous faites cela avec la forme `clé=valeur`, où `valeur` sera la valeur par défaut pour ce paramètre.

```python
def langage_prefere(langage="python"):
    print(f"Mon langage de programmation préféré est {langage} !")

langage_prefere()
#sortie
#Mon langage de programmation préféré est python !
```

Comme vous le voyez, les arguments par défaut ne sont *pas* requis dans l'appel de fonction, et la valeur de `langage` sera toujours par défaut Python si une autre valeur n'est pas fournie dans l'appel.

Cependant, les valeurs par défaut peuvent être facilement remplacées si vous fournissez une autre valeur dans l'appel de la fonction :

```python
def langage_prefere(langage="python"):
    print(f"Mon langage de programmation préféré est {langage} !")

langage_prefere("Java")
#imprime "Mon langage de programmation préféré est Java !" sur la console
```

Il peut y avoir plus d'une valeur par défaut passée à la fonction.

Lorsque la fonction est appelée, aucun, un, certains ou tous les arguments par défaut peuvent être fournis et l'ordre n'a pas d'importance.

```python
def details_personnels(nom="Jimmy", age=28, ville="Berlin"):
    print(f"Je suis {nom}, j'ai {age} ans et je vis à {ville}")

#Nous pouvons faire :

details_personnels()
#sortie :
#Je suis Jimmy, j'ai 28 ans et je vis à Berlin

details_personnels(age=30)
#Je suis Jimmy, j'ai 30 ans et je vis à Berlin

details_personnels(ville="Athènes", nom="Ben", age=24)
##Je suis Ben, j'ai 24 ans et je vis à Athènes
```

Les arguments par défaut peuvent être combinés avec des arguments non par défaut dans l'appel de la fonction.

Voici une fonction qui accepte deux arguments : un positionnel, non par défaut (`nom`) et un optionnel, par défaut (`langage`).

```python
def langage_prefere(nom, langage="Python"):
    print(f"Je m'appelle {nom} et mon langage de programmation préféré est {langage} !")

langage_prefere("Dionysia")
#sortie :
#"Je m'appelle Dionysia et mon langage de programmation préféré est Python !"
```

L'argument par défaut, `langage="Python"`, est *optionnel*. Mais l'argument positionnel, `nom`, sera toujours requis. Si un autre `langage` n'est pas passé, la valeur sera toujours par défaut Python.

Une autre chose à mentionner ici est que, lorsque les valeurs par défaut et non par défaut sont utilisées ensemble, l'ordre dans lequel elles sont définies dans la définition de la fonction compte.

Tous les arguments positionnels viennent en premier et sont suivis par les arguments par défaut.

Cela ne fonctionnera pas :

```python
def langage_prefere(langage="Python", nom):
    print(f"Je m'appelle {nom} et mon langage de programmation préféré est {langage} !")

langage_prefere("Dionysia")
```

Sortie :

```
 File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```

## Conclusion

Dans cet article, vous avez appris comment déclarer des fonctions et les invoquer avec des paramètres dans le langage de programmation Python.

C'était une introduction sur la façon de créer des fonctions simples et comment leur passer des données, avec des paramètres. Nous avons également passé en revue les différents types d'arguments comme les arguments *positionnels*, *de mot-clé* et *par défaut*.

Pour résumer :
- L'ordre et le nombre d'arguments *positionnels* comptent.
- Avec les arguments *de mot-clé*, l'ordre n'a pas d'importance. Le nombre compte, cependant, puisque chaque argument de mot-clé correspond à chaque paramètre dans la définition de la fonction.
- Les arguments *par défaut* sont entièrement optionnels. Vous pouvez en passer tous, certains ou aucun.

Si vous êtes intéressé à approfondir et à en apprendre davantage sur le langage de programmation Python, freeCodeCamp propose une [certification Python gratuite](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

Vous commencerez par les bases et les fondamentaux du langage, puis vous progresserez vers des concepts plus avancés comme les structures de données et les bases de données relationnelles. À la fin, vous construirez 5 projets pour mettre en pratique ce que vous avez appris.

Merci d'avoir lu et bon apprentissage.