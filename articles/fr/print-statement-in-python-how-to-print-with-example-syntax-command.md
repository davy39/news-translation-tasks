---
title: Instruction print en Python – Comment imprimer avec la syntaxe de commande
  d'exemple
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-12-10T17:45:08.000Z'
originalURL: https://freecodecamp.org/news/print-statement-in-python-how-to-print-with-example-syntax-command
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/pexels-wendelin-jacober-1440504.jpg
tags:
- name: Python
  slug: python
seo_title: Instruction print en Python – Comment imprimer avec la syntaxe de commande
  d'exemple
seo_desc: 'How to print out information is one of the first things you learn as a
  beginner programmer.

  This article goes over what you need to know about printing in Python, and we''ll
  look at plenty of code examples along the way.

  Let''s get started!

  What is pri...'
---

Comment imprimer des informations est l'une des premières choses que vous apprenez en tant que programmeur débutant.

Cet article passe en revue ce que vous devez savoir sur l'impression en Python, et nous examinerons de nombreux exemples de code en cours de route.

Commençons !

## À quoi sert print ?

L'impression est probablement la première chose que vous apprendrez lorsque vous commencerez votre voyage d'apprentissage de Python.

C'est une sorte de tradition d'écrire un programme "Hello World" comme vos premières lignes de code. Et vous faites cela en utilisant la fonction `print()` pour sortir ce morceau de texte vers la console.

L'impression est principalement utilisée pour afficher des informations sur la console, qu'il s'agisse d'afficher un certain message ou un résultat de calcul. Mais elle est également utilisée à des fins de débogage.

### Impression en Python 2 vs impression en Python 3

Pour imprimer quelque chose sur la console en Python 2, il suffisait d'utiliser le mot-clé `print` :

```python
print "Hello world"

#sortie
#Hello world
```

Cela s'appelait une instruction print.

En Python 3, l'instruction print a été remplacée par la fonction `print()`.

```python
print("Hello world")

#sortie
#Hello world
```

Si vous n'ajoutez pas l'ensemble des parenthèses ouvrantes et fermantes qui suivent `print` en Python 3, vous obtiendrez une erreur lorsque vous exécuterez le code :

```python
print "Hello world"

#sortie
#File "/Users/dionysialemonaki/python_articles/demo.py", line 1
#    print "Hello world"
#   ^^^^^^^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean #print(...)?
```

Ainsi, en Python 2, le mot-clé print était une instruction, alors qu'en Python 3, print est une fonction.

## Syntaxe de `print()` en Python

La syntaxe complète de la fonction `print()`, ainsi que les valeurs par défaut des paramètres qu'elle prend, sont présentées ci-dessous.

Voici à quoi ressemble `print()` sous le capot :

```
print(*object,sep=' ',end='\n',file=sys.stdout,flush= False)
```

Décomposons cela :

- `*object` peut être aucun, un ou plusieurs valeurs de données à imprimer, et il peut être de n'importe quel type de données. Les objets sont convertis en chaîne avant l'impression.
- `sep` est un paramètre optionnel qui spécifie comment plus d'un objet sont séparés. La valeur par défaut est `' '` – un espace.
- `end` est un paramètre optionnel qui spécifie avec quoi la ligne se terminera. Par défaut, l'appel de print se termine par un saut de ligne, avec `\n` étant le caractère de nouvelle ligne.
- `file` est un paramètre optionnel qui est un objet avec une méthode write – il peut écrire et ajouter (ajouter) la sortie à un fichier. La valeur par défaut est `sys.stdout` (ou sortie standard du système) et la sortie est affichée à l'écran.
- `flush` est un paramètre booléen qui spécifie si le flux sera forcé à être vidé ou mis en mémoire tampon. Vidé signifie si l'appel de print prendra effet immédiatement. La valeur par défaut est False (ou mis en mémoire tampon).

La fonction `print()` n'a pas de valeur de retour.

## Comment imprimer des objets en Python

Même si vous ne passez aucun argument à `print()` – c'est-à-dire que vous ne passez aucun objet à imprimer – vous devez toujours inclure un ensemble de parenthèses vides.

Cela affichera simplement une ligne vide sur la console dans un tel cas.

Cela est mieux illustré lors de l'utilisation de la REPL Python (Read Eval Print Loop).

Pour démarrer une nouvelle session, après avoir installé Python sur votre machine, tapez `python3`. Lorsque vous avez terminé, tapez `exit()` pour terminer la session.

```python
>>> print()

>>> 
```

C'est similaire à appuyer sur la touche `Entrée` de votre clavier lors de l'écriture dans un traitement de texte. Tout comme la touche Entrée crée une nouvelle ligne et déplace le curseur vers une nouvelle ligne, de la même manière, appeler `print()` sans arguments affiche une ligne vide.

## Comment imprimer des chaînes de caractères en Python

Vous imprimez des chaînes de caractères en passant le littéral de chaîne comme argument à `print()`, enfermé dans des guillemets simples ou doubles.

La sortie sera le littéral de chaîne, sans les guillemets.

```python
print("J'apprends Python")

#sortie
#J'apprends Python
```

Si vous avez une chaîne de caractères ou une phrase que vous souhaitez imprimer, vous pouvez la stocker dans une variable et passer le nom de la variable comme argument à `print()`.

```python
salutation = "Hey là !"

print(salutation)

#sortie
#Hey là !
```

Il est considéré comme une bonne pratique de donner des noms significatifs aux variables, selon le contenu stocké à l'intérieur. Cela rendra le code plus lisible pour vous-même et pour toute autre personne avec qui vous travaillez.

Comme montré dans la syntaxe de `print()` plus tôt, il peut y avoir plus d'un objet passé comme arguments (`*object`).

Vous pouvez faire cela en **séparant chaque argument avec une virgule**.

```python
print("Bonjour","là !")

#sortie
#Bonjour là !
```

Il y a deux arguments : "Bonjour" et "là !".

Dans les exemples ci-dessous, les arguments sont un littéral de chaîne et une variable.

```python
nom_complet = "John Doe"

print("Hey",nom_complet)

#sortie
#Hey John Doe
```

Vous pouvez également faire cela en utilisant la **concaténation** avec l'opérateur d'addition :

```python
nom_complet = "John Doe"

print("Hey " + nom_complet)

#sortie
#Hey John Doe
```

Avec la concaténation, vous devez tenir compte des espaces, sinon vous finirez par obtenir ce qui suit :

```python
nom_complet = "John Doe"

print("Hey" + nom_complet)

#sortie
#HeyJohn Doe
```

Gardez à l'esprit que vous ne pouvez pas ajouter un littéral de chaîne avec un nombre.

Cela entraînerait une erreur :

```python
print("Hey" + 7)

#sortie
#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 1, in #<module>
#    print("Hey" + 7)
#TypeError: can only concatenate str (not "int") to str
```

Comme le suggère l'erreur, vous ne pouvez concaténer (ajouter) qu'une chaîne à une chaîne. Cela signifie que si vous souhaitez inclure un nombre, vous devrez le convertir en son équivalent de chaîne par transtypage.

```python
#utilisez la méthode str() pour convertir un entier en chaîne

print("Hey" + str(7))

#sortie
#Hey 7
```

Une manière moderne d'imprimer des objets est d'utiliser des **`f-strings`**.

```python
nom_complet = "John Doe"

print(f"Hey là {nom_complet}")

#sortie
#Hey là John Doe
```

Les chaînes de caractères ne sont pas les seuls objets qui peuvent être passés comme arguments.

En fait, `print()` accepte tous les types de données que vous verrez dans la section suivante.

### Exemples de la façon d'imprimer le reste des types de données intégrés de Python

```python
#comment imprimer des entiers
print(7) #la sortie est 7

#comment imprimer des flottants
print(7.0) #la sortie est 7.0

#comment imprimer des nombres complexes
print(1j) #la sortie est 1j

#comment imprimer une liste
print([10,20,30]) #la sortie est [10,20,30]

#comment imprimer un tuple
print((10,20,30)) #la sortie est (10,20,30)

#comment imprimer un dictionnaire
print({"langage": "Python", "domaine": "science des données"})
#la sortie est {"langage": "Python", "domaine": "science des données"

#comment imprimer un ensemble
print({"automne","hiver","printemps","été"})
#la sortie est {"automne","hiver","printemps","été"}

#comment imprimer un booléen
print(True) #la sortie est True
print(False) #la sortie est False
```

## Comment changer la façon dont les objets sont séparés dans la fonction `print()`

Comme vous l'avez vu dans la syntaxe de la fonction `print()`, `sep` détermine comment un objet est séparé du suivant.

Par défaut, les objets sont séparés par un seul espace.

```python
print("Bonjour","Monde")

#sortie
#Bonjour Monde
```

Pour désactiver cela, vous changez explicitement la valeur de `sep` par le caractère que vous souhaitez.

Par exemple, les objets peuvent être séparés par des tirets :
```python
print("Bonjour","Monde", sep="---")

#sortie
#Bonjour---Monde
```

Ou vous pourriez même supprimer l'espace en ajoutant une chaîne vide à la place :

```python
print("Bonjour","Monde", sep="")

#sortie
#BonjourMonde
```

## Comment supprimer le saut de ligne par défaut dans `print()`

Comme vous l'avez vu plus tôt dans la décomposition de la syntaxe de la fonction `print()`, le paramètre par défaut pour l'argument mot-clé `end` était `'\n'`.

Par défaut, après chaque appel de print, une nouvelle ligne est créée.

Si vous appelez print deux fois séparément, l'une après l'autre, vous verrez que le deuxième appel est affiché sur une nouvelle ligne immédiatement après le premier appel.

```python
print("Bonjour")
print("Monde")

#sortie
#Bonjour
#Monde
```

Pour désactiver cela, vous pouvez changer explicitement la valeur de `end` en une chaîne vide, `""`.

```python
print("Bonjour ", end="")
print("Monde")

#sortie
#Bonjour Monde
```

Maintenant, les deux sont sur la même ligne.

Vous pouvez même la changer en un point :

```python
print("Bonjour", end=".")
print("Monde")

#sortie
#Bonjour.Monde
```

Tout ce qui n'est pas la valeur par défaut supprimera le saut de ligne qui est créé.

## Comment diriger la sortie de `print()` vers un fichier en Python

Vous voudrez principalement imprimer la sortie vers la sortie standard, ou la sortie standard de la ligne de commande.

Il peut y avoir des moments, cependant, où vous voudrez diriger cette sortie vers un fichier existant.

Supposons que vous avez un fichier texte et que vous souhaitez ajouter du texte en utilisant la fonction `print()`.

Pour ouvrir et écrire dans un fichier en Python, vous appelez la fonction `open()`. À l'intérieur, vous incluez le nom du fichier, `output.txt` dans ce cas, et le mode `-w`, signifiant pour l'écriture uniquement.

Avec ce mode, chaque fois que vous exécutez votre code, le contenu du fichier sera supprimé et remplacé par tout nouveau texte que vous ajoutez.

Si vous ne voulez pas perdre de contenu, vous pourriez utiliser le mode `-a` à la place, pour ajouter du texte à la fin du fichier.

À l'intérieur de la fonction `print()`, vous ajoutez tout texte que vous souhaitez ajouter au fichier et définissez le paramètre `file` égal au nom de l'espace réservé que vous avez créé pour le fichier auquel vous souhaitez ajouter le texte, dans ce cas `f`.

```python
with open('output.txt', 'w') as f:
    print('Bonjour le monde !', file=f)
```

## Conclusion

Merci d'avoir lu et d'être arrivé à la fin ! J'espère que vous avez trouvé ce tutoriel utile. Vous connaissez maintenant les bases de l'utilisation de la fonction `print()` en Python.

Si vous êtes intéressé à en apprendre davantage sur le langage de programmation Python, consultez la [certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp pour commencer.

Elle couvre tous les concepts fondamentaux de la programmation et progresse progressivement vers des sujets plus avancés. À la fin, vous construirez également cinq projets pour solidifier votre apprentissage.

Bon codage !