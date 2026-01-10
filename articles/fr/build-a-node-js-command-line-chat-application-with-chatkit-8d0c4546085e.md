---
title: Créer une application de chat en ligne de commande Node.js avec Chatkit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T15:17:38.000Z'
originalURL: https://freecodecamp.org/news/build-a-node-js-command-line-chat-application-with-chatkit-8d0c4546085e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X_nJ9SNJQRlrgMt7_V4GxA.gif
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Créer une application de chat en ligne de commande Node.js avec Chatkit
seo_desc: 'By Hugo

  Building chat in your app can be pretty complex. Yet, with Chatkit, implementing
  fully-featured chat is nothing but a few lines of code.

  In this tutorial, I’ll walk you through how to build a command-line chat, like this:


  The complete code c...'
---

Par Hugo

Intégrer un chat dans votre application peut être assez complexe. Pourtant, avec [Chatkit](http://pusher.com/chatkit), implémenter un chat entièrement fonctionnel n'est qu'une question de quelques lignes de code.

Dans ce tutoriel, je vais vous guider à travers la création d'un chat en ligne de commande, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X_nJ9SNJQRlrgMt7_V4GxA.gif)

Le code complet peut être trouvé sur [GitHub](https://github.com/pusher/chatkit-command-line-chat).

### Qu'est-ce que Chatkit ?

Vous vous demandez peut-être, « qu'est-ce que Chatkit ? »

En résumé, Chatkit est une API pour vous aider à construire des fonctionnalités de chat dans votre application. Des fonctionnalités comme :

* Rooms
* Présence en ligne
* Indicateurs de frappe
* Indicateurs de lecture (compteur de messages non lus, accusés de réception)
* Messages multimédias riches
* Et plus encore

De plus, Chatkit gère les détails complexes qui surviennent lors de la création d'un chat en temps réel comme la fiabilité et la scalabilité.

Pour moi, utiliser Chatkit signifie ne pas avoir à gérer un serveur web socket, gérer l'infrastructure pour celui-ci, et gérer le chat à grande échelle !

Dans ce tutoriel, nous n'effleurerons que la surface de ce que Chatkit peut faire. Pour vous donner une idée de ce que vous pouvez construire, consultez ce clone open source de Slack, alimenté par Chatkit :

Plutôt cool, non ?

### Créer une instance Chatkit

Avant de plonger dans le tutoriel, vous devriez configurer une instance Chatkit. Cela ne prend qu'une seconde.

Pour en créer une, rendez-vous sur [pusher.com/chatkit](http://pusher.com/chatkit) et cliquez sur **Sign Up**. Dans le tableau de bord, sous « Chatkit », cliquez sur **Create new +** puis entrez un nom pour l'instance. J'ai appelé la mienne « My Awesome Chatkit App ! » :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kYfepxG_GUM--LSt4ZtyxA.gif)

Dans l'onglet **Keys**, notez votre **Instance Locator** et **Secret Key**. Nous en aurons besoin dans un instant.

### Créer une room Chatkit

Chatkit nous permet de créer des rooms de chat publiques ou privées, et prend même en charge le chat en un-à-un.

Normalement, vous créeriez des rooms de manière dynamique — par exemple, lorsqu'un utilisateur final crée une nouvelle room — mais dans ce tutoriel, nous utiliserons l'**Inspector** pour en créer une manuellement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jtaXDiTlO2NBV24K-fey3A.gif)

### Créer un serveur d'authentification

L'authentification est l'action de prouver qu'un utilisateur est bien celui qu'il prétend être. Normalement, cela implique un mot de passe.

Dans ce tutoriel, nous n'authentifierons pas les utilisateurs — nous ne leur demanderons pas de mot de passe — mais nous devrons tout de même écrire une route `/authenticate` qui retourne un [jeton Chatkit](https://docs.pusher.com/chatkit/authentication#define-a-token-provider).

De plus, nous devrons définir une route appelée `/users` qui crée un utilisateur Chatkit.

Pour ce faire, créez un nouveau dossier, j'ai appelé le mien `terminal-chat`. Ensuite, installez `@pusher-chatkit-server`, `express`, et quelques middlewares Express :

```
mkdir terminal-chat
```

```
cd terminal-chat
```

```
npm init -y
```

```
npm install --save @pusher/chatkit-server npm install --save express npm install --save body-parser cors
```

Ensuite, créez un nouveau fichier appelé `server.js` et collez le code suivant :

N'oubliez pas de remplacer `YOUR_INSTANCE_LOCATOR` et `YOUR_CHATKIT_KEY` par les vôtres.

### Configurer notre client

Maintenant que nous avons un serveur et une instance Chatkit, nous pouvons commencer à construire le client en ligne de commande.

Dans le même projet, installez `@pusher/chatkit` et `jsdom` :

```
npm install --save @pusher/chatkitnpm install --save jsdom
```

Pour être clair, dans l'étape précédente, nous avons installé le SDK serveur Chatkit (`@pusher/chatkit-server`) et ici, nous installons le SDK client Chatkit (`@pusher/chatkit-client`). Nous avons également installé `jsdom`, mais nous en parlerons plus tard.

Dans un nouveau fichier appelé `client.js`, collez le code suivant :

En commençant par le haut, nous importons d'abord `ChatManager` et `TokenProvider` depuis `@pusher/chatkit`. Nous y ferons référence bientôt.

Nous importons également `jsdom`, la dépendance dont j'ai parlé plus tôt.

En résumé, `@pusher/chatkit-client` fonctionne dans le navigateur mais pas dans Node. Dans une fonction appelée `makeChatkitNodeCompatible`, nous utilisons `jsdom` pour « tromper » Chatkit en lui faisant croire qu'il s'exécute dans le navigateur ?. C[eci est une solution de contournement _temporaire_,](https://github.com/pusher/chatkit-client-js/issues/70) mais elle fonctionne parfaitement.

En bas du module, nous définissons une fonction `async` appelée `main`, qui nous permet d'utiliser `await` lors de l'appel de fonctions asynchrones.

Si `await` est un nouveau concept pour vous, voici une [excellente introduction](https://www.youtube.com/watch?v=DwQJ_NPQWWo&feature=youtu.be).

### Demander à l'utilisateur son nom d'utilisateur

Avant de permettre à un utilisateur de rejoindre une room, nous devons lui demander son nom. Pour ce faire, nous pouvons utiliser `prompt`.

D'abord, installez `prompt` :

```
npm install --save prompt
```

Puis, importez-le :

Ensuite, mettez à jour notre fonction main :

Maintenant, si nous exécutons l'application avec la commande `node client.js`, nous devrions avoir notre prompt :

![Image](https://cdn-media-1.freecodecamp.org/images/1*74GdmZ0wvdboEgKba_TCxw.gif)

Woo ?!

### Créer un utilisateur

Avant de se connecter à Chatkit, nous devons d'abord créer un utilisateur Chatkit via le serveur que nous avons écrit précédemment.

Pour ce faire, nous enverrons une requête à la route `/users` en utilisant `axios`, qui est un client HTTP :

```
npm install --save axios
```

Après avoir installé `axios`, importez-le :

Ensuite, définissez une fonction appelée `createUser` :

Nous pouvons maintenant appeler cette fonction avec le nom d'utilisateur demandé :

Testons cela.

Ouvrez deux fenêtres de terminal. Dans l'une, démarrez le serveur avec `node server.js` et dans l'autre, exécutez le client avec `node client.js`. Si tout va bien, vous _devriez_ être invité à entrer un nom d'utilisateur, et vous verrez `User created: <username>` dans la sortie du serveur.

Si vous voyez une erreur du type `Failed to create a user, connect ECONNREFUSED`, votre serveur n'est peut-être pas en cours d'exécution, alors vérifiez cela.

### Configurer le SDK Chatkit

À ce stade, nous avons un nom d'utilisateur et la capacité de créer un utilisateur. Ensuite, nous voudrons nous connecter à Chatkit en tant que cet utilisateur.

Pour ce faire, sous l'appel que vous venez de faire à `createUser`, collez le code suivant :

Encore une fois, n'oubliez pas de remplacer votre `YOUR_INSTANCE_LOCATOR` par l'**Instance Locator** que vous avez noté précédemment.

Ce code initialise Chatkit puis se connecte au service, retournant le `currentUser`. Notez comment nous fournissons un `TokenProvider` qui pointe vers _notre serveur d'authentification_.

### Lister les rooms

Maintenant que nous avons un utilisateur authentifié, nous pouvons lui montrer une liste de roomsqu'il peut rejoindre.

Pour ce faire, nous devons mettre à jour la fonction principale dans `client.js` pour récupérer les rooms rejoignables (`getJoinableRooms`), et les lister aux côtés des roomsqu'un utilisateur a _déjà_ rejointes (`user.rooms`) :

La syntaxe `...` là est appelée [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment), et elle fournit un moyen succinct de fusionner deux tableaux ou plus.

L'exécution de `node client.js` devrait maintenant afficher une liste de rooms :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dmwgkCmdXa_2wou1dnMW0A.gif)

Vous ne verrez probablement qu'une seule room au début. Pour créer des rooms supplémentaires, retournez à l'Inspector ou utilisez la fonction `[createRoom](https://docs.pusher.com/chatkit/reference/server-node#creating-a-room)`.

### S'abonner à une room

Ensuite, nous devons inviter l'utilisateur à choisir une room, avec ce code :

Une chose cool à propos de `prompt` est que vous pouvez créer des règles de validation. Ci-dessus, nous en créons une pour nous assurer que l'entrée de l'utilisateur est comprise entre `0` et le nombre de rooms rejoignables.

Une fois que nous avons le choix de la room de l'utilisateur, nous pouvons la définir comme `room` et nous abonner à la room :

Lors de l'abonnement, nous ajoutons un _hook_ `**onNewMessage**`.

Vous pouvez penser à un hook comme une fonction qui est appelée chaque fois qu'un événement se produit. Dans ce cas, c'est lorsqu'un nouveau message est reçu.

`onNewMessage` sera appelé en **temps réel** chaque fois qu'un nouveau message est envoyé par « un utilisateur ». Lorsque je dis « un utilisateur », cela _inclut_ l'utilisateur actuel, donc dans la fonction, nous n'affichons le message que s'il a été envoyé par quelqu'un d'autre.

### Envoyer des messages à partir de l'entrée utilisateur

Pouvoir recevoir des messages n'est pas très utile si nous ne pouvons pas aussi envoyer des messages, n'est-ce pas ?

Heureusement, envoyer un message n'est qu'une ligne de code avec Chatkit.

D'abord, installez `[readline](https://nodejs.org/api/readline.html)` pour lire l'entrée de l'utilisateur :

```
npm install --save readline
```

Puis, importez-le :

Enfin, référencez-le ci-dessous :

Si vous exécutez deux instances du client, vous devriez pouvoir envoyer et recevoir des messages :

![Image](https://cdn-media-1.freecodecamp.org/images/1*w5JT7M0ckdcTFCUlVNy9eQ.gif)

### Ajouter un indicateur de chargement pour un peu de fun ✨

Comme toujours, l'envoi de données sur le réseau peut prendre une seconde ou deux. Pour un peu de fun, et pour rendre notre application _plus rapide_, ajoutons un indicateur de chargement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*siPbXaNhYdzxcMxKI5--tw.gif)

D'abord, installez `ora`, un module d'indicateur de chargement :

```
npm install --save ora
```

Puis, dans `client.js`, nous pouvons appeler `start`, `succeed`, etc. selon le statut de la commande.

Voici le fichier `client.js` complet, avec le nouveau code lié à l'indicateur de chargement mis en évidence :

### Conclusion

Incroyable, nous avons terminé !

Pour résumer, vous avez appris à :

* Demander et authentifier l'utilisateur
* Se connecter à Chatkit
* Lister les rooms disponibles pour l'utilisateur
* Rejoindre une room
* Envoyer et recevoir des messages depuis une room
* Et, pour le fun, ajouter un indicateur de chargement

Dans ce tutoriel, nous avons à peine effleuré la surface de Chatkit. Il y a tant d'autres choses que nous pourrions construire, y compris :

* Changer de room
* Créer de nouvelles rooms
* Afficher le statut en ligne/hors ligne des utilisateurs
* Afficher les indicateurs de frappe
* Afficher les accusés de réception

Vous voulez apprendre comment ? Faites-le moi savoir dans les commentaires et nous écrirons la partie 2.

[Alex Booker](https://www.freecodecamp.org/news/build-a-node-js-command-line-chat-application-with-chatkit-8d0c4546085e/undefined) a créé un tutoriel vidéo basé sur cet article. Allez le voir !