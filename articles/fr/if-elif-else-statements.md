---
title: Les instructions If, Elif et Else en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T23:32:00.000Z'
originalURL: https://freecodecamp.org/news/if-elif-else-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e09740569d1a4ca3afe.jpg
tags:
- name: Python
  slug: python
seo_title: Les instructions If, Elif et Else en Python
seo_desc: 'If Elif Else Statements

  The if/elif/else structure is a common way to control the flow of a program, allowing
  you to execute specific blocks of code depending on the value of some data.

  if statement

  If the condition following the keyword if evaluates...'
---

## **Les instructions If Elif Else**

La structure `if`/`elif`/`else` est une méthode courante pour contrôler le flux d'un programme, vous permettant d'exécuter des blocs de code spécifiques en fonction de la valeur de certaines données.

### Instruction if

Si la condition suivant le mot-clé `if` est évaluée comme `true`, le bloc de code sera exécuté. Notez que les parenthèses ne sont pas utilisées avant et après la vérification de la condition comme dans d'autres langues.

```python
if True:
  print('Le bloc If sera exécuté !')
```

```python
x = 5

if x > 4:
  print("La condition était vraie !") # cette instruction est exécutée
```

### Instruction else

Vous pouvez optionnellement ajouter une réponse `else` qui sera exécutée si la condition est `false` :

```python
if not True:
  print('L'instruction If sera exécutée !')
else:
  print('L'instruction Else sera exécutée !')
```

Ou vous pouvez également voir cet exemple :

```python
y = 3

if y > 4:
  print("Je ne serai pas imprimé !") # cette instruction n'est pas exécutée
else:
  print("La condition n'était pas vraie !") # cette instruction est exécutée
```

*Notez qu'il n'y a pas de condition suivant le mot-clé `else` - il attrape toutes les situations où la condition était `false`*

### Instruction elif

Plusieurs conditions peuvent être vérifiées en incluant une ou plusieurs vérifications `elif` après votre instruction `if` initiale. Gardez simplement à l'esprit qu'une seule condition sera exécutée :

```python
z = 7

if z > 8:
  print("Je ne serai pas imprimé !") # cette instruction n'est pas exécutée
elif z > 5:
  print("Je le serai !") # cette instruction sera exécutée
elif z > 6:
  print("Je ne serai pas imprimé non plus !") # cette instruction n'est pas exécutée
else:
  print("Moi non plus !") # cette instruction n'est pas exécutée
```

*Note : seule la première condition évaluée comme `true` sera exécutée.* Même si `z > 6` est `true`, le bloc `if/elif/else` se termine après la première condition vraie. Cela signifie qu'un `else` ne sera exécuté que si aucune des conditions n'était `true`.

### Instructions if imbriquées

Nous pouvons également créer des if imbriqués pour la prise de décision. Avant de continuer, veuillez vous référer au guide d'indentation une fois avant de continuer.

Prenons un exemple de recherche d'un nombre qui est pair et également supérieur à 10

```text
python 
x = 34
if x %  2 == 0:  # voici comment vous créez un commentaire et maintenant, vérifiez si le nombre est pair.
  if x > 10:
    print("Ce nombre est pair et est supérieur à 10")
  else:
    print("Ce nombre est pair, mais pas supérieur à 10")
else:
  print ("Le nombre n'est pas pair. Donc, pas besoin de vérifier plus loin.")
```

Ce n'était qu'un simple exemple pour les if imbriqués. N'hésitez pas à explorer davantage en ligne.

Bien que les exemples ci-dessus soient simples, vous pouvez créer des conditions complexes en utilisant des [comparaisons booléennes](https://guide.freecodecamp.org/python/comparisons) et des [opérateurs booléens](https://guide.freecodecamp.org/python/boolean-operations).

### Instruction if-else en ligne en Python

Nous pouvons également utiliser des instructions if-else en ligne dans les fonctions Python. L'exemple suivant devrait vérifier si le nombre est supérieur ou égal à 50, si oui, retourner True :

```text
python 
x = 89
is_greater = True if x >= 50 else False

print(is_greater)
```

Sortie

```text
>
True
>
```

## Plus d'informations sur les instructions if/elif/else :

* [Comment sortir de l'enfer if/else](https://www.freecodecamp.org/news/so-youre-in-if-else-hell-here-s-how-to-get-out-of-it-fc6407fec0e/)
* [If/else en JavaScript](https://www.freecodecamp.org/news/javascript-essentials-how-to-make-life-decisions-with-if-else-statements-1908ff7cf5da/)