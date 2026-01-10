---
title: 'Robustesse dans les systèmes complexes : un résumé d''article académique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-22T15:43:29.000Z'
originalURL: https://freecodecamp.org/news/robustness-in-complex-systems-a-summary-95d6f4067116
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hHLvV3GwQhGGhPF0G8-MHw.jpeg
tags:
- name: General Programming
  slug: programming
- name: research
  slug: research
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Robustesse dans les systèmes complexes : un résumé d''article académique'
seo_desc: 'By Shubheksha Jalan

  Today, we’re going to look at the paper titled “Robustness in Complex Systems” published
  in 2001 by Steven D. Gribble. All pull quotes and figures are from the paper.


  This paper argues that a common design paradigm for systems is...'
---

Par Shubheksha Jalan

Aujourd'hui, nous allons examiner l'article intitulé « [Robustness in Complex Systems](https://www.gribble.org/papers/robust.pdf) » publié en 2001 par Steven D. Gribble. Toutes les citations et figures sont tirées de l'article.

> Cet article soutient qu'un paradigme de conception courant pour les systèmes est fondamentalement défectueux, entraînant un comportement instable et imprévisible à mesure que la complexité du système augmente.

Le « paradigme de conception courant » fait référence à la pratique de prédire l'environnement dans lequel le système fonctionnera et ses modes de défaillance. L'article indique qu'un système sera confronté à des conditions non prévues à mesure qu'il devient plus complexe, il doit donc être conçu pour gérer les défaillances de manière élégante. L'article explore ces idées à l'aide de « distributed data structures (DDD), un serveur de stockage scalable et basé sur des clusters ».

> Par leur nature même, les grands systèmes fonctionnent grâce à l'interaction complexe de nombreux composants. Cette interaction conduit à un couplage omniprésent des éléments du système ; ce couplage peut être fort (par exemple, les paquets envoyés entre les routeurs adjacents dans un réseau) ou subtil (par exemple, la synchronisation des annonces de routage dans un réseau étendu).

Une caractéristique commune que de tels grands systèmes présentent est quelque chose connu sous le nom d'[Effet papillon](https://en.wikipedia.org/wiki/Butterfly_effect). Cela fait référence à une petite perturbation inattendue dans le système résultant de l'interaction complexe de divers composants qui provoque un changement généralisé.

Un objectif courant pour la conception de systèmes est la robustesse : la capacité d'un système à fonctionner correctement dans diverses conditions et à échouer de manière élégante dans une situation inattendue. L'article s'oppose au schéma courant consistant à essayer de prédire un certain ensemble de conditions de fonctionnement pour le système et à l'architecturer pour qu'il fonctionne bien dans **seulement ces** conditions.

> Il est également effectivement impossible de prédire toutes les perturbations qu'un système subira en raison des changements dans les conditions environnementales, telles que les défaillances matérielles, les pics de charge ou l'introduction de logiciels malveillants. Étant donné cela, nous croyons que tout système qui tente de gagner en robustesse uniquement par la précognition est sujet à la fragilité.

### DDS : Une étude de cas

L'hypothèse énoncée ci-dessus est explorée à l'aide d'un système de stockage scalable et basé sur des clusters, Distributed Data Structures (DDD) — « une table de hachage virtuelle à haute capacité et à haut débit qui est partitionnée et répliquée sur de nombreux nœuds de stockage individuels appelés bricks ».

![Image](https://cdn-media-1.freecodecamp.org/images/pCMHFuUnLdELprmvHYYW8ZuJ4F-3bKymp1YJ)

Ce système a été construit en utilisant une philosophie de conception prédictive comme celle décrite ci-dessus.

> Sur la base d'une expérience approfondie avec de tels systèmes, nous avons tenté de raisonner sur le comportement des composants logiciels, des algorithmes, des protocoles et des éléments matériels du système, ainsi que sur les charges de travail qu'il recevrait.

Lorsque le système fonctionnait dans le cadre des hypothèses faites par les concepteurs, il fonctionnait bien. Ils ont pu le mettre à l'échelle et améliorer les performances. Cependant, dans le cas où une ou plusieurs des hypothèses sur les conditions de fonctionnement étaient violées, le système se comportait de manière inattendue, entraînant une perte de données ou des incohérences.

Ensuite, nous parlons de plusieurs de ces anomalies.

#### **Garbage Collection Thrashing et Bounded Synchrony**

Les concepteurs du système ont utilisé des délais d'attente pour détecter la défaillance des composants dans le système. Si un composant particulier ne répondait pas dans le temps spécifié, il était considéré comme mort. Ils ont supposé une synchronie bornée dans le système.

> Le DDS a été implémenté en Java et utilisait donc la collecte des déchets. Le garbage collector dans notre JVM était un collecteur de type mark-and-sweep ; par conséquent, plus il y avait d'objets actifs résidents dans le tas JVM, plus la durée pendant laquelle le garbage collector s'exécuterait pour récupérer une quantité fixe de mémoire augmenterait.

Lorsque le système était à saturation, même de légères variations de charge sur les bricks augmentaient le temps pris par le garbage collector, réduisant ainsi le débit du brick. Cela s'appelle le **GC thrashing**. Les bricks affectés prenaient du retard par rapport à leurs homologues, entraînant une dégradation supplémentaire des performances du système.

![Image](https://cdn-media-1.freecodecamp.org/images/9dhVsogmVj7xeTLMrAC-MB4iE7RjXYZE2hXF)

Ainsi, la collecte des déchets violait l'hypothèse de synchronie bornée lorsqu'elle approchait ou dépassait le point de saturation.

#### **Slow Leaks et Co-related Failure**

Une autre hypothèse faite lors de la conception du système était que les défaillances sont indépendantes. DDS utilisait la réplication pour rendre le système tolérant aux pannes. La probabilité que plusieurs répliques tombent en panne simultanément était très faible.

Cependant, cette hypothèse a été violée lorsqu'ils ont rencontré une condition de course dans leur code qui provoquait une fuite de mémoire sans affecter la correction.

> Chaque fois que nous lancions notre système, nous avions tendance à lancer tous les bricks en même temps. Étant donné une charge à peu près équilibrée dans le système, tous les bricks manquaient donc d'espace de tas presque au même moment, plusieurs jours après leur lancement. Nous avons également spéculé que nos mécanismes de basculement automatique aggravaient cette situation en augmentant la charge sur une réplique après qu'un pair avait échoué, augmentant le taux auquel la réplique fuyait de la mémoire.

Puisque toutes les répliques étaient soumises à une charge uniforme sans prendre en compte la dégradation des performances et d'autres problèmes, cela créait un couplage entre les répliques et...

> ...quand cela était combiné avec une fuite de mémoire lente, cela conduisait à la violation de notre hypothèse de défaillances indépendantes, ce qui à son tour causait à notre système de subir une indisponibilité et une perte partielle de données.

#### **Unchecked Dependencies and Fail-stop**

Sur la base de l'hypothèse que si un composant dépassait le délai d'attente, il avait échoué, les concepteurs ont également supposé des défaillances « fail-stop », c'est-à-dire qu'un composant qui avait échoué ne reprendrait pas son fonctionnement après un certain temps. Les bricks du système effectuaient tout le travail à latence longue (E/S disque) de manière asynchrone.

Cependant, ils n'ont pas remarqué que certaines parties de leur code utilisaient des appels de fonction bloquants. Cela a provoqué le blocage aléatoire du thread principal de gestion des événements, entraînant l'arrêt inexplicable des bricks pendant quelques minutes et leur reprise par la suite.

> Bien que cette erreur soit due à notre propre échec à vérifier le comportement du code que nous utilisions, elle sert à démontrer que l'interaction de bas niveau entre des composants construits indépendamment peut avoir des implications profondes sur le comportement global du système. Un changement très subtil de comportement a entraîné la violation de notre hypothèse de fail-stop dans l'ensemble du cluster, ce qui a finalement conduit à la corruption des données dans notre système.

### Vers des systèmes robustes

> ..de petits changements dans un système complexe et couplé peuvent entraîner de grands changements inattendus dans le comportement, pouvant faire sortir le système du régime de fonctionnement attendu par ses concepteurs.

Quelques solutions qui peuvent nous aider à créer des systèmes plus robustes :

#### Sur-provisionnement systématique

Lorsqu'ils approchent du point de saturation, les systèmes tendent à devenir fragiles lorsqu'ils tentent d'accommoder un comportement inattendu. Une façon de combattre cela est de sur-provisionner délibérément le système.

![Image](https://cdn-media-1.freecodecamp.org/images/eOxFAEt5Vdd1dOchH6GpyfpXb2-ZXKOHLcwx)

Cependant, cela présente son propre ensemble de problèmes : cela conduit à la sous-utilisation des ressources. Cela nécessite également de prédire l'environnement de fonctionnement attendu et donc le point de saturation du système. Cela ne peut pas être fait de manière précise dans la plupart des cas.

#### Utiliser le contrôle d'admission

Une autre technique consiste à commencer à rejeter la charge une fois que le système commence à approcher du point de saturation. Cependant, cela nécessite de prédire le point de saturation — quelque chose qui n'est pas toujours possible, surtout avec les grands systèmes qui ont beaucoup de variables contributives.

Le rejet des demandes consomme également certaines ressources du système. Les services conçus avec le contrôle d'admission à l'esprit ont généralement deux modes de fonctionnement : normal où les demandes sont traitées et un mode extrêmement léger où elles sont rejetées.

#### Intégrer l'introspection dans le système

> un système introspectif est un système dans lequel la capacité à surveiller le système est conçue dès le début.

Lorsque un système peut être surveillé, et que les concepteurs et les opérateurs peuvent dériver des mesures significatives sur son fonctionnement, il est beaucoup plus robuste qu'un système boîte noire. Il est plus facile d'adapter un tel système au changement dans son environnement, ainsi que de le gérer et de le maintenir.

#### Introduire l'adaptabilité en fermant la boucle de contrôle

Un exemple de boucle de contrôle est celui des concepteurs et opérateurs humains adaptant la conception en réponse à un changement dans son environnement de fonctionnement indiqué par diverses mesures. Cependant, la chronologie d'une telle boucle de contrôle n'est pas très prévisible. Les auteurs soutiennent que les systèmes doivent être construits avec des boucles de contrôle internes.

> Ces systèmes intègrent les résultats de l'introspection et tentent d'adapter dynamiquement les variables de contrôle pour maintenir le système en fonctionnement dans un régime stable ou performant.

> Tous ces systèmes ont la propriété que le composant effectuant l'adaptation est capable d'émettre des hypothèses quelque peu précises sur les effets de l'adaptation ; sans cette capacité, le système fonctionnerait « dans le noir » et deviendrait probablement imprévisible. Une nouvelle approche intéressante pour émettre des hypothèses sur les effets de l'adaptation consiste à utiliser l'apprentissage automatique statistique ; étant donné cela, un système peut expérimenter des changements afin de construire un modèle de leurs effets.

#### Planifier pour l'échec

> Les systèmes complexes doivent s'attendre à l'échec et planifier en conséquence.

Quelques techniques pour le faire :

1. découplage des composants pour contenir les échecs localement
2. minimiser les dommages en utilisant des abstractions robustes telles que les transactions
3. minimiser la durée de l'état d'échec (en utilisant des points de contrôle pour une récupération rapide)

Dans cet article, les auteurs soutiennent que la conception de systèmes en supposant les contraintes et la nature de leur fonctionnement, des échecs et du comportement conduit souvent à des systèmes fragiles et imprévisibles. Nous avons besoin d'une approche radicalement différente pour construire des systèmes plus robustes face à l'échec.

> Ce paradigme de conception différent est celui dans lequel les systèmes ont la meilleure chance possible de comportement stable (grâce à des techniques telles que le sur-provisionnement, le contrôle d'admission et l'introspection), ainsi que la capacité de s'adapter à des situations inattendues (en traitant l'introspection comme un retour d'information pour une boucle de contrôle fermée). En fin de compte, les systèmes doivent être conçus pour gérer les échecs de manière élégante, car la complexité semble conduire à une imprévisibilité inévitable.