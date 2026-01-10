---
title: 'Styled Components : Les Essentiels Expliqués en 3 Étapes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-12T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/styled-components-essentials-in-three-steps
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/lego-1.jpeg
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: styled-components
  slug: styled-components
seo_title: 'Styled Components : Les Essentiels Expliqués en 3 Étapes'
seo_desc: 'By Thomas Weibenfalk


  Cover Photo by Hello I’m Nik ?? on Unsplash


  I love React and Styled Components. It’s like building stuff with lego bricks into
  something bigger and whole.

  Styled Components are awesome and a perfect match for React. They really...'
---

Par Thomas Weibenfalk

> Photo de couverture par [Hello I’m Nik ??](https://unsplash.com/@helloimnik?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/search/photos/lego-part?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

J'adore React et Styled Components. C'est comme construire des choses avec des briques Lego pour en faire quelque chose de plus grand et de complet.

Les Styled Components sont géniaux et parfaits pour React. Vraiment. Et ils sont aussi faciles à comprendre... vraiment.

Dans cet article, je vais décomposer tout ce que vous devez savoir pour commencer (et aller au-delà) en trois parties. Pas profondément technique, et simplement expliqué. Si vous connaissez ces trois choses, vous en savez assez pour utiliser les Styled Components dans votre projet sans tracas.

Les trois choses sont :

1. **Comment créer et utiliser un Styled Component.**
2. **Comment modifier votre CSS conditionnellement avec des props**
3. **Comment créer un Style Global.**

Je vais les passer en revue une par une maintenant.

# 1. Comment créer et utiliser un Styled Component

Je vais plonger directement dedans. D'abord, vous devez installer Styled Components dans votre projet. Faites-le en tapant :

```js
npm i styled-components
```

Maintenant, vous êtes prêt à utiliser les Styled Components dans vos projets. Ci-dessous se trouve du code que je vais expliquer ci-dessous. Jetez-y un bon coup d'œil et continuez à lire en dessous du code.

```js
import React from "react";
import styled from "styled-components";

const StyledLogin = styled.div`
  display: flex;
  align-items: center;
  flex-flow: column;
  width: 200px;
  height: 200px;
  margin: 0 auto;
  border: 2px solid #000;
  border-radius: 20px;
  background: #eee;

  h2 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 14px;
  }

  button {
    background: green;
    color: #fff;
    padding: 10px;
    margin: 5px;
    width: 150px;
    border: none;
    border-radius: 10px;
    box-sizing: border-box;
  }
`;

const StyledInput = styled.input`
  border: 1px solid #000;
  border-radius: 10px;
  padding: 10px;
  margin: 5px;
  width: 150px;
  box-sizing: border-box;
`;

const Login = () => (
  <StyledLogin>
    <h2>Login</h2>
    <StyledInput type="text" placeholder="email" />
    <StyledInput type="password" placeholder="password" />
    <button>Login</button>
  </StyledLogin>
);

export default Login;
```

Le code ci-dessus créera un composant appelé Login qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/login_1.png)
_Formulaire de connexion du composant Login.js_

Rien de fantaisiste, rien de spécial. Juste un composant de connexion pour nous aider à mieux comprendre les Styled Components. D'accord - la première chose que vous remarquerez dans le code ci-dessus est que nous devons d'une manière ou d'une autre dire à React que nous voulons utiliser les Styled Components. Nous faisons cela en l'important comme suit :

```js
import styled from "styled-components";
```

Maintenant, nous avons importé un objet appelé `styled` que nous pouvons utiliser pour styliser nos composants. Cet objet a différentes propriétés que vous pouvez utiliser en fonction de ce que vous voulez styliser. Si c'est une div, comme dans notre exemple, vous accédez simplement à la propriété div de l'objet `styled`. Comme ceci : `styled.div`

Si vous voulez styliser un bouton, vous pouvez simplement taper `styled.button` à la place. 
Ou si c'était une balise h2, vous pouvez taper `styled.h2` ... vous avez compris !

Ces propriétés contiennent des fonctions que vous pouvez appeler avec des _littéraux de gabarit étiquetés_. Cela signifie que nous pouvons envoyer les données à ces fonctions en utilisant des backticks et ensuite mettre notre CSS entre ces backticks (````). Vous créez également une const pour contenir le Styled Component. Donc, si nous voulons créer un Styled Component pour notre composant de connexion, nous écrivons simplement le code ci-dessous :

```js
const StyledLogin = styled.div`
  display: flex;
  align-items: center;
  flex-flow: column;
  width: 200px;
  height: 200px;
  // Et plus de code CSS ci-dessous
`;
```

En bref, pour créer un style pour un élément div avec Styled Components, vous utilisez simplement cette syntaxe :

```js
const SomeName = styled.div` Le code CSS va ici ... `;
```

Ensuite, vous pouvez simplement l'utiliser comme un composant régulier :

```js
<SomeName> Votre autre code ici ... </SomeName>
```

Vous pouvez créer autant de ces Styled Components que vous le souhaitez. Dans l'exemple ci-dessus, j'ai créé deux Styled Components, l'un qui s'appelle `StyledLogin` et l'autre qui s'appelle `StyledInput`.

Une autre chose à savoir sur la création d'un Styled Component standard est la partie imbriquée. Les Styled Components ont la capacité d'imbriquer les styles comme vous pouvez le faire dans, par exemple, SASS. 

Vous pouvez voir dans le code ci-dessus que j'ai imbriqué mon style pour les éléments **h2** et **button**. C'est génial à bien des égards ! Cela rendra votre code beaucoup plus structuré et propre. Vous pouvez facilement voir quel style appartient à quel composant. Vous isolez également le style à ce composant uniquement, ce qui signifie que les autres éléments **h2** et **button** dans votre App ne seront pas affectés.

Donc, lorsque cela a du sens, utilisez l'imbrication pour styliser les éléments. Cela n'a pas toujours de sens, cependant. Vous n'avez pas besoin de créer un tout nouveau Styled Component pour chaque petit élément. C'est là que l'imbrication comme celle-ci devient pratique.

_C'est le premier_ - _il en reste deux._

# **2. Comment modifier votre CSS conditionnellement avec des props.**

Les composants stylisés peuvent recevoir des props. Tout comme un composant régulier. En passant des props à votre Styled Component, vous pouvez faire du style CSS conditionnel. Smooooooth ... 👨‍💻

Supposons que nous voulons changer la couleur du champ de saisie du mot de passe en fonction de si l'utilisateur a tapé le mauvais mot de passe ou non.

D'accord, je réalise que c'est une solution vraiment simplifiée et qu'il y aurait beaucoup plus qu'une simple prop impliquée dans des choses comme celle-ci. Mais pour le bien de cet article de tutoriel, disons que nous le faisons comme ceci.

Si nous avons une prop qui s'appelle `correct` définie sur false, nous faisons notre zone de texte rouge à la place. Jetons un coup d'œil au code ci-dessous. J'ai intentionnellement laissé de côté le code de style pour tout le composant Login pour économiser de l'espace. Donc, faisons semblant que cela est là et est le même que ci-dessus.

```js
const StyledInput = styled.input`
  border: 1px solid #000;
  border-radius: 10px;
  padding: 10px;
  margin: 5px;
  width: 150px;
  box-sizing: border-box;
  background: ${prop => prop.correct ? 'white' : 'red'};
`;

const Login = () => (
  <StyledLogin>
    <h2>Login</h2>
    <StyledInput correct={true} type="text" placeholder="email" />
    <StyledInput correct={false} type="password" placeholder="password" />
    <button>Login</button>
  </StyledLogin>
);
```

Cela nous donnera ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/login_2.png)

Tout d'abord, regardez le composant `Login`. Et les composants `StyledInput`. J'ai créé une prop qui s'appelle `correct` et je passe `true` et `false` aux deux différents composants. Celui qui reçoit la valeur _true_ sera affiché en blanc. 
Pour accéder à cette valeur de prop dans votre CSS de Styled Component, vous pouvez utiliser le code ci-dessous :

```js
background: ${prop => prop.correct ? 'white' : 'red'};
```

Vous créez simplement un opérateur ternaire à l'intérieur d'une fonction fléchée entourée de `${}` en disant à ce Styled Component de sélectionner la couleur blanche si `prop.correct` est `false`. Et utiliser la couleur rouge si `prop.correct` est `true`. Simple comme ça !

Vous pouvez faire cela avec n'importe quelle propriété CSS que vous voulez ! ✍️ Et c'est ainsi que vous faites du CSS conditionnel avec des props dans les Styled Components.

_Deux faits_ - _il en reste un._

# **3. Comment créer un Style Global.**

La dernière chose essentielle que vous devez savoir pour utiliser les Styled Components est comment créer un style global.

Le style global est réalisé en utilisant une fonction spéciale à cet effet de la bibliothèque Styled Components. Elle s'appelle `createGlobalStyle` et vous l'importez comme ceci :

```js
import { createGlobalStyle } from 'styled-components';
```

Ensuite, vous pouvez créer un composant Styled Global comme ceci :

```js
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    background: #000;
    color: #fff;
  }
`;

const App = () => {
  <>
    <GlobalStyle />
    <Login />
  </>
}
```

Vous placez simplement le composant de style global au niveau supérieur de votre application. Ensuite, il utilisera le style dans toute votre App. Dans ce cas, je suppose que le composant de niveau supérieur s'appelle `App`. Vous pouvez également utiliser des props et faire du CSS conditionnel dans les composants Styled globaux. Tout comme les Styled Components réguliers.

# Conclusion

C'est tout ! Il y a plus à savoir sur les Styled Components que cela, mais je pense que ce sont vraiment les essentiels que vous devez connaître pour utiliser les Styled Components. 

Si vous êtes intéressé à en apprendre plus, je vous recommande fortement d'aller sur le site [https://www.styled-components.com/docs/](https://www.styled-components.com/docs/) et de lire la documentation.

De plus, merci d'avoir lu cet article. Je suis un développeur de Suède qui aime enseigner et coder. Je crée également des cours sur React et Gatsby en ligne. Vous pouvez me trouver sur Udemy. Il suffit de chercher Thomas Weibenfalk ou de me contacter sur Twitter **@weibenfalk**

J'ai aussi une chaîne YouTube où j'enseigne des choses gratuites, vérifiez-la [**ici**](https://www.youtube.com/channel/UCnnnWy4UTYN258FfVGeXBbg).