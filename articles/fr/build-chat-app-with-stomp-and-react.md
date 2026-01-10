---
title: 'Comment utiliser RxStomp avec React : Créer une application de chat'
subtitle: ''
author: Harsh Deep
co_authors: []
series: null
date: '2024-10-23T14:02:10.236Z'
originalURL: https://freecodecamp.org/news/build-chat-app-with-stomp-and-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729648105968/2926c346-0058-4a84-981e-2ff4bd6833df.png
tags:
- name: React
  slug: reactjs
- name: websocket
  slug: websocket
- name: Chat
  slug: chat
seo_title: 'Comment utiliser RxStomp avec React : Créer une application de chat'
seo_desc: STOMP is an amazingly simple yet powerful protocol for sending messages
  implemented by popular servers like RabbitMQ, ActiveMQ, and Apollo. Using STOMP
  over WebSocket is a straightforward protocol, making it a popular choice for sending
  messages from...
---

STOMP est un protocole incroyablement simple mais puissant pour envoyer des messages, implémenté par des serveurs populaires comme RabbitMQ, ActiveMQ et Apollo. L'utilisation de STOMP sur WebSocket est un protocole simple, ce qui en fait un choix populaire pour envoyer des messages depuis un navigateur web, car des protocoles comme AMQP sont limités par le blocage des connexions TCP par les principaux navigateurs.

Pour utiliser STOMP sur WebSocket, vous pouvez utiliser [@stomp/stompjs](https://www.npmjs.com/package/@stomp/stompjs), mais cela implique des callbacks compliqués et une API complexe qui répond à des cas d'utilisation plus spécialisés. Heureusement, il existe également le moins connu [@stomp/rx-stomp](https://www.npmjs.com/package/@stomp/rx-stomp) qui offre une interface agréable via les observables [RxJS](https://www.npmjs.com/package/rxjs). Les observables ne sont pas exclusifs à Angular, et ils s'intègrent très bien avec le fonctionnement de React. C'est une interface pratique pour composer des flux de travail et des pipelines complexes avec de nombreuses sources de messages différentes.

Ce tutoriel suit un chemin quelque peu similaire à la version initiale en [Angular](https://stomp-js.github.io/guide/rx-stomp/rx-stomp-with-angular.html), mais la structure des composants et le style de code sont adaptés au style fonctionnel de React.

**Note :** Ce tutoriel est écrit avec TypeScript en mode `strict`, mais le code JavaScript est presque identique puisque nous n'avons que 5 déclarations de types. Pour la version JS, vous pouvez ignorer les imports et les définitions de types.

## Table des matières

* [Objectifs](#heading-objectifs)
    
* [Prérequis](#heading-prerequis)
    
* [Serveur STOMP de démarrage avec RabbitMQ](#heading-serveur-stomp-de-demarrage-avec-rabbitmq)
    
* [Modèle React de démarrage](#heading-modele-react-de-demarrage)
    
* [Comment installer RxStomp](#heading-comment-installer-rxstomp)
    
* [Comment gérer la connexion et la déconnexion avec le serveur STOMP](#heading-comment-gerer-la-connexion-et-la-deconnexion-avec-le-serveur-stomp)
    
* [Comment surveiller l'état de la connexion](#heading-comment-surveiller-letat-de-la-connexion)
    
* [Comment envoyer des messages](#heading-comment-envoyer-des-messages)
    
* [Comment recevoir des messages](#heading-comment-recevoir-des-messages)
    
* [Résumé](#heading-resume)
    

## Objectifs

Ici, nous allons construire une application de chat simplifiée qui montre divers aspects de RxStomp à travers différents composants. Globalement, nous voulons avoir :

* Un frontend React connecté avec RxStomp à un serveur STOMP.
    
* Un affichage en direct de l'état de la connexion basé sur notre connexion au serveur STOMP.
    
* Une logique Pub/Sub pour tout sujet configurable.
    
* La répartition de la logique RxStomp sur plusieurs composants pour montrer comment séparer la logique et les responsabilités.
    
* L'alignement des cycles de vie de la connexion/abonnements RxStomp avec les cycles de vie des composants React pour garantir qu'il n'y a pas de fuites ou d'observateurs non fermés.
    

## Prérequis

* Vous devez avoir un serveur STOMP en cours d'exécution afin que l'application React puisse s'y connecter. Ici, nous utiliserons RabbitMQ avec l'extension `rabbitmq_web_stomp`.
    
* La dernière version de React. Ce tutoriel utilisera la v18, bien que les versions plus anciennes devraient également fonctionner.
    
* Une certaine familiarité avec les observables sera également utile.
    

## Serveur STOMP de démarrage avec RabbitMQ

Si vous souhaitez également utiliser RabbitMQ (ce n'est pas strictement nécessaire), voici des [guides d'installation pour différents systèmes d'exploitation](https://www.rabbitmq.com/docs/download). Pour ajouter l'extension, vous devrez exécuter :

```bash
$ rabbitmq-plugins enable rabbitmq_web_stomp
```

Si vous pouvez utiliser `Docker`, un fichier Docker similaire à [celui-ci](https://github.com/harsh183/rabbitmq-intro/blob/master/code_examples/Dockerfile) configurera tout ce qui est nécessaire pour le tutoriel :

```bash
FROM rabbitmq:3.8.8-alpine

run rabbitmq-plugins enable --offline rabbitmq_web_stomp

EXPOSE 15674
```

## Modèle React de démarrage

Pour ce tutoriel, nous utiliserons le modèle `react-ts` de [Vite](https://vite.dev/guide/). La partie centrale de notre application sera dans le composant `App`, et nous créerons des composants enfants pour d'autres fonctionnalités STOMP spécifiques.

## Comment installer RxStomp

Nous utiliserons le package npm `@stomp/rx-stomp` :

```bash
$ npm i @stomp/rx-stomp rxjs
```

Cela installera la version `2.0.0`.

**Note :** Ce tutoriel fonctionne toujours sans spécifier explicitement `rxjs` puisque c'est une dépendance sœur, mais il est bon de l'indiquer explicitement.

## Comment gérer la connexion et la déconnexion avec le serveur STOMP

Maintenant, ouvrons **App.tsx** et initialisons notre client `RxStomp`. Puisque le client n'est pas un état qui changera pour le rendu, nous l'envelopperons dans le Hook `useRef`.

```typescript
// src/App.tsx
import { useRef } from 'react'
import { RxStomp } from '@stomp/rx-stomp'

import './App.css'

function App() {
  const rxStompRef = useRef(new RxStomp())
  const rxStomp = rxStompRef.current

  return (
    <>
      <h1>Bonjour RxStomp !</h1>
    </>
  )
}

export default App
```

En supposant les ports et les détails d'authentification par défaut, nous définirons ensuite une configuration pour notre connexion.

```typescript
// src/App.tsx

import { RxStomp } from '@stomp/rx-stomp'
import type { RxStompConfig } from '@stomp/rx-stomp'
...
const rxStompConfig: RxStompConfig = {
  brokerURL: 'ws://localhost:15674/ws',
  connectHeaders: {
    login: 'guest',
    passcode: 'guest',
  },
  debug: (msg) => {
    console.log(new Date(), msg)
  },
  heartbeatIncoming: 0,
  heartbeatOutgoing: 20000,
  reconnectDelay: 200,
}

function App() {
  ...
```

Pour une meilleure expérience de développement, nous avons journalisé tous les messages avec des horodatages dans une console locale et défini des fréquences de temporisation basses. Votre configuration devrait être assez différente pour votre application de production, alors consultez la [documentation RxStompConfig](https://stomp-js.github.io/api-docs/latest/classes/RxStompConfig.html) pour toutes les options disponibles.

Ensuite, nous passerons la configuration à `rxStomp` à l'intérieur d'un Hook `useEffect`. Cela gère l'activation de la connexion parallèlement au cycle de vie du composant.

```typescript
// src/App.tsx
...
function App() {
  const rxStompRef = useRef(new RxStomp())
  const rxStomp = rxStompRef.current

  useEffect(() => {
    rxStomp.configure(rxStompConfig)
    rxStomp.activate()

    return () => { 
      rxStomp.deactivate() 
    }
  })
  ...
```

Bien qu'il n'y ait aucun changement visuel dans notre application, la vérification des logs devrait montrer les logs de connexion et de ping. Voici un exemple de ce à quoi cela devrait ressembler :

```typescript
Date ... >>> CONNECT
login:guest
passcode:guest
accept-version:1.2,1.1,1.0
heart-beat:20000,0

Date ... Received data 
Date ... <<< CONNECTED
version:1.2
heart-beat:0,20000
session:session-EJqaGQijDXqlfc0eZomOqQ
server:RabbitMQ/4.0.2
content-length:0

Date ... connected to server RabbitMQ/4.0.2 
Date ... send PING every 20000ms 
Date ... <<< PONG 
Date ... >>> PING
```

**Note :** Généralement, si vous voyez des logs en double, cela peut être un signe qu'une fonctionnalité de désactivation ou de désabonnement n'a pas été implémentée correctement. React rend chaque composant deux fois dans un environnement de développement pour aider les gens à attraper ces bugs via `React.StrictMode`.

## Comment surveiller l'état de la connexion

RxStomp dispose d'une énumération [RxStompState](https://stomp-js.github.io/api-docs/latest/miscellaneous/enumerations.html#RxStompState) qui représente les états de connexion possibles avec notre courtier. Notre prochain objectif est d'afficher l'état de la connexion dans notre interface utilisateur.

Créons un nouveau composant pour cela appelé `Status.tsx` :

```typescript
// src/Status.tsx
import { useState } from 'react'

export default function Status() {
  const [connectionStatus, setConnectionStatus] = useState('')

  return (
    <>
      <h2>État de la connexion : {connectionStatus}</h2>
    </>
  )
}
```

Nous pouvons utiliser l'observable `rxStomp.connectionState$` pour lier à notre chaîne `connectionStatus`. De manière similaire à l'utilisation de `useEffect`, nous utiliserons l'action de démontage pour `unsubscribe()`.

```typescript
// src/Status.tsx
import { RxStompState } from '@stomp/rx-stomp'
import { useEffect, useState } from 'react'
import type { RxStomp } from '@stomp/rx-stomp'


export default function Status(props: { rxStomp: RxStomp }) {
  const [connectionStatus, setConnectionStatus] = useState('')

  useEffect(() => {
    const statusSubscription = props.rxStomp.connectionState$.subscribe((state) => {
      setConnectionStatus(RxStompState[state])
    })

    return () => {
      statusSubscription.unsubscribe()
    }
  }, [])

  return (
    <>
      <h2>État de la connexion : {connectionStatus}</h2>
    </>
  )
}
```

Pour le visualiser, nous l'incluons dans notre application :

```typescript
// src/App.tsx
import Status from './Status'
...
  return (
    <>
      <h1>Bonjour RxStomp !</h1>

      <Status rxStomp={rxStomp}/>
    </>
  )
```

À ce stade, vous devriez avoir un indicateur visuel fonctionnel à l'écran. Essayez de manipuler en arrêtant le serveur STOMP et voyez si les logs fonctionnent comme prévu.

## Comment envoyer des messages

Créons un simple salon de discussion pour montrer un flux de messagerie simplifié de bout en bout avec le courtier.

Nous pouvons placer la fonctionnalité dans un nouveau composant `Chatroom`. Tout d'abord, nous pouvons créer le composant avec un champ `username` et `message` personnalisé qui est lié aux entrées.

```typescript
// src/Chatroom.tsx
import { useState } from 'react'
import type { RxStomp } from '@stomp/rx-stomp'

export default function Chatroom(props: {rxStomp: RxStomp}) {
  const [message, setMessage] = useState('')
  const [userName, setUserName] = useState(`user${Math.floor(Math.random() * 1000)}`)

  return (
    <>
      <h2>Salon de discussion</h2>

      <label htmlFor='username'>Nom d'utilisateur : </label>
      <input
        type='text'
        name='username'
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
      />

      <label htmlFor='message'>Message : </label>

      <input
        type='text'
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        name='message'
      />
    </>
  )    
}
```

Incluons cela dans notre **App** avec un basculeur pour rejoindre le salon de discussion :

```typescript
// src/App.tsx
import { useEffect, useState, useRef } from 'react'
import Chatroom from './Chatroom'
...
function App() {
  const [joinedChatroom, setJoinedChatroom] = useState(false)
  ...
  return (
    <>
      <h1>Bonjour RxStomp !</h1>

      <Status rxStomp={rxStomp}/>

      {!joinedChatroom && (
        <button onClick={() => setJoinedChatroom(true)}>
          Rejoindre le salon de discussion !
        </button>
      )}

      {joinedChatroom && (
        <>
          <button onClick={() => setJoinedChatroom(false)}>
            Quitter le salon de discussion !
          </button>

          <Chatroom rxStomp={rxStomp}/>
        </>
      )}

    </>
  )
```

Il est temps d'envoyer réellement des messages. STOMP est idéal pour envoyer des messages basés sur du texte (les données binaires sont également possibles). Nous définirons la structure des données que nous envoyons dans un nouveau fichier **types** :

```typescript
// types.ts
interface ChatMessage {
  userName: string,
  message: string
}
```

**Note :** Si vous n'utilisez pas TypeScript, vous pouvez ignorer l'ajout de cette définition de type.

Ensuite, utilisons JSON pour séquentialiser le message et envoyer des messages à notre serveur STOMP en utilisant `.publish` avec un sujet de destination et notre `body` JSON.

```typescript
// src/Chatroom.tsx
import type { ChatMessage } from './types'
...
const CHATROOM_NAME = '/topic/test'

export default function Chatroom(props: {rxStomp: RxStomp}) {
  ...
  function sendMessage(chatMessage: ChatMessage) {
    const body = JSON.stringify({ ...chatMessage })
    props.rxStomp.publish({ destination: CHATROOM_NAME, body })
    console.log(`Envoyé ${body}`)
    setMessage('')
  }

  return (
    <>
      <h2>Salon de discussion</h2>

      <label htmlFor="username">Nom d'utilisateur : </label>
      <input
        type="text"
        name="username"
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
      />

      <label htmlFor="message">Message : </label>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        name="message"
      />

      <button onClick={() => sendMessage({userName, message})}>Envoyer le message</button>
    </>
  )
}
```

Pour le tester, essayez de cliquer sur le bouton **Envoyer le message** plusieurs fois et voyez si la séquentialisation fonctionne correctement. Bien que vous ne puissiez pas encore voir de changements visuels, les logs de la console devraient les montrer :

```typescript
Date ... >>> SEND
destination:/topic/test
content-length:45

Sent {"userName":"user722","message":"1234567890"}
```

## Comment recevoir des messages

Nous allons créer un nouveau composant pour afficher la liste des messages de tous les utilisateurs. Pour l'instant, nous utiliserons le même type, passerons le nom du sujet en tant que prop, et afficherons tout sous forme de liste. Tout cela va dans un nouveau composant appelé `MessageList`.

```typescript
// src/MessageDisplay.tsx
import { useEffect, useState } from 'react'
import type { RxStomp } from '@stomp/rx-stomp'
import type { ChatMessage } from './types'

export default function MessageDisplay(props: {rxStomp: RxStomp, topic: string}) {
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([
    {userName: 'admin', message: `Bienvenue dans la salle ${props.topic} !`}
  ])

  return(
  <>
  <h2>Messages de discussion</h2>
  <ul>
    {chatMessages.map((chatMessage, index) => 
      <li key={index}>
        <strong>{chatMessage.userName}</strong>: {chatMessage.message}
      </li>
    )}
  </ul>
  </>
  )
}
```

Il est temps de tout rassembler !

Nous pouvons afficher nos messages à afficher dans notre composant `Chatroom` en l'ajoutant en bas.

```typescript
// src/Chatroom.tsx
import { useState } from 'react'
import type { ChatMessage } from './types'
import type { RxStomp } from '@stomp/rx-stomp'

import MessageDisplay from './MessageDisplay'

export const CHATROOM_NAME = '/topic/test'

export default function Chatroom(props: {rxStomp: RxStomp}) {
  const [message, setMessage] = useState('')
  const [userName, setUserName] = useState(`user${Math.floor(Math.random() * 1000)}`)

  function sendMessage(chatMessage: ChatMessage) {
    const body = JSON.stringify({ ...chatMessage })
    props.rxStomp.publish({ destination: CHATROOM_NAME, body })
    console.log(`Envoyé ${body}`)
    setMessage('')
  }

  return (
    <>
      <h2>Salon de discussion</h2>

      <label htmlFor='username'>Nom d'utilisateur : </label>
      <input
        type='text'
        name='username'
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
      />

      <label htmlFor='message'>Message : </label>

      <input
        type='text'
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        name='message'
      />

      <button onClick={() => sendMessage({userName, message})}>Envoyer le message</button>

      <MessageDisplay rxStomp={props.rxStomp} topic={CHATROOM_NAME} />
    </>
  )
}
```

Et une fois que vous avez vérifié que l'affichage statique fonctionne localement, nous pouvons rendre cet affichage dynamique en utilisant un Observable RxJS pour recevoir nos messages de discussion.

De manière similaire à la gestion de l'abonnement avec le composant `Status`, nous configurons l'abonnement au montage et nous désabonnons au démontage.

En utilisant le `pipe` et `map` de RxJS, nous pouvons désérialiser notre JSON en notre `ChatMessage`. La conception modulaire peut vous permettre de configurer un pipeline plus compliqué si nécessaire en utilisant les opérateurs `RxJS`.

```typescript
// src/MessageDisplay.tsx
...
import { map } from 'rxjs'

export default function MessageDisplay(props: {rxStomp: RxStomp, topic: string}) {
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([
    {userName: 'admin', message: `Bienvenue dans la salle ${props.topic} !`}
  ])

  useEffect(() => {
    const subscription = props.rxStomp
      .watch(props.topic)
      .pipe(map((message) => JSON.parse(message.body)))
      .subscribe((message) => setChatMessages((chatMessages) => [...chatMessages, message]))

    return () => {
      subscription.unsubscribe()
    }
  }, [])

  ...
```

À ce stade, l'interface graphique du chat devrait afficher les messages correctement, et vous pouvez expérimenter en ouvrant plusieurs onglets en tant qu'utilisateurs différents.

Une autre chose à essayer ici est d'éteindre le serveur STOMP, d'envoyer quelques messages, puis de le rallumer. Les messages devraient être mis en file d'attente localement et envoyés une fois que le serveur est prêt. Sympa !

## Résumé

Dans ce tutoriel, nous avons :

* Installé `@stomp/rx-stomp` pour une bonne expérience de développement.
    
* Configuré `RxStompConfig` pour configurer notre client avec les détails de connexion, la journalisation du débogueur et les paramètres du temporisateur.
    
* Utilisé `rxStomp.activate` et `rxStomp.deactivate` pour gérer le cycle de vie principal du client.
    
* Surveillé l'état de l'abonnement en utilisant l'observable `rxStomp.connectionState$`.
    
* Publié des messages en utilisant `rxStomp.publish` avec des destinations configurables et des corps de messages.
    
* Créé un observable pour un sujet donné en utilisant `rxStomp.watch`.
    
* Utilisé à la fois les logs de la console et les composants React pour voir la bibliothèque en action, et vérifier la fonctionnalité et la tolérance aux pannes.
    

Vous pouvez trouver le code final sur Gitlab : [https://gitlab.com/harsh183/rxstomp-react-tutorial](https://gitlab.com/harsh183/rxstomp-react-tutorial). N'hésitez pas à l'utiliser comme modèle de départ et à signaler tout problème qui pourrait survenir.