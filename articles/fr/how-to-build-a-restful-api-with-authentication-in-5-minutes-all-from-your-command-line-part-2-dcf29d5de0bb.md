---
title: Comment créer une API RESTful avec authentification en 5 minutes — tout depuis
  votre ligne de commande (partie 2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-17T14:37:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-restful-api-with-authentication-in-5-minutes-all-from-your-command-line-part-2-dcf29d5de0bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HPcs-cQJpiVbW3de-ZA-1A.png
tags:
- name: coding
  slug: coding
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment créer une API RESTful avec authentification en 5 minutes — tout
  depuis votre ligne de commande (partie 2)
seo_desc: 'By Niharika Singh

  I’ve created this tutorial based on popular demand. This tutorial is the second
  part of this article. So before proceeding further with this one, please ensure
  that you’ve completed Part 1 so that we are on the same page!

  In this tu...'
---

Par Niharika Singh

J'ai créé ce tutoriel en réponse à une demande populaire. Ce tutoriel est la deuxième partie de [cet](https://medium.freecodecamp.org/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca) article. Donc, avant de continuer avec celui-ci, assurez-vous d'avoir terminé la [Partie 1](https://medium.freecodecamp.org/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca) pour que nous soyons sur la même longueur d'onde !

Dans ce tutoriel, nous allons développer le frontend de notre application 'Restaurant-Menu' en utilisant la très célèbre bibliothèque ReactJS et nous utiliserons MongoDB comme base de données. Nous garderons cela simple en faisant une requête GET à l'API que nous avons créée dans la [Partie 1](https://medium.freecodecamp.org/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca) et en affichant les articles alimentaires sur le navigateur.

L'application web finale ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/IDsX-VQ3nDvpTeaVSqZCXcBpDeT9R-UhKHdh)

Êtes-vous excité ? Eh bien, je le suis !

![Image](https://cdn-media-1.freecodecamp.org/images/iEyJze1p4AbkDf1y02WnaEDZEXal5h9qEg5m)
_Source : [https://giphy.com/](https://giphy.com/gifs/doctor-who-emoji-whomoji-XA0jsAWaxrgOI" rel="noopener" target="_blank" title=")_

### D'abord, configurer l'environnement de développement

_Je suppose que vous avez déjà configuré l'environnement de développement comme décrit dans la [Partie 1](https://medium.freecodecamp.org/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca). De plus, cet article suppose une connaissance de base de la terminologie React et de la syntaxe ES2015._

1. **Installer React**

```
$ npm install -g create-react-app
```

Si vous êtes bloqué quelque part, [ici](https://codeburst.io/installing-reactjs-and-creating-your-first-application-d437706498ed) se trouve un très bon tutoriel pour commencer.

**2. Installer un éditeur de texte**

Dans la [Partie 1](https://medium.freecodecamp.org/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca), nous n'avons pas écrit de code, donc il n'y avait pas de "vrai" besoin d'utiliser un éditeur de texte. Dans cette partie, nous allons écrire beaucoup de code. Donc, vous pouvez utiliser votre éditeur de texte préféré ou mon éditeur de texte préféré.

[**Télécharger Visual Studio Code - Mac, Linux, Windows**](https://code.visualstudio.com/download)  
[_Visual Studio Code est gratuit et disponible sur votre plateforme préférée - Linux, macOS et Windows. Télécharger Visual Studio..._code.visualstudio.com](https://code.visualstudio.com/download)

**3. Robomongo**

Ceci est optionnel. Si vous souhaitez avoir une interface graphique pour votre base de données MongoDB, alors Robomongo est un outil essentiel. Personnellement, je l'adore.

[**Robo 3T - anciennement Robomongo - outil de gestion natif MongoDB (Interface d'administration)**](https://robomongo.org/)  
[_L'outil Robo 3T (anciennement Robomongo) a été acquis par 3T Software Labs, les créateurs du client MongoDB Studio..._robomongo.org](https://robomongo.org/)

#### Une petite modification dans le fichier serveur Loopback :

Par défaut, l'explorateur d'API Loopback est servi sur le port 3000, et coïncidemment, React est également servi sur le port 3000 par défaut. Ces deux ports **DOIVENT** être différents. Donc, je vais transférer l'explorateur d'API Loopback sur le port 8080.

Ouvrez donc `config.json` et apportez les modifications suivantes :

```json
{
  "restApiRoot": "/api",
  "host": "0.0.0.0",
  "port": 8080,
  "remoting": {
    "context": false,
    "rest": {
      "handleErrors": false,
      "normalizeHttpPath": false,
      "xml": false
    },
    "json": {
      "strict": false,
      "limit": "100kb"
    },
    "urlencoded": {
      "extended": true,
      "limit": "100kb"
    },
    "cors": false
  }
}

```

Cela garantira que React et les explorateurs d'API Loopback ne se heurteront pas.

### Étape 1 : Remplir votre base de données avec quelques plats

Les données que nous alimentons dans notre base de données apparaîtront dans notre application web React lorsque nous ferons une requête GET.

Il existe différentes façons de remplir les données. La plus appropriée serait d'utiliser l'explorateur d'API.

Pointez donc votre navigateur web vers [http://localhost:8080/explorer](http://localhost:8080/explorer) et faites une requête POST. Cette fois, j'ai modifié le schéma du modèle et ajouté 'picture' également pour que nous ayons une application attrayante.

Voici à quoi ressemble mon schéma :

```js
{ "name": "string", "price": 0, "picture": "string" }

```

J'ai fait 4 entrées ici :

```json
[
  {
    "name": "Lasagna",
    "price": 50,
    "picture": "https://www.thewholesomedish.com/wp-content/uploads/2018/07/Best-Lasagna-550.jpg",
    "id": "5c401174d3bf4ffe05b5d42b"
  },
  {
    "name": "Pizza",
    "price": 100,
    "picture": "https://www.tasteofhome.com/wp-content/uploads/2017/10/Chicken-Pizza_exps30800_FM143298B03_11_8bC_RMS-2.jpg",
    "id": "5c401678d3bf4ffe05b5d42c"
  },
  {
    "name": "Pasta",
    "price": 30,
    "picture": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/2/4/1/RX-FNM_030111-Lighten-Up-012_s4x3.jpg.rend.hgtvcom.616.462.suffix/1382539856907.jpeg",
    "id": "5c401698d3bf4ffe05b5d42d"
  },
  {
    "name": "French Fries",
    "price": 10,
    "picture": "https://shop.gerald.ph/content/images/thumbs/0003743_french-fries_340.jpeg",
    "id": "5c404b677199790b33f2e3a6"
  }
]

```

Vous pouvez faire autant d'entrées que vous le souhaitez avec les plats de votre choix !

Après avoir fait les entrées, vous pouvez les visualiser sur Robomongo.

![Image](https://cdn-media-1.freecodecamp.org/images/vYaxueDDNlnAfKH4dNTj7qpMZ35YeWtNy0XV)

### Étape 2 : Créer une application React

Utilisons `create-react-app` pour créer notre application web React.

```
$ create-react-app restaurant-app
```

J'ai nommé mon application `restaurant-app`.

Ensuite, `cd restaurant-app`.

Ensuite, exécutez l'application React avec `npm start`. Cela démarrera l'application web sur localhost:3000.

Vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/o0KOcdopwtJlhL5w6hopbvCONxFaaTtcq5KT)

### Étape 3 : Supprimer tous les fichiers dans le dossier `src`

Dans le code de base de React, supprimez les fichiers dans le dossier src. Nous allons écrire le code à partir de zéro.

### Étape 4 : Ajouter une bibliothèque CSS pour réduire certains maux de tête de conception

Dans ce projet, j'utilise Semantic UI. Vous êtes libre d'utiliser la bibliothèque que vous souhaitez.

Dans le dossier de notre projet React, ouvrez le fichier `index.html` et ajoutez une balise `link` n'importe où dans le `<head>`. Ajoutons donc le CDN de Semantic UI.

```html
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css"
/>

```

### Étape 5 : Créer Index.js et App.js

Créez un nouveau fichier dans le dossier `src` nommé `index.js`.

Créez un dossier nommé `Components` dans le dossier `src`. Créez un fichier nommé `App.js` dans `Components`.

![Image](https://cdn-media-1.freecodecamp.org/images/K3SuwqWjHxpyHWIAs690xU32Xu9c4s-lD2SB)
_Structure du répertoire_

#### Contenu de `App.js` :

```jsx
import React from "react";
class App extends React.Component {
  render() {
    return <div>App Component </div>;
  }
}

```

#### Contenu de Index.js :

```jsx
import React from "react";
import ReactDOM from "react-dom";
import App from "./Components/App";

ReactDOM.render(<App />, document.querySelector("#root"));

```

Maintenant, si vous pointez votre navigateur vers localhost:3000, vous devriez voir **App Component** écrit sur l'écran.

### Étape 6 : Installer Axios pour faire des appels API

Lancez votre terminal et installez Axios.

```
$ npm install --save axios
```

### Étape 7 : Faire des appels API

Nous devons apporter des modifications à `App.js`.

```jsx
import React from "react";
import axios from "axios";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: [],
      price: [],
      picture: [],
    };
  }
  
  componentDidMount = () => {
    axios
      .get("http://localhost:8080/api/dishes")
      .then((res) => {
        for (var i = 0; i < res.data.length; i++)
          this.setState({
            name: [...this.state.name, res.data[i].name],
            price: [...this.state.price, res.data[i].price],
            picture: [...this.state.picture, res.data[i].picture],
          });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  
  Style = {
    margin: "10px",
    padding: "10px",
  };
  
  render() {
    return (
      <div className="ui list" style={this.Style}>
        <h1> Menu du Restaurant de Niharika </h1>
        <div className="item">
          <img
            className="ui small rounded image"
            src={this.state.picture[0]}
            alt="lasagna"
          />
          <div className="content">
            <h1>
              <a className="header">{this.state.name[0]}</a>
            </h1>
            <div className="description">
              {" "}
              <h3> $ {this.state.price[0]} </h3> .{" "}
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;

```

Cela n'affichera que le nom, le prix et l'image de la première entrée. Pour simplifier les choses, nous allons créer un nouveau composant nommé `FoodItem` pour réduire le code dans `App.js`.

![Image](https://cdn-media-1.freecodecamp.org/images/d8f0GCZlcNtt11tCw3GzsZSUSivvIc6-i4ez)

### Étape 8 : Créer un composant FoodItem pour rendre d'autres plats

Dans le dossier `Components`, créez un fichier nommé `FoodItem.js`.

#### Contenu de FoodItem.js :

```jsx
import React from "react";

const FoodItem = (props) => {
  return (
    <div className="item">
      <img
        className="ui small rounded image"
        src={props.picture}
        alt="lasagna"
      />
      <div className="content">
        <h1>
          <a className="header">{props.name}</a>
        </h1>
        <div className="description">
          {" "}
          <h3> $ {props.price} </h3> .{" "}
        </div>
      </div>
    </div>
  );
};

export default FoodItem;

```

Le concept de props est utilisé ici.

Modifiez `App.js` :

```jsx
import React from "react";
import axios from "axios";
import FoodItem from "./FoodItem";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: [],
      price: [],
      picture: [],
    };
  }
  
  componentDidMount = () => {
    axios
      .get("http://localhost:8080/api/dishes")
      .then((res) => {
        for (var i = 0; i < res.data.length; i++)
          this.setState({
            name: [...this.state.name, res.data[i].name],
            price: [...this.state.price, res.data[i].price],
            picture: [...this.state.picture, res.data[i].picture],
          });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  
  Style = {
    margin: "10px",
    padding: "10px",
  };
  
  render() {
    return (
      <div className="ui list" style={this.Style}>
        <h1> Menu du Restaurant de Niharika </h1>
        <FoodItem
          picture={this.state.picture[0]}
          name={this.state.name[0]}
          price={this.state.price[0]}
        />
        <br />{" "}
        <FoodItem
          picture={this.state.picture[1]}
          name={this.state.name[1]}
          price={this.state.price[1]}
        />
        <br />
        <FoodItem
          picture={this.state.picture[2]}
          name={this.state.name[2]}
          price={this.state.price[2]}
        />
        <br />
        <FoodItem
          picture={this.state.picture[3]}
          name={this.state.name[3]}
          price={this.state.price[3]}
        />
      </div>
    );
  }
}

export default App;

```

Le résultat final devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/nR3G948HMYj2Cq23Ydd6hyyFHdO4gJXXmS3f)

#### Conclusion

Dans ce tutoriel, nous nous sommes uniquement concentrés sur la méthode GET. Nous pouvons même POSTER plus de plats depuis cette console et faire beaucoup plus de choses.

C'est tout pour l'instant !

J'espère que vous avez tenu jusqu'à la fin. Si vous avez aimé, merci de l'apprécier en applaudissant. Merci beaucoup ! ❤