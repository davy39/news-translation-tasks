---
title: Comment utiliser gRPC-web avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-09T17:48:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-grpc-web-with-react-1c93feb691b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PJce89y7GZdBYsiHzmmUow.jpeg
tags:
- name: Envoy Proxy
  slug: envoy-proxy
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment utiliser gRPC-web avec React
seo_desc: 'By Mohak Puri

  For the past few months, my team has been working on a gRPC service. A few weeks
  back a new requirement came in: we needed a web portal to display some information.
  Since we already had a gRPC backend, the server side was sorted. But fo...'
---

Par Mohak Puri

Au cours des derniers mois, mon équipe a travaillé sur un service gRPC. Il y a quelques semaines, une nouvelle exigence est apparue : nous avions besoin d'un portail web pour afficher certaines informations. Comme nous avions déjà un backend gRPC, le côté serveur était réglé. Mais pour le front-end, nous avions quelques choix importants à faire.

```
1. Vue ou React (Nous avons choisi React)2. REST ou gRPC depuis le portail web
```

Si vous ne savez pas ce qu'est gRPC, vous pouvez en lire plus [ici](https://grpc.io/). Voici quelques raisons qui nous ont fait choisir gRPC plutôt que REST.

1. Un facteur majeur pour choisir gRPC était le fait que nous avions déjà des protos que nous utilisions dans notre service backend. Nous pouvions utiliser les mêmes protos pour générer du code côté client en JavaScript.
2. Utiliser gRPC signifierait que nous n'aurions pas à écrire de code pour créer le client. L'ajout de nouveaux endpoints signifierait apporter des modifications au proto et générer du code côté client.
3. Nous avions besoin de streaming côté serveur, qui est supporté par gRPC-web.
4. Nous avions déjà une configuration d'Envoy pour l'équilibrage de charge de notre service backend (plus d'informations à ce sujet plus tard).

### Points à considérer

1. Le client web gRPC n'enverra pas de requêtes HTTP2. Au lieu de cela, vous avez besoin d'un proxy entre votre client web et le service backend gRPC pour convertir cette requête HTTP1 en HTTP2. Le client web gRPC a un support intégré pour Envoy comme proxy. Vous pouvez trouver plus d'informations à ce sujet [ici](https://grpc.io/blog/state-of-grpc-web#f2).
2. Les équipes de Google et Improbable ont toutes deux mis en œuvre la spécification dans deux dépôts différents. Nous utiliserons le client web gRPC fourni par Google. Vous pouvez trouver l'implémentation de Google [ici](https://github.com/grpc/grpc-web) et celle d'Improbable [ici](https://github.com/improbable-eng/grpc-web).
3. À l'heure actuelle, le streaming côté client n'est pas supporté.

![Image](https://cdn-media-1.freecodecamp.org/images/OQ0IsJZIV2TFKQc7ErPHvNc735UGRcIHcWmK)
_Crédits : [https://grpc.io/blog/state-of-grpc-web](https://grpc.io/blog/state-of-grpc-web" rel="noopener" target="_blank" title=")_

Maintenant que nous avons une idée de gRPC web, voici un diagramme illustrant comment la communication complète aura lieu. Nous allons créer une application web React qui enverra une requête _Ping_ et recevra une réponse _Pong_.

![Image](https://cdn-media-1.freecodecamp.org/images/wZ-PKPpwVBps6i71c37sQ8G2pZRjtlguKsPx)
_Front-end + Proxy + Back-end_

#### Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

```
1. npm (Node package manager) - Pour générer un projet React2. Docker - Pour exécuter Envoy localement3. protoc - Pour générer du code à partir des protos
```

Il y a trois éléments à ce puzzle. Nous allons les aborder un par un.

### 1. Interface utilisateur — Site web utilisant React

Pour créer un projet React, nous utiliserons la commande _create-react-app_.

```
create-react-app learn-react-grpc
```

Maintenant que nous avons un projet d'exemple en place, créons un proto. Voici à quoi ressemble un proto ping pong.

Pour que les commandes suivantes s'exécutent, assurez-vous que le proto est à l'intérieur du dossier src/ du projet React. Pour générer du code côté client en JavaScript, exécutez la commande suivante :

```
protoc -I=. src/ping_pong.proto --js_out=import_style=commonjs:. --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.
```

Cela générera deux nouveaux fichiers : **_ping_pong_pb.js_** et **_ping_pong_grpc_web_pb.js_**, avec tout le code généré. Nous utiliserons ce code pour faire des requêtes à notre service gRPC.

Tout d'abord, mettons à jour notre package.json avec quelques dépendances liées à gRPC et protobuf, puis exécutons **_npm install_**.

Voici toute la logique pour construire notre site web. Vous pouvez utiliser ce code dans votre fichier App.js. Il s'agit d'un site web très simple qui contient un bouton, en cliquant dessus, une requête ping pong est créée et une réponse est obtenue.

Maintenant, si vous exécutez le serveur node avec **npm start**, vous risquez de rencontrer ce problème de compilation. Il s'agit apparemment d'un problème lors de l'utilisation de gRPC-web avec un projet créé à l'aide de l'interface de ligne de commande _create-react-app_.

![Image](https://cdn-media-1.freecodecamp.org/images/5ZczeglnF24jEX58qfPUxInNybjRcJTZQww6)
_problèmes de compilation lors de l'utilisation de create-react-app_

Cependant, ce problème peut être résolu en ajoutant _eslint-disable_ à tous les fichiers générés par proto. Assurez-vous de le faire pour _tous_ les fichiers. Maintenant, si vous démarrez le serveur, tout devrait fonctionner.

![Image](https://cdn-media-1.freecodecamp.org/images/hAk-fyDb6JZ6bq5Vyqsxxoiyxkp5CB5gxueY)
_correction des problèmes de compilation_

### 2. Backend — Serveur gRPC en Node

Créons un simple serveur node. Nous utiliserons le même proto que celui utilisé dans notre application React. Créons une application node js node-ping-pong-server. Voici notre fichier server.js d'exemple.

Nous pouvons exécuter le serveur node avec la commande suivante :

```
node server.js
```

### 3. Proxy — Envoy

Comme mentionné ci-dessus, nous utiliserons Docker pour configurer Envoy. Voici le fichier Docker. Au moment de l'écriture, la dernière version pointe vers Envoy _version 1.11._ Créez un Dockerfile à l'intérieur du dossier src/ de votre application React.

Avant d'exécuter le conteneur Docker, nous devons nous assurer que nous avons un fichier de configuration pour Envoy. Ajoutez ce fichier envoy.yml à l'intérieur du dossier src/ de votre application React.

Comprenons ce que fait ce fichier de configuration Envoy :

9901 est le port où le portail d'administration d'Envoy est en cours d'exécution. Vous pouvez utiliser ce portail pour vérifier les routes Envoy, les vérifications de santé et bien plus encore.

9090 est le port où Envoy écoute les requêtes entrantes. Notre site web fera une requête à Envoy sur ce port.

Toute requête correspondant à ce préfixe est routée vers le cluster ping_pong_service. Comme notre serveur node (alias cluster) est en cours d'exécution sur la machine hôte (votre ordinateur portable) et non sur le conteneur Docker, nous devons router ces requêtes hors du conteneur vers l'hôte. **_host.docker.internal_** fait exactement cela.

Maintenant, construisons notre image Docker avec la commande suivante :

```
docker build -t mohak1712/learn-grpc-web .
```

Maintenant, exécutons l'image Docker :

```
docker run -d -p 9090:9090 mohak1712/learn-grpc-web
```

Nous devons transférer le port hôte 9090 vers le port conteneur 9090 afin que toute requête sur le port 9090 soit transférée au conteneur Docker où Envoy est en cours d'exécution.

### Résultat final

Maintenant que tout est configuré, assurez-vous que le site web, le serveur node et le conteneur Envoy sont en cours d'exécution. Vous pouvez exécuter l'ensemble de commandes suivant si ce n'est pas encore fait.

```
npm start -> démarrer le serveur web
```

```
node server.js -> démarrer le serveur node
```

```
docker run -d -p 9090:9090 mohak1712/learn-grpc-web -> démarrer Envoy
```

![Image](https://cdn-media-1.freecodecamp.org/images/ybrDqzwv38XiKDlSZfVpdcjX2pTn2kkYaaOK)

![Image](https://cdn-media-1.freecodecamp.org/images/nfvEXxasFhtEuT9fqkKkXLBGE6DB8Eq4-xSq)

Maintenant, lorsque vous cliquez sur le bouton, il envoie une requête Ping et reçoit une réponse Pong !

C'est à peu près tout ! Merci d'avoir lu, et j'espère que vous avez apprécié l'article.

Vous pouvez me suivre sur [Medium](https://medium.com/@mohak1712) et [Github](https://github.com/mohak1712) :)