---
title: Comment mettre à jour le statut d'un utilisateur en temps réel en utilisant
  JavaScript et Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T13:55:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-a-users-status-in-realtime-using-javascript-and-pusher-2cae8f4aaafa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oCKom0PmUDVRGM5p7mXT9w.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment mettre à jour le statut d'un utilisateur en temps réel en utilisant
  JavaScript et Pusher
seo_desc: 'By Rahat Khanna

  “Hey, what’s up?” is not a phrase we need to ask someone these days. These days
  knowing what someone is up to has become so easy, because we keep seeing updated
  statuses for all our friends on WhatsApp, Snapchat, Facebook and so on.

  I...'
---

Par Rahat Khanna

« Hey, what’s up ? » n'est plus une phrase que nous devons poser à quelqu'un de nos jours. De nos jours, savoir ce que quelqu'un fait est devenu si facile, car nous voyons constamment les statuts mis à jour de tous nos amis sur WhatsApp, Snapchat, Facebook et bien d'autres.

Dans cet article, nous allons apprendre comment nous pouvons mettre à jour le statut d'un utilisateur dans un composant en temps réel ainsi qu'une liste de tous les membres qui sont en ligne.

Nous allons utiliser [Node.js](https://nodejs.org/en/) comme serveur d'application, Vanilla JavaScript en front-end, et [Pusher](https://pusher.com/) pour la communication en temps réel entre notre serveur et le front-end.

Nous allons construire une application, qui sera comme votre liste d'amis ou une salle de chat commune, où vous pouvez voir qui est en ligne et quel est leur dernier statut mis à jour en temps réel. Nous allons apprendre à connaître le canal **presence** de Pusher et comment savoir quels sont les membres en ligne sur ce canal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MfEOUmfGsInLeL8j8xWyrA.gif)

Nous allons construire les composants suivants au cours de cet article de blog :

Serveur Node.js utilisant le Framework Express.js :

* **/register** API — Afin d'enregistrer/connecter un nouvel utilisateur à notre canal et serveur en créant leur session et en sauvegardant leurs informations
* **/isLoggedIn** API — Pour vérifier si un utilisateur est déjà connecté ou non en cas de rafraîchissement du navigateur
* **/usersystem/auth** API — Validation d'authentification effectuée par Pusher après l'avoir enregistré avec notre application et lors de l'abonnement à un canal de présence ou privé
* **/logout** API — Pour déconnecter l'utilisateur et supprimer la session

Application Front-End utilisant JavaScript :

* Formulaire d'enregistrement/connexion — Pour enregistrer/connecter un nouvel utilisateur en remplissant leur nom d'utilisateur et leur statut initial
* Liste des membres — Pour voir tout le monde qui est en ligne et leurs statuts mis à jour
* Mettre à jour le statut — Pour cliquer sur le statut existant et le mettre à jour lors de la perte de focus du contrôle d'édition du texte du statut

Trouvez ici le [lien](https://github.com/mappmechanic/whats-up-realtime-status-update) vers le dépôt Github pour référence.

### Introduction à Pusher

Pusher est une plateforme qui abstrait les complexités de la mise en œuvre d'un système en temps réel par nous-mêmes en utilisant WebSockets ou Long Polling. Nous pouvons instantanément ajouter des fonctionnalités en temps réel à nos applications web existantes en utilisant Pusher, car il supporte une grande variété de kits de développement logiciel (SDK).

Des kits d'intégration sont disponibles pour une variété de bibliothèques front-end comme Backbone, React, Angular, et jQuery — et aussi pour des plateformes/langages back-end comme .NET, Java, Python, Ruby, PHP, et GO.

### S'inscrire avec Pusher

Vous pouvez créer un compte gratuit sur Pusher [ici](http://pusher.com/signup). Après votre inscription et votre première connexion, vous serez invité à créer une nouvelle application comme vu dans l'image ci-dessous. Vous devrez remplir quelques informations sur votre projet, et également fournir la bibliothèque front-end ou le langage back-end avec lequel vous allez construire votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3SMGJP-h-cbEJSXw.png)

Pour cet article en particulier, nous allons sélectionner JavaScript pour le front-end et Node.js pour le back-end comme vu dans l'image ci-dessus.

Cela vous montrera simplement un ensemble de codes d'exemple de démarrage pour ces sélections, mais vous pouvez utiliser n'importe quel kit d'intégration plus tard avec cette application.

![Image](https://cdn-media-1.freecodecamp.org/images/0*rbktLHXpbR6GDzkv.png)

### Serveur Node.js

Node.js doit être installé dans le système comme prérequis à ce projet. Commençons maintenant à construire le serveur Node.js et toutes les API requises en utilisant Express. Initialisez un nouveau projet node avec la commande suivante :

```
npm init
```

### Installation des dépendances

Nous allons installer les dépendances requises comme Express, express-session, Pusher, body-parser, cookie-parser avec la commande suivante :

### Serveur de base

Nous allons maintenant créer la base fondamentale pour le serveur Node.js et également activer les sessions avec le module `express-session`.

Dans le code ci-dessus, nous avons créé un serveur Express de base, et en utilisant la méthode `.use`, nous avons activé cookie-parser, body-parser, et un serveur de fichiers statiques à partir du dossier `**public**`. Nous avons également activé les sessions en utilisant le module `express-session`. Cela nous permettra de sauvegarder les informations de l'utilisateur dans la session de requête appropriée pour l'utilisateur.

### Ajout de Pusher

Pusher dispose d'un module npm open source pour les intégrations Node.js, que nous allons utiliser. Il fournit un ensemble de méthodes utilitaires pour s'intégrer avec les API de Pusher en utilisant un `appId`, une `key` et un `secret` uniques. Nous allons d'abord installer le module `npm` de Pusher en utilisant la commande suivante :

```
npm install pusher --save
```

Maintenant, nous pouvons utiliser `require` pour obtenir le module `Pusher` et créer une nouvelle instance en passant un objet d'options avec des clés importantes pour initialiser notre intégration. Pour cet article, j'ai choisi des clés aléatoires — vous devrez les obtenir pour votre application à partir du tableau de bord de Pusher.

Vous devrez remplacer le `appId`, la `key` et le `secret` par des valeurs spécifiques à votre propre application. Après cela, nous allons écrire le code pour une nouvelle API qui sera utilisée pour créer un nouveau commentaire.

### API d'enregistrement/connexion

Maintenant, nous allons développer la première route API de notre application grâce à laquelle un nouvel utilisateur peut s'enregistrer/se connecter et se rendre disponible sur notre application.

Dans le code ci-dessus, nous avons exposé un appel API `POST` sur la route `/register` qui attendrait les paramètres `username` et `status` à passer dans le corps de la requête. Nous allons sauvegarder ces informations d'utilisateur dans la `session de requête`.

### API d'authentification du système utilisateur

Afin de permettre à tout client de s'abonner aux canaux `**Private**` et `**Presence**` de Pusher, nous devons implémenter une API `auth` qui authentifierait la requête de l'utilisateur en appelant la méthode `**Pusher.authenticate**` côté serveur. Ajoutez le code suivant dans le serveur afin de remplir cette condition :

Nous devons fournir la route spécifique lors de l'initialisation de la bibliothèque côté client de Pusher, que nous verrons plus tard. La bibliothèque cliente de Pusher appellera automatiquement cette route et passera les propriétés `channel_name` et `socket_id`. Nous obtiendrons simultanément les informations de l'utilisateur à partir de l'objet de session de l'utilisateur et les passerons en tant que `presenceData` à l'appel de la méthode `Pusher.authenticate`.

### API IsLoggedIn et Logout

Si l'utilisateur rafraîchit le navigateur, l'application côté client doit détecter si l'utilisateur est déjà enregistré ou non. Nous allons implémenter une route API `isLoggedIn` pour cela. De plus, nous avons besoin d'une route `logout` pour permettre à tout utilisateur de se déconnecter de l'application.

### Application Front-End utilisant Vanilla JavaScript

Nous allons maintenant développer l'application front-end pour enregistrer un nouvel utilisateur avec un statut initial et voir les membres qui sont en ligne et leurs statuts. Nous allons également construire la fonctionnalité pour que l'utilisateur connecté mette à jour leur statut et que tous les autres utilisateurs voient le statut mis à jour en temps réel.

### Étape 1 : Créer un dossier nommé public et créer un fichier index.html

Nous avons déjà écrit du code dans notre `server.js` pour servir du contenu statique à partir du dossier `public`, donc nous allons écrire tout notre code front-end dans ce dossier.

Veuillez créer un nouveau dossier `public` et également créer un fichier `index.html` vide pour l'instant.

### Étape 2 : Ajouter le code de base à notre index.html

Nous allons ajouter un peu de code de base pour établir la structure de base de notre application web comme `Header`, et `Sections` où le formulaire d'enregistrement et la liste des membres peuvent être placés.

Dans le code de base ci-dessus, nous avons référencé notre fichier JavaScript principal `app.js` et la bibliothèque JavaScript côté client de Pusher. Nous avons également une balise script où nous placerons le modèle pour une ligne de membre dans la liste des membres. De plus, nous avons deux balises div vides avec les ids `**me**` et `**membersList**` pour contenir le nom et les informations du membre connecté, ainsi que la liste de tous les autres membres avec leur statut.

### Étape 3 : Style.css

Il est important de noter que nous allons afficher le formulaire d'inscription pour la première fois et que le bouton `MembersList` et `Logout` seront masqués par défaut initialement. Veuillez créer un nouveau fichier appelé `**style.css**` et y ajouter le CSS suivant :

Veuillez essayer d'ouvrir l'URL [**http://localhost:9000**](http://localhost:9000/) dans votre navigateur et l'application se chargera avec le formulaire de base d'enregistrement ou de connexion avec le nom d'utilisateur et le statut. Le résultat ressemblera à la capture d'écran ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0*29ug0ae4efpquw-u.png)

### Étape 4 : Ajouter le code de base de app.js

Maintenant, nous allons ajouter notre code JavaScript pour avoir des éléments utilitaires de base à l'intérieur d'une fonction auto-invocatrice afin de créer une portée privée pour nos variables d'application. Nous ne voulons pas polluer la portée globale de JavaScript.

Dans le code ci-dessus, nous avons référencé toutes les variables importantes dont nous aurons besoin. Nous allons également initialiser la bibliothèque Pusher en utilisant `new Pusher` et en passant la clé API comme premier argument. Le deuxième argument contient un objet de configuration optionnel dans lequel nous allons ajouter la clé `authEndpoint` avec la route personnalisée de l'API node `/usersystem/auth` et également ajouter la clé `**encrypted**` en la définissant sur la valeur `true`.

Nous allons créer quelques fonctions génériques pour afficher ou masquer un élément en passant son identifiant unique. Nous avons également ajouté une méthode commune nommée `**ajax**` pour faire des requêtes AJAX en utilisant l'objet XMLHttp en Vanilla JavaScript.

Au chargement de la page, nous faisons une requête AJAX pour vérifier si l'utilisateur est connecté ou non. Si l'utilisateur est connecté, nous allons utiliser directement l'instance Pusher pour abonner l'utilisateur à un canal de présence nommé `presence-whatsup-members`. Vous pouvez avoir cela comme la salle de chat unique ou l'emplacement de l'application où vous souhaitez signaler/suivre les membres en ligne.

Nous avons également écrit une méthode ci-dessus pour `addNewMember` en utilisant une requête AJAX vers la route API `register` que nous avons construite dans Node.js. Nous allons passer le nom et le statut initial saisis dans le formulaire.

Nous avons également une méthode pour mettre à jour l'état de la vue de l'utilisateur en fonction de l'état de connexion. Cette méthode ne fait rien d'autre que mettre à jour la visibilité de la liste des membres, du bouton de déconnexion et du formulaire d'inscription. Nous avons utilisé une méthode `bindChannelEvents` lorsque l'utilisateur est connecté, que nous allons implémenter plus tard dans l'article de blog.

Veuillez ajouter le CSS suivant dans le fichier `**style.css**` pour afficher l'élément `me` de manière appropriée avec le nom d'utilisateur et le statut de l'utilisateur connecté.

### Étape 5 : Ajouter le code pour rendre la liste des membres et bindChannelEvents

Maintenant, après nous être abonnés au canal, nous devons lier certains événements afin de savoir chaque fois qu'un nouveau membre est ajouté au canal ou supprimé de celui-ci. Nous allons également lier à un événement personnalisé pour savoir chaque fois que quelqu'un met à jour son statut.

Ajoutez le code suivant au fichier `**app.js**` :

Dans la méthode `bindChannelEvents` ci-dessus, nous utilisons la méthode `channel.bind` pour lier les gestionnaires d'événements pour 3 événements internes — `**pusher:subscription_succeeded**`, `**pusher:member_added**`, `**pusher:member_removed**` et 1 événement personnalisé — `**client-status-update**`.

Maintenant, nous allons ajouter le code JavaScript pour rendre la liste des membres. Il est important de savoir que l'objet que j'ai retourné de la méthode `.subscribe` a une propriété appelée `members`, qui peut être utilisée pour connaître les informations sur l'utilisateur connecté référencé par la clé `me` et les autres membres par la clé `members`. Ajoutez le code suivant au fichier `**app.js**` :

Nous avons ajouté le gestionnaire d'événements pour l'ajout/suppression de nouveaux membres afin de re-rendre la liste des membres afin qu'elle reste mise à jour avec uniquement les membres en ligne. Afin d'afficher la liste des membres, nous devons ajouter le style suivant dans notre fichier `**style.css**` :

Maintenant, nous allons écrire le code pour déclencher un événement client sur notre canal afin de notifier tous les utilisateurs du changement de statut de l'utilisateur connecté. Ajoutez le code suivant à votre fichier `**app.js**` :

**IMPORTANT** : Lorsque nous exécutons ce code dans nos navigateurs, mettons à jour le statut et sortons du contrôle de statut, nous obtiendrons une erreur dans la console JavaScript pour la bibliothèque Pusher. Pour corriger cela, allez dans la console du site [Pusher.com](https://pusher.com), allez dans les paramètres et activez l'envoi d'événements directement depuis les clients.

Nous pouvons uniquement envoyer des événements directement depuis les clients pour les canaux `Presence` ou `Private`. Lien vers la documentation officielle — [https://Pusher.com/docs/client_api_guide/client_events#trigger-events](https://pusher.com/docs/client_api_guide/client_events#trigger-events)

### Conclusion

Nous avons construit une application qui affichera tous les membres en ligne pour un canal `presence` particulier et leur statut. Si l'un des utilisateurs en ligne met à jour son statut, chaque utilisateur sera notifié du statut mis à jour.

Ce composant ou code peut être utilisé pour développer une section de réseau social dans la plupart des applications web de nos jours. C'est un cas d'utilisation important où l'utilisateur doit connaître les autres participants disponibles. Par exemple : une application de classe en ligne peut voir les autres participants et le statut peut correspondre à toute question que tout participant souhaite poser au présentateur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*A1pL1ImjGKS6sCyp.gif)

Nous avons simplement utilisé Node.js et Vanilla JavaScript pour implémenter la fonctionnalité ci-dessus. Vous pouvez utiliser JavaScript pour le code front-end avec n'importe quel framework populaire comme [React](https://reactjs.org/) ou [Angular](https://angular.io/). Le back-end peut également être [Java](https://java.com/en/) ou [Ruby](https://www.ruby-lang.org/en/). Veuillez vous référer à la documentation de Pusher pour plus d'informations à ce sujet.

Cet article de blog a été initialement publié sur [le blog de Pusher](https://blog.pusher.com/update-users-status-realtime-javascript/).