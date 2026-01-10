---
title: Le Guide des Décorateurs Python
subtitle: ''
author: Atharva Shah
co_authors: []
series: null
date: '2024-01-26T17:17:03.000Z'
originalURL: https://freecodecamp.org/news/the-python-decorator-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/The-Python-Decorator-Handbook-Cover.png
tags:
- name: decorator
  slug: decorator
- name: handbook
  slug: handbook
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Le Guide des Décorateurs Python
seo_desc: 'Python decorators provide an easy yet powerful syntax for modifying and
  extending the behavior of functions in your code.

  A decorator is essentially a function that takes another function, augments its
  functionality, and returns a new function – with...'
---

Les décorateurs Python offrent une syntaxe facile mais puissante pour modifier et étendre le comportement des fonctions dans votre code.

Un décorateur est essentiellement une fonction qui prend une autre fonction, augmente sa fonctionnalité et retourne une nouvelle fonction – sans modifier définitivement la fonction originale elle-même.

Ce tutoriel vous guidera à travers 11 décorateurs pratiques pour vous aider à ajouter des fonctionnalités comme le chronométrage de l'exécution, la mise en cache, la limitation de débit, le débogage et plus encore. Que vous souhaitiez profiler les performances, améliorer l'efficacité, valider les données ou gérer les erreurs, ces décorateurs vous couvrent !

Les exemples ici se concentrent sur les motifs d'utilisation courants et les utilitaires des décorateurs qui peuvent s'avérer pratiques dans votre programmation quotidienne et vous faire économiser beaucoup d'efforts. Comprendre la flexibilité des décorateurs vous aidera à écrire un code d'application propre, résilient et optimisé.

## Table des Matières

Voici les décorateurs couverts dans ce tutoriel :

* [Journaliser les Arguments et la Valeur de Retour d'une Fonction](#heading-journaliser-les-arguments-et-la-valeur-de-retour-dune-fonction)

* [Obtenir le Temps d'Exécution d'une Fonction](#heading-obtenir-le-temps-dexecution-dune-fonction)

* [Convertir la Valeur de Retour de la Fonction en un Type de Données Spécifié](#heading-convertir-la-valeur-de-retour-de-la-fonction-en-un-type-de-donnees-specifie)

* [Mettre en Cache les Résultats de la Fonction](#heading-mettre-en-cache-les-resultats-de-la-fonction)

* [Valider les Arguments de la Fonction en Fonction de la Condition](#heading-valider-les-arguments-de-la-fonction-en-fonction-de-la-condition)

* [Réessayer une Fonction Plusieurs Fois en Cas d'Échec](#heading-reessayer-une-fonction-plusieurs-fois-en-cas-dechec)

* [Appliquer des Limites de Débit à une Fonction](#heading-appliquer-des-limites-de-debit-a-une-fonction)

* [Gérer les Exceptions et Fournir une Réponse par Défaut](#heading-gerer-les-exceptions-et-fournir-une-reponse-par-defaut)

* [Appliquer la Vérification de Type sur les Arguments de la Fonction](#heading-appliquer-la-verification-de-type-sur-les-arguments-de-la-fonction)

* [Mesurer l'Utilisation de la Mémoire d'une Fonction](#heading-mesurer-lutilisation-de-la-memoire-dune-fonction)

* [Mettre en Cache les Résultats de la Fonction avec un Temps d'Expiration](#heading-mettre-en-cache-les-resultats-de-la-fonction-avec-un-temps-dexpiration)

* [Conclusion](#heading-conclusion)

Mais d'abord, une petite introduction.

## Comment Fonctionnent les Décorateurs Python

Avant de plonger, comprenons quelques avantages clés des décorateurs en Python :

* **Améliorer les fonctions sans modifications invasives** : Les décorateurs augmentent les fonctions de manière transparente sans altérer le code original, gardant la logique centrale propre et maintenable.

* **Réutiliser la fonctionnalité à travers différents endroits** : Des capacités communes comme la journalisation, la mise en cache et la limitation de débit peuvent être construites une fois dans les décorateurs et appliquées où nécessaire.

* **Syntaxe lisible et déclarative** : La syntaxe `@decorateur` communique simplement l'amélioration de la fonctionnalité au site de définition.

* **Modularité et séparation des préoccupations** : Les décorateurs promeuvent un couplage lâche entre la logique fonctionnelle et les capacités secondaires comme la performance, la sécurité, la journalisation, etc.

Le point à retenir est que les décorateurs déverrouillent des moyens simples mais flexibles d'améliorer de manière transparente les fonctions Python pour une meilleure organisation du code, une meilleure efficacité et une meilleure réutilisation sans introduire de complexité ou de redondance.

Voici un exemple de base de la syntaxe des décorateurs en Python avec des annotations :

```python
# Fonction décorateur
def my_decorator(func):

# Fonction wrapper
    def wrapper():
        print("Avant l'appel de la fonction") # Traitement supplémentaire avant la fonction
        func() # Appel de la fonction réelle décorée
        print("Après l'appel de la fonction") # Traitement supplémentaire après la fonction
    return wrapper # Retourne la fonction wrapper imbriquée

# Fonction à décorer
def my_function():
    print("À l'intérieur de ma fonction")

# Appliquer le décorateur sur la fonction
@my_decorator
def my_function():
    print("À l'intérieur de ma fonction")

# Appeler la fonction décorée
my_function()
```

Un décorateur en Python est une fonction qui prend une autre fonction comme argument et étend son comportement sans la modifier. La fonction décorateur enveloppe la fonction originale en définissant une fonction wrapper à l'intérieur. Cette fonction wrapper exécute du code avant et après l'appel de la fonction originale.

Plus précisément, lors de la définition d'une fonction décorateur telle que `my_decorator` dans l'exemple, elle prend une fonction comme argument, que nous appelons généralement `func`. Cette `func` sera la fonction réelle qui est décorée en coulisses.

La fonction wrapper à l'intérieur de `my_decorator` peut exécuter un code arbitraire avant et après l'appel de `func()`, qui invoque la fonction originale. Lorsque vous appliquez `@my_decorator` avant la définition de `my_function`, il passe `my_function` comme argument à `my_decorator`, donc func fait référence à `my_function` dans ce contexte.

La fonction wrapper retourne ensuite la fonction enveloppée améliorée. Ainsi, `my_function` a été décorée par `my_decorator`. Lorsqu'elle est appelée plus tard, le code wrapper à l'intérieur de `my_decorator` s'exécute avant et après que `my_function` ne s'exécute. Cela permet aux décorateurs d'étendre de manière transparente le comportement d'une fonction, sans avoir besoin de modifier la fonction elle-même.

Et comme vous vous en souviendrez, la fonction `my_function` originale reste inchangée, gardant les décorateurs non invasifs et flexibles.

Lorsque `my_function()` est décorée avec `@my_decorator`, elle est automatiquement améliorée. La fonction `my_decorator` ici retourne une fonction wrapper. Cette fonction wrapper est exécutée lorsque `my_function()` est appelée maintenant.

Tout d'abord, le wrapper imprime `"Avant l'appel de la fonction"` avant d'appeler réellement la fonction `my_function()` originale décorée. Ensuite, après que `my_function()` s'exécute, il imprime `"Après l'appel de la fonction"`.

Ainsi, un comportement supplémentaire et des messages imprimés sont ajoutés avant et après l'exécution de `my_function()` dans le wrapper, sans modifier directement `my_function()` elle-même. Le décorateur vous permet d'étendre `my_function()` de manière transparente sans affecter sa logique centrale, car le wrapper gère le comportement amélioré.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-109.png align="left")

*Application d'un Décorateur à une Fonction*

Alors commençons à explorer les 11 décorateurs pratiques que tout développeur Python devrait connaître.

## Journaliser les Arguments et la Valeur de Retour d'une Fonction

Le décorateur Journaliser les Arguments et la Valeur de Retour suit les paramètres d'entrée et la sortie des fonctions. Cela supporte le débogage en journalisant un enregistrement clair du flux de données à travers des opérations complexes.

```python
def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        print(f"Appel de {original_function.__name__} avec args: {args}, kwargs: {kwargs}")

        # Appeler la fonction originale
        result = original_function(*args, **kwargs)

        # Journaliser la valeur de retour
        print(f"{original_function.__name__} a retourné: {result}")

        # Retourner le résultat
        return result
    return wrapper

# Exemple d'utilisation
@log_decorator
def calculate_product(x, y):
    return x * y

# Appeler la fonction décorée
result = calculate_product(10, 20)
print("Résultat:", result)
```

**Sortie:**

```javascript
Appel de calculate_product avec args: (10, 20), kwargs: {}
calculate_product a retourné: 200
Résultat: 200
```

Dans cet exemple, la fonction décorateur est nommée `log_decorator()` et accepte une fonction, `original_function`, comme argument. À l'intérieur de `log_decorator()`, une fonction imbriquée appelée `wrapper()` est définie. Cette fonction `wrapper()` est ce que le décorateur retourne et remplace effectivement la fonction originale.

Lorsque la fonction `wrapper()` est invoquée, elle imprime des déclarations de journalisation concernant l'appel de la fonction. Ensuite, elle appelle la fonction originale, `original_function`, capture son résultat, imprime le résultat, et retourne le résultat.

La syntaxe `@log_decorator` au-dessus de la fonction `calculate_product()` est une convention Python pour appliquer le `log_decorator` comme décorateur à la fonction `calculate_product`. Ainsi, lorsque `calculate_product()` est invoquée, elle appelle en réalité la fonction `wrapper()` retournée par `log_decorator()`. Par conséquent, `log_decorator()` agit comme un wrapper, introduisant des déclarations de journalisation avant et après l'exécution de la fonction `calculate_product()` originale.

### Utilisation et Applications

Ce décorateur est largement adopté dans le développement d'applications pour ajouter une journalisation à l'exécution sans interférer avec l'implémentation de la logique métier.

Par exemple, considérons une application bancaire qui traite les transactions financières. La logique de traitement des transactions principales réside dans des fonctions comme `transfer_funds()` et `accept_payment()`. Pour surveiller ces transactions, la journalisation peut être ajoutée en incluant `@log_decorator` au-dessus de chaque fonction.

Ensuite, lorsque les transactions sont déclenchées en appelant `transfer_funds()`, vous pouvez imprimer le nom de la fonction, les arguments comme l'expéditeur, le destinataire et le montant avant le transfert réel. Ensuite, après que la fonction retourne, vous pouvez imprimer si le transfert a réussi ou échoué.

Ce type de journalisation avec des décorateurs vous permet de suivre les transactions sans ajouter de code aux fonctions principales comme `transfer_funds()`. La logique reste propre tandis que la débogabilité et l'observabilité s'améliorent. Les messages de journalisation peuvent être dirigés vers un tableau de bord de surveillance ou un système d'analyse de journaux également.

## Obtenir le Temps d'Exécution d'une Fonction

Ce décorateur est votre allié dans la quête d'optimisation des performances. En mesurant et en journalisant le temps d'exécution d'une fonction, ce décorateur facilite une plongée profonde dans l'efficacité de votre code, vous aidant à identifier les goulots d'étranglement et à rationaliser les performances de votre application.

Il est idéal pour les scénarios où la vitesse est cruciale, comme les applications en temps réel ou le traitement de données à grande échelle. Et il vous permet d'identifier et de traiter les goulots d'étranglement de performance de manière systématique.

```python
import time

def measure_execution_time(func):
    def timed_execution(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        end_timestamp = time.time()
        execution_duration = end_timestamp - start_timestamp
        print(f"La fonction {func.__name__} a pris {execution_duration:.2f} secondes pour s'exécuter")
        return result
    return timed_execution

# Exemple d'utilisation
@measure_execution_time
def multiply_numbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Appeler la fonction décorée
result = multiply_numbers([i for i in range(1, 10)])
print(f"Résultat: {result}")
```

**Sortie:**

```javascript
La fonction multiply_numbers a pris 0.00 secondes pour s'exécuter
Résultat: 362880
```

Ce code présente un décorateur conçu pour mesurer la durée d'exécution des fonctions.

Le décorateur `measure_execution_time()` prend une fonction, `func`, et définit une fonction interne, `timed_execution()`, pour envelopper la fonction originale. Lors de l'invocation, `timed_execution()` enregistre l'heure de début, appelle la fonction originale, enregistre l'heure de fin, calcule la durée et l'imprime.

La syntaxe `@measure_execution_time` applique ce décorateur aux fonctions en dessous, comme `multiply_numbers()`. Par conséquent, lorsque `multiply_numbers()` est appelée, elle invoque le wrapper `timed_execution()`, qui journalise la durée ainsi que le résultat de la fonction.

Cet exemple illustre comment les décorateurs augmentent de manière transparente les fonctions existantes avec des fonctionnalités supplémentaires, comme le chronométrage, sans modification directe.

### Utilisation et Applications

Ce décorateur est utile pour profiler les fonctions afin d'identifier les goulots d'étranglement de performance dans les applications. Par exemple, considérons un site de commerce électronique avec plusieurs fonctions backend comme `get_recommendations()`, `calculate_shipping()`, etc. En les décorant avec `@measure_execution_time`, vous pouvez surveiller leur temps d'exécution.

Lorsque `get_recommendations()` est invoquée dans une session utilisateur, le décorateur chronométrera sa durée d'exécution en enregistrant un horodatage de début et de fin. Après l'exécution, il imprimera le temps pris avant de retourner les recommandations.

Faire cela de manière systématique à travers les applications et analyser les sorties vous montrera les fonctions qui prennent un temps anormalement long. L'équipe de développement peut alors optimiser ces fonctions par la mise en cache, le traitement parallèle et d'autres techniques pour améliorer les performances globales de l'application.

Sans de tels décorateurs de chronométrage, trouver des candidats à l'optimisation nécessiterait des ajouts fastidieux de code de journalisation. Les décorateurs fournissent une visibilité facilement sans contaminer la logique métier.

## Convertir la Valeur de Retour de la Fonction en un Type de Données Spécifié

Le décorateur Convertir le Type de Valeur de Retour améliore la cohérence des données dans les fonctions en convertissant automatiquement la valeur de retour en un type de données spécifié, favorisant la prévisibilité et prévenant les erreurs inattendues. Il est particulièrement utile pour les processus en aval qui nécessitent des types de données cohérents, réduisant les erreurs d'exécution.

```python
def convert_to_data_type(target_type):
    def type_converter_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return target_type(result)
        return wrapper
    return type_converter_decorator

@convert_to_data_type(int)
def add_values(a, b):
    return a + b

int_result = add_values(10, 20)
print("Résultat:", int_result, type(int_result))

@convert_to_data_type(str)
def concatenate_strings(str1, str2):
    return str1 + str2

str_result = concatenate_strings("Python", " Decorator")
print("Résultat:", str_result, type(str_result))
```

**Sortie:**

```javascript
Résultat: 30 <class 'int'>
Résultat: Python Decorator <class 'str'>
```

L'exemple de code ci-dessus montre un décorateur conçu pour convertir la valeur de retour d'une fonction en un type de données spécifié.

Le décorateur, nommé `convert_to_data_type()`, prend le type de données cible comme paramètre et retourne un décorateur nommé `type_converter_decorator()`. À l'intérieur de ce décorateur, une fonction `wrapper()` est définie pour appeler la fonction originale, convertir sa valeur de retour au type cible en utilisant `target_type()`, et retourner ensuite le résultat converti.

La syntaxe `@convert_to_data_type(int)` appliquée au-dessus d'une fonction (comme `add_values()`) utilise ce décorateur pour convertir la valeur de retour en un entier. De même, pour `concatenate_strings()`, en passant `str`, elle formate la valeur de retour en tant que chaîne.

Cet exemple montre également comment les décorateurs modifient de manière transparente les sorties des fonctions aux formats souhaités sans altérer la logique principale des fonctions.

### Utilisation et Application

Ce décorateur de transformation de valeur de retour est utile dans les applications où vous devez adapter automatiquement les fonctions aux formats de données attendus.

Par exemple, vous pourriez l'utiliser dans une API météo qui retourne les températures par défaut au format décimal comme 23,456 degrés. Mais l'application front-end du consommateur attend une valeur entière à afficher.

Au lieu de changer la fonction de l'API pour retourner un entier, il suffit de la décorer avec `@convert_to_data_type(int)`. Cela convertira de manière transparente la température décimale en l'entier `23`, dans cet exemple, avant de la retourner à l'application cliente. Sans aucune modification de la fonction de l'API, vous avez reformatté la valeur de retour.

De même, pour le traitement backend attendant du JSON, les valeurs de retour peuvent être converties en utilisant le décorateur `@convert_to_data_type(json)`. La logique principale reste inchangée tandis que le format de présentation s'adapte en fonction des besoins de votre cas d'utilisation. Cela évite la duplication du code de gestion des formats à travers les fonctions.

Les décorateurs imposent de manière externe les représentations de données requises pour une intégration et une réutilisation transparentes à travers les couches de l'application avec des formats incompatibles.

## Mettre en Cache les Résultats de la Fonction

Ce décorateur optimise les performances en stockant et en récupérant les résultats des fonctions, éliminant les calculs redondants pour les entrées répétées et améliorant la réactivité de l'application, en particulier pour les calculs chronophages.

```python
def cached_result_decorator(func):
    result_cache = {}

    def wrapper(*args, **kwargs):
        cache_key = (*args, *kwargs.items())

        if cache_key in result_cache:
            return f"[FROM CACHE] {result_cache[cache_key]}"

        result = func(*args, **kwargs)
        result_cache[cache_key] = result

        return result

    return wrapper

# Exemple d'utilisation

@cached_result_decorator
def multiply_numbers(a, b):
    return f"Product = {a * b}"

# Appeler la fonction décorée plusieurs fois
print(multiply_numbers(4, 5))  # Le calcul est effectué
print(multiply_numbers(4, 5))  # Le résultat est récupéré depuis le cache
print(multiply_numbers(5, 7))  # Le calcul est effectué
print(multiply_numbers(5, 7))  # Le résultat est récupéré depuis le cache
print(multiply_numbers(-3, 7))  # Le calcul est effectué
print(multiply_numbers(-3, 7))  # Le résultat est récupéré depuis le cache
```

**Sortie:**

```javascript
Product = 20
[FROM CACHE] Product = 20
Product = 35
[FROM CACHE] Product = 35
Product = -21
[FROM CACHE] Product = -21
```

Cet exemple de code présente un décorateur conçu pour mettre en cache et réutiliser efficacement les résultats des appels de fonction.

La fonction `cached_result_decorator()` prend une autre fonction et retourne un wrapper. À l'intérieur de ce wrapper, un dictionnaire de cache (`result_cache`) stocke les paramètres d'appel uniques et leurs résultats correspondants.

Avant d'exécuter la fonction réelle, le `wrapper()` vérifie si le résultat pour les paramètres actuels est déjà dans le cache. Si c'est le cas, il récupère et retourne le résultat mis en cache – sinon, il appelle la fonction, stocke le résultat dans le cache et le retourne.

La syntaxe `@cached_result_decorator` applique cette logique de mise en cache à toute fonction, telle que `multiply_numbers()`. Cela garantit que, lors des appels ultérieurs avec les mêmes arguments, le résultat mis en cache est réutilisé, évitant ainsi les calculs redondants.

En essence, le décorateur améliore la fonctionnalité en optimisant les performances grâce à la mise en cache des résultats.

### Utilisation et Applications

Les décorateurs de mise en cache comme celui-ci sont extrêmement utiles dans le développement d'applications pour optimiser les performances des appels de fonction répétitifs.

Par exemple, considérons un moteur de recommandation appelant des fonctions de modèle prédictif pour générer des suggestions utilisateur. `get_user_recommendations()` prépare les données d'entrée et les alimente dans le modèle pour chaque demande utilisateur. Au lieu de réexécuter les calculs, il peut être décoré avec `@cached_result_decorator` pour introduire une couche de mise en cache.

Maintenant, la première fois que des paramètres utilisateur uniques sont passés, le modèle s'exécute et le résultat est mis en cache. Les appels suivants avec les mêmes entrées retournent directement les sorties du modèle mises en cache, en sautant le recalcul du modèle.

Cela améliore considérablement la latence pour répondre aux demandes des utilisateurs en évitant les inférences de modèle en double. Vous pouvez surveiller les taux de succès du cache pour justifier la réduction des coûts d'infrastructure du serveur de modèle.

Le découplage de telles préoccupations d'optimisation par le biais de décorateurs de mise en cache plutôt que de les mélanger à l'intérieur de la logique de fonction améliore la modularité, la lisibilité et permet des gains de performance rapides. Les caches seront configurés, invalidés séparément sans intruder dans les fonctions métier.

## Valider les Arguments de la Fonction en Fonction de la Condition

Celui-ci vérifie si les arguments d'entrée répondent à des critères prédéfinis avant l'exécution, améliorant la fiabilité de la fonction et prévenant les comportements inattendus. Il est utile pour les paramètres nécessitant des entiers positifs ou des chaînes non vides.

```python
def check_condition_positive(value):
    def argument_validator(func):
        def validate_and_calculate(*args, **kwargs):
            if value(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Arguments invalides passés à la fonction")
        return validate_and_calculate
    return argument_validator

@check_condition_positive(lambda x: x > 0)
def compute_cubed_result(number):
    return number ** 3

print(compute_cubed_result(5))  # Sortie: 125
print(compute_cubed_result(-2))  # Lève ValueError: Arguments invalides passés à la fonction
```

**Sortie:**

```javascript
125Traceback (most recent call last):

  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 16, in <module>
    print(compute_cubed_result(-2))  # Lève ValueError: Arguments invalides passés à la fonction
  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 7, in validate_and_calculate
    raise ValueError("Arguments invalides passés à la fonction")
ValueError: Arguments invalides passés à la fonction
```

Ce code montre comment vous pouvez implémenter un décorateur pour valider les arguments de fonction.

La fonction `check_condition_positive()` est une usine à décorateurs qui génère un décorateur `argument_validator()`. Ce validateur, lorsqu'il est appliqué avec `@check_condition_positive()` au-dessus de la fonction `compute_cubed_result()`, vérifie si la condition (dans ce cas, que l'argument doit être supérieur à 0) est vraie pour les arguments passés.

Si la condition est remplie, la fonction décorée est exécutée – sinon, une exception `ValueError` est levée.

Cet exemple succinct illustre comment les décorateurs servent de mécanisme pour valider les arguments de fonction avant leur exécution, garantissant le respect des conditions spécifiées.

### Utilisation et Applications

De tels décorateurs de validation de paramètres sont extrêmement utiles dans les applications pour aider à faire respecter les règles métier, les contraintes de sécurité, etc.

Par exemple, un système de traitement des réclamations d'assurance aurait une fonction `process_claim()` qui prend des détails comme l'identifiant de la réclamation, le nom de l'approbateur, etc. Certaines règles métier dictent qui peut approuver les réclamations.

Plutôt que d'encombrer la logique de la fonction elle-même, vous pouvez la décorer avec `@check_condition_positive()` qui valide si le rôle de l'approbateur correspond au montant de la réclamation. Si un agent junior essaie d'approuver une réclamation importante (violant ainsi les règles), ce décorateur l'attraperait en levant une exception avant même que `process_claim()` ne s'exécute.

De même, les contraintes de validation des données d'entrée pour la sécurité et la conformité peuvent être imposées sans toucher aux fonctions individuelles. Les décorateurs garantissent de manière externe que les arguments violés n'atteignent jamais les risques de l'application.

Les motifs de validation courants doivent être réutilisés à travers plusieurs fonctions. Cela améliore la sécurité et promeut la séparation des préoccupations en isolant les contraintes du flux logique principal de manière modulaire.

## Réessayer une Fonction Plusieurs Fois en Cas d'Échec

Ce décorateur est pratique lorsque vous souhaitez réessayer automatiquement une fonction après un échec, améliorant ainsi sa résilience dans des situations impliquant des échecs transitoires. Il est utilisé pour les services externes ou les requêtes réseau sujettes à des échecs intermittents.

```python
import sqlite3
import time

def retry_on_failure(max_attempts, retry_delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as error:
                    print(f"Erreur survenue: {error}. Réessai...")
                    time.sleep(retry_delay)
            raise Exception("Nombre maximum de tentatives dépassé. La fonction a échoué.")

        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, retry_delay=2)
def establish_database_connection():
    connection = sqlite3.connect("example.db")
    db_cursor = connection.cursor()
    db_cursor.execute("SELECT * FROM users")
    query_result = db_cursor.fetchall()
    db_cursor.close()
    connection.close()
    return query_result

try:
    retrieved_data = establish_database_connection()
    print("Données récupérées avec succès:", retrieved_data)
except Exception as error_message:
    print(f"Échec de l'établissement de la connexion à la base de données: {error_message}")
```

**Sortie:**

```javascript
Erreur survenue: no such table: users. Réessai...
Erreur survenue: no such table: users. Réessai...
Erreur survenue: no such table: users. Réessai...
Échec de l'établissement de la connexion à la base de données: Nombre maximum de tentatives dépassé. La fonction a échoué.
```

Cet exemple introduit un décorateur conçu pour réessayer les exécutions de fonctions en cas d'échecs. Il a un nombre maximum spécifié de tentatives et un délai entre les réessais.

La fonction `retry_on_failure()` est une usine à décorateurs, prenant des paramètres pour le nombre maximum de réessais et le délai, et retournant un `decorator()` qui gère la logique de réessai.

À l'intérieur de la fonction `wrapper()`, la fonction décorée subit une exécution dans une boucle, tentant un nombre maximum spécifié de fois.

En cas d'exception, elle imprime un message d'erreur, introduit un délai spécifié par `retry_delay`, et réessaie. Si toutes les tentatives échouent, elle lève une exception indiquant que le nombre maximum de tentatives a été dépassé.

Le `@retry_on_failure()` appliqué au-dessus de `establish_database_connection()` intègre cette logique de réessai, permettant jusqu'à 3 réessais avec un délai de 2 secondes entre chaque tentative en cas d'échec de la connexion à la base de données.

Cela démontre l'utilité des décorateurs dans l'incorporation transparente des capacités de réessai sans altérer le code de la fonction principale.

### Utilisation et Application

Ce décorateur de réessai peut s'avérer extrêmement utile dans le développement d'applications pour ajouter de la résilience contre les erreurs temporaires ou intermittentes.

Par exemple, une application de réservation de vols qui appelle une API de passerelle de paiement `process_payment()` pour gérer les transactions des clients. Parfois, des pics réseau ou des charges élevées du côté du fournisseur de paiement pourraient causer des erreurs transitoires dans la réponse de l'API.

Plutôt que de montrer directement les échecs aux clients, la fonction `process_payment()` peut être décorée avec `@retry_on_failure` pour gérer de tels scénarios de manière implicite. Maintenant, lorsqu'un paiement échoue une fois, il réessayera automatiquement d'envoyer la demande jusqu'à 3 fois avant de finalement signaler l'erreur si elle persiste.

Cela offre une protection contre les petits problèmes temporaires sans exposer les utilisateurs à un comportement d'infrastructure peu fiable directement. L'application reste également disponible de manière fiable même si les services dépendants échouent occasionnellement.

Le décorateur aide à confiner la logique de réessai de manière nette sans la répandre dans le code de l'API. Les échecs hors du contrôle de l'application sont gérés avec grâce plutôt que d'impacter directement les utilisateurs par des défauts d'application. Cela démontre comment les décorateurs apportent une meilleure résilience sans compliquer la logique métier.

## Appliquer des Limites de Débit à une Fonction

En contrôlant la fréquence des fonctions appelées, le décorateur Appliquer des Limites de Débit assure une gestion efficace des ressources et se protège contre les abus. Il est particulièrement utile dans des scénarios comme l'abus d'API ou la conservation des ressources où la restriction des appels de fonction est essentielle.

```python
import time

def rate_limiter(max_allowed_calls, reset_period_seconds):
    def decorate_rate_limited_function(original_function):
        calls_count = 0
        last_reset_time = time.time()

        def wrapper_function(*args, **kwargs):
            nonlocal calls_count, last_reset_time
            elapsed_time = time.time() - last_reset_time

            # Si le temps écoulé est supérieur à la période de réinitialisation, réinitialiser le compteur d'appels
            if elapsed_time > reset_period_seconds:
                calls_count = 0
                last_reset_time = time.time()

            # Vérifier si le compteur d'appels a atteint la limite maximale autorisée
            if calls_count >= max_allowed_calls:
                raise Exception("Limite de débit dépassée. Veuillez réessayer plus tard.")

            # Incrémenter le compteur d'appels
            calls_count += 1

            # Appeler la fonction originale
            return original_function(*args, **kwargs)

        return wrapper_function
    return decorate_rate_limited_function

# Autoriser un maximum de 6 appels API en 10 secondes.
@rate_limiter(max_allowed_calls=6, reset_period_seconds=10)
def make_api_call():
    print("Appel API exécuté avec succès...")

# Faire des appels API
for _ in range(8):
    try:
        make_api_call()
    except Exception as error:
        print(f"Erreur survenue: {error}")
time.sleep(10)
make_api_call()
```

**Sortie:**

```javascript
Appel API exécuté avec succès...
Appel API exécuté avec succès...
Appel API exécuté avec succès...
Appel API exécuté avec succès...
Appel API exécuté avec succès...
Appel API exécuté avec succès...
Erreur survenue: Limite de débit dépassée. Veuillez réessayer plus tard.
Erreur survenue: Limite de débit dépassée. Veuillez réessayer plus tard.
Appel API exécuté avec succès...
```

Ce code montre la mise en œuvre d'un mécanisme de limitation de débit pour les appels de fonction à l'aide d'un décorateur.

La fonction `rate_limiter()`, spécifiée avec un nombre maximum d'appels et une période en secondes pour réinitialiser le compteur, sert de cœur à la logique de limitation de débit. Le décorateur, `decorate_rate_limited_function()`, utilise un wrapper pour gérer les limites de débit en réinitialisant le compteur si la période s'est écoulée. Il vérifie si le compteur a atteint le maximum autorisé, puis lève une exception ou incrémente le compteur et exécute la fonction en conséquence.

Appliqué à `make_api_call()` en utilisant `@rate_limiter()`, il restreint la fonction à six appels dans toute période de 10 secondes. Cela introduit une limitation de débit sans changer la logique de la fonction, garantissant que les appels respectent les limites et empêchant une utilisation excessive dans les intervalles définis.

### Utilisation et Application

Les décorateurs de limitation de débit comme celui-ci sont très utiles dans le développement d'applications pour contrôler l'utilisation des API et prévenir les abus.

Par exemple, une application de réservation de voyages peut dépendre d'une API de recherche de vols tierce pour vérifier la disponibilité des sièges en temps réel auprès des compagnies aériennes. Bien que la plupart des utilisations soient légitimes, certains utilisateurs pourraient potentiellement appeler cette API de manière excessive, dégradant ainsi les performances globales du service.

En décorant le module d'intégration de l'API comme `@rate_limiter(100, 60)`, l'application peut restreindre les appels excessifs en interne également. Cela limiterait le module de réservation à effectuer seulement 100 appels à l'API de vols par minute. Les appels supplémentaires sont rejetés directement par le décorateur sans même atteindre l'API réelle.

Cela permet de préserver le service en aval de l'utilisation excessive, permettant une distribution plus équitable de la capacité pour le fonctionnement général de l'application.

Les décorateurs fournissent un contrôle facile du débit pour les API internes et externes sans changer le code fonctionnel. Cela signifie que vous n'avez pas à tenir compte des quotas d'utilisation tout en protégeant les services, l'infrastructure et en limitant le risque d'adoption. Et tout cela grâce aux contrôles côté application utilisant des wrappers.

## Gérer les Exceptions et Fournir une Réponse par Défaut

Le décorateur Gérer les Exceptions est un filet de sécurité pour les fonctions, gérant les exceptions avec grâce et fournissant des réponses par défaut lorsqu'elles se produisent. Il protège l'application contre les plantages dus à des circonstances imprévues, assurant un fonctionnement fluide.

```python
def handle_exceptions(default_response_msg):
    def exception_handler_decorator(func):
        def decorated_function(*args, **kwargs):
            try:
                # Appeler la fonction originale
                return func(*args, **kwargs)
            except Exception as error:
                # Gérer l'exception et fournir la réponse par défaut
                print(f"Exception survenue: {error}")
                return default_response_msg
        return decorated_function
    return exception_handler_decorator

# Exemple d'utilisation
@handle_exceptions(default_response_msg="Une erreur s'est produite!")
def divide_numbers_safely(dividend, divisor):
    return dividend / divisor

# Appeler la fonction décorée
result = divide_numbers_safely(7, 0)  # Cela lèvera une ZeroDivisionError
print("Résultat:", result)
```

**Sortie:**

```javascript
Exception survenue: division by zero
Résultat: Une erreur s'est produite!
```

Ce code montre la gestion des exceptions dans les fonctions en utilisant des décorateurs.

L'usine à décorateurs `handle_exceptions()`, acceptant une réponse par défaut, produit `exception_handler_decorator()`. Ce décorateur, lorsqu'il est appliqué aux fonctions, tente d'exécuter la fonction originale. Si une exception survient, il imprime les détails de l'erreur et retourne la réponse par défaut spécifiée.

La syntaxe `@handle_exceptions()` au-dessus d'une fonction incorpore cette logique de gestion des exceptions. Par exemple, dans `divide_numbers_safely()`, la division par zéro déclenche une exception, que le décorateur attrape, empêchant un plantage et retournant la réponse par défaut "Une erreur s'est produite!" réponse.

Essentiellement, ces décorateurs capturent habilement les exceptions dans les fonctions, fournissant un moyen transparent d'incorporer une logique de gestion et de prévenir les plantages.

### Utilisation et Applications

Les décorateurs de gestion des exceptions simplifient grandement la gestion des erreurs dans les applications et aident à masquer les comportements peu fiables aux utilisateurs.

Par exemple, un site de commerce électronique peut dépendre des services de paiement, d'inventaire et d'expédition pour finaliser les commandes. Au lieu de blocs d'exception complexes partout, la fonction principale de traitement des commandes comme `place_order()` peut être décorée pour obtenir de la résilience.

Le décorateur `@handle_exceptions` appliqué au-dessus interceptait toute panne de service tiers ou problème intermittent lors de la finalisation de la commande. En cas d'exception, il journalise les erreurs pour le débogage tout en servant un message élégant "La commande a échoué, veuillez réessayer plus tard" à l'utilisateur. Cela évite d'exposer les causes profondes complexes des échecs comme les délais d'attente de paiement à l'utilisateur final.

Les décorateurs protègent les clients des problèmes de service peu fiables sans changer le code métier. Ils fournissent des réponses par défaut conviviales lorsque des erreurs se produisent. Cela améliore l'expérience client

De plus, les décorateurs donnent aux développeurs une visibilité sur ces erreurs en coulisses. Ainsi, ils peuvent se concentrer sur la correction systématique des causes profondes des échecs. Cette séparation des préoccupations par le biais des décorateurs réduit la complexité. Les clients voient plus de fiabilité, et vous obtenez des informations exploitables sur les défauts – tout en gardant la logique métier intacte.

## Appliquer la Vérification de Type sur les Arguments de la Fonction

Le décorateur Appliquer la Vérification de Type garantit l'intégrité des données en vérifiant que les arguments de la fonction sont conformes aux types de données spécifiés, empêchant les erreurs liées aux types et favorisant la fiabilité du code. Il est particulièrement utile dans les situations où le respect strict des types de données est crucial.

```python
import inspect

def enforce_type_checking(func):
    def type_checked_wrapper(*args, **kwargs):
        # Obtenir la signature de la fonction et les noms des paramètres
        function_signature = inspect.signature(func)
        function_parameters = function_signature.parameters

        # Itérer sur les arguments positionnels
        for i, arg_value in enumerate(args):
            parameter_name = list(function_parameters.keys())[i]
            parameter_type = function_parameters[parameter_name].annotation
            if not isinstance(arg_value, parameter_type):
                raise TypeError(f"L'argument '{parameter_name}' doit être de type '{parameter_type.__name__}'")

        # Itérer sur les arguments de mots-clés
        for keyword_name, arg_value in kwargs.items():
            parameter_type = function_parameters[keyword_name].annotation
            if not isinstance(arg_value, parameter_type):
                raise TypeError(f"L'argument '{keyword_name}' doit être de type '{parameter_type.__name__}'")

        # Appeler la fonction originale
        return func(*args, **kwargs)

    return type_checked_wrapper

# Exemple d'utilisation
@enforce_type_checking
def multiply_numbers(factor_1: int, factor_2: int) -> int:
    return factor_1 * factor_2

# Appeler la fonction décorée
result = multiply_numbers(5, 7)  # Pas d'erreurs de type, retourne 35
print("Résultat:", result)

result = multiply_numbers("5", 7)  # Erreur de type: 'factor_1' doit être de type 'int'
```

**Sortie:**

```javascript
Résultat:Traceback (most recent call last):
  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 36, in <module>
 35
    result = multiply_numbers("5", 7)  # Erreur de type: 'factor_1' doit être de type 'int'
  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 14, in type_checked_wrapper
    raise TypeError(f"L'argument '{parameter_name}' doit être de type '{parameter_type.__name__}'")
TypeError: L'argument 'factor_1' doit être de type 'int'
```

Le décorateur `enforce_type_checking` valide si les arguments passés à une fonction correspondent aux annotations de type spécifiées.

À l'intérieur du `type_checked_wrapper`, il examine la signature de la fonction décorée, récupère les noms des paramètres et les annotations de type, et s'assure que les arguments fournis correspondent aux types attendus. Cela inclut la vérification des arguments positionnels par rapport à leur ordre, et des arguments de mots-clés par rapport aux noms des paramètres. Si une incompatibilité de type est détectée, une erreur TypeError est levée.

Ce décorateur est illustré par son application à la fonction `multiply_numbers`, où les arguments sont annotés comme des entiers. Tenter de passer une chaîne entraîne une exception, tandis que le passage d'entiers exécute la fonction sans problème. Cette vérification de type est appliquée sans modifier le corps de la fonction originale.

### Utilisation et Applications

Les décorateurs de vérification de type sont appliqués pour détecter les problèmes tôt et améliorer la fiabilité. Par exemple, considérons un backend d'application web avec une fonction de couche d'accès aux données `get_user_data()` annotée pour attendre des identifiants d'utilisateur entiers. Ses requêtes échoueraient si des identifiants de chaîne circulaient à partir du code frontal.

Plutôt que d'ajouter des vérifications explicites et de lever des exceptions localement, vous pouvez utiliser ce décorateur. Maintenant, tout code en amont ou consommateur passant des types invalides sera automatiquement attrapé pendant l'exécution de la fonction. Le décorateur examine les annotations par rapport aux types d'arguments et lance des erreurs en conséquence avant d'atteindre la couche de base de données.

Cette protection d'exécution pour les composants par le biais de décorateurs garantit que seules les formes de données valides circulent à travers les couches, prévenant les erreurs obscures. La sécurité de type est imposée sans vérifications supplémentaires encombrant une logique plus propre.

## Mesurer l'Utilisation de la Mémoire d'une Fonction

En ce qui concerne les applications intensives en données ou les environnements contraints en ressources, le décorateur Mesurer l'Utilisation de la Mémoire est un détective de mémoire qui offre des informations sur la consommation de mémoire des fonctions. Il le fait en optimisant l'utilisation de la mémoire.

```python
import tracemalloc

def measure_memory_usage(target_function):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        # Appeler la fonction originale
        result = target_function(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")

        # Imprimer les lignes les plus consommatrices de mémoire
        print(f"Utilisation de la mémoire de {target_function.__name__}:")
        for stat in top_stats[:5]:
            print(stat)

        # Retourner le résultat
        return result

    return wrapper

# Exemple d'utilisation
@measure_memory_usage
def calculate_factorial_recursive(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial_recursive(number - 1)

# Appeler la fonction décorée
result_factorial = calculate_factorial_recursive(3)
print("Factorielle:", result_factorial)
```

**Sortie:**

```javascript
Utilisation de la mémoire de calculate_factorial_recursive:
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1552 B, count=6, average=259 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:8: size=896 B, count=3, average=299 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:10: size=416 B, count=1, average=416 B
Utilisation de la mémoire de calculate_factorial_recursive:
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1552 B, count=6, average=259 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:226: size=880 B, count=3, average=293 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:8: size=832 B, count=2, average=416 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:173: size=800 B, count=2, average=400 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:505: size=592 B, count=2, average=296 B
Utilisation de la mémoire de calculate_factorial_recursive:
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1440 B, count=4, average=360 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:535: size=1240 B, count=3, average=413 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:67: size=1216 B, count=19, average=64 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:193: size=1104 B, count=23, average=48 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:226: size=880 B, count=3, average=293 B
Utilisation de la mémoire de calculate_factorial_recursive:
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:558: size=1416 B, count=29, average=49 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:67: size=1408 B, count=22, average=64 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1392 B, count=3, average=464 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:535: size=1240 B, count=3, average=413 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:226: size=832 B, count=2, average=416 B
Factorielle: 6
```

Ce code présente un décorateur, `measure_memory_usage`, conçu pour mesurer la consommation de mémoire des fonctions.

Le décorateur, lorsqu'il est appliqué, initie le suivi de la mémoire avant que la fonction originale ne soit appelée. Une fois que la fonction a terminé son exécution, un instantané de la mémoire est pris et les 5 lignes consommant le plus de mémoire sont imprimées.

Illustré à travers l'exemple de `calculate_factorial_recursive()`, le décorateur vous permet de surveiller l'utilisation de la mémoire sans modifier la fonction elle-même, offrant des informations précieuses à des fins d'optimisation.

En essence, il fournit un moyen simple d'évaluer et d'analyser la consommation de mémoire de toute fonction pendant son temps d'exécution.

### Utilisation et Applications

Les décorateurs de mesure de mémoire comme ceux-ci sont extrêmement précieux dans le développement d'applications pour identifier et résoudre les problèmes de gonflement ou de fuite de mémoire.

Par exemple, considérons un pipeline de streaming de données avec des composants ETL critiques comme `transform_data()` qui traite de grands volumes d'informations. Bien que le processus semble fonctionner correctement pendant les charges régulières, des données de grand volume comme les ventes du Black Friday pourraient causer une utilisation excessive de la mémoire et des plantages.

Plutôt que de déboguer manuellement, décorer les processeurs comme @measure_memory_usage peut révéler des informations utiles. Il imprimera les lignes les plus intensives en mémoire pendant le flux de données de pointe sans aucun changement de code.

Vous devriez viser à identifier les étapes spécifiques qui consomment rapidement de la mémoire et les corriger grâce à de meilleurs algorithmes ou optimisations.

De tels décorateurs aident à intégrer des perspectives de diagnostic dans les chemins critiques pour reconnaître les tendances de consommation anormales tôt. Au lieu de problèmes de production retardés, les problèmes peuvent être identifiés de manière préventive grâce au profilage avant la sortie. Ils réduisent les maux de tête de débogage et minimisent les échecs d'exécution grâce à une instrumentation plus facile pour le suivi de la mémoire.

## Mettre en Cache les Résultats de la Fonction avec un Temps d'Expiration

Spécifiquement conçu pour les données obsolètes, le décorateur Mettre en Cache les Résultats de la Fonction avec un Temps d'Expiration est un outil qui combine la mise en cache avec une fonctionnalité d'expiration basée sur le temps pour s'assurer que les données mises en cache sont régulièrement actualisées afin d'éviter l'obsolescence et de maintenir la pertinence.

```python
import time

def cached_function_with_expiry(expiry_time):
    def decorator(original_function):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())

            if key in cache:
                cached_value, cached_timestamp = cache[key]

                if time.time() - cached_timestamp < expiry_time:
                    return f"[CACHED] - {cached_value}"

            result = original_function(*args, **kwargs)
            cache[key] = (result, time.time())

            return result

        return wrapper

    return decorator

# Exemple d'utilisation

@cached_function_with_expiry(expiry_time=5)  # Temps d'expiration du cache défini à 5 secondes
def calculate_product(x, y):
    return f"PRODUCT - {x * y}"

# Appeler la fonction décorée plusieurs fois
print(calculate_product(23, 5))  # Le calcul est effectué
print(calculate_product(23, 5))  # Le résultat est récupéré depuis le cache
time.sleep(5)
print(calculate_product(23, 5))  # Le calcul est effectué (cache expiré)
```

**Sortie:**

```javascript
PRODUCT - 115
[CACHED] - PRODUCT - 115
PRODUCT - 115
```

Ce code montre un décorateur de mise en cache qui a un temps d'expiration automatique du cache.

La fonction `cached_function_with_expiry()` génère un décorateur qui, lorsqu'il est appliqué, utilise un dictionnaire appelé `cache` pour stocker les résultats des fonctions et leurs horodatages correspondants. La fonction `wrapper()` vérifie si le résultat pour les arguments actuels est dans le cache. Si présent et dans le délai d'expiration, elle retourne le résultat mis en cache – sinon, elle appelle la fonction.

Illustré en utilisant `calculate_product()`, le décorateur calcule et met d'abord en cache le résultat. Les appels suivants récupèrent le résultat mis en cache jusqu'à la période d'expiration, moment auquel le cache est actualisé par un nouveau calcul.

En essence, cette implémentation évite les calculs redondants tout en actualisant automatiquement les résultats après la période d'expiration spécifiée.

### Utilisation et Applications

Les décorateurs de cache avec expiration automatique sont très utiles dans le développement d'applications pour optimiser les performances des modules de récupération de données.

Par exemple, considérons un site de voyage qui appelle l'API backend `get_flight_prices()` pour afficher les prix en direct aux utilisateurs. Bien que les caches réduisent les appels aux sources de données de vols coûteuses, la mise en cache statique conduit à afficher des prix obsolètes.

Au lieu de cela, vous pouvez utiliser `@cached_function_with_expiry(60)` pour actualiser automatiquement toutes les minutes. Maintenant, le premier appel utilisateur récupère les prix en direct et les met en cache, tandis que les demandes suivantes dans une fenêtre de 60 secondes réutilisent efficacement le cache des prix. Mais les caches s'invalident automatiquement après la période d'expiration pour garantir des données fraîches.

Cela vous permet d'optimiser les flux sans vous soucier des cas particuliers liés aux représentations obsolètes. Ce décorateur gère la situation de manière fiable, en gardant les caches synchronisés avec les changements en amont grâce à l'actualisation configurable. Il n'y a aucune redondance des recalculs, et vous obtenez toujours les meilleures informations mises à jour pour les utilisateurs finaux. Les motifs de mise en cache courants sont emballés de manière pratique pour une réutilisation dans la base de code avec des règles d'expiration personnalisées.

## Conclusion

Les décorateurs Python continuent de voir une utilisation généralisée dans le développement d'applications pour insérer proprement des préoccupations transversales courantes. Les authentifications, la surveillance et les restrictions sont quelques exemples standards de cas d'utilisation qui utilisent des décorateurs dans des frameworks comme Django et Flask.

La popularité des API web a également conduit à l'adoption courante de décorateurs de limitation de débit et de mise en cache pour les performances.

Les décorateurs existent depuis les premières versions de Python. Guido van Rossum a écrit sur l'amélioration avec les décorateurs dans un article de 1990 sur Python. Plus tard, lorsque la syntaxe des décorateurs de fonction s'est stabilisée dans Python 2.4 en 2004, cela a ouvert la porte à des solutions élégantes par le biais de la programmation orientée. Du web à la science des données, ils continuent d'alimenter l'abstraction et la modularité à travers les domaines Python.

Les exemples de ce manuel ne font qu'effleurer la surface de ce que des décorateurs sur mesure peuvent permettre. En fonction de tout objectif spécifique comme la sécurité, la limitation des demandes des utilisateurs, le chiffrement transparent, etc., vous pouvez créer des décorateurs innovants pour répondre à vos besoins. Structurer les pipelines de traitement logique en utilisant une composition de décorateurs spécialisés à responsabilité unique encourage également la réutilisation plutôt que la redondance.

Comprendre les décorateurs non seulement améliore les compétences de développement mais déverrouille des moyens de dicter le comportement du programme de manière flexible. Je vous encourage à évaluer les besoins courants dans vos bases de code qui peuvent être abstraits en décorateurs autonomes. Avec un peu de pratique, il devient facile de repérer les préoccupations transversales et d'étendre les fonctions efficacement sans transpirer.

Si vous avez aimé cette leçon et que vous souhaitez explorer plus de contenu technique perspicace, y compris des lectures sur Python, Django et la conception de systèmes, consultez mon [Blog](https://atharvashah.netlify.app). Vous pouvez également voir mes projets avec preuve de travail sur [GitHub](https://github.com/HighnessAtharva) et me connecter sur [LinkedIn](https://www.linkedin.com/in/atharva-shah-5873a2111/) pour discuter.