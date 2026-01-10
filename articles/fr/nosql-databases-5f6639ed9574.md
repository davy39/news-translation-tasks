---
title: Les bases des bases de données NoSQL — et pourquoi nous en avons besoin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T18:33:53.000Z'
originalURL: https://freecodecamp.org/news/nosql-databases-5f6639ed9574
coverImage: https://cdn-media-1.freecodecamp.org/images/0*e6sondpXX3eeM_Tv
tags:
- name: database
  slug: database
- name: NoSQL
  slug: nosql
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Les bases des bases de données NoSQL — et pourquoi nous en avons besoin
seo_desc: 'By Nandhini Saravanan

  A beginner’s guide to the NoSQL world

  Organizing data is a very difficult task. When we say organise, we are actually
  categorising stuff depending on its type and function.


  _[Source](https://bitnine.net/wp-content/uploads/2016/...'
---

Par Nandhini Saravanan

#### Un guide pour débutants dans le monde NoSQL

Organiser des données est une tâche très difficile. Lorsque nous parlons d'organisation, nous catégorisons en réalité des éléments en fonction de leur type et de leur fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYo3nxIVQPPy6mPRJ-RbVw.jpeg)
_[Source](https://bitnine.net/wp-content/uploads/2016/12/SQL-vs.-NoSQL-Comparative-Advantages-and-Disadvantages.jpg" rel="noopener" target="_blank" title=")_

Une option est le SGBDR (Système de Gestion de Base de Données Relationnelle), similaire à une feuille Excel — vous catégorisez les données sous forme de tables. Vous pouvez établir des relations entre les tables.

Une **requête** interroge la base de données, qui vous retourne une réponse pertinente. Ce langage de requête est le **SQL** ou **Structured Query Language** (Langage de Requête Structuré).

Par exemple,

```
select * from Employee_Data;
```

sélectionne toutes les données des employés de la table Employee_Data.

Les bases de données relationnelles suivent un [**schéma**](https://en.wikipedia.org/wiki/Database_schema), un plan détaillé de la manière dont vos tables fonctionnent.

Vous utilisez Amazon, Facebook et de nombreuses applications de réseau. Ils publient des mises à jour, ajoutent de nouvelles fonctionnalités et même des modules supplémentaires. Comment modifier le schéma à chaque fois ? N'est-ce pas chronophage pour de si grandes entreprises de consacrer leur temps et leur main-d'œuvre à la modification du schéma ?

C'est là que **SQL ne pouvait pas fonctionner**.

### Les inconvénients des SGBDR

Les bases de données relationnelles ne sont pas aussi mauvaises que les gens le dépeignent de nos jours. Elles sont encore utilisées par de nombreuses organisations. L'introduction de NoSQL dans le paysage vise à combler les lacunes où les SGBDR ne peuvent plus être utiles.

Je vais vous montrer des exemples pour que vous ayez une compréhension claire.

#### 1. Les SGBDR ne peuvent pas gérer la 'variété de données'.

La quantité de données non structurées continue d'augmenter chaque année et leur gestion est difficile. Les SGBDR ne peuvent pas forcer tous les types de données sous un schéma unifié de tables.

Les **silos de données** sont également un problème pour les développeurs.

Selon [Tech Target](https://www.techtarget.com/), un **silo de données** est un dépôt de données qui reste sous le contrôle d'un seul département. Il est isolé du reste de l'organisation.

Cela signifie que lorsque plus de silos existent pour les mêmes données, leurs contenus sont susceptibles de différer. Cela crée une confusion sur quel dépôt représente la version la plus à jour.

L'augmentation des données de l'année 2013 à 2020 est visible dans l'image ci-dessous.

> Environ 44 zettaoctets de données seront générés en 2020.

Gérer des données aussi diverses qui ne sont pas liées les unes aux autres pourrait être beaucoup plus difficile dans les SGBDR.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JdDNyv7ujiszKRC2rsYfJw.jpeg)
_[Source](https://www.emc.com/leadership/digital-universe/2014iview/executive-summary.htm" rel="noopener" target="_blank" title=")_

**Exemple** : Il est difficile de stocker les détails d'un patient, qui a des conditions corporelles variables. La catégorisation de données aussi diverses est difficile dans les SGBDR.

#### 2. Difficile de modifier les tables et les relations.

La modification des relations entre les tables ou l'ajout d'une nouvelle table pourrait affecter les relations existantes. Cela signifie changer le schéma.

Changer le schéma serait comme éliminer celui existant et en concevoir un nouveau.

L'ajout d'une nouvelle fonctionnalité nécessiterait que tous les éléments supportent la nouvelle structure. Le changement est inévitable.

**Exemple** : Chaque colonne supplémentaire nécessite que toutes les lignes précédentes aient des valeurs pour cette colonne. Alors que dans **Cassandra** (une base de données NoSQL), vous pouvez ajouter une colonne à des partitions de lignes spécifiques.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-tu66cPX8XHUkhqQ)
_Dans les SGBDR, chaque entrée doit avoir le même nombre de colonnes. Mais dans Cassandra, chaque ligne peut avoir un nombre différent de colonnes. Comme vous pouvez le voir, 104 a seulement un nom alors que 103 a un email, un nom, un téléphone et un téléphone 2. — [Markus Klems](https://www.slideshare.net/yellow7?utm_campaign=profiletracking&amp;utm_medium=sssite&amp;utm_source=ssslideview" rel="noopener" target="_blank" title=")_

#### 3. Les SGBDR suivent les propriétés ACID de la base de données.

Les propriétés ACID d'une base de données sont l'atomicité, la cohérence, l'isolation et la durabilité.

**Atomicité** — Une approche "tout ou rien". Si une instruction de la transaction échoue, toute la transaction est annulée.

**Cohérence** — La transaction doit respecter tous les protocoles définis par le système. Pas de transactions à moitié complétées.

**Isolation** — Aucune transaction n'a accès à une autre transaction qui est dans un état intermédiaire ou inachevé. Chaque transaction est indépendante.

**Durabilité** — Garantit que, une fois qu'une transaction est validée dans la base de données, elle est préservée grâce à l'utilisation de sauvegardes et de journaux de transactions.

Les propriétés ACID ne sont pas flexibles.

Par exemple, les SGBDR suivent la [**normalisation**](https://en.wikipedia.org/wiki/Database_normalization) ou un concept de **"single point of truth"** (source unique de vérité). Pour chaque changement que vous faites, vous devez garantir des propriétés ACID strictes. Les règles d'[intégrité des entités](https://en.wikipedia.org/wiki/Entity_integrity) et d'[intégrité référentielle](https://en.wikipedia.org/wiki/Referential_integrity) s'appliquent également.

### Le théorème CAP

Selon [Wikipedia](https://en.wikipedia.org/wiki/CAP_theorem), le **théorème CAP** (théorème de Brewer) stipule qu'il est impossible pour un magasin de données distribué de **fournir simultanément plus de deux** des trois garanties suivantes :

**Cohérence** : Comme le C dans ACID.

**Disponibilité** : Les ressources doivent toujours être disponibles. Il doit y avoir une réponse sans erreur.

**Tolérance aux partitions** : Aucun point unique (ou nœud) de défaillance.

Il est difficile de satisfaire les trois conditions. Il faut faire un compromis entre les trois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DXG4bVXnJ6xhHbJe6SmkFA.png)
_[Source](https://www.dummies.com/wp-content/uploads/423504.image0.jpg" rel="noopener" target="_blank" title=")_

### BASE à la rescousse !

NoSQL repose sur un modèle plus souple connu sous le nom de modèle BASE. **BASE** (**B**asically **A**vailable, **S**oft state, **E**ventual consistency).

**Basically Available** : Garantit la disponibilité des données. Il y aura une réponse à toute requête (peut être un échec également).

**Soft state** : L'état du système pourrait changer avec le temps.

**Eventual consistency** : Le système deviendra finalement cohérent une fois qu'il cessera de recevoir des entrées.

Les bases de données NoSQL abandonnent les exigences A, C et/ou D, et en retour, elles améliorent la scalabilité.

### NoSQL

C'est là que NoSQL est venu à la rescousse. C'est "**Not Only SQL**" ou "Non relationnel".

Caractéristiques de NoSQL :

* Sans schéma
* Cohérence éventuelle (comme dans la propriété BASE)
* Réplication des magasins de données pour éviter un point unique de défaillance.
* Peut gérer la variété de données et de grandes quantités de données.

### Types de bases de données NoSQL

Les bases de données NoSQL se divisent en quatre catégories principales :

**Magasins clé-valeur** — Riak, Voldemort et Redis

**Magasins à colonnes larges** — Cassandra et HBase.

**Bases de données documentaires** — MongoDB

**Bases de données de graphes** — Neo4J et HyperGraphDB.

Les mots à droite sont des exemples des types de bases de données NoSQL.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k7VI_3bUow1CvXHxSBKaww.jpeg)
_[Source](https://s3.amazonaws.com/dev.assets.neo4j.com/wp-content/uploads/nosql-quadrant.jpg" rel="noopener" target="_blank" title=")_

### 1. **Magasins clé-valeur**

Un magasin clé-valeur utilise une **table de hachage** dans laquelle il existe une **clé unique** et un **pointeur** vers un élément de données particulier.

Imaginez les magasins clé-valeur comme un annuaire téléphonique où les noms des individus et leurs numéros sont associés.

Les magasins clé-valeur n'ont pas de langage de requête par défaut. Vous récupérez les données en utilisant les commandes _get, put et delete_. C'est la raison pour laquelle ils ont une **haute performance**.

**Applications** : Utile pour le stockage des commentaires et des informations de session. Pinterest utilise Redis pour stocker des listes d'utilisateurs, de followers, de non-followers, de tableaux.

### **2. Magasins à colonnes larges**

Dans une base de données à colonnes, les colonnes de chaque ligne sont contenues dans cette ligne.

Chaque **famille de colonnes** est un conteneur de lignes dans une table SGBDR. La **clé** identifie la ligne composée de plusieurs colonnes.

Les lignes n'ont pas besoin d'avoir le **même nombre** de colonnes. Des colonnes peuvent être ajoutées à n'importe quelle ligne à n'importe quel moment sans avoir à les ajouter à d'autres lignes. C'est un **magasin de lignes partitionnées**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wJdqYEIbxD63059_UNWUYA.png)
_[Source](https://studio3t.com/wp-content/uploads/2017/12/cassandra-column-family-example.png" rel="noopener" target="_blank" title=")_

#### **Comment une base de données colonnaire stocke-t-elle les données ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*p9QNl8LCMfluRlqq7SmV4g.png)
_Comment les magasins colonnaires stockent les données_

**Applications** : [**Spotify**](https://www.spotify.com/) utilise Cassandra pour stocker les attributs de profil des utilisateurs et les métadonnées.

### **3. Bases de données documentaires**

Les bases de données documentaires utilisent des documents JSON, XML ou BSON (encodage binaire de JSON) pour stocker les données.

C'est comme une base de données clé-valeur, mais une base de données documentaire contient des **données semi-structurées**.

Un seul document sert à stocker des enregistrements et leurs données.

Elle **ne supporte pas les relations ou les jointures**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*65P8gE1JkCGgZDHWhVt3gg.png)
_Un exemple de document JSON — [Source](https://webassets.mongodb.com/_com_assets/cms/JSON_Example_Python_MongoDB-mzqqz0keng.png" rel="noopener" target="_blank" title=")_

Si nous voulons stocker les détails des clients et leurs commandes, nous pouvons utiliser des bases de données documentaires pour le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MrhoMn_ewuvDcbOO.png)
_La base de données des clients est stockée sous forme d'un ensemble de documents (peut être JSON) qui est mappé à la base de données des commandes. Source : [Blog MSDN Microsoft](https://blogs.msdn.microsoft.com/usisvde/2012/04/05/getting-acquainted-with-nosql-on-windows-azure/" rel="noopener" target="_blank" title=")_

Applications : [**SEGA**](https://www.sega.com/games) utilise MongoDB pour gérer 11 millions de comptes de jeu construits sur MongoDB.

### **4. Bases de données de graphes**

Les nœuds et les relations sont les constituants essentiels des bases de données de graphes. Un **nœud représente une entité**. Une **relation** représente comment deux nœuds sont associés.

Dans les SGBDR, l'ajout d'une autre relation entraîne de nombreux changements de schéma.

Une base de données de graphes nécessite seulement de stocker les données une fois (nœuds). Les différents types de relations (arêtes) sont spécifiés pour les données stockées.

Les relations entre les nœuds sont prédéterminées, c'est-à-dire qu'elles ne sont pas déterminées au moment de la requête.

Parcourir des **relations persistantes** est plus rapide.

Il est difficile de changer une relation entre deux nœuds. Cela entraînerait des changements régressifs dans la base de données.

**Exemple** : Cette image montre comment **MySQL** fonctionne où il doit effectuer de nombreuses opérations pour trouver un résultat correct pour Alice.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0MjP3w9EuC6AK6JOt2FsoA.png)
_[Source](https://s3.amazonaws.com/dev.assets.neo4j.com/wp-content/uploads/from_relational_model.png" rel="noopener" target="_blank" title=")_

Une **base de données de graphes**, qui **prédétermine les relations**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q2s8IGzh-dF-A_qE5HCT5g.png)
_[Source](https://s3.amazonaws.com/dev.assets.neo4j.com/wp-content/uploads/relational_to_graph.png" rel="noopener" target="_blank" title=")_

Ce sont quelques-unes des informations de base dont vous aurez besoin pour commencer à explorer NoSQL. De nouvelles bases de données sont inventées pour des usages spécifiques.

Apprenez le type de données que votre application génère, et il sera alors facile de choisir la bonne base de données.

#### J'écris des articles sur les leçons de vie, la programmation et la technologie. Pour en lire plus, suivez-moi sur [Twitter](https://twitter.com/snandhini98) et [Medium](http://medium.com/@nandhus05).