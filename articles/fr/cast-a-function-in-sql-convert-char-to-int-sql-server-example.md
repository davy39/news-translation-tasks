---
title: Convertir une fonction en SQL – Convertir Char en Int Exemple SQL Server
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-08T19:35:48.000Z'
originalURL: https://freecodecamp.org/news/cast-a-function-in-sql-convert-char-to-int-sql-server-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Cast-a-Function-in-SQL
seo_title: Convertir une fonction en SQL – Convertir Char en Int Exemple SQL Server
---

Convert-Char-to-Int-SQL-Server-Example.png
tags:
- name: base de données
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "La conversion d'un type de données à un autre est une opération courante que vous effectuerez lorsque vous travaillerez avec des bases de données. Et SQL fournit une utilité connue sous le nom de CAST pour y parvenir. Nous verrons comment cela fonctionne dans cet article. Qu'est-ce que la fonction CAST en SQL ? CAST ..."
---

La conversion d'un type de données à un autre est une opération courante que vous effectuerez lorsque vous travaillerez avec des bases de données.

Et SQL fournit une utilité connue sous le nom de CAST pour y parvenir. Nous verrons comment cela fonctionne dans cet article.

## Qu'est-ce que la fonction CAST en SQL ?

CAST nous permet de convertir d'un type de données à un autre. Il est très utile pour concaténer des résultats de différents types de données. Il nous aide également à effectuer des calculs sur deux types de données différents.

CAST ne modifie pas les données dans la base de données. La conversion n'est valide que pendant la durée de vie de la requête. Mais il est possible de convertir et d'insérer dans une nouvelle colonne ou table.

### Syntaxe de CAST en SQL

Voici la syntaxe de la fonction CAST :

```sql
CAST ( expression AS data_type [ ( length ) ])
```

Où,

* `expression` est la requête telle que : `id as VARCHAR`
* `data_type` est le type de données cible.
* `length` détermine la longueur du type de données cible. Cette partie est facultative.

## Comment utiliser la fonction CAST en SQL

### Tableau d'exemple

Créons une table `store_locations` comme indiqué ci-dessous :

```sql
-- créer une table nommée store_locations

CREATE TABLE store_locations (
  id INTEGER PRIMARY KEY,
  store_name VARCHAR(10) NOT NULL,
  store_id INTEGER NOT NULL,
  postal_code VARCHAR(10)
);

```

Où,

* `id` est la clé primaire.
* `store_name` est le nom du magasin avec le type de données `VARCHAR`.
* `store_id` est l'ID du magasin et un `INTEGER`.
* `postal_code` est l'adresse postale du magasin avec le type `VARCHAR`.

Après avoir inséré quelques valeurs, notre table ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-24.png)
_table store_locations_

### Comment convertir `char` en `int` en SQL

Examinons un exemple de conversion du type de données char (VARCHAR) en int.

Dans notre exemple, notre tâche consiste à générer une nouvelle colonne qui additionne (somme) le `store_id` et le `postal_code` pour générer un autre ID unique.

Rappelons que `store_id` est un `INTEGER`, tandis que `postal_code` est `VARCHAR`. Pour convertir `postal_code` en entier, nous pouvons utiliser CAST comme ceci :

```sql
-- convertir char en int
-- générer un nouvel id en ajoutant l'id du magasin et le code postal

select store_id, postal_code, store_id + cast(postal_code AS INTEGER) AS [StoreID-Postalcode] from store_locations


```

**Sortie** :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-25.png)
_Combinaison des colonnes store_id et postal_code_

### Comment convertir `int` en `char` en SQL

Dans cet exemple, notre objectif est de combiner deux colonnes – `store_name` et `store_id` – pour générer une nouvelle colonne.

Rappelons que `store_name` est un `VARCHAR`, tandis que `store_id` est un `INTEGER`.

Si nous essayons d'ajouter `int` et `char` sans conversion, quel serait le résultat ?

Nous obtiendrions une exception comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-26.png)
_Exception de conversion de type_

Faisons une conversion et voyons les résultats.

```bash
-- conversion de int en char
-- nom du magasin + ID du magasin

select store_name, store_id, store_name + ' - ' + cast(store_id AS VARCHAR) AS [Storename-storeId]
from store_locations
```

**Sortie** :

Nous pouvons voir que notre sortie a été concaténée sans erreur.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-27.png)

## Conclusion

La fonction CAST est très utile pour convertir des types de données et effectuer des calculs complexes.

N'hésitez pas à essayer ces commandes et à expérimenter avec différents types de données comme 'date'.