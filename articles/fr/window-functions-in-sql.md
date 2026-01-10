---
title: Comment utiliser les fonctions de fenêtre en SQL – avec des exemples de requêtes
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2023-02-09T21:47:41.000Z'
originalURL: https://freecodecamp.org/news/window-functions-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/windows-image.jpeg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Comment utiliser les fonctions de fenêtre en SQL – avec des exemples de
  requêtes
seo_desc: 'Window functions are an advanced type of function in SQL. They let you
  work with observations more easily.

  Window functions give you access to features like advanced analytics and data manipulation
  without the need to write complex queries.

  In this l...'
---

Les fonctions de fenêtre sont un type avancé de fonction en SQL. Elles vous permettent de travailler plus facilement avec des observations.

Les fonctions de fenêtre vous donnent accès à des fonctionnalités comme l'analyse avancée et la manipulation de données sans avoir besoin d'écrire des requêtes complexes.

Dans cette leçon, vous apprendrez ce que sont les fonctions de fenêtre et comment elles fonctionnent. Sans plus attendre, commençons.

## Qu'est-ce qu'une fonction de fenêtre ?

Avant d'apprendre exactement ce qu'est une fonction de fenêtre, définissons le sens d'un terme qui apparaîtra fréquemment dans cet article : jeu de résultats.

En SQL, un jeu de résultats est la donnée ou le résultat qui est retourné par une requête. C'est-à-dire, c'est le résultat (table) de l'exécution du code d'une instruction select.

Pour que vous compreniez ce qu'est une fonction de fenêtre, décomposons les mots en morceaux.

### Qu'est-ce qu'une fenêtre en SQL ?

Une fenêtre est essentiellement un ensemble de lignes ou d'observations dans une table ou un jeu de résultats. Dans une table, vous pouvez avoir plus d'une fenêtre selon la manière dont vous spécifiez la requête – vous apprendrez cela sous peu. Une fenêtre est définie en utilisant la clause `OVER()` en SQL.

Vous apprendrez comment déterminer le nombre de fenêtres dans un jeu de résultats plus tard dans cet article.

### Qu'est-ce qu'une fonction ?

Les fonctions sont prédéfinies en SQL et vous les utilisez pour effectuer des opérations sur des données. Elles vous permettent de faire des choses comme agréger des données, formater des chaînes, extraire des dates, et ainsi de suite.

Ainsi, les fonctions de fenêtre sont des fonctions SQL qui nous permettent d'effectuer des opérations sur une fenêtre – c'est-à-dire, un ensemble d'enregistrements.

L'intérêt des fonctions de fenêtre est que vous pouvez spécifier les fenêtres sur lesquelles vous souhaitez appliquer la fonction. Par exemple, nous pouvons partitionner le jeu de résultats complet en divers groupes/fenêtres.

Avant d'aborder la syntaxe des fonctions de fenêtre, examinons les catégories de fonctions de fenêtre.

## Différents types de fonctions de fenêtre

Il existe de nombreuses fonctions de fenêtre en SQL, mais elles sont principalement catégorisées en 3 types différents :

* Fonctions de fenêtre d'agrégation
  
* Fonctions de fenêtre de valeur
  
* Fonctions de fenêtre de classement
  

Les fonctions de fenêtre d'agrégation sont utilisées pour effectuer des opérations sur des ensembles de lignes dans une ou plusieurs fenêtres. Elles incluent `SUM()`, `MAX()`, `COUNT()`, et d'autres.

Les fonctions de fenêtre de classement sont utilisées pour classer les lignes dans une ou plusieurs fenêtres. Elles incluent `RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`, et d'autres.

Les fonctions de fenêtre de valeur sont similaires aux fonctions de fenêtre d'agrégation qui effectuent plusieurs opérations dans une fenêtre, mais elles sont différentes des fonctions d'agrégation. Elles incluent des choses comme `LAG()`, `LEAD()`, `FIRST_VALUE()`, et d'autres. Nous verrons leur utilité plus tard dans la section.

## Tableau d'exemple

Dans ce tutoriel, vous travaillerez avec une table appelée `student_score` qui contient des données telles que `student_id`, `student_name`, `dep_name` et `score`.

Vous pouvez créer la table en utilisant le code suivant :

```sql
DROP TABLE IF EXISTS student_score;

CREATE TABLE student_score (
  student_id SERIAL PRIMARY KEY,
  student_name VARCHAR(30),
  dep_name VARCHAR(40),
  score INT
);

INSERT INTO student_score VALUES (11, 'Ibrahim', 'Computer Science', 80);
INSERT INTO student_score VALUES (7, 'Taiwo', 'Microbiology', 76);
INSERT INTO student_score VALUES (9, 'Nurain', 'Biochemistry', 80);
INSERT INTO student_score VALUES (8, 'Joel', 'Computer Science', 90);
INSERT INTO student_score VALUES (10, 'Mustapha', 'Industrial Chemistry', 78);
INSERT INTO student_score VALUES (5, 'Muritadoh', 'Biochemistry', 85);
INSERT INTO student_score VALUES (2, 'Yusuf', 'Biochemistry', 70);
INSERT INTO student_score VALUES (3, 'Habeebah', 'Microbiology', 80);
INSERT INTO student_score VALUES (1, 'Tomiwa', 'Microbiology', 65);
INSERT INTO student_score VALUES (4, 'Gbadebo', 'Computer Science', 80);
INSERT INTO student_score VALUES (12, 'Tolu', 'Computer Science', 67);
```

### Syntaxe des fonctions de fenêtre

Dans une expression simple, une fonction de fenêtre ressemble à ceci :

```sql
function(expression|column) OVER(
	[ PARTITION BY expr_list optional]
    [ ORDER BY order_list optional]
)
```

Passons en revue la syntaxe pièce par pièce :

`function(expression|column)` est la fonction de fenêtre telle que `SUM()` ou `RANK()`.

`OVER()` spécifie que la fonction avant elle est une fonction de fenêtre et non une fonction ordinaire. Ainsi, lorsque le moteur SQL voit la clause over, il saura que la fonction avant la clause over est une fonction de fenêtre.

La clause `OVER()` a certains paramètres qui sont optionnels selon ce que vous souhaitez réaliser. Le premier étant `PARTITION BY`.

La clause `PARTITION BY` divise le jeu de résultats en différentes partitions/fenêtres. Par exemple, si vous spécifiez la clause `PARTITION BY` par une ou plusieurs colonnes, alors le jeu de résultats sera divisé en différentes fenêtres de la valeur de cette ou ces colonnes.

La `expr_list` dans la clause `PARTITION BY` est :

```javascript
expression | column_name [, expr_list ]
```

Ce qui signifie que la clause `PARTITION BY` peut avoir une expression, une colonne, ou plus d'une occurrence ou une expression ou colonne qui doit être séparée par une virgule. Par exemple `PARTITION BY column1, column2`.

Le paramètre suivant `ORDER BY` est utilisé pour trier les observations dans une fenêtre. La clause `ORDER BY` prend `order_list` qui est :

```sql
expression | column_name [ ASC | DESC ]
[ NULLS FIRST | NULLS LAST ][, order_list ]
```

où `order_list` peut être une expression ou un nom de colonne et vous pouvez également spécifier l'ordre de tri (soit ascendant ou descendant), ou vous pouvez trier les valeurs nulles en premier ou en dernier. De plus, le order by peut prendre de nombreuses expressions ou noms de colonnes.

Comme mentionné précédemment, la clause `OVER()` est utilisée pour spécifier la fenêtre dans un jeu de résultats. Maintenant, une chose à noter est que si un paramètre n'est pas spécifié dans la clause `OVER()`, le nombre par défaut de fenêtres dans le jeu de résultats sera un.

Vous utilisez les paramètres `PARTITION BY` et `ORDER BY` pour déterminer ou spécifier le nombre de fenêtres. Passons à un exemple.

## Comment utiliser une fonction de fenêtre – Exemple

Passons à un exemple de la façon d'utiliser une fonction de fenêtre. Supposons, par exemple, que vous souhaitez comparer le score minimum et le score maximum de tous les enregistrements dans la table que nous avons créée précédemment. Vous pouvez faire cela en utilisant une fonction de fenêtre comme montré ci-dessous.

Rappelez-vous que ne pas spécifier une clause de partition dans la clause `OVER` fera en sorte que toutes les fenêtres s'étendent à travers l'ensemble du jeu de données.

```sql
SELECT 
	*,
	MAX(score) OVER() AS maximum_score,
	MIN(score) OVER() AS minimum_score
	
FROM student_score;
```

Comme vous pouvez le voir, nous avons le score minimum et maximum à travers l'ensemble du jeu de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-43.png align="left")

*Tableau montrant le résultat de la fonction de fenêtre*

De plus, notez que la requête ci-dessus peut également être réalisée en utilisant des sous-requêtes comme ceci :

```sql
SELECT *,
	(SELECT MAX(score) FROM student_score) AS maximum_score,
	(SELECT MIN(score) FROM student_score) AS minimum_score
FROM student_score;
```

Comme vous pouvez le voir, la fonction de fenêtre est plus facile à comprendre par rapport à la méthode de sous-requête qui semble un peu plus avancée.

## Comment utiliser une fonction de fenêtre avec `PARTITION BY`

Supposons, par exemple, que vous souhaitez diviser le jeu de données en différentes partitions. Ensuite, vous souhaitez comparer chaque enregistrement dans chaque partition avec une valeur d'agrégation ou une valeur calculée de chaque partition. Vous pouvez spécifier la clause `PARTITION BY` dans la fonction `OVER`.

Par exemple, supposons que vous souhaitez comparer le score maximum et le score moyen dans chaque département avec le score individuel. Vous pouvez faire cela en spécifiant la clause `PARTITION BY` dans l'instruction `OVER` et également l'utiliser avec la fonction d'agrégation que vous souhaitez utiliser pour obtenir votre résultat souhaité.

```sql
SELECT 
	*,
	MAX(score)OVER(PARTITION BY dep_name) AS dep_maximum_score,
	ROUND(AVG(score)OVER(PARTITION BY dep_name), 2) AS dep_average_score
FROM student_score;
```

Vous pouvez voir que la clause `PARTITION BY` spécifiée dans la clause `OVER()` divise le jeu de résultats en 4 partitions différentes. Cela est dû au fait qu'il y a 4 départements différents dans la colonne `dep_name` (qui sont `Biochemistry, Computer Science, Industrial Chemistry, and Microbiology`).

Maintenant, après la clause `PARTITION BY`, vous pouvez ensuite calculer la fonction d'agrégation pour chaque enregistrement dans les différents départements.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-26.png align="left")

Vous pouvez voir à partir de l'image ci-dessus que la fonction d'agrégation `MAX()` et `AVG()` est calculée pour chaque partition.

## Autres exemples de fonctions de fenêtre

Passons en revue certaines des fonctions de fenêtre courantes avec lesquelles vous travaillerez en SQL.

### Comment utiliser la fonction `ROW_NUMBER`

Vous utilisez `ROW_NUMBER()` pour attribuer des numéros de série aux enregistrements dans une fenêtre. Supposons que nous voulons attribuer des numéros de série aux enregistrements dans une partition. Par exemple, nous voulons ajouter des numéros de ligne au jeu de données en fonction de leurs noms dans l'ordre alphabétique. Vous pouvez faire cela en utilisant le code suivant :

```sql
SELECT
	*,
	ROW_NUMBER() OVER(ORDER BY student_name) AS name_serial_number
FROM student_score;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-29.png align="left")

Comme vous pouvez le voir à partir de l'image ci-dessus, le `student_name` avec la plus petite valeur (c'est-à-dire, celui qui arrive le plus tôt dans l'alphabet) est `Gbadebo` puisque cela commence par `G`. Ensuite, 1 est ajouté comme son numéro de ligne qui est suivi par le nom qui commence par `H`, et ainsi de suite.

### Comment utiliser la fonction `RANK`

`RANK()`, comme son nom l'indique, vous permet de classer les observations dans une fenêtre mais avec des écarts. Voyons ce que cela signifie :

```sql
SELECT
	*,
	RANK()OVER(PARTITION BY dep_name ORDER BY score DESC)	
FROM student_score;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--11-.png align="left")

Comme vous pouvez le voir dans le code ci-dessus, le jeu de résultats a été partitionné en différentes fenêtres en fonction de la colonne de département. Ensuite, nous avons utilisé la clause `ORDER BY` pour trier les enregistrements des étudiants en fonction de leur score dans l'ordre décroissant dans chaque partition. Après cela, nous avons appliqué la fonction `RANK`.

Maintenant, concernant les écarts, comme vous pouvez le voir dans la partie surlignée dans l'image ci-dessus, deux enregistrements dans le département de Computer Science ont le même score (`80`). Cela a fait en sorte que les deux soient classés avec la valeur `2` (au lieu que l'un soit classé 2 et l'autre 3). Donc, elle ne sait pas comment gérer une égalité, en gros.

Vous pouvez éviter ce scénario en utilisant une autre fonction de fenêtre appelée `DENSE_RANK` qui classe les observations dans une fenêtre sans ces écarts.

### Comment utiliser la fonction `DENSE_RANK`

`DENSE_RANK` est similaire à `RANK` sauf qu'elle classe les observations dans une fenêtre sans écarts.

```sql
SELECT
	*,
	DENSE_RANK()OVER(PARTITION BY dep_name ORDER BY score DESC)	
FROM student_score;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--10-.png align="left")

Comme vous pouvez le voir dans la sortie ci-dessus, lorsque vous utilisez `DENSE_RANK`, le numéro de rang suivant (qui est `3`) a été attribué à `Tolu` (contrairement à l'utilisation de `RANK` qui a attribué à Tolu un rang de `4`, en sautant 3 à cause de l'égalité).

### Comment utiliser la fonction `LAG`

`LAG` est utilisé pour retourner la ligne de décalage avant la ligne actuelle dans une fenêtre. Par défaut, il retourne la ligne précédente avant la ligne actuelle.

Vous utilisez généralement `LAG` lorsque vous souhaitez comparer la valeur d'une ligne précédente avec la ligne actuelle. Il est couramment appliqué dans l'[analyse de séries temporelles](https://www.tableau.com/learn/articles/time-series-analysis#:~:text=Time%20series%20analysis%20is%20a,data%20points%20intermittently%20or%20randomly.). Par exemple :

```sql
SELECT
	*,
	LAG(score) OVER(PARTITION BY dep_name ORDER BY score)	
FROM student_score;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-32.png align="left")

Comme montré dans la première partition, le premier enregistrement dans la partition de biochimie (celui de Yusuf) n'a pas de valeur précédente (c'est-à-dire qu'aucun enregistrement ne vient avant lui), c'est pourquoi null a été retourné. Ensuite, en passant à l'enregistrement suivant – celui de Muritadoh – il a un enregistrement précédent, donc il retourne la valeur précédente qui est `70`.

## Comment utiliser la clause Frame dans `ORDER BY`

Maintenant que vous avez appris certaines fonctions de fenêtre courantes avec lesquelles vous pourriez travailler au quotidien, passons à l'apprentissage d'un autre concept clé lié à la clause `ORDER BY` appelé la clause frame.

Une clause frame, comme son nom l'indique, fournit le cadre (c'est-à-dire, l'ensemble des lignes dans une fenêtre) sur lequel la fonction doit être appliquée. Vous l'utilisez pour fournir le décalage des lignes à inclure ou à calculer avec la ligne actuelle (c'est-à-dire, les lignes avant ou après la ligne actuelle – le moteur SQL traite les lignes une après l'autre).

Maintenant, avant de voir comment spécifier une clause frame, examinons certaines des hypothèses de la clause frame :

1. Premièrement, une clause frame ne s'applique pas aux fonctions de classement. La fonction de classement ne classe que l'observation dans la fenêtre en fonction de la clause `ORDER BY`.
   
2. Lorsque vous utilisez une fonction de fenêtre d'agrégation, vous ne pouvez pas inclure la clause `ORDER BY`. Mais lorsque vous utilisez la clause `ORDER BY`, il est bon de spécifier la clause frame pour des résultats précis. Ce que cela signifie, c'est que si vous souhaitez utiliser une fonction de fenêtre d'agrégation et que vous souhaitez également ordonner les observations dans cette fenêtre par une colonne, il est bon de spécifier une clause frame pour obtenir un résultat précis. Mais si vous ne triez pas les observations dans la fenêtre lorsque vous utilisez une fonction d'agrégation, vous n'avez pas besoin de spécifier une clause frame.
   

Vous pouvez spécifier une clause frame en utilisant deux choses – `ROWS` et `RANGE`. Mais dans cette partie, vous apprendrez à utiliser le mot-clé `ROWS` puisque c'est celui qui est couramment utilisé pour spécifier une clause frame. Le mot-clé `RANGE` dépasse le cadre de cet article.

La clause `ROWS` définit le cadre en termes de décalage physique des lignes par rapport aux lignes actuelles. C'est-à-dire, elle est utilisée pour spécifier les lignes qui seront utilisées en conjonction avec la ligne actuelle pour le calcul.

Par exemple, la clause frame suivante `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` définit un cadre qui inclut la ligne actuelle, 1 ligne la précédant et 1 ligne la suivant.

Examinons les mots-clés que vous pouvez utiliser en conjonction avec la clause `ROWS` :

1. `N PRECEDING` est un mot-clé que vous utilisez pour spécifier les N lignes qui seront incluses dans le calcul avec la ligne actuelle. Par exemple, `3 PRECEDING` signifie 3 lignes précédant la ligne actuelle.
   
2. `N FOLLOWING` fonctionne comme `N PRECEDING` sauf qu'il fonctionne de manière opposée. `N FOLLOWING` spécifie le nombre de lignes après la ligne actuelle.
   
3. `UNBOUNDED PRECEDING` signifie toutes les lignes avant la ligne actuelle.
   
4. `UNBOUNDED FOLLOWING` signifie toutes les lignes après la ligne actuelle.
   
5. `CURRENT ROW` est utilisé pour spécifier la ligne actuelle.
   

Par exemple, examinons la clause frame suivante :

`ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` utilisera moins ou égal à 2 lignes avant la ligne actuelle, ainsi que la ligne actuelle pour le calcul.

### Exemple de clause frame

Examinons un exemple. Supposons, par exemple, que vous souhaitez obtenir la somme cumulative de tous les scores des étudiants. Vous pouvez faire cela en utilisant une clause frame.

Donc, tout d'abord, pour pouvoir faire cela, vous devez d'abord connaître les types de mots-clés que vous spécifierez dans la clause frame.

Puisque vous souhaitez additionner toutes les lignes avant la ligne actuelle et la ligne actuelle elle-même, vous pouvez utiliser le mot-clé `UNBOUNDED PRECEDING`. Rappelez-vous que cela obtient toutes les lignes avant la ligne actuelle et utilise également la ligne actuelle elle-même.

Le code pour réaliser cette tâche est montré ci-dessous :

```sql
SELECT
	*,
	SUM(score)OVER(ORDER BY student_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cummulative_sum
FROM student_score
```

Décomposons le code de la fonction de fenêtre :

```sql
SUM(score)OVER(ORDER BY student_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cummulative_sum
```

Tout d'abord, dans la clause `OVER()`, nous trions toute la fenêtre – qui est l'ensemble du jeu de données – en utilisant l'identifiant de l'étudiant.

Ensuite, nous spécifions la clause frame qui est `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. Cela signifie que toutes les lignes avant la ligne actuelle et la ligne actuelle seront utilisées pour le calcul.

Le résultat est montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-6.png align="left")

La première ligne du jeu de données n'a aucune ligne avant elle. Mais puisque nous spécifions également le mot-clé `CURRENT ROW` comme dernier cadre, le moteur SQL trouve sa somme qui est égale à `65`.

Ensuite, en passant à la deuxième ligne. Elle a 1 ligne avant elle. Donc le moteur SQL additionne le score de la première ligne `65` avec la ligne actuelle qui est `70`. C'est pourquoi le résultat est `135`... et ainsi de suite dans le tableau.

### Quand utiliser une fonction de fenêtre

Vous avez appris ce que sont les fonctions de fenêtre dans ce tutoriel. Voici quelques cas pratiques où vous pouvez les utiliser :

1. Lorsque vous souhaitez comparer une valeur d'agrégation dans une fenêtre avec des enregistrements individuels dans cette fenêtre.
   
2. Lorsque vous souhaitez faire des choses comme le classement, le percentile, la somme cumulative ou le total courant, la moyenne mobile, et ainsi de suite.
   
## Conclusion

Dans ce tutoriel, vous avez appris ce que sont les fonctions de fenêtre, et vous avez également examiné certaines des clauses que vous pouvez ajouter dans les fonctions de fenêtre. Un exemple est la clause PARTITION BY, qui divise le jeu de résultats en partitions ou fenêtres séparées.

Vous avez également appris comment utiliser la clause ORDER BY pour ordonner les observations dans une fenêtre et vous avez vu divers exemples courants de fonctions de fenêtre.

Enfin, vous avez appris une autre clause avancée que vous pouvez utiliser avec les fonctions de fenêtre, la clause frame, qui vous permet d'accéder à plus de fonctionnalités d'une fenêtre.

Merci d'avoir lu jusqu'à la fin. Vous pouvez utiliser le tutoriel listé ci-dessous pour en apprendre davantage sur les fonctions de fenêtre SQL.

%[https://www.postgresql.org/docs/current/functions-window.html]