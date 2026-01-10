---
title: How to Handle Navigation in React Native with react-navigation 5
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
seo_title: null
seo_desc: "By Said Hayani\nReact-navigation is the navigation library that comes to\
  \ my mind when we talk about navigation in React Native. \nI'm a big fan of this\
  \ library and it's always the first solution I use to handle navigation in React\
  \ Native. This is in pa..."
---

By Said Hayani

React-navigation is the navigation library that comes to my mind when we talk about navigation in React Native. 

I'm a big fan of this library and it's always the first solution I use to handle navigation in React Native. This is in part becausae it has an awesome and easy API and is very customizable. 

I'm writing this article because version 5 just went from beta to stable. It comes with some feature changes and a new API design that provides a simple and different way to declare routes.

In this article, we are going to go through the new APIs and look at ways to use them in our applications.

> Originally published on [saidhayani.com](https://saidhayani.com/Introducing-react-navigation-5/)


## Installing

The way you install react-navigation has changed a little bet compared to previous versions (>4.x):

```shell
// > 4.x verions
yarn add react-navigation
```

Installing react-navigation 5 will look like this:

```shell
// yarn
yarn add @react-navigation/native
// npm
npm install @react-navigation/native
```

The latest versions of react-navigation use many third party library like [react-native-gesture-handler](https://github.com/software-mansion/react-native-gesture-handler) for animation and handling transitions. So you always need to install those libraries.

```shell
// yarn
yarn add react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
// npm
npm install react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
```

## Dynamic screens

The new API introduces dynamism in initializing routes. Previously it was done statically - basically, we had to define our Routes in a config file.

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

The new API comes with dynamic components. and made the navigation to be more dynamic.
The new way to declare the Routes will be much like the following.

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

This new way is dynamic, simpler to use, and is kinda similar to react-router API.

## Dynamic options

This has been the most requested feature by the community for a long time. I always had issues with the old method (static) and it was really hard to change the navigation behavior dynamically.

### The old method => < 4.x

With older versions of [react-navigation](https://reactnavigation.org/) we had to define static options. And there was no way to change this dynamically.

```js
  static navigationOptions = {
    title: "Sign In",
    header: null,
    mode: "modal",
    headerMode: "none"
  };
```

### The new method (version 5)

React-navigation comes with a dynamic method which is quite simple. We can set the options to any screen using just `props`.

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

With dynamic options, I can change the title based on authentication. For example if the user is authenticated, I can set the screen title to be the user’s username, or I can change the backgroundColor for the header. 

This is more useful especially if you are using dynamic themes or if you are willing to implement dark mode in your app.

## Hooks

This is my favorite feature so far, and it’s a time-saver. The new API introduced some custom hooks to perform certain actions.

In previous versions, for example, if I had to get the currentName of the active screen, I had to create some helpers to do that for me pretty much like the following.

```jsx
export function getCurrentRouteName(): string | null {
  const tag = "[getCurrentRouteNameSync] "
  const navState = getStore().getState().nav
  const currentRoute = getActiveRouteState(navState)
  console.log(tag + " currentRoute > ", currentRoute)
  return currentRoute && currentRoute.routeName ? currentRoute.routeName : null
}
```

The hooks API helps me avoid all these things and makes it easier for me to access the Navigation API with one single line using a hook.

Now I can easily get the RouteName using `useRoute` Hook.

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
      {/*    Display the RouteName here */}
      <Text style={styles.title}>{route.name}</Text>
    </View>
  )
}
```

We can do the same thing with the `useNavigationState` Hook. It gives us access to the navigation state.

```js
const navigationState = useNavigationState(state => state)
let index = navigationState.index
let routes = navigationState.routes.length
console.log(index)
console.log(routes)
```

React-navigation offers other hooks as well, for example:

- `useFocuseEffect` : a side effect hook that, when the screens are loaded, returns the focused screen
- `useLinking`: handles deepLinking

I highly recommend that you [check them out](https://reactnavigation.org/docs/use-navigation/).

## Wrapping Up

The new react-navigation API definitely moves from static to dynamic. It’s a great direction that will absolutely change the way we handle navigation in React Native. Dynamic routes were a major request by react-navigation users, and this new way will help us create a better user navigation experience.

### You can find more content about [React Native here](https://saidhayani.com/)

> Thanks for reading

- [Twitter](https://twitter.com/SaidHYN)
- [GitHub](https://github.com/hayanisaid)
- [Join the mail-list](https://webege.us16.list-manage.com/subscribe?u=311846a57d1e1a666287ad128&id=2b386b2ebb)


> Looking for a React Native developer for your project? **[Hit me up](mailto:info.said.dev@gmail.com)**.

