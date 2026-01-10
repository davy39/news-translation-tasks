---
title: Arrêtez d'écrire du code supplémentaire — vous pouvez le faire en SQL à la
  place
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T22:13:24.000Z'
originalURL: https://freecodecamp.org/news/stop-writing-extra-code-you-can-do-it-in-sql-instead-61883bfcf16d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a0b9O6_F9pLl_BpkjiBPrA.jpeg
tags:
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Arrêtez d'écrire du code supplémentaire — vous pouvez le faire en SQL à
  la place
seo_desc: 'By Geshan Manandhar


  “SQL, Lisp, and Haskell are the only programming languages that I’ve seen where
  one spends more time thinking than typing.“ — Philip Greenspun


  Even with thinking more than typing SQL (Structured Query Language) we software
  engin...'
---

Par Geshan Manandhar

> **SQL, Lisp et Haskell sont les seuls langages de programmation que j'ai vus où l'on passe plus de temps à réfléchir qu'à taper.** — Philip Greenspun

Même en réfléchissant plus qu'en tapant en SQL (Structured Query Language), nous, ingénieurs logiciels, l'utilisons comme un moyen de simplement extraire les données.

> *Nous n'exploitons généralement pas la puissance de manipulation des données de SQL pour effectuer les modifications nécessaires dans notre code.*

Ceci est assez courant parmi les ingénieurs logiciels qui travaillent sur des applications web. Une autre chose que nous manquons est que si nous effectuons la manipulation directement en SQL, les données extraites auront le même format pour tout langage de programmation. Cet article vise à vous éclairer sur les pouvoirs de SQL que vous connaissez peut-être mais que vous n'utilisez généralement pas.

![Image](https://cdn-media-1.freecodecamp.org/images/DbqkDm6MXNYDaK6uYMfg0JO-8v4ZwikjhB7f)
_Image de bougies de [Pixabay](https://pixabay.com/en/tea-lights-candles-light-prayer-2223898/" rel="noopener" target="_blank" title=")_

### TL;DR

Voici les points forts :

* Utilisez SQL pour faire des maths comme la somme, la moyenne, etc.
* Utilisez-le pour regrouper des valeurs relationnelles un-à-plusieurs comme obtenir les catégories de produits.
* Exploitez SQL pour la manipulation de chaînes comme utiliser CONCAT_WS pour concaténer le prénom et le nom.
* Exploitez SQL pour trier selon une formule de priorité personnalisée.

Exemples ci-dessous...

### Quelques hypothèses

Voici quelques hypothèses faites pour cet article :

1. Juste parce que vous pouvez le faire en SQL, cela ne signifie pas que vous devez le faire en SQL et utiliser les ressources de la base de données. Profilez toujours votre solution et décidez ensuite où il est préférable de l'utiliser. Il a été suggéré qu'il est plus difficile et coûteux de mettre à l'échelle une base de données que du code d'application.
2. Utilisez SQL de manière judicieuse et optimale. Pensez toujours aux ressources nécessaires comme le processeur et la mémoire. `EXPLAIN` est votre ami pour l'optimisation des requêtes.
3. Cet article ne préconise pas de mettre toute la logique dans la base de données sous forme de déclencheurs, de procédures stockées ou de vues. Le code dans la base de données ne peut généralement pas être mis dans un système de contrôle de version et tester le code de la base de données est difficile.
4. SQL est généralement insensible à la casse, soyez donc prudent lorsque vous effectuez des opérations comme `CONCAT` ou toute autre manipulation de chaînes.
5. Dans les systèmes distribués, il s'agit d'un équilibre de compromis. Même chose pour décider de faire quelque chose en SQL ou dans le langage de programmation. Évaluez vos options et choisissez la meilleure en fonction du cas d'utilisation.
6. L'exemple ci-dessous utilise MYSQL, donc la syntaxe et l'implémentation pour d'autres variantes de SQL seront différentes.

### L'exemple

Il sera plus facile d'expliquer les superpouvoirs de SQL en le mettant en action dans un exemple. Voici un schéma de base avec 2 tables dans MYSQL pour un microservice de remboursement :

![Image](https://cdn-media-1.freecodecamp.org/images/ri57whhXR9n9RTApP5SsN4vx-fPKYl-RBRYH)

Il y a 2 remboursements et 7 paiements associés comme exemple de [données](http://sqlfiddle.com/#!9/b242d/5).

### Quelques hypothèses

Pour le schéma et les applications du microservice de remboursement, les hypothèses suivantes sont faites :

1. Le microservice de remboursement et la structure de données stockent le fk_item (l'id de l'article commandé/livré), mais ce n'est pas une clé étrangère stricte.
2. L'article peut être remboursé soit en espèces soit en crédit pour le montant payé pour celui-ci.
3. Les articles peuvent être remboursés plusieurs fois tant que le solde restant peut couvrir le montant de remboursement demandé pour chaque espèce et crédit. Par exemple, disons que l'article a été payé 50 en espèces et 50 en crédit. 2 remboursements de 20 espèces et 20 crédits peuvent être effectués. Ainsi, après ces transactions, le solde sera de 10 espèces et 10 crédits pour cet article (50–20–20).
4. Chaque remboursement peut avoir plusieurs articles pour le paiement. Chaque paiement peut être de type soit espèces soit crédit.
5. Tous les montants sont stockés en cents, donc ce sont des entiers.

Maintenant, utilisons quelques pouvoirs de SQL. Vous pouvez trouver l'exemple avec les requêtes associées en cours d'exécution sur ce [SQL Fiddle](http://sqlfiddle.com/#!9/b242d/5).

### Faire les maths en SQL

En tant qu'ingénieurs logiciels, disons que si nous devons trouver le montant total en espèces et en crédit remboursé pour un article, que ferions-nous ? Nous exécuterions quelque chose comme :

`SELECT fk_item, fk_refund, amount, is_cash FROM payment WHERE fk_item=2001;`

Avec les données actuelles, cela donnera 3 lignes comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/47KGYhwpcPnlyHSDJuZmZscjtnCYz8Qz9JfR)

Avec ces 3 lignes, nous les parcourrions en boucle. Si c'est en espèces, accumulez-le dans la variable cashBalance, sinon additionnez-le dans la variable creditBalance. Mais au lieu de cela, ce serait beaucoup plus facile (et probablement plus rapide) de le faire en SQL comme ceci :

`SELECT fk_item, SUM(amount) AS total_paid, IF(is_cash = 1, 'cash', 'credit') as type FROM payment WHERE fk_item = 2001 GROUP BY fk_item, is_cash;`

Ce qui donne ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/8S45Vi1zHw1k2zTRdKiryUwehMrUv5czFUiy)

Le résultat est maintenant facilement obtenu. Si vous avez besoin du remboursement total pour l'article, changez simplement le GROUP BY pour qu'il soit sur fk_item et c'est fait. Pour 2 et 3 enregistrements, cela ne semblera pas significatif. Si il y avait, par exemple, 20 remboursements pour cet article, la première solution avec une boucle est d'écrire plus de code sans gain. Comme pour la somme, d'autres fonctions SQL peuvent également être utilisées. Des opérations mathématiques simples comme [sum](https://www.w3schools.com/sql/func_mysql_sum.asp), multiply, [average](https://www.w3schools.com/sql/func_mysql_avg.asp), etc., peuvent être faciles avec SQL. Cela signifie plus de boucles.

### Utiliser GROUP_CONCAT pour récupérer des valeurs de relation 1:m

[Group concat](http://www.mysqltutorial.org/mysql-group_concat/) est une opération robuste dans les bases de données SQL. Elle est instrumentale lorsque vous devez obtenir des données d'une relation un-à-plusieurs.

Par exemple, disons que vous voulez obtenir tous les tags pour un article de blog ou que vous voulez obtenir toutes les catégories d'un produit. Concernant cet exemple de remboursement, un article peut être remboursé plusieurs fois. Nous allons donc obtenir tous les remboursements associés à l'id de l'article. Pour obtenir cela, nous allons exécuter une seule requête et l'obtenir sans aucune boucle dans le code, comme ci-dessous :

`SELECT fk_item, GROUP_CONCAT(DISTINCT fk_refund) refund_ids FROM payment WHERE fk_item = 2001;`

Cela donne :

![Image](https://cdn-media-1.freecodecamp.org/images/GWnoZNm5uqdxV6fLvd094ozvv8tGcw47vHNl)

Maintenant, nous savons que l'article 2001 a été remboursé deux fois pour 2 remboursements. Il sera facile d'exploser les identifiants de remboursement avec `,` et de procéder à toute opération associée. Soyez conscient que la longueur maximale de GROUP_CONCAT dans MYSQL est de 1024 caractères.

### Manipulation de chaînes

De nombreuses tâches de [manipulation de chaînes](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html) comme sous-chaîne, concaténation, changement de casse et comparaison de chaînes peuvent être effectuées en SQL. Avec cet exemple, je vais montrer l'utilisation de `CONCAT_WS`. Il s'agit d'une concaténation avec un séparateur. Il peut également être utilisé pour sélectionner, par exemple, un first_name et un last_name avec un espace entre les deux.

> *Dans le cas d'un second prénom optionnel, `COALESCE` peut être utilisé avec `CONCAT_WS`. C'est quelque chose pour vous à explorer :).*

Dans cet exemple, je vais sélectionner refund_nr avec sa raison associée :

`SELECT CONCAT_WS("-", refund_nr, reason) AS refund_nr_with_reason FROM refund;`

Ce qui donne :

![Image](https://cdn-media-1.freecodecamp.org/images/h8hVeGa8wznSHn5bRrAc9HorrwPFq7Ysowm8)

Si cela doit être affiché sur le document de note de crédit, par exemple, aucun code supplémentaire n'est nécessaire pour joindre les valeurs à nouveau. SQL le rend à nouveau plus facile. Soyez à nouveau conscient que SQL est un langage insensible à la casse.

### Tri avec une formule personnalisée

Tous les ingénieurs logiciels savent que vous pouvez trier en fonction d'une colonne. Mais si vous avez une formule de priorité personnalisée pour trier, que feriez-vous ? Probablement revenir au code et boucler pour trier. Alors, fixons les règles de la formule de priorité pour l'exemple ci-dessus :

1. Les remboursements des clients premium obtiennent la priorité la plus élevée (nous le bidouillons avec une priorité de 9999999999)
2. Autres que les clients premium, les remboursements en espèces obtiennent une priorité de montant * 25, et pour le crédit, c'est montant * 20.

Selon les règles ci-dessus, il est décidé que les clients premium et la priorité supérieure à 50000 (en cents) seront traités en premier. Ensuite, les autres remboursements seront traités. Obtenons les remboursements prioritaires comme suit :

`SELECT r.refund_nr, r.reason, p.fk_item, p.amount, p.is_cash, IF(p.premium_customer = 1, 9999999999, p.amount * (IF(is_cash = 1, 25, 20))) AS priority FROM refund AS r INNER JOIN payment AS p ON r.id = p.fk_refund HAVING priority > 50000 ORDER BY priority DESC`

Les résultats sont ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/8JRjCiq9YxzYGrv81MxUzPeWBdrZ3prQ5OMp)

Avec l'utilisation appropriée de IF en SQL, le tri par une formule de priorité personnalisée est beaucoup plus facile que d'essayer de le faire avec des boucles dans le code. Remarquez que même des montants plus petits comme 7,5 (750 cents) et 9,0 (900 cents) sont arrivés à la priorité la plus élevée car ces montants de paiement de remboursement étaient associés à des clients premium.

> *Utilisez les superpouvoirs de SQL pour faciliter votre vie en tant qu'ingénieur logiciel.*

Vous pouvez jouer avec l'exemple et exécuter vos requêtes sur [SQL fiddle](http://sqlfiddle.com/#!9/b242d/5).

### Conclusion

Il existe d'autres astuces de SQL qui peuvent vous aider en tant qu'ingénieur logiciel. Comme, `UPDATE` avec `INSERT` en utilisant `ON DUPLICATE KEY UPDATE`. Chaque fois que vous avez envie de faire une manipulation sur les données extraites d'une base de données dans le code avec des boucles, réfléchissez à nouveau. Comme tout autre langage ou outil, SQL est puissant mais utilisez-le judicieusement. Le principal enseignement de cette histoire est :

> *Exploitez la puissance de SQL **de manière optimale et judicieuse** pour écrire moins de code car le meilleur code est celui qui n'a jamais été écrit. S'il n'est pas écrit, il n'y a pas besoin de le maintenir.*

*Vous pouvez lire plus de mes articles de blog sur [geshan.com.np](https://geshan.com.np/blog/2018/12/you-can-do-it-in-sql/).*