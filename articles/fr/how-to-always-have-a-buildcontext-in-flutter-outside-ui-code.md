---
title: Comment toujours avoir un BuildContext dans Flutter en dehors du code UI
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2024-03-19T14:42:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-always-have-a-buildcontext-in-flutter-outside-ui-code
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Untitled-design.png
tags:
- name: Flutter
  slug: flutter
seo_title: Comment toujours avoir un BuildContext dans Flutter en dehors du code UI
seo_desc: "The BuildContext provides important app-wide configuration information\
  \ to all widgets in the widget tree. It is always naturally available in build methods\
  \ and within State classes. \nIn this article, we will explore how we can obtain\
  \ a valid BuildCon..."
---

Le BuildContext fournit des informations de configuration importantes pour l'ensemble de l'application à tous les widgets de l'arborescence des widgets. Il est toujours naturellement disponible dans les méthodes de construction et au sein des classes State. 

Dans cet article, nous allons explorer comment obtenir un BuildContext valide en dehors de la portée de sa disponibilité naturelle.

## Table des matières

* [Introduction](#heading-introduction)
* [L'essence du BuildContext dans Flutter](#heading-lessence-du-buildcontext-dans-flutter)
* [Le besoin d'un BuildContext en dehors du code UI](#heading-le-besoin-dun-buildcontext-en-dehors-du-code-ui)
* [Avoir une clé navigatorKey globalement disponible](#heading-avoir-une-cle-navigatorkey-globalement-disponible)
* [Une note sur Navigator 2.0](#heading-une-note-sur-navigator-20)
* [Utilisation de l'état de navigation de navigatorKey pour afficher des toasts](#heading-utilisation-de-letat-de-navigation-de-navigatorkey-pour-afficher-des-toasts)
* [Résumé](#heading-resume)

## Introduction

Flutter est un kit d'interface utilisateur pour créer des applications de bureau, mobiles et web. Flutter est un framework qui permet de créer des applications dans le langage de programmation Dart.

Dans Flutter, vous construisez des interfaces utilisateur en composant des widgets. Un widget est toute pièce logique de ce qui est rendu à l'écran comme Icon, Image, Text, et ainsi de suite.

La composition de widgets implique de les définir comme enfant ou comme enfants d'autres widgets parents. En d'autres termes, vous construisez une arborescence de widgets. Tous les widgets de votre arborescence UI ont accès au BuildContext.

## L'essence du BuildContext dans Flutter

Le BuildContext fournit des informations de configuration importantes pour l'ensemble de l'application à tous les widgets de l'arborescence des widgets.

Le BuildContext est pour les widgets Flutter ce que l'eau est pour notre corps. Tout comme l'eau circule dans notre système avec des nutriments et de l'oxygène, le BuildContext fournit des valeurs spécifiques à l'exécution à chaque widget de nos applications.

Dans Flutter, vous créez généralement un widget en étendant les classes StatelessWidget ou StatefulWidget (et son State).

Dans les deux cas, vous devez substituer la méthode build. Dans la méthode build, vous devez retourner un autre widget. De cette manière, vous continuez à construire l'arborescence des widgets.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/widget_tree.png)
_Source de l'image : https://groups.google.com/g/flutter-dev/c/jfPgd5FS6EM_

Toutes les méthodes build ne prennent qu'un seul argument : le BuildContext. Vous avez besoin du BuildContext dans Flutter pour rendre l'interface utilisateur. Il est indispensable. Le framework Flutter lui-même fournit le BuildContext à chaque méthode build de widget.

Le BuildContext vous donne accès à des getters et méthodes comme :

* [`findAncestorStateOfType`](https://api.flutter.dev/flutter/widgets/BuildContext/findAncestorStateOfType.html) : une méthode _typée_ qui retourne l'objet `State` du `StatefulWidget` spécifié.
* [`getInheritedWidgetOfExactType`](https://api.flutter.dev/flutter/widgets/BuildContext/dependOnInheritedWidgetOfExactType.html) : une méthode _typée_ qui retourne un type de widget demandé qui est trouvé plus haut dans l'arborescence des widgets.
* [`mounted`](https://api.flutter.dev/flutter/widgets/BuildContext/mounted.html) : un `bool` qui indique si le widget _en contexte_ est en vue.

Il existe d'autres getters et méthodes utiles disponibles sur le BuildContext. En dehors de ceux-ci, le BuildContext est également important car grâce à lui, nous pouvons obtenir l'instance active de l'application de classes spécifiques. Par exemple : MediaQuery, Navigator, Theme, et ainsi de suite.

Un modèle courant consiste à appeler la méthode statique `.of` sur la classe d'intérêt et à fournir notre BuildContext (ou simplement "context") à cette méthode `.of`.

```dart
final isLandscape = MediaQuery.of(context).orientation == Orientation.landscape;
final hasConfirmed = Navigator.of(context).pop(false);
final lightTheme = Theme.of(context).copyWith(brightness: Brightness.light);

```

Le `.of` est le modèle le plus courant. Cependant, il existe d'autres cas d'utilisation plus directs, spécifiques et rares de tels getters statiques qui dépendent du contexte.

```dart
final isDarkTheme = Theme.brightnessOf(context) == Brightness.dark;

```

Vous pouvez également créer des getters statiques d'instances de vos classes qui dépendent du BuildContext. [Vous pouvez en apprendre plus sur la façon de faire cela (via InheritedWidget) ici](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html).

Comme nous le voyons, voici pourquoi nous avons besoin du BuildContext :

* Pour construire des widgets,
* Pour accéder aux ressources,
* Pour obtenir des instances de classes,
* et ainsi de suite.

## Le besoin d'un BuildContext en dehors du code UI

Le BuildContext est naturellement disponible à l'intérieur de toutes les méthodes build et à l'intérieur de la classe `State` des `StatefulWidgets`. La plupart des appels de méthodes avec contexte dans ces portées fonctionneront comme prévu.

Dans de rares occasions, vous devrez accéder au BuildContext depuis un endroit où il n'est pas naturellement disponible. Vous voudrez obtenir des instances d'exécution en dehors du code UI (en dehors des méthodes build et des classes `State`).

Cela est généralement difficile car nous ne pouvons pas instancier un BuildContext nous-mêmes. Nous n'avons accès à un BuildContext que lorsque notre application a commencé à s'exécuter.

Les raisons populaires d'accéder au BuildContext de cette manière sont soit lors de la navigation, lors de l'affichage d'alertes et de modales dans du code non-UI, ou lors du déclenchement de mises à jour de l'interface utilisateur à partir de changements dans l'architecture d'état de l'application.

De plus, lorsqu'un utilisateur ouvre une notification, nous voulons naviguer vers l'écran cible si l'application est déjà ouverte. Nous avons besoin du BuildContext pour cela.

## Avoir une clé navigatorKey globalement disponible

Une solution pour toujours avoir un BuildContext dans Flutter est d'en fournir un vous-même au démarrage de l'application.

Le widget le plus haut des applications Flutter est généralement soit [`CupertinoApp`](https://api.flutter.dev/flutter/cupertino/CupertinoApp-class.html), [`MaterialApp`](https://api.flutter.dev/flutter/material/MaterialApp-class.html), ou [`WidgetsApp`](https://api.flutter.dev/flutter/widgets/WidgetsApp-class.html). En d'autres termes, ce sont le point d'entrée de notre application.

Ces widgets "app" prennent un paramètre optionnel `navigatorKey`. Il est de type `GlobalKey<NavigatorState>`. Cette GlobalKey spécifique à NavigatorState a un BuildContext attaché une fois que l'application est en cours d'exécution. 

Lorsque vous créez une navigatorKey et la donnez au widget "app" le plus haut, votre application Flutter conservera le BuildContext qu'elle utilise dans votre navigatorKey. Ainsi, vous pouvez avoir accès au BuildContext partout où vous avez accès à la navigatorKey.

Créez et exposez la navigatorKey en tant que variable _static final_ à partir d'une classe utilitaire globale. Fournissez-la au widget "app" le plus haut. Ensuite, obtenez le contexte à partir de cette classe globalement disponible partout où vous en avez besoin.

```dart
/* Dans services/navigation_service.dart */
class NavigationService {
  static final navigatorKey = GlobalKey<NavigatorState>();

  // ... autres méthodes et getters
}

/* Dans main.dart */
import 'package:flutter/material.dart';

import 'services/navigation_service.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      navigatorKey: NavigationService.navigatorKey, // ligne d'intérêt
      home: const Scaffold(body: Center(child: Text('BuildContext'))),
    );
  }
}

/* Dans services/modal_service.dart */
import 'package:flutter/material.dart';

import 'services/navigation_service.dart';

Future<T?> showModal<T>(Widget modal) async {
  return await showModalBottomSheet<T>(
    context: NavigationService.navigatorKey.currentContext!,
    backgroundColor: Colors.transparent,
    isScrollControlled: true,
    builder: (_) => modal,
  );
}

```

Dans l'exemple ci-dessus, vous pouvez voir comment nous pouvons appeler [`showModalBottomSheet`](https://api.flutter.dev/flutter/material/showModalBottomSheet.html) à partir d'un fichier non-widget en utilisant le contexte de la navigatorKey. Cela ne fonctionnera que si cette clé a été attachée au widget "app" le plus haut comme montré dans l'extrait de code.

Cette façon d'accéder au BuildContext a toujours existé. [Nous pouvons la voir utilisée dans l'architecture Stacked](https://github.com/Stacked-Org/stacked/blob/53ef130d36db1d8d6756375cb8e9495f82c1d771/example/navigator_example/lib/main.dart#L20).

Vous pourriez conserver la navigatorKey dans une classe entièrement différente de certains NavigationService. Elle pourrait également être une variable globale autonome dans votre projet Flutter. De plus, vous pourriez la rendre disponible via l'architecture de gestion d'état que vous utilisez.

La manière dont vous rendez la navigatorKey globalement disponible vous appartient. Ce qui est nécessaire, c'est que vous en fournissiez une à Flutter lorsque vous avez besoin du BuildContext en dehors du code UI.

## Une note sur Navigator 2.0

Il existe une configuration spéciale qui mérite d'être mentionnée à ce stade. 

Les widgets "app" les plus hauts (CupertinoApp, MaterialApp et WidgetsApp) ont tous un constructeur `.router`. Ce constructeur est différent de l'équivalent direct car il crée une application qui utilise un [`Router` au lieu d'un `Navigator`](https://docs.flutter.dev/ui/navigation).

Plus précisément, les applications `.router` nous permettent d'effectuer une navigation déclarative (`router.go`) au lieu de seulement une navigation impérative (`navigator.push` et `navigator.pop`). 

La navigation déclarative fonctionne bien avec le deep linking (lorsque les applications mobiles ouvrent des URL) et avec l'historique du navigateur (un plus pour Flutter web).

Ces constructeurs `.router` ne prennent pas d'argument navigatorKey. Cependant, ils peuvent accepter diverses classes spécifiques au routeur comme arguments. Dans ces classes, vous pouvez fournir une navigatorKey d'une manière ou d'une autre.

Par exemple, [`go_router`](https://pub.dev/packages/go_router) est un package bien connu pour Navigator 2.0 dans Flutter. Il abstrait les complexités de ces classes spécifiques au routeur. 

Maintenant, le constructeur [`GoRouter`](https://pub.dev/documentation/go_router/latest/go_router/GoRouter-class.html), comme vous vous en doutez, accepte un argument navigatorKey. Ainsi, si vous l'utilisez, vous pouvez toujours avoir accès au BuildContext dans n'importe quel code non-UI dans votre projet Flutter.

## Utilisation de l'état de navigation de navigatorKey pour afficher des toasts

Un avantage supplémentaire d'avoir une navigatorKey attachée est lorsque nous voulons afficher des informations à l'utilisateur sous forme de toast. 

Nous pouvons le faire en ajoutant un [`OverlayEntry`](https://api.flutter.dev/flutter/widgets/OverlayEntry-class.html) (avec un widget toast) dans le `overlay` de `NavigatorState` qui est attaché à notre navigatorKey.

Avec l'aide d'un `Timer`, le toast est supprimé après quelques secondes :

```dart
/* Dans services/toast_service.dart */
import 'dart:async';

import 'navigation_service.dart';

Widget _toast(String text) => Container(
    padding: const EdgeInsets.fromLTRB(16, 12, 16, 12),
    decoration: BoxDecoration(
      borderRadius: BorderRadius.circular(6),
      color: Colors.teal,
    ),
    child: Text(text),
  );

class ToastService {
  static OverlayEntry? _entry;
  static Timer? _timer;

  static show(String text) {
    _dismiss();
    _entry = OverlayEntry(builder: (context) => _Toast(text));
    NavigationService.navigatorKey.currentState!.overlay!.insert(_entry!);
    _timer = Timer(const Duration(seconds: 5), _dismiss);
  }

  static _dismiss() {
    try {
      _timer?.cancel();
      _timer = null;
      _entry?.remove();
      _entry = null;
    } catch () {
    }
  }
}

/* Dans services/auth_service.dart */
import 'toast_service.dart';

class AuthService {
  static void login({required String email, required String password}) async {
    // ... appel de l'API

    // toast après une connexion réussie
    ToastService.show('Bienvenue à nouveau !');
  }
}

```

## Résumé

"context" est quelque chose que vous utiliserez toujours dans Flutter. 

Lorsque vous en avez besoin en dehors de la méthode build (ou des classes State), créez une navigatorKey et attachez-la au widget "app" le plus haut. 

Vous pouvez ensuite accéder au même contexte que votre code UI utilise à partir de cette clé, depuis n'importe où dans le projet Flutter.

Santé !