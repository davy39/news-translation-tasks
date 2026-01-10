---
title: React Native – Éléments tactiles et dimensions de l'écran
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T19:44:00.000Z'
originalURL: https://freecodecamp.org/news/react-native-touchables-and-screen-dimensions
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/daniel-korpai-8GDCzWrcE3M-unsplash.jpg
tags:
- name: api
  slug: api
- name: Libraries
  slug: libraries
- name: React Native
  slug: react-native
- name: responsive design
  slug: responsive-design
- name: toothbrush
  slug: toothbrush
seo_title: React Native – Éléments tactiles et dimensions de l'écran
seo_desc: React Native makes the process of developing an application that works on
  both Android and iOS devices much easier than it once was. While before you had
  to work with at least two programming languages and vastly different APIs, React
  Native includes...
---

React Native facilite grandement le processus de développement d'une application qui fonctionne à la fois sur les appareils Android et iOS. Alors qu'auparavant, vous deviez travailler avec au moins deux langages de programmation et des API très différentes, React Native inclut certaines API utiles dès le départ.

Voici un aperçu de deux d'entre elles qui vous aideront à construire votre prochaine application.

## Éléments tactiles

Certaines des principales fonctionnalités des appareils mobiles tournent autour des interactions tactiles de l'utilisateur. La manière dont une application mobile gère et répond à ces interactions peut faire ou défaire l'expérience de l'utilisateur.

React Native est livré avec un composant `Button` qui fonctionne pour de nombreuses interactions `onPress` standard. Par défaut, il donnera un retour à l'utilisateur en changeant l'opacité pour montrer que le bouton a été pressé. Utilisation :

```js
<Button onPress={handlePress} title="Submit" />
```

Pour des cas d'utilisation plus complexes, React Native dispose d'API intégrées pour gérer les interactions de pression appelées `Touchables`.

```text
TouchableHighlight
TouchableNativeFeedback
TouchableOpacity
TouchableWithoutFeedback
```

Chacun de ces composants tactiles peut être stylisé et utilisé avec une bibliothèque, comme la bibliothèque intégrée `Animated`, vous permettant de créer vos propres types de retours utilisateur personnalisés.

Quelques exemples d'utilisation de ces composants :

```js
// avec des images
<TouchableHighlight onPress={this.handlePress}>
  <Image
    style={styles.button}
    source={require('./logo.png')}
  />
</TouchableHighlight>

// avec du texte
<TouchableHighlight onPress={this.handlePress}>
  <Text>Bonjour</Text>
</TouchableHighlight>
```

Vous pouvez également gérer différents types de pressions sur les boutons. Par défaut, les boutons et les éléments tactiles sont configurés pour gérer les taps réguliers, mais vous pouvez également désigner une fonction à appeler pour les interactions de pression longue, par exemple.

```js
<TouchableHighlight onPress={this.handlePress} onLongPress={this.handleLongPress}>
```

Pour voir toutes les props disponibles et comment ces composants fonctionnent, vous pouvez consulter [le code source JavaScript pour les Touchables ici](https://github.com/facebook/react-native/tree/master/Libraries/Components/Touchable).

## Dimensions de l'écran

React Native utilise les Dots Per Inch (DPI) pour mesurer la taille de l'Interface Utilisateur (UI) et tout ce qui est affiché sur l'UI. Ce type de mesure permet à une application de paraître uniforme sur diverses tailles d'écran et densités de pixels.

Pour les cas d'utilisation standard, les applications peuvent être développées sans avoir à connaître les spécificités de l'appareil de l'utilisateur (par exemple, la densité de pixels) puisque les éléments de l'UI s'adapteront automatiquement.

Lorsque cela est nécessaire, des API sont disponibles telles que `PixelRatio` pour vous aider à connaître la densité de pixels de l'appareil de l'utilisateur.

Pour obtenir la hauteur/largeur de la fenêtre ou de l'écran de l'appareil de l'utilisateur, React Native dispose d'une API appelée `Dimensions`.

```js
import { Dimensions } from 'react-native';
```

Voici les méthodes que l'API `Dimensions` fournit :

```js
Dimensions.get('window').height;
Dimensions.get('window').width;
Dimensions.get('screen').height;
Dimensions.get('screen').width;
```

**Note :** Il y a eu quelques problèmes connus dans le passé avec l'API Dimensions, comme le fait de ne pas retourner les informations correctes lorsque l'utilisateur fait pivoter son appareil. Il est préférable de s'assurer que vous testez cela sur des appareils réels avant de déployer une application.

### Plus d'informations sur le design responsive :

* [Cours gratuit sur le design responsive](https://www.freecodecamp.org/news/master-responsive-website-design/)
* [Meilleurs tutoriels Bootstrap pour le design web responsive](https://www.freecodecamp.org/news/p/f401cbed-6c27-46e5-a56f-c9853b87e244/freecodecamp.org/news/best-bootstrap-tutorial-responsive-web-design/)
* [Comment penser de manière responsive](https://www.freecodecamp.org/news/how-to-start-thinking-responsively/)
* [Guide des images responsives](https://www.freecodecamp.org/news/your-complete-guide-to-truly-responsive-images/)
* [Apprendre le design responsive en 5 minutes](https://www.freecodecamp.org/news/learn-responsive-web-design-in-5-minutes/)