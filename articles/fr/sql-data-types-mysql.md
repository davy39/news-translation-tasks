---
title: Types de données SQL expliqués et exemples de syntaxe MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-24T23:18:00.000Z'
originalURL: https://freecodecamp.org/news/sql-data-types-mysql
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/sql-data-types.jpeg
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Types de données SQL expliqués et exemples de syntaxe MySQL
seo_desc: 'SQL Data Types

  Each column in a database table is required to have a name and a data type.

  An SQL developer must decide what type of data that will be stored inside each column
  when creating a table. The data type is a guideline for SQL to understand...'
---

# Types de données SQL

Chaque colonne dans une table de base de données doit avoir un nom et un type de données.

Un développeur SQL doit décider quel type de données sera stocké dans chaque colonne lors de la création d'une table. Le type de données est une directive pour SQL afin de comprendre quel type de données est attendu dans chaque colonne, et il identifie également comment SQL interagira avec les données stockées.

# Types de données MySQL

Les types de données généraux SQL se composent des éléments suivants :

1. Une valeur basée sur du texte et/ou des chiffres, souvent appelée CHAÎNE
2. Une valeur numérique uniquement, souvent appelée ENTIER
3. Une valeur basée sur un calendrier et/ou une horloge, souvent appelée DATE ou HEURE
4. Une valeur spécifique à la base de données telle qu'un booléen (drapeau à deux options), un tableau qui stocke plusieurs valeurs dans un seul point de données

## Types de données texte :

|Type de données|Description|
| --- | --- |
|CHAR(taille)|Contient une chaîne de longueur fixe (peut contenir des lettres, des chiffres et des caractères spéciaux). La taille fixe est spécifiée entre parenthèses. Peut stocker jusqu'à 255 caractères|
|VARCHAR(taille)|Contient une chaîne de longueur variable (peut contenir des lettres, des chiffres et des caractères spéciaux). La taille maximale est spécifiée entre parenthèses. Peut stocker jusqu'à 255 caractères. Remarque : Si vous mettez une valeur supérieure à 255, elle sera convertie en type TEXTE|
|TINYTEXT|Contient une chaîne avec une longueur maximale de 255 caractères|
|TEXT|Contient une chaîne avec une longueur maximale de 65 535 caractères|
|BLOB|Pour les BLOB (Binary Large OBjects). Contient jusqu'à 65 535 octets de données|
|MEDIUMTEXT|Contient une chaîne avec une longueur maximale de 16 777 215 caractères|
|MEDIUMBLOB|Pour les BLOB (Binary Large OBjects). Contient jusqu'à 16 777 215 octets de données|
|LONGTEXT|Contient une chaîne avec une longueur maximale de 4 294 967 295 caractères|
|LONGBLOB|Pour les BLOB (Binary Large OBjects). Contient jusqu'à 4 294 967 295 octets de données|
|ENUM(x,y,z,etc.)|Permet d'entrer une liste de valeurs possibles. Vous pouvez lister jusqu'à 65 535 valeurs dans une liste ENUM. Si une valeur est insérée qui n'est pas dans la liste, une valeur vide sera insérée. Remarque : Les valeurs sont triées dans l'ordre où vous les entrez. Vous entrez les valeurs possibles dans ce format : ENUM('X','Y','Z')|
|SET|Similaire à ENUM sauf que SET peut contenir jusqu'à 64 éléments de liste et peut stocker plus d'un choix|

# Types de données numériques :

|Type de données|Description|
| --- | --- |
|TINYINT(taille)|-128 à 127 normal. 0 à 255 UNSIGNED*. Le nombre maximum de chiffres peut être spécifié entre parenthèses|
|SMALLINT(taille)|-32768 à 32767 normal. 0 à 65535 UNSIGNED*. Le nombre maximum de chiffres peut être spécifié entre parenthèses|
|MEDIUMINT(taille)|-8388608 à 8388607 normal. 0 à 16777215 UNSIGNED*. Le nombre maximum de chiffres peut être spécifié entre parenthèses|
|INT(taille)|-2147483648 à 2147483647 normal. 0 à 4294967295 UNSIGNED*. Le nombre maximum de chiffres peut être spécifié entre parenthèses|
|BIGINT(taille)|-9223372036854775808 à 9223372036854775807 normal. 0 à 18446744073709551615 UNSIGNED*. Le nombre maximum de chiffres peut être spécifié entre parenthèses|
|FLOAT(taille,d)|Un petit nombre avec un point décimal flottant. Le nombre maximum de chiffres peut être spécifié dans le paramètre taille. Le nombre maximum de chiffres à droite du point décimal est spécifié dans le paramètre d|
|DOUBLE(taille,d)|Un grand nombre avec un point décimal flottant. Le nombre maximum de chiffres peut être spécifié dans le paramètre taille. Le nombre maximum de chiffres à droite du point décimal est spécifié dans le paramètre d|
|DECIMAL(taille,d)|Un DOUBLE stocké sous forme de chaîne, permettant un point décimal fixe. Le nombre maximum de chiffres peut être spécifié dans le paramètre taille. Le nombre maximum de chiffres à droite du point décimal est spécifié dans le paramètre d|

# Types de données de date :

|Type de données|Description|
| --- | --- |
|DATE()|Une date. Format : AAAA-MM-JJ Remarque : La plage prise en charge est de '1000-01-01' à '9999-12-31'|
|DATETIME()|Une combinaison de date et d'heure. Format : AAAA-MM-JJ HH:MI:SS Remarque : La plage prise en charge est de '1000-01-01 00:00:00' à '9999-12-31 23:59:59'|
|TIMESTAMP()|Un timestamp. Les valeurs TIMESTAMP sont stockées sous forme de nombre de secondes depuis l'époque Unix ('1970-01-01 00:00:00' UTC). Format : AAAA-MM-JJ HH:MI:SS Remarque : La plage prise en charge est de '1970-01-01 00:00:01' UTC à '2038-01-09 03:14:07' UTC|
|TIME()|Une heure. Format : HH:MI:SS Remarque : La plage prise en charge est de '-838:59:59' à '838:59:59'|
|YEAR()|Une année en format à deux ou quatre chiffres. Remarque : Valeurs autorisées en format à quatre chiffres : 1901 à 2155. Valeurs autorisées en format à deux chiffres : 70 à 69, représentant les années de 1970 à 2069|

Enfin, il existe quelques autres types de données que vous utiliserez :

### Autres types de données

|Type de données|Description|
| --- | --- |
|`BOOLEAN`|Stocke les valeurs `VRAI` ou `FAUX`|
|`ARRAY`|Une collection ordonnée d'éléments de longueur fixe|
|`MULTISET`|Une collection non ordonnée d'éléments de longueur variable|
|`XML`|Stocke les données XML|