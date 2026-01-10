---
title: 'Comment fonctionnent les méthodes magiques de Python : Un guide pratique'
subtitle: ''
author: Vivek Sahu
co_authors: []
series: null
date: '2025-03-20T15:27:59.389Z'
originalURL: https://freecodecamp.org/news/python-magic-methods-practical-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742482738702/0b357de2-855d-47c2-960f-453e0bfd9a3d.png
tags:
- name: Python
  slug: python
- name: python magic method
  slug: python-magic-method
- name: dunder method
  slug: dunder-method
- name: Tutorial
  slug: tutorial
- name: Python advanced
  slug: python-advanced
seo_title: 'Comment fonctionnent les méthodes magiques de Python : Un guide pratique'
seo_desc: 'Have you ever wondered how Python makes objects work with operators like
  + or -? Or how it knows how to display objects when you print them? The answer lies
  in Python''s magic methods, also known as dunder (double under) methods.

  Magic methods are spe...'
---

Vous êtes-vous déjà demandé comment Python fait fonctionner les objets avec des opérateurs comme `+` ou `-` ? Ou comment il sait comment afficher les objets lorsque vous les imprimez ? La réponse réside dans les méthodes magiques de Python, également connues sous le nom de méthodes dunder (double underscore).

Les méthodes magiques sont des méthodes spéciales qui vous permettent de définir comment vos objets se comportent en réponse à diverses opérations et fonctions intégrées. Elles sont ce qui rend la programmation orientée objet de Python si puissante et intuitive.

Dans ce guide, vous apprendrez à utiliser les méthodes magiques pour créer un code plus élégant et puissant. Vous verrez des exemples pratiques qui montrent comment ces méthodes fonctionnent dans des scénarios réels.

## Prérequis

* Compréhension de base de la syntaxe Python et des concepts de programmation orientée objet.

* Familiarité avec les classes, les objets et l'héritage.

* Connaissance des types de données intégrés de Python (listes, dictionnaires, etc.).

* Une installation Python 3 fonctionnelle est recommandée pour interagir activement avec les exemples ici.

## **Table des matières**

1. [Qu'est-ce que les méthodes magiques ?](#quest-ce-que-les-methodes-magiques)

2. [Représentation des objets](#representation-des-objets)

   * [**str** vs **repr**](#str-vs-repr)

   * [Exemple pratique : Classe d'erreur personnalisée](#exemple-pratique-classe-derreur-personnalisee)

3. [Surcharge des opérateurs](#surcharge-des-operateurs)

   * [Opérateurs arithmétiques](#operateurs-arithmetiques)

   * [Opérateurs de comparaison](#operateurs-de-comparaison)

   * [Exemple pratique : Classe Money](#exemple-pratique-classe-money)

4. [Méthodes de conteneur](#methodes-de-conteneur)

   * [Protocole de séquence](#protocole-de-sequence)

   * [Protocole de mappage](#protocole-de-mappage)

   * [Exemple pratique : Cache personnalisé](#exemple-pratique-cache-personnalise)

5. [Accès aux attributs](#acces-aux-attributs)

   * [**getattr** et **getattribute**](#getattr-et-getattribute)

   * [**setattr** et **delattr**](#setattr-et-delattr)

   * [Exemple pratique : Propriétés avec journalisation automatique](#exemple-pratique-proprietes-avec-journalisation-automatique)

6. [Gestionnaires de contexte](#gestionnaires-de-contexte)

   * [**enter** et **exit**](#enter-et-exit)

   * [Exemple pratique : Gestionnaire de connexion à la base de données](#exemple-pratique-gestionnaire-de-connexion-a-la-base-de-donnees)

7. [Objets appelables](#objets-appelables)

   * [**call**](#call)

   * [Exemple pratique : Décorateur de mémoisation](#exemple-pratique-decorateur-de-memoisation)

8. [Méthodes magiques avancées](#methodes-magiques-avancees)

   * [**new** pour la création d'objets](#new-pour-la-creation-dobjets)

   * [**slots** pour l'optimisation de la mémoire](#slots-pour-loptimisation-de-la-memoire)

   * [**missing** pour les valeurs par défaut des dictionnaires](#missing-pour-les-valeurs-par-defaut-des-dictionnaires)

9. [Considérations de performance](#considerations-de-performance)

10. [Meilleures pratiques](#meilleures-pratiques)

11. [Conclusion](#heading-conclusion)

12. [Références](#references)

## **Qu'est-ce que les méthodes magiques ?**

Les méthodes magiques de Python sont des méthodes spéciales qui commencent et se terminent par des doubles underscores (`__`). Lorsque vous utilisez certaines opérations ou fonctions sur vos objets, Python appelle automatiquement ces méthodes.

Par exemple, lorsque vous utilisez l'opérateur `+` sur deux objets, Python recherche la méthode `__add__` dans l'opérande de gauche. Si elle la trouve, elle appelle cette méthode avec l'opérande de droite comme argument.

Voici un exemple simple qui montre comment cela fonctionne :

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Cela appelle p1.__add__(p2)
print(p3.x, p3.y)  # Sortie : 4 6
```

Décomposons ce qui se passe ici :

1. Nous créons une classe `Point` qui représente un point dans un espace 2D

2. La méthode `__init__` initialise les coordonnées x et y

3. La méthode `__add__` définit ce qui se passe lorsque nous additionnons deux points

4. Lorsque nous écrivons `p1 + p2`, Python appelle automatiquement `p1.__add__(p2)`

5. Le résultat est un nouveau `Point` avec les coordonnées (4, 6)

Ce n'est que le début. Python a de nombreuses méthodes magiques qui vous permettent de personnaliser le comportement de vos objets dans différentes situations. Explorons certaines des plus utiles.

## **Représentation des objets**

Lorsque vous travaillez avec des objets en Python, vous devez souvent les convertir en chaînes de caractères. Cela se produit lorsque vous imprimez un objet ou essayez de l'afficher dans la console interactive. Python fournit deux méthodes magiques à cet effet : `__str__` et `__repr__`.

### **str vs repr**

Les méthodes `__str__` et `__repr__` servent à des fins différentes :

* `__str__` : Appelée par la fonction `str()` et par la fonction `print()`. Elle doit retourner une chaîne lisible pour les utilisateurs finaux.

* `__repr__` : Appelée par la fonction `repr()` et utilisée dans la console interactive. Elle doit retourner une chaîne qui, idéalement, pourrait être utilisée pour recréer l'objet.

Voici un exemple qui montre la différence :

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __str__(self):
        return f"{self.celsius}\u00b0C"
    
    def __repr__(self):
        return f"Temperature({self.celsius})"

temp = Temperature(25)
print(str(temp))      # Sortie : 25\u00b0C
print(repr(temp))     # Sortie : Temperature(25)
```

Dans cet exemple :

* `__str__` retourne une chaîne conviviale montrant la température avec un symbole de degré

* `__repr__` retourne une chaîne qui montre comment créer l'objet, ce qui est utile pour le débogage

La différence devient claire lorsque vous utilisez ces objets dans différents contextes :

* Lorsque vous imprimez la température, vous voyez la version conviviale : `25\u00b0C`

* Lorsque vous inspectez l'objet dans la console Python, vous voyez la version détaillée : `Temperature(25)`

### **Exemple pratique : Classe d'erreur personnalisée**

Créons une classe d'erreur personnalisée qui fournit de meilleures informations de débogage. Cet exemple montre comment vous pouvez utiliser `__str__` et `__repr__` pour rendre vos messages d'erreur plus utiles :

```python
class ValidationError(Exception):
    def __init__(self, field, message, value=None):
        self.field = field
        self.message = message
        self.value = value
        super().__init__(self.message)
    
    def __str__(self):
        if self.value is not None:
            return f"Erreur dans le champ '{self.field}' : {self.message} (obtenu : {repr(self.value)})"
        return f"Erreur dans le champ '{self.field}' : {self.message}"
    
    def __repr__(self):
        if self.value is not None:
            return f"ValidationError(field='{self.field}', message='{self.message}', value={repr(self.value)})"
        return f"ValidationError(field='{self.field}', message='{self.message}')"

# Utilisation
try:
    age = -5
    if age < 0:
        raise ValidationError("age", "L'âge doit être positif", age)
except ValidationError as e:
    print(e)  # Sortie : Erreur dans le champ 'age' : L'âge doit être positif (obtenu : -5)
```

Cette classe d'erreur personnalisée offre plusieurs avantages :

1. Elle inclut le nom du champ où l'erreur s'est produite

2. Elle montre la valeur réelle qui a causé l'erreur

3. Elle fournit des messages d'erreur à la fois conviviaux et détaillés

4. Elle facilite le débogage en incluant toutes les informations pertinentes

## **Surcharge des opérateurs**

La surcharge des opérateurs est l'une des fonctionnalités les plus puissantes des méthodes magiques de Python. Elle vous permet de définir comment vos objets se comportent lorsqu'ils sont utilisés avec des opérateurs comme `+`, `-`, `*`, et `==`. Cela rend votre code plus intuitif et lisible.

### **Opérateurs arithmétiques**

Python fournit des méthodes magiques pour toutes les opérations arithmétiques de base. Voici un tableau montrant quelle méthode correspond à quel opérateur :

| Opérateur | Méthode magique | Description |
| --- | --- | --- |
| `+` | `__add__` | Addition |
| `-` | `__sub__` | Soustraction |
| `*` | `__mul__` | Multiplication |
| `/` | `__truediv__` | Division |
| `//` | `__floordiv__` | Division entière |
| `%` | `__mod__` | Modulo |
| `**` | `__pow__` | Exponentiation |

### **Opérateurs de comparaison**

De même, vous pouvez définir comment vos objets sont comparés en utilisant ces méthodes magiques :

| Opérateur | Méthode magique | Description |
| --- | --- | --- |
| `==` | `__eq__` | Égal à |
| `!=` | `__ne__` | Différent de |
| `<` | `__lt__` | Inférieur à |
| `>` | `__gt__` | Supérieur à |
| `<=` | `__le__` | Inférieur ou égal à |
| `>=` | `__ge__` | Supérieur ou égal à |

### **Exemple pratique : Classe Money**

Créons une classe `Money` qui gère correctement les opérations de devise. Cet exemple montre comment implémenter plusieurs opérateurs et gérer les cas limites :

```python
from functools import total_ordering
from decimal import Decimal

@total_ordering  # Implémente toutes les méthodes de comparaison basées sur __eq__ et __lt__
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = Decimal(str(amount))
        self.currency = currency
    
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Impossible d'additionner des devises différentes : {self.currency} et {other.currency}")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Impossible de soustraire des devises différentes : {self.currency} et {other.currency}")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Money(self.amount * Decimal(str(other)), self.currency)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Money(self.amount / Decimal(str(other)), self.currency)
        return NotImplemented
    
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.currency == other.currency and self.amount == other.amount
    
    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Impossible de comparer des devises différentes : {self.currency} et {other.currency}")
        return self.amount < other.amount
    
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"
    
    def __repr__(self):
        return f"Money({repr(float(self.amount))}, {repr(self.currency)})"
```

Décomposons les principales caractéristiques de cette classe `Money` :

1. **Gestion de la précision** : Nous utilisons `Decimal` au lieu de `float` pour éviter les problèmes de précision des nombres à virgule flottante dans les calculs monétaires.

2. **Sécurité des devises** : La classe empêche les opérations entre différentes devises pour éviter les erreurs.

3. **Vérification des types** : Chaque méthode vérifie si l'autre opérande est du bon type en utilisant `isinstance()`.

4. **NotImplemented** : Lorsque qu'une opération n'a pas de sens, nous retournons `NotImplemented` pour laisser Python essayer l'opération inverse.

5. **@total_ordering** : Ce décorateur implémente automatiquement toutes les méthodes de comparaison basées sur `__eq__` et `__lt__`.

Voici comment utiliser la classe `Money` :

```python
# Arithmétique de base
wallet = Money(100, "USD")
expense = Money(20, "USD")
remaining = wallet - expense
print(remaining)  # Sortie : USD 80.00

# Travailler avec différentes devises
salary = Money(5000, "USD")
bonus = Money(1000, "USD")
total = salary + bonus
print(total)  # Sortie : USD 6000.00

# Division par un scalaire
weekly_pay = salary / 4
print(weekly_pay)  # Sortie : USD 1250.00

# Comparaisons
print(Money(100, "USD") > Money(50, "USD"))  # Sortie : True
print(Money(100, "USD") == Money(100, "USD"))  # Sortie : True

# Gestion des erreurs
try:
    Money(100, "USD") + Money(100, "EUR")
except ValueError as e:
    print(e)  # Sortie : Impossible d'additionner des devises différentes : USD et EUR
```

Cette classe `Money` démontre plusieurs concepts importants :

1. Comment gérer différents types d'opérandes

2. Comment implémenter une gestion d'erreur appropriée

3. Comment utiliser le décorateur `@total_ordering`

4. Comment maintenir la précision dans les calculs financiers

5. Comment fournir des méthodes de chaîne et de représentation

## **Méthodes de conteneur**

Les méthodes de conteneur vous permettent de faire en sorte que vos objets se comportent comme des conteneurs intégrés tels que des listes, des dictionnaires ou des ensembles. Cela est particulièrement utile lorsque vous avez besoin d'un comportement personnalisé pour stocker et récupérer des données.

### **Protocole de séquence**

Pour faire en sorte que votre objet se comporte comme une séquence (comme une liste ou un tuple), vous devez implémenter ces méthodes :

| Méthode | Description | Exemple d'utilisation |
| --- | --- | --- |
| `__len__` | Retourne la longueur du conteneur | `len(obj)` |
| `__getitem__` | Permet l'indexation avec `obj[key]` | `obj[0]` |
| `__setitem__` | Permet l'assignation avec `obj[key] = value` | `obj[0] = 42` |
| `__delitem__` | Permet la suppression avec `del obj[key]` | `del obj[0]` |
| `__iter__` | Retourne un itérateur pour le conteneur | `for item in obj:` |
| `__contains__` | Implémente l'opérateur `in` | `42 in obj` |

### **Protocole de mappage**

Pour un comportement de type dictionnaire, vous voudrez implémenter ces méthodes :

| Méthode | Description | Exemple d'utilisation |
| --- | --- | --- |
| `__getitem__` | Obtenir la valeur par clé | `obj["key"]` |
| `__setitem__` | Définir la valeur par clé | `obj["key"] = value` |
| `__delitem__` | Supprimer la paire clé-valeur | `del obj["key"]` |
| `__len__` | Obtenir le nombre de paires clé-valeur | `len(obj)` |
| `__iter__` | Itérer sur les clés | `for key in obj:` |
| `__contains__` | Vérifier si la clé existe | `"key" in obj` |

### **Exemple pratique : Cache personnalisé**

Implémentons un cache basé sur le temps qui expire automatiquement les anciennes entrées. Cet exemple montre comment créer un conteneur personnalisé qui se comporte comme un dictionnaire mais avec des fonctionnalités supplémentaires :

```python
import time
from collections import OrderedDict

class ExpiringCache:
    def __init__(self, max_age_seconds=60):
        self.max_age = max_age_seconds
        self._cache = OrderedDict()  # {key: (value, timestamp)}
    
    def __getitem__(self, key):
        if key not in self._cache:
            raise KeyError(key)
        
        value, timestamp = self._cache[key]
        if time.time() - timestamp > self.max_age:
            del self._cache[key]
            raise KeyError(f"La clé '{key}' a expiré")
        
        return value
    
    def __setitem__(self, key, value):
        self._cache[key] = (value, time.time())
        self._cache.move_to_end(key)  # Déplacer à la fin pour maintenir l'ordre d'insertion
    
    def __delitem__(self, key):
        del self._cache[key]
    
    def __len__(self):
        self._clean_expired()  # Nettoyer les éléments expirés avant de rapporter la longueur
        return len(self._cache)
    
    def __iter__(self):
        self._clean_expired()  # Nettoyer les éléments expirés avant l'itération
        for key in self._cache:
            yield key
    
    def __contains__(self, key):
        if key not in self._cache:
            return False
        
        _, timestamp = self._cache[key]
        if time.time() - timestamp > self.max_age:
            del self._cache[key]
            return False
        
        return True
    
    def _clean_expired(self):
        """Supprimer toutes les entrées expirées du cache."""
        now = time.time()
        expired_keys = [
            key for key, (_, timestamp) in self._cache.items()
            if now - timestamp > self.max_age
        ]
        for key in expired_keys:
            del self._cache[key]
```

Décomposons comment ce cache fonctionne :

1. **Stockage** : Le cache utilise un `OrderedDict` pour stocker les paires clé-valeur ainsi que les timestamps.

2. **Expiration** : Chaque valeur est stockée sous forme de tuple `(value, timestamp)`. Lorsque l'on accède à une valeur, nous vérifions si elle a expiré.

3. **Méthodes de conteneur** : La classe implémente toutes les méthodes nécessaires pour se comporter comme un dictionnaire :

   * `__getitem__` : Récupère les valeurs et vérifie l'expiration

   * `__setitem__` : Stocke les valeurs avec le timestamp actuel

   * `__delitem__` : Supprime les entrées

   * `__len__` : Retourne le nombre d'entrées non expirées

   * `__iter__` : Itère sur les clés non expirées

   * `__contains__` : Vérifie si une clé existe

Voici comment utiliser le cache :

```python
# Créer un cache avec une expiration de 2 secondes
cache = ExpiringCache(max_age_seconds=2)

# Stocker quelques valeurs
cache["name"] = "Vivek"
cache["age"] = 30

# Accéder aux valeurs
print("name" in cache)  # Sortie : True
print(cache["name"])    # Sortie : Vivek
print(len(cache))       # Sortie : 2

# Attendre l'expiration
print("Attente de l'expiration...")
time.sleep(3)

# Vérifier les valeurs expirées
print("name" in cache)  # Sortie : False
try:
    print(cache["name"])
except KeyError as e:
    print(f"KeyError : {e}")  # Sortie : KeyError : 'name'

print(len(cache))  # Sortie : 0
```

Cette implémentation de cache offre plusieurs avantages :

1. Expiration automatique des anciennes entrées

2. Interface de type dictionnaire pour une utilisation facile

3. Efficacité mémoire en supprimant les entrées expirées

4. Opérations thread-safe (en supposant un accès monothread)

5. Maintien de l'ordre d'insertion des entrées

## **Accès aux attributs**

Les méthodes d'accès aux attributs vous permettent de contrôler comment vos objets gèrent l'obtention, la définition et la suppression des attributs. Cela est particulièrement utile pour implémenter des propriétés, des validations et des journalisations.

### **getattr et getattribute**

Python fournit deux méthodes pour contrôler l'accès aux attributs :

1. `__getattr__` : Appelée uniquement lorsqu'une recherche d'attribut échoue (c'est-à-dire lorsque l'attribut n'existe pas)

2. `__getattribute__` : Appelée pour chaque accès à un attribut, même pour les attributs qui existent

La différence clé est que `__getattribute__` est appelée pour tous les accès aux attributs, tandis que `__getattr__` n'est appelée que lorsque l'attribut n'est pas trouvé par des moyens normaux.

Voici un exemple simple montrant la différence :

```python
class AttributeDemo:
    def __init__(self):
        self.name = "Vivek"
    
    def __getattr__(self, name):
        print(f"__getattr__ appelé pour {name}")
        return f"Valeur par défaut pour {name}"
    
    def __getattribute__(self, name):
        print(f"__getattribute__ appelé pour {name}")
        return super().__getattribute__(name)

demo = AttributeDemo()
print(demo.name)      # Sortie : __getattribute__ appelé pour name
                      #        Vivek
print(demo.age)       # Sortie : __getattribute__ appelé pour age
                      #        __getattr__ appelé pour age
                      #        Valeur par défaut pour age
```

### **setattr et delattr**

De même, vous pouvez contrôler comment les attributs sont définis et supprimés :

1. `__setattr__` : Appelée lorsqu'un attribut est défini

2. `__delattr__` : Appelée lorsqu'un attribut est supprimé

Ces méthodes vous permettent d'implémenter une validation, une journalisation ou un comportement personnalisé lorsque les attributs sont modifiés.

### **Exemple pratique : Propriétés avec journalisation automatique**

Créons une classe qui journalise automatiquement tous les changements de propriétés. Cela est utile pour le débogage, l'audit ou le suivi des changements d'état des objets :

```python
import logging

# Configurer la journalisation
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LoggedObject:
    def __init__(self, **kwargs):
        self._data = {}
        # Initialiser les attributs sans déclencher __setattr__
        for key, value in kwargs.items():
            self._data[key] = value
    
    def __getattr__(self, name):
        if name in self._data:
            logging.debug(f"Accès à l'attribut {name} : {self._data[name]}")
            return self._data[name]
        raise AttributeError(f"L'objet '{self.__class__.__name__}' n'a pas d'attribut '{name}'")
    
    def __setattr__(self, name, value):
        if name == "_data":
            # Permettre de définir l'attribut _data directement
            super().__setattr__(name, value)
        else:
            old_value = self._data.get(name, "<indéfini>")
            self._data[name] = value
            logging.info(f"Changé {name} : {old_value} -> {value}")
    
    def __delattr__(self, name):
        if name in self._data:
            old_value = self._data[name]
            del self._data[name]
            logging.info(f"Supprimé {name} (était : {old_value})")
        else:
            raise AttributeError(f"L'objet '{self.__class__.__name__}' n'a pas d'attribut '{name}'")
```

Décomposons comment cette classe fonctionne :

1. **Stockage** : La classe utilise un dictionnaire privé `_data` pour stocker les valeurs des attributs.

2. **Accès aux attributs** :

   * `__getattr__` : Retourne les valeurs de `_data` et journalise les messages de débogage

   * `__setattr__` : Stocke les valeurs dans `_data` et journalise les changements

   * `__delattr__` : Supprime les valeurs de `_data` et journalise les suppressions

3. **Gestion spéciale** : L'attribut `_data` lui-même est géré différemment pour éviter la récursion infinie.

Voici comment utiliser la classe :

```python
# Créer un objet journalisé avec des valeurs initiales
user = LoggedObject(name="Vivek", email="hello@wewake.dev")

# Modifier les attributs
user.name = "Vivek"  # Journalise : Changé name : Vivek -> Vivek
user.age = 30         # Journalise : Changé age : <indéfini> -> 30

# Accéder aux attributs
print(user.name)      # Sortie : Vivek

# Supprimer les attributs
del user.email        # Journalise : Supprimé email (était : hello@wewake.dev)

# Essayer d'accéder à un attribut supprimé
try:
    print(user.email)
except AttributeError as e:
    print(f"AttributeError : {e}")  # Sortie : AttributeError : L'objet 'LoggedObject' n'a pas d'attribut 'email'
```

Cette implémentation offre plusieurs avantages :

1. Journalisation automatique de tous les changements d'attributs

2. Journalisation de niveau débogage pour l'accès aux attributs

3. Messages d'erreur clairs pour les attributs manquants

4. Suivi facile des changements d'état des objets

5. Utile pour le débogage et l'audit

## **Gestionnaires de contexte**

Les gestionnaires de contexte sont une fonctionnalité puissante de Python qui vous aide à gérer correctement les ressources. Ils garantissent que les ressources sont correctement acquises et libérées, même si une erreur se produit. L'instruction `with` est le moyen le plus courant d'utiliser les gestionnaires de contexte.

### **enter et exit**

Pour créer un gestionnaire de contexte, vous devez implémenter deux méthodes magiques :

1. `__enter__` : Appelée lors de l'entrée dans le bloc `with`. Elle doit retourner la ressource à gérer.

2. `__exit__` : Appelée lors de la sortie du bloc `with`, même si une exception se produit. Elle doit gérer le nettoyage.

La méthode `__exit__` reçoit trois arguments :

* `exc_type` : Le type de l'exception (si elle existe)

* `exc_val` : L'instance de l'exception (si elle existe)

* `exc_tb` : La trace de la pile (si elle existe)

### **Exemple pratique : Gestionnaire de connexion à la base de données**

Créons un gestionnaire de contexte pour les connexions à la base de données. Cet exemple montre comment gérer correctement les ressources de la base de données et les transactions :

```python
import sqlite3
import logging

# Configurer la journalisation
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        logging.info(f"Connexion à la base de données : {self.db_path}")
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f"Une erreur s'est produite : {exc_val}")
            self.connection.rollback()
            logging.info("Transaction annulée")
        else:
            self.connection.commit()
            logging.info("Transaction validée")
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        
        logging.info("Connexion à la base de données fermée")
        
        # Retourner False pour propager les exceptions, True pour les supprimer
        return False
```

Décomposons comment ce gestionnaire de contexte fonctionne :

1. **Initialisation** :

   * La classe prend un chemin de base de données

   * Elle initialise la connexion et le curseur à None

2. **Méthode Enter** :

   * Crée une connexion à la base de données

   * Crée un curseur

   * Retourne le curseur pour une utilisation dans le bloc `with`

3. **Méthode Exit** :

   * Gère la gestion des transactions (commit/rollback)

   * Ferme le curseur et la connexion

   * Journalise toutes les opérations

   * Retourne False pour propager les exceptions

Voici comment utiliser le gestionnaire de contexte :

```python
# Créer une base de données de test en mémoire
try:
    # Transaction réussie
    with DatabaseConnection(":memory:") as cursor:
        # Créer une table
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)
        
        # Insérer des données
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            ("Vivek", "hello@wewake.dev")
        )
        
        # Interroger les données
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())  # Sortie : [(1, 'Vivek', 'hello@wewake.dev')]
    
    # Démontrer l'annulation de transaction en cas d'erreur
    with DatabaseConnection(":memory:") as cursor:
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            ("Wewake", "contact@wewake.dev")
        )
        # Cela provoquera une erreur - la table 'nonexistent' n'existe pas
        cursor.execute("SELECT * FROM nonexistent")
except sqlite3.OperationalError as e:
    print(f"Exception capturée : {e}")
```

Ce gestionnaire de contexte offre plusieurs avantages :

1. Les ressources sont gérées automatiquement (par exemple, les connexions sont toujours fermées).

2. Sécurité des transactions, les changements sont validés ou annulés de manière appropriée.

3. Les exceptions sont capturées et gérées avec grâce

4. Toutes les opérations sont journalisées pour le débogage

5. L'instruction `with` rend le code clair et concis

## **Objets appelables**

La méthode magique `__call__` vous permet de faire en sorte que les instances de votre classe se comportent comme des fonctions. Cela est utile pour créer des objets qui maintiennent un état entre les appels ou pour implémenter un comportement de type fonction avec des fonctionnalités supplémentaires.

### **call**

La méthode `__call__` est appelée lorsque vous essayez d'appeler une instance de votre classe comme si c'était une fonction. Voici un exemple simple :

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Créer des instances qui se comportent comme des fonctions
double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # Sortie : 10
print(triple(5))  # Sortie : 15
```

Cet exemple montre comment `__call__` vous permet de créer des objets qui maintiennent un état (le facteur) tout en étant appelables comme des fonctions.

### **Exemple pratique : Décorateur de mémoisation**

Implémentons un décorateur de mémoisation en utilisant `__call__`. Ce décorateur mettra en cache les résultats des fonctions pour éviter les calculs redondants :

```python
import time
import functools

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        # Préserver les métadonnées de la fonction (nom, docstring, etc.)
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        # Créer une clé à partir des arguments
        # Pour simplifier, nous supposons que tous les arguments sont hashables
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)
        
        return self.cache[key]

# Utilisation
@Memoize
def fibonacci(n):
    """Calculer le n-ième nombre de Fibonacci de manière récursive."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Mesurer le temps d'exécution
def time_execution(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__}({args}, {kwargs}) a pris {end - start:.6f} secondes")
    return result

# Sans mémoisation, cela serait extrêmement lent
print("Calcul de fibonacci(35)...")
result = time_execution(fibonacci, 35)
print(f"Résultat : {result}")

# Le deuxième appel est instantané grâce à la mémoisation
print("\nCalcul de fibonacci(35) à nouveau...")
result = time_execution(fibonacci, 35)
print(f"Résultat : {result}")
```

Décomposons comment ce décorateur de mémoisation fonctionne :

1. **Initialisation** :

   * Prend une fonction comme argument

   * Crée un dictionnaire de cache pour stocker les résultats

   * Préserve les métadonnées de la fonction en utilisant `functools.update_wrapper`

2. **Méthode Call** :

   * Crée une clé unique à partir des arguments de la fonction

   * Vérifie si le résultat est dans le cache

   * Si ce n'est pas le cas, calcule le résultat et le stocke

   * Retourne le résultat mis en cache

3. **Utilisation** :

   * Appliqué comme un décorateur à n'importe quelle fonction

   * Met automatiquement en cache les résultats pour les appels répétés

   * Préserve les métadonnées et le comportement de la fonction

Les avantages de cette implémentation incluent :

1. Meilleure performance, car elle évite les calculs redondants

2. Meilleure transparence, car elle fonctionne sans modifier la fonction originale

3. Flexible, peut être utilisée avec n'importe quelle fonction

4. Efficace en mémoire, met en cache les résultats pour réutilisation

5. Maintient la documentation des fonctions

## **Méthodes magiques avancées**

Explorons maintenant certaines des méthodes magiques plus avancées de Python. Ces méthodes vous donnent un contrôle fin sur la création d'objets, l'utilisation de la mémoire et le comportement des dictionnaires.

### **new pour la création d'objets**

La méthode `__new__` est appelée avant `__init__` et est responsable de la création et du retour d'une nouvelle instance de la classe. Cela est utile pour implémenter des motifs comme les singletons ou les objets immuables.

Voici un exemple de motif singleton utilisant `__new__` :

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name=None):
        # Cela sera appelé chaque fois que Singleton() est appelé
        if name is not None:
            self.name = name

# Utilisation
s1 = Singleton("Vivek")
s2 = Singleton("Wewake")
print(s1 is s2)  # Sortie : True
print(s1.name)   # Sortie : Wewake (la deuxième initialisation a écrasé la première)
```

Décomposons comment ce singleton fonctionne :

1. **Variable de classe** : `_instance` stocke l'instance unique de la classe

2. **Méthode new** :

   * Vérifie si une instance existe

   * En crée une si elle n'existe pas

   * Retourne l'instance existante si elle existe

3. **Méthode init** :

   * Appelée chaque fois que le constructeur est utilisé

   * Met à jour les attributs de l'instance

### **slots pour l'optimisation de la mémoire**

La variable de classe `__slots__` restreint les attributs qu'une instance peut avoir, économisant ainsi de la mémoire. Cela est particulièrement utile lorsque vous avez de nombreuses instances d'une classe avec un ensemble fixe d'attributs.

Voici une comparaison des classes régulières et slottées :

```python
import sys

class RegularPerson:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class SlottedPerson:
    __slots__ = ['name', 'age', 'email']
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Comparer l'utilisation de la mémoire
regular_people = [RegularPerson("Vivek" + str(i), 30, "hello@wewake.dev") for i in range(1000)]
slotted_people = [SlottedPerson("Vivek" + str(i), 30, "hello@wewake.dev") for i in range(1000)]

print(f"Taille d'une personne régulière : {sys.getsizeof(regular_people[0])} octets")  # Sortie : Taille d'une personne régulière : 48 octets
print(f"Taille d'une personne slottée : {sys.getsizeof(slotted_people[0])} octets")  # Sortie : Taille d'une personne slottée : 56 octets
print(f"Mémoire économisée par instance : {sys.getsizeof(regular_people[0]) - sys.getsizeof(slotted_people[0])} octets")  # Sortie : Mémoire économisée par instance : -8 octets
print(f"Mémoire totale économisée pour 1000 instances : {(sys.getsizeof(regular_people[0]) - sys.getsizeof(slotted_people[0])) * 1000 / 1024:.2f} Ko")  # Sortie : Mémoire totale économisée pour 1000 instances : -7.81 Ko
```

L'exécution de ce code produit un résultat intéressant :

```plaintext
Taille d'une personne régulière : 48 octets
Taille d'une personne slottée : 56 octets
Mémoire économisée par instance : -8 octets
Mémoire totale économisée pour 1000 instances : -7.81 Ko
```

Étonnamment, dans cet exemple simple, l'instance slottée est en fait 8 octets plus grande que l'instance régulière ! Cela semble contredire le conseil commun sur `__slots__` économisant de la mémoire.

Alors, que se passe-t-il ici ? Les vraies économies de mémoire de `__slots__` proviennent de :

1. Élimination des dictionnaires : Les objets Python réguliers stockent leurs attributs dans un dictionnaire (`__dict__`), qui a un surcoût. La fonction `sys.getsizeof()` ne tient pas compte de la taille de ce dictionnaire.

2. Stockage des attributs : Pour les petits objets avec peu d'attributs, le surcoût des descripteurs de slot peut l'emporter sur les économies de dictionnaire.

3. Évolutivité : Le vrai bénéfice apparaît lorsque :

   * Vous avez de nombreuses instances (des milliers ou des millions)

   * Vos objets ont de nombreux attributs

   * Vous ajoutez des attributs dynamiquement

Faisons une comparaison plus complète :

```python
# Une mesure de mémoire plus précise
import sys

def get_size(obj):
    """Obtenir une meilleure estimation de la taille de l'objet en octets."""
    size = sys.getsizeof(obj)
    if hasattr(obj, '__dict__'):
        size += sys.getsizeof(obj.__dict__)
        # Ajouter la taille du contenu du dictionnaire
        size += sum(sys.getsizeof(v) for v in obj.__dict__.values())
    return size

class RegularPerson:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class SlottedPerson:
    __slots__ = ['name', 'age', 'email']
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

regular = RegularPerson("Vivek", 30, "hello@wewake.dev")
slotted = SlottedPerson("Vivek", 30, "hello@wewake.dev")

print(f"Taille complète d'une personne régulière : {get_size(regular)} octets")  # Sortie : Taille complète d'une personne régulière : 610 octets
print(f"Taille complète d'une personne slottée : {get_size(slotted)} octets")  # Sortie : Taille complète d'une personne slottée : 56 octets
```

Avec cette mesure plus précise, vous verrez que les objets slottés utilisent généralement moins de mémoire totale, surtout lorsque vous ajoutez plus d'attributs.

Points clés sur `__slots__` :

1. **Vrais bénéfices de mémoire** : Les principales économies de mémoire proviennent de l'élimination du `__dict__` de l'instance

2. **Restrictions dynamiques** : Vous ne pouvez pas ajouter d'attributs arbitraires aux objets slottés

3. **Considérations d'héritage** : L'utilisation de `__slots__` avec l'héritage nécessite une planification minutieuse

4. **Cas d'utilisation** : Meilleur pour les classes avec de nombreuses instances et des attributs fixes

5. **Bonus de performance** : Peut également fournir un accès plus rapide aux attributs dans certains cas

### **missing pour les valeurs par défaut des dictionnaires**

La méthode `__missing__` est appelée par les sous-classes de dictionnaire lorsqu'une clé n'est pas trouvée. Cela est utile pour implémenter des dictionnaires avec des valeurs par défaut ou une création automatique de clés.

Voici un exemple de dictionnaire qui crée automatiquement des listes vides pour les clés manquantes :

```python
class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]

# Utilisation
groups = AutoKeyDict()
groups["team1"].append("Vivek")
groups["team1"].append("Wewake")
groups["team2"].append("Vibha")

print(groups)  # Sortie : {'team1': ['Vivek', 'Wewake'], 'team2': ['Vibha']}
```

Cette implémentation offre plusieurs avantages :

1. Pas besoin de vérifier si une clé existe, ce qui est plus pratique.

2. Initialisation automatique crée des valeurs par défaut selon les besoins.

3. Réduit le code répétitif pour l'initialisation des dictionnaires.

4. Plus flexible, peut implémenter n'importe quelle logique de valeur par défaut.

5. Ne crée des valeurs que lorsque nécessaire, ce qui est plus efficace en mémoire.

## **Considérations de performance**

Bien que les méthodes magiques soient puissantes, elles peuvent avoir un impact sur les performances si vous ne les utilisez pas avec soin. Explorons quelques considérations de performance courantes et comment les mesurer.

### **Impact des méthodes magiques sur les performances**

Différentes méthodes magiques ont différentes implications de performance :

**Méthodes d'accès aux attributs** :

* `__getattr__`, `__getattribute__`, `__setattr__`, et `__delattr__` sont appelées fréquemment

* Des opérations complexes dans ces méthodes peuvent ralentir considérablement votre code

**Méthodes de conteneur** :

* `__getitem__`, `__setitem__`, et `__len__` sont souvent appelées dans les boucles

* Des implémentations inefficaces peuvent rendre votre conteneur beaucoup plus lent que les types intégrés

**Surcharge des opérateurs** :

* Les opérateurs arithmétiques et de comparaison sont utilisés fréquemment

* Des implémentations complexes peuvent rendre les opérations simples inattendues lentes

Mesurons l'impact de performance de `__getattr__` vs. l'accès direct aux attributs :

```python
import time

class DirectAccess:
    def __init__(self):
        self.value = 42

class GetAttrAccess:
    def __init__(self):
        self._value = 42
    
    def __getattr__(self, name):
        if name == "value":
            return self._value
        raise AttributeError(f"L'objet '{self.__class__.__name__}' n'a pas d'attribut '{name}'")

# Mesurer les performances
direct = DirectAccess()
getattr_obj = GetAttrAccess()

def benchmark(obj, iterations=1000000):
    start = time.time()
    for _ in range(iterations):
        x = obj.value
    end = time.time()
    return end - start

direct_time = benchmark(direct)
getattr_time = benchmark(getattr_obj)

print(f"Accès direct : {direct_time:.6f} secondes")
print(f"Accès __getattr__ : {getattr_time:.6f} secondes")
print(f"__getattr__ est {getattr_time / direct_time:.2f}x plus lent")
```

L'exécution de ce benchmark montre des différences de performance significatives :

```plaintext
Accès direct : 0.027714 secondes
Accès __getattr__ : 0.060646 secondes
__getattr__ est 2.19x plus lent
```

Comme vous pouvez le voir, l'utilisation de `__getattr__` est plus de deux fois plus lente que l'accès direct aux attributs. Cela peut ne pas importer pour les attributs rarement accédés, mais cela peut devenir significatif dans du code critique pour les performances qui accède aux attributs dans des boucles serrées.

### **Stratégies d'optimisation**

Heureusement, il existe diverses façons d'optimiser les méthodes magiques.

1. **Utiliser slots pour l'efficacité mémoire** : Cela réduit l'utilisation de la mémoire et améliore la vitesse d'accès aux attributs. C'est le meilleur pour les classes avec de nombreuses instances.

2. **Mettre en cache les valeurs calculées** : Vous pouvez stocker les résultats des opérations coûteuses et mettre à jour le cache uniquement lorsque nécessaire. Utilisez `@property` pour les attributs calculés.

3. **Minimiser les appels de méthodes** : Assurez-vous d'éviter les appels inutiles aux méthodes magiques et utilisez l'accès direct aux attributs lorsque cela est possible. Envisagez d'utiliser `__slots__` pour les attributs fréquemment accédés.

## **Meilleures pratiques**

Lorsque vous utilisez des méthodes magiques, suivez ces meilleures pratiques pour vous assurer que votre code est maintenable, efficace et fiable.

### **1. Soyez cohérent**

Lorsque vous implémentez des méthodes magiques liées, maintenez une cohérence dans le comportement :

```python
from functools import total_ordering

@total_ordering
class ConsistentNumber:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, ConsistentNumber):
            return NotImplemented
        return self.value == other.value
    
    def __lt__(self, other):
        if not isinstance(other, ConsistentNumber):
            return NotImplemented
        return self.value < other.value
```

### **2. Retournez NotImplemented**

Lorsque qu'une opération n'a pas de sens, retournez `NotImplemented` pour laisser Python essayer l'opération inverse :

```python
class Money:
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        # ... reste de l'implémentation
```

### **3. Gardez cela simple**

Les méthodes magiques doivent être simples et prévisibles. Évitez la logique complexe qui pourrait conduire à un comportement inattendu :

```python
# Bien : Simple et prévisible
class SimpleContainer:
    def __init__(self):
        self.items = []
    
    def __getitem__(self, index):
        return self.items[index]

# Mal : Complexe et potentiellement confus
class ComplexContainer:
    def __init__(self):
        self.items = []
        self.access_count = 0
    
    def __getitem__(self, index):
        self.access_count += 1
        if self.access_count > 100:
            raise RuntimeError("Trop d'accès")
        return self.items[index]
```

### **4. Documentez le comportement**

Documentez clairement comment vos méthodes magiques se comportent, surtout si elles s'écartent des attentes standard :

```python
class CustomDict(dict):
    def __missing__(self, key):
        """
        Appelée lorsqu'une clé n'est pas trouvée dans le dictionnaire.
        Crée une nouvelle liste pour la clé et la retourne.
        Cela permet la création automatique de listes lors de l'accès
        à des clés non existantes.
        """
        self[key] = []
        return self[key]
```

### **5. Considérez la performance**

Soyez conscient des implications de performance, surtout pour les méthodes fréquemment appelées :

```python
class OptimizedContainer:
    __slots__ = ['items']  # Utiliser __slots__ pour de meilleures performances
    
    def __init__(self):
        self.items = []
    
    def __getitem__(self, index):
        return self.items[index]  # L'accès direct est plus rapide
```

### **6. Gérez les cas limites**

Toujours considérer les cas limites et les gérer de manière appropriée :

```python
class SafeContainer:
    def __getitem__(self, key):
        if not isinstance(key, (int, slice)):
            raise TypeError("L'index doit être un entier ou une tranche")
        if key < 0:
            raise ValueError("L'index ne peut pas être négatif")
        # ... reste de l'implémentation
```

## **Conclusion**

Les méthodes magiques de Python fournissent un moyen puissant de faire en sorte que vos classes se comportent comme des types intégrés, permettant un code plus intuitif et expressif. Tout au long de ce guide, nous avons exploré comment ces méthodes fonctionnent et comment les utiliser efficacement.

### **Points clés à retenir**

1. **Représentation des objets** :

   * Utilisez `__str__` pour une sortie conviviale

   * Utilisez `__repr__` pour le débogage et le développement

2. **Surcharge des opérateurs** :

   * Implémentez les opérateurs arithmétiques et de comparaison

   * Retournez `NotImplemented` pour les opérations non supportées

   * Utilisez `@total_ordering` pour des comparaisons cohérentes

3. **Comportement des conteneurs** :

   * Implémentez les protocoles de séquence et de mappage

   * Considérez la performance pour les opérations fréquemment utilisées

   * Gérez les cas limites de manière appropriée

4. **Gestion des ressources** :

   * Utilisez les gestionnaires de contexte pour une gestion appropriée des ressources

   * Implémentez `__enter__` et `__exit__` pour le nettoyage

   * Gérez les exceptions dans `__exit__`

5. **Optimisation des performances** :

   * Utilisez `__slots__` pour l'efficacité mémoire

   * Mettez en cache les valeurs calculées lorsque cela est approprié

   * Minimisez les appels de méthodes dans le code fréquemment utilisé

### **Quand utiliser les méthodes magiques**

Les méthodes magiques sont les plus utiles lorsque vous avez besoin de :

1. Créer des structures de données personnalisées

2. Implémenter des types spécifiques à un domaine

3. Gérer correctement les ressources

4. Ajouter un comportement spécial à vos classes

5. Rendre votre code plus Pythonique

### **Quand éviter les méthodes magiques**

Évitez les méthodes magiques lorsque :

1. Un accès simple aux attributs est suffisant

2. Le comportement serait confus ou inattendu

3. La performance est critique et les méthodes magiques ajouteraient un surcoût

4. L'implémentation serait trop complexe

Rappelez-vous qu'avec un grand pouvoir vient une grande responsabilité. Utilisez les méthodes magiques avec discernement, en gardant à l'esprit leurs implications de performance et le principe de la moindre surprise. Lorsque cela est approprié, les méthodes magiques peuvent améliorer considérablement la lisibilité et l'expressivité de votre code.

## **Références et lectures complémentaires**

### **Documentation officielle de Python**

1. [Modèle de données Python - Documentation officielle](https://docs.python.org/3/reference/datamodel.html) - Guide complet du modèle de données de Python et des méthodes magiques.

2. [functools.total_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering) - Documentation pour le décorateur total_ordering qui remplit automatiquement les méthodes de comparaison manquantes.

3. [Noms de méthodes spéciales de Python](https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers) - Référence officielle pour les identifiants de méthodes spéciales en Python.

4. [Classes de base abstraites des collections](https://docs.python.org/3/library/collections.abc.html) - Apprenez les classes de base abstraites pour les conteneurs qui définissent les interfaces que vos classes de conteneurs peuvent implémenter.

### **Ressources communautaires**

5. [Un guide des méthodes magiques de Python - Rafe Kettler](https://rszalski.github.io/magicmethods/) - Exemples pratiques de méthodes magiques et cas d'utilisation courants.

### **Lectures complémentaires**

Si vous avez aimé cet article, vous pourriez trouver ces articles liés à Python sur mon [blog personnel](https://wewake.dev) utiles :

1. [Expériences pratiques pour les optimisations de requêtes Django ORM](https://wewake.dev/posts/practical-experiments-for-django-orm-query-optimizations/) - Apprenez à optimiser vos requêtes Django ORM avec des exemples et expériences pratiques.

2. [Le coût élevé de uWSGI synchrone](https://wewake.dev/posts/high-cost-of-sync-uwsgi/) - Comprenez les implications de performance du traitement synchrone dans uWSGI et comment cela affecte vos applications web Python.