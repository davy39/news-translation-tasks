---
title: Normalisation des bases de données – Formes normales 1NF, 2NF, 3NF avec exemples
  de tables
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-12-21T16:40:26.000Z'
originalURL: https://freecodecamp.org/news/database-normalization-1nf-2nf-3nf-table-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/normalization.png
tags:
- name: database
  slug: database
seo_title: Normalisation des bases de données – Formes normales 1NF, 2NF, 3NF avec
  exemples de tables
seo_desc: 'In relational databases, especially large ones, you need to arrange entries
  so that other maintainers and administrators can read them and work on them. This
  is why database normalization is important.

  In simple words, database normalization entails ...'
---

Dans les bases de données relationnelles, surtout les grandes, il est nécessaire d'organiser les entrées de manière à ce que d'autres mainteneurs et administrateurs puissent les lire et y travailler. C'est pourquoi la normalisation des bases de données est importante.

En termes simples, la normalisation des bases de données consiste à organiser une base de données en plusieurs tables afin de réduire la redondance. Vous pouvez concevoir la base de données pour suivre l'un des types de normalisation tels que 1NF, 2NF et 3NF.

Dans cet article, nous examinerons en détail ce qu'est la normalisation des bases de données et son but. Nous examinerons également les types de normalisation – 1NF, 2NF, 3NF – avec des exemples.

## Ce que nous allons couvrir
- [Qu'est-ce que la normalisation des bases de données ?](#heading-quest-ce-que-la-normalisation-des-bases-de-donnees)
- [Quel est le but de la normalisation ?](#heading-quel-est-le-but-de-la-normalisation)
- [Qu'est-ce que 1NF, 2NF et 3NF ?](#heading-quest-ce-que-1nf-2nf-et-3nf)
  - [La première forme normale – 1NF](#heading-la-premiere-forme-normale-1nf)
  - [La deuxième forme normale – 2NF](#heading-la-deuxieme-forme-normale-2nf)
  - [La troisième forme normale – 3NF](#heading-la-troisieme-forme-normale-3nf)
- [Exemples de 1NF, 2NF et 3NF](#heading-exemples-de-1nf-2nf-et-3nf)
- [Conclusion](#heading-conclusion)


## Qu'est-ce que la normalisation des bases de données ?
La normalisation des bases de données est un principe de conception de base de données pour organiser les données de manière organisée et cohérente.

Elle vous aide à éviter la redondance et à maintenir l'intégrité de la base de données. Elle vous aide également à éliminer les caractéristiques indésirables associées à l'insertion, à la suppression et à la mise à jour.

## Quel est le but de la normalisation ?
Le principal objectif de la normalisation des bases de données est d'éviter les complexités, d'éliminer les doublons et d'organiser les données de manière cohérente. Dans la normalisation, les données sont divisées en plusieurs tables liées entre elles par des relations.

Les administrateurs de bases de données sont en mesure d'atteindre ces relations en utilisant des clés primaires, des clés étrangères et des clés composites.

Pour y parvenir, une clé primaire dans une table, par exemple, `employee_wages` est liée à la valeur d'une autre table, par exemple, `employee_data`.

**N.B.** : **Une clé primaire** est une colonne qui identifie de manière unique les lignes de données dans cette table. C'est un identifiant unique tel qu'un identifiant d'employé, un identifiant d'étudiant, un numéro d'identification de l'électeur (VIN), etc.

**Une clé étrangère** est un champ qui se rapporte à la clé primaire dans une autre table.

**Une clé composite** est comme une clé primaire, mais au lieu d'avoir une colonne, elle a plusieurs colonnes.


## Qu'est-ce que 1NF, 2NF et 3NF ?
1NF, 2NF et 3NF sont les trois premiers types de normalisation des bases de données. Ils signifient respectivement **première forme normale**, **deuxième forme normale** et **troisième forme normale**.

Il existe également 4NF (quatrième forme normale) et 5NF (cinquième forme normale). Il existe même 6NF (sixième forme normale), mais la forme normale la plus courante que vous verrez est 3NF (troisième forme normale).

Tous les types de normalisation des bases de données sont cumulatifs – ce qui signifie que chacun s'appuie sur ceux qui le précèdent. Ainsi, tous les concepts de 1NF se reportent également à 2NF, et ainsi de suite.

### La première forme normale – 1NF
Pour qu'une table soit en première forme normale, elle doit répondre aux critères suivants :
- une seule cellule ne doit pas contenir plus d'une valeur (atomicité)
- il doit y avoir une clé primaire pour l'identification
- pas de lignes ou de colonnes dupliquées
- chaque colonne doit avoir une seule valeur pour chaque ligne dans la table

### La deuxième forme normale – 2NF
La 1NF élimine uniquement les groupes répétitifs, pas la redondance. C'est pourquoi il y a 2NF.

Une table est dite en 2NF si elle répond aux critères suivants :
- elle est déjà en 1NF
- elle n'a pas de dépendance partielle. C'est-à-dire que tous les attributs non clés dépendent entièrement d'une clé primaire.

### La troisième forme normale – 3NF

Lorsque une table est en 2NF, elle élimine les groupes répétitifs et la redondance, mais elle n'élimine pas la dépendance partielle transitive.

Cela signifie qu'un attribut non premier (un attribut qui ne fait pas partie de la clé candidate) dépend d'un autre attribut non premier. C'est ce que la troisième forme normale (3NF) élimine.

Ainsi, pour qu'une table soit en 3NF, elle doit :
- être en 2NF
- ne pas avoir de dépendance partielle transitive.


## Exemples de 1NF, 2NF et 3NF
La normalisation des bases de données est assez technique, mais nous allons illustrer chacune des formes normales avec des exemples.

Imaginons que nous construisons une application de gestion de restaurant. Cette application doit stocker des données sur les employés de l'entreprise et commence par créer la table suivante des employés :

|employee_id| name | job_code | job |state_code |home_state |
|--|--| -- |-- |-- | -- |
| E001  | Alice | J01 |Chef | 26| Michigan|
| E001  | Alice | J02 | Waiter|26 | Michigan| 
| E002  | Bob | J02 |Waiter |56 |Wyoming |
| E002  | Bob |J03 |Bartender |56 |Wyoming |
| E003  |Alice  |J01 |Chef |56 |Wyoming |

Toutes les entrées sont atomiques et il y a une clé primaire composite (employee_id, job_code), donc la table est en **première forme normale (1NF)**.

Mais même si vous ne connaissez que le `employee_id` de quelqu'un, vous pouvez déterminer son `name`, `home_state` et `state_code` (parce qu'il devrait s'agir de la même personne). Cela signifie que `name`, `home_state` et `state_code` dépendent de `employee_id` (une partie de la clé composite primaire). Donc, la table n'est pas en **2NF**. Nous devrions les séparer dans une table différente pour la rendre 2NF.		

### Exemple de deuxième forme normale (2NF)
#### Table `employee_roles`
|employee_id|job_code|
|--|--|
|E001|J01|
|E001|J02|
|E002|J02|
|E002|J03|
|E003|J01|

#### Table `employees`
|employee_id|name|state_code|home_state|
|--|--|--|--|
|E001|Alice|26|Michigan|
|E002|Bob|56|Wyoming|
|E003|Alice|56|Wyoming|

#### Table `jobs`
|job_code|job|
|--|--|
|J01|Chef|
|J02|Waiter|
|J03|Bartender|

`home_state` dépend maintenant de `state_code`. Donc, si vous connaissez le `state_code`, vous pouvez trouver la valeur de `home_state`.					

Pour aller plus loin, nous devrions les séparer à nouveau dans une table différente pour la rendre 3NF.

### Exemple de troisième forme normale (3NF)
#### Table `employee_roles`
|employee_id|job_code|
|--|--|--|
|E001|J01|
|E001|J02|
|E002|J02|
|E002|J03|
|E003|J01|

#### Table `employees`
|employee_id|name|state_code|
|--|--|--|
|E001|Alice|26|
|E002|Bob|56|
|E003|Alice|56|


#### Table `jobs`
|job_code|job|
|--|--|
|J01|Chef|
|J02|Waiter|
|J03|Bartender|

#### Table `states`
|state_code|home_state|
|--|--|
|26|Michigan|
|56|Wyoming|

Maintenant, notre base de données est en 3NF.

## Conclusion
Cet article vous a expliqué ce qu'est la normalisation des bases de données, son but et ses types. Nous avons également examiné ces types de normalisation et les critères qu'une table doit respecter avant de pouvoir être certifiée comme étant dans l'un d'eux.

Il est important de noter que la plupart des tables ne dépassent pas la limite 3NF, mais vous pouvez également les amener à 4NF et 5NF, selon les exigences et la taille des données en question.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.