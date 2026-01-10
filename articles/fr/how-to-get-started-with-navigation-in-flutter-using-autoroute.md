---
title: Comment débuter avec la navigation dans Flutter en utilisant AutoRoute
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-08T14:03:37.205Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-navigation-in-flutter-using-autoroute
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757340174515/e1614c20-e403-44a7-8509-514c6839bc4c.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment débuter avec la navigation dans Flutter en utilisant AutoRoute
seo_desc: 'Navigation is one of the most important parts of any mobile application.
  Users expect to move seamlessly between screens such as home, settings, profile,
  and more.

  While Flutter provides built-in navigation using Navigator, managing routes can
  quickl...'
---

La navigation est l'une des parties les plus importantes de toute application mobile. Les utilisateurs s'attendent à passer de manière fluide entre des écrans tels que l'accueil, les paramètres, le profil, et plus encore.

Bien que Flutter fournisse une navigation intégrée via `Navigator`, la gestion des routes peut rapidement devenir complexe dans les grandes applications. C'est là que les packages de routage comme **AutoRoute** interviennent. AutoRoute simplifie la navigation en générant des routes fortement typées, en réduisant le code redondant (boilerplate) et en rendant votre base de code plus facile à maintenir.

Cet article vous guidera à travers la configuration et l'utilisation d'AutoRoute dans un projet Flutter. À la fin, vous disposerez d'un projet fonctionnel avec plusieurs écrans et un système de routage structuré.

### Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
    
3. [Étape 1 : Configuration du projet](#heading-etape-1-configuration-du-projet)
    
4. [Étape 2 : Organisation de la structure du projet](#heading-etape-2-organisation-de-la-structure-du-projet)
    
5. [Étape 3 : Définition des routes avec AutoRoute](#heading-etape-3-definition-des-routes-avec-autoroute)
    
    * [Analyse détaillée](#heading-analyse-detaillee)
        
    * [Pourquoi faire cela avant les écrans ?](#heading-pourquoi-faire-cela-avant-les-ecrans)
        
6. [Étape 4 : Génération des fichiers de route](#heading-etape-4-generation-des-fichiers-de-route)
    
7. [Étape 5 : Configuration d'AutoRoute dans main.dart](#heading-etape-5-configuration-d-autoroute-dans-maindart)
    
    * [Points clés](#heading-points-cles)
        
8. [Étape 6 : Création des écrans](#heading-etape-6-creation-des-ecrans)
    
    * [screen1.dart](#heading-screen1dart)
        
    * [Analyse détaillée](#heading-analyse-detaillee-1)
        
    * [Répéter pour les autres écrans](#heading-repeter-pour-les-autres-ecrans)
        
    * [Pourquoi est-ce important ?](#heading-pourquoi-est-ce-important)
        
9. [Étape 7 : Écran de contrôle](#heading-etape-7-ecran-de-controle)
    
    * [Analyse étape par étape](#heading-analyse-etape-par-etape)
        
    * [Comment tout cela fonctionne ensemble](#heading-comment-tout-cela-fonctionne-ensemble)
        
10. [Captures d'écran](#heading-captures-decran)
    
11. [Bonnes pratiques lors de l'utilisation d'AutoRoute](#heading-bonnes-pratiques-lors-de-lutilisation-dautoroute)
    
12. [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, vous devriez avoir :

* Le SDK Flutter installé et configuré ([Guide d'installation Flutter](https://docs.flutter.dev/get-started/install)).
    
* Une compréhension de base des widgets Flutter, des widgets stateless vs stateful, et de l'API `Navigator`.
    
* Une familiarité avec l'exécution de commandes dans le terminal.
    
* Un IDE comme Android Studio, VS Code ou IntelliJ.
    

Si vous savez déjà comment construire des applications Flutter simples, vous êtes prêt.

## Ce que nous allons construire

Nous allons créer une application Flutter avec quatre écrans :

* **Control Screen** : l'écran principal avec des boutons pour naviguer vers les autres écrans.
    
* **Screen 1, Screen 2, Screen 3** : des pages simples qui démontrent la navigation.
    

Notre navigation sera entièrement gérée par AutoRoute, assurant une structure de projet propre et évolutive.

## Étape 1 : Configuration du projet

Commencez par créer un nouveau projet Flutter :

```bash
flutter create auto_route_example
```

Naviguez dans le dossier du projet et ouvrez le fichier `pubspec.yaml`. Ajoutez les dépendances suivantes :

```yaml
dependencies:
  auto_route: ^7.8.4

dev_dependencies:
  auto_route_generator: 7.3.2
  build_runner:
```

Exécutez la commande ci-dessous pour installer les packages :

```bash
flutter pub get
```

## Étape 2 : Organisation de la structure du projet

Pour l'évolutivité, gardez votre projet organisé. Créez la structure de dossiers suivante à l'intérieur de `lib` :

```dart
/lib
  /screens
    /sub_screens
      screen1.dart
      screen2.dart
      screen3.dart
    control_screen.dart
  /route_config
    app_route.dart
main.dart
```

Cette structure sépare les écrans de la logique de routage, rendant l'application plus facile à maintenir.

## Étape 3 : Définition des routes avec AutoRoute

Avant de commencer à annoter les écrans réels, configurons d'abord la configuration des routes. Ce fichier agira comme la carte de navigation de notre application : il indique à AutoRoute **quels chemins existent** et vers **quels écrans** ils doivent pointer.

Créez `lib/route_config/app_route.dart` et ajoutez ce qui suit :

```dart
import 'package:auto_route/annotations.dart';
import 'package:auto_route/auto_route.dart';
import 'app_route.gr.dart'; // fichier généré

@AutoRouterConfig()
class AppRouter extends $AppRouter {
  @override
  List<AutoRoute> get routes => [
        AutoRoute(path: '/', page: Controlscreen.page),
        AutoRoute(path: '/screen1', page: Screen1.page),
        AutoRoute(path: '/screen2', page: Screen2.page),
        AutoRoute(path: '/screen3', page: Screen3.page),
      ];
}
```

Analyse du code :

1. `@AutoRouterConfig()` dit à AutoRoute : « Voici la configuration centrale de routage. Veuillez l'utiliser pour générer le système de navigation. »
    
2. `class AppRouter extends $AppRouter` :
    
    * `AppRouter` est notre définition de routeur.
        
    * `$AppRouter` sera généré par AutoRoute une fois que nous aurons exécuté la génération de code. Il contient le travail lourd (comme les classes de routes et les helpers).
        

`List<AutoRoute> get routes => [...]`

* C'est ici que nous déclarons la carte de navigation de notre application.
    
* Chaque `AutoRoute` possède un **path** (`/screen1`) et une **page** (`Screen1.page`).
    

Exemple :

* `/` → `Controlscreen` (notre page de démarrage).
    
* `/screen1` → `Screen1`.
    
* `/screen2` → `Screen2`.
    
* `/screen3` → `Screen3`.
    

Pour l'instant, ces pages (`Screen1.page`, etc.) n'existent pas encore. Nous les créerons et les annoterons à l'**Étape 6**.

* `page: Screen1.page`
    
    * Ce getter `.page` ne deviendra disponible qu'après avoir annoté les écrans avec `@RoutePage`.
        
    * AutoRoute s'appuie sur cette annotation pour générer les usines (factories) de pages correctes.
        

### Pourquoi faire cela avant les écrans ?

En définissant les routes tôt, vous établissez un plan de navigation clair pour votre application. Plus tard, lorsque nous créerons les écrans, nous les « brancherons » simplement sur cette structure avec `@RoutePage`. Cela aide à garder le tutoriel logique : définir d'abord la carte, puis construire les destinations.

## Étape 4 : Génération des fichiers de route

Pour générer les fichiers de route, exécutez :

```bash
flutter pub run build_runner build
```

Ou, pour surveiller les changements automatiquement :

```bash
flutter pub run build_runner watch
```

Cela crée `app_route.gr.dart` dans le dossier `route_config`. Le fichier comprend des classes fortement typées pour chaque écran, telles que `Controlscreen`, `Screen1`, `Screen2`, et `Screen3`.

Cela signifie qu'au lieu de s'appuyer sur des chaînes de caractères brutes pour la navigation, vous utiliserez ces classes générées, réduisant ainsi les bugs liés aux fautes de frappe et offrant une meilleure autocomplétion dans l'IDE.

## Étape 5 : Configuration d'AutoRoute dans main.dart

Dans `main.dart`, configurez l'application pour utiliser AutoRoute :

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'route_config/app_route.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    final appRouter = AppRouter();

    SystemChrome.setSystemUIOverlayStyle(
      const SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
        statusBarIconBrightness: Brightness.dark,
      ),
    );

    return MaterialApp.router(
      title: 'Flutter AutoRoute Example',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.brown),
        useMaterial3: true,
      ),
      routerConfig: appRouter.config(),
    );
  }
}
```

Points clés dans ce code :

* `MaterialApp.router` remplace le `MaterialApp` traditionnel lors de l'utilisation d'AutoRoute.
    
* `appRouter.config()` fournit la configuration d'AutoRoute.
    

## Étape 6 : Création des écrans

Dans Flutter, chaque page ou section de votre application est généralement représentée par un **screen** (écran). Les écrans ne sont que des widgets (généralement enveloppés dans un `Scaffold`) qui contiennent l'interface utilisateur et la logique de cette page. Puisque nous utilisons AutoRoute, chaque écran vers lequel nous voulons naviguer doit être annoté avec `@RoutePage`.

L'annotation `@RoutePage` dit à AutoRoute : « Ce widget est une route. Veuillez l'inclure dans le système de routes généré. »

Sans cette annotation, AutoRoute ne connaîtra pas l'écran, et vous ne pourrez pas y naviguer via le routeur.

### screen1.dart

```dart
import 'package:auto_route/annotations.dart';
import 'package:flutter/material.dart';

@RoutePage(name: 'Screen1')
class Screen1 extends StatelessWidget {
  const Screen1({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Screen 1')),
      body: const Center(child: Text('Welcome to Screen 1')),
    );
  }
}
```

Analyse du code ici :

1. `@RoutePage(name: 'Screen1')`
    
    * Cette annotation enregistre le widget en tant que page routable.
        
    * Le paramètre `name` donne à AutoRoute un identifiant clair pour l'écran, qui sera également reflété dans le fichier `app_route.gr.dart` généré.
        
2. `class Screen1 extends StatelessWidget`
    
    * Définit l'écran comme un widget stateless car il n'a pas d'état dynamique dans cet exemple.
        
    * Pour des pages plus complexes (comme des formulaires ou des tableaux de bord), vous pourriez utiliser un `StatefulWidget`.
        
3. `Scaffold`
    
    * Fournit la structure de mise en page de base pour les applications Material Design.
        
    * Contient l'`AppBar` (barre supérieure avec le titre) et le `body` (zone de contenu principal).
        
4. `AppBar(title: const Text('Screen 1'))`
    
    * Affiche une barre d'application supérieure avec le titre "Screen 1".
        
5. `body: Center(child: Text('Welcome to Screen 1'))`
    
    * Centre le texte au milieu de l'écran.
        
    * Dans les applications réelles, c'est ici que vous ajouteriez vos widgets (listes, formulaires, tableaux de bord, etc.).
        

### Répéter pour les autres écrans

Suivez exactement la même structure pour **Screen2** et **Screen3** :

* Créez `screen2.dart` et `screen3.dart` à l'intérieur de `sub_screens`.
    
* Annotez chaque classe avec `@RoutePage` et donnez-lui un nom unique (`Screen2`, `Screen3`).
    
* Mettez à jour l'interface utilisateur à l'intérieur du `body` pour refléter de quel écran il s'agit.
    

Par exemple :

```dart
@RoutePage(name: 'Screen2')
class Screen2 extends StatelessWidget {
  const Screen2({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Screen 2')),
      body: const Center(child: Text('Welcome to Screen 2')),
    );
  }
}
```

### Pourquoi est-ce important ?

AutoRoute scanne votre projet et recherche les annotations `@RoutePage`. Il génère ensuite des classes de navigation fortement typées afin que vous puissiez écrire `context.router.push(const Screen2())` au lieu de taper manuellement des chaînes de route comme `'/screen2'`. Cela élimine l'erreur humaine (comme les fautes de frappe dans les chaînes de route) et rend la navigation plus facile à maintenir à mesure que votre application grandit.

## Étape 7 : Écran de contrôle

Le **ControlScreen** fait office de point d'entrée de notre application. C'est le premier écran qui se charge au démarrage de l'application (car dans `app_route.dart`, nous avons configuré `/` &gt; `Controlscreen`).

Cet écran ne montre aucun contenu complexe, à la place, il fournit des boutons pour naviguer vers d'autres écrans. Pensez-y comme à un **menu** ou un **tableau de bord** qui vous dirige vers les autres routes.

```dart
import 'package:auto_route/annotations.dart';
import 'package:auto_route/auto_route.dart';
import 'package:flutter/material.dart';

enum Screen { screen1, screen2, screen3 }

@RoutePage(name: 'Controlscreen')
class ControlScreen extends StatelessWidget {
  const ControlScreen({super.key});

  void navigateToScreen(BuildContext context, Screen screen) {
    switch (screen) {
      case Screen.screen1:
        context.router.pushNamed('/screen1');
        break;
      case Screen.screen2:
        context.router.pushNamed('/screen2');
        break;
      case Screen.screen3:
        context.router.pushNamed('/screen3');
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Control Screen')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () => navigateToScreen(context, Screen.screen1),
              child: const Text('Navigate to Screen 1'),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: () => navigateToScreen(context, Screen.screen2),
              child: const Text('Navigate to Screen 2'),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: () => navigateToScreen(context, Screen.screen3),
              child: const Text('Navigate to Screen 3'),
            ),
          ],
        ),
      ),
    );
  }
}
```

Analyse étape par étape du code :

1. `@RoutePage(name: 'Controlscreen')`
    
    * Marque `ControlScreen` comme une page routable.
        
    * AutoRoute générera une entrée `Controlscreen.page` pour une utilisation dans `app_route.dart`.
        

2. `enum Screen { screen1, screen2, screen3 }`
    
    * Nous définissons une énumération pour nos écrans cibles.
        
    * Cela rend la méthode de navigation plus propre et moins sujette aux erreurs que de taper des chaînes brutes à plusieurs endroits.
        

3. `navigateToScreen(BuildContext context, Screen screen)`
    
    * Une méthode helper qui vérifie **quel écran nous voulons** (basé sur l'enum) et appelle ensuite `context.router.pushNamed('/screenX')`.
        
    * `context.router` provient d'AutoRoute, il vous donne accès à la pile de navigation de l'application.
        
    * `pushNamed('/screen1')` correspond au chemin que nous avons défini plus tôt dans `app_route.dart` :
        
        ```dart
        AutoRoute(path: '/screen1', page: Screen1.page),
        ```
        
    * C'est ainsi que fonctionne la connexion bouton → chemin → route.
        

4. Mise en page UI (`Scaffold`)
    
    * `AppBar(title: Text('Control Screen'))` ajoute une barre de titre en haut.
        
    * `Column` avec 3 boutons : chaque bouton appelle `navigateToScreen()` avec une valeur d'enum différente.
        
    
    Exemple :
    
    * Bouton 1 `navigateToScreen(context, Screen.screen1)` : navigue vers `/screen1`.
        
    * Bouton 2 : navigue vers `/screen2`.
        
    * Bouton 3 : navigue vers `/screen3`.
        

### Comment tout cela fonctionne ensemble

1. **Démarrage de l'application** : Le routeur charge `/`, qui pointe vers `Controlscreen`.
    
2. **L'utilisateur appuie sur un bouton** : `navigateToScreen()` s'exécute et appelle `context.router.pushNamed('/screenX')`.
    
3. **AutoRoute fait correspondre le chemin** : Il recherche `/screenX` dans la liste des routes que nous avons définie dans `app_route.dart`.
    
4. **Le code généré prend le relais** : `app_route.gr.dart` (généré par AutoRoute) crée et pousse le bon widget d'écran sur la pile.
    

Le résultat : la navigation fonctionne sans écrire manuellement le code redondant de `Navigator.push`. AutoRoute gère tout pour vous.

## **Captures d'écran**

![control screen - main menu](https://cdn.hashnode.com/res/hashnode/image/upload/v1704182865496/ce5a0a5c-f5d8-4491-9f41-2d443631e3bd.png align="center")

![screen one](https://cdn.hashnode.com/res/hashnode/image/upload/v1704182887768/cc4156c9-afe3-4fc3-b4a3-75db71968c4a.png align="center")

![screen two](https://cdn.hashnode.com/res/hashnode/image/upload/v1704182902830/5f131796-cf76-41ed-940a-4486de90a966.png align="center")

![screen three](https://cdn.hashnode.com/res/hashnode/image/upload/v1704182916234/950633e3-1bf7-4a91-9b47-e61a1df00a0e.png align="center")

## Bonnes pratiques lors de l'utilisation d'AutoRoute

1. Organisez toujours les routes dans un dossier dédié (`route_config`) pour séparer les préoccupations.
    
2. Utilisez des routes fortement typées (classes générées) au lieu de chaînes brutes. Par exemple, utilisez `Screen1()` au lieu de `'/screen1'`.
    
3. Tirez parti des routes imbriquées pour les applications complexes (ex: onglets, flux d'authentification).
    
4. Utilisez des gardes (guards) dans AutoRoute pour protéger les routes qui nécessitent une authentification.
    
5. Gardez les écrans indépendants, évitez de placer la logique de navigation à l'intérieur des widgets d'écran sauf si nécessaire.
    

## Conclusion

AutoRoute simplifie la navigation dans les applications Flutter en générant du code répétitif, en assurant la sécurité des types et en offrant des fonctionnalités avancées comme la navigation imbriquée et les gardes. Avec une structure de projet propre et de bonnes pratiques, vous pouvez faire évoluer votre application Flutter en toute confiance.

Pour un apprentissage plus approfondi et des fonctionnalités avancées, reportez-vous à la documentation officielle :  
[AutoRoute sur pub.dev](https://pub.dev/packages/auto_route)