---
title: Comment les bases de données garantissent l'isolation - Contrôle de concurrence
  pessimiste vs optimiste expliqué
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2024-02-05T22:41:18.000Z'
originalURL: https://freecodecamp.org/news/how-databases-guarantee-isolation
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/cover--1-.png
tags:
- name: concurrency
  slug: concurrency
- name: database
  slug: database
seo_title: Comment les bases de données garantissent l'isolation - Contrôle de concurrence
  pessimiste vs optimiste expliqué
seo_desc: 'ACID (Atomicity, Consistency, Isolation, and Durability) is a set of guarantees
  when working with a DBMS. Pessimistic and optimistic concurrency control explains
  how databases achieve the “I” in ACID.

  Isolation is a guarantee that concurrently runnin...'
---

ACID (Atomicité, Cohérence, Isolation et Durabilité) est un ensemble de garanties lors de l'utilisation d'un SGBD. Le contrôle de concurrence pessimiste et optimiste explique comment les bases de données atteignent le "I" dans ACID.

L'isolation est une garantie que les transactions s'exécutant simultanément ne doivent pas interférer les unes avec les autres. C'est probablement la propriété ACID la plus importante, car différents SGBD peuvent souvent avoir différents niveaux d'isolation par défaut. Et vous devrez peut-être changer cela en fonction des besoins de votre application.

Dans un [article précédent](https://lightcloud.substack.com/p/acid-databases-explained), j'ai expliqué les deux principaux niveaux d'isolation utilisés par la plupart des SGBD. Ce sont les niveaux d'isolation [read committed](https://lightcloud.substack.com/i/140524854/read-committed) et [repeatable read](https://lightcloud.substack.com/i/140524854/repeatable-read).

Les contrôles de concurrence pessimiste et optimiste expliquent essentiellement certaines des façons dont une base de données est capable d'atteindre ces deux garanties d'isolation.

## Table des matières

1. [Contrôle de concurrence pessimiste](#heading-controle-de-concurrence-pessimiste)
   
2. [Analogie du contrôle de concurrence pessimiste](#heading-une-analogie-de-bibliotheque-pour-le-controle-de-concurrence-pessimiste)
   
3. [Exemple réel simple de contrôle de concurrence pessimiste en action](#heading-un-exemple-reel-simple-de-controle-de-concurrence-pessimiste-en-action)
   
4. [Avantages et inconvénients du contrôle de concurrence pessimiste](#heading-avantages-et-defis-du-controle-de-concurrence-pessimiste)
   
5. [Comment il garantit le niveau d'isolation Read Committed](#heading-comment-les-controles-de-concurrence-pessimistes-garantissent-le-niveau-disolation-read-committed)
   
6. [Contrôle de concurrence optimiste](#heading-controle-de-concurrence-optimiste)
   
7. [Exemple réel simple de contrôle de concurrence optimiste en action](#heading-un-exemple-reel-simple-de-controle-de-concurrence-optimiste-en-action)
   
8. [Avantages et inconvénients du contrôle de concurrence optimiste](#heading-avantages-et-defis-du-controle-de-concurrence-optimiste)
   
9. [Comment il garantit le niveau d'isolation Repeatable Read](#heading-comment-les-controles-de-concurrence-optimistes-garantissent-le-niveau-disolation-repeatable-read)
   
10. [Conclusion](#heading-conclusion)
   

## Contrôle de concurrence pessimiste

Avec le contrôle de concurrence pessimiste, le SGBD suppose que des conflits entre les transactions sont susceptibles de se produire. Il est pessimiste – c'est-à-dire qu'il suppose que si quelque chose peut mal tourner, cela se produira. Ce pessimisme empêche les conflits de se produire en les bloquant avant qu'ils n'aient une chance de commencer.

Pour prévenir ces conflits, il *verrouille* les données qu'une transaction utilise jusqu'à ce que la transaction soit terminée. Cette approche est 'pessimiste' car elle suppose le pire scénario – que chaque transaction pourrait conduire à un *conflit*. Les données sont donc verrouillées afin d'empêcher les conflits de se produire.

J'ai mentionné ici deux termes techniques qui nécessitent une clarification : *verrous* et *conflit*.

### Qu'est-ce que les verrous ?

Un verrou est un mécanisme utilisé pour contrôler l'accès à un élément de base de données, comme une ligne ou une table. Les verrous garantissent l'intégrité des données, si plusieurs transactions se produisent en même temps.

En termes très simples, un verrou est analogue à une réservation sur l'élément de la base de données. Une réservation, qu'il s'agisse d'un restaurant, d'un hôtel ou d'un train, empêche d'autres personnes d'utiliser la ressource que vous avez réservée pour une durée fixe. Les verrous fonctionnent de manière similaire.

Il existe deux types de verrous : un verrou de lecture et un verrou d'écriture.

Un verrou de lecture peut être partagé par plusieurs transactions essayant de lire le même élément de base de données. Mais il bloque les autres transactions de mettre à jour cet élément de base de données.

Un verrou d'écriture est exclusif – c'est-à-dire qu'il ne peut être détenu que par une seule transaction. Une transaction avec un verrou d'écriture sur un élément de base de données bloque toute autre transaction de lire ou de mettre à jour cet élément de base de données.

### Qu'est-ce que les conflits ?

Un conflit fait référence à une situation où plusieurs transactions tentent d'accéder et de modifier les mêmes données simultanément, de manière à pouvoir entraîner des incohérences ou des erreurs dans la base de données.

### Une analogie de bibliothèque pour le contrôle de concurrence pessimiste

Tout d'abord, décrivons une analogie pour un verrou d'écriture.

Imaginez que vous êtes dans une bibliothèque et que vous souhaitez emprunter un exemplaire papier d'un livre populaire, disons, Le Grand Gatsby de F. Scott Fitzgerald.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd683922-af28-4886-a6dc-6c121ac7e915_1858x1054.png align="left")

*Les verrous d'écriture sont analogues à l'emprunt d'un livre physique de la bibliothèque*

Avec un verrou d'écriture, le bibliothécaire suppose qu'il peut y avoir des conflits sur qui obtient le livre. Ils mettent donc en place une règle stricte pour éviter les conflits : une seule personne peut détenir la réservation pour un livre physique à la fois.

Lorsque vous réservez le livre, personne d'autre ne peut l'emprunter. Le livre est disponible pour être réservé à nouveau uniquement une fois qu'il est retourné. Cela est similaire à la façon dont un verrou d'écriture fonctionne.

Les verrous d'écriture sont exclusifs. Cela signifie qu'ils ne peuvent être détenus que par une seule transaction à la fois. De même, réserver un livre physique de la bibliothèque signifie que personne d'autre n'a accès à celui-ci. Seule la personne avec la réservation peut lire le livre, ou écrire dedans (bien qu'écrire dans un livre de bibliothèque soit une mauvaise pratique).

Les verrous de lecture fonctionnent un peu différemment.

Un verrou de lecture est analogue à quelqu'un faisant une réservation pour emprunter un e-book. Emprunter un e-book n'est pas une chose très populaire à faire, mais certaines bibliothèques offrent un tel service.

De nombreuses personnes peuvent faire la même réservation pour le même e-book sans aucun conflit. Une personne empruntant une version e-book du Grand Gatsby n'empêche pas les autres de faire de même. Mais personne qui emprunte un e-book ne peut le mettre à jour, par exemple en griffonnant des notes qui peuvent être vues par d'autres.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb2c7acc-c32e-47f6-a412-2000ae14da2b_2156x1344.png align="left")

*Les verrous de lecture sont analogues à l'emprunt d'un e-book de la bibliothèque*

Le contrôle de concurrence pessimiste est très sûr car il empêche les conflits de se produire en les bloquant avant qu'ils n'aient une chance de commencer. Un verrou d'écriture sur un élément de base de données empêche les autres transactions de lire ou de mettre à jour cet élément tant que ce verrou est détenu, de manière similaire à la façon dont une bibliothèque empêche plus d'une personne d'essayer d'emprunter le même livre physique au même moment.

Un verrou de lecture sur un élément de base de données permet à d'autres transactions d'obtenir également un verrou de lecture pour cet élément, mais empêche les transactions de mettre à jour cet élément. Cela est analogue à l'emprunt d'un e-book, où plusieurs personnes peuvent emprunter le même e-book au même moment, mais ne peuvent pas y apporter de mises à jour.

### Un exemple réel simple de contrôle de concurrence pessimiste en action

Illustrons comment fonctionne le contrôle de concurrence pessimiste à l'aide d'un exemple simple impliquant une table de base de données de solde bancaire. Supposons que nous avons une table nommée Comptes avec les colonnes suivantes : AccountID et Balance.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d9e2dd5-5abe-46ea-bbb6-033f1d5bc663_1096x534.png align="left")

*Colonnes de la base de données pour AccountID et Balance*

Deux transactions, T1 et T2, ont l'intention de mettre à jour le solde du compte 12345. T1 souhaite retirer 300 $, et T2 souhaite déposer 400 $. À la fin de ces deux transactions, le solde du compte devrait être de 1600 $.

Voici les étapes de fonctionnement avec des verrous d'écriture :

1. Début de T1 (Retrait) : T1 demande à mettre à jour le solde de AccountID 12345. Le système de base de données place un verrou d'écriture exclusif sur la ligne pour AccountID 12345, empêchant les autres transactions de lire ou d'écrire sur cette ligne jusqu'à ce que T1 soit terminée. T1 lit le solde (1500 $).
   
2. Traitement de T1 : T1 calcule le nouveau solde à 1200 $ (1500 $ - 300 $).
   
3. Validation de T1 : T1 écrit le nouveau solde (1200 $) dans la base de données. Après une validation réussie, T1 libère le verrou exclusif sur AccountID 12345.
   
4. Début de T2 (Dépôt) après la fin de T1 : Maintenant que T1 est terminée et que le verrou est libéré, T2 peut commencer. T2 tente de lire et de mettre à jour le solde pour AccountID 12345. Le système de base de données place un verrou exclusif sur la ligne pour AccountID 12345 pour T2, garantissant qu'aucune autre transaction ne peut interférer. T2 lit le solde mis à jour (1200 $).
   
5. Traitement de T2 : T2 calcule le nouveau solde à 1600 $ (1200 $ + 400 $).
   
6. Validation de T2 : T2 écrit le nouveau solde (1600 $) dans la base de données. Après une validation réussie, T2 libère le verrou exclusif sur AccountID 12345.
   
7. Résultat : La table Comptes est mise à jour en utilisant des verrous Après T1 : 1200 $ Après T2 : 1600 $.
   

Sans un verrou d'écriture dans cet exemple, T1 et T2 pourraient lire le solde initial de 1500 $ en même temps. Ainsi, au lieu d'un solde de 1200 $ après que T1 ait été validée, T2 lit toujours le solde initial de 1500 $ et ajoute 400 $. Cela entraînerait un solde final de 1500 $ + 400 $ = 1900 $ (au lieu de 1600 $).

L'absence de verrouillage a créé de l'argent gratuit, ce qui n'est jamais une mauvaise chose pour un client. Mais, si de l'argent peut être créé à partir de rien à cause de ces conflits, il peut aussi disparaître, et la réduction accidentelle des soldes bancaires est un moyen rapide de rendre les clients mécontents.

### Avantages et défis du contrôle de concurrence pessimiste

Tout comme la réservation d'un livre garantit qu'il est mis de côté pour une personne, le contrôle de concurrence pessimiste verrouille les données pour une seule transaction. Les autres transactions ne peuvent pas accéder ou modifier ces données jusqu'à ce que le verrou soit libéré.

Cette méthode empêche deux personnes d'essayer de prendre le même livre populaire au même moment, évitant ainsi les conflits. De même, dans les bases de données, elle empêche les conflits dus aux transactions simultanées avant qu'ils n'aient une chance de commencer.

Mais cette approche peut être inefficace. Le livre réservé peut rester sur l'étagère des réservations pendant un certain temps, empêchant les autres de le lire.

Dans les bases de données, ce mécanisme de verrouillage peut entraîner une sous-utilisation des ressources et un ralentissement de la vitesse de traitement des transactions, puisque un sous-ensemble des données est verrouillé et inaccessible aux autres transactions.

### Comment les contrôles de concurrence pessimistes garantissent le niveau d'isolation Read Committed

Alors, comment exactement le contrôle de concurrence pessimiste fonctionne-t-il pour garantir l'isolation, c'est-à-dire le "I" dans ACID ? Les détails d'implémentation peuvent varier selon les différents SGBD. Mais l'explication ici montre l'approche générale.

Rappelons que le niveau d'isolation [read committed](https://lightcloud.substack.com/i/140524854/read-committed) empêche les écritures et lectures sales.

#### Prévention des écritures sales

Écraser des données qui ont déjà été écrites par une autre transaction mais pas encore validées est appelé une écriture sale. Une approche courante pour prévenir les écritures sales est d'utiliser le contrôle de concurrence pessimiste. Par exemple, en utilisant un verrou d'écriture au niveau de la ligne.

Lorsque une transaction souhaite modifier une ligne, elle acquiert un verrou sur cette ligne et le maintient jusqu'à ce que la transaction soit terminée. Rappelons que les verrous d'écriture ne peuvent être détenus que par une seule transaction. Cela empêche une autre transaction d'acquérir un verrou pour modifier cette ligne.

#### Prévention des lectures sales

Lire des données d'une autre transaction qui n'ont pas encore été validées est appelé une lecture sale. Les lectures sales sont empêchées en utilisant soit un verrou de lecture soit un verrou d'écriture. Une fois qu'une transaction acquiert un verrou de lecture sur un élément de base de données, elle empêchera les mises à jour de cet élément.

Mais que se passe-t-il si vous essayez de lire quelque chose qui est déjà en cours de mise à jour mais que la transaction n'a pas encore été validée ? Dans ce cas, le verrou d'écriture sauve la situation.

Puisque les verrous d'écriture sont exclusifs (ne peuvent pas être partagés avec d'autres transactions), toute transaction souhaitant lire le même élément de base de données devra attendre jusqu'à ce que la transaction avec le verrou d'écriture soit validée (ou abandonnée, si elle échoue). Cela empêche les autres transactions de lire les changements non validés.

## Contrôle de concurrence optimiste

Avec le contrôle de concurrence optimiste, les transactions n'obtiennent pas de verrous sur les données lorsqu'elles lisent ou écrivent. Le terme "Optimiste" dans le nom vient de l'hypothèse que les conflits sont peu probables, donc les verrous ne sont pas nécessaires. Si quelque chose ne va pas, les conflits seront toujours empêchés et tout ira bien.

Contrairement au contrôle de concurrence pessimiste – qui empêche les conflits de se produire en les bloquant avant qu'ils n'aient une chance de commencer – le contrôle de concurrence optimiste vérifie les conflits à la fin d'une transaction.

Avec le contrôle de concurrence optimiste, plusieurs transactions peuvent lire ou mettre à jour le même élément de base de données sans acquérir de verrous. Comment cela fonctionne-t-il exactement ?

Chaque fois qu'une transaction souhaite mettre à jour un élément de base de données, disons une ligne, elle lira également deux colonnes supplémentaires ajoutées à chaque table par le SGBD – l'horodatage et le numéro de version. Avant que cette transaction ne soit validée, elle vérifie si une autre transaction a apporté des modifications à cette ligne en confirmant si le numéro de version et l'horodatage sont les mêmes.

S'ils ont changé, cela signifie qu'une autre transaction a mis à jour cette ligne, donc la transaction initiale devra être réessayée.

### Un exemple réel simple de contrôle de concurrence optimiste en action

Illustrons comment fonctionne le contrôle de concurrence optimiste à l'aide d'un exemple simple impliquant une table de base de données de solde bancaire. Supposons que nous avons une table nommée Comptes avec les colonnes suivantes : AccountID, Balance, VersionNumber et Timestamp.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc46a7d00-c1b9-46c6-80c0-0bc1a7aba9ae_2180x542.png align="left")

*Tableau montrant les colonnes AccountID, Balance, VersionNumber et Timestamp*

Deux transactions, T1 et T2, ont l'intention de mettre à jour le solde du compte 12345 en même temps. T1 souhaite retirer 200 $, et T2 souhaite déposer 300 $. À la fin de ces deux transactions, le solde du compte devrait être de 1100 $.

Voici les étapes de fonctionnement :

1. Début des transactions : T1 lit le solde, le numéro de version et l'horodatage pour AccountID 12345. Simultanément, T2 lit la même ligne avec le même solde, numéro de version et horodatage.
   
2. Traitement : T1 calcule le nouveau solde à 800 $ (1000 $ - 200 $) mais ne l'écrit pas immédiatement. T2 calcule le nouveau solde à 1300 $ (1000 $ + 300 $) mais attend également pour valider.
   
3. Tentative de validation de T1 : Avant de valider, T1 vérifie le VersionNumber et le Timestamp actuels de AccountID 12345 dans la base de données. Comme aucune autre transaction n'a modifié la ligne, T1 met à jour le solde à 800 $, incrémente le VersionNumber à 2, met à jour le Timestamp et valide avec succès.
   
4. Tentative de validation de T2 : T2 tente de valider en vérifiant d'abord le VersionNumber et le Timestamp. T2 constate que le VersionNumber et le Timestamp ont changé (maintenant VersionNumber est 2, et Timestamp est mis à jour), indiquant qu'une autre transaction (T1) a mis à jour la ligne. Comme le numéro de version et l'horodatage ont changé, T2 réalise qu'il y avait un conflit.
   
5. Résolution pour T2 : T2 doit redémarrer sa transaction. Il relit le solde mis à jour de 800 $, le nouveau VersionNumber 2 et le Timestamp mis à jour. T2 recalcule le nouveau solde à 1100 $ (800 $ + 300 $), met à jour le VersionNumber à 3, met à jour le Timestamp et valide avec succès.
   

Résultat : La table Comptes est mise à jour de manière séquentielle et sûre sans aucun verrou : Après T1 : 800 $, VersionNumber : 2. Après T2 : 1100 $, VersionNumber : 3.

### Avantages et défis du contrôle de concurrence optimiste

Du côté positif, éviter les verrous permet des niveaux élevés de concurrence. Cela est particulièrement bénéfique dans les charges de travail intensives en lecture où les transactions sont moins susceptibles d'entrer en conflit, permettant au système de traiter plus de transactions dans une période donnée. Par exemple, les sauvegardes de bases de données et les requêtes analytiques typiquement utilisées dans un entrepôt de données.

Mais dans les scénarios où les conflits sont fréquents, le coût de l'annulation et de la nouvelle tentative répétées des transactions peut l'emporter sur les avantages de l'évitement des verrous, rendant le contrôle de concurrence optimiste moins efficace.

### Comment les contrôles de concurrence optimistes garantissent le niveau d'isolation Repeatable Read

Le repeatable read est un niveau d'isolation plus strict en ce sens qu'il offre les mêmes garanties que l'isolation read committed, plus il garantit que les lectures sont répétables.

Un repeatable read garantit que si une transaction lit une ligne de données, toute lecture ultérieure de cette même ligne de données dans la même transaction donnera le même résultat, indépendamment des modifications apportées par d'autres transactions. Cette cohérence est maintenue tout au long de la durée de la transaction.

Comment un repeatable read peut-il être atteint ? Le contrôle pessimiste utilisant un verrou de lecture peut aider à cela, puisque une transaction avec un verrou de lecture sur un élément de base de données empêchera cet élément d'être mis à jour. Mais cela peut être inefficace, puisque une transaction de lecture longue peut bloquer les mises à jour de cet élément de base de données.

Le Contrôle de Concurrence Multi-Version (MVCC) est une méthode de contrôle de concurrence utilisée par certains SGBD pour permettre à plusieurs transactions d'accéder aux mêmes données simultanément sans verrouiller les données. Cela en fait un choix populaire pour réduire la contention des verrous et améliorer la scalabilité des bases de données.

Le MVCC atteint cela en conservant plusieurs versions des objets de données, ce qui aide à gérer différents niveaux de visibilité pour les transactions en fonction de leurs horodatages ou numéros de version.

## Conclusion

Un verrou est un mécanisme utilisé pour contrôler l'accès à un élément de base de données, comme une ligne ou une table. En termes très simples, il est analogue à une réservation sur un élément de base de données.

Le contrôle de concurrence pessimiste suppose le pire. Il suppose que les conflits sont susceptibles de se produire, donc des verrous sont utilisés pour bloquer les transactions qui peuvent causer des conflits avant qu'elles n'aient une chance de commencer.

Dans les situations où les conflits sont courants, comme dans une application intensive en écriture, cette approche peut prévenir les frais généraux associés aux annulations et nouvelles tentatives fréquentes (qui se produisent dans le contrôle de concurrence optimiste) en garantissant un accès exclusif aux éléments de la base de données pendant les transactions.

Le contrôle de concurrence optimiste suppose le meilleur. Il suppose que les conflits sont peu probables, donc les verrous ne sont pas nécessaires pour arrêter les transactions avant qu'elles ne commencent. Au lieu de cela, les conflits potentiels sont vérifiés à la fin d'une transaction et, si des conflits sont trouvés, la transaction est abandonnée ou réessayée.

Le contrôle de concurrence optimiste est utile pour les transactions intensives en lecture avec des écritures peu fréquentes, car il permet à plusieurs transactions de se poursuivre sans avoir besoin d'utiliser un verrou, ce qui peut être inefficace.