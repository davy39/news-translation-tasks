---
title: Comment utiliser Databricks Delta Lake avec SQL – Guide complet
subtitle: ''
author: Atharva Shah
co_authors: []
series: null
date: '2023-09-05T13:57:32.000Z'
originalURL: https://freecodecamp.org/news/databricks-sql-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Databricks-Delta-Lake-with-SQL-Handbook-Cover.png
tags:
- name: data-engineering
  slug: data-engineering
- name: Data Science
  slug: data-science
- name: handbook
  slug: handbook
- name: SQL
  slug: sql
seo_title: Comment utiliser Databricks Delta Lake avec SQL – Guide complet
seo_desc: 'Welcome to the Databricks Delta Lake with SQL Handbook! Databricks is a
  unified analytics platform that brings together data engineering, data science,
  and business analytics into a collaborative workspace.

  Delta Lake, a powerful storage layer built ...'
---

Bienvenue dans le guide Databricks Delta Lake avec SQL ! Databricks est une plateforme d'analyse unifiée qui combine l'ingénierie des données, la science des données et l'analyse métier dans un espace de travail collaboratif.

Delta Lake, une couche de stockage puissante construite sur Databricks, offre une fiabilité, des performances et une qualité de données améliorées pour les charges de travail de big data.

Ce guide de formation pratique vous permettra de plonger dans le monde de Databricks et d'apprendre à utiliser efficacement Delta Lake pour gérer et analyser des données. Il vous fournira les compétences SQL essentielles pour interagir efficacement avec les tables Delta et effectuer des analyses de données avancées.

## Prérequis

Ce guide est conçu pour les utilisateurs SQL de niveau débutant qui ont une certaine expérience avec les plateformes cloud et les clusters. Bien qu'aucune expérience préalable avec Databricks ne soit requise, il est recommandé d'avoir une compréhension de base des concepts suivants :

* **Bases de données** : La familiarité avec la structure et la fonctionnalité de base des bases de données sera utile.

* **Requêtes SQL** : La connaissance de la syntaxe SQL et la capacité à écrire des requêtes de base sont essentielles.

* **Cahiers Jupyter** : Comprendre le fonctionnement des cahiers Jupyter et être à l'aise avec l'exécution de cellules de code est recommandé.

Bien que ce guide suppose un certain niveau de familiarité avec les bases de données, SQL et les cahiers Jupyter, il vous guidera étape par étape à travers chaque processus, en veillant à ce que vous compreniez et suiviez le matériel.

Ainsi, aucune installation n'est nécessaire, car tout le travail sera effectué sur les cahiers Databricks Delta fonctionnant dans le cluster. Tout a déjà été provisionné, éliminant le besoin de toute configuration ou installation.

À la fin de ce guide, vous aurez acquis une solide base dans l'utilisation de SQL avec Databricks, vous permettant de tirer parti de ses puissantes capacités pour l'analyse et la manipulation des données.

Commençons !

## **Table des matières**

Voici les sections de ce tutoriel :

1. [Introduction à Databricks](#heading-introduction-a-databricks)

* Qu'est-ce que Databricks ?

* Fonctionnalités et avantages clés

* Prise en main de l'espace de travail Databricks

* Notions de base sur les cahiers et l'analyse interactive

2. [Introduction à Delta](#heading-introduction-a-delta)

* Comprendre Delta Lake

* Avantages de l'utilisation de Delta

* Cas d'utilisation de Delta dans des scénarios réels

* Langages et plateformes pris en charge pour Delta

3. [Comment créer et gérer des tables](#heading-comment-creer-et-gerer-des-tables)

* Création de tables à partir de diverses sources de données

* Commandes SQL Data Definition Language (DDL)

* Commandes SQL Data Manipulation Language (DML)

* Création de tables à partir d'un ensemble de données Databricks

* Enregistrement du fichier CSV chargé dans Delta en utilisant Python

4. [Prise en charge des commandes SQL Delta](#heading-prise-en-charge-des-commandes-sql-delta)

* Commandes SQL Delta pour la gestion des données

* Exécution des opérations UPSERT (UPDATE et INSERT)

5. [Requêtes SQL avancées](#heading-requetes-sql-avancees)

* Gestion de la visualisation des données dans Delta

* Requêtes d'agrégation avancées dans Delta

* Comptage des diamants par clarté en utilisant SQL

* Ajout de contraintes de table pour l'intégrité des données

6. [Comment travailler avec les DataFrames](#heading-comment-travailler-avec-les-dataframes)

* Création d'un DataFrame à partir d'un ensemble de données Databricks

* Manipulation des données et affichage des résultats en utilisant les DataFrames

7. [Contrôle de version et voyage dans le temps dans Delta](#heading-controle-de-version-et-voyage-dans-le-temps-dans-delta)

* Comprendre le contrôle de version et le voyage dans le temps dans Delta

* Restauration des données à une version spécifique

* Utilisation des champs autogénérés pour le suivi des métadonnées

8. [Clonage de table Delta](#heading-clonage-de-table-delta)

* Copie profonde et superficielle des tables Delta

* Clonage efficace des tables Delta pour l'exploration et l'analyse des données

9. [Conclusion](#heading-conclusion)

## Introduction à Databricks

Databricks est une plateforme d'analyse unifiée qui combine l'ingénierie des données, la science des données et l'apprentissage automatique dans un seul environnement collaboratif. En exploitant Apache Spark, elle traite et analyse de vastes quantités de données de manière efficace.

Databricks offre des avantages tels que la scalabilité transparente, la collaboration en temps réel et des flux de travail simplifiés, ce qui en fait un choix privilégié pour les entreprises axées sur les données.

Sa polyvalence convient à divers cas d'utilisation : des processus ETL et de préparation des données à l'analyse avancée et au développement de modèles d'IA. Databricks aide à découvrir des informations à partir de données structurées et non structurées, permettant aux entreprises de prendre des décisions éclairées rapidement.

Vous pouvez voir son application dans la finance pour la détection de fraudes, dans les soins de santé pour l'analyse prédictive, dans le commerce électronique pour les moteurs de recommandation, et ainsi de suite. En gros, Databricks accélère l'innovation basée sur les données, transformant les informations brutes en intelligence exploitable.

Pour suivre ce tutoriel, vous devez d'abord créer un [compte Community Edition](https://www.databricks.com/try-databricks) afin de pouvoir créer vos clusters.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-209.png align="left")

*Créer un compte Databricks Community Edition*

Une fois que vous avez créé votre compte, rendez-vous sur la [page de connexion de la Community Edition](https://community.cloud.databricks.com/login.html). Une fois connecté, vous serez accueilli avec un écran très similaire à celui montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-212.png align="left")

*Tableau de bord de l'utilisateur Databricks avec des options pour créer des espaces de travail, des cahiers et importer des données*

À partir de la barre latérale de gauche, vous pouvez créer vos espaces de travail, et télécharger des ensembles de données et des fichiers que vous souhaitez traiter.

Pour suivre ce tutoriel, cliquez sur le lien mis en évidence dans l'image ci-dessus (celui qui dit "créer un cahier"). Il lancera un nouveau cahier sur la plateforme Databricks où nous écrirons tout le code.

Vous pouvez également accéder à tous vos cahiers à partir de la barre latérale de gauche ou de l'onglet "Recents" sur l'écran d'accueil une fois connecté.

Vous pouvez trouver tout le code, les instructions et les étapes utilisés dans ce guide avec des explications dans l'un des cahiers publics que j'ai créés [ici](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4547302627522723/2783251604801531/8769490171999815/latest.html).

Lors de la création d'un nouveau cahier, vous devez créer un cluster pour exécuter vos commandes et traiter les données. Les clusters dans la plateforme Databricks Delta sont des groupes de ressources informatiques qui permettent un traitement efficace des données. Ils exécutent des tâches en parallèle, accélérant ainsi les tâches telles que l'ETL et l'analyse.

Les clusters offrent une allocation de ressources sur mesure, garantissant des performances et une scalabilité optimales. Prenant en charge plusieurs utilisateurs et tâches simultanément, les clusters encouragent la collaboration. En exploitant Apache Spark, ils permettent des analyses avancées et l'apprentissage automatique.

Intégrés aux transactions ACID de Databricks Delta, les clusters garantissent l'intégrité des données. Globalement, les clusters permettent une gestion des données transparente et haute performance, essentielle pour des tâches allant de la préparation des données à des analyses sophistiquées et à la formation de modèles d'IA.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-213.png align="left")

*Provisionner un cluster en créant une nouvelle ressource pour exécuter des commandes dans le cahier*

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-214.png align="left")

*Procéder avec la configuration standard*

Maintenant que nous avons le cahier et les clusters configurés, nous pouvons commencer avec le code. Mais avant cela, voici quelques termes clés à connaître. La connaissance de ces termes concerne davantage la plateforme et moins la syntaxe SQL qui sera couverte ci-dessous.

### Ingestion de données

L'ingestion de données dans Delta implique le chargement de données à partir de sources tierces, telles que Fivetran. Le support de stockage le plus efficace pour les données dans Delta est Parquet, qui est un format de stockage colonne. Pour charger des données dans Delta, nous pouvons utiliser Spark ou PySpark Python et spécifier l'emplacement de stockage. Les données chargées peuvent être consultées et interrogées en utilisant la syntaxe SQL avec la commande `COPY INTO`.

### Tableaux de bord

Les visualisations créées dans les cahiers SQL au sein de Delta peuvent être ajoutées à des tableaux de bord personnalisés pour le BI/Analytics. Ces tableaux de bord sont légers et fournissent des mises à jour en temps réel basées sur le rafraîchissement des données. Cela permet aux utilisateurs de créer des tableaux de bord perspicaces et interactifs pour l'analyse et le reporting des données. Vous n'avez pas besoin de créer vos tableaux de bord à partir de zéro. Des modèles de tableaux de bord populaires sont disponibles.

### Politiques

Delta fournit une gouvernance des données via le Unity Catalog, garantissant que les utilisateurs n'ont accès qu'aux bases de données et aux tables qu'ils sont autorisés à consulter ou à modifier. Ce contrôle granulaire sur l'accès aux données améliore la sécurité et la confidentialité des données au sein du système.

### Historique

Les modérateurs ou superutilisateurs peuvent accéder à l'historique de chaque requête exécutée contre toutes les bases de données, ainsi qu'aux horodatages et aux temps d'exécution des requêtes. Cette fonctionnalité aide à comprendre les schémas de requêtes et à optimiser les performances de la base de données en fonction des insights d'utilisation.

### Optimisation

Pour améliorer les performances des requêtes, Delta offre diverses techniques d'optimisation, telles que l'indexation des bases de données, le clustering, l'indexation des filtres Bloom et l'exploitation des paradigmes MPP comme MapReduce. La connaissance de la normalisation et de la conception de schémas contribue également à l'écriture de requêtes SQL efficaces.

### Alertes

Delta permet aux utilisateurs de définir des alertes basées sur des opérateurs de comparaison appliqués aux résultats des requêtes. Par exemple, lorsqu'une requête de comptage des ventes retourne une valeur inférieure à un seuil, une alerte peut être déclenchée via Slack, des outils de ticketing ou des e-mails. Les alertes personnalisables garantissent des notifications en temps opportun pour les événements critiques de données.

### Conception basée sur les personas

La plateforme Databricks est conçue pour répondre aux besoins de différents personas, y compris les spécialistes de la science des données/analytics et du BI/MLOps. Les utilisateurs obtiennent des interfaces segmentées adaptées à leurs rôles. Cependant, le Unity Catalog peut agréger toutes ces vues, offrant une expérience cohésive.

### Espace de travail SQL

L'espace de travail SQL dans Delta fournit une interface similaire à MySQL Workbench ou PgAdmin. Les utilisateurs peuvent effectuer des requêtes SQL sur des ensembles de données sans avoir besoin de charger les données à plusieurs reprises, comme cela se fait dans les cahiers. Cette interrogation efficace améliore l'expérience d'analyse des données basée sur SQL.

### Intégration avec d'autres outils BI

Databricks s'intègre bien avec Tableau et PowerBI. Vous pouvez importer vos points de données et visualisations de manière transparente et obtenir des résultats cohérents et synchronisés dans les outils BI de votre choix. D'un simple clic, des requêtes en direct sont générées contre les ensembles de données Databricks.

## Introduction à Delta

Delta Lake est un format de stockage ouvert utilisé pour sauvegarder vos données dans votre Lakehouse. Delta fournit une couche d'abstraction au-dessus des fichiers. C'est la fondation de stockage de votre Lakehouse.

### Pourquoi Delta Lake ?

![Image](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-logo-whitebackground.png align="left")

L'exécution d'un pipeline d'ingestion sur le stockage cloud peut être très difficile. Les équipes de données sont généralement confrontées aux défis suivants :

* Difficile d'ajouter des données (L'ajout de nouvelles données entraîne des lectures incorrectes).

* La modification des données existantes est difficile (Le RGPD/CCPA nécessite des modifications granulaires du lac de données existant).

* Les travaux échouent en cours de route (La moitié des données apparaît dans le lac de données, le reste peut être manquant).

* Problèmes de qualité des données (C'est un casse-tête constant de s'assurer que toutes les données sont correctes et de haute qualité).

* Opérations en temps réel (Le mélange du streaming et du traitement par lots entraîne une incohérence).

* Coûteux de conserver les versions historiques des données (Les environnements réglementés nécessitent la reproductibilité, l'audit et la gouvernance).

* Difficile de gérer les grandes métadonnées (Pour les grands lacs de données, les métadonnées elles-mêmes deviennent difficiles à gérer).

* Problèmes de "trop de fichiers" (Les lacs de données ne sont pas très performants pour gérer des millions de petits fichiers).

* Difficile d'obtenir de grandes performances (Le partitionnement des données pour les performances est sujet aux erreurs et difficile à changer).

Ces défis ont un impact réel sur l'efficacité et la productivité de l'équipe, passant un temps inutile à corriger des problèmes techniques de bas niveau au lieu de se concentrer sur la mise en œuvre de haut niveau et les besoins métiers.

Parce que Delta Lake résout tous les défis techniques de bas niveau liés à l'enregistrement de pétaoctets de données dans votre lakehouse, il vous permet de vous concentrer sur la mise en œuvre d'un pipeline de données simple tout en fournissant des réponses de requêtes ultra-rapides pour vos rapports BI et analytiques.

De plus, Delta Lake est un projet entièrement open source sous la Linux Foundation et est adopté par la plupart des acteurs du secteur des données. Vous savez que vous possédez vos données et que vous n'aurez pas de verrouillage par le fournisseur.

### Fonctionnalités et capacités

Vous pouvez considérer Delta comme un format de fichier que votre moteur peut exploiter pour apporter les capacités suivantes dès la sortie de la boîte :

* Transactions ACID

* Prise en charge de DELETE/UPDATE/MERGE

* Unifier le traitement par lots et le streaming

* Voyage dans le temps

* Clone sans copie

* Partitions générées

* CDF - Change Data Flow (runtime DBR)

* Requêtes ultra-rapides

Ce guide de démarrage rapide pratique va se concentrer sur :

* Chargement de bases de données et de données tabulaires à partir de diverses sources

* Écriture de requêtes DDL, DML et DTL sur ces ensembles de données

* Visualisation des ensembles de données pour obtenir des résultats concluants

* Voyage dans le temps et restauration de la base de données

* Optimisation des performances

## Comment créer et gérer des tables

D'accord, c'est l'heure de coder ! Si vous avez toujours le cahier que nous avons créé précédemment ainsi que les clusters ouverts, vous pouvez commencer par suivre le code ci-dessous. Ne vous inquiétez pas, des explications pour chaque étape suivront.

Sélectionnez le menu déroulant à côté du titre du cahier et assurez-vous que SQL est sélectionné puisque ce guide est entièrement consacré à Delta Lakes avec SQL.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-215.png align="left")

*Sélectionner le langage du cahier comme étant SQL*

### Comment créer des tables à partir d'un ensemble de données Databricks

Les cahiers Databricks sont très similaires aux cahiers Jupyter. Vous devez insérer votre code dans des cellules et les exécuter une par une ou ensemble. Tous les résultats sont affichés cellule par cellule, progressivement.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-216.png align="left")

*Interface du cahier Databricks*

Voici le code de l'image ci-dessus :

```sql
DROP TABLE IF EXISTS diamonds; 
CREATE TABLE diamonds 
USING csv 
OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header "true")
```

Dans le code ci-dessus, les deux instructions SQL (`CREATE TABLE`) sont utilisées pour créer une table nommée `diamonds` dans une base de données. La table est basée sur des données provenant d'un fichier CSV situé à l'emplacement spécifié.

Si une table avec le même nom existe déjà, l'instruction `DROP TABLE IF EXISTS diamonds` garantit qu'elle est supprimée avant d'en créer une nouvelle. La table aura le même schéma que le fichier CSV, la première ligne étant considérée comme l'en-tête contenant les noms des colonnes ("header 'true'").

Voici une commande qui retourne tous les enregistrements de la table `diamonds` :

```sql
SELECT * from diamonds
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-183.png align="left")

*La requête ci-dessus retourne tous les enregistrements de la table diamonds*

Voici une autre commande :

```sql
describe diamonds;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-184.png align="left")

*Métadonnées de la table retournées par la commande* `describe`

En SQL, l'instruction `DESCRIBE` est utilisée pour récupérer des informations de métadonnées sur la structure d'une table. La syntaxe spécifique de l'instruction `DESCRIBE` peut varier en fonction du système de base de données utilisé.

Cependant, son objectif principal est de fournir des détails sur les colonnes d'une table, tels que leurs noms, types de données, contraintes et autres propriétés.

### Enregistrement du fichier CSV chargé dans Delta en utilisant Python

La meilleure partie de l'utilisation de la plateforme Databricks est qu'elle vous permet d'écrire du Python, du SQL, du Scala et du R de manière interchangeable dans le même cahier.

Vous pouvez changer de langage à tout moment en utilisant les **"Commandes Magiques Delta"**. Vous pouvez trouver une liste complète des commandes magiques à la fin de ce guide.

```python
%python

diamonds = spark.read.csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header="true", inferSchema="true")

diamonds.write.format("delta").mode("overwrite").save("/delta/diamonds")
```

Les données sont lues à partir d'un fichier CSV situé à **/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv** dans un DataFrame Spark nommé `diamonds`. La première ligne du fichier CSV est traitée comme l'en-tête, et Spark infère le schéma pour le DataFrame en fonction des données.

Le DataFrame `diamonds` est écrit dans un format de table Delta Lake. Si la table existe déjà à l'emplacement spécifié (**/delta/diamonds**), elle sera écrasée. Si elle n'existe pas, une nouvelle table sera créée.

```sql

DROP TABLE IF EXISTS diamonds;
 
CREATE TABLE diamonds USING DELTA LOCATION '/delta/diamonds/'
```

Les instructions SQL ci-dessus suppriment toute table existante nommée `diamonds` et créent une nouvelle table Delta Lake nommée `diamonds` en utilisant les données stockées dans le format Delta Lake à l'emplacement **/delta/diamonds/**.

Vous pouvez exécuter une instruction SELECT pour vous assurer que la table apparaît comme prévu :

```sql
SELECT * from diamonds
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-185.png align="left")

*Le même jeu de résultats de la table diamonds une fois restauré à partir de Delta Lake*

## **Prise en charge des commandes SQL Delta**

Dans le monde des bases de données, il existe deux types fondamentaux de commandes : Data Manipulation Language (DML) et Data Definition Language (DDL). Ces commandes jouent un rôle crucial dans la gestion et l'organisation des données au sein d'une base de données. Dans cet article, nous allons explorer ce que sont les commandes DML et DDL, leurs différences clés, et fournir des exemples de leur utilisation.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-186.png align="left")

*Les cahiers Databricks prennent en charge toutes les commandes SQL, y compris les commandes DDL et DML mises en évidence ici*

### Data Manipulation Language (DML)

Il est utilisé pour manipuler ou modifier les données stockées dans une base de données. Ces commandes permettent aux utilisateurs d'insérer, de récupérer, de mettre à jour et de supprimer des données des tables de la base de données. Examinons de plus près certaines commandes DML couramment utilisées :

**SELECT** : La commande `SELECT` est utilisée pour récupérer des données d'une ou plusieurs tables dans une base de données. Elle vous permet de spécifier les colonnes et les lignes que vous souhaitez extraire en utilisant des conditions et des filtres. Par exemple, `SELECT * FROM Customers` récupère tous les enregistrements de la table `Customers`.

**INSERT** : La commande `INSERT` ajoute de nouvelles données dans une table. Elle vous permet de spécifier la valeur pour chaque colonne ou de sélectionner des valeurs à partir d'une autre table. Par exemple, `INSERT INTO Customers (Name, Email) VALUES ('John Doe', 'john@example.com')` ajoute un nouvel enregistrement client à la table `Customers`.

**UPDATE** : La commande `UPDATE` est utilisée pour modifier les données existantes dans une table. Elle vous permet de changer les valeurs de colonnes spécifiques en fonction de certaines conditions. Par exemple, `UPDATE Customers SET Email = 'new@example.com' WHERE ID = 1` met à jour l'adresse e-mail du client avec l'ID 1.

**DELETE** : La commande `DELETE` est utilisée pour supprimer des données d'une table. Elle vous permet de supprimer des lignes spécifiques en fonction de certaines conditions. Par exemple, `DELETE FROM Customers WHERE ID = 1` supprime l'enregistrement client avec l'ID 1 de la table `Customers`.

### Commandes Data Definition Language (DDL)

Les commandes DDL sont utilisées pour définir la structure et l'organisation d'une base de données. Ces commandes permettent aux utilisateurs de créer, modifier et supprimer des objets de base de données tels que des tables, des index et des contraintes.

Explorons quelques commandes DDL couramment utilisées :

**CREATE** : Crée un nouvel objet de base de données, tel qu'une table ou un index. Il vous permet de définir les colonnes, les types de données et les contraintes pour l'objet. Par exemple, `CREATE TABLE Customers (ID INT, Name VARCHAR(50), Email VARCHAR(100))` crée une nouvelle table nommée `Customers` avec trois colonnes.

**ALTER** : Modifie la structure d'un objet de base de données existant. Il vous permet d'ajouter, de modifier ou de supprimer des colonnes, des contraintes ou des index. Par exemple, `ALTER TABLE Customers ADD COLUMN Phone VARCHAR(20)` ajoute une nouvelle colonne nommée `Phone` à la table `Customers`.

**DROP** : Supprime un objet de base de données existant. Il supprime définitivement l'objet et ses données associées de la base de données. Par exemple, `DROP TABLE Customers` supprime la table `Customers` de la base de données.

**TRUNCATE** : La commande `TRUNCATE` est utilisée pour supprimer toutes les données d'une table, tout en conservant la structure de la table intacte. Elle est plus rapide que la commande `DELETE` lorsque vous souhaitez supprimer tous les enregistrements d'une table. Par exemple, `TRUNCATE TABLE Customers` supprime tous les enregistrements de la table `Customers`.

Delta Lake prend en charge le DML standard, y compris `UPDATE`, `DELETE` et `MERGE INTO`, offrant aux développeurs un meilleur contrôle pour gérer leurs grands ensembles de données.

Voici un exemple qui utilise les commandes `INSERT`, `UPDATE` et `SELECT` :

```sql
INSERT INTO diamonds(_c0, carat, cut,    color,    clarity,    depth,    table,    price,    x,    y,    z) values (53941, 0.22,    'Premium', 'I',    'SI2',    '60.3',    '62.1',    '334',    '3.79',    '3.75',    '2.27');
 
UPDATE diamonds SET carat = 0.20 WHERE _c0 = 53941;
 
select * from diamonds where _c0=53941;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-187.png align="left")

*Récupération d'un enregistrement unique de la table*

Dans l'exemple ci-dessus, une ligne initiale est insérée dans la table `diamonds` avec des valeurs spécifiques pour chaque colonne.

Ensuite, la valeur de carat pour la ligne avec `_c0` égal à 53941 est mise à jour à 0,20.

L'instruction `SELECT` finale récupère la ligne avec `_c0` égal à 53941, montrant son état actuel après les opérations `INSERT` et `UPDATE`. Cela montre que l'insertion de l'enregistrement a réussi.

```sql
DELETE FROM diamonds where _c0=53941;
 
select * from diamonds where _c0=53941;
```

La commande `DELETE` ci-dessus, associée à la clause `WHERE`, supprime la ligne de la base de données et la requête `SELECT` suivante valide cela en retournant un ensemble de résultats nul.

### Opération UPSERT

L'opération "upsert" met à jour si l'enregistrement existe, et insère l'enregistrement s'il n'existe pas.

```sql
CREATE TABLE  diamond__mini(_c0 int, carat double, cut string,    color string,    clarity string,    depth double, table double,    price int,    x double,    y double,    z double);
 
delete from diamond__mini;
 
INSERT INTO diamond__mini(_c0, carat, cut,    color,    clarity,    depth,    table,    price,    x,    y,    z) values (1, 0.22,    'Premium', 'I',    'SI2',    '60.3',    '62.1',    '334',    '3.79',    '3.75',    '2.27');
INSERT INTO diamond__mini(_c0, carat, cut,    color,    clarity,    depth,    table,    price,    x,    y,    z) values (2, 0.22,    'Premium', 'I',    'SI2',    '60.3',    '62.1',    '334',    '3.79',    '3.75',    '2.27');
INSERT INTO diamond__mini(_c0, carat, cut,    color,    clarity,    depth,    table,    price,    x,    y,    z) values (90000, 0.22,    'Premium', 'I',    'SI2',    '60.3',    '62.1',    '334',    '3.79',    '3.75',    '2.27');
 
select * from diamond__mini;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-188.png align="left")

*Création d'un sous-ensemble* `diamonds_mini` pour démontrer l'opération UPSERT

Dans ce scénario, nous avons créé une table nommée `diamond__mini` pour tester les opérations d'upsert (c'est-à-dire, insérer ou mettre à jour) dans la table `diamonds`.

`diamond__mini` est un sous-ensemble de la table `diamonds`, contenant seulement 3 enregistrements. Deux de ces lignes (avec les valeurs `_c0` 1 et 2) existent déjà dans la table `diamonds`, et une ligne (avec la valeur `_c0` 90000) n'existe pas.

Par conséquent, le code supprimera et créera la table `diamond__mini` avec un schéma spécifique pour correspondre à la table `diamonds`.

Ensuite, il effacera la table `diamond__mini` en supprimant tous les enregistrements existants, garantissant ainsi que nous avons une ardoise propre pour le test d'upsert.

Il effectuera ensuite trois instructions `INSERT` dans la table `diamond__mini`, tentant d'ajouter trois nouveaux enregistrements avec différentes valeurs `_c0`, y compris une avec `_c0 = 90000`.

Enfin, nous sélectionnerons tous les enregistrements de la table `diamond__mini` pour observer les changements et vérifier si l'upsert a fonctionné correctement.

Puisque les valeurs `_c0` 1 et 2 existent déjà dans la table `diamonds`, les lignes correspondantes dans `diamond__mini` seront considérées comme des mises à jour pour les lignes existantes.

D'autre part, la ligne avec `_c0 = 90000` est nouvelle et n'existe pas dans la table `diamonds`, elle sera donc traitée comme une insertion.

La commande `describe` montre les métadonnées de la nouvelle table :

```sql
describe diamond__mini
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-189.png align="left")

*Récupération des métadonnées de la table nouvellement créée*

Voici un autre exemple qui utilise l'opération upsert :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-192.png align="left")

*opération upsert sur les tables diamond et diamond\_mini*

```sql
-- effectuer une opération UPSERT basée sur la correspondance de colonne et de ligne de diamond__mini à la table diamonds. Si une correspondance est trouvée, l'enregistrement sera mis à jour, sinon il sera inséré.
 
MERGE INTO diamonds as d USING diamond__mini as m
  ON d._c0 = m._c0
  WHEN MATCHED THEN 
    UPDATE SET *
  WHEN NOT MATCHED 
    THEN INSERT * ;
  
select * from diamonds where _c0 in (1 ,2, 90000)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-193.png align="left")

*Opération UPSERT réussie. Les valeurs des enregistrements avec* `_c0` = \[1,2\] ont été mises à jour et 90,000 a été inséré

Dans cet exemple, une opération `MERGE` est effectuée entre deux tables : `diamonds` (table cible) et `diamond__mini` (table source). L'instruction `MERGE` compare les enregistrements des deux tables en fonction de la colonne `_c0` commune.

Voici une explication concise :

1. L'instruction `MERGE` fait correspondre les enregistrements avec la même valeur `_c0` dans les deux tables (`diamonds` et `diamond__mini`).

2. Lorsqu'une correspondance est trouvée (basée sur `_c0`), elle effectue une `UPDATE` sur la table cible (`diamonds`) en utilisant les valeurs de la table source (`diamond__mini`). Cela est fait pour toutes les colonnes en utilisant `UPDATE SET *`.

3. Si aucune correspondance n'est trouvée pour un enregistrement de la table source (`diamond__mini`), elle effectue une `INSERT` dans la table cible (`diamonds`) en utilisant les valeurs de la table source pour toutes les colonnes (en utilisant `INSERT *`).

4. Après l'opération `MERGE`, une instruction `SELECT` récupère les enregistrements de la table cible (`diamonds`) avec les valeurs _c0 1, 2 et 90000 pour observer les changements effectués lors de la fusion.

L'instruction `MERGE` est utilisée pour synchroniser les données entre les tables `diamonds` et `diamond__mini` en fonction de leur colonne `_c0` commune, en mettant à jour les enregistrements existants et en insérant de nouveaux.

## Requêtes SQL avancées

### Visualisation des données dans Delta

Dans la plateforme Databricks Delta, vous pouvez exploiter les requêtes SQL pour visualiser les données et obtenir des informations précieuses sans avoir besoin de programmation complexe. Voici quelques façons de visualiser les données en utilisant des requêtes SQL dans Databricks Delta :

1. **Requêtes SELECT de base** : Récupère les données de vos tables Delta. En sélectionnant des colonnes spécifiques ou en appliquant des filtres avec des clauses WHERE, vous pouvez rapidement obtenir un aperçu des caractéristiques des données.

2. **Fonctions d'agrégation** : SQL fournit une variété de fonctions d'agrégation comme `COUNT`, `SUM`, `AVG`, `MIN` et `MAX`. En utilisant ces fonctions, vous pouvez résumer et visualiser les données à un niveau supérieur. Vous effectuez des opérations telles que le comptage du nombre d'enregistrements, le calcul des valeurs moyennes ou la recherche des valeurs maximales et minimales.

3. **Regroupement et agrégation des données** : La clause `GROUP BY` en SQL vous permet de regrouper les données en fonction de colonnes spécifiques, puis d'appliquer des fonctions d'agrégation à chaque groupe. Cela permet de générer des informations significatives en analysant les données sur une base catégorielle.

4. **Fonctions de fenêtre** : Les fonctions de fenêtre SQL, comme `ROW_NUMBER`, `RANK` et `DENSE_RANK`, sont précieuses pour partitionner les données et calculer les classements ou les totaux cumulatifs. Ces fonctions permettent d'analyser les données de manière plus granulaire et aident à découvrir des motifs.

5. **Jointure de tables** : Aide à combiner les données de plusieurs tables Delta en utilisant les opérations SQL `JOIN`. La fusion de données liées, l'analyse inter-tables et les visualisations avancées sont possibles grâce aux jointures.

6. **Sous-requêtes et CTEs** : Les sous-requêtes SQL et les expressions de table communes (CTEs) vous permettent de décomposer des problèmes complexes en parties gérables. Ces techniques peuvent simplifier l'analyse et rendre les requêtes SQL plus organisées et maintenables.

7. **Agrégats de fenêtre** : Les agrégats de fenêtre SQL, tels que `SUM`, `AVG` et `ROW_NUMBER` avec la clause `OVER`, vous permettent d'effectuer des calculs sur des fenêtres ou des plages de données spécifiques. Cela est utile pour analyser les tendances au fil du temps ou au sein de sous-ensembles spécifiques de vos données.

8. **Instructions CASE** : Les instructions CASE en SQL vous aident à créer des expressions conditionnelles, vous permettant de catégoriser ou de regrouper les données en fonction de certaines conditions. Cela peut aider à créer des étiquettes personnalisées ou à regrouper les données dans différentes catégories à des fins de visualisation.

Les puissantes capacités SQL de la plateforme permettent aux analystes de données et aux développeurs d'extraire des informations significatives de leurs données Delta Lake, le tout sans avoir besoin de langages ou d'outils de programmation supplémentaires.

```sql
-- requête d'agrégation pour obtenir le prix moyen basé sur les couleurs des diamants
SELECT color, avg(price) AS avg_price FROM diamonds GROUP BY color ORDER BY color
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-194.png align="left")

*Vue tabulaire de la requête*

Cette requête SQL ci-dessus est utilisée pour récupérer le prix moyen des diamants en fonction de leurs couleurs.

Décomposons le code :

`SELECT color, avg(price) AS avg_price` spécifie les colonnes qui seront sélectionnées dans l'ensemble de résultats. Il sélectionne la colonne `color` et calcule le prix moyen en utilisant la fonction `avg()`. La moyenne calculée est aliasée comme `avg_price` pour une référence plus facile dans l'ensemble de résultats.

La commande `FROM diamonds` spécifie la table à partir de laquelle les données seront récupérées. Dans ce cas, la table est nommée `diamonds`.

`GROUP BY color` regroupe les données par la colonne `color`. L'ensemble de résultats contiendra une ligne pour chaque couleur unique, et le prix moyen sera calculé pour chaque groupe séparément.

`ORDER BY color` organise l'ensemble de résultats par ordre croissant en fonction de la colonne `color`. La sortie sera triée par ordre alphabétique par couleur.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-195.png align="left")

*Résultats visualisés pour la requête*

### Compte des diamants par clarté

```sql
SELECT clarity, COUNT(*) AS count
FROM diamonds
GROUP BY clarity
ORDER BY count DESC;
```

Cette requête SQL ci-dessus calcule le nombre de diamants pour chaque niveau de clarté et présente les résultats par ordre décroissant. Elle sélectionne la colonne `clarity` et utilise la fonction `COUNT()` pour compter le nombre d'occurrences pour chaque valeur de clarté.

L'ensemble de résultats est regroupé par clarté et trié par ordre décroissant en fonction du nombre de diamants.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-196.png align="left")

*Visualisation en diagramme circulaire basée sur la requête ci-dessus*

### Prix moyen par plage de profondeur

```sql
-- Cette requête SQL calcule le prix moyen des diamants regroupés par plages de profondeur (60-62 et 62-64), et 'Autre' pour toutes les autres valeurs de profondeur, à partir de la table 'diamonds'. Les résultats sont triés par ordre décroissant en fonction du prix moyen.
 
SELECT CASE 
         WHEN depth BETWEEN 60 AND 62 THEN '60-62'
         WHEN depth BETWEEN 62 AND 64 THEN '62-64'
         ELSE 'Other'
       END AS depth_range,
       AVG(CAST(price AS DOUBLE)) AS avg_price
FROM diamonds
GROUP BY depth_range
ORDER BY avg_price DESC;
```

Ici, nous calculons le prix moyen des diamants regroupés par plages de profondeur. Il utilise une instruction `CASE` pour catégoriser les diamants en trois plages de profondeur : '60-62' pour les profondeurs comprises entre 60 et 62, '62-64' pour les profondeurs comprises entre 62 et 64, et 'Autre' pour toutes les autres valeurs de profondeur.

La fonction `AVG()` est ensuite utilisée pour calculer le prix moyen pour chaque plage de profondeur. L'ensemble de résultats est regroupé par la colonne `depth_range` et trié par ordre décroissant en fonction du prix moyen.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-197.png align="left")

*Prix moyen basé sur la plage de profondeur groupée, obtenu en utilisant la syntaxe CASE*

### Distribution des prix par table

```sql
--  Calculer la médiane, le premier quartile (q1) et le troisième quartile (q3) des prix pour chaque 'table' unique dans la table 'diamonds' en fonction de la colonne 'price'. Les résultats sont regroupés par 'table' et fournissent des informations statistiques précieuses sur la distribution des prix au sein de chaque catégorie.
 
SELECT table, 
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY CAST(price AS DOUBLE)) AS median_price,
       PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY CAST(price AS DOUBLE)) AS q1_price,
       PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY CAST(price AS DOUBLE)) AS q3_price
FROM diamonds
GROUP BY table;
```

Cette requête SQL calcule la médiane, le premier quartile (q1) et le troisième quartile (q3) des prix pour chaque valeur unique de `table` dans la table `diamonds`. Elle utilise la fonction `PERCENTILE_CONT()` pour calculer ces mesures statistiques.

La fonction est appliquée à la colonne `price`, qui est convertie en double pour des calculs précis. L'ensemble de résultats est regroupé par la colonne `table`, fournissant des informations sur la distribution des prix au sein de chaque catégorie `table`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-198.png align="left")

*Casting media, Q1 et Q3 figures basées sur le prix*

### Facteur de prix par X, Y et Z

```sql
-- Calculer le prix moyen des diamants regroupés par leurs valeurs x, y et z à partir de la table 'diamonds'. Les résultats sont triés par ordre décroissant en fonction du prix moyen, fournissant des informations précieuses sur le prix moyen des diamants avec différentes dimensions x, y et z.
 
SELECT x, y, z, AVG(CAST(price AS DOUBLE)) AS avg_price
FROM diamonds
GROUP BY x, y, z
ORDER BY avg_price DESC;
```

Cette requête calculera le prix moyen des diamants regroupés par leurs valeurs x, y et z à partir de la table `diamonds`. Elle sélectionne les colonnes `x`, `y`, `z`, et utilise la fonction `AVG()` pour calculer le prix moyen pour chaque combinaison de valeurs x, y et z.

L'ensemble de résultats est ensuite trié par ordre décroissant en fonction du prix moyen, fournissant des informations sur le prix moyen des diamants avec différentes dimensions.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-199.png align="left")

*Visualisation montrant le prix moyen des diamants regroupés par leurs valeurs x, y et z à partir de la table 'diamonds'*

### Ajouter des contraintes

```sql
-- Ce snippet de code SQL modifie la table 'diamonds' en supprimant la contrainte existante 'id_not_null' si elle existe. Ensuite, il ajoute une nouvelle contrainte nommée 'id_not_null' pour s'assurer que la colonne '_c0' ne doit pas contenir de valeurs nulles, renforçant ainsi l'intégrité des données dans la table.
 
ALTER TABLE diamonds DROP CONSTRAINT IF EXISTS id_not_null;
ALTER TABLE diamonds ADD CONSTRAINT id_not_null CHECK (_c0 is not null);
```

```sql
-- Cette commande échouera car nous insérons un utilisateur avec un id nul ::
INSERT INTO diamonds(_c0, carat, cut,    color,    clarity,    depth,    table,    price,    x,    y,    z) values (null, 0.22,    'Premium', 'I',    'SI2',    '60.3',    '62.1',    '334',    '3.79',    '3.75',    '2.27');
```

Notez que cela ne produira en réalité aucune sortie. Devinez pourquoi ? Parce qu'il ne respecte pas la contrainte NOT NULL. Donc, chaque fois que les contraintes ne sont pas remplies, une erreur sera générée. Dans ce cas, cette erreur exacte est affichée :

```sql
Error in SQL statement: DeltaInvariantViolationException: CHECK constraint id_not_null (_c0 IS NOT NULL) violated by row with values:
 - _c0 : null
```

Ce snippet de code SQL démontre la modification de la table `diamonds` pour renforcer l'intégrité des données.

La première ligne de code, `ALTER TABLE diamonds DROP CONSTRAINT IF EXISTS id_not_null;`, vérifie si une contrainte nommée `id_not_null` existe dans la table `diamonds` et la supprime si elle existe. Cette étape garantit que toute contrainte existante avec le même nom est supprimée avant d'en ajouter une nouvelle.

La deuxième ligne de code, `ALTER TABLE diamonds ADD CONSTRAINT id_not_null CHECK (_c0 is not null);`, ajoute une nouvelle contrainte nommée `id_not_null` à la table `diamonds`. Cette contrainte spécifie que la colonne `_c0` ne doit pas contenir de valeurs nulles. Elle garantit que chaque fois que des données sont insérées ou mises à jour dans cette table, la colonne '\_c0' ne peut pas avoir une valeur nulle, maintenant ainsi l'intégrité des données.

Cependant, la commande suivante, `INSERT INTO diamonds(_c0, carat, cut, color, clarity, depth, table, price, x, y, z) VALUES (null, 0.22, 'Premium', 'I', 'SI2', '60.3', '62.1', '334', '3.79', '3.75', '2.27');`, tente d'insérer une ligne dans la table `diamonds` avec une valeur nulle dans la colonne `_c0`.

Puisque la nouvelle contrainte interdit les valeurs nulles dans cette colonne, l'opération `INSERT` échouera, préservant ainsi l'intégrité des données spécifiée par la contrainte.

## Comment travailler avec les DataFrames

La meilleure partie est que vous n'êtes pas limité à l'utilisation de SQL pour y parvenir. Ci-dessous, la même chose est faite en chargeant d'abord l'ensemble de données dans `diamonds` avec Python, puis en utilisant les fonctions de la bibliothèque pyspark pour effectuer des requêtes complexes.

```python
%python
diamonds = spark.read.csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header="true", inferSchema="true")
```

Dans la plateforme Databricks Delta Lake, l'objet `spark` représente la SparkSession, qui est le point d'entrée pour interagir avec les fonctionnalités de Spark. Il fournit une interface de programmation pour travailler avec des données structurées et semi-structurées.

La fonction `spark.read.csv()` est utilisée pour lire un fichier CSV dans un DataFrame. Dans ce cas, elle lit le fichier **diamonds.csv** à partir du chemin spécifié. Les arguments passés à la fonction incluent :

* `"/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv"` : Il s'agit du chemin vers le fichier CSV. Vous pouvez remplacer cela par le chemin réel où se trouve votre fichier.

* `header="true"` : Cela spécifie que la première ligne du fichier CSV contient les noms des colonnes.

* `inferSchema="true"` : Cela indique à Spark de déduire automatiquement les types de données des colonnes dans le DataFrame.

Une fois le fichier CSV lu, il est stocké dans la variable `diamonds` en tant que DataFrame. Le DataFrame représente une collection distribuée de données organisées en colonnes nommées. Il fournit diverses fonctions et méthodes pour manipuler et analyser les données.

En lisant le fichier CSV dans un DataFrame sur la plateforme Databricks Delta Lake, vous pouvez exploiter les riches capacités de requête et de traitement de Spark pour effectuer des analyses de données, des transformations et d'autres opérations sur les données de diamants.

### **Manipuler les données et afficher les résultats**

L'exemple ci-dessous montre que sur la plateforme Databricks Delta Lake, vous n'êtes pas limité à l'utilisation de requêtes SQL uniquement. Vous pouvez également exploiter Python et son riche écosystème de bibliothèques, telles que PySpark, pour effectuer des manipulations et des analyses de données complexes.

En utilisant Python, vous avez accès à une large gamme de fonctions et de méthodes fournies par l'API DataFrame de PySpark. Cela vous permet d'effectuer diverses transformations, agrégations, calculs et opérations de tri sur vos données.

Que vous choisissiez d'utiliser SQL ou Python, la plateforme Databricks Delta Lake offre un environnement flexible pour le traitement et l'analyse des données, vous permettant de découvrir des informations précieuses à partir de vos données.

```python
%python
from pyspark.sql.functions import avg
 
display(diamonds.select("color","price").groupBy("color").agg(avg("price")).sort("color"))
```

Tout d'abord, l'instruction `from pyspark.sql.functions import avg` importe la fonction `avg` du module `pyspark.sql.functions`. Cette fonction est utilisée pour calculer la valeur moyenne d'une colonne.

Ensuite, l'expression `diamonds.select("color", "price").groupBy("color").agg(avg("price")).sort("color")` effectue les opérations suivantes :

`diamonds.select("color", "price")` sélectionne uniquement les colonnes `color` et `price` du DataFrame `diamonds`.

`groupBy("color")` regroupe les données en fonction de la colonne `color`.

`agg(avg("price"))` calcule le prix moyen pour chaque groupe (couleur). L'argument `avg("price")` spécifie que nous voulons calculer la moyenne de la colonne "price".

`sort("color")` trie le DataFrame résultant par ordre croissant en fonction de la colonne `color`.

Enfin, la fonction `display()` est utilisée pour visualiser le DataFrame résultant dans un format tabulaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-200.png align="left")

## **Contrôle de version et voyage dans le temps dans Delta**

Les capacités de voyage dans le temps de Databricks Delta simplifient la construction de pipelines de données. Cela s'avère utile lors de l'audit des modifications de données, de la reproduction d'expériences et de rapports ou de l'exécution de rollbacks de transactions de base de données. Cela est également utile pour la récupération après sinistre et nous permet d'annuler les modifications et de revenir à n'importe quelle version spécifique d'une base de données.

Lorsque vous écrivez dans une table Delta ou un répertoire, chaque opération est automatiquement versionnée. Interrogez une table en faisant référence à un horodatage ou à un numéro de version.

La commande ci-dessous retourne une liste de toutes les versions et horodatages dans une table appelée `diamonds` :

```javascript
DESCRIBE HISTORY diamonds;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-201.png align="left")

*DESCRIBE HISTORY* `table_name` retourne une liste de toutes les versions de la table avec leurs horodatages, opérations. Il inclut également quel utilisateur a exécuté la requête.

### Restaurer la configuration

Delta offre un support intégré pour les stratégies de sauvegarde et de restauration afin de gérer les problèmes tels que la corruption des données ou la perte accidentelle de données. Dans notre scénario, nous allons intentionnellement supprimer certaines lignes de la table principale pour simuler de telles situations.

Nous utiliserons ensuite la capacité de restauration de Delta pour revenir à un point dans le temps avant l'opération de suppression. En faisant cela, nous pouvons vérifier si la suppression a été réussie ou si les données ont été correctement restaurées à leur état précédent. Cette fonctionnalité garantit la sécurité des données et offre un moyen facile de se remettre des changements indésirables ou des échecs.

Voici le code :

```sql
-- Supprimer 10 enregistrements de la table principale
DELETE FROM diamonds where `_c0`in (1,2,3,4,5,6,7,8,9,10);
SELECT COUNT(*) from diamonds;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-202.png align="left")

*Nombre de lignes après la suppression de 10 enregistrements de la table principale*

```sql
SELECT COUNT(*) FROM diamonds VERSION AS OF 19;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-203.png align="left")

*Nombre de lignes en référençant une version précédente de la table*

## **Restauration à partir d'un numéro de version**

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-204.png align="left")

*Illustration de la manière dont une restauration de version fonctionne dans les cahiers Databricks*

Le code ci-dessous restaure la table `diamonds` à la version qui existait au numéro de version 19, en utilisant une fonctionnalité de versionnement de base de données ou de données historiques. Après la restauration, une instruction `SELECT` est exécutée pour récupérer toutes les données de la table `diamonds` telles qu'elles existaient à la version 19.

Ce processus vous permet de visualiser l'état historique de la table à cette version spécifique, permettant l'analyse des données ou les comparaisons avec la version actuelle.

```sql
-- restaurer l'état de la table diamonds à celui de la version 19 (référer les images de la base de données dans la cellule précédente)
 
RESTORE TABLE diamonds TO VERSION AS OF 19;
SELECT * from diamonds;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-205.png align="left")

*Requête SELECT s'exécutant contre une version restaurée de la base de données*

### Champs autogénérés

Voyons comment utiliser l'auto-incrément dans Delta avec SQL. Le code ci-dessous démontre la création d'une table appelée `test__autogen` avec un champ "autogénéré" nommé `id`. La colonne `id` est définie comme `BIGINT GENERATED ALWAYS AS IDENTITY`, ce qui signifie que ses valeurs seront automatiquement générées par le moteur de base de données lors du processus d'insertion.

L'`id` sert de clé primaire auto-incrémentée pour la table, garantissant que chaque nouvel enregistrement reçoit un identifiant unique sans aucune entrée manuelle. Cette fonctionnalité simplifie l'insertion de données et garantit l'unicité des enregistrements au sein de la table, améliorant ainsi l'efficacité de la gestion de la base de données.

Cette fonctionnalité d'auto-incrément est couramment utilisée pour les clés primaires, car elle garantit l'unicité de chaque enregistrement dans la table. Elle évite également aux développeurs de devoir gérer la génération d'identifiants uniques manuellement, offrant ainsi un flux de travail plus rationalisé et efficace.

```sql
%sql 
CREATE TABLE IF NOT EXISTS test__autogen (
  id BIGINT GENERATED ALWAYS AS IDENTITY ( START WITH 10000 INCREMENT BY 1 ), 
  name STRING, 
  surname STRING, 
  email STRING, 
  city STRING) ;
 
-- Notez que nous n'insérons pas de données pour l'id. Le moteur s'en chargera pour nous :
INSERT INTO test__autogen (name, surname, email, city) VALUES ('Atharva', 'Shah', 'highnessatharva@gmail.com', 'Pune, IN');
INSERT INTO test__autogen (name, surname, email, city) VALUES ('James', 'Dean', 'james@proton.mail', 'Tokyo, JP');
 
-- L'ID est généré automatiquement !
SELECT * from test__autogen;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-206.png align="left")

*Enregistrements avec un* `id` autogénéré

## **Clonage de table Delta**

Le clonage de tables Delta vous permet de créer une réplique d'une table Delta existante à une version spécifique. Cette fonctionnalité est particulièrement précieuse lorsque vous devez transférer des données d'un environnement de production vers un environnement de préproduction ou lorsque vous archivez une version spécifique à des fins réglementaires.

Il existe deux types de clones disponibles :

1. **Clone profond** : Ce type de clone copie à la fois les données et les métadonnées de la table source vers la cible de clonage. En d'autres termes, il réplique l'ensemble de la table, la rendant indépendante de la source.

2. **Clone superficiel** : Un clone superficiel ne réplique que les métadonnées de la table sans copier les fichiers de données réels vers la cible de clonage. Par conséquent, ces clones sont plus économiques à créer. Cependant, il est crucial de noter que les clones superficiels agissent comme des pointeurs vers la table principale. Si une opération `VACUUM` est effectuée sur la table d'origine, elle peut supprimer les fichiers sous-jacents et potentiellement impacter le clone superficiel.

Il est important de se rappeler que toute modification apportée aux clones profonds ou superficiels n'affecte que les clones eux-mêmes et non la table source.

Le clonage de tables Delta est une fonctionnalité puissante qui simplifie la réplication des données et l'archivage des versions, améliorant ainsi les capacités de gestion des données au sein de votre environnement Delta Lake.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-207.png align="left")

*Différence entre un clone superficiel et un clone profond*

Le code ci-dessous montre comment cloner une table en utilisant des clones superficiels et profonds :

```sql
-- Clone superficiel (zéro copie)
CREATE TABLE IF NOT EXISTS diamonds__shallow__clone
  SHALLOW CLONE diamonds
  VERSION AS OF 19;
 
SELECT * FROM diamonds__shallow__clone;
 
-- Clone profond (copie des données)
CREATE TABLE IF NOT EXISTS diamonds__deep__clone
  DEEP CLONE diamonds;
 
SELECT * FROM diamonds__deep__clone;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-208.png align="left")

*Sélection des enregistrements de la table clonée en profondeur*

## Commandes magiques Delta

Il existe des raccourcis pratiques dans les cahiers Databricks pour gérer les tables Delta. Ils simplifient les opérations courantes comme l'affichage des métadonnées des tables et l'exécution de l'optimisation.

Vous pouvez utiliser ces commandes de raccourci pour améliorer la productivité en rationalisant les tâches de gestion des tables Delta dans un environnement de cahier.

1. `%run` : exécute un fichier Python ou un cahier.

2. `%sh` : exécute des commandes shell sur les nœuds du cluster.

3. `%fs` : vous permet d'interagir avec le système de fichiers Databricks.

4. `%sql` : vous permet d'exécuter des requêtes SQL.

5. `%scala` : bascule le contexte du cahier vers Scala.

6. `%python` : bascule le contexte du cahier vers Python.

7. `%md` : vous permet d'écrire du texte en markdown.

8. `%r` : bascule le contexte du cahier vers R.

9. `%lsmagic` : liste toutes les commandes magiques disponibles.

10. `%jobs` : liste tous les travaux en cours d'exécution.

11. `%config` : vous permet de définir des options de configuration pour le cahier.

12. `%reload` : recharge le contenu d'un module.

13. `%pip` : vous permet d'installer des packages Python.

14. `%load` : charge le contenu d'un fichier dans une cellule.

15. `%matplotlib` : configure le backend matplotlib.

16. `%who` : liste toutes les variables dans la portée actuelle.

17. `%env` : vous permet de définir des variables d'environnement.

## Conclusion

Ce guide approfondi a exploré la puissance de Databricks, une plateforme qui unifie l'analyse et la science des données dans un seul espace de travail. Nous avons parcouru l'espace de travail Databricks, l'analyse interactive et Delta Lake, en mettant l'accent sur ses capacités de manipulation et d'analyse des données.

Delta, un moteur d'intégrité et d'agilité des données, prend en charge les commandes SQL ainsi que les requêtes sophistiquées. Les DataFrames sont utilisés pour façonner et afficher les données afin d'améliorer les insights. La rétrospection et la précision sont activées par le contrôle de version et le voyage dans le temps. Le clonage de tables Delta offre de l'innovation en permettant des études analytiques dans des territoires encore inexplorés.

Votre quête de l'excellence des données ne s'arrête pas ici. Restons connectés : explorez plus d'insights sur mon [blog](https://atharvashah.netlify.app/), envisagez de me soutenir avec un [café](https://www.buymeacoffee.com/atharvashah), et rejoignez la conversation sur [Twitter](https://twitter.com/cultist_dev) et [LinkedIn](https://www.linkedin.com/in/atharva-shah-5873a2111/). Maintenez l'élan en consultant quelques-uns de mes autres articles.

## Références

1. [Documentation officielle de Databricks](https://docs.databricks.com/delta/index.html)

2. [Tutoriels Databricks Labs - Delta Lake](https://databricks.com/labs)