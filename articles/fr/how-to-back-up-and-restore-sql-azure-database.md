---
title: Comment sauvegarder et restaurer les bases de données Azure SQL
subtitle: ''
author: Alex Tray
co_authors: []
series: null
date: '2024-01-24T22:34:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-back-up-and-restore-sql-azure-database
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/maxresdefault.jpg
tags:
- name: Azure
  slug: azure
- name: Backup
  slug: backup
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Comment sauvegarder et restaurer les bases de données Azure SQL
seo_desc: Microsoft's Azure provides many services via a single cloud, which lets
  them offer one solution for multiple corporate infrastructures. Development teams
  often use Azure because they value the opportunity to run SQL databases in the cloud
  and complet...
---

Microsoft Azure offre de nombreux services via un seul cloud, ce qui permet de proposer une solution unique pour plusieurs infrastructures d'entreprise. Les équipes de développement utilisent souvent Azure car elles apprécient la possibilité d'exécuter des bases de données SQL dans le cloud et de compléter des opérations simples via le portail Azure.

Mais vous aurez besoin d'une méthode pour sauvegarder vos données, car cela est crucial pour garantir le fonctionnement du site de production et la stabilité des flux de travail quotidiens. Ainsi, la création de sauvegardes Azure SQL peut vous aider, vous et votre équipe, à éviter les urgences de perte de données et à avoir le temps d'arrêt le plus court possible tout en maintenant le contrôle sur l'[infrastructure](https://www.hostpapa.com/blog/technology/what-is-an-it-infrastructure/).

Une autre raison d'avoir une sauvegarde à jour de la base de données Azure est la politique de Microsoft. Microsoft utilise le modèle de responsabilité partagée, qui rend l'utilisateur responsable de l'intégrité des données et de leur récupération, tandis que Microsoft ne garantit que la disponibilité de ses services. Microsoft recommande directement l'utilisation de solutions tierces pour créer des sauvegardes de bases de données.

Dans le cas où vous exécutez un serveur SQL local, vous devrez vous préparer à la possibilité de défaillances matérielles qui peuvent entraîner une perte de données et un temps d'arrêt. Une base de données SQL sur Azure aide à atténuer ce risque, bien qu'elle soit toujours sujette à des erreurs humaines ou à des menaces spécifiques au cloud comme les logiciels malveillants.

Ces menaces et d'autres rendent nécessaire l'activation des sauvegardes de bases de données Azure SQL pour toute organisation utilisant le service de Microsoft pour gérer et traiter des données.

Dans ce tutoriel, vous apprendrez à sauvegarder les bases de données Azure et à restaurer vos données à la demande avec les instruments natifs fournis par Microsoft, y compris des méthodes comme :

* Fonctionnalité de sauvegarde intégrée de la base de données Azure
* Archivage cloud
* Gestion de la base de données secondaire et des tables
* Serveur lié
* Stretch Database

## Pourquoi sauvegarder votre base de données SQL Azure ?

Bien que j'aie brièvement couvert cela dans l'introduction, il existe de nombreuses raisons de sauvegarder les données de votre base de données SQL Azure.

### Récupération après sinistre

Les centres de données peuvent être endommagés ou détruits par des cyberattaques planifiées, des infiltrations de logiciels malveillants aléatoires ([consultez cet article](https://www.nakivo.com/blog/how-to-protect-against-ransomware-attacks/) pour en savoir plus sur la protection contre les ransomwares), et des catastrophes naturelles comme les inondations ou les ouragans, entre autres. Les sauvegardes peuvent être utilisées pour récupérer rapidement les données et restaurer les opérations après divers cas de sinistre.

### Prévention de la perte de données

La corruption des données, la défaillance matérielle et la suppression accidentelle ou malveillante entraînent une perte de données et peuvent menacer une organisation. Les flux de travail de sauvegarde configurés pour s'exécuter régulièrement signifient que vous pouvez rapidement récupérer les données qui ont été perdues ou corrompues.

### Conformité et réglementations

Les exigences de conformité et les réglementations législatives peuvent être sévères, quelle que soit l'industrie de votre organisation. La plupart du temps, les lois vous obligent à maintenir la sécurité et à effectuer des sauvegardes régulières pour la conformité.

### Test et développement

Vous pouvez utiliser les sauvegardes pour créer des copies de bases de données Azure pour le développement, le dépannage ou les tests. Ainsi, vous pouvez corriger, développer ou améliorer les flux de travail de votre organisation sans impliquer l'environnement de production.

## Comment sauvegarder votre base de données Azure SQL

Sauvegarder votre base de données Azure SQL peut être difficile si vous passez par le processus sans préparation. C'est pourquoi j'ai écrit ce guide – pour vous aider à être préparé. Voici ce que nous allons couvrir dans les sections suivantes :

* Exigences pour la sauvegarde de la base de données SQL Azure
* Comment configurer les sauvegardes de bases de données dans Azure avec les outils natifs
* Archivage cloud
* Vérification des sauvegardes et restauration des données

### Exigences pour la sauvegarde de la base de données SQL Azure

Avant de sauvegarder vos bases de données SQL Azure, vous devez créer et configurer le stockage Azure. Avant de faire cela, vous devrez suivre les étapes suivantes :

Tout d'abord, ouvrez le portail de gestion Azure et trouvez **Créer une ressource**.

Ensuite, allez dans **Stockage** > **Compte de stockage**. Fournissez les informations, y compris l'emplacement et les noms d'un compte de stockage et d'un groupe de ressources selon vos préférences. Après avoir entré les informations, cliquez sur **Suivant**.

![Image](https://lh7-us.googleusercontent.com/TbuVyIRHXKkKd1__mMSo8RJTktZVnJjK2r8ijtY1h5gvlY5KqkRE8NPsej18m-A1-p3UwF-YO0W0p9AzJa8AW7TwR1yXp531y7qXrm84hJQIuTIKUMwhbnU7WAiUoGRPIdL_SrQCv0nxav4RnCu389o)
_Configuration du compte de stockage_

Ensuite, allez dans la section avancée pour des paramètres supplémentaires. Le choix optimal est de définir _"_Transfert sécurisé requis" comme **Activé** et "Autoriser l'accès" depuis **Tous** les réseaux. Pour plus de résilience en cas d'erreur humaine, vous pouvez définir "Suppression logicielle de blob" comme **Activé**. Avec ce paramètre, vous pouvez rapidement corriger les suppressions accidentelles dans le compte de stockage.

Après cela, spécifiez les balises dont vous avez besoin pour simplifier la navigation dans votre infrastructure.

![Image](https://lh7-us.googleusercontent.com/BTXJpa8dz9wKa7p9pQm84fmtqtwD5WEuRB9yh2_Htpa-pF86Zf70CuKP7j32uPR56igplljn6fehCuJEgnMkiCiAcZPZVU_FNEL2JZcrtVjunthzLKQOWp9wbtXLLLKMgYTerYNJpsiQxZjJcMlr05I)
_Balises de stockage de sauvegarde Azure_

Vérifiez les paramètres une fois de plus. Si tout est configuré correctement, cliquez sur **Créer**. Votre nouveau compte de stockage est maintenant créé.

Une fois le volume de stockage créé, il est temps de configurer un conteneur de stockage de données de sauvegarde.

Accédez au compte de stockage, trouvez **Conteneurs**, puis cliquez sur l'onglet **+ Conteneur**. Après cela, spécifiez un nom pour le nouveau conteneur et basculez le niveau d'accès public sur **Privé (aucun accès anonyme)**.

![Image](https://lh7-us.googleusercontent.com/eGTyBc9-uiRO52QsQ0pGzlWPAZlvyMR0miExCMX-Pck9yPQvUlwKqa0_N-zWc908TzHONdzLC2Kv8ACU5UHJjuJ8G6kBOmgxONkLN5LE33ItBsKOx5XdIKtMg8oYDY6eKrdFrZ0bhuOD535QALtqxMU)
_Conteneur de compte de stockage Azure_

Vous pouvez ensuite utiliser le conteneur comme stockage de sauvegarde (les fichiers .bak y seront stockés dans ce cas).

## Configuration de la sauvegarde de la base de données Azure

Maintenant, tout est prêt pour que vous sauvegardiez votre base de données SQL Azure. Faites ce qui suit pour créer une sauvegarde de la base de données :

Tout d'abord, allez dans **SQL Management Studio**, et établissez une connexion avec le serveur SQL. Après cela, faites un clic droit sur la base de données qui doit être sauvegardée. Le menu contextuel apparaît, alors allez dans **Tâches**. Ensuite, cliquez sur **Sauvegarder…**.

![Image](https://lh7-us.googleusercontent.com/l5g6ajoZ6ZuBObluCiG7mra9pz9BPgP-iOCAoGh36SY5zfg1yv300oQQ1cvgrVFNL75Nu7roFIVp2BfPze3ag5nTzL1NQYiO_fhUokWSd9fVms1SDcoP5pJ7a4wWdB3fQJWeKbrNIK_-vo2-hiXTDl0)
_Tâches de sauvegarde du serveur SQL_

Ensuite, trouvez l'onglet Destination, et définissez **Sauvegarder vers l'URL**. Après cela, cliquez sur **Nouveau conteneur**.

Ensuite, connectez-vous à Azure. Choisissez le conteneur que vous avez créé précédemment. Fournissez vos identifiants, puis cliquez sur **OK**.

Vous verrez un message vous demandant de vous connecter à l'abonnement Azure. Ensuite, choisissez le conteneur et cliquez sur **OK**.

Maintenant, vous verrez l'URL de destination de la sauvegarde configurée listée. Pour démarrer le flux de travail pour sauvegarder vos données Azure, cliquez sur **OK** une fois de plus.

Lorsque la sauvegarde de votre base de données SQL Azure est terminée, le message s'affiche : "_La sauvegarde de la base de données 'nom de votre base de données' s'est terminée avec succès_."

Le fichier de sauvegarde dans le conteneur cible devrait maintenant être visible depuis le portail Azure.

Gardez à l'esprit que, lors du téléchargement de sauvegardes vers un stockage cloud, vous pouvez rencontrer des problèmes si votre connexion réseau n'est pas assez rapide.

Dans ce cas, vous pouvez réorganiser vos flux de travail de sauvegarde : envoyez d'abord les données de sauvegarde vers un lecteur de stockage physique, puis envoyez une autre copie vers le cloud. Ainsi, vous pouvez prévenir les défis opérationnels qui pourraient apparaître en raison d'une insuffisance de bande passante réseau.

## Archivage cloud pour les sauvegardes de bases de données Azure

Les bases de données tendent à croître en volume à mesure que l'organisation se développe. Cela signifie que l'espace de stockage requis pour contenir les données et la sauvegarde de ces données augmente considérablement. De plus, le volume de données original prolonge la durée des flux de travail de sauvegarde complète, posant un autre défi.

Bien sûr, la première façon d'obtenir plus d'espace de stockage est de réviser régulièrement vos données et d'effacer les enregistrements qui sont irrelevants, obsolètes ou inutiles. Cependant, il est parfois difficile de déterminer si les données seront ou deviendront inutiles ou irrelevantes, surtout lorsqu'on traite des questions de conformité.

Pour garder votre organisation conforme dans tous les cas, l'archivage des données peut vous aider à résoudre deux problèmes à la fois : vous pouvez garantir l'accessibilité des données d'une part, et économiser de l'espace de stockage d'autre part.

Pour archiver votre base de données SQL dans le cloud, vous devez d'abord sauvegarder cette copie de base de données dans un conteneur blob Azure. Ensuite, pour déplacer un blob nouvellement créé vers le niveau d'archivage dans le portail Azure, faites ce qui suit :

1. Accédez au conteneur requis où la base de données SQL est stockée.
2. Choisissez le blob que vous devez déplacer.
3. Cliquez sur **Changer de niveau**.

![Image](https://lh7-us.googleusercontent.com/p41GC9ys42mQBQGWW1jqcR2xCfACpCYF1MpGG7Qx6EdqzjDSK6xnuqlPRCtDuhEmH_-8E6Lz2gY8H3h1CoZ4_jpScQWUxB-21GXOnuDEBSHVJiGa1zBiHu4JJP2Xntq1fpbPLjbb1-APOTJMO2sdBMk)
_Changer de niveau du conteneur blob Azure_

4. Dans le menu déroulant **Niveau d'accès**, choisissez **Archive**.

![Image](https://lh7-us.googleusercontent.com/qlyKGop3uj6kfi71fSpVsqKkhf8vc1TiQRyoeHEiwjKdg1i3Dsz_LXLHcD5q-qR77utIPUbkLyWU7Xzn7ehl3Z1IWUQZjy0LndXLEcDA1PRZj4ufO8QGR0GCmEDGqoWQ6paFwo8pn0VbUH8RWjlRzLU)
_Changer de niveau du blob Azure_

5. Cliquez sur **Enregistrer**.

De plus, le niveau de stockage Archive est le plus abordable dans Azure, ce qui signifie que vous pouvez réduire le TCO des données de votre base de données avec celui-ci.

### Gestion de la base de données secondaire et des tables

Il existe plusieurs flux de travail qui peuvent vous aider à configurer l'archivage des sauvegardes de bases de données Azure pour votre organisation. Lorsque vous avez besoin que les données restent dans la base de données initiale, par exemple, la création d'une table séparée et le déplacement de ces données là-bas peut être votre choix. Cependant, le groupe de fichiers de cette table doit rester à part de la base de données principale et être déplacé vers un disque séparé chaque fois que possible.

Très probablement, vous voudrez permettre aux utilisateurs d'accéder aux données que vous envoyez à une table séparée. Pour que cela se produise, vous pouvez créer une vue fusionnant les tables pertinentes et rediriger les requêtes vers cette vue, et non vers la table d'origine. En faisant les choses de cette manière, vous pouvez garder les données accessibles tout en traitant la maintenance plus rapidement.

### Liaison de serveur SQL

Si vous ne pouvez pas déplacer les données vers une autre base de données pour des raisons internes telles que des politiques de sauvegarde Azure spéciales, vous pouvez envisager de maintenir votre base de données principale en conséquence.

Ici, le résultat est probablement celui du cas précédent, mais vous devez lier les serveurs SQL ou configurer les applications pour qu'elles puissent envoyer des requêtes directes à votre deuxième serveur.

L'inconvénient ici est que votre base de données SQL, qui était censée être une sauvegarde, devient une base de données de production et gagne une importance appropriée pour une organisation.

Il existe deux façons de créer des serveurs liés via SQL Server Management Studio (SSMS) :

* **sp_addlinkedserver** (Transact-SQL) procédure stockée système qui crée un serveur lié
* **Interface graphique SSMS**

Après vous être assuré que vous avez les droits d'accès appropriés sur les deux instances de serveur que vous devez lier, que le réseau est configuré de manière appropriée pour y accéder, et que SSMS est installé, vous devrez suivre les étapes suivantes :

Tout d'abord, ouvrez SSMS.

![Image](https://lh7-us.googleusercontent.com/6NS8wE2UmtV5Bs3-loE7kIASfehk4-hSaPP5y7Wm1oEVIUFDCPyxD_f1rLQzxsJVdCGaFJwcRHqKVrnypgETOSohLP5hQK50m4tj4pBZBIx6oTUj8WOJbcttfhy0IybUyC_CrJCyK8saEPnchKInp7g)
_Microsoft SSMS_

Connectez-vous à l'instance où vous devez établir un serveur lié. Ensuite, trouvez **Explorateur d'objets > Objets de serveur**, puis faites un clic droit sur **Serveurs liés**.

Choisissez **Nouveau serveur lié** dans le menu déroulant :

![Image](https://lh7-us.googleusercontent.com/tD5YO2e1RtfLUmtBdRFNfiHQSyaxnQml9lBGnRPPzuNrW4Fcu-3alTg4N3-mdR-oQxcaUyMpyqp36l7r3aTfg29RzT6Jgx0Nb1eT2T-y-zotl1RujRUIC4gSwE25aslpfMJJUvNW4MMivP4BstyQu4o)
_Nouveau serveur lié SSMS_

Ensuite, configurez les propriétés du serveur, y compris le nom, le type de serveur, le fournisseur et le nom du produit :

![Image](https://lh7-us.googleusercontent.com/y-WSzJni8uyKBAcJywPqk-iufIeJ_4TTs1rf3e_9RYhj1Kt8nUsZfad9Vekec4yL6eFCX8doLR4Qr7iA6X3p78jnRfIs3AYlHMn1GOhR8Ya29CW5X9DIU-nbj_jDaTwAvwEJXNjr7npd5THmnD7Iv3A)
_Configuration du serveur lié SSMS_

Ensuite, vous devrez simplement compléter la configuration de sécurité, configurer les options du serveur et terminer le test de connexion.

### Suppression des données originales

Lorsque vous n'avez pas besoin d'une disponibilité des données 24h/24 et 7j/7, mais que vous devez stocker les données en raison de politiques internes ou d'exigences de conformité, vous pouvez choisir ce qui est probablement la solution la plus simple pour augmenter l'efficacité de l'espace de stockage. Il suffit de sauvegarder les données qui peuvent rester indisponibles, puis de supprimer les originales de la base de données principale. L'accès à tous les enregistrements dont vous pourriez avoir besoin sera toujours possible via la sauvegarde.

### Stretch Database

Dans le but de simplifier la gestion des données des bases de données des organisations, Microsoft a implémenté une fonctionnalité Stretch Database dans SQL Server 2016. Avec cette fonctionnalité, vous pouvez obtenir une sauvegarde SQL vers Azure après avoir envoyé les données de la base de données hébergée vers une base de données SQL Azure. La méthode vous permet d'augmenter l'efficacité globale des coûts de l'infrastructure en simplifiant les flux de travail de sauvegarde.

Pour activer ce flux de travail dans votre environnement, développez la politique spécifiant les données sur un serveur hébergé à envoyer vers Azure. Vous n'avez pas besoin d'introduire de changements dans les applications qui utilisent la base de données de production : SQL Server peut indépendamment obtenir les enregistrements de la base de données SQL Azure.

### Vérification et restauration des sauvegardes de bases de données Azure

Lors d'une sauvegarde de base de données SQL Azure, vous pouvez choisir de créer de telles sauvegardes **AVEC CHECKSUMS** ou sans eux. Lorsque le flux de travail est terminé, je vous recommande d'utiliser la commande suivante : **`RESTORE VERIFYONLY`**. Cette commande vous permet de vérifier la récupérabilité des fichiers de sauvegarde.

Pour accéder aux données, vous pouvez restaurer les enregistrements d'une sauvegarde vers une autre base de données. Avec les scripts d'automatisation Azure sur les sauvegardes, vous pouvez accélérer le processus de restauration, minimisant ainsi le temps d'arrêt et augmentant la résilience globale de votre infrastructure Azure.

Vous devez suivre seulement quelques étapes pour restaurer une base de données SQL Azure à un point de récupération requis à partir d'une sauvegarde. Cependant, gardez à l'esprit que votre abonnement peut définir la période de rétention disponible qui peut varier de 7 à 35 jours. Un outil natif pour la restauration de sauvegardes vers les serveurs SQL est Server Management Studio.

## Conclusion

La nature critique des données de la base de données Azure SQL rend les sauvegardes Azure SQL obligatoires pour toute organisation utilisant cette solution Microsoft. Dans ce guide, nous avons passé en revue le processus de création de sauvegardes de bases de données SQL Azure en utilisant les outils natifs de Microsoft.

Ces outils fournissent des fonctionnalités de sauvegarde de données, de vérification de sauvegarde et de récupération, ainsi que certaines automatisations.

Vous pouvez également implémenter une solution de protection de données tout-en-un spécialisée, telle que [NAKIVO](https://www.nakivo.com/backup-to-azure-blob/), l'entreprise où je travaille. Elle peut vous aider à rendre vos flux de travail de sauvegarde de données plus efficaces.