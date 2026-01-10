---
title: Comment utiliser PostgreSQL en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-14T15:16:10.000Z'
originalURL: https://freecodecamp.org/news/postgresql-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/postgresql-in-python.png
tags:
- name: database
  slug: database
- name: postgres
  slug: postgres
- name: Python
  slug: python
seo_title: Comment utiliser PostgreSQL en Python
seo_desc: "By Shittu Olumide\nThere are many different types of databases in use today.\
  \ We have centralized databases, commercial databases, cloud databases, distributed\
  \ databases, end-user databases, NoSQL databases, relational databases, and lots\
  \ more.  \nThis ..."
---

Par Shittu Olumide

Il existe de nombreux types de bases de données différents utilisés aujourd'hui. Nous avons des bases de données centralisées, des bases de données commerciales, des bases de données cloud, des bases de données distribuées, des bases de données utilisateur final, des bases de données NoSQL, des bases de données relationnelles, et bien d'autres. 
  
Cet article se concentrera sur un exemple de base de données relationnelle (PostgreSQL) et sur la manière d'interroger des données à partir de celle-ci. D'autres exemples de bases de données relationnelles incluent MySQL, MariaDB et SQLite. 

Dans ce tutoriel, vous apprendrez à installer, connecter et enfin interroger une base de données PostgreSQL avec Python.

Pour commencer, apprenons un peu plus sur PostgreSQL.

## Qu'est-ce que PostgreSQL ?

L'une des bases de données relationnelles open-source les plus connues est PostgreSQL. Elle est utilisée par des développeurs et des entreprises de toutes tailles dans le monde entier. 

En termes de popularité mondiale, PostgreSQL est [classé quatrième](https://db-engines.com/en/ranking) par DB-Engines, et sa popularité est en croissance. Cela ne devrait pas surprendre, étant donné que de nombreuses applications web et mobiles, ainsi que des outils analytiques, utilisent des bases de données PostgreSQL.

PostgreSQL possède également un écosystème robuste avec une grande sélection d'add-ons et d'extensions qui fonctionnent bien avec la base de données principale. Pour ces raisons, PostgreSQL est une option fantastique que vous souhaitiez créer votre propre solution de base de données personnalisée ou avoir besoin d'une base de données transactionnelle ou analytique.

Maintenant que vous savez ce qu'est PostgreSQL, discutons de la manière de se connecter à la base de données en utilisant Python.

## Getting Started

Nous devons utiliser une bibliothèque de connecteur de base de données pour nous connecter à une instance de base de données PostgreSQL à partir de notre script Python. Nous pouvons choisir parmi une variété d'alternatives en Python, mais [Psycopg2](https://www.psycopg.org/docs/) est la plus connue et largement utilisée.

Il existe des bibliothèques alternatives entièrement écrites en Python, telles que [pg8000](https://github.com/tlocke/pg8000) et [py-postgresql](https://github.com/python-postgres/fe), mais nous utiliserons Psycopg2 ici.

### Qu'est-ce que Psycopg2 ?

La bibliothèque Psycopg2 utilise le langage de programmation C comme wrapper autour de la bibliothèque [libpq](https://www.postgresql.org/docs/current/libpq.html) de PostgreSQL pour supporter les standards Python DB API 2.0. L'implémentation en C de Psycopg2 le rend incroyablement rapide et efficace.

En utilisant une requête SQL, nous pouvons utiliser Psycopg2 pour obtenir une ou plusieurs lignes de la base de données. Avec cette bibliothèque, nous pouvons également insérer des données dans la base de données en utilisant diverses méthodes d'insertion unique ou par lots.

La bibliothèque est similaire à SQL (Structured Query Language) et elle effectue toutes les tâches et opérations qu'un langage de requête peut faire. Elle est à la fois compatible Unicode et Python 3, et elle offre également une sécurité des threads (la même connexion est partagée par plusieurs threads).

Elle est conçue pour exécuter des programmes très multithreads, qui produisent et suppriment souvent beaucoup de curseurs et effectuent beaucoup d'INSERTIONS ou de MISES À JOUR simultanées. Les fonctionnalités de Psycopg2 incluent des curseurs côté client et côté serveur, une communication asynchrone et des notifications.

## Comment installer Psycopg2

Nous devons d'abord installer Psycopg2 pour pouvoir l'utiliser. Nous pouvons l'installer via le terminal ou l'invite de commande en utilisant `pip`.

```python
#installation

pip install psycopg2
pip3 install psycopg2
```

Si nous décidons également d'installer la bibliothèque de connecteur dans un environnement virtuel, vous pouvez le faire en utilisant ce code :

```python
virtualenv env && source env/bin/activate
pip install psycopg2-binary
```

La bibliothèque Psycopg2 et toutes ses dépendances seront installées dans notre environnement virtuel Python avec ce snippet de code.

Nous avons installé notre connecteur, alors commençons à écrire quelques requêtes.

## Comment interroger PostgreSQL en utilisant Python 

Tout d'abord, vous devrez créer un nouveau fichier et lui donner le nom que vous souhaitez. Ensuite, ouvrez-le dans votre IDE et commencez à écrire le code. 

La première chose à faire est d'importer la bibliothèque (ceci est très important). Nous utiliserons deux objets Psycogp2 :

* **Objet de connexion** : L'objet de connexion gère la connexion à une instance de base de données PostgreSQL. Il encapsule une session de base de données, créée en utilisant la fonction `connect()`.
* **Objet curseur** : L'objet curseur permet aux scripts Python d'exécuter des commandes PostgreSQL dans une session de base de données. La connexion génère des curseurs, puis la méthode `cursor()` les lie de manière permanente à la connexion. Toutes les commandes sont exécutées dans le cadre de la session de base de données enfermée dans la connexion.

```python
import psycopg2

conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="db_user",
                        password="db_pass",
                        port="db_port")
```

Nous devons spécifier ces arguments afin de pouvoir nous connecter à la base de données. Jetons un coup d'œil rapide à ces arguments.

* **database** : le nom de la base de données à laquelle nous souhaitons accéder ou nous connecter. Notez que nous ne pouvons nous connecter qu'à une seule base de données avec un seul objet de connexion.
* **host** : cela fait probablement référence à l'adresse IP ou à l'URL du serveur de base de données.
* **user** : comme le nom l'indique, cela fait référence au nom de l'utilisateur PostgreSQL.
* **password** : il s'agit du mot de passe qui correspond à l'utilisateur PostgreSQL.
* **port** : le numéro de port du serveur PostgreSQL sur localhost – il est généralement 5432.

Si nos identifiants de base de données ont été saisis correctement, nous recevrons un objet de connexion de base de données en direct que nous pouvons utiliser pour créer un objet curseur. Nous pouvons ensuite exécuter n'importe quelle requête de base de données et récupérer des données à l'aide d'un objet curseur.

```python
cursor = conn.cursor()
```

 Écrivons une requête simple :

```python
cursor.execute("SELECT * FROM DB_table WHERE id = 1")
```

Nous appliquons la fonction `execute()` et fournissons une chaîne de requête comme paramètre. Ensuite, la base de données sera interrogée en utilisant la requête que nous avons entrée.

Après avoir réussi cette étape, afin de pouvoir récupérer des données de la base de données en utilisant Pyscopg2, nous devons utiliser l'une de ces fonctions : `fetchone()`, `fetchall()`, ou `fetchmany()`.

### Comment utiliser `fetchone()` :

Après avoir exécuté la requête SQL, cette fonction ne retournera que la première ligne. C'est la méthode la plus simple pour extraire des données d'une base de données.

```python
#code
print(cursor.fetchone())

#output
(1, 'A-CLASS', '2018', 'Subcompact executive hatchback')
```

La fonction `fetchone()` retourne une seule ligne sous la forme d'un tuple, avec les informations organisées dans l'ordre spécifié par les colonnes fournies par la requête.

Lors de la construction de la chaîne de requête, il est crucial de fournir les ordres de colonne précisément afin de distinguer à quelle donnée dans le tuple appartient quelle.

### Comment utiliser `fetchall()` :

La fonction `fetchall()` fonctionne de la même manière que `fetchone()` sauf qu'elle retourne non pas une seule ligne mais toutes les lignes. Donc, dans le cas où nous voulons 20-200 lignes ou plus, nous utilisons `fetchall()` de Psycopg2.

```python
#code
print(cursor.fetchall())

#output
[(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
 (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
 (3, 'CLA', '2019', 'Subcompact executive fastback sedan'),
 (4, 'CLS', '2018', 'E-segment/executive fastback sedan'),
 (5, 'E-CLASS', '2017', 'E-segment/executive sedan'),
 (6, 'EQE', '2022', 'All-electric E-segment fastback'),
 (7, 'EQS', '2021', 'All-electric full-size luxury liftback'),
 (8, 'S-CLASS', '2020', 'F-segment/full-size luxury sedan.'),
 (9, 'G-CLASS', '2018', 'Mid-size luxury SUV, known as the G-Wagen'),
 (10, 'GLE', '2019', 'Mid-size luxury crossover SUV')]
[...]
```

### Comment utiliser `fetchmany()` : 

La fonction `fetchmany()` nous permet d'obtenir un certain nombre d'enregistrements de la base de données et nous donne un contrôle supplémentaire sur le nombre précis de lignes que nous obtenons.

```python
#code
print(cursor.fetchmany(size=3))

#output
[(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
 (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
 (3, 'CLA', '2019', 'Subcompact executive fastback sedan')]

```

Parce que nous avons défini l'argument à 3, nous n'avons reçu que trois lignes. 

Lorsque nous avons terminé d'interroger notre base de données, nous devons fermer la connexion avec `conn.close()`.

## Conclusion 

C'était assez facile, n'est-ce pas ? Nous avons pu effectuer toutes ces tâches à partir d'un seul script Python et cela a très bien fonctionné.

J'espère que cet article a été utile et que vous pouvez maintenant travailler avec PostgreSQL en utilisant Python. 

Pour plus d'informations, consultez la [documentation](https://www.psycopg.org/docs/) de Psycopg2 pour en savoir plus.