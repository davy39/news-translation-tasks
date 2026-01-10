---
title: Comment Flutter est-il indépendant de la plateforme ?
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2024-05-07T07:21:09.000Z'
originalURL: https://freecodecamp.org/news/how-is-flutter-platform-agnostic
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-02-225922.png
tags:
- name: Flutter
  slug: flutter
seo_title: Comment Flutter est-il indépendant de la plateforme ?
seo_desc: "Flutter builds applications for multiple platforms (desktop, mobile, and\
  \ web) from the same codebase. Flutter does this in a pixel-perfect and platform-agnostic\
  \ manner. \nIn this article, we will explore how Flutter is platform-agnostic through\
  \ how it..."
---

Flutter construit des applications pour plusieurs plateformes (bureau, mobile et web) à partir de la même base de code. Flutter le fait de manière pixel-perfect et indépendante de la plateforme.

Dans cet article, nous allons explorer comment Flutter est indépendant de la plateforme à travers la manière dont il rend les interfaces utilisateur et à travers les canaux de plateforme.

## Table des matières

* [Qu'est-ce que l'indépendance de la plateforme ?](#heading-quest-ce-que-lindependance-de-la-plateforme)
* [Comment les applications natives et autres applications multiplateformes fonctionnent](#heading-comment-les-applications-natives-et-autres-applications-multiplateformes-fonctionnent)
* [Comment les applications Flutter sont différentes de leurs applications hôtes](#heading-comment-les-applications-flutter-sont-differentes-de-leurs-applications-hotes)
* [Comment Flutter rend les interfaces utilisateur (UI) ?](#heading-comment-flutter-rend-les-interfaces-utilisateur-ui)
* [Comment fonctionnent les canaux de plateforme dans Flutter ?](#heading-comment-fonctionnent-les-canaux-de-plateforme-dans-flutter)
  - [Canaux de méthode](#heading-canaux-de-methode)
  - [Canaux d'événements](#heading-canaux-devenements)
  - [Paquets et plugins](#heading-paquets-et-plugins)
* [Résumé](#heading-resume)

## Qu'est-ce que l'indépendance de la plateforme ?

L'indépendance de la plateforme est une mesure relative de la manière dont une application fonctionne de la même manière, indépendamment du système d'exploitation sur lequel l'application est exécutée.

Lorsque nous disons qu'une application ou un outil est indépendant de la plateforme, les utilisateurs s'attendent à la même expérience sur cette application donnée à travers leurs différents appareils.

Être indépendant de la plateforme, c'est être indifférent à l'appareil ou au système d'exploitation. Les utilisateurs ne connaissent pas les obstacles techniques derrière l'architecture d'une application. Ils veulent profiter de votre application. C'est pourquoi vous devriez leur offrir la même expérience sur diverses plateformes.

Les applications Flutter fonctionnent de manière indépendante de la plateforme. Les applications Flutter fonctionnent de la même manière sur différentes plateformes. Cela offre aux utilisateurs (et aux développeurs) une expérience transparente.

Cet article explore comment Flutter fait cela. Mais avant de plonger dans le sujet, regardons comment les outils natifs et autres multiplateformes gèrent leurs applications.

## Comment les applications natives et autres applications multiplateformes fonctionnent

Les systèmes d'exploitation ou les plateformes (Android, iOS, Linux, macOS, Windows, etc.) spécifient comment construire des applications sur eux. Ils fournissent aux développeurs les API nécessaires pour que les applications fonctionnent.

Lorsque les applications s'exécutent, elles communiquent constamment avec le système d'exploitation sous-jacent. Ces applications natives affichent des boutons, des icônes, du texte et d'autres éléments d'interface utilisateur sous forme de widgets fournis par la plateforme ou l'OEM. Elles ont également accès aux services de l'appareil comme l'audio, le Bluetooth, la caméra, etc.

Pour construire une application pour un système d'exploitation spécifique, vous utilisez normalement le ou les langages de programmation et les SDK spécifiés par cette plateforme.

![Comment les applications natives fonctionnent](https://www.freecodecamp.org/news/content/images/2024/05/native_apps.png)
_Comment les applications natives fonctionnent_

Initialement, si vous vouliez que votre application soit disponible sur plusieurs plateformes, vous deviez construire la même application pour chaque plateforme mais avec des SDK séparés comme chaque plateforme l'exige. Cela implique également des bases de code séparées, différents développeurs et plus de temps de codage.

Aujourd'hui, nous utilisons principalement des outils multiplateformes pour construire des applications. Ils utilisent la même base de code pour construire des applications sur plusieurs systèmes d'exploitation. Ils résolvent le problème de la compétence de plusieurs développeurs et du long temps de développement en utilisant la même base de code.

Les frameworks d'applications multiplateformes ont également leurs règles et langages. Néanmoins, en coulisses, ils compilent toujours le code que vous avez écrit en ce dont chaque plateforme a besoin. Des exemples de tels outils multiplateformes incluent Flutter, React Native, Xamarin, etc.

Chaque framework a ses mécanismes sous-jacents pour compiler sur plusieurs systèmes d'exploitation. D'autres frameworks (en dehors de Flutter) sont généralement étroitement couplés à la plateforme cible. Ils utilisent des ponts pour accéder aux services de la plateforme. Le pont rend également l'UI de l'application en utilisant les composants UI spécifiques de la plateforme cible. De plus, certaines applications multiplateformes utilisent parfois webview pour rendre les UI.

![Comment les applications multiplateformes fonctionnent](https://www.freecodecamp.org/news/content/images/2024/05/other_cross_platform_apps.png)
_Comment les applications multiplateformes fonctionnent_

Ce qui précède n'est pas la manière dont Flutter fonctionne. Flutter utilise une approche différente et innovante pour construire des applications multiplateformes. Il le fait en s'assurant que l'application est la même indépendamment de la plateforme hôte.

Flutter est indépendant de la plateforme. Les applications Flutter sont techniquement séparées de leur application hôte.

## Comment les applications Flutter sont différentes de leurs applications hôtes

Lorsque Flutter construit une application pour une plateforme cible, il intègre une _application Flutter interne_ et le moteur Flutter dans l'application construite. Par exemple, lorsque nous construisons une base de code Flutter pour Android, nous obtiendrons un APK (un "installable" Android). Dans cet APK construit par Flutter se trouveront le moteur Flutter et l'application Flutter.

Avec cela, l'application Flutter interne fonctionne de manière similaire sur chaque plateforme. Lorsque l'utilisateur lance l'application "hôte" sur son appareil, le moteur Flutter démarre et, à son tour, lance l'application Flutter interne. Étant donné que le moteur exécute Flutter, il exécutera toujours la même chose sur n'importe quelle plateforme.

L'avantage de séparer les applications Flutter de leurs applications hôtes est l'indépendance de la plateforme. En d'autres termes, avoir la même application et la même expérience utilisateur sur toutes les plateformes.

Si la plateforme devait exécuter directement le contenu de l'application ou s'il s'agissait d'un pont multiplateforme, nous aurions des différences et des divergences dans la manière dont l'application s'exécute sur divers systèmes d'exploitation. Cela est dû au fait que chaque système d'exploitation a sa propre manière unique d'exécuter les applications.

Parce que les applications Flutter s'exécutent indépendamment de leurs applications hôtes, le framework Flutter élève le rendu de l'UI et l'accès aux services dans l'application Flutter (via le moteur Flutter). De cette manière, l'application Flutter est plus en charge et a un meilleur contrôle sur la manière dont l'application se comporte.

Pour le rendu des UI, l'application Flutter dessine des widgets Flutter sur un "canvas" dans l'application hôte. Pour accéder aux services, l'application Flutter utilise des canaux de plateforme pour interagir avec l'application hôte lorsque cela est nécessaire.

![Comment les applications Flutter fonctionnent](https://www.freecodecamp.org/news/content/images/2024/05/flutter_apps.png)
_Comment les applications Flutter fonctionnent_

## Comment Flutter rend les interfaces utilisateur (UI) ?

Au cœur du rendu des UI indépendantes de la plateforme de Flutter se trouve un pipeline, orchestré par plusieurs couches d'UI. Ces couches incluent l'embedder, le moteur Flutter (avec Skia ou Impeller), et l'UI de votre application Flutter.

L'embedder sert de pont entre le moteur Flutter et la plateforme hôte. Il fournit une interface binaire d'application (ABI) agnostique pour le moteur Flutter. Il est écrit dans le langage de programmation natif de la plateforme hôte. Il est déployé par plateforme. En d'autres termes, chaque plateforme a son embedder. Flutter utilise l'embedder pour interfacer avec le système d'exploitation sous-jacent.

Le moteur Flutter exécute le code Dart, gère les actifs, gère les événements et, surtout, rend l'UI. Il dessine (ou rasterise les interfaces utilisateur) de la même manière indépendamment de la plateforme. D'où l'indépendance de la plateforme.

Le moteur Flutter utilise [Skia](https://skia.org) ou [Impeller](https://docs.flutter.dev/perf/impeller) pour les tâches de rendu de bas niveau. Skia est une bibliothèque graphique open-source avec un ensemble robuste de capacités de dessin. Skia permet de créer des UI fluides.

Récemment, nous avons obtenu Impeller. Impeller fournit un nouveau runtime de rendu pour Flutter. Il est déjà l'outil de rendu par défaut sur les appareils iOS et arrive bientôt sur Android. Il s'agit d'une amélioration et devrait remplacer Skia.

Sur la plateforme hôte, Flutter accède à un "canvas" noir (ou à l'écran) et rend avec ses outils. Sur le web, c'est la même chose mais avec une légère différence. Il n'y a pas d'embedder (car il n'y a pas de système d'exploitation). Cependant, nous convertissons l'UI directement du framework Flutter en rendu CanvasKit.

Que nous utilisions l'embedder et le moteur Flutter pour rendre une application sur n'importe quel système d'exploitation ou que nous nous appuyions sur la transpilation de Dart en JavaScript pour rendre sur les navigateurs, les applications Flutter sont les mêmes sur l'UI peinte.

![Les "canvas" utilisés par Flutter pour chaque plateforme](https://www.freecodecamp.org/news/content/images/2024/05/image.png)
_Les "canvas" utilisés par Flutter pour chaque plateforme_

![Les couches de rendu des applications Flutter dans les systèmes d'exploitation et les navigateurs](https://www.freecodecamp.org/news/content/images/2024/05/image-4.png)
_Les couches de rendu des applications Flutter dans les systèmes d'exploitation et les navigateurs_



Cette architecture entière rend possible que si un nouveau système d'exploitation apparaît, nous n'aurons besoin que de répliquer l'embedder avec l'ABI du moteur Flutter attendu pour ce nouveau système d'exploitation. Une fois fait, toutes les applications Flutter existantes fonctionneront facilement sur le système d'exploitation.

En dehors du rendu de l'UI, Flutter est également indépendant de la plateforme grâce aux canaux de plateforme.

## Comment fonctionnent les canaux de plateforme dans Flutter ?

Dans Flutter, les canaux de plateforme servent de routes de communication importantes à l'exécution entre le framework Flutter et l'application hôte (ou la plateforme native sous-jacente). Les canaux de plateforme agissent comme des ponts entre le code Dart indépendant de la plateforme et les fonctionnalités spécifiques à la plateforme.

Les canaux de plateforme permettent une intégration transparente des fonctionnalités spécifiques à la plateforme dans les applications Flutter. Avec eux, vous pouvez tirer parti des capacités de chaque plateforme cible tout en maintenant une base de code unifiée.

Avec les canaux de plateforme, Flutter atteint l'indépendance de la plateforme en abstraisant les détails spécifiques à la plateforme. Ainsi, vous pouvez écrire du code Flutter qui peut s'exécuter de manière transparente sur plusieurs plateformes sans modification superflue.

Il existe deux types de canaux de plateforme : les canaux de méthode et les canaux d'événements.

### Canaux de méthode

Ils sont les plus utilisés. Ils facilitent la communication bidirectionnelle entre le code Dart et le code de la plateforme native.

À travers les canaux de méthode, les applications Flutter peuvent invoquer des méthodes spécifiques à la plateforme, passer des paramètres et recevoir des résultats de manière asynchrone. L'inverse est également possible. L'hôte (ou le côté natif de l') application peut appeler des méthodes définies à l'intérieur de l'application Flutter.

Cela vous permet d'accéder aux API spécifiques à la plateforme, aux services système et aux fonctionnalités matérielles, telles que l'accès aux capteurs de l'appareil, l'interaction avec les composants UI natifs, ou l'intégration avec les SDK spécifiques à la plateforme.

![Diagramme systématique des MethodChannels](https://www.freecodecamp.org/news/content/images/2024/05/platform-channels.png)
_Diagramme systématique des MethodChannels_

### Canaux d'événements

Les canaux d'événements transmettent des événements asynchrones de la plateforme native au code Dart. Ils sont utiles dans les cas où la plateforme native doit notifier l'application Flutter des événements ou mises à jour asynchrones.

De bons exemples de tels scénarios incluent :

* Réception de données de capteurs en temps réel
* Gestion des notifications push
* Surveillance des événements au niveau du système, etc.

Les canaux d'événements sont cruciaux. Avec eux, vous pouvez construire des applications réactives, pilotées par des événements, qui répondent aux changements dans la plateforme sous-jacente de manière indépendante de la plateforme.

Votre code Dart doit écouter les flux d'événements. Les valeurs de ces flux sont émises depuis la plateforme sous-jacente. Mais la manière dont vous les gérez dans la partie Dart de Flutter est généralement la même, d'où l'indépendance de la plateforme.

### Paquets et plugins

Un paquet Flutter est un code réutilisable qui peut étendre votre application. Plus de 25000 paquets Flutter sont déployés sur [pub.dev](https://pub.dev). Il existe déjà un ou des paquets de fonctionnalités spécifiques à la plateforme que vous souhaitez implémenter dans votre application.

Le framework Flutter lui-même est relativement petit. C'est la contribution de la communauté qui construit ces paquets qui rend l'écosystème entier grand.

Bien qu'il existe de nombreux paquets pour les fonctionnalités directes de Flutter, certains fournissent des fonctionnalités dépendantes de la plateforme (comme la caméra, la localisation, les permissions, etc.). Ces paquets dépendants de la plateforme utilisent des canaux de plateforme et des plugins en coulisses.

Les plugins dans Flutter sont des paquets qui encapsulent des fonctionnalités spécifiques à la plateforme et les exposent au code Dart via des canaux de méthode et d'événements. Ils agissent comme des enveloppes autour des canaux de plateforme, fournissant une surface d'API unifiée pour accéder aux fonctionnalités spécifiques à la plateforme. Ils abstraient les complexités de l'interaction avec les canaux de plateforme.

Cependant, s'il n'y a pas de plugin pour une fonctionnalité que vous construisez (ce qui est rare), vous pouvez utiliser des canaux de plateforme. Ils font en sorte que le code Flutter fonctionne de la même manière, quelle que soit la plateforme. Vous devrez écrire les gestionnaires de méthodes ou d'événements spécifiques à la plateforme dans les langages de programmation spécifiés par les plateformes impliquées.

![Langages de programmation des canaux de plateforme](https://www.freecodecamp.org/news/content/images/2024/05/image-5.png)
_Langages de programmation des canaux de plateforme_

## Résumé

Comprendre l'indépendance de la plateforme de Flutter est important pour apprécier l'architecture innovante qui alimente Flutter.

De la manière dont il rend les interfaces utilisateur de la même manière sur chaque appareil, à la manière dont il peut exécuter du code spécifique à l'appareil à l'exécution, Flutter vous offre une expérience de développeur fluide et des applications hautement performantes.

La prochaine fois que vous utiliserez Flutter, ne soyez pas surpris de la manière dont il atteint la même application sur différents appareils.

Santé !