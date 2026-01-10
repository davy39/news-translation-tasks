---
title: Comment implémenter les principes SOLID dans Flutter et Dart
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-10-01T12:29:48.777Z'
originalURL: https://freecodecamp.org/news/implement-the-solid-principles-in-flutter-and-dart
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759321694714/7751ee74-dfe6-4c22-ac6f-b614f5920b7f.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
seo_title: Comment implémenter les principes SOLID dans Flutter et Dart
seo_desc: When building Flutter applications, it’s easy to get caught up in writing
  code that just works. But as your app grows in size and complexity, poorly structured
  code becomes harder to maintain, test, and extend. That’s where the SOLID principles
  come ...
---

Lors de la création d'applications Flutter, il est facile de se laisser emporter par l'écriture d'un code qui fonctionne tout simplement. Mais à mesure que votre application gagne en taille et en complexité, un code mal structuré devient plus difficile à maintenir, à tester et à étendre. C'est là qu'interviennent les principes SOLID.

SOLID est un acronyme pour cinq principes de conception qui aident les développeurs à écrire un code propre, évolutif et maintenable :

* **S** – Single Responsibility Principle (SRP / Principe de Responsabilité Unique)
    
* **O** – Open/Closed Principle (OCP / Principe Ouvert/Fermé)
    
* **L** – Liskov Substitution Principle (LSP / Principe de Substitution de Liskov)
    
* **I** – Interface Segregation Principle (ISP / Principe de Ségrégation des Interfaces)
    
* **D** – Dependency Inversion Principle (DIP / Principe d'Inversion des Dépendances)
    

Dans ce guide, nous allons décomposer chaque principe, expliquer sa signification et montrer des exemples pratiques de code Flutter/Dart que vous pouvez appliquer dans vos projets.

## Table des matières :

* [Prérequis](#heading-prerequis)
    
* [1\. Principe de Responsabilité Unique (SRP)](#heading-1-principe-de-responsabilite-unique-srp)
    
    * [Exemple Flutter](#heading-exemple-flutter)
        
    * [Explication du code](#heading-explication-du-code)
        
* [2\. Principe Ouvert-Fermé (OCP)](#heading-2-principe-ouvert-ferme-ocp)
    
    * [Exemple Flutter](#heading-exemple-flutter-1)
        
    * [Explication du code](#heading-explication-du-code-1)
        
* [3\. Principe de Substitution de Liskov (LSP)](#heading-3-principe-de-substitution-de-liskov-lsp)
    
    * [Exemple Flutter](#heading-exemple-flutter-2)
        
    * [Explication du code](#heading-explication-du-code-2)
        
* [4\. Principe de Ségrégation des Interfaces (ISP)](#heading-4-principe-de-segregation-des-interfaces-isp)
    
    * [Exemple Flutter](#heading-exemple-flutter-3)
        
    * [Explication du code](#heading-explication-du-code-3)
        
* [5\. Principe d'Inversion des Dépendances (DIP)](#heading-5-principe-d-inversion-des-dependances-dip)
    
    * [Exemple Flutter](#heading-exemple-flutter-4)
        
    * [Explication du code](#heading-explication-du-code-4)
        
* [Tests et refactorisation avec SOLID](#heading-tests-et-refactorisation-avec-solid)
    
* [Réflexions finales](#heading-reflexions-finales)
    
* [Références](#heading-references)
    

## Prérequis

Avant de commencer, vous devriez :

* Savoir utiliser Dart et Flutter.
    
* Avoir une compréhension de base des concepts de la POO (classes, héritage, interfaces et polymorphisme).
    
* Avoir Flutter installé sur votre système ([Guide d'installation Flutter](https://docs.flutter.dev/get-started/install)).
    
* Être familier avec l'exécution d'applications Flutter sur un émulateur ou un appareil physique.
    

## Comment implémenter le Principe de Responsabilité Unique (SRP) dans Flutter

**Définition :** Une classe ne devrait avoir qu'une seule raison de changer. Ce principe empêche la création de « classes dieux » qui essaient de tout faire. Au lieu de cela, chaque classe doit gérer une responsabilité spécifique.

### Exemple Flutter

```dart
// Principe de Responsabilité Unique (SRP)

// La classe Logger gère uniquement la journalisation
class Logger {
  void log(String message) {
    print(message);
  }
}

// La classe UserManager gère uniquement la gestion des utilisateurs
class UserManager {
  final Logger _logger;

  UserManager(this._logger);

  void addUser(String username) {
    // Logique métier pour ajouter un utilisateur
    _logger.log('Utilisateur $username ajouté.');
  }
}
```

### Explication du code

* `class Logger { ... }` → Cette classe est responsable uniquement de la journalisation (logging). Elle possède une méthode unique `log`.
    
* `class UserManager { ... }` → Cette classe gère les utilisateurs (par exemple, leur ajout).
    
* `final Logger _logger;` → Au lieu de journaliser directement, `UserManager` dépend de la classe `Logger`.
    
* `addUser(String username)` → Se concentre sur la gestion des utilisateurs, pas sur la journalisation.
    

En séparant les responsabilités, nous pouvons remplacer `Logger` par une autre implémentation (comme la sauvegarde des logs dans un fichier) sans toucher à `UserManager`.

**Le SRP dans les projets Flutter réels :**

* `AuthService` pour la logique d'authentification
    
* `ApiService` pour les appels réseau
    
* `DatabaseService` pour la persistance locale
    

![Diagramme du Principe de Responsabilité Unique (SRP)](https://cdn.hashnode.com/res/hashnode/image/upload/v1757913175392/5605cc80-3729-46ac-90dc-4fc2688b53f6.png align="center")

## Comment implémenter le Principe Ouvert-Fermé (OCP) dans Flutter

**Définition :** Les classes doivent être ouvertes à l'extension mais fermées à la modification. Cela signifie que vous ne devriez pas avoir besoin de modifier le code existant lors de l'ajout de nouvelles fonctionnalités — il suffit de l'étendre.

### Exemple Flutter

```dart
// Principe Ouvert/Fermé (OCP)

// Abstraction de base
abstract class Shape {
  double area();
}

// La classe Circle étend Shape
class Circle implements Shape {
  final double radius;

  Circle(this.radius);

  @override
  double area() => 3.14 * radius * radius;
}

// La classe Square étend Shape
class Square implements Shape {
  final double side;

  Square(this.side);

  @override
  double area() => side * side;
}
```

### Explication du code

* `abstract class Shape` → Définit le contrat `area()` pour toutes les formes.
    
* `class Circle implements Shape` → Étend le comportement sans modifier le code existant.
    
* `class Square implements Shape` → Ajoute une autre forme de la même manière.
    

Si vous souhaitez ajouter un `Triangle`, il vous suffit de créer une nouvelle classe au lieu de modifier `Shape`, `Circle` ou `Square`.

**L'OCP dans les projets Flutter réels :**

* Ajouter de nouveaux composants UI sans modifier la classe widget de base.
    
* Supporter de nouvelles méthodes de paiement dans une application en implémentant une interface `PaymentMethod`.
    

![Diagramme du Principe Ouvert-Fermé (OCP)](https://cdn.hashnode.com/res/hashnode/image/upload/v1757913242929/731542b0-bad6-4758-8a98-6119f4555a85.png align="center")

## Comment implémenter le Principe de Substitution de Liskov (LSP) dans Flutter

**Définition :** Les sous-classes doivent pouvoir être substituées à leurs classes de base sans casser la fonctionnalité. Si votre fonction accepte un type de base, elle doit également accepter ses sous-types sans problème.

### Exemple Flutter

```dart
// Principe de Substitution de Liskov (LSP)

void printArea(Shape shape) {
  print('Surface : ${shape.area()}');
}

void main() {
  Shape circle = Circle(5);
  Shape square = Square(4);

  printArea(circle); // Fonctionne avec Circle
  printArea(square); // Fonctionne avec Square
}
```

### Explication du code

1. `void printArea(Shape shape)` → Fonctionne avec n'importe quelle classe implémentant `Shape`.
    
2. `circle` et `square` → Les deux sont des substituts valides pour `Shape`.
    

**Le LSP dans les projets Flutter réels :**

* Un `TextField` peut être remplacé par un widget `PasswordField`, car les deux se comportent comme des champs de saisie.
    
* Un `FirebaseAuthService` peut être remplacé par un `MockAuthService` dans les tests.
    

![Diagramme du Principe de Substitution de Liskov (LSP)](https://cdn.hashnode.com/res/hashnode/image/upload/v1757913229737/e183674a-04f5-45d9-ba92-78ebf654c9da.png align="center")

## Comment implémenter le Principe de Ségrégation des Interfaces (ISP) dans Flutter

**Définition :** Les clients ne devraient pas dépendre de méthodes qu'ils n'utilisent pas. Au lieu d'une seule grande interface, divisez-la en interfaces plus petites et ciblées.

### Exemple Flutter

```dart
// Principe de Ségrégation des Interfaces (ISP)

abstract class Flyable {
  void fly();
}

abstract class Swimmable {
  void swim();
}

class Bird implements Flyable {
  @override
  void fly() => print('L\'oiseau vole.');
}

class Fish implements Swimmable {
  @override
  void swim() => print('Le poisson nage.');
}
```

### Explication du code

1. `Flyable` et `Swimmable` → Contrats séparés pour le vol et la nage.
    
2. `Bird implements Flyable` → Les oiseaux n'ont pas besoin d'une méthode `swim`.
    
3. `Fish implements Swimmable` → Les poissons n'ont pas besoin d'une méthode `fly`.
    

**L'ISP dans les projets Flutter réels :**

* Diviser `AuthService` en interfaces plus petites comme `LoginService`, `RegistrationService`, `PasswordResetService`.
    
* Widgets implémentant uniquement les propriétés dont ils ont réellement besoin.
    

![Diagramme du Principe de Ségrégation des Interfaces (ISP)](https://cdn.hashnode.com/res/hashnode/image/upload/v1757913202271/0625c762-ea78-4a77-8a2f-c430431ad944.png align="center")

## Comment implémenter le Principe d'Inversion des Dépendances (DIP) dans Flutter

**Définition :** Les modules de haut niveau doivent dépendre d'abstractions, et non d'implémentations concrètes. Cela rend votre code plus flexible et testable.

### Exemple Flutter

```dart
// Principe d'Inversion des Dépendances (DIP)

// Abstraction
abstract class Database {
  void saveData(String data);
}

// Implémentation concrète
class SqlDatabase implements Database {
  @override
  void saveData(String data) {
    print('SQL : Données sauvegardées -> $data');
  }
}

// Module de haut niveau
class DataService {
  final Database _database;

  DataService(this._database);

  void processData(String data) {
    _database.saveData(data);
  }
}

void main() {
  Database db = SqlDatabase();
  DataService service = DataService(db);

  service.processData('Infos utilisateur');
}
```

### Explication du code

1. `abstract class Database` → Définit le contrat pour la sauvegarde des données.
    
2. `class SqlDatabase implements Database` → Une implémentation possible.
    
3. `class DataService` → Dépend uniquement de l'abstraction `Database`, et non de `SqlDatabase`.
    
4. `Database db = SqlDatabase();` → L'implémentation peut facilement être remplacée (par exemple, par `FirebaseDatabase`).
    

**Le DIP dans les projets Flutter réels :**

* Utiliser `AuthRepository` au lieu de lier le code directement à Firebase.
    
* Injecter des services avec `get_it` ou `riverpod`.
    

![Diagramme du Principe d'Inversion des Dépendances (DIP)](https://cdn.hashnode.com/res/hashnode/image/upload/v1757913100217/04ced0cf-eaea-427c-b413-295e0019b15d.png align="center")

## Tests et refactorisation avec SOLID

* **Les tests unitaires** deviennent plus faciles puisque vous pouvez simuler (mock) les dépendances.
    
* **La refactorisation** est plus fluide car les responsabilités sont bien séparées.
    
* **Les revues de code** permettent de détecter tôt les violations des principes SOLID.
    

## Réflexions finales

En suivant les principes SOLID dans Flutter et Dart :

* Votre code devient plus maintenable.
    
* Les nouvelles fonctionnalités sont plus faciles à ajouter.
    
* Les tests deviennent beaucoup plus simples.
    

Ces principes ne sont pas seulement théoriques, ils améliorent directement les projets Flutter du monde réel. Commencez petit, appliquez un principe à la fois, et vous verrez rapidement votre base de code évoluer vers quelque chose de beaucoup plus évolutif et paré pour l'avenir.

## Références

* Robert C. Martin – *Clean Architecture*
    
* [Documentation Flutter](https://docs.flutter.dev/)
    
* [Effective Dart](https://dart.dev/guides/language/effective-dart)
    
* [Injection de dépendances dans Flutter (get_it)](https://pub.dev/packages/get_it)