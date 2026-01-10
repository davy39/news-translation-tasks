---
title: Comment gérer l'état dans Flutter en utilisant le modèle BLoC
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T21:39:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-state-in-flutter-using-the-bloc-pattern-8ed2f1e49a13
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6xT0ZOACZCdy_61tTJ3r1Q.png
tags:
- name: coding
  slug: coding
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment gérer l'état dans Flutter en utilisant le modèle BLoC
seo_desc: 'By Chuks Opia

  Last year, I picked up Flutter and I must say it has been an awesome journey so
  far. Flutter is Google’s awesome framework for crafting high-quality applications
  for Android and iOS.

  As with building almost any application, there’s alwa...'
---

Par Chuks Opia

L'année dernière, j'ai adopté [Flutter](https://flutter.io/) et je dois dire que cela a été un voyage incroyable jusqu'à présent. Flutter est le framework génial de Google pour créer des applications de haute qualité pour Android et iOS.

Comme pour la construction de presque n'importe quelle application, il y a toujours le besoin de gérer l'état de l'application. Il est important que la gestion de l'état soit traitée efficacement, afin d'éviter d'accumuler de la dette technique, surtout à mesure que votre application grandit et devient plus complexe.

Dans Flutter, tous les composants UI sont des widgets. À mesure que vous commencez à composer ces widgets pour créer votre application géniale, vous finirez par avoir un arbre de widgets profondément imbriqués. Ces widgets auront très probablement besoin de partager l'état de l'application entre eux.

Dans cet article, nous verrons comment gérer l'état dans Flutter en utilisant le modèle BLoC.

La gestion de l'état dans Flutter peut être réalisée de plusieurs manières différentes :

**Inherited Widget** : Il permet de propager des données à ses widgets enfants et les widgets sont reconstruits chaque fois qu'il y a un changement dans l'état de l'application. L'inconvénient de l'utilisation de la classe de base InheritedWidget est que votre état est final et cela pose un problème si vous souhaitez muter votre état.

**Scoped Model** : Il s'agit d'un package externe construit sur InheritedWidget et il offre une manière légèrement meilleure d'accéder, de mettre à jour et de muter l'état. Il vous permet de passer facilement un modèle de données d'un widget parent à ses descendants. De plus, il reconstruit également tous les enfants qui utilisent le modèle lorsque le modèle est mis à jour.

Cela peut soulever un problème de performance, selon le nombre de ScopedModelDescendants qu'un modèle a, car ils sont reconstruits lorsqu'il y a une mise à jour.

Ce problème peut être résolu en décomposant le ScopedModel en plusieurs modèles afin d'obtenir des dépendances plus fines. La définition du drapeau `rebuildOnChange` à `false` résout également ce problème, mais cela apporte avec lui la charge cognitive de décider quel widget doit être reconstruit ou non.

**Redux** : Oui ! Comme avec React, il existe un package Redux qui vous aide à créer et à consommer facilement un store Redux dans Flutter. Comme son homologue JavaScript, il y a généralement quelques lignes de code boilerplate et le cycle des _actions_ et _réducteurs_.

#### Entrée du modèle BLoC

Le modèle Business Logic Component (BLoC) est un modèle créé par Google et annoncé lors de [Google I/O '18](https://www.youtube.com/watch?v=RS36gBEp8OI). Le modèle BLoC utilise la programmation réactive pour gérer le flux de données au sein d'une application.

Un BLoC sert d'intermédiaire entre une source de données dans votre application (par exemple, une réponse d'API) et les widgets qui ont besoin des données. Il reçoit des flux d'événements/données de la source, gère toute logique métier requise et publie des flux de changements de données aux widgets qui s'y intéressent.

Un BLoC a deux composants simples : **_Sinks_** et **_Streams_**, tous deux fournis par un **_StreamController_**. Vous ajoutez des flux d'entrée d'événements/données dans un _Sink_ et vous les écoutez en tant que flux de sortie de données via un _Stream_.

Un _StreamController_ peut être accessible via la bibliothèque `'dart:async'` ou en tant que _PublishSubject_, _ReplaySubject_ ou _BehaviourSubject_ via le package `[rxdart](https://pub.dartlang.org/packages/rxdart)`.

Ci-dessous se trouve un extrait de code montrant un BLoC simple :

```dart
import 'dart:async';
// import 'package:rxdart/rxdart.dart'; si vous souhaitez utiliser PublishSubject, ReplaySubject ou BehaviourSubject.
// assurez-vous d'avoir rxdart: comme dépendance dans votre fichier pubspec.yaml pour utiliser l'import ci-dessus


class CounterBloc {
  final counterController = StreamController();  // créer un StreamController ou
  // final counterController = PublishSubject() ou toute autre option rxdart;
  Stream get getCount => counterController.stream; // créer un getter pour notre Stream
  // les contrôleurs de flux rxdart retournent un Observable au lieu d'un Stream
  
  void updateCount() {
    counterController.sink.add(data); // ajouter les données que nous voulons dans le Sink
  }
  
  void dispose() {
    counterController.close(); // fermer notre StreamController pour éviter les fuites de mémoire
  }
}

final bloc = CounterBloc(); // créer une instance du bloc counter

//======= fin du fichier CounterBloc



//======= ailleurs dans notre application
import 'counter_bloc.dart'; // importer le fichier counter bloc ici

@override
void dispose() {
  bloc.dispose(); // appeler la méthode dispose pour fermer notre StreamController
  super.dispose();
}

...
@override
Widget build(BuildContext context) {
  return StreamBuilder( // Envelopper notre widget avec un StreamBuilder
    stream: bloc.getCount, // passer notre getter de Stream ici
    initialData: 0, // fournir une donnée initiale
    builder: (context, snapshot) => Text('${snapshot.data}'), // accéder aux données dans notre Stream ici
  );
}
...
```

Un BLoC est une simple classe Dart. Dans l'extrait de code ci-dessus, nous avons créé une classe `CounterBloc` et dans celle-ci, un `StreamController` que nous avons appelé `counterController`. Nous avons créé un _getter_ pour notre Stream appelé `getCount`, une méthode `updateCount` qui ajoute des données dans notre Sink lorsqu'elle est appelée, et une méthode `dispose` pour fermer notre StreamController.

Pour accéder aux données dans notre Stream, nous avons créé un widget `StreamBuilder` et passé notre Stream à sa propriété `stream` et accédé aux données dans sa fonction `builder`.

#### Implémentation du BLoC

Nous allons convertir l'application d'exemple Flutter par défaut pour utiliser un BLoC. Allons-y et générons une nouvelle application Flutter. Dans votre terminal, exécutez la commande suivante :

```
$ flutter create bloc_counter && cd bloc_counter
```

Ouvrez l'application dans votre éditeur préféré et créez trois fichiers dans le dossier lib : `counter.dart`, `counter_provider.dart` et `counter_bloc.dart`.

Notre `CounterProvider` contiendra un entier et une méthode pour l'incrémenter. Ajoutez le code suivant au fichier `counter_provider.dart` :

```dart
class CounterProvider {
  int count = 0;
  void increaseCount() => count++;
}
```

Ensuite, nous allons implémenter notre BLoC de compteur. Ajoutez le code ci-dessous dans votre fichier `counter_block.dart` :

Dans notre classe `CounterBloc`, nous avons utilisé une partie de notre code d'exemple initial ci-dessus. À la ligne 7, nous avons instancié notre classe `CounterProvider` et dans la méthode `updateCount`, nous avons appelé la méthode du fournisseur pour incrémenter le compte, puis à la ligne 13, nous avons passé le compte à notre Sink.

Remplacez le code dans votre fichier `main.dart` par le code ci-dessous. Dans le code ci-dessous, nous avons simplement supprimé la plupart du code de compteur par défaut, que nous allons déplacer vers notre fichier `counter.dart`. Chaque fois que la méthode `incrementCounter` est appelée, nous appelons la méthode `updateCount` du BLoC qui met à jour le compte et l'ajoute à notre Sink.

Maintenant, notre BLoC reçoit et diffuse des données. Nous pouvons accéder à ces données et les afficher sur un écran via un **_StreamBuilder_**. Nous enveloppons le widget qui a besoin des données dans un widget StreamBuilder et lui passons le flux contenant les données. Ajoutez le code suivant au fichier `counter.dart` :

Dans le code ci-dessus, nous avons un widget stateful. Dans notre classe d'état, à la ligne 13, nous appelons la méthode dispose de notre bloc, afin que le contrôleur de flux puisse être fermé chaque fois que le widget est retiré de l'arbre.

À la ligne 19, nous retournons un widget StreamBuilder et à la ligne 20, nous lui passons le getter pour notre flux ainsi qu'une donnée initiale à la ligne 21. Le StreamBuilder a également un `builder` qui nous donne accès aux données via un `snapshot`. À la ligne 30, nous accédons et affichons les données dans le snapshot.

Allez-y et exécutez l'application en exécutant la commande ci-dessous. Assurez-vous d'avoir un émulateur en cours d'exécution.

```
$ flutter run
```

Avec votre application en cours d'exécution, cliquez sur l'icône plus et regardez le compteur augmenter à chaque clic.

![Image](https://cdn-media-1.freecodecamp.org/images/1*21qeIQKSfZy9nxiJ3bNhqA.gif)
_application de démonstration_

Ensemble, nous avons pu implémenter la forme la plus simple d'un BLoC dans Flutter. Le concept reste le même, quel que soit votre cas d'utilisation.

J'espère que vous avez trouvé cet article utile. N'hésitez pas à le partager pour que d'autres puissent le trouver. Contactez-moi sur Twitter @d[evelopia_](https://twitter.com/developia_) pour des questions ou pour discuter.