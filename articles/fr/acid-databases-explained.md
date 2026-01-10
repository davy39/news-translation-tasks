---
title: Bases de données ACID – Atomicité, Cohérence, Isolation et Durabilité expliquées
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2024-01-17T17:45:53.000Z'
originalURL: https://freecodecamp.org/news/acid-databases-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/cover-fcc.png
tags:
- name: database
  slug: database
seo_title: Bases de données ACID – Atomicité, Cohérence, Isolation et Durabilité expliquées
seo_desc: 'ACID stands for Atomicity, Consistency, Isolation and Durability. These
  are four key properties that most database management systems (DBMS) offer as guarantees
  when handling transactions.

  Most popular DBMS like MySQL, PostgresSQL and Oracle have ACI...'
---

ACID signifie Atomicité, Cohérence, Isolation et Durabilité. Ce sont quatre propriétés clés que la plupart des systèmes de gestion de bases de données (SGBD) offrent comme garanties lors de la gestion des transactions.

La plupart des SGBD populaires comme [MySQL](https://dev.mysql.com/doc/refman/8.0/en/mysql-acid.html), [PostgresSQL](https://www.postgresql.org/about/) et [Oracle](https://docs.oracle.com/cd/F51125_01/docs.85/SDS%20PI/acid-compliant-transactions.html#GUID-ECB79D66-46DE-4F48-93DC-8677E7BB44EF) ont des garanties ACID dès la sortie de la boîte. D'autres ont des garanties ACID partielles comme [Redis](https://www.oreilly.com/library/view/redis-cookbook/9781449311353/ch01.html#:~:text=Redis%20provides%20partial%20ACID%20compliance,also%20be%20a%20key%20factor.), DynamoDB et Cassandra. La tendance, cependant, semble être que de plus en plus de SGBD offrent la conformité ACID.

Il est important de noter que bien que de nombreux SGBD puissent dire qu'ils sont conformes ACID, la mise en œuvre de cette conformité peut varier.

Ainsi, par exemple, si l'isolation est une propriété clé dont vous avez besoin pour une application que vous construisez, vous devez comprendre comment exactement votre SGBD choisi met en œuvre l'isolation.

Cet article expliquera ce que sont les transactions et passera en revue, en détail, ce que signifient l'atomicité, la cohérence, l'isolation et la durabilité, en utilisant des analogies et des exemples concrets.

### Table des matières :

1. [Qu'est-ce que les transactions ?](#heading-quest-ce-que-les-transactions)
   
2. [Que signifie l'atomicité ?](#heading-que-signifie-latomicite)
   
3. [Que signifie la cohérence ?](#heading-que-signifie-la-coherence)
   
4. [Que signifie l'isolation ?](#heading-que-signifie-lisolation)
   
5. [Que signifie la durabilité ?](#heading-que-signifie-la-durabilite)
   
6. [Mettre tout ensemble](#heading-mettre-tout-ensemble)
   

## Qu'est-ce que les transactions ?

Beaucoup de choses peuvent mal tourner lors de l'utilisation d'une base de données :

* le matériel ou le logiciel de la base de données peut tomber en panne
   
* l'application appelant la base de données peut tomber en panne en cours d'opération
   
* le réseau peut être saturé avec plus de trafic qu'il ne peut gérer (le rendant inopérable)
   
* plusieurs clients peuvent effectuer des écritures en même temps qui écrasent les modifications des autres
   
* les clients peuvent lire des données fantômes qui ne devraient pas être dans la base de données
   

Et ainsi de suite – ceci n'est en aucun cas une liste exhaustive des choses qui peuvent mal tourner.

Puisque les choses peuvent échouer de plus de manières que nous ne pouvons possiblement anticiper, essayer de prévenir chaque échec possible peut devenir inutilement coûteux et compliqué. Au lieu de cela, il est préférable de concevoir un système qui peut continuer à fonctionner malgré un échec. Les transactions nous permettent de faire cela.

Les transactions servent un seul but : elles s'assurent qu'un système est [**tolérant aux pannes**](https://lightcloud.substack.com/i/59017006/fault-tolerance)**.** Si une panne se produit dans un système, le système peut-il continuer à fonctionner sans catastrophe complète ? Autrement dit, le système peut-il tolérer les pannes ? Une réponse de 'oui' à cette question signifie que ce système est tolérant aux pannes.

Alors, qu'est-ce qu'une transaction exactement ?

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F718d52b8-c016-4746-a1eb-73b6aac6d5fa_636x960.png align="left")

*Pas ce type de transaction*

Une transaction est une [abstraction](https://lightcloud.substack.com/p/cloud-computing-abstractions-explained). C'est une collection d'opérations (lectures et écritures) qui sont traitées comme une seule opération logique.

Imaginez que vous souhaitez acheter un seul livre dans une boutique en ligne, par exemple amazon.com. Les étapes ci-dessous montrent une vue simplifiée de ce qui doit se passer :

1. Tout d'abord, vous sélectionnez le livre, ce qui ajoute l'article à votre panier.
   
2. La quantité en stock du livre est vérifiée pour s'assurer qu'elle est valide (c'est-à-dire que la valeur du stock pour le titre que vous achetez doit être supérieure à 0).
   
3. Vous cliquez sur 'acheter', ce qui met à jour l'inventaire d'Amazon pour le livre et le diminue de 1 (puisque vous achetez un seul livre).
   
4. De plus, le solde de votre compte bancaire est mis à jour pour tenir compte du coût du livre.
   

Une transaction garantit que toutes les opérations liées à l'achat sont traitées comme une seule opération. Si une partie de la transaction échoue, l'ensemble de la transaction est annulé, laissant la base de données dans un état comme si le client n'avait jamais tenté l'achat, maintenant ainsi l'intégrité des données.

La transaction est validée lorsque toutes les opérations au sein de la transaction sont complétées avec succès et que leurs résultats sont enregistrés de manière permanente. Cette permanence est généralement obtenue en écrivant les modifications dans le stockage de la base de données, qui peut être sur disque pour les bases de données traditionnelles ou en mémoire pour les bases de données en mémoire comme Redis.

En traitant toutes ces différentes opérations comme une seule opération logique, la base de données est en mesure d'offrir certaines garanties quant à la manière dont elle peut être tolérante aux pannes. Ces garanties sont l'**atomicité**, la **cohérence**, l'**isolation** et la **durabilité**.

## Que signifie l'atomicité ?

L'atomicité signifie simplement que toutes les requêtes dans une transaction doivent réussir pour que la transaction réussisse. Si une requête échoue, l'ensemble de la transaction échoue.

### Un restaurant atomique

Imaginez utiliser une machine en libre-service dans un restaurant de restauration rapide. La transaction dans ce cas est la commande de nourriture et se compose de deux opérations distinctes :

1. Sélectionner la nourriture
   
2. Effectuer le paiement
   

Ces deux opérations doivent réussir pour que la transaction réussisse. Si l'une d'elles échoue, la transaction échoue.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb52901d6-a9e0-43a7-a198-d56ca2a82219_544x886.png align="left")

*Client passant une commande dans un restaurant "atomique"*

Vous sélectionnez votre burger, vos frites et une boisson dans le menu tactile. La machine vous invite à payer, et ce n'est qu'après que votre paiement a été traité avec succès qu'elle envoie votre commande à la cuisine. Quelques instants plus tard, votre commande entière est prête, et vous la récupérez au comptoir.

C'est une opération atomique : la transaction (commande de nourriture) est soit entièrement complétée (si vous sélectionnez votre article de nourriture et effectuez un paiement) soit pas complétée du tout.

L'échec de l'une ou l'autre partie de la transaction signifie que l'ensemble de la transaction échouera. Si votre paiement échoue, la machine ne traitera aucune partie de la commande, donc la transaction échoue. Si vous effectuez un paiement sans sélectionner d'article de nourriture, la transaction échoue également, car il n'y a rien à préparer pour la cuisine.

### Un restaurant non atomique

Maintenant, considérons l'alternative, un restaurant traditionnel où vous commandez plusieurs plats. À mesure que chaque plat est préparé, il est apporté à votre table.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F045c9ec7-dbb9-45b7-ad4d-357f7b7cc37c_888x1026.png align="left")

*Client passant une commande dans un restaurant "non atomique"*

Encore une fois, la transaction est la commande de nourriture et se compose de deux opérations distinctes :

1. Sélectionner la nourriture
   
2. Effectuer le paiement
   

Dans ce restaurant non atomique, l'échec du paiement n'empêche pas la transaction de se compléter, puisque vous payez après avoir terminé votre repas. Les échecs partiels ne provoquent pas l'échec d'une transaction.

Cela crée un risque pour le restaurant. Les clients qui choisissent de manger et de partir sans payer peuvent commander de la nourriture à leur guise et simplement partir sans payer, causant une perte financière pour le restaurant.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4136ceee-82b9-4cf0-b0de-5a0af3f1aa71_2218x1278.png align="left")

*Les restaurants non atomiques sont à risque de clients qui mangent et partent sans payer*

### Transactions atomiques

Si plusieurs requêtes SQL sont regroupées dans une transaction, l'atomicité est une garantie que, si l'une des requêtes échoue pour une raison quelconque (problèmes matériels, d'application ou de réseau), alors la transaction est annulée et la base de données revient à son état précédent, comme si rien ne s'était passé.

Sans atomicité, si une panne se produit alors que certaines requêtes sont en cours d'exécution, il est difficile de savoir quelles requêtes ont été validées (c'est-à-dire complétées) et lesquelles ne l'ont pas été. Exécuter à nouveau les requêtes après une panne peut aggraver le problème, puisque vous risquez d'introduire des données incorrectes dans la base de données en réexécutant des requêtes qui ont précédemment réussi.

Les transactions atomiques empêchent une telle incertitude, puisque vous savez que si la transaction précédente a échoué, elle a échoué dans son intégralité, et vous pouvez simplement réessayer sans vous soucier d'introduire des données incohérentes.

## Que signifie la cohérence ?

La cohérence peut signifier différentes choses dans le cloud/l'ingénierie logicielle, selon le contexte. Dans le cas de ACID, le "C" a probablement été ajouté pour faire fonctionner l'acronyme.

La cohérence dans le contexte de ACID signifie *cohérence des données*, qui est définie par le créateur de la base de données. Le terme technique pour la cohérence des données est appelé intégrité référentielle. L'intégrité référentielle est une méthode pour s'assurer que les relations entre les tables restent cohérentes. Elle est généralement appliquée par l'utilisation de clés étrangères.

Pour comprendre l'intégrité référentielle, considérons ce qui suit.

Imaginez un système de bibliothèque avec deux types de cartes : une carte de livre et une carte d'emprunteur.

* La carte de livre répertorie tous les livres disponibles dans la bibliothèque.
   
* La carte d'emprunteur suit quels livres sont empruntés par quels membres.
   

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82ea7c95-f55f-4cb6-86ea-47c11399b5c7_2324x1316.png align="left")

*Une carte de livre et une carte d'emprunteur pour une bibliothèque*

La règle de la bibliothèque est qu'un livre ne peut être répertorié sur une carte d'emprunteur que s'il existe sur une carte de livre. C'est l'intégrité référentielle. Si quelqu'un essaie de répertorier un livre sur une carte d'emprunteur qui n'est pas sur la carte de livre (c'est-à-dire un livre qui n'existe pas dans la bibliothèque), le système ne le permettra pas.

Alors que l'atomicité, l'isolation et la durabilité sont des propriétés intrinsèques à la base de données elle-même, la cohérence des données, ou l'intégrité référentielle, n'est pas une propriété intrinsèque à la base de données.

La cohérence est définie par le créateur de la base de données. L'application appelant la base de données s'appuie sur les propriétés d'atomicité et d'isolation de la base de données pour maintenir cette cohérence.

## Que signifie l'isolation ?

L'isolation est une garantie que les transactions s'exécutant simultanément ne doivent pas interférer les unes avec les autres. La simultanéité fait ici référence à deux transactions ou plus essayant de modifier ou de lire les mêmes enregistrements de la base de données en même temps.

Il existe trois niveaux d'isolation des transactions. Je vais simplement expliquer les deux principaux ci-dessous, classés par ordre du moins strict au plus strict.

### Lecture validée

Cela donne deux garanties. Il empêche les lectures sales et les écritures sales.

**Pas de lectures sales** : Lire des données d'une autre transaction qui n'a pas encore été validée est appelé une lecture sale. Avec le niveau d'isolation de lecture validée, vous ne verrez que les données qui ont été validées par une autre transaction.

**Pas d'écritures sales** : Écraser des données qui ont déjà été écrites par une autre transaction mais pas encore validées est appelé une écriture sale.

Pour comprendre comment fonctionne l'isolation de lecture validée, considérons l'exemple suivant.

Imaginez un restaurant de restauration rapide avec un seul burger spécial disponible, et deux clients affamés, Marie et Marko, essayant de l'acheter simultanément.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec0fd185-63c9-4821-bcac-b0140f2f4183_2360x1322.png align="left")

*Deux clients commandant un burger en même temps*

1. Marie vérifie la disponibilité des burgers et voit le dernier disponible. Sans le savoir, la commande de Marko est en cours de traitement mais n'a pas encore été finalisée dans le système, car il n'a pas payé. Puisque sa commande n'a pas encore été finalisée, Marie n'est pas au courant que sa commande est en conflit avec la sienne. Cela est similaire à une transaction lisant les données les plus récemment validées, où elle ne voit pas les modifications non validées (comme la commande en attente de Marko).
   
2. Marie passe une commande sur la base de ces informations incomplètes, pensant qu'un burger est disponible.
   
3. Une fois que Marko a payé, le système est mis à jour pour montrer qu'il n'y a plus de burgers. Cela est similaire à une transaction étant validée.
   
4. La commande de Marie devra être annulée puisqu'il n'y a plus de burgers.
   

Le point clé ici est l'étape #3. Et si le paiement de Marko échouait à ce stade ? Alors la transaction ne serait pas validée et il y aurait encore un burger disponible pour Marie.

Dans cet exemple, l'isolation de lecture validée garantit que Marie n'est pas prématurément exclue de l'achat du burger simplement parce que quelqu'un d'autre a dit qu'il le voulait. Seules les transactions validées peuvent être lues. Par conséquent, le burger est disponible pour être commandé tant que personne n'a payé pour lui.

### Lecture répétable

La lecture répétable est un niveau d'isolation plus strict, en ce sens qu'elle a les mêmes garanties que l'isolation de lecture validée – plus elle garantit que les lectures sont répétables.

Une lecture répétable garantit que si une transaction lit une ligne de données, toute lecture ultérieure de cette même ligne de données dans la même transaction donnera le même résultat, indépendamment des modifications apportées par d'autres transactions. Cette cohérence est maintenue pendant toute la durée de la transaction.

Lorsque une transaction lit les mêmes données deux fois, mais voit une valeur différente à chaque lecture parce qu'une transaction validée a mis à jour la valeur entre les deux lectures, cela est appelé une lecture floue. Le niveau d'isolation de lecture répétable empêche les lectures floues.

Les lectures floues ne sont ni intrinsèquement bonnes ni mauvaises. Tout dépend de ce que vous essayez d'accomplir.

Les lectures floues sont mauvaises pour les transactions longues et en lecture seule, puisque de nouvelles écritures sont susceptibles de se produire pendant la transaction et cela peut causer des incohérences dans les données. Des exemples de transactions longues et en lecture seule sont une sauvegarde de base de données et des requêtes analytiques typiquement utilisées dans un entrepôt de données.

Les lectures répétables sont généralement mises en œuvre par le SGBD en lisant à partir d'un instantané de la base de données qui reste inchangé pendant la durée de la transaction, ignorant ainsi toute nouvelle écriture validée pendant cette période.

## Que signifie la durabilité ?

La durabilité est une garantie que les modifications apportées par une transaction validée ne doivent pas être perdues. Toutes les transactions validées doivent être persistées sur un stockage durable et non volatile, c'est-à-dire sur disque. Cela garantit que toutes les transactions validées sont protégées même si la base de données plante.

Naturellement, la durabilité ne peut pas protéger contre la destruction du disque qui stocke les données. Une redondance supplémentaire peut être ajoutée en ayant des sauvegardes de votre base de données stockées séparément de l'originale.

## Mettre tout ensemble

ACID (Atomicité, Cohérence, Isolation et Durabilité) fournit un ensemble de garanties lors de l'utilisation d'un SGBD. Bien que la plupart des SGBD relationnels soient conformes à ACID, la mise en œuvre de cette conformité peut varier.

L'atomicité garantit que toutes les parties d'une transaction sont complétées ou aucune du tout. Les échecs partiels ne sont pas autorisés.

La cohérence, ou intégrité référentielle, garantit que les données restent exactes et fiables, en adhérant à des règles prédéfinies. Contrairement aux autres priorités, la cohérence n'est pas intrinsèque au SGBD lui-même. Au lieu de cela, l'application appelant la base de données s'appuie sur les propriétés d'atomicité et d'isolation de la base de données pour maintenir la cohérence.

L'isolation est une garantie que les transactions s'exécutant simultanément ne doivent pas interférer les unes avec les autres. C'est probablement la propriété la plus importante car un SGBD peut souvent avoir différents niveaux d'isolation par défaut, qui peuvent devoir être changés en fonction de ce qui est nécessaire pour votre application.

Enfin, la durabilité est une garantie que les modifications apportées par une transaction validée ne doivent pas être perdues.