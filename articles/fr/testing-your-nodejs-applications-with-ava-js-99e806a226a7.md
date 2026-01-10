---
title: Comment tester vos applications Node.js avec Ava.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-20T18:55:23.000Z'
originalURL: https://freecodecamp.org/news/testing-your-nodejs-applications-with-ava-js-99e806a226a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d8Lk-1QmDqhF0UeFH0FhXQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Comment tester vos applications Node.js avec Ava.js
seo_desc: 'By Nitish Phanse

  Why would you want to write test cases for your applications, anyway? Well, it’s
  a question a number of developers try to dodge, purely because it takes effort and
  time, and because manual testing is so much more satisfying. Click… c...'
---

Par Nitish Phanse

Pourquoi voudriez-vous écrire des cas de test pour vos applications, de toute façon ? Eh bien, c'est une question à laquelle un certain nombre de développeurs essaient d'échapper, purement parce que cela prend du temps et des efforts, et parce que les tests manuels sont tellement plus satisfaisants. Cliquez... cliquez... remplissez un formulaire... Cliquez... Presto. Mon application fonctionne, mes API sont bonnes, tout est parfait.

Avancez rapidement jusqu'à presque 30 pull requests par jour étant fusionnées dans votre branche master. Maintenant, comment vous sentez-vous à l'idée de tester 30 fonctionnalités manuellement ou de refactoriser un bloc de code et de casser involontairement le code de quelqu'un d'autre ?

À ce stade, vous diriez normalement : « Je souhaite avoir écrit quelques cas de test pour commencer. » Alors prenez un peu d'inspiration de Facebook : ils ont partagé un article assez cool [ici](https://code.facebook.com/posts/1716776591680069/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/), expliquant comment l'équipe a développé React 16 avec le développement piloté par les tests.

Les applications Node sont par elles-mêmes assez faciles à construire. Il y a beaucoup de soutien communautaire impliqué, et vous obtiendrez généralement ce dont vous avez besoin en demandant autour de vous. Les applications Node peuvent être un excellent serveur proxy pour un certain nombre de serveurs API, rendant ainsi leurs tests de points de terminaison plus cruciaux.

Dans cet article, j'ai couvert **comment configurer et écrire des cas de test unitaires de base avec des rapports de couverture pour les applications Node.js**_. Alors, plongeons-nous.

### Bonjour Ava

[Ava](https://github.com/avajs/ava) est un exécuteur de tests JavaScript. Il utilise la nature async I/O de Node et exécute des tests concurrents, réduisant ainsi considérablement vos temps de test.

#### Commençons

Dans votre répertoire de travail, créez un fichier `package.json` et ajoutez les packages suivants :

```
yarn add ava babel-register
```

Créez un dossier **tests**. Il est utile de garder vos tests au même endroit. Vous pouvez également y garder les modules/contrôleurs de test.

Votre fichier `package.json` mis à jour devrait maintenant ressembler à ceci :

```
{  "name": "ava-test",  "version": "1.0.0",  "description": "",  "main": "index.js",  "scripts": {    "start" : "node server.js",    "test": "node_modules/.bin/ava tests/**/*.test.js --verbose",    "test:watch": "node_modules/.bin/ava --verbose --watch"  },  "dependencies": {    "ava": "^0.23.0",    "babel-register": "^6.26.0"  },  "ava": {    "require": [      "babel-register"    ]  }}
```

Le module `babel-register` transpile le code ES6 au moment de l'exécution au cas où certaines machines fonctionneraient avec une ancienne version de Node qui ne supporte pas ES6. Le drapeau `verbose` nous donnera une sortie propre selon que nos tests échouent ou réussissent. Ce drapeau est très utile lors du débogage de vos tests, mais si vous écrivez des centaines de cas de test, vous voudrez peut-être le désactiver.

Dans votre fichier `tests/index.test.js`, vous pouvez ajouter votre premier cas de test :

L'avantage pratique d'Ava est qu'il vous permet d'exécuter des tests asynchrones, via des fonctions async await. La syntaxe est également assez simple. La méthode plan nous permet de mentionner explicitement le nombre d'assertions que nous aimerions avoir par test.

L'exécution de `yarn test` à partir de votre console vous donne la sortie suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yKpSSSM5lLRN25oksAHiXA.png)

En cas d'échec de l'un de nos tests, nous obtiendrions :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KFS2QoVG57Q30L656dxe0w.png)

C'est la beauté du mode `verbose`. Il vous donne une pile d'erreurs propre et aucune des traces de pile inutiles. En cas de rencontre d'une erreur d'exécution, vous verrez également une belle mise en évidence de la syntaxe.

Vous pouvez vraiment exploiter l'API Ava et utiliser son puissant outil d'assertion pour écrire des cas de test flexibles.

### Configuration de votre serveur Node

Jusqu'à présent, nous n'avons parlé que d'une configuration de base pour écrire des tests — et soyons francs, c'est assez simple. Donc dans cette section, j'expliquerai comment un simple serveur Node peut être lancé et ses points de terminaison testés avec Ava.

```
yarn add express body-parser 
```

Dans votre répertoire de travail, créez un fichier `app.js` et ajoutez le snippet suivant :

La raison pour laquelle j'ai exporté le module app est afin qu'il puisse être utilisé avec le serveur API mock dont Ava aura besoin pour exécuter vos tests.

Créez un nouveau fichier `server.js` et importez le module app pour démarrer le serveur.

L'exécution de npm start devrait démarrer votre serveur, et la navigation vers le point de terminaison http://localhost/status devrait vous donner une réponse 200OK.

**Super, donc notre serveur fonctionne.**

Un rapide coup d'œil au code montre que nous avons créé 3 points de terminaison : un point de terminaison de statut, un point de terminaison de salutation, et un point de terminaison d'enregistrement. Il y a une certaine validation sur le point de terminaison d'enregistrement, qui renvoie un 400 (Bad request) en cas de paramètres manquants dans le corps de la requête. La méthode de validation ci-dessus est assez naïve, mais elle sert notre objectif de test de point de terminaison — donc je vais m'en tenir à celle-ci.

> _Astuce pro : Vous pouvez toujours assigner la gestion des erreurs à un middleware et utiliser next pour invoquer le gestionnaire d'erreurs._

Écrivons quelques tests supplémentaires autour du point de terminaison. J'utiliserai le module [**supertest**](https://github.com/visionmedia/supertest). Il est très similaire à [superagent](https://github.com/visionmedia/superagent) : il utilise les mêmes API et a une syntaxe similaire. Donc, gagnant-gagnant.

Nous avons importé le module `app` précédemment exporté et l'avons passé à supertest. Supertest crée un serveur proxy, qui frappera ensuite toutes les URL de points de terminaison mentionnées dans le test. Vous pouvez utiliser la méthode `**deepEqual**` pour tester l'objet entier ou la méthode `**is**` pour tester manuellement chaque champ.

L'exécution de yarn test donnera le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fm2ye0fObwshLJrRVOpDLQ.png)

Super. Nous avons écrit quatre tests et ils passent tous comme prévu. Mais qu'en est-il de la couverture de code ?

### **Bonjour nyc**

Pour créer ces jolis rapports de couverture, nous utiliserons [nyc](https://github.com/istanbuljs/nyc) qui est l'interface de ligne de commande d'Istanbul.js. Il est très facile à utiliser et dispose de nombreuses options configurables. Pour simplifier, nous utiliserons une configuration très simple.

```
yarn add nyc --save
```

La commande **nyc** s'enroule bien autour de votre commande de test et créera un dossier de couverture (celui-ci devrait être dans votre gitignore) dans votre répertoire de travail.

Mettez à jour votre `package.json` comme indiqué ci-dessous :

```
{  "name": "ava-test",  "version": "1.0.0",  "description": "",  "main": "index.js",  "scripts": {    "test": "node_modules/.bin/ava tests/**/*.test.js --verbose",    "test:watch": "node_modules/.bin/ava --verbose --watch",    "cover": "node_modules/.bin/nyc yarn test",  },  ... autres dépendances   "nyc": {    "reporter": [      "lcov",      "text",      "html"    ]  }}
```

Les types de rapporteur que vous souhaitez peuvent être configurés dans la section nyc de votre fichier `package.json`.

Exécutons yarn cover :

![Image](https://cdn-media-1.freecodecamp.org/images/1*whUkDdODhPlr5PBEhnndqw.png)

D'accord, donc nous n'avons pas encore 100% de couverture. Corrigons cela. D'abord, vous voudrez aller dans le dossier de couverture de votre répertoire de travail et voir quelle partie de votre code n'a pas été couverte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*D-7W9IuXIMoaRhnI2vxzWQ.png)

Clairement, nous avons manqué un endroit. Ajoutons notre dernier cas de test dans le fichier `tests/index.tests.js`, qui couvrira l'ensemble du fichier `app.js`.

```
test('Créer un nouvel utilisateur', async t => {  let username = 'some-hase'  const password = 'some-hase'  const response = await request(app)    .post('/register')    .send({username, password});
```

```
t.is(response.status, 200);    t.is(response.body.message, `nouvel utilisateur créé`);});
```

Et maintenant...

![Image](https://cdn-media-1.freecodecamp.org/images/1*jy3XmIeypPeFL_CqW7gVrA.png)

Presto.

> **_Astuce pro:_** _Si vous voulez ajouter un seuil pour les cas de test, vous pouvez ajouter un script dans votre fichier package.json._

```
"check-coverage": "node_modules/.bin/nyc check-coverage --lines 100 --functions 100 --branches 100 --statements 100"
```

Cette commande peut être exécutée dans le cadre de vos systèmes de construction de pipeline travis / gitlab.

### **Conclusion**

Nous avons couvert une configuration de base avec Ava pour les cas de test unitaires de vos API Node. La documentation est vraiment extensive et peut être consultée en cas de doute.

PS : J'espère que vous aimez l'article, corrigez-moi si je me trompe quelque part. Toujours ouvert à une discussion.