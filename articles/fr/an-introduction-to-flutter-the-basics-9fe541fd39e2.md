---
title: 'Une introduction à Flutter : les bases'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T17:02:55.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-flutter-the-basics-9fe541fd39e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iXlLHBudODi07-1X3qFNBA.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Une introduction à Flutter : les bases'
seo_desc: 'By Stanislav Termosa

  I’ve been hearing about how amazing Flutter is and I’ve decided to try it out to
  learn something new. I wished to have more topics to discuss with colleagues.

  It started by watching, then reading, and then I started coding. It wa...'
---

Par Stanislav Termosa

J'ai entendu parler de la façon dont Flutter est incroyable et j'ai décidé de l'essayer pour apprendre quelque chose de nouveau. Je souhaitais avoir plus de sujets à discuter avec mes collègues.

Cela a commencé par regarder, puis lire, et ensuite j'ai commencé à coder. C'était une bonne expérience. Les applications fonctionnaient, et tout ce qui était écrit n'était pas difficile à comprendre.

Cependant, le processus n'était pas assez fluide - certains détails n'étaient pas expliqués dans ces ressources. De plus, comme tout était nouveau pour moi (la plateforme elle-même, le langage de programmation, les approches et même le développement d'applications mobiles), le manque de ces détails était douloureux.

À chaque fois que quelque chose ne fonctionnait pas, je ne savais pas quoi rechercher sur Google : Dart, Flutter, Window, Screen, Route, Widget ?

J'ai décidé que lire la documentation sur Dart, Flutter et tous ses widgets ne serait pas une bonne idée car cela prendrait trop de temps. De plus, je n'avais pas beaucoup de temps car le but était de découvrir cette nouvelle chose, et non de devenir un expert dans le domaine. J'ai pensé à ce moment-là qu'il serait incroyable s'il existait un guide court sur Flutter, qui décrirait tous les concepts nécessaires pour comprendre le framework et être capable d'écrire des applications simples, mais pas plus !

#### À propos du guide

La plupart des articles sur ce sujet sont bien écrits et directs. Le problème est qu'ils nécessitent que vous connaissiez certaines bases, et ces petites choses ne sont pas décrites dans les articles qui sont censés vous donner des connaissances de base.

Dans cette série, j'essaierai d'éviter ce problème. Nous commencerons à partir de zéro et créerons des applications en expliquant chaque étape. Au cours de cette série, nous utiliserons **tous les widgets de base**, concevrons **une interface unique**, interagirons avec **des modules natifs**, et construirons notre application pour **les plateformes iOS et Android**.

Cette série est écrite du point de vue d'un développeur web. La plupart d'entre vous sont probablement familiers avec cette pile. L'analogie avec une plateforme familière est meilleure que celle où vous devez construire des maisons ou utiliser Animal, Dog, Foo, Bar, etc.

Je vais garder cela court, pour économiser votre temps. Pour les plus curieux d'entre vous, je mettrai des liens utiles autour du texte.

#### À propos de la plateforme

Flutter est très nouveau, mais une plateforme prometteuse, qui a attiré l'attention de grandes entreprises qui ont [publié leurs applications](https://flutter.io/showcase) déjà. Elle est intéressante en raison de sa simplicité par rapport au développement d'applications web, et en raison de sa vitesse par rapport aux applications natives.

Les hautes performances et la productivité dans Flutter sont atteintes en utilisant plusieurs techniques :

* Contrairement à de nombreuses autres plateformes mobiles populaires, Flutter **n'utilise pas JavaScript de quelque manière que ce soit**. Dart est le langage de programmation. Il compile en code binaire, et c'est pourquoi il fonctionne avec les performances natives d'Objective-C, Swift, Java ou Kotlin.
* Flutter **n'utilise pas de composants d'interface utilisateur natifs**. Cela peut sembler étrange au premier abord. Cependant, parce que les composants sont implémentés dans Flutter lui-même, il n'y a pas de couche de communication entre la vue et votre code. Grâce à cela, les jeux atteignent la meilleure vitesse pour leurs graphismes sur les smartphones. Ainsi, les boutons, le texte, les éléments multimédias, l'arrière-plan sont tous dessinés par le moteur graphique de Flutter. En passant, il convient de mentionner que le bundle de l'application Flutter "Hello, World" est assez petit : iOS ≈ 2,5 Mo et Android ≈ 4 Mo.
* Flutter **utilise une approche déclarative**, inspirée par le framework web React, pour construire son interface utilisateur basée sur des widgets (appelés "composants" dans le monde du web). Pour tirer le meilleur parti des widgets, ils sont **rendus uniquement lorsque nécessaire**, généralement lorsque leur état a été modifié (comme le fait le Virtual DOM pour nous).
* En plus de tout ce qui précède, le framework dispose d'un **Hot-reload intégré** [Hot-reload](https://flutter.io/docs/development/tools/hot-reload), typique du web, mais toujours absent sur les plateformes natives. Cela permet au framework Flutter de reconstruire automatiquement l'arborescence des widgets, vous permettant de visualiser rapidement les effets de vos modifications.

Il existe un excellent article sur l'utilisation pratique de ces fonctionnalités par un développeur Android qui a recréé son [application de Java à Dart](https://proandroiddev.com/why-flutter-will-change-mobile-development-for-the-best-c249f71fa63c) et a partagé ses impressions.

Je voulais partager avec vous quelques chiffres de son article.

* **Java** (avant) : Nombre de fichiers = 179 et lignes de code 12 176
* **Dart** (après) : Nombre de fichiers = 31 et lignes de code 1 735.

Vous pouvez en savoir plus sur les [détails techniques de la plateforme](https://flutter.io/docs/resources/inside-flutter) ou consulter des [exemples d'applications](https://itsallwidgets.com/).

#### À propos de Dart

Dart est un langage de programmation que nous utiliserons pour développer notre application dans Flutter. Son apprentissage n'est pas difficile si vous avez de l'expérience avec Java ou JavaScript. Vous le comprendrez rapidement.

J'ai essayé d'écrire un article sur Dart pour vous, afin de décrire le champ minimal requis pour Flutter. Après plusieurs tentatives, je n'arrivais toujours pas à l'écrire de manière à ce qu'il soit court et couvre les concepts de base en même temps. Les auteurs de [A Tour of the Dart Language](https://www.dartlang.org/guides/language/language-tour) ont bien réussi cette tâche !

#### Installation initiale

Ce sujet, tout comme Dart, est bien couvert dans le guide officiel — je ne vais donc pas le copier ici.

Suivez ce [guide d'installation court](https://flutter.io/docs/get-started/install), en choisissant votre système d'exploitation et en le suivant étape par étape. Configurez également [votre éditeur préféré](https://flutter.io/docs/get-started/editor?tab=vscode) pour travailler avec Dart et Flutter (généralement, cela nécessite 2 plugins différents). [Exécutez votre application](https://flutter.io/docs/get-started/test-drive?ide=vscode) pour vous assurer que vous êtes prêt à continuer.

Voici un conseil pour les utilisateurs de MacOS. Si vous n'aimez pas la quantité d'espace gaspillée par les bordures des appareils virtuels, vous pouvez les désactiver et passer à un modèle d'iPhone 8 (il n'est pas aussi long que l'iPhone X) :

* Matériel → Appareil → iOS # → iPhone 8
* Fenêtre → Afficher les bordures de l'appareil

Il est possible de vivre sans les boutons virtuels car nous avons des touches de raccourci : **Maj + Cmd** (⌘) **+ H** - aller à l'accueil, **Cmd (⌘) + Droite** - faire pivoter le téléphone, et vous pouvez en trouver plus dans le menu Matériel. Je recommanderais également d'activer le clavier à l'écran, car il est important de comprendre si votre application est utilisable lorsque la moitié de l'écran est recouverte. Pour ce faire, vous appuyez sur **Cmd (⌘) + K** après avoir mis le focus sur un champ de saisie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZMOglBNOwXyCGeSoRyDZpw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*01LRxQhezBpJy7v5gMENyw.jpeg)
_iPhone 8 & iPhone X avec et sans bordures_

#### Structure du projet

Voyons d'abord ce qu'il y a dans le projet généré par le framework Flutter :

* **lib/** - tout comme [pub](https://www.dartlang.org/guides/libraries/create-library-packages) (le gestionnaire de paquets de Dart), tout le code sera ici
* **pubspec.yml** - stocke une liste de paquets nécessaires pour exécuter l'application, tout comme **package.json** le fait. Vous devez vous souvenir que dans les projets Flutter, vous ne pouvez pas utiliser pub directement, mais à la place, vous utiliserez la commande Flutter : `flutter pub get <package_name>`
* **test/** - Je suis sûr que vous savez de quoi il s'agit. N'est-ce pas ? Vous pouvez les exécuter via flutter test
* **ios/** & **android/** - le code spécifique à chaque plateforme, y compris les icônes d'application et les paramètres où vous définissez les permissions dont vous aurez besoin pour votre application (comme l'accès à la localisation, Bluetooth).

Nous n'avons pas besoin d'en savoir plus sur les fichiers dans le dossier pour l'instant. Ouvrons le dossier **lib/** où **main.dart** nous attend. Comme vous pouvez le deviner, celui-ci est le point d'entrée de notre application. Tout comme dans le langage C (ou des tonnes d'autres), l'application sera exécutée en appelant la fonction main().

#### À propos des widgets (Hello World est ici)

Dans Flutter, tout est construit sur des Widgets. Les éléments d'interface utilisateur, les styles, les thèmes, et même l'état est géré dans des Widgets spécifiques. Commençons par une petite application.

Remplacez le code de **main.dart** par celui donné ci-dessous, lisez les commentaires et exécutez l'application.

```dart
import 'package:flutter/widgets.dart'; // ensemble de base de widgets

// Lorsque Dart exécute l'application, il appelle la fonction main()
main() => runApp( // La fonction runApp() démarre l'application Flutter
  Text( // ceci est un widget, il rend le texte donné (pensez à cela comme un <span>)
    'Hello, World!!!', // le premier argument est un texte qui doit être rendu
    textDirection: TextDirection.ltr, // ici nous définissons la direction "de gauche à droite"
  ),
);
```

**runApp(…)** n'a qu'un argument widget. Le widget deviendra le widget racine pour toute l'application. D'ailleurs, changer le widget racine ne peut pas être géré par Hot-reload, vous devrez donc redémarrer votre application pour voir les changements.

[**Text(…)**](https://docs.flutter.io/flutter/widgets/Text-class.html) - Flutter ne peut pas rendre le texte sans connaître la préférence pour la direction du texte. Pour rendre le texte, nous devons définir **Text.textDirection**. Ne le confondez pas avec la règle CSS [**text-align**](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align). C'est l'analogie de [**direction**](https://developer.mozilla.org/en-US/docs/Web/CSS/direction) - la partie de l'API d'internationalisation. Cependant, ne vous inquiétez pas, nous n'aurons pas besoin de le définir pour chaque widget **Text** - plus tard nous verrons comment le définir pour toute l'application.

Votre application est-elle en cours d'exécution ? Hourra ! "Hello, World!" est maintenant à l'écran. N'est-ce pas ? Eh bien, quelque chose a mal tourné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OioFvf1U2Ysd5Bt1ViG_5A.jpeg)
_Contenu chevauché par l'encoche de l'iPhone_

Le texte est chevauché par l'encoche. Nous pouvons utiliser tout l'écran pour notre application, et nous avons imprimé notre contenu tout en haut où les informations système sont également rendues.

Essayons de décaler notre contenu.

```dart
import 'package:flutter/widgets.dart';

main() => runApp(
  Center( // Le widget qui aligne le contenu au centre
    child: Text(
      'Hello, World!',
      textDirection: TextDirection.ltr,
    ),
  ),
);
```

**Center(…)** est le widget qui aligne un autre widget donné dans la propriété **child** au centre de lui-même. Vous verrez souvent les propriétés **child** et **children** dans les applications Flutter, car presque tous les widgets les utilisent s'ils ont besoin d'un ou de plusieurs widgets à rendre à l'intérieur d'eux.

Une composition de widgets dans Flutter est utilisée pour représenter une interface, pour changer son apparence et pour partager des données. Par exemple, **Directionality(…)** définit la direction du texte pour tous les widgets imbriqués (donc nous n'avons pas besoin de la spécifier pour **Text** à chaque fois).

```dart
import 'package:flutter/widgets.dart';

main() => runApp(
  Directionality(
    textDirection: TextDirection.ltr,
    child: Center(
      child: Text('Hello, World!'),
    ),
  ),
);
```

Jetons un coup d'œil à un widget très important, et changeons le design de notre application :

```dart
import 'package:flutter/widgets.dart';

main() => runApp(
  Directionality(
    textDirection: TextDirection.ltr,
    child: Container( // le nouveau widget ! C'est <div> pour le monde de Flutter
      // Pour [Container], la propriété [color] signifie la couleur de l'arrière-plan
      color: Color(0xFF444444),
      child: Center(
        child: Text(
          'Hello, World!',
          style: TextStyle( // nous utilisons le widget [TextStyle] pour personnaliser le texte
            color: Color(0xFFFD620A), // définir la couleur
            fontSize: 32.0, // et la taille de la police
          ),
        ),
      ),
    ),
  ),
);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*qI7ecRrkzB34tmlOhDXd_w.png)
_Application Hello World réalisée avec Flutter_

Il existe plusieurs options sur [comment utiliser le widget **Color(…)**](https://docs.flutter.io/flutter/dart-ui/Color-class.html). Nous avons utilisé le widget avec le nombre donné en utilisant la notation hexadécimale. Cela ressemble presque à la manière dont nous définissons les couleurs HEX sur le web, mais ici nous avons 2 symboles supplémentaires au début. Il s'agit d'un nombre qui représente la transparence où 0x00 est complètement transparent, et 0xFF n'est pas transparent du tout.

[**TextStyle(…)**](https://docs.flutter.io/flutter/dart-ui/TextStyle/TextStyle.html) est plus intéressant. Vous pouvez l'utiliser pour définir une couleur, une taille et un poids de police, un espacement des lignes, souligner le texte, etc.

L'application Flutter est complète ! Vous pouvez lire comment la construire pour [Android](https://flutter.io/docs/deployment/android) et [iOS](https://flutter.io/docs/deployment/ios), où vous pouvez également apprendre à la publier sur le magasin d'applications pertinent. Si cela ne vous suffit pas, j'ai couvert quelques sujets supplémentaires ci-dessous.

#### À propos des widgets sans état

Maintenant, nous savons à quel point il est facile d'utiliser des widgets. L'étape logique suivante serait de créer nos propres widgets. J'ai mentionné précédemment qu'il existe deux types de widgets (en fait, il y en a plus, mais ne compliquons pas les choses pour l'instant). Il y a des widgets sans état et des widgets avec état.

Nous avons utilisé des widgets sans état dans les exemples précédents. "Sans état" ne signifie pas qu'ils n'ont pas d'état du tout. Les widgets sont des classes Dart, qui peuvent être déclarées avec des propriétés. Mais changer ces propriétés dans un widget sans état n'affectera pas ce qui a déjà été rendu. La mise à jour des propriétés d'un widget avec état déclenchera des hooks de cycle de vie et rendra son contenu en utilisant le nouvel état. Nous commencerons par les widgets sans état car ils semblent un peu plus faciles.

Pour en créer un, nous avons besoin de :

1. Un beau nom pour la nouvelle classe.
2. Étendre notre classe à partir de **StatelessWidget**.
3. Implémenter la méthode **build()**, qui recevra un argument de type **BuildContext** et retournera un résultat de type **Widget**.

```dart
import 'package:flutter/widgets.dart';

main() => runApp(
  Directionality(
    textDirection: TextDirection.ltr,
    child: Center(
      child: MyStatelessWidget()
    ),
  ),
);

class MyStatelessWidget extends StatelessWidget {
  // L'annotation @override est nécessaire pour l'optimisation, en l'utilisant
  // nous disons que nous n'avons pas besoin de la même méthode de la classe parente
  // donc le compilateur peut l'ignorer
  @override
  Widget build(BuildContext context) { // Je décrirai [context] plus tard
    return Text('Hello!');
  }
}
```

Un exemple de widget avec un argument :

```dart
// …

class MyStatelessWidget extends StatelessWidget {
  // Toutes les propriétés du widget Stateless doivent être déclarées avec le mot-clé final ou const
  final String name; // propriété de classe habituelle
  MyStatelessWidget(this.name); // constructeur de classe habituel

  @override
  Widget build(BuildContext context) { // il est encore trop tôt pour décrire [context]
    return Text('Hello, $name!');
  }
}
```

Je n'ai rien de plus à ajouter sur les widgets sans état. Ils sont simples.

#### À propos du Hot Reload

Remarquez que une fois que nous avons déplacé le contenu de notre application vers le widget séparé, l'application est re-rendue chaque fois que nous sauvegardons nos modifications. C'est le hot-reload en action.

Il est également crucial de comprendre que pendant que vous travaillez en mode développement avec le hot-reload activé, l'application fonctionnera beaucoup plus lentement qu'en mode release.

#### À propos de GestureDetector

![Image](https://cdn-media-1.freecodecamp.org/images/1*IWxG51RHKS3LskOupmShPA.gif)
_Widget GestureDetector gérant une action de tapotement_

Nous allons créer un StatefulWidget dans la section suivante. Pour nous assurer que ce sera intéressant, nous devons pouvoir changer l'état du widget, n'est-ce pas ? Nous utiliserons [**GestureDetector(…)**](https://docs.flutter.io/flutter/widgets/GestureDetector-class.html) à cette fin. Ce widget ne rendra rien à l'écran mais gère l'interaction de l'utilisateur avec l'écran et appelle les fonctions associées qui lui sont données.

L'exemple ci-dessous crée un bouton bleu au centre de l'écran, et une fois ce bouton pressé, le texte est imprimé dans le terminal :

```dart
import 'package:flutter/widgets.dart';

main() => runApp(
  Directionality(
    textDirection: TextDirection.ltr,
    child: Container(
      color: Color(0xFFFFFFFF),
      child: App(),
    ),
  ),
);

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: GestureDetector( // juste un widget normal
        onTap: () { // une des propriétés de [GestureDetector]
          // Cette fonction sera appelée lorsque le widget enfant est pressé
          print('You pressed me');
        },
        child: Container( // le [Container] représentera notre bouton
          decoration: BoxDecoration( // c'est ainsi que vous stylez le [Container]
            shape: BoxShape.circle, // change sa forme de rectangulaire à circulaire
            color: Color(0xFF17A2B8), // et le peint en bleu
          ),
          width: 80.0,
          height: 80.0,
        ),
      ),
    );
  }
}
```

Appuyez sur le bouton, et le message sera imprimé dans le terminal. Appuyez à nouveau, et le texte apparaîtra à nouveau.

#### À propos des widgets avec état

Les **StatefulWidget** sont simples. Oui, même plus simples que les **StatelessWidget** ! Cependant, il y a une nuance. Ils n'existent pas par eux-mêmes. Ils nécessitent une classe supplémentaire pour stocker l'état du widget. De plus, la partie visuelle du widget devient son état.

Voici un exemple de la classe **StatefulWidget** :

```dart
// …

class Counter extends StatefulWidget {
  // L'état est stocké non pas dans le widget, mais dans la classe spécifique
  // qui est créée par createState()
  @override
  State<Counter> createState() => _CounterState();
  // Le résultat de la fonction est un objet, qui doit être
  // de type State<Counter> (où Counter est le nom de notre widget)
}
```

Nous avons créé un widget "vide" qui implémente seulement une méthode et ne contient pas d'état ou de représentation UI. En forçant une telle séparation, Flutter cherche une plus grande optimisation de l'application.

L'objet d'état n'est pas non plus compliqué. En effet, il est tout comme notre **StatelessWidget**. La principale différence est sa classe parente.

```dart
// …

class _CounterState extends State<Counter> {
  // Enfin, nous pouvons déclarer des variables dynamiques à l'intérieur de nos classes,
  // pour stocker l'état de nos widgets
  
  // Dans ce cas, nous allons stocker le nombre
  int counter = 0;

  // Le reste est super simple, nous implémentons simplement la méthode build() familière,
  // de la même manière que nous l'avons fait pour notre [StatelessWidget]
  @override
  Widget build(BuildContext context) {
    // Presque rien n'a changé depuis le dernier exemple.
    // J'ai ajouté des commentaires pour mettre en évidence la différence
    return Center(
      child: GestureDetector(
        onTap: () {
          // Une fois le bouton tapé, nous augmentons la valeur de la variable [counter]
          setState(() {
            // L'utilisation de setState() est nécessaire pour déclencher les hooks de cycle de vie
            // afin que le widget sache qu'il doit être mis à jour
            ++counter;
          });
        },
        child: Container(
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            color: Color(0xFF17A2B8),
          ),
          width: 80.0,
          child: Center(
            child: Text( // ici nous imprimons la valeur de [counter]
              '$counter', // pour voir comment elle change
              style: TextStyle(fontSize: 30.0),
            ),
          ),
        ),
      ),
    );
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*pRD3U_zDnuLmcmNZ-1spGA.gif)
_Application de compteur construite en utilisant des widgets Flutter primitifs_

J'ai nommé notre classe d'état en commençant par un underscore. Dans le langage Dart, tous les noms qui commencent par un underscore sont privés (contrairement à JavaScript ou Python, ils sont vraiment indisponibles en dehors de la bibliothèque). Habituellement, nous n'avons pas besoin d'exposer nos classes d'état en dehors de la bibliothèque, il est donc bon de les garder privées.

Nous avons construit une application aussi merveilleuse. Excellent résultat !

Avant de terminer cette partie, jetons un coup d'œil à quelques widgets intéressants. Cette fois, nous allons écrire plus de code à la fois, et je n'expliquerai pas chaque ligne. Vous pouvez probablement déjà comprendre la plupart du code :

```dart
import 'package:flutter/widgets.dart';

main() => runApp(App());

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.ltr,
      child: Container(
        padding: EdgeInsets.symmetric(
          vertical: 60.0,
          horizontal: 80.0,
        ),
        color: Color(0xFFFFFFFF),
        child: Content(),
      ),
    );
  }
}

class Content extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Counter('Manchester United'),
        Counter('Juventus'),
      ],
    );
  }
}

class Counter extends StatefulWidget {
  final String _name;
  Counter(this._name);

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int count = 0;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(bottom: 10.0),
      padding: EdgeInsets.all(4.0),
      decoration: BoxDecoration(
        border: Border.all(color: Color(0xFFFD6A02)),
        borderRadius: BorderRadius.circular(4.0),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          // [widget] est la propriété de la classe State qui stocke
          // l'instance du [StatefulWidget] ([Counter] dans notre cas)
          _CounterLabel(widget._name),
          _CounterButton(
            count,
            onPressed: () {
              setState(() {
                ++count;
              });
            },
          ),
        ],
      ),
    );
  }
}

class _CounterLabel extends StatelessWidget {
  static const textStyle = TextStyle(
    color: Color(0xFF000000),
    fontSize: 26.0,
  );

  final String _label;
  _CounterLabel(this._label);

  @override
  Widget build(BuildContext context) {
    return Text(
      _label,
      style: _CounterLabel.textStyle,
    );
  }
}

class _CounterButton extends StatelessWidget {
  final count;
  final onPressed;
  _CounterButton(this.count, {@required this.onPressed});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onPressed,
      child: Container(
        padding: EdgeInsets.symmetric(horizontal: 6.0),
        decoration: BoxDecoration(
          color: Color(0xFFFD6A02),
          borderRadius: BorderRadius.circular(4.0),
        ),
        child: Center(
          child: Text(
            '$count',
            style: TextStyle(fontSize: 20.0),
          ),
        ),
      ),
    );
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AHC5cs2E2uLXDqeORwzpEw.png)
_Utilisation de la composition de widgets pour l'application de compteur_

Nous avons donc utilisé deux nouveaux widgets : [**Column()**](https://docs.flutter.io/flutter/widgets/Column-class.html) et [**Row()**](https://docs.flutter.io/flutter/widgets/Row-class.html). Il n'est pas difficile de deviner leur but.

Dans le prochain article, nous les examinerons plus précisément. Nous apprendrons également comment assembler plusieurs widgets et créer une application sexy en utilisant la bibliothèque Material de Flutter.

#### Ressources supplémentaires

Si vous souhaitez en savoir plus sur les sujets mentionnés, voici une liste de liens intéressants :

* [https://flutter.io/docs/get-started/flutter-for/web-devs](https://flutter.io/docs/get-started/flutter-for/web-devs)
* Codage en utilisant [VS Code](https://flutter.io/docs/development/tools/ide/vs-code) et [IntelliJ](https://flutter.io/docs/development/tools/ide/android-studio)
* [Plus de détails sur les widgets](https://flutter.io/docs/development/ui/widgets-intro)
* Il est également important de lire sur le [Hot reload](https://flutter.io/docs/development/tools/hot-reload) pour comprendre quand et pourquoi votre application peut ne pas être mise à jour automatiquement.