---
title: 'Valeurs Truthy et Falsy en Python : Une Introduction Détaillée'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-01-22T12:22:00.000Z'
originalURL: https://freecodecamp.org/news/truthy-and-falsy-values-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Truthy-and-Falsy-Values.png
tags:
- name: Computer Science
  slug: computer-science
- name: learning to code
  slug: learning-to-code
- name: programming languages
  slug: programming-languages
- name: Python
  slug: python
seo_title: 'Valeurs Truthy et Falsy en Python : Une Introduction Détaillée'
seo_desc: 'Welcome

  In this article, you will learn:


  What truthy and falsy values are.

  What makes a value truthy or falsy.

  How to use the bool() function to determine if a value is truthy or falsy.

  How to make objects from user-defined classes truthy or falsy u...'
---

## Bienvenue

Dans cet article, vous apprendrez :

* Ce que sont les valeurs truthy et falsy.
* Ce qui rend une valeur truthy ou falsy.
* Comment utiliser la fonction `bool()` pour déterminer si une valeur est truthy ou falsy.
* Comment rendre les objets de classes définies par l'utilisateur truthy ou falsy en utilisant la méthode spéciale `__bool__`.

**Commençons ! ✨**

## 🔹 Valeurs de Vérité vs. Valeurs Truthy et Falsy

Permettez-moi de vous présenter ces concepts en les comparant aux valeurs `True` et `False` que nous utilisons typiquement.

Les expressions avec des opérandes et des opérateurs évaluent à soit `True` soit `False` et peuvent être utilisées dans une condition `if` ou `while` pour déterminer si un bloc de code doit s'exécuter.

Voici un exemple :

```python
# Expression 5 < 3
>>> if 5 < 3:
	print("True")
else:
	print("False")

# Sortie
False
```

Dans cet exemple, tout fonctionne comme prévu car nous avons utilisé une expression avec deux opérandes et un opérateur `5 < 3`.

**Mais que pensez-vous qu'il se passera si nous essayons d'exécuter ce code ?**

```python
>>> a = 5

>>> if a:
	print(a)
```

Remarquez que maintenant nous n'avons pas une expression typique à côté du mot-clé `if`, seulement une variable :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-3.png)

Étonnamment, la sortie est :

```python
5
```

Si nous changeons la valeur de `a` à zéro, comme ceci :

```python
>>> a = 0

>>> if a:
	print(a)
```

Il n'y a pas de sortie.

Je suis sûr que vous devez vous demander ceci maintenant : **qu'est-ce qui a fait que le code s'exécute avec succès ?**

La variable `a` n'est pas une expression typique. Elle n'a pas d'opérateurs et d'opérandes, alors pourquoi a-t-elle évalué à `True` ou `False` selon sa valeur ?

La réponse réside dans le concept des valeurs Truthy et Falsy, qui ne sont pas des valeurs de vérité en elles-mêmes, mais qui évaluent à soit `True` soit `False`.

## 🔸 Valeurs Truthy et Falsy

En Python, des **valeurs** individuelles peuvent évaluer à soit `True` soit `False`. Elles n'ont pas nécessairement besoin de faire partie d'une expression plus large pour évaluer à une valeur de vérité car elles ont déjà une valeur déterminée par les règles du langage Python.

Les règles de base sont :

* Les valeurs qui évaluent à **`False`** sont considérées comme `**Falsy**`.
* Les valeurs qui évaluent à **`True`** sont considérées comme `**Truthy**`.

Selon la [Documentation Python](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) :

> Tout objet peut être testé pour sa valeur de vérité, pour une utilisation dans une condition [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) ou [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) ou comme opérande des opérations booléennes ci-dessous (and, or, not).

### 🔹 Contexte Booléen

Lorsque nous utilisons une valeur comme partie d'une expression plus large, ou comme condition `if` ou `while`, nous l'utilisons dans un **contexte booléen**. 

Vous pouvez penser à un contexte booléen comme une partie "particulière" de votre code qui nécessite qu'une valeur soit soit `True` soit `False` pour avoir du sens.

Par exemple, (voir ci-dessous) la condition après le mot-clé `if` ou après le mot-clé `while` doit évaluer à soit `True` soit `False` :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-1.png)

💡 **Astuce :** La valeur peut être stockée dans une variable. Nous pouvons écrire le nom de la variable après le mot-clé `if` ou `while` au lieu de la valeur elle-même. Cela fournira la même fonctionnalité.

Maintenant que vous savez ce que sont les valeurs truthy et falsy et comment elles fonctionnent dans un contexte booléen, regardons quelques exemples réels de valeurs truthy et falsy.

### 🔸 Valeurs Falsy

**Séquences et Collections :**

* Listes vides `[]`
* Tuples vides `()`
* Dictionnaires vides `{}`
* Ensembles vides `set()`
* Chaînes de caractères vides `""`
* Plages vides `range(0)`

**Nombres**

* Zéro de tout type numérique.
* Entier : `0`
* Flottant : `0.0`
* Complexe : `0j`

**Constantes**

* `None`
* `False`

Les valeurs falsy étaient la raison pour laquelle il n'y avait pas de sortie dans notre exemple initial lorsque la valeur de `a` était zéro.

La valeur `0` est falsy, donc la condition `if` sera `False` et la conditionnelle ne s'exécutera pas dans cet exemple :

```python
>>> a = 0
>>> if a:
	print(a)

# Pas de Sortie
```

### 🔹 Valeurs Truthy

Selon la [Documentation Python](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) :

> Par défaut, un objet est considéré comme **vrai**.

**Les valeurs truthy incluent :**

* Séquences ou collections non vides (listes, tuples, chaînes de caractères, dictionnaires, ensembles).
* Valeurs numériques différentes de zéro.
* `True`

C'est pourquoi la valeur de `a` a été imprimée dans notre exemple initial car sa valeur était 5 (une valeur truthy) :

```python
>>> a = 5

>>> if a:
	print(a)
    
 # Sortie
 5
```

### 🔸 La Fonction Intégrée bool()

Vous pouvez vérifier si une valeur est truthy ou falsy avec la fonction intégrée `bool()`.

Selon la [Documentation Python](https://docs.python.org/3/library/functions.html#bool), cette fonction :

> Retourne une valeur booléenne, c'est-à-dire l'une de `True` ou `False`. _x (l'argument)_ est converti en utilisant la procédure standard de test de vérité.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-2.png)

Vous devez simplement passer la valeur comme argument, comme ceci :

```python
>>> bool(5)
True
>>> bool(0)
False
>>> bool([])
False
>>> bool({5, 5})
True
>>> bool(-5)
True
>>> bool(0.0)
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(range(0))
False
>>> bool(set())
False
>>> bool({5, 6, 2, 5})
True
```

💡 **Astuce :** Vous pouvez également passer une variable comme argument pour tester si sa valeur est truthy ou falsy.

### 🔹 Exemples Réels

L'un des avantages de l'utilisation des valeurs truthy et falsy est qu'elles peuvent vous aider à rendre votre code plus concis et lisible. Voici deux exemples réels.

**Exemple :**   
Nous avons cette fonction `print_even()` qui prend comme argument une liste ou un tuple contenant des nombres et imprime uniquement les valeurs qui sont paires. Si l'argument est vide, elle imprime un message descriptif :

```python
def print_even(data):
	if len(data) > 0:
		for value in data:
			if value % 2 == 0:
				print(value)
 	else:
 		print("L'argument ne peut pas être vide")
```

Remarquez cette ligne :

```python
if len(data) > 0:
```

Nous pouvons rendre la condition beaucoup plus concise avec les valeurs truthy et falsy :

```python
if data:
```

Si la liste est vide, `data` évaluera à `False`. Si elle n'est pas vide, elle évaluera à `True`. Nous obtenons la même fonctionnalité avec un code plus concis.

Ce serait notre fonction finale :

```python
def print_even(data):
	if data:
		for value in data:
			if value % 2 == 0:
				print(value)
 	else:
 		print("L'argument ne peut pas être vide")
```

**Exemple :**   
Nous pourrions également utiliser les valeurs truthy et falsy pour lever une exception (erreur) lorsque l'argument passé à une fonction n'est pas valide.

```python
>>> def print_even(data):

	if not data:
		raise ValueError("L'argument data ne peut pas être vide")

	for value in data:
		if value % 2 == 0:
			print(value)
```

Dans ce cas, en utilisant `not data` comme condition de l'instruction `if`, nous obtenons la valeur de vérité opposée de `data` pour la condition `if`.

Analysons `not data` plus en détail :

Si `data` est vide :

* Ce sera une valeur falsy, donc `data` évaluera à `False`.
* `not data` sera équivalent à `not False`, ce qui est `True`.
* La condition sera `True`.
* L'exception sera levée.

Si `data` n'est pas vide :

* Ce sera une valeur truthy, donc elle évaluera à `True`.
* `not data` sera équivalent à `not True`, ce qui est `False`.
* La condition sera `False`.
* L'exception ne sera pas levée.

## 🔸 Rendre les Objets Personnalisés Truthy et Falsy

Si vous êtes familier avec les classes et la programmation orientée objet, vous pouvez ajouter une méthode spéciale à vos classes pour faire en sorte que vos objets se comportent comme des valeurs truthy et falsy.

### __bool__()

Avec la méthode spéciale `__bool__()`, vous pouvez définir une condition "personnalisée" qui déterminera quand un objet de votre classe évaluera à `True` ou `False`.

Selon la [Documentation Python](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) :

> Par défaut, un objet est considéré comme vrai sauf si sa classe définit soit une méthode [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__) qui retourne `False` soit une méthode [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__) qui retourne zéro, lorsqu'elle est appelée avec l'objet.

Par exemple, si nous avons cette classe très simple :

```python
>>> class Account:
	
	def __init__(self, balance):
		self.balance = balance
```

Vous pouvez voir qu'aucune méthode spéciale n'est définie, donc tous les objets que vous créez à partir de cette classe évalueront toujours à `True` :

```python
>>> account1 = Account(500)
>>> bool(account1)
True
>>> account2 = Account(0)
>>> bool(account2)
True
```

Nous pouvons personnaliser ce comportement en ajoutant la méthode spéciale [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__) :

```python
>>> class Account:
	def __init__(self, balance):
		self.balance = balance
		
	def __bool__(self):
		return self.balance > 0
```

Maintenant, si le solde du compte est supérieur à zéro, l'objet évaluera à `True`. Sinon, si le solde du compte est zéro, l'objet évaluera à `False`.

```python
>>> account1 = Account(500)
>>> bool(account1)
True
>>> account2 = Account(0)
>>> bool(account2)
False
```

💡 **Astuce :** Si [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__) n'est pas définie dans la classe mais que la méthode `__len__()` l'est, la valeur retournée par cette méthode déterminera si l'objet est truthy ou falsy.

## 🔹 En Résumé

* Les valeurs truthy sont des valeurs qui évaluent à `True` dans un contexte booléen.
* Les valeurs falsy sont des valeurs qui évaluent à `False` dans un contexte booléen.
* Les valeurs falsy incluent les séquences vides (listes, tuples, chaînes de caractères, dictionnaires, ensembles), zéro dans chaque type numérique, `None`, et `False`.
* Les valeurs truthy incluent les séquences non vides, les nombres (sauf `0` dans chaque type numérique), et essentiellement chaque valeur qui n'est pas falsy.
* Elles peuvent être utilisées pour rendre votre code plus concis.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous pouvez travailler avec des valeurs truthy et falsy dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐️