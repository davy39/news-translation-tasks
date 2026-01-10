---
title: Jointures SQL – LEFT Join, RIGHT Join et INNER Join expliqués
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-01-10T18:23:24.000Z'
originalURL: https://freecodecamp.org/news/understanding-sql-joins
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/JOIN-s.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Jointures SQL – LEFT Join, RIGHT Join et INNER Join expliqués
seo_desc: 'SQL is a programming language we use to interact with relational databases.
  SQL databases contain tables, which contain rows of data. These tables usually contain
  similar or related data.

  In an office management web application database, you would ha...'
---

SQL est un langage de programmation que nous utilisons pour interagir avec les bases de données relationnelles. Les bases de données SQL contiennent des tables, qui contiennent des lignes de données. Ces tables contiennent généralement des données similaires ou liées.

Dans une base de données d'application web de gestion de bureau, vous auriez des tables pour les `employees` (employés), leurs `departments` (départements), leurs `managers` (responsables), les `projects` (projets) sur lesquels ils travaillent, et ainsi de suite en fonction de la structure de votre application.

Dans la table `employees`, vous trouveriez des données comme l'ID de l'employé, le nom, le salaire, l'ID du département (utilisé pour lier l'employé au département), et d'autres champs qui correspondent à vos besoins. Les autres tables contiendraient également des données pour leurs entités spécifiques.

## **Qu'est-ce que les Jointures ?**

Si vous devez jamais rassembler plusieurs tables de votre base de données pour accéder aux données, vous utilisez une JOINTURE.

Les jointures vous permettent de récupérer des données qui sont dispersées dans plusieurs tables. Par exemple, en utilisant les tables de base de données que nous allons créer dans un instant, nous pourrons obtenir tous les détails d'un employé, ainsi que le nom de son responsable et le département dans lequel il travaille, en utilisant une jointure.

Une jointure vous permet d'utiliser une seule requête pour y parvenir. Vous utilisez une jointure parce que vous ne pouvez obtenir ces données qu'en rassemblant les données des tables `employees`, `departments` et `projects`. En termes simples, vous JOINDRIEZ ces tables ensemble.

Pour effectuer une jointure, vous utilisez le mot-clé **JOIN**. Et nous verrons comment cela fonctionne dans ce tutoriel.

### Prérequis :

Pour continuer avec ce tutoriel, vous devez connaître les bases des opérations d'insertion et de récupération avec SQL.

De plus, vous pouvez configurer une base de données de démonstration que nous utiliserons pour cet article. La base de données doit avoir des tables comme ceci :

```sql
CREATE TABLE employees (
    id int,
    emp_name varchar(100),
    salary int,
    dept_id int,
    manager_id int
);

INSERT INTO employees 
VALUES (1, 'Idris', 1000, 1, 1), (2, 'Aweda', 2000, 2, 2), (3, 'Zubair', 3000, 3, 2), (4, 'Young', 4000, 3, 3), (5, 'Babu', 5000, 1, 3), (6, 'John', 1000, 8, 1);

CREATE TABLE departments (
    id int,
    dept_name varchar(100)
);

INSERT INTO departments
VALUES (1, 'Engineering'), (2, 'Product'), (3, 'Marketing'), (4, 'Support');

CREATE TABLE managers (
    id int,
    manager_name varchar(100),
    dept_id int
);

INSERT INTO managers
VALUES (1, 'Doe', 1), (2, 'Jane', 2), (3, 'May', 4);

CREATE TABLE projects (
    id int,
    project_name varchar(100),
    emp_id int
);

INSERT INTO projects
VALUES (1, 'Fintech App', 1), (1, 'Fintech App', 5), (1, 'Fintech App', 6), (2, 'Cooking Website', 1), (2, 'Cooking Website', 2);
```

## **Comment utiliser une jointure interne (INNER JOIN) en SQL**

Il existe de nombreux types de jointures en SQL, et chacune a un but différent.

La jointure interne est le type de jointure le plus basique. Elle est si basique que parfois, vous pouvez omettre le mot-clé JOIN et toujours effectuer une jointure interne.

Par exemple, disons que vous souhaitez récupérer le nom de tous les employés de l'organisation, ainsi que le nom de leurs départements. Dans une situation comme celle-ci, vous avez besoin de données à la fois de la table `employees` et de la table `departments`. Une simple jointure comme celle-ci ferait l'affaire :

```sql
SELECT e.emp_name, d.dept_name 
FROM employees e, departments d 
WHERE e.dept_id = d.id;
```

Alors, comment cela fonctionne-t-il réellement ? Pour commencer, regardez la partie `FROM` de la requête :

```sql
FROM employees e, departments d
```

Ici, les données sont récupérées depuis plus d'une table, et chaque table est aliasée. L'alias est très utile dans les scénarios où les deux tables ont des champs nommés de manière similaire, comme le champ `id` que les deux tables ont dans ce cas. Vous pourrez accéder aux différents champs facilement en utilisant l'alias court créé.

Ensuite, dans la partie `SELECT` de la requête, nous spécifions également les colonnes que nous voulons (et nous utilisons l'alias pour indiquer de quelle table provient chaque valeur) :

```sql
SELECT e.emp_name, d.dept_name
```

Et enfin, pour garantir que seules les valeurs correctes sont appariées les unes aux autres, la partie `WHERE` de la requête spécifie les conditions qui doivent être remplies pour que les données soient jointes.

```sql
WHERE e.dept_id = d.id;
```

Ainsi, pour le premier employé, le `dept_id` est `1`, donc nous récupérons le département avec `id = 1`, et son nom est retourné. Cela se produit pour autant de lignes qu'il y en a dans la table des employés.

Le résultat de la requête ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-15.45.09.png)
_Résultat de la requête JOIN_

Ici, remarquez que le nombre d'employés retournés est inférieur au nombre d'employés qui existent réellement. Cela est dû au fait que lorsque vous utilisez une INNER JOIN, _vous n'obtenez que les enregistrements qui existent dans les deux tables_.

C'est-à-dire que l'employé avec `id = 6` qui n'a pas été retourné a un `dept_id = 8`. Maintenant, ce département n'est pas dans la table `departments`, donc il n'a pas été retourné.

Une autre façon d'obtenir ce même résultat serait d'écrire explicitement la JOIN comme ceci :

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
JOIN departments d
ON (e.dept_id = d.id);
```

Ou utiliser l'INNER JOIN comme ceci :

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN departments d
ON (e.dept_id = d.id);
```

Ces requêtes retournent exactement le même résultat que la première. Mais elles sont plus lisibles car elles sont explicites.

Dans ces requêtes, vous sélectionnez depuis la table `employees`, puis vous joignez la table `departments` au résultat. Le ON dans la requête est utilisé pour spécifier les conditions sur lesquelles effectuer la JOIN. C'est la même chose que la condition WHERE dans la première requête.

### Cas d'utilisation de l'INNER JOIN

Dans les applications réelles, vous utilisez une INNER JOIN lorsque seuls les enregistrements qui existent dans les deux tables sont importants.

Par exemple, dans une application de gestion de stocks, vous pourriez avoir une table pour les `sales` (ventes), et une autre pour les `products` (produits). Maintenant, la table `sales` contiendra `product_id` (une référence au produit vendu), ainsi que d'autres détails comme `sold_at` (quand le produit a été vendu) et peut-être les détails du client.

La table `products`, en revanche, contiendra le `name` (nom), le `price` (prix), et peut-être la `quantity` (quantité) de chaque produit.

Maintenant, disons que c'est la fin de la semaine et que vous devez faire un rapport de ventes. Vous devrez récupérer tous les enregistrements de `sales`, ainsi que le nom et le prix du produit à afficher sur un tableau de bord ou à exporter sous forme de CSV. 

Pour ce faire, vous utiliseriez une INNER JOIN de la table `products` sur la table `sales`, car vous ne vous souciez pas des produits qui n'ont pas été vendus – vous voulez seulement voir chaque vente qui a été faite, et le nom et le prix du produit qui a été vendu. Tous les autres produits seront exclus de ce rapport.

## **Comment utiliser une jointure gauche (LEFT JOIN) en SQL**

Dans un autre scénario, vous pourriez vouloir récupérer tous les noms d'employés et les noms de leurs départements, mais cette fois sans laisser de côté aucun employé ou nom de département. Ici, vous utiliseriez une LEFT JOIN.

Dans une LEFT JOIN, _chaque enregistrement de la table de gauche, la table de base, sera retourné_. Ensuite, les valeurs de la table de droite, la table étant jointe, seront ajoutées là où elles existent.

La LEFT JOIN est également connue sous le nom de LEFT OUTER JOIN et vous pouvez les utiliser de manière interchangeable.

Ainsi, pour récupérer tous les noms d'employés et de départements, vous pouvez modifier la requête précédente pour utiliser LEFT JOIN, comme ceci :

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON (e.dept_id = d.id);
```

Le résultat de cette requête ressemble maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-15.55.10.png)
_Résultat de la LEFT JOIN_

Maintenant, l'employé avec `id = 6` et `dept_id = 8` est retourné, avec le nom du département défini comme NULL car il n'y a pas de département avec `id = 8`.

### Cas d'utilisation de la LEFT JOIN

Dans les applications réelles, vous utilisez une LEFT JOIN lorsqu'il y a une entité principale, toujours existante, qui peut être liée à une autre entité qui n'existe pas toujours.

Un cas d'utilisation simple serait dans une application e-commerce multi-vendeurs où, après qu'un utilisateur s'inscrit, il peut configurer une boutique et ajouter des produits à la boutique.

Un utilisateur, lors de son inscription, n'a pas automatiquement une boutique jusqu'à ce qu'il la crée. Donc, si vous essayez de voir tous les utilisateurs, avec les détails de leur boutique, vous utiliseriez une LEFT JOIN de la table `stores` sur la table `users`. Cela est dû au fait que chaque enregistrement dans la table `users` est important, boutique ou non.

Lorsque l'utilisateur a une boutique configurée, les détails de la boutique sont retournés, et si ce n'est pas le cas, NULL est retourné. Mais vous ne perdrez aucune donnée existante.

## **Comment utiliser une jointure droite (RIGHT JOIN) en SQL**

La RIGHT JOIN fonctionne comme l'inverse de la LEFT JOIN. Dans une RIGHT JOIN, chaque enregistrement de la table de droite, la table étant jointe, sera retourné. Ensuite, les valeurs de la table de gauche, la table de base, seront ajoutées là où elles existent.

La RIGHT JOIN est également connue sous le nom de RIGHT OUTER JOIN et vous pouvez les utiliser de manière interchangeable.

Un exemple serait de modifier la requête précédente pour utiliser une RIGHT JOIN au lieu d'une LEFT JOIN, comme ceci :

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
RIGHT JOIN departments d
ON (e.dept_id = d.id);
```

Maintenant, votre résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-16.02.08.png)
_Résultat de la RIGHT JOIN_

Maintenant, chaque département de la table `departments` a été retourné. Et les employés de ces départements ont également été retournés. Pour la dernière ligne, il n'y a pas d'employé avec `dept_id = 4`, c'est pourquoi la valeur NULL est retournée.

### Cas d'utilisation de la RIGHT JOIN

La RIGHT JOIN fonctionne exactement comme la LEFT JOIN dans les applications réelles. La différence entre elles vient du niveau d'importance des tables à joindre.

La LEFT JOIN est plus couramment utilisée car vous écriverez très probablement votre requête de gauche à droite, en listant les tables dans cet ordre d'importance également. Sinon, la RIGHT JOIN fonctionne exactement comme la LEFT JOIN.

### Comment combiner les JOINTURES en SQL

Jusqu'à présent, nous n'avons joint qu'une table à une autre. Mais vous pouvez en fait joindre autant de tables que vous le souhaitez en utilisant l'une ou l'autre de ces jointures ensemble comme vous le souhaitez.

Par exemple, disons que vous voulez récupérer les noms de tous les employés, avec les noms de leurs départements, les noms de leurs responsables et les noms de leurs projets. Vous devrez joindre la table `employees` à la table `departments`, la table `managers` et la table `projects`. Vous pouvez y parvenir en utilisant cette requête :

```sql
SELECT e.emp_name, d.dept_name, m.manager_name, p.project_name
FROM employees e
LEFT JOIN departments d
ON (e.dept_id = d.id)
LEFT JOIN managers m
ON (e.manager_id = m.id)
LEFT JOIN projects p
ON (e.id = p.emp_id);
```

Dans cette requête, commencez par la table `employees` comme table de base. Ensuite, vous effectuez une LEFT JOIN avec la table `departments`. Vous effectuez également une LEFT JOIN avec la table `managers`, et enfin, la table `projects`.

Le résultat de cette requête ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-19.30.29.png)
_Résultat de la requête JOIN générale_

La raison d'utiliser une LEFT JOIN ici est que vous devez récupérer TOUS les employés. Vous pourriez utiliser une INNER JOIN à la place de la LEFT JOIN dans la table `managers` car tous les employés ont un `manager_id` qui existe réellement dans la table `managers`. Mais pour être sûr, vous pouvez simplement utiliser la LEFT JOIN.

## **Comment utiliser une jointure croisée (CROSS JOIN) en SQL**

Cela est également connu sous le nom de CARTESIAN JOIN. Elle retourne chaque enregistrement des deux tables de manière multiplicative. Elle retourne toutes les combinaisons possibles de lignes des deux tables. Elle n'a pas besoin d'une condition de JOIN comme les autres JOINTURES.

Par exemple, si vous effectuez une CROSS JOIN entre les tables `employees` et `departments`, votre résultat ressemblera à ceci :

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
CROSS JOIN departments d;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-20.19.24.png)
_CROSS JOIN des tables `employees` et `departments`._

Ici, vous avez 24 lignes, ce qui est le produit du nombre de lignes dans la table `employees`, 6, et du nombre de lignes dans la table `departments`, 4. Les enregistrements ont été retournés de sorte que pour chaque enregistrement dans la table `employees`, il est mappé à un enregistrement dans la table `departments`.

### Cas d'utilisation de la CROSS JOIN

Un cas d'utilisation courant de la CROSS JOIN serait dans une application e-commerce où il est possible d'avoir des variations de taille ou de couleur pour tous les produits. Si vous devez jamais récupérer une liste de tous les produits dans différentes tailles, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-10-at-13.13.55.png)
_Résultat d'une CROSS JOIN basique_

Ce résultat a été obtenu en effectuant une CROSS JOIN d'une table `sizes` qui contient un `id` pour chaque taille, une chaîne `size` qui peut être soit 'Small', 'Medium', ou 'Large' et un autre champ appelé `ratio` pour affecter comment cette taille affecte le prix du produit. Ainsi, pour chaque produit, il est mappé à une taille, et le prix est calculé.

```sql
SELECT 
  p.product_name, 
  ROUND(p.price * s.ratio, 2) as price, 
  s.size 
FROM products p 
CROSS JOIN sizes s;
```

## **Comment utiliser une auto-jointure (SELF JOIN) en SQL**

Comme son nom l'indique, c'est lorsque vous essayez _de joindre une table à elle-même_. Il n'existe pas de mot-clé SELF JOIN.

Prenons cette nouvelle table `categories`, par exemple. Cette table contient à la fois des catégories principales et des sous-catégories. Si vous devez jamais récupérer les catégories et leurs sous-catégories, vous pouvez utiliser une SELF JOIN.

```sql
CREATE TABLE categories (
    id int,
    cat_name varchar(100),
    parent_category_id int DEFAULT NULL
);

INSERT INTO categories 
VALUES (1, 'Ladies', NULL), (2, 'Mens', NULL), (3, 'Lingeries', 1), (4, 'Shoes', 2);
```

```sql
SELECT cat.cat_name, parent_cat.cat_name AS parent 
FROM categories cat
JOIN categories parent_cat 
ON cat.parent_category_id = parent_cat.id;
```

Ici, voyez comment la table a été référencée deux fois. Soyez prudent avec l'alias car il est important pour différencier les deux instances. Le résultat de cette requête ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-21.40.25.png)
_Résultat d'une SELF JOIN simple sur la table `categories`_

### Cas d'utilisation de la SELF JOIN

Dans de nombreuses applications, vous trouvez des données hiérarchiques stockées dans une seule table. Comme la catégorie et la sous-catégorie comme montré dans l'exemple précédent. Ou comme dans le cas de l'employé et du responsable, car ils sont tous deux des employés de l'entreprise.

Dans le cas de ce dernier, la table aura des champs tels que `id`, `name`, `manager_id` (ceci est essentiellement l'`id` d'un autre employé). Supposons que vous souhaitiez écrire une requête où vous devez récupérer une liste de responsables et le nombre de leurs employés. Étant donné que ces responsables sont également des employés, vous n'avez qu'une seule table à partir de laquelle récupérer, la table `employees`. Pour effectuer cette récupération, faites une SELF JOIN de la table `employees` sur la table `employees` comme ceci :

```sql
SELECT e2.name AS supervisor, COUNT(e1.name) AS number_of_employees
FROM employee e1
JOIN employee e2
ON e1.manager_id = e2.id
GROUP BY e2.name;
```

Cela retournerait correctement les responsables et le nombre d'employés travaillant sous leurs ordres.

## **Résumé**

J'espère que vous comprenez maintenant les jointures SQL, les différents types et quand les utiliser afin d'écrire de meilleures requêtes.

Toutes les jointures ici fonctionnent avec MySQL. Il existe d'autres jointures comme FULL OUTER JOIN et NATURAL JOIN que nous n'avons pas discutées, mais vous pouvez les explorer par vous-même si vous le souhaitez.

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me retrouver sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), et [Github](https://github.com/Zubs). C'est rapide, c'est facile, et c'est gratuit !