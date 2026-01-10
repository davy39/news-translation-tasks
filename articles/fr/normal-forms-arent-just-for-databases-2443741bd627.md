---
title: Les formes normales ne sont pas uniquement pour les bases de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-08T22:48:15.000Z'
originalURL: https://freecodecamp.org/news/normal-forms-arent-just-for-databases-2443741bd627
coverImage: https://cdn-media-1.freecodecamp.org/images/1*19XklLfx0ufFE97NSzwBng.jpeg
tags:
- name: data
  slug: data
- name: metadata
  slug: metadata
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Les formes normales ne sont pas uniquement pour les bases de données
seo_desc: 'By Jeff M Lowery

  You can apply similar rules to data object types, too.

  You probably learned the term Normal Form in the context of defining schemas for
  relational databases. Database normalization strives to reduce data redundancy in
  table rows and ...'
---

Par Jeff M Lowery

#### _Vous pouvez appliquer des règles similaires aux types d'objets de données, également._

Vous avez probablement appris le terme [Forme Normale](https://en.wikipedia.org/wiki/Database_normalization#Normal_forms) dans le contexte de la définition de schémas pour les bases de données relationnelles. La normalisation des bases de données vise à réduire la redondance des données dans les lignes et colonnes des tables. Par conséquent, les anomalies de données sont moins susceptibles de se produire.

#### Qu'est-ce qu'une anomalie de données ?

Supposons que nous ayons la situation suivante :

> La table A contient des valeurs pour les propriétés X, Y, Z pour une ligne identifiée par l'id de **x** ; ce sont des **_assertions_** _à propos de x_. Disons que Y dans la ligne **x** est affirmé être la valeur 3.  
>   
> La table B contient également les mêmes assertions sur pourquoi Y pour **x**  
>   
> La table A est informée plus tard, « Les faits ont changé. Y est maintenant 4 »  
>   
> La table B est interrogée plus tard et dit que Y est toujours 3.  
>   
> Maintenant, A et B affirment deux faits différents sur Y, selon la table que vous interrogez.

C'est une anomalie de données : deux assertions différentes sur un fait. Et les faits comptent dans les systèmes informatiques.

### Le quoi et le pourquoi des formes normales

J'utiliserai le terme **type** pour désigner les métadonnées d'un objet. Cela pourrait être implémenté par une définition de [classe](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html), un [mixin](https://www.culttt.com/2015/07/08/working-with-mixins-in-ruby/), un [trait](http://php.net/manual/en/language.oop5.traits.php), un [stamp](https://medium.com/javascript-scene/introducing-the-stamp-specification-77f8911c2fee), ou tout autre mécanisme que votre préférence et votre langage de choix supportent. Je me concentrerai également sur les **objets de données**, tels que les [POJOs](https://spring.io/understanding/POJO), les [PODOs](https://benatkin.com/2012/11/10/podo-generalization-of-pojo/), JSON et des objets simples similaires.

De manière informelle, les trois premières formes normales [sont décrites comme suit](http://www.andrewrollins.com/2009/08/11/database-normalization-first-second-and-third-normal-forms/) :

> Première Forme Normale (1NF) : Pas d'éléments ou de groupes d'éléments répétitifs  
>   
> Deuxième Forme Normale (2NF) : Tous les attributs non-clés dépendent de tous les éléments de la clé  
>   
> Troisième Forme Normale (3NF) : Pas de dépendances sur les attributs non-clés

C'est une lecture assez aride. Mais l'application de ces principes aux définitions de types d'objets est en réalité assez intuitive. Une fois que vous avez intériorisé ces règles, vous n'y penserez même plus consciemment.

### Les objets sont relationnels, aussi

Les bases de données relationnelles supportent les **associations** par le biais de contraintes de clés primaires et étrangères. Les hiérarchies sont implicites, si elles existent. Les associations sont plus lâches que les hiérarchies et les taxonomies, mais aussi plus difficiles à conceptualiser.

Dans une hiérarchie, vous avez des relations parent-enfant. Il existe souvent une hiérarchie de types de données (classe-sous-classe) qui est également modélisée. Les relations dans une hiérarchie de contenu d'objet sont plus contraintes, généralement unidirectionnelles (parent vers enfant), mais aussi plus faciles à comprendre qu'une association plus générale (et flexible).

#### 1NF : Pas d'éléments ou de groupes d'éléments répétitifs

Disons que nous avons les informations de contact suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/K6MgfQspOPhM3PLOSTXy5R07r-kZHXmENGgZ)

Où sont les éléments répétitifs ?

1. Attributs de nom : cela pourrait être considéré comme une relation un-à-plusieurs, où le nombre de noms est indéterminé (comme la royauté britannique). En pratique, cependant, le prénom, le nom et éventuellement le deuxième prénom sont suffisants pour la plupart des domaines d'application, donc il n'y a pas vraiment besoin de normaliser ces champs.
2. Téléphones : La répétition des attributs de téléphone semble être un problème potentiel : deux téléphones suffisent-ils ? Et que se passe-t-il si des informations supplémentaires sont associées plus tard au numéro de téléphone, comme le temps disponible ?
3. Lignes d'adresse : encore une fois, deux suffisent-elles ? Dans certains pays, les adresses postales peuvent comporter quatre lignes, mais c'est la limite. Comme ce sont des chaînes de caractères simples, ce n'est pas une tragédie si une ou deux lignes d'adresse supplémentaires sont ajoutées plus tard.

Voici un modèle possible, avec les types Contact et Phone :

![Image](https://cdn-media-1.freecodecamp.org/images/9U5kybRDlVxzkYsQAakm-4UKr6Ag8jLedftT)

#### 2NF : Tous les attributs non-clés dépendent de tous les éléments de la clé

Que signifie cela en anglais simple ? Dans une base de données, cela signifie que toutes les colonnes d'une ligne doivent dépendre directement de toute [clé candidate](https://en.wikipedia.org/wiki/Second_normal_form) de cette ligne.

Alors, examinons à nouveau Contact :

![Image](https://cdn-media-1.freecodecamp.org/images/XUzKdMHD4qLCfsrcFuVnAjnbt4jW4P52iNnL)

Ici, la clé est une valeur d'id générée, parfois appelée clé de substitution. Les attributs d'adresse dépendent-ils de l'ID de contact ? Eh bien...

**Tout dépend du domaine.**

Les six propriétés d'adresse ne sont certainement pas des attributs du Contact, mais plutôt des moyens d'identifier un emplacement physique. Il est possible qu'un contact puisse avoir plusieurs adresses, et peut-être qu'une adresse a plusieurs contacts.

Cela devrait-il être modélisé comme une relation plusieurs-à-plusieurs, avec un type d'objet ContactAddress qui a un ID de Contact et un ID d'Adresse ? Cela dépendra de ce qui est important pour votre domaine d'application. Certaines applications peuvent traiter les Contacts comme des entités fortes, indépendantes de l'Adresse, mais les Adresses comme des entités faibles, dépendantes d'un Contact pour exister. Dans ce cas, un contact peut avoir plusieurs adresses, et chaque adresse fait référence à un contact, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/fR5nqYyCmC8BomUNDq8wl514ZiFl41UOWe-K)

Il y a une anomalie de données potentielle : si vous changez l'adresse pour un contact, vous ne changez pas cette même adresse pour tous les contacts. Si Contact est votre source de référence principale, alors cela peut être le comportement souhaité : votre contact déménage (vers une autre organisation, par exemple) et les Contacts restants restent en place.

#### 3NF : Pas de dépendances sur les attributs non-clés

En regardant à nouveau l'Adresse, vous pourriez repérer les deux champs dépendants, **région** et **pays**. Un pays peut ou non avoir des régions, mais une région a un pays : vous ne voulez pas les mélanger.

Une façon de s'assurer que la région appartient au pays correct est de créer un identifiant pour chaque paire (pays, région), puis de faire en sorte que l'adresse se réfère à l'identifiant plutôt qu'à la région et au pays indépendamment :

![Image](https://cdn-media-1.freecodecamp.org/images/iILOA2dV6A3xU--R6yv4Raa80jsHU0KRh55L)

#### Un mot sur les identifiants générés

À mon avis, les identifiants générés sont un détail d'implémentation et ne sont vraiment nécessaires que par le code client lors de la modification ou de la suppression d'un enregistrement back-end (comme une ligne dans une base de données), mais jamais dans le cadre d'une requête en lecture seule. Ils ne devraient également jamais être vus par l'utilisateur du système, car ils sont dénués de sens.

### Table par Type, Table par Hiérarchie de Types

Ce qui est intéressant avec les types d'objets normalisés, c'est qu'ils se mappent facilement aux tables de bases de données relationnelles. Pour une implémentation de base de données relationnelle, les tables reflètent les types d'objets ([Table par Type](https://blog.devart.com/table-per-type-vs-table-per-hierarchy-inheritance.html)) ou contiennent au moins des informations pour plusieurs types dérivés d'un type de base ([Table par Hiérarchie de Types](https://www.codeproject.com/Articles/545395/A-Beginners-Tutorial-on-Understanding-Table-Per-Ty)). Cela peut sembler que je prône le [Mappage Objet-Relationnel](https://en.wikipedia.org/wiki/Object-relational_mapping), mais non... Je dis simplement qu'il est bénéfique que votre [Modèle Logique](https://www.1keydata.com/datawarehousing/logical-data-model.html) partage les mêmes caractéristiques que le [Modèle Physique](https://www.1keydata.com/datawarehousing/physical-data-model.html) à un niveau **conceptuel**. L'implémentation est un autre sujet entièrement.

### **Références**

Il existe de nombreuses ressources sur la normalisation des schémas de bases de données relationnelles :

[**Normalisation des bases de données : Première, Deuxième et Troisième Formes Normales - Andrew Rollins**](http://www.andrewrollins.com/2009/08/11/database-normalization-first-second-and-third-normal-forms/)  
[_J'ai lu une excellente explication des première, deuxième et troisième formes normales il y a quelques semaines. Pour ceux qui savent ce qu'est une base de données..._](http://www.andrewrollins.com/2009/08/11/database-normalization-first-second-and-third-normal-forms/)  
[www.andrewrollins.com](http://www.andrewrollins.com/2009/08/11/database-normalization-first-second-and-third-normal-forms/)

[**Deuxième Forme Normale de la Base de Données Expliquée en Anglais Simple**](https://www.essentialsql.com/get-ready-to-learn-sql-10-database-second-normal-form-explained-in-simple-english/)  
[_Le deuxième article se concentrait sur la première forme normale, sa définition et des exemples pour la comprendre. Maintenant, il est temps de..._](https://www.essentialsql.com/get-ready-to-learn-sql-10-database-second-normal-form-explained-in-simple-english/)  
[www.essentialsql.com](https://www.essentialsql.com/get-ready-to-learn-sql-10-database-second-normal-form-explained-in-simple-english/)

[**Qu'est-ce que la Deuxième Forme Normale (2NF) ? - Définition de Techopedia**](https://www.techopedia.com/definition/21980/second-normal-form-2nf)  
[_Deuxième Forme Normale 2NF Définition - La deuxième forme normale (2NF) est la deuxième étape de la normalisation d'une base de données. 2NF construit..._](https://www.techopedia.com/definition/21980/second-normal-form-2nf)  
[www.techopedia.com](https://www.techopedia.com/definition/21980/second-normal-form-2nf)

[**Troisième Forme Normale de la Base de Données Expliquée en Anglais Simple**](https://www.essentialsql.com/get-ready-to-learn-sql-11-database-third-normal-form-explained-in-simple-english/)  
[_Le troisième article se concentrait sur la deuxième forme normale, sa définition et des exemples pour la comprendre. Une fois qu'une table est dans..._](https://www.essentialsql.com/get-ready-to-learn-sql-11-database-third-normal-form-explained-in-simple-english/)  
[www.essentialsql.com](https://www.essentialsql.com/get-ready-to-learn-sql-11-database-third-normal-form-explained-in-simple-english/)

De plus, en recherchant pour cet article, je suis tombé sur une approche quelque peu différente de l'application des règles de normalisation aux types d'objets.

[**Introduction à la Normalisation des Classes**](http://www.agiledata.org/essays/classNormalization.html)  
[www.agiledata.org](http://www.agiledata.org/essays/classNormalization.html)