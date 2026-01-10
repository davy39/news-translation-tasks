---
title: 'Questions d''entretien SQL courantes : Votre aide-mémoire de base de données'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T22:48:00.000Z'
originalURL: https://freecodecamp.org/news/sql-interview-questions
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/sql-interview.jpeg
tags:
- name: database
  slug: database
- name: interview
  slug: interview
- name: SQL
  slug: sql
seo_title: 'Questions d''entretien SQL courantes : Votre aide-mémoire de base de données'
seo_desc: 'The following are some of the most commonly-asked SQL questions in job
  interviews.

  By understanding these, you will be better-prepared for your upcoming technical
  interviews.

  What is an inner join in SQL?

  This is the default type of join if no join i...'
---

Voici quelques-unes des questions SQL les plus fréquemment posées lors des entretiens d'embauche.

En les comprenant, vous serez mieux préparé pour vos prochains entretiens techniques.

### Qu'est-ce qu'une jointure interne en SQL ?

Il s'agit du type de jointure par défaut si aucune jointure n'est spécifiée. Elle retourne toutes les lignes pour lesquelles il y a au moins une correspondance dans les deux tables.

```
SELECT * FROM A x JOIN B y ON y.aId = x.Id

```

### Qu'est-ce qu'une jointure gauche en SQL ?

Une jointure gauche retourne toutes les lignes de la table de gauche et les lignes correspondantes de la table de droite. Les lignes de la table de gauche seront retournées même s'il n'y a pas de correspondance dans la table de droite. Les lignes de la table de gauche sans correspondance dans la table de droite auront des valeurs `null` pour les colonnes de la table de droite.

```
SELECT * FROM A x LEFT JOIN B y ON y.aId = x.Id

```

### Qu'est-ce qu'une jointure droite en SQL ?

Une jointure droite retourne toutes les lignes de la table de droite et les lignes correspondantes de la table de gauche. Contrairement à une jointure gauche, cela retournera toutes les lignes de la table de droite même s'il n'y a pas de correspondance dans la table de gauche. Les lignes de la table de droite qui n'ont pas de correspondance dans la table de gauche auront des valeurs `null` pour les colonnes de la table de gauche.

```
SELECT * FROM A x RIGHT JOIN B y ON y.aId = x.Id

```

### Qu'est-ce qu'une jointure complète en SQL ?

Une jointure complète retourne toutes les lignes pour lesquelles il y a une correspondance dans l'une ou l'autre des tables. Ainsi, si des lignes de la table de gauche n'ont pas de correspondance dans la table de droite, elles seront incluses. De même, si des lignes de la table de droite n'ont pas de correspondance dans la table de gauche, elles seront incluses.

```
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName

```

### Quel est le résultat de la commande suivante ?

```
  DROP VIEW view_name

```

Ici, ce sera une erreur car nous ne pouvons pas effectuer une opération DML sur une vue.

### Peut-on effectuer un rollback après avoir utilisé la commande ALTER ?

Non, car ALTER est une commande DDL et le serveur Oracle effectue un COMMIT automatique lorsque les instructions DDL sont exécutées.

### Quelle est la seule contrainte qui impose des règles au niveau des colonnes ?

NOT NULL est la seule contrainte qui fonctionne au niveau des colonnes.

### Quelles sont les pseudocolonnes en SQL ? Donnez quelques exemples.

Une pseudocolonne est une fonction qui retourne une valeur générée par le système. La raison pour laquelle elle est appelée ainsi est qu'une pseudocolonne est une valeur assignée par Oracle, utilisée dans le même contexte qu'une colonne de base de données Oracle mais non stockée sur disque.

```
    ROWNUM, ROWID, USER, CURRVAL, NEXTVAL, etc.

```

### Créez un utilisateur my723acct avec le mot de passe kmd26pt. Utilisez les tablespaces user_data et temporary_data fournis par PO8 et attribuez à cet utilisateur 10 Mo d'espace de stockage dans user_data et 5 Mo d'espace de stockage dans temporary_data.

```
    CREATE USER my723acct IDENTIFIED BY kmd26pt
    DEFAULT TABLESPACE user_data
    TEMPORARY TABLESPACE temporary_data
    QUOTA 10M on user_data QUOTA 5M on temporary_data

```

### Créez le rôle role_tables_and_views.

```
    CREATE ROLE role_tables_and_views

```

### Accordez au rôle de la question précédente les privilèges de se connecter à la base de données et les privilèges de créer des tables et des vues.

Le privilège de se connecter à la base de données est CREATE SESSION. Le privilège de créer une table est CREATE TABLE. Le privilège de créer une vue est CREATE VIEW.

```
    GRANT Create session, create table, create view TO role_tables_and_views

```

### Accordez le rôle précédent de la question aux utilisateurs anny et rita.

```
    GRANT role_tables_and_views TO anny, rita

```

### Créez un utilisateur my723acct avec le mot de passe kmd26pt. Utilisez les tablespaces user_data et temporary_data fournis par PO8 et attribuez à cet utilisateur 10 Mo d'espace de stockage dans user_data et 5 Mo d'espace de stockage dans temporary_data.

```
    CREATE USER my723acct IDENTIFIED BY kmd26pt
    DEFAULT TABLESPACE user_data
    TEMPORARY TABLESPACE temporary_data
    QUOTA 10M on user_data QUOTA 5M on temporary_data

```

### Créez le rôle role_tables_and_views.

```
    CREATE ROLE role_tables_and_views

```

### Accordez au rôle de la question précédente les privilèges de se connecter à la base de données et les privilèges de créer des tables et des vues.

Le privilège de se connecter à la base de données est CREATE SESSION. Le privilège de créer une table est CREATE TABLE. Le privilège de créer une vue est CREATE VIEW.

```
    GRANT Create session, create table, create view TO role_tables_and_views

```

### Accordez le rôle précédent de la question aux utilisateurs anny et rita.

```
    GRANT role_tables_and_views TO anny, rita

```

### Écrivez une commande pour changer le mot de passe de l'utilisateur rita de abcd à dfgh.

```
    ALTER USER rita IDENTIFIED BY dfgh

```

Les utilisateurs rita et anny n'ont pas de privilèges SELECT sur la table INVENTORY créée par SCOTT. Écrivez une commande pour permettre à SCOTT d'accorder aux utilisateurs des privilèges SELECT sur ces tables.

```
    GRANT select ON inventory TO rita, anny

```

L'utilisateur rita a été transféré et n'a plus besoin des privilèges qui lui avaient été accordés via le rôle role_tables_and_views. Écrivez une commande pour lui retirer ses privilèges précédents, sauf celui de se connecter à la base de données.

```
    REVOKE select ON scott.inventory FROM rita
    REVOKE create table, create view FROM rita

```

L'utilisateur rita, qui a été transféré, quitte maintenant pour une autre entreprise. Comme les objets qu'elle a créés ne sont plus utiles, écrivez une commande pour supprimer cet utilisateur et tous ses objets.

Ici, l'option CASCADE est nécessaire pour supprimer tous les objets de l'utilisateur dans la base de données.

```
   DROP USER rita CASCADE

### L'utilisateur rita a été transféré et n'a plus besoin des privilèges qui lui avaient été accordés via le rôle role_tables_and_views. Écrivez une commande pour lui retirer ses privilèges précédents, sauf celui de se connecter à la base de données.
``` sql    
    REVOKE select ON scott.inventory FROM rita
    REVOKE create table, create view FROM rita

```

L'utilisateur rita, qui a été transféré, quitte maintenant pour une autre entreprise. Comme les objets qu'elle a créés ne sont plus utiles, écrivez une commande pour supprimer cet utilisateur et tous ses objets.

Ici, l'option CASCADE est nécessaire pour supprimer tous les objets de l'utilisateur dans la base de données.

```
   DROP USER rita CASCADE

```

### Écrivez une requête SQL pour trouver le n-ième salaire le plus élevé dans une table.

```
   SELECT TOP 1 Salary
   FROM (
      SELECT DISTINCT TOP N Salary
      FROM Employee
      ORDER BY Salary DESC
      )
    ORDER BY Salary ASC

```