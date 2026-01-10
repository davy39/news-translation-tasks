---
title: Comment débuter avec GoRouter dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-04T00:30:26.384Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-gorouter-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756945807034/30528205-5ed9-4517-add6-5a3f32e6ac96.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment débuter avec GoRouter dans Flutter
seo_desc: 'Navigating between screens in Flutter is crucial for any app. And while
  the built-in Navigator API provides functionality, it can get complex for larger
  projects.

  This is where go_router shines, offering a more declarative, URL-based, and feature-ric...'
---

La navigation entre les écrans dans Flutter est cruciale pour n'importe quelle application. Bien que l'API Navigator intégrée offre des fonctionnalités, elle peut devenir complexe pour les grands projets.

C'est là que `go_router` brille, en proposant un système de navigation plus déclaratif, basé sur l'URL et riche en fonctionnalités. Cet article approfondit chaque détail de `go_router`, vous guidant de l'installation aux fonctionnalités avancées comme la redirection et les routes imbriquées.

`go_router` est une bibliothèque de routage flexible et légère pour Flutter qui simplifie le processus de navigation et fournit une API propre pour gérer les routes, passer des paramètres et gérer les redirections. Elle est conçue pour être facile à utiliser tout en offrant des fonctionnalités avancées pour des exigences de navigation plus complexes.

La navigation joue un rôle crucial dans la création d'expériences utilisateur fluides. Alors que Navigator 2.0 intégré offre de la polyvalence, il peut devenir complexe dans les projets de plus grande envergure. C'est ici que `go_router` intervient et aide à simplifier considérablement le processus.

### Table des matières :

1. [Prérequis](#heading-prerequis)
    
2. [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
    
3. [Installation](#heading-installation)
    
4. [Comment définir des routes](#heading-comment-definir-des-routes)
    
5. [Comment créer le routeur](#heading-comment-creer-le-routeur)
    
6. [Comment naviguer entre les écrans](#heading-comment-naviguer-entre-les-ecrans)
    
7. [Comment passer des paramètres](#heading-comment-passer-des-parametres)
    
8. [Sous-routes et ShellRoute](#heading-sous-routes-et-shellroute)
    
9. [Redirection et Guards](#heading-redirection-et-guards)
    
10. [Comment configurer un projet Flutter réel utilisant GoRouter](#heading-comment-configurer-un-projet-flutter-reel-utilisant-gorouter)
    
11. [Structure du projet :](#heading-structure-du-projet)
    
    * [1\. main.dart](#heading-1-maindart)
        
    * [2\. Modèle](#heading-2-modele)
        
    * [3\. Contrôleur](#heading-3-controleur)
        
    * [4\. Configuration](#heading-4-configuration)
        
    * [5\. Écrans](#heading-5-ecrans)
        
    * [6\. Widgets](#heading-6-widgets)
        
12. [Quelques captures d'écran :](#heading-quelques-captures-decran)
    
13. [Conclusion](#heading-conclusion)
    
14. [Références](#heading-references)
    

## Prérequis

Pour suivre cet article et construire l'exemple d'application, vous aurez besoin de :

* **Flutter SDK :** Assurez-vous d'avoir installé et configuré Flutter sur votre machine de développement. Vous trouverez les instructions d'installation sur le site officiel de Flutter.
    
* **Connaissances de base de Flutter :** Une familiarité avec les widgets Flutter, la gestion d'état (même un simple `setState`) et les concepts généraux de développement d'applications sera utile.
    
* **Bases du langage Dart :** Une bonne compréhension de la syntaxe Dart, des classes et des fonctions est essentielle.
    
* **Un IDE :** Visual Studio Code ou Android Studio avec les plugins Flutter et Dart installés.
    

## Ce que nous allons construire

À la fin de cet article, nous aurons construit une application de shopping minimaliste qui démontre les fonctionnalités de base de `go_router`. Cette application aura les fonctionnalités suivantes :

1. Un écran de liste de produits affichant une grille de produits.
    
2. Un écran de détails du produit affichant des informations détaillées sur un produit sélectionné.
    
3. Un écran d'achat de produit qui confirme l'achat d'un produit.
    
4. La navigation entre ces écrans à l'aide de `go_router`, y compris le passage de données via des paramètres de requête (query) et de chemin (path).
    
5. La redirection de route et les Exit Guards pour un contrôle de navigation amélioré.
    

## Installation

Pour commencer, ajoutez `go_router` à votre fichier `pubspec.yaml` :

```yaml
dependencies:
  go_router: ^13.0.0
```

Ceci ajoute le package `go_router` comme dépendance à votre projet, vous permettant d'utiliser ses fonctionnalités.

Importez-le dans vos fichiers Dart :

```dart
import 'package:go_router/go_router.dart';
```

Cette instruction rend toutes les classes et fonctions fournies par le package `go_router` disponibles pour une utilisation dans votre fichier Dart.

## Comment définir des routes

Créez une liste d'objets `GoRoute`, chacun définissant une route :

```dart
final routes = [
  GoRoute(
    path: '/',
    builder: (context, state) => const HomeScreen(),
  ),
  GoRoute(
    path: '/products/:id',
    builder: (context, state) => ProductDetailsScreen(productId: state.params['id']!),
  ),
  // ... plus de routes
];
```

Voici ce qui se passe dans ce code :

* `final routes = [...]` : Ceci déclare une liste finale nommée `routes` qui contiendra toutes nos configurations de routes.
    
* `GoRoute(...)` : C'est la classe centrale pour définir une route. Chaque objet `GoRoute` représente un chemin distinct dans votre application.
    
* `path: '/'` : La propriété `path` définit le chemin URL pour cette route. Dans ce cas, `/` représente la racine ou l'écran d'accueil de l'application.
    
* `builder: (context, state) => const HomeScreen()` : La propriété `builder` est une fonction qui renvoie le widget à afficher lorsque cette route est active. `context` fournit le contexte de construction, et `state` donne accès aux informations spécifiques à la route comme les paramètres. Ici, il construit un widget `HomeScreen`.
    
* `path: '/products/:id'` : Cette route définit un chemin dynamique. La partie `:id` est un paramètre de chemin, ce qui signifie que toute valeur située à cette position dans l'URL sera capturée en tant que paramètre.
    
* `builder: (context, state) => ProductDetailsScreen(productId: state.params['id']!)` : Lorsque cette route est activée, elle construit un `ProductDetailsScreen`. `state.params['id']!` accède à la valeur du paramètre de chemin `id`. Le `!` affirme que `id` ne sera pas nul.
    

## Comment créer le routeur

Instanciez un objet `GoRouter`, en passant les routes et en l'intégrant au `MaterialApp` de votre application :

```dart
MaterialApp.router(
  routeInformationParser: GoRouter.of(context).routeInformationParser,
  routerDelegate: GoRouter(routes: routes),
  // ... autres propriétés de MaterialApp
)
```

Voici ce qui se passe dans ce code :

* `MaterialApp.router(...)` : Il s'agit d'un constructeur spécial pour `MaterialApp` qui s'intègre à un délégué de routeur, comme `GoRouter`.
    
* `routerConfig: router,` ou `routeInformationParser: GoRouter.of(context).routeInformationParser, routerDelegate: GoRouter(routes: routes),` : Ces propriétés sont cruciales pour que `go_router` gère la navigation.
    
    1. `routeInformationParser` : Responsable de l'analyse des informations de route provenant de la plateforme (par exemple, l'URL dans un navigateur web) dans une structure de données que le routeur peut comprendre.
        
    2. `routerDelegate` : Responsable de la construction et de la gestion de la pile de navigation en fonction des informations de route analysées.
        
* `GoRouter(routes: routes)` : Ceci crée une instance de `GoRouter`, en passant la liste des objets `GoRoute` que nous avons définis précédemment.
    

## Comment naviguer entre les écrans

Vous pouvez naviguer par programmation en utilisant `GoRouter.of(context).go()` :

```dart
GoRouter.of(context).go('/products/123');
```

Voici ce que fait ce code :

* `GoRouter.of(context)` : Cette méthode statique récupère l'instance `GoRouter` la plus proche dans l'arborescence des widgets.
    
* `.go('/products/123')` : Cette méthode navigue vers le chemin URL spécifié. Cela remplacera la route actuelle dans la pile de navigation.
    

Vous pouvez également naviguer en utilisant des routes nommées comme ceci :

```dart
GoRouter.of(context).goNamed('productDetails', params: {'id': 123});
```

Dans ce code** :**

* `.goNamed('productDetails', ...)` : Cette méthode navigue vers une route identifiée par sa propriété `name` (qui doit être définie dans la configuration `GoRoute`).
    
* `params: {'id': 123}` : Ce dictionnaire fournit des valeurs pour tous les paramètres de chemin définis dans la route nommée.
    

## Comment passer des paramètres

Dans la plupart des applications réelles, nous ne nous contentons pas de naviguer entre les écrans – nous devons également transmettre des informations. Par exemple :

* D'une liste de produits à une page de détails de produit, vous voudrez passer l'ID du produit.
    
* D'un écran de paiement, vous devrez peut-être passer la description ou le prix du produit.
    

Avec `go_router`, vous pouvez passer des paramètres de deux manières principales :

1. **Query Parameters (Paramètres de requête)** : Ajoutés à l'URL après un `?`. Utiles pour les données facultatives ou les filtres (par exemple, `/products?id=123`).
    
2. **Path Parameters (Paramètres de chemin)** : Embarqués directement dans le chemin de la route. Idéal pour les valeurs requises (par exemple, `/products/123`).
    

Explorons les deux.

### 1\. Passage de paramètres de requête

Les paramètres de requête sont des paires clé-valeur flexibles attachées à l'URL. Ils sont généralement utilisés pour des informations non essentielles ou facultatives, telles que des filtres, des requêtes de recherche ou des identifiants.

Exemple : appuyer sur une carte de produit pour ouvrir son écran de détails.

```dart
GestureDetector( 
  onTap: () => context.goNamed(
    ProductDetailsScreen.routeName, 
    queryParameters: {'id': product.id}, 
  ), 
  child: SingleProduct(product: product), 
);
```

Que se passe-t-il ici ?

* `context.goNamed(...)` : Navigue vers une route en utilisant son nom (défini dans votre configuration de routes).
    
* `queryParameters: {'id': product.id}` : Ajoute l'ID du produit à l'URL comme ceci :
    
    ```bash
    /product-details?id=abc123
    ```
    

Sur l'écran de destination, vous récupérez le paramètre comme ceci :

```dart
GoRoute(
  path: ProductDetailsScreen.routeName,
  name: ProductDetailsScreen.routeName,
  builder: (context, state) {
    return ProductDetailsScreen(
      productId: state.uri.queryParameters['id'] ?? "",
    );
  },
)
```

* `state.uri.queryParameters['id']` : Extrait la valeur `id` de l'URL.
    
* `?? ""` : Fournit une chaîne vide par défaut si le paramètre est manquant.
    

Utilisez les paramètres de requête lorsque :

* Le paramètre est facultatif.
    
* Vous voulez autoriser plusieurs paramètres sans changer la route de base.
    
* Les données ne modifient pas fondamentalement la structure de la route.
    

### 2\. Passage de paramètres de chemin

Les paramètres de chemin font partie de la route elle-même et sont généralement obligatoires. Sans eux, la route n'a pas de sens.

Exemple : un flux d'achat où la description du produit est requise.

Naviguer vers la route :

```dart
context.goNamed(
  'pay-now',
  pathParameters: {
    'description': product.description,
  },
);
```

Définir la route :

```dart
GoRoute(
  path: 'product-purchase/:description',
  name: ProductPurchaseScreen.routeName,
  builder: (context, state) {
    return ProductPurchaseScreen(
      description: state.pathParameters['description']!,
    );
  },
)
```

Que se passe-t-il ici ?

* `path: 'product-purchase/:description'` : La partie `:description` définit un segment dynamique.
    
* `pathParameters: {'description': product.description}` : Remplace `:description` par la valeur réelle. L'URL ressemblera à :
    
    ```bash
    /product-purchase/AwesomeProduct
    ```
    
* `state.pathParameters['description']!` : Récupère le paramètre à l'intérieur de l'écran.
    

Utilisez les paramètres de chemin lorsque :

* La valeur est requise (par exemple, ID, nom d'utilisateur, slug).
    
* La route ne devrait pas exister sans elle.
    

## Sous-routes et ShellRoute

À mesure que votre application grandit, vous devrez organiser les routes de manière hiérarchique ou conserver des éléments d'interface persistants comme une barre de navigation inférieure. `go_router` rend cela possible avec les **Sub-routes** et **ShellRoute**.

### 1\. Sous-routes

Les sous-routes vous permettent d'imbriquer des routes sous un parent. Cela permet de regrouper les routes liées.

Exemple : Profil et sa page de paramètres.

```dart
GoRoute(
  path: '/profile',
  builder: (context, state) => ProfileScreen(),
  routes: [
    GoRoute(
      path: 'settings',
      builder: (context, state) => SettingsScreen(),
    ),
  ],
),
```

* `/profile` : Ouvre `ProfileScreen`.
    
* `/profile/settings` : Ouvre `SettingsScreen`.
    

Utilisez les sous-routes pour garder les écrans liés organisés sous une route parente.

### 2\. ShellRoute

`ShellRoute` est utilisé lorsque vous avez besoin d'un conteneur d'interface persistant (comme une `BottomNavigationBar` ou un `Drawer`) qui reste visible lors de la commutation entre les routes enfants.

Exemple : Une mise en page avec navigation inférieure.

```dart
ShellRoute(
  builder: (context, state, child) {
    return MainScaffold(child: child); // contient BottomNavigationBar
  },
  routes: [
    GoRoute(
      path: '/home',
      builder: (context, state) => HomeScreen(),
    ),
    GoRoute(
      path: '/profile',
      builder: (context, state) => ProfileScreen(),
    ),
  ],
),
```

`ShellRoute` : Enveloppe un widget persistant (`MainScaffold`). `child` : Change dynamiquement selon la route active.

Utilisez `ShellRoute` lorsque :

* Vous avez besoin d'onglets ou d'une navigation inférieure.
    
* Vous voulez qu'une mise en page reste tandis que seul le contenu interne change.
    

## Redirection et Guards

Dans de nombreuses applications, la navigation ne consiste pas seulement à se déplacer entre les pages. Il s'agit également de contrôler qui peut accéder à quoi et quand. Par exemple :

* Rediriger un utilisateur déconnecté vers l'écran de connexion.
    
* Empêcher les non-administrateurs d'accéder aux routes d'administration.
    

`go_router` fournit deux outils principaux ici : les **redirections** et les **guards**.

### 1\. Redirection

Une redirection redirige automatiquement les utilisateurs si une condition n'est pas remplie.

Exemple : redirection d'anciennes URL ou imposition de la connexion.

```dart
GoRoute(
  path: '/old-path',
  redirect: (state) => '/new-path',
),

GoRoute(
  path: '/dashboard',
  builder: (context, state) => DashboardScreen(),
  redirect: (context, state) {
    final isLoggedIn = AuthService.isLoggedIn();
    return isLoggedIn ? null : '/login';
  },
),
```

* `/old-path` : Redirige toujours vers `/new-path`.
    
* `/dashboard` : Redirige vers `/login` si l'utilisateur n'est pas connecté.
    

### 2\. Guards

Les Guards sont comme des "vérifications" placées sur les routes. Ils décident si un utilisateur peut accéder à une route ou non.

Exemple : restreindre l'accès aux administrateurs uniquement.

```dart
GoRoute(
  path: '/admin',
  builder: (context, state) => AdminScreen(),
  redirect: (context, state) {
    final isAdmin = AuthService.isAdmin();
    return isAdmin ? null : '/not-authorized';
  },
),
```

Si `isAdmin` est `true`, l'utilisateur peut accéder à `/admin`. Sinon, il est redirigé vers `/not-authorized`.

Utilisez les redirections et les guards pour :

* Les flux d'authentification (connexion/déconnexion).
    
* L'accès basé sur les rôles (administrateur vs utilisateur).
    
* La gestion des routes obsolètes ou modifiées.
    

## Comment configurer un projet Flutter réel utilisant Go Router

Avant de plonger dans GoRouter, commençons par configurer un nouveau projet Flutter et organiser le code. La structure du projet comprend les dossiers et fichiers suivants :

```bash
go_router_project/
|-- lib/
|   |-- main.dart
|   |-- models/
|   |   |-- product.dart
|   |-- controller/
|   |   |-- product_controller.dart
|   |-- config/
|   |   |-- route_config.dart
|   |-- screens/
|   |   |-- product_details_screen.dart
|   |   |-- product_list_screen.dart
|   |   |-- product_purchase_screen.dart
|   |-- widgets/
|       |-- bottom_container.dart
|       |-- color_container.dart
|       |-- ratings.dart
|       |-- search_section.dart
|       |-- show_modal.dart
|       |-- single_product.dart
|-- pubspec.yaml
```

Maintenant, ouvrez le fichier `pubspec.yaml` et ajoutez la dépendance suivante :

```yaml
dependencies:
  go_router: ^13.0.0
```

Enregistrez le fichier et exécutez `flutter pub get` dans le terminal pour récupérer la dépendance.

Nous allons créer une application de shopping minimaliste avec seulement trois pages.

## Structure du projet

### 1\. `main.dart` :

Remplacez le code dans `lib/main.dart` par celui-ci :

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'go_router/config/route_config.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    SystemChrome.setSystemUIOverlayStyle(
      const SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
        statusBarIconBrightness: Brightness.dark,
      ),
    );

    return MaterialApp.router(
      title: 'Flutter GoRouter',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.brown),
        useMaterial3: true,
      ),
      routerConfig: router, // go router
    );
  }
}
```

Voici ce qui se passe dans ce code :

* `main()` : Le point d'entrée de l'application Flutter. Il lance le widget `MyApp`.
    
* `SystemChrome.setSystemUIOverlayStyle(...)` : Ceci configure l'overlay de l'UI système, en rendant notamment la barre d'état transparente et ses icônes sombres.
    
* `MaterialApp.router(...)` : C'est le widget racine de notre application, configuré avec `go_router`.
    
* `title: 'Flutter GoRouter'` : Définit le titre de l'application.
    
* `theme: ThemeData(...)` : Définit le thème visuel de l'application, en utilisant une couleur de base `brown` (marron) et le design Material 3.
    
* `routerConfig: router` : C'est ici que `go_router` est intégré. `router` est l'instance `GoRouter` définie dans `route_config.dart`.
    

### **2\. Modèle**

Le dossier `models` est l'endroit où nous définissons nos structures de données. Un modèle est simplement une classe Dart qui représente la forme des données avec lesquelles vous travaillerez dans votre application.

Par exemple, dans ce projet, `Product` est le modèle. Il contient des détails tels que `id`, `name`, `imageUrl`, `description`, `price`, et ainsi de suite. Les modèles ne gèrent pas la logique ou l'interface utilisateur, ils ne sont que des plans pour les données.

Considérez les modèles comme la fondation. Chaque fois que votre application récupère, stocke ou manipule des informations sur un produit, elle utilise ce modèle `Product` pour plus de cohérence. Nous allons créer un modèle appelé **product.dart**.

#### `product.dart` :

Ajoutez ce code à `lib/models/product.dart` :

```dart
import 'package:flutter/foundation.dart';

class Product {
  final String id;
  final String name;
  final String imageUrl;
  final String description;
  final double price;
  final double previousPrice;
  final String colors;

  Product({
    required this.id,
    required this.name,
    required this.imageUrl,
    required this.description,
    required this.previousPrice,
    required this.price,
    required this.colors,
  });

  factory Product.initial() => Product(
        id: '',
        name: '',
        imageUrl: '',
        description: '',
        previousPrice: 0.0,
        price: 0.0,
        colors: '',
      );
}
```

* Classe `Product` : Cette classe définit la structure d'un produit, avec des propriétés comme `id`, `name`, `imageUrl`, `description`, `price`, `previousPrice` et `colors`.
    
* `Product.initial()` : Un constructeur d'usine (factory) pour créer un objet `Product` vide, utile pour l'initialisation.
    

### **3\. Contrôleur**

Le dossier `controllers` contient des classes qui gèrent la logique métier, la façon dont les données entrent et sortent de votre application. Les contrôleurs se situent entre vos vues (UI) et vos modèles (données).

Dans cet exemple, le `ProductController` est un simple fournisseur de données en mémoire. Il :

* Stocke une liste d'objets `Product`.
    
* Expose une méthode `findById()` pour que nous puissions rechercher un produit rapidement.
    
* Permet d'accéder à la liste des produits via le getter `products`.
    

Dans les applications plus importantes, les contrôleurs récupèrent souvent des données à partir d'API, gèrent la mise en cache ou l'état de l'application. Ici, il est resté simple à des fins d'apprentissage. Nous allons créer un contrôleur de produit.

#### `product_controller.dart` :

Ajoutez ce code à `lib/controllers/product_controller.dart` :

```dart
import '../models/product.dart';

class ProductController {
  Product findById(String? id) {
    return _products.firstWhere((product) => product.id == id);
  }

  List<Product> get products => _products;

  final List<Product> _products = [
    Product(
      id: 'p7',
      name: 'Leather BackPack',
      imageUrl:
          'https://images.unsplash.com/photo-1571689936114-b16146c9570a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NzR8fHByb2R1Y3R8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60',
      description:
          'Plus il est solide, mieux c\'est de le charger avec tout ce que les yeux voient d\'utile et de nécessaire aussi. Le BackPack est un sac en cuir solide et polyvalent pour transporter tout ce que les mains peuvent stocker et il vaut littéralement chaque centime',
      price: 30.9,
      previousPrice: 40.9,
      colors: 'red,grey,black,indigo,purple',
    ),
    Product(
      id: 'p1',
      name: 'Smart Watch',
      imageUrl:
          'https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZHVjdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60',
      description: 'Une montre connectée blanche avec de bonnes fonctionnalités et plus encore',
      price: 29.99,
      previousPrice: 39.99,
      colors: 'red,grey,black,indigo,purple',
    ),
    Product(
      id: 'p16',
      name: 'PowerBook',
      imageUrl:
          'https://get.pxhere.com/photo/laptop-computer-macbook-mac-screen-water-board-keyboard-technology-air-mouse-photo-airport-aircraft-tablet-aviation-office-black-monitor-keys-graphic-hardware-image-pc-exhibition-multimedia-calculator-vector-water-cooling-floppy-disk-phased-out-desktop-computer-netbook-personal-computer-computer-monitor-electronic-device-computer-hardware-display-device-448748.jpg',
      description:
          'Matériel génial, clavier médiocre et prix élevé. Achetez maintenant avant la sortie d\'un nouveau !',
      price: 2299.99,
      previousPrice: 3299.99,
      colors: 'red,grey,black,indigo,purple',
    ),
    Product(
      id: 'p2',
      name: 'Red Sneakers',
      imageUrl:
          'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fHByb2R1Y3R8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60',
      description:
          'Parfait pour vos joggings, vos t-shirts noirs et plus encore. Les baskets sont disponibles en différentes tailles et couleurs. On ne sait jamais quand ce t-shirt a besoin de style avec les couches souples d\'une basket',
      price: 199.99,
      previousPrice: 299.99,
      colors: 'yellow,grey,black,red,teal',
    ),
    Product(
      id: 'p3',
      name: 'Nikon Camera',
      imageUrl:
          'https://images.unsplash.com/photo-1564466809058-bf4114d55352?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fHByb2R1Y3R8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60',
      description:
          'Vous ne pouvez voir plus clair qu\'avec vos yeux, mais un appareil photo enregistre le souvenir dans ses yeux',
      price: 89.9,
      previousPrice: 109.9,
      colors: 'red,grey,black,indigo,purple',
    ),
    Product(
      id: 'p4',
      name: 'HeadSets',
      imageUrl:
          'https://images.unsplash.com/photo-1583394838336-acd977736f90?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjJ8fHByb2R1Y3R8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60',
      description:
          'Plus le son est fort, mieux on se sent à l\'intérieur avec le corps',
      price: 120.1,
      previousPrice: 150.1,
      colors: 'red,grey,black,indigo,purple',
    ),
    Product(
      id: 'p5',
      name: 'Amazon SoundBox',
      imageUrl:
          'https://images.unsplash.com/photo-1543512214-318c7553f230?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjR8fHByb2R1Y3R8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60',
      description:
          'Enceinte automatisée avec reconnaissance vocale et plus. Qu\'est-ce qui pourrait être mieux',
      price: 78.19,
      previousPrice: 88.19,
      colors: 'red,grey,black,indigo,purple',
    ),
    Product(
      id: 'p6',
      name: 'Xbox 360 GamePads',
      imageUrl:
          'https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzd8fHByb2R1Y3R8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60',
      description:
          'On ne sait jamais quand il est temps de mieux toucher, sauf si les manettes de la Xbox sont là pour aider',
      price: 98.99,
      previousPrice: 108.99,
      colors: 'red,grey,black,indigo,purple',
    ),
  ];
}
```

* Classe `ProductController` : Cette classe agit comme une simple source de données pour nos produits.
    
* `findById(String? id)` : Une méthode pour trouver un produit par son ID dans la liste `_products`.
    
* Getter `products` : Permet d'accéder à la liste `_products`. `_products` : Une liste privée d'objets `Product`, pré-remplie avec des données d'exemple.
    

### **4\. Configuration**

Le dossier `config` stocke tous les fichiers de configuration et de paramétrage de votre application. Dans ce projet, c'est là que nous gardons `route_config.dart`, qui contient toute la configuration de `go_router` et les définitions des routes.

C'est important car :

* Les routes peuvent devenir complexes à mesure que votre application se développe.
    
* Avoir toute la configuration de navigation en un seul endroit permet de garder les choses propres et gérables.
    
* Les fichiers de configuration sont également un excellent endroit pour mettre des constantes à l'échelle de l'application, des paramètres d'environnement ou des thèmes.
    

Considérez la configuration comme le **câblage** central de votre application. Il ne s'agit pas de données ou de logique, mais de la manière dont l'application est structurée et liée.

#### `route_config.dart` :

Ajoutez ce code à `lib/config/route_config.dart` :

```dart
import 'package:flutter/material.dart';
import 'package:get_it_auto_router_go_router/go_router/controllers/product_controller.dart';
import 'package:go_router/go_router.dart';
import '../models/product.dart';
import '../screens/product_details_screen.dart';
import '../screens/product_list_screen.dart';
import '../screens/product_purchase_screen.dart';

/// La configuration des routes.
final GoRouter router = GoRouter(
  routes: <RouteBase>[
    GoRoute(
      path: '/',
      builder: (BuildContext context, GoRouterState state) {
        return const ProductListScreen();
      },
      routes: <RouteBase>[
        GoRoute(
          path: ProductDetailsScreen.routeName,
          name: ProductDetailsScreen.routeName,
          builder: (BuildContext context, GoRouterState state) {
            return ProductDetailsScreen(
              productId: state.uri.queryParameters['id'] ?? "",
            );
          },
          routes: <RouteBase>[
            GoRoute(
              path: 'product-purchase/:description',
              name: ProductPurchaseScreen.routeName,
              builder: (BuildContext context, GoRouterState state) {
                return ProductPurchaseScreen(
                  productImage: state.uri.queryParameters['img']!,
                  productPrice: state.uri.queryParameters['price']!,
                  productName: state.uri.queryParameters['name']!,
                  description: state.pathParameters['description']!,
                );
              },
              onExit: (BuildContext context) async {
                final bool? confirmed = await showDialog<bool>(
                  context: context,
                  builder: (_) {
                    return AlertDialog(
                      content: const Text('Êtes-vous sûr de vouloir quitter cette page ?'),
                      actions: <Widget>[
                        TextButton(
                          onPressed: () => Navigator.of(context).pop(false),
                          child: const Text('Annuler'),
                        ),
                        TextButton(
                          onPressed: () => Navigator.of(context).pop(true),
                          child: const Text('Confirmer'),
                        ),
                      ],
                    );
                  },
                );
                return confirmed ?? false;
              },
            )
          ],
        )
      ],
    ),
  ],
);
```

Voici ce qui se passe dans ce code :

* `final GoRouter router = GoRouter(...)` : Il s'agit de l'instance `GoRouter` principale de notre application.
    
* `routes: <RouteBase>[...]` : Définit les routes de niveau supérieur.
    
* `GoRoute(path: '/', builder: ...)` : La route racine, menant à `ProductListScreen`.
    
* `GoRoute` imbriqué pour `ProductDetailsScreen` : Cette route est un enfant de la racine.
    
* `path: ProductDetailsScreen.routeName` : Utilise une constante statique pour le chemin.
    
* `name: ProductDetailsScreen.routeName` : Attribue un nom à la route pour faciliter la navigation.
    
* `builder` : Construit le `ProductDetailsScreen`, en extrayant `productId` des paramètres de requête.
    
* `GoRoute` imbriqué pour `ProductPurchaseScreen` : Cette route est un enfant de `ProductDetailsScreen`.
    
* `path: 'product-purchase/:description'` : Définit un chemin avec un paramètre de chemin `description`.
    
* `name: ProductPurchaseScreen.routeName` : Attribue un nom pour la navigation.
    
* `builder` : Construit le `ProductPurchaseScreen`, en extrayant `productImage`, `productPrice`, `productName` des paramètres de requête et `description` des paramètres de chemin.
    
* `onExit: (BuildContext context) async { ... }` : Il s'agit d'un Guard `onExit` qui déclenche un dialogue de confirmation lorsque l'utilisateur tente de quitter le `ProductPurchaseScreen`. Si l'utilisateur annule, la navigation est empêchée.
    

### 5\. Écrans

Vos écrans sont les pages de l'interface utilisateur avec lesquelles l'utilisateur interagit. Chaque écran a un rôle différent dans le flux d'achat :

#### ProductListScreen :

C'est l'**écran d'entrée** de votre application qui affiche tous les produits disponibles sous forme de grille.

* Agit comme une page de catalogue/navigation.
    
* Utilise le `ProductController` pour récupérer les données des produits.
    
* Comprend une barre de recherche (`SearchSection`) pour filtrer les produits.
    
* Navigue vers le `ProductDetailsScreen` lorsqu'un produit est touché.
    

#### ProductDetailsScreen :

Cet écran affiche les **détails complets** d'un produit sélectionné.

* Affiche l'image du produit, son nom, son prix, les couleurs disponibles et sa description.
    
* Permet à l'utilisateur de visualiser un modal d'image plus grand en touchant l'image.
    
* Fournit un bouton "Acheter maintenant" en bas (via `bottomContainer`).
    
* Utilise les paramètres de chemin et de requête dans la navigation pour transmettre les données du produit à l'écran suivant.
    

#### ProductPurchaseScreen :

C'est l'**écran de confirmation finale** avant l'achat.

* Affiche l'image du produit sélectionné, son nom, son prix et sa description.
    
* Confirme l'intention d'achat de l'utilisateur avec un `FloatingActionButton` (actuellement juste une icône).
    
* Complète le flux de navigation : Liste &gt; Détails &gt; Achat.
    

Très bien, passons-les maintenant en revue un par un :

#### `product_list_screen.dart` :

Ajoutez ce code à `lib/screens/product_list_screen.dart` :

```dart
import 'package:flutter/material.dart';
import 'package:get_it_auto_router_go_router/go_router/controllers/product_controller.dart';
import 'package:get_it_auto_router_go_router/go_router/screens/product_details_screen.dart';
import 'package:get_it_auto_router_go_router/go_router/widgets/search_section.dart';
import 'package:get_it_auto_router_go_router/go_router/widgets/single_product.dart';
import 'package:go_router/go_router.dart';

import '../models/product.dart';

class ProductListScreen extends StatelessWidget {
  const ProductListScreen({super.key});


  @override
  Widget build(BuildContext context) {
    ProductController productController = ProductController();
    TextEditingController searchController = TextEditingController();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Produits'),
        elevation: 0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            SearchSection(
              searchController: searchController,
            ),
            const SizedBox(height: 10),
            Expanded(
              child: GridView.builder(
                itemCount: productController.products.length,
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2,
                  mainAxisSpacing: 10,
                  crossAxisSpacing: 10,
                ),
                itemBuilder: (context, index) {
                  Product product = productController.products[index];

                  return GestureDetector(
                    onTap: () => context.goNamed(
                      ProductDetailsScreen.routeName,
                      queryParameters: {'id': product.id},
                    ),
                    child: SingleProduct(product: product),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

Voici ce qui se passe :

* `ProductListScreen` : Un `StatelessWidget` qui affiche une liste de produits.
    
* `ProductController productController = ProductController()` : Crée une instance de `ProductController` pour accéder aux données des produits.
    
* `AppBar` : Affiche le titre "Produits".
    
* `SearchSection` : Un widget personnalisé pour une barre de recherche.
    
* `Expanded` avec `GridView.builder` : Affiche les produits dans une grille défilante.
    
* `onTap` de `GestureDetector` : Lorsqu'un produit est touché, il navigue vers le `ProductDetailsScreen` en utilisant `context.goNamed`, en passant l'`id` du produit comme paramètre de requête.
    
* `SingleProduct` : Un widget personnalisé pour afficher les informations individuelles d'un produit.
    

#### `product_details_screen.dart` :

Ajoutez ce code à `lib/screens/product_details_screen.dart` :

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import '../controllers/product_controller.dart';
import '../models/product.dart';
import '../widgets/bottom_container.dart';
import '../widgets/color_container.dart';
import '../widgets/ratings.dart';
import '../widgets/show_modal.dart';

class ProductDetailsScreen extends StatelessWidget {
  static const routeName = 'product-details';
  final String productId;

  const ProductDetailsScreen({
    super.key,
    required this.productId,
  });

  @override
  Widget build(BuildContext context) {
    late Color colored;

    // obtenir la couleur
    Color getColor(String color) {
      switch (color) {
        case 'red':
          colored = Colors.red;
          break;
        case 'purple':
          colored = Colors.purple;
          break;
        case 'grey':
          colored = Colors.grey;
          break;
        case 'black':
          colored = Colors.black;
          break;
        case 'orange':
          colored = Colors.orange;
          break;
        case 'indigo':
          colored = Colors.indigo;
          break;
        case 'yellow':
          colored = Colors.yellow;
          break;
        case 'blue':
          colored = Colors.blue;
          break;
        case 'brown':
          colored = Colors.brown;
          break;
        case 'teal':
          colored = Colors.teal;
          break;
        default:
      }

      return colored;
    }

    ProductController productController = ProductController();
    Product product = productController.findById(productId);

    List<String> availableColors = product.colors.split(',');

    // acheter maintenant
    void payNow() {
      context.goNamed(
        'pay-now',
        pathParameters: <String, String>{
          'description': product.description,
        },
        queryParameters: <String, String>{
          'img': product.imageUrl.toString(),
          'price': product.price.toString(),
          'name': product.name.toString(),
        },
      );
    }

    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        automaticallyImplyLeading: false,
        backgroundColor: Colors.transparent,
        elevation: 0,
        systemOverlayStyle: const SystemUiOverlayStyle(
          statusBarColor: Colors.transparent,
        ),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          color: Colors.black,
          onPressed: () {
            Navigator.of(context).pop();
          },
        ),
      ),
      body: Column(
        children: [
          Expanded(
            flex: 2,
            child: GestureDetector(
              onTap: () => showImageModal(context, product),
              child: ClipRRect(
                borderRadius: const BorderRadius.vertical(
                  top: Radius.zero,
                  bottom: Radius.circular(50),
                ),
                child: Hero(
                  tag: product.id,
                  child: Image.network(
                    product.imageUrl,
                    fit: BoxFit.cover,
                    width: double.infinity,
                  ),
                ),
              ),
            ),
          ),
          Expanded(
            flex: 3,
            child: Padding(
              padding: const EdgeInsets.all(15.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text(
                    product.name,
                    style: const TextStyle(
                      fontSize: 30,
                    ),
                  ),
                  const SizedBox(height: 5),
                  ratings(),
                  const SizedBox(height: 5),
                  Row(
                    children: [
                      Text(
                        '\$${product.price.toString()}',
                        style: const TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(width: 3),
                      Text(
                        '\$${product.previousPrice.toString()}',
                        style: const TextStyle(
                          fontSize: 15,
                          color: Colors.grey,
                          decoration: TextDecoration.lineThrough,
                        ),
                      ),
                    ],
                  ),
                  const Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text(
                        'En stock',
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(
                        'Rupture de stock',
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: Colors.deepOrange,
                          decoration: TextDecoration.lineThrough,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),
                  const Text(
                    'Couleurs disponibles',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 15,
                    ),
                  ),
                  const SizedBox(height: 10),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      for (var color in availableColors)
                        buildContainer(
                          color,
                          getColor,
                        )
                    ],
                  ),
                  const SizedBox(height: 15),
                  const Text(
                    'À propos',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 15,
                    ),
                  ),
                  const SizedBox(height: 10),
                  Text(
                    product.description,
                    textAlign: TextAlign.justify,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
      bottomSheet: bottomContainer(product, payNow),
    );
  }
}
```

C'est beaucoup de choses – voici ce que fait ce code :

* `ProductDetailsScreen` : Un `StatelessWidget` qui affiche les détails d'un seul produit.
    
* `static const routeName = 'product-details'` : Définit une constante statique pour le nom de la route, assurant la cohérence.
    
* `productId` : C'est un paramètre requis pour l'écran, passé lors de la navigation.
    
* `getColor(String color)` : Une fonction utilitaire pour convertir les noms de couleurs (chaînes) en objets `Color`.
    
* `ProductController productController = ProductController()` : Accède aux données du produit.
    
* `Product product = productController.findById(productId)` : Récupère le produit spécifique en fonction du `productId` reçu.
    
* `payNow()` : Une fonction qui navigue vers le `ProductPurchaseScreen` en utilisant `context.goNamed`, en passant les détails du produit comme paramètres de chemin et de requête.
    
* `AppBar` : Affiche une flèche de retour pour revenir en arrière.
    
* `Expanded` pour l'image du produit : Affiche l'image du produit avec une animation `Hero` pour des transitions fluides.
    
* `GestureDetector` permet de toucher l'image pour afficher un modal.
    
* `Expanded` pour les détails du produit : Affiche le nom du produit, les notes (ratings), les prix, la disponibilité, les couleurs disponibles et la description.
    
* `bottomSheet: bottomContainer(product, payNow)` : Attache un widget personnalisé `bottomContainer` au `Scaffold`, qui comprend le bouton "Acheter maintenant".
    

#### `product_purchase_screen.dart` :

Ajoutez ce code à `lib/screens/product_purchase_screen.dart` :

```dart
import 'package:flutter/material.dart';

class ProductPurchaseScreen extends StatelessWidget {
  const ProductPurchaseScreen({
    super.key,
    required this.productImage,
    required this.productName,
    required this.productPrice,
    required this.description,
  });

  static const routeName = 'pay-now';

  final String productName;
  final String productPrice;
  final String productImage;
  final String description;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: const FloatingActionButton(
        onPressed: null,
        child: Icon(
          Icons.check_circle,
        ),
      ),
      appBar: AppBar(
        title: const Text('Acheter l\'article'),
      ),
      body: SingleChildScrollView(
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              children: <Widget>[
                ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: Image.network(productImage),
                ),
                const SizedBox(height: 10),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: <Widget>[
                    Text(
                      productName,
                      style: const TextStyle(
                        fontWeight: FontWeight.w800,
                        fontSize: 18,
                      ),
                    ),
                    Text(
                      '\$$productPrice',
                      style: const TextStyle(
                        fontWeight: FontWeight.w800,
                        fontSize: 16,
                        color: Colors.grey,
                      ),
                    )
                  ],
                ),
                const SizedBox(height: 10),
                Text(
                  description,
                  style: const TextStyle(
                    fontSize: 16,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```

Voici ce qui se passe :

* `ProductPurchaseScreen` : Un `StatelessWidget` qui confirme l'achat du produit.
    
* `static const routeName = 'pay-now'` : Définit le nom de la route.
    
* `productImage`, `productName`, `productPrice`, `description` : Ce sont des paramètres requis reçus de l'écran précédent.
    
* `FloatingActionButton` : Affiche une icône de coche, bien que `onPressed` soit actuellement nul.
    
* `AppBar` : Affiche le titre "Acheter l'article".
    
* `SingleChildScrollView` : Rend le contenu défilant.
    
* `Image.network(productImage)` : Affiche l'image du produit reçue.
    
* `Row` pour le nom et le prix du produit : Affiche le nom du produit et son prix.
    
* `Text(description)` : Affiche la description du produit.
    

### 6\. **Widgets**

Les widgets sont les blocs de construction réutilisables de votre interface utilisateur. Au lieu de dupliquer le code de l'interface utilisateur sur plusieurs écrans, vous les divisez en widgets.

#### `bottom_container.dart` :

Ajoutez ce code à `lib/widgets/bottom_container.dart` :

```dart
// bottom container
import 'package:flutter/material.dart';

import '../models/product.dart';

Container bottomContainer(Product productDetails,Function payNow) {
  return Container(
    color: Colors.white,
    child: Padding(
      padding: const EdgeInsets.symmetric(
        horizontal: 18.0,
        vertical: 10,
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Prix',
                style: TextStyle(
                  color: Colors.grey,
                  fontWeight: FontWeight.w500,
                  fontSize: 14,
                ),
              ),
              const SizedBox(height: 5),
              Text(
                '\$${productDetails.price}',
                style: const TextStyle(
                  color: Colors.brown,
                  fontWeight: FontWeight.w700,
                  fontSize: 25,
                ),
              )
            ],
          ),
          Wrap(
            crossAxisAlignment: WrapCrossAlignment.center,
            children: [
              Container(
                height: 50,
                width: 80,
                decoration: BoxDecoration(
                  color: Colors.brown.withOpacity(0.3),
                  borderRadius: const BorderRadius.only(
                    bottomLeft: Radius.circular(5),
                    topLeft: Radius.circular(5),
                  ),
                ),
                child: const Center(
                  child: Wrap(
                    crossAxisAlignment: WrapCrossAlignment.center,
                    children: [
                      Icon(
                        Icons.shopping_cart_checkout,
                        color: Colors.white,
                      ),
                      SizedBox(width: 15),
                      Text(
                        '1',
                        style: TextStyle(
                          color: Colors.white,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              GestureDetector(
                onTap: () => payNow(),
                child: Container(
                  height: 50,
                  width: 120,
                  decoration: const BoxDecoration(
                    color: Colors.brown,
                    borderRadius: BorderRadius.only(
                      bottomRight: Radius.circular(5),
                      topRight: Radius.circular(5),
                    ),
                  ),
                  child: const Center(
                    child: Text(
                      'Acheter maintenant',
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ),
                ),
              )
            ],
          )
        ],
      ),
    ),
  );
}
```

Dans ce code :

* `bottomContainer` : Une fonction qui renvoie un widget `Container` pour la feuille inférieure (bottom sheet). Il affiche le prix du produit et un bouton "Acheter maintenant".
    
* `onTap` de `GestureDetector` : Le bouton "Acheter maintenant" déclenche la fonction `payNow` passée en argument.
    

#### `ratings.dart` :

Ajoutez ce code à `lib/widgets/ratings.dart` :

```dart
import 'package:flutter/material.dart';

Widget ratings() => const Row(
      children: [
        Icon(Icons.star, color: Colors.deepOrange, size: 15),
        Icon(Icons.star, color: Colors.deepOrange, size: 15),
        Icon(Icons.star, color: Colors.deepOrange, size: 15),
        Icon(Icons.star, color: Colors.deepOrange, size: 15),
        Icon(Icons.star, color: Colors.deepOrange, size: 15),
        SizedBox(width: 20),
        Text('(3400 avis)')
      ],
    );
```

* `ratings()` : Un simple widget qui affiche une rangée de cinq étoiles orange et un nombre d'avis.
    

#### `color_container.dart` :

Ajoutez ce code à `lib/widgets/color_container.dart` :

```dart
// build container for color
import 'package:flutter/cupertino.dart';

Widget buildContainer(String color,Function getColor) {
  return Container(
    height: 5,
    width: 40,
    decoration: BoxDecoration(
      color: getColor(color),
      borderRadius: BorderRadius.circular(20),
    ),
  );
}
```

Voici ce qui se passe :

* `buildContainer` : Une fonction qui crée un petit `Container` arrondi pour représenter une couleur de produit disponible. Elle prend le nom de la couleur sous forme de chaîne et une fonction `getColor` pour la convertir en un objet `Color`.
    

#### `search_section.dart` :

Ajoutez ce code à `lib/widgets/search_section.dart` :

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SearchSection extends StatelessWidget {
  const SearchSection({
    super.key,
    required this.searchController,
  });

  final TextEditingController searchController;

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: searchController,
      decoration: InputDecoration(
        prefixIcon: const Icon(
          CupertinoIcons.search,
          color: Colors.black,
        ),
        hintText: 'Entrez un mot-clé',
        label: const Text(
          'Rechercher ici',
        ),
        fillColor: Colors.grey.withOpacity(0.1),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
        ),
      ),
    );
  }
}
```

Dans ce code :

* `SearchSection` : Un `StatelessWidget` qui affiche un champ de saisie de recherche.
    
* `searchController` : Un `TextEditingController` pour gérer la saisie de texte.
    
* `InputDecoration` : Style le champ de texte avec une icône de recherche, un texte d'indice, une étiquette et des bordures arrondies.
    

#### `show_modal.dart` :

Ajoutez ce code à `lib/widgets/show_modal.dart` :

```dart
// show modal for image
import 'package:flutter/material.dart';

import '../models/product.dart';


void showImageModal(BuildContext context,Product product) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return Dialog(
        insetPadding: const EdgeInsets.all(12),
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
        ),
        child: Padding(
          padding: const EdgeInsets.all(3.0),
          child: Stack(children: [
            ClipRRect(
              borderRadius: BorderRadius.circular(20),
              child: Image(
                width: double.infinity,
                fit: BoxFit.cover,
                image: NetworkImage(product.imageUrl),
              ),
            ),
            Positioned(
              right: 1,
              child: Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(10),
                  color: Colors.grey.withOpacity(0.5),
                ),
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Row(
                    children: [
                      Text(product.name),
                      const SizedBox(width: 5),
                      Text(
                        '\$${product.price}',
                        style: const TextStyle(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            )
          ]),
        ),
      );
    },
  );
}
```

Dans ce code :

* `showImageModal` : Une fonction qui affiche un dialogue avec une vue agrandie de l'image du produit, son nom et son prix.
    
* `Dialog` : Un dialogue de conception matérielle (material design).
    
* `Stack` avec `Positioned` : Utilisé pour superposer le nom et le prix du produit sur l'image.
    

#### `single_product.dart` :

Ajoutez ce code à `lib/widgets/single_product.dart` :

```dart
import 'package:flutter/material.dart';

import '../models/product.dart';



class SingleProduct extends StatelessWidget {
  const SingleProduct({
    super.key,
    required this.product,
  });

  final Product product;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.grey.withOpacity(0.1),
        borderRadius: BorderRadius.circular(10),
      ),
      child: Column(
        children: [
          ClipRRect(
            borderRadius: const BorderRadius.only(
              topRight: Radius.circular(10),
              topLeft: Radius.circular(10),
            ),
            child: Hero(
              tag: product.id,
              child: Image.network(
                product.imageUrl,
                height: 120,
                width: double.infinity,
                fit: BoxFit.cover,
              ),
            ),
          ),
          const SizedBox(height: 10),
          Text(
            product.name,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 10),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text('\$${product.price}'),
                Text(
                  '\$${product.price}',
                  style: const TextStyle(
                    decoration: TextDecoration.lineThrough,
                  ),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }
}
```

Voici ce qui se passe :

* `SingleProduct` : Un `StatelessWidget` qui affiche un seul article de produit dans la grille.
    
* `product` : L'objet `Product` à afficher.
    
* `Container` : Fournit une couleur d'arrière-plan et des bordures arrondies.
    
* Animation `Hero` pour l'image : Facilite une animation fluide lors de la transition vers le `ProductDetailsScreen`.
    
* `Text` pour le nom du produit : Affiche le nom du produit, tronqué s'il est trop long.
    
* `Row` pour les prix : Affiche le prix actuel et le prix précédent barré.
    

## Quelques captures d'écran :

![Page d'accueil de l'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1703872135819/0470da63-f9e7-4358-a523-803222e8469e.png align="center")

![page de détail du produit](https://cdn.hashnode.com/res/hashnode/image/upload/v1703872148850/fc84b934-844f-4dee-8b09-3c7fcf03ce78.png align="center")

![prévisualiseur d'image](https://cdn.hashnode.com/res/hashnode/image/upload/v1703872217140/610e283e-2588-446e-9a0f-300e3f1d961c.png align="center")

![section inférieure de la page de détail](https://cdn.hashnode.com/res/hashnode/image/upload/v1703872162253/6c7de9e7-b5f4-4773-91b8-df5e97a4d0cc.png align="center")

![affichage de la boîte de dialogue dans la page de détail du produit](https://cdn.hashnode.com/res/hashnode/image/upload/v1703872199030/bc0cd8d3-4028-4bff-bf5a-620e32fcdd45.png align="center")

## Conclusion

`go_router` est une bibliothèque de routage puissante et flexible pour Flutter, offrant une API propre et intuitive pour la navigation. Que vous construisiez une application simple ou une structure de navigation complexe, `go_router` fournit les outils dont vous avez besoin pour créer une expérience utilisateur fluide.

En suivant ce guide complet, vous devriez maintenant être bien équipé pour intégrer et exploiter `go_router` dans vos projets Flutter. L'exemple fourni d'une application de shopping minimaliste démontre l'application pratique de ses fonctionnalités.

### Références

1. Pour des fonctionnalités plus avancées et des exemples de code détaillés, reportez-vous à la [documentation officielle de `go_router`](https://pub.dev/packages/go_router)
    
2. Vous pouvez également consulter le [dépôt GitHub de `go_router`](https://github.com/flutter/packages/blob/main/packages/go_router)