---
title: Insert Into SQL – Comment insérer dans une table avec une requête [Exemple
  de déclaration]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-10-06T16:10:50.000Z'
originalURL: https://freecodecamp.org/news/insert-into-sql-how-to-insert-into-a-table-query-example-statement
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/caspar-camille-rubin-fPkvU7RDmCo-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Insert Into SQL – Comment insérer dans une table avec une requête [Exemple
  de déclaration]
seo_desc: "If you want to add data to your SQL table, then you can use the INSERT\
  \ statement. \nIn this article, I will show you how to use the INSERT statement\
  \ to add a single row, multiple rows, and to copy rows from one SQL table to another.\n\
  Basic INSERT synta..."
---

Si vous souhaitez ajouter des données à votre table SQL, vous pouvez utiliser l'instruction `INSERT`.

Dans cet article, je vais vous montrer comment utiliser l'instruction `INSERT` pour ajouter une seule ligne, plusieurs lignes, et pour copier des lignes d'une table SQL à une autre.

## Syntaxe de base de INSERT

Voici la syntaxe de base pour ajouter des lignes à une table en SQL :

```sql
INSERT INTO table_name (column1, column2, column3, etc)
VALUES (value1, value2, value3, etc);
```

La première ligne de code utilise l'instruction `INSERT` suivie du nom de la table dans laquelle vous souhaitez ajouter les données. Après le nom de la table, vous devez spécifier les noms des colonnes.

La deuxième ligne de code est celle où vous ajouterez les valeurs pour les lignes. Il est important que le nombre de valeurs corresponde au nombre de colonnes spécifiées, sinon vous obtiendrez un message d'erreur.

## Comment ajouter une ligne à une table SQL

Dans cet exemple, nous avons une table appelée `dogs` avec les colonnes `id`, `name` et `gender`. Nous voulons ajouter un chien appelé `AXEL`.

Voici à quoi ressemble le code pour ajouter `AXEL` à la table :

```sql
INSERT INTO dogs(id, name, gender) VALUES (1, 'AXEL', 'M');
```

Voici à quoi ressemble la table.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.19.41-AM.png)

## Que se passe-t-il si le nombre de valeurs ne correspond pas aux colonnes ?

Comme mentionné précédemment, le nombre de colonnes doit correspondre au nombre de valeurs.

Si je modifie le code pour supprimer une valeur, j'obtiens un message d'erreur.

```sql
INSERT INTO dogs(id, name, gender) VALUES (1, 'AXEL');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.22.25-AM.png)

Puisque nous avons spécifié 3 colonnes, nous devons fournir trois valeurs pour chaque ligne ajoutée à la table.

## Que se passe-t-il si vous ignorez les contraintes de colonne ?

Lorsque vous créez des tables SQL, vous ajoutez des contraintes de colonne qui servent de règles pour la colonne.

Dans notre table `dogs`, les colonnes `name` et `gender` ont une contrainte `NOT NULL`. Cette règle signifie qu'une valeur ne peut pas être absente de la ligne.

Lorsque j'essaie d'ajouter `NULL` pour le `gender`, je reçois un message d'erreur.

```sql
INSERT INTO dogs(id, name, gender) VALUES (1, 'AXEL', NULL);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.46.44-AM.png)

Toutes les contraintes que vous avez spécifiées lors de la création de votre table SQL doivent être respectées lors de l'ajout de lignes.

## Comment ajouter plusieurs lignes à une table en SQL

Si vous souhaitez ajouter plusieurs lignes à une table en une seule fois, vous pouvez utiliser cette syntaxe :

```sql
INSERT INTO table_name (column1, column2, column3, etc)
VALUES 
	(value1, value2, value3, etc),
    (value1, value2, value3, etc),
    (value1, value2, value3, etc);
```

Il est important de se souvenir des virgules entre chaque ligne, sinon vous obtiendrez un message d'erreur.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.58.22-AM.png)

Voici à quoi ressemblerait le code pour ajouter huit chiens à la table en une seule fois :

```sql
INSERT INTO dogs(id, name, gender) 
VALUES 
    (1, 'AXEL', 'M'),
    (2, 'Annie', 'F'),
    (3, 'Ace', 'M'),
    (4, 'Zelda', 'F'),
    (5, 'Diesel', 'M'),
    (6, 'Tilly', 'F'),
    (7, 'Leroy', 'M'),
    (8, 'Olivia', 'F');
```

Voici à quoi ressemble la table maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-6.00.14-AM.png)

## Comment copier des lignes d'une table et les insérer dans une autre table

Vous pouvez utiliser les instructions `SELECT` et `INSERT` pour copier des lignes d'une table SQL à une autre.

Voici la syntaxe de base :

```sql
INSERT INTO table_name1 (columns) 
SELECT columns FROM table_name2;
```

Dans cet exemple, j'ai créé une table `cats` avec trois lignes ayant les mêmes noms de colonnes que la table `dogs`.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-6.26.46-AM.png)

Nous pouvons ajouter toutes les données `cats` dans la table `dogs` en utilisant le code suivant :

```sql
INSERT INTO dogs SELECT * FROM  cats;
```

Voici à quoi ressemble la nouvelle table `dogs` avec les `cats` supplémentaires :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-6.27.43-AM.png)

## Conclusion

Si vous souhaitez ajouter des données à votre table SQL, vous pouvez utiliser l'instruction `INSERT`.

Voici la syntaxe de base pour ajouter des lignes à votre table SQL :

```sql
INSERT INTO table_name (column1, column2, column3, etc)
VALUES (value1, value2, value3, etc);
```

La deuxième ligne de code est celle où vous ajouterez les valeurs pour les lignes. Il est important que le nombre de valeurs corresponde au nombre de colonnes spécifiées, sinon vous obtiendrez un message d'erreur.

Lorsque vous essayez d'ignorer les contraintes de colonne lors de l'ajout de lignes à la table, vous recevrez un message d'erreur.

Si vous souhaitez ajouter plusieurs lignes à une table en une seule fois, vous pouvez utiliser cette syntaxe :

```sql
INSERT INTO table_name (column1, column2, column3, etc)
VALUES 
	(value1, value2, value3, etc),
    (value1, value2, value3, etc),
    (value1, value2, value3, etc);
```

Vous pouvez utiliser les instructions `SELECT` et `INSERT` pour copier des lignes d'une table SQL à une autre.

Voici la syntaxe de base :

```sql
INSERT INTO table_name1 (columns) 
SELECT columns FROM table_name2;
```

J'espère que vous avez apprécié cet article et je vous souhaite bonne chance dans votre apprentissage de SQL.