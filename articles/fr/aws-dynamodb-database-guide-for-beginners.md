---
title: AWS DynamoDB – Guide de la base de données NoSQL pour débutants
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-01-11T16:50:00.000Z'
originalURL: https://freecodecamp.org/news/aws-dynamodb-database-guide-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/dynamodb.png
tags:
- name: AWS
  slug: aws
- name: database
  slug: database
- name: NoSQL
  slug: nosql
seo_title: AWS DynamoDB – Guide de la base de données NoSQL pour débutants
seo_desc: 'What is DynamoDB?

  DynamoDB is a fully managed NoSQL database from AWS. DynamoDB is similar to other
  NoSQL databases like MongoDB, except for the fact that you don’t have to do any
  maintenance or scaling on your part.


  DynamoDB can handle more than 10...'
---

## Qu'est-ce que DynamoDB ?

DynamoDB est une base de données [NoSQL](https://www.mongodb.com/nosql-explained) entièrement gérée par AWS. DynamoDB est similaire à d'autres bases de données NoSQL comme MongoDB, à l'exception du fait que vous n'avez pas à effectuer de maintenance ou de mise à l'échelle de votre côté.

> DynamoDB peut gérer plus de 10 billions de requêtes par jour et peut supporter des pics de plus de 20 millions de requêtes par seconde — via la documentation AWS.

DynamoDB offre une sécurité intégrée, des sauvegardes à la demande et ponctuelles, une réplication inter-régions, une mise en cache en mémoire et de nombreuses autres fonctionnalités qui supportent des charges de travail critiques pour les entreprises.

Plus important encore, DynamoDB fonctionne de manière transparente avec d'autres applications AWS comme S3 et Lambda.

Mais avant de commencer l'article, il est important que vous compreniez le concept des bases de données NoSQL.

## Qu'est-ce que les bases de données NoSQL ?

NoSQL signifie « **not only SQL** ». En termes simples, les bases de données NoSQL stockent des documents dans un format similaire à JSON, tandis que les bases de données relationnelles stockent les données sous forme de tableau.

NoSQL offre plus de flexibilité en termes de modélisation des données et ne vous oblige pas à avoir un schéma pour stocker des documents.

Quelques types de bases de données NoSQL incluent les bases de données de documents purs (comme MongoDB), les magasins clé-valeur (comme DynamoDB), les bases de données à colonnes larges (comme Cassandra) et les bases de données de graphes (comme Neo4j). [En savoir plus sur les bases de données NoSQL ici](https://www.couchbase.com/resources/why-nosql).

Très bien. Maintenant, examinons quelques-unes des fonctionnalités de DynamoDB.

## Fonctionnalités principales de DynamoDB

### Mise à l'échelle automatique

Probablement la fonctionnalité la plus importante de DynamoDB est qu'elle offre une mise à l'échelle automatique du débit et du stockage en fonction des performances ou de l'utilisation de votre application.

Dans un serveur de base de données typique, l'administrateur système s'occupe de la mise à l'échelle lorsque l'application rencontre un trafic plus élevé que d'habitude.

Avec DynamoDB, vous pouvez créer des tables de base de données qui peuvent stocker et récupérer n'importe quelle quantité de données, et la mise à l'échelle est automatiquement gérée par AWS. Cela inclut la mise à l'échelle pour un trafic plus élevé et la réduction pour un trafic plus faible, afin que vous ne payiez que pour ce que vous utilisez.

### Modèles de données

DynamoDB prend en charge les modèles de données clé-valeur et document. Cela vous permet d'avoir un schéma flexible, de sorte que chaque ligne peut avoir n'importe quel nombre de colonnes à tout moment. Cela est crucial pour les entreprises en croissance qui ont des exigences en constante évolution.

Redéfinir le schéma de la base de données est un cauchemar que de nombreux développeurs/administrateurs de bases de données traversent dans une application en croissance. Cette flexibilité des modèles de données offre une solution de base de données robuste pour les petites ainsi que les grandes entreprises.

### Réplication

AWS s'occupe de la réplication des tables DynamoDB automatiquement en fonction de votre choix de régions AWS (réplication inter-régions). Même les applications distribuées peuvent avoir des performances de lecture et d'écriture en millisecondes à un chiffre en utilisant DynamoDB.

Avec la réplication en place, vous n'avez pas à vous soucier de la disponibilité des données. En cas de défaillance de la source principale, vous pouvez facilement accéder aux données à partir d'une réserve secondaire, réduisant ainsi la probabilité de temps d'arrêt de l'application.

### Sauvegardes et récupération

DynamoDB fournit des sauvegardes à la demande pour vos tables que vous pouvez activer dans la console AWS. Vous pouvez également activer la sauvegarde automatique et l'archivage de vos données vers d'autres solutions AWS comme S3.

DynamoDB offre également la récupération à un instant donné. Cela protège vos données contre les opérations d'écriture/suppression accidentelles.

Avec la récupération à un instant donné, vous pouvez restaurer votre base de données à n'importe quel moment au cours des 35 derniers jours. La récupération à un instant donné est réalisée en stockant des sauvegardes incrémentielles de votre base de données et cela est géré automatiquement par AWS.

### Sécurité

DynamoDB chiffre les données au repos par défaut et également en transit en utilisant les clés stockées dans AWS Key Management Service (ou des clés fournies par le client).

Avec le chiffrement en place, vous pouvez construire des applications sensibles à la sécurité qui répondent aux exigences de conformité et de réglementation. DynamoDB fournit également un contrôle d'accès via les [rôles AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

### Surveillance

La surveillance est cruciale pour toute application critique pour les entreprises. Elle aide à maintenir la fiabilité et notifie également le personnel en cas d'événement ou de défaillance.

AWS offre des outils de surveillance détaillés comme CloudWatch Logs, CloudWatch Events et CloudTrail Logs qui vous aideront à surveiller, notifier et déboguer tous les types d'événements dans DynamoDB. Vous pouvez également définir des déclencheurs personnalisés basés sur des métriques comme les erreurs système, l'utilisation de la capacité, etc.

Maintenant, comparons DynamoDB avec deux alternatives de bases de données populaires — MySQL et MongoDB.

## DynamoDB vs MySQL

Il existe une différence majeure entre MySQL et MongoDB car MySQL est une base de données relationnelle. En termes d'avantages, je pense que MySQL est limité en raison de l'exigence d'avoir un schéma avant de pouvoir commencer à pousser des données.

Mais MySQL est également excellent pour de nombreux cas d'utilisation. Il est souvent appelé « La base de données open-source la plus populaire au monde » et il offre un serveur de base de données SQL (Structured Query Language) rapide, multithread, multi-utilisateur et robuste.

Mais être une base de données NoSQL donne à DynamoDB beaucoup plus de flexibilité en termes de modélisation des données.

Même si AWS fournit des services gérés pour MySQL et d'autres bases de données relationnelles, DynamoDB est une base de données conçue par AWS et pas seulement une solution de base de données hébergée. Cela offre donc plus d'améliorations et de fonctionnalités que MySQL et d'autres bases de données relationnelles ne peuvent pas.

## DynamoDB vs MongoDB

DynamoDB et MongoDB sont étroitement liés l'un à l'autre puisque tous deux sont des bases de données NoSQL. Mais puisque DynamoDB est construit et maintenu par AWS, il offre beaucoup plus de fonctionnalités et d'intégrations, en particulier avec d'autres services Amazon comme S3, par rapport à MongoDB.

Si je dirigeais une entreprise en croissance, je préférerais utiliser DynamoDB uniquement en raison de sa scalabilité et de ses fonctionnalités de réplication inter-régions. AWS ne propose pas de service géré MongoDB, mais si vous en cherchez un, [MongoDB Atlas](https://www.mongodb.com/atlas/database) serait une excellente alternative.

Une autre fonctionnalité importante de DynamoDB par rapport à MongoDB est que MongoDB n'est pas sécurisé par défaut et vous devez configurer la sécurité vous-même. DynamoDB est sécurisé par défaut, donc ce pourrait être une meilleure option si la sécurité est un critère décisif pour vous.

## Conclusion

AWS DynamoDB est une base de données NoSQL entièrement gérée qui peut monter et descendre en échelle en fonction de la demande. AWS s'occupe des fonctions typiques, y compris la correction de logiciels, la réplication et la maintenance.

DynamoDB offre également un chiffrement au repos, des instantanés ponctuels et des capacités de surveillance puissantes. En résumé, c'est une excellente option lorsque vous construisez une application qui nécessite une base de données NoSQL scalable et haute performance.

_Vous avez aimé cet article ?_ [**_Rejoignez ma newsletter_**](http://tinyletter.com/manishmshiva) _et recevez un résumé de mes articles et vidéos chaque lundi matin. Vous pouvez également [**visiter mon blog ici.**](https://www.hardcoder.io/)