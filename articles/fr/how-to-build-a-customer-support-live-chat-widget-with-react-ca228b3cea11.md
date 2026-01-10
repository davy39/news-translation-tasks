---
title: Comment créer un widget de chat en direct pour le support client avec React
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2019-03-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-customer-support-live-chat-widget-with-react-ca228b3cea11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dezdlu7b6juRGJAMukMwJQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer un widget de chat en direct pour le support client avec React
seo_desc: Live chat is a customer support method with a proven record. It’s fast and
  efficient since one agent can help many customers at once. Best of all, the quicker
  you can answer customer’s questions during the buying process, the more likely that
  person ...
---

Le chat en direct est une méthode de support client avec un bilan éprouvé. Il est rapide et efficace puisque un agent peut aider de nombreux clients à la fois. Le plus important, plus vous pouvez répondre rapidement aux questions des clients pendant le processus d'achat, plus cette personne est susceptible d'acheter.

Alors, comment intégrer un chat en direct dans votre application React ?

Dans ce tutoriel, je vais vous montrer comment intégrer une fonctionnalité de chat en direct dans votre application React sans vous soucier de maintenir votre propre serveur et architecture de chat.

Voici un aperçu de ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/nkdiOYtSzmINCDBH6JIuM5CvvnVPA50JduwO)

Pour alimenter notre application de chat, nous allons utiliser CometChat Pro.

CometChat Pro est une puissante API de communication qui vous permet d'ajouter des fonctionnalités de chat à votre application. Avec des intégrations faciles et une documentation claire, vous pourrez ajouter une fonctionnalité de chat en direct à votre application avec seulement quelques lignes de code, comme vous le verrez bientôt. Si vous souhaitez suivre ce tutoriel, vous pouvez créer un compte gratuit [ici](https://www.cometchat.com/pro).

En plus de CometChat, nous utiliserons les technologies suivantes :

* [Create React App](https://github.com/facebook/create-react-app)
* [react-chat-widget](https://github.com/Wolox/react-chat-widget)
* [Express](https://expressjs.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Axios](https://github.com/axios/axios)
* [react-md](https://react-md.mlaursen.com/) (composant spinner uniquement)

Je vous encourage à suivre ce tutoriel, mais si vous préférez passer directement au code, vous pouvez trouver le code complet de cette application sur [GitHub](https://github.com/cometchat-pro-samples/react-customer-support-live-widget).

### Premières étapes, créez votre application [CometChat](https://cometchat.com/pro)

Pour alimenter votre application de chat, vous utiliserez CometChat. Cependant, avant de pouvoir intégrer CometChat, vous devez d'abord créer une application CometChat.

Pour créer une application CometChat, allez sur le tableau de bord CometChat (si vous n'avez pas encore de compte CometChat gratuit, c'est le bon moment pour [vous inscrire](http://app.cometchat.com/)) et cliquez sur l'icône +.

J'ai appelé mon application "react-chat-widget" mais vous pouvez l'appeler comme vous le souhaitez.

Nous aurons deux types d'utilisateurs connectés à notre chat : les clients qui ouvrent le widget de chat et un agent de support qui accédera au chat et répondra aux demandes depuis le tableau de bord. Les utilisateurs sont un concept fondamental dans CometChat, que vous pouvez lire plus en détail [ici](https://prodocs.cometchat.com/docs/concepts#section-users).

Parce que nous aurons probablement de nombreux clients, pour chaque client qui se connecte à notre chat, nous devrons créer dynamiquement un utilisateur CometChat. Cependant, comme il n'y aura qu'un seul agent, nous pouvons créer un utilisateur "Agent" à l'avance depuis le tableau de bord.

Pour ce faire, cliquez sur Explorer puis allez dans l'onglet Utilisateurs. Ici, vous pouvez cliquer sur Créer un utilisateur :

![Image](https://cdn-media-1.freecodecamp.org/images/c20REaOyoYFEzfzz3K5JcIfxehKYXuGczwgn)

Pour l'ID de l'utilisateur, j'ai écrit "ecommerce-agent" et pour le nom, j'ai écrit "Demo Agent". Je vous recommande d'utiliser les mêmes valeurs si vous suivez ce tutoriel. Dans tous les cas, notez l'ID de l'utilisateur car vous devrez vous y référer plus tard.

Avant de quitter le tableau de bord et de passer au code, nous devons créer une clé d'accès complet CometChat.

Sur la même page, cliquez sur l'onglet Clés API puis sur Créer une clé API :

![Image](https://cdn-media-1.freecodecamp.org/images/XZ6MX86rfV24YbJOfeeGzcs5mDF8ejr22rwJ)

![Image](https://cdn-media-1.freecodecamp.org/images/624wwWHoFZg6LPsyw0i37TcHqgYC9CHIrr7C)

J'ai appelé ma clé "react-chat-api" mais cela n'a pas vraiment d'importance ce que vous écrivez ici.

Notez votre clé API et votre ID d'application car, comme l'ID de l'utilisateur agent, vous en aurez besoin plus tard.

### Configuration d'Express

Dans l'étape précédente, nous avons créé une clé d'accès complet, que nous pouvons utiliser pour créer des utilisateurs CometChat dynamiquement. Bien que nous puissions le faire sur le client, cela signifierait partager notre clé d'accès complet privée en public, ce qui est à éviter.

Pour éviter ce problème, nous allons créer un simple serveur Express qui :

1. Crée un utilisateur CometChat en utilisant la clé d'accès complet
2. Retourne des jetons d'authentification (nous en parlerons plus tard)
3. Retourne une liste d'utilisateurs CometChat, pour une utilisation ultérieure dans le tableau de bord

Très bien, commençons.

Tout d'abord, créez un nouveau répertoire vide pour votre application Express et exécutez `npm init -y` :

```
mkdir react-express-chat-widget
cd react-express-chat-widget
npm init -y
```

Ensuite, installez Express et axios :

```
npm install express axios
```

Puis, dans un fichier appelé `server.js`, collez :

```js
const express = require('express');
const axios = require('axios');
const app = express();

// entrer les configurations CometChat Pro ici
const appID = '{appID}';
const apiKey = '{apiKey}';
const agentUID = '{agentUID}';

const url = 'https://api.cometchat.com/v1';

const headers = {
  'Content-Type': 'application/json',
  appid: appID,
  apikey: apiKey,
};
```

Dans le fichier ci-dessus, nous :

1. Stockez les informations d'identification de notre application et l'ID de l'utilisateur agent, que nous avons créés précédemment
2. Définissons l'URL de l'API CometChat pour un accès pratique
3. Créons un objet `headers` avec notre `appID` et `apiKey`. Nous enverrons cet en-tête avec chaque requête à CometChat

Dans le même fichier, définissons maintenant une route pour gérer la création de nouveaux utilisateurs CometChat.

Pour créer un nouvel utilisateur, nous devons envoyer une requête POST avec l'UID et le nom de l'utilisateur.

Dans ce tutoriel, nous allons coder en dur le même nom pour tous les clients — nous appellerons chaque client "customer" — mais l'UID doit être unique. Pour l'UID, nous pouvons utiliser `new Date().getTime()` pour générer un ID aléatoire.

Ajoutez le code suivant à `server.js` :

```js
app.get('/api/create', (req, res) => {
  // données pour le nouvel utilisateur
  const data = {
  // vous pouvez utiliser votre propre logique pour générer un UID et un nom aléatoires
  // seul l'uid doit être unique
    uid: new Date().getTime(),
    name: 'customer',
  };
  axios
    .post(`${url}/users`, JSON.stringify(data), {
      headers,
    })
    .then(response => { 
    // l'utilisateur est créé, récupérer le jeton d'authentification
      requestAuthToken(response.data.data.uid)
        .then(token => {
          console.log('Succès:' + JSON.stringify(token));
          // le jeton est retourné au client
          res.json(token); 
        })
        .catch(error => console.error('Erreur:', error));
    })
    .catch(error => console.error('Erreur:', error));
});

// cette fonction récupérera le jeton
const requestAuthToken = uid => {
  return new Promise((resolve, reject) => {
    axios
      .post(`${url}/users/${uid}/auth_tokens`, null, {
        headers,
      })
      .then(response => {
        console.log('Nouveau jeton d\'authentification:', response.data);
        resolve(response.data.data);
      })
      .catch(error => reject(error));
  });
};
```

Lorsque cette route est appelée, Express va :

* Envoyer une requête POST à [https://api.cometchat.com/v1/users/](http://api.cometchat.com/v1/users) avec les `headers` corrects et les informations sur le nouvel utilisateur
* Récupérer un jeton d'authentification pour le nouvel utilisateur
* Et, enfin, le retourner à l'appelant

Nous avons également créé une fonction appelée `requestAuthToken` pour aider à récupérer le jeton d'authentification.

Ensuite, dans le même fichier, créons une route d'authentification que nous pouvons appeler pour créer des jetons pour les utilisateurs de retour :

```js
//...

app.get('/api/auth', (req, res) => {
  const uid = req.query.uid;
  // si vous avez votre propre méthode de connexion, appelez-la ici.
  // puis appelez CometChat pour le jeton d'authentification
  requestAuthToken(uid)
    .then(token => {
      console.log('Succès:' + JSON.stringify(token));
      res.json(token);
    })
    .catch(error => console.error('Erreur:', error));
});

//...
```

Enfin, créons une fonction pour retourner une liste d'utilisateurs, à l'exclusion de l'agent.

Nous appellerons ce point de terminaison depuis le tableau de bord plus tard pour afficher une liste d'utilisateurs avec lesquels l'agent peut discuter (bien sûr, l'agent ne veut pas discuter avec lui-même, nous le filtrons donc de la liste) :

```js
//...

app.get('/api/users', (req, res) => {
  axios
    .get(`${url}/users`, {
      headers,
    })
    .then(response => {
      const { data } = response.data;
      const filterAgentData = data.filter(data => {
      // filtrer l'agent de la liste des utilisateurs
        return data.uid !== agentUID;
      });
      res.json(filterAgentData);
    })
    .catch(error => console.error('Erreur:', error));
});
//...
```

Tout en bas de `server.js`, exécutez le serveur :

```js
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Écoute sur le port ${PORT}`);
});
```

Si vous avez suivi jusqu'à présent, voici à quoi devrait ressembler `server.js` :

```js
const express = require('express');
const axios = require('axios');
const app = express();

const appID = '{appID}';
const apiKey = '{apiKey}';
const agentUID = '{agentUID}';

const url = 'https://api.cometchat.com/v1';

const headers = {
  'Content-Type': 'application/json',
  appid: appID,
  apikey: apiKey,
};

app.get('/api/create', (req, res) => {
  const data = {
    uid: new Date().getTime(),
    name: 'customer',
  };
  axios
    .post(`${url}/users`, JSON.stringify(data), {
      headers,
    })
    .then(response => {
      requestAuthToken(response.data.data.uid)
        .then(token => {
          console.log('Succès:' + JSON.stringify(token));
          res.json(token);
        })
        .catch(error => console.error('Erreur:', error));
    })
    .catch(error => console.error('Erreur:', error));
});

app.get('/api/auth', (req, res) => {
  const uid = req.query.uid;
  requestAuthToken(uid)
    .then(token => {
      console.log('Succès:' + JSON.stringify(token));
      res.json(token);
    })
    .catch(error => console.error('Erreur:', error));
});

const requestAuthToken = uid => {
  return new Promise((resolve, reject) => {
    axios
      .post(`${url}/users/${uid}/auth_tokens`, null, {
        headers,
      })
      .then(response => {
        console.log('Nouveau jeton d\'authentification:', response.data);
        resolve(response.data.data);
      })
      .catch(error => reject(error));
  });
};

app.get('/api/users', (req, res) => {
  axios
    .get(`${url}/users`, {
      headers,
    })
    .then(response => {
      const { data } = response.data;
      const filterAgentData = data.filter(data => {
        return data.uid !== agentUID;
      });
      res.json(filterAgentData);
    })
    .catch(error => console.error('Erreur:', error));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Écoute sur le port ${PORT}`);
});
```

Dans une fenêtre de terminal, exécutez `node server.js` et recherchez un message indiquant "Écoute sur le port 5000". Ce serait un bon moment pour tester les points de terminaison avec curl ou [Postman](https://www.getpostman.com/) mais nous allons faire confiance et passer à la partie client.

### Configuration de l'application React

À l'intérieur de votre répertoire, exécutez `npx create-react-app` pour créer une nouvelle application React :

```
npx create-react-app client
```

Votre structure de dossiers devrait ressembler à ceci :

```js
|-- express-react-chat-widget
    |-- package-lock.json
    |-- package.json
    |-- server.js
    |-- client
        |-- .gitignore
        |-- package-lock.json
        |-- package.json
        |-- public
        |-- src
```

Avec votre application React en place, naviguez vers le répertoire `client` et installez les modules suivants :

```
cd client
npm install @cometchat-pro/chat react-chat-widget react-router-dom bootstrap react-md-spinner
```

Create React App est vraiment utile pour démarrer une application React, mais il génère également beaucoup de fichiers dont nous n'avons pas besoin (fichiers de test, etc.).

Avant de plonger dans le code, supprimez tout dans le répertoire `client/src` - nous allons partir de zéro.

Pour commencer, créez un fichier `config.js` avec votre ID d'application et l'UID de l'agent à l'intérieur :

```js
// client/src/config.js
const config = {
  appID: '{appID}',
  agentUID: '{agentUID}',
}
export default config;
```

C'est un peu de code standard que nous pouvons utiliser pour référencer nos identifiants CometChat depuis n'importe où.

Pendant que nous traitons du code standard, profitons-en également pour créer un fichier `index.css` :

```css
body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
    "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
    
code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New", monospace;
}
    
.message {
  overflow: hidden;
}
    
.balon1 {
  float: right;
  background: #35cce6;
  border-radius: 10px;
}
    
.balon2 {
  float: left;
  background: #f4f7f9;
  border-radius: 10px;
}
```

Nous allons référencer cela plus tard depuis le tableau de bord.

Maintenant, dans un fichier appelé `index.js`, collez ce qui suit :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import App from './App';
import { CometChat } from '@cometchat-pro/chat';
import config from './config';

CometChat.init(config.appID)
ReactDOM.render(<App />, document.getElementById('root'));
```

Ici, nous importons Bootstrap, CometChat et le fichier de configuration que nous venons de créer avant d'initialiser CometChat et de rendre notre `App`.

Si vous suivez ce tutoriel, vous aurez remarqué que nous n'avons pas encore défini `App` - faisons cela maintenant.

Dans un fichier appelé `App.js` :

```js
import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Client from './Client';
import Agent from './Agent';

const App = () => {
  return (
    <Router>
      <React.Fragment>
        <ul>
          <li>
            <Link to='/'>Accueil Client</Link>
          </li>
          <li>
            <Link to='/agent'>Tableau de bord de l'Agent</Link>
          </li>
        </ul>
        <hr />
        <Route exact path='/' component={Client} />
        <Route path='/agent' component={Agent} />
      </React.Fragment>
    </Router>
  );
}
export default App;
```

Ici, nous définissons deux routes :

* La route `/` ou "Accueil Client" pour que le client discute avec l'agent
* Et la route `/agent` ou "Tableau de bord de l'Agent" pour un accès rapide et pratique au tableau de bord

Occupons-nous d'abord du composant client. Nous l'appellerons le composant client.

### Création du composant client

Notre composant client aura deux responsabilités principales :

1. Créer un nouvel utilisateur CometChat via notre serveur Express lorsqu'un client se connecte pour la première fois
2. Envoyer et recevoir des messages en temps réel.

Créez un fichier appelé `Client.js` et collez ce qui suit :

```
// Client.js

import React, {Component} from 'react';
import { Widget, addResponseMessage, addUserMessage, dropMessages } from 'react-chat-widget';
import { CometChat } from '@cometchat-pro/chat';
import config from './config';
import 'react-chat-widget/lib/styles.css';

const agentUID = config.agentUID;
const CUSTOMER_MESSAGE_LISTENER_KEY = "client-listener";
const limit = 30;

class Client extends Component {
  componentDidMount() {
    addResponseMessage('Bienvenue dans notre magasin !');
    addResponseMessage('Cherchez-vous quelque chose en particulier ?');
  }
 
  render() {
    return (
      <div className='App'>
        <Widget
          handleNewUserMessage={this.handleNewUserMessage}
          title='Mon Chat en Direct E-commerce'
          subtitle='Prêt à vous aider'
        />
      </div>
    );
  }
  
  createUser = async () => {
    const response = await fetch(`/api/create`)
    const result = await response.json()
    return result;
  }
    
  handleNewUserMessage = newMessage => {
    console.log(`Nouveau message entrant ! ${newMessage}`);
    var textMessage = new CometChat.TextMessage(
      agentUID,
      newMessage,
      CometChat.MESSAGE_TYPE.TEXT,
      CometChat.RECEIVER_TYPE.USER
    );
    let uid = localStorage.getItem("cc-uid");
    if (uid === null) {
    // pas d'uid, créer un utilisateur
      this.createUser().then(
        result => {
          console.log('jeton d\'authentification récupéré', result);
          localStorage.setItem("cc-uid",result.uid)
          // faire la connexion
          CometChat.login(result.authToken)
          .then(user => {
            console.log("Connexion réussie:", { user });
            CometChat.sendMessage(textMessage).then(
              message => {
                console.log('Message envoyé avec succès:', message);
              },
              error => {
                console.log('Échec de l\'envoi du message avec erreur:', error);
              }
            );
            // créer un écouteur
            CometChat.addMessageListener(
              CUSTOMER_MESSAGE_LISTENER_KEY,
              new CometChat.MessageListener({
                onTextMessageReceived: message => {
                  console.log("Journal des messages entrants", { message });
                  addResponseMessage(message.text);
                }
              })
            );
          })
      },
      error => {
        console.log('Échec de l\'initialisation avec erreur:', error);
      })
    } else {
      // nous avons un uid, envoyer
      CometChat.sendMessage(textMessage).then(
        message => {
          console.log('Message envoyé avec succès:', message);
        },
        error => {
          console.log('Échec de l\'envoi du message avec erreur:', error);
        }
      );
    }
  };
  componentWillUnmount() {
    CometChat.removeMessageListener(CUSTOMER_MESSAGE_LISTENER_KEY);
    CometChat.logout();
    dropMessages();
  }
}

export default Client;
```

Woah, c'est beaucoup de nouveau code. Décomposons-le.

La fonction `render` est assez simple, elle consiste principalement à rendre le [react-chat-widget](https://github.com/Wolox/react-chat-widget).

La majeure partie du code est dédiée à la gestion des nouveaux messages envoyés par le client dans la fonction appelée `handleNewUserMessage`.

En résumé, nous vérifions d'abord si l'UID du client existe dans le localStorage. Si c'est le cas, nous utiliserons cet UID pour connecter l'utilisateur et envoyer des messages. Sinon, nous appelons `createUser()` et utilisons la valeur retournée pour nous connecter. Cette fonction `createUser` appelle le point de terminaison que nous avons défini plus tôt dans le tutoriel.

Enfin, dans une fonction de cycle de vie React appelée `componentWillUnmount`, nous n'oublions pas de supprimer l'écouteur de messages.

Avant de continuer, voici un petit conseil : dans le code ci-dessus, au lieu de taper l'URL du serveur et le port (`"localhost:5000/users"` ou quelque chose comme ça) dans notre front-end, nous pouvons plutôt ajouter une option de [proxy](https://facebook.github.io/create-react-app/docs/proxying-api-requests-in-development) à `package.json`. Cela nous permettra d'écrire `/users"` au lieu de `//localhost:5000/users"` :

```
"browserslist": [
  ">0.2%",
  "not dead",
  "not ie <= 11",
  "not op_mini all"
],
"proxy": "http://localhost:5000"
```

Voici à quoi devrait ressembler l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/Mhun3ZqMeAdDcERDU0ZvUtty46PAwbcU6Ibm)

Comme vous pouvez le voir, vous pouvez envoyer et recevoir des messages, mais si nous actualisons notre page, tous les messages de chat disparaîtront et ce n'est pas bon.

Pour résoudre ce problème, nous allons configurer la méthode `componentDidMount` pour rechercher l'UID du client dans le `localStorage`, afin que lorsque les clients actualisent la page, ils puissent continuer à discuter là où ils se sont arrêtés.

Une fois trouvé, nous utiliserons cet UID pour initier une chaîne de méthodes pour [se connecter, récupérer les messages précédents](https://prodocs.cometchat.com/docs/js-messaging#section-fetch-previous-messages) et [créer un écouteur](https://prodocs.cometchat.com/docs/js-messaging#section-receive-messages) pour les messages entrants.

```
componentDidMount() {
  addResponseMessage('Bienvenue dans notre magasin !');
  addResponseMessage('Cherchez-vous quelque chose en particulier ?');
  
  let uid = localStorage.getItem("cc-uid");
  // vérifier l'uid, s'il existe alors obtenir le jeton d'authentification
 if ( uid !== null) {
   this.fetchAuthToken(uid).then(
     result => {
       console.log('jeton d\'authentification récupéré', result);
       // connexion SDK
       CometChat.login(result.authToken)
       .then( user => {
         console.log("Connexion réussie:", { user });
         // écouter les messages entrants et récupérer les messages précédents
         this.createMessageListener();
         this.fetchPreviousMessages();
         
      })
     },
     error => {
       console.log('Échec de l\'initialisation avec erreur:', error);
     }
   );
 }
}

// Les fonctions utilisées ci-dessus

fetchAuthToken = async uid => {
  const response = await fetch(`/api/auth?uid=${uid}`)
  const result = await response.json()
  return result;
}
  
createMessageListener = () => {
  CometChat.addMessageListener(
    CUSTOMER_MESSAGE_LISTENER_KEY,
    new CometChat.MessageListener({
      onTextMessageReceived: message => {
        console.log("Journal des messages entrants", { message });
        addResponseMessage(message.text);
      }
    })
  );
}

fetchPreviousMessages = () => {
  var messagesRequest = new CometChat.MessagesRequestBuilder()
  .setUID(agentUID)
  .setLimit(limit)
  .build();
  messagesRequest.fetchPrevious().then(
    messages => {
      console.log("Liste des messages récupérée:", messages);
      // ajouter les messages aux bulles de chat du widget
      messages.forEach( message => {
        if(message.receiver !== agentUID){
          addResponseMessage(message.text);
        } else {
          addUserMessage(message.text)
        }
      });
    },
    error => {
      console.log("Échec de la récupération des messages avec erreur:", error);
    }
  );
}
```

Maintenant, si nous actualisons notre page, l'application essaiera de se connecter à CometChat et de récupérer les messages précédents automatiquement en recherchant notre UID client dans le `localStorage`. Super !

Il y a encore un petit problème, cependant. Tel qu'il est maintenant, il n'y a toujours aucun moyen pour un agent de répondre aux messages des clients.

Nous allons résoudre ce problème en construisant le tableau de bord de l'agent, où notre agent peut voir et répondre aux messages de chat des clients.

Nous avons terminé avec le fichier `Client.js`, donc vous pouvez prendre un café avant de passer au codage du fichier `Agent.js` ☕

### Création du composant agent

La fonction principale du tableau de bord de l'agent est de récupérer tous les clients de CometChat Pro et d'afficher tout message entrant d'un nouveau client dans la liste de chat des clients pour que les agents puissent cliquer et répondre. La fonctionnalité principale est très similaire à celle du client :

![Image](https://cdn-media-1.freecodecamp.org/images/QzJMIoy0i7ve8IeeSsKPmxREgMAn6QocG7MQ)

Avec CometChat, vous pourriez facilement créer plusieurs agents, mais pour garder les choses simples et éviter la gestion des utilisateurs, nous n'avons qu'un seul agent, que nous avons créé précédemment.

Créez un composant appelé `Agent.js` et définissez l'état initial :

```js
import React, {Component} from 'react';
import {CometChat} from '@cometchat-pro/chat';
import MDSpinner from "react-md-spinner";
import config from './config';

const agentUID = config.agentUID;
const AGENT_MESSAGE_LISTENER_KEY = 'agent-listener'
const limit = 30;

class Agent extends Component {
  state = {
    customers: [],
    selectedCustomer: '',
    chat: [],
    chatIsLoading: false,
    customerIsLoading:true
  }
}
```

Dans le même fichier, créez une méthode `componentDidMount` :

```js
componentDidMount(){
  this.fetchAuthToken(agentUID).then(
    authToken => {
      console.log('jeton d\'authentification récupéré', authToken);
      CometChat.login(authToken)
      .then( user => {
        console.log("Connexion réussie:", { user });
        // après la connexion, récupérer tous les utilisateurs
        // les mettre dans l'état des clients
        this.fetchUsers().then(result => {
          this.setState({
            customers: result,
            customerIsLoading: false
          })
        });
        
        CometChat.addMessageListener(
          AGENT_MESSAGE_LISTENER_KEY,
          new CometChat.MessageListener({
            onTextMessageReceived: message => {
              let {customers, selectedCustomer, chat} = this.state;
              console.log("Journal des messages entrants", { message });
              // vérifier le message entrant
              // s'il provient du même client avec lequel l'agent discute actuellement
              // ajouter un nouvel élément de chat à l'état du chat
              if(selectedCustomer === message.sender.uid){
                chat.push(message);
                this.setState({
                  chat
                })
              } else {
              // si nouveau client, ajouter un nouveau client à l'état des clients
                let aRegisteredCustomer = customers.filter( customer => {
                 return customer.uid === message.sender.uid }); 
                if(!aRegisteredCustomer.length){
                  customers.push(message.sender)
                  this.setState({
                    customers
                  })
                }
              }
            }
          })
        );
     })
    },
    error => {
      console.log('Échec de l\'initialisation avec erreur:', error);
    }
  );
}

fetchUsers = async () => {
  const response = await fetch(`/api/users`)
  const result = await response.json()
  return result;
}
```

Il se passe beaucoup de choses dans le code ci-dessus, voici un résumé pour vous aider à comprendre :

1. Tout d'abord, nous connectons automatiquement notre agent et récupérons tous les utilisateurs avec lesquels l'agent peut discuter depuis le serveur
2. Ensuite, nous créons un écouteur de messages entrants. Chaque fois qu'un message est reçu dans la conversation sélectionnée, nous le poussons dans l'état du chat qui, à son tour, met à jour l'interface utilisateur
3. Si le message entrant ne provient pas de la conversation actuellement sélectionnée, nous vérifions s'il s'agit d'un nouveau message d'un client enregistré. Si ce n'est pas le cas, nous poussons ce nouveau client dans l'état des clients.

Vous reconnaîtrez probablement l'API Express que nous avons créée pour obtenir une liste des utilisateurs enregistrés. Nous l'utilisons pour remplir la liste des utilisateurs sur le côté gauche du tableau de bord. Nous positionnerons la liste sur le côté gauche à l'aide d'une combinaison de classes Bootstrap et du fichier `index.css` que nous avons défini précédemment.

Ensuite, créons la fonction de rendu. Elle rendra une interface de conversation, stylisée avec Bootstrap. Pour faciliter le suivi du code, nous allons séparer `CustomerList` et `ChatBox` en leurs propres composants, que vous pouvez définir dans le même fichier :

```js
render() {
  return(
    <div className='container-fluid'>
      <div className='row'>
        <div className='col-md-2'></div>
        <div className="col-md-8 h-100pr border rounded">
          <div className='row'>
            <div className='col-lg-4 col-xs-12 bg-light' style={{ height: 658 }}>
            <div className='row p-3'><h2>Liste des Clients</h2></div>
            <div className='row ml-0 mr-0 h-75 bg-white border rounded' 
            style={{ height: '100%', overflow:'auto' }}>
            {/* Le composant CustomerList */}
            <CustomerList {...this.state} selectCustomer={this.selectCustomer}/>
            </div>
            </div>
            <div className='col-lg-8 col-xs-12 bg-light'  style={{ height: 658 }}>
              <div className='row p-3 bg-white'>
                <h2>Avec qui allez-vous discuter ?</h2>
              </div>
              <div className='row pt-5 bg-white' 
              style={{ height: 530, overflow:'auto' }}>
              {/* Le composant ChatBox */}
              <ChatBox {...this.state} />
              </div>
              <div className="row bg-light" style={{ bottom: 0, width: '100%' }}>
              <form className="row m-0 p-0 w-100" onSubmit={this.handleSubmit}>
  
              <div className="col-9 m-0 p-1">
                <input id="text" 
                  className="mw-100 border rounded form-control" 
                  type="text" 
                  name="text" 
                  ref="message"
                  placeholder="Tapez un message..."/>
              </div>
              <div className="col-3 m-0 p-1">
                <button className="btn btn-outline-secondary rounded border w-100" 
                  title="Envoyer" 
                  style={{ paddingRight: 16 }}>Envoyer</button>
              </div>
              </form>
              </div>  
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
```

Composant `Chatbox` :

```js
class ChatBox extends Component {
  render(){
    const {chat, chatIsLoading} = this.props;
    if (chatIsLoading) {
      return (
        <div className='col-xl-12 my-auto text-center'>
          <MDSpinner size='72'/>
        </div>
      )
    }
    else {
    // simple mapping du tableau depuis les props
      return (
        <div className='col-xl-12'>
          { 
            chat
            .map(chat => 
              <div key={chat.id} className="message">
                <div className={
                  `${chat.receiver !== agentUID ? 'balon1': 'balon2'} p-3 m-1`
                  }>
                  {chat.text}
                </div>
              </div>)
          }  
        </div>
      )
    }
  }
}
```

Composant `CustomerList` :

```js
class CustomerList extends Component {
  render(){
    const {customers, customerIsLoading, selectedCustomer} = this.props;
    if (customerIsLoading) {
      return (
        <div className='col-xl-12 my-auto text-center'>
          <MDSpinner size='72'/>
        </div>
      )
    }
    else {
      // simple mapping du tableau depuis les props
      return (
        <ul className="list-group list-group-flush w-100">
          { 
            customers
            .map(customer => 
              <li 
                key={customer.uid} 
                className={
                  `list-group-item ${customer.uid === selectedCustomer ? 'active':''}`
                } 
                onClick={ () => this.props.selectCustomer(customer.uid) }>
                  {customer.name} 
              </li>)
          }                
        </ul>
      )
    }
  }
}
```

Cela constitue la base de notre interface utilisateur, mais nous ne pouvons toujours pas envoyer de messages.

Pour envoyer des messages, nous devons créer un gestionnaire pour lorsque l'agent soumet un nouveau message. Comment envoyer des messages devrait vous être familier maintenant car nous allons faire le même appel `sendMessage` que nous avons fait dans le composant Client également.

```js
handleSubmit = event => {
  event.preventDefault();
  let message = this.refs.message.value;
  var textMessage = new CometChat.TextMessage(
    this.state.selectedCustomer,
    message,
    CometChat.MESSAGE_TYPE.TEXT,
    CometChat.RECEIVER_TYPE.USER
  );
  
  CometChat.sendMessage(textMessage).then(
    message => {
      let {chat} = this.state;
      console.log('Message envoyé avec succès:', message);
      chat.push(message);
      this.setState({
        chat
      })
    },
    error => {
      console.log('Échec de l\'envoi du message avec erreur:', error);
    }
  );
  this.refs.message.value='';
}
```

Nous voudrons également permettre à l'agent de voir les messages historiques comme nous l'avons fait pour le client :

```js
selectCustomer = uid => {
  this.setState({
    selectedCustomer: uid
  }, ()=> {this.fetchPreviousMessage(uid)})
}
    
fetchPreviousMessage = uid => {
  this.setState({
    hat: [],
    chatIsLoading: true
  }, () => {
    var messagesRequest = new CometChat.MessagesRequestBuilder()
    .setUID(uid)
    .setLimit(limit)
    .build();
    messagesRequest.fetchPrevious().then(
       messages => {
        console.log("Liste des messages récupérée:", messages);
        this.setState({
          chat: messages,
            chatIsLoading: false
        })
      },
      error => {
        console.log("Échec de la récupération des messages avec erreur:", error);
      }
    );
  });
}
```

N'oubliez pas de supprimer l'écouteur de messages lorsque le composant est démonté :

```js
componentWillUnmount(){
  CometChat.removeMessageListener(AGENT_MESSAGE_LISTENER_KEY);
  CometChat.logout();
}
```

Si vous avez des difficultés, vous pouvez vous référer au fichier complet [Agent](https://github.com/cometchat-pro-samples/react-customer-support-live-widget/blob/master/client/src/Agent.js) ici sur GitHub.

Découvrez le produit final :

![Image](https://cdn-media-1.freecodecamp.org/images/zaqzGAOhLibBXYDBBnAzqf20wb0qNBelmKB2)

Si vous vous demandez d'où viennent ces utilisateurs super-héros, ils sont automatiquement créés par CometChat Pro lorsque vous créez une nouvelle application. N'oubliez pas de les supprimer avant d'utiliser l'application en production.

Maintenant, l'agent de support et vos clients sont prêts à discuter ensemble. Vous pouvez ouvrir l'accueil client et le tableau de bord de l'agent dans des fenêtres séparées et l'essayer.

Félicitations !

## Conclusion

Nous avons créé notre propre widget de chat en direct pour une application React, et cela n'a pris presque aucun temps ! En effet, CometChat Pro vous permet d'envoyer et de recevoir des messages en écrivant seulement quelques lignes de code. Vous n'avez pas besoin de gérer la création de votre propre serveur et architecture de chat. Il a également plus de capacités que simplement créer un widget de chat.

Si vous souhaitiez étendre cette application, essayez d'activer l'envoi de [messages multimédias](https://prodocs.cometchat.com/docs/js-messaging#section-send-media-message) par les clients avec CometChat.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide étape par étape qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !