---
title: Comment utiliser l'instruction SQL CASE – avec un défi d'exemple
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2022-11-04T14:28:57.000Z'
originalURL: https://freecodecamp.org/news/sql-case-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Sql-case-banner.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Comment utiliser l'instruction SQL CASE – avec un défi d'exemple
seo_desc: "Writing SQL with multiple conditions can be an arduous task, especially\
  \ if you need to make numerous checks. \nFor example, an if () else if () else {}\
  \ check case expression handles all SQL conditionals. If the first condition is\
  \ satisfied, the query ..."
---

Écrire du SQL avec plusieurs conditions peut être une tâche ardue, surtout si vous devez effectuer de nombreuses vérifications. 

Par exemple, une expression de cas de vérification `if () else if () else {}` gère toutes les conditionnelles SQL. Si la première condition est satisfaite, la requête cesse de s'exécuter avec une valeur de retour. La valeur spécifiée dans le else est retournée si aucune condition n'est satisfaite.

Dans cet article, nous allons couvrir :

1. Ce qu'est l'instruction SQL CASE et comment elle fonctionne
2. Comment résoudre un exercice en utilisant l'instruction SQL CASE
3. La signification de certains termes importants, comme order by, limit, offset, left join et alias.

## Explication de l'instruction SQL CASE

En programmation, lorsque vous avez un ensemble donné de conditions, vous finissez par utiliser des conditionnelles (`switch` ou `if else`) pour savoir quel bloc de code exécuter lorsqu'une condition est remplie. 

Avec SQL, vous pouvez faire cela en utilisant l'instruction CASE. Vous utilisez le mot-clé CASE avec la clause WHEN pour exécuter un bloc de code d'instruction conditionnelle. Vous utilisez une instruction THEN pour retourner le résultat de l'expression. Si aucune des conditions n'est remplie, alors vous utilisez une clause ELSE finale pour retourner un résultat de secours. 

L'**instruction SQL CASE a la syntaxe suivante** :

```sql
CASE
    WHEN conditional_statement1 THEN result1
    .
    .
    .
    .
    WHEN condition_statementN THEN resultN
    
    ELSE result
END;
```

Lorsque vous utilisez l'instruction CASE, elle doit être suivie d'un WHEN et THEN le résultat si la première condition est remplie. Si la première condition n'est pas remplie, elle continue à vérifier les autres conditions jusqu'à la n-ième (ou finale) condition. Si celle-ci n'est toujours pas remplie, alors la condition ELSE est exécutée. 

De plus, la partie ELSE est facultative lors de l'utilisation de l'instruction CASE. Dans les scénarios où vous ne l'utilisez pas, le résultat de la requête retourne NULL.

## Défi SQL

Dans cette section, nous allons prendre une étude de cas d'un scénario réel pour vous aider à apprendre comment résoudre un défi SQL qui utilise l'instruction CASE. 

Le défi est l'un de ceux que j'ai rencontrés sur Coderbyte, une plateforme pour pratiquer des défis de codage. C'était un peu difficile à résoudre, et je vais décomposer le processus étape par étape impliqué dans cet article.

### Quel est le défi ?

Le défi consiste à trouver une requête SQL pour retourner l'employé avec le troisième salaire le plus élevé d'une table. 

Vous devrez structurer une requête pour trouver cet employé et retourner cette ligne. Vous devez également remplacer la position de la colonne DivisionID par le DivisionName correspondant de la table company_divisions. Ensuite, vous devrez remplacer la colonne ManagerID par le ManagerName si l'ID existe dans la table et n'est pas NULL.

### Quel problème l'instruction SQL CASE résout-elle dans ce défi ?

Dans ce défi, nous avons besoin de l'instruction CASE pour aider à réaliser les points suivants :

1. Assurer que le MangerID n'est pas NULL.
2. Faire correspondre le ManagerID de l'entreprise à l'ID de l'entreprise et retourner le Nom en tant que ManagerName.
3. Assurer que si aucun Nom n'est retourné, alors le nom Susan Wall est utilisé comme ManagerName par défaut.

**Voici le résultat attendu :**

<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>DivisionName</th>
        <th>ManagerName</th>
        <th>Salary</th>
    </tr>
    <tr>
      	<td>222</td>
      	<td>Mark Red</td>
      	<td>Sales</td>
        <td>Susan Wall</td>
      	<td>86000</td>
     </tr>
</table>
        		

Et voici les données dont vous aurez besoin pour résoudre ce défi :

#### Table 1 : company

<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>DivisionID</th>
        <th>ManagerID</th>
        <th>Salary</th>
    </tr>
    <tr>
        <td>356</td>
        <td>Daniel smith</td>
        <td>100</td>
        <td>133</td>
        <td>40000</td>
    </tr>
    <tr>
        <td>122</td>
        <td>Arnold Sully</td>
        <td>101</td>
        <td>null</td>
        <td>60000</td>
    </tr>
    <tr>
        <td>467</td>
        <td>Lisa Roberts</td>
        <td>100</td>
        <td>null</td>
        <td>80000</td>
    </tr>
    <tr>
        <td>112</td>
        <td>Mary Dial</td>
        <td>105</td>
        <td>467</td>
        <td>65000</td>
    </tr>
    <tr>
        <td>775</td>
        <td>Dennis Front</td>
        <td>103</td>
        <td>null</td>
        <td>90000</td>
    </tr>
    <tr>
        <td>111</td>
        <td>Larry Weis</td>
        <td>104</td>
        <td>35534</td>
        <td>75000</td>
    </tr>
    <tr>
        <td>222</td>
        <td>Mark Red</td>
        <td>102</td>
        <td>133</td>
        <td>86000</td>
    </tr>
    <tr>
        <td>577</td>
        <td>Robert Niger</td>
        <td>105</td>
        <td>12353</td>
        <td>76000</td>
    </tr>
    <tr>
        <td>133</td>
        <td>Susan Wall</td>
        <td>105</td>
        <td>577</td>
        <td>110000</td>
    </tr>
</table>
    
        

#### Table 2 : company_divisions

<table>
    <tr>
        <th> ID </th>
        <th> </th>
        <th> DivisionName </th>
    </tr>
    <tr>
        <td> 100 </td>
        <td> </td>
        <td> Accounting </td>
    </tr>
    <tr>
        <td> 101 </td>
        <td> </td>
        <td> IT </td>
    </tr>
    <tr>
        <td> 102 </td>
        <td> </td>
        <td> Sales </td>
    </tr>
    <tr>
        <td> 103 </td>
        <td> </td>
        <td> Marketing </td>
    </tr>
    <tr>
        <td> 104 </td>
        <td> </td>
        <td> Engineering </td>
    </tr>
    <tr>
        <td> 105 </td>
        <td> </td>
        <td> Customer Support </td>
    </tr>
</table>

## Comment résoudre le défi de l'instruction SQL CASE

Dans cette section, nous allons examiner le processus étape par étape impliqué dans la résolution du défi.

### Étape 1 : Obtenir le troisième salaire le plus élevé

Tout d'abord, vous devrez structurer une requête pour retourner le troisième salaire le plus élevé. Vous le ferez en sélectionnant dans la table company et en ordonnant par salaire (puisque nous nous intéressons à l'enregistrement avec le troisième salaire le plus élevé). 

Vous pouvez faire cela comme suit :

```sql
SELECT *

FROM company

ORDER BY salary DESC limit 1 offset 2;
```

La requête retourne la ligne de l'employé avec le troisième salaire le plus élevé, comme prévu.

<table>
    <tr>
     	<th>ID</th>
        <th>Name</th>
        <th>DivisionID</th>
        <th>ManagerID</th>
        <th>Salary</th>   
    </tr>
    <tr>
        <td>222</td>
        <td>Mark Red</td>
        <td>102</td>
        <td>133</td>
        <td>86000</td>
    </tr>
</table>

Alors, que se passe-t-il dans cette requête ?

`SELECT` : vous utilisez la commande SELECT avec l'astérisque (*), également connu sous le nom de caractère générique) pour récupérer toutes les colonnes de la table **company**.

`ORDER BY` : La commande ORDER BY ordonne les colonnes dans l'ordre ascendant ou descendant. SQL ordonne par ascendant (**ASC**) par défaut, mais nous allons ordonner la colonne salaire par descendant (**DESC**). Cela est dû au fait que nous avons besoin du salaire descendant du plus élevé au plus bas, c'est-à-dire 110 000 - 40 000.

`limit` : La commande limit limite le nombre d'enregistrements retournés en fonction de la valeur définie par la limite. Puisque nous nous intéressons uniquement à une seule ligne, nous allons définir la limite dans la requête à 1. Cela garantit que nous obtiendrons une valeur de retour d'un seul enregistrement à chaque fois que cette requête est exécutée.

`offset` : L'utilisation de la clause offset ici vous aide à spécifier le nombre de lignes à ignorer avant le début du retour effectif de la ligne de la requête. Offset nous permet d'ignorer les deux lignes les mieux payées (Susan Wall et Dennis Front) et de retourner la troisième ligne la mieux payée (Mark Red).

### Étape 2 : Remplacer DivisionID par DivisionName

Maintenant, vous devez modifier la requête en sélectionnant uniquement les colonnes dont vous avez besoin – ID, Name, ManagerID, DivisionName et Salary. Ensuite, vous devez remplacer la colonne DivisionID par le DivisionName correspondant de la table **company_divisions**.

Vous pouvez faire cela comme suit :

```sql
SELECT c.ID, c.Name, c.ManagerID, c.salary, cd.DivisionName

FROM company as c

LEFT JOIN company_divisions as cd ON c.DivisionId = cd.id

ORDER BY salary DESC limit 1 offset 2;
```

Voici le résultat :

<table>
    <tr>
     	<th>ID</th>
        <th>Name</th>
        <th>DivisionName</th>
        <th>ManagerID</th>
        <th>Salary</th>   
    </tr>
    <tr>
        <td>222</td>
        <td>Mark Red</td>
        <td>Sales</td>
        <td>133</td>
        <td>86000</td>
    </tr>
</table>

Discutons de ce qui se passe dans la requête ci-dessus :

`LEFT JOIN` : Puisque les enregistrements sont retournés du côté gauche (company), nous allons les faire correspondre en utilisant le LEFT JOIN du côté droit (company_divisions) en utilisant `company_division.id et company.DivisionID`. 

Si un enregistrement correspondant est trouvé, c'est-à-dire que l'ID de l'entreprise est également présent dans la division de l'entreprise, alors la colonne DivisionName est remplie avec la valeur réelle du left join, dans notre cas (Sales). Si aucun enregistrement n'est trouvé, rien n'est retourné.

`as` (alias) : L'alias utilisé est un nom temporaire pour la table. Ainsi, plutôt que company.name avec un alias pour la company en tant que c, nous pouvons le définir comme c.name. L'utilisation d'alias aide à améliorer la lisibilité.

### Étape 3 : Remplacer ManagerID par ManagerName

Nous allons nous appuyer sur le résultat de la requête de l'étape 2. Nous allons utiliser l'instruction CASE que nous avons apprise pour ajouter des conditionnelles lorsque le ManagerId n'est pas null et pour vérifier si le ManagerId existe également.

La première chose que nous devons faire est de vérifier si le company.ManagerID n'est pas null et de nous assurer que l'ID existe dans la table. Nous allons appliquer l'instruction CASE ici.

```sql
CASE WHEN c.ManagerID IS NOT NULL 

AND c.ManagerID = c.ID

```

La deuxième partie de l'instruction CASE consiste à remplacer la colonne ManagerID par le ManagerName. Ensuite, nous devrons utiliser le bloc THEN que nous avons appris plus tôt comme ceci :

```sql
CASE WHEN c.ManagerID IS NOT NULL 

AND c.ManagerID = c.ID

THEN Name ELSE 'Susan Wall' END AS 'ManagerName'
```

Enfin, nous pouvons maintenant inclure le bloc CASE dans le code déjà existant que nous avions de l'ÉTAPE 2. Cela ressemblera à ceci maintenant :

```sql
SELECT c.ID, c.Name, c.salary, cd.DivisionName

CASE WHEN c.ManagerID IS NOT NULL 

AND c.ManagerID = c.ID

THEN Name ELSE 'Susan Wall' END AS 'ManagerName'

FROM company as c

LEFT JOIN company_divisions as cd ON c.DivisionId = cd.id

ORDER BY salary DESC limit 1 offset 2;
```

Le résultat de l'étape 3 est le résultat attendu – l'employé avec le troisième salaire le plus élevé.

<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>DivisionName</th>
        <th>ManagerName</th>
        <th>Salary</th>
    </tr>
    <tr>
      	<td>222</td>
      	<td>Mark Red</td>
      	<td>Sales</td>
        <td>Susan Wall</td>
      	<td>86000</td>
     </tr>
</table>
        		

## **Conclusion**

Dans cet article, j'espère que vous avez appris à propos de l'instruction CASE en SQL et comment aborder un problème réel en utilisant CASE.

Vous avez également appris d'autres commandes SQL telles que SELECT, ORDER BY, LIMIT, OFFSET, LEFT JOIN et ALIAS.