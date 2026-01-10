---
title: Utilisez Model-View-ViewModel pour rendre votre code plus propre dans Flutter
  avec Dart Streams
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/app-architecture-mvvm-in-flutter-using-dart-streams-26f6bd6ae4b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9spr-LhRLN2uWPcPqnvvZA.jpeg
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Utilisez Model-View-ViewModel pour rendre votre code plus propre dans Flutter
  avec Dart Streams
seo_desc: 'By QuickBird Studios

  A common problem when developing apps is that you end up with over-complicated classes.
  These classes contain view logic as well as business logic. Both are so intertwined
  that it’s impossible to test them independently. Code-rea...'
---

Par QuickBird Studios

Un problème courant lors du développement d'applications est que vous vous retrouvez avec des classes trop compliquées. Ces classes contiennent à la fois la logique de vue et la logique métier. Les deux sont si imbriquées qu'il est impossible de les tester indépendamment. La lisibilité du code en souffre, et les modifications futures du code sont difficiles à implémenter.

Puisque il y a presque aucune contrainte sur votre architecture dans Flutter, il est assez facile de rencontrer ce problème. Certains développeurs écrivent tout leur code dans le Widget jusqu'à ce qu'ils réalisent le désordre qu'ils ont produit. Réutiliser le code dans d'autres projets semble impossible, et finalement, vous écrivez la plupart de votre code deux fois. Model-View-ViewModel (MVVM) essaie de résoudre cela en séparant la logique métier et les détails de la vue.

Dans cet article, nous vous montrons à quoi pourrait ressembler MVVM avec Flutter. Nous allons créer un ViewModel réactif fonctionnel en utilisant l'API Stream de Dart.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yXqTw6EdqmA1pewkAFvHGQ.jpeg)

### Model-View-ViewModel

Avant de regarder le code, nous devrions avoir une compréhension de base de MVVM. Si vous êtes familier avec MVVM, vous pouvez sauter cette partie.

L'objectif principal derrière MVVM est de déplacer autant que possible l'état et la logique de la Vue vers une entité séparée. Le nom donné à cette entité est le ViewModel. Le ViewModel contient également la logique métier. Il sert de médiateur entre la Vue et le Modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A87nt_oqnajSSejzJHGY5w.png)
_MVVM : Model-View-ViewModel_

Le ViewModel a essentiellement deux responsabilités :

* il réagit aux entrées utilisateur (par exemple en changeant le modèle, en initiant des requêtes réseau, ou en routant vers différents écrans)
* il offre des données de sortie auxquelles la Vue peut s'abonner

La Vue ne contient aucune logique métier. Voici les responsabilités de la vue :

* elle réagit aux nouveaux états de sortie du ViewModel et les rend en conséquence (par exemple en affichant une chaîne dans un champ de texte)
* elle informe le ViewModel des nouvelles entrées utilisateur (par exemple, clics sur des boutons, changements de texte, touches d'écran)

Contrairement aux approches MVC populaires, le Fragment / Activity / UIViewController ou Widget ne contient pas de logique métier dans MVVM. C'est une vue humble qui rend les états de sortie du ViewModel. Le ViewModel ne **connaît pas** la Vue (une différence avec les formes de MVP et MVC). Il offre des états de sortie que la Vue observe :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vO41CcfdKftvklRsFt4sWQ.png)
_Interface d'entrée-sortie d'un ViewModel_

### MVVM dans Flutter

Dans Flutter, le Widget représente la Vue de MVVM. La logique métier réside dans une classe ViewModel séparée. Le ViewModel est totalement indépendant de la plateforme. Il ne contient aucune dépendance à Flutter et peut être facilement réutilisé, par exemple dans un projet web.

C'est l'un des plus grands atouts de MVVM. Nous pouvons créer une application mobile et un site web qui partagent tous deux le même ViewModel. Vous n'avez pas besoin de réinventer et d'écrire la logique deux fois.

#### Exemple : Widget d'abonnement par email

Regardons un exemple. Nous allons implémenter un formulaire d'inscription à une newsletter avec un champ de texte pour l'email et un bouton de soumission. Le bouton est désactivé et l'utilisateur voit une erreur si l'email est invalide :

![Image](https://cdn-media-1.freecodecamp.org/images/0*_90H8ZlAkMucYABz.gif)

#### La mauvaise façon

Sans aucune architecture spécifique, la logique métier et l'état actuel font partie du widget. Cela pourrait ressembler à ceci :

Le problème est que la logique de vue, l'état de la vue et la logique métier sont mélangés. Cela conduit à quelques problèmes :

1. Il est difficile de faire des tests unitaires
2. D'autres projets Dart ne peuvent pas réutiliser la logique métier, puisqu'elle est imbriquée avec la logique de vue dépendante de Flutter
3. Ce style devient rapidement désordonné et vous vous retrouvez avec d'énormes classes de Widget

Voyons comment nous pouvons améliorer cela...

#### Solution avec MVVM

Comme expliqué ci-dessus, le ViewModel a des paramètres d'entrée et de sortie. Nous ajouterons un préfixe 'input' ou 'output' pour plus de clarté.

Toutes les entrées sont des `Sinks`. La Vue peut les utiliser pour insérer des données dans le ViewModel. Toutes les sorties sont des `Streams`. La Vue peut écouter les changements en s'abonnant aux `Streams`. L'interface pour notre ViewModel ressemble à ceci :

Nous utilisons un `StreamController` comme `Sink` d'entrée. Ce `StreamController` fournit un stream que nous pouvons utiliser en interne pour gérer ces événements d'entrée.

### Liaison d'une Vue au ViewModel

Alors, comment fournissons-nous des entrées et gérons-nous les événements de sortie ? Pour fournir des valeurs d'entrée au ViewModel, nous les insérons dans les `Sinks` du ViewModel. Nous allons lier un Widget au ViewModel. Dans ce cas, nous insérons le texte du TextField chaque fois qu'il change.

Vous écoutez les sorties du ViewModel en vous abonnant aux **Streams** de sortie.

Flutter fournit un Widget vraiment cool appelé `StreamBuilder` qui se mettra à jour chaque fois qu'un **Stream** fournira une nouvelle valeur. Nous n'appellerons plus jamais `setState` !
La méthode `builder` du **StreamBuilder** vous donne un snapshot chaque fois qu'il se construit. Ce snapshot contient des informations sur le stream, ses données et ses erreurs. Si notre stream n'a émis aucune valeur, `snapshot.data` sera null. Donc, soyez prudent.

ASTUCE RAPIDE : Essayez d'aider le compilateur Dart lorsque vous travaillez avec des streams. Ajoutez tous les types génériques nécessaires pour éviter les erreurs d'exécution.

Ici, vous pouvez voir le tableau complet :

Comme vous pouvez le voir, la seule responsabilité de la Vue est de rendre les sorties et de fournir des entrées au ViewModel. Notre Widget est donc super mince et facile à lire.

### Conclusion

Nous avons commencé avec MVVM dans le monde natif et nous nous sommes demandé si cela fonctionnerait également avec Flutter. Après l'avoir essayé, nous pouvons dire : MVVM est également un excellent choix pour Flutter.

Nous aimons la façon dont la logique de vue est bien séparée de la logique métier. Nous aimons la facilité avec laquelle les ViewModels peuvent être testés unitaires. Et nous aimons la façon dont les ViewModels Dart peuvent être partagés avec d'autres plateformes utilisant Dart.

L'API Stream prend un certain temps pour s'y habituer, mais ensuite, cela devient très fluide. Pour des tâches plus compliquées, nous avons utilisé RxDart. Cela ajoute des fonctionnalités à l'API Stream standard.

Si vous bricolez simplement une petite application, alors l'approche normale "mettre-tout-dans-une-classe" peut être plus simple. Si vous prévoyez de construire une application plus grande, cependant, MVVM pourrait être l'architecture qu'il vous faut.

_Publié à l'origine sur [quickbirdstudios.com](https://quickbirdstudios.com/blog/mvvm-in-flutter/) le 12 juin 2018._