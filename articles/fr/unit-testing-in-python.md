---
title: Comment écrire des tests unitaires en Python – avec exemple de code de test
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2024-06-10T16:33:04.000Z'
originalURL: https://freecodecamp.org/news/unit-testing-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/WhatsApp-Image-2024-06-10-at-10.46.58-AM.jpeg
tags:
- name: Python
  slug: python
- name: unit testing
  slug: unit-testing
seo_title: Comment écrire des tests unitaires en Python – avec exemple de code de
  test
seo_desc: 'Unit testing is a software testing technique in which individual components
  or units of a software application are tested independently from the rest of the
  application.

  In software development, it''s beneficial to break your application into small,
  i...'
---

Les tests unitaires sont une technique de test logiciel dans laquelle les composants individuels ou unités d'une application logicielle sont testés indépendamment du reste de l'application.

En développement logiciel, il est bénéfique de diviser votre application en petites unités isolées. Cette approche vous permet d'écrire des tests indépendants pour vérifier toutes les parties de votre application, garantissant qu'elles se comportent comme prévu. De plus, si un test échoue, vous pouvez facilement isoler et dépanner la partie du code qui contient le bug sans toucher au reste de votre application.

Python fournit un support intégré pour les tests unitaires via le framework de test [unittest](https://docs.python.org/3/library/unittest.html). Il existe également d'autres frameworks de test tiers que vous pouvez utiliser pour vos tests unitaires, tels que [pytest](https://docs.pytest.org/en/7.1.x/contents.html).

Cet article se concentre sur l'utilisation du framework `unittest` pour écrire des tests pour vos applications Python et pourquoi les développeurs le préfèrent souvent.

Pour tirer le meilleur parti de cet article, vous devez avoir une compréhension de base du langage de programmation Python.

## Pourquoi les développeurs préfèrent-ils utiliser unittest ?

Bien qu'il existe de nombreux frameworks pour les tests unitaires dans l'écosystème Python, de nombreux développeurs préfèrent toujours le `unittest` intégré en raison de ses avantages convaincants.

Premièrement, le module `unittest` fait partie de la bibliothèque standard de Python. Cela garantit une disponibilité immédiate et une compatibilité entre divers environnements sans dépendances supplémentaires. L'intégration transparente avec divers environnements le rend pratique pour les développeurs d'utiliser `unittest` sans installer de packages supplémentaires.

Deuxièmement, en tant que framework de longue date au sein de l'écosystème Python, `unittest` bénéficie de la familiarité et de la longévité. De nombreux développeurs sont déjà habitués à son API et à sa structure, ce qui en fait un choix fiable pour les tests.

Troisièmement, la plupart des environnements de développement intégrés (IDE) tels que PyCharm offrent un support intégré pour `unittest`. Cela améliore la productivité des développeurs et rationalise le processus de test, permettant une gestion et une exécution des tests plus faciles.

Quatrièmement, le framework dispose d'une documentation complète et bien entretenue. Cela fournit des conseils détaillés et des exemples, aidant les développeurs à utiliser efficacement `unittest` pour leurs besoins de test.

Enfin, de nombreux projets Python existants utilisent `unittest` pour les tests, garantissant la compatibilité avec les bases de code héritées. Cette adoption généralisée permet aux développeurs de maintenir et d'étendre des projets plus anciens sans avoir besoin d'introduire et de s'adapter à un nouveau framework de test.

## Comment écrire des tests unitaires avec unittest

Les tests unitaires avec `unittest` impliquent la création de cas de test pour vérifier la fonctionnalité des unités individuelles de votre code. Chaque cas de test est défini en sous-classant `unittest.TestCase`. Cela vous permet d'hériter des plusieurs méthodes fournies par la classe [TestCase](https://docs.python.org/3/library/unittest.html#test-cases).

Certaines des méthodes fournies par la classe `TestCase` sont des méthodes d'assertion. Ces méthodes d'assertion vous permettent de vérifier si le résultat réel d'une fonction ou d'une opération correspond au résultat attendu, ou si certaines conditions sont remplies. Si une assertion échoue, le test est marqué comme échoué et vous recevrez un message d'erreur.

Voir [Classes et fonctions](https://docs.python.org/3/library/unittest.html#classes-and-functions) pour des informations détaillées sur les différentes méthodes fournies par la classe `TestCase`.

Maintenant, utilisons deux des méthodes d'assertion pour écrire des tests pour un programme de calculatrice simple. Tout d'abord, créez un nouveau dossier (répertoire), nommé `unit-testing`. Ensuite, créez un fichier nommé `calculator.py` dans votre dossier `unit-testing`. Maintenant, copiez le code suivant dans votre fichier `calculator.py` :

```python
def add(x, y):
    """additionne les nombres"""
    return x + y

def subtract(x, y):
    """soustrait les nombres"""
    return x - y

def divide(x, y):
    """divise les nombres"""
    return x / y

def multiply(x, y):
    """multiplie les nombres"""
    return x * y
```

Remarquez que, au lieu d'avoir votre programme de calculatrice dans une seule fonction, nous l'avons divisé en quatre fonctions indépendantes (unités). Cela permet de tester chaque partie du programme indépendamment. Ainsi, si l'une des unités donne une erreur lors des tests, vous pouvez facilement identifier cette unité et la dépanner sans toucher aux autres parties de votre programme.

Comme mentionné précédemment, les tests avec `unittest` impliquent la création d'une sous-classe de la classe `unittest.TestCase`, puis la définition de méthodes au sein de la sous-classe pour tester les unités individuelles de votre programme.

Pour montrer comment cela fonctionne, écrivons un test pour la fonction `add` de votre programme de calculatrice. Dans votre dossier `unit-testing`, créez un nouveau fichier nommé `test_calculator.py` et copiez le code suivant :

```python
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
```

Dans les lignes une et deux de votre code, vous avez importé les modules `unittest` et `calculator`. Vous avez ensuite créé une classe `TestCalculator`, qui hérite de la classe `TestCase`.

Dans la ligne cinq de votre code, vous avez défini une méthode `test_add` dans votre classe. La méthode, comme toutes les méthodes d'instance en Python, prend `self` comme premier argument. Puisque `self` est une référence de la classe `TestCalculator`, il peut accéder à la méthode `assertEqual` fournie par la classe `TestCase`, dont `TestCalculator` hérite.

La méthode `assertEqual` vérifie si deux valeurs sont égales. Elle a la syntaxe suivante :

```python
self.assertEqual(first, second, msg=None)
```

Dans la syntaxe précédente, `first` représente la valeur que vous souhaitez tester par rapport à la valeur `second`. `msg` est facultatif et représente un message personnalisé que vous recevrez si l'assertion échoue. Si vous ne fournissez pas de valeur pour `msg`, vous recevrez un message par défaut.

Maintenant, utilisons l'explication de la syntaxe pour expliquer l'utilisation de `assertEqual` dans votre méthode `test_add`. Dans votre première assertion, `self.assertEqual(add(1, 2), 3)` vérifie si le résultat de `add(1, 2)` est égal à 3. Si la fonction retourne 3, le test passe. Sinon, il échoue et affiche un message indiquant la non-correspondance. Cette explication est la même pour le reste de vos assertions.

De plus, remarquez que vous avez testé uniquement des valeurs représentatives dans votre méthode `test_add`. Cela garantit que votre test couvre une large gamme de valeurs d'entrée possibles sans code redondant. Voici une ventilation des valeurs représentatives dans votre méthode `test_add` :

* L'addition de deux nombres positifs (`self.assertEqual(calculator.add(1, 2), 3)`).
  
* L'addition d'un nombre négatif et d'un nombre positif (`self.assertEqual(calculator.add(-1, 1), 0)`).
  
* L'addition de deux nombres négatifs (`self.assertEqual(calculator.add(-1, -1), -2)`).
  
* L'addition de deux zéros (`self.assertEqual(calculator.add(0, 0), 0)`).
  
Maintenant, pour exécuter votre test, naviguez vers le répertoire `unit-testing` dans votre terminal et exécutez la commande suivante :

```bash
python -m unittest test_calculator.py
```

L'exécution de la commande précédente vous donnera le message suivant dans votre terminal :

```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

La sortie indique que vous avez exécuté un seul test et qu'il a réussi.

Pour vous assurer que votre test fonctionne comme prévu, retournez à votre fichier `calculator.py` et changez l'opérateur d'addition (`+`) dans votre fonction `add` en soustraction (`-`), comme ceci :

```python
def add(x, y):
    """additionne les nombres"""
    return x - y
```

Une fois les modifications effectuées, l'exécution de votre test à nouveau lèvera une `AssertionError` montrant que votre test a échoué :

```bash
Traceback (most recent call last):
  File ".../test_calculator.py", line 6, in test_add
    self.assertEqual(calculator.add(1, 2), 3)
AssertionError: -1 != 3

----------------------------------------------------------------------
Ran 1 test in 0.000s
```

Vous vous demandez peut-être pourquoi vous devez inclure le module `unittest` dans votre commande au lieu d'exécuter `python test_calculator.py`. C'est parce que vous n'avez pas encore rendu votre fichier `test_calculator.py` exécutable en tant que script autonome. Ainsi, l'exécution de `python test_calculator.py` ne vous donnera aucune sortie.

Pour rendre votre `test_calculator.py` exécutable en tant que script autonome, vous devez ajouter ce qui suit à la fin de votre fichier `test_calculator.py` :

```python
if __name__ == "__main__":
    unittest.main()
```

De plus, le module `unittest` exige que vous commenciez le nom de vos méthodes de test par le mot `test`, sinon, votre test ne s'exécutera pas comme prévu.

Pour essayer cela, changez le nom de votre méthode `test_add` en `add_test` comme ceci :

```python
class TestCalculator(unittest.TestCase):
    def add_test(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
```

Maintenant, si vous exécutez la commande `python test_calculator.py`, vous obtiendrez un message similaire à ceci :

```bash
----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```

Remarquez que la sortie précédente montre que zéro test a été exécuté. Maintenant, changez le nom de votre méthode en `test_add`. De plus, changez l'opérateur dans la fonction `add` de votre `calculator.py` en addition (`+`). Maintenant, réexécutez le test avec la commande `python test_calculator.py` et comparez votre sortie à la sortie précédente.

Il est courant pour les développeurs de gérer les entrées invalides en levant des exceptions. Il est donc important d'écrire des tests qui vérifient ces exceptions.

Par exemple, Python lèvera une `ZeroDivisionError` si vous essayez de diviser un nombre par zéro. Vous pouvez utiliser le module `unittest` pour tester de telles erreurs.

Maintenant, modifiez votre fichier `test_calculator.py` pour inclure une méthode de test pour votre fonction `divide` :

```python
import unittest
import calculator

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(-6, 2), -3)
        self.assertEqual(calculator.divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

Dans le code précédent, votre nouvelle méthode `test_divide` teste des valeurs représentatives comme votre méthode `test_add`. Mais il y a un nouveau code à la fin qui utilise `assertRaises`. `assertRaises` est une autre méthode d'assertion fournie par `unittest` pour vérifier si votre code lève une exception. Ici, vous avez utilisé la méthode pour vérifier `ZeroDivisionError`.

Ainsi, si vous exécutez les tests maintenant, vous obtiendrez un message montrant deux points (`..`) et indiquant que vous avez exécuté deux tests réussis :

```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Conclusion

Cet article vous a appris les bases des tests unitaires en Python en utilisant le framework de test `unittest`.

Vous avez appris l'importance de tester indépendamment les unités individuelles de votre application et les raisons pour lesquelles `unittest` est encore un choix populaire parmi les développeurs Python. De plus, vous avez appris à écrire des cas de test de base pour les fonctions `add` et `divide` de votre programme de calculatrice simple.

Avec cette connaissance, vous pouvez maintenant créer en toute confiance des tests qui garantissent que votre code se comporte comme prévu, le rendant ainsi plus robuste et maintenable. Je vous encourage à appliquer ces leçons en écrivant des tests pour les fonctions restantes `subtract` et `multiply` de votre programme de calculatrice.