---
title: Créer un point de terminaison REST API simple en utilisant Webtask.io
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-01T09:18:04.000Z'
originalURL: https://freecodecamp.org/news/create-a-simple-rest-api-endpoint-using-webtask-io-d9607fc00c17
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NeGT5gT1GaOUWOC-ZSRlag.jpeg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Créer un point de terminaison REST API simple en utilisant Webtask.io
seo_desc: 'By ismapro

  Webtask.io is a service by Auth0 that allows you to run single pieces of code in
  the cloud through HTTP calls.

  Each deployed piece will run under a sandbox with some limitations:


  limited processor time

  a limited amount of libraries availa...'
---

Par ismapro

Webtask.io est un service d'Auth0 qui vous permet d'exécuter des morceaux de code individuels dans le cloud via des appels HTTP.

Chaque morceau déployé s'exécutera dans un bac à sable avec certaines limitations :

* temps de processeur limité
* une quantité limitée de bibliothèques disponibles par tâche
* stockage limité

Mais ces limitations servent à présenter un environnement où vous pouvez exposer votre application via _HTTP_, de manière simple et scalable, sans vous soucier des détails de l'administration serveur ou des configurations d'environnement.

Il existe de nombreuses autres fonctionnalités disponibles comme la validation de jetons pour contrôler l'accès, les données secrètes et les métadonnées. Si vous souhaitez en savoir plus sur le fonctionnement de Webtask, [leur documentation](https://webtask.io/docs/how) contient des exemples de ce que vous pouvez faire avec cette technologie.

#### Commençons à coder l'API REST de base

Pour créer une webtask, vous devrez utiliser _webtask-cli_. Il s'agit d'une application en ligne de commande qui vous permet de gérer vos webtasks.

Installez-la d'abord dans votre environnement :

```
npm install wt-cli -g
```

Ensuite, initialisez votre session en utilisant ce processus de connexion par email :

```
wt init votre_email@quelquechose.com
```

Une fois cela fait, vous devriez recevoir un code pour activer votre compte.

Vous pouvez maintenant procéder à la création du fichier qui contiendra la logique de notre webtask. Vous pouvez le nommer comme vous le souhaitez, mais rappelez-vous qu'il fera partie de l'URL que le service fournira plus tard. Nommons-le :

```
basic-rest.js
```

et ajoutons le code suivant :

Naviguez depuis la ligne de commande vers l'emplacement où vous avez enregistré le fichier et exécutez cette commande :

```
wt create basic-rest.js
```

Vous recevrez une URL que vous pouvez utiliser pour vérifier votre webtask, similaire à celle-ci :

```
https://webtask.it.auth0.com/api/run/wt-monemail-gmail_com-0/basic-rest?webtask_no_cache=1
```

Depuis votre navigateur, accédez à votre URL et vous verrez la réponse de votre application :

```
{"error":"La méthode GET n'est pas implémentée"}
```

Ce qui est la réponse que nous attendions de notre code. Vous pouvez maintenant ajouter toute logique que vous souhaitez à chacune des méthodes. Vous pouvez ensuite tester les autres méthodes (POST, DELETE, PUT) en utilisant Postman ou curl.

Et c'est tout. Vous avez déployé un service sans aucune configuration ou administration supplémentaire. L'avantage de ce service est la capacité d'intégrer des webhooks depuis des API externes et d'interagir avec les données ou de faire des requêtes en utilisant d'autres backends.

Il existe de nombreuses fonctionnalités et options que je n'ai pas explorées, mais vous pouvez consulter [leur page web](https://webtask.io) pour en savoir plus.

_J'espère que cela vous a plu, faites-moi savoir ce que vous en pensez dans la section des commentaires. Bon codage !_