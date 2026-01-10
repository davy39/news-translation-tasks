---
title: Tutoriel React Native – Comment créer une mise en page responsive simple pour
  débutants
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2023-02-02T23:50:26.000Z'
originalURL: https://freecodecamp.org/news/responsive-layout-react-native
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-luna-lovegood-4087468.jpg
tags:
- name: React Native
  slug: react-native
- name: responsive design
  slug: responsive-design
seo_title: Tutoriel React Native – Comment créer une mise en page responsive simple
  pour débutants
seo_desc: Having a responsive layout is an important component of user interface (UI)
  design. It enables a website or application to automatically adjust its size and
  layout based on the size of the user's device and screen. This provides an optimal
  viewing ex...
---

Avoir une mise en page responsive est un composant important de la conception d'interface utilisateur (UI). Elle permet à un site web ou à une application de s'ajuster automatiquement en taille et en disposition en fonction de la taille de l'appareil et de l'écran de l'utilisateur. Cela offre une expérience de visualisation optimale.

Les mises en page responsives donnent également à l'utilisateur une apparence plus cohérente et unifiée sur tous les appareils et plateformes, tout en veillant à ce que l'expérience de l'utilisateur soit adaptée à son appareil.

Cela contribue à créer une expérience plus conviviale et améliore l'utilisabilité globale du site web ou de l'application.

Dans ce tutoriel, je vais vous montrer comment créer une mise en page responsive simple dans React Native. Vous pouvez prévisualiser la démonstration [ici](https://snack.expo.dev/@ubahthebuilder/67d71a).

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin de :

* Une compréhension de base de React Native

* [Expo Snack](https://snack.expo.dev/) – un environnement de développement basé sur le navigateur pour React Native

## Comment créer une mise en page responsive

Allez sur Expo Snack et effacez le contenu de App.js. Commencez par importer la bibliothèque React et les composants d'interface utilisateur Text, View et Stylesheet :

```c
import * as React from 'react';
import { Text, View, StyleSheet } from 'react-native';
```

React Native est basé sur React, nous devons donc importer explicitement la bibliothèque React. Le composant Text est utilisé pour créer du texte, View est un élément conteneur utilisé pour regrouper d'autres éléments, et StyleSheet est utilisé pour définir la feuille de style des composants.

Ensuite, définissez une fonction App et retournez deux composants personnalisés, `<Header />` et `<Boxes />` :

```c
export default function App() {
  return (
    <View style={styles.container}>
      <Header />
      <Boxes />
    </View>
  );
}
```

Ici, nous enveloppons `<Header />` et `<Boxes />` dans un conteneur `<View />`. Les deux sont des composants personnalisés, et comme ils n'ont pas encore été créés, vous obtiendrez une ReferenceError. Ignorez cela pour l'instant.

Ensuite, créez la feuille de style pour ce composant et définissez le style pour l'élément conteneur :

```c
const styles = StyleSheet.create({
  container: {
    flex: 1,   
  },  
});
```

Cette valeur `flex:1` indique au composant de remplir tout l'espace disponible et de partager l'espace de manière égale entre ses enfants.

Créons maintenant les composants `<Header>` et `<Boxes/>`.

## Comment créer le composant `<Header />`

Dans le dossier des composants, créez un nouveau fichier nommé Header.js. Ensuite, importez les éléments suivants :

```c
import * as React from 'react';
import { Text, View, StyleSheet} from 'react-native';
```

Créez une fonction `<Header />` et retournez un seul `<View />` avec le texte "Header Component" :

```c
export default function Header() {
  return (
    <View style={styles.header}>
      <Text>Composant d'en-tête</Text>
    </View>
  );
}
```

Le `<View />` est lié à une propriété `style` de `header`. Gardez à l'esprit que nous voulons rendre cet en-tête responsive sur toutes les tailles d'écran. Faisons cela en utilisant CSS.

```c
const styles = StyleSheet.create({
  header: {
    width: "100%",
    height: "15%",
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'grey'    
  },
});
```

Avec cette feuille de style, nous spécifions que, quelle que soit la taille de l'écran, l'en-tête doit s'étendre sur toute la largeur de l'écran (100%) et ne prendre que 15% de la hauteur de l'écran.

Passons maintenant aux boîtes.

## Comment créer le composant `<Boxes />`

Sous l'en-tête, nous voulons placer deux boîtes, une à gauche et une à droite. Nous voulons également que les boîtes occupent une certaine largeur et hauteur en fonction de la dimension de l'écran de l'appareil cible.

Dans le dossier des composants, créez un nouveau fichier nommé boxes.js. Commencez par importer les éléments suivants :

```c
import * as React from 'react';
import { Text, View, StyleSheet} from 'react-native';
```

Ensuite, créez une fonction Boxes et retournez le balisage pour les boîtes :

```c
export default function Boxes() {
  return (
    <View style={styles.container}>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Text>Boîte 1</Text>
        </View>                      
      </View>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Text>Boîte 2</Text>
        </View>                      
      </View>
    </View>
  );
}
```

Ici, nous avons deux boîtes placées dans le conteneur. À l'intérieur des deux se trouve un élément View contenant l'étiquette de texte pour chaque boîte.

Ensuite, définissez le style pour le composant. Nous allons créer trois ensembles de styles, un pour le conteneur de boîte, un pour l'enveloppe intérieure et le dernier pour les boîtes elles-mêmes.

```c
const styles = StyleSheet.create({
  container: {
    width: "100%",
    height: "85%",
    alignItems: "center",
    flexDirection: 'row',
    flexWrap: 'wrap'    
  },
  box: {
    width: "50%",
    height: "50%",
    padding: 5
  },
  inner: {
    flex: 1,
    backgroundColor: "#D3D3D3",
    alignItems: 'center',
    justifyContent: 'center'
  }
});
```

Rappelons que l'en-tête occupe 15% de la hauteur de l'écran. Par conséquent, avec le CSS ci-dessus, nous spécifions que le conteneur de boîte doit occuper les 85% restants.

Nous alignons les boîtes au centre et les plaçons dans un arrangement en ligne. Chaque boîte occupe 50% de la hauteur et de la largeur totales, et nous appliquons un espacement de 5 pour les espacer un peu.

Maintenant que nous avons à la fois l'en-tête et les boîtes responsives prêtes, importons-les dans App.js et voyons les résultats.

## Comment importer `<Header />` et `<Boxes />`

Dans App.js, en haut du fichier, importez `<Header />` et `<Boxes />` comme suit :

```c
import Header from "./components/Header"
import Boxes from "./components/Boxes"
```

Une fois l'application compilée, vous devriez voir votre mise en page responsive du côté droit de votre fenêtre, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/UI.png align="left")

*Apparence finale de la mise en page responsive*

Cet arrangement sera cohérent sur toutes les tailles d'écran car nous avons utilisé des pourcentages pour définir la hauteur et la largeur au lieu de valeurs de largeur fixes.

## Conclusion

J'espère que ce tutoriel vous a aidé à mieux comprendre le positionnement dans React Native. Vous devriez maintenant être en mesure de créer des mises en page responsives dans votre application React Native en utilisant les techniques que nous avons couvertes dans cet article.

Téléchargez ma checklist gratuite de rédaction freelance [ici](https://kingchuks.gumroad.com/l/fwc). Passez une excellente semaine !