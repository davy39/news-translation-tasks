---
title: Comment utiliser ObjectBox dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-16T17:07:32.404Z'
originalURL: https://freecodecamp.org/news/how-to-use-objectbox-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758042509445/329dd5bf-f143-4a35-9828-8441d501afed.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
seo_title: Comment utiliser ObjectBox dans Flutter
seo_desc: ObjectBox is a high-performance, lightweight, NoSQL embedded database built
  specifically for Flutter and Dart applications. It provides reactive APIs, indexes,
  relationships, and migrations, all designed to make local data management smooth
  and effic...
---

ObjectBox est une base de données NoSQL embarquée, performante et légère, conçue spécifiquement pour les applications Flutter et Dart. Elle propose des API réactives, des index, des relations et des migrations, le tout conçu pour rendre la gestion des données locales fluide et efficace.

Dans ce guide, nous allons intégrer ObjectBox dans un projet Flutter et implémenter les opérations CRUD fondamentales (Création, Lecture, Mise à jour, Suppression), tout en expliquant chaque étape en détail.

## Table des matières

* [Prérequis](#heading-pre-requis)
    
* [Facultatif mais recommandé](#heading-facultatif-mais-recommande)
    
* [Comment configurer un projet Flutter avec ObjectBox](#heading-comment-configurer-un-projet-flutter-avec-objectbox)
    
* [Comment initialiser ObjectBox](#heading-comment-initialiser-objectbox)
    
* [Comment créer un modèle de données](#heading-comment-creer-un-modele-de-donnees)
    
* [Comment implémenter les opérations CRUD](#heading-comment-implementer-les-operations-crud)
    
* [Comment intégrer les opérations CRUD à l'interface utilisateur Flutter](#heading-comment-integrer-les-operations-crud-a-linterface-utilisateur-flutter)
    
* [Fonctionnalités avancées d'ObjectBox](#heading-fonctionnalites-avancees-dobjectbox)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer avec ObjectBox dans Flutter, vous avez besoin d'un environnement de développement approprié. Assurez-vous d'avoir installé Flutter 3.x ou une version supérieure, ainsi que le SDK Dart fourni avec, et vérifiez l'installation avec `flutter --version`.

Vous aurez également besoin d'un IDE tel que VS Code, Android Studio ou IntelliJ avec les plugins Flutter et Dart. Les tests peuvent être effectués sur un émulateur ou un simulateur, mais un appareil réel est recommandé car certaines fonctionnalités d'ObjectBox y sont plus performantes. Si vous prévoyez de stocker la base de données dans des répertoires spécifiques à la plateforme, assurez-vous que votre application dispose des permissions de stockage de fichiers nécessaires, bien que les répertoires standards de l'application gèrent généralement cela automatiquement.

En termes de connaissances Flutter et Dart, vous devriez déjà être à l'aise avec les bases de Flutter telles que `StatelessWidget`, `StatefulWidget`, `setState()`, et les widgets courants comme `ListView.builder`, `Column`, `Row`, `Scaffold` et `AppBar`. La familiarité avec les composants d'interface utilisateur incluant `FloatingActionButton`, `TextField`, `Button`, `IconButton` et `ExpansionTile` est également importante. Côté Dart, vous devez comprendre les classes, les constructeurs, les champs, les paramètres nommés, les variables `late` et la programmation asynchrone avec `Future` et `Stream`. Savoir utiliser `FutureBuilder` et `StreamBuilder` dans Flutter rendra l'intégration beaucoup plus fluide.

Enfin, vous devrez saisir les concepts clés d'ObjectBox. Cela inclut les entités (classes Dart annotées avec `@Entity()` qui correspondent aux tables de la base de données), les clés primaires (généralement un entier `id`), et les boxes (`Box<T>`, qui représentent les tables et gèrent les opérations CRUD comme `put()`, `getAll()` et `remove()`). Comprendre les relations via `ToOne` et `ToMany`, travailler avec des requêtes réactives via `query().watch()`, et exécuter des opérations atomiques avec `store.runInTransaction()` sera essentiel. Les index avec `@Index()` peuvent également aider à optimiser les performances lors de la recherche sur des champs fréquemment consultés. Bien que facultatif, il est bénéfique d'avoir une bonne maîtrise des flux (streams) dans Flutter, de l'async/await en Dart, et une familiarité avec le package `path_provider` pour la gestion de l'emplacement de stockage de la base de données.

## Comment configurer un projet Flutter avec ObjectBox

Tout d'abord, assurez-vous d'avoir un projet Flutter prêt. Vous pouvez en créer un nouveau avec :

```bash
flutter create objectbox_demo
```

Une fois votre projet prêt, ouvrez `pubspec.yaml` et ajoutez la dépendance ObjectBox :

```yaml
dependencies:
  objectbox: ^4.3.1
```

`objectbox` est le package principal de la base de données. Le numéro de version `^4.3.1` garantit que vous obtenez une version compatible avec Flutter.

Récupérez les dépendances en exécutant :

```bash
flutter pub get
```

Ceci télécharge ObjectBox et le rend disponible pour votre projet.

## Comment initialiser ObjectBox

Pour utiliser ObjectBox, vous devez créer un "store" — le point d'accès principal à votre base de données.

Créez un nouveau fichier Dart, par exemple, `objectbox_setup.dart` :

```dart
import 'package:objectbox/objectbox.dart';

late final Store store;

Future<void> initObjectBox() async {
  store = await openStore(); // Initialise la base de données ObjectBox
}
```

**Explication :**

* `Store` est la classe centrale qui représente la base de données.
    
* `openStore()` ouvre la base de données et la prépare pour les opérations CRUD.
    
* `late final Store store;` garantit que le store est initialisé une seule fois et peut être accédé globalement.
    

**Astuce** : Vous pouvez également personnaliser le répertoire ou activer les migrations dans `openStore()` si votre schéma évolue.

## Comment créer un modèle de données

Dans ObjectBox, les données sont représentées sous forme d'entités. Chaque entité correspond à une classe Dart annotée avec `@Entity()`. Créons une entité `Task` :

```dart
import 'package:objectbox/objectbox.dart';

@Entity()
class Task {
  int? id; // Clé primaire générée automatiquement

  late String name;       // Nom de la tâche
  late DateTime createdAt; // Horodatage lors de la création de la tâche

  Task(this.name) : createdAt = DateTime.now(); // Constructeur
}
```

**Explication :**

* `@Entity()` marque la classe comme une entité ObjectBox.
    
* `id` est la clé primaire. ObjectBox la génère automatiquement si elle est nulle.
    
* Les champs `late` doivent être initialisés avant utilisation.
    
* `createdAt` stocke automatiquement l'horodatage lors de la création d'une `Task`.
    

## Comment implémenter les opérations CRUD

Pour un code propre, nous encapsulons les opérations de base de données dans une classe repository :

```dart
import 'package:objectbox/objectbox.dart';
import 'task.dart'; // Importez votre entité

class TaskRepository {
  final Store _store;
  late final Box<Task> _tasks;

  TaskRepository(this._store) : _tasks = _store.box<Task>();

  // CRÉER (CREATE)
  Future<void> addTask(String name) async {
    await _store.runInTransaction(() async {
      await _tasks.put(Task(name));
    });
  }

  // LIRE (READ)
  Future<List<Task>> getAllTasks() async {
    return _tasks.getAll();
  }

  // METTRE À JOUR (UPDATE)
  Future<void> updateTask(Task task) async {
    await _store.runInTransaction(() async {
      await _tasks.put(task); // Remplace l'enregistrement existant si l'id existe
    });
  }

  // SUPPRIMER (DELETE)
  Future<void> deleteTask(Task task) async {
    await _store.runInTransaction(() async {
      await _tasks.remove(task.id!);
    });
  }
}
```

**Analyse détaillée :**

* `Box<T>` : Un conteneur pour tous les objets de type `T`. Considérez cela comme une table dans une base de données relationnelle.
    
* `put()` : Insère un nouvel objet ou met à jour un objet existant si l' `id` existe.
    
* `getAll()` : Récupère tous les objets dans la box.
    
* `remove(id)` : Supprime un objet par son id.
    
* `runInTransaction()` : Garantit que toutes les opérations à l'intérieur du bloc sont atomiques — soit elles réussissent toutes, soit elles échouent toutes.
    

## Comment intégrer les opérations CRUD à l'interface utilisateur Flutter

Maintenant, connectons ObjectBox à une interface utilisateur Flutter pour des opérations CRUD interactives :

```dart
import 'package:flutter/material.dart';
import 'objectbox_setup.dart';
import 'task_repository.dart';
import 'task.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await initObjectBox(); // Initialiser ObjectBox
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: TaskListScreen(),
    );
  }
}

class TaskListScreen extends StatefulWidget {
  @override
  _TaskListScreenState createState() => _TaskListScreenState();
}

class _TaskListScreenState extends State<TaskListScreen> {
  final TaskRepository _taskRepository = TaskRepository(store);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Exemple CRUD ObjectBox')),
      body: FutureBuilder<List<Task>>(
        future: _taskRepository.getAllTasks(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Erreur : ${snapshot.error}'));
          } else {
            final tasks = snapshot.data ?? [];
            return ListView.builder(
              itemCount: tasks.length,
              itemBuilder: (context, index) {
                final task = tasks[index];
                return ListTile(
                  title: Text(task.name),
                  subtitle: Text('Créé le : ${task.createdAt}'),
                  trailing: IconButton(
                    icon: Icon(Icons.delete),
                    onPressed: () => _deleteTask(task),
                  ),
                );
              },
            );
          }
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _addTask,
        child: Icon(Icons.add),
      ),
    );
  }

  Future<void> _addTask() async {
    await _taskRepository.addTask('Nouvelle tâche');
    setState(() {}); // Rafraîchir l'interface après l'ajout
  }

  Future<void> _deleteTask(Task task) async {
    await _taskRepository.deleteTask(task);
    setState(() {}); // Rafraîchir l'interface après la suppression
  }
}
```

**Explication :**

* `FutureBuilder` : Gère la récupération asynchrone des tâches depuis ObjectBox.
    
* `ListView.builder` : Affiche efficacement une liste de tâches.
    
* `_addTask` & `_deleteTask` : Appellent les méthodes du repository et rafraîchissent l'interface utilisateur avec `setState()`.
    

## Fonctionnalités avancées d'ObjectBox

### Requêtes réactives

ObjectBox peut mettre à jour automatiquement l'interface utilisateur dès que la base de données change :

```dart
final reactiveTasks = _tasks.query().watch().listen((query) {
  // Ce bloc s'exécute chaque fois que les données changent
});
```

* `watch()` : Renvoie un flux qui émet des mises à jour en temps réel.
    
* Utile pour les mises à jour en direct dans les applications Flutter sans rafraîchissement manuel.
    

### Indexation

L'indexation accélère les performances des requêtes :

```dart
@Entity()
class Task {
  @Id(assignable: true)
  int? id;

  @Index()
  late String name;

  late DateTime createdAt;
}
```

* `@Index()` sur un champ crée un index pour des recherches plus rapides.
    
* Essentiel pour les grands ensembles de données.
    

### Relations

ObjectBox prend en charge les relations, permettant des modèles complexes :

```dart
@Entity()
class Project {
  int? id;
  late String name;

  @Backlink(to: 'project')
  final tasks = ToMany<Task>();
}
```

* `ToMany<Task>` : Un projet peut avoir plusieurs tâches.
    
* `@Backlink` : Connecte automatiquement `Task` à `Project`.
    

### Requêtes personnalisées

Effectuez des requêtes complexes avec filtres, tri et pagination :

```dart
final highPriorityTasks = _tasks.query()
    .greater(Task_.priority, 3)
    .order(Task_.createdAt)
    .build()
    .find();
```

* `greater()`, `less()`, `equal()` : Filtrent les enregistrements.
    
* `order()` : Trie par une propriété.
    

### Migrations

ObjectBox gère les changements de schéma :

```dart
final store = await openStore(
  directory: (await getApplicationDocumentsDirectory()).path,
  model: getObjectBoxModel(),
  onVersionChanged: (store, oldVersion, newVersion) {
    if (oldVersion == 1) {
      // Migrer le schéma de la version 1 vers la 2
    }
  },
);
```

* `onVersionChanged` : Exécute la logique de migration pour les mises à jour de schéma.
    

### Transactions et opérations par lots

Exécutez plusieurs opérations de manière atomique :

```dart
await _store.runInTransaction(() async {
  await _tasks.putMany([
    Task('Tâche 1'),
    Task('Tâche 2'),
    Task('Tâche 3'),
  ]);
});
```

* `putMany()` : Insère plusieurs objets efficacement.
    
* Garantit que soit tout réussit, soit rien n'est sauvegardé.
    

## Conclusion

ObjectBox offre une base de données locale rapide, réactive et facile à utiliser pour Flutter. Au-delà des opérations CRUD, elle prend en charge l'indexation, les relations, les requêtes réactives, les migrations et les transactions par lots. Cela en fait une solution idéale pour les applications Flutter nécessitant un stockage local robuste et des performances élevées.

Pour la documentation officielle et approfondir vos connaissances :

1. [Package ObjectBox Flutter](https://pub.dev/packages/objectbox)
    
2. [Documentation ObjectBox](https://docs.objectbox.io/)