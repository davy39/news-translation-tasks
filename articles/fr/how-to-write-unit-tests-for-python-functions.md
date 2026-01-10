---
title: Comment écrire des tests unitaires pour les fonctions Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2022-10-27T18:53:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-for-python-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-image-unit-tests-python.png
tags:
- name: Python
  slug: python
- name: unit testing
  slug: unit-testing
seo_title: Comment écrire des tests unitaires pour les fonctions Python
seo_desc: 'This guide will teach you how to write unit tests for Python functions.
  But why should you consider writing unit tests at all?

  Well, when working on a large project, you''ll often have to update certain modules
  and refactor code as needed. But such ch...'
---

Ce guide vous apprendra à écrire des tests unitaires pour les fonctions Python. Mais pourquoi devriez-vous envisager d'écrire des tests unitaires ?

Eh bien, lorsque vous travaillez sur un grand projet, vous devrez souvent mettre à jour certains modules et refactoriser le code selon les besoins. Mais de tels changements peuvent avoir des conséquences involontaires sur d'autres modules qui utilisent un module mis à jour. Cela peut parfois casser des fonctionnalités existantes.

En tant que développeur, vous devez tester votre code pour vous assurer que tous les modules de l'application fonctionnent comme prévu. Les tests unitaires vous permettent de vérifier si de petites unités de code isolées fonctionnent correctement et vous permettent de corriger les incohérences qui surviennent suite aux mises à jour et au refactoring.

Ce guide vous aidera à commencer avec les tests unitaires en Python. Vous apprendrez à utiliser le module intégré `unittest` de Python pour configurer et exécuter des tests unitaires et écrire des cas de test pour tester les fonctions Python. Vous apprendrez également à tester les fonctions qui lèvent des exceptions.

Commençons !

## Testing in Python – First Steps

Nous allons commencer par définir une [fonction Python](https://www.freecodecamp.org/news/functions-in-python-a-beginners-guide/) et écrire des tests unitaires pour vérifier si elle fonctionne comme prévu. Pour nous concentrer sur la configuration des tests unitaires, nous allons considérer une fonction simple `is_prime()`, qui prend un nombre et vérifie s'il est premier ou non.

```python
import math

def is_prime(num):
    '''Vérifie si num est premier ou non.'''
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

```

Démarrons un REPL Python, appelons la fonction `is_prime()` avec des arguments et vérifions les résultats.

```python
>>> from prime_number import is_prime
>>> is_prime(3)
True
>>> is_prime(5)
True
>>> is_prime(12)
False
>>> is_prime(8)
False
>>> assert is_prime(7) == True
```

Vous pouvez également utiliser l'instruction `assert` pour vérifier que `is_prime()` retourne la valeur booléenne attendue, comme montré ci-dessus. Si la valeur de retour de la fonction est différente de la valeur booléenne attendue, une `AssertionError` est levée.

Ce type de **test manuel** est _inefficace_ lorsque vous souhaitez vérifier de manière exhaustive votre fonction pour une liste beaucoup plus grande d'arguments. Vous pouvez vouloir configurer des tests automatisés qui s'exécutent et valident la sortie de la fonction par rapport aux cas de test définis dans la suite de tests.

## How to Use Python's `unittest` Module

Python est livré avec le module `unittest` qui vous permet de configurer des tests automatisés pour les fonctions et les classes de votre application. La procédure générique pour configurer des tests unitaires en Python est la suivante :

```python
# <module-name>.py

import unittest
from <module> import <function_to_test>
# toutes les entrées dans <> sont des espaces réservés

class TestClass(unittest.TestCase):
	def test_<name_1>(self):
		# vérifier function_to_test

	def test_<name_2>(self):
		# vérifier function_to_test
	:
	:
	:

	def test_<name_n>(self):
		# vérifier function_to_test

```

Le fragment de code ci-dessus `<module-name>.py` fait ce qui suit :

* Importe le module intégré `unittest` de Python.
* Importe la fonction Python à tester, `<function_to_test>` depuis le module dans lequel elle est définie, `<module>`.
* Crée une classe de test (`TestClass`) qui hérite de la classe `unittest.TestCase`.
* Chacun des tests à exécuter doit être défini comme des méthodes à l'intérieur de la classe de test.
* 💡 **Note** : Pour que le module `unittest` identifie ces méthodes comme des tests et les exécute, les noms de ces méthodes doivent commencer par `test_`.
* La classe `TestCase` dans le module `unittest` fournit des méthodes d'assertion utiles pour vérifier si la fonction sous test retourne les valeurs attendues.

Les méthodes d'assertion les plus courantes sont listées ci-dessous, et nous en utiliserons certaines dans ce tutoriel.

|Méthode| Description|
|-------|-----------|
|`assertEqual(expected_value,actual_value)`|Assert que `expected_value == actual_value`|
|`assertTrue(result)`|Assert que `bool(result)` est `True`|
|`assertFalse(result)`|Assert que `bool(result)` est `False`|
|`assertRaises(exception, function, *args, **kwargs)`|Assert que `function(*args, **kwargs)` lève l'`exception`|

📝 Pour une liste complète des méthodes d'assertion, consultez la [documentation unittest](https://docs.python.org/3/library/unittest.html).

Pour exécuter ces tests, nous devons exécuter unittest comme module principal, en utilisant la commande suivante :

```bash
$ python -m unittest <module-name>.py
```

Nous pouvons ajouter la condition `if __name__=='__main__'` pour exécuter `unittest` comme module principal.

```python
if __name__=='__main__':
	unittest.main()
```

L'ajout de la condition ci-dessus nous permettra d'exécuter les tests en exécutant directement le module Python contenant les tests.

```bash
$ python <module-name>.py
```

## How to Define Test Cases for Python Functions

![Image](https://www.freecodecamp.org/news/content/images/2022/10/unittesting-101.png)

Dans cette section, nous allons écrire des tests unitaires pour la fonction `is_prime()` en utilisant la syntaxe que nous avons apprise.

Pour tester la fonction `is_prime()` qui retourne un booléen, nous pouvons utiliser les méthodes `assertTrue()` et `assertFalse()`. Nous définissons quatre méthodes de test dans la classe `TestPrime` qui hérite de `unittest.TestCase`.

```python
import unittest
# importer la fonction is_prime
from prime_number import is_prime
class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertTrue(is_prime(2))
    def test_five(self):
    	self.assertTrue(is_prime(5))
    def test_nine(self):
    	self.assertFalse(is_prime(9))
    def test_eleven(self):
    	self.assertTrue(is_prime(11))
if __name__=='__main__':
	unittest.main()
```

```bash
$ python test_prime.py
```

Dans la sortie ci-dessous, '.' indique un test réussi.

```
Output
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
```

Dans le code ci-dessus, il y a quatre méthodes de test, chacune vérifiant une entrée spécifique. Vous pouvez plutôt définir une seule méthode de test qui assert si la sortie est correcte, pour les quatre entrées.

```python
import unittest
from prime_number import is_prime
class TestPrime(unittest.TestCase):
	def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
```

Après avoir exécuté le module `test_prime`, nous voyons qu'un test a été exécuté avec succès. Si l'une des méthodes assert lève une `AssertionError`, alors le test échoue.

```bash
$ python test_prime.py
```

```
Output
.
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK
```

## How to Write Unit Tests to Check for Exceptions

Dans la section précédente, nous avons testé la fonction `is_prime()` avec des nombres premiers et non premiers comme entrées. Plus précisément, les entrées étaient toutes des entiers positifs.

Nous n'avons pas encore imposé que les arguments dans l'appel de fonction à `is_prime()` doivent être des entiers positifs. Vous pouvez utiliser des indications de type pour imposer des types ou lever des exceptions pour des entrées invalides.

En testant la fonction `is_prime()`, nous n'avons pas tenu compte des éléments suivants :

* Pour un argument de type flottant, la fonction `is_prime()` s'exécuterait toujours et retournerait `True` ou `False`, ce qui est incorrect.
* Pour des arguments d'autres types, par exemple, la chaîne 'five' au lieu du nombre 5, la fonction lève une **TypeError.**
* Si l'argument est un entier négatif, alors la fonction `math.sqrt()` lève une **ValueError**. Les carrés de tous les nombres réels (positifs, négatifs ou zéro) sont toujours non négatifs. Donc la racine carrée est définie uniquement pour les nombres non négatifs.

Vérifions ce qui précède en exécutant quelques exemples dans un REPL Python.

```python
>>> from prime_number import is_prime

>>> is_prime('five')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/home/bala/unit-test-1/prime_number.py", line 5, in is_prime
for i in range(2,int(math.sqrt(num))+1):
TypeError: must be real number, not str

>>> is_prime(-10)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/home/bala/unit-test-1/prime_number.py", line 5, in is_prime
for i in range(2,int(math.sqrt(num))+1):
ValueError: math domain error

>>> is_prime(2.5)
True
```

### How to Raise Exceptions for Invalid Inputs

Pour traiter les cas ci-dessus, nous allons valider la valeur utilisée dans l'appel de fonction pour `num` et lever des exceptions si nécessaire.

* Vérifiez si `num` est un entier. Si oui, passez à la vérification suivante. Sinon, levez une exception `TypeError`.
* Vérifiez si `num` est un entier négatif. Si oui, levez une exception `ValueError`.

En modifiant la définition de la fonction pour valider l'entrée et lever des exceptions, nous avons :

```python
import math
def is_prime(num):
    '''Vérifie si num est premier ou non.'''
    # lever TypeError pour un type d'entrée invalide
    if type(num) != int:
        raise TypeError('num est de type invalide')
    # lever ValueError pour une valeur d'entrée invalide
    if num < 0:
        raise ValueError('Vérifiez la valeur de num ; est-ce que num est un entier non négatif ?')
    # pour une entrée valide, procédez à la vérification si num est premier
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
        return False
    return True
```

Maintenant que nous avons modifié la fonction pour lever ValueError et TypeError pour les entrées invalides, l'étape suivante consiste à tester si ces exceptions sont levées.

## How to Use the `assertRaises()` Method to Test Exceptions

![Image](https://www.freecodecamp.org/news/content/images/2022/10/test-exceptions.png)

Dans la définition de la classe `TestPrime`, ajoutons des méthodes pour vérifier si les exceptions sont levées.

Nous définissons les méthodes `test_typeerror_1()` et `test_typeerror_2()` pour vérifier si l'exception `TypeError` est levée et la méthode `test_valueerror()` pour vérifier si l'exception `ValueError` est levée.

📍 Pour appeler la méthode `assertRaises()`, nous pouvons utiliser la syntaxe générale suivante :

```python
def test_exception(self):
    self.assertRaises(exception-name,function-name,args)
```

Nous pouvons également utiliser la syntaxe suivante en utilisant le gestionnaire de contexte (nous utiliserons cette syntaxe dans cet exemple) :

```python
def test_exception(self):
    with self.assertRaises(exception-name):
        function-name(args)
```

En ajoutant les méthodes de test pour vérifier les exceptions, nous avons :

```python
import unittest
from prime_number import is_prime
class TestPrime(unittest.TestCase):
    def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
        	is_prime(6.5)
    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
        	is_prime('five')
    def test_valueerror(self):
        with self.assertRaises(ValueError):
        	is_prime(-4)
            
if __name__=='__main__':
	unittest.main()
```

Exécutons le module `test_prime` et observons la sortie :

```bash
$ python test_prime.py
```

```
Output
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s
OK
```

Dans les exemples que nous avons codés jusqu'à présent, tous les tests ont réussi. Modifions l'une des méthodes, par exemple, `test_typeerror_2()`, comme suit :

```python
def test_typeerror_2(self):
    with self.assertRaises(TypeError):
    	is_prime(5)
```

Nous appelons la fonction `is_prime()` avec le nombre 5 comme argument. Ici, 5 est une entrée valide pour laquelle la fonction retourne `True`. Par conséquent, la fonction ne lève pas de `TypeError`. Lorsque nous exécutons les tests à nouveau, nous verrons qu'il y a un test qui échoue.

```bash
$ python test_prime.py
```

```
Output

..F.
======================================================================
FAIL: test_typeerror_2 (__main__.TestPrime)
----------------------------------------------------------------------
Traceback (most recent call last):
File "test_prime.py", line 17, in test_typeerror_2
is_prime(5)
AssertionError: TypeError not raised
----------------------------------------------------------------------
Ran 4 tests in 0.003s
FAILED (failures=1)
```

## Conclusion

Merci d'avoir lu jusqu'ici ! 😄 J'espère que ce tutoriel vous a aidé à comprendre les bases des tests unitaires en Python.

Vous avez appris à configurer des tests qui vérifient si une fonction fonctionne comme prévu ou lève une exception—tout cela en utilisant le module intégré `unittest` de Python.

Continuez à coder, et à la prochaine dans le prochain tutoriel ! 👩🏽‍💻