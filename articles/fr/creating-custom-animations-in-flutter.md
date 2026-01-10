---
title: Comment créer des animations personnalisées dans Flutter – Un guide étape par
  étape
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-07-26T17:44:21.000Z'
originalURL: https://freecodecamp.org/news/creating-custom-animations-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Flutter-Animation.png
tags:
- name: animations
  slug: animations
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment créer des animations personnalisées dans Flutter – Un guide étape
  par étape
seo_desc: "Animations play a crucial role in enhancing user experience and making\
  \ mobile apps more engaging. \nFlutter, Google's UI toolkit for building natively\
  \ compiled applications for mobile, web, and desktop, offers a powerful animation\
  \ system that allows d..."
---

Les animations jouent un rôle crucial dans l'amélioration de l'expérience utilisateur et rendent les applications mobiles plus engageantes. 

Flutter, la boîte à outils UI de Google pour construire des applications compilées nativement pour mobile, web et desktop, offre un système d'animation puissant qui permet aux développeurs de créer des animations personnalisées époustouflantes. 

Dans ce guide étape par étape, nous allons explorer comment construire de belles animations personnalisées dans Flutter pour faire passer l'UI de votre application au niveau supérieur.

## **Prérequis**

Avant de commencer, assurez-vous d'avoir Flutter installé sur votre système. Il est également utile d'avoir une compréhension de base des concepts fondamentaux du framework, tels que les widgets, la gestion d'état et la gestion des gestes.

Enfin, mais surtout, trouvez une petite étincelle d'intérêt pour apprendre l'animation ! :) Car une fois que vous verrez les widgets s'animer avec la magie de l'animation, cette étincelle va grandir en un incendie d'excitation.

Dans ce guide, nous allons voir comment implémenter l'animation dans deux types de tâches :

1. Liste Animée
2. Chargeur Animé

Nous allons créer une simple application Todo avec une Liste Animée et un Chargeur Animé. Alors, préparez-vous, et plongeons dans le monde de l'animation des listes et des chargeurs dans Flutter. 🐡🐔.

## Comment construire une Liste Animée dans Flutter

Tout d'abord, nous allons créer une simple liste Flutter avec animation. La Liste Animée est un widget Flutter qui permet aux développeurs de créer des listes dynamiques et animées avec des transitions fluides et visuellement attrayantes. Elle fait partie du framework d'animation Flutter et est une extension du widget ListView. 

La Liste Animée anime automatiquement les changements dans le contenu de la liste, tels que l'insertion ou la suppression d'éléments, offrant une expérience utilisateur engageante et interactive.

### Fonctionnalités Clés

#### Animations d'Insertion et de Suppression

Lorsque vous ajoutez ou supprimez des éléments de la liste, la Liste Animée anime ces changements avec des animations prédéfinies ou personnalisées, rendant les modifications de la liste visuellement fluides.

#### Contrôleurs d'Animation Intégrés

La Liste Animée est livrée avec des contrôleurs d'animation intégrés qui gèrent le timing et les courbes d'assouplissement des animations, simplifiant le processus de création de transitions fluides et fluides.

#### Animations Personnalisables

Bien que la Liste Animée fournisse des animations par défaut, les développeurs peuvent également personnaliser les animations pour les adapter au style visuel unique et aux exigences de l'application.

Maintenant, bien que la théorie soit essentielle, les exemples pratiques donnent vie aux concepts. Alors, plongeons dans un exemple pratique d'utilisation d'une Liste Animée dans Flutter.

### Configuration du Projet et Dépendances

Pour créer notre application Flutter, nous utiliserons Visual Studio Code comme environnement de développement. 

Si vous n'êtes pas familier avec la configuration d'un nouveau projet Flutter, ne vous inquiétez pas – vous pouvez vous référer à mes [blogs](https://www.freecodecamp.org/news/how-to-build-a-simple-login-app-with-flutter/) précédents pour des instructions étape par étape. Si vous êtes déjà à l'aise avec la création de projets Flutter, passez cette partie et poursuivez avec le développement de l'application.

Aucun besoin d'installer un plugin externe pour créer une Liste Animée.

## Comment Créer un Modèle de Tâche

Dans ce blog, nous nous concentrerons davantage sur l'animation afin de garder les fonctionnalités simples. Définissez une classe Task qui représente une seule tâche avec un titre et un statut.

J'ai créé un fichier appelé `todo_list.dart` dans le dossier `lib` qui contiendra la Liste Animée. Tout d'abord, j'ai créé une classe simple qui représente une Tâche avec un titre et un statut décrivant si elle est terminée ou non.

`todo_list.dart`

```
class Task {
  String title;
  bool isCompleted;
  Task(this.title, this.isCompleted);
}
```

## Comment Créer une Liste Simple avec Animation

Techniquement, notre objectif est de créer un conteneur défilant qui anime les éléments lorsqu'ils sont insérés ou supprimés. L'état de ce widget [AnimatedListState](https://api.flutter.dev/flutter/widgets/AnimatedListState-class.html) peut être utilisé pour insérer ou supprimer dynamiquement des éléments. 

Pour faire référence à l'AnimatedListState, fournissez soit une [GlobalKey](https://api.flutter.dev/flutter/widgets/GlobalKey-class.html) soit utilisez la méthode statique [of](https://api.flutter.dev/flutter/widgets/AnimatedList/of.html) à partir d'un rappel d'entrée d'élément.

Pour ce faire, créons un StatefulWidget pour créer une Liste Animée.

`todo_list.dart`

```dart
// todo_list.dart
import 'package:flutter/material.dart';
void main() {
  runApp(TodoListApp());
}
class Task {
  String title;
  bool isCompleted;
  Task(this.title, this.isCompleted);
}

class TodoListApp extends StatefulWidget {
  @override
  _TodoListAppState createState() => _TodoListAppState();
}

class _TodoListAppState extends State<TodoListApp> {
  List<Task> tasks = [];
  bool isLoading = false;

  final GlobalKey<AnimatedListState> _animatedListKey = GlobalKey();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Liste de Tâches')),
        body: AnimatedList(
          key: _animatedListKey,
          initialItemCount: tasks.length,
          itemBuilder: (context, index, animation) {
            return _buildTaskItem(tasks[index], animation, index);
          },
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: _addTask,
          child: const Icon(Icons.add),
        ),
        backgroundColor: Colors.white60,
      ),
    );
  }

  Widget _buildTaskItem(Task task, Animation<double> animation, int index) {
    return SizeTransition(
        sizeFactor: animation,
        child: Card(
          color: Colors.white,
          child: ListTile(
            title: Text(task.title),
            onLongPress: () => _removeTask(index),
          ),
        ));
  }

  void _addTask() async {
    Task newTask = Task('Nouvelle Tâche ${tasks.length + 1}', false);
    tasks.add(newTask);
    _animatedListKey.currentState!.insertItem(tasks.length - 1);
  }

  void _removeTask(int index) async {
    _animatedListKey.currentState!.removeItem(index,
        (context, animation) => _buildTaskItem(tasks[index], animation, index));
    tasks.removeAt(index);
  }
}
```

Ici, nous avons utilisé `AnimatedList` (un package Flutter par défaut). La classe `AnimatedList` dans Flutter est un widget puissant qui nous permet de créer des listes dynamiques et animées avec des transitions fluides. C'est une extension du widget ListView, fournissant un support d'animation intégré pour ajouter, supprimer et mettre à jour des éléments dans la liste. 

L'objectif principal de `AnimatedList` est d'améliorer l'expérience utilisateur en animant les changements dans le contenu de la liste, rendant l'application plus interactive et visuellement engageante.

`AnimatedList` possède plusieurs propriétés ou paramètres qui contrôlent divers aspects du comportement, de l'apparence et des animations du widget. Comprendre et utiliser correctement ces propriétés est crucial pour obtenir le comportement et les effets visuels souhaités dans une `AnimatedList`. 

Pour en savoir plus sur les propriétés et le comportement de `AnimatedList`, veuillez consulter la [documentation officielle](https://api.flutter.dev/flutter/widgets/AnimatedList-class.html).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/flutter_animated_list_demo.gif)
_Liste Animée Simple dans Flutter_

Dans ce tutoriel, nous allons nous concentrer sur la Liste Animée et le Chargeur Animé. Si vous n'êtes pas familier avec les bases de Flutter (comme les widgets, les états, etc.), je vous recommande de lire mon [tutoriel précédent](https://www.freecodecamp.org/news/learn-state-management-in-flutter/).

## Comment Construire le Chargeur Animé

Un chargeur est couramment utilisé pour fournir un retour visuel aux utilisateurs pendant l'attente du chargement des données, le traitement du contenu ou la réalisation de requêtes réseau. Les chargeurs aident à améliorer l'expérience utilisateur en donnant un sentiment d'activité et en empêchant l'application de sembler sans réponse pendant les périodes d'attente.

Il existe diverses façons d'implémenter des chargeurs dans Flutter, y compris l'utilisation de widgets intégrés, de packages tiers ou la création de chargeurs personnalisés. De plus, les "chargeurs animés" ajoutent une touche supplémentaire de dynamisme au processus de chargement en incorporant des animations fluides.

Ajoutons un chargeur animé dans notre TodoApp pendant la création et la suppression d'une tâche.

### Comment Ajouter le Package de Chargeur Flutter

Vous devrez installer le package avec la commande suivante :

```
flutter pub add loading_animation_widget
```

Ensuite, vous devriez voir l'écran suivant :

![Image](https://www.gogosoon.com/wp-content/uploads/2023/07/image-28-1024x208.png)
_Installation du package d'animation de chargement dans Flutter_

Maintenant, votre package devrait être prêt à l'emploi.

### Comment Implémenter `AnimatedLoader`

Le package `loading_animation_widget` offre diverses animations de chargeur que nous pouvons utiliser pour afficher des indicateurs de chargement dans notre application. En important le package, nous avons accès à ces animations de chargeur et pouvons les utiliser pour améliorer l'expérience utilisateur pendant les opérations de chargement ou toute autre tâche asynchrone.

Toutes les API d'animation de chargement suivent la même implémentation simple. Il y a une méthode statique pour chaque animation à l'intérieur de la classe LoadingAnimationWidget, qui retourne l'objet de cette animation. Les paramètres `size` et `color` sont requis, certaines animations nécessitent plus d'une couleur.

`loading_animation_widget` offre plusieurs chargeurs animés avec une animation personnalisée. Explorons quelques-uns de ceux-ci et intégrons-les dans notre Todo App.

J'ai maintenant créé un fichier appelé `animated_loader.dart`, qui contient le widget AnimatedLoader.

```dart
// animated_loader.dart
import 'package:flutter/material.dart';
import 'package:loading_animation_widget/loading_animation_widget.dart';

void main() {
  runApp(AnimatedLoader());
}
class AnimatedLoader extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyLoaderScreen(),
    );
  }
}
class MyLoaderScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: LoadingAnimationWidget.staggeredDotsWave(
            size: 75, color: Colors.deepPurple),
      ),
      backgroundColor: Colors.transparent,
    );
  }
}

```

Affichons ce chargeur animé dans notre liste animée pendant l'ajout ou la suppression d'une tâche.

`todo_list.dart`

```dart
import 'package:flutter/material.dart';
import 'package:flutter_animation/animated_loader.dart';
import 'package:loader_overlay/loader_overlay.dart';

void main() {
  runApp(TodoListApp());
}

class Task {
  String title;
  bool isCompleted;
  Task(this.title, this.isCompleted);
}

class TodoListApp extends StatefulWidget {
  @override
  _TodoListAppState createState() => _TodoListAppState();
}

class _TodoListAppState extends State<TodoListApp> {
  List<Task> tasks = [];
  bool isLoading = false;

  final GlobalKey<AnimatedListState> _animatedListKey = GlobalKey();

  Future<void> loadData() async {
    setState(() {
      isLoading = true;
    });
    await Future.delayed(const Duration(seconds: 2));
    setState(() {
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Liste de Tâches')),
        body: Stack(
          children: [
            AnimatedList(
              key: _animatedListKey,
              initialItemCount: tasks.length,
              itemBuilder: (context, index, animation) {
                return _buildTaskItem(tasks[index], animation, index);
              },
            ),
            if (isLoading)
              const Opacity(
                opacity: 0,
                child: ModalBarrier(dismissible: false, color: Colors.black),
              ),
            if (isLoading)
              Center(
                child: Center(child: AnimatedLoader()),
              ),
          ],
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: _addTask,
          child: const Icon(Icons.add),
        ),
        backgroundColor: Colors.white60,
      ),
    );
  }

  Widget _buildTaskItem(Task task, Animation<double> animation, int index) {
    return SizeTransition(
        sizeFactor: animation,
        child: Card(
          color: Colors.white,
          child: ListTile(
            title: Text(task.title),
            onLongPress: () => _removeTask(index),
          ),
        ));
  }

  void _addTask() async {
    Task newTask = Task('Nouvelle Tâche ${tasks.length + 1}', false);
    await loadData();
    tasks.add(newTask);
    _animatedListKey.currentState!.insertItem(tasks.length - 1);
  }

  void _removeTask(int index) async {
    await loadData();
    _animatedListKey.currentState!.removeItem(index,
        (context, animation) => _buildTaskItem(tasks[index], animation, index));
    tasks.removeAt(index);
  }
}

```

Pour explorer davantage le Chargeur, vous pouvez consulter la [documentation](https://pub.dev/packages/loading_animation_widget). Il propose plusieurs chargeurs avec des options de personnalisation.

![Image](https://www.gogosoon.com/wp-content/uploads/2023/07/flutter_animation_with_loader-2.gif)
_Liste Animée avec Chargeur Animé dans Flutter_

Hourra ! Nous pouvons voir que le Chargeur Animé et la Liste Animée se rendent très fluidement, et ils ont l'air encore mieux.

Si vous implémentez cela à partir de zéro, c'est génial et cela vous aidera vraiment à apprendre. Mais si vous préférez, vous pouvez également cloner le dépôt depuis [GitHub](https://github.com/5minslearn/flutter_animation). Dans tous les cas, je suis ravi de voir le Chargeur Animé et la Liste Animée en action de votre part.

Note : Dans le contexte de la création d'une tâche en temps réel, un chargeur peut ne pas être nécessaire puisque la création d'une tâche se fait généralement rapidement et n'implique aucun processus long comme la récupération de données depuis une API ou l'exécution de calculs complexes. Mais l'ajout d'un chargeur pendant la création d'une tâche peut encore être un indice visuel utile pour indiquer que la tâche est en cours de traitement et fournir un retour immédiat à l'utilisateur.

## Conclusion

Nous avons exploré le monde de la création de belles animations personnalisées dans Flutter, en nous concentrant sur l'implémentation de la Liste Animée et du Chargeur Animé. En comprenant la Liste Animée, nous avons appris comment créer des listes dynamiques et interactives avec des insertions et suppressions d'éléments fluides.

À travers ces exemples, vous avez vu la capacité de Flutter à rendre l'implémentation des animations agréable et simple. En incorporant des animations personnalisées dans vos applications, vous pouvez créer des interfaces engageantes et visuellement attrayantes qui captivent les utilisateurs et distinguent vos applications.

Si vous souhaitez en savoir plus sur Flutter, abonnez-vous à ma [newsletter par email](https://5minslearn.gogosoon.com/?ref=fcc_flutter_animation) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_flutter_animation)) et suivez-moi sur les réseaux sociaux.

Bonne Animation et Bonne Utilisation de Flutter ! 🚀