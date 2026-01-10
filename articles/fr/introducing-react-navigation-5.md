---
title: Comment gérer la navigation dans React Native avec react-navigation 5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-23T19:24:43.000Z'
originalURL: https://freecodecamp.org/news/introducing-react-navigation-5
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/react-navigation5-featured-1.png
tags:
- name: React navigation 5
  slug: react-navigation-5
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: programming languages
  slug: programming-languages
- name: react hooks
  slug: react-hooks
- name: React Native
  slug: react-native
- name: react-navigation
  slug: react-navigation
- name: technology
  slug: technology
seo_title: Comment gérer la navigation dans React Native avec react-navigation 5
seo_desc: "By Said Hayani\nReact-navigation is the navigation library that comes to\
  \ my mind when we talk about navigation in React Native. \nI'm a big fan of this\
  \ library and it's always the first solution I use to handle navigation in React\
  \ Native. This is in pa..."
---

Par Said Hayani

React-navigation est la bibliothèque de navigation qui me vient à l'esprit lorsque nous parlons de navigation dans React Native. 

Je suis un grand fan de cette bibliothèque et c'est toujours la première solution que j'utilise pour gérer la navigation dans React Native. Cela est en partie dû au fait qu'elle dispose d'une API formidable et facile à utiliser, et qu'elle est très personnalisable. 

J'écris cet article parce que la version 5 vient de passer de la version bêta à la version stable. Elle apporte des changements de fonctionnalités et une nouvelle conception d'API qui offre une manière simple et différente de déclarer les routes.

Dans cet article, nous allons passer en revue les nouvelles API et examiner les moyens de les utiliser dans nos applications.

> Originalement publié sur [saidhayani.com](https://saidhayani.com/Introducing-react-navigation-5/)


## Installation

La manière d'installer react-navigation a un peu changé par rapport aux versions précédentes (>4.x) :

```shell
// > 4.x verions
yarn add react-navigation
```

L'installation de react-navigation 5 se fera comme suit :

```shell
// yarn
yarn add @react-navigation/native
// npm
npm install @react-navigation/native
```

Les dernières versions de react-navigation utilisent de nombreuses bibliothèques tierces comme [react-native-gesture-handler](https://github.com/software-mansion/react-native-gesture-handler) pour l'animation et la gestion des transitions. Vous devez donc toujours installer ces bibliothèques.

```shell
// yarn
yarn add react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
// npm
npm install react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
```

## Écrans dynamiques

La nouvelle API introduit le dynamisme dans l'initialisation des routes. Auparavant, cela se faisait de manière statique - en gros, nous devions définir nos routes dans un fichier de configuration.

```jsx
// @flow
import React from "react";

import { createAppContainer, createSwitchNavigator } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";


/** ---------Screens----------- */
// import LaunchScreen from "../Containers/LaunchScreen";
import HomeScreen from "../Containers/HomeScreen";

import ProfileScreen from "../Containers/ProfileScreen";
import LoginScreen from "../Containers/LoginScreen";






const StackNavigator = createStackNavigator(
  {
    initialRouteName: "Home"
  },
  {
    Home: {
      screen: HomeScreen
    },
     Login: {
      screen: LoginScreen,
      headerMode: "none",

    },
      Profile: {
      screen: ProfileScreen
    }



);

export default createAppContainer(StackNavigator);
```

La nouvelle API vient avec des composants dynamiques et rend la navigation plus dynamique.
La nouvelle façon de déclarer les routes sera beaucoup comme suit.

```jsx
import React from "react"
import { SafeAreaView, StyleSheet, View, Text, StatusBar } from "react-native"

import { NavigationContainer } from "@react-navigation/native"
import { createStackNavigator } from "@react-navigation/stack"

const App: () => React$Node = () => {
  return (
    <>
      <StatusBar barStyle="dark-content" />
      <SafeAreaView style={styles.containerStyle}>
        <AppNavigation />
      </SafeAreaView>
    </>
  )
}
const Stack = createStackNavigator()
const AppNavigation = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="home">
        <Stack.Screen name="home" component={HomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  )
}
const HomeScreen = () => {
  return (
    <View style={styles.containerStyle}>
      <Text style={styles.title}>Home Screen</Text>
    </View>
  )
}
```

![react-navigation5-demo](https://www.freecodecamp.org/news/content/images/2020/03/react-navigation5-demo.gif)

Cette nouvelle méthode est dynamique, plus simple à utiliser et assez similaire à l'API react-router.

## Options dynamiques

Cela a été la fonctionnalité la plus demandée par la communauté depuis longtemps. J'ai toujours eu des problèmes avec l'ancienne méthode (statique) et il était vraiment difficile de changer dynamiquement le comportement de la navigation.

### L'ancienne méthode => < 4.x

Avec les anciennes versions de [react-navigation](https://reactnavigation.org/), nous devions définir des options statiques. Et il n'y avait aucun moyen de changer cela dynamiquement.

```js
  static navigationOptions = {
    title: "Sign In",
    header: null,
    mode: "modal",
    headerMode: "none"
  };
```

### La nouvelle méthode (version 5)

React-navigation vient avec une méthode dynamique qui est assez simple. Nous pouvons définir les options pour n'importe quel écran en utilisant simplement `props`.

```jsx
const AppNavigation = ({}) => {
  let auth = {
    authenticated: true,
    user: {
      email: "user@mail.com",
      username: "John",
    },
  }
  let ProfileScreenTitle = auth.authenticated ? auth.user.username : "Profile"
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen
          name="Profile"
          component={ProfileScreen}
          options={{
            title: ProfileScreenTitle,
            headerTintColor: "#4aa3ba",
            headerStyle: {
              backgroundColor: darkModeOn ? "#000" : "#fff",
            },
          }}
        />
        <Stack.Screen name="About" component={AboutScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  )
}
```

![react-navigation-header](https://www.freecodecamp.org/news/content/images/2020/03/react-navigation-header.png)

Avec les options dynamiques, je peux changer le titre en fonction de l'authentification. Par exemple, si l'utilisateur est authentifié, je peux définir le titre de l'écran pour qu'il soit le nom d'utilisateur de l'utilisateur, ou je peux changer la couleur de fond pour l'en-tête. 

Cela est plus utile surtout si vous utilisez des thèmes dynamiques ou si vous souhaitez implémenter un mode sombre dans votre application.

## Hooks

C'est ma fonctionnalité préférée jusqu'à présent, et c'est un gain de temps. La nouvelle API a introduit certains hooks personnalisés pour effectuer certaines actions.

Dans les versions précédentes, par exemple, si je devais obtenir le currentName de l'écran actif, je devais créer des helpers pour le faire pour moi, un peu comme suit.

```jsx
export function getCurrentRouteName(): string | null {
  const tag = "[getCurrentRouteNameSync] "
  const navState = getStore().getState().nav
  const currentRoute = getActiveRouteState(navState)
  console.log(tag + " currentRoute > ", currentRoute)
  return currentRoute && currentRoute.routeName ? currentRoute.routeName : null
}
```

L'API des hooks m'aide à éviter toutes ces choses et me permet d'accéder plus facilement à l'API de navigation avec une seule ligne en utilisant un hook.

Maintenant, je peux facilement obtenir le RouteName en utilisant le hook `useRoute`.

```jsx
import { useRoute } from "@react-navigation/native"
const AboutScreen = ({ navigation }) => {
  const route = useRoute()
  return (
    <View
      style={{
        justifyContent: "space-around",
        flex: 1,
        alignItems: "center",
      }}
    >
      {/*    Afficher le RouteName ici */}
      <Text style={styles.title}>{route.name}</Text>
    </View>
  )
}
```

Nous pouvons faire la même chose avec le hook `useNavigationState`. Il nous donne accès à l'état de navigation.

```js
const navigationState = useNavigationState(state => state)
let index = navigationState.index
let routes = navigationState.routes.length
console.log(index)
console.log(routes)
```

React-navigation offre d'autres hooks également, par exemple :

- `useFocuseEffect` : un hook d'effet secondaire qui, lorsque les écrans sont chargés, retourne l'écran focalisé
- `useLinking` : gère le deepLinking

Je vous recommande vivement de [les vérifier](https://reactnavigation.org/docs/use-navigation/).

## Conclusion

La nouvelle API react-navigation passe définitivement du statique au dynamique. C'est une excellente direction qui changera absolument la manière dont nous gérons la navigation dans React Native. Les routes dynamiques étaient une demande majeure des utilisateurs de react-navigation, et cette nouvelle méthode nous aidera à créer une meilleure expérience de navigation pour l'utilisateur.

### Vous pouvez trouver plus de contenu sur [React Native ici](https://saidhayani.com/)

> Merci pour la lecture

- [Twitter](https://twitter.com/SaidHYN)
- [GitHub](https://github.com/hayanisaid)
- [Rejoignez la liste de diffusion](https://webege.us16.list-manage.com/subscribe?u=311846a57d1e1a666287ad128&id=2b386b2ebb)


> Vous cherchez un développeur React Native pour votre projet ? **[Contactez-moi](mailto:info.said.dev@gmail.com)**.