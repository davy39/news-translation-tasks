---
title: Comment joindre MySQL et PostgreSQL dans une vue matérialisée en temps réel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-03T15:18:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-join-mysql-and-postgres-in-a-live-materialized-view
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/how-to-join-mysql-and-postgres-in-a-live-materialized-view2.jpeg
tags:
- name: database
  slug: database
- name: Microservices
  slug: microservices
- name: MySQL
  slug: mysql
- name: postgres
  slug: postgres
seo_title: Comment joindre MySQL et PostgreSQL dans une vue matérialisée en temps
  réel
seo_desc: "By Bobby Iliev\nWhen you're working on a project that consists of a lot\
  \ of microservices, it'll likely also include multiple databases. \nFor example,\
  \ you might have a MySQL database and a PostgreSQL database, both running on separate\
  \ servers.\nUsually,..."
---

Par Bobby Iliev

Lorsque vous travaillez sur un projet composé de nombreux microservices, il est probable qu'il inclue également plusieurs bases de données. 

Par exemple, vous pourriez avoir une base de données [MySQL](https://www.mysql.com) et une base de données [PostgreSQL](https://www.postgresql.org), toutes deux exécutées sur des serveurs séparés.

Habituellement, pour joindre les données des deux bases de données, vous devriez introduire un nouveau microservice qui joindrait les données ensemble. Mais cela augmenterait la complexité du système.

Dans ce tutoriel, nous allons utiliser Materialize pour joindre MySQL et PostgreSQL dans une vue matérialisée en temps réel. Nous pourrons ensuite interroger directement cette vue et obtenir des résultats des deux bases de données en temps réel en utilisant SQL standard.  
  
[Materialize](https://github.com/MaterializeInc/materialize/) est une base de données de streaming source-disponible écrite en Rust qui maintient les résultats d'une requête SQL (une vue matérialisée) en mémoire à mesure que les données changent. 

Le tutoriel inclut un projet de démonstration que vous pouvez démarrer en utilisant `docker-compose`.

Le projet de démonstration que nous allons utiliser surveillera les commandes sur notre site web fictif. Il générera des événements qui pourraient, plus tard, être utilisés pour envoyer des notifications lorsqu'un panier a été abandonné pendant longtemps.

L'architecture du projet de démonstration est la suivante :

![mz-abandoned-cart-demo](https://user-images.githubusercontent.com/21223421/143267063-2dbb1ec2-d48d-4ba5-8da8-f0d9ac1404e4.png)

## Prérequis

  
Tous les services que nous allons utiliser dans la démonstration s'exécuteront à l'intérieur de conteneurs Docker, de cette manière vous n'aurez pas à installer de services supplémentaires sur votre ordinateur portable ou serveur autre que Docker et Docker Compose.  
  
Au cas où vous n'auriez pas encore Docker et Docker Compose installés, vous pouvez suivre les instructions officielles sur la manière de le faire ici :

* [Installer Docker](https://docs.docker.com/get-docker/)
* [Installer Docker Compose](https://docs.docker.com/compose/install/)

## Aperçu

Comme le montre le diagramme ci-dessus, nous aurons les composants suivants :

* Un service fictif pour générer continuellement des commandes.
* Les commandes seront stockées dans une **base de données MySQL**.
* À mesure que les écritures de la base de données se produisent, **Debezium** diffuse les changements depuis MySQL vers un sujet **Redpanda**.
* Nous aurons également une **base de données Postgres** où nous pouvons obtenir nos utilisateurs.
* Nous allons ensuite ingérer ce sujet Redpanda directement dans **Materialize** ainsi que les utilisateurs de la base de données Postgres.
* Dans Materialize, nous allons joindre nos commandes et utilisateurs ensemble, faire un peu de filtrage, et créer une vue matérialisée qui montre les informations sur les paniers abandonnés.
* Nous allons ensuite créer un sink pour envoyer les données des paniers abandonnés vers un nouveau sujet Redpanda.
* À la fin, nous allons utiliser **Metabase** pour visualiser les données.
* Vous pourriez, plus tard, utiliser les informations de ce nouveau sujet pour envoyer des notifications à vos utilisateurs et leur rappeler qu'ils ont un panier abandonné.

En tant que note à part ici, vous seriez parfaitement à l'aise en utilisant Kafka au lieu de Redpanda. J'aime simplement la simplicité que Redpanda apporte, car vous pouvez exécuter une seule instance Redpanda au lieu de tous les composants de Kafka.

## Comment exécuter la démonstration

Tout d'abord, commencez par cloner le dépôt :

```
git clone https://github.com/bobbyiliev/materialize-tutorials.git

```

Après cela, vous pouvez accéder au répertoire :

```
cd materialize-tutorials/mz-join-mysql-and-postgresql

```

Commençons par exécuter le conteneur Redpanda :

```
docker-compose up -d redpanda

```

Construisez les images :

```
docker-compose build

```

Enfin, démarrez tous les services :

```
docker-compose up -d

```

Pour lancer l'interface de ligne de commande Materialize, vous pouvez exécuter la commande suivante :

```
docker-compose run mzcli

```

Ce n'est qu'un raccourci vers un conteneur Docker avec `postgres-client` préinstallé. Si vous avez déjà `psql`, vous pourriez exécuter `psql -U materialize -h localhost -p 6875 materialize` à la place.

### Comment créer une source Kafka Materialize

Maintenant que vous êtes dans l'interface de ligne de commande Materialize, définissons les tables `orders` dans la base de données `mysql.shop` comme sources Redpanda :

```sql
CREATE SOURCE orders
FROM KAFKA BROKER 'redpanda:9092' TOPIC 'mysql.shop.orders'
FORMAT AVRO USING CONFLUENT SCHEMA REGISTRY 'http://redpanda:8081'
ENVELOPE DEBEZIUM;

```

Si vous deviez vérifier les colonnes disponibles de la source `orders` en exécutant l'instruction suivante :

```sql
SHOW COLUMNS FROM orders;

```

Vous pourriez voir que, comme Materialize extrait les données de schéma de message du registre Redpanda, il connaît les types de colonnes à utiliser pour chaque attribut :

```sql
    name      | nullable |   type
--------------+----------+-----------
 id           | f        | bigint
 user_id      | t        | bigint
 order_status | t        | integer
 price        | t        | numeric
 created_at   | f        | text
 updated_at   | t        | timestamp

```

### Comment créer des vues matérialisées

Ensuite, nous allons créer notre première vue matérialisée, pour obtenir toutes les données de la source Redpanda `orders` :

```sql
CREATE MATERIALIZED VIEW orders_view AS
SELECT * FROM orders;

```

```sql
CREATE MATERIALIZED VIEW abandoned_orders AS
    SELECT
        user_id,
        order_status,
        SUM(price) as revenue,
        COUNT(id) AS total
    FROM orders_view
    WHERE order_status=0
    GROUP BY 1,2;

```

Vous pouvez maintenant utiliser `SELECT * FROM abandoned_orders;` pour voir les résultats :

```sql
SELECT * FROM abandoned_orders;

```

Pour plus d'informations sur la création de vues matérialisées, consultez la section [Vues matérialisées](https://materialize.com/docs/sql/create-materialized-view/) de la documentation Materialize.

### Comment créer une source Postgres

Il existe deux façons de créer une source Postgres dans Materialize :

* En utilisant Debezium comme nous l'avons fait avec la source MySQL.
* En utilisant la source Materialize Postgres, qui vous permet de connecter Materialize directement à Postgres pour que vous n'ayez pas à utiliser Debezium.

Pour cette démonstration, nous allons utiliser la source Materialize Postgres juste pour montrer comment l'utiliser, mais n'hésitez pas à utiliser Debezium à la place.

Pour créer une source Materialize Postgres, exécutez l'instruction suivante :

```sql
CREATE MATERIALIZED SOURCE "mz_source" FROM POSTGRES
CONNECTION 'user=postgres port=5432 host=postgres dbname=postgres password=postgres'
PUBLICATION 'mz_source';

```

Un bref aperçu de l'instruction ci-dessus :

* `MATERIALIZED` : Matérialise les données de la source PostgreSQL. Toutes les données sont conservées en mémoire et rendent les sources directement sélectionnables.
* `mz_source` : Le nom de la source PostgreSQL.
* `CONNECTION` : Les paramètres de connexion PostgreSQL.
* `PUBLICATION` : La publication PostgreSQL, contenant les tables à diffuser vers Materialize.

Une fois que nous avons créé la source PostgreSQL, afin de pouvoir interroger les tables PostgreSQL, nous devrions créer des vues qui représentent les tables originales de la publication en amont.

Dans notre cas, nous n'avons qu'une seule table appelée `users`, donc l'instruction que nous devrions exécuter est :

```sql
CREATE VIEWS FROM SOURCE mz_source (users);

```

Pour voir les vues disponibles, exécutez l'instruction suivante :

```sql
SHOW FULL VIEWS;

```

Une fois cela fait, vous pouvez interroger les nouvelles vues directement :

```sql
SELECT * FROM users;

```

Ensuite, continuons et créons quelques vues supplémentaires.

### Comment créer un sink Kafka

Les [Sinks](https://materialize.com/docs/sql/create-sink/) vous permettent d'envoyer des données de Materialize vers une source externe.

Pour cette démonstration, nous allons utiliser [Redpanda](https://materialize.com/docs/third-party/redpanda/).

Redpanda est compatible avec l'API Kafka et Materialize peut traiter les données de la même manière qu'il traiterait les données d'une source Kafka.

Créons une vue matérialisée, qui contiendra toutes les commandes non payées de haut volume :

```sql
 CREATE MATERIALIZED VIEW high_value_orders AS
      SELECT
        users.id,
        users.email,
        abandoned_orders.revenue,
        abandoned_orders.total
      FROM users
      JOIN abandoned_orders ON abandoned_orders.user_id = users.id
      GROUP BY 1,2,3,4
      HAVING revenue > 2000;

```

Comme vous pouvez le voir, ici nous joignons en réalité la vue `users` qui ingère les données directement de notre source Postgres, et la vue `abandond_orders` qui ingère les données du sujet Redpanda, ensemble.

Créons un Sink où nous allons envoyer les données de la vue matérialisée ci-dessus :

```sql
CREATE SINK high_value_orders_sink
    FROM high_value_orders
    INTO KAFKA BROKER 'redpanda:9092' TOPIC 'high-value-orders-sink'
    FORMAT AVRO USING
    CONFLUENT SCHEMA REGISTRY 'http://redpanda:8081';

```

Maintenant, si vous deviez vous connecter au conteneur Redpanda et utiliser la commande `rpk topic consume`, vous pourriez lire les enregistrements du sujet.

Cependant, pour le moment, nous ne pourrons pas prévisualiser les résultats avec `rpk` car ils sont au format AVRO. Redpanda implémentera probablement cela à l'avenir, mais pour le moment, nous pouvons en fait diffuser le sujet vers Materialize pour confirmer le format.

Tout d'abord, obtenez le nom du sujet qui a été généré automatiquement :

```sql
SELECT topic FROM mz_kafka_sinks;

```

Sortie :

```sql
                              topic
-----------------------------------------------------------------
 high-volume-orders-sink-u12-1637586945-13670686352905873426

```

Pour plus d'informations sur la manière dont les noms des sujets sont générés, consultez la documentation [ici](https://materialize.com/docs/sql/create-sink/#kafka-sinks).

Ensuite, créez une nouvelle source matérialisée à partir de ce sujet Redpanda :

```sql
CREATE MATERIALIZED SOURCE high_volume_orders_test
FROM KAFKA BROKER 'redpanda:9092' TOPIC ' high-volume-orders-sink-u12-1637586945-13670686352905873426'
FORMAT AVRO USING CONFLUENT SCHEMA REGISTRY 'http://redpanda:8081';

```

Assurez-vous de changer le nom du sujet en conséquence !

Enfin, interrogez cette nouvelle vue matérialisée :

```sql
SELECT * FROM high_volume_orders_test LIMIT 2;

```

Maintenant que vous avez les données dans le sujet, vous pouvez avoir d'autres services se connecter à celui-ci et les consommer, puis déclencher des e-mails ou des alertes par exemple.

## Comment se connecter à Metabase

Pour accéder à l'instance [Metabase](https://materialize.com/docs/third-party/metabase/), visitez `http://localhost:3030` si vous exécutez la démonstration localement ou `http://your_server_ip:3030` si vous exécutez la démonstration sur un serveur. Suivez ensuite les étapes pour compléter la configuration de Metabase.

Assurez-vous de sélectionner Materialize comme source des données.

Une fois prêt, vous pourrez visualiser vos données comme vous le feriez avec une base de données PostgreSQL standard.

## Comment arrêter la démonstration

Pour arrêter tous les services, exécutez la commande suivante :

```
docker-compose down

```

## Conclusion

Comme vous pouvez le voir, ceci est un exemple très simple de l'utilisation de Materialize. Vous pouvez utiliser Materialize pour ingérer des données à partir de diverses sources et les diffuser vers diverses destinations.

## Ressources utiles :

* [`CREATE SOURCE: PostgreSQL`](https://materialize.com/docs/sql/create-source/postgres/)
* [`CREATE SOURCE`](https://materialize.com/docs/sql/create-source/)
* [`CREATE VIEWS`](https://materialize.com/docs/sql/create-views)
* [`SELECT`](https://materialize.com/docs/sql/select)