---
title: Comment stocker des données localement avec Isar dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-19T13:09:48.736Z'
originalURL: https://freecodecamp.org/news/store-data-locally-with-isar-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758287132737/7886bedc-374f-401d-b59c-04c59590e81f.png
tags:
- name: Flutter
  slug: flutter
- name: NoSQL
  slug: nosql
- name: database
  slug: database
- name: Dart
  slug: dart
seo_title: Comment stocker des données localement avec Isar dans Flutter
seo_desc: When building Flutter applications, managing local data efficiently is critical.
  You want a database that is lightweight, fast, and easy to integrate, especially
  if your app will work offline. Isar is one such database. It is a high-performance,
  easy...
---

Lors du développement d'applications Flutter, la gestion efficace des données locales est cruciale. Vous avez besoin d'une base de données légère, rapide et facile à intégrer, particulièrement si votre application doit fonctionner hors ligne. Isar est l'une de ces bases de données. C'est une base de données NoSQL intégrée de haute performance et facile à utiliser, conçue sur mesure pour Flutter. Avec des fonctionnalités telles que les requêtes réactives, les index, les relations, les migrations et les transactions, Isar rend la persistance des données locales à la fois puissante et conviviale pour les développeurs.

Dans cet article, vous apprendrez comment intégrer Isar dans un projet Flutter, configurer un modèle de données et effectuer la gamme complète des opérations CRUD (Création, Lecture, Mise à jour, Suppression). Pour rendre cela concret, vous allez construire une application de liste de tâches (to-do app) simple qui permet aux utilisateurs de créer, consulter, mettre à jour et supprimer des tâches.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
    
* [Comment configurer Isar dans un projet Flutter](#heading-comment-configurer-isar-dans-un-projet-flutter)
    
* [Comment créer le modèle de tâche](#heading-comment-creer-le-modele-de-tache)
    
* [Comment construire le repository pour les opérations CRUD](#heading-comment-construire-le-repository-pour-les-operations-crud)
    
* [Comment intégrer le CRUD dans l'UI Flutter](#heading-comment-integrer-le-crud-dans-l-ui-flutter)
    
* [Au-delà du CRUD : Fonctionnalités avancées d'Isar](#heading-au-dela-du-crud-fonctionnalites-avancees-d-isar)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :

1. **SDK Flutter** installé (version 3.0 ou supérieure recommandée).  
    Vérifiez votre version avec :
    
    ```bash
    flutter --version
    ```
    
2. **Connaissances en Dart** : Familiarité avec la syntaxe Dart, les classes et la programmation asynchrone.
    
3. **Bases de Flutter** : Vous devez savoir comment configurer un projet Flutter, construire des widgets et utiliser `FutureBuilder` ou `setState` pour la gestion d'état.
    
4. **Éditeur de code** : VS Code ou Android Studio est recommandé.
    

Si tout cela est en place, nous sommes prêts à commencer.

## Ce que nous allons construire

Nous allons créer une application de gestion de tâches qui permet aux utilisateurs de :

* Ajouter de nouvelles tâches.
    
* Afficher toutes les tâches dans une liste.
    
* Mettre à jour les tâches existantes.
    
* Supprimer des tâches.
    

À la fin, vous aurez une application CRUD entièrement fonctionnelle construite avec Flutter et Isar.

## Comment configurer Isar dans un projet Flutter

### Étape 1 : Ajouter les dépendances

Ouvrez votre fichier `pubspec.yaml` et ajoutez ce qui suit :

```yaml
dependencies:
  flutter:
    sdk: flutter
  isar: ^3.1.0
  isar_flutter_libs: ^3.1.0

dev_dependencies:
  isar_generator: ^3.1.0
  build_runner: any
```

* `isar` : Le package Isar principal.
    
* `isar_flutter_libs` : Requis pour l'intégration Flutter.
    
* `isar_generator` : Utilisé pour générer le code de vos modèles.
    
* `build_runner` : Exécute le générateur de code.
    

Exécutez :

```bash
flutter pub get
```

### Étape 2 : Créer et initialiser Isar

Créez un fichier nommé `isar_setup.dart`. Celui-ci gérera l'ouverture de la base de données Isar.

```dart
import 'package:isar/isar.dart';
import 'package:path_provider/path_provider.dart';
import 'task.dart'; // we will create this model soon

late final Isar isar;

Future<void> initializeIsar() async {
  final dir = await getApplicationDocumentsDirectory();
  isar = await Isar.open(
    [TaskSchema],
    directory: dir.path,
  );
}
```

**Explication** :

* `getApplicationDocumentsDirectory()` fournit un emplacement de stockage pour le fichier de base de données.
    
* `Isar.open()` initialise la base de données et enregistre notre schéma `Task`.
    
* `late final Isar isar;` garantit que nous pouvons accéder à l'instance de la base de données globalement après l'initialisation.
    

## Comment créer le modèle de tâche

Définissons maintenant notre modèle de données pour les tâches. Créez un fichier nommé `task.dart`.

```dart
import 'package:isar/isar.dart';

part 'task.g.dart';

@Collection()
class Task {
  Id id = Isar.autoIncrement; // auto-incrementing primary key

  late String name;

  late DateTime createdAt;

  Task(this.name) : createdAt = DateTime.now();
}
```

**Explication** :

* `@Collection()` indique à Isar que cette classe représente une collection de base de données.
    
* `Id id = Isar.autoIncrement;` crée automatiquement un identifiant unique.
    
* `late String name;` stocke le nom de la tâche.
    
* `late DateTime createdAt;` stocke l'horodatage de création.
    
* `part 'task.g.dart';` établit le lien avec le code généré, qui sera créé après l'exécution du générateur de code.
    

Générez le code avec :

```bash
flutter pub run build_runner build
```

Cela génère `task.g.dart`, qui contient le code de schéma nécessaire.

## Comment construire le repository pour les opérations CRUD

Créez un nouveau fichier nommé `task_repository.dart`. Il contiendra les méthodes d'interaction avec la base de données.

```dart
import 'package:isar/isar.dart';
import 'task.dart';
import 'isar_setup.dart';

class TaskRepository {
  Future<void> addTask(String name) async {
    final task = Task(name);
    await isar.writeTxn(() async {
      await isar.tasks.put(task);
    });
  }

  Future<List<Task>> getAllTasks() async {
    return await isar.tasks.where().findAll();
  }

  Future<void> updateTask(Task task) async {
    await isar.writeTxn(() async {
      await isar.tasks.put(task);
    });
  }

  Future<void> deleteTask(Task task) async {
    await isar.writeTxn(() async {
      await isar.tasks.delete(task.id);
    });
  }
}
```

**Explication** :

* `addTask` : Crée une nouvelle tâche et l'enregistre.
    
* `getAllTasks` : Lit toutes les tâches de la base de données.
    
* `updateTask` : Met à jour une tâche existante en appelant à nouveau `.put()`.
    
* `deleteTask` : Supprime une tâche par son `id`.
    
* `isar.writeTxn` : Garantit que les opérations s'exécutent dans une transaction pour la sécurité et la cohérence.
    

## Comment intégrer le CRUD dans l'UI Flutter

Maintenant, connectons le tout dans `main.dart`.

```dart
import 'package:flutter/material.dart';
import 'isar_setup.dart';
import 'task_repository.dart';
import 'task.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await initializeIsar(); // initialize Isar before runApp
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
  final TaskRepository _taskRepository = TaskRepository();
  late Future<List<Task>> _tasksFuture;

  @override
  void initState() {
    super.initState();
    _tasksFuture = _taskRepository.getAllTasks();
  }

  Future<void> _addTask() async {
    await _taskRepository.addTask('New Task');
    setState(() {
      _tasksFuture = _taskRepository.getAllTasks();
    });
  }

  Future<void> _deleteTask(Task task) async {
    await _taskRepository.deleteTask(task);
    setState(() {
      _tasksFuture = _taskRepository.getAllTasks();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Isar CRUD Example')),
      body: FutureBuilder<List<Task>>(
        future: _tasksFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            final tasks = snapshot.data ?? [];
            if (tasks.isEmpty) {
              return Center(child: Text('No tasks yet.'));
            }
            return ListView.builder(
              itemCount: tasks.length,
              itemBuilder: (context, index) {
                final task = tasks[index];
                return ListTile(
                  title: Text(task.name),
                  subtitle: Text('Created at: ${task.createdAt}'),
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
}
```

**Explication** :

* `initializeIsar()` : Garantit que la base de données est prête avant le lancement de l'application.
    
* `_tasksFuture` : Contient un Future de la liste des tâches.
    
* `_addTask` : Ajoute une nouvelle tâche et rafraîchit la liste.
    
* `_deleteTask` : Supprime une tâche et rafraîchit la liste.
    
* `FutureBuilder` : Reconstruit automatiquement l'UI lorsque le Future est terminé.
    
* `ListView.builder` : Affiche toutes les tâches de manière dynamique.
    

Cela vous donne une application CRUD simple mais complète utilisant Isar.

## Au-delà du CRUD : Fonctionnalités avancées d'Isar

Une fois que vous êtes à l'aise avec le CRUD, Isar propose des outils avancés pour optimiser et étendre votre application :

1. **Requêtes réactives** :  
    Au lieu d'utiliser `FutureBuilder`, vous pouvez écouter les changements directement.
    
    ```dart
    final stream = isar.tasks.where().watch(fireImmediately: true);
    ```
    
2. **Index** :  
    Améliorez les performances des requêtes en indexant les champs.
    
    ```dart
    @Collection()
    class Task {
      Id id = Isar.autoIncrement;
    
      @Index()
      late String name;
    }
    ```
    
3. **Relations** :  
    Liez une collection à une autre (par exemple, `Project` avec plusieurs `Tasks`).
    
4. **Requêtes personnalisées** :  
    Effectuez des filtrages, des tris et des paginations complexes.
    
5. **Migrations** :  
    Faites évoluer votre schéma en toute sécurité à mesure que l'application grandit.
    
6. **Opérations par lots (Batch)** :  
    Insérez ou mettez à jour plusieurs enregistrements en une seule transaction.
    

## Conclusion

Nous avons construit une application de tâches Flutter simple avec Isar qui prend en charge la création, la lecture, la mise à jour et la suppression de tâches. En chemin, nous avons appris comment :

1. Ajouter les dépendances Isar.
    
2. Définir un modèle avec des annotations.
    
3. Générer le code du schéma.
    
4. Implémenter les opérations CRUD dans un repository.
    
5. Connecter Isar à l'UI Flutter.
    

Grâce à ses performances, son API conviviale pour les développeurs et ses fonctionnalités avancées, Isar est un excellent choix pour la persistance locale dans les applications Flutter.

Pour en savoir plus, consultez la documentation officielle :

1. [Isar sur pub.dev](https://pub.dev/packages/isar)
    
2. [Documentation Isar](https://isar.dev/)