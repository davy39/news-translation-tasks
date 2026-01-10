---
title: Comment faire en sorte que votre application React Native réponde élégamment
  lorsque le clavier apparaît
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-24T04:14:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-react-native-app-respond-gracefully-when-the-keyboard-pops-up-7442c1535580
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gQEm5r-73VpwmSrHYRi0AQ.jpeg
tags:
- name: animation
  slug: animation
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: Comment faire en sorte que votre application React Native réponde élégamment
  lorsque le clavier apparaît
seo_desc: 'By Spencer Carli

  When you’re working with React Native apps, a common problem is that the keyboard
  will pop up and hide text inputs when you focus on them. Something like this:


  There are a few ways you can avoid this. Some are simple, some less so. ...'
---

Par Spencer Carli

Lorsque vous travaillez avec des applications React Native, un problème courant est que le clavier apparaît et masque les champs de texte lorsque vous les sélectionnez. Quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dcFgfha_NfuPIi4YqEnsmQ.gif)

Il existe plusieurs façons d'éviter cela. Certaines sont simples, d'autres moins. Certaines peuvent être personnalisées, d'autres non. Aujourd'hui, je vais vous montrer 3 façons différentes d'éviter le problème du clavier dans React Native.

> _J'ai mis tout le code source de ce tutoriel [sur Github](https://github.com/spencercarli/react-native-keyboard-avoidance-examples)._

#### KeyboardAvoidingView

La solution la plus simple et la plus facile à installer est [KeyboardAvoidingView](https://facebook.github.io/react-native/docs/keyboardavoidingview.html). C'est un composant de base, mais il est aussi assez simple dans ce qu'il fait.

Vous pouvez prendre le [code de base](https://gist.github.com/spencercarli/8acb7208090f759b0fc2fda3394796f1), qui a le clavier couvrant les champs de saisie, et le mettre à jour pour que les champs ne soient plus couverts. La première chose à faire est de remplacer le conteneur `View` par `KeyboardAvoidingView` et d'ajouter une propriété `behavior`. Si vous regardez la documentation, vous verrez qu'il accepte 3 valeurs différentes — _height, padding, position_. J'ai trouvé que _padding_ fonctionne de la manière la plus prévisible. C'est donc ce que j'utiliserai.

```jsx
import React from 'react';
import { View, TextInput, Image, KeyboardAvoidingView } from 'react-native';
import styles from './styles';
import logo from './logo.png';

const Demo = () => {
  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior="padding"
    >
      <Image source={logo} style={styles.logo} />
      <TextInput
        placeholder="Email"
        style={styles.input}
      />
      <TextInput
        placeholder="Nom d'utilisateur"
        style={styles.input}
      />
      <TextInput
        placeholder="Mot de passe"
        style={styles.input}
      />
      <TextInput
        placeholder="Confirmer le mot de passe"
        style={styles.input}
      />
      <View style={{ height: 60 }} />
    </KeyboardAvoidingView>
  );
};

export default Demo;
```

Cela nous donne le résultat suivant. Ce n'est pas parfait, mais pour presque aucun travail, c'est assez bien.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YrvCTP6RN8zn7r7W1lJtuQ.gif)

Une chose à noter est qu'à la ligne 30, vous verrez un `View` qui a une hauteur définie à 60px. J'ai trouvé que la vue d'évitement du clavier ne fonctionne pas tout à fait avec le dernier élément, et la définition de la marge ou du remplissage n'a pas fonctionné. J'ai donc ajouté un nouvel élément pour "déplacer" tout de quelques pixels.

L'image en haut est poussée hors de la vue lors de l'utilisation de cette implémentation simple. Je vais vous montrer comment vous pouvez corriger cela à la fin.

> _Utilisateurs d'Android : J'ai trouvé que c'était la meilleure/seule option. En ajoutant `android:windowSoftInputMode="adjustResize"` à votre AndroidManifest.xml, le système d'exploitation s'occupera de la plupart du travail pour vous et le KeyboardAvoidingView s'occupera du reste. [Exemple AndroidManifest.xml](https://gist.github.com/spencercarli/e1b9575c1c8845c2c20b86415dfba3db#file-androidmanifest-xml-L23). Le reste de cet article ne s'appliquera probablement pas à vous._

#### Keyboard Aware ScrollView

L'option suivante est [react-native-keyboard-aware-scroll-view](https://github.com/APSL/react-native-keyboard-aware-scroll-view), qui offre beaucoup pour votre argent. En arrière-plan, il utilise un ScrollView ou ListView pour tout gérer (selon le composant que vous choisissez), ce qui rend l'interaction de défilement assez fluide. L'autre avantage majeur de ce package est qu'il fait défiler jusqu'au champ de saisie qui est en focus, ce qui offre une bonne expérience utilisateur.

L'utilisation est également très facile — vous devez simplement remplacer le conteneur `View`, en commençant à nouveau par le [code de base](https://gist.github.com/spencercarli/8acb7208090f759b0fc2fda3394796f1), et définir quelques options. Voici le code, puis je le décrirai.

```jsx
import React from 'react';
import { View, TextInput, Image } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import styles from './styles';
import logo from './logo.png';

const Demo = () => {
  return (
    <KeyboardAwareScrollView
      style={{ backgroundColor: '#4c69a5' }}
      resetScrollToCoords={{ x: 0, y: 0 }}
      contentContainerStyle={styles.container}
      scrollEnabled={false}
    >
        <Image source={logo} style={styles.logo} />
        <TextInput
          placeholder="Email"
          style={styles.input}
        />
        <TextInput
          placeholder="Nom d'utilisateur"
          style={styles.input}
        />
        <TextInput
          placeholder="Mot de passe"
          style={styles.input}
        />
        <TextInput
          placeholder="Confirmer le mot de passe"
          style={styles.input}
        />
    </KeyboardAwareScrollView>
  );
};

export default Demo;
```

Tout d'abord, vous voulez définir la _backgroundColor_ du ScrollView de cette manière (si vous réactivez le défilement) la backgroundColor est toujours la même. Ensuite, vous voulez indiquer au composant où se trouve la position par défaut afin que, une fois le clavier fermé, il revienne à cet endroit — en omettant cette propriété, la vue pourrait rester bloquée en haut après la fermeture du clavier, comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WzOzG3P9npDpHpFj896nXA.png)

Après la propriété _resetScrollToCoords_, vous définissez le _contentContainerStyle_ — cela remplace essentiellement les styles du conteneur `View` que vous aviez auparavant. La dernière chose que je fais est de désactiver le défilement par interaction utilisateur. Cela n'a peut-être pas toujours de sens pour votre interface utilisateur (comme une interface où un utilisateur modifie de nombreux champs de profil), mais pour celle-ci, cela en a, il n'est pas très logique de permettre à l'utilisateur de faire défiler manuellement car il n'y a rien à faire défiler.

En combinant ces propriétés, vous obtenez le résultat suivant, qui fonctionne assez bien.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M64W128GRs8X2IaBbSv7sA.gif)

#### Module Keyboard

C'est de loin l'option la plus manuelle, mais elle vous donne aussi le plus de contrôle. Vous utiliserez la bibliothèque Animated pour aider à donner des interactions fluides comme vous l'avez vu précédemment.

Le module Keyboard, qui n'est pas documenté sur le site React Native, vous permet d'écouter les événements du clavier émis par l'appareil. Les événements que vous utiliserez sont _keyboardWillShow_ et _keyboardWillHide_, qui retournent la durée de l'animation et la position finale du clavier (entre autres informations).

> Si vous êtes sur Android, vous voudrez utiliser keyboardDidShow et keyboardDidHide à la place.

Lorsque l'événement _keyboardWillShow_ est émis, vous définirez une variable animée à la hauteur finale du clavier et la ferez animer pendant la même durée que l'animation de glissement du clavier. Vous utilisez ensuite cette valeur animée pour définir un remplissage en bas du conteneur pour déplacer tout le contenu vers le haut.

Je vais montrer le code dans un instant, mais faire ce que j'ai décrit ci-dessus nous laisse avec cette expérience.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mOhomWU9OwZN8Kieq3Pezw.gif)

Cette fois, je veux corriger cette image. Pour ce faire, vous utiliserez une valeur animée pour gérer la hauteur de l'image, que vous ajusterez lorsque le clavier sera ouvert. Voici le code.

```jsx
import React, { Component } from 'react';
import { View, TextInput, Image, Animated, Keyboard } from 'react-native';
import styles, { IMAGE_HEIGHT, IMAGE_HEIGHT_SMALL} from './styles';
import logo from './logo.png';

class Demo extends Component {
  constructor(props) {
    super(props);

    this.keyboardHeight = new Animated.Value(0);
    this.imageHeight = new Animated.Value(IMAGE_HEIGHT);
  }

  componentWillMount () {
    this.keyboardWillShowSub = Keyboard.addListener('keyboardWillShow', this.keyboardWillShow);
    this.keyboardWillHideSub = Keyboard.addListener('keyboardWillHide', this.keyboardWillHide);
  }

  componentWillUnmount() {
    this.keyboardWillShowSub.remove();
    this.keyboardWillHideSub.remove();
  }

  keyboardWillShow = (event) => {
    Animated.parallel([
      Animated.timing(this.keyboardHeight, {
        duration: event.duration,
        toValue: event.endCoordinates.height,
      }),
      Animated.timing(this.imageHeight, {
        duration: event.duration,
        toValue: IMAGE_HEIGHT_SMALL,
      }),
    ]).start();
  };

  keyboardWillHide = (event) => {
    Animated.parallel([
      Animated.timing(this.keyboardHeight, {
        duration: event.duration,
        toValue: 0,
      }),
      Animated.timing(this.imageHeight, {
        duration: event.duration,
        toValue: IMAGE_HEIGHT,
      }),
    ]).start();
  };

  render() {
    return (
      <Animated.View style={[styles.container, { paddingBottom: this.keyboardHeight }]}>
        <Animated.Image source={logo} style={[styles.logo, { height: this.imageHeight }]} />
        <TextInput
          placeholder="Email"
          style={styles.input}
        />
        <TextInput
          placeholder="Nom d'utilisateur"
          style={styles.input}
        />
        <TextInput
          placeholder="Mot de passe"
          style={styles.input}
        />
        <TextInput
          placeholder="Confirmer le mot de passe"
          style={styles.input}
        />
      </Animated.View>
    );
  }
};

export default Demo;
```

Il y a certainement beaucoup plus à faire que pour les autres solutions. Au lieu d'une `View` ou `Image` normale, vous utilisez une `Animated.View` et `Animated.Image` afin que les valeurs animées puissent être exploitées. La partie amusante se trouve vraiment dans les fonctions _keyboardWillShow_ et _keyboardWillHide_ où les valeurs animées changent.

Ce qui se passe là, c'est que deux valeurs animées changent en parallèle, qui sont ensuite utilisées pour piloter l'interface utilisateur. Cela vous laisse avec ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fj87SXCLXlkKsG7aAi_5mg.gif)

C'est un peu plus de code, mais c'est assez élégant. Vous avez beaucoup d'options pour ce que vous pouvez faire et pouvez vraiment personnaliser l'interaction à votre guise.

#### Combinaison des options

Si vous voulez économiser du code, vous pouvez combiner quelques options, ce que je tends à faire. Par exemple, en combinant l'option 1 et 3, vous n'avez à vous soucier que de la gestion et de l'animation de la hauteur de l'image.

Le code n'est pas beaucoup moins que la source de l'option 3, mais à mesure qu'une interface utilisateur devient plus complexe, cela peut vous aider un peu.

```jsx
import React, { Component } from 'react';
import { View, TextInput, Image, Animated, Keyboard, KeyboardAvoidingView } from 'react-native';
import styles, { IMAGE_HEIGHT, IMAGE_HEIGHT_SMALL } from './styles';
import logo from './logo.png';

class Demo extends Component {
  constructor(props) {
    super(props);

    this.imageHeight = new Animated.Value(IMAGE_HEIGHT);
  }

  componentWillMount () {
    this.keyboardWillShowSub = Keyboard.addListener('keyboardWillShow', this.keyboardWillShow);
    this.keyboardWillHideSub = Keyboard.addListener('keyboardWillHide', this.keyboardWillHide);
  }

  componentWillUnmount() {
    this.keyboardWillShowSub.remove();
    this.keyboardWillHideSub.remove();
  }

  keyboardWillShow = (event) => {
    Animated.timing(this.imageHeight, {
      duration: event.duration,
      toValue: IMAGE_HEIGHT_SMALL,
    }).start();
  };

  keyboardWillHide = (event) => {
    Animated.timing(this.imageHeight, {
      duration: event.duration,
      toValue: IMAGE_HEIGHT,
    }).start();
  };

  render() {
    return (
      <KeyboardAvoidingView
        style={styles.container}
        behavior="padding"
      >
          <Animated.Image source={logo} style={[styles.logo, { height: this.imageHeight }]} />
          <TextInput
            placeholder="Email"
            style={styles.input}
          />
          <TextInput
            placeholder="Nom d'utilisateur"
            style={styles.input}
          />
          <TextInput
            placeholder="Mot de passe"
            style={styles.input}
          />
          <TextInput
            placeholder="Confirmer le mot de passe"
            style={styles.input}
          />
      </KeyboardAvoidingView>
    );
  }
};

export default Demo;
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*g3clh5FFPJzBWt9egIY2cA.gif)

Chaque implémentation a ses avantages et ses inconvénients — vous devrez choisir la plus appropriée en fonction de l'expérience utilisateur que vous visez.

> Êtes-vous intéressé à en savoir plus sur l'utilisation de React Native pour créer des applications mobiles de haute qualité ? [Inscrivez-vous à mon cours gratuit sur React Native](http://learn.handlebarlabs.com/p/react-native-basics-build-a-currency-converter) !