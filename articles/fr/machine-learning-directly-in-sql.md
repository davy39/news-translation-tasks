---
title: Apprentissage automatique directement en SQL – Comment utiliser le ML dans
  les bases de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-12T16:10:22.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-directly-in-sql
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605de0b79618b008528a7b35.jpg
tags:
- name: algorithms
  slug: algorithms
- name: database
  slug: database
- name: Machine Learning
  slug: machine-learning
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
seo_title: Apprentissage automatique directement en SQL – Comment utiliser le ML dans
  les bases de données
seo_desc: 'By Peter Gleeson

  Machine learning need not be mysterious. A lot of the basics come wrapped up in
  high-level software packages such as scikit-learn, but you can actually do a lot
  without ever having to leave the database.

  PostgreSQL lets you build que...'
---

Par Peter Gleeson

L'apprentissage automatique n'a pas besoin d'être mystérieux. Beaucoup des bases sont intégrées dans des packages logiciels de haut niveau tels que [scikit-learn](https://scikit-learn.org/), mais vous pouvez en fait faire beaucoup sans jamais avoir à quitter la base de données.

[PostgreSQL](https://www.postgresql.org/) vous permet de construire des requêtes qui exécutent une variété d'algorithmes d'apprentissage automatique sur vos données.

Ici, je démontre quatre algorithmes populaires d'apprentissage automatique écrits entièrement en SQL.

Je présenterai ces requêtes de manière à permettre une exposition facile, mais elles ne sont pas destinées à être utilisées dans un environnement de production.

Quoi qu'il en soit, travailler avec eux est un excellent moyen de tester vos connaissances en apprentissage automatique et en SQL, ainsi qu'en résolution de problèmes - des compétences essentielles pour tout scientifique des données.

## Régression linéaire

La régression linéaire est peut-être l'exemple le plus élémentaire de l'apprentissage automatique. L'objectif est d'« apprendre » les paramètres `m` et `c` d'une équation linéaire de la forme `y = mx + c` à partir d'un ensemble de données d'entraînement.

C'est un excellent exemple des [fonctions statistiques](https://www.postgresql.org/docs/13/functions-aggregate.html) intégrées à PostgreSQL.

Les données d'entrée sont dans une table avec deux colonnes :

`x | y`

Certaines valeurs de `y` sont définies sur NULL. Le but est de prédire ces valeurs manquantes.

```sql
WITH regression AS
  (SELECT 
      regr_slope(y, x) AS gradient,
      regr_intercept(y, x) AS intercept
   FROM
      linear_regression
   WHERE
      y IS NOT NULL
   )

SELECT
   x,
   (x * gradient) + intercept AS prediction
FROM
   linear_regression
CROSS JOIN
   regression
WHERE
   y IS NULL ;
```

Les fonctions `regr_slope()` et `regr_intercept()` sont utilisées pour estimer respectivement les termes de gradient et d'interception. Ceux-ci correspondent aux paramètres `m` et `c` dans l'équation.

La sortie sera tous les points inconnus, avec une valeur prédite pour `y` basée sur la valeur de `x`.

![nuage de points montrant une relation linéaire entre les variables x et y. les valeurs prédites sont montrées en bleu, les valeurs connues en rouge](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1f34db45-f083-4a8c-be24-2cc252910eac_1448x776.png)

## K-Nearest Neighbours

[K-nearest neighbours](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) est un exemple classique d'algorithme de classification supervisée. Le principe est assez simple. Chaque point de données est représenté comme un point dans l'espace, étiqueté comme l'une des nombreuses catégories ou classes.

Pour classer un point de données non étiqueté, il suffit de regarder les étiquettes des points les plus proches de celui-ci. L'étiquette qui apparaît le plus fréquemment est utilisée comme estimation.

Le nombre de points voisins considérés est déterminé par un paramètre `K`.

Ici, les données d'entrée sont une table avec les colonnes suivantes :

`id | x_loc | y_loc | category`

Certaines des valeurs dans la colonne `category` sont NULL. Le but est de classer celles-ci en utilisant l'algorithme des K-plus proches voisins.

```
-- CTE pour obtenir les données d'entraînement étiquetées
WITH training AS
  (SELECT
      id,
      POINT(x_loc, y_loc) as xy,
      category
  FROM
      k_nearest
  WHERE
      category IS NOT NULL
  ),

-- CTE pour obtenir les points non étiquetés
test AS
  (SELECT
      id,
      POINT(x_loc, y_loc) as xy,
      category
  FROM
      k_nearest
  WHERE
      category IS NULL
  ),

-- calculer les distances entre les points non étiquetés et étiquetés
distances AS
  (SELECT
      test.id,
      training.category,
      test.xy <-> training.xy AS dist,
      ROW_NUMBER() OVER (
         PARTITION BY test.id
         ORDER BY test.xy <-> training.xy 
         ) AS row_no
  FROM
      test
  CROSS JOIN training
  ORDER BY 1, 4 ASC
  ),

-- compter les "votes" par étiquette pour chaque point non étiqueté
votes AS
  (SELECT
      id,
      category,
      count(*) AS votes
  FROM distances
  WHERE row_no <= {{K}}
  GROUP BY 1,2
  ORDER BY 1)

-- requête pour l'étiquette avec le plus de votes
SELECT
  v.id,
  v.category
FROM
  votes v
JOIN
  (SELECT
      id,
      max(votes) AS max_votes
  FROM
      votes
  GROUP BY 1
  ) mv 
ON v.id = mv.id
AND v.votes = mv.max_votes
ORDER BY 1 ASC ;
```

Dans la requête ci-dessus, le paramètre `K` est écrit comme une variable `{{K}}`. Si vous utilisez un outil tel que [Metabase](https://www.metabase.com/start/oss/), vous pouvez entrer différentes valeurs de `K` et voir quel effet elles ont.

La requête utilise le type de données `POINT()` de PostgreSQL et l'opérateur de distance pour calculer les distances entre les données.

La sortie sera chacun des points non étiquetés, ainsi que la classe estimée.

![nuage de points de 2 groupes de points, colorés en bleu et rouge respectivement](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4d186029-9149-4060-851a-c2ba5e976f20_2872x1456.png)

## Classification Naive Bayes

La [classification Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) est une technique utilisée pour des tâches de classification variées, allant de la détection de spam à la classification de documents et à l'analyse de sentiments.

Elle fonctionne en utilisant la [règle de Bayes](https://www.freecodecamp.org/news/p/885a763e-a3d5-473a-a951-2c5fdd2abcda/) pour relier la « probabilité de la classe, étant donné les données » à la « probabilité des données, étant donné la classe ». Cette dernière peut être facilement estimée à partir d'un ensemble de données d'entraînement étiquetées.

La requête ci-dessous prend en entrée une table avec les colonnes suivantes :

`id | record | category`

Ici, `record` est un morceau de texte (par exemple, la ligne d'objet d'un email) et `category` est l'une des plusieurs classes possibles (par exemple, spam ou non spam).

Pour certaines lignes, `category` est défini sur NULL. Le but est d'estimer les catégories manquantes en utilisant la classification Naive Bayes.

```sql
-- CTE pour créer une ligne par mot
WITH staging AS
  (SELECT 
      REGEXP_SPLIT_TO_TABLE(
         LOWER(record), '[^a-z]+') AS word,
      category
   FROM
      naive_bayes
   WHERE
      category IS NOT NULL
  ),

-- données de test
test AS
  (SELECT
      id,
      record
   FROM
      naive_bayes
   WHERE
      category is NULL
  ),
          
-- une ligne par mot + catégorie
cartesian AS
  (SELECT
      *
   FROM
     (SELECT
         DISTINCT word
      FROM
         staging) w
      CROSS JOIN
     (SELECT
         DISTINCT category
      FROM
         staging) c
      WHERE
         length(word) > 0
   ),

-- CTE des fréquences lissées de chaque mot par catégorie
frequencies AS
  (SELECT
      c.word,
      c.category,
      -- numérateur plus un
      (SELECT
          count(*)+1
       FROM
          staging s
       WHERE
          s.word = c.word
       AND
          s.category = c.category) /
      -- dénominateur plus deux
      (SELECT
          count(*)+2
       FROM
          staging s1
       WHERE
          s1.category = c.category) ::DECIMAL AS freq
   FROM
      cartesian c
   ),

-- pour chaque ligne dans le test, obtenir les probabilités   
probabilities AS
  (SELECT
      t.id,
      f.category,
      SUM(LN(f.freq)) AS probability
   FROM
     (SELECT
         id,
         REGEXP_SPLIT_TO_TABLE(
            LOWER(record), '[^a-z]+') AS word
      FROM
         test) t
   JOIN
     (SELECT
         word,
         category,
         freq
      FROM
         frequencies) f 
   ON t.word = f.word
   GROUP BY 1, 2
  )

-- garder seulement l'estimation la plus élevée            
SELECT
   record,
   probabilities.category
FROM
   probabilities
JOIN
  (SELECT
      id,
      max(probability) AS max_probability
   FROM
      probabilities
   GROUP BY 1) p
ON probabilities.id = p.id
AND probabilities.probability = p.max_probability
JOIN
   test
ON probabilities.id = test.id
ORDER BY 1 ;
```

La sortie est chacun des enregistrements non classés, avec une catégorie prédite assignée.

La requête ci-dessus fait quelques simplifications. Pour commencer, le seul prétraitement des données textuelles est une simple [expression régulière](https://www.postgresql.org/docs/13/functions-matching.html#FUNCTIONS-POSIX-REGEXP) pour garder les lettres A-Z, et l'utilisation de la fonction `LOWER()` pour tout convertir en minuscules.

Elle suppose également une probabilité a priori uniforme pour chacune des classes (en d'autres termes, l'hypothèse est que, avant de regarder les données, les emails spam et non-spam sont également probables).

![exemple de sortie montrant des lignes d'objet d'email telles que vous avez gagné un prix en espèces, réclamez votre compensation maintenant, slim fast avec le nouveau régime insensé classées comme spam, et des lignes d'objet telles que réunion d'équipe reportée, atelier stratégique et calendrier du comité pour le prochain trimestre classées comme non spam](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2801278-ee24-4726-9248-1644c4ed4866_1190x792.png)

## Clustering K-means

Le [clustering K-means](https://en.wikipedia.org/wiki/K-means_clustering) est un algorithme de classification bien connu. Il s'agit d'un [algorithme non supervisé](https://en.wikipedia.org/wiki/Unsupervised_learning), ce qui signifie qu'il ne nécessite aucune donnée d'entraînement étiquetée.

Le clustering K-means fonctionne en représentant chaque point de données comme un point dans l'espace. Chaque point est initialement assigné aléatoirement à l'un des `K` clusters (où `K` est un paramètre choisi à l'avance).

Ensuite, l'emplacement moyen des points est calculé pour chaque cluster.

Puis, chaque point est réassigné au cluster avec l'emplacement moyen le plus proche.

Ces deux étapes sont répétées encore et encore jusqu'à ce que les points ne soient plus réassignés entre les étapes.

Les données d'entrée sont une table avec les colonnes suivantes :

`id | x_loc | y_loc`

La sortie est l'ensemble complet de points, chacun assigné à l'un des `K` clusters.

Celui-ci était difficile à implémenter. La solution ci-dessous est largement basée sur une généralisation de [cet exemple de données d'achat](https://github.com/decibel/examples) créé par Jim Nasby sous une [licence BSD 2-clause](https://github.com/decibel/examples/blob/master/LICENSE) (qui s'applique ci-dessous).

```sql
WITH points AS
   (SELECT
       id,
       POINT(x_loc, y_loc) AS xy
    FROM
       k_means_clustering
    ),

initial AS
   (SELECT 
       RANK() OVER (
          ORDER BY random() 
       ) AS cluster,
       xy
    FROM points 
    LIMIT {{K}}
    ),

iteration AS
   (WITH RECURSIVE kmeans(iter, id, cluster, avg_point) AS (
       SELECT
          1,
          NULL::INTEGER,
          *
        FROM 
           initial
        UNION ALL
        SELECT
           iter + 1,
           id,
           cluster,
           midpoint
        FROM (
           SELECT DISTINCT ON(iter, id)
              *
           FROM (
              SELECT
                 iter,
                 cluster,
                 p.id, 
                 p.xy <-> k.avg_point AS distance,
                 @@ LSEG(p.xy, k.avg_point) AS midpoint,
                 p.xy,
                 k.avg_point
               FROM points p
               CROSS JOIN kmeans k
               ) d
            ORDER BY 1, 3, 4
            ) r
       WHERE iter < {{max_iter}}
   )
   SELECT
      *
   FROM
      kmeans
   )

SELECT
   k.*,
   cluster
FROM
   iteration i
JOIN
   k_means_clustering k
USING(id)
WHERE
   iter = {{max_iter}}
ORDER BY 4,1 ASC ;
```

Cette requête utilise quelques fonctionnalités intéressantes.

Tout d'abord, elle utilise les [types de données géométriques](https://www.postgresql.org/docs/13/datatype-geometric.html) et les [opérateurs](https://www.postgresql.org/docs/13/functions-geometry.html) de PostgreSQL pour modéliser les données en termes de points et de segments de ligne.

Elle utilise également une [requête récursive](https://www.postgresql.org/docs/13/queries-with.html) pour recalculer de manière itérative les centres de chaque cluster jusqu'à un nombre maximum d'itérations.

Cette implémentation utilise un nombre prédéterminé d'itérations avant de terminer, plutôt que de s'arrêter une fois que les points cessent d'être réassignés entre les itérations.

Si vous utilisez un outil tel que Metabase, vous pouvez définir les paramètres `K` et le nombre maximum d'itérations dynamiquement en utilisant les variables `{{K}}` et `{{max_iter}}`.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F164a13dc-c2c6-4339-8021-83d77332c226_1442x640.png)

## Résumé

SQL est un langage puissant capable de bien plus que simplement stocker et charger des données dans des bases de données.

C'est un langage déclaratif, donc vous devez décrire le résultat que vous recherchez (par opposition à un langage impératif, où vous donnez des instructions à l'ordinateur étape par étape).

Cela nécessite de penser aux problèmes d'apprentissage automatique d'une manière différente, mais il est toujours possible d'obtenir des résultats intéressants.

Toutes les données d'exemple et les requêtes utilisées dans cet article peuvent être trouvées [ici](https://github.com/pg0408/sql-machine-learning).

Si vous avez aimé cet article, vous pourriez également être intéressé par [Apprenez ces astuces rapides dans PostgreSQL](https://www.freecodecamp.org/news/postgresql-tricks/) et [Comment utiliser la correspondance floue de chaînes avec PostgreSQL](https://www.freecodecamp.org/news/fuzzy-string-matching-with-postgresql/).

Vous pouvez suivre plus de mes écrits sur [gleeson.substack.com](https://gleeson.substack.com/)