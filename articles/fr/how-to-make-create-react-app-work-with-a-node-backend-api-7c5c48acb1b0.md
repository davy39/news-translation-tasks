---
title: Comment faire fonctionner create-react-app avec une API Back-end Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T00:17:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-create-react-app-work-with-a-node-backend-api-7c5c48acb1b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eo3-wlU7ny1XYqPk4i2Blw.jpeg
tags:
- name: create-react-app
  slug: create-react-app
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: React
  slug: react
seo_title: Comment faire fonctionner create-react-app avec une API Back-end Node
seo_desc: 'By Esau Silva

  This is a very common question among newer React developers, and one question I
  had when I was starting out with React and Node.js. In this short example I will
  show you how to make create-react-app work with Node.js and Express Back-en...'
---

Par Esau Silva

C'est une question très courante chez les nouveaux développeurs React, et une question que je me posais quand je commençais avec React et Node.js. Dans ce court exemple, je vais vous montrer comment faire fonctionner `create-react-app` avec un Back-end Node.js et Express.

#### create-react-app

Créez un projet en utilisant `create-react-app`.

```bash
npx create-react-app example-create-react-app-express
```

Créez un répertoire `/client` sous le répertoire `example-create-react-app-express` et déplacez tout le code boilerplate React créé par `create-react-app` dans ce nouveau répertoire client.

```bash
cd example-create-react-app-express
mkdir client
```

#### Le serveur Node Express

Créez un fichier `package.json` à l'intérieur du répertoire racine (`example-create-react-app-express`) et copiez le contenu suivant :

```json
{
  "name": "example-create-react-app-express",
  "version": "1.0.0",
  "scripts": {
    "client": "cd client && yarn start",
    "server": "nodemon server.js",
    "dev": "concurrently --kill-others-on-fail \"yarn server\" \"yarn client\""
  },
  "dependencies": {
    "body-parser": "^1.18.3",
    "express": "^4.16.4"
  },
  "devDependencies": {
    "concurrently": "^4.0.1"
  }
}
```

Notez que j'utilise `concurrently` pour exécuter l'application React et le serveur en même temps. Le drapeau `–kill-others-on-fail` tuera les autres processus si l'un d'eux se termine avec un code d'état non nul.

Installez `nodemon` globalement et les dépendances du serveur :

```bash
npm i nodemon -g
yarn
```

Créez un fichier `server.js` et copiez le contenu suivant :

```js
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/api/hello', (req, res) => {
  res.send({ express: 'Hello From Express' });
});

app.post('/api/world', (req, res) => {
  console.log(req.body);
  res.send(
    `I received your POST request. This is what you sent me: ${req.body.post}`,
  );
});

app.listen(port, () => console.log(`Listening on port ${port}`));
```

Il s'agit d'un simple serveur Express qui s'exécutera sur le port 5000 et aura deux routes API : `GET` - `/api/hello`, et `POST` - `/api/world`.

À ce stade, vous pouvez exécuter le serveur Express avec la commande suivante (toujours à l'intérieur du répertoire racine) :

```bash
node server.js
```

Naviguez maintenant vers [http://localhost:5000/api/hello](http://localhost:5000/api/hello), et vous obtiendrez ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/TPcEMDY475EhrLyGruM9uWQvM33ZKlDAl-cb)

Nous testerons la route `POST` une fois que nous aurons construit l'application React.

#### L'application React

Passez maintenant au répertoire `client` où se trouve notre application React.

Ajoutez la ligne suivante au fichier `package.json` créé par `create-react-app`.

```json
"proxy": "http://localhost:5000/"
```

La clé pour utiliser un serveur back-end Express avec un projet créé avec `create-react-app` est d'utiliser un proxy. Cela indique au serveur de développement Web-pack de relayer nos requêtes API vers notre serveur API, étant donné que notre serveur Express s'exécute sur `localhost:5000`.

Modifiez maintenant `./client/src/App.js` pour appeler notre Back-end API Express, les modifications sont en gras.

```js
import React, { Component } from 'react';

import logo from './logo.svg';

import './App.css';

class App extends Component {
  state = {
    response: '',
    post: '',
    responseToPost: '',
  };
  
  componentDidMount() {
    this.callApi()
      .then(res => this.setState({ response: res.express }))
      .catch(err => console.log(err));
  }
  
  callApi = async () => {
    const response = await fetch('/api/hello');
    const body = await response.json();
    if (response.status !== 200) throw Error(body.message);
    
    return body;
  };
  
  handleSubmit = async e => {
    e.preventDefault();
    const response = await fetch('/api/world', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ post: this.state.post }),
    });
    const body = await response.text();
    
    this.setState({ responseToPost: body });
  };
  
render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
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
        <p>{this.state.response}</p>
        <form onSubmit={this.handleSubmit}>
          <p>
            <strong>Post to Server:</strong>
          </p>
          <input
            type="text"
            value={this.state.post}
            onChange={e => this.setState({ post: e.target.value })}
          />
          <button type="submit">Submit</button>
        </form>
        <p>{this.state.responseToPost}</p>
      </div>
    );
  }
}

export default App;
```

Nous créons la méthode `callApi` pour interagir avec notre route API Express `GET`, puis nous appelons cette méthode dans `componentDidMount` et enfin nous définissons l'état sur la réponse de l'API, qui sera _Hello From Express_.

Notez que nous n'avons pas utilisé d'URL complète [http://localhost:5000/api/hello](http://localhost:5000/api/hello) pour appeler notre API, même si notre application React s'exécute sur un port différent (3000). C'est grâce à la ligne `**proxy**` que nous avons ajoutée au fichier `package.json` précédemment.

Nous avons un formulaire avec une seule entrée. Une fois soumis, il appelle `handleSubmit`, qui à son tour appelle notre route API Express `POST`, puis enregistre la réponse dans l'état et affiche un message à l'utilisateur : _I received your POST request. This is what you sent me: [message de l'entrée]_.

Ouvrez maintenant `./client/src/App.css` et modifiez la classe `.App-header` comme suit (modifications en gras)

```js
.App-header {
...
  min-height: 50%;
...
  padding-bottom: 10px;
}
```

### Exécution de l'application

_Si le serveur est toujours en cours d'exécution, arrêtez-le en appuyant sur Ctrl+C dans votre terminal._

Depuis le répertoire racine du projet, exécutez ce qui suit :

```bash
yarn dev
```

Cela lancera l'application React et exécutera le serveur en même temps.

Naviguez maintenant vers [http://localhost:3000](http://localhost:3000) et vous arriverez sur l'application React affichant le message provenant de notre route Express `GET`. Sympa ?!

![Image](https://cdn-media-1.freecodecamp.org/images/v3LAoDh50Yq4c60yOY69WpRwnZL2fRCIXfTs)
_Affichage de la route GET_

Maintenant, tapez quelque chose dans le champ de saisie et soumettez le formulaire, vous verrez la réponse de la route Express `POST` affichée juste en dessous du champ de saisie.

![Image](https://cdn-media-1.freecodecamp.org/images/NcLZDJaVE0g833Xrn8jM2G8e5f4LVVygt10O)
_Appel de la route POST_

Enfin, jetez un œil à votre terminal, vous verrez le message que nous avons envoyé depuis le client, car nous appelons `console.log` sur le corps de la requête dans la route Express `POST`.

![Image](https://cdn-media-1.freecodecamp.org/images/r43BMtm-aiA84Nxrin1eTHXi4YnnEX3SYzMM)
_Node_

### Déploiement en production sur Heroku

Ouvrez `server.js` et remplacez-le par le contenu suivant :

```js
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Appels API
app.get('/api/hello', (req, res) => {
  res.send({ express: 'Hello From Express' });
});

app.post('/api/world', (req, res) => {
  console.log(req.body);
  res.send(
    `I received your POST request. This is what you sent me: ${req.body.post}`,
  );
});

if (process.env.NODE_ENV === 'production') {
  // Servir tous les fichiers statiques
  app.use(express.static(path.join(__dirname, 'client/build')));
    
  // Gérer le routage React, renvoyer toutes les requêtes à l'application React
  app.get('*', function(req, res) {
    res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
  });
}

app.listen(port, () => console.log(`Listening on port ${port}`));
```

Ouvrez `./package.json` et ajoutez ce qui suit à l'entrée `scripts`

```json
"start": "node server.js",
"heroku-postbuild": "cd client && npm install && npm install --only=dev --no-shrinkwrap && npm run build"
```

Heroku exécutera le script `start` par défaut et cela servira notre application. Ensuite, nous voulons demander à Heroku de construire notre application client, nous le faisons avec le script `heroku-postbuild`.

Maintenant, rendez-vous sur [Heroku](https://www.heroku.com/) et connectez-vous (ou ouvrez un compte si vous n'en avez pas).

Créez une nouvelle application et donnez-lui un nom

![Image](https://cdn-media-1.freecodecamp.org/images/YSsjVCvWV0-uieTxyQG1TDLrDT4ZxjOTb4pP)
_Créer une nouvelle application sur Heroku_

Cliquez sur l'onglet **_Deploy_** et suivez les instructions de déploiement (qui, je pense, sont assez explicites, pas la peine de les reproduire ici ?)

![Image](https://cdn-media-1.freecodecamp.org/images/vFyFAdbumn-k-39zK9DFZLJ6oWS9vfflmH1N)
_Déployer une application sur Heroku_

Et voilà, vous pouvez ouvrir votre application en cliquant sur le bouton **_Open app_** dans le coin supérieur droit du tableau de bord Heroku de votre application.

Visitez l'application déployée pour ce tutoriel : [https://cra-express.herokuapp.com/](https://cra-express.herokuapp.com/)

#### Autres options de déploiement

J'écris sur d'autres options de déploiement ici :

* [Netlify](https://blog.bitsrc.io/react-production-deployment-part-1-netlify-703686631dd1)
* [Now](https://blog.bitsrc.io/react-production-deployment-part-2-now-c81657c700b7)
* [Heroku](https://blog.bitsrc.io/react-production-deployment-part-3-heroku-316319744885) (explication plus détaillée)

### Structure du projet

Voici la structure finale du projet.

![Image](https://cdn-media-1.freecodecamp.org/images/YSFfgasf0j6pDjUX5TgcGCW6b8m74M6DTnY9)

Obtenez le code complet sur le [répertoire GitHub](https://github.com/esausilva/example-create-react-app-express).

Merci de votre lecture et j'espère que vous avez apprécié. Pour toute question ou suggestion, faites-le moi savoir dans les commentaires ci-dessous !

Vous pouvez me suivre sur [Twitter](https://twitter.com/_esausilva), [GitHub](https://github.com/esausilva), [Medium](https://medium.com/@_esausilva/latest), [LinkedIn](https://www.linkedin.com/in/esausilva/) ou tous à la fois.

Cet article a été initialement publié sur mon [site web de blog personnel](https://esausilva.com/2017/11/14/how-to-use-create-react-app-with-a-node-express-backend-api/).

---

**<ins>Mise à jour 25/08/19 :</ins>** J'ai construit une application web de prière appelée « **My Quiet Time - A Prayer Journal** ». Si vous souhaitez rester informé, veuillez vous inscrire via le lien suivant : [http://b.link/mqt](http://b.link/mqt)  

L'application sortira avant la fin de l'année, j'ai de grands projets pour cette application. Pour voir quelques captures d'écran de maquettes, suivez le lien suivant : [http://pc.cd/Lpy7](http://pc.cd/Lpy7)

Mes DM sur [Twitter](https://twitter.com/_esausilva) sont ouverts si vous avez des questions concernant l'application ?