---
title: Comment créer un chargeur animé magnifiquement dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T22:00:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-beautifully-animated-loader-in-react-native-21da37a8f6b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2jY8OGNqWzZo-sqUBApBkg.gif
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment créer un chargeur animé magnifiquement dans React Native
seo_desc: 'By Vikrant Negi

  Use Airbnb’s Lottie library to jazz up your loaders.


  Lottie Animation for Loaders

  A loader in Web or Mobile is an essential design element usually used when we need
  to perform some asynchronous task like data processing or fetching. ...'
---

Par Vikrant Negi

#### Utilisez la bibliothèque [Lottie](https://airbnb.design/lottie/) d'Airbnb pour dynamiser vos chargeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/D7aU6jFKntF2FdAchdkb9AUmUUpjjBZiP4On)
_Animation Lottie pour les chargeurs_

Un chargeur dans une application Web ou Mobile est un élément de design essentiel généralement utilisé lorsque nous devons effectuer une tâche asynchrone comme le traitement ou la récupération de données. Puisque ces tâches peuvent prendre un certain temps et que les utilisateurs doivent être divertis pendant ce temps, c'est là que les chargeurs deviennent utiles.

Les chargeurs aident les développeurs à garder l'utilisateur engagé pendant qu'il attend et évitent tout manque de réactivité dans l'application. ?

> Vous ne voulez pas attendre ? Consultez le package npm [React-Native-Animated-Loader](https://github.com/vikrantnegi/react-native-animated-loader).

#### Pour commencer

React Native dispose d'un `[ActivityIndicator](https://facebook.github.io/react-native/docs/activityindicator)` intégré qui peut être utilisé comme indicateur de chargement.

Mais pour les `Loaders`, nous ne pouvons pas simplement utiliser `ActivityIndicator` car nous voulons empêcher l'utilisateur d'effectuer une action jusqu'à ce que la tâche soit terminée. Pour cela, nous allons utiliser `[Modals](https://facebook.github.io/react-native/docs/modal#docsNav)`.

Si vous voulez simplement un chargeur simple et basique, consultez [ce](https://medium.com/@kelleyannerose/react-native-activityindicator-for-a-quick-easy-loading-animation-593c06c044dc) tutoriel.

Mais si vous voulez ajouter une touche d'originalité ? à vos chargeurs, continuez avec ce tutoriel. ?

#### Lottie d'Airbnb ?

[Lottie](https://airbnb.design/lottie/) est une bibliothèque pour iOS, Android et React Native qui rend les animations After Effects en temps réel, permettant aux applications d'utiliser des animations aussi facilement que des images statiques.

Nous allons utiliser sa bibliothèque wrapper React Native [lottie-react-native](https://github.com/react-native-community/lottie-react-native) pour notre animation de chargeur personnalisée.

#### Créer une application

Nous allons utiliser `react-native-cli` pour créer un projet React Native, mais vous pouvez également utiliser Expo.

Créez un projet exemple avec la commande suivante :

```
~ react-native init LoaderExample
```

#### Installer les dépendances

Maintenant, ajoutons les packages nécessaires. Installez d'abord `react-native-animated-loader` et `lottie-react-native`.

```
~ npm install react-native-animated-loader --save
```

```
~ npm i --save lottie-react-native
```

> Si vous utilisez Expo, vous n'avez pas besoin d'installer Lottie.

Puisque `lottie-react-native` nécessite un lien natif, exécutez les commandes suivantes :

```
~ react-native link lottie-ios
```

```
~ react-native link lottie-react-native
```

Après cela, ouvrez la configuration du projet Xcode et ajoutez le `Lottie.framework` en tant que `Embedded Binaries`.

> Si vous rencontrez une erreur après avoir lié Lottie, suivez les instructions d'installation détaillées [ici](https://github.com/react-native-community/lottie-react-native/blob/master/README.md#getting-started).

#### Ajoutons de la magie ?

Maintenant, mettez à jour votre `App.js` avec le code suivant :

```
import React, { Component } from 'react';import { StyleSheet, View, Button } from 'react-native';import AnimatedLoader from 'react-native-animated-loader';
```

```
export default class App extends Component<Props> {  constructor(props) {    super(props);    this.state = { visible: false };  }
```

```
  handlePress = () => {    setTimeout(() => {      this.setState({         visible: !this.state.visible,      });    }, 1000);  };
```

```
  render() {    const { visible } = this.state;
```

```
    return (      <View style={styles.container}>        <AnimatedLoader          visible={visible}          overlayColor="rgba(255,255,255,0.75)"          animationStyle={styles.lottie}          speed={1}        />        <Button title="press" onPress={this.handlePress} />      </View>    );  }}
```

```
const styles = StyleSheet.create({  container: {    flex: 1,    justifyContent: 'center',    alignItems: 'center',    backgroundColor: '#F5FCFF',  },  lottie: {    width: 100,    height: 100,  },});
```

Lorsque vous cliquez, vous devriez voir l'animation suivante dans quelques secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/746QhP7tWnW-IRfc5QQw9kTRV9cQZ7whLI43)

#### Personnaliser l'animation

L'animation que vous voyez est celle par défaut, mais vous pouvez ajouter votre propre animation Lottie. Si vous souhaitez trouver des animations de chargeur sympas, rendez-vous sur [lottiefiles](https://lottiefiles.com/), où vous pouvez trouver des animations de chargeur pré-construites. Choisissez simplement celle que vous aimez et téléchargez son fichier JSON.

Maintenant, ajoutez le fichier JSON téléchargé au projet `LoaderExample` et ajoutez la prop source à `AnimatedLoader`. Après avoir ajouté la source, cela devrait ressembler à ceci :

```
<AnimatedLoader  visible={visible}  overlayColor="rgba(255,255,255,0.75)"  animationStyle={styles.lottie}  speed={1}  source={require("./path-of-your-json-file.json")} // Ajoutez ici/>
```

Vous pouvez également personnaliser les styles du chargeur en ajoutant la prop `animationStyle`.

#### Utilisation

Dans notre exemple, j'ai utilisé `setTimeout` pour simuler une tâche asynchrone. Dans le monde réel, vous l'utiliseriez pour toutes sortes de tâches asynchrones comme la récupération de données depuis une API.

#### Conclusion

Maintenant que vous savez comment créer un chargeur animé cool, j'espère que vous allez arrêter d'utiliser l'ancien indicateur d'activité ennuyeux pour vos chargeurs.

> Trouvez le dépôt de la bibliothèque [ici](https://github.com/vikrantnegi/react-native-animated-loader).

Si vous aimez cet article, n'hésitez pas à montrer votre soutien avec vos applaudissements.

Consultez mes autres articles sur React Native :

* [React Native FlatList avec capacité de recherche en temps réel](https://medium.freecodecamp.org/how-to-build-a-react-native-flatlist-with-realtime-searching-ability-81ad100f6699)
* [Suivi de localisation avec React Native](https://medium.com/quick-code/react-native-location-tracking-14ab2c9e2db8)
* [Graphiques React Native avec infobulles dynamiques](https://medium.freecodecamp.org/how-to-build-react-native-charts-with-dynamic-tooltips-64aefc550c95)