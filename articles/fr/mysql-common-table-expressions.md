---
title: Comment utiliser les expressions de table commune MySQL – avec des exemples
  de requêtes
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-02-20T17:52:56.000Z'
originalURL: https://freecodecamp.org/news/mysql-common-table-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Common-dining-table-eettafel-Esstisch-04-1280x854.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
seo_title: Comment utiliser les expressions de table commune MySQL – avec des exemples
  de requêtes
seo_desc: "In your day to day job as a Software Engineer or Database Administrator,\
  \ you'll likely have to write long complex queries, often with some subqueries.\
  \ \nThese queries over time become less performant, difficult to read and understand,\
  \ and even more di..."
---

Dans votre travail quotidien en tant qu'ingénieur logiciel ou administrateur de base de données, vous devrez probablement écrire de longues requêtes complexes, souvent avec des sous-requêtes.

Ces requêtes deviennent avec le temps moins performantes, difficiles à lire et à comprendre, et encore plus difficiles à gérer. Et personne ne veut faire le travail difficile de les refactoriser, alors elles continuent simplement à vivre.

Ou vous avez probablement dû récupérer des données similaires basées sur un ensemble de données ou de paramètres. Pour y parvenir, vous écrivez de nombreuses sous-requêtes similaires, parfois exactement identiques, et vous les assemblez en utilisant le mot-clé UNION.

Eh bien, vous pouvez vous faciliter la vie et résoudre ces problèmes efficacement en utilisant une expression de table commune.

> Une expression de table commune (CTE) est un ensemble de résultats temporaire nommé qui existe dans le cadre d'une seule instruction et qui peut être référencé plus tard dans cette instruction, éventuellement plusieurs fois. – [MySQL.com](https://dev.mysql.com/doc/refman/8.0/en/with.html)

En utilisant une expression de table commune, vous pouvez écrire des requêtes plus lisibles et plus performantes très facilement. C'est en fait plus facile que d'écrire plusieurs sous-requêtes qui pourraient rendre vos requêtes illisibles et moins performantes.

Vous utiliserez principalement une expression de table commune pour deux raisons :

* Pour écrire des requêtes sans utiliser de sous-requêtes (ou en utilisant moins de sous-requêtes)
* Pour écrire des fonctions récursives

Dans ce tutoriel, je vais vous montrer comment écrire vos propres expressions de table commune.

## Comment créer une expression de table commune

Vous pouvez créer une expression de table commune (CTE) en utilisant le mot-clé `WITH`. Vous pouvez spécifier plusieurs expressions de table commune en même temps en séparant les requêtes constituant chaque expression de table commune par des virgules.

La forme générale d'une expression de table commune est la suivante :

```sql
WITH cte_name AS (query)

-- Multiple CTEs
WITH
    cte_name1 AS (
        -- Query here
    ),
    cte_name2 AS (
        -- Query here
    )
```

Le mot-clé `WITH` est suivi du nom de la CTE. Après le nom, vous introduisez la requête à exécuter dans la CTE en utilisant le mot-clé `AS`. Vous devez enfermer la requête dans des parenthèses. La CTE ne peut pas être suivie d'un point-virgule comme les autres requêtes SQL. Au lieu de cela, elle est suivie d'une autre requête qui l'utilise.

Après avoir créé une CTE, vous pouvez facilement utiliser le résultat des requêtes exécutées dans la CTE en référençant la CTE dans d'autres requêtes, d'autres CTE ou même en elle-même.

### Exemple de CTE

Si vous avez une table de joueurs de la coupe du monde, par exemple, vous pouvez créer une CTE comme ceci :

```sql
WITH
    barca_players AS (
        SELECT
            id,
            player_name,
            nationality,
            position,
            TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
        FROM
            wc_players
        WHERE
            club = 'Barcelona'
    )
SELECT
    *
FROM
    barca_players;
```

Ici, nous avons créé une CTE nommée `barca_players`. Cette CTE retournera le nom, la position, l'âge et la nationalité de chaque joueur de Barcelone qui était à la coupe du monde. Elle contient la sous-requête :

```sql
SELECT
    id,
    player_name,
    nationality,
    position,
    TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
FROM
    wc_players
WHERE
    club = 'Barcelona';
```

Cette sous-requête est ce qui produit le résultat de la CTE. Ensuite, elle est suivie d'une requête qui utilise ce résultat. Vous pouvez voir le résultat de la sélection de chaque enregistrement dans la CTE ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-17-at-22.59.25.png)

Vous pouvez également sélectionner uniquement des champs spécifiques de la CTE, par exemple :

```sql
WITH
    barca_players AS (
        SELECT
            id,
            player_name,
            nationality,
            position,
            TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
        FROM
            wc_players
        WHERE
            club = 'Barcelona'
    )
SELECT
    player_name,
    position
FROM
    barca_players;
```

Cette requête est presque la même que la première, sauf qu'elle sélectionne uniquement les noms et les positions des joueurs dans la liste.

## Comment utiliser les expressions de table commune avec des paramètres

Vous pouvez également passer des arguments à la CTE. Ce sont des alias que vous pouvez utiliser pour référencer les colonnes des résultats de la requête. Le nombre de paramètres passés dans la CTE doit être le même que le nombre de colonnes sélectionnées dans sa sous-requête. Cela est dû au fait que les colonnes sont appariées aux alias une par une, les unes après les autres.

Par exemple, dans la CTE `barca_players` créée ci-dessus, vous pouvez décider de référencer la colonne `nationality` comme `country`, et `position` comme `role` :

```sql
WITH
    barca_players (id, player_name, country, role, age) AS (
        SELECT
            id,
            player_name,
            nationality,
            position,
            TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
        FROM
            wc_players
        WHERE
            club = 'Barcelona'
    )
SELECT
    player_name,
    role
FROM
    barca_players;
```

Remarquez que dans la sous-requête de la CTE, vous utilisez toujours les noms de colonnes corrects. Mais dans la requête `SELECT` externe, vous utilisez les nouveaux alias spécifiés comme paramètres de la CTE.

## Expressions de table commune récursives

Lorsque vous référencez une expression de table commune dans elle-même, elle devient une expression de table commune récursive.

Une expression de table commune récursive, comme son nom l'indique, est une expression de table commune qui peut exécuter une sous-requête plusieurs fois, tant qu'une condition est remplie. Elle itère continuellement jusqu'à ce qu'elle atteigne un point d'arrêt, lorsque la condition cesse d'être vraie.

Pour définir une CTE récursive, le mot-clé `RECURSIVE` doit être dans son nom. Sans ce mot-clé, MySQL génère une erreur.

Par exemple, vous pouvez écrire une expression de table commune qui imprime les nombres de 1 à 10 et leurs carrés comme ceci :

```sql
WITH RECURSIVE
    numbers_list (n, square) AS (
        SELECT
            1,
            1
        UNION ALL
        SELECT
            n + 1,
            (n + 1) * (n + 1)
        FROM
            numbers_list
        WHERE
            n < 10
    )
SELECT
    *
FROM
    numbers_list;
```

Examinons ce qui se passe ici :

Dans les deux premières lignes, l'expression de table commune récursive est définie avec deux paramètres, l'un représentant la colonne pour le nombre, et l'autre représentant la colonne pour le carré :

```sql
WITH RECURSIVE
    numbers_list (n, square) AS (
```

Ensuite, la sous-requête. La sous-requête est en deux parties, jointes par le mot-clé `UNION ALL` pour n'en former qu'une. Vous pouvez également joindre ces sous-requêtes par le mot-clé `UNION` si vous n'avez pas besoin de enregistrements en double.

La première partie de la sous-requête est une partie clé des expressions de table commune récursives. C'est la requête de base, le premier ensemble de résultats, l'itération initiale. Cette requête est le point de départ de toutes les itérations.

Dans cet exemple, elle est statique, car aucun enregistrement n'est récupéré.

```sql
SELECT
    1,
    1
```

Après cette première requête, la table de résultats a une ligne et ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-17-at-23.55.27.png)

La deuxième partie de la sous-requête est l'endroit où l'itération se produit vraiment.

Dans cette requête, la CTE est référencée dans elle-même, et ses colonnes peuvent être utilisées. Lorsqu'un nom de colonne est mentionné, la valeur la plus récente de cette colonne est prise.

Ainsi, au début de l'itération, `n` est 1 et `square` est également 1. Cela signifie que `n + 1` est 2, et `(n + 1) * (n + 1)` est 2 * 2, ce qui est 4. 2 et 4 sont ajoutés à la table de résultats et deviennent ensuite les valeurs les plus récentes dans la table. `n` devient 2, et `square` devient `4`.

Cela continue jusqu'à ce que la condition dans le mot-clé `WHERE` cesse d'être vraie.

Le mot-clé `WHERE` dans la requête spécifie le point d'arrêt de la CTE. Jusqu'à ce que la condition spécifiée soit remplie, la requête continue à être exécutée. Dans ce cas, après chaque itération, la requête vérifie si `n` est inférieur à 10.

Si une condition qui sera toujours évaluée à vrai est définie, cela crée une boucle sans fin et vous obtenez une erreur comme `Recursive query aborted after 1001 iterations. Try increasing @@cte_max_recursion_depth to a larger value.`

```sql
SELECT
    n + 1,
    (n + 1) * (n + 1)
FROM
    numbers_list
WHERE
    n < 10
```

Maintenant, vous pourriez penser, "Si la condition vérifie `n < 10`, comment se fait-il que 10 soit toujours dans la table finale ?".

Eh bien, la raison est que dans SQL, la partie `WHERE` d'une requête est évaluée en premier avant les autres parties. Donc, lorsque `n = 9` est la dernière ligne, la requête s'exécute une fois de plus, et avant l'insertion ou autre chose, elle vérifie si 9 est inférieur à 10. Comme 9 est inférieur à 10, elle ajoute `n + 1` qui est 10 à la liste. Ensuite, lors de l'itération suivante, 10 est l'enregistrement le plus récent et il n'est pas inférieur à lui-même, donc la boucle se termine.

Gardez à l'esprit qu'une expression de table commune récursive se compose d'une requête `SELECT` récursive et d'une requête `SELECT` non récursive.

### Règles simples des expressions de table commune récursives

* Vous ne pouvez pas utiliser le mot-clé `GROUP BY`. Cela est dû au fait que vous ne pouvez regrouper qu'une collection, mais dans une expression de table commune récursive, les enregistrements sont traités et évalués individuellement. D'autres mots-clés comme `ORDER BY`, `DISTINCT`, et les fonctions d'agrégation comme `SUM` ne peuvent pas être utilisés non plus.
* Vous ne pouvez pas utiliser de fonctions de fenêtrage.

Ces règles s'appliquent à la partie récursive d'une expression de table commune récursive.

### Cas d'utilisation des CTE récursives

#### Suite de Fibonacci

> La suite de Fibonacci est une suite dans laquelle chaque nombre est la somme des deux précédents. La suite commence généralement par 0 et 1, bien que certains auteurs commencent la suite par 1 et 1 ou parfois par 1 et 2. ([source](https://en.wikipedia.org/wiki/Fibonacci_number))

Vous pouvez facilement générer une suite de Fibonacci de n'importe quelle longueur en utilisant une expression de table commune récursive. Par exemple, voici une requête qui obtiendra les 20 premiers nombres d'une suite de Fibonacci commençant par 0 et 1.

```sql
WITH RECURSIVE
    fibonacci (n, fib_n, next_fib_n) AS (
        /*
        * n - Nombre d'itérations
        * fib_n - Nombre de Fibonacci actuel. Commence à 0
        * next_fib_n - Nombre de Fibonacci suivant. Commence à 1
        */
        SELECT
            1,
            0,
            1
        UNION ALL
        SELECT
            n + 1,
            next_fib_n,
            fib_n + next_fib_n
        FROM
            fibonacci
        WHERE
            n < 20
    )
SELECT
    *
FROM
    fibonacci;
```

#### Parcours de données hiérarchiques

Dans de nombreuses bases de données d'applications, vous constaterez que les données hiérarchiques sont stockées dans la même table.

Par exemple, une table `categories` contiendra généralement des catégories principales et des sous-catégories référençant leur catégorie parente. Une table `employees` contiendra des employés réguliers avec leur `manager_id`, ainsi que leurs managers ou superviseurs, car ils sont également des employés.

Si vous aviez une table `categories` comme ceci, avec 4 enregistrements, 1 catégorie principale, et une chaîne de sous-catégories :

```sql
CREATE TABLE
    categories (
        id int,
        cat_name varchar(100),
        parent_category_id int DEFAULT NULL
    );

INSERT INTO
    categories
VALUES
    (1, 'Mens', NULL),
    (2, 'Tops', 1),
    (3, 'Jerseys', 2),
    (4, 'England', 3);
```

Vous pouvez récupérer chaque catégorie, avec sa catégorie parente attachée facilement comme ceci :

```sql
WITH RECURSIVE
    category_tree AS (
        SELECT
            id,
            cat_name,
            parent_category_id,
            cat_name AS full_name
        FROM
            categories
        WHERE
            parent_category_id IS NULL
        UNION ALL
        SELECT
            c.id,
            c.cat_name,
            c.parent_category_id,
            CONCAT (ct.full_name, ' > ', c.cat_name)
        FROM
            categories c
            JOIN category_tree ct ON c.parent_category_id = ct.id
    )
SELECT
    full_name
FROM
    category_tree;
```

Dans cet exemple, la requête de base sélectionne la catégorie racine, où `parent_category_id IS NULL`. Ensuite, elle cherche une catégorie où le `parent_category_id` est l'`id` de la catégorie actuelle en utilisant un `JOIN`. Elle répète cela jusqu'à ce qu'elle atteigne la catégorie finale. Le résultat de cette requête est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-18-at-01.19.10.png)

## **Résumé**

J'espère que vous comprenez maintenant comment utiliser les expressions de table commune MySQL, leurs variations (régulières et récursives), et quand les utiliser afin que vous puissiez écrire de meilleures requêtes. Vous pouvez trouver plus d'informations sur les expressions de table commune dans la documentation [ici](https://dev.mysql.com/doc/refman/8.0/en/with.html).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me connecter sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), et [Github](https://github.com/Zubs). C'est rapide, c'est facile, et c'est gratuit !