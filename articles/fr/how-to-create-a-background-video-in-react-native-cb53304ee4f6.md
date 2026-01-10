---
title: Comment utiliser une vidéo comme arrière-plan dans React Native
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
seo_title: Comment utiliser une vidéo comme arrière-plan dans React Native
seo_desc: 'By Said Hayani

  In this post, we are going to create a **backgroundVideo** in React Native. If you
  have just started with React Native check out my article What you need to know to
  start building mobile apps with React Native.


  Demo: Peleton Home Scre...'
---

Par Said Hayani

Dans cet article, nous allons créer un `**backgroundVideo**` dans React Native. Si vous débutez avec React Native, consultez mon article [Ce que vous devez savoir pour commencer à créer des applications mobiles avec React Native](https://medium.freecodecamp.org/what-you-need-to-know-to-start-building-mobile-apps-in-react-native-dded951277b7).

![Image](https://cdn-media-1.freecodecamp.org/images/1*mOSwlhVAq7PTzOuc1J-Hpg.gif)
_Démo : Écran d'accueil de Peleton_

Une vidéo d'arrière-plan peut ajouter un bel effet à l'interface utilisateur d'une application. Elles peuvent également être utiles si vous souhaitez afficher, par exemple, des publicités ou envoyer un message à l'utilisateur, comme nous allons le faire ici.

Vous aurez besoin de quelques prérequis de base. Pour commencer, vous devez avoir configuré l'environnement React Native. Cela signifie que vous avez :

* [react-native-cli](https://github.com/react-native-community/react-native-cli) installé
* Le SDK Android ; si vous avez un Mac, vous n'en aurez pas besoin, juste Xcode

### Mise en route

Commençons par initialiser une nouvelle application React Native. Dans mon cas, j'utilise react-native-cli. Donc, dans votre terminal, exécutez :

```
react-native init monapp
```

Cela devrait installer toutes les dépendances et packages nécessaires pour exécuter votre application React Native.

L'étape suivante consiste à exécuter et installer l'application sur le simulateur.

Pour iOS :

```
react-native run-ios
```

Cela devrait ouvrir le simulateur iOS.

Pour Android :

```
react-native run-android
```

Vous pourriez rencontrer des problèmes avec Android. Je recommande d'utiliser [Genymotion](https://www.genymotion.com/) et l'émulateur Android ou de consulter [ce guide convivial](https://medium.com/@sunilk/react-native-development-getting-started-with-android-and-ios-ada22e3d00b1) pour configurer l'environnement.

Tout d'abord, nous allons cloner l'écran d'accueil de l'application Peleton. Nous utilisons `[**react-native-video**](https://github.com/react-native-community/react-native-video)` pour le streaming vidéo, et `[**styled-component**](https://www.styled-components.com/docs/basics#react-native)` pour le style. Vous devez donc les installer :

* Yarn :

```
yarn add react-native-video styled-components
```

* NPM

```
npm install react-native-video styled-components --save
```

Ensuite, vous devez lier react-native-video car il contient du code natif — et pour `**styled-components**`, nous n'en avons pas besoin. Exécutez simplement :

```
react-native link
```

Vous n'avez pas à vous soucier des autres choses, concentrez-vous simplement sur le composant `Video`. Tout d'abord, importez Video depuis react-native-video et commencez à l'utiliser.

```js
import Video from "react-native-video";
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

Analysons cela :

* **source** : le chemin vers la vidéo source. Vous pouvez utiliser l'URL à la place :

```
source={{uri:"https://votreVideoEnLigne.mp4"}}
```

* **style** : le style personnalisé que nous voulons donner à la vidéo, et la clé pour faire une vidéo d'arrière-plan
* resizeMode : dans notre cas, c'est `cover` ; vous pouvez essayer aussi `contain` ou `stretch`, mais cela ne nous donnera pas ce que nous voulons

Et les autres props sont optionnelles.

Passons à la partie importante : placer la vidéo en position d'arrière-plan. Définissons les styles.

```js
// Nous utilisons StyleSheet de react-native, alors n'oubliez pas de l'importer
// import { StyleSheet } from "react-native";
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

Qu'avons-nous fait ici ?

Nous avons donné à la vidéo une `position : absolute` et nous lui avons donné la `height` de la fenêtre de l'appareil. Nous avons utilisé `Dimensions` de React Native pour nous assurer que la vidéo prend toute la hauteur — `top:0, left:0, bottom:0, right:0` — afin que la vidéo occupe tout l'espace !

Le code complet :

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
          <Title>Rejoignez des cours en direct et à la demande</Title>
          <TextDescription>
            Avec des instructions de classe mondiale, ici et maintenant
          </TextDescription>
          <ButtonWrapper>
            <Fragment>
              <Button title="Créer un compte" />
              <Button transparent title="Connexion" />
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

Vous pouvez également rendre ce composant réutilisable en procédant comme suit :

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

Et vous pouvez l'utiliser avec d'autres composants :

C'est à peu près tout. Merci d'avoir lu !

![Image](https://cdn-media-1.freecodecamp.org/images/1*G8eN5JqWSRzGTXxpp-CICA.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/wQZSl60DGDM?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">David Boca</a> sur <a href="https://unsplash.com/search/photos/app?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### En savoir plus sur React Native :

* [Ce que vous devez savoir pour commencer à créer des applications mobiles dans React Native](https://medium.freecodecamp.org/what-you-need-to-know-to-start-building-mobile-apps-in-react-native-dded951277b7)
* [Styling dans React Native](https://blog.bitsrc.io/styling-in-react-native-c48caddfbe47)

#### Autres articles :

* [JavaScript ES6, écrire moins — faire plus](https://medium.freecodecamp.org/write-less-do-more-with-javascript-es6-5fd4a8e50ee2)
* [Comment utiliser le routage dans Vue.js pour créer une meilleure expérience utilisateur](https://medium.freecodecamp.org/how-to-use-routing-in-vue-js-to-create-a-better-user-experience-98d225bbcdd9)
* [Voici les moyens les plus populaires de faire une requête HTTP en JavaScript](https://medium.freecodecamp.org/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa)

> Vous pouvez me trouver [sur Twitter](https://twitter.com/SaidHYN) ?

#### Abonnez-vous à ma liste de diffusion pour rester informé des prochains articles.