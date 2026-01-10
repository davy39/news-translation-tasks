---
title: Messages d'erreur de code courants
date: '2024-01-24T12:24:00.000Z'
author: Samyak Jain
authorURL: https://www.freecodecamp.org/news/author/samyak/
originalURL: https://freecodecamp.org/news/python-debugging-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/The-Python-Debugging-Handbook-Cover--1-.png
tags:
- name: debugging
  slug: debugging
- name: handbook
  slug: handbook
- name: Python
  slug: python
seo_desc: 'Programming is an art, and bugs are an inevitable part of the creative
  process. Every developer encounters errors in their code – there''s really no exception
  to it.

  Because of this, understanding how to effectively debug is a crucial skill that
  can s...'
---


La programmation est un art, et les bugs sont une partie inévitable du processus créatif. Chaque développeur rencontre des erreurs dans son code – il n'y a vraiment aucune exception à cela.

<!-- more -->

C'est pourquoi comprendre comment déboguer efficacement est une compétence cruciale qui peut vous faire gagner du temps et vous éviter bien des frustrations.

Dans ce tutoriel, nous allons approfondir les bases du débogage de code Python. Nous explorerons les messages d'erreur courants, verrons comment s'appuyer sur la communauté et utiliserons des instructions `print` pour identifier et résoudre les problèmes. L'objectif principal est d'identifier et de corriger les erreurs dans votre code, et la clé d'un débogage réussi réside dans une approche systématique.

## Table des matières

1.  **[Messages d'erreur de code courants][1]**

-   [SyntaxError: invalid syntax][2]
-   [IndentationError: unexpected indent][3]
-   [NameError: name 'variable' is not defined][4]
-   [AttributeError: 'module' object has no attribute 'attribute\_name'][5]
-   [FileNotFoundError: \[Errno 2\] No such file or directory: 'filename'][6]
-   [IndexError: list index out of range][7]
-   [ImportError: No module named 'module\_name'][8]
-   [TypeError][9]
-   [ValueError][10]

2\.  **[Comment déboguer du code Python][11]**

3\.   [**Techniques de débogage fondamentales**][12]

-   [Instructions Print][13]
-   [Logging][14]
-   [Gestion des exceptions][15]
-   [Assertions][16]

4.   [**Techniques de débogage avancées**][17]

-   [Tests unitaires][18]
-   [Débogueur interactif (PDB)][19]
-   [Débogage à distance][20]

5\.  [**Débogage de performance**][21]

-   [Linters et analyseurs de code][22]
-   [Profilage][23]

6\.  **[Fonctionnalités des IDE pour le débogage][24]**

7.   **[Quelques conseils supplémentaires pour un débogage efficace][25]**

8.   **[Comment rechercher des solutions aux bugs et erreurs][26]**

-   [Stratégies de recherche efficaces][27]
-   [Exploiter les ressources web][28]

# Messages d'erreur de code courants

Avant de passer au débogage, examinons d'abord quelques messages d'erreur courants et leurs significations :

_Si vous êtes déjà familier avec les messages d'erreur de code courants, n'hésitez pas à sauter cette section et à passer directement aux [Techniques de débogage][29]._

## 1\. SyntaxError: invalid syntax

Cette erreur se produit lorsque l'interpréteur Python rencontre du code qui ne respecte pas les règles de syntaxe correctes. Il peut s'agir d'une parenthèse manquante, d'un deux-points mal placé ou d'un autre problème lié à la syntaxe.

Pour corriger ce type d'erreurs, vérifiez les éléments de syntaxe manquants et assurez-vous que les guillemets, parenthèses et crochets vont bien par paires.

## 2\. IndentationError: unexpected indent

Python s'appuie sur l'indentation pour définir les blocs de code. Cette erreur survient lorsque l'indentation est incohérente ou incorrecte.

Pour éviter ces erreurs, assurez-vous d'utiliser une indentation appropriée et constante en utilisant des espaces ou des tabulations comme requis par le langage.

## 3\. NameError: name 'variable' is not defined

Ces types d'erreurs peuvent résulter d'une tentative d'utilisation d'une variable ou d'une fonction qui n'a pas été définie.

Assurez-vous de vérifier les fautes de frappe dans les noms de variables ou de fonctions, et assurez-vous qu'elles sont définies avant d'être utilisées.

## 4\. AttributeError: 'module' object has no attribute 'attribute\_name'

Vous pouvez obtenir ce type d'erreur en essayant d'accéder à un attribut ou une méthode qui n'existe pas pour un module ou un objet.

Pour corriger cela, examinez le code et confirmez que l'attribut ou la méthode appelé est correct et disponible.

## 5\. FileNotFoundError: \[Errno 2\] No such file or directory: 'filename'

Vous obtiendrez cette erreur en tentant d'accéder à un fichier qui n'existe pas.

Vous devez vérifier le chemin du fichier et vous assurer que le fichier existe à l'emplacement spécifié.

## 6\. IndexError: list index out of range

Ce type d'erreur se produit lorsque vous essayez d'accéder à un index dans une séquence (comme une liste ou une chaîne de caractères) qui n'existe pas. La même erreur peut se produire pour les chaînes et les tuples pour la même raison.

Pour la corriger, assurez-vous que l'index utilisé se trouve dans la plage valide de la séquence.

## 7\. ImportError: No module named 'module\_name'

Vous obtiendrez cette erreur si vous tentez d'importer un module qui n'est pas installé ou accessible.

Pour éviter cela, installez le module requis à l'aide d'un gestionnaire de paquets (pip) ou vérifiez le nom du module pour détecter d'éventuelles fautes de frappe.

## 8\. TypeError:

Il s'agit d'une exception courante en Python qui se produit lorsqu'une opération ou une fonction est appliquée à un objet d'un type inapproprié. Voici quelques types courants de `TypeError` :

1.  `TypeError: unsupported operand type(s) for +: 'type1' and 'type2'`**:** Cette erreur se produit lors d'une tentative d'opération sur deux objets de types incompatibles. Par exemple, essayer d'additionner une chaîne et un entier ou de multiplier une liste par une chaîne.
2.  `TypeError: function_name() takes X positional arguments but Y were given`**:** Cette erreur survient lors de l'appel d'une fonction avec un nombre incorrect d'arguments. Elle indique que la fonction attend un nombre spécifique d'arguments, mais qu'un nombre différent a été fourni.
3.  `TypeError: 'int' object is not callable`: Cette erreur se produit lorsque vous essayez d'appeler un objet comme s'il s'agissait d'une fonction, alors qu'il ne peut pas être appelé. Par exemple, tenter d'appeler un entier.

## 9\. ValueError:

Ce type d'erreur se produit lorsqu'une fonction reçoit un argument du bon type mais avec une valeur inappropriée.

1.  `ValueError: invalid literal for int() with base X: 'non-numeric'`: Cela se produit lors d'une tentative de conversion d'une chaîne en entier à l'aide de `int()`, mais la chaîne n'est pas une représentation valide d'un entier dans la base spécifiée (X). Par exemple, essayer de convertir une chaîne non numérique ou une chaîne avec un format invalide (contenant des lettres, par exemple) en entier.
2.  `ValueError: could not convert string to float: 'non-numeric'`: Cela arrive en essayant de convertir une chaîne en nombre à virgule flottante à l'aide de `float()`, mais la chaîne n'est pas une représentation valide d'un nombre. Comme pour le premier cas, cela implique souvent des caractères non numériques ou un format incorrect.
3.  `ValueError: invalid literal for int() with base 10: 'non-numeric'`: Similaire au premier cas, cette erreur survient en essayant de convertir une chaîne en entier avec `int()`, mais la chaîne n'est pas une représentation numérique valide en base 10. C'est une forme plus générale du premier type, où la base est explicitement fixée à 10.
4.  `ValueError: unhashable type: 'mutable_type'`: Cette erreur se produit en essayant d'utiliser un type mutable (par exemple, une liste, un dictionnaire) comme clé dans un dictionnaire ou comme élément dans un ensemble (set). Les dictionnaires et les ensembles exigent que les clés et les éléments soient d'un type hachable (immuable). Pour résoudre cela, convertissez le type mutable en un type immuable ou envisagez une structure de données différente qui supporte les éléments mutables.

Comprendre ces erreurs courantes constitue une base pour un débogage efficace.

# Comment déboguer du code Python

Maintenant que vous comprenez certains types d'erreurs courants, explorons diverses techniques et outils qui peuvent vous aider à déboguer votre code Python efficacement.

## Techniques de débogage fondamentales :

### Instructions Print

Lorsque vous écrivez du code, en particulier dans des programmes complexes, il est essentiel de comprendre comment votre code s'exécute et de connaître les valeurs des variables à différents points du programme. Les instructions print vous permettent d'insérer des messages dans votre code qui s'affichent dans la console ou le terminal lors de l'exécution du programme.

En plaçant stratégiquement des instructions print dans différentes parties de votre code, vous pouvez créer une sorte de journal qui montre l'ordre dans lequel les différentes sections de votre code sont exécutées. Cela peut vous aider à comprendre le flux de contrôle et à identifier l'endroit où le programme pourrait dévier de vos attentes.

Voici un exemple :

```python
def my_function(x, y):
    print("Entering my_function")
    print(f'x: {x}, y: {y}')
    result = x + y
    print(f'Result: {result}')
    print("Exiting my_function")
    return result
```

Bien que les instructions `print` soient souvent le moyen le plus rapide et le plus simple d'avoir un aperçu du flux d'exécution d'un programme, surtout lors du développement initial, elles peuvent être fastidieuses à gérer et peuvent ne pas être appropriées pour du code en production. C'est là qu'intervient le Logging, qui offre un moyen structuré d'enregistrer des informations.

### Logging

Le logging consiste à prendre des notes pendant que votre programme s'exécute. Au lieu de simplement afficher des choses à l'écran, vous les écrivez dans un journal (log). Cela vous aide à suivre ce que fait votre programme, surtout quand les choses tournent mal.

Vous pouvez configurer le logging pour contrôler le niveau de détail des messages et spécifier la destination des journaux. Il peut s'agir de la console, d'un fichier ou d'autres destinations.

#### Niveaux de Logging :

-   **DEBUG :** Informations détaillées, utiles pour les développeurs pendant le débogage.
-   **INFO :** Informations générales sur ce qui se passe dans le programme.
-   **WARNING :** Indique que quelque chose d'inattendu s'est produit, mais que le programme peut continuer.
-   **ERROR :** Quelque chose s'est mal passé, et le programme ne peut pas se poursuivre comme prévu.
-   **CRITICAL :** Une erreur très grave, pouvant entraîner l'arrêt du programme.

Voici un exemple de logging :

```python
import logging

logging.basicConfig(level=logging.Info)

def example_function(x, y):
    logging.debug(f"Input values: x={x}, y={y}")
    result = x + y
    logging.debug(f"Result: {result}")
    return result

result = example_function(3, 7)

# Logging an error message
if result > 10:
    logging.error("Result exceeds the expected maximum.")
```

-   **`level=logging.INFO`** définit le niveau du logger racine sur `INFO`. Cela signifie que les messages de log de sévérité `INFO` et supérieure seront capturés, tandis que les messages de sévérité inférieure (comme `DEBUG`) seront ignorés. Il écrit les logs dans un fichier nommé `example.log`.
-   À l'intérieur de `example_function`, `logging.debug()` est utilisé pour enregistrer des informations sur les valeurs d'entrée et le résultat. Ces messages ne seront affichés que si le niveau de logging est réglé sur `DEBUG` ou inférieur.
-   Un message d'erreur est enregistré via `logging.error()` si le résultat dépasse le maximum attendu (dans ce cas, 10).
-   Le logging peut être configuré pour écrire des messages à la fois sur la console et dans un fichier nommé `example.log`. Le paramètre `format` peut être utilisé pour personnaliser l'apparence des messages, incluant l'horodatage, le niveau de log et le message lui-même.

```python
# Optionnel
logging.basicConfig(
    filename='example.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# ce format inclut l'horodatage, le nom du module et le niveau de log dans chaque message.
```

**Note** : Dans les applications plus importantes, il est courant d'utiliser des loggers spécifiques plutôt que le logger racine directement. Cette approche permet un contrôle plus fin du logging dans différentes parties de l'application. Vous pouvez en apprendre davantage sur le logging et les loggers ici.

Pour en savoir plus sur le logging et les loggers en Python, consultez ce blog : [https://www.samyakinfo.tech/blog/logging-in-python][30]

### Gestion des exceptions

Enveloppez les blocs de code suspects avec des instructions try-except pour capturer et gérer les exceptions. Cela empêche votre programme de s'arrêter brusquement, vous permettant de gérer les erreurs avec élégance et d'enregistrer les informations pertinentes.

L'instruction `try-except` est un moyen de gérer les exceptions en Python. Voici une structure de base :

```python
try:
    result = x / y
except ExceptionType as e:
    print(f"An exception of type {type(e).__name__} occurred: {e}")
    # Logique de gestion supplémentaire, si nécessaire
```

-   **Bloc `try` :** Contient le code susceptible de lever une exception.
-   **Bloc `except` :** Contient le code qui est exécuté si une exception du type spécifié se produit dans le bloc `try`.
-   **Type d'exception :** Spécifie le type d'exception à capturer. Vous pouvez capturer des exceptions spécifiques ou un type `Exception` plus général pour capturer n'importe quelle exception.
-   **`as e:` :** Assigne l'objet exception à la variable `e`, vous permettant d'accéder aux informations sur l'erreur.

```python
def safe_divide(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {type(e).__name__} - {e}")
        # Gérer le cas de division par zéro
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")
        # Gérer d'autres types d'exceptions
    finally:
        print("This block always executes, whether an exception occurred or not.")

# Ex.
safe_divide(10, 2)
safe_divide(5, 0)
```

Dans cet exemple, la fonction `safe_divide` tente d'effectuer une division. Si une `ZeroDivisionError` se produit (division par zéro), elle est capturée dans le premier bloc `except`. Si n'importe quel autre type d'exception survient, elle est capturée dans le second bloc `except`. Le bloc `finally` s'exécute toujours, qu'une exception se soit produite ou non.

### Assertions

Une assertion est une instruction que vous ajoutez à votre code pour vérifier si une certaine condition est vraie. Si la condition est fausse, cela indique un bug ou une situation inattendue dans votre programme.

En Python, vous utilisez le mot-clé `assert` pour créer une assertion. La syntaxe est :

```python
assert condition, "Optional error message"

# Exemple d'assertion avec un message d'erreur optionnel
x = 10
y = 0
assert y != 0, "Divisor (y) should not be zero"

# Gestion de AssertionError
try:
    assert x > 0, "x should be greater than zero"
except AssertionError as e:
    print(f"Assertion failed: {e}")
```

Dans cet exemple, `assert y != 0` vérifie si le diviseur (`y`) n'est pas nul. S'il est nul, l'assertion échoue et le programme lève une `AssertionError` avec le message d'erreur spécifié.

#### Considérations lors de l'utilisation des assertions :

-   Les assertions sont généralement utilisées pendant le développement et le débogage. Dans un environnement de production, vous pouvez choisir de les désactiver pour des raisons de performance. Pour les désactiver, utilisez l'option de ligne de commande `-O` (ex. `python -O script.py`) ou la variable d'environnement `PYTHONOPTIMIZE`. Le drapeau `-O` (optimisation) désactive les instructions assert.
-   Les assertions ne sont pas destinées à la validation des entrées des utilisateurs ou des systèmes externes. Elles servent plutôt à détecter des erreurs logiques dans votre code.
-   Les assertions doivent être des conditions simples, faciles à vérifier et à comprendre. Évitez les expressions complexes ou les effets secondaires.

## Techniques de débogage avancées :

### Tests unitaires

Le test unitaire est une méthodologie de test logiciel où des composants ou fonctions individuels d'un programme sont testés de manière isolée pour s'assurer qu'ils fonctionnent correctement. En Python, les unités désignent généralement des fonctions, des méthodes ou des classes.

1.  Les tests unitaires aident à détecter les bugs tôt dans le processus de développement, les empêchant de devenir des problèmes plus complexes.
2.  Les tests unitaires se concentrent sur des fonctions ou méthodes spécifiques de manière isolée. Cela permet de localiser précisément la source des erreurs lorsqu'elles surviennent.
3.  À mesure que le code évolue, les tests unitaires agissent comme un filet de sécurité, garantissant que les nouvelles modifications ne cassent pas par inadvertance les fonctionnalités existantes.

### Comment utiliser `unittest`

`unittest` est le framework de test intégré à Python, inspiré par JUnit de Java. Il fournit un mécanisme de découverte de tests et diverses méthodes d'assertion pour vérifier le comportement attendu.

Commençons par un exemple simple. Supposons que nous ayons une fonction qui additionne deux nombres :

```Python
# my_module.py

def add_numbers(a, b):
    return a + b
```

Maintenant, nous pouvons créer un fichier de test correspondant :

```Python
# test_my_module.py
import unittest
from my_module import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```

Pour lancer les tests, exécutez la commande suivante dans le terminal :

```
python -m unittest test_my_module.py
```

### Comment utiliser `pytest`

`pytest` est un framework de test tiers qui offre une syntaxe plus concise et des fonctionnalités supplémentaires telles que des fixtures puissantes et un support étendu de plugins.

En utilisant le même exemple que précédemment, un test `pytest` pourrait ressembler à ceci :

```Python
# test_my_module.py

from my_module import add_numbers

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5
```

Pour lancer les tests, exécutez simplement :

```
pytest test_my_module.py
```

### Comment utiliser le débogueur interactif (PDB)

Python est livré avec un débogueur intégré appelé PDB (Python Debugger). Il vous permet de suspendre l'exécution de votre code Python, d'inspecter les variables et de parcourir votre code ligne par ligne pour trouver et corriger les problèmes.

Alors que les instructions print et le logging sont utiles pour le débogage de base, PDB fait passer le débogage au niveau supérieur en vous permettant d'intervenir et d'analyser votre code en temps réel.

Dans votre script Python, commencez par importer le module `pdb`. Ce module fournit les fonctionnalités de débogage. `import pdb`

```python
import pdb

def example_function(x, y):
    pdb.set_trace()
    result = x + y
    return result
```

#### Définir des points d'arrêt

Pour démarrer le débogage à un point précis de votre code, insérez l'instruction `pdb.set_trace()`. Cette ligne agit comme un point d'arrêt (breakpoint), indiquant où le débogueur doit suspendre l'exécution du programme.

```python
def some_function():
    pdb.set_trace()  # Cette ligne définit un point d'arrêt
    print("Hello, World!")
```

Lorsque le programme atteint cette ligne pendant l'exécution, il s'arrête et le débogueur est activé.

#### Démarrer le débogueur :

Il existe deux façons de démarrer le débogueur :

**a.** **Utilisation de la commande `break` :**

Dans Python 3.7 et les versions ultérieures, `pdb` a introduit la fonction `pdb.breakpoint()` comme un moyen plus pratique et standardisé de définir un point d'arrêt et de résoudre certains problèmes potentiels avec la méthode `pdb.set_trace()`.

Vous pouvez définir des points d'arrêt directement dans votre code en utilisant la commande `break`. Par exemple :

```python
import pdb

def some_function():
    # Définition d'un point d'arrêt à la ligne 4
    pdb.breakpoint()
    print("Hello, World!")

some_function()
```

**b.** **Exécution du script avec l'option `-m pdb` :**

Alternativement, vous pouvez exécuter votre script Python avec l'option `-m pdb`, qui démarre automatiquement le débogueur. Par exemple :

```
python -m pdb your_script.py
```

#### Entrer en mode débogueur :

Lorsque votre code rencontre le point d'arrêt (défini via `pdb.set_trace()` ou `pdb.breakpoint()`), il entre dans le mode débogueur interactif. Ceci est indiqué par l'invite `(Pdb)`.

![Screenshot-2024-01-18-212824-1](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-18-212824-1.png)

Un aperçu du mode débogueur interactif dans le terminal

#### Commandes de base :

Maintenant, vous pouvez interagir avec le débogueur et utiliser diverses commandes pour inspecter les variables, parcourir le code, et identifier puis corriger les problèmes.

Certaines commandes courantes du débogueur pdb incluent :

-   `n` (next) : Continue l'exécution jusqu'à ce que la ligne suivante de la fonction actuelle soit atteinte. Si la ligne actuelle contient un appel de fonction, il ne rentrera pas dans la fonction appelée.
-   `c` (continue) : Continue l'exécution jusqu'à ce que le prochain point d'arrêt soit rencontré.
-   `s` (step) : Exécute la ligne de code actuelle et s'arrête à la première occasion possible (soit dans une fonction appelée, soit à la ligne suivante de la fonction actuelle).
-   `q` (quit) : Quitte le débogueur et termine le programme.
-   **`break` (ou `b`) :** `break [file:]line_number` ou `break [function_name]` Définit un point d'arrêt au numéro de ligne ou à la fonction spécifiés. Lorsque l'exécution du programme atteint le point d'arrêt, elle s'arrête, vous permettant d'inspecter les variables et de parcourir le code.

En plaçant stratégiquement des points d'arrêt et en utilisant ces commandes, vous pouvez déboguer efficacement votre code Python et identifier la source des problèmes de manière systématique.

<table style="
    box-sizing: border-box;
    margin: 25px auto;
    padding: 0px;
    border: 0px;
    font-size: 17px;
    vertical-align: baseline;
    border-collapse: collapse;
    border-spacing: 0px;
    overflow-x: auto;
    display: inherit;
    color: rgb(39, 50, 57);
    font-family: Nunito, sans-serif;
    font-style: normal;
    font-variant-ligatures: normal;
    font-variant-caps: normal;
    font-weight: 400;
    letter-spacing: 0.162px;
    orphans: 2;
    text-align: justify;
    text-transform: none;
    widows: 2;
    word-spacing: 0px;
    -webkit-text-stroke-width: 0px;
    white-space: normal;
    background-color: rgb(255, 255, 255);
    text-decoration-thickness: initial;
    text-decoration-style: initial;
    text-decoration-color: initial;
  "><tbody style="
      box-sizing: border-box;
      margin: 0px;
      padding: 0px;
      border: 0px;
      font-size: 17px;
      vertical-align: baseline;
    "><tr style="
        box-sizing: border-box;
        margin: 0px;
        padding: 0px;
        border: 0.3px solid rgb(223, 223, 223);
        font-size: 17px;
        vertical-align: baseline;
        background-color: var(--gfg-body-color);
      "><td style="
          box-sizing: border-box;
          margin: 0px;
          padding: 14px 10px;
          border: 0.3px solid rgb(223, 223, 223);
          font-size: 12.5pt;
          vertical-align: middle;
          width: 120px;
          font-weight: 400;
          text-align: center;
        "><strong style="
            box-sizing: border-box;
            margin: 0px;
            padding: 0px;
            border: 0px;
            font-size: var(--font-secondary);
            vertical-align: baseline;
          ">Commande</strong></td><td style="
          box-sizing: border-box;
          margin: 0px;
          padding: 14px 10px;
          border: 0.3px solid rgb(223, 223, 223);
          font-size: 12.5pt;
          vertical-align: middle;
          font-weight: 400;
          text-align: center;
        "><strong style="
            box-sizing: border-box;
            margin: 0px;
            padding: 0px;
            border: 0px;
            font-size: var(--font-secondary);
            vertical-align: baseline;
          ">Fonctionnalité</strong></td></tr><tr style="
      box-sizing: border-box;
      margin: 0px;
      padding: 0px;
      border: 0.3px solid rgb(223, 223, 223);
      font-size: 17px;
      vertical-align: baseline;
      background-color: var(--gfg-body-color);
    "><td style="
        box-sizing: border-box;
        margin: 0px;
        padding: 14px 10px;
        border: 0.3px solid rgb(223, 223, 223);
        font-size: 12.5pt;
        vertical-align: middle;
        font-weight: 400;
        text-align: center;
      ">list (ou l)</td><td style="
        box-sizing: border-box;
        margin: 0px;
        padding: 14px 10px;
        border: 0.3px solid rgb(223, 223, 223);
        font-size: 12.5pt;
        vertical-align: middle;
        font-weight: 400;
        text-align: center;
      "><strong>list ou list [first[, last]]:</strong> Affiche le code source autour de la ligne actuelle. Optionnellement, vous pouvez spécifier une plage de lignes à afficher.</td></tr><tr style="
    box-sizing: border-box;
    margin: 0px;
    padding: 0px;
    border: 0.3px solid rgb(223, 223, 223);
    font-size: 17px;
    vertical-align: baseline;
    background-color: var(--gfg-body-color);
  "><td style="
      box-sizing: border-box;
      margin: 0px;
      padding: 14px 10px;
      border: 0.3px solid rgb(223, 223, 223);
      font-size: 12.5pt;
      vertical-align: middle;
      font-weight: 400;
      text-align: center;
    ">print (ou p)</td><td style="
      box-sizing: border-box;
      margin: 0px;
      padding: 14px 10px;
      border: 0.3px solid rgb(223, 223, 223);
      font-size: 12.5pt;
      vertical-align: middle;
      font-weight: 400;
      text-align: center;
    "><b>print expression:</b> Évalue et affiche la valeur de l'expression spécifiée. Utile pour inspecter les variables.</td></tr><tr style="
  box-sizing: border-box;
  margin: 0px;
  padding: 0px;
  border: 0.3px solid rgb(223, 223, 223);
  font-size: 17px;
  vertical-align: baseline;
  background-color: var(--gfg-body-color);
"><td style="
    box-sizing: border-box;
    margin: 0px;
    padding: 14px 10px;
    border: 0.3px solid rgb(223, 223, 223);
    font-size: 12.5pt;
    vertical-align: middle;
    font-weight: 400;
    text-align: center;
  ">break (ou b)</td><td style="
    box-sizing: border-box;
    margin: 0px;
    padding: 14px 10px;
    border: 0.3px solid rgb(223, 223, 223);
    font-size: 12.5pt;
    vertical-align: middle;
    font-weight: 400;
    text-align: center;
  "><b>[file:]line_number ou break [function_name]:</b> Définit un point d'arrêt au numéro de ligne ou à la fonction spécifiés. Lorsque l'exécution du programme atteint le point d'arrêt, elle s'arrête, vous permettant d'inspecter les variables et de parcourir le code.</td></tr><tr style="
        box-sizing: border-box;
        margin: 0px;
        padding: 0px;
        border: 0.3px solid rgb(223, 223, 223);
        font-size: 17px;
        vertical-align: baseline;
      "><td style="
          box-sizing: border-box;
          margin: 0px;
          padding: 14px 10px;
          border: 0.3px solid rgb(223, 223, 223);
          font-size: 12.5pt;
          vertical-align: middle;
          font-weight: 400;
          text-align: center;
        ">help</td><td style="
          box-sizing: border-box;
          margin: 0px;
          padding: 14px 10px;
          border: 0.3px solid rgb(223, 223, 223);
          font-size: 12.5pt;
          vertical-align: middle;
          font-weight: 400;
          text-align: center;
        ">Affiche la liste des commandes ou fournit des informations sur une commande ou un sujet spécifique (ex. help breakpoints)</td></tr><tr style="
        box-sizing: border-box;
        margin: 0px;
        padding: 0px;
        border: 0.3px solid rgb(223, 223, 223);
        font-size: 17px;
        vertical-align: baseline;
        background-color: var(--gfg-body-color);
      "><td style="
          box-sizing: border-box;
          margin: 0px;
          padding: 14px 10px;
          border: 0.3px solid rgb(223, 223, 223);
          font-size: 12.5pt;
          vertical-align: middle;
          font-weight: 400;
          text-align: center;
        ">where</td><td style="
          box-sizing: border-box;
          margin: 0px;
          padding: 14px 10px;
          border: 0.3px solid rgb(223, 223, 223);
          font-size: 12.5pt;
          vertical-align: middle;
          font-weight: 400;
          text-align: center;
        ">Affiche une trace de la pile (stack traceback) des appels de fonctions menant au point actuel dans le code. Chaque ligne de la trace inclut généralement le nom de la fonction, le nom du fichier et le numéro de ligne où la fonction a été appelée.</td></tr></tbody></table>

#### Extensions de débogueur

Envisagez d'utiliser des outils et extensions de débogage tiers, tels que `pdbpp`, `pudb` et `ipdb`, qui améliorent les fonctionnalités du débogueur PDB intégré.

`pdbpp` offre des fonctionnalités supplémentaires telles que la coloration syntaxique, la complétion par tabulation et de meilleures capacités de navigation.

`ipdb` est un débogueur basé sur IPython, intégrant les puissantes fonctionnalités d'IPython dans l'expérience de débogage. Il offre une interface interactive et conviviale. Il supporte les commandes magiques d'IPython, facilitant les tâches de débogage complexes.

`pudb` est un débogueur visuel plein écran basé sur la console qui fournit la coloration syntaxique et une expérience de débogage visuellement attrayante. Il comprend une interface visuelle avec un explorateur de code, facilitant la navigation.

Pour utiliser l'un d'entre eux, remplacez `pdb` par le débogueur correspondant. Par ex. `import pdb; pdb.set_trace()` par `import pdbpp; pdbpp.set_trace()` dans votre code.

### Débogage à distance

Le débogage à distance désigne le processus de débogage d'un code qui s'exécute sur un système ou un serveur distinct de l'environnement de développement. C'est couramment utilisé lorsque l'application est déployée sur un serveur distant, dans le cloud ou sur un appareil différent.

Vous connectez votre environnement de développement intégré (IDE) local à l'environnement distant où le code s'exécute.

Vous pouvez le faire de deux manières :

-   **IDE avec support du débogage à distance :** Les IDE populaires comme PyCharm, Visual Studio Code et d'autres offrent un support intégré pour le débogage à distance.
-   **Bibliothèque pdb ou pydevd :** Le module `pdb` intégré à Python peut être utilisé pour un débogage de base. Alternativement, vous pouvez utiliser `pydevd`, un puissant débogueur à distance.

Les points d'arrêt à distance, le parcours du code, l'inspection des variables et d'autres fonctionnalités de débogage sont employés, de manière similaire au débogage local.

## Fonctionnalités des IDE pour le débogage

La plupart des environnements de développement intégrés (IDE) pour Python, tels que PyCharm, Visual Studio Code et Jupyter Notebooks, sont dotés de puissantes fonctionnalités de débogage. Celles-ci incluent des points d'arrêt visuels, l'inspection de variables et l'exécution pas à pas. Utilisez ces fonctionnalités pour rationaliser votre processus de débogage.

### Points d'arrêt visuels :

Les points d'arrêt (breakpoints) sont des marqueurs qui suspendent l'exécution de votre programme Python à une ligne de code spécifique, vous permettant d'inspecter les variables, d'évaluer des expressions et de comprendre le flux de votre programme à ce point précis.

-   **PyCharm :** Cliquez simplement dans la marge gauche à côté du numéro de ligne où vous souhaitez définir le point d'arrêt.
-   **Visual Studio Code :** Cliquez dans la marge gauche ou utilisez le raccourci `F9`.
-   **IDLE :** Vous pouvez ajouter la ligne `import pdb; pdb.set_trace()` à l'emplacement souhaité.

![image-101](https://www.freecodecamp.org/news/content/images/2024/01/image-101.png)

Aperçu d'un point d'arrêt (point rouge) dans PyCharm

Une fois le point d'arrêt défini, lancez votre programme en mode débogage pour arrêter l'exécution à cet endroit précis.

### Parcours du code (Stepping) :

Après avoir atteint un point d'arrêt, vous pouvez parcourir votre code ligne par ligne. Trois options courantes sont disponibles :

-   **Step Into (F7) :** Passe à la ligne de code suivante et entre dans les appels de fonction si applicable.
-   **Step Over (F8) :** Exécute la ligne de code actuelle et s'arrête à la ligne suivante, sans entrer dans les appels de fonction.
-   **Step Out (Shift + F8) :** Termine l'exécution de la fonction actuelle et s'arrête à la fonction appelante.

![image-119](https://www.freecodecamp.org/news/content/images/2024/01/image-119.png)

Options de parcours du code

Les débogueurs dans les IDE vous permettent d'exécuter votre code étape par étape. Ce contrôle fin vous aide à tracer le flux de votre programme et à identifier l'emplacement exact d'un problème.

Les Jupyter Notebooks supportent cette fonctionnalité à l'aide de commandes magiques telles que `%debug` qui vous permet de déboguer une cellule de manière interactive.

### Exploration de la pile d'appels (Call Stack) :

Les IDE fournissent généralement une pile d'appels qui montre la hiérarchie des appels de fonctions menant au point actuel du code. C'est précieux pour comprendre le flux d'exécution et particulièrement utile lors de la manipulation d'applications complexes.

PyCharm, par exemple, affiche la pile d'appels dans la fenêtre de l'outil de débogage.

### Inspection des variables :

L'inspection des variables est cruciale pour comprendre comment les données changent pendant l'exécution du programme. Les IDE fournissent un panneau "Variables" où vous pouvez voir l'état actuel des variables. Survolez simplement une variable ou consultez l'onglet Variables pour voir sa valeur actuelle.

-   **PyCharm :** Utilise un volet "Variables" dédié pendant le débogage.
-   **Visual Studio Code :** Propose l'inspection des variables dans les volets "Watch" (Espion) et "Variables".
-   **IDLE :** Vous permet de taper les noms des variables dans la console interactive pendant le débogage.

L'inspection des variables est cruciale pour comprendre comment les données évoluent au cours de l'exécution du programme.

### Points d'arrêt conditionnels :

En plus des points d'arrêt standard, certains IDE vous permettent de définir des points d'arrêt avec des conditions. Cela signifie que le débogueur ne s'arrêtera que si une condition spécifiée est remplie.

-   **PyCharm :** Faites un clic droit sur un point d'arrêt et définissez des conditions.
-   **Visual Studio Code :** Faites un clic droit sur un point d'arrêt, sélectionnez "Edit Breakpoint" et définissez une condition.
-   **IDLE :** Utilisez la bibliothèque `pdb` pour définir des points d'arrêt conditionnels dans votre code.

![hitCount--1-](https://www.freecodecamp.org/news/content/images/2024/01/hitCount--1-.gif)

Aperçu illustrant le processus de définition d'un point d'arrêt conditionnel dans PyCharm

### Expressions espionnes (Watch Expressions) :

Les expressions espionnes vous permettent de surveiller des variables ou expressions spécifiques en continu pendant l'exécution. C'est utile pour garder un œil sur certaines valeurs sans les inspecter manuellement à chaque point d'arrêt.

-   **PyCharm :** Ajoutez des expressions au volet "Watches" pour les surveiller tout au long du débogage.
-   **Visual Studio Code :** Utilisez le volet "Watch" pour ajouter des expressions à surveiller en continu.
-   **IDLE :** À un point d'arrêt, tapez des expressions dans la console interactive pour observer leurs valeurs.

En utilisant les expressions espionnes, vous pouvez suivre l'évolution de variables spécifiques et identifier des motifs ou des changements inattendus pendant l'exécution.

Les IDE fournissent d'autres outils à des fins de débogage tels que :

-   Le "Python Profiler" dans VSCode et le profileur intégré de PyCharm comme **outils de profilage.**
-   "Code With Me" dans PyCharm et des extensions comme "Live Share" dans VSCode pour le **débogage collaboratif.**

## Débogage de performance :

### Linters et analyseurs de code

Les linters et les analyseurs statiques sont des outils qui aident à identifier les problèmes potentiels dans votre code en analysant le code source sans l'exécuter. Ils peuvent détecter des erreurs de programmation courantes, imposer des standards de codage et fournir des suggestions d'amélioration.

Ici, nous allons parler de deux de ces outils – PyLint et mypy – pour voir comment les installer et comment ils fonctionnent.

#### Comment installer PyLint :

```
pip install pylint
```

Lancez `pylint` sur votre script ou module Python à l'aide de cette commande :

```
pylint your_script.py
```

Lorsque vous lancez PyLint, il génère un rapport détaillé avec des informations sur les problèmes potentiels, les violations des conventions de codage et d'autres analyses. La sortie inclut un score pour votre code, ainsi que des messages indiquant les domaines à améliorer.

PyLint peut être personnalisé pour répondre aux besoins spécifiques de votre projet. Vous pouvez créer un fichier de configuration (généralement nommé `.pylintrc`) pour définir vos préférences. Ce fichier peut être placé à la racine de votre projet. Ex :

```
[MASTER]
enable = all

[MESSAGES CONTROL]
disable = missing-docstring
```

Dans cet exemple, nous activons toutes les vérifications sauf celle concernant les docstrings manquantes. Vous pouvez adapter la configuration à votre style de codage et aux exigences du projet.

#### Comment installer mypy :

```
pip install mypy
```

Lancez `mypy` sur votre script ou module Python avec cette commande :

```
mypy your_script.py
```

Mypy vérifiera votre code pour détecter les problèmes liés aux types et fournira des retours sur les éventuelles incompatibilités de types et les violations des annotations de type.

Mypy est particulièrement utile lorsque vous utilisez des annotations de type dans votre code Python. Il vérifie que les types que vous spécifiez correspondent à l'utilisation réelle des variables, fonctions et autres éléments.

Discutons également d'autres formateurs de code.

### flake8

flake8 combine trois outils principaux :

1.  **PyFlakes :** Cet outil effectue une analyse statique pour trouver des erreurs dans votre code Python sans l'exécuter.
2.  **pycodestyle :** Anciennement connu sous le nom de pep8, cet outil vérifie votre code par rapport au guide de style PEP 8.
3.  **McCabe :** Ce vérificateur de complexité identifie les blocs de code complexes qui pourraient être difficiles à comprendre ou à maintenir.

#### Comment installer flake8 :

```
pip install flake8
```

Comme pour PyLint, vous pouvez lancer flake8 sur votre code Python en exécutant la commande suivante dans votre terminal :

```
flake8 your_file.py 
#Remplacez your_file.py par le nom réel de votre fichier Python.
```

flake8 peut être configuré selon vos besoins. Vous pouvez créer un fichier de configuration (généralement nommé `.flake8`) dans le répertoire racine de votre projet. Ex.

```
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

Dans cet exemple, nous fixons la longueur maximale de ligne à 88 caractères et étendons la liste des erreurs ignorées.

### Black

Black est un formateur de code "opinionated" (intransigeant) qui automatise les décisions de formatage pour un code cohérent et lisible.

Black possède un ensemble de règles de formatage et les applique de manière constante, ce qui élimine les débats sur le style de code au sein des équipes de développement.

Vous pouvez installer Black avec cette commande :

```
pip install black
```

Et voici comment l'utiliser :

```
black your_file.py
```

Black complète les linters traditionnels comme PyLint et flake8. Vous pouvez utiliser ces outils en combinaison pour garantir à la fois la qualité du code et un formatage cohérent.

De nombreux éditeurs populaires comme Visual Studio Code, Atom et Sublime Text disposent d'extensions ou de plugins qui vous permettent d'utiliser les résultats de ces linters et analyseurs directement dans l'éditeur pendant que vous écrivez.

### Profilage

Le profilage consiste à analyser les performances de votre code pour identifier les goulots d'étranglement et les zones pouvant être optimisées. Python fournit des outils intégrés et des bibliothèques externes pour le profilage, aidant les développeurs à obtenir des informations sur le temps d'exécution et l'utilisation des ressources.

-   **Identifier les problèmes de performance :** Le profilage vous permet de localiser les sections de votre code qui consomment le plus de temps et de ressources.
-   **Optimiser le code :** Une fois les goulots d'étranglement identifiés, les développeurs peuvent se concentrer sur l'optimisation de fonctions ou de blocs de code spécifiques.
-   **Analyse de l'utilisation de la mémoire :** Les outils de profilage peuvent également aider à analyser la consommation de mémoire, facilitant la détection des fuites de mémoire.

Python est livré avec des modules intégrés pour le profilage de base. Les deux modules principaux sont `cProfile` and `profile`.

#### **1**. cProfile:****

`cProfile` est un module intégré qui fournit un profilage déterministe des programmes Python. Il enregistre le temps que chaque fonction prend pour s'exécuter.

**Exemple :**

```Python
import cProfile

def example_function():
    # Votre code ici

if __name__ == "__main__":
    cProfile.run('example_function()')
```

Cela affichera un rapport détaillé des appels de fonctions, leur temps d'exécution et le pourcentage du temps total passé dans chaque fonction.

#### **2**. profile:****

Le module `profile` est similaire à `cProfile` mais est implémenté en pur Python. Il fournit une analyse plus détaillée des appels de fonctions et peut être utilisé lorsqu'un profilage plus fin est nécessaire.

```Python
import profile

def example_function():
    # Votre code ici

if __name__ == "__main__":
    profile.run('example_function()')
```

`cProfile` et `profile` produisent des sorties similaires, mais le premier est généralement préféré pour son impact moindre sur les performances.

### Comment visualiser les résultats du profilage :

Bien que les modules intégrés fournissent des rapports textuels, la visualisation des résultats peut faciliter l'analyse. Un outil populaire pour cela est `snakeviz`.

#### ****Installer snakeviz :****

```
pip install snakeviz
```

#### ****Utiliser snakeviz :****

```Python
import cProfile
import snakeviz

def example_function():
    # Votre code ici

if __name__ == "__main__":
    cProfile.run('example_function()', 'profile_results')
    snakeviz.view('profile_results')
```

Cela ouvrira une fenêtre de navigateur affichant une visualisation interactive des résultats du profilage.

### Techniques de profilage avancées :

Bien que les outils intégrés offrent des informations précieuses, des techniques plus avancées et des bibliothèques externes peuvent fournir des données supplémentaires.

#### ****Profilage par ligne (Line Profiling) :****

Le profilage par ligne vous permet de voir combien de temps est passé sur chaque ligne de code au sein d'une fonction. Le module `line_profiler` est couramment utilisé à cette fin.

#### Installer line\_profiler :

```
pip install line_profiler
```

#### Utiliser line\_profiler :

```Python
from line_profiler import LineProfiler

def example_function():
    # Votre code ici

if __name__ == "__main__":
    profiler = LineProfiler()
    profiler.add_function(example_function)

    profiler.run('example_function()')

    # Afficher les résultats
    profiler.print_stats()
```

Cela affichera un rapport détaillé avec le temps passé sur chaque ligne dans `example_function`.

#### Profilage de la mémoire :

Comprendre l'utilisation de la mémoire est crucial pour optimiser le code. Le module `memory_profiler` aide à profiler la consommation de mémoire.

#### Installer memory\_profiler :

```
pip install memory-profiler
```

#### Utiliser memory\_profiler :

```Python
from memory_profiler import profile

@profile
def example_function():
    # Votre code ici

if __name__ == "__main__":
    example_function()
```

Une fois exécuté, cela affichera une analyse ligne par ligne de l'utilisation de la mémoire pendant l'exécution de `example_function`.

Bien que ces techniques couvrent un large éventail de scénarios, il est important de noter que le débogage le plus efficace implique souvent une combinaison de ces méthodes.

# Quelques conseils supplémentaires pour un débogage efficace :

-   **Contrôle de version et Git Bisect :** Tirez parti des fonctionnalités de votre système de contrôle de version pour suivre les modifications et revenir à des versions fonctionnelles si nécessaire. Si le bug a été introduit récemment, l'utilisation de `git bisect` peut vous aider à identifier le commit exact responsable du problème.
-   **Documentation et commentaires de code** : Écrire du code bien documenté et des commentaires aide à comprendre le but de fonctions ou blocs de code spécifiques, rendant le débogage plus simple pour vous et pour les autres.
-   **Décomposer les problèmes complexes** : Divisez les gros blocs de code en fonctions plus petites et testables pour faciliter le débogage et la maintenance.
-   **Faire des pauses** : S'éloigner et revenir avec un regard neuf permet souvent de révéler des solutions qui n'étaient pas apparentes auparavant.
-   **Débogage du canard en plastique (Rubber Duck Debugging)** : C'est comme une séance de thérapie pour votre code, sauf que le thérapeute est un canard en plastique. Imaginez que vous êtes bloqué sur un problème de code ardu. Au lieu de demander de l'aide à une personne, vous parlez à un canard en plastique. Vous expliquez votre code au canard, ligne par ligne. Même si le canard ne répond pas, quelque chose de magique se produit : en expliquant votre problème à voix haute, vous commencez à voir la solution par vous-même.

# Comment rechercher des solutions aux bugs et erreurs

## 1\. Stratégies de recherche efficaces :

-   ****Comprendre le message d'erreur :**** Commencez par bien comprendre le message d'erreur ou la description du bug. Identifiez les termes clés et les codes d'erreur à utiliser dans votre recherche.
-   **Inclure les détails du contexte** : par exemple, le système d'exploitation, le numéro de version du logiciel, les bibliothèques ou les frameworks avec lesquels vous travaillez. Les bugs et les solutions peuvent varier d'une version à l'autre.
-   ****Guillemets :**** Utilisez des guillemets pour rechercher une expression exacte. C'est utile pour rechercher des messages d'erreur spécifiques ou des extraits de code.
-   ****Utiliser des mots-clés descriptifs :**** Utilisez des mots-clés spécifiques liés à l'erreur. Incluez les langages de programmation, les frameworks et les technologies pertinentes. Dans la mesure du possible, incluez des extraits de code dans votre requête de recherche.

## 2\. Exploiter les ressources web :

-   ****Dépôts GitHub :**** Recherchez dans les dépôts GitHub des problèmes similaires. De nombreux projets ont des gestionnaires de tickets (issue trackers) où les utilisateurs discutent des problèmes et des solutions.
-   ****Documentation et manuels :**** Consultez la documentation officielle des technologies que vous utilisez. Parfois, la réponse s'y trouve directement.
-   ****Recherches spécifiques à un site :**** Utilisez l'opérateur "site:" pour effectuer une recherche au sein d'un site web ou d'un domaine spécifique (ex: `site:stackoverflow.com`).
-   Quelques forums/sites utiles : Stack Overflow, discussions GitHub, Reddit et autres communautés de développeurs. Ces plateformes hébergent souvent des discussions sur les bugs courants.

Même si vous ne trouvez pas de correspondance exacte, des problèmes similaires peuvent fournir des pistes. Si vous ne trouvez aucune solution, envisagez de poster votre problème sur les forums pertinents.

La résolution de bugs peut exiger de la patience. Soyez persévérant et essayez différentes requêtes de recherche, surtout si le problème est complexe.

# Conclusion

Dans ce manuel de débogage, nous avons exploré les messages d'erreur courants, appris des stratégies de recherche efficaces et découvert l'utilité pratique des instructions print.

Le débogage fait partie intégrante du processus de développement logiciel. C'est un art qui demande de la patience, de la persévérance et de la résolution de problèmes. En employant une combinaison d'instructions print, de logging, d'outils de débogage intégrés et d'utilitaires tiers, vous pouvez identifier et résoudre efficacement les problèmes dans votre code Python.

Développer de bonnes habitudes de débogage et exploiter les outils disponibles vous fera non seulement gagner du temps, mais améliorera également la qualité globale et la fiabilité de vos programmes.

[1]: #heading-messages-d-erreur-de-code-courants
[2]: #heading-1-syntaxerror-invalid-syntax
[3]: #heading-2-indentationerror-unexpected-indent
[4]: #heading-3-nameerror-name-variable-is-not-defined
[5]: #heading-4-attributeerror-module-object-has-no-attribute-attribute_name-
[6]: #heading-5-filenotfounderror-errno-2-no-such-file-or-directory-filename-
[7]: #heading-6-indexerror-list-index-out-of-range
[8]: #heading-7-importerror-no-module-named-module_name-
[9]: #heading-8-typeerror-
[10]: #heading-9-valueerror-
[11]: #heading-comment-deboguer-du-code-python
[12]: #heading-techniques-de-debogage-fondamentales
[13]: #heading-instructions-print
[14]: #heading-logging
[15]: #heading-gestion-des-exceptions
[16]: #heading-assertions
[17]: #heading-techniques-de-debogage-avancees
[18]: #heading-tests-unitaires
[19]: #heading-comment-utiliser-le-debogueur-interactif-pdb
[20]: #heading-debogage-a-distance
[21]: #heading-debogage-de-performance
[22]: #heading-linters-et-analyseurs-de-code
[23]: #heading-profilage
[24]: #heading-fonctionnalites-des-ide-pour-le-debogage
[25]: #heading-quelques-conseils-supplementaires-pour-un-debogage-efficace
[26]: #heading-comment-rechercher-des-solutions-aux-bugs-et-erreurs
[27]: #heading-1-strategies-de-recherche-efficaces
[28]: #heading-2-exploiter-les-ressources-web
[29]: #heading-comment-deboguer-du-code-python
[30]: https://www.samyakinfo.tech/blog/logging-in-python