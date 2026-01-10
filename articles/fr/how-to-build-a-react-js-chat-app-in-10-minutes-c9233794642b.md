---
title: Apprendre à créer une application de chat React en 10 minutes - Tutoriel React
  JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-19T15:25:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-react-js-chat-app-in-10-minutes-c9233794642b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SUeSr13iO7yJfIf4ipaeFg.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: Apprendre à créer une application de chat React en 10 minutes - Tutoriel
  React JS
seo_desc: 'By Per Harald Borgen


  _Click here to get to the full course this article is based on._

  In this article, I’ll show you the easiest way possible to create a chat application
  using React.js. It’ll be done entirely without server-side code, as we’ll let ...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*NE_xQlf9WZkO3LTpxG5TNA.png)
_[Cliquez ici pour accéder au cours complet](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=greactchatkit_10_minute_article) sur lequel cet article est basé._

Dans cet article, je vais vous montrer la manière la plus simple possible de créer une application de chat en utilisant React.js. Cela sera fait entièrement sans code côté serveur, car nous laisserons l'API [Chatkit](https://pusher.com/chatkit) gérer le back-end.

Je suppose que vous connaissez le JavaScript de base et que vous avez déjà rencontré un peu React.js. À part cela, il n'y a pas de prérequis.

Note : J'ai également créé un cours complet gratuit sur [comment créer une application de chat React.js ici :](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article)

Si vous suivez ce tutoriel, vous aurez votre propre application de chat à la fin, que vous pourrez ensuite développer davantage si vous le souhaitez.

Commençons !

### Étape 1 : Décomposer l'interface utilisateur en composants

React est construit autour des composants, donc la première chose à faire lors de la création d'une application est de décomposer son interface utilisateur en composants.

Commençons par dessiner un rectangle autour de l'ensemble de l'application. C'est votre composant racine et l'ancêtre commun de tous les autres composants. Appelons-le `App` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*66jz6LtljJtOPDouK9PmYA.png)

Une fois que vous avez défini votre composant racine, vous devez vous poser la question suivante :

Quels sont les enfants directs de ce composant ?

Dans notre cas, il est logique de lui donner trois composants enfants, que nous appellerons :

* `Title`
* `MessagesList`
* `SendMessageForm`

Dessinons un rectangle pour chacun d'eux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SUeSr13iO7yJfIf4ipaeFg.png)

Cela nous donne une bonne vue d'ensemble des différents composants et de l'architecture de notre application.

Nous aurions pu continuer à nous demander quels enfants ces composants ont à leur tour. Ainsi, nous aurions pu décomposer l'interface utilisateur en encore plus de composants, par exemple en transformant chacun des messages en leurs propres composants. Cependant, nous nous arrêterons ici pour des raisons de simplicité.

### Étape 2 : Configuration de la base de code

Maintenant, nous devons configurer notre dépôt. Nous utiliserons la structure la plus simple possible : un fichier *index.html* avec des liens vers un fichier JavaScript et une feuille de style. Nous importons également le SDK Chatkit et Babel, qui est utilisé pour transformer notre JSX :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YCcPOlQGBk-dP-UQnyLEMA.png)

[Voici un terrain de jeu Scrimba](https://scrimba.com/c/c7aW2hd?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article) avec le code final du tutoriel. Je vous recommande de l'ouvrir dans un nouvel onglet et de jouer avec lorsque vous êtes confus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xmr7Z2oR1PwJvLq2sHuZbQ.png)

Alternativement, vous pouvez télécharger le projet Scrimba sous forme de fichier .zip et exécuter un simple [serveur pour le faire fonctionner localement.](https://gist.github.com/willurd/5720255)

### Étape 3 : Création du composant racine

Avec le dépôt en place, nous pouvons commencer à écrire du code React, que nous ferons à l'intérieur du fichier *index.js*.

Commençons par le composant principal, `App`. Ce sera notre seul composant "intelligent", car il gérera les données et la connexion avec l'API. Voici la configuration de base (avant d'avoir ajouté de la logique) :

```jsx
    class App extends React.Component {
      
      render() {
        return (
          <div className="app">
            <Title />
            <MessageList />
            <SendMessageForm />
         </div>
        )
      }
    }

```

Comme vous pouvez le voir, il rend simplement trois enfants : les composants `<Title>`, `<MessageList>`, et `<SendMessageForm>`.

Nous allons le rendre un peu plus complexe, car les messages de chat devront être stockés dans l'_état_ de ce composant `App`. Cela nous permettra d'accéder aux messages via `this.state.messages`, et ainsi de les transmettre à d'autres composants.

Nous commencerons par utiliser des données factices afin de comprendre le flux de données de l'application. Ensuite, nous les remplacerons par des données réelles de l'API [Chatkit](https://pusher.com/chatkit) plus tard.

Créons une variable `DUMMY_DATA` :

```jsx
    const DUMMY_DATA = [
      {
        senderId: "perborgen",
        text: "qui va gagner ?"
      },
      {
        senderId: "janedoe",
        text: "qui va gagner ?"
      }
    ]

```

Ensuite, nous ajouterons ces données à l'état de `App` et les transmettrons au composant `MessageList` en tant que prop.

```jsx
    class App extends React.Component {
      
      constructor() {
        super()
        this.state = {
           messages: DUMMY_DATA
        }
      }
      
      render() {
        return (
          <div className="app">
            <MessageList messages={this.state.messages}/>
            <SendMessageForm />
         </div>
        )
      }
    }

```

Ici, nous initialisons l'état dans le `constructor` et nous transmettons également `this.state.messages` à `MessageList`.

Notez que nous appelons `super()` dans le constructeur. Vous devez le faire si vous voulez créer un composant avec état.

### Étape 4 : Affichage des messages factices

Voyons comment nous pouvons afficher ces messages dans le composant `MessageList`. Voici à quoi il ressemble :

```jsx
    class MessageList extends React.Component {
      render() {
        return (
          <ul className="message-list">                 
            {this.props.messages.map(message => {
              return (
               <li key={message.id}>
                 <div>
                   {message.senderId}
                 </div>
                 <div>
                   {message.text}
                 </div>
               </li>
             )
           })}
         </ul>
        )
      }
    }

```

C'est ce qu'on appelle un composant stupide. Il prend une prop, `messages`, qui contient un tableau d'objets. Ensuite, nous affichons simplement les propriétés `text` et `senderId` des objets.

Avec nos données factices circulant dans ce composant, il affichera ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nf12vqc4Ti_GWY0FwqmQKw.png)

Nous avons donc maintenant la structure de base de notre application, et nous sommes également capables d'afficher des messages. Excellent travail !

**Maintenant, remplaçons nos données factices par des messages réels d'une salle de chat !**

### Étape 5 : Récupération des clés API de Chatkit

Pour récupérer des messages, nous devons nous connecter à l'API Chatkit. Et pour ce faire, nous devons obtenir des clés API.

À ce stade, je vous encourage à suivre mes étapes afin que vous puissiez faire fonctionner votre propre application de chat. Vous pouvez utiliser mon [terrain de jeu Scrimba](https://scrimba.com/c/crVznf6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article) afin de tester vos propres clés API.

Commencez par créer un compte gratuit [ici](https://pusher.com/chatkit#sign-up). Une fois que vous l'avez fait, vous verrez votre tableau de bord. C'est ici que vous créez de nouvelles instances Chatkit. Créez-en une et donnez-lui le nom que vous voulez :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-72.png)

Ensuite, vous serez redirigé vers votre nouvelle instance. Ici, vous devrez copier quatre valeurs :

* Localisateur d'instance
* Fournisseur de jeton de test
* Identifiant de salle
* Nom d'utilisateur

Nous commencerons par le **Localisateur d'instance** :

![Vous pouvez copier en utilisant l'icône sur le côté droit du Localisateur d'instance.](https://cdn-media-1.freecodecamp.org/images/1*AkbH5NfvHfwHAxiun37k9g.png)

_Vous pouvez copier en utilisant l'icône sur le côté droit du Localisateur d'instance._

Et si vous faites défiler un peu vers le bas, vous trouverez le **Fournisseur de jeton de test** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uSvabQgYrppTGsWKXQsJSQ.png)

L'étape suivante consiste à créer un **Utilisateur** et une **Salle**, ce qui se fait sur la même page. Notez que vous devrez d'abord créer un utilisateur, puis vous pourrez créer une salle, ce qui vous donnera accès à l'identifiant de la salle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hCXjDJ3PQJ_emU4WfJRQEQ.png)

Vous avez donc trouvé vos quatre identifiants. Bien joué !

Cependant, avant de retourner à la base de code, je veux que vous envoyiez manuellement un message depuis le tableau de bord Chatkit, car cela nous aidera dans le prochain chapitre.

Voici comment faire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HU3mzUknYj8_MwY7ceK2Ow.png)

Cela nous permettra d'avoir un message à afficher à l'étape suivante.

### Étape 6 : Affichage des vrais messages de chat

Maintenant, retournons à notre fichier _index.js_ et stockons ces quatre identifiants en tant que variables en haut de notre fichier.

Voici les miens, mais je vous encourage à créer les vôtres :

```jsx
    const instanceLocator = "v1:us1:dfaf1e22-2d33-45c9-b4f8-31f634621d24"

    const testToken = "https://us1.pusherplatform.io/services/chatkit_token_provider/v1/dfaf1e22-2d33-45c9-b4f8-31f634621d24/token"

    const username = "perborgen"

    const roomId = 9796712

```

Et avec cela en place, nous sommes enfin prêts à nous connecter à Chatkit. Cela se fera dans le composant `App`, et plus précisément dans la méthode `componentDidMount`. C'est la méthode à utiliser lors de la connexion des composants React.js aux API.

Tout d'abord, nous créerons un `chatManager` :

```jsx
    componentDidMount() {
      const chatManager = new Chatkit.ChatManager({
        instanceLocator: instanceLocator,
        userId: userId,
        tokenProvider: new Chatkit.TokenProvider({
          url: testToken
        })
     })  

```

... et ensuite nous ferons `chatManager.connect()` pour nous connecter à l'API :

```jsx
      chatManager.connect().then(currentUser => {
          currentUser.subscribeToRoom({
          roomId: roomId,
          hooks: {
            onNewMessage: message => {
              this.setState({
                messages: [...this.state.messages, message]
              })
            }
          }
        })
      })
    }

```

Cela nous donne accès à l'objet `currentUser`, qui est l'interface pour interagir avec l'API.

Note : Comme nous aurons besoin d'utiliser `currentUser` plus tard, nous le stockerons sur l'instance en faisant `this.currentUser = currentUser`.

Ensuite, nous appelons `currentUser.subscribeToRoom()` et lui passons notre `roomId` et un hook `onNewMessage`.

Le hook `onNewMessage` est déclenché chaque fois qu'un nouveau message est diffusé dans la salle de chat. Ainsi, chaque fois que cela se produit, nous ajouterons simplement le nouveau message à la fin de `this.state.messages`.

Cela permet à l'application de récupérer les données de l'API et de les afficher sur la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EAi9TyUba39xN3fciic3aA.png)

C'est génial, car nous avons maintenant le squelette de notre connexion client-serveur.

Hourra !

### Étape 7 : Gestion de l'entrée utilisateur

La prochaine chose que nous devons créer est le composant `SendMessageForm`. Ce sera un composant contrôlé, ce qui signifie que le composant contrôle ce qui est rendu dans le champ de saisie via son état.

Jetez un coup d'œil à la méthode `render()`, et portez une attention particulière aux lignes que j'ai mises en évidence :

```jsx
    class SendMessageForm extends React.Component {
      render() {
        return (
          <form
            className="send-message-form">
            <input
              onChange={this.handleChange}
              value={this.state.message}
              placeholder="Tapez votre message et appuyez sur ENTRÉE"
              type="text" />
          </form>
        )
      }
    }

```

Nous faisons deux choses :

1. Écouter les entrées utilisateur avec l'écouteur d'événements `onChange`, afin de pouvoir déclencher la méthode `handleChange`
2. Définir la `value` du champ de saisie explicitement en utilisant `this.state.message`

La connexion entre ces deux étapes se trouve à l'intérieur de la méthode `handleChange`. Elle met simplement à jour l'état avec ce que l'utilisateur tape dans le champ de saisie :

```jsx
    handleChange(e) {
      this.setState({
        message: e.target.value
      })
    }

```

Cela déclenche un nouveau rendu, et puisque le champ de saisie est défini explicitement à partir de l'état en utilisant `value={this.state.message}`, le champ de saisie sera mis à jour.

Ainsi, même si l'application semble instantanée pour l'utilisateur lorsqu'il tape quelque chose dans le champ de saisie, **les données passent en réalité par l'état avant que React ne mette à jour l'interface utilisateur.**

Pour finaliser cette fonctionnalité, nous devons donner au composant un `constructor`. Dans celui-ci, nous initialiserons l'état et lierons `this` dans la méthode `handleChange` :

```jsx
    constructor() {
        super()
        this.state = {
           message: ''
        }
        this.handleChange = this.handleChange.bind(this)
    }

```

Nous devons lier la méthode `handleChange` afin d'avoir accès au mot-clé `this` à l'intérieur de celle-ci. C'est ainsi que fonctionne JavaScript : le mot-clé `this` est par défaut _indéfini_ à l'intérieur du corps d'une fonction.

### Étape 8 : Envoi de messages

Notre composant `SendMessageForm` est presque terminé, mais nous devons également gérer la soumission du formulaire. Nous devons récupérer les messages et les envoyer !

Pour ce faire, nous allons associer un gestionnaire d'événements `handleSubmit` à l'écouteur d'événements `onSubmit` dans le `<form>`.

```jsx
    render() {
        return (
          <form
            onSubmit={this.handleSubmit}
            className="send-message-form">
            <input
              onChange={this.handleChange}
              value={this.state.message}
              placeholder="Tapez votre message et appuyez sur ENTRÉE"
              type="text" />
        </form>
        )
      }

```

Comme nous avons la valeur du champ de saisie stockée dans `this.state.message`, il est en fait assez facile de transmettre les données correctes avec la soumission. Nous allons simplement faire :

```jsx
    handleSubmit(e) {
      e.preventDefault()
      this.props.sendMessage(this.state.message)
      this.setState({
        message: ''
      })
    }

```

Ici, nous appelons la prop `sendMessage` et passons `this.state.message` en tant que paramètre. Vous pourriez être un peu confus par cela, car nous n'avons pas encore créé la méthode `sendMessage`. Cependant, nous le ferons dans la section suivante, car cette méthode réside dans le composant `App`. Donc ne vous inquiétez pas !

Deuxièmement, nous vidons le champ de saisie en définissant `this.state.message` sur une chaîne vide.

Voici l'ensemble du composant `SendMessageForm`. Remarquez que nous avons également lié `this` à la méthode `handleSubmit` :

```jsx
    class SendMessageForm extends React.Component {
      constructor() {
        super()
        this.state = {
          message: ''
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
      }

      handleChange(e) {
        this.setState({
          message: e.target.value
        })
      }

      handleSubmit(e) {
        e.preventDefault()
        this.props.sendMessage(this.state.message)
        this.setState({
          message: ''
        })
      }

      render() {
        return (
          <form
            onSubmit={this.handleSubmit}
            className="send-message-form">
            <input
              onChange={this.handleChange}
              value={this.state.message}
              placeholder="Tapez votre message et appuyez sur ENTRÉE"
              type="text" />
          </form>
        )
      }
    }

```

### Étape 9 : Envoi des messages à Chatkit

Nous sommes maintenant prêts à envoyer les messages à Chatkit. Cela se fait dans le composant `App`, où nous créerons une méthode appelée `this.sendMessage` :

```jsx
    sendMessage(text) {
      this.currentUser.sendMessage({
        text: text,
        roomId: roomId
      })
    }

```

Elle prend un paramètre (le texte) et appelle simplement `this.currentUser.sendMessage()`.

La dernière étape consiste à transmettre cela au composant `<SendMessageForm>` en tant que prop :

```jsx
    /* Composant App */
      
    render() {
      return (
        <div className="app">
          <Title />
          <MessageList messages={this.state.messages} />
          <SendMessageForm sendMessage={this.sendMessage} />
      )
    }

```

Et avec cela, nous avons transmis le gestionnaire afin que `SendMessageForm` puisse l'invoquer lorsque le formulaire est soumis.

### Étape 10 : Création du composant Title

Pour terminer, créons également le composant Title. C'est simplement un composant fonctionnel, c'est-à-dire une fonction qui retourne une expression JSX.

```jsx
    function Title() {
      return <p class="title">Mon application de chat géniale</p>
    }

```

C'est une bonne pratique d'utiliser des composants fonctionnels, car ils ont plus de contraintes que les composants de classe, ce qui les rend moins sujets aux bugs.

### Le résultat

Et avec cela en place, vous avez votre propre application de chat que vous pouvez utiliser pour discuter avec vos amis !

![Image](https://cdn-media-1.freecodecamp.org/images/1*KQzdlJJLMGyq5IdZu6cZ1Q.png)

Félicitez-vous si vous avez codé jusqu'à la fin.

Si vous voulez apprendre à développer davantage cet exemple, [consultez mon cours gratuit sur comment créer une application de chat avec React ici.](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_10_minute_article)

Merci d'avoir lu et bon codage :)