---
title: Feuille de triche des commandes SQL – Comment apprendre SQL en 10 minutes
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-11-23T15:36:59.000Z'
originalURL: https://freecodecamp.org/news/learn-sql-in-10-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/sql-in-10-min-image.jpeg
tags:
- name: cheatsheet
  slug: cheatsheet
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Feuille de triche des commandes SQL – Comment apprendre SQL en 10 minutes
seo_desc: 'I’m an AI researcher, so one of the main things I deal with is data. A
  lot of it.

  With more than 2.5 exabytes of data generated every day, it comes as no surprise
  that this data needs to be stored somewhere where we can access it when we need
  it.

  Thi...'
---

Je suis un chercheur en IA, donc l'une des principales choses que je gère est la donnée. Beaucoup de données.

Avec plus de [2,5 exaoctets de données générés *chaque jour*](https://www.socialmediatoday.com/news/how-much-data-is-generated-every-minute-infographic-1/525692/), il n'est pas surprenant que ces données doivent être stockées quelque part où nous pouvons y accéder lorsque nous en avons besoin.

Cet article vous guidera à travers une feuille de triche modifiable pour vous mettre rapidement en route avec SQL.

## Qu'est-ce que SQL ?

SQL signifie Structured Query Language. C'est un langage pour les systèmes de gestion de bases de données relationnelles. SQL est utilisé aujourd'hui pour stocker, récupérer et manipuler des données au sein de bases de données relationnelles.

Voici à quoi ressemble une base de données relationnelle de base :

![Source : https://assets-global.website-files.com/5debb9b4f88fbc3f702d579e/5e3c1a71724a38245aa43b02_99bf70d46cc247be878de9d3a88f0c44.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1745433576314/ef41d0e6-7187-4856-927f-c1b899e3b73b.png align="center")

En utilisant SQL, nous pouvons interagir avec la base de données en écrivant des *requêtes*.

Voici à quoi ressemble une requête d'exemple :

```sql
SELECT * FROM customers;
```

En utilisant cette instruction `SELECT`, la requête sélectionne *toutes* les données de toutes les colonnes dans la table des clients et retourne des données comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-55.png align="left")

*Source : Database Guide*

Le caractère générique astérisque (*) fait référence à « *tous* » et sélectionne *toutes* les lignes et colonnes. Nous pouvons le remplacer par des noms de colonnes spécifiques à la place—ici, seules ces colonnes seront retournées par la requête

```sql
SELECT FirstName, LastName FROM customers;
```

L'ajout d'une clause `WHERE` vous permet de filtrer ce qui est retourné :

```sql
SELECT * FROM customers WHERE age >= 30 ORDER BY age ASC;
```

Cette requête retourne toutes les données de la table des produits avec une valeur *age* supérieure à 30.

L'utilisation du mot-clé `ORDER BY` signifie simplement que les résultats seront triés en utilisant la colonne age de la valeur la plus basse à la plus haute

En utilisant l'instruction `INSERT INTO`, nous pouvons ajouter de nouvelles données à une table. Voici un exemple de base ajoutant un nouvel utilisateur à la table des clients :

```sql
INSERT INTO customers(FirstName, LastName, address, email)
VALUES ('Alice', 'Bob', 'McLaren Vale, South Australia', 'test@fakeGmail.com');
```

Bien sûr, ces exemples ne démontrent qu'une très petite sélection de ce que le langage SQL peut faire. Nous en apprendrons davantage dans ce guide.

## Pourquoi apprendre SQL ?

Nous vivons à l'ère du Big Data, où les données sont utilisées de manière extensive pour trouver des informations et informer la stratégie, le marketing, la publicité et une pléthore d'autres opérations.

Les grandes entreprises comme Google, Amazon, AirBnb utilisent de grandes bases de données relationnelles comme base pour améliorer l'expérience client. Comprendre SQL est une compétence précieuse à avoir non seulement pour les scientifiques et analystes de données, mais pour tout le monde.

*Comment pensez-vous que vous avez soudainement obtenu une publicité YouTube sur des chaussures alors qu'il y a quelques minutes, vous cherchiez vos chaussures préférées sur Google ? C'est SQL (ou une forme de SQL) en action !*

## SQL vs MySQL

Avant de continuer, je veux simplement clarifier un sujet souvent confondu—la différence entre SQL et MySQL. Il s'avère qu'ils *ne sont pas* la même chose !

SQL est un langage, tandis que MySQL est un système pour implémenter SQL.

**SQL** définit la syntaxe qui vous permet d'écrire des requêtes qui gèrent les bases de données relationnelles.

**MySQL** est un système de *base de données* qui s'exécute sur un serveur. Il vous permet d'écrire des requêtes en utilisant la syntaxe SQL pour gérer les bases de données MySQL.

En plus de MySQL, il existe d'autres systèmes qui implémentent SQL. Certains des plus populaires incluent :

* SQLite

* Oracle Database

* PostgreSQL

* Microsoft SQL Server

## Comment installer MySQL

Dans la plupart des cas, MySQL est le choix préféré pour un système de gestion de base de données. De nombreux systèmes de gestion de contenu populaires (comme Wordpress) utilisent MySQL par défaut, donc utiliser MySQL pour gérer ces applications peut être une bonne idée.

Pour utiliser MySQL, vous devrez l'installer sur votre système :

### Installer MySQL sur Windows

La méthode recommandée pour installer MySQL sur Windows est d'utiliser l'installateur MSI du [site web de MySQL](https://dev.mysql.com/doc/mysql-installer/en/mysql-installer.html).

[Cette ressource vous guidera dans le processus d'installation.](https://www.liquidweb.com/kb/install-mysql-windows/)

### Installer MySQL sur macOS

Sur macOS, l'installation de MySQL implique également de télécharger un [installateur](https://dev.mysql.com/doc/mysql-osx-excerpt/8.0/en/osx-installation-pkg.html).

[Cette ressource vous guidera dans le processus d'installation.](https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html)

## Comment utiliser MySQL

Avec MySQL maintenant installé sur votre système, je vous recommande d'utiliser une sorte d'*application de gestion SQL* pour rendre la gestion de vos bases de données beaucoup plus facile.

Il existe de nombreuses applications parmi lesquelles choisir, qui font largement le même travail, donc c'est une question de préférence personnelle pour savoir laquelle utiliser :

* [MySQL Workbench](https://www.mysql.com/products/workbench/) développé par Oracle

* [phpMyAdmin](http://phpmyadmin.net/) (fonctionne dans le navigateur web)

* [HeidiSQL](https://www.heidisql.com/) **(Recommandé pour Windows)**

* [Sequel Pro](https://www.sequelpro.com/) **(Recommandé pour macOS)**

Lorsque vous êtes prêt à commencer à écrire vos propres requêtes SQL, envisagez d'importer des données factices plutôt que de créer votre propre base de données.

Voici quelques [bases de données factices](https://dev.mysql.com/doc/index-other.html) qui sont disponibles pour le téléchargement gratuitement.

## Feuille de triche SQL – La cerise sur le gâteau

### Mots-clés SQL

Ici, vous pouvez trouver une collection de mots-clés utilisés dans les instructions SQL, une description et, lorsque cela est approprié, un exemple. Certains des mots-clés les plus avancés ont leur propre section dédiée.

Lorsque MySQL est mentionné à côté d'un exemple, cela signifie que cet exemple est uniquement applicable aux bases de données MySQL (par opposition à tout autre système de base de données).

```sql
ADD -- Ajoute une nouvelle colonne à une table existante

ADD CONSTRAINT -- Crée une nouvelle contrainte sur une table existante, qui est utilisée pour spécifier des règles pour toute donnée dans la table.

ALTER TABLE -- Ajoute, supprime ou modifie des colonnes dans une table. Il peut également être utilisé pour ajouter et supprimer des contraintes dans une table, comme indiqué ci-dessus.

ALTER COLUMN -- Modifie le type de données d'une colonne de table.

ALL -- Retourne vrai si toutes les valeurs de la sous-requête satisfont la condition passée.

AND -- Utilisé pour joindre des conditions séparées au sein d'une clause WHERE.

ANY -- Retourne vrai si l'une des valeurs de la sous-requête satisfait la condition donnée.

AS -- Renomme une table ou une colonne avec une valeur d'alias qui n'existe que pour la durée de la requête.

ASC -- Utilisé avec ORDER BY pour retourner les données dans l'ordre croissant.

BETWEEN -- Sélectionne les valeurs dans la plage donnée.

CASE -- Modifie la sortie de la requête en fonction des conditions.

CHECK -- Ajoute une contrainte qui limite la valeur qui peut être ajoutée à une colonne.

CREATE DATABASE -- Crée une nouvelle base de données.

CREATE TABLE -- Crée une nouvelle table.

DEFAULT -- Définit une valeur par défaut pour une colonne

DELETE -- Supprime des données d'une table.

DESC -- Utilisé avec ORDER BY pour retourner les données dans l'ordre décroissant.

DROP COLUMN -- Supprime une colonne d'une table.

DROP DATABASE -- Supprime la base de données entière.

DROP DEAFULT -- Supprime une valeur par défaut pour une colonne.

DROP TABLE -- Supprime une table d'une base de données.

EXISTS -- Vérifie l'existence de tout enregistrement dans la sous-requête, retourne vrai si un ou plusieurs enregistrements sont retournés.

FROM -- Spécifie quelle table sélectionner ou supprimer des données.

IN -- Utilisé avec une clause WHERE comme raccourci pour plusieurs conditions OR.

INSERT INTO -- Ajoute de nouvelles lignes à une table.

IS NULL -- Teste les valeurs vides (NULL).

IS NOT NULL -- L'inverse de NULL. Teste les valeurs qui ne sont pas vides / NULL.

LIKE -- Retourne vrai si la valeur de l'opérande correspond à un motif.

NOT -- Retourne vrai si un enregistrement NE RÉPOND PAS à la condition.

OR -- Utilisé avec WHERE pour inclure des données lorsque l'une ou l'autre condition est vraie.

ORDER BY -- Utilisé pour trier les données de résultat dans l'ordre croissant (par défaut) ou décroissant par l'utilisation des mots-clés ASC ou DESC.

ROWNUM -- Retourne les résultats où le numéro de ligne répond à la condition passée.

SELECT -- Utilisé pour sélectionner des données dans une base de données, qui sont ensuite retournées dans un ensemble de résultats.

SELECT DISTINCT -- Identique à SELECT, sauf que les valeurs en double sont exclues.

SELECT INTO -- Copie les données d'une table et les insère dans une autre.

SELECT TOP -- Vous permet de retourner un nombre défini d'enregistrements à retourner d'une table.

SET -- Utilisé avec UPDATE pour mettre à jour les données existantes dans une table.

SOME -- Identique à ANY.

TOP -- Utilisé avec SELECT pour retourner un nombre défini d'enregistrements d'une table.

TRUNCATE TABLE -- Similaire à DROP, mais au lieu de supprimer la table et ses données, cela supprime uniquement les données.

UNION -- Combine les résultats de 2 instructions SELECT ou plus et retourne uniquement des valeurs distinctes.

UNION ALL -- Identique à UNION, mais inclut les valeurs en double.

UNIQUE -- Cette contrainte garantit que toutes les valeurs dans une colonne sont uniques.

UPDATE -- Met à jour les données existantes dans une table.

VALUES -- Utilisé avec le mot-clé INSERT INTO pour ajouter de nouvelles valeurs à une table.

WHERE -- Filtre les résultats pour n'inclure que les données qui répondent à la condition donnée.
```

### Commentaires en SQL

Les commentaires vous permettent d'expliquer des sections de vos instructions SQL, sans être exécutés directement.

En SQL, il existe 2 types de commentaires, les commentaires sur une seule ligne et les commentaires sur plusieurs lignes.

#### Commentaires sur une seule ligne en SQL

Les commentaires sur une seule ligne commencent par '--'. Tout texte après ces 2 caractères jusqu'à la fin de la ligne sera ignoré.

```sql
-- Cette partie est ignorée

SELECT * FROM customers;
```

#### Commentaires sur plusieurs lignes en SQL

Les commentaires sur plusieurs lignes commencent par /* et se terminent par */. Ils s'étendent sur plusieurs lignes jusqu'à ce que les caractères de fermeture aient été trouvés.

```json
/*

Ceci est un commentaire sur plusieurs lignes.
Il peut s'étendre sur plusieurs lignes.

*/

SELECT * FROM customers;

/*

Ceci est un autre commentaire.
Vous pouvez même mettre du code dans un commentaire pour empêcher son exécution

SELECT * FROM icecreams;

*/
```

### Types de données dans MySQL

Lors de la création d'une nouvelle table ou de la modification d'une table existante, vous devez spécifier le type de données que chaque colonne accepte.

[Dans cet exemple](https://www.datadriveninvestor.com/2020/05/04/could-machine-learning-and-nlp-have-predicted-oils-crash-the-answer-is-yes/), les données passées à la colonne `id` doivent être un int (entier), tandis que la colonne `FirstName` a un type de données `VARCHAR` avec un maximum de 255 caractères.

```sql
CREATE TABLE customers(
id int,
FirstName varchar(255)
);
```

#### 1. Types de données de chaîne

```sql
CHAR(size) -- Chaîne de longueur fixe qui peut contenir des lettres, des chiffres et des caractères spéciaux. Le paramètre size définit la longueur maximale de la chaîne, de 0 à 255 avec une valeur par défaut de 1.

VARCHAR(size) -- Chaîne de longueur variable similaire à CHAR(), mais avec une plage de longueur maximale de chaîne de 0 à 65535.

BINARY(size) -- Similaire à CHAR() mais stocke des chaînes d'octets binaires.

VARBINARY(size) -- Similaire à VARCHAR() mais pour les chaînes d'octets binaires.

TINYBLOB -- Contient des objets binaires volumineux (BLOB) avec une longueur maximale de 255 octets.

TINYTEXT -- Contient une chaîne avec une longueur maximale de 255 caractères. Utilisez VARCHAR() à la place, car il est récupéré beaucoup plus rapidement.

TEXT(size) -- Contient une chaîne avec une longueur maximale de 65535 octets. Encore une fois, mieux vaut utiliser VARCHAR().

BLOB(size) -- Contient des objets binaires volumineux (BLOB) avec une longueur maximale de 65535 octets.

MEDIUMTEXT -- Contient une chaîne avec une longueur maximale de 16 777 215 caractères.

MEDIUMBLOB -- Contient des objets binaires volumineux (BLOB) avec une longueur maximale de 16 777 215 octets.

LONGTEXT -- Contient une chaîne avec une longueur maximale de 4 294 967 295 caractères.

LONGBLOB -- Contient des objets binaires volumineux (BLOB) avec une longueur maximale de 4 294 967 295 octets.

ENUM(a, b, c, etc...) -- Un objet de chaîne qui n'a qu'une seule valeur, qui est choisie dans une liste de valeurs que vous définissez, jusqu'à un maximum de 65535 valeurs. Si une valeur est ajoutée qui n'est pas dans cette liste, elle est remplacée par une valeur vide.

SET(a, b, c, etc...) -- Un objet de chaîne qui peut avoir 0 ou plusieurs valeurs, qui est choisi dans une liste de valeurs que vous définissez, jusqu'à un maximum de 64 valeurs.
```

#### 2. Types de données numériques

```sql
BIT(size) -- Un type de valeur binaire avec une valeur par défaut de 1. Le nombre autorisé de bits dans une valeur est défini via le paramètre size, qui peut contenir des valeurs de 1 à 64.

TINYINT(size) -- Un entier très petit avec une plage signée de -128 à 127, et une plage non signée de 0 à 255. Ici, le paramètre size spécifie la largeur d'affichage maximale autorisée, qui est de 255.

BOOL -- Essentiellement un moyen rapide de définir la colonne sur TINYINT avec une taille de 1. 0 est considéré comme faux, tandis que 1 est considéré comme vrai.

BOOLEAN	-- Identique à BOOL.

SMALLINT(size) -- Un petit entier avec une plage signée de -32768 à 32767, et une plage non signée de 0 à 65535. Ici, le paramètre size spécifie la largeur d'affichage maximale autorisée, qui est de 255.

MEDIUMINT(size) -- Un entier moyen avec une plage signée de -8388608 à 8388607, et une plage non signée de 0 à 16777215. Ici, le paramètre size spécifie la largeur d'affichage maximale autorisée, qui est de 255.

INT(size) -- Un entier moyen avec une plage signée de -2147483648 à 2147483647, et une plage non signée de 0 à 4294967295. Ici, le paramètre size spécifie la largeur d'affichage maximale autorisée, qui est de 255.

INTEGER(size) -- Identique à INT.

BIGINT(size) -- Un entier moyen avec une plage signée de -9223372036854775808 à 9223372036854775807, et une plage non signée de 0 à 18446744073709551615. Ici, le paramètre size spécifie la largeur d'affichage maximale autorisée, qui est de 255.

FLOAT(p) -- Une valeur de nombre à virgule flottante. Si le paramètre de précision (p) est entre 0 et 24, alors le type de données est défini sur FLOAT(), tandis que s'il est de 25 à 53, le type de données est défini sur DOUBLE(). Ce comportement est destiné à rendre le stockage des valeurs plus efficace.

DOUBLE(size, d) -- Une valeur de nombre à virgule flottante où le nombre total de chiffres est défini par le paramètre size, et le nombre de chiffres après le point décimal est défini par le paramètre d.

DECIMAL(size, d) -- Un nombre à point fixe exact où le nombre total de chiffres est défini par les paramètres size, et le nombre total de chiffres après le point décimal est défini par le paramètre d.

DEC(size, d) -- Identique à DECIMAL.
```

#### 3. Types de données Date/Heure

```sql
DATE -- Une date simple au format AAAA-MM-JJ, avec une plage prise en charge de '1000-01-01' à '9999-12-31'.

DATETIME(fsp) -- Une date et heure au format AAAA-MM-JJ hh:mm:ss, avec une plage prise en charge de '1000-01-01 00:00:00' à '9999-12-31 23:59:59'. En ajoutant DEFAULT et ON UPDATE à la définition de la colonne, elle se définit automatiquement à la date/heure actuelle.

TIMESTAMP(fsp) -- Un horodatage Unix, qui est une valeur relative au nombre de secondes depuis l'époque Unix ('1970-01-01 00:00:00' UTC). Cela a une plage prise en charge de '1970-01-01 00:00:01' UTC à '2038-01-09 03:14:07' UTC.
En ajoutant DEFAULT CURRENT_TIMESTAMP et ON UPDATE CURRENT TIMESTAMP à la définition de la colonne, elle se définit automatiquement à la date/heure actuelle.

TIME(fsp) -- Une heure au format hh:mm:ss, avec une plage prise en charge de '-838:59:59' à '838:59:59'.

YEAR -- Une année, avec une plage prise en charge de '1901' à '2155'.
```

### Opérateurs SQL

#### 1. Opérateurs arithmétiques en SQL

```sql
+ -- Addition
- -- Soustraction
* -- Multiplication
/ -- Division
% -- Modulo
```

#### 2. Opérateurs bit à bit en SQL

```sql
& -- ET bit à bit
| -- OU bit à bit
^ -- OU exclusif bit à bit
```

#### 3. Opérateurs de comparaison en SQL

```sql
= -- Égal à
> -- Supérieur à
< -- Inférieur à
>= -- Supérieur ou égal à
<= -- Inférieur ou égal à
<> -- Différent de
```

#### 4. Opérateurs composés en SQL

```sql
+= -- Ajoute et affecte
-= -- Soustrait et affecte
*= -- Multiplie et affecte
/= -- Divise et affecte
%= -- Modulo et affecte
&= -- ET bit à bit et affecte
^-= -- OU exclusif bit à bit et affecte
|*= -- OU bit à bit et affecte
```

### Fonctions SQL

#### 1. Fonctions de chaîne en SQL

```sql
ASCII -- Retourne la valeur ASCII équivalente pour un caractère spécifique.

CHAR_LENGTH -- Retourne la longueur de caractère d'une chaîne.

CHARACTER_LENGTH -- Identique à CHAR_LENGTH.

CONCAT -- Ajoute des expressions ensemble, avec un minimum de 2.

CONCAT_WS -- Ajoute des expressions ensemble, mais avec un séparateur entre chaque valeur.

FIELD -- Retourne une valeur d'index relative à la position d'une valeur dans une liste de valeurs.

FIND IN SET -- Retourne la position d'une chaîne dans une liste de chaînes.

FORMAT -- Lorsque vous passez un nombre, retourne ce nombre formaté pour inclure des virgules (par exemple 3 400 000).

INSERT -- Vous permet d'insérer une chaîne dans une autre à un certain point, pour un certain nombre de caractères.

INSTR -- Retourne la position de la première fois qu'une chaîne apparaît dans une autre.

LCASE -- Convertit une chaîne en minuscules.

LEFT -- En commençant par la gauche, extrait le nombre donné de caractères d'une chaîne et les retourne sous forme d'une autre.

LENGTH -- Retourne la longueur d'une chaîne, mais en octets.

LOCATE -- Retourne la première occurrence d'une chaîne dans une autre,

LOWER -- Identique à LCASE.

LPAD -- Remplit à gauche une chaîne avec une autre, jusqu'à une longueur spécifique.

LTRIM -- Supprime les espaces de début de la chaîne donnée.

MID -- Extrait une chaîne d'une autre, en commençant à n'importe quelle position.

POSITION -- Retourne la position de la première fois qu'une sous-chaîne apparaît dans une autre.

REPEAT -- Vous permet de répéter une chaîne

REPLACE -- Vous permet de remplacer les instances d'une sous-chaîne dans une chaîne par une nouvelle sous-chaîne.

REVERSE	-- Inverse la chaîne.

RIGHT -- En commençant par la droite, extrait le nombre donné de caractères d'une chaîne et les retourne sous forme d'une autre.

RPAD -- Remplit à droite une chaîne avec une autre, jusqu'à une longueur spécifique.

RTRIM -- Supprime les espaces de fin de la chaîne donnée.

SPACE -- Retourne une chaîne pleine d'espaces égale à la quantité que vous lui passez.

STRCMP -- Compare 2 chaînes pour les différences

SUBSTR -- Extrait une sous-chaîne d'une autre, en commençant à n'importe quelle position.

SUBSTRING -- Identique à SUBSTR

SUBSTRING_INDEX	-- Retourne une sous-chaîne d'une chaîne avant que la sous-chaîne passée ne soit trouvée le nombre de fois égal au nombre passé.

TRIM --	Supprime les espaces de fin et de début de la chaîne donnée. Identique à l'exécution de LTRIM et RTRIM ensemble.

UCASE -- Convertit une chaîne en majuscules.

UPPER -- Identique à UCASE.
```

#### 2. Fonctions numériques en SQL

```sql
ABS -- Retourne la valeur absolue du nombre donné.

ACOS -- Retourne l'arccosinus du nombre donné.

ASIN -- Retourne l'arcsinus du nombre donné.

ATAN -- Retourne l'arctangente d'un ou deux nombres donnés.

ATAN2 -- Retourne l'arctangente de deux nombres donnés.

AVG -- Retourne la valeur moyenne de l'expression donnée.

CEIL -- Retourne le nombre entier (entier) le plus proche vers le haut à partir d'un nombre décimal donné.

CEILING -- Identique à CEIL.

COS -- Retourne le cosinus d'un nombre donné.

COT -- Retourne la cotangente d'un nombre donné.

COUNT -- Retourne le nombre d'enregistrements retournés par une requête SELECT.

DEGREES -- Convertit une valeur en radians en degrés.

DIV -- Vous permet de diviser des entiers.

EXP -- Retourne e à la puissance du nombre donné.

FLOOR -- Retourne le nombre entier (entier) le plus proche vers le bas à partir d'un nombre décimal donné.

GREATEST -- Retourne la valeur la plus élevée dans une liste d'arguments.

LEAST -- Retourne la valeur la plus petite dans une liste d'arguments.

LN -- Retourne le logarithme naturel du nombre donné.

LOG -- Retourne le logarithme naturel du nombre donné, ou le logarithme du nombre donné à la base donnée.

LOG10 -- Fait la même chose que LOG, mais à la base 10.

LOG2 -- Fait la même chose que LOG, mais à la base 2.

MAX -- Retourne la valeur la plus élevée d'un ensemble de valeurs.

MIN -- Retourne la valeur la plus basse d'un ensemble de valeurs.

MOD -- Retourne le reste de la division du nombre donné par l'autre nombre donné.

PI -- Retourne PI.

POW -- Retourne la valeur du nombre donné élevé à la puissance de l'autre nombre donné.

POWER -- Identique à POW.

RADIANS -- Convertit une valeur en degrés en radians.

RAND -- Retourne un nombre aléatoire.

ROUND -- Arrondit le nombre donné au nombre de décimales donné.

SIGN -- Retourne le signe du nombre donné.

SIN -- Retourne le sinus du nombre donné.

SQRT -- Retourne la racine carrée du nombre donné.

SUM -- Retourne la valeur de l'ensemble donné de valeurs combinées.

TAN -- Retourne la tangente du nombre donné.

TRUNCATE -- Retourne un nombre tronqué au nombre de décimales donné.
```

#### 3. Fonctions de date en SQL

```sql
ADDDATE -- Ajoute un intervalle de date (par exemple : 10 JOURS) à une date (par exemple : 20/01/20) et retourne le résultat (par exemple : 20/01/30).

ADDTIME -- Ajoute un intervalle de temps (par exemple : 02:00) à une heure ou une date/heure (05:00) et retourne le résultat (07:00).

CURDATE -- Obtient la date actuelle.

CURRENT_DATE -- Identique à CURDATE.

CURRENT_TIME -- Obtient l'heure actuelle.

CURRENT_TIMESTAMP -- Obtient la date et l'heure actuelles.

CURTIME -- Identique à CURRENT_TIME.

DATE -- Extrait la date d'une expression de date/heure.

DATEDIFF -- Retourne le nombre de jours entre les deux dates données.

DATE_ADD -- Identique à ADDDATE.

DATE_FORMAT -- Formate la date selon le motif donné.

DATE_SUB -- Soustrait un intervalle de date (par exemple : 10 JOURS) à une date (par exemple : 20/01/20) et retourne le résultat (par exemple : 20/01/10).

DAY -- Retourne le jour pour la date donnée.

DAYNAME -- Retourne le nom du jour de la semaine pour la date donnée.

DAYOFWEEK -- Retourne l'index pour le jour de la semaine pour la date donnée.

DAYOFYEAR -- Retourne le jour de l'année pour la date donnée.

EXTRACT -- Extrait de la date la partie donnée (par exemple MOIS pour 20/01/20 = 01).

FROM DAYS -- Retourne la date à partir de la valeur numérique de date donnée.

HOUR -- Retourne l'heure de la date donnée.

LAST DAY -- Obtient le dernier jour du mois pour la date donnée.

LOCALTIME -- Obtient la date et l'heure locales actuelles.

LOCALTIMESTAMP -- Identique à LOCALTIME.

MAKEDATE -- Crée une date et la retourne, basée sur l'année donnée et les valeurs de nombre de jours.

MAKETIME -- Crée une heure et la retourne, basée sur les valeurs d'heure, de minute et de seconde données.

MICROSECOND -- Retourne la microseconde d'une heure ou d'une date/heure donnée.

MINUTE -- Retourne la minute de l'heure ou de la date/heure donnée.

MONTH -- Retourne le mois de la date donnée.

MONTHNAME -- Retourne le nom du mois de la date donnée.

NOW -- Identique à LOCALTIME.

PERIOD_ADD -- Ajoute le nombre de mois donné à la période donnée.

PERIOD_DIFF -- Retourne la différence entre deux périodes données.

QUARTER -- Retourne le trimestre de l'année pour la date donnée.

SECOND -- Retourne la seconde d'une heure ou d'une date/heure donnée.

SEC_TO_TIME -- Retourne une heure basée sur les secondes données.

STR_TO_DATE -- Crée une date et la retourne basée sur la chaîne et le format donnés.

SUBDATE -- Identique à DATE_SUB.

SUBTIME -- Soustrait un intervalle de temps (par exemple : 02:00) à une heure ou une date/heure (05:00) et retourne le résultat (03:00).

SYSDATE -- Identique à LOCALTIME.

TIME -- Retourne l'heure d'une heure ou d'une date/heure donnée.

TIME_FORMAT -- Retourne l'heure donnée dans le format donné.

TIME_TO_SEC -- Convertit et retourne une heure en secondes.

TIMEDIFF -- Retourne la différence entre deux expressions de temps/date/heure données.

TIMESTAMP -- Retourne la valeur de date/heure de la date ou de la date/heure donnée.

TO_DAYS -- Retourne le nombre total de jours qui se sont écoulés depuis '00-00-0000' jusqu'à la date donnée.

WEEK -- Retourne le numéro de semaine pour la date donnée.

WEEKDAY -- Retourne le numéro du jour de la semaine pour la date donnée.

WEEKOFYEAR -- Retourne le numéro de semaine pour la date donnée.

YEAR -- Retourne l'année de la date donnée.

YEARWEEK -- Retourne l'année et le numéro de semaine pour la date donnée.
```

#### 4. Fonctions diverses en SQL

```sql
BIN -- Retourne le nombre donné en binaire.

BINARY -- Retourne la valeur donnée sous forme de chaîne binaire.

CAST -- Convertit un type en un autre.

COALESCE -- À partir d'une liste de valeurs, retourne la première valeur non nulle.

CONNECTION_ID -- Pour la connexion actuelle, retourne l'ID de connexion unique.

CONV -- Convertit le nombre donné d'un système de base numérique à un autre.

CONVERT -- Convertit la valeur donnée dans le type de données ou le jeu de caractères donné.

CURRENT_USER -- Retourne l'utilisateur et le nom d'hôte qui ont été utilisés pour s'authentifier auprès du serveur.

DATABASE -- Obtient le nom de la base de données actuelle.

GROUP BY -- Utilisé avec des fonctions d'agrégation (COUNT, MAX, MIN, SUM, AVG) pour regrouper les résultats.

HAVING -- Utilisé à la place de WHERE avec des fonctions d'agrégation.

IF -- Si la condition est vraie, elle retourne une valeur, sinon elle retourne une autre valeur.

IFNULL -- Si l'expression donnée équivaut à null, elle retourne la valeur donnée.

ISNULL -- Si l'expression est nulle, elle retourne 1, sinon elle retourne 0.

LAST_INSERT_ID -- Pour la dernière ligne qui a été ajoutée ou mise à jour dans une table, retourne l'ID d'auto-incrément.

NULLIF -- Compare les deux expressions données. Si elles sont égales, NULL est retourné, sinon la première expression est retournée.

SESSION_USER -- Retourne l'utilisateur actuel et les noms d'hôte.

SYSTEM_USER -- Identique à SESSION_USER.

USER -- Identique à SESSION_USER.

VERSION -- Retourne la version actuelle de MySQL alimentant la base de données.
```

### Caractères génériques en SQL

En SQL, les caractères génériques sont des caractères spéciaux utilisés avec les mots-clés `LIKE` et `NOT LIKE`. Cela nous permet de rechercher des données avec des motifs sophistiqués de manière assez efficace.

```sql
% -- Équivaut à zéro ou plusieurs caractères.
-- Exemple : Trouver tous les clients dont les noms de famille se terminent par 'ory'.
SELECT * FROM customers
WHERE surname LIKE '%ory';

_ -- Équivaut à n'importe quel caractère unique.
-- Exemple : Trouver tous les clients vivant dans des villes commençant par n'importe quels 3 caractères, suivis de 'vale'.
SELECT * FROM customers
WHERE city LIKE '_ _ _vale';

[charlist] -- Équivaut à n'importe quel caractère unique dans la liste.
-- Exemple : Trouver tous les clients dont les prénoms commencent par J, K ou T.
SELECT * FROM customers
WHERE first_name LIKE '[jkt]%';
```

### Clés SQL

Dans les bases de données relationnelles, il existe un concept de clés *primaires* et *étrangères*. Dans les tables SQL, celles-ci sont incluses en tant que contraintes, où une table peut avoir une clé primaire, une clé étrangère, ou les deux.

#### 1. Clés primaires en SQL

Une clé primaire permet à chaque enregistrement dans une table d'être identifié de manière unique. Vous ne pouvez avoir qu'une seule clé primaire par table, et vous pouvez attribuer cette contrainte à n'importe quelle colonne unique ou combinaison de colonnes. Cependant, cela signifie que chaque valeur au sein de cette ou ces colonnes doit être unique.

Typiquement dans une table, la colonne ID est une clé primaire, et est généralement associée au mot-clé `AUTO_INCREMENT`. Cela signifie que la valeur augmente automatiquement au fur et à mesure que de nouveaux enregistrements sont créés.

#### Exemple (MySQL)

Créez une nouvelle table et définissez la clé primaire sur la colonne ID.

```sql
CREATE TABLE customers (
id int NOT NULL AUTO_INCREMENT,
FirstName varchar(255),
Last Name varchar(255) NOT NULL,
address varchar(255),
email varchar(255),
PRIMARY KEY (id)
);
```

#### 2. Clés étrangères en SQL

Vous pouvez appliquer une clé étrangère à une ou plusieurs colonnes. Vous l'utilisez pour *lier* 2 tables ensemble dans une base de données relationnelle.

La table contenant la clé étrangère est appelée la clé *enfant*,

La table contenant la clé référencée (ou candidate) est appelée la table *parente*.

Cela signifie essentiellement que les données de la colonne sont partagées entre 2 tables, car une clé étrangère empêche également l'insertion de données invalides qui ne sont pas également présentes dans la table parente.

#### Exemple (MySQL)

Créez une nouvelle table et transformez toute colonne qui référence les ID dans d'autres tables en clés étrangères.

```sql
CREATE TABLE orders (
id int NOT NULL,
user_id int,
product_id int,
PRIMARY KEY (id),
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### Index en SQL

Les index sont des attributs qui peuvent être assignés aux colonnes qui sont fréquemment recherchées pour rendre la récupération des données plus rapide et plus efficace.

```sql
CREATE INDEX -- Crée un index nommé 'idx_test' sur les colonnes first_name et surname de la table users. Dans ce cas, les valeurs en double sont autorisées.
CREATE INDEX idx_test
ON users (first_name, surname);
CREATE UNIQUE INDEX -- Identique à ci-dessus, mais sans valeurs en double.
CREATE UNIQUE INDEX idx_test
ON users (first_name, surname);
DROP INDEX -- Supprime un index.
ALTER TABLE users
DROP INDEX idx_test;
```

### Jointures SQL

En SQL, une clause `JOIN` est utilisée pour retourner un résultat qui combine des données de plusieurs tables, sur la base d'une colonne commune qui est présente dans les deux.

Il existe plusieurs types de jointures disponibles pour vous :

* **Inner Join (Par défaut)** : Retourne tous les enregistrements qui ont des valeurs correspondantes dans les deux tables.

* **Left Join** : Retourne tous les enregistrements de la première table, ainsi que tous les enregistrements correspondants de la deuxième table.

* **Right Join** : Retourne tous les enregistrements de la deuxième table, ainsi que tous les enregistrements correspondants de la première.

* **Full Join** : Retourne tous les enregistrements des deux tables lorsqu'il y a une correspondance.

Une manière courante de visualiser le fonctionnement des jointures est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-56.png align="left")

[*Source*](https://websitesetup.org/sql-cheat-sheet/)*: Website Setup*

```sql
SELECT orders.id, users.FirstName, users.Surname, products.name as 'product name'
FROM orders
INNER JOIN users on orders.user_id = users.id
INNER JOIN products on orders.product_id = products.id;
```

### Vues en SQL

Une vue est essentiellement un ensemble de résultats SQL qui est stocké dans la base de données sous une étiquette, afin que vous puissiez y revenir plus tard sans avoir à réexécuter la requête.

Celles-ci sont particulièrement utiles lorsque vous avez une requête SQL coûteuse que vous pourriez avoir besoin plusieurs fois. Ainsi, au lieu de l'exécuter encore et encore pour générer le même ensemble de résultats, vous pouvez simplement le faire une fois et l'enregistrer sous forme de vue.

#### Comment créer des vues en SQL

Pour créer une vue, vous pouvez le faire comme suit :

```sql
CREATE VIEW priority_users AS
SELECT * FROM users
WHERE country = 'United Kingdom';
```

Ensuite, si vous avez besoin d'accéder à l'ensemble de résultats stocké, vous pouvez le faire comme suit :

```sql
SELECT * FROM [priority_users];
```

#### Comment remplacer des vues en SQL

Avec la commande `CREATE OR REPLACE`, vous pouvez mettre à jour une vue comme suit :

```sql
CREATE OR REPLACE VIEW [priority_users] AS
SELECT * FROM users
WHERE country = 'United Kingdom' OR country='USA';
```

#### Comment supprimer des vues en SQL

Pour supprimer une vue, utilisez simplement la commande `DROP VIEW`.

```sql
DROP VIEW priority_users;
```

## Conclusion

La majorité des sites web et des applications utilisent des bases de données relationnelles d'une manière ou d'une autre. Cela rend SQL extrêmement précieux à connaître, car il vous permet de créer des systèmes plus complexes et fonctionnels.

Bon apprentissage !