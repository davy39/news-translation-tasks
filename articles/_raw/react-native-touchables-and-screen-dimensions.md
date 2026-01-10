---
title: React Native – Touchables and Screen Dimensions
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
seo_title: null
seo_desc: React Native makes the process of developing an application that works on
  both Android and iOS devices much easier than it once was. While before you had
  to work with at least two programming languages and vastly different APIs, React
  Native includes...
---

React Native makes the process of developing an application that works on both Android and iOS devices much easier than it once was. While before you had to work with at least two programming languages and vastly different APIs, React Native includes some helpful ones out of the box.

Here's a rundown of two that will help you build your next app.

## Touchables

Some of the main features of mobile devices revolve around user touch interactions. How a mobile app handles and responds to these interactions can make or break the user’s experience.

React Native ships with a `Button` component which works for many standard `onPress` interactions. By default, it will give the user feedback by changing the opacity to show the button was pressed. Usage:

```js
<Button onPress={handlePress} title="Submit" />
```

For more complex use cases, React Native has APIs build in to handle press interactions called `Touchables`.

```text
TouchableHighlight
TouchableNativeFeedback
TouchableOpacity
TouchableWithoutFeedback
```

Each of these Touchable components can be styled and used with a library, like the built-in `Animated`, allowing you to make your own types of custom user feedback.

Some examples of using these components:

```js
// with images
<TouchableHighlight onPress={this.handlePress}>
  <Image
    style={styles.button}
    source={require('./logo.png')}
  />
</TouchableHighlight>

// with text
<TouchableHighlight onPress={this.handlePress}>
  <Text>Hello</Text>
</TouchableHighlight>
```

You can handle different types of button presses as well. By default, buttons and touchables are configured to handle regular taps, but you can also denote a function to call for press and hold interactions for example.

```js
<TouchableHighlight onPress={this.handlePress} onLongPress={this.handleLongPress}>
```

To see all of the available props and how these components work, you can look at [the JavaScript source code for Touchables here](https://github.com/facebook/react-native/tree/master/Libraries/Components/Touchable).

## Screen Dimensions

React Native uses Dots Per Inch (DPI) to measure the sizing of the User Interface (UI) and anything displayed on the UI. This type of measurement allows an application to look uniform across various screen sizes and pixel densities.

For standard use cases, applications can be developed without having to know the specifics of the user’s device (for example, pixel density) since the UI elements will scale automatically. 

When it is required, there are APIs available such as `PixelRatio` to help you find out the pixel density of the user's device.

To get the window or screen height/width of a user's device, React Native has an API called `Dimensions`.

```js
import { Dimensions } from 'react-native';
```

Here are the methods that the `Dimensions` API provides:

```js
Dimensions.get('window').height;
Dimensions.get('window').width;
Dimensions.get('screen').height;
Dimensions.get('screen').width;
```

**Note:** There have been some known issues in the past with the Dimensions API such as not returning the correct information when a user rotates their device. It’s best to make sure you test this on actual devices before deploying an application.

### More info on responsive design:

* [Free responsive design course](https://www.freecodecamp.org/news/master-responsive-website-design/)
* [Best Bootstrap tutorials for responsive web design](https://www.freecodecamp.org/news/p/f401cbed-6c27-46e5-a56f-c9853b87e244/freecodecamp.org/news/best-bootstrap-tutorial-responsive-web-design/)
* [How to think responsively](https://www.freecodecamp.org/news/how-to-start-thinking-responsively/)
* [Guide to responsive images](https://www.freecodecamp.org/news/your-complete-guide-to-truly-responsive-images/)
* [Learn responsive design in 5 minutes](https://www.freecodecamp.org/news/learn-responsive-web-design-in-5-minutes/)


