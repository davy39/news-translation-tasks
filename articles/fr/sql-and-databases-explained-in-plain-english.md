---
title: Qu'est-ce que SQL ? Qu'est-ce qu'une base de données ? Les systèmes de gestion
  de bases de données relationnelles (RDBMS) expliqués en anglais simple.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-07T16:29:55.000Z'
originalURL: https://freecodecamp.org/news/sql-and-databases-explained-in-plain-english
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c96c2740569d1a4ca127c.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Qu'est-ce que SQL ? Qu'est-ce qu'une base de données ? Les systèmes de
  gestion de bases de données relationnelles (RDBMS) expliqués en anglais simple.
seo_desc: "By Sameer Khoja\nDatabases can be tricky to wrap your head around. However,\
  \ they're essential to full-stack programming and building out back-end services\
  \ that store data. \nIn this post, I'll be demystifying SQL, Databases, and Relational\
  \ Database Man..."
---

Par Sameer Khoja

Les bases de données peuvent être difficiles à comprendre. Cependant, elles sont essentielles à la programmation full-stack et à la construction de services back-end qui stockent des données. 

Dans cet article, je vais démystifier SQL, les bases de données et les systèmes de gestion de bases de données relationnelles. J'utiliserai également quelques analogies avec le [Monde des Sorciers](https://en.wikipedia.org/wiki/Wizarding_World), y compris Harry Potter lui-même et certains des cours qu'il suit à Poudlard.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-135.png)

Avant de plonger dans les termes clés, définissons ce qu'est une base de données :

Une **base de données** est un ensemble structuré de données stockées dans un ordinateur, surtout accessible de diverses manières. Il s'agit essentiellement d'un ensemble organisé de données sur un ordinateur, qui peut être accessible électroniquement à partir d'un système informatique.

## Termes clés

Voici quelques termes clés avec lesquels nous allons commencer :

* **RDBMS** : Systèmes de gestion de bases de données relationnelles. Ce cadre pour les bases de données est la base de MySQL.
* **SQL** : Langage de requête structuré.
* **Tables** : Objets de base de données qui contiennent des données. Un exemple de nom de table est "Étudiants", "Professeurs" ou "Cours".
* **Champs** : Les valeurs d'une table sont appelées champs. Des exemples de champs pour les étudiants seraient "Prénom", "Nom de famille" et "Moyenne".
* **Enregistrement/Ligne** : Une entrée individuelle dans la table. 

Après avoir ajouté les professeurs et les cours à la base de données, nous pouvons avoir des tables pour les étudiants, les professeurs et les cours. 

Alors que nous avançons dans le guide, nous n'utiliserons que l'exemple des **Étudiants** ici comme référence. Si vous aviez la chance d'être embauché comme ingénieur logiciel à Poudlard, votre base de données pourrait bien utiliser certaines de ces commandes :D

## Instructions SQL

### Syntaxe

Le point-virgule est la manière standard de séparer une instruction SQL d'une autre. Il permet d'exécuter plusieurs instructions SQL dans le même appel. Dans ce guide, nous aurons un point-virgule à la fin de chaque instruction.

### Les commandes SQL les plus importantes

**Create** : Crée une nouvelle table SQL. 

Si nous créions la base de données des étudiants pour l'école de Poudlard, par exemple, nous utiliserions **CREATE** pour créer une table appelée "Étudiants". 

* Syntaxe

```sql
CREATE TABLE nom_table (
    colonne1 type_de_données,
    colonne2 type_de_données,
    colonne3 type_de_données,
   ....
);
```

* Exemple

```sql
CREATE TABLE Étudiants
                (prénom VARCHAR(255),
                nom VARCHAR(255),
                login VARCHAR(255),
                âge INTEGER,
                moyenne REAL,
                maison VARCHAR(255));
```

**Drop** : Supprime une table. Soyez très prudent lorsque vous utilisez cette commande, car elle effacera toutes les données de la table !

Si nous voulions supprimer toute la base de données des étudiants, nous utiliserions **DROP** pour effectuer cette action.

* Syntaxe

```sql
DROP TABLE nom_table;
```

* Exemple

```sql
DROP TABLE Étudiants;
```

**Insert** : Ajoute de nouvelles lignes de données à une table. 

Nous utiliserions **INSERT** pour ajouter de nouveaux étudiants lorsqu'ils s'inscrivent à Poudlard. 

* Syntaxe

```sql
INSERT INTO nom_table (colonne1, colonne2, colonne3, ...)
VALUES (valeur1, valeur2, valeur3, ...);
```

* Exemple

```sql
INSERT 
INTO Étudiants(prénom, nom, login, âge, moyenne, maison)
VALUES 
('Harry',     'Potter', 'legarçonquisurvecu', 15, 4.0, 'Gryffondor'),
('Hermione', 'Granger','granger2',       15, 4.5, 'Gryffondor'),
('Ron',       'Weasley','weasley7',       15, 3.7, 'Gryffondor'),
('Draco',     'Malfoy', 'malfoy999',      15, 4.0, 'Serpentard'),
('Cedric',    'Diggory','diggory123',     15, 4.0, 'Poufsouffle');
```

**Select** : Utilisé pour récupérer des données dans une base de données à retourner sous forme de tableau. 

Si nous voulions récupérer tous les noms des étudiants qui sont dans la maison Gryffondor, nous utiliserions la commande **SELECT**. L'exemple ci-dessous interroge la table des étudiants pour le prénom et le nom de famille de chaque étudiant dans la base de données, ce qui pour nous est simplement les cinq lignes décrites ci-dessus.

* Syntaxe

```sql
SELECT colonne1, colonne2, ...
FROM nom_table;
```

* Exemple

```sql
SELECT prénom, nom FROM Étudiants;
```

| prénom | nom |
| ---------- | --------- |
| Harry      | Potter    |
| Hermione  | Granger   |
| Ron        | Weasley   |
| Draco      | Malfoy    |
| Cedric     | Diggory   |

Alternativement, si nous voulons sélectionner tous les champs de la table, notre commande utiliserait la syntaxe "*", qui signifie sélectionner tous les champs :

```sql
SELECT * FROM Étudiants;
```

| prénom | nom | login          | âge | moyenne | maison      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | legarçonquisurvecu | 15  | 4   | Gryffondor |
| Hermione  | Granger   | granger2       | 15  | 4.5 | Gryffondor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffondor |
| Draco      | Malfoy    | malfoy999      | 15  | 4   | Serpentard  |
| Cedric     | Diggory   | diggory123     | 15  | 4   | Poufsouffle |

### Clauses

Une **clause** est un morceau logique d'une instruction SQL, et elle est (en théorie) un champ facultatif. 

Dans l'instruction ci-dessus, nous avons simplement retourné tous les champs de la base de données des étudiants. Nous n'avons pas spécifié de condition sur les valeurs retournées. 

Et si nous voulions interroger non pas tous les étudiants, mais seulement ceux dont la maison est Gryffondor ? Et si nous voulions interroger les étudiants dont le prénom commence par "H", ou les étudiants dans Poufsouffle ou Serpentard ? Ces cas plus complexes sont résolus par les clauses SQL.

Voici un aperçu des clauses les plus courantes, mais il existe plusieurs autres clauses dans le langage SQL. Voici un [bon aperçu général](https://www.freecodecamp.org/news/basic-sql-commands/) si vous voulez plus d'informations.

### Exemples de clauses

**Where** : Utilisé pour indiquer une condition lors de la récupération de données dans une base de données. En revenant à l'exemple avec Select, nous devrions utiliser **WHERE** afin de spécifier la maison comme Gryffondor.

* Syntaxe

```sql
SELECT colonne1, colonne2, ...
FROM nom_table
WHERE condition;
```

* Exemple

```sql
SELECT * FROM Étudiants
WHERE maison='Gryffondor';
```

| prénom | nom | login          | âge | moyenne | maison      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | legarçonquisurvecu | 15  | 4   | Gryffondor |
| Hermione  | Granger   | granger2       | 15  | 4.5 | Gryffondor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffondor |

**And** : Utilisé pour combiner plusieurs clauses dans une instruction SQL, où toutes les conditions séparées par AND sont vraies. Nous utiliserions AND pour obtenir les étudiants de Gryffondor qui ont une moyenne supérieure à 3,8.

* Syntaxe

```sql
SELECT colonne1, colonne2, ...
FROM nom_table
WHERE condition1 AND condition2 AND condition3 ...;
```

* Exemple

```sql
SELECT * FROM Étudiants
WHERE maison='Gryffondor' AND moyenne>3.8;
```

| prénom | nom | login          | âge | moyenne | maison      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | legarçonquisurvecu | 15  | 4   | Gryffondor |
| Hermione  | Granger   | granger2       | 15  | 4.5 | Gryffondor |

**Or** : Similaire à AND, mais ne retourne les données que si UNE SEULE des conditions séparées par OR est vraie. Si nous voulions récupérer les étudiants de Poufsouffle et de Serpentard, mais pas les deux, nous utiliserions la commande OR.

* Syntaxe

```sql
SELECT colonne1, colonne2, ...
FROM nom_table
WHERE condition1 OR condition2 OR condition3 ...;
```

* Exemple

```sql
SELECT * FROM Étudiants
WHERE maison='Serpentard' OR maison='Poufsouffle';
```

| prénom | nom | login      | âge | moyenne | maison      |
| ---------- | --------- | ---------- | --- | --- | ---------- |
| Draco      | Malfoy    | malfoy999  | 15  | 4   | Serpentard  |
| Cedric     | Diggory   | diggory123 | 15  | 4   | Poufsouffle |

**Like** : Utilisé avec WHERE pour rechercher un motif spécifique. Si nous voulions seulement le prénom et le nom des sorciers/sorcières dont les noms commencent par "H", nous pourrions utiliser la commande Like.

* Syntaxe

```sql
SELECT colonne1, colonne2, ...
FROM nom_table
WHERE colonneN LIKE motif;
```

* Exemple

```sql
SELECT prénom, nom FROM Étudiants
WHERE prénom LIKE 'H%';
```

| prénom | nom |
| ---------- | --------- |
| Harry      | Potter    |
| Hermione  | Granger   |

**Count** : Utilisé pour trouver le nombre d'une colonne (ou de colonnes) dans une table.

* Syntaxe

```sql
SELECT COUNT(nom_colonne)
FROM nom_table
WHERE condition;
```

* Exemple

```sql
SELECT COUNT(prénom) FROM Étudiants;
```

| COUNT(prénom) |
| ----------------- |
| 5                 |

Deux autres commandes qui utilisent la même syntaxe sont AVG et SUM. AVG calculera la moyenne de toutes les valeurs, et SUM calculera la somme de toutes les valeurs.

**Select Limit** : Utilisé pour limiter les réponses à un nombre spécifié. La manière dont les meilleures réponses sont choisies est dans l'ordre d'insertion dans la base de données chronologiquement.

* Syntaxe

```sql
SELECT nom_colonne(s)
FROM nom_table
WHERE condition
LIMIT nombre;
```

* Exemple

```sql
SELECT * FROM Étudiants LIMIT 3;
```

| prénom | nom | login          | âge | moyenne | maison      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Harry      | Potter    | legarçonquisurvecu | 15  | 4   | Gryffondor |
| Hermione  | Granger   | granger2       | 15  | 4.5 | Gryffondor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffondor |

### Autres commandes utiles

**Order By** : Trie les résultats par ordre croissant ou décroissant.

* Syntaxe

```sql
SELECT colonne1, colonne2, ...
FROM nom_table
ORDER BY colonne1, colonne2, ... ASC|DESC;
```

* Exemple

```sql
SELECT * FROM Étudiants ORDER BY prénom;
```

| prénom | nom | login          | âge | moyenne | maison      |
| ---------- | --------- | -------------- | --- | --- | ---------- |
| Cedric     | Diggory   | diggory123     | 15  | 4   | Poufsouffle |
| Draco      | Malfoy    | malfoy999      | 15  | 4   | Serpentard  |
| Harry      | Potter    | legarçonquisurvecu | 15  | 4   | Gryffondor |
| Hermione  | Granger   | granger2       | 15  | 4.5 | Gryffondor |
| Ron        | Weasley   | weasley7       | 15  | 3.7 | Gryffondor |

**Group By** : Regroupe les catégories qui ont les mêmes valeurs en lignes. Si vous vouliez connaître le nombre d'étudiants dans chaque maison (3 à Gryffondor par exemple), vous pouvez utiliser la commande Group By.

* Syntaxe

```sql
SELECT nom_colonne(s)
FROM nom_table
WHERE condition
GROUP BY nom_colonne(s)
ORDER BY nom_colonne(s);
```

* Exemple

```sql
SELECT COUNT(prénom), maison FROM Étudiants GROUP BY maison;
```

| COUNT(prénom) | maison      |
| ----------------- | ---------- |
| 3                 | Gryffondor |
| 1                 | Poufsouffle |
| 1                 | Serpentard  |

Enfin, [ici](https://www.db-fiddle.com/f/9Jq8KfBPtcYRh84PnPUQWi/61) se trouve un DB Fiddle qui montre toutes les commandes ci-dessus en action !

## Bases de données normalisées vs dénormalisées

Lors de la conception d'une base de données, il existe deux principaux modèles de conception que vous pouvez suivre, chacun avec ses propres compromis.

**Normalisées** : Optimisées pour **minimiser la redondance**, pas pour le temps de lecture.

Supposons que nous avons une table de cours qui contient un identifiant de professeur pour le professeur enseignant ce cours. Nous avons également une base de données de professeurs qui contient le nom du professeur. 

Lorsque nous voulons obtenir les noms des professeurs enseignant un cours particulier, nous devrons interroger à la fois les tables Cours et Professeurs car la table des cours ne contient pas le nom du professeur (efficace mais redondant).

**Dénormalisées** : Optimisées pour le **temps de lecture**, pas pour minimiser la redondance.

Supposons que nous avons une table de cours qui contient un identifiant de professeur ET un nom de professeur. Nous avons une base de données de professeurs qui contient également le nom du professeur. Lorsque nous voulons obtenir les noms des professeurs dans le cours, nous pouvons simplement utiliser la table des cours (redondant mais efficace).

## Intégrité des données

Il est vital pour les utilisateurs que les données avec lesquelles ils interagissent soient sécurisées, correctes et sensées. Des exemples incluent s'assurer que l'âge n'est pas un nombre négatif, ou que deux étudiants n'ont pas les mêmes informations. Nous appelons cela **l'intégrité des données**. 

L'intégrité des données prend plusieurs formes et peut être divisée en quatre catégories :

* **Intégrité d'entité** : Aucune ligne en double n'existe dans une table. Par exemple, nous ne pouvons pas insérer Ron Weasley deux fois dans la base de données.
* **Intégrité de domaine** : Restreindre le type de valeurs que l'on peut insérer afin de forcer des valeurs correctes. Par exemple, une maison ne peut être que Gryffondor, Serdaigle, Serpentard ou Poufsouffle.
* **Intégrité référentielle** : Les enregistrements utilisés par d'autres enregistrements ne peuvent pas être supprimés. Un professeur ne peut pas être supprimé s'il enseigne actuellement un cours.
* **Intégrité définie par l'utilisateur** : Une catégorie "autre" qui consiste en une logique et des règles liées à l'entreprise pour la base de données.

## Bases de données SQL courantes

* **Oracle** : Très stable et mature mais peut être coûteux
* **MySQL** : Léger et rapide à configurer mais pas aussi mature qu'Oracle
* **PostgreSQL** : Bon pour certains cas d'utilisation mais pas super rapide

## Ressources

* [SWEPrep - Questions d'entretien directement dans votre boîte de réception](https://sweprep.substack.com/)
* [SQL et bases de données de freeCodeCamp](https://www.freecodecamp.org/news/sql-and-databases-full-course/)
* [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
* [Effective Java](https://www.amazon.com/Effective-Java-2nd-Joshua-Bloch/dp/0321356683)
* [Documentation Oracle](https://www.oracle.com/uk/database/index.html)
* [Documentation MySql](https://www.mysql.com/)
* [Documentation PostgreSQL](https://www.postgresql.org/)

## Rester à jour

* **Fils Reddit** : Excellents fils sur les bases de données, SQL et les nouvelles technologies
* **[Hacker News](https://news.ycombinator.com/)** : Ressource vraiment excellente pour rester informé des derniers développements dans l'industrie technologique
* **[CodePen](https://codepen.io/)** : Une excellente ressource pour découvrir de bonnes pratiques SQL.