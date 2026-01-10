---
title: Comment utiliser part dans Dart – Diviser les fichiers pour un accès limité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-03T16:17:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-part-in-dart
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/parts-in-dart-1.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment utiliser part dans Dart – Diviser les fichiers pour un accès limité
seo_desc: 'By Rutvik Tak

  When you''re coding in Dart, you may come across these  following situations:


  A class/method is associated with a particular file of your codebase and you want
  to keep it private only to that one file.

  You want to break your one big fil...'
---

Par Rutvik Tak

Lorsque vous codez en Dart, vous pouvez rencontrer les situations suivantes :

1. Une classe/méthode est associée à un fichier particulier de votre base de code et vous souhaitez la garder privée à ce fichier uniquement.
2. Vous souhaitez diviser votre gros fichier en différentes parties mais éviter d'utiliser accidentellement des membres privés de ce fichier dans d'autres sections de votre base de code.

Maintenant, pour résoudre le premier problème, vous pourriez dire que c'est assez simple, n'est-ce pas ? Vous rendez simplement la `classe/méthode` privée dans ce fichier, afin qu'elle ne soit accessible qu'à l'intérieur de celui-ci. Comme ceci :

```dart
// Classe privée accessible uniquement dans le fichier où elle est déclarée.

class _MyPrivateClassOne {	

}
```

Oui, c'est une façon de faire. Mais ce n'est peut-être pas la manière la plus appropriée dans certains cas.

Si vous continuez à faire cela, vous allez rencontrer le deuxième problème que nous avons mentionné. Vous aurez bientôt un fichier très volumineux avec plusieurs membres à l'intérieur. Et il deviendra très rapidement pénible de gérer et de naviguer dans différentes parties de ce fichier.

## **Comment utiliser `part` dans Dart**

C'est là que `part` intervient. C'est une fonctionnalité intéressante du langage **Dart** qui facilite la division d'un fichier en différentes parties pour mieux gérer et naviguer dans le fichier à mesure qu'il grandit.

Nous allons examiner l'exemple suivant :

```
// main_file.dart

part "private_class2.dart"

void main() { 

final privateClassOne = _PrivateClassOne();
final privateClassTwo = _PrivateClassTwo();

}

// private_class1.dart

part of "main_file.dart"

class _PrivateClassOne{

}

// private_class2.dart

part of "main_file.dart"

class _PrivateClassTwo{

}
```

Décomposons l'exemple ci-dessus et comprenons ce que nous faisons ici :

```dart
// #1 Déclaration des parties privées

part "private_class1.dart"

part "private_class2.dart"

void main() { 

final privateClassOne = _PrivateClassOne();
final privateClassTwo = _PrivateClassTwo();

}

```

Dans la première étape, nous avons déclaré les fichiers dans lesquels nous voulons diviser notre fichier principal.

Deuxièmement, dans les fichiers respectifs `private_class1.dart` et `private_class2.dart`, nous devons ajouter la ligne suivante en haut de ces fichiers pour les associer au fichier principal :

```dart
// #2 Association du fichier avec le fichier principal pour l'accès.

part of "main_file.dart"

class _PrivateClassOne{

}
```

De cette manière, vous êtes en mesure de diviser votre gros fichier en plusieurs parties pour une meilleure gestion et lisibilité.

## **Autres exemples d'utilisation de `part`**

Un package populaire qui utilise `part` est **[Freezed](https://pub.dev/packages/freezed)**. C'est un package pour la génération de code pour les `data-classes/unions/pattern-matching/cloning`. Vous pouvez, par exemple, l'utiliser pour créer des méthodes d'assistance sur votre modèle comme `fromJson/toJson` qui vous permet de prendre des données JSON et de les convertir en votre modèle ou vice-versa.

Pour en savoir plus sur **Freezed**, vous pouvez consulter [pub.dev](https://pub.dev/packages/freezed).

Chaque fois que vous générez un modèle **Freezed** – par exemple, `Screenshot` et qu'il se trouve dans un fichier `screenshot.dart` – vous remarquerez qu'il génère deux autres fichiers, `screenshot.freezed.dart` et `screenshot.g.dart`. Ceux-ci incluent les méthodes d'assistance comme `fromJson/toJson/copyWith`.

Vous remarquerez que, au début de votre fichier de modèle **Freezed**, vous devez ajouter ces deux lignes :

```dart
// #1 Déclaration des fichiers privés séparés

part 'screenshot.freezed.dart';

part 'screenshot.g.dart';
```

Comme nous l'avons discuté dans notre exemple précédent, ici vous mentionnez les parties de votre fichier principal `screenshot.dart` modèle.

Et ces deux fichiers générés ont la ligne suivante ajoutée à leur début :

```dart
// #2 Association des fichiers privés respectifs avec le fichier principal

part of 'screenshot.dart';
```

Ici, **Freezed** génère ces autres méthodes d'assistance que votre modèle utilise. Mais il les divise dans ces différents fichiers pour garder les parties du code généré à l'écart de vous, dont vous n'avez pas besoin de vous soucier.

## **Cas d'utilisation pour part**

Actuellement, je travaille sur mon projet personnel, [AppShots](https://appshots.co/) où j'ai dû utiliser `part` pour résoudre un problème réel.

J'ai deux couches de base de données, `PrimaryDatabaseLayer` et `_SecondaryDatabaseLayer` dans mon application Flutter. La couche `_SecondaryDatabaseLayer` communiquerait directement avec la base de données locale pour ajouter/mettre à jour/supprimer des éléments.

Voyons à quoi ressemble la `PrimaryDatabaseLayer` :

```dart
// primary_database_layer.dart

part "secondary_database_layer.dart"

class PrimaryDatabaseLayer {

	Future<Screenshot1> addScreenshot(....){
	  // convertir le modèle de Screenshot1 à Screenshot2 et appeler la méthode addScreenshot de _SecondaryDatabase avec Screenshot2
		....
        .......
	}

	Future<Screenshot1> updateScreenshot(....){
		// mettre à jour la capture d'écran dans la base de données locale
		....
        .......
	}

	Future<Screenshot1> deleteScreenshot(....){
		// supprimer la capture d'écran de la base de données locale
		....
        .......
	}

}
```

Ensuite, j'avais la deuxième couche comme suit :

```dart
// secondary_database_layer.dart

part of "primary_database_layer.dart"

class _SecondaryDatabaseLayer {

	Future<Screenshot2> addScreenshot(....){
		// ajouter la capture d'écran à la base de données locale
		....
        .......
	}

	Future<Screenshot2> updateScreenshot(....){
		// mettre à jour la capture d'écran dans la base de données locale
		....
        .......
	}

	Future<Screenshot2> deleteScreenshot(....){
		// supprimer la capture d'écran de la base de données locale
		....
        .......
	}

}
```

La principale raison d'avoir deux couches de base de données ici était que j'avais deux modèles différents, `Screenshot1` et `Screenshot2`. Le modèle `Screenshot2` est adapté pour interagir avec la base de données locale réelle et `Screenshot1` est le modèle que j'ai utilisé dans **la logique métier de l'application et les vues de l'interface utilisateur**.

Maintenant, comme vous pouvez le voir, la `PrimaryDatabaseLayer` est simplement un wrapper autour de la `_SecondaryDatabaseLayer` pour la conversion pratique des modèles de données.

L'ajout de la `_SecondaryDatabaseLayer` dans le même fichier que `PrimaryDatabaseLayer` rend difficile la gestion et la navigation à mesure que les couches grandissent en termes de fonctionnalités. J'ai donc utilisé `part` ici pour faire de la `_SecondaryDatabaseLayer` une partie de la `PrimaryDatabaseLayer`.

## **Conclusion**

Dans ce tutoriel, nous avons discuté de la manière d'utiliser `part` dans **Dart** pour améliorer votre base de code. Et vous avez appris quelques exemples où l'utilisation de `part` est bénéfique et facilite la gestion de votre code.

☁️ J'espère que vous avez apprécié cet article. Je prévois de publier plus de contenu où je partagerai mes expériences/défis dans la construction de projets personnels/professionnels en Dart et Flutter pour vous aider à devenir un meilleur développeur. 📊

Si vous avez aimé cet article et que vous avez des questions ou souhaitez entrer en contact, vous pouvez me rejoindre sur Twitter [**@TakRutvik**](https://twitter.com/TakRutvik) où je suis actif et partage toutes mes découvertes et les projets intéressants sur lesquels je travaille. ✨

Passez une excellente journée ! ☁️

Continuez à Flutterer 💙