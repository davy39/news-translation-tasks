---
title: Avis sur Google Flutter – Pourquoi les développeurs d'applications mobiles
  adorent Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-22T13:56:46.000Z'
originalURL: https://freecodecamp.org/news/why-mobile-apps-makers-are-in-love-with-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/emile-perron-xrVDYZRGdw4-unsplash.jpg
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Avis sur Google Flutter – Pourquoi les développeurs d'applications mobiles
  adorent Flutter
seo_desc: 'By Vitaly Kuprenko

  Why do app makers love Flutter? Because Flutter is amazing.

  Flutter caters to both businesses (by offering reasonable development costs) and
  developers (by offering great usability and speed). That’s why some big companies
  have swi...'
---

Par Vitaly Kuprenko

Pourquoi les créateurs d'applications adorent-ils Flutter ? Parce que Flutter est incroyable.

Flutter répond aux besoins des entreprises (en offrant des coûts de développement raisonnables) et des développeurs (en offrant une grande convivialité et rapidité). C'est pourquoi certaines grandes entreprises ont adopté Flutter, comme Google Ads, Alibaba, Reflectly, et bien d'autres. 

Google a fait un excellent travail en développant Flutter, et ils continuent d'améliorer ce framework.

Dans cet article, je vais donner un aperçu rapide de Flutter et de ses toutes nouvelles fonctionnalités, et je vais expliquer pourquoi ce framework vaut la peine d'être utilisé. De plus, je vais discuter de ce qui pourrait freiner les grandes entreprises à adopter Flutter.

Mais commençons par le début.

## Quel est l'essentiel de Flutter ?

Voici quelques points sur Flutter que vous connaissez peut-être déjà :

* c'est un outil open-source et multiplateforme
* les applications sont écrites en langage de programmation Dart
* il possède son propre moteur graphique (Skia)
* il supporte officiellement trois plateformes : iOS, Android et le web (en bêta)
* officiellement, il supporte également le bureau

Google a introduit la première version de Flutter à la fin février 2018. En avril 2020, la version 1.12 est disponible.

## Qu'y a-t-il de si spécial avec Flutter ?

Flutter combine la qualité des applications natives avec la flexibilité du développement multiplateforme.

En fait, de nombreux outils multiplateformes permettent d'écrire le code une fois et de l'utiliser sur iOS et Android. Pourtant, tous ne peuvent pas rendre le même aspect qu'une application native.

Mais c'est exactement ce que fait Flutter : au lieu d'être un wrapper sur le dessus des composants UI natifs (comme React Native et Xamarin), Flutter dessine l'UI à partir de zéro.

Flutter maintient l'expérience et le ressenti natifs de l'application, et vous n'avez pas à vous soucier de ses performances sur aucune plateforme.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Mockup1-Copy.png)

De plus, puisque Flutter est un framework open-source, n'importe quel développeur peut y apporter des modifications sur [GitHub](https://github.com/flutter/flutter) et envoyer des demandes de fusion. Et si vous regardez la popularité de Flutter – **90,4K** étoiles GitHub, **12k forks**, et **18 445 commits** – vous comprendrez que les développeurs adorent Flutter et contribuent à son amélioration.

## Comment fonctionne Flutter ?

**Flutter n'est pas compilé directement en applications iOS ou Android**. Les applications sont lancées sur la base d'une combinaison de moteur de rendu (construit en C++) et de Flutter (construit en Dart). Tous les fichiers générés de cette manière s'attachent à chaque application et aux assemblages SDK pour une plateforme spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Flutter-Architecture.png)

C'est comme le développement de jeux : un jeu n'alloue pas son framework, et la fonctionnalité est exécutée avec le moteur de jeu. Même chose pour les logiciels Flutter – toutes les applications basées sur le SDK Flutter remplacent des parties des frameworks natifs par des éléments Flutter.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/How-Flutter-interacts-with-native-components.png)

Bien que cela puisse impacter la taille de l'application finale, les performances restent assez bonnes – le rendu est effectué avec des vitesses allant jusqu'à **120 FPS**.

Grâce à la compilation native pour les processeurs ARM, le rendu simple et un ensemble de widgets et d'outils intégrés, Flutter simplifie le processus de développement.

De plus, il offre quelques fonctionnalités très intéressantes comme **Hot Reload**.

Voici comment cela fonctionne :

Lorsque vous cliquez sur le bouton Hot Reload, toutes les modifications du code sont affichées immédiatement sur les appareils, émulateurs et simulateurs. L'application continue de fonctionner là où elle en était avant que vous n'ayez cliqué sur le hot reload : le code est mis à jour, mais l'exécution continue.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/How-Flutter-works-Copy.png)

## Pourquoi choisir Flutter pour les applications multiplateformes ?

Les nouvelles versions de Flutter continueront de sortir avec des fonctionnalités plus avancées. Mais il y a déjà beaucoup de fonctionnalités améliorées qui expliquent parfaitement pourquoi Flutter est si apprécié.

**Premièrement**, le développement multiplateforme avec Flutter, contrairement à la croyance populaire, ne rend pas le logiciel pire.

Flutter est livré avec tous les widgets natifs pour les interfaces Android et iOS comme Material Design et Cupertino. De plus, le framework peut modifier le comportement d'éléments séparés pour créer une UX similaire pour les utilisateurs de l'application.

**Deuxièmement**, Flutter permet de mettre en œuvre la compilation discrète de fichiers en mode développement. La compilation JiT accélère le développement et le débogage des logiciels.

**Troisièmement**, Flutter permet un backend flexible et évolutif.

Il supporte des plugins comme Firebase, SQLite, et bien d'autres ([pub.dev](https://pub.dev/flutter/packages) vous aidera à trouver celui dont vous avez besoin). Firebase rend l'infrastructure de l'application évolutive, sans serveur et redondante.

Ainsi, si vous travaillez sur des applications nécessitant des bases de données en temps réel ou des fonctions cloud, Flutter vous couvre.

Et enfin : Flutter est très **facile à apprendre**.

Dès le début, les développeurs Google se sont fixés pour objectif de réduire la barrière à l'entrée. Ils ont soigneusement élaboré la documentation et les ressources que les développeurs peuvent utiliser. Il dispose même de sections spéciales que vous pouvez utiliser pour commencer à apprendre le framework en fonction de votre spécialisation :

* Flutter pour les développeurs [Android](https://flutter.dev/docs/get-started/flutter-for/android-devs)
* Flutter pour les développeurs [iOS](https://flutter.dev/docs/get-started/flutter-for/ios-devs)
* Flutter pour les développeurs [React Native](https://flutter.dev/docs/get-started/flutter-for/react-native-devs)
* Flutter pour les développeurs [Xamarin.Forms](https://flutter.dev/docs/get-started/flutter-for/xamarin-forms-devs)
* Flutter pour les développeurs [web](https://flutter.dev/docs/get-started/flutter-for/web-devs)

Grâce à la documentation détaillée de Flutter, vous comprendrez comment écrire du code en Dart même si vous n'avez de l'expérience qu'avec les outils graphiques Unity pour créer des jeux Android.

## Flutter 1.12 (Dernière Version) et ses avantages

Voyons quelles nouvelles fonctionnalités Flutter a introduites dans sa dernière version [1.12](https://flutter.dev/docs/development/tools/sdk/release-notes/release-notes-1.12.13) :

### Mode sombre iOS

Désormais, Flutter supporte l'apparence et le ressenti d'iOS 13, y compris la prise en charge complète du mode sombre dans les widgets Cupertino. Et il ne s'agit pas seulement de changer l'arrière-plan, mais aussi d'adapter le reste des couleurs pour qu'elles soient bien assorties.

### Support d'ajout à l'application

Une autre grande amélioration est la mise à jour d'Add-to-App, qui permet d'intégrer Flutter dans des applications iOS/Android déjà existantes.

La nouvelle version de Flutter supporte l'ajout d'une instance Flutter en plein écran à l'application, ainsi que :

* Intégration stabilisée des [APIs](https://flutter.dev/docs/development/add-to-app#api-usage) en Java, Kotlin, Objective-C et Swift
* Support de l'utilisation de plugins dans les modules Flutter
* Mécanismes d'intégration supplémentaires via les AARs Android et les frameworks iOS

### Support web bêta

Les nouveaux canaux Flutter master, dev et beta offrent un support amélioré pour le web. Vous voulez des exemples ?

Voici **Rivet**, un projet éducatif qui a utilisé Flutter et Firebase pour créer une version web de leur application.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Mockup1-Copy-2.png)

### Dart 2.7

La nouvelle version du framework introduit Dart 2.7.

Cette mise à jour améliore l'expérience de fonctionnement avec Dart 2.5 dans la manière dont les chaînes sécurisées gèrent les capacités et les processus d'extension. Cela aide les développeurs à prévenir les erreurs lorsque les variables obtiennent une valeur nulle et analysent les entiers dans une chaîne.

Et voici quelques autres fonctionnalités de la dernière version de Flutter :

* support de bureau macOS (alpha)
* débogage multi-appareils
* tests d'images goldens
* améliorations de la construction Android
* DartPad mis à jour

## C'est bien, mais pas sans problèmes : Qu'est-ce qui retient les développeurs ?

Flutter est vraiment génial : facile à démarrer, simple à utiliser, et présenté par une grande entreprise technologique. Pourtant, voici les raisons pour lesquelles votre développeur senior pourrait ne pas partager votre optimisme.

### La (faible) popularité de Dart

Contrairement à Java/Kotlin pour Android ou Swift/Objective-C pour iOS, Dart n'a pas encore une grande popularité. Et il est peu probable qu'il en ait un jour.

Dart n'est pas trop difficile à apprendre, et il existe de nombreux tutoriels (comme [celui-ci](https://dart.dev/guides/language/language-tour)), mais certains développeurs continuent à utiliser Java et d'autres outils familiers.

En même temps, vous ne pouvez pas utiliser Flutter sans utiliser Dart : même la fonctionnalité phare de Flutter – Hot Reload – ne fonctionnera pas sans Dart.

### Ne supporte pas tous les appareils

Vous ne pouvez pas créer d'applications pour les appareils iOS 32 bits comme ceux plus anciens que l'iPhone 5s. Même chose pour les ordinateurs Windows : vous ne pouvez pas exécuter Flutter sur votre ordinateur portable 32 bits.

Et les développeurs de Flutter n'ont pas l'intention de corriger cela car "cela nécessiterait un travail très important".

Ainsi, si vous souhaitez coder avec Flutter, vous devrez posséder un appareil x64 bits ou mettre à niveau celui que vous utilisez actuellement.

### Nombre limité de bibliothèques

Bien qu'il existe de nombreuses bibliothèques Flutter comme **fl_chart** (pour dessiner des graphiques dans Flutter), **path_provider** (utilisé pour localiser un fichier sur Android/iOS), [**flutter_sliding_tutorial**](https://github.com/Cleveroad/flutter_sliding_tutorial) et bien d'autres, le nombre est encore limité.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/-------1-.gif)
_Tutoriel de glissement Flutter_

Ce n'est pas difficile à expliquer : Flutter est un framework relativement nouveau, et les développeurs n'ont pas eu assez de temps pour développer autant de bibliothèques que les langages natifs offrent.

Néanmoins, les bibliothèques les plus importantes sont déjà là, et de nouvelles sortent tout le temps.

### Les applications Flutter sont plus grandes en taille

...par rapport aux applications développées en natif. L'équipe de Flutter a [mesuré](https://flutter.dev/docs/resources/faq#how-big-is-the-flutter-engine) la taille minimale de l'application (sans composants Material, juste un widget Center unique, construit avec flutter build apk --split-per-abi), regroupée et compressée, à 4,3 Mo pour ARM, et 4,6 Mo pour ARM 64.

L'application de base est maintenant d'environ **4 Mo** sur Android et **10 Mo** sur iOS.

### Peu d'expertise prouvée

Flutter peut être aimé par les développeurs, mais les grandes entreprises n'ont pas précipité l'arrêt de la création d'applications natives (ou React Native) pour se tourner vers Flutter.

Pour la plupart des entreprises, le plus gros problème est la nouveauté de Flutter. Dart est plus récent que Java ou C#, et Flutter lui-même est tout nouveau.

Bien sûr, il existe de nombreuses [applications open-source Flutter](https://www.cleveroad.com/blog/open-source-flutter-apps), y compris de grandes comme Google Ads ou Hamilton (consultez la liste complète [ici](https://itsallwidgets.com/)), mais pas trop nombreuses.

Et personne ne veut être la personne qui adopte un tout nouveau framework pour devoir revenir au développement natif quelques mois plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Flutter-vs-React-Native-Copy.png)

Mais ce qui est encore plus important, c'est que Flutter est un chemin que vous parcourez seul :

* il n'y a pas beaucoup de bonnes pratiques confirmées (au moins pour les grands projets)
* il y a toujours une chance que vous soyez le premier à rencontrer ce problème particulier
* peu d'espoir que quelqu'un vous aide – vous devrez faire chaque étape avec soin et être prêt à affronter les conséquences

## Où utiliser Flutter

Tout d'abord, il est préférable d'utiliser Flutter pour les startups MVP lorsque vous avez un temps limité et souvent un budget limité pour vérifier le modèle économique.

Une application Flutter est **moins chère** :

* par rapport au coût de deux applications natives
* l'équipe de développement est 40 % plus petite
* processus linéaires
* vous pouvez passer plus de temps à travailler sur les fonctionnalités de l'application

En optant pour un projet Flutter, vous réduisez le nombre d'heures de développement. Le développement Flutter ne prend pas autant de temps que le natif.

Voici un exemple. Supposons que vous créez une application de type Instagram pour deux plateformes. Le développement iOS prendra, environ, **700** heures, Android également **700h**.

Avec Flutter, vous couvrirez les deux plateformes et gagnerez du temps : **700h Android + 700h iOS vs. 700h Flutter**.

Vous économisez énormément de temps que vous pouvez consacrer à autre chose, comme peaufiner les fonctionnalités.

## Conclusion

Si vous construisez des applications avec un temps et un budget limités, Flutter vaut définitivement la peine d'être essayé.

Il est aussi bon qu'il en a l'air, et avec chaque nouvelle mise à jour, les développeurs Google ajoutent encore plus d'outils pour le développement multiplateforme.

Bien sûr, ce framework peut sembler inhabituel pour les amateurs de C# et Java, mais cela ne signifie pas qu'il vous sortira de votre zone de confort. Après avoir maîtrisé les petites différences de syntaxe, vous verrez bientôt que le développement d'UI est quelques fois plus rapide par rapport au développement natif.

Et si vous réussissez, et si Flutter persiste, cela pourrait vous apporter une expérience passionnante en développement mobile et des opportunités pour l'avenir.