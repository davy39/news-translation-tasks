---
title: Comment ajouter un chat en direct à vos applications avec Rocket.Chat
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2025-04-07T13:26:13.790Z'
originalURL: https://freecodecamp.org/news/add-live-chat-to-your-applications-with-rocketchat
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744032217209/1ad8ea61-a8bd-4bea-9bec-152e52db7377.png
tags:
- name: Web Development
  slug: web-development
- name: chatbot
  slug: chatbot
seo_title: Comment ajouter un chat en direct à vos applications avec Rocket.Chat
seo_desc: 'The fastest way to gather valuable information about your site’s users
  is still by talking to them. And what better way to do this than by adding a chat
  system to your app?

  For my case, I just wanted to add a chat system to my portfolio website so I ...'
---

La manière la plus rapide de recueillir des informations précieuses sur les utilisateurs de votre site est encore de leur parler. Et quelle meilleure façon de le faire qu'en ajoutant un système de chat à votre application ?

Pour ma part, je voulais simplement ajouter un système de chat à mon site portfolio afin de pouvoir obtenir des informations précieuses de la part d'employeurs et de clients potentiels. J'ai fini par construire quelque chose comme ceci :

![Capture d'écran de la démonstration du chat en direct](https://cdn.hashnode.com/res/hashnode/image/upload/v1743755398731/f7bce275-ed01-4e7f-98b6-0eed955dc428.png align="left")

### **Table des matières**

1. [Pourquoi](#pourquoi-rocketchat-pourriez-vous-demander) [Rocket.Chat](http://Rocket.Chat)[, pourriez-vous demander ?](#pourquoi-rocketchat-pourriez-vous-demander)
    
2. [Prérequis](#prerequis)
    
3. [Prise en main](#prise-en-main)
    
    * [Étape 1 : Configurer le](#etape-1-configurer-le-serveur-rocketchat) [serveur Rocket.Chat](#etape-1-configurer-le-serveur-rocketchat)
        
    * [Étape 2 : Configurer le](#etape-2-configurer-le-serveur-rocketchat) [serveur Rocket.Chat](#etape-2-configurer-le-serveur-rocketchat)
        
    * [Étape 3 : Enregistrer le visiteur](#etape-3-enregistrer-le-visiteur)
        
        * [Comment enregistrer le visiteur](#comment-enregistrer-le-visiteur)
            
        * [Comment créer ou récupérer la salle de chat](#comment-creer-ou-recuperer-la-salle-de-chat)
            
        * [Comment récupérer la configuration Livechat](#comment-recuperer-la-configuration-livechat)
            
    * [Étape 4 : Créer la connexion à WebSocket](#etape-4-creer-la-connexion-a-websocket)
        
4. [Conclusion](#conclusion)
    

## Pourquoi Rocket.Chat, pourriez-vous demander ?

Rocket.Chat est une excellente option car :

* **Open Source** : Il est gratuit et personnalisable.
    
* **API complètes** : Leurs API rendent l'intégration simple.
    
* **Hébergement flexible** : Auto-hébergez le vôtre ou utilisez leur version cloud avec un essai gratuit (que nous utiliserons ici).
    

### Prérequis

Avant de continuer, il y a quelques choses que vous devez savoir et avoir :

* Un serveur Rocket.Chat en cours d'exécution (auto-hébergé ou sur Rocket.Chat Cloud). Ici, je vais vous montrer comment en configurer un avec Rocket.Chat Cloud.
    
* Une connaissance pratique des fondamentaux de JavaScript.
    

## Prise en main

Tout d'abord, configurons un serveur Rocket.Chat. Encore une fois, vous pouvez soit l'auto-héberger soit utiliser leur version cloud. Et ne vous inquiétez pas, vous n'avez pas à payer quoi que ce soit pour l'instant ou pour ce tutoriel, car ils fournissent un essai gratuit de 30 jours.

### Étape 1 : Configurer le serveur Rocket.Chat

Rendez-vous sur [https://cloud.rocket.chat](https://cloud.rocket.chat) et créez votre compte gratuit.

Une fois connecté, cliquez sur le bouton **"Passer à l'essai SaaS"** pour lancer un serveur hébergé dans le cloud.

![Bouton Passer à l'essai SaaS](https://cdn.hashnode.com/res/hashnode/image/upload/v1743755542942/1b57e01d-2338-4af7-9a77-9140f65bb1f7.png align="left")

Ensuite, créez un espace de travail Cloud en fournissant le nom de votre espace de travail, l'URL et la région du serveur.

![Capture d'écran de l'espace de travail Cloud Rocket.Chat](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sdorooqpo032qjibt1vp.png align="left")

Cela prendra un peu de temps à configurer. Une fois terminé, vous devriez voir quelque chose de similaire à ceci :

![Capture d'écran du tableau de bord Rocket.Chat](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rcpvsdl49rw9t7bv7vfn.png align="left")

Maintenant, copiez l'URL de votre serveur, elle devrait ressembler à ceci : [`https://example.rocket.chat`](https://example.rocket.chat).

### Étape 2 : Configurer le serveur Rocket.Chat

Avant de plonger dans le code, nous devons configurer notre serveur afin de pouvoir utiliser l'API livechat.

Pour commencer, ouvrez votre serveur Rocket.Chat et cliquez sur le bouton de menu, puis cliquez sur **Omnichannel**.

![Capture d'écran du menu Omnichannel Rocket.Chat](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8cql8hzejwep1zhxxhgg.png align="left")

Cliquez sur **Agents** dans la barre latérale et ajoutez-vous en tant qu'agent.

![Capture d'écran de la section Agents Omnichannel Rocket.Chat](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zsnnbjsbo64h8d5zya8u.png align="left")

Ensuite, cliquez sur **Departments** et créez un département. Je vais appeler le mien **Chats**.

![Capture d'écran de la section Departments Omnichannel Rocket.Chat](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ej4n16odg3iy578ltna0.png align="left")

Maintenant, vous devez configurer quelques éléments concernant le widget Livechat :

* Assurez-vous d'activer le formulaire hors ligne et de définir l'adresse e-mail pour envoyer les messages hors ligne.
    
* Configurez également vos heures d'ouverture aux moments où vous serez disponible.
    

### Étape 3 : Enregistrer le visiteur

Ensuite, nous devons enregistrer le visiteur et créer une salle pour lui. Pour ce faire, vous devez collecter le nom et l'e-mail du visiteur et générer un identifiant unique aléatoire.

#### Comment enregistrer le visiteur

Tout d'abord, nous devons enregistrer le visiteur sur le serveur. Nous avons besoin de son nom, de son e-mail et de son jeton. Vous envoyez ces informations à ce point de terminaison : `/api/v1/livechat/visitor`. Voici un exemple de code que vous pourriez envoyer depuis votre backend :

```js
const body = {
  name: "Nom du visiteur",          // Remplacez par le nom du visiteur
  email: "visiteur@example.com",  // Remplacez par l'e-mail du visiteur
  token: "jeton-visiteur-unique"  // Remplacez par un jeton unique généré
};

fetch(`${process.env.ROCKETCHAT_URL}/api/v1/livechat/visitor`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache'
  },
  body: JSON.stringify(body)
})
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      console.log("Visiteur enregistré :", data);
    } else {
      console.error("Échec de l'enregistrement du visiteur :", data);
    }
  })
  .catch(error => console.error("Erreur lors de l'enregistrement du visiteur :", error));
```

#### Comment créer ou récupérer la salle de chat

Après avoir enregistré le visiteur, vous devez créer une salle pour lui afin qu'il puisse vous envoyer des messages et que vous puissiez répondre.

Appelez ce point de terminaison `/api/v1/livechat/room` avec le jeton du visiteur comme paramètre de requête. Si le visiteur a déjà une salle, elle sera retournée. Sinon, une nouvelle sera créée. Voici comment vous pouvez faire cette demande depuis votre backend :

```js
const token = "jeton-visiteur-unique"; // Remplacez par le jeton réel du visiteur

fetch(`${process.env.ROCKETCHAT_URL}/api/v1/livechat/room?token=${token}`, {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      console.log("Salle récupérée :", data);
    } else {
      console.error("Échec de la récupération de la salle :", data);
    }
  })
  .catch(error => console.error("Erreur lors de la récupération de la salle :", error));
```

#### Comment récupérer la configuration Livechat

Enfin, nous devons obtenir les informations sur le visiteur et l'agent que nous avons enregistrés. Utilisez ce point de terminaison API pour obtenir le jeton du visiteur, l'ID de la salle et les informations sur l'agent. Vous pouvez l'utiliser pour vérifier si l'agent est en ligne avant d'essayer de vous connecter au WebSocket.

```js
const token = "jeton-visiteur-unique"; // Remplacez par le jeton réel du visiteur
const url = `${process.env.ROCKETCHAT_URL}/api/v1/livechat/config?token=${token}`;

fetch(url, {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
})
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      console.log("Configuration Livechat :", data);
    } else {
      console.error("Échec de la récupération de la configuration Livechat :", data);
    }
  })
  .catch(error => console.error("Erreur lors de la récupération de la configuration Livechat :", error));
```

### Étape 4 : Créer la connexion à WebSocket

Pour établir l'expérience de chat en direct, nous devons ouvrir une connexion WebSocket à Rocket.Chat et gérer la messagerie.

#### Exemple de connexion WebSocket

Tout d'abord, ouvrez le WebSocket comme ceci :

```js
const rocketChatSocket = new WebSocket("ws://example.rocket.chat/websocket");
```

Ensuite, connectez-vous :

```js
const connectRequest = {
  msg: "connect",
  version: "1",
  support: ["1", "pre2", "pre1"]
};
rocketChatSocket.send(JSON.stringify(connectRequest));
```

Vous pouvez maintenir la connexion active en répondant aux messages `"ping"` du serveur avec un `"pong"`.

```js
rocketChatSocket.onmessage = (event) => {
  try {
    const data = JSON.parse(event.data);
    if (data.msg === "ping") {
      console.log("Ping reçu du serveur, envoi de pong");
      rocketChatSocket.send(JSON.stringify({ msg: "pong" }));
    }
  } catch (error) {
    console.error("Erreur lors de l'analyse du message WebSocket :", error);
  }
};
```

Vous pouvez vous abonner à la salle créée pour le visiteur. Utilisez simplement le jeton du visiteur et l'ID de la salle des sections précédentes.

```js
const subscribeRequest = {
  msg: "sub",
  id: "id-abonnement-unique", // Remplacez par votre ID unique
  name: "stream-room-messages",
  params: [
    "id-salle-recuperée", // Remplacez par la variable d'ID de salle
    {
      useCollection: false,
      args: [
        { visitorToken: "jeton-visiteur" } // Remplacez par votre variable de jeton de visiteur
      ],
    },
  ],
};
rocketChatSocket.send(JSON.stringify(subscribeRequest));
```

Vous pouvez également écouter les messages entrants. Voici comment vous pouvez traiter les nouveaux messages à leur arrivée :

```js
rocketChatSocket.onmessage = (event) => {
  try {
    const data = JSON.parse(event.data);
    if (
      data.msg === "changed" &&
      data.collection === "stream-room-messages"
    ) {
      // Traiter les nouveaux messages
      if (data.fields && data.fields.args && data.fields.args.length > 0) {
        const newMessage = data.fields.args[0];
        // Supposons que isValidChatMessage est défini pour valider le format du message
        if (isValidChatMessage(newMessage)) {
          // Mettez à jour votre liste de messages ici
          console.log("Nouveau message reçu :", newMessage);
        }
      }
    }
  } catch (error) {
    console.error("Erreur lors de l'analyse du message WebSocket :", error);
  }
};
```

Et si vous voulez envoyer des messages livechat ? Utilisez simplement ce code pour le faire :

```js
const sendMessageRequest = {
  msg: "method",
  method: "sendMessageLivechat",
  params: [
    {
      _id: "id-message-unique",  // Remplacez par un ID unique généré pour le message
      rid: "id-salle",            // Remplacez par l'ID réel de la salle
      msg: "Votre message ici",  // Remplacez par le texte du message que vous souhaitez envoyer
      token: "jeton-visiteur"     // Remplacez par le jeton réel du visiteur
    }
  ],
  id: "id-requete-unique"        // Remplacez par un ID de requête unique
};

rocketChatSocket.send(JSON.stringify(sendMessageRequest));
```

Dans votre implémentation réelle, vous pouvez intégrer ces exemples dans votre logique backend ou côté client selon vos besoins.

Vous pouvez consulter le [code source](https://github.com/iamspruce/resume) pour voir comment je l'ai implémenté avec Next.js ou vous pouvez regarder la démonstration en direct [demo](https://resume-alpha-jet-70.vercel.app).

## Conclusion

Ajouter une fonctionnalité de chat en direct à vos applications web ne devrait pas être difficile. Avec l'API livechat de Rocket.Chat, vous pouvez rapidement intégrer une fonctionnalité de chat et obtenir des informations précieuses de vos utilisateurs. J'ai même créé un [wrapper SDK](https://www.npmjs.com/package/rocketchat-livechat-sdk) pour faciliter son utilisation.

Maintenant, c'est à vous ! Essayez l'API de Rocket.Chat et construisez votre propre système de chat en direct. Vous pouvez explorer davantage dans la [documentation](https://docs.rocket.chat) de Rocket.Chat.

Bon codage !