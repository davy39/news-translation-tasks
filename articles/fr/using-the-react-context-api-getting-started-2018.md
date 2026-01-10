---
title: Utilisation de l'API de Contexte React - Prise en main
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-08T16:54:00.000Z'
originalURL: https://freecodecamp.org/news/using-the-react-context-api-getting-started-2018
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/cover-1.png
tags:
- name: getting started
  slug: getting-started
- name: React
  slug: react
- name: React context
  slug: react-context
seo_title: Utilisation de l'API de Contexte React - Prise en main
seo_desc: 'By Scott Spence

  Let''s use the React Context API to change theme in an app!


  But first, some context! ?

  Ok terrible puns aside let''s have a look at what the React Context API is for and
  what it does. There''s a great one liner from the React docs...

  Co...'
---

Par Scott Spence

Utilisons l'API de Contexte React pour changer de thème dans une application !

![Image](https://thepracticaldev.s3.amazonaws.com/i/zmp2k4r128poj1gsws61.gif)

## Mais d'abord, un peu de **contexte** ! ?

Ok, mis à part les jeux de mots terribles, examinons à quoi sert l'API de Contexte React et ce qu'elle fait. Il y a une excellente description en une ligne dans la [documentation React](https://reactjs.org/docs/context.html)...

Le contexte fournit un moyen de transmettre des données à travers l'arborescence des composants sans avoir à passer manuellement les props à chaque niveau.

En d'autres termes, vous pouvez utiliser l'API de Contexte React pour éviter le [prop drilling](https://blog.kentcdodds.com/prop-drilling-bb62e02cb691). Si vous avez besoin de plus de détails sur le concept, veuillez consulter les liens fournis.

J'ai précédemment abordé la mise en œuvre de l'API de Contexte React dans [mon blog Gatsby](https://blog.scottspence.me), que j'ai documenté au fur et à mesure ; vous pouvez voir [comment cela s'est passé ici](https://blog.scottspence.me/react-context-api-with-gatsby).

### Expliquez-moi l'API de Contexte.

Une excellente ressource pour expliquer l'API peut être trouvée auprès de [@leighchalliday](https://twitter.com/leighchalliday) avec un [excellent cas d'utilisation](https://www.youtube.com/watch?v=yzQ_XulhQFw) sur le sujet.

## Ce que nous faisons...

Pour cet article, nous allons étendre l'exemple que nous avons créé pour [prise en main de styled-components](https://blog.scottspence.me/styled-components-getting-started), car il contient la majorité du code dont nous aurons besoin pour commencer avec l'API de Contexte React.

Nous allons étendre cet exemple pour gérer l'état du thème de l'application exemple.

Donc, en résumé :

* Échafauder une application Create React App de base
* Utiliser styled-components ? pour le style
* Ajouter des thèmes à basculer avec l'API de Contexte React
* Utiliser l'API de Contexte React !

## Ce dont nous aurons besoin...

Tout ce dont nous aurons besoin est une connexion Internet et un navigateur Web moderne ! Parce que nous allons tout faire cela en ligne dans l'excellent [CodeSandbox](https://codesandbox.io) !

Que vous ayez un compte GitHub ou non, CodeSandbox vous permettra de [commencer à coder immédiatement](https://codesandbox.io/s/new) !

### Versions :

**Ce guide est utilisé avec les versions de dépendances suivantes.**

* react : 16.4.2
* react-dom : 16.4.2
* react-scripts : 1.1.4
* styled-components : 3.4.5

---

## Commençons

Alors, passons en revue le thème de l'application React de base, cette fois, au lieu d'ajouter un état dans le composant, nous allons utiliser l'API de Contexte React pour gérer l'état pour nous. Il y aura des gens qui diront que c'est un peu excessif pour un changement de thème, mais c'est donné comme un exemple de [quand utiliser le Contexte API](https://reactjs.org/docs/context.html#when-to-use-context) dans la documentation React, donc je vous laisse juger de la validité de ce point. Pour cet exemple, j'espère qu'il vous donnera une image plus claire de la façon d'utiliser l'API de Contexte dans une application.

### Dépendances

[Ouvrez un CodeSandbox React](https://codesandbox.io/s/new) et ajoutez `styled-components` comme dépendance :

![Image](https://thepracticaldev.s3.amazonaws.com/i/d49drafvtvz3ws2br9vs.gif)

### Structure des fichiers

Un autre domaine pour le [bikeshedding](https://en.wiktionary.org/wiki/bikeshedding) est la structure des fichiers, dans ce scénario nous ajoutons des dossiers pour `components`, `contexts` et `theme`, n'hésitez pas à structurer vos fichiers comme vous le souhaitez, voici comment nous allons le faire pour cet exemple f494

Ajoutez les répertoires dans le dossier `src` afin que nous puissions ajouter quelques composants, la structure des fichiers devrait ressembler à ceci :

```bash
context-demo/
├── public/
├── src/
│  ├── components/
│  ├── contexts/
│  ├── theme/
└── package.json

```

## Échafauder une application Create React App de base

D'accord, donc ce que nous allons faire est d'ajouter un composant `App.js` dans le dossier `components`, puis l'utiliser dans le fichier `src/index.js`.

Le composant `App.js` peut être un [composant fonctionnel sans état](https://reactjs.org/docs/state-and-lifecycle.html#the-data-flows-down) pour cet exemple, car nous allons gérer l'état avec l'API de Contexte.

Ici, vous pouvez voir ma frappe approximative alors que je crée les répertoires et ajoute le composant `App.js`.

![Image](https://thepracticaldev.s3.amazonaws.com/i/oyxpggt00q754iv1azp0.gif)

Nous pouvons ensuite supprimer le fichier `style.css` et le référencer dans `src/index.js`, car nous allons styliser avec styled-components ? puis utiliser notre composant `App.js` :

![Image](https://thepracticaldev.s3.amazonaws.com/i/yyne3q36jc0zca2ld89u.gif)

D'accord, donc la raison pour laquelle j'ai abstrait le composant `App.js` du fichier `src/index.js` est afin que lorsque nous viendrons à utiliser l'API de Contexte, nous pourrons l'ajouter au niveau le plus élevé de notre application, qui est `src/index.js`.

### Et le reste ?

Donc, ce n'est pas vraiment l'application Create React App, puisque nous utilisons CodeSandbox à la place, j'ai abordé le style de base utilisé dans l'article [prise en main de styled-components](https://blog.scottspence.me/styled-components-getting-started), il est donc temps de s'y référer pour imiter les styles dont nous avons besoin.

Cela signifie que ce que nous allons faire, plutôt que d'entrer dans les détails du style de chacune des parties composantes qui constituent l'apparence de base de l'application Create React App, nous allons réutiliser des composants, donc il va y avoir un peu de copier-coller maintenant.

Le code de base de l'application Create React App a un fichier que nous abordons dans l'article [prise en main de styled-components](https://blog.scottspence.me/styled-components-getting-started), qui est le fichier `App.js`, les autres sont laissés ou supprimés, le style de base de `App.js` est :

**`App.css`**

```css
.App {
  text-align: center;
}

.App-logo {
  animation: App-logo-spin infinite 20s linear;
  height: 80px;
}

.App-header {
  background-color: #222;
  height: 150px;
  padding: 20px;
  color: white;
}

.App-title {
  font-size: 1.5em;
}

.App-intro {
  font-size: large;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

```

## Utiliser styled-components pour le style

Maintenant, nous allons recréer les styles du fichier `App.css` avec styled-components, listons-les ici et passons-les en revue :

```bash
AppWrapper
AppHeader
AppTitle
rotate360
AppLogo
# Nous ajoutons nos propres styles pour
AppIntro
Underline
StyledHyperLink
Button

```

`AppWrapper` est l'enveloppe de niveau supérieur qui, dans un composant plus grand, pourrait être utilisée pour la mise en page avec CSS Grid ou Flexbox, dans notre cas, nous allons aligner le texte au centre.

![Image](https://thepracticaldev.s3.amazonaws.com/i/uc08zkkf4ay1hq8pkt3w.gif)

Assez simple, n'est-ce pas ? Maintenant, la majorité des autres composants utiliseront le [`ThemeProvider`](https://www.styled-components.com/docs/advanced#theming) de styled-components, que nous allons transmettre notre thème depuis l'API de Contexte.

## Ajouter des thèmes à basculer avec l'API de Contexte React

D'accord, nous devons définir quelques thèmes à transmettre au `ThemeProvider`, nous allons définir plusieurs aspects de thème que nous voulons changer, ils seront :

```js
primary; // couleur
secondary; // couleur
danger; // couleur
fontHeader; // police
fontBody; // police

```

Créez un fichier pour contenir l'objet thème dans le répertoire `theme` et appelez-le `globalStyle.js` et ajoutez ce qui suit :

```js
import { injectGlobal } from 'styled-components';

export const themes = {
  theme1: {
    primary: '#ff0198',
    secondary: '#01c1d6',
    danger: '#e50000',
    fontHeader: 'Old Standard TT, sans, sans-serif',
    fontBody: 'Nunito, sans-serif',
  },

  theme2: {
    primary: '#6e27c5',
    secondary: '#ffb617',
    danger: '#ff1919',
    fontHeader: 'Enriqueta, sans-serif',
    fontBody: 'Exo 2, sans, sans-serif',
  },

  theme3: {
    primary: '#f16623',
    secondary: '#2e2e86',
    danger: '#cc0000',
    fontHeader: 'Kaushan Script, sans, sans-serif',
    fontBody: 'Headland One, sans-serif',
  },
};

injectGlobal`
  @import url('
    https://fonts.googleapis.com/css?family=
    Old+Standard+TT:400,700|
    Nunito:400,700'|
    Enriqueta:400,700|
    Exo+2:400,700|
    Kaushan+Script:400,700|
    Headland+One:400,700|
  ');

  body {
    padding: 0;
    margin: 0;
  }
`;

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/qnxbteccbaw92jbwsq9c.gif)

D'accord, donc rien de vraiment excitant ici, à part la configuration des styles pour une utilisation ultérieure.

Vous remarquerez que `injectGlobal` est utilisé ici, c'est là que nous définissons les polices pour une utilisation dans toute l'application, `injectGlobal` [devrait être utilisé une fois](https://stackoverflow.com/a/42899789/1138354) dans une application pour définir des styles globaux comme celui-ci.

En avant ! Concentrons-nous maintenant sur l'obtention des styles de base de l'application dans le composant `App.js`. Nous pouvons maintenant commencer à utiliser le `ThemeProvider` dans `App.js`. Pour ce faire, pour l'instant, afin d'obtenir un retour visuel, nous allons appliquer l'un des thèmes de l'objet `themes` dans `globalStyle.js`, afin que, lorsque nous ajoutons des composants, nous puissions voir le thème appliqué.

Nous pouvons le faire maintenant avec `AppHeader`, qui est une div stylisée :

```js
const AppHeader = styled.div`
  height: 12rem;
  padding: 1rem;
  color: ${({ theme }) => theme.dark};
  background-color: ${({ theme }) => theme.primary};
`;

```

Vous remarquerez ici que nous commençons à utiliser les props `theme` de styled-components, mais si nous collons ce code maintenant, il n'y aura aucun changement tant que le `ThemeProvider` n'aura pas reçu l'objet `theme`, donc nous allons envelopper `App.js` avec le composant `ThemeProvider` afin que tout composant encapsulé par le `ThemeProvider` puisse recevoir les props `theme`.

![Image](https://thepracticaldev.s3.amazonaws.com/i/nuyaw29uoex6qcluf8va.gif)

`AppTitle` va être un h1 donc :

```js
const AppTitle = styled.h1`
  font-family: ${({ theme }) => theme.fontHeader};
`;

```

Pour le logo React tournant, nous pouvons utiliser l'actif utilisé précédemment dans l'exemple [prise en main de styled-components](https://codesandbox.io/s/x26q7l9vyq)

Nous pouvons l'ajouter avec les imports en haut du composant `App.js` et l'ajouter dans le composant stylisé `AppLogo` en tant que balise `img` :

```js
const logo = `https://user-images.githubusercontent.com/
    234708/37256552-32635a02-2554-11e8-8fe3-8ab5bd969d8e.png`;

```

L'aide `keyframes` devra être importée avec le `ThemeProvider` pour l'animation du logo React.

```js
const rotate360 = keyframes`
  from { 
    transform: rotate(0deg); 
  }
  to { 
    transform: rotate(360deg); 
  }
`;

const AppLogo = styled.img`
  animation: ${rotate360} infinite 5s linear;
  height: 80px;
  &:hover {
    animation: ${rotate360} infinite 1s linear;
  }
`;

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/pxe3fb5zqvprvtjthq5b.gif)

### Composants partagés

Les composants partagés sont couverts dans le guide [prise en main de styled-components](https://blog.scottspence.me/styled-components-getting-started) si vous avez besoin de plus d'informations, pour cet exemple, nous allons apporter les derniers composants en tant que composants partagés pour `StyledHyperLink` et `Button` dans `src/Shared.js`, ajoutez ce qui suit :

**`src/Shared.js`**

```js
import styled, { css } from 'styled-components';

export const Button = styled.button`
  padding: 0.5rem 1rem;
  margin: 0.5rem 1rem;
  color: ${({ theme }) => theme.primary};
  font-size: 1rem;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  border: 2px solid ${props => props.border};
  background-color: Transparent;
  text-transform: uppercase;
  border-radius: 4px;
  transition: all 0.1s;
  &:hover {
    transform: translateY(1px);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.15);
  }
  ${props =>
    props.primary &&
    css`
      background: ${({ theme }) => theme.primary};
      border: 2px solid ${({ theme }) => theme.primary};
      color: white;
    `};
  ${props =>
    props.danger &&
    css`
      background: ${({ theme }) => theme.danger};
      border: 2px solid ${({ theme }) => theme.danger};
      color: white;
    `};
  &:hover {
    transform: translateY(2px);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.15);
  }
`;

export const StyledHyperLink = styled.a`
  cursor: pointer;
  &:visited,
  &:active {
    color: ${({ theme }) => theme.primary};
  }
  &:hover {
    color: ${({ theme }) => theme.secondary};
  }
  color: ${({ theme }) => theme.primary};
`;

```

Ensuite, importez les composants comme n'importe quel autre :

![Image](https://thepracticaldev.s3.amazonaws.com/i/ipi1kdmy83ieiw6sppog.gif)

Les trois derniers composants pour l'instant, `AppIntro`, `Underline` et `StyledHyperLink` :

```js
const AppIntro = styled.p`
  color: ${({ theme }) => theme.dark};
  font-size: large;
  code {
    font-size: 1.3rem;
  }
  font-family: ${({ theme }) => theme.fontBody};
`;

const Underline = styled.span`
  border-bottom: 4px solid ${({ theme }) => theme.secondary};
`;

const StyledHyperLink = SHL.extend`
  text-decoration: none;
  font-family: ${({ theme }) => theme.fontBody};
  color: ${({ theme }) => theme.fontDark};
`;

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/smm6hpg2w71sxm6nf3ln.gif)

Ajoutez-les sous le composant stylisé `AppLogo`, puis nous pouvons ajouter le reste des composants dans la fonction `return` de `App`, donc, prêt pour un autre copier-coller ? Voici :

```js
<AppIntro>
  Bootstrapped avec{' '}
  <Underline>
    <code>
      <StyledHyperLink
        href={`https://github.com/facebook/create-react-app`}
        target="_blank"
        rel="noopener"
      >
        create-react-app
      </StyledHyperLink>
    </code>
  </Underline>.
</AppIntro>
<AppIntro>
  Composants stylisés avec{' '}
  <Underline>
    <code>
      <StyledHyperLink
        href={`https://www.styled-components.com`}
        target="_blank"
        rel="noopener"
      >
        styled-components
      </StyledHyperLink>
    </code>
  </Underline>{' '}
  <span role="img" aria-label="vernis à ongles">
    ?
  </span>
</AppIntro>
<AppIntro>
  Polices choisies avec{' '}
  <Underline>
    <code>
      <StyledHyperLink
        href={`https://fontjoy.com/`}
        target="_blank"
        rel="noopener"
      >
        fontjoy.com
      </StyledHyperLink>
    </code>
  </Underline>
</AppIntro>
<Button>Bouton Normal</Button>
<Button primary>Bouton Principal</Button>
<Button danger>Bouton Danger</Button>

```

Désolé pour le mur de code ! À droite, collez cela sous la balise de fermeture `</AppHeader>` et nous devrions avoir la base de ce que nous allons thématiser !

![Image](https://thepracticaldev.s3.amazonaws.com/i/zfcnihvmyvb9my5dn11x.gif)

D'accord ? Comment cela semble-t-il ?

Maintenant, nous avons une application React de base qui utilise styled-components !

## Utiliser l'API de Contexte React

Maintenant, l'événement principal ! Ici, nous allons couvrir :

La création du contexte de thème.

L'utilisation de l'API de contexte avec un composant.

La consommation de l'API de Contexte dans plusieurs composants.

Donc, le passage d'état inutilement à travers les composants est ce que nous pouvons utiliser l'API de Contexte pour éviter. Si nous jetons un coup d'œil à l'exemple [prise en main de styled-components](https://codesandbox.io/s/x26q7l9vyq), nous pouvons voir l'état géré dans le composant `App.js` et la fonction `handleThemeChange` doit être passée au composant `ThemeSelect` de la même manière que n'importe quelles props devraient être passées. C'est un exemple simplifié, mais il est assez facile d'imaginer que si ce composant vivait dans un composant de pied de page ou un élément de menu, il y aurait plusieurs autres composants qui devraient avoir l'état passé à travers eux qui n'auraient pas réellement besoin de cet état ou de ces props. Cela a du sens ?

**exemple**

```js
<App>               {/* l'état commence ici */}
  <Header>          {/* passe par ici */}
    <Navigation>    {/* et ici */}
      <ThemeSelect> {/* à utiliser ici */}
    </Navigation>
  </Header>
  <Footer/>
</App>

```

### Ajouter le contexte du thème du site

Dans notre répertoire `src/contexts/`, nous allons créer notre `SiteThemeContext.js`, importer React et définir et exporter notre contexte :

```js
import React from 'react';

export const SiteThemeContext = React.createContext();

```

### Alors, qu'est-ce qu'un contexte ?

Un contexte est composé de deux choses, un fournisseur et un consommateur, vous avez un seul fournisseur qui se situera aussi haut que possible dans l'arborescence des composants afin que plusieurs consommateurs puissent obtenir l'état et les props du fournisseur.

Espérons que vous vous souvenez du point où nous avons abstrait le composant `function App` du fichier `src/index.js`, c'est afin que nous puissions ajouter le fournisseur de contexte au niveau le plus élevé de l'application, dans le fichier `src/index.js`. Cela signifie que tout consommateur dans l'application, peu importe à quel point il est profond dans l'arborescence des composants, peut obtenir l'état et les props de ce niveau supérieur.

Maintenant, pour créer un fournisseur, le fournisseur est un composant React régulier, donc :

```js
import React from 'react'

export const SiteThemeContext = React.createContext()

export class SiteThemeProvider extends React.Component {
  render() {
    return (
      <SiteThemeContext.Provider value={}>
        {this.props.children}
      </SiteThemeContext.Provider>
    )
  }
}

```

Ce qui est retourné par `<SiteThemeProvider>` est le `<SiteThemeContext.Provider>` et les enfants de ce composant, la seule prop que vous devez fournir au fournisseur est une prop `value`. C'est la variable à laquelle le consommateur a accès. Le consommateur étant `<SiteThemeContext.Consumer>` (plus sur cela sous peu).

Donc, ce que nous pouvons faire maintenant, c'est que ce qui est passé dans `value` soit un objet `value={{}}` afin qu'il puisse stocker plusieurs propriétés de l'état et les fonctions qui sont définies dans `SiteThemeContext`.

L'état pour le contexte doit être le `theme`, donc nous devons importer le thème depuis `src/theme/globalStyle` et l'ajouter à l'état, nous allons définir le thème par défaut (et l'état) sur `theme1` et ajouter une copie de celui-ci dans la prop `value` en le développant dans l'état `...f494`, cela devrait ressembler à ceci :

```js
import React from 'react';
import PropTypes from 'prop-types';

import { themes } from '../theme/globalStyle';

export const SiteThemeContext = React.createContext();

export class SiteThemeProvider extends React.Component {
  state = {
    theme: themes['theme1'],
  };

  render() {
    return (
      <SiteThemeContext.Provider
        value={{
          ...this.state,
        }}>
        {this.props.children}
      </SiteThemeContext.Provider>
    );
  }
}

```

D'accord, cela fait un moment que je n'ai pas ajouté de gif, il est temps d'en ajouter un autre !

![Image](https://thepracticaldev.s3.amazonaws.com/i/n2qbxs7cbf7w5opqcri2.gif)

Et apportez les `themes` et ajoutez l'état :

![Image](https://thepracticaldev.s3.amazonaws.com/i/y6n32p1gshah5ex747mu.gif)

Maintenant, nous pouvons ajouter une fonction au fournisseur pour changer l'état du thème en fonction de ce qui a été sélectionné via la valeur de l'événement `handleThemeChange` :

```js
handleThemeChange = e => {
  const key = e.target.value;
  const theme = themes[key];
  this.setState({ theme });
};

```

Cela peut ensuite être consommé par tout fournisseur qui souhaite l'utiliser, nous allons devoir l'ajouter dans la prop `value`, comme ceci :

```js
import React from 'react';
import PropTypes from 'prop-types';

import { themes } from '../theme/globalStyle';

export const SiteThemeContext = React.createContext();

export class SiteThemeProvider extends React.Component {
  state = {
    theme: themes['theme1'],
  };

  handleThemeChange = e => {
    const key = e.target.value;
    const theme = themes[key];
    this.setState({ theme });
  };

  render() {
    return (
      <SiteThemeContext.Provider
        value={{
          ...this.state,
          handleThemeChange: this.handleThemeChange,
        }}>
        {this.props.children}
      </SiteThemeContext.Provider>
    );
  }
}

```

D'accord, cela couvre le composant de contexte du thème du site, assez simple, n'est-ce pas ?

Ce que je devrais mentionner, c'est que le `e` dans la fonction `handleThemeChange` va être l'événement de la boîte de sélection du thème que nous allons créer.

Passons en revue l'ajout de la fonction et l'ajout de celle-ci à l'état :

![Image](https://thepracticaldev.s3.amazonaws.com/i/3bh3bwi4ekb24uowvm65.gif)

Et maintenant, nous pouvons ajouter le fournisseur de thème à `src/index.js` afin que tout ce qui est plus bas dans l'arborescence des dépendances puisse y accéder via un consommateur.

![Image](https://thepracticaldev.s3.amazonaws.com/i/p8nibx8ecfildi92jscm.gif)

### Ajouter la sélection de thème

Maintenant, nous voulons appeler la fonction `handleThemeChange` qui fait partie du `SiteThemeProvider` via le `SiteThemeContext` ! Je suis sûr que tout cela a parfaitement du sens en ce moment (?) alors plongeons-nous et définissons le composant que nous allons utiliser pour consommer le `SiteThemeContext.Provider` avec un composant `ThemeSelect` !

Dans le répertoire `src/components`, ajoutez un nouveau composant `ThemeSelect.js`, c'est là que nous allons consommer le contexte du thème du site avec un consommateur.

L'enfant d'un consommateur n'est pas un composant, c'est une fonction, donc ce que nous allons devoir faire, c'est avoir la sélection de thème à l'intérieur du retour de cette fonction.

Commençons par configurer les styled-components qui composeront la sélection, qui est une boîte de sélection, quelques options et une enveloppe.

D'abord, nous allons le faire sans le consommateur, puis nous l'ajouterons.

**`ThemeSelect.js`**

```js
import React from 'react';
import styled from 'styled-components';

import { themes } from '../theme/globalStyle';

const SelectWrapper = styled.div`
  margin: 0rem 0.5rem 0rem 0.25rem;
  padding: 0rem 0.5rem 0rem 0.25rem;
`;

const Select = styled.select`
  margin: 1.5rem 0.5rem;
  padding: 0.25rem 0.5rem;
  font-family: ${({ theme }) => theme.fontBody};
  border: 2px solid ${({ theme }) => theme.secondary};
  box-shadow: 0px 0px 0px 1px rgba(0, 0, 0, 0.1);
  background: ${({ theme }) => theme.foreground};
  border-radius: 4px;
`;

export const SelectOpt = styled.option`
  font-family: ${({ theme }) => theme.fontBody};
`;

const ThemeSelect = props => {
  return (
    <SelectWrapper>
      <Select>
        {Object.keys(themes).map((theme, index) => {
          return (
            <SelectOpt key={index} value={theme}>
              Thème {index + 1}
            </SelectOpt>
          );
        })}
      </Select>
    </SelectWrapper>
  );
};

export default ThemeSelect;

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/43e15llsi8uhlmi1z1ut.gif)

Ainsi, à partir de cela, nous pouvons lister les thèmes disponibles pour nous dans l'objet `themes`. Mais c'est tout, la fonction pour gérer le changement de thème vit sur le `SiteThemeProvider`.

Retour au `SiteThemeContext.Consumer`, comme je l'ai mentionné précédemment, l'enfant d'un consommateur est une fonction `() => ()`, la première section est la `value` du fournisseur (`<SiteThemeContext.Provider>`), alors jetons un coup d'œil rapide à ce que nous avons précédemment défini dans le fournisseur :

```js
value={{
  ...this.state,
  handleThemeChange: this.handleThemeChange
}}

```

Disponible depuis `SiteThemeContext.Provider`, il y a l'état et une fonction, donc n'importe lequel de ces éléments peut être extrait et passé au fournisseur, ou pour le dire autrement, le consommateur peut accéder à ces valeurs.

Ici, nous pouvons utiliser la déstructuration pour extraire la fonction `handleThemeChange` dont nous avons besoin pour changer le thème.

```js
import React from 'react'

import { SiteThemeContext } from '../contexts/SiteThemeContext'

const ThemeSelect = props => {
  return (
    <SiteThemeContext.Consumer>
      {({ handleThemeChange }) => ()}
    </SiteThemeContext.Consumer>
  )
}

export default ThemeSelect

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/1qq4hc2zqa50t0t2vi5v.gif)

Actuellement, cela ne va pas changer le thème car nous l'avons codé en dur dans le `ThemeProvider` de styled-components, ce que nous voulons faire est d'utiliser un consommateur pour le thème actuellement sélectionné dans le `SiteThemeContext`.

Avant cela, nous devrons également ajouter l'événement `onChange` que nous voulons utiliser pour passer l'événement (`e`) à la fonction `handleThemeChange` sur `SiteThemeContext`.

Ensuite, dans le composant `App`, nous pouvons importer notre `<SiteThemeContext.Consumer>` pour consommer le `theme` sur l'état `SiteThemeContext` et le passer au `ThemeProvider` de styled-components.

![Image](https://thepracticaldev.s3.amazonaws.com/i/jn5u8bzuvufpa56c9ta7.gif)

### Voulez-vous en savoir plus ?

Comme mentionné au début de cet article, une excellente ressource est [@leighchalliday](https://twitter.com/leighchalliday) et [sa chaîne YouTube](https://www.youtube.com/channel/UCWPY8W-FAZ2HdDiJp2RC_sQ) où vous pouvez trouver son [excellent cas d'utilisation](https://www.youtube.com/watch?v=yzQ_XulhQFw) pour l'API de Contexte React.

Il y a aussi la [communauté React sur Spectrum](https://spectrum.chat/react) et [styled-components sur Spectrum](https://spectrum.chat/styled-components).

Le [code exemple](https://codesandbox.io/s/5vl16n5oxp) de la visite guidée est disponible sur [CodeSandbox](https://codesandbox.io).

### Merci d'avoir lu

Si j'ai manqué quelque chose, ou s'il y a une meilleure façon de faire quelque chose, faites-le moi savoir.

Suivez-moi sur [Twitter](https://twitter.com/spences10) ou [Demandez-moi n'importe quoi](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**