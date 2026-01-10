---
title: Comment se connecter à votre AWS RDS Microsoft SQL Server en utilisant Azure
  Data Studio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T09:41:13.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-connect-your-aws-rds-microsoft-sql-server-using-azure-data-studio
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-29-at-2.36.26-AM.png
tags:
- name: AWS
  slug: aws
- name: Azure
  slug: azure
- name: database
  slug: database
- name: MSSQL
  slug: mssql
- name: SQL
  slug: sql
seo_title: Comment se connecter à votre AWS RDS Microsoft SQL Server en utilisant
  Azure Data Studio
seo_desc: "By Clark Jason Ngo\nThe goal of this guide is to play around with cloud\
  \ databases and connect one to a database tool. Once you are done with this guide,\
  \ you should be able to create databases and tables, and more. \nImporting a sample\
  \ database is a pai..."
---

Par Clark Jason Ngo

Le but de ce guide est de manipuler des bases de données cloud et de connecter l'une d'elles à un outil de base de données. Une fois ce guide terminé, vous devriez être en mesure de créer des bases de données et des tables, et bien plus encore. 

Importer une base de données d'exemple est fastidieux, voici donc un autre guide que j'ai créé : [_Comment importer une base de données d'exemple vers votre AWS RDS Microsoft SQL Server en utilisant S3_](https://www.freecodecamp.org/news/cjn-how-to-import-a-sample-database-to-your-aws-rds-microsoft-sql-server-using-s3/).

Heureusement, comme j'étais nouveau dans ce domaine, j'ai également découvert comment connecter un serveur MSSQL avec Docker à Azure Data Studio. Consultez ce guide : [_Comment connecter votre AWS RDS Microsoft SQL Server en utilisant Azure Data Studio_](https://www.freecodecamp.org/news/cjn-how-to-connect-your-microsoft-sql-server-docker-container-with-azure-data-studio/).

Nous allons aborder les technologies présentées ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-242.png)

* Base de données : Amazon Relational RDS avec MSSQL Server Express Edition
* Outil de base de données et GUI : Azure Data Studio

## Création et configuration de votre instance AWS RDS MSSQL Server

### Connectez-vous à AWS.com :

1. Allez sur [https://aws.amazon.com/console/](https://aws.amazon.com/console/)
2. Cliquez sur **Se connecter à votre compte AWS**

### Créer une instance de base de données Microsoft SQL Server :

1. Dans la section Créer une base de données, choisissez **Créer une base de données**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-213.png)

2.   Choisissez **Création facile** pour la méthode de création de la base de données.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-216.png)

3.   Choisissez l'icône **Microsoft SQL Server** pour le type de moteur.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-217.png)

4.   Sélectionnez **Niveau gratuit** pour la taille de l'instance de base de données.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-218.png)

5.   Remplissez les détails suivants pour l'identifiant de l'instance de base de données :

* **Identifiant de l'instance de base de données** : myrdstest.
* **Nom d'utilisateur principal** : Tapez un nom d'utilisateur
* **Mot de passe principal** : Tapez un mot de passe contenant de 8 à 41 caractères imprimables.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-221.png)

6.   Sélectionnez **Créer une base de données**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-220.png)

Note : Cela peut prendre quelques minutes pour le provisionnement

Si vous quittez accidentellement la page, vous devriez voir votre base de données **myrdstest** sous **RDS** > **Bases de données**.

Pour un tutoriel plus détaillé, suivez les étapes dans la [documentation AWS](https://aws.amazon.com/getting-started/tutorials/create-microsoft-sql-db/).

### Autoriser l'accès public à votre instance RDS

1. Cliquez sur **Modifier**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-223.png)

2.   Choisissez **Oui** dans Accessibilité publique sous Réseau et sécurité.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-224.png)

3.  Choisissez **Appliquer immédiatement** sous Planification des modifications, puis cliquez sur **Modifier l'instance de base de données**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-225.png)

### Autoriser les règles entrantes

1. Cliquez sur **default (sg-0000d009)** sous les groupes de sécurité VPC.

Note : le numéro est différent dans votre propre instance.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-226.png)

2.   Cliquez sur **Entrant**, puis cliquez sur **Modifier les règles entrantes**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-228.png)

3.  Choisissez **Mon IP** dans Source, puis cliquez sur **Enregistrer les règles**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-227.png)

## Tester votre connexion à AWS RDS

Ouvrez votre terminal (MacOS) et tapez ce qui suit : **nc -zv _aws_rds_endpoint port_number_**

Exemple de connexion réussie :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-229.png)

Exemple de connexion échouée :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-230.png)

Assurez-vous que votre instance RDS est publique et que les règles entrantes autorisent votre IP.

## Télécharger un GUI SQL Server - Azure Data Studio

[Azure Data Studio](https://database.guide/what-is-azure-data-studio/) (anciennement SQL Operations Studio) est un outil de gestion GUI gratuit que vous pouvez utiliser pour gérer SQL Server. Vous pouvez l'utiliser pour créer et gérer des bases de données, écrire des requêtes, sauvegarder et restaurer des bases de données, et bien plus encore.

Azure Data Studio est disponible sur Windows, Mac et Linux.

### Installer Azure Data Studio

Pour installer Azure Data Studio sur un Mac :

1. Visitez la [page de téléchargement d'Azure Data Studio](https://docs.microsoft.com/en-us/sql/azure-data-studio/download), et cliquez sur le fichier .zip pour macOS
2. Une fois le téléchargement du fichier .zip terminé, double-cliquez dessus pour extraire son contenu
3. Faites glisser le fichier .app vers le dossier Applications.

### Se connecter à SQL Server

Maintenant qu'Azure Data Studio est installé, vous pouvez l'utiliser pour vous connecter à SQL Server :

1. Lancez Azure Data Studio. Il se trouve dans votre dossier Applications.
2. Entrez les informations d'identification de connexion et autres informations pour l'instance SQL Server à laquelle vous souhaitez vous connecter :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-231.png)

Cela devrait ressembler à ceci :

* **Nom du serveur** : [Point de terminaison AWS RDS], [numéro de port]   
**Exemple** : myrdstest.blahblahblah.us-west-2/ds.amazonaws.com, 1433
* **Type d'authentification** : Connexion SQL
* **Nom d'utilisateur** : [votre nom d'utilisateur AWS]
* **Mot de passe** : [votre mot de passe AWS]
* **Nom de la base de données** : <par défaut>
* **Groupe de serveurs** : <par défaut>

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-232.png)

Si vous avez utilisé un port autre que le port par défaut 1433, cliquez sur **Avancé** et entrez-le dans le champ Port.

Alternativement, vous pouvez l'ajouter à votre nom de serveur avec une virgule entre les deux. Par exemple, si vous avez utilisé le port 1400, tapez localhost,1400.

Si vous obtenez une erreur :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-233.png)

Assurez-vous que votre instance RDS est publique et que les règles entrantes autorisent votre IP.

Vous pouvez maintenant créer des bases de données, exécuter des scripts et effectuer d'autres tâches de gestion SQL Server.

1. Cliquez sur **Nouvelle requête**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-234.png)

2.   Tapez **SELECT @@VERSION**, puis cliquez sur **Exécuter la requête**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-235.png)



Vous devriez pouvoir voir : _Microsoft SQL Server_ dans les Résultats

Félicitations ! ???

## Ressources :

* [Comment créer une base de données Microsoft SQL](https://aws.amazon.com/getting-started/tutorials/create-microsoft-sql-db/)

Connectez-vous avec moi sur LinkedIn [ici](https://www.linkedin.com/in/clarkngo/)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-184.png)