---
title: Questions d'entretien SQL courantes pour Amazon, Apple, Google
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-02T16:57:00.000Z'
originalURL: https://freecodecamp.org/news/common-sql-interview-questions
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9faf740569d1a4ca43fc.jpg
tags:
- name: interview
  slug: interview
- name: SQL
  slug: sql
seo_title: Questions d'entretien SQL courantes pour Amazon, Apple, Google
seo_desc: SQL is used in a wide variety of programming jobs. It's important to be
  familiar with SQL if you are going to be interviewing soon for a software position.
  This is especially true if you are going to interview at a top tech company such
  as Amazon, Ap...
---

SQL est utilisé dans une grande variété d'emplois en programmation. Il est important de bien connaître SQL si vous allez bientôt passer un entretien pour un poste en logiciel. Cela est particulièrement vrai si vous allez passer un entretien dans une grande entreprise technologique comme Amazon, Apple ou Google. 

Ce guide couvrira la syntaxe SQL de base comme rappel, puis listera quelques questions d'entretien SQL courantes. Les réponses à toutes les questions sont fournies et vous pouvez utiliser ces informations pour étudier pour votre entretien de programmation.

## **Exemple de syntaxe SQL de base**

SQL est une norme internationale (ISO), mais vous trouverez quelques différences entre les implémentations. Ce guide utilise MySQL comme exemple car c'est l'implémentation la plus populaire de SQL. 

### **Comment utiliser une base de données spécifique**

Voici la commande SQL utilisée pour sélectionner la base de données contenant les tables pour vos instructions SQL :

```sql
USE fcc_sql_guides_database; 

```

### **Clauses SELECT et FROM**

Utilisez SELECT pour déterminer quelles colonnes des données vous souhaitez afficher dans les résultats. Il existe également des options que vous pouvez utiliser pour afficher des données qui ne sont pas une colonne de table.

L'exemple suivant montre deux colonnes sélectionnées dans la table « student », et deux colonnes calculées. La première des colonnes calculées est un nombre sans signification, et l'autre est la date du système.

```sql
SELECT studentID, FullName, 3+2 AS five, now() AS currentDate FROM student;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax01.JPG)

### **Clause WHERE**

La clause WHERE spécifie une condition lors de la récupération des données. La clause WHERE est utilisée pour limiter le nombre de lignes retournées. Elle est souvent utilisée dans une instruction SELECT mais peut également être utilisée dans d'autres instructions telles que UPDATE et DELETE.

Voici la syntaxe de base de la clause WHERE :

```sql
SELECT column1, column2
FROM table_name
WHERE [condition]
```

La condition dans une clause WHERE peut inclure des opérateurs logiques comme >, <, =, LIKE, NOT, AND, OR.

Voici un exemple d'instruction SQL utilisant la clause WHERE. Elle spécifie que si l'un des étudiants a certains scores SAT (1000, 1400), ils ne seront pas présentés :

```
SELECT studentID, FullName, sat_score, recordUpdated
FROM student
WHERE (studentID BETWEEN 1 AND 5
    OR studentID = 8
    OR FullName LIKE '%Maximo%')
    AND sat_score NOT IN (1000, 1400);

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax02.JPG)

### **ORDER BY (ASC, DESC)**

ORDER BY nous donne un moyen de trier le jeu de résultats par un ou plusieurs des éléments de la section SELECT.

Voici la même liste que ci-dessus, mais triée par le nom complet de l'étudiant. L'ordre de tri par défaut est ascendant (ASC), mais pour trier dans l'ordre inverse (descendant), vous utilisez DESC, comme dans l'exemple ci-dessous :

```sql
SELECT studentID, FullName, sat_score
FROM student
WHERE (studentID BETWEEN 1 AND 5
    OR studentID = 8
    OR FullName LIKE '%Maximo%')
    AND sat_score NOT IN (1000, 1400)
ORDER BY FullName DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax03.JPG)

### **GROUP BY et HAVING**

GROUP BY nous donne un moyen de combiner des lignes et d'agréger des données. La clause HAVING est similaire à la clause WHERE ci-dessus, sauf qu'elle agit sur les données groupées.

L'instruction SQL ci-dessous répond à la question : « Quels candidats ont reçu le plus grand nombre de contributions (ordonnées par compte (*)) en 2016, mais seulement ceux qui avaient plus de 80 contributions ? »

Ordonner cet ensemble de données dans un ordre décroissant (DESC) place les candidats avec le plus grand nombre de contributions en haut de la liste.

```
SELECT Candidate, Election_year, SUM(Total_$), COUNT(*)
FROM combined_party_data
WHERE Election_year = 2016
GROUP BY Candidate, Election_year
HAVING count(*) > 80
ORDER BY count(*) DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax04.JPG)

## Questions d'entretien SQL courantes

### **Qu'est-ce qu'une jointure interne en SQL ?**

Il s'agit du type de jointure par défaut si aucune jointure n'est spécifiée. Elle retourne toutes les lignes pour lesquelles il y a au moins une correspondance dans les deux tables.

```sql
SELECT * FROM A x JOIN B y ON y.aId = x.Id
```

### **Qu'est-ce qu'une jointure gauche en SQL ?**

Une jointure gauche retourne toutes les lignes de la table de gauche, et les lignes correspondantes de la table de droite. Les lignes de la table de gauche seront retournées même s'il n'y avait aucune correspondance dans la table de droite. Les lignes de la table de gauche sans correspondance dans la table de droite auront `null` pour les valeurs de la table de droite.

```sql
SELECT * FROM A x LEFT JOIN B y ON y.aId = x.Id
```

### **Qu'est-ce qu'une jointure droite en SQL ?**

Une jointure droite retourne toutes les lignes de la table de droite, et les lignes correspondantes de la table de gauche. Contrairement à une jointure gauche, cela retournera toutes les lignes de la table de droite même s'il n'y a pas de correspondance dans la table de gauche. Les lignes de la table de droite qui n'ont pas de correspondance dans la table de gauche auront des valeurs `null` pour les colonnes de la table de gauche.

```sql
SELECT * FROM A x RIGHT JOIN B y ON y.aId = x.Id
```

### **Qu'est-ce qu'une jointure complète ou jointure externe complète en SQL ?**

Une jointure externe complète et une jointure complète sont la même chose. La jointure externe complète ou jointure complète retourne toutes les lignes des deux tables, en faisant correspondre les lignes chaque fois qu'une correspondance peut être faite et en plaçant des NULLs aux endroits où aucune ligne correspondante n'existe.

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName
```

### **Quel est le résultat de la commande suivante ?**

```sql
DROP VIEW view_name
```

Cela entraînera une erreur car vous ne pouvez pas effectuer une opération DML sur une vue. Une opération DML est toute opération qui manipule les données telles que DROP, INSERT, UPDATE et DELETE.

### **Pouvons-nous effectuer un rollback après avoir utilisé la commande ALTER ?**

Non, car ALTER est une commande DDL et le serveur Oracle effectue un COMMIT automatique lorsque les instructions DDL sont exécutées. Les instructions DDL définissent des structures de données telles que `CREATE table` et `ALTER table`.

### **Quelle est la seule contrainte qui impose des règles au niveau des colonnes ?**

NOT NULL est la seule contrainte qui fonctionne au niveau des colonnes.

### **Quelles sont les pseudocolonnes en SQL ? Donnez quelques exemples ?**

Une pseudocolonne se comporte comme une colonne, mais n'est pas réellement stockée dans la table car elle est générée. Les valeurs d'une pseudocolonne peuvent être sélectionnées mais elles ne peuvent pas être insérées, mises à jour ou supprimées. 

```
ROWNUM, ROWID, USER, CURRVAL, NEXTVAL etc.
```

### Créer un utilisateur "my723acct" avec le mot de passe "kmd26pt". Utilisez les tablespaces "user_data" et "temporary_data" fournis par PO8 et attribuez à cet utilisateur 10 Mo d'espace de stockage dans "user_data" et 5 Mo d'espace de stockage dans "temporary_data".

```sql
CREATE USER my723acct IDENTIFIED BY kmd26pt
DEFAULT TABLESPACE user_data
TEMPORARY TABLESPACE temporary_data
QUOTA 10M on user_data QUOTA 5M on temporary_data
```

### **Créer le rôle** _role_tables_and_views_**.**

```sql
CREATE ROLE role_tables_and_views
```

### **Accorder au rôle de la question précédente les privilèges de se connecter à la base de données et les privilèges de créer des tables et des vues.**

Le privilège de se connecter à la base de données est CREATE SESSION. Le privilège de créer une table est CREATE TABLE. Le privilège de créer une vue est CREATE VIEW.

```sql
    GRANT CREATE SESSION, CREATE TABLE, CREATE VIEW TO role_tables_and_views
```

### **Accorder le rôle précédent de la question aux utilisateurs _anny_ et _rita_.**

```sql
    GRANT role_tables_and_views TO anny, rita
```

### **Écrire une commande pour changer le mot de passe de l'utilisateur _rita_ de "abcd" à "dfgh"**

```sql
    ALTER USER rita IDENTIFIED BY dfgh
```

### Les utilisateurs _rita_ et _anny_ n'ont pas de privilèges SELECT sur la table INVENTORY qui a été créée par _scott_. Écrire une commande pour permettre à _scott_ d'accorder aux utilisateurs des privilèges SELECT sur ces tables.

```sql
    GRANT select ON inventory TO rita, anny
```

### **L'utilisateur** _**rita**_ **a été transféré et n'a plus besoin du privilège qui lui a été accordé par le rôle** _role_tables_and_views_. Écrire une commande pour lui retirer ses privilèges précédemment accordés. Elle doit toujours pouvoir se connecter à la base de données.

```sql
REVOKE select ON scott.inventory FROM rita
REVOKE create table, create view FROM rita
```

### **L'utilisateur _rita_ qui a été transféré part maintenant pour une autre entreprise. Puisque les objets qu'elle a créés ne sont plus utilisés, écrire une commande pour supprimer cet utilisateur et tous ses objets.**

L'option CASCADE est nécessaire pour supprimer tous les objets de l'utilisateur dans la base de données.

```sql
DROP USER rita CASCADE
```

### **Écrire une requête SQL pour trouver le n-ième "Salaire" le plus élevé de la table "Employee".**

```sql
   SELECT TOP 1 Salary
   FROM (
      SELECT DISTINCT TOP N Salary
      FROM Employee
      ORDER BY Salary DESC
      )
    ORDER BY Salary ASC
```

## Conclusion

Si vous pensez pouvoir répondre à toutes ces questions, vous êtes peut-être prêt pour votre entretien. Bonne chance !