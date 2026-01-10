---
title: 'Style React Native : Styled Components, Flexbox Layouts et plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-12T19:53:00.000Z'
originalURL: https://freecodecamp.org/news/react-native-styling-styled-components-flexbox-layouts-and-more
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df2740569d1a4ca3a8a.jpg
tags:
- name: flexbox
  slug: flexbox
- name: React Native
  slug: react-native
- name: styled-components
  slug: styled-components
seo_title: 'Style React Native : Styled Components, Flexbox Layouts et plus'
seo_desc: "React Native provides an API for creating stylesheets and styling your\
  \ components: StyleSheet.\nimport React, { Component } from 'react';\nimport { StyleSheet,\
  \ View, Text } from 'react-native';\n\nexport default class App extends Component\
  \ {\n  render () ..."
---

React Native fournit une API pour créer des feuilles de style et styliser vos composants : [StyleSheet](https://facebook.github.io/react-native/docs/stylesheet).

```jsx
import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';

export default class App extends Component {
  render () {
    return (
      <View>
        <Text style={styles.header}>Je suis un en-tête !</Text>
        <Text style={styles.text}>Je suis un texte bleu.</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  header: {
    fontSize: 20
  },
  text: {
    color: 'blue'
  }
});
```

Bien que les feuilles de style CSS régulières ne soient pas valides, le sur-ensemble de CSS de React Native est très similaire au CSS traditionnel.

De nombreuses propriétés CSS (par exemple, `color`, `height`, `top`, `right`, `bottom`, `left`) sont les mêmes dans StyleSheet. Toutes les propriétés CSS qui contiennent des tirets (par exemple, `font-size`, `background-color`) doivent être converties en camelCase (par exemple, `fontSize`, `backgroundColor`).

Toutes les propriétés CSS n'existent pas dans StyleSheet. Comme il n'y a pas de vrai concept de survol sur les appareils mobiles, les propriétés CSS de survol n'existent pas dans React Native. À la place, React Native fournit des [composants tactiles](https://facebook.github.io/react-native/docs/handling-touches#touchables) qui répondent aux événements tactiles.

Les styles ne sont pas non plus hérités comme dans le CSS traditionnel. Dans la plupart des cas, vous devez déclarer le style de chaque composant.

## Dispositions Flexbox

React Native utilise une implémentation de [flexbox](https://facebook.github.io/react-native/docs/flexbox) similaire à la norme web. Par défaut, les éléments de la vue seront définis sur `display: flex`.

Si vous ne souhaitez pas utiliser flexbox, vous pouvez également organiser les composants React Native via un positionnement `relative` ou `absolute`.

Flexbox dans React Native utilise par défaut `flexDirection: column`, au lieu de `flex-direction: row` (norme web). La valeur `column` affiche les éléments flexibles verticalement, ce qui convient aux appareils mobiles en orientation portrait.

Pour en savoir plus sur flexbox, consultez [ce guide détaillé sur CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) et une approche d'apprentissage ludique avec [Flexbox Froggy](http://flexboxfroggy.com/).

## Composants stylisés

Inclure de nombreux styles dans un fichier avec un composant n'est pas toujours facile à maintenir. Les composants stylisés peuvent résoudre ce problème.

Par exemple, un composant Button peut être utilisé à plusieurs endroits dans une application. Copier et coller l'objet de style avec chaque instance de Button serait inefficace. Au lieu de cela, créez un composant Button stylisé et réutilisable :

```jsx
import React from 'react';
import { Text, TouchableOpacity } from 'react-native';

const Button = ({ onPress, children }) => {
  const { buttonStyle, textStyle } = styles;
  return (
    <TouchableOpacity onPress={onPress} style={buttonStyle}>
      <Text style={textStyle}>
        {children}
      </Text>
    </TouchableOpacity>
  );
};

export default Button;

const styles = {
  textStyle: {
    alignSelf: 'center',
    color: '#336633',
    fontSize: 16,
    fontWeight: '600',
    paddingTop: 10,
    paddingBottom: 10
  },
  buttonStyle: {
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#336633',
    paddingTop: 4,
    paddingBottom: 4,
    paddingRight: 25,
    paddingLeft: 25,
    marginTop: 10,
    width: 300
  }
};
```

Le composant Button stylisé peut être facilement importé et utilisé dans toute l'application sans avoir à déclarer à plusieurs reprises l'objet de style :

```jsx
import React, { Component } from 'react';
import { TextInput, View } from 'react-native';
import Button from './styling/Button';

export default class Login extends Component {
  render() {
    return (
        <View>
          <TextInput placeholder='Nom d\'utilisateur ou Email' />
          <TextInput placeholder='Mot de passe' />
          <Button>Se connecter</Button>
        </View>
    );
  }
}
```

## Bibliothèques pour le style

Il existe plusieurs bibliothèques populaires pour styliser React Native. Certaines d'entre elles fournissent des fonctionnalités similaires à [Bootstrap](https://guide.freecodecamp.org/bootstrap/index.md), y compris des formulaires par défaut, des styles de boutons et des options de mise en page.

L'une des bibliothèques les plus populaires est [styled-components](https://github.com/styled-components/styled-components). Il en existe beaucoup d'autres que vous pouvez trouver sur npm et GitHub pour essayer par vous-même.