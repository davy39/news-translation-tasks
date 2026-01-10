---
title: Comment produire et consommer des flux de données directement via Cypher avec
  les procédures Streams
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-09T17:13:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-produce-and-consume-data-streams-directly-via-cypher-with-streams-procedures-52cbc5f543f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*47Ktwi-Gdj5S7keZpiteZA.gif
tags:
- name: Apache Kafka
  slug: apache-kafka
- name: data
  slug: data
- name: Neo4j
  slug: neo4j
- name: streaming
  slug: streaming
- name: 'tech '
  slug: tech
seo_title: Comment produire et consommer des flux de données directement via Cypher
  avec les procédures Streams
seo_desc: 'By Andrea Santurbano

  Leveraging Neo4j Streams — Part 3

  This article is the third part of the Leveraging Neo4j Streams series (Part 1 is
  here, Part 2 is here). In it, I’ll show you how to bring Neo4j into your Apache
  Kafka flow by using the streams pr...'
---

Par Andrea Santurbano

#### Tirer parti de Neo4j Streams — Partie 3

Cet article est la troisième partie de la série **Tirer parti de Neo4j Streams** (la partie 1 est [ici](https://medium.freecodecamp.org/how-to-leverage-neo4j-streams-and-build-a-just-in-time-data-warehouse-64adf290f093), la partie 2 est [ici](https://medium.freecodecamp.org/how-to-ingest-data-into-neo4j-from-a-kafka-stream-a34f574f5655)). Dans cet article, je vais vous montrer comment intégrer Neo4j dans votre flux **Apache Kafka** en utilisant les procédures de flux disponibles avec [**Neo4j Streams**](https://medium.com/neo4j/a-new-neo4j-integration-with-apache-kafka-6099c14851d2).

Afin de montrer comment les intégrer, simplifier l'intégration et vous permettre de tester l'ensemble du projet manuellement, j'utiliserai [**Apache Zeppelin**](https://towardsdatascience.com/building-a-graph-data-pipeline-with-zeppelin-spark-and-neo4j-8b6b83f4fb70), un exécuteur de notebooks qui permet simplement de [interagir nativement avec Neo4j](https://towardsdatascience.com/building-a-graph-data-pipeline-with-zeppelin-spark-and-neo4j-8b6b83f4fb70).

### Qu'est-ce qu'une procédure stockée Neo4j ?

À partir de Neo4j 3.x, le concept de [**procédures et fonctions définies par l'utilisateur**](https://neo4j.com/docs/java-reference/current/extending-neo4j/procedures/) a été introduit. Il s'agit d'implémentations personnalisées de certaines fonctionnalités et/ou règles métiers qui ne peuvent pas être (facilement) exprimées en Cypher lui-même.

Neo4j fournit un certain nombre de procédures intégrées. La bibliothèque [APOC](http://neo4j-contrib.github.io/neo4j-apoc-procedures/) en ajoute environ 450 pour couvrir tous types d'usages, de l'intégration de données aux refactorings de graphes.

### Quelles sont les procédures de flux ?

Le projet Neo4j Streams propose deux procédures :

* `streams.publish` : permet l'envoi de messages personnalisés de Neo4j vers l'environnement configuré en utilisant le Producteur configuré sous-jacent
* `streams.consume` : permet de consommer des messages à partir d'un sujet donné.

### Installation de l'environnement

En vous rendant sur le dépôt [Github suivant](https://github.com/conker84/leveraging-neo4j-streams), vous trouverez tout ce qui est nécessaire pour reproduire ce que je présente dans cet article. Ce dont vous aurez besoin pour commencer est [**Docker**](https://docs.docker.com/), puis vous pourrez simplement lancer la pile en entrant dans le répertoire et en exécutant la commande suivante depuis le Terminal :

```
$ docker-compose up
```

Cela démarrera l'ensemble de l'environnement qui comprend :

* Neo4j + module Neo4j Streams + procédures APOC
* Apache Kafka
* Apache Spark (qui n'est pas nécessaire dans cet article, mais il est utilisé dans les deux précédents)
* Apache Zeppelin

En accédant à Apache Zeppelin @ `http://localhost:8080`, vous trouverez dans le répertoire `Medium/Part 3` un notebook appelé « **Streams Procedures** » qui est le sujet de cet article.

### streams.publish

Cette procédure permet l'envoi de messages personnalisés de Neo4j vers l'environnement configuré en utilisant le Producteur configuré sous-jacent.

Elle prend deux variables en entrée et ne retourne rien (car elle envoie sa charge utile de manière asynchrone au flux) :

* **topic**, _type String_ : où les données seront publiées
* **payload**, _type Object_ : ce que vous souhaitez envoyer en flux.

Exemple :

```
CALL streams.publish('my-topic', 'Hello World from Neo4j!')
```

Le message récupéré par le Consommateur est le suivant :

```
{"payload": "Hello world from Neo4j!"}
```

Vous pouvez envoyer tout type de données dans la charge utile : **nœuds, relations, chemins, listes, cartes, valeurs scalaires et versions imbriquées de ceux-ci**.

Dans le cas de nœuds et/ou de relations, si le sujet est défini dans les motifs fournis par la configuration de Capture des Données Modifiées (CDC), leurs propriétés seront filtrées selon la configuration.

Voici une simple vidéo qui montre la procédure en action :

![Image](https://cdn-media-1.freecodecamp.org/images/jmaPyKRDXsCEdwZEdeMzNyE2BoKXolGMEbjR)
_La procédure streams.publish en action_

### streams.consume

Cette procédure permet de consommer des messages à partir d'un sujet donné.

Elle prend deux variables en entrée :

* **topic**, _type String_ : où vous souhaitez consommer les données
* **config**, _type Map<String, Object>_ : les paramètres de configuration

et retourne une liste d'événements collectés.

Les paramètres de **config** sont :

* **timeout**, _type Long_ : il s'agit de la valeur passée à la méthode Kafka `[Consumer#poll](https://kafka.apache.org/10/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html#poll-long-)` (millisecondes). Par défaut 1000.
* **from**, _type String_ : il s'agit du paramètre de configuration Kafka `auto.offset.reset`

Utilisation :

```
CALL streams.consume('my-topic', {<config>}) YIELD event RETURN event
```

Exemple : Imaginez que vous avez un producteur qui publie des événements comme ceci :

```
{"name": "Andrea", "surname": "Santurbano"}
```

Nous pouvons créer des nœuds utilisateur de cette manière :

```
CALL streams.consume('my-topic', {<config>}) YIELD eventCREATE (p:Person{firstName: event.data.name, lastName: event.data.surname})
```

Voici une simple vidéo qui montre la procédure en action :

![Image](https://cdn-media-1.freecodecamp.org/images/m0Lui2cBqiT0OQO9DTuiQfOYHZmpAKwRB4Ys)
_La procédure stream.consume en action_

Nous voici à la fin de la série « Tirer parti de Neo4j Streams », j'espère que vous l'avez appréciée !

Si vous avez déjà testé le module Neo4j-Streams ou l'avez testé via ce notebook, veuillez remplir notre [**enquête de feedback**](https://goo.gl/forms/VLwvqwsIvdfdm9fL2).

Si vous rencontrez des problèmes ou avez des idées pour améliorer notre travail, [veuillez ouvrir une issue GitHub](http://github.com/neo4j-contrib/neo4j-streams/issues).