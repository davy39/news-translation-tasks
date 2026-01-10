---
title: Comment utiliser les Streams dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-10-29T21:57:11.148Z'
originalURL: https://freecodecamp.org/news/how-to-use-streams-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761774911652/ca6749c7-391b-4a9f-9264-5f15e54855ee.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: flutter-aware
  slug: flutter-aware
- name: Streams
  slug: streams
seo_title: Comment utiliser les Streams dans Flutter
seo_desc: Flutter, Google's open-source UI software development toolkit, has rapidly
  become a preferred choice for building natively compiled, cross-platform applications
  from a single codebase. Its declarative UI paradigm, coupled with robust performance,
  hel...
---

Flutter, le Framework de développement logiciel d'interface utilisateur open-source de Google, est rapidement devenu un choix privilégié pour créer des applications multiplateformes compilées nativement à partir d'une base de code unique. Son paradigme d'UI déclaratif, associé à des performances robustes, aide les développeurs à concevoir des expériences utilisateur magnifiques et hautement réactives.

Mais pour construire des applications aussi dynamiques et efficaces dans Flutter, vous aurez besoin d'une compréhension approfondie de la programmation asynchrone. Et dans ce domaine, les **streams** sont un outil indispensable.

Ce guide complet plongera au cœur de l'univers des streams dans Flutter, en démystifiant leurs concepts fondamentaux, en illustrant leurs applications pratiques et en fournissant une multitude d'exemples de code pour consolider votre compréhension.

## Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Le défi des opérations asynchrones](#heading-le-defi-des-operations-asynchrones)
    
3. [Que sont les Streams ? Le flux d'événements asynchrones](#heading-que-sont-les-streams-le-flux-devenements-asynchrones)
    
    * [Analogie : La rivière de données](#heading-analogie-la-riviere-de-donnees)
        
4. [Pourquoi les Streams sont cruciaux dans Flutter](#heading-pourquoi-les-streams-sont-cruciaux-dans-flutter)
    
5. [Concepts clés des Streams](#heading-concepts-cles-des-streams)
    
    * [1\. StreamController](#heading-1-streamcontroller)
        
    * [Types de Streams : Single-Subscription vs. Broadcast](#heading-types-de-streams-single-subscription-vs-broadcast)
        
    * [2\. StreamBuilder](#heading-2-streambuilder)
        
    * [3\. StreamSubscription](#heading-3-streamsubscription)
        
    * [Programmation asynchrone avec les Streams : async\* et yield](#heading-programmation-asynchrone-avec-les-streams-async-et-yield)
        
6. [Comment travailler avec les Streams : Scénarios pratiques](#heading-comment-travailler-avec-les-streams-scenarios-pratiques)
    
    * [1\. Transformer les Streams : map, where, take, skip, etc.](#heading-1-transformer-les-streams-map-where-take-skip-etc)
        
    * [2\. Combiner des Streams](#heading-2-combiner-des-streams)
        
7. [Exemples concrets dans Flutter](#heading-exemples-concrets-dans-flutter)
    
    * [1\. Récupération de données réseau avec mises à jour en direct](#heading-1-recuperation-de-donnees-reseau-avec-mises-a-jour-en-direct)
        
    * [2\. Gestion des entrées utilisateur : Debouncing d'un champ de recherche](#heading-2-gestion-des-entrees-utilisateur-debouncing-dun-champ-de-recherche)
        
8. [Bonnes pratiques et considérations](#heading-bonnes-pratiques-et-considerations)
    
9. [Concepts avancés (Brève introduction)](#heading-concepts-avances-breve-introduction)
    
10. [Conclusion](#heading-conclusion)
    
11. [Références](#heading-references)
    
    * [Documentation officielle](#heading-documentation-officielle)
        
    * [Packages clés](#heading-packages-cles)
        
    * [Articles et tutoriels (Général)](#heading-articles-et-tutoriels-general)
        
    * [Modèles de gestion d'état associés](#heading-modeles-de-gestion-detat-associes)
        
    * [Package HTTP (pour les exemples réseau)](#heading-package-http-pour-les-exemples-reseau)
        

## Prérequis

Avant de nous lancer dans ce voyage, assurez-vous d'avoir une compréhension de base de :

1. **Langage de programmation Dart :** Familiarité avec la syntaxe de Dart, les variables, les fonctions et les concepts orientés objet.
    
2. **Fondamentaux de Flutter :** Connaissance des widgets Flutter, `StatefulWidget` vs `StatelessWidget`, et de la mise en page de base de l'UI.
    
3. **Bases de la programmation asynchrone (le** `Future` **de Dart) :** Une compréhension de ce qu'un `Future` représente et comment les mots-clés `async`/`await` fonctionnent pour gérer des opérations asynchrones uniques. Si vous débutez avec `Future`, voyez-le comme un conteneur pour une valeur qui sera disponible à un moment donné dans le futur.
    

Si vous êtes à l'aise avec ces concepts, vous êtes prêt à explorer la puissance des streams.

## Le défi des opérations asynchrones

Dans les applications modernes, bloquer l'UI est une mauvaise pratique. Imaginez une application qui se fige pendant qu'elle récupère des données sur Internet, traite un fichier volumineux ou effectue un calcul complexe. Cela conduit à une expérience utilisateur frustrante.

La programmation synchrone traditionnelle exécute les tâches de manière séquentielle. Lorsqu'une tâche longue est rencontrée, tout le programme attend qu'elle se termine. La programmation asynchrone, en revanche, permet aux tâches de s'exécuter en arrière-plan sans bloquer le thread d'exécution principal, en particulier le thread de l'UI.

La classe `Future` de Dart est excellente pour gérer des événements asynchrones uniques (par exemple, une requête réseau unique qui renvoie une seule donnée). Mais que se passe-t-il si vous avez un flux continu d'événements ? Et si vous devez écouter des mises à jour de données au fil du temps, comme des messages de chat en temps réel, des lectures de capteurs ou des entrées utilisateur continues ? C'est là que les `Streams` brillent.

## Que sont les Streams ? Le flux d'événements asynchrones

Dans Flutter (et Dart), un **stream** est fondamentalement une séquence d'événements asynchrones. Considérez-le comme un tapis roulant transportant des éléments de données au fil du temps. Ces événements peuvent être :

1. **Valeurs de données :** L'information réelle transmise (par exemple, des entiers, des chaînes de caractères, des objets personnalisés).
    
2. **Erreurs :** Des signaux indiquant que quelque chose s'est mal passé pendant la séquence d'événements.
    
3. **Terminaison du stream :** Un signal indiquant qu'aucun autre événement ne sera envoyé.
    

Les streams offrent un puissant paradigme de programmation réactive, permettant à votre application de réagir aux événements au fur et à mesure qu'ils se produisent, sans bloquer l'interface utilisateur. Cela permet la création d'applications hautement réactives et efficaces.

### Analogie : La rivière de données

Imaginez une rivière. L'eau qui coule dans la rivière est comme les données (événements) dans un stream.

* Vous pouvez installer un **auditeur** (comme un filet de pêche) pour attraper les poissons (données) au fur et à mesure qu'ils passent.
    
* Parfois, des débris (erreurs) peuvent descendre la rivière.
    
* Finalement, la rivière peut s'assécher (terminaison du stream).
    

Ce flux continu est ce qui distingue les streams des objets `Future`, qui représentent une seule « livraison » plutôt qu'un « flux » continu.

### Pourquoi les Streams sont cruciaux dans Flutter

1. **Mises à jour en temps réel :** Idéal pour les applications de chat, les flux de données en direct (bourse, météo) et les données de capteurs.
    
2. **Gestion des événements :** Gérer les entrées utilisateur continues (par exemple, les suggestions de barre de recherche), les gestes ou les notifications.
    
3. **Découplage de la logique :** Séparer la récupération/le traitement des données du rendu de l'UI, ce qui conduit à un code plus propre et plus facile à maintenir.
    
4. **Gestion d'état :** De nombreuses solutions avancées de gestion d'état Flutter (comme BLoC, le `StreamProvider` de Provider) exploitent largement les Streams.
    

Voici une représentation visuelle du fonctionnement d'un stream :

![une représentation visuelle du fonctionnement d'un stream](https://cdn.hashnode.com/res/hashnode/image/upload/v1761638371213/7029f337-d63d-4178-b24c-6678173349ed.png align="center")

## Concepts clés des Streams

Pour travailler efficacement avec les Streams, vous devez comprendre quelques composants de base :

### 1\. `StreamController`

Un `StreamController` est votre outil principal pour créer et gérer des streams. Il agit à la fois comme un **sink** (où vous ajoutez des données/événements au stream) et une **source** (d'où vous pouvez obtenir le stream pour l'écouter). C'est le mécanisme qui vous permet de « contrôler » le flux d'événements dans votre stream.

Le but d'un `StreamController` est de créer, gérer et ajouter des événements (données, erreurs, signaux de fin) à un stream.

**Exemple de code :**

```dart
import 'dart:async'; // Requis pour StreamController

void main() {
  // 1. Créer un StreamController pour des données de type String
  //    L'argument de type <String> spécifie le type de données que ce stream émettra.
  final streamController = StreamController<String>();

  // 2. Obtenir le stream à partir du contrôleur
  //    C'est le stream que d'autres parties de votre application écouteront.
  Stream<String> myStream = streamController.stream;

  // 3. Écouter le stream
  //    La méthode .listen() enregistre un rappel pour gérer les données entrantes.
  //    Elle renvoie une StreamSubscription, qui peut être utilisée pour gérer l'auditeur.
  var subscription = myStream.listen((data) {
    print('Données reçues : $data');
  });

  // 4. Ajouter des données au stream
  //    Utilisez la propriété sink du contrôleur pour ajouter des événements.
  streamController.sink.add('Hello');
  streamController.sink.add('Flutter');
  streamController.sink.add('Streams!');

  // 5. Simuler une erreur
  //    Vous pouvez également ajouter des erreurs au stream.
  streamController.sink.addError('Quelque chose s\'est mal passé !');

  // 6. Fermer le stream quand vous avez terminé
  //    Il est crucial de fermer le contrôleur de stream pour éviter les fuites de mémoire.
  //    Cela envoie également un événement "done" à tous les auditeurs.
  streamController.close();

  // Optionnellement, annuler l'abonnement s'il n'est plus nécessaire avant la fermeture du stream
  // subscription.cancel();
}
```

Dans ce code :

La ligne `final streamController = StreamController<String>();` initialise un `StreamController` conçu pour gérer des données `String`, bien qu'il puisse être créé pour n'importe quel type de données (par exemple, `int`, classes personnalisées, etc.). L'instruction `Stream<String> myStream = streamController.stream;` récupère le `Stream` réel auquel les consommateurs, tels que les widgets `StreamBuilder` ou d'autres auditeurs, peuvent s'abonner.

En appelant `myStream.listen((data) { ... });`, vous configurez un auditeur qui exécute la fonction de rappel fournie chaque fois que `streamController.sink.add()` est invoqué avec de nouvelles données. Pour émettre des données, vous utilisez `streamController.sink.add('Hello');`, tandis que `streamController.sink.addError('Quelque chose s\'est mal passé !');` vous permet d'émettre des événements d'erreur auxquels les auditeurs peuvent répondre.

Enfin, l'appel à `streamController.close();` est essentiel, car il informe tous les auditeurs que le stream est terminé et n'émettra plus d'événements, tout en libérant les ressources. Négliger de fermer un contrôleur peut provoquer des fuites de mémoire, en particulier dans les applications à longue durée de vie.

### Types de Streams : Single-Subscription vs. Broadcast

Les streams existent en deux variantes, chacune adaptée à des cas d'utilisation différents :

1. **Streams à abonnement unique (Single-Subscription - Par défaut) :**
    
    * **Objectif :** Conçu pour un seul auditeur. Une fois que vous l'avez écouté via `listen()`, vous ne pouvez pas l'écouter à nouveau, sauf si le premier abonnement est annulé ou si le stream est créé en tant que stream de diffusion (broadcast).
        
    * **Cas d'utilisation :** Récupération de données (comme la lecture d'un fichier), réponses HTTP où vous n'avez besoin que d'un seul composant pour consommer le résultat.
        
    * **Exemple :** Lorsque vous appelez `http.get(...).asStream()`, vous obtenez un stream à abonnement unique.
        
2. **Streams de diffusion (Broadcast Streams) :**
    
    * **Objectif :** Permet à plusieurs auditeurs de s'abonner et de recevoir des événements simultanément. Les événements sont livrés à tous les auditeurs actifs.
        
    * **Cas d'utilisation :** Mises à jour de données en temps réel où plusieurs widgets UI ou composants logiques ont besoin de la même information (par exemple, un statut d'authentification global, des notifications en temps réel).
        
    * **Création :** Vous créez un stream de diffusion en passant `broadcast: true` au constructeur du `StreamController` ou en utilisant `.asBroadcastStream()`.
        

**Exemple de code (Broadcast Stream) :**

```dart
import 'dart:async';

void main() async {
  // Créer un StreamController qui supporte plusieurs auditeurs
  final broadcastController = StreamController<int>.broadcast();

  // Auditeur 1
  broadcastController.stream.listen((event) {
    print('L\'auditeur 1 a reçu : $event');
  }, onError: (e) => print('Erreur auditeur 1 : $e'));

  // Auditeur 2 (peut écouter même pendant que l\'auditeur 1 est actif)
  broadcastController.stream.listen((event) {
    print('  L\'auditeur 2 a reçu : $event');
  }, onError: (e) => print('  Erreur auditeur 2 : $e'));

  broadcastController.sink.add(1);
  await Future.delayed(Duration(milliseconds: 500)); // Simuler un délai
  broadcastController.sink.add(2);
  await Future.delayed(Duration(milliseconds: 500));
  broadcastController.sink.addError('Erreur de diffusion !');
  await Future.delayed(Duration(milliseconds: 500));
  broadcastController.sink.add(3);

  await Future.delayed(Duration(seconds: 1)); // Laisser le temps aux événements d'être traités
  broadcastController.close(); // Fermer le contrôleur, notifiant tous les auditeurs
}
```

Dans `final broadcastController = StreamController<int>.broadcast();`, la clé est `.broadcast()`. Cela garantit que plusieurs appels `listen()` sur `broadcastController.stream` recevront tous les événements. L'auditeur 1 et l'auditeur 2 s'abonnent indépendamment et reçoivent `1`, `2`, l'erreur et `3`.

Choisissez soigneusement le type de stream en fonction des besoins de votre application. En cas de doute, commencez par un stream à abonnement unique et ne passez au broadcast que si c'est réellement nécessaire, car les streams de diffusion peuvent parfois rendre le débogage du flux d'événements plus complexe.

### 2\. `StreamBuilder`

Le widget `StreamBuilder` est l'outil dédié de Flutter pour intégrer les Streams directement dans votre UI. C'est un `StatefulWidget` sous le capot qui écoute un stream et reconstruit son UI chaque fois que de nouvelles données, des erreurs ou des signaux de fin arrivent. Cela rend votre UI réactive aux changements de données sans avoir à appeler manuellement `setState()`.

`StreamBuilder` reconstruit automatiquement une partie de l'UI en réponse aux nouvelles données d'un stream.

**Exemple de code :**

```dart
import 'package:flutter/material.dart';
import 'dart:async';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Démo StreamBuilder',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: StreamBuilderPage(),
    );
  }
}

class StreamBuilderPage extends StatefulWidget {
  @override
  _StreamBuilderPageState createState() => _StreamBuilderPageState();
}

class _StreamBuilderPageState extends State<StreamBuilderPage> {
  final _dataController = StreamController<int>();
  int _counter = 0;

  @override
  void initState() {
    super.initState();
    // Commencer à ajouter des données au stream chaque seconde
    Timer.periodic(Duration(seconds: 1), (timer) {
      _counter++;
      _dataController.sink.add(_counter);
      if (_counter >= 5) {
        timer.cancel(); // Arrêter d'ajouter après 5 événements
        _dataController.close(); // Fermer le stream
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Exemple StreamBuilder')),
      body: Center(
        // StreamBuilder est le widget central ici
        child: StreamBuilder<int>(
          stream: _dataController.stream, // Le stream à écouter
          // initialData: 0, // Optionnel : Une valeur à afficher avant l'arrivée des données
          builder: (context, snapshot) {
            // La fonction builder est appelée chaque fois que le stream émet un nouvel événement.
            // 'snapshot' contient le dernier état du stream.

            if (snapshot.connectionState == ConnectionState.waiting) {
              // Afficher un indicateur de chargement en attendant le premier événement
              return CircularProgressIndicator();
            } else if (snapshot.hasError) {
              // Afficher un message d'erreur si le stream émet une erreur
              return Text('Erreur : ${snapshot.error}', style: TextStyle(color: Colors.red));
            } else if (snapshot.hasData) {
              // Afficher les données reçues
              return Text(
                'Données reçues : ${snapshot.data}',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              );
            } else {
              // Ce cas peut se produire si le stream se ferme sans envoyer de données
              // ou si initialData n'a pas été fourni et qu'aucune donnée n'est encore arrivée.
              return Text('Pas encore de données ou stream fermé.');
            }
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Vous pourriez aussi ajouter des données via un bouton, par exemple
          // _dataController.sink.add(99);
        },
        child: Icon(Icons.add),
      ),
    );
  }

  @override
  void dispose() {
    // IMPORTANT : Fermer le StreamController quand le widget est détruit
    // pour éviter les fuites de mémoire.
    _dataController.close();
    super.dispose();
  }
}
```

C'est beaucoup d'informations – explorons donc ce qui se passe dans ce code :

Un widget `StreamBuilder<int>(stream: _dataController.stream, builder: (context, snapshot) { ... })` écoute un stream et reconstruit l'UI en réponse aux nouveaux événements ou aux changements d'état de connexion.

Le paramètre `stream` spécifie le stream à écouter, tandis que la fonction `builder` est appelée chaque fois que le stream émet un nouvel événement ou change d'état. Elle reçoit le `BuildContext` et un `AsyncSnapshot<T>`, qui encapsule les dernières données et le statut du stream.

Le `snapshot` fournit des détails clés sur le stream :

* `snapshot.connectionState` indique l'état actuel de la connexion : `none` (aucun stream connecté), `waiting` (connecté mais pas encore de données), `active` (reçoit activement des événements) et `done` (stream fermé).
    
* `snapshot.hasData` et `snapshot.data` indiquent si le stream a émis des données et permettent d'accéder à la valeur la plus récente.
    
* `snapshot.hasError` et `snapshot.error` gèrent les erreurs émises par le stream.
    

Dans le `builder`, le rendu conditionnel (utilisant des instructions `if` ou `switch`) vous permet d'afficher l'UI appropriée pour chaque état, comme des indicateurs de chargement, des messages d'erreur ou les données réelles.

Vous pouvez également spécifier `initialData` pour fournir une valeur de départ avant l'arrivée du premier événement, évitant ainsi les indicateurs de chargement inutiles si vous avez déjà un état initial connu.

Enfin, fermez toujours votre `StreamController` dans la méthode `dispose()` du widget pour éviter les fuites de mémoire lorsque le widget est retiré de l'arborescence.

### 3\. `StreamSubscription`

Lorsque vous appelez `stream.listen()`, cela renvoie un objet `StreamSubscription`. Cet objet représente la connexion active entre votre auditeur et le stream. Il est essentiel pour gérer le cycle de vie de votre auditeur.

`StreamSubscription` gère un auditeur actif sur un stream, principalement pour l'annuler.

**Exemple de code (déjà partiellement montré dans l'exemple** `StreamController`**, mais mettant l'accent sur** `StreamSubscription`) :

```dart
import 'dart:async';

void main() async {
  final streamController = StreamController<String>();

  StreamSubscription<String>? subscription; // Déclaré comme nullable

  // Écouter le stream et stocker l'objet d'abonnement
  subscription = streamController.stream.listen(
    (data) {
      print('Données reçues : $data');
      // Après avoir reçu 'Stop', annuler l'abonnement
      if (data == 'Stop') {
        print('Annulation de l\'abonnement...');
        subscription?.cancel(); // Utilisation de l'appel null-safe
        streamController.close(); // Fermer le contrôleur après l'arrêt
      }
    },
    onError: (error) {
      print('Erreur : $error');
    },
    onDone: () {
      print('Le stream est terminé (fermé) !');
    },
    cancelOnError: false, // Ne pas annuler l'abonnement si une erreur survient
  );

  streamController.sink.add('Start');
  await Future.delayed(Duration(milliseconds: 500));
  streamController.sink.add('Continue');
  await Future.delayed(Duration(milliseconds: 500));
  streamController.sink.add('Stop'); // Cela déclenchera l'annulation

  // Si le stream n'a pas été fermé par la logique 'Stop', assurez-vous qu'il l'est ici après un délai
  // await Future.delayed(Duration(seconds: 2));
  // if (!streamController.isClosed) {
  //   streamController.close();
  // }
}
```

Dans ce code, une variable `StreamSubscription<String>? subscription;` est déclarée pour contenir l'abonnement à un stream. Lorsque `subscription = streamController.stream.listen(...)` est appelé, la méthode `listen` renvoie un objet `StreamSubscription` qui vous permet de contrôler le comportement du stream.

La méthode `subscription?.cancel();` est la partie la plus cruciale : elle détache l'auditeur du stream, l'empêchant de recevoir d'autres événements. C'est particulièrement important pour les streams à abonnement unique ou lorsque vous devez arrêter temporairement d'écouter un stream de diffusion. Oublier d'annuler les abonnements, en particulier dans les `StatefulWidgets`, peut entraîner des fuites de mémoire.

La méthode `listen` accepte plusieurs paramètres :

* Le premier argument positionnel est le rappel `onData` (déclenché à l'arrivée de nouvelles données)
    
* `onError` est un rappel optionnel pour gérer les erreurs
    
* `onDone` est un rappel optionnel pour la fermeture du stream
    
* Et `cancelOnError` est un booléen qui, lorsqu'il est vrai, annule automatiquement l'abonnement après la première erreur, arrêtant tous les événements ultérieurs.
    

### Programmation asynchrone avec les Streams : `async*` et `yield`

Alors que `StreamController` vous donne un contrôle précis sur l'ajout d'événements, Dart propose également une manière plus déclarative de créer des streams en utilisant `async*` et `yield`. Cette syntaxe est similaire à `async`/`await` pour les `Future`s mais pour des flux continus de données.

1. `async*` (fonction générateur asynchrone) : Une fonction marquée par `async*` renvoie un `Stream`.
    
2. `yield` : À l'intérieur d'une fonction `async*`, `yield` est utilisé pour émettre des événements de données vers le stream.
    

Nous utilisons `async*` et `yield` pour créer facilement des streams en produisant itérativement des données sans gérer manuellement un `StreamController`.

**Exemple de code :**

```dart
import 'dart:async';

// Une fonction qui renvoie un Stream d'entiers
Stream<int> countStream(int max) async* {
  for (int i = 1; i <= max; i++) {
    // Simuler un travail asynchrone
    await Future.delayed(Duration(milliseconds: 500));
    // Produire (émettre) la valeur actuelle vers le stream
    yield i;
  }
  // Pas besoin de close() explicite ; le stream se ferme automatiquement à la fin de la fonction.
}

void main() {
  print('Démarrage du stream...');
  // Écouter le stream généré par countStream
  final subscription = countStream(5).listen(
    (data) {
      print('Reçu : $data');
    },
    onDone: () {
      print('Le stream est terminé !');
    },
    onError: (error) {
      print('Erreur dans le stream : $error');
    },
  );

  // Vous pouvez toujours annuler l'abonnement manuellement si nécessaire
  // Future.delayed(Duration(seconds: 2), () => subscription.cancel());
}
```

Dans ce code, la fonction `Stream<int> countStream(int max) async*` utilise le mot-clé `async*` pour indiquer qu'elle renvoie un stream. À l'intérieur, `await Future.delayed(Duration(milliseconds: 500));` démontre qu'on peut toujours utiliser `await` dans une fonction `async*` pour suspendre l'exécution jusqu'à ce qu'un futur se termine, permettant des opérations asynchrones pendant la génération du stream.

L'instruction `yield i;` est ce qui ajoute chaque valeur au stream. Chaque fois qu'elle est appelée, la valeur `i` est émise en tant qu'événement, et la fonction s'interrompt jusqu'à ce que la valeur suivante soit prête ou demandée.

Lorsque la fonction se termine (par exemple, à la fin de la boucle `for`), le stream se ferme automatiquement et émet un événement `onDone` à tous les auditeurs, rendant la gestion du stream plus simple que l'utilisation manuelle d'un `StreamController`.

Cette syntaxe `async*`/`yield` est particulièrement élégante pour générer des flux de données dont la séquence est connue ou peut être calculée de manière itérative.

## Comment travailler avec les Streams : Scénarios pratiques

Explorons les modèles et opérations courants avec les streams.

### 1\. Transformer les Streams : `map`, `where`, `take`, `skip`, etc.

Les streams sont puissants car ils sont itérables, ce qui signifie que vous pouvez appliquer diverses transformations à leur flux de données en utilisant des méthodes similaires à celles trouvées sur les `Iterable`s de Dart (`List`, `Set`).

```dart
import 'dart:async';

void main() async {
  final numbersController = StreamController<int>();

  // Créer un stream qui émet les carrés des nombres d'un autre stream,
  // mais seulement pour les nombres pairs, et ne prend que les 3 premiers résultats.
  numbersController.stream
      .where((number) => number % 2 == 0) // Ne laisse passer que les nombres pairs
      .map((evenNumber) => evenNumber * evenNumber) // Transforme les nombres pairs en leurs carrés
      .take(3) // Ne prend que les 3 premiers carrés de nombres pairs
      .listen(
        (squaredEven) {
          print('Données transformées : $squaredEven');
        },
        onDone: () {
          print('Le stream transformé est terminé !');
        },
        onError: (e) {
          print('Erreur du stream transformé : $e');
        }
      );

  // Ajouter des nombres au stream source
  numbersController.sink.add(1);
  numbersController.sink.add(2); // Passe le where, map vers 4, pris (1er)
  numbersController.sink.add(3);
  numbersController.sink.add(4); // Passe le where, map vers 16, pris (2e)
  numbersController.sink.add(5);
  numbersController.sink.add(6); // Passe le where, map vers 36, pris (3e)
  numbersController.sink.add(7);
  numbersController.sink.add(8); // Ne sera pas traité à cause de .take(3)
  await Future.delayed(Duration(milliseconds: 100)); // Laisser les événements être traités

  numbersController.close();
}
```

Dans les streams Dart, plusieurs méthodes de transformation et de filtrage sont disponibles :

* `.where(bool test(T element))` filtre les événements selon une condition
    
* `.map<R>(R convert(T event))` transforme chaque événement d'un type vers un autre
    
* `.take(int count)` n'émet que le nombre spécifié de premiers événements
    
* `.skip(int count)` ignore les premiers événements et émet le reste
    
* `.distinct()` ne laisse passer que les événements consécutifs uniques
    
* `.first`, `.last`, et `.single` renvoient un `Future` qui se termine respectivement par le premier, le dernier ou l'unique événement
    
* `.fold<R>(R initialValue, R combine(R previous, T element))` accumule les valeurs comme `reduce`
    
* `.asyncMap<R>(FutureOr<R> convert(T event))` applique des transformations asynchrones à chaque événement, ce qui est utile pour les opérations asynchrones sur les éléments du stream.
    

Ces opérateurs sont incroyablement puissants pour manipuler et affiner le flux de données au sein de votre application.

### 2\. Combiner des Streams

Parfois, vous devez combiner des événements provenant de plusieurs streams.

1. `Stream.fromFutures(Iterable<Future<T>> futures)` : Crée un stream qui émet les résultats de plusieurs `Future(s)` au fur et à mesure qu'ils se terminent.
    
2. `StreamGroup` (du package `async`) : Un utilitaire pour combiner plusieurs streams en un seul stream, en préservant l'ordre des événements des streams originaux.
    

**Exemple de code (Stream.fromFutures) :**

```dart
import 'dart:async';

Future<String> fetchUserData(String userId) async {
  await Future.delayed(Duration(seconds: 1));
  return 'Données utilisateur pour $userId';
}

Future<String> fetchProductData(String productId) async {
  await Future.delayed(Duration(milliseconds: 500));
  return 'Données produit pour $productId';
}

void main() {
  final userFuture = fetchUserData('user123');
  final productFuture = fetchProductData('prod456');

  // Créer un stream à partir de ces deux futures
  Stream.fromFutures([userFuture, productFuture]).listen(
    (data) {
      print('Reçu : $data');
    },
    onDone: () {
      print('Tous les futures sont terminés et le stream est clos.');
    },
    onError: (e) {
      print('Erreur : $e');
    }
  );
}
```

Le stream créé par `Stream.fromFutures` émettra d'abord « Données produit pour prod456 » (car il se résout plus vite), puis « Données utilisateur pour user123 ». Cela démontre que les événements sont émis au fur et à mesure que leurs futures respectifs se terminent, pas nécessairement dans l'ordre où ils ont été fournis dans la liste.

## Exemples concrets dans Flutter

### 1\. Récupération de données réseau avec mises à jour en direct

Imaginez une application affichant une liste d'articles de presse qui doit se rafraîchir automatiquement.

```dart
import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http; // Ajouter http: ^0.13.0 au pubspec.yaml

// Modèle pour un Article simple
class Article {
  final String title;
  final String description;

  Article({required this.title, required this.description});

  factory Article.fromJson(Map<String, dynamic> json) {
    return Article(
      title: json['title'] ?? 'Sans titre',
      description: json['body'] ?? 'Pas de description', // Utilisation de 'body' pour simplifier
    );
  }
}

class NewsService {
  final _articleController = StreamController<List<Article>>.broadcast();
  Stream<List<Article>> get articlesStream => _articleController.stream;

  Timer? _refreshTimer;

  NewsService() {
    _startAutoRefresh();
  }

  Future<void> _fetchArticles() async {
    try {
      final response = await http.get(Uri.parse('https://jsonplaceholder.typicode.com/posts?_limit=5')); // Fake API
      if (response.statusCode == 200) {
        List<dynamic> jsonList = json.decode(response.body);
        List<Article> fetchedArticles = jsonList.map((json) => Article.fromJson(json)).toList();
        _articleController.sink.add(fetchedArticles);
      } else {
        _articleController.sink.addError('Échec du chargement des articles : ${response.statusCode}');
      }
    } catch (e) {
      _articleController.sink.addError('Erreur réseau : $e');
    }
  }

  void _startAutoRefresh() {
    _fetchArticles(); // Récupération immédiate
    _refreshTimer = Timer.periodic(Duration(seconds: 10), (timer) {
      print('Rafraîchissement automatique des articles...');
      _fetchArticles(); // Récupération toutes les 10 secondes
    });
  }

  void dispose() {
    _refreshTimer?.cancel();
    _articleController.close();
  }
}

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flux d\'actualités en direct',
      theme: ThemeData(primarySwatch: Colors.deepPurple),
      home: NewsFeedPage(),
    );
  }
}

class NewsFeedPage extends StatefulWidget {
  @override
  _NewsFeedPageState createState() => _NewsFeedPageState();
}

class _NewsFeedPageState extends State<NewsFeedPage> {
  final NewsService _newsService = NewsService();

  @override
  void dispose() {
    _newsService.dispose(); // Important : libérer le service quand le widget disparaît
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Flux d\'actualités en direct')),
      body: StreamBuilder<List<Article>>(
        stream: _newsService.articlesStream,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Text('Erreur : ${snapshot.error}', style: TextStyle(color: Colors.red, fontSize: 18)),
              ),
            );
          } else if (snapshot.hasData) {
            final articles = snapshot.data!;
            if (articles.isEmpty) {
              return Center(child: Text('Aucun article trouvé.'));
            }
            return ListView.builder(
              itemCount: articles.length,
              itemBuilder: (context, index) {
                final article = articles[index];
                return Card(
                  margin: EdgeInsets.all(8.0),
                  elevation: 4.0,
                  child: Padding(
                    padding: const EdgeInsets.all(16.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(article.title, style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                        SizedBox(height: 8),
                        Text(article.description, style: TextStyle(fontSize: 14, color: Colors.grey[700])),
                      ],
                    ),
                  ),
                );
              },
            );
          } else {
            return Center(child: Text('En attente d\'actualités...'));
          }
        },
      ),
    );
  }
}
```

Dans ce code, la classe `NewsService` encapsule la logique de récupération des articles. Elle utilise un `StreamController.broadcast()` pour permettre à plusieurs widgets d'écouter les mises à jour d'articles, même si dans cet exemple seul `NewsFeedPage` le fait.

La méthode `_fetchArticles()` gère la requête HTTP réelle, tandis que `_startAutoRefresh()` lance une récupération immédiate et utilise un `Timer.periodic` pour déclencher de nouvelles récupérations toutes les 10 secondes, ajoutant chaque nouvelle liste d'articles au `_articleController.sink`. La méthode `dispose()` est essentielle pour annuler le minuteur et fermer le contrôleur de stream afin d'éviter les fuites de mémoire.

Côté UI, `NewsFeedPage` crée une instance de `NewsService`, et dans sa méthode `dispose()`, elle appelle `_newsService.dispose()` pour libérer les ressources. Un `StreamBuilder<List<Article>>` écoute `_newsService.articlesStream`, et sa fonction builder met à jour l'UI dynamiquement, affichant un indicateur de chargement, un message d'erreur ou la liste des articles au fur et à mesure que de nouveaux événements arrivent du stream.

Ce modèle est un moyen robuste de gérer des données dynamiques mises à jour de manière asynchrone dans vos applications Flutter.

### 2\. Gestion des entrées utilisateur : Debouncing d'un champ de recherche

Imaginez une barre de recherche où vous ne voulez pas effectuer un appel API de recherche à chaque frappe de touche, mais plutôt après que l'utilisateur a fait une pause dans sa saisie pendant une courte durée (debouncing).

```dart
import 'package:flutter/material.dart';
import 'dart:async';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Recherche avec Debounce',
      theme: ThemeData(primarySwatch: Colors.green),
      home: DebouncedSearchPage(),
    );
  }
}

class DebouncedSearchPage extends StatefulWidget {
  @override
  _DebouncedSearchPageState createState() => _DebouncedSearchPageState();
}

class _DebouncedSearchPageState extends State<DebouncedSearchPage> {
  final TextEditingController _searchController = TextEditingController();
  final _searchQueryController = StreamController<String>.broadcast();

  String _lastSearchedTerm = '';
  StreamSubscription<String>? _debouncedSubscription;

  @override
  void initState() {
    super.initState();

    // Écouter les changements dans le champ de texte
    _searchController.addListener(() {
      _searchQueryController.sink.add(_searchController.text);
    });

    // Appliquer le debounce sur le stream de requêtes de recherche
    _debouncedSubscription = _searchQueryController.stream
        .distinct() // N'émettre que si la valeur est différente de la précédente
        .debounce(Duration(milliseconds: 500)) // Attendre 500ms après le dernier événement
        .listen((query) {
          if (query.isNotEmpty) {
            _performSearch(query);
          } else {
            setState(() {
              _lastSearchedTerm = '';
         });
          }
        });
     }

  void _performSearch(String query) {
    // Dans une application réelle, ce serait un appel API
    print('Exécution de la recherche pour : "$query"');
    setState(() {
      _lastSearchedTerm = query;
    });
  }

  @override
  void dispose() {
    _searchController.dispose();
    _searchQueryController.close();
    _debouncedSubscription?.cancel(); // Annuler l'abonnement
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Recherche avec Debounce')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _searchController,
              decoration: InputDecoration(
                labelText: 'Rechercher',
                hintText: 'Tapez pour rechercher...',
                prefixIcon: Icon(Icons.search),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8.0),
                ),
              ),
              onChanged: (text) {
                // Le addListener gère déjà l'ajout au stream
              },
            ),
            SizedBox(height: 20),
            Text(
              _lastSearchedTerm.isEmpty
                  ? 'Commencez à taper pour rechercher.'
                  : 'Dernière recherche effectuée : "${_lastSearchedTerm}"',
              style: TextStyle(fontSize: 18),
            ),
            SizedBox(height: 10),
            Text(
              'Une recherche est déclenchée 500ms après l\'arrêt de la saisie.',
              style: TextStyle(fontSize: 14, color: Colors.grey),
            ),
          ],
        ),
      ),
    );
  }
}

// Extension pour ajouter un opérateur debounce à n'importe quel Stream<T>
extension DebounceExtension<T> on Stream<T> {
  Stream<T> debounce(Duration duration) => transform(
    _DebounceStreamTransformer(duration),
  );
}

// StreamTransformer personnalisé pour le debouncing
class _DebounceStreamTransformer<T> extends StreamTransformerBase<T, T> {
  final Duration duration;

  _DebounceStreamTransformer(this.duration);

  @override
  Stream<T> bind(Stream<T> stream) {
    StreamController<T> controller = StreamController<T>();
    Timer? _timer;
    StreamSubscription<T>? _subscription;

    controller.onListen = () {
      _subscription = stream.listen(
        (data) {
          _timer?.cancel(); // Annuler le minuteur précédent
          _timer = Timer(duration, () {
            controller.add(data); // Ajouter les données après la durée
            _timer = null;
          });
        },
        onError: controller.addError,
        onDone: () {
          _timer?.cancel(); // S'assurer que le minuteur est annulé si le stream est fini
          controller.close();
        },
      );
    };

    controller.onPause = () => _subscription?.pause();
    controller.onResume = () => _subscription?.resume();
    controller.onCancel = () {
      _timer?.cancel(); // Annuler tout minuteur en attente
      return _subscription?.cancel();
    };

    return controller.stream;
  }
}    
```

Dans ce code, le `TextEditingController _searchController` est un contrôleur Flutter standard qui gère le texte à l'intérieur d'un `TextField`. À ses côtés, le `StreamController<String> _searchQueryController` sert de stream source pour tous les changements bruts de saisie de texte. C'est un stream de diffusion, permettant à plusieurs auditeurs, comme la logique de debouncing, de recevoir des événements chaque fois que la saisie change.

Chaque fois que l'utilisateur tape, `_searchController.addListener(() { _searchQueryController.sink.add(_searchController.text); });` ajoute la dernière valeur de texte au stream `_searchQueryController`. Cela garantit que chaque changement de saisie émet un événement dans le stream.

La ligne `debouncedSubscription = _searchQueryController.stream ... .listen(...);` contient la logique principale de debouncing. L'opérateur `.distinct()` garantit que les saisies identiques (comme taper « pomme », l'effacer et retaper « pomme ») ne déclenchent pas d'événements redondants. L'opérateur `.debounce(Duration(milliseconds: 500))`, implémenté comme un transformateur de stream personnalisé, attend 500 millisecondes d'inactivité avant d'émettre la valeur la plus récente, réinitialisant son minuteur à chaque nouvel événement. Une fois que la requête « debouncée » est enfin émise, `.listen((query) { performSearch(query); });` exécute la méthode `performSearch` avec cette requête.

L'`DebounceExtension` et le `_DebounceStreamTransformer` rendent cela possible en définissant un `StreamTransformer` personnalisé. La logique centrale réside dans `bind(Stream<T> stream)`, qui prend le stream original et en produit un transformé. À l'intérieur, un nouveau `StreamController` est créé pour gérer le stream de sortie, tandis que le stream d'entrée est écouté avec `stream.listen(...)`.

Le comportement de debouncing est obtenu en annulant tout minuteur existant et en en démarrant un nouveau (`timer?.cancel(); timer = Timer(duration, () { ... });`). Lorsque le minuteur se termine sans nouveaux événements, les données sont émises via `controller.add(data)`. Les méthodes de cycle de vie comme `onCancel`, `onPause` et `onResume` gèrent le nettoyage et le contrôle appropriés, assurant une gestion efficace des ressources lorsque les auditeurs sont mis en pause, repris ou annulés.

Ce modèle de debounce est incroyablement utile pour optimiser les opérations coûteuses liées à une saisie utilisateur rapide.

## Bonnes pratiques et considérations

Gardez à l'esprit les points suivants lorsque vous travaillez avec des streams :

1. **Toujours fermer les** `StreamControllers` **:** C'est primordial. Oublier d'appeler `_controller.close()` (en particulier dans les méthodes `dispose()` des `StatefulWidgets` ou lorsqu'un service n'est plus nécessaire) entraîne des fuites de mémoire. Si vous utilisez `async*`/`yield`, le stream se ferme automatiquement à la fin de la fonction générateur.
    
2. **Annuler les** `StreamSubscriptions` **:** Si vous appelez manuellement `stream.listen()`, n'oubliez pas de stocker la `StreamSubscription` renvoyée et d'appeler `subscription.cancel()` lorsque vous n'avez plus besoin d'écouter. Encore une fois, cela se fait généralement dans `dispose()`. `StreamBuilder` gère ses abonnements internes automatiquement.
    
3. **Choisir le bon type de stream :**
    
    * **Abonnement unique (Single-Subscription) :** Pour les flux de données ponctuels, comme la lecture d'un fichier ou une réponse HTTP unique.
        
    * **Diffusion (Broadcast) :** Pour plusieurs widgets UI ou composants logiques devant réagir au même flux d'événements continu. Utilisez `StreamController.broadcast()`.
        
4. **Gestion des erreurs :** Implémentez toujours des rappels `onError` pour `listen()` et gérez `snapshot.hasError` dans `StreamBuilder` pour offrir une expérience utilisateur robuste.
    
5. `initialData` **avec** `StreamBuilder` **:** Utilisez `initialData` lorsque vous avez une valeur significative à afficher avant l'arrivée du premier événement du stream. Cela peut éviter de brefs indicateurs de chargement si l'état initial est connu.
    
6. **Éviter l'imbrication excessive de** `StreamBuilder` **:** Bien que pratique, avoir trop de `StreamBuilders` imbriqués peut mener à un code complexe et à des problèmes de performance potentiels s'ils ne sont pas bien gérés. Envisagez de consolider la logique des streams liés.
    
7. **Tester les streams :** Simulez des `StreamControllers` ou utilisez `Stream.fromIterable` pour créer des streams de test pour vos widgets et votre logique métier.
    
8. **Extensions réactives (RxDart) :** Pour des opérations de stream plus avancées (combinaison, throttling, buffering, etc.), envisagez d'utiliser le package rxdart. Il fournit un riche ensemble d'opérateurs inspirés de ReactiveX, rendant la logique asynchrone complexe plus gérable et déclarative.
    

## Concepts avancés (Brève introduction)

Si vous souhaitez aller plus loin avec les streams, il existe des concepts clés à comprendre. Voici une brève introduction pour savoir vers quoi vous diriger :

1. **RxDart :** Comme mentionné, RxDart étend l'API Stream de Dart avec des opérateurs puissants. Si vous avez besoin de manipulations de streams plus complexes que ce que propose l'API standard de Dart, RxDart est l'étape logique suivante. Il introduit des concepts comme `BehaviorSubject` (un `StreamController` qui mémorise la dernière valeur émise et l'émet immédiatement aux nouveaux auditeurs) et `PublishSubject`.
    
2. **Modèle BLoC/Cubit :** De nombreuses solutions de gestion d'état Flutter populaires, comme le modèle BLoC (Business Logic Component), reposent lourdement sur les streams. Les BLoCs exposent des streams (utilisant souvent des `StreamController`s en interne) pour que l'UI écoute les changements d'état, découplant complètement la présentation de la logique métier.
    
3. **Générateurs de flux avec** `sync*` **et** `yield` **(pour les Iterables) :** Alors que `async*`/`yield` créent des Streams, Dart possède également `sync*`/`yield` pour créer des Iterables (séquences synchrones). Ce n'est pas directement lié aux streams asynchrones mais utilise une syntaxe similaire.
    

## Conclusion

Les streams sont une pierre angulaire de la programmation asynchrone moderne dans Flutter. En comprenant `StreamController`, `StreamBuilder`, `StreamSubscription` et la syntaxe `async*`/`yield`, vous acquérez le pouvoir de construire des applications hautement réactives, efficaces et dynamiques.

De la gestion des données réseau aux interactions utilisateur en temps réel, les streams offrent un mécanisme flexible et robuste pour gérer des séquences d'événements asynchrones. Adoptez-les, et vous débloquerez un nouveau niveau de réactivité et d'élégance dans votre développement Flutter.

## Références

### Documentation officielle

1. [Tutoriel Dart Streams (Site officiel de Dart)](https://dart.dev/tutorials/language/streams) **:** C'est la ressource fondamentale. Elle couvre les concepts de base des streams en Dart, y compris `StreamController`, `listen`, `async*`/`yield`, et les transformations de base.
    
2. [Documentation de l'API de la classe `Stream` (Dart)](https://api.dev/stable/dart-async/Stream-class.html) : La référence complète pour toutes les méthodes et propriétés de la classe `Stream` elle-même. Essentiel pour comprendre les méthodes de transformation comme `map`, `where`, `take`, `skip`, etc.
    
3. [Documentation de l'API de la classe `StreamController` (Dart)](https://api.dev/stable/dart-async/StreamController-class.html) : Détails sur la création et la gestion des `StreamController`s, y compris l'abonnement unique vs diffusion.
    
4. [Documentation de l'API de la classe `StreamSubscription` (Dart)](https://api.dev/stable/dart-async/StreamSubscription-class.html) : Informations sur la gestion de vos auditeurs et l'annulation des abonnements.
    
5. [Documentation de l'API du widget `StreamBuilder` (Flutter)](https://api.flutter.dev/flutter/widgets/StreamBuilder-class.html) : La documentation officielle de Flutter pour le widget `StreamBuilder`, expliquant ses propriétés (`stream`, `builder`, `initialData`) et l'`AsyncSnapshot`.
    

### Packages clés

1. [Package `async`](https://pub.dev/packages/async) : Fournit des utilitaires pour la programmation asynchrone en Dart, y compris `StreamGroup` qui est utile pour combiner plusieurs streams.
    
2. [Package `rxdart`](https://pub.dev/packages/rxdart) : Étend les streams de Dart avec des opérateurs Rx (ReactiveX) puissants, rendant la gestion d'événements asynchrones complexes beaucoup plus facile et déclarative. Un incontournable pour une utilisation avancée des streams.
    

### Articles et tutoriels (Général)

1. [Programmation asynchrone](https://dart.dev/guides/language/language-tour#asynchrony-support) : Futures, async, await (Guide officiel de Dart) : Bien que ne traitant pas directement des streams, une solide compréhension des `Future`s est un prérequis.
    

### Modèles de gestion d'état associés

1. [Modèle BLoC](https://pub.dev/packages/flutter_bloc) **:** Les streams sont fondamentaux pour le modèle BLoC (Business Logic Component) pour la gestion d'état dans Flutter. Package `flutter_bloc`.
    
2. [Documentation de la bibliothèque Bloc](https://bloclibrary.dev/)
    

### Package HTTP (pour les exemples réseau)

1. [Package `http`](https://pub.dev/packages/http) : Pour effectuer des requêtes HTTP, comme montré dans l'exemple réseau.
    

En explorant ces ressources, vous acquerrez une compréhension encore plus profonde et faisant autorité des streams dans l'écosystème Dart et Flutter.