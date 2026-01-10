---
title: Le Modèle AWS Web Complet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-05T21:56:09.000Z'
originalURL: https://freecodecamp.org/news/the-complete-aws-web-boilerplate-d0ca89d1691f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AD9ZSLXKAhZ-_WomszsmPg.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Le Modèle AWS Web Complet
seo_desc: 'By Kangze Huang

  Build powerful scalable web apps by leveraging Amazon Cloud


  Table of Contents


  Part 0: Introduction to the Complete AWS Web Boilerplate

  Part 1: User Authentication with AWS Cognito (3 parts)

  Part 2: Saving File Storage Costs with Ama...'
---

Par Kangze Huang

#### Construisez des applications web puissantes et évolutives en exploitant le cloud Amazon

![Image](https://cdn-media-1.freecodecamp.org/images/fzOJgD2oVvWU8x7OmE7cDU3x1M3KQ6xkRpGp)

### Table des Matières

> **Partie 0 :** [Introduction au Modèle AWS Web Complet](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.3eqpvcjsy)

> **Partie 1 :** [Authentification des Utilisateurs avec AWS Cognito](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.cbkz7b2jp) (3 parties)

> **Partie 2 :** [Économiser les Coûts de Stockage de Fichiers avec Amazon S3](https://medium.com/@kangzeroo/amazon-s3-cloud-file-storage-for-performance-and-cost-savings-8f38d7769619#.l9so2hk00) (1 partie)

> **Partie 3 :** [Envoyer des E-mails avec Amazon SES](https://medium.com/@kangzeroo/sending-emails-with-amazon-ses-7617e83327b6#.5nhcrr609) (1 partie)

> Partie 4 : Gérer les Utilisateurs et les Permissions avec AWS IAM **[Bientôt Disponible]**

> Partie 5 : Hébergement de Serveur Cloud avec AWS EC2 et ELB **[Bientôt Disponible]**

> Partie 6 : Le Tueur de MongoDB : AWS DynamoDB **[Bientôt Disponible]**

> Partie 7 : Mise à l'Échelle SQL Sans Douleur avec AWS RDS **[Bientôt Disponible]**

> Partie 8 : Architecture Sans Serveur avec Amazon Lambda **[Bientôt Disponible]**

### Bonjour 2017

Vous voulez construire des applications évolutives prêtes pour la production, mais vous n'avez pas les ressources pour embaucher une équipe de plusieurs personnes pour gérer tout le code nécessaire pour les grandes ligues. Vous avez entendu parler d'équipes de deux personnes qui créent des applications fantastiquement efficaces avec une fraction des budgets de milliers de dollars des équipes traditionnelles. Votre portefeuille vous aimerait si vous pouviez payer uniquement pour les services dont vous avez besoin, sans aucun des coûts fixes. Alors vous faites vos recherches et arrivez à Amazon Web Services, le plus grand et le plus complet fournisseur de services cloud au monde. Mais après une heure d'investigation, vous êtes submergé par la taille et la variété des solutions disponibles. "Damn", dites-vous, "par où commencer ?"

Si vous avez déjà regardé la documentation sur AWS et essayé de comprendre comment toutes les pièces s'assemblent, vous savez que ce n'est pas une tâche facile. Lorsque vous essayez d'implémenter quelque chose de simple comme S3, vous vous retrouvez dans IAM pour la sécurité et de là, vous pourriez tomber dans AWS STS, AWS Cognito... la liste est longue. Et EC2 ? Les groupes de sécurité ? AWS Lambda ? C'est juste un trou de lapin après l'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/L0ovnoYuFQiYh-ms3-X8Ntcvh7DJeWOBqMTx)
_Un regard intimidant sur Amazon Web Services_

![Image](https://cdn-media-1.freecodecamp.org/images/UFCyDOjarhXiUk3qsk-KzYtG7KUUHayG-qNc)
_La nouvelle page d'accueil semble toujours intimidante_

Maintenant, vous n'avez pas nécessairement besoin d'utiliser Amazon pour tout. Si vous savez déjà comment intégrer l'authentification des utilisateurs avec des moyens existants, c'est probablement votre meilleure option. Pas besoin d'ajouter une complexité supplémentaire. Mais qu'en est-il de la mise à l'échelle des bases de données ? D'accord, peut-être que vous n'avez pas besoin de mettre à l'échelle MAINTENANT, donc pas de problème. Mais gérez-vous vos secrets d'application de manière sécurisée ? Économisez-vous la bande passante du serveur en hébergeant vos gros fichiers ailleurs dans le cloud ? Peut-être que votre entreprise bénéficierait de la collecte de nombreuses données utilisateur, mais vous n'êtes pas sûr que votre base de données principale puisse gérer la charge supplémentaire. Il y a tant de choses que vous POURRIEZ faire pour développer votre produit, mais que vous NE FAITES PAS parce que c'est juste trop de travail.

Présentation du Modèle AWS Web Complet de Kangzeroo — une application de démarrage qui intègre pleinement Amazon dans chaque tâche d'infrastructure fastidieuse et qui se met à l'échelle automatiquement. En exploitant AWS dans vos applications dès le début, votre entreprise peut démarrer rapidement et concentrer vos précieuses ressources sur l'affinage de votre produit. Il s'agit véritablement d'une pile moderne qui vous permettra de manier le pouvoir d'une équipe entière de développeurs à une fraction du coût et du temps. Nous ne couvrirons pas chaque service Amazon, seulement ceux que vous utiliserez probablement. Si vous êtes excité et prêt à commencer, continuez à lire. Bien que ce soit une série de tutoriels avancés, n'ayez pas peur de suivre, même si vous ne codez pas — la connaissance est inestimable. Alors commençons !

### Aperçu de l'Infrastructure AWS

![Image](https://cdn-media-1.freecodecamp.org/images/GjAnNygebel-5sWN-MK2xIfCK3E954MKw37i)
_Les 8 services Amazon que nous utiliserons_

La capture d'écran précédente de tous les services AWS était super intimidante. Pour être honnête, j'essayais juste de vous faire peur. Ce sont les 8 services que nous utiliserons réellement. Passons en revue chaque service et à quoi il sert, ainsi que les options de niveau gratuit potentielles. Pour utiliser AWS, vous devez vous inscrire à un compte qui nécessite une carte de crédit. La bonne nouvelle est que vous n'aurez pas nécessairement à payer, car chaque nouveau compte AWS bénéficie d'un niveau d'utilisation gratuit pendant un an.

#### Identity & Access Management (IAM)

Amazon IAM est utilisé pour gérer les permissions dans votre compte Amazon. Un compte Amazon peut avoir plusieurs utilisateurs, comme un pour déployer des applications et un autre pour analyser uniquement des données. Comme vous ne voulez pas que l'analyste puisse modifier quoi que ce soit, nous avons besoin d'un "compte" séparé pour l'analyste. Nous pouvons utiliser IAM pour créer et gérer ce "compte" séparé (via les utilisateurs ou rôles IAM) et contenir notre paranoïa. Merci le ciel ! IAM peut également être utilisé pour accorder des permissions spécifiques à certains services, comme un rôle IAM spécifiquement pour envoyer des e-mails ou accéder à un bucket S3. IAM est complètement gratuit.

#### Elastic Cloud Compute (EC2)

Amazon EC2 est utilisé pour héberger vos applications sur des serveurs cloud virtuels. C'est le service Amazon le plus couramment utilisé et probablement l'hébergement cloud le moins cher et le plus fiable que vous puissiez obtenir. Vous avez peut-être entendu parler de concurrents d'EC2 comme DigitalOcean, Linode et A Small Orange qui semblent très conviviaux. Il est vrai qu'ils sont très conviviaux, mais pourquoi ne pas rester dans l'écosystème Amazon ? Gardez tout dans Amazon et vous n'aurez pas à apprendre plusieurs systèmes différents. Le meilleur, c'est que le niveau gratuit est très généreux ! Vous pouvez garder votre serveur en marche 24/7 et toujours rester dans les limites du niveau gratuit.

![Image](https://cdn-media-1.freecodecamp.org/images/zlHWTlarhJhz-BzszXJHaldWWlDVk1va7XTH)

#### Cognito

AWS Cognito est un service d'authentification et de gestion des utilisateurs. Avec Cognito, vous n'avez pas besoin de garder une trace des clés secrètes utilisées pour hacher les mots de passe ni d'implémenter une sécurité complexe. Tout est géré par Amazon, et vous obtenez même des fonctionnalités avancées comme l'authentification à deux facteurs et la fonctionnalité "j'ai oublié mon mot de passe". L'utilisation de Cognito facilite également la restriction de l'accès public à d'autres services AWS, comme S3, en associant un rôle IAM à une connexion Cognito et en donnant la permission d'accès uniquement à ce rôle. Cognito est très généreux, avec jusqu'à 50 000 utilisateurs actifs mensuels gratuits même après l'expiration du niveau gratuit.

![Image](https://cdn-media-1.freecodecamp.org/images/h-UeM9PsnYNf3uSiqoK6ewstuWGKQWQRu9Ws)

#### Simple Scalable Storage (S3)

AWS S3 est le stockage de fichiers cloud. C'est un service Amazon très populaire qui nous permet de stocker tout type de fichier de n'importe quelle taille sur un système de fichiers séparé de nos serveurs. D'un point de vue performance, c'est génial car les serveurs n'ont pas besoin de gaspiller de la puissance de calcul et de la bande passante pour transférer des fichiers. D'un point de vue financier, S3 est également une aubaine car la bande passante/stockage S3 est beaucoup moins chère que celle d'EC2. Au lieu d'envoyer un fichier image, vous envoyez une chaîne d'URL et votre client d'application récupère l'image depuis S3. Amazon S3 a également un niveau gratuit, mais même sans lui, c'est ridiculement bon marché. Pour stocker 10 Go d'images avec 30 Go de transfert de données sortantes et 1 million de requêtes GET, cela revient à un total mensuel de... 1,89 USD.

![Image](https://cdn-media-1.freecodecamp.org/images/MJTahOPp2EfVwLPsrhuw-mQ8nWjMHXql0D4h)

#### Relational Database Service (RDS)

AWS RDS (quel nom compliqué) est un service de base de données relationnelle gérée dans le cloud. Bien qu'Amazon propose sa propre base de données relationnelle propriétaire, appelée Amazon Aurora, vous pouvez choisir d'utiliser une variété de bases de données bien connues existantes. Les options incluent MySQL, PostgreSQL, Oracle et Microsoft SQL Server. Le grand avantage de RDS est qu'il se met à l'échelle automatiquement pour vous, vous faisant économiser des heures de travail coûteuses/expertise.

![Image](https://cdn-media-1.freecodecamp.org/images/mrxqe8rvfqf7TLJ4ejkjHz7H6JnkAXsSjMiM)

#### DynamoDB

AWS DynamoDB est une base de données noSQL propriétaire gérée et mise à l'échelle automatiquement par Amazon. Elle est idéale pour stocker vos données non structurées diverses, ou comme "alternative approximative" à AWS Redshift si vous ne pouvez pas vous le permettre. DynamoDB a vraiment mûri au fil des ans. Il y a quelques années, ce n'était qu'un magasin clé-valeur (c'est-à-dire sans objets ou tableaux imbriqués), mais aujourd'hui, il est extrêmement flexible. Vous pouvez imbriquer des objets jusqu'à 16 niveaux de profondeur et interroger sur plusieurs index. Cela en fait également une "alternative approximative" à MongoDB, à condition que vous ayez votre propre vérification de structure de données en place. Le meilleur, c'est que les 25 Go de stockage gratuit ne disparaissent pas après votre essai gratuit !

![Image](https://cdn-media-1.freecodecamp.org/images/pI8gSKh2-RQIdy3d-lztrjgaxuqXue4gBm2X)

#### Simple Email Service (SES)

Pourquoi se donner la peine de configurer votre propre serveur de messagerie lorsque vous pouvez utiliser AWS SES ? Si votre produit utilise des e-mails pour envoyer des reçus, des newsletters ou comme journal d'activité, vous pouvez utiliser SES pour gérer ces communications de manière abordable. L'envoi d'e-mails est un service cloud assez standard, et vous pourriez opter pour des fournisseurs comme MailChimp et SendGrid, mais encore une fois, rester dans l'écosystème Amazon a de nombreux avantages ! Alors que MailChimp vous offre 12 000 e-mails gratuits par mois, AWS SES vous en offre 62 000. Voici les économies d'échelle pour vous !

![Image](https://cdn-media-1.freecodecamp.org/images/qhy44pO6PgMnL2NjAFbs9P9k-LXyNpF1D6Tz)

#### Lambda

AWS Lambda est un service très unique offert par Amazon. L'un des principaux avantages de rester dans l'écosystème Amazon est que vous pouvez utiliser AWS Lambda pour déclencher des événements ou des actions d'un service à un autre sans exécuter votre propre serveur. Un exemple est si vous vouliez créer un dossier utilisateur dans votre bucket S3 chaque fois qu'un utilisateur s'inscrit. Ou peut-être voulez-vous déclencher un e-mail si quelqu'un supprime un certain contenu de votre base de données. Ou peut-être voulez-vous configurer des pipelines de données pour diffuser vos données utilisateur à traiter et à router en temps réel. Les possibilités sont flexibles et infinies ! AWS Lambda est également gratuit après la fin de votre période d'essai.

![Image](https://cdn-media-1.freecodecamp.org/images/qsOvcw7wJpSmlUeq-XME1f6pHu-qeEQTlt9C)

### Conclusion

Après avoir vu cet aperçu de haut niveau des services Amazon que nous utiliserons, vous êtes probablement très enthousiaste. C'est génial car je crois que vous devriez aimer la technologie que vous utilisez. Amazon est à la fois puissant et abordable, vous permettant d'être un développeur 10x (accomplit le travail de 10 autres programmeurs) en esprit et en pratique. Sentez-vous le pouvoir circuler dans vos veines ? Êtes-vous excité à l'idée d'apprendre cette pile ? Êtes-vous prêt à mettre à l'échelle dès le premier jour ? Si oui, commençons.

### Table des Matières

> **Partie 0 :** [Introduction au Modèle AWS Web Complet](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.3eqpvcjsy)

> **Partie 1 :** [Authentification des Utilisateurs avec AWS Cognito](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.cbkz7b2jp) (3 parties)

> **Partie 2 :** [Économiser les Coûts de Stockage de Fichiers avec Amazon S3](https://medium.com/@kangzeroo/amazon-s3-cloud-file-storage-for-performance-and-cost-savings-8f38d7769619#.l9so2hk00) (1 partie)

> **Partie 3 :** [Envoyer des E-mails avec Amazon SES](https://medium.com/@kangzeroo/sending-emails-with-amazon-ses-7617e83327b6#.5nhcrr609) (1 partie)

> Partie 4 : Gérer les Utilisateurs et les Permissions avec AWS IAM **[Bientôt Disponible]**

> Partie 5 : Hébergement de Serveur Cloud avec AWS EC2 et ELB **[Bientôt Disponible]**

> Partie 6 : Le Tueur de MongoDB : AWS DynamoDB **[Bientôt Disponible]**

> Partie 7 : Mise à l'Échelle SQL Sans Douleur avec AWS RDS **[Bientôt Disponible]**

> Partie 8 : Architecture Sans Serveur avec Amazon Lambda **[Bientôt Disponible]**

> Ces méthodes ont été partiellement utilisées dans le déploiement de [renthero.ca](http://renthero.ca)