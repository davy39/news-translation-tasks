---
title: Fonctions de date MySQL – Expliquées avec des exemples de requêtes
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-01-25T17:15:13.000Z'
originalURL: https://freecodecamp.org/news/mysql-date-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/image-162-1.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Fonctions de date MySQL – Expliquées avec des exemples de requêtes
seo_desc: 'SQL is a programming language we use to interact with relational databases.
  SQL databases contain tables, which contain rows of data. These tables can contain
  a wide range of data types.

  In this article, you''ll learn how MySQL functions help make dat...'
---

SQL est un langage de programmation que nous utilisons pour interagir avec les bases de données relationnelles. Les bases de données SQL contiennent des tables, qui contiennent des lignes de données. Ces tables peuvent contenir une large gamme de types de données.

Dans cet article, vous apprendrez comment les fonctions MySQL facilitent grandement la gestion des dates. 

Ces fonctions aident à effectuer diverses tâches. Certaines effectuent des tâches simples comme ajouter des jours à des dates, trouver combien de jours séparent deux dates, ou même des tâches plus compliquées comme déterminer à quel point une date est avancée dans une année en nombre de jours.

Avant de continuer, gardez à l'esprit que cet article a été écrit le `2023-01-24`. Ainsi, vos résultats en exécutant les requêtes ici pourraient être légèrement différents en fonction de quand vous le lisez.

## Comment utiliser la fonction `CURRENT_DATE` en SQL

Cette fonction retourne la date d'aujourd'hui au format '**AAAA-MM-JJ**'. C'est l'une des fonctions MySQL les plus simples à utiliser. Elle ne prend aucun argument.

```sql
SELECT CURRENT_DATE;
-- Retourne 2023-01-24
```

Cette fonction a des fonctions synonymes qui fonctionnent exactement de la même manière : `CUR_DATE` et `CURRENT_DATE()` retourneront le même résultat que `CURRENT_DATE`.

## Comment utiliser la fonction `ADDDATE` en SQL

Cette fonction effectue des additions ou des soustractions sur des valeurs de date. Elle prend un intervalle qui peut être en jours, mois ou même années. Cet intervalle peut être positif ou négatif. La fonction suit ce format :

```sql
ADDDATE(date/expr, INTERVAL expr unit);
```

Ici, `date/expr` fait référence à la valeur de date de base à laquelle ajouter ou soustraire. Et `INTERVAL` est un mot-clé constant qui doit précéder `expr`, utilisé pour définir la valeur de l'incrément en nombres. Enfin, vous avez l'unité, qui peut être `day` (jour), `week` (semaine), `month` (mois), `quarter` (trimestre) ou même `year` (année). L'unité peut également être une valeur plus petite comme `second` (seconde) ou même `microsecond` (microseconde). Consultez la [documentation MySQL](https://dev.mysql.com/doc/refman/8.0/en/expressions.html#temporal-intervals) pour plus de valeurs possibles.

Cette fonction fonctionne exactement de la même manière que `DATE_ADD` et vous pouvez les utiliser indifféremment.

En utilisant ADDDATE, vous pouvez trouver la date dans 45 jours à partir d'aujourd'hui comme ceci :

```sql
SELECT ADDDATE(CURRENT_DATE, INTERVAL 45 DAY);
-- Retourne 2023-03-10
```

Pour obtenir la date d'il y a 7 mois et 3 semaines, utilisez ADDDATE comme ceci :

```sql
SELECT ADDDATE(
	ADDDATE(CURRENT_DATE, INTERVAL -7 MONTH), 
	INTERVAL -3 WEEK
);
-- Retourne 2022-06-03
```

Ici, nous avons appelé la fonction ADDDATE deux fois. D'abord, pour obtenir la date d'il y a 7 mois. Ensuite, nous l'avons appelée à nouveau pour obtenir la date d'il y a 3 semaines avant cette période.

Un cas d'utilisation courant de ADDDATE dans les applications réelles est d'obtenir des valeurs de données à utiliser dans une clause WHERE comme une plage. 

Par exemple, si vous aviez une table `employees` avec un champ `hiredate` qui stocke leur date d'embauche. Pour voir tous les employés qui ont commencé au cours de l'année passée (où `hiredate` > la date d'il y a un an), utilisez ADDDATE comme ceci :

```sql
SELECT * 
FROM employees 
WHERE hiredate > ADDDATE(CURRENT_DATE, INTERVAL -1 YEAR);
```

Un autre cas courant serait lorsque vous devez filtrer par une plage de temps. Dans une table `songs` avec un champ `released`, pour récupérer toutes les chansons sorties au cours des trois dernières semaines sauf celles sorties cette semaine, utilisez ADDDATE comme ceci :

```sql
SELECT * 
FROM songs 
WHERE released 
BETWEEN ADDDATE(CURRENT_DATE, INTERVAL -3 WEEK) 
AND ADDDATE(CURRENT_DATE, INTERVAL -1 WEEK);
```

## Comment utiliser la fonction `DATEDIFF` en SQL

Cette fonction retourne le nombre de jours entre deux dates. Elle prend les deux dates à soustraire. Utilisons `DATEDIFF` pour trouver le nombre de jours entre aujourd'hui et `2023-03-10`.

```sql
SELECT DATEDIFF('2023-03-10', CURRENT_DATE);
-- Retourne 45
```

En réarrangeant les dates et en appelant à nouveau la fonction, le résultat change :

```sql
SELECT DATEDIFF(CURRENT_DATE, '2023-03-10');
-- Retourne -45
```

Vous pouvez utiliser cette fonction avec la fonction `ABS` pour obtenir la valeur absolue et éviter les problèmes avec le signe ou la valeur négative.

```sql
SELECT ABS(DATEDIFF(CURRENT_DATE, '2023-03-10'));
-- Retourne 45
```

Cela est très utile lorsque vous devez retourner des données en fonction du temps. Par exemple, dans de nombreux blogs, vous voyez une partie qui dit quelque chose comme 'Publié il y a 7 jours'. Vous pouvez utiliser `DATEDIFF` pour obtenir cette valeur facilement.

## Comment utiliser la fonction `DATE_FORMAT` en SQL

Cette fonction vous permet de présenter vos données comme vous le souhaitez. C'est une fonction très utile. Elle prend la date à formater et une chaîne représentant le format souhaité. La fonction suit ce format :

```sql
DATE_FORMAT(date, format)
```

La chaîne de format peut être de n'importe quelle longueur et chaque caractère définit un format spécifique et doit être précédé du symbole de pourcentage, `%`. Par exemple, étant donné la date `2023-03-10`, vous pouvez la présenter comme `Ven 10 mars, 2023` comme ceci :

```sql
SELECT DATE_FORMAT('2023-03-10', '%a %D %M, %Y');
```

Ici, nous avons passé la chaîne de format `'%a %D %M, %Y'`. Mais que signifie-t-elle vraiment ? Voici quelques points à noter :

* La chaîne de format fournie, `'%a %D %M, %Y'`, est exactement de la même forme que le résultat, `Ven 10 mars, 2023`. Cela signifie que vous pouvez façonner le résultat comme vous le souhaitez – même les caractères d'espace comptent. Chaque caractère dans la chaîne de format est retourné comme partie du résultat, sauf s'il est précédé du signe de pourcentage, auquel cas il est lu comme un caractère de format. Par exemple, réécrire la chaîne de format en `'45 jours à partir d'aujourd'hui est %a, %D jour de %M, %Y'` donnera `45 jours à partir d'aujourd'hui est Ven, 10 jour de mars, 2023`.
* Le `a` utilisé donne le nom du jour de la semaine abrégé, Ven.
* Le `D` retourne le jour du mois avec le suffixe anglais, 10.
* Le `M` retourne le nom du mois, mars.
* Le `Y` retourne l'année, 2023.

Il existe de nombreux autres caractères que vous pouvez utiliser dans la chaîne de format, et vous pouvez les trouver [ici](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format).

## Comment utiliser les fonctions `MAX` et `MIN` en SQL

Bien que ces fonctions ne soient pas limitées ou spécifiques au type de données date, elles sont très utiles lorsque vous travaillez avec des dates. Vous pouvez utiliser MAX pour trouver le dernier enregistrement dans une table. Vous pouvez utiliser MIN pour trouver le plus ancien enregistrement dans une table.

Dans une table d'`employees`, avec un champ `birthday` stockant leur date de naissance, vous pouvez trouver l'employé le plus âgé en utilisant la fonction MAX comme ceci :

```sql
SELECT *
FROM employees
WHERE birthday = (SELECT MAX(birthday) from employees);
```

Ou alternativement, comme ceci :

```sql
SELECT *
FROM employees
ORDER BY birthday DESC
LIMIT 1;
```

Vous pourriez obtenir le plus jeune employé en utilisant la fonction MIN :

```sql
SELECT *
FROM employees
WHERE birthday = (SELECT MIN(birthday) from employees);
```

```sql
SELECT *
FROM employees
ORDER BY birthday
LIMIT 1;
```

## **Résumé**

J'espère que vous comprenez maintenant les fonctions de date MySQL que nous avons discutées ici, leurs variations et arguments, et quand les utiliser pour écrire de meilleures requêtes. Vous pouvez trouver plus de ces fonctions [ici](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me retrouver sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), et [Github](https://github.com/Zubs). C'est rapide, c'est facile, et c'est gratuit !