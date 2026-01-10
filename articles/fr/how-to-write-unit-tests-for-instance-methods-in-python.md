---
title: Comment écrire des tests unitaires pour les méthodes d'instance en Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2023-01-31T00:13:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-for-instance-methods-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/instance-methods-python.png
tags:
- name: Python
  slug: python
- name: unit testing
  slug: unit-testing
seo_title: Comment écrire des tests unitaires pour les méthodes d'instance en Python
seo_desc: 'This tutorial will teach you how to write unit tests for instance methods
  in Python.

  In a previous tutorial, we covered how to write unit tests for Python functions.
  While unit testing for instance methods works similarly, you may have some challenge...'
---

Ce tutoriel vous apprendra à écrire des tests unitaires pour les méthodes d'instance en Python.

Dans un [tutoriel précédent](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/), nous avons couvert comment écrire des tests unitaires pour les fonctions Python. Bien que les tests unitaires pour les méthodes d'instance fonctionnent de manière similaire, vous pourriez rencontrer des défis lors de la création et de la gestion d'objets (instances d'une classe). 

Ce tutoriel vous apprendra à utiliser de telles méthodes pour configurer et libérer des ressources efficacement. 

Commençons !

## Classes et Objets en Python – Un Rapide Rappel

Si vous êtes familier avec la programmation orientée objet, vous savez que les classes vous permettent de regrouper des **données** et des **comportements** liés. Vous pouvez ensuite utiliser ces classes comme modèles pour créer des instances de la classe. Si une classe Python est un emporte-pièce, alors chaque instance est un cookie. 🍪

Les données et les comportements sont décrits par les **attributs** et les **méthodes** dans la définition de la classe, respectivement. Nous allons examiner un exemple pour mieux comprendre ces concepts.

Je sais que cette section aurait dû s'appeler classes et objets expliqués pour les impatients. 🙂 Pour rafraîchir vos compétences en POO Python, vous pouvez consulter [ce cours](https://www.youtube.com/watch?v=Ej_02ICOIgs) sur la chaîne YouTube de freeCodeCamp.

%[https://www.youtube.com/watch?v=Ej_02ICOIgs]

## Comment Tester les Méthodes d'Instance d'une Classe Python

Maintenant, nous allons apprendre à configurer des tests unitaires pour les instances de classes Python. Nous allons écrire des tests unitaires pour vérifier la fonctionnalité de la classe `Book` présentée ci-dessous :

```python
class Book:
    def __init__(self,title,author,pages,price,discount):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.discount = discount
    def get_reading_time(self):
        return f"{self.pages*1.5} minutes"
    def apply_discount(self):
        discounted_price = self.price - (self.discount*self.price)
        return f"${discounted_price}"
```

La classe `Book` sert de modèle ou de plan avec les attributs : titre, auteur, pages, prix et remise. `get_reading_time()` et `apply_discount()` sont les méthodes d'instance qui utilisent les attributs ci-dessus. 

Ainsi, nous pouvons créer des objets livre à partir de la classe `Book`, chacun avec leurs propres attributs.

![Image](https://lh6.googleusercontent.com/JRAfU2HbOIqGFPPEqBi1Wj0Uttbn_TBLgnl0CqnGaqonBaa2KYpBmcJu2aXywtT9eoFJb3H5q4AD8r3ce8oB8sTKX1Y9qkjIiCT4f0A5HHFblsZjtUiPF0kyTLDooVpQnH8HKtX-6joRG7JJTWm-L9Ss-nFBtOxQjHN8Y7LqCtNoR-jMl7rQrAPJ6g)
_Illustration de la classe livre et des objets livre_

Pour tester les méthodes d'instance `get_reading_time()` et `apply_discount()`, nous pouvons créer deux instances de la classe `Book` à l'intérieur des méthodes de test. Nous pouvons utiliser la méthode d'assertion `assertEqual()` pour vérifier si les valeurs de retour des méthodes d'instance sont correctes.

```python
from book import Book
import unittest

class TestBook(unittest.TestCase):
    def test_reading_time(self):
        book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
        self.assertEqual(book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
        self.assertEqual(book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(book_2.apply_discount(),f"${16 - 16*0.15}" )
        
if __name__=='__main__':
	unittest.main()
```

## Comment Configurer et Libérer des Ressources Pendant les Tests Unitaires

Lors de la configuration de tests pour des méthodes d'instance, nous instancions deux objets livre, puis vérifions si les méthodes d'instance fonctionnent comme prévu. Et nous devons faire cela pour chacune des méthodes.

Mais cela est répétitif et sous-optimal lorsque vous devez tester un grand nombre de méthodes d'instance. 

Dans ce cas, il sera plus pratique si nous pouvons définir une méthode qui instancie ces objets pour nous avant d'exécuter chaque test. C'est là que la méthode `setUp()` entre en jeu. 

### Comment les Méthodes `setUp()` et `tearDown()` Fonctionnent

Les méthodes `setUp()` et `tearDown()` sont typiquement utilisées pour les tâches complémentaires d'allocation et de désallocation de ressources, avant et après chaque test unitaire, respectivement. 

* La méthode `setUp()` s'exécute avant chaque test, et
* La méthode `tearDown()` s'exécute après chaque test.

Ici, nous pouvons utiliser la méthode `setUp()` pour instancier les objets livre. Parfois, vous devrez également utiliser la méthode `tearDown()`. 

Par exemple, si chaque test ajoute des fichiers à un répertoire ou crée plusieurs objets en mémoire, vous pourriez vouloir libérer le répertoire et supprimer les objets créés après chaque test. Nous allons ajouter la méthode `tearDown()` pour vérifier qu'elle s'exécute après chaque test.

Pour mieux comprendre cela, ajoutons des instructions `print()` explicatives, comme montré dans le code ci-dessous :

```python
from book import Book
import unittest
class TestBook(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        self.book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
    def tearDown(self):
        print("Running tearDown method...")
    def test_reading_time(self):
        print("Running test_reading_time...")
        self.assertEqual(self.book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(self.book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        print("Running test_discount...")
        self.assertEqual(self.book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(self.book_2.apply_discount(),f"${16 - 16*0.15}" )
if __name__=='__main__':
	unittest.main()
```

Maintenant, exécutez le module `test_book`. Voici le résultat :

```
Output
Running setUp method...
Running test_discount...
Running tearDown method...
.
Running setUp method...
Running test_reading_time...
Running tearDown method...
.
----------------------------------------------------------------------
Ran 2 tests in 0.003s
OK
```

## Comment Utiliser les Méthodes `setUpClass()` et `tearDownClass()`

En plus des méthodes ci-dessus, vous pouvez également utiliser les méthodes de classe : `setUpClass()` et `tearDownClass()`. 

En Python, les méthodes de classe se lient à une classe et non à une instance particulière. Pour définir une méthode comme une méthode de classe, vous pouvez utiliser le décorateur `@classmethod`. 

Alors, quand devrions-nous utiliser ces méthodes de classe ?

L'instanciation d'objets, comme dans l'exemple ci-dessus, est une tâche simple et non coûteuse en calcul. Mais vous pourriez parfois avoir des tâches trop coûteuses pour être effectuées avant chaque test : par exemple, démarrer une base de données en mémoire.

Si tous les tests suivants dans la classe de test ne font que lire certaines données de la base de données, nous pouvons utiliser la méthode de classe `setUpClass()` pour démarrer la base de données et la méthode de classe `tearDownClass()` pour arrêter la base de données après que tous les tests ont été exécutés.

En résumé :

* La méthode de classe `setUpClass()` est exécutée **avant** _tout_ test.
* La méthode de classe `tearDownClass()` est exécutée **après** _tous_ les tests.
* Les méthodes `setUp()` et `tearDown()` sont exécutées **avant** et **après** _chaque_ test, respectivement. 

Ajoutons les méthodes de classe `setUpClass()` et `tearDownClass()` à la classe `TestBook`. 

```python
from book import Book
import unittest
class TestBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        self.book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
    def tearDown(self):
        print("Running tearDown method...")
    def test_reading_time(self):
        print("Running test_reading_time...")
        self.assertEqual(self.book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(self.book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        print("Running test_discount...")
        self.assertEqual(self.book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(self.book_2.apply_discount(),f"${16 - 16*0.15}" )
    @classmethod
    def tearDownClass(cls):
    	print("\ntearDownClass method: Runs after all tests...")
        
if __name__=='__main__':
	unittest.main()
```

Maintenant, réexécutez `test_book.py`.

D'après la sortie ci-dessous, nous voyons que les méthodes `setUpClass()` et `tearDownClass()` s'exécutent avant et après tous les tests, respectivement.

```
Output
setUpClass method: Runs before all tests...
Running setUp method...
Running test_discount...
Running tearDown method...
.
Running setUp method...
Running test_reading_time...
Running tearDown method...
.
tearDownClass method: Runs after all tests...
----------------------------------------------------------------------
Ran 2 tests in 0.010s
OK
```

## Conclusion

J'espère que ce tutoriel vous a aidé à apprendre comment configurer des tests unitaires pour les méthodes d'instance en Python. 

Si vous êtes intéressé à en apprendre davantage sur la nécessité des tests unitaires avec un focus sur les fonctions Python, envisagez de lire l'article [Comment Écrire des Tests Unitaires pour les Fonctions Python](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/).

Bon codage !