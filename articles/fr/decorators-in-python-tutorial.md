---
title: Qu'est-ce que les Décorateurs en Python ? Expliqué avec des Exemples de Code
subtitle: ''
author: Samyak Jain
co_authors: []
series: null
date: '2024-06-18T18:53:30.000Z'
originalURL: https://freecodecamp.org/news/decorators-in-python-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/decorators-in-python.jpg
tags:
- name: decorator
  slug: decorator
- name: Python
  slug: python
seo_title: Qu'est-ce que les Décorateurs en Python ? Expliqué avec des Exemples de
  Code
seo_desc: 'In this tutorial, you will learn about Python decorators: what they are,
  how they work, and when to use them.

  Table of Contents


  Foundation for Decorators

  [Introduction to Python Decorators](#Introduction to Python Decorators)

  Creating Simple Decorat...'
---

Dans ce tutoriel, vous apprendrez tout sur les décorateurs Python : ce qu'ils sont, comment ils fonctionnent et quand les utiliser.

## **Table des Matières**

1. [Fondation pour les Décorateurs](#heading-fondation-pour-les-decorateurs)
2. [Introduction aux Décorateurs Python](#heading-introduction-aux-decorateurs-python)
3. [Création de Décorateurs Simples](#heading-creons-un-decorateur-simple)  
– [Application des Décorateurs aux Fonctions](#heading-application-des-decorateurs-aux-fonctions)  
– [Utilisation de la Syntaxe @ pour les Décorateurs](#heading-utilisation-de-la-syntaxe-pour-les-decorateurs)
4. [Comment Gérer les Fonctions avec Arguments](#heading-comment-gerer-les-fonctions-avec-arguments)
5. [Utilisation des Classes comme Décorateurs](#heading-comment-utiliser-les-classes-comme-decorateurs)
6. [Bonnes Pratiques pour Utiliser les Décorateurs](#heading-bonnes-pratiques-pour-utiliser-les-decorateurs)
7. [Applications Pratiques des Décorateurs](#heading-applications-pratiques-des-decorateurs)
8. [Conclusion](#heading-conclusion)

Les décorateurs sont un moyen puissant et élégant d'étendre le comportement des fonctions ou méthodes sans modifier leur code source. Mais avant de plonger dans les décorateurs, il est utile de comprendre deux concepts fondamentaux en Python : les fonctions de première classe et les fermetures.

## Fondation pour les Décorateurs

### Fonctions de Première Classe en Python

Les fonctions de première classe signifient que les fonctions en Python sont traitées comme n'importe quel autre objet. Cela implique que les fonctions peuvent être :

* Passées comme arguments à d'autres fonctions.
* Retournées par d'autres fonctions.
* Assignées à des variables.

### Comprendre les Fermetures

Les fermetures en Python permettent à une fonction de se souvenir de l'environnement dans lequel elle a été créée. Cela signifie que la fonction interne a accès aux variables de la portée locale de la fonction externe, même après que la fonction externe a terminé son exécution.

Regardons un exemple pour comprendre les fermetures :

```python
def outer_func():
    greet = "Bonjour !"

    def inner_func():
        print(greet)

    return inner_func

new_function = outer_func()
new_function()  # Affiche : Bonjour !
new_function()  # Affiche : Bonjour !

```

Dans cet exemple :

* Nous avons `outer_func` qui ne prend aucun paramètre mais a une variable locale `greet`.
* Une `inner_func` est définie dans `outer_func` qui affiche `greet`.
* Lorsque nous appelons `outer_func`, elle retourne `inner_func` mais ne l'exécute pas immédiatement. Nous assignons la fonction retournée à `new_function`. Maintenant, `new_function` peut être appelée plus tard, et elle se souviendra de la variable `greet` de la portée de `outer_func`, affichant "Bonjour !" à chaque appel.

C'est ce qu'est une fermeture : elle se souvient de notre variable `greet` même après que la fonction externe a terminé son exécution.

#### Modification des Fermetures avec des Paramètres

Améliorons notre fermeture en passant un paramètre à `outer_func` au lieu d'utiliser une variable locale :

```python
def outer_func(greet):
    def inner_func():
        print(greet)
    return inner_func

namaste_func = outer_func("Namaste !")
howdy_func = outer_func("Salut !")

namaste_func()  # Affiche : Namaste !
howdy_func()    # Affiche : Salut !

```

Ici :

* `outer_func` prend maintenant un paramètre `greet`.
* La `inner_func` affiche ce `greet`.
* Lorsque nous appelons `outer_func` avec "Namaste !" et "Salut !", elle retourne des fonctions qui se souviennent de ces messages spécifiques.

Voici donc un bref aperçu des fonctions de première classe et des fermetures. Si vous souhaitez en apprendre davantage, vous pouvez lire ce blog complet [ici](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/).

## **Introduction aux Décorateurs Python**

Un décorateur est une fonction qui prend une autre fonction comme argument, ajoute une certaine fonctionnalité, et retourne une nouvelle fonction. Cela vous permet d'"envelopper" une autre fonction pour étendre son comportement (en ajoutant une certaine fonctionnalité avant ou après) sans modifier le code source de la fonction originale.

Voici donc l'exemple de fermeture que nous avons utilisé ci-dessus :

```python
def outer_func(greet):
    def inner_func():
        print(greet)
    return inner_func

```

### Maintenant, regardons un Exemple de Décorateur :

```python
def decorator_function(func):
    def wrapper_function():
        return func()
    return wrapper_function

```

Ici, au lieu d'une valeur (comme `greet`), nous acceptons une fonction (`func`) comme argument. Dans notre `wrapper_function`, au lieu de simplement afficher un message, nous allons exécuter cette `func` puis la retourner.

### Application des Décorateurs aux Fonctions

Voici comment nous pouvons appliquer notre décorateur à une fonction simple :

```python
def decorator_function(func):
    def wrapper_function():
        return func()
    return wrapper_function

def display():
    print('La fonction display a été appelée')

decorated_display = decorator_function(display)
decorated_display()  # Affiche : La fonction display a été appelée

```

Dans cet exemple :

* Nous définissons une fonction simple `display` qui affiche un message.
* Nous appliquons le `decorator_function` à `display`, créant une nouvelle variable `decorated_display`.
* Lorsque nous appelons `decorated_display()`, il exécute la `wrapper_function` à l'intérieur de notre décorateur, qui à son tour appelle et retourne la fonction `display`.

### Utilisation de la Syntaxe @ pour les Décorateurs

Python fournit une manière plus lisible d'appliquer les décorateurs en utilisant le symbole `@`. Cette syntaxe est plus facile à comprendre et est couramment utilisée dans le code Python :

```python
def decorator_function(func):
    def wrapper_function():
        print(f'Wrapper exécuté avant {func.__name__}')
        return func()
    return wrapper_function

@decorator_function
def display():
    print('La fonction display a été appelée')

display()  # Affiche : Wrapper exécuté avant display
           #          La fonction display a été appelée

```

Ici :

* Nous utilisons `@decorator_function` comme décorateur au-dessus de la définition de la fonction `display`, ce qui est équivalent à `display = decoratorFunction(display)`.
* Maintenant, lorsque nous appelons `display()`, il passe automatiquement par le décorateur, affichant d'abord le message supplémentaire.

## Comment Gérer les Fonctions avec Arguments

Le décorateur que nous avons écrit jusqu'à présent ne fonctionnera pas si notre fonction originale prend des arguments. Par exemple, considérons la fonction suivante :

```python
def display_info(name, age):
    print('display_info a été appelée avec ({}, {})'.format(name, age))

display_info('Kalam', 83)  # Affiche : display_info a été appelée avec (Kalam, 83)

```

Si nous essayons d'appliquer notre décorateur actuel à `display_info`, il générera une erreur car la `wrapperFunction` ne prend aucun argument mais la fonction originale en attend deux.

### Modification du Décorateur pour Gérer les Arguments

Nous pouvons modifier notre décorateur pour accepter n'importe quel nombre d'arguments positionnels et de mots-clés en utilisant `*args` et `**kwargs`.

```python
import functools

def decoratorFunction(func):
    @functools.wraps(func)
    def wrapperFunction(*args, **kwargs):
        print('Wrapper exécuté avant {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapperFunction

@decoratorFunction
def display():
    print('La fonction display a été appelée')

@decoratorFunction
def display_info(name, age):
    print('display_info a été appelée avec ({}, {})'.format(name, age))

display_info('Kalam', 83)  
display()                        
```

Dans ce décorateur mis à jour :

* `wrapperFunction` accepte maintenant n'importe quel nombre d'arguments positionnels (`*args`) et de mots-clés (`**kwargs`).
* Ces arguments sont passés à `func` lorsqu'il est appelé à l'intérieur de `wrapperFunction`.

La sortie de ceci sera :

```
Wrapper exécuté avant display_info
display_info a été appelée avec (Kalam, 83)
Wrapper exécuté avant display
La fonction display a été appelée
```

Cette configuration rend notre décorateur suffisamment flexible pour gérer n'importe quelle fonction, indépendamment de ses paramètres.

Au fait, remarquez comment nous avons ajouté une nouvelle fonctionnalité à deux fonctions différentes (`display()` et `display_info()`) sans les modifier ? C'est l'un des principaux avantages des décorateurs : ils nous permettent d'étendre le comportement de plusieurs fonctions de manière DRY (Don't Repeat Yourself), comme démontré dans cet exemple.

## Comment Utiliser les Classes comme Décorateurs

Bien que les décorateurs basés sur des fonctions soient courants, vous pouvez également utiliser des classes pour créer des décorateurs. L'utilisation de classes comme décorateurs peut offrir plus de flexibilité et de lisibilité, surtout pour les décorateurs complexes.

Pour vous aider à mieux les comprendre, nous allons transformer un décorateur basé sur une fonction en un décorateur basé sur une classe :

### Décorateur Basé sur une Fonction Original

Commençons par un décorateur basé sur une fonction simple :

```python
def decoratorFunction(func):
    def wrapperFunction(*args, **kwargs):
        print('Wrapper exécuté avant l\'appel de {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapperFunction

```

### Création d'un Décorateur Basé sur une Classe

Pour transformer ce décorateur basé sur une fonction en un décorateur basé sur une classe, suivez ces étapes :

**Étape 1 : Définir la Classe**  
Tout d'abord, nous définissons une nouvelle classe appelée `DecoratorClass`. Cette classe gérera le processus de décoration.

```python
class DecoratorClass:
    pass

```

**Étape 2 : Implémenter la Méthode `__init__`**  
La méthode `__init__` est une méthode spéciale qui initialise l'objet lorsqu'une instance de la classe est créée.  
Ensuite, nous passons la fonction à décorer (`func`) comme argument à la méthode `__init__` et la stockons dans une variable d'instance `self.func`.

```python
class DecoratorClass:
    def __init__(self, func):
        self.func = func

```

**Étape 3 : Implémenter la Méthode `__call__`**  
La méthode `__call__` est une méthode spéciale qui permet à une instance de la classe d'être appelée comme une fonction. Cette méthode est essentielle car elle gère la logique de décoration réelle. Dans ce cas :

* La méthode `__call__` prend `*args` et `**kwargs` pour gérer n'importe quel nombre d'arguments positionnels et de mots-clés.
* À l'intérieur de `__call__`, nous affichons un message puis appelons la fonction originale avec ses arguments.

```python
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Exécution du wrapper avant {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)

```

### Utilisation du Décorateur Basé sur une Classe

Nous pouvons maintenant utiliser la syntaxe `@` pour appliquer le décorateur basé sur une classe aux fonctions, tout comme nous l'avons fait avec le décorateur basé sur une fonction.

```python
@DecoratorClass
def display():
    print('fonction display exécutée')

@DecoratorClass
def display_info(name, age):
    print('fonction display_info exécutée avec les arguments ({}, {})'.format(name, age))

```

### Exécution des Fonctions Décorées

Lorsque nous appelons les fonctions décorées, la méthode `__call__` de `DecoratorClass` est exécutée :

```python
display_info('Kalam', 83)
display()

```

### Exemple Complet

Voici l'exemple complet avec les décorateurs basés sur une classe :

```python
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Exécution du wrapper avant {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)

@DecoratorClass
def display():
    print('fonction display exécutée')

@DecoratorClass
def display_info(name, age):
    print('fonction display_info exécutée avec les arguments ({}, {})'.format(name, age))

display_info('Kalam', 83)
display()

```

Dans ce décorateur basé sur une classe :

* **Méthode `__init__` :** Cette méthode lie la fonction originale à une instance de la classe.
* **Méthode `__call__` :** Cette méthode permet à une instance de `DecoratorClass` d'être appelée comme une fonction. Elle affiche un message puis appelle la fonction originale avec les arguments fournis.
* **Décoration des Fonctions :** Nous utilisons la syntaxe `@DecoratorClass` pour décorer les fonctions `display` et `display_info`.
* **Exécution :** Lorsque `display_info('Kalam', 83)` est appelée, la méthode `__call__` de `DecoratorClass` est exécutée, affichant le message puis exécutant `display_info`. De même, lorsque `display()` est appelée, elle exécute la méthode `__call__`, affiche le message, puis exécute `display`.

Les décorateurs basés sur des fonctions et ceux basés sur des classes fournissent la même fonctionnalité. Le choix entre eux dépend des préférences personnelles et de la complexité de la logique du décorateur.

## Bonnes Pratiques pour Utiliser les Décorateurs

Lors de l'utilisation de décorateurs en Python, il est essentiel de suivre les bonnes pratiques pour maintenir un code propre et maintenable, conforme aux conventions Python.

#### 1. Préserver les Métadonnées des Fonctions avec `functools.wraps`

Lorsque vous créez un décorateur, les métadonnées de la fonction originale (comme son nom, sa docstring et son module) sont souvent perdues. Cela peut entraîner des confusions et des problèmes avec l'introspection, la documentation et le débogage. Pour préserver ces métadonnées, utilisez le décorateur `functools.wraps` dans votre fonction wrapper.

`functools.wraps` a été introduit dans Python 2.5 dans le cadre du module `functools`, qui fournit des fonctions d'ordre supérieur et des opérations sur des objets appelables. Le décorateur `wraps` est spécifiquement conçu pour mettre à jour la fonction wrapper afin qu'elle ressemble davantage à la fonction enveloppée en copiant des attributs tels que le nom de la fonction, le module et la docstring (oui, vous avez deviné juste - `functools.wraps()` est lui-même un décorateur). 

Regardons un exemple :

```python
import functools

def decoratorFunction(func):
    @functools.wraps(func)
    def wrapperFunction(*args, **kwargs):
        print(f'Wrapper exécuté avant {func.__name__}')
        return func(*args, **kwargs)
    return wrapperFunction

@decoratorFunction
def display():
    """Docstring de la fonction display"""
    print('La fonction display a été appelée')

print(display.__name__)   # Affiche : display
print(display.__doc__)    # Affiche : Docstring de la fonction display

```

Dans cet exemple, `@functools.wraps(func)` est utilisé pour s'assurer que la `wrapperFunction` conserve les métadonnées originales de `func`.

#### 2. Gardez les Décorateurs Simples et Ciblés

Un décorateur doit avoir une seule responsabilité et ne doit pas essayer de faire trop de choses. Si un décorateur devient complexe, envisagez de le décomposer en plusieurs décorateurs plus simples qui peuvent être composés ensemble. Exemple :

```python
import functools

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Appel de {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} a pris {end - start} secondes')
        return result
    return wrapper

@log_function_call
@measure_time
def compute_square(n):
    return n * n

print(compute_square(5))

```

Dans cet exemple, `log_function_call` et `measure_time` sont des décorateurs simples et à responsabilité unique qui peuvent être composés pour ajouter à la fois la journalisation et la mesure du temps à `compute_square`. C'est ce que font les décorateurs : fournir un moyen propre et lisible de mettre en œuvre des motifs courants comme la journalisation et la mesure du temps.

#### 3. Utilisez des Noms Descriptifs pour les Décorateurs et les Fonctions Enveloppées

Choisissez des noms clairs et descriptifs pour vos décorateurs et les fonctions qu'ils enveloppent afin qu'ils indiquent clairement leur fonctionnalité. Cela rend le but et le comportement du code plus apparents. 

#### 4. Documentez Vos Décorateurs

Documentez toujours vos décorateurs, en expliquant leur but et comment ils doivent être utilisés. Cela est particulièrement important si d'autres personnes utiliseront vos décorateurs ou si vous travaillez en équipe.

## Applications Pratiques des Décorateurs

Maintenant, vous vous demandez peut-être : "D'accord, les décorateurs sont élégants et tout, mais comment et où les utilisons-nous réellement ?" Eh bien, voici quelques applications pratiques :

* **Journalisation des Appels de Fonctions** :  
La journalisation est une exigence courante pour suivre l'utilisation des fonctions et des méthodes, en particulier dans les applications de débogage et de surveillance.
* **Mesure du Temps d'Exécution des Fonctions** :  
Les décorateurs peuvent mesurer le temps qu'il faut pour qu'une fonction s'exécute, ce qui est utile pour l'analyse des performances.

Nous avons vu ces deux exemples ci-dessus dans la [section des bonnes pratiques](#heading-2-gardez-les-decorateurs-simples-et-cibles).

Au-delà de ces utilisations courantes, il existe d'autres cas d'utilisation tels que :

* **Validation des Entrées** :  
Les décorateurs peuvent être utilisés pour valider les entrées des fonctions, en s'assurant qu'elles répondent à certains critères avant que la fonction ne procède.
* **Mémoïsation** :  
La fonction `memoize` est un décorateur qui aide à mettre en cache (stocker) les résultats des appels de fonctions coûteuses et à réutiliser le résultat mis en cache lorsque les mêmes entrées se produisent à nouveau. Cette technique est appelée mémoïsation et elle est utile pour optimiser les performances, en particulier pour les fonctions récursives comme le calcul des nombres de Fibonacci.

```python
from functools import wraps

def validate_non_negative(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("Les arguments doivent être non négatifs")
        return func(*args, **kwargs)
    return wrapper

@validate_non_negative
def square_root(x):
    return x ** 0.5

print(square_root(4))

```

```python
import functools

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)
```

Exécutez [cette fonction](https://gist.github.com/theSamyak/09a54ed5a6cc0380ee34a1a527f2c9e8) pour voir la différence de temps lors de l'exécution de la fonction Fibonacci avec ou sans mémoïsation.

* **Contrôle d'Accès et Authentification** :  
Dans les applications web, le contrôle d'accès et l'authentification sont cruciaux pour la sécurité. Les décorateurs peuvent être utilisés pour faire respecter les permissions des utilisateurs, en s'assurant que seuls les utilisateurs autorisés peuvent accéder à certaines fonctions ou points de terminaison.

```python
from functools import wraps

def requires_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user_is_logged_in():
            raise Exception("L'utilisateur n'est pas connecté")
        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_dashboard():
    return "Contenu du tableau de bord"

# user_is_logged_in est un espace réservé pour la fonction de vérification d'authentification réelle.

```

## Conclusion

Les décorateurs en Python fournissent un moyen propre et puissant d'étendre le comportement des fonctions. En comprenant les fonctions de première classe et les fermetures, vous pouvez saisir comment les décorateurs fonctionnent sous le capot.

Que vous utilisiez des décorateurs basés sur des fonctions ou des classes, vous pouvez améliorer vos fonctions sans altérer leur code original, en gardant votre base de code propre et maintenable.

* Les décorateurs sont puissants pour étendre la fonctionnalité des fonctions.
* Ils peuvent être implémentés en utilisant des fonctions ou des classes.
* La syntaxe `@decorator` est une manière plus propre et plus lisible d'appliquer les décorateurs.
* Ils aident à garder votre code DRY (Don't Repeat Yourself) en abstraisant les fonctionnalités communes.

**Merci d'avoir lu !** Si vous avez des commentaires, des critiques ou des questions, n'hésitez pas à tweeter ou à me contacter à @[OGsamyak](https://x.com/OGsamyak). Vos retours m'aident à m'améliorer !