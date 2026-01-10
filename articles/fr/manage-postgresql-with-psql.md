---
title: Comment gérer les bases de données PostgreSQL depuis la ligne de commande avec
  psql
subtitle: ''
author: Gerard Hynes
co_authors: []
series: null
date: '2022-06-07T15:29:11.000Z'
originalURL: https://freecodecamp.org/news/manage-postgresql-with-psql
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/manage-postgreSQL-with-psql.png
tags:
- name: command line
  slug: command-line
- name: database
  slug: database
- name: postgres
  slug: postgres
- name: terminal
  slug: terminal
seo_title: Comment gérer les bases de données PostgreSQL depuis la ligne de commande
  avec psql
seo_desc: 'Now is a great time to learn relational databases and SQL. From web development
  to data science, they are used everywhere.

  In the Stack Overflow 2021 Survey, 4 out of the top 5 database technologies used
  by professional developers were relational dat...'
---

C'est le moment idéal pour apprendre les bases de données relationnelles et SQL. Du développement web à la science des données, elles sont utilisées partout.

Dans l'[Enquête Stack Overflow 2021](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-database-prof), 4 des 5 technologies de bases de données les plus utilisées par les développeurs professionnels étaient des systèmes de gestion de bases de données relationnelles.

PostgreSQL est un excellent choix comme premier système de gestion de bases de données relationnelles à apprendre.

1. Il est largement utilisé dans l'industrie, y compris chez [Uber, Netflix, Instagram, Spotify et Twitch](https://stackshare.io/postgresql).
   
2. Il est open source, donc vous ne serez pas lié à un fournisseur particulier.
   
3. Il a plus de 25 ans, et pendant ce temps, il s'est forgé une réputation de stabilité et de fiabilité.
   

Que vous appreniez à partir de la certification [Relational Database Certification](https://www.freecodecamp.org/learn/relational-database/) de freeCodeCamp ou que vous essayiez PostgreSQL sur votre propre ordinateur, vous avez besoin d'un moyen de créer et de gérer des bases de données, d'y insérer des données et d'en interroger les données.

Bien qu'il existe plusieurs applications graphiques pour interagir avec PostgreSQL, l'utilisation de psql et de la ligne de commande est probablement le moyen le plus direct de communiquer avec votre base de données.

## Qu'est-ce que psql ?

psql est un outil qui vous permet d'interagir avec les bases de données PostgreSQL via une interface terminal. Lorsque vous installez PostgreSQL sur une machine, psql est automatiquement inclus.

psql vous permet d'écrire des requêtes SQL, de les envoyer à PostgreSQL et de voir les résultats. Il vous permet également d'utiliser des méta-commandes (qui commencent par un antislash) pour administrer les bases de données. Vous pouvez même écrire des scripts et automatiser des tâches liées à vos bases de données.

Maintenant, exécuter une base de données sur votre ordinateur local et utiliser la ligne de commande peut sembler intimidant au début. Je suis là pour vous dire que ce n'est vraiment pas si compliqué. Ce guide vous apprendra les bases de la gestion des bases de données PostgreSQL depuis la ligne de commande, y compris comment créer, gérer, sauvegarder et restaurer des bases de données.

## Prérequis - Installer PostgreSQL

Si vous n'avez pas encore installé PostgreSQL sur votre ordinateur, suivez les instructions pour votre système d'exploitation sur la [documentation officielle de PostgreSQL](https://www.postgresql.org/download/).

Lorsque vous installez PostgreSQL, on vous demandera un mot de passe. Conservez-le dans un endroit sûr car vous en aurez besoin pour vous connecter à toute base de données que vous créerez.

## Comment se connecter à une base de données

Vous avez deux options lorsque vous utilisez psql pour vous connecter à une base de données : vous pouvez vous connecter via la ligne de commande ou en utilisant l'application psql. Les deux offrent à peu près la même expérience.

### Option 1 - Se connecter à une base de données avec la ligne de commande

Ouvrez un terminal. Vous pouvez vous assurer que psql est installé en tapant `psql --version`. Vous devriez voir `psql (PostgreSQL) version_number`, où `version_number` est la version de PostgreSQL installée sur votre machine. Dans mon cas, c'est 14.1.

![Vérification de la version de psql via la ligne de commande](https://www.freecodecamp.org/news/content/images/2022/06/image-4.png align="left")

*Vérification de la version de psql via la ligne de commande*

Le modèle pour se connecter à une base de données est :

```python
psql -d database_name -U username
```

Le drapeau `-d` est une alternative plus courte pour `--dbname` tandis que `-U` est une alternative pour `--username`.

Lorsque vous avez installé PostgreSQL, une base de données et un utilisateur par défaut ont été créés, tous deux appelés `postgres`. Donc entrez `psql -d postgres -U postgres` pour vous connecter à la base de données `postgres` en tant que superutilisateur `postgres`.

```python
psql -d postgres -U postgres
```

Vous serez invité à entrer un mot de passe. Entrez le mot de passe que vous avez choisi lorsque vous avez installé PostgreSQL sur votre ordinateur. Votre prompt de terminal changera pour montrer que vous êtes maintenant connecté à la base de données `postgres`.

![Connexion à une base de données depuis la ligne de commande avec psql](https://www.freecodecamp.org/news/content/images/2022/06/image-5.png align="left")

*Connexion à une base de données depuis la ligne de commande avec psql*

Si vous voulez vous connecter directement à une base de données en tant que vous-même (plutôt qu'en tant que superutilisateur `postgres`), entrez votre nom d'utilisateur système comme valeur de nom d'utilisateur.

### Option 2 - Se connecter à une base de données avec l'application psql

Lancez l'application psql - elle s'appellera "SQL Shell (psql)". Vous serez invité à entrer un serveur, une base de données, un port et un nom d'utilisateur. Vous pouvez simplement appuyer sur Entrée pour sélectionner les valeurs par défaut, qui sont `localhost`, `postgres`, `5432`, et `postgres`.

Ensuite, vous serez invité à entrer le mot de passe que vous avez choisi lorsque vous avez installé PostgreSQL. Une fois que vous l'avez entré, votre prompt de terminal changera pour montrer que vous êtes connecté à la base de données `postgres`.

![Connexion à une base de données avec l'application psql](https://www.freecodecamp.org/news/content/images/2022/06/image-2.png align="left")

*Connexion à une base de données avec l'application psql*

**Note :** Si vous êtes sur Windows, vous pourriez voir un avertissement comme "Console code page (850) differs from Windows code page (1252) 8-bit characters might not work correctly. See psql reference page 'Notes for Windows users' for details." Vous n'avez pas besoin de vous en soucier à ce stade. Si vous voulez en savoir plus, consultez la [documentation psql](https://www.postgresql.org/docs/current/app-psql.html).

## Comment obtenir de l'aide dans psql

Pour voir une liste de toutes les méta-commandes psql, et un bref résumé de ce qu'elles font, utilisez la commande `\?`.

```python
\?
```

![Commande d'aide de psql](https://www.freecodecamp.org/news/content/images/2022/06/image-6.png align="left")

*Commande d'aide de psql*

Si vous voulez de l'aide avec une commande PostgreSQL, utilisez `\h` ou `\help` et la commande.

```python
\h COMMAND
```

Cela vous donnera une description de la commande, sa syntaxe (avec les parties optionnelles entre crochets), et une URL pour la partie pertinente de la documentation PostgreSQL.

![psql décrivant l'instruction DROP TABLE](https://www.freecodecamp.org/news/content/images/2022/06/image-7.png align="left")

*psql décrivant l'instruction DROP TABLE*

## Comment quitter une commande dans psql

Si vous avez exécuté une commande qui prend beaucoup de temps ou qui imprime trop d'informations dans la console, vous pouvez la quitter en tapant `q`.

```python
q
```

## Comment créer une base de données

Avant de pouvoir gérer des bases de données, vous devez en créer une.

**Note :** Les commandes SQL doivent se terminer par un point-virgule, tandis que les méta-commandes (qui commencent par un antislash) n'en ont pas besoin.

La commande SQL pour créer une base de données est :

```sql
CREATE DATABASE database_name;
```

Pour ce guide, nous allons travailler avec des données de livres, alors créons une base de données appelée `books_db`.

```sql
CREATE DATABASE books_db;
```

## Comment lister les bases de données

Vous pouvez voir une liste de toutes les bases de données disponibles avec la commande list.

```python
\l
```

![Liste de toutes les bases de données](https://www.freecodecamp.org/news/content/images/2022/06/image-8.png align="left")

*Liste de toutes les bases de données*

Vous devriez voir `books_db`, ainsi que `postgres`, `template0`, et `template1`. (La commande `CREATE DATABASE` fonctionne en copiant la base de données standard, appelée `template1`. Vous pouvez en savoir plus à ce sujet dans la [documentation PostgreSQL](https://www.postgresql.org/docs/current/manage-ag-templatedbs.html).)

L'utilisation de `\l+` affichera des informations supplémentaires, telles que la taille des bases de données et leurs tablespaces (l'emplacement dans le système de fichiers où les fichiers représentant la base de données seront stockés).

```python
\l+
```

![Liste de toutes les bases de données avec des informations supplémentaires](https://www.freecodecamp.org/news/content/images/2022/06/image-22.png align="left")

*Liste de toutes les bases de données avec des informations supplémentaires*

## Comment changer de base de données

Vous êtes actuellement toujours connecté à la base de données par défaut `postgres`. Pour vous connecter à une base de données ou pour changer de base de données, utilisez la commande `\c`.

```python
\c database_name
```

Donc `\c books_db` vous connectera à la base de données `books_db`. Notez que votre prompt de terminal change pour refléter la base de données à laquelle vous êtes actuellement connecté.

![Changement de base de données](https://www.freecodecamp.org/news/content/images/2022/06/image-9.png align="left")

*Changement de base de données*

## Comment supprimer une base de données

Si vous voulez supprimer une base de données, utilisez la commande `DROP DATABASE`.

```sql
DROP DATABASE database_name;
```

Vous ne serez autorisé à supprimer une base de données que si vous êtes un superutilisateur, comme `postgres`, ou si vous êtes le propriétaire de la base de données.

Si vous essayez de supprimer une base de données qui n'existe pas, vous obtiendrez une erreur. Utilisez `IF EXISTS` pour obtenir une notification à la place.

```sql
DROP DATABASE IF EXISTS database_name;
```

![Suppression d'une base de données](https://www.freecodecamp.org/news/content/images/2022/06/image-10.png align="left")

*Suppression d'une base de données*

Vous ne pouvez pas supprimer une base de données qui a des connexions actives. Donc si vous voulez supprimer la base de données à laquelle vous êtes actuellement connecté, vous devrez changer pour une autre base de données.

## Comment créer des tables

Avant de pouvoir gérer des tables, nous devons en créer quelques-unes et les remplir avec des données d'exemple.

La commande pour créer une table est :

```sql
CREATE TABLE table_name();
```

Cela créera une table vide. Vous pouvez également passer des valeurs de colonne entre les parenthèses pour créer une table avec des colonnes. Au minimum, une table de base devrait avoir une clé primaire (un identifiant unique pour distinguer chaque ligne) et une colonne avec des données.

Pour notre `books_db`, nous allons créer une table pour les auteurs et une autre pour les livres. Pour les auteurs, nous enregistrerons leur prénom et leur nom de famille. Pour les livres, nous enregistrerons le titre et l'année de publication.

Nous nous assurerons que les `first_name` et `last_name` des auteurs et le `title` des livres ne sont pas nuls, car ce sont des informations assez vitales à connaître à leur sujet. Pour ce faire, nous incluons la contrainte `NOT NULL`.

```sql
CREATE TABLE authors(
	author_id SERIAL PRIMARY KEY, 
	first_name VARCHAR(100) NOT NULL, 
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE books(
	book_id SERIAL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	published_year INT
);
```

Vous verrez `CREATE TABLE` imprimé dans le terminal si la table a été créée avec succès.

Maintenant, connectons les deux tables en ajoutant une clé étrangère aux livres. Les clés étrangères sont des identifiants uniques qui référencent la clé primaire d'une autre table. Les livres peuvent, bien sûr, avoir plusieurs auteurs, mais nous n'allons pas entrer dans les complexités des relations plusieurs à plusieurs pour l'instant.

Ajoutez une clé étrangère à `books` avec la commande suivante :

```sql
ALTER TABLE books ADD COLUMN author_id INT REFERENCES authors(author_id);
```

Ensuite, insérons quelques données d'exemple dans les tables. Nous commencerons par `authors`.

```sql
INSERT INTO authors (first_name, last_name) 
VALUES ('Tamsyn', 'Muir'), ('Ann', 'Leckie'), ('Zen', 'Cho');
```

Sélectionnez tout depuis `authors` pour vous assurer que la commande d'insertion a fonctionné.

```sql
SELECT * FROM authors;
```

![Interrogation de toutes les données de la table des auteurs](https://www.freecodecamp.org/news/content/images/2022/06/image-13.png align="left")

*Interrogation de toutes les données de la table des auteurs*

Ensuite, nous allons insérer quelques données de livres dans `books`.

```sql
INSERT INTO books(title, published_year, author_id) 
VALUES ('Gideon the Ninth', 2019, 1), ('Ancillary Justice', 2013, 2), ('Black Water Sister', 2021, 3);
```

Si vous exécutez `SELECT * FROM books;` vous verrez les données des livres.

![Interrogation de toutes les données de la table des livres](https://www.freecodecamp.org/news/content/images/2022/06/image-14.png align="left")

*Interrogation de toutes les données de la table des livres*

## Comment lister toutes les tables

Vous pouvez utiliser la commande `\dt` pour lister toutes les tables dans une base de données.

```python
\dt
```

Pour `books_db`, vous verrez `books` et `authors`. Vous verrez également `books_book_id_seq` et `authors_author_id_seq`. Ceux-ci gardent une trace de la séquence d'entiers utilisés comme identifiants par les tables car nous avons utilisé `SERIAL` pour générer leurs clés primaires.

![Liste de toutes les tables dans une base de données](https://www.freecodecamp.org/news/content/images/2022/06/image-15.png align="left")

*Liste de toutes les tables dans une base de données*

## Comment décrire une table

Pour voir plus d'informations sur une table particulière, vous pouvez utiliser la commande describe table : `\d table_name`. Cela listera les colonnes, les index et toutes les références à d'autres tables.

```python
\d table_name
```

![Description de la table des auteurs](https://www.freecodecamp.org/news/content/images/2022/06/image-25.png align="left")

*Description de la table des auteurs*

L'utilisation de `\dt+ table_name` fournira plus d'informations, telles que sur le stockage et la compression.

## Comment renommer une table

Si vous devez changer le nom d'une table, vous pouvez la renommer avec la commande `ALTER TABLE`.

```sql
ALTER TABLE table_name RENAME TO new_table_name;
```

## Comment supprimer une table

Si vous voulez supprimer une table, vous pouvez utiliser la commande `DROP TABLE`.

```sql
DROP TABLE table_name;
```

Si vous essayez de supprimer une table qui n'existe pas, vous obtiendrez une erreur. Vous pouvez éviter cela en incluant l'option `IF EXISTS` dans l'instruction. De cette façon, vous obtiendrez une notification à la place.

```sql
DROP TABLE IF EXISTS table_name;
```

## Comment gérer des commandes et requêtes plus longues

Si vous écrivez des requêtes SQL plus longues, la ligne de commande n'est pas le moyen le plus ergonomique de le faire. Il est probablement préférable d'écrire votre SQL dans un fichier et de faire exécuter celui-ci par psql.

Si vous travaillez avec psql et pensez que votre prochaine requête sera longue, vous pouvez ouvrir un éditeur de texte depuis psql et l'écrire là. Si vous avez une requête existante, ou peut-être souhaitez exécuter plusieurs requêtes pour charger des données d'exemple, vous pouvez exécuter des commandes à partir d'un fichier déjà écrit.

### Option 1 - Ouvrir un éditeur de texte depuis psql

Si vous entrez la commande `\e`, psql ouvrira un éditeur de texte. Lorsque vous sauvegardez et fermez l'éditeur, psql exécutera la commande que vous venez d'écrire.

```python
\e
```

![Écriture de commandes dans un éditeur de texte](https://www.freecodecamp.org/news/content/images/2022/06/image-30.png align="left")

*Écriture de commandes dans un éditeur de texte*

Sur Windows, l'éditeur de texte par défaut pour psql est Notepad, tandis que sur MacOs et Linux, c'est vi. Vous pouvez changer cela pour un autre éditeur en définissant la valeur `EDITOR` dans les variables d'environnement de votre ordinateur.

### Option 2 - Exécuter des commandes et requêtes depuis un fichier

Si vous avez des commandes particulièrement longues ou plusieurs commandes que vous voulez exécuter, il serait préférable d'écrire le SQL dans un fichier à l'avance et de faire exécuter ce fichier par psql une fois que vous êtes prêt.

La commande `\i` vous permet de lire l'entrée depuis un fichier comme si vous l'aviez tapée dans le terminal.

```python
\i path_to_file/file_name.sql
```

**Note :** Si vous exécutez cette commande sur Windows, vous devez toujours utiliser des barres obliques dans le chemin du fichier.

Si vous ne spécifiez pas de chemin, psql cherchera le fichier dans le dernier répertoire dans lequel vous étiez avant de vous connecter à PostgreSQL.

![Exécution de commandes SQL depuis un fichier](https://www.freecodecamp.org/news/content/images/2022/06/image-29.png align="left")

*Exécution de commandes SQL depuis un fichier*

## Comment chronométrer les requêtes

Si vous voulez voir combien de temps prennent vos requêtes, vous pouvez activer le chronométrage de l'exécution des requêtes.

```python
\timing
```

Cela affichera en millisecondes le temps que la requête a pris pour s'exécuter.

Si vous exécutez à nouveau la commande `\timing`, elle désactivera le chronométrage de l'exécution des requêtes.

![Utilisation du chronométrage de l'exécution des requêtes](https://www.freecodecamp.org/news/content/images/2022/06/image-19.png align="left")

*Utilisation du chronométrage de l'exécution des requêtes*

## Comment importer des données depuis un fichier CSV

Si vous avez un fichier CSV avec des données et que vous voulez charger celles-ci dans une base de données PostgreSQL, vous pouvez le faire depuis la ligne de commande avec psql.

Tout d'abord, créez un fichier CSV appelé `films.csv` avec la structure suivante (peu importe si vous utilisez Excel, Google Sheets, Numbers ou tout autre programme).

![Une feuille de calcul avec des données de films Pixar](https://www.freecodecamp.org/news/content/images/2022/06/image-21.png align="left")

*Une feuille de calcul avec des données de films Pixar*

Ouvrez psql et créez une base de données `films_db`, connectez-vous à celle-ci et créez une table `films`.

```sql
CREATE DATABASE films_db;

\c films_db

CREATE TABLE films(
	id SERIAL PRIMARY KEY,
	title VARCHAR(100),
	year INT,
	running_time INT
);
```

Vous pouvez ensuite utiliser la commande `\copy` pour importer le fichier CSV dans `films`. Vous devez fournir un chemin absolu vers l'emplacement du fichier CSV sur votre ordinateur.

```python
\copy films(title, year, running_time) FROM 'path_to_file' DELIMITER ',' CSV HEADER;
```

L'option `DELIMITER` spécifie le caractère qui sépare les colonnes dans chaque ligne du fichier importé, `CSV` spécifie qu'il s'agit d'un fichier CSV, et `HEADER` spécifie que le fichier contient une ligne d'en-tête avec les noms des colonnes.

**Note :** Les noms des colonnes de la table `films` n'ont pas besoin de correspondre aux noms des colonnes de `films.csv`, mais ils doivent être dans le même ordre.

Utilisez `SELECT * FROM films;` pour voir si le processus a réussi.

![Importation de données depuis un fichier .csv](https://www.freecodecamp.org/news/content/images/2022/06/image-31.png align="left")

*Importation de données depuis un fichier .csv*

## Comment sauvegarder une base de données avec `pg_dump`

Si vous devez sauvegarder une base de données, `pg_dump` est un utilitaire qui vous permet d'extraire une base de données dans un fichier de script SQL ou un autre type de fichier d'archive.

Tout d'abord, sur la ligne de commande (pas dans psql), naviguez jusqu'au dossier `bin` de PostgreSQL.

```python
cd "C:\Program Files\PostgreSQL\14\bin"
```

Ensuite, exécutez la commande suivante, en utilisant `postgres` comme nom d'utilisateur, et en remplissant la base de données et le fichier de sortie que vous souhaitez utiliser.

```python
pg_dump -U username database_name > path_to_file/filename.sql
```

Utilisez `postgres` pour le nom d'utilisateur et vous serez invité à entrer le mot de passe du superutilisateur `postgres`. `pg_dump` créera alors un fichier `.sql` contenant les commandes SQL nécessaires pour recréer la base de données.

![Sauvegarde d'une base de données dans un fichier .sql](https://www.freecodecamp.org/news/content/images/2022/06/image-60.png align="left")

*Sauvegarde d'une base de données dans un fichier .sql*

Si vous ne spécifiez pas de chemin pour le fichier de sortie, `pg_dump` enregistrera le fichier dans le dernier répertoire dans lequel vous étiez avant de vous connecter à PostgreSQL.

![Contenu du fichier de sauvegarde films.sql](https://www.freecodecamp.org/news/content/images/2022/06/image-45.png align="left")

*Contenu du fichier de sauvegarde films.sql*

Vous pouvez passer le drapeau `-v` ou `--verbose` à `pg_dump` pour voir ce que `pg_dump` fait à chaque étape.

![Exécution de pg_dump en mode verbeux](https://www.freecodecamp.org/news/content/images/2022/06/image-61.png align="left")

*Exécution de pg_dump en mode verbeux*

Vous pouvez également sauvegarder une base de données dans d'autres formats de fichiers, tels que `.tar` (un format d'archive).

```python
pg_dump -U username -F t database_name > path_to_file/filename.tar
```

Ici, le drapeau `-F` indique à `pg_dump` que vous allez spécifier un format de sortie, tandis que `t` lui indique qu'il sera au format `.tar`.

## Comment restaurer une base de données

Vous pouvez restaurer une base de données à partir d'un fichier de sauvegarde en utilisant soit psql, soit l'utilitaire `pg_restore`. Celui que vous choisissez dépend du type de fichier à partir duquel vous restaurez la base de données.

1. Si vous avez sauvegardé la base de données dans un format texte brut, tel que `.sql`, utilisez psql.
   
2. Si vous avez sauvegardé la base de données dans un format d'archive, tel que `.tar`, utilisez `pg_restore`.
   

### Option 1 - Restaurer une base de données en utilisant psql

Pour restaurer une base de données à partir d'un fichier `.sql`, sur la ligne de commande (donc pas dans psql), utilisez `psql -U username -d database_name -f filename.sql`.

Vous pouvez utiliser la base de données `films_db` et le fichier `films.sql` que vous avez utilisés précédemment, ou créer un nouveau fichier de sauvegarde.

Créez une base de données vide pour que le fichier y restaure les données. Si vous utilisez `films.sql` pour restaurer `films_db`, la chose la plus simple pourrait être de supprimer `films_db` et de la recréer.

```python
DROP DATABASE films_db;

CREATE DATABASE films_db;
```

Dans un terminal séparé (pas dans psql), exécutez la commande suivante, en passant `postgres` comme nom d'utilisateur, et les noms de la base de données et du fichier de sauvegarde que vous utilisez.

```python
psql -U username -d database_name -f path_to_file/filename.sql
```

Le drapeau `-d` pointe psql vers une base de données spécifique, tandis que le drapeau `-f` indique à psql de lire depuis le fichier spécifié.

Si vous ne spécifiez pas de chemin pour le fichier de sauvegarde, psql cherchera le fichier dans le dernier répertoire dans lequel vous étiez avant de vous connecter à PostgreSQL.

Vous serez invité à entrer le mot de passe du superutilisateur `postgres` et verrez ensuite une série de commandes s'imprimer dans la ligne de commande pendant que psql recrée la base de données.

![Restauration d'une base de données en utilisant psql](https://www.freecodecamp.org/news/content/images/2022/06/image-52.png align="left")

*Restauration d'une base de données en utilisant psql*

Cette commande ignore toute erreur qui se produit pendant la restauration. Si vous voulez arrêter la restauration de la base de données si une erreur se produit, passez `--set ON_ERROR_STOP=on`.

```python
psql -U username -d database_name --set ON_ERROR_STOP=on -f filename.sql
```

### Option 2 - Restaurer une base de données en utilisant `pg_restore`

Pour restaurer une base de données en utilisant `pg_restore`, utilisez `pg_restore -U username -d database_name path_to_file/filename.tar`.

Créez une base de données vide pour que le fichier y restaure les données. Si vous restaurez `films_db` à partir d'un fichier `films.tar`, la chose la plus simple pourrait être de supprimer `films_db` et de la recréer.

```python
DROP DATABASE films_db;

CREATE DATABASE films_db;
```

Sur la ligne de commande (pas dans psql), exécutez la commande suivante, en passant `postgres` comme nom d'utilisateur, et les noms de la base de données et du fichier de sauvegarde que vous utilisez.

```python
pg_restore -U username -d database_name path_to_file/filename.tar
```

![Restauration d'une base de données en utilisant pg_restore](https://www.freecodecamp.org/news/content/images/2022/06/image-54.png align="left")

*Restauration d'une base de données en utilisant pg_restore*

Vous pouvez également passer le drapeau `-v` ou `--verbose` pour voir ce que `pg_restore` fait à chaque étape.

![Utilisation de pg_restore en mode verbeux](https://www.freecodecamp.org/news/content/images/2022/06/image-55.png align="left")

*Utilisation de pg_restore en mode verbeux*

## Comment quitter psql

Si vous avez terminé avec psql et que vous souhaitez en sortir, entrez `quit` ou `\q`.

```python
\q
```

Cela fermera l'application psql si vous l'utilisiez, ou vous ramènera à votre prompt de commande habituel si vous utilisiez psql depuis la ligne de commande.

## Où aller à partir de là

Il y a beaucoup plus de choses que vous pouvez faire avec psql, comme gérer des schémas, des rôles et des tablespaces. Mais ce guide devrait être suffisant pour vous aider à démarrer avec la gestion des bases de données PostgreSQL depuis la ligne de commande.

Si vous voulez en savoir plus sur PostgreSQL et psql, vous pourriez essayer la certification [Relational Database Certificate](https://www.freecodecamp.org/learn/relational-database/) de freeCodeCamp. La documentation officielle de [PostgreSQL](https://www.postgresql.org/docs/current/) est complète, et [PostgreSQL Tutorial](https://www.postgresqltutorial.com/postgresql-administration/psql-commands/) offre plusieurs tutoriels approfondis.

J'espère que vous trouverez ce guide utile alors que vous continuez à apprendre PostgreSQL et les bases de données relationnelles.