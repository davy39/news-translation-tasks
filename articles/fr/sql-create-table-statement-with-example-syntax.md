---
title: Instruction SQL CREATE TABLE - Avec la syntaxe d'exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-21T15:58:38.000Z'
originalURL: https://freecodecamp.org/news/sql-create-table-statement-with-example-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/fabio-oyXis2kALVg-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Instruction SQL CREATE TABLE - Avec la syntaxe d'exemple
seo_desc: 'By Jonathan Sexton

  SQL is one of the most reliable and straightforward querying languages around. It
  provides clear cut syntax that reads easily without abstracting away too much of
  the functionality''s meaning.

  If you''d like some history on the langu...'
---

Par Jonathan Sexton

SQL est l'un des langages de requête les plus fiables et les plus simples disponibles. Il offre une syntaxe claire qui se lit facilement sans trop abstraire la signification de la fonctionnalité.

Si vous souhaitez en savoir plus sur l'histoire du langage ainsi que quelques faits intéressants, consultez la partie introduction de mon [article sur l'instruction SQL UPDATE](https://www.freecodecamp.org/news/sql-update-statement-example-queries-for-updating-table-values/).  

Dans cet article, nous allons passer en revue les parties importantes de la création d'une table en SQL. Ma "version" préférée de SQL est SQL Server, mais les informations sur la création d'une table sont assez universelles dans toutes les variations de SQL.  

Si vous n'avez jamais utilisé SQL ou ne savez pas ce qu'est une table, ne vous inquiétez pas ! Brièvement (et de manière générale), une table est un objet de base de données qui contient toutes les données de cette partie de la base de données. Elle stocke ces données dans des colonnes nommées et des lignes numérotées, ce qui n'est pas inconnu si vous avez déjà utilisé un programme de tableur. Chaque ligne représente un enregistrement complet de la base de données.

Si les données étaient sous forme de boîte, alors une table serait une section des étagères de l'entrepôt où nous stockons ces boîtes.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/nana-smirnova-IEiAmhXehwE-unsplash.jpg)
_Photo par [Unsplash](https://unsplash.com/@nananadolgo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Nana Smirnova</a> sur <a href="https://unsplash.com/s/photos/warehouse?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

Je simplifie grandement l'explication et il y a beaucoup plus à dire sur les tables SQL, mais cela dépasse le cadre de cet article. Si vous avez envie d'une explication plus approfondie sur les tables, je vous encourage à plonger dans la [documentation Microsoft sur la conception de bases de données](https://docs.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver15).

Avant d'apprendre à créer la table, il est important que nous apprenions quels types de données ces colonnes et lignes peuvent stocker.

## Types de données

Les tables SQL peuvent contenir du texte, des nombres, une combinaison de texte et de nombres, ainsi que des images et des liens.

Lors de la création de notre table, nous désignons le type de données que ses lignes et colonnes contiendront. Voici les classifications générales des données :

- Numériques approximatifs
- Chaînes de caractères
- Date et heure
- Chaînes de caractères Unicode
- Numériques exacts
- Autres

Je vais lister ci-dessous certains des types de données les plus couramment utilisés, mais si vous souhaitez en savoir plus sur tous les types de données, je vous invite à consulter cet [article exhaustif sur chaque type de Microsoft](https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver15). 

Voici les types de données les plus couramment utilisés selon mon expérience, dans aucun ordre particulier :

- char(taille) - chaîne de longueur *fixe* qui peut contenir des lettres, des nombres, des caractères spéciaux
- varchar(taille) - chaîne de longueur *variable* qui peut contenir des lettres, des nombres et des caractères spéciaux
- boolean - Zéro (ou valeurs équivalentes à 0) est faux, non-zéro est vrai
- int(*taille optionnelle*) - un nombre jusqu'à 10 caractères de long, accepte les nombres négatifs et positifs
- bigint(*taille optionnelle*) - un nombre jusqu'à 19 caractères de long, accepte les nombres négatifs et positifs
- float(taille, d) - un nombre avec une taille totale représentée par taille et le nombre de caractères après la virgule représenté par *d*
- date - date au format *AAAA-MM-JJ*
- datetime - date et heure au format *AAAA-MM-JJ hh:mm:ss*
- time - heure au format *hh:mm:ss*

Très bien, maintenant que nous savons quels types de données les lignes et colonnes peuvent contenir, passons aux parties amusantes !

## Création d'une table

![Image](https://www.freecodecamp.org/news/content/images/2020/07/nikhil-mitra-Q_6BS8IN0J8-unsplash.jpg)
_Photo par [Unsplash](https://unsplash.com/@nikhilmitra?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Nikhil Mitra</a> sur <a href="https://unsplash.com/s/photos/create?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

Avant de commencer, il est important de noter que je fournirai tous mes exemples indépendamment de tout programme. 

Cependant, si vous souhaitez commencer à écrire des requêtes et que vous n'êtes pas sûr de par où commencer, regardez [SQL Server Management Studio.](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15) C'est un programme gratuit et robuste, largement utilisé et soutenu par la communauté.

Alternativement, il existe plusieurs options, y compris [DB Fiddle](https://www.db-fiddle.com/), qui vous permettent de construire des schémas et d'écrire des requêtes directement dans votre navigateur.  

Commençons par une instruction simple pour créer une table de base :

```sql
CREATE TABLE nom_table (
    nom_colonne1 type_donnee, 
    nom_colonne2 type_donnee,
    nom_colonne3 type_donnee,
    nom_colonne4 type_donnee,
    nom_colonne5 type_donnee,
)
```

Il existe d'autres paramètres que nous pouvons ajouter après le `type_donnee` pour augmenter les colonnes :

- `NOT NULL` - passer ce paramètre garantira que la colonne ne peut pas contenir une valeur `NULL`
- `UNIQUE` - passer ce paramètre empêchera la colonne de contenir la même valeur plus d'une fois
- `UNIQUE KEY` - passer ce paramètre désignera cette colonne comme un identifiant unique. C'est essentiellement une combinaison des deux paramètres précédents.

Maintenant, nous allons créer une table (nommée doggo_info qui doit adhérer aux [normes d'identifiants pour les bases de données](https://docs.microsoft.com/en-us/sql/relational-databases/databases/database-identifiers?view=sql-server-ver15)) pour contenir des informations sur les résidents de Woof Woof Retreat, une garderie pour chiens fictive que je viens d'imaginer :)

```sql
CREATE TABLE doggo_info (
ID int UNIQUE KEY,
Name varchar(50) NOT NULL, 
Color varchar(50), 
Breed varchar(50), 
Age int, 
Weight int, 
Height int, 
Fav_Food varchar(100), 
Fav_Toy varchar(100), 
Dislikes varchar(500), 
Allergies varchar(500) NOT NULL
    )
```

Et voici la toute nouvelle table que nous venons de créer :

<table>
    <tr style="font-weight: bold;">
      <td>Name</td>
      <td>Color</td>
      <td>Breed</td>
      <td>Age</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Fav_Food</td>
      <td>Fav_Toy</td>
      <td>Dislikes</td>
      <td>Allergies</td>
    </tr>
    <tr>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
</table>

Vous remarquerez que notre table est complètement vide et cela est dû au fait que nous n'avons pas encore ajouté de données. Cela dépasse le cadre de cet article, mais je voulais que vous soyez conscient de ce détail.

### Créer une table à partir d'une table existante

Il est également possible de créer une nouvelle table basée sur une table existante.

C'est assez facile et ne nécessite pas beaucoup plus de syntaxe. Nous devons sélectionner la table et les colonnes à "copier" :

```sql
CREATE TABLE nouveau_nom_table AS
SELECT colonne1, colonne2, colonne3, colonne4 (utilisez * pour sélectionner toutes les colonnes à ajouter à la nouvelle_table)
FROM nom_table_actuelle
WHERE conditions_existent
```

Pour l'efficacité, j'ai ajouté quelques données à notre table `doggo_info` et elle ressemble maintenant à l'exemple ci-dessous :

<table>
  <th>
    <tr style="font-weight: bold;">
      <td>Name</td>
      <td>Color</td>
      <td>Breed</td>
      <td>Age</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Fav_Food</td>
      <td>Fav_Toy</td>
      <td>Dislikes</td>
      <td>Allergies</td>
    </tr>
  </th>
  <tbody>
    <tr>
      <td>daisy</td>
      <td>red</td>
      <td>standard dachshund</td>
      <td>1</td>
      <td>14</td>
      <td>6</td>
      <td>salmon flavored kibble</td>
      <td>squeeky ball</td>
      <td>birds flying over the yard</td>
      <td>cats, baths, cleanliness</td>
    </tr>
    <tr>
      <td>chief</td>
      <td>black/tan</td>
      <td>rottweiler</td>
      <td>3</td>
      <td>41</td>
      <td>17</td>
      <td>literally anything</td>
      <td>rope tug</td>
      <td>staying off the couch</td>
      <td>listening, behaving, not slobbering on everything</td>
    </tr>
    <tr>
      <td>sammie</td>
      <td>light honey</td>
      <td>golden retriever</td>
      <td>9</td>
      <td>46</td>
      <td>19</td>
      <td>beef flavored kibble</td>
      <td>her bed</td>
      <td>rambutcious puppies</td>
      <td>none known</td>
    </tr>
  </tbody>
</table>

Maintenant, nous pouvons créer une autre table basée sur les données que nous avons dans notre table `doggo_info` en exécutant la requête suivante :

```sql
CREATE TABLE puppies_only AS
SELECT *
FROM doggo_info
WHERE Age < 4
```

Nous voulons créer une nouvelle table avec toutes les colonnes de la table `doggo_info`, mais seulement où l'`Age` est inférieur à 4. Après avoir exécuté cette requête, notre nouvelle table ressemblera à ceci :

<table>
  <th>
    <tr style="font-weight: bold;">
      <td>Name</td>
      <td>Color</td>
      <td>Breed</td>
      <td>Age</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Fav_Food</td>
      <td>Fav_Toy</td>
      <td>Dislikes</td>
      <td>Allergies</td>
    </tr>
  </th>
  <tbody>
    <tr>
      <td>daisy</td>
      <td>red</td>
      <td>standard dachshund</td>
      <td>1</td>
      <td>14</td>
      <td>6</td>
      <td>salmon flavored kibble</td>
      <td>squeeky ball</td>
      <td>birds flying over the yard</td>
      <td>cats, baths, cleanliness</td>
    </tr>
    <tr>
      <td>chief</td>
      <td>black/tan</td>
      <td>rottweiler</td>
      <td>3</td>
      <td>41</td>
      <td>17</td>
      <td>literally anything</td>
      <td>rope tug</td>
      <td>staying off the couch</td>
      <td>listening, behaving, not slobbering on everything</td>
    </tr>
  </tbody>
</table>

J'espère que vous pouvez voir à quel point cette instruction peut être puissante. Avec quelques lignes dans notre requête, nous avons essentiellement copié des données d'une table à une autre, mais seulement les lignes que nous voulions.  

Ce n'est pas seulement un outil pratique à avoir dans votre boîte à outils de développeur, il vous fera gagner des quantités incalculables de temps lorsque vous devrez déplacer des données entre les tables.

## Conclusion

Maintenant que vous savez comment créer (ou copier) une table en SQL, peu importe la situation qui se présente à vous, vous pouvez commencer à remplir les colonnes et les lignes avec des données à stocker !

L'instruction `CREATE TABLE` est extrêmement utile et puissante. Vous êtes prêt à commencer à l'utiliser à bon escient.

Si vous avez trouvé cet article utile, consultez mon [blog](https://jonathansexton.me/blog) où je publie fréquemment des articles sur le développement web, la vie et l'apprentissage.

Pendant que vous y êtes, pourquoi ne pas vous inscrire à ma newsletter ? Vous pouvez le faire en haut à droite de la page principale du blog. J'aime envoyer des articles intéressants (les miens et ceux des autres), des ressources et des outils pour les développeurs de temps en temps.

Si vous avez des questions sur cet article ou simplement en général, faites-le moi savoir, venez dire bonjour sur [Twitter](https://twitter.com/jj_goose) ou sur l'un de mes autres comptes de réseaux sociaux que vous pouvez trouver sous l'inscription à la newsletter sur la page principale de mon blog ou sur mon profil ici chez fCC :)

Passez une journée géniale ! Bon apprentissage et bon codage, ami !