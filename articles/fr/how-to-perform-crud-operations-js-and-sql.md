---
title: Comment effectuer des opérations CRUD – Exemple JavaScript et SQL
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-08-03T20:41:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-js-and-sql
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/5f9ca0b7740569d1a4ca4a58.jpg
tags:
- name: crud
  slug: crud
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: SQL
  slug: sql
seo_title: Comment effectuer des opérations CRUD – Exemple JavaScript et SQL
seo_desc: For the most part, interactive website architectures will involve generating
  or dispensing data of one sort or another. You can certainly use HTML forms to collect
  user input. But the kind of web form that's described here will only take you so
  far. ...
---

Pour la plupart, les architectures de sites web interactifs impliqueront la génération ou la distribution de données d'une sorte ou d'une autre. Vous pouvez certainement utiliser des formulaires HTML pour collecter les entrées des utilisateurs. Mais le type de formulaire web [décrit ici](https://www.freecodecamp.org/news/creating-html-forms/) ne vous mènera que jusqu'à un certain point. 

Ce dont nous avons vraiment besoin, c'est d'une manière de stocker et de manipuler nos données de manière fiable au sein de l'environnement de l'application. 

Dans cet article, je vais vous montrer comment connecter une base de données back-end à votre processus de collecte de données. Le plan implique de mélanger du HTML, du JavaScript et le petit moteur de base de données SQLite, de mélanger vigoureusement et de voir ce qui en sort. 

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/yf2RJmpMEiI]

Comme vous le savez peut-être déjà, le SQL dans SQLite signifie _langage de requête structuré_. Cela signifie que la syntaxe que vous utiliserez pour interagir avec une base de données SQLite sera très similaire à celle que vous utiliseriez avec des bases de données comme MariaDB, Amazon Aurora, Oracle ou Microsoft SQL Server. Si vous avez de l'expérience avec l'une de ces bases de données, vous serez ici comme chez vous.

Pourquoi allons-nous utiliser SQLite ici ? Parce que c'est un choix très populaire pour le type de travail que vous êtes susceptible d'entreprendre dans un environnement web. 

Vous devrez créer un nouveau répertoire sur votre machine ainsi que quelques fichiers avec du code JavaScript. Nous apprendrons comment créer, modifier et supprimer des enregistrements dans une base de données SQLite. 

Je pourrais incorporer toutes ces actions dans un seul fichier, bien sûr, mais je pense que les diviser en plusieurs fichiers rendra plus facile la compréhension de ce qui se passe.

## Connexion à une base de données et création d'une table

Voici à quoi ressemblera le premier fichier :

```
const sqlite3 = require('sqlite3').verbose();

// Créer/se connecter à la base de données
const db = new sqlite3.Database('mydatabase.db');

// Créer une table
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)`);

// Insérer des données
const insertQuery = `INSERT INTO users (name, age) VALUES (?, ?)`;
const name = 'Trevor';
const age = 5;
db.run(insertQuery, [name, age], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Inserted data with id ${this.lastID}`);
    }
});

// Fermer la connexion à la base de données
db.close();
```

Nous commençons par charger le module sqlite3 en tant que `sqlite3`, puis nous créons la variable `db` pour représenter notre nouvelle instance de base de données. La base de données s'appellera `mydatabase.db`. 

```
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('mydatabase.db');
```

S'il n'y a pas de base de données utilisant ce nom dans notre répertoire local, le code en créera une, sinon il se connectera simplement à celle qui existe déjà.

Puisque c'est notre première exécution, je vais créer une nouvelle table dans la base de données `mydatabase.db`. Il y aura trois clés dans notre table : `id`, `name` et `age`. 

```
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)`);
```

Comme vous pouvez le voir, `id` sera la clé primaire que nous utiliserons pour référencer les enregistrements individuels. 

Nous avons défini le type de données de chaque clé : entier, texte et, à nouveau, entier. Cette définition est quelque chose que nous devons faire une seule fois. Mais nous voulons la faire correctement, car la modifier plus tard, après avoir déjà ajouté des données, peut être délicat.

## Insertion de nouvelles données dans une table

Dans cette section, nous allons ajouter un nouvel enregistrement à la table en utilisant la commande SQL `INSERT`.

```
const insertQuery = `INSERT INTO users (name, age) VALUES (?, ?)`;
const name = 'Trevor';
const age = 5;
db.run(insertQuery, [name, age], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Inserted data with id ${this.lastID}`);
    }
});
```

Vous découvrirez probablement que la documentation officielle SQL capitalise toujours les termes de syntaxe clés comme `INSERT` et `SELECT`. C'est une bonne pratique utile, mais ce n'est pas réellement nécessaire. En règle générale, je suis bien trop paresseux pour m'en soucier.

La requête elle-même est modélisée sous forme de `insertQuery`, avec les détails `name` et `age` ajoutés en tant que constantes dans les lignes qui suivent. 

La méthode `db.run`, utilisant la constante `insertQuery` et ces deux valeurs (`name` et `age`) comme attributs, est ensuite exécutée. En fonction du succès ou de l'échec de l'opération, des messages de journalisation seront générés.

Mais attendez un moment. Que signifient ces points d'interrogation après la déclaration de `insertQuery` ? Et pourquoi avons-nous dû diviser ce processus en deux parties ? 

Il s'agit en réalité d'une pratique de sécurité importante connue sous le nom de variable d'échappement. Avec cela en place, lorsque la méthode `db.run()` exécute l'instruction préparée, elle gérera automatiquement l'échappement de la valeur de la variable, empêchant ainsi l'injection SQL.

Enfin, nous fermons la connexion :

```
db.close();
```

## Modification des données

Maintenant, voyons comment fonctionne le code de "modification". Comme avant, nous créons une constante SQLite3 puis nous nous connectons à notre base de données. 

Cette fois, cependant, notre table existe déjà, donc nous pouvons passer directement à la section "modification".

```
const sqlite3 = require('sqlite3').verbose();

// Créer/se connecter à la base de données
const db = new sqlite3.Database('mydatabase.db');

// Modifier les données
const updateQuery = `UPDATE users SET age = ? WHERE name = ?`;
const updatedAge = 30;
const updatedName = 'name2';
db.run(updateQuery, [updatedAge, updatedName], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Modified ${this.changes} row(s)`);
    }
});

// Fermer la connexion à la base de données
db.close();
```

Le schéma est similaire. Nous définissons une méthode `updateQuery` pour `UPDATE` un enregistrement que nous allons définir. Cette opération changera la valeur `age` pour une entrée dont le nom est égal à `Trevor`. 

Vous vous souvenez peut-être que l'âge de Trevor était précédemment indiqué comme étant 25. Nous allons le mettre à jour à 30. Tout le reste fonctionnera de la même manière qu'avant, y compris la fermeture de la connexion lorsque nous aurons terminé.

Cette section de code du troisième fichier supprimera un enregistrement :

```
const deleteQuery = `DELETE FROM users WHERE name = ?`;
const deletedName = 'name1';
db.run(deleteQuery, [deletedName], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Deleted ${this.changes} row(s)`);
    }
});

```

Le code ci-dessus supprimera l'enregistrement où le nom est égal à `Trevor`.

Vous pouvez exécuter l'un de ces fichiers en utilisant la commande `node`. Mais vous devez d'abord vous assurer d'avoir installé le module `sqlite3` :

```
$ npm install sqlite3
```

Ensuite, j'utiliserai `node` pour exécuter le premier fichier (que vous pourriez choisir d'appeler `db.js`). 

```
$ node db.js
Inserted data with id 1
```

Nous verrons qu'un nouvel enregistrement a été inséré avec succès. Si vous listez le contenu du répertoire, vous verrez également qu'un nouveau fichier `mydatabase.db` a été créé.

Vous pouvez toujours vous connecter manuellement à sqlite3 pour voir comment les choses ont pu changer. Je vais référencer le fichier `mydatabase.db` afin que nous puissions l'ouvrir immédiatement. 

```
$ sqlite3 mydatabase.db
```

En tapant `.tables` dans l'interface SQLite, vous listerez toutes les tables existantes dans cette base de données. Dans notre cas, ce sera la table `users` que nous avons créée. 

```
sqlite> .tables
users
sqlite>
```

Maintenant, j'utiliserai la commande SQL `select` pour afficher un enregistrement. Ici, j'utiliserai l'astérisque pour représenter tous les enregistrements et spécifier la table `users`. 

```
sqlite> SELECT * FROM users;
1|Trevor|25
sqlite>
```

Nous pouvons voir que l'enregistrement `1` contenant `Trevor` qui a 25 ans a été créé. Super !

Enfin, nous pouvons exécuter le code `delete` qui devrait supprimer Trevor complètement :

```
const deleteQuery = `DELETE FROM users WHERE name = ?`;
const deletedName = 'Trevor';
db.run(deleteQuery, [deletedName], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Deleted ${this.changes} row(s)`);
    }
});
```

Je devrais noter que le format `db.run` et `db.close` que j'ai utilisé pour ces méthodes peut également être appelé `Database.run()`, et `database.close()`. C'est simplement une question de préférence - ou, dans mon cas, de paresse. Je suis un administrateur Linux, après tout, et les meilleurs administrateurs sont, en principe, paresseux.

## Résumé

Nous avons vu comment utiliser JavaScript pour se connecter à une base de données back-end, créer une nouvelle table, puis ajouter, modifier et supprimer des enregistrements dans cette table. Et nous semblons nous en être sortis, aussi ! 

Maintenant, essayez cela sur votre propre ordinateur. Mais jouez avec les valeurs. Encore mieux : construisez quelque chose de pratique.

_Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_