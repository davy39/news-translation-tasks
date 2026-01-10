---
title: Un cours accéléré sur la sécurisation des API Serverless avec les JSON Web
  Tokens
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T22:56:20.000Z'
originalURL: https://freecodecamp.org/news/a-crash-course-on-securing-serverless-apis-with-json-web-tokens-ff657ab2f5a5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AxeOW_M6gdCts83RVl2aaQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un cours accéléré sur la sécurisation des API Serverless avec les JSON
  Web Tokens
seo_desc: 'By Adnan Rahić

  What a mouthful of a title. Wouldn’t you agree? In this walkthrough you’ll learn
  about securing your Serverless endpoints with JSON web tokens.

  This will include a basic setup of a Serverless REST API with a few endpoints, and
  of cours...'
---

Par Adnan Rahić

Quel titre à rallonge. N'est-ce pas ? Dans ce guide, vous apprendrez à sécuriser vos endpoints Serverless avec des JSON Web Tokens.

Cela inclura une configuration de base d'une API REST Serverless avec quelques endpoints, et bien sûr une fonction **authorizer**. Cette fonction **authorizer** agira comme un middleware pour autoriser l'accès à vos ressources.

Lors du processus de création, nous utiliserons le [Framework Serverless](https://serverless.com/) pour simuler un environnement de développement comme celui auquel vous êtes habitué. Pour conclure le guide, nous configurerons également un outil de surveillance appelé [Dashbird](https://dashbird.io/). Il nous permettra de simuler les capacités de débogage et de donner un aperçu d'une application Node.js régulière d'une manière naturelle et facile à comprendre. Il dispose également d'un [niveau gratuit](https://dashbird.io/pricing/) et ne nécessite pas de carte de crédit pour la configuration.

Si quelque chose de ce que je viens de mentionner est nouveau pour vous, ne vous inquiétez pas. Je vais tout expliquer ci-dessous. Sinon, vous pouvez rafraîchir vos connaissances en jetant un coup d'œil à ces tutoriels :

* [Sécuriser les API RESTful Node.js avec JWT](https://medium.freecodecamp.org/securing-node-js-restful-apis-with-json-web-tokens-9f811a92bb52) — Authentification et autorisation expliquées.
* [Un cours accéléré sur Serverless avec Node.js](https://hackernoon.com/a-crash-course-on-serverless-with-node-js-632b37d58b44) — Les bases de Serverless expliquées.
* [Créer une API REST Serverless avec Node.js et MongoDB](https://hackernoon.com/building-a-serverless-rest-api-with-node-js-and-mongodb-2e0ed0638f47) — Les API REST Serverless expliquées.

### TL;DR

Avant de plonger tête baissée, vous pouvez gravement blesser mes sentiments et ne lire que ce TL;DR. Ou, continuez à lire l'article entier. ❤️

* [**Création de l'API**](https://medium.com/p/ff657ab2f5a5#2aa5)  
- [Ajout d'une base de données](https://medium.com/p/ff657ab2f5a5#8132)  
- [Ajout des fonctions](https://medium.com/p/ff657ab2f5a5#e344)  
- [Ajout de la logique métier pour les utilisateurs](https://medium.com/p/ff657ab2f5a5#5845)  
- [Ajout de l'authentification](https://medium.com/p/ff657ab2f5a5#5663)  
- [Ajout de l'autorisation](https://medium.com/p/ff657ab2f5a5#40d6)
* [**Déploiement**](https://medium.com/p/ff657ab2f5a5#52e1)
* [**Test**](https://medium.com/p/ff657ab2f5a5#2e10)
* [**Surveillance**](https://medium.com/p/ff657ab2f5a5#6e91)

Prêt ? C'est parti !

### Création de l'API

Tout d'abord, nous devons configurer le Framework Serverless pour notre environnement de développement local. Ce framework est le framework *de facto* pour tout ce qui concerne les architectures Serverless. Rendez-vous sur [leur site](https://serverless.com/) et suivez les instructions pour le configurer, ou référez-vous à [l'article que j'ai lié ci-dessus](https://hackernoon.com/a-crash-course-on-serverless-with-node-js-632b37d58b44).

Le processus d'installation est incroyablement simple. Vous configurez un rôle de gestion AWS dans votre compte AWS, et vous le liez à votre installation du Framework Serverless. Le processus d'installation réel consiste simplement à exécuter une commande simple.

Ouvrez une fenêtre de terminal et exécutez la commande ci-dessous.

```
$ npm install -g serverless
```

Ensuite, une fois que vous l'avez installé, il n'y a qu'une seule commande à exécuter dans le terminal pour obtenir un service Serverless de base sur votre machine de développement local.

```
$ sls create -t aws-nodejs -p api-with-auth
```

La commande ci-dessus générera le code de base dont vous avez besoin.

Changez pour le répertoire nouvellement créé appelé `api-with-auth` et ouvrez-le avec votre éditeur de code préféré.

```
$ cd api-with-auth
```

Une fois ouvert, vous verrez deux fichiers principaux. Un fichier `handler.js` et un fichier `serverless.yml`. Le fichier `handler.js` contient la logique de notre application tandis que le fichier `serverless.yml` définit nos ressources.

Maintenant, il est temps d'installer quelques dépendances afin de configurer nos méthodes d'authentification/autorisation nécessaires, le chiffrement des mots de passe et l'ORM pour l'interaction avec la base de données.

```
$ npm init -y
$ npm install --save bcryptjs bcryptjs-then jsonwebtoken mongoose
```

Voici ce dont nous avons besoin pour la production, mais pour le développement, nous prendrons le plugin Serverless Offline.

```
$ npm install --save-dev serverless-offline
```

Super !

#### Ajout d'une base de données

Pour le stockage de données persistant, nous allons simplement prendre une instance MongoDB hébergée sur [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). [Voici](https://hackernoon.com/building-a-serverless-rest-api-with-node-js-and-mongodb-2e0ed0638f47) une référence pour un article où je l'ai expliqué en détail.

À la racine du dossier de service, créons un fichier `db.js` pour garder notre logique de connexion à la base de données. Allez-y et collez ce snippet de code.

Il s'agit d'une implémentation assez simple pour établir une connexion à la base de données si aucune connexion n'existe. Mais, si elle existe, j'utiliserai la connexion déjà établie. Vous voyez le `process.env.DB` ? Nous utiliserons un fichier `secrets.json` personnalisé pour garder nos clés privées hors de GitHub en l'ajoutant au `.gitignore`. Ce fichier sera ensuite chargé dans le `serverless.yml`. En fait, faisons cela maintenant.

Ajoutez votre chaîne de connexion MongoDB au champ `db`.

Avec ce fichier créé, passons au `serverless.yml`. Ouvrez-le et supprimez tout le code de base afin que nous puissions commencer frais. Ensuite, allez-y et collez ceci.

Comme vous pouvez le voir, il s'agit simplement d'une configuration de base. La section `custom` indique à la configuration principale de récupérer les valeurs d'un fichier `secrets.json`. Nous ajouterons ce fichier au `.gitignore` car pousser des clés privées vers GitHub est un péché mortel punissable de mort ! Non, pas vraiment, mais quand même, ne poussez pas de clés vers GitHub. Sérieusement, s'il vous plaît, ne le faites pas.

#### Ajout des fonctions

Juste un petit peu de configuration à faire avant de plonger dans la logique métier ! Nous devons ajouter les définitions de fonction dans le `serverless.yml` juste en dessous de la section des fournisseurs que nous avons ajoutée ci-dessus.

Il y a un total de cinq fonctions.

* Le `VerifyToken.js` contiendra une méthode `.auth` pour vérifier la validité du JWT passé avec la requête au serveur. Ce sera notre fonction **authorizer**. Le concept de fonctionnement d'un authorizer est très similaire à celui d'un middleware dans le bon vieux Express.js de base. Juste une étape entre la réception de la requête par le serveur et la gestion des données à renvoyer au client.
* Les fonctions `login` et `register` effectueront l'authentification de base de l'utilisateur. Nous ajouterons la logique métier pour celles-ci dans le fichier `AuthHandler.js`.
* Cependant, la fonction `me` répondra avec l'utilisateur actuellement authentifié en fonction du JWT fourni. C'est là que nous utiliserons la fonction **authorizer**.
* La fonction `getUsers` est simplement une API publique générique pour récupérer les utilisateurs enregistrés dans la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OkT0fGBzGM7Ig6ZkAkdwSw.png)

À partir du fichier `serverless.yml` ci-dessus, vous pouvez distinguer une structure de projet approximative. Pour la rendre plus claire, regardez l'image ci-dessus.

Cela a un peu plus de sens maintenant ? Continuons et ajoutons la logique pour récupérer les utilisateurs.

#### Ajout de la logique métier pour les utilisateurs

De retour dans votre éditeur de code, supprimez le fichier `handler.js` et créez un nouveau dossier, en le nommant `user`. Ici, vous ajouterez un fichier `User.js` pour le modèle, et un `UserHandler.js` pour la logique réelle.

Assez simple si vous avez déjà écrit une application Node. Nous nécessitons Mongoose, créons le schéma, l'ajoutons à Mongoose en tant que modèle, et enfin l'exportons pour une utilisation dans le reste de l'application.

Une fois le modèle terminé, il est temps d'ajouter la logique de base.

Cela peut être un peu difficile à comprendre lorsque vous le voyez pour la première fois. Mais commençons par le haut.

En nécessitant le `db.js`, nous avons accès à la connexion de la base de données sur MongoDB Atlas. Avec notre logique personnalisée pour vérifier la connexion, nous nous sommes assurés de ne pas créer une nouvelle connexion une fois qu'une connexion a été établie.

La fonction auxiliaire `getUsers` ne récupérera que tous les utilisateurs, tandis que la fonction Lambda `module.exports.getUsers` se connectera à la base de données, exécutera la fonction auxiliaire et renverra la réponse au client. Cela est plus que suffisant pour le `UserHandler.js`. Le vrai plaisir commence avec le `AuthProvider.js`.

#### Ajout de l'authentification

À la racine de votre service, créez un nouveau dossier appelé `auth`. Ajoutez un nouveau fichier appelé `AuthHandler.js`. Ce gestionnaire contiendra la logique d'authentification principale pour notre API. Sans perdre plus de temps, allez-y et collez ce snippet dans le fichier. Cette logique permettra l'enregistrement des utilisateurs, l'enregistrement de l'utilisateur dans la base de données et le retour d'un jeton JWT au client pour le stockage dans les requêtes futures.

Tout d'abord, nous nécessitons les dépendances, et ajoutons la fonction `module.exports.register`. C'est assez simple. Nous nous connectons à nouveau à la base de données, enregistrons l'utilisateur et renvoyons un objet de session qui contiendra un jeton JWT. Regardez de plus près la fonction locale `register()`, car nous ne l'avons pas encore déclarée. Patience, nous y viendrons dans un instant.

Avec la structure de base correctement configurée, commençons par ajouter les fonctions auxiliaires. Dans le même fichier `AuthHandler.js`, allez-y et collez ceci également.

Nous avons créé trois fonctions auxiliaires pour signer un jeton JWT, valider la saisie de l'utilisateur et créer un utilisateur s'il n'existe pas déjà dans notre base de données. Super !

Avec la fonction `register()` terminée, nous devons encore ajouter la fonction `login()`. Ajoutez le `module.exports.login` juste en dessous du commentaire des fonctions.

Une fois de plus, nous avons une fonction locale, cette fois nommée `login()`. Ajoutons cela également sous le commentaire des fonctions auxiliaires.

Super ! Nous avons également ajouté les fonctions auxiliaires. Avec cela, nous avons ajouté l'**authentification** à notre API. Aussi simple que cela. Maintenant, nous avons un modèle d'authentification basé sur des jetons avec la possibilité d'ajouter une autorisation. Ce sera notre prochaine étape. Accrochez-vous !

#### Ajout de l'autorisation

Avec l'ajout d'un fichier `VerifyToken.js`, nous pouvons héberger toute la logique d'autorisation en tant que middleware séparé. Très pratique si nous voulons maintenir la séparation des préoccupations. Allez-y et créez un nouveau fichier appelé `VerifyToken.js` dans le dossier `auth`.

Nous avons une seule fonction exportée depuis le fichier, appelée `module.exports.auth` avec les trois paramètres habituels. Cette fonction agira comme un **middleware**. Si vous êtes familier avec Node.js, vous savez ce qu'est un middleware, sinon, consultez [ceci](https://medium.freecodecamp.org/securing-node-js-restful-apis-with-json-web-tokens-9f811a92bb52) pour une explication plus détaillée.

Le `authorizationToken`, notre JWT, sera passé au middleware via l'événement. Nous l'assignons simplement à une constante locale pour un accès plus facile.

Toute la logique ici consiste simplement à vérifier si le jeton est valide et à renvoyer une politique générée en appelant la fonction `generatePolicy`. Cette fonction est requise par AWS, et vous pouvez la récupérer à partir de diverses documentations sur AWS et de la page GitHub des [exemples du Framework Serverless](https://github.com/serverless/examples/blob/master/aws-node-auth0-custom-authorizers-api/handler.js).

C'est important car nous passons le `decoded.id` dans le `callback`. Cela signifie que la prochaine fonction Lambda qui se trouve derrière notre fonction **authorizer** `VerifyToken.auth` aura accès au `decoded.id` dans son paramètre `event`. Super, n'est-ce pas ?

Une fois que nous avons terminé la vérification du jeton, tout ce qui reste est d'ajouter une route pour se situer derrière la fonction **authorizer**. Pour simplifier, ajoutons une route `/me` pour récupérer l'utilisateur actuellement connecté en fonction du JWT passé avec la requête `GET`.

Retournez au fichier `AuthHandler.js` et collez ceci.

Super ! La dernière fonction Lambda que nous ajouterons dans ce tutoriel sera `module.exports.me`. Elle récupérera simplement le `userId` passé par l'**authorizer** et appellera la fonction auxiliaire `me` tout en passant le `userId`. La fonction `me` récupérera l'utilisateur de la base de données et le renverra. Tout ce que fait la fonction Lambda `module.exports.me` est de récupérer l'utilisateur actuellement authentifié. Mais, l'endpoint est protégé, ce qui signifie qu'un seul jeton valide peut y accéder.

Excellent travail en suivant jusqu'à présent, déployons-le afin que nous puissions faire quelques tests.

### Déploiement

Espérons que vous avez configuré votre compte AWS pour qu'il fonctionne avec le Framework Serverless. Si c'est le cas, il n'y a qu'une seule commande à exécuter, et vous êtes prêt.

```
$ sls deploy
```

Voilà ! Attendez qu'il se déploie, et commencez à profiter de votre API Serverless avec authentification et autorisation JWT.

Vous recevrez un ensemble d'endpoints renvoyés dans le terminal une fois les fonctions déployées. Nous en aurons besoin dans la section suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hexa4mq9xD91AfZCelMbVw.png)

### Test

La dernière étape de tout processus de développement devrait idéalement consister à s'assurer que tout fonctionne comme il se doit. Ce n'est pas une exception. L'un des deux outils que j'utilise pour tester mes endpoints est [Insomnia](https://insomnia.rest/). Donc, je vais l'ouvrir. Mais vous pouvez utiliser [Postman](https://www.getpostman.com/), ou tout autre outil que vous aimez.

**_Note_**_: Si vous voulez commencer par tout tester localement, soyez mon invité. Vous pouvez toujours utiliser [serverless-offline](https://www.freecodecamp.org/news/a-crash-course-on-securing-serverless-apis-with-json-web-tokens-ff657ab2f5a5/%20add%20link)._

Dans votre terminal, exécutez une commande simple :

```
$ sls offline start --skipCacheInvalidation
```

Mais j'aime aller à fond ! Testons directement sur les endpoints déployés.

Commençons lentement, d'abord, appelez l'endpoint `/register` avec une requête `POST`. Assurez-vous d'envoyer la charge utile en JSON. Cliquez sur **Envoyer** et vous recevrez un jeton en retour ! Bien, c'est exactement ce que nous voulions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zbCWN9qyIt0_8kWXwjszGQ.png)

Copiez le jeton et appelez maintenant l'endpoint `/me` avec une requête `GET`. N'oubliez pas d'ajouter le jeton dans les en-têtes avec la clé `Authorization`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n5QxngulaY-QFfGNUtgm8g.png)

Vous recevrez l'utilisateur actuel renvoyé. Et le voilà. Super.

Juste pour s'assurer que les autres endpoints fonctionnent également, appelez l'endpoint `/login` avec les mêmes informations d'identification que celles de l'endpoint `/register` que vous venez d'appeler.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vcc8I4KgAPw-O015G7_ySw.png)

Est-ce que cela fonctionne ? Bien sûr que oui. Nous y voilà, un système d'authentification et d'autorisation entièrement fonctionnel implémenté dans un environnement Serverless avec **JWT** et **Authorizers**. Il ne reste plus qu'à ajouter un moyen de tout surveiller.

### Surveillance

Je surveille généralement mes Lambdas avec [Dashbird](https://www.dashbird.io/). Cela a très bien fonctionné pour moi jusqu'à présent. Mon objectif en vous montrant cela est de vous permettre de voir les logs de la console à partir des invocations des fonctions Lambda. Ils vous montreront quand la Lambda utilise une nouvelle connexion de base de données ou une connexion existante. Voici à quoi ressemble le tableau de bord principal, où je vois toutes mes Lambdas et leurs statistiques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pMkJIIgerPBAeq9sf8T0Tg.png)

En appuyant sur l'une des fonctions Lambda, disons **register**, vous verrez les logs pour cette fonction particulière. Le bas affichera une liste des invocations pour la fonction. Vous pouvez même voir celles qui étaient des plantages et des démarrages à froid.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-yTb5eKa_Uj-X7nfPieLMw.png)

En appuyant sur l'invocation de démarrage à froid, vous serez redirigé vers la page d'invocation et vous verrez un joli log qui dit `=> using new database connection`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*unMBkIOwUIOv0EZvVYWr-Q.png)

Maintenant, revenez un peu en arrière et choisissez l'une des invocations qui n'est pas un démarrage à froid. En vérifiant les logs pour cette invocation, vous verrez `=> using existing database connection`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p5WdW_FEKohXcAtKEVfXcA.png)

Super ! Vous avez une vision claire de votre système !

### Conclusion

Incroyable ce que l'on peut faire avec quelques bons outils. Créer une API REST avec authentification et autorisation est simplifié avec [Serverless](# runtime: nodejs6.10), JWT, MongoDB et [Dashbird](https://dashbird.io). Une grande partie de l'approche de ce tutoriel a été inspirée par certains de mes tutoriels précédents. N'hésitez pas à les consulter ci-dessous.

[**Adnan Rahić - Medium**](https://medium.com/@adnanrahic)  
[_Lire les écrits d'Adnan Rahić sur Medium. Co-fondateur @bookvar_co. Enseignant @ACADEMY387. Auteur @PacktPub. Responsable de camping..._medium.com](https://medium.com/@adnanrahic)

L'approche consistant à utiliser des **authorizers** pour simuler des fonctions middleware est incroyablement puissante pour sécuriser vos API Serverless. C'est une technique que j'utilise quotidiennement. J'espère que vous la trouverez utile dans vos futures entreprises également !

Si vous souhaitez jeter un coup d'œil à tout le code que nous avons écrit ci-dessus, [voici le dépôt](https://github.com/adnanrahic/a-crash-course-on-serverless-auth). Ou si vous souhaitez approfondir le merveilleux monde de Serverless, jetez un coup d'œil à tous les outils que j'ai mentionnés ci-dessus, ou consultez [un cours que j'ai écrit](https://www.packtpub.com/web-development/serverless-javascript-example-video).

_J'espère que vous, les gars et les filles, avez apprécié la lecture de ceci autant que j'ai apprécié l'écrire. Pensez-vous que ce tutoriel sera utile à quelqu'un ? N'hésitez pas à le partager. Si vous l'avez aimé, cliquez sur le bouton **applaudir** ci-dessous pour que d'autres personnes puissent le voir ici sur Medium._