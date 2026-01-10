---
title: How to create a beautifully animated loader in React Native
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
seo_title: null
seo_desc: 'By Vikrant Negi

  Use Airbnb’s Lottie library to jazz up your loaders.


  Lottie Animation for Loaders

  A loader in Web or Mobile is an essential design element usually used when we need
  to perform some asynchronous task like data processing or fetching. ...'
---

By Vikrant Negi

#### Use Airbnb’s [Lottie](https://airbnb.design/lottie/) library to jazz up your loaders.

![Image](https://cdn-media-1.freecodecamp.org/images/D7aU6jFKntF2FdAchdkb9AUmUUpjjBZiP4On)
_Lottie Animation for Loaders_

A loader in Web or Mobile is an essential design element usually used when we need to perform some asynchronous task like data processing or fetching. Since these tasks may take some time and users must be entertained during this time, this is where loaders come in handy.

Loaders help developers keep the user engaged while they wait and avoid any lack of responsiveness in the app. ?

> Don’t want to wait? Check out the npm package [React-Native-Animated-Loader](https://github.com/vikrantnegi/react-native-animated-loader).

#### Getting Started

React Native has an `[ActivityIndicator](https://facebook.github.io/react-native/docs/activityindicator)` built in which can be used as a loading indicator.

But for `Loaders` we can’t just use `ActivityIndicator` as we want to prevent the user from performing any action until the task is complete. And for this, we’ll use `[Modals](https://facebook.github.io/react-native/docs/modal#docsNav)`.

If you just want a plain, simple loader, then check out [this](https://medium.com/@kelleyannerose/react-native-activityindicator-for-a-quick-easy-loading-animation-593c06c044dc) tutorial.

But if you want some awesomeness ? sprinkled into your loaders, continue with the tutorial. ?

#### Airbnb’s Lottie ?

[Lottie](https://airbnb.design/lottie/) is an iOS, Android, and React Native library that renders After Effects animations in real time, allowing apps to use animations as easily as they use static images.

We are going to use its React Native wrapper library [lottie-react-native](https://github.com/react-native-community/lottie-react-native) for our custom loader animation.

#### Create an App

We are going to use `react-native-cli` to create a React Native project, but you can use Expo as well.

Create an example project with the following command:

```
~ react-native init LoaderExample
```

#### Install Dependencies

Now let’s add the necessary packages. First Install `react-native-animated-loader` and `lottie-react-native`.

```
~ npm install react-native-animated-loader --save
```

```
~ npm i --save lottie-react-native
```

> If you are using Expo you don’t need to install Lottie.

Since `lottie-react-native` requires native linking, run the following commands:

```
~ react-native link lottie-ios
```

```
~ react-native link lottie-react-native
```

After this, open the Xcode project configuration and add the `Lottie.framework` as `Embedded Binaries`.

> If you face any error after linking Lottie, following the detailed installation instructions [here](https://github.com/react-native-community/lottie-react-native/blob/master/README.md#getting-started).

#### Let’s add magic ?

Now update your `App.js` with the following code:

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
    return (      <View style={styles.container}>        <AnimatedLoader          visible={visible}          overlayColor="rgba(255,255,255,0.75)"          animationStyle={styles.lottie}          speed={1}        />        &lt;Button title="press" onPress={this.handlePress} />      </View>    );  }}
```

```
const styles = StyleSheet.create({  container: {    flex: 1,    justifyContent: 'center',    alignItems: 'center',    backgroundColor: '#F5FCFF',  },  lottie: {    width: 100,    height: 100,  },});
```

When you click you should the following animation within a few seconds.

![Image](https://cdn-media-1.freecodecamp.org/images/746QhP7tWnW-IRfc5QQw9kTRV9cQZ7whLI43)

#### Customize Animation

The animation you see is the default, but you can add your own Lottie animation. If you want to find some cool loader animations, go to [lottiefiles](https://lottiefiles.com/), where you can find some pre-built loader animations. Just choose the one you like and download its JSON file.

Now add the downloaded JSON file to the `LoaderExample` project and add source prop to the `AnimatedLoader`. After adding the source it should look like this:

```
<AnimatedLoader  visible={visible}  overlayColor="rgba(255,255,255,0.75)"  animationStyle={styles.lottie}  speed={1}  source={require("./path-of-your-json-file.json")} // Add here/>
```

You can also customize the loader styles by adding `animationStyle` prop.

#### Usage

In our example, I’ve used `setTimeout` to mimic an Asynchronous task. In the real world, you would be using it for all sorts of asynchronous tasks like fetching data from an API.

#### Conclusion

Now you know how to make a cool animated loader, I hope you’ll stop using the old, boring activity indicator for your loaders.

> Find the library repo [here](https://github.com/vikrantnegi/react-native-animated-loader).

If you like this article, go ahead and show some love with your claps.

Check out my other articles on React Native:

* R[eact Native FlatList with realtime searching ability](https://medium.freecodecamp.org/how-to-build-a-react-native-flatlist-with-realtime-searching-ability-81ad100f6699)
* [React Native Location Tracking](https://medium.com/quick-code/react-native-location-tracking-14ab2c9e2db8)
* [React Native charts with dynamic tooltips](https://medium.freecodecamp.org/how-to-build-react-native-charts-with-dynamic-tooltips-64aefc550c95)

