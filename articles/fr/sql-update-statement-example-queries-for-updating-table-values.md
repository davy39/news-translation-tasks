---
title: Instruction SQL UPDATE — Exemples de requêtes pour mettre à jour les valeurs
  de table
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-26T16:20:52.000Z'
originalURL: https://freecodecamp.org/news/sql-update-statement-example-queries-for-updating-table-values
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/markus-winkler-cxoR55-bels-unsplash.jpg
tags:
- name: SQL
  slug: sql
seo_title: Instruction SQL UPDATE — Exemples de requêtes pour mettre à jour les valeurs
  de table
seo_desc: 'By Jonathan Sexton

  SQL (pronounced Seequel) stands for Structured Query Language. It is a strongly
  typed, static (types are checked before runtime) querying language that first appeared
  in 1974 (woah, 46 years old!), but was not initially released un...'
---

Par Jonathan Sexton

SQL (prononcé Seequel) signifie Structured Query Language. C'est un langage de requête [fortement typé](https://en.wikipedia.org/wiki/Strong_and_weak_typing), statique (les types sont vérifiés avant l'exécution) qui est apparu pour la première fois en 1974 (woah, 46 ans !), mais qui n'a été initialement publié qu'en 1986. 

Vous pourriez penser qu'un outil aussi "ancien" a ses meilleurs jours derrière lui, mais vous auriez tort. En 2019, selon l'enquête [DeveloperWeek](https://scalegrid.io/blog/2019-database-trends-sql-vs-nosql-top-databases-single-vs-multiple-database-use/) de Scale Grid, SQL était utilisé par 60,5 % des répondants, tandis que [NoSQL](https://en.wikipedia.org/wiki/NoSQL) n'était utilisé que par 39,5 % des répondants.

Pour être clair, la catégorie SQL a été divisée en plusieurs sous-catégories incluant [MySQL](https://en.wikipedia.org/wiki/MySQL), [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL), [SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server), et ainsi de suite, tandis que la catégorie NoSQL a été divisée en sous-catégories contenant [MongoDB](https://en.wikipedia.org/wiki/MongoDB), [Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra), etc.

Même en 2017, selon l'enquête [Stack Overflow Developer's Survey](https://insights.stackoverflow.com/survey/2017), le deuxième langage le plus populaire utilisé était SQL (juste derrière JavaScript) avec 50 % des 64 000 répondants déclarant qu'ils utilisaient encore SQL sous une forme ou une autre.

Sa popularité est due, au moins en partie, à la simplicité du langage, au fait qu'il a été conçu en pensant aux données relationnelles, et parce qu'il s'est avéré fiable pour la recherche, la jointure et le filtrage des données.

Il suffit de dire que SQL n'est pas seulement vivant et bien vivant, mais qu'il prospère au sein de la communauté de développement d'aujourd'hui.

Maintenant, voyons pourquoi !

<h2>Les parties amusantes</h2>	

SQL Server est la version préférée de SQL que j'utilise dans mes activités quotidiennes au travail, donc les exemples ci-dessous se conformeront à ces normes. 

Une chose que je fais beaucoup est la mise à jour de plusieurs enregistrements dans une table. Maintenant, je pourrais le faire un enregistrement à la fois, mais SQL nous donne la possibilité de mettre à jour plusieurs (des milliers et des milliers si nécessaire) enregistrements à la fois grâce à l'instruction `UPDATE`.

L'instruction `UPDATE` peut être utilisée pour mettre à jour une seule colonne, un ensemble plus grand d'enregistrements (grâce à l'utilisation de conditions), et/ou la table entière dans une base de données. La ou les conditions peuvent être un booléen, une vérification de chaîne, ou une séquence mathématique qui se résout en un booléen (supérieur à, inférieur à, etc.).

Bien que cela puisse varier légèrement d'une version à l'autre, la syntaxe générale est la suivante :

<code><strong>UPDATE</strong> <em>nom-de-table</em><br />
<strong>SET</strong> <em>nom-de-colonne = valeur[, nom-de-colonne=valeur]</em><br />
[<strong>WHERE</strong> <em>condition</em>]</code>

Les crochets ( [] ) ci-dessus désignent des ajouts optionnels à la requête. 

**<ins>***Il est très important de noter que sans condition `WHERE`, TOUS les enregistrements de la table seront mis à jour dès que vous exécuterez la requête.***</ins>**

<h2 id="heading-installation">Exemples de requêtes</h2>

Pour notre ensemble de données, j'utiliserai cette table nommée _**Work_Tickets**_ :

<table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
            <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
            <td>1250</td> 
              <td>sales@wayneindustries.com</td>
            <td>0.00</td>
            <td>False</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>  
              <td>contact@starkindustries.com</td>
            <td>0.00</td>
            <td>False</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>0.00</td>
            <td>False</td>
            <td>085569</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

<h4>Requête simple sans conditions</h4>

Voici une requête de mise à jour très simple qui changera tous les champs `UnitCost` en `131.6152` :

`UPDATE Work_Tickets`   
`SET UnitCost = 131.6152`   


Notez qu'il n'y a pas de clause `WHERE`, donc chaque ligne de la table sera mise à jour et notre ensemble de données ressemblera maintenant à ceci :

    <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>False</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>False</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>131.6152</td>
            <td>False</td>
            <td>085569</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

<h4 id="simple_query_condition">Requêtes simples avec condition(s)</h4>

Voici une requête simple avec une instruction conditionnelle :

<code>UPDATE Work_Tickets<br />SET Billed = true<br />WHERE UnitCost <> 0.00</code>


Cette requête mettra à jour le champ `Billed` à _true_ sur chaque ligne qui correspond à la condition où `UnitCost` n'est pas égal à 0. Après avoir exécuté notre requête, l'ensemble de données ressemblera à ceci :

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085569</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

Voici une requête où nous changeons le `ParentLineKey` en la chaîne `000134` où le `SalesOrderNum` et le `WorkTicketNum` correspondent tous deux aux chaînes données.

<code>UPDATE Work_Tickets <br />SET ParentLineKey = 000134 <br />WHERE SalesOrderNum = 00061358 and WorkTicketNumber = 000933</code>

Ainsi, le 085569 dans le champ `ParentLineKey` sera remplacé par `000134` et notre ensemble de données ressemble maintenant à ceci :

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
            <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>000134</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

<h4>Mise à jour de plusieurs champs</h4>

Imaginons que vous avez un ensemble de données beaucoup plus grand que celui que nous utilisons actuellement et que vous avez plusieurs champs à mettre à jour. 

Il serait fastidieux et ennuyeux de les mettre à jour avec différentes instructions de mise à jour. Heureusement pour nous, il est également possible de mettre à jour plusieurs champs à la fois avec une instruction de mise à jour, tant que nous séparons les noms de colonnes par une virgule :

<code>UPDATE Work_Tickets <br />SET UnitCost = 129.8511, Qty_Ordered = 72, Qty_Shipped = 72 <br />WHERE SalesOrderNum = 00061358</code>

Et voici le résultat avec les champs mis à jour après l'exécution de la requête :

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>129.8511</td>
            <td>True</td>
            <td>000134</td>
            <td>72</td>
            <td>72</td>
          </tr>
        </tbody>
      </table>

<h4>Utilisation de Update dans une sous-requête</h4>

Les exemples ci-dessus sont parfaits si vous travaillez avec une seule source de données. Cependant, la plupart de vos données ne seront pas stockées dans une seule table. C'est là que l'utilisation de _UPDATE_ avec plusieurs sources de données devient pratique.

La syntaxe pour mettre à jour une colonne/table change un peu si nous voulons importer des données d'une autre table :

<code><strong>UPDATE</strong> <em>nom-de-table</em><br />
<strong>SET</strong> <em>nom-de-colonne = (SELECT nom-de-colonne(s) <br />  FROM nom-de-table2<br />  WHERE condition(s))</em><br />
[<strong>WHERE</strong> <em>condition</em>]</code>

Et voici les deux tables que nous utiliserons pour cette requête - la **table _Work_Tickets_** :

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>129.8511</td>
            <td>True</td>
            <td>000134</td>
            <td>72</td>
            <td>72</td>
          </tr>
        </tbody>
      </table>

et la **table _Customer_Info_** :

<table>
        <th>
          <tr>
            <td><strong>Name</strong></td>
            <td><strong>Industry</strong></td>
            <td><strong>Code</strong></td>
            <td><strong>Address</strong></td>
              <td><strong>City</strong></td>
            <td><strong>Discount</strong></td>
            <td><strong>PhoneNumber</strong></td>
            <td><strong>Email</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>Wayne Enterprises</td>
            <td>Defense,weaponry,aerospace,enginerring</td>
            <td>NULL</td>
            <td>1631 Dark Knight Way</td>
            <td>Gotham</td>
            <td>19.75</td>
            <td>5556614000</td>
              <td>sales@wayneindustires.com</td>
          </tr>
          <tr>
            <td>Stark Industries</td>
            <td>Defense,weaponry,protection</td>
              <td>1251</td>
            <td>5641 Iron Dr</td>
            <td>Undisclosed</td>
            <td>19.73</td>
            <td>9993126156</td>
            <td>contact@starkindustries.com</td>
          </tr>
          <tr>
            <td>Acme Corp</td>
            <td>Comedy,laughter,animation</td>
            <td>1252</td>
            <td>24569 Smiling St</td>
            <td>Toon Town</td>
            <td>17.53</td>
            <td>3216549877</td>
              <td>animation@acmetoons.com
          </tr>
        </tbody>
      </table>

L'instruction `UPDATE` avec une [sous-requête](https://docs.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver15) ressemble à ceci :

<code>UPDATE Customer_Info<br />SET Code = (SELECT Customer_Code<br />  FROM Work_Tickets<br />  WHERE Work_Tickets.Customer_Contact = Customer_Info.Email)  <br />FROM Work_Tickets<br />WHERE Code IS NULL</code>

Cet exemple mettra à jour le champ _Code_ de la table _Customer_Info_ où les adresses e-mail correspondent dans les deux tables. Et voici à quoi ressemble maintenant notre table _Customer_Info_ :

<table>
        <th>
          <tr>
            <td><strong>Name</strong></td>
            <td><strong>Industry</strong></td>
            <td><strong>Code</strong></td>
            <td><strong>Address</strong></td>
              <td><strong>City</strong></td>
            <td><strong>Discount</strong></td>
            <td><strong>PhoneNumber</strong></td>
            <td><strong>Email</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>Wayne Enterprises</td>
            <td>Defense,weaponry,aerospace,enginerring</td>
            <td>1250</td>
            <td>1631 Dark Knight Way</td>
            <td>Gotham</td>
            <td>19.75</td>
            <td>5556614000</td>
              <td>sales@wayneindustires.com</td>
          </tr>
          <tr>
            <td>Stark Industries</td>
            <td>Defense,weaponry,protection</td>
              <td>1251</td>
            <td>5641 Iron Dr</td>
            <td>Undisclosed</td>
            <td>19.73</td>
            <td>9993126156</td>
            <td>contact@starkindustries.com</td>
          </tr>
          <tr>
            <td>Acme Corp</td>
            <td>Comedy,laughter,animation</td>
            <td>1252</td>
            <td>24569 Smiling St</td>
            <td>Toon Town</td>
            <td>17.53</td>
            <td>3216549877</td>
              <td>animation@acmetoons.com
          </tr>
        </tbody>
      </table>

## Conclusion

J'espère que cet article vous a été utile pour comprendre comment fonctionne l'instruction _UPDATE_ en SQL.

Vous êtes maintenant prêt à écrire vos propres instructions SQL _UPDATE_ comme un champion ! Après l'avoir fait, j'adorerais que vous les partagiez avec moi sur les réseaux sociaux !

N'oubliez pas de consulter mon [blog](https://jonathansexton.me/blog) où je publie fréquemment des articles sur le développement web.

Pendant que vous y êtes, pourquoi ne pas vous inscrire à ma newsletter ? Vous pouvez le faire en haut à droite de la page principale du blog. J'aime envoyer des articles intéressants (les miens et ceux des autres), des ressources et des outils pour les développeurs de temps en temps.

Si vous avez des questions sur cet article ou simplement en général, mes DM sont ouverts – venez dire bonjour sur [Twitter](https://twitter.com/jj_goose) ou sur l'un de mes autres comptes de réseaux sociaux que vous pouvez trouver sous l'inscription à la newsletter sur la page principale de mon blog ou sur mon profil ici chez fCC :)

Passez une journée géniale et bon codage, ami !