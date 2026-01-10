---
title: Comment créer des applications mobiles avec Flutter
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-02-28T01:10:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-mobile-apps-with-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/flutter.jpeg
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment créer des applications mobiles avec Flutter
seo_desc: "Flutter is a mobile app development framework from Google that lets you\
  \ build beautiful, high-performance iOS and Android applications. \nIn this article,\
  \ let’s look at what Flutter is and how to work with it.\nWhat is Flutter?\nFlutter\
  \ is an open-sourc..."
---

Flutter est un framework de développement d'applications mobiles de Google qui vous permet de créer des applications iOS et Android belles et haute performance. 

Dans cet article, examinons ce qu'est Flutter et comment travailler avec.

## Qu'est-ce que Flutter ?

Flutter est un framework de développement d'applications mobiles open-source créé par Google. Il vous aide à créer des applications de haute qualité, rapides et belles pour iOS, Android et le web – le tout à partir d'une seule base de code.

Flutter est rapidement devenu un choix populaire parmi les développeurs. Grâce à sa facilité d'utilisation et ses performances, vous pouvez créer de belles applications mobiles en utilisant Flutter.

## Avantages de Flutter

Flutter utilise le [langage de programmation Dart](https://dart.dev/) de Google. Dart est similaire à JavaScript ou TypeScript et offre un modèle de programmation réactive pour construire des interfaces utilisateur.

Cela signifie que, au lieu de devoir mettre à jour l'interface utilisateur lorsque vous modifiez votre code, le framework le fera pour vous. Cela rend plus facile et plus efficace la construction d'interfaces utilisateur dynamiques et réactives.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/flutter1.gif)
_Rechargement à chaud de Flutter. Image de l'auteur._

Flutter a également un cycle de développement rapide. Flutter dispose d'une fonctionnalité de rechargement à chaud qui vous permet de voir les modifications que vous apportez au code immédiatement. Avec Flutter, vous n'avez pas à attendre que le code compile à chaque fois que vous modifiez un morceau de code.

La force centrale de Flutter réside dans les widgets.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/flutter2.gif)
_Widgets Flutter_

Lors de la création d'une application, vous devez généralement écrire la fonctionnalité à partir de zéro. Par exemple, si vous souhaitez intégrer une carte Google dans votre code, vous devez écrire le code pour importer Google Maps dans votre application.

Mais Flutter fournit des widgets prêts à l'emploi pour presque toutes les fonctions courantes des applications. Pensez-y comme travailler avec un ensemble de lego. Flutter fournit un ensemble riche de widgets préconçus que vous pouvez personnaliser pour créer de belles interfaces.

Ces widgets ne sont pas de simples éléments d'interface utilisateur comme des boutons et des zones de texte. Ils incluent des widgets complexes comme des listes déroulantes, des navigations, des curseurs et bien d'autres. Ces widgets vous aident à gagner du temps et vous permettent de vous concentrer sur la logique métier de votre application.

[Voici une liste complète des widgets intégrés de Flutter](https://docs.flutter.dev/development/ui/widgets) que vous pouvez consulter.

Un autre avantage de Flutter est sa performance.

Le moteur graphique de Flutter, Skia, dessine chaque pixel à l'écran. Cela permet d'obtenir des animations fluides à 60 images par seconde, même sur des appareils bas de gamme.

Flutter dispose également d'une grande communauté de développeurs en croissance qui contribuent au framework. Il est également livré avec une documentation détaillée et une vaste bibliothèque de packages et de plugins. Vous pouvez facilement intégrer ces plugins dans votre application pour ajouter des fonctionnalités comme des cartes, la communication réseau et le stockage local.

Maintenant que vous savez ce qu'est Flutter et pourquoi il est utile, voyons comment il se compare à une autre bibliothèque populaire, React-Native.

## React Native vs. Flutter

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-153.png)
_Flutter vs React Native_

React Native et Flutter sont deux des frameworks de développement d'applications mobiles multiplateformes les plus populaires disponibles aujourd'hui. Tous deux offrent la possibilité de créer des applications mobiles haute performance et visuellement attrayantes pour plusieurs plateformes.

Mais il existe quelques différences clés entre les deux frameworks que vous devez prendre en compte lors du choix de celui qui convient à votre projet.

React Native est basé sur JavaScript et est une extension de la [bibliothèque React](https://reactjs.org/). React-native utilise des composants natifs pour construire l'interface utilisateur, ce qui donne à l'application une apparence et une sensation natives.

React Native dispose d'une grande communauté établie par rapport à Flutter et est un excellent choix si vos produits existants utilisent JavaScript ou React.

Flutter offre une approche unique pour construire des interfaces utilisateur en utilisant son propre ensemble de widgets personnalisables. Cette approche donne à Flutter une apparence et une sensation uniques par rapport aux autres frameworks de développement mobile.

Le cycle de développement rapide de Flutter et sa fonctionnalité de rechargement à chaud permettent aux développeurs de construire des applications plus rapidement que les autres alternatives.

React Native a une courbe d'apprentissage plus facile par rapport à Flutter. Puisque la plupart des développeurs connaissent JavaScript, ils n'ont pas à apprendre un nouveau langage comme Dart pour construire des applications avec Flutter.

Mais la dépendance de React Native aux composants natifs rend difficile l'obtention de performances cohérentes sur plusieurs plateformes. Cela peut également entraîner des incohérences dans l'interface utilisateur entre iOS et Android.

Flutter offre de meilleures performances, avec son moteur graphique dessinant chaque pixel à l'écran. Avec Flutter, vous pouvez obtenir des animations fluides et fluides même sur du matériel bas de gamme. Flutter offre également une apparence et une sensation unifiées et cohérentes pour l'application sur toutes les plateformes, car les développeurs utilisent le même ensemble de widgets pour construire l'interface utilisateur.

Ainsi, React Native et Flutter ont tous deux leurs propres forces et faiblesses, et le bon choix dépend de vos besoins et exigences spécifiques.

React Native est un bon choix pour les entreprises ayant des investissements existants dans JavaScript et React. Flutter est un meilleur choix pour les projets qui nécessitent des interfaces utilisateur haute performance, uniques et réactives, ainsi qu'un cycle de développement rapide.

## Comment installer Flutter

La meilleure façon d'installer Flutter est de suivre la [page d'installation officielle](https://docs.flutter.dev/get-started/install). Vous pouvez choisir votre système d'exploitation et suivre les instructions.

Une fois que vous avez installé Flutter, vous pouvez utiliser son outil intégré appelé Flutter doctor pour vérifier les composants. Par exemple, sur Mac, vous devriez voir une réponse similaire en exécutant `flutter doctor`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-154.png)
_Flutter doctor_

## Hello World dans Flutter

Créons une simple application hello world en utilisant Flutter.

Nous pouvons utiliser `flutter create <nom de l'application>` pour créer une nouvelle application.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-155.png)
_Flutter create_

Maintenant, nous pouvons nous déplacer dans le répertoire et modifier le fichier principal. Il sera situé sous <nom_de_l'application>/lib/main.dart. Remplacez le code dans le fichier main.dart par le code suivant :

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bonjour, le monde !',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Bonjour, le monde !'),
        ),
        body: const Center(
          child: Text('Bonjour, le monde !'),
        ),
      ),
    );
  }
}
```

Ce code définit une application Flutter qui affichera « Bonjour, le monde ! » au centre de l'écran. La fonction main() appellera la fonction runApp() avec une instance de la classe MyApp.

Dans la méthode build() de MyApp, un widget MaterialApp avec le titre « Bonjour, le monde ! » est créé. Le widget Scaffold contient une AppBar avec le titre « Bonjour, le monde ! » et le widget Center placera le texte au centre de l'écran.

Voici à quoi ressemblera la sortie après avoir exécuté la commande `flutter run`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-156.png)
_Flutter hello world_

## Qu'est-ce que Flutterflow ?

![Image](https://www.freecodecamp.org/news/content/images/2023/02/flutter3.gif)
_Flutterflow. Crédits : Flutterflow.io_

Avant de terminer, je veux partager un outil qui a considérablement amélioré ma productivité lors de la création d'applications avec Flutter. Ce n'est pas une recommandation – je veux simplement que vous sachiez que cet outil existe.

[Flutter Flow](https://flutterflow.io/) est un outil de conception visuelle qui vous permet de créer des applications Flutter en utilisant une interface glisser-déposer. Vous pouvez créer des interfaces utilisateur complexes et interactives pour vos applications Flutter sans écrire de code.

Flutterflow fonctionne en fournissant une interface visuelle pour concevoir l'interface utilisateur de votre application, qui est ensuite traduite en code Flutter. Il facilite la création et l'itération sur la conception de votre application, car vous pouvez voir les modifications que vous apportez en temps réel.

Flutterflow offre également un développement collaboratif, vous pouvez donc créer vos applications avec une équipe. Flutterflow est livré avec de nombreuses intégrations comme Firebase, Stripe et même l'API d'OpenAI.

Une fois que vous avez construit votre application, vous pouvez la publier sur l'app store ou le play store en utilisant l'intégration Codemagic intégrée.

## Conclusion

Flutter est un framework génial pour créer des applications mobiles. Il offre des temps de développement rapides, des designs beaux et réactifs, et une seule base de code pour iOS et Android. Sa fonctionnalité de rechargement à chaud permet aux développeurs de voir les modifications en temps réel, réduisant ainsi le temps de développement global.

De plus, la bibliothèque de widgets de Flutter permet de créer des designs personnalisés et complexes avec facilité. En termes de performance, Flutter devance largement des alternatives comme React-Native.

_J'espère que cet article vous a aidé à comprendre Flutter en détail. Vous pouvez en apprendre plus sur moi sur_ [_manishmshiva.com_](http://manishmshiva.com)_._