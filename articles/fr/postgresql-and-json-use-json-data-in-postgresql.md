---
title: PostgreSQL et JSON – Comment utiliser les données JSON dans PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-10T20:02:00.000Z'
originalURL: https://freecodecamp.org/news/postgresql-and-json-use-json-data-in-postgresql
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/PostgreSQL-and-JSON-Using-JSON-Data-in-PostgreSQL.jpg
tags:
- name: database
  slug: database
- name: json
  slug: json
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
seo_title: PostgreSQL et JSON – Comment utiliser les données JSON dans PostgreSQL
seo_desc: 'By Faith Oyama

  PostgreSQL is a powerful open-source relational database management system (RDBMS).
  It was initially created as a successor to the Ingres database system and was later
  named "PostgreSQL" (short for "Post-Ingres SQL").

  PostgreSQL is kno...'
---

Par Faith Oyama

PostgreSQL est un puissant système de gestion de base de données relationnelle (SGBDR) open-source. Il a été initialement créé comme successeur du système de base de données Ingres et a ensuite été nommé "PostgreSQL" (abréviation de "Post-Ingres SQL").

PostgreSQL est connu pour sa robustesse, sa fiabilité et sa scalabilité, ce qui en fait un choix populaire pour les applications de base de données grandes et complexes. Il offre des fonctionnalités avancées telles que la prise en charge de JSON et d'autres types de données non relationnelles ainsi que la prise en charge des données spatiales.

La prise en charge des fichiers JSON a été introduite pour la première fois dans PostgreSQL v9.2, et avec chaque nouvelle version, des améliorations constantes sont apportées.

Dans ce guide complet, vous apprendrez les fonctions et opérateurs JSON dans PostgreSQL. Nous aborderons également les bases du stockage des données JSON dans PostgreSQL, comment interroger les données JSON dans PostgreSQL pour les rendre facilement accessibles, et enfin, vous apprendrez à travailler avec les tableaux JSON.

## Qu'est-ce que JSON ?

JSON signifie JavaScript Object Notation. C'est une manière courante de stocker des données, en particulier dans les applications web. Il est assez similaire à HTML ou XML et a été conçu pour que les applications puissent facilement lire les fichiers JSON.

**Paires clé-valeur** : Les données JSON sont écrites en paires clé-valeur entourées de guillemets. Voici un exemple de paire clé-valeur "email" : "[jsonlearning@gmail.com](mailto:jsonlearning@gmail.com)". "Email" est ici la clé, tandis que "[jsonlearning@gmail.com](mailto:jsonlearning@gmail.com)" représente la valeur. Les deux sont séparés par un deux-points ":".

**Objets** : Un objet est une paire clé-valeur ou des paires enfermées dans des accolades. Chaque fois qu'une paire clé-valeur est enfermée dans des accolades, elle devient un objet et peut être traitée comme une seule unité. Plusieurs paires clé-valeur peuvent être ajoutées dans un objet, séparées par une virgule.

Exemple d'un objet JSON :

```
{"email" : "jsonlearning@gmail.com", 
"country" : "United Kingdom"}
```

**Tableaux** : Les tableaux en JSON sont un moyen de stocker une collection de valeurs dans un seul objet JSON. Un tableau en JSON est représenté par des crochets `[ ]` contenant une liste de valeurs séparées par des virgules.

Voici un exemple de tableau en JSON : `[ "apple",  "banana",  "cherry"]`.

Les tableaux en JSON peuvent également être imbriqués, ce qui signifie qu'un tableau peut contenir d'autres tableaux ou objets comme valeurs. Voici un exemple de tableau imbriqué :

```
{ "firstname" : "Claire", 
"location" : "United Kingdom", 
"blog" : [{ "id" : "1", 
"title" : "Welcome to my blog" }, 
{ "id" : "2", 
"title" : "My first programming language" }]}
```

Dans cet exemple de tableaux imbriqués, vous pouvez voir que "blog" est contenu dans un tableau, et le tableau contient également plusieurs objets.

## JSONB dans PostgreSQL

### Qu'est-ce que le type de données JSONB ? Et en quoi est-il différent de JSON ?

JSONB (JSON Binaire) est un type de données dans PostgreSQL qui permet de stocker et de manipuler des données JSON de manière plus efficace que le type de données JSON régulier.

JSONB stocke les données JSON dans un format binaire, ce qui permet un indexage et des performances de requête plus rapides par rapport au type de données JSON régulier. Cela est dû au fait que le format binaire permet un stockage et une récupération plus efficaces des données JSON, en particulier lors de la manipulation d'objets JSON grands ou complexes.

De plus, JSONB prend en charge des options d'indexation supplémentaires, telles que la possibilité d'indexer des clés spécifiques au sein d'un objet JSON, ce qui permet des requêtes encore plus rapides.

Le type de données JSON régulier dans PostgreSQL stocke les données JSON sous forme de texte brut, sans aucun encodage binaire ou prise en charge spéciale de l'indexation. Cela le rend plus simple à utiliser, mais peut entraîner des performances de requête plus lentes lors de la manipulation d'objets JSON grands ou complexes.

### Comment créer une table avec le type de données JSONB

Vous pouvez créer une table et donner à une colonne un type de données JSON ou JSONB, tout comme vous donnez à une colonne le type de données Int, VARCHAR ou Double. Vous pouvez simplement donner à la colonne un type de données JSON ou JSONB.

Voici un exemple de création d'une table Journal et de donner à la colonne "diary_information" le type de données JSONB.

```sql
CREATE TABLE journal (
  id Int NOT NULL PRIMARY KEY, day VARCHAR, 
  diary_information JSONB
);
```

Parce que nous avons spécifié le type de données comme étant de type JSONB, toute donnée stockée dans cette colonne doit être un JSON valide.

### Comment insérer des données JSON dans des tables

Après avoir créé une table et donné à notre colonne le type de données JSONB, comment insérons-nous des valeurs dans la colonne ? N'oubliez pas que les données doivent être dans un format JSON valide.

Pour insérer des données dans notre table, nous utilisons cette instruction :

```sql
INSERT INTO journal (id, day, diary_information) 
VALUES 
  (
    1, "Tuesday", '{"title": "My first day at work", "Feeling": "Mixed feeling"}'
  );
```

Si nous essayons de récupérer les informations en utilisant une instruction select `SELECT * FROM journal`, nous obtenons la sortie suivante, ce qui signifie que les enregistrements ont été insérés.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/select-from.png)

Dans la section suivante, nous allons examiner quelques fonctions et opérateurs.

## Aperçu des fonctions et opérateurs JSON

Les fonctions et opérateurs permettent de stocker, manipuler et interroger des données au format JSON dans PostgreSQL.

Voici quelques fonctions et opérateurs PostgreSQL couramment utilisés pour travailler avec des fichiers JSON :

* `->` : Cet opérateur permet d'extraire une valeur spécifique d'un objet JSON, vous spécifiez la clé comme un "enfant" du "parent".

Par exemple :

Pour récupérer une valeur spécifique d'un objet JSON en utilisant l'opérateur `->`, utilisez-le dans une instruction SELECT comme vu ci-dessous :

```sql
SELECT 
  Id, 
  day, 
  diary_information -> 'Feeling' AS Feeling 
FROM 
  journal;
```

Une chose à noter ici est que cet opérateur extrait le nom du champ, avec les guillemets autour.

* `->>` : Cet opérateur permet d'extraire un champ d'objet JSON sous forme de texte sans les guillemets autour de celui-ci à partir d'un objet JSON.

Par exemple :

```sql
SELECT 
  id, 
  day, 
  dairy_information ->> 'Feeling' as Feeling 
FROM 
  products;
```

Cela extraira la valeur de la clé "material" sous forme de texte à partir de la colonne "features" dans la table "products".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/material-products.png)

* `json_agg` : Cette fonction agrège les valeurs JSON dans un tableau JSON.

Par exemple, `SELECT json_agg(my_column) FROM my_table;` retournera un tableau JSON contenant les valeurs de la colonne "my_column" de la table "my_table".

* `jsonb_set` : Cette fonction met à jour un champ d'objet JSON avec une nouvelle valeur. Par exemple :

```sql
UPDATE 
  my_table 
SET 
  json_column = jsonb_set(
    json_column, '{field_name}', '"new_value"'
  ) 
WHERE 
  id = 1;
```

Pour mettre à jour un enregistrement JSON existant, nous utilisons la fonction `jsonb_set() ()` dans une instruction de mise à jour.

Par exemple, pour mettre à jour l'enregistrement dans la table que nous avons créée précédemment, vous pouvez exécuter le code suivant :

```sql
UPDATE 
  journal 
SET 
  diary_information = jsonb_set(
    diary_information, '{Feeling}', '"Excited"'
  ) 
WHERE 
  id = 1;
```

Cela mettra à jour la clé "Feeling" dans la colonne "diary_information" de la table "journal" avec la nouvelle valeur "Excited".

* `JSONB_BUILD_OBJECT` : L'insertion manuelle de valeurs JSON peut entraîner des erreurs, surtout si c'est la première fois que vous travaillez avec des données JSON. Mais avec cette fonction, vous pouvez saisir des valeurs sans avoir à vous soucier des accolades, des deux-points, etc.

Vous pouvez utiliser une fonction `JSONB_BUILD_OBJECT` pour insérer un enregistrement en texte brut et cela le convertira en données JSON. Par exemple, si vous exécutez le code :

```sql
JSONB_BUILD_OBJECT('Morning', 'Everybody is annoying today', 'Evening', 'Cannot wait to go home')
```

Cela créera une valeur qui ressemble à ceci :

```sql
{"Morning": "Everybody is annoying today", "Evening": "Cannot wait to go home"} 
```

En utilisant cette fonction dans une instruction d'insertion :

```sql
INSERT INTO journal (id, day, feeling) 
VALUES 
  (
    2, 
    'Wednesday', 
    JSONB_BUILD_OBJECT(
      'Tired', 
      'Everybody is annoying today', 
      'Hungry', 
      'Cannot wait to go home'));
```

Le nouvel enregistrement sera ajouté à la table et, parce que nous avons utilisé la fonction `JSONB_BUILD_OBJECT`, les valeurs qui suivent seront au format JSON.

Ce sont les quelques fonctions et opérateurs que nous pouvons couvrir dans cet article. Vous pouvez en lire plus sur les fonctions et opérateurs JSON dans PostgreSQL dans la documentation officielle [ici](https://www.postgresql.org/docs/9.5/functions-json.html).

## Comment travailler avec les tableaux JSON dans PostgreSQL

Dans PostgreSQL, vous pouvez stocker des données JSON comme valeur de colonne dans une table, et vous pouvez utiliser des tableaux JSON pour stocker une collection d'objets JSON dans une seule colonne.

Travailler avec des tableaux JSON dans PostgreSQL implique diverses opérations, telles que l'insertion, l'interrogation et la manipulation de données JSON. Voyons comment cela fonctionne.

### Comment insérer des tableaux JSON dans des tables

Pour insérer des tableaux JSON dans une table dans PostgreSQL, vous pouvez utiliser l'instruction INSERT INTO avec la clause VALUES pour spécifier le tableau JSON comme valeur de chaîne.

Voici un exemple :

Supposons que vous avez une table appelée employees avec des colonnes id, name et skills. La colonne skills stocke un tableau d'objets JSON représentant les compétences de chaque employé.

Pour insérer un nouvel enregistrement d'employé avec les détails suivants :

* id : 1
* name : John
* skills : [{"name": "Python", "level": "Intermediate"}, {"name": "JavaScript", "level": "Expert"}]

Vous pouvez utiliser l'instruction SQL suivante :

```sql
INSERT INTO employees (id, name, skills) 
VALUES 
  (
    1, 'John', '[{"name": "Python", "level": "Intermediate"}, {"name": "JavaScript", "level": "Expert"}]'
  );
```

### Comment interroger des tableaux JSON en utilisant des opérateurs JSON

Pour interroger des tableaux JSON dans PostgreSQL, vous pouvez utiliser les diverses fonctions et opérateurs JSON fournis par PostgreSQL. Ces fonctions permettent d'extraire des valeurs ou des éléments spécifiques du tableau JSON et d'effectuer diverses opérations sur ceux-ci. Regardons un exemple.

#### Comment extraire des valeurs d'un tableau JSON

Supposons que vous avez une table appelée employees avec une colonne skills qui stocke un tableau d'objets JSON représentant les compétences de chaque employé.

Pour extraire les noms de tous les employés qui ont "Python" comme l'une de leurs compétences, vous pouvez utiliser l'opérateur `->>` pour extraire la propriété "name" de chaque objet de compétence, et l'opérateur `@>` pour vérifier si le tableau résultant contient la valeur "Python" :

```sql
SELECT 
  name 
FROM 
  employees 
WHERE 
  skills @ > '[{"name": "Python"}]' :: jsonb
```

Ce n'est qu'un exemple des nombreuses façons dont vous pouvez interroger et manipuler des tableaux JSON en utilisant les opérateurs JSON fournis par PostgreSQL.

## Conclusion

En conclusion, la prise en charge de JSON par PostgreSQL offre aux développeurs la possibilité de simplifier les modèles de données, d'améliorer les performances des applications, et bien plus encore. Cela offre également une relation transparente entre les structures de données relationnelles et non relationnelles.

Vous avez appris les types de données JSON et JSONB, et ce que sont les paires clé-valeur, les objets et les tableaux en JSON. Vous avez également appris quelques opérateurs et fonctions dans PostgreSQL pour interroger des données au format JSON.

Si vous avez appris une ou deux choses de cet article, veuillez le partager avec d'autres.