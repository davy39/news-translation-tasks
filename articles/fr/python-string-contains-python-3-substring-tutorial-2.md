---
title: Python String Contains – Tutoriel sur les sous-chaînes en Python 3
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-11-17T16:47:04.000Z'
originalURL: https://freecodecamp.org/news/python-string-contains-python-3-substring-tutorial-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-kevin-ku-577585.jpg
tags:
- name: Python
  slug: python
seo_title: Python String Contains – Tutoriel sur les sous-chaînes en Python 3
seo_desc: 'In this article, you will learn how to check if a string contains a substring
  in Python.

  Checking if a string contains a substring comes in handy when you have received
  user input and want your program to behave a certain way – or even when you want
  ...'
---

Dans cet article, vous apprendrez à vérifier si une chaîne contient une sous-chaîne en Python.

Vérifier si une chaîne contient une sous-chaîne est utile lorsque vous avez reçu une entrée utilisateur et que vous souhaitez que votre programme se comporte d'une certaine manière – ou même lorsque vous souhaitez remplacer un mot par un autre.

Python offre de nombreuses façons de confirmer si une sous-chaîne est présente dans une chaîne, et dans ce guide rapide, vous en verrez quelques-unes en action.

Voici ce que nous allons couvrir :

1. [Comment vérifier si une chaîne contient une sous-chaîne en utilisant l'opérateur `in`](#operateur-in)
    1. [Comment effectuer une recherche insensible à la casse en utilisant l'opérateur `in`](#insensible-casse)
2. [Comment vérifier si une chaîne contient une sous-chaîne en utilisant la méthode `.index()`](#methode-index)
3. [Comment vérifier si une chaîne contient une sous-chaîne en utilisant la méthode `.find()`](#methode-find)

## Comment vérifier si une chaîne contient une sous-chaîne en utilisant l'opérateur `in` en Python <a name="operateur-in"></a>

Utiliser l'opérateur `in` est l'une des façons les plus claires, les plus lisibles et les plus pythoniques de confirmer si une sous-chaîne est présente dans une chaîne.

Par conséquent, l'opérateur `in` est la méthode préférée pour vérifier qu'une chaîne contient une sous-chaîne.

La syntaxe générale pour utiliser l'opérateur `in` est la suivante :

```
sous_chaine in chaine
```

L'opérateur `in` retourne une valeur booléenne. Une valeur booléenne est soit `True` soit `False`.

L'opérateur `in` retourne `True` si la sous-chaîne est présente dans la chaîne et `False` si la sous-chaîne n'est pas présente.

```python
>>> apprendre_codage = "Vous pouvez apprendre à coder gratuitement !"
>>> "gratuit" in apprendre_codage
True
```

Dans l'exemple ci-dessus, je suis entré dans la console interactive de Python, également connue sous le nom d'interpréteur Python ou shell Python.

Vous pouvez y accéder après avoir installé Python localement, ouvert votre terminal et tapé `Python` ou `Python3` selon votre système.

Je stocke la phrase `Vous pouvez apprendre à coder gratuitement !` dans une variable appelée `apprendre_codage`.

Ensuite, je vérifie si la sous-chaîne `gratuit` est présente dans la phrase `Vous pouvez apprendre à coder gratuitement !` en utilisant l'opérateur `in`.

Puisque la sous-chaîne est présente, `in` retourne `True`.

Il est important de noter que l'opérateur `in` vérifie uniquement si la sous-chaîne est présente et existe dans la chaîne. Il ne vérifie pas la position de la sous-chaîne, ni ne donne d'informations sur le nombre de fois où la sous-chaîne apparaît dans la chaîne.

En aparté, vous pouvez également choisir de vérifier si une sous-chaîne n'est **pas** présente dans une chaîne en utilisant l'opérateur `not in` :

```python
>>> apprendre_codage = "Vous pouvez apprendre à coder gratuitement !"
>>> "gratuit" not in apprendre_codage
False
```

Cette fois, j'utilise l'opérateur `not in` pour vérifier si la sous-chaîne `gratuit` n'est **pas** présente dans la chaîne `Vous pouvez apprendre à coder gratuitement !`. Puisque `gratuit` est présent, l'opérateur `not in` retourne `False`.

Maintenant, revenons à l'opérateur `in`.

Vous pouvez utiliser l'opérateur `in` pour contrôler le comportement de votre programme en définissant des conditions.

Prenons l'exemple suivant :

```python
entree_utilisateur = input("Do you need to pay to learn to code?: ")

if "yes" in entree_utilisateur:
  print("Faux ! Vous pouvez apprendre à coder gratuitement !")
```

Dans l'exemple ci-dessus, je demande une entrée à un utilisateur et stocke sa réponse dans une variable nommée `entree_utilisateur`.

Ensuite, j'utilise une instruction conditionnelle associée à l'opérateur `in` pour prendre une décision (si vous avez besoin d'un rappel sur les instructions conditionnelles en Python, lisez [cet article](https://www.freecodecamp.org/news/python-else-if-statement-example/)).

Si sa réponse contient la sous-chaîne `yes`, alors `in` retourne la phrase `Faux ! Vous pouvez apprendre à coder gratuitement` car le code dans l'instruction `if` s'exécute :

```
Do you need to pay to learn to code?: yes, I think you do
Faux ! Vous pouvez apprendre à coder gratuitement !
```

Dans l'exemple ci-dessus, la chaîne que l'utilisateur a entrée, `yes, I think you do`, contient la sous-chaîne `yes` et le code dans le bloc `if` s'exécute.

Que se passe-t-il lorsque l'utilisateur entre `Yes, I think you do` avec un `Y` majuscule au lieu d'un `y` minuscule ?

```
Do you need to pay to learn to code?: Yes, I think you do
```

Comme vous le voyez, rien ne se passe ! Le programme n'a pas de sortie car les chaînes Python sont sensibles à la casse.

Vous pourriez écrire une instruction `else` pour résoudre ce problème. Cependant, vous pourriez plutôt tenir compte de la sensibilité à la casse lors de la vérification de la présence d'une sous-chaîne dans une chaîne.

Voyons comment faire cela dans la section suivante.

### Comment effectuer une recherche insensible à la casse en utilisant l'opérateur `in` en Python <a name="insensible-casse"></a>

Dans la section ci-dessus, vous avez vu que lors de la recherche d'une sous-chaîne dans une chaîne, la recherche est sensible à la casse.

Alors, comment pouvez-vous rendre la recherche insensible à la casse ?

Vous pouvez convertir toute l'entrée utilisateur en minuscules en utilisant la méthode `.lower()` :

```python
entree_utilisateur = input("Do you need to pay to learn to code?: ").lower()

if "yes" in entree_utilisateur:
  print("Faux ! Vous pouvez apprendre à coder gratuitement !")
```

Maintenant, lorsque l'utilisateur entre `Yes` avec un `Y` majuscule, le code dans l'instruction `if` s'exécute, même si vous cherchiez la sous-chaîne `yes` avec un `y` minuscule. Cela est dû au fait que vous avez converti le texte de l'entrée utilisateur en lettres minuscules.

## Comment vérifier si une chaîne contient une sous-chaîne en utilisant la méthode `.index()` en Python <a name="methode-index"></a>

Vous pouvez utiliser la méthode `.index()` de Python pour trouver le numéro d'index de départ du premier caractère de la première occurrence d'une sous-chaîne dans une chaîne :

```python
apprendre_codage = "Vous pouvez apprendre à coder gratuitement ! Oui, gratuitement !"
sous_chaine = "gratuit"

print(apprendre_codage.index(sous_chaine))

# sortie

# 26
```

Dans l'exemple ci-dessus, j'ai stocké la chaîne `Vous pouvez apprendre à coder gratuitement ! Oui, gratuitement !` dans une variable nommée `apprendre_codage`.

J'ai également stocké la sous-chaîne `gratuit` dans la variable `sous_chaine`.

Ensuite, j'ai appelé la méthode `.index()` sur la chaîne et passé la sous-chaîne comme argument pour trouver où la première occurrence de la sous-chaîne `gratuit` apparaît. (La chaîne stockée dans `apprendre_codage` contient deux instances de la sous-chaîne `gratuit`).

Enfin, j'ai imprimé le résultat.

Si la sous-chaîne n'est **pas** présente dans la chaîne, une erreur `ValueError: substring not found` est levée :

```python
apprendre_codage = "Vous pouvez apprendre à coder gratuitement ! Oui, gratuitement !"
sous_chaine = "payant"

print(apprendre_codage.index(sous_chaine))

# sortie

# Traceback (most recent call last):
#  File "main.py", line 4, in <module>
#    print(apprendre_codage.index(sous_chaine))
# ValueError: substring not found
```

La méthode `.index()` est utile lorsque vous souhaitez connaître l'emplacement de la sous-chaîne que vous recherchez et où la sous-chaîne se produit et commence dans la chaîne.

L'opérateur `in` vous indique si la sous-chaîne existe dans la chaîne, tandis que la méthode `.index()` vous indique également *où* elle existe.

Cela dit, `.index()` n'est pas idéal lorsque Python ne trouve pas la sous-chaîne dans la chaîne car elle lève une erreur `ValueError`.

Si vous souhaitez éviter que cette erreur ne soit levée lors de la recherche d'une chaîne, et que vous ne souhaitez pas utiliser l'opérateur `in`, vous pouvez utiliser la méthode `find()` de Python à la place.

## Comment vérifier si une chaîne contient une sous-chaîne en utilisant la méthode `.find()` en Python <a name="methode-find"></a>

La méthode `.find()` fonctionne de manière similaire à la méthode `.index()` – elle vérifie si une chaîne contient une sous-chaîne, et si la sous-chaîne est présente, elle retourne son index de départ.

```python
apprendre_codage = "Vous pouvez apprendre à coder gratuitement ! Oui, gratuitement !"
sous_chaine = "gratuit"

print(apprendre_codage.find(sous_chaine))

# sortie

# 26
```

La différence entre la méthode `.find()` et la méthode `.index()` est qu'avec `.find()`, vous n'avez pas à vous soucier de la gestion des exceptions, contrairement à `.index()`.

Comme vous l'avez vu dans la section ci-dessus, lorsque la chaîne ne contient pas la sous-chaîne, `index()` lève une erreur.

En revanche, lorsque vous utilisez la méthode `.find()` et que la chaîne ne contient pas la sous-chaîne que vous recherchez, `.find()` retourne `-1` sans lever d'exception :

```python
apprendre_codage = "Vous pouvez apprendre à coder gratuitement ! Oui, gratuitement !"
sous_chaine = "payant"

print(apprendre_codage.find(sous_chaine))

# sortie

# -1
```

## Conclusion

Espérons que cet article vous a aidé à comprendre comment vérifier si une chaîne contient une sous-chaîne en Python.

Pour en savoir plus sur le langage de programmation Python, consultez [la certification Python de freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu, et bon codage !