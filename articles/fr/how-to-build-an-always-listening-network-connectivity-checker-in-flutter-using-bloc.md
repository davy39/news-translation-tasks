---
title: Comment créer un vérificateur de connectivité réseau à l'écoute permanente
  dans Flutter avec BLoC
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-08-18T13:52:56.888Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-always-listening-network-connectivity-checker-in-flutter-using-bloc
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755525049875/2d9540c1-5a4a-41f4-87c6-59ee15bb99e4.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment créer un vérificateur de connectivité réseau à l'écoute permanente
  dans Flutter avec BLoC
seo_desc: Many mobile applications require a stable internet connection to provide
  a smooth user experience. And as a Flutter developer, you need a robust way to handle
  network state changes, ensuring that your app responds gracefully whether it's connected,
  d...
---

De nombreuses applications mobiles nécessitent une connexion internet stable pour offrir une expérience utilisateur fluide. En tant que développeur Flutter, vous avez besoin d'un moyen robuste pour gérer les changements d'état du réseau, en garantissant que votre application réagisse de manière appropriée, qu'elle soit connectée, déconnectée ou en transition entre deux états.

Cet article vous propose un guide détaillé pour construire un vérificateur de connectivité réseau complet en utilisant une combinaison puissante de packages Flutter modernes et de patrons architecturaux.

Nous exploiterons :

1. `connectivity_plus` : Un package pour vérifier la connectivité réseau de base (par exemple, WiFi, données mobiles, Ethernet).
    
2. `internet_connection_checker` : Un outil plus fiable qui va au-delà d'une simple vérification réseau en effectuant un ping actif vers une URL connue pour confirmer l'accès réel à Internet.
    
3. **Un appel HTTP direct vers une URL de confiance (comme Google)** : En tant que solution de secours, un appel réseau direct peut servir de confirmation finale de la connectivité.
    
4. `rxdart` avec `debounce` : Pour éviter des vérifications réseau excessives et rapides, qui peuvent être inefficaces et épuiser la batterie de l'appareil.
    
5. **Injection de Dépendances avec** `get_it` et `injectable` : Pour une base de code propre, modulaire et testable.
    
6. **Gestion d'état avec BLoC et** `freezed` : Le patron BLoC sépare la logique métier de l'interface utilisateur, et `freezed` simplifie la création d'états et d'événements immuables.
    
7. **Streams** : Pour permettre une approche réactive "à l'écoute permanente" des changements de statut réseau.
    
8. `fluttertoast` : Pour fournir un retour utilisateur clair et non intrusif.
    

Plongeons dans le vif du sujet.

### **Table des matières :**

1. [Prérequis](#heading-prerequis)
    
2. [Étape 1 : Configurer l'Injection de Dépendances avec get\_it et injectable](#heading-etape-1-configurer-l-injection-de-dependances-avec-get-it-et-injectable)
    
3. [Étape 2 : Implémenter le vérificateur de connectivité réseau](#heading-etape-2-implementer-le-verificateur-de-connectivite-reseau)
    
4. [Étape 3 : Créer le BLoC pour la connectivité réseau](#heading-etape-3-creer-le-bloc-pour-la-connectivite-reseau)
    
5. [Étape 4 : Intégrer le BLoC à l'interface utilisateur](#heading-etape-4-integrer-le-bloc-a-l-ui)
    
6. [Étape 5 : Afficher des notifications Toast](#heading-etape-5-afficher-des-notifications-toast)
    
7. [Conclusion](#heading-conclusion)
    
8. [Références](#heading-references)
    

### Prérequis

Avant de commencer, assurez-vous d'avoir une compréhension de base de :

1. **Flutter et Dart** : Les fondamentaux de la création d'applications avec Flutter.
    
2. **Programmation Asynchrone** : Les concepts tels que `async`, `await` et `Future`.
    
3. **Patron BLoC** : Les principes de base du BLoC (Business Logic Component) pour la gestion d'état.
    
4. **Génération de code** : Comment utiliser des packages comme `build_runner` pour générer du code répétitif (boilerplate).
    

## Étape 1 : Configurer l'Injection de Dépendances avec `get_it` et `injectable`

L'Injection de Dépendances (DI) est un patron de conception logicielle qui permet à une classe de recevoir ses dépendances depuis une source externe plutôt que de les créer elle-même. Cela rend votre code plus flexible, réutilisable et plus facile à tester.

Examinons les deux outils que nous utiliserons pour implémenter cela :

1. `get_it` est un "localisateur de services" (service locator) qui agit comme un registre central. Vous enregistrez vos services (dépendances) auprès de `get_it`, et il fournit un moyen de récupérer leur instance unique de n'importe où dans votre application. C'est une alternative simple et efficace aux frameworks de DI plus complexes.
    
2. `injectable` est un package de génération de code qui fonctionne avec `get_it`. En annotant vos classes avec `@injectable`, `@lazySingleton` ou `@module`, `injectable` écrit automatiquement le code répétitif pour enregistrer vos dépendances auprès de `get_it` pour vous, vous épargnant une configuration manuelle.
    

Tout d'abord, créez un nouveau projet Flutter comme ceci :

```bash
flutter create my_injectable_project
cd my_injectable_project
```

Ensuite, ajoutez les packages nécessaires à votre fichier `pubspec.yaml` :

```yaml
dependencies:
  freezed_annotation: ^2.4.1
  rxdart: ^0.28.0
  get_it: ^7.6.7
  injectable: ^2.3.2
  internet_connection_checker: ^1.0.0+1
  connectivity_plus: ^5.0.2
  fluttertoast: ^8.2.4
  flutter_bloc: ^8.1.3
  http: ^0.13.3
  
dev_dependencies:
  build_runner:
  freezed: ^2.4.7
  injectable_generator: ^2.4.1
```

Alors, que se passe-t-il ici ?

* `freezed_annotation` & `freezed` : Utilisés pour créer des classes de données immuables pour les états et événements BLoC.
    
* `rxdart` : Fournit des opérateurs puissants liés aux flux (streams), incluant `debounceTime`, qui est essentiel pour notre vérificateur de connectivité.
    
* `get_it` & `injectable` : Pour l'injection de dépendances.
    
* `internet_connection_checker` & `connectivity_plus` : Les packages de base pour vérifier le statut réseau.
    
* `fluttertoast` : Pour afficher des notifications à l'utilisateur.
    
* `flutter_bloc` : Le package BLoC principal.
    
* `http` : Un package pour effectuer des requêtes HTTP, utilisé pour la vérification de l'URL Google.
    
* `build_runner` : L'outil en ligne de commande qui exécute les générateurs de code.
    
* `injectable_generator` : Le générateur qui fonctionne avec `injectable`.
    

Il est maintenant temps de créer le fichier de configuration de l'injection. Créez un fichier, par exemple `lib/core/dependency_injection/injection.dart`, pour configurer `get_it` et `injectable`.

```dart
import 'package:get_it/get_it.dart';
import 'package:injectable/injectable.dart';
import 'package:my_injectable_project/core/dependency_injection/injection.config.dart';

// The global instance of GetIt
final GetIt getIt = GetIt.instance;

// The annotation @injectableInit tells injectable to generate the init method
@injectableInit
void configureDependencies(String env) => getIt.init(environment: env);
```

* `final GetIt getIt = GetIt.instance;` : Nous créons une instance statique de `GetIt` accessible globalement.
    
* `@injectableInit` : Cette annotation signale à `injectable_generator` que c'est dans ce fichier qu'il doit générer le code d'enregistrement des dépendances.
    
* `void configureDependencies(String env) => getIt.init(environment: env);` : Cette fonction initialise `get_it` et nous permet de le configurer pour différents environnements (ex: 'dev', 'prod').
    

Enfin, nous devons créer un module pour les dépendances. Créez un fichier de module, par exemple `lib/core/dependency_injection/register_module.dart`, pour enregistrer les classes tierces qui n'appartiennent pas à la structure de votre propre projet.

```dart
import 'package:connectivity_plus/connectivity_plus.dart';
import 'package:get_it/get_it.dart';
import 'package:injectable/injectable.dart';
import 'package:internet_connection_checker/internet_connection_checker.dart';
import 'package:my_injectable_project/core/network_info/network_info.dart';
import 'package:my_injectable_project/features/network_info/bloc/network_info_bloc.dart';

// The @module annotation marks this class as a module for injectable
@module
abstract class RegisterModule {
  
  // A @lazySingleton means the instance will be created only when it's first requested
  @lazySingleton
  Connectivity get connectivity => Connectivity();

  @lazySingleton
  InternetConnectionChecker get internetConnectionChecker => InternetConnectionChecker();

  @lazySingleton
  NetworkInfoImpl get networkInfo => NetworkInfoImpl(
        connectivity: connectivity,
        internetConnectionChecker: internetConnectionChecker,
      );

  @lazySingleton
  NetworkInfoBloc get networkInfoBloc => NetworkInfoBloc(
        networkInfo: getIt<NetworkInfo>(),
        connectivity: getIt<Connectivity>(),
      );
}
```

* `@module` : Une annotation spéciale qui marque une classe comme module pour `injectable`. Les modules sont utiles pour enregistrer des classes tierces ou créer des instances de classes nécessitant une configuration complexe.
    
* `@lazySingleton` : Cette annotation indique à `injectable` de créer une instance unique de la classe et de la réutiliser à chaque fois qu'elle est demandée. La partie "lazy" signifie que l'instance n'est créée que lorsqu'elle est nécessaire pour la première fois.
    

## Étape 2 : Implémenter le vérificateur de connectivité réseau

### **Interface et Implémentation**

C'est une bonne pratique de programmer par rapport à une interface plutôt qu'à une implémentation concrète. Cela permet de remplacer facilement les implémentations et simplifie les tests. Ci-dessous, `lib/core/network_info/network_info.dart` est la classe abstraite tandis que `lib/core/network_info/network_info_impl.dart` est l'implémentation. C'est ici que réside la fonctionnalité du flux, que le bloc utilise.

`lib/core/network_info/network_info.dart` :

```dart
// The abstract class defines the contract for our network checker
abstract class NetworkInfo {
  Future<bool> get isConnected;
}
```

`lib/core/network_info/network_info_impl.dart` :

```dart
import 'package:connectivity_plus/connectivity_plus.dart';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:injectable/injectable.dart';
import 'package:internet_connection_checker/internet_connection_checker.dart';
import 'package:my_injectable_project/core/network_info/network_info.dart';

// @LazySingleton(as: NetworkInfo) tells injectable to register this class
// as a lazy singleton, and to provide it when a NetworkInfo is requested.
@LazySingleton(as: NetworkInfo)
class NetworkInfoImpl implements NetworkInfo {
  final Connectivity connectivity;
  final InternetConnectionChecker internetConnectionChecker;

  const NetworkInfoImpl({
    required this.connectivity,
    required this.internetConnectionChecker,
  });

  @override
  Future<bool> get isConnected async {
    try {
      bool isDeviceConnected = false;
      // First, check the connectivity type (WiFi, mobile, etc.)
      final connectivityResult = await connectivity.checkConnectivity();
      debugPrint('Connectivity Result: $connectivityResult');

      if (connectivityResult != ConnectivityResult.none) {
        // If there's a network type, verify actual internet access
        isDeviceConnected = await internetConnectionChecker.hasConnection ||
            await hasInternetConnection();
      }
      debugPrint('Device Connected: $isDeviceConnected');
      return isDeviceConnected;
    } catch (e) {
      debugPrint('Error checking network connection: $e');
      return false;
    }
  }

  // A redundant but useful check with a direct HTTP call
  Future<bool> hasInternetConnection() async {
    try {
      final response = await http.get(Uri.parse('https://www.google.com')).timeout(
        const Duration(seconds: 5),
      );
      if (response.statusCode == 200) {
        return true;
      }
    } catch (e) {
      debugPrint('Error checking internet connection: $e');
    }
    return false;
  }
}
```

* `@LazySingleton(as: NetworkInfo)` : C'est l'annotation clé. Elle enregistre `NetworkInfoImpl` comme un singleton qui implémente l'interface `NetworkInfo`. Lorsque `getIt<NetworkInfo>()` est appelé, une instance de `NetworkInfoImpl` sera fournie.
    
* `connectivity.checkConnectivity()` : Fournit une vérification rapide du type de connexion de l'appareil.
    
* `internetConnectionChecker.hasConnection` : Ce package est plus fiable que la simple vérification du type de réseau, car un appareil peut être "connecté" à un réseau WiFi sans avoir d'accès Internet. `internet_connection_checker` effectue un ping actif sur une série d'adresses pour vérifier.
    
* `hasInternetConnection()` : Une fonction de secours qui effectue une requête HTTP directe vers une URL fiable comme Google. Cela fournit une couche de vérification supplémentaire.
    

## Étape 3 : Créer le BLoC pour la connectivité réseau

Le BLoC gère la logique métier de la vérification du statut réseau et émet les changements d'état appropriés vers l'interface utilisateur.

`lib/features/network_info/bloc/network_info_bloc.dart` :

```dart
import 'dart:async';
import 'package:bloc/bloc.dart';
import 'package:connectivity_plus/connectivity_plus.dart';
import 'package:flutter/foundation.dart';
import 'package:injectable/injectable.dart';
import 'package:my_injectable_project/core/network_info/network_info.dart';
import 'package:rxdart/rxdart.dart';
import 'package:freezed_annotation/freezed_annotation.dart';

part 'network_info_bloc.freezed.dart';
part 'network_info_event.dart';
part 'network_info_state.dart';

// @injectable marks this class to be registered by injectable
@injectable
class NetworkInfoBloc extends Bloc<NetworkInfoEvent, NetworkInfoState> {
  final NetworkInfo networkInfo;
  final Connectivity connectivity;
  late StreamSubscription<List<ConnectivityResult>> connectivitySubscription;

  NetworkInfoBloc({
    required this.networkInfo,
    required this.connectivity,
  }) : super(NetworkInfoState.initial()) {
    // Custom event transformer for debouncing
    EventTransformer<T> debounce<T>(Duration duration) {
      return (events, mapper) => events.debounceTime(duration).flatMap(mapper);
    }

    // The 'on' method maps events to states
    on<CheckNetwork>(
      _onCheckNetwork,
      // Apply the debounce transformer to limit the rate of function calls
      transformer: debounce(
        const Duration(seconds: 1),
      ),
    );

    // Listen to changes from the connectivity_plus package
    connectivitySubscription = connectivity.onConnectivityChanged.listen((connectivityResult) async {
      await Future.delayed(const Duration(seconds: 1)); // Small delay to avoid race conditions
      debugPrint('Connectivity Result after delay: $connectivityResult');
      add(const CheckNetwork());
    });
  }

  // The event handler for CheckNetwork
  Future<void> _onCheckNetwork(
    CheckNetwork event,
    Emitter<NetworkInfoState> emit,
  ) async {
    final isConnected = await networkInfo.isConnected;
    // Only emit a new state if the network status has actually changed
    if (state.networkStatus != isConnected) {
      emit(state.copyWith(networkStatus: isConnected));
    }
    debugPrint(
        'Network Status ==> ${isConnected ? "Data connection is available." : "You are disconnected from the internet."}');
  }

  @override
  Future<void> close() {
    // It's crucial to cancel the stream subscription to prevent memory leaks
    connectivitySubscription.cancel();
    return super.close();
  }
}
```

* `EventTransformer<T> debounce<T>(Duration duration)` : Il s'agit d'un transformateur personnalisé. Il utilise l'opérateur `debounceTime` de `rxdart` pour attendre une durée d'inactivité spécifiée avant de permettre le traitement de l'événement. C'est parfait pour éviter une cascade de vérifications réseau.
    
* `connectivity.onConnectivityChanged.listen(...)` : Cela crée un abonnement à un flux de `ConnectivityResult`. Chaque fois que le statut de connectivité de l'appareil change (par exemple, passage du WiFi aux données mobiles), ce flux émet une nouvelle valeur, qui à son tour déclenche notre événement `CheckNetwork`.
    
* `_onCheckNetwork(...)` : Cette fonction est le cœur de la logique du BLoC. Elle appelle `networkInfo.isConnected` pour obtenir le statut actuel et émet ensuite un nouvel état si le statut a changé.
    
* `close()` : Surcharger cette méthode est vital pour une gestion appropriée des ressources. C'est ici que nous nettoyons notre `StreamSubscription` pour éviter les fuites de mémoire.
    

### **Événements et États**

`freezed` est un outil de génération de code qui facilite la création de classes de données immuables, essentielles pour le patron BLoC.

`lib/features/network_info/bloc/network_info_event.dart` :

```dart
part of 'network_info_bloc.dart';

@freezed
class NetworkInfoEvent with _$NetworkInfoEvent {
  const factory NetworkInfoEvent.checkNetwork() = CheckNetwork;
}
```

* `@freezed` : Cette annotation déclenche `freezed` pour générer le code répétitif de cette classe.
    
* `const factory NetworkInfoEvent.checkNetwork() = CheckNetwork;` : Définit un événement unique pour notre BLoC, qui est `CheckNetwork`.
    

`lib/features/network_info/bloc/network_info_state.dart` :

```dart
part of 'network_info_bloc.dart';

@freezed
class NetworkInfoState with _$NetworkInfoState {
  const factory NetworkInfoState({required bool networkStatus}) = _NetworkInfoState;

  factory NetworkInfoState.initial() => const NetworkInfoState(
    networkStatus: true,
  );
}
```

* `const factory NetworkInfoState(...)` : Définit notre état, qui contient simplement un booléen `networkStatus`.
    
* `factory NetworkInfoState.initial()` : Une usine (factory) utilitaire pour créer l'état initial du BLoC.
    

### **Exécuter le générateur de code**

Pour générer les fichiers `*.freezed.dart` et `*.g.dart`, exécutez la commande suivante dans votre terminal :

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

Cette commande surveillera votre projet pour détecter les changements et régénérera automatiquement les fichiers nécessaires.

## Étape 4 : Intégrer le BLoC à l'interface utilisateur (UI)

Enfin, nous allons connecter notre BLoC à l'UI Flutter pour réagir aux changements d'état.

Dans votre widget principal, par exemple `main.dart`, vous pouvez accéder au BLoC via `getIt`.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:my_injectable_project/core/dependency_injection/injection.dart';
import 'package:my_injectable_project/features/network_info/bloc/network_info_bloc.dart';

void main() {
  // Initialize dependency injection
  configureDependencies('dev');
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    // Provide the BLoC to the widget tree
    return BlocProvider(
      create: (context) => getIt<NetworkInfoBloc>(),
      child: MaterialApp(
        title: 'Network Checker Demo',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: const NetworkCheckerPage(),
      ),
    );
  }
}

class NetworkCheckerPage extends StatefulWidget {
  const NetworkCheckerPage({super.key});

  @override
  State<NetworkCheckerPage> createState() => _NetworkCheckerPageState();
}

class _NetworkCheckerPageState extends State<NetworkCheckerPage> {
  final NetworkInfoBloc networkInfoBloc = getIt<NetworkInfoBloc>();

  @override
  void initState() {
    super.initState();
    // Listen to the BLoC's state stream
    networkInfoBloc.stream.listen((state) {
      if (state.networkStatus) {
        toastInfo(
          msg: "Data connection is available.",
          status: Status.success,
        );
      } else {
        toastInfo(
          msg: "You are disconnected from the internet.",
          status: Status.error,
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Network Connectivity'),
      ),
      body: Center(
        child: BlocBuilder<NetworkInfoBloc, NetworkInfoState>(
          builder: (context, state) {
            return Text(
              state.networkStatus
                  ? 'Connected to the Internet!'
                  : 'Disconnected from the Internet.',
              style: TextStyle(
                fontSize: 20,
                color: state.networkStatus ? Colors.green : Colors.red,
              ),
            );
          },
        ),
      ),
    );
  }
}
```

* `BlocProvider` : Ce widget fournit l'instance de `NetworkInfoBloc` à l'arborescence des widgets, le rendant accessible à n'importe quel widget enfant via `BlocProvider.of<NetworkInfoBloc>(context)`.
    
* `networkInfoBloc.stream.listen(...)` : Dans `initState`, nous nous abonnons au flux d'état du BLoC. Chaque fois qu'un nouvel état est émis (ce qui arrive quand le statut réseau change), notre écouteur est déclenché, et nous pouvons afficher une notification toast.
    
* `BlocBuilder` : Ce widget est utilisé pour reconstruire l'UI en réponse aux changements d'état. Il écoute les nouveaux états du `NetworkInfoBloc` et reconstruit sa fonction `builder`, mettant à jour le widget `Text` pour refléter le statut réseau actuel.
    

## Étape 5 : Afficher des notifications Toast

Le package `fluttertoast` fournit un moyen simple et indépendant de la plateforme pour afficher des messages non intrusifs.

```dart
import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

enum Status { success, error }

void toastInfo({
  required String msg,
  required Status status,
}) {
  Fluttertoast.showToast(
    msg: msg,
    toastLength: Toast.LENGTH_SHORT,
    gravity: ToastGravity.BOTTOM,
    backgroundColor: status == Status.success ? Colors.green : Colors.red,
    textColor: Colors.white,
    fontSize: 16.0,
  );
}
```

Cette fonction utilitaire simplifie le processus d'affichage des toasts en vous permettant de spécifier un message et un statut, lequel détermine la couleur d'arrière-plan.

## Conclusion

En combinant la puissance du patron BLoC, de l'injection de dépendances avec `get_it` et `injectable`, et des bibliothèques de vérification réseau robustes, vous pouvez construire un vérificateur de connectivité réseau hautement fiable et maintenable dans votre application Flutter.

Cette architecture garantit que votre application est réactive aux changements de réseau et offre une séparation claire des préoccupations, rendant votre base de code évolutive et facile à tester.

### Références

Voici quelques références qui soutiennent les concepts et packages utilisés dans cet article :

**Fondamentaux Flutter et Dart :**

1. [**Documentation officielle Flutter**](https://flutter.dev/docs) : Fournit des guides complets sur le développement Flutter, incluant les widgets, la gestion d'état et la programmation asynchrone.
    
2. [**Documentation officielle Dart**](https://dart.dev/guides) : Détaille les fonctionnalités du langage Dart, incluant la programmation asynchrone avec `Future` et `Stream`.
    

**Connectivité et Vérification Réseau :**

1. [Package `connectivity_plus` sur Pub.dev](https://pub.dev/packages/connectivity_plus) : Documentation officielle du plugin `connectivity_plus`, expliquant son utilisation pour vérifier les types de connectivité réseau.
    
2. [Package `internet_connection_checker` sur Flutter Gems](https://fluttergems.dev/packages/internet_connection_checker/) : Détails sur le package `internet_connection_checker`, qui vérifie l'accès réel à Internet en effectuant un ping sur des serveurs externes.
    
3. [Package `http` sur Pub.dev](https://pub.dev/packages/http) : La documentation officielle pour effectuer des requêtes HTTP en Dart et Flutter.
    

**Injection de Dépendances :**

1. [Package `get_it` sur Pub.dev](https://pub.dev/packages/get_it) : La documentation officielle de `get_it`, un localisateur de services simple pour Dart et Flutter.
    
2. [Package `injectable` sur Pub.dev](https://pub.dev/packages/injectable) : La documentation officielle d' `injectable`, un générateur de code pour `get_it` qui simplifie l'enregistrement des dépendances.
    
3. **Gestion d'état (BLoC) :** [Package `flutter_bloc` sur Pub.dev](https://pub.dev/packages/flutter_bloc) – la documentation officielle du package `flutter_bloc`, fournissant des widgets et utilitaires pour implémenter le patron BLoC.
    

**Immuabilité et Génération de Code :**

1. [Package `freezed` sur Pub.dev](https://pub.dev/packages/freezed) : La documentation officielle de `freezed`, un puissant générateur de code pour créer des classes de données immuables.
    
2. [Package `build_runner` sur Pub.dev](https://pub.dev/packages/build_runner) : L'outil utilisé pour exécuter les générateurs de code comme `injectable_generator` et `freezed`.
    

**Programmation Réactive (RxDart) et Streams :**

1. [Package `rxdart` sur Pub.dev](https://pub.dev/packages/rxdart) : Documentation officielle de RxDart, qui étend l'API Stream de Dart avec des opérateurs puissants comme `debounceTime`.
    
2. [**"Classe Stream - bibliothèque dart:async" sur Flutter API Docs**](https://api.flutter.dev/flutter/dart-async/Stream-class.html) : La documentation officielle de Dart pour la classe `Stream`.
    

**Retour Utilisateur :**

1. [Package `fluttertoast` sur Pub.dev](https://pub.dev/packages/fluttertoast) : Documentation officielle du package `fluttertoast` pour afficher des messages toast.