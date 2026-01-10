---
title: Comment apprendre Serverless AWS en construisant 7 projets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-26T15:34:58.000Z'
originalURL: https://freecodecamp.org/news/learn-serverless-aws-by-building-7-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-christina-morillo-1181316.jpg
tags:
- name: AWS
  slug: aws
- name: lambda
  slug: lambda
- name: projects
  slug: projects
- name: serverless
  slug: serverless
seo_title: Comment apprendre Serverless AWS en construisant 7 projets
seo_desc: "By Sam Williams\nFollowing tutorials when you start learning serverless\
  \ is a good first step. But to really get better, you need to build your own projects.\
  \ \nThe problem is that coming up with ideas that are realistic but help you grow\
  \ is hard.\nTo hel..."
---

Par Sam Williams

Suivre des tutoriels lorsque vous commencez à apprendre le serverless est une bonne première étape. Mais pour vraiment progresser, vous devez construire vos propres projets. 

Le problème est qu'il est difficile de trouver des idées réalistes qui vous aident à grandir.

Pour vous aider, j'ai imaginé 7 idées de projets géniales pour vous aider progressivement à devenir un meilleur développeur serverless.

Si vous débutez avec Serverless, commencez par les premiers projets. Si vous avez déjà construit des APIs et utilisé Dynamo avec Serverless, choisissez les projets qui couvrent les sujets que vous souhaitez le plus apprendre.

J'ai également fait une vidéo si vous préférez regarder et suivre :

%[https://youtu.be/ROiAUWX8p5E]

# Projet d'API de Combinaison

Ce projet est conçu pour vous familiariser avec le déploiement d'une API avec Lambda. Vous pratiquerez également l'appel d'autres APIs et la fusion de ces données.

Il existe de nombreuses logiques que vous pourriez utiliser pour cela, mais voici deux exemples :

* Obtenir les offres de jeux Steam, converties dans votre devise locale
* Obtenir des nouvelles traduites dans votre langue locale

![Image](https://completecoding.io/wp-content/uploads/2022/08/ch2.drawio.png)

L'architecture de ce projet est simple, ce qui est exactement ce que vous voulez pour votre premier projet. L'idée est que l'API que vous créez prendra certains paramètres, donc elle ressemblera à ceci :

```
https://apiurl.amazonaws.com/dev/steamdeals?currency=EUR
https://apiurl.amazonaws.com/dev/news/fr
```

Toute la logique sera écrite dans le Lambda. Je ne vais pas écrire le code complet, mais voici un pseudo-code :

```
const handler = (event: APIGatewayProxyEvent) => {
    // obtenir la valeur du paramètre de chemin ou de chaîne de requête

    // appeler la première API pour obtenir les premières données

    // obtenir les données à traduire / convertir

    // passer les données de l'API1 à l'API2

    // combiner les données 

    // retourner les données au format API Gateway
}	
```

Si vous avez besoin d'APIs gratuites et publiques à utiliser, voici un document complet pour en choisir : [https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis).

Ensuite, construisez ce projet en utilisant le Serverless Framework ou AWS CDK. Ces outils vous rendront beaucoup plus précieux en tant que développeur.

Pour commencer avec le Serverless Framework, [regardez cette vidéo](https://youtu.be/HhgXwKFUzT8).

# Projet de Raccourcisseur d'URL

Ce projet vous permettra de déployer votre première table DynamoDB, puis d'écrire et de lire des données depuis celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/ch3-url-shortener.drawio.png)

Il y aura deux points de terminaison API. L'un pour ajouter une nouvelle URL au raccourcisseur, l'autre pour obtenir une URL raccourcie et récupérer l'originale.

Voici le pseudo-code pour les deux points de terminaison :

```
// Ajouter une nouvelle URL
const handler = (event: APIGatewayProxyEvent) => {
    // obtenir leur URL originale (corps de l'événement)
    
    // générer un code aléatoire de 5 caractères
    
    // écrire dans Dynamo - {id: code, url: originalUrl }
    
    // retourner l'URL (https://{apiurl}.amazonaws.com/dev/get/{code})
}
```

Pour obtenir l'`apiURL`, nous pouvons la passer en tant que variable d'environnement. Si vous utilisez le Serverless Framework, vous pouvez le faire en ajoutant ceci à la section environnement de votre configuration :

```
apiUrl: {
  "Fn::Join": [
    "",
    [
      "https://",
      { Ref: "HttpApi" },
      ".execute-api.${self:provider.region}.amazonaws.com",
    ],
  ],
},
```

```
// Obtenir une URL par code
const handler = (event: APIGatewayProxyEvent) => {
    // obtenir le code depuis le chemin de l'URL
    
    // obtenir depuis Dynamo par ID
    
    // retourner l'URL originale
}
```

Vous pouvez aller plus loin en changeant le code de statut de la fonction `getUrl` pour retourner une redirection 301 - permanente. Vous devrez ajouter quelques en-têtes supplémentaires, mais cela redirigera automatiquement l'utilisateur vers la page souhaitée.

# Projet d'Application de Rappel

Ce projet vous apprendra à utiliser les Index Secondaires dans Dynamo ainsi que le Time-To-Live de Dynamo. Vous pourrez également essayer l'automatisation des emails avec Amazon Simple Email Service (SES) ou l'envoi de SMS avec Simple Notification Service (SNS). 

Vous pourriez également construire une simple application front-end et apprendre à l'héberger dans S3 et à utiliser CloudFront pour la distribuer.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/ch4-reminder-app.drawio.png)

L'idée de cette application est que vous pouvez poster un nouveau rappel au premier point de terminaison API. Cela écrira un nouvel enregistrement dans DynamoDB, mais vous aurez ajouté un index secondaire global (GSI) à la table. Cela signifie que vous pouvez obtenir un rappel par ID, ou vous pouvez interroger en fonction de l'utilisateur. 

Il aura également un Time-To-Live (TTL) qui vous permettra de déclencher un Lambda au moment du rappel. Le code pour définir les rappels ressemblera beaucoup au projet précédent.

La table ressemblera à ceci :

| id    | userId          | TTL        | notificationType | message |
| ----- | ----------- | --- | -- | -- |
| 123   | test@gmail.com |1648277828 | email | Publier la prochaine vidéo YouTube |
| 897   | 447113350882  |1648842828 | sms | Acheter plus de LAIT |

Le Time-To-Live (TTL) indique à Dynamo que lorsque le temps atteint cette date, supprimez l'enregistrement de Dynamo. 

Deux choses à noter avec TTL :

* Assurez-vous que ceci est le timestamp Unix pour la date de suppression - mais en secondes. `new Date('october 20 2022').getTime()` sera en millisecondes, donc divisez simplement par 1000.
* L'enregistrement sera supprimé dans une fenêtre de 15 minutes après votre TTL, donc ne paniquez pas si cela fait 5 minutes et que l'enregistrement n'a pas encore été supprimé.

Vous pouvez ensuite configurer un second Lambda qui est déclenché chaque fois qu'un enregistrement est supprimé de Dynamo. Cela envoie ensuite le message soit à leur email soit à leur téléphone.

```
// Envoyer un rappel
const handler = async (event: DynamoDBStreamEvent) => {
    // obtenir la liste des enregistrements supprimés
    
    // mapper chaque enregistrement
       // Appeler SES ou SNS pour envoyer le rappel
}
```

Le second point de terminaison API sera pour obtenir tous les rappels pour un utilisateur. Assurez-vous d'avoir configuré un GSI avec une clé de partition de `userId` et une clé de tri de `TTL`.

```
// Obtenir mes rappels
const handler = (event: APIGatewayProxyEvent) => {
    // obtenir le userId depuis la requête
    
    // params = KeyConditionExpression: "'userId' = userId",
    
    // Interroger Dynamo
    
    // formater les rappels 
    
    // retourner à l'utilisateur
}
```

Pour le front-end, vous pouvez écrire une simple application web avec deux sections : créer un nouveau rappel et lister mes rappels. Cela peut être en React, Vue, Angular, ou même en HTML, CSS et JavaScript bruts.

Une fois que vous avez l'application, vous pouvez utiliser `serverless-s3-sync` pour pousser automatiquement le code dans S3 (que vous créez dans Serverless).

# Projet d'Application de Chat en Direct

Ce projet vous apprendra à construire des WebSockets. Un utilisateur peut soit créer une nouvelle "salle" soit rejoindre une salle existante. Tout message envoyé est envoyé à tous ceux connectés à la salle.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/ch5-live-chat.drawio.png)

Les WebSockets fonctionnent légèrement différemment des APIs régulières. Au lieu d'avoir plusieurs points de terminaison, vous avez un seul point de terminaison et différents types de messages. 

Il y a quelques types de messages par défaut et quelques-uns personnalisés :

* connectToRoom – Personnalisé
* createRoom – Personnalisé
* onMessage – Personnalisé
* disconnect – Par défaut

Lorsque l'utilisateur se connecte au WebSocket, il peut envoyer un message `connectToRoom` ou `createRoom`. Les deux créeront un enregistrement dans Dynamo avec l'`connectionId` du WebSocket de l'utilisateur et le `roomId`. Comme nous l'avons fait auparavant, nous aurons un GSI dans Dynamo pour pouvoir interroger plus tard et obtenir tous les utilisateurs pour un `roomId`.

Le code pour `connectToRoom` et `createRoom` ressemblera beaucoup aux lambdas précédents "écrire des données dans Dynamo". 

Vous pouvez vérifier dans `connectToRoom` que la salle existe déjà. Vous pouvez le faire en interrogeant tous les utilisateurs par roomId. S'il n'y a pas d'utilisateurs dans la salle, cela signifie qu'ils essaient de se connecter à une salle qui n'existe plus.

Maintenant qu'un utilisateur est dans une salle, il peut envoyer un message. Voici le pseudo-code pour ce Lambda :

```
// onMessage
const handler = (event: WebsocketMessageEvent) => {
    // obtenir l'connectionId de l'utilisateur
    
    // obtenir l'utilisateur par connectionId depuis Dynamo pour obtenir le roomId
    
    // interroger tous les utilisateurs dans ce roomId
    
    // envoyer le message à tous les utilisateurs
    
    // retourner
}
```

Enfin, il y a le onDisconnect qui sera un simple Lambda qui supprime simplement l'enregistrement de l'utilisateur de Dynamo.

# Projet d'Application de Vote d'Idées

Ce projet vous apprendra à concevoir et construire des tables Dynamo plus avancées et à travailler avec Cognito pour l'authentification. Vous devriez également construire un simple front-end pour apprendre à intégrer Cognito dans les applications web.

L'outil vous permet de demander des idées à votre communauté et de découvrir lesquelles sont les plus populaires.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/ch6-idea-voting-app.drawio.png)

Cela commence par tous les utilisateurs devant s'inscrire à votre application. Nous utilisons Cognito pour cela et le faisons afin de nous assurer que chaque personne ne peut voter qu'une seule fois. 

Vous devrez ensuite créer quelques points de terminaison :

* créer un tableau
* ajouter une idée à un tableau
* voter pour une idée
* obtenir les détails du tableau

### Créer un tableau

Le premier point de terminaison API dont nous avons besoin est celui pour créer un nouveau tableau d'idées. N'importe qui peut créer un tableau et l'enregistrement dans Dynamo est vraiment simple. Juste un `boardId` et quelques informations sur le propriétaire du tableau, peut-être un titre et une description.

<table>
<thead>
<tr>
<th>boardId</th>
<th>owner</th>
<th>title</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>boardId</td>
<td>userId</td>
<td>Mon idée géniale</td>
<td>une description</td>
</tr>
</tbody>
</table>

### Ajouter des idées à un tableau

Ensuite, nous devons pouvoir ajouter des idées à un tableau. Ce sera un autre point de terminaison API et Lambda. Avec l'enregistrement de la base de données d'idées, nous devons être un peu plus intelligents car nous devons pouvoir référencer directement une idée, mais aussi obtenir toutes les idées pour un tableau.

Pour cela, nous avons un schéma comme celui-ci. `pk` est une clé de partition et `sk` est une clé de tri, qui sont toutes deux nécessaires pour interroger sur DynamoDB.

<table>
<thead>
<tr>
<th>id</th>
<th>pk</th>
<th>sk</th>
<th>idea</th>
<th>owner</th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>boardId</td>
<td>ideaId</td>
<td>l'idée</td>
<td>userId</td>
</tr>
</tbody>
</table>

Avec l'`id`, nous pouvons référencer directement l'idée, mais nous pouvons également interroger l'enregistrement. Nous pouvons obtenir toutes les idées pour le tableau `1234` en interrogeant pour `pk = 1234`.

### Ajouter un vote à l'idée

Maintenant que nous avons des idées sur le tableau, nous devons que nos utilisateurs votent pour elles. Ce sera un nouveau point de terminaison API et Lambda. Ce Lambda a un peu plus de travail à faire que les deux autres. Tout d'abord, nous allons regarder le schéma pour cet enregistrement.

<table>
<thead>
<tr>
<th>pk</th>
<th>sk</th>
<th>pk2</th>
<th>sk2</th>
</tr>
</thead>
<tbody>
<tr>
<td>ideaId</td>
<td>userId</td>
<td>userId</td>
<td>ideaId</td>
</tr>
</tbody>
</table>

Cela peut sembler étrange au premier abord, mais je vais expliquer pourquoi nous voulons structurer cela ainsi.

Pour une idée donnée, nous voulons savoir combien de votes elle a. Nous pouvons le découvrir en interrogeant sur `pk = ideaId` qui retournera tous les votes pour l'idée.

Lors de l'ajout d'un vote, nous voulons vérifier que l'utilisateur n'a pas déjà voté pour l'idée. Nous pouvons le faire en interrogeant `pk = ideaId && sk = userId`. Si nous trouvons un enregistrement qui correspond, nous savons qu'ils ont déjà voté pour cette idée. Sinon, nous pouvons ajouter l'enregistrement `vote` pour cet utilisateur et cette idée.

### Obtenir les détails du tableau

Nous pouvons maintenant écrire un lambda qui interrogera les données que nous avons :

```
export const handler = async (event: APIGatewayProxyEvent) => {
    // obtenir boardId depuis la requête
    // interroger toutes les idées sur le tableau
    // mapper chaque idée
        // interroger tous les votes sur cette idée
    // formater le tout dans un joli format
    // retourner à l'utilisateur
}
```

### Obtenir les votes pour un utilisateur

Enfin, nous voulons pouvoir afficher tous les votes pour un utilisateur donné. Nous ne pouvons pas interroger où `sk = userId` car vous avez toujours besoin d'une clé de partition lors de l'interrogation de DynamoDB. Par conséquent, nous avons créé une deuxième clé de partition (`pk2`) qui contient le userId. Maintenant, nous pouvons interroger `pk2 = userId` pour obtenir toutes les idées pour lesquelles un utilisateur a voté.

Ce modèle consistant à avoir un deuxième GSI où les PK et SK sont inversées est très courant. Il permet d'avoir une relation plusieurs-à-plusieurs. Vous pouvez interroger tous les B qui sont connectés à un A spécifique et tous les A qui sont connectés à un B spécifique. Cela s'appelle souvent une table de jonction.

## Projet d'Application de Messagerie

Ce projet vous apprendra à utiliser les clés composites de Dynamo et vous donnera plus de pratique avec les websockets et Cognito.

Cette application permet aux utilisateurs de s'inscrire, de demander à rejoindre une salle, puis de voir tous les messages qui ont été envoyés dans cette salle. Le propriétaire d'une salle décide s'il laisse quelqu'un rejoindre la salle.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/ch7-messaging-app-api.drawio.png)

L'architecture commencera par ressembler beaucoup à l'application de chat en direct - avec une connexion WebSocket avec des Lambdas pour `onConnect, onDisconnect, createGroup, joinGroup, listMyGroups handleJoinGroupRequest` et `sendMessage`.

Avant de passer au code Lambda, nous voulons ajouter Cognito à l'application pour que les utilisateurs puissent s'inscrire. Cela sera utilisé plus tard lorsqu'un utilisateur demandera l'accès à un groupe.

Le Lambda `createGroup` sera presque identique à la solution de chat en direct. Il crée simplement un enregistrement de `groupe`.

### Connexion / Déconnexion WebSocket

Maintenant, lorsqu'un utilisateur se connecte et se connecte au WebSocket, nous pouvons créer un Lambda onConnection. Cela obtiendra le userId et vérifiera leur jeton d'utilisateur Cognito. Ce jeton nous donnera facilement le userId et le userName. 

S'ils ne passent pas de jeton ou si le jeton est invalide (ou a expiré), nous pouvons tuer le websocket, les empêchant de faire quoi que ce soit d'autre sans un jeton valide.

Si le jeton est valide, nous pouvons stocker un simple enregistrement de connexion. Cela nous permettra d'envoyer des messages en retour via le websocket plus tard.

N'oubliez pas de supprimer cet enregistrement lorsque l'utilisateur se déconnecte du WebSocket. Nous pouvons utiliser l'action par défaut `$disconnect` pour déclencher un lambda `onDisconnect`.

### Créer un groupe

La première chose que quelqu'un doit pouvoir faire est de créer un groupe auquel il peut ensuite inviter ses amis.

Cela impliquera de créer deux enregistrements dans Dynamo. Le premier est simplement un enregistrement du groupe. Cela inclura l'ID du groupe, le nom du groupe et qui est le propriétaire du groupe.

Le second sera un enregistrement d'appartenance au groupe. Cela indiquera que cet utilisateur fait partie de ce groupe.

<table>
<thead>
<tr>
<th>pk</th>
<th>sk</th>
<th>pk2</th>
<th>sk2</th>
<th>userName</th>
<th>groupName</th>
</tr>
</thead>
<tbody>
<tr>
<td>groupId</td>
<td>user#{userId}</td>
<td>userId</td>
<td>groupId</td>
<td>nom d'utilisateur</td>
<td>nom de groupe</td>
</tr>
</tbody>
</table>

Cette première partie nous permettra d'interroger sur `pk = groupId et sk commence par ('user')` pour obtenir tous les utilisateurs du groupe. Cela sera utilisé dans le Lambda `sendMessage` pour obtenir tous les utilisateurs à qui envoyer le message WebSocket.

Les secondes parties (PK2, SK2) sont ajoutées pour nous permettre d'obtenir tous les groupes auxquels un utilisateur est autorisé en interrogeant où `PK2 = userId`. Cela est utilisé lorsque nous devons obtenir une liste de tous les groupes de l'utilisateur.

### Rejoindre un groupe

La demande de `joinGroup` créera maintenant un enregistrement dans Dynamo pour une `demande d'accès`. Cela ne donnera pas à l'utilisateur l'accès au groupe, mais permettra au propriétaire du groupe de passer en revue les demandes d'accès.

Ces enregistrements seront la première fois que nous utiliserons des clés composites. Cela consiste à porter la clé de tri au niveau supérieur et l'enregistrement ressemblera à ceci :

<table>
<thead>
<tr>
<th>pk</th>
<th>sk</th>
</tr>
</thead>
<tbody>
<tr>
<td>groupId</td>
<td>joinRequest#{userId}</td>
</tr>
</tbody>
</table>

Cela nous permet d'interroger où `pk = groupId et sk commence par ('joinRequest')`. Cela retournera toutes les demandes d'accès pour ce groupe. Lorsque quelqu'un fait cette demande, nous pouvons d'abord vérifier qu'il est le propriétaire du groupe.

Le propriétaire du groupe a alors deux options - accepter ou rejeter. Si le propriétaire rejette l'utilisateur, nous pouvons simplement supprimer l'enregistrement de la demande d'accès. S'il accepte l'utilisateur, nous devons ajouter un `utilisateur autorisé`. Cela nécessitera un nouvel enregistrement dans Dynamo.

### Envoyer un message

Maintenant, nous arrivons au cœur de l'application de messagerie - l'envoi et le stockage des messages.

Dans le Lambda WebSocket `sendMessage`, nous pouvons interroger tous les utilisateurs du groupe et envoyer le message à toutes les connexions actuelles. Nous devons également stocker le message dans Dynamo.

<table>
<thead>
<tr>
<th>pk</th>
<th>sk</th>
<th>message</th>
<th>user</th>
</tr>
</thead>
<tbody>
<tr>
<td>groupId</td>
<td>message#{timestamp}</td>
<td>mon message</td>
<td>userId</td>
</tr>
</tbody>
</table>

### Obtenir les messages précédents

Lorsque l'utilisateur se connecte, il doit pouvoir obtenir les messages qu'il a manqués pendant qu'il était hors ligne. Avec les données de message structurées de cette manière, nous pouvons interroger où :

`pk = groupId et sk > 'message#{ timestamp pour hier }'`

Cela retournera tous les messages créés depuis hier.

Nous pourrions également leur permettre d'obtenir des messages plus anciens en passant le dernier message qu'ils ont. Cela nous permettra d'obtenir le prochain lot de messages. Cela nous permettra de créer un défilement infini vers le haut sur l'historique des messages.

## Système de Commerce Électronique Basé sur les Événements

Ce projet vous apprendra à utiliser Event Bridge, ainsi que de vous donner un peu plus de pratique avec la conception de tables DynamoDB et des services comme SES et SNS pour les emails et les SMS.

Ce système aura des produits et des filtres, des paniers et des commandes comme vous pourriez vous y attendre. La clé ici est que le passage de commande, les changements de statut de commande et les mises à jour de livraison seront tous gérés via Event Bridge.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/ch8-event-ecomerce.drawio.png)

### Stocker les Produits

Pour commencer, nous devons stocker les produits. Nous pouvons structurer nos clés de tri de manière à permettre un niveau de hiérarchie pour nos produits.

<table>
<thead>
<tr>
<th>id</th>
<th>pk</th>
<th>sk</th>
<th>title</th>
<th>description</th>
<th>...</th>
</tr>
</thead>
<tbody>
<tr>
<td>productId</td>
<td>clothing</td>
<td>mens#tops#{productId}</td>
<td>Next Slimfit T-Shirt</td>
<td>...</td>
<td>...</td>
</tr>
<tr>
<td>productId</td>
<td>clothing</td>
<td>womens#trousers#{productId}</td>
<td>Levi's Jeans</td>
<td>...</td>
<td>...</td>
</tr>
</tbody>
</table>

Cela nous permet d'interroger pour `pk = clothing et sk commence par mens` pour obtenir tous les vêtements pour hommes ou pour `pk = clothing et sk commence par womens#trousers` pour obtenir tous les pantalons pour femmes.

### Passer une Commande

La partie suivante consiste à pouvoir passer une commande. Nous n'allons pas essayer de prendre le paiement, simplement ajouter un enregistrement de commande à la table dynamoDB.

### Event Bridge

La grande différence ici est que nous allons commencer à utiliser Event Bridge. C'est un outil qui nous permet d'avoir des événements qui peuvent déclencher plusieurs lambdas. C'est génial car nous pouvons ajouter un nouvel écouteur sans avoir à changer le code initial.

### Commande Créée

Nous allons avoir deux lambdas qui écoutent l'événement `orderCreated`. Le premier va prendre les données de commande et les envoyer à une API d'entrepôt pour qu'elles soient préparées. Le second va envoyer à l'utilisateur un email de confirmation de commande.

### Commande Préparée

Nous allons prétendre qu'il y a un vrai entrepôt et qu'après avoir obtenu la liste de préparation de commande, ils ont préparé et rendu la commande prête pour l'expédition. Ils ont un système qui appelle notre API et change le statut de la commande en `packed`.

Ce changement dans l'enregistrement Dynamo déclenchera un autre événement Event Bridge pour `orderPacked`. Celui-ci a également deux écouteurs : l'un pour envoyer un email de mise à jour à l'utilisateur, et un autre pour envoyer un email à un service de livraison pour récupérer le colis de l'entrepôt et le livrer au client.

### Commande Expédiée

De même, nous allons prétendre qu'une société de livraison a pris le colis et l'a livré. Ils appellent un autre point de terminaison API `Order Shipped` et cela change à nouveau le statut de la commande dans la base de données.

Cela déclenche un autre événement pour `orderDelivered` et celui-ci a deux écouteurs :

Un pour envoyer un message de "merci" au client.

Et un autre qui fera quelque chose d'un peu différent. Il prendra la commande, supprimera toutes les données personnelles, et la stockera dans une autre table DynamoDB. 

Cela devient de plus en plus courant comme étape de préparation pour un scientifique des données. Nous supprimons les données personnelles pour réduire les problèmes juridiques, mais permettons toujours à un scientifique des données de faire des choses comme entraîner un modèle pour vous donner des recommandations du type "Les gens ont aussi acheté ....".

## Qu'est-ce qui suit

Si vous aimez ces idées de projets mais ne savez pas par où commencer, alors j'ai un cours vidéo complet qui vous apprendra à construire tous ces projets.

[Découvrez le cours ici](https://completecoding.mykajabi.com/7-serverless-projects).

Vous pouvez également télécharger un [PDF Gratuit](https://completecoding.mykajabi.com/7-practical-project-pdf) de ces projets afin de visualiser votre progression dans votre parcours d'apprentissage.