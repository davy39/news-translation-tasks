---
title: Comment déployer une application React sur Netlify qui lit depuis une feuille
  Google Sheet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T19:39:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-react-application-to-netlify-that-reads-from-a-google-sheet-97a015806c47
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cad7b740569d1a4ca9fb9.jpg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Comment déployer une application React sur Netlify qui lit depuis une feuille
  Google Sheet
seo_desc: 'By Sergiy Dybskiy

  In this tutorial, we’re going to cover how to connect to a spreadsheet hosted on
  Google, display that information inside a React application, and deploy it to Netlify.

  Skip to “The Setup” if you don’t care where the data will be com...'
---

Par Sergiy Dybskiy

Dans ce tutoriel, nous allons voir comment se connecter à une feuille de calcul hébergée sur Google, afficher ces informations dans une application React et la déployer sur Netlify.

Passez à « L'installation » si vous ne vous souciez pas de savoir d'où proviennent les données ou pourquoi j'ai choisi de construire cela. Je ne vous en voudrai pas, je vous le promets.

Pour l'instant, le résultat final ressemble à ceci, mais j'ajouterai bientôt plus de fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/B0fW0hCrk6UNfnyhZz49Wyigj8BSLWe6H-yN)
_Vous pouvez le trouver à [https://dougscore.netlify.com](https://dougscore.netlify.com" rel="noopener" target="_blank" title=")_

### Pourquoi

J'adore les voitures ? ?f3ce. Si vous êtes même légèrement intéressé par les voitures, vous avez probablement déjà trébuché sur la chaîne YouTube de Doug Demuro. Il passe en revue une large gamme de voitures, allant d'une Ferrari Enzo à 3 millions de dollars à une BMW Isetta à trois roues. Le format de Doug est un peu différent de la plupart des avis des utilisateurs. Ses vidéos d'environ 20 minutes ont trois points principaux :

* Particularités et fonctionnalités intéressantes : environ 70 % de la vidéo consiste à parler des particularités extérieures et intérieures de la voiture. Cela peut aller d'un paragraphe dans le manuel du propriétaire à une forme intéressante des feux de freinage.

![Image](https://cdn-media-1.freecodecamp.org/images/PRwgOYulrc9WjHVypGBsN84K-kMaZdTARG4W)
_Pas vraiment Doug, mais un chien heureux ?_

* Conduite : environ 20 % de la vidéo montre Doug prenant la voiture sur la route et faisant des grimaces lorsqu'il accélère. Il parle également du bruit intérieur, de la maniabilité, de la vitesse, etc.
* Le DougScore : Doug a créé une feuille de calcul avec toutes les voitures qu'il a jamais passées en revue (depuis la création du système de notation) et les a toutes classées en utilisant son propre système. Il est divisé en deux catégories :
  * Note du week-end : Essentiellement à quel point la voiture est amusante.
  * Note quotidienne : Essentiellement à quel point la voiture est pratique.

![Image](https://cdn-media-1.freecodecamp.org/images/2pf1-UBRO1QVYtj6hntKdeHSHpr077skCXkB)
_Je me demande si Doug lit tous ces commentaires_

![Image](https://cdn-media-1.freecodecamp.org/images/6Mmm4aJZrLSRGzfI3fimEpDhy0BraT31sylA)
_Ensuite, il trouvera une faute de frappe à la page 73_

C'est pourquoi, à mon avis, il peut obtenir plus de 1,5 million de vues sur une vidéo de 25 minutes d'un monospace ??f3ce. Comme les vidéos sont si particulières, et que Doug lui-même est assez particulier aussi, ses followers ont inventé des commentaires créatifs. Mes préférés sont les remarques « Doug est le genre de gars à... », comme celles ci-dessus.

Et maintenant, à tous ceux qui sont restés après cette introduction qui n'a rien à voir avec la construction d'une application, l'API Google Sheets ou React, voici ce dont je parle.

### L'installation

Doug garde sa feuille de calcul sur Google Sheets, et toute personne ayant le lien peut y accéder. Pour moi, c'était difficile à naviguer. J'ai donc décidé de voir s'il y avait un moyen de l'étendre et d'ajouter quelques fonctionnalités supplémentaires.

#### React Create App

Le modèle React de Facebook nous permettra de démarrer assez rapidement sans avoir besoin de configurer des backends. Dans votre terminal de choix (Hyper pour moi), allez-y et entrez :

```
npx create-react-app doug-score
cd doug-score
yarn start
```

(Ou `npm start`, comme vous préférez, mais j'utiliserai yarn.)

Ouvrez le dossier dans votre éditeur de choix (VS Code pour moi) et allez dans `App.js`. Nous allons créer un composant séparé appelé `CarList`, le mettre dans un dossier `components` et l'ajouter à `App`.

```js
import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import CarList from "./components/CarList";
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <CarList />
      </div>
    );
  }
}
export default App;
```

Pour l'instant, voici à quoi ressemblera le composant CarList :

```js
import React, { Component } from 'react';
class CarList extends Component {
  render() {
    return (
      <div>
        This will be the car list
      </div>
    );
  }
}
```

#### API Google Sheets

Allons-y et créons un nouveau projet sur Google. Je l'ai appelé `doug-score`. Une fois créé, dans la boîte des API, cliquez sur « Aller à l'aperçu des API ». Une fois que vous cliquez sur « Activer les API et services », vous serez présenté à la bibliothèque d'API. Nous allons chercher « Google Sheets API ». Une fois que vous cliquez dessus, cliquez sur « Activer », et après le traitement, vous devriez voir cette page.

![Image](https://cdn-media-1.freecodecamp.org/images/XmCCcDJkZbQM7lLZLE1F6V25c2CwRtKvpEEt)
_Tableau de bord des API Google_

Dans la barre latérale, allez dans « Identifiants », cliquez sur le bouton « Créer des identifiants » et sélectionnez « Clé API ». Cliquez sur « Restreindre la clé » et donnez-lui un nom (je l'ai appelé « DougScore »). Sous « Restrictions d'application », nous allons le définir sur « Référents HTTP » et ajouter `http://localhost:3000` pour l'instant. Sous « Restrictions d'API », sélectionnez « Google Sheets API » et enregistrez. Nous devrions être prêts de ce côté.

#### La connexion

Maintenant que nous avons une clé API, revenez au code de l'application et créez un nouveau fichier appelé `config.js`. Entrez votre clé API et l'ID de la feuille de calcul.

```js
export default {
  apiKey: "VOTRE_CLE_API",
  discoveryDocs: 
    ["https://sheets.googleapis.com/$discovery/rest?version=v4"],
  spreadsheetId: "1KTArYwDWrn52fnc7B12KvjRb6nmcEaU6gXYehWfsZSo"
};
```

Maintenant, nous aurons besoin de la bibliothèque Google API, donc nous utiliserons notre fichier `index.html` dans le dossier `public` après notre `<div id="root">`</div>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Contenu -->
  </head>
  <body>
    <noscript>
      Vous devez activer JavaScript pour exécuter cette application.
    </noscript>
    <div id="root"></div>
    <script src="https://apis.google.com/js/api.js"></script>
    <!-- Contenu -->
  </body>
</html>
```

Cela nous donnera accès à `window.gapi` que nous utiliserons pour nous connecter à l'API Sheets. Pour plus d'informations, consultez la documentation de Google.

### Les données

Maintenant que nous avons accès à l'API, établissons la connexion. Le meilleur endroit pour le faire serait dans le cycle de vie `componentDidMount` du composant `CarList` que nous avons créé précédemment. Allons-y.

```js
componentDidMount() {
  // 1. Chargez la bibliothèque cliente JavaScript.
  window.gapi.load("client", this.initClient);
}
```

`window.gapi.load` accepte un rappel, donc notre fonction `initClient` ressemble à ceci :

```js
initClient = () => {
  // 2. Initialisez la bibliothèque cliente JavaScript.
  window.gapi.client
    .init({
      apiKey: config.apiKey,
      // Votre clé API sera automatiquement ajoutée aux URL des documents de découverte.
      discoveryDocs: config.discoveryDocs
    })
    .then(() => {
    // 3. Initialisez et faites la demande à l'API.
    load(this.onLoad);
  });
};
```

Quelques éléments sont introduits ici. `config` provient du fichier `config.js` que nous avons créé précédemment, alors n'oubliez pas de faire `import config from "../config";` en haut du fichier `CarList.js`.

`load` est une fonction que nous allons créer maintenant. Elle sera responsable de la connexion à la bonne feuille de calcul, du formatage correct des données et de leur retour au composant dans le rappel `this.onLoad` (ou du retour d'une erreur si nous avons fait une erreur).

Je voulais séparer cette logique du composant pour garder les fichiers petits et assez lisibles. Créons un nouveau dossier appelé `helpers` dans `src` et mettons un fichier `spreadsheet.js` dedans.

```js
import config from "../config";
/**
 * Charge les voitures depuis la feuille de calcul
 * Obtenez les bonnes valeurs et attribuez-les.
 */
export function load(callback) {
  window.gapi.client.load("sheets", "v4", () => {
    window.gapi.client.sheets.spreadsheets.values
      .get({
        spreadsheetId: config.spreadsheetId,
        range: "Sheet1!A4:T"
      })
      .then(
        response => {
          const data = response.result.values;
const cars = data.map(car => ({
            year: car[0],
            make: car[1],
            model: car[2]
          })) || [];
callback({
            cars
          });
        },
        response => {
          callback(false, response.result.error);
        }
      );
  });
}
```

Ici, nous invoquons l'API sheets et obtenons les valeurs de la feuille de calcul en passant le `spreadsheetId` et la `range`. La promesse retourne deux réponses : une si des données sont présentes et une autre en cas d'erreur. Les valeurs de réponse sont un tableau de tableaux où chacun représente une ligne dans la feuille de calcul.

### L'affichage

Maintenant que nous avons des données dans le composant `CarList`, nous pouvons commencer à configurer l'affichage. Dans la fonction `initClient`, nous avions la fonction `load(this.onLoad)`, alors reprenons là.

```js
onLoad = (data, error) => {
  if (data) {
    const cars = data.cars;
    this.setState({ cars });
  } else {
    this.setState({ error });
  }
};
```

Si la fonction `load` dans `spreadsheet.js` retourne des données, nous définissons l'état `cars` avec ces données. Sinon, nous définissons un état `error` pour montrer à nos utilisateurs que quelque chose a mal tourné.

#### État par défaut

Comme les données ne seront pas disponibles instantanément, nous devons définir un état par défaut pour notre composant.

```js
state = {
  cars: [],
  error: null
}
```

#### Rendu

Maintenant, dans la fonction `render`, nous pouvons afficher l'état :

```js
render() {
  const { cars, error } = this.state;
  if (error) {
    return <div>{this.state.error}</div>;
  }
  return (
    <ul>
      {cars.map((car, i) => (
        <li key={i}>
          {car.year} {car.make} {car.model}
        </li>
      ))}
    </ul>
  );
}
```

Ici, nous déstructurons l'état (ES6 FTW ??) et vérifions d'abord s'il y a une erreur. Si ce n'est pas le cas, nous parcourons les voitures et les affichons dans une liste non ordonnée.

![Image](https://cdn-media-1.freecodecamp.org/images/s4i4xPrmJ5iQs9yt7v2jNI4EcbTdZujHhtmb)

### Déploiement

Maintenant que nous avons notre superbe liste de voitures que Doug a passées en revue, nous pouvons la partager avec le monde. Comme il s'agira d'un site web statique, je vais le déployer sur Netlify en utilisant leur CLI. Pour cela, nous allons arrêter notre serveur local et exécuter les commandes suivantes :

```
yarn build
```

Cela créera un dossier `build` dans l'application qui sera prêt pour la production. Maintenant, tout ce que vous avez à faire est :

```
npm install netlify-cli -g
netlify deploy
```

Lorsque cela vous est demandé, assurez-vous de mettre `build` comme `Chemin à déployer ? (répertoire actuel)`.

Netlify va faire son travail et vous montrer l'URL finale (la mienne est [https://laughing-yonath-118f58.netlify.com](https://laughing-yonath-118f58.netlify.com/) ?)

Si vous essayez d'accéder à celle que vous avez créée, vous verrez une erreur dans votre console car votre URL n'a pas été ajoutée à la console Google API. Allez-y et ajoutez l'URL dont vous avez besoin, et après cela, tout devrait fonctionner comme prévu.

### La fin

J'espère que tout cela avait du sens. Vous pouvez maintenant travailler votre magie en ajoutant des fonctionnalités à cette liste telles que le tri, le filtrage, la pagination, la recherche, la comparaison, etc. Et lorsque Doug ajoutera une autre voiture à cette liste, l'application sera automatiquement mise à jour avec les nouvelles informations.

Si ce tutoriel vous a semblé clair, donnez-lui un ?? et partagez-le avec un ami. Si vous voulez me dire qu'il était nul ou si vous avez d'autres questions, commentez ci-dessous ou criez sur moi sur Twitter, je n'en ai vraiment pas l'esprit. Si Doug lit ceci, hey Doug ??!