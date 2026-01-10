---
title: Comment gérer l'état dans les applications Flutter
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2022-04-25T14:11:47.000Z'
originalURL: https://freecodecamp.org/news/manage-state-in-flutter-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/connor-betts-50rXLuz0Txg-unsplash-1.jpg
tags:
- name: Flutter
  slug: flutter
- name: 'State Management '
  slug: state-management
seo_title: Comment gérer l'état dans les applications Flutter
seo_desc: "Managing state is something most developers need to deal with when working\
  \ on applications. \nYou might be familiar with the model-view-viewmodel (MVVM)\
  \ pattern, where the ViewModel is the one responsible for a view’s state. But in\
  \ Flutter, things are..."
---

La gestion de l'état est quelque chose que la plupart des développeurs doivent gérer lorsqu'ils travaillent sur des applications. 

Vous êtes probablement familier avec le modèle modèle-vue-viewmodel (MVVM), où le ViewModel est responsable de l'état d'une vue. Mais dans Flutter, les choses sont un peu différentes. 

Si vous lisez ceci, alors vous êtes probablement conscient des nombreuses façons de gérer l'état dans Flutter. Il existe de nombreux articles qui tentent d'expliquer cela, mais ils couvrent généralement une solution spécifique et fournissent un exemple très minimal. 

Comme vous, j'ai parcouru ces articles et j'ai essayé de saisir ce concept intangible dans Flutter. Mais rien ne vaut de mettre les mains dans le cambouis et d'essayer les choses par soi-même. 

Après beaucoup de tribulations et ma juste part d'essais et d'erreurs, je commence à voir la lumière dans ma compréhension de la gestion de l'état dans les applications basées sur Flutter.

À mesure que Flutter gagne en popularité et que votre application peut devenir de plus en plus complexe, vous arriverez à un point où la création de widgets stateful ne suffira plus. 

Lorsque vous atteindrez ce point, vous pouvez essayer de bricoler une solution qui vous fournit la fonctionnalité souhaitée, mais elle ne suivra probablement pas les bons paradigmes. Ou vous pouvez vous confronter au monolithe qu'est la gestion de l'état dans Flutter.

L'aborder seul peut sembler écrasant, alors j'espère que cet article vous servira de boussole lorsque vous en aurez besoin. 

Nous allons passer en revue plusieurs concepts fondamentaux de base dans la gestion de l'état dans Flutter et je travaillerai avec un exemple de cas d'utilisation réel pour rendre les choses aussi claires que possible (aucune de ces absurdités d'application de compteur 😁).

Prêt à SetState?

## Contexte de l'état dans Flutter

Pour les non-initiés, voici une liste de toutes les solutions d'état offertes par l'équipe Flutter (en avril 2022) :

* Provider
* Riverpod
* setState
* InhertiedWidget et InheritedModel
* Redux
* Fish-Redux
* BLoC/Rx
* GetIt
* MobX
* Flutter Commands
* Binder
* GetX
* States Rebuilder
* Triple Pattern

😱 H-o-l-y crap! Pouvez-vous croire cette liste ?

La liste ci-dessus est tirée directement de la [documentation Flutter pour la gestion de l'état](https://docs.flutter.dev/development/data-and-backend/state-mgmt/options) et je voulais vous la montrer pour deux raisons :

1. Valeur de choc
2. Pour vous donner une meilleure compréhension de ce dont je parlais plus tôt

Maintenant, avant de continuer à lire, il est important de comprendre que, selon la logique et la complexité de votre application, vous n'aurez peut-être pas besoin de l'une des solutions mentionnées ci-dessus. Il peut être tout à fait acceptable pour vous de gérer l'état avec des widgets stateful et setState. 

Vous saurez quand cela ne suffira plus lorsque vous essayerez de développer un composant et utiliserez ces deux options et découvrirez que vous avez besoin de quelque chose d'autre pour faire fonctionner les choses.

Comment le saurez-vous ? Excellente question.

À un moment donné dans le développement de mon application, j'ai décidé que je voulais avoir un écran de paramètres. Dans cet écran de paramètres, l'utilisateur peut faire certaines configurations au niveau de l'application. 

L'application elle-même n'est pas très complexe et je n'ai pas eu à utiliser l'une des solutions d'état listées ci-dessus. J'ai utilisé un état lié à un widget stateful et il n'a pas eu à être partagé entre de nombreux composants différents. Dans les cas où un widget devait informer d'une action de l'utilisateur dans un autre widget, j'ai utilisé des callbacks.

Maintenant, lorsque j'ai créé la page des paramètres, une action de l'utilisateur prise là-bas devait être reflétée ailleurs dans l'application. Par exemple, j'ai ajouté la possibilité de basculer entre le mode clair et le mode sombre dans l'application. 

Cela affecte l'ensemble de l'interface utilisateur de l'application et doit être reflété instantanément lorsque l'utilisateur bascule cette option. Donc, avoir un autre widget stateful pour l'écran des paramètres ne m'aiderait pas ici.

> Comment pourrais-je refléter les changements se produisant dans l'écran des paramètres au reste de mon application ?

Cela ressemble certainement à un problème lié à l'état.

## La Fondation – ChangeNotifier

L'état dans Flutter doit être déclaré au-dessus (dans l'arborescence des widgets) des composants qui l'utilisent. Cela permet à l'état d'être transmis aux widgets enfants. 

Pour que cet état remonte, vous devez utiliser des composants qui peuvent vous aider à faire cela.

Dites bonjour à [**ChangeNotifier**](https://api.flutter.dev/flutter/foundation/ChangeNotifier-class.html).

C'est une classe qui permet à d'autres endroits du code d'écouter les changements via une API de notification. Cela peut vous sembler familier si vous avez déjà rencontré le concept d'un [observable](https://en.wikipedia.org/wiki/Observer_pattern#:~:text=The%20observer%20pattern%20is%20a,calling%20one%20of%20their%20methods.). Si ce n'est pas le cas, ne vous inquiétez pas. Le concept est assez simple. 

De la même manière que setState fait reconstruire un widget stateful, ChangeNotifier a une méthode appelée notifyListeners qui permet à des endroits de votre code de réagir au changement qui s'est produit. Cette fonctionnalité est intégrée dans Flutter, car ChangeNotifier fait partie du package flutter:foundation.

Prenons l'écran des paramètres que j'ai mentionné plus tôt. Une fois que l'utilisateur change le thème de l'application, d'autres endroits de l'application peuvent écouter ce changement et mettre à jour leur interface utilisateur respective.

Afin de minimiser la logique requise ici, prenons le projet de démarrage vanilla que vous obtenez lorsque vous créez un projet Flutter (celui du compteur) et ajoutons un écran de paramètres.

Voici à quoi ressemble le fichier main.dart (sans toute la logique du compteur) :

```dart
import 'package:flutter/material.dart';
import 'settings_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'State Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      darkTheme: ThemeData.dark(),
      themeMode: ThemeMode.light,
      home: const MyHomePage(title: 'State Example'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(
            icon: const Icon(
              Icons.settings,
              color: Colors.white,
            ),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const SettingsScreen()
                ),
              );
            },
          )
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'State Example',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
    );
  }
}
```

Voici à quoi ressemble le fichier settings_screen :

```dart
import 'package:flutter/material.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
            title: const Text("Settings"),
        ),
      body:
         Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
            SwitchListTile(
              title: const Text('Dark Mode'),
              value: false,
              secondary:  const Icon(Icons.dark_mode,
                  color: Color(0xFF642ef3)
                ),
               onChanged: (bool value) {

              }
              )
            ]
          )
        );
      }
}
```

Pour l'instant, il n'y a pas grand-chose et il n'y a aucune logique pour mettre à jour lorsque l'utilisateur appuie sur le SwitchTile. Vous pouvez également remarquer que nous n'avons pas rempli le callback onChanged.

Créons notre classe ChangeNotifier, **SettingsScreenNotifier**. 

```dart
import 'package:flutter/cupertino.dart';

class SettingsScreenNotifier extends ChangeNotifier { /// 1
  bool _isDarkModeEnabled = false;                    /// 2
  get isDarkModeEnabled => _isDarkModeEnabled;        /// 3
  void toggleApplicationTheme(bool darkModeEnabled) { /// 4
    _isDarkModeEnabled = darkModeEnabled;
    notifyListeners();
  }

}
```

1. Notre classe étend la classe ChangeNotifier
2. Nous avons déclaré un membre privé appelé _isDarkModeEnabled
3. Nous avons exposé un getter pour ce membre
4. Remarquez comment à l'intérieur de la méthode toggleApplicationTheme, la dernière ligne est l'appel à `notifyListeners()`. Cela garantit que chaque fois que cette méthode est appelée, tous les écouteurs seront mis à jour.

Comme mentionné précédemment, nous avons besoin d'un moyen d'exposer l'état dans notre SettingsScreenNotifier à notre application. Puisque dans ce scénario spécifique, cet état sera utilisé par notre application principale (puisqu'il implique le thème de l'ensemble de l'application), nous devons le placer en haut de notre application. 

Nous pouvons faire cela en utilisant le **ChangeNotifierProvider**. Il s'agit d'un widget qui fournit une instance de notre ChangeNotifier à tous les widgets descendants et provient du [package provider](https://pub.dev/packages/provider). Il s'agit d'un package qui enveloppe beaucoup de fonctionnalités autour du [InheritedWidget](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html).

⚠️ Soyez attentif à l'endroit où vous placez votre widget ChangeNotifierProvider. Si vous le placez trop haut dans votre arborescence de widgets, il peut provoquer le re-rendu de widgets que vous ne souhaitez pas (et aussi polluer la portée).

Ajoutons le package provider au fichier pubspec.yaml :

```yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.0.2
```

Appuyez sur Pub get pour télécharger le package.

Ensuite, nous allons envelopper notre application avec ChangeNotifierProvider (n'oubliez pas d'importer le package provider).

```dart
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => SettingsScreenNotifier(),  /// 1
      builder: (context, provider) {                  /// 2
        return MaterialApp(
          title: 'State Example',
          theme: ThemeData(
            primarySwatch: Colors.blue,
          ),
          darkTheme: ThemeData.dark(),
          themeMode: ThemeMode.light,
          home: const MyHomePage(title: 'State Example'),
        );
      }
    );
  }
}
```

Le premier argument est la méthode create où nous créons une instance de notre ChangeNotifier.

Le deuxième argument est une fonction builder qui accepte le contexte et le provider qui a été créé.

Super ! Maintenant, notre application pourra écouter les changements de notre ChangeNotifier.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/zuzana-ruttkay-1kslaBtXBk8-unsplash.jpg)
_Photo par [Unsplash](https://unsplash.com/@zuzi_ruttkay?utm_source=medium&amp;utm_medium=referral" rel="noopener ugc nofollow">Zuzana Ruttkay</a> sur <a href="https://unsplash.com/?utm_source=medium&amp;utm_medium=referral" rel="noopener ugc nofollow)_

## Comment tout connecter ensemble

Nous avons infusé notre application avec un provider, mais comment connectons-nous les données de notre ChangeNotifier ?

Pour cela, nous utilisons un widget [**Consumer**](https://pub.dev/documentation/provider/latest/provider/Consumer-class.html). Ce widget expose les données détenues par notre ChangeNotifier. Chaque fois que nous déclarons un widget Consumer, nous devons également lui fournir le type de l'objet qu'il fournit. 

Dans notre cas, ce sera notre **SettingsScreenNotifier**. Le widget Consumer a un argument appelé builder (comme ChangeNotifierProvider et d'autres widgets) et il est appelé chaque fois que l'objet ChangeNotifier que vous lui avez donné change (ce qui signifie que notifyListeners a été appelé). 

La fonction builder accepte trois arguments :

1. Le contexte
2. Instance du ChangeNotifier
3. Un widget enfant (celui-ci peut être utilisé dans le cas où la partie de votre arborescence de widgets sous le widget Consumer ne change pas et vous ne voulez pas le reconstruire)

Nous devons envelopper notre MaterialApp avec un widget Consumer afin que le thème puisse changer lorsque l'utilisateur fait une sélection dans l'écran des paramètres.

```dart
@override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => SettingsScreenNotifier(),
      builder: (context, provider) {
        return Consumer<SettingsScreenNotifier>(
          builder: (context, notifier, child) {
            return MaterialApp(
              title: 'State Example',
              theme: ThemeData(
                primarySwatch: Colors.blue,
              ),
              darkTheme: ThemeData.dark(),
              themeMode: notifier.isDarkModeEnabled ? ThemeMode.dark : ThemeMode.light,
              home: const MyHomePage(title: 'State Example'),
            );
          },
        );
      }
    );
  }
}
```

Et dans notre écran des paramètres, nous devrons :

1. Envelopper notre **SwitchTile** avec un widget Consumer afin que l'interface utilisateur puisse répondre correctement lorsqu'une interaction est faite
2. Appeler toggleApplicationTheme dans le callback onChanged

```dart
import 'package:flutter/material.dart';
import 'package:state_example/settings_screen_notifier.dart';
import 'package:provider/provider.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
          return Scaffold(
              appBar: AppBar(
                title: const Text("Settings"),
                ),
                body:
                  Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: [
                        Consumer<SettingsScreenNotifier> (                   /// 1
                         builder: (context, notifier, child) {
                           return SwitchListTile(
                               title: const Text('Dark Mode'),
                               value: notifier.isDarkModeEnabled,
                               secondary:  const Icon(Icons.dark_mode,
                                   color: Color(0xFF642ef3)
                               ),
                               onChanged: (bool value) {
                                 notifier.toggleApplicationTheme(value);    /// 2 
                               }
                           );
                         }
                        )
                      ]
                  )
                );
          }
}
```

Admirez l'extraordinaire 🔥 ☀️🌙

![Image](https://www.freecodecamp.org/news/content/images/2022/04/qemu-system-x86_64_p9BcpAJnZO.gif)

Cet article n'est que la partie émergée de l'iceberg concernant l'état dans Flutter et l'utilisation du package provider. Il y a beaucoup plus à apprendre et je vous encourage vraiment à essayer les choses par vous-même. 

Le package provider a une excellente documentation, et dans le cas où vous voyez une erreur dans les logs, il a une explication assez robuste de ce qui s'est mal passé et de la manière dont vous pouvez le corriger.

Où aller à partir de là ?

* [Documentation Provider](https://pub.dev/documentation/provider/latest/index.html)
* [Package GetIt](https://pub.dev/packages/get_it) – une autre solution de gestion d'état, qui peut être plus facile à comprendre
* [ValueNotifier](https://api.flutter.dev/flutter/foundation/ValueNotifier-class.html) – similaire à ChangeNotifier mais pour une seule valeur
* [Suragch](https://medium.com/@suragch) – Un développeur Flutter passionné qui a écrit de nombreux articles sur le développement Flutter et la gestion de l'état en particulier. Ses articles m'ont énormément aidé 👍

Les exemples présentés dans cet article sont tirés d'une application que j'ai créée appelée **BirthdayCalendar**. Vous pouvez la consulter ici :

%[https://play.google.com/store/apps/details?id=com.tomerpacific.birthday_calendar]

Vous pouvez voir le code source ici :

%[https://github.com/TomerPacific/BirthdayCalendar]