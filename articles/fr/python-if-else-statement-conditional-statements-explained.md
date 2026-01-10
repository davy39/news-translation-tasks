---
title: Instruction Python If Else – Explication des instructions conditionnelles
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-29T15:32:30.000Z'
originalURL: https://freecodecamp.org/news/python-if-else-statement-conditional-statements-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/clement-helardot-95YRwf6CNw8-unsplash.jpg
tags:
- name: Conditionals
  slug: conditionals
- name: Python
  slug: python
seo_title: Instruction Python If Else – Explication des instructions conditionnelles
seo_desc: 'There are many cases where you don''t want all of your code to be executed
  in your programs.

  Instead, you might want certain code to run only when a specific condition is met,
  and a different set of code to run when the condition is not satisified.

  Th...'
---

Il existe de nombreux cas où vous ne souhaitez pas que tout votre code soit exécuté dans vos programmes.

Au lieu de cela, vous pouvez vouloir qu'un certain code ne s'exécute que lorsqu'une condition spécifique est remplie, et qu'un autre ensemble de code s'exécute lorsque la condition n'est pas satisfaite.

C'est là que les instructions conditionnelles sont utiles.

Les instructions conditionnelles vous permettent de contrôler le flux logique des programmes de manière propre et compacte.

Elles sont des branches – comme des fourches dans la route – qui modifient la manière dont le code est exécuté et gèrent la prise de décision.

Ce tutoriel passe en revue les bases des instructions `if`, `if..else` et `elif` dans le langage de programmation Python, en utilisant des exemples tout au long.

Commençons !

## La syntaxe d'une instruction `if` de base

Une instruction `if` en Python dit essentiellement :

"Si cette expression est évaluée à True, alors exécutez une fois le code qui suit l'expression. Si ce n'est pas True, alors n'exécutez pas le bloc de code qui suit."

La syntaxe générale pour une instruction `if` de base ressemble à ceci :

```
if condition:
    exécuter l'instruction
```

Une instruction `if` se compose de :

- Le mot-clé `if`, qui commence l'instruction `if`.
- Ensuite vient une condition. Une condition peut être évaluée à True ou False. Les parenthèses (`()`) entourant la condition sont facultatives, mais elles aident à améliorer la lisibilité du code lorsqu'il y a plus d'une condition.
- Un deux-points `:` qui sépare la condition de l'instruction exécutable qui suit.
- Une nouvelle ligne.
- Un niveau d'indentation de **4** espaces, qui est une convention Python. Le niveau d'indentation est associé au corps de l'instruction qui suit.
- Enfin vient le corps de l'instruction. Il s'agit du code qui s'exécutera uniquement si l'instruction a été évaluée à True. Nous pouvons avoir plusieurs lignes dans le corps qui peuvent être exécutées, et dans ce cas, nous devons veiller à ce qu'elles aient toutes le même niveau d'indentation.

Prenons l'exemple suivant :

```python
a = 1
b = 2

if b > a:
    print("b est en fait plus grand que a")
```

Sortie :

```
b est en fait plus grand que a
```

Dans l'exemple ci-dessus, nous avons créé deux variables, `a` et `b`, et leur avons attribué les valeurs `1` et `2`, respectivement.

La phrase dans l'instruction print est effectivement imprimée sur la console parce que la condition `b > a` a été évaluée à True, donc le code qui la suivait a été exécuté. Si ce n'était pas True, rien ne se serait passé. Aucun code n'aurait été exécuté.

Si nous avions fait ceci à la place :

```python
a = 1
b = 2

if a > b
    print("a est en fait plus grand que b")
```

Aucun code n'aurait été exécuté et rien n'aurait été imprimé sur la console.

## Comment fonctionnent les instructions `if..else` en Python ?

Une instruction `if` exécute du code uniquement lorsqu'une condition est remplie. Sinon, rien ne se passe.

Que faire si nous voulons également que du code s'exécute lorsque la condition n'est pas remplie ? C'est là que la partie `else` intervient.

La syntaxe d'une instruction `if..else` ressemble à ceci :

```
if condition:
    exécuter l'instruction si la condition est True
else:
     exécuter l'instruction si la condition est False
```

Une instruction `if..else` en Python signifie :

"Lorsque l'expression `if` est évaluée à True, alors exécutez le code qui la suit. Mais si elle est évaluée à False, alors exécutez le code qui suit l'instruction `else`"

L'instruction `else` est écrite sur une nouvelle ligne après la dernière ligne de code indenté et elle *ne peut pas* être écrite seule. Une instruction `else` fait partie d'une instruction `if`.

Le code qui la suit doit également être indenté avec **4** espaces pour montrer qu'il fait partie de la clause `else`.

Le code suivant l'instruction `else` est exécuté *si et seulement si* l'instruction `if` est False. Si votre instruction `if` est True et donc que le code a été exécuté, alors le code dans le bloc `else` ne sera jamais exécuté.

```python
a = 1
b = 2

if a < b:
    print("b est en fait plus grand que a")
else:
    print("a est en fait plus grand que b")
```

Ici, la ligne de code suivant l'instruction `else`, `print("a est en fait plus grand que b")`, ne sera jamais exécutée. L'instruction `if` qui la précédait est True, donc seul ce code s'exécute à la place.

Le bloc `else` s'exécute lorsque :

```python
a = 1
b = 2

if a > b:
    print("a est en fait plus grand que b")
else:
    print("b est en fait plus grand que a")
```

Sortie :
```
b est en fait plus grand que a
```

Soyez conscient que vous ne pouvez pas écrire d'autre code entre `if` et `else`. Vous obtiendrez une `SyntaxError` si vous le faites :

```python
if 1 > 2:
   print("1 est plus grand que 2")
print("hello world")
else:
   print("1 est plus petit que 2")
```

Sortie :

```
File "<stdin>", line 3
print("hello world")
^
SyntaxError: invalid syntax
```

## Comment fonctionne `elif` en Python ?

Que faire si nous voulons avoir plus de deux options ?

Au lieu de dire : "Si la première condition est vraie, faites ceci, sinon faites cela à la place", nous disons maintenant "Si ceci n'est pas True, essayez cela à la place, et si toutes les conditions échouent à être True, faites cela".

`elif` signifie else, if.

La syntaxe de base ressemble à ceci :

```
if première_condition:
    exécuter l'instruction
elif deuxième_condition:
    exécuter l'instruction
else:
    instruction exécutable alternative si toutes les conditions précédentes sont False
```

Nous pouvons utiliser plus d'une instruction `elif`. Cela nous donne plus de conditions et plus d'options.

Par exemple :

```python
x = 1

if x > 10:
    print("x est plus grand que 10 !")
elif x < 10:
      print("x est plus petit que 10 !")
elif x < 20 :
      print("x est plus petit que 20 !")
else:
     print("x est égal à 10")
```

Sortie :

```
x est plus petit que 10 !
```

Dans cet exemple, l'instruction `if` teste une condition spécifique, les blocs `elif` sont deux alternatives, et le bloc `else` est la dernière solution lorsque toutes les conditions précédentes n'ont pas été remplies.

Faites attention à l'ordre dans lequel vous écrivez vos instructions `elif`.

Dans l'exemple précédent, si vous aviez écrit :

```python
x = 1

if x > 10:
    print("x est plus grand que 10 !")
elif x < 20 :
      print("x est plus petit que 20 !")
elif x < 10:
      print("x est plus petit que 10 !")
else:
     print("x est égal à 10")
```

La ligne `x est plus petit que 20 !` aurait été exécutée parce qu'elle est venue en premier.

L'instruction `elif` rend le code plus facile à écrire. Vous pouvez l'utiliser au lieu de suivre les instructions `if..else` à mesure que les programmes deviennent plus complexes et grandissent en taille.

Si toutes les instructions `elif` ne sont pas considérées et sont False, alors et seulement alors, en dernier recours, le code suivant l'instruction `else` s'exécutera.

Par exemple, voici un cas où l'instruction `else` s'exécuterait :

```python
x = 10

if x > 10:
    print("x est plus grand que 10 !")
elif x < 10:
      print("x est plus petit que 10 !")
elif x > 20 :
      print("x est plus grand que 20 !")
else:
     print("x est égal à 10")
```

Sortie :

```
x est égal à 10
```

## Conclusion

Et voilà !

Ce sont les principes de base des instructions `if`, `if..else` et `elif` en Python pour vous aider à démarrer avec les instructions conditionnelles.

À partir de là, les instructions peuvent devenir plus avancées et complexes.

Les instructions conditionnelles peuvent être imbriquées à l'intérieur d'autres instructions conditionnelles, selon le problème que vous essayez de résoudre et la logique derrière la solution.

Merci d'avoir lu et bon codage !