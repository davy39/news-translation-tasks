---
title: Comment lire et écrire des données dans une base de données SQL avec Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-08T19:27:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-and-write-data-to-a-sql-database-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/SQL-Queries.JPG
tags:
- name: database
  slug: database
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: Comment lire et écrire des données dans une base de données SQL avec Python
seo_desc: 'Databases are a crucial component of modern-day software systems. And SQL
  databases are one of the most widely used types of databases.

  They are ideal for managing data in a structured and organized way, and they are
  widely used in various applicatio...'
---

Les bases de données sont un composant crucial des systèmes logiciels modernes. Et les bases de données SQL sont l'un des types de bases de données les plus largement utilisés.

Elles sont idéales pour gérer les données de manière structurée et organisée, et elles sont largement utilisées dans diverses applications, notamment le commerce électronique, la santé, la finance, et bien plus encore.

Dans cet article, nous allons discuter de la manière de lire et d'écrire des données dans une base de données SQL en utilisant Python. Nous fournirons des exemples de la manière de se connecter à une base de données SQL en utilisant Python et de la manière d'exécuter des commandes SQL pour effectuer des opérations de base de données telles que l'insertion, la mise à jour, la suppression et la sélection.

### Prérequis

Avant de plonger dans les exemples de code, assurez-vous d'avoir les prérequis suivants installés sur votre système :

* Python 3.x

* Un système de gestion de base de données SQL (par exemple, MySQL, PostgreSQL, SQLite, etc.)

* Un client de base de données SQL (par exemple, MySQL Workbench, pgAdmin, DB Browser pour SQLite, etc.)

## Comment se connecter à une base de données SQL en utilisant Python

Python dispose de plusieurs bibliothèques pour se connecter à des bases de données SQL, notamment `pymysql`, `psycopg2` et `sqlite3`. Dans cette section, nous allons discuter de la manière de se connecter à une base de données MySQL en utilisant `pymysql`.

Tout d'abord, nous devons installer la bibliothèque `pymysql` en utilisant pip :

```python
pip install pymysql
```

Ensuite, nous devons importer la bibliothèque `pymysql` et nous connecter à la base de données MySQL en utilisant le code suivant :

```python
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='mydatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
```

Dans le code ci-dessus, nous importons d'abord la bibliothèque `pymysql`. Ensuite, nous utilisons la fonction `connect()` pour établir une connexion à la base de données MySQL. Nous devons fournir les paramètres suivants à la fonction `connect()` :

* `host` : le nom d'hôte ou l'adresse IP du serveur MySQL

* `user` : le nom d'utilisateur utilisé pour s'authentifier auprès du serveur MySQL

* `password` : le mot de passe utilisé pour s'authentifier auprès du serveur MySQL

* `db` : le nom de la base de données à laquelle se connecter

* `charset` : le jeu de caractères à utiliser pour la connexion

* `cursorclass` : le type de curseur à utiliser pour la connexion (dans ce cas, nous utilisons le curseur `DictCursor`, qui retourne les lignes sous forme de dictionnaires)

Une fois que nous avons établi une connexion à la base de données MySQL, nous pouvons exécuter des commandes SQL pour effectuer diverses opérations sur la base de données.

## Comment insérer des données dans une base de données SQL en utilisant Python

Pour insérer des données dans une base de données SQL en utilisant Python, nous devons exécuter une commande SQL `INSERT`. Dans l'exemple suivant, nous allons insérer un nouvel enregistrement dans une base de données MySQL :

```python
try:
    with conn.cursor() as cursor:
        # Créer un nouvel enregistrement
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('john@example.com', 'mypassword'))

    # Valider les changements
    conn.commit()

    print("Enregistrement inséré avec succès")
finally:
    conn.close()
```

Dans le code ci-dessus, nous utilisons un bloc `try`/`finally` pour nous assurer que la connexion à la base de données est correctement fermée. Dans le bloc `try`, nous utilisons la fonction `cursor()` pour créer un nouvel objet curseur. Nous exécutons ensuite la commande `INSERT` en utilisant la fonction `execute()` et nous passons les valeurs que nous voulons insérer dans la base de données.

Une fois que la fonction `execute()` a été appelée, nous utilisons la fonction `commit()` pour valider les changements dans la base de données. Enfin, nous fermons la connexion à la base de données en utilisant la fonction `close()`.

## Comment mettre à jour des données dans une base de données SQL en utilisant Python

Pour mettre à jour des données dans une base de données SQL en utilisant Python, nous devons exécuter une commande SQL `UPDATE`. Dans l'exemple suivant, nous allons mettre à jour un enregistrement existant dans une base de données MySQL :

```python
try:
    with conn.cursor() as cursor:
        # Mettre à jour un enregistrement
        sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
        cursor.execute(sql, ('newpassword', 'john@example.com'))

    # Valider les changements
    conn.commit()

    print("Enregistrement mis à jour avec succès")
finally:
    conn.close()
```

Dans le code ci-dessus, nous utilisons un bloc `try`/`finally` pour nous assurer que la connexion à la base de données est correctement fermée. Dans le bloc `try`, nous utilisons la fonction `cursor()` pour créer un nouvel objet curseur. Nous exécutons ensuite la commande `UPDATE` en utilisant la fonction `execute()` et nous passons la nouvelle valeur que nous voulons mettre à jour et la condition qui spécifie quel enregistrement mettre à jour.

Une fois que la fonction `execute()` a été appelée, nous utilisons la fonction `commit()` pour valider les changements dans la base de données. Enfin, nous fermons la connexion à la base de données en utilisant la fonction `close()`.

## Comment supprimer des données d'une base de données SQL en utilisant Python

Pour supprimer des données d'une base de données SQL en utilisant Python, nous devons exécuter une commande SQL `DELETE`. Dans l'exemple suivant, nous allons supprimer un enregistrement d'une base de données MySQL :

```python
try:
    with conn.cursor() as cursor:
        # Supprimer un enregistrement
        sql = "DELETE FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('john@example.com',))

    # Valider les changements
    conn.commit()

    print("Enregistrement supprimé avec succès")
finally:
    conn.close()
```

Dans le code ci-dessus, nous utilisons un bloc `try`/`finally` pour nous assurer que la connexion à la base de données est correctement fermée. Dans le bloc `try`, nous utilisons la fonction `cursor()` pour créer un nouvel objet curseur. Nous exécutons ensuite la commande `DELETE` en utilisant la fonction `execute()` et nous passons la condition qui spécifie quel enregistrement supprimer.

Une fois que la fonction `execute()` a été appelée, nous utilisons la fonction `commit()` pour valider les changements dans la base de données. Enfin, nous fermons la connexion à la base de données en utilisant la fonction `close()`.

## Comment lire des données d'une base de données SQL en utilisant Python

Pour lire des données d'une base de données SQL en utilisant Python, nous devons exécuter une commande SQL `SELECT`. Dans l'exemple suivant, nous allons lire des données d'une base de données MySQL et afficher les résultats :

```python
try:
    with conn.cursor() as cursor:
        # Lire les données de la base de données
        sql = "SELECT * FROM `users`"
        cursor.execute(sql)

        # Récupérer toutes les lignes
        rows = cursor.fetchall()

        # Afficher les résultats
        for row in rows:
            print(row)
finally:
    conn.close()
```

Dans le code ci-dessus, nous utilisons un bloc `try`/`finally` pour nous assurer que la connexion à la base de données est correctement fermée. Dans le bloc `try`, nous utilisons la fonction `cursor()` pour créer un nouvel objet curseur. Nous exécutons ensuite la commande `SELECT` en utilisant la fonction `execute()`.

Une fois que la fonction `execute()` a été appelée, nous utilisons la fonction `fetchall()` pour récupérer toutes les lignes retournées par la requête. Nous parcourons ensuite les lignes et affichons les résultats.

## Conclusion

Dans cet article, nous avons discuté de la manière de lire et d'écrire des données dans une base de données SQL en utilisant Python.

Nous avons fourni des exemples de la manière de se connecter à une base de données MySQL en utilisant `pymysql`, et de la manière d'exécuter des commandes SQL pour effectuer des opérations de base de données telles que l'insertion, la mise à jour, la suppression et la sélection.

En suivant les exemples de code fournis dans cet article, vous pouvez rapidement et facilement lire et écrire des données dans une base de données SQL en utilisant Python.

Restons en contact sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).