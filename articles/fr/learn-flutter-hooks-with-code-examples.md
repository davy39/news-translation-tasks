---
title: Apprendre les Flutter Hooks – Les hooks courants expliqués avec des exemples
  de code
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-26T13:19:39.711Z'
originalURL: https://freecodecamp.org/news/learn-flutter-hooks-with-code-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758892716695/6af49b6f-d088-405a-9c48-57d5db3b0a98.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: hooks
  slug: hooks
seo_title: Apprendre les Flutter Hooks – Les hooks courants expliqués avec des exemples
  de code
seo_desc: Flutter hooks are powerful functions that streamline state management, side
  effects handling, and code organization in Flutter applications. Inspired by React
  hooks, they provide a more concise and modular approach compared to traditional
  StatefulWid...
---

Les Flutter hooks sont des fonctions puissantes qui simplifient la gestion de l'état, la manipulation des effets secondaires et l'organisation du code dans les applications Flutter. Inspirés des hooks React, ils offrent une approche plus concise et modulaire par rapport aux modèles traditionnels `StatefulWidget` et `setState`.

À la fin de ce guide, vous comprendrez les hooks essentiels de Flutter, comment les utiliser efficacement, comment créer vos propres hooks personnalisés et les meilleures pratiques pour les utiliser dans des projets réels.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Pourquoi utiliser les Flutter Hooks ?](#heading-pourquoi-flutter-hooks)
    
* [Hooks Flutter courants](#heading-hooks-flutter-courants)
    
    * [Comment utiliser le hook useState dans Flutter](#heading-comment-utiliser-le-hook-usestate-dans-flutter)
        
    * [Comment utiliser le hook useAnimationController dans Flutter](#heading-comment-utiliser-le-hook-useanimationcontroller-dans-flutter)
        
    * [Comment utiliser le hook useEffect dans Flutter](#heading-comment-utiliser-le-hook-useeffect-dans-flutter)
        
    * [Comment utiliser le hook useMemoized dans Flutter](#heading-comment-utiliser-le-hook-usememoized-dans-flutter)
        
    * [Comment utiliser le hook useRef dans Flutter](#heading-comment-utiliser-le-hook-useref-dans-flutter)
        
    * [Comment utiliser le hook useCallback dans Flutter](#heading-comment-utiliser-le-hook-usecallback-dans-flutter)
        
    * [Comment utiliser le hook useContext dans Flutter](#heading-comment-utiliser-le-hook-usecontext-dans-flutter)
        
    * [Comment utiliser le hook useTextEditingController dans Flutter](#heading-comment-utiliser-le-hook-usetexteditingcontroller-dans-flutter)
        
* [Comment créer un hook personnalisé dans Flutter](#heading-comment-creer-un-hook-personnalise-dans-flutter)
    
* [Hooks avancés](#heading-hooks-avances)
    
* [Démonstration : Exemple de compteur avec des hooks](#heading-demonstration-exemple-de-compteur-avec-des-hooks)
    
* [Bonnes pratiques](#heading-bonnes-pratiques)
    
* [Hooks vs Stateful Widgets](#heading-hooks-vs-widgets-a-etat)
    
* [Ressources supplémentaires](#heading-ressources-supplementaires)
    

## Prérequis

Avant de plonger dans les Flutter hooks, assurez-vous de disposer des éléments suivants :

* **Flutter SDK** : Installé et configuré (Flutter 3.x ou supérieur recommandé). Vérifiez avec :
    
    ```bash
    flutter --version
    ```
    
* **Dart SDK** : Inclus avec Flutter, assurez-vous qu'il est à jour.
    
* **IDE** : Visual Studio Code, Android Studio ou IntelliJ avec les extensions Flutter.
    
* **Connaissances de base de Flutter** : Familiarité avec les widgets, `StatelessWidget`, `StatefulWidget` et les bases de la gestion d'état.
    
* **Dépendance du package** : Le package `flutter_hooks` installé en ajoutant ce qui suit au fichier `pubspec.yaml` :
    
    ```yaml
    dependencies:
      flutter_hooks: ^0.21.3+1
    ```
    
    Ensuite, exécutez :
    
    ```bash
    flutter pub get
    ```
    

## Pourquoi utiliser les Flutter Hooks ?

Voici quelques-uns des avantages de l'utilisation des Flutter hooks :

1. **Lisibilité et maintenabilité améliorées**  
    Les hooks réduisent le code redondant (boilerplate) en intégrant la logique d'état et d'effets secondaires directement dans la méthode build du widget. Cela rend le code plus propre et plus facile à comprendre.
    
2. **Réutilisabilité**  
    Les hooks peuvent être abstraits dans des hooks personnalisés. Par exemple, vous pourriez extraire une logique complexe (comme la récupération de données) dans une fonction réutilisable.
    
3. **Gestion d'état granulaire**  
    Au lieu de gérer un seul objet `State` pour un widget entier, les hooks vous permettent de gérer de petits morceaux d'état indépendants. C'est particulièrement utile pour les interfaces utilisateur complexes.
    
4. **Effets secondaires simplifiés**  
    Les hooks tels que `useEffect` offrent un moyen élégant de gérer les tâches liées au cycle de vie, comme la récupération de données, les écouteurs (listeners) ou les abonnements.
    

## Hooks Flutter courants

Parcourons les hooks les plus courants, avec des explications ligne par ligne.

### Comment utiliser le hook `useState` dans Flutter

C'est le hook le plus simple et le plus utilisé. Il vous permet de déclarer et de gérer un état à l'intérieur d'un `HookWidget`.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class CounterButton extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final counter = useState<int>(0); // Étape 1 : créer l'état avec une valeur initiale de 0

    return ElevatedButton(
      onPressed: () => counter.value++, // Étape 2 : mettre à jour l'état via counter.value
      child: Text('Compte : ${counter.value}'), // Étape 3 : lire l'état
    );
  }
}
```

**Explication**

* `useState<int>(0)` initialise l'état avec une valeur de `0`.
    
* `counter.value` lit la valeur de l'état.
    
* La mise à jour de `counter.value` déclenche une reconstruction (rebuild), tout comme `setState`.
    

### Comment utiliser le hook `useAnimationController` dans Flutter

Gère les animations tout en gérant automatiquement le cycle de vie du contrôleur.

```dart
class AnimatedBox extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final controller = useAnimationController(
      duration: const Duration(seconds: 1), // Étape 1 : définir la durée de l'animation
    );

    return FadeTransition(
      opacity: controller, // Étape 2 : lier le contrôleur à l'animation
      child: Container(width: 100, height: 100, color: Colors.blue),
    );
  }
}
```

**Explication**

* Le hook crée un `AnimationController` d'une durée d'une seconde.
    
* Le contrôleur est automatiquement libéré (`disposed`) lorsque le widget est supprimé.
    
* Vous pouvez déclencher des animations avec `controller.forward()` ou `controller.reverse()`.
    

### Comment utiliser le hook `useEffect` dans Flutter

Gère les effets secondaires tels que la récupération de données ou la mise en place d'écouteurs.

```dart
class DataWidget extends HookWidget {
  @override
  Widget build(BuildContext context) {
    useEffect(() {
      fetchData(); // Étape 1 : exécuter l'effet secondaire
      return () => cancelSubscription(); // Étape 2 : nettoyage optionnel
    }, []); // Étape 3 : liste de dépendances

    return Text('Chargement des données...');
  }
}
```

**Explication**

* Le callback s'exécute lors de la construction du widget.
    
* La fonction de nettoyage s'exécute lorsque le widget est supprimé ou que les dépendances changent.
    
* La liste de dépendances vide `[]` signifie que l'effet ne s'exécute qu'une seule fois.
    

### Comment utiliser le hook `useMemoized` dans Flutter

Met en cache les calculs coûteux et réutilise les résultats à moins que les dépendances ne changent.

```dart
final calculatedValue = useMemoized(() => calculateExpensiveValue(), []);
```

**Explication**

* `calculateExpensiveValue()` s'exécute une fois et met le résultat en cache.
    
* Si des dépendances sont fournies, la fonction ne s'exécute à nouveau que lorsqu'elles changent.
    

### Comment utiliser le hook `useRef` dans Flutter

Conserve une référence mutable à travers les reconstructions.

```dart
final textController = useRef(TextEditingController());

TextFormField(
  controller: textController.value,
  decoration: InputDecoration(labelText: 'Nom d\'utilisateur'),
);
```

**Explication**

* `useRef` stocke un objet sans déclencher de reconstructions.
    
* Utile pour les contrôleurs, les focus nodes ou les valeurs mutables qui ne doivent pas être réinitialisées.
    

### Comment utiliser le hook `useCallback` dans Flutter

Mémorise un callback pour éviter les reconstructions inutiles de widgets.

```dart
final onPressed = useCallback(() => print('Appuyé'), []);
```

**Explication**

* Sans `useCallback`, les fonctions peuvent être recréées à chaque reconstruction.
    
* Les callbacks mémorisés améliorent les performances lorsqu'ils sont transmis à des widgets comme `ListView`.
    

### Comment utiliser le hook `useContext` dans Flutter

Fournit un accès direct aux valeurs du `BuildContext` comme les thèmes ou les providers.

```dart
final theme = useContext();
```

### Comment utiliser le hook `useTextEditingController` dans Flutter

Un raccourci pour créer des contrôleurs de texte.

```dart
final usernameController = useTextEditingController();

TextFormField(
  controller: usernameController,
  decoration: InputDecoration(labelText: 'Nom d\'utilisateur'),
);
```

**Explication :**

### 1\. **Qu'est-ce que** `useTextEditingController()` ?

```dart
final usernameController = useTextEditingController();
```

* Normalement dans Flutter, si vous voulez gérer la saisie de texte, vous créez un `TextEditingController`.
    
* Avec un `StatefulWidget` classique, vous feriez quelque chose comme :
    

```dart
late TextEditingController usernameController;

@override
void initState() {
  super.initState();
  usernameController = TextEditingController();
}

@override
void dispose() {
  usernameController.dispose();
  super.dispose();
}
```

* Mais avec les **Flutter Hooks**, vous pouvez remplacer tout ce code redondant par :
    
    ```dart
    final usernameController = useTextEditingController();
    ```
    
* Ce hook effectue automatiquement les actions suivantes :
    
    * **Crée** le contrôleur.
        
    * **Le maintient en vie** tant que le widget existe.
        
    * **Le libère (dispose)** lorsque le widget est détruit.  
        Vous n'avez donc plus besoin de gérer manuellement le cycle de vie.
        

### 2\. **Utilisation du contrôleur dans un** `TextFormField`

```dart
TextFormField(
  controller: usernameController,
  decoration: InputDecoration(labelText: 'Nom d\'utilisateur'),
);
```

* Ce `TextFormField` est lié au `usernameController`.
    
* Tout ce que l'utilisateur tape dans le champ de saisie sera stocké dans `usernameController.text`.
    
* Vous pouvez le lire ou le modifier à tout moment :
    
    ```dart
    print(usernameController.text);  // obtenir le texte saisi
    usernameController.text = "Anthony"; // définir une valeur par défaut
    ```
    

### 3\. **Fonctionnement global**

* `useTextEditingController()` fournit un `TextEditingController` prêt à l'emploi sans les tracas de l'initialisation et de la libération.
    
* Le `TextFormField` utilise ce contrôleur pour gérer la saisie de l'utilisateur.
    
* C'est la **méthode hooks** pour gérer les champs de texte.
    

**Résumé**

* `useTextEditingController()` → Hook pour créer et libérer automatiquement un `TextEditingController`.
    
* `TextFormField(controller: ...)` → Utilise ce contrôleur pour gérer et accéder au texte saisi dans le champ.
    
* Plus propre et plus sûr que la gestion manuelle dans un `StatefulWidget`.
    

## Comment créer un hook personnalisé dans Flutter

Vous pouvez encapsuler la logique dans des hooks réutilisables.

```dart
Future<String> useFetchData() {
  final data = useState<String>('Chargement...');

  useEffect(() {
    Future.microtask(() async {
      data.value = await fetchDataFromApi();
    });
    return null;
  }, []);

  return data.value;
}
```

**Explication :**

### 1\. **Signature de la fonction**

```dart
Future<String> useFetchData()
```

À première vue, on dirait que cette fonction devrait renvoyer un `Future<String>`.  
Mais en réalité, la fonction ne renvoie pas un `Future`, elle renvoie `data.value`, qui est une `String`.

La signature correcte devrait donc être :

```dart
String useFetchData()
```

Parce que vous renvoyez l'état actuel des données, pas un `Future`.

### 2\. **Configuration de l'état**

```dart
final data = useState<String>('Chargement...');
```

* Cela crée une variable d'état `data` avec une valeur initiale de `"Chargement..."`.
    
* `data.value` contient la valeur réelle de la chaîne.
    
* La mise à jour de `data.value` provoquera la reconstruction du widget.
    

### 3\. **Hook d'effet**

```dart
useEffect(() {
  Future.microtask(() async {
    data.value = await fetchDataFromApi();
  });
  return null;
}, []);
```

* `useEffect` s'exécute une fois (car la liste de dépendances `[]` est vide).
    
* À l'intérieur, un `Future.microtask` planifie une tâche asynchrone pour récupérer les données.
    
* Une fois l'appel API terminé, `data.value` est mis à jour avec la réponse de `fetchDataFromApi()`.
    
* La mise à jour de `data.value` déclenche une reconstruction, de sorte que l'interface utilisateur affichera les nouvelles données au lieu de `"Chargement..."`.
    

### 4\. **Valeur de retour**

```dart
return data.value;
```

* Cela renvoie la valeur de l'état actuel (`'Chargement...'` au début, remplacée plus tard par les données récupérées).
    
* Lors de la première construction, vous obtiendrez `"Chargement..."`.
    
* Une fois l'appel API terminé, une reconstruction se produit et maintenant `useFetchData()` renverra la chaîne récupérée.
    

### 5\. **Fonctionnement en pratique**

Imaginez ce code de widget :

```dart
class MyWidget extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final result = useFetchData();

    return Text(result); 
  }
}
```

**Étape 1** → L'interface affiche `"Chargement..."`.  
**Étape 2** → L'API est appelée en arrière-plan.  
**Étape 3** → Lorsque la réponse de l'API arrive, `data.value` est mis à jour.  
**Étape 4** → Le widget se reconstruit et maintenant `Text(result)` affiche les données récupérées.

**Résumé**

* `useState` contient les données (`Chargement...` → résultat récupéré).
    
* `useEffect` s'exécute une fois pour déclencher la récupération asynchrone.
    
* Lorsque la récupération est terminée, l'état est mis à jour → le widget se reconstruit → l'interface affiche la nouvelle valeur.
    
* La fonction devrait renvoyer une `String`, pas un `Future<String>`.
    

## Hooks avancés

* `useListenable` : Fonctionne avec `ValueNotifier` ou `ChangeNotifier`.
    
* `useDebounced` : Temporise la saisie, utile pour les champs de recherche.
    
* `usePreviousState` (provenant de bibliothèques communautaires) : Garde la trace de la valeur précédente.
    

## Démonstration : Exemple de compteur avec des hooks

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class Counter extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final count = useState<int>(0); // variable d'état initialisée à 0

    useEffect(() {
      print('Compte mis à jour : ${count.value}'); // log à chaque changement du compte
      return null; // aucun nettoyage nécessaire
    }, [count.value]); // dépendance : s'exécute à nouveau quand count change

    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text('Vous avez cliqué ${count.value} fois', style: TextStyle(fontSize: 24)),
        ElevatedButton(
          onPressed: () => count.value++, // incrémenter l'état
          child: Text('Incrémenter'),
        ),
      ],
    );
  }
}
```

**Explication :**

Ce code utilise le package `flutter_hooks` pour gérer l'état et le cycle de vie dans un style fonctionnel au lieu du classique `StatefulWidget` + `setState`. Décomposons-le étape par étape :

### 1\. **Définition de la classe**

```dart
class Counter extends HookWidget {
  @override
  Widget build(BuildContext context) {
    ...
  }
}
```

* `Counter` étend `HookWidget` au lieu de `StatelessWidget` ou `StatefulWidget`.
    
* `HookWidget` vous permet d'utiliser des hooks (comme `useState`, `useEffect`) directement dans la méthode `build` pour gérer l'état et les effets secondaires.
    

### 2\. **État avec** `useState`

```dart
final count = useState<int>(0);
```

* `useState` est un hook qui crée un morceau d'état.
    
* Ici, il initialise `count` à `0`.
    
* `count` n'est pas seulement un `int`, mais un `ValueNotifier<int>` (ce qui signifie que vous pouvez lire `count.value` et le mettre à jour en lui assignant une nouvelle valeur via `count.value`).
    

Initialement :  
`count.value = 0`.

### 3\. **Effet avec** `useEffect`

```dart
useEffect(() {
  print('Compte mis à jour : ${count.value}');
  return null;
}, [count.value]);
```

* `useEffect` est utilisé pour effectuer des effets secondaires chaque fois que les dépendances changent.
    
* Dans ce cas, il s'exécute chaque fois que `count.value` change.
    
* Il affiche la valeur mise à jour dans la console à chaque changement du compteur.
    
* Le second argument `[count.value]` est la liste des dépendances (comme les React Hooks). Si `count.value` change, cet effet s'exécute à nouveau.
    

### 4\. **Interface utilisateur (UI)**

```dart
return Column(
  mainAxisAlignment: MainAxisAlignment.center,
  children: [
    Text('Vous avez cliqué ${count.value} fois', style: TextStyle(fontSize: 24)),
    ElevatedButton(
      onPressed: () => count.value++, // incrémenter l'état
      child: Text('Incrémenter'),
    ),
  ],
);
```

* Une `Column` affiche deux widgets :
    
    1. Un widget `Text` montrant le nombre de fois que le bouton a été cliqué.
        
    2. Un `ElevatedButton` qui incrémente le compteur lorsqu'on appuie dessus (`count.value++`).
        

Comme `count` est un `ValueNotifier`, la mise à jour de `count.value` déclenche automatiquement une reconstruction du widget.

### 5\. **Fonctionnement en pratique**

1. L'application affiche : "Vous avez cliqué 0 fois" et un bouton "Incrémenter".
    
2. Lorsque vous appuyez sur le bouton :
    
    * `count.value` augmente de 1.
        
    * Le widget se reconstruit, affichant le nouveau compte.
        
    * `useEffect` s'exécute, affichant `Compte mis à jour : X` dans la console.
        

**Résumé :**  
Ce code est une application de compteur construite avec Flutter Hooks.

* `useState` gère l'état du compteur.
    
* `useEffect` écoute les changements du compteur et exécute un effet secondaire (affichage dans la console).
    
* L'interface affiche le compte et un bouton pour l'incrémenter.
    

## Bonnes pratiques

* **Utilisez correctement les listes de dépendances** avec `useEffect` et `useMemoized`.
    
* **Ne sur-utilisez pas les hooks** : Parfois, un `StatefulWidget` est plus simple.
    
* **Testez minutieusement**, surtout lorsque des effets secondaires sont impliqués.
    
* **Extrayez la logique réutilisable** dans des hooks personnalisés pour que vos widgets restent concentrés sur l'UI.
    

## Hooks vs Stateful Widgets

### **Que sont les Stateful Widgets ?**

Un StatefulWidget est un widget qui peut changer au fil du temps car il détient un état mutable.

* Il est composé de deux classes :
    
    1. `StatefulWidget` → la configuration immuable.
        
    2. `State<T>` → l'état mutable et la logique.
        

### **Comment ils fonctionnent**

* Lorsqu'un élément de l'état change, vous appelez `setState()`.
    
* Cela indique à Flutter de reconstruire l'arbre des widgets avec l'état mis à jour.
    

Exemple :

```dart
class Counter extends StatefulWidget {
  @override
  _CounterState createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int count = 0;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Vous avez cliqué $count fois'),
        ElevatedButton(
          onPressed: () => setState(() => count++),
          child: Text('Incrémenter'),
        ),
      ],
    );
  }
}
```

### **Points clés**

* Adaptés pour les états d'interface simples (compteurs, interrupteurs, champs de formulaire).
    
* Flutter gère le cycle de vie du widget (initialisation, reconstruction, suppression).
    
* Vous gérez l'initialisation dans `initState` et le nettoyage dans `dispose`.
    

**En résumé :**  
Les widgets à état (Stateful widgets) sont la *méthode classique* de gestion d'état dans Flutter. Ils sont intuitifs pour les débutants et parfaits pour des cas d'utilisation simples. Pour une logique d'état plus complexe ou réutilisable, les hooks (ou les bibliothèques de gestion d'état comme BLoC ou Riverpod) peuvent être plus propres et plus évolutifs.

**Résumé :**

* **Hooks** : Plus propres, modulaires, réutilisables, excellents pour la gestion d'état avancée.
    
* **Stateful Widgets** : Plus faciles pour les débutants et suffisants pour les états simples.
    

## Ressources supplémentaires

* [Package flutter\_hooks sur pub.dev](https://pub.dev/packages/flutter_hooks)