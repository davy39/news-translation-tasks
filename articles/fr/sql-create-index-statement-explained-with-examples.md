---
title: Instruction SQL Create Index Expliquée avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/sql-create-index-statement-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cee740569d1a4ca34f5.jpg
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
- name: toothbrush
  slug: toothbrush
seo_title: Instruction SQL Create Index Expliquée avec des Exemples
seo_desc: 'This statement is used to create an “index” on a column in an existing
  table.

  Key points on indexes:


  They are used to improve the efficiency of searches for data, presenting the data
  in a specific order, when joining tables (see the ultimate guide t...'
---

Cette instruction est utilisée pour créer un « index » sur une colonne dans une table existante.

Points clés sur les index :

* Ils sont utilisés pour améliorer l'efficacité des recherches de données, présenter les données dans un ordre spécifique, lors de la jointure de tables (voir le [guide ultime des instructions `JOIN`](https://www.freecodecamp.org/news/the-ultimate-guide-to-sql-join-statements/)) et plus encore.
* Un index est un objet « système », ce qui signifie qu'il est utilisé par le gestionnaire de base de données.
* Une partie de cette utilisation consiste pour le gestionnaire de base de données à mettre à jour l'index lorsque les données utilisées par l'index changent dans la table associée. Gardez cela à l'esprit car, à mesure que le nombre d'index augmente dans une base de données, les performances globales du système peuvent être affectées.
* Si vous constatez que vos requêtes SQL s'exécutent lentement sur une ou plusieurs tables, la création d'un index est la première chose à considérer pour corriger le problème.

Voici un exemple de la syntaxe de l'instruction `create index`. Notez que la syntaxe permet à un index de couvrir plus d'une colonne :

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

Pour créer un nouvel index sur le champ `programOfStudy` de la table student, utilisez l'instruction suivante :

Voici une instruction pour créer l'index :

```sql
create index pStudyIndex
on student (programOfStudy);
```

Dans MySQL, vous utilisez la commande `ALTER TABLE` pour modifier et supprimer des index. MySQL Workbench fournit également des outils GUI pour gérer les index.

Mais ce n'est qu'un aperçu. Consultez la documentation de votre gestionnaire de base de données préféré et amusez-vous à essayer différentes options vous-même.