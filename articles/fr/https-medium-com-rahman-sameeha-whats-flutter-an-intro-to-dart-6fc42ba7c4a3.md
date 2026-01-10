---
title: Une introduction simplifiée à Dart et Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T22:41:46.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-rahman-sameeha-whats-flutter-an-intro-to-dart-6fc42ba7c4a3
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca4bf740569d1a4ca64ae.jpg
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
seo_title: Une introduction simplifiée à Dart et Flutter
seo_desc: 'By Sameeha Rahman

  A bit of background

  It all began in 2011: Xamarin, now a Microsoft-owned company, came up with a solution
  for hybrid mobile apps through its signature product, Xamarin SDK with C#. And thus
  began the revolution of hybrid mobile appl...'
---

Par Sameeha Rahman

#### Un peu de contexte

Tout a commencé en 2011 : Xamarin, maintenant une entreprise appartenant à Microsoft, a proposé une solution pour les applications mobiles hybrides grâce à son produit phare, Xamarin SDK avec C#. Et ainsi a commencé la révolution des applications mobiles hybrides, facilitant l'écriture d'une base de code unique pour plusieurs plateformes.

Ionic a émergé en 2013 avec sa première version par Drifty Co. Ionic a aidé les développeurs web à utiliser leurs compétences existantes dans l'industrie croissante des applications mobiles. En 2015, Facebook a utilisé React.js pour le réinventer pour les développeurs d'applications mobiles. Ils nous ont donné React Native, une base de code entièrement JavaScript reposant sur les SDK natifs.

Et ceux-ci ne sont pas les seuls, mais quelques-uns des nombreux frameworks mobiles hybrides. Plus d'informations peuvent être trouvées [ici](https://blog.jscrambler.com/10-frameworks-for-mobile-hybrid-apps/).

Maintenant, nous pouvons voir le tour de Google de mettre ses doigts dans la tarte avec Flutter.

![Image](https://cdn-media-1.freecodecamp.org/images/MiAWLAfns7pPgptcHFFPe8UAwMhPTPp3WWgt)

### Qu'est-ce que Dart ?

Google a sorti sa première version de Flutter 1.0 en décembre dernier, après l'avoir eu en mode bêta pendant plus de 18 mois. Dart est le langage de programmation utilisé pour coder les applications Flutter. Dart est un autre produit de Google et a sorti la version 2.1, avant Flutter, en novembre. Comme il commence, la communauté Flutter n'est pas aussi étendue que ReactNative, Ionic ou Xamarin.

Il y a quelque temps, j'ai découvert un penchant pour JavaScript. J'étais ravie de travailler sur une application mobile ReactNative pour mon stage. J'aime aussi coder des applications mobiles hybrides, donc je voulais essayer Flutter, comme je l'avais fait avec Xamarin il y a quelque temps.

À mon premier regard sur Flutter (et Dart), je me sentais perplexe et ne semblais rien comprendre. Ils avaient même une section dans leur documentation pour les développeurs passant de React Native. Donc, je me suis mise à creuser plus profondément sur tout ce qui concerne Dart.

Dart ressemble un peu à C et est un langage de programmation orienté objet. Donc, si vous préférez les langages C ou Java, Dart est fait pour vous, et vous serez probablement compétent en lui.

Dart n'est pas seulement utilisé pour le développement d'applications mobiles mais est un langage de programmation. Approuvé comme standard par Ecma (ECMA-408), il est utilisé pour construire à peu près tout sur le web, les serveurs, le bureau et bien sûr, les applications mobiles (Oui, les mêmes personnes qui ont standardisé nos préférés ES5 et ES6.)

Dart, lorsqu'il est utilisé dans les applications web, est transpilé en JavaScript pour qu'il s'exécute sur tous les navigateurs web. L'installation de Dart comprend également une VM pour exécuter les fichiers .dart à partir d'une interface de ligne de commande. Les fichiers Dart utilisés dans les applications Flutter sont compilés et empaquetés dans un fichier binaire (.apk ou .ipa) et téléchargés sur les magasins d'applications.

### À quoi ressemble la programmation en Dart ?

Comme la plupart des langages ALGOL (comme C# ou Java) :

1. Le point d'entrée d'une classe Dart est la méthode `main()`. Cette méthode sert également de point de départ pour les applications Flutter.
2. La valeur par défaut de la plupart des types de données est `null`.
3. Les classes Dart ne supportent que l'héritage simple. Il ne peut y avoir qu'une seule superclasse pour une classe particulière, mais elle peut avoir de nombreuses implémentations d'interfaces.
4. Le contrôle de flux de certaines instructions, comme les conditions if, les boucles (for, while et do-while), les instructions switch-case, break et continue sont les mêmes.
5. L'abstraction fonctionne de manière similaire, permettant les classes abstraites et les interfaces.

Contrairement à eux (et parfois un peu comme JavaScript) :

1. Dart a l'inférence de type. Le type de données d'une variable n'a pas besoin d'être explicitement déclaré, car Dart "inférera" ce qu'il est. En Java, une variable doit avoir son type explicitement donné lors de la déclaration. Par exemple, `String something;`. Mais en Dart, le mot-clé est utilisé comme suit, `var something;`. Le code traite la variable selon ce qu'elle contient, qu'il s'agisse d'un nombre, d'une chaîne, d'un booléen ou d'un objet.
2. Tous les types de données sont des objets, y compris les nombres. Donc, s'ils sont laissés non initialisés, leur valeur par défaut n'est pas 0 mais est plutôt null.
3. Un type de retour d'une méthode n'est pas requis dans la signature de la méthode.
4. Le type `num` déclare tout élément numérique, à la fois réel et entier.
5. L'appel de la méthode `super()` n'est qu'à la fin du constructeur d'une sous-classe.
6. Le mot-clé `new` utilisé avant le constructeur pour la création d'objets est facultatif.
7. Les signatures de méthode peuvent inclure une valeur par défaut pour les paramètres passés. Donc, si l'un n'est pas inclus dans l'appel de la méthode, la méthode utilise les valeurs par défaut à la place.
8. Il a un nouveau type de données intégré appelé Runes, qui traite les points de code UTF-32 dans une chaîne. Pour un exemple simple, voir les emojis et les icônes similaires.

Et toutes ces différences ne sont que quelques-unes parmi les nombreuses que vous pouvez trouver dans le tour du langage Dart, que vous pouvez consulter [ici](https://www.dartlang.org/guides/language/language-tour).

Dart a également des bibliothèques intégrées installées dans le SDK Dart, les plus couramment utilisées étant :

1. dart:core pour la fonctionnalité de base ; elle est importée dans tous les fichiers dart.
2. dart:async pour la programmation asynchrone.
3. dart:math pour les fonctions et constantes mathématiques.
4. dart:convert pour la conversion entre différentes représentations de données, comme JSON en UTF-8.

Vous pouvez trouver plus d'informations sur les bibliothèques Dart [ici](https://www.dartlang.org/guides/libraries/library-tour).

### Utilisation de Dart dans Flutter

Flutter a plus de bibliothèques spécifiques aux applications, plus souvent sur les éléments d'interface utilisateur comme :

1. Widget : éléments communs des applications, comme Text ou ListView.
2. Material : contenant des éléments suivant le design Material, comme FloatingActionButton.
3. Cupertino : contenant des éléments suivant les designs iOS actuels, comme CupertinoButton.

Vous pouvez trouver des bibliothèques spécifiques à Flutter [ici](https://docs.flutter.io/flutter/animation/animation-library.html).

### Installation de Flutter

Donc, pour mettre cela en marche, suivez la [documentation Flutter](https://flutter.io/docs/get-started/install). Elle donne des détails sur l'installation du SDK Flutter et la configuration de votre IDE préféré ; le mien serait VS code. La configuration de VS code avec l'extension Flutter est utile. Elle vient avec des commandes intégrées, par opposition à l'utilisation du terminal.

Suivez à nouveau les docs pour créer votre première application. Dans mon cas, exécutez la commande d'extension Flutter : Nouveau Projet. Ensuite, tapez le nom du projet et choisissez le dossier de destination.

Si vous préférez utiliser le terminal, déplacez-vous vers le dossier de destination de l'application. Ensuite, utilisez la commande `flutter create <nom_de_l_app>` pour créer le dossier de l'application. Cela génère l'ensemble du dossier de l'application, y compris les dossiers de projet Android et iOS. Pour ouvrir ces dossiers, utilisez Android Studio et XCode, pour construire l'application.

À la racine du projet, vous trouvez `pubspec.yaml`. Ce fichier contient les dépendances de l'application. Cela inclut à la fois les bibliothèques/modules externes et les actifs comme les images et les fichiers de configuration. Il fonctionne comme un `package.json`, contenant tous les modules externes de l'application. Pour installer ces packages, entrez le nom du package et la version sous la section `dependencies:` du `pubspec.yaml`. Exécutez la commande `flutter packages get`. Incluez les actifs de l'application à l'intérieur de la section `flutter:` du même fichier.

Le point d'entrée de l'application est `main.dart`, trouvé à l'intérieur du dossier lib. Ce dossier contient également toutes les classes Dart (pages de l'application ou composants réutilisables). Lors de la création de l'application, le fichier `main.dart` contient un code pré-écrit simple. Avant d'exécuter ce code, un appareil est soit connecté au PC, avec le débogage USB activé. Ensuite, exécutez la commande flutter run sur le terminal.

### Un premier regard sur l'application Flutter

L'application ressemble actuellement à ceci maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/G4pmMIBnRS2wy75f6zHCoq5OyD-lkSbO7Dsx)

La construction de l'interface utilisateur d'une application Flutter utilise des Widgets.

Les Widgets fonctionnent de manière similaire à React. Un widget utilise différents composants pour décrire à quoi doit ressembler l'UI. Ils peuvent être soit Stateful ou Stateless. Dans les composants Stateful, le widget se reconstruit en raison des changements d'état, pour accommoder le nouvel état.

Lorsque nous regardons le code actuel pour la page d'accueil, nous voyons qu'il s'agit d'une page Stateful. Si la variable counter augmente, le framework essaie de trouver le moyen le moins coûteux de réafficher la page. Dans ce cas, trouver la différence minimale entre la description actuelle du widget et la future. Il prend en compte l'état changé.

![Image](https://cdn-media-1.freecodecamp.org/images/b7P-4CeJ4Si40a4Npx4cHsRnCL4-0CJNCp29)

La classe Scaffold est une structure de mise en page de design material et est le conteneur principal pour la page d'accueil. L'AppBar, également un élément de design material, est la barre de titre trouvée en haut de la page. Tous les autres composants, comme le bouton flottant et les deux balises de texte, tombent sous le corps de la page. La classe Center est une classe de mise en page qui centre ses composants enfants verticalement et horizontalement.

La classe Column, un autre widget de mise en page, liste chaque élément enfant verticalement. Chacun de ses éléments enfants est ajouté à un tableau et mis sous la section children:.

Les deux textes parlent d'eux-mêmes. Le premier affiche le texte 'Vous avez poussé.' Le second affiche la valeur actuelle dans la variable `_counter`.

Le FloatingActionButton fait partie des widgets de design Material. Il affiche une icône + et déclenche l'incrément de la variable `_counter`.

### Rechargement à chaud

Un autre point positif de l'utilisation de Flutter est la fonction de rechargement à chaud. Elle vous permet de voir les modifications apportées au code en temps réel, sans redémarrer le processus de construction. Tapez 'r' sur la même console où vous avez exécuté la commande `flutter run`.

![Image](https://cdn-media-1.freecodecamp.org/images/Fx8T01uSSqXqQoPwcK4qjpoHEEgXslUBXmyg)

### Modification du code actuel

Comme nous pouvons le voir, lorsque vous cliquez sur le bouton, la valeur de la variable _counter augmente. Cela réaffiche la page et la nouvelle valeur est affichée sur le corps de la page.

Je vais changer cela un peu. Pour chaque clic sur le bouton, nous afficherons un composant Card personnalisé avec le numéro de l'élément.

#### Création du composant Card personnalisé

Donc, pour commencer, nous créons un nouveau fichier .dart à l'intérieur du dossier lib. J'ai créé le mien dans un sous-dossier `commonComponents` et l'ai nommé `customCard.dart`.

```dart
import 'package:flutter/material.dart';

class CustomCard extends StatelessWidget {  CustomCard({@required this.index});
	final index;
    
    @override  
    Widget build(BuildContext context) {    
    	return Card(      
        	child: Column(        
            	children: <Widget>[Text('Card $index')],      
            )    
        );  
    }
}
```

Ce composant sera un widget sans état et n'affichera que la valeur que nous lui envoyons, dans le widget Text.

#### Affichage d'une liste de cartes personnalisées

Importez le composant ci-dessus dans le `main.dart` comme suit :

```dart
import 'commonComponents/customCard.dart';
```

J'ai ensuite remplacé le code du corps de la page d'accueil, de celui ci-dessus par celui-ci :

```dart
body: Center(  
	child: Container(    
    	child: ListView.builder(      
        	itemCount: _counter,      
            itemBuilder: (context, int index) {        
            	return CustomCard(          
                	index: ++index,        
                );      
            },    
        )  
    ),
),
```

![Image](https://cdn-media-1.freecodecamp.org/images/zUmlhYuKaGz-WF4S1opD9t-EyDYBRIeEbUtD)

Il affiche maintenant une liste d'éléments `CustomCard`, jusqu'au nombre de fois où le bouton est cliqué. Le `itemCount` est utilisé pour définir le nombre d'éléments que le `ListView` doit afficher. Le `itemBuilder` retourne l'élément réel qui est affiché.

Et c'est un exemple simple de l'utilisation de Flutter.

### En conclusion...

Avant que mon intérêt ne se tourne vers JavaScript, je travaillais avec Java. Si j'avais rencontré Dart à cette époque, j'aurais peut-être pu le comprendre plus facilement que maintenant. Dans l'ensemble, ce n'était pas trop difficile mais cela a pris un peu de temps pour s'y habituer. Je pourrais me voir l'utiliser avec le temps.

Trouvez le dépôt de code, [ici](https://github.com/samsam-026/flutter-example).

Trouvez le commit pour ce post, [ici](https://github.com/samsam-026/flutter-example/commit/683ffb2ccc13571cee9471d7e2c3455d8ce9ce8f).