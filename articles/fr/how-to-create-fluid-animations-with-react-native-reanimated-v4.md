---
title: Comment créer des animations fluides avec React Native Reanimated v4
subtitle: ''
author: Balogun Wahab
co_authors: []
series: null
date: '2025-11-17T15:26:35.718Z'
originalURL: https://freecodecamp.org/news/how-to-create-fluid-animations-with-react-native-reanimated-v4
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1763052228638/4416e81d-b76e-4c40-987e-0aff1d82ff7b.png
tags:
- name: React Native
  slug: react-native
- name: React
  slug: reactjs
- name: react native reanimated
  slug: react-native-reanimated
- name: animation
  slug: animation
- name: JavaScript
  slug: javascript
seo_title: Comment créer des animations fluides avec React Native Reanimated v4
seo_desc: Reanimated 4 brings Cascading Style Sheets (CSS) animations to React Native
  while keeping full backward compatibility with its worklet-based API. You can now
  build 60+ frames-per-second (FPS) animations using familiar web syntax, or drop
  down to work...
---

Reanimated 4 apporte les animations Cascading Style Sheets (CSS) à React Native tout en conservant une rétrocompatibilité totale avec son API basée sur les worklets. Vous pouvez désormais créer des animations à plus de 60 images par seconde (FPS) en utilisant une syntaxe web familière, ou descendre au niveau des worklets pour les interactions pilotées par des gestes.

La bibliothèque nécessite la Nouvelle Architecture de React Native (Fabric), vous aurez donc besoin de la version 0.76 ou plus récente.

Dans ce tutoriel, vous apprendrez :

* Comment utiliser les transitions CSS pour les animations pilotées par l'état
    
* Quand utiliser les worklets pour les interactions de gestes et de défilement
    
* Comment migrer de Reanimated 3 vers la version 4
    
* Des modèles pratiques pour les en-têtes rétractables, les bottom sheets et les carrousels
    
* Des techniques d'optimisation de performance
    

### Prérequis

Vous devriez avoir :

* React Native 0.76+ avec la Nouvelle Architecture activée
    
* Des connaissances de base sur les hooks React (useState, useEffect)
    
* Node.js et npm ou yarn installés
    

## Table des matières

* [Installation et Configuration](#heading-installation-et-configuration)
    
* [Comprendre les deux approches (Animations CSS et Worklets)](#heading-comprendre-les-deux-approches)
    
* [Comment migrer de Reanimated Version 3 vers la Version 4](#heading-comment-migrer-de-reanimated-version-3-vers-la-version-4)
    
* [Tutoriel sur les animations CSS](#heading-tutoriel-sur-les-animations-css)
    
* [Tutoriel sur les Worklets](#heading-tutoriel-sur-les-worklets)
    
* [Modèles du monde réel](#heading-modeles-du-monde-reel)
    
* [Optimisations de performance](#heading-optimisations-de-performance)
    
* [Conseils de débogage](#heading-conseils-de-debogage)
    
* [Conclusion](#heading-conclusion)
    

## Installation et Configuration

Pour commencer, vous devrez installer les packages requis :

```bash
# Pour Expo
npx expo install react-native-reanimated react-native-worklets

# Pour React Native CLI  
npm install react-native-reanimated react-native-worklets
cd ios && pod install && cd ..
```

Mettez à jour `babel.config.js` (le plugin doit être en dernier) :

```javascript
module.exports = {
  presets: ['module:metro-react-native-babel-preset'],
  plugins: [
    'react-native-worklets/plugin', // Doit être en dernier
  ],
};
```

Ensuite, effacez le cache et reconstruisez :

```bash
npm start -- --reset-cache
npx react-native run-ios
```

## Comprendre les deux approches

React Native Reanimated est une bibliothèque d'animation qui exécute les animations sur le thread natif au lieu du thread JavaScript. Cela signifie que vos animations restent fluides même lorsque votre code JavaScript est occupé à traiter des données ou à gérer des interactions utilisateur.

Contrairement à l'API Animated intégrée de React Native, Reanimated exécute la logique d'animation directement sur le thread UI. Cela élimine le goulot d'étranglement de performance causé par la communication entre JavaScript et le code natif, ce qui permet à Reanimated de maintenir 60 FPS même lors d'opérations complexes.

Reanimated 4 propose deux systèmes d'animation, chacun conçu pour des cas d'utilisation différents.

### Animations CSS

Les animations CSS fonctionnent de manière déclarative, ce qui signifie que vous décrivez ce que vous voulez qu'il se passe plutôt que comment le faire. Vous définissez quelles propriétés doivent être animées (comme la largeur, la couleur ou l'opacité), spécifiez le timing et l'easing, puis changez simplement les valeurs via les mises à jour d'état React. Reanimated gère automatiquement l'animation entre l'ancienne et la nouvelle valeur.

Cette approche excelle pour les animations prévisibles et pilotées par l'état où vous connaissez à la fois l'état de départ et l'état de fin. Elle est idéale pour :

* Afficher et masquer des éléments d'interface (modales, info-bulles, notifications)
    
* Développer et réduire du contenu (accordéons, menus déroulants)
    
* Retour visuel pour les changements d'état (effets de survol de bouton, mise en évidence de sélection)
    
* Indicateurs de chargement et animations de progression
    
* Transitions de couleur et d'opacité
    

### Worklets

Les Worklets adoptent une approche différente en vous donnant un contrôle impératif, image par image, sur les animations. Ils s'exécutent sur le thread UI et utilisent des "shared values" – des variables spéciales qui peuvent être consultées et modifiées à la fois depuis JavaScript et le code natif sans aucun surcoût de communication.

Les Worklets sont essentiels pour les animations interactives qui doivent répondre en temps réel aux entrées de l'utilisateur ou aux flux de données continus. Ils sont parfaits pour :

* Interactions pilotées par les gestes (glisser-déposer, balayer pour fermer, pincer pour zoomer)
    
* Effets liés au défilement (images parallaxe, en-têtes rétractables, éléments collants)
    
* Animations basées sur la physique (effets de ressort, défilement par inertie)
    
* Animations basées sur les capteurs (réponse à l'orientation de l'appareil)
    
* Toute animation nécessitant un contrôle dynamique en temps réel
    

Maintenant que vous comprenez les deux approches proposées par Reanimated, voyons comment migrer depuis la version 3 si vous utilisez déjà la bibliothèque.

## Comment migrer de Reanimated Version 3 vers la Version 4

Si vous utilisez actuellement Reanimated 3, vous serez heureux d'apprendre que la version 4 maintient la rétrocompatibilité. Vos animations existantes utilisant des worklets, des shared values et `useAnimatedStyle` continueront de fonctionner sans modification.

Mais la version 4 introduit certains changements architecturaux et supprime des API obsolètes, vous devrez donc effectuer quelques mises à jour de la configuration de votre projet et de votre code. Passons en revue le processus de migration étape par étape.

### Ce qui a changé dans la Version 4

Le changement le plus significatif est que les worklets ont été extraits dans un package séparé appelé `react-native-worklets-core`. Cette approche modulaire permet à d'autres bibliothèques au-delà de Reanimated de tirer parti des fonctionnalités de worklet.

En raison de cette séparation, vous devrez mettre à jour votre configuration Babel. Changez le plugin de `react-native-reanimated/plugin` à `react-native-worklets/plugin`.

La version 4 prend également en charge exclusivement la Nouvelle Architecture de React Native (Fabric). L'ancien moteur de rendu Paper n'est plus compatible. Si votre projet n'a pas encore migré vers la Nouvelle Architecture, vous devrez soit passer à React Native 0.76+ (où la Nouvelle Architecture est activée par défaut), soit rester sur Reanimated 3.x jusqu'à ce que vous soyez prêt à effectuer cette transition.

### API supprimées

Plusieurs API qui étaient obsolètes dans la version 3 ont été supprimées dans la version 4. Voici ce que vous devez remplacer :

* `useAnimatedGestureHandler` → Utilisez l'API `Gesture` de react-native-gesture-handler 2.x à la place
    
* `useWorkletCallback` → Utilisez `useCallback` avec la directive `'worklet'`
    
* `combineTransition` → Utilisez `EntryExitTransition.entering().exiting()`
    

Le hook `useScrollViewOffset` a été renommé en `useScrollOffset`. L'ancien nom fonctionne toujours mais est obsolète, mettez donc à jour votre code pour utiliser le nouveau nom.

### Changement de configuration du ressort (Spring)

La configuration de l'animation par ressort a changé pour paraître plus naturelle. Le paramètre `duration` représente désormais la "durée perceptuelle" plutôt que des millisecondes exactes. L'animation réelle dure environ 1,5 fois plus longtemps que la durée spécifiée, créant des ressorts qui semblent plus organiques et moins mécaniques.

```javascript
// Version 3
withSpring(100, { duration: 300 }) // S'exécute pendant exactement 300ms

// Version 4  
withSpring(100, { duration: 200 }) // S'exécute pendant environ 300ms
```

Si vous devez maintenir le timing exact de la version 3, divisez vos valeurs de durée par 1,5.

### Processus de migration étape par étape

Voici comment migrer votre projet de Reanimated 3 vers la version 4 :

**Étape 1 :** Vérifiez que votre projet utilise React Native 0.76 ou plus récent avec la Nouvelle Architecture activée. Vérifiez votre Podfile iOS pour `ENV['RCT_NEW_ARCH_ENABLED'] = '1'` et votre gradle.properties Android pour `newArchEnabled=true`.

**Étape 2 :** Installez les nouvelles versions de Reanimated et du package worklets :

```bash
npm install react-native-reanimated@^4.1.0 react-native-worklets@^0.5.0
```

**Étape 3 :** Mettez à jour votre `babel.config.js` pour utiliser le nouveau plugin worklets :

```javascript
module.exports = {
  plugins: [
    'react-native-worklets/plugin', // Changé depuis react-native-reanimated/plugin
  ],
};
```

**Étape 4 :** Recherchez dans votre code les API supprimées et remplacez-les :

* Remplacez `useAnimatedGestureHandler` par l'API `Gesture`
    
* Remplacez `useWorkletCallback` par `useCallback` et ajoutez la directive `'worklet'`
    
* Remplacez `combineTransition` par `EntryExitTransition.entering().exiting()`
    
* Renommez `useScrollViewOffset` en `useScrollOffset`
    

**Étape 5 :** Reconstruisez vos applications natives :

```bash
cd ios && pod install && cd ..
npx react-native run-ios
# ou pour Android
npx react-native run-android
```

Après avoir terminé ces étapes, votre application devrait fonctionner sur Reanimated 4 avec toutes vos animations existantes fonctionnant comme avant. Vous êtes maintenant prêt à commencer à utiliser les nouvelles fonctionnalités d'animation CSS aux côtés de vos animations basées sur les worklets existantes. Dans la section suivante, vous apprendrez à créer des animations en utilisant la syntaxe CSS.

## Tutoriel sur les animations CSS

Les animations CSS offrent un moyen propre et déclaratif de gérer les transitions déclenchées par des changements d'état. Au lieu de gérer manuellement les valeurs d'animation, vous déclarez simplement quelles propriétés doivent être animées et comment, puis vous mettez à jour l'état de votre composant – Reanimated s'occupe du reste.

Cette approche est particulièrement puissante pour les animations dont vous connaissez les états de début et de fin à l'avance. C'est parfait pour les éléments d'interface qui basculent entre différents états visuels, comme des modales qui apparaissent et disparaissent, des boutons fournissant un retour lors de la pression, ou du contenu qui se développe et se réduit.

### Transitions de base

Une transition anime le changement entre deux valeurs de propriété. Lorsque vous spécifiez une propriété qui doit faire l'objet d'une transition, Reanimated interpole automatiquement entre l'ancienne et la nouvelle valeur sur la durée spécifiée.

Regardons une carte extensible qui s'agrandit lorsqu'on appuie dessus :

```javascript
import React, { useState } from 'react';
import { Pressable, Text } from 'react-native';
import Animated from 'react-native-reanimated';

function ExpandableCard() {
  const [expanded, setExpanded] = useState(false);
  
  return (
    <Pressable onPress={() => setExpanded(!expanded)}>
      <Animated.View style={{
        width: expanded ? 300 : 200,
        height: expanded ? 200 : 100,
        backgroundColor: expanded ? '#4ade80' : '#86efac',
        transitionProperty: ['width', 'height', 'backgroundColor'],
        transitionDuration: 300,
        transitionTimingFunction: 'ease-in-out',
      }}>
        <Text>Tap to toggle</Text>
      </Animated.View>
    </Pressable>
  );
}
```

Voici ce qui se passe : la largeur, la hauteur et la couleur d'arrière-plan de la carte sont contrôlées par l'état `expanded`. Le tableau `transitionProperty` indique à Reanimated quelles propriétés animer. Lorsque `expanded` change, Reanimated anime en douceur des valeurs actuelles vers les nouvelles valeurs sur 300 millisecondes, en utilisant une fonction de timing ease-in-out qui commence lentement, accélère, puis ralentit à nouveau.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762274975831/7e25aa04-24b8-43eb-9db0-a3c088c44132.gif align="center")

### Animations par images clés (Keyframes)

Alors que les transitions gèrent les changements entre deux états, les animations par images clés vous permettent de définir des séquences en plusieurs étapes avec un contrôle précis sur chaque étape. Vous créez un objet où chaque clé représente un pourcentage de la chronologie de l'animation, et la valeur définit à quoi les propriétés doivent ressembler à ce moment-là.

Voici un badge pulsé qui s'agrandit et s'estompe légèrement, puis revient à la normale :

```javascript
const pulseAnimation = {
  '0%': { scale: 1, opacity: 1 },
  '50%': { scale: 1.05, opacity: 0.8 },
  '100%': { scale: 1, opacity: 1 },
};

function PulsingBadge() {
  return (
    <Animated.View style={{
      width: 50,
      height: 50,
      borderRadius: 25,
      backgroundColor: '#ef4444',
      animationName: pulseAnimation,
      animationDuration: 2000,
      animationIterationCount: 'infinite',
    }} />
  );
}
```

L'animation commence à 0% (taille et opacité normales), s'agrandit et s'estompe à la marque des 50%, puis revient à l'état d'origine à 100%. En réglant `animationIterationCount` sur 'infinite', l'animation boucle continuellement. Cela crée l'effet de pulsation que l'on voit souvent sur les badges de notification ou les indicateurs en direct.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762274903470/d10d856f-03b8-4d6c-b616-22cbea3434c2.gif align="center")

### Animations intégrées

Reanimated comprend une collection d'animations pré-construites pour les effets d'entrée et de sortie courants. Celles-ci vous évitent d'écrire des configurations d'animation pour des modèles standard comme le fondu, le glissement et le zoom.

Voici une modale qui apparaît en fondu lorsqu'elle est affichée et disparaît en fondu lorsqu'elle est masquée :

```javascript
import { FadeIn, FadeOut } from 'react-native-reanimated';

function Modal({ visible, children }) {
  if (!visible) return null;
  
  return (
    <Animated.View 
      entering={FadeIn.duration(300)}
      exiting={FadeOut.duration(200)}
    >
      {children}
    </Animated.View>
  );
}
```

La prop `entering` applique automatiquement l'animation de fondu à l'entrée lorsque le composant est monté, et `exiting` applique le fondu à la sortie avant le démontage. D'autres animations intégrées couramment utilisées incluent `SlideInRight`, `SlideOutLeft` (pour les entrées de type tiroir) et `ZoomIn`, `ZoomOut` (pour les apparitions qui attirent l'attention).

Maintenant que vous comprenez les animations CSS pour les transitions pilotées par l'état, explorons les worklets pour créer des animations interactives qui répondent aux entrées de l'utilisateur en temps réel.

## Tutoriel sur les Worklets

Alors que les animations CSS excellent dans les transitions d'état prédéfinies, de nombreuses animations doivent répondre dynamiquement aux entrées de l'utilisateur. C'est là que les worklets interviennent. Les worklets vous donnent un contrôle image par image sur les animations, leur permettant de suivre les gestes, la position de défilement ou toute autre source d'entrée en temps réel.

Les animations interactives diffèrent des animations CSS en ce qu'elles n'ont pas d'états de début et de fin prédéfinis. Au lieu de cela, elles se mettent à jour continuellement en fonction de l'entrée de l'utilisateur. Par exemple, un élément déplaçable doit suivre votre doigt précisément pendant que vous le déplacez – il n'y a aucun moyen de savoir à l'avance où vous le ferez glisser. Cela nécessite un contrôle impératif, où vous manipulez directement les valeurs d'animation en réponse aux événements.

### Animation de base avec Worklet

Les shared values sont le fondement des animations basées sur les worklets. Ce sont des variables spéciales qui existent simultanément dans les threads JavaScript et UI, vous permettant de les mettre à jour depuis JavaScript pendant que le thread UI les lit pour mettre à jour l'affichage – tout cela sans aucun surcoût de communication.

Voici un bouton qui rétrécit lorsqu'on appuie dessus et rebondit lorsqu'on le relâche :

```javascript
import Animated, { 
  useSharedValue, 
  useAnimatedStyle, 
  withSpring 
} from 'react-native-reanimated';
import { Pressable } from 'react-native';

function BouncyButton() {
  const scale = useSharedValue(1);
  
  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
  }));
  
  return (
    <Pressable
      onPressIn={() => { scale.value = withSpring(0.9); }}
      onPressOut={() => { scale.value = withSpring(1); }}
    >
      <Animated.View style={[styles.button, animatedStyle]}>
        <Text>Press Me</Text>
      </Animated.View>
    </Pressable>
  );
}
```

Le `useSharedValue(1)` crée une shared value initialisée à 1 (échelle normale). Le hook `useAnimatedStyle` crée un objet de style qui dépend de cette shared value et s'exécute sur le thread UI. Lorsque vous appuyez sur le bouton, `scale.value = withSpring(0.9)` met à jour la shared value, et `withSpring` crée une animation de ressort vers la nouvelle valeur. Le hook `useAnimatedStyle` s'exécute automatiquement à nouveau, mettant à jour la transformation avec la nouvelle valeur d'échelle.

### Animations de gestes

Les gestes nécessitent une intégration encore plus étroite entre l'entrée utilisateur et l'animation. La bibliothèque react-native-gesture-handler fournit une reconnaissance de gestes haute performance qui fonctionne parfaitement avec Reanimated.

Tout d'abord, installez le gestionnaire de gestes :

```bash
npm install react-native-gesture-handler
cd ios && pod install && cd ..
```

Ensuite, vous devez envelopper votre application avec `GestureHandlerRootView`. Ce composant configure le système de gestion des gestes à la racine de votre application. Sans lui, les gestes ne fonctionneront pas. Considérez-le comme l'activation du système de gestes pour toute votre application :

```javascript
import { GestureHandlerRootView } from 'react-native-gesture-handler';

export default function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      {/* Le contenu de votre application va ici */}
    </GestureHandlerRootView>
  );
}
```

Vous pouvez maintenant créer des animations pilotées par les gestes. Voici une boîte que vous pouvez faire glisser sur l'écran et qui revient au centre par un effet de ressort lorsqu'elle est relâchée :

```javascript
import { Gesture, GestureDetector } from 'react-native-gesture-handler';

function DraggableBox() {
  const offsetX = useSharedValue(0);
  const offsetY = useSharedValue(0);
  
  const pan = Gesture.Pan()
    .onChange((event) => {
      offsetX.value += event.changeX;
      offsetY.value += event.changeY;
    })
    .onEnd(() => {
      offsetX.value = withSpring(0);
      offsetY.value = withSpring(0);
    });
  
  const animatedStyle = useAnimatedStyle(() => ({
    transform: [
      { translateX: offsetX.value },
      { translateY: offsetY.value },
    ],
  }));
  
  return (
    <GestureDetector gesture={pan}>
      <Animated.View style={[styles.box, animatedStyle]} />
    </GestureDetector>
  );
}
```

Le `Gesture.Pan()` crée un reconnaisseur de geste de panoramique. Le rappel `.onChange()` se déclenche continuellement pendant que vous faites glisser – `event.changeX` et `event.changeY` vous indiquent de combien le doigt a bougé depuis la dernière image. En ajoutant ces valeurs aux décalages (offsets), la boîte suit votre doigt. Lorsque vous levez le doigt, `.onEnd()` se déclenche et fait revenir la boîte au centre (0, 0) avec un effet de ressort.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762275456257/3a536406-d678-46eb-9cfe-f689428d3412.gif align="center")

### Animations liées au défilement

Un autre cas d'utilisation courant des worklets est la création d'effets qui répondent à la position de défilement, comme des en-têtes qui rétrécissent au fur et à mesure que vous défilez vers le bas ou des arrière-plans parallaxe.

Voici un en-tête qui se réduit lors du défilement :

```javascript
function ParallaxHeader() {
  const scrollY = useSharedValue(0);
  
  const scrollHandler = useAnimatedScrollHandler({
    onScroll: (event) => {
      scrollY.value = event.contentOffset.y;
    },
  });
  
  const headerStyle = useAnimatedStyle(() => {
    const height = interpolate(
      scrollY.value,
      [0, 150],
      [200, 60],
      'clamp'
    );
    
    return { height };
  });
  
  return (
    <>
      <Animated.View style={[styles.header, headerStyle]}>
        <Text>Header</Text>
      </Animated.View>
      <Animated.ScrollView
        onScroll={scrollHandler}
        scrollEventThrottle={16}
      >
        {/* Contenu */}
      </Animated.ScrollView>
    </>
  );
}
```

Le `useAnimatedScrollHandler` crée un gestionnaire d'événements de défilement qui s'exécute sur le thread UI. Chaque fois que vous défilez, il met à jour `scrollY` avec la position de défilement actuelle. La fonction `interpolate` mappe la position de défilement à la hauteur de l'en-tête – quand scrollY est à 0 (haut du défilement), la hauteur est de 200. Quand scrollY atteint 150, la hauteur est de 60. L'option 'clamp' empêche la hauteur de sortir de cette plage.

Avec ces fondamentaux des animations CSS et des worklets couverts, voyons comment les appliquer à des scénarios réels courants.

## Modèles du monde réel

Maintenant que vous comprenez à la fois les animations CSS et les worklets, combinons-les pour construire trois modèles que vous rencontrerez fréquemment dans les applications de production. Ces exemples démontrent quand utiliser chaque approche d'animation et comment structurer votre code pour la maintenabilité.

Dans cette section, vous apprendrez à construire un en-tête rétractable qui rétrécit au fur et à mesure que les utilisateurs défilent (en utilisant des worklets pour le suivi du défilement), une bottom sheet qui répond aux gestes de glissement (en utilisant des worklets pour le contrôle des gestes), et une interaction de balayage pour supprimer des éléments de liste (combinant des worklets pour la détection des gestes avec des animations pour l'effet de suppression).

### En-tête rétractable

Un en-tête rétractable est une barre de navigation qui commence haute et rétrécit au fur et à mesure que vous défilez vers le bas. Ce modèle est populaire car il maximise l'espace de contenu tout en gardant la navigation accessible. Vous utiliserez des worklets ici car l'animation doit suivre la position de défilement en temps réel.

```javascript
function CollapsibleHeader() {
  const scrollY = useSharedValue(0);
  const HEADER_MAX = 200;
  const HEADER_MIN = 60;
  
  const scrollHandler = useAnimatedScrollHandler({
    onScroll: (event) => {
      scrollY.value = event.contentOffset.y;
    },
  });
  
  const headerStyle = useAnimatedStyle(() => ({
    height: interpolate(
      scrollY.value,
      [0, HEADER_MAX - HEADER_MIN],
      [HEADER_MAX, HEADER_MIN],
      'clamp'
    ),
  }));
  
  return (
    <View style={{ flex: 1 }}>
      <Animated.View style={[styles.header, headerStyle]}>
        <Text>My App</Text>
      </Animated.View>
      <Animated.ScrollView
        onScroll={scrollHandler}
        scrollEventThrottle={16}
      >
        <View style={{ height: 1000, padding: 16 }}>
          <Text>Scroll to see header collapse</Text>
        </View>
      </Animated.ScrollView>
    </View>
  );
}
```

Ce modèle suit la position de défilement dans `scrollY` et utilise `interpolate` pour la mapper à la hauteur de l'en-tête. Lorsque vous êtes en haut (scrollY = 0), l'en-tête fait 200 pixels de haut. Au fur et à mesure que vous défilez de 140 pixels, l'en-tête rétrécit à 60 pixels. L'animation se produit à chaque image pendant que vous défilez, c'est pourquoi les worklets sont nécessaires – les animations CSS ne pourraient pas suivre la position de défilement aussi fluidement.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762326945758/044ca9d6-dd6e-4891-b9f4-3a4dc8590b58.gif align="center")

### Bottom Sheet

Une bottom sheet est un panneau qui glisse depuis le bas de l'écran, couramment utilisé pour les menus d'action, les filtres ou du contenu supplémentaire. Les utilisateurs peuvent la faire glisser à différentes hauteurs ou la fermer d'un geste vers le bas. Cela nécessite des worklets car un suivi des gestes image par image est nécessaire.

```javascript
function BottomSheet({ children }) {
  const translateY = useSharedValue(300);
  const context = useSharedValue({ y: 0 });
  
  const pan = Gesture.Pan()
    .onStart(() => {
      context.value = { y: translateY.value };
    })
    .onChange((event) => {
      translateY.value = Math.max(
        event.translationY + context.value.y,
        -300
      );
    })
    .onEnd((event) => {
      if (event.velocityY > 500) {
        translateY.value = withSpring(300); // Fermer
      } else if (translateY.value > -100) {
        translateY.value = withSpring(-50); // Réduit
      } else {
        translateY.value = withSpring(-300); // Développé
      }
    });
  
  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ translateY: translateY.value }],
  }));
  
  return (
    <GestureDetector gesture={pan}>
      <Animated.View style={[styles.bottomSheet, animatedStyle]}>
        <View style={styles.handle} />
        {children}
      </Animated.View>
    </GestureDetector>
  );
}
```

La bottom sheet commence hors écran à translateY = 300. Lorsque vous commencez à faire glisser, `.onStart()` enregistre la position de départ dans `context`. Pendant que vous faites glisser, `.onChange()` met à jour la position, mais `Math.max()` l'empêche de descendre en dessous de -300 (entièrement développée). Lorsque vous relâchez, `.onEnd()` vérifie la vitesse – si vous avez balayé vers le bas rapidement (vitesse > 500), elle se ferme. Sinon, elle se fixe soit en position réduite (-50), soit en position développée (-300) selon l'endroit où vous l'avez relâchée.

![Bottom sheet demo](https://cdn.hashnode.com/res/hashnode/image/upload/v1763051520805/dd09d10f-4d77-40a9-be9c-ef85d69be69e.gif align="center")

### Glisser pour supprimer

Le balayage pour supprimer permet aux utilisateurs de retirer des éléments d'une liste en glissant vers la gauche. C'est un modèle courant dans les applications d'e-mail et les listes de tâches. Cela utilise des worklets pour le suivi des gestes et des fonctions de timing pour l'animation de suppression.

```javascript
function SwipeToDelete({ children, onDelete }) {
  const translateX = useSharedValue(0);
  const itemHeight = useSharedValue(60);
  
  const pan = Gesture.Pan()
    .activeOffsetX([-10, 10])
    .onChange((event) => {
      if (event.translationX < 0) {
        translateX.value = event.translationX;
      }
    })
    .onEnd(() => {
      if (translateX.value < -100) {
        translateX.value = withTiming(-500, { duration: 200 });
        itemHeight.value = withTiming(0, { duration: 200 }, () => {
          runOnJS(onDelete)();
        });
      } else {
        translateX.value = withSpring(0);
      }
    });
  
  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ translateX: translateX.value }],
    height: itemHeight.value,
  }));
  
  return (
    <GestureDetector gesture={pan}>
      <Animated.View style={[styles.item, animatedStyle]}>
        {children}
      </Animated.View>
    </GestureDetector>
  );
}
```

Le réglage `.activeOffsetX([-10, 10])` signifie que le geste ne s'active qu'après avoir bougé de 10 pixels horizontalement, évitant les déclenchements accidentels lors du défilement vertical. La vérification `if (event.translationX < 0)` garantit que vous ne pouvez glisser que vers la gauche, pas vers la droite. Si vous glissez au-delà de -100 pixels et relâchez, cela déclenche la suppression : l'élément glisse hors de l'écran (-500), la hauteur se réduit à 0, et `runOnJS` appelle votre fonction de suppression depuis le thread UI vers JavaScript.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1763051815614/6e2c2d60-3d2e-49ec-9fb5-c17db00e9120.gif align="center")

Ces modèles démontrent la puissance de la combinaison des approches d'animation de Reanimated avec la gestion des gestes. Maintenant, voyons comment maintenir la fluidité de ces animations.

## Optimisations de performance

Même si Reanimated s'exécute sur le thread UI, des animations mal structurées peuvent toujours perdre des images. Voici quatre optimisations clés qui maintiendront vos animations à 60 FPS de manière constante.

### Mémoriser les animations

Chaque fois que votre composant est rendu à nouveau, toutes les animations que vous créez à l'intérieur de la fonction de rendu sont recréées. Cela gaspille de la mémoire et du temps de traitement.

Ne faites pas ceci – créer un nouvel objet d'animation à chaque rendu :

```javascript
{items.map(item => (
  <Animated.View entering={FadeIn.duration(300)} key={item.id} />
))}
```

Au lieu de cela, créez l'animation une seule fois en dehors du composant ou mémorisez-la :

```javascript
const fadeIn = FadeIn.duration(300);
{items.map(item => (
  <Animated.View entering={fadeIn} key={item.id} />
))}
```

En stockant l'animation dans une constante, vous la créez une fois et réutilisez le même objet pour tous les éléments. Cela réduit l'allocation de mémoire et le ramasse-miettes (garbage collection), gardant vos animations fluides même avec de longues listes.

### Utiliser useDerivedValue

Si vous effectuez des calculs coûteux à l'intérieur de `useAnimatedStyle`, ces calculs s'exécutent à chaque image, même si les dépendances n'ont pas changé.

Ne faites pas ceci – recalculer à chaque image :

```javascript
const animatedStyle = useAnimatedStyle(() => ({
  width: Math.min(Math.max(offset.value * 2, 100), 500),
}));
```

Utilisez plutôt `useDerivedValue` pour calculer la valeur uniquement lorsque les dépendances changent :

```javascript
const width = useDerivedValue(() => 
  Math.min(Math.max(offset.value * 2, 100), 500)
);

const animatedStyle = useAnimatedStyle(() => ({
  width: width.value,
}));
```

Désormais, le calcul complexe ne s'exécute que lorsque `offset.value` change, et non à chaque image. Le `useAnimatedStyle` lit simplement la largeur pré-calculée, ce qui est beaucoup plus rapide.

### Mises à jour par lots (Batching)

Lorsque vous mettez à jour plusieurs shared values, chaque mise à jour peut déclencher un rendu séparé. Cela crée un travail inutile pour le thread UI.

Ne faites pas ceci – déclencher plusieurs rendus :

```javascript
scale.value = withSpring(1.2);
opacity.value = withSpring(0.8);
```

Utilisez plutôt `runOnUI` pour regrouper les mises à jour :

```javascript
runOnUI(() => {
  'worklet';
  scale.value = withSpring(1.2);
  opacity.value = withSpring(0.8);
})();
```

La fonction `runOnUI` garantit que les deux mises à jour se produisent dans la même image, de sorte que l'interface utilisateur ne se restitue qu'une seule fois. C'est particulièrement important lors de la mise à jour de nombreuses valeurs à la fois, comme dans des gestes complexes ou des animations chorégraphiées.

### Préférer Transform au Layout

Animer des propriétés de mise en page (layout) comme la largeur, la hauteur ou les marges force React Native à recalculer la position de chaque élément qui dépend de l'élément qui change. C'est coûteux.

Ne faites pas ceci – recalcul de mise en page coûteux :

```javascript
width: withSpring(newWidth)
```

Utilisez plutôt des propriétés de transformation (transform), qui n'affectent que l'apparence visuelle sans déclencher de mise en page :

```javascript
transform: [{ scaleX: withSpring(scale) }]
```

Les opérations de transformation sont accélérées matériellement et n'affectent pas la mise en page, ce qui les rend considérablement plus rapides. Autant que possible, utilisez `translateX/Y` au lieu de changer la position, `scale` au lieu de changer la taille, et `rotate` au lieu de changer l'orientation.

Ces optimisations garderont vos animations parfaitement fluides. Voyons maintenant comment déboguer les problèmes lorsqu'ils surviennent.

## Conseils de débogage

Même avec une configuration correcte, vous pouvez rencontrer des problèmes avec les animations. Voici les problèmes les plus courants et leurs solutions, rédigés sous forme d'étapes de dépannage complètes.

### Les animations ne fonctionnent pas

Si vos animations ne s'exécutent pas du tout, la cause la plus fréquente est un plugin Babel manquant ou mal configuré. Ouvrez votre fichier `babel.config.js` et vérifiez que `react-native-worklets/plugin` est présent dans le tableau des plugins et qu'il est le dernier plugin de la liste. L'ordre est important car le plugin worklets doit traiter votre code après toutes les autres transformations.

Après avoir confirmé que le plugin est correctement configuré, effacez le cache de votre bundler Metro en exécutant `npm start -- --reset-cache`, puis reconstruisez complètement votre application. Le simple rechargement du JavaScript ne fonctionnera pas car les transformations Babel se produisent pendant le processus de construction.

### L'application plante au démarrage ou au rechargement

Si votre application plante immédiatement après l'installation de Reanimated ou lors d'un rechargement, les modules natifs ne sont probablement pas correctement liés. Avec React Native 0.76+, cela signifie généralement que les pods n'ont pas été installés ou que la construction native n'est pas synchronisée.

Pour iOS, exécutez `cd ios && pod install && cd ..` puis effectuez une construction propre avec `npx react-native run-ios`. Pour Android, nettoyez la construction avec `cd android && ./gradlew clean && cd ..` puis reconstruisez avec `npx react-native run-android`.

Si vous obtenez des erreurs de construction concernant des en-têtes ou des modules manquants, assurez-vous d'avoir ajouté à la fois `react-native-reanimated` et `react-native-worklets` à vos dépendances package.json.

### "TurboModuleRegistry Not Found"

Si vous voyez un message d'erreur indiquant "TurboModuleRegistry.get('NativeReanimated'): 'NativeReanimated' could not be found", cela signifie que le code natif n'a pas été correctement lié à votre code JavaScript.

Tout d'abord, vérifiez que vous utilisez React Native 0.76 ou plus récent, car Reanimated 4 nécessite la Nouvelle Architecture. Vérifiez votre `ios/Podfile` pour `ENV['RCT_NEW_ARCH_ENABLED'] = '1'` et `android/gradle.properties` pour `newArchEnabled=true`.

Ensuite, reconstruisez complètement : `cd ios && pod install && cd .. && npx react-native run-ios`.

### Journalisation et inspection des Shared Values

Si vous essayez de déboguer des worklets en utilisant `console.log()`, vous remarquerez que rien n'apparaît dans votre console. C'est parce que les worklets s'exécutent sur le thread UI, qui n'a pas d'accès direct à la console JavaScript.

Pour journaliser des valeurs depuis des worklets, utilisez le hook `useDerivedValue` :

```javascript
const offset = useSharedValue(0);

useDerivedValue(() => {
  console.log('Offset:', offset.value);
  return offset.value;
});
```

Pour un débogage plus avancé, le débogueur intégré de React Native (accessible via le menu dev → "Open Debugger") prend désormais en charge le débogage des deux threads. Vous pouvez définir des points d'arrêt dans les worklets et inspecter les shared values en temps réel.

### Surveiller la performance

Pour voir si vos animations s'exécutent réellement à 60 FPS, activez le moniteur de performance intégré à React Native. Secouez votre appareil (ou appuyez sur Cmd+D dans le simulateur iOS, Cmd+M dans l'émulateur Android) pour ouvrir le menu dev, puis sélectionnez "Show Perf Monitor".

Le moniteur affiche deux chiffres critiques : le FPS du thread JS et le FPS du thread UI. Vos animations s'exécutent sur le thread UI, surveillez donc ce chiffre. S'il reste à 60 FPS, vos animations sont fluides. S'il descend en dessous de 60, vos animations sautent des images et paraîtront saccadées. Le FPS du thread JS indique si votre code React suit le rythme – si celui-ci chute, cela indique des problèmes avec les rendus de vos composants, pas vos animations.

Pour des informations de débogage plus détaillées et un dépannage avancé, consultez le [guide de débogage officiel ici](https://docs.swmansion.com/react-native-reanimated/docs/guides/debugging/).

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1763053624344/7aeffb5f-4829-4871-bd49-6e589adeb8ad.png align="center")

## Conclusion

Reanimated 4 vous offre deux approches puissantes pour l'animation : les animations CSS pour les changements d'état simples et les worklets pour les animations complexes et interactives qui nécessitent un contrôle en temps réel.

Commencez par les transitions CSS lors de la création de votre prochaine fonctionnalité d'animation. Elles sont plus simples à écrire, plus faciles à maintenir et parfaites pour la majorité des animations d'interface utilisateur. Tournez-vous vers les worklets lorsque vous avez besoin d'un contrôle par gestes, d'effets de défilement ou de toute animation nécessitant des mises à jour image par image.

La [documentation officielle](https://docs.swmansion.com/react-native-reanimated) fournit des références API complètes, des guides détaillés et des exemples interactifs. Le [dépôt GitHub](https://github.com/software-mansion/react-native-reanimated) comprend du code d'exemple prêt pour la production que vous pouvez étudier et adapter.

Créer des animations fluides n'est pas seulement une question de capacité technique – il s'agit de créer des expériences qui semblent réactives, intuitives et agréables à utiliser. Reanimated 4 rend l'atteinte de ce standard simple, que vous animiez une simple pression sur un bouton ou que vous construisiez une transition d'écran complexe avec plusieurs éléments coordonnés.