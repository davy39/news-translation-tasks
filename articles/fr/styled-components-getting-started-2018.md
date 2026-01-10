---
title: 'styled-components : prise en main'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T16:44:00.000Z'
originalURL: https://freecodecamp.org/news/styled-components-getting-started-2018
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/ezgif.com-gif-maker.jpg
tags:
- name: getting started
  slug: getting-started
- name: styled-components
  slug: styled-components
seo_title: 'styled-components : prise en main'
seo_desc: 'By Scott Spence

  We''re going to style the basic create react app with styled-components to look
  something like this:


  But first, preamble✨: I have always struggled with styling sites, it seems to be
  an aspect of starting web development that is either...'
---

Par Scott Spence

Nous allons styliser l'application React de base avec styled-components pour qu'elle ressemble à ceci :

![Image](https://thepracticaldev.s3.amazonaws.com/i/5dwv10zpqa13wb4pr47l.gif)

Mais d'abord, préambule ✨ : J'ai toujours eu du mal à styliser des sites, cela semble être un aspect du développement web qui est soit une réflexion après coup, soit survolé. Jusqu'en décembre de l'année dernière, je n'aimais pas vraiment styliser quoi que ce soit avec CSS, c'était une corvée plutôt qu'une activité que j'appréciais.

Cela a changé lorsque j'ai commencé à utiliser styled-components, lorsque j'ai rejoint un projet de construction pour apprendre lors d'un voyage [Chingu](https://medium.com/chingu) ([`grad.then()`](https://github.com/chingu-voyage3/grad.then/) si vous êtes intéressé), nous avons décidé d'utiliser un package CSS-in-JS. [Marina](https://twitter.com/mar_biletska), qui faisait partie de mon équipe, a été une telle inspiration pour moi en observant comment les composants étaient stylisés et m'a vraiment donné la confiance nécessaire pour commencer à utiliser styled-components.

###### moi avec css avant

![Image](https://media.giphy.com/media/2rj8VysAig8QE/giphy.gif)

Je veux partager ce que j'ai appris jusqu'à présent en passant par le stylisme d'une application React de base.

Il y a quelques concepts CSS de base dans cet article dont je n'avais pas conscience avant de commencer avec styled-components et que je présume être supposés dans le stylisme des pages web.

Le stylisme de l'élément body d'un site est supposé, donc lorsque vous commencez avec une toile blanche, il y a quelques valeurs par défaut pour tous les navigateurs web modernes que vous ajoutez à votre site, comme laisser la taille de la police à 16px (ou 1rem) ou `box-sizing:` `border-box;` il existe quelques packages pour prendre soin de cela pour vous également.

### Installer styled-components

D'accord, commençons par démarrer l'application React de base que vous obtenez lorsque vous utilisez [Create React App](https://github.com/facebook/create-react-app#create-react-app-) avec [`npx`](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b). Si vous avez déjà Create React App installé globalement, vous pouvez utiliser la commande sans `npx`.

```bash
npx create-react-app style-with-styled-components
cd style-with-styled-components/
npm i styled-components

```

D'accord, maintenant nous avons l'application de base que nous pouvons styliser. Heureusement, [Dan](https://github.com/gaearon) a gentiment fourni les styles de départ pour nous, alors commençons par les utiliser avec styled-components.

La manière dont le CSS de CRA est organisé suppose que vous aurez un fichier CSS correspondant pour chaque composant, ce qui peut aider à maintenir le CSS et s'inscrit dans l'idée de React d'avoir tous vos fichiers séparés en leurs parties de composants.

Nous pouvons commencer avec le fichier `App.js` et son fichier `App.css` accompagnateur. Commençons par regarder `App.js` :

```js
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}
export default App;

```

Dans styled-components, nous créerions des composants pour chacun de ces éléments qui remplacent les `className` mentionnés précédemment. D'accord, nous pouvons commencer par migrer nos styles vers des composants, faisons d'abord un composant pour avoir une idée de la direction que nous prenons.

Tout d'abord, importons `styled` dans le module `App.js` :

```js
import styled from 'styled-components';

```

Maintenant, regardons `<div className="App">`, c'est la div de niveau supérieur pour ce composant et c'est ce que j'aime appeler le wrapper pour le composant. Alors donnons-lui un nom imaginatif AppWrapper.

En se référant au App.css, il y a `text-align: center;` qui appartient à ceci, donc :

```js
const AppWrapper = styled.div`
  text-align: center;
`;

```

Ici, nous avons défini la constante `AppWrapper` comme un `styled.div` suivi de backticks. À l'intérieur des backticks, nous pouvons écrire n'importe quel CSS régulier avec la même syntaxe CSS exacte que vous utiliseriez dans un fichier `.css` normal.

Maintenant que nous avons notre `AppWrapper`, nous pouvons remplacer la div de niveau supérieur dans le composant `App.js`.

```js
import React, { Component } from 'react';
import styled from 'styled-components';
import logo from './logo.svg';
import './App.css';
class App extends Component {
  render() {
    return (
      <AppWrapper>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </AppWrapper>
    );
  }
}
export default App;

```

### styled-components pour tout

Alors faisons cela pour les quatre classes CSS restantes, et voyons, je vais les définir sous `AppWrapper` ici :

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
  animation: ${rotate360} infinite 120s linear;
  height: 80px;
`;
const AppHeader = styled.div`
  background-color: #222;
  height: 150px;
  padding: 20px;
  color: white;
`;
const AppTitle = styled.h1`
  font-size: 1.3em;
`;
const AppIntro = styled.p`
  font-size: large;
`;

```

Tout d'abord, nous avons créé une variable pour l'animation svg React, vous devrez importer l'aide `keyframes` de styled-components comme ceci :

```js
import styled, { keyframes } from 'styled-components';

```

Cela peut maintenant être utilisé dans tout le composant `App.js` et nous pouvons ajouter un sélecteur `hover` à n'importe lequel de nos styled-components dans ce module. Ici, nous allons l'ajouter à `AppLogo` pour garder le super logo React rotatif.

```js
const AppLogo = styled.img`
  animation: ${rotate360} infinite 120s linear;
  height: 80px;
  &:hover {
    animation: ${rotate360} infinite 1.5s linear;
  }
`;

```

D'accord, notre application ne devrait pas avoir l'air différente car nous n'avons pas encore ajouté nos styled-components à la méthode `render()` de l'application, alors faisons cela maintenant.

Changeons également le texte d'introduction. Vous pouvez ajouter un wrapper pour les balises `<code>` comme ceci :

```js
const CodeWrapper = styled.code`
  font-size: 1.3rem;
`;

```

Mais si vous préférez, vous pouvez imbriquer des sélecteurs dans le composant, comme :

```js
const AppIntro = styled.p`
  color: ${props => props.theme.dark};
  font-size: large;
  code {
    font-size: 1.3rem;
  }
`;

```

Regardons maintenant la méthode `render()`...

```js
render() {
  return (
    <AppWrapper>
      <AppHeader>
        <AppLogo src={logo} alt="logo" />
        <AppTitle>Welcome to React</AppTitle>
      </AppHeader>
      <AppIntro>
        Bootstrapped with <code>create-react-app</code>.
      </AppIntro>
      <AppIntro>
        Components styled with <code>styled-components</code>{' '}
        <EmojiWrapper aria-label="nail polish"></EmojiWrapper>
      </AppIntro>
    </AppWrapper>
  )
}

```

Maintenant, toutes les classes initialement utilisées dans `App.js` ont été remplacées, donc il n'est plus nécessaire d'importer `./App.css`, supprimez cela et... toujours aucun changement ! Ce qui est une bonne chose car pour le moment nous remplaçons les fichiers `.css` par styled-components.

Cool, nous avons maintenant remplacé tout le css par styled-components, maintenant nous pouvons regarder `injectGlobal`.

Regardons à quoi devrait ressembler le fichier `App.js` avant de continuer :

```js
import React, { Component } from 'react';
import styled, { keyframes } from 'styled-components';
import logo from './logo.svg';

const AppWrapper = styled.div`
  text-align: center;
`;

const rotate360 = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

const AppLogo = styled.img`
  animation: ${rotate360} infinite 120s linear;
  height: 80px;
  &:hover {
    animation: ${rotate360} infinite 1.5s linear;
  }
`;

const AppHeader = styled.div`
  background-color: #222;
  height: 12rem;
  padding: 1rem;
  color: white;
`;

const AppTitle = styled.h1`
  font-weight: 900;
`;

const AppIntro = styled.p`
  font-size: large;
  code {
    font-size: 1.3rem;
  }
`;

const EmojiWrapper = styled.span.attrs({
  role: 'img',
})``;

class App extends Component {
  render() {
    return (
      <AppWrapper>
        <AppHeader>
          <AppLogo src={logo} alt="logo" />
          <AppTitle>Welcome to React</AppTitle>
        </AppHeader>
        <AppIntro>
          Bootstrapped with <code>create-react-app</code>.
        </AppIntro>
        <AppIntro>
          Components styled with <code>styled-components</code> <EmojiWrapper aria-label="nail polish" />
        </AppIntro>
      </AppWrapper>
    );
  }
}

export default App;

```

### Styliser le body avec injectGlobal

Pour styliser le body de notre application React, nous avons actuellement le fichier `index.css` qui est importé dans le point de montage de notre application dans le fichier `index.js`.

Pour styliser le body, nous pouvons utiliser [`injectGlobal`](https://www.styled-components.com/docs/api#injectglobal) de styled-components qui ajoute les styles directement à la feuille de style.

Pour cela, vous importez l'export nommé `injectGlobal` de styled-components et ajoutez vos styles entre les backticks.

Le `index.css` actuel ressemble à ceci :

```css
body {
  padding: 0;
  margin: 0;
  font-family: sans-serif;
}

```

Ajoutons un dossier `theme` dans le répertoire `src` et ajoutons un fichier `globalStyle.js` où nous pouvons garder tous les styles que nous voulons utiliser dans toute l'application. Garder les styles à un seul endroit simplifiera les modifications.

Dans `src/theme/globalStyle.js`, nous devrons importer l'export nommé `injectGlobal` de styled-components et ajouter les styles `index.css` dedans :

```js
import { injectGlobal } from 'styled-components';

injectGlobal`
  body {
    padding: 0;
    margin: 0;
    font-family: sans-serif;
  }
`;

```

D'accord, maintenant nous ajoutons le style du body directement à la feuille de style, donc il n'est plus nécessaire d'importer le fichier `index.css` qui est dans `index.js`, il devrait maintenant ressembler à ceci :

```js
import React from 'react' import ReactDOM from 'react-dom'

import App from './App'

import registerServiceWorker from './registerServiceWorker'

ReactDOM.render(<App />, document.getElementById('root'))

registerServiceWorker()

```

Nous devrions toujours avoir notre belle police `sans-serif`, mais ajoutons une belle police Roboto pour le body et Montserrat pour l'en-tête dans notre module `globalStyle.js`. Nous pouvons importer les polices Google avec un `@import` dans `injectGlobal` et appliquer Roboto au body :

```js
injectGlobal`
  @import url('https://fonts.googleapis.com/css?family=Montserrat|Roboto');
 
  body {
    padding: 0;
    margin: 0;
    font-family: Roboto, sans-serif;
  }
`;

```

Cool, maintenant nous pouvons ajouter notre police importée pour l'en-tête de l'application, et il y a l'option si nous voulons que tous nos `<h1>` utilisent la même police, nous pouvons ajouter cela à l'injectGlobal dans notre module `globalStyle.js`.

```js
injectGlobal`
  @import url('https://fonts.googleapis.com/css?family=Montserrat:400,900|Roboto');
  body {
    padding: 0;
    margin: 0;
    font-family: Roboto, sans-serif;
  }
  h1 {
    font-family: Montserrat;
  }
`;

```

Ensuite, nous pouvons ajuster le poids du composant `AppTitle` :

```js
const AppTitle = styled.h1`
  font-weight: 900;
`;

```

Pour ajouter les styles supplémentaires pour les polices comme Montserrat et Roboto, vous pouvez les spécifier dans l'@import url(), vous remarquerez que Montserrat a `:400,900` après lui qui spécifie les styles réguliers (400) et noirs (900), vous pouvez importer autant que vous le souhaitez depuis Google fonts (CDN), mais plus vous importez, plus cela prendra du temps à les charger. Si vous avez beaucoup de polices et de styles que vous voulez dans votre application, envisagez de les ajouter à un dossier dans le projet, comme :

```js
import Montserrat from './fonts/Montserrat-Regular.ttf';

injectGlobal`@font-face { font-family: Montserrat; src: url(${Montserrat}); }`;

```

### Thèmes

Les thèmes sont souvent utilisés pour changer l'apparence et la sensation d'une large gamme de choses à la fois. Par exemple, vous pouvez avoir un mode nuit et jour comme dans Twitter. Vous pouvez également créer vos propres thèmes dans styled-components.

![Image](https://thepracticaldev.s3.amazonaws.com/i/gwn8czgagns1n1545zgn.png)

### Utiliser le ThemeProvider de styled-components

Maintenant, disons que nous voulons avoir plusieurs composants dans notre application qui utilisent une propriété de couleur CSS `color: #6e27c5` au lieu de la coder en dur dans l'application pour chaque composant qui l'utilise, nous pouvons utiliser le `ThemeProvider` de styled-components.

Pour cela, nous devrons importer l'export nommé `ThemeProvider` de styled-components, puis définir un objet `theme` où notre couleur va résider :

```js
export const theme = {
  primary: '#6e27c5',
};

```

Ajoutons le `theme` nouvellement créé au module `globalStyle` que nous avons créé précédemment.

Pour rendre l'objet theme disponible dans tout le composant de l'application, nous allons envelopper notre composant d'application dans le `ThemeProvider` et importer notre thème génial pour l'utiliser dans le `ThemeProvider` :

```js
import React, { Component } from 'react';
import styled, { keyframes, ThemeProvider } from 'styled-components';
import logo from './logo.svg';
import { theme } from './theme/globalStyle';

// nos styled-components

class App extends Component {
  render() {
    return <ThemeProvider theme={theme}>{/* tous les enfants peuvent accéder à l'objet theme */}</ThemeProvider>;
  }
}
export default App;

```

Maintenant, les propriétés du `theme` peuvent être utilisées comme props dans nos styled-components, changeons la `background-color:` dans le composant `AppHeader`, et pendant que nous y sommes, ajoutons une propriété `dark: #222` à notre objet `theme` et utilisons-la pour la propriété `color` :

```js
const AppHeader = styled.div`
  height: 12rem;
  padding: 1rem;
  color: ${props => props.theme.dark};
  background-color: ${props => props.theme.primary};
`;

```

Maintenant, nous pouvons changer le thème de notre application globalement.

### D'accord, cool, pouvez-vous changer de thème ?

C'est ce que je pensais et il s'avère que vous pouvez, il y a une excellente [réponse sur Stack Overflow](https://stackoverflow.com/a/42899979/1138354) de [Max](https://twitter.com/mxstbr) à ce sujet.

Cela m'a fait réfléchir si vous pouvez basculer entre les thèmes plutôt que de les définir pour différentes sections comme dans la réponse SO.

J'ai commencé par définir deux thèmes (avec des noms imaginatifs) dans le module `globalStyle.js` :

```js
export const theme1 = {
  primary: '#ff0198',
  secondary: '#01c1d6',
  danger: '#eb238e',
  light: '#f4f4f4',
  dark: '#222',
};

export const theme2 = {
  primary: '#6e27c5',
  secondary: '#ffb617',
  danger: '#f16623',
  light: '#f4f4f4',
  dark: '#222',
};

```

Maintenant, nous avons besoin d'un moyen de basculer entre les deux objets `theme`, utilisons une boîte de sélection pour eux, créons un dossier de composants et ajoutons-y un composant `ThemeSelect.js`, nous pourrons nous soucier de refactoriser le composant `App.js` lorsque je ne suis pas là :

#### ThemeSelect.js

```js
import React from 'react';
import styled from 'styled-components';

const Select = styled.select`
  margin: 2rem 0.5rem;
  padding: 0rem 0.5rem;
  font-family: Roboto;
  font-size: 1rem;
  border: 1px solid ${props => props.theme.light};
  box-shadow: 0px 0px 0px 1px rgba(0, 0, 0, 0.1);
  background: ${props => props.theme.light};
  border-radius: 2px;
`;

export const SelectOpt = styled.option`
  font-family: Roboto;
  font-size: 1rem;
`;

class ThemeSelect extends React.Component {
  render() {
    return (
      <div>
        <Select onChange={e => this.props.handleThemeChange(e)}>
          <SelectOpt value="theme1">Theme 1</SelectOpt>
          <SelectOpt value="theme2">Theme 2</SelectOpt>
        </Select>
      </div>
    );
  }
}

export default ThemeSelect;

```

Vous avez probablement remarqué l'événement `onChange={e => this.props.handleThemeChange(e)`, nous allons ajouter cette méthode au composant `App.js` avec un état pour gérer le thème sélectionné.

#### App.js

```js
import React, { Component } from 'react';
import styled, { keyframes, ThemeProvider } from 'styled-components';

import logo from './logo.svg';

import { theme1, theme2 } from './theme/globalStyle';
import ThemeSelect from './components/ThemeSelect';

// nos jolis styled-components ici

class App extends Component {
  state = {
    theme: theme1,
  };
  handleThemeChange = e => {
    let theme = e.target.value;
    theme === 'theme1' ? (theme = theme1) : (theme = theme2);
    this.setState({ theme });
  };
  render() {
    return (
      <ThemeProvider theme={this.state.theme}>
        <AppWrapper>
          <AppHeader>
            <AppLogo src={logo} alt="logo" />
            <AppTitle>Welcome to React</AppTitle>
          </AppHeader>
          <AppIntro>
            Bootstrapped with <code>create-react-app</code>.
          </AppIntro>
          <AppIntro>
            Components styled with <code>styled-components</code> <EmojiWrapper aria-label="nail polish" />
          </AppIntro>
          <ThemeSelect handleThemeChange={this.handleThemeChange} />
        </AppWrapper>
      </ThemeProvider>
    );
  }
}

export default App;

```

Pour résumer ce que nous avons fait avec `App.js` ici, ajoutons un état par défaut à theme1 où les deux thèmes sont importés comme des exports nommés du module `globalStyle.js`.

Ajoutez une méthode pour gérer le changement du composant `ThemeSelect.js` `handleThemeChange`, c'est ici que nous pouvons basculer entre les deux objets `theme`.

Essayons cela, nous devrions pouvoir basculer entre les deux thèmes que nous avons définis maintenant.

### Étendre styled-components

Jusqu'à présent, notre application n'a pas beaucoup de styled-components qui sont similaires, mais que se passe-t-il si nous ajoutons des boutons...

```js
export const Button = styled.button`
  font-size: 1rem;
  border-radius: 5px;
  padding: 0.25rem 1rem;
  margin: 0 1rem;
  background: transparent;
  color: ${props => props.theme.primary};
  border: 2px solid ${props => props.theme.primary};
  ${props =>
    props.primary &&
    css`
      background: ${props => props.theme.primary};
      color: white;
    `};
`;

```

Ici, j'ai ajouté un composant `Button` au `globalStyle.js` pour que nous puissions l'utiliser dans le composant `App.js`. Pour des raisons de commodité, nous allons l'ajouter ici, vous pouvez constater que si vous avez beaucoup de composants similaires que vous réutilisez dans toute votre application, il peut être judicieux de les ajouter tous à un dossier `components`.

Nous pouvons importer le `Button` comme n'importe quel autre composant et l'utiliser dans le module, comme nous l'étendons, cela signifie que nous devons uniquement appliquer les styles spécifiques que nous voulons pour ce bouton. Mais d'abord, dans le composant `App.js`, nous pouvons spécifier un bouton normal et un bouton principal :

```html
<button>Normal Button</button> <button primary>Primary Button</button>

```

Maintenant, pour spécifier un autre bouton avec le même css que le bouton importé, nous pouvons l'étendre, comme dans cet exemple, nous allons faire en sorte que le bouton occupe 40 % de la largeur de l'écran et rendre les coins plus arrondis :

```js
const BigButt = Button.extend`
  height: 3rem;
  font-size: 2rem;
  width: 40vw;
  border-radius: 30px;
`;

```

Appliquons également le thème pour un soulignement sur `create-react-app` et `styled-components` en ajoutant un composant `Underline` styled-component :

```js
const Underline = styled.span`
  border-bottom: 4px solid ${props => props.theme.secondary};
`;

```

Maintenant, nous pouvons changer le thème et l'avoir appliqué à nos composants utilisant le thème, assez cool, non ?

J'ai mis tous les exemples que nous avons passés ici dans un exemple fonctionnel pour que vous puissiez jouer avec le thème et les styled-components, amusez-vous.

[https://codesandbox.io/s/x26q7l9vyq?from-embed](https://codesandbox.io/s/x26q7l9vyq?from-embed)

### Voulez-vous en savoir plus ?

Une excellente ressource pour commencer avec styled-components qui m'a vraiment aidé est la [playlist](https://egghead.io/playlists/styled-components-4169206d) de [Simon Vrachliotis](https://twitter.com/simonswiss) sur [egghead.io](https://egghead.io/), qui est une excellente base pour commencer avec styled-components ? la première leçon est pour les membres pro, mais le reste est actuellement disponible à regarder gratuitement.

Il y a aussi la communauté [spectrum.chat](https://spectrum.chat/?t=54887141-57a9-4386-807c-ed950c4d5132) et bien sûr [Stack Overflow](https://stackoverflow.com/questions/tagged/styled-components).

### Merci d'avoir lu

Si j'ai manqué quelque chose, ou si vous avez une meilleure façon de faire quelque chose, veuillez me le faire savoir.

Trouvez-moi sur [Twitter](https://twitter.com/spences10) ou [Ask Me Anything](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**