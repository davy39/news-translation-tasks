---
title: Express.js et AWS Lambda — une histoire d'amour sans serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-15T13:18:11.000Z'
originalURL: https://freecodecamp.org/news/express-js-and-aws-lambda-a-serverless-love-story-7c77ba0eaa35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FOKLXN58KdHMIXnq9XmMbQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: Express.js et AWS Lambda — une histoire d'amour sans serveur
seo_desc: 'By Slobodan Stojanović

  If you are a Node.js developer or you’ve built an API with Node.js, there’s a big
  chance you used Express.js. Express is de facto the most popular Node.js framework.

  Express apps are easy to build. For a simple app, you just ne...'
---

Par Slobodan Stojanović

Si vous êtes un développeur Node.js ou si vous avez construit une API avec Node.js, il y a de grandes chances que vous ayez utilisé [Express.js](https://expressjs.com). Express est *de facto* le framework Node.js le plus populaire.

Les applications Express sont faciles à construire. Pour une application simple, vous devez simplement ajouter quelques routes et des gestionnaires de routes. C'est tout.

![Image](https://cdn-media-1.freecodecamp.org/images/jPiykM308q60-GoIAAHpb29s8rCZwICxw8Ql)
_Une application Express.js simple, hébergée traditionnellement, avec une seule requête._

Par exemple, l'application Express la plus simple ressemble au extrait de code suivant :

```
'use strict'
```

```
const express = require('express')const app = express()
```

```
app.get('/', (req, res) => res.send('Hello world!'))
```

```
const port = process.env.PORT || 3000app.listen(port, () =>   console.log(`Server is listening on port ${port}.`))
```

Si vous enregistrez cet extrait de code sous _app.js_ dans un nouveau dossier, vous n'êtes qu'à trois étapes de disposer d'une application Express simple :

1. Créez un nouveau projet Node.js. Pour ce faire, exécutez la commande `npm init -y` dans votre terminal. Assurez-vous simplement d'avoir d'abord navigué vers le dossier contenant `app.js`.
2. Installez le module Express depuis NPM en exécutant la commande `npm install express --save` depuis le terminal.
3. Exécutez la commande `node app.js`, et vous devriez voir « Server is listening on port 3000. » en réponse.

Et voilà ! Vous avez une application Express. Visitez http://localhost:3000 dans votre navigateur, et vous verrez un message « Hello world ! ».

### Déploiement de l'application

Maintenant vient la partie difficile : comment pouvez-vous la montrer à vos amis ou à votre famille ? Comment la rendre disponible pour tout le monde ?

Le déploiement peut être un processus long et douloureux, mais imaginons que vous parvenez à le faire rapidement et avec succès. Votre application est disponible pour tout le monde et elle a vécu heureuse pour toujours.

Jusqu'au jour où une armée inattendue d'utilisateurs a commencé à l'utiliser.

Votre serveur a lutté, mais il a fonctionné.

![Image](https://cdn-media-1.freecodecamp.org/images/ueApaQnpCr59fOa5uoPBwHQsJRTHcbzr9FHn)
_Une application Express.js simple, hébergée traditionnellement, sous charge._

Au moins pendant un certain temps. Et puis elle est morte. ☠️

![Image](https://cdn-media-1.freecodecamp.org/images/S4odA9NYozNbrZ1hHjZ3avcFeo2SO15oVJah)
_Une application Express.js simple, mais morte, hébergée traditionnellement, qui a planté parce que trop d'utilisateurs y ont accédé._

Une armée d'utilisateurs est en colère (au moins ils n'ont pas payé pour l'application — ou l'ont-ils fait ?) Vous êtes désespéré et essayez de chercher la solution sur Google. Le cloud peut-il aider ?

![Image](https://cdn-media-1.freecodecamp.org/images/ExXxV2mNOs2LIgwTyPX1svo1xZkdEQQ6ycWi)
_Le cloud devrait résoudre vos problèmes de mise à l'échelle, non ?_

Et vous avez rencontré l'un de vos amis énervants. Elle parle encore de ce truc sans serveur. Mais allons, vous avez toujours un serveur. Il appartient simplement à quelqu'un d'autre et vous n'avez aucun contrôle dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/xZJgWMPLs-Mi-hsYtrp6vps2HQyI6h3uA8Wf)
_Mais, il y a des serveurs !_

Mais vous êtes désespéré, vous essayeriez n'importe quoi, y compris la magie noire et même le sans serveur. « Qu'est-ce que ce truc sans serveur, de toute façon ? »

Vous vous êtes retrouvé avec de nombreux liens, y compris celui vers le [premier chapitre gratuit](https://livebook.manning.com/?utm_source=twitter&utm_medium=social&utm_campaign=book_serverlessappswithnodeandclaudiajs&utm_content=medium#!/book/serverless-apps-with-node-and-claudiajs/chapter-1/) de « Serverless Applications with Node.js » de Manning Publications.

Ce chapitre explique le sans serveur avec des machines à laver !? Cela semble fou, mais cela a un certain sens. 💩 a déjà frappé le ventilateur, alors vous décidez de l'essayer.

### Rendre votre application Express.js sans serveur

Ce chapitre parlait du sans serveur sur AWS. Et maintenant vous savez que l'API Serverless se compose d'une API Gateway et de fonctions AWS Lambda. Mais comment pouvez-vous passer au sans serveur avec votre application Express ?

Cela semble aussi prometteur que ce film sur Matt Damon qui rétrécit...

![Image](https://cdn-media-1.freecodecamp.org/images/CAukVX9EmOszN8MqqTioMl6ARqgdrJQHu3pv)
_Comment faire tenir votre application Express.js dans AWS Lambda ?_

[Claudia](https://claudiajs.com) pourrait vous aider à déployer votre application sur AWS Lambda — demandons-lui de l'aide !

Assurez-vous d'avoir configuré vos identifiants d'accès AWS comme expliqué dans [ce tutoriel](https://claudiajs.com/tutorials/installing.html) avant d'exécuter les commandes Claudia.

Votre code doit être légèrement modifié pour prendre en charge AWS Lambda et le déploiement via Claudia. Vous devez exporter votre `app` au lieu de démarrer le serveur en utilisant `app.listen`. Votre `app.js` devrait ressembler à la liste de code suivante :

```
'use strict'
```

```
const express = require('express')const app = express()
```

```
app.get('/', (req, res) => res.send('Hello world!'))
```

```
module.exports = app
```

Cela casserait un serveur Express local, mais vous pouvez ajouter un fichier `app.local.js` avec le contenu suivant :

```
'use strict'
```

```
const app = require('./app')
```

```
const port = process.env.PORT || 3000app.listen(port, () =>   console.log(`Server is listening on port ${port}.`))
```

Puis exécutez le serveur local en utilisant la commande suivante :

```
node app.local.js
```

Pour que votre application fonctionne correctement avec AWS Lambda, vous devez générer un wrapper AWS Lambda pour votre application Express. Avec Claudia, vous pouvez le faire en exécutant la commande suivante dans votre terminal :

```
claudia generate-serverless-express-proxy --express-module app
```

où `app` est le nom d'un fichier d'entrée de votre application Express, sans l'extension `.js`.

Cette étape a généré un fichier nommé `lambda.js`, avec le contenu suivant :

```
'use strict'const awsServerlessExpress = require('aws-serverless-express')const app = require('./app')const binaryMimeTypes = [  'application/octet-stream',  'font/eot',  'font/opentype',  'font/otf',  'image/jpeg',  'image/png',  'image/svg+xml']const server = awsServerlessExpress  .createServer(app, null, binaryMimeTypes)exports.handler = (event, context) =>  awsServerlessExpress.proxy(server, event, context)
```

C'est tout ! Maintenant, vous devez simplement déployer votre application Express (avec le fichier `lambda.js`) sur AWS Lambda et API Gateway en utilisant la commande `claudia create`.

```
claudia create --handler lambda.handler --deploy-proxy-api --region eu-central-1
```

Après quelques instants, la commande s'est terminée et a imprimé la réponse suivante :

```
{  "lambda": {    "role": "awesome-serverless-expressjs-app-executor",    "name": "awesome-serverless-expressjs-app",    "region": "eu-central-1"  },  "api": {    "id": "iltfb5bke3",    "url": "https://iltfb5bke3.execute-api.eu-central-1.amazonaws.com/latest"  }}
```

Et si vous visitez le lien de cette réponse dans votre navigateur, il imprime « Hello world ! » Cela a fonctionné ! 🎉

![Image](https://cdn-media-1.freecodecamp.org/images/tp2YxJ0FlE5CNYnsNVXd9wvQnvPolDGI-8kR)
_Application Express sans serveur._

Avec une application sans serveur, votre armée d'utilisateurs peut continuer à croître et votre application continuera à fonctionner.

C'est possible, car AWS Lambda s'adaptera automatiquement jusqu'à 1000 exécutions simultanées par défaut. De nouvelles fonctions sont prêtes quelques instants après que l'API Gateway reçoit la requête.

![Image](https://cdn-media-1.freecodecamp.org/images/IXjAf4zo1k645HGOC9P-YSPqmYlss6wXRTUf)
_Application Express.js sans serveur sous charge lourde._

Mais ce n'est pas votre seul avantage. Vous avez également économisé de l'argent tout en ayant une application stable sous une charge plus élevée. Avec AWS Lambda, vous ne payez que pour les requêtes que vous avez utilisées. De plus, le premier million de requêtes chaque mois sont gratuites, dans le cadre d'un niveau gratuit.

![Image](https://cdn-media-1.freecodecamp.org/images/iAe-5ys7ROwR1NJ7vZIEOhNMmBhIVY89wdU3)
_Votre application sans serveur économise également votre argent !_

Pour en savoir plus sur les façons dont votre entreprise bénéficie du sans serveur, consultez [cet](https://hackernoon.com/7-ways-your-business-will-benefit-through-serverless-522b3f628a33) article.

### Limites des applications Express.js sans serveur

Les applications Express sans serveur semblent géniales, mais elles ont certaines limites.

![Image](https://cdn-media-1.freecodecamp.org/images/WfoHBlMIEMr7Z84f3r9XWili4O3zUy0DwmyX)
_Sans serveur, l'édition limitée._

Certaines des limites importantes des applications Express sans serveur sont les suivantes :

* Les _Websockets_ ne fonctionnent pas avec AWS Lambda. Cela est dû au fait que votre serveur n'existe pas lorsqu'il n'y a pas de requêtes. Un support limité pour les websockets est disponible via [AWS IOT websockets sur le protocole MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html#mqtt).
* Le _téléchargement_ vers le système de fichiers ne fonctionnera pas non plus, sauf si vous téléchargez vers le dossier `/tmp`. Cela est dû au fait que la fonction AWS Lambda est en lecture seule. Même si vous téléchargez des fichiers vers le dossier `/tmp`, ils existeront pendant une courte durée, tant que la fonction est encore « chaude ». Pour vous assurer que votre fonctionnalité de téléchargement fonctionne correctement, vous devez télécharger des fichiers vers AWS S3.
* Les _limites d'exécution_ peuvent également affecter votre application Express sans serveur. Parce que l'API Gateway a un délai d'attente de 30 secondes, et le temps d'exécution maximum d'AWS Lambda est de 5 minutes.

Ce n'est qu'un début d'une histoire d'amour sans serveur entre vos applications et AWS Lambda. Attendez-vous à plus d'histoires bientôt !

_Comme toujours, un grand merci à mes amis [Aleksandar Simović](https://twitter.com/simalexan) et [Milovan Jovićić](https://twitter.com/violinar) pour leur aide et leurs commentaires sur l'article._

> Toutes les illustrations sont créées à l'aide de l'application [SimpleDiagrams4](https://www.simplediagrams.com).

Si vous souhaitez en savoir plus sur Express sans serveur et les applications sans serveur en général, consultez « Serverless Applications with Node.js », le livre que j'ai écrit avec [Aleksandar Simovic](https://www.freecodecamp.org/news/express-js-and-aws-lambda-a-serverless-love-story-7c77ba0eaa35/undefined) pour Manning Publications :

[**Serverless Applications with Node.js**](https://www.manning.com/books/serverless-applications-with-nodejs)
[_Une introduction convaincante aux déploiements sans serveur utilisant Claudia.js._www.manning.com](https://www.manning.com/books/serverless-applications-with-nodejs)

Le livre vous apprendra davantage sur les applications Express sans serveur, mais vous apprendrez également à construire et déboguer une API sans serveur réelle (avec base de données et authentification) en utilisant Node et Claudia.js. Et comment construire des chatbots, pour Facebook Messenger et SMS (en utilisant Twilio), et des compétences Alexa.