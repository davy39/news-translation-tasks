---
title: Comment accélérer le développement serverless en simulant AWS Lambda localement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-28T19:41:14.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-speed-up-serverless-development-by-simulating-aws-lambda-locally-41c61a60fbae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E980zTsgOV5Cpc5JdmXs2A.jpeg
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment accélérer le développement serverless en simulant AWS Lambda localement
seo_desc: 'By John McKim

  Designing AWS Lambda functions can be a frustrating experience. Each time you make
  a change, you have to deploy your code to AWS before you can test it. Well, my friend
  and I finally decided to do something about this.

  The end result is...'
---

Par John McKim

Concevoir des fonctions [AWS Lambda](https://aws.amazon.com/lambda/) peut être une expérience frustrante. Chaque fois que vous apportez une modification, vous devez déployer votre code sur AWS avant de pouvoir le tester. Eh bien, [mon ami](https://twitter.com/gertjvr81) et moi avons finalement décidé de faire quelque chose à ce sujet.

Le résultat final est le [Serverless Simulate Plugin](https://github.com/gertjvr/serverless-plugin-simulate). Ce plugin est un simulateur AWS Lambda et API Gateway pour le Serverless Framework.

Je vais vous expliquer comment nous l'avons construit et comment vous pouvez commencer à l'utiliser lorsque vous développez des applications serverless.

![Image](https://cdn-media-1.freecodecamp.org/images/J0xqnDbXf3ACqsKwbYKqhR-9j94Dr7Depp8E)

### Simulation d'API Gateway

API Gateway fournit des endpoints HTTP qui invoquent des fonctions Lambda en réponse aux requêtes.

API Gateway mappe la requête HTTP entrante à un payload d'événement pour Lambda. Lorsque la fonction Lambda retourne un résultat, le résultat est mappé à une réponse HTTP.

![Image](https://cdn-media-1.freecodecamp.org/images/JDwRNzjdJbzytCfcNjsDDUKaN1AFl7Ncj0-h)

Bien qu'API Gateway ait de nombreuses fonctionnalités, la plupart des développeurs n'en utilisent que quelques-unes. Nous avons choisi de n'implémenter que les fonctionnalités couramment utilisées par les développeurs Serverless.

#### Serveur HTTP

Pour simuler API Gateway, le plugin crée un serveur HTTP avec [express](http://expressjs.com/). Le plugin lit le [fichier de configuration Serverless](https://serverless.com/framework/docs/providers/aws/guide/serverless.yml/) et crée des endpoints à partir des [événements HTTP](https://serverless.com/framework/docs/providers/aws/events/apigateway/).

Si l'endpoint a activé CORS, le plugin ajoutera un [CORS Middleware](https://github.com/expressjs/cors) à l'endpoint.

#### Autorisateurs Personnalisés

API Gateway peut autoriser les endpoints de plusieurs manières. Une approche courante consiste à utiliser un [Autorisateur Personnalisé](https://aws.amazon.com/blogs/compute/introducing-custom-authorizers-in-amazon-api-gateway/).

Pour simuler les Autorisateurs Personnalisés, nous avons créé une fonction middleware express js. Le middleware crée l'événement Lambda avec les informations d'autorisation de la requête. La fonction Autorisateur est ensuite invoquée localement.

Les Autorisateurs Personnalisés permettent ou refusent les requêtes en fonction d'un [document de politique](http://docs.aws.amazon.com/apigateway/latest/developerguide/use-custom-authorizer.html). Le middleware lit le document de politique retourné par l'Autorisateur. Si la requête n'est pas autorisée à accéder à un endpoint, le middleware retournera une réponse Non Autorisée.

#### Intégration Lambda

API Gateway a deux intégrations avec AWS Lambda. L'intégration [Lambda](http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html) originale et la plus récente [Lambda Proxy](https://aws.amazon.com/blogs/aws/api-gateway-update-new-features-simplify-api-development/).

Les deux intégrations mappent les requêtes HTTP à un événement Lambda. Lorsque Lambda retourne un résultat, l'intégration mappe le résultat à une réponse HTTP.

Nous avons développé deux fonctions de mappage qui imitent Lambda et Lambda Proxy. Le serveur sélectionne l'intégration en fonction de la configuration de l'événement HTTP dans `[serverless.yml](https://serverless.com/framework/docs/providers/aws/guide/serverless.yml/)`.

Lorsqu'une requête est reçue, le serveur effectue le même processus de mappage qu'API Gateway. Une version simplifiée du code est ci-dessous.

```
function(req, res) {  integration.event(req)    .then(event => lambda.invoke(context, event))    .then(result => integration.response(req, result))    .then(response => respond(res, response))}
```

Le résultat final est un serveur express qui se comporte comme API Gateway.

![Image](https://cdn-media-1.freecodecamp.org/images/OUcsIE-kabY1gzGSmgCTIr66IsK-ZKleJYGW)

#### Utilisation du Simulateur API Gateway

Pour utiliser le simulateur API Gateway, vous devez installer le plugin dans votre projet Serverless. Veuillez [lire la documentation](https://github.com/gertjvr/serverless-docker) pour les instructions.

Pour démarrer le simulateur API Gateway, exécutez la commande suivante :

`sls simulate apigateway -p 5000`

Cela démarrera un serveur HTTP que vous pourrez utiliser pour tester vos endpoints et fonctions localement.

![Image](https://cdn-media-1.freecodecamp.org/images/O99KxRZ6Bm9RvWZcZwAExefJJ9W69lK2fwrH)
_Exécution du simulateur sur notre projet d'exemple_

La simulation API Gateway est similaire à d'autres plugins hors ligne pour le Serverless Framework. La réelle différence avec [Serverless Simulate](https://github.com/gertjvr/serverless-plugin-simulate) est la manière dont nous simulons Lambda localement.

### Simulation d'AWS Lambda

AWS Lambda est alimenté par une API HTTP. Les fonctions sont invoquées via une requête HTTP à l'API Lambda.

Lorsque l'API Invoke est appelée, le service Lambda exécute votre code à l'intérieur d'un conteneur. Pour plus de détails, voir [la documentation](http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html).

![Image](https://cdn-media-1.freecodecamp.org/images/AZSo7MXWrfo6hRB8i36IvFErb9qAIbaxsWR2)

Bien qu'AWS Lambda soit un service complexe, les éléments principaux sont raisonnablement faciles à simuler. Pour le simuler localement, nous avons implémenté trois services : des runtimes de fonction, un registre de fonctions et une API HTTP.

#### Runtimes de Fonction

Nous utilisons une [image Docker](https://hub.docker.com/r/lambci/lambda/~/dockerfile/) créée par [Michael Hart](https://www.freecodecamp.org/news/how-you-can-speed-up-serverless-development-by-simulating-aws-lambda-locally-41c61a60fbae/undefined) pour créer le runtime de fonction. L'utilisation de Docker nous permet de contrôler l'environnement et de faire respecter les limites de mémoire et les timeouts.

#### Registre de Fonctions

Le Registre de Fonctions est une base de données JSON locale alimentée par [lowdb](https://github.com/typicode/lowdb). Le registre stocke des informations sur la configuration et l'emplacement de la fonction.

Cela permet au serveur de rechercher les détails d'une fonction lorsqu'une requête est reçue par l'API.

#### API HTTP

L'API HTTP fournit un endpoint d'enregistrement pour les clients. L'endpoint d'enregistrement est utilisé par le plugin pour enregistrer les fonctions.

L'API HTTP fournit également un endpoint pour invoquer les fonctions. L'endpoint d'invocation imite l'API AWS Lambda. Cela permet aux clients d'utiliser un SDK AWS pour invoquer des fonctions.

![Image](https://cdn-media-1.freecodecamp.org/images/d0cLqWRGZjL5-lqJw6PN5VA2prssO6VQxXFk)

#### Pourquoi utiliser le Simulateur Lambda

Le simulateur Lambda vous permet d'invoquer des fonctions Lambda localement à partir d'autres services. Cela peut inclure une autre fonction Lambda dans un service Serverless différent. Ou cela pourrait inclure une application complètement différente.

Cela est utile si vous enchaînez des fonctions Lambda ou migrez une application existante vers AWS Lambda.

Par exemple, cette fonction invoque une autre fonction Lambda localement. Sans le Simulateur Lambda, la deuxième fonction serait invoquée dans AWS.

```
// Si hors ligne, utilisez le registre local
const endpoint = process.env.SERVERLESS_SIMULATE ?  process.env.SERVERLESS_SIMULATE_LAMBDA_ENDPOINT :  undefined
```

```
// configurez le SDK AWS pour utiliser l'endpoint local
const lambda = new AWS.Lambda({ endpoint })
```

```
const handler = (event, context, callback) => {  const params = {    FunctionName: 'my-other-function',    Payload: JSON.stringify({ foo: 'bar' })  }
```

```
lambda.invoke(params, (err, result) => {    if (err) {      return callback(err)    }        callback(null, {      statusCode: 200,      body: result.Payload    })    })
```

#### Utilisation du Simulateur Lambda

Pour utiliser le simulateur Lambda, vous devez installer le plugin dans votre projet Serverless. Veuillez [lire la documentation](https://github.com/gertjvr/serverless-docker) pour les instructions.

Pour démarrer le simulateur Lambda, exécutez la commande suivante :

`sls simulate lambda -p 4000`

![Image](https://cdn-media-1.freecodecamp.org/images/8z3TiTZj94ndFEyzVLfcMMWopXHoIRipHlAw)
_Démarrage du Simulateur Lambda_

Pour utiliser le Simulateur Lambda avec API Gateway, exécutez la commande API Gateway avec l'argument `--lambda-port`.

`sls simulate apigateway -p 5000 --lambda-port`

Lors de l'utilisation de l'argument `--lambda-port`, le simulateur API Gateway invoque les fonctions via l'API HTTP.

![Image](https://cdn-media-1.freecodecamp.org/images/YgkjCWii73PxwGeTSHZyHeUISYgTgUZyn2xx)
_10 fonctions enregistrées avec le Simulateur Lambda_

Cela vous permet de simuler des architectures complexes localement avant de les déployer dans le cloud.

### Comparaison avec d'autres Plugins

[Serverless Offline](https://github.com/dherault/serverless-offline) est le plugin le plus populaire pour le Serverless Framework. Malheureusement, la conception de Serverless Offline limite la qualité de la simulation.

Ce plugin simule API Gateway et exécute les fonctions dans le processus du plugin. Les inconvénients de cette décision incluent :

* Pas de support Python
* Il utilise la version NodeJS que vous exécutez, qui peut ne pas être la même version NodeJS qu'AWS Lambda
* Il ne fait pas respecter les limites de mémoire ou les timeouts
* Il n'y a aucun moyen d'enchaîner les appels de fonctions Lambda

Nous avons conçu Serverless Simulate pour résoudre ces problèmes.

### Allez de l'avant et construisez

Ce plugin aidera à résoudre un gros problème pour moi et l'équipe de [A Cloud Guru](https://www.freecodecamp.org/news/how-you-can-speed-up-serverless-development-by-simulating-aws-lambda-locally-41c61a60fbae/undefined). Les tests unitaires et les exécutions locales réduisent le temps que nous passons à attendre les déploiements dans le cloud.

Le Serverless Framework et Serverless Simulate sont tous deux des projets Open Source. Si vous souhaitez vous impliquer, vous pouvez aider en créant des issues ou en soumettant une pull request.

J'espère que cela vous aidera à gagner du temps lorsque vous testez des fonctions Lambda localement.

Si vous avez des questions sur ce projet ou sur Serverless en général, vous pouvez me contacter sur Medium ou [Twitter](https://twitter.com/johncmckim). Je dirigerai un atelier à [ServerlessConf Austin](http://austin.serverlessconf.io/) si vous souhaitez me rencontrer en personne.