---
title: Comment construire un microservice NodeJS sans serveur sur AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-18T17:12:29.000Z'
originalURL: https://freecodecamp.org/news/building-a-nodejs-microservice-on-aws-lambda-6adb6da53cbb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*foHs8AleRqNMimdXsK9hAA.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment construire un microservice NodeJS sans serveur sur AWS Lambda
seo_desc: "By Paul Matthew Jaworski\nDEPRECATED\nUnfortunately, since I wrote this\
  \ article, v1.0 of the Serverless Framework has been released, along with some breaking\
  \ changes. I believe that you can migrate to the new version simply by adding:\n\
  \ integration: lam..."
---

Par Paul Matthew Jaworski

### **OBSOLÈTE**

Malheureusement, depuis que j'ai écrit cet article, la version 1.0 du [Serverless Framework](https://serverless.com/) a été publiée, avec quelques changements majeurs. Je crois que vous pouvez migrer vers la nouvelle version simplement en ajoutant :

```
 integration: lambda
```

à chacune de vos ressources. Par exemple :

```
createPet:    handler: handler.create    events:      - http:          path: pets          method: POST          cors: true          integration: lambda
```

Cependant, j'ai décidé de passer à autre chose pour l'instant, principalement en raison de problèmes d'authentification, d'autorisation et de frustrations avec DynamoDB, donc je ne mettrai pas à jour cet article. J'explorerai ces problèmes et ma décision de revenir à une API REST "traditionnelle" dans une prochaine histoire.

Pour l'instant, je vous recommande de consulter [la documentation officielle de Serverless sur API Gateway](https://serverless.com/framework/docs/providers/aws/events/apigateway/#api-gateway) pour commencer, et éventuellement d'utiliser le reste de cet article comme référence, en gardant à l'esprit que toute information dans la documentation de Serverless prime sur tout ce qui est écrit ici.

### Procédez avec prudence à partir d'ici :

Dans cet article, je vais partager mon expérience en passant au "serverless" et en construisant une API CRUD "microservice" en utilisant AWS Lambda, API Gateway et DynamoDB. Cela servira de guide pour que vous puissiez créer vos propres microservices avec ces outils.

### **Prise en main**

Je vais supposer que vous avez un compte AWS et que NodeJS est installé. Si ce n'est pas le cas, faites-le maintenant.

Ensuite, vous devrez installer le package npm Serverless, qui fournit un moyen de créer, modifier et déployer facilement des microservices en tant que fonctions AWS Lambda :

```
npm install -g serverless
```

Puis suivez les [instructions d'Amazon sur la création d'un utilisateur IAM et la configuration de Serverless](https://github.com/serverless/serverless/blob/master/docs/02-providers/aws/01-setup.md) pour utiliser ces identifiants.

Naviguez jusqu'au répertoire où vous souhaitez stocker votre nouveau projet et exécutez :

```
serverless create --template aws-nodejs --path pets-service
```

C'est le bon moment pour configurer le linting dans votre projet. Comme ce n'est pas une introduction à ESLint, je n'entrerai pas dans les détails, mais je vous recommande de l'installer maintenant et de configurer votre **.eslintrc** comme ceci :

```
{  "plugins": ["node"],  "extends": ["eslint:recommended", "plugin:node/recommended"],  "env": {    "node": true,    "mocha": true  },  "rules": {    "no-console": 0,    "node/no-unsupported-features": [2, {"version": 4}]  }}
```

La chose importante à noter ici est la règle "no-unsupported-features" du plugin node. AWS Lambda utilise Node v4.3, et savoir quelles fonctionnalités ES6 sont disponibles peut être un vrai casse-tête. Cela rend les choses plus faciles.

### **Création du Handler**

Installez aws-sdk et lodash avec npm :

```
npm i -S aws-sdk lodash
```

Maintenant, rendez-vous dans **handler.js** et ajoutez ces dépendances en haut de votre fichier :

```
const aws = require('aws-sdk');const _ = require('lodash/fp');
```

Notez que nous utilisons la variante "programmation fonctionnelle" de lodash car sa fonction merge ne mutera pas l'objet original.

En dessous, configurez votre client de document pour communiquer avec DynamoDB :

```
const dynamo = new aws.DynamoDB.DocumentClient();
```

Maintenant, créons notre fonction **create()** pour créer un nouvel animal de compagnie dans la base de données :

```
exports.create = function(event, context) {  const payload = {    TableName: 'Pets',    Item: event.body  };
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail('Error creating pet');    } else {      console.log(data);      context.succeed(data);    }  }
```

```
  dynamo.put(payload, cb);};
```

Il est assez facile de voir ce qui se passe ici pour la plupart :

Nous recevons un objet **event** avec une clé **body** qui contient les données que nous voulons stocker. Le DocumentClient nécessite au minimum un objet avec les clés **TableName** et **Item** pour être passé dans put().

Nous fournissons également un callback qui fait deux choses importantes :

Si une erreur survient, nous exécutons **context.fail()**, qui est essentiellement un callback onError fourni par AWS.

Si la création de l'élément est réussie, nous exécutons **context.succeed()**, en passant les données à retourner comme résultat de notre fonction Lambda.

Un point important avec DynamoDB est que nous devons fournir la clé primaire nous-mêmes lors de la création. Dans ce cas, nous devons inclure **petId** comme clé dans notre objet event.body.

Pourquoi une fonctionnalité aussi basique manque-t-elle à DynamoDB ? Votre supposition est aussi bonne que la mienne.

J'ai la chance dans mon application d'avoir un identifiant unique généré pour moi par Auth0, que j'utilise pour ma gestion d'authentification/utilisateurs. Vous devrez résoudre ce problème d'une autre manière si ce n'est pas le cas.

Nous allons suivre ce même modèle de base pour le reste de nos opérations CRUD :

```
exports.show = function(event, context) {  const payload = {    TableName: 'Pets',    Key: {      petId: event.params.path.petId    }  }
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail('Error retrieving pet');    } else {      console.log(data);      context.done(null, data);    }  }
```

```
  dynamo.get(payload, cb);};
```

```
exports.list = function(event, context) { const payload = {  TableName: 'Pets' }
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail('Error getting pets');    } else {      console.log(data);      context.done(null, data);    }  }
```

```
  dynamo.scan(payload, cb);}
```

```
exports.update = function(event, context) {  const payload = {    TableName: 'Pets',    Key: {      petId: event.params.path.petId    }  };
```

```
  dynamo.get(payload, (err, data) => {    if (err) {      console.log(err);      context.fail('No pet with that id exists.');    } else {      const item = _.merge(data.Item, event.body);      payload.Item = item;
```

```
      dynamo.put(payload, (putErr, putData) => {        if (putErr) {          console.log('Error updating pet.');          console.log(putErr);          context.fail('Error updating pet.');        } else {          console.log('Success!');          console.log(putData);          context.done(null, item);        }      });    }  });}
```

```
exports.delete = function(event, context) {  const payload = {    TableName: 'Pets',    Key: {      petId: event.params.path.petId    }  };
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail('Error retrieving pet');    } else {      console.log(data);      context.done(null, data);    }  }
```

```
  dynamo.delete(payload, cb);}
```

Il y a juste quelques points à noter ici :

Nous voulons pouvoir faire des mises à jour partielles, ce qui signifie que vous n'avez pas besoin d'envoyer l'objet Pet entier avec ses modifications, vous pouvez simplement envoyer les modifications. Pour y parvenir, nous appelons d'abord un **get** dans la fonction **update()**, puis nous fusionnons nos modifications dans le résultat de cette opération.

Notre **petId** est passé en tant que paramètre à API Gateway puis fourni à Lambda via event.params.path.petId. Vous pourriez également utiliser des chaînes de requête si vous préférez.

### **Configuration de Serverless**

Nous avons presque terminé ici, alors configurons maintenant nos fichiers de configuration Serverless. Ouvrez **serverless.yml** et modifiez-le pour qu'il ressemble à ceci :

```
service: pets-service
```

```
provider:  name: aws  runtime: nodejs4.3
```

```
defaults:  stage: dev  region: us-west-2
```

```
functions:  createPet:    handler: handler.create    events:      - http:          path: pets          method: POST  showPet:    handler: handler.show    events:      - http:          path: pets/{petId}          method: GET  listPets:    handler: handler.list    events:      - http:          path: pets          method: GET  updatePet:    handler: handler.update    events:      - http:          path: pets/{petId}          method: PUT  deletePet:    handler: handler.delete    events:      - http:          path: pets/{petId}          method: DELETE
```

Cela est assez facile à comprendre, je pense. Nous spécifions simplement les noms de nos fonctions Lambda, puis nous les mappons à nos fonctions **handler.js** et aux méthodes HTTP et chemins auxquels nous voulons qu'elles répondent.

J'ai changé les valeurs par défaut pour utiliser 'us-west-2' comme région, et j'ai gardé 'dev' comme étape. La configuration de différentes étapes avec Serverless n'est pas quelque chose que j'ai entièrement exploré.

La documentation est _très_ limitée pour l'instant, mais cette configuration entraînera la création d'une API Gateway nommée "dev-pets-service", même si ce n'est pas vraiment ce que nous voulons.

Les API Gateways ne devraient pas avoir l'environnement référencé dans leur nom, car elles peuvent contenir plusieurs environnements ou "stages".

Espérons que je trouverai une solution à ce problème et que je la publierai dans une future édition ;)

### **Déploiement et test de notre service**

Maintenant, nous sommes prêts à déployer ! Il suffit d'exécuter :

```
serverless deploy
```

En une minute ou deux, vos fonctions Lambda devraient être déployées et votre API Gateway créée.

Créez une table DynamoDB nommée 'Pets' (ou ce que vous appelez votre ressource). Ensuite, rendez-vous dans API Gateway. Trouvez votre 'dev-pets-service' et naviguez jusqu'à la méthode POST.

Testez votre API en cliquant sur le bouton "TEST" avec l'éclair et en utilisant les données suivantes :

```
{ petId: "029340", name: "Fido", type: "dog" }
```

Vous devriez avoir créé avec succès un nouvel élément dans votre base de données !

### **Quelles sont les prochaines étapes ?**

Vos prochaines étapes pourraient être l'activation de CORS pour vos ressources, l'utilisation d'un nom de domaine personnalisé pour votre API et la configuration de votre application front-end pour qu'elle communique avec ces points de terminaison.

Cela dépasse le cadre de cet article et devrait être assez simple, mais faites-moi savoir dans les commentaires si vous avez des questions.

**ÉDIT**

L'utilisateur jcready sur Reddit a suggéré une amélioration à notre méthode de mise à jour :

```
exports.update = function(event, context) {  const payload = _.reduce(event.body, (memo, value, key) => {    memo.ExpressionAttributeNames[`#${key}`] = key    memo.ExpressionAttributeValues[`:${key}`] = value    memo.UpdateExpression.push(`#${key} = :${key}`)    return memo  }, {    TableName: 'Pets',    Key: { petId: event.params.path.petId },    UpdateExpression: [],    ExpressionAttributeNames: {},    ExpressionAttributeValues: {}  })  payload.UpdateExpression = 'SET ' + payload.UpdateExpression.join(', ')  dynamo.update(payload, context.done)}
```

Le problème avec notre implémentation actuelle est qu'un utilisateur pourrait écraser les modifications d'un autre si deux requêtes de mise à jour sont envoyées en même temps.

DocumentClient nous fournit une méthode **update** qui nous permet de spécifier les champs que nous voulons mettre à jour, mais la syntaxe est un peu étrange et nécessite la génération d'une "UpdateExpression" pour réaliser ces changements.

Ce code construit cette expression en fonction des clés passées et résout le problème de l'écrasement des mises à jour dans une application où les ressources sont partagées entre les utilisateurs.