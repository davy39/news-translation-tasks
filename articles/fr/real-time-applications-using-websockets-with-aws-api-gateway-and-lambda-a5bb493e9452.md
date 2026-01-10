---
title: Comment créer des applications en temps réel en utilisant WebSockets avec AWS
  API Gateway et Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T08:47:49.000Z'
originalURL: https://freecodecamp.org/news/real-time-applications-using-websockets-with-aws-api-gateway-and-lambda-a5bb493e9452
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OaDVOjdkCturioO_.png
tags:
- name: Apps
  slug: apps-tag
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: websocket
  slug: websocket
seo_title: Comment créer des applications en temps réel en utilisant WebSockets avec
  AWS API Gateway et Lambda
seo_desc: 'By Janitha Tennakoon

  Recently AWS has announced the launch of a widely-requested feature: WebSockets
  for Amazon API Gateway. With WebSockets, we are able to create a two-way communication
  line which can be used in many scenarios like real-time applic...'
---

Par Janitha Tennakoon

Récemment, AWS a annoncé le lancement d'une fonctionnalité largement demandée : WebSockets pour Amazon API Gateway. Avec WebSockets, nous sommes en mesure de créer une ligne de communication bidirectionnelle qui peut être utilisée dans de nombreux scénarios comme les applications en temps réel. Cela soulève la question : quelles sont les applications en temps réel ? Alors répondons d'abord à cette question.

La plupart des applications actuellement opérationnelles utilisent l'architecture client-serveur. Dans l'architecture client-serveur, le client envoie les requêtes via Internet en utilisant la communication réseau, puis le serveur traite cette requête et envoie la réponse au client.

Ici, vous pouvez voir que c'est le client qui initie la communication avec le serveur. Donc, d'abord, le client initie la communication et le serveur répond à la requête envoyée par le serveur. Mais que se passe-t-il si le serveur veut initier la communication et envoyer des réponses sans que le client les demande d'abord ? C'est là que les applications en temps réel entrent en jeu.

Les applications en temps réel sont des applications où le serveur obtient la capacité de pousser des données vers les clients sans que le client demande d'abord les données. Supposons que nous avons une application de chat où deux clients de chat peuvent communiquer via un serveur. Dans cette situation, il est inefficace que tous les clients de chat demandent des données au serveur toutes les secondes. Ce qui est plus efficace, c'est que le serveur envoie des données aux applications de chat client lorsqu'un message est reçu. Cette fonctionnalité peut être réalisée grâce aux applications en temps réel.

Amazon a annoncé qu'ils allaient supporter WebSockets dans API Gateway lors de l'AWS re:Invent 2018. Plus tard, en décembre, ils l'ont lancé dans API Gateway. Ainsi, maintenant, en utilisant l'infrastructure AWS, nous sommes en mesure de créer des applications en temps réel en utilisant API Gateway.

Dans cet article, nous allons créer une simple application de chat en utilisant WebSockets API Gateway. Avant de commencer à implémenter notre application de chat, il y a quelques concepts que nous devons comprendre concernant les applications en temps réel et API Gateway.

### Concepts de l'API WebSocket

Une API WebSocket est composée d'une ou plusieurs routes. Une _expression de sélection de route_ est là pour déterminer quelle route une requête entrante particulière doit utiliser, qui sera fournie dans la requête entrante. L'expression est évaluée contre une requête entrante pour produire une valeur qui correspond à l'une des valeurs _routeKey_ de vos routes. Par exemple, si nos messages JSON contiennent une propriété appelée action, et que vous souhaitez effectuer différentes actions en fonction de cette propriété, votre expression de sélection de route pourrait être `${request.body.action}`.

Par exemple : si votre message JSON ressemble à {"action" : "onMessage" , "message" : "Bonjour à tous"}, alors la route onMessage sera choisie pour cette requête.

Par défaut, il y a trois routes qui sont déjà définies dans l'API WebSocket. En plus des routes mentionnées ci-dessous, nous pouvons ajouter des routes personnalisées pour nos besoins.

* **$default** — Utilisé lorsque l'expression de sélection de route produit une valeur qui ne correspond à aucune des autres clés de route dans vos routes d'API. Cela peut être utilisé, par exemple, pour implémenter un mécanisme de gestion des erreurs générique.
* **$connect** — La route associée est utilisée lorsqu'un client se connecte pour la première fois à votre API WebSocket.
* **$disconnect** — La route associée est utilisée lorsqu'un client se déconnecte de votre API.

Une fois qu'un appareil est connecté avec succès via l'API WebSocket, l'appareil se verra attribuer un identifiant de connexion unique. Cet identifiant de connexion sera conservé tout au long de la durée de vie de la connexion. Pour envoyer des messages à l'appareil, nous devons utiliser la requête POST suivante en utilisant l'identifiant de connexion.

```
POST https://{api-id}.execute-api.us-east-1.amazonaws.com/{stage}/@connections/{connection_id}
```

### Implémentation de l'application de chat

Après avoir appris les concepts de base de l'API WebSocket, voyons comment nous pouvons créer une application en temps réel en utilisant l'API WebSocket. Dans cet article, nous allons implémenter une simple application de chat en utilisant l'API WebSocket, AWS Lambda et DynamoDB. Le diagramme suivant montre l'architecture de notre application en temps réel.

![Image](https://cdn-media-1.freecodecamp.org/images/EiHc2HzJkq621fqsah0gFRGo6J0298tfu5KF)

Dans notre application, les appareils seront connectés à l'API Gateway. Lorsqu'un appareil se connecte, une fonction lambda enregistrera l'identifiant de connexion dans une table DynamoDB. Dans une instance où nous voulons envoyer un message à l'appareil, une autre fonction lambda récupérera l'identifiant de connexion et enverra les données à l'appareil en utilisant une URL de rappel.

#### Création de l'API WebSocket

Pour créer l'API WebSocket, nous devons d'abord aller au service Amazon API Gateway en utilisant la console. Là, choisissez de créer une nouvelle API. Cliquez sur WebSocket pour créer une API WebSocket, donnez un nom d'API et notre expression de sélection de route. Dans notre cas, ajoutez $request.body.action comme notre expression de sélection et cliquez sur Créer l'API.

![Image](https://cdn-media-1.freecodecamp.org/images/Fu3WT1nNu67o1AEQbVvyqPjF4Xfgdy5DIdU8)

Après avoir créé l'API, nous serons redirigés vers la page des routes. Ici, nous pouvons voir les trois routes déjà prédéfinies : $connect, $disconnect et $default. Nous allons également créer une route personnalisée $onMessage. Dans notre architecture, les routes $connect et $disconnect réalisent les tâches suivantes :

* $connect — lorsque cette route est appelée, une fonction Lambda ajoutera l'identifiant de connexion de l'appareil connecté à DynamoDB.
* $disconnect — lorsque cette route est appelée, une fonction Lambda supprimera l'identifiant de connexion de l'appareil déconnecté de DynamoDB.
* onMessage — lorsque cette route est appelée, le corps du message sera envoyé à tous les appareils connectés à ce moment-là.

Avant d'ajouter la route selon ce qui précède, nous devons effectuer quatre tâches :

* Créer une table DynamoDB
* Créer une fonction lambda de connexion
* Créer une fonction lambda de déconnexion
* Créer une fonction lambda onMessage

Tout d'abord, créons la table DynamoDB. Allez au service DynamoDB et créez une nouvelle table appelée Chat. Ajoutez la clé primaire comme 'connectionid'.

![Image](https://cdn-media-1.freecodecamp.org/images/tC0qYzoiulwhYS3pdneXVn1uzu927lCTm2Mz)

Ensuite, créons la fonction Lambda de connexion. Pour créer la fonction Lambda, allez dans les services Lambda et cliquez sur créer une fonction. Sélectionnez Auteur à partir de zéro et donnez le nom 'ChatRoomConnectFunction' et un rôle avec les permissions nécessaires. (Le rôle doit avoir la permission de récupérer, mettre et supprimer des éléments de DynamoDB, effectuer des appels d'API dans l'API gateway.)

Dans le code de la fonction lambda, ajoutez le code suivant. Ce code ajoutera l'identifiant de connexion de l'appareil connecté à la table DynamoDB que nous avons créée.

```
exports.handler = (event, context, callback) => {    const connectionId = event.requestContext.connectionId;    addConnectionId(connectionId).then(() => {    callback(null, {        statusCode: 200,        })    });}
```

```
function addConnectionId(connectionId) {    return ddb.put({        TableName: 'Chat',        Item: {            connectionid : connectionId        },    }).promise();}
```

Ensuite, créons également la fonction lambda de déconnexion. En utilisant les mêmes étapes, créez une nouvelle fonction lambda nommée 'ChatRoomDisconnectFunction'. Ajoutez le code suivant à la fonction. Ce code supprimera l'identifiant de connexion de la table DynamoDB lorsqu'un appareil se déconnecte.

```
const AWS = require('aws-sdk');const ddb = new AWS.DynamoDB.DocumentClient();
```

```
exports.handler = (event, context, callback) => {    const connectionId = event.requestContext.connectionId;    deleteConnectionId(connectionId).then(() => {    callback(null, {        statusCode: 200,        })    });}
```

```
function deleteConnectionId(connectionId) {    return ddb.delete({        TableName: 'Chat',        Key: {            connectionid : connectionId,        },    }).promise();}
```

Maintenant que nous avons créé la table DynamoDB et deux fonctions lambda, avant de créer la troisième fonction lambda, retournons à API Gateway et configurons les routes en utilisant nos fonctions lambda créées. Tout d'abord, cliquez sur la route $connect. Comme type d'intégration, sélectionnez la fonction Lambda et sélectionnez ChatRoomConnectionFunction.

![Image](https://cdn-media-1.freecodecamp.org/images/Jm4gDZE2iTvkM7jjEIbD5dJwxMpfQqNJcxaw)

Nous pouvons faire de même pour la route $disconnect où la fonction lambda sera ChatRoomDisconnectionFunction :

![Image](https://cdn-media-1.freecodecamp.org/images/xydcct1RcCF4MMgATbCUE7RoOlVw5Zx-rBzy)

Maintenant que nous avons configuré nos routes $connect et $disconnect, nous pouvons tester si notre API WebSocket fonctionne. Pour cela, nous devons d'abord déployer l'API. Dans le bouton Actions, cliquez sur Déployer l'API pour déployer. Donnez un nom de stage tel que Test puisque nous déployons l'API uniquement pour les tests.

![Image](https://cdn-media-1.freecodecamp.org/images/Bflmr7zIfPBtVbdcQw-FhWrdWLomxD5wSMIu)

Après le déploiement, nous obtiendrons deux URL. La première URL est appelée URL WebSocket et la seconde est appelée URL de Connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/81K7bxiFXv-JMJx8b5jScxBmnjkKM4brxY9Q)

L'URL WebSocket est l'URL utilisée pour se connecter via WebSockets à notre API par les appareils. Et la deuxième URL, qui est l'URL de Connexion, est l'URL que nous utiliserons pour rappeler les appareils qui sont connectés. Puisque nous n'avons pas encore configuré le rappel vers les appareils, testons d'abord uniquement les routes $connect et $disconnect.

Pour appeler via WebSockets, nous pouvons utiliser l'outil wscat. Pour l'installer, il suffit d'exécuter la commande `npm install -g wscat` dans la ligne de commande. Après l'installation, nous pouvons utiliser l'outil avec la commande wscat. Pour se connecter à notre API WebSocket, exécutez la commande suivante. Assurez-vous de remplacer l'URL WebSocket par l'URL correcte fournie.

```
wscat -c wss://bh5a9s7j1e.execute-api.us-east-1.amazonaws.com/Test
```

![Image](https://cdn-media-1.freecodecamp.org/images/8uYGb6iG04XmfBsGOWxhLsxAenVIafGSWRE3)

Lorsque la connexion est réussie, un message de connexion s'affichera sur le terminal. Pour vérifier si notre fonction lambda fonctionne, nous pouvons aller dans DynamoDB et chercher dans la table l'identifiant de connexion du terminal connecté.

![Image](https://cdn-media-1.freecodecamp.org/images/uMqXnECECOiDAkC4NcS4OYjWgpvLOsUBNA8z)

Comme ci-dessus, nous pouvons également tester la déconnexion en appuyant sur CTRL + C, ce qui simulera une déconnexion.

Maintenant que nous avons testé nos deux routes, examinons la route personnalisée onMessage. Ce que cette route personnalisée fera, c'est qu'elle recevra un message de l'appareil et enverra le message à tous les appareils connectés à l'API WebSocket. Pour y parvenir, nous allons avoir besoin d'une autre fonction lambda qui interrogera notre table DynamoDB, obtiendra tous les identifiants de connexion et enverra le message à ces appareils.

Créons d'abord la fonction lambda de la même manière que nous avons créé les deux autres fonctions lambda. Nommez la fonction lambda ChatRoomOnMessageFunction et copiez le code suivant dans le code de la fonction.

```
const AWS = require('aws-sdk');const ddb = new AWS.DynamoDB.DocumentClient();require('./patch.js');
```

```
let send = undefined;function init(event) {  console.log(event)    const apigwManagementApi = new AWS.ApiGatewayManagementApi({    apiVersion: '2018-11-29',    endpoint: event.requestContext.domainName + '/' + event.requestContext.stage  });        send = async (connectionId, data) => {  await apigwManagementApi.postToConnection({ ConnectionId: connectionId, Data: `Echo: ${data}` }).promise();  }}
```

```
exports.handler =  (event, context, callback) => {  init(event);  let message = JSON.parse(event.body).message    getConnections().then((data) => {        console.log(data.Items);        data.Items.forEach(function(connection) {           console.log("Connection " +connection.connectionid)           send(connection.connectionid, message);        });    });        return {}};
```

```
function getConnections(){    return ddb.scan({        TableName: 'Chat',    }).promise();}
```

Le code ci-dessus analysera DynamoDB pour obtenir tous les enregistrements disponibles dans la table. Pour chaque enregistrement, il enverra un message en utilisant l'URL de Connexion fournie dans l'API. Dans le code, nous nous attendons à ce que les appareils envoient le message dans l'attribut nommé 'message' que la fonction lambda analysera et enverra aux autres.

Puisque l'API WebSockets est encore nouvelle, il y a certaines choses que nous devons faire manuellement. Créez un nouveau fichier nommé patch.js et ajoutez le code suivant à l'intérieur.

```
require('aws-sdk/lib/node_loader');var AWS = require('aws-sdk/lib/core');var Service = AWS.Service;var apiLoader = AWS.apiLoader;
```

```
apiLoader.services['apigatewaymanagementapi'] = {};AWS.ApiGatewayManagementApi = Service.defineService('apigatewaymanagementapi', ['2018-11-29']);Object.defineProperty(apiLoader.services['apigatewaymanagementapi'], '2018-11-29', {  get: function get() {    var model = {      "metadata": {        "apiVersion": "2018-11-29",        "endpointPrefix": "execute-api",        "signingName": "execute-api",        "serviceFullName": "AmazonApiGatewayManagementApi",        "serviceId": "ApiGatewayManagementApi",        "protocol": "rest-json",        "jsonVersion": "1.1",        "uid": "apigatewaymanagementapi-2018-11-29",        "signatureVersion": "v4"      },      "operations": {        "PostToConnection": {          "http": {            "requestUri": "/@connections/{connectionId}",            "responseCode": 200          },          "input": {            "type": "structure",            "members": {              "Data": {                "type": "blob"              },              "ConnectionId": {                "location": "uri",                "locationName": "connectionId"              }            },            "required": [              "ConnectionId",              "Data"            ],            "payload": "Data"          }        }      },      "shapes": {}    }    model.paginators = {      "pagination": {}    }    return model;  },  enumerable: true,  configurable: true});
```

```
module.exports = AWS.ApiGatewayManagementApi;
```

J'ai pris le code ci-dessus de cet [article](https://hackernoon.com/websockets-api-gateway-9d4aca493d39). La fonctionnalité de ce code est de créer automatiquement l'URL de rappel pour notre API et d'envoyer la requête POST.

![Image](https://cdn-media-1.freecodecamp.org/images/Uq12ZG3KNn38ut5jQQLRjOPebZBuLIxxqesW)

Maintenant que nous avons créé la fonction lambda, nous pouvons créer notre route personnalisée dans API Gateway. Dans la nouvelle clé de route, ajoutez 'OnMessage' comme route et ajoutez la route personnalisée. Comme les configurations ont été faites pour les autres routes, ajoutez notre fonction lambda à cette route personnalisée et déployez l'API.

Maintenant que nous avons terminé notre API WebSocket, nous pouvons tester complètement l'application. Pour tester l'envoi de messages pour plusieurs appareils, nous pouvons ouvrir et nous connecter en utilisant plusieurs terminaux.

Après la connexion, envoyez le JSON suivant pour envoyer des messages :

```
{"action" : "onMessage" , "message" : "Bonjour à tous"}
```

Ici, l'action est la route personnalisée que nous avons définie et le message est la donnée qui doit être envoyée aux autres appareils.

![Image](https://cdn-media-1.freecodecamp.org/images/hHo2bGE-lEcSiKIF9CNUpHwXJrKj05h2F5mV)

C'est tout pour notre simple application de chat en utilisant l'API WebSocket d'AWS. Nous n'avons pas réellement configuré la route $default qui est appelée à chaque occasion où aucune route n'est trouvée. Je vous laisse l'implémentation de cette route. Merci et à bientôt dans un autre article. :)