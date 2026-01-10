---
title: Comment créer des interfaces utilisateur réactives dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-10-28T18:17:34.078Z'
originalURL: https://freecodecamp.org/news/how-to-build-responsive-uis-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761675310940/332589a7-55e0-4cb2-935e-aa1011709e2e.png
tags:
- name: Flutter
  slug: flutter
- name: UI Design
  slug: ui-design
- name: User Interface
  slug: user-interface
seo_title: Comment créer des interfaces utilisateur réactives dans Flutter
seo_desc: Building responsive UIs in Flutter can be challenging, especially when you
  want your app to look great on phones, tablets, and desktops without maintaining
  multiple layouts. Fortunately, Flutter provides powerful tools like MediaQuery,
  LayoutBuilder,...
---

Créer des interfaces utilisateur (UI) réactives dans Flutter peut s'avérer difficile, surtout lorsque vous voulez que votre application soit élégante sur téléphones, tablettes et ordinateurs sans avoir à maintenir plusieurs mises en page. Heureusement, Flutter fournit des outils puissants comme `MediaQuery`, `LayoutBuilder` et le package `flutter_screenutil` pour rendre ce processus fluide.

Dans cet article, nous allons parcourir un exemple complet d'écran réactif, en expliquant chaque partie du code étape par étape. Vous apprendrez non seulement comment adapter votre mise en page aux différentes tailles d'écran et orientations, mais aussi comment utiliser des utilitaires de mise à l'échelle pour maintenir la cohérence de votre texte et de vos espacements sur tous les appareils.

À la fin, vous comprendrez comment structurer une application Flutter qui ajuste automatiquement sa mise en page et sa typographie en fonction de l'espace disponible à l'écran, une compétence indispensable pour tout développeur ciblant plusieurs plateformes.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Comprendre le design réactif (Responsive) vs adaptatif (Adaptive)](#heading-comprendre-le-design-reactif-vs-adaptatif)
    
* [Widgets de mise en page Flutter essentiels pour une UI réactive](#heading-widgets-de-mise-en-page-flutter-essentiels-pour-une-ui-reactive)
    
    * [Container/SizedBox](#heading-containersizedbox)
        
    * [Dimensionnement trop fixe (non réactif)](#heading-dimensionnement-trop-fixe-non-reactif)
        
    * [Dimensionnement réactif / flexible](#heading-dimensionnement-reactif-flexible)
        
    * [SizedBox pour l'espacement ou les contraintes](#heading-sizedbox-pour-lespacement-ou-les-contraintes)
        
    * [Row, Column](#heading-row-column)
        
    * [Expanded et Flexible](#heading-expanded-et-flexible)
        
    * [LayoutBuilder](#heading-layoutbuilder)
        
* [MediaQuery et informations sur l'écran](#heading-mediaquery-et-informations-sur-lecran)
    
    * [Points d'arrêt, orientation et adaptation aux grands écrans](#heading-points-darret-orientation-et-adaptation-aux-grands-ecrans)
        
    * [Typographie, images et assets réactifs](#heading-typographie-images-et-assets-reactifs)
        
    * [Mises en page flexibles : Expanded, Flexible, FractionallySizedBox](#heading-mises-en-page-flexibles-expanded-flexible-fractionallysizedbox)
        
    * [Outils et packages avancés](#heading-outils-et-packages-avances)
        
    * [Gestion des zones de sécurité (Safe Areas), des encoches et des marges (Insets)](#heading-gestion-des-safe-areas-des-encoches-et-des-insets)
        
    * [UI adaptative pour tablettes/ordinateurs et multi-fenêtres](#heading-ui-adaptative-pour-tablettes-ordinateurs-et-multi-fenetres)
        
* [Bonnes pratiques et considérations de performance](#heading-bonnes-pratiques-et-considerations-de-performance)
    
* [Test et débogage de mises en page réactives](#heading-test-et-debogage-de-mises-en-page-reactives)
    
* [Création de widgets réactifs réutilisables / widgets personnalisés](#heading-creation-de-widgets-reactifs-reutilisables-widgets-personnalises)
    
* [Exemple d'un écran réactif complet](#heading-exemple-dun-ecran-reactif-complet)
    
    * [Configuration du projet et importations](#heading-configuration-du-projet-et-importations)
        
    * [Point d'entrée de l'application : la classe MyApp](#heading-point-dentree-de-lapplication-la-classe-myapp)
        
    * [L'écran d'accueil réactif (MyHomePage)](#heading-lecran-daccueil-reactif-myhomepage)
        
    * [Construction du contenu principal](#heading-construction-du-contenu-principal)
        
* [Guide complet : explication approfondie du code](#heading-guide-complet-explication-approfondie-du-code)
    
    * [Importations et point d'entrée de l'application](#heading-importations-et-point-dentree-de-lapplication)
        
    * [Racine de l'application : le widget MyApp](#heading-racine-de-lapplication-le-widget-myapp)
        
    * [La mise en page de l'écran d'accueil MyHomePage](#heading-la-mise-en-page-de-lecran-daccueil-myhomepage)
        
    * [Le Scaffold et l'AppBar](#heading-le-scaffold-et-lappbar)
        
    * [SafeArea + LayoutBuilder](#heading-safearea-layoutbuilder)
        
    * [Gestion des petits et grands écrans](#heading-gestion-des-petits-et-grands-ecrans)
        
    * [Construction du contenu principal](#heading-construction-du-contenu-principal-1)
        
    * [Pourquoi cela fonctionne](#heading-pourquoi-cela-fonctionne)
        
* [Points clés à retenir](#heading-points-cles-a-retenir)
    
* [Conclusion](#heading-conclusion)
    
* [Références](#heading-references)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir :

* Un environnement Flutter fonctionnel (SDK, IDE, émulateur ou appareil).
    
* Une maîtrise de base de Flutter : connaissance des widgets, stateless/stateful, Row/Column, Scaffold, etc.
    
* Une familiarité avec les bases de Dart et le fonctionnement de la mise en page dans Flutter (contraintes, dimensionnement).
    
* (Optionnel mais utile) Un design/maquette (par exemple de Figma) avec une taille de conception définie ou un écran cible.
    
* La compréhension que la création d'interfaces utilisateur véritablement adaptatives/réactives signifie s'adapter aux **différentes tailles d'écran**, **orientations**, **ratios d'aspect** et **plateformes** (mobile/tablette/web/ordinateur).
    

## Comprendre le design réactif (Responsive) vs adaptatif (Adaptive)

Il est utile de clarifier la terminologie :

* Le **design réactif (Responsive)** consiste à *ajuster* l'interface utilisateur à l'espace disponible : la mise en page se redimensionne, se réorganise et se reformate à mesure que la taille de l'écran ou l'orientation change.
    
* Le **design adaptatif (Adaptive)** consiste à sélectionner différents modèles d'interface utilisateur en fonction de l'appareil/écran. Par exemple, utiliser un panneau latéral sur ordinateur et une navigation inférieure sur mobile. L'interface s'adapte au contexte d'utilisation.
    
* En pratique avec Flutter, on fait souvent les *deux* : réactif (mise à l'échelle/reformatage) et adaptatif (choix de variantes de mise en page).
    
* Selon la documentation officielle :
    
    > « Le design réactif consiste à adapter l'interface utilisateur à l'espace. Le design adaptatif consiste à rendre l'interface utilisateur utilisable dans l'espace. » ([Docs Flutter](https://docs.flutter.dev/ui/adaptive-responsive))
    
* Quelques bonnes pratiques à suivre : ne présumez pas du type d'appareil (téléphone/tablette) en fonction de la taille de l'écran, ne verrouillez pas l'orientation et ne vous fiez pas uniquement à `MediaQuery.orientation`. ([Docs Flutter](https://docs.flutter.dev/ui/adaptive-responsive/best-practices))
    

## Widgets de mise en page Flutter essentiels pour une UI réactive

Flutter fournit de nombreux widgets fondamentaux pour la mise en page – lorsqu'ils sont bien utilisés, ils constituent l'épine dorsale des interfaces utilisateur réactives.

1. ### Container/SizedBox
    

`Container` et `SizedBox` vous permettent de dimensionner les widgets explicitement ou via des contraintes.

À utiliser avec précaution : des tailles trop fixes peuvent entraver la réactivité (par exemple, un Container(width: 300) peut déborder sur les petits écrans).

Il est préférable d'utiliser un dimensionnement relatif ou de permettre la flexibilité.

Voici des exemples de code Flutter clairs et pratiques qui illustrent **comment utiliser** `Container` et `SizedBox`, incluant les approches de dimensionnement **mauvaises (fixes)** et **bonnes (réactives/flexibles)** :

### Dimensionnement trop fixe (non réactif)

```dart
class FixedContainerExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        // Cela pourrait déborder sur les petits écrans !
        child: Container(
          width: 300,
          height: 200,
          color: Colors.blue,
          child: const Center(
            child: Text(
              'Conteneur à taille fixe',
              style: TextStyle(color: Colors.white),
            ),
          ),
        ),
      ),
    );
  }
}
```

**Problème :**  
Si la largeur de l'écran est inférieure à 300px (comme sur certains petits appareils mobiles), ce widget risque de déborder ou d'être coupé.

### Dimensionnement réactif / flexible

```dart
class ResponsiveContainerExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final screenWidth = MediaQuery.of(context).size.width;

    return Scaffold(
      body: Center(
        // Utilisation d'une largeur et hauteur relatives
        child: Container(
          width: screenWidth * 0.8, // 80% de la largeur de l'écran
          height: 200,
          decoration: BoxDecoration(
            color: Colors.blue,
            borderRadius: BorderRadius.circular(12),
          ),
          child: const Center(
            child: Text(
              'Conteneur réactif (80% de largeur)',
              style: TextStyle(color: Colors.white),
            ),
          ),
        ),
      ),
    );
  }
}
```

**Pourquoi c'est mieux :**  
Il s'ajuste automatiquement aux différentes tailles d'écran.

### SizedBox pour l'espacement ou les contraintes

```dart
class SizedBoxExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text('Au-dessus de l\'espaceur'),
            const SizedBox(height: 16), // Ajoute de l'espacement
            Container(
              width: 200,
              height: 100,
              color: Colors.green,
              child: const Center(child: Text('Conteneur dimensionné')),
            ),
          ],
        ),
      ),
    );
  }
}
```

  
`SizedBox` est léger et idéal pour ajouter un **espacement fixe** ou définir des **dimensions simples** sans avoir besoin d'un `Container` complet.

2. ### Row, Column
    

`Row` et `Column` organisent les enfants horizontalement ou verticalement.

**Note** : `Row` donne un espace horizontal infini (soumis aux contraintes du parent), les enfants doivent donc gérer leur dimensionnement sous peine de débordement.

Lorsque vous utilisez un **Row** ou une **Column**, Flutter essaie de leur donner autant d'espace que possible **le long de leur axe principal** (horizontal pour Row, vertical for Column).  
Si les enfants à l'intérieur ne savent pas quel espace occuper, **ils peuvent déborder** ou ne pas s'afficher comme prévu.

C'est pourquoi nous utilisons `Expanded`, `Flexible` ou `SizedBox` pour indiquer à Flutter **comment chaque enfant doit utiliser l'espace disponible**.

Exemple :

```dart
Row(
  children: [
    Expanded(
      child: Container(
        // Le contenu de votre widget ici
      ),
    ),
    // Autres widgets...
  ],
)
```

Ici, `Expanded` dit : « occupe l'espace restant proportionnellement ».

### Expanded et Flexible

`Expanded` force son enfant à remplir l'espace restant dans une `Row` ou une `Column`.

`Flexible` donne de la flexibilité à son enfant : il peut rétrécir ou s'agrandir mais ne remplit pas l'espace de force.

Exemple :

```dart
Row(
  children: [
    Flexible(
      child: Container(
        // Contenu du widget
      ),
    ),
    // Autres widgets...
  ],
)
```

L'utilisation de `Flexible`/`Expanded` aide à distribuer l'espace de manière dynamique et à s'adapter naturellement aux tailles d'écran variables.

3. ### LayoutBuilder
    

`LayoutBuilder` vous donne les contraintes du widget parent (`maxWidth`, `maxHeight`) et vous permet de reconstruire l'interface utilisateur en conséquence.

```dart
LayoutBuilder(
  builder: (BuildContext context, BoxConstraints constraints) {
    if (constraints.maxWidth > 600) {
      // Mise en page pour grand écran
      return LargeScreenWidget();
    } else {
      // Mise en page pour petit écran
      return SmallScreenWidget();
    }
  },
)
```

C'est souvent plus fiable que de simplement vérifier `MediaQuery.orientation` ou `MediaQuery.size`, en particulier sur les appareils multi-fenêtres ou pliables. ([Docs Flutter](https://docs.flutter.dev/ui/adaptive-responsive/best-practices?utm_source=chatgpt.com))

4. #### FractionallySizedBox et AspectRatio
    

`FractionallySizedBox` : Dimensionne son enfant comme une fraction de la taille du parent (par exemple, `widthFactor: 0.5`).

`AspectRatio` : Maintient un ratio d'aspect fixe (largeur/hauteur), utile pour les images ou les conteneurs.

```dart
AspectRatio(
  aspectRatio: 16 / 9,
  child: YourWidget(),
)
```

Ces outils aident à maintenir des mises en page proportionnellement cohérentes sur toutes les tailles d'écran.

## MediaQuery et informations sur l'écran

Comprendre la taille de l'écran, l'orientation, le padding, le ratio de pixels de l'appareil, etc., est essentiel.

#### Utilisation de MediaQuery

```dart
double screenWidth  = MediaQuery.of(context).size.width;
double screenHeight = MediaQuery.of(context).size.height;
Orientation orientation = MediaQuery.of(context).orientation;
double devicePixelRatio = MediaQuery.of(context).devicePixelRatio;
EdgeInsets padding = MediaQuery.of(context).padding;
```

`size` donne la largeur/hauteur en pixels logiques, `orientation` indique si l'appareil est en portrait ou paysage, `devicePixelRatio` montre combien de pixels physiques par pixel logique (utile pour la mise à l'échelle des images), et `padding` donne les insets de l'interface système (encoches, barre d'état, barre de navigation).

Utilisez ces valeurs pour personnaliser votre interface utilisateur : par exemple, ajuster la taille des polices, la largeur des conteneurs ou les décisions de mise en page.

#### Exemple : Typographie réactive

```dart
Text(
  'Votre texte ici',
  style: TextStyle(
    fontSize: screenWidth * 0.04, // 4% de la largeur de l'écran
  ),
)
```

Approche : Calculer la taille de la police par rapport à la largeur ou à la hauteur de l'écran. Mais soyez prudent, la lisibilité du texte et l'accessibilité (par exemple, les changements de taille de police du système) doivent être pris en compte, voir les bonnes pratiques ci-dessous.

### Points d'arrêt, orientation et adaptation aux grands écrans

Pour créer des interfaces utilisateur qui sont aussi belles sur tablettes/ordinateurs que sur téléphones :

#### Orientation

```dart
if (MediaQuery.of(context).orientation == Orientation.portrait) {
  // Mise en page portrait
} else {
  // Mise en page paysage
}
```

Fonctionne pour les cas de base, mais attention : l'orientation seule ne capture pas la taille de la fenêtre (surtout dans les environnements de bureau ou multi-fenêtres), préférez vérifier les contraintes ou la taille. ([Docs Flutter](https://docs.flutter.dev/ui/adaptive-responsive/best-practices?utm_source=chatgpt.com))

#### Points d'arrêt et mises en page adaptatives

Définissez des points d'arrêt personnalisés basés sur la largeur (ou d'autres mesures) pour déclencher différentes mises en page.

Exemple :

```dart
if (screenWidth > 600) {
  // UI pour tablette/grand écran
} else {
  // UI pour téléphone
}
```

Certaines sources proposent des points d'arrêt standard, par exemple, compact (<600), moyen (600-840), large (>840). Avec `LayoutBuilder`, vous pouvez détecter la largeur des contraintes parentales au lieu de la largeur globale de l'écran, ce qui est plus robuste.

#### Grands écrans et utilisation sûre de l'espace

Sur des écrans très larges, remplir toute la largeur peut nuire à la lisibilité. La documentation officielle de Flutter recommande de limiter la largeur du contenu (par exemple, en utilisant `ConstrainedBox` + `Center`) pour les grands écrans afin que les lignes de texte ne soient pas excessivement longues. ([Docs Flutter](https://docs.flutter.dev/ui/adaptive-responsive/best-practices?utm_source=chatgpt.com))

Exemple :

```dart
Center(
  child: ConstrainedBox(
    constraints: BoxConstraints(maxWidth: 800),
    child: YourContent(),
  ),
)
```

### Typographie, images et assets réactifs

#### Typographie

Utilisez des unités évolutives autant que possible (voir les packages plus loin). Enveloppez le texte dans `Flexible`/`Expanded` s'il est à l'intérieur d'une `Row`/`Column` pour éviter les débordements, et tenez compte du facteur d'échelle de la police système : vous pouvez utiliser `MediaQuery.of(context).textScaleFactor` pour adapter les polices pour l'accessibilité.

#### Images et BoxFit

```dart
Image.asset(
  'assets/votre_image.png',
  fit: BoxFit.cover,  // ou BoxFit.contain, BoxFit.fitWidth etc.
  width: someWidth,   // largeur réactive
  height: someHeight, // hauteur réactive
)
```

`BoxFit.cover` permet à l'image de remplir le conteneur tout en conservant son ratio d'aspect.

Utilisez `AspectRatio` ou `FractionallySizedBox` pour garder les images proportionnelles.

#### Densité des assets et ratio de pixels

Pour les appareils à haute résolution (`devicePixelRatio` élevé), fournissez des assets de plus haute résolution (2x/3x) pour qu'ils paraissent nets.

Flutter gère automatiquement les variantes d'assets (`asset@2x.png`, etc.), mais dans les mises en page pour très grands écrans, vous pourriez vouloir des détails supplémentaires.

### Mises en page flexibles : Expanded, Flexible, FractionallySizedBox

Nous en avons discuté partiellement plus haut, mais voici des directives plus approfondies.

#### Expanded et Flexible

À utiliser à l'intérieur d'une `Row` ou d'une `Column` pour distribuer l'espace.

Exemple :

```dart
Row(
  children: [
    Expanded(flex: 2, child: Container(color: Colors.red)),
    SizedBox(width: 8),
    Expanded(flex: 1, child: Container(color: Colors.blue)),
  ],
)
```

Le conteneur rouge prend deux fois la largeur du bleu. L'utilisation de `Flexible` permet à son enfant de s'étendre ou de rétrécir, mais ne force pas l'occupation de tout l'espace.

#### FractionallySizedBox

Exemple :

```dart
FractionallySizedBox(
  widthFactor: 0.8,  // 80% de la largeur du parent
  child: SomeWidget(),
)
```

Utile lorsque vous voulez qu'un widget occupe une fraction de l'espace disponible sans utiliser de valeurs de pixels exactes.

#### AspectRatio

```dart
AspectRatio(
  aspectRatio: 16/9,
  child: Container(color: Colors.green),
)
```

Garantit que le conteneur conserve un ratio 16:9 quelle que soit la taille du parent.

### Outils et packages avancés

L'utilisation de packages peut simplifier de nombreuses tâches répétitives. En voici quelques-uns très utilisés.

#### flutter\_screenutil

Aide à mettre à l'échelle les largeurs, hauteurs et tailles de police en fonction d'une taille de conception que vous spécifiez.

Exemple d'initialisation :

```dart
ScreenUtilInit(
  designSize: Size(360, 690), // votre taille de conception de base
  builder: () => MaterialApp(
    home: MyHomePage(),
  ),
);
```

Utilisation :

```dart
width: 200.w,         // largeur mise à l'échelle
height: 150.h,        // hauteur mise à l'échelle
fontSize: 16.sp,      // taille de police mise à l'échelle
radius: 12.r,         // rayon mis à l'échelle
```

Avantages : Mise à l'échelle facile de nombreuses tailles. Mais vous devez utiliser `.w`, `.h`, `.sp`, `.r` de manière cohérente.

#### responsive\_builder

Aide à produire des mises en page pour différents types d'écrans d'appareils (mobile/tablette/ordinateur).

Exemple :

```dart
ResponsiveBuilder(
  builder: (context, sizingInformation) {
    if (sizingInformation.deviceScreenType == DeviceScreenType.mobile) {
      return MobileLayout();
    } else if (sizingInformation.deviceScreenType == DeviceScreenType.tablet) {
      return TabletLayout();
    } else {
      return DesktopLayout();
    }
  },
);
```

Utile pour basculer des arbres de widgets entiers en fonction du type d'appareil. ([Medium](https://medium.com/%40ravipatel84184/mastering-responsive-ui-in-flutter-a-comprehensive-guide-49c4ba9902af?utm_source=chatgpt.com))

#### Autres

1. `responsive_framework`, `adaptive_breakpoints`, etc.
    
2. Lors du choix d'un package, vérifiez la maintenance, la popularité et la compatibilité avec votre version de Flutter.
    

### Gestion des zones de sécurité (Safe Areas), des encoches et des marges (Insets)

Les appareils modernes ont des encoches, des barres d'état, des barres de navigation, des écrans pliables, etc. Utilisez des widgets et des API pour les gérer.

1. Enveloppez le contenu principal dans un `SafeArea` pour éviter les intrusions de l'interface système.
    
2. Utilisez `MediaQuery.of(context).padding` pour détecter le padding de sécurité (haut, bas, gauche, droite).
    

Exemple :

```dart
Padding(
  padding: MediaQuery.of(context).padding,
  child: YourContent(),
)
```

Sur Android, vous pouvez également définir le mode UI :

```dart
SystemChrome.setEnabledSystemUIMode(SystemUiMode.edgeToEdge);
```

et mettre à jour les styles pour que la barre d'état/navigation devienne transparente, ce qui aide pour les interfaces plein écran.

### UI adaptative pour tablettes/ordinateurs et multi-fenêtres

À mesure que votre application s'exécute sur des écrans plus grands ou dans des environnements multi-fenêtres (pliables, ordinateurs, web), considérez :

1. Passer d'une navigation inférieure (mobile) à un rail de navigation ou un panneau latéral (tablette/ordinateur).
    
2. Utiliser `ConstrainedBox` pour limiter la largeur du contenu sur les écrans larges pour la lisibilité.
    
3. Changements de mise en page : au lieu d'un défilement sur une seule colonne, vous pouvez afficher des panneaux côte à côte ou des mises en page en grille.
    
4. Utiliser `LayoutBuilder` ou des packages pour détecter la largeur/contraintes et choisir la mise en page appropriée.
    
5. Éviter la vérification du type d'appareil (par exemple, « si tablette »), basez-vous plutôt sur la taille de la fenêtre.
    
    Exemple :
    
    ```dart
    LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth > 1024) {
          return DesktopScaffold();
        } else if (constraints.maxWidth > 600) {
          return TabletScaffold();
        } else {
          return MobileScaffold();
        }
      },
    );
    ```
    

## Bonnes pratiques et considérations de performance

Résumé des bonnes pratiques clés :

1. **Diviser les widgets en petits widgets réutilisables** améliore la maintenabilité et la réutilisation.
    
2. **Commencer la construction de l'intérieur vers l'extérieur**. Commencez par les plus petits composants et progressez vers l'extérieur, plutôt que d'imposer d'abord des contraintes de conteneur externe.
    
3. **Assurer des contraintes définies** pour éviter les limites infinies et les débordements en utilisant `Expanded`, `Flexible`, etc.
    
4. **Éviter les tailles fixes lorsque c'est inutile**. Le dimensionnement relatif ou les mises en page flexibles s'adaptent mieux.
    
5. **Éviter de se fier uniquement à la taille de l'écran ou à l'orientation**, utilisez des contraintes au lieu de vérifications du type d'appareil.
    
6. **La performance compte**, évitez de trop imbriquer des mises en page lourdes, évitez de reconstruire de grands sous-arbres quand ce n'est pas nécessaire. Utilisez des widgets `const` et gardez la méthode build légère.
    
7. **Accessibilité** : tenez compte de la mise à l'échelle des polices (`MediaQuery.textScaleFactor`), des lecteurs d'écran, de l'entrée clavier/souris sur les écrans plus grands.
    
8. **Tester sur plusieurs tailles d'écran/orientations** : appareils réels/émulateurs/tailles d'affichage.
    
9. **Débordement de police/texte** : enveloppez le texte dans `Flexible`, définissez `overflow`, `softWrap`, et testez pour le contenu dynamique.
    

## Test et débogage de mises en page réactives

1. Utilisez des émulateurs/simulateurs d'appareils avec différentes tailles d'écran (téléphones, tablettes, ordinateurs).
    
2. Pour le web/ordinateur, redimensionnez la fenêtre du navigateur pour voir comment la mise en page s'adapte.
    
3. Utilisez le package `device_preview` ou les outils intégrés de Flutter pour simuler divers appareils.
    
4. Utilisez le **Widget Inspector** et le **Layout Explorer** des Flutter DevTools pour comprendre comment les widgets sont dimensionnés et disposés.
    
5. Testez les changements d'orientation, le multi-fenêtres, la vue fractionnée (par exemple, les pliables Android).
    
6. Vérifiez les erreurs de débordement (rayures jaunes/noires) ou les comportements de défilement inattendus.
    
7. Vérifiez l'accessibilité : augmentez/diminuez la taille des polices, testez avec un lecteur d'écran, vérifiez la navigation au clavier en mode bureau.
    

## Création de widgets réactifs réutilisables / widgets personnalisés

L'une des clés d'une UI réactive évolutive est de créer des widgets réutilisables qui encapsulent le comportement réactif.

#### Exemple : Widget ResponsiveText

```dart
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

class ResponsiveText extends StatelessWidget {
  final String text;
  final FontWeight fontWeight;
  final Color color;

  const ResponsiveText(
    this.text, {
    Key? key,
    this.fontWeight = FontWeight.normal,
    this.color = Colors.black,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: TextStyle(
        fontSize: 16.sp,         // taille de police mise à l'échelle
        fontWeight: fontWeight,
        color: color,
      ),
    );
  }
}
```

Utilisation : au lieu de spécifier manuellement la taille de la police à chaque fois, vous utilisez `ResponsiveText`. De même, vous pouvez construire `ResponsiveContainer`, `ResponsivePadding`, etc. L'encapsulation de la logique réactive dans des widgets améliore la réutilisation du code et la cohérence.

#### Exemple : Widget BreakpointAwareLayout

```dart
import 'package:flutter/material.dart';

class BreakpointAwareLayout extends StatelessWidget {
  final Widget mobile;
  final Widget tablet;
  final Widget desktop;

  const BreakpointAwareLayout({
    Key? key,
    required this.mobile,
    required this.tablet,
    required this.desktop,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth >= 1024) {
          return desktop;
        } else if (constraints.maxWidth >= 600) {
          return tablet;
        } else {
          return mobile;
        }
      },
    );
  }
}
```

Utilisation : vous fournissez trois versions de votre UI et le widget choisira en fonction de la largeur.

## Exemple d'un écran réactif complet

Nous allons diviser l'exemple en ces parties :

1. **Configuration du projet et importations**
    
2. **Point d'entrée de l'application (**`main()` et `MyApp`)
    
3. **Initialisation de ScreenUtil**
    
4. **Mise en page de la page principale (**`MyHomePage`)
    
5. **Mise en page adaptative avec** `LayoutBuilder`
    
6. **Constructeur de contenu principal (**`_buildMainContent`)
    
7. **Style réactif avec** `flutter_screenutil`
    

### **Configuration du projet et importations**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

void main() {
  runApp(MyApp());
}
```

### **Point d'entrée de l'application : la classe** `MyApp`

```dart
class MyApp extends StatelessWidget {
  // La taille de conception correspond au design de référence (ex: iPhone 6/7/8)
  final Size designSize = const Size(360, 690);

  @override
  Widget build(BuildContext context) {
    return ScreenUtilInit(
      designSize: designSize,
      minTextAdapt: true,       // adapte la taille de la police
      splitScreenMode: true,    // supporte le mode écran scindé
      builder: (context, child) {
        return MaterialApp(
          title: 'Exemple Flutter Réactif',
          home: MyHomePage(),
        );
      },
    );
  }
}
```

### **L'écran d'accueil réactif (**`MyHomePage`)

```dart
class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final double screenWidth  = MediaQuery.of(context).size.width;
    final double screenHeight = MediaQuery.of(context).size.height;
    final Orientation orientation = MediaQuery.of(context).orientation;

    return Scaffold(
      appBar: AppBar(
        title: Text(
          'UI Réactive',
          style: TextStyle(fontSize: 20.sp),
        ),
      ),
      body: SafeArea(
        child: LayoutBuilder(
          builder: (context, constraints) {
            if (constraints.maxWidth > 600) {
              // Mise en page Tablette/Ordinateur
              return Row(
                children: [
                  Expanded(
                    flex: 2,
                    child: Container(
                      color: Colors.blueGrey[50],
                      child: Center(
                        child: Text(
                          'Panneau latéral',
                          style: TextStyle(fontSize: 18.sp),
                        ),
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 5,
                    child: Container(
                      padding: EdgeInsets.all(16.w),
                      child: _buildMainContent(context),
                    ),
                  ),
                ],
              );
            } else {
              // Mise en page Mobile
              return SingleChildScrollView(
                child: Padding(
                  padding: EdgeInsets.symmetric(horizontal: 16.w, vertical: 24.h),
                  child: _buildMainContent(context),
                ),
              );
            }
          },
        ),
      ),
    );
  }
}
```

### **Construction du contenu principal**

```dart
Widget _buildMainContent(BuildContext context) {
  return Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      Text(
        'Bienvenue sur l\'application réactive',
        style: TextStyle(fontSize: 24.sp, fontWeight: FontWeight.bold),
      ),
      SizedBox(height: 12.h),
      Text(
        'Cette interface s\'adapte automatiquement aux différentes tailles d\'écran. Essayez de redimensionner votre fenêtre ou de changer l\'orientation.',
        style: TextStyle(fontSize: 16.sp),
      ),
      SizedBox(height: 24.h),
      Row(
        children: [
          Expanded(
            child: Image.asset(
              'assets/sample.jpg',
              width: double.infinity,
              height: 200.h,
              fit: BoxFit.cover,
            ),
          ),
        ],
      ),
      SizedBox(height: 24.h),
      Row(
        children: [
          Expanded(
            child: ElevatedButton(
              onPressed: () {},
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(vertical: 14.h),
                textStyle: TextStyle(fontSize: 16.sp),
              ),
              child: Text('Commencer'),
            ),
          ),
        ],
      ),
    ],
  );
}
```

## Guide complet : explication approfondie du code

Passons maintenant à une **explication détaillée** de l'exemple complet d'écran Flutter réactif, ligne par ligne et bloc par bloc.

### **Importations et point d'entrée de l'application**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

void main() {
  runApp(MyApp());
}
```

#### Explication :

`import 'package:flutter/material.dart';` importe la bibliothèque Material Design de Flutter, qui contient les widgets UI essentiels tels que `Scaffold`, `AppBar`, `Text` et `Column`. `import 'package:flutter_screenutil/flutter_screenutil.dart';` importe le package `flutter_screenutil`, fournissant des utilitaires de mise à l'échelle comme `.sp`, `.h`, `.w` et `.r` qui ajustent automatiquement les éléments de l'interface utilisateur en fonction de la taille de l'écran de l'appareil. La fonction `void main()` sert de point d'entrée à l'application Flutter, appelant `runApp(MyApp())` pour rendre le widget `MyApp` comme racine de l'application.

### **Racine de l'application : le widget** `MyApp`

```dart
class MyApp extends StatelessWidget {
  // La taille de conception correspond au design de référence (ex: iPhone 6/7/8)
  final Size designSize = const Size(360, 690);

  @override
  Widget build(BuildContext context) {
    return ScreenUtilInit(
      designSize: designSize,
      minTextAdapt: true,       // adapte la taille de la police
      splitScreenMode: true,    // supporte le mode écran scindé
      builder: (context, child) {
        return MaterialApp(
          title: 'Exemple Flutter Réactif',
          home: MyHomePage(),
        );
      },
    );
  }
}
```

#### Explication :

`MyApp` étend `StatelessWidget`, ce qui signifie qu'il ne maintient aucun état interne et construit simplement l'arbre des widgets. Le `designSize` définit la résolution de conception de base utilisée dans vos maquettes (dans ce cas, 360x690, typique d'un iPhone 8). `ScreenUtilInit` initialise le package `flutter_screenutil`, et ses paramètres configurent le fonctionnement de la réactivité : `designSize: Size(360, 690)` définit la taille de conception de référence pour tous les calculs de mise à l'échelle, `minTextAdapt: true` garantit que le texte s'adapte automatiquement sur les petits écrans sans être coupé, et `splitScreenMode: true` maintient un comportement de mise en page correct en mode écran scindé sur des appareils comme les tablettes Android. À l'intérieur de son constructeur, il renvoie un `MaterialApp`, qui définit le titre de l'application et définit `home: MyHomePage()`, l'écran principal affiché au lancement de l'application.

Jusqu'à présent, cette partie configure l'environnement pour la mise à l'échelle réactive.

### **La mise en page de l'écran d'accueil** `MyHomePage`

```dart
class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key}) : super(key: key);
```

Le widget est **stateless**, ce qui signifie que sa mise en page ne dépend pas d'un état mutable.

À l'intérieur de `build(BuildContext context)` :

```dart
final double screenWidth  = MediaQuery.of(context).size.width;
final double screenHeight = MediaQuery.of(context).size.height;
final Orientation orientation = MediaQuery.of(context).orientation;
```

Ces trois lignes accèdent à `MediaQuery`, une API Flutter qui fournit des informations sur la taille de l'écran, l'orientation et d'autres propriétés de mise en page, où `screenWidth` représente la largeur actuelle de l'écran de l'appareil, `screenHeight` représente sa hauteur, et `orientation` indique si l'appareil est en mode portrait ou paysage.

Vous utiliserez ces valeurs pour ajuster dynamiquement votre mise en page.

### **Le Scaffold et l'AppBar**

```dart
return Scaffold(
  appBar: AppBar(
    title: Text(
      'UI Réactive',
      style: TextStyle(fontSize: 20.sp),
    ),
  ),
```

#### Explication :

`Scaffold` fournit la structure de base de la page, incluant la barre d'application, le corps et des éléments optionnels comme un bouton d'action flottant ou un tiroir. À l'intérieur de l' `AppBar`, le texte du titre utilise `20.sp` au lieu d'une valeur de pixel fixe, `.sp` (pixels mis à l'échelle) de `flutter_screenutil` garantit que la taille de la police s'ajuste automatiquement à la densité de pixels et à la résolution de l'écran, ce qui signifie qu'un texte de `20.sp` apparaîtra plus petit sur les écrans compacts et s'agrandira proportionnellement sur les appareils plus grands comme les tablettes.

### **SafeArea + LayoutBuilder**

```dart
body: SafeArea(
  child: LayoutBuilder(
    builder: (context, constraints) {
```

#### Explication :

`SafeArea` garantit que le contenu ne chevauche pas les zones de l'interface système telles que l'encoche, la barre d'état ou les gestes de navigation, tandis que `LayoutBuilder` fournit les contraintes (largeur et hauteur maximales) de l'espace disponible à l'intérieur de son parent, permettant la création de mises en page réactives qui s'adaptent dynamiquement à la taille réelle de l'écran au moment de l'exécution.

### **Gestion des petits et grands écrans**

```dart
if (constraints.maxWidth > 600) {
  // Mise en page Tablette/Ordinateur
  return Row(
    children: [
      Expanded(
        flex: 2,
        child: Container(
          color: Colors.blueGrey[50],
          child: Center(
            child: Text(
              'Panneau latéral',
              style: TextStyle(fontSize: 18.sp),
            ),
          ),
        ),
      ),
      Expanded(
        flex: 5,
        child: Container(
          padding: EdgeInsets.all(16.w),
          child: _buildMainContent(context),
        ),
      ),
    ],
  );
} else {
  // Mise en page Mobile
  return SingleChildScrollView(
    child: Padding(
      padding: EdgeInsets.symmetric(horizontal: 16.w, vertical: 24.h),
      child: _buildMainContent(context),
    ),
  );
}
```

#### Explication :

Ce bloc gère les points d'arrêt réactifs en déterminant comment l'interface utilisateur s'adapte aux différentes largeurs d'écran. Si `constraints.maxWidth > 600`, la mise en page est traitée comme une vue tablette ou ordinateur. Dans ce cas, l'interface utilise une `Row` pour diviser l'écran horizontalement, avec `Expanded(flex: 2)` créant une barre latérale qui occupe deux parties de la largeur disponible, et `Expanded(flex: 5)` créant la zone de contenu principal qui occupe cinq parties, maintenant un ratio de 2:5. La barre latérale affiche « Panneau latéral », représentant l'endroit où la navigation latérale ou des panneaux supplémentaires peuvent apparaître sur des écrans plus grands. Pour les écrans plus petits (téléphones), la mise en page passe à une disposition verticale utilisant `SingleChildScrollView` pour permettre le défilement, avec un padding appliqué via un espacement mis à l'échelle (`16.w` horizontalement et `24.h` verticalement). La fonction `_buildMainContent()` est réutilisée pour maintenir la logique du contenu cohérente sur toutes les mises en page.

### **Construction du contenu principal**

```dart
Widget _buildMainContent(BuildContext context) {
  return Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      Text(
        'Bienvenue sur l\'application réactive',
        style: TextStyle(fontSize: 24.sp, fontWeight: FontWeight.bold),
      ),
      SizedBox(height: 12.h),
      Text(
        'Cette interface s\'adapte automatiquement aux différentes tailles d\'écran. Essayez de redimensionner votre fenêtre ou de changer l\'orientation.',
        style: TextStyle(fontSize: 16.sp),
      ),
      SizedBox(height: 24.h),
      Row(
        children: [
          Expanded(
            child: Image.asset(
              'assets/sample.jpg',
              width: double.infinity,
              height: 200.h,
              fit: BoxFit.cover,
            ),
          ),
        ],
      ),
      SizedBox(height: 24.h),
      Row(
        children: [
          Expanded(
            child: ElevatedButton(
              onPressed: () {},
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(vertical: 14.h),
                textStyle: TextStyle(fontSize: 16.sp),
              ),
              child: Text('Commencer'),
            ),
          ),
        ],
      ),
    ],
  );
}
```

#### Explication :

Cette méthode construit le contenu visible réel de l'application. Elle utilise une `Column` pour empiler les widgets verticalement, avec `crossAxisAlignment: CrossAxisAlignment.start` alignant tous les widgets enfants au début de l'axe horizontal (côté gauche dans les mises en page LTR). Les widgets Text utilisent `.sp` pour une mise à l'échelle réactive, appliquant une taille de police plus grande (24.sp) pour le titre et une taille confortable plus petite (16.sp) pour le corps. `SizedBox` fournit un espacement vertical (`12.h` ou `24.h`), où `.h` s'adapte proportionnellement à la hauteur de l'écran. Une `Row` contenant `Image.asset` utilise `Expanded` pour que l'image remplisse la largeur disponible, avec `fit: BoxFit.cover` garantissant que l'image remplit correctement son conteneur et `height: 200.h` permettant une mise à l'échelle dynamique de la hauteur. Une autre `Row` contient un `ElevatedButton` qui s'étend sur toute la largeur disponible via `Expanded`, avec un padding et une mise à l'échelle de la taille de la police via `EdgeInsets.symmetric(vertical: 14.h)` et `TextStyle(fontSize: 16.sp)`. Dans l'ensemble, la méthode `_buildMainContent()` produit une mise en page propre, évolutive et réactive qui maintient une cohérence visuelle sur tous les appareils.

### **Pourquoi cela fonctionne**

`LayoutBuilder` donne les contraintes parentales, vous permettant de rendre conditionnellement différentes mises en page pour les mobiles et les grands écrans. `ScreenUtil` garantit que tous les éléments (texte, padding, tailles) s'adaptent proportionnellement. `MediaQuery` peut être utilisé si vous avez besoin d'une adaptation en temps réel basée sur la rotation, la taille ou le padding de l'appareil. `SafeArea` empêche le contenu d'être coupé sous les zones de l'interface système.

Ensemble, ces techniques combinent la **flexibilité native de Flutter** avec la **puissance de mise à l'échelle de ScreenUtil**, rendant l'interface utilisateur dynamique, élégante et cohérente sur toutes les plateformes.

## **Points clés à retenir**

1. Concevez toujours avec une **taille de référence** et mettez à l'échelle avec `flutter_screenutil`.
    
2. Utilisez `LayoutBuilder` ou `MediaQuery` pour les points d'arrêt.
    
3. Testez les mises en page en **portrait/paysage** et sur **petits/grands écrans**.
    
4. Évitez les valeurs de pixels codées en dur, utilisez plutôt `.sp`, `.w`, `.h`.
    
5. Gardez votre contenu modulaire avec des fonctions d'aide comme `_buildMainContent()`.
    

## Conclusion

Créer des interfaces utilisateur réactives et adaptatives dans Flutter ne consiste pas seulement à faire en sorte que les choses « aient l'air correctes » sur différents appareils, il s'agit de concevoir des expériences **fluides, cohérentes** et **utilisables** quels que soient la taille de l'écran, l'orientation ou la plateforme. En tirant parti des widgets de mise en page intégrés de Flutter (`Row`, `Column`, `Flexible`, `Expanded`, `LayoutBuilder`), et en les couplant avec des API sensibles à l'écran (`MediaQuery`, `SafeArea`, etc.) et des packages spécialisés (comme `flutter_screenutil`), vous pouvez créer des applications qui s'adaptent magnifiquement.

Points clés à retenir :

* Pensez d'abord à la **flexibilité** : évitez les dimensionnements rigides.
    
* Utilisez la taille/les contraintes de l'écran pour décider des variations de mise en page (au lieu du type d'appareil).
    
* Mettez à l'échelle la typographie, les images et les paddings pour maintenir l'utilisabilité et l'esthétique.
    
* Testez toujours sur plusieurs appareils/tailles/orientations.
    
* Encapsulez la logique réactive dans des widgets réutilisables pour garder votre code propre et maintenable.
    

Avec ces pratiques en main, vous serez bien équipé pour proposer des applications Flutter visuellement époustouflantes, performantes et véritablement réactives pour 2024 et au-delà.

## Références

* « Design adaptatif et réactif dans Flutter », Docs Flutter. ([Docs Flutter](https://docs.flutter.dev/ui/adaptive-responsive))
    
* « Créer des UI réactives dans Flutter : conseils et bonnes pratiques ». Blog TheOneTechnologies. ([TheOneTechnologies](https://theonetechnologies.com/blog/post/building-responsive-ui-in-flutter-tips-and-best-practices))
    
* « Meilleure stratégie pour implémenter le design réactif : r/FlutterDev », discussion Reddit. ([Reddit](https://www.reddit.com/r/FlutterDev/comments/192sqg5/best_strategy_to_implement_responsive_design))
    
* « Comment rendre une application Flutter réactive pour différentes tailles d'écran mobile », Q&A StackOverflow. ([Stack Overflow](https://stackoverflow.com/questions/79539122/how-to-make-a-flutter-app-responsive-for-different-mobile-screen-sizes))
    
* « 5 bonnes pratiques pour créer des UI robustes et réactives dans Flutter », blog Somnio Software. ([somniosoftware.com](https://somniosoftware.com/blog/5-best-practices-to-build-robust-and-responsive-uis-in-flutter))