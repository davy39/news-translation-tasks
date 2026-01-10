---
title: Comment utiliser SQLite avec Python
subtitle: ''
author: Eesa Zahed
co_authors: []
series: null
date: '2023-02-21T21:41:41.000Z'
originalURL: https://freecodecamp.org/news/sqlite-python-beginners-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/218187404-b5da9bc5-a6aa-446f-a8d5-5805344d091e.jpeg
tags:
- name: Python
  slug: python
- name: SQLite
  slug: sqlite
seo_title: Comment utiliser SQLite avec Python
seo_desc: 'Databases are a crucial component in software development. After all, we
  need to collect data in a location where we can digitally access it for reading,
  writing, updating, and deleting.

  In this tutorial, you''ll learn how to use SQLite with Python. L...'
---

Les bases de données sont un composant crucial dans le développement logiciel. Après tout, nous devons collecter des données dans un endroit où nous pouvons y accéder numériquement pour les lire, les écrire, les mettre à jour et les supprimer.

Dans ce tutoriel, vous apprendrez à utiliser SQLite avec Python. Apprendre SQLite est un excellent moyen de comprendre comment fonctionnent les bases de données et comment effectuer des opérations CRUD (create, read, update, delete) de base. 

De nombreux postes de développeur logiciel impliquent de travailler avec des bases de données, et si vous envisagez un jour de créer une application à grande échelle (comme une application de médias sociaux ou un jeu en ligne), vous aurez définitivement besoin d'une base de données.

Ce tutoriel expliquera de nombreux concepts de base et opérations simples, afin que vous puissiez mieux comprendre comment travailler avec les bases de données.

## Qu'est-ce que SQLite ?

SQLite est une bibliothèque de moteur de base de données SQL (Structured Query Language) intégrée qui fonctionne avec de nombreux langages. 

Selon le [site officiel](https://www.sqlite.org/arch.html), le texte SQL est compilé en bytecode, qui est ensuite exécuté par une machine virtuelle. Par conséquent, il est extrêmement rapide et peut gérer efficacement des requêtes complexes.

Une base de données SQLite est stockée sous forme de fichier disque, similaire à un fichier CSV (comma-separated values). Mais SQLite présente de nombreux avantages par rapport à l'utilisation d'un fichier CSV :

* Il est écrit en C. Le C est un langage statiquement typé et compilé qui est beaucoup plus rapide que la plupart des langages, y compris Python.
* Il est léger, donc il performe mieux et plus rapidement que la lecture d'un fichier CSV.
* Il est facile à installer
* Il peut gérer des requêtes plus complexes.
* Il est plus utile à apprendre, au cas où vous seriez un jour chargé d'utiliser SQL ou MySQL à l'avenir.

## Comment installer SQLite

Voici un exemple d'utilisation de SQLite avec Python. J'utilise [l'IDE en ligne de Replit](https://replit.com), mais vous êtes libre de suivre avec n'importe quel IDE que vous préférez. 

Tout d'abord, je vais créer un projet Python avec un fichier `main.py`. J'utiliserai la bibliothèque SQL de CS50, que vous pouvez installer en exécutant `pip3 install cs50`.

La première étape consiste à créer un fichier database.db dans le répertoire racine, ce que vous pouvez faire en entrant la commande suivante dans le terminal :

```
touch database.db

```

À ce stade, le code suivant doit être ajouté à main.py :

```
from cs50 import SQL

db = SQL("sqlite:///database.db")

```

### Comment créer une table de base de données

L'étape suivante consiste à créer une table dans la base de données. SQL stocke les données dans des tables, qui sont similaires aux tables trouvées dans Excel ou Google Sheets. Le code pour cela est :

```
db.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age NUMBER, fav_food STRING)")

```

Pour décomposer cela, db est la base de données dans laquelle les données sont écrites. Ensuite, une commande est exécutée. Si la table `users` n'existe pas, créez une table avec le nom users, avec les noms de colonnes `name`, `age`, et `fav_food`, avec les types de données pour chaque valeur spécifiés.

### Comment écrire dans la base de données

Vous pouvez utiliser l'opération INSERT pour ajouter un utilisateur.

```
db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)", "eesa", 14, "pizza")

```

La valeur "eesa" est insérée dans la colonne name, la valeur 14 est insérée dans la colonne age, et la valeur "pizza" est insérée dans la colonne fav_food.

Le code pour ajouter un autre utilisateur (dans ce cas, Bob), serait le suivant :

```
db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)", "bob", 20, "burgers")
```

### Comment lire depuis la base de données

Après cela, nous pouvons essayer de lire tous les utilisateurs de la base de données. Vous pouvez faire cela en exécutant le code suivant.

```
people = db.execute("SELECT * FROM users")
print(people) # [{'name': 'eesa', 'age': 14, 'fav_food': 'pizza'}]

```

Le code ci-dessus est assez simple. Le * dans l'instruction SELECT sélectionne tout ce qui se trouve dans la base de données.

Pour sélectionner uniquement des valeurs spécifiques, vous pouvez utiliser l'instruction DISTINCT. Supposons par exemple que vous ne voulez que la nourriture préférée de chaque utilisateur. Vous pouvez faire cela en exécutant le code suivant :

```
people = db.execute("SELECT DISTINCT fav_food FROM users")
print(people)

```

Vous pouvez également séparer les valeurs en utilisant des virgules dans une requête SELECT DISTINCT :

```
people = db.execute("SELECT DISTINCT age, fav_food FROM users")
print(people)

```

Et si nous voulions simplement lire les données pour Bob, et ignorer tout le monde ? Vous pouvez faire cela en utilisant la clause WHERE de SQL :

```
people = db.execute("SELECT * FROM users WHERE name='bob'")
print(people)

```

Et pour des requêtes plus complexes ? Vous pouvez le faire en utilisant la syntaxe AND, OR et NOT. Vous pouvez séparer les clauses WHERE avec ces mots-clés pour des requêtes plus complexes.

```
people = db.execute("SELECT * FROM users WHERE name='bob' AND age=20")
print(people)
```

Cela imprimera les données pour Bob, car Bob a 20 ans. 

### Comment mettre à jour une ligne dans la base de données

Pour mettre à jour une ligne, vous pouvez utiliser l'instruction UPDATE comme ceci :

```
db.execute("UPDATE users SET fav_food='shawarma' WHERE name='eesa'")

```

### Comment supprimer une ligne dans la base de données

Pour supprimer une ligne, utilisez la syntaxe DELETE (comme vous l'auriez peut-être deviné). Cela ressemble à ceci :

```
db.execute("DELETE FROM users WHERE name='bob'") # au revoir bob

people = db.execute("SELECT * FROM users")
print(people) # [{'name': 'eesa', 'age': 14, 'fav_food': 'shawarma'}]

```

Pour supprimer toutes les lignes de la table, il suffit de supprimer la clause WHERE :

```
db.execute("DELETE FROM users") # :(

people = db.execute("SELECT * FROM users")
print(people) # []

```

## Conclusion

Et c'est tout pour l'instant. Pour plus d'informations sur SQLite, je vous recommande de consulter la [documentation officielle](https://docs.python.org/3/library/sqlite3.html). Je vous souhaite le meilleur dans la création de choses incroyables !

N'hésitez pas à consulter mon [GitHub](https://github.com/eesazahed) et [Replit](https://replit.com/@eesazahed) pour voir mes projets.

Si vous souhaitez me contacter, mon adresse e-mail est eszhd1 (at) gmail.com