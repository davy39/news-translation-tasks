---
title: Comment sauvegarder votre base de données MySQL de manière programmatique avec
  mysql-backup4j
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T05:01:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-backup-mysql-database-programmatically-using-mysql-backup4j-2b53a1cbf9b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2l8ivsdetW149P5ZT2rUEQ.jpeg
tags:
- name: database
  slug: database
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment sauvegarder votre base de données MySQL de manière programmatique
  avec mysql-backup4j
seo_desc: 'By Seun Matt

  In this article, we’re going to be looking at mysql-backup4j, a very flexible Java
  library that we can use to back-up our database periodically.

  Once our app is in production, we can’t afford to not have a timely backup in case
  of eventu...'
---

Par Seun Matt

Dans cet article, nous allons examiner [mysql-backup4j](https://github.com/SeunMatt/mysql-backup4j), une bibliothèque Java très flexible que nous pouvons utiliser pour sauvegarder notre base de données périodiquement.

Une fois notre application en production, nous ne pouvons pas nous permettre de ne pas avoir une sauvegarde à jour en cas d'éventualités. Habituellement, ce qui rend le processus quelque peu ardu, c'est si nous devons déclencher manuellement le processus tout le temps.

Imaginez un scénario dans lequel nous avons à la fois des processus automatisés et manuels de sauvegarde de la base de données — c'est ce que nous allons faire.

### 2. Installation de la dépendance

Ajoutons la dépendance à notre projet dans le fichier _pom.xml_ :

```
<dependency>   <groupId>com.smattme</groupId>   <artifactId>mysql-backup4j</artifactId>   <version>1.0.1</version></dependency>
```

La dernière version peut être trouvée [ici](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22com.smattme%22%20a%3A%22mysql-backup4j%22).

### 3. Exportation de la base de données MySQL de manière programmatique

Exporter une base de données MySQL de manière programmatique est très simple avec mysql-backup4j. Nous devons simplement l'instancier et lui passer un objet Java _Properties_ qui a les bonnes propriétés de configuration définies :

```
// propriétés requises pour l'exportation de la base de données Properties properties = new Properties(); properties.setProperty(MysqlExportService.DB_NAME, "nom-de-la-base-de-données"); properties.setProperty(MysqlExportService.DB_USERNAME, "root"); properties.setProperty(MysqlExportService.DB_PASSWORD, "root"); 
```

```
// propriétés relatives à la configuration email properties.setProperty(MysqlExportService.EMAIL_HOST, "smtp.mailtrap.io"); properties.setProperty(MysqlExportService.EMAIL_PORT, "25"); properties.setProperty(MysqlExportService.EMAIL_USERNAME, "nom-d-utilisateur-mailtrap"); properties.setProperty(MysqlExportService.EMAIL_PASSWORD, "mot-de-passe-mailtrap"); properties.setProperty(MysqlExportService.EMAIL_FROM, "test@smattme.com"); properties.setProperty(MysqlExportService.EMAIL_TO, "backup@smattme.com"); 
```

```
// définir le répertoire temporaire de sortie properties.setProperty(MysqlExportService.TEMP_DIR, new File("external").getPath()); 
```

```
MysqlExportService mysqlExportService = new MysqlExportService(properties); mysqlExportService.export();
```

Dans l'extrait ci-dessus, nous avons créé un nouvel objet _Properties_ puis ajouté les propriétés requises pour la connexion à la base de données, qui sont : le nom de la base de données, le nom d'utilisateur et le mot de passe.

**Fournir uniquement ces propriétés fera en sorte que _mysql-backup4j_ suppose que la base de données s'exécute sur _localhost_ au port _3306_.** Il tentera donc de se connecter en utilisant ces valeurs ainsi que le nom d'utilisateur et le mot de passe fournis.

À ce stade, la bibliothèque peut exporter notre base de données et générer un fichier zip contenant le fichier de vidage SQL. Le fichier est nommé selon le format :

```
chainealeatoire_jour_mois_annee_heure_minute_seconde_nom-de-la-base-de-données_dump.zip
```

Puisque nous avons fourni des identifiants de messagerie complets dans le cadre des propriétés utilisées pour le configurer, le vidage de la base de données zippé sera envoyé par e-mail à l'adresse configurée. **Si aucune configuration de messagerie n'est définie, alors rien ne se passe après la sauvegarde.**

Une autre configuration importante que nous avons définie est le _TEMP_DIR_ ; il s'agit du répertoire qui sera utilisé par la bibliothèque pour stocker temporairement les fichiers générés pendant le traitement. **Ce _dir_ doit être accessible en écriture par le programme en cours d'exécution.**

Le _TEMP_DIR_ sera automatiquement supprimé une fois l'opération de sauvegarde terminée. Simple et efficace, n'est-ce pas ? Oui.

### 4. Envoyer le fichier zippé généré vers n'importe quel stockage cloud

Bien que la bibliothèque puisse envoyer la sauvegarde à une adresse e-mail préconfigurée, elle fournit également un moyen pour nous d'obtenir le fichier généré en tant qu'objet Java _File_ afin que nous puissions en faire ce que nous voulons.

Pour y parvenir, nous devons ajouter cette propriété de configuration :

```
//... properties.setProperty(MysqlExportService.PRESERVE_GENERATED_ZIP, "true");
```

Cette propriété indique à _mysql-backup4j_ de conserver le fichier zip généré afin que nous puissions y accéder :

```
File file = mysqlExportService.getGeneratedZipFile();
```

Maintenant que nous avons un objet fichier, nous pouvons le télécharger vers n'importe quel stockage cloud de notre choix en utilisant les SDK et bibliothèques appropriés.

**Une fois que nous avons terminé, nous devons manuellement supprimer le fichier zip du _TEMP_DIR_ en appelant :**

```
mysqlExportService.clearTempFiles(false);
```

Cet aspect est très important afin que nous n'ayons pas de fichiers redondants dans notre stockage local. Si nous voulons obtenir le vidage SQL exporté brut en tant que chaîne, nous devons simplement appeler cette méthode :

```
String generatedSql = mysqlExportService.getGeneratedSql();
```

J'aime la flexibilité de cette bibliothèque. D'autres propriétés qui peuvent être définies sont :

```
properties.setProperty(MysqlExportService.DELETE_EXISTING_DATA, "true"); properties.setProperty(MysqlExportService.DROP_TABLES, "true"); properties.setProperty(MysqlExportService.ADD_IF_NOT_EXISTS, "true"); properties.setProperty(MysqlExportService.JDBC_DRIVER_NAME, "root.ss"); properties.setProperty(MysqlExportService.JDBC_CONNECTION_STRING, "jdbc:mysql://localhost:3306/nom-de-la-base-de-données");
```

_DELETE_EXISTING_DATA_ ajoutera une instruction SQL _DELETE * FROM table_ avant une instruction SQL _INSERT INTO table_.

_DROP_TABLES_ ajoutera une instruction SQL _DROP TABLE IF EXISTS_ avant l'instruction _CREATE TABLE IF NOT EXISTS_.

_ADD_IF_NOT_EXISTS_, qui est par défaut _true_, ajoutera une clause _IF NOT EXISTS_ aux instructions _CREATE TABLE_.

Nous pouvons également spécifier le _JDBC_DRIVER_NAME_ et le _JDBC_CONNECTION_STRING_ via les propriétés.

Si notre base de données se trouve sur un autre hôte ou port que _localhost:3306_, nous pouvons utiliser la propriété JDBC_CONNECTION_STRING pour configurer la connexion. Le DB_NAME sera extrait de la chaîne de connexion fournie.

**Nous pouvons automatiser ce processus en utilisant des planificateurs de tâches Java comme [quartz](http://www.quartz-scheduler.org/)** ou d'autres moyens. De plus, dans une application web typique, nous pouvons simplement créer un chemin pour cela qui déclenchera le processus de sauvegarde dans un _Service_ ou un _Controller_.

Nous pouvons même l'intégrer dans une application web de sorte que la sauvegarde sera déclenchée lorsque la base de données aura une mise à jour significative des enregistrements. Les possibilités sont limitées uniquement par notre créativité.

### 5. Importation du vidage de la base de données

Oui ! Nous avons réussi à sauvegarder notre base de données et à la verrouiller dans un coffre-fort sécurisé. Mais comment importer la base de données et effectuer une restauration ?

Tout d'abord, nous devons décompresser le fichier zip généré et extraire le vidage SQL dans un dossier. Ensuite, nous pouvons utiliser des clients de base de données comme [HeidiSQL](https://www.heidisql.com/) et [Adminer](https://www.adminer.org/) pour importer la base de données. L'utilisation d'un client de gestion de base de données fournira une aide visuelle et d'autres outils intéressants qui l'accompagnent.

Cependant, supposons que nous nous trouvions dans le besoin de restaurer la base de données de manière programmatique, au sein de l'application, alors qu'elle est encore en cours d'exécution.

Tout ce que nous devons faire est de lire le contenu du vidage SQL généré en tant que chaîne et de le passer au _MySqlImportService_ de la bibliothèque avec des configurations minimales :

```
String sql = new String(Files.readAllBytes(Paths.get("chemin/vers/fichier/sql/dump/file.sql")));
```

```
boolean res = MysqlImportService.builder() .setDatabase("nom-de-la-base-de-données") .setSqlString(sql).setUsername("root") .setPassword("root") .setDeleteExisting(true).setDropExisting(true) .importDatabase(); 
```

```
assertTrue(res);
```

Dans l'extrait ci-dessus, nous avons lu le SQL à partir d'un système de fichiers, puis nous avons utilisé le _MySqlImportService_ pour effectuer l'opération d'importation.

Nous avons configuré _MySqlImportService_ pour supprimer tout contenu existant dans la table et pour supprimer les tables existantes. Nous pouvons toujours ajuster ces paramètres pour répondre à nos besoins. Le service retournera true en cas d'opération réussie ou false sinon.

Et si notre base de données s'exécute sur un autre serveur et port que localhost:3306 ? Nous pouvons configurer cela également en utilisant la méthode _setJdbcConnString()_.

Bien que nous ayons lu le fichier SQL à partir d'un système de fichiers local, si nous sommes dans une interface web, nous pouvons en fait fournir une interface qui permettra de sélectionner le fichier à partir du système de fichiers. Ensuite, le contenu peut être lu et envoyé en tant que requête HTTP POST au serveur.

### 6. Conclusion

Ouf ! Voici un outil de productivité que nous venons d'examiner. N'oubliez pas de mettre une étoile à mysql-backup4j sur [Github](https://github.com/SeunMatt/mysql-backup4j) si vous l'avez aimé.

Maintenant, allez l'utiliser dans votre projet. Des questions ? Des contributions ? De l'appréciation ? N'hésitez pas à les laisser dans la section des commentaires ci-dessous.

**Lisez mes autres articles techniques et mes vues sur la vie sur [https://smattme.com](https://smattme.com)**

> _Si vous trouvez cet article utile, si vous avez appris quelque chose, applaudissez l'article et partagez-le avec vos amis sur Facebook et Twitter. Soyez fier du contenu de qualité que vous lisez._

_Publié à l'origine sur [smattme.com](https://smattme.com/blog/technology/how-to-backup-mysql-database-programmatically-using-mysql-backup4j)._