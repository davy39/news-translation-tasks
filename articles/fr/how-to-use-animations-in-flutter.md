---
title: Comment utiliser les animations dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-10-03T18:39:38.007Z'
originalURL: https://freecodecamp.org/news/how-to-use-animations-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759507962194/9f1bff80-2205-4e63-a6b7-8fee605bc5fa.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: flutter-aware
  slug: flutter-aware
- name: animation
  slug: animation
seo_title: Comment utiliser les animations dans Flutter
seo_desc: 'Animations are a fundamental aspect of mobile app development. They go
  beyond just adding visual appeal, and have become essential for enhancing the overall
  user experience.

  Flutter, Google''s open-source UI development toolkit, lets you create seamle...'
---

Les animations sont un aspect fondamental du développement d'applications mobiles. Elles vont au-delà du simple attrait visuel et sont devenues essentielles pour améliorer l'expérience utilisateur globale.

Flutter, le kit de développement d'interface utilisateur open-source de Google, vous permet de créer des animations fluides et attrayantes sans effort. Voyons plus en détail pourquoi les animations sont cruciales et comment Flutter fait du développement d'animations une entreprise passionnante et créative.

## Table des matières :

1. [Prérequis](#heading-prerequis)
    
2. [Commandes de configuration rapide](#heading-commandes-de-configuration-rapide)
    
3. [Pourquoi les animations sont importantes](#heading-pourquoi-les-animations-sont-importantes)
    
4. [Types d'animations Flutter de haut niveau](#heading-types-danimations-flutter-de-haut-niveau)
    
5. [Animations implicites](#heading-animations-implicites)
    
    * [Exemple AnimatedContainer](#heading-exemple-animatedcontainer)
        
6. [Animations explicites](#heading-animations-explicites)
    
    * [Explication](#heading-explication)
        
7. [Animations courbes](#heading-animations-courbes)
    
8. [Enchaînement d'animations (translation + rotation)](#heading-enchainement-danimations-translation-rotation)
    
9. [Animations décalées](#heading-animations-decalees)
    
10. [Animations Hero](#heading-animations-hero)
    
11. [AnimatedBuilder avec plusieurs propriétés](#heading-animatedbuilder-avec-plusieurs-proprietes)
    
12. [Animations basées sur les gestes](#heading-animations-basees-sur-les-gestes)
    
13. [AnimatedSwitcher](#heading-animatedswitcher)
    
14. [TweenSequence](#heading-tweensequence)
    
15. [Animations basées sur la physique](#heading-animations-basees-sur-la-physique)
    
16. [TweenSequence vs Staggered vs Chained](#heading-tweensequence-vs-staggered-vs-chained)
    
17. [AnimatedWidget vs AnimatedBuilder](#heading-animatedwidget-vs-animatedbuilder)
    
18. [Conseils pratiques supplémentaires et bonnes pratiques](#heading-conseils-pratiques-supplementaires-et-bonnes-pratiques)
    
19. [Aides et widgets courants (liste aide-mémoire)](#heading-aides-et-widgets-courants-liste-aide-memoire)
    
20. [Références](#heading-references)
    

## Prérequis

Avant de plonger dans les animations Flutter, assurez-vous que votre environnement de développement est prêt. Vous devriez avoir :

* **Le SDK Flutter installé et ajouté au PATH**. Vous pouvez le confirmer en exécutant `flutter doctor`, qui vérifie votre configuration pour les problèmes courants et s'assure que tout ce qui est nécessaire au développement Flutter est correctement installé.
    
* **Des connaissances de base sur Dart et les widgets Flutter**, y compris `StatelessWidget`, `StatefulWidget`, et la compréhension de la méthode `build()`.
    
* **Un IDE** comme VS Code ou Android Studio, avec les plugins Flutter installés.
    
* **Un appareil ou un émulateur** disponible pour exécuter vos projets en utilisant `flutter run`.
    
* **Une familiarité avec async/await** et la sécurité nulle (null-safety) de Dart (`late`, types non-nullables).
    

## Commandes de Configuration Rapide

Pour ce guide, nous utiliserons un projet de démonstration simple appelé `animation_demo` pour explorer diverses animations. Voici comment commencer :

```bash
flutter doctor
flutter create animation_demo
cd animation_demo
flutter run
```

* `flutter doctor` : vérifie votre environnement et vous indique s'il manque quelque chose.
    
* `flutter create animation_demo` : génère la structure d'un nouveau projet Flutter appelé `animation_demo`.
    
* `flutter run` : lance l'application sur un appareil connecté ou un émulateur.
    

Avec cette configuration, nous pouvons commencer à expérimenter les animations.

## Pourquoi les Animations sont Importantes

Les animations ne servent pas seulement à rendre une application attrayante. Elles jouent également un rôle crucial dans l'amélioration de l'expérience utilisateur. Des animations bien pensées aident les utilisateurs à comprendre votre interface, fournissent un retour d'information et rendent votre application plus fluide et plus engageante.

Par exemple, le retour visuel est essentiel lorsqu'un utilisateur interagit avec votre application. Une pression sur un bouton peut légèrement réduire sa taille ou produire un effet d'ondulation (ripple effect) pour indiquer que l'action a été reconnue. Les transitions fluides aident également les utilisateurs à comprendre la navigation ou les changements dans l'interface. Passer d'une vue en liste à une vue détaillée à l'aide d'une animation Hero semble intuitif plutôt qu'abrupt ou saccadé.

Enfin, des animations bien conçues peuvent augmenter l'engagement et la performance perçue. Des mouvements subtils, des transitions ou des indicateurs de chargement peuvent donner l'impression qu'une application est plus rapide et plus réactive. Lorsque les animations sont judicieusement implémentées, elles élèvent la qualité globale de l'application, lui donnant un aspect fini et professionnel.

## Types d'Animations Flutter de Haut Niveau

Flutter propose une variété de types d'animations pour gérer différents scénarios. Il est important de comprendre ces types conceptuellement avant de passer au code :

### Animations Implicites

Il s'agit d'animations simples, basées sur les propriétés, qui nécessitent une configuration minimale. Par exemple, l'animation de la largeur, de la hauteur ou de la couleur d'un conteneur peut être réalisée avec des widgets comme `AnimatedContainer`, `AnimatedOpacity` ou `AnimatedPositioned`. Les animations implicites sont idéales pour des changements simples sans avoir besoin d'un contrôle granulaire.

### Animations Explicites

Les animations explicites vous donnent un contrôle total sur le timing, l'assouplissement (easing) et le cycle de vie de l'animation. Vous utilisez `AnimationController`, `Tween` et des widgets comme `AnimatedBuilder` ou `AnimatedWidget` pour créer des animations personnalisées et complexes. Les animations explicites sont préférables lorsque vous avez besoin d'un contrôle précis sur plusieurs propriétés ou d'un comportement personnalisé.

### Animations Basées sur la Physique

Les animations basées sur la physique simulent un mouvement naturel en utilisant la bibliothèque `flutter/physics` de Flutter. Les exemples incluent `SpringSimulation` et `FlingSimulation`. Elles sont parfaites lorsque vous voulez un mouvement réaliste et naturel, comme des widgets déplaçables ou des éléments d'interface rebondissants.

### Animations Hero

Les animations Hero permettent des transitions d'éléments partagés entre les écrans. En utilisant le widget `Hero`, vous pouvez animer un widget d'une route à une autre, rendant les transitions fluides et connectées.

### Animations Décalées (Staggered) & Séquentielles

Les animations décalées vous permettent de synchroniser plusieurs animations pour qu'elles commencent à des moments différents. `TweenSequence` permet des animations enchaînées à plusieurs étapes au sein d'un seul contrôleur. Ces techniques sont utiles pour orchestrer des mouvements d'interface complexes.

Passons maintenant en revue chacun de ces types d'animations afin que vous puissiez voir comment ils fonctionnent en pratique.

## Animations Implicites

Les animations implicites vous permettent d'animer automatiquement les changements de propriétés des widgets. Voyons un exemple avec `AnimatedContainer` :

```dart
AnimatedContainer(
  duration: Duration(milliseconds: 300),
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  color: _isExpanded ? Colors.blue : Colors.grey,
  curve: Curves.easeInOut,
  child: Center(child: Text('Tap')),
)
```

Voici ce qui se passe dans ce code :

* `AnimatedContainer` : anime automatiquement les changements de ses propriétés.
    
* `duration` : définit la durée de l'animation.
    
* `width` / `height` : s'anime entre 100 et 200 selon `_isExpanded`.
    
* `color` : s'anime du gris au bleu.
    
* `curve` : contrôle l'accélération/décélération, rendant le mouvement naturel.
    
* `child` : widget enfant optionnel, qui n'est pas animé à moins que ses propres propriétés ne changent.
    

Les animations implicites sont parfaites pour des effets rapides basés sur les propriétés avec un minimum de code.

## Animations Explicites

Les animations explicites nécessitent plus de configuration mais offrent un contrôle total. Voici un exemple complet, moderne et respectant la null-safety qui redimensionne un bouton :

```dart
import 'package:flutter/material.dart';

class ScaleDemo extends StatefulWidget {
  @override
  _ScaleDemoState createState() => _ScaleDemoState();
}

class _ScaleDemoState extends State<ScaleDemo> with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(seconds: 1),
      vsync: this,
    );
    _animation = Tween<double>(begin: 0.5, end: 1.5).animate(_controller);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Scale Animation')),
      body: Center(
        child: AnimatedBuilder(
          animation: _animation,
          builder: (context, child) {
            return Transform.scale(
              scale: _animation.value,
              child: child,
            );
          },
          child: ElevatedButton(
            onPressed: () {
              if (_controller.status == AnimationStatus.completed) {
                _controller.reverse();
              } else {
                _controller.forward();
              }
            },
            child: const Text('Animate'),
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
```

Examinons les concepts clés de ce code :

* **AnimationController** : contrôle la chronologie de l'animation de 0.0 à 1.0.
    
* **Tween** : fait correspondre les valeurs du contrôleur à une plage (ici, 0.5 → 1.5 pour la mise à l'échelle). Un tween définit les valeurs de début et de fin d'une animation.
    
* **AnimatedBuilder** : reconstruit uniquement les widgets à l'intérieur de son constructeur pendant les battements (ticks) de l'animation, optimisant ainsi les performances.
    
* **Paramètre child dans AnimatedBuilder** : évite de reconstruire des widgets coûteux à chaque image. Dans cet exemple, le bouton est passé comme `child` pour éviter des reconstructions inutiles.
    

Vous pouvez également utiliser un `TextButton` plus simple avec la même logique d'animation :

```dart
TextButton(
  onPressed: () {
    if (_controller.status == AnimationStatus.completed) {
      _controller.reverse();
    } else {
      _controller.forward();
    }
  },
  child: Text('Animate'),
)
```

## Animations Courbes

Les animations semblent souvent peu naturelles si elles se déplacent de manière linéaire. **CurvedAnimation** modifie la progression de l'animation pour la rendre plus naturelle :

```dart
_controller = AnimationController(
  duration: Duration(seconds: 2),
  vsync: this,
);
_animation = CurvedAnimation(
  parent: _controller,
  curve: Curves.easeInOut,
);
```

**CurvedAnimation** enveloppe un contrôleur et applique une courbe pour remapper linéairement 0→1 en valeurs assouplies.

Souvent, vous combinez une CurvedAnimation avec un Tween comme ceci :

```dart
_animation = Tween<double>(begin: 0, end: 1).animate(
  CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
);
```

**Tween** définit ici la valeur de début et de fin d'une animation, fournissant la plage numérique pilotée par le contrôleur.

## Enchaînement d'Animations (Translation + Rotation)

Parfois, vous voulez qu'un widget se déplace et pivote simultanément. Voici comment configurer de telles animations :

```dart
import 'dart:math' as math;

_translation = Tween<double>(begin: 0, end: 100).animate(_controller);
_rotation = Tween<double>(begin: 0, end: 2 * math.pi).animate(_controller);
```

Voici ce qui se passe ici :

* `math.pi` est utilisé pour les calculs de rotation.
    
* `_translation` déplace le widget de 100 pixels horizontalement.
    
* `_rotation` fait pivoter le widget de 360 degrés (2π radians).
    

Vous pouvez envelopper les deux dans un `Transform` imbriqué à l'intérieur d'un `AnimatedBuilder` comme ceci :

```dart
Transform.translate(
  offset: Offset(_translation.value, 0),
  child: Transform.rotate(angle: _rotation.value, child: YourWidget()),
);
```

## Animations Décalées

Le décalage (staggering) permet à plusieurs animations de s'exécuter à différents intervalles sur le même contrôleur :

```dart
_controller = AnimationController(duration: Duration(seconds: 2), vsync: this);

_animation1 = Tween<double>(begin: 0, end: 1).animate(
  CurvedAnimation(
    parent: _controller,
    curve: Interval(0.0, 0.5, curve: Curves.easeInOut),
  ),
);

_animation2 = Tween<double>(begin: 0, end: 1).animate(
  CurvedAnimation(
    parent: _controller,
    curve: Interval(0.5, 1.0, curve: Curves.easeInOut),
  ),
);
```

* **Interval** définit quand chaque animation commence et se termine par rapport à la chronologie du contrôleur.
    
* Les deux animations partagent le même contrôleur mais s'exécutent en séquence.
    

## Animations Hero

Les animations Hero créent des transitions fluides entre les routes :

**Premier Écran :**

```dart
class FirstScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        Navigator.push(context, MaterialPageRoute(builder: (context) => SecondScreen()));
      },
      child: Hero(
        tag: 'hero-tag',
        child: Image.asset('assets/avatar.png', width: 100, height: 100),
      ),
    );
  }
}
```

**Deuxième Écran :**

```dart
class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Hero(
          tag: 'hero-tag',
          child: Image.asset('assets/avatar.png', width: 300, height: 300),
        ),
      ),
    );
  }
}
```

* **Le widget Hero** anime l'élément partagé entre les routes.
    
* **Le tag** doit être unique pour chaque animation partagée.
    
* Interpole automatiquement la taille, la position et la forme.
    

## AnimatedBuilder avec Plusieurs Propriétés

Vous pouvez animer plusieurs propriétés simultanément :

```dart
_controller = AnimationController(duration: Duration(seconds: 2), vsync: this);

_width = Tween<double>(begin: 100, end: 200).animate(_controller);
_height = Tween<double>(begin: 100, end: 200).animate(_controller);

AnimatedBuilder(
  animation: _controller,
  builder: (context, child) {
    return Container(
      width: _width.value,
      height: _height.value,
      child: child,
    );
  },
  child: YourWidget(),
)
```

* Plusieurs objets `Tween<double>` progressent ensemble avec un seul contrôleur.
    
* L'utilisation de `child` empêche les reconstructions inutiles de la sous-arborescence de widgets.
    

## Animations Basées sur les Gestes

Les animations basées sur les gestes répondent aux interactions directes de l'utilisateur comme les pressions, les glissements ou les appuis longs. Elles sont particulièrement utiles pour créer des interfaces interactives telles que des cartes déplaçables, des listes avec balayage pour supprimer ou des curseurs personnalisés.

Dans l'exemple ci-dessous, l'animation écoute les gestes de glissement horizontal (`onPanUpdate` et `onPanEnd`). À mesure que l'utilisateur fait glisser, le widget suit fluidement le doigt. Lorsque le geste se termine, l'animation décide de continuer vers l'avant ou de revenir en arrière selon la distance parcourue par l'utilisateur.

```dart
_controller = AnimationController(duration: Duration(milliseconds: 300), vsync: this);
_position = Tween<double>(begin: 0, end: 200).animate(_controller);

GestureDetector(
  onPanUpdate: (details) {
    _controller.value -= (details.primaryDelta ?? 0) / 200;
  },
  onPanEnd: (_) {
    if (_controller.value > 0.5) {
      _controller.forward();
    } else {
      _controller.reverse();
    }
  },
  child: AnimatedBuilder(
    animation: _controller,
    builder: (context, child) {
      return Transform.translate(offset: Offset(_position.value, 0), child: YourWidget());
    },
  ),
)
```

* `onPanUpdate` fait correspondre le mouvement du geste à la progression du contrôleur.
    
* `onPanEnd` détermine l'état final de l'animation.
    

## AnimatedSwitcher

`AnimatedSwitcher` est idéal lorsque vous souhaitez basculer entre deux widgets avec une transition fluide, comme passer d'un formulaire de connexion à un formulaire d'inscription, ou remplacer un indicateur de chargement par le contenu réel. Il gère automatiquement le fondu, la mise à l'échelle ou des transitions personnalisées lorsque le widget enfant change.

Par exemple, vous pouvez basculer entre des widgets avec une animation de fondu enchaîné :

```dart
AnimatedSwitcher(
  duration: Duration(seconds: 1),
  child: _showFirstWidget ? YourFirstWidget() : YourSecondWidget(),
)
```

**Les clés (Keys)** garantissent qu'AnimatedSwitcher reconnaît les différents widgets :

```dart
AnimatedSwitcher(
  duration: Duration(milliseconds: 500),
  child: _showFirstWidget
      ? Container(key: ValueKey('first'), child: YourFirstWidget())
      : Container(key: ValueKey('second'), child: YourSecondWidget()),
)
```

## TweenSequence

Utilisez `TweenSequence` lorsque vous voulez une animation qui passe par plusieurs étapes dans une seule chronologie, comme faire pulser un bouton (grossir -> rétrécir -> réinitialiser) ou animer une barre de progression avec des vitesses différentes à chaque phase.

Vous pouvez créer des animations à plusieurs étapes comme ceci :

```dart
_controller = AnimationController(duration: Duration(seconds: 4), vsync: this);

_animation = TweenSequence<double>([
  TweenSequenceItem(tween: Tween(begin: 0.0, end: 1.0), weight: 1),
  TweenSequenceItem(tween: Tween(begin: 1.0, end: 0.0), weight: 1),
]).animate(_controller);
```

* Chaque étape est définie par un `TweenSequenceItem`.
    
* Le poids (`weight`) détermine la durée relative.
    

## Animations Basées sur la Physique

Les animations basées sur la physique sont idéales pour les interactions qui doivent sembler "naturelles", comme les rebonds, les ressorts ou les mouvements de décélération. Par exemple, vous pouvez les utiliser pour des feuilles déplaçables, des cartes à balayer pour supprimer ou des effets de sur-défilement élastiques. Contrairement aux animations à durée fixe, elles s'appuient sur des paramètres tels que la masse, la rigidité et l'amortissement pour simuler la physique du monde réel.

Si vous voulez simuler un mouvement réaliste, voici comment faire :

```dart
import 'package:flutter/physics.dart';

final SpringDescription spring = SpringDescription(mass: 1, stiffness: 100, damping: 10);
final SpringSimulation sim = SpringSimulation(spring, 0.0, 1.0, 0.0);
_controller.animateWith(sim);
```

`SpringSimulation` pilote l'animation selon des paramètres physiques.

## Conseils, Bonnes Pratiques & Aide-mémoire

* Utilisez vsync avec les mixins `TickerProvider` pour réduire l'utilisation du CPU et de la batterie. Par exemple, `SingleTickerProviderStateMixin` garantit que l'animation ne s'exécute que lorsque l'écran est visible.
    
* Libérez toujours les contrôleurs dans `dispose()`. Ne pas appeler `_controller.dispose()` peut provoquer des fuites de mémoire. Appelez-le toujours dans votre classe `State`.
    
* Préférez les constructeurs `const` lorsque c'est possible pour de meilleures performances de reconstruction. L'utilisation de `const` pour les widgets statiques comme les icônes ou le texte les empêche de se reconstruire inutilement.
    
* N'enveloppez que la partie qui nécessite une animation et minimisez les zones de reconstruction. N'enveloppez pas tout votre écran dans un `AnimatedBuilder`. À la place, isolez uniquement le widget qui change.
    
* Analysez les performances avec Flutter DevTools si les images tombent en dessous de 60fps : si vous remarquez des saccades, ouvrez l'onglet Performance dans DevTools pour identifier les reconstructions coûteuses.
    
* Gardez les animations subtiles, car une utilisation excessive peut nuire à l'expérience utilisateur. Par exemple, une mise à l'échelle de bouton de 1.0 à 1.05 semble naturelle. Passer à 1.5 peut sembler brusque.
    
* Testez les animations sur de vrais appareils. Les simulateurs exécutent souvent les animations de manière fluide. Testez sur des téléphones Android de milieu de gamme pour vous assurer que les performances sont acceptables.
    

**Aides et widgets courants :**

* **Implicites** : `AnimatedContainer`, `AnimatedOpacity`, `AnimatedPositioned`, `AnimatedCrossFade`, `AnimatedSwitcher`. Idéal pour des changements de propriétés rapides en une ligne.
    
* **Utilitaires explicites** : `AnimationController`, `Tween`, `CurvedAnimation`, `AnimatedBuilder`, `AnimatedWidget`. Utilisez-les lorsque vous avez besoin de précision et de contrôle sur le cycle de vie.
    
* **Physique** : `SpringSimulation`, `FlingSimulation`, `ClampingScrollSimulation`. Excellent pour les effets naturels de glissement et de rebond.
    
* **Transitions** : `Hero`, `PageRouteBuilder`. Idéal pour la navigation entre écrans et les éléments partagés.
    
* **Pilotés par les gestes** : `GestureDetector`, `Draggable`, `Dismissible`. Utilisez-les pour des interactions directes comme le glissement ou le balayage.
    

## Conclusion

Les animations dans Flutter sont plus qu'un simple plaisir visuel. Ce sont des outils pour guider les utilisateurs, fournir un retour d'information et rendre les applications vivantes. Des simples animations implicites aux interactions avancées basées sur la physique, Flutter vous offre la flexibilité nécessaire pour concevoir des expériences naturelles et engageantes.

Au fur et à mesure de vos expérimentations, commencez petit avec les animations implicites, puis passez aux techniques explicites et pilotées par les gestes pour plus de contrôle. Gardez toujours à l'esprit les performances et l'expérience utilisateur : des animations subtiles et ciblées contribuent grandement à donner à votre application un aspect professionnel.

Avec ces briques de base et ces bonnes pratiques, vous êtes prêt à donner vie à vos interfaces Flutter.

**Références :**

* [Livre de recettes Flutter : animations](https://docs.flutter.dev/cookbook/animation)
    
* [Performance des animations & bonnes pratiques (DevTools)](https://docs.flutter.dev/tools/devtools/performance)
    
* Livres : *Flutter in Action* (Eric Windmill), *Practical Flutter* (Frank Zammetti)