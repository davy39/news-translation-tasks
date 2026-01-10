---
title: Comment déployer des modifications à une application – Stratégies de déploiement
  expliquées
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-04-26T14:41:00.000Z'
originalURL: https://freecodecamp.org/news/application-deployment-strategies
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-2.png
tags:
- name: deployment
  slug: deployment
- name: Web Development
  slug: web-development
seo_title: Comment déployer des modifications à une application – Stratégies de déploiement
  expliquées
seo_desc: 'When deploying changes to an application, there are several strategies
  you can use.

  In this article, I''ll explain the different strategies with an analogy, and then
  we''ll analyze the benefits and tradeoffs.

  Deployment Strategies

  Imagine you are the m...'
---

Lors du déploiement de modifications à une application, plusieurs stratégies peuvent être utilisées.

Dans cet article, j'expliquerai les différentes stratégies avec une analogie, puis nous analyserons les avantages et les compromis.

# Stratégies de déploiement

Imaginez que vous êtes le gérant d'un restaurant à pizza populaire ouvert 24h/24 pour les livraisons. Ce restaurant compte deux cuisiniers en cuisine et tous deux sont nécessaires pour garantir que les commandes sont honorées à temps.

Vous avez une nouvelle recette spéciale qui changera la façon dont toutes les pizzas sont préparées. Cette nouvelle recette implique l'utilisation d'une pâte différente pour le pain à pizza, d'un type de fromage différent, de nouvelles garnitures sur la pizza et des modifications des réglages du four à pizza.

Ce sont des changements importants que vous espérez mener à des pizzas plus délicieuses, ce qui signifie des clients plus heureux, ce qui, espérons-le, se traduira par plus d'argent.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc75206fe-9d56-48ce-9309-58d6772389df_2248x1492.png align="left")

Cette nouvelle recette est assez complexe et prendra une heure pour qu'un seul cuisinier l'apprenne. Comment enseignez-vous cette nouvelle recette aux cuisiniers ? N'oubliez pas que ce restaurant doit être ouvert 24h/24. Votre approche dépendra de ce que vous essayez de faire :

* réduire le temps nécessaire aux deux cuisiniers pour apprendre la nouvelle recette

* vous assurer d'avoir suffisamment de cuisiniers pour honorer les commandes pendant qu'un cuisinier apprend la nouvelle recette

* maintenir les coûts bas pendant le changement de recette

* pouvoir revenir rapidement à l'ancienne recette

* tester la nouvelle recette avec un petit sous-ensemble de vos clients

Vous feriez un ensemble de compromis similaire lors du choix d'une stratégie de déploiement d'application. Souhaitez-vous :

* minimiser le temps de déploiement

* avoir un temps d'arrêt nul

* garantir que la capacité est maintenue

* réduire le coût de déploiement

* pouvoir revenir en arrière ou annuler facilement les modifications

* tester le changement avec un petit sous-ensemble de vos utilisateurs

Le compromis vient du fait que vous ne pouvez pas tout avoir. Par exemple, avoir un temps d'arrêt nul, garantir que la capacité est maintenue et avoir la possibilité de revenir en arrière se fait au prix d'un temps de déploiement plus long et d'un coût plus élevé.

J'expliquerai la logique derrière cet exemple en utilisant l'exemple de la stratégie de déploiement bleu/vert. En fin de compte, il n'y a pas de solutions, seulement des compromis.

Nous utiliserons une application web à trois niveaux comme exemple d'architecture pour les différents types de déploiement. Cela consiste en une couche de présentation, une couche logique et une couche de base de données, comme illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f739c67-e79c-4995-b58d-71d695cccd47_1018x1682.png align="left")

*Exemple d'architecture d'application*

La couche de présentation est responsable de la présentation de l'interface utilisateur à l'utilisateur. Elle inclut les composants de l'interface utilisateur tels que HTML, CSS et JavaScript.

La couche logique est responsable du traitement des requêtes utilisateur et de la génération de réponses, en communiquant avec la couche de base de données pour récupérer ou stocker des données.

La couche de base de données est responsable du stockage et de la gestion des données de l'application et permet l'accès à ses données via la couche logique.

## Déploiement instantané

Dans ce type de déploiement, vous apportez des modifications à toutes les instances d'une application en même temps. Dans l'architecture d'application web à trois niveaux, un déploiement instantané qui apporte des modifications à l'UI mettra hors service les deux instances de la couche de présentation pendant le déploiement, comme illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa03758ef-ff46-49c7-9d7b-22596c842240_1018x1682.png align="left")

*Illustration de la stratégie de déploiement instantané*

Ce type de déploiement présente certains avantages :

* les déploiements sont rapides

* les déploiements sont peu coûteux

Et certains inconvénients :

* temps d'arrêt pendant le déploiement

* un déploiement échoué entraînera un temps d'arrêt supplémentaire puisque vous devrez revenir en arrière en déployant la version précédente de l'application sur les instances

* les retours en arrière sont manuels

Un déploiement instantané est idéal dans une situation où un déploiement doit être effectué rapidement. Il est également idéal pour les situations où l'impact d'un problème est faible. Par exemple, les déploiements dans des environnements non actifs comme les environnements de développement et de test, qui n'ont pas d'utilisateurs réels.

Tout cas d'utilisation où les inconvénients listés ci-dessus ne sont pas acceptables serait un anti-pattern pour un déploiement instantané.

Un déploiement instantané est analogue au fait que les deux cuisiniers se voient dire d'arrêter de prendre de nouvelles commandes ainsi que d'arrêter toute commande sur laquelle ils travaillent pour apprendre la nouvelle recette de pizza. Ensuite, ils utiliseraient cette recette à l'avenir.

Pendant qu'ils apprennent la nouvelle recette, les commandes ne seront pas honorées. S'ils ne parviennent pas tout à fait à maîtriser la nouvelle recette, les pizzas qu'ils prépareront ne seront pas non plus aussi bonnes, prendront plus de temps à préparer, ou les deux.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99f3efd5-9f11-4d90-9730-69bcbac1ffa4_1628x1080.png align="left")

De plus, si vous découvrez plus tard que les clients n'aiment pas le goût des nouvelles pizzas, vous devez revenir à l'ancienne recette. Cela signifie réapprovisionner votre cuisine avec la pâte et le fromage précédents que vous utilisiez et vous débarrasser des nouvelles garnitures.

Ce n'est pas une manière idéale de changer une recette car vous pouvez perdre des clients s'ils n'aiment pas le goût de la pizza.

D'un autre côté, cette approche est peu coûteuse, en termes de coût initial au moins. Si cela tourne mal, cela peut être très coûteux en raison des ventes futures perdues et des clients mécontents.

C'est aussi rapide à mettre en œuvre. Si chaque cuisinier met une heure à maîtriser la nouvelle recette et que vous leur montrez à tous les deux en même temps, la nouvelle recette peut être prête à être mise en ligne en une heure.

## Déploiement progressif

Dans un déploiement progressif, vous apportez des modifications à une instance ou à un lot d'instances en même temps. Dans l'exemple d'application web à trois niveaux, les modifications de l'UI seront d'abord déployées sur une instance et une fois cela terminé, cela sera répété sur l'autre instance.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76e9f8f4-c652-4eab-9bbc-7854aa7df6da_2276x1812.png align="left")

*Illustration d'une stratégie de déploiement progressif*

Avec cette approche, vous évitez les temps d'arrêt car les modifications ne sont apportées qu'à une instance à la fois. L'inconvénient est que les déploiements prendront naturellement plus de temps puisque vous devez attendre que le premier déploiement soit terminé avant de déployer sur la deuxième instance.

En revenant à l'analogie des cuisiniers, la nouvelle recette ne sera montrée qu'à un cuisinier à la fois. Cela signifie une capacité réduite à traiter les commandes, mais les commandes seront toujours honorées puisque il y aura toujours au moins un cuisinier disponible.

## Déploiement progressif avec lot supplémentaire

Cela ressemble à un déploiement progressif, mais une instance supplémentaire est ajoutée au cluster pendant le déploiement pour maintenir la capacité, comme illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea5df353-96ed-45e9-b96d-33a0a6dbae67_2588x1330.png align="left")

*Illustration de la stratégie de déploiement progressif avec lot supplémentaire*

D'abord, vous **lancez** une nouvelle instance, puis vous **déployez** la nouvelle application dessus. Après le déploiement réussi, vous **terminez** une instance exécutant l'ancienne application.

Ces trois étapes de lancement d'une nouvelle instance, de déploiement de la nouvelle application dessus et de terminaison de l'ancienne instance sont répétées jusqu'à ce que vous ayez déployé la nouvelle application sur toutes les instances.

Le point clé à noter avec cette approche est qu'en ajoutant une nouvelle instance avec la nouvelle version de l'application avant de terminer une instance, vous maintenez toujours la capacité. Si vous avez besoin de deux instances en cours d'exécution en même temps, cette stratégie de déploiement garantira que vous avez toujours deux instances disponibles. Cela est utile pour les applications nécessitant une haute disponibilité.

Avec cette approche, certains utilisateurs seront routés vers différentes instances pendant le déploiement. Cela signifie que les clients verront différentes interfaces utilisateur sur la page web – certains verront l'ancienne, d'autres verront la nouvelle interface utilisateur pendant que les instances sont encore mises à jour.

Si une expérience utilisateur cohérente est absolument nécessaire pour tous vos utilisateurs à tout moment, ce déploiement peut ne pas être adapté.

Le déploiement progressif avec lot supplémentaire est analogue à l'embauche d'un cuisinier supplémentaire pour montrer la nouvelle recette pendant que les deux cuisiniers existants continuent de préparer les commandes de pizza. Une fois que ce nouveau cuisinier est familier avec la nouvelle recette, les commandes sont routées vers lui et l'un des cuisiniers existants. Le troisième cuisinier est ensuite renvoyé chez lui.

Cela est répété jusqu'à ce que les deux cuisiniers de la cuisine soient nouveaux et familiers avec la nouvelle recette. Mais pendant cette transition, il y a toujours un minimum de deux cuisiniers qui peuvent préparer les commandes de pizza dans la cuisine.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0d5d9c1-5e64-495b-97da-124c7943b652_1860x598.png align="left")

## Déploiement Canary

L'expression « canari dans la mine de charbon » provient d'une ancienne pratique dans l'exploitation minière où les mineurs emmenaient un canari dans la mine de charbon comme alarme précoce.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da625e7-f768-440e-9850-a003fd3acb08_520x876.png align="left")

Les canaris sont très sensibles aux gaz toxiques comme le méthane et le monoxyde de carbone, que les humains ne peuvent pas facilement détecter, car ils sont inodores et incolores. La mort du canari était un signal pour évacuer la mine, car des niveaux dangereux de gaz toxiques s'étaient accumulés à des niveaux suffisamment élevés pour tuer l'oiseau. C'était une méthode efficace, bien que brutale, de signaler un danger potentiel aux mineurs.

Dans le déploiement canary, un ensemble séparé d'instances aura la nouvelle application déployée dessus, et un petit pourcentage de tous les visiteurs sera routé vers la nouvelle version. Cela peut être fait avec l'[option de routage pondéré utilisant Route 53](https://lightcloud.substack.com/i/64925113/weighted-routing) (service DNS géré par AWS). Avec le routage pondéré, vous pouvez spécifier un poids pour chaque équilibreur de charge cible.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a074098-b40f-4f17-aeb2-b5d0c9a2a961_1124x1080.png align="left")

*Illustration de la stratégie de déploiement canary*

Dans cet exemple, Route 53 pointera initialement 90 % de tous les utilisateurs vers l'ancienne application et 10 % vers la nouvelle application. La nouvelle application sera ensuite étroitement surveillée pour voir des métriques comme les taux d'erreur, les temps de réponse, etc. Si des problèmes surviennent avec la nouvelle application à ce stade, les poids sont simplement mis à jour pour que tout le trafic pointe à nouveau vers l'ancienne application.

Tout comme le canari dans la mine de charbon, la surveillance initiale sur un petit ensemble d'utilisateurs sert de signal peu coûteux pour vous donner la confiance de continuer la transition vers la nouvelle application ou de revenir à l'ancienne.

Pour les applications critiques qui ne peuvent se permettre aucun temps d'arrêt ou autres problèmes, c'est un moyen efficace de gérer le risque d'un nouveau déploiement tout en pouvant revenir immédiatement à l'ancienne application.

Si tout semble correct avec la nouvelle application pendant les tests initiaux avec un petit nombre d'utilisateurs, vous pouvez alors augmenter lentement le pourcentage d'utilisateurs routés vers celle-ci. À mesure que vous gagnez en confiance dans ses performances, vous pouvez finalement router tous les utilisateurs vers la nouvelle application et terminer les anciennes instances.

## Déploiement bleu/vert

Le déploiement bleu/vert implique la création de deux environnements identiques : un environnement « bleu » qui héberge la version actuelle de l'application, et un environnement « vert » qui héberge la nouvelle version de l'application. Cela est illustré dans l'image ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea56e413-b77d-4439-848e-c733bcab0c26_1852x1766.png align="left")

*Illustration de la stratégie de déploiement bleu/vert*

Une fois la nouvelle version de l'application déployée dans l'environnement vert, l'enregistrement DNS Route 53 est mis à jour pour ne pointer que vers l'équilibreur de charge de l'environnement vert devant la couche de présentation, comme illustré ci-dessous. Les instances de la couche de présentation dans l'environnement bleu peuvent également être arrêtées pour économiser des coûts. Vous pouvez les redémarrer lorsque qu'une nouvelle version de l'application doit être déployée.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6caffdc-d822-410d-889c-f5212c80a6c5_1852x1760.png align="left")

*Exemple de déploiement bleu/vert avec des instances de la couche de présentation dans un environnement séparé*

Dans cet exemple de bleu/vert, seules les instances de la couche de présentation sont dans un environnement séparé.

Mais vous pourriez avoir une copie identique des environnements bleu et vert sur tous les niveaux. Cela signifierait que si vous apportiez des modifications aux couches logique ou de base de données de l'application, il n'y aurait également aucun temps d'arrêt pendant le déploiement, avec la possibilité de revenir facilement en arrière. Vous pouvez voir ce scénario ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6329476-8072-44a9-9228-d452c14df946_1852x1794.png align="left")

*Déploiement bleu/vert sans temps d'arrêt et avec une capacité facile à revenir en arrière*

Le principal avantage du déploiement bleu/vert est l'absence de temps d'arrêt pendant les déploiements, puisque tout ce que vous avez à faire est de mettre à jour l'enregistrement DNS pour pointer vers l'équilibreur de charge de l'environnement « vert ».

Le bleu/vert est similaire au déploiement canary, mais au lieu d'envoyer initialement un petit pourcentage d'utilisateurs vers la nouvelle version de l'application, tous les utilisateurs sont envoyés vers la nouvelle version une fois qu'elle est déployée et soigneusement testée. Il n'y a pas de test en direct avec de vrais utilisateurs dans un déploiement bleu/vert.

Le déploiement bleu/vert est analogue à avoir deux succursales de restaurant, chacune avec deux équipes de cuisiniers. Le restaurant « bleu » utilise la recette de pizza actuelle et toutes les commandes à emporter sont d'abord routées vers ce restaurant comme illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c339e6d-d970-4639-b794-71bc4b3b95c0_1456x852.png align="left")

Le restaurant « vert » a perfectionné la nouvelle recette et est prêt à recevoir des commandes. Les commandes des clients sont ensuite routées vers ce restaurant comme illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12fa5167-f6fb-4711-b195-f0d458b0afdc_1456x852.png align="left")

Si les clients se plaignent du temps de livraison ou de la qualité de la pizza (ce qui ne devrait pas arriver si la nouvelle recette a été testée avec de vrais clients au préalable), le gérant peut simplement router les commandes vers le restaurant bleu préparant l'ancienne recette. Ensuite, ils peuvent déterminer ce qui n'allait pas avec la nouvelle recette, apporter quelques ajustements et réessayer.

# Conclusion

La bonne stratégie de déploiement pour votre application dépend de ce que vous essayez d'optimiser.

Les déploiements instantanés sont idéaux si vous souhaitez minimiser le temps de déploiement et le coût initial. Le prix à payer, cependant, est le temps d'arrêt de l'application, avec un temps d'arrêt supplémentaire si le déploiement échoue (ainsi qu'un processus de retour en arrière manuel).

Les déploiements progressifs prendront plus de temps à déployer qu'un déploiement instantané. Cependant, il n'y aura pas de temps d'arrêt puisque les déploiements sont effectués de manière incrémentielle sur une instance ou un ensemble d'instances. Mais il y aura une capacité réduite pendant le déploiement, donc cela peut ne pas être idéal pour une application nécessitant une haute disponibilité.

Le déploiement progressif avec lot supplémentaire aborde le problème de la capacité réduite avec une mise à jour progressive. Une instance supplémentaire ou un lot d'instances avec la nouvelle version est ajouté au cluster afin de maintenir la même capacité. Ce n'est qu'alors que les instances exécutant l'ancienne version de l'application sont terminées.

Le déploiement canary n'a pas de temps d'arrêt et pas de capacité réduite pendant le déploiement. Il est également plus sûr car il permet de tester avec une fraction des utilisateurs et de surveiller de près les performances avant de router progressivement tous les utilisateurs vers la nouvelle version.

Mais cela ne vient pas sans coût. Une infrastructure supplémentaire est nécessaire. De plus, une surveillance et une observabilité détaillées de l'application doivent être en place. Cela signifie qu'il est plus coûteux et plus complexe de déployer en utilisant cette stratégie.

Il est important de nuancer « plus coûteux ». Cette approche entraînera des coûts initiaux plus élevés, mais pour une application critique avec de nombreux utilisateurs qui ne peut se permettre aucun temps d'arrêt, cela pourrait être plus coûteux (par le biais de revenus futurs perdus, de clients mécontents ou d'une réputation ruinée) d'utiliser une autre stratégie de déploiement qui est « moins chère » mais finalement moins robuste face aux échecs.

Enfin, le bleu/vert est idéal pour les déploiements sans temps d'arrêt qui sont faciles à revenir en arrière. Il nécessite cependant un coût supplémentaire pour un ensemble séparé d'infrastructures identiques à provisionner.

Merci d'avoir lu !