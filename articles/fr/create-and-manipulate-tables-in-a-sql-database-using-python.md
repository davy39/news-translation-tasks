---
title: Comment créer et manipuler des tables dans une base de données SQL en utilisant
  Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-14T16:28:25.000Z'
originalURL: https://freecodecamp.org/news/create-and-manipulate-tables-in-a-sql-database-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/tables.JPG
tags:
- name: database
  slug: database
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: Comment créer et manipuler des tables dans une base de données SQL en utilisant
  Python
seo_desc: 'Python is a powerful programming language that you can use to interact
  with SQL databases. With the help of Python, you can create, manipulate, and interact
  with the tables in the SQL database.

  In this tutorial, we will be discussing how to create an...'
---

Python est un langage de programmation puissant que vous pouvez utiliser pour interagir avec des bases de données SQL. Avec l'aide de Python, vous pouvez créer, manipuler et interagir avec les tables d'une base de données SQL.

Dans ce tutoriel, nous allons voir comment créer et manipuler des tables dans une base de données SQL en utilisant Python.

### Prérequis :

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* Une connaissance pratique de Python.
    
* Une base de données SQL. Pour ce tutoriel, nous utiliserons SQLite.
    

## Comment créer une table dans une base de données SQL en utilisant Python

Pour créer une table dans une base de données SQL en utilisant Python, nous devons d'abord établir une connexion à la base de données. Pour ce tutoriel, nous utiliserons la base de données SQLite. SQLite est une base de données légère et sans serveur, idéale pour les petits projets.

Pour se connecter à la base de données SQLite, nous utiliserons le module sqlite3 intégré à Python.

Voici le code pour créer une table dans notre base de données SQLite en utilisant Python :

```python
import sqlite3

# connexion à la base de données
conn = sqlite3.connect('example.db')

# créer un objet curseur
c = conn.cursor()

# créer une table
c.execute('''CREATE TABLE employees
             (id INT PRIMARY KEY NOT NULL,
              name TEXT NOT NULL,
              age INT NOT NULL)''')

# sauvegarder les modifications
conn.commit()

# fermer la connexion
conn.close()
```

Dans le code ci-dessus, nous avons d'abord établi une connexion à la base de données SQLite en utilisant la méthode `connect` du module `sqlite3`. Nous avons ensuite créé un objet curseur en utilisant la méthode `cursor`.

Ensuite, nous avons exécuté une requête SQL pour créer une table nommée `employees` avec trois colonnes : `id`, `name`, et `age`. La colonne `id` est définie comme clé primaire (PRIMARY KEY), ce qui signifie que chaque enregistrement de la table aura une valeur `id` unique. Les colonnes `name` et `age` sont définies comme `NOT NULL`, ce qui signifie qu'elles ne peuvent pas être vides.

Enfin, nous avons sauvegardé les modifications en utilisant la méthode `commit` et fermé la connexion en utilisant la méthode `close`.

## Comment insérer des données dans une table

Maintenant que nous avons créé une table, nous pouvons y insérer des données. Voici le code pour insérer des données dans la table `employees` :

```python
import sqlite3

# connexion à la base de données
conn = sqlite3.connect('example.db')

# créer un objet curseur
c = conn.cursor()

# insérer des données dans la table
c.execute("INSERT INTO employees (id, name, age) VALUES (1, 'John Doe', 30)")
c.execute("INSERT INTO employees (id, name, age) VALUES (2, 'Jane Doe', 25)")

# sauvegarder les modifications
conn.commit()

# fermer la connexion
conn.close()
```

Dans le code ci-dessus, nous avons inséré deux enregistrements dans la table `employees` en utilisant la méthode `execute`. Nous avons passé deux requêtes SQL, une pour chaque enregistrement.

## Comment sélectionner des données d'une table

Maintenant que nous avons inséré des données dans la table `employees`, nous pouvons les récupérer en utilisant l'instruction `SELECT`. Voici le code pour sélectionner des données de la table `employees` :

```python
import sqlite3

# connexion à la base de données
conn = sqlite3.connect('example.db')

# créer un objet curseur
c = conn.cursor()

# sélectionner des données de la table
c.execute("SELECT * FROM employees")

# récupérer tous les enregistrements
records = c.fetchall()

# afficher les enregistrements
for record in records:
    print(record)

# fermer la connexion
conn.close()
```

Dans le code ci-dessus, nous avons sélectionné tous les enregistrements de la table `employees` en utilisant l'instruction `SELECT`. Nous avons ensuite récupéré tous les enregistrements en utilisant la méthode `fetchall` et nous les avons affichés à l'aide d'une boucle for.

## Comment mettre à jour des données dans une table

Pour mettre à jour des données dans une table, nous utilisons l'instruction `UPDATE`. Voici le code pour mettre à jour des données dans la table `employees` :

```python
import sqlite3

# connexion à la base de données
conn = sqlite3.connect('example.db')

# créer un objet curseur
c = conn.cursor()

# mettre à jour des données dans la table
c.execute("UPDATE employees SET age = 35 WHERE name = 'John Doe'")

# sauvegarder les modifications
conn.commit()

# sélectionner des données de la table
c.execute("SELECT * FROM employees")

# récupérer tous les enregistrements
records = c.fetchall()

# afficher les enregistrements
for record in records:
    print(record)

# fermer la connexion
conn.close()
```

Dans le code ci-dessus, nous avons mis à jour l'âge de l'enregistrement portant le nom 'John Doe' à 35 en utilisant l'instruction `UPDATE`. Nous avons ensuite sauvegardé les modifications en utilisant la méthode `commit`.

## Comment supprimer des données d'une table

Pour supprimer des données d'une table, nous utilisons l'instruction `DELETE`. Voici le code pour supprimer des données de la table `employees` :

```python
import sqlite3

# connexion à la base de données
conn = sqlite3.connect('example.db')

# créer un objet curseur
c = conn.cursor()

# supprimer des données de la table
c.execute("DELETE FROM employees WHERE name = 'Jane Doe'")

# sauvegarder les modifications
conn.commit()

# sélectionner des données de la table
c.execute("SELECT * FROM employees")

# récupérer tous les enregistrements
records = c.fetchall()

# afficher les enregistrements
for record in records:
    print(record)

# fermer la connexion
conn.close()
```

Dans le code ci-dessus, nous avons supprimé l'enregistrement portant le nom 'Jane Doe' de la table `employees` en utilisant l'instruction `DELETE`. Nous avons ensuite sauvegardé les modifications en utilisant la méthode `commit`.

## Conclusion

Dans cet article, nous avons vu comment créer et manipuler des tables dans une base de données SQL en utilisant Python.

Nous avons couvert la création d'une table, l'insertion de données, la sélection de données, la mise à jour et la suppression de données. Nous avons également fourni le code nécessaire pour accomplir ces tâches.

En suivant les étapes décrites dans ce tutoriel, vous pouvez créer et manipuler des tables dans n'importe quelle base de données SQL en utilisant Python.

Connectons-nous sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).