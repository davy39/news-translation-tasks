---
title: Comment créer et manipuler des bases de données SQL avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T19:24:57.000Z'
originalURL: https://freecodecamp.org/news/connect-python-with-sql
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Untitled-design-1-.png
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: Comment créer et manipuler des bases de données SQL avec Python
seo_desc: "By Craig Dickson\nPython and SQL are two of the most important languages\
  \ for Data Analysts. \nIn this article I will walk you through everything you need\
  \ to know to connect Python and SQL.\nYou'll learn how to pull data from relational\
  \ databases straigh..."
---

Par Craig Dickson

[Python](https://www.python.org/) et [SQL](https://en.wikipedia.org/wiki/SQL) sont deux des langages les plus importants pour les analystes de données. 

Dans cet article, je vais vous guider à travers tout ce que vous devez savoir pour connecter Python et SQL.

Vous apprendrez à extraire des données de bases de données relationnelles directement dans vos pipelines de machine learning, à stocker des données de votre application Python dans une base de données, ou tout autre cas d'utilisation que vous pourriez imaginer.

Ensemble, nous allons couvrir :
* Pourquoi apprendre à utiliser Python et SQL ensemble ?
* Comment configurer votre environnement Python et le serveur MySQL
* Se connecter au serveur MySQL dans Python
* Créer une nouvelle base de données
* Créer des tables et des relations entre tables
* Remplir les tables avec des données
* Lire des données
* Mettre à jour des enregistrements
* Supprimer des enregistrements
* Créer des enregistrements à partir de listes Python
* Créer des fonctions réutilisables pour tout cela à l'avenir

C'est beaucoup de choses très utiles et très intéressantes. Commençons !

Une petite note avant de commencer : il y a un Jupyter Notebook contenant tout le code utilisé dans ce tutoriel disponible dans [ce dépôt GitHub](https://github.com/thecraigd/Python_SQL). Il est fortement recommandé de coder en parallèle !

La base de données et le code SQL utilisés ici proviennent tous de ma série précédente [Introduction à SQL](https://towardsdatascience.com/tagged/sql-series) publiée sur [Towards Data Science](https://towardsdatascience.com/) ([contactez-moi](https://www.craigdoesdata.de/contact.html) si vous avez des problèmes pour voir les articles et je peux vous envoyer un lien pour les voir gratuitement). 

Si vous n'êtes pas familier avec SQL et les concepts derrière les bases de données relationnelles, je vous orienterais vers [cette série](https://towardsdatascience.com/tagged/sql-series) (plus il y a bien sûr une énorme quantité de choses disponibles ici sur [freeCodeCamp](https://www.freecodecamp.org/news/search/?query=sql) !)

## Pourquoi Python avec SQL ?

Pour les analystes de données et les scientifiques des données, Python a de nombreux avantages. Une énorme gamme de bibliothèques open-source en font un outil incroyablement utile pour tout analyste de données. 

Nous avons [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) et [Vaex](https://vaex.readthedocs.io/en/latest/) pour l'analyse de données, [Matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/) et [Bokeh](https://bokeh.org/) pour la visualisation, et [TensorFlow](https://www.freecodecamp.org/news/p/5fe3a414-f0df-488b-9402-44d8edc12652/www.tensorflow.org), [scikit-learn](https://scikit-learn.org/stable/) et [PyTorch](https://pytorch.org/) pour les applications de machine learning (plus beaucoup d'autres).

Avec sa courbe d'apprentissage (relativement) facile et sa polyvalence, il n'est pas surprenant que Python soit l'un des [langages de programmation à la croissance la plus rapide](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) qui existent.

Donc, si nous utilisons Python pour l'analyse de données, il est utile de se demander - d'où viennent toutes ces données ? 

Bien qu'il existe une grande variété de sources pour les ensembles de données, dans de nombreux cas - en particulier dans les entreprises - les données sont stockées dans une base de données relationnelle. Les bases de données relationnelles sont un moyen extrêmement efficace, puissant et largement utilisé pour [créer, lire, mettre à jour et supprimer](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) des données de toutes sortes. 

Les systèmes de gestion de bases de données relationnelles (SGBDR) les plus largement utilisés - [Oracle](https://www.oracle.com/database/), [MySQL](https://www.mysql.com/), [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server), [PostgreSQL](https://www.oracle.com/database/what-is-a-relational-database/), [IBM DB2](https://en.wikipedia.org/wiki/IBM_DB2) - utilisent tous le [langage de requête structuré](https://en.wikipedia.org/wiki/SQL) (SQL) pour accéder et apporter des modifications aux données. 

Notez que chaque SGBDR utilise une version légèrement différente de [SQL](https://towardsdatascience.com/the-many-flavours-of-sql-7b7da5d56c1e), donc le code SQL écrit pour l'un ne fonctionnera généralement pas dans un autre sans (normalement assez mineures) modifications. Mais les concepts, structures et opérations sont largement identiques.

Cela signifie que pour un analyste de données en activité, une solide compréhension de SQL est extrêmement importante. Savoir comment utiliser Python et SQL ensemble vous donnera encore plus d'avantages lorsqu'il s'agit de travailler avec vos données.

Le reste de cet article sera consacré à vous montrer exactement comment nous pouvons faire cela.

## Pour commencer

### Exigences et installation

Pour coder en suivant ce tutoriel, vous aurez besoin de votre propre [environnement Python](https://www.python.org/downloads/) configuré.

J'utilise [Anaconda](https://www.anaconda.com/), mais il existe de nombreuses façons de faire cela. Il suffit de chercher "comment installer Python" si vous avez besoin d'aide supplémentaire. Vous pouvez également utiliser [Binder](https://mybinder.org/) pour coder en suivant le [Jupyter Notebook](https://github.com/thecraigd/Python_SQL) associé. 

Nous allons utiliser [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) car il est gratuit et largement utilisé dans l'industrie. Si vous utilisez Windows, [ce guide](https://www.youtube.com/watch?v=2HQC94la6go) vous aidera à vous installer. Voici des guides pour les utilisateurs de [Mac](https://www.youtube.com/watch?v=5BQ5GvjiAR4) et de [Linux](https://www.youtube.com/watch?v=0o0tSaVQfV4) également (bien que cela puisse varier selon la distribution Linux).

Une fois que vous avez tout configuré, nous devons les faire communiquer entre eux. 

Pour cela, nous devons installer la bibliothèque Python [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/). Pour ce faire, suivez [les instructions](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html), ou utilisez simplement pip :

```terminal
pip install mysql-connector-python
```

Nous allons également utiliser [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html), alors assurez-vous de l'avoir installé également.

```terminal
pip install pandas
```

### Importation des bibliothèques

Comme pour chaque projet en Python, la toute première chose que nous voulons faire est d'importer nos bibliothèques. 

Il est considéré comme une bonne pratique d'importer toutes les bibliothèques que nous allons utiliser au début du projet, afin que les personnes lisant ou révisant notre code sachent à peu près ce qui va suivre, sans surprises.

Pour ce tutoriel, nous n'allons utiliser que deux bibliothèques - [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) et [pandas](https://pandas.pydata.org/).

```python
import mysql.connector
from mysql.connector import Error
import pandas as pd
```

Nous importons la fonction Error séparément afin d'avoir un accès facile pour nos fonctions.

## Connexion au serveur MySQL

À ce stade, nous devrions avoir [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) configuré sur notre système. Maintenant, nous devons écrire du code en Python qui nous permet d'établir une connexion à ce serveur.

```python
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connexion à la base de données MySQL réussie")
    except Error as err:
        print(f"Erreur : '{err}'")

    return connection
```

Créer une fonction réutilisable pour du code comme celui-ci est une bonne pratique, afin que nous puissions l'utiliser encore et encore avec un minimum d'effort. Une fois que cela est écrit une fois, vous pouvez le réutiliser dans tous vos projets futurs également, donc votre futur vous en sera reconnaissant !

Passons en revue cela ligne par ligne pour comprendre ce qui se passe ici :

La première ligne est nous nommant la fonction (create_server_connection) et nommant les arguments que cette fonction prendra (host_name, user_name et user_password). 

La ligne suivante ferme toute connexion existante afin que le serveur ne soit pas confus avec plusieurs connexions ouvertes.

Ensuite, nous utilisons un bloc [try-except](https://www.w3schools.com/python/python_try_except.asp) de Python pour gérer toute erreur potentielle. La première partie tente de créer une connexion au serveur en utilisant la méthode [mysql.connector.connect()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysql-connector-connect.html) en utilisant les détails spécifiés par l'utilisateur dans les arguments. Si cela fonctionne, la fonction imprime un petit message de succès. 

La partie except du bloc imprime l'erreur que le serveur MySQL retourne, dans le cas malheureux où il y a une erreur. 

Enfin, si la connexion est réussie, la fonction retourne un [objet de connexion](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html). 

Nous utilisons cela en pratique en assignant la sortie de la fonction à une variable, qui devient alors notre objet de connexion. Nous pouvons ensuite appliquer d'autres méthodes (comme [cursor](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)) et créer d'autres objets utiles.

```python
connection = create_server_connection("localhost", "root", pw)
```

Cela devrait produire un message de succès :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-146.png)
_Hourra !_

### Créer une nouvelle base de données

Maintenant que nous avons établi une connexion, notre prochaine étape est de créer une nouvelle base de données sur notre serveur. 

Dans ce tutoriel, nous ne ferons cela qu'une seule fois, mais nous allons à nouveau écrire cela comme une fonction réutilisable afin d'avoir une fonction utile que nous pourrons réutiliser pour des projets futurs.

```python
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Base de données créée avec succès")
    except Error as err:
        print(f"Erreur : '{err}'")
```

Cette fonction prend deux arguments, connection (notre objet de connexion) et query (une requête SQL que nous allons écrire à l'étape suivante). Elle exécute la requête dans le serveur via la connexion.

Nous utilisons la méthode [cursor](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html) sur notre objet de connexion pour créer un objet curseur (MySQL Connector utilise un [paradigme de programmation orientée objet](https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/), donc il y a beaucoup d'objets héritant des propriétés des objets parents). 

Cet objet curseur a des méthodes telles que [execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html), [executemany](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html) (que nous allons utiliser dans ce tutoriel) ainsi que plusieurs autres méthodes utiles. 

Si cela aide, nous pouvons penser à l'objet curseur comme nous donnant accès au curseur clignotant dans une fenêtre de terminal du serveur MySQL.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-148.png)
_Vous savez, celui-ci._

Ensuite, nous définissons une requête pour créer la base de données et appelons la fonction :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-149.png)

Toutes les requêtes SQL utilisées dans ce tutoriel sont expliquées dans ma série de tutoriels [Introduction à SQL](https://towardsdatascience.com/tagged/sql-series), et le code complet peut être trouvé dans le Jupyter Notebook associé dans [ce dépôt GitHub](https://github.com/thecraigd/Python_SQL), donc je ne fournirai pas d'explications sur ce que fait le code SQL dans ce tutoriel.

C'est peut-être la requête SQL la plus simple possible, cependant. Si vous pouvez lire l'anglais, vous pouvez probablement comprendre ce qu'elle fait ! 

L'exécution de la fonction create_database avec les arguments ci-dessus entraîne la création d'une base de données appelée 'school' dans notre serveur.

Pourquoi notre base de données s'appelle-t-elle 'school' ? Peut-être serait-il bon de regarder plus en détail ce que nous allons implémenter dans ce tutoriel.

### Notre base de données

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ERD.png)
_Le diagramme de relation d'entités pour notre base de données._

En suivant l'exemple de ma [série précédente](https://towardsdatascience.com/tagged/sql-series), nous allons implémenter la base de données pour l'International Language School - une école de formation linguistique fictive qui fournit des cours de langue professionnels à des clients d'entreprise. 

Ce [diagramme de relation d'entités](https://www.lucidchart.com/pages/er-diagrams) (ERD) présente nos entités (Teacher, Client, Course et Participant) et définit les relations entre elles.

Toutes les informations concernant ce qu'est un ERD et ce qu'il faut considérer lors de sa création et de la conception d'une base de données peuvent être trouvées dans [cet article](https://towardsdatascience.com/designing-a-relational-database-and-creating-an-entity-relationship-diagram-89c1c19320b2). 

Le code SQL brut, les exigences de la base de données et les données à insérer dans la base de données sont tous contenus dans [ce dépôt GitHub](https://github.com/thecraigd/SQL_School_Tutorial), mais vous les verrez tous au fur et à mesure de ce tutoriel.

### Connexion à la base de données

Maintenant que nous avons créé une base de données dans MySQL Server, nous pouvons modifier notre fonction create_server_connection pour nous connecter directement à cette base de données. 

Notez qu'il est possible - et même courant - d'avoir plusieurs bases de données sur un seul serveur MySQL, donc nous voulons toujours et automatiquement nous connecter à la base de données qui nous intéresse. 

Nous pouvons faire cela comme suit :

```python
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connexion à la base de données MySQL réussie")
    except Error as err:
        print(f"Erreur : '{err}'")

    return connection
```

C'est exactement la même fonction, mais maintenant nous prenons un argument supplémentaire - le nom de la base de données - et nous le passons comme argument à la méthode connect().

### Créer une fonction d'exécution de requête

La dernière fonction que nous allons créer (pour l'instant) est extrêmement vitale - une fonction d'exécution de requête. Celle-ci va prendre nos requêtes SQL, stockées en Python sous forme de chaînes de caractères, et les transmettre à la méthode [cursor.execute()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html) pour les exécuter sur le serveur. 

```python
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Requête réussie")
    except Error as err:
        print(f"Erreur : '{err}'")
```

Cette fonction est exactement la même que notre fonction create_database de tout à l'heure, sauf qu'elle utilise la méthode [connection.commit()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html) pour s'assurer que les commandes détaillées dans nos requêtes SQL sont implémentées. 

C'est cette fonction qui sera notre cheval de bataille, que nous utiliserons (avec create_db_connection) pour créer des tables, établir des relations entre ces tables, remplir les tables avec des données, et mettre à jour et supprimer des enregistrements dans notre base de données.

Si vous êtes un expert en SQL, cette fonction vous permettra d'exécuter toutes les commandes et requêtes complexes que vous pourriez avoir sous la main, directement à partir d'un script Python. Cela peut être un outil très puissant pour gérer vos données.

## Créer des tables

Maintenant, nous sommes prêts à commencer à exécuter des commandes SQL dans notre serveur et à commencer à construire notre base de données. La première chose que nous voulons faire est de créer les tables nécessaires. 

Commençons par notre table Teacher :

```python
create_teacher_table = """
CREATE TABLE teacher (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  language_2 VARCHAR(3),
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """

connection = create_db_connection("localhost", "root", pw, db) # Connexion à la base de données
execute_query(connection, create_teacher_table) # Exécution de notre requête définie
```

Tout d'abord, nous assignons notre commande SQL (expliquée en détail [ici](https://towardsdatascience.com/coding-and-implementing-a-relational-database-using-mysql-d9bc69be90f5)) à une variable avec un nom approprié. 

Dans ce cas, nous utilisons la notation [triple quote de Python pour les chaînes de caractères multi-lignes](https://developers.google.com/edu/python/strings) pour stocker notre requête SQL, puis nous la transmettons à notre fonction execute_query pour l'implémenter.

Notez que ce formatage multi-lignes est purement pour le bénéfice des humains lisant notre code. Ni SQL ni Python ne 'se soucient' si la commande SQL est étalée comme cela. Tant que la syntaxe est correcte, les deux langages l'accepteront. 

Pour le bénéfice des humains qui liront votre code, cependant, (même si ce ne sera que vous dans le futur !) il est très utile de faire cela pour rendre le code plus lisible et compréhensible. 

Il en va de même pour la CAPITALISATION des opérateurs en SQL. Il s'agit d'une convention largement utilisée qui est fortement recommandée, mais le logiciel qui exécute le code est insensible à la casse et traitera 'CREATE TABLE teacher' et 'create table teacher' comme des commandes identiques. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-151.png)

L'exécution de ce code nous donne nos messages de succès. Nous pouvons également vérifier cela dans le client de ligne de commande MySQL Server :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-152.png)

Super ! Maintenant, créons les tables restantes. 

```python
create_client_table = """
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40) NOT NULL,
  address VARCHAR(60) NOT NULL,
  industry VARCHAR(20)
);
 """

create_participant_table = """
CREATE TABLE participant (
  participant_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20),
  client INT
);
"""

create_course_table = """
CREATE TABLE course (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(40) NOT NULL,
  language VARCHAR(3) NOT NULL,
  level VARCHAR(2),
  course_length_weeks INT,
  start_date DATE,
  in_school BOOLEAN,
  teacher INT,
  client INT
);
"""


connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_client_table)
execute_query(connection, create_participant_table)
execute_query(connection, create_course_table)
```

Cela crée les quatre tables nécessaires pour nos quatre entités. 

Maintenant, nous voulons définir les relations entre elles et créer une table supplémentaire pour gérer la relation plusieurs-à-plusieurs entre les tables participant et course (voir [ici](https://towardsdatascience.com/designing-a-relational-database-and-creating-an-entity-relationship-diagram-89c1c19320b2) pour plus de détails). 

Nous faisons cela de la même manière :

```python
alter_participant = """
ALTER TABLE participant
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""

alter_course = """
ALTER TABLE course
ADD FOREIGN KEY(teacher)
REFERENCES teacher(teacher_id)
ON DELETE SET NULL;
"""

alter_course_again = """
ALTER TABLE course
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""

create_takescourse_table = """
CREATE TABLE takes_course (
  participant_id INT,
  course_id INT,
  PRIMARY KEY(participant_id, course_id),
  FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
  FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, alter_participant)
execute_query(connection, alter_course)
execute_query(connection, alter_course_again)
execute_query(connection, create_takescourse_table)
```

Maintenant, nos tables sont créées, avec les contraintes appropriées, la clé primaire et les relations de clé étrangère.

### Remplir les tables

L'étape suivante consiste à ajouter des enregistrements aux tables. Nous utilisons à nouveau execute_query pour alimenter nos commandes SQL existantes dans le serveur. Commençons à nouveau par la table Teacher.

```python
pop_teacher = """
INSERT INTO teacher VALUES
(1,  'James', 'Smith', 'ENG', NULL, '1985-04-20', 12345, '+491774553676'),
(2, 'Stefanie',  'Martin',  'FRA', NULL,  '1970-02-17', 23456, '+491234567890'), 
(3, 'Steve', 'Wang',  'MAN', 'ENG', '1990-11-12', 34567, '+447840921333'),
(4, 'Friederike',  'Müller-Rossi', 'DEU', 'ITA', '1987-07-07',  45678, '+492345678901'),
(5, 'Isobel', 'Ivanova', 'RUS', 'ENG', '1963-05-30',  56789, '+491772635467'),
(6, 'Niamh', 'Murphy', 'ENG', 'IRI', '1995-09-08',  67890, '+491231231232');
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, pop_teacher)
```

Cela fonctionne-t-il ? Nous pouvons vérifier à nouveau dans notre client de ligne de commande MySQL :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-153.png)
_Cela a l'air bien !_

Maintenant, remplissons les tables restantes.

```python
pop_client = """
INSERT INTO client VALUES
(101, 'Big Business Federation', '123 Falschungstraße, 10999 Berlin', 'NGO'),
(102, 'eCommerce GmbH', '27 Ersatz Allee, 10317 Berlin', 'Retail'),
(103, 'AutoMaker AG',  '20 Künstlichstraße, 10023 Berlin', 'Auto'),
(104, 'Banko Bank',  '12 Betrugstraße, 12345 Berlin', 'Banking'),
(105, 'WeMoveIt GmbH', '138 Arglistweg, 10065 Berlin', 'Logistics');
"""

pop_participant = """
INSERT INTO participant VALUES
(101, 'Marina', 'Berg','491635558182', 101),
(102, 'Andrea', 'Duerr', '49159555740', 101),
(103, 'Philipp', 'Probst',  '49155555692', 102),
(104, 'René',  'Brandt',  '4916355546',  102),
(105, 'Susanne', 'Shuster', '49155555779', 102),
(106, 'Christian', 'Schreiner', '49162555375', 101),
(107, 'Harry', 'Kim', '49177555633', 101),
(108, 'Jan', 'Nowak', '49151555824', 101),
(109, 'Pablo', 'Garcia',  '49162555176', 101),
(110, 'Melanie', 'Dreschler', '49151555527', 103),
(111, 'Dieter', 'Durr',  '49178555311', 103),
(112, 'Max', 'Mustermann', '49152555195', 104),
(113, 'Maxine', 'Mustermann', '49177555355', 104),
(114, 'Heiko', 'Fleischer', '49155555581', 105);
"""

pop_course = """
INSERT INTO course VALUES
(12, 'English for Logistics', 'ENG', 'A1', 10, '2020-02-01', TRUE,  1, 105),
(13, 'Beginner English', 'ENG', 'A2', 40, '2019-11-12',  FALSE, 6, 101),
(14, 'Intermediate English', 'ENG', 'B2', 40, '2019-11-12', FALSE, 6, 101),
(15, 'Advanced English', 'ENG', 'C1', 40, '2019-11-12', FALSE, 6, 101),
(16, 'Mandarin für Autoindustrie', 'MAN', 'B1', 15, '2020-01-15', TRUE, 3, 103),
(17, 'Français intermédiaire', 'FRA', 'B1',  18, '2020-04-03', FALSE, 2, 101),
(18, 'Deutsch für Anfänger', 'DEU', 'A2', 8, '2020-02-14', TRUE, 4, 102),
(19, 'Intermediate English', 'ENG', 'B2', 10, '2020-03-29', FALSE, 1, 104),
(20, 'Fortgeschrittenes Russisch', 'RUS', 'C1',  4, '2020-04-08',  FALSE, 5, 103);
"""

pop_takescourse = """
INSERT INTO takes_course VALUES
(101, 15),
(101, 17),
(102, 17),
(103, 18),
(104, 18),
(105, 18),
(106, 13),
(107, 13),
(108, 13),
(109, 14),
(109, 15),
(110, 16),
(110, 20),
(111, 16),
(114, 12),
(112, 19),
(113, 19);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, pop_client)
execute_query(connection, pop_participant)
execute_query(connection, pop_course)
execute_query(connection, pop_takescourse)
```

Incroyable ! Nous avons maintenant créé une base de données complète avec des relations, des contraintes et des enregistrements dans MySQL, en utilisant uniquement des commandes Python. 

Nous avons passé en revue chaque étape pour garder cela compréhensible. Mais à ce stade, vous pouvez voir que tout cela pourrait très facilement être écrit dans un seul script Python et exécuté en une seule commande dans le terminal. C'est puissant.

## Lire des données 

Maintenant, nous avons une base de données fonctionnelle avec laquelle travailler. En tant qu'analyste de données, vous serez probablement en contact avec des bases de données existantes dans les organisations où vous travaillez. Il sera très utile de savoir comment extraire des données de ces bases de données afin qu'elles puissent ensuite être alimentées dans votre pipeline de données Python. C'est ce sur quoi nous allons travailler ensuite.

Pour cela, nous aurons besoin d'une fonction supplémentaire, cette fois en utilisant [cursor.fetchall()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html) au lieu de [cursor.commit()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html). Avec cette fonction, nous lisons des données de la base de données et ne ferons aucune modification.

```python
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Erreur : '{err}'")
```

Encore une fois, nous allons implémenter cela de manière très similaire à execute_query. Essayons-le avec une requête simple pour voir comment cela fonctionne.

```python
q1 = """
SELECT *
FROM teacher;
"""

connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q1)

for result in results:
  print(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-154.png)

Exactement ce à quoi nous nous attendions. La fonction fonctionne également avec des requêtes plus complexes, comme celle-ci impliquant une [JOIN](https://www.w3schools.com/sql/sql_join.asp) sur les tables course et client.

```python
q5 = """
SELECT course.course_id, course.course_name, course.language, client.client_name, client.address
FROM course
JOIN client
ON course.client = client.client_id
WHERE course.in_school = FALSE;
"""

connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q5)

for result in results:
  print(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-155.png)

Très bien. 

Pour nos pipelines et flux de travail de données en Python, nous pourrions vouloir obtenir ces résultats dans différents formats pour les rendre plus utiles ou prêts à être manipulés. 

Passons en revue quelques exemples pour voir comment nous pouvons faire cela.

### Formater la sortie en une liste

```python
# Initialiser une liste vide
from_db = []

# Boucler sur les résultats et les ajouter à notre liste

# Retourne une liste de tuples
for result in results:
  result = result
  from_db.append(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-156.png)

### Formater la sortie en une liste de listes

```python
# Retourne une liste de listes
from_db = []

for result in results:
  result = list(result)
  from_db.append(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-157.png)

### Formater la sortie en un [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

Pour les analystes de données utilisant Python, [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) est notre vieil ami beau et fiable. Il est très simple de convertir la sortie de notre base de données en un DataFrame, et à partir de là, les possibilités sont infinies !

```python
# Retourne une liste de listes puis crée un pandas DataFrame
from_db = []

for result in results:
  result = list(result)
  from_db.append(result)


columns = ["course_id", "course_name", "language", "client_name", "address"]
df = pd.DataFrame(from_db, columns=columns)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-158.png)

Espérons que vous pouvez voir les possibilités qui s'offrent à vous ici. Avec seulement quelques lignes de code, nous pouvons facilement extraire toutes les données que nous pouvons gérer des bases de données relationnelles où elles résident, et les intégrer dans nos pipelines d'analyse de données de pointe. C'est vraiment utile.

## Mettre à jour des enregistrements

Lorsque nous maintenons une base de données, nous devons parfois apporter des modifications aux enregistrements existants. Dans cette section, nous allons voir comment faire cela.

Disons que l'ILS est informée qu'un de ses clients existants, la Big Business Federation, déménage ses bureaux au 23 Fingiertweg, 14534 Berlin. Dans ce cas, l'administrateur de la base de données (c'est nous !) devra apporter quelques modifications. 

Heureusement, nous pouvons faire cela avec notre fonction execute_query ainsi que l'instruction SQL [UPDATE](https://dev.mysql.com/doc/refman/8.0/en/update.html).

```python
update = """
UPDATE client 
SET address = '23 Fingiertweg, 14534 Berlin' 
WHERE client_id = 101;
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, update)
```

Notez que la clause WHERE est très importante ici. Si nous exécutons cette requête sans la clause WHERE, alors toutes les adresses de tous les enregistrements dans notre table Client seraient mises à jour pour 23 Fingiertweg. Ce n'est absolument pas ce que nous cherchons à faire.

Notez également que nous avons utilisé "WHERE client_id = 101" dans la requête UPDATE. Il aurait également été possible d'utiliser "WHERE client_name = 'Big Business Federation'" ou "WHERE address = '123 Falschungstraße, 10999 Berlin'" ou même "WHERE address LIKE '%Falschung%'". 

L'important est que la clause WHERE nous permet d'identifier de manière unique l'enregistrement (ou les enregistrements) que nous voulons mettre à jour.

## Supprimer des enregistrements

Il est également possible d'utiliser notre fonction execute_query pour supprimer des enregistrements, en utilisant [DELETE](https://dev.mysql.com/doc/refman/8.0/en/delete.html). 

Lorsque nous utilisons SQL avec des bases de données relationnelles, nous devons être prudents avec l'opérateur DELETE. Ce n'est pas Windows, il n'y a pas de pop-up d'avertissement 'Êtes-vous sûr de vouloir supprimer cela ?', et il n'y a pas de corbeille. Une fois que nous supprimons quelque chose, c'est vraiment parti.

Cela dit, nous devons vraiment supprimer des choses parfois. Alors, regardons cela en supprimant un cours de notre table Course. 

Tout d'abord, rappelons-nous quels cours nous avons.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-174.png)

Disons que le cours 20, 'Fortgeschrittenes Russisch' (c'est-à-dire 'Russe avancé' pour vous et moi), touche à sa fin, donc nous devons le supprimer de notre base de données.

À ce stade, vous ne serez absolument pas surpris de la manière dont nous faisons cela - enregistrer la commande SQL sous forme de chaîne de caractères, puis l'alimenter dans notre fonction execute_query.

```python
delete_course = """
DELETE FROM course 
WHERE course_id = 20;
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, delete_course)
```

Vérifions pour confirmer que cela a eu l'effet souhaité :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-175.png)

'Russe avancé' a disparu, comme nous nous y attendions. 

Cela fonctionne également avec la suppression de colonnes entières en utilisant la commande [DROP COLUMN](https://www.w3schools.com/sql/sql_ref_drop_column.asp) et de tables entières en utilisant la commande [DROP TABLE](https://www.w3schools.com/sql/sql_ref_drop_table.asp), mais nous ne les couvrirons pas dans ce tutoriel. 

Allez-y et expérimentez avec eux, cependant - cela n'a pas d'importance si vous supprimez une colonne ou une table d'une base de données pour une école fictive, et c'est une bonne idée de se familiariser avec ces commandes avant de passer à un environnement de production.

### Oh [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

À ce stade, nous sommes maintenant capables de compléter les quatre opérations majeures pour le stockage de données persistant.

Nous avons appris comment :
* Créer - des bases de données, des tables et des enregistrements entièrement nouveaux
* Lire - extraire des données d'une base de données, et stocker ces données dans plusieurs formats
* Mettre à jour - apporter des modifications aux enregistrements existants dans la base de données
* Supprimer - retirer des enregistrements qui ne sont plus nécessaires

Ce sont des choses fantastiquement utiles à savoir faire. 

Avant de terminer ici, nous avons une autre compétence très utile à apprendre.

## Créer des enregistrements à partir de listes

Nous avons vu lors du remplissage de nos tables que nous pouvons utiliser la commande SQL [INSERT](https://dev.mysql.com/doc/refman/8.0/en/insert.html) dans notre fonction execute_query pour insérer des enregistrements dans notre base de données. 

Étant donné que nous utilisons Python pour manipuler notre base de données SQL, il serait utile de pouvoir prendre une structure de données Python (comme une [liste](https://www.w3schools.com/python/python_lists.asp)) et l'insérer directement dans notre base de données.

Cela pourrait être utile lorsque nous voulons stocker des journaux d'activité des utilisateurs sur une application de médias sociaux que nous avons écrite en Python, ou des entrées d'utilisateurs dans un Wiki que nous avons construit, par exemple. Il y a autant d'utilisations possibles pour cela que vous pouvez imaginer.  

Cette méthode est également plus sécurisée si notre base de données est ouverte à nos utilisateurs à un moment donné, car elle aide à prévenir les attaques par [injection SQL](https://en.wikipedia.org/wiki/SQL_injection), qui peuvent [endommager ou même détruire](https://www.lucidchart.com/pages/er-diagrams) notre base de données entière.

Pour ce faire, nous allons écrire une fonction utilisant la méthode [executemany()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html), au lieu de la méthode plus simple [execute()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html) que nous avons utilisée jusqu'à présent.

```python
def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Requête réussie")
    except Error as err:
        print(f"Erreur : '{err}'")
```

Maintenant que nous avons la fonction, nous devons définir une commande SQL ('sql') et une liste contenant les valeurs que nous souhaitons entrer dans la base de données ('val'). Les valeurs doivent être stockées sous forme de [liste](https://www.w3schools.com/python/python_lists.asp) de [tuples](https://www.w3schools.com/python/python_tuples.asp), ce qui est une manière assez courante de stocker des données en Python.

Pour ajouter deux nouveaux enseignants à la base de données, nous pouvons écrire un code comme celui-ci :

```python
sql = '''
    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    
val = [
    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
]
```

Remarquez ici que dans le code 'sql', nous utilisons '%s' comme espace réservé pour notre valeur. La ressemblance avec le ['%s' espace réservé](https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting/48660475) pour une chaîne de caractères en Python est purement fortuite (et franchement, très confuse), nous voulons utiliser '%s' pour tous les types de données (chaînes de caractères, entiers, dates, etc.) avec le connecteur MySQL Python. 

Vous pouvez voir un certain nombre de questions sur [Stackoverflow](https://stackoverflow.com/questions/20818155/not-all-parameters-were-used-in-the-sql-statement-python-mysql/20818201) où quelqu'un s'est trompé et a essayé d'utiliser des ['%d' espaces réservés](https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting/48660475) pour les entiers parce qu'il est habitué à le faire en Python. Cela ne fonctionnera pas ici - nous devons utiliser un '%s' pour chaque colonne à laquelle nous voulons ajouter une valeur.

La fonction executemany prend ensuite chaque tuple dans notre liste 'val' et insère la valeur pertinente pour cette colonne à la place de l'espace réservé et exécute la commande SQL pour chaque tuple contenu dans la liste.

Cela peut être effectué pour plusieurs lignes de données, tant qu'elles sont formatées correctement. Dans notre exemple, nous allons simplement ajouter deux nouveaux enseignants, à des fins d'illustration, mais en principe, nous pouvons en ajouter autant que nous le souhaitons. 

Allons-y et exécutons cette requête et ajoutons les enseignants à notre base de données.

```python
connection = create_db_connection("localhost", "root", pw, db)
execute_list_query(connection, sql, val)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-177.png)

Bienvenue à l'ILS, Hank et Sue !

C'est encore une autre fonction profondément utile, nous permettant de prendre des données générées dans nos scripts et applications Python, et de les entrer directement dans notre base de données. 

## Conclusion

Nous avons couvert beaucoup de terrain dans ce tutoriel. 

Nous avons appris comment utiliser Python et MySQL Connector pour créer une base de données entièrement nouvelle dans MySQL Server, créer des tables dans cette base de données, définir les relations entre ces tables, et les remplir avec des données. 

Nous avons couvert comment [Créer, Lire, Mettre à jour et Supprimer](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) des données dans notre base de données.

Nous avons vu comment extraire des données de bases de données existantes et les charger dans des DataFrames pandas, prêts pour l'analyse et d'autres travaux tirant parti de toutes les possibilités offertes par la [pile PyData](https://www.pluralsight.com/guides/a-lap-around-the-pydata-stack). 

Dans l'autre sens, nous avons également appris comment prendre des données générées par nos scripts et applications Python, et les écrire dans une base de données où elles peuvent être stockées en toute sécurité pour une récupération et une manipulation ultérieures.

J'espère que ce tutoriel vous a aidé à voir comment nous pouvons utiliser Python et SQL ensemble pour pouvoir manipuler les données encore plus efficacement !

_Si vous souhaitez voir plus de mes projets et travaux, veuillez visiter mon site web à l'adresse [craigdoesdata.de](https://www.craigdoesdata.de/). Si vous avez des commentaires sur ce tutoriel, veuillez [me contacter](https://www.craigdoesdata.de/contact.html) directement - tous les commentaires sont chaleureusement accueillis !_

![Image](https://www.freecodecamp.org/news/content/images/2020/08/logo.png)