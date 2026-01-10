---
title: Comment utiliser les Streams et les Services pour l'état Flutter
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2024-09-25T09:49:36.117Z'
originalURL: https://freecodecamp.org/news/flutter-streams-and-services
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727130776096/a52147fe-e05a-45e7-af73-9f7a9a8510b5.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser les Streams et les Services pour l'état Flutter
seo_desc: 'Among the many state management architectures in Flutter, combining Dart
  streams with singleton classes (services) is an unpopular yet easy architecture.

  In this article, we’ll explore how to achieve this combination for app-wide state
  in Flutter.

  Ta...'
---

Parmi les nombreuses architectures de gestion d'état dans Flutter, la combinaison des Dart streams avec des classes singleton (services) est une architecture peu commune mais facile à mettre en œuvre.

Dans cet article, nous explorerons comment réaliser cette combinaison pour l'état global de l'application dans Flutter.

## Table des matières

* [Qu'est-ce que l'état global de l'application dans Flutter ?](#heading-quest-ce-que-letat-global-de-lapplication-dans-flutter)
    
* [Qu'est-ce qu'un Stream en Dart ?](#heading-quest-ce-quun-stream-en-dart)
    
* [Comment créer un Stream en Dart](#heading-comment-creer-un-stream-en-dart)
    
* [Comment créer des instances de classes Singleton (ou Services)](#heading-comment-creer-des-instances-de-classes-singleton-ou-services)
    
* [Comment manipuler l'état (streams) au sein des services](#heading-comment-manipuler-letat-streams-au-sein-des-services)
    
* [Comment utiliser les Streams Dart dans les widgets Flutter](https://untitled+.vscode-resource.vscode-cdn.net/Untitled-1#heading-comment-manipuler-letat-streams-au-sein-des-services)
    
* [Comment rendre un service dépendant d'un autre](#heading-comment-rendre-un-service-dependant-dun-autre)
    
* [Comment améliorer les Streams avec les classes et extensions rxdart](#heading-comment-ameliorer-les-streams-avec-les-classes-et-extensions-rxdart)
    
* [Comment mettre à jour l'état dans les rappels AppLifecycle](#heading-comment-mettre-a-jour-letat-dans-les-rappels-applifecycle)
    
* [Flexibi](https://untitled+.vscode-resource.vscode-cdn.net/Untitled-1#heading-comment-ameliorer-les-streams-avec-les-classes-et-extensions-rxdart)[l](#heading-flexibilite-dans-la-gestion-de-letat)[ité dans](https://untitled+.vscode-resource.vscode-cdn.net/Untitled-1#heading-comment-ameliorer-les-streams-avec-les-classes-et-extensions-rxdart) [la gestion de l'état](#heading-flexibilite-dans-la-gestion-de-letat)
    
* [Résumé](#heading-resume)
    

## Qu'est-ce que l'état global de l'application dans Flutter ?

L'état global de l'application comprend toutes les variables qui sont pertinentes pour plusieurs widgets en même temps. Par état global, nous ne voulons pas dire l'état qui est attaché aux `StatefulWidgets`. Ceux-là sont des états éphémères. Les mettre à jour nécessite des appels locaux ou scopés à [setState](https://api.flutter.dev/flutter/widgets/State/setState.html).

Dans Flutter, l'état global a généralement une gestion logique séparée du code UI. Cette logique séparée est appelée une architecture de gestion d'état. Nous avons de nombreuses architectures de gestion d'état avec lesquelles nous pouvons concevoir l'état global. Les exemples incluent [Provider](https://github.com/obumnwabude/write/blob/main/2024/flutter/get-the-link), [InheritedWidget](https://github.com/obumnwabude/write/blob/main/2024/flutter/get-the-link), [Riverpod](https://github.com/obumnwabude/write/blob/main/2024/flutter/get-the-link), [Bloc](https://github.com/obumnwabude/write/blob/main/2024/flutter/get-the-link), [Redux](https://github.com/obumnwabude/write/blob/main/2024/flutter/get-the-link), [Stacked](https://github.com/obumnwabude/write/blob/main/2024/flutter/get-the-link), et ainsi de suite. Chacune de ces architectures de gestion d'état est efficace, bonne et tranchée.

Bien que votre choix d'architecture puisse varier en fonction de différents facteurs, envisagez d'adopter l'architecture suivante dans vos projets. Elle implique l'utilisation de Dart streams et de services (classes singleton) pour suivre l'état de votre application.

## Qu'est-ce qu'un Stream en Dart ?

Un [stream](https://dart.dev/libraries/dart-async#stream) émet continuellement des valeurs. Vous pouvez écouter un stream et recevoir constamment de nouvelles valeurs lorsqu'elles sont émises. Les streams en Dart sont l'équivalent des [`Observable`](https://rxjs.dev/guide/observable) en JavaScript.

En Dart, les streams sont différents des [futures](https://dart.dev/libraries/dart-async#future). La différence est que, alors qu'un future se résout en une seule valeur, un stream émettra continuellement diverses valeurs au cours de sa vie.

Supposons que nous ayons un stream `counter` qui suit un certain décompte entier actuel. Ce décompte peut être incrémenté ou décrémenté. Pour utiliser les valeurs émises par ce stream `counter`, vous écoutez le `counter`. Écouter implique d'appeler la méthode `.listen` sur le stream et de gérer la valeur émise.

```dart
counter.listen((int value) => print('Reçu $value.'));
```

## Comment créer un Stream en Dart

La classe [`Stream`](https://dart.dev/libraries/dart-async#stream) est livrée avec plusieurs constructeurs factory. Ils vous permettent de créer divers streams à des fins diverses. Ils incluent :

* `Stream.empty`
    
* `Stream.value`
    
* `Stream.error`
    
* `Stream.fromFuture`
    
* `Stream.fromFutures`
    
* `Stream.fromIterable`
    
* `Stream.multi`
    
* `Stream.periodic`
    
* `Stream.eventTransformed`
    

Chaque constructeur sert un objectif spécifique comme son nom l'indique.

Une autre technique de création d'un `Stream` consiste à l'obtenir à partir d'un `StreamController`. Vous devrez créer le `StreamController` vous-même. L'avantage de faire cela est que le contrôleur vous permet d'*ajouter* des valeurs. Lorsque vous ajoutez des valeurs au contrôleur, elles sont émises aux écouteurs de son stream.

```dart
import 'dart:async';

void main() {
  final counterCtrl = StreamController<int>();
  counterCtrl.stream.listen(print);
  counterCtrl.add(1); // affiche 1
}
```

Le problème avec le `StreamController` par défaut de la bibliothèque `dart:async` est qu'il n'autorise qu'un seul écouteur. Il est Unicast. Si vous tentez d'attacher un autre écouteur à ce stream obtenu via `StreamController`, il lancera une erreur "bad state".

Ce problème est résolu par la classe `BehaviorSubject` du package [`rxdart`](https://pub.dev/packages/rxdart). Techniquement, `BehaviorSubject` est un `StreamController`. La différence est qu'il possède plus de fonctionnalités telles que :

1. Permet plusieurs écouteurs (très important).
    
2. Met en cache la dernière valeur ou erreur émise.
    
3. Émet la dernière valeur/erreur mise en cache à un nouvel écouteur dès qu'il s'abonne.
    
4. Vous permet de lire de manière synchrone la valeur actuelle (ou la dernière émise).
    
5. Vous permet d'y ajouter des valeurs même s'il n'a pas encore d'écouteur (le `StreamController` par défaut ne le permet pas).
    

Le package `rxdart` étend les capacités des Dart streams. Par exemple, il vous fournit `BehaviorSubject`. De plus, il expose des classes et des extensions qui permettent plus de manipulations de streams. Pour utiliser le package `rxdart`, ajoutez-le aux dépendances de votre projet depuis pub en utilisant la commande suivante :

```bash
flutter pub add rxdart
```

Ensuite, importez-le dans les fichiers Dart de votre projet. À partir de là, vous pouvez créer un `BehaviorSubject` (`StreamController` plus robuste) qui peut autoriser plusieurs écouteurs tout en vous permettant de les contrôler (en ajoutant des valeurs aux streams).

```dart
import 'package:rxdart/rxdart.dart';

void main() {
  // Créer un BehaviorSubject.
  //
  // En plus de créer le BehaviorSubject, nous pouvons également  
  // ajouter immédiatement une valeur en utilisant l'opérateur en cascade de Dart.
  final counterBS = BehaviorSubject<int>()..add(0);

  counterBS.stream.listen(print); // affiche 0
  counterBS.stream.listen(print); // affiche 0
  counterBS.add(1); // affiche 1 deux fois
}
```

Maintenant que nous pouvons créer des streams (et les écouter), nous avons besoin que ces mêmes streams soient disponibles pour chaque partie de nos applications Flutter.

Pour garantir que c'est la même instance de streams à laquelle les différentes parties de nos applications Flutter accèdent, nous pouvons exposer les streams à partir d'instances de classes singleton que nous créons dans le projet.

## Comment créer des instances de classes Singleton (ou Services)

Quand quelque chose est appelé un singleton, cela signifie qu'il n'en existe qu'un seul. Par exemple, nous pouvons dire que le soleil est une étoile singleton car nous n'avons qu'un seul soleil.

En programmation, nous utilisons un singleton lorsque nous avons besoin de la même copie d'un objet partout. Déjà, les propriétés [`static`](https://en.m.wikipedia.org/wiki/Static_variable) d'une classe sont des singletons pour chaque instance de cette classe. Lorsque vous déclarez un champ ou une méthode comme `static`, vous dites au moteur d'exécution de toujours réutiliser le même élément statique.

Ceci explique pourquoi les propriétés `static` sont utilisées comme constantes. C'est une autre raison pour laquelle nous les utilisons sans instancier un objet. De plus, dans Flutter, nous utilisons conventionnellement des propriétés statiques comme moyen d'obtenir des instances nouvelles ou existantes d'une classe. Par exemple, de nombreuses classes Flutter (`MediaQuery`, `Navigator`, `ThemeData`, et ainsi de suite) ont une méthode statique `.of` pour obtenir leurs instances.

Dans cette architecture de streams et services, nous n'exposons qu'une seule instance d'une classe avec le mot-clé `static`. En même temps, nous cachons le constructeur de cette classe. Cacher le constructeur garantit qu'aucun autre code Dart en dehors du fichier Dart ne peut créer une autre instance de la même classe. Cela maintient l'instance en tant que singleton.

En suivant les conventions courantes, nous pouvons appeler cette classe un service. Tout autre fichier Dart dans le projet peut écouter le ou les streams exposés depuis la classe de service et recevoir toujours les valeurs mises à jour qui lui sont émises.

Les services ici sont des détenteurs de l'état global de l'application. Chaque service est un conteneur logique de fonctionnalités liées. Dans n'importe quelle autre partie du code, à travers ces services, nous pouvons accéder aux variables d'état global (dans notre cas, les streams). Dans une application en production, nous pourrions avoir un service d'authentification, un autre pour les notifications, un autre pour les fichiers, et ainsi de suite.

Pour avoir un service disponible globalement (classe singleton) avec un stream à l'intérieur :

1. Créez une classe de service.
    
2. Créez un constructeur privé (afin qu'aucun autre code Dart en dehors de la classe ne puisse l'instancier).
    
3. Créez une instance privée statique de cette même classe.
    
4. Exposez cette instance privée en tant que singleton.
    
5. Créez un `BehaviorSubject` privé dans cette classe.
    
6. Exposez le stream du `BehaviorSubject` en tant que getter statique public de la classe.
    

```dart
/* Dans le fichier counter_service.dart */
import 'package:rxdart/rxdart.dart';

// 1. Créer une classe
// 
// Le nom de la classe avec "Service" ajouté indique 
// qu'il s'agit d'un objet d'état global.
class CounterService {
  // 2. Créer un constructeur privé.
  //
  // Ce constructeur "juste-underscore" fonctionne. Si nous le voulons, nous pourrions  
  // toujours ajouter un nom après l'underscore. L'essentiel est que 
  // l'underscore rend le constructeur privé.
  CounterService._();
 
  // 3. Créer une instance privée statique.
  // 
  // Préfixer un underscore (_) au nom de la variable la rend privée.
  // En étant privée, aucun autre code Dart en dehors de ce fichier ne peut y 
  // accéder directement.
  static final _instance = CounterService._();

  // 4. Exposer cette instance privée comme le singleton.
  static CounterService get instance => _instance;

  // 5. Créer un BehaviorSubject privé.
  final _counterBS = BehaviorSubject<int>()..add(0);
  
  // 6. Exposer le Stream du BehaviorSubject.
  Stream<int> get countStream => _counterBS.stream;

  // De plus, si nécessaire, exposer la valeur actuelle du BehaviorSubject via un getter.
  int get currentCount => _counterBS.value;
}

/* Dans n'importe quel autre fichier Dart du projet */
import 'counter_service.dart'

// Attacher un écouteur au stream
CounterService.instance.countStream.listen((count) {
   // Utilisez le count comme vous le souhaitez. Le code que vous écrivez dans ce 
   // bloc d'écouteur sera appelé chaque fois que count est 
   // mis à jour/ré-émis.
   
   print(count); // affiche 0
});

// Lire la valeur actuelle du stream une seule fois sans s'abonner
print(CounterService.instance.currentCount); // affiche 0
```

## Comment manipuler l'état (Streams) au sein des services

La plupart du temps, chaque service aura plusieurs streams. C'est prévisible, étant donné que, pour une fonctionnalité d'état logique donnée, il y aurait plusieurs variables l'affectant. Par conséquent, si nécessaire, n'hésitez pas à déclarer plusieurs `BehaviorSubject` (tout en exposant leurs streams) au sein de la même classe de service.

Pour chaque stream, vous voulez contrôler ses données. C'est pourquoi nous utilisons `BehaviorSubject`, afin de pouvoir lui ajouter des valeurs lorsqu'il est nécessaire de mettre à jour l'état.

Différents événements (qu'ils proviennent de l'utilisateur ou de vos serveurs) peuvent être la cause de telles mises à jour d'état. Vous voulez déclencher des mises à jour d'état (ou ajouter des valeurs aux streams) chaque fois que ces événements se produisent.

Vous pourriez toujours sonder votre backend et émettre des changements vers vos streams si un événement se produit. Vous pourriez également émettre des valeurs basées sur des changements dans d'autres services. De plus, si nécessaire, les services devraient également exposer des méthodes pertinentes qui mettront à jour leurs streams. À leur tour, d'autres parties de l'application peuvent appeler ces méthodes et déclencher des changements. L'avantage évident est que chaque écouteur recevra respectivement la nouvelle valeur du stream qui lui est émise.

```dart
/* Dans le fichier counter_service.dart */
import 'package:rxdart/rxdart.dart';

class CounterService {
  CounterService._();
  static final _instance = CounterService._();
  static CounterService get instance => _instance;

  final _counterBS = BehaviorSubject<int>()..add(0);
  Stream<int> get countStream => _counterBS.stream;
  int get currentCount => _counterBS.value;

  // Incrémenter/Décrémenter le compteur déclenchera des mises à jour d'état.
  void incrementCount() => _counterBS.add(currentCount + 1);
  void decrementCount() => _counterBS.add(currentCount - 1);
}

/* Dans un autre fichier Dart du projet */
import 'counter_service.dart'

void main() {
  final service = CounterService.instance;
  service.countStream.listen(print); // affiche 0
  service.incrementCount(); // provoque l'affichage de 1
  service.decrementCount(); // provoque l'affichage de 0
}
```

Pour un exemple plus concret, disons que nous avons un `AuthenticationService`. Il déclare un `_userBS` et expose un stream `currentUser` de type `Stream<User?>`, l'utilisateur sera valide s'il est authentifié ou `null` s'il est déconnecté. Ce service d'authentification aura naturellement `signIn` et `signOut` qui peuvent tous deux ajouter des valeurs à `_userBS`. Les écrans d'inscription et de connexion peuvent chacun appeler `signIn` tandis que les boutons "changer de compte" et "se déconnecter" peuvent chacun appeler `signOut`.

```dart
/* Dans user.dart */
// Un utilisateur simple avec seulement un email et un nom d'utilisateur pour les besoins de la démo. 
// Votre modèle/schéma User aurait plus de propriétés.
class User {
  final String email;
  final String username;

  const User(this.email, this.username);
}

/* Dans authentication_service.dart */
import 'package:rxdart/rxdart.dart';
import 'user.dart';

class AuthenticationService {
   AuthenticationService._();
   static final _instance = AuthenticationService._();
   static AuthenticationService instance => _instance;

   // User BehaviorSubject et son stream.
   final _userBS = BehaviorSubject<User?>()..add(null);
   Stream<User?> get currentUser => _userBS.stream;

   // signIn ajoute un nouvel User au stream.
   void signIn(String email, String username) {
     _userBS.add(User(email, username));
   }

   // signOut définit le currentUser comme null
   void signOut() => _userBS.add(null);

   // Les méthodes signIn et signOut qui modifient l'état pourraient effectuer d'autres 
   // actions comme l'enregistrement d'analyses ou la navigation.
   // De plus, elles pourraient faire de la validation ou exécuter des vérifications avant
   // d'émettre des valeurs. L'idée est que vous vous sentiez à l'aise avec
   // la mise à jour des valeurs de BehaviorSubject (donc l'émission de streams) 
   // à partir de méthodes contrôlées au sein du service.
}
```

Un autre point de manipulation de l'état se situe lors de l'initialisation des services. Certains streams peuvent justifier un initialiseur asynchrone avant de pouvoir être utilisés. Vous pouvez définir des méthodes `init` dans les services et appeler ces méthodes avant d'appeler [`runApp`](https://api.flutter.dev/flutter/widgets/runApp.html) dans la méthode principale (main) au sommet de Flutter.

Les méthodes `init` peuvent être des valeurs sauvegardées dans le "localStorage" lors des exécutions précédentes de l'application. Elles peuvent effectuer des appels d'API, vérifier des permissions ou configurer des écouteurs [EventChannel](https://api.flutter.dev/flutter/services/EventChannel-class.html). Lorsque vous les appelez avant `runApp`, assurez-vous d'appeler `ensureInitialized()` de [`WidgetsFlutterBinding`](https://api.flutter.dev/flutter/widgets/WidgetsFlutterBinding-class.html) avant d'initialiser les services. C'est particulièrement obligatoire si l'un des codes `init` du service accède à un [`PlatformChannel`](https://docs.flutter.dev/platform-integration/platform-channels).

```dart
/* authentication_service.dart */
// ... imports
class AuthenticationService {
  // ... autre code

  // initialiser le service et effectuer d'autres configurations si nécessaire.
  Future<void> init() async => _userBS.add(await _fetchSavedUser());
}

/* main.dart */
import 'package:flutter/material.dart';
import 'authentication_service.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
   
  // Initialiser le service pour s'assurer qu'il est opérationnel avant
  // de lancer l'application. Vous pourriez également initialiser d'autres services ici.
  // Ne faites cela que s'ils effectuent des exécutions asynchrones,
  // et que les résultats doivent être prêts avant le lancement de l'UI.
  await AuthenticationService.instance.init();

  runApp(const MyApp());
}
```

## Comment utiliser les Streams Dart dans les widgets Flutter

Flutter est livré avec un widget [StreamBuilder](https://api.flutter.dev/flutter/widgets/StreamBuilder-class.html) intégré. Il prend un stream et une fonction builder. Cette fonction builder recevra un `BuildContext` et des données snapshot sur le stream. La fonction doit toujours retourner un widget.

Lors de la construction des interfaces utilisateur, vous pouvez envelopper les parties de l'UI qui dépendent de ou affichent des valeurs émises par des streams globaux dans des `StreamBuilders`. De cette façon, une fois que le stream émet une valeur, Flutter reconstruit automatiquement les widgets enfants des `StreamBuilders` avec les dernières valeurs.

```dart
import 'package:flutter/material.dart';
import 'counter_service.dart';

class CounterWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return StreamBuilder<int>(
      stream: CounterService.instance.countStream, // Le stream à écouter
      initialData: CounterService.instance.currentCount, // Valeur initiale
      builder: (context, snapshot) {
        // Vérifier si le snapshot contient des données
        if (snapshot.hasData) {
          return Text('Compteur : ${snapshot.data}', style: TextStyle(fontSize: 24));
        } else {
          // Gérer tout état d'erreur ou vide
          return Text('Chargement...', style: TextStyle(fontSize: 24));
        }
      },
    );
  }
}
```

Les `StreamBuilders` sont d'excellents outils. Cependant, il y a des moments où il n'est pas approprié de les utiliser. Par exemple :

* Lorsqu'un écran d'interface utilisateur donné dépend de plusieurs streams qui sont exposés par le même service ou des services différents.
    
* Lorsque vous souhaitez effectuer un calcul sur les valeurs du stream avant de les rendre dans l'UI.
    

Dans ces cas, nous devons écouter les streams séparément dans `initState`, définir les valeurs via des appels `setState` (pour mettre à jour l'UI) et libérer les `StreamSubscriptions` dans la méthode `dispose` du StatefulWidget.

Écouter les streams séparément nous permet d'effectuer toutes les personnalisations ou de fusionner les données lorsque les streams émettent des valeurs. De plus, nous rendons notre code UI plus facile à lire étant donné que nous avons retiré le code lié à la logique de la méthode build. Cependant, nous ne devrions faire cela que lorsque c'est nécessaire : les `StreamBuilders` seront, la plupart du temps, suffisants.

```dart
import 'dart:async';

import 'package:flutter/material.dart';
import 'counter_service.dart';

class CounterStatefulWidget extends StatefulWidget {
  const CounterStatefulWidget({super.key});

  @override
  _CounterStatefulWidgetState createState() => _CounterStatefulWidgetState();
}

class _CounterStatefulWidgetState extends State<CounterStatefulWidget> {
  late StreamSubscription<int> counterSub;
  int count = CounterService.instance.currentCount;

  @override
  void initState() {
    super.initState();

    // Initialiser l'abonnement au stream
    counterSub = CounterService.instance.countStream.listen((count) {
      // Mettre à jour l'état lors d'une nouvelle valeur du stream
      setState(() => this.count = count);
    });
  }

  @override
  void dispose() {
    // Annuler l'abonnement au stream pour éviter les fuites de mémoire
    counterSub.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Text('Compteur : $count', style: TextStyle(fontSize: 24));
  }
}
```

L'exemple ci-dessus démontre l'écoute et l'annulation depuis l'extérieur de la méthode build. Cet exemple n'est pas un bon cas d'utilisation pour le faire.

## Comment rendre un service dépendant d'un autre

Dans les applications complexes, il est courant d'avoir des services qui dépendent les uns des autres. Le service dépendant peut écouter les streams et appeler les méthodes du service indépendant. De plus, le service dépendant peut importer et référencer le service indépendant tout comme nous l'avons fait dans le code UI ci-dessus.

Par exemple, si nous construisons une application de commerce électronique, un `CartService` peut dépendre d'un `AuthenticationService` pour récupérer les paniers et les commandes de l'utilisateur connecté. Si l'utilisateur se déconnecte, un certain stream `currentUser` dans l' `AuthenticationService` émettra `null`. À son tour, le `CartService` à l'écoute mettra à jour le panier. Lorsqu'un nouvel utilisateur se connectera ensuite, il récupérera le nouveau panier.

```dart
import 'package:rxdart/rxdart.dart';
import 'authentication_service.dart';

// Modèle Item représentant un article du panier.
class CartItem {
  final String name;
  final int quantity;

  const CartItem(this.name, this.quantity);
}

// CartService pour gérer le panier d'achat de l'utilisateur.
class CartService {
  // ...

  // Dépendance vis-à-vis d'AuthenticationService.
  final _auth = AuthenticationService.instance;

  final _cartItemsBS = BehaviorSubject<List<CartItem>>();
  Stream<List<CartItem>> get cartStream => _cartItemsBS.stream;

  CartService() {
    // Écouter le stream currentUser dans AuthenticationService.
    _auth.currentUserStream.listen((user) {
      if (user == null) {
        // Utilisateur déconnecté, vider le panier.
        _clearCart();
      } else {
        // Utilisateur connecté, récupérer son panier.
        _fetchCartForUser(user.email);
      }
    });
  }

  // Méthode pour vider le panier (appelée lors de la déconnexion).
  void _clearCart() {
    _cartItemsBS.add([]);  // Émettre une liste vide pour vider le panier.
  }

  // Méthode pour récupérer le panier d'un utilisateur connecté (simulé).
  Future<void> _fetchCartForUser(String email) async {
    // ...
  }
}
```

Faites attention aux problèmes de [dépendance circulaire](https://en.wikipedia.org/wiki/Circular_dependency) lorsque vos services dépendent les uns des autres. Une dépendance circulaire se produit lorsque deux services inter-dépendent l'un de l'autre. Ce scénario est généralement inévitable à mesure que la logique métier se développe.

Face à cela, déplacez l'état qu'ils veulent partager vers un service différent et importez ce nouveau service dans les autres. Une autre solution consiste à utiliser les mots-clés `late` de Dart lors de l'importation des services interdépendants. Vous pouvez également trouver des moyens de garantir que l'accès aux variables se fait au sein de fonctions et non lors d'une déclaration de haut niveau.

## Comment améliorer les Streams avec les classes et extensions rxdart

En plus d'avoir des méthodes de service qui mettent à jour les streams, vous pouvez également avoir des streams nouveaux ou améliorés basés sur des streams existants, en utilisant les classes et extensions `rxdart`.

Un exemple de classe est [`CombineLatestStream`](https://pub.dev/documentation/rxdart/latest/rx/CombineLatestStream-class.html). Elle prend plusieurs streams et une fonction de combinaison pour retourner un nouveau stream qui ré-émettra les dernières valeurs combinées des streams sources (selon le combinateur optionnel).

```dart
import 'package:rxdart/rxdart.dart';

class MultipliedCounterService {
  // ... 

  final _counterBS = BehaviorSubject<int>()..add(0);
  final _multiplierBS = BehaviorSubject<int>()..add(2);

  Stream<int> get combinedStream => CombineLatestStream(
        [_counterBS.stream, _multiplierBS.stream],
        (values) => values[0] * values[1],
      );

  void incrementCounter() => _counterBS.add(_counterBS.value + 1);
  void changeMultiplier(int mul) => _multiplierBS.add(mul);
}
```

Une autre bonne méthode de stream est [`debounceTime`](https://pub.dev/documentation/rxdart/latest/rx/DebounceExtensions/debounceTime.html). C'est une extension de stream utile pour ignorer les émissions fréquentes et traiter la dernière valeur après un délai (comme lors d'une recherche). Une émission ne se produira qu'après la durée définie et lorsqu'il n'y a aucune autre émission entre-temps. Cela aide à éviter les appels d'API excessifs en attendant une période d'inactivité avant d'émettre la dernière valeur.

```dart
import 'package:rxdart/rxdart.dart';

class SearchService {
  // ... 

  final _searchQueryBS = BehaviorSubject<String>()..add('');

  // Stream avec antirebond (debouncing) pour n'émettre des valeurs qu'après un
  // délai de 300ms. Par exemple : les frappes au clavier seront regroupées.
  Stream<String> get debouncedSearchQueryStream =>
      _searchQueryBS.stream.debounceTime(Duration(milliseconds: 300));

  void updateSearchQuery(String query) => _searchQueryBS.add(query);
}
```

Le package `rxdart` fournit plus de classes et d'extensions de stream qui vous seront utiles, même si vous n'utilisez pas cette architecture. Consultez-les plus tard.

## Comment mettre à jour l'état dans les rappels AppLifecycle

Lorsqu'un utilisateur réduit ou quitte votre application et revient, certains éléments externes sur lesquels vous comptez pour les données peuvent avoir changé.

Par exemple, lorsque vous demandez à un utilisateur d'accorder des permissions, le système d'exploitation affiche une fenêtre contextuelle (popup) par-dessus votre application. Par programmation, la popup affichée a fait perdre le focus à votre application ou l'a mise en arrière-plan. Lorsque la popup disparaît, votre application reprend le focus et vous devez détecter si vous avez obtenu les permissions.

De même, si vous gérez le contenu d'un répertoire spécifique de l'explorateur de fichiers au sein de votre application (comme de la musique convertie, des documents cryptés, des journaux d'appels, etc.), lorsque votre application passe en arrière-plan, l'utilisateur peut avoir apporté des modifications à ce répertoire, qu'il vaut la peine de détecter lorsque l'utilisateur revient.

Parfois, vous voudrez savoir quand l'utilisateur revient dans votre application à des fins d'authentification, comme mettre fin à une session s'il s'est absenté trop longtemps et qu'il doit se ré-authentifier. D'autres fois, vous voudrez rafraîchir le contenu de l'application pour fidéliser l'utilisateur, comme vous le feriez si vous construisiez une application de réseau social.

Dans tous ces cas, nous avons besoin d'un moyen de savoir par programmation quand notre application revient au focus de l'utilisateur après que celui-ci l'ait quittée. Heureusement, Flutter nous fournit [`AppLifecycleState`](https://api.flutter.dev/flutter/dart-ui/AppLifecycleState.html) et un moyen de réagir aux changements de ces états.

Le cycle de vie d'une application fait référence à ses différents états pendant qu'elle est en cours d'exécution. Dans Flutter, `AppLifecycleState` inclut detached, resumed, inactive, hidden et paused. Dans les cas d'exemple ci-dessus, chaque fois que l'utilisateur revient sur l'application, l'état du cycle de vie de l'application devient `AppLifecycleState.resumed`.

Nous pouvons réagir aux changements de cycle de vie et appeler nos méthodes de service lorsqu'un état particulier se produit. Pour écouter les changements de cycle de vie, votre classe de service doit ajouter le mixin `WidgetsBindingObserver` à sa déclaration. Ensuite, vous devez surcharger `didChangeAppLifecycleState` avec un rappel (callback). Ce rappel doit gérer les états qui l'intéressent.

```dart
import 'package:flutter/material.dart';

class PermissionService with WidgetsBindingObserver {
  // ...

  Future<void> checkPermissions() async {
    // ... 
  }

  @override
  Future<void> didChangeAppLifecycleState(AppLifecycleState state) async {
    if (state == AppLifecycleState.resumed) {
      await checkPermissions();
    }
    // vous pouvez également vérifier les autres états et les gérer comme prévu.
  }
}
```

## Flexibilité dans la gestion de l'état

Il existe de multiples choix et variantes pour la gestion de l'état dans la communauté Flutter. La plupart du temps, les mêmes fonctionnalités peuvent toujours être construites avec n'importe quelle gestion d'état de votre choix.

Gardez cela à l'esprit et soyez flexible avec les architectures de gestion d'état dans Flutter. Ce ne sont pas des règles immuables. Adaptez-les et jouez avec elles pour répondre aux cas uniques de votre application car il n'y a pas de solution unique ici.

Vous pouvez expérimenter avec les streams et les services. Vous pourriez utiliser [getIt](https://pub.dev/packages/get_it) pour obtenir des singletons. `getIt` vous permet également d'obtenir des singletons scopés, c'est-à-dire des singletons attachés à un navigateur ou à une partie logique de fonctionnalités (au sein d'une recherche par exemple).

Vous pouvez également combiner cette architecture avec d'autres. Comme déclarer et gérer des streams comme expliqué ici mais au sein de providers ou de cubits. Ou intégrer des fonctionnalités d'autres architectures dans les services que vous déclarez comme décrit dans cet article.

Assurez-vous simplement de savoir ce que vous faites et de comprendre comment coordonner les variables représentant l'état de l'application. De préférence, documentez votre choix d'architectures dans votre base de code pour référence future.

## Résumé

En résumé, nous avons exploré une architecture efficace pour gérer l'état global de l'application dans Flutter en utilisant les Dart streams et des services singleton.

Nous avons également vu comment manipuler les streams, comment les utiliser dans le code UI, rendre les services dépendants les uns des autres, améliorer les streams en utilisant `rxdart` et gérer les changements de cycle de vie de l'application.

N'oubliez pas que la gestion de l'état dans Flutter est flexible et qu'aucune solution unique ne convient à tous. Adaptez votre choix d'architecture de gestion d'état pour répondre aux besoins spécifiques de votre application.