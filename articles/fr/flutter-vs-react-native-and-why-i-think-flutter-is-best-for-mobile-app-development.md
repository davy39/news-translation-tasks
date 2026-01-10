---
title: Flutter VS React Native – Et pourquoi je pense que Flutter est le meilleur
  pour le développement d'applications mobiles
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-01-18T22:26:00.000Z'
originalURL: https://freecodecamp.org/news/flutter-vs-react-native-and-why-i-think-flutter-is-best-for-mobile-app-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca64b740569d1a4ca6f40.jpg
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: Flutter VS React Native – Et pourquoi je pense que Flutter est le meilleur
  pour le développement d'applications mobiles
seo_desc: "This isn’t the type of article you might think it’s going to be. I’m not\
  \ going to list the pros and cons of every framework and I am not going to do a\
  \ comparative analysis of performance. \nOver the past few weeks, I have dipped\
  \ my coding hand in tryi..."
---

Ce n'est pas le type d'article que vous pourriez penser qu'il va être. Je ne vais pas lister les avantages et les inconvénients de chaque framework et je ne vais pas faire une analyse comparative des performances. 

Au cours des dernières semaines, j'ai essayé de créer des applications simples et fonctionnelles en utilisant les deux frameworks. Le titre de cet article est la conclusion à laquelle je suis parvenu suite à mes expérimentations.

_⚠️ Avertissement : Je ne prétends en aucun cas que le framework A est meilleur que le framework B et je n'ai pas été payé par l'un ou l'autre pour donner mon opinion. Il s'agit uniquement d'un article basé sur mon expérience personnelle et rien de plus._

## Un peu de contexte

Bien que je ne sois pas familier avec [Dart](https://www.dartlang.org/) ou [React](https://reactjs.org/), j'ai quelques connaissances en JavaScript et plus que ma part de développement natif. Comme ces deux frameworks sont relativement nouveaux et offrent le même type d'expérience de développement, j'ai pensé les essayer pour voir de quoi il en retourne. Je ne suis pas profondément compétent dans toute la logique des deux et je n'ai pas encore pleinement compris le composant d'état dans React ou la hiérarchie des composants dans Dart. Cela dit, je me suis lancé dans la création d'une application de base sur les deux plateformes. Le principe de l'application ? Une application qui accepte l'entrée de l'utilisateur et, au toucher d'un bouton, affiche l'entrée de l'utilisateur dans une sorte de liste que l'utilisateur peut faire défiler à l'écran.

---

# Ma Réaction

J'ai d'abord commencé à travailler sur l'application en utilisant **_React Native_**. La configuration du projet était _très_ simple. Il suffisait de suivre les instructions dans la [documentation Getting Started](https://facebook.github.io/react-native/docs/getting-started.html). J'ai installé **_Expo_** et en quelques minutes, mon application était chargée sur mon téléphone. J'ai vraiment apprécié la rapidité avec laquelle le scanner de code QR de l'application Expo identifie le code à l'écran. L'interface d'Expo sur l'ordinateur était également très intuitive. Vous pouvez voir l'état de l'application (en construction ou en échec), démarrer un émulateur Android/iOS et plus encore. Il était maintenant temps de mettre ma propre logique dans l'application. C'est là que les choses sont devenues frustrantes.

Remplacer l'élément View par une entrée de texte était facile, et il en était de même pour ajouter un bouton avec une action onClick. Mais essayer d'avoir un ensemble de données pour sauvegarder l'entrée de l'utilisateur était tout simplement déconcertant. J'ai créé une variable qui était un tableau dans l'objet state et j'ai essayé diverses façons de la mettre à jour lorsque l'utilisateur avait fini de saisir sa propre entrée. J'ai cherché haut et bas et j'ai implémenté diverses solutions pour permettre à mon application de sauvegarder des données dans le tableau, mais sans succès. La documentation que j'ai trouvée était rare et n'était pas vraiment utile. Sans parler de la pléthore d'erreurs de compilation que j'avais, qui n'étaient pas très instructives sur ce qui n'allait pas dans mon code. Après un certain temps, cela est devenu assez ennuyeux de voir cet écran rouge à plusieurs reprises.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_QwBpjtvPlj0B8YZ6Mc1VIA.png)
_Pourquoi React ? Pourquoi ?_

# S'envoler avec Flutter

Étant frustré et honteux de ne pas pouvoir créer la plus simple des applications en utilisant React, et suite à l'annonce de Flutter, j'ai pensé essayer de construire la même application. **_Vous savez ce qu'on dit, changement de place - changement de chance._**

La configuration était un jeu d'enfant et offrait la même expérience rapide que React et j'étais prêt à commencer à développer en un rien de temps. Télécharger le SDK Flutter et installer le plugin faisaient partie de quelques étapes simples pour commencer à développer dans Flutter.

Ensuite est venue la tâche de regarder le code. Comment puis-je le mettre en mots ? Pas ce à quoi je m'attendais. Vous avez différents composants dans une hiérarchie longue et sinueuse, qui peut parfois être difficile à suivre. À part cela, vous avez des widgets et des colonnes et des lignes et vous devez comprendre où tout s'emboîte. Maintenant, vous pensez que je suis censé vous dire pourquoi j'aime Flutter. Comme la plupart des choses, elles ont leurs forces et leurs faiblesses. Et après avoir passé en revue les choses que je trouve irritantes, je peux savourer ce que j'ai trouvé attachant.

Pour commencer, Flutter est fortement [documenté](https://flutter.io/docs). Chaque fois que je devais chercher quelque chose, je pouvais facilement le trouver dans la documentation. De plus, il existe de nombreux exemples concrets de diverses applications, de sorte que vous êtes sûr d'en trouver une similaire à ce que vous essayez de faire.

Après avoir bidouillé avec le code de démarrage, vous commencez à comprendre la hiérarchie et comment les vues sont affichées, de sorte que vous en venez à comprendre les intricacités étranges de tout cela. C'était aussi un plaisir de réaliser que faire en sorte qu'un composant se comporte d'une certaine manière était aussi simple que d'ajouter une autre caractéristique au widget.

Et surtout, **_j'étais déjà dans un environnement natif_**. J'étais à l'aise avec Android Studio, comprenant où tout va et profitant des luxes et des avantages d'un environnement familier.

Comparé au temps que j'ai passé à **_essayer_** de développer mon application dans React, le temps que j'ai passé dans Flutter était une fraction de cela. De plus, même si ce que vous essayez de faire ne fonctionne pas toujours, vous avez le sentiment de progrès éventuel et vous êtes encouragé à examiner les choses plus en détail dans la documentation.

En colère ?? Bouleversé ?? Exalté ?? Jubilant ? ? Faites-moi savoir ce que vous en pensez.