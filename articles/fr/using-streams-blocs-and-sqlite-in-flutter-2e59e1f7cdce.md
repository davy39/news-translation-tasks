---
title: Comment utiliser les Streams, les BLoCs et SQLite dans Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-17T19:58:12.000Z'
originalURL: https://freecodecamp.org/news/using-streams-blocs-and-sqlite-in-flutter-2e59e1f7cdce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ihvDZXwv6oGz760kKUgYTQ.png
tags:
- name: Apps
  slug: apps-tag
- name: Flutter
  slug: flutter
- name: General Programming
  slug: programming
- name: SQLite
  slug: sqlite
- name: 'tech '
  slug: tech
seo_title: Comment utiliser les Streams, les BLoCs et SQLite dans Flutter
seo_desc: 'By Eric Grandt

  Recently, I’ve been working with streams and BLoCs in Flutter to retrieve and display
  data from an SQLite database. Admittedly, it took me a very long time to make sense
  of them. With that said, I’d like to go over all this in hopes yo...'
---

Par Eric Grandt

Récemment, j'ai travaillé avec des streams et des BLoCs dans Flutter pour récupérer et afficher des données à partir d'une base de données SQLite. Je dois admettre que cela m'a pris beaucoup de temps pour les comprendre. Cela dit, j'aimerais passer en revue tout cela dans l'espoir que vous vous sentirez confiant dans leur utilisation au sein de vos propres applications. Je vais entrer dans autant de détails que possible et expliquer tout cela aussi simplement que possible.

Dans cet article, nous allons créer une application simple de A à Z qui utilise des streams, des BLoCs et une base de données SQLite. Cette application nous permettra de créer, modifier et supprimer des notes. Si vous ne l'avez pas encore fait, créez une nouvelle application Flutter basique en utilisant `flutter create APPNAME`. Il sera beaucoup plus facile de comprendre tout cela si vous commencez à partir de zéro. Ensuite, plus tard, implémentez ce que vous avez appris dans vos applications existantes.

La première chose à faire est de créer une classe pour gérer la création de nos tables et pour interroger la base de données. Pour cela, nous devons ajouter `sqflite` et `path_provider` comme dépendances dans notre fichier `pubspec.yaml`.

<script src="https://gist.github.com/Erigitic/b7f663db0901d93295c3c4c7a0f50495.js"></script>

Au cas où cela ne s'exécuterait pas automatiquement, exécutez `flutter packages get` pour récupérer les packages. Une fois terminé, créez un dossier `data` et un fichier `database.dart` à l'intérieur. Cette classe créera un singleton afin que nous puissions accéder à la base de données depuis d'autres fichiers, ouvrir la base de données et exécuter des requêtes sur cette base de données. J'ai inclus des commentaires pour expliquer certaines parties du code.

<script src="https://gist.github.com/Erigitic/f6835ec9f36832eb7440a6ab1a4443a7.js"></script>

Créez un autre dossier, `models`, et ajoutez-y un fichier : `note_model.dart`. Voici un excellent outil pour créer facilement des modèles : [https://app.quicktype.io/#l=dart](https://app.quicktype.io/#l=dart).

**NOTE :** Gardez à l'esprit que les modèles n'ont pas à copier les colonnes de la table. Par exemple, si vous avez un identifiant d'utilisateur stocké dans une table en tant que clé étrangère, le modèle ne devrait probablement pas contenir cet identifiant d'utilisateur. Au lieu de cela, le modèle devrait utiliser cet identifiant d'utilisateur afin de récupérer un objet `User` réel.

<script src="https://gist.github.com/Erigitic/5a70f4a10130fba98155fd93f03c108c.js"></script>

Avec notre modèle de note créé, nous pouvons ajouter les fonctions finales à notre fichier de base de données qui géreront toutes les requêtes liées aux notes.

<script src="https://gist.github.com/Erigitic/88a40ab6402dc9ac274b45a1f233505e.js"></script>

Commençons maintenant avec les streams et les BLoCs. Si c'est la première fois que vous travaillez avec ceux-ci, cela peut être assez intimidant. Je vous promets cependant que les streams et les BLoCs sont exceptionnellement simples une fois que vous avez passé la phase d'apprentissage.

La première chose dont nous avons besoin est un dossier `blocs` dans le dossier `data`. Ce dossier contiendra tous nos BLoCs, comme le suggère le nom. Créons les fichiers pour chaque BLoC : `bloc_provider.dart`, `notes_bloc.dart` et `view_note_bloc.dart`. Un BLoC par page et un pour fournir les BLoCs à ces pages.

Le `bloc_provider` est responsable de fournir facilement à nos pages le BLoC nécessaire, puis de le disposer lorsque cela est nécessaire. Chaque fois que nous voulons utiliser un BLoC, nous utiliserons le `bloc_provider`.

<script src="https://gist.github.com/Erigitic/f21abb7afa652d75a67a64a087072eb6.js"></script>

Chaque fois que nous avons besoin d'un BLoC sur l'une de nos pages, nous utiliserons le `BlocProvider` comme ceci :

<script src="https://gist.github.com/Erigitic/f72c35d2cbc3291a904e75dddcda6ae3.js"></script>

Créons notre BLoC de notes qui gérera la récupération de toutes nos notes et l'ajout de nouvelles notes à la base de données. Puisque nos BLoCs sont spécifiques à une page, ce BLoC ne sera utilisé que sur la page des notes. J'ai commenté le code pour expliquer ce qui se passe.

<script src="https://gist.github.com/Erigitic/edb7fe1650f1f9a248d81a0bb12696da.js"></script>

Avec le BLoC de notes créé, nous avons tout ce dont nous avons besoin pour créer notre page de notes. Cette page affichera toutes nos notes et nous permettra d'en ajouter de nouvelles. Nous mettrons le code de notre page de notes dans `main.dart`. Une fois de plus, j'ai commenté toutes les parties nécessaires du code pour expliquer ce qui se passe.

<script src="https://gist.github.com/Erigitic/b278a95269fa712f06c83927a8a480f1.js"></script>

Maintenant, nous avons besoin d'un moyen de visualiser, modifier, sauvegarder et supprimer les notes. C'est là que le BLoC de visualisation de notes et la page de visualisation de notes entrent en jeu. Nous commencerons par `view_note_bloc.dart`.

<script src="https://gist.github.com/Erigitic/5b7c50bbe9eeae3d2c7dfaa898eda203.js"></script>

Maintenant, nous pouvons construire la page réelle pour nous permettre d'interagir avec nos notes. Le code de cette page ira dans `view_note.dart`.

<script src="https://gist.github.com/Erigitic/a9af0325bab99057f71c313fd9b3b5d4.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/VM6e-BtScNO6RMweffYoZGr8kiqmcnstM2DE)
_Application finale utilisant des streams, des BLoCs et SQLite_

C'est tout ce qu'il faut pour travailler avec des streams, des BLoCs et SQLite. En les utilisant, nous avons créé une application super simple qui nous permet de créer, visualiser, modifier et supprimer des notes. J'espère que ce guide vous a rendu plus confiant dans le travail avec les streams. Vous serez maintenant en mesure de les implémenter dans vos propres applications avec facilité. Si vous avez des questions, n'hésitez pas à laisser un commentaire car j'adorerais y répondre. Merci d'avoir lu.

Voir le code complet ici : [https://github.com/Erigitic/flutter-streams](https://github.com/Erigitic/flutter-streams)