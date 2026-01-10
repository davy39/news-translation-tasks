---
title: Pourquoi vous devriez utiliser Flutter pour vos projets
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2022-07-12T20:12:35.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-use-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-pixabay-326055.jpg
tags:
- name: Flutter
  slug: flutter
seo_title: Pourquoi vous devriez utiliser Flutter pour vos projets
seo_desc: "Flutter is a UI toolkit and SDK which you can use to build applications.\
  \ Flutter is open source and you can use it to build highly performant mobile and\
  \ desktop apps. \nIn this article, I'll explain in detail the various benefits of\
  \ using Flutter so y..."
---

Flutter est un kit d'interface utilisateur (UI) et un SDK que vous pouvez utiliser pour construire des applications. Flutter est open source et vous pouvez l'utiliser pour construire des applications mobiles et de bureau hautement performantes. 

Dans cet article, je vais expliquer en détail les divers avantages de l'utilisation de Flutter afin que vous puissiez décider de l'utiliser pour votre prochain projet.

## Principaux avantages de Flutter

1. [Flutter est multiplateforme](#heading-flutter-est-multiplateforme)
2. [Comment Flutter est multiplateforme](#heading-flutter-est-multiplateforme)
3. [Flutter dispose d'un moteur d'interface utilisateur puissant](#heading-flutter-dispose-dun-moteur-dinterface-utilisateur-puissant) 
4. [Comment Flutter rend les interfaces utilisateur](#heading-comment-flutter-rend-les-interfaces-utilisateur)
5. [Flutter offre une excellente gestion d'état](#heading-flutter-offre-une-excellente-gestion-detat) 
6. [Flutter offre une excellente expérience développeur](#heading-flutter-offre-une-excellente-experience-developpeur) 
7. [Flutter dispose d'une communauté de développeurs formidable](#heading-flutter-dispose-dune-communaute-de-developpeurs-formidable)
8. [Résumé](#heading-resume)

Examinons maintenant chacun de ces aspects plus en détail.

## Flutter est multiplateforme 

Un logiciel est multiplateforme lorsqu'il est disponible pour différents systèmes d'exploitation. Vous souhaitez que votre produit ait cette capacité multiplateforme afin que les utilisateurs sur n'importe quel appareil puissent utiliser votre produit confortablement.

Avoir un support pour les plateformes de bureau, mobiles et web est difficile. Pour le bureau, vous devrez écrire du code pour macOS (avec Swift), Linux (avec C) et Windows (avec C++). Pour les mobiles, vous devrez écrire du code pour Android (avec Kotlin/Java et XML) et iOS (avec Swift).

Pour rendre votre produit accessible en tant que site web, vous devez utiliser HTML, CSS et JavaScript. Ou utiliser n'importe quel framework JavaScript frontal comme Angular, React ou Vue.

La création d'applications pour les différents systèmes d'exploitation de bureau et mobiles nécessite des SDK et des compétences distincts. Par le passé, vous auriez dû embaucher des développeurs compétents sur chaque plateforme pour implémenter votre application sur chacune de ces plateformes. Cela est coûteux. 

Pour ajouter une fonctionnalité, vous auriez dû mettre à jour le code sur toutes ces plateformes, ce qui est fastidieux.

### Comment Flutter est multiplateforme

Le code Flutter peut s'exécuter sur les plateformes de bureau, mobiles et web. Ainsi, vous n'avez pas besoin d'embaucher des développeurs pour chaque plateforme. Vous devez écrire le code une seule fois dans Flutter et vous pouvez être assuré que l'application fonctionnera sur les autres plateformes. Donc, Flutter est économique.

L'ajout de fonctionnalités à votre application est rapide car vous n'avez qu'à faire les mises à jour du code une seule fois dans Flutter et c'est tout.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/demo.gif)
_La même application Flutter fonctionnant sur bureau, mobile et web._

Le framework Flutter vous fournit des API pour le rendu et les événements (via les widgets). Il fournit également des API pour les services spécifiques à la plateforme (via les canaux de méthode). Ainsi, Flutter _expose_ _tout_ ce dont vous avez besoin pour construire l'application de la manière que vous souhaitez. C'est ainsi que fonctionne le multiplateforme.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--224--2.png)
_Adapté de https://youtu.be/l-YO9CmaSUM_

Ne vous inquiétez pas pour les performances. Naturellement, Dart peut compiler en code natif. Ainsi, les performances des applications Flutter sont proches (sinon égales) à celles des applications natives. 

Le [compilateur Ahead-Of-Time de Dart](https://dart.dev/tools/dart-compile) est utilisé pour bundler le code Flutter. Il est utilisé lorsque vous lancez la commande `flutter build`. Pendant l'étape de build, seul l'application et le moteur Flutter sont livrés. Cela rend l'application construite petite en taille (très proche d'une application native). 

## Flutter dispose d'un moteur d'interface utilisateur puissant

Le rendu de l'interface utilisateur dans Flutter est pixel-perfect. En tant que développeur Flutter, vous êtes responsable de chaque pixel peint sur l'écran de l'appareil. 

Flutter réalise cela grâce à son moteur. Le moteur Flutter est responsable de l'interprétation du code Flutter en ce qui est exactement dessiné sur l'écran de l'appareil. Chaque application Flutter (construite pour une plateforme donnée) contient le moteur qui gère le rendu à l'exécution.

Cela explique également comment Flutter est efficacement multiplateforme, en termes de rendu d'interface utilisateur. Mais cela concerne davantage l'efficacité du moteur. Le moteur Flutter utilise [Skia](https://skia.org/) pour les graphiques. Skia est une bibliothèque graphique 2D qui gère la rasterisation des graphiques sur divers matériels et logiciels.

Le moteur Flutter ne contient pas seulement Skia. Il comprend également des implémentations des API principales de Flutter (comme les textes et les E/S réseau) à des niveaux de base.

Le moteur Flutter est si puissant qu'il peut re-rendre efficacement les interfaces utilisateur à une vitesse de **60 images par seconde** (60 fps). Ainsi, lorsque des changements d'interface utilisateur ou des animations se produisent, le moteur les rend si rapidement que cela semble être une application native.

### Comment Flutter rend les interfaces utilisateur

Flutter utilise la composition de manière agressive. La composition ici signifie que les widgets contiennent des widgets, qui à leur tour contiennent des widgets, et ainsi de suite. Tout dans Flutter est un widget et le code d'interface utilisateur de Flutter est essentiellement un grand arbre de widgets. 

En coulisses, Flutter maintient **3 arbres séparés** pour l'interface utilisateur. Nous codons normalement l'arbre de widgets le plus externe. À son tour, le moteur Flutter crée un arbre _Element_ et un arbre _RenderObject_ basé sur l'arbre de widgets.

En essence, chaque widget a son propre Element et RenderObject correspondants. Ces deux dernières entités sont responsables de la représentation réelle des widgets sur l'écran de l'appareil. Les widgets eux-mêmes contiennent simplement les propriétés de l'interface utilisateur (comme la couleur, le remplissage, les ombres, etc.) que nous définissons nous-mêmes.

Lorsque l'interface utilisateur est re-rendue, Flutter détruit et reconstruit toujours tout widget modifié (car les widgets sont immuables). Cependant, il ne remplace un Element ou un RenderObject lié _que si nécessaire._

Ces arbres d'interface utilisateur supplémentaires expliquent comment l'arbre de widgets est détruit et reconstruit dans chaque frame de la vitesse de rendu de 60 fps et pourtant l'interface utilisateur est re-rendue correctement. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/widget_tree_1.png)
_Les 3 arbres d'interface utilisateur, adapté de https://youtu.be/996ZgFRENMs_

![Image](https://www.freecodecamp.org/news/content/images/2022/07/widget_tree_2.png)
_Les 3 arbres d'interface utilisateur avec le widget Center comme exemple. Adapté de https://youtu.be/996ZgFRENMs_

## Flutter offre une excellente gestion d'état

L'état fait référence aux données dont votre application a besoin pour rendre son interface utilisateur à tout moment. Il peut être généré par l'utilisateur ou provenir de vos serveurs ou backend. 

En général, Flutter dispose de deux types de widgets : StatelessWidgets et StatefulWidgets. Chaque fois que vous devrez mettre à jour l'interface utilisateur en fonction de l'état, utilisez simplement un StatefulWidget à l'avance. Ensuite, pour mettre à jour l'interface utilisateur, appelez `setState()` n'importe où à l'intérieur de la classe State d'un StatefulWidget et Flutter reconstruira l'arbre de l'interface utilisateur.

Ce mécanisme `setState()` s'avère être le plus efficace qui soit. C'est aussi le style React de mise à jour de l'interface utilisateur en fonction de l'état. La programmation d'interface utilisateur devrait être déclarative et `setState()` préconise simplement cela.

Vous devriez appeler `setState()` après que le code asynchrone a été exécuté (le cas échéant). Cela est dû au fait qu'il fait partie du thread principal de l'interface utilisateur et que les appels bloquants peuvent détourner le processus de rendu de l'interface utilisateur.

Si vous avez des processus très intensifs en CPU dans une application Flutter, envisagez d'utiliser [Dart Isolates](https://dart.dev/guides/language/concurrency#how-isolates-work) pour effectuer ces processus, puis appelez `setState()` avec les données que vous obtenez lorsque le traitement est terminé.

Parfois, vous pourriez avoir besoin d'accéder à un état non limité à un widget particulier. À ce moment-là, vous avez besoin d'une architecture de gestion d'état. Il en existe un bon nombre parmi lesquels choisir. Ces architectures fournissent un état au niveau de l'application entière sans reconfiguration dans chaque widget.

Les [options disponibles](https://docs.flutter.dev/development/data-and-backend/state-mgmt/options) incluent Provider, Riverpod, Redux, InheritedWidget, [Stacked](https://filledstacks.com/), et bien d'autres.

Un autre avantage de ces architectures est qu'un bon nombre d'entre elles permettent une bonne [séparation des préoccupations](https://en.m.wikipedia.org/wiki/Separation_of_concerns) et [injection de dépendances (ou inversion de contrôle)](https://en.m.wikipedia.org/wiki/Dependency_injection).

En termes plus simples, la séparation des préoccupations vous donne la capacité d'écrire du code spécifique à l'interface utilisateur séparé du code spécifique à la logique. Ainsi, si vous souhaitez déboguer ou changer les packages ou les API que vous utilisez, vous pourrez le faire facilement à partir d'un seul endroit (sans craindre d'endommager la base de code). De plus, cela favorise également un code propre.

L'injection de dépendances implique l'utilisation de services ou quelque chose de similaire pour obtenir ce dont les widgets ont besoin pour fonctionner sans que les widgets configurent eux-mêmes les services. Certaines architectures comme Stacked vous permettent de gérer les états de l'application entière sans le BuildContext. 

Ce modèle est utile car, dans les StatelessWidgets, le BuildContext est disponible uniquement dans la méthode build et vous pourriez avoir besoin d'utiliser des éléments en dehors de celle-ci. Ainsi, vous pourriez faire d'autres choses comme BottomSheet, Navigation, Toast, et ainsi de suite sans BuildContext.

## Flutter offre une excellente expérience développeur

Il y a de nombreuses raisons pour lesquelles l'expérience développeur avec Flutter est formidable. En voici quelques-unes :

### Flutter n'a qu'un seul langage de programmation – Dart.

La programmation en elle-même est une activité exigeante. Les frameworks, les bibliothèques et les outils ne devraient pas rendre le codage plus difficile. 

Lors du codage pour certaines plateformes, vous écrivez généralement du code dans plus d'un langage de programmation. Par exemple, lors du codage pour le web frontal, vous alternerez entre les fichiers HTML, CSS et JavaScript pour gérer une partie donnée de votre page web.

Flutter facilite le codage car vous écrivez dans un seul langage de programmation : Dart. Ainsi, la plupart du temps, la logique et les propriétés de l'interface utilisateur pour une partie donnée de votre application Flutter seront dans le même fichier Dart. 

De plus, Flutter et Dart sont écrits en anglais simple. Les noms des widgets et leurs propriétés reflètent ce qu'ils sont. Lors du codage Flutter, vous êtes moins susceptible d'avoir des maux de tête pour comprendre un widget donné et/ou ses cas d'utilisation.

### Flutter dispose du rechargement à chaud.

Dart est un langage de programmation moderne qui est livré avec [un compilateur Ahead-Of-Time (AOT) et un compilateur Just-In-Time (JIT).](https://dart.dev/tools/dart-compile) 

Le compilateur JIT donne l'impression que Dart est plutôt interprété à l'exécution. En d'autres termes, il permet aux modifications des fichiers Dart de se refléter immédiatement sans avoir besoin de recompiler le fichier, comme c'est le cas avec certains langages de programmation comme C ou Java. 

Flutter exploite le JIT pour le développement. Flutter livre une [machine virtuelle Dart](https://mrale.ph/dartvm) à la plateforme dans laquelle le code de l'application est hébergé. Ainsi, lorsque vous lancez la commande `flutter run`, appuyer sur `r` dans ce terminal intègre les modifications dans les fichiers dart, sans recompiler toute l'application. Cette fonctionnalité de réflexion des changements instantanée, pourtant _multiplateforme_ de Flutter est appelée **rechargement à chaud**.

Flutter dispose également du **redémarrage à chaud**. Le redémarrage à chaud est réalisé en appuyant sur `R` (majuscule au lieu de minuscule cette fois). Le _redémarrage à chaud_ redémarre entièrement l'application.

Vous devez effectuer un redémarrage à chaud si vous modifiez certaines parties importantes du code Flutter. Par exemple, la modification des déclarations de `class` ou de leurs superclasses nécessitera un redémarrage à chaud.

### Flutter est universel.

Flutter est disponible pour chaque système d'exploitation. Ainsi, vous n'aurez pas besoin de migrer ou d'utiliser un système d'exploitation particulier pour créer des applications avec Flutter comme c'est le cas avec les applications iOS (où vous avez besoin d'un ordinateur Apple).  

Flutter s'intègre parfaitement avec les IDE populaires. Android Studio, IntelliJ et VS Code (Visual Studio Code) disposent de plugins ou d'extensions pour Flutter. Ainsi, vous pouvez manipuler les commandes Flutter directement dans l'IDE sans utiliser le terminal. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/demo2.gif)
_Édition de Flutter en tant qu'application Android dans Android Studio_

![Image](https://www.freecodecamp.org/news/content/images/2022/06/demo3.gif)
_Édition de Flutter en tant qu'application Windows dans VS Code_

Android Studio est relativement exigeant en termes de ressources informatiques. Si votre ordinateur portable [n'a pas au moins 8 Go de RAM](https://developer.android.com/studio#system-requirements-a-namerequirementsa), ne vous sentez pas exclu. 

La configuration de Flutter détecte automatiquement votre système d'exploitation et vos navigateurs. Flutter est disponible pour le web (pour exécuter des applications Flutter dans les navigateurs). Ainsi, vous pouvez tester le code Flutter dans votre navigateur ou en tant qu'application de bureau si la capacité de la RAM ou du CPU pourrait poser problème. 

Il existe également [dartpad.dev](https://dartpad.dev), [flutlab.io](https://flutlab.io) et [flutterflow.io](https://flutterflow.io) qui vous permettent de créer des applications Flutter en ligne, dans le navigateur. Vous trouverez ces outils utiles car ils ne nécessitent pas autant de ressources informatiques que l'exécution de Flutter pour Android ou iOS. 

### Flutter DevTools 

Dart est naturellement livré avec un ensemble d'utilitaires pour optimiser et déboguer le code Dart. Cette suite d'outils est accessible depuis le navigateur ou l'IDE que vous utilisez. Lors du codage Flutter, l'utilisation de DevTools raccourcira votre temps de codage et vous donnera des informations approfondies sur votre application. 

[Flutter DevTools](https://docs.flutter.dev/development/tools/devtools/overview) inclut des outils indispensables comme un inspecteur, un débogueur, un moniteur de performance, un moniteur réseau, un logger, et plus encore.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--234-.png)
_Flutter DevTools_

## Flutter dispose d'une communauté de développeurs formidable 

> Le framework Flutter est relativement petit... – [d'après la documentation Flutter](https://docs.flutter.dev/resources/architectural-overview) 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/flutter_is_smalll.png)

L'équipe Flutter elle-même reconnaît la communauté. En soi, le framework Flutter est relativement petit par rapport à l'ensemble de l'écosystème Flutter. Flutter est Open Source. 

Autour de Flutter, il y a tant de développeurs qui ont étendu le framework. Ces développeurs ont publié plus de 24 000 packages sur [pub.dev](https://pub.dev). Chaque package contient au moins un widget que vous pouvez importer dans votre application Flutter. 

Si vous rencontrez des problèmes avec Flutter ou si vous tombez sur des erreurs en utilisant Flutter, vous trouverez une solution une fois que vous aurez recherché en ligne. Il y a des chances que des [problèmes GitHub](https://github.com/flutter/flutter/issues) ou des [questions Stackoverflow](https://stackoverflow.com/questions/tagged/flutter) existent sur ce que vous cherchez. Stackoverflow compte de nombreux développeurs Flutter prêts à vous aider, alors n'hésitez pas à poser des questions avec le tag Flutter. 

Les [Flutter Groups](https://flutter.dev/community) et les [GDG](https://developers.google.com/community/gdg) sont des communautés techniques, présentes dans divers pays. Chaque année, ces communautés organisent un événement dédié à Flutter communément appelé [FlutterFest](https://www.flutterfestival.com/). Certains événements FlutterFest sont en personne tandis que d'autres sont virtuels. Ces événements rassemblent les membres de la communauté pour Flutter, Flutter et encore Flutter.

Cela dit, vous devriez utiliser Flutter parce que vous n'êtes pas seul. Vous êtes confiant qu'il y a des personnes autour de vous qui l'utilisent également et peuvent vous aider lorsque vous en avez besoin. 

De plus, la maintenance et le support futur pour Flutter semblent prometteurs. [Fuchsia](https://fuchsia.dev) est un système d'exploitation open source à venir. En plus du support multiplateforme actuel, Flutter pour Fuchsia est disponible.

## Résumé

En résumé, utilisez Flutter en raison des nombreux avantages que vous en tirerez. 

Vous aurez une application multiplateforme dont l'interface utilisateur est pixel perfect et l'état correctement géré. Vous profiterez également de votre expérience de développement et tirerez parti de la communauté Flutter.  

À vos nombreuses applications Flutter que vous allez construire.

## Ressources utiles 

* [Comment Flutter est différent pour le développement d'applications](https://youtu.be/l-YO9CmaSUM)
* [Comment Flutter rend les widgets](https://youtu.be/996ZgFRENMs) 
* [Aperçu architectural de Flutter](https://docs.flutter.dev/resources/architectural-overview) 
* [Liste des approches de gestion d'état](https://docs.flutter.dev/development/data-and-backend/state-mgmt/options) 
* [Comment implémenter n'importe quelle interface utilisateur dans Flutter](https://www.freecodecamp.org/news/how-to-implement-any-ui-in-flutter)