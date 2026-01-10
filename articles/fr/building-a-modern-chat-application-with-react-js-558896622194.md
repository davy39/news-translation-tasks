---
title: Comment créer une application de chat moderne avec React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-13T19:16:43.000Z'
originalURL: https://freecodecamp.org/news/building-a-modern-chat-application-with-react-js-558896622194
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g_B4JNulmfXSj0AyEjImyA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de chat moderne avec React.js
seo_desc: 'By Samuel Omole

  In this tutorial, I will guide you to build your own group chat application using
  React, React Router, and CometChat Pro. Yes, rather than roll out our own server,
  we will instead use CometChat Pro to handle the real-time sending and ...'
---

Par Samuel Omole

Dans ce tutoriel, je vais vous guider pour créer votre propre application de chat de groupe en utilisant React, React Router et [CometChat Pro](https://www.cometchat.com/pro). Oui, plutôt que de déployer notre propre serveur, nous allons utiliser CometChat Pro pour gérer l'envoi et la réception en temps réel des messages de chat.

Lorsque vous aurez terminé, vous devriez avoir une application de chat fonctionnelle qui ressemble à ceci (bien sûr, vous êtes libre de modifier et d'expérimenter avec les choses au fur et à mesure) :

![Image](https://cdn-media-1.freecodecamp.org/images/uUjaJRgeq1EtbCKptPuNQ2zKMSk4lfMfeQLs)

![Image](https://cdn-media-1.freecodecamp.org/images/BMXCWPYnepUrYQ31dqqWXygDARpYOk1Ky0lS)

J'ai structuré ce tutoriel en une série d'étapes pour le rendre facile à suivre. Si vous souhaitez simplement consulter le code, [cliquez ici](https://github.com/cometchat-pro-samples/react-comet-chat-app).

### Installation du projet

Avant d'aller trop loin, nous devons d'abord configurer notre projet React. Pour ce faire, nous allons utiliser un outil moins connu appelé Create React App.

Le meilleur aspect ? Parce que vous avez npm installé, vous pouvez utiliser npx pour installer et exécuter create-react-app en une seule étape :

`npx create-react-app chatapp // note: npm v5.2+`

Après avoir exécuté cette commande, un nouveau dossier appelé "chatapp" sera créé avec la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/IKF841Qr62aFXMFI5C9qQHiO0xH-nW0taEK1)

En plus de React, nous aurons également besoin d'installer React Router et le SDK CometChat Pro. Pour ce faire, dirigez-vous vers le répertoire chatapp et exécutez :

`npm install react-router-dom @cometchat-pro/chat --save`

### Ajouter React Router

En fin de compte, notre application aura deux pages — une appelée `Login` où l'utilisateur se connectera, et une autre appelée `Groupchat` où nous afficherons la salle de chat. Nous utiliserons React Router pour diriger les utilisateurs vers la page dont ils ont besoin.

Pour configurer React Router, nous devons d'abord importer le composant _wrapper_ `Router` dans notre fichier index.js. Je l'appelle un composant wrapper car nous enveloppons notre `App` à l'intérieur du composant `Router`.

Remplacez index.js par ce snippet :

```js
import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom'; // ajouté
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
ReactDOM.render(
  <Router>
    <App />
  </Router>
  , document.getElementById('root'));
```

`index.js` est le point d'entrée de notre application. Son seul vrai travail est de rendre notre application React. La plupart de notre logique "réelle" se trouve dans un fichier appelé App.js, que nous allons modifier ensuite.

Dans App.js, nous devons importer des dépendances supplémentaires de React Router qui nous permettront de rendre différents composants en fonction de la route chargée par l'utilisateur. Par exemple, si l'utilisateur va à la route "login", nous devons rendre le composant Login. De même, si l'utilisateur va à la route "chat", nous devons rendre le composant `Groupchat` :

```js
import React, { Component } from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import "./App.css";
// les composants ci-dessous seront créés prochainement
import Login from "./components/Login";
import Groupchat from "./components/Groupchat";
class App extends Component {
  constructor(props) {
    super(props);
  }
render() {
    return (
      <Switch>
        <Redirect exact from="/" to="/login" />
        <Route path="/login" component={Login} />
        <Route path="/chat" component={Groupchat} />
      </Switch>
    );
  }
}
export default App;
```

Si vous essayez d'exécuter ce code, il lancera définitivement des erreurs car nous n'avons pas encore créé les composants `Login` et `Groupchat`. Faisons cela maintenant.

### Créer le composant Login

Pour garder notre projet bien organisé, créez un dossier appelé `components` pour contenir nos composants personnalisés.

Ensuite, dans ce dossier nouvellement créé, créez un fichier appelé Login.js avec le code suivant :

```js
import React from "react";
class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }
  render() {
    return ( 
      <div className="App">
        <h1>Login</h1>
      </div>
    );
  }
}
export default Login;
```

Tout ce que nous faisons ici est d'exporter un composant avec le texte d'en-tête, "Login". Nous développerons ce composant bientôt, mais pour l'instant, nous créons simplement un modèle de base.

### Créer le composant Groupchat

Dans le même dossier components, créez un nouveau composant appelé Groupchat.js :

```js
import React from "react";
class Groupchat extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <div className="chatWindow" />;
  }
}
export default Groupchat;
```

Au fur et à mesure que nous progressons dans le tutoriel, nous développerons ce modeste composant en le cœur de notre application de chat.

Avec les composants `Groupchat` et `Login` en place, vous devriez pouvoir exécuter l'application sans erreur. Ouvrez l'application sur localhost et naviguez vers localhost:3000/login puis localhost:3000/chat pour voir les composants en action.

### Créer l'ID d'application CometChat et la clé API

Comme je l'ai mentionné au début du tutoriel, nous ne déployerons pas notre propre serveur dans ce tutoriel. Au lieu de cela, nous utiliserons un service hébergé de [CometChat Pro](http://cometchat.com/pro).

Avant de pouvoir nous connecter à CometChat, nous devons d'abord créer une application CometChat à partir du tableau de bord :

![Image](https://cdn-media-1.freecodecamp.org/images/1uiJPWklG1WfpuVdMSYwC6FBajscCNoNR-fw)

Une fois votre application créée, cliquez sur "Explore" puis dirigez-vous vers l'onglet "API Keys" :

![Image](https://cdn-media-1.freecodecamp.org/images/0I2N1oshD4NW7urTY4hLWXYo5mSDdxS4JZ4Y)

Cliquez sur "Create API key" et remplissez le formulaire, en choisissant Auth Only scope. À partir du tableau, vous pouvez noter votre ID d'application et votre clé d'application, nous en aurons besoin sous peu.

### Créer l'ID de groupe CometChat

Pendant que nous avons le tableau de bord ouvert, créons également un _groupe_. Normalement, vous feriez cela avec du code (par exemple, vous pourriez permettre à l'utilisateur de créer un groupe de chat personnalisé pour leur équipe ou projet via votre application), mais pour l'apprentissage et les tests, le tableau de bord est suffisant.

Dirigez-vous vers l'onglet "Groups" et créez un nouveau groupe appelé testgroup :

![Image](https://cdn-media-1.freecodecamp.org/images/GeeNNciJ-UnawrFegFOX04dsAzhii7V3GPeE)

Comme la dernière fois, vous serez redirigé vers un tableau où vous pourrez noter l'ID du groupe :

![Image](https://cdn-media-1.freecodecamp.org/images/7IQuc9f-PA6USd3CHkZmuekCSwZiyiTphEUG)

Prenez note car nous en aurons besoin à l'étape suivante.

### Créer le fichier de configuration

Pour faciliter la référence à notre configuration, créez un nouveau fichier appelé config.js et collez vos identifiants :

```js
export default {
  appId: "", //Entrez votre App ID
  apiKey: "", //Entrez votre API KEY
  GUID: "", // Entrez votre group UID
};
```

Vous pouvez maintenant fermer le tableau de bord. Une fois que vous avez configuré CometChat, toutes les interactions se font via le code.

### Créer une classe CometChat Manager

L'une des belles choses à propos de React est qu'il se prête à une séparation des préoccupations. Nos composants peuvent se concentrer purement sur la présentation tandis que nous pouvons créer d'autres modules pour gérer des choses comme la récupération de données et la gestion d'état.

Pour vraiment tirer parti de cela, créons un nouveau dossier appelé "lib" et dans ce nouveau dossier, un fichier appelé chat.js. C'est là que toutes nos interactions avec CometChat auront lieu :

```js
import { CometChat } from "@cometchat-pro/chat";
import config from "../config";
export default class CCManager {
  static LISTENER_KEY_MESSAGE = "msglistener";
  static appId = config.appId;
  static apiKey = config.apiKey;
  static LISTENER_KEY_GROUP = "grouplistener";
  static init() {
    return CometChat.init(CCManager.appId);
  }
  static getTextMessage(uid, text, msgType) {
    if (msgType === "user") {
      return new CometChat.TextMessage(
        uid,
        text,
        CometChat.MESSAGE_TYPE.TEXT,
        CometChat.RECEIVER_TYPE.USER
      );
    } else {
      return new CometChat.TextMessage(
        uid,
        text,
        CometChat.MESSAGE_TYPE.TEXT,
        CometChat.RECEIVER_TYPE.GROUP
      );
    }
  }
  static getLoggedinUser() {
    return CometChat.getLoggedinUser();
  }
  static login(UID) {
    return CometChat.login(UID, this.apiKey);
  }
  static getGroupMessages(GUID, callback, limit = 30) {
    const messagesRequest = new CometChat.MessagesRequestBuilder()
      .setGUID(GUID)
      .setLimit(limit)
      .build();
    callback();
    return messagesRequest.fetchPrevious();
  }
  static sendGroupMessage(UID, message) {
    const textMessage = this.getTextMessage(UID, message, "group");
    return CometChat.sendMessage(textMessage);
  }
  static joinGroup(GUID) {
    return CometChat.joinGroup(GUID, CometChat.GROUP_TYPE.PUBLIC, "");
  }
  static addMessageListener(callback) {
    CometChat.addMessageListener(
      this.LISTENER_KEY_MESSAGE,
      new CometChat.MessageListener({
        onTextMessageReceived: textMessage => {
          callback(textMessage);
        }
      })
    );
  }
}

```

En plus de nous permettre de créer une séparation des préoccupations, présenter le code de cette manière le rend également plus facile à digérer.

Permettez-moi d'expliquer certaines parties importantes de ce module, en commençant par le haut :

* `LISTENER_KEY_MESSAGE` – Cela est requis par l'écouteur de messages.
* `init()` – Cela doit être appelé une seule fois tout au long du cycle de vie de l'application, il appelle la méthode `init` de CometChat avec l'appID.
* `getTextMessage(uid, text, msgType)` – il crée l'objet message basé sur la méthode `CometChat.TextMessage`, il accepte l'UID (GUID dans notre cas) et le message texte à envoyer.
* `getLoggedInUser()` – il est utilisé pour obtenir l'utilisateur actuellement connecté.
* `login()` – il est utilisé pour connecter un utilisateur basé sur la méthode CometChat.login, il prend l'UID (GUID dans notre cas) et l'apiKey.
* `getGroupMessages(GUID, callback, limit = 30)` – cela est utilisé pour obtenir les messages de groupe précédents de CometChat en utilisant la méthode `CometChat.MessagesRequestBuilder()` qui prend en paramètres le GUID et la limite.
* `sendGroupMessage(UID, message)` – cela est utilisé pour envoyer des messages en utilisant la méthode `CometChat.sendMessage()` et il accepte le GUID et le message comme paramètres.
* `joinGroup(GUID)` – Il est utilisé pour rejoindre un groupe choisi en utilisant un GUID.
* `addMessageListener(callback)` – Utilise `CometChat.addMessageListener()` pour écouter les messages (ai-je mentionné que cela est appelé en temps réel ?), il nécessite `LISTENER_KEY_MESSAGE` comme paramètre et également un callback qui est appelé lorsqu'un message est reçu.

Il n'y a rien de spécifique à cette application ici. Vous pourriez bien prendre ce module, l'étendre si nécessaire, et l'importer dans un autre projet. Généralement, cependant, ce n'est qu'un wrapper mince autour du SDK.

### Mettre à jour le composant de connexion

Avec toute notre configuration et notre code de chat en place, nous pouvons maintenant construire rapidement l'interface utilisateur en commençant par le composant `Login`.

Juste pour vous rappeler, voici à quoi ressemblera le composant Login :

![Image](https://cdn-media-1.freecodecamp.org/images/fm3GKd-dBpRogU66edgVDEx-VbBk2EFF0mdO)

Comme vous pouvez le voir, sa fonction principale est de demander à l'utilisateur son nom. Une fois qu'un nom est fourni, nous rendons le composant `Groupchat`.

Remplacez `Login.js` par :

```js
import React from "react";
import { Redirect } from "react-router-dom";
import chat from "../lib/chat";
import spinner from "../logo.svg";
class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      isAuthenticated: false,
      user: null,
      isSubmitting: false,
      errorMessage: ""
    };
  }
  onSubmit = e => {
    if (this.state.username !== "") {
      e.preventDefault();
      this.login();
    }
  };
  login = () => {
    this.toggleIsSubmitting();
    chat
    .login(this.state.username)
    .then(user => {
      this.setState({
        user,
        isAuthenticated: true
      });
    })
    .catch(error => {
      this.setState({
        errorMessage: "Veuillez entrer un nom d'utilisateur valide"
      });
      this.toggleIsSubmitting();
      console.log(error);
    });
  };
  toggleIsSubmitting = () => {
    this.setState(prevState => ({
      isSubmitting: !prevState.isSubmitting
    }));
  };
  handleInputChange = e => {
    this.setState({
      username: e.target.value
    });
  };
  render() {
    if (this.state.isAuthenticated) {
      return (
        <Redirect
          to={{
            pathname: "/chat",
            state: { user: this.state.user }
          }}
        />
      );
    }
    return (
      <div className="App">
        <h1>COMETCHAT</h1>
        <p>Créez un compte via votre tableau de bord CometChat ou connectez-vous avec l'un de nos utilisateurs de test, superhero1, superhero2, etc.</p>
        <form className="form" onSubmit={this.onSubmit}>
          <input onChange={this.handleInputChange} type="text" />
          <span className="error">{this.state.errorMessage}</span>
          {this.state.isSubmitting ? (
            <img src={spinner} alt="Composant Spinner" className="App-logo" />
          ) : (
            <input
              type="submit"
              disabled={this.state.username === ""}
              value="CONNEXION"
            />
          )}
        </form>
      </div>
    );
  }
}
export default Login;
```

En dehors du HTML de présentation, la plupart du code ici est dédié à la gestion d'un [formulaire React](https://reactjs.org/docs/forms.html).

### Mettre à jour le composant Groupchat

Le composant Groupchat a beaucoup plus de responsabilités que le composant Login. Pour un rappel rapide, voici à quoi il ressemblera :

![Image](https://cdn-media-1.freecodecamp.org/images/UazFSe6wyPti-CxoNLE5ERziJt4Pmqt1ucro)

Pour la plupart, le travail du composant `Groupchat` est de faire le pont entre le module de bibliothèque de chat et l'interface utilisateur que nous présenterons à l'utilisateur. Par exemple, lorsqu'un utilisateur envoie un message, nous appelons `chat.sendMessage` et à mesure que de nouveaux messages arrivent, une fonction de rappel est appelée :

```js
import React from "react";
import { Redirect } from "react-router-dom";
import chat from "../lib/chat";
import config from "../config";
class Groupchat extends React.Component {
  constructor(props) {
    super(props);
this.state = {
      receiverID: "",
      messageText: null,
      groupMessage: [],
      user: {},
      isAuthenticated: true
    };
this.GUID = config.GUID;
  }
sendMessage = () => {
    chat.sendGroupMessage(this.GUID, this.state.messageText).then(
      message => {
        console.log("Message envoyé avec succès :", message);
        this.setState({ messageText: null });
      },
      error => {
        if (error.code === "ERR_NOT_A_MEMBER") {
          chat.joinGroup(this.GUID).then(response => {
            this.sendMessage();
          });
        }
      }
    );
  };
scrollToBottom = () => {
    const chat = document.getElementById("chatList");
    chat.scrollTop = chat.scrollHeight;
  };
handleSubmit = event => {
    event.preventDefault();
    this.sendMessage();
    event.target.reset();
  };
handleChange = event => {
    this.setState({ messageText: event.target.value });
  };
getUser = () => {
    chat
      .getLoggedinUser()
      .then(user => {
        console.log("détails de l'utilisateur :", { user });
        this.setState({ user });
      })
      .catch(({ error }) => {
        if (error.code === "USER_NOT_LOGED_IN") {
          this.setState({
            isAuthenticated: false
          });
        }
      });
  };
messageListener = () => {
    chat.addMessageListener((data, error) => {
      if (error) return console.log(`error: ${error}`);
      this.setState(
        prevState => ({
          groupMessage: [...prevState.groupMessage, data]
        }),
        () => {
          this.scrollToBottom();
        }
      );
    });
  };
componentDidMount() {
    this.getUser();
    this.messageListener();
    // chat.joinGroup(this.GUID)
  }
render() {
    const { isAuthenticated } = this.state;
    if (!isAuthenticated) {
      return <Redirect to="/" />;
    }
    return (
      <div className="chatWindow">
        <ul className="chat" id="chatList">
          {this.state.groupMessage.map(data => (
            <div key={data.id}>
              {this.state.user.uid === data.sender.uid ? (
                <li className="self">
                  <div className="msg">
                    <p>{data.sender.uid}</p>
                    <div className="message"> {data.data.text}</div>
                  </div>
                </li>
              ) : (
                <li className="other">
                  <div className="msg">
                    <p>{data.sender.uid}</p>
                   <div className="message"> {data.data.text} </div>
                  </div>
                </li>
              )}
            </div>
          ))}
        </ul>
        <div className="chatInputWrapper">
          <form onSubmit={this.handleSubmit}>
            <input
              className="textarea input"
              type="text"
              placeholder="Entrez votre message..."
              onChange={this.handleChange}
            />
          </form>
        </div>
      </div>
    );
  }
}
export default Groupchat;
```

Il y a beaucoup à digérer ici, alors décomposons les parties importantes :

* `sendMessage()` – Cette fonction gère l'envoi d'un message au groupe, en passant le GUID et le message texte qui est stocké dans l'état du composant. Si l'utilisateur ne fait pas partie du groupe, nous faisons alors une demande pour rejoindre le groupe et appelons à nouveau la fonction sendMessage.
* `scrollToBottom()` – Cette fonction sera utilisée comme fonction de rappel pour l'écouteur de messages, elle s'assure simplement que les derniers messages sont affichés dans la liste de chat.
* `handleSubmit()` – Cela appelle la fonction sendMessage.
* `getUser()` – Cela appelle la méthode chat.getLoggedInUser() et stocke l'objet utilisateur dans l'état du composant.
* `messageListener()` – Cela appelle la fonction chat.addMessageListener() et ajoute chaque nouveau message reçu au tableau `groupMessage` qui est stocké dans l'état du composant et rendu dans l'application.
* `componentDidMount()` – Cela appelle les fonctions getUser et messageListener.

Enfin, nous rendons une classe en fonction de si le message est le nôtre ou celui de quelqu'un d'autre. De cette façon, nous pouvons appliquer différents styles, ce qui est le sujet de la section suivante.

### Mettre à jour les styles

Si vous deviez exécuter l'application maintenant, elle fonctionnerait mais sans CSS à proprement parler jusqu'à présent, elle aurait l'air assez, eh bien, étrange.

Ce n'est pas un tutoriel sur CSS, donc je ne l'expliquerai pas en détail, mais pour vous aider à suivre, vous pouvez coller ce qui suit dans votre fichier App.css (vous en aurez déjà un car il a été généré par `create-react-app` plus tôt) :

```css
.App {
  text-align: center;
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 50vh;
}
.App p{
  font-size: 12px;
  width: 50%;
}
.App-logo {
  animation: App-logo-spin infinite 0.5s linear;
  height: 10vmin;
}
.form {
  display: flex;
  flex-direction: column;
}
.form input[type="text"] {
  width: 300px;
  height: 30px;
  margin-bottom: 10px;
}
.form input[type="submit"] {
  padding: 5px;
  height: 30px;
  border: none;
  background-color: #187dbc;
  color: #fff;
}
.form input[type="submit"]:hover {
  border: #fff;
  cursor: pointer;
  background-color: #000;
  color: #fff;
}
.error{
  color: red;
  font-size: 10px;
  text-align: center;
}
@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.message {
  font-size: 15px !important;
}
body {
  background-color: #f5f5f5;
  font: 600 18px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Lato,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  color: #4b4b4b;
}
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(1, 50px);
  grid-gap: 3px;
  margin-top: 15px;
}
.group {
  background: #4eb5e5;
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 190;
  border-radius: 5px;
}
.chatWindow {
  display: grid;
  grid-column-start: 2;
  grid-column-end: 9;
  grid-row-start: 1;
  grid-row-end: 190;
  background: rgb(233, 229, 229);
  border-radius: 5px;
}
.chatInputWrapper {
  display: grid;
  grid-row-start: 190;
  grid-row-end: 190;
}
::-webkit-scrollbar {
  display: none;
}
/* M E S S A G E S */
.chat {
  list-style: none;
  background: none;
  margin: 0;
  padding: 0 0 50px 0;
  margin-top: 60px;
  margin-bottom: 10px;
  max-height: 400px;
  overflow: scroll;
  scroll-behavior: smooth;
}
.chat li {
  padding: 0.5rem;
  overflow: hidden;
  display: flex;
}
.chat .avatar {
  position: relative;
  display: block;
  z-index: 2;
}
.chat .avatar img {
  background-color: rgba(255, 255, 255, 0.9);
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.chat .uid img {
  background-color: rgba(255, 255, 255, 0.9);
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.chat .day {
  position: relative;
  display: block;
  text-align: center;
  color: #c0c0c0;
  height: 20px;
  text-shadow: 7px 0px 0px #e5e5e5, 6px 0px 0px #e5e5e5, 5px 0px 0px #e5e5e5,
    4px 0px 0px #e5e5e5, 3px 0px 0px #e5e5e5, 2px 0px 0px #e5e5e5,
    1px 0px 0px #e5e5e5, 1px 0px 0px #e5e5e5, 0px 0px 0px #e5e5e5,
    -1px 0px 0px #e5e5e5, -2px 0px 0px #e5e5e5, -3px 0px 0px #e5e5e5,
    -4px 0px 0px #e5e5e5, -5px 0px 0px #e5e5e5, -6px 0px 0px #e5e5e5,
    -7px 0px 0px #e5e5e5;
  box-shadow: inset 20px 0px 0px #e5e5e5, inset -20px 0px 0px #e5e5e5,
    inset 0px -2px 0px #d7d7d7;
  line-height: 38px;
  margin-top: 5px;
  margin-bottom: 20px;
  cursor: default;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.other .msg {
  order: 1;
  border-top-left-radius: 0px;
  box-shadow: -1px 2px 0px #d4d4d4;
}
.other:before {
  content: "";
  position: relative;
  top: 0px;
  right: 0px;
  left: 40px;
  width: 0px;
  height: 0px;
  border: 5px solid #fff;
  border-left-color: transparent;
  border-bottom-color: transparent;
}
.self {
  justify-content: flex-end;
  align-items: flex-end;
}
.self .msg {
  order: 1;
  border-bottom-right-radius: 0px;
  box-shadow: 1px 2px 0px #d4d4d4;
}
.self .avatar {
  order: 2;
}
.self .avatar:after {
  content: "";
  position: relative;
  display: inline-block;
  bottom: 19px;
  right: 0px;
  width: 0px;
  height: 0px;
  border: 5px solid #fff;
  border-right-color: transparent;
  border-top-color: transparent;
  box-shadow: 0px 2px 0px #d4d4d4;
}
.msg {
  background: white;
  min-width: fit-content;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.07);
}
.msg p {
  font-size: 0.8rem;
  margin: 0 0 0.2rem 0;
  color: rgb(81, 84, 255);
}
.msg img {
  position: relative;
  display: block;
  width: 450px;
  border-radius: 5px;
  box-shadow: 0px 0px 3px #eee;
  transition: all 0.4s cubic-bezier(0.565, -0.26, 0.255, 1.41);
  cursor: default;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
@media screen and (max-width: 800px) {
  .msg img {
    width: 300px;
  }
}
@media screen and (max-width: 550px) {
  .msg img {
    width: 200px;
  }
}
.msg time {
  font-size: 0.7rem;
  color: #ccc;
  margin-top: 3px;
  float: right;
  cursor: default;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.msg time:before {
  content: " ";
  color: #ddd;
  font-family: FontAwesome;
  display: inline-block;
  margin-right: 4px;
}
::-webkit-scrollbar {
  min-width: 12px;
  width: 12px;
  max-width: 12px;
  min-height: 12px;
  height: 12px;
  max-height: 12px;
  background: #e5e5e5;
}
::-webkit-scrollbar-thumb {
  background: rgb(48, 87, 158);
  border: none;
  border-radius: 100px;
  border: solid 3px #e5e5e5;
  box-shadow: inset 0px 0px 3px #999;
}
::-webkit-scrollbar-thumb:hover {
  background: #b0b0b0;
  box-shadow: inset 0px 0px 3px #888;
}
::-webkit-scrollbar-thumb:active {
  background: #aaa;
  box-shadow: inset 0px 0px 3px #7f7f7f;
}
::-webkit-scrollbar-button {
  display: block;
  height: 26px;
}
/* T Y P E */
input.textarea {
  width: 100%;
  height: 50px;
  background: #fafafa;
  border: none;
  outline: none;
  padding-left: 55px;
  padding-right: 55px;
  color: #666;
  font-weight: 400;
}
```

### Conclusion

Exécutez l'application avec `npm start` et, à votre grande surprise, votre application de chat est complète. Au moins, la fonctionnalité de base est en place. Avec CometChat, vous pourriez facilement étendre l'application pour inclure une liste "qui est en ligne", des messages directs, des messages multimédias et une série d'autres fonctionnalités.

_Cet article a été initialement publié sur le [blog](https://www.cometchat.com/tutorials/build-a-modern-chat-application-with-react) de Cometchat._