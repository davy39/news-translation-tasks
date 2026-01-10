---
title: Une introduction simple au développement piloté par les tests avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-18T22:36:57.000Z'
originalURL: https://freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ak94Xh5LGvl2TgtnXPQQhQ.jpeg
tags:
- name: coding
  slug: coding
- name: Python
  slug: python
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Une introduction simple au développement piloté par les tests avec Python
seo_desc: 'By Dmitry Rastorguev

  I am a self-taught beginning developer who is able to write simple apps. But I have
  a confession to make. It’s impossible to remember how everything is interconnected
  in my head.

  This situation is made worse if I come back to the...'
---

Par Dmitry Rastorguev

Je suis un développeur débutant autodidacte capable d'écrire des applications simples. Mais j'ai une confession à faire. Il est impossible de me souvenir comment tout est interconnecté dans ma tête.

Cette situation est aggravée si je reviens au code que j'ai écrit après quelques jours. Il s'avère que ce problème pourrait être surmonté en suivant une méthodologie de [Développement Piloté par les Tests](https://en.wikipedia.org/wiki/Test-driven_development) (TDD).

### Qu'est-ce que le TDD et pourquoi est-il important ?

En termes simples, le TDD recommande d'écrire des tests qui vérifieraient la fonctionnalité de votre code avant d'écrire le code réel. Ce n'est que lorsque vous êtes satisfait de vos tests et des fonctionnalités qu'ils testent que vous commencez à écrire le code réel afin de satisfaire les conditions imposées par le test qui permettraient de les réussir.

Suivre ce processus garantit que vous planifiez soigneusement le code que vous écrivez afin de passer ces tests. Cela empêche également la possibilité de reporter l'écriture des tests à une date ultérieure, car ils pourraient ne pas être jugés aussi nécessaires que des fonctionnalités supplémentaires qui pourraient être créées pendant ce temps.

Les tests vous donnent également confiance lorsque vous commencez à refactoriser le code, car vous êtes plus susceptible de détecter des bugs grâce au retour instantané lorsque les tests sont exécutés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZGakHQbCUMAyDinf-KBiw.png)
_Flux de travail général du TDD_

### Comment commencer ?

Pour commencer à écrire des tests en Python, nous utiliserons le module `unittest` qui est inclus avec Python. Pour ce faire, nous créons un nouveau fichier `mytests.py`, qui contiendra tous nos tests.

Commençons par le classique "hello world" :

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
```

Remarquez que nous importons la fonction `helloworld()` depuis le fichier `mycode`. Dans le fichier `mycode.py`, nous inclurons initialement uniquement le code ci-dessous, qui crée la fonction mais ne retourne rien à ce stade :

```py
def hello_world():
    pass
```

L'exécution de `python mytests.py` générera la sortie suivante dans la ligne de commande :

```
F

====================================================================

FAIL: test_hello (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 7, in test_hello

self.assertEqual(hello_world(), 'hello world')

AssertionError: None != 'hello world'

--------------------------------------------------------------------

Ran 1 test in 0.000s

FAILED (failures=1)
```

Cela indique clairement que le test a échoué, ce qui était attendu. Heureusement, nous avons déjà écrit les tests, donc nous savons qu'ils seront toujours là pour vérifier cette fonction, ce qui nous donne confiance dans la détection de bugs potentiels à l'avenir.

Pour garantir que le code passe, modifions `mycode.py` comme suit :

```py
def hello_world():
    return 'hello world'
```

En exécutant à nouveau `python mytests.py`, nous obtenons la sortie suivante dans la ligne de commande :

```
.

--------------------------------------------------------------------

Ran 1 test in 0.000s

OK
```

Félicitations ! Vous venez d'écrire votre premier test. Passons maintenant à un défi légèrement plus difficile. Nous allons créer une fonction qui nous permettra de créer une compréhension de liste numérique personnalisée en Python.

Commençons par écrire un test pour une fonction qui créerait une liste de longueur spécifique.

Dans le fichier `mytests.py`, ce serait une méthode `test_custom_num_list` :

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
    
    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)
```

Cela testerait que la fonction `create_num_list` retourne une liste de longueur 10. Créons la fonction `create_num_list` dans `mycode.py` :

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    pass
```

L'exécution de `python mytests.py` générera la sortie suivante dans la ligne de commande :

```
E.

====================================================================

ERROR: test_custom_num_list (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 14, in test_custom_num_list

self.assertEqual(len(create_num_list(10)), 10)

TypeError: object of type 'NoneType' has no len()

--------------------------------------------------------------------

Ran 2 tests in 0.000s

FAILED (errors=1)
```

Cela est attendu, alors modifions la fonction `create_num_list` dans `mytest.py` afin de passer le test :

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]
```

L'exécution de `python mytests.py` sur la ligne de commande démontre que le deuxième test a également réussi :

```
..

--------------------------------------------------------------------

Ran 2 tests in 0.000s

OK
```

Créons maintenant une fonction personnalisée qui transformerait chaque valeur dans la liste comme ceci : `const * ( X ) ^ power`. Commençons par écrire le test pour cela, en utilisant la méthode `test_custom_func_` qui prendrait la valeur 3 comme X, l'élèverait à la puissance de 3, et multiplierait par une constante de 2, résultant en la valeur 54 :

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)
```

Créons la fonction `custom_func_x` dans le fichier `mycode.py` :

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    pass
```

Comme prévu, nous obtenons un échec :

```
F..

====================================================================

FAIL: test_custom_func_x (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 17, in test_custom_func_x

self.assertEqual(custom_func_x(3,2,3), 54)

AssertionError: None != 54

--------------------------------------------------------------------

Ran 3 tests in 0.000s

FAILED (failures=1)
```

Mettons à jour la fonction `custom_func_x` pour passer le test, nous avons ce qui suit :

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power
```

En exécutant à nouveau les tests, nous obtenons un succès :

```
...

--------------------------------------------------------------------

Ran 3 tests in 0.000s

OK
```

Enfin, créons une nouvelle fonction qui incorporerait la fonction `custom_func_x` dans la compréhension de liste. Comme d'habitude, commençons par écrire le test. Notez que pour être certain, nous incluons deux cas différents :

```py
import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)

    def test_custom_non_lin_num_list(self):
        self.assertEqual(custom_non_lin_num_list(5,2,3)[2], 16)
        self.assertEqual(custom_non_lin_num_list(5,3,2)[4], 48)
```

Créons maintenant la fonction `custom_non_lin_num_list` dans `mycode.py` :

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power

def custom_non_lin_num_list(length, const, power):
    pass
```

Comme avant, nous obtenons un échec :

```
.E..

====================================================================

ERROR: test_custom_non_lin_num_list (__main__.MyFirstTests)

--------------------------------------------------------------------

Traceback (most recent call last):

File "mytests.py", line 20, in test_custom_non_lin_num_list

self.assertEqual(custom_non_lin_num_list(5,2,3)[2], 16)

TypeError: 'NoneType' object has no attribute '__getitem__'

--------------------------------------------------------------------

Ran 4 tests in 0.000s

FAILED (errors=1)
```

Afin de passer le test, mettons à jour le fichier `mycode.py` comme suit :

```py
def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power

def custom_non_lin_num_list(length, const, power):
    return [custom_func_x(x, const, power) for x in range(length)]
```

En exécutant les tests pour la dernière fois, nous réussissons tous !

```
....

--------------------------------------------------------------------

Ran 4 tests in 0.000s

OK
```

Félicitations ! Cela conclut cette introduction aux tests en Python. Assurez-vous de consulter les ressources ci-dessous pour plus d'informations sur les tests en général.

Le code est disponible ici sur [GitHub](https://github.com/drastorguev/python_testing).

### Ressources utiles pour approfondir vos connaissances !

#### Ressources Web

Voici des liens vers certaines des bibliothèques axées sur les tests en Python :

* [**25.3. unittest - Framework de tests unitaires - Documentation Python 2.7.14**](https://docs.python.org/2.7/library/unittest.html)
* [**pytest : vous aide à écrire de meilleurs programmes - Documentation pytest**](https://docs.pytest.org/en/latest/)
* [**Bienvenue dans Hypothesis ! - Documentation Hypothesis 3.45.2**](https://hypothesis.readthedocs.io/en/latest/)
* [**unittest2 1.1.0 : Index des paquets Python**](https://pypi.python.org/pypi/unittest2)

#### Vidéos YouTube

Si vous préférez ne pas lire, je recommande de regarder les vidéos suivantes sur YouTube.