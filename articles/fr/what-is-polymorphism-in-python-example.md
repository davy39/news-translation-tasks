---
title: Qu'est-ce que le polymorphisme en Python ? Expliqué avec un exemple
subtitle: ''
author: Danny
co_authors: []
series: null
date: '2025-02-06T15:12:42.681Z'
originalURL: https://freecodecamp.org/news/what-is-polymorphism-in-python-example
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738335631634/ef8f79a0-73df-430c-b955-a5325ca22f04.png
tags:
- name: Python
  slug: python
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: oop
  slug: oop
- name: design patterns
  slug: design-patterns
- name: software development
  slug: software-development
seo_title: Qu'est-ce que le polymorphisme en Python ? Expliqué avec un exemple
seo_desc: Polymorphism is an object-oriented programming (OOP) principle that helps
  you write high quality, flexible, maintainable, reusable, testable, and readable
  software. If you plan to work with object-oriented software, it is crucial to understand
  polymo...
---

Le polymorphisme est un principe de la programmation orientée objet (POO) qui vous aide à écrire des logiciels de haute qualité, flexibles, maintenables, réutilisables, testables et lisibles. Si vous prévoyez de travailler avec des logiciels orientés objet, il est crucial de comprendre le polymorphisme.

## Qu'est-ce que le polymorphisme ?

Le mot *polymorphisme* est dérivé du grec et signifie "avoir plusieurs formes" :

* Poly = plusieurs

* Morph = formes

**En programmation, le polymorphisme est la capacité d'un objet à prendre plusieurs formes**.

L'avantage clé du polymorphisme est qu'il nous permet d'écrire un code plus **générique** et **réutilisable**. Au lieu d'écrire une logique séparée pour différentes classes, nous définissons des comportements communs dans une classe parente et laissons les classes enfants les redéfinir selon les besoins. Cela élimine le besoin de vérifications excessives `if-else`, rendant le code plus maintenable et extensible.

Les frameworks MVC comme [Django](http://djangoproject.com/) utilisent le polymorphisme pour rendre le code plus flexible. Par exemple, Django supporte différentes bases de données comme SQLite, MySQL et PostgreSQL. Normalement, chaque base de données nécessite un code différent pour interagir avec elle, mais Django fournit une seule API de base de données qui fonctionne avec toutes. Cela signifie que vous pouvez écrire le même code pour les opérations de base de données, peu importe la base de données que vous utilisez. Donc, si vous commencez un projet avec SQLite et passez plus tard à PostgreSQL, vous n'aurez pas besoin de réécrire une grande partie de votre code, grâce au polymorphisme.

Dans cet article, pour faciliter la compréhension, je vais vous montrer un mauvais exemple de code sans polymorphisme. Nous discuterons des problèmes que ce mauvais code cause, puis nous résoudrons ces problèmes en refactorisant le code pour utiliser le polymorphisme.

(En passant, si vous apprenez mieux par vidéo, consultez ma vidéo YouTube [Polymorphisme en Python](https://youtu.be/zuPg8_qsL7A).)

## D'abord, un exemple sans polymorphisme :

```python
class Car:
    def __init__(self, brand, model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")
```

```python
class Motorcycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_bike(self):
        print("Motorcycle is starting.")

    def stop_bike(self):
        print("Motorcycle is stopping.")
```

Supposons que nous voulons créer une liste de véhicules, puis parcourir cette liste et effectuer une inspection sur chaque véhicule :

```python
# Créer une liste de véhicules à inspecter
vehicles = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018),
]

# Parcourir la liste de véhicules et les inspecter
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, Motorcycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a valid vehicle")
```

Remarquez le code peu élégant à l'intérieur de la boucle `for` ! Parce que `vehicles` est une liste de n'importe quel type d'objet, nous devons déterminer quel type d'objet nous traitons à l'intérieur de chaque boucle avant de pouvoir accéder à toute information sur l'objet.

Ce code deviendra de plus en plus peu élégant à mesure que nous ajouterons plus de types de véhicules. Par exemple, si nous *étendions* notre base de code pour inclure une nouvelle classe `Plane`, alors nous devrions *modifier* (et potentiellement casser) le code existant - nous devrions ajouter une autre vérification conditionnelle dans la boucle `for` pour les avions.

### **Introduction : Le polymorphisme...**

Les voitures et les motos sont toutes deux des véhicules. Elles partagent toutes deux certaines propriétés et méthodes communes. Donc, créons une classe parente qui contient ces propriétés et méthodes partagées :

Classe parente (ou "superclasse") :

```python
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")

    def stop(self):
        print("Vehicle is stopping.")
```

`Car` et `Motorcycle` peuvent maintenant *hériter* de `Vehicle`. Créons les classes enfants (ou "sous-classes") de la superclasse `Vehicle` :

```python
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    # Ci-dessous, nous "redéfinissons" les méthodes start et stop, héritées de Vehicle, pour fournir un comportement spécifique à la voiture

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")
```

```python
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # Ci-dessous, nous "redéfinissons" les méthodes start et stop, héritées de Vehicle, pour fournir un comportement spécifique à la moto

    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")
```

`Car` et `Motorcycle` étendent tous deux `Vehicle`, car ce sont des véhicules. Mais quel est l'intérêt pour `Car` et `Motorcycle` d'étendre `Vehicle` s'ils vont implémenter leurs propres versions des méthodes `start()` et `stop()` ? Regardez le code ci-dessous :

```python
# Créer une liste de véhicules à inspecter
vehicles = [Car("Ford", "Focus", 2008, 5), Motorcycle("Honda", "Scoopy", 2018)]

# Parcourir la liste de véhicules et les inspecter
for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")
```

**Dans cet exemple :**

* Nous avons une liste, `vehicles`, contenant des instances de `Car` et `Motorcycle`.

* Nous parcourons chaque véhicule dans la liste et effectuons une inspection générale sur chacun.

* Le processus d'inspection implique de démarrer le véhicule, de vérifier sa marque et son modèle, et de l'arrêter ensuite.

* Malgré le fait que les véhicules soient de types différents, le polymorphisme nous permet de les traiter tous comme des instances de la classe de base `Vehicle`. Les implémentations spécifiques des méthodes `start()` et `stop()` pour chaque type de véhicule sont invoquées dynamiquement à l'exécution, en fonction du type réel de chaque véhicule.

Parce que la liste ne peut *contenir* que des objets qui étendent la classe `Vehicle`, nous savons que chaque objet partagera certains champs et méthodes communs. Cela signifie que nous pouvons les appeler en toute sécurité, sans avoir à nous soucier de savoir si chaque véhicule spécifique possède ces champs ou méthodes.

Cela démontre comment le polymorphisme permet d'écrire du code de manière plus générique et flexible, permettant une extension et une maintenance faciles lorsque de nouveaux types de véhicules sont ajoutés au système.

Par exemple, si nous voulions ajouter un autre véhicule à la liste, nous n'avons pas à modifier le code utilisé pour inspecter les véhicules ("le code client"). Au lieu de cela, nous pouvons simplement *étendre* notre base de code (c'est-à-dire créer une nouvelle classe), sans *modifier* le code existant :

```python
class Plane(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Plane is starting.")

    def stop(self):
        print("Plane is stopping.")
```

```python
# Créer une liste de véhicules à inspecter
vehicles = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018),

    ########## AJOUTER UN AVION À LA LISTE : #########

    Plane("Boeing", "747", 2015, 16),
    
    ############################################
]
```

Le code pour effectuer les inspections de véhicules n'a pas besoin d'être modifié pour prendre en compte un avion. Tout fonctionne toujours, sans avoir à modifier notre logique d'inspection.

## Conclusion

Le polymorphisme permet aux clients de traiter différents types d'objets de la même manière. Cela améliore grandement la flexibilité du logiciel et la maintenabilité du logiciel, car de nouvelles classes peuvent être créées sans que vous ayez à modifier (souvent en ajoutant des blocs `if`/`else if` supplémentaires) le code existant, fonctionnel et testé.

## Pour aller plus loin

Le polymorphisme est lié à de nombreux autres principes de la programmation orientée objet, tels que *l'injection de dépendances* et le principe *ouvert-fermé* SOLID. Si vous souhaitez maîtriser la POO, consultez mon cours Udemy :

* [Python OOP : Programmation Orientée Objet de Débutant à Pro 🎥](https://www.udemy.com/course/python-oop-object-oriented-programming-from-beginner-to-pro)

Si vous préférez les livres aux vidéos, consultez mes livres :

* [Amazon Kindle et broché 📖](https://www.amazon.com/dp/B0DR6ZPZQ8)

* [Gumroad PDF 📖](https://doabledanny.gumroad.com/l/python-oop-beginner-to-pro)

Merci d'avoir lu :)