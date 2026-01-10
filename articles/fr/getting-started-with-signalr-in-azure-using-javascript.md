---
title: Comment commencer avec SignalR sur Azure avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-16T14:54:40.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-signalr-in-azure-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/travel14.jpg
tags:
- name: Azure
  slug: azure
- name: Cloud Computing
  slug: cloud-computing
- name: JavaScript
  slug: javascript
- name: SignalR
  slug: signalr
- name: websocket
  slug: websocket
seo_title: Comment commencer avec SignalR sur Azure avec JavaScript
seo_desc: "By Amber Wilkie\nThe other day, some fine developers at my company were\
  \ getting ready to roll out a status update page. We'd tested it extensively but\
  \ now we were about to put it out at scale. \nI was worried about its dependency\
  \ on an API server that ..."
---

Par Amber Wilkie

L'autre jour, quelques développeurs talentueux de mon entreprise étaient sur le point de déployer une page de mise à jour de statut. Nous l'avions testée extensivement, mais nous allions maintenant la mettre à l'échelle.

J'étais inquiet quant à sa dépendance à un serveur API qui avait eu des problèmes récemment. Nous n'avons pas déterminé la cause racine de nos problèmes côté API, et cette application utilise le polling - c'est-à-dire qu'elle demande constamment à l'API de nouvelles données. Si cette API tombe en panne, elle emporte notre application avec elle et la charge accrue de notre application pourrait aggraver les problèmes que nous observons.

![Touristes en Irlande, peut-être en attente d'un message](https://wilkie-portfolio-images.s3.us-east-2.amazonaws.com/travel14.jpg)

Une façon de s'éloigner du polling est d'intégrer [SignalR](https://dotnet.microsoft.com/apps/aspnet/signalr), un outil de connexion persistante qui utilise les websockets et les technologies associées pour permettre aux serveurs de _pousser_ des mises à jour vers les clients.

La technologie est écrite en .NET, et la plupart de la documentation que vous trouverez sur le web utilise C#. Ce tutoriel couvrira une implémentation JavaScript de base.

# Que fait-il ?
[Open-sourcé](https://github.com/aspnet/AspNetCore/tree/master/src/SignalR), SignalR crée une connexion persistante entre un client et un serveur. Il utilise d'abord les websockets, puis le long polling et d'autres technologies lorsque les websockets ne sont pas disponibles.

Une fois que le client et le serveur ont établi une connexion, SignalR peut être utilisé pour "diffuser" des messages au client. Lorsque le client reçoit ces messages, il peut effectuer des fonctions comme la mise à jour d'un store.

L'exemple le plus courant donné pour les websockets est une application de chat - de nouvelles données doivent être montrées à l'utilisateur sans qu'elle ait besoin de rafraîchir la page. Mais si votre serveur reçoit des mises à jour sur des données changeantes que vous devez montrer à un client, ce pourrait être le service qu'il vous faut.

# SignalR sur la plateforme Azure
Peut-être parce qu'il a été développé par Microsoft, SignalR a une intégration très propre sur la plateforme cloud Azure. Comme pour les autres applications de fonction, vous créerez un déclencheur "in" et une liaison "out" pour diffuser des messages.

## Coûts
Parce que j'ai été la première à examiner cette technologie à grande échelle dans mon entreprise, j'ai dû creuser un peu sur les coûts de ce service. Azure facture environ 50 $/mois pour une "unité" de service SignalR - 1000 connexions simultanées et un million de messages par jour. Il existe également un service gratuit pour ceux qui expérimentent ou les petites entreprises.

C'était vraiment bien que j'aie creusé ces chiffres, comme vous le verrez un peu plus bas.

## Créer un hub SignalR
Commençons. Nous aurons besoin d'un hub SignalR, de deux applications de fonction et de code client à ajouter à notre application web.

Allez dans SignalR -> Ajouter et remplissez vos détails. Il faut quelques secondes pour que le worker construise votre service. Assurez-vous de donner au service un nom de ressource décent, car vous l'utiliserez avec le reste de vos applications. Prenez également les clés -> Chaîne de connexion pour une utilisation dans notre liaison.

![Configuration de SignalR sur Azure](https://wilkie-portfolio-images.s3.us-east-2.amazonaws.com/setting-up-signalr-service.png)

# Créer votre application de fonction pour envoyer des messages SignalR
Parce que nous travaillons avec Azure, nous allons créer des applications de fonction pour interfacer avec SignalR. J'ai écrit un article de blog [blog post](https://wilkie.tech/tech/azure-function-apps-101/) sur les applications de fonction Azure il y a quelque temps.

Ce tutoriel suppose que vous savez déjà comment travailler avec les applications de fonction. Naturellement, vous pouvez travailler avec ces bibliothèques sans la magie des liaisons, mais vous devrez faire votre propre traduction du code .NET !

## L'application de connexion
La première chose dont nous avons besoin est un moyen pour que les clients demandent la permission de se connecter à notre service SignalR. Le code de cette fonction ne pourrait pas être plus basique :
```javascript
module.exports = function (context, _req, connectionInfo) {
  context.res = { body: connectionInfo }
  context.done()
}
```
Toute la magie se passe dans les liaisons, où nous intégrons notre service SignalR. Le déclencheur est une requête HTTP que notre client peut appeler.
```javascript
{
  "bindings": [
      {
          "authLevel": "function",
          "type": "httpTrigger",
          "direction": "in",
          "name": "req",
          "methods": ["get"]
      },
      {
          "type": "signalRConnectionInfo",
          "name": "connectionInfo",
          "hubName": "votre-nom-de-service-signalr",
          "connectionStringSetting": "chaine-de-connexion",
          "direction": "in"
      }
  ]
}
```

## Le code client
Pour accéder à cette méthode, notre client appellera :
```javascript
import * as signalR from '@microsoft/signalr'

const { url: connectionUrl, accessToken } = await axios
  .get(url-vers-votre-application-de-connexion)
  .then(({ data }) => data)
  .catch(console.error)
```
Notre application de fonction retournera une `url` et un `accessToken`, que nous pourrons ensuite utiliser pour nous connecter à notre service SignalR. Notez que nous avons créé la liaison avec le `hubName` de notre service SignalR - cela signifie que vous pourriez avoir plusieurs connexions à différents hubs dans un seul client.

# Le service de diffusion
Maintenant, nous sommes prêts à commencer à envoyer des messages. Nous allons à nouveau commencer par l'application de fonction. Elle prend un déclencheur et envoie un message SignalR.

Un déclencheur pourrait être un autre utilisateur publiant un message, un événement provenant d'un hub d'événements, ou tout autre déclencheur pris en charge par Azure. J'ai besoin de déclencher des changements de base de données.
```javascript
{
  "bindings": [
      {
          "type": "cosmosDBTrigger",
          "name": "documents",
          "direction": "in",
          [...]
      },
      {
        "type": "signalR",
        "name": "signalRMessages",
        "hubName": "votre-nom-de-service-signalr",
        "connectionStringSetting": "chaine-de-connexion",
        "direction": "out"
      }
  ]
}
```
Et le code. Encore une fois, très simple.
```javascript
module.exports = async function (context, documents) {
  const messages = documents.map(update => {
    return {
      target: 'statusUpdates',
      arguments: [update]
    }
  })
  context.bindings.signalRMessages = messages
}
```
Les messages SignalR prennent un objet `target` et `arguments`. Une fois que vos déclencheurs commencent à se déclencher, c'est tout ce dont vous avez besoin pour commencer avec SignalR sur le serveur ! Microsoft a rendu tout cela très facile pour nous.

## Le code client
Côté client, les choses sont un peu plus complexes, mais pas ingérables. Voici le reste du code client :
```javascript
const connection = new signalR.HubConnectionBuilder()
  .withUrl(connectionUrl, { accessTokenFactory: () => accessToken })
  // .configureLogging(signalR.LogLevel.Trace)
  .withAutomaticReconnect()
  .build()

connection.on('statusUpdates', data => {
  // faire quelque chose avec les données que vous recevez de SignalR
})
connection.onclose(function() {
  console.log('signalr déconnecté')
})
connection.onreconnecting(err =>
  console.log('err reconnexion  ', err)
)

connection
  .start()
  .then(res => // Potentiel de faire quelque chose au chargement initial)
  .catch(console.error)
```
Nous utilisons l'`connectionUrl` et l'`accessToken` que nous avons reçus de la fonction de connexion plus tôt, puis nous construisons notre connexion en utilisant ces valeurs.

Ensuite, nous écoutons les messages avec la clé partagée (pour moi, c'est `statusUpdates`), et nous fournissons des gestionnaires pour les fonctions de fermeture et de reconnexion.

Enfin, nous démarrons la connexion. Ici, nous pouvons fournir une fonction de chargement initial. J'en avais besoin pour récupérer les données initiales afin de montrer le statut actuel. Si vous construisez une application de chat, vous pourriez avoir besoin de récupérer les messages initiaux ici.

Ceci est (presque, peut-être) tout ce dont vous avez besoin pour commencer avec JavaScript avec SignalR sur Azure !

# Portée par utilisateur
Mais peut-être que vous, comme moi, devez envoyer beaucoup de messages à beaucoup d'utilisateurs.

Lorsque j'ai mis cela en production pour la première fois, sur un sous-ensemble d'utilisateurs, j'envoyais chaque mise à jour à chaque connexion. Parce que le code client peut définir la portée des messages qu'il écoute, j'ai utilisé quelque chose comme `statusUpdates-${userId}` pour que le client ne voie que ses propres mises à jour.

Cela pourrait fonctionner très bien si vous avez un très faible volume, et le plus général est idéal si tout le monde dans votre système a besoin du même message. Mais le statut avec lequel je travaille est particulier à un individu.

![800 000 messages SignalR envoyés depuis la plateforme Azure](https://wilkie-portfolio-images.s3.us-east-2.amazonaws.com/800000signalrmessages.png)

Rappelez-vous comment Azure facture par "unité" et chaque unité a un million de messages ? J'ai atteint cette limite pendant quelques heures de test pendant une période peu occupée.

Azure compte chaque message que SignalR doit envoyer comme un message. C'est-à-dire, si cinq connexions sont connectées à votre hub et que vous envoyez dix messages, cela compte comme 50, et non 10. Cela a été une surprise pour moi, et cela a également nécessité quelques heures de recherche supplémentaires.

Nous pouvons définir la portée de notre code de fonction SignalR pour envoyer uniquement à certains utilisateurs. Tout d'abord, nous mettons à jour l'application de connexion pour accepter `userId` comme paramètre de requête :
```javascript
      {
          "type": "signalRConnectionInfo",
          "name": "connectionInfo",
          "userId": "{userId}",
          "hubName": "votre-nom-de-service-signalr",
          "connectionStringSetting": "chaine-de-connexion",
          "direction": "in"
      }
```
Ensuite, nous mettons à jour la fonction de diffusion pour envoyer uniquement à cet utilisateur :
```javascript
const messages = documents.map(update => {
  return {
    target: 'statusUpdates',
    userId: update.user.id,
    arguments: [update]
  }
})
```
Le service de diffusion ne saura pas qui est connecté, vous devrez donc le déclencher avec quelque chose qui a accès à un identifiant unique auquel le client aura également accès.

Le code client passe simplement l'userId comme paramètre de requête :
```javascript
const { url: connectionUrl, accessToken } = await axios
  .get(`${url-vers-votre-application-de-connexion}&userId=${userId}`)
  .then(({ data }) => data)
  .catch(console.error)
```
Je vous jure, le seul endroit sur tout l'internet où j'ai trouvé pour me laisser savoir comment demander une connexion en utilisant le `userId` était une réponse sur [cette question Stack Overflow](https://stackoverflow.com/questions/29509396/signalr-client-how-to-set-user-when-start-connection).

L'internet est incroyable, et les documents Azure JavaScript sont difficiles à trouver.

# Ressources
- [Documentation du client JavaScript SignalR de Microsoft](https://docs.microsoft.com/en-us/aspnet/core/signalr/javascript-client?view=aspnetcore-3.0)
- [Configuration des utilisateurs et des groupes lors de l'envoi de messages SignalR](https://docs.microsoft.com/en-us/aspnet/signalr/overview/guide-to-the-api/mapping-users-to-connections#IUserIdProvider) - 
Exemples en C# mais vous pouvez peut-être comprendre comment le client JavaScript va se comporter et faire quelques suppositions éclairées.
- [Liaisons de service SignalR pour les fonctions Azure](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/azure-functions/functions-bindings-signalr-service.md)
- [API Client](https://github.com/SignalR/SignalR/wiki/SignalR-JS-Client)
- [Travail avec les groupes dans SignalR](https://github.com/aspnet/AspNetDocs/blob/master/aspnet/signalr/overview/guide-to-the-api/working-with-groups.md)
- [Tutoriel : Authentification du service Azure SignalR avec les fonctions Azure](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-tutorial-authenticate-azure-functions)


_Cet article est initialement paru sur [wilkie.tech](https://wilkie.tech/tech/getting-started-with-signal-r-in-azure/)._