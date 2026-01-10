---
title: Instruction SQL DELETE - Comment supprimer des données d'une table avec des
  exemples de requêtes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-07T18:11:32.000Z'
originalURL: https://freecodecamp.org/news/sql-delete-row-statement-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/u-j-e-s-h-7ySd00IGyx4-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Instruction SQL DELETE - Comment supprimer des données d'une table avec
  des exemples de requêtes
seo_desc: "By Jonathan Sexton\nI make no qualms about how much I enjoy working with\
  \ SQL both in my professional and personal projects. \nIts straightforwardness and\
  \ simplicity appeal to my desire to have well-defined boundaries in terms of what\
  \ the language will ..."
---

Par Jonathan Sexton

Je ne cache pas à quel point j'aime travailler avec SQL, tant dans mes projets professionnels que personnels. 

Sa simplicité et sa clarté répondent à mon désir d'avoir des limites bien définies en termes de ce que le langage permettra ou non en matière de syntaxe. 

SQL est structuré avec une manière claire et concise de fonctionner, où l'entrée de l'utilisateur dicte les données retournées. D'où mon commentaire sur les limites bien définies de la syntaxe.

Tout en célébrant sa résilience (SQL a été créé en 1974 avec une première version en 1986) au sein de la communauté de développement, je sais aussi que travailler avec des données peut sembler stressant et effrayant, même pour les fondamentaux.

Je suis ici pour (espérons-le) éclairer l'un de ces fondamentaux du travail avec des données : supprimer une ligne entière de données. 

Bien que nous n'allons pas passer en revue le processus de [création d'une table en SQL](https://www.freecodecamp.org/news/sql-create-table-statement-with-example-syntax/) ou de [peuplement de cette table avec des données/mise à jour de ces données](https://www.freecodecamp.org/news/sql-update-statement-example-queries-for-updating-table-values/), j'ai lié ces autres articles au cas où vous souhaiteriez en savoir plus ou avez simplement besoin d'un rappel.

Très bien, maintenant la partie amusante - commençons à supprimer des données d'une table !

## Aperçu de l'instruction SQL DELETE

Voici la table, aptement nommée _Cute_Doggos_, que nous utiliserons comme exemple pour commencer à supprimer des données :

 <table>
            <th>
              <tr style="font-weight: bold">
                <td>Nom</td>
                <td>Couleur</td>
                <td>Race</td>
                <td>Âge</td>
                <td>Poids</td>
                <td>Taille</td>
                <td>Nourriture_préférée</td>
                <td>Jouet_préféré</td>
                <td>Déteste</td>
                <td>Allergies</td>
              </tr>
            </th>
            <tbody>
              <tr>
                <td>daisy</td>
                <td>rouge</td>
                <td>teckel standard</td>
                <td>1 an</td>
                <td>14</td>
                <td>6</td>
                <td>croquettes au saumon</td>
                <td>balle qui couine</td>
                <td>les oiseaux volant au-dessus du jardin</td>
                <td>chats, bains, propreté</td>
              </tr>
                <tr style="background-color: lightgrey">
                <td>winston</td>
                <td>noir/marron</td>
                <td>rottweiler</td>
                <td>3 ans</td>
                <td>41</td>
                <td>17</td>
                <td>littéralement n'importe quoi</td>
                <td>corde à tirer</td>
                <td>rester hors du canapé</td>
                <td>écouter, se comporter, ne pas baver sur tout</td>
              </tr>
              <tr>
                <td>sammie</td>
                <td>miel clair</td>
                <td>golden retriever</td>
                <td>9 ans</td>
                <td>46</td>
                <td>19</td>
                <td>croquettes au bœuf</td>
                <td>son lit</td>
                <td>chiots turbulents</td>
                <td>aucune connue</td>
              </tr>
              <tr style="background-color: lightgrey">
                <td>penelope</td>
                <td>gris et blanc</td>
                <td>husky</td>
                <td>9 mois</td>
                <td>16</td>
                <td>12</td>
                <td>vieilles chaussures</td>
                <td>extérieur</td>
                <td>chenil</td>
                <td>aucune connue</td>
              </tr>
            </tbody>
 </table>

Comme vous l'avez peut-être deviné, il s'agit de données fictives issues d'une table que j'ai inventée de toutes pièces :) Cependant, j'espère qu'elle illustre suffisamment bien les données pour nos besoins.

Comme pour la plupart des aspects de nature technique, il est toujours utile de consulter la documentation officielle. Si vous souhaitez le faire, Microsoft propose des informations approfondies sur l'instruction [SQL DELETE](https://docs.microsoft.com/en-us/sql/t-sql/statements/delete-transact-sql?view=sql-server-ver15).

Passons au cœur de cet article - la suppression de données. L'action est aussi simple que son nom et voici la syntaxe de base :

<code>DELETE FROM <em>nom_de_la_table</em></code>

### ***Avec cette syntaxe, vous supprimerez toutes les lignes de données de la table entière.*** 



Pour notre table d'exemple ci-dessus, la requête ressemblerait à ce qui suit :

<code>DELETE FROM Cute_Doggos</code>

Cela peut être votre intention et plus vous écrivez en SQL, plus vous trouverez de cas pour utiliser l'instruction delete de cette manière. 

J'ai utilisé cette instruction de nombreuses fois pour vider une table après l'avoir remplie de données de test. Cette approche nous permet de conserver les noms de colonnes, les types de données, les index et la structure globale de la table sans supprimer la table elle-même.

*En tant que note secondaire, si votre intention est de supprimer toutes les lignes d'une table, l'approche la plus rapide serait d'utiliser l'instruction [TRUNCATE TABLE](https://docs.microsoft.com/en-us/sql/t-sql/statements/truncate-table-transact-sql?view=sql-server-ver15) car elle utilise beaucoup moins de ressources système.*

## Exemples de requêtes DELETE

La grande majorité du temps, lorsque vous utilisez la fonctionnalité de suppression, vous voudrez être un peu plus ciblé dans votre approche. Pour cela, nous ajouterons une condition et la syntaxe ressemblera à ceci :

<code>DELETE FROM <em>nom_de_la_table</em> WHERE <em>conditions_existent</em></code>

En utilisant notre table de chiens ci-dessus, notre requête ressemblerait à ceci :

<code>DELETE FROM Cute_Doggos WHERE dbo.Cute_Doggos.Taille > 18</code>

Cela supprimerait toutes les entrées de notre table qui correspondent à notre condition de *Taille supérieure à 18*. Et si vous utilisez Microsoft SQL Server Manager, vous obtiendrez un message de retour comme suit : 

<code>(1 ligne affectée)</code>

Si vous souhaitez voir les lignes de données qui ont été supprimées (à des fins de journalisation, d'indications visuelles pour les utilisateurs, etc.), nous pouvons utiliser l'instruction OUTPUT pour cela.

Notre table ressemblerait maintenant à ceci :

 <table>
            <th>
              <tr style="font-weight: bold">
                <td>Nom</td>
                <td>Couleur</td>
                <td>Race</td>
                <td>Âge</td>
                <td>Poids</td>
                <td>Taille</td>
                <td>Nourriture_préférée</td>
                <td>Jouet_préféré</td>
                <td>Déteste</td>
                <td>Allergies</td>
              </tr>
            </th>
            <tbody>
              <tr>
                <td>daisy</td>
                <td>rouge</td>
                <td>teckel standard</td>
                <td>1 an</td>
                <td>14</td>
                <td>6</td>
                <td>croquettes au saumon</td>
                <td>balle qui couine</td>
                <td>les oiseaux volant au-dessus du jardin</td>
                <td>chats, bains, propreté</td>
              </tr>
                <tr style="background-color: lightgrey">
                <td>winston</td>
                <td>noir/marron</td>
                <td>rottweiler</td>
                <td>3 ans</td>
                <td>41</td>
                <td>17</td>
                <td>littéralement n'importe quoi</td>
                <td>corde à tirer</td>
                <td>rester hors du canapé</td>
                <td>écouter, se comporter, ne pas baver sur tout</td>
              </tr>
              <tr>
                <td>penelope</td>
                <td>gris et blanc</td>
                <td>husky</td>
                <td>9 mois</td>
                <td>16</td>
                <td>12</td>
                <td>vieilles chaussures</td>
                <td>extérieur</td>
                <td>chenil</td>
                <td>aucune connue</td>
              </tr>
            </tbody>
 </table>



La condition que nous avons définie est entièrement notre choix, et si cela est trop restrictif pour vos besoins, il existe d'autres options.

Supposons que vous ne vous souciez pas des enregistrements spécifiques que vous supprimez, mais que vous devez simplement supprimer un certain nombre d'enregistrements dans la table.

<code>DELETE TOP 2 FROM Cute_Doggos</code>

Vous pourriez penser que cette requête supprimerait les deux premiers enregistrements de votre table - et vous n'êtes pas loin. Le seul problème est que SQL stocke les enregistrements dans un ordre aléatoire, donc cette syntaxe supprimera 2 **<ins>ENREGISTREMENTS ALÉATOIRES</ins>** de la table.

Si vous cherchez à supprimer un pourcentage des enregistrements, SQL peut également le faire :

<code>DELETE TOP 25 PERCENT FROM Cute_Doggos</code>

Encore une fois, cette requête supprimera des **<ins>ENREGISTREMENTS ALÉATOIRES</ins>**. Dans notre exemple, puisque nous avons 4 enregistrements, cette requête supprimerait 1 enregistrement aléatoire (4 * 0,25 = 1).

En tant que dernière note secondaire, lors de l'utilisation du mot-clé TOP, nous ne pouvons pas utiliser une clause [ORDER BY](https://docs.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver15) en raison de l'aléatoire du stockage des enregistrements.

## Conclusion

Maintenant que vous avez vu l'instruction DELETE en action, vous êtes prêt à partir à l'aventure et à supprimer toutes les données de toutes les tables ! Peut-être ne faites pas cela, car cela vous donnera un long week-end de restauration à partir de sauvegardes :)

En tout cas, vous êtes maintenant prêt à commencer à l'utiliser à bon escient.

Si vous avez trouvé cet article utile, consultez mon [blog](https://jonathansexton.me/blog) (je le reconstruis actuellement avec Gatsby/WordPress, alors restez à l'écoute pour un article à ce sujet) où je publie fréquemment des articles sur le développement web, la vie et l'apprentissage.

Pendant que vous y êtes, pourquoi ne pas vous inscrire à ma newsletter ? Vous pouvez le faire en haut à droite de la page principale du blog. J'aime envoyer des articles intéressants (les miens et ceux des autres), des ressources et des outils pour les développeurs de temps en temps.

Si vous avez des questions sur cet article ou simplement en général, faites-le moi savoir - venez dire bonjour sur [Twitter](https://twitter.com/jj_goose) ou sur l'un de mes autres comptes de réseaux sociaux que vous pouvez trouver sous l'inscription à la newsletter sur la page principale de mon blog ou sur mon profil ici chez freeCodeCamp :)

Passez une journée géniale ! Bon apprentissage et bon codage, ami.