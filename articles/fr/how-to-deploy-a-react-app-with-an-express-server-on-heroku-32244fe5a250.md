---
title: Comment déployer une application React avec un serveur Express sur Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-18T21:35:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-react-app-with-an-express-server-on-heroku-32244fe5a250
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j8DELPVuI_w8045sxmHQsA.png
tags:
- name: Express.js
  slug: expressjs
- name: Heroku
  slug: heroku
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: 'tech '
  slug: tech
seo_title: Comment déployer une application React avec un serveur Express sur Heroku
seo_desc: 'By Ashish Nandan Singh

  Hello, world! Recently I had to deploy a website to Heroku for one of the pieces
  of freelance work I was doing. I think this process may be somewhat difficult, and
  a detailed tutorial or article on how to do this should help. S...'
---

Par Ashish Nandan Singh

Bonjour le monde ! Récemment, j'ai dû déployer un site web sur Heroku pour l'un des travaux freelance que je faisais. Je pense que ce processus peut être quelque peu difficile, et un tutoriel ou un article détaillé sur la façon de le faire devrait aider. Donc, celui-ci va être très simple et, espérons-le, très court.

Nous allons commencer par créer une application Express, qui agira comme notre serveur. Une fois le serveur terminé, nous créerons une simple application create-react-app, connecterons le serveur avec le frontend et, enfin, déployerons le tout sur une plateforme d'hébergement telle que Heroku.

Avant d'aller plus loin, je veux que vous compreniez que dans le monde du développement web, presque tout est une question de préférence. Certains d'entre vous peuvent ne pas être d'accord sur certaines choses, vous pouvez continuer à faire les choses comme vous le souhaitez, et c'est tout à fait correct. Jusqu'au point où nous cassons l'application, je considère que tout est correct.

Commençons.

### Créer une application Node/Express

Commencez par créer un dossier pour le projet global. Ce dossier contiendra l'application côté client — notre application React dans ce cas. Naviguez jusqu'au répertoire dans votre terminal et tapez les commandes ci-dessous.

```
$ touch server.js$ npm init
```

La dernière commande du snippet ci-dessus vous guidera à travers certaines étapes et initialisera votre projet avec un fichier `package.json`. Si vous êtes totalement nouveau dans ce domaine, vous pouvez considérer ce fichier comme un registre où vous gardez la trace de toutes les dépendances que vous utiliserez tout au long du processus de construction de votre application.

Ensuite, maintenant que nous avons le fichier `package.json` prêt, nous pouvons commencer par ajouter notre dépendance pour le projet.

Ajout d'Express :

```
$ npm i -g express --save
```

Cela ajoutera Express comme une dépendance à votre package.json. Maintenant que nous avons cela, tout ce dont nous avons besoin est une dépendance supplémentaire et celle-ci est pour le rechargement à chaud de l'application chaque fois que nous apportons une modification au code :

```
$ npm i -g nodemon --save --dev
```

Cela ajoutera nodemon à l'application. Si vous souhaitez en savoir plus sur nodemon, vous pouvez consulter [ce](https://nodemon.io/) lien pour plus d'informations.

Maintenant que nous avons ajouté ces éléments, nous sommes prêts à créer notre serveur le plus basique dans Express. Voyons comment cela se fait.

```
const express = require('express');const app = express();const port = process.env.PORT || 5000;
```

```
//Configuration de la routeapp.get('/', (req, res) => {    res.send('route racine');
```

```
})
```

```
//Démarrer le serveurapp.listen(port, (req, res) => {
```

```
console.log(`serveur à l'écoute sur le port : ${port}`)
```

```
 });
```

C'est tout. Il suffit de naviguer vers le terminal, de s'assurer que vous êtes dans le répertoire racine du projet, et de taper :

```
$ nodemon <nom-du-fichier> (index.js/server.js)
```

Dans notre cas, puisque nous l'avons nommé `server.js`, ce serait `nodemon server.js`. Cela démarrera le serveur sur le port 5000 de votre ordinateur localement. Si vous allez visiter le navigateur et ouvrez [https://localhost:5000/](https://localhost:5000/) vous verrez le texte « route racine », ce qui signifie que le serveur a démarré. En cas de problème, n'hésitez pas à les ajouter dans les commentaires ci-dessous.

Maintenant que le serveur est configuré et fonctionne, procédons à la configuration de l'application React.

### Application React

```
$ npm i -g create-react-app$ create-react-app <nom-de-l-application>
```

Pour les besoins de ce tutoriel, nous nommerons l'application « client », donc notre commande ressemblera à ceci `create-react-app client`.

Une fois cela fait, la configuration prendra un certain temps et créera un joli petit dossier à l'intérieur de votre application principale avec le nom « client ».

Nous n'apporterons aucune modification majeure à l'application React globale pour l'instant — cela est hors du cadre de ce tutoriel.

Maintenant, le défi est que nous devons appeler et nous connecter à notre serveur qui s'exécute sur le localhost. Pour ce faire, nous devons effectuer un appel d'API.

#### Ajout d'un proxy

React nous donne la possibilité de le faire en ajoutant une valeur de proxy à notre fichier `package.json`. Naviguez jusqu'au fichier `package.json` dans votre répertoire et ajoutez le morceau de code ci-dessous.

```
"proxy": "http://localhost:5000",
```

Dans notre cas, le serveur s'exécute sur le port 5000, d'où le 5000 dans la valeur du proxy. La valeur peut varier si vous utilisez un port différent.

Maintenant, nous devons appeler les points de terminaison définis par Express, ou les points de terminaison de l'API, à partir de nos composants React. Ce que cela signifie vraiment, c'est que maintenant nous pouvons simplement appeler « api/users/all » depuis notre côté client, ce qui proxyfiera notre requête et cela ressemblera à ceci « https://localhost:5000/api/users/all ». Cela nous évite de faire une requête cross-origin, que la plupart des navigateurs modernes n'autorisent pas pour des raisons de sécurité.

Ensuite, nous apporterons quelques modifications au fichier `src/app.js`.

```
import React, { Component } from 'react';import './App.css';import Navbar from './Components/Layout/Navbar';import { BrowserRouter as Router, Route } from 'react-router-dom';import Footer from './Components/Layout/Footer';import Home from './Components/Layout/Home';import Social from './Components/social/Social';
```

```
class App extends Component {  constructor(props) {    super(props);    this.state = {}    this.connecToServer = this.connecToServer.bind(this);  }
```

```
  connecToServer() {    fetch('/');  }
```

```
  componentDidMount() {    this.connecToServer();  }
```

```
  render() {    return (      <Router>      <div className="container">         <Navbar />         <Route exact path="/" component={Home} />         <Route exact path="/social" component={Social} />         <Footer />      </div>      </Router>    );  }}
```

```
export default App;
```

Ce que nous avons fait, c'est créer un constructeur, et lier la valeur de this dans notre fonction qui effectuera l'appel d'API fetch. Ensuite, nous appelons la fonction dès que le composant est monté. Ensuite, nous avons la fonction render qui contient le balisage global pour l'application. Donc, c'était la dernière modification que nous ferons dans React ou notre application frontend.

Votre fichier `package.json` devrait ressembler au snippet de code ci-dessous.

```
{  "name": "nom-du-projet",  "version": "0.1.0",  "private": true,  "dependencies": {    "react": "^16.6.3",    "react-dom": "^16.6.3",    "react-scripts": "2.1.1",    "react-router-dom": "^4.3.1"  },
```

```
  "scripts": {    "start": "react-scripts start",    "build": "react-scripts build",    "test": "react-scripts test",    "eject": "react-scripts eject"  },
```

```
  "eslintConfig": {    "extends": "react-app"  },
```

```
  "proxy": "http://localhost:5000",
```

```
  "browserslist": [    ">0.2%",    "not dead",    "not ie <= 11",    "not op_mini all"  ]}
```

Maintenant, faisons une pause d'une minute et réfléchissons à ce que nous devons faire ensuite... des idées ?

Certains d'entre vous ont raison de penser que nous devons nous assurer que nos fichiers React sont servis par notre serveur Express. Apportons quelques modifications au fichier `server.js` pour nous assurer que les fichiers React sont servis par le serveur Express.

#### Modification du fichier serveur

```
const express = require('express');const app = express();const path = require('path');const port = process.env.PORT || 5000;
```

```
//Déclaration de fichier statiqueapp.use(express.static(path.join(__dirname, 'client/build')));
```

```
//mode productionif(process.env.NODE_ENV === 'production') {  app.use(express.static(path.join(__dirname, 'client/build')));  //  app.get('*', (req, res) => {    res.sendfile(path.join(__dirname = 'client/build/index.html'));  })}
```

```
//mode buildapp.get('*', (req, res) => {  res.sendFile(path.join(__dirname+'/client/public/index.html'));})
```

```
//démarrer le serveurapp.listen(port, (req, res) => {  console.log( `serveur à l'écoute sur le port : ${port}`);})
```

Dans le snippet de code ci-dessus, vous devez d'abord utiliser le module path intégré dans node et déclarer le dossier statique que vous souhaitez utiliser dans ce serveur Express.

Ensuite, vous vérifiez si le processus **est en production**, ce qui sera le cas une fois l'application déployée sur Heroku. Sous cette condition, vous souhaitez servir le fichier `index.html` à partir du dossier build **et non** du dossier public.

Si ce **n'est pas le mode production**, et que vous testez une fonctionnalité et que votre serveur s'exécute sur le localhost, vous souhaitez que le fichier `index.html` du dossier public soit servi.

Maintenant, nous devons nous assurer que nous démarrons d'abord notre serveur Express, puis nous nous occupons de démarrer notre serveur React. Il existe de nombreuses façons de faire cela, et pour la simplicité de ce tutoriel, nous utiliserons un module appelé `concurrently` pour exécuter les deux serveurs avec une seule commande.

Assurez-vous d'être dans le répertoire racine, puis exécutez la commande ci-dessous à partir de votre terminal.

```
npm i concurrently --save
```

Après avoir fait cela, apportons quelques modifications aux scripts que nous avons dans nos fichiers `package.json` du serveur Express.

```
"scripts": {    "client-install": "npm install --prefix client",    "start": "node index.js",    "server": "nodemon index.js",    "client": "npm start --prefix client",    "dev": "concurrently \"npm run server\" \"npm run client\"",
```

```
}
```

* `npm run client-install` installera toutes les dépendances pour l'application React
* `npm start` démarrera le serveur et ne rechargera pas après avoir détecté un changement
* `npm run server` démarrera le serveur, écoutera les changements dans le code, et rechargera à chaud la page dans le navigateur pour refléter le changement.
* `npm run client` exécutera l'application React sans démarrer le serveur
* `npm run dev` exécutera simultanément le serveur puis exécutera le client sur votre navigateur

### Configuration de Heroku

Assurez-vous d'avoir un compte sur Heroku. Si vous n'en avez pas, vous pouvez en créer un rapidement en utilisant vos identifiants GitHub.

Ensuite, nous installerons l'interface de ligne de commande Heroku, qui nous aidera à déployer l'application directement depuis notre terminal. [Cliquez ici](https://devcenter.heroku.com/articles/heroku-cli) pour obtenir des instructions d'installation sur macOS et Windows.

```
$ heroku login
```

Entrez les identifiants de connexion pour Heroku, puis :

```
$ heroku create
```

Cela créera une application pour vous. Si vous visitez le tableau de bord Heroku maintenant, il contiendra l'application.

Maintenant, nous devons nous assurer que nous avons un dossier build dans notre projet avant de pousser le projet vers le dépôt Heroku. Ajoutez le script ci-dessous dans votre fichier `package.json`.

```
"scripts": {    "client-install": "npm install --prefix client",
```

```
    "start": "node server.js",
```

```
    "server": "nodemon server.js",
```

```
    "client": "npm start --prefix client",
```

```
    "dev": "concurrently \"npm run server\" \"npm run client\"",
```

```
    "heroku-postbuild":      "NPM_CONFIG_PRODUCTION=false npm install --prefix client        && npm run build --prefix client"  },
```

Après avoir fait cela, enregistrez le fichier et poussez l'ensemble du dépôt du projet vers la branche de votre application Heroku.

```
//ajouter une télécommande
```

```
$ heroku git:remote -a nom-de-l-application
```

```
$ git add .
```

```
$ git commit -am 'prêt à déployer'
```

```
$ git push heroku master
```

Et cela devrait être tout.

Une fois tout cela terminé, vous obtiendrez une URL pour votre projet hébergé en direct. Partagez et montrez ce que vous pouvez construire en utilisant ces technologies.

Si vous avez des questions ou des commentaires, n'hésitez pas à ajouter votre commentaire ou à vous connecter directement.

Github : [https://github.com/ashishcodes4](https://github.com/ashishcodes4)

Twitter : [https://twitter.com/ashishnandansin](https://twitter.com/ashishnandansin)

LinkedIn : [https://www.linkedin.com/in/ashish-nandan-singh-490987130/](https://www.linkedin.com/in/ashish-nandan-singh-490987130/)