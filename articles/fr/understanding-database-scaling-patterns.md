---
title: Un guide pour comprendre les modèles de mise à l'échelle des bases de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-30T17:07:05.000Z'
originalURL: https://freecodecamp.org/news/understanding-database-scaling-patterns
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/database-1954920_1920.jpg
tags:
- name: coding
  slug: coding
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: scaling
  slug: scaling
- name: technology
  slug: technology
seo_title: Un guide pour comprendre les modèles de mise à l'échelle des bases de données
seo_desc: 'By Kousik Nath

  There are lot of articles online describing database scalability patterns, but they
  are mostly scattered articles — just techniques that are defined haphazardly without
  much context. I find that they are not defined in a step by step m...'
---

Par Kousik Nath

Il existe de nombreux articles en ligne décrivant les modèles de scalabilité des bases de données, mais ils sont pour la plupart des articles épars — juste des techniques définies de manière désordonnée sans beaucoup de contexte. Je trouve qu'ils ne sont pas définis étape par étape, et ne discutent pas de quand choisir quelle option de mise à l'échelle, quelles options de mise à l'échelle sont réalisables en pratique, et pourquoi. 

Par conséquent, je prévois de discuter de certaines de ces techniques en détail dans de futurs articles. Pour commencer, je pense qu'il est préférable de discuter des techniques étape par étape avec un certain contexte à ma manière. Cet article est un article de haut niveau — je ne discuterai pas des techniques de mise à l'échelle en détail ici, mais je fournirai un aperçu. Alors, commençons.

### Une étude de cas

Supposons que vous avez créé une startup qui propose du covoiturage à moindre coût. Initialement, lorsque vous commencez, vous ciblez une ville et vous avez à peine des dizaines de clients après votre publicité initiale. 

Vous enregistrez tous les clients, les trajets, les lieux, les données de réservation et l'historique des trajets des clients dans la même base de données ou très probablement sur une seule machine physique. Il n'y a pas de cache sophistiqué ni de pipeline de big data pour résoudre les problèmes puisque votre application est très nouvelle. Cela est parfait pour votre cas d'utilisation à ce moment-là, car il y a très peu de clients et votre système réserve à peine 1 trajet en 5 minutes, par exemple.

Mais avec le temps, de plus en plus de personnes commencent à s'inscrire dans votre système puisque vous êtes le service le moins cher sur le marché et grâce à votre promotion et à vos publicités. Vous commencez à réserver, disons, 10 réservations par minute, et lentement le nombre augmente à 20, 30 réservations par minute. 

À ce stade, vous réalisez que le système a commencé à mal performer : la latence de l'API a considérablement augmenté, et certaines transactions sont en interlock ou en famine et finissent par échouer. Votre application met plus de temps à répondre, ce qui cause de l'insatisfaction chez les clients. Que pouvez-vous faire pour résoudre le problème ?

## Modèle 1 - Optimisation des requêtes et mise en œuvre du pool de connexions :

La première solution qui vient à l'esprit est que le cache utilise fréquemment des données non dynamiques comme l'historique des réservations, l'historique des paiements, les profils utilisateurs, etc. Mais après cette mise en cache au niveau de l'application, vous ne pouvez pas résoudre le problème de latence des API exposant des données dynamiques comme l'emplacement actuel du conducteur, les taxis les plus proches pour un client donné ou le coût actuel du trajet à un certain moment après le début du trajet. 

Vous identifiez que votre base de données est probablement fortement normalisée, vous introduisez donc quelques colonnes redondantes (ces colonnes apparaissent fréquemment dans les clauses `WHERE` ou `JOIN ON` des requêtes) dans les tables très utilisées pour le bien de la dénormalisation. Cela réduit les requêtes de jointure, divise une grande requête en plusieurs requêtes plus petites et additionne leurs résultats dans la couche application.

Une autre optimisation parallèle que vous pouvez faire est de régler les connexions à la base de données. Les bibliothèques clientes de bases de données et les bibliothèques externes sont disponibles dans presque tous les langages de programmation. Vous pouvez utiliser des bibliothèques de pool de connexions pour mettre en cache les connexions à la base de données ou configurer la taille du pool de connexions dans le système de gestion de base de données lui-même. 

La création de toute connexion réseau est coûteuse car elle nécessite une certaine communication aller-retour entre le client et le serveur. Le pooling de connexions peut vous aider à optimiser le nombre de connexions. Les bibliothèques de pool de connexions peuvent vous aider à multiplexer les connexions — plusieurs threads d'application peuvent utiliser la même connexion de base de données. Je verrai si je peux expliquer le pooling de connexions en détail dans un article séparé plus tard.

Vous mesurez la latence de vos API et trouvez probablement une latence réduite de 20 à 50 % ou plus. C'est une bonne optimisation à ce stade.

Vous avez maintenant étendu votre activité à une autre ville, plus de clients s'inscrivent, vous commencez lentement à faire 80 à 100 réservations par minute. Votre système n'est pas en mesure de gérer cette échelle. Vous voyez à nouveau que la latence de l'API a augmenté, la couche de base de données a abandonné, mais cette fois, aucune optimisation de requête ne vous donne un gain de performance significatif. Vous vérifiez les métriques du système, vous trouvez que l'espace disque est presque plein, le CPU est occupé 80 % du temps, la RAM se remplit très rapidement.

## Modèle 2 - Mise à l'échelle verticale ou Scale Up :

Après avoir examiné toutes les métriques du système, vous savez qu'il n'y a pas d'autre solution facile que de mettre à niveau le matériel du système. Vous augmentez la taille de votre RAM de 2 fois, vous augmentez l'espace disque de, disons, 3 fois ou plus. Cela s'appelle la mise à l'échelle verticale ou la mise à niveau de votre système. Vous informez votre équipe d'infrastructure ou votre équipe devops ou les agents du centre de données tiers de mettre à niveau votre machine.

**Mais comment configurez-vous la machine pour la mise à l'échelle verticale ?**

Vous allouez une machine plus grande. Une approche consiste à ne pas migrer les données manuellement de l'ancienne machine, mais à configurer la nouvelle machine comme `réplica` de la machine existante (`primaire`)—créer une configuration temporaire de `réplica primaire`. Laissez la réplication se faire naturellement. Une fois la réplication terminée, [promouvez la nouvelle machine en primaire](https://blog.pythian.com/mysql-recipes-promoting-a-slave-to-master-or-changing-masters/?source=post_page---------------------------) et mettez l'ancienne machine hors ligne. Puisque la machine plus grande est censée servir toutes les requêtes, toutes les lectures/écritures se feront sur cette machine.

Cool. Votre système est à nouveau opérationnel avec des performances accrues.

Votre entreprise se porte très bien et vous décidez de vous étendre à 3 autres villes — vous êtes maintenant opérationnel dans 5 villes au total. Le trafic est 3 fois plus élevé qu'avant, vous êtes censé faire environ 300 réservations par minute. Avant même d'atteindre cet objectif de réservation, vous rencontrez à nouveau des problèmes de performance, la taille de l'index de la base de données augmente fortement en mémoire, elle nécessite un entretien constant, le balayage des tables avec l'index devient plus lent que jamais. Vous calculez le coût de la mise à niveau de la machine, mais vous n'êtes pas convaincu par le coût. Que faites-vous maintenant ?

## Modèle 3 - Ségrégation des responsabilités de commande et de requête (CQRS) :

Vous identifiez que la grande machine n'est pas en mesure de gérer toutes les requêtes de `lecture/écriture`. De plus, dans la plupart des cas, toute entreprise a besoin de capacités transactionnelles pour les opérations d'`écriture`, mais pas pour les opérations de `lecture`. Vous êtes également satisfait d'un peu d'incohérence ou de retard dans les opérations de `lecture` et votre entreprise n'a pas de problème avec cela non plus. Vous voyez une opportunité où il pourrait être bon de séparer les opérations de `lecture` et d'`écriture` physiquement. Cela créera une opportunité pour les machines individuelles de gérer plus d'opérations de `lecture/écriture`. 

Vous prenez maintenant deux autres grandes machines et les configurez comme `réplica` de la machine actuelle. La réplication de la base de données se chargera de distribuer les données de la machine `primaire` vers les machines `réplica`. Vous dirigez toutes les requêtes de lecture (Query (`Q`) dans `CQRS`) vers les réplicas — n'importe quel `réplica` peut servir n'importe quelle requête de lecture, vous dirigez toutes les requêtes d'écriture (Command (`C`) dans `CQRS`) vers le `primaire`. Il peut y avoir un léger retard dans la réplication, mais selon votre cas d'utilisation commercial, c'est acceptable.

La plupart des startups de taille moyenne qui servent quelques centaines de milliers de requêtes chaque jour peuvent survivre avec une configuration primaire-réplica à condition qu'elles archivent périodiquement les anciennes données.

Maintenant, vous vous étendez à 2 autres villes, vous voyez que votre `primaire` n'est pas en mesure de gérer toutes les requêtes d'`écriture`. De nombreuses requêtes d'`écriture` ont une latence. De plus, le retard entre le `primaire` et le `réplica` impacte parfois les clients et les conducteurs, par exemple — lorsque le trajet se termine, le client paie le conducteur avec succès, mais le conducteur n'est pas en mesure de voir le paiement puisque l'activité du client est une requête d'`écriture` qui va au `primaire`, tandis que l'activité du conducteur est une requête de `lecture` qui va à l'un des réplicas. Votre système global est si lent que le conducteur n'est pas en mesure de voir le paiement pendant au moins une demi-minute — frustrant pour le conducteur et le client. Comment résolvez-vous cela ?

## Modèle 4 - Réplication Multi Primaire

Vous avez bien évolué avec la configuration `primaire-réplica`, mais maintenant vous avez besoin de plus de performances en écriture. Vous pourriez être prêt à compromettre un peu les performances des requêtes de `lecture`. Pourquoi ne pas distribuer la requête d'écriture à un `réplica` également ?

Dans une configuration `multi-primaire`, toutes les machines peuvent fonctionner à la fois comme `primaire` et `réplica`. Vous pouvez penser au `multi-primaire` comme un cercle de machines, par exemple `A->B->C->D->A`. `B` peut répliquer les données de `A`, `C` peut répliquer les données de `B`, `D` peut répliquer les données de `C`, `A` peut répliquer les données de `D`. Vous pouvez écrire des données sur n'importe quel nœud, tandis que lors de la lecture des données, vous pouvez diffuser la requête à tous les nœuds, celui qui répond retourne cela. Tous les nœuds auront le même schéma de base de données, le même ensemble de tables, d'index, etc. Vous devez donc vous assurer qu'il n'y a pas de collision dans les `id` entre les nœuds dans la même table, sinon lors de la diffusion, plusieurs nœuds retourneraient des données différentes pour le même `id`. 

Généralement, il est préférable d'utiliser `UUID` ou `GUID` pour l'id. Un autre inconvénient de cette technique est que les requêtes de `lecture` peuvent être inefficaces car elles impliquent la diffusion de la requête et l'obtention du résultat correct — essentiellement une approche de diffusion-rassemblement.

Maintenant, vous vous étendez à 5 autres villes et votre système est à nouveau en difficulté. Vous êtes censé gérer environ 50 requêtes par seconde. Vous avez désespérément besoin de gérer un grand nombre de requêtes concurrentes. Comment y parvenir ?

## Modèle 5 - Partitionnement :

Vous savez que votre base de données `location` est quelque chose qui reçoit un trafic élevé de `lecture` et d'`écriture`. Probablement, le ratio `écriture:lecture` est de `7:3`. Cela exerce une forte pression sur les bases de données existantes. Les tables `location` contiennent quelques données principales comme `longitude`, `latitude`, `timestamp`, `driver id`, `trip id`, etc. Cela n'a pas grand-chose à voir avec les trajets des utilisateurs, les données des utilisateurs, les données de paiement, etc. Que diriez-vous de séparer les tables `location` dans un schéma de base de données séparé ? Que diriez-vous de placer cette base de données dans des machines séparées avec une configuration `primaire-réplica` ou `multi-primaire` appropriée ? 

Cela s'appelle le partitionnement des données par fonctionnalité. Différentes bases de données peuvent héberger des données catégorisées par différentes fonctionnalités, si nécessaire, le résultat peut être agrégé dans la couche backend. En utilisant cette technique, vous pouvez vous concentrer sur la mise à l'échelle de ces fonctionnalités qui demandent un grand nombre de requêtes de `lecture/écriture`. Bien que la couche backend ou la couche application doive prendre la responsabilité de joindre les résultats lorsque cela est nécessaire, ce qui entraîne probablement plus de changements de code.

Maintenant, imaginez que vous avez étendu votre entreprise à un total de 20 villes dans votre pays et que vous prévoyez de vous étendre bientôt en Australie. Votre demande croissante d'application nécessite des réponses de plus en plus rapides. Aucune des méthodes ci-dessus ne peut vous aider à l'extrême maintenant. Vous devez mettre à l'échelle votre système de manière à ce que l'expansion vers d'autres pays/régions ne nécessite pas toujours des changements fréquents d'ingénierie ou d'architecture. Comment faites-vous cela ?

## Modèle 6 - Mise à l'échelle horizontale :

Vous faites beaucoup de recherches sur Google, vous lisez beaucoup sur la façon dont d'autres entreprises ont résolu le problème — et vous en arrivez à la conclusion que vous devez mettre à l'échelle horizontalement. Vous allouez, disons, 50 machines — toutes ont le même schéma de base de données qui contient à son tour le même ensemble de tables. Toutes les machines ne contiennent qu'une partie des données. 

Puisque toutes les bases de données contiennent le même ensemble de tables, vous pouvez concevoir le système de manière à ce que la localité des données soit présente, c'est-à-dire que toutes les données liées se trouvent sur la même machine. Chaque machine peut avoir ses propres réplicas, les réplicas peuvent être utilisés pour la récupération en cas de défaillance. Chacune des bases de données est appelée `shard`. Une machine physique peut avoir un ou plusieurs `shards` — cela dépend de votre conception. Vous devez décider de la `clé de sharding` de manière à ce qu'une seule `clé de sharding` fasse toujours référence à la même machine. Vous pouvez donc imaginer beaucoup de machines contenant toutes des données liées dans le même ensemble de tables, les requêtes de `lecture/écriture` pour la même ligne ou le même ensemble de ressources se trouvent sur la même machine de base de données.

Le sharding est en général difficile — du moins, les ingénieurs de différentes entreprises le disent. Mais lorsque vous servez des millions ou des milliards de requêtes, vous devez prendre de telles décisions difficiles.

Je discuterai du `sharding` plus en détail dans mon prochain article, donc je retiens mon envie d'en discuter davantage dans cet article.

Maintenant que vous avez mis en place le sharding, vous êtes confiant que vous pouvez vous étendre à de nombreux pays. Votre entreprise a tellement grandi que les investisseurs vous poussent à développer l'entreprise à travers les continents. Vous voyez à nouveau un problème ici. Latence de l'API à nouveau. Votre service est hébergé aux États-Unis et les personnes du Vietnam ont du mal à réserver des trajets. Pourquoi ? Que faites-vous à ce sujet ?

## Modèle 7 - Partition par centre de données :

Votre entreprise se développe en Amérique, en Asie du Sud et dans quelques pays d'Europe. Vous effectuez des millions de réservations quotidiennement avec des milliards de requêtes frappant votre serveur. Félicitations — c'est un moment de pointe pour votre entreprise. 

Mais comme les requêtes de l'application doivent traverser les continents à travers des centaines ou des milliers de serveurs sur Internet, la latence apparaît. Que diriez-vous de distribuer le trafic entre les centres de données ? Vous pouvez mettre en place un centre de données à Singapour qui gère toutes les requêtes d'Asie du Sud, un centre de données en Allemagne peut gérer toutes les requêtes des pays européens, et un centre de données en Californie peut gérer toutes les requêtes des États-Unis. 

Vous activez également la réplication inter-centres de données, ce qui aide à la récupération après sinistre. Ainsi, si le centre de données de Californie effectue une réplication vers le centre de données de Singapour, en cas de panne du centre de données de Californie due à un problème d'électricité ou à une catastrophe naturelle, toutes les requêtes des États-Unis peuvent basculer vers le centre de données de Singapour, et ainsi de suite. 

Cette technique de mise à l'échelle est utile lorsque vous avez des millions de clients à servir à travers les pays et que vous ne pouvez pas tolérer de perte de données, vous devez toujours maintenir la disponibilité du système.

Ce sont quelques techniques générales étape par étape pour la mise à l'échelle des bases de données. Bien que la plupart des ingénieurs n'aient pas assez l'occasion de mettre en œuvre ces techniques, il est préférable d'avoir une idée plus large de tels systèmes qui, à l'avenir, pourraient vous aider à concevoir de meilleurs systèmes et architectures.

Dans mes prochains articles, je tenterai de discuter de certains de ces concepts en détail. N'hésitez pas à donner des commentaires appropriés pour cet article si nécessaire.

L'article a été initialement publié sur le compte Medium de l'auteur : [https://medium.com/@kousiknath/understanding-database-scaling-patterns-ac24e5223522](https://medium.com/@kousiknath/understanding-database-scaling-patterns-ac24e5223522)