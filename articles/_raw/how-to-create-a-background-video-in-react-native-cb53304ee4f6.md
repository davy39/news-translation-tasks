---
title: How to use video as a background in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T21:02:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-background-video-in-react-native-cb53304ee4f6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Y-yUIvkbgkWU7Tlm
tags:
- name: 100Days100Projects
  slug: 100days100projects
- name: coding
  slug: coding
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: React
  slug: reactjs
- name: technology
  slug: technology
- name: user experience
  slug: user-experience
- name: User Interface
  slug: user-interface
seo_title: null
seo_desc: 'By Said Hayani

  In this post, we are going to create a **backgroundVideo** in React Native. If you
  have just started with React Native check out my article What you need to know to
  start building mobile apps with React Native.


  Demo: Peleton Home Scre...'
---

By Said Hayani

In this post, we are going to create a `**backgroundVideo**` in React Native. If you have just started with React Native check out my article [What you need to know to start building mobile apps with React Nativ](https://medium.freecodecamp.org/what-you-need-to-know-to-start-building-mobile-apps-in-react-native-dded951277b7)e.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mOSwlhVAq7PTzOuc1J-Hpg.gif)
_Demo: Peleton Home Screen_

Background video can add a nice effect to the UI of an app. They may be helpful also if you want to display, for example, ads or send a message to the user, like we’ll do here.

You will need some basic requirements. To get started, you must have the react-native environment setup. That means you have:

* [react-native-cli](https://github.com/react-native-community/react-native-cli) installed
* Android SDK; if you have a mac you won’t need that, just Xcode

### Getting started

First things first, let’s bootstrap a new React Native app. In my case I’m using react-native-cli. So in your terminal run:

```
react-native init myapp
```

This should install all the dependencies and packages to run your React Native app.

Next step is to run and install the app on the simulator.

For iOS:

```
react-native run-ios
```

This should open up the iOS simulator.

On Android:

```
react-native run-android 
```

You may have some trouble with Android. I recommend that you use [Genymotion](https://www.genymotion.com/) and the Android emulator or check out [this friendly guide](https://medium.com/@sunilk/react-native-development-getting-started-with-android-and-ios-ada22e3d00b1) to set up the environment.

First what we are going to do is clone the Peleton app’s home screen. We are using `[**react-native-video**](https://github.com/react-native-community/react-native-video)` for video streaming, and `[**styled-component**](https://www.styled-components.com/docs/basics#react-native)` for styling. So you have to install them:

* Yarn:

```
yarn add react-native-video styled-components
```

* NPM

```
npm -i react-native-video styled-components --save
```

Then you need to link react-native-video because it contains native code — and for `**styled-components**` we don’t need that. So simply run:

```
react-native link
```

You don’t have to worry about the other things, just focus on the `Video` Component. First, import Video from react-native-video and start using it.

```js
import import Video from "react-native-video";
  <Video
source={require("./../assets/video1.mp4")}
style={styles.backgroundVideo}
muted={true}
repeat={true}
resizeMode={"cover"}
rate={1.0}
ignoreSilentSwitch={"obey"}
/>
```

Let’s break it down:

* **source**: the path to the source video. You can use the URL instead:

```
source={{uri:"https://youronlineVideo.mp4"}}
```

* **style:** the costume style we want to give to the video, and the key to making the background video
* resizeMode: in our case it is `cover`; you can try also `contain or stretch` but this won’t give us what we want

And other props are optional.

Let’s move to the important part: placing the video in the background position. Let’s define the styles.

```hs 
// We use StyleSheet from react-native so don't forget to import it
//import {StyleSheet} from "react-native";
const { height } = Dimensions.get("window");
const styles = StyleSheet.create({
backgroundVideo: {
height: height,
position: "absolute",
top: 0,
left: 0,
alignItems: "stretch",
bottom: 0,
right: 0
}
});
```

What did we do here?

We gave the video a `position :absolute` and we give it the window `height` of the device. We used the `Dimensions` from React Native to ensure that the video is taking up the whole hight — `top:0, left:0,bottom:0,right:0` — so that the video takes up all the space!

The entire code:

```js
import React, { Component, Fragment } from "react";
import {
  Text,
  View,
  StyleSheet,
  Dimensions,
  TouchableHighlight
} from "react-native";
import styled from "styled-components/native";
import Video from "react-native-video";
const { width, height } = Dimensions.get("window");
export default class BackgroundVideo extends Component {
  render() {
    return (
      <View>
        <Video
          source={require("./../assets/video1.mp4")}
          style={styles.backgroundVideo}
          muted={true}
          repeat={true}
          resizeMode={"cover"}
          rate={1.0}
          ignoreSilentSwitch={"obey"}
        />

        <Wrapper>
          <Logo
            source={require("./../assets/cadence-logo.png")}
            width={50}
            height={50}
            resizeMode="contain"
          />
          <Title>Join Live And on-demand classes</Title>
          <TextDescription>
            With world-class instructions right here, right now
          </TextDescription>
          <ButtonWrapper>
            <Fragment>
              <Button title="Create Account" />
              <Button transparent title="Login" />
            </Fragment>
          </ButtonWrapper>
        </Wrapper>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  backgroundVideo: {
    height: height,
    position: "absolute",
    top: 0,
    left: 0,
    alignItems: "stretch",
    bottom: 0,
    right: 0
  }
});

// styled-component

export const Wrapper = styled.View`
  justify-content: space-between;
  padding: 20px;
  align-items: center;
  flex-direction: column;
`;
export const Logo = styled.Image`
  max-width: 100px;
  width: 100px;
  height: 100px;
`;
export const TextDescription = styled.Text`
  letter-spacing: 3;
  color: #f4f4f4;
  text-align: center;
  text-transform: uppercase;
`;
export const ButtonWrapper = styled.View`
  justify-content: center;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
`;
export const Title = styled.Text`
  color: #f4f4f4;
  margin: 50% 0px 20px;
  font-size: 30;
  text-align: center;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 3;
`;
const StyledButton = styled.TouchableHighlight`
 width:250px;
 background-color:${props => (props.transparent ? "transparent" : "#f3f8ff")};
 padding:15px;
border:${props => (props.transparent ? "1px solid #f3f8ff " : 0)}
 justify-content:center;
 margin-bottom:20px;
 border-radius:24px
`;
StyledTitle = styled.Text`
  text-transform: uppercase;
  text-align: center;
  font-weight: bold;
  letter-spacing: 3;
  color: ${props => (props.transparent ? "#f3f8ff " : "#666")};
`;

export const Button = ({ onPress, color, ...props }) => {
  return (
    <StyledButton {...props}>
      <StyledTitle {...props}>{props.title}</StyledTitle>
    </StyledButton>
  );
};
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*mOSwlhVAq7PTzOuc1J-Hpg.gif)

Also, you can make this component reusable by doing the following:

```html
<View>
<Video
source={require("./../assets/video1.mp4")}
style={styles.backgroundVideo}
muted={true}
repeat={true}
resizeMode={"cover"}
rate={1.0}
ignoreSilentSwitch={"obey"}
/>
{this.props.children}
</View>
```

And you can use it with other components:

That’s pretty much it. Thank you for reading!

![Image](https://cdn-media-1.freecodecamp.org/images/1*G8eN5JqWSRzGTXxpp-CICA.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/wQZSl60DGDM?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">David Boca</a> on <a href="https://unsplash.com/search/photos/app?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### Learn more about React Native:

* [What you need to know to start building mobile apps in React Native](https://medium.freecodecamp.org/what-you-need-to-know-to-start-building-mobile-apps-in-react-native-dded951277b7)
* [Styling in React Native](https://blog.bitsrc.io/styling-in-react-native-c48caddfbe47)

#### Other posts:

* [JavaScript ES6, write Less — Do more](https://medium.freecodecamp.org/write-less-do-more-with-javascript-es6-5fd4a8e50ee2)
* [How to use routing in Vue.js to create a better user experience](https://medium.freecodecamp.org/how-to-use-routing-in-vue-js-to-create-a-better-user-experience-98d225bbcdd9)
* [Here are the most popular ways to make an HTTP request in JavaScript](https://medium.freecodecamp.org/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa)

> You can find me [on Twitter](https://twitter.com/SaidHYN) ?

#### Subscribe to my Mailing list to stay tuned for upcoming articles.

