---
title: Exemple de déclaration If-Else en Python
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-10T17:05:36.000Z'
originalURL: https://freecodecamp.org/news/python-if-else-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/rosie-steggles-h1OhvEIIcxs-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Exemple de déclaration If-Else en Python
seo_desc: 'If-Else statements – AKA conditional logic – are the bedrock of programming.
  And Python has these in spades.

  Python offers several options for evaluating variables, their states, and whether
  specific conditions are met:


  Vanilla if-else statements

  if...'
---

Les déclarations If-Else – également connues sous le nom de logique conditionnelle – sont la pierre angulaire de la programmation. Et Python en regorge.

Python offre plusieurs options pour évaluer les variables, leurs états et si des conditions spécifiques sont remplies :

* Déclarations if-else classiques
* Déclarations if sans la partie else
* Déclarations if-else imbriquées
* Déclarations else-if ou `elif`
* Et déclarations if-else en boucle sous la forme de for-else et while-else

Nous parlerons de tout cela et expliquerons également l'opérateur double-égal `==` extrêmement utile.

## Comment écrire une déclaration if-else en Python ?

Si vous cherchez simplement un exemple à copier-coller, voici une déclaration if-else super simple en Python :

```py
if x < y:
	print("x est inférieur à y")
else:
	print("x est égal ou supérieur à y")
```

Notez que le fait que Python soit sensible à l'espace garantit que ces déclarations if-else sont faciles à lire – même lorsqu'elles sont imbriquées sur plusieurs niveaux.

Cela étant dit, parlons un peu plus de la logique conditionnelle et de l'importance des déclarations if-else pour Python et d'autres langages de programmation.

## Comment utilisons-nous la déclaration if-else ?

Les déclarations if-else sont une forme de logique conditionnelle. Essentiellement, cela signifie que :

1. Nous testons une condition. Par exemple, si une variable donnée est égale à une autre variable donnée.
2. Si la condition est vraie, nous exécutons le bloc de code suivant.
3. Et si la condition est fausse, nous exécutons un bloc de code différent.

Cela est absolument crucial pour tout type de programmation. Vous ne pouvez pas avoir de langages de programmation Turing-complets sans une forme de logique conditionnelle. En Python, cela signifie beaucoup de déclarations if-else.

## En quoi la déclaration if est-elle différente de la déclaration if else en Python ?

Vous n'avez pas techniquement besoin de la partie `else` de la déclaration if-else. Par exemple :

```py
age = int(input("Entrez votre âge : ")) 
if age >= 18: print("Vous êtes éligible pour voter !")

```

Pour voir comment cela fonctionne, voici le REPL Python :

```py
>>> age = int(input("Entrez votre âge : "))
Entrez votre âge : 20
>>> if age >= 18: print("Vous êtes éligible pour voter !")
Vous êtes éligible pour voter !

>>> age = int(input("Entrez votre âge : "))
Entrez votre âge : 17
>>> if age >= 18: print("Vous êtes éligible pour voter !")
[rien ne se passe]

```

Comme vous pouvez le voir, c'est un peu comme une déclaration if-else avec un `else` invisible. Si la partie `else` était présente et que la condition n'était pas remplie, ce serait comme "OK. Continuez alors."

## Quelle est la différence entre Else et Elif dans la structure IF ?

Si vous souhaitez avoir plus de conditions potentielles, vous pouvez utiliser une déclaration `elif`.

Voici un exemple de déclaration `elif` :

```py
if x > y:
    print("x est supérieur à y")
elif x < y:
    print("x est inférieur à y")
else:
    print("x est égal à y")

```

Vous remarquerez que l'opérateur `elif` apparaît entre les opérateurs `if` et `else` initiaux.

Notez également que vous pouvez utiliser autant de `elif` que vous le souhaitez.

```py
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
elif condition4:
    statement4
elif condition5:
    statement5
else
	statement6
```

## Qu'est-ce que for else et while else en Python ?

Vous pouvez combiner la logique conditionnelle avec des boucles en utilisant une déclaration `for else` ou `while else`.

Voici un exemple de déclaration `for else` qui atteint le `break` et sort :

```py
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("Ce code ne s'exécutera que si la boucle for se termine sans atteindre une déclaration break.")

# cela produira :
0
1
2
3
4
5

```

Et voici la même déclaration `for if` qui commence à un nombre plus élevé, ce qui ignorera l'événement `break` et se terminera. Jetez un œil au code et à sa sortie :

```py
for i in range(6,10):
    print(i)
    if i == 5:
        break
else:
    print("Ce code ne s'exécutera que si la boucle for se termine sans atteindre une déclaration break.")

# cela produira :
6
7
8
9
Ce code ne s'exécutera que si la boucle for se termine sans atteindre une déclaration break.

```

## Peut-on avoir plusieurs déclarations if en Python ?

Absolument. Vous pouvez avoir autant de déclarations if imbriquées que vous le souhaitez. Faites attention, cependant. Cela peut conduire à la soi-disant "pyramide de la mort".

Voici un exemple de déclarations if imbriquées :

```py
if x == 5:
	if y == 10:
	    print("x est 5 et y est 10")
	else:
	    print("x est 5 et y est autre chose")
else:
	print("x est autre chose")

```

Remarquez comment il y a deux déclarations if-else, mais l'une d'elles est imbriquée dans l'autre. Cela va pour une ou deux couches, mais cela peut devenir confus rapidement :

```py
if x == 1:
    if y == 2:
        if z == 3:
            print("x, y et z sont tous égaux à 1, 2 et 3, respectivement")
        else:
            print("x et y sont égaux à 1 et 2, respectivement, mais z n'est pas égal à 3")
    else:
        print("x est égal à 1 mais y n'est pas égal à 2")
else:
    print("x n'est pas égal à 1")

```

## Peut-on avoir 3 conditions dans une déclaration if ?

Oui. Mais si vous faites cela, il est probablement judicieux d'utiliser certains opérateurs `elif` dans votre déclaration pour plus de clarté.

Voici un exemple de déclaration if avec 3 conditions :

```py
if (condition1):
    # exécuter code1
elif (condition2):
    # exécuter code2
elif (condition3):
    # exécuter code3

```

## Que signifie `==` en Python ?

L'opérateur `==` de Python – également connu sous le nom d'opérateur d'égalité – est un opérateur de comparaison qui retourne True si les deux opérandes (les variables ou valeurs à gauche et à droite de `==`) sont égaux. Sinon, il retournera False.

C'est un outil extrêmement courant pour créer des déclarations if et d'autres logiques conditionnelles.

Apprenez-le. Connaissez-le. Aimez-le.

## J'espère que vous avez beaucoup appris sur les déclarations if.

Moi aussi, en dépoussiérant mes connaissances Python et en écrivant ce tutoriel. J'espère que vous avez trouvé cela utile.

Si vous souhaitez en apprendre davantage sur la programmation Python et la technologie en général, essayez [le programme de codage principal de freeCodeCamp](https://www.freecodecamp.org/learn). C'est gratuit.