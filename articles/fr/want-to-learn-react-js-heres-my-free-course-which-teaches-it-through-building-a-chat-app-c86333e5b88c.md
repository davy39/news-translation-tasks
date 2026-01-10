---
title: Un cours React gratuit qui développera vos compétences React JS en construisant
  une application de chat
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T13:58:01.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-react-js-heres-my-free-course-which-teaches-it-through-building-a-chat-app-c86333e5b88c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ik3tRrwdvnBFu3_B0rpimw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: Un cours React gratuit qui développera vos compétences React JS en construisant
  une application de chat
seo_desc: 'By Per Harald Borgen


  Chat is eating the world, and React is eating front-end development. So what could
  be better than learning React through building chat app? In my latest course at
  Scrimba, you’ll do exactly that.

  It consists of 17 interactive le...'
---

Par Per Harald Borgen

![Cliquez sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*NE_xQlf9WZkO3LTpxG5TNA.png)

Le chat envahit le monde, et React domine le développement front-end. Alors, quoi de mieux que d'apprendre React en construisant une application de chat ? Dans mon dernier cours sur Scrimba, vous ferez exactement cela.

Il se compose de 17 leçons interactives (plus une introduction et une conclusion) et de cinq défis dans lesquels vous devrez modifier le code vous-même.

Et la meilleure partie : tout se fait dans le navigateur. Vous n'avez pas à écrire de code côté serveur. L'API [Chatkit](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post) s'occupe des tâches lourdes côté back-end, afin que nous puissions nous concentrer sur la construction du client de chat.

À la fin du cours, vous aurez votre propre application de chat personnalisée, qui inclut plusieurs salles, la possibilité de créer de nouvelles salles, le défilement automatique, et plus encore. De plus, elle sera très facilement personnalisable grâce à CSS Grid et aux variables CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ik3tRrwdvnBFu3_B0rpimw.png)

Je suppose que vous connaissez JavaScript et que vous avez déjà vu un peu de React (par exemple, lu mon [article d'introduction de cinq minutes](https://medium.freecodecamp.org/learn-react-js-in-5-minutes-526472d292f4), et peut-être consulté quelques tutoriels). Mais à part cela, il n'y a pas de prérequis pour le cours.

Maintenant, jetons un coup d'œil à la manière dont il est structuré !

### Leçon #1 : Introduction au cours

![Image](https://cdn-media-1.freecodecamp.org/images/1*zcRbKlNUmWNxStHWrQJEOw.png)

Je commencerai par vous donner une rapide introduction au cours. Nous passerons en revue ce que vous apprendrez, et je me présenterai également. Je vous donnerai également un aperçu de la manière dont vous pourrez personnaliser votre propre application de chat à la fin du cours.

### Leçon #2 : Architecture des composants

![Image](https://cdn-media-1.freecodecamp.org/images/1*JD33BOZnuutza8G_trur1A.png)

Avant de commencer à construire une application React, vous devriez commencer par obtenir une vue d'ensemble de l'architecture des composants, et ainsi décomposer l'interface utilisateur en composants. Donc, dans cette leçon, je vous montrerai comment faire exactement cela.

### Leçon #3 : Architecture de la base de code

![Image](https://cdn-media-1.freecodecamp.org/images/1*xr6dWMCFWVA942U1w2r90Q.png)

Ensuite, nous verrons comment notre architecture de composants se traduit en code. Je jetterai également un coup d'œil à la manière dont le reste du dépôt est configuré, car je ne veux pas que vous soyez confus à propos des divers fichiers dans le dépôt une fois que nous commencerons à coder.

Je ne créerai pas le dépôt à partir de zéro, car il existe de nombreux tutoriels qui vous aident à configurer votre environnement de développement, et ce n'est pas vraiment ce pour quoi la plateforme Scrimba est la mieux adaptée.

### Leçon #4 : Composant MessageList

Maintenant, nous sommes enfin prêts à commencer à coder, donc dans cette leçon, nous allons rendre des données factices dans notre composant `MessageList`. Cela vous introduira à JSX, et vous apprendrez à créer dynamiquement des éléments en utilisant, par exemple, la méthode de tableau `map()`.

```js
{DUMMY_DATA.map((message, index) => {  
   return (  
     <div key={index} className="message">  
        <div className="message-username">{message.senderId}</div>  
        <div className="message-text">{message.text}</div>  
     </div>  
   )  
})}

```

Dans cette leçon, vous aurez également votre tout premier défi !

### Leçon #5 : Introduction à Chatkit

[!Cliquez sur l'image pour accéder à l'API Chatkit.]([https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post))  
Cliquez sur l'image pour accéder à l'API Chatkit.

Maintenant que nous sommes capables de rendre des données sur la page, nous allons commencer à intégrer l'API [Chatkit](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post), qui s'occupera du back-end de l'application. Dans cette leçon, je vous donne un rapide aperçu de l'API.

### Leçon #6 : Connexion à Chatkit

![Image](https://cdn-media-1.freecodecamp.org/images/1*dRgHCdd44zgpOOFoqPwRPg.png)

Ensuite, nous allons simplement coder l'intégration de [Chatkit](https://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=announcment-post), ce qui est super simple : le code ci-dessus est tout ce dont vous avez besoin pour commencer à récupérer des messages d'une salle de chat. Vous serez exposé à la méthode de cycle de vie `componentDidMount()` de React, qui est l'endroit où vous devez connecter votre composant avec des API tierces.

### Leçon #7 : État et props

L'état et les props sont les deux façons dont nous gérons les données dans React, et vous devez comprendre la différence entre les deux. Dans cette leçon, nous aurons besoin d'utiliser les deux types, car nous stockerons les messages de chat dans l'état de notre composant `App` et nous les passerons également en tant que props au composant `MessageList`.

```js
constructor() {  
  super()  
  this.state = {  
    messages: []  
  }  
}

```

### Leçon #8 : Le composant Message

Dans cette leçon, nous construirons le composant Message. Il a une seule tâche : rendre le nom d'utilisateur et le texte qui lui sont passés par ses parents. Je vous donnerai également un défi pour le transformer d'un composant basé sur une classe en un composant fonctionnel.

```jsx
function Message(props) {  
  return (  
    <div className="message">  
      <div className="message-username">{props.username}</div>  
      <div className="message-text">{props.text}</div>  
    </div>  
  )  
}

```

### Leçon #9 : Le composant SendMessageForm

![Image](https://cdn-media-1.freecodecamp.org/images/1*bYkfM_KQ54Qxyh41g-XnvQ.png)

Vous ne pouvez pas avoir une application de chat sans un formulaire pour envoyer des messages. Donc, dans cette leçon, nous créerons exactement cela. Cela vous enseignera les composants contrôlés, qui est un concept critique dans React. Cela signifie que le composant lui-même décide de ce qui est rendu dans le champ de saisie, au lieu que le nœud DOM lui-même conserve cet état interne.

### Leçon #10 : Diffusion des messages

```js
sendMessage(text) {  
  this.currentUser.sendMessage({  
    text,  
    roodId: 9434230  
  })  
}

```

Maintenant que nous avons le `SendMessageForm` en place, nous devons envoyer les messages à Chatkit afin qu'il puisse les diffuser. Cela vous forcera à apprendre un autre concept central de React : le flux de données inverse.

Dans React, les données circulent de haut en bas, du parent à l'enfant. Cependant, parfois nous avons besoin que les composants enfants remontent vers leurs parents et déclenchent leurs méthodes, ainsi que certaines données d'eux-mêmes.

### Leçon #11 : Le composant RoomList

![Image](https://cdn-media-1.freecodecamp.org/images/1*rqi85uI26PUeQ_cAJVkbIg.png)

Maintenant que nous avons les fonctionnalités principales du chat en place (envoi et affichage de messages), il est temps de passer au composant `RoomList`, qui affiche toutes les salles disponibles sur votre instance Chatkit.

Cela vous introduira à quelques nouveaux concepts dans Chatkit, ainsi que de consolider vos connaissances sur la manière d'envoyer des données des composants parents aux composants enfants. Nous revisiterons également l'opérateur de propagation ES6, qui est super pratique à connaître lors de la construction d'applications React.js.

### Leçon #12 : S'abonner aux salles

Ensuite, vous devrez apprendre à vous abonner à des salles spécifiques. Nous allons connecter un écouteur d'événements à chacune des salles affichées dans le composant `RoomList`. Cela déclenchera une méthode dans le composant `App`, qui indique à Chatkit que l'utilisateur souhaite s'abonner à cette salle spécifique.

```js
subscribeToRoom(roomId) {  
  this.setState({ messages: [] })  
  this.currentUser.subscribeToRoom({  
    roomId: roomId,  
    hooks: {  
      onNewMessage: message => {  
        this.setState({  
          messages: [...this.state.messages, message]  
        })  
      }  
    }  
  })  
}

```

### Leçon #13 : Ordre des salles et mise en évidence de la salle actuelle

Cette leçon vous introduira à la méthode de tableau `.sort()` en JavaScript, car nous devrons nous assurer que nos salles sont triées dans le bon ordre, peu importe d'où proviennent les données initialement.

const orderedRooms = [...this.props.rooms].sort((a, b) => a.id - b.id)

Nous ajouterons également une classe `active` à la salle dans laquelle nous discutons actuellement afin de la signaler à l'utilisateur.

### Leçon #14 : Ajout du défilement automatique

Le défilement automatique est nécessaire pour sauter automatiquement vers les derniers messages lorsqu'ils apparaissent dans le composant `MessageList`. C'est une petite astuce qui vous introduira aux méthodes de cycle de vie des composants suivantes :

* `componentWillUpdate()`
* `componentDidUpdate()`

Nous devrons également utiliser la méthode `ReactDOM.findDOMNode()`, donc vous apprendrez à connaître celle-ci également.

### Leçon #15 : Le composant NewRoomForm

Ce composant vous permet de créer de nouvelles salles. Ce sera un rappel sur les composants contrôlés de la neuvième leçon.

Avec cela, nous avons terminé tout le code React pour l'application. Donc, pour le reste du cours, nous nous concentrerons sur le design en utilisant CSS.

### Leçon #16 : Création de votre propre application de chat

![Image](https://cdn-media-1.freecodecamp.org/images/1*0N6xXGInxOYIGin0rjkFKg.png)

Avant de commencer à modifier le design de l'application, je veux cloner mon code afin que vous obteniez votre propre copie du dépôt. Cela vous prépare pour les prochains screencasts où vous personnaliserez le design. Je vous guiderai à travers chaque étape jusqu'à ce que vous ayez votre propre copie et des clés API gratuites de Chatkit.

### Leçon #17 : Changement de la mise en page avec CSS Grid

Nous utilisons CSS Grid pour contrôler la mise en page de l'application, ce qui vous offre une flexibilité super agréable lorsque vous souhaitez la modifier, grâce à `grid-template-areas`. Je vous montrerai comment vous pouvez déplacer des éléments sur la page en changeant simplement quelques lignes de CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yAyieAB9wQk-s2lJbO4Ybw.png)

### Leçon #18 : Changement du thème avec les variables CSS

![Image](https://cdn-media-1.freecodecamp.org/images/1*23UzFS7KCSj9d0Ten6WZsw.png)

![Avant et après la modification des variables.](https://cdn-media-1.freecodecamp.org/images/1*RTHSzUyGjN8H5VyFJnzVZA.png)

  
Avant et après la modification des variables.

Comme nous utilisons des variables CSS pour nos couleurs, vous pouvez également changer très facilement le thème de l'application. Ici, je vous donnerai le défi de trouver une belle palette en ligne et de l'implémenter dans votre application.

Si vous combinez les changements de mise en page de la leçon précédente avec une nouvelle palette dans celle-ci, vous aurez votre propre application de chat personnalisée ! En voici une que j'ai faite pour moi, juste pour le plaisir :

![Image](https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png)

### Leçon #19 : Conclusion et défis finaux

Si vous arrivez jusqu'ici : félicitations ! Vous avez vraiment investi dans l'amélioration de vos compétences, et je suis sûr à 100 % que cela portera ses fruits. Dans ce screencast, je vous donne quelques défis finaux que vous pouvez faire si vous êtes vraiment motivé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rk3YHJTml0Au8SzkZgN-CA.png)

Si vous avez été satisfait du [cours](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_free_course), nous vous serions vraiment reconnaissants si vous le recommandiez à un ami ou le partagiez sur les réseaux sociaux, car c'est ainsi que les gens découvrent nos cours gratuits Scrimba.

Bonne chance avec le cours, et bon codage :)