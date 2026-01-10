---
title: 'Comment utiliser pytest : Un guide simple pour les tests en Python'
subtitle: ''
author: Olowo Jude
co_authors: []
series: null
date: '2025-07-08T20:42:29.803Z'
originalURL: https://freecodecamp.org/news/how-to-use-pytest-a-guide-to-testing-in-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752007334998/e196493e-f3e0-4e63-b6eb-ce66c5481d9c.png
tags:
- name: Python
  slug: python
- name: pytest
  slug: pytest
- name: Testing
  slug: testing
- name: TDD (Test-driven development)
  slug: tdd
- name: unit testing
  slug: unit-testing
- name: guide
  slug: guide
seo_title: 'Comment utiliser pytest : Un guide simple pour les tests en Python'
seo_desc: 'With the recent advancements in AI, tools like ChatGPT have made the development
  process faster and more accessible. Developers can now write code and build web
  apps with some well-articulated prompts and careful code reviews.

  While this brings an in...'
---

Avec les avancées récentes en IA, des outils comme ChatGPT ont rendu le processus de développement plus rapide et plus accessible. Les développeurs peuvent maintenant écrire du code et construire des applications web avec quelques invites bien articulées et des revues de code minutieuses.

Bien que cela augmente la productivité, il y a un inconvénient croissant. Le code généré par l'IA est sujet aux erreurs, aux bugs inattendus ou à une mauvaise intégration avec le reste de votre code.

En raison de ces risques, il est plus important que jamais d'établir des pratiques de test robustes pour s'assurer que votre code est de haute qualité et fonctionne correctement. Divers outils de test sont disponibles pour aider à résoudre ces défis, et pytest se distingue dans l'écosystème Python pour sa simplicité, sa flexibilité et ses fonctionnalités puissantes.

Dans cet article, nous explorerons les sujets suivants :

## Table des matières

* [Pourquoi utiliser pytest ?](#heading-pourquoi-utiliser-pytest)
    
* [Comment écrire vos premiers tests avec pytest](#heading-comment-écrire-vos-premiers-tests-avec-pytest)
    
* [Comment exécuter les tests pytest](#heading-comment-exécuter-les-tests-pytest)
    
* [Comment interpréter les résultats de pytest](#heading-comment-interpréter-les-résultats-de-pytest)
    
* [Comment gérer les exceptions dans pytest](#heading-comment-gérer-les-exceptions-dans-pytest)
    
* [Fonctionnalités avancées de pytest](#heading-fonctionnalités-avancées-de-pytest)
    
    * [1. Marqueurs pytest](#heading-1-marqueurs-pytest)
        
    * [2. Fixtures pytest](#heading-2-fixtures-pytest)
        
    * [3. Paramétrisation](#heading-3-paramétrisation)
        
    * [4. Plugins pytest](#heading-4-plugins-pytest)
        
* [Conclusion](#heading-conclusion)
    

À la fin de cet article, vous aurez une connaissance approfondie de pytest et serez en mesure de l'utiliser dans votre processus de développement Python.

## **Prérequis**

* Avoir Python installé
    
* Une compréhension du langage de programmation Python
    

## Pourquoi utiliser pytest ?

![Une image du logo pytest.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751221734601/f5d6093a-37d2-4d49-85f2-c1a41a98ab67.png align="center")

pytest est un framework de test populaire pour Python qui facilite l'écriture et l'exécution de tests. Contrairement à unittest et à d'autres frameworks de test Python, la syntaxe simple de pytest permet aux développeurs d'écrire des tests directement sous forme de fonctions ou dans des classes. Cela vous permet d'écrire un code propre et lisible sans complexités.

pytest supporte également des frameworks Python populaires comme Flask, Django, et bien d'autres. Combiné à d'autres fonctionnalités riches, pytest vous équipe des outils nécessaires pour livrer des logiciels fiables à l'ère actuelle de l'IA.

Les fonctionnalités clés de pytest qui en font un outil de test préféré incluent :

* **Flexibilité :** il offre une flexibilité dans la structure des tests en supportant les tests pour les fonctions, les classes et les modules.
    
* **Sortie de test détaillée :** il fournit une sortie de test détaillée et lisible, facilitant la compréhension des échecs et des erreurs de test.
    
* **Découverte automatique des tests :** il découvre automatiquement les tests en recherchant les fichiers qui commencent par "`test_`" ou se terminent par "`_test.py`". Cela élimine le besoin de spécifier manuellement les fichiers de test.
    
* **Paramétrisation :** il supporte les tests paramétrés, qui permettent d'exécuter une seule fonction de test avec plusieurs ensembles d'entrées.
    
* **Fixtures :** les fixtures de pytest fournissent des méthodes `setup` et `tearDown` qui aident à prévenir la répétition de code. Cela vous permet de configurer des conditions de base pour vos tests et également de les supprimer après chaque test.
    
* **Plugins et extensions :** il dispose d'un riche écosystème de plugins et d'extensions qui ajoutent des fonctionnalités supplémentaires, telles que des rapports de tests détaillés, et une intégration avec d'autres outils et frameworks Python comme Django et Flask.
    
* **Compatibilité :** il est compatible avec d'autres frameworks de test comme `unittest`, permettant de migrer des tests de différents frameworks de test et de les exécuter de manière transparente.
    

## Comment écrire vos premiers tests avec pytest

Cette section vous guidera à travers l'écriture de votre premier ensemble de tests en utilisant le framework pytest.

pytest est un package Python, et vous devrez l'installer avant de l'utiliser. Vous pouvez le faire avec la commande suivante :

```python
pip install pytest
```

**NOTE :** Suivant les meilleures pratiques de Python, il est recommandé d'installer pytest dans un environnement virtuel. [Voici un guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) pour vous aider à le configurer.

Ensuite, créez un fichier Python où vous écrirez vos tests et importez pytest avec :

```python
import pytest
```

pytest propose 2 méthodes de base pour écrire des tests, qui incluent :

* **La méthode basée sur les fonctions :** Cette méthode est simple pour écrire des tests car vous écrivez les tests dans des fonctions individuelles.
    
    **Note :** Chaque nom de fonction doit être préfixé par le mot `test_` pour que pytest découvre et exécute automatiquement ces tests.
    
    Voici un exemple de test basé sur une fonction :
    
    ```python
    def test_addition():
        assert 1 + 1 == 2
    ```
    
    **Note :** Dans le code ci-dessus, l'instruction `assert` utilisée ici dans pytest est l'instruction "`assert`" intégrée de Python. Elle est plus pratique et ne nécessite pas les méthodes spécifiques comme `assertEqual` et `assertTrue` qui sont courantes avec unittest. Un autre avantage de l'utilisation de l'instruction `assert` est qu'elle fournit des messages d'erreur plus détaillés lorsqu'une assertion échoue.
    
* **Méthode basée sur les classes :** Cette méthode est similaire à la façon d'écrire des tests dans `unittest`, sauf que votre classe de test n'hérite d'aucune méthode. Un exemple est montré ci-dessous :
    
    ```python
    class TestMathOperations:
        def test_addition(self):
            assert 1 + 1 == 2
    ```
    
    Cette méthode d'écriture de tests dans pytest est utile lorsque vous souhaitez regrouper des tests liés ensemble.
    

## Comment exécuter les tests pytest

L'exécution de pytest diffère légèrement de la convention normale d'exécution des scripts Python réguliers.

La méthode générale d'exécution des tests pytest consiste à exécuter la commande `pytest` dans votre terminal. pytest recherchera et exécutera automatiquement tous les fichiers de la forme `test_*.py` ou `*_test.py` dans le répertoire courant et les sous-répertoires. Mais bien que cela puisse être un excellent moyen d'exécuter des tests, pytest offre plus de flexibilité au-delà de cette méthode générale d'exécution des tests.

Selon les préférences, vous pouvez souhaiter exécuter vos fichiers de test en fonction des éléments suivants :

1. **Pour exécuter un fichier de test spécifique :** Pour exécuter des tests dans un fichier spécifique, utilisez la commande `pytest` suivie du nom du fichier. Par exemple : `pytest test_example.py`.
    
2. **Pour exécuter des tests dans un répertoire :** Supposons que vous avez un répertoire nommé Tests qui contient certains fichiers de test. Pour exécuter tous les tests dans ce répertoire, utilisez la commande `pytest` suivie du répertoire et d'une barre oblique. Par exemple : `pytest Tests/`.
    
3. **Pour exécuter des tests en utilisant des mots-clés spécifiques :** Pour exécuter des tests en fonction d'un certain mot-clé, utilisez la commande `pytest -k "keyword"`. Pytest recherchera et exécutera automatiquement les noms de fonctions, les noms de classes ou les noms de fichiers correspondant à ce mot-clé dans le répertoire courant et les sous-répertoires. Mais pour exécuter des tests correspondant à un certain mot-clé dans un fichier spécifique, vous devrez spécifier le nom du fichier après la commande `pytest`. Par exemple : `pytest test_example.py -k "keyword"`.
    
4. **Exécuter un test spécifique dans un fichier de test :** Pour exécuter uniquement un test spécifique dans un fichier de test, utilisez la commande `pytest test_example.py::test_addition`. Cela exécutera uniquement la fonction de test `test_addition` dans le module `test_example.py`.
    
5. **Pour exécuter toutes les méthodes de test dans une classe spécifique :** Pour exécuter tous les tests dans une classe spécifique, utilisez `pytest test_example.py::TestClass`. Cette commande exécutera toutes les méthodes de test dans la classe `TestClass` dans le module `test_example.py`.
    
6. **Pour exécuter une méthode de test spécifique dans une classe spécifique :** Pour exécuter un test spécifique dans une classe spécifique, utilisez `pytest test_example.py::TestClass::test_addition`. Cette commande exécutera la méthode spécifique `test_addition` dans la classe `TestClass` dans le module `test_example.py`.
    

## Comment interpréter les résultats de pytest

Un avantage majeur de pytest par rapport à d'autres frameworks de test Python est la sortie riche qu'il fournit, qui donne des informations très détaillées sur l'état de vos tests.

Utilisons un test de base pour comprendre comment interpréter la sortie de pytest :

```python
import pytest

def test_addition():
    assert 1 + 1 == 3
```

Exécutez ce test, et nous obtenons une sortie similaire à celle ci-dessous :

```python
============================== test session starts ====================================
platform win32 -- Python 3.10.5, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\\Users\\hp\\Desktop\\Pytest
collected 1 items

                                                                                  [ 50%]
test_example.py F                                                                 [100%]

===================================== FAILURES =========================================
____________________________________test_addition ______________________________________

    def test_addition():
>       assert 1 + 1 == 3
E       assert (1 + 1) == 3

test_example.py:4: AssertionError
============================== short test summary info =================================
FAILED test_example.py::test_addition - assert (1 + 1) == 3
========================= 1 failed, 1 passed in 0.13s ==================================
```

La sortie ci-dessus est divisée en plusieurs sections. Voici une explication de ce que signifie chaque section :

1. Informations sur la session de test :
    
    ```python
    =============================== test session starts ===============================
    platform win32 -- Python 3.10.5, pytest-8.4.1, pluggy-1.6.0
    rootdir: C:\\Users\\hp\\Desktop\\TDD pytest
    collected 1 item
    ```
    
    * Cette section affiche un résumé de l'environnement de test. Elle commence par un marqueur de ligne qui indique le début de la session de test.
        
    * Sous le marqueur, pytest affiche des informations sur le système d'exploitation, ainsi que les versions installées de Python, pytest et pluggy. (Pluggy est une dépendance pytest utilisée pour gérer les plugins.)
        
    * La ligne suivante indique le répertoire racine où le test est exécuté.
        
    * La dernière ligne de cette section affiche le nombre de tests trouvés dans ce répertoire.
        
2. État du test :
    
    ```python
    test_example.py F                                                              [100%]
    
    ================================== FAILURES =========================================
    ________________________________ test_addition ______________________________________
    
        def test_addition():
    >       assert 1 + 1 == 3
    E       assert (1 + 1) == 3
    
    test_example.py:4: AssertionError
    ```
    
    * Cette section affiche des informations sur l'état de nos tests
        
    * La première ligne de cette section spécifie le fichier de test qui est exécuté, suivi de l'état (F dans ce cas, ce qui indique un échec de test).
        
    * Le prochain ensemble de lignes donne des informations spécifiques sur les tests échoués. Cela inclut la fonction où l'échec s'est produit (`test_addition`), et la ligne exacte de code responsable de l'erreur.
        
    * La dernière ligne donne un résumé concis de cette section. Elle indique que l'erreur s'est produite dans `test_example.py` à la ligne `4` et qu'il s'agissait d'une `AssertionError`.
        
3. Résumé du test :
    
    ```python
    ============================= short test summary info =============================
    FAILED test_example.py::test_addition - assert (1 + 1) == 3
    ================================ 1 failed in 0.13s ================================
    ```
    
    * Cette section fournit un résumé général du test.
        
    * Elle indique que le test échoué s'est produit dans le fichier `test_example.py` dans la fonction `test_addition` en raison d'une assertion incorrecte `(1 + 1) == 3` qui n'est pas vraie.
        

Modifiez le code avec l'assertion correcte `assert(1 + 1) == 2` et relancez le code. Cette fois, le code passe avec une sortie différente.

```python
=============================== test session starts ==================================
platform win32 -- Python 3.10.5, pytest-8.3.2, pluggy-1.5.0
rootdir: C:\\Users\\hp\\Desktop\\TDD pytest
collected 1 items

test_example.py .                                                               [100%]

=============================== 1 passed in 0.01s =================================
```

### Comment gérer les exceptions dans pytest

Les exceptions sont des erreurs inattendues qui se produisent lors de l'exécution de nos tests, et elles empêchent notre code de fonctionner comme prévu. En conséquence, pytest offre plusieurs mécanismes intégrés pour gérer ces exceptions (mais nous n'en couvrirons qu'un dans cet article).

Le **gestionnaire de contexte** `pytest.raises` est un outil qui vérifie si votre code lève des exceptions spécifiques. Si l'exception spécifiée est levée, ce test passe, confirmant que l'erreur attendue s'est produite. Mais si l'exception spécifiée n'est pas levée, ce test échoue.

**Exemples d'utilisation de** `pytest.raises`

1. **Vérification de** `ValueError` : En Python, une `ValueError` est levée lorsqu'une fonction reçoit un argument avec une valeur incorrecte. Dans l'exemple ci-dessous, nous pouvons vérifier qu'une `ValueError` est levée lors de la tentative de calcul de la racine carrée d'un nombre négatif.
    
    ```python
    import pytest
    import math
    
    def calculate_square_root(value):
        if value < 0:
            raise ValueError("Cannot calculate the square root of a negative number")
        return math.sqrt(value)
    
    def test_calculate_square_root():
        with pytest.raises(ValueError):
            calculate_square_root(-1)
    ```
    
2. **Vérification de** `ZeroDivisionError` : Diviser un nombre par zéro lève une `ZeroDivisionError`. Dans cet exemple, nous vérifions que cette erreur est levée lors de la division d'un nombre par zéro.
    
    ```jsx
    import pytest
    
    def divide_numbers(numerator, denominator):
        return numerator / denominator
    
    def test_divide_numbers():
        with pytest.raises(ZeroDivisionError):
            divide_numbers(10, 0)
    ```
    
3. **Vérification de** `TypeError` : Une `TypeError` est levée lorsqu'une opération est appliquée à un objet d'un type inapproprié. Ici, nous vérifions que cette erreur est levée lors de l'addition de types de données incompatibles, tels qu'une chaîne et un entier donnés dans l'exemple.
    
    ```jsx
    import pytest
    
    def add_numbers(a, b):
        return a + b
    
    def test_add_numbers():
        with pytest.raises(TypeError):
            add_numbers("10", 5)
    ```
    
4. **Vérification de** `KeyError` : Une `KeyError` est levée lorsque nous essayons d'accéder à une clé de dictionnaire qui n'existe pas. Nous pouvons vérifier et gérer cette erreur en utilisant le code suivant :
    
    ```python
    import pytest
    
    def get_value(dictionary, key):
        return dictionary[key]
    
    def test_get_value():
        with pytest.raises(KeyError):
            get_value({"name": "Alice"}, "age")
    ```
    

## Fonctionnalités avancées de pytest

En tant que framework de test robuste, pytest offre certaines fonctionnalités avancées qui vous aident à gérer des scénarios de test complexes. Dans cette section, nous explorerons certaines de ces fonctionnalités avancées à un niveau adapté aux débutants et démontrerons comment vous pouvez commencer à les appliquer dans vos tests.

### 1. Marqueurs pytest

Lorsqu'on travaille avec une grande base de code, parfois exécuter chaque test peut être chronophage. C'est là que les marqueurs pytest sont utiles.

Un marqueur est comme une étiquette que vous pouvez attacher à une fonction de test pour la catégoriser. Une fois qu'un test est étiqueté, vous pouvez instruire pytest d'exécuter uniquement les tests avec certains marqueurs. Par exemple, vous pouvez étiqueter certains tests comme "lents" s'ils prennent plus de temps à s'exécuter et les exécuter séparément des plus rapides.

Un avantage de l'utilisation des marqueurs est qu'ils permettent d'exécuter des tests spécifiques basés sur des catégories ou des paramètres spécifiques, et également de sauter des tests si certaines conditions ne sont pas remplies.

pytest est livré avec certains marqueurs intégrés qui peuvent être assez utiles :

1. `@pytest.mark.skip` : Ce marqueur vous permet de sauter un test de manière inconditionnelle, et peut être utile lorsque vous savez qu'un test échouera en raison d'un problème externe ou d'un code incomplet.
    
    **Exemple :**
    
    ```python
    @pytest.mark.skip(reason="Feature not yet implemented")
    def test_feature():
        pass
    ```
    
2. `@pytest.mark.skipif` : Ce marqueur vous permet de sauter un test de manière conditionnelle si certaines conditions sont remplies.
    
    **Exemple :**
    
    ```python
    import sys
    
    @pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
    class TestClass:
        def test_function(self):
            "This test will not run under 'win32' platform"
    ```
    
3. `@pytest.mark.xfail` : Ce marqueur est attaché aux tests qui sont censés échouer, probablement en raison d'un bug ou d'une fonctionnalité incomplète. Ainsi, lorsque pytest exécute de tels tests, il ne les comptera pas comme un échec.
    
    **Exemple :**
    
    ```python
    @pytest.mark.xfail(reason="division by zero not handled yet")
    def test_divide_by_zero():
        assert divide(10, 0) == 0
    ```
    
    **Note :** Les informations détaillées sur les tests ignorés/échoués ne sont pas affichées par défaut pour éviter d'encombrer la sortie.
    

Bien que pytest soit livré avec certains marqueurs intégrés, vous pouvez également créer votre propre marqueur personnalisé (mais nous n'aborderons pas cela dans ce tutoriel). Veuillez vous référer à la documentation pour plus d'informations sur [le travail avec des marqueurs personnalisés](https://docs.pytest.org/en/stable/example/markers.html)

### 2. Fixtures pytest

Dans pytest, les fixtures vous permettent de créer des données par défaut réutilisables qui peuvent être partagées entre plusieurs tests. En utilisant des fixtures, vous pouvez réduire la répétition de code, rendant vos tests plus propres et plus faciles à maintenir.

Dans pytest, les fixtures sont définies avec le décorateur `@pytest.fixture` comme montré dans l'exemple ci-dessous :

Supposons que nous avons plusieurs tests qui dépendent d'une liste de données utilisateur. Au lieu de répéter les mêmes données dans chaque test, nous pouvons créer une fixture pour contenir ces données, et la fixture est transmise aux tests qui en ont besoin.

```python
import pytest

@pytest.fixture
def user_data():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]

# Fonction de test pour vérifier un utilisateur spécifique par nom et âge
def test_user_exists(user_data):
    user = {"name": "Alice", "age": 30}

    # Vérifier si l'utilisateur cible est dans la liste
    assert user in user_data
   
# Test de l'âge moyen des utilisateurs
def test_average_age(user_data):
    ages = [user["age"] for user in user_data]
    avg_age = sum(ages) / len(ages)
    assert avg_age == 30
```

**Note :** Le décorateur `@pytest.fixture` dans le code ci-dessus marque la fonction `user_data` comme une fixture dans pytest. Cette fixture fournit des données réutilisables qui peuvent être partagées entre plusieurs fonctions de test, leur permettant de partager la même configuration sans répéter de code.

### 3. Paramétrisation

La paramétrisation est une fonctionnalité de pytest qui permet d'exécuter une fonction de test avec différents ensembles de données à la fois.

Par exemple : Supposons que vous avez une fonction qui calcule le carré d'un nombre. Pour fournir une couverture suffisante lors des tests, vous souhaiteriez tester la fonction avec des nombres zéro, positifs et négatifs.

Au lieu d'écrire des fonctions de test séparées pour chaque scénario, vous pouvez utiliser la paramétrisation pour exécuter une fonction de test avec différents ensembles de données à la fois. Cette approche est plus concise et réduit la duplication de code.

Pour utiliser la paramétrisation dans pytest, nous utilisons le décorateur `@pytest.mark.parametrize` comme montré dans l'exemple ci-dessous :

```python
import pytest

# Fonction pour calculer le carré d'un nombre
def square_numbers(num):
    return num * num

# Décorateur Parametrize pour tester la fonction square avec différentes entrées
@pytest.mark.parametrize("input_value, expected_output", [
    (2, 4),     
    (-3, 9),    
    (0, 0)    
])

def test_square(input_value, expected_output):
    assert square_numbers(input_value) == expected_output
```

Dans l'exemple ci-dessus, les différentes valeurs d'entrée et les valeurs attendues sont listées dans le décorateur `@pytest.mark.parametrize`. Nous testons la fonction `square_numbers()` avec trois valeurs d'entrée différentes : `2`, `-3`, et `0`.

Pour chaque valeur, pytest appelle la fonction `test_square()` et compare le résultat de `square_numbers(input_value)` à `expected_output`.

Cette approche est plus efficace et garantit que la fonction se comporte comme prévu dans une variété de cas.

### 4. Plugins pytest

Les plugins sont un mécanisme d'extension qui permet d'ajouter de nouvelles fonctionnalités à pytest ou de modifier son comportement existant. Ces plugins fonctionnent en fournissant des fonctionnalités supplémentaires qui étendent les capacités de pytest, ce qui peut être utile, surtout dans des scénarios de test complexes.

pytest dispose d'un vaste écosystème de plugins, chacun conçu pour répondre à vos différents besoins de test. Vous pouvez trouver la liste complète des plugins disponibles sur [PyPI](https://pypi.org/) dans la [liste des plugins pytest](https://docs.pytest.org/en/stable/reference/plugin_list.html#plugin-list).

Pour utiliser un plugin, il suffit de l'installer avec `pip`.

**Par exemple :**

```python
pip install pytest-NAME
pip uninstall pytest-NAME
```

**Note :** `NAME` dans le code ci-dessus doit être remplacé par le nom du plugin que vous souhaitez installer.

Après avoir installé un plugin, pytest le trouve et l'intègre automatiquement. Il n'est pas nécessaire de faire une configuration supplémentaire.

Dans cette section, nous avons exploré certaines des fonctionnalités avancées de pytest. En tirant parti de ces fonctionnalités, vous pouvez maintenant améliorer significativement la qualité de vos tests en vous assurant qu'ils sont plus efficaces, évolutifs et plus faciles à maintenir au fil du temps.

## Conclusion

Dans cet article, vous avez appris les bases des tests avec pytest, de l'écriture et de l'interprétation des tests à la gestion des exceptions et à l'utilisation de fonctionnalités avancées comme les fixtures et la paramétrisation.

Que votre code soit écrit manuellement ou généré par l'IA, apprendre à écrire des tests vous permet de détecter les bugs tôt et de construire des logiciels plus fiables. Les tests agissent comme un filet de sécurité qui renforce votre confiance pendant le développement et garantit que votre code fonctionne comme prévu.

Si vous êtes prêt à aller plus loin, j'ai écrit un article approfondi sur le [Développement Piloté par les Tests en Python](https://judeolowo.hashnode.dev/test-driven-development-in-python-a-complete-guide-to-unittest). C'est une approche puissante où l'écriture de tests guide votre processus de codage entier.

Si vous avez trouvé cela utile, faites-le moi savoir, partagez-le avec votre réseau, ou donnez-lui un like pour aider les autres à le découvrir aussi.