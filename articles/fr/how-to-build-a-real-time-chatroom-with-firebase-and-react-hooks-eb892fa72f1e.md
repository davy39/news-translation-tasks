---
title: Comment créer un salon de discussion en temps réel avec Firebase et React (Hooks)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T17:07:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-chatroom-with-firebase-and-react-hooks-eb892fa72f1e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*CPTNvq87xG-sUGdx.png
tags:
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer un salon de discussion en temps réel avec Firebase et React
  (Hooks)
seo_desc: 'By Aswin M Prabhu

  If you are into front-end development, I bet you know what react is. It has become
  the most popular front-end framework and does not appear to be slowing down. Firebase
  is a back-end service created by Google that enables developers...'
---

Par Aswin M Prabhu

Si vous vous intéressez au développement front-end, je parie que vous savez ce qu'est [**React**](https://reactjs.org). Il est devenu le framework front-end le plus populaire et ne semble pas ralentir. [**Firebase**](https://firebase.google.com/) est un service back-end créé par Google qui permet aux développeurs d'itérer rapidement sur leurs applications sans se soucier des tâches courantes comme l'authentification, la base de données, le stockage.

![Image](https://cdn-media-1.freecodecamp.org/images/0*CPTNvq87xG-sUGdx.png)

Firebase propose deux options de base de données, toutes deux avec des capacités [**en temps réel**](https://firebase.google.com/docs/firestore/query-data/listen) impressionnantes. Par exemple, vous pouvez vous abonner aux changements dans un document stocké dans Firebase Cloud Firestore avec le snippet JavaScript suivant.

```jsx
db.collection("cities").doc("SF")
    .onSnapshot(function(doc) {
        console.log("Current data: ", doc.data());
    });
```

La fonction de rappel fournie à la fonction `onSnapshot()` se déclenche chaque fois que le document change. Les écritures locales de votre application la déclencheront immédiatement avec une fonctionnalité appelée compensation de latence.

[**Les Hooks React**](https://reactjs.org/docs/hooks-intro.html) sont une fonctionnalité à venir de React qui vous permet d'utiliser l'état et d'autres fonctionnalités de React sans écrire de classe. Ils sont actuellement dans React v16.7.0-alpha. Construire cette application est un excellent moyen d'explorer l'avenir de React avec les hooks.

Le produit final sera une application de salon de discussion global similaire à IRC où nous demandons d'abord à l'utilisateur de saisir un pseudonyme. Simple.

### Échafaudage

Une nouvelle application React peut être facilement créée avec l'outil cli officiel [**create-react-app**](https://www.npmjs.com/package/create-react-app) avec les commandes de terminal suivantes (les hooks React nécessitent React et React-DOM v16.7.0-alpha).

```bash
npm i -g create-react-app
create-react-app react-firebase-chatroom
cd react-firebase-chatroom
npm i -S react@16.7.0-alpha.2 react-dom@16.7.0-alpha.2
```

La configuration de Firebase est également assez simple. Créez un nouveau projet depuis la [**console Firebase**](https://console.firebase.google.com/). Configurez la base de données Firebase en temps réel en mode test. Initialisez le projet local avec la commande [**firebase-tools**](https://www.npmjs.com/package/firebase-tools?activeTab=versions). Choisissez la base de données en temps réel et l'hébergement comme fonctionnalités activées. Sélectionnez `build` comme répertoire public. Toutes les autres options peuvent être laissées telles quelles.

```bash
npm i -g firebase-tools
firebase-tools init
npm i -S firebase
```

Il peut être nécessaire de vous connecter avant de pouvoir initialiser le dépôt.

La structure de la base de données ressemblera à ce qui suit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ee0K24UqQJF9cgjkOaS2ug.png)
_Structure de la base de données_

### Construction de l'application en utilisant les composants basés sur les classes

Les hooks React sont encore une fonctionnalité expérimentale et l'API pourrait changer à l'avenir. Nous allons donc d'abord voir comment l'application peut être construite avec des composants basés sur les classes. J'ai opté uniquement pour le composant `App` car la logique de l'application était suffisamment simple.

L'utilisateur sera invité à rejoindre avec un pseudonyme et un email si la variable `joined` est `false`. Elle est initialement définie sur false dans le `constructor`.

```jsx
constructor() {
    super();
    this.state = {
      joined: false,
      nickname: "",
      email: "",
      msg: "",
      messages: {},
    };
    this.chatRoom = db.ref().child('chatrooms').child('global');
    this.handleNewMessages = snap => {
      console.log(snap.val());
      if (snap.val()) this.setState({ messages: snap.val() });
    };
  }
  
  componentDidMount() {
    this.chatRoom.on('value', this.handleNewMessages);
  }
  
  componentWillUnmount() {
    this.chatRoom.off('value', this.handleNewMessages);
  }

```

Tous les messages sont initialement récupérés depuis Firebase dans la méthode de cycle de vie `componentDidMount`. La méthode `on` sur une référence de base de données prend un [type d'événement](https://firebase.google.com/docs/reference/js/firebase.database.Reference#on) et une fonction de rappel comme arguments. Chaque fois qu'un utilisateur envoie un nouveau message et met à jour la base de données, la fonction `handleNewMessages` reçoit un instantané des données mises à jour et met à jour l'état avec les nouveaux messages. Nous pouvons nous désabonner des mises à jour de la base de données dans la méthode de cycle de vie `componentWillUnmount` en utilisant la méthode `off` sur la référence de la base de données.

Un message peut être envoyé en ajoutant le message à la référence du salon de discussion dans la base de données. La méthode `push` de la référence génère un identifiant unique pour la nouvelle entrée et l'ajoute aux données existantes.

```jsx
this.chatRoom.push({
  sender: this.state.nickname,
  msg: this.state.msg,
});
```

Les messages sont rendus en parcourant l'objet `messages`.

```jsx
{Object.keys(this.state.messages).map(message => {
  if(this.state.messages[message]["sender"] === this.state.nickname)
    // rendre les messages de l'utilisateur      
  else
    // rendre les messages des autres utilisateurs
})}
```

Le composant final `App` ressemblera à ceci.

```jsx
class App extends Component {
  constructor() {
    super();
    this.state = {
      joined: false,
      nickname: "",
      email: "",
      msg: "",
      messages: {},
    };
    this.chatRoom = db.ref().child('chatrooms').child('global');
    this.handleNewMessages = snap => {
      console.log(snap.val());
      // si non null alors mettre à jour l'état
      if (snap.val()) this.setState({ messages: snap.val() });
    };
  }
  
  componentDidMount() {
    // s'abonner
    this.chatRoom.on('value', this.handleNewMessages);
  }
  componentWillUnmount() {
    // se désabonner
    this.chatRoom.off('value', this.handleNewMessages);
  }
  handleNameChange = e => this.setState({ nickname: e.target.value });
  handleEmailChange = e => this.setState({ email: e.target.value });
  handleClick = e => {
    // enregistrer le pseudonyme
    db.ref().child('nicknames').push({
      nickname: this.state.nickname,
      email: this.state.email,
    });
    this.setState({ joined: true });
  };

  handleMsgChange = e => this.setState({ msg: e.target.value });
  handleKeyDown = e => {
    if (e.key === "Enter") {
      // envoyer le message
      this.chatRoom.push({
        sender: this.state.nickname,
        msg: this.state.msg,
      });
      // effacer le champ
      this.setState({ msg: "" });
    }
  };
  render() {
    return (
      <div className="App">
        {!this.state.joined ? (
          <div className="joinForm">
            <input placeholder="Pseudonyme" value={this.state.nickname} onChange={this.handleNameChange} /><br />
            <input placeholder="Email" value={this.state.email} onChange={this.handleEmailChange} /><br />
            <button onClick={this.handleClick}>Rejoindre</button>
          </div>
        ) : (
            <div className="chat">
              <div className="messages">
                {Object.keys(this.state.messages).map(message => {
                  // Vérifier si le message est de l'utilisateur
                  if (this.state.messages[message]["sender"] === this.state.nickname)
                    return (
                      <div className="message">
                        <span id="me">{this.state.messages[message]["sender"]} :</span><br />
                        {this.state.messages[message]["msg"]}
                      </div>
                    );
                  else
                    return (
                      <div className="message">
                        <span id="sender">{this.state.messages[message]["sender"]} :</span><br />
                        {this.state.messages[message]["msg"]}
                      </div>
                    );
                })}
              </div>
              <input placeholder="message" onChange={this.handleMsgChange} onKeyDown={this.handleKeyDown} value={this.state.msg} /><br />
            </div>
          )}
      </div>
    );
  }
}
```

Trouvez le gist [**ici**](https://gist.github.com/aswinmprabhu/665c555577f78b4865bb782bb26df3bb).

### Migration vers les hooks React

Le hook le plus simple est le hook `useState`. Il prend l'état initial et retourne la variable d'état et une fonction qui vous permet de la mettre à jour. Cette fonction agit comme un remplacement pour `this.setState`. Par exemple, la logique d'état du pseudonyme peut être modifiée comme suit.

```jsx
const [nickname, setNickname] = useState("");
const handleNameChange = e => setNickname(e.target.value);
.
.
.
// pendant le rendu
<input placeholder="Pseudonyme" value={nickname} onChange={handleNameChange} />
```

Le prochain défi est de trouver un endroit pour la logique à l'intérieur des méthodes de cycle de vie. C'est là que le hook `useEffect` intervient. C'est là que nous effectuons la logique qui a des effets secondaires. Il peut être considéré comme une combinaison de toutes les méthodes de cycle de vie. `useEffect` peut également retourner une fonction qui est utilisée pour nettoyer (comme se désabonner d'un événement).

```jsx
useEffect(() => {
  const handleNewMessages = snap => {
    if (snap.val()) setMessages(snap.val());
  }
  chatRoom.on('value', handleNewMessages);
  return () => {
    chatRoom.off('value', handleNewMessages);
  };
});
```

L'abonnement et le désabonnement étaient des morceaux de logique liés qui étaient divisés en différentes méthodes de cycle de vie. Maintenant, ils sont rassemblés dans un seul hook. L'utilisation de différents hooks `useEffect` pour différents effets secondaires permet la séparation des préoccupations.

Par défaut, `useEffect` s'exécute à la fois après le premier rendu _et_ après chaque mise à jour.

L'un des principaux avantages de l'utilisation des hooks est que la logique d'état peut être réutilisée entre les composants. Par exemple, imaginez que vous souhaitez réutiliser la logique de gestion et de validation de la saisie d'email dans plusieurs composants. Un hook personnalisé peut atteindre cet objectif comme montré ci-dessous. Un hook personnalisé est une fonction qui peut appeler d'autres hooks et commence par « use ». Commencer par « use » n'est pas une règle mais une convention très importante.

```jsx
function useEmail(defaultEmail) {
  const [email, setEmail] = useState(defaultEmail);
  const [isValidEmail, setValidEmail] = useState(defaultEmail);
  
  function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }
  
function handleEmailChange(e) {
    if (validateEmail(e.target.value)) {
      setValidEmail(true);
    }
    setEmail(e.target.value);
  }
  return {
    email,
    handleEmailChange,
    isValidEmail
  };
}
```

Et dans vos composants, vous pouvez utiliser le hook personnalisé comme montré ci-dessous.

```jsx
// dans vos composants
const { email, handleEmailChange, isValidEmail } = useEmail("")
.
.
.
<input value={email} value={email} onChange={handleEmailChange} />
// afficher le message d'erreur basé sur isValidEmail
```

Les hooks personnalisés facilitent également les tests unitaires d'une partie de la logique indépendante des composants qui utilisent le hook.

Le composant final `App` ressemble à ce qui suit.

```jsx
function App() {
  const [nickname, setNickname] = useState("");
  const [email, setEmail] = useState("");
  const [joined, setJoined] = useState(false);
  const [msg, setMsg] = useState("");
  const [messages, setMessages] = useState({});

  const chatRoom = db.ref().child('chatrooms').child('global');

  useEffect(() => {
    const handleNewMessages = snap => {
      if (snap.val()) setMessages(snap.val());
    }
    chatRoom.on('value', handleNewMessages);
    return () => {
      chatRoom.off('value', handleNewMessages);
    };
  });

  const handleNameChange = e => setNickname(e.target.value);
  const handleEmailChange = e => setEmail(e.target.value);
  const handleClick = e => {
    db.ref().child('nicknames').push({
      nickname,
      email,
    });
    setJoined(true);
  };

  const handleMsgChange = e => setMsg(e.target.value);
  const handleKeyDown = e => {
    if (e.key === "Enter") {
      chatRoom.push({
        sender: nickname,
        msg,
      });
      setMsg("");
    }
  };

  return (
    <div className="App">
      {!joined ? (
        <div className="joinForm">
          <input placeholder="Pseudonyme" value={nickname} onChange={handleNameChange} /><br />
          <input placeholder="Email" value={email} onChange={handleEmailChange} /><br />
          <button onClick={handleClick}>Rejoindre</button>
        </div>
      ) : (
          <div className="chat">
            <div className="messages">
              {Object.keys(messages).map(message => {
                if (messages[message]["sender"] === nickname)
                  return (
                    <div className="message">
                      <span id="me">{messages[message]["sender"]} :</span><br />
                      {messages[message]["msg"]}
                    </div>
                  );
                else
                  return (
                    <div className="message">
                      <span id="sender">{messages[message]["sender"]} :</span><br />
                      {messages[message]["msg"]}
                    </div>
                  );
              })}
            </div>
            <input placeholder="message" onChange={handleMsgChange} onKeyDown={handleKeyDown} value={msg} /><br />
          </div>
        )}
    </div>
  );
}
```

Trouvez le gist [**ici**](https://gist.github.com/aswinmprabhu/601e74d26e88e882038764cc2e0b3df6).

#### Il y a plus à lire sur les hooks

1. [**Motivation derrière les hooks**](https://reactjs.org/docs/hooks-intro.html#motivation)
2. [**Règles d'or des hooks**](https://reactjs.org/docs/hooks-rules.html)
3. [**Référence de l'API des hooks**](https://reactjs.org/docs/hooks-reference.html)
4. [**Comprendre les hooks par Dan Abramov**](https://medium.com/@dan_abramov/making-sense-of-react-hooks-fdbde8803889)

Trouvez [l'application finale](https://react-chat-room-4b8e8.firebaseapp.com/) avec un style minimal.

Merci d'avoir lu et bon codage !

Retrouvez-moi sur [**Twitter**](https://twitter.com/aswinmprabhu) et [**GitHub**](https://github.com/aswinmprabhu).