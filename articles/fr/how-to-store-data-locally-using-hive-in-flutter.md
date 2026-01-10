---
title: Comment stocker des données localement avec Hive dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-09T14:36:07.693Z'
originalURL: https://freecodecamp.org/news/how-to-store-data-locally-using-hive-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757428555303/4228b0b2-9edf-48af-a917-2535b6adffa3.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: flutter-aware
  slug: flutter-aware
- name: hive
  slug: hive
seo_title: Comment stocker des données localement avec Hive dans Flutter
seo_desc: 'In this tutorial, we’ll build a Flutter application that demonstrates how
  to perform CRUD (Create, Read, Update, Delete) operations using Hive for local data
  storage.

  Hive is a lightweight, fast key-value database written in pure Dart. Unlike SQLite,...'
---

Dans ce tutoriel, nous allons construire une application Flutter qui démontre comment effectuer des opérations CRUD (Create, Read, Update, Delete) en utilisant [Hive](https://pub.dev/packages/hive) pour le stockage local des données.

Hive est une base de données clé-valeur légère et rapide écrite en pur Dart. Contrairement à SQLite, elle n'a pas besoin d'un moteur SQL lourd. Elle stocke les données dans des « boxes » (boîtes), que vous pouvez considérer comme des conteneurs (similaires aux tables, mais plus simples).

Pour une petite application CRUD comme celle-ci, Hive est un excellent choix car :

1. Elle est « offline-first » (conçue d'abord pour le mode hors ligne), et toutes les données sont stockées localement sur l'appareil – aucune connexion internet n'est requise.
    
2. Elle est « type-safe » (sécurisée au niveau des types) et s'intègre bien avec les modèles Dart (comme notre `Item`).
    
3. Elle est beaucoup plus rapide que SQLite pour les opérations simples.
    
4. Elle dispose d'une API adaptée à Flutter (`hive_flutter`) pour des fonctionnalités telles que les mises à jour réactives.
    

Hive est idéal pour de nombreux cas d'utilisation différents, comme le stockage des préférences/paramètres de l'application, la gestion de listes de données structurées de petite à moyenne taille (comme des notes, des tâches ou des listes de courses), la mise en cache hors ligne pour les réponses d'API et le stockage local des données de session ou de profil utilisateur.

Ici, Hive alimente une liste d'articles de type gestion de tâches ou inventaire, ce qui signifie que tout (titre, quantité) est stocké localement et persiste même après le redémarrage de l'application.

À la fin de ce tutoriel, vous disposerez d'une application entièrement fonctionnelle qui vous permettra d'ajouter, de modifier, de supprimer et de visualiser des éléments localement. Je fournirai des explications claires sur le code tout au long du processus.

## Table des matières :

1. [Prérequis](#heading-pre-requis)
    
2. [Étape 1 : Configuration du projet](#heading-etape-1-configuration-du-projet)
    
3. [Étape 2 : Structure des dossiers du projet](#heading-etape-2-structure-des-dossiers-du-projet)
    
4. [Étape 3 : Implémentation de l'application](#heading-etape-3-implementation-de-l-application)
    
    * [1\. main.dart](#heading-1-maindart)
        
    * [2\. item.dart (Modèle)](#heading-2-itemdart-modele)
        
    * [3\. controller.dart (Contrôleur Hive)](#heading-3-controllerdart-controleur-hive)
        
        * [Importations](#heading-importations)
            
        * [Définition de la classe et constructeur](#heading-definition-de-la-classe-et-constructeur)
            
        * [Référence à la Box Hive](#heading-reference-a-la-box-hive)
            
        * [Récupération des données](#heading-recuperation-des-donnees)
            
        * [Création d'un élément](#heading-creation-dun-element)
            
        * [Modification d'un élément](#heading-modification-dun-element)
            
        * [Suppression d'un élément](#heading-suppression-dun-element)
            
        * [Suppression de tous les éléments](#heading-suppression-de-tous-les-elements)
            
        * [Assistant après action](#heading-assistant-apres-action)
            
    * [4\. string\_constants.dart](#heading-4-stringconstantsdart)
        
    * [5\. status.dart (Enum)](#heading-5-statusdart-enum)
        
    * [6\. yes\_no.dart (Enum)](#heading-6-yesnodart-enum)
        
    * [7\. toast.dart](#heading-7-toastdart)
        
    * [8\. are\_you\_sure.dart (Dialogue de confirmation)](#heading-8-areyousuredart-dialogue-de-confirmation)
        
    * [9\. single\_list\_tile.dart (Widget d'élément de liste)](#heading-9-singlelisttiledart-widget-delement-de-liste)
        
    * [10\. main\_screen.dart (Interface utilisateur + Gestion d'état)](#heading-10-mainscreendart-ui-gestion-detat)
        
5. [Captures d'écran](#heading-captures-decran)
    
6. [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :

1. Le SDK Flutter installé (version 3.0 ou supérieure recommandée).
    
2. Des connaissances de base sur Flutter : widgets, widgets stateful/stateless et navigation.
    
3. Un éditeur de code comme VS Code ou Android Studio.
    
4. Une familiarité avec les classes, les maps et les enums Dart.
    

## Étape 1 : Configuration du projet

Commencez par créer un nouveau projet Flutter :

```bash
flutter create flutter_hive_crud
cd flutter_hive_crud
```

Ouvrez `pubspec.yaml` et ajoutez les dépendances suivantes :

```yaml
dependencies:
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  fluttertoast: ^8.2.12
  equatable: ^2.0.7
```

Installez-les :

```bash
flutter pub get
```

* `hive` – Base de données clé-valeur légère pour Flutter.
    
* `hive_flutter` – Liaisons Flutter pour Hive.
    
* `fluttertoast` – Affiche des messages toast.
    
* `equatable` – Simplifie l'égalité des valeurs dans les objets Dart.
    

## Étape 2 : Structure des dossiers du projet

Organisez votre projet comme suit :

```dart
lib/
├── main.dart
├── model/
│   └── item.dart
├── controller/
│   └── controller.dart
├── constants/
│   ├── string_constants.dart
│   └── enums/
│       ├── status.dart
│       └── yes_no.dart
└── screens/
    ├── main_screen.dart
    └── widgets/
        ├── are_you_sure.dart
        ├── single_list_tile.dart
        ├── text_action.dart
        └── toast.dart
```

Cette structure permet de garder l'application modulaire et facile à maintenir.

## Étape 3 : Implémentation de l'application

Nous allons passer en revue le processus fichier par fichier, et j'expliquerai le rôle de chaque partie au fur et à mesure.

### 1\. `main.dart`

C'est le point d'entrée de l'application. Il initialise Hive et lance l'application.

```dart
import 'package:flutter/material.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'screens/main_screen.dart';
import 'constants/string_constants.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialiser Hive pour Flutter
  await Hive.initFlutter();

  // Ouvrir la box Hive pour stocker les éléments
  await Hive.openBox(StringConstants.hiveBox);

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Hive CRUD',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.brown),
        useMaterial3: true,
      ),
      home: const MainScreen(),
    );
  }
}
```

Voici ce qui se passe dans ce code :

* `WidgetsFlutterBinding.ensureInitialized()` garantit que les widgets Flutter sont prêts.
    
* `Hive.initFlutter()` initialise Hive dans Flutter.
    
* `Hive.openBox(...)` ouvre une boîte de stockage persistante.
    
* `MyApp` configure le thème Material et l'écran principal.
    

### 2\. `item.dart` (Modèle)

Comme Hive stocke les données sous forme de paires clé-valeur, nous devons décider comment représenter chaque élément (comme une entrée de liste de courses ou un produit en stock). Pour garder notre code organisé, nous allons envelopper chaque élément dans une classe Dart appelée `Item`. De cette façon, nous pouvons facilement créer, mettre à jour et convertir des éléments en Maps lors de leur enregistrement dans Hive.

```dart
import 'package:equatable/equatable.dart';

class Item extends Equatable {
  final String title;
  final int quantity;

  const Item({required this.title, required this.quantity});

  @override
  List<Object> get props => [title, quantity];

  // Convertir l'Item en Map pour le stockage Hive
  Map<String, dynamic> toMap() {
    return {'title': title, 'quantity': quantity};
  }

  // Créer un Item à partir d'une Map
  factory Item.fromMap(Map<String, dynamic> map) {
    return Item(title: map['title'], quantity: map['quantity']);
  }
}
```

Ainsi, chaque fois que nous sauvegardons ou récupérons des données, nous effectuons simplement une conversion entre `Item` (instance de classe) et `Map` (format Hive).

Voici ce qui se passe :

* `Equatable` permet de comparer les éléments par valeur plutôt que par référence.
    
* `toMap()` et `fromMap()` effectuent la conversion entre les objets Dart et le format de stockage Hive.
    

### 3\. `controller.dart` (Contrôleur Hive)

Ce contrôleur gère toutes les opérations CRUD de Hive et les mises à jour de l'interface utilisateur (UI).

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hive_crud/constants/string_constants.dart';
import 'package:flutter_hive_crud/screens/widgets/toast.dart';
import 'package:hive_flutter/hive_flutter.dart';
import '../constants/enums/status.dart';
import '../model/item.dart';

class HiveController {
  final BuildContext context;
  final Function fetchDataFunction;

  HiveController({required this.context, required this.fetchDataFunction});

  final hiveBox = Hive.box(StringConstants.hiveBox);

  // Récupérer tous les éléments de Hive
  List<Map<String, dynamic>> fetchData() {
    return hiveBox.keys.map((key) {
      final item = hiveBox.get(key);
      return {
        'key': key,
        'title': item['title'],
        'quantity': item['quantity'],
      };
    }).toList().reversed.toList();
  }

  Future<void> createItem({required Item item}) async {
    try {
      await hiveBox.add(item.toMap());
      afterAction('saved');
    } catch (e) {
      toastInfo(msg: 'Failed to create item', status: Status.error);
    }
  }

  Future<void> editItem({required Item item, required int itemKey}) async {
    try {
      hiveBox.put(itemKey, item.toMap());
      afterAction('edited');
    } catch (e) {
      toastInfo(msg: 'Failed to edit item', status: Status.error);
    }
  }

  Future<void> deleteItem({required int key}) async {
    try {
      await hiveBox.delete(key);
      afterAction('deleted');
    } catch (e) {
      toastInfo(msg: 'Failed to delete item', status: Status.error);
    }
  }

  Future<void> clearItems() async {
    try {
      await hiveBox.clear();
      afterAction('cleared');
    } catch (e) {
      toastInfo(msg: 'Failed to clear items', status: Status.error);
    }
  }

  void afterAction(String keyword) {
    toastInfo(msg: 'Item $keyword successfully', status: Status.success);
    fetchDataFunction(); // Rafraîchir l'UI
    Navigator.of(context).pop(); // Fermer les modales
  }
}
```

Analysons ce bloc de code `HiveController` étape par étape.

#### Importations :

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hive_crud/constants/string_constants.dart';
import 'package:flutter_hive_crud/screens/widgets/toast.dart';
import 'package:hive_flutter/hive_flutter.dart';
import '../constants/enums/status.dart';
import '../model/item.dart';
```

Voici ce qui se passe :

* `flutter/material.dart` – Fournit les widgets et utilitaires de conception Material de Flutter.
    
* `string_constants.dart` – Contient les constantes globales de l'application, comme le nom de la box Hive.
    
* `toast.dart` – Utilitaire pour afficher des messages toast en cas de succès ou d'erreur.
    
* `hive_flutter.dart` – Intégration du package Hive avec Flutter.
    
* `status.dart` – Enum représentant les types d'état (`error` ou `success`) pour les messages toast.
    
* `item.dart` – La classe modèle représentant un élément individuel (titre + quantité).
    

Ces importations permettent au contrôleur de gérer les données Hive et d'interagir avec l'interface utilisateur.

#### Définition de la classe et constructeur :

```dart
class HiveController {
  final BuildContext context;
  final Function fetchDataFunction;

  HiveController({required this.context, required this.fetchDataFunction});
```

Voici le rôle de chaque élément :

* `HiveController` – Cette classe gère toutes les opérations CRUD pour Hive.
    
* `context` – Le `BuildContext` actuel de Flutter, utilisé pour la navigation et l'affichage des modales ou dialogues.
    
* `fetchDataFunction` – Une fonction transmise par l'interface utilisateur qui actualise la liste après avoir effectué une opération Hive.
    

Le constructeur requiert les deux paramètres, garantissant que chaque instance de `HiveController` a accès au contexte de l'interface utilisateur et à un moyen de rafraîchir les données.

#### Référence à la box Hive :

```dart
  final hiveBox = Hive.box(StringConstants.hiveBox);
```

Ici,

* `hiveBox` est une référence à la box Hive définie dans `StringConstants.hiveBox`.
    
* Une box Hive est comparable à un magasin clé-valeur où nous enregistrons nos articles localement.
    
* Cela permet au contrôleur d'interagir avec Hive sans avoir à rouvrir la boîte à chaque fois.
    

#### Récupération des données :

```dart
  List<Map<String, dynamic>> fetchData() {
    return hiveBox.keys.map((key) {
      final item = hiveBox.get(key);
      return {
        'key': key,
        'title': item['title'],
        'quantity': item['quantity'],
      };
    }).toList().reversed.toList();
  }
```

Voici ce que fait ce code :

* `hiveBox.keys` – Récupère toutes les clés stockées dans la box Hive.
    
* `.map((key) => ...)` – Parcourt chaque clé et récupère l'élément associé.
    
* Convertit chaque élément en une Map contenant :
    
    * `'key'` – La clé Hive unique (utilisée pour les mises à jour/suppressions).
        
    * `'title'` – Le titre de l'élément.
        
    * `'quantity'` – La quantité de l'élément.
        
* `.toList().reversed.toList()` – Convertit l'itérable mappé en liste et l'inverse pour que les **éléments les plus récents apparaissent en premier**.
    

Cette méthode renvoie une liste d'éléments prêts à être affichés dans l'interface utilisateur.

#### Création d'un élément :

```dart
  Future<void> createItem({required Item item}) async {
    try {
      await hiveBox.add(item.toMap());
      afterAction('saved');
    } catch (e) {
      toastInfo(msg: 'Failed to create item', status: Status.error);
    }
  }
```

Dans ce code,

* `item.toMap()` – Convertit l'objet `Item` en Map pour que Hive puisse le stocker.
    
* `hiveBox.add(...)` – Ajoute une nouvelle entrée à la box Hive, générant automatiquement une clé unique.
    
* `afterAction('saved')` – Affiche un toast de succès, rafraîchit l'interface utilisateur et ferme toute modale ouverte.
    
* Le bloc `catch` gère les erreurs et affiche un toast en cas de problème.
    

#### Modification d'un élément :

```dart
  Future<void> editItem({required Item item, required int itemKey}) async {
    try {
      hiveBox.put(itemKey, item.toMap());
      afterAction('edited');
    } catch (e) {
      toastInfo(msg: 'Failed to edit item', status: Status.error);
    }
  }
```

Dans ce code,

* `hiveBox.put(itemKey, item.toMap())` – Met à jour l'élément à la clé spécifique avec les nouvelles données.
    
* `afterAction('edited')` – Gère les retours et les mises à jour de l'interface utilisateur.
    
* Le bloc `catch` gère toutes les erreurs pendant le processus d'édition.
    

#### Suppression d'un élément :

```dart
  Future<void> deleteItem({required int key}) async {
    try {
      await hiveBox.delete(key);
      afterAction('deleted');
    } catch (e) {
      toastInfo(msg: 'Failed to delete item', status: Status.error);
    }
  }
```

Ici,

* `hiveBox.delete(key)` – Supprime de Hive l'élément associé à la clé spécifiée.
    
* Appelle `afterAction('deleted')` pour rafraîchir l'interface utilisateur et afficher un message de succès.
    
* Les erreurs sont gérées avec un toast.
    

#### Suppression de tous les éléments :

```dart
  Future<void> clearItems() async {
    try {
      await hiveBox.clear();
      afterAction('cleared');
    } catch (e) {
      toastInfo(msg: 'Failed to clear items', status: Status.error);
    }
  }
```

Voici ce qui se passe :

* `hiveBox.clear()` – Supprime **tous les éléments** de la box Hive.
    
* Utile pour la fonctionnalité « Tout effacer » de l'application.
    
* Le succès et les erreurs sont gérés de la même manière que pour les autres actions.
    

#### Assistant après action :

```dart
  void afterAction(String keyword) {
    toastInfo(msg: 'Item $keyword successfully', status: Status.success);
    fetchDataFunction(); // Rafraîchir l'UI
    Navigator.of(context).pop(); // Fermer les modales
  }
```

Voici le fonctionnement :

* `toastInfo(...)` – Affiche un toast de succès, par exemple « Item saved successfully ».
    
* `fetchDataFunction()` – Appelle la fonction transmise par l'interface utilisateur pour recharger la liste.
    
* `Navigator.of(context).pop()` – Ferme toute modale ou dialogue ouvert (comme le formulaire d'élément).
    

Cette méthode évite la répétition en centralisant la logique après toute opération CRUD.

**Résumé des responsabilités de HiveController :**

1. Récupérer les éléments de Hive pour l'affichage de l'interface utilisateur.
    
2. Créer, mettre à jour, supprimer et effacer des éléments.
    
3. Fournir un retour à l'utilisateur via des messages toast.
    
4. Rafraîchir l'interface utilisateur automatiquement après tout changement de données.
    
5. Gérer les modales et les dialogues avec le contexte.
    
6. `HiveController` abstrait les opérations Hive pour un code d'interface utilisateur plus propre.
    
7. Méthodes : `createItem`, `editItem`, `deleteItem`, `clearItems`.
    
8. `afterAction` met à jour l'interface utilisateur et affiche des messages de succès.
    

### 4\. `string_constants.dart`

Il s'agit du stockage centralisé des constantes de chaînes de caractères comme les noms de box Hive.

```dart
class StringConstants {
  static const hiveBox = 'items';
}
```

Dans ce code :

* `class StringConstants` – Définit une classe uniquement utilisée pour regrouper des valeurs constantes.
    
* `static` – Signifie que vous n'avez pas besoin de créer une instance de `StringConstants` pour l'utiliser. Vous pouvez y accéder directement via `StringConstants.hiveBox`.
    
* `const` – En fait une constante au moment de la compilation, elle ne peut donc être modifiée nulle part dans votre code.
    
* `'items'` – Il s'agit simplement d'une valeur de chaîne. Dans ce cas, c'est le nom de la box Hive que vous allez ouvrir.
    

### 5\. `status.dart` (Enum)

```dart
enum Status { error, success }
```

Dans ce code :

* `enum` – Abréviation d'**énumération**. C'est un type spécial qui vous permet de définir un ensemble fixe de valeurs nommées.
    
* `Status` – Le nom de l'enum.
    
* `{ error, success }` – Les valeurs possibles que cet enum peut prendre.
    

Ainsi, `Status` est désormais un type personnalisé avec seulement **deux valeurs valides** :

```dart
Status.error
Status.success
```

#### Pourquoi l'utiliser ici ?

Au lieu de manipuler des chaînes de caractères simples comme `"error"` ou `"success"` (qui sont faciles à mal orthographier), le code peut utiliser `Status.error` ou `Status.success`.

Par exemple, lors de l'affichage d'un toast :

```python
toastInfo(msg: 'Item deleted', status: Status.success);
```

Ou :

```dart
toastInfo(msg: 'Failed to delete item', status: Status.error);
```

Cela rend le code plus sûr (vous ne pouvez pas accidentellement passer `"sucess"` et casser des choses), plus clair (vous voyez l'intention immédiatement) et plus facile à maintenir (si vous ajoutez d'autres statuts plus tard comme `warning` ou `info`, il n'y a qu'un seul endroit à mettre à jour).

### 6\. `yes_no.dart` (Enum)

```dart
enum YesNo { yes, no }
```

* Définit un nouveau type appelé `YesNo`.
    
* Il ne peut avoir que **deux valeurs possibles** :
    
    * `YesNo.yes`
        
    * `YesNo.no`
        

#### Pourquoi l'utiliser ?

Au lieu de manipuler des booléens (`true` / `false`) ou des chaînes (`"yes"` / `"no"`), vous pouvez utiliser cet enum pour rendre votre intention beaucoup plus claire dans le code.

Par exemple :

```dart
YesNo userAccepted = YesNo.yes;

if (userAccepted == YesNo.yes) {
  print("User agreed!");
} else {
  print("User declined!");
}
```

C'est plus descriptif que d'utiliser un simple `bool` où vous devriez deviner ce que signifie `true` ou `false` dans le contexte.

#### Cas d'utilisation courants :

* Confirmations (par exemple, *« Voulez-vous enregistrer ce fichier ? »*).
    
* Bascules de paramètres (par exemple, *« Activer les notifications ? »*).
    
* Réponses d'API qui renvoient `"yes"` / `"no"` sous forme de chaînes. Vous pouvez les mapper à cet enum pour une gestion plus sûre.
    

### 7\. `toast.dart`

```dart
import 'package:fluttertoast/fluttertoast.dart';
import '../../../constants/enums/status.dart';

void toastInfo({required String msg, required Status status}) {
  Fluttertoast.showToast(
    msg: msg,
    backgroundColor: status == Status.error ? Colors.red : Colors.green,
    toastLength: Toast.LENGTH_LONG,
    gravity: ToastGravity.TOP,
  );
}
```

C'est une fonction utilitaire pour afficher des messages toast dans votre application Flutter.

Un **toast** est un petit message contextuel temporaire (généralement en bas ou en haut de l'écran) utilisé pour informer rapidement l'utilisateur de quelque chose. Par exemple, vous pourriez avoir *« Élément enregistré avec succès »* ou *« Erreur lors de la suppression de l'élément »*.

### 8\. `are_you_sure.dart` (Dialogue de confirmation)

```dart
import 'dart:io';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

Future<void> areYouSureDialog({
  required String title,
  required String content,
  required BuildContext context,
  required Function action,
  bool isKeyInvolved = false,
  int key = 0,
}) {
  return showDialog(
    context: context,
    builder: (context) => Platform.isIOS
        ? CupertinoAlertDialog(
            title: Text(title),
            content: Text(content),
            actions: [
              CupertinoDialogAction(
                  onPressed: () =>
                      isKeyInvolved ? action(key: key) : action(),
                  child: const Text('Yes')),
              CupertinoDialogAction(
                  onPressed: () => Navigator.of(context).pop(),
                  child: const Text('Dismiss')),
            ],
          )
        : AlertDialog(
            title: Text(title),
            content: Text(content),
            actions: [
              ElevatedButton(
                  onPressed: () =>
                      isKeyInvolved ? action(key: key) : action(),
                  child: const Text('Yes')),
              ElevatedButton(
                  onPressed: () => Navigator.of(context).pop(),
                  child: const Text('Dismiss')),
            ],
          ),
  );
}
```

Ce code gère les confirmations des utilisateurs pour des actions telles que la suppression ou l'effacement.

Cette fonction affiche une boîte de dialogue de confirmation sensible à la plateforme (« Êtes-vous sûr ? ») qui :

1. Fonctionne sur iOS avec un `CupertinoAlertDialog`.
    
2. Fonctionne sur Android/autres avec un Material `AlertDialog`.
    
3. Appelle une `action` fournie lorsque l'utilisateur appuie sur « Yes ».
    
4. Ferme le dialogue lorsque l'utilisateur appuie sur « Dismiss ».
    
5. Passe éventuellement une clé (`key`) à la fonction d'action.
    

### 9\. `single_list_tile.dart` (Widget d'élément de liste)

```dart
import 'package:flutter/material.dart';
import '../../model/item.dart';
import 'text_action.dart';
import '../../constants/enums/yes_no.dart';

class SingleListItem extends StatelessWidget {
  final Item item;
  final int itemKey;
  final Function editHandle;
  final Function deleteDialog;
  final Function deleteItem;

  const SingleListItem({
    super.key,
    required this.item,
    required this.itemKey,
    required this.editHandle,
    required this.deleteDialog,
    required this.deleteItem,
  });

  @override
  Widget build(BuildContext context) {
    return Dismissible(
      key: ValueKey(itemKey),
      confirmDismiss: (_) => showDialog(
        context: context,
        builder: (_) => AlertDialog(
          title: const Text('Are you sure?'),
          content: Text('Delete ${item.title}?'),
          actions: [
            textAction('Yes', YesNo.yes, context),
            textAction('No', YesNo.no, context),
          ],
        ),
      ),
      onDismissed: (_) => deleteItem(key: itemKey),
      background: Container(
        color: Colors.red,
        alignment: Alignment.centerRight,
        padding: const EdgeInsets.only(right: 20),
        child: const Icon(Icons.delete, color: Colors.white),
      ),
      child: ListTile(
        title: Text(item.title),
        subtitle: Text(item.quantity.toString()),
        trailing: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            IconButton(onPressed: () => editHandle(item: item, key: itemKey), icon: const Icon(Icons.edit)),
            IconButton(onPressed: () => deleteDialog(key: itemKey), icon: const Icon(Icons.delete)),
          ],
        ),
      ),
    );
    
  }
}
```

Ce code représente chaque élément de la liste avec des options d'édition/suppression et une fonctionnalité de suppression par balayage (swipe).

Ce widget représente **un élément** (comme une ligne dans une liste de courses, une liste de tâches, une application d'inventaire, etc.) avec :

1. Une fonctionnalité de suppression par balayage.
    
2. Des boutons d'édition et de suppression.
    
3. Une boîte de dialogue de confirmation avant la suppression.
    

### 10\. `main_screen.dart` (UI + Gestion d'état)

C'est l'écran principal qui assemble le tout, y compris les formulaires, les listes et les modales.
En raison de sa longueur, l'explication complète est déjà bien commentée dans le code d'origine, couvrant :

* `itemModal()` – Formulaire en bas de l'écran pour la création/l'édition.
    
* `fetchData()` – Chargement des éléments depuis Hive.
    
* `editHandle()` – Chargement d'un élément pour l'édition.
    
* `deleteDialog()` – Confirmation de suppression.
    
* `clearAllDialog()` – Confirmation de la suppression de tous les éléments.
    

## Captures d'écran

![capture d'écran d'une liste remplie](https://cdn.hashnode.com/res/hashnode/image/upload/v1703246520284/6d8ab811-24f4-4482-82f3-a1ab37eff384.png align="center")

![capture d'écran de l'ajout d'un nouvel élément](https://cdn.hashnode.com/res/hashnode/image/upload/v1703246525459/80ac292a-271d-4adf-b2bb-7dfbdb57170d.png align="center")

![capture d'écran d'un dialogue demandant de confirmer la suppression d'un élément sur iOS](https://cdn.hashnode.com/res/hashnode/image/upload/v1703246531588/5e88c1ca-1ae0-4655-be16-e6646ef5e97d.png align="center")

![capture d'écran d'une boîte de dialogue de confirmation de suppression sur Android](https://cdn.hashnode.com/res/hashnode/image/upload/v1703246535449/aa2f7469-bbab-4c5d-bf8d-25ce9ba01743.png align="center")

![capture d'écran d'une boîte de dialogue pour effacer les éléments](https://cdn.hashnode.com/res/hashnode/image/upload/v1703246539025/233ddf98-62c8-4c0f-89b0-344be26dfabe.png align="center")

![capture d'écran d'une notification toast](https://cdn.hashnode.com/res/hashnode/image/upload/v1703246543769/13c5ecba-0916-4083-ab00-e756543f7643.png align="center")

![capture d'écran d'un état vide](https://cdn.hashnode.com/res/hashnode/image/upload/v1703246547869/33aae852-e656-43a6-b41b-887cedd81e47.png align="center")

## Conclusion

Vous disposez maintenant d'une application Flutter entièrement fonctionnelle utilisant Hive pour la persistance locale des données. Votre application peut :

* Créer, Lire, Mettre à jour, Supprimer des éléments.
    
* Afficher des messages toast pour les retours utilisateur.
    
* Confirmer les actions avec des dialogues pour Android et iOS.
    
* Utiliser une architecture propre et modulaire avec des contrôleurs, des modèles et des widgets.
    

Vous pouvez explorer davantage Hive dans la [Documentation du package Hive](https://pub.dev/packages/hive) si vous souhaitez en savoir plus.