---
title: 'Récolte, Rendement et Systèmes Tolérants Évolutifs : Un Résumé'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-30T17:14:37.000Z'
originalURL: https://freecodecamp.org/news/harvest-yield-and-scalable-tolerant-systems-a-summary-5609a088bb2b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*PlLhXyx7tBvL4fVm.png
tags:
- name: Computer Science
  slug: computer-science
- name: data
  slug: data
- name: distributed systems
  slug: distributed-systems
- name: research
  slug: research
- name: summary
  slug: summary
seo_title: 'Récolte, Rendement et Systèmes Tolérants Évolutifs : Un Résumé'
seo_desc: 'By Shubheksha Jalan

  This article presents a summary of the paper “Harvest, Yield, and Scalable Tolerant
  Systems” published by Eric Brewer & Amando Fox in 1999. All unattributed quotes
  are from this paper.

  The paper deals with the trade-offs between c...'
---

Par Shubheksha Jalan

Cet article présente un résumé du document [Harvest, Yield, and Scalable Tolerant Systems](https://pdfs.semanticscholar.org/5015/8bc1a8a67295ab7bce0550886a9859000dc2.pdf) publié par Eric Brewer & Amando Fox en 1999. Toutes les citations non attribuées proviennent de ce document.

Le document traite des compromis entre cohérence et disponibilité (CAP) pour les grands systèmes. Il est très facile de pointer vers CAP et d'affirmer qu'aucun système ne peut avoir à la fois cohérence et disponibilité.

Mais il y a un piège. CAP a été mal compris de diverses manières. Comme l'explique Coda Hale dans son excellent article de blog [You Cant Sacrifice Partition Tolerance](https://codahale.com/you-cant-sacrifice-partition-tolerance/) :

> Parmi la cohérence, la disponibilité et la tolérance aux partitions du théorème CAP, la tolérance aux partitions est obligatoire dans les systèmes distribués. Vous ne pouvez pas **ne pas** la choisir. Au lieu de CAP, vous devriez penser à votre disponibilité en termes de rendement (pourcentage de requêtes traitées avec succès) et de récolte (pourcentage des données requises effectivement incluses dans les réponses) et lequel de ces deux éléments votre système sacrifiera en cas de défaillances.

Le document se concentre sur l'augmentation de la disponibilité des systèmes à grande échelle par la tolérance aux pannes, le confinement et l'isolement :

> Nous supposons que les clients font des requêtes aux serveurs, dans ce cas, il existe au moins deux métriques pour un comportement correct : le rendement, qui est la probabilité de compléter une requête, et la récolte, qui mesure la fraction des données reflétées dans la réponse, c'est-à-dire l'exhaustivité de la réponse à la requête.

Les deux métriques, **récolte** et **rendement**, peuvent être résumées comme suit :

* **Récolte** : données dans la réponse/données totales  
Par exemple : Si l'un des nœuds est hors service dans un cluster de 100 nœuds, la récolte est de 99 % pendant la durée de la panne.
* **Rendement** : requêtes complétées avec succès/nombre total de requêtes  
**Note** : Le rendement est différent du temps de fonctionnement. Le rendement traite du nombre de requêtes, pas seulement du temps pendant lequel le système n'a pas pu répondre aux requêtes.

Le document soutient qu'il existe certains systèmes qui nécessitent des réponses parfaites aux requêtes à chaque fois. Il existe également des systèmes qui peuvent tolérer des réponses imparfaites de temps en temps.

Pour augmenter la disponibilité globale de nos systèmes, nous devons réfléchir attentivement aux garanties de cohérence et de disponibilité qu'ils doivent fournir.

#### Échanger la Récolte contre le Rendement — Disponibilité Probabiliste

> Presque tous les systèmes sont probabilistes, qu'ils le réalisent ou non. En particulier, tout système qui est disponible à 100 % en cas de défaillance unique est probabilistiquement disponible dans l'ensemble (puisqu'il existe une probabilité non nulle de défaillances multiples)

Le document parle de la compréhension de la nature probabiliste de la disponibilité. Cela aide à comprendre et à limiter l'impact des pannes en prenant des décisions sur ce qui doit être disponible et sur le type de pannes que le système peut gérer.

Ils décrivent la dégradation linéaire de la récolte en cas de défaillances multiples de nœuds. La récolte est directement proportionnelle au nombre de nœuds qui fonctionnent correctement. Par conséquent, elle diminue/augmente linéairement.

Deux stratégies sont suggérées pour augmenter le rendement :

1. Distribution aléatoire des données sur les nœuds   
Si l'un des nœuds tombe en panne, le comportement moyen et le pire cas de panne ne changent pas. Pourtant, si la distribution n'est pas aléatoire, alors, selon le type de données, l'impact d'une panne peut varier.  
Par exemple, si seul l'un des nœuds stockant des informations liées au solde du compte d'un utilisateur tombe en panne, l'ensemble du système bancaire ne pourra pas fonctionner.
2. Réplication des données les plus importantes  
Cela réduit l'impact si l'un des nœuds contenant un sous-ensemble de données à haute priorité tombe en panne.   
Cela améliore également la récolte.

Une autre observation notable faite dans le document est qu'il est possible de répliquer toutes vos données. Cela ne fait pas grand-chose pour améliorer votre récolte/rendement, mais cela augmente considérablement le coût de fonctionnement. Cela est dû au fait que l'internet fonctionne sur la base de protocoles de type best-effort qui ne peuvent jamais garantir une récolte/rendement à 100 %.

#### Décomposition des Applications et Mécanismes Orthogonaux

La deuxième stratégie se concentre sur les avantages de la conception de systèmes orthogonaux.

Elle commence par affirmer que les grands systèmes sont composés de sous-systèmes qui ne peuvent pas tolérer les défaillances. Mais ils échouent de manière à permettre à l'ensemble du système de continuer à fonctionner avec un certain impact sur l'utilité.

> Le bénéfice réel est la capacité de provisionner la gestion de l'état de chaque sous-système séparément, en fournissant une forte cohérence ou un état persistant uniquement pour les sous-systèmes qui en ont besoin, et non pour l'ensemble de l'application. Les économies peuvent être significatives si seulement quelques petits sous-systèmes nécessitent la complexité supplémentaire.

Le document indique que les composants orthogonaux sont complètement indépendants les uns des autres. Ils n'ont pas d'interface d'exécution avec d'autres composants, sauf s'il y a une interface de configuration. Cela permet à chaque composant individuel de tomber en panne indépendamment et minimise son impact sur le système global.

> La composition de sous-systèmes orthogonaux déplace la charge de vérification des interactions potentiellement nocives du temps d'exécution au temps de compilation, et le déploiement de mécanismes de garde orthogonaux améliore la robustesse des interactions d'exécution qui se produisent, en fournissant un meilleur confinement des pannes.

Le but de ce document était de motiver la recherche dans le domaine de la conception de systèmes à grande échelle tolérants aux pannes et hautement disponibles.

De plus, de réfléchir attentivement aux garanties de cohérence et de disponibilité que l'application doit fournir, ainsi qu'aux compromis qu'elle est capable de faire en termes de récolte contre rendement.

Si vous avez aimé ce document, veuillez cliquer sur le bouton d'applaudissements pour que plus de personnes le voient. Merci.

P.S. — Si vous êtes arrivé jusqu'ici et que vous souhaitez recevoir un e-mail chaque fois que je publie l'un de ces articles, inscrivez-vous [ici](http://eepurl.com/dcHGFP).