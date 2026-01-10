---
title: Comment utiliser RabbitMQ avec NodeJS pour envoyer et recevoir des messages
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-05-23T14:45:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-rabbitmq-with-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/What-is-RabbitMQ-and-How-to-use-it-with-NodeJS_1.png
tags:
- name: message broker
  slug: message-broker
- name: Node.js
  slug: nodejs
seo_title: Comment utiliser RabbitMQ avec NodeJS pour envoyer et recevoir des messages
seo_desc: "If you're exploring the world of distributed systems and real-time data\
  \ pipelines, you've probably come across the concept of message queues. \nThere\
  \ are a number of tools in this field, but RabbitMQ and Apache Kafka are two of\
  \ the most popular. While..."
---

Si vous explorez le monde des systèmes distribués et des pipelines de données en temps réel, vous avez probablement rencontré le concept des files d'attente de messages. 

Il existe un certain nombre d'outils dans ce domaine, mais RabbitMQ et Apache Kafka sont deux des plus populaires. Bien que les deux soient robustes et fiables, ils ont des caractéristiques et des cas d'utilisation uniques qui les distinguent.

RabbitMQ est un courtier de messages open-source. Il est reconnu pour sa flexibilité et son support de divers protocoles de messagerie. Apache Kafka gagne rapidement en popularité et est connu pour sa capacité à gérer des flux de données en temps réel avec une faible latence.

Dans ce tutoriel, je me concentrerai sur RabbitMQ, ses fonctionnalités principales et comment vous pouvez l'utiliser pour construire efficacement des applications scalables et faiblement couplées.

Restez avec moi alors que nous explorons le monde de RabbitMQ, ses capacités uniques et comment il se distingue dans le paysage en constante évolution des technologies de files d'attente de messages.

## Qu'est-ce que RabbitMQ ?

RabbitMQ est un logiciel de courtier de messages open-source (également appelé middleware orienté messages) qui implémente le protocole Advanced Message Queuing Protocol (AMQP). Il fournit une plateforme commune pour envoyer et recevoir des messages. 

RabbitMQ supporte plusieurs protocoles de messagerie et peut être déployé dans des configurations distribuées et fédérées pour répondre aux exigences de haute échelle et de haute disponibilité.

## Quand devez-vous utiliser RabbitMQ ?

Considérez un site de commerce électronique (comme Amazon) où les utilisateurs peuvent passer des commandes qui doivent être traitées. 

Le système de traitement des commandes peut impliquer plusieurs étapes, telles que les vérifications d'inventaire, le traitement des paiements, l'expédition, etc., chacune pouvant potentiellement prendre un certain temps et étant idéalement gérée de manière asynchrone.

1. **Vérifications d'inventaire** : Lorsqu'un utilisateur passe une commande, le système doit vérifier si les produits commandés sont en stock. Vous pouvez envoyer un message à une file d'attente qui est consommée par un service responsable de la vérification de l'inventaire. De cette manière, même si le service d'inventaire est temporairement hors ligne ou surchargé, les messages de commande ne seront pas perdus - ils seront traités dès que le service sera disponible.
2. **Traitement des paiements** : Le traitement des paiements peut être effectué par un autre microservice. Une fois la vérification de l'inventaire terminée, un message peut être envoyé à une file d'attente pour le service de paiement. Cela découple le traitement des paiements de la vérification de l'inventaire, permettant à ces opérations de s'évoluer indépendamment.
3. **Expédition** : Après confirmation du paiement, un message peut être envoyé à une autre file d'attente qui est responsable de la gestion de l'expédition. Encore une fois, ce service peut prendre un certain temps, mais parce qu'il est découplé du reste du système, il ne ralentira pas les autres opérations.
4. **Système de notification** : Après chaque placement de commande, paiement et expédition réussis, des notifications (Email ou SMS) doivent être envoyées au client. Cela peut être géré par des services séparés qui écoutent des files d'attente spécifiques.

## Comment installer et exécuter RabbitMQ

Dans cet exemple, je vais vous montrer comment utiliser Docker pour exécuter RabbitMQ. Mais si vous préférez, vous pouvez l'installer et l'exécuter manuellement sur votre système. La documentation officielle fournit un guide détaillé sur la façon de procéder.

Je trouve que Docker est un outil pratique pour exécuter RabbitMQ car il simplifie les processus de configuration et de gestion. Si vous êtes nouveau dans Docker, je vous recommande de lire mes tutoriels précédents liés à Docker pour une compréhension approfondie.

Pour commencer, vous devrez extraire l'image Docker depuis Docker Hub.

```
docker pull rabbitmq
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-64.png)
_Image Docker officielle de RabbitMQ dans Docker Desktop_

Avant d'exécuter l'image, vous devez mapper les deux numéros de port (15672 et 5672).

1. **Port 5672** : Il s'agit du port par défaut pour RabbitMQ lors de l'utilisation de AMQP (Advanced Message Queuing Protocol). Les clients qui se connectent avec AMQP utilisent généralement ce port. Donc, si vous utilisez une bibliothèque cliente AMQP pour vous connecter à RabbitMQ, il est probable qu'elle se connecte sur le port 5672.
2. **Port 15672** : Il s'agit du port par défaut pour l'interface utilisateur de gestion de RabbitMQ, lors de l'utilisation du plugin `rabbitmq_management`. L'interface utilisateur de gestion est une interface basée sur le web qui vous permet de surveiller et de contrôler votre serveur RabbitMQ.

J'exécute RabbitMQ sur Docker en ajoutant les ports mentionnés ci-dessus. Veuillez vous référer à la capture d'écran ci-dessous pour une référence supplémentaire. 

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-75.png)
_Configuration des ports pour exécuter l'image RabbitMQ._

Notre serveur RabbitMQ est opérationnel et fonctionne dans Docker.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-66.png)
_Conteneur du serveur RabbitMQ en cours d'exécution dans Docker_

## Comment implémenter une file d'attente de messages dans NodeJS

J'utiliserai `amqplib`, qui est une bibliothèque NodeJS populaire qui fournit une API pour interagir avec RabbitMQ. Elle supporte toutes les fonctionnalités du modèle AMQP 0-9-1 de RabbitMQ, y compris des choses comme les canaux de confirmation, les échanges, les files d'attente, les liaisons et les propriétés des messages.

J'ai utilisé le terme Protocole AMQ dans ce tutoriel et je pense que c'est le bon moment pour donner une rapide introduction à ce sujet.

### Qu'est-ce que AMQP ?

AMQP signifie Advanced Message Queuing Protocol. Il s'agit d'un protocole standard ouvert pour les middlewares orientés messages. Les caractéristiques définissantes de AMQP sont l'orientation message, la mise en file d'attente, le routage (y compris point à point et publication-abonnement), la fiabilité et la sécurité.

AMQP a les composants suivants :

1. **Producteur** est une application qui envoie des messages.
2. **Consommateur** est une application qui reçoit des messages.
3. **File d'attente** est un tampon qui stocke les messages.
4. **Message** est l'information qui est envoyée du producteur à un consommateur.
5. **Échange** reçoit les messages des producteurs et les pousse vers les files d'attente en fonction des règles définies par le type d'échange. Le type d'échange détermine comment les messages sont routés.
6. **Liaison** lie la file d'attente à l'échange.

Le protocole AMQP permet une communication standardisée entre différentes applications, ce qui en fait un bon choix pour un système de messagerie dans une architecture de microservices. Ce protocole peut garantir qu'un message est livré non seulement au système de messagerie, mais jusqu'au bon consommateur.

Vous vous souviendrez de l'exemple que j'ai décrit au début de cet article sur l'implémentation de haut niveau des files d'attente de messages sur un site de commerce électronique.

Passons en revue le même exemple, mais un peu plus en profondeur dans le contexte de RabbitMQ.

### Passation de commande

Lorsque qu'un client passe une commande sur le site de commerce électronique, le service de commande produit un message vers un échange RabbitMQ. Le message contient des informations sur l'ID du produit et la quantité commandée.

### Mise à jour de l'inventaire

Un service d'inventaire est configuré comme un consommateur pour recevoir des messages d'une file d'attente liée à l'échange. Une fois qu'il reçoit un message, il réduit l'inventaire pour le produit spécifié de la quantité commandée. Si l'inventaire est insuffisant, il peut envoyer un message au service de commande pour indiquer le problème.

### Confirmation de commande

Une fois que le service d'inventaire a mis à jour l'inventaire avec succès, il enverra un message au service de commande. Le service de commande, configuré comme un consommateur pour cet échange, peut alors mettre à jour le statut de la commande et notifier le client.

## Avantages

### Résilience

Supposons que votre service d'inventaire soit hors ligne pendant un certain temps. Les messages dans la file d'attente RabbitMQ resteront là et ne seront pas perdus. Une fois que le service d'inventaire est de nouveau en ligne, il continuera à traiter les messages là où il s'était arrêté.

### Scalabilité

Pendant les périodes de trafic élevé, plus d'instances du service d'inventaire peuvent être lancées, toutes consommant des messages de la même file d'attente. Cela permet l'équilibrage de charge et garantit que le système peut gérer la charge accrue.

Revenons à notre implémentation. Dans cet exemple, nous allons envoyer un message de l'expéditeur à notre récepteur. À l'extrémité du récepteur, nous imprimons le message sur la console. 

## Comment créer l'expéditeur (Producteur)

Il s'agit du composant ou de la partie de notre application qui crée et envoie des messages à la file d'attente de messagerie. 

L'expéditeur n'envoie pas de messages directement au consommateur. Au lieu de cela, il envoie les messages à un échange dans RabbitMQ. L'échange route ensuite les messages vers la file d'attente appropriée en fonction de certains critères.

Ici, nous créons une file d'attente appelée `product_inventory`. Alternativement, vous pouvez cloner mon dépôt depuis [ici](https://github.com/5minslearn/rabbit-sender). 

<script src="https://gist.github.com/5minslearn/f7f53295e107e50424a762739f3747d9.js"></script>

Nous pouvons envoyer uniquement des tableaux d'octets dans le message, donc je convertis l'objet message en une chaîne et l'envoie à la file d'attente. À partir du code ci-dessus, vous pouvez comprendre que nous créons un canal et envoyons un message à travers celui-ci. 

## Comment créer le récepteur (Consommateur)

Il s'agit du composant ou de la partie de notre application qui reçoit et traite les messages de la file d'attente. Un consommateur peut interroger en continu la file d'attente pour de nouveaux messages ou être configuré pour se déclencher automatiquement lorsqu'un nouveau message est ajouté à la file d'attente.

Ici, nous écoutons les messages. Alternativement, vous pouvez cloner mon dépôt depuis [ici](https://github.com/5minslearn/rabbit-receiver). 

<script src="https://gist.github.com/5minslearn/1c7a63cdfaef99accb503857d9afbcf4.js"></script>

Dans le code ci-dessus, nous écoutons les messages (`consume`) et les imprimons sur la console une fois que nous les recevons. 

Dans le contexte de notre cas d'utilisation spécifique, le fichier contenant l'expéditeur de messages (ou producteur) doit généralement être situé dans le répertoire racine de notre projet de site de commerce électronique. C'est là que nous générons et envoyons des messages en fonction des actions de l'utilisateur, comme le passage d'une commande.

D'autre part, le fichier contenant le récepteur de messages (ou consommateur) doit idéalement être situé dans le service de gestion des stocks. Cela est dû au fait que le service de gestion des stocks est responsable du traitement de ces messages, comme la mise à jour de l'inventaire lorsqu'une commande est passée.

Lançons d'abord notre service récepteur :

```
yarn start
```

La sortie initiale du service consommateur ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-78.png)
_Sortie initiale dans le service consommateur - Écoute des messages_

Une fois que nous exécutons notre expéditeur, un message sera envoyé au consommateur. Exécutez la même commande `yarn start` sur le dépôt de l'expéditeur. 

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-79.png)
_Envoi d'un message du producteur au consommateur_

Hourra ! Nous avons reçu un message envoyé par le producteur RabbitMQ dans notre service consommateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-80.png)
_Message reçu du producteur RabbitMQ dans notre service consommateur_

## Conclusion

Dans cet article, nous avons exploré les bases de RabbitMQ, un courtier de messages robuste et efficace, et démontré son application dans un environnement NodeJS. 

En utilisant un scénario simple de commerce électronique, nous avons montré comment configurer un expéditeur (producteur) et un consommateur pour gérer des messages asynchrones entre différentes composantes de notre application. Mais dans les applications réelles, vous rencontrerez probablement des scénarios plus complexes qui nécessitent des intégrations avancées et l'utilisation de RabbitMQ.

Pour naviguer dans ces complexités, il est crucial d'avoir une solide compréhension des concepts sous-jacents de RabbitMQ et de son protocole AMQP. À mesure que vous approfondissez RabbitMQ, vous trouverez qu'il s'agit d'un outil incroyablement polyvalent, capable de gérer une large gamme de besoins en messagerie, et vous aidant finalement à construire des applications scalables, découplées et résilientes.

Consultez le code source du projet sur GitHub : [rabbit-sender](https://github.com/5minslearn/rabbit-sender), [rabbit-receiver](https://github.com/5minslearn/rabbit-receiver). 

Pour en savoir plus sur RabbitMQ, abonnez-vous à ma newsletter par email sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_rabbitmq) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_rabbitmq)) et suivez-moi sur les réseaux sociaux.