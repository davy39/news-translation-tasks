---
title: Comment créer un moniteur de médias sociaux simple avec NodeJS, GraphQL et
  Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T19:55:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-social-media-monitor-with-nodejs-graphql-and-vue-55ffe4124ab5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*apsmd1svbRnvOh_Evak5nA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Comment créer un moniteur de médias sociaux simple avec NodeJS, GraphQL
  et Vue
seo_desc: 'By Paschal

  Introduction

  We’ll build a simple monitor that will track the number of people that followed
  us on specific dates, using Medium as the use case. This is just a bare prototype
  and can be done for any other social media or networking platfor...'
---

Par Paschal

#### Introduction

Nous allons créer un moniteur simple qui suivra le nombre de personnes qui nous ont suivis à des dates spécifiques, en utilisant Medium comme cas d'utilisation. Ce n'est qu'un prototype de base et peut être fait pour toute autre plateforme de médias sociaux ou de réseautage.

À la fin, nous devrions avoir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IWAiDTjoSP9FrikYuvcvvA.png)

Pour y parvenir, nous utiliserons le package [node-imap](https://github.com/mscdex/node-imap). Les deux principaux protocoles pour gérer les emails sont IMAP (Internet Messaged Access Protocol) et POP (Post office protocol). IMAP est préféré, car il se synchronise toujours avec le serveur de messagerie, donc les modifications apportées sur le client de messagerie apparaîtront immédiatement dans la boîte de réception du webmail.

#### Prérequis

* NodeJS
* VueJS
* Un compte Gmail

#### Installation du back-end avec node-imap et apollo

Tout d'abord, installez les packages nécessaires.

```
npm i --save node-imap apollo-server mailparser
```

Maintenant, vous pouvez définir les types et le resolver puis exécuter le serveur apollo.

Un type **User** qui a les types de chaîne email et password comme schéma a été défini, et une mutation appelée **imapMutation** qui reçoit l'email et le mot de passe de l'utilisateur et retourne ensuite une réponse avec le type User.

Le resolver gère la mutation, et vous pouvez ensuite travailler avec les arguments envoyés par le client.

Maintenant, vous pouvez exécuter le serveur.

Vous pouvez ensuite importer les modules **node-imap** et **mailparser**. Le module **mailparser** sera utilisé pour recevoir les réponses de mail en JSON.

```
const Imap = require('imap')const simpleParser = require('mailparser').simpleParser
```

Vous allez créer une fonction **connectImap** qui gérera notre fonctionnalité IMAP. À partir de la [documentation node-imap](https://github.com/mscdex/node-imap), vous pouvez obtenir le squelette de la façon dont le module fonctionne, puis le copier et le coller dans le code. Il fonctionne principalement avec des callbacks et des émetteurs, donc nous allons l'envelopper dans une promesse.

Vous devriez avoir quelque chose comme ceci.

Lorsque l'événement **ready** est appelé, nous nous connectons à notre mail, puis nous pouvons rechercher des messages. Donc, nous allons rechercher des emails provenant du compte medium qui gère les followers (**_noreply@medium.com_**).

Notre événement **_ready_** devrait ressembler à ceci.

Nous recherchons des emails où chaque sujet contient une sous-chaîne **_started following you_**. Ensuite, nous divisons les tableaux avec une virgule ou la conjonction and pour obtenir le nombre de followers, puis nous gérons les cas comme **_Peter and 3 others started following you_**. Après avoir divisé la chaîne ci-dessus, nous aurons une sortie :

```
[  'Peter',  '3 others started following you']
```

La longueur de ce tableau est **2**, donc nous avons deux followers. Si le sujet contient **_others_**, nous prenons le chiffre derrière et ajoutons à la longueur du tableau, qui est **5**, puis nous soustrayons **1** pour nous débarrasser de la chaîne **_3 others started following you_**. Cela nous laisse avec **4**.

Ensuite, nous résolvons la promesse lorsque l'événement **_end_** est déclenché (_imap.once(end)_).

Puisque nous devrons envoyer le tableau à notre client apollo, nous devrons définir le type du tableau **_graphPoints_**.

Nos définitions de type devraient ressembler à ceci :

Nous avons ajouté la clé **data** au type **_User_**, qui contiendra la valeur **_graphPoints_**, et son type est un tableau d'objets avec le type **_Graph_**.

Enfin, nous gérons le resolver, qui obtiendra l'email et le mot de passe de l'utilisateur puis retournera l'**email** et les données (**_graphPoints_**).

Si nous enregistrons l'objet **user**, notre structure devrait être quelque chose comme ceci :

```
email: String,data: [ { numberOfFollowers: 1, date: 2017-07-05T07:53:18.000Z },        { numberOfFollowers: 1, date: 2017-07-07T19:34:57.000Z }      ]
```

#### Installation du front-end avec v-charts et apollo client

Maintenant, nous voulons obtenir les données envoyées par le serveur et tracer le graphique avec le module [v-charts](https://www.npmjs.com/package/v-charts).

Mais d'abord, nous installons nos dépendances.

```
npm install --save vue-chartjs vue-apollo apollo-client apollo-link-http apollo-cache-persist apollo-cache-inmemory graphql graphql-tag moment
```

Je sais ce que vous pensez — c'est beaucoup de dépendances. Si vous avez des problèmes pour configurer un projet Vue, vous pouvez découvrir comment faire [ici](https://cli.vuejs.org/guide/creating-a-project.html#vue-create). Nous devrions également inclure [vuetify](https://vuetifyjs.com/en/getting-started/quick-start) et le [vue-router](https://router.vuejs.org/installation.html#direct-download-cdn) si nous voulons styliser le projet et créer des routes supplémentaires.

Dans notre dossier **_src_**, nous pouvons créer un dossier **_config_**. La structure devrait ressembler à ceci :

```
|src  |config     -graphql.js     -index.js     -LineChart.js  |pages      -login.vue  |router      -index.js  App.vue  main.js
```

Nous devrons configurer notre client graphql dans le fichier **_src/config/index.js_**.

Assurez-vous que l'**_uri_** est sur le même port que votre serveur apollo, par défaut le serveur apollo s'exécute sur le port **4000**. Notre client apollo est ensuite configuré avec le _httpLink_ et le _cache_.

Le fichier **_src/config/graphql.js_** devrait ressembler à ceci :

Cette requête soumettra l'**email** et le **password** de l'utilisateur à imapMutation puis obtiendra l'**email** et les **data**(graphPoints) du serveur apollo.

Ensuite, nous créons notre composant de graphique dans le fichier **_src/config/LineChart.js_**. Nous pouvons utiliser des graphiques allant des graphiques en barres aux histogrammes. Un graphique en ligne a été utilisé dans cet exemple.

Nous pouvons importer le package **_vue-apollo_** dans notre fichier main.js et inclure le **apolloProvider** lors de l'initialisation de l'application.

Enfin, nous configurerons le fichier **src/pages/login.vue**, que nous devrions avoir configuré comme le composant pour la route d'accueil par défaut / dans le fichier **src/router/index.js**.

Nous avons donc créé un formulaire de base qui accepte l'email et le mot de passe de l'utilisateur, puis envoie ces données au serveur via la méthode **_signup()_**. La méthode **_plotGraph()_** parcourt la réponse (graphPoints) et pousse les dates vers le tableau des labels et le nombre de followers vers le tableau des données.

Après avoir stylisé en utilisant l'objet **_options_**, nous devrions avoir quelque chose comme la capture d'écran montrée lors de l'introduction à ce projet.

#### Conclusion

Vous pouvez encore faire plus avec votre projet personnel, mais le but de ceci était de montrer comment travailler avec le package node-imap, et comment apollo fonctionne comme serveur et comme client. Si vous avez eu des problèmes avec ce projet, vous pouvez laisser un commentaire ou envoyer un message sur [Twitter](https://twitter.com/_Obbap).

Vous pouvez essayer la version live de [ceci](https://medium-followers.netlify.com/), ou vous pourriez consulter les dépôts pour les applications [client](https://github.com/obbap1/MonitorFollowers_frontend) et [serveur](https://github.com/obbap1/MonitorFollowers_backend) sur GitHub.

Si vous voulez apprendre de nouvelles technologies et frameworks, vous pouvez le faire [ici](https://www.microverse.org/) et si vous avez appris quelque chose, n'hésitez pas à applaudir ci-dessous.

_Je tiens à remercier [Wes Wagner](https://www.freecodecamp.org/news/how-to-build-a-simple-social-media-monitor-with-nodejs-graphql-and-vue-55ffe4124ab5/undefined) pour ses commentaires dans la rédaction de cet article._

Merci !

![Image](https://cdn-media-1.freecodecamp.org/images/1*SRAIx1jmXTBHByfDCOtZig.png)