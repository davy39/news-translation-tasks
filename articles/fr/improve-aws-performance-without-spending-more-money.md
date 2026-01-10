---
title: Comment améliorer les performances d'AWS sans dépenser plus d'argent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-15T21:50:26.000Z'
originalURL: https://freecodecamp.org/news/improve-aws-performance-without-spending-more-money
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-howard-adams-575835.jpg
tags:
- name: AWS
  slug: aws
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: Comment améliorer les performances d'AWS sans dépenser plus d'argent
seo_desc: 'By Zaid Humayun

  Identifying performance issues has always been the holy grail of engineering. You
  want to be known as the software engineer who''s able to diagnose and rectify the
  performance issue that came up in production. It really adds credibilit...'
---

Par Zaid Humayun

Identifier les problèmes de performance a toujours été le Saint-Graal de l'ingénierie. Vous voulez être connu comme l'ingénieur logiciel capable de diagnostiquer et de rectifier le problème de performance survenu en production. Cela ajoute vraiment de la crédibilité à vos compétences en ingénierie.

Nous avons eu un problème au travail récemment que j'ai pensé amusant d'écrire. Je vais entrer dans les détails de la manière dont nous avons tenté de trouver la cause racine du problème (ce qui représente 90% du problème habituellement) et ensuite comment nous l'avons résolu.

## Où les problèmes ont commencé

Les problèmes ont commencé avec AWS. L'application fonctionnait sans aucun problème depuis un certain temps. Nous avons décidé d'exécuter un test de charge pour comprendre si un point de terminaison API spécifique pouvait gérer la charge que nous attendions.

Nous avons téléchargé JMeter, essayé de comprendre comment l'utiliser, puis abandonné. Nous y sommes retournés le lendemain et avons finalement eu une idée de comment le faire fonctionner.

Nous l'avons pointé vers le serveur de test en cours d'exécution sur AWS et avons lancé 25 threads en boucle pour s'exécuter 8 fois et avons rapidement vu environ 25% des requêtes échouer. Le temps moyen pour la requête était d'environ 45 secondes. Je ne vais pas mentir – c'était assez terrifiant.

Cela nous a effrayés car cela signifiait que notre route était si ridiculement inefficace qu'elle ne parvenait à générer un débit que d'environ 1,2 requêtes/seconde. Mais nous attendions qu'elle gère une charge d'environ 4-8 requêtes/seconde.

D'accord, alors qu'est-ce qui se passait ? Pourquoi cette route était-elle si extrêmement inefficace ?

## Limitation du CPU

La première hypothèse que nous avons faite a été de pointer du doigt le système ERP interne de l'entreprise sur lequel nous dépendons pour la validation. Bien sûr, cela devait être l'ERP, car cela signifiait que nous n'aurions pas à en prendre la responsabilité puisque c'est un fournisseur différent.

Eh bien, après avoir pointé JMeter vers une machine locale et exécuté le même test de charge, nous avons facilement atteint le débit que nous voulions. En fait, nous l'avons dépassé de beaucoup. Si c'était le système ERP interne qui causait le problème, pourquoi ne pouvait-il pas être reproduit sur une machine locale ?

J'ai contacté quelqu'un qui travaille chez Amazon pour obtenir de l'aide et on m'a orienté vers la limitation des serveurs AWS parce que notre charge CPU ne dépassait jamais 10% sur l'instance de test EC2. Et cela m'a ouvert une boîte de Pandore.

Alors, lorsque vous exécutez votre application sur AWS, que se passe-t-il exactement ? Pour être honnête, je ne comprenais pas vraiment les détails internes et je ne les comprends toujours pas complètement, mais voici l'essentiel.

Vous achetez du temps de calcul auprès d'AWS. Ce que je pensais que cela signifiait, c'est qu'ils exécutaient notre application sur un serveur et que nous payions pour le temps du serveur. Mais ce n'est pas tout à fait exact.

AWS a ce concept d'Unité de Calcul EC2 (ECU) qui est leur manière d'abstraire la nécessité de penser aux serveurs sur lesquels votre application est réellement exécutée. Si vous pouvez penser en termes d'ECU, vous n'avez pas à vous soucier de l'infrastructure physique réelle.

AWS a ensuite changé l'ECU en une unité de CPU virtuelle (vCPU), mais vous trouverez encore beaucoup de références à une ECU sur le web.

Ainsi, un vCPU est la manière dont ils décrivent la puissance de calcul de leurs diverses instances. Nous utilisons une instance EC2 t2.micro pour notre serveur de test et en exécutons deux pour notre serveur de production. Notre application est principalement une charge de travail OLTP qui est intensive en lecture.

Puisque AWS exécute plusieurs applications sur un seul serveur séparées par un hyperviseur, ils allouent une quantité spécifique de bande passante de calcul, de bande passante réseau et de stockage à votre application en fonction de votre choix d'instance.

La manière dont AWS gère cela pour les instances de classe t2 est par quelque chose appelé Crédits de Burst.

## Alors, comment est-ce que je perds de l'argent avec les Crédits de Burst ?

![Image](https://www.freecodecamp.org/news/content/images/2022/08/AWS_burst_credits_chart.png)

Le graphique ci-dessus explique exactement comment les crédits de burst d'AWS fonctionnent pour les instances EC2. La source de l'image est [cette documentation AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html).

L'idée est qu'AWS vous fournit une utilisation de base du CPU au-delà de laquelle vous payez pour le temps de CPU que vous consommez.

Prenons l'exemple d'une instance EC2 t2.micro, l'utilisation de base du CPU pour celle-ci est fixée à 10%. L'instance gagne constamment des crédits en fonction du nombre de vCPU qu'elle possède.

Le calcul pour gagner des crédits est :

`1vCPU * 10% de base * 60 minutes = 6 crédits par heure.`

Le calcul pour dépenser des crédits si vous utilisez 15% est :

`1vCPU * 15% CPU * 60 minutes = 9 crédits par heure.`

Ainsi, si vous fonctionnez constamment à 15%, votre instance perd 9 crédits par heure. Une instance t2.micro ne peut accumuler qu'un total de 144 crédits. Une fois ces crédits épuisés, votre utilisation du CPU sera limitée à 10%, ce qui est l'utilisation de base.

Ainsi, bien que vous ne perdiez peut-être pas strictement de l'argent sur l'instance, vous payez pour cela en cycles de CPU qui sont perdus.

Une autre façon de confirmer que vous perdez des cycles de CPU à cause de la limitation est de vous connecter à votre instance EC2 et d'exécuter la commande `top` pour vérifier le temps de vol. Si vous essayez de tester la charge de votre serveur et que votre CPU est limité, vous pouvez alors observer en temps réel comment le temps de vol augmente pour empêcher votre processus de prendre du temps CPU supplémentaire.

## Échecs de la base de données

D'accord, donc si le problème est la limitation de l'instance EC2, supprimer la limitation devrait résoudre le problème, n'est-ce pas ? Eh bien, nous avons vérifié nos instances de production et avons remarqué qu'elles avaient également des échecs même si elles n'étaient pas limitées.

Sur les instances de production, nous avons réalisé que certaines requêtes prenaient plus de 10 secondes et dépassaient le temps imparti une fois qu'il était 14h.

Pourquoi l'heure de 14h est-elle pertinente ?

Parce que de la même manière qu'AWS limite les cycles de CPU que vous pouvez utiliser sur un serveur EC2, ils limitent également le nombre d'IOPS dont vous disposez pour vos instances RDS.

AWS limite vos IOPS au taux de 3 * (stockage assigné à votre volume EBS). Lorsque vous instanciez une instance RDS, vous devez également lui assigner un certain stockage sur disque. En découplant ces deux éléments, AWS parvient à mettre à niveau votre instance RDS sans affecter aucune des données.

Nous avons commencé avec 20 Go dans notre stockage GP2, ce qui nous donne 60 IOPS. AWS, cependant, fournit un minimum de 100 IOPS.

Chaque fois que votre instance RDS dépasse 100 IOPS, vous consommez des crédits de burst qui sont spécifiques aux instances de base de données et différents des crédits de CPU pour les instances EC2.

La raison pour laquelle les utilisateurs rencontraient un ralentissement vers 14h chaque jour était que nos IOPS étaient supérieurs à 100 tout au long de la journée, ce qui consommait des crédits de burst qui s'épuisaient ensuite vers 14h, après quoi nous étions limités à 100 IOPS.

Cela a causé tous les dépassements de temps auxquels nos utilisateurs étaient confrontés ! Nous avons pensé que la manière la plus simple et la moins chère de résoudre cela serait d'augmenter la capacité de stockage de notre volume EBS. Nous l'avons augmentée à 100 Go, ce qui nous a donné une base de 300 IOPS. Nous avons pensé que cela serait suffisant car nos IOPS moyens au cours d'une journée avaient des fluctuations importantes mais semblaient se situer autour de ce nombre.

Nous avons mis à niveau notre volume EBS et avons attendu l'après-midi suivant – et le même problème est réapparu !

En regardant nos IOPS moyens, j'avais choisi l'intervalle de 1 minute qui ne donnait pas une réflexion équitable de la moyenne car il montrait beaucoup de pics. Choisir l'intervalle de 1 heure montrait une moyenne significativement plus élevée de 600 IOPS !

En enquêtant un peu plus sur le problème des IOPS, j'ai découvert que les IOPS de lecture contribuaient le plus à la charge totale des IOPS.

En dernier recours, nous avons décidé d'activer Performance Insights sur la console AWS pour notre instance RDS afin que nous puissions voir quelles requêtes consommaient la plupart des IOPS et corriger cette requête spécifique.

Lorsque nous avons essayé d'activer Performance Insights, nous avons découvert qu'il ne fonctionnerait pas pour autre chose qu'un `db.t3.medium`, ce qui nous a forcés à passer à une instance de base de données avec 4 Go de RAM.

Nous avons mis à niveau l'instance, puis redémarré le serveur de base de données et attendu. J'ai gardé un œil sur la métrique des IOPS mais elle ne semblait pas bouger au-delà de 0-10 IOPS, ce que j'ai supposé signifier que personne n'utilisait encore l'application.

J'ai vérifié et on m'a répété que les gens utilisaient l'application et qu'elle fonctionnait parfaitement bien, mais je ne comprenais tout simplement pas ce qui se passait. Pourquoi fonctionnait-elle ? Elle n'aurait pas dû fonctionner, il y avait à peine des IOPS qui se produisaient.

## Se souvenir pourquoi la RAM est importante

Eh bien, une des choses que je n'avais pas réalisée était l'impact de la RAM sur le nombre d'IOPS qui se produisent pour une base de données.

AWS mesure les IOPS comme les lectures et écritures sur le disque dur lui-même. Il ne les mesure pas comme les lectures/écritures dans le pool de tampons maintenu par le moteur innoDB dans MySQL.

Le problème était que l'ancienne instance de base de données que nous avions utilisée (le `db.t2.micro`) n'avait que 1 Go de RAM, ce qui signifiait que la taille du pool de tampons était d'environ 250 Mo. Sur la nouvelle instance qui avait 4 Go de RAM, cela signifiait que le pool de tampons avait 2 Go à utiliser.

La requête problématique qui causait le nombre élevé d'IOPS interrogeait une table d'environ 210 Mo de taille. Et comme elle effectuait un balayage de table, elle chargeait presque toute la table dans le pool de tampons puis exécutait les opérations qu'elle devait effectuer.

Comme le pool de tampons n'était que d'environ 250 Mo, une fois qu'il avait chargé la grande table, il supprimait constamment toutes les autres données et devait ensuite retourner au disque pour les récupérer, entraînant plus d'IOPS.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/inno_db_engine_architecture.png)

## La requête problématique

Il manque encore une pièce à ce puzzle. Quelle est cette requête qui cause le chargement de 210 Mo de données en mémoire à chaque fois qu'elle s'exécute ? Certes, nous avons résolu le problème en augmentant la RAM, mais il était clair que quelque chose n'allait pas ici. La table ne ferait qu'augmenter en taille et augmenter constamment la RAM n'était pas une bonne solution.

Voici la requête qui causait tous les problèmes :

```
EXPLAIN ANALYZE
SELECT `oc`.`oc_number` AS `ocNumber` , `roll`.`po_number` AS `poNumber` ,
`item`.`item_code` AS `itemCode` , `roll`.`roll_length` AS `rollLength` ,
`roll`.`roll_utilized` AS `rollUtilized`
FROM `fabric_barcode_rolls` AS `roll`
INNER JOIN `fabric_barcode_oc` AS `oc` ON `oc`.`oc_unique_id` = `roll` . `oc_unique_id`
INNER JOIN `fabric_barcode_items` AS `item` ON `item`.`item_unique_id` = `roll`.`item_unique_id_fk`
WHERE BINARY `roll`.`roll_number` = 'dZkzHJ_je8'

```

En exécutant `EXPLAIN ANALYZE` sur celle-ci, MySQL a fourni le plan de requête suivant :

```
-> Nested loop inner join  (cost=468792.05 rows=582836) (actual time=0.092..288.104 rows=1 loops=1)
    -> Nested loop inner join  (cost=264799.45 rows=582836) (actual time=0.067..288.079 rows=1 loops=1)
        -> Filter: (cast(roll.roll_number as char charset binary) = 'dZkzHJ_je8')  (cost=60806.85 rows=582836) (actual time=0.053..288.064 rows=1 loops=1)
            -> Table scan on roll  (cost=60806.85 rows=582836) (actual time=0.048..230.675 rows=600367 loops=1)
        -> Single-row index lookup on oc using PRIMARY (oc_unique_id=roll.oc_unique_id)  (cost=0.25 rows=1) (actual time=0.014..0.014 rows=1 loops=1)
    -> Single-row index lookup on item using PRIMARY (item_unique_id=roll.item_unique_id_fk)  (cost=0.25 rows=1) (actual time=0.024..0.024 rows=1 loops=1)

```

En regardant le plan de requête, il est étrange qu'il y ait un balayage complet de la table `roll` à chaque fois que la requête s'exécute. Elle examine 582 000 lignes à chaque fois, ce qui est à l'origine des problèmes de performance.

Cela semblait être un problème de mauvais indexation. J'ai donc passé en revue les tables et vérifié les index sur chacune d'elles pour m'assurer qu'ils étaient corrects. J'ai essayé de réécrire la requête pour filtrer la table `roll` avant d'exécuter le reste de la requête et la performance était encore pire.

Enfin, sur un coup de tête, j'ai supprimé l'appel de la fonction `BINARY` dans la requête que j'avais mise pour m'assurer que la sensibilité à la casse ne poserait pas de problème. Le plan d'exécution de la requête résultante était choquant :

```
-> Rows fetched before execution  (cost=0.00 rows=1) (actual time=0.000..0.000 rows=1 loops=1)

```

Une quantité ridicule de temps d'exécution était gaspillée par cet appel de fonction. Alors, pourquoi cet appel de fonction causait-il tous ces problèmes ?

J'y ai réfléchi et j'ai fait ce que tout ingénieur logiciel qui se respecte fait lorsqu'il est confronté à un problème qu'il ne peut pas résoudre. J'ai posté la question sur Stack Overflow.

[Voici un lien vers la question](https://stackoverflow.com/questions/71908085/why-does-removing-the-binary-function-call-from-my-sql-query-change-the-query-pl). La réponse est que cela a à voir avec la collation des colonnes.

Puisque je convertissais chaque valeur dans la colonne `roll_number` de la table `roll` en une valeur binaire, MySQL ne peut pas utiliser les index à moins que cette collation spécifique ne soit définie sur la colonne dans le DDL.

Puisque l'index était inutile, il effectuait un balayage complet de la table et vérifiait la valeur de chaque ligne via des jointures internes imbriquées.

Supprimer l'appel de la fonction `BINARY` était le moyen le plus simple de résoudre le problème. Mais changer la collation de la colonne pour utiliser le jeu de caractères Latin et être sensible à la casse afin que l'index soit construit avec une sensibilité à la casse a assuré que nous ne rencontrions pas de problèmes de collisions de codes-barres.

## Défis avec AWS

Il ne fait aucun doute qu'AWS a fait un travail formidable en abstraant le matériel pour des millions d'ingénieurs logiciels. Mais il a simultanément rendu les prix si difficiles à comprendre que personne ne sait vraiment combien ils paient jusqu'à ce qu'il soit trop tard.

Nous ne pouvons pas rétrograder le volume EBS de 100 Go à 20 Go car AWS ne le permet pas. Nous n'avons pas besoin du stockage supplémentaire et cela n'a pas de sens de l'avoir, mais nous sommes coincés avec.

Nous ne pouvons pas non plus rétrograder de `db.t3.medium` à `db.t3.micro` car nous perdons l'accès à Performance Insights. Bien sûr, nous pourrions recréer Performance Insights car il est essentiellement construit sur Performance Schema qui est une fonctionnalité native de MySQL – mais cela représente tellement de temps d'ingénierie qui n'apporte rien en termes de valeur à notre client final.

## En conclusion

J'aime AWS et j'aime la facilité avec laquelle il a rendu l'accès au matériel pour des millions de développeurs. Mais je ne peux m'empêcher de me frustrer face à la mauvaise documentation entourant AWS et à la facilité avec laquelle on peut se tirer une balle dans le pied à moins d'être prêt à débourser constamment de l'argent.

Je sais que comprendre comment le matériel est utilisé est un must pour les ingénieurs logiciels. Mais cela semble être un double coup dur lorsque vous devez passer autant de temps à comprendre l'abstraction AWS qui devrait éliminer le besoin de s'inquiéter du matériel sous-jacent.

AWS dispose d'une base de données Aurora qui semble être une base de données gérée empêchant ce genre de problèmes de se produire. Mais parfois, il semble plus facile de simplement exécuter son propre matériel comme [Oxide Computer](https://oxide.computer/) encourage les gens à le faire.

_Note : Vous pouvez trouver cet article et d'autres sur mon blog [ici](https://redixhumayun.github.io/performance/2022/05/27/diagnosing-performance-issues.html)._