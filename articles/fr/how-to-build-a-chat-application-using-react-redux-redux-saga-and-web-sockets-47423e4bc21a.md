---
title: Comment créer une application de chat en utilisant React, Redux, Redux-Saga
  et Web Sockets
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2017-12-07T16:21:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chat-application-using-react-redux-redux-saga-and-web-sockets-47423e4bc21a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uttr9Cbjv7DOlgxP1r0pnA.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de chat en utilisant React, Redux, Redux-Saga
  et Web Sockets
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  In this tutorial I’m going to build a basic chat room. Every user that connects
  to the server is registered upon connection, gets a username, and then can write
  messages that are broa...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/1*J3QJAw-Yst12S6yP4rMsVg.gif)

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Dans ce tutoriel, je vais créer une salle de chat basique. Chaque utilisateur qui se connecte au serveur est enregistré à la connexion, obtient un nom d'utilisateur, puis peut écrire des messages qui sont diffusés à chaque client connecté.

> Il y a beaucoup à apprendre sur ce sujet et les nouvelles API du navigateur. Je publie un nouveau tutoriel chaque jour sur mon [blog sur le développement frontend](https://flaviocopes.com), ne le manquez pas !

L'application est une application distribuée construite en utilisant un **serveur Node.js**, et un client navigateur construit en **React**, gérant les données avec **Redux** et les effets secondaires avec **Redux-Saga**.

La communication client-serveur est gérée via **WebSockets**.

Le code source complet de cette application [est disponible ici](https://github.com/flaviocopes/chat-app-react-redux-saga-websockets).

### Initialiser create-react-app

Commençons le projet en utilisant le démarrage rapide **create-react-app**, `create-react-app chat`

![Image](https://cdn-media-1.freecodecamp.org/images/1*p2yTo9GV4zRaWAAWEtEnbQ.png)

Une fois cela fait, `cd` dans le dossier de l'application et exécutez `yarn start`

![Image](https://cdn-media-1.freecodecamp.org/images/1*EXosDPsWjYFa9_P8xDdjcw.png)

### La disposition de l'application de chat

Notre application aura cette disposition de base, très courante dans les applications de chat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uttr9Cbjv7DOlgxP1r0pnA.png)

Pour cela, nous devons créer une version statique d'un chat en utilisant du HTML et du CSS simples, qui est une disposition de chat minimaliste et rétro avec CSS Grid.

Le code est très simple :

Le résultat est une barre latérale qui hébergera la liste des utilisateurs et une zone principale avec la boîte de nouveau message en bas de l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Eu_5i-mCp1UADBYRt5TJg.png)

### Ajouter Redux pour gérer l'état

Maintenant, parlons des données.

Nous allons gérer l'état en utilisant **Redux**.

Installez Redux et react-redux avec `yarn add redux react-redux`. Ensuite, nous pouvons traduire la disposition HTML de base que nous avons ajoutée ci-dessus et la préparer pour remplir les composants que nous créerons plus tard :

Nous incluons les composants **Sidebar**, **MessagesList** et **AddMessage**.

Ils ont tous :

* un composant de présentation, qui gère l'interface utilisateur
* un composant conteneur, qui gère son comportement et les données que le composant de présentation affichera

Modifions le fichier principal de l'application `**index.js**` pour initialiser Redux, puis importer le réducteur `chat`, et enfin créer le `store`.

Au lieu de dire à ReactDOM de rendre `<App` />, entrez Provider, qui rend le store disponible à tous les composants de l'**app, sans le passer explicitement.

Ensuite, les **actions**.

Entrez les constantes d'actions dans le fichier `**ActionTypes.js**`, afin que nous puissions les référencer facilement dans d'autres fichiers :

Ce fichier contient les quatre actions qui alimenteront notre chat. Vous pouvez ajouter un nouveau message, et un nouvel utilisateur peut être ajouté au chat. Un nouveau message peut être envoyé, et le serveur enverra des mises à jour à la liste des utilisateurs lorsqu'une personne rejoindra ou quittera le chat.

Lorsque qu'un nouveau message est créé, je force maintenant le nom de l'auteur à « Moi ». Nous ajouterons des noms d'utilisateur plus tard.

Les **réducteurs** s'occupent de créer un nouvel état lorsqu'une action est dispatchée. En particulier :

* lorsqu'un **message est ajouté par nous**, nous l'ajoutons à la liste (locale) des messages
* lorsque **nous recevons un message** du serveur, nous l'ajoutons à notre liste de messages
* lorsque **nous ajoutons un utilisateur** (nous-mêmes), nous le mettons dans la liste des utilisateurs
* lorsque **nous obtenons une liste d'utilisateurs mise à jour** du serveur, nous rafraîchissons

Plongeons dans les composants qui rendront ces données et déclencheront les actions, en commençant par `**AddMessage**` :

Ce composant fonctionnel est très simple et crée un champ `input` dans la section `#new-message`. Lorsque la touche **entrée** est pressée, nous dispatchons l'action `addMessage`, en passant la valeur du champ d'entrée.

Ensuite, le composant `Message`. Il rend un seul message de chat, en utilisant le format `_Auteur : Message_` :

Il est rendu par le composant `MessagesList`, qui itère sur la liste des messages :

Le composant `Sidebar` itère quant à lui sur chaque utilisateur et imprime le nom de l'utilisateur pour chaque utilisateur qui rejoint le chat :

Nous générons les composants conteneurs pour les composants de présentation ci-dessus, en utilisant la fonction `connect()` fournie par `react-redux` :

Ce code nous donne ce beau résultat. Lorsque nous tapons un message et pressons entrée, il est ajouté à la liste des messages :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4vltWKu61NunDertK0VpKg.gif)

### Nous ajouter dans la liste des utilisateurs

La barre latérale devrait afficher la liste des utilisateurs. En particulier, puisque l'application ne parle à personne pour l'instant, nous devrions voir `**Moi**` dans la barre latérale. Plus tard, nous ajouterons d'autres personnes qui rejoignent le chat. Nous avons déjà l'action Redux `addUser`, il s'agit donc de l'appeler dans notre fichier `**index.js**` après avoir initialisé le store :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TTd4ccmkU8y6JsSQQnNb_Q.png)

### Tests

Ajoutons des tests automatisés pour nous assurer que tout fonctionne correctement et continue de fonctionner correctement à l'avenir lorsque nous ajouterons plus de fonctionnalités.

Puisque j'utilise `create-react-app`, [Jest](http://facebook.github.io/jest/) est déjà disponible à l'utilisation, et je peux simplement commencer à ajouter des tests. Pour garder les choses simples, j'ajoute le fichier de test dans le dossier qui contient le fichier à tester.

Nous commençons par tester nos actions :

et nous pouvons également tester nos réducteurs :

Nous ajoutons également quelques tests de base pour nos composants de présentation :

### Ajout d'une partie côté serveur

Un chat qui est local et ne communique pas avec le réseau n'est, franchement, pas un endroit très intéressant pour passer du temps. Créons un serveur centralisé où les utilisateurs se connecteront et où ils pourront discuter entre eux.

J'utiliserai l'objet [WebSocket natif](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) dans le navigateur, qui est largement supporté, et la bibliothèque [ws WebSocket](https://github.com/websockets/ws) sur le serveur Node.js.

Commençons par le serveur, qui est super simple :

Dès qu'un client se connecte, nous commençons à écouter les événements `**ADD_USER**` et `**ADD_MESSAGE**`. Lorsque le client établit la connexion, il enverra un événement `ADD_USER` avec le nom. Nous **l'ajouterons à la liste côté serveur des utilisateurs** et **émettons une diffusion** à tous les clients connectés.

Lorsque qu'un événement `ADD_MESSAGE` est envoyé, **nous le diffusons à tous les clients connectés**.

À la fermeture de la connexion, nous **retirons le nom de l'utilisateur** de la liste et diffusons la nouvelle liste des utilisateurs.

Côté client, nous devons **initialiser l'objet `WebSocket`** et envoyer un événement `ADD_USER` lorsque nous nous connectons au chat. Ensuite, **nous écoutons les événements `ADD_USER` et `ADD_MESSAGE`** diffusés par le serveur :

Nous importerons `setupSocket()` depuis le fichier principal `**index.js**`.

Nous devons maintenant introduire un moyen de **gérer les effets secondaires** dans notre code, et de gérer la création d'un événement WebSocket lorsque l'utilisateur tape un message, afin qu'il puisse être diffusé à tous les clients connectés.

Pour effectuer cette opération de manière propre, nous allons utiliser `[**redux-saga**](https://redux-saga.js.org/)`, une bibliothèque qui fournit un bon moyen de gérer les effets secondaires dans Redux/React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-GC9G3YWGrTD85yV5N0STg.png)

Commencez avec `yarn add redux-saga`

Nous initialisons le middleware `redux-saga` et le connectons au store Redux pour accrocher notre `**saga**` :

Redux-Saga est un **middleware Redux**, nous devons donc l'initialiser lors de la création du store. Une fois cela fait, nous exécutons le middleware et passons le nom de l'utilisateur et la fonction `dispatch`. Avant de le faire, nous initialisons le socket afin de pouvoir le référencer à l'intérieur de la saga.

Auparavant, l'utilisateur s'appelait 'Moi', mais ce n'est pas très agréable si chaque utilisateur s'appelle lui-même 'Moi'. J'ai donc ajouté un **générateur de nom d'utilisateur dynamique**, en utilisant [Chance.js](http://chancejs.com/). Chaque fois que nous nous connectons, nous avons un nom unique généré pour nous en important `utils/name` :

Plongeons maintenant dans notre **saga** :

Conceptuellement, c'est très simple. Nous prenons toutes les actions de type `ADD_MESSAGE` et lorsque cette action se produit, nous envoyons un message au WebSocket, en passant l'action et quelques détails. Le message de chat envoyé par notre utilisateur peut être dispatché à tous les clients connectés par le serveur.

Nous arrivons ici au résultat final, et ci-dessous vous pouvez voir un gif qui montre comment le chat fonctionne avec plusieurs clients connectés. Nous pouvons ouvrir autant de fenêtres que nous le souhaitons, et dès que nous chargeons l'URL du serveur, nous allons être connectés avec un nouveau nom d'utilisateur au chat. Nous ne voyons pas les messages passés, comme dans IRC, mais nous verrons chaque message écrit à partir du moment où nous nous connectons.

Dès que nous partons, notre nom d'utilisateur est retiré et les autres personnes dans le chat peuvent continuer à discuter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J3QJAw-Yst12S6yP4rMsVg.gif)

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)