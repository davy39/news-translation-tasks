---
title: Comment implémenter des files d'attente de messages dans vos applications backend
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-08-14T09:56:07.629Z'
originalURL: https://freecodecamp.org/news/how-to-implement-message-queues-in-your-backend-applications
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723280791863/cdc4faaa-2f95-4219-8753-881dfcafbf45.jpeg
tags:
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: queue
  slug: queue
seo_title: Comment implémenter des files d'attente de messages dans vos applications
  backend
seo_desc: 'The goal of every web developer is to create a product that appeals to
  a wide range of users. However, this comes with its problems, chief among them being
  scalability issues to meet overwhelming user demands.

  If not addressed, this can result in a d...'
---

L'objectif de tout développeur web est de créer un produit qui plaît à un large éventail d'utilisateurs. Cependant, cela comporte ses propres problèmes, parmi lesquels les problèmes de scalabilité pour répondre à une demande utilisateur écrasante.

Si ces problèmes ne sont pas résolus, cela peut entraîner un désordre dans la communication entre les services, annulant les mesures mises en place pour garantir des transactions de base de données ordonnées. Mais heureusement, nous avons des courtiers de messages pour nous sauver.

Dans cet article, nous mettrons en lumière l'importance de la mise en file d'attente des messages en tant que meilleure pratique pour le développement backend, les cas d'utilisation pertinents et les outils populaires de mise en file d'attente des messages, et comment implémenter la mise en file d'attente des messages dans les applications backend.

Voici quelques prérequis pour pouvoir suivre cet article :

* Connaissance de Node.js
  
* Connaissance de l'architecture des microservices
  

## Qu'est-ce que la mise en file d'attente des messages ?

Dans les systèmes distribués, plusieurs requêtes et files d'attente sont envoyées simultanément. Le concept de file d'attente de messages permet le stockage des messages de manière ordonnée, permettant aux destinataires de ces messages et requêtes de les traiter en conséquence.

Il fonctionne de manière asynchrone, permettant le fonctionnement indépendant des différents composants d'un système distribué. Avoir ces éléments en place garantit que les messages envoyés au destinataire sont finalement traités, indépendamment d'un temps d'arrêt du système. Les messages sont stockés en toute sécurité jusqu'à ce qu'ils soient accusés de réception.

### Cas d'utilisation pertinents des courtiers de messages

Voici quelques cas d'utilisation réels des courtiers de messages.

* Ils sont activement utilisés dans les applications fintech modernes pour garantir une exécution et un traitement fluides et ordonnés des transactions financières effectuées sur l'application. Cela aide à prévenir la surcharge du serveur et les erreurs de transaction.
  
* La mise en file d'attente des messages est également utilisée dans nos applications de notification quotidiennes, garantissant la réception précoce des notifications envoyées depuis d'autres services. Cela permet au destinataire d'accéder à ces notifications indépendamment du moment où elles ont été envoyées ou du moment où le destinataire accède à l'application de notification.
  
* Elle est également utilisée dans les marchés financiers pour une exécution fluide et efficace des ordres financiers passés. D'autres utilisations de cette fonctionnalité sont observées dans le streaming média et l'industrie de la santé.
  

Dans le paragraphe suivant, nous discuterons davantage des outils qui offrent des fonctionnalités de mise en file d'attente des messages.

## Exemples de services populaires de files d'attente de messages

Une large gamme d'applications et de services offrent des fonctionnalités de mise en file d'attente des messages. Certains de ces services sont intégrés dans des fournisseurs d'infrastructure cloud commerciaux. Voici une liste de certains services de mise en file d'attente de messages couramment utilisés :

* RabbitMQ
  
* Apache Kafka
  
* Redis
  
* Amazon SQS
  
* Google Cloud Pub/sub
  
* NATS
  
* Pulsar
  
* IBM MQ
  

Nous utiliserons une application Rabbit MQ Cloud-as-a-service pour alimenter nos messages en raison de sa popularité et de sa facilité d'utilisation. Voici un lien vers la [documentation](https://www.cloudamqp.com/docs/index.html). Vous pouvez également consulter d'autres applications de mise en file d'attente de messages mentionnées ci-dessus.

Ensuite, nous développerons un projet de démonstration qui utilise les fonctionnalités de mise en file d'attente des messages.

## Projet de démonstration

Dans ce projet, nous utiliserons Rabbit MQ en tant que plateforme cloud de service pour construire un système simple de courtier de messages qui permet une communication fluide et ordonnée entre deux serveurs Node.js.

Dans ce tutoriel, nous créerons un éditeur de messages qui servira d'expéditeur, et un consommateur de messages qui reçoit les messages.

Pour commencer, nous devrons créer les deux serveurs Node.js qui communiqueront entre eux.

Vous pouvez créer deux fichiers différents et initialiser un projet Node en utilisant `npm init`.

Par la suite, vous pouvez installer les packages pertinents qui aideront à la mise en œuvre des fonctionnalités. Nous utiliserons la bibliothèque `amqplib`, une implémentation de bibliothèque Node pour Rabbit MQ.

Ce package nous permet de communiquer rapidement avec RabbitMQ via l'application Node.js. Il atteint cela de manière transparente grâce à ses fonctions intégrées pour créer des files d'attente, publier des messages et consommer des messages. Plus de détails concernant son utilisation seront discutés plus tard.

Pour installer cela dans notre projet, veuillez exécuter :

```javascript
npm i amqplib
```

La fonction de publication sera maintenant rédigée. Après cela, nous devrons initialiser `amqplib` dans notre projet.

```javascript
const amp = require("amqplib")

```

De plus, nous devons configurer notre courtier RabbitMQ qui gérera nos messages.

Il existe plusieurs façons de créer des serveurs RabbitMQ, la plus populaire étant de les installer sur un ordinateur personnel et de les configurer pour interagir avec les serveurs backend. Vous pouvez télécharger le logiciel [ici](https://www.rabbitmq.com/docs/download). Cependant, pour faciliter l'utilisation, nous utiliserons une application RabbitMQ basée sur le cloud en tant que service pour générer notre serveur.

Pour cela, veuillez naviguer vers [https://www.cloudamqp.com/](https://www.cloudamqp.com/) et créer un compte. Pour ce tutoriel, une instance a été créée et configurée dans la région la plus proche de moi. Une fois l'instance créée avec succès, les détails de Rabbit MQ seront mis à disposition.

![Page d'accueil de CloudAMQP](https://www.freecodecamp.org/news/content/images/2024/08/cloudAmpq.PNG align="left")

![Création d'une instance gratuite sur CloudAMQP](https://www.freecodecamp.org/news/content/images/2024/08/instance.PNG align="left")

![Détails de l'instance gratuite créée](https://www.freecodecamp.org/news/content/images/2024/08/amqpdets.PNG align="left")

Ensuite, nous allons créer une file d'attente de messages que les deux parties pourront utiliser comme pipeline de connexion. Nous commencerons par créer une fonction pour envoyer des messages.

```javascript
async function sendMessage(msg) {
  try {
    const connection = await amqp.connect(url);
    const channel = await connection.createChannel();
    
    await channel.assertQueue(queue);
    await channel.sendToQueue(queue, Buffer.from(msg));
```

Dans le code ci-dessus, une connexion a été établie et maintenue. Par la suite, un canal de communication a également été créé. La fonction assert queue est ensuite déclarée lorsqu'elle est exécutée, garantissant que la file d'attente existante est maintenue, et crée la file d'attente si elle n'existe pas.

Le message attaché à la fonction est mis en mémoire tampon puis envoyé à la file d'attente créée.

```javascript
async function receiveMessage() {
  try {
    const connection = await amqp.connect(url);
    const channel = await connection.createChannel();
    
    await channel.assertQueue(queue);
    await channel.consume(queue, (msg) => {
      console.log(`Message reçu : ${msg.content.toString()}`);
      channel.ack(msg);
    });
```

La fonction de réception est également exécutée pour recevoir tout message qui arrive dans la file d'attente en exécutant la méthode consume à la file d'attente exacte. Dans notre cas, le message est sorti sous forme de message de journal.

La fonction `ack` est maintenant exécutée pour accuser réception du message reçu de la file d'attente.

Voici le code complet du projet :

```javascript
const amqp = require("amqplib");
const url = "amqp://localhost"; // Remplacez par l'URL de votre serveur RabbitMQ
const queue = "queue";

async function receiveMessage() {
  try {
    const connection = await amqp.connect(url);
    const channel = await connection.createChannel();
    
    await channel.assertQueue(queue);
    await channel.consume(queue, (msg) => {
      if (msg !== null) {
        console.log(`Message reçu : ${msg.content.toString()}`);
        channel.ack(msg);
      }
    });
  } catch (err) {
    console.error("Échec de la réception du message :", err);
  }
}

receiveMessage();
```

Voici le code de l'application d'édition de messages :

```javascript
const amqp = require("amqplib");
const url = "amqp://localhost"; // Remplacez par l'URL de votre serveur RabbitMQ
const queue = "queue";

async function sendMessage(msg) {
  try {
    const connection = await amqp.connect(url);
    const channel = await connection.createChannel();
    
    await channel.assertQueue(queue);
    await channel.sendToQueue(queue, Buffer.from(msg));
    
    console.log(`Message envoyé à ${queue} : ${msg}`);
    
    await channel.close();
    await connection.close();
  } catch (err) {
    console.error("Échec de l'envoi du message :", err);
  }
}

sendMessage("Bonjour le monde !");
```

Voici le résultat du code :

![Code Node JS exécuté](https://www.freecodecamp.org/news/content/images/2024/08/msg-queue.PNG align="left")

## Informations supplémentaires

Jusqu'à présent, nous avons terminé ce tutoriel sur la mise en file d'attente des messages et son rôle dans la facilitation de la communication fluide entre divers systèmes. Pour améliorer davantage vos compétences, voici quelques meilleures pratiques supplémentaires qui devraient être mises en œuvre lors de la construction de services complexes :

* Limitation de débit
  
* Équilibrage de charge
  
* Surveillance et journalisation des applications
  
* Intégration et déploiement continus
  

## Résumé

Nous avons mis en lumière l'importance des courtiers de messages et comment implémenter la mise en file d'attente des messages dans une application backend.

N'hésitez pas à consulter mes autres articles [ici](https://linktr.ee/tobilyn77). Jusqu'à la prochaine fois, continuez à coder !