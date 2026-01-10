---
title: Python SQL – Comment utiliser les bases de données SQLite, MySQL et PostgreSQL
  avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-25T19:38:59.000Z'
originalURL: https://freecodecamp.org/news/python-sql-how-to-use-sql-databases-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/max-duzij-qAjJk-un3BI-unsplash-1.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: Python
  slug: python
- name: SQL
  slug: sql
- name: SQLite
  slug: sqlite
seo_title: Python SQL – Comment utiliser les bases de données SQLite, MySQL et PostgreSQL
  avec Python
seo_desc: "By Daniel Chae\nOne of my greatest joys as a developer is learning how\
  \ different technologies intersect. \nOver the years I've had the opportunity to\
  \ work with different types of software and tools. Of the many tools I've used,\
  \ Python and Structured Qu..."
---

Par Daniel Chae

L'une de mes plus grandes joies en tant que développeur est d'apprendre comment différentes technologies s'intersectent. 

Au fil des ans, j'ai eu l'opportunité de travailler avec différents types de logiciels et d'outils. Parmi les nombreux outils que j'ai utilisés, Python et le langage de requête structuré (SQL) sont deux de mes préférés. 

Dans cet article, je vais vous expliquer comment Python et les différentes bases de données SQL interagissent. 

Je parlerai des bases de données les plus populaires, SQLite, MySQL et PostgreSQL. J'expliquerai les différences clés de chaque base de données et les cas d'utilisation correspondants. Et je terminerai l'article avec un peu de code Python. 

Le code vous montrera comment écrire une requête SQL pour extraire des données d'une base de données PostgreSQL et stocker les données dans un data frame pandas.

*Si vous n'êtes pas familier avec les bases de données relationnelles (RDBMS), je vous suggère de consulter l'article de Sameer sur la terminologie de base des RDBMS [ici](https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/). Le reste de l'article utilisera des termes référencés dans l'article de Sameer.* 

## Bases de données SQL populaires

### SQLite

SQLite est surtout connu pour être une base de données intégrée. Cela signifie que vous n'avez pas besoin d'installer une application supplémentaire ou d'utiliser un serveur séparé pour exécuter la base de données. 

Si vous créez un MVP ou n'avez pas besoin d'un énorme espace de stockage de données, vous voudrez opter pour une base de données SQLite. 

Les avantages sont que vous pouvez avancer plus rapidement avec une base de données SQLite par rapport à MySQL et PostgreSQL. Cela dit, vous serez limité en termes de fonctionnalités. Vous ne pourrez pas personnaliser les fonctionnalités ou ajouter beaucoup de fonctionnalités multi-utilisateurs.

### MySQL/PostgreSQL

Il existe des différences distinctes entre MySQL et PostgreSQL. Cela dit, dans le contexte de cet article, ils appartiennent à une catégorie similaire. 

Les deux types de bases de données sont excellents pour les solutions d'entreprise. Si vous devez évoluer rapidement, MySQL et PostgreSQL sont vos meilleurs choix. Ils fourniront une infrastructure à long terme et renforceront votre sécurité. 

Une autre raison pour laquelle ils sont excellents pour les entreprises est qu'ils peuvent gérer des activités à haute performance. Les instructions d'insertion, de mise à jour et de sélection plus longues nécessitent beaucoup de puissance de calcul. Vous pourrez écrire ces instructions avec moins de latence que ce qu'une base de données SQLite vous offrirait.

## Pourquoi connecter Python et une base de données SQL ?

Vous vous demandez peut-être, "pourquoi devrais-je me soucier de connecter Python et une base de données SQL ?"

Il existe de nombreux cas d'utilisation pour lesquels quelqu'un voudrait connecter Python à une base de données SQL. Comme je l'ai mentionné précédemment, vous pourriez travailler sur une application web. Dans ce cas, vous devriez connecter une base de données SQL afin de pouvoir stocker les données provenant de l'application web. 

Peut-être travaillez-vous dans le domaine de l'ingénierie des données et devez-vous construire un pipeline ETL automatisé. Connecter Python à une base de données SQL vous permettra d'utiliser Python pour ses capacités d'automatisation. Vous pourrez également communiquer entre différentes sources de données. Vous n'aurez pas à changer de langage de programmation.

Connecter Python et une base de données SQL rendra également votre travail en science des données plus pratique. Vous pourrez utiliser vos compétences en Python pour manipuler des données provenant d'une base de données SQL. Vous n'aurez pas besoin d'un fichier CSV.

## Comment Python et les bases de données SQL se connectent

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-design-1-.png)

Python et les bases de données SQL se connectent via des bibliothèques Python personnalisées. Vous pouvez importer ces bibliothèques dans votre script Python. 

Les bibliothèques Python spécifiques aux bases de données servent d'instructions supplémentaires. Ces instructions guident votre ordinateur sur la manière dont il peut interagir avec votre base de données SQL. Sinon, votre code Python sera une langue étrangère pour la base de données à laquelle vous essayez de vous connecter.

### Comment configurer le projet

Prenons l'exemple d'une base de données PostgreSQL, AWS Redshift. Tout d'abord, vous voudrez importer la bibliothèque psycopg. C'est une bibliothèque Python universelle pour les bases de données PostgreSQL. 

```installation
#Bibliothèque pour se connecter à AWS Redshift
import psycopg

#Bibliothèque pour lire le fichier de configuration, qui est en JSON
import json

#Bibliothèque de manipulation de données
import pandas as pd
```

Vous remarquerez que nous avons également importé les bibliothèques JSON et pandas. Nous avons importé JSON car la création d'un fichier de configuration JSON est un moyen sécurisé de stocker vos identifiants de base de données. Nous ne voulons pas que quelqu'un d'autre les voie ! 

La bibliothèque pandas vous permettra d'utiliser toutes les capacités statistiques de pandas pour votre script Python. Dans ce cas, la bibliothèque permettra à Python de stocker les données que votre requête SQL retourne dans un data frame. 

Ensuite, vousoudrez accéder à votre fichier de configuration. La fonction `json.load()` lit le fichier JSON afin que vous puissiez accéder à vos identifiants de base de données dans l'étape suivante.

```installation (suite)
config_file = open(r"C:\Users\yourname\config.json")
config = json.load(config_file)


```

Maintenant que votre script Python peut accéder à votre fichier de configuration JSON, vousoudrez créer une connexion à la base de données. Vous devrez lire et utiliser les identifiants de votre fichier de configuration :

```
con = psycopg2.connect(dbname= "db_name", host=config[hostname], port = config["port"],user=config["user_id"], password=config["password_key"])
cur = con.cursor()
```

Vous venez de créer une connexion à la base de données ! Lorsque vous avez importé la bibliothèque psycopg, vous avez traduit le code Python que vous avez écrit ci-dessus pour communiquer avec la base de données PostgreSQL (AWS Redshift). 

En soi, AWS Redshift ne comprendrait pas le code ci-dessus. Mais parce que vous avez importé la bibliothèque psycopg, vous parlez maintenant une langue qu'AWS Redshift peut comprendre. 

L'avantage de Python est qu'il dispose de bibliothèques pour SQLite, MySQL et PostgreSQL. Vous pourrez intégrer les technologies avec facilité.

### Comment écrire une requête SQL

*N'hésitez pas à télécharger les [Données de football européen](https://www.kaggle.com/hugomathien/soccer) vers votre base de données PostgreSQL. J'utiliserai ses données pour cet exemple.*  

La connexion à la base de données que vous avez créée dans l'étape précédente vous permet d'écrire du SQL pour ensuite stocker les données dans une structure de données compatible avec Python. Maintenant que vous avez établi une connexion à la base de données, vous pouvez écrire une requête SQL pour commencer à extraire des données :

```sql query
query = "SELECT *
         FROM League
         JOIN Country ON Country.id = League.country_id;"
```

Le travail n'est pas encore terminé, cependant. Vous devez écrire un peu plus de code Python qui exécute la requête SQL :

```
#Exécute votre requête SQL
execute1 = cur.execute(query)
result = cur.fetchall()
```

Ensuite, vous devez stocker les données retournées dans un data frame pandas :

```
#Crée le data frame initial à partir des données SQL
raw_initial_df = pd.read_sql_query(query, con)
print(raw_initial_df)
```

Vous devriez obtenir un data frame pandas (raw_initial_df) qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-108.png)

## Il y a une base de données pour tout le monde

![Image](https://www.freecodecamp.org/news/content/images/2021/03/nastya-dulhiier-0Oppqi4r394-unsplash.jpg)

SQLite, MySQL et PostgreSQL ont tous leurs avantages et inconvénients. Celui que vous sélectionnez doit dépendre des besoins de votre projet ou de votre entreprise. Vous devez également considérer ce dont vous avez besoin maintenant par rapport à plusieurs années plus tard. 

L'important à retenir est que Python peut s'intégrer avec chaque type de base de données. 

Cet article effleure la surface de ce qui est possible avec la connexion de Python à une base de données SQL. J'adore voir comment les logiciels s'intersectent et se combinent pour ajouter une valeur incroyable. 

Si vous voulez plus de ce type de contenu, vous pouvez me trouver sur [Course to Hire](https://coursetohire.com/) ! Je veux aider plus de gens à apprendre à coder et à décrocher un emploi dans la tech. N'hésitez pas à me contacter pour toute question ou simplement pour dire bonjour :)