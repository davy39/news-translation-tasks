---
title: Un examen approfondi de l'indexation des bases de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-16T14:05:46.000Z'
originalURL: https://freecodecamp.org/news/database-indexing-at-a-glance-bb50809d48bd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca322740569d1a4ca596f.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Un examen approfondi de l'indexation des bases de données
seo_desc: 'By Kousik Nath

  Performance is extremely important in many consumer products like e-commerce, payment
  systems, gaming, transportation apps, and so on. Although databases are internally
  optimised through multiple mechanisms to meet their performance re...'
---

Par Kousik Nath

Les performances sont extrêmement importantes dans de nombreux produits grand public comme le commerce électronique, les systèmes de paiement, les jeux, les applications de transport, etc. Bien que les bases de données soient optimisées en interne par le biais de multiples mécanismes pour répondre à leurs exigences de performance dans le monde moderne, beaucoup dépend également du développeur d'applications — après tout, seul un développeur sait quelles requêtes l'application doit effectuer.

Les développeurs qui travaillent avec des bases de données relationnelles ont utilisé ou au moins entendu parler de l'indexation, et c'est un concept très courant dans le monde des bases de données. Cependant, la partie la plus importante est de comprendre quoi indexer et comment l'indexation va améliorer le temps de réponse des requêtes. Pour cela, vous devez comprendre comment vous allez interroger vos tables de base de données. Un index approprié ne peut être créé que lorsque vous savez exactement à quoi ressemblent vos requêtes et vos modèles d'accès aux données.

En termes simples, un index mappe les clés de recherche aux données correspondantes sur le disque en utilisant différentes structures de données en mémoire et sur disque. L'index est utilisé pour accélérer la recherche en réduisant le nombre d'enregistrements à rechercher.

La plupart du temps, un index est créé sur les colonnes spécifiées dans la clause `WHERE` d'une requête, car la base de données récupère et filtre les données des tables en fonction de ces colonnes. Si vous ne créez pas d'index, la base de données analyse toutes les lignes, filtre les lignes correspondantes et retourne le résultat. Avec des millions d'enregistrements, cette opération de balayage peut prendre plusieurs secondes et ce temps de réponse élevé rend les API et les applications plus lentes et inutilisables. Regardons un exemple —

Nous allons utiliser MySQL avec un moteur de base de données InnoDB par défaut, bien que les concepts expliqués dans cet article soient plus ou moins les mêmes dans d'autres serveurs de bases de données comme Oracle, MSSQL, etc.

Créez une table appelée `index_demo` avec le schéma suivant :

```sql
CREATE TABLE index_demo ( 
    name VARCHAR(20) NOT NULL, 
    age INT, 
    pan_no VARCHAR(20), 
    phone_no VARCHAR(20) 
);
```

#### Comment vérifier que nous utilisons le moteur InnoDB ?

Exécutez la commande suivante :

```sql
SHOW TABLE STATUS WHERE name = 'index_demo' \G;
```

![Image](https://cdn-media-1.freecodecamp.org/images/uxVilFVSg5RdsxB4PUlc4VLgroz3w9OMVkmM)

La colonne `Engine` dans la capture d'écran ci-dessus représente le moteur utilisé pour créer la table. Ici, `InnoDB` est utilisé.

Maintenant, insérez quelques données aléatoires dans la table, ma table avec 5 lignes ressemble à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/CRQKjuAqZ5BpQpQFJIMRmnb23VdRb9UUqJfb)

Je n'ai pas créé d'index jusqu'à présent sur cette table. Vérifions cela avec la commande : `SHOW INDEX`. Elle retourne 0 résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/F8nt1XUt0AJmVyjxX6rCUtK18tANZPKogvdj)

À ce stade, si nous exécutons une simple requête `SELECT`, comme il n'y a pas d'index défini par l'utilisateur, la requête analysera toute la table pour trouver le résultat :

```sql
EXPLAIN SELECT * FROM index_demo WHERE name = 'alex';
```

![Image](https://cdn-media-1.freecodecamp.org/images/cTrVkwvORbzU51MvqnKt7sDTHfQznnjKKFsJ)

`EXPLAIN` montre comment le moteur de requête prévoit d'exécuter la requête. Dans la capture d'écran ci-dessus, vous pouvez voir que la colonne `rows` retourne `5` et `possible_keys` retourne `null`. `possible_keys` représente tous les index disponibles qui peuvent être utilisés dans cette requête. La colonne `key` représente quel index va être utilisé parmi tous les index possibles dans cette requête.

### Clé primaire :

La requête ci-dessus est très inefficace. Optimisons cette requête. Nous allons faire de la colonne `phone_no` une `PRIMARY KEY` en supposant qu'aucun utilisateur ne peut exister dans notre système avec le même numéro de téléphone. Prenez en considération les points suivants lors de la création d'une clé primaire :

* Une clé primaire doit faire partie de nombreuses requêtes vitales dans votre application.
* La clé primaire est une contrainte qui identifie de manière unique chaque ligne dans une table. Si plusieurs colonnes font partie de la clé primaire, cette combinaison doit être unique pour chaque ligne.
* La clé primaire doit être non nulle. Ne faites jamais de champs nullables votre clé primaire. Selon les normes ANSI SQL, les clés primaires doivent être comparables entre elles, et vous devez définitivement pouvoir dire si la valeur de la colonne de la clé primaire pour une ligne particulière est supérieure, inférieure ou égale à celle d'une autre ligne. Puisque `NULL` signifie une valeur non définie dans les normes SQL, vous ne pouvez pas comparer de manière déterministe `NULL` avec toute autre valeur, donc logiquement `NULL` n'est pas autorisé.
* Le type idéal de clé primaire doit être un nombre comme `INT` ou `BIGINT` car les comparaisons d'entiers sont plus rapides, donc le parcours de l'index sera très rapide.

Souvent, nous définissons un champ `id` comme `AUTO INCREMENT` dans les tables et l'utilisons comme clé primaire, mais le choix d'une clé primaire dépend des développeurs.

#### Que se passe-t-il si vous ne créez pas de clé primaire vous-même ?

Il n'est pas obligatoire de créer une clé primaire vous-même. Si vous n'avez défini aucune clé primaire, InnoDB en crée une implicitement pour vous car InnoDB doit par conception avoir une clé primaire dans chaque table. Donc, une fois que vous créez une clé primaire plus tard pour cette table, InnoDB supprime la clé primaire précédemment définie automatiquement.

Puisque nous n'avons pas défini de clé primaire pour l'instant, voyons ce qu'InnoDB a créé par défaut pour nous :

```sql
SHOW EXTENDED INDEX FROM index_demo;
```

![Image](https://cdn-media-1.freecodecamp.org/images/49GA8I8PuohOIIAjmWpztDIWgyAwD8LUwVQN)

`EXTENDED` montre tous les index qui ne sont pas utilisables par l'utilisateur mais gérés complètement par MySQL.

Ici, nous voyons que MySQL a défini un index composite (nous discuterons des index composites plus tard) sur `DB_ROW_ID`, `DB_TRX_ID`, `DB_ROLL_PTR`, et toutes les colonnes définies dans la table. En l'absence de clé primaire définie par l'utilisateur, cet index est utilisé pour trouver les enregistrements de manière unique.

#### Quelle est la différence entre clé et index ?

Bien que les termes `clé` et `index` soient utilisés de manière interchangeable, `clé` signifie une contrainte imposée sur le comportement de la colonne. Dans ce cas, la contrainte est que la clé primaire est un champ non nullable qui identifie de manière unique chaque ligne. D'autre part, `index` est une structure de données spéciale qui facilite la recherche de données dans la table.

Créons maintenant l'index primaire sur `phone_no` et examinons l'index créé :

```sql
ALTER TABLE index_demo ADD PRIMARY KEY (phone_no);
SHOW INDEXES FROM index_demo;
```

Notez que `CREATE INDEX` ne peut pas être utilisé pour créer un index primaire, mais `ALTER TABLE` est utilisé.

![Image](https://cdn-media-1.freecodecamp.org/images/JMvreHhinpyihnKSQybzuyfDIAi2JWiIPCDh)

Dans la capture d'écran ci-dessus, nous voyons qu'un index primaire est créé sur la colonne `phone_no`. Les colonnes des images suivantes sont décrites comme suit :

`Table` : La table sur laquelle l'index est créé.

`Non_unique` : Si la valeur est 1, l'index n'est pas unique, si la valeur est 0, l'index est unique.

`Key_name` : Le nom de l'index créé. Le nom de l'index primaire est toujours `PRIMARY` dans MySQL, indépendamment du fait que vous ayez fourni un nom d'index ou non lors de la création de l'index.

`Seq_in_index` : Le numéro de séquence de la colonne dans l'index. Si plusieurs colonnes font partie de l'index, le numéro de séquence sera attribué en fonction de l'ordre des colonnes lors de la création de l'index. Le numéro de séquence commence à 1.

`Collation` : comment la colonne est triée dans l'index. `A` signifie ascendant, `D` signifie descendant, `NULL` signifie non trié.

`Cardinality` : Le nombre estimé de valeurs uniques dans l'index. Plus la cardinalité est élevée, plus les chances que l'optimiseur de requêtes choisisse l'index pour les requêtes sont grandes.

`Sub_part` : Le préfixe de l'index. Il est `NULL` si la colonne entière est indexée. Sinon, il montre le nombre d'octets indexés dans le cas où la colonne est partiellement indexée. Nous définirons un index partiel plus tard.

`Packed` : Indique comment la clé est compressée ; `NULL` si elle ne l'est pas.

`Null` : `YES` si la colonne peut contenir des valeurs `NULL` et vide si ce n'est pas le cas.

`Index_type` : Indique quelle structure de données d'index est utilisée pour cet index. Certains candidats possibles sont — `BTREE`, `HASH`, `RTREE`, ou `FULLTEXT`.

`Comment` : Les informations sur l'index non décrites dans sa propre colonne.

`Index_comment` : Le commentaire pour l'index spécifié lorsque vous avez créé l'index avec l'attribut `COMMENT`.

Maintenant, voyons si cet index réduit le nombre de lignes qui seront recherchées pour un `phone_no` donné dans la clause `WHERE` d'une requête.

```sql
EXPLAIN SELECT * FROM index_demo WHERE phone_no = '9281072002';
```

![Image](https://cdn-media-1.freecodecamp.org/images/TJz8cx0CrDPswJzfooUNA5HThlP5bAqZ5f8w)

Dans cette capture, notez que la colonne `rows` a retourné `1` seulement, les colonnes `possible_keys` et `key` retournent toutes deux `PRIMARY`. Donc, cela signifie essentiellement que, en utilisant l'index primaire nommé `PRIMARY` (le nom est automatiquement attribué lorsque vous créez la clé primaire), l'optimiseur de requêtes va directement à l'enregistrement et le récupère. C'est très efficace. C'est exactement à quoi sert un index — minimiser la portée de la recherche au coût d'un espace supplémentaire.

### Index clusterisé :

Un `index clusterisé` est colocalisé avec les données dans le même espace de table ou le même fichier disque. Vous pouvez considérer qu'un index clusterisé est un index `B-Tree` dont les nœuds feuilles sont les blocs de données réels sur le disque, puisque l'index et les données résident ensemble. Ce type d'index organise physiquement les données sur le disque selon l'ordre logique de la clé d'index.

#### Que signifie l'organisation physique des données ?

Physiquement, les données sont organisées sur le disque à travers des milliers ou des millions de blocs de disque / blocs de données. Pour un index clusterisé, il n'est pas obligatoire que tous les blocs de disque soient stockés de manière contiguë. Les blocs de données physiques sont tout le temps déplacés ici et là par le système d'exploitation chaque fois que c'est nécessaire. Un système de base de données n'a aucun contrôle absolu sur la manière dont l'espace de données physique est géré, mais à l'intérieur d'un bloc de données, les enregistrements peuvent être stockés ou gérés dans l'ordre logique de la clé d'index. Le diagramme simplifié suivant l'explique :

![Image](https://cdn-media-1.freecodecamp.org/images/aVIkXV0c5nNwQHjL1T501JC0OG-E9iZGzt3H)

* Le grand rectangle de couleur jaune représente un bloc de disque / bloc de données
* les rectangles de couleur bleue représentent les données stockées sous forme de lignes à l'intérieur de ce bloc
* la zone de pied de page représente l'index du bloc où les petits rectangles de couleur rouge résident dans l'ordre trié d'une clé particulière. Ces petits blocs ne sont rien d'autre que des pointeurs pointant vers les décalages des enregistrements.

Les enregistrements sont stockés sur le bloc de disque dans un ordre arbitraire. Chaque fois que de nouveaux enregistrements sont ajoutés, ils sont ajoutés dans l'espace disponible suivant. Chaque fois qu'un enregistrement existant est mis à jour, le système d'exploitation décide si cet enregistrement peut encore s'adapter à la même position ou si une nouvelle position doit être allouée pour cet enregistrement.

Ainsi, la position des enregistrements est entièrement gérée par le système d'exploitation et aucune relation définie n'existe entre l'ordre de deux enregistrements. Afin de récupérer les enregistrements dans l'ordre logique de la clé, les pages de disque contiennent une section d'index dans le pied de page, l'index contient une liste de pointeurs de décalage dans l'ordre de la clé. Chaque fois qu'un enregistrement est modifié ou créé, l'index est ajusté.

De cette manière, vous n'avez vraiment pas besoin de vous soucier de l'organisation physique réelle des enregistrements dans un certain ordre, mais une petite section d'index est maintenue dans cet ordre et la récupération ou la maintenance des enregistrements devient très facile.

#### Avantages de l'index clusterisé :

Cet ordre ou cette colocalisation de données connexes rend en fait un index clusterisé plus rapide. Lorsque les données sont récupérées du disque, le bloc complet contenant les données est lu par le système puisque notre système d'E/S de disque écrit et lit les données par blocs. Donc, dans le cas de requêtes de plage, il est tout à fait possible que les données colocalisées soient mises en mémoire tampon. Supposons que vous exécutiez la requête suivante :

```sql
SELECT * FROM index_demo WHERE phone_no > '9010000000' AND phone_no < '9020000000'
```

Un bloc de données est récupéré en mémoire lorsque la requête est exécutée. Supposons que le bloc de données contient `phone_no` dans la plage de `9010000000` à `9030000000`. Donc, quelle que soit la plage que vous avez demandée dans la requête, ce n'est qu'un sous-ensemble des données présentes dans le bloc. Si vous exécutez maintenant la requête suivante pour obtenir tous les numéros de téléphone dans la plage, disons de `9015000000` à `9019000000`, vous n'avez pas besoin de récupérer d'autres blocs du disque. L'ensemble des données peut être trouvé dans le bloc de données actuel, ainsi `clustered_index` réduit le nombre d'E/S de disque en colocalisant les données connexes autant que possible dans le même bloc de données. Cette réduction des E/S de disque entraîne une amélioration des performances.

Ainsi, si vous avez une clé primaire bien pensée et que vos requêtes sont basées sur la clé primaire, les performances seront super rapides.

#### Contraintes de l'index clusterisé :

Puisqu'un index clusterisé impacte l'organisation physique des données, il ne peut y avoir qu'un seul index clusterisé par table.

#### Relation entre la clé primaire et l'index clusterisé :

Vous ne pouvez pas créer manuellement un index clusterisé en utilisant InnoDB dans MySQL. MySQL le choisit pour vous. Mais comment le choisit-il ? Les extraits suivants proviennent de la documentation MySQL :

> Lorsque vous définissez une `PRIMARY KEY` sur votre table, `InnoDB` l'utilise comme index clusterisé. Définissez une clé primaire pour chaque table que vous créez. Si aucune colonne ou ensemble de colonnes unique et non nulle n'existe logiquement, ajoutez une nouvelle colonne [auto-incrémentée](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_auto_increment), dont les valeurs sont remplies automatiquement.  
>   
> Si vous ne définissez pas de `PRIMARY KEY` pour votre table, MySQL localise le premier index `UNIQUE` où toutes les colonnes clés sont `NOT NULL` et `InnoDB` l'utilise comme index clusterisé.  
>   
> Si la table n'a pas de `PRIMARY KEY` ou d'index `UNIQUE` approprié, `InnoDB` génère en interne un index clusterisé caché nommé `GEN_CLUST_INDEX` sur une colonne synthétique contenant des valeurs d'ID de ligne. Les lignes sont ordonnées par l'ID que `InnoDB` attribue aux lignes dans une telle table. L'ID de ligne est un champ de 6 octets qui augmente de manière monotone à mesure que de nouvelles lignes sont insérées. Ainsi, les lignes ordonnées par l'ID de ligne sont physiquement dans l'ordre d'insertion.

En bref, le moteur MySQL InnoDB gère en fait l'index primaire comme un index clusterisé pour améliorer les performances, donc la clé primaire et l'enregistrement réel sur le disque sont clusterisés ensemble.

#### Structure de l'index de clé primaire (clusterisé) :

Un index est généralement maintenu sous forme d'arbre B+ sur le disque et en mémoire, et tout index est stocké dans des blocs sur le disque. Ces blocs sont appelés blocs d'index. Les entrées dans le bloc d'index sont toujours triées sur la clé d'index/recherche. Le bloc d'index feuille de l'index contient un localisateur de ligne. Pour l'index primaire, le localisateur de ligne fait référence à l'adresse virtuelle de l'emplacement physique des blocs de données sur le disque où les lignes résident en étant triées selon la clé d'index.

Dans le diagramme suivant, les rectangles de gauche représentent les blocs d'index de niveau feuille, et les rectangles de droite représentent les blocs de données. Logiquement, les blocs de données semblent être alignés dans un ordre trié, mais comme déjà décrit précédemment, les emplacements physiques réels peuvent être dispersés ici et là.

![Image](https://cdn-media-1.freecodecamp.org/images/9IxaFv3dJJe6m0NotCQC6wXzzo6bcGQwwNCu)

#### Est-il possible de créer un index primaire sur une clé non primaire ?

Dans MySQL, un index primaire est automatiquement créé, et nous avons déjà décrit ci-dessus comment MySQL choisit l'index primaire. Mais dans le monde des bases de données, il n'est en fait pas nécessaire de créer un index sur la colonne de clé primaire — l'index primaire peut être créé sur n'importe quelle colonne non primaire également. Mais lorsqu'il est créé sur la clé primaire, toutes les entrées de clé sont uniques dans l'index, tandis que dans l'autre cas, l'index primaire peut également avoir une clé dupliquée.

#### Est-il possible de supprimer une clé primaire ?

Il est possible de supprimer une clé primaire. Lorsque vous supprimez une clé primaire, l'index clusterisé associé ainsi que la propriété d'unicité de cette colonne sont perdus.

```sql
ALTER TABLE `index_demo` DROP PRIMARY KEY;

- Si la clé primaire n'existe pas, vous obtenez l'erreur suivante :

"ERROR 1091 (42000): Can't DROP 'PRIMARY'; check that column/key exists"
```

#### Avantages de l'index primaire :

* Les requêtes de plage basées sur l'index primaire sont très efficaces. Il est possible que le bloc de disque que la base de données a lu du disque contienne toutes les données appartenant à la requête, puisque l'index primaire est clusterisé et les enregistrements sont ordonnés physiquement. Ainsi, la localité des données peut être fournie par l'index primaire.
* Toute requête qui tire parti de la clé primaire est très rapide.

#### Inconvénients de l'index primaire :

* Puisque l'index primaire contient une référence directe à l'adresse du bloc de données via l'espace d'adressage virtuel et que les blocs de disque sont physiquement organisés dans l'ordre de la clé d'index, chaque fois que le système d'exploitation effectue une division de page de disque en raison d'opérations `DML` comme `INSERT` / `UPDATE` / `DELETE`, l'index primaire doit également être mis à jour. Ainsi, les opérations `DML` exercent une certaine pression sur les performances de l'index primaire.

### Index secondaire :

Tout index autre qu'un index clusterisé est appelé un index secondaire. Les index secondaires n'impactent pas les emplacements de stockage physiques contrairement aux index primaires.

#### Quand avez-vous besoin d'un index secondaire ?

Vous pouvez avoir plusieurs cas d'utilisation dans votre application où vous n'interrogez pas la base de données avec une clé primaire. Dans notre exemple, `phone_no` est la clé primaire, mais nous pouvons avoir besoin d'interroger la base de données avec `pan_no`, ou `name`. Dans de tels cas, vous avez besoin d'index secondaires sur ces colonnes si la fréquence de ces requêtes est très élevée.

#### Comment créer un index secondaire dans MySQL ?

La commande suivante crée un index secondaire dans la colonne `name` de la table `index_demo`.

```sql
CREATE INDEX secondary_idx_1 ON index_demo (name);
```

![Image](https://cdn-media-1.freecodecamp.org/images/iWZI5S-Lqf9EljZxrNpmFCIajB8kmsTVkQ0i)

#### Structure de l'index secondaire :

Dans le diagramme ci-dessous, les rectangles de couleur rouge représentent les blocs d'index secondaires. L'index secondaire est également maintenu dans l'arbre B+ et il est trié selon la clé sur laquelle l'index a été créé. Les nœuds feuilles contiennent une copie de la clé des données correspondantes dans l'index primaire.

Ainsi, pour comprendre, vous pouvez supposer que l'index secondaire a une référence à l'adresse de la clé primaire, bien que ce ne soit pas le cas. La récupération des données via l'index secondaire signifie que vous devez parcourir deux arbres B+ — l'un est l'arbre B+ de l'index secondaire lui-même, et l'autre est l'arbre B+ de l'index primaire.

![Image](https://cdn-media-1.freecodecamp.org/images/0eg06hWYJWhXPt1QNuaDlETYrmnSKAo6Nf44)

#### Avantages d'un index secondaire :

Logiquement, vous pouvez créer autant d'index secondaires que vous le souhaitez. Mais en réalité, le nombre d'index réellement nécessaires nécessite un processus de réflexion sérieux, car chaque index a sa propre pénalité.

#### Inconvénients d'un index secondaire :

Avec les opérations `DML` comme `DELETE` / `INSERT`, l'index secondaire doit également être mis à jour afin que la copie de la colonne de clé primaire puisse être supprimée / insérée. Dans de tels cas, l'existence de nombreux index secondaires peut créer des problèmes.

De plus, si une clé primaire est très grande comme une `URL`, puisque les index secondaires contiennent une copie de la valeur de la colonne de clé primaire, cela peut être inefficace en termes de stockage. Plus il y a de clés secondaires, plus le nombre de copies dupliquées de la valeur de la colonne de clé primaire est grand, donc plus de stockage en cas de clé primaire grande. De plus, la clé primaire elle-même stocke les clés, donc l'effet combiné sur le stockage sera très élevé.

#### Considérations avant de supprimer un index primaire :

Dans MySQL, vous pouvez supprimer un index primaire en supprimant la clé primaire. Nous avons déjà vu qu'un index secondaire dépend d'un index primaire. Donc, si vous supprimez un index primaire, tous les index secondaires doivent être mis à jour pour contenir une copie de la nouvelle clé d'index primaire que MySQL ajuste automatiquement.

Ce processus est coûteux lorsque plusieurs index secondaires existent. De plus, d'autres tables peuvent avoir une référence de clé étrangère à la clé primaire, vous devez donc supprimer ces références de clé étrangère avant de supprimer la clé primaire.

Lorsque une clé primaire est supprimée, MySQL crée automatiquement une autre clé primaire en interne, et c'est une opération coûteuse.

### Index de clé UNIQUE :

Comme les clés primaires, les clés uniques peuvent également identifier les enregistrements de manière unique avec une différence — la colonne de clé unique peut contenir des valeurs `null`.

Contrairement à d'autres serveurs de bases de données, dans MySQL, une colonne de clé unique peut avoir autant de valeurs `null` que possible. Dans la norme SQL, `null` signifie une valeur non définie. Donc, si MySQL doit contenir une seule valeur `null` dans une colonne de clé unique, il doit supposer que toutes les valeurs null sont les mêmes.

Mais logiquement, ce n'est pas correct puisque `null` signifie non défini — et les valeurs non définies ne peuvent pas être comparées entre elles, c'est la nature de `null`. Comme MySQL ne peut pas affirmer si tous les `null` signifient la même chose, il permet plusieurs valeurs `null` dans la colonne.

La commande suivante montre comment créer un index de clé unique dans MySQL :

```sql
CREATE UNIQUE INDEX unique_idx_1 ON index_demo (pan_no);
```

![Image](https://cdn-media-1.freecodecamp.org/images/ApzPAl3z-AwYSR7YXofmjf17TYXgPLHoX6AZ)

### Index composite :

MySQL vous permet de définir des index sur plusieurs colonnes, jusqu'à 16 colonnes. Cet index est appelé un index multi-colonnes / composite / composé.

Supposons que nous avons un index défini sur 4 colonnes — `col1`, `col2`, `col3`, `col4`. Avec un index composite, nous avons une capacité de recherche sur `col1`, `(col1, col2)`, `(col1, col2, col3)`, `(col1, col2, col3, col4)`. Donc nous pouvons utiliser n'importe quel préfixe de gauche des colonnes indexées, mais nous ne pouvons pas omettre une colonne du milieu et utiliser cela comme — `(col1, col3)` ou `(col1, col2, col4)` ou `col3` ou `col4`, etc. Ce sont des combinaisons invalides.

Les commandes suivantes créent 2 index composites dans notre table :

```sql
CREATE INDEX composite_index_1 ON index_demo (phone_no, name, age);

CREATE INDEX composite_index_2 ON index_demo (pan_no, name, age);
```

Si vous avez des requêtes contenant une clause `WHERE` sur plusieurs colonnes, écrivez la clause dans l'ordre des colonnes de l'index composite. L'index bénéficiera à cette requête. En fait, lors de la décision des colonnes pour un index composite, vous pouvez analyser différents cas d'utilisation de votre système et essayer de trouver l'ordre des colonnes qui bénéficiera à la plupart de vos cas d'utilisation.

Les index composites peuvent vous aider dans les requêtes `JOIN` et `SELECT` également. Exemple : dans la requête `SELECT *` suivante, `composite_index_2` est utilisé.

![Image](https://cdn-media-1.freecodecamp.org/images/SmJU2MejEJjaWUtJxkYprwJXNye6fOhYvkFr)

Lorsque plusieurs index sont définis, l'optimiseur de requêtes MySQL choisit celui qui élimine le plus grand nombre de lignes ou qui analyse le moins de lignes possible pour une meilleure efficacité.

#### Pourquoi utilisons-nous des index composites ? Pourquoi ne pas définir plusieurs index secondaires sur les colonnes qui nous intéressent ?

_MySQL utilise un seul index par table par requête sauf pour UNION._ (Dans une UNION, chaque requête logique est exécutée séparément, et les résultats sont fusionnés.) Donc, définir plusieurs index sur plusieurs colonnes ne garantit pas que ces index seront utilisés même s'ils font partie de la requête.

MySQL maintient ce qu'on appelle les statistiques d'index qui aident MySQL à déduire à quoi ressemblent les données dans le système. Les statistiques d'index sont une généralisation, mais sur la base de ces métadonnées, MySQL décide quel index est approprié pour la requête actuelle.

#### Comment fonctionne l'index composite ?

Les colonnes utilisées dans les index composites sont concaténées ensemble, et ces clés concaténées sont stockées dans l'ordre trié en utilisant un arbre B+. Lorsque vous effectuez une recherche, la concaténation de vos clés de recherche est comparée à celles de l'index composite. Ensuite, s'il y a une incompatibilité entre l'ordre de vos clés de recherche et l'ordre des colonnes de l'index composite, l'index ne peut pas être utilisé.

Dans notre exemple, pour l'enregistrement suivant, une clé d'index composite est formée en concaténant `pan_no`, `name`, `age` — `HJKXS9086Wkousik28`.

```sql
+--------+------+------------+------------+
 name   
 age  
 pan_no     
 phone_no
 
+--------+------+------------+------------+
 kousik 
   28 
 HJKXS9086W 
 9090909090
```

#### Comment identifier si vous avez besoin d'un index composite :

* Analysez d'abord vos requêtes selon vos cas d'utilisation. Si vous voyez que certains champs apparaissent ensemble dans de nombreuses requêtes, vous pouvez envisager de créer un index composite.
* Si vous créez un index dans `col1` et un index composite dans (`col1`, `col2`), alors seul l'index composite devrait suffire. `col1` seul peut être servi par l'index composite lui-même puisqu'il s'agit d'un préfixe de gauche de l'index.
* Considérez la cardinalité. Si les colonnes utilisées dans l'index composite finissent par avoir une cardinalité élevée ensemble, elles sont de bons candidats pour l'index composite.

### Index couvrant :

Un index couvrant est un type spécial d'index composite où toutes les colonnes spécifiées dans la requête existent quelque part dans l'index. Ainsi, l'optimiseur de requêtes n'a pas besoin d'accéder à la base de données pour obtenir les données — plutôt, il obtient le résultat de l'index lui-même. Exemple : nous avons déjà défini un index composite sur `(pan_no, name, age)`, donc maintenant considérons la requête suivante :

```sql
SELECT age FROM index_demo WHERE pan_no = 'HJKXS9086W' AND name = 'kousik'
```

Les colonnes mentionnées dans les clauses `SELECT` et `WHERE` font partie de l'index composite. Donc, dans ce cas, nous pouvons en fait obtenir la valeur de la colonne `age` à partir de l'index composite lui-même. Voyons ce que la commande `EXPLAIN` montre pour cette requête :

```sql
EXPLAIN FORMAT=JSON SELECT age FROM index_demo WHERE pan_no = 'HJKXS9086W' AND name = '111kousik1';
```

![Image](https://cdn-media-1.freecodecamp.org/images/1HqlKe6UuO9ldQ3tgbZ0zxsHdm8YBxHARAUK)

Dans la réponse ci-dessus, notez qu'il y a une clé — `using_index` qui est définie sur `true` ce qui signifie que l'index couvrant a été utilisé pour répondre à la requête.

Je ne sais pas dans quelle mesure les index couvrant sont appréciés dans les environnements de production, mais apparemment, cela semble être une bonne optimisation si la requête correspond au projet de loi.

### Index partiel :

Nous savons déjà que les index accélèrent nos requêtes au coût de l'espace. Plus vous avez d'index, plus les exigences de stockage sont élevées. Nous avons déjà créé un index appelé `secondary_idx_1` sur la colonne `name`. La colonne `name` peut contenir de grandes valeurs de n'importe quelle longueur. De plus, dans l'index, les métadonnées des localisateurs de lignes ou des pointeurs de lignes ont leur propre taille. Donc, globalement, un index peut avoir une charge de stockage et de mémoire élevée.

Dans MySQL, il est possible de créer un index sur les premiers octets des données. Exemple : la commande suivante crée un index sur les 4 premiers octets du nom. Bien que cette méthode réduise la surcharge de mémoire d'un certain montant, l'index ne peut pas éliminer de nombreuses lignes, puisque dans cet exemple, les 4 premiers octets peuvent être communs à de nombreux noms. Habituellement, ce type d'indexation de préfixe est pris en charge sur les colonnes de type `CHAR`, `VARCHAR`, `BINARY`, `VARBINARY`.

```sql
CREATE INDEX secondary_index_1 ON index_demo (name(4));
```

#### Que se passe-t-il sous le capot lorsque nous définissons un index ?

Exécutons à nouveau la commande `SHOW EXTENDED` :

```sql
SHOW EXTENDED INDEXES FROM index_demo;
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZdBDdRbFqPSdScLJ51qAVPaDffc4qUXcAtUB)

Nous avons défini `secondary_index_1` sur `name`, mais MySQL a créé un index composite sur (`name`, `phone_no`) où `phone_no` est la colonne de clé primaire. Nous avons créé `secondary_index_2` sur `age` et MySQL a créé un index composite sur (`age`, `phone_no`). Nous avons créé `composite_index_2` sur (`pan_no`, `name`, `age`) et MySQL a créé un index composite sur (`pan_no`, `name`, `age`, `phone_no`). L'index composite `composite_index_1` a déjà `phone_no` comme partie de celui-ci.

Ainsi, quel que soit l'index que nous créons, MySQL crée en arrière-plan un index composite de support qui, à son tour, pointe vers la clé primaire. Cela signifie que la clé primaire est un citoyen de première classe dans le monde de l'indexation MySQL. Cela prouve également que tous les index sont soutenus par une copie de l'index primaire — mais je ne suis pas sûr de savoir si une seule copie de l'index primaire est partagée ou si différentes copies sont utilisées pour différents index.

Il existe de nombreux autres index comme l'index spatial et l'index de recherche en texte intégral offerts par MySQL. Je n'ai pas encore expérimenté avec ces index, donc je ne les discute pas dans cet article.

#### Directives générales d'indexation :

* Puisque les index consomment de la mémoire supplémentaire, décidez soigneusement combien et quel type d'index suffira à vos besoins.
* Avec les opérations `DML`, les index sont mis à jour, donc les opérations d'écriture sont assez coûteuses avec les index. Plus vous avez d'index, plus le coût est élevé. Les index sont utilisés pour rendre les opérations de lecture plus rapides. Donc, si vous avez un système qui est intensif en écriture mais pas en lecture, réfléchissez bien à savoir si vous avez besoin d'un index ou non.
* La cardinalité est importante — la cardinalité signifie le nombre de valeurs distinctes dans une colonne. Si vous créez un index dans une colonne qui a une faible cardinalité, cela ne sera pas bénéfique puisque l'index devrait réduire l'espace de recherche. Une faible cardinalité ne réduit pas de manière significative l'espace de recherche.   
Exemple : si vous créez un index sur une colonne de type booléen ( `int` `1` ou `0` seulement ), l'index sera très déséquilibré puisque la cardinalité est faible (la cardinalité est de 2 ici). Mais si ce champ booléen peut être combiné avec d'autres colonnes pour produire une cardinalité élevée, optez pour cet index lorsque cela est nécessaire.
* Les index peuvent nécessiter une certaine maintenance également si les anciennes données restent dans l'index. Elles doivent être supprimées, sinon la mémoire sera monopolisée, donc essayez d'avoir un plan de surveillance pour vos index.

En fin de compte, il est extrêmement important de comprendre les différents aspects de l'indexation des bases de données. Cela aidera lors de la conception de systèmes de bas niveau. De nombreuses optimisations réelles de nos applications dépendent de la connaissance de tels détails complexes. Un index soigneusement choisi vous aidera certainement à améliorer les performances de votre application.

**_Veuillez applaudir et partager avec vos amis et sur les réseaux sociaux si vous aimez cet article. :)_**

### Références :

1. [https://dev.mysql.com/doc/refman/5.7/en/innodb-index-types.html](https://dev.mysql.com/doc/refman/5.7/en/innodb-index-types.html)
2. [https://www.quora.com/What-is-difference-between-primary-index-and-secondary-index-exactly-And-whats-advantage-of-one-over-another](https://www.quora.com/What-is-difference-between-primary-index-and-secondary-index-exactly-And-whats-advantage-of-one-over-another)
3. [https://dev.mysql.com/doc/refman/8.0/en/create-index.html](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
4. [https://www.oreilly.com/library/view/high-performance-mysql/0596003064/ch04.html](https://www.oreilly.com/library/view/high-performance-mysql/0596003064/ch04.html)
5. [http://www.unofficialmysqlguide.com/covering-indexes.html](http://www.unofficialmysqlguide.com/covering-indexes.html)
6. [https://dev.mysql.com/doc/refman/8.0/en/multiple-column-indexes.html](https://dev.mysql.com/doc/refman/8.0/en/multiple-column-indexes.html)
7. [https://dev.mysql.com/doc/refman/8.0/en/show-index.html](https://dev.mysql.com/doc/refman/8.0/en/show-index.html)
8. [https://dev.mysql.com/doc/refman/8.0/en/create-index.html](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)