---
title: Apprenez à créer votre propre application de chat de bureau avec React et Electron,
  étape par étape
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-04T16:51:35.000Z'
originalURL: https://freecodecamp.org/news/build-a-desktop-chat-app-with-react-electron-and-chatkit-744d168e6f2f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-_ZbCJQtclP5tVK3
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Apprenez à créer votre propre application de chat de bureau avec React
  et Electron, étape par étape
seo_desc: 'By Alex Booker

  This tutorial was written in collaboration with the awesome Christian Nwamba.

  When learning to code, you have a bunch of resources at your disposal — books, screencasts,
  tutorials, even exercises. But to become a great developer, you n...'
---

Par Alex Booker

_Cet article a été écrit en collaboration avec le formidable Christian Nwamba._

Lorsque vous apprenez à coder, vous avez une multitude de ressources à votre disposition — livres, screencasts, tutoriels, même des exercices. Mais pour devenir un excellent développeur, vous devez pratiquer ce que vous apprenez avec un projet.

Apprendre en faisant est la motivation de cet article. Vous partirez de zéro et construirez une application de chat complète, étape par étape.

Vous construirez le projet étape par étape et pour tester votre compréhension, nous avons inclus quelques défis bonus spéciaux à la fin. Êtes-vous prêt à relever le défi ?

Voici ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/0*o0ILCOojCdCs4NB0.gif)

Plutôt cool, non ??

Lorsque vous suivez ce tutoriel, vous apprendrez à construire un chat en temps réel, une liste « qui est en ligne » et en cours de route, comment structurer une application React. Pour alimenter notre chat, nous utiliserons un service que j'aide à construire appelé [Chatkit](https://pusher.com/chatkit?utm_source=medium&utm_term=desktop-chat-app-tut).

Ça vous semble bien ? Écoutez [FreeCodeCamp radio](https://youtu.be/twcOr043i4k) pour une musique de fond douce et agréable pour rester concentré et c'est parti !

### Ce que vous devez savoir

En fait, une dernière chose ?:

Il serait bien que vous connaissiez déjà quelques bases de JavaScript, Node et React. Cela dit, si vous ne vous sentez pas à l'aise avec ces technologies, essayez quand même !

Nous avons intentionnellement structuré ce tutoriel pour qu'il soit clair où coller le code afin que vous puissiez suivre. Si vous avez des questions, posez-les ici !

Très bien, première étape :

### Installation d'Electron

Pour construire une application de bureau multiplateforme avec des technologies web, nous utiliserons [Electron](https://electronjs.org/).

Pour nous lancer, nous avons créé un modèle de démarrage minimal. Téléchargez-le :

```
git clone https://github.com/pusher/electron-desktop-starter-template electron-desktop-chat
```

```
cd electron-desktop-chat
```

Et installez les dépendances locales :

```
npm install
```

### Créer un compte Chatkit

Nous ne nous préoccupons pas trop de la construction d'un back-end dans ce tutoriel, nous utiliserons donc [Chatkit](http://pusher.com/chatkit).

Pour suivre ce tutoriel, [créez un compte gratuit](http://pusher.com/chatkit) et une nouvelle instance appelée « Electron desktop chat » :

![Image](https://cdn-media-1.freecodecamp.org/images/0*mIYRakmmplQuXiyI.gif)

Dans la fenêtre des paramètres, activez le fournisseur de jetons de test :

![Image](https://cdn-media-1.freecodecamp.org/images/0*bfFE2Zg1VWukbpkd.gif)

Notez **Votre point de terminaison du fournisseur de jetons de test**, **Localisateur d'instance** et **Clé secrète**. Nous en aurons besoin à l'étape suivante.

### Configuration du serveur Node

Chatkit a deux concepts fondamentaux : [Utilisateurs](https://docs.pusher.com/chatkit/core-concepts#users) et [salles](https://docs.pusher.com/chatkit/core-concepts#rooms).

Les utilisateurs peuvent créer des salles, les rejoindre et discuter dedans. Mais avant qu'un utilisateur puisse interagir avec une salle, nous devons en créer une.

Cela doit se faire sur le serveur.

Dans electron-desktop-chat, exécutez :

```
npm install --save express cors body-parser pusher-chatkit-server
```

Et collez ceci dans un nouveau fichier appelé server.js :

N'oubliez pas de remplacer instanceLocator et key par votre propre **Localisateur d'instance** et **Clé**.

La plupart de ce code est du code standard, importation des dépendances, configuration d'Express, et ainsi de suite.

La partie importante est la route « /users » qui gère les requêtes pour créer un nouvel utilisateur.

Exécutez le serveur avec `node server.js` et vous verrez que le serveur est « En cours d'exécution sur le port 3001 ».

### Créer le formulaire de nom d'utilisateur

Lorsque quelqu'un charge notre application, nous voudrons lui demander un nom d'utilisateur et ensuite l'envoyer à « /users ».

Installez quelques composants d'interface utilisateur natifs avec :

```
npm install --save react-desktop
```

Et créez un composant de formulaire appelé UsernameForm :

Vous pouvez en savoir plus sur les composants de formulaire React [ici](https://reactjs.org/docs/forms.html). Par hasard, la documentation utilise une classe NameForm similaire à la nôtre, donc tout devrait vous être familier !

Ensuite, remplacez tout App par :

Et pour le tester, exécutez `npm run dev`. Vous verrez que le formulaire de nom d'utilisateur est rendu :

![Image](https://cdn-media-1.freecodecamp.org/images/0*yQY4Z9AKtmAV1rvD.png)

Assurez-vous que le serveur est en cours d'exécution (rappelez-vous, la commande est `node server.js`), cliquez sur **Submit**, et vous verrez qu'un utilisateur est créé :

![Image](https://cdn-media-1.freecodecamp.org/images/0*hjNlVMLHXd9VV2Qu.gif)

### Transition entre les écrans sans bibliothèque

Une fois que nous avons un utilisateur, nous pouvons le faire passer du UsernameForm à l'écran de chat réel. Nous devrions le définir maintenant.

Créez un nouveau composant appelé Chat :

Et mettez à jour App :

Exécutez l'application, entrez un nom d'utilisateur, et vous passerez à l'écran de chat :

![Image](https://cdn-media-1.freecodecamp.org/images/0*yz6R-9aO0mtQO8cD.gif)

### Ajouter un chat en temps réel avec Chatkit

Les choses avancent bien, n'est-ce pas ?

Pour se connecter à Chatkit depuis le client, vous devez installer [@pusher/chatkit](https://www.npmjs.com/package/@pusher/chatkit) :

```
npm install --save add @pusher/chatkit
```

Et remplacez tout Chat par :

N'oubliez pas de remplacer les valeurs `tokenProviderUrl` et `instanceLocator` par **Votre point de terminaison du fournisseur de jetons de test** et **Localisateur d'instance**.

Exécutez l'application, appuyez sur ⌘+⇧+I (Ctrl+Maj+I) et vous verrez que vous êtes connecté à Chatkit.

![Image](https://cdn-media-1.freecodecamp.org/images/0*awt3lX7P8-34CD9W.png)

### Créer une salle Chatkit

Nous avons un utilisateur mais maintenant nous avons besoin d'une salle !

Pour en créer une, utilisez l'inspecteur Chatkit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*bjy-pDVLlEf_TwC5.gif)

N'oubliez pas de copier votre ID de salle, nous en aurons besoin à l'étape suivante.

### Créer un composant de salle de chat

Maintenant que nous avons une salle, nous pouvons nous abonner aux nouveaux messages envoyés dans cette salle.

Pour les afficher, créez un composant MessageList :

Et mettez à jour Chat :

Comme toujours, n'oubliez pas de mettre à jour `roomId` avec votre ID de salle réel.

Maintenant, lorsque des messages sont envoyés dans notre salle, `onNewMessage` sera appelé. À partir de là, nous pouvons mettre à jour notre état et, à notre tour, notre interface utilisateur.

Dans un instant, nous permettrons aux utilisateurs d'envoyer leurs propres messages. Pour l'instant, pour tester l'abonnement, utilisez l'inspecteur :

![Image](https://cdn-media-1.freecodecamp.org/images/0*MRLxCyFW8Mi3uydt.gif)

### Envoyer des messages

Pour permettre aux utilisateurs d'envoyer leurs propres messages, créez un composant SendMessageForm :

Et mettez à jour Chat :

Rechargez l'application avec ⌘+R (Ctrl+Maj+R) et vous pourrez envoyer des messages :

![Image](https://cdn-media-1.freecodecamp.org/images/0*iPUvhRR4bH0oeEql.gif)

En fait, pourquoi ne pas ouvrir deux applications côte à côte et avoir une conversation avec vous-même ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*IK1ZRrRPs61nvy0_.gif)

Quelle époque pour être en vie...

### Styliser l'interface utilisateur

Grâce à [React Desktop](http://reactdesktop.js.org/), notre application a déjà l'air décente mais nous pouvons faire mieux.

Apportons quelques ajustements et définissons notre mise en page pour une utilisation dans la prochaine et dernière étape.

Remplacez tout index.css par :

### Montrer qui est en ligne

Pour terminer notre application de chat, nous ajouterons une liste « qui est en ligne » pour montrer, vous l'avez deviné, qui est en ligne !

Créez un composant OnlineList :

Ensuite, mettez à jour Chat :

Vous attendiez-vous à ce que ce soit plus difficile ? Je m'y attendais définitivement la première fois que j'ai essayé !

Parce que Chatkit met à jour la propriété `users` dynamiquement, nous n'avons pas à gérer notre propre état. Nous devons simplement dire à React de se re-rendre et, à son tour, réévaluer `users` chaque fois que quelqu'un se connecte (`onUserCameOnline`), se déconnecte (`onUserWentOffline`) ou rejoint la salle (`onUserJoined`).

Allez-y, exécutez le serveur et le client et admirez votre magnifique nouvelle application de chat :

![Image](https://cdn-media-1.freecodecamp.org/images/0*oFR5EvkwrXoJmt1K.gif)

Si vous êtes arrivé jusqu'ici, vous pourriez aussi bien continuer ! Essayez ces défis bonus...

### Défi 1 : Montrer qui dans la salle est en train de taper activement

Voyez si vous pouvez ajouter des indicateurs de frappe à l'application. Par exemple, si je tape, vous et tout le monde dans la salle verriez « Booker est en train de taper... ».

Si Chris et moi tapions tous les deux, vous verriez « Booker et Chris sont en train de taper... » et ainsi de suite.

Indices :

* [Documentation sur les indicateurs de frappe de Chatkit](https://docs.pusher.com/chatkit/reference/javascript#typing-indicators)
* [Tutoriel sur le clone de Slack](https://github.com/pusher/build-a-slack-clone-with-react-and-pusher-chatkit)

### Défi 2 : Permettre à l'utilisateur de créer sa propre salle

Dans ce tutoriel, nous avons utilisé l'inspecteur pour créer une salle puis nous avons codé en dur l'ID de la salle. Ce n'est pas une bonne pratique.

Dans la plupart des applications, vous voudriez créer des salles dynamiquement avec la fonction [createRoom](https://docs.pusher.com/chatkit/reference/server-node#creating-a-room).

Lorsque quelqu'un charge l'application, demandez-lui également un nom de salle :

![Image](https://cdn-media-1.freecodecamp.org/images/0*3pU3TxftH-vyDnGL.png)

Si la salle existe, rejoignez-la ; sinon, créez-la puis rejoignez-la.

Indices :

* [Documentation sur createRoom](https://docs.pusher.com/chatkit/reference/javascript#create-a-room)

### Conclusion

C'était amusant ! Nous avons construit une application de chat plutôt cool en quoi, moins d'une heure ?

Une chose que j'ai remarqué (et peut-être vous aussi) est que une fois que les fondations sont en place (modèle, connexion Chatkit, et ainsi de suite), l'ajout de nouvelles fonctionnalités de chat est assez simple.

Outre les défis, nous serions curieux de voir où ailleurs vous pourriez emmener l'application. Quelques idées :

* Envoyer des fichiers
* Compteur de messages non lus
* Notifications
* Curseurs de lecture
* Messagerie privée en un-à-un

N'hésitez pas à nous suivre sur Twitter, [@bookercodes](http://twitter.com/bookercodes) et [@codebeast](http://twitter.com/codebeast).

Jusqu'à la prochaine fois, ciao.