---
title: Qu'est-ce qu'un ORM – La signification des outils de mappage objet-relationnel
  de base de données
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-10-21T18:18:25.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/markus-winkler-gLdJnQFcIXE-unsplash.jpg
tags:
- name: database
  slug: database
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: SQL
  slug: sql
seo_title: Qu'est-ce qu'un ORM – La signification des outils de mappage objet-relationnel
  de base de données
seo_desc: 'Object Relational Mapping (ORM) is a technique used in creating a "bridge"
  between object-oriented programs and, in most cases, relational databases.

  Put another way, you can see the ORM as the layer that connects object oriented
  programming (OOP) to...'
---

Le mappage objet-relationnel (ORM) est une technique utilisée pour créer un "pont" entre les programmes orientés objet et, dans la plupart des cas, les [bases de données relationnelles](https://www.freecodecamp.org/news/what-is-a-relational-database-rdbms-definition/).

En d'autres termes, vous pouvez voir l'ORM comme la couche qui connecte la [programmation orientée objet](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/) (OOP) aux bases de données relationnelles.

Lors de l'interaction avec une base de données en utilisant des langages OOP, vous devrez effectuer différentes opérations comme la création, la lecture, la mise à jour et la suppression (CRUD) de données dans une base de données. Par conception, vous utilisez SQL pour effectuer ces opérations dans les bases de données relationnelles.

Bien que l'utilisation de SQL à cette fin ne soit pas nécessairement une mauvaise idée, l'ORM et les outils ORM aident à simplifier l'interaction entre les bases de données relationnelles et les différents langages OOP.

## Qu'est-ce qu'un outil ORM ?

Un outil ORM est un logiciel conçu pour aider les développeurs OOP à interagir avec les bases de données relationnelles. Ainsi, au lieu de créer votre propre logiciel ORM à partir de zéro, vous pouvez utiliser ces outils.

Voici un exemple de code SQL qui récupère des informations sur un utilisateur particulier dans une base de données :

```sql
"SELECT id, name, email, country, phone_number FROM users WHERE id = 20"
```

Le code ci-dessus retourne des informations sur un utilisateur — `name`, `email`, `country`, et `phone_number` — à partir d'une table appelée `users`. En utilisant la clause `WHERE`, nous avons spécifié que les informations doivent provenir d'un utilisateur avec un `id` de 20.

D'autre part, un outil ORM peut effectuer la même requête que ci-dessus avec des méthodes plus simples. C'est-à-dire :

```
users.GetById(20)
```

Ainsi, le code ci-dessus fait la même chose que la requête SQL. Notez que chaque outil ORM est construit différemment, donc les méthodes ne sont jamais les mêmes, mais le but général est similaire.

Les outils ORM peuvent générer des méthodes comme celle du dernier exemple.

La plupart des langages OOP disposent d'une variété d'outils ORM parmi lesquels vous pouvez choisir. Voici quelques-uns des plus populaires pour le développement Java, Python, PHP et .NET :

### Outils ORM populaires pour Java

#### 1. Hibernate

[Hibernate](https://hibernate.org/orm/) permet aux développeurs d'écrire des classes de persistance de données en suivant des concepts OOP comme l'héritage, le polymorphisme, l'association, la composition. Hibernate est très performant et également scalable.

#### 2. Apache OpenJPA

[Apache OpenJPA](https://openjpa.apache.org/) est également un outil de persistance Java. Il peut être utilisé comme une couche de persistance **POJO** (plain old Java object) autonome.

#### 3. EclipseLink

[EclipseLink](https://www.eclipse.org/eclipselink/) est une solution de persistance Java open source pour les services web relationnels, XML et de base de données.

#### 4. jOOQ

[jOOQ](https://www.jooq.org/) génère du code Java à partir de données stockées dans une base de données. Vous pouvez également utiliser cet outil pour construire des requêtes SQL sûres en termes de typage.

#### 5. Oracle TopLink

Vous pouvez utiliser [Oracle TopLink](https://docs.oracle.com/cd/E17904_01/web.1111/b32441/undtl.htm#JITDG91126) pour construire des applications haute performance qui stockent des données persistantes. Les données peuvent être transformées en données relationnelles ou en éléments XML.

### Outils ORM populaires pour Python

#### 1. Django

[Django](https://docs.djangoproject.com/en/4.1/topics/db/queries/) est un excellent outil pour construire rapidement des applications web.

#### 2. web2py

[web2py](http://www.web2py.com/init/default/index) est un framework full-stack Python open source pour construire des applications web rapides, scalables, sécurisées et pilotées par les données.

#### 3. SQLObject

[SQLObject](http://www.sqlobject.org/) est un gestionnaire objet-relationnel qui fournit une interface objet à votre base de données.

#### 4. SQLAlchemy

[SQLAlchemy](https://www.sqlalchemy.org/) fournit des modèles de persistance conçus pour un accès efficace et performant aux bases de données.

### Outils ORM populaires pour PHP

#### 1. Laravel

[Laravel](https://laravel.com/docs/9.x/eloquent) est livré avec un gestionnaire objet-relationnel appelé Eloquent qui facilite l'interaction avec les bases de données.

#### 2. CakePHP

[CakePHP](https://book.cakephp.org/4/en/orm.html) fournit deux types d'objets : les dépôts qui vous donnent accès à une collection de données et les entités qui représentent des enregistrements individuels de données.

#### 3. Qcodo

[Qcodo](https://github.com/qcodo/qcodo) fournit différentes commandes qui peuvent être exécutées dans le terminal pour interagir avec les bases de données.

#### 4. RedBeanPHP

[RedBeanPHP](https://redbeanphp.com/index.php) est un mapper objet-relationnel sans configuration.

### Outils ORM populaires pour .NET

#### 1. Entity Framework

[Entity Framework](https://learn.microsoft.com/en-us/ef/) est un mapper objet-base de données multi-base de données. Il supporte SQL, SQLite, MySQL, PostgreSQL et Azure Cosmos DB.

#### 2. NHibernate

[NHibernate](https://nhibernate.info/) est un mapper objet-relationnel open source avec des tonnes de plugins et d'outils pour rendre le développement plus facile et plus rapide.

#### 3. Dapper

[Dapper](https://www.learndapper.com/) est un micro-ORM. Il est principalement utilisé pour mapper des requêtes à des objets. Cet outil ne fait pas la plupart des choses qu'un outil ORM ferait comme la génération de SQL, la mise en cache des résultats, le chargement paresseux, etc.

#### 4. Base One Foundation Component Library (BFC)

[BFC](http://www.boic.com/b1mspecsheet.htm) est un framework pour créer des applications de base de données en réseau avec Visual Studio et des logiciels DBMS de Microsoft, Oracle, IBM, Sybase et MySQL.

Vous pouvez voir plus d'outils ORM [ici](https://en.wikipedia.org/wiki/List_of_object%E2%80%93relational_mapping_software).

Maintenant, discutons de certains des avantages et inconvénients de l'utilisation des outils ORM.

## Avantages de l'utilisation des outils ORM

Voici quelques-uns des avantages de l'utilisation d'un outil ORM :

* Il accélère le temps de développement pour les équipes.
* Réduit le coût de développement.
* Gère la logique nécessaire pour interagir avec les bases de données.
* Améliore la sécurité. Les outils ORM sont conçus pour éliminer la possibilité d'attaques par injection SQL.
* Vous écrivez moins de code en utilisant des outils ORM qu'avec SQL.

## Inconvénients de l'utilisation des outils ORM

* Apprendre à utiliser les outils ORM peut être chronophage.
* Ils ne performeront probablement pas mieux lorsque des requêtes très complexes sont impliquées.
* Les ORM sont généralement plus lents que l'utilisation de SQL.

## Résumé

Dans cet article, nous avons parlé du mappage objet-relationnel. Il s'agit d'une technique utilisée pour connecter les programmes orientés objet aux bases de données relationnelles.

Nous avons listé certains des outils ORM populaires pour différents langages de programmation.

Nous avons conclu avec certains des avantages et inconvénients de l'utilisation des outils ORM.

Bon codage !