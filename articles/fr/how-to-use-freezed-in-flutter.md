---
title: Comment utiliser Freezed dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-10-06T13:44:43.860Z'
originalURL: https://freecodecamp.org/news/how-to-use-freezed-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759758218094/78645767-b4be-4210-9adb-a137ea605c9c.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment utiliser Freezed dans Flutter
seo_desc: 'Flutter is a UI toolkit developed by Google. It’s gained immense popularity
  for its ability to create beautiful and natively compiled applications for mobile,
  web, and desktop from a single codebase.

  While Dart, the language behind Flutter, is powerf...'
---

Flutter est un toolkit d'interface utilisateur développé par Google. Il a acquis une popularité immense pour sa capacité à créer de belles applications compilées nativement pour le mobile, le web et le bureau à partir d'une seule base de code (codebase).

Bien que Dart, le langage derrière Flutter, soit puissant, l'écriture de modèles de données implique souvent des tâches répétitives et sujettes aux erreurs. Un modèle typique peut nécessiter :

* La définition d'un constructeur et de propriétés
    
* La redéfinition de `toString`, de l'opérateur `==` et de `hashCode`
    
* L'implémentation d'une méthode `copyWith`
    
* L'écriture de méthodes de sérialisation (`toJson`) et de désérialisation (`fromJson`)
    

Faire tout cela à la main peut rapidement alourdir votre code et réduire sa lisibilité.

C'est là qu'intervient Freezed. Freezed est un générateur de code Dart qui crée le boilerplate pour les classes de données immuables, les unions, le pattern matching, le clonage et la sérialisation JSON. Avec Freezed, vous pouvez écrire des modèles concis et sûrs pendant que le package gère les parties répétitives.

Dans ce tutoriel, vous apprendrez à utiliser Freezed pour créer des classes de données immuables, générer la sérialisation JSON et implémenter des unions puissantes pour gérer plusieurs états de manière type-safe. À la fin, vous saurez comment réduire le boilerplate et rendre votre code Flutter plus propre, plus sûr et plus facile à maintenir.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Pourquoi Freezed ?](#heading-pourquoi-freezed)
    
* [Sans Freezed : Un exemple manuel](#heading-sans-freezed-un-exemple-manuel)
    
* [Avec Freezed : Une alternative plus propre](#heading-avec-freezed-une-alternative-plus-propre)
    
* [Définir une classe Freezed](#heading-definir-une-classe-freezed)
    
    * [Explication ligne par ligne :](#heading-explication-ligne-par-ligne)
        
* [Exécuter la génération de code](#heading-executer-la-generation-de-code)
    
* [Utiliser la classe Freezed](#heading-utiliser-la-classe-freezed)
    
    * [Explication :](#heading-explication)
        
* [Ajouter la sérialisation JSON](#heading-ajouter-la-serialisation-json)
    
    * [Explication des nouvelles parties :](#heading-explication-des-nouvelles-parties)
        
* [Utiliser la sérialisation JSON](#heading-utiliser-la-serialisation-json)
    
    * [Explication :](#heading-explication-1)
        
* [Utilisation avancée : Unions Freezed](#heading-utilisation-avancee-unions-freezed)
    
    * [Définir une Union](#heading-definir-une-union)
        
    * [Utiliser l'Union](#heading-utiliser-l-union)
        
    * [Pattern Matching avec Freezed](#heading-pattern-matching-avec-freezed)
        
    * [MaybeWhen : Gérer les états partiels](#heading-maybewhen-gerer-les-etats-partiels)
        
    * [Map : Travailler directement avec les objets d'état](#heading-map-travailler-directement-avec-les-objets-d-etat)
        
* [Pourquoi utiliser les Unions ?](#heading-pourquoi-utiliser-les-unions)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, vous devriez être à l'aise avec :

1. **Les bases de Flutter** : Être capable de créer un nouveau projet Flutter et de l'exécuter sur un émulateur ou un appareil.
    
2. **Les fondamentaux du langage Dart** : Comprendre le fonctionnement des classes, des constructeurs et des méthodes.
    
3. **Les outils en ligne de commande** : Être capable d'exécuter des commandes comme `flutter pub get` ou `flutter pub run`.
    
4. **Les concepts JSON** : Savoir ce qu'est le JSON et comment il est couramment utilisé pour l'échange de données via API.
    

Si vous êtes déjà à l'aise avec ces sujets, vous êtes prêt à plonger dans Freezed.

## Pourquoi Freezed ?

Lors de la construction d'applications Flutter, deux défis surviennent souvent lors du travail avec les modèles de données : l'**immuabilité** et la **sérialisation**. Freezed aide à résoudre les deux de manière claire et automatisée.

### 1\. Immuabilité

En Dart, les objets sont mutables par défaut. Cela signifie qu'une fois que vous créez un objet, ses champs peuvent être modifiés n'importe où dans votre code. Bien que pratique, cela peut entraîner des effets secondaires imprévus, comme la modification accidentelle d'un objet utilisateur dans une partie de votre application, cassant la logique ailleurs.

Garantir l'immuabilité manuellement nécessite beaucoup de boilerplate : vous devez déclarer tous les champs comme `final`, implémenter des méthodes `copyWith` pour créer des copies modifiées, et redéfinir correctement `==` et `hashCode` pour maintenir l'égalité des objets. Cela peut être répétitif et sujet aux erreurs.

#### Comment Freezed aide :

Freezed génère automatiquement des classes immuables. Tous les champs sont `final`, et une méthode `copyWith` est fournie pour que vous puissiez créer en toute sécurité des copies modifiées sans muter l'objet original. De plus, Freezed gère `==` et `hashCode` pour vous, ce qui garantit que vos objets se comportent correctement lorsqu'ils sont comparés ou utilisés dans des collections. Cela réduit considérablement le boilerplate tout en imposant l'immuabilité.

### 2\. Sérialisation

Lors de l'interaction avec des API, la conversion d'objets Dart vers et depuis le format JSON est une tâche courante. Sans automatisation, vous devez écrire des méthodes `toJson` et `fromJson` pour chaque classe, en mappant soigneusement chaque champ. C'est répétitif et facile à rater, surtout lorsque vos modèles évoluent avec le temps.

#### Comment Freezed aide :

Freezed s'intègre au package `json_serializable` pour générer automatiquement la logique de sérialisation et de désérialisation. Il vous suffit d'annoter votre classe et d'exécuter le générateur de code, puis Freezed crée pour vous des méthodes `toJson` et `fromJson` parfaitement fonctionnelles. Cela permet non seulement de gagner du temps, mais aussi de réduire les risques d'erreurs et de garder votre code propre et maintenable.

## Sans Freezed : Un exemple manuel

Voici à quoi ressemble une classe `User` de base sans Freezed :

```dart
class User {
  final String name;
  final int age;
  final String email;

  const User({
    required this.name,
    required this.age,
    required this.email,
  });

  User copyWith({
    String? name,
    int? age,
    String? email,
  }) {
    return User(
      name: name ?? this.name,
      age: age ?? this.age,
      email: email ?? this.email,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'age': age,
      'email': email,
    };
  }

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      name: json['name'] as String,
      age: json['age'] as int,
      email: json['email'] as String,
    );
  }

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is User &&
          runtimeType == other.runtimeType &&
          name == other.name &&
          age == other.age &&
          email == other.email;

  @override
  int get hashCode => name.hashCode ^ age.hashCode ^ email.hashCode;

  @override
  String toString() {
    return 'User{name: $name, age: $age, email: $email}';
  }
}
```

C'est verbeux, et il est facile d'oublier des détails comme la mise à jour de `hashCode` lors de l'ajout de nouveaux champs.

## Avec Freezed : Une alternative plus propre

Maintenant que vous comprenez les défis que Freezed résout, voyons comment il rend le travail avec les modèles de données plus simple et plus propre. Dans cette section, vous allez installer les packages nécessaires, configurer une classe Freezed et générer le code boilerplate. Une fois cette configuration terminée, nous plongerons dans des exemples montrant comment utiliser la classe Freezed, y compris la copie d'objets et la sérialisation JSON.

Tout d'abord, installez Freezed et ses packages associés. Ajoutez ceci à votre fichier **pubspec.yaml** :

```yaml
dependencies:
  freezed_annotation: ^2.4.1
  json_annotation: ^4.8.1

dev_dependencies:
  flutter_lints: ^2.0.0
  build_runner: ^2.0.0
  freezed: ^2.4.7
  json_serializable: ^6.7.1
```

Ensuite, exécutez :

```bash
flutter pub get
```

Pour les projets Dart purs, utilisez :

```bash
dart pub get
```

### Définir une classe Freezed

Créez un fichier nommé `user.dart` et ajoutez ce qui suit :

```dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'user.freezed.dart';

@freezed
class User with _$User {
  factory User({required String name, required int age}) = _User;
}
```

Voici ce qui se passe dans ce code :

* `import 'package:freezed_annotation/freezed_annotation.dart';` : Importe les annotations requises par Freezed.
    
* `part 'user.freezed.dart';` : Indique que Freezed générera du code dans ce fichier.
    
* `@freezed` : Indique à Freezed de traiter la classe suivante.
    
* `class User with _$User` : Déclare la classe `User`. La partie `with _$User` connecte la classe au code généré.
    
* `factory User({required String name, required int age}) = _User;` : Définit un constructeur factory. Freezed génère la classe d'implémentation (`_User`) en coulisses.
    

### Exécuter la génération de code

Exécutez la commande suivante pour générer le code :

```bash
flutter pub run build_runner watch --delete-conflicting-outputs
```

Pour les projets Dart :

```bash
dart pub run build_runner watch --delete-conflicting-outputs
```

Cela crée le fichier `user.freezed.dart`, contenant le boilerplate comme `copyWith`, `==`, `hashCode` et `toString`.

### Utiliser la classe Freezed

Voyons Freezed en action :

```dart
void main() {
  final user = User(name: 'John Doe', age: 25);
  final user2 = user.copyWith(name: 'Jane Doe');
  final user3 = user2;

  print(user);
  print(user2);
  print(user2 == user3);
  print('Name: ${user.name}');
  print('Age: ${user.age}');
}
```

Voici ce qui se passe :

* `final user = User(name: 'John Doe', age: 25);` : Crée un nouvel `User` immuable.
    
* `final user2 = user.copyWith(name: 'Jane Doe');` : Crée une copie de `user` avec un nouveau nom mais conserve le même âge.
    
* `final user3 = user2;` : Fait pointer `user3` vers le même objet que `user2`.
    
* `print(user);` : Affiche une chaîne lisible, grâce au `toString` généré.
    
* `print(user2 == user3);` : Compare les objets en utilisant le `==` généré.
    

### Ajouter la sérialisation JSON

Mettez à jour `user.dart` pour supporter le JSON :

```dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'user.freezed.dart';
part 'user.g.dart';

@freezed
class User with _$User {
  factory User({required String name, required int age}) = _User;

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
}
```

Dans les nouvelles parties du code :

* `part 'user.g.dart';` : Ajoute un autre fichier généré pour le support JSON.
    
* `factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);` : Permet la désérialisation depuis le JSON.
    

Ensuite, relancez le générateur :

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

### Utiliser la sérialisation JSON

Exemple d'utilisation :

```dart
void main() {
  final userJson = {'name': 'Alice', 'age': 30};
  final user = User.fromJson(userJson);

  print('Name: ${user.name}');
  print('Age: ${user.age}');

  final userBackToJson = user.toJson();
  print('Back to JSON: $userBackToJson');
}
```

Dans ce code :

* `final user = User.fromJson(userJson);` : Convertit une map JSON en une instance de `User`.
    
* `user.toJson();` : Convertit un objet `User` en JSON.
    

## Utilisation avancée : Unions Freezed

Jusqu'à présent, nous avons utilisé Freezed pour des modèles de données immuables. Une autre fonctionnalité puissante de Freezed est les **unions** (également connues sous le nom de classes scellées ou sealed classes).

Les unions vous permettent de représenter plusieurs états possibles d'un objet de manière type-safe. C'est particulièrement utile dans Flutter lors du travail avec des tâches asynchrones telles que les appels d'API, où vous avez souvent des états comme `loading`, `success` et `error`.

### Définir une Union

Créez un nouveau fichier appelé `result.dart` :

```dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'result.freezed.dart';

@freezed
class Result<T> with _$Result<T> {
  const factory Result.loading() = Loading<T>;
  const factory Result.success(T data) = Success<T>;
  const factory Result.error(String message) = Error<T>;
}
```

Explication du code ligne par ligne :

* `import 'package:freezed_annotation/freezed_annotation.dart';` : Importe la bibliothèque d'annotations nécessaire pour Freezed.
    
* `part 'result.freezed.dart';` : Indique à Freezed de générer le boilerplate dans ce fichier.
    
* `@freezed` : Demande à Freezed de générer le code pour la classe annotée.
    
* `class Result<T> with _$Result<T>` : Déclare une classe générique `Result` qui peut contenir des données de type `T`.
    
* `const factory Result.loading() = Loading<T>;` : Définit l'état `loading`. `Loading<T>` est la classe générée.
    
* `const factory Result.success(T data) = Success<T>;` : Définit l'état `success` avec les données associées.
    
* `const factory Result.error(String message) = Error<T>;` : Définit l'état `error` avec un message.
    

Après avoir sauvegardé, générez le code :

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

### Utiliser l'Union

Simulons un appel d'API et renvoyons des résultats en utilisant notre union `Result` :

```dart
Future<Result<String>> fetchUserData() async {
  await Future.delayed(const Duration(seconds: 2)); // simule un délai réseau

  final success = true; // changez à false pour simuler une erreur

  if (success) {
    return const Result.success("Données utilisateur récupérées avec succès");
  } else {
    return const Result.error("Échec de la récupération des données utilisateur");
  }
}
```

Voici ce qui se passe :

* `Future<Result<String>> fetchUserData()` : Renvoie un objet `Result` qui contient des données de type `String`.
    
* `await Future.delayed(...)` : Simule un délai de 2 secondes, imitant un véritable appel réseau.
    
* `if (success) { ... } else { ... }` : Renvoie aléatoirement un résultat `success` ou `error`.
    

### Pattern Matching avec Freezed

L'une des meilleures parties de Freezed est le **pattern matching**. Vous pouvez gérer tous les états sans écrire de longues vérifications `if`.

```dart
void main() async {
  final result = await fetchUserData();

  result.when(
    loading: () => print("Chargement..."),
    success: (data) => print("Succès : $data"),
    error: (message) => print("Erreur : $message"),
  );
}
```

Voici ce qui se passe dans ce code :

* `result.when(...)` : Appelle le callback approprié en fonction de l'état.
    
    * S'il s'agit de `loading`, il exécute la fonction `loading`.
        
    * S'il s'agit de `success`, il exécute la fonction `success` avec les données.
        
    * S'il s'agit de `error`, il exécute la fonction `error` avec le message.
        

Cela garantit que tous les états sont gérés. Si vous en oubliez un, le compilateur affichera une erreur.

### MaybeWhen : Gérer les états partiels

`maybeWhen` est une version plus sûre et plus flexible de `when`. Alors que `when` vous oblige à gérer **tous les états possibles**, `maybeWhen` vous permet de ne gérer que ceux qui vous intéressent et de fournir une solution de repli avec `orElse`.

Cela le rend utile lorsque vous n'êtes pas intéressé par chaque état, mais seulement par un sous-ensemble.

Parfois, vous ne vous souciez que de certains états. Voici comment utiliser `maybeWhen` :

```dart
result.maybeWhen(
  success: (data) => print("Données reçues : $data"),
  orElse: () => print("Pas de données"),
);
```

Voici ce qui se passe :

* `success: (data)` s'exécute uniquement si l'état actuel est `success`.
    
* `orElse` agit comme un repli pour tous les autres états (`loading`, `error`, etc.).
    

Ainsi, dans cet extrait, le code montre comment vous pouvez réagir uniquement à l'état de succès tout en ignorant le reste en toute sécurité.

### Map : Travailler directement avec les objets d'état

Une autre approche est `map`, qui fournit l'instance complète de la classe :

```dart
result.map(
  loading: (value) => print("Actuellement en cours de chargement"),
  success: (value) => print("Succès obtenu : ${value.data}"),
  error: (value) => print("Erreur obtenue : ${value.message}"),
);
```

Ici, chaque branche reçoit la classe générée (`Loading`, `Success`, `Error`), vous donnant accès à tous les champs.

### Pourquoi utiliser les Unions ?

Les unions brillent lors de la construction d'applications Flutter avec une logique asynchrone. Par exemple :

* **Requêtes réseau** : `loading`, `success`, `error`
    
* **Validation de formulaire** : `valid`, `invalid`, `submitting`
    
* **Authentification** : `authenticated`, `unauthenticated`, `loading`
    

Au lieu d'écrire des drapeaux `bool isLoading` et `String? error` éparpillés dans votre application, les unions vous offrent un moyen structuré et type-safe de modéliser l'état.

## Conclusion

Freezed est un outil essentiel pour les développeurs Flutter qui souhaitent réduire le boilerplate tout en maintenant des modèles sûrs, immuables et facilement sérialisables.

En gérant le code répétitif tel que `copyWith`, les vérifications d'égalité et la sérialisation JSON, Freezed vous permet de vous concentrer sur la construction d'applications au lieu d'écrire du code répétitif.

Que vous soyez débutant ou développeur Flutter expérimenté, Freezed peut améliorer la lisibilité, la sécurité et la maintenabilité de votre base de code.

Pour les fonctionnalités avancées et les meilleures pratiques, visitez la documentation officielle de Freezed sur [pub.dev](https://pub.dev/packages/freezed).