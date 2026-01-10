---
title: Comment utiliser l'architecture Stacked pour créer une application Todo Flutter
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2022-07-18T22:03:02.000Z'
originalURL: https://freecodecamp.org/news/flutter-stacked-architecture-todo-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-2.png
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser l'architecture Stacked pour créer une application Todo
  Flutter
seo_desc: "Flutter is a UI toolkit for building cross-platform applications. You can\
  \ build Flutter apps using various state management techniques like the Stacked\
  \ architecture. \nThis article will explain what Stacked architecture is and will\
  \ guide you through c..."
---

Flutter est un kit d'interface utilisateur pour créer des applications multiplateformes. Vous pouvez créer des applications Flutter en utilisant diverses techniques de gestion d'état comme l'architecture [Stacked](https://pub.dev/packages/stacked). 

Cet article expliquera ce qu'est l'architecture Stacked et vous guidera à travers la création d'une simple application Todo en Flutter avec Stacked.

## Table des matières

* [Introduction à l'état de l'application et aux widgets Flutter](#heading-introduction-a-letat-de-lapplication-et-aux-widgets-flutter)
* [Pourquoi avez-vous besoin d'architectures de gestion d'état dans Flutter](#heading-pourquoi-avez-vous-besoin-darchitectures-de-gestion-detat-dans-flutter) ?
* [Qu'est-ce que l'architecture Stacked](#heading-quest-ce-que-larchitecture-stacked) ?
* [À propos de l'application Todo que nous allons créer](#heading-a-propos-de-lapplication-todo-que-nous-allons-creer)
* [Comment configurer Flutter et le service Todos](#heading-comment-configurer-flutter-et-le-service-todos)
* [Comment construire l'interface utilisateur de l'application Todo](#heading-comment-construire-linterface-utilisateur-de-lapplication-todo)
* [Note sur d'autres fonctionnalités de Stacked](#heading-note-sur-dautres-fonctionnalites-de-stacked)
* [Résumé](#heading-resume)

## Introduction à l'état de l'application et aux widgets Flutter

L'état fait référence à toute donnée que vous utilisez pour rendre votre interface utilisateur. Il peut s'agir de données générées par l'utilisateur ou provenant de vos serveurs ou backend.

Dans Flutter, l'interface utilisateur (UI) de l'application est une fonction de l'état. En d'autres termes, votre interface utilisateur à un moment donné est une représentation visuelle de l'état de votre application. 

Toujours dans Flutter, vous utilisez des widgets pour construire différentes parties de l'interface utilisateur de l'application. Un widget dans Flutter est une pièce ou une unité de l'interface utilisateur. Essentiellement, une application Flutter est un grand arbre de widgets. Des exemples de widgets sont [AppBar](https://api.flutter.dev/flutter/material/AppBar-class.html), [Container](https://api.flutter.dev/flutter/widgets/Container-class.html), [Icon](https://api.flutter.dev/flutter/widgets/Icon-class.html), [Image](https://api.flutter.dev/flutter/widgets/Image-class.html), [Text](https://api.flutter.dev/flutter/widgets/Text-class.html), et ainsi de suite. 

Flutter a deux types de widgets : [StatelessWidget](https://api.flutter.dev/flutter/widgets/StatelessWidget-class.html)s et [StatefulWidget](https://api.flutter.dev/flutter/widgets/StatefulWidget-class.html)s. Vous utilisez StatefulWidgets dans Flutter pour construire des widgets qui ont un état. 

Pour indiquer à Flutter qu'un état a changé dans votre application, vous appelez la fonction `[setState](https://api.flutter.dev/flutter/widgets/State/setState.html)` (disponible uniquement à l'intérieur des StatefulWidgets) et Flutter reconstruira l'arbre de widgets en fonction des données d'état qui ont changé.

Les widgets dans Flutter ne changent pas. Ils sont immuables. Flutter dessine les interfaces utilisateur efficacement à environ 60 images par seconde. 

À chaque image, Flutter vérifie l'arbre de widgets. Si des widgets ont changé, Flutter s'en débarrasse et les remplace par de nouveaux widgets qui ont l'état modifié.

## Pourquoi avez-vous besoin d'architectures de gestion d'état dans Flutter ?

`setState` est bien. C'est une manière optimale de gérer l'interface utilisateur et l'état car elle encourage un style de programmation [déclaratif](https://www.freecodecamp.org/news/imperative-vs-declarative-programming-difference/) (qui est la meilleure façon de coder les interfaces utilisateur).

Mais ensuite, à mesure que votre base de code Flutter grandit, vous réaliserez que vous appelerez toujours `setState`. Votre application Flutter aura tant de widgets qui dépendent de données d'état volumineuses et changeantes. Cela encombre votre code.

L'utilisation d'architectures de gestion d'état à travers les frameworks et les bibliothèques aide à la [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns), au code propre et à la scalabilité. La gestion d'état est également utile lorsque plusieurs développeurs contribuent à la même base de code. Les architectures aident également à la testabilité du code.

Ainsi, pour construire des applications robustes, vous devriez utiliser la gestion d'état là où vous en avez besoin. Par défaut, `setState` est votre option de prédilection pour la gestion d'état. Mais à mesure que vous commencez à adopter des architectures, vous utiliserez d'autres options de [gestion d'état disponibles dans Flutter](https://docs.flutter.dev/development/data-and-backend/state-mgmt/options).

Dans Flutter, chaque widget a une méthode `build` qui retourne son arbre de widgets. La méthode `build` prend un `BuildContext` avec lequel elle peut accéder à des données importantes sur l'application ou effectuer des tâches comme la navigation ou l'affichage de dialogues. 

[`InheritedWidget`](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html) est une approche intégrée pour accéder à l'état d'un widget plus haut dans l'arbre de widgets. Il accède à l'état de ce widget supérieur avec l'aide du BuildContext.

`[ChangeNotifier](https://api.flutter.dev/flutter/foundation/ChangeNotifier-class.html)` est une classe Flutter qui fait ce que son nom indique. Elle notifie les auditeurs des changements dans ses valeurs. Vous pouvez étendre cette classe et appeler sa méthode `[notifyListeners();](https://api.flutter.dev/flutter/foundation/ChangeNotifier/notifyListeners.html)` que vous pouvez à votre tour utiliser pour mettre à jour l'interface utilisateur là où c'est nécessaire. Les options populaires de gestion d'état dans Flutter utilisent `ChangeNotifier`. Par exemple, [Provider](https://docs.flutter.dev/development/data-and-backend/state-mgmt/simple).

Certaines architectures de gestion d'état trouvent un moyen de naviguer ou d'afficher des dialogues sans le BuildContext dans la méthode build. Ainsi, elles peuvent effectuer ces parties cruciales de l'application dans des fichiers ne contenant pas de widgets. Et si elles doivent mettre à jour l'interface utilisateur, elles utilisent `notifyListeners()`. Tel est le cas avec l'architecture Stacked.

## Qu'est-ce que l'architecture Stacked ?

Stacked est une gestion d'état moderne pour Flutter avec une [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns) de premier ordre et une [injection de dépendances](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/). 

La séparation des préoccupations implique de séparer tout le code de l'interface utilisateur du code logique. Une telle séparation est importante pour la maintenabilité de votre projet Flutter.

Par exemple, avec une séparation des préoccupations correctement configurée dans votre base de code, si des mises à jour sont apportées à votre API backend, vous n'auriez besoin de mettre à jour que les fichiers qui traitent de la logique de l'API. Vous n'aurez pas nécessairement besoin de mettre à jour le code de l'interface utilisateur. Cela minimise les bugs qui pourraient survenir lors du codage.

L'injection de dépendances (ou inversion de contrôle) est une technique de programmation populaire. Pour un bloc de code donné, l'injection de dépendances est le fait que ce bloc ne configure pas lui-même les éléments dont il a besoin pour fonctionner (dépendances).

Avec l'injection de dépendances, vous fournissez à une classe les services (dépendances) dont elle a besoin pour fonctionner correctement. À leur tour, ces services abstraient et gèrent la logique métier de l'application.

Par exemple, un service météo peut s'occuper de récupérer les détails météo et un widget d'affichage météo utilisera ce service pour afficher les données. Ce widget ne sait pas comment configurer le service. Tout ce qu'il sait, c'est qu'il recevra les données météo dont il a besoin pour l'affichage de la classe de service météo d'une manière ou d'une autre.

Stacked met en œuvre la séparation des préoccupations et l'injection de dépendances en construisant le code Flutter autour de 3 entités : **Views**, **ViewModels** et **Services**. 

Les Views gèrent uniquement le code de l'interface utilisateur et sont liées aux ViewModels. Les ViewModels accompagnent les vues et gèrent la logique de l'interface utilisateur. Les ViewModels utilisent des services. Les vues ne doivent jamais accéder directement aux services.  

Stacked a été fondé par [Dane Mackier](https://www.linkedin.com/in/dane-mackier-a0b99670) et est maintenant maintenu par la communauté. [Dane Mackier est un GDE (Google Developer Expert) pour Dart et Flutter](https://developers.google.com/community/experts/directory/profile/profile-dane-mackier). Il a utilisé d'autres architectures populaires de gestion d'état et a combiné leurs avantages pour construire Stacked.

Notez que Stacked utilise ChangeNotifier.

## À propos de l'application Todo que nous allons créer

Pour garder les choses simples, nous allons créer une application Todo en mode sombre à un seul écran avec l'architecture Stacked. 

L'application affichera un message s'il n'y a pas encore de todos. Cependant, s'il y a des Todos, elle les affichera tous les uns après les autres. 

Chaque Todo aura un "cercle coachable" à sa gauche pour indiquer s'il a été complété ou non. À sa droite, un Todo aura un bouton (avec une icône de trait) pour supprimer le Todo. Le contenu textuel du Todo remplira le centre ou la majeure partie de l'écran. 

Nous aurons également un bouton d'action flottant (avec une icône plus) pour créer de nouveaux todos.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/sample.png)

En plus de ce qui précède, nous stockerons les Todos dans un stockage de navigateur ou de périphérique avec [Hive](https://pub.dev/packages/hive). Par conséquent, lors de la fermeture et de la réouverture de l'application Todo, tous les Todos précédemment créés seront restaurés.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/fcc_refresh.gif)
_Todos restaurés après le rechargement du navigateur_

Parce que c'est l'architecture Stacked, nous aurons un TodosService qui prendra en charge la gestion des Todos. Nous aurons également un TodosScreen (pour l'interface utilisateur). Le TodosScreen aura une Vue et un ViewModel. 

Cela dit, commençons à coder.

[Si vous ne voulez pas coder, le code final est ici.](https://github.com/obumnwabude/flutter_stacked_todo/tree/freecodecamp)

## Comment configurer Flutter et le service Todos

### 1. Installer Flutter

Tout d'abord, vous devrez avoir Flutter installé et fonctionnant correctement. Si c'est le cas, vous pouvez passer à la deuxième étape. Vous pouvez également passer à la deuxième étape si vous ne souhaitez pas suivre.

Si vous n'avez pas installé Flutter, installez-le en suivant [les étapes pour votre système d'exploitation ici](https://docs.flutter.dev/get-started/install). 

Exécutez la commande `flutter doctor -v` dans votre terminal. Si toutes les options listées ont une bonne coche ou une couleur verte, alors vous êtes prêt à continuer. Si l'un des résultats contient des erreurs, recherchez l'erreur en ligne et vous trouverez des solutions au problème.

### 2. Créer le projet Flutter

Exécutez la commande suivante pour créer un nouveau projet Flutter :

```bash
flutter create todo 
```

Cela crée un nouveau projet Flutter avec `todo` comme nom de l'application. Si vous voulez un nom d'application différent (autre que `todo`), utilisez-le à la place de `todo`.

### 3. Ajouter les packages

Nous devons ajouter le package Flutter `[stacked](https://pub.dev/packages/stacked)` au projet. Il nous fournira les classes nécessaires (comme ViewModels), étant donné que nous construisons avec l'architecture Stacked.

Nous devons également installer un autre package pour aider à l'injection de dépendances ou aux services. Pour garder les choses simples, nous utiliserons le package `[get_it](https://pub.dev/packages/get_it)` pour "obtenir" les services dans cette application Todo. 

Parce que nous voulons persister les todos à travers les fermetures de l'application avec Hive, nous devrons également ajouter les packages `[hive](https://pub.dev/packages/hive)` et `[hive_flutter](https://pub.dev/packages/hive_flutter)`.

Changez le répertoire de focus du terminal pour qu'il soit à l'intérieur du projet Flutter `todo` que vous venez de créer ci-dessus. Exécutez la commande suivante dans le même terminal :

```bash
cd todo
```

Si vous avez utilisé un nom d'application différent, utilisez-le avec la commande `cd` au lieu de `todo`.

Exécutez la commande suivante dans votre terminal pour ajouter `get_it`, `hive`, `hive_flutter` et `stacked` dans le projet Flutter. 

```bash
flutter pub add get_it hive hive_flutter stacked
```

### 4. Créer un modèle Todo

Nous construisons une application Todo, ce qui signifie que nous interagirons avec des Todos. Un Todo, dans le contexte du code, est une entité que nous manipulerons.

Pour garder les choses simples, un Todo sera une classe Dart avec seulement trois propriétés : 

1. `id` : Chaîne d'identification unique pour chaque Todo.
2. `completed` : Valeur booléenne pour indiquer l'état du Todo
3. `content` : Le contenu textuel réel du Todo.

Ouvrez le projet Flutter dans votre éditeur préféré. 

Créez un nouveau dossier avec le nom `models` à l'intérieur du dossier `lib`. À l'intérieur de ce dossier `models` nouvellement créé, créez un nouveau fichier avec le nom `todo.dart`.

Collez ce qui suit dans le fichier nouvellement créé `lib/models/todo.dart` :

```dart
class Todo {
  final String id;
  bool completed;
  String content;

  Todo({required this.id, this.completed = false, this.content = ''});
}

```

Remarquez que la propriété `id` est requise pour chaque todo. Cependant, par défaut, un Todo n'est **pas** complété et a un contenu vide.

### 5. Créer le TodoAdapter (pour Hive)

Hive fonctionne bien avec les types primitifs (comme les booléens, les entiers, les chaînes, etc.). Mais pour récupérer et sauvegarder correctement les types personnalisés (comme notre modèle Todo) depuis et vers le stockage du navigateur ou de l'appareil, Hive a besoin que nous créions des adaptateurs pour nos types personnalisés.

Créez un fichier nommé `todo.adapter.dart` dans le dossier `lib/models`. Le fichier `todo.adapter.dart` doit accompagner le fichier `todo.dart`. 

Collez ce qui suit dans le fichier nouvellement créé `lib/models/todo.adapter.dart` :

```dart
import 'package:hive_flutter/hive_flutter.dart';

import 'todo.dart';

class TodoAdapter extends TypeAdapter<Todo> {
  @override
  final int typeId = 1;

  @override
  Todo read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return Todo(
      id: fields[0] as String,
      completed: fields[1] as bool,
      content: fields[2] as String,
    );
  }

  @override
  void write(BinaryWriter writer, Todo obj) {
    writer
      ..writeByte(3)
      ..writeByte(0)
      ..write(obj.id)
      ..writeByte(1)
      ..write(obj.completed)
      ..writeByte(2)
      ..write(obj.content);
  }
}

```

Le code ci-dessus fournit essentiellement des méthodes de lecture et d'écriture pour que Hive puisse récupérer et stocker un Todo. 

### 6. Créer le TodosService

Créez un nouveau dossier avec le nom `services` à l'intérieur du dossier `lib`. À l'intérieur de ce dossier `services` nouvellement créé, créez un nouveau fichier avec le nom `todos.service.dart`.

Collez ce qui suit dans le fichier nouvellement créé `lib/services/todos.services.dart` :

```dart
import 'dart:math';

import 'package:hive_flutter/hive_flutter.dart';
import 'package:stacked/stacked.dart';

import '../models/todo.dart';

class TodosService with ReactiveServiceMixin {
  final _todos = ReactiveValue<List<Todo>>(
    Hive.box('todos').get('todos', defaultValue: []).cast<Todo>(),
  );
  final _random = Random();

  List<Todo> get todos => _todos.value;

  TodosService() {
    listenToReactiveValues([_todos]);
  }

  String _randomId() {
    return String.fromCharCodes(
      List.generate(10, (_) => _random.nextInt(33) + 80),
    );
  }

  void _saveToHive() => Hive.box('todos').put('todos', _todos.value);

  void newTodo() {
    _todos.value.insert(0, Todo(id: _randomId()));
    _saveToHive();
    notifyListeners();
  }

  bool removeTodo(String id) {
    final index = _todos.value.indexWhere((todo) => todo.id == id);
    if (index != -1) {
      _todos.value.removeAt(index);
      _saveToHive();
      notifyListeners();
      return true;
    } else {
      return false;
    }
  }

  bool toggleStatus(String id) {
    final index = _todos.value.indexWhere((todo) => todo.id == id);
    if (index != -1) {
      _todos.value[index].completed = !_todos.value[index].completed;
      _saveToHive();
      notifyListeners();
      return true;
    } else {
      return false;
    }
  }

  bool updateTodoContent(String id, String text) {
    final index = _todos.value.indexWhere((todo) => todo.id == id);
    if (index != -1) {
      _todos.value[index].content = text;
      _saveToHive();
      return true;
    } else {
      return false;
    }
  }
}

```

#### Comprendre les services réactifs dans Stacked

La déclaration de la classe TodosService est accompagnée d'un [ReactiveServiceMixin](https://pub.dev/documentation/stacked/latest/stacked/ReactiveServiceMixin-mixin.html). C'est là que les fonctionnalités de Stacked commencent à apparaître.

Avec Stacked, les services par défaut ne sont pas réactifs. Cependant, vous devez rendre un service réactif si d'autres parties du code du projet (d'autres services ou ViewModels) doivent "réagir" aux changements dans les valeurs du service. 

Si un service est réactif, c'est-à-dire qu'il a le ReactiveServiceMixin, cela signifie que ce service aura au moins une [ReactiveValue](https://pub.dev/documentation/stacked/latest/stacked/ReactiveValue-class.html) parmi ses propriétés. Cela signifie également que le service doit appeler `[listenToReactiveValues](https://pub.dev/documentation/stacked/latest/stacked/ReactiveServiceMixin/listenToReactiveValues.html)` avec une liste des valeurs réactives dans ce service.

L'idée derrière la réactivité est que lorsque les valeurs réactives changent (soit par interaction utilisateur ou par votre serveur backend), le service peut mettre à jour les auditeurs de cette valeur qu'il y a des changements. À leur tour, ces auditeurs peuvent reconstruire les interfaces utilisateur comme si `setState` avait été appelé depuis le widget.

#### À propos de la classe TodosService

Dans notre cas, la classe TodosService n'a qu'un seul champ réactif privé `_todos`. `_todos` conserve une `ReactiveValue` de TodoList. Ce champ réactif privé `_todos` est également donné à la liste des valeurs réactives à écouter dans le constructeur (`listenToReactiveValues`).

C'est là que Hive intervient. Avec Hive, vous stockez les données sous forme de paires clé-valeur à l'intérieur de boîtes. Pour notre application, nous utilisons une boîte 'todos'. À l'intérieur de cette boîte, nous utilisons la clé 'todos' pour récupérer les `todos` stockés. 

```dart
 Hive.box('todos').get('todos', defaultValue: []).cast<Todo>(),
```

La valeur par défaut de la liste vide (`[]`) est nécessaire. Pour la première fois, l'application Todo est exécutée sur un appareil qui n'avait jamais stocké de `todos` auparavant, donc la liste vide sera retournée à la place.

Le [casting](https://en.wikipedia.org/wiki/Type_conversion) de la valeur récupérée en tant qu'objet Todo est également important (`.cast<Todo>()`). Si vous omettez cette étape, Flutter lancera des erreurs.

La classe TodosService fournit un getter `todos` pour accéder à la valeur de la liste Todo réactive privée (`_todos.value`).

```dart
List<Todo> get todos => _todos.value;
```

La classe TodosService fournit également des méthodes pour manipuler les Todos et leurs propriétés (`removeTodo`, `toggleStatus` et `updateTodoContent`). Chacune de ces méthodes prend l'`id` du Todo et utilise l'`id` pour effectuer l'action appropriée.

Remarquez que toutes ces méthodes appellent la méthode privée `_saveToHive()`. La raison est que chaque fois que les `todos` sont mis à jour, les mises à jour sont sauvegardées dans notre stockage local avec Hive. Ainsi, si l'application est fermée et rouverte, le dernier état des `todos` sera rechargé.

Remarquez également que ces méthodes appellent `notifyListeners()`. Cela fait partie de l'idée derrière le fait d'avoir uniquement un getter pour `todos` (et pas de setter). Ainsi, chaque fois qu'il y a des mises à jour (à partir de ces méthodes), nous pouvons appeler `notifyListeners()` (si nécessaire) et effectuer la logique appropriée (comme `_saveToHive`).

`notifyListeners()` est l'équivalent de `setState()` mais cette fois-ci, pas à l'intérieur d'un StatefulWidget. Il indique aux auditeurs possibles (comme le futur TodosScreenViewModel) que le getter `todos` a changé. À leur tour, le ViewModel reconstruira l'interface utilisateur de sa vue et rendra le nouvel état des `todos`.

Il est important de souligner que `updateTodoContent` n'appelle pas `notifyListeners()`. Nous indiquerons la raison lorsque nous construirons l'interface utilisateur de la TodosScreenView.

Remarquez la méthode privée `_randomId()` qui retourne une chaîne aléatoire de 10 caractères. La méthode `newTodo()` utilise `_randomId()` pour définir l'`id` d'un nouveau Todo et insère ce nouveau Todo au début de la TodoList.

Si vous voulez que les nouveaux Todos soient ajoutés à la fin de la liste, utilisez `_todos.value.add(Todo(id: _randomId()));` au lieu de `_todos.value.insert(0, Todo(id: _randomId()));` dans la méthode `newTodo()`.

L'ensemble du modèle ci-dessus d'utilisation d'un service introduit une structure de code et rend le code plus facile à lire (par rapport à si tout était dans un widget).

Ce modèle de service devient très utile si nous sauvegardions les `todos` dans une API externe et les récupérions au chargement de l'application. Mais cela dépasserait le cadre de la simple introduction de l'architecture Stacked.

### 6. Configurer le Service Locator

Créez un nouveau dossier avec le nom `app` à l'intérieur du dossier `lib`. À l'intérieur de ce dossier `app` nouvellement créé, créez un nouveau fichier avec le nom `locator.dart`.

Collez ce qui suit dans le fichier nouvellement créé `lib/app/locator.dart` :

```dart
import 'package:get_it/get_it.dart';

import '../services/todos.service.dart';

final locator = GetIt.instance;

setupLocator() {
  locator.registerLazySingleton(() => TodosService());
}

```

Ici, par convention, nous avons nommé l'instance `GetIt` `locator`. Après tout, ce nom reflète ce qu'elle fait. Elle localise les services. D'autres développeurs pourraient vouloir utiliser `getIt` ou un autre nom descriptif pour ce localisateur de services. C'est acceptable.

Nous avons une fonction `setupLocator()` qui enregistre notre TodosService avec le localisateur. Si nous avions d'autres services, nous les enregistrerions ici de manière similaire. 

Nous devons appeler la fonction `setupLocator()` avant le lancement de l'ensemble de l'application Flutter. Ainsi, les services sont disponibles pour tous les widgets dont l'application Flutter aura besoin. 

Supprimez tout le contenu du fichier `lib/main.dart` et collez ce qui suit à la place :

```dart
import 'package:flutter/material.dart';
import 'package:hive_flutter/hive_flutter.dart';

import 'app/locator.dart';
import 'models/todo.adapter.dart';
import 'ui/views/todos_screen_view.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Hive.initFlutter();
  Hive.registerAdapter(TodoAdapter());
  await Hive.openBox('todos');
  
  setupLocator();
  
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const TodosScreenView(),
      theme: ThemeData.dark(),
      title: 'Flutter Stacked Todos',
    );
  }
}

```

`WidgetsFlutterBinding.ensureInitialized()` est la première instruction dans la même méthode `main`. 

En termes simples, nous utilisons cette instruction parce que Flutter nous demande de toujours l'inclure comme première chose dans la méthode `main` chaque fois que nous voulons faire d'autres choses (comme `Hive.initFlutter()` ou `setupLocator()`) avant de lancer l'application Flutter avec `runApp()`.

Remarquez que nous initialisons Hive, enregistrons le TodoAdapter et ouvrons la boîte 'todos' dans la méthode `main`. C'est la dernière partie de la configuration de Hive.

Remarquez également que nous appelons maintenant la fonction `setupLocator()` à l'intérieur de la méthode `main` et avant l'appel final à `runApp` pour lancer l'application Flutter.

Nous avons utilisé un thème sombre dans notre MaterialApp en définissant la propriété `theme` sur `ThemeData.dark()`. Ce thème sombre est juste pour le style - vous pouvez le supprimer si vous préférez le thème clair par défaut. Vous pouvez également personnaliser le thème de l'application comme vous le souhaitez.

Notre fichier `lib/main.dart` contient actuellement des erreurs. L'erreur est que le widget `TodosScreenView` n'existe pas et nous l'avons défini comme propriété `home` de notre MaterialApp. 

Si vous utilisez un [IDE compatible avec Flutter](https://docs.flutter.dev/get-started/editor), vous remarquerez que les erreurs ci-dessus ont été indiquées.

Pas de soucis, nous allons créer ces fichiers maintenant.

## Comment construire l'interface utilisateur de l'application Todo

### Les différents types de ViewModels

Dans Stacked, pensez d'abord aux ViewModels avant leurs Views. Cela vous aidera à rassembler les dépendances dont la vue correspondante a besoin avant de construire réellement la vue.

Stacked propose différents types de ViewModel. Dans Stacked, vous avez BaseViewModels, ReactiveViewModels, FutureViewModels, StreamViewModels et MultipleFutureViewModels. Utilisez chacun en fonction de votre besoin actuel. 

Utilisez ReactiveViewModels si votre Vue ou son ViewModel devra utiliser des valeurs réactives provenant de services réactifs. 

Nous utiliserons le type de ViewModel réactif pour notre TodosScreenViewModel. Nous utilisons un ReactiveViewModel car nous aurons besoin du getter réactif `todos` dans le TodosScreen.

### 1. Créer le TodosScreenViewModel

Créez un nouveau dossier avec le nom `ui` à l'intérieur du dossier `lib`. À l'intérieur de ce dossier `ui` nouvellement créé, créez un autre dossier nommé `todos_screen`. Ensuite, à l'intérieur du nouveau dossier `todos_screen`, créez un nouveau fichier avec le nom `todos_screen_viewmodel.dart`.

Collez ce qui suit dans le fichier nouvellement créé `lib/ui/todos_screen/todos_screen_viewmodel.dart` :

```dart
import 'package:flutter/material.dart';
import 'package:stacked/stacked.dart';

import '../../app/locator.dart';
import '../../models/todo.dart';
import '../../services/todos.service.dart';

class TodosScreenViewModel extends ReactiveViewModel {
  final _firstTodoFocusNode = FocusNode();
  final _todosService = locator<TodosService>();
  late final toggleStatus = _todosService.toggleStatus;
  late final removeTodo = _todosService.removeTodo;
  late final updateTodoContent = _todosService.updateTodoContent;

  List<Todo> get todos => _todosService.todos;

  void newTodo() {
    _todosService.newTodo();
    _firstTodoFocusNode.requestFocus();
  }

  FocusNode? getFocusNode(String id) {
    final index = todos.indexWhere((todo) => todo.id == id);
    return index == 0 ? _firstTodoFocusNode : null;
  }

  @override
  List<ReactiveServiceMixin> get reactiveServices => [_todosService];
}

```

Remarquez comment nous avons accès au `_todosService` avec l'aide de `locator`. Nous remplaçons le getter `reactiveServices` sur ReactiveViewModels et fournissons le `_todosService` à cette liste. 

Ainsi, chaque fois que `notifyListeners()` est appelé à l'intérieur de TodosService, ce TodosScreenViewModel sera notifié et il reconstruira l'interface utilisateur si nécessaire.

À partir de TodosScreenViewModel, nous exposons les méthodes `removeTodo`, `toggleStatus` et `updateTodoContent` du service à la TodosScreenView (qui viendra plus tard).

Vous pourriez vous demander pourquoi nous devons faire cela. Pourquoi ne pas simplement exposer le service lui-même ou plutôt accéder au service depuis la Vue ou le widget lui-même ?

Le point ici est les règles architecturales et la séparation des préoccupations. Rappelez-vous que l'architecture Stacked stipule que les Vues ne doivent jamais accéder aux services. 

De plus, nous faisons cela parce que nous gardons les choses simples. Si l'application devient plus grande que cela et que nous commençons à ajouter des fonctionnalités aux vues, vous réaliserez que le TodosScreenViewModel devra effectuer d'autres logiques avant ou après avoir fait des appels aux méthodes du service. Dans ce cas, nous ne ferons pas une telle exposition directe des méthodes.

Cela est évident dans la méthode `newTodo()` de TodosScreenViewModel. Elle appelle la fonction `_todosService.newTodo()` pour créer un nouveau Todo vide. Ensuite, elle demande le focus sur le premier nœud ou le nœud nouvellement créé du Todo (`_firstTodoFocusNode.requestFocus()`).

Ainsi, le curseur se concentrera automatiquement sur le champ de saisie de texte du Todo vide nouvellement créé après sa création. Vous verrez cela en action lorsque nous créerons la TodosScreenView.

La méthode `getFocusNode` retourne ce `_firstTodoFocusNode` si le Todo qui l'appelle est le premier Todo. Cet appel sera fait à partir de l'interface utilisateur dans la TodosScreenView (à venir plus tard).

#### Note sur le mot-clé `late`

Le mot-clé `late` attaché aux méthodes de service directement exposées est nécessaire. 

Dart est beau. `late` est une fonctionnalité de Dart qui indique que nous sommes sûrs que ces méthodes seront assignées _plus tard_ (à partir du service) après que le ViewModel a été instancié.

Si vous supprimez le mot-clé `late`, Dart se plaindra avec "The instance member '_todosService' can't be accessed in an initializer." Cette plainte est valide.

La plainte survient parce que, lorsque le TodosScreenViewModel a été instancié, Dart n'est pas sûr que, au moment où il doit instancier ces méthodes exposées (qui avaient `late` devant elles), le '_todosService' a terminé son initialisation pour être disponible pour les méthodes.

Généralement, les membres d'instance ne peuvent pas s'initialiser mutuellement. L'exception est soit d'utiliser le mot-clé `late` (comme nous l'avons fait) soit de faire une telle initialisation dans le constructeur. 

En coulisses, le mot-clé `late` retarde l'initialisation des membres d'instance dépendants (dans ce cas, les méthodes directement exposées) jusqu'à ce que le membre d'instance indépendant (dans ce cas, _todosService) ait terminé son initialisation.

Nous n'avons pas fait ces initialisations dans le constructeur car cela rendrait le code plus long. Et de plus, cela a le même effet que d'utiliser `late`.

### 2. Créer le TodosScreenView

Créez un nouveau fichier avec le nom `todos_screen_view.dart` à l'intérieur du dossier `lib/ui/todos_screen`. En d'autres termes, le fichier `todos_screen_view.dart` doit accompagner son fichier ViewModel : `todos_screen_viewmodel.dart`.

Collez ce qui suit dans le fichier nouvellement créé `lib/ui/todos_screen/todos_screen_view.dart` :

```dart
import 'package:flutter/material.dart';
import 'package:stacked/stacked.dart';

import 'todos_screen_viewmodel.dart';

class TodosScreenView extends StatelessWidget {
  const TodosScreenView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ViewModelBuilder<TodosScreenViewModel>.reactive(
      viewModelBuilder: () => TodosScreenViewModel(),
      builder: (context, model, _) => Scaffold(
        appBar: AppBar(title: const Text('Flutter Stacked Todos')),
        body: ListView(
          padding: const EdgeInsets.symmetric(vertical: 16),
          children: [
            if (model.todos.isEmpty)
              Opacity(
                opacity: 0.5,
                child: Column(
                  children: const [
                    SizedBox(height: 64),
                    Icon(Icons.emoji_food_beverage_outlined, size: 48),
                    SizedBox(height: 16),
                    Text('Aucun todo pour le moment. Cliquez sur + pour en ajouter un nouveau.'),
                  ],
                ),
              ),
            ...model.todos.map((todo) {
              return ListTile(
                leading: IconButton(
                  icon: Icon(
                    todo.completed ? Icons.task_alt : Icons.circle_outlined,
                  ),
                  onPressed: () => model.toggleStatus(todo.id),
                ),
                title: TextField(
                  controller: TextEditingController(text: todo.content),
                  decoration: null,
                  focusNode: model.getFocusNode(todo.id),
                  maxLines: null,
                  onChanged: (text) => model.updateTodoContent(todo.id, text),
                  style: TextStyle(
                    fontSize: 20,
                    decoration:
                        todo.completed ? TextDecoration.lineThrough : null,
                  ),
                ),
                trailing: IconButton(
                  icon: const Icon(Icons.horizontal_rule),
                  onPressed: () => model.removeTodo(todo.id),
                ),
              );
            }),
          ],
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: model.newTodo,
          child: const Icon(Icons.add),
        ),
      ),
    );
  }
}

```

#### À propos du TodosScreenView

La première ligne après la déclaration de la méthode `build` est une instruction de retour. Cette instruction retourne un widget `ViewModelBuilder` pour le TodosScreenViewModel. 

C'est un autre aspect de l'architecture Stacked. Cela explique ce que nous entendons par les Vues étant attachées aux ViewModels. En essence, nous utilisons des ViewModelBuilders pour rendre une Vue.

Ainsi, la Vue a accès aux propriétés et méthodes publiques de son ViewModel. De plus, l'appel à `notifyListeners()` à l'intérieur du ViewModel met automatiquement à jour l'interface utilisateur de la Vue. De plus, la plupart (sinon toutes) des logiques d'interface utilisateur qui ne sont pas déclaratives doivent être déplacées vers le ViewModel.   

Cela explique pourquoi nous avons déplacé la logique du FocusNode du premier Todo vers le TodosScreenViewModel.

Le `body` de la vue TodosScreenView's Scaffold est une `ListView` pour tous les Todos obtenus à partir de `model.todos`.

Cependant, le premier membre de la ListView est un widget Opacity conditionnel avec une opacité de 0,5. Son enfant est une colonne pour l'état vide avec un espacement, une icône de tasse de thé et un texte pour les enfants.

Nous avons utilisé `ListTile` pour afficher chaque Todo. C'est un widget de commodité qui prend des widgets `leading`, `title` et `trailing` pour les parties gauche, centrale et droite de l'écran.

**Note sur le sens droite-gauche** : ListTile est un bon widget, et Flutter est un bon framework. Ils sont tous deux internationalisés. Si cette application était exécutée sur un appareil naturellement configuré avec une locale de droite à gauche (en arabe par exemple), l'application serait mise en miroir. Ainsi, les widgets leading, title et trailing des ListTiles seraient les parties droite, centrale et gauche de l'écran au lieu de cela. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/rtl-sample.png)

Le widget `leading` sur le ListTile est un IconButton dont l'icône est soit un cercle vide ou coché selon que le Todo est complété ou non. Le callback `onPressed` sur l'IconButton bascule le statut du Todo.

Le widget `title` (centre) sur le ListTile est un TextField sans décoration. Pas de décoration ici signifie qu'il n'a pas de fonds, de bordures ou de soulignements. Le but est de donner à l'utilisateur le sentiment qu'il peut simplement lire le contenu de son Todo, tout en ayant la possibilité de modifier le contenu au même endroit. 

Le `[TextEditingController](https://api.flutter.dev/flutter/widgets/TextEditingController-class.html)` donné au TextField est utilisé pour définir le contenu textuel sur le champ à partir du contenu du Todo. La définition de `maxLines` à null sur le TextField indique à Flutter que le texte dans le TextField peut s'étendre sur plusieurs lignes. 

Le callback `onChanged` met à jour le contenu textuel du Todo attaché. Ce callback est appelé pour chaque frappe ou édition de texte. Nous faisons cela pour garder tous les Todos toujours synchronisés avec l'interface utilisateur.

Nous n'avons pas appelé `notifyListeners()` dans ce callback (`updateTodoContent`) dans le TodosService pour empêcher le curseur de sauter (étant donné que nous faisons l'appel pour chaque frappe). 

Si `notifyListeners()` était appelé dans ce callback, l'interface utilisateur serait reconstruite chaque fois, et le curseur continuerait à sauter au début du TextField après chaque frappe.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/todo_jumping_cursor-1.gif)

### 3. Exécuter l'application Todo

Si vous utilisez un IDE compatible avec Flutter, vous devriez pouvoir exécuter l'application ci-dessus sur un appareil préconfiguré. 

Si vous ne l'êtes pas, pas de problème - exécutez la commande suivante dans le même terminal. Ou plutôt, assurez-vous d'être dans le même dossier de projet dans le terminal, puis exécutez la commande :

```bash
flutter run
```

Il devrait exécuter l'application Flutter sur un appareil disponible ou vous demander de choisir un appareil et ensuite exécuter l'application sur celui-ci. 

Vous devriez pouvoir créer des Todos, les marquer comme complets et les supprimer.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/todo_usage.gif)

Si vous êtes arrivé jusqu'ici, félicitations pour avoir construit une application Todo avec l'architecture Stacked !

Pour un mini-récapitulatif, les fichiers à l'intérieur de votre dossier `lib` devraient maintenant être :

* `app/locator.dart`
* `models/todo.adapter.dart`
* `models/todo.dart`
* `services/todos.service.dart`
* `ui/todos_screen/todos_screen_view.dart`
* `ui/todos_screen/todos_screen_viewmodel.dart`
* `main.dart`

[Vous pouvez obtenir le code final sur GitHub ici](https://github.com/obumnwabude/flutter_stacked_todo/tree/freecodecamp).

## Note sur d'autres fonctionnalités de Stacked

Il y a plus à utiliser l'architecture Stacked. L'application Todo ci-dessus était à un seul écran et n'avait pas besoin de navigation.

Vous devrez configurer la Navigation ou le Routing dans la plupart, sinon toutes les applications que vous construirez avec Flutter. La navigation est une nécessité une fois que vous avez plus d'un écran dans l'application Flutter.

Stacked vous permet de configurer une décoration `@StackedApp` sur une classe Dart vide. Cette décoration peut prendre des informations sur les routes et les dépendances comme dans l'extrait suivant :

```dart
@StackedApp(
  routes: [MaterialRoute(page: TodosScreenView, initial: true)],
  dependencies: [LazySingleton(classType: TodosService)],
)
class App {
  // Cette classe n'a pas d'autre but que d'héberger l'annotation qui
  // génère la fonctionnalité requise.
}

```

Vous devrez ensuite ajouter les packages `build_runner` et `stacked_generator` au projet Flutter. Ensuite, en développement, vous garderez la commande suivante en cours d'exécution :

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

Cette commande générera le contenu de la fonction `setupLocator()` pour vous. Et c'est le fichier généré (et la fonction) que vous ajouteriez à la méthode principale dans `lib/main.dart`.

De plus, l'architecture Stacked dispose également d'un package `[stacked_services](https://pub.dev/packages/stacked_services)`. Ce package aide à configurer des services cruciaux comme les feuilles de fond, les dialogues, la navigation et les barres de notification, sans le BuildContext, à l'intérieur des ViewModels. 

Toutes ces fonctionnalités introduisent de la commodité et vous offrent une meilleure expérience de développement tout en utilisant Stacked.

Mais ces fonctionnalités seraient excessives pour la simple application Todo que nous venons de construire. C'est pourquoi nous ne les avons pas incluses.

L'idée est de comprendre les principes fondamentaux derrière l'architecture Stacked et de pouvoir utiliser l'architecture dans vos projets Flutter **à grande échelle**.

L'accent est mis sur la grande échelle. En réalité, si vous construisez quelque chose de simple, vous n'aurez pas besoin d'utiliser _aucune_ architecture de gestion d'état. Même une application Todo _simple_. 

Mais dans cet article, j'ai visé à vous initier à l'architecture Stacked et j'avais besoin de quelque chose de simple (comme cette application Todo) pour expliquer les concepts.

Bien sûr, vous pouvez toujours utiliser Stacked pour construire des choses simples. C'est ce que nous venons de faire avec une application Todo. Mais comprenez que vous profiterez des avantages de Stacked lorsque vous commencerez à ajouter plus de fonctionnalités comme l'enregistrement des todos sur un serveur, l'authentification, le regroupement des todos en catégories, et plus encore dans l'application Todo.

## Résumé

Les architectures de gestion d'état sont de bonnes façons de structurer les projets Flutter. Elles sont optionnelles mais peuvent devenir une nécessité si vous construisez une application complexe ou si plus d'une personne contribue à la même base de code.

Ces architectures trouvent un moyen de mettre à jour l'interface utilisateur sans les appels par défaut à `setState()`. Stacked est une telle architecture. Elle utilise `notifyListeners()` pour mettre à jour l'interface utilisateur. 

Une caractéristique clé de Stacked est la réalisation de services cruciaux comme la navigation sans le BuildContext. Nous n'avons pas exploré cette fonctionnalité dans cette application Todo. Mais gardez-la à l'esprit lorsque vous irez plus loin avec l'utilisation de Stacked.

Vos applications Stacked doivent avoir des widgets à l'intérieur des fichiers View. Les Vues doivent être liées aux ViewModels et la logique de l'interface utilisateur doit avoir lieu ici. Les Services doivent être utilisés pour la logique métier de l'application et les API. Ils doivent être utilisés par d'autres services ou ViewModels.

Nous avons utilisé cette structure simple à 3 entités pour construire une application Todo fonctionnelle. Vous pouvez utiliser le même modèle pour construire des applications plus grandes et meilleures. Mieux encore, vous pouvez refactoriser des applications existantes pour suivre ce modèle et avoir un code plus propre.

Nous avons également utilisé Hive pour sauvegarder et récupérer les Todos après la fermeture et la réouverture de l'application Flutter. Hive est un package léger et peut servir des objectifs similaires dans vos applications.

[L'application mobile freeCodeCamp](https://play.google.com/store/apps/details?id=org.freecodecamp) est construite avec Flutter. Elle est open-source et a été construite en utilisant l'architecture Stacked. [Vous pouvez contribuer à l'application freeCodeCamp ici.](https://github.com/freeCodeCamp/mobile) 

Santé !