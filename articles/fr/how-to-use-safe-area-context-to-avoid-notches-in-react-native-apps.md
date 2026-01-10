---
title: Comment utiliser Safe Area Context dans les applications React Native pour
  éviter l'encoche
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-20T19:37:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-safe-area-context-to-avoid-notches-in-react-native-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/2-1.png
tags:
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: Comment utiliser Safe Area Context dans les applications React Native pour
  éviter l'encoche
seo_desc: 'By Aman Mittal

  Most devices nowadays come with a notch at the top of the screen. So when you''re
  building a mobile application using React Native, you need to make sure that the
  content of the app''s screen is rendered correctly across different types ...'
---

Par Aman Mittal

La plupart des appareils aujourd'hui sont équipés d'une encoche en haut de l'écran. Ainsi, lorsque vous construisez une application mobile avec React Native, vous devez vous assurer que le contenu de l'écran de l'application est rendu correctement sur différents types d'appareils.

Dans cet article, nous examinerons deux approches différentes pour créer des écrans d'application dans React Native. Chacune évite que le contenu soit positionné derrière une encoche ou une barre d'état.

La première approche utilise le composant `SafeAreaView` de l'API des composants React Native. La deuxième approche discute de l'avantage d'utiliser la bibliothèque open source [react-native-safe-area-context](https://github.com/th3rdwave/react-native-safe-area-context) et comment elle fournit une solution multiplateforme.

## Le problème de l'encoche

Lorsque vous commencez à construire un écran dans une application React Native, vous pourriez utiliser le code suivant pour afficher du texte :

```js
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export const HomeScreen = () => {
  return (
    <View style={[styles.container]}>
      <View style={{ backgroundColor: 'blue' }}>
        <Text style={{ fontSize: 28, color: 'white' }}>Bonjour le monde</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'red'
  }
});
```

Le code ci-dessus a un composant parent `View` avec une couleur de fond `red`. Il enveloppe un autre composant `View` avec une couleur de fond `blue` qui contient un composant `Text` pour afficher du texte à l'écran.

Cela affichera le contenu de l'écran sur un appareil iOS comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ss1-1.png)
_Sans SafeAreaView sur iOS_

Le contenu du composant `View` imbriqué se cache derrière la barre d'état et l'encoche sur l'appareil iOS.

Sur un appareil Android, le comportement est exactement le même :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ss2-1.png)
_La barre d'état chevauche le contenu de l'écran sur Android_

## Comment utiliser le composant SafeAreaView de React Native

Une approche consiste à utiliser le [composant SafeAreaView](https://reactnative.dev/docs/safeareaview) disponible dans React Native.

```js
import { SafeAreaView } from 'react-native';
```

Vous l'utilisez simplement à la place du composant `View` de niveau supérieur. Il garantit que le contenu dans les limites de la zone sécurisée est correctement rendu autour du contenu imbriqué et applique un remplissage automatiquement.

Nous pouvons donc modifier l'extrait de code précédent :

```js
import React from 'react';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';

export const HomeScreen = () => {
  return (
    <SafeAreaView style={[styles.container]}>
      <View style={{ backgroundColor: 'blue' }}>
        <Text style={{ fontSize: 28, color: 'white' }}>Bonjour le monde</Text>
      </View>
    </SafeAreaView>
  );
};
```

Ainsi, il fonctionne parfaitement sur iOS :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ss3-1.png)
_En utilisant le composant SafeAreaView_

Dans React Native, ce composant n'est applicable qu'aux appareils iOS avec la version iOS 11 ou ultérieure. Malheureusement, cela signifie qu'il ne fonctionne pas pour les appareils Android, car le contenu de l'écran est toujours derrière la barre d'état.

## Comment utiliser la bibliothèque Safe Area Context de React Native

Heureusement, il existe une solution multiplateforme pour gérer les zones sécurisées sur les appareils avec encoche appelée [react-native-safe-area-context](https://github.com/th3rdwave/react-native-safe-area-context). Elle fournit une API flexible pour gérer les marges de zone sécurisée en JS et fonctionne sur iOS, Android et le Web.

Commencez par l'installer dans votre application React Native :

```shell
# pour les applications React Native standard
yarn add react-native-safe-area-context

# installer la dépendance pod pour iOS uniquement
npx pod-install

# pour les applications Expo
expo install react-native-safe-area-context
```

Cette bibliothèque fournit un `SafeAreaProvider` qui doit envelopper soit votre Navigateur Racine, soit l'écran où vous souhaitez gérer les marges de zone sécurisée.

Par exemple, dans l'extrait de code ci-dessous, le `SafeAreaProvider` enveloppe le composant `HomeScreen` puisque l'application exemple ne contient qu'un seul écran.

```js
import React from 'react';
import { SafeAreaProvider } from 'react-native-safe-area-context';

import { HomeScreen } from './src/screens';

export default function App() {
  return (
    <SafeAreaProvider>
      <HomeScreen />
    </SafeAreaProvider>
  );
}
```

Maintenant, vous pouvez importer le composant `SafeAreaView` de la bibliothèque `react-native-safe-area-context` et le remplacer par celui de React Native.

```js
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

export const HomeScreen = () => {
  return (
    <SafeAreaView style={[styles.container]}>
      <View style={{ backgroundColor: 'blue' }}>
        <Text style={{ fontSize: 28, color: 'white' }}>Bonjour le monde</Text>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'red'
  }
});
```

Cela fonctionne à la fois pour iOS et Android :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ss4-1.png)
_La bibliothèque fonctionne sur iOS et Android sans configuration supplémentaire_

Si vous donnez au composant `View` imbriqué une propriété `flex: 1` comme ceci :

```js
<View style={{ backgroundColor: 'blue', flex: 1 }}>
```

Vous pouvez voir les bords de la zone sécurisée sur iOS :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ss5-1.png)

Le `SafeAreaView` agit comme un composant `View` standard de React Native et inclut un remplissage supplémentaire pour positionner le contenu sous l'encoche ou la barre d'état d'un appareil.

Il est également livré avec une propriété `edges` qui personnalise les marges de zone sécurisée autour de différents bords tels que le haut, le bas, la gauche et la droite.

## Comment utiliser le hook useSafeAreaInsets

Un autre avantage de l'utilisation de cette bibliothèque est qu'elle fournit un hook appelé `useSafeAreaInsets` qui offre plus de flexibilité. Il vous donne également plus de contrôle, et vous pouvez appliquer un remplissage pour chaque bord en utilisant une propriété de ce hook.

Par exemple, dans le composant `View` ci-dessous, nous voulons que le remplissage soit appliqué uniquement au bord supérieur :

```js
import { useSafeAreaInsets } from 'react-native-safe-area-context';

export const HomeScreen = () => {
  const insets = useSafeAreaInsets();

  return (
    <View
      style={{
        paddingTop: insets.top
      }}
    >
      {children}
    </View>
  );
};
```

## Conclusion

La gestion des barres d'état et des encoches sur différents appareils devient beaucoup plus facile avec la bibliothèque react-native-safe-area-context. Essayez-la dans votre prochaine bibliothèque React Native.

🐆 [Code source dans ce dépôt GitHub](https://github.com/amandeepmittal/react-native-examples/tree/master/rnSplashAndIconExample)

Visitez mon [blog](https://amanhimself.dev/) et [suivez-moi](https://twitter.com/amanhimself) sur Twitter pour plus de contenu lié à React Native ou Expo.