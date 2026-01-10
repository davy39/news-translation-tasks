---
title: Comment créer une application sociale multilingue de recettes avec Flutter
  et Strapi
subtitle: ''
author: Kevine Nzapdi
co_authors: []
series: null
date: '2025-04-08T21:51:08.500Z'
originalURL: https://freecodecamp.org/news/build-a-multilingual-social-recipe-app-with-flutter-and-strapi
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743509325302/fd7d5d6c-9a48-4037-9cc2-3b35a92b6006.png
tags:
- name: Recipe Apps
  slug: recipe-apps
- name: Strapi
  slug: strapi
- name: Flutter
  slug: flutter
- name: Beginner Developers
  slug: beginners
- name: multilingual
  slug: multilingual
seo_title: Comment créer une application sociale multilingue de recettes avec Flutter
  et Strapi
seo_desc: 'Hey there!

  In this project, you will build a multilingual social recipe application using Flutter
  and Strapi.

  Flutter is an open-source UI software development kit created by Google. It allows
  you to build beautiful and highly interactive user interf...'
---

Salut !

Dans ce projet, vous allez créer une application sociale multilingue de recettes en utilisant Flutter et Strapi.

Flutter est un kit de développement d'interface utilisateur open-source créé par Google. Il permet de créer des interfaces utilisateur belles et hautement interactives pour mobile, web et desktop à partir d'une seule base de code.

Strapi, quant à lui, est un CMS headless qui facilite la création, la gestion et la distribution de contenu partout où vous en avez besoin – le tout depuis un seul endroit.

La fonctionnalité multilingue de l'application permettra aux utilisateurs de différentes parties du monde d'interagir avec l'application dans leur langue maternelle, la rendant ainsi plus conviviale et accessible. Cette fonctionnalité est particulièrement bénéfique pour une application sociale de recettes où les utilisateurs partagent des recettes de différentes cuisines et cultures.

Dans cette application, les utilisateurs pourront consulter des recettes, demander une recette spécifique, partager leurs recettes préférées, et aimer ou commenter des recettes.

## Table des matières

1. [Prérequis](#heading-prerequisites)

2. [Démo](#heading-demo)

3. [Créer des Modèles](#heading-create-models)

4. [Ajouter des Langues et Activer l'Internationalisation dans Strapi](#heading-add-languages-and-enable-internationalization-in-strapi)

5. [Ajouter du Contenu de Recette](#heading-add-recipe-content)

* [Ajouter du Contenu de Recette en Anglais](#heading-add-recipe-english-content)

* [Ajouter du Contenu de Recette en Français](#heading-add-recipe-french-content)

* [Ajouter du Contenu de Recette en Japonais](#heading-add-recipe-japanese-content)

6. [Générer un Jeton API et Définir les Permissions](#heading-generate-api-token-and-set-permissions)

* [Définir les Rôles et Permissions des Utilisateurs](#heading-set-user-roles-and-permissions)

7. [Configurer Flutter](#heading-installation)

* [Structure du Projet](#heading-project-structure)

8. [Installer les Packages](#heading-install-packages)

* [Ajouter des Assets](#heading-add-assets)

* [Examiner main.dart](#heading-taking-a-look-at-maindart)

9. [Ajouter des Variables d'Environnement](#heading-add-environment-variables)

10. [Créer des Modèles](#heading-create-models-1)

* [1. RecipeRequest](#heading-1-reciperequest)

* [2. Step](#heading-2-step)

* [3. Description](#heading-3-description)

* [4. TextContent](#heading-4-textcontent)

* [5. Comment](#heading-5-comment)

* [6. Recipe](#heading-6-recipe)

11. [Créer des Services](#heading-create-services)

* [1. Variables de Classe](#heading-1-class-variables)

* [2. Méthodes d'Assistance](#heading-2-helper-methods)

* [3. Opérations Utilisateur](#heading-3-user-operations)

* [4. Récupération et Manipulation des Données](#heading-4-data-fetching-and-manipulation)

12. [Autorisation et Authentification](#heading-authorization-and-authentication)

* [Inscription](#heading-registration)

* [Connexion](#heading-login)

13. [Créer des Composants d'Application](#heading-build-app-components)

* [Drawer](#heading-drawer)

* [AppBar](#heading-appbar)

14. [Récupérer les Recettes](#heading-fetch-recipes)

15. [Voir la Recette](#heading-view-recipe)

16. [Créer l'Écran de Demande de Recette](#heading-create-request-recipe-screen)

17. [Créer l'Écran de Profil Utilisateur](#heading-create-user-profile-screen)

18. [Tester l'Application](#heading-test-the-app)

19. [Conclusion](#heading-conclusion)

20. [Références](#heading-references)

## Prérequis

Pour suivre ce tutoriel, assurez-vous d'avoir :

* [Node.js](https://nodejs.org/en) installé.

* Une connaissance de base de [Flutter](https://flutter.dev/)

* Une compréhension de base de Strapi avec ce [guide rapide](https://docs.strapi.io/dev-docs/quick-start)

## Démo

Voici ce que vous allez construire dans ce tutoriel :

1. Authentification et Autorisation : [Démo](https://drive.google.com/file/d/1cjnnRD38wQsj_sYHl5EG5uM3AyHJUWdf/view?usp=sharing)

2. Commentaires et Likes : [Démo](https://drive.google.com/file/d/1wM0xQ2R7inL90gAkiYjLcGV5df4AmzH1/view?usp=sharing)

3. Demande de recette : [Démo](https://drive.google.com/file/d/1xlxSFD2qU2rOE4kICiX-py_JxvgrphqK/view?usp=sharing)

4. Changement de Langue : [Démo](https://drive.google.com/file/d/14lmBCIgX4VIKOFmS9pG71cIHH7HLaW1J/view?usp=sharing)

Vous pouvez obtenir le code complet de l'application depuis [ce dépôt GitHub](https://github.com/Gunkev/flutter_strapi_multilingual_app).

## Créer des Modèles

Une fois que vous avez configuré un projet Strapi avec [ce guide rapide](https://docs.strapi.io/dev-docs/installation/cli), créez deux modèles, Recipe et RecipeRequest, dans le panneau d'administration Strapi.

Une recette contient généralement les éléments suivants :

* Titre : `text` qui représente le titre de la recette

* Ingrédients : `text` qui représente les ingrédients de la recette

* Likes : `int` qui représente le nombre de likes

* Auteur : `relation` qui représente l'auteur de la recette

* Commentaires : `relation` qui représente la liste des commentaires d'une recette spécifique

* Étapes : `rich text` qui représente le contenu principal de la recette

* Description : `rich text` qui représente une description de la recette

* Nombre de Commentaires : `int` qui représente le nombre de commentaires qu'une recette a

* Image de Couverture : `media` qui représente l'image de couverture de la recette

![modèle de recette](https://cdn.hashnode.com/res/hashnode/image/upload/v1743504946186/e1be7d98-fff8-4e2e-b446-1ddbf541d1c0.png align="center")

Assurez-vous d'activer l'internationalisation pour le Type de Contenu Recipe lorsque vous le créez :

![activer l'internationalisation](https://cdn.hashnode.com/res/hashnode/image/upload/v1743504992503/73842540-4b8d-4412-9c51-1c55e095e83e.png align="center")

Une demande de recette contient généralement :

* Titre, qui est `text` représentant le titre de la demande

* Description, qui est `rich text` représentant le contenu de la demande

![modèle de demande de recette](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505019316/6d172672-af58-4a6d-b0a3-cb713ee32dd2.png align="center")

Un commentaire contient généralement :

* Auteur, qui est une `relation` représentant l'auteur du commentaire

* Contenu, qui est `text` représentant le contenu des commentaires

* Date, qui est une `date` représentant la date de publication du commentaire

![modèle de commentaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505036935/92d02ecb-9a86-43f9-99a9-a2a534aab871.png align="center")

L'utilisateur aura également 4 nouveaux champs :

![champs utilisateur supplémentaires](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505060587/cda0be86-298b-4053-b8ae-8c894e07a592.png align="center")

## Ajouter des Langues et Activer l'Internationalisation dans Strapi

L'application prendra en charge trois langues différentes (anglais, français et japonais). L'anglais est la langue par défaut, vous devez donc ajouter les deux autres. Dans le panneau Strapi, vous devrez naviguer vers Paramètres, puis Internationalisation et ajouter le français et le japonais. Je vais expliquer le processus en détail dans les sections suivantes.

## Ajouter du Contenu de Recette

Ensuite, vous allez remplir certaines données de recettes en anglais, français et japonais.

### Ajouter du Contenu de Recette en Anglais

Puisque l'anglais est la langue par défaut, allez dans le gestionnaire de contenu, puis sélectionnez Recipe, et ensuite sélectionnez **Créer une nouvelle entrée** :

![liste des recettes ajoutées](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505111608/3fb2d615-d649-4c22-8a73-87cbcbd38bdb.png align="center")

### Ajouter du Contenu de Recette en Français

Pour le français, naviguez vers Paramètres, sélectionnez Internationalisation, puis sous les paramètres globaux, cliquez sur **Ajouter une nouvelle locale**. Ici, vous ajouterez la langue française.

![configuration de la langue française](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505140738/a8e5b0d0-0871-46b1-8fb0-2921c84b913a.png align="center")

Retournez dans le gestionnaire de contenu, cliquez sur recette et sélectionnez la langue française dans le coin supérieur droit. Ensuite, choisissez **Créer une entrée de recette** en français.

![version du modèle français](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505164770/2ad75e5a-a20d-496d-9fe3-75fdc3cf64b1.png align="center")

### Ajouter du Contenu de Recette en Japonais

Retournez dans Paramètres et Internationalisation, et sous les paramètres globaux, cliquez à nouveau sur **Ajouter une nouvelle locale**. Maintenant, vous allez ajouter la langue japonaise.

![configuration de la langue japonaise](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505187987/91251e4e-4172-4ce5-9e53-78ca12352af4.png align="center")

Retournez dans le gestionnaire de contenu, cliquez sur recette et sélectionnez la langue japonaise dans le coin supérieur droit. Ensuite, sélectionnez **Créer une nouvelle entrée** en japonais.

![liste des recettes japonaises](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505218903/0e7b7025-8473-4012-ab54-130fe5b63164.png align="center")

## Générer un Jeton API et Définir les Permissions

Une fois que vous avez ajouté le contenu pour les différentes langues, il est temps de créer votre API et de définir les permissions nécessaires.

Pour ce faire, naviguez vers Paramètres, puis Jetons API, et ensuite Créer un Jeton API. Ajoutez les détails de votre clé ici.

![création de jeton API](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505239235/5a183f54-6469-4d4e-aa62-d81f4dccf8ae.png align="center")

* Durée du jeton : choisissez Illimité

* Type de jeton : Personnalisé. Le type personnalisé vous permet de spécifier les permissions pour certaines entités.

Ensuite, toujours dans l'écran de création de jeton API, faites défiler vers le bas jusqu'à la section des permissions et définissez les permissions sur "Sélectionner tout" pour les commentaires, RecipeRequest, upload, email, type de contenu, i18n, et les permissions utilisateur comme dans la capture d'écran ci-dessous pour Recipe-request :

![activer les permissions pour la demande de recette](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505260256/84f6f009-4c7a-4136-8497-6c22b9fa87de.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744116611459/f5518d2e-5200-40b3-9b74-ed0b0adeeabb.png align="center")

Ensuite, cliquez sur le bouton Enregistrer dans le coin supérieur droit pour générer votre clé API. Copiez et enregistrez la clé sur votre PC car vous ne pourrez plus la voir ensuite.

### Définir les Rôles et Permissions des Utilisateurs

Vous devrez également définir les rôles et permissions des utilisateurs en utilisant le [Plugin Utilisateurs et Permissions](https://docs.strapi.io/dev-docs/plugins/users-permissions). Il permet de gérer ce que les utilisateurs authentifiés et non authentifiés peuvent faire dans votre application.

Rendez-vous dans la section Paramètres du tableau de bord et allez dans Rôles sous le plugin Utilisateurs et Permissions.

Nous avons deux types d'utilisateurs :

* Utilisateurs authentifiés

* Utilisateurs publics

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744117848867/8023d7c4-c07b-43dc-ba00-89a958bc0672.png align="center")

Sélectionnez les utilisateurs authentifiés et donnez-leur les permissions suivantes pour :

Commentaire :

![activer les permissions pour les commentaires](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505301527/3939448a-48f4-44fc-baa9-a528a78e73c7.png align="center")

Recette :

![autoriser l'utilisateur à effectuer des actions sur le modèle de recette](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505327113/f9224713-105d-4cdb-9a5b-4846d1789b07.png align="center")

Demande de recette :

![activer les permissions pour le modèle de demande de recette](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505346092/d328c629-4ea9-40a0-baa6-90a96ae364ec.png align="center")

Sélectionnez également tout pour le générateur de type de contenu, i18n, et Upload, puis enregistrez.

Les utilisateurs publics ne peuvent que lire les recettes et les commentaires :

![limiter les opérations de commentaire pour les utilisateurs publics](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505362706/4d776b8f-84f9-4a41-a1d4-73b1a2fd6a4c.png align="center")

![limiter les opérations de recette pour les utilisateurs publics](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505369235/54ed5f73-9841-43bf-a088-0079358b6b05.png align="center")

## Configurer Flutter

Une fois que vous avez [configuré Flutter](https://docs.flutter.dev/get-started/install/windows/desktop)[r](https://docs.flutter.dev/get-started/install/windows/desktop) dans votre environnement, exécutez la commande suivante pour démarrer une nouvelle application dans votre répertoire préféré :

```bash
flutter create flutter_recipe_app
```

Pour voir votre application en action, vous devez l'exécuter sur un appareil mobile. Vous pouvez soit :

* Utiliser un **émulateur** (un appareil Android ou iOS virtuel qui s'exécute sur votre ordinateur), soit

* Connecter un **appareil physique** (comme votre smartphone) à votre ordinateur avec un câble USB.

Une fois que votre émulateur ou appareil est prêt, naviguez dans le dossier du projet nouvellement créé :

```bash
flutter run
```

Cette commande construit l'application et la démarre sur votre appareil connecté ou émulateur.

![application de démarrage flutter](https://cdn.hashnode.com/res/hashnode/image/upload/v1743505498936/6e1e461d-9fee-4e19-81e0-65d25ddebd63.png align="center")

### Structure du Projet

Examinons maintenant la structure des fichiers du projet :

```bash
flutter_recipe_app/
|
|-- .dart_tool/
|-- .idea/
|-- android/ [flutter_recipe_app_android]
|   |-- assets/
|   |   |-- images/
|   |   |-- translations/
|
|-- build/
|-- ios/
|-- lib/
|   |-- components/
|   |   |-- appBar.dart
|   |   |-- drawer.dart
|   |
|   |-- models/
|   |   |-- recipe.dart
|   |
|   |-- screens/
|   |   |-- detail.dart
|   |   |-- home.dart
|   |   |-- login.dart
|   |   |-- profile.dart
|   |   |-- requestRecipe.dart
|   |   |-- signUp.dart
|   |
|   |-- utils/
|       |-- server2.dart
|
|-- main.dart
|-- test/
|-- .env
```

La structure est organisée comme suit :

* `.dart_tool/` : Contient les outils Dart et les sorties de construction.

* `.idea/` : Paramètres spécifiques à l'IDE.

* `android/` : Fichiers de projet spécifiques à Android, y compris des assets personnalisés comme des images et des traductions.

* `build/` : Fichiers générés par le processus de construction.

* `ios/` : Fichiers de projet spécifiques à iOS.

* `lib/` : Le répertoire source principal pour le code Dart, qui inclut :

* `components/` : Widgets ou composants d'interface utilisateur réutilisables comme `appBar` et `drawer`.

* `models/` : Modèles de données pour votre application, comme `recipe`.

* `screens/` : Écrans individuels de l'application, tels que les écrans `recipe details`, `home`, `login`, `profile`, `request recipe` et `signUp` de l'application

* `utils/` : Utilitaires et fonctions d'assistance, comme `server2.dart` pour la logique de communication avec le serveur.

* `main.dart` : Le point d'entrée de l'application Flutter.

* `test/` : Répertoire pour les fichiers de test.

* `.env` : Fichier pour les variables spécifiques à l'environnement.

Cette configuration est typique pour une application Flutter modérément complexe, séparant les fonctionnalités en sections logiques et gérables pour une meilleure organisation et maintenabilité.

## Installer les Packages

Dans ce tutoriel, nous utilisons cinq packages principaux :

* [flutter\_dotenv](https://pub.dev/packages/flutter_dotenv) : pour gérer les variables d'environnement

* [http](https://pub.dev/packages/http) : pour gérer les requêtes HTTP et interagir avec [Strapi REST API](https://docs.strapi.io/dev-docs/api/rest)

* [shared\_preferences](https://pub.dev/packages/shared_preferences) : persiste les données clé-valeur sur l'appareil comme les jetons de connexion utilisateur

* [provider](https://pub.dev/packages/provider) : pour la gestion d'état et la mise à jour de votre interface utilisateur de manière réactive lorsque l'état sous-jacent change

* [easy\_localization](https://pub.dev/packages/easy_localization) : pour gérer les traductions et les données de localisation. Il prend en charge les formats de fichiers JSON et YAML pour définir les traductions.

Dans votre fichier `pubspec.yaml`, ajoutez les lignes suivantes :

```yaml
dependencies:
  flutter:
    ...
  flutter_dotenv: ^5.1.0
  http: ^1.1.0
  shared_preferences: ^2.2.2
  provider: ^6.1.2
  easy_localization: ^3.0.7
```

Ensuite, exécutez la commande suivante pour installer les packages :

```bash
flutter pub get
```

### Ajouter des Assets

Ajoutez le chemin vers vos assets dans votre fichier `pubspec.yaml` situé à la racine de votre projet :

```yaml
flutter:
  uses-material-design: true
  assets:
    - .env
    - assets/translations/
    - assets/images/
```

Le dossier translations contient la liste de vos traductions tandis que le dossier images héberge les photos de votre application.

### Examiner main.dart

Dans le fichier `main.dart`, vous devez configurer votre localisation, charger les variables d'environnement, et une liste de providers pour l'injection de dépendances :

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:flutter_recipe_app/screens/home.dart';
import 'package:flutter_recipe_app/screens/login.dart';
import 'package:flutter_recipe_app/screens/requestRecipe.dart';
import 'package:flutter_recipe_app/screens/signUp.dart';
import 'package:flutter_recipe_app/utils/server.dart';
import 'package:provider/provider.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

Future<void> main() async{
  // Assurez-vous que toutes les liaisons sont initialisées
  WidgetsFlutterBinding.ensureInitialized();
  await EasyLocalization.ensureInitialized();

  // Chargez les variables d'environnement
  await dotenv.load(fileName: ".env");
  runApp(EasyLocalization(
    supportedLocales: const [
      Locale('en'),
      Locale('fr', 'FR'),
      Locale('ja', 'JP')],
    path: 'assets/translations', //
    fallbackLocale: Locale('en'),
    child: MyApp(),
  ));
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        Provider(create: (_) => ApiService()),
      ],
      child: MaterialApp(
        title: tr('app_description'),
        localizationsDelegates: context.localizationDelegates,
        supportedLocales: context.supportedLocales,
        locale: context.locale,
        initialRoute: '/home',
        routes: {
          '/request': (context) => RecipeRequestScreen(),
          '/login': (context) => LoginScreen(),
          '/register': (context) => RegisterScreen(),
          '/home': (context) => HomeScreen(), // Implémenter HomeScreen
        },
      ),
    );
  }
}
```

Dans l'extrait de code ci-dessus, `WidgetsFlutterBinding.ensureInitialized()` garantit que toutes les liaisons Flutter sont initialisées avant toute autre opération et `EasyLocalization.ensureInitialized()` initialise le package EasyLocalization pour gérer les traductions.

Chargez les variables d'environnement avec `dotenv.load(fileName: ".env")` pour lire les variables depuis le fichier `.env`. La fonction `runApp` enveloppe le widget `MyApp` avec le widget `EasyLocalization`, qui est configuré pour prendre en charge les locales anglais (`en`), français (`fr_FR`), et japonais (`ja_JP`). Le chemin pour les fichiers de traduction est défini sur `'assets/translations'`, et la locale de secours est définie sur l'anglais.

Il crée également les routes principales de l'application de recettes et définit `home` comme route initiale.

## Ajouter des Variables d'Environnement

Vous allez stocker des données de configuration telles que les clés API, les URL spécifiques à l'environnement (URL de base, points de terminaison des recettes, points de terminaison des commentaires), et d'autres données sensibles ou configurables en dehors de votre base de code en utilisant le package `flutter_dotenv` que vous avez installé précédemment. Créez un fichier `.env` dans votre répertoire racine et ajoutez vos variables d'environnement :

```bash
BASE_URL=your-base-url
USERS_ENDPOINT=/auth/local
USERS_ENDPOINT_REG=/auth/local/register
ACCESS_TOKEN=your-api-key
RECIPE_ENDPOINT=/recipes
COMMENT_ENDPOINT=/comments
R_REQUEST_ENDPOINT=/recipe-requests
```

* `BASE_URL` : Il s'agit de l'URL de base pour votre serveur backend Strapi. Le `/api` signifie que tous les points de terminaison de l'API sont accessibles via ce chemin de base. Cette URL est utilisée pour construire des URL complètes pour toutes les requêtes API en ajoutant des points de terminaison spécifiques à celle-ci.

* `USERS_ENDPOINT` : Ce point de terminaison gère généralement les opérations de connexion où les utilisateurs existants s'authentifient en soumettant leurs identifiants.

* `USERS_ENDPOINT_REG` : Il s'agit du point de terminaison d'inscription pour les nouveaux utilisateurs.

* `ACCESS_TOKEN` : Il s'agit du jeton API que vous avez créé précédemment et qui est utilisé pour authentifier les requêtes API.

* `RECIPE_ENDPOINT` : Ce point de terminaison est utilisé pour récupérer une liste de recettes ou une seule recette. Vous pouvez également l'utiliser pour publier de nouvelles recettes, ou mettre à jour ou supprimer une recette.

* `COMMENT_ENDPOINT` : Ce point de terminaison gère les commentaires liés aux recettes.

* `R_REQUEST_ENDPOINT` : Ce point de terminaison gère les demandes liées aux recettes.

## Créer des Modèles

Ici, vous allez créer les différents modèles de l'application. Vous pouvez créer tous les modèles dans un seul fichier ou les créer dans des fichiers individuels. Dans ce tutoriel, nous allons créer tous les modèles dans un seul fichier qui est `lib/models/recipe.dart` :

```dart
import 'package:flutter_dotenv/flutter_dotenv.dart';

// modèles recipe_request
class RecipeRequest {
  final int id;
  final String title;
  final List<Description> description

  RecipeRequest({
    required this.id,
    required this.title,
    required this.description,
  });

  factory RecipeRequest.fromJson(Map<String, dynamic> json) {
    var attr = json['attributes'] ?? {};
    var attributes = json['attributes'] ?? {};
    List<Description> descriptionList = (attr['description'] as List? ?? [])
        .map((desc) => Description.fromJson(desc)).toList();

    print("Parsed Recipe: ${json['id']} - Descriptions: ${descriptionList.length}");

    return RecipeRequest(
      id: json['id'] ?? 0,
      title: attr['title'] ?? 'No title',
      description: descriptionList,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'title': title,
      'description': description.map((desc) => desc.toJson()).toList(),
      // 'id': id
    };
  }
}

// modèle d'étape

class Step {
  final String type;
  final List<TextContent> children;
  final int? level;

  Step({required this.type, required this.children, this.level});

  factory Step.fromJson(Map<String, dynamic> json) {
    var childrenList = json['children'] as List? ?? [];
    List<TextContent> parsedChildren = childrenList.map((child) => TextContent.fromJson(child)).toList();
    return Step(
      type: json['type'] ?? '',
      children: parsedChildren,
      level: json['level'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'type': type,
      'children': children.map((child) => child.toJson()).toList(),
      'level': level,
    };
  }
}

// modèle de description

class Description {
  final String type;
  final List<TextContent> children;
  final int? level;

  Description({required this.type, required this.children, this.level});

  factory Description.fromJson(Map<String, dynamic> json) {
    var childrenList = json['children'] as List? ?? [];
    List<TextContent> parsedChildren = childrenList.map((child) => TextContent.fromJson(child)).toList();
    return Description(
      type: json['type'] ?? '',
      children: parsedChildren,
      level: json['level'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'type': type,
      'children': children.map((child) => child.toJson()).toList(),
      'level': level,
    };
  }
}

class TextContent {
  final String type;
  final String text;
  final bool? bold;

  TextContent({required this.type, required this.text, this.bold});

  factory TextContent.fromJson(Map<String, dynamic> json) {
    return TextContent(
      type: json['type'] ?? '',
      text: json['text'] ?? '',
      bold: json['bold'] ?? false,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'type': type,
      'text': text,
      'bold': bold,
    };
  }
}

class Comment {
  final String content;
  final String author;
  final DateTime createdAt;

  Comment({
    required this.content,
    required this.author,
    required this.createdAt,
  });

  factory Comment.fromJson(Map<String, dynamic> json) {
    var attributes = json['attributes'] as Map<String, dynamic> ?? {};
    var authorData = attributes['comment_author']?['data']?['attributes'] ?? {};
    return Comment(
      content: attributes['content'] ?? 'No content',
      author: authorData['username'] ?? 'Unknown',
      createdAt: DateTime.parse(attributes['createdAt'] ?? DateTime.now().toString()),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'content': content,
      'author': author,
      'createdAt': createdAt.toIso8601String(),
    };
  }
}

//modèle de recette

class Recipe {
  final int id;
  final String title;
  final List<Description> description;
  final String ingredients;
  late int likes;
  final DateTime createdAt;
  final DateTime updatedAt;
  final DateTime publishedAt;
  final List<Step> steps;
  late int commentCount;
  final List<Comment> comments;
  final String coverImageUrl;

  Recipe({
    required this.id,
    required this.title,
    required this.description,
    required this.ingredients,
    required this.likes,
    required this.createdAt,
    required this.updatedAt,
    required this.publishedAt,
    required this.steps,
    required this.commentCount,
    required this.comments,
    required this.coverImageUrl
  });

  factory Recipe.fromJson(Map<String, dynamic> json) {
    var attr = json['attributes'] as Map<String, dynamic> ?? {};

    // Analyser les descriptions
    List<Description> descriptionList = [];
    if (attr['description'] != null && attr['description'] is List) {
      descriptionList = (attr['description'] as List).map((desc) => Description.fromJson(desc)).toList();
    }

    // Analyser les étapes
    List<Step> stepsList = [];
    if (attr['steps'] != null && attr['steps'] is List) {
      stepsList = (attr['steps'] as List).map((step) => Step.fromJson(step)).toList();
    }

    // Analyser les commentaires
    List<Comment> commentList = [];
    if (attr['comments'] != null && attr['comments']['data'] != null && attr['comments']['data'] is List) {
      commentList = (attr['comments']['data'] as List).map((comment) => Comment.fromJson(comment)).toList();
    }
    
    // var attr = json['attributes'] as Map<String, dynamic>;
    final String baseUrl = dotenv.env['BASE_URL']!;

    // Assurez-vous que l'URL de l'image est correctement préfixée
    String coverImageUrl = '';
    if (attr['cover'] != null && attr['cover']['data'] != null) {
      var imageUrl = attr['cover']['data']['attributes']['url'];
      coverImageUrl = imageUrl.startsWith('http')
          ? imageUrl
          : baseUrl + imageUrl; 
    }

    return Recipe(
        id: json['id'] ?? 0,
        title: attr['title'] ?? 'No title',
        description: descriptionList,
        ingredients: attr['ingredients'] ?? 'No ingredients',
        likes: attr['likes'] ?? 0,
        createdAt: DateTime.tryParse(attr['createdAt'] ?? DateTime.now().toIso8601String()) ?? DateTime.now(),
        updatedAt: DateTime.tryParse(attr['updatedAt'] ?? DateTime.now().toIso8601String()) ?? DateTime.now(),
        publishedAt: DateTime.tryParse(attr['publishedAt'] ?? DateTime.now().toIso8601String()) ?? DateTime.now(),
        steps: stepsList,
        commentCount: commentList.length,
        comments: commentList,
        coverImageUrl: coverImageUrl
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description.map((desc) => desc.toJson()).toList(),
      'ingredients': ingredients,
      'likes': likes,
      'createdAt': createdAt.toIso8601String(),
      'updatedAt': updatedAt.toIso8601String(),
      'publishedAt': publishedAt.toIso8601String(),
      'steps': steps.map((step) => step.toJson()).toList(),
      'commentCount': commentCount,
      'comments': comments.map((comment) => comment.toJson()).toList(),
      'cover': coverImageUrl
    };
  }
}
```

Passons en revue ce code morceau par morceau, car il est assez long :

### 1. **RecipeRequest**

La classe `RecipeRequest` représente la classe qui permet à un utilisateur de demander une recette. Elle possède trois propriétés (`id`, `title`, et une liste d'objets `Description` tels que définis dans le backend Strapi) avec 2 méthodes :

* `fromJson` : pour convertir les données JSON en un objet `RecipeRequest`, y compris l'analyse d'une liste de descriptions.

* `toJson` : pour convertir un objet `RecipeRequest` en JSON.

### 2. **Step**

Représente les étapes de cuisson dans une recette. Il contient une liste d'objets `Textcontent`, et chaque objet Step a un type, un niveau, et des enfants car il s'agit d'un type richtext. Il possède également deux méthodes :

* `fromJson` : pour analyser le JSON afin de créer un objet `Step`.

* `toJson` : pour convertir un objet `Step` en JSON.

### 3. **Description**

Cette classe contient également une liste d'objets `TextContent` (`children`). Chaque objet `Description` a également un `type` et un `level` optionnel pour indiquer une structure hiérarchique. Elle possède également deux méthodes :

* `fromJson` : pour convertir le JSON en un objet `Description`.

* `toJson` : pour sérialiser un objet `Description` en JSON.

### 4. **TextContent**

Cette classe est conçue pour représenter des morceaux individuels de texte au sein de structures plus grandes. Chaque objet `TextContent` peut contenir une chaîne de texte (`text`), le type de texte (`type`), et un booléen optionnel pour indiquer si le texte est en gras (`bold`)

* `fromJson` : Analyse le JSON en un objet `TextContent`.

* `toJson` : Convertit un objet `TextContent` en JSON.

### 5. **Comment**

Comme son nom l'indique, cela représente un commentaire écrit par un utilisateur. Il possède trois propriétés : le contenu du commentaire `content`, `author`, et `createdAt`. Comme les autres, il inclut également deux méthodes :

* `fromJson` : pour extraire et construire un objet `Comment` à partir de JSON, y compris l'analyse des données de l'auteur.

* `toJson` : pour sérialiser un objet `Comment` en JSON.

### 6. **Recipe**

Enfin, il y a la classe `Recipe` qui est l'objet principal de la recette. Elle contient divers détails sur une recette, y compris l'id, le titre, les descriptions, les ingrédients, les likes, les timestamps, les étapes, le nombre de commentaires, la liste des commentaires, et une URL d'image de couverture. Nous avons :

* `fromJson` : pour construire un objet `Recipe` à partir de données JSON. Cela inclut l'analyse des listes de descriptions, d'étapes et de commentaires. Il ajuste également l'URL de l'image pour s'assurer qu'elle est absolue.

* `toJson` : pour convertir l'objet `Recipe` en format JSON.

Comme vous pouvez le voir, chaque classe est conçue pour gérer des parties spécifiques des données de la recette, avec des méthodes `fromJson` pour analyser le JSON en objets Dart et des méthodes `toJson` pour sérialiser les objets Dart en JSON.

## Créer des Services

Maintenant que vos variables d'environnement sont configurées, vous pouvez créer différents services pour communiquer avec le serveur. Dans votre fichier `lib/utils/server.dart`, ajoutez le code ci-dessous :

```dart
import 'dart:convert';
import 'dart:developer';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:easy_localization/easy_localization.dart';
import '../models/recipe.dart';

class ApiService {
  final String baseUrl = dotenv.env['BASE_URL']!;
  final String registerEndpoint = dotenv.env['USERS_ENDPOINT_REG']!;
  final String loginEndpoint = dotenv.env['USERS_ENDPOINT']!;
  final String accessToken = dotenv.env['ACCESS_TOKEN']!;
  final String recipeEndpoint = dotenv.env['RECIPE_ENDPOINT']!;
  final String commentEndpoint = dotenv.env['COMMENT_ENDPOINT']!;
  final String requestEndpoint = dotenv.env['R_REQUEST_ENDPOINT']!;

  // Méthode d'assistance pour obtenir les en-têtes avec un jeton JWT optionnel
  Future<Map<String, String>> _getHeaders({bool includeJwt = false}) async {
    final headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer $accessToken",
    };
    if (includeJwt) {
      final jwt = await getJwt();
      if (jwt != null) {
        headers["Authorization"] = "Bearer $jwt";
      }
    }
    return headers;
  }

  // Obtenir le JWT
  Future<String?> getJwt() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString('jwt');
  }

  // Définir le JWT
  Future<void> setJwt(String jwt) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('jwt', jwt);
  }

  // Supprimer le JWT
  Future<void> removeJwt() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('jwt');
  }

  // Définir les données de l'utilisateur
  Future<void> setUserData(Map<String, dynamic> data) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('userId', data['user']['id'].toString());
    await prefs.setString('username', data['user']['username']);
  }

  // Supprimer les données de l'utilisateur
  Future<void> removeUserData() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('userId');
    await prefs.remove('username');
  }

  // Inscription de l'utilisateur
  Future<http.Response> register(String username, String email, String password) async {
    final url = Uri.parse('$baseUrl$registerEndpoint');
    try {
      final response = await http.post(
        url,
        headers: await _getHeaders(),
        body: json.encode({
          "username": username,
          "email": email,
          "password": password,
        }),
      );
      return response;
    } catch (e) {
      log("Error registering user: $e");
      rethrow;
    }
  }

  // Connexion de l'utilisateur
  Future<http.Response> login(String email, String password) async {
    final url = Uri.parse('$baseUrl$loginEndpoint');
    try {
      final response = await http.post(
        url,
        headers: await _getHeaders(),
        body: json.encode({
          "identifier": email,
          "password": password,
        }),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        await setJwt(data['jwt']);
        await setUserData(data);
      }

      return response;
    } catch (e) {
      log("Error logging in user: $e");
      rethrow;
    }
  }

  // Déconnexion de l'utilisateur
  Future<void> logout() async {
    await removeJwt();
    await removeUserData();
  }

  // Récupérer les recettes
  Future<List<Recipe>> fetchRecipes(BuildContext context) async {
    final String localeCode = context.locale.toString().replaceAll('_', '-');
    final String lang = localeCode == 'en' ? 'en' : localeCode;
    final url = Uri.parse('$baseUrl$recipeEndpoint?locale=$lang&populate=*');
    final response = await http.get(url);

    if (response.statusCode == 200) {
      var jsonResponse = jsonDecode(response.body);
      List<dynamic> dataList = jsonResponse['data'];
      List<Recipe> recipes = [];

      for (var item in dataList) {
        try {
          recipes.add(Recipe.fromJson(item));
        } catch (e) {
          print('Failed to parse item: $e');
          print('Item data: $item');
        }
      }

      return recipes;
    } else {
      throw Exception('Failed to load recipes: HTTP ${response.statusCode}');
    }
  }

  // Récupérer les commentaires
    Future<List<Comment>> fetchComments(int recipeId) async {
    final url = Uri.parse('$baseUrl$commentEndpoint?filters[recipe][id][\$eq]=$recipeId&populate=comment_author');
    try {
      final response = await http.get(url, headers: await _getHeaders());
      print('Response fetch status: ${response.statusCode}');
      print('Response fetch body: ${response.body}');

      if (response.statusCode == 200) {
        var jsonData = jsonDecode(response.body);
        print("Parsed JSON: $jsonData");

        if (jsonData != null && jsonData.containsKey('data')) {
          List<dynamic> data = jsonData['data'];
          return data.map<Comment>((json) {
            if (json == null || json['attributes'] == null) {
              print('json or json[\'attributes\'] is null');
              return Comment(content: 'Invalid', author: 'Invalid', createdAt: DateTime.now());
            }
            return Comment.fromJson(json);
          }).toList();
        } else {
          print('Data field is missing or null in the response');
          return [];
        }
      } else {
        print('Failed to load comments with status code: ${response.statusCode}');
        return [];
      }
    } catch (e) {
      print('Error server fetching comments: $e');
      throw Exception('Error fetching comments: $e');
    }
  }

  Future<Comment> postComment(String content, int recipeId, String authorId) async {
    final url = Uri.parse('$baseUrl$commentEndpoint?populate=comment_author');
    try {
      final response = await http.post(
        url,
        headers: await _getHeaders(),
        body: json.encode({
          "data": {
            "content": content,
            "recipe": recipeId,
            "comment_author": authorId,
          },
        }),
      );
      print('Post comment response status: ${response.statusCode}');
      print('Post comment response body: ${response.body}');

      if (response.statusCode == 200 || response.statusCode == 201) {
        var jsonData = jsonDecode(response.body);
        return Comment.fromJson(jsonData['data']);
      } else {
        throw Exception('Failed to post comment');
      }
    } catch (e) {
      log("Error posting comment: $e");
      rethrow;
    }
  }

  Future<void> updateCommentCount(int recipeId, {required bool increment}) async {
    final recipeUrl = Uri.parse('$baseUrl$recipeEndpoint/$recipeId');
    try {
      // Récupérer les données actuelles de la recette
      final recipeResponse = await http.get(recipeUrl, headers: await _getHeaders());
      print('Fetch recipe response status: ${recipeResponse.statusCode}');
      print('Fetch recipe response body: ${recipeResponse.body}');

      if (recipeResponse.statusCode == 200) {
        var recipeData = jsonDecode(recipeResponse.body)['data'];
        int currentComments = recipeData['attributes']['comments'] ?? 0;
        int updatedComments = increment ? currentComments + 1 : currentComments - 1;

        // Assurez-vous que updatedComments n'est pas négatif
        if (updatedComments < 0) {
          updatedComments = 0;
        }

        // Mettre à jour la recette avec le nouveau nombre de commentaires
        final updateResponse = await http.put(
          recipeUrl,
          headers: await _getHeaders(),
          body: json.encode({
            "data": {
              "comments": updatedComments,
            },
          }),
        );

        print('Update recipe response status: ${updateResponse.statusCode}');
        print('Update recipe response body: ${updateResponse.body}');

        if (updateResponse.statusCode != 200) {
          throw Exception('Failed to update comment count');
        }
      } else {
        throw Exception('Failed to fetch recipe data');
      }
    } catch (e) {
      log("Error updating comment count: $e");
      throw Exception('Error updating comment count: $e');
    }
  }

  // Aimer une recette
  Future<void> likeRecipe(int recipeId) async {
    final recipeUrl = Uri.parse('$baseUrl$recipeEndpoint/$recipeId');
    try {
      // Récupérer les données actuelles de la recette
      final recipeResponse = await http.get(recipeUrl, headers: await _getHeaders());
      if (recipeResponse.statusCode == 200) {
        var recipeData = jsonDecode(recipeResponse.body)['data'];
        int currentLikes = recipeData['attributes']['likes'] ?? 0;
        int updatedLikes = currentLikes + 1;

        // Mettre à jour la recette avec le nouveau nombre de likes
        final updateResponse = await http.put(
          recipeUrl,
          headers: await _getHeaders(),
          body: json.encode({
            "data": {
              "likes": updatedLikes,
            },
          }),
        );

        if (updateResponse.statusCode != 200) {
          throw Exception('Failed to update likes count');
        }
      } else {
        throw Exception('Failed to fetch recipe data');
      }
    } catch (e) {
      log("Error liking recipe: $e");
      throw Exception('Error liking recipe: $e');
    }
  }

  // Soumettre une demande de recette
  Future<void> submitRecipeRequest(RecipeRequest r_request) async {
    final url = Uri.parse('$baseUrl$requestEndpoint');

    try {
      final response = await http.post(
        url,
        headers: await _getHeaders(includeJwt: true),
        body: jsonEncode({
          'data': r_request.toJson(), // Envelopper la demande dans un objet 'data'
        }),
      );
      print('Response status code: ${response.statusCode}');
      print('Response body: ${response.body}');
      if (response.statusCode != 200 && response.statusCode != 201) {
        throw Exception('Failed to submit recipe request');
      }
    } catch (e) {
      print("Error submitting recipe request: $e");
      rethrow;
    }
  }

  // Récupérer les recettes demandées par l'utilisateur
  Future<List<RecipeRequest>> fetchUserRequestedRecipes() async {
    final url = Uri.parse('$baseUrl$requestEndpoint');
    try {
      final response = await http.get(
        url,
        headers: await _getHeaders(includeJwt: true),
      );
      print('Response status code: ${response.statusCode}');
      print('Response body: ${response.body}');

      if (response.statusCode == 200) {
        var jsonResponse = jsonDecode(response.body);
        List<dynamic> data = jsonResponse['data'];
        return data.map((json) => RecipeRequest.fromJson(json)).toList();
      } else {
        throw Exception('Failed to load user requested recipes');
      }
    } catch (e) {
      print("Error fetching user requested recipes: $e");
      rethrow;
    }
  }
}
```

La classe `ApiService` du code ci-dessus est un utilitaire pour gérer diverses opérations liées à l'authentification des utilisateurs et à la récupération de données depuis un serveur backend. Ce service utilise des requêtes HTTP pour communiquer avec le serveur Strapi.

Il existe quatre entités principales :

### 1. Variables de Classe

* `baseUrl` est l'URL de base.

* `registerEndpoint`, `loginEndpoint`, `recipeEndpoint`, `commentEndpoint`, `requestEndpoint` sont les points de terminaison spécifiques pour l'inscription, la connexion, les recettes, les commentaires et les demandes.

* `accessToken` est le jeton utilisé pour l'authentification de l'API.

### 2. Méthodes d'Assistance

* `_getHeaders` prépare les en-têtes pour les requêtes HTTP et inclut optionnellement un jeton JWT si `includeJwt` est vrai.

* `getJwt` récupère le jeton JWT depuis les préférences partagées.

* `setJwt` et `setUserData` stockent le jeton JWT et les données de l'utilisateur (ID et nom d'utilisateur) dans les préférences partagées une fois que l'utilisateur se connecte.

* `removeJwt` et `removeUserData` suppriment le jeton JWT et les données de l'utilisateur des préférences partagées, respectivement, et déconnectent l'utilisateur.

### 3. Opérations Utilisateur

* `register` inscrit un nouvel utilisateur avec le nom d'utilisateur, l'email et le mot de passe donnés. Il envoie une requête POST au point de terminaison d'inscription avec les détails de l'utilisateur.

* `login` connecte un utilisateur avec l'email et le mot de passe donnés. Si cela réussit, il stocke le jeton JWT reçu et les données de l'utilisateur.

* `logout` déconnecte l'utilisateur en supprimant le jeton JWT et les données de l'utilisateur des préférences partagées.

### 4. Récupération et Manipulation des Données

* `fetchRecipes` récupère une liste de recettes basée sur la locale (langue) actuelle depuis le backend. Il gère l'analyse de la réponse JSON en une liste d'objets `Recipe`.

* `fetchComments` récupère les commentaires pour une recette spécifique par son ID. Il remplit le champ `comment_author` et retourne une liste d'objets `Comment`.

* `postComment` publie un nouveau commentaire sur une recette spécifique. Il envoie le contenu du commentaire, l'ID de la recette et l'ID de l'auteur au backend.

* `updateCommentCount` met à jour le nombre de commentaires pour une recette spécifique. Il récupère d'abord le nombre actuel, le modifie, puis le met à jour sur le backend.

* `likeRecipe` : Incrémente le nombre de likes pour une recette spécifique en récupérant le nombre actuel, en ajoutant un, et en mettant à jour le backend.

* `submitRecipeRequest` soumet une nouvelle demande de recette au backend. Il envoie les données de la demande enveloppées dans un objet `data`.

* `fetchUserRequestedRecipes` récupère une liste de recettes demandées par un utilisateur spécifique depuis le backend.

## Autorisation et Authentification

L'autorisation est ce qui permet à un utilisateur d'accéder à une ressource particulière et détermine si un utilisateur peut effectuer certaines actions au sein de l'application comme commenter une recette, aimer une recette, ou demander une recette.

D'autre part, l'authentification est le processus de validation et de vérification d'un utilisateur.

Il existe de nombreuses méthodes d'autorisation et d'authentification, mais dans ce tutoriel, nous utiliserons l'authentification basée sur un mot de passe et une clé API pour l'autorisation.

### Inscription

Dans le fichier `lib/screen/signUp.dart`, ajoutez le code ci-dessous :

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../utils/server2.dart';
import 'login.dart';

class RegisterScreen extends StatefulWidget {
  @override
  _RegisterScreenState createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final _formKey = GlobalKey<FormState>();
  bool _isLoading = false;

  @override
  void dispose() {
    usernameController.dispose();
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  Future<void> _register() async {
    if (_formKey.currentState!.validate()) {
      setState(() {
        _isLoading = true;
      });

      final response = await Provider.of<ApiService>(context, listen: false)
          .register(usernameController.text, emailController.text, passwordController.text);

      setState(() {
        _isLoading = false;
      });

      if (response.statusCode == 200) {
        // Naviguer vers l'écran de connexion après une inscription réussie
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (_) => LoginScreen()),
        );
      } else {
        // Gérer l'erreur
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: Text(tr('register_fail')),
            content: Text(tr('register_error')),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text(tr('ok')),
              ),
            ],
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(tr('register'))),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: usernameController,
                decoration: InputDecoration(labelText: tr('username')),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return tr('username_required');
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: emailController,
                decoration: InputDecoration(labelText: tr('email')),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return tr('email_required');
                  } else if (!RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(value)) {
                    return tr('email_invalid');
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: passwordController,
                decoration: InputDecoration(labelText: tr('password')),
                obscureText: true,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return tr('password_required');
                  }
                  return null;
                },
              ),
              SizedBox(height: 20),
              _isLoading
                  ? CircularProgressIndicator()
                  : ElevatedButton(
                onPressed: _register,
                child: Text(tr('register')),
              ),
              TextButton(
                onPressed: () {
                  // Naviguer vers l'écran de connexion
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(builder: (_) => LoginScreen()),
                  );
                },
                child: Text(
                  tr("have_account"),
                  style: const TextStyle(fontSize: 16),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Ce code fournit une interface d'inscription conviviale pour l'application de recettes. La classe `RegisterScreen` est un widget avec état qui gère le processus d'inscription.

La méthode `_register` valide le formulaire et appelle la méthode `register` de `ApiService`. Si l'inscription réussit (indiquée par un code de statut HTTP 200), elle redirige vers l'écran de connexion. Si elle échoue, une boîte de dialogue d'erreur est affichée avec un message.

Le code ci-dessus utilise également la validation de formulaire pour s'assurer que les utilisateurs entrent des informations valides. Les champs nom d'utilisateur et mot de passe ne doivent pas être vides, et le champ email doit suivre un format d'email approprié.

Lors de la soumission, le formulaire affiche un indicateur de chargement pendant que l'application communique avec le serveur pour inscrire l'utilisateur.

L'état du formulaire est géré à l'aide d'une GlobalKey, et les contrôleurs pour les champs de texte sont correctement supprimés pour libérer des ressources lorsque le widget est retiré de l'arbre.

### Connexion

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../utils/server2.dart';
import 'signUp.dart';

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final _formKey = GlobalKey<FormState>();
  bool _isLoading = false;

  @override
  void dispose() {
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  Future<void> _login() async {
    if (_formKey.currentState!.validate()) {
      setState(() {
        _isLoading = true;
      });

      final response = await Provider.of<ApiService>(context, listen: false)
          .login(emailController.text, passwordController.text);

      setState(() {
        _isLoading = false;
      });

      if (response.statusCode == 200) {
        Navigator.pushReplacementNamed(context, '/home');
      } else {
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: Text(tr('login_failed')),
            content: Text(tr('invalid_email_password')),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text(tr('ok')),
              ),
            ],
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(tr('login'))),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: emailController,
                decoration: InputDecoration(labelText: tr('email')),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return tr('email_required');
                  } else if (!RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(value)) {
                    return tr('email_invalid');
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: passwordController,
                decoration: InputDecoration(labelText: tr('password')),
                obscureText: true,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return tr('password_required');
                  }
                  return null;
                },
              ),
              SizedBox(height: 20),
              _isLoading
                  ? CircularProgressIndicator()
                  : ElevatedButton(
                      onPressed: _login,
                      child: Text(tr('login')),
                    ),
              TextButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (_) => RegisterScreen()),
                  );
                },
                child: Text(
                  tr("dont_have_account"),
                  style: const TextStyle(fontSize: 16),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Le `LoginScreen` contient deux champs de saisie pour l'email et le mot de passe de l'utilisateur, et il valide les entrées avant de tenter de se connecter. Lorsque l'utilisateur soumet le formulaire, l'application vérifie si l'entrée est valide. Si elle est valide, elle définit un indicateur de chargement et envoie une requête de connexion à l'API backend.

Si la connexion réussit, l'application navigue vers l'écran d'accueil, tandis que si la connexion échoue, une boîte de dialogue d'alerte est affichée pour informer l'utilisateur de l'email ou du mot de passe invalide. Le formulaire utilise également une `GlobalKey` pour gérer son état et s'assure que les contrôleurs de texte sont correctement supprimés lorsque le widget est retiré de l'arbre.

## Créer des Composants d'Application

### Drawer

Le Drawer est un panneau latéral qui glisse depuis la gauche (par défaut) et fournit des options de navigation pour l'utilisateur. C'est un excellent moyen d'organiser les sections de votre application sans encombrer l'écran principal.

Dans notre application, le drawer inclura des liens vers l'écran de demande de recette, le profil, la déconnexion et les langues pour les utilisateurs authentifiés.

Dans le fichier `lib/components/drawer.dart`, ajoutez le code ci-dessous :

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../screens/profile.dart';
import '../screens/requestRecipe.dart';

class CustomDrawer extends StatefulWidget {
  @override
  _CustomDrawerState createState() => _CustomDrawerState();
}

class _CustomDrawerState extends State<CustomDrawer> {
  bool _isAuthenticated = false;
  String? _username;
  String? _userId;

  @override
  void initState() {
    super.initState();
    _checkAuthentication();
  }

  Future<void> _checkAuthentication() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _isAuthenticated = prefs.containsKey('jwt');
      _username = prefs.getString('username');
      _userId = prefs.getString('userId');
    });
  }

  void _navigateToLogin() {
    Navigator.pushReplacementNamed(context, '/login');
  }

  Future<void> _logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.clear();
    setState(() {
      _isAuthenticated = false;
      _username = null;
      _userId = null;
    });
    Navigator.pushReplacementNamed(context, '/login');
  }

  void _changeLanguage(Locale locale) {
    context.setLocale(locale);
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          DrawerHeader(
            decoration: BoxDecoration(
              color: Colors.blue,
            ),
            child: Text(
              _isAuthenticated ? tr('hello', namedArgs: {'username': _username ?? ''}) : tr('welcome'),
              style: TextStyle(
                color: Colors.white,
                fontSize: 24,
              ),
            ),
          ),
          if (_isAuthenticated)
            ListTile(
              leading: Icon(Icons.request_page),
              title:Text(tr('request_recipe')),
              onTap: () {

                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => RecipeRequestScreen()),

                );
              },
            ),
          if (_isAuthenticated)
            ListTile(
              leading: const Icon(Icons.person),
              title: Text(tr('profile')),
              onTap: () {
                if (_userId != null) {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => ProfileScreen()),
                  );
                }
              },
            ),
          if (_isAuthenticated)
            ListTile(
              leading: Icon(Icons.logout),
              title: Text(tr('logout')),
              onTap: _logout,

            )
          else
            ListTile(
              leading: Icon(Icons.login),
              title: Text(tr('login')),
              onTap: _navigateToLogin,
            ),
          Divider(),
          ListTile(
            leading: SizedBox(
              width: 24.0,
              height: 24.0,
              child: Image.asset(
                'assets/images/en-flag.jpg',
              ),
            ),
            title: Text(tr('english')),
            onTap: () {
              Navigator.pop(context);
              _changeLanguage(Locale('en'));
    },
          ),
          ListTile(
            leading: SizedBox(
              width: 24.0,
              height: 24.0,
              child: Image.asset(
                'assets/images/fr-flag.jpg',
              ),
            ),
            title: Text(tr('french')),
            onTap: () {
              Navigator.pop(context);
              _changeLanguage(Locale('fr', 'FR'));
            },
          ),
          ListTile(
            leading: SizedBox(
              width: 24.0,
              height: 24.0,
              child: Image.asset(
                'assets/images/ja-flag.jpg',
              ),
            ),
            title: Text(tr('japanese')),
            onTap: () {
              Navigator.pop(context);
              _changeLanguage(Locale('ja', 'JP'));
            },
          ),
        ],
      ),
    );
  }
}
```

Le `CustomDrawer` donne aux utilisateurs accès à différentes parties de l'application et leur permet de changer de langue. Il met à jour son contenu en fonction de l'état de connexion de l'utilisateur. Les utilisateurs connectés voient des options comme « Demander une Recette », « Profil » et « Déconnexion », tandis que les invités ne voient qu'une option « Connexion ». Il personnalise l'expérience utilisateur en saluant les utilisateurs connectés avec leur nom d'utilisateur.

Il inclut également un sélecteur de langue avec des icônes de drapeaux pour l'anglais, le français et le japonais, alimenté par le package `easy_localization`. Cela permet aux utilisateurs de changer la langue de l'application instantanément.

Au démarrage, le drawer vérifie l'état d'authentification de l'utilisateur en utilisant `SharedPreferences` et ajuste l'interface utilisateur en conséquence. La navigation est gérée avec `Navigator`, permettant des transitions fluides vers différents écrans en fonction de l'élément de menu sélectionné.

### AppBar

L'AppBar est la barre supérieure de l'écran de votre application. Elle contient généralement le titre de l'application, un bouton de retour (si nécessaire), et parfois des actions comme la recherche, les paramètres, ou un basculement de langue. Dans notre application multilingue de recettes, nous utiliserons l'`AppBar` pour afficher le titre de la page actuelle et permettre une navigation facile à travers le drawer.

Dans le fichier `lib/components/appBar.dart`, ajoutez le code ci-dessous :

```dart
import 'package:flutter/material.dart';

/// Une AppBar personnalisable pour l'application de recettes.
///
/// Cette AppBar permet de définir un titre, des actions, un widget principal,
/// centrer le titre, la couleur de fond et l'élévation.
class RecipeBar extends StatelessWidget implements PreferredSizeWidget {
  final String title;
  final List<Widget>? actions;
  final Widget? leading;
  final bool centerTitle;
  final Color? backgroundColor;
  final double elevation;

  const RecipeBar({
    required this.title,
    this.actions,
    this.leading,
    this.centerTitle = true,
    this.backgroundColor,
    this.elevation = 4.0,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Text(title),
      actions: actions,
      leading: leading,
      centerTitle: centerTitle,
      backgroundColor: backgroundColor,
      elevation: elevation,
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}
```

L'AppBar utilise un `StatelessWidget` puisqu'il ne gère aucun état qui change au fil du temps. Il implémente l'interface `PreferredSizeWidget`, qui est nécessaire pour la personnalisation de l'AppBar dans Flutter.

Le constructeur de la classe `RecipeBar` prend plusieurs paramètres pour personnaliser l'AppBar. Le paramètre `title` est requis, tandis que les autres sont optionnels avec des valeurs par défaut. Le paramètre `actions` permet d'ajouter des widgets comme des boutons pour la connexion, le changement de langue, ou simplement la navigation vers un autre écran de l'application.

Dans la méthode `build`, l'AppBar est construite en utilisant les paramètres fournis. Le getter `preferredSize` retourne la hauteur préférée de l'AppBar, qui est définie sur la hauteur standard de la barre d'outils en utilisant `kToolbarHeight`. Cette classe fournit un composant AppBar flexible et réutilisable pour l'application de recettes, permettant une personnalisation facile et une conception d'interface utilisateur cohérente sur différents écrans.

## Récupérer les Recettes

Dans le fichier `lib/screens/home.dart`, ajoutez le code ci-dessous :

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../components/drawer.dart';
import '../models/recipe.dart';
import '../utils/server2.dart';
import 'detail.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late Future<List<Recipe>> _recipesFuture;
  bool _isAuthenticated = false;
  String? _username;

  @override
  void initState() {
    super.initState();
    _checkAuthentication(); // Vérifier l'état d'authentification lors de l'initialisation
  }

  Future<void> _checkAuthentication() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _isAuthenticated = prefs.containsKey('jwt'); // Vérifier si le jeton JWT est stocké
      _username = prefs.getString('username'); // Obtenir le nom d'utilisateur de l'utilisateur connecté depuis les préférences partagées
    });
  }

  void _navigateToLogin() {
    Navigator.pushReplacementNamed(context, '/login');
  }

  // Méthode de déconnexion
  Future<void> _logout() async {
    await ApiService().logout();
    setState(() {
      _isAuthenticated = false;
      _username = null;
    });
    Navigator.pushReplacementNamed(context, '/login');
  }

  String truncateWithEllipsis(int cutoff, String myString) {
    return (myString.length <= cutoff) ? myString : '${myString.substring(0, cutoff)}...';
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // Initialiser _recipesFuture après que le contexte soit disponible
    _recipesFuture = ApiService().fetchRecipes(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(tr('recipe_list')),
        actions: [
          if (_isAuthenticated)
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Center(
                child: Text(tr('hello', namedArgs: {'username': _username ?? ''})),
              ),
            ),
          if (_isAuthenticated)
            IconButton(
              icon: const Icon(Icons.logout),
              onPressed: _logout,
            )
          else
            TextButton(
              onPressed: _navigateToLogin,
              child: Text(
                tr('login'),
                style: const TextStyle(color: Colors.white),
              ),
            ),
        ],
      ),
      drawer: CustomDrawer(),
      body: FutureBuilder<List<Recipe>>(
        future: _recipesFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error.toString()}'));
          } else if (snapshot.data == null || snapshot.data!.isEmpty) {
            return Center(child: Text(tr('no_recipe')));
          }

          return ListView.builder(
            itemCount: snapshot.data!.length,
            itemBuilder: (context, index) {
              Recipe recipe = snapshot.data![index];
              String fullDescription = recipe.description.isNotEmpty
                  ? recipe.description.map((d) => d.children.map((t) => t.text).join(' ')).join('\n')
                  : tr('no_description');
              String truncatedDescription = truncateWithEllipsis(100, fullDescription);

              print("Recipe Title: ${recipe.title}");
              print("Full Description: $fullDescription");

              return GestureDetector(
                onTap: () async {
                  final result = await Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => RecipeDetailPage(recipe: recipe),
                    ),
                  );

                  if (result != null && result is Map<String, int>) {
                    setState(() {
                      Recipe updatedRecipe = Recipe(
                        id: recipe.id,
                        title: recipe.title,
                        description: recipe.description,
                        ingredients: recipe.ingredients,
                        likes: result['likes']!,
                        createdAt: recipe.createdAt,
                        updatedAt: recipe.updatedAt,
                        publishedAt: recipe.publishedAt,
                        steps: recipe.steps,
                        commentCount: result['commentsCount']!,
                        comments: recipe.comments,
                        coverImageUrl: recipe.coverImageUrl,
                      );
                      snapshot.data![index] = updatedRecipe;
                    });
                  }
                },
                child: Container(
                  margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(15),
                    border: Border.all(
                      color: const Color(0xff595959),
                      width: 0.5,
                    ),
                  ),
                  child: Row(
                    children: [
                      Container(
                        height: 80,
                        width: 80,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(15),
                          image: DecorationImage(
                            image: NetworkImage(recipe.coverImageUrl),
                            fit: BoxFit.cover,
                          ),
                        ),
                      ),
                      const SizedBox(width: 10),
                      Expanded(
                        flex: 3,
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              recipe.title.toUpperCase(),
                              style: const TextStyle(fontWeight: FontWeight.bold),
                            ),
                            const SizedBox(height: 5),
                            Text(
                              truncatedDescription,
                              style: const TextStyle(color: Color(0xff595959)),
                            ),
                            const SizedBox(height: 5),
                            Row(
                              children: [
                                Expanded(
                                  child: Row(
                                    children: [
                                      Text('${recipe.likes}'),
                                      const SizedBox(width: 5),
                                      const Icon(Icons.thumb_up, size: 18, color: Colors.redAccent),
                                    ],
                                  ),
                                ),
                                Expanded(
                                  child: Row(
                                    children: [
                                      Text('${recipe.commentCount}'),
                                      const SizedBox(width: 5),
                                      const Icon(Icons.comment, size: 18, color: Colors.blue),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              );
            },
          );
        },
      ),
    );
  }
}
```

Le `HomeScreen` affiche principalement une liste de recettes. Il vérifie si l'utilisateur est authentifié en recherchant un jeton JWT dans les préférences partagées et définit l'état d'authentification en conséquence. Si l'utilisateur est authentifié, il affiche un message de bienvenue avec son nom d'utilisateur et fournit une option de déconnexion dans la barre d'application.

Le `FutureBuilder` pour récupérer les recettes depuis `ApiService`. Pendant que les données sont en cours de récupération, il affiche un indicateur de chargement. Une fois les données récupérées, il affiche la liste des recettes. Chaque carte de recette inclut le titre, la description tronquée, l'image de couverture, et les comptes de likes et de commentaires.

Lorsque l'utilisateur appuie sur une recette, il navigue vers une page détaillée pour cette recette. Si la page détaillée met à jour les likes ou les commentaires de la recette, la liste se met à jour en conséquence sans recharger tout l'écran.

## Voir la Recette

Dans le fichier `lib/screens/detail.dart`, ajoutez le code ci-dessous :

```dart
import 'dart:developer';
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/recipe.dart';
import '../utils/server2.dart';

class RecipeDetailPage extends StatefulWidget {
  final Recipe recipe;

  const RecipeDetailPage({Key? key, required this.recipe}) : super(key: key);

  @override
  _RecipeDetailPageState createState() => _RecipeDetailPageState();
}

class _RecipeDetailPageState extends State<RecipeDetailPage> {
  final _commentController = TextEditingController();
  List<Comment> _comments = [];
  bool _isLoading = true;
  bool _isAuthenticated = false;
  String? _userId;
  int _likes = 0;
  int _commentsCount = 0;

  @override
  void initState() {
    super.initState();
    _initializePage();
  }

  Future<void> _initializePage() async {
    _checkAuthentication();
    _loadComments();
    _likes = widget.recipe.likes;
    _comments = widget.recipe.comments;
    _commentsCount = widget.recipe.commentCount;
    _commentController.addListener(() => setState(() {}));
  }

  @override
  void dispose() {
    _commentController.dispose();
    super.dispose();
  }

  Future<void> _checkAuthentication() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _isAuthenticated = prefs.containsKey('jwt');
      _userId = prefs.getString('userId');
    });
  }

  void _showError(String message) {
    final snackBar = SnackBar(content: Text(message));
    ScaffoldMessenger.of(context).showSnackBar(snackBar);
  }

  Future<void> _loadComments() async {
    try {
      var comments = await ApiService().fetchComments(widget.recipe.id);
      setState(() {
        _comments = comments;
        _commentsCount = comments.length;
        _isLoading = false;
      });
    } catch (e) {
      log('Error server fetching comments: $e');
      _showError('Failed to load comments: $e');
      setState(() => _isLoading = false);
    }
  }

  Future<void> _addComment() async {
    if (_commentController.text.isNotEmpty && _userId != null) {
      try {
        Comment newComment = await ApiService().postComment(
            _commentController.text, widget.recipe.id, _userId!);

        setState(() {
          _comments.add(newComment);
          _commentsCount++;
          _commentController.clear();
        });

        await ApiService().updateCommentCount(widget.recipe.id, increment: true);
      } catch (e) {
        log("Error posting comment: $e");
        _showError('Error posting comment: $e');
      }
    }
  }

  Future<void> _likeRecipe() async {
    try {
      await ApiService().likeRecipe(widget.recipe.id);
      setState(() => _likes++);
    } catch (e) {
      log("Error liking recipe: $e");
      _showError('Error liking recipe: $e');
    }
  }

  Future<void> _logout() async {
    await ApiService().logout();
    setState(() {
      _isAuthenticated = false;
      _userId = null;
    });
    Navigator.pushReplacementNamed(context, '/login');
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        Navigator.pop(context, {
          'likes': _likes,
          'commentsCount': _commentsCount,
        });
        return true;
      },
      child: Scaffold(
        appBar: AppBar(
          title: Text(widget.recipe.title),
          actions: [
            if (_isAuthenticated)
              IconButton(
                icon: const Icon(Icons.logout),
                onPressed: _logout,
              ),
          ],
        ),
        body: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (widget.recipe.coverImageUrl.isNotEmpty)
                  Image.network(
                    widget.recipe.coverImageUrl,
                    width: double.infinity,
                    height: 200,
                    fit: BoxFit.cover,
                  ),
                const SizedBox(height: 10),
                Row(
                  children: [
                    Expanded(
                      child: Row(
                        children: [
                          Text('$_likes'),
                          const SizedBox(width: 5),
                          IconButton(
                            icon: const Icon(Icons.thumb_up, size: 18, color: Colors.redAccent),
                            onPressed: _likeRecipe,
                          ),
                        ],
                      ),
                    ),
                    Expanded(
                      child: Row(
                        children: [
                          Text('$_commentsCount'),
                          const SizedBox(width: 5),
                          const Icon(Icons.comment, size: 18, color: Colors.blue),
                        ],
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 20),
                ...widget.recipe.description.map((desc) =>
                    Text(desc.children.map((child) => child.text).join())),
                const SizedBox(height: 20),
                const Text('Ingredients', style: TextStyle(fontWeight: FontWeight.bold)),
                const SizedBox(height: 20),
                Text(widget.recipe.ingredients),
                const SizedBox(height: 20),
                const Text('Procedure', style: TextStyle(fontWeight: FontWeight.bold)),
                const SizedBox(height: 20),
                ...widget.recipe.steps.map((step) =>
                    Text(step.children.map((child) => child.text).join())),
                if (_isLoading)
                  const CircularProgressIndicator(),
                ..._comments.map((comment) => ListTile(
                  title: Text(comment.author),
                  subtitle: Text(comment.content),
                  trailing: Text(comment.createdAt.toLocal().toString()),
                )),
                if (_isAuthenticated)
                  Column(
                    children: [
                      TextField(
                        controller: _commentController,
                        decoration: InputDecoration(labelText: tr('add_comment')),
                      ),
                      ElevatedButton(
                        onPressed: _commentController.text.isNotEmpty ? _addComment : null,
                        child: Text(tr('submit')),
                      ),
                    ],
                  )
                else
                  Text(tr('login_comment')),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```

Cette `RecipeDetailPage` affiche des informations détaillées sur une recette sélectionnée, y compris son image de couverture, les likes, les commentaires, les ingrédients et la procédure. Seuls les utilisateurs authentifiés peuvent commenter ou aimer une recette. Lors de l'initialisation, la page vérifie si l'utilisateur est authentifié en lisant depuis le stockage local. Si authentifié, elle définit `_isAuthenticated` à `true` et récupère l'ID de l'utilisateur, activant des fonctionnalités comme l'ajout de commentaires et l'ajout de likes aux recettes.

* **Ajouter un commentaire** : La fonction `_addComment` publie le nouveau commentaire sur le serveur, l'ajoute à la liste locale des commentaires, incrémente le nombre de commentaires et efface le champ de saisie.

* **Aimer une recette** : La fonction `_likeRecipe` envoie une requête de like au serveur, augmente le nombre local de likes et met à jour l'interface utilisateur.

Si l'utilisateur n'est pas authentifié, il est invité à se connecter pour laisser un commentaire ou interagir avec la recette.

## Créer l'Écran de Demande de Recette

Dans le fichier `lib/screens/requestRecipe.dart`, ajoutez le code ci-dessous :

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import '../models/recipe.dart';
import '../utils/server2.dart';

class RecipeRequestScreen extends StatefulWidget {
  @override
  _RecipeRequestScreenState createState() => _RecipeRequestScreenState();
}

class _RecipeRequestScreenState extends State<RecipeRequestScreen> {
  final _formKey = GlobalKey<FormState>();
  final _titleController = TextEditingController();
  final _descriptionController = TextEditingController();
  final ApiService _apiService = ApiService();

  @override
  void dispose() {
    _titleController.dispose();
    _descriptionController.dispose();
    super.dispose();
  }

  Future<void> _submitRequest() async {
    if (_formKey.currentState!.validate()) {
      final description = _descriptionController.text;
      final descriptionList = [
        Description(
          type: 'paragraph',
          children: [
            TextContent(
              type: 'text',
              text: description,
              bold: false
            ),
          ],
        ),
      ];
      final request = RecipeRequest(
        title: _titleController.text,
        description: descriptionList,
        id: 0,
      );
      try {
        await _apiService.submitRecipeRequest(request);
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(tr('request_successful'))),
        );
        _titleController.clear();
        _descriptionController.clear();
      } catch (e) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Failed to submit recipe request: $e')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(tr('request_recipe')),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: _titleController,
                decoration: InputDecoration(labelText: tr('recipe_title')),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter a title';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: _descriptionController,
                decoration: InputDecoration(labelText: tr('description')),
                maxLines: 5,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return tr('enter_description');
                  }
                  return null;
                },
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _submitRequest,
                child: Text(tr('submit_request')),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

La `RecipeRequestPage` permet aux utilisateurs authentifiés de soumettre une demande pour une nouvelle recette. `widget` est un widget avec état géré par la classe `_RecipeRequestPageState`. Il utilise un formulaire avec deux champs de saisie : un pour le titre de la recette et un pour la description. Ces champs de saisie sont contrôlés par des instances de `TextEditingController`, qui gèrent le texte saisi par l'utilisateur.

La méthode `_submitRequest` gère la soumission du formulaire. Elle valide les champs du formulaire, construit un objet `RecipeRequest` avec le titre et la description saisis, et l'envoie au serveur en utilisant `ApiService`. Si la soumission réussit, un message de succès est affiché en utilisant `ScaffoldMessenger`. Si une erreur se produit, un message d'erreur est affiché.

La méthode `build` construit l'interface utilisateur de l'écran et affiche le formulaire avec ses entrées.

## Créer l'Écran de Profil Utilisateur

Dans le fichier `lib/screens/profile.dart`, ajoutez le code ci-dessous :

```dart
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:flutter_recipe_app/screens/requestRecipe.dart';
import '../models/recipe.dart';
import '../utils/server2.dart';

class ProfileScreen extends StatefulWidget {
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  late Future<List<RecipeRequest>> _requestedRecipesFuture;

  @override
  void initState() {
    super.initState();
    _requestedRecipesFuture = ApiService().fetchUserRequestedRecipes();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(tr('profile')),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 10),
                Text(
                  tr('request_list'),
                  style: TextStyle(fontSize: 16, color: Colors.grey[600]),
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {
                    Navigator.pop(context);
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => RecipeRequestScreen(),
                      ),
                    );
                  },
                  child: Text(tr('request_new_recipe')),
                ),
              ],
            ),
          ),
          Expanded(
            child: FutureBuilder<List<RecipeRequest>>(
              future: _requestedRecipesFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return Center(child: CircularProgressIndicator());
                } else if (snapshot.hasError) {
                  return Center(child: Text('Error: ${snapshot.error.toString()}'));
                } else if (snapshot.data == null || snapshot.data!.isEmpty) {
                  return Center(child: Text(tr('no_request_found')));
                }

                return ListView.builder(
                  itemCount: snapshot.data!.length,
                  itemBuilder: (context, index) {
                    RecipeRequest request = snapshot.data![index];
                    String fullDescription = request.description
                        .map((d) => d.children.map((t) => t.text).join('\n'))
                        .join('\n\n');

                    return Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 40.0),
                      child: ListTile(
                        title: Text(
                          request.title.toUpperCase(),
                          style: const TextStyle(fontWeight: FontWeight.bold),
                        ),
                        subtitle: Text(fullDescription),
                      ),
                    );
                  },
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
```

La classe `ProfileScreen` dans cette application Flutter représente une page de profil utilisateur où ils peuvent voir leurs recettes demandées. Lorsque l'écran est initialisé, il récupère une liste de recettes demandées par l'utilisateur en appelant la méthode `fetchUserRequestedRecipes` de `ApiService`. Ces données sont ensuite stockées dans la variable `_requestedRecipesFuture`, qui est un `Future` qui contiendra éventuellement la liste des recettes demandées.

Dans la méthode `build`, l'écran est construit en utilisant un widget `Scaffold`.

La partie principale de l'écran est un widget `Expanded` contenant un `FutureBuilder`. Le widget `FutureBuilder` attend que `_requestedRecipesFuture` se termine puis construit la liste des recettes demandées. Si les données sont encore en cours de chargement, il affiche un `CircularProgressIndicator`. Si une erreur se produit, il affiche un message d'erreur. Et s'il n'y a pas de recettes, il affiche un message "aucune demande trouvée". Sinon, il affiche la liste des recettes demandées, chacune rendue sous forme de `ListTile` avec le titre et la description de la recette.

## Tester l'Application

Pour tester l'application, connectez votre appareil ou lancez un émulateur, puis exécutez le backend avec la commande suivante :

```bash
npm run develop
```

Et le frontend :

```bash
npm run dev
```

## Conclusion

Dans ce tutoriel, vous avez créé une application de recettes Flutter et Strapi où les utilisateurs pouvaient s'inscrire et se connecter pour demander une recette à l'administrateur, consulter et aimer des recettes, ou ajouter leurs commentaires à une recette spécifique.

Pour améliorer l'application, vous pouvez ajouter une fonctionnalité de recherche, une fonctionnalité de partage, ou permettre aux utilisateurs non seulement de demander une recette mais aussi de créer une liste personnelle de recettes qu'ils peuvent partager avec d'autres.

Merci d'avoir lu !

### Références

* [https://docs.strapi.io/dev-docs/configurations/api-tokens](https://docs.strapi.io/dev-docs/configurations/api-tokens)

* [https://docs.strapi.io/user-docs/settings/API-tokens](https://docs.strapi.io/user-docs/settings/API-tokens)

* [https://docs.strapi.io/dev-docs/backend-customization/examples/authentication](https://docs.strapi.io/dev-docs/backend-customization/examples/authentication)

* [https://docs.strapi.io/dev-docs/plugins/i18n](https://docs.strapi.io/dev-docs/plugins/i18n)

* [https://strapi.io/blog/how-to-create-a-refresh-token-feature-in-your-strapi-application](https://strapi.io/blog/how-to-create-a-refresh-token-feature-in-your-strapi-application)

* [https://strapi.io/blog/a-beginners-guide-to-authentication-and-authorization-in-strapi](https://strapi.io/blog/a-beginners-guide-to-authentication-and-authorization-in-strapi)

* [https://jwt.io/introduction](https://jwt.io/introduction)