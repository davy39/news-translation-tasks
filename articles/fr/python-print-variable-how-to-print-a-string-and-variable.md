---
title: Python Print Variable – Comment imprimer une chaîne et une variable
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-12-07T17:26:18.000Z'
originalURL: https://freecodecamp.org/news/python-print-variable-how-to-print-a-string-and-variable
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/denise-jans-_dXkaD3l574-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Print Variable – Comment imprimer une chaîne et une variable
seo_desc: 'Python is a versatile and flexible language – there is often more than
  one way to achieve something.

  In this tutorial, you''ll see some of the ways you can print a string and a variable
  together.

  Let''s get started!

  How to use the print() function in P...'
---

Python est un langage polyvalent et flexible – il existe souvent plusieurs façons d'accomplir quelque chose.

Dans ce tutoriel, vous verrez quelques-unes des façons dont vous pouvez imprimer une chaîne et une variable ensemble.

Commençons !

## Comment utiliser la fonction `print()` en Python

Pour imprimer quoi que ce soit en Python, vous utilisez la fonction `print()` – c'est le mot-clé `print` suivi d'une paire de parenthèses ouvrantes et fermantes, `()`.

```python
#comment imprimer une chaîne
print("Hello world")

#comment imprimer un entier
print(7)

#comment imprimer une variable
#pour simplement imprimer la variable seule, incluez seulement son nom

fave_language = "Python"
print(fave_language)

#sortie

#Hello world
#7
#Python
```

Si vous omettez les parenthèses, vous obtiendrez une erreur :

```python
print "hello world"

#sortie après avoir exécuté le code :
#File "/Users/dionysialemonaki/python_articles/demo.py", line 1
#    print "hello world"
#    ^^^^^^^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

Si vous écrivez votre code Python dans Visual Studio Code, avec l'[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), vous verrez également un soulignement et un indice qui indiquent tous deux que quelque chose ne va pas tout à fait :

![Screenshot-2021-12-07-at-3.08.14-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-07-at-3.08.14-PM.png)

Comme mentionné ci-dessus, l'instruction print est utilisée pour sortir toutes sortes d'informations. Cela inclut les données textuelles et numériques, les variables et d'autres types de données.

Vous pouvez également imprimer du texte (ou des chaînes) combiné avec des variables, le tout en une seule instruction.

Vous verrez quelques-unes des différentes façons de faire cela dans les sections qui suivent.

## Comment imprimer une variable et une chaîne en Python en utilisant la concaténation

Concatenate, selon le dictionnaire, signifie lier (des choses) ensemble dans une chaîne ou une série.

Vous faites cela en ajoutant diverses choses (dans ce cas, la programmation – vous ajoutez des données) les unes aux autres, en utilisant l'opérateur d'addition Python, `+`.

Gardez à l'esprit que la concaténation n'est utilisée que pour les chaînes, donc si la variable que vous voulez concaténer avec le reste des chaînes est d'un type de données entier, vous devrez la convertir en chaîne avec la fonction `str()`.

Dans l'exemple suivant, je veux imprimer la valeur d'une variable ainsi que du texte supplémentaire.

J'ajoute les chaînes entre guillemets doubles et le nom de la variable sans rien l'entourer, en utilisant l'opérateur d'addition pour les enchaîner toutes ensemble :

```python
fave_language = "Python"

print("I like coding in " + fave_language + " the most")

#sortie
#I like coding in Python the most
```

Avec la concaténation de chaînes, vous devez ajouter les espaces vous-même, donc si dans l'exemple précédent je n'avais pas inclus d'espaces à l'intérieur des guillemets, la sortie aurait ressembler à ceci :

```python
fave_language = "Python"

print("I like coding in" + fave_language + "the most")

#sortie
#I like coding inPythonthe most
```

Vous pouvez même ajouter les espaces séparément :

```python
fave_language = "Python"

print("I like coding in" + " " + fave_language + " "  + "the most")

#sortie
#I like coding in Python the most
```

Ce n'est pas la méthode la plus préférée pour imprimer des chaînes et des variables, car elle peut être sujette aux erreurs et prendre du temps.

## Comment imprimer une variable et une chaîne en Python en séparant chaque élément par une virgule

Vous pouvez imprimer du texte à côté d'une variable, séparés par des virgules, dans une seule instruction print.

```python
first_name = "John"

print("Hello",first_name)

#sortie
#Hello John
```

Dans l'exemple ci-dessus, j'ai d'abord inclus du texte que je voulais imprimer entre guillemets doubles – dans ce cas, le texte était la chaîne `Hello`.

Après le guillemet fermant, j'ai ajouté une virgule qui sépare ce morceau de texte de la valeur contenue dans le nom de la variable (`first_name` dans ce cas) que j'ai ensuite incluse.

J'aurais pu ajouter plus de texte suivant la variable, comme ceci :

```python
first_name = "John"

print("Hello",first_name,"good to see you")

#sortie
#Hello John good to see you
```

Cette méthode fonctionne également avec plus d'une variable :

```python
first_name = "John"
last_name = "Doe"

print("Hello",first_name,last_name,"good to see you")

#sortie
Hello John Doe good to see you
```

Assurez-vous de séparer tout avec une virgule.

Ainsi, vous séparez le texte des variables avec une virgule, mais aussi les variables des autres variables, comme montré ci-dessus.

Si la virgule n'avait pas été ajoutée entre `first_name` et `last_name`, le code aurait généré une erreur :

```python
first_name = "John"
last_name = "Doe"

print("Hello",first_name last_name,"good to see you")

#sortie
#File "/Users/dionysialemonaki/python_articles/demo.py", line 4
#    print("Hello",first_name last_name,"good to see you")
#                 ^^^^^^^^^^^^^^^^^^^^
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

Comme vous le voyez, les messages d'erreur de Python sont extrêmement utiles et rendent le processus de débogage un peu plus facile :)

## Comment imprimer une variable et une chaîne en Python en utilisant la mise en forme de chaîne

Vous utilisez la mise en forme de chaîne en incluant un ensemble d'accolades ouvrantes et fermantes, `{}`, à l'endroit où vous voulez ajouter la valeur d'une variable.

```python
first_name = "John"

print("Hello {}, hope you're well!")
```

Dans cet exemple, il y a une variable, `first_name`.

À l'intérieur de l'instruction print, il y a un ensemble de guillemets doubles ouvrants et fermants avec le texte qui doit être imprimé.

À l'intérieur de cela, j'ai ajouté un ensemble d'accolades à l'endroit où je veux ajouter la valeur de la variable `first_name`.

Si j'essaie d'exécuter ce code, il aura la sortie suivante :

```python
#sortie
#Hello {}, hope you're well!
```

Il n'imprime pas réellement la valeur de `first_name` !

Pour l'imprimer, je dois ajouter la méthode de chaîne `.format()` à la fin de la chaîne – c'est immédiatement après le guillemet fermant :

```python
first_name = "John"

print("Hello {}, hope you're well!".format(first_name))

#sortie
#Hello John, hope you're well!
```

Lorsque qu'il y a plus d'une variable, vous utilisez autant d'accolades que le nombre de variables que vous voulez imprimer :

```python
first_name = "John"
last_name = "Doe"

print("Hello {} {}, hope you're well!")
```

Dans cet exemple, j'ai créé deux variables et je veux les imprimer toutes les deux, l'une après l'autre, donc j'ai ajouté deux ensembles d'accolades à l'endroit où je veux que les variables soient substituées.

Maintenant, en ce qui concerne la méthode `.format()`, l'ordre dans lequel vous placez les noms de variables à l'intérieur compte.

Ainsi, la valeur du nom de la variable qui sera ajoutée en premier dans la méthode sera à la place de la première accolade, la valeur du nom de la variable qui sera ajoutée en second sera à la place de la deuxième accolade, et ainsi de suite.

Assurez-vous de séparer les noms de variables par des virgules à l'intérieur de la méthode :

```python
first_name = "John"
last_name = "Doe"

print("Hello {} {}, hope you're well!".format(first_name,last_name))

#sortie
#Hello John Doe, hope you're well!
```

Si j'avais inversé l'ordre des noms à l'intérieur de la méthode, la sortie aurait été différente :

```python
first_name = "John"
last_name = "Doe"

print("Hello {} {}, hope you're well!".format(last_name,first_name))

#sortie
#Hello Doe John, hope you're well!
```

## Comment imprimer une variable et une chaîne en Python en utilisant les `f-strings`

Les `f-strings` sont une meilleure façon, plus lisible et concise, d'atteindre la mise en forme de chaîne par rapport à la méthode que nous avons vue dans la section précédente.

La syntaxe est plus facile et nécessite moins de travail manuel.

La syntaxe générale pour créer une `f-string` ressemble à ceci :

```python
print(f"I want this text printed to the console!")

#sortie
#I want this text printed to the console!
```

Vous incluez d'abord le caractère `f` avant les guillemets ouvrants et fermants, à l'intérieur de la fonction `print()`.

Pour imprimer une variable avec une chaîne en une ligne, vous incluez à nouveau le caractère `f` au même endroit – juste avant les guillemets.

Ensuite, vous ajoutez le texte que vous voulez à l'intérieur des guillemets, et à l'endroit où vous voulez ajouter la valeur d'une variable, vous ajoutez un ensemble d'accolades avec le nom de la variable à l'intérieur :

```python
first_name = "John"

print(f"Hello, {first_name}!")

#sortie
#Hello, John!
```

Pour imprimer plus d'une variable, vous ajoutez un autre ensemble d'accolades avec le nom de la deuxième variable :

```python
first_name = "John"
last_name = "Doe"

print(f"Hello, {first_name} {last_name}!")

#sortie
#Hello, John Doe!
```

L'ordre dans lequel vous placez les noms de variables compte, alors assurez-vous de les ajouter selon la sortie que vous voulez.

Si j'avais inversé l'ordre des noms, j'aurais obtenu la sortie suivante :

```python
first_name = "John"
last_name = "Doe"

print(f"Hello, {last_name} {first_name}!")

#sortie
#Hello, Doe John!
```

## Conclusion

Merci d'avoir lu et d'être arrivé à la fin ! Vous connaissez maintenant plusieurs façons différentes d'imprimer des chaînes et des variables ensemble en une seule ligne en Python.

Si vous voulez en apprendre plus sur Python, consultez la [Certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Elle est adaptée aux débutants car elle commence par les fondamentaux et construit progressivement des concepts plus avancés. Vous aurez également l'occasion de construire cinq projets et de mettre en pratique toutes les nouvelles connaissances que vous acquérez.

Bon codage !