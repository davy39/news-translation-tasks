---
title: Comment connecter votre conteneur Docker Microsoft SQL Server avec Azure Data
  Studio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T11:22:53.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-connect-your-microsoft-sql-server-docker-container-with-azure-data-studio
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-29-at-3.52.47-AM.png
tags:
- name: mssql
  slug: mssql-3
- name: database
  slug: database
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
- name: SQL
  slug: sql
seo_title: Comment connecter votre conteneur Docker Microsoft SQL Server avec Azure
  Data Studio
seo_desc: "By Clark Jason Ngo\nThis guide shows you how to use Docker to pull a MSSQL\
  \ Server image and run it. Azure Data Studio is a cross-platform database tool that\
  \ will be using to connect our Docker container with MSSQL and execute SQL statements.\
  \ \nAt the e..."
---

Par Clark Jason Ngo

Ce guide vous montre comment utiliser Docker pour télécharger une image de serveur MSSQL et l'exécuter. Azure Data Studio est un outil de base de données multiplateforme qui sera utilisé pour connecter notre conteneur Docker avec MSSQL et exécuter des instructions SQL.

À la fin, je vous montrerai comment importer une base de données dans le système de fichiers Docker afin que vous puissiez y accéder via Azure Data Studio.

Consultez d'autres guides connexes ici :

* _[Comment connecter votre AWS RDS Microsoft SQL Server en utilisant Azure Data Studio](https://www.freecodecamp.org/news/cjn-how-to-connect-your-aws-rds-microsoft-sql-server-using-azure-data-studio/)_
* [_Comment importer une base de données d'exemple dans votre AWS RDS Microsoft SQL Server en utilisant S3_](https://www.freecodecamp.org/news/cjn-how-to-import-a-sample-database-to-your-aws-rds-microsoft-sql-server-using-s3/)

Nous allons aborder les technologies présentées ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-238.png)

* Base de données : Microsoft SQL Server
* Conteneur pour télécharger mssql-server-demo : Docker
* Installeur pour mssql-cli : Node.js (Environnement d'exécution) / Node Package Manager (NPM)
* Outil de base de données et GUI : Azure Data Studio

## Construction de notre environnement avec Docker

### Installation de Docker

Guide complet pour cette partie [ici](https://database.guide/how-to-install-sql-server-on-a-mac/) :

1. Téléchargez Docker CE (Community Edition) pour Mac [ici](https://store.docker.com/editions/community/docker-ce-desktop-mac?tab=description).
2. Pour installer, double-cliquez sur le fichier .dmg puis faites glisser l'icône de l'application Docker vers votre dossier Applications.

#### Qu'est-ce que Docker ?

Docker est une plateforme qui permet aux logiciels de s'exécuter dans leur propre environnement isolé. SQL Server (à partir de 2017) peut être exécuté sur Docker dans son propre conteneur isolé.

Une fois Docker installé, vous téléchargez simplement — ou « pull » — l'image Docker de SQL Server sur Linux sur votre Mac, puis vous l'exécutez en tant que conteneur Docker. Ce conteneur est un environnement isolé qui contient tout ce dont SQL Server a besoin pour fonctionner.

### Lancer Docker

Ouvrez votre application Docker, elle devrait se trouver dans le dossier Applications.

### Augmenter la mémoire

Par défaut, Docker aura 2 Go de mémoire alloués. SQL Server a besoin d'au moins 3,25 Go. Pour plus de sécurité, augmentez à 4 Go si possible. Comme il s'agit simplement d'un bac à sable, 2 Go devraient suffire.

### Optionnel - au cas où vous souhaitez augmenter la taille de la mémoire :

1. Sélectionnez Préférences à partir de la petite icône Docker dans le menu supérieur
2. Faites glisser le curseur de mémoire jusqu'à au moins 2 Go
3. Cliquez sur Appliquer et redémarrer

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-245.png)

![Image](cid:E87AD92D-0D8E-48A7-BE61-59CD6832E27F@hsd1.wa.comcast.net.)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-246.png)



### Télécharger SQL Server

Ouvrez une fenêtre de terminal et exécutez la commande suivante.

```terminal
sudo docker pull mcr.microsoft.com/mssql/server:2019-latest
```

Cela télécharge la dernière version de SQL Server 2019 pour l'image Docker Linux sur votre ordinateur.

Vous pouvez également vérifier la [dernière version du conteneur](https://hub.docker.com/_/microsoft-mssql-server) sur le site web de Docker si vous le souhaitez.

### Lancer l'image Docker

Exécutez la commande suivante pour lancer une instance de l'image Docker que vous venez de télécharger :

```terminal
docker run -d --name sql_server_demo -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=really
```

Exemple de sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-254.png)

### Vérifier le conteneur Docker (optionnel)

Vous pouvez taper la commande suivante pour vérifier que le conteneur Docker est en cours d'exécution.

```terminal
docker ps
```

S'il est en cours d'exécution, il devrait retourner quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-247.png)

Si vous avez accidentellement fermé votre application Docker, ouvrez votre terminal et tapez

```terminal
docker start sql_server_demo
```

### Installer Node.js et NPM

Vérifiez si vous avez Node.js et NPM. Exécutez les commandes suivantes dans votre terminal.

```terminal
node -v
npm -v
```

Si vous obtenez une sortie avec un numéro de version, passez le reste de cette section.

Visitez ensuite le site web de Node.js en cliquant sur le lien suivant :

[https://nodejs.org/en/](https://nodejs.org/en/)

Cliquez sur le bouton de téléchargement de la version LTS (le numéro de version peut varier) pour télécharger le package Node.js :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-249.png)

Ensuite, cliquez et exécutez le package après l'avoir téléchargé. macOS et Windows auront des processus d'installation différents. Veuillez suivre les instructions pour installer Node.js.

Testez à nouveau si Node.js et NPM ont été installés avec succès en exécutant les commandes suivantes dans le terminal :

```terminal
node -v
npm -v
```

Une sortie devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-248.png)

#### 

### Installer sql-cli

Exécutez la commande suivante pour installer l'outil de ligne de commande sql-cli. Cet outil vous permet d'exécuter des requêtes et d'autres commandes contre votre instance SQL Server.

```terminal
npm install -g sql-cli
```

Si vous obtenez une erreur de permission, utilisez la commande `sudo` :

```terminal
sudo npm install -g sql-cli
```

### 

## Connexion à MSSQL Server

Connectez-vous à votre SQL Server en utilisant la commande mssql, suivie des paramètres de nom d'utilisateur et de mot de passe. Syntaxe : -u <nom d'utilisateur> -p <mot de passe>

```terminal
mssql -u sa -p reallyStrongPwd123
```

Votre sortie devrait ressembler à ceci si vous êtes connecté avec succès :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-250.png)

### Exécuter un test rapide

Exécutez un test rapide pour vérifier si vous pouvez vous connecter à votre SQL Server. Utilisez l'instruction SQL suivante pour vérifier la version de votre SQL Server :

```sql
SELECT @@VERSION;
```

S'il est en cours d'exécution, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-251.png)

## Télécharger un GUI SQL Server - Azure Data Studio

[Azure Data Studio](https://database.guide/what-is-azure-data-studio/) (anciennement SQL Operations Studio) est un outil de gestion GUI gratuit que vous pouvez utiliser pour gérer SQL Server sur votre ordinateur. Vous pouvez l'utiliser pour créer et gérer des bases de données, écrire des requêtes, sauvegarder et restaurer des bases de données, et plus encore.

Azure Data Studio est disponible sur Windows, Mac et Linux.

### Installer Azure Data Studio

Pour installer Azure Data Studio sur votre Mac :

1. Visitez la [page de téléchargement d'Azure Data Studio](https://docs.microsoft.com/en-us/sql/azure-data-studio/download), et cliquez sur le fichier .zip pour macOS
2. Une fois le fichier .zip téléchargé, double-cliquez dessus pour en extraire le contenu
3. Faites glisser le fichier .app vers le dossier Applications (le fichier s'appellera probablement _Azure Data Studio.app_)

### Connexion à SQL Server

Maintenant qu'Azure Data Studio est installé, vous pouvez l'utiliser pour vous connecter à SQL Server.

1. Lancez Azure Data Studio. Il se trouve dans votre dossier Applications.
2. Entrez les informations d'identification de connexion et autres informations pour l'instance SQL Server à laquelle vous souhaitez vous connecter :

Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-259.png)

Cela devrait ressembler à ceci :

* **Nom du serveur** : localhost, [numéro de port]   
**Exemple** : localhost, 1433
* **Type d'authentification** : Connexion SQL
* **Nom d'utilisateur** : [votre nom d'utilisateur SQL Server] ou sa
* **Mot de passe** : [votre mot de passe SQL Server] ou reallyStrongPwd123
* **Nom de la base de données** : <par défaut>
* **Groupe de serveurs** : <par défaut>

Si vous utilisez un port autre que le port par défaut 1433, cliquez sur Avancé et entrez-le dans le champ Port.

Alternativement, vous pouvez l'ajouter à votre nom de serveur avec une virgule entre les deux. Par exemple, si vous avez utilisé le port 1400, tapez localhost,1400.

Vous pouvez maintenant créer des bases de données, exécuter des scripts et effectuer d'autres tâches de gestion SQL Server.

1. Cliquez sur **Nouvelle requête**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-253.png)

2.     Tapez **SELECT @@VERSION**, puis cliquez sur **Exécuter la requête**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-241.png)



Vous devriez pouvoir voir : _Microsoft SQL Server_ dans les Résultats.

## Importer une base de données d'exemple dans votre SQL Server en utilisant Azure Data Studio

### Télécharger le fichier de base de données d'exemple AdventureWorks

Pour obtenir les téléchargements OLTP d'AdventureWorks, allez à ce [lien](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15) et choisissez n'importe quelle base de données d'exemple. Dans mon exemple, je choisis `AdventureWorks2017.bak`. Nous allons télécharger cela vers le bucket S3.

### Copier le fichier vers votre docker

Tapez la commande suivante dans le terminal en suivant cette syntaxe :

```
docker cp <emplacement_du_fichier> <id_conteneur>:/var/opt/mssql/data
```

Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-255.png)

Si vous avez oublié votre identifiant de conteneur, utilisez la commande `docker ps`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-258.png)

### Importer la base de données d'exemple dans Docker

Allez dans Azure Data Studio, et cliquez sur **localhost, 1443**, puis choisissez **Restaurer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-265.png)

Choisissez ensuite **Fichier de sauvegarde** comme sélection pour _Restaurer à partir de_. Ensuite, cliquez sur le bouton bleu à droite de _Chemin du fichier de sauvegarde_.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-264.png)

Recherchez le fichier de base de données d'exemple. Il devrait se trouver dans

```terminal
/var/opt/mssql/data/AdventureWorks2017.bak
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-260.png)

Choisissez **Restaurer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-263.png)

Vérifiez votre localhost, 1443. Il devrait générer une base de données nommée AdventureWorks2017 et contenir des éléments tels que des tables et des vues. Si ce n'est pas le cas, faites un clic droit sur localhost, 1443 et choisissez Actualiser. Vous pouvez également redémarrer votre application Azure Data Studio.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-262.png)

### Tester la base de données d'exemple

1. Choisissez **AdventureWorks2017** dans le menu déroulant.
2. Écrivez une requête SQL :

```sql
SELECT * FROM HumanResources.Department;
```

3.   Cliquez sur **Exécuter** pour exécuter la requête.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-266.png)

Vous devriez obtenir une sortie comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-267.png)

Félicitations ! 🎉

Ressources :

* [Comment installer SQL Server sur un Mac](https://database.guide/how-to-install-sql-server-on-a-mac/)

Connectez-vous avec moi sur LinkedIn [ici](https://www.linkedin.com/in/clarkngo/)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-240.png)