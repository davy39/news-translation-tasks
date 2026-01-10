---
title: Comment utiliser le Provider Pattern dans Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-12T13:17:49.000Z'
originalURL: https://freecodecamp.org/news/provider-pattern-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/flutter-provider-pattern.png
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment utiliser le Provider Pattern dans Flutter
seo_desc: 'By Ayusch Jain

  In this post we''ll take a look at the provider pattern in Flutter. Some other patterns,
  such as BLoC Architecture, use the provider pattern internally. But the provider
  pattern is far easier to learn and has much less boilerplate code....'
---

Par Ayusch Jain

Dans cet article, nous allons examiner le Provider Pattern dans Flutter. Certains autres patterns, comme l'architecture BLoC, utilisent le Provider Pattern en interne. Mais le Provider Pattern est bien plus facile à apprendre et nécessite beaucoup moins de code boilerplate.

Dans cet article, nous allons prendre l'application Counter par défaut fournie par Flutter et la refactoriser pour utiliser le Provider Pattern.

Si vous voulez savoir ce que l'équipe Flutter de Google dit à propos du Provider Pattern, consultez [cette conférence de 2019](https://www.youtube.com/watch?v=d_m5csmrf7I).

Si vous voulez en savoir plus sur [l'architecture BLoC, consultez-la ici.](https://ayusch.com/understanding-bloc-architecture-in-flutter/)

# Installation

Créez un nouveau projet Flutter et nommez-le comme vous le souhaitez.

Tout d'abord, nous devons supprimer tous les commentaires pour avoir une base propre avec laquelle travailler :

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}

```

Maintenant, ajoutez la dépendance pour le Provider Pattern dans le fichier `pubspec.yaml`. Au moment de la rédaction, la dernière version est 4.1.2.

Voici à quoi ressemble votre fichier `pubspec.yaml` maintenant :

```dart
name: provider_pattern_explained
description: A new Flutter project.

publish_to: 'none' 

version: 1.0.0+1

environment:
  sdk: ">=2.7.0 <3.0.0"

dependencies:
  flutter:
    sdk: flutter
  provider: ^4.1.2

  cupertino_icons: ^0.1.3

dev_dependencies:
  flutter_test:
    sdk: flutter

flutter:
  uses-material-design: true

```

L'application par défaut est essentiellement un widget stateful qui se reconstruit chaque fois que vous cliquez sur le `FloatingActionButton` (qui appelle `setState()`).

Mais maintenant, nous allons le convertir en un widget stateless.

# Création du Provider

Allons-y et créons notre provider. Ce sera la source unique de vérité pour notre application. C'est ici que nous stockerons notre état, qui dans ce cas est le compteur actuel.

Créez une classe nommée `Counter` et ajoutez la variable `count` :

```dart
import 'package:flutter/material.dart';

class Counter {
  var _count = 0;
}

```

Pour la convertir en une classe provider, étendez `ChangeNotifier` du package `material.dart`. Cela nous fournit la méthode `notifyListeners()`, et notifiera tous les listeners chaque fois que nous changerons une valeur.

Maintenant, ajoutez une méthode pour incrémenter le compteur :

```dart
import 'package:flutter/material.dart';

class Counter extends ChangeNotifier {
  var _count = 0;
  void incrementCounter() {
    _count += 1;
  }
}

```

À la fin de cette méthode, nous appellerons `notifyListeners()`. Cela déclenchera un changement dans toute l'application pour les widgets qui l'écoutent.

C'est la beauté du Provider Pattern dans Flutter – vous n'avez pas à vous soucier de la diffusion manuelle vers les streams.

Enfin, créez un getter pour retourner la valeur du compteur. Nous l'utiliserons pour afficher la dernière valeur :

```dart
import 'package:flutter/material.dart';

class Counter extends ChangeNotifier {
  var _count = 0;
  int get getCounter {
    return _count;
  }

  void incrementCounter() {
    _count += 1;
    notifyListeners();
  }
}

```

## **Écoute des clics sur les boutons**

Maintenant que nous avons configuré le provider, nous pouvons l'utiliser dans notre widget principal.

Tout d'abord, convertissons `MyHomePage` en un widget stateless au lieu d'un widget stateful. Nous devrons supprimer l'appel à `setState()` car il n'est disponible que dans un `StatefulWidget` :

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatelessWidget {
  int _counter = 0;
  final String title;
  MyHomePage({this.title});
  void _incrementCounter() {}
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}

```

Avec cela fait, nous pouvons maintenant utiliser le Provider Pattern dans Flutter pour définir et obtenir la valeur du compteur. À chaque clic sur le bouton, nous devons incrémenter la valeur du compteur de 1.

Donc, dans la méthode `_incrementCounter` (qui est appelée lorsque le bouton est pressé), ajoutez cette ligne :

```dart
Provider.of<Counter>(context, listen: false).incrementCounter();
```

Ce qui se passe ici, c'est que vous avez demandé à Flutter de remonter dans l'_arbre des widgets_ et de trouver le premier endroit où `Counter` est fourni. (Je vous dirai comment le fournir dans la section suivante.) C'est ce que fait `Provider.of()`.

Les génériques (valeurs à l'intérieur des crochets **<>**) indiquent à Flutter quel type de provider rechercher. Ensuite, Flutter remonte à travers l'arbre des widgets jusqu'à ce qu'il trouve la valeur fournie. Si la valeur n'est fournie nulle part, une exception est levée.

Enfin, une fois que vous avez obtenu le provider, vous pouvez appeler n'importe quelle méthode sur celui-ci. Ici, nous appelons notre méthode `incrementCounter`.

Mais nous avons aussi besoin d'un contexte, donc nous acceptons le contexte comme argument et modifions la méthode `onPressed` pour passer le contexte également :

```dart
void _incrementCounter(BuildContext context) {
  Provider.of<Counter>(context, listen: false).incrementCounter();
}

```

Remarque : Nous avons défini listen à false car nous n'avons pas besoin d'écouter des valeurs ici. Nous envoyons simplement une action à effectuer.

# Fournir le Provider

Le Provider Pattern dans Flutter recherchera la dernière valeur fournie. Le diagramme ci-dessous vous aidera à mieux comprendre.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Provider-Pattern-Flow.png)

Dans ce diagramme, l'objet **VERT** **A** sera disponible pour le reste des éléments en dessous, c'est-à-dire **B, C, D, E,** et **F.**

Maintenant, supposons que nous voulons ajouter une fonctionnalité à l'application et que nous créons un autre provider, **Z.** Z est requis par E et F.

Alors, quel est le meilleur endroit pour l'ajouter ?

Nous pouvons l'ajouter à la racine au-dessus de **A**. Cela fonctionnerait :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Provider-Pattern-Flow-2.png)

Mais cette méthode n'est pas très efficace.

Flutter parcourra tous les widgets au-dessus et finira par atteindre la racine. Si vous avez des arbres de widgets très longs – ce que vous aurez définitivement dans une application de production – alors ce n'est pas une bonne idée de tout mettre à la racine.

Au lieu de cela, nous pouvons regarder le dénominateur commun de E et F. C'est C. Donc, si nous plaçons Z juste au-dessus de E et F, cela fonctionnerait.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Provider-Pattern-Flow-3.png)

Mais que se passe-t-il si nous voulons ajouter un autre objet **X** qui est requis par E et F ? Nous ferons la même chose. Mais remarquez comment l'arbre continue de grandir.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Provider-Pattern-Flow-4.png)

Il existe une meilleure façon de gérer cela. Que se passe-t-il si nous fournissons tous les objets à un seul niveau ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Provider-Pattern-Flow-5.png)

C'est parfait, et c'est ainsi que nous implémenterons finalement notre Provider Pattern dans Flutter. Nous utiliserons quelque chose appelé `MultiProvider` qui nous permet de déclarer plusieurs providers à un seul niveau.

Nous allons faire en sorte que `MultiProvider` enveloppe le widget `MaterialApp` :

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider.value(
          value: Counter(),
        ),
      ],
      child: MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: MyHomePage(title: "AndroidVille Provider Pattern"),
      ),
    );
  }
}

```

Avec cela, nous avons fourni le provider à notre arbre de widgets et pouvons l'utiliser n'importe où en dessous de ce niveau dans l'arbre.

Il ne reste plus qu'une chose à faire : nous devons mettre à jour la valeur qui est affichée.

## **Mise à jour du texte**

Pour mettre à jour le texte, obtenez le provider dans la fonction build de votre widget `MyHomePage`. Nous utiliserons le getter que nous avons créé pour obtenir la dernière valeur.

Ensuite, ajoutez simplement cette valeur au widget de texte ci-dessous.

Et nous avons terminé ! Voici à quoi devrait ressembler votre fichier `main.dart` final :

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:provider_pattern_explained/counter.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider.value(
          value: Counter(),
        ),
      ],
      child: MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: MyHomePage(title: "AndroidVille Provider Pattern"),
      ),
    );
  }
}

class MyHomePage extends StatelessWidget {
  final String title;
  MyHomePage({this.title});
  void _incrementCounter(BuildContext context) {
    Provider.of<Counter>(context, listen: false).incrementCounter();
  }

  @override
  Widget build(BuildContext context) {
    var counter = Provider.of<Counter>(context).getCounter;
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _incrementCounter(context),
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}

```

Remarque : Nous n'avons pas défini `listen:false` dans ce cas car nous voulons écouter les mises à jour de la valeur du compteur.

Voici le code source sur GitHub si vous souhaitez y jeter un coup d'œil : [https://github.com/Ayusch/Flutter-Provider-Pattern](https://github.com/Ayusch/Flutter-Provider-Pattern).

Faites-moi savoir si vous avez des problèmes.

## Bienvenue à AndroidVille :)

AndroidVille est une communauté de développeurs mobiles où nous partageons des connaissances liées au développement Android, au développement Flutter, aux tutoriels React Native, à Java, à Kotlin et bien plus encore.

[Cliquez sur ce lien pour rejoindre l'espace de travail SLACK d'AndroidVille. C'est absolument gratuit !](https://rebrand.ly/73lbl3)

Si vous avez aimé cet article, n'hésitez pas à le partager sur Facebook ou LinkedIn. Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Twitter](https://twitter.com/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), et [Medium](https://medium.com/@jain.ayusch10) où je réponds aux questions liées au développement mobile, à Android et à Flutter.