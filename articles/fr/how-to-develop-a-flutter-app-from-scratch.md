---
title: Tutoriel Flutter – Comment développer une application avec Flutter à partir
  de zéro
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2024-04-26T18:11:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-a-flutter-app-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/1060
seo_title: Tutoriel Flutter – Comment développer une application avec Flutter à partir
  de zéro
---

539.jpg
tags:
- name: Flutter
  slug: flutter
- name: Développement Front-end
  slug: front-end-development
- name: Développement Web
  slug: web-development
seo_title: null
seo_desc: "Récemment, j'ai travaillé sur une stratégie marketing pour une nouvelle application basée sur le framework Flutter. Une équipe de développement entière m'a enseigné les tenants et aboutissants de Flutter en tant que technologie multiplateforme. \nEt d'après ce que j'ai appris, je crois que ..."
---

Récemment, j'ai travaillé sur une stratégie marketing pour une nouvelle application basée sur le framework Flutter. Une équipe de développement entière m'a enseigné les tenants et aboutissants de Flutter en tant que technologie multiplateforme. 

Et d'après ce que j'ai appris, je crois que le framework est accessible à presque tout le monde, même à ceux qui ont peu de compétences techniques.

Dans ce tutoriel, vous apprendrez à construire votre première application Flutter, du développement du concept à la publication sur l'App Store. 

Je vous enseignerai comment configurer correctement votre environnement de développement et coder avec le principal langage de code Flutter – Dart. Certains concepts clés comme la gestion d'état, la construction d'interface utilisateur et les widgets vous prépareront à créer et lancer une application polie. Je vous guiderai même à travers la publication de votre application sur l'App Store

Alors, trouvez un siège confortable et préparez-vous, car nous allons plonger dans le sujet. 

### Prérequis

Tout d'abord, vous devez choisir un environnement. Je vous conseille de choisir soit Visual Studio Code, soit Android Studio. Le premier est léger et est une bonne option qui fonctionne bien sur différents types de systèmes d'exploitation. Android Studio est tout aussi puissant, si vous prévoyez de construire des applications Android. 

Si vous êtes débutant, regardez VS Code avec l'extension Flutter, car il offre une expérience conviviale et c'est un très bon point de départ. Assurez-vous simplement que votre PC répond aux exigences minimales du système pour le développement Flutter, comme mentionné dans [la documentation officielle de Flutter](https://docs.flutter.dev/get-started/install/windows/desktop).

## Table des matières

* [Développement d'applications mobiles avec Flutter](#heading-developpement-dapplications-mobiles-avec-flutter)
* [11 étapes simples pour créer votre première application Flutter](#heading-11-etapes-simples-pour-creer-votre-premiere-application-flutter)
* [Étape 1 : Commencez avec une idée ou une vision pour votre future application](#heading-etape-1-commencez-avec-une-idee-ou-une-vision-pour-votre-future-application)
* [Étape 2 : Installez le SDK Flutter sur votre ordinateur](#heading-etape-2-installez-le-sdk-flutter-sur-votre-ordinateur)
* [Étape 3 : Installez des bibliothèques et des plugins pour faciliter le codage](#heading-etape-3-installez-des-bibliotheques-et-des-plugins-pour-faciliter-le-codage)
* [Étape 4 : C'est l'heure de coder !](#heading-etape-4-cest-lheure-de-coder)
* [Étape 5 : Organisez votre projet](#heading-etape-5-organisez-votre-projet)
* [Étape 6 : Codez les éléments d'interface utilisateur et les interactions (Widgets)](#heading-etape-6-codez-les-elements-dinterface-utilisateur-et-les-interactions-widgets)
* [Étape 7 : Écrivez l'écran de splash](#heading-etape-7-ecrivez-lecran-de-splash)
* [Étape 8 : Démonstration des changements](#heading-etape-8-demonstration-des-changements)
* [Étape 9 : Testez votre application](#heading-etape-9-testez-votre-application)
* [Étape 10 : Styles de code](#heading-etape-10-styles-de-code)
* [Étape 11 : Publiez votre application](#heading-etape-11-publiez-votre-application)
* [Conclusion](#heading-conclusion)

## Développement d'applications mobiles avec Flutter

Commençons par quelques informations utiles sur notre framework. Basiquement, Flutter est un kit open-source développé par Google qui vous permet de construire des applications mobiles, ainsi que des applications réseau et intégrées. 

La chose clé à retenir à propos de Flutter est que, une fois que vous écrivez du code, vous pouvez télécharger votre application sur Android, iOS et le web. Ensuite, vous pouvez l'installer sur plusieurs systèmes, y compris un PC. Cela vous fait vraiment gagner beaucoup de temps et d'efforts par rapport à la construction d'applications séparées pour chaque plateforme.

Avant de commencer, apprenons pourquoi Flutter est extrêmement utile pour le développement mobile.

### Avantages de Flutter

Comme je l'ai déjà mentionné, Flutter fonctionne avec plusieurs systèmes et plateformes à la fois, couvrant Android et iOS ainsi que Windows, Linux et MacOS. Imaginez – c'est une seule base de code qui les gouverne tous ! 

Un autre avantage est que Flutter a une barrière d'entrée basse grâce à sa syntaxe simple. Par exemple, si vous voulez afficher du texte, vous créez facilement un widget appelé "Text", attribuez un style et une couleur, ajoutez du texte – et voilà. Cela semble simple – et c'est le cas.

### Limites de Flutter

Avant de décider d'utiliser Flutter, vous devez comprendre le tableau complet. Il existe des technologies natives comme Kotlin et Swift qui ont leurs avantages uniques. 

Le premier est qu'elles fournissent le délai le plus bas possible et l'expérience utilisateur la plus fluide. Elles sont parfaites pour les applications qui nécessitent des temps de réponse courts, comme les applications de trading financier.

Le deuxième avantage est l'excellente performance et l'optimisation. Vous n'avez aucune redondance dans ces situations spécifiques. Mais seulement dans ces situations. Donc, si votre application nécessite une utilisation intensive du matériel de l'appareil, comme des graphiques 3D en temps réel ou l'intégration de capteurs, vous devriez envisager de passer au natif.

### Développement Back-end avec Flutter

Mais, si vous avez décidé de suivre la voie Flutter, il y a une chose importante à considérer : Flutter est un framework front-end, et il nécessite un framework back-end pour les applications complexes. En bref, si votre application a un état qui doit être stocké, vous avez besoin d'une technologie back-end supplémentaire. 

Je préfère Node.js car il peut être lancé n'importe où, mais vous pouvez utiliser tout autre service viable. Pour une startup, un bon exemple est les fonctions cloud Firebase gratuites. Et comme je l'ai déjà mentionné, Dart est le principal langage de code de Flutter, donc vous pouvez également écrire un back-end avec son aide.

Mais choisir un bon back-end pour votre application Flutter est un tout autre sujet. Je vous recommande de lire l'article « [Décoder l'art de choisir le back-end Flutter parfait : Un guide pour les développeurs](https://www.dhiwise.com/post/decoding-the-art-of-choosing-the-perfect-flutter-backend) ».

Sinon, n'hésitez pas à me rejoindre dans ce tutoriel – commençons !

## 11 étapes simples pour créer votre première application Flutter

### Étape 1 : Commencez avec une idée ou une vision pour votre future application

De nombreux outils peuvent vous aider à cette étape, mais celui que vous choisissez dépendra de vos compétences en design. 

Vous pouvez trouver de l'inspiration visuelle sur Dribbble, Pinterest et de nombreux autres sites web. Mais lorsqu'il s'agit de créer un design, il y a trois façons de procéder :

Si vous n'avez pas de compétences en design, envisagez d'utiliser Canva pour le design d'applications et MockFlow pour les maquettes.

Si vous avez quelques compétences, alors plongez dans Figma et vous apprécierez ses nombreuses fonctionnalités. Créez vos maquettes, et seulement après une réflexion approfondie, développez le design complet. 

Notez que vous pouvez également utiliser des plugins comme [Figma2Flutter](https://www.figma.com/community/plugin/1110606481076006495/figma2flutter) et [FigmaToFlutter](https://www.figma.com/community/plugin/844008530039534144/figmatoflutter) pour transformer votre design en code Flutter fonctionnel. Ainsi, la première étape peut facilement être la dernière dans la création de votre première application Flutter. 

Mais je vous encourage à continuer à lire et à vous faire une idée de l'ensemble du processus. Le code auto-généré par l'un des plugins peut contenir des bugs, et vous devrez être capable de les corriger.

![Image](https://lh7-us.googleusercontent.com/Ia_FGjqAIgXnhIgIektxVcy7Cz5tt0HIHPZUfYDmaaeEemW4-b85f-5l6gKNt-m4TlvAtvDgXHPtpuPoAzxZvpoOhqnV2wXyq2KLUTvsyVX1cReuL8StA-b0Ni7scnnkV8sQ93_UT3ORN7ZiLT1gjfU)
_Figma2Flutter est une excellente source de plugins_

Et enfin, si vous êtes bloqué, trouvez un designer. Cela peut être un freelance professionnel, une agence de design, ou simplement un ami avec des compétences en design. Dans tous les cas, vous aurez toujours l'option de transformer votre design en utilisant les plugins Figma2Flutter ou FigmaToFlutter.

### Étape 2 : Installez le SDK Flutter sur votre ordinateur

Cette étape est très facile. Suivez le lien vers la [page de téléchargement de Flutter](https://docs.flutter.dev/get-started/install). Choisissez votre système d'exploitation et votre plateforme. N'oubliez pas de vérifier les exigences logicielles. 

Ici, vous pourriez avoir besoin de mieux matériel ou d'installer certains paquets supplémentaires, mais je pense que vous pouvez le faire en utilisant le tutoriel sur le site web de Flutter.

[Le tutoriel Flutter](https://docs.flutter.dev/get-started/install/windows/desktop) propose différentes options pour un éditeur de texte ou un environnement de développement intégré (IDE). Donc, installez celui que vous préférez, comme Android Studio, et installez le SDK Flutter. Lorsque vous avez terminé le tutoriel, revenez ici, et nous continuerons.

### Étape 3 : Installez des bibliothèques et des plugins pour faciliter le codage

Les bibliothèques Flutter sont comme des boîtes à outils qui contiennent des parties pré-construites pour vous aider à créer du code plus rapidement et plus facilement. Elles sont remplies de toutes sortes de choses utiles comme des boutons, des formulaires, des animations et plus encore. Vous pouvez les utiliser pour tout, de la conception d'interfaces utilisateur à la gestion des données et à la gestion des interactions. 

Maintenant, parlons des plugins dans Flutter. Ils sont comme des outils spéciaux qui aident votre application à faire plus. 

Ces plugins connectent votre code Flutter aux fonctionnalités natives de votre appareil, comme la caméra ou le GPS. Vous pouvez également ajouter facilement des fonctionnalités supplémentaires à votre application sans avoir à écrire tout le code vous-même. Il suffit d'écrire un peu de code initial, d'appuyer sur entrée et vous obtiendrez plusieurs lignes de code à partir de l'exemple.

![Image](https://lh7-us.googleusercontent.com/90Szu_VCkBADwx-I817QjLhKju50Rcl5K5vdq_D0L6gAS-8L29_fflJjQof4l5hZAuOOzmiraI3TKefuHgJR4Zm3cBfg35NCL14t2B_t8174787S65ygVulzay9ffHAFzoNSiL7jiSLfDNRpnY-zRIQ)
_Paramètres -> Plugins_

Vous pouvez également trouver des idées pratiques pour votre application sur [Flutter Awesome](https://flutterawesome.com/) et [pub.dev](https://pub.dev/) avec des bibliothèques officielles et le soutien de la communauté. Ces sites hébergent des développeurs tiers qui construisent leurs bibliothèques sur [GitHub](https://github.com) et les partagent ici. Elles ont été testées sur des projets réels et incluent une large gamme de fonctionnalités telles que la connexion à des serveurs, l'utilisation de Bluetooth et l'ajout d'effets visuels. 

De plus, les bibliothèques sont notées selon leur popularité et leur qualité. Une note élevée augmente les chances que la bibliothèque que vous choisissez ait le moins de bugs possible.

Si vous rencontrez des problèmes, ne vous inquiétez pas ! Vous pouvez vous tourner vers [Flutter Awesome](https://flutterawesome.com/) et [pub.dev](https://pub.dev/) pour obtenir de l'aide. Puisque Flutter est open source, vous pourrez trouver les dernières mises à jour et obtenir de l'aide d'autres développeurs Flutter. Et s'il y a un nouveau problème, il est probable qu'il soit corrigé dans la prochaine mise à jour de Flutter. Facile comme bonjour !

### Étape 4 : C'est l'heure de coder !

Flutter est construit et traduit en code machine en utilisant le langage de programmation Dart. Les appareils hôtes comprennent ce code, assurant une performance rapide et efficace. C'est un langage de programmation orienté objet, ouvert, développé par Google. 

Voici quelques-unes des principales caractéristiques de Dart :

* Orienté objet avec des classes, l'héritage et les mixins
* Typage statique pour la détection précoce des erreurs
* Prend en charge la compilation juste-à-temps (JIT) et à l'avance (AOT)
* Gestion automatique de la mémoire avec garbage collection
* Ressource de programmation asynchrone intégrée
* Syntaxe cohérente et simple

Dart est un langage de programmation qui vous permet de décrire toute logique dans une application mobile de manière facile à comprendre. Ses fonctionnalités, telles que la version de programmation réactive et les fonctionnalités asynchrones, le rendent adapté à la construction d'applications haute performance et réactives qui peuvent fonctionner sur iOS et Android. 

Bien que moins largement adopté que certains autres langages, l'intégration étroite de Dart avec Flutter l'a rendu de plus en plus populaire pour l'amélioration des applications mobiles.

Maintenant, revenons au code ! Créez simplement votre projet sur une page blanche standard avec la possibilité de lancer et de tester votre application.

Voici notre simple application Flutter, qui affiche un message "Bonjour, Flutter !". Elle démontre la forme de base d'une application Flutter, ainsi que l'aspect d'accès principal, définissant un widget statique et construisant une MaterialApp avec un Scaffold, une AppBar et un widget Text ciblé :

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Ma première application Flutter'),
        ),
        body: Center(
          child: Text(
            'Bonjour, Flutter !',
            style: TextStyle(fontSize: 24),
          ),
        ),
      ),
    );
  }
}

```

Je vous conseille vivement de diviser votre code en parties logiques :

* UI
* communication serveur
* logique métier
* images
* traduction et plus

Le plan vous permet d'organiser votre code et de le structurer facilement.  

L'étape suivante est tout aussi importante que le codage lui-même. Choisir la bonne gestion d'état est comme les bases du développement d'applications Flutter. Là, vous découvrirez différents aperçus comme les facteurs, l'architecture Model-View-ViewModel et la différence entre deux modèles de gestion populaires de Flutter. 

Alors, qu'attendons-nous, passons directement à cela.

### Étape 5 : Organisez votre projet

#### Choisissez la bonne solution de gestion d'état

La gestion d'état contrôle l'état des éléments de l'interface utilisateur tels que les champs de texte, les boutons et les cases à cocher dans une interface utilisateur graphique (UI). Elle garantit que l'état des autres contrôles UI affecte l'état d'un contrôle UI particulier. Cette technique est cruciale pour assurer une expérience utilisateur fluide dans votre application 

Pour choisir la bonne gestion d'état, considérez des facteurs tels que la complexité de votre projet, votre familiarité avec différentes solutions de gestion d'état et les besoins spécifiques de votre projet. Google recommande de commencer avec quelque chose de basique comme Vanilla, qui est simple et facile à utiliser.

Maintenant, regardons l'architecture Model-View-ViewModel (MVVM), qui est une partie importante de la gestion d'état. Et vous devez choisir entre Provider et BloC. La différence entre ces deux modèles populaires de gestion d'état de Flutter est la suivante : 

* Pour les petits projets et les délais courts, vous pouvez utiliser Provider MVVM. Mais attention : le compromis est une performance légèrement plus lente et une scalabilité moindre.
* Pour les projets de taille moyenne et grands, Google suggère d'utiliser BLoC. Une telle approche vous permet de gérer la flexibilité et l'échelle de votre code. 

Si vous n'avez pas encore décidé ce que vous allez utiliser pour votre projet, voici quelques pages avec des descriptions et des exemples de la documentation de la bibliothèque officielle :

1. [https://pub.dev/packages/flutter_bloc](https://pub.dev/packages/flutter_bloc)
2. [https://pub.dev/packages/provider](https://pub.dev/packages/provider)
3. [https://docs.flutter.dev/data-and-backend/state-mgmt](https://docs.flutter.dev/data-and-backend/state-mgmt)

Alors, choisissez une option de gestion d'état qui convient à votre application.

#### Dossiers séparés pour les écrans

Vous devez garder votre code propre. Pour cela, il est bon de créer des dossiers séparés pour chaque écran, où les fichiers de code sont stockés. 

Par exemple, vous auriez un dossier pour l'écran de splash et un autre pour l'écran de connexion. De plus, gardez le code de l'interface utilisateur séparé du code de la logique métier, dans des fichiers séparés.

Votre structure de répertoire préparée devrait ressembler à ceci :

![Image](https://lh7-us.googleusercontent.com/U5DSbWDz5PicgCi690wdIzoxFlkUVz9p-z0jHq74AHs3Cvu18kIpiQ2eo47sMo4Bkbwwi4_kKcyv-EU-ZmuNt368IzJvoLC-VEGDjpoSBIdTHyf0-CBNzkJcHg-1IqoURIBHVXj8pci-2dBVJ3xkBsk)
_Mon organisation de dossiers_

#### Système hautement décomposé

Lorsque vous commencez à travailler avec un écran, vous devez le décomposer soigneusement en petites parties. Par exemple, sur l'écran principal, il y a une liste de produits. Cet élément doit être dans un fichier séparé et même un seul élément d'une liste doit être dans un fichier différent. 

Plus votre système est décomposé, plus il vous sera facile à l'avenir de changer un morceau de code, ainsi que de supporter et de mettre à l'échelle votre produit. 

Voici quelques conseils sur la manière de décomposer un système en composants plus petits efficacement :

* Commencez par définir les objectifs, les fonctionnalités, les utilisateurs potentiels et les limitations de votre système pour établir des limites claires.
* Divisez le système en morceaux plus petits et indépendants pour une gestion plus facile.
* Attribuez des fonctionnalités spécifiques et des interfaces à chaque composant et comment ils interagissent.
* Pour atteindre les objectifs du système, testez tous les composants et leurs interactions.
* Pour optimiser les performances, affinez les composants en fonction des retours.

#### Couleurs et styles

Lorsque vous avez la structure des écrans, vous pouvez coder la transition de base entre eux et les styles d'une application. Flutter facilite la gestion de tous vos styles en un seul endroit, comme les couleurs des boutons, les polices et les icônes, afin que vous puissiez les personnaliser facilement. Vous les codez dans un style choisi – un schéma de style clair ou sombre.

L'étape suivante consiste à coder des transitions simples et des motifs qui feront correspondre votre application à vos choix de style. Comme vous le verrez dans l'exemple de code ci-dessous, Flutter facilite grandement le contrôle des styles. Cela vous permet de tester et de personnaliser l'apparence de votre application autant que vous le souhaitez.

![Image](https://lh7-us.googleusercontent.com/Kzimy6hu5i143WNcWPIPCkLkoB1wz9LpZCEmHZ-UJ-ByYiysAI5QG42YaqXjk0Icelxx-SdxmHGwoBDnvPMhnOTCniDnO_cA4Xxd5siib0dnXfMbyGCzNJ9hpBJBd1WZw5ZRj9cCut-wsFwbOgMpARo)
_Mon fichier pour gérer les thèmes_

Et voici un exemple de code utile, afin que vous puissiez expérimenter et essayer vos propres idées à votre guise.

```dart
@override
Widget build(BuildContext context) {
 return TextField(
   controller: controller,
   focusNode: focusNode,
   style: AppStyles.getCitySearchTextStyle(),
   decoration: InputDecoration(
     hintText: context.tr().searchHint,
     hintStyle: AppStyles.getSearchHintStyle(),
     contentPadding: AppPaddings.horizontalPaddingM,
     isDense: true,
     border: InputBorder.none,
     focusedBorder: InputBorder.none,
     enabledBorder: InputBorder.none,
     errorBorder: InputBorder.none,
     disabledBorder: InputBorder.none,
   ),
 );
}
```

#### Configuration du routeur

Il existe un outil de navigation robuste pour gérer les transitions entre des moniteurs spécifiques au sein de l'application. Il existe deux techniques de navigation principales que vous pouvez utiliser dans Flutter :

* Navigator : il s'agit d'un widget de navigation intégré à Flutter. Il vous permet de faire glisser et de soulever l'écran de la pile, offrant une expérience de navigation simple vers l'avant et vers l'arrière. Vous pouvez utiliser des routes nommées et anonymes pour comprendre les unités d'affichage vidéo de l'application.
* Bibliothèque de routage : vous pouvez utiliser une bibliothèque comme go_router ou auto_router si vous avez besoin d'une navigation plus complexe. Ce package fournit des fonctionnalités telles que l'analyse des liens profonds et le contrôle fin des piles de navigation.

Voici également la [documentation sur la navigation Flutter](https://docs.flutter.dev/cookbook/navigation), au cas où vous auriez besoin de quelque chose.

Maintenant, vous devez configurer le routeur comme montré dans l'exemple à l'écran et me faire savoir si tout a bien fonctionné pour vous :

#### Navigation simple entre les écrans

En utilisant l'approche `Navigator.Push` et `MaterialPageRoute`, cet exemple montre une façon de naviguer entre les écrans (ou routes) dans une application Flutter.

```dart
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => SecondScreen())
```

![Image](https://lh7-us.googleusercontent.com/cv3qVAKCIT0XjdyyFJg9Lt6Vu9zLdENES21LD9_z9JJJSUV_rL6Wiu0kRakHjSR6jgzl77-0U45GQkgX9tUEQbAKTvCEawJp7o4HSjIUrJ1u0rWAfvIx3jELK2E64Eb9xBtDQYS-GFACr64SK0WLRLg)
_Mon fichier pour gérer le routeur_

Alors, maintenant vous pouvez commencer à configurer les langues pour votre application car c'est aussi important que d'avoir les bons éléments d'interface utilisateur dans le projet.

#### Langues

Vous voudrez localiser votre application, afin que les utilisateurs puissent sélectionner différentes langues ou l'avoir automatiquement localisée.

Google fournit des recommandations sur l'approche qui convient le mieux à vos besoins et exigences techniques que vous pouvez [lire ici](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization).

Commencez par créer un fichier de traductions pour une langue. Si nécessaire, vous pouvez ajouter plus de langues plus tard.

![Image](https://lh7-us.googleusercontent.com/DOZzrnB6iANF95EyDh9EnlFeGJ057zLaudUk7Ej5pP-5z12SMT7W5Ceh3Laf10i7izm7mCloUz29goBSyh4G25LqTWeo8hu1kJXfLHU3baEAaWk0l3lcamLBlTZqkMYLIQzvxylphHh6fZKigPcTvaY)
_Ma localisation en ukrainien_

```dart
return Center(
 child: Text(Localization.from(context).continueText),
)
```

Une fois que vous avez terminé cette partie, vous aurez les éléments de base d'une application – styles, localisation, structures d'écran et transitions. Et ensuite, vous pouvez commencer à programmer chaque écran.

### Étape 6 : Codez les éléments d'interface utilisateur et les interactions (Widgets)

À ce stade, vous coderez les éléments de base de l'interface utilisateur d'un écran et la logique qui contrôlera l'interface utilisateur. Par exemple, vous pourriez développer une logique pour parcourir une liste de produits à partir d'un serveur distant en sélectionnant un élément dans une liste de produits. Ensuite, vous écrivez du code qui convertit un modèle de données particulier en un élément.

Flutter utilise des widgets prêts à l'emploi. En fait, Flutter est tout à propos des widgets. L'une des choses innovantes à leur sujet est qu'ils sont des composants d'interface utilisateur réutilisables que vous pouvez intégrer directement dans l'application au lieu de les construire à partir de zéro. Comparez cela à différentes stratégies qui utilisent des objets exclusifs (dispositions, perspectives, contrôleurs), où Flutter a un modèle d'objet unique et unique.

Chaque objet dans Flutter est un widget – des boutons aux pads en passant par le texte, et les blocs de construction existants jusqu'aux niveaux les plus bas de personnalisation. Vous utiliserez les mêmes outils que l'équipe Flutter utilise pour construire les leurs.

Les widgets dans Flutter sont disponibles pour le rendu, mais ils peuvent également poser un problème avec la structure globale. Vous devrez planifier le formulaire car les grandes applications peuvent nécessiter jusqu'à dix couches de code pour créer un élément principal. Pour un excellent article avec de nombreux widgets prêts à l'emploi, consultez [ce guide](https://proandroiddev.com/my-flutter-adventure-widgets-8ea08a7067eb). 

Sinon, voici une liste courte mais utile d'éléments de code indispensables pour votre application de base :

#### Élément 1 : Créer des listes

Cette partie du code démontre une façon de créer une liste d'éléments en utilisant `ListView.Builder`. Elle prend une liste d'éléments et génère des widgets `ListTile` pour chaque élément, vous permettant de gérer les événements de robinet sur les gadgets :

```dart
 
  final List<String> items =
      List<String>.generate(10, (int index) => "Élément avec le numéro $index");

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView.builder(
        itemCount: items.length,
        itemBuilder: (BuildContext context, int index) {
          return ListTile(
            title: Text(items[index]),
            onTap: () {
              ScaffoldMessenger.of(context)
                  .showSnackBar(SnackBar(content: Text('Élément $index tapé !')));
            },
          );
        },
      ),
    );
  }
```

Voici à quoi votre liste devrait ressembler après le codage :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-29.png)
_Vue de la liste_

#### Élément 2 : Requête API

Ce code montre comment obtenir des données à partir d'une API en utilisant le bundle HTTP. Il effectue une requête GET à l'URL souhaitée et gère la réponse, traitant les enregistrements récupérés ou gérant les erreurs :

```dart
Future<void> fetchData() async {
  final response = await http.get(Uri.parse('https://api.example.com/data'));
  if (response.statusCode == 200) {
    final data = json.decode(response.body);
    // Traiter les données récupérées ici
    print(data);
  } else {
    // Gérer l'erreur
    print('Échec de la récupération des données : ${response.statusCode}');
  }
}
```

#### Élément 3 : Stylisation du texte

Ici, vous pouvez voir une démonstration de la façon d'afficher deux textes en colonne et de styliser le contenu textuel dans Flutter en utilisant la classe `TextStyle`, qui vous permet de personnaliser les styles comme la couleur, la taille de la police, le poids de la police et le style de la police :

```dart

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Bonjour !',
              style: TextStyle(
                color: Colors.red,
                fontSize: 36,
                fontWeight: FontWeight.bold,
                fontStyle: FontStyle.italic,
              ),
            ),
            Text(
              'Flutter',
              style: TextStyle(
                color: Colors.blue,
                fontSize: 18,
                fontWeight: FontWeight.bold,
                fontStyle: FontStyle.italic,
              ),
            ),
          ],
        ),
      ),
    );
  }
```

Le résultat est superbe, n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-30.png)
_Vue du texte stylisé_

#### Élément 4 : Boutons avec style personnalisé

Celui-ci montre une façon de créer un bouton avec style personnalisé en utilisant le widget `MaterialButton`. Il vous permet de personnaliser des propriétés telles que la hauteur, le haut, la forme, la couleur et un widget (dans cette situation, un widget de texte avec style personnalisé) :

```dart

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: MaterialButton(
          elevation: 0,
          height: 50,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
          ),
          color: Colors.blue,
          onPressed: () {
            ScaffoldMessenger.of(context)
                .showSnackBar(const SnackBar(content: Text("Bouton tapé !")));
          },
          child: const Padding(
            padding: EdgeInsets.all(16),
            child: Text(
              "Bonjour bouton",
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Colors.white,
                fontSize: 12,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ),
      ),
    );
  }
```

Le bouton Bonjour est prêt !

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-31.png)
_Vue du bouton avec style personnalisé_

#### Élément 5 : Icônes

Celui-ci suggère une façon d'afficher une icône (dans cette situation, une icône de célébrité) dans votre application Flutter, vous permettant de personnaliser sa couleur et sa longueur :

```dart
Icon(
  Icons.star,
  color: Colors.yellow,
  size: 24,
)
```

#### Élément 6 : Affichage d'images à partir du réseau

En spécifiant l'URL de la photo, la largeur, le haut et la santé, ce code démontre comment afficher une photo à partir d'une URL réseau en utilisant le widget `Image.Network` :

```dart
Image.network(
  'https://example.com/image.jpg',
  width: 200,
  height: 200,
  fit: BoxFit.cover,
)
```

#### Élément 7 : Conteneur animé simple

Ce code crée un conteneur actif qui change sa taille (largeur et haut) lorsqu'un ensemble vrai (`_isExpanded`) est changé, avec une animation fluide décrite en utilisant la période requise et la courbe :

```dart
AnimatedContainer(
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  color: Colors.blue,
  duration: Duration(milliseconds: 500),
  curve: Curves.easeInOut,
)
```

#### Élément 8 : Gestion de la saisie de texte

Ce code démontre comment prendre soin de la saisie de texte en utilisant le widget TextField, fournissant une propriété de rappel pour gérer les changements de texte et de telles décorations (comme une étiquette) au processus de saisie de données :

```dart

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: TextField(
          decoration: InputDecoration(
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.greenAccent, width: 5.0),
            ),
            enabledBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.red, width: 5.0),
            ),
            hintText: 'Entrez votre nom',
          ),
        ),
      ),
    );
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-32.png)
_Vue de la gestion du texte_

### Étape 7 : Écrivez l'écran de splash

Chaque application commence par un écran de splash qui affiche un logo ou un indicateur de chargement pendant que l'application se prépare. Après cela, l'application charge les données nécessaires et l'écran de splash apparaît.

Alors, créons notre premier écran et les choses deviendront beaucoup plus faciles à partir de là. Vous avez déjà beaucoup de widgets dans votre arsenal, mais vous pouvez copier et coller une partie du code ci-dessous. Vous pouvez voir plus de mon code à l'écran, mais je laisserai le reste pour que vous l'amélioriez.

Ci-dessous, vous pouvez voir mes images pour écrire un écran de splash :

![Image](https://lh7-us.googleusercontent.com/tPabzLQbBRwNIBLaitdmqZdqbUGuGwiNVD_X-dgGiOKMZLUbv50BYL_bU1lLxHTtMI25xScW2QeQ9qRItt_aXp5w_C9xGj7xWLpjtE-rq5AN0pr5AqaI5UGaMd4e2FWS-ey_v2Od31wwBpSzvxamKDY)
_Mon code d'écran de splash_

```dart
IntrinsicWidth(
 child: Column(
   mainAxisSize: MainAxisSize.min,
   children: [
     const FlutterLogo(
       size: 250,
     ),
     const Gap(AppSizes.sizeM),
     Container(
       padding: AppPaddings.allPaddingXS,
       decoration: const BoxDecoration(
         color: AppColors.alabaster,
         borderRadius: AppBordersRadius.borderRadiusAll100,
       ),
       child: const LinearProgressIndicator(
         backgroundColor: AppColors.alabaster,
         borderRadius: AppBordersRadius.borderRadiusAll100,
         minHeight: AppSizes.sizeSSM,
       ),
     )
   ],
 ),
)
```

![Image](https://lh7-us.googleusercontent.com/OAsCqqs-qai8W6FMItKdWqdjCM_DaBW4jnBD02yvOVGRIGAIFoMmBTDTLg2H1atQQdwc8MOVos18GnJTBiHvL8RqVmYkk4T9jQiqzlPn9-sSr30ywM8TVCZR9M1H7Z-RkEFekHfDGrxxB5utONCbOYs)
_C'est ainsi que l'écran apparaît à partir du code précédent_

### Étape 8 : Démonstration des changements

Une fois que vous avez terminé une section de votre code, appuyez sur un bouton dans Android Studio pour voir rapidement les changements sur votre écran. 

C'est l'une des principales caractéristiques de Flutter. Vous n'avez pas besoin de redémarrer votre projet ou de reconstruire l'ensemble de l'application chaque fois que vous apportez une modification. Avec Flutter, vous pouvez utiliser le rechargement à chaud ou le redémarrage à chaud. Appuyez sur un bouton et vos modifications apparaîtront sur votre téléphone ou votre site web en une seconde.

Voici à quoi vos modifications peuvent ressembler sur votre écran :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/IMG_1562.JPG)
_Démonstration des changements_

À l'heure actuelle, votre application est presque prête, mais il reste quelques étapes importantes. L'une d'entre elles est le test. C'est la seule façon de vérifier que tout fonctionne bien. Et si ce n'est pas le cas, vous pouvez facilement voir l'erreur et la corriger.

### Étape 9 : Testez votre application

Pour vous assurer que votre application fonctionne et que tout est construit correctement, vous devez la tester. Par exemple, vous avez peut-être programmé une fonctionnalité et accidentellement cassé une autre. De plus, si vous avez des éléments dépendants de la plateforme, comme Bluetooth ou NFC, vous devrez vérifier comment ils fonctionnent dans votre application.  

Mais les tests peuvent avoir des cas de test positifs et négatifs. Les cas positifs doivent toujours être testés. Par exemple, une application doit fonctionner avec un login et un mot de passe corrects. Les cas négatifs sont lorsque qu'un ingénieur QA essaie de "casser" un produit en entrant les mauvais types de données (au lieu d'un email, nous entrons "11111111"). Les cas négatifs sont nécessaires pour minimiser les erreurs des utilisateurs et pour écrire des invites de vérification compréhensibles ("Veuillez entrer votre email ici").

Comme vous pouvez le voir, cela souligne l'importance de tests approfondis. En simulant des erreurs utilisateur, nous pouvons nous assurer que nos applications fonctionnent correctement et offrent une expérience utilisateur fluide. 

Dans l'exemple ci-dessous avec une connexion, vous pouvez voir la fonctionnalité de test appropriée :

```dart
  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
           TextField(
            controller: textEditingController,
            decoration: const InputDecoration(
             focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.greenAccent, width: 5.0),
            ),
            enabledBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.red, width: 5.0),
                borderSide: BorderSide(color: Colors.red, width: 5.0),
            ),
            hintText: 'Entrez votre nom',
          ),
        ),
        const SizedBox(
         height: 16,
        ),
        MaterialButton(
         elevation: 0,
         height:50,
         shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
         ),
         color: Colors.blue,
         onPressed:(){
          if (textEditingController.text.trim().isEmpty){
           ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(
             content: Text("Vous devez entrer votre nom"),
            ),
           );
          }else{
         ScaffoldMessenger.of(context).showSnackBar(
         SnackBar(
         content:Text(
         "Votre nom est ${textEditingController.text.trim()}",
        ),
       ),
      );
     }
    },
    child: const Padding(
     padding: EdgeInsets.all(16),
     child: Text(
      "Afficher mon nom",
      textAlign: TextAlign.center,
      style: TextStyle(
       color: Colors.white,
       fontSize: 12
       fontWeight: FontWeight.bold,
      ),
     ),
    ),
   ),
  ],
 ),
),
);
}
```



![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-33.png)
_La vue de test_

### Étape 10 : Styles de code

Pour maintenir un style cohérent, il est important de suivre certaines normes lors du codage. Google recommande un certain style de code – une façon d'appeler les variables ou les méthodes et les dimensions. Les bibliothèques et les plugins (analyseurs) pour Android Studio marquent le code et suggèrent des modifications au fur et à mesure que vous écrivez votre code. 

En voici quelques-uns que je peux recommander :

* [Dio](https://pub.dev/packages/dio) pour les requêtes réseau
* [Flutter bloc + bloc + bloc](https://pub.dev/packages/bloc_concurrency) concurrency pour utiliser la gestion d'état BLoC
* [Provider](https://docs.flutter.dev/data-and-backend/state-mgmt/simple) pour utiliser la gestion d'état Provider
* [Auto_route](https://pub.dev/packages/auto_route) + [Auto Route Generator](https://pub.dev/packages/auto_route_generator) pour le routage

Il y en a beaucoup plus que vous pouvez trouver, des plugins pour mettre en cache toute image réseau aux générations de splash natifs. Les styles de code sont nécessaires pour garantir la qualité du code et le support futur du code pour les plus grands projets.

Vous pouvez [lire plus dans la documentation Flutter ici](https://docs.flutter.dev/tools/formatting).

### Étape 11 : Publiez votre application

Lorsque vous avez terminé de coder et de tester votre application, vous devez tester ses performances sur les plateformes où vous prévoyez de l'avoir – iOS, Android et Web. 

La première étape consiste à publier la création d'un compte développeur sur chaque système. Après cela, vous devrez payer une certaine somme d'argent (une fois par an dans le cas d'Apple) et ensuite télécharger les applications. Ensuite, [les employés de Google et Apple examinent les applications](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en) pour vérifier leur conformité aux exigences, aux normes et aux lois. Si tout se passe bien, l'application sera publiée.

Après avoir surmonté tous les défis, rappelez-vous qu'un lancement réussi n'est qu'un début. Jetez un coup d'œil aux images ci-dessous et assurez-vous que votre application est prête à être découverte par les utilisateurs :

![Image](https://lh7-us.googleusercontent.com/V7Dinp2-PzzMP_WXNlPyjiD8TmyWMRPlzH-NA_zPspEDSlCMFvF2hWNjenMg_pFNmY_w8trDKBNOKhTXDVhuVQ9NNcSlSNIPyW8qzFM38zRLLyY_aj-jCSpLabSkiFP7zHsmjDFsHL5INg1rvD1UD-w)
_Tableau de bord de publication Google Play_

![Image](https://lh7-us.googleusercontent.com/s0yHjjeKHt38vxojQONVe1FKAbh4RqjeFHFprV2kKkAcfiFYiF9UYr-FCrF8O1u3J1wyuo7eAMzfICA57wfbPEgmGEyRrHwuKuewICvsATNuxg6DZLV60mAhHrE8_IuNIM46-Nd4epEYZGAxoBRyJfI)
_Tableau de bord de publication App Store_

Pour publier votre application Flutter sur l'App Store, vous devez compléter quelques étapes. 

Tout d'abord, inscrivez-vous au programme Apple Developer et téléchargez les certificats pour signer votre application. Après cela, créez un compte App Store Connect pour gérer votre application. Maintenant, en utilisant Xcode, téléchargez votre application pour la distribution sur l'App Store. Lorsque tout est fait, votre dernière étape consiste à entrer des détails tels que des captures d'écran, une description et un prix pour votre application. 

Cela semble assez facile, n'est-ce pas ? Si vous cherchez plus d'informations, visitez simplement la [page du développeur Apple](https://developer.apple.com/ios/submit/) pour en savoir plus.

Presque la même chose s'applique au Google Play Store. Inscrivez-vous à un compte Google Play Developer et liez-le à un compte Google Wallet Merchant pour les achats intégrés (si nécessaire). Ensuite, assurez-vous simplement que votre application répond à leurs exigences techniques et directives. Cela inclut des choses comme la signature de l'application, la politique de confidentialité et la classification du contenu. 

Lors de la troisième étape, vous devez remplir les détails de votre application que les utilisateurs verront dans le Play Store. Maintenant, téléchargez votre bundle d'application ou simplement un fichier APK et configurez les paramètres de prix et de distribution. Vous devrez peut-être attendre un peu, car Google prendra un certain temps pour examiner votre application afin de s'assurer qu'elle respecte leurs politiques.

Une fois votre application approuvée, vous pouvez enfin la publier sur le Google Play Store et la rendre disponible pour les utilisateurs ! Ce n'était qu'un aperçu – donc pour en savoir plus sur le processus, [visitez la page officielle](https://support.google.com/googleplay/android-developer/answer/9859751) et obtenez autant d'informations que vous en avez besoin.

Maintenant, vous êtes prêt à conquérir le monde. Assurez-vous simplement de vérifier attentivement tous les paramètres avant de publier votre application. Vous pouvez définir une date et une heure précises pour la publication de votre application Flutter, gérer les versions de production, et plus encore. Pour être honnête avec vous, il y a beaucoup plus de fonctionnalités que vous ne pouvez l'imaginer, alors je vous laisse le faire par vous-même.

## Conclusion

Très bien, maintenant votre application est prête. Dans ce tutoriel, je vous ai donné les bases de la construction d'une application mobile Flutter de base. N'ayez pas peur de prendre votre idée unique et de la concrétiser. 

Comme je vous l'ai déjà dit, la communauté Flutter est une mine d'informations, alors n'hésitez pas à vous y plonger et à l'explorer ! 

Au fait, voici un autre conseil précieux de ma part à garder dans votre boîte à outils de développeur : commencez simplement, gardez votre code propre et organisé, et testez au fur et à mesure que vous construisez. Avec ces bases et un peu d'effort, vous construirez rapidement une excellente application Flutter !

Je tiens également à remercier mon partenaire de développement, Mikhailo, qui m'a aidé tout au long de la création de ce guide pour vous. Sans son expertise technique, je ne saurais même pas comment vous expliquer correctement toutes ces instructions, merci encore !

### Avez-vous une idée pour un projet Flutter ?

Mon entreprise Covent IT est un adopteur précoce du [framework Flutter](https://coventit.com/services/flutter-development) et une entreprise bien établie de développement d'applications mobiles en général. Si vous avez un projet prometteur en tête, n'hésitez pas à [demander une consultation pour un projet Flutter](https://coventit.com/contact-us).