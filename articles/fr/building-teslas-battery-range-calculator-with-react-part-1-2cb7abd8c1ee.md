---
title: Construction du calculateur d'autonomie de batterie de Tesla avec React (Partie
  1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-21T00:25:23.000Z'
originalURL: https://freecodecamp.org/news/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8hlNoLDBy5XWZct5tAtPoA.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Construction du calculateur d'autonomie de batterie de Tesla avec React
  (Partie 1)
seo_desc: 'By Matthew Choi

  In this series of articles, I will walk you through the process of building Tesla’s
  battery range calculator with React.

  In this tutorial, we’ll build the React version of Todd Motto’s Building Tesla’s
  battery range calculator with An...'
---

Par Matthew Choi

Dans cette série d'articles, je vais vous guider à travers le processus de construction du calculateur d'autonomie de batterie de Tesla avec React.

Dans ce tutoriel, nous allons construire la version React du [Building Tesla's battery range calculator with Angular 2 reactive forms](https://toddmotto.com/building-tesla-range-calculator-angular-2-reactive-forms) de Todd Motto.

Ainsi, cet article réutilisera certains matériaux (données, images et style CSS). Nous nous concentrerons sur la reconstruction de celui-ci à la manière **React**.

Voici l'image GIF finale de notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/fUI8CpLiySb4PZmrg2l8MU9NRpEEn9oECeCw)

? Consultez la [version live](http://react-tesla-charge-calculator.surge.sh/) avant de commencer.

? Vous pouvez également consulter le [code source](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial).

Maintenant, créons l'application étape par étape.

Notez que vous aurez peut-être besoin de quelques connaissances de base sur React pour suivre ce tutoriel. Voir les ressources suivantes :

* [Documentation officielle de React](https://facebook.github.io/react/docs/hello-world.html)
* [React : Getting Started and Concepts](https://scotch.io/tutorials/learning-react-getting-started-and-concepts)

### 1. Configuration du projet et create-react-app

### 1.1 Prérequis

Les outils et versions que j'ai utilisés lors de l'implémentation de cette application :

```
node v7.3.0
npm v3.10.10
```

### 1.2 create-react-app

[**create-react-app**](https://github.com/facebookincubator/create-react-app) est un nouvel outil open-source de Facebook pour le développement rapide d'applications React, qui permet de démarrer facilement des applications React sans configurations complexes. Vous pouvez facilement installer notre projet `react-tesla-range-calculator` et démarrer l'application immédiatement avec la commande suivante :

* npm install -g create-react-app
* create-react-app react-tesla-range-calculator
* cd react-tesla-range-calculator
* npm start

![Image](https://cdn-media-1.freecodecamp.org/images/uSkna3EYzFNgD2Bx6sxmnctVveRaihVJqpnA)

Créez une nouvelle application via `create-react-app` et ouvrez `http://localhost:3000/` pour vérifier l'application générée.

Si vous voyez l'écran ci-dessous, le projet a été configuré avec succès.

![Image](https://cdn-media-1.freecodecamp.org/images/T9IvNxAK5EUahMqx-7ZqWamaqas3XIQFGbfv)

Avant de commencer le projet, nous devons modifier la structure source du projet. Conservez uniquement les fichiers nécessaires au projet et supprimez le reste. (Supprimez App.test.js, logo.svg)

Notre répertoire src devrait maintenant ressembler à ceci :

```
src
 - App.css
 - App.js
 - index.css
 - index.js
```

Voici la structure source du projet :

![Image](https://cdn-media-1.freecodecamp.org/images/gX8PXxxctxfOc9BYffAzWqDcSDqvRMH2QfYV)

### 1.3 Point d'entrée du projet

Tout d'abord, nous devons définir le point d'entrée pour démarrer notre application Tesla. Heureusement, il est déjà créé par `create-react-app`.

`src/App.js` est le point d'entrée de notre application.

Tout d'abord, modifiez votre `App.js` comme suit :

```
import React, { Component } from 'react';
import './App.css';
```

```
class App extends Component {
  render() {
    return (
      <div>
        <h2>Commençons</h2>
      </div>
    );
  }
}
```

```
export default App;
```

Lorsque vous enregistrez le fichier, il sera automatiquement compilé et vous pourrez voir l'écran mis à jour.

### 1.4 Images et ressources du projet

Toutes les images nécessaires à ce projet peuvent être téléchargées depuis :

* images [Télécharger](https://toddmotto.com/static/assets.zip)
* favicon.ico [Télécharger](https://toddmotto.com/static/favicon.ico)

Décompressez `assets.zip` et placez toutes les images dans le répertoire `src/assets` et placez le `favicon.ico` téléchargé à la racine du projet.

```
react-tesla-range-calculator/src/assets
```

> À tout moment, si vous avez l'impression d'avoir manqué quelque chose ou si vous n'êtes pas sûr de faire les choses correctement, vous pouvez vous référer au [code source](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial) comme référence.

### 1.5 Service de données

Les données que vous pouvez obtenir depuis le site Tesla sont codées en dur et très volumineuses, nous allons donc utiliser la nouvelle version des données de Todd pour les rendre plus faciles à utiliser. [lien](https://github.com/toddmotto/angular-tesla-range-calculator/blob/master/src/app/tesla-battery/tesla-battery.service.ts)

Nous n'utilisons pas le `décorateur Injectable` utilisé dans Angular2, nous allons donc copier uniquement la partie `export`, enregistrez-la simplement dans `src/services/BatteryService.js` pour l'instant. Plus tard, nous l'utiliserons dans le conteneur `TeslaBattery`.

Nous reviendrons sur ce service de données plus tard.

### 2. Décomposition de l'interface utilisateur

Presque toutes les interfaces utilisateur des applications React consistent en une composition de composants. Par exemple, une application météo consiste en un composant qui affiche un nom local, un composant qui affiche la température actuelle et un composant graphique qui représente une prévision sur cinq jours. Pour cette raison, il est bon de décomposer l'interface utilisateur en unités de composants avant de développer l'application React.

> Voir [Thinking in React](https://facebook.github.io/react/docs/thinking-in-react.html) pour une approche de l'examen d'une application comme une combinaison de composants.

La disposition de cette application est montrée ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/2qCWIymRRtFN24HQ2mdpfooQf1GimpMxmtzv)

L'interface utilisateur est représentée par un arbre de composants comme suit.

```
<App> -- Point d'entrée de l'application
  <Header></Header>
  <TeslaBattery> -- Conteneur
    <TeslaCar />     -- Composant de présentation
    <TeslaStats />   -- Composant de présentation
    <TeslaCounter /> -- Composant de présentation
    <TeslaClimate /> -- Composant de présentation
    <TeslaWheels />  -- Composant de présentation
    <TeslaNotice />  -- Composant de présentation
  </TeslaBattery>
</App>
```

### 2.1 Composants Conteneur et Présentation

Dans l'arbre de composants mentionné ci-dessus, nous pouvons voir qu'il est classé comme `Composant Conteneur` et `Composant de Présentation`.

C'est un modèle utile qui peut être utilisé lors du développement d'une application avec React. Il est plus facile de réutiliser en divisant les composants en deux catégories.

```
* Composant Conteneur (composant avec état) :
  - S'occupe de la manière dont les choses fonctionnent.
  - En général, à part quelques divs d'encapsulation, ils n'ont pas leur propre balisage DOM et n'ont pas de style.
  - Fournissent des données et des actions aux composants de présentation ou à d'autres composants conteneurs.
  - Sont souvent avec état, car ils tendent à servir de sources de données.
```

```
* Composant de Présentation (composant sans état) :
  - S'occupe de l'apparence des choses.
  - Ont généralement un balisage DOM et des styles propres.
  - Reçoivent des données et des rappels exclusivement via les props.
  - Ont rarement leur propre état (quand ils en ont, c'est un état d'interface utilisateur plutôt que de données).
```

Quels sont les avantages de l'utilisation de ces modèles ?

* Meilleure séparation des préoccupations
* Meilleure réutilisabilité
* Extraction des composants de mise en page pour éviter la duplication

> Pour plus de détails, voir [Composants de Présentation et Conteneur](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0#.mbwo09sds)

### 3. Composant Header

Créons notre premier composant React, `Header`. Le composant `Header` est simplement une barre noire avec le logo Tesla et du texte.

Créez le répertoire `src/components/Header`, créez un fichier `Header.js` dans celui-ci, et entrez le code suivant :

```
import React from 'react';
import './Header.css';
import logoUrl from '../../assets/logo.svg';
```

```
const Header = () => (
  <div className="header">
    <img src={logoUrl} alt="Tesla" />
  </div>
)
```

```
export default Header;
```

> Ici, le composant est sous la forme d'une fonction (`ES6 Arrow Function`). Un composant déclaré sous cette forme est appelé un `composant fonctionnel`. Si il n'y a pas d'`état` et que la méthode `lifecycle` n'est pas nécessaire, c'est un bon modèle de le déclarer comme un type fonction. Les composants fonctionnels sont adaptés pour les `Composants de Présentation` car ils n'ont pas d'état et dépendent uniquement des `props` qu'ils reçoivent des composants parents.

### 3.1 Style du Composant Header

Créez un fichier `Header.css` dans le répertoire `src/components/Header` et tapez le style suivant :

```
.header {
  padding: 25px 0;
  text-align: center;
  background: #222;
}
```

```
.header img {
  width: 100px;
  height: 13px;
}
```

> Il existe plusieurs façons d'appliquer des styles aux composants, mais ici nous allons créer chaque répertoire de composant dans le répertoire `src/components` et associer les fichiers `js` et `css` chaque fois que nous créons un composant.

### 3.2 Importer le composant Header dans le Conteneur App

Maintenant que vous avez créé le composant `Header`, utilisons `import` dans le point d'entrée `App.js`.

```
import React, { Component } from 'react';
import './App.css';
import Header from './components/Header/Header';
```

```
class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
      </div>
    );
  }
}
```

```
export default App;
```

Lorsque vous enregistrez tous les fichiers modifiés, ils seront mis à jour automatiquement et vous devriez voir le logo Tesla comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/CBG-JQw6g9uFWVPRzryHZjuh-vxYom7Tt4ZS)

### 4. Conteneur TeslaBattery

Dans notre application, le composant `TeslaBattery` est responsable de la création et de la gestion des données et de l'état en tant que `Composant Conteneur`, de leur transmission à d'autres `Composants de Présentation`, de l'exécution d'une fonction de rappel et du changement de son état.

En héritant de `React.Component`, `TeslaBattery` doit avoir une méthode `render`, optionnellement il peut initialiser son état via le `constructeur`, et implémenter d'autres méthodes telles que les rappels de [lifecycle](https://facebook.github.io/react/docs/react-component.html).

Les rappels de `lifecycle` sont utiles lorsque vous souhaitez rendre ou mettre à jour des composants, ou pour recevoir des notifications à différentes étapes du `lifecycle`.

Créez le répertoire `src/containers`, créez un fichier `TeslaBattery.js` dans celui-ci, et entrez le code suivant :

```
import React from 'react';
import './TeslaBattery.css';
```

```
class TeslaBattery extends React.Component {
  render() {
    return (
      <form className="tesla-battery">
        <h1>Autonomie par charge</h1>
      </form>
    )
  }
}
```

```
export default TeslaBattery;
```

### 4.1 Style du Conteneur TeslaBattery

`TeslaBattery.css` ne contient qu'un style minimal.

```
.tesla-battery {
  width: 1050px;
  margin: 0 auto;
}
```

```
.tesla-battery h1 {
  font-family: 'RobotoNormal';
  font-weight: 100;
  font-size: 38px;
  text-align: center;
  letter-spacing: 3px;
}
```

Les composants à créer dans le futur seront configurés dans le conteneur `TeslaBattery` séquentiellement.

### 5. Composant TeslaNotice

Créons une partie de texte statique avec un composant `TeslaNotice`.

Créez le répertoire `src/components/TeslaNotice`, créez un fichier `TeslaNotice.js` dans celui-ci, et entrez le code suivant :

```
import React from 'react';
import './TeslaNotice.css';
```

```
const TeslaNotice = () => (
  <div className="tesla-battery__notice">
    <p>
      La quantité réelle d'autonomie que vous expériencerez variera en fonction de vos conditions d'utilisation particulières. Voyez comment des conditions d'utilisation particulières peuvent affecter votre autonomie dans notre modèle de simulation.
    </p>
    <p>
      L'autonomie du véhicule peut varier en fonction de la configuration du véhicule, de l'âge et de l'état de la batterie, du style de conduite et des conditions environnementales et climatiques.
    </p>
  </div>
)
```

```
export default TeslaNotice;
```

### 5.1 Style du Composant TeslaNotice

Ensuite, créez le répertoire `src/components/TeslaNotice`, créez `TeslaNotice.css` dans celui-ci et ajoutez ces styles à votre fichier `TeslaNotice.css` :

```
.tesla-battery__notice {
    margin: 20px 0;
    font-size: 15px;
    color: #666;
    line-height: 20px;
}
```

### 5.2 Importer le composant TeslaNotice dans le Conteneur TeslaBattery

Ensuite, importez le composant `TeslaNotice` dans `TeslaBattery.js` :

```
...import TeslaNotice from '../components/TeslaNotice/TeslaNotice';
```

```
class TeslaBattery extends React.Component {
  render() {
    return (
      <form className="tesla-battery">
        <h1>Autonomie par charge</h1>
        <TeslaNotice />
      </form>
    )
  }
}
```

> Nous continuerons de cette manière, les composants sont créés selon ce modèle et importés depuis le conteneur `TeslaBattery`.

### 6. Composant TeslaCar

Maintenant, affichons une belle image de voiture Tesla avec une animation de roues.

Créez le répertoire `src/components/TeslaCar`, créez un fichier `TeslaCar.js` dans celui-ci, et à l'intérieur de votre fichier `TeslaCar.js` :

```
import React from 'react';
import './TeslaCar.css';
```

```
const TeslaCar = (props) => (
  <div className="tesla-car">
    <div className="tesla-wheels">
      <div className={`tesla-wheel tesla-wheel--front tesla-wheel--${props.wheelsize}`}></div>
      <div className={`tesla-wheel tesla-wheel--rear tesla-wheel--${props.wheelsize}`}></div>
    </div>
  </div>
);
```

```
TeslaCar.propTypes = {
  wheelsize: React.PropTypes.number
}
```

```
export default TeslaCar;
```

Ici, nous spécifions `propTypes` en utilisant la vérification de type intégrée de React. En mode développement, React vérifie les `props` passés au composant. (Uniquement en mode développement pour des raisons de performance)

Pour chaque attribut `props`, React tente de le trouver dans l'objet `propType` du composant pour déterminer si (1) la prop est attendue (2) la prop est du bon type. Dans ce cas, le composant `TeslaCar` attend l'attribut `props` `wheelsize` et spécifie qu'il est de type `number`. Si la mauvaise valeur est fournie, un avertissement apparaît dans la console JavaScript, ce qui est utile pour corriger les bugs potentiels à un stade précoce.

> Plus d'informations sur `React.PropTypes` peuvent être trouvées [ici](https://facebook.github.io/react/docs/typechecking-with-proptypes.html)

> Mise à jour : Nouveaux avertissements de dépréciation dans React 15.5

> Dans la version 15.5, au lieu d'accéder à `PropTypes` depuis l'objet principal `React`, installez le package `prop-types` et importez-les depuis celui-ci :

https://facebook.github.io/react/blog/2017/04/07/react-v15.5.0.html#migrating-from-react.proptypes

```
// Avant (15.4 et versions antérieures)
import React from 'react';
```

```
import React from 'react';
import './TeslaCar.css';
```

```
.........................
```

```
TeslaCar.propTypes = {
  wheelsize: React.PropTypes.number
}
```

```
export default TeslaCar;
```

```
// Après (15.5)
import React from 'react';
import PropTypes from 'prop-types';
import './TeslaCar.css';
```

```
...........................
```

```
TeslaCar.propTypes = {
   wheelsize: PropTypes.number
}

export default TeslaCar;
```

### 6.1 Style du Composant TeslaCar

Ensuite, créez un fichier `TeslaCar.css` dans le répertoire `src/components/TeslaCar` et donnez-lui le style suivant. Comme le code est long et omis ici, vérifions le [code source](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaCar/TeslaCar.css).

```
.tesla-car {
  width: 100%;
  min-height: 350px;
  background: #fff url(../../assets/tesla.jpg) no-repeat top center;
  background-size: contain;
}
```

```
.tesla-wheels {
  height: 247px;
  width: 555px;
  position: relative;
  margin: 0 auto;
}
```

```
...
```

Cela nous donne nos animations et la base du composant pour la voiture, qui est affichée comme des images de fond.

### 6.2 Importer le composant TeslaCar dans le Conteneur TeslaBattery

Ensuite, nous devons ajouter ce composant à notre conteneur. Importez le composant `TeslaNotice` dans `TeslaBattery.js` :

```
...import TeslaCar from '../components/TeslaCar/TeslaCar';
```

```
class TeslaBattery extends React.Component {
  render() {
    return (
      <form className="tesla-battery">
        <h1>Autonomie par charge</h1>
        <TeslaCar />
        <TeslaNotice />
      </form>
    )
  }
}
```

Voici ce que vous devriez voir :

![Image](https://cdn-media-1.freecodecamp.org/images/slITEDdL1ebpoM9t9iRnSgqxsoMhm7ltfzIF)

### 7. Props et React Developer Tools

Wow ! C'est bien, mais il manque quelque chose. Les roues ne sont pas affichées. Cherchons la cause. Selon le code source, `TeslaCar` devrait recevoir `props` et changer le nom de la classe en fonction de `props.wheelsize`.

En d'autres termes, vous devez recevoir certaines données (dans ce cas, wheelsize) du composant parent et les rendre correctement, et il doit y avoir une méthode de communication qui peut recevoir les données.

React est composé d'un arbre de composants, qui consiste en un conteneur pour livrer des données et un état, et un composant pour recevoir passivement des données et un état d'un conteneur. L'outil qui livre cet état aux sous-composants est un objet unique, `props`.

Vous pouvez facilement comprendre cela en vérifiant l'arbre de composants en utilisant [React Developer Tools](https://www.google.com.au/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwi10rn7soTSAhVJp5QKHYPcC5YQFggbMAA&url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Freact-developer-tools%2Ffmkadmapgofadopljbjfkapdkoienihi%3Fhl%3Den&usg=AFQjCNEv0udXgBoaukzJa59I_vufhScUbQ&sig2=wTA5bB3JG2ZQ6wbSiDgq8g) dans Chrome.

![Image](https://cdn-media-1.freecodecamp.org/images/z1YAvglHQweK1-OKRD1hDZoFEUR3spY5c9ls)

`props` est un objet JavaScript unique, dans ce cas un objet vide. Cela est dû au fait que nous n'avons pas passé `props` dans le composant parent `TeslaBattery`.

### 8. État de l'application

Nous devons réfléchir à l'état nécessaire à gérer dans notre application. Si vous regardez l'image GIF de l'application finale en haut de cet article, les valeurs d'état sont :

* **carstats (tableau d'objets)** : Un tableau d'objets de valeurs numériques de batterie par modèle de voiture selon la valeur de condition actuellement sélectionnée (vitesse, température, climat, roue)
* **config (objet)** : Objet des conditions actuellement sélectionnées (vitesse : 55, température : 20, climat : aircon activé, roue : 19)

![Image](https://cdn-media-1.freecodecamp.org/images/-4uy9c8rD8Zg2kftWpeSpuR5ibIteogplLb4)
_état de l'application_

C'est la seule source de vérité pour notre application. Maintenant, nous allons ajouter la méthode constructeur au conteneur `TeslaBattery` et définir la valeur initiale afin que nous puissions gérer cette valeur d'état et la transmettre au sous-composant. Le composant `TeslaCar` accepte l'entrée `wheelsize` via `props` et rend l'image de la voiture Tesla et fait tourner les roues.

> Ni le composant parent ni le composant enfant ne savent si un composant particulier est avec état ou sans état et ne se soucient pas de savoir s'il est défini comme une `fonction` ou une `classe`. C'est pourquoi l'état est souvent appelé local ou encapsulé. Cet état ne peut pas être accédé par des composants autres que le composant qui possède et définit l'état. Ainsi, cette valeur d'état peut être transmise au sous-composant en tant que `props`. Cela est communément appelé un flux de données "top-down" ou "unidirectionnel". Chaque état est toujours possédé par un composant particulier, et toute donnée ou interface utilisateur dérivée de cet état n'affecte que le composant "descendant" de l'arbre.

```
...class TeslaBattery extends React.Component {
  constructor(props) {
    super(props);
```

```
    this.state = {
      carstats: [],
      config: {
        speed: 55,
        temperature: 20,
        climate: true,
        wheels: 19
      }
    }
  }
    render() {
    // Syntaxe de déstructuration d'objet ES6,
    // prend les valeurs requises et crée des références à celles-ci
    const { config } = this.state;
    return (
      <form className="tesla-battery">
        <h1>Autonomie par charge</h1>
        <TeslaCar wheelsize={config.wheels}/>
        <TeslaNotice />
      </form>
    )
  }
}
```

Dans `render()`, le code sous la forme `const {a, b} = c` est la `Déstructuration d'Objets ES6`. Il prend la valeur requise de l'objet et en fait une référence.

> Conceptuellement, le composant React est comme une fonction JavaScript et reçoit une entrée arbitraire appelée **'props'** et retourne un élément React qui décrit ce qui doit être montré.

En un mot, ce concept peut être exprimé par la formule suivante.

> **fn(d) = V**

Une fonction qui reçoit des données en entrée et retourne une vue.

Si vous enregistrez les fichiers, vous pouvez voir que la voiture Tesla rendue et l'animation des roues fonctionnent bien sur l'écran mis à jour. Vous pouvez également voir que `props` est bien passé dans l'arbre des composants.

![Image](https://cdn-media-1.freecodecamp.org/images/3xPha8EmpJmYvDZscwHafy9GQfChrIeqz8eB)
_props de TeslaCar_

> Certaines fonctions sont appelées "pures" dans le sens où elles retournent toujours la même valeur de sortie si elles ont la même valeur d'entrée sans changer la valeur d'entrée. (`Fonction pure`) Une règle stricte importante de React ici est que tous les composants React doivent se comporter comme des fonctions pures par rapport aux props. `props` doit être en lecture seule.

### 9. Composant TeslaStats

Maintenant, nous allons construire le composant `TeslaStats`. Créez le répertoire `src/components/TeslaStats`, créez un fichier `TeslaStats.js` dans celui-ci, et entrez le code suivant :

```
import React from 'react';
import './TeslaStats.css';
```

```
const TeslaStats = (props) => {
  const listItems = props.carstats.map((stat) => (
    <li key={stat.model}>
      <div className={`tesla-stats-icon tesla-stats-icon--${stat.model.toLowerCase()}`}></div>
      <p>{stat.miles}</p>
    </li>
  ));
  return (
    <div className="tesla-stats">
    <ul>
      {listItems}
      </ul>
  </div>
  )};
```

```
TeslaStats.propTypes = {
  carstats: React.PropTypes.array
}
```

```
export default TeslaStats;
```

`TeslaStats` est également un `composant de présentation` qui reçoit l'état, et il prend une liste de tableaux contenant des valeurs de modèle par `props` et les rend.

Tout d'abord, réfléchissons à la manière de transformer une liste en JavaScript. Le code suivant utilise la fonction `map()` pour prendre un tableau `numbers` et retourner une valeur double.

Ce code imprime `[2, 4, 6, 8, 10]` dans la console.

```
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((number) => number * 2);
console.log(doubled);
```

La conversion d'un tableau en une liste dans React est presque identique. Ici, nous utilisons la fonction `map` de JavaScript pour itérer à travers le tableau `props.carstats`.

Pour chaque itération, il retourne un élément `<li>` contenant le modèle et un élément `<li>` entourant la balise `<p>` contenant les miles.

Enfin, il retourne le tableau `listItems` dans l'élément `<ul>`.

### 9.1 Style du Composant TeslaStats

Ensuite, créez un fichier `TeslaStats.css` dans le répertoire `src/components/TeslaStats` et tapez le style suivant. Comme le code est long et omis ici, vérifions le [code source](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaStats/TeslaStats.css)

```
....tesla-stats {
  margin: -70px 0 30px;
}
.tesla-stats ul {
  text-align: center;
}
...
```

La tâche que ce composant effectue est d'itérer à travers le tableau `props.carstats` et de lier une classe particulière à un élément en fonction de `stat.model`. Vous pouvez ensuite remplacer l'image de fond pour afficher le modèle Tesla.

### 9.2 Importer le composant TeslaStats dans le Conteneur TeslaBattery

Ensuite, ajoutez l'`import` suivant pour utiliser le composant `TeslaStats` dans `TeslaBattery.js`.

```
...import TeslaStats from '../components/TeslaStats/TeslaStats';
...render() {
  const { config, carstats } = this.state;
  return (
    <form className="tesla-battery">
      <h1>Autonomie par charge</h1>
      <TeslaCar wheelsize={config.wheels}/>
      <TeslaStats carstats={carstats}/>
      <TeslaNotice />
    </form>
  )
}
...
```

Nous devons passer le tableau `carstats` à `props`, alors définissons la valeur en utilisant `BatteryService` que nous avons déjà implémenté.

### 9.3 CalculateStats et setState

Ajoutez d'abord l'import `getModelData`.

Après que le composant soit monté via `componentDidMount()`, il appelle la fonction `statsUpdate()`. Lorsque la fonction `calculateStats()` qui reçoit `carModels` et la valeur d'état actuelle en entrée est exécutée, l'objet avec les valeurs `model` et `miles` correspondantes est retourné, et la valeur de retour est passée via `setState()` puis l'objet d'état est mis à jour.

```
...import { getModelData } from '../services/BatteryService';
...
```

```
calculateStats = (models, value) => {
  const dataModels = getModelData();
  return models.map(model => {
    // Syntaxe de déstructuration d'objet ES6,
    // prend les valeurs requises et crée des références à celles-ci
    const { speed, temperature, climate, wheels } = value;
    const miles = dataModels[model][wheels][climate ? 'on' : 'off'].speed[speed][temperature];
    return {
      model,
      miles
    };
  });
}

statsUpdate() {
  const carModels = ['60', '60D', '75', '75D', '90D', 'P100D'];
  // Récupérer les informations du modèle depuis BatteryService et calculer puis mettre à jour l'état
  this.setState({
    carstats: this.calculateStats(carModels, this.state.config)
  })
}

componentDidMount() {
  this.statsUpdate();
}
...
```

Un point à noter est que la liaison explicite dans la fonction constructeur `TeslaBattery` est requise pour accéder à `this` dans la classe.

```
...this.calculateStats = this.calculateStats.bind(this);
this.statsUpdate = this.statsUpdate.bind(this);
...
```

### 9.4 Ajouter un Style Supplémentaire

Un style supplémentaire est nécessaire pour une belle mise en page ici.

Ouvrez d'abord le fichier `src/index.css` et supprimez tout le code existant et ajoutez ce qui suit :

```
@font-face {
  font-family: 'RobotoNormal';
  src: url('./assets/fonts/Roboto-Regular-webfont.eot');
  src: url('./assets/fonts/Roboto-Regular-webfont.eot?#iefix') format('embedded-opentype'),
       url('./assets/fonts/Roboto-Regular-webfont.woff') format('woff'),
       url('./assets/fonts/Roboto-Regular-webfont.ttf') format('truetype'),
       url('./assets/fonts/Roboto-Regular-webfont.svg#RobotoRegular') format('svg');
  font-weight: normal;
  font-style: normal;
}
```

```
*, *:before, *:after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font: 300 14px/1.4 'Helvetica Neue', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
```

```
.cf:before,.cf:after {
    content: '';
    display: table;
}
.cf:after {
    clear: both;
}
.cf {
  *zoom: 1;
}
```

Ensuite, ouvrez le fichier `src/App.css` et supprimez tout le code existant et ajoutez ce qui suit :

```
.wrapper {
  margin: 100px 0 150px;
}
```

Le résultat du travail jusqu'à présent est le suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/Zavrgma-9iWKaUxYeSex7M-hTUwrhXRua2kG)

### 10. Composant TeslaCounter Réutilisable

Les contrôles de vitesse et de température extérieure de Tesla doivent être des composants réutilisables, je vais donc en faire un composant Counter générique qui permet d'autres métadonnées telles que le pas, le minimum, le maximum, le titre et les unités (mph / degrés).

De plus, contrairement aux composants que nous avons créés jusqu'à présent, nous avons besoin d'une action pour changer la valeur d'état en réponse à l'entrée de l'utilisateur (clic sur un bouton, sélection de case à cocher, etc.). Voyons comment gérer les événements qui se produisent dans un sous-composant.

Créez le répertoire `src/components/TeslaCounter` comme précédemment, créez un fichier `TeslaCounter.js` dans celui-ci, et entrez le code suivant :

```
import React from 'react';
import './TeslaCounter.css';
```

```
const TeslaCounter = (props) => (
  <div className="tesla-counter">
    <p className="tesla-counter__title">{props.initValues.title}</p>
    <div className="tesla-counter__container cf">
      <div className="tesla-counter__item">
        <p className="tesla-counter__number">
          { props.currentValue }
          <span>{ props.initValues.unit }</span>
        </p>
        <div className="tesla-counter__controls">
          <button
             onClick={(e) => props.increment(e, props.initValues.title)}
             disabled={props.currentValue >= props.initValues.max}
           >
          </button>
          <button
             onClick={(e) => props.decrement(e, props.initValues.title)}
             disabled={props.currentValue <= props.initValues.min}
           >
          </button>
        </div>
      </div>
    </div>
  </div>
);
```

```
TeslaCounter.propTypes = {
  currentValue: React.PropTypes.number,
  increment: React.PropTypes.func,
  decrement: React.PropTypes.func,
  initValues: React.PropTypes.object
}
```

```
export default TeslaCounter;
```

Réfléchissons à ce que nous voulons ici. Chaque fois que vous cliquez et changez la vitesse et la température, vous devez mettre à jour l'état afin que la valeur soit reflétée entre les valeurs maximale et minimale.

Puisque le composant n'a besoin de mettre à jour que son propre état, `TeslaBattery` passe le rappel (`increment`, `decrement`) à `TeslaCounter` chaque fois qu'il doit mettre à jour son état. Vous pouvez utiliser l'événement `onClick` sur un bouton pour notifier l'événement. Le rappel passé par `TeslaBattery` appelle `setState()` et l'application est mise à jour.

Nous allons implémenter un rappel qui sera passé par `TeslaBattery` dans quelques instants.

### 10.1 Style du Composant TeslaCounter

Implémentons d'abord le style. Créez un fichier `TeslaCounter.css` dans le répertoire `src/components/TeslaCounter` et spécifiez les styles suivants. Comme le code est long et omis ici, vérifions le [code source](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaCounter/TeslaCounter.css)

```
.tesla-counter {
  float: left;
  width: 230px;
}
.tesla-counter__title {
  letter-spacing: 2px;
  font-size: 16px;
}
...
```

### 10.2 Importer le Composant TeslaCounter dans le Conteneur TeslaBattery

Maintenant, nous allons implémenter `callback` dans `TeslaBattery` et le passer au composant `TeslaCounter`.

Tout d'abord, ajoutez `import` pour utiliser le composant `TeslaCounter` dans `TeslaBattery.js`.

Nous implémentons également les fonctions de rappel `increment()` et `decrement()`, et la fonction interne `updateCounterState()` et les lions dans le `constructeur`. Ensuite, nous passons la fonction `callback` au composant `TeslaCounter` avec `props`.

```
...constructor(props) {
    super(props);
```

```
    this.calculateStats = this.calculateStats.bind(this);
    this.statsUpdate = this.statsUpdate.bind(this);
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
    this.updateCounterState = this.updateCounterState.bind(this);
```

```
    this.state = {
      carstats: [],
      config: {
        speed: 55,
        temperature: 20,
        climate: true,
        wheels: 19
      }
    }
  }

...

updateCounterState(title, newValue) {
    const config = { ...this.state.config };
    // mettre à jour l'état de la configuration avec la nouvelle valeur
    title === 'Speed' ? config['speed'] = newValue : config['temperature'] = newValue;
    // mettre à jour notre état
    this.setState({ config });
}
```

```
  increment(e, title) {
    e.preventDefault();
    let currentValue, maxValue, step;
    const { speed, temperature } = this.props.counterDefaultVal;
    if (title === 'Speed') {
      currentValue = this.state.config.speed;
      maxValue = speed.max;
      step = speed.step;
    } else {
      currentValue = this.state.config.temperature;
      maxValue = temperature.max;
      step = temperature.step;
    }
```

```
    if (currentValue < maxValue) {
      const newValue = currentValue + step;
      this.updateCounterState(title, newValue);
    }
  }
```

```
  decrement(e, title) {
    e.preventDefault();
    let currentValue, minValue, step;
    const { speed, temperature } = this.props.counterDefaultVal;
    if (title === 'Speed') {
      currentValue = this.state.config.speed;
      minValue = speed.min;
      step = speed.step;
    } else {
      currentValue = this.state.config.temperature;
      minValue = temperature.min;
      step = temperature.step;
    }
```

```
    if (currentValue > minValue) {
      const newValue = currentValue - step;
      this.updateCounterState(title, newValue);
    }
  }

  ...

  render() {
    return (
      <form className="tesla-battery">
        <h1>Autonomie par charge</h1>
        <TeslaCar wheelsize={config.wheels} />
        <TeslaStats carstats={carstats} />
        <div className="tesla-controls cf">
          <TeslaCounter
            currentValue={this.state.config.speed}
            initValues={this.props.counterDefaultVal.speed}
            increment={this.increment}
            decrement={this.decrement}
          />
          <div className="tesla-climate-container cf">
            <TeslaCounter
              currentValue={this.state.config.temperature}
              initValues={this.props.counterDefaultVal.temperature}
              increment={this.increment}
              decrement={this.decrement}
            />
          </div>
        </div>
        <TeslaNotice />
      </form>
    )
  }
```

### 10.3 Style du Conteneur TeslaBattery

Un style supplémentaire est nécessaire pour `TeslaBattery` dès que le composant `TeslaCounter` est ajouté. Ouvrez le fichier `TeslaBattery.css` et ajoutez ce qui suit :

```
.tesla-climate-container {
  float: left;
  width: 420px;
  padding: 0 40px;
  margin: 0 40px 0 0;
  border-left: 1px solid #ccc;
  border-right: 1px solid #ccc;
}
.tesla-controls {
  display: block;
  width: 100%;
}
```

### 10.4 Valeurs par Défaut des Props

Ici, `initValues` passé à `TeslaCounter` est une valeur constante et est passé depuis `App` qui est un composant parent de `TeslaBattery`.

Ouvrez `App.js` et passez l'objet `counterDefaultVal` au composant `TeslaBattery` comme suit :

```
import React, { Component } from 'react';
import './App.css';
import Header from './components/Header/Header';
import TeslaBattery from './containers/TeslaBattery';
```

```
const counterDefaultVal = {
  speed: {
    title: "Vitesse",
    unit: "mph",
    step: 5,
    min: 45,
    max: 70
  },
  temperature: {
    title: "Température extérieure",
    unit: "0",
    step: 10,
    min: -10,
    max: 40
  }
};
```

```
class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <TeslaBattery counterDefaultVal={counterDefaultVal}/>
      </div>
    );
  }
}
```

```
export default App;
```

Maintenant, lorsque vous cliquez sur Vitesse et Température, vous pouvez voir que les valeurs modifiées sont mises à jour et réaffichées dans l'objet d'état via l'outil `React Developer Tool`.

![Image](https://cdn-media-1.freecodecamp.org/images/aYvEg1qqv4lLWNFYRUaHe9hPAEbMJ838Crsz)

### 10.5 DOM Virtuel

Ce qu'une application monopage peut nous offrir est une expérience utilisateur fluide et une interaction fluide.

Dans notre application, les valeurs du modèle de voiture sont mises à jour sans avoir à recharger toute la page chaque fois que l'utilisateur change la vitesse ou la température. Même si vous devez vous connecter au serveur pour obtenir les données. Pour offrir cette expérience utilisateur, vous devez savoir quelle partie du `DOM` vous devez mettre à jour lorsque des changements ou des interactions se produisent.

Chaque framework JavaScript utilise une stratégie différente : `Ember` utilise `data-binding`, `Angular1` utilise [dirty checking](https://docs.angularjs.org/guide/scope), et `React` utilise [Virtual DOM](https://facebook.github.io/react/docs/rendering-elements.html).

Dans React, la première fois que la méthode de rendu du composant est appelée, elle imprime un modèle de `virtual DOM`, plutôt que l'élément `DOM` réel lui-même. Le `virtual DOM` est une structure de données JavaScript qui représente l'apparence du `DOM`. React prend ensuite ce modèle et crée l'élément `DOM` réel.

Ensuite, chaque fois que l'état du composant change (par exemple, `setState` est appelé), la méthode de rendu du composant est appelée et un nouveau `virtual DOM` est créé, et ce nouveau `virtual DOM` est comparé avec le `virtual DOM` précédent. Le résultat de cette comparaison est de montrer les changements réels du `DOM` et le `DOM` sera "patché" avec les changements et l'écran changera.

> Les informations sur le modèle de voiture ne changent pas encore avec la vitesse et la température. Cela sera finalement implémenté plus tard.

### 11. Contrôles de Climatisation et de Chauffage

Nous surveillons la température et changeons le `chauffage` en `climatisation` lorsqu'elle est supérieure à 20 degrés, et en `chauffage` lorsqu'elle est inférieure à 20 degrés.

Tout d'abord, créez un répertoire `src/components/TeslaClimate`, créez un fichier `TeslaClimate.js` dans celui-ci, et entrez le code suivant :

```
import React from 'react';
import './TeslaClimate.css';
```

```
const TeslaClimate = (props) => (
  <div className="tesla-climate">
    <label
      className={`tesla-climate__item ${props.value ? 'tesla-climate__item--active' : '' }  ${!props.limit ? 'tesla-heat':''}`}
    >
      <p>{props.limit ? 'ac' : 'heat'} {props.value ? 'on' : 'off'}</p>
      <i className="tesla-climate__icon"></i>
      <input
        type="checkbox"
        name="climate"
        checked={props.value}
        onChange={() => {props.handleChangeClimate()}}
      />
    </label>
  </div>
);
```

```
TeslaClimate.propTypes = {
  value: React.PropTypes.bool,
  limit: React.PropTypes.bool,
  handleChangeClimate: React.PropTypes.func
}
```

```
export default TeslaClimate;
```

Ce composant change la classe de style selon la `props.value` passée, et change le texte selon `props.limit`.

`TeslaBattery` passe le rappel (`handleChangeClimate` dans ce cas) à `TeslaClimate`, qui est exécuté chaque fois que l'état doit être mis à jour. L'événement `onChange` peut être utilisé pour notifier l'événement. Le `callback` passé par `TeslaBattery` est appelé avec `setState()` pour mettre à jour son état et réafficher.

### 11.1 Style du Composant TeslaClimate

Créez un fichier `TeslaClimate.css` dans le répertoire `src/components/TeslaClimate` et spécifiez les styles suivants. Comme le code est long et omis ici, vérifions le [code source](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaClimate/TeslaClimate.css).

```
.tesla-climate {
  float: left;
}
.tesla-climate__item {
    cursor: pointer;
    display: block;
    width: 100px;
    height: 100px;
    border: 6px solid #f7f7f7;
    border-radius: 50%;
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.3);
    color: #666;
    background: #fff;
}
...
```

### 11.2 Importer le Composant TeslaClimate dans le Conteneur TeslaBattery

Maintenant, nous allons implémenter `callback` dans `TeslaBattery` et le passer au composant `TeslaClimate`.

Tout d'abord, ajoutez `import` pour utiliser le composant `TeslaClimate` dans `TeslaBattery.js`. Nous implémentons la fonction de rappel `handleChangeClimate()` et la lions dans `constructor()`. Ensuite, nous passons la fonction de rappel au composant `TeslaClimate` en tant que `props`.

```
...import TeslaClimate from '../components/TeslaClimate/TeslaClimate';
...constructor(props) {
  super(props);
  ...
  this.handleChangeClimate = this.handleChangeClimate.bind(this);
  ...
}
// Gestionnaire d'événements de clic pour la climatisation et le chauffage
handleChangeClimate() {
  const config = {...this.state.config};
  config['climate'] = !this.state.config.climate;
  this.setState({ config });
}
```

```
...<TeslaClimate
  value={this.state.config.climate}
  limit={this.state.config.temperature > 10}
  handleChangeClimate={this.handleChangeClimate}/>
  ...
```

Maintenant, la valeur de l'état change en fonction du changement de température, et lorsque la valeur modifiée est passée au composant `TeslaClimate`, la classe de style et le texte sont modifiés en fonction de la valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/O-n3pVztFgNz1nkaazxOS2wCkdpbub2AA4We)

### 12. Composant TeslaWheels

Enfin, créons le dernier composant `TeslaWheels`. Comme toujours, créez un répertoire `src/components/TeslaWheels`, créez un fichier `TeslaWheels` dans celui-ci, et entrez le code suivant.

```
import React from 'react';
import './TeslaWheels.css';
```

```
const LabelLists = (props) => {
  const value = props.wheels.value;
  const changeHandler = props.wheels.handleChangeWheels;
  const sizes = [19, 21];
  const LabelItems = sizes.map(size => (
    <label key={size} className={`tesla-wheels__item tesla-wheels__item--${size} ${value === size ? 'tesla-wheels__item--active' : '' }`}>
      <input
        type="radio"
        name="wheelsize"
        value={size}
        checked={value === size}
         onChange={() => {changeHandler(size)}} />
      <p>
        {size}"
      </p>
    </label>
     )
  );
  return (
    <div>
      {LabelItems}
    </div>
  );
}

const TeslaWheels = (props) => (
  <div className="tesla-wheels__component">
    <p className="tesla-wheels__title">Roues</p>
    <div className="tesla-wheels__container cf">
      <LabelLists wheels={props}/>
    </div>
  </div>
);

TeslaWheels.propTypes = {
  value: React.PropTypes.number,
  handleChangeWheels: React.PropTypes.func
}

export default TeslaWheels;
```

Notre implémentation ici est similaire à la conversion de l'objet tableau `props` en une liste dans le composant `TeslaStats`. Répétez le tableau `props.sizes` en utilisant la fonction `javascript map()`.

Pour chaque itération, il retourne les éléments `<label>` contenant la taille. Enfin, la liste `LabelItems` est construite dans le composant `TeslaWheels` et rendue.

Dans l'élément `<label>`, l'effet de l'animation de la roue est montré en changeant la classe selon la taille de la roue transmise.

### 12.1 Style du Composant TeslaWheels

Créez un fichier `TeslaWheels.css` dans le répertoire `src/components/TeslaWheels` et spécifiez les styles suivants. Comme le code est long et omis ici, vérifions le [code source](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaWheels/TeslaWheels.css).

```
.tesla-wheels__component {
  float: left;
  width: 355px;
}
.tesla-wheels__title {
  letter-spacing: 2px;
  font-size: 16px;
}
...
```

### 12.2 Importer le Composant TeslaWheels dans le Conteneur TeslaBattery

Enfin, implémentez `callback` dans `TeslaBattery` et passez-le au composant `TeslaWheels`.

Ajoutez `import` pour utiliser le composant `TeslaWheels` dans `TeslaBattery.js`. Nous implémentons ensuite la fonction de rappel `handleChangeWheels()` et la lions dans `constructor`. Ensuite, nous passons la fonction de rappel au composant `TeslaWheels` en tant que `props`.

```
...import TeslaWheels from '../components/TeslaWheels';
...constructor(props) {
    super(props);
    this.calculateStats = this.calculateStats.bind(this);
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
    this.handleChangeClimate = this.handleChangeClimate.bind(this);
    this.handleChangeWheels = this.handleChangeWheels.bind(this);
    this.statsUpdate = this.statsUpdate.bind(this);
...
handleChangeWheels(size) {
  const config = {...this.state.config};
  config['wheels'] = size;
  this.setState({ config });
}
...
<TeslaWheels
  value={this.state.config.wheels}
  handleChangeWheels={this.handleChangeWheels}/>
...
```

Le résultat de l'achèvement de l'animation des roues est le suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/RobRs9CaB7HHDMeL59VivOVicS1Tr0K9zrjB)

### 13. Mise à jour de l'état

Avons-nous enfin terminé ? Même si l'utilisateur change plusieurs valeurs de condition, la valeur de différence du modèle de véhicule ne change pas correctement.

Jusqu'à présent, nous n'avons mis à jour qu'une partie du statut de notre application chaque fois qu'un événement se produit.

```
this.setState({ config });
```

Maintenant, changeons l'état `carstats` chaque fois que la valeur de l'état de configuration change.

```
statsUpdate() {
  const carModels = ['60', '60D', '75', '75D', '90D', 'P100D'];
  // Récupérer les informations du modèle depuis BatteryService et calculer puis mettre à jour l'état
  this.setState({
  carstats: this.calculateStats(carModels, this.state.config)
  })
}
```

Maintenant, nous créons une fonction qui prend les `carModels` et la valeur d'état actuelle en entrées et reflète les `carStats` modifiés dans l'état de l'application et les passe à `this.setState` en tant que rappel.

En faisant cela, il est possible de mettre à jour l'objet `config` en premier dans `setState()`, qui fonctionne de manière asynchrone, et de rendre les `stats` modifiés à l'écran sur cette base.

```
this.setState({ config }, () => {this.statsUpdate()});
```

Cela complète toutes les pièces du puzzle. Le code complet pour TeslaBattery est :

```
import React from 'react';
import './TeslaBattery.css';
import TeslaNotice from '../components/TeslaNotice/TeslaNotice';
import TeslaCar from '../components/TeslaCar/TeslaCar';
import TeslaStats from '../components/TeslaStats/TeslaStats';
import TeslaCounter from '../components/TeslaCounter/TeslaCounter';
import TeslaClimate from '../components/TeslaClimate/TeslaClimate';
import TeslaWheels from '../components/TeslaWheels/TeslaWheels';
import { getModelData } from '../services/BatteryService';
```

```
class TeslaBattery extends React.Component {
  constructor(props) {
    super(props);
```

```
    this.calculateStats = this.calculateStats.bind(this);
    this.statsUpdate = this.statsUpdate.bind(this);
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
    this.updateCounterState = this.updateCounterState.bind(this);
    this.handleChangeClimate = this.handleChangeClimate.bind(this);
    this.handleChangeWheels = this.handleChangeWheels.bind(this);
```

```
    this.state = {
      carstats: [],
      config: {
        speed: 55,
        temperature: 20,
        climate: true,
        wheels: 19
      }
    }
  }
```

```
  calculateStats = (models, value) => {
    const dataModels = getModelData();
    return models.map(model => {
      const { speed, temperature, climate, wheels } = value;
      const miles = dataModels[model][wheels][climate ? 'on' : 'off'].speed[speed][temperature];
      return {
        model,
        miles
      };
    });
  }
```

```
  statsUpdate() {
    const carModels = ['60', '60D', '75', '75D', '90D', 'P100D'];
    // Récupérer les informations du modèle depuis BatteryService et calculer puis mettre à jour l'état
    this.setState({
      carstats: this.calculateStats(carModels, this.state.config)
    })
  }
```

```
  componentDidMount() {
    this.statsUpdate();
  }
```

```
  updateCounterState(title, newValue) {
    const config = { ...this.state.config };
    // mettre à jour l'état de la configuration avec la nouvelle valeur
    title === 'Speed' ? config['speed'] = newValue : config['temperature'] = newValue;
    // mettre à jour notre état
    this.setState({ config }, () => {this.statsUpdate()});
  }
```

```
  increment(e, title) {
    e.preventDefault();
    let currentValue, maxValue, step;
    const { speed, temperature } = this.props.counterDefaultVal;
    if (title === 'Speed') {
      currentValue = this.state.config.speed;
      maxValue = speed.max;
      step = speed.step;
    } else {
      currentValue = this.state.config.temperature;
      maxValue = temperature.max;
      step = temperature.step;
    }
```

```
    if (currentValue < maxValue) {
      const newValue = currentValue + step;
      this.updateCounterState(title, newValue);
    }
  }
```

```
  decrement(e, title) {
    e.preventDefault();
    let currentValue, minValue, step;
    const { speed, temperature } = this.props.counterDefaultVal;
    if (title === 'Speed') {
      currentValue = this.state.config.speed;
      minValue = speed.min;
      step = speed.step;
    } else {
      currentValue = this.state.config.temperature;
      minValue = temperature.min;
      step = temperature.step;
    }
```

```
    if (currentValue > minValue) {
      const newValue = currentValue - step;
      this.updateCounterState(title, newValue);
    }
  }
```

```
  // Gestionnaire d'événements de clic pour la climatisation et le chauffage
  handleChangeClimate() {
    const config = {...this.state.config};
    config['climate'] = !this.state.config.climate;
    this.setState({ config }, () => {this.statsUpdate()});
  }
```

```
  // Gestionnaire d'événements de clic pour les roues
  handleChangeWheels(size) {
    const config = {...this.state.config};
    config['wheels'] = size;
    this.setState({ config }, () => {this.statsUpdate()});
  }
  
```

```
  render() {
        const { config, carstats } = this.state;
    return (
      <form className="tesla-battery">
        <h1>Autonomie par charge</h1>
        <TeslaCar wheelsize={config.wheels} />
        <TeslaStats carstats={carstats} />
        <div className="tesla-controls cf">
          <TeslaCounter
            currentValue={this.state.config.speed}
            initValues={this.props.counterDefaultVal.speed}
            increment={this.increment}
            decrement={this.decrement}
          />
          <div className="tesla-climate-container cf">
            <TeslaCounter
              currentValue={this.state.config.temperature}
              initValues={this.props.counterDefaultVal.temperature}
              increment={this.increment}
              decrement={this.decrement}
            />
            <TeslaClimate
              value={this.state.config.climate}
              limit={this.state.config.temperature > 10}
              handleChangeClimate={this.handleChangeClimate}
            />
          </div>
          <TeslaWheels
            value={this.state.config.wheels}
            handleChangeWheels={this.handleChangeWheels}
          />
        </div>
        <TeslaNotice />
      </form>
    )
  }
}
```

```
export default TeslaBattery;
```

> Consultez le [code final du projet](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial)

### 14. Construction

Il est temps de construire notre application.

```
npm run build
```

Si la construction réussit, le dossier build sera créé dans notre répertoire de projet et le message suivant sera affiché.

![Image](https://cdn-media-1.freecodecamp.org/images/W02jWxxUeOGPU4OKDIs6palLSqDd5ActUNj1)

Maintenant, notre build est prêt à être déployé.

### 15. Déploiement

Avec des outils comme [Surge](http://surge.sh/), nous pouvons vraiment facilement déployer notre application construite.

`Surge` est une publication web simple et en une seule commande. Il publie HTML, CSS et JS gratuitement, sans quitter la ligne de commande.

Tout d'abord, installez l'outil avec `npm` et exécutez la commande `surge` dans le répertoire `build`.

```
$ npm install -global surge
$ cd build
$ surge
```

Si c'est la première fois que vous exécutez cette commande, vous devrez entrer votre email et votre mot de passe pour enregistrer un nouveau compte.

Le déploiement est terminé en un instant.

![Image](https://cdn-media-1.freecodecamp.org/images/l98jRmRZB19gq-TRo-IiWV9TDHm9QHmG8lkj)

Connectons-nous à notre projet déployé.

> [react-tesla-charge-calculator.surge.sh](http://react-tesla-charge-calculator.surge.sh/)

![Image](https://cdn-media-1.freecodecamp.org/images/l4vf5tJQ261AlVSnUkehVI4CyOS7FRcrjRKa)

### Conclusion

Dans cet article, nous avons appris quelques points sur la création de composants React et leur composition pour créer une application front-end en reconstruisant le `Calculateur d'autonomie de batterie de Tesla`. Si vous avez suivi jusqu'à présent, félicitations pour avoir mis en place une application React.

Dans le prochain volet, nous explorerons comment améliorer notre gestion d'état avec la bibliothèque `Redux`. En attendant, si vous avez des commentaires, des suggestions ou des corrections, n'hésitez pas à les poster dans la section des commentaires.

Merci pour vos retours à l'avance.