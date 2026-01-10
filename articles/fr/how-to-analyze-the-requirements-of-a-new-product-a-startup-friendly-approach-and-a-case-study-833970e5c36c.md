---
title: 'Analyse des exigences : comment utiliser cette approche adaptée aux startups
  + une étude de cas'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-28T17:11:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-analyze-the-requirements-of-a-new-product-a-startup-friendly-approach-and-a-case-study-833970e5c36c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*10Wu8Q4Oxj0JsvDbXGqJdw.png
tags:
- name: agile
  slug: agile
- name: Apps
  slug: apps-tag
- name: Case Study
  slug: case-study
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Analyse des exigences : comment utiliser cette approche adaptée aux startups
  + une étude de cas'
seo_desc: 'By Turgay Çelik

  In our previous blog posts, we explained why we decided to develop the Badges App
  and how we evaluated the feasibility of our idea at OpsGenie:

  Since we found that our idea is worth developing, the next step is analyzing the
  requireme...'
---

Par Turgay Çelik

Dans nos précédents articles de blog, nous avons expliqué pourquoi nous avons décidé de développer l'application [Badges App](https://engineering.opsgenie.com/badges-app-opsgenies-response-to-skill-tracking-and-management-challenges-c539feb1db9d) et comment nous avons [évalué la faisabilité](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9) de notre idée chez [OpsGenie](https://www.opsgenie.com) :

Puisque nous avons trouvé que notre idée valait la peine d'être développée, l'étape suivante est l'analyse des exigences.

L'analyse des exigences — un domaine très bien étudié du génie logiciel — est le processus de détermination des attentes des utilisateurs pour un produit, ou brièvement de définition de la portée du produit. Il existe des tonnes de ressources disponibles sur les méthodologies d'analyse des exigences, les caractéristiques des bonnes exigences et le suivi des exigences. Au lieu de répéter la littérature, nous allons résumer les points critiques d'une manière adaptée aux startups.

Nous savons que les entrepreneurs de startups n'aiment généralement pas les termes comme « processus », « preuve de concept », « exigences », « portée », « calendrier », « conception », « documentation » ou « maintenabilité ». Généralement, ils sont impatients et veulent simplement coder et publier. Nous acceptons que l'agilité est vitale dans notre monde et que nous devons essayer, échouer et nous rétablir rapidement. Mais bénéficier de l'héritage du monde du logiciel nous aidera sur la voie du succès. Le point clé est de rester agile.

Suivre un processus n'est pas un objectif, c'est un outil qui nous aide à atteindre nos objectifs. Alors, voyons comment nous pouvons adopter les approches classiques dans notre monde dans le contexte de la gestion des exigences.

Le [Triangle de gestion de projet](https://en.wikipedia.org/wiki/Project_management_triangle) est un modèle des contraintes de la gestion de logiciels. Malgré le fait que ce soit un concept ancien des années 1950, je pense qu'il est toujours pertinent.

En résumé, le triangle de gestion de projet dit que la qualité du travail est contrainte par le **budget**, les **délais** et les **fonctionnalités** du projet. Il y a un compromis entre ces trois contraintes pour atteindre la qualité nécessaire du projet. Nous pouvons donc dire que le développement de logiciels est un [problème d'optimisation multi-objectif](https://en.wikipedia.org/wiki/Multi-objective_optimization).

![Image](https://cdn-media-1.freecodecamp.org/images/owsDttjxHCqVOtiAj02sAeV5RQB-5K5z0FTY)
_Le Triangle de gestion de projet (Image de [Wikipedia](https://en.wikipedia.org/wiki/Project_management_triangle" rel="noopener" target="_blank" title="))_

Nous n'aimons pas nous contraindre par des approches classiques, alors adaptons l'ancien Triangle de gestion de projet au nouveau monde des startups. Rappelez-vous les Facteurs de succès des startups que nous avons mentionnés dans l'article [Analyse de faisabilité](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9).

Voici comment nous cartographions ces facteurs de succès au triangle classique de gestion de projet :

![Image](https://cdn-media-1.freecodecamp.org/images/ztFEbFyTRgCO7ffOwMRFTvIcJtpnmcYbjh13)

Comme le montre le tableau ci-dessus, tous les facteurs de succès des startups sont liés à diverses contraintes du triangle de gestion de projet. Puisque ces trois contraintes sont en compromis, nous pouvons dire que garder une portée nette est vital pour le succès d'une startup.

Pour définir une portée nette, nous devons effectuer une bonne analyse des exigences avant de commencer le développement. Veuillez noter que cela ne signifie pas que nous allons effectuer une analyse des exigences entièrement détaillée comme définie dans le processus en cascade. Nous allons le faire de manière agile.

### Conseils pour l'analyse des exigences

Dans cette section, nous allons fournir des conseils importants que vous devez garder à l'esprit :

#### Inspecter les produits alternatifs/similaires en profondeur

Comme toujours, ne réinventez pas la roue. Vérifiez ce que font les autres pour atteindre vos objectifs. Vous pourriez même réaliser que votre produit ne semble pas avoir l'impact commercial que vous pensiez auparavant.

C'est un bon signe pour pivoter votre idée. Cela peut sembler un échec, mais rappelez-vous, **nous devons échouer le plus rapidement possible**.

#### Documenter vos exigences

Vous n'avez pas à utiliser un outil de gestion des exigences tel que [IBM Rational DOORS](https://www.ibm.com/us-en/marketplace/rational-doors). Mais un document d'exigences court et à puces aidera à négocier avec les parties prenantes.

#### Garder vos (potentiels) clients dans la boucle

Je pense que c'est l'une des choses les plus importantes concernant le développement des exigences. Une capacité que vous pensez être révolutionnaire peut ne pas avoir de sens pour les clients.

Pour garder vos clients potentiels dans la boucle, vous devez suivre une approche itérative. Vous pouvez le faire en livrant une version initiale de votre produit — Produit Minimum Viable (MVP) — et en l'améliorant selon les retours des clients.

Par exemple, l'équipe d'Amazon Web Services utilise fréquemment cette approche. Ils livrent un service avec des capacités minimales et l'améliorent en fonction des retours des clients.

Une autre approche consiste à développer des applications fictives qui fournissent simplement une interface utilisateur (UI) factice pour aider le client potentiel à comprendre les fonctionnalités du produit et à donner son avis. Vous pouvez utiliser des produits comme [InvisionApp](https://www.invisionapp.com/) pour produire ces maquettes.

#### La gestion des exigences est un processus continu

Vous n'avez pas à passer des mois à analyser les exigences au début d'un projet, et s'il vous plaît, ne le faites pas — ce n'est pas la manière agile.

Au début, votre objectif est de définir les limites du système, de négocier avec l'équipe et les autres parties prenantes, et de préparer la définition du Produit Minimum Viable. Les exigences doivent être détaillées ou peuvent même évoluer pendant les itérations de développement.

#### Grouper vos exigences

Après avoir créé une liste de toutes vos exigences, regroupez-les (diviser pour mieux régner) pour former des ensembles de fonctionnalités liées. Le regroupement des exigences en groupes de fonctionnalités facilitera votre vie pendant la phase de développement et peut même vous aider à définir des [contextes délimités](https://martinfowler.com/bliki/BoundedContext.html), des architectures de microservices, etc.

#### Penser à l'UX

Il n'est plus nécessaire de dire que l'expérience utilisateur (UX) est un facteur très important dans le succès d'un produit ; aujourd'hui, c'est si évident. Mais nous devons encore rappeler que l'expérience utilisateur ne concerne pas seulement les interfaces utilisateur fantaisistes.

Comme le nom l'indique, il s'agit de l'« expérience » et il est difficile d'améliorer l'UX d'un système après son développement.

Pensez à l'UX dès l'analyse des exigences, cela pourrait même être une motivation pendant la phase d'analyse de faisabilité pour développer un nouveau produit si les alternatives disponibles sur le marché manquent de bonne UX.

L'expérience utilisateur affecte les exigences commerciales. Par exemple, si vous développez une application de commerce électronique, la conception d'un système de support client rapide est une question d'amélioration de l'expérience utilisateur.

#### Être agnostique des technologies de mise en œuvre autant que possible

Bien sûr, cela ne s'applique pas si vous développez une infrastructure ou une bibliothèque pour une technologie spécifique :)

Ne tombez pas dans le piège « Si tout ce que vous avez est un marteau, tout ressemble à un clou ». Trouvez de nouveaux outils et utilitaires au lieu de limiter les capacités du produit aux technologies que vous connaissez ou avec lesquelles vous aimez jouer.

Dans les entreprises, l'analyse des exigences est généralement effectuée par des ingénieurs non-logiciels généralement connus sous le nom d'analystes d'affaires ou d'ingénieurs système. Cette séparation présente certains inconvénients, notamment en termes de transfert des exigences aux équipes de développement, mais je pense qu'elle présente également certains avantages.

À mon avis, le plus grand avantage des équipes d'analyse indépendantes est qu'elles sont agnostiques des technologies qui seront utilisées pendant le développement.

Mais dans le monde des startups, il est probable que, en tant que membre de l'équipe (ou même en tant que fondateur), vous deviez porter plusieurs casquettes : analyste, développeur, responsable du recrutement, ou même des rôles plus intéressants que vous n'imaginiez pas lorsque vous vous êtes engagé dans cette voie. Donc, si vous portez la casquette d'analyste pour le moment, essayez d'être agnostique des technologies que vous prévoyez d'utiliser pendant la mise en œuvre.

Nous entendons constamment des expressions comme « mais le Framework Spring ne supporte pas… » et « Cela cause beaucoup de travail sur le front-end » pendant l'analyse des exigences.

Prendre en compte ces types de limitations dès le départ dégrade la qualité du produit final. Définissons la capacité ultime et faisons-la évoluer pendant le développement si nécessaire.

La capacité ultime est l'objectif final à atteindre, vous pouvez implémenter une forme plus simple au début et la faire évoluer dans les versions futures. Mais connaître le point que nous voulons atteindre nous aidera à définir notre vision pour la croissance du produit.

Par exemple, pensez à la capacité « pincer pour zoomer » des téléphones mobiles. Cela semble être une capacité triviale, mais c'était une révolution lorsque [Steve Jobs l'a démontrée pour la première fois](https://www.youtube.com/watch?v=ze559mhbrD0). Si les concepteurs de l'iPhone n'avaient pas pensé hors des sentiers battus et s'étaient cantonnés aux technologies et méthodes disponibles, nous n'aurions pas cette fonctionnalité aujourd'hui. Nous savons que c'est un exemple exagéré, mais le point principal est de ne pas laisser la technologie que vous souhaitez utiliser vous limiter, vous pouvez passer à d'autres technologies si cela vous aide à créer un produit de niche.

### Analyse des exigences pour l'application Badges

Nous avons effectué l'analyse des exigences selon les pratiques que nous avons résumées ci-dessus :

* Nous avons défini un ensemble initial d'exigences
* Nous avons partagé les exigences avec notre premier client — l'équipe OpsGenie — et mis à jour les exigences selon les commentaires de l'équipe.
* Chez OpsGenie, nous utilisons JIRA d'Atlassian pour le suivi des problèmes. Pour suivre les exigences, nous avons créé un problème de type « Nouvelle fonctionnalité » pour chaque exigence dans JIRA.
* Nous avons regroupé les exigences liées avec des [Épics JIRA](https://confluence.atlassian.com/agile/jira-agile-user-s-guide/working-with-epics). Certaines de nos épics sont les opérations utilisateur, les opérations de groupe, les opérations de badge, l'approbation et l'intégration d'outils tiers.
* Dans les étapes ultérieures du développement, nous avons créé des problèmes détaillés pour les tâches quotidiennes, comme le recommandent les pratiques Agile. Nous avons lié chaque tâche à une ou plusieurs exigences pour garder la traçabilité des activités de développement avec les exigences.
* Chaque épic contient un ensemble d'exigences (comme une nouvelle fonctionnalité), des tâches de développement et des bugs.

![Image](https://cdn-media-1.freecodecamp.org/images/NV65NKbZ1GLiSwXILHrxsnRv18fgFbyX85nV)
_Traçage des exigences avec les tâches de développement_

Vous souhaitez suivre notre application Badges, ou mieux encore, recommander de nouvelles fonctionnalités et nous aider à l'améliorer ? [Rejoignez](https://community.opsgenie.com/c/badges) la communauté de l'application Badges !

Pour aller plus loin :

[**Badges App : La réponse d'OpsGenie aux défis de suivi et de gestion des compétences**](https://engineering.opsgenie.com/badges-app-opsgenies-response-to-skill-tracking-and-management-challenges-c539feb1db9d)  
[_Comme nous voyons le suivi et la gestion des compétences comme une tâche cruciale pour la croissance saine de notre entreprise, nous avons investi dans un…_engineering.opsgenie.com](https://engineering.opsgenie.com/badges-app-opsgenies-response-to-skill-tracking-and-management-challenges-c539feb1db9d)[**Comment avons-nous décidé que notre nouvelle idée de produit était réalisable ?**](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9)  
[_Alors, nous avons une nouvelle idée de produit, et nous pensons qu'elle serait « utile », « géniale » et même, « Elle rendra le monde…_engineering.opsgenie.com](https://engineering.opsgenie.com/how-did-we-decide-that-our-new-product-idea-is-feasible-d43e0fc6fde9)