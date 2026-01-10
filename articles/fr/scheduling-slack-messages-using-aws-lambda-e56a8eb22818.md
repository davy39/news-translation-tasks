---
title: Planification de messages Slack à l'aide d'AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-24T09:42:41.000Z'
originalURL: https://freecodecamp.org/news/scheduling-slack-messages-using-aws-lambda-e56a8eb22818
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SC4rJV1oo4Q_jGkjAVwuwA.png
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Planification de messages Slack à l'aide d'AWS Lambda
seo_desc: 'By Slobodan Stojanovic

  Migrating to serverless brings a lot of questions. How do you do some of the non-serverless
  tasks, such as a cronjob in a serverless application?

  Let’s say you have a small Slack app that sends the top five stories from Hacker
  ...'
---

Par Slobodan Stojanovic

La migration vers le serverless soulève de nombreuses questions. Comment effectuer certaines des tâches non serverless, telles qu'un cronjob dans une application serverless ?

Imaginons que vous avez une petite application Slack qui envoie les cinq meilleures histoires de Hacker News à votre canal Slack. À un moment donné, vous avez décidé d'arrêter le serveur où vous exécutez cette application, mais vous souhaitez toujours recevoir les histoires. Le serverless avec AWS Lambda semble cool. Mais comment déclencher la fonction AWS Lambda à un moment spécifique ?

![Image](https://cdn-media-1.freecodecamp.org/images/yxY9HN0WQ-feWbL9t3GwVrMZwqwQn6pfIqYo)
_Tous les diagrammes sont créés à l'aide de l'application [SimpleDiagrams 4](https://www.simplediagrams.com" rel="noopener" target="_blank" title=")_

Au cas où vous ne seriez pas familier, le serverless est une méthode de déploiement et d'exécution d'applications sur une infrastructure cloud, sur une base de paiement à l'usage et sans louer ou acheter de serveurs. Pour en savoir plus sur le serverless et son fonctionnement avec AWS, consultez [ce guide](https://livebook.manning.com/#!/book/serverless-apps-with-node-and-claudiajs/chapter-1/v-5).

Vous pouvez déclencher des fonctions AWS Lambda avec une variété de services AWS, tels que API Gateway pour les API et S3 pour les fichiers. Pour la liste complète des services, voir la documentation [ici](https://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html). L'un des déclencheurs disponibles est [AWS CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html).

Attendez, CloudWatch n'est-il pas pour les logs ?

En effet. Mais il semble que quelqu'un chez AWS soit un grand fan de Dr. Jekyll et Mr. Hyde et dans certains cas, quelques services différents sont cachés derrière le même nom (bonjour [Cognito](https://aws.amazon.com/cognito/getting-started/)).

En plus de servir les logs, Amazon CloudWatch dispose d'événements qui fournissent un flux en temps quasi réel d'événements système décrivant les changements dans les ressources AWS. Les événements peuvent également planifier des actions automatisées à l'aide d'expressions cron ou de taux. Bingo !

### Flux de l'application

Comment l'application fonctionnerait-elle avec CloudWatch Events ?

Vous devez configurer un événement planifié CloudWatch en utilisant la [syntaxe cron](https://fr.wikipedia.org/wiki/Cron) ou une expression de taux (par exemple, 5 minutes). L'événement CloudWatch déclenche ensuite une fonction AWS Lambda à des intervalles configurés. Dans votre fonction AWS Lambda, vous obtenez les cinq meilleurs articles de l'API Hacker News et les publiez sur Slack en utilisant [Incoming Webhooks](https://api.slack.com/incoming-webhooks).

Vous pouvez voir le flux dans la figure ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/nRLfCXLIjaUsXISxyK-qQqFLbq6iJGLNySwJ)
_Le flux des messages Slack planifiés serverless_

Cela semble simple, n'est-ce pas ? Voyons comment cela fonctionne en pratique.

### Envoi de messages planifiés

Avant de commencer, pour pouvoir suivre ce tutoriel, vous devez avoir un compte AWS, et AWS CLI et Node.js (v6+) doivent être installés. Vous pouvez obtenir AWS CLI [ici](https://aws.amazon.com/cli/).

Vous aurez également besoin de configurer un Slack Incoming Webhook. Pour ce faire, suivez [ce tutoriel](https://api.slack.com/tutorials/slack-apps-hello-world). À la fin du tutoriel, vous obtiendrez l'URL du webhook. Enregistrez cette URL, car vous en aurez besoin dans peu de temps. Allez, faites-le, je vous attends ici ☕

Ok, le temps est écoulé ! Commençons avec la partie amusante.

Pour commencer, créez un nouveau dossier et démarrez un nouveau projet Node.js (vous pouvez utiliser la commande `npm init -y`).

Comme vous devrez envoyer quelques requêtes HTTP, installez le module [minimal request promise](https://www.npmjs.com/package/minimal-request-promise) depuis NPM en tant que dépendance. Pour ce faire, exécutez la commande suivante :

```
npm install minimal-request-promise --save
```

Minimal request promise est un petit module Node.js qui enveloppe simplement les modules HTTP et HTTPS natifs dans des Promesses JavaScript.

Maintenant que la dépendance est prête, examinons la figure suivante avec la structure du projet que nous allons utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/tth9sqtLCdMEiMc8Bh2u5PuiEiRom5N4N1eb)
_Structure des dossiers de votre projet_

Même si le code est simple, nous allons le diviser en quelques petits fichiers pour simplifier les tests (voir [l'introduction à l'architecture hexagonale](http://alistair.cockburn.us/Hexagonal+architecture) pour plus d'informations). Comme vous pouvez le voir dans la figure ci-dessus, votre code contient les fichiers suivants :

* `index.js` - le fichier initial pour votre fonction Lambda qui invoque les deux autres fichiers et répond à CloudWatch Events.
* `src/get-top-hackernews-stories.js` - un fichier qui obtient les cinq meilleures histoires avec des détails de Hacker News.
* `src/send-slack-message.js` - un fichier qui formate et envoie un message Slack.

Commençons par le fichier initial. Ce fichier nécessite simplement les deux autres fichiers et invoque la fonction `getTopHackerNewsStories` puis la fonction `sendSlackMessage`. Lorsque les deux fonctions sont prêtes, ou si une erreur se produit, il répond au déclencheur (CloudWatch Event).

Votre fichier `index.js` devrait ressembler au listing de code suivant.

Pour la lisibilité, il ne contient pas de validation d'événement, qui devrait être présente dans le code de production.

```
'use strict'
```

```javascript
const getTopHackerNewsStories = require('./src/get-top-hackernews-stories')
const sendSlackMessage = require('./src/send-slack-message')
```

```
function scheduledSlackMessage(event, context, callback) {  getTopHackerNewsStories()    .then(stories => sendSlackMessage(stories))    .then(() => callback(null))    .catch(callback)}
```

```
exports.handler = scheduledSlackMessage
```

La première des deux fonctions, `getTopHackerNewsStories`, effectue une requête HTTP à l'API [Hacker News API](https://github.com/HackerNews/API) (aucune authentification requise). Comme l'API retourne une liste d'IDs d'histoires, vous devez obtenir les cinq premiers IDs et envoyer une requête HTTP pour chaque ID, afin d'obtenir les détails de l'histoire. Enfin, vous devez analyser le corps de la réponse (parce que la promesse de requête minimale ne le fait pas sous le capot) et retourner les résultats.

Votre fichier `get-top-hackernews-stories.js` devrait ressembler au listing de code suivant.

```
'use strict'
```

```
const rp = require('minimal-request-promise')
```

```
function getTopNews() {  return rp.get('https://hacker-news.firebaseio.com/v0/topstories.json', {    'Content-Type': 'application/json'  })    .then(response => {      const storyIds = JSON.parse(response.body)
```

```
      return Promise.all(        storyIds.slice(0, 5)          .map(id => {            return rp.get(`https://hacker-news.firebaseio.com/v0/item/${id}.json`, {              'Content-Type': 'application/json'            })              .then(response => JSON.parse(response.body))          })      )    })}
```

```
module.exports = getTopNews
```

Lorsque vous obtenez les histoires, la fonction `sendSlackMessage` formate le message et envoie une autre requête HTTP à l'URL du Slack Incoming Webhook, comme le montre le listing de code suivant.

Au lieu de coder en dur l'URL du Incoming Webhook, nous allons la passer en tant que variable d'environnement AWS Lambda. Pour en savoir plus sur les variables d'environnement et d'autres moyens de partager des secrets dans les applications serverless, consultez [ce guide](https://livebook.manning.com/#!/book/serverless-apps-with-node-and-claudiajs/chapter-14/v-5/92).

```
'use strict'
```

```
const rp = require('minimal-request-promise')
```

```
function sendSlackMessage(news, url = process.env.SlackWebhookUrl) {  const body = JSON.stringify({    text: 'Les posts suivants sont tendance sur Hacker News :',    attachments: news.map(item => ({      'author_name': `${item.score} points par ${item.by}`,      title: item.title,      'title_link': item.url    }))  })
```

```
  return rp.post(url, {    headers: {      'Content-Type': 'application/json'    },    body: body  })}
```

```
module.exports = sendSlackMessage
```

Maintenant que le code est prêt, déployons l'application et planifions les messages.

### Déploiement, configuration et test de l'application

Nous allons utiliser [Claudia.js](https://claudiajs.com) pour déployer notre fonction sur AWS Lambda. Avant de continuer, assurez-vous de suivre [ce tutoriel](https://claudiajs.com/tutorials/installing.html) pour installer Claudia et configurer les informations d'identification d'accès AWS.

De plus, vous devrez créer le fichier `env.json` dans votre dossier de projet, pour définir l'URL du Webhook Slack. Ce fichier doit avoir un contenu similaire au listing de code suivant. Assurez-vous de remplacer l'URL générique par celle que vous avez reçue lorsque vous avez configuré l'application Slack.

```
{  "SlackWebhookUrl": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"}
```

Maintenant que tout est prêt, exécutez la commande suivante dans votre terminal pour déployer votre application :

```
claudia create --region eu-central-1 --handler index.handler --timeout 10 --set-env-from-json env.json
```

Dans cette commande, vous faites les choses suivantes :

* Définissez _la région_ où votre fonction Lambda sera déployée. Pour la liste complète des régions prises en charge, voir [la documentation](https://docs.aws.amazon.com/general/latest/gr/rande.html#lambda_region).
* Définissez le fichier de gestionnaire, qui est un chemin relatif vers votre fichier de point d'entrée, mais avec une extension `.handler` au lieu de `.js`.
* Définissez _le délai d'attente_, car le délai d'attente par défaut d'AWS Lambda est de 3 secondes, mais vous devez effectuer quelques requêtes HTTP. Pour être sûr, augmentez le délai d'attente à au moins 10 secondes.
* Définissez _les variables d'environnement_ à partir du fichier JSON que vous avez préparé.

Après quelques secondes, vous recevrez une réponse JSON comme dans l'exemple ci-dessous. Vous verrez également le fichier `claudia.json` dans votre dossier de projet.

```
{  "lambda": {    "role": "scheduled-slack-messages-executor",    "name": "scheduled-slack-messages",    "region": "eu-central-1"  }}
```

Cela signifie que votre fonction AWS Lambda est prête.

L'étape suivante consiste à créer un événement CloudWatch. Supposons que vous souhaitiez recevoir un message tous les jours à 10h00 CET, car votre cron s'exécute dans le fuseau horaire GMT. Votre commande cron devrait ressembler à ceci : `cron(0 9 * * ? *)`.

Pour configurer un événement tous les jours à 10h00, exécutez la commande suivante depuis votre terminal :

```
aws events put-rule --name hackerNewsDigest --schedule-expression 'cron(0 9 * * ? *)'
```

Cette commande affichera l'ARN de la règle, que vous devrez enregistrer car vous en aurez besoin dans un instant.

Les noms de ressources Amazon (ARN) sont des identifiants uniques des ressources AWS. Lisez plus sur les ARN dans la documentation [ici](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

Maintenant que votre événement CloudWatch est prêt, vous devez lui permettre de déclencher une fonction Lambda. Pour ce faire, exécutez la commande suivante depuis votre terminal :

```
aws lambda add-permission \  --statement-id 'hackernews-scheduled-messages' \  --action 'lambda:InvokeFunction' \  --principal 'events.amazonaws.com' \  --source-arn ruleArn \  --function-name functionName \  --region region
```

Dans cette commande :

* `ruleArn` est l'ARN de la règle d'événement CloudWatch que vous avez reçue après avoir exécuté la commande précédente.
* `functionName` est le nom de votre fonction dans votre fichier `claudia.json`.
* `region` est la région de votre fichier `claudia.json`.

Votre commande retournera une réponse JSON. Trouvez la **Resource** dans la réponse et copiez l'**ARN** de Lambda. Il devrait ressembler à ceci :

* _arn:aws:lambda:eu-central-1:123456789012:function:scheduled-slack-messages_

Enfin, vous devrez définir le déclencheur en exécutant la commande suivante depuis votre terminal :

```
aws events put-targets --rule hackerNewsDigest --targets '[{ "Id": "1", "Arn": "votre ARN Lambda" }]'
```

Et voilà, votre événement Slack planifié est prêt. Le lendemain à 10h00 CET, vous devriez recevoir un message qui ressemble à la figure suivante.

Si vous ne pouvez pas attendre 10h00 et que vous souhaitez voir le résultat plus tôt, exécutez la commande `claudia test-lambda` depuis votre terminal. Assurez-vous de naviguer d'abord vers votre dossier de projet.

![Image](https://cdn-media-1.freecodecamp.org/images/eqh0Xc8b2BzNL4H6nLBcOq8yGSwOaySx4fyX)
_Message reçu dans Slack_

D'autres articles similaires sont en route. Si vous souhaitez rester à jour avec mes nouveaux articles, ou si vous avez un sujet que vous aimeriez lire, suivez-moi et contactez-moi sur twitter - [twitter.com/slobodan_](https://twitter.com/slobodan_).

_Comme toujours, un grand merci à mon ami [Aleksandar Simović](https://twitter.com/simalexan) pour son aide et ses commentaires sur l'article._

> Toutes les illustrations sont créées à l'aide de l'application [SimpleDiagrams4](https://www.simplediagrams.com).

Si vous souhaitez en savoir plus sur les applications serverless en général, consultez « Serverless Apps with Node and Claudia.js », le livre que j'ai écrit avec [Aleksandar Simovic](https://www.freecodecamp.org/news/scheduling-slack-messages-using-aws-lambda-e56a8eb22818/undefined) pour Manning Publications.

[**Serverless Apps with Node and Claudia.js**](https://www.manning.com/books/serverless-apps-with-node-and-claudiajs)  
[_D'abord les mots à la mode : Serverless computing. AWS Lambda. API Gateway. Node.js. Microservices. Cloud-hosted functions…www.manning.com](https://www.manning.com/books/serverless-apps-with-node-and-claudiajs)

Le livre vous apprendra à construire et déboguer des API serverless réelles (avec DB, authentification et tests) en utilisant Node et Claudia.js. Il couvre également la migration de votre application existante qui s'exécute sur des serveurs vers une application serverless, comment construire des chatbots pour Facebook Messenger et SMS (en utilisant Twilio), et des compétences Alexa.