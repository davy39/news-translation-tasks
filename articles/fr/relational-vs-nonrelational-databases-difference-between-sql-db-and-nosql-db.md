---
title: Bases de données relationnelles VS non relationnelles – la différence entre
  une base de données SQL et une base de données NoSQL
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-04-18T17:56:26.000Z'
originalURL: https://freecodecamp.org/news/relational-vs-nonrelational-databases-difference-between-sql-db-and-nosql-db
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/valeriia-svitlini-5w0ZbF8P5-4-unsplash.jpg
tags:
- name: database
  slug: database
- name: NoSQL
  slug: nosql
- name: SQL
  slug: sql
seo_title: Bases de données relationnelles VS non relationnelles – la différence entre
  une base de données SQL et une base de données NoSQL
seo_desc: "This article is an overview of relational and non-relational databases.\
  \ \nBesides learning the fundamental differences between the two types of databases,\
  \ you will also learn how to decide which one to use for your next project by going\
  \ over their str..."
---

Cet article est un aperçu des bases de données relationnelles et non relationnelles. 

En plus d'apprendre les différences fondamentales entre les deux types de bases de données, vous apprendrez également comment décider laquelle utiliser pour votre prochain projet en passant en revue leurs forces et leurs faiblesses. 

Voici ce que nous allons couvrir :

1. [Définition d'une base de données](#definition)
    1. [Qu'est-ce que SQL ?](#sql)
2. [Bases de données relationnelles](#relational)
    1. [Caractéristiques](#caracteristiques)
    2. [Propriétés ACID](#acid)
3. [Bases de données non relationnelles](#non-relational)
    1. [Types](#types)
    2. [Propriétés BASE](#base)
4. [Bases de données relationnelles VS non relationnelles](#pick)
5. [Apprentissage supplémentaire](#extra)

## Qu'est-ce qu'une base de données ? Une définition pour les débutants <a name="definition"></a>

En informatique, les données sont des morceaux d'information qui se présentent sous différentes formes. Les données peuvent être du texte, des nombres, des images, des extraits audio ou des vidéos. 

Les collections d'informations doivent être stockées quelque part, traitées et interprétées. 

Vous avez besoin d'un moyen de rechercher, d'accéder, d'extraire et de récupérer les ressources enregistrées facilement chaque fois que vous en avez besoin. 

Cela permet aux ordinateurs et aux humains d'analyser les données accessibles, d'effectuer des calculs et des comparaisons, de prendre des décisions logiques et d'aboutir à une conclusion.

Vous pouvez stocker les données dans un fichier de quelque sorte, en utilisant un programme logiciel comme une feuille de calcul Excel – et cela peut faire le travail.

Mais que se passe-t-il s'il y a de grandes quantités de données, et que vous devez être sûr qu'elles sont exactes ? 

Ou que se passe-t-il si vous devez récupérer de grands ensembles de données rapidement ?  

Ou que se passe-t-il si les données doivent avoir une structure prédéfinie à laquelle elles doivent adhérer ?

Les bases de données sont un moyen beaucoup plus accessible, efficace et organisé de stocker et de travailler avec des informations sur une longue période.

La capacité de stocker des données de manière logique et systématique et de les récupérer pour une utilisation ultérieure fait des bases de données une partie critique de toutes les applications web.

Les bases de données alimentent toutes les applications. Elles enregistrent et stockent les informations des utilisateurs telles que les noms d'utilisateur, les adresses e-mail, les mots de passe chiffrés et les adresses physiques. 

Elles stockent également le comportement des utilisateurs. Par exemple, dans un magasin de commerce électronique, la base de données enregistre et suit les articles que vous avez marqués comme 'favoris'.

Vous aurez besoin d'un **Système de Gestion de Base de Données** (ou SGBD en abrégé) pour gérer vos bases de données.

Un Système de Gestion de Base de Données est un programme logiciel qui sert d'intermédiaire entre les utilisateurs finaux et la base de données elle-même.

Il permet à ses utilisateurs de créer et de gérer des bases de données. Il leur permet également d'accéder, de modifier et de manipuler les données stockées dans la base de données en effectuant des opérations connues sous le nom de requêtes. 

Les utilisateurs peuvent facilement stocker, récupérer, mettre à jour et supprimer des données à l'aide de quelques commandes.

En ce qui concerne les Systèmes de Gestion de Base de Données, il existe généralement **deux** types parmi lesquels choisir :

- **Bases de données relationnelles** (également connues sous le nom de **bases de données SQL**)
- **Bases de données non relationnelles** (également connues sous le nom de **bases de données NoSQL**)

### Qu'est-ce que SQL ? <a name="sql"></a>

SQL est l'abréviation de **S**tructured **Q**uery **L**anguage. 

Vous l'entendrez probablement prononcer de deux manières différentes – "*S. Q. L.*" (ess-kew-ell), ou "*se-quel*" (comme une suite à un film).


![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-13-at-6.25.32-PM.png)
_https://i.imgur.com/NtGaNA8.png_

Dans tous les cas, SQL est un langage utilisé pour traiter les bases de données. 

Plus précisément, avec SQL, vous pouvez écrire des requêtes de base de données pour communiquer avec la base de données. Celles-ci peuvent être des commandes pour effectuer l'une des opérations CRUD (Create Read Update Delete).

SQL est le langage de choix pour les Systèmes de Gestion de Base de Données Relationnelles, que vous apprendrez en détail dans la section suivante.

## Qu'est-ce qu'une base de données relationnelle ? <a name="relational"></a>

Les bases de données relationnelles (ou bases de données SQL) existent depuis un certain temps. La première base de données relationnelle est apparue en 1970, et elles sont toujours populaires aujourd'hui. Certaines des plus couramment utilisées sont :

- [PostgreSQL](https://www.postgresql.org/)  
- [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- [MySQL](https://www.mysql.com/)
- [Oracle](https://www.oracle.com/index.html)
- [SQLite](https://sqlite.org/index.html)

Une base de données relationnelle stocke les données de manière structurée et tabulaire. C'est-à-dire qu'elle stocke les informations dans des **tables**, que vous pouvez considérer comme des conteneurs de stockage pour les données. Par exemple, une entreprise pourrait avoir une table `employees` pour stocker les données sur ses employés.

Les bases de données relationnelles ont un schéma logique strict, statique et prédéfini. Vous pouvez considérer un schéma de base de données comme un plan d'organisation – un ensemble de règles pour ce qui peut et ne peut pas entrer dans la table et les conditions pour configurer les données.

Dans chaque table, il y a au moins une **colonne**. Ces colonnes ont un type de données spécifique, tel que `INTEGER` ou `VARCHAR`. Dans la table `employees`, certaines colonnes pourraient être `employee_id`, `name`, `department`, `email`, et `salary`.

Les colonnes et les types de données autorisés dans chaque colonne constituent le schéma.

```sql
             EMPLOYEES

+-------------+------+------------+-------+--------+
| employee_id | name | department | email | salary |
+-------------+------+------------+-------+--------+
```


Une table aura également des **lignes**, ou *enregistrements*. Un enregistrement est une seule entrée de valeur de données qui doit adhérer au schéma prédéfini. Essentiellement, c'est un seul élément.

```sql
             EMPLOYEES
+-------------+------------------+------------+-----------------------+--------+
| employee_id |       name       | department |         email         | salary |
+-------------+------------------+------------+-----------------------+--------+
|           1 |  John Doe        | IT         | johndoe@company.com   |   3500 |
|           2 |  Kelly Kellinson | Marketing  | kelly@company.com     |   1500 |
|           3 |  Mike Manson     | Product    | mikekane@company.com  |   2300 |
+-------------+------------------+------------+-----------------------+--------+
```

Et puisque les bases de données relationnelles supportent SQL, vous pouvez effectuer des requêtes. Par exemple, si vous vouliez `voir` les `noms` des `employés`, dont le salaire mensuel est `supérieur à 2000 dollars`, alors vous écriviez la requête SQL suivante :

```SQL
SELECT name FROM employees
WHERE salary > 2000;
```

À partir de la requête ci-dessus, vous obtiendriez le résultat suivant :

```SQL
+-------------+
|    name     |
+-------------+
| John Doe    |
| Mike Manson |
+-------------+
```

### Caractéristiques des bases de données relationnelles <a name="caracteristiques"></a>

Jusqu'à présent, vous savez que les bases de données relationnelles :

- sont au format tabulaire,
- sont très organisées, et les données stockées sont bien structurées,
- ont un schéma strict, rigide et prédéfini,
- utilisent SQL pour effectuer des requêtes de base de données et manipuler les données.

De plus, une base de données relationnelle peut avoir plus d'une table, et comme le suggère le nom de ce type de Système de Gestion de Base de Données, les tables sont *liées* les unes aux autres.

Par exemple, une entreprise de commerce électronique peut avoir une table `products`, une table `users`, une table `emails` et une table `orders`.

Puisqu'il existe un lien et une connexion entre les tables et les informations qu'elles contiennent, vous pouvez même joindre des tables à l'aide de quelques commandes.

Il existe une *clé primaire*, qui agit comme un identifiant et garantit que chaque élément de la table est unique, évitant ainsi les doublons et les données redondantes dans les tables. 

Et il existe une *clé étrangère* qui crée ces relations préétablies entre les tables.

Les points de données dans différentes tables peuvent avoir des relations distinctes :

- **Relations un-à-un**. Dans de tels cas, un enregistrement dans une table est lié à un seul enregistrement dans une autre table. Un exemple de relation un-à-un dans un magasin de commerce électronique est qu'un utilisateur ne peut avoir qu'une seule adresse e-mail, et qu'une adresse e-mail ne peut appartenir qu'à un seul utilisateur.
- **Relations un-à-plusieurs**. Dans de tels cas, un enregistrement dans une table est lié à de nombreux autres enregistrements dans une autre table. Par exemple, dans un magasin de commerce électronique, un seul utilisateur peut passer de nombreuses commandes, mais chacune de ces commandes est passée par un seul utilisateur.
- **Relations plusieurs-à-plusieurs**. Dans de tels cas, un ou plusieurs enregistrements dans une table peuvent être liés à un ou plusieurs enregistrements dans une autre table. Par exemple, dans un magasin de commerce électronique, une commande peut contenir de nombreux produits et un produit peut être commandé plusieurs fois.

### Propriétés ACID dans les bases de données relationnelles <a name="acid"></a>

Les bases de données relationnelles offrent le modèle de cohérence ACID. 

ACID est un acronyme pour **A**tomicité, **C**ohérence, **I**solation, **D**urabilité.

**Atomicité** signifie que les transactions sont atomiques et adoptent une approche "tout ou rien". 

Par exemple, soit l'opération entière est réussie et est terminée du début à la fin, soit elle est infructueuse, et il y a un "retour arrière" de l'opération entière. 

Toutes les opérations sont garanties de se terminer soit par un succès, soit par un échec, et aucune n'est partiellement réussie. 

**Cohérence** est la propriété qui garantit que la structure de la base de données reste intacte du début à la fin d'une transaction. Elle s'assure que toute donnée entrant dans la base de données suit les règles et contraintes qui sont mises en place. C'est ce qui sécurise et maintient l'intégrité des données dans les bases de données relationnelles.

**Isolation** signifie que malgré le nombre de transactions ayant lieu à un moment donné, chaque transaction est traitée comme une unité atomique et séparée, et les transactions semblent se produire dans un ordre séquentiel. 

Par exemple, si deux transactions se produisent en même temps, cette propriété garantit qu'une transaction, et les changements qui s'y produisent, n'affectera en aucune manière l'autre transaction.

Et enfin, **Durabilité** signifie que tout résultat et changement des transactions sont validés et donc permanents et persisteront, même en cas de défaillance du système.

Le modèle ACID garantit que les bases de données sont fiables et sécurisées.

## Qu'est-ce qu'une base de données non relationnelle ? <a name="non-relational"></a>

Une base de données non relationnelle est également appelée base de données NoSQL. Vous verrez souvent que NoSQL signifie à la fois "**N**ot **o**nly **SQL**" et aussi "Non-SQL".

Dans tous les cas, une base de données non relationnelle fait référence à une base de données qui n'utilise pas le modèle de données relationnel.

Bien que ce terme et ce type de base de données existent depuis des décennies, les bases de données NoSQL ont commencé à gagner en popularité à la fin des années 1990, lorsque l'Internet a connu un essor. 

Les bases de données relationnelles seules ne pouvaient pas gérer la vitesse – ainsi que les grandes quantités et la taille des données diverses et complexes – que cette augmentation de l'utilisation d'Internet et les nouvelles applications web développées exigeaient et demandaient.

Certaines des bases de données non relationnelles les plus populaires sont :

- [MongoDB](https://www.mongodb.com/),
- [Redis](https://redis.io/),
- [Apache Cassandra](https://cassandra.apache.org/_/index.html),
- [Google Cloud Bigtable](https://cloud.google.com/bigtable),
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

Une base de données non relationnelle ne stocke pas et n'organise pas les données dans un format tabulaire. Il n'y a pas de tables, de lignes, de colonnes ou de relations entre différents points de données.

Au lieu de cela, les données sont stockées dans des **collections**. La base de données est généralement non structurée et utilise un schéma dynamique.

### Types de bases de données non relationnelles <a name="types"></a>

Il existe quatre principaux types de bases de données non relationnelles :

- **Bases de données orientées colonnes**,
- **Stores clé-valeur**,
- **Stores orientés documents**,
- **Bases de données orientées graphe**.


**Bases de données orientées colonnes** sont similaires en concept aux bases de données relationnelles. Mais elles utilisent des groupes, ou des ensembles de colonnes (également connus sous le nom de familles de colonnes) au lieu de lignes pour organiser logiquement les données liées.

Vous pouvez accéder à une famille de colonnes indépendamment en utilisant une clé de ligne unique associée à une colonne individuelle. La recherche de données spécifiques est beaucoup plus rapide et économise un temps significatif puisque il n'est pas nécessaire de parcourir des lignes d'informations non liées pour trouver ce que vous recherchez.

**Stores clé-valeur** sont l'un des types les plus simples de bases de données non relationnelles.

Les données sont stockées dans des dictionnaires ou des tables de hachage sous la forme de collections de paires clé-valeur. 

Ce type de base de données a des clés qui doivent être uniques. 

Les clés agissent comme un pointeur vers une valeur spécifique et sont associées à cette valeur.

La valeur assignée à une clé peut être n'importe quel morceau d'information et type de données. 

Pour récupérer et accéder à la valeur, vous utilisez la clé unique comme référence.


**Stores orientés documents** stockent également les données sous forme de paires clé-valeur. Mais dans ce cas, la valeur est un document qui a une clé unique comme identifiant.

Le document peut avoir n'importe quel format, tel que XML, YAML ou binaire, mais généralement il a un format JSON.

Ce type de base de données stocke les données de manière semi-structurée.

Il n'y a pas de schéma ou de structure prédéfinie. Grâce à cela, il offre de la flexibilité et la capacité de réorganiser et de retravailler la structure de la base de données si les exigences du projet changent.

Il fournit également un type de langage de requête similaire à SQL ou une API pour effectuer des requêtes et des opérations CRUD sur les données.

**Bases de données orientées graphe** sont le type le plus complexe de base de données non relationnelle, et elles peuvent gérer de grands ensembles de données. 

Elles se concentrent sur les connexions et les relations entre les éléments de données et utilisent la théorie des graphes pour stocker, rechercher et gérer ces relations. 

Elles utilisent des *nœuds* pour stocker les données et représenter une entité ou un morceau de données individuel. Un nœud est connecté et lié à un autre nœud. 

Pour représenter les connexions ou les relations entre les entités, les bases de données orientées graphe utilisent des *arêtes*.

### Propriétés BASE dans les bases de données non relationnelles <a name="base"></a>

Les bases de données non relationnelles offrent le modèle de cohérence BASE. Ce modèle n'est pas aussi rigide que le modèle ACID des bases de données relationnelles.

BASE est un acronyme pour :

- **B**asic **A**vailability. Ce modèle ne se concentre pas sur la cohérence immédiate des données. Cependant, le système semble fonctionner en continu et garantit la disponibilité des données à tout moment.
- **S**oft state. En raison du manque de cohérence immédiate, l'état du système peut changer avec le temps. Un état souple signifie que le système n'a pas besoin d'être cohérent en écriture.
- **E**ventual consistency. La priorité principale est la disponibilité constante des données et non celle de la cohérence des données. Cependant, à un moment donné, vous pouvez vous attendre à ce que les données soient cohérentes. Cela peut se produire lorsque le système cesse de recevoir des entrées.

## Comment choisir entre les bases de données SQL et NoSQL <a name="pick"></a>

Après avoir appris les bases des bases de données SQL et NoSQL, vous vous demandez peut-être laquelle des deux choisir pour votre projet.

Eh bien, il n'y a pas de réponse claire à cette question. 

Les deux types de bases de données ont des avantages et des inconvénients, et cela dépend largement du type d'application que vous construisez, du genre de données avec lesquelles vous allez travailler, et de vos objectifs futurs.

Il est courant pour les entreprises d'utiliser les deux types de bases de données pour leurs produits.

Voici un résumé rapide de leurs caractéristiques pour vous aider à décider laquelle pourrait être la plus adaptée pour vous.

### Quand utiliser une base de données SQL :

- Vous avez besoin de données très structurées réparties sur plusieurs tables. Vous avez besoin que vos données adhèrent à un schéma strict, prévisible, prédéfini et déjà planifié.
- Vos données resteront relativement les mêmes. Les bases de données SQL sont pratiques si vous ne prévoyez pas de changer fréquemment la structure de la base de données et n'avez pas besoin de mettre à jour régulièrement les éléments. Gardez à l'esprit qu'elles offrent peu de flexibilité.
- Vous avez besoin de données cohérentes.
- L'intégrité et la sécurité des données sont une priorité.
- Vous voulez des résultats précis pour des requêtes complexes.

Un inconvénient des bases de données SQL est qu'elles évoluent verticalement.

Vous devrez augmenter les efforts matériels et de puissance de calcul sur votre machine actuelle à mesure que vous collectez et stockez plus de données. 

Cela peut être coûteux. 

Une augmentation de la puissance de traitement et de la mémoire de stockage est nécessaire pour gérer une augmentation de la charge afin d'améliorer les performances.

### Quand utiliser une base de données NoSQL :

- Vous travaillez dans un environnement de développement rapide qui nécessite des adaptations fréquentes des exigences et des changements constants de la structure de la base de données.
- Vous travaillez avec de grandes quantités de données qui sont diverses par nature mais ne nécessitent pas beaucoup de structure ou de précision.
- Vous travaillez avec des données qui nécessitent des mises à jour fréquentes. Les bases de données NoSQL offrent un schéma flexible et dynamique qui permet des changements réguliers des données.
- Vous voulez des résultats de requêtes rapides et une disponibilité continue du système.
- Vous ne voulez pas effectuer de planification, de préparation ou de conception préalable de la base de données, mais voulez commencer à construire immédiatement.

Un grand avantage des bases de données NoSQL est qu'elles évoluent horizontalement.

Elles sont conçues de manière à ce que davantage de machines puissent être ajoutées à la machine existante (comme des serveurs cloud). Ce comportement est plus souhaitable par rapport à l'évolution verticale qui nécessite des ressources CPU (Unité Centrale de Traitement) ou RAM (Mémoire Vive) supplémentaires.

Mais bien sûr, un inconvénient des bases de données NoSQL est qu'elles ne garantissent pas l'intégrité et la cohérence des données.

## Apprentissage supplémentaire <a name="extra"></a>

Cet article n'a fait qu'effleurer la surface, et la meilleure façon d'apprendre est de pratiquer.

Voici quelques ressources d'apprentissage pour en savoir plus sur les bases de données et SQL :

- [Apprendre SQL – Cours gratuits sur les bases de données relationnelles pour débutants](https://www.freecodecamp.org/news/learn-sql-free-relational-database-courses-for-beginners/). Marquez cette page pour une liste de cours SQL gratuits.
- [Certification en bases de données relationnelles de freeCodeCamp](https://www.freecodecamp.org/learn/relational-database/). Dans ce cours, vous apprendrez les outils de développement nécessaires. Ensuite, vous apprendrez à utiliser un éditeur de code, la ligne de commande et Git. Vous apprendrez également à travailler avec PostgreSQL (un système de gestion de base de données relationnelle) et SQL – son langage de requête.
- [Apprendre les bases de données NoSQL dans ce cours de 3 heures](https://www.freecodecamp.org/news/learn-nosql-in-3-hours/). Dans ce cours, vous apprendrez les quatre différents types de bases de données NoSQL. En plus d'apprendre la théorie, vous pratiquerez également la construction des quatre types.
## Conclusion

Vous êtes arrivé à la fin de l'article !

Espérons qu'il vous a aidé à comprendre les différences principales entre les bases de données relationnelles et non relationnelles. Vous avez également quelques ressources supplémentaires pour commencer à apprendre et mettre en pratique vos nouvelles compétences.

Merci d'avoir lu, et bon codage !