---
title: Comment utiliser Redux dans ReactJS avec des exemples concrets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-10T22:59:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-redux-in-reactjs-with-real-life-examples-687ab4441b85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hOT8TIpiXVDCK02sQkvhDQ.jpeg
tags:
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Redux dans ReactJS avec des exemples concrets
seo_desc: 'By Nazare Emanuel Ioan

  Since I started to work with ReactJS, at Creative-Tim, I’ve only used it to create
  simple react apps, or templates if you will. I have used ReactJS only with create-react-app
  and have never tried to integrate it with something ...'
---

Par Nazare Emanuel Ioan

Depuis que j'ai commencé à travailler avec [ReactJS](https://reactjs.org/), chez [Creative-Tim](https://www.creative-tim.com/), je ne l'ai utilisé que pour créer des [applications react simples](https://www.creative-tim.com/bootstrap-themes/react-themes), ou des [modèles](https://www.creative-tim.com/bootstrap-themes/react-themes) si vous préférez. J'ai utilisé ReactJS uniquement avec [create-react-app](https://github.com/facebook/create-react-app) et je n'ai jamais essayé de l'intégrer avec autre chose.

Beaucoup de nos utilisateurs m'ont demandé, à moi ou à mon équipe, si les modèles que j'ai créés avaient [Redux](https://redux.js.org/) intégré. Ou s'ils étaient créés de manière à pouvoir être utilisés avec Redux. Et ma réponse était toujours quelque chose comme : « Je n'ai pas encore travaillé avec Redux et je ne sais pas quelle réponse vous donner ».

Me voilà donc maintenant, en train d'écrire un article sur Redux et sur la manière de l'utiliser dans React. Plus tard dans cet article, je vais ajouter Redux à l'un des projets sur lesquels j'ai travaillé au cours de l'année et demie écoulée.

Bon à savoir avant de nous lancer et de nous battre avec ces deux bibliothèques :

* Je vais utiliser [create-react-app@2.1.](https://github.com/facebook/create-react-app)1 (installé globalement)
* J'utilise [npm@6.4.1](https://www.npmjs.com/package/npm)
* Ma version de [Node.js](https://nodejs.org/en/) au moment de la rédaction de cet article était 10.13.0 (LTS)
* Si vous souhaitez utiliser [Webpack](https://webpack.js.org/) à la place, vous pouvez lire mon [article sur Webpack](https://medium.freecodecamp.org/how-to-use-reactjs-with-webpack-4-babel-7-and-material-design-ff754586f618), et combiner ce que je vous montre là-bas avec ce que je vais vous montrer ici.

### Création d'un nouveau projet basé sur ReactJS et ajout de Redux

Commençons par créer une nouvelle application react, accédons-y et démarrons-la.

```bash
create-react-app react-redux-tutorial
cd react-redux-tutorial
npm start
```

![Image](https://cdn-media-1.freecodecamp.org/images/nDaQRa3VplnG8gqJg08kGNkwpeSvlad2s30B)
_sortie par défaut de **create-react-app** de **npm start**_

Comme nous pouvons le voir, create-react-app nous donne un modèle très basique avec un paragraphe, un lien vers le site web de React et l'icône officielle de ReactJS en rotation.

Je ne vous ai pas encore dit ce que nous allons utiliser Redux pour faire, ou ce que nous faisons ici. Et c'est parce que j'avais besoin de l'image gif ci-dessus.

Pour rendre cet article de tutoriel léger et facile à comprendre, nous ne allons pas construire quelque chose de très complexe. Nous allons utiliser Redux pour faire en sorte que l'image React ci-dessus s'arrête ou commence à tourner.

Cela étant dit, ajoutons les packages **Redux** suivants :

```bash
npm install --save redux react-redux
```

[redux v4.0.1](https://redux.js.org/)

* Ce que Redux fait, de manière très générale, c'est qu'il crée un état global pour toute l'application, accessible par n'importe quel composant
* C'est une bibliothèque de gestion d'état
* Vous n'avez qu'un seul état pour toute votre application, et non des états pour chacun de vos composants

[react-redux v5.1.1](https://www.npmjs.com/package/react-redux)

* Cela est utilisé pour que nous puissions accéder aux données de Redux et les modifier en envoyant des actions à Redux — en fait, pas à Redux, mais nous y viendrons
* La documentation officielle indique : _Il permet à vos composants React de lire les données d'un magasin Redux et de dispatcher des actions au magasin pour mettre à jour les données_

**NOTE** : _Si vous avez des problèmes avec la commande ci-dessus, essayez d'installer les packages séparément_

Lorsque vous travaillez avec Redux, vous aurez besoin de trois choses principales :

* [actions](https://redux.js.org/basics/actions) : ce sont des objets qui doivent avoir deux propriétés, une décrivant le **type** d'action, et une décrivant ce qui doit être changé dans l'état de l'application.
* [reducers](https://redux.js.org/basics/reducers) : ce sont des fonctions qui implémentent le comportement des actions. Elles changent l'état de l'application, en fonction de la description de l'action et de la description du changement d'état.
* [store](https://redux.js.org/basics/store) : il rassemble les actions et les reducers, maintenant et changeant l'état pour toute l'application — il n'y a qu'un seul store.

Comme je l'ai dit ci-dessus, nous allons arrêter et démarrer la rotation du logo React. Cela signifie que nous allons avoir besoin de deux actions comme suit :

1 — Commandes Linux / Mac

```bash
mkdir src/actions
touch src/actions/startAction.js
touch src/actions/stopAction.js
```

2 — Commandes Windows

```bash
mkdir src\actions
echo "" > src\actions\startAction.js
echo "" > src\actions\stopAction.js
```

Modifions maintenant le fichier **src/actions/startAction.js** comme suit :

```js
export const startAction = {
  type: "rotate",
  payload: true
};
```

Nous allons donc dire à notre reducer que le type de l'action concerne la _rotation_ (**rotate**) du logo React. Et l'état de la rotation du logo React doit être changé en **true** — nous voulons que le logo commence à tourner.

Modifions maintenant le fichier **src/actions/stopAction.js** comme suit :

```js
export const stopAction = {
  type: "rotate",
  payload: false
};
```

Nous allons donc dire à notre reducer que le type de l'action concerne la _rotation_ (**rotate**) du logo React. Et l'état de la rotation du logo React doit être changé en **false** — nous voulons que le logo arrête de tourner.

Créons également le reducer pour notre application :

1 — Commandes Linux / Mac

```bash
mkdir src/reducers
touch src/reducers/rotateReducer.js
```

2 — Commandes Windows

```bash
mkdir src\reducers
echo "" > src\reducers\rotateReducer.js
```

Et, ajoutons le code suivant à l'intérieur :

```js
export default (state, action) => {
  switch (action.type) {
    case "rotate":
      return {
        rotating: action.payload
      };
    default:
      return state;
  }
};
```

Le reducer recevra donc nos deux actions, toutes deux de type **rotate**, et elles changeront toutes deux le même état dans l'application — qui est _state.rotating_. En fonction du payload de ces actions, _state.rotating_ changera en **true** ou **false**.

J'ai ajouté un cas **default**, qui maintiendra l'état inchangé si le type d'action n'est pas **rotate**. La valeur par défaut est là au cas où nous créons une action et que nous oublions d'ajouter un cas pour cette action. De cette manière, nous ne supprimons pas tout l'état de l'application — nous ne faisons simplement rien, et gardons ce que nous avions.

La dernière chose que nous devons faire est de créer notre store pour toute l'application. Puisqu'il n'y a qu'un seul store / un seul état pour toute l'application, nous n'allons pas créer un nouveau dossier pour le store. Si vous le souhaitez, vous pouvez créer un nouveau dossier pour le store et l'ajouter là, mais ce n'est pas comme pour les actions, par exemple, où vous pouvez avoir plusieurs actions et il est préférable de les garder à l'intérieur d'un dossier.

Cela étant dit, nous allons exécuter cette commande :

1 — Commande Linux / Mac

```bash
touch src/store.js
```

2 — Commande Windows

```bash
echo "" > src\store.js
```

Et aussi ajouter le code suivant à l'intérieur :

```js
import { createStore } from "redux";
import rotateReducer from "reducers/rotateReducer";

function configureStore(state = { rotating: true }) {
  return createStore(rotateReducer,state);
}

export default configureStore;
```

Nous créons donc une fonction nommée **configureStore** dans laquelle nous envoyons un état par défaut, et nous créons notre store en utilisant le reducer créé et l'état par défaut.

Je ne suis pas sûr que vous ayez vu mes imports, ils utilisent des chemins absolus, donc vous pourriez avoir des erreurs à cause de cela. La solution pour cela est l'une des deux :

Soit

1 — Ajoutez un fichier .env dans votre application comme ceci :

```bash
echo "NODE_PATH=./src" > .env
```

Ou

2 — Installez cross-env globalement et changez le script de démarrage dans le fichier package.json comme ceci :

```bash
npm install -g cross-env
```

Et à l'intérieur de package.json

```json
"start": "NODE_PATH=./src react-scripts start",
```

Maintenant que nous avons configuré notre store, nos actions et notre reducer, nous devons ajouter une nouvelle classe dans le fichier **src/App.css**. Cette classe mettra en pause l'animation de rotation du logo.

Nous allons donc écrire ce qui suit dans **src/App.css** :

```css
.App-logo-paused {
  animation-play-state: paused;
}
```

Votre fichier **App.css** devrait donc ressembler à ceci :

```css
.App {
  text-align: center;
}

.App-logo {
  animation: App-logo-spin infinite 20s linear;
  height: 40vmin;
}

/* nouvelle classe ici */
.App-logo-paused {
  animation-play-state: paused;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
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

Maintenant, nous devons uniquement modifier notre fichier **src/App.js** afin qu'il écoute l'état de notre store. Et lorsqu'on clique sur le logo, il appelle l'une des actions de démarrage ou d'arrêt.

Tout d'abord, nous devons connecter notre composant à notre store redux, donc nous importons **connect** depuis **react-redux**.

```js
import { connect } from "react-redux";
```

Après cela, nous allons exporter notre composant App via la méthode connect comme ceci :

```js
export default connect()(App);
```

Pour changer l'état du store redux, nous aurons besoin des actions que nous avons faites précédemment, donc importons-les également :

```js
import { startAction } from "actions/startAction";
import { stopAction } from "actions/stopAction";
```

Maintenant, nous devons récupérer l'état de notre store et dire que nous voulons que les actions de démarrage et d'arrêt soient utilisées pour changer l'état.

Cela sera fait en utilisant la fonction connect, qui accepte deux paramètres :

* **mapStateToProps** : cela est utilisé pour récupérer l'état du store
* **mapDispatchToProps** : cela est utilisé pour récupérer les actions et les dispatcher au store

Vous pouvez en lire plus ici : [arguments de la fonction connect de react-redux](https://github.com/reduxjs/react-redux/blob/master/docs/api.md#arguments).

Écrivons donc à l'intérieur de notre App.js (à la fin du fichier si vous le souhaitez) :

```js
const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  startAction: () => dispatch(startAction),
  stopAction: () => dispatch(stopAction)
});
```

Après cela, ajoutons-les à l'intérieur de notre fonction connect comme ceci :

```js
export default connect(mapStateToProps, mapDispatchToProps)(App);
```

Et maintenant, à l'intérieur de notre composant App, nous pouvons accéder à l'état du store, à startAction et stopAction via les props.

Changeons la balise **img** en :

```jsx
<img 
  src={logo} 
  className={
    "App-logo" + 
    (this.props.rotating ? "":" App-logo-paused")
  } 
  alt="logo" 
  onClick={
    this.props.rotating ? 
      this.props.stopAction : this.props.startAction
  }
/>
```

Donc, ce que nous disons ici, c'est que si l'état du store de rotation (**this.props.rotating**) est vrai, alors nous voulons que seul le **className** _App-logo_ soit défini pour notre **img**. Si c'est faux, alors nous voulons également que la classe _App-logo-paused_ soit définie dans le **className**. De cette manière, nous mettons en pause l'animation.

De plus, si **this.props.rotating** est **true**, alors nous voulons envoyer à notre store pour la fonction **onClick** et le changer en **false**, et vice-versa.

Nous avons presque terminé, mais nous avons oublié quelque chose.

Nous n'avons pas encore dit à notre application react que nous avons un état global, ou si vous préférez, que nous utilisons la gestion d'état redux.

Pour cela, nous allons dans **src/index.js**, nous importons un **Provider** depuis **react-redux**, et le store nouvellement créé comme ceci :

```js
import { Provider } from "react-redux";

import configureStore from "store";
```

* [Provider](https://react-redux.js.org/docs/api/provider) : rend le Redux store disponible pour tous les composants imbriqués qui ont été enveloppés dans la fonction connect

Après cela, au lieu de rendre notre composant App directement, nous le rendons via notre Provider en utilisant le store que nous avons créé comme ceci :

```js
ReactDOM.render(
  <Provider store={configureStore()}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

Ici, nous aurions pu utiliser la fonction **configureStore** avec un autre état, par exemple **_configureStore({ rotating: false })_**.

Donc, votre **index.js** devrait ressembler à ceci :

```js
import React from 'react';
import ReactDOM from 'react-dom';
// nouvelles importations commencent
import { Provider } from "react-redux";

import configureStore from "store";
// nouvelles importations se terminent

import './index.css';

import App from './App';
import * as serviceWorker from './serviceWorker';

// rendu modifié
ReactDOM.render(
  <Provider store={configureStore()}>
    <App />
  </Provider>,
  document.getElementById('root')
);
// rendu modifié

serviceWorker.unregister();
```

Allons-y et voyons si notre application redux fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/cOdx8xHzZjMmqEYSTgVkkPSXkG925Hwewoxj)
_**react** et **redux** en action_

### Utilisation des créateurs d'actions

Optionnellement, au lieu des **actions**, nous pouvons utiliser des [créateurs d'actions](https://redux.js.org/basics/actions#action-creators), qui sont des fonctions qui créent des actions.

De cette manière, nous pouvons combiner nos deux actions en une seule fonction et réduire un peu notre code.

Créons donc un nouveau fichier :

1 — Commande Linux / Mac

```bash
touch src/actions/rotateAction.js
```

2 — Commande Windows

```bash
echo "" > src\actions\rotateAction.js
```

Et ajoutons ce code :

```jsx
const rotateAction = (payload) => {
  return {
    type: "rotate",
    payload
  }
}
export default rotateAction;
```

Nous allons envoyer une action de type rotate, avec un payload que nous allons obtenir dans le composant App.

À l'intérieur du composant src/App.js, nous devons importer notre nouveau créateur d'action :

```js
import rotateAction from "actions/rotateAction";
```

Ajoutons la nouvelle fonction à mapDispatchToProps comme ceci :

rotateAction : recevra un (payload) et dispatchera rotateAction avec le payload

Changeons la fonction **onClick** en :

```js
onClick={() => this.props.rotateAction(!this.props.rotating)}
```

Et enfin, ajoutons notre nouveau créateur d'action à **mapDispatchToProps** comme ceci :

```js
rotateAction: (payload) => dispatch(rotateAction(payload))
```

Nous pouvons également supprimer les anciennes importations des anciennes actions, et les supprimer de **mapDispatchToProps** également.

Voici à quoi devrait ressembler votre nouveau src/App.js :

```jsx
import React, { Component } from 'react';
// nouvelles lignes à partir d'ici
import { connect } from "react-redux";
import rotateAction from "actions/rotateAction";

//// nouvelles lignes jusqu'ici

import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    console.log(this.props);
    return (
      <div className="App">
        <header className="App-header">
          <img
            src={logo}
            className={
              "App-logo" +
              (this.props.rotating ? "":" App-logo-paused")
            }
            alt="logo"
            onClick={
              () => this.props.rotateAction(!this.props.rotating)
            }
          />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  ...state
});
const mapDispatchToProps = dispatch => ({
  rotateAction: (payload) => dispatch(rotateAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(App);
```

### Un exemple concret avec [Paper Dashboard React](https://www.creative-tim.com/product/paper-dashboard-react)

![Image](https://cdn-media-1.freecodecamp.org/images/356UctzmEu8euFGJLpMVitFUDLy3LduQQTl4)
_**Paper Dashboard React** — Gif du produit_

Comme vous pouvez le voir dans l'image gif ci-dessus, j'utilise le menu de droite pour changer les couleurs du menu de gauche. Cela est réalisé en utilisant les états des composants, et en passant cet état d'un composant parent aux deux menus et certaines fonctions pour changer cet état.

![Image](https://cdn-media-1.freecodecamp.org/images/V3KhG508UOWnU1CA2FFtKEACx7vU3BRyDfyQ)
_petit diagramme sur le fonctionnement de l'application à l'heure actuelle_

J'ai pensé que ce serait un bon exemple, de prendre ce produit et de remplacer les états des composants par Redux.

Vous pouvez l'obtenir de ces 3 manières :

1. Télécharger depuis [creative-tim.com](https://www.creative-tim.com/product/paper-dashboard-react)
2. Télécharger depuis [Github](https://github.com/creativetimofficial/paper-dashboard-react)
3. Cloner depuis Github :

```bash
git clone https://github.com/creativetimofficial/paper-dashboard-react.git
```

Maintenant que nous avons ce produit, accédons-y et installons à nouveau redux et react-redux :

```bash
npm install --save redux react-redux
```

Après cela, nous devons créer les actions. Puisque dans le menu de droite nous avons 2 couleurs qui définissent l'arrière-plan du menu de gauche, et 5 couleurs qui changent la couleur des liens, nous avons besoin de 7 actions, ou 2 créateurs d'actions — et nous allons avec cette deuxième option puisque c'est un peu moins de code à écrire :

1 — Commandes Linux / Mac

```bash
mkdir src/actions
touch src/actions/setBgAction.js
touch src/actions/setColorAction.js
```

2 — Commandes Windows

```bash
mkdir src\actions
echo "" > src\actions\setBgAction.js
echo "" > src\actions\setColorAction.js
```

Après cela, créons le code des actions comme suit :

— **src/actions/setBgAction.js**

```js
const setBgAction = (payload) => {
  return {
    type: "bgChange",
    payload
  }
}
export default setBgAction;
```

— **src/actions/setColorAction.js**

```js
const setColorAction = (payload) => {
  return {
    type: "colorChange",
    payload
  }
}
export default setColorAction;
```

Maintenant, comme dans la première partie, nous avons besoin du reducer :

1 — Commandes Linux / Mac

```bash
mkdir src/reducers
touch src/reducers/rootReducer.js
```

2 — Commandes Windows

```bash
mkdir src\reducers
echo "" > src\reducers\rootReducer.js
```

Et le code pour le reducer :

```js
export default (state, action) => {
  switch (action.type) {
    case "bgChange":
      return {
        ...state,
        bgColor: action.payload
      };
    case "colorChange":
      return {
        ...state,
        activeColor: action.payload
      };
    default:
      return state;
  }
};
```

Comme vous pouvez le voir ici, contrairement à notre premier exemple, nous voulons conserver notre ancien état et mettre à jour son contenu.

Nous avons également besoin du store :

1 — Commande Linux / Mac

```bash
touch src/store.js
```

2 — Commande Windows

```bash
echo "" > src\store.js
```

Le code pour celui-ci :

```js
import { createStore } from "redux";
import rootReducer from "reducers/rootReducer";

function configureStore(state = { bgColor: "black", activeColor: "info" }) {
  return createStore(rootReducer,state);
}
export default configureStore;
```

À l'intérieur de src/index.js, nous avons besoin de :

```js
// nouvelles importations commencent
import { Provider } from "react-redux";

import configureStore from "store";
// nouvelles importations se terminent
```

Et aussi, changeons la fonction **render** :

```js
ReactDOM.render(
  <Provider store={configureStore()}>
    <Router history={hist}>
      <Switch>
        {indexRoutes.map((prop, key) => {
          return <Route path={prop.path} key={key} component={prop.component} />;
        })}
      </Switch>
    </Router>
  </Provider>,
  document.getElementById("root")
);
```

Donc, le fichier **index.js** devrait ressembler à ceci :

```js
import React from "react";
import ReactDOM from "react-dom";
import { createBrowserHistory } from "history";
import { Router, Route, Switch } from "react-router-dom";
// nouvelles importations commencent
import { Provider } from "react-redux";

import configureStore from "store";
// nouvelles importations se terminent

import "bootstrap/dist/css/bootstrap.css";
import "assets/scss/paper-dashboard.scss";
import "assets/demo/demo.css";

import indexRoutes from "routes/index.jsx";

const hist = createBrowserHistory();

ReactDOM.render(
  <Provider store={configureStore()}>
    <Router history={hist}>
      <Switch>
        {indexRoutes.map((prop, key) => {
          return <Route path={prop.path} key={key} component={prop.component} />;
        })}
      </Switch>
    </Router>
  </Provider>,
  document.getElementById("root")
);
```

Maintenant, nous devons apporter quelques modifications à l'intérieur de **src/layouts/Dashboard/Dashboard.jsx**. Nous devons supprimer l'état et les fonctions qui changent l'état. Alors, allez-y et **supprimez ces morceaux de code** :

Le constructeur (entre les lignes 16 et 22) :

```jsx
constructor(props){
  super(props);
  this.state = {
    backgroundColor: "black",
    activeColor: "info",
  }
}
```

Les fonctions d'état (entre les lignes 41 et 46) :

```jsx
handleActiveClick = (color) => {
    this.setState({ activeColor: color });
  }
handleBgClick = (color) => {
  this.setState({ backgroundColor: color });
}
```

Les props **bgColor** et **activeColor** de la sidebar (lignes 53 et 54) :

```jsx
bgColor={this.state.backgroundColor}
activeColor={this.state.activeColor}
```

Toutes les props de FixedPlugin (entre les lignes 59-62) :

```jsx
bgColor={this.state.backgroundColor}
activeColor={this.state.activeColor}
handleActiveClick={this.handleActiveClick}
handleBgClick={this.handleBgClick}
```

Donc, nous restons avec ce code à l'intérieur du composant de mise en page Dashboard :

```jsx
import React from "react";
// plugin javascript utilisé pour créer des barres de défilement sur windows
import PerfectScrollbar from "perfect-scrollbar";
import { Route, Switch, Redirect } from "react-router-dom";

import Header from "components/Header/Header.jsx";
import Footer from "components/Footer/Footer.jsx";
import Sidebar from "components/Sidebar/Sidebar.jsx";
import FixedPlugin from "components/FixedPlugin/FixedPlugin.jsx";

import dashboardRoutes from "routes/dashboard.jsx";

var ps;

class Dashboard extends React.Component {
  componentDidMount() {
    if (navigator.platform.indexOf("Win") > -1) {
      ps = new PerfectScrollbar(this.refs.mainPanel);
      document.body.classList.toggle("perfect-scrollbar-on");
    }
  }
  componentWillUnmount() {
    if (navigator.platform.indexOf("Win") > -1) {
      ps.destroy();
      document.body.classList.toggle("perfect-scrollbar-on");
    }
  }
  componentDidUpdate(e) {
    if (e.history.action === "PUSH") {
      this.refs.mainPanel.scrollTop = 0;
      document.scrollingElement.scrollTop = 0;
    }
  }
  render() {
    return (
      <div className="wrapper">
        <Sidebar
          {...this.props}
          routes={dashboardRoutes}
        />
        <div className="main-panel" ref="mainPanel">
          <Header {...this.props} />
          <Switch>
            {dashboardRoutes.map((prop, key) => {
              if (prop.pro) {
                return null;
              }
              if (prop.redirect) {
                return <Redirect from={prop.path} to={prop.pathTo} key={key} />;
              }
              return (
                <Route path={prop.path} component={prop.component} key={key} />
              );
            })}
          </Switch>
          <Footer fluid />
        </div>
        <FixedPlugin />
      </div>
    );
  }
}

export default Dashboard;
```

Nous devons connecter les composants **Sidebar** et **FixedPlugin** au store.

Pour **src/components/Sidebar/Sidebar.jsx** :

```jsx
import { connect } from "react-redux";
```

Et changez l'export en :

```jsx
const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(Sidebar);
```

Pour **src/components/FixedPlugin/FixedPlugin.jsx** :

```jsx
import { connect } from "react-redux";
import setBgAction from "actions/setBgAction";
import setColorAction from "actions/setColorAction";
```

Et l'export devrait maintenant être :

```jsx
const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  setBgAction: (payload) => dispatch(setBgAction(payload)),
  setColorAction: (payload) => dispatch(setColorAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(FixedPlugin);
```

Nous allons avoir ces prochains changements :

* partout où vous trouvez le mot **handleBgClick**, vous devrez le changer en **setBgAction**
* partout où vous trouvez le mot **handleActiveClick**, vous devrez le changer en **setColorAction**

Donc, le composant FixedPlugin devrait maintenant ressembler à ceci :

```jsx
import React, { Component } from "react";

import { connect } from "react-redux";
import setBgAction from "actions/setBgAction";
import setColorAction from "actions/setColorAction";

import Button from "components/CustomButton/CustomButton.jsx";

class FixedPlugin extends Component {
  constructor(props) {
    super(props);
    this.state = {
      classes: "dropdown show"
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    if (this.state.classes === "dropdown") {
      this.setState({ classes: "dropdown show" });
    } else {
      this.setState({ classes: "dropdown" });
    }
  }
  render() {
    return (
      <div className="fixed-plugin">
        <div className={this.state.classes}>
          <div onClick={this.handleClick}>
            <i className="fa fa-cog fa-2x" />
          </div>
          <ul className="dropdown-menu show">
            <li className="header-title">SIDEBAR BACKGROUND</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.bgColor === "black"
                      ? "badge filter badge-dark active"
                      : "badge filter badge-dark"
                  }
                  data-color="black"
                  onClick={() => {
                    this.props.setBgAction("black");
                  }}
                />
                <span
                  className={
                    this.props.bgColor === "white"
                      ? "badge filter badge-light active"
                      : "badge filter badge-light"
                  }
                  data-color="white"
                  onClick={() => {
                    this.props.setBgAction("white");
                  }}
                />
              </div>
            </li>
            <li className="header-title">SIDEBAR ACTIVE COLOR</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.activeColor === "primary"
                      ? "badge filter badge-primary active"
                      : "badge filter badge-primary"
                  }
                  data-color="primary"
                  onClick={() => {
                    this.props.setColorAction("primary");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "info"
                      ? "badge filter badge-info active"
                      : "badge filter badge-info"
                  }
                  data-color="info"
                  onClick={() => {
                    this.props.setColorAction("info");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "success"
                      ? "badge filter badge-success active"
                      : "badge filter badge-success"
                  }
                  data-color="success"
                  onClick={() => {
                    this.props.setColorAction("success");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "warning"
                      ? "badge filter badge-warning active"
                      : "badge filter badge-warning"
                  }
                  data-color="warning"
                  onClick={() => {
                    this.props.setColorAction("warning");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "danger"
                      ? "badge filter badge-danger active"
                      : "badge filter badge-danger"
                  }
                  data-color="danger"
                  onClick={() => {
                    this.props.setColorAction("danger");
                  }}
                />
              </div>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react"
                color="primary"
                block
                round
              >
                Download now
              </Button>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react/#/documentation/tutorial"
                color="default"
                block
                round
                outline
              >
                <i className="nc-icon nc-paper"></i> Documentation
              </Button>
            </li>
            <li className="header-title">Want more components?</li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-pro-react"
                color="danger"
                block
                round
                disabled
              >
                Get pro version
              </Button>
            </li>
          </ul>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  setBgAction: (payload) => dispatch(setBgAction(payload)),
  setColorAction: (payload) => dispatch(setColorAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(FixedPlugin);
```

Et nous avons terminé, vous pouvez démarrer le projet et voir comment tout fonctionne bien :

![Image](https://cdn-media-1.freecodecamp.org/images/Pxtk6P8ssePiK2LaAmOuG4tvn8SCXwJPVKs3)

### Plusieurs reducers

Comme vous pouvez avoir plusieurs actions, vous pouvez avoir plusieurs reducers. La seule chose est que vous devez les combiner — nous verrons cela un peu plus loin.

Allons-y et créons deux nouveaux reducers pour notre application, un pour **setBgAction** et un pour **setColorAction** :

1 — Commandes Linux / Mac

```bash
touch src/reducers/bgReducer.js
touch src/reducers/colorReducer.js
```

2 — Commandes Windows

```bash
echo "" > src\reducers\bgReducer.js
echo "" > src\reducers\colorReducer.js
```

Après cela, créons le code des reducers comme suit :

— **src/reducers/bgReducer.js**

```js
export default (state = {}, action) => {
  switch (action.type) {
    case "bgChange":
      return {
        ...state,
        bgColor: action.payload
      };
    default:
      return state;
  }
};
```

— **src/reducers/colorReducer.js**

```js
export default (state = {} , action) => {
  switch (action.type) {
    case "colorChange":
      return {
        ...state,
        activeColor: action.payload
      };
    default:
      return state;
  }
};
```

Lorsque vous travaillez avec des reducers combinés, vous devez ajouter un **état par défaut** dans chacun de vos reducers qui vont être combinés. Dans mon cas, j'ai choisi un objet vide, c'est-à-dire **state = {}**;

Et maintenant, notre **rootReducer** combinera ces deux éléments comme suit :

— **src/reducers/rootReducer.js**

```js
import { combineReducers } from 'redux';

import bgReducer from 'reducers/bgReducer';
import colorReducer from 'reducers/colorReducer';

export default combineReducers({
  activeState: colorReducer,
  bgState: bgReducer
});
```

Nous disons donc que nous voulons que le **colorReducer** soit référencé par la prop **activeState** de l'état de l'application, et que le **bgReducer** soit référencé par la prop **bgState** de l'état de l'application.

Cela signifie que notre état ne ressemblera plus à ceci :

```js
state = {
  activeColor: "color1",
  bgColor: "color2"
}
```

Il ressemblera maintenant à ceci :

```js
state = {
  activeState: {
    activeColor: "color1"
  },
  bgState: {
    bgColor: "color2"
  }
}
```

Puisque nous avons changé nos reducers, nous les avons maintenant combinés en un seul, nous devons également changer notre **store.js** :

— **src/store.js**

```js
import { createStore } from "redux";
import rootReducer from "reducers/rootReducer";

// nous devons passer l'état initial avec le nouveau look
function configureStore(state = { bgState: {bgColor: "black"}, activeState: {activeColor: "info"} }) {
  return createStore(rootReducer,state);
}
export default configureStore;
```

Puisque nous avons changé la façon dont l'état est structuré, nous devons maintenant changer les props à l'intérieur des composants **Sidebar** et **FixedPlugin** pour correspondre au nouvel objet d'état :

— **src/components/Sidebar/Sidebar.jsx** :

Changez la **ligne 36** de

```jsx
<div className="sidebar" data-color={this.props.bgColor} data-active-color={this.props.activeColor}>
```

en

```jsx
<div className="sidebar" data-color={this.props.bgState.bgColor} data-active-color={this.props.activeState.activeColor}>
```

— **src/components/FixedPlugin/FixedPlugin.jsx** :

Nous devons changer tous les `**this.props.bgColor**` en `**this.props.bgState.bgColor**`. Et tous les `**this.props.activeColor**` en `**this.props.activeState.activeColor**`.

Donc, le nouveau code devrait ressembler à ceci :

```jsx
import React, { Component } from "react";

import Button from "components/CustomButton/CustomButton.jsx";

import { connect } from "react-redux";
import setBgAction from "actions/setBgAction";
import setColorAction from "actions/setColorAction";

class FixedPlugin extends Component {
  constructor(props) {
    super(props);
    this.state = {
      classes: "dropdown show"
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    if (this.state.classes === "dropdown") {
      this.setState({ classes: "dropdown show" });
    } else {
      this.setState({ classes: "dropdown" });
    }
  }
  render() {
    return (
      <div className="fixed-plugin">
        <div className={this.state.classes}>
          <div onClick={this.handleClick}>
            <i className="fa fa-cog fa-2x" />
          </div>
          <ul className="dropdown-menu show">
            <li className="header-title">SIDEBAR BACKGROUND</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.bgState.bgColor === "black"
                      ? "badge filter badge-dark active"
                      : "badge filter badge-dark"
                  }
                  data-color="black"
                  onClick={() => {
                    this.props.setBgAction("black");
                  }}
                />
                <span
                  className={
                    this.props.bgState.bgColor === "white"
                      ? "badge filter badge-light active"
                      : "badge filter badge-light"
                  }
                  data-color="white"
                  onClick={() => {
                    this.props.setBgAction("white");
                  }}
                />
              </div>
            </li>
            <li className="header-title">SIDEBAR ACTIVE COLOR</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.activeState.activeColor === "primary"
                      ? "badge filter badge-primary active"
                      : "badge filter badge-primary"
                  }
                  data-color="primary"
                  onClick={() => {
                    this.props.setColorAction("primary");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "info"
                      ? "badge filter badge-info active"
                      : "badge filter badge-info"
                  }
                  data-color="info"
                  onClick={() => {
                    this.props.setColorAction("info");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "success"
                      ? "badge filter badge-success active"
                      : "badge filter badge-success"
                  }
                  data-color="success"
                  onClick={() => {
                    this.props.setColorAction("success");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "warning"
                      ? "badge filter badge-warning active"
                      : "badge filter badge-warning"
                  }
                  data-color="warning"
                  onClick={() => {
                    this.props.setColorAction("warning");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "danger"
                      ? "badge filter badge-danger active"
                      : "badge filter badge-danger"
                  }
                  data-color="danger"
                  onClick={() => {
                    this.props.setColorAction("danger");
                  }}
                />
              </div>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react"
                color="primary"
                block
                round
              >
                Download now
              </Button>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react/#/documentation/tutorial"
                color="default"
                block
                round
                outline
              >
                <i className="nc-icon nc-paper"></i> Documentation
              </Button>
            </li>
            <li className="header-title">Want more components?</li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-pro-react"
                color="danger"
                block
                round
                disabled
              >
                Get pro version
              </Button>
            </li>
          </ul>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  setBgAction: (payload) => dispatch(setBgAction(payload)),
  setColorAction: (payload) => dispatch(setColorAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(FixedPlugin);
```

Ouvrons à nouveau le projet avec `npm start` et voyons comment tout fonctionne. Et voilà !

### Merci d'avoir lu !

Si vous avez apprécié la lecture de ce tutoriel, veuillez le partager. Je suis très intéressé par vos commentaires à ce sujet. Laissez simplement un commentaire dans ce fil et je serai plus qu'heureux de répondre.

Des remerciements spéciaux doivent également aller à [Esther Falayi](https://medium.com/@estherfalayi) pour son [tutoriel](https://medium.com/backticks-tildes/setting-up-a-redux-project-with-create-react-app-e363ab2329b8) qui m'a donné une compréhension bien nécessaire de **Redux**.

Liens utiles :

* Obtenez le code de ce tutoriel depuis [Github](https://github.com/creativetimofficial/react-redux-tutorial)
* Lisez plus sur ReactJS sur [leur site officiel](https://reactjs.org/)
* Lisez plus sur [Redux ici](https://redux.js.org/)
* Lisez plus sur [React-Redux](https://react-redux.js.org/)
* Consultez notre plateforme pour voir [ce que nous faisons](https://www.creative-tim.com/) et [qui nous sommes](https://www.creative-tim.com/presentation)
* Obtenez Paper Dashboard React depuis [www.creative-tim.com](https://www.creative-tim.com/product/paper-dashboard-react) ou depuis [Github](https://github.com/creativetimofficial/paper-dashboard-react)
* Lisez plus sur [Reactstrap](https://reactstrap.github.io/), le cœur de Paper Dashboard React

Trouvez-moi sur :

* Email : [manu@creative-tim.com](mailto:manu@creative-tim.com)
* Facebook : [https://www.facebook.com/NazareEmanuel](https://www.facebook.com/NazareEmanuel)
* Instagram : [https://www.instagram.com/manu.nazare/](https://www.instagram.com/manu.nazare/)
* Linkedin : [https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/](https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/)