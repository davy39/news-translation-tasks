---
title: Comment migrer vos données locales vers MongoDB Atlas
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-03-18T14:40:31.000Z'
originalURL: https://freecodecamp.org/news/mongodb-data-migration
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/mongoCloud.jpg
tags:
- name: Cloud
  slug: cloud
- name: MongoDB
  slug: mongodb
seo_title: Comment migrer vos données locales vers MongoDB Atlas
seo_desc: 'Data forms the bedrock of our daily lives, as a lot of day-to-day decision-making
  is hinged on its existence. Just like energy, data can be transformed from one medium
  to another.

  So far, web development has become much more advanced, and data migrat...'
---

Les données constituent la base de notre vie quotidienne, car une grande partie de la prise de décision au jour le jour repose sur leur existence. Tout comme l'énergie, les données peuvent être transformées d'un support à un autre.

Jusqu'à présent, le développement web est devenu beaucoup plus avancé, et la migration et la sauvegarde des données sont des compétences essentielles que tout développeur web devrait avoir pour aider à assurer la continuité des données et préserver les informations des utilisateurs, quelles que soient les circonstances.

Pour les développeurs comme moi qui préfèrent tester toutes les fonctionnalités de leur code localement dans un environnement de développement avant le déploiement final dans le cloud, ce tutoriel vous sera utile lorsque vous serez confronté au défi de migrer vos données MongoDB stockées localement vers une plateforme cloud ou toute autre plateforme.

L'inspiration pour cet article est le résultat de mon besoin de migrer l'ensemble des données JSON de mon serveur local MongoDB Compass vers le cloud (MongoDB Atlas) pour un projet en cours. J'ai parcouru les ressources internet et la documentation sans fin, mais je n'ai pas pu trouver une solution simple et directe. Après plusieurs essais et erreurs, j'ai réussi à effectuer la migration. Cet article devrait servir de guide définitif dont vous avez besoin pour vous faire gagner du temps et obtenir des résultats rapides.

Dans cet article, nous allons nous pencher sur la gestion des données dans MongoDB, la sauvegarde des données et les outils efficaces de migration de données qui facilitent l'ensemble du processus. Cet article est adapté aux personnes ayant des connaissances intermédiaires à avancées de MongoDB et du développement backend.

Si vous avez des difficultés avec les terminologies utilisées dans cet article, je vous suggère d'étudier la documentation MongoDB [ici](https://www.mongodb.com/docs/).

Commençons.

## Introduction à MongoDB

MongoDB est une base de données NoSQL non relationnelle qui stocke les données via le modèle de document au format JSON. Elle est assez populaire et se classe parmi les bases de données les plus utilisées au monde.

Elle est également plus conviviale pour le code, car elle est actuellement la base de données par défaut utilisée par de nombreux développeurs full stack et backend basés sur JavaScript.

Elle offre diverses options de base de données, comprenant à la fois des serveurs de base de données locaux et une base de données basée sur le cloud en tant que plateforme.

Un bon exemple de cela est MongoDB Atlas. MongoDB Atlas est une implémentation flexible et scalable de MongoDB avec une sécurité cloud robuste.

Il fournit l'indexation, l'équilibrage de charge et le sharding, parmi d'autres fonctionnalités. Plus d'informations à ce sujet peuvent être trouvées [ici](https://www.mongodb.com/features).

## Comment initialiser le serveur MongoDB

Vous devriez déjà avoir le serveur local MongoDB installé. Cependant, si vous ne l'avez pas installé, il peut être téléchargé [ici](https://www.mongodb.com/try/download/community).

Le serveur MongoDB peut ensuite être facilement exécutable en ajoutant son chemin aux variables d'environnement sur Windows.

Pour initialiser l'application MongoDB, activez l'invite de commande et tapez
`Mongod`

![Serveur Mongo DB en cours d'exécution](https://hackmd.io/_uploads/r1aAf6gCp.jpg)
_Serveur MongoDb en cours d'exécution_

Pour explorer les bases de données sur le serveur MongoDB, ouvrez l'invite de commande MongoDB et tapez `show dbs`

![Les bases de données dans mon serveur mongodb](https://hackmd.io/_uploads/rJY2G6eC6.jpg)
_Les bases de données sur le serveur MongoDB_

Cela affiche toutes les bases de données sur le serveur MongoDB.

Avec cela, continuons à migrer l'une de ces bases de données vers le cloud.

## Comment sauvegarder les données

Pour télécharger efficacement les collections de la base de données vers le cloud, elles doivent d'abord être sauvegardées.

Pour sauvegarder votre base de données, vous devrez installer un outil supplémentaire. Retournez sur le site de téléchargement de MongoDB et téléchargez les outils d'administration de la base de données MongoDB [ici](https://www.mongodb.com/try/download/database-tools).

Ce package contient de nombreux outils de base de données, tels que `MongoExport`, `MongoImport`, `MongoDump` et `MongoRestore`.

Les paramètres ci-dessus sont applicables pour les utilisateurs qui ont une version de MongoDB supérieure à la version 4.4. MongoDB a décidé de le publier en tant qu'outil autonome. Pour les utilisateurs dont la version est inférieure à la version 4.4, ces outils peuvent être préinstallés dans le package MongoDB.

Maintenant, passons aux deux principaux outils qui aideront à faciliter le processus de migration : `MongoDump` et `MongoRestore`.

Lorsque `MongoDump` est exécuté sur une base de données, il aide à créer un fichier de sauvegarde de la base de données au format JSON encodé en binaire (BSON). Tandis que `MongoRestore` aide à restaurer la base de données sauvegardée dans MongoDB pour une utilisation.

Ensuite, assurez-vous que leur chemin de package est inclus dans les variables d'environnement afin de garantir une exécution efficace.

Pour sauvegarder une base de données locale, ouvrez l'invite de commande MongoDB et entrez cette commande :

```
Mongodump --db={LeNomDeVotreBD} --collection={LeNomDeVotreCollection} –out={Le nom du dossier où les fichiers JSON sauvegardés seront situés}

```

Avec cette exécution, vous avez réussi à sauvegarder votre base de données locale MongoDB.

## Comment configurer MongoDB Atlas

MongoDB Atlas est l'option cloud de MongoDB en tant que service de base de données accessible à ses utilisateurs à tout moment avec peu ou pas de perturbation.

De plus, pour la plupart des applications de production qui utilisent la puissance de MongoDB sur le serveur en tant qu'outil de base de données, le fournisseur le plus facile et le plus pratique de cette solution est MongoDB Atlas.

Par conséquent, c'est notre choix pour sauvegarder nos données MongoDB dans le cloud. Je suppose que vous avez déjà un compte MongoDB Atlas, mais vous pouvez encore en créer un et ensuite créer une base de données qui servira de destinataire pour la base de données locale.

Pour configurer le compte, veuillez vous rendre sur la page d'accueil d'Atlas [ici](https://www.mongodb.com/atlas/database). Créez un compte et vous serez dirigé vers un tableau de bord où vous pourrez créer de nouvelles bases de données.

![atllas](https://hackmd.io/_uploads/S15QNeGAp.jpg)
_Page d'accueil de MongoDb Atlas_

Vous pouvez cependant lui donner le nom que vous souhaitez. Pour compléter le téléchargement des données locales MongoDB vers le cloud, accédez à l'onglet des paramètres sur la base de données MongoDB Atlas et cliquez sur l'option de migration des données. Avec cela fait avec succès, passons maintenant à la suite du processus de migration.

## Comment migrer vos données vers le cloud

Pour migrer votre base de données sauvegardée vers le cloud, `MongoImport` et `MongoExport` seront invoqués.

Dans l'invite de commande, collez le code de migration copié depuis Atlas, puis exécutez-le dans l'invite de commande. Avec cela, vous devriez voir un texte de succès.

Vous pouvez ensuite vérifier et actualiser votre base de données cloud pour voir les nouveaux fichiers qui y ont été téléchargés. Par la suite, vous pouvez connecter la nouvelle base de données cloud à votre application backend et l'exécuter avec succès pour obtenir les mêmes résultats sur votre ordinateur local.

## Conclusion

Avec cela, nous arrivons à la fin du tutoriel. Nous espérons que vous avez appris la gestion et la migration des données dans MongoDB, les outils impliqués et toutes ses intricacités.

N'hésitez pas à laisser des commentaires et des questions, et consultez également mes autres articles [ici](https://www.freecodecamp.org/news/author/oluwatobi/). Jusqu'à la prochaine fois, continuez à coder !