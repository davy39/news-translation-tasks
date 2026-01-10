---
title: Disponibilité élevée vs Tolérance aux pannes vs Reprise après sinistre – Expliqué
  avec une analogie
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2022-11-07T17:10:24.000Z'
originalURL: https://freecodecamp.org/news/high-availability-fault-tolerance-and-disaster-recovery-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Slide6.JPG
tags:
- name: availability
  slug: availability
- name: Disaster recovery
  slug: disaster-recovery
- name: software architecture
  slug: software-architecture
- name: System Architecture
  slug: system-architecture
seo_title: Disponibilité élevée vs Tolérance aux pannes vs Reprise après sinistre
  – Expliqué avec une analogie
seo_desc: 'High availability, fault tolerance and disaster recovery are important
  things to consider when designing a system.

  These terms are sometimes used interchangeably by architects and developers. They
  are not, however, the same thing – and understanding ...'
---

La disponibilité élevée, la tolérance aux pannes et la reprise après sinistre sont des éléments importants à considérer lors de la conception d'un système.

Ces termes sont parfois utilisés de manière interchangeable par les architectes et les développeurs. Ils ne sont cependant pas identiques – et comprendre les différences peut vous éviter bien des maux de tête, ainsi que du temps et de l'argent.

Cet article passera en revue les différences entre ces trois termes et expliquera comment vous pouvez les implémenter dans AWS.

## Disponibilité élevée vs Tolérance aux pannes vs Reprise après sinistre

Un système hautement disponible est un système qui vise à être en ligne aussi souvent que possible. Bien que des temps d'arrêt puissent encore survenir dans un système hautement disponible, l'objectif de la haute disponibilité est de limiter la durée des temps d'arrêt, et non de les éliminer complètement.

Un système tolérant aux pannes est un système qui peut fonctionner malgré une panne sans aucun temps d'arrêt. La tolérance aux pannes vise à éviter complètement les temps d'arrêt.

En cas de défaillance complète du système, cependant, la haute disponibilité et la tolérance aux pannes ne suffisent pas. La reprise après sinistre décrit comment le système peut continuer à fonctionner lorsque le coussin de haute disponibilité et de tolérance aux pannes disparaît dans une défaillance systémique.

## Que signifie la haute disponibilité ?

Tout d'abord, décrivons ce que la haute disponibilité n'est pas. La haute disponibilité ne signifie pas que le système ne tombe jamais en panne ou ne subit jamais de temps d'arrêt. Un système hautement disponible est simplement un système qui vise à être en ligne aussi souvent que possible.

Imaginez que nous avons un restaurant de pizzas ouvert 24 heures sur 24, tous les jours de l'année. Si ce restaurant n'a qu'un seul chef, alors sa disponibilité – c'est-à-dire sa capacité à traiter les commandes – ne sera pas de 100 %. Cela est dû au fait qu'un seul chef ne peut travailler que huit heures par jour avec une pause d'une heure – soit effectivement sept heures par jour, sept jours par semaine.

Le chef peut donc ne travailler que 49 heures par semaine sur un total possible de 168 heures. Ce restaurant a une disponibilité de 29 %.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3e3d174-070d-447d-9088-92c6f7377c99_1504x861.jpeg align="left")

*Un restaurant à faible disponibilité*

Cela n'est bien sûr pas une disponibilité suffisante pour un restaurant qui souhaite être ouvert 24 heures sur 24 tout au long de l'année.

Alors, comment obtenir une disponibilité plus élevée pour le restaurant ? Engagez plus de chefs. Si nous avons quatre chefs travaillant en équipes de six heures par jour, sept jours par semaine, cela nous donne une disponibilité théorique de 100 %.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8b1538ad-5148-44f1-b025-c6705a5c3780_1504x830.jpeg align="left")

*Un restaurant à haute disponibilité*

Cette disponibilité de 100 % n'est que théorique car elle suppose qu'aucun chef ne manque de travail dans une année entière. C'est une supposition erronée car les chefs peuvent tomber malades, leur voiture peut tomber en panne sur le chemin du travail, ou ils peuvent devoir quitter le travail plus tôt pour aller chercher leurs enfants.

Disons que tout ce temps d'arrêt des chefs s'accumule à cinq heures dans une année. Cela vous donne une disponibilité de 99,94 %.

Comment pouvez-vous rendre le restaurant encore plus disponible ? Engagez des chefs de réserve prêts à venir au restaurant à tout moment. Mais cela vient à un prix élevé puisque vous devez payer ces chefs pour qu'ils attendent jusqu'à ce qu'ils soient nécessaires.

Ce que ces chefs de réserve vous apportent, c'est **la capacité de récupérer rapidement du manque de chefs pour répondre aux commandes des clients**. Vous ne pouvez jamais avoir une disponibilité de 100 % en raison des contraintes de la réalité. Vous ne pouvez vous approcher d'une disponibilité de 100 % qu'à un prix de plus en plus élevé.

### Qu'est-ce que la disponibilité dans un système ?

La disponibilité est la probabilité qu'un système soit en mesure de répondre à une demande.

Notez que la haute disponibilité n'a rien à dire sur la qualité des pizzas ou la rapidité avec laquelle elles sont livrées. La haute disponibilité est simplement préoccupée par la capacité du restaurant à répondre aux commandes de pizza des clients.

Les principaux fournisseurs de cloud ont généralement des [SLA](https://www.cio.com/article/274740/outsourcing-sla-definitions-and-solutions.html) qui décrivent la disponibilité d'un système.

Prenons par exemple un système de stockage blob. AWS S3 standard a un SLA de disponibilité de 99,99 %. C'est la même figure pour le stockage blob Azure et le stockage cloud Google.

Que signifie exactement une disponibilité de 99,99 % ? Cela signifie qu'en une année, il y a une probabilité de 99,99 % que le système soit en ligne. Un temps de fonctionnement de 99,99 % équivaut à un temps d'arrêt de 0,01 %. Cela équivaut à un temps d'arrêt d'environ 53 minutes - juste sous une heure pour une année entière.

Et une disponibilité de 99,9 % ? Un tel système aurait un temps d'arrêt de 0,1 %, soit 8,8 heures par an.

Bien que 99,9 % de disponibilité puissent sembler élevés, pour une banque traitant des paiements, un système de contrôle du trafic aérien ou tout autre système critique, une telle quantité de temps d'arrêt peut simplement être inacceptable.

Quel est le bon niveau de disponibilité que vous devriez viser ? Cela dépend des exigences du système que vous construisez.

Vous êtes bien sûr limité par les SLA de disponibilité des fournisseurs de cloud, donc il y a une flexibilité limitée pour atteindre, par exemple, 99,999 % de disponibilité pour un système de stockage blob. Et, plus le niveau de disponibilité que vous souhaitez atteindre est élevé, plus la solution devient coûteuse et complexe.

## Que signifie la tolérance aux pannes ?

Si une défaillance se produit dans un système, le système peut-il continuer à fonctionner sans aucune interruption ? Si c'est le cas, alors le système est tolérant aux pannes.

Alors, quelle est la différence entre la haute disponibilité et la tolérance aux pannes ? Avec un système hautement disponible, des défaillances causant des temps d'arrêt se produiront, mais rarement. Le système est également capable de se rétablir de telles défaillances. **Mais lorsque le système est en panne, il ne peut pas répondre aux demandes.**

Dans un système tolérant aux pannes, le système **peut continuer à fonctionner malgré une défaillance.**

Utilisons à nouveau l'exemple du restaurant de pizzas. Si le restaurant subit une panne de courant, alors aucun nombre de chefs dans la cuisine ou de chefs en réserve ne pourra aider à faire des pizzas pour les clients puisque les fours ont besoin d'une alimentation électrique.

Un générateur de secours qui se met en marche immédiatement en cas de perte de courant rend le restaurant tolérant aux pannes.

Un autre bon exemple de cela est un avion commercial propulsé par des moteurs à réaction. Ces avions sont conçus pour être tolérants aux pannes afin qu'en cas de défaillance d'un moteur, l'avion puisse continuer à voler et à atterrir sans interruption ou avoir à réparer le moteur défaillant en vol.

Les hélicoptères ou les avions à moteur unique, en revanche, ne sont pas tolérants aux pannes. Une défaillance du moteur signifie que l'avion ne peut pas voler. De telles défaillances sont généralement catastrophiques et expliquent en partie le taux plus élevé de crashes d'hélicoptères et d'avions à moteur unique par rapport aux avions à double moteur.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfafca0a-1940-4215-ac2b-39a7a84b9660_1504x861.jpeg align="left")

*Un avion avec deux moteurs est tolérant aux pannes*

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F964241a9-8fc6-4d65-86c2-48f509a5951a_1504x861.jpeg align="left")

*Les hélicoptères et les avions à moteur unique ne sont pas tolérants aux pannes*

## Que signifie la reprise après sinistre ?

Si l'ampleur de la défaillance du système est si grande que la haute disponibilité et la tolérance aux pannes du système sont effectivement neutralisées, le système peut-il continuer à fonctionner ?

Revenons à l'exemple du restaurant. Si un incendie, une inondation ou tout autre sinistre frappe votre restaurant de pizzas, comment pouvez-vous continuer à faire des pizzas pour vos clients ?

C'est un exemple quelque peu facétieux puisque, en cas d'incendie, se soucier des commandes des clients n'est pas la principale priorité – mais la logique de l'exemple reste valable.

Dans ce cas, la haute disponibilité n'est d'aucune aide. Avoir un nombre infini de chefs dans la cuisine ou en réserve dans un restaurant en flammes = pas de pizzas pour les clients.

La tolérance aux pannes n'est également d'aucune aide. Un générateur de secours est inutile pour les appareils qu'il est censé alimenter s'ils ont été détruits.

La seule façon pour le système (restaurant) de continuer à fonctionner est de rediriger les commandes vers un autre restaurant à proximité non affecté par l'incendie. La reprise après sinistre est un plan d'action proactif qui détaille comment récupérer **après qu'un sinistre s'est produit**.

## Tout mettre ensemble

Maintenant, examinons une architecture unique qui est simultanément hautement disponible, tolérante aux pannes et qui intègre la reprise après sinistre.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3995b811-f03f-44b5-8118-8f7965e7f09a_893x560.jpeg align="left")

*Tout en un - haute disponibilité, tolérance aux pannes et reprise après sinistre dans une seule architecture*

L'architecture ci-dessus montre un déploiement de service de base de données relationnelle (Amazon RDS) multi-zone de disponibilité (AZ). Elle montre une base de données RDS avec une instance de secours dans une AZ séparée, une seule réplique en lecture seule et un bucket S3 utilisé pour stocker des sauvegardes de la base de données sur une base quotidienne.

Ce RDS est une offre de base de données en tant que service entièrement gérée par AWS, où AWS gère le matériel, le logiciel et l'application sous-jacents de la base de données. Vous pouvez trouver plus d'informations ici sur [AWS RDS](https://aws.amazon.com/rds/) et les [zones de disponibilité](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).

Maintenant, analysons comment ce système fonctionnerait et comment la conception garantit qu'il est hautement disponible, tolérant aux pannes et peut se remettre d'un sinistre.

### Comment la haute disponibilité est atteinte

L'instance RDS principale dans l'AZ A réplique de manière synchrone ses données vers l'instance de secours dans l'AZ B.

Avec la réplication synchrone, l'instance principale attend que l'instance de secours ait reçu la dernière opération d'écriture avant que la transaction ne soit enregistrée comme réussie. Cela garantit que les deux bases de données ont des informations identiques – c'est-à-dire qu'elles sont cohérentes, admettons au détriment d'une latence accrue des transactions.

Les instances principale et de secours sont dans une configuration active-passive. Seule l'instance principale reçoit les requêtes de lecture et d'écriture. Le rôle de l'instance de secours est simplement de prendre le relais en tant qu'instance principale en cas de défaillance de l'instance principale.

Le temps nécessaire pour basculer de l'instance principale vers l'instance de secours est appelé l'objectif de temps de récupération (RTO). Le RTO décrit simplement le temps nécessaire pour se remettre d'une défaillance. Dans ce cas, le temps de basculement pour RDS dans une configuration multi-AZ est actuellement de 1 à 2 minutes.

L'instance de secours a un seul but : augmenter la disponibilité du système. Si l'instance principale tombe en panne, ou si l'ensemble de l'AZ A tombe en panne, l'instance de secours dans une AZ séparée sera promue en tant qu'instance principale. Ce processus de basculement prend 1 à 2 minutes. Cela représente 1 à 2 minutes de temps d'arrêt.

Rappelons que la haute disponibilité ne consiste pas à prévenir les temps d'arrêt, mais simplement à les réduire. Sans une instance de secours, il y a une forte probabilité que le temps d'arrêt dépasse les 1 à 2 minutes nécessaires pour se rétablir avec une instance de secours.

Notez que l'instance de secours n'aide pas à la tolérance aux pannes, car la défaillance de l'instance principale entraînera toujours un temps d'arrêt.

### Comment la tolérance aux pannes est atteinte

Pour éliminer les temps d'arrêt, vous avez besoin d'une configuration qui ne nécessite aucun basculement. C'est un travail pour les répliques en lecture seule. Ce sont des copies répliquées de manière asynchrone de l'instance principale. Les écritures ne sont effectuées que sur l'instance principale. Les répliques de lecture sont, comme leur nom l'indique, en lecture seule.

Une telle approche est idéale pour les applications à forte charge de lecture, car les répliques de lecture peuvent soulager l'instance principale du fardeau supplémentaire des requêtes de lecture.

Dans la réplication asynchrone, les écritures sur une instance principale n'attendent pas de réponse de la réplique en lecture seule avant que la transaction ne soit enregistrée comme un succès. Cela signifie que, pendant un certain temps, les données sur l'instance principale et la réplique de lecture peuvent ne pas être identiques (mais plutôt incohérentes) après une écriture sur l'instance principale.

Cette cohérence éventuelle (un sujet pour un autre article) est un inconvénient de la réplication asynchrone. L'avantage de la réplication asynchrone est qu'elle n'attend pas que la réplique de lecture réponde avant que la transaction ne soit enregistrée comme un succès.

Cela est important car si la réplique de lecture est hors ligne ou s'il y a une défaillance du réseau, l'instance principale peut toujours accepter les écritures suivantes sans attendre de réponse de la réplique de lecture, confirmant que l'écriture précédente a été répliquée avec succès.

L'architecture ci-dessus a deux répliques : une synchrone et l'autre asynchrone. Si toutes les répliques sont synchrones, alors une défaillance dans la réplique de secours ou la réplique en lecture seule, ou même une défaillance du réseau, fait tomber l'ensemble du cluster. C'est une conception fragile qui expose l'ensemble du système à une défaillance si un seul composant tombe en panne. Avoir certaines répliques qui sont synchrones et d'autres qui sont asynchrones améliore la tolérance aux pannes du système.

Où intervient également la tolérance aux pannes ? Comme un avion avec deux moteurs à réaction qui fournissent la poussée, une réplique de lecture et une instance principale peuvent travailler ensemble simultanément. L'instance principale traite les écritures et la réplique de lecture répond aux requêtes de lecture.

La défaillance de l'instance principale n'a aucun effet sur la capacité de la réplique de lecture à répondre aux requêtes de lecture. Il n'y a pas de temps d'arrêt pour les lectures puisque seule la réplique de lecture répond aux lectures.

Et pour les écritures ? La réplique de lecture peut être promue en tant qu'instance principale, bien que, avec RDS, ce soit actuellement un processus manuel.

### Comment la reprise après sinistre est atteinte

Avec l'architecture ci-dessus, vous pouvez gérer la reprise après sinistre de deux manières. Il n'y a pas de contrainte pour limiter la reprise après sinistre à une seule approche, donc vous pouvez utiliser les deux en même temps. Et en fait, plus vous avez d'approches, mieux c'est, car cela fournit une redondance supplémentaire.

En fin de compte, vous devez peser tout cela contre le coût, car la mise en œuvre de stratégies de reprise après sinistre peut être coûteuse.

La première méthode consiste à utiliser des sauvegardes automatiques. Les sauvegardes sont effectuées à partir de l'instance de secours, évitant ainsi la dégradation des performances de l'instance principale qui doit servir les écritures (et les lectures si elle n'est pas configurée avec une réplique de lecture). Puisqu'il y a une réplication synchrone entre l'instance principale et l'instance de secours, nous avons la garantie que l'instance de secours est une copie à jour de l'instance principale, ce qui en fait un choix idéal pour effectuer des sauvegardes.

Avec RDS, les sauvegardes sont effectuées selon un calendrier fixe une fois par jour (spécifié par vous) et stockées dans un bucket S3. Puisque c'est un composant entièrement séparé, toute défaillance systémique liée à RDS n'affectera pas la durabilité des sauvegardes.

Avec les sauvegardes, une perte de l'instance principale, de l'instance de secours et des répliques de lecture ne signifie pas une perte permanente de données. Les sauvegardes peuvent ensuite être utilisées pour restaurer la base de données sur une nouvelle instance de base de données.

La deuxième méthode consiste à promouvoir la réplique en lecture seule en tant qu'instance autonome si l'instance principale tombe en panne. La réplique de lecture peut être configurée dans une autre [région AWS](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). Ainsi, si un sinistre se produit à l'échelle régionale où plusieurs AZ sont hors ligne, une réplique de lecture interrégionale garantira qu'une autre instance est disponible dans une région AWS différente pour servir les requêtes de lecture et d'écriture.

Cela est analogue à la redirection des commandes vers un autre restaurant en cas d'incendie.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb353885-8d22-4542-8155-2f92e3d49314_943x635.jpeg align="left")

*Comment différents composants améliorent la disponibilité, la tolérance aux pannes et la reprise après sinistre d'une solution*

## Conclusion

La disponibilité est mesurée en pourcentages - plus le nombre est élevé, plus le système est disponible (d'où moins de temps d'arrêt).

Très peu de systèmes visent une disponibilité de 100 % – bien que les stimulateurs cardiaques soient une exception notable. Une disponibilité de 99,999 % a un temps d'arrêt de 0,001 % = 5 minutes de temps d'arrêt par an. Cela tend à être la limite supérieure pour la plupart des systèmes logiciels.

Viser des niveaux de disponibilité plus élevés que cela est de plus en plus compliqué, coûteux et souvent inutile. Cela est particulièrement vrai lorsque vous considérez que le système logiciel que vous construisez repose sur des infrastructures comme le réseau électrique et les fournisseurs de services Internet, qui peuvent avoir des niveaux de disponibilité inférieurs.

La tolérance aux pannes, en revanche, ne peut pas être mesurée. Votre conception est soit tolérante aux pannes, soit elle ne l'est pas. De même, la reprise après sinistre ne peut pas être mesurée. Vous avez soit un plan d'action qui décrit précisément comment votre système peut se remettre d'un sinistre, soit vous ne l'avez pas.

Connaître la différence entre la haute disponibilité, la tolérance aux pannes et la reprise après sinistre est important. Cela garantit que vous construisez l'architecture correcte en fonction des besoins des clients.

Sur-ingénier une solution en fournissant une reprise après sinistre alors que seule la haute disponibilité ou la tolérance aux pannes est requise est souvent un exercice coûteux et complexe.

D'un autre côté, sous-ingénier une solution en ne fournissant que la haute disponibilité alors que la tolérance aux pannes est requise peut entraîner des conséquences graves pour certains systèmes critiques qui ne peuvent se permettre aucun temps d'arrêt.