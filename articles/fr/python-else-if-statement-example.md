---
title: Exemple de déclaration Else-If en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-07-01T22:02:40.000Z'
originalURL: https://freecodecamp.org/news/python-else-if-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/pexels-pixabay-459653.jpg
tags:
- name: Python
  slug: python
seo_title: Exemple de déclaration Else-If en Python
seo_desc: "Conditional statements are helpful for decision-making and are a core concept\
  \ in all programming languages.\nIn this article, you will learn how to write conditional\
  \ statements in Python. \nSpecifically, you will learn how to write if, if else,\
  \ and eli..."
---

Les instructions conditionnelles sont utiles pour la prise de décision et constituent un concept central dans tous les langages de programmation.

Dans cet article, vous apprendrez à écrire des instructions conditionnelles en Python.

Plus précisément, vous apprendrez à écrire des instructions `if`, `if else` et `elif` (également connues sous le nom de `else if`) en Python.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une instruction `if` ?](#if)
    1. [Syntaxe d'une instruction `if`](#if-syntax)
    2. [Exemple d'une instruction `if`](#if-example)
2. [Qu'est-ce qu'une instruction `if else` ?](#if-else)
    1. [Exemple d'une instruction `if else`](#if-else-example)
3. [Qu'est-ce qu'une instruction `elif` ?](#elif)
    1. [Exemple d'une instruction `elif`](#elif-example)

## Qu'est-ce qu'une instruction `if` en Python ? <a name="if"></a>

Une instruction `if` est également connue sous le nom d'**instruction conditionnelle**, et les instructions conditionnelles sont un pilier de la prise de décision.

Une instruction conditionnelle effectue une action spécifique basée sur une vérification ou une comparaison.

En résumé, une instruction `if` prend une décision basée sur une condition.

La condition est une expression booléenne. Une expression booléenne ne peut être que l'une des deux valeurs : `True` ou `False`.

Ainsi, essentiellement, une instruction `if` dit : "Exécutez le code suivant uniquement *si* et seulement *si* cette condition évalue à `True`. Si ce n'est *pas* le cas, alors n'exécutez pas ce code du tout. Ignorez-le simplement et passez-le entièrement".

### Comment créer une instruction `if` en Python - Une analyse de la syntaxe <a name="if-syntax"></a>

La syntaxe générale d'une instruction `if` en Python est la suivante :

```python
if expression:
   # exécutez ce code si l'expression évalue à True
   code statement(s)
```

Décomposons-la :

- Vous commencez l'instruction `if` en utilisant le mot-clé `if`.
- Vous laissez un espace et ajoutez ensuite une valeur booléenne. Une valeur booléenne sera une expression qui évalue à `True` ou `False`.
- Vous ajoutez ensuite un deux-points, `:`.
- Sur une nouvelle ligne, ajoutez un niveau d'indentation. De nombreux éditeurs de code le feront automatiquement pour vous. Par exemple, lorsque vous utilisez l'éditeur [Visual Studio Code](https://code.visualstudio.com/) avec l'extension [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), juste après avoir écrit le deux-points de l'étape précédente et avoir appuyé sur `Enter`, il indentera automatiquement votre code avec le bon niveau d'indentation. Ce niveau d'indentation est la manière dont Python sait que les instructions de code que vous allez écrire sont associées à l'instruction `if`.
- Enfin, écrivez toutes les lignes d'instructions de code. Ces lignes s'exécuteront si et seulement si l'expression évalue à `True`. Si l'expression évalue à `False`, elles ne s'exécuteront pas.

### Quel est un exemple d'une instruction `if` en Python ? <a name="if-example"></a>

Ensuite, voyons un exemple d'une instruction `if` en action.

Je veux demander à l'utilisateur d'entrer son langage de programmation préféré et stocker sa réponse dans une variable nommée `language`.

```python
language = input("Veuillez entrer votre langage de programmation préféré : ")
```

Ensuite, je vais définir une condition.

Si l'utilisateur entre `Python` comme langage préféré, alors et seulement alors, je veux afficher un message dans la console disant que c'est la bonne réponse.

Ainsi, la condition vérifiera si la valeur stockée dans la variable `language` est égale à `Python`.

Pour cela, vous utilisez l'opérateur d'égalité (`==`) pour vérifier si la valeur stockée dans la variable `language` est égale à la chaîne `Python`.

```python
language = input("Veuillez entrer votre langage de programmation préféré : ")

if language == "Python":
    print("Correct ! Bien sûr que c'est Python !")
```

J'exécute mon code, et lorsque l'invite "Veuillez entrer votre langage de programmation préféré :" apparaît, j'entre `Python`.

J'obtiens alors la sortie suivante :

```
# sortie

# Veuillez entrer votre langage de programmation préféré : Python
# Correct ! Bien sûr que c'est Python !
```

La condition (`language == "Python"`) est `True`, donc le code dans l'instruction `if` s'exécute.

Si je réexécute mon programme et entre un autre langage de programmation, il n'y aura pas de sortie car la condition sera `False`.

Le code à l'intérieur de l'instruction `if` ne **s'exécutera pas**, et l'instruction `if` sera entièrement ignorée :

```python
# sortie

# Veuillez entrer votre langage de programmation préféré : Java
```

À ce stade, il est également utile de mentionner que vous devez vous assurer d'indenter le code à l'intérieur de l'instruction `if`. Si vous oubliez d'indenter cette instruction print, vous finirez par obtenir l'erreur d'indentation suivante :

```python
language = input("Veuillez entrer votre langage de programmation préféré : ")

if language == "Python":
# Ne faites pas cela !
print("Correct ! Bien sûr que c'est Python !")

# sortie

# print("Correct ! Bien sûr que c'est Python !")
# ^
# IndentationError: expected an indented block after 'if' statement on line 3
```

## Qu'est-ce qu'une instruction `if else` en Python ? <a name="if-else"></a>

Écrire des instructions `if` seules, surtout plusieurs d'entre elles, n'est pas très utile. Ce n'est pas non plus considéré comme une bonne pratique lorsque le programme devient de plus en plus grand. C'est pourquoi une instruction `if` est généralement accompagnée d'une instruction `else`.

L'instruction `if else` dit essentiellement : "`if` cette condition est True, faites ce qui suit, `else` faites cela à la place".

Le code à l'intérieur d'une instruction `else` est le code que vous voulez exécuter si et seulement si la condition que vous avez définie dans votre instruction `if` évalue à `False`.

Si la condition dans votre instruction `if` évalue à `True`, le code à l'intérieur de l'instruction `else` ne s'exécutera jamais.

Le mot-clé `else` est la solution lorsque la condition `if` est False et que le code à l'intérieur du bloc `if` ne s'exécute pas. Il fournit une alternative.

La syntaxe générale d'une instruction `if else` en Python est la suivante :

```
if condition:
    # exécutez ce code si la condition est True
    code statement(s)
else:
    # si la condition ci-dessus est False, exécutez ce code
    code statement(s)
```

### Quel est un exemple d'une instruction `if else` en Python ? <a name="if-else-example"></a>

Reprenons l'exemple précédent :

```python
language = input("Veuillez entrer votre langage de programmation préféré : ")

if language == "Python":
    print("Correct ! Bien sûr que c'est Python !")
```

Comme vous l'avez vu précédemment, lorsque j'entre la chaîne `Python`, le code dans la fonction `print()` s'exécute car la condition évalue à `True`.

Cependant, il n'y a pas d'alternative lorsque l'utilisateur entre quelque chose qui n'est **pas** égal à la chaîne `Python`.

C'est là que l'instruction `else` est utile et est ajoutée à l'instruction `if` :

```python
language = input("Veuillez entrer votre langage de programmation préféré : ")

if language == "Python":
    print("Correct ! Bien sûr que c'est Python !")
else:
    print("Hmm..Êtes-vous sûr que ce n'est pas Python ?")
```

Si la condition est `False`, le code dans l'instruction `if` est ignoré. Au lieu de cela, le code dans l'instruction `else` s'exécute :

```python
# sortie

# Veuillez entrer votre langage de programmation préféré : Java
# Hmm..Êtes-vous sûr que ce n'est pas Python ?
```

Une chose à noter à ce stade est le fait que vous ne pouvez pas écrire de code supplémentaire entre l'instruction `if else` :

```python
language = input("Veuillez entrer votre langage de programmation préféré : ")

if language == "Python":
    print("Correct ! Bien sûr que c'est Python !")
# Ne faites pas cela !!
print("Hello world")
else:
    print("Hmm..Êtes-vous sûr que ce n'est pas Python ?")

# sortie
# else:
    ^^^^
# SyntaxError: invalid syntax
```

## Qu'est-ce qu'une instruction `elif` en Python ? <a name="elif"></a>

`elif` signifie `else if`.

Lorsque vous voulez définir plus de conditions et ne pas seulement avoir les instructions `if` et `else` à choisir, vous pouvez introduire des instructions `elif`.

Si l'instruction `if` est `False`, Python passera à l'instruction `elif` et essaiera de vérifier la condition définie dans ce bloc.

Vous pouvez également écrire plusieurs blocs `elif`, selon la variété d'options que vous souhaitez avoir.

Une instruction `elif` signifie essentiellement : "Si cette condition est True, faites ce qui suit. Si ce n'est pas le cas, essayez de faire cela à la place. Cependant, si aucune des conditions ci-dessus n'est True et que tout le reste échoue, faites enfin cela."

La syntaxe générale d'une instruction `elif` est la suivante :

```python
if condition:
    # si la condition est True, exécutez ce code
    code statement(s)
elif:
    # si la condition ci-dessus était False et que cette condition est True,
   # exécutez le code dans ce bloc
    code statement(s)
else:
    # si les deux conditions ci-dessus sont False, exécutez ce code
    code statement
```

Le code est évalué dans l'ordre où il est écrit, de haut en bas.

Lorsque Python trouve une condition qui évalue à `True`, il exécutera le code dans ce bloc et ignorera le reste.

Ainsi, si le code dans le bloc `if` est `True`, aucun des autres blocs ne s'exécutera. Ils seront ignorés et sautés.

Si le code dans le bloc `if` est `False`, il passera au bloc `elif`.

Si celui-ci est `True`, alors le reste des blocs est ignoré.

Si ce n'est pas le cas, Python passera à d'autres blocs `elif` s'il y en a.

Enfin, si toutes les conditions sont `False`, alors et seulement alors le code dans le bloc `else` s'exécutera. Le bloc `else` signifie essentiellement que "quand tout le reste échoue, exécutez ce code à la place".

### Quel est un exemple d'une instruction `elif` en Python ? <a name="elif-example"></a>

Voyons un exemple de fonctionnement de l'instruction `elif`.

Prenons l'exemple suivant :

```python
age = int(input("Veuillez entrer votre âge : "))

if age < 18:
    print("Vous devez avoir plus de 18 ans pour continuer")
elif age < 21:
    print("Vous devez avoir plus de 21 ans")
else:
    print("Vous avez plus de 18 et 21 ans donc vous pouvez continuer")
```

Si l'instruction `if` est `True`, le reste du code est ignoré :

```python
# sortie

# Veuillez entrer votre âge : 14
# Vous devez avoir plus de 18 ans pour continuer
```

Lorsque l'instruction `if` est `False`, Python passe au bloc `elif` et vérifie cette condition. Si l'instruction `elif` est `True`, le reste du code est ignoré :

Si c'est `True`, Python exécutera le code dans le bloc `elif` et ignorera le reste du code :

```python
# sortie

# Veuillez entrer votre âge : 19
# Vous devez avoir plus de 21 ans
```

Si les deux conditions précédentes sont toutes `False`, alors le dernier recours est le bloc `else` :

```python
# sortie

# Veuillez entrer votre âge : 45
# Vous avez plus de 18 et 21 ans donc vous pouvez continuer
```

## Conclusion

Et voilà ! Vous savez maintenant comment écrire des instructions `if`, `if else` et `elif` en Python.

J'espère que vous avez trouvé ce tutoriel utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Bon codage !