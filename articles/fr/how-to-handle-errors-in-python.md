---
title: Comment gérer les erreurs en Python – les mots-clés try, except, else et finally
  expliqués
subtitle: ''
author: P S Mohammed Ali
co_authors: []
series: null
date: '2022-11-01T14:53:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-errors-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/11.jpg
tags:
- name: error handling
  slug: error-handling
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Comment gérer les erreurs en Python – les mots-clés try, except, else et
  finally expliqués
seo_desc: '“It’s hard enough to find an error in your code when you’re looking for
  it; it’s even harder when you’ve assumed your code is error-free.”― Steve McConnell


  Errors are inevitable in a programmer''s life. In fact, while writing programs,
  errors can be ...'
---

> « Il est déjà assez difficile de trouver une erreur dans votre code lorsque vous la cherchez ; c'est encore plus difficile lorsque vous avez supposé que votre code était exempt d'erreurs. »
> – Steve McConnell

Les erreurs sont inévitables dans la vie d'un programmeur. En fait, lors de l'écriture de programmes, les erreurs peuvent être vraiment utiles pour identifier les bugs logiques et les erreurs de syntaxe dans votre code.

Mais, si vous pouvez anticiper une erreur dans un ensemble particulier de lignes de code avant l'exécution, alors vous pouvez gérer ces erreurs et rendre le code exempt d'erreurs.

## Pourquoi la gestion des erreurs est importante

Gérer ou prendre soin des erreurs dont vous avez connaissance aide le flux de code et son exécution à se dérouler sans interruption. Si des erreurs se produisent dans une ligne de code, la gestion des erreurs s'en occupe, puis le code reprend son exécution.

Prenons un exemple et comprenons pourquoi nous avons besoin de la gestion des erreurs :

```python
a = 12
b = 6
result = a/b
print(result)
print("J'ai atteint la fin de la ligne")
```

D'après le code ci-dessus, que pouvez-vous attendre ? Eh bien, la variable `result` affiche `2.0` et sur la ligne suivante, la console affiche `J'ai atteint la fin de la ligne`. C'est ce que nous attendons.

Changeons la valeur de `b` de `b = 6` à `b = 0` et exécutons.

```python
1. a = 12
2. b = 0
3. result = a/b
4. print(result)
5. print("J'ai atteint la fin de la ligne")
```

Lorsque ce code est exécuté, nous obtenons une erreur comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/2.PNG align="left")

*Message d'erreur affiché lorsque b est défini à 0*

Le code n'a pas affiché la valeur `result` et il n'a pas non plus affiché `J'ai atteint la fin de la ligne`.

Le message d'erreur ci-dessus indique `division par zéro`, ce qui signifie que si nous essayons de diviser un nombre par `0`, nous obtiendrons cette erreur.

Le problème est à la ligne `3`. Même si le code n'a pas affiché la valeur `result`, il aurait dû afficher `J'ai atteint la fin de la ligne`. Mais il ne l'a pas fait – pourquoi ?

Eh bien, parce que l'interpréteur Python s'est arrêté à la ligne 3 lorsque `a` a été divisé par `0`. À ce moment-là, il a levé une erreur dans la console et a quitté le code.

L'une des solutions naïves pour résoudre ce problème peut être de coder en dur les valeurs. Si les valeurs de `a` et `b` sont codées en dur, alors l'exécution du code résoudra cette erreur dans une certaine mesure.

Mais l'autre problème majeur qui peut survenir est lorsque l'utilisateur souhaite donner des valeurs à `a` et `b` au moment de l'exécution.

```python
a = int(input())
b = int(input())
result = a/b
print(result)
print("J'ai atteint la fin de la ligne")
```

À ce moment-là, il y a une forte probabilité que l'utilisateur donne `0` comme entrée pour `b`. Afin de gérer ce type d'erreur attendue, nous utiliserons certaines méthodes de gestion des erreurs afin d'éviter d'interrompre le flux d'exécution (même si l'utilisateur pourrait donner une entrée invalide comme `0` comme entrée pour `b`).

## Comment utiliser les mots-clés Try et Except en Python

Toute ligne de code plus sujette aux erreurs est placée dans le bloc `try`. Si une erreur se produit, alors le bloc `except` s'en occupera.

La structure du code ressemble à ceci :

```python
try:
   code qui peut/ne peut pas produire d'erreurs
except:
   lorsque l'erreur survient, ce bloc de code s'exécute.
   Sinon, ce bloc de code ne s'exécute pas
```

Revenons à l'exemple standard que nous avons discuté. Nous allons gérer le problème de `division par zéro` en utilisant les blocs `try/except`.

Insérons les lignes de code qui ont une forte probabilité de produire une erreur. Dans notre cas, les lignes `1-4` de notre code ont un fort potentiel de produire une erreur. Nous plaçons donc ces quatre lignes dans le bloc `try` :

```python
try:
  a = int(input())
  b = int(input())
  result = a/b
  print(result)
except:
  print("Nous avons attrapé une erreur")
 
print("J'ai atteint la fin de la ligne")
```

Maintenant, lorsque nous donnons à `b` une valeur de `0`, une erreur se produit. Le bloc `except` s'exécute donc et l'interpréteur affiche `Nous avons attrapé une erreur` et sort du bloc except pour reprendre l'impression de `J'ai atteint la fin de la ligne`.

D'autre part, lorsque nous donnons à `b` une valeur non nulle, nous imprimons la valeur `result`. Le code sort du bloc try et reprend l'impression de `J'ai atteint la fin de la ligne`.

Dans les deux cas, nous sommes en mesure d'exécuter jusqu'à la dernière ligne de code sans aucune interruption.

Outre try et except, il est assez important de comprendre les mots-clés `else` et `finally` qui accompagnent `try` et `except`.

Le bloc de code `else` vient après les blocs `try` et `except` et s'exécute lorsqu'aucune erreur n'est levée à partir du bloc de code `try`. De même, le bloc de code `finally` vient après le bloc `else` et s'exécute qu'il y ait des erreurs ou non – ce bloc s'exécutera à coup sûr.

Maintenant que vous comprenez comment fonctionnent les blocs de code `try`, `except`, `else` et `finally`, l'ordre du flux sera :

```python
try:
   code qui peut/ne peut pas produire d'erreurs

except:
   lorsque l'erreur survient, ce bloc de code s'exécute

else:
   lorsque l'erreur ne survient pas, ce bloc de code s'exécute

finally:
   Ce bloc s'exécutera qu'il y ait une erreur ou non.
```

En appliquant la même structure au problème de division de nombres, nous obtenons ceci :

```python
try:
  a = int(input())
  b = int(input())
  result = a/b
  print(result)

except:
   print("Nous avons attrapé une erreur")

else:
   print("Hourra, nous n'avons aucune erreur")

finally:
   print("J'ai atteint la fin de la ligne")
```

Lorsque `b` est assigné à `0`, nous obtenons une erreur. Le bloc except s'exécute donc et affiche `Nous avons attrapé une erreur`, puis le bloc de code finally s'exécute et affiche `J'ai atteint la fin de la ligne`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/55.PNG align="left")

*Flux d'exécution du code lorsqu'une erreur se produit*

D'autre part, si `b` reçoit `6` par exemple (ou toute valeur non nulle), alors nous divisons la valeur `a` par `6` et la stockons dans la variable `result`. Le code affiche ensuite la valeur `result`.

Ensuite, le bloc `else` s'exécute et affiche `Hourra, nous n'avons aucune erreur`, puis le bloc de code finally s'exécute et affiche `J'ai atteint la fin de la ligne`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/56.PNG align="left")

*Flux d'exécution du code lorsqu'aucune erreur ne se produit*

## Résumé

Maintenant, j'espère que vous comprenez comment vous pouvez implémenter la gestion des erreurs en Python afin d'attraper les erreurs potentielles avec les blocs `try/except`.

Vous avez également appris comment utiliser les blocs de code `else` et `finally` qui sont associés à ces méthodes de gestion des erreurs.

Bon codage...