---
title: Comment travailler de manière optimale avec les bases de données relationnelles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T16:32:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-optimally-with-relational-databases-627073f82d56
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sd50m5VidzQA8wzhJiFHhQ.jpeg
tags:
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment travailler de manière optimale avec les bases de données relationnelles
seo_desc: 'By Milap Neupane

  Relational databases handle data smoothly, whether working with small volumes or
  processing millions of rows. We will be looking at how we can use relational databases
  according to our needs, and get the most out of them.

  MySQL has b...'
---

Par Milap Neupane

Les bases de données relationnelles gèrent les données de manière fluide, qu'il s'agisse de travailler avec de petits volumes ou de traiter des millions de lignes. Nous allons examiner comment nous pouvons utiliser les bases de données relationnelles selon nos besoins et en tirer le meilleur parti.

MySQL a été un choix populaire pour les petites et grandes entreprises en raison de sa capacité à évoluer. De même, PostgreSQL a également connu une augmentation de popularité.

![Image](https://cdn-media-1.freecodecamp.org/images/NuCURJVqv3ixjGlK-U2yBGDWGzmoloI9PzIe)
*Source de la photo : [https://insights.stackoverflow.com/survey/2018/](https://insights.stackoverflow.com/survey/2018/" rel="noopener" target="_blank" title=")*

> Selon l'enquête [Stack Overflow 2018](https://insights.stackoverflow.com/survey/2018/), MySQL est la base de données la plus populaire parmi tous les utilisateurs.

Les exemples décrits ci-dessous utilisent InnoDB comme moteur MySQL. Ceux-ci ne sont pas limités uniquement à MySQL mais sont également pertinents avec d'autres bases de données relationnelles comme PostgreSQL. Tous les benchmarks sont réalisés sur une machine avec 8 Go de RAM et un processeur i5 à 2,7 GHz.

Commençons par les bases de la manière dont les bases de données relationnelles stockent les données.

### Comprendre les bases de données relationnelles

#### Stockage

MySQL est une base de données relationnelle où toutes les **données** sont représentées en termes de tuples, regroupées en **relations**. Un tuple est représenté par ses attributs.

![Image](https://cdn-media-1.freecodecamp.org/images/5aDL3AR1tfjEnDtw4rPGQYskfOyDJ-V2RBgg)
*Source de l'image : [https://commons.wikimedia.org/wiki/File:Relational_database_terms.svg](https://commons.wikimedia.org/wiki/File:Relational_database_terms.svg" rel="noopener" target="_blank" title=")*

Supposons que nous avons une application où les gens peuvent emprunter des livres. Nous devrons stocker toutes les transactions de prêt de livres. Afin de les stocker, nous avons conçu une simple table relationnelle avec la commande suivante :

```
> CREATE TABLE book_transactions ( id INTEGER NOT NULL   AUTO_INCREMENT, book_id INTEGER, borrower_id INTEGER, lender_id INTEGER, return_date DATE, PRIMARY KEY (id));
```

La table ressemble à ceci :

```
book_transactions
------------------------------------------------
id  borrower_id  lender_id  book_id  return_date
```

Ici, **id** est la clé primaire et **borrower_id**, **lender_id**, **book_id** sont les clés étrangères. Après avoir lancé notre application, quelques transactions sont enregistrées :

```
book_transactions
------------------------------------------------
id  borrower_id  lender_id  book_id  return_date
------------------------------------------------
1   1            1          1        2018-01-13
2   2            3          2        2018-01-13
3   1            2          1        2018-01-13
```

#### Récupération des données

Nous avons une page de tableau de bord pour chaque utilisateur où ils peuvent voir les transactions de leurs livres loués. Alors, récupérons les transactions de livres pour un utilisateur :

```
> SELECT * FROM book_transactions WHERE borrower_id = 1;
book_transactions
------------------------------------------------
id  borrower_id  lender_id  book_id  return_date
------------------------------------------------
1   1            1          1        2018-01-13
2   1            2          1        2018-01-13
```

Cela parcourt la relation séquentiellement et nous donne les données pour l'utilisateur. Cela semble être très rapide, car il y a très peu de données dans notre relation. Pour voir le temps exact de l'exécution de la requête, activez le **profiling** en exécutant la commande suivante :

```
> set profiling=1;
```

Une fois le profiling activé, exécutez à nouveau la requête et utilisez la commande suivante pour voir le **temps d'exécution** :

```
> show profiles;
```

Cela retournera la durée de la requête que nous avons exécutée.

```
Query_ID | Duration   | Query
       1 | 0.00254000 | SELECT * FROM book_transactions ...
```

L'exécution semble être très bonne.

Petit à petit, la table book_transactions commence à se remplir de données, car il y a beaucoup de transactions en cours.

### Le problème

Cela augmente le nombre de **tuples** dans notre relation. Avec cela, le temps nécessaire pour récupérer les transactions de livres pour l'utilisateur commencera à prendre plus de temps. MySQL doit parcourir tous les tuples pour trouver le résultat.

Pour insérer beaucoup de données dans cette table, j'ai écrit la procédure stockée suivante :

```
DELIMITER //
 CREATE PROCEDURE InsertALot()
   BEGIN
   DECLARE i INT DEFAULT 1;
   WHILE (i <= 100000) DO
    INSERT INTO book_transactions (borrower_id, lender_id, book_id,   return_date) VALUES ((FLOOR(1 + RAND() * 60)), (FLOOR(1 + RAND() * 60)), (FLOOR(1 + RAND() * 60)), CURDATE());
    SET i = i+1;
   END WHILE;
 END //
 DELIMITER ;
* Il a fallu environ 7 minutes pour insérer 1,5 million de données
```

Cela insère 100 000 enregistrements aléatoires dans notre table book_transactions. Après avoir exécuté cela, le profileur montre une légère augmentation du temps d'exécution :

```
Query_ID | Duration   | Query
       1 | 0.07151000 | SELECT * FROM book_transactions ...
```

Ajoutons quelques données supplémentaires en exécutant la procédure ci-dessus et voyons ce qui se passe. Avec de plus en plus de données ajoutées, la durée de la requête augmente. Avec 1,5 million de données insérées dans la table, le temps de réponse pour obtenir la même requête est maintenant augmenté.

```
Query_ID | Duration   | Query
       1 | 0.36795200 | SELECT * FROM book_transactions ...
```

Ce n'est qu'une simple requête impliquant un champ entier.

Avec des requêtes plus complexes, des requêtes d'ordre et des requêtes de comptage, le temps d'exécution devient encore pire.

Cela ne semble pas être un long temps pour une seule requête, mais lorsque nous avons des milliers, voire des millions de requêtes qui s'exécutent chaque minute, cela fait une grande différence.

Il y aura beaucoup plus de temps d'attente et cela nuira à la performance globale de l'application. Le temps d'exécution pour la même requête est passé de 2 ms à 370 ms.

### Récupérer la vitesse

#### Index

MySQL et d'autres bases de données fournissent l'indexation, une structure de données qui aide à récupérer les données plus rapidement.

Il existe différents types d'indexation dans MySQL :

* **Clé primaire** — Index ajouté à la clé primaire. Par défaut, les clés primaires sont toujours indexées. Cela garantit également que deux lignes n'ont pas la même valeur de clé primaire.
* **Unique** — L'index de clé unique garantit que deux lignes dans une relation n'ont pas la même valeur. Plusieurs valeurs Null peuvent être stockées avec un index unique.
* **Index** — Ajout à tout autre champ autre que la clé primaire.
* **Texte complet** — L'index de texte complet aide les requêtes contre les données basées sur des caractères.

Il existe principalement deux façons de stocker un index :

**Hash** — cela est principalement utilisé pour la correspondance exacte (=), et ne fonctionne pas avec les comparaisons (⩾, ⩽)

**B-Tree** — C'est la manière la plus courante dont les types d'index mentionnés ci-dessus sont stockés.

MySQL utilise un B-Tree comme format d'indexation par défaut. Les données sont stockées dans un [arbre binaire](https://en.wikipedia.org/wiki/Binary_tree) ce qui rend la récupération des données rapide.

![Image](https://cdn-media-1.freecodecamp.org/images/xUuJBk8kDuyCrIzQTpfznpiwENHzXr5gMLYC)
*Format de stockage des données B-Tree*

L'organisation des données effectuée par le B-tree aide à éviter le scan complet de la table à travers tous les tuples dans notre relation.

Il y a un total de 16 nœuds dans le B-Tree ci-dessus. Supposons que nous devons trouver le nombre 6. Nous devons effectuer un total de 3 scans pour obtenir le nombre. Cela aide à améliorer la performance de la recherche.

Alors, pour améliorer la performance de notre relation book_transactions, ajoutons l'index sur le champ lender_id.

```
> CREATE INDEX lenderId ON book_transactions(lender_id)
----------------------------------------------------
* Il a fallu environ 6,18 secondes pour ajouter cet index
```

La commande ci-dessus ajoute un index sur le champ lender_id. Voyons comment cela affecte la performance pour les 1,5 million de données que nous avons en exécutant à nouveau la même requête.

```
> SELECT * FROM book_transactions WHERE lender_id = 1;
Query_ID | Duration   | Query
       1 | 0.00787600 | SELECT * FROM book_transactions ...
```

Hourra ! Nous sommes de retour.

C'est aussi rapide que lorsque nous avions seulement 3 enregistrements dans notre relation. Avec le bon index ajouté, nous pouvons voir une amélioration spectaculaire des performances.

#### Index composite et index simple

L'index que nous avons ajouté était un index à champ unique. Les index peuvent également être ajoutés à un champ composite.

Si notre requête impliquait plusieurs champs, un index composite nous aurait aidés. Nous pouvons ajouter un index composite avec la commande suivante :

```
> CREATE INDEX lenderReturnDate ON book_transactions(lender_id, return_date);
```

#### Autres utilisations des index

L'interrogation n'est pas la seule utilisation des index. Ils peuvent également être utilisés pour la clause **ORDER BY**. Classons les enregistrements par rapport à lender_id.

```
> SELECT * FROM book_transactions ORDER BY lender_id;
1517185 rows in set (4.08 sec)
```

**4.08** **sec**, c'est beaucoup ! Alors, qu'est-ce qui a mal tourné ? Nous avons notre index en place. Plongeons profondément dans la manière dont la requête est exécutée avec l'aide de la clause **EXPLAIN**.

#### Utilisation de Explain

Nous pouvons ajouter une clause explain pour voir comment la requête sera exécutée dans notre ensemble de données actuel.

```
> EXPLAIN SELECT * FROM book_transactions ORDER BY lender_id;

```

La sortie de cela est comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ZDNJi8luN9QYAnV54eRQ4WZp6WMCQQLnGdOY)
*Utilisation de explain pour voir comment la requête sera exécutée*

Il y a divers champs que [explain](https://dev.mysql.com/doc/refman/5.5/en/explain.html) retourne. Regardons la table ci-dessus et trouvons le problème.

**rows:** Nombre total de lignes qui seront scannées

**filtered:** Le pourcentage de lignes qui seront scannées pour obtenir les données

**type:** Il est donné si l'index est utilisé. ALL signifie qu'il n'utilise pas d'index

**possible_keys, key, key_len** sont tous NULL, ce qui signifie qu'aucun index n'est utilisé.

Alors, pourquoi la requête n'utilise-t-elle pas l'index ?

C'est parce que nous avons `select *` dans notre requête, ce qui signifie que nous sélectionnons tous les champs de notre relation.

L'index n'a des informations que sur les champs qui sont indexés, et non sur les autres champs. Cela signifie que MySQL devra retourner à la table principale pour récupérer les données à nouveau.

Alors, comment devrions-nous écrire la requête ?

#### Sélectionner uniquement le champ requis

Pour supprimer le besoin de retourner à la table principale pour la requête, nous devons sélectionner uniquement la valeur qui est présente dans la table d'index. Alors, changeons la requête :

```
> SELECT lender_id FROM book_transactions ORDER BY lender_id;

```

Cela retournera le résultat en 0,46 seconde, ce qui est beaucoup plus rapide. Mais il y a encore place à l'amélioration.

Comme cette requête est effectuée sur les 1,5 million d'enregistrements que nous avons, elle prend un peu plus de temps car elle doit charger les données en mémoire.

#### Utiliser Limit

Nous n'avons peut-être pas besoin de toutes les 1,5 million de données en même temps. Alors, au lieu de récupérer toutes les données, utiliser LIMIT et récupérer les données par lots est une meilleure façon de procéder.

```
> SELECT lender_id
  FROM book_transactions
  ORDER BY lender_id LIMIT 1000;
```

Avec une limite en place, le temps de réponse s'améliore considérablement et s'exécute en 0,0025 seconde. Maintenant, nous pouvons récupérer le lot suivant avec **OFFSET**.

```
> SELECT lender_id
  FROM book_transactions
  ORDER BY lender_id LIMIT 1000 OFFSET 1000;
```

Cela récupérera le lot suivant de 1000 lignes. Avec cela, nous pouvons augmenter le décalage et la limite pour obtenir toutes les données. Mais il y a un 'piège' ! Avec une augmentation du décalage, la performance de la requête diminue.

C'est parce que MySQL parcourra toutes les données pour atteindre le point de décalage. Il est donc préférable de ne pas utiliser un décalage plus élevé.

#### Et la requête Count ?

Le moteur InnoDB a la capacité d'écrire de manière concurrente. Cela le rend hautement évolutif et améliore le débit par seconde.

Mais cela a un coût. InnoDB ne peut pas ajouter de compteur de cache pour le nombre d'enregistrements dans une table. Ainsi, le comptage doit être effectué en temps réel en parcourant toutes les données filtrées. Cela rend la requête COUNT lente.

Il est donc recommandé de calculer les données de comptage résumées à partir de la logique de l'application pour un grand nombre de données.

### Pourquoi ne pas ajouter un index à tous les champs ?

L'ajout d'un index aide à améliorer considérablement les performances, mais cela a également un coût. Il doit être utilisé efficacement. L'ajout d'un index à plus de champs pose les problèmes suivants :

* Nécessite beaucoup de mémoire, machine plus grande
* Lorsque nous supprimons, il y a une réindexation (intensive en CPU et suppressions plus lentes)
* Lorsque nous ajoutons quelque chose, il y a une réindexation (intensive en CPU et insertions plus lentes)
* La mise à jour ne fait pas de réindexation complète, donc la mise à jour est plus rapide et efficace en CPU.

Nous sommes maintenant clairs que l'ajout d'un index aide beaucoup. Mais nous ne pouvons pas sélectionner toutes les données, sauf celles qui sont indexées pour des performances rapides.

Alors, comment pouvons-nous sélectionner tous les attributs et obtenir des performances rapides ?

### Partitionnement

Lors de la création d'index, nous n'avons des informations que sur le champ qui est indexé. Mais nous n'avons pas de données sur les champs qui ne sont pas présents dans l'index.

Ainsi, comme nous l'avons dit précédemment, MySQL doit revenir à la table principale pour obtenir les données des autres champs. Cela peut ralentir le temps d'exécution.

La manière dont nous pouvons résoudre cela est en utilisant le partitionnement.

Le partitionnement est une technique dans laquelle MySQL divise les données d'une table en plusieurs tables, mais les gère toujours comme une seule.

Lors de l'exécution de toute opération dans la table, nous devons spécifier quelle partition est utilisée. Avec les données étant décomposées, MySQL a un ensemble de données plus petit à interroger. Trouver le bon partitionnement selon les besoins est la clé pour des performances élevées.

Mais si nous utilisons toujours la même machine, cela évoluera-t-il ?

### Sharding

Avec un grand ensemble de données, stocker toutes vos données sur la même machine peut être problématique.

Une partition spécifique peut être lourde et nécessite plus de requêtes, tandis que d'autres le sont moins. Ainsi, l'une affectera l'autre. Elles ne peuvent pas évoluer séparément.

Supposons que les données des trois derniers mois soient les plus utilisées, tandis que les plus anciennes le sont moins. Peut-être que les données récentes sont principalement mises à jour/créées tandis que les anciennes données sont principalement seulement lues.

Pour résoudre ce problème, nous pouvons déplacer la partition des trois derniers mois vers une autre machine. Le sharding est une manière de diviser un grand ensemble de données en morceaux plus petits et de les déplacer vers des SGBDR séparés. En d'autres termes, le sharding peut également être appelé 'partitionnement horizontal'.

Les bases de données relationnelles ont la capacité d'évoluer à mesure que l'application grandit. Trouver le bon index et ajuster l'infrastructure selon les besoins est nécessaire.

---

Également publié sur le blog de Milap Neupane : [Comment travailler de manière optimale avec les bases de données relationnelles](https://milapneupane.com.np/2019/07/06/how-to-work-optimally-with-relational-databases/)