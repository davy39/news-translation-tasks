---
title: SQL Select – Exemples de déclarations et de requêtes
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-24T18:07:46.000Z'
originalURL: https://freecodecamp.org/news/sql-select-statement-and-query-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--17-.png
tags:
- name: beginner
  slug: beginner
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL Select – Exemples de déclarations et de requêtes
seo_desc: 'Structured Query Language (SQL) is a programming language that you use
  to manage data in relational databases. You can use SQL to create, read, update,
  and delete (CRUD) data in a relational database.

  You can write SQL queries to insert data with INS...'
---

Structured Query Language (SQL) est un langage de programmation que vous utilisez pour gérer des données dans des bases de données relationnelles. Vous pouvez utiliser SQL pour créer, lire, mettre à jour et supprimer (CRUD) des données dans une base de données relationnelle.

Vous pouvez écrire des requêtes SQL pour insérer des données avec INSERT, lire des données avec SELECT, mettre à jour avec UPDATE et supprimer des données avec DELETE.

Cet article vous apprendra à écrire des requêtes SQL SELECT. Vous apprendrez les différentes façons d'écrire ces requêtes et quels résultats attendre.

## Comment utiliser la déclaration SQL SELECT

Vous pouvez utiliser la déclaration SQL SELECT pour récupérer des données d'une table de base de données spécifiée.

Vous pouvez écrire votre déclaration de diverses manières pour obtenir les données exactes que vous souhaitez. Ces données sont extraites de la table de la base de données et retournées sous forme de table.

```sql
// Syntaxe

SELECT expression(s)
FROM table(s)
[WHERE condition(s)]
[ORDER BY expression(s) [ ASC | DESC ]];
```

Le code précédent est une syntaxe très détaillée qui englobe beaucoup d'informations que je vais expliquer avec des exemples.

Commençons par passer en revue les paramètres et arguments :

* **expression(s)** : Cela représente la ou les colonnes dont vous souhaitez récupérer les données ou toutes les colonnes de la table en utilisant un astérisque (`*`).

* **table(s)** : Le nom de la ou des tables à partir desquelles vous souhaitez récupérer des enregistrements. La clause FROM doit inclure au moins une table.

* **WHERE condition(s)** : Il s'agit d'un champ facultatif. Cela vous permet de spécifier une condition qui guidera les données récupérées pour la ou les colonnes spécifiées. Si aucune condition n'est spécifiée, tous les enregistrements seront choisis.

* **ORDER BY expression(s)** : Il s'agit d'un champ facultatif. Cela vous permet de déclarer une colonne dont les données seront utilisées pour trier les résultats. Une virgule doit séparer les valeurs si vous fournissez plus d'une expression.

* **ASC** : Il s'agit d'une valeur d'expression facultative. ASC trie le jeu de résultats par expression dans l'ordre croissant. Si cela n'est pas spécifié, il s'agit du comportement par défaut.

* **DESC** : Il s'agit d'une valeur d'expression facultative. DESC trie le jeu de résultats par expression dans l'ordre décroissant.

## Requêtes SQL Select

Supposons que vous avez une base de données avec le nom "Users" et contenant les données suivantes :

| user\_id | first\_name | last\_name | age | status |
| --- | --- | --- | --- | --- |
| 1 | John | Doe | 33 | Married |
| 2 | Alice | Truss | 23 | Single |
| 3 | David | Bohle | 56 | Married |
| 4 | Aaron | Ben | 34 | Single |
| 5 | Louis | Vic | 72 | Married |
| 6 | Charles | Chris | 19 | Single |

Explorons maintenant diverses requêtes et voyons comment elles fonctionnent.

### SQL Select All

Vous pourriez avoir besoin de sélectionner toutes les colonnes d'une base de données. Au lieu de lister chaque colonne, vous pouvez utiliser le caractère astérisque (`*`).

```sql
SELECT *
FROM Users;
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666430594839_Untitled.drawio+19.png align="left")

### SQL Select Specified Columns

Vous pouvez également récupérer des colonnes spécifiées au lieu de toutes les colonnes en listant les colonnes et en les séparant par une virgule :

```sql
SELECT first_name, last_name
FROM Users;
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666441467406_Untitled.drawio+27.png align="left")

### SQL Select WHERE Clause

Vous pouvez vouloir retourner uniquement les lignes qui satisfont une condition spécifique. Cette condition peut être spécifiée en utilisant la clause facultative `WHERE`. La clause `WHERE` vous permet de récupérer des enregistrements d'une table de base de données qui correspondent à une ou plusieurs conditions données.

Par exemple, supposons que vous ne souhaitez récupérer que les utilisateurs dont le statut est "single" :

```sql
SELECT *
FROM Users
WHERE status = 'Single';
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666431175784_Untitled.drawio+21.png align="left")

Généralement, la clause WHERE est utilisée pour filtrer les résultats. Vous pouvez également utiliser des opérateurs courants comme `=`, que vous avez utilisé, et d'autres comme `<`, `>`, `<=`, `>=`, `AND`, `BETWEEN` et `IN`.

### SELECT Using Equality Operators

Supposons que vous souhaitez récupérer uniquement les utilisateurs dont l'âge est supérieur à 30. Votre requête sera alors :

```sql
SELECT *
FROM Users
WHERE age > 30;
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666431269376_Untitled.drawio+22.png align="left")

Vous pouvez également utiliser d'autres opérateurs d'égalité comme `<`, `<=` et `>=`.

### SELECT Using the AND Operator

Vous pouvez souvent vouloir utiliser plus d'une condition pour filtrer le contenu de la table. Vous pouvez le faire avec l'opérateur AND.

```sql
SELECT *
FROM Users
WHERE status = 'Single' AND age > 30;
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666433362143_Untitled.drawio+23.png align="left")

### SELECT Using the BETWEEN Operator

Vous utilisez l'opérateur BETWEEN pour obtenir la plage de données que vous souhaitez filtrer. Vous pouvez décider d'utiliser l'opérateur d'égalité et AND, mais BETWEEN offre une meilleure syntaxe.

```sql
SELECT *
FROM Users
WHERE age BETWEEN 20 AND 30;
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666433680877_Untitled.drawio+24.png align="left")

### SELECT Using the IN Operator

De plus, l'opérateur `IN` vous permet de définir plus d'une base exacte pour filtrer chaque ligne. Par exemple, vous pouvez récupérer uniquement les lignes dont la valeur est dans les crochets définis :

```sql
SELECT *
FROM Users
WHERE age IN (56,33,10);
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666433956123_Untitled.drawio+26.png align="left")

### SQL Select ORDER BY Clause

Jusqu'à présent, vous avez appris à récupérer des données de votre table avec SQL, mais vous remarquerez que ces données suivent toujours l'ordre d'origine. Vous pouvez ajuster l'ordre dans lequel les données sont récupérées en utilisant la clause ORDER BY.

Deux options principales sont l'ordre croissant (`ASC`) et décroissant (`DESC`). Par exemple, vous pouvez vouloir que les lignes de votre table soient disposées dans l'ordre croissant en fonction du `first_name` :

```sql
SELECT *
FROM Users
ORDER BY first_name ASC;
```

Voici à quoi ressemblera votre sortie lorsque vous utiliserez cette commande sur la table des utilisateurs :

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666441975760_Untitled.drawio+28.png align="left")

> **Note :** Vous pouvez toujours combiner ces options et clauses dans une seule requête pour récupérer exactement ce que vous voulez.

## Conclusion

Dans cet article, vous avez appris à utiliser la requête SQL SELECT pour récupérer des données d'une base de données relationnelle. D'autres options sont disponibles, mais ce sont celles que vous utiliserez probablement régulièrement.

Amusez-vous bien à coder !