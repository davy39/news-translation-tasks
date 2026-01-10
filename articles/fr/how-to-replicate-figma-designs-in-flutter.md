---
title: Comment reproduire les designs Figma dans Flutter — Un guide pour la réplication
  d'UI pixel-perfect
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-08-07T23:16:31.092Z'
originalURL: https://freecodecamp.org/news/how-to-replicate-figma-designs-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754608436544/1825df06-20a8-47a3-af5e-ae0c6d15a7c4.png
tags:
- name: Flutter
  slug: flutter
- name: figma
  slug: figma
- name: handbook
  slug: handbook
seo_title: Comment reproduire les designs Figma dans Flutter — Un guide pour la réplication
  d'UI pixel-perfect
seo_desc: Successfully translating a Figma design into a Flutter application requires
  more than just placing elements on the screen. The objective is to achieve pixel-perfect
  fidelity, meaning that the Flutter app must precisely mirror the designer's original
  ...
---

La traduction réussie d'un design Figma en une application Flutter nécessite plus que simplement placer des éléments à l'écran. L'objectif est d'atteindre une fidélité pixel-perfect, ce qui signifie que l'application Flutter doit refléter précisément la vision originale du designer. Cela implique de prêter une attention particulière à chaque détail, des ombres et des rayons de courbure aux hauteurs de ligne et aux espacements. Une petite divergence dans l'un de ces domaines peut altérer l'apparence et la sensation souhaitées de l'interface utilisateur.

Ce guide complet fournit des stratégies concrètes et des méthodes pratiques pour les développeurs. Il couvre les étapes spécifiques et les considérations nécessaires pour combler le fossé entre les fichiers de design et le code fonctionnel. En suivant les pratiques décrites ici, vous serez en mesure de transformer des planches Figma statiques en interfaces utilisateur Flutter de haute qualité et entièrement fonctionnelles qui correspondent exactement aux spécifications de design.

## Table des matières

* [Table des matières](#heading-table-des-matières)
    
* [Prérequis](#heading-prérequis)
    
* [Utiliser le panneau "Inspect" de Figma : Votre plan précis pour la précision](#heading-utiliser-le-panneau-inspect-de-figma-votre-plan-précis-pour-la-précision)
    
* [Implémenter un système cohérent d'espacement et de dimensionnement : La fin des nombres magiques](#heading-implémenter-un-système-cohérent-d'espacement-et-de-dimensionnement-la-fin-des-nombres-magiques)
    
* [Répliquer la typographie avec une fidélité absolue : Au-delà des polices de base](#heading-répliquer-la-typographie-avec-une-fidélité-absolue-au-delà-des-polices-de-base)
    
* [Déconstruire les mises en page avec les primitives de Flutter : Column, Row, Stack et Spacer](#heading-déconstruire-les-mises-en-page-avec-les-primitives-de-flutter-column-row-stack-et-spacer)
    
* [Maîtriser BoxDecoration : Le cheval de bataille esthétique](#heading-maîtriser-boxdecoration-le-cheval-de-bataille-esthétique)
    
* [Utiliser ClipRRect et la gestion du débordement : Gérer les intangibles](#heading-utiliser-cliprrect-et-la-gestion-du-débordement-gérer-les-intangibles)
    
* [Exploiter FittedBox et AspectRatio : Maintenir les proportions](#heading-exploiter-fittedbox-et-aspectratio-maintenir-les-proportions)
    
* [Répliquer l'opacité et les modes de fusion : Les couches subtiles](#heading-répliquer-l'opacité-et-les-modes-de-fusion-les-couches-subtiles)
    
* [Implémenter des vecteurs et des icônes avec une scalabilité : La netteté à toute échelle](#heading-implémenter-des-vecteurs-et-des-icônes-avec-une-scalabilité-la-netteté-à-toute-échelle)
    
* [Maîtriser la composabilité et la réutilisabilité : Construire des interfaces utilisateur scalables](#heading-maîtriser-la-composabilité-et-la-réutilisabilité-construire-des-interfaces-utilisateur-scalables)
    
* [Examiner les états interactifs : Boutons, entrées et autres](#heading-examiner-les-états-interactifs-boutons-entrées-et-autres)
    
* [Référencement croisé et itération continue : La boucle de vérification](#heading-référencement-croisé-et-itération-continue-la-boucle-de-vérification)
    
* [Comprendre la pensée du système de design : Au-delà des composants individuels](#heading-comprendre-la-pensée-du-système-de-design-au-delà-des-composants-individuels)
    
* [Embrasser les contraintes et la réactivité : S'adapter à tous les écrans](#heading-embrasser-les-contraintes-et-la-réactivité-s'adapter-à-tous-les-écrans)
    
* [Gestion efficace des actifs : Images et SVGs](#heading-gestion-efficace-des-actifs-images-et-svgs)
    
* [Considérations d'accessibilité : Concevoir pour tous](#heading-considérations-d'accessibilité-concevoir-pour-tous)
    
* [Optimisation des performances pendant la réplication](#heading-optimisation-des-performances-pendant-la-réplication)
    
* [Contrôle de version et collaboration : Travailler avec des équipes](#heading-contrôle-de-version-et-collaboration-travailler-avec-des-équipes)
    
* [Gestion des cas limites et des données dynamiques](#heading-gestion-des-cas-limites-et-des-données-dynamiques)
    
* [Implémenter des vecteurs et des icônes avec une scalabilité : Atteindre une cohérence visuelle sur toutes les résolutions](#heading-implémenter-des-vecteurs-et-des-icônes-avec-une-scalabilité-atteindre-une-cohérence-visuelle-sur-toutes-les-résolutions)
    
* [Auto-correction et apprentissage des erreurs](#heading-auto-correction-et-apprentissage-des-erreurs)
    
* [Aperçu du projet](#heading-aperçu-du-projet)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre et mettre en œuvre efficacement les stratégies décrites dans le guide complet pour la réplication pixel-perfect de Figma à Flutter, vous devriez idéalement posséder les prérequis suivants :

### **I. Connaissances de base en programmation et en frameworks**

1. **Langage de programmation Dart :**
    
    * **Concepts de base :** Compréhension solide de la syntaxe de Dart, des types de données, des variables, du flux de contrôle (`if/else`, boucles), des fonctions, des classes, des objets et de la programmation asynchrone (Futures, `async`/`await`).
        
    * **Null Safety :** Familiarité avec les fonctionnalités de null safety de Dart.
        
2. **SDK Flutter et environnement de développement :**
    
    * **Installation et configuration :** SDK Flutter correctement installé et configuré sur votre machine.
        
    * **Maîtrise de l'IDE :** Familiarité avec un IDE compatible Flutter comme VS Code ou Android Studio, y compris l'exécution/débogage des applications, l'utilisation du rechargement à chaud/redémarrage.
        
    * **Structure de projet de base :** Compréhension de la structure de répertoire typique d'un projet Flutter (`lib`, `assets`, `pubspec.yaml`, etc.).
        
3. **Concepts fondamentaux de Flutter :**
    
    * **Arbre de widgets :** Une compréhension claire du fonctionnement de l'arbre de widgets de Flutter, y compris les relations parent-enfant et la composition des widgets.
        
    * **StatelessWidget & StatefulWidget :** Capacité à différencier et à utiliser de manière appropriée `StatelessWidget` pour l'UI statique et `StatefulWidget` pour l'UI dynamique/interactive.
        
    * **Contexte de construction :** Compréhension de `BuildContext` et de son rôle dans l'arbre de widgets.
        

### **II. Connaissances essentielles de Figma**

1. **Navigation dans l'interface Figma :**
    
    * Capacité à ouvrir et naviguer dans les fichiers et les planches Figma.
        
    * Compréhension des calques, des groupes et des cadres.
        
2. **Maîtrise du panneau "Inspect" de Figma :**
    
    * **Crucial :** Utilisation experte du panneau "Inspect" pour extraire des valeurs précises pour :
        
        * Dimensions (largeur, hauteur)
            
        * Espacement (remplissage, marge, espace entre les éléments)
            
        * Couleurs (codes hexadécimaux, RGB, opacité)
            
        * Typographie (famille de polices, poids, taille, hauteur de ligne, espacement des lettres)
            
        * Bordures (rayon, largeur, couleur)
            
        * Ombres (décalage, flou, étalement, couleur, opacité)
            
        * Dégradés (couleurs, arrêts, angle)
            
    * **Compréhension de l'Auto Layout :** Compréhension de base du fonctionnement de l'Auto Layout dans Figma, car il dicte souvent l'utilisation de `Column`/`Row` et `Spacer`/`Expanded` dans Flutter.
        
3. **Exportation des actifs Figma :**
    
    * Connaissance de la manière de sélectionner et d'exporter divers actifs depuis Figma (images, SVGs) dans les formats et résolutions corrects.
        

### **III. Pratiques générales de développement (fortement recommandé) :**

1. **Contrôle de version (Git) :**
    
    * Compréhension de base des commandes Git (clone, add, commit, push, pull, branch). Cela est essentiel pour le développement collaboratif et la gestion des changements de code.
        
2. **Compétences en débogage :**
    
    * Capacité à utiliser le débogueur de votre IDE pour inspecter les arbres de widgets, les valeurs des variables et diagnostiquer les problèmes.
        
    * Familiarité avec Flutter DevTools pour l'inspection de l'UI et le profilage des performances.
        
3. **Résolution de problèmes :**
    
    * Une approche logique pour décomposer les problèmes complexes en parties plus petites et gérables.
        
    * Patience et persévérance dans le dépannage des divergences visuelles.
    

## Utiliser le panneau "Inspect" de Figma : Votre plan précis pour la précision

Le panneau "Inspect" dans Figma est votre ressource la plus précieuse. Avant d'écrire une seule ligne de code, passez du temps à disséquer chaque élément ici. Considérez-le comme votre plan précis.

* **Dimensions exactes :** Ne faites pas d'approximations. Notez les valeurs exactes de `width` et `height`, même si elles ont des décimales (par exemple, `123.45px`). Les valeurs `double` de Flutter accommodent parfaitement cette précision.
    
* **Espacement granulaire :** Examinez `margin` et `padding` de tous les quatre côtés. Sont-ils uniformes, ou y a-t-il une asymétrie ? Cela détermine si vous utilisez `EdgeInsets.all()`, `EdgeInsets.symmetric()`, ou le plus spécifique `EdgeInsets.fromLTRB()`.
    
* **Logique de positionnement :** Comprenez si un élément est positionné de manière absolue ou fait partie d'un cadre Auto Layout. Cette distinction cruciale détermine si vous emploierez des widgets `Positioned` dans un `Stack` ou si vous vous appuierez sur `Column`/`Row` avec `mainAxisAlignment` et `crossAxisAlignment`.
    
* **Plongée typographique approfondie :** Extrayez la famille de polices exacte, le poids (par exemple, "Inter Medium", "Inter Bold"), la taille, la hauteur de ligne, l'espacement des lettres et la couleur. Chacune de ces propriétés a un équivalent direct dans `TextStyle` de Flutter.
    
* **Codes de couleur :** Copiez les codes hexadécimaux exactement. Utilisez toujours `Color(0xFFRRGGBB)` dans Flutter pour garantir une correspondance exacte des couleurs, y compris le canal alpha si spécifié.
    
* **Bordures et ombres :** Extrayez le rayon de la bordure, la couleur, la largeur, et pour les ombres, le décalage x/y, le flou, l'étalement et la couleur. Ces éléments se traduisent directement par les propriétés `BoxDecoration` et `BoxShadow`.
    
* **Dégradés :** Si un dégradé est présent, notez méticuleusement son angle, les couleurs précises impliquées et leurs arrêts respectifs. `LinearGradient` ou `RadialGradient` de Flutter seront vos outils ici.
    

## Implémenter un système cohérent d'espacement et de dimensionnement : La fin des nombres magiques

Coder en dur des valeurs comme `16.0`, `8.0`, ou `24.0` dans votre base de code est une recette pour l'incohérence et les maux de tête de maintenance. Établissez un système de design pour l'espacement et le dimensionnement.

* **Identifier l'unité de base :** Les designs Figma utilisent souvent implicitement une unité de base d'espacement (par exemple, tous les remplissages sont des multiples de 4 ou 8 pixels). Identifiez cet incrément cohérent.
    
* **Constantes centralisées :** Créez un fichier dédié, peut-être `lib/utils/app_dimensions.dart`, pour stocker vos variables d'espacement et de dimensionnement.
    
    ```dart
    // lib/utils/app_dimensions.dart
    class AppDimensions {
      static const double spacingSmall = 8.0;
      static const double spacingMedium = 16.0;
      static const double spacingLarge = 24.0;
      static const double iconSizeMedium = 24.0;
      // ... et ainsi de suite pour toutes les mesures cohérentes
    }
    ```
    
* **Utilisation cohérente :** Faites toujours référence à ces constantes dans vos widgets :
    
    ```dart
    Padding(
      padding: const EdgeInsets.all(AppDimensions.spacingMedium),
      child: // ...
    ),
    SizedBox(width: AppDimensions.spacingSmall),
    ```
    
* **Avantage :** Cette approche garantit non seulement une cohérence visuelle mais simplifie également les ajustements de design globaux.
    

## Répliquer la typographie avec une fidélité absolue : Au-delà des polices de base

Le texte est un élément fondamental de la conception de l'interface utilisateur. Atteindre une typographie pixel-perfect signifie aller au-delà de la simple sélection de la bonne famille de polices.

* **Intégration de polices personnalisées :** Si votre design Figma utilise des polices personnalisées, vous devez les ajouter correctement à votre fichier `pubspec.yaml` et vous assurer qu'elles se chargent correctement dans votre application Flutter.
    
* **Poids de police précis :** Distinguez méticuleusement entre `FontWeight.w400` (Normal), `w500` (Moyen), `w600` (SemiGras), `w700` (Gras), etc. Le panneau d'inspection Figma vous fournira le poids exact.
    
* Précision de la `fontSize` : Utilisez la taille exacte en pixels de Figma pour la propriété `fontSize` dans `TextStyle`.
    
* **Hauteur de ligne (**`height`): Cela est primordial pour l'espacement vertical du texte. La propriété "Hauteur de ligne" de Figma, souvent exprimée en pourcentage ou en valeur de pixel, nécessite une conversion. Si Figma indique une hauteur de ligne de `24px` pour une taille de police de `16px`, votre propriété `height` de `TextStyle` doit être `24 / 16 = 1.5`.
    
* `letterSpacing` : Appliquez directement la valeur d'espacement des lettres de Figma (qui est souvent en pixels et se traduit directement par la propriété `letterSpacing` de Flutter).
    
* `textBaseline` (Avancé) : Pour des alignements très spécifiques de polices multiples ou d'icônes avec du texte, vous devrez peut-être ajuster finement `textBaseline` pour correspondre à la précision visuelle de Figma.
    

## Déconstruire les mises en page avec les primitives de Flutter : `Column`, `Row`, `Stack` et `Spacer`

Le système de mise en page déclaratif de Flutter offre des primitives puissantes. Apprendre à mapper les arrangements visuels de Figma à ces widgets est essentiel.

* **Flux principal :** Déterminez si le flux principal des éléments est horizontal (`Row`) ou vertical (`Column`).
    
* **Éléments superposés (`Stack`) :** Si des éléments sont superposés ou positionnés les uns sur les autres dans Figma, un widget `Stack` combiné avec des enfants `Positioned` est la bonne approche. Ne forcez pas les éléments superposés dans `Column`/`Row` avec des marges ou des remplissages négatifs complexes.
    
* **Distribution du contenu :**
    
    * `mainAxisAlignment` : Utilisez cela pour distribuer les enfants le long de l'axe principal d'un `Row` ou `Column` (par exemple, `start`, `center`, `end`, `spaceBetween`, `spaceAround`, `spaceEvenly`).
        
    * `crossAxisAlignment` : Utilisez cela pour aligner les enfants le long de l'axe transversal (par exemple, `start`, `center`, `end`, `stretch`, `baseline`).
        
* **Espacement flexible (`Spacer`) :** Répliquez les comportements d'auto-layout "étirer" ou "remplir l'espace disponible" de Figma en utilisant des widgets `Spacer()` dans `Row` ou `Column`.
    
* **Dimensionnement adaptatif (`Expanded`, `Flexible`) :** Lorsque des éléments doivent occuper l'espace restant ou être contraints dans une certaine proportion, `Expanded` et `Flexible` sont essentiels. Imitez précisément les comportements "Remplir le conteneur" ou "Largeur fixe" de Figma.
    

## Maîtriser `BoxDecoration` : Le cheval de bataille esthétique

`BoxDecoration` est votre outil principal pour reproduire l'esthétique visuelle des conteneurs dans Figma, y compris les arrière-plans, les bordures, les ombres et les dégradés.

* `color` : La couleur d'arrière-plan du conteneur, directement à partir du code hexadécimal de Figma.
    
* `borderRadius` : Faites correspondre les rayons de coin exacts de Figma. Utilisez `BorderRadius.circular()` pour des coins uniformes, `BorderRadius.only()` pour des coins spécifiques, ou `BorderRadius.all(Radius.elliptical(x, y))` pour des formes plus complexes.
    
* `border` : Répliquez les styles de bordure en utilisant `Border.all(color: ..., width: ...)` ou des options plus spécifiques comme `Border.symmetric()` ou `BorderDirectional()` si les côtés individuels ont des styles différents.
    
* `boxShadow` : C'est ici que les détails minutieux comptent vraiment. Extrayez chaque valeur :
    
    ```dart
    boxShadow: [
      BoxShadow(
        color: Color(0x33000000), // Couleur exacte, y compris l'opacité (canal alpha)
        offset: Offset(0, 4),      // Décalage X et Y exact
        blurRadius: 8,             // Rayon de flou exact
        spreadRadius: 0,           // Rayon d'étalement exact (souvent 0, mais toujours vérifier)
      ),
    ],
    ```
    
* `gradient` : Traduisez précisément les dégradés linéaires ou radiaux :
    
    ```dart
    gradient: LinearGradient(
      begin: Alignment.topLeft, // Ou des angles spécifiques dérivés de Figma
      end: Alignment.bottomRight,
      colors: [Color(0xFF00FF00), Color(0xFF0000FF)], // Couleurs exactes
      stops: [0.0, 1.0], // Positions exactes des arrêts de couleur
    ),
    ```
    

## Utiliser `ClipRRect` et la gestion du débordement : Gérer les intangibles

Parfois, les éléments dans Figma peuvent sembler "déborder" ou être précisément rognés. Comprendre le comportement de rognage et de débordement de Flutter est crucial.

* `ClipRRect` pour les coins arrondis : Si le contenu d'un widget enfant doit être rogné selon les coins arrondis d'un parent (par exemple, une image dans une carte), enveloppez l'enfant dans `ClipRRect`. Ne vous fiez pas uniquement à la `BoxDecoration` du parent, surtout dans les hiérarchies complexes.
    
* **Comportement de débordement (`OverflowBox`) :** Les designs Figma peuvent montrer des éléments s'étendant au-delà des limites d'un cadre. Par défaut, `Column`/`Row` rognent le contenu (`overflow: Clip.hardEdge`). Si vous avez besoin que le contenu soit visible à l'extérieur de son parent immédiat, vous pourriez avoir besoin d'un `Stack` ou de gérer explicitement le débordement, éventuellement en utilisant un `OverflowBox` pour des scénarios spécifiques.
    
* **Ombres étendues :** Si une ombre dans Figma s'étend considérablement au-delà de son élément, assurez-vous que les valeurs `spreadRadius` et `offset` de votre `BoxShadow` sont précises. Assurez-vous également que le conteneur parent permet cette extension visuelle (par exemple, il n'a pas `clipBehavior: Clip.hardEdge` si le rognage n'est pas souhaité).
    

## Exploiter `FittedBox` et `AspectRatio` : Maintenir les proportions

Les images et les blocs de contenu doivent souvent être mis à l'échelle de manière proportionnelle ou s'adapter à des zones spécifiques. Ces widgets sont indispensables pour le design réactif.

* `FittedBox` : Excellent pour garantir qu'un widget enfant (comme une icône ou un bloc de texte) est mis à l'échelle pour s'adapter à son parent, tout en maintenant son rapport d'aspect d'origine. Pensez soigneusement aux propriétés `fit` comme `contain`, `cover`, `fill`, et `scaleDown` pour correspondre au comportement de Figma.
    
* `AspectRatio` : Crucial pour les images, les vidéos ou tout conteneur où le rapport largeur/hauteur doit être maintenu indépendamment de l'espace d'écran disponible.
    
    ```dart
    AspectRatio(
      aspectRatio: 16 / 9, // Dérivé directement des dimensions de l'image de Figma
      child: Image.network('...'),
    ),
    ```
    
* **Dimensionnement intelligent des images** : Évitez de définir des `width` et `height` fixes sur [`Image.network`](http://Image.network) ou `Image.asset` sauf si le design dicte explicitement une taille statique. Pensez plutôt à la manière dont l'image est mise à l'échelle et remplit son conteneur dans Figma.
    

## Répliquer l'opacité et les modes de fusion : Les couches subtiles

Les effets subtils définissent souvent le "ressenti" d'un design. Ne négligez pas la transparence et le mélange.

* Widget `Opacity` : Utilisez ce widget pour la transparence générale des éléments.
    
* **Canal alpha dans les couleurs** : Pour les couleurs d'arrière-plan, les bordures ou les couleurs de texte avec transparence, incluez toujours le canal alpha dans votre code hexadécimal (par exemple, `0x80RRGGBB` pour 50% d'opacité).
    
* `ColorFiltered` ou `ShaderMask` (Modes de fusion avancés) : Bien que moins courants pour les designs quotidiens, si Figma utilise des modes de fusion complexes (par exemple, "Multiply", "Screen", "Overlay"), vous devrez explorer `ColorFiltered` avec sa propriété `blendMode` ou, pour des effets personnalisés plus avancés, `ShaderMask`. Recherchez les interactions de couleurs subtiles où une couche visuelle affecte directement une autre.
    

## Implémenter des vecteurs et des icônes avec une scalabilité : La netteté à toute échelle

La rasterisation des icônes ou des formes vectorielles complexes est une erreur courante qui conduit à un flou sur différentes densités d'écran. Adoptez les graphiques vectoriels.

* **Icônes SVG** : Exportez toujours les icônes depuis Figma en tant que SVGs. Utilisez une bibliothèque comme `flutter_svg` pour les rendre dans votre application Flutter, assurant ainsi une netteté et une scalabilité sur toutes les résolutions d'appareils.
    
* `CustomPaint` pour les formes uniques : Pour les formes très uniques, non standard, les illustrations ou les diviseurs complexes, `CustomPainter` est votre outil ultime. Cela nécessite de traduire les chemins vectoriels de Figma (courbes de Bézier, lignes) en objet `Path` de Flutter. C'est l'apogée de l'"attention aux détails" pour les graphiques personnalisés.
    
* **Polices d'icônes** : Pour les ensembles d'icônes standard (par exemple, Material Icons, Font Awesome), utilisez le widget `Icon` intégré de Flutter ou importez la famille de polices d'icônes spécifique dans votre `pubspec.yaml` et référencez-la dans votre widget `Icon`.
    

## Maîtriser la composabilité et la réutilisabilité : Construire des interfaces utilisateur scalables

Les composants de Figma ne sont pas seulement pour le design, ils sont un indice direct sur la manière de structurer votre code Flutter.

* **Identifier les composants Figma** : Chaque bouton, carte, champ de saisie ou barre de navigation qui est un composant dans Figma devrait idéalement être un `StatelessWidget` ou `StatefulWidget` réutilisable dans Flutter.
    
* **Personnalisation basée sur les propriétés** : Concevez vos composants Flutter pour accepter des paramètres (props) pour le texte, les couleurs, les icônes et les comportements interactifs, tout comme les composants Figma ont des variantes ou des propriétés.
    
* **Intégration du thème** : Utilisez `ThemeData` de Flutter pour définir des styles globaux pour les couleurs, la typographie et les comportements des widgets. Cela reflète les jetons de design de Figma et garantit la cohérence dans votre application.
    
* **Styles partagés** : Créez des classes ou des constantes pour les `TextStyle` ou `BoxDecoration` fréquemment utilisés pour centraliser votre langage de design.
    

## Examiner les états interactifs : Boutons, entrées et autres

Le design n'est pas statique. Répliquer les états interactifs est un détail critique, souvent négligé.

* **Survol, pression, focus** : Les designs Figma incluent souvent des états pour les boutons (survol, pressé), les champs de saisie (focus, erreur) et autres éléments interactifs. Vous devez implémenter ceux-ci dans Flutter en utilisant `GestureDetector`, `InkWell`, `MaterialButton`, `TextFormField`, etc., et gérer leur état visuellement.
    
* **Animations** : Si Figma présente des micro-interactions ou des transitions, planifiez comment les répliquer en utilisant `AnimatedContainer`, les animations `Hero`, `PageTransitionsBuilder`, ou un `AnimationController` personnalisé.
    
* **États désactivés** : Assurez-vous que les boutons ou champs de saisie désactivés sont visuellement distincts et correspondent à leurs homologues Figma en termes de couleur, d'opacité et de changements de curseur.
    

## Référencement croisé et itération continue : La boucle de vérification

La réplication n'est pas une tâche ponctuelle, c'est un processus itératif de comparaison et d'affinement.

* **Comparaison côte à côte** : Ayez toujours votre application Flutter en cours d'exécution sur un appareil ou un émulateur à côté de votre design Figma. Idéalement, prenez des captures d'écran de votre application et superposez-les sur le design Figma pour repérer les divergences.
    
* **Scan pixel par pixel** : Zoomez littéralement dans le design Figma et votre application Flutter en cours d'exécution. Recherchez :
    
    * **Erreurs de décalage d'un pixel** : Une différence d'un seul pixel dans le remplissage, la bordure ou l'espacement.
        
    * **Décalages de couleur subtils** : Les couleurs sont-elles exactement les mêmes ? Tenez compte de l'étalonnage du moniteur, mais efforcez-vous de faire correspondre les codes hexadécimaux.
        
    * **Nuances de rendu de police** : Parfois, le rendu de la police peut varier subtilement selon les plateformes ou le moteur de texte de Flutter. Ajustez légèrement `letterSpacing` ou `height` si nécessaire pour obtenir une parité visuelle.
        
    * **Fidélité des ombres** : Les ombres sont-elles aussi douces/dures, diffuses et décalées que dans Figma ?
        
    * **Précision de l'alignement** : Même un léger désalignement des lignes de base du texte ou des centres des icônes doit être corrigé.
        
* **Outils automatisés (si applicable)** : Bien que l'inspection manuelle soit primordiale, certains plugins ou outils tiers peuvent aider à comparer l'UI Flutter avec Figma, offrant une vérification initiale rapide.
    
* **Revue par les pairs** : Une paire d'yeux frais d'un autre développeur peut souvent repérer des détails que vous avez devenus aveugle à voir.
    

## Comprendre la pensée du système de design : Au-delà des composants individuels

**Pourquoi c'est important :** Les fichiers Figma représentent souvent un système de design vivant. Comprendre cette philosophie vous aide à construire une application Flutter plus robuste et maintenable.

**Conseils pratiques :**

* **Jetons de design :** Reconnaissez comment Figma utilise les "jetons de design" (variables pour les couleurs, la typographie, l'espacement, les ombres). Traduisez-les directement dans `ThemeData` de Flutter, les constantes `Color` et `TextStyle` personnalisées, et votre classe `AppDimensions`.
    
* **Bibliothèques de composants :** Considérez vos widgets Flutter comme une extension directe de la bibliothèque de composants Figma. Chaque composant dans Figma devrait idéalement correspondre à un widget Flutter bien défini et réutilisable.
    
* **Conventions de nommage :** Adoptez des conventions de nommage cohérentes dans votre code qui reflètent celles de Figma (par exemple, `primaryButton`, `headline1TextStyle`). Cela crée un langage commun entre les designers et les développeurs.
    

## Embrasser les contraintes et la réactivité : S'adapter à tous les écrans

**Pourquoi c'est important :** Les designs Figma sont souvent fixes à une certaine largeur (par exemple, 375px pour le mobile). Votre application Flutter doit être réactive et s'adapter élégamment à diverses tailles d'écran, orientations et types d'appareils.

**Conseils pratiques :**

* **Contraintes Figma :** Prêtez une attention particulière à la manière dont les éléments sont contraints dans Figma (gauche/droite, haut/bas, centre, échelle). Ceux-ci informent directement votre utilisation de `Flexible`, `Expanded`, `Align`, `Positioned` et `FractionallySizedBox` dans Flutter.
    
* `MediaQuery` : Utilisez `MediaQuery.of(context).size` pour obtenir les dimensions actuelles de l'écran et adapter les mises en page en conséquence. Évitez les largeurs/hauteurs de pixels fixes pour les écrans entiers.
    
* **Constructeurs de mise en page (`LayoutBuilder`, `OrientationBuilder`)** : Pour des mises en page réactives plus complexes, utilisez `LayoutBuilder` pour obtenir les contraintes disponibles d'un widget parent et ajuster les enfants en fonction de cela. `OrientationBuilder` aide à s'adapter aux modes portrait et paysage.
    
* **Unités relatives** : Lorsque cela est possible, pensez en termes de pourcentages ou de fractions (`FractionallySizedBox`) plutôt qu'en valeurs de pixels absolues pour l'espacement et le dimensionnement qui doivent être mis à l'échelle.
    

## Gestion efficace des actifs : Images et SVGs

**Pourquoi c'est important :** Une gestion appropriée des actifs est cruciale pour les performances et la scalabilité.

**Conseils pratiques :**

* **Formats d'exportation :** Discutez avec les designers des meilleurs formats d'exportation. Pour les icônes et les illustrations simples, les SVGs sont rois (bibliothèque `flutter_svg`). Pour les photos complexes, les PNG ou WebP (avec une compression appropriée) sont souvent préférés.
    
* **Résolution :** Pour les images raster (PNG, JPG), assurez-vous que les designers exportent les actifs en résolutions 2x et 3x, et les placent dans les répertoires `assets/images/2.0x/` et `assets/images/3.0x/` respectivement, afin que Flutter choisisse automatiquement celui qui convient à la densité de pixels de l'appareil.
    
* **Regroupement des actifs :** Déclarez tous vos actifs dans `pubspec.yaml` sous la section `assets:`.
    
* **Mise en cache des images :** Pour les images réseau, envisagez d'utiliser `cached_network_image` pour améliorer les performances et l'expérience utilisateur.
    

## Considérations d'accessibilité : Concevoir pour tous

**Pourquoi c'est important :** Une réplique pixel-perfect n'est pas vraiment complète si elle n'est pas accessible. Les designs Figma devraient idéalement inclure des annotations d'accessibilité, mais en tant que développeur, vous êtes la dernière ligne de défense.

**Conseils pratiques :**

* **Widgets sémantiques :** Utilisez les widgets sémantiques de Flutter chaque fois que possible (par exemple, `ElevatedButton` au lieu d'un `Container` personnalisé avec un `GestureDetector`). Ces widgets ont souvent des fonctionnalités d'accessibilité intégrées.
    
* **Étiquettes significatives :** Fournissez `semanticsLabel` pour les icônes et les images qui transmettent des informations aux lecteurs d'écran.
    
* **Contraste des couleurs :** Bien que ce soit principalement une responsabilité de design, vérifiez les ratios de contraste des couleurs, surtout pour le texte, par rapport aux directives WCAG. Si le design échoue, signalez-le.
    
* **Zones de toucher :** Assurez-vous que les éléments interactifs ont des zones de toucher suffisamment grandes (minimum 48x48 pixels logiques) même si l'élément visuel est plus petit, en utilisant `minWidth` sur les boutons ou `Padding` autour des `Icons`.
    

## Optimisation des performances pendant la réplication

**Pourquoi c'est important :** Une belle UI est inutile si elle est saccadée. Les décisions au niveau du code impactent les performances.

**Conseils pratiques :**

* Widgets `const` : Utilisez le constructeur `const` pour les widgets chaque fois que possible. Cela indique à Flutter que le widget peut être réutilisé sans être reconstruit, améliorant ainsi significativement les performances. C'est une opportunité souvent manquée.
    
* `RepaintBoundary` : Pour les parties complexes et statiques de votre UI qui ne changent pas souvent mais qui ont beaucoup d'enfants ou de la peinture personnalisée, envisagez de les envelopper dans un `RepaintBoundary` pour éviter les repeints inutiles de leurs enfants.
    
* **Éviter les imbrications profondes** : Bien que l'arbre de widgets de Flutter soit profond, une imbrication excessivement profonde peut parfois entraîner des problèmes de performance. Essayez d'aplatir votre arbre de widgets lorsque cela est logique (par exemple, en utilisant `Wrap` au lieu de nombreuses `Rows` imbriquées pour les mises en page de flux).
    
* **Profilage de votre application** : Utilisez l'onglet Performance de Flutter DevTools pour identifier les défauts de l'UI et les fuites de mémoire tôt dans le processus de développement.
    

## Contrôle de version et collaboration : Travailler avec des équipes

**Pourquoi c'est important :** Le développement de l'UI est rarement une entreprise solo. Une collaboration efficace en équipe est essentielle.

**Conseils pratiques :**

* **Bonnes pratiques Git** : Utilisez Git pour le contrôle de version. Créez des branches de fonctionnalités pour des écrans ou composants UI spécifiques. Commitez fréquemment avec des messages descriptifs.
    
* **Revue de code** : Faites réviser votre code UI par vos pairs. Ils peuvent repérer des détails manqués, des problèmes de performance potentiels ou suggérer une meilleure utilisation des widgets.
    
* **Communication avec les designers** : Maintenez un canal de communication ouvert. Si un détail de Figma n'est pas clair, demandez. Si une réplication s'avère difficile, discutez des alternatives. Utilisez des outils comme Slack, Discord ou des plateformes de gestion de projet pour partager les progrès et clarifier les exigences.
    
* **Plugins/Intégrations Figma** : Explorez les plugins Figma qui pourraient aider les développeurs (par exemple, extraire des extraits de code CSS/Flutter, bien que souvent ceux-ci ne soient que des points de départ).
    

## Gestion des cas limites et des données dynamiques

**Pourquoi c'est important :** Les designs montrent souvent des états idéaux. Les applications réelles ont des données variables, des états vides et des états de chargement.

**Conseils pratiques :**

* **États vides** : Répliquez tous les designs d'"états vides" de Figma (par exemple, panier d'achat vide, aucun résultat de recherche).
    
* **États de chargement** : À quoi ressemble l'UI lorsque les données sont en cours de récupération (par exemple, squelettes, indicateurs de chargement) ?
    
* **États d'erreur** : Que se passe-t-il si un appel API échoue ou si des erreurs de validation d'entrée se produisent ? Assurez-vous que ceux-ci sont conçus et répliqués.
    
* **Contenu dynamique** : Considérez comment les longueurs de texte variables (noms courts vs longs), les rapports d'aspect des images à partir de données réelles, ou les listes avec beaucoup/peu d'éléments affecteront votre mise en page. Testez avec des données diverses.
    

## Implémenter des vecteurs et des icônes avec une scalabilité : Atteindre une cohérence visuelle sur toutes les résolutions

La rasterisation des icônes ou des formes vectorielles complexes est une erreur courante qui conduit à un flou sur différentes densités d'écran. Adoptez les graphiques vectoriels et assurez-vous d'utiliser les **icônes exactes** spécifiées dans le design.

* **Vérification de la source exacte des icônes :**
    
    * **Panneau d'inspection Figma :** Pour chaque icône, vérifiez méticuleusement le panneau "Inspect" dans Figma. Indique-t-il une police d'icônes spécifique (par exemple, Material Icons, Font Awesome), un SVG personnalisé ou une image raster ?
        
    * **Documentation du système de design :** Consultez la documentation du système de design (si disponible) pour l'ensemble d'icônes prescrit et la manière dont elles doivent être implémentées.
        
* **Icônes SVG (Préférées pour les icônes personnalisées) :**
    
    * **Exportation depuis Figma :** Exportez toujours les icônes personnalisées ou uniques depuis Figma en tant que SVGs. Ce format garantit qu'elles s'adaptent sans pixelisation.
        
    * **Intégration Flutter :** Utilisez le package `flutter_svg` (ajoutez `flutter_svg: ^x.x.x` à votre `pubspec.yaml`).
        
        ```dart
        import 'package:flutter_svg/flutter_svg.dart';
        // ...
        SvgPicture.asset(
          'assets/icons/my_custom_icon.svg',
          width: 24.0, // Faites correspondre la taille exacte de Figma pour la mise en page initiale
          height: 24.0,
          colorFilter: ColorFilter.mode(Colors.black, BlendMode.srcIn), // Faites correspondre la couleur de l'icône si nécessaire
        );
        ```
        
* **Polices d'icônes (Préférées pour les ensembles standard) :**
    
    * **Identifier la police :** Si Figma utilise une police d'icônes standard comme Material Icons, Cupertino Icons ou Font Awesome, assurez-vous d'utiliser la bonne.
        
    * **Icônes Material/Cupertino :** Pour les icônes intégrées de Flutter, utilisez simplement le widget `Icon` avec la constante appropriée :
        
        ```dart
        Icon(
          Icons.arrow_back,
          size: 24.0, // Faites correspondre la taille exacte de Figma
          color: Colors.blue, // Faites correspondre la couleur exacte de Figma
        );
        ```
        
    * **Polices d'icônes personnalisées (par exemple, Font Awesome, icônes de marque personnalisées) :**
        
        1. **Obtenir les fichiers de police :** Obtenez le(s) fichier(s) `.ttf` de police auprès de votre designer ou du fournisseur de polices d'icônes.
            
        2. **Ajouter à** `pubspec.yaml`:
            
            ```yaml
            flutter:
              fonts:
                - family: MyCustomIcons
                  fonts:
                    - asset: assets/fonts/MyCustomIcons.ttf
            ```
            
        3. **Référence dans le code :** Créez une classe `static const IconData` ou utilisez le constructeur direct `Icon`:
            
            ```dart
            import 'package:flutter/material.dart';
            
            class MyCustomIcons {
              MyCustomIcons._(); // Constructeur privé
            
              static const IconData home = IconData(0xe900, fontFamily: 'MyCustomIcons');
              static const IconData settings = IconData(0xe901, fontFamily: 'MyCustomIcons');
              // ... map other icons using their Unicode code points from the font
            }
            
            // Usage:
            Icon(MyCustomIcons.home, size: 24.0, color: Colors.red);
            ```
            
* `CustomPaint` (Pour les formes complexes et uniques) :
    
    * **Traduction du chemin vectoriel :** Si l'icône est une illustration très personnalisée et unique qui ne peut pas être facilement exportée en tant que SVG simple ou fait partie d'un graphique complexe plus large, vous devrez peut-être traduire ses chemins vectoriels de Figma en un objet `Path` en utilisant `CustomPainter`. C'est le niveau le plus granulaire de réplication d'icônes.
        
* **Éviter les icônes rasterisées :** Sauf si une icône est intrinsèquement une photographie ou une image raster complexe, **ne jamais exporter les icônes en PNG ou JPG** car elles se pixeliseront lorsqu'elles seront mises à l'échelle ou vues sur des écrans haute densité.
    

## Auto-correction et apprentissage des erreurs

**Pourquoi c'est important :** La meilleure façon de s'améliorer est de réfléchir à ce qui a mal tourné et pourquoi.

**Conseils pratiques :**

* **Documenter les défis :** Lorsque vous rencontrez une réplication particulièrement délicate, documentez le problème, les détails de Figma et comment vous l'avez finalement résolu. Cela construit votre base de connaissances.
    
* **Refactoriser régulièrement :** À mesure que vous apprenez de nouvelles techniques Flutter ou découvrez des moyens plus efficaces de structurer votre UI, n'ayez pas peur de refactoriser le code existant pour appliquer ces améliorations.
    
* **Rester à jour :** Flutter et Figma évoluent constamment. Gardez un œil sur les nouvelles fonctionnalités, widgets et meilleures pratiques qui peuvent rendre votre processus de réplication plus fluide.
    

Pour combler le fossé entre la théorie et la pratique, nous allons construire une application Flutter complète qui reproduit les trois designs d'UI distincts présentés ci-dessous. J'ai obtenu cette image de [Envato](https://elements.envato.com/learn/top-10-ui-templates-for-figma-and-adobe-xd). Ce projet ne consiste pas seulement à copier, il s'agit d'une démonstration pratique de chaque principe que nous avons discuté, de la dissection des valeurs du panneau "Inspect" de Figma à la mise en œuvre d'une structure de composants robuste, scalable et pixel-perfect.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1754566726914/6ef84737-9847-428a-bd7a-bc9f877c774e.png align="center")

Ce que nous allons construire :

1. Un tableau de bord de maison intelligente : En mettant l'accent sur la mise en page, BoxDecoration et une hiérarchie d'informations claire.
    
2. Une interface utilisateur de lecteur de musique : Mettant en avant l'utilisation de Stack pour des mises en page complexes et superposées et des éléments de liste personnalisés.
    
3. Une application de réservation d'appartements : Démontrant PageView pour créer des carrousels interactifs et une barre de navigation inférieure personnalisée avec un FloatingActionButton.
    

Cet exemple pratique consolidera votre compréhension et servira de référence pour vos propres projets. Plongeons dans le code.

## Aperçu du projet

Ce projet est construit en suivant les principes fondamentaux d'une application Flutter scalable et maintenable. Nous ne nous contentons pas de reproduire l'UI, nous l'architectons correctement.

**Guide :**

1. **Composants :** Chaque partie logique de l'UI (un en-tête, une carte, un bouton) est isolée dans son propre fichier de widget. Cela rend le code lisible, réutilisable et facile à tester.
    
2. **Séparation des préoccupations :** Les fichiers "Screen" sont responsables de la mise en page globale et de la gestion de l'état. Les fichiers "Widget" sont responsables uniquement de leur propre apparence et de leur logique interne.
    
3. **Système de design centralisé :** Toutes les couleurs, dimensions et styles de texte sont définis dans des fichiers d'utilitaires centraux (`utils/`), reflétant le concept de "Design Tokens" dans Figma.
    

### **Structure finale du répertoire du projet**

Voici la structure de fichiers propre et organisée que nous allons construire. C'est la norme professionnelle pour les projets Flutter.

```yaml
lib/
├── main.dart
|
├── models/
│   └── track_model.dart
|
├── screens/
│   ├── home_dashboard_screen.dart
│   ├── smart_home_screen.dart
│   ├── music_player_screen.dart
│   └── apartment_booking_screen.dart
|
├── utils/
│   ├── app_colors.dart
│   ├── app_dimensions.dart
│   └── app_styles.dart
|
└── widgets/
    ├── app_mockup_frame.dart
    ├── smart_home/
    │   ├── power_usage_card.dart
    │   ├── remote_access_card.dart
    │   ├── room_card.dart
    │   └── smart_home_header.dart
    ├── music_player/
    │   ├── artist_card.dart
    │   ├── music_player_header.dart
    │   ├── track_list.dart
    │   └── track_list_item.dart
    └── apartment_booking/
        ├── apartment_card.dart
        ├── apartment_carousel.dart
        ├── booking_bottom_nav.dart
        ├── booking_header.dart
        └── booking_search.dart
```

### **Implémentation du code étape par étape**

Voici le code complet pour chaque fichier, avec des explications.

### **1\.** `pubspec.yaml`

Tout d'abord, assurez-vous que votre `pubspec.yaml` inclut le package `google_fonts` pour correspondre à la typographie.

```yaml
name: figma_replication_project
description: Un nouveau projet Flutter.
publish_to: 'none'

version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  google_fonts: ^6.1.0 # Pour des polices personnalisées de haute qualité

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
```

### **2\. Utilitaires (**`lib/utils/`)

Ce répertoire centralise notre système de design, démontrant parfaitement les principes de "Design Tokens" et "Consistent Spacing" de votre article.

#### `lib/utils/app_colors.dart`

```dart
import 'package:flutter/material.dart';

// Centralise toutes les couleurs de l'application pour la cohérence et le thème facile.
class AppColors {
  static const Color background = Color(0xFFFFD1B5);
  static const Color primaryBlue = Color(0xFF3D82F8);
  static const Color lightBlue = Color(0xFFD2E2FF);
  static const Color textDark = Color(0xFF2E3A59);
  static const Color textLight = Color(0xFF8F9BB3);
  static const Color cardBackground = Colors.white;
}
```

#### `lib/utils/app_dimensions.dart`

```dart
// Centralise toutes les valeurs d'espacement et de dimensionnement pour maintenir un rythme visuel cohérent.
class AppDimensions {
  static const double spacingXXSmall = 4.0;
  static const double spacingXSmall = 8.0;
  static const double spacingSmall = 12.0;
  static const double spacingMedium = 16.0;
  static const double spacingLarge = 24.0;
  static const double spacingXLarge = 32.0;

  static const double borderRadiusSmall = 8.0;
  static const double borderRadiusMedium = 16.0;
  static const double borderRadiusLarge = 24.0;
  
  static const double mockupWidth = 320.0;
  static const double mockupHeight = 680.0;
}
```

#### `lib/utils/app_styles.dart`

```dart
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'app_colors.dart';
import 'app_dimensions.dart';

// Centralise les styles de texte et les éléments de décoration communs comme les ombres.
// Cela garantit une fidélité absolue aux spécifications de typographie de Figma.
class AppStyles {
  // Style de texte de base utilisant une Google Font spécifique pour un look moderne.
  static TextStyle get _baseTextStyle => GoogleFonts.poppins(
        color: AppColors.textDark,
      );

  // Styles de texte spécifiques et nommés qui correspondent au design de Figma.
  static TextStyle h1 = _baseTextStyle.copyWith(fontSize: 22, fontWeight: FontWeight.w600);
  static TextStyle h2 = _baseTextStyle.copyWith(fontSize: 18, fontWeight: FontWeight.w600);
  static TextStyle bodyText = _baseTextStyle.copyWith(fontSize: 14, fontWeight: FontWeight.w500);
  static TextStyle subtitle = _baseTextStyle.copyWith(fontSize: 12, color: AppColors.textLight, fontWeight: FontWeight.normal);
  static TextStyle buttonText = _baseTextStyle.copyWith(fontSize: 14, color: Colors.white, fontWeight: FontWeight.w600);

  // Ombre de boîte réutilisable, correspondant exactement aux propriétés de Figma.
  static BoxShadow cardShadow = BoxShadow(
    color: AppColors.primaryBlue.withOpacity(0.1),
    blurRadius: 20,
    offset: const Offset(0, 10),
  );
}
```

### **3\. Modèle (**`lib/models/`)

Cela contient la structure de données pour le contenu de notre application, séparant les données de l'UI.

#### `lib/models/track_model.dart`

```dart
// Représente la structure de données pour une seule piste musicale.
class Track {
  final String title;
  final String duration;
  final bool isPlaying;

  Track({required this.title, required this.duration, this.isPlaying = false});
}

// Données fictives pour l'écran du lecteur de musique.
final List<Track> topTracks = [
  Track(title: 'Old Town Road', duration: '3:41'),
  Track(title: 'I Don\'t Care', duration: '4:35', isPlaying: true),
  Track(title: 'Dancing With A Stranger', duration: '3:12'),
  Track(title: 'Sweet But Psycho', duration: '4:07'),
  Track(title: 'If I Can\'t Have You', duration: '4:07'),
];
```

### **4\. Widgets réutilisables (**`lib/widgets/`)

C'est le cœur de notre architecture basée sur les composants.

#### **Widget générique**

#### `lib/widgets/app_mockup_frame.dart`

```dart
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:flutter/material.dart';

// Un widget wrapper pour créer le "cadre de téléphone" autour de chaque design d'UI.
class AppMockupFrame extends StatelessWidget {
  final Widget child;

  const AppMockupFrame({Key? key, required this.child}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: AppDimensions.mockupWidth,
      height: AppDimensions.mockupHeight,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(AppDimensions.borderRadiusLarge),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.15),
            blurRadius: 30,
            offset: const Offset(0, 10),
          ),
        ],
        border: Border.all(color: Colors.white.withOpacity(0.5), width: 2),
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(AppDimensions.borderRadiusLarge - 2),
        child: child,
      ),
    );
  }
}
```

#### **Widgets Smart Home (**`lib/widgets/smart_home/`)

Chaque fichier ici est un composant autonome pour l'écran Smart Home.

`lib/widgets/smart_home/smart_home_header.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

class SmartHomeHeader extends StatelessWidget {
  const SmartHomeHeader({Key? key}) : super(key: key);
  // ... (code de la réponse précédente)
}
```

`lib/widgets/smart_home/power_usage_card.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

class PowerUsageCard extends StatelessWidget {
  const PowerUsageCard({Key? key}) : super(key: key);
  // ... (code de la réponse précédente)
}
```

`lib/widgets/smart_home/room_card.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

class RoomCard extends StatelessWidget {
  final String roomName;
  final String deviceCount;
  final Color color;
  final Color textColor;

  const RoomCard({
    Key? key,
    required this.roomName,
    required this.deviceCount,
    required this.color,
    required this.textColor,
  }) : super(key: key);
  // ... (code de la réponse précédente)
}
```

`lib/widgets/smart_home/remote_access_card.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

class RemoteAccessCard extends StatelessWidget {
  const RemoteAccessCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(
        horizontal: AppDimensions.spacingMedium,
        vertical: AppDimensions.spacingSmall,
      ),
      decoration: BoxDecoration(
        color: AppColors.primaryBlue,
        borderRadius: BorderRadius.circular(AppDimensions.borderRadiusMedium),
      ),
      child: Row(
        children: [
          const Icon(Icons.info_outline, color: Colors.white, size: 20),
          const SizedBox(width: AppDimensions.spacingSmall),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Quick Remote Access',
                    style: AppStyles.bodyText.copyWith(color: Colors.white)),
                Text(
                  'Click here to connect with your phone.',
                  style: AppStyles.subtitle
                      .copyWith(color: Colors.white.withOpacity(0.8), fontSize: 10),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
```

### **Widgets du lecteur de musique (**`lib/widgets/music_player/`)

Ces widgets sont les éléments de base de l'interface utilisateur du lecteur de musique.

#### `lib/widgets/music_player/music_player_header.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';

// Ce widget crée l'en-tête bleu distinctif et courbé.
// Il utilise SafeArea pour s'assurer que le contenu n'est pas obscurci par l'UI système (comme les encoches).
class MusicPlayerHeader extends StatelessWidget {
  const MusicPlayerHeader({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 260,
      decoration: const BoxDecoration(
        color: AppColors.primaryBlue,
        borderRadius: BorderRadius.only(
          bottomLeft: Radius.circular(50),
          bottomRight: Radius.circular(50),
        ),
      ),
      child: SafeArea(
        bottom: false,
        child: Padding(
          padding: const EdgeInsets.all(AppDimensions.spacingLarge),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Icon(Icons.arrow_back, color: Colors.white),
              Container(
                width: 40,
                height: 40,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: AppColors.lightBlue.withOpacity(0.5),
                  border: Border.all(color: Colors.white, width: 1.5),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

#### `lib/widgets/music_player/artist_card.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

// La carte flottante qui affiche les informations sur l'artiste.
// Elle utilise l'ombre centralisée AppStyles.cardShadow pour un effet d'ombre cohérent.
class ArtistCard extends StatelessWidget {
  const ArtistCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(AppDimensions.spacingMedium),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(AppDimensions.borderRadiusMedium),
        boxShadow: [AppStyles.cardShadow],
      ),
      child: Row(
        children: [
          Container(
            width: 80,
            height: 80,
            decoration: BoxDecoration(
              color: AppColors.lightBlue,
              borderRadius: BorderRadius.circular(AppDimensions.borderRadiusSmall),
            ),
          ),
          const SizedBox(width: AppDimensions.spacingMedium),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Antonia Berger', style: AppStyles.h2),
              Text('Hip Hop Artist', style: AppStyles.subtitle),
              Text('antonia.com', style: AppStyles.subtitle.copyWith(color: AppColors.primaryBlue)),
            ],
          )
        ],
      ),
    );
  }
}
```

#### `lib/widgets/music_player/track_list_item.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/models/track_model.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

// Représente une seule ligne dans la liste des pistes musicales.
// Il rend conditionnellement son UI en fonction de la propriété `track.isPlaying`.
class TrackListItem extends StatelessWidget {
  final Track track;
  const TrackListItem({Key? key, required this.track}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: AppDimensions.spacingSmall),
      child: Row(
        children: [
          Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              color: track.isPlaying ? AppColors.primaryBlue : Colors.transparent,
              shape: BoxShape.circle,
              border: Border.all(color: track.isPlaying ? AppColors.primaryBlue : AppColors.textLight.withOpacity(0.5), width: 1.5),
            ),
            child: Icon(
              track.isPlaying ? Icons.pause : Icons.play_arrow,
              color: track.isPlaying ? Colors.white : AppColors.textDark,
              size: 20,
            ),
          ),
          const SizedBox(width: AppDimensions.spacingMedium),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(track.title, style: AppStyles.bodyText),
                if (track.isPlaying)
                  Padding(
                    padding: const EdgeInsets.only(top: 4.0),
                    child: SizedBox(
                      height: 2,
                      child: LinearProgressIndicator(
                        value: 0.4,
                        backgroundColor: AppColors.lightBlue,
                        valueColor: const AlwaysStoppedAnimation<Color>(AppColors.primaryBlue),
                      ),
                    ),
                  ),
              ],
            ),
          ),
          Text(track.duration, style: AppStyles.subtitle),
        ],
      ),
    );
  }
}
```

#### `lib/widgets/music_player/track_list.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/models/track_model.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';
import 'package:figma_replication_project/widgets/music_player/track_list_item.dart';

// Ce widget construit la liste déroulante des pistes.
// Il mappe les données fictives de `topTracks` aux widgets `TrackListItem`.
class TrackList extends StatelessWidget {
  const TrackList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(
        AppDimensions.spacingLarge,
        AppDimensions.spacingLarge,
        AppDimensions.spacingLarge,
        0,
      ),
      children: [
        Text('Top Tracks', style: AppStyles.h2),
        const SizedBox(height: AppDimensions.spacingMedium),
        // Utilisation de l'opérateur de propagation (...) pour ajouter tous les éléments de la liste.
        ...topTracks.map((track) => TrackListItem(track: track)).toList(),
      ],
    );
  }
}
```

### **Widgets de réservation d'appartement (**`lib/widgets/apartment_booking/`)

Ces widgets sont les éléments de base de l'interface utilisateur de réservation d'appartement.

#### `lib/widgets/apartment_booking/booking_header.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

// La section d'en-tête pour l'écran de réservation d'appartement.
class BookingHeader extends StatelessWidget {
  const BookingHeader({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(
        AppDimensions.spacingLarge,
        AppDimensions.spacingMedium,
        AppDimensions.spacingLarge,
        0,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Icon(Icons.arrow_back, color: AppColors.textDark),
              Container(
                width: 40,
                height: 40,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: AppColors.lightBlue.withOpacity(0.5),
                  border: Border.all(color: AppColors.primaryBlue, width: 1.5),
                ),
              ),
            ],
          ),
          const SizedBox(height: AppDimensions.spacingMedium),
          Text('Discover & book', style: AppStyles.h1),
          Text('unique apartments', style: AppStyles.h1),
        ],
      ),
    );
  }
}
```

#### `lib/widgets/apartment_booking/booking_search.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

// Le composant de la barre de recherche avec une puce de suggestion et un bouton de recherche.
class BookingSearch extends StatelessWidget {
  const BookingSearch({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: AppDimensions.spacingLarge),
      child: Row(
        children: [
          Expanded(
            child: Container(
              padding: const EdgeInsets.symmetric(
                horizontal: AppDimensions.spacingMedium,
                vertical: AppDimensions.spacingSmall,
              ),
              decoration: BoxDecoration(
                color: AppColors.primaryBlue,
                borderRadius: BorderRadius.circular(30),
              ),
              child: Center(
                child: Text(
                  'TRY "COPENHAGEN"',
                  style: AppStyles.buttonText.copyWith(fontSize: 12),
                ),
              ),
            ),
          ),
          const SizedBox(width: AppDimensions.spacingSmall),
          Container(
            padding: const EdgeInsets.all(AppDimensions.spacingSmall),
            decoration: const BoxDecoration(
              color: AppColors.primaryBlue,
              shape: BoxShape.circle,
            ),
            child: const Icon(Icons.search, color: Colors.white, size: 24),
          ),
        ],
      ),
    );
  }
}
```

#### `lib/widgets/apartment_booking/apartment_card.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/utils/app_styles.dart';

// Une seule carte représentant un appartement dans le carrousel.
// Elle utilise un Stack pour positionner le texte et le bouton d'envoi.
class ApartmentCard extends StatelessWidget {
  const ApartmentCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: AppColors.lightBlue,
        borderRadius: BorderRadius.circular(AppDimensions.borderRadiusLarge),
        boxShadow: [AppStyles.cardShadow],
      ),
      child: Stack(
        children: [
          Positioned(
            left: AppDimensions.spacingMedium,
            bottom: AppDimensions.spacingMedium,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Tidy Minimal', style: AppStyles.h2),
                Text('Berlin, Germany', style: AppStyles.subtitle),
              ],
            ),
          ),
          Positioned(
            right: AppDimensions.spacingMedium,
            bottom: AppDimensions.spacingMedium,
            child: Container(
              padding: const EdgeInsets.all(AppDimensions.spacingSmall),
              decoration: const BoxDecoration(
                color: AppColors.primaryBlue,
                shape: BoxShape.circle,
              ),
              child: const Icon(Icons.send, color: Colors.white, size: 20, semanticLabel: 'Send'),
            ),
          ),
        ],
      ),
    );
  }
}
```

#### `lib/widgets/apartment_booking/apartment_carousel.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/widgets/apartment_booking/apartment_card.dart';

// Ce widget gère le PageView pour les cartes d'appartement.
// C'est un StatelessWidget car il reçoit son état (contrôleur, page actuelle)
// du widget StatefulWidget parent.
class ApartmentCarousel extends StatelessWidget {
  final PageController pageController;
  final int currentPage;

  const ApartmentCarousel({
    Key? key,
    required this.pageController,
    required this.currentPage,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 320,
      child: PageView.builder(
        controller: pageController,
        itemCount: 3,
        itemBuilder: (context, index) {
          // AnimatedContainer crée l'effet de mise à l'échelle subtil lorsqu'une carte est active.
          return AnimatedContainer(
            duration: const Duration(milliseconds: 300),
            curve: Curves.easeInOut,
            margin: EdgeInsets.only(
              right: AppDimensions.spacingSmall,
              top: currentPage == index ? 0 : 20,
              bottom: currentPage == index ? 20 : 0,
            ),
            child: const ApartmentCard(),
          );
        },
      ),
    );
  }
}
```

#### `lib/widgets/apartment_booking/booking_bottom_nav.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';

// La barre de navigation inférieure personnalisée avec une encoche pour le FloatingActionButton.
class BookingBottomNav extends StatelessWidget {
  const BookingBottomNav({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return BottomAppBar(
      shape: const CircularNotchedRectangle(),
      notchMargin: 8.0,
      color: AppColors.cardBackground,
      surfaceTintColor: AppColors.cardBackground,
      elevation: 20,
      shadowColor: Colors.black.withOpacity(0.05),
      child: const Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          Icon(Icons.home_outlined, color: AppColors.textLight, size: 28),
          Icon(Icons.search, color: AppColors.textLight, size: 28),
          SizedBox(width: 48), // L'espace réservé pour le FAB
          Icon(Icons.favorite_border, color: AppColors.textLight, size: 28),
          Icon(Icons.person_outline, color: AppColors.textLight, size: 28),
        ],
      ),
    );
  }
}
```

### **5\. Écrans (**`lib/screens/`)

Ces fichiers agissent maintenant comme des plans propres et lisibles. Ils composent les widgets plus petits pour construire l'UI finale.

#### `lib/screens/smart_home_screen.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/widgets/smart_home/power_usage_card.dart';
import 'package:figma_replication_project/widgets/smart_home/remote_access_card.dart';
import 'package:figma_replication_project/widgets/smart_home/room_card.dart';
import 'package:figma_replication_project/widgets/smart_home/smart_home_header.dart';

// Cet écran compose divers widgets "smart_home" pour construire l'UI.
// Remarquez à quel point cela est lisible par rapport à avoir tout le code dans un seul fichier.
class SmartHomeScreen extends StatelessWidget {
  const SmartHomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.cardBackground,
      body: Padding(
        padding: const EdgeInsets.all(AppDimensions.spacingLarge),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SmartHomeHeader(),
            const SizedBox(height: AppDimensions.spacingXLarge),
            const PowerUsageCard(),
            const SizedBox(height: AppDimensions.spacingLarge),
            const Row(
              children: [
                Expanded(
                  child: RoomCard(
                    roomName: 'Living Room',
                    deviceCount: '9 Active Devices',
                    color: AppColors.lightBlue,
                    textColor: AppColors.textDark,
                  ),
                ),
                SizedBox(width: AppDimensions.spacingMedium),
                Expanded(
                  child: RoomCard(
                    roomName: 'Bathroom',
                    deviceCount: '1 Active Device',
                    color: AppColors.primaryBlue,
                    textColor: Colors.white,
                  ),
                ),
              ],
            ),
            const Spacer(),
            const RemoteAccessCard(),
          ],
        ),
      ),
    );
  }
}
```

#### `lib/screens/music_player_screen.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/widgets/music_player/artist_card.dart';
import 'package:figma_replication_project/widgets/music_player/music_player_header.dart';
import 'package:figma_replication_project/widgets/music_player/track_list.dart';

// Cet écran utilise un Stack pour créer l'effet de superposition de l'UI,
// une démonstration parfaite du principe "Déconstruire les mises en page avec Stack".
class MusicPlayerScreen extends StatelessWidget {
  const MusicPlayerScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.cardBackground,
      body: Stack(
        children: [
          const Positioned.fill(top: 220, child: TrackList()),
          const MusicPlayerHeader(),
          const Positioned(
            top: 120,
            left: AppDimensions.spacingLarge,
            right: AppDimensions.spacingLarge,
            child: ArtistCard(),
          ),
        ],
      ),
    );
  }
}
```

#### `lib/screens/apartment_booking_screen.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/utils/app_colors.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/widgets/apartment_booking/apartment_carousel.dart';
import 'package:figma_replication_project/widgets/apartment_booking/booking_bottom_nav.dart';
import 'package:figma_replication_project/widgets/apartment_booking/booking_header.dart';
import 'package:figma_replication_project/widgets/apartment_booking/booking_search.dart';

// Il s'agit d'un StatefulWidget car il doit gérer l'état du
// PageController et l'index de la page active pour l'animation du carrousel.
class ApartmentBookingScreen extends StatefulWidget {
  const ApartmentBookingScreen({Key? key}) : super(key: key);

  @override
  State<ApartmentBookingScreen> createState() => _ApartmentBookingScreenState();
}

class _ApartmentBookingScreenState extends State<ApartmentBookingScreen> {
  final PageController _pageController = PageController(viewportFraction: 0.85);
  int _currentPage = 0;

  @override
  void initState() {
    super.initState();
    // Écoutez les changements de page pour mettre à jour l'UI pour l'effet de mise à l'échelle.
    _pageController.addListener(() {
      if (_pageController.page?.round() != _currentPage) {
        setState(() {
          _currentPage = _pageController.page!.round();
        });
      }
    });
  }

  @override
  void dispose() {
    _pageController.dispose(); // Toujours disposer des contrôleurs pour éviter les fuites de mémoire.
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.cardBackground,
      body: SafeArea(
        bottom: false,
        child: Column(
          children: [
            const BookingHeader(),
            const SizedBox(height: AppDimensions.spacingMedium),
            const BookingSearch(),
            const SizedBox(height: AppDimensions.spacingLarge),
            // Le carrousel reçoit le contrôleur et l'état de la page actuelle.
            ApartmentCarousel(
              pageController: _pageController,
              currentPage: _currentPage,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        backgroundColor: AppColors.primaryBlue,
        shape: const CircleBorder(),
        elevation: 4.0,
        child: const Icon(Icons.add, color: Colors.white, size: 32),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      bottomNavigationBar: const BookingBottomNav(),
    );
  }
}
```

### **6\. Point d'entrée de l'application**

Enfin, le `main.dart` et `home_dashboard_screen.dart` rassemblent tout.

#### `lib/screens/home_dashboard_screen.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/screens/apartment_booking_screen.dart';
import 'package:figma_replication_project/screens/music_player_screen.dart';
import 'package:figma_replication_project/screens/smart_home_screen.dart';
import 'package:figma_replication_project/utils/app_dimensions.dart';
import 'package:figma_replication_project/widgets/app_mockup_frame.dart';

// Il s'agit de l'écran principal qui affiche les trois maquettes.
// Il utilise un LayoutBuilder pour créer une mise en page réactive, démontrant
// le principe "Embrasser les contraintes et la réactivité".
class HomeDashboardScreen extends StatelessWidget {
  const HomeDashboardScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: AppDimensions.spacingXLarge),
            child: LayoutBuilder(
              builder: (context, constraints) {
                bool isWide = constraints.maxWidth > (AppDimensions.mockupWidth * 3 + 100);
                
                // Afficher en Row sur les écrans larges, et en Column sur les écrans étroits.
                return isWide
                    ? const Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          AppMockupFrame(child: SmartHomeScreen()),
                          SizedBox(width: AppDimensions.spacingXLarge),
                          AppMockupFrame(child: MusicPlayerScreen()),
                          SizedBox(width: AppDimensions.spacingXLarge),
                          AppMockupFrame(child: ApartmentBookingScreen()),
                        ],
                      )
                    : Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const AppMockupFrame(child: SmartHomeScreen()),
                          const SizedBox(height: AppDimensions.spacingXLarge),
                          const AppMockupFrame(child: MusicPlayerScreen()),
                          const SizedBox(height: AppDimensions.spacingXLarge),
                          const AppMockupFrame(child: ApartmentBookingScreen()),
                        ],
                      );
              },
            ),
          ),
        ),
      ),
    );
  }
}
```

#### `lib/main.dart`

```dart
import 'package:flutter/material.dart';
import 'package:figma_replication_project/screens/home_dashboard_screen.dart';
import 'package:figma_replication_project/utils/app_colors.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Figma to Flutter Replication',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primaryColor: AppColors.primaryBlue,
        scaffoldBackgroundColor: AppColors.background,
        useMaterial3: true,
      ),
      home: const HomeDashboardScreen(),
    );
  }
}
```

## Conclusion

La réplication des designs Figma dans Flutter avec une précision pixel-perfect est une compétence développée par la pratique délibérée et un engagement inébranlable envers les détails. Cela nécessite plus que la simple compréhension des widgets Flutter. Cela exige une profonde appréciation des nuances du design, une approche systématique pour décomposer les mises en page complexes et une quête implacable de la fidélité visuelle. En internalisant ces pratiques, vous ne serez pas seulement en train d'écrire du code, vous serez en train de sculpter des interfaces utilisateur qui honorent vraiment la vision du designer.