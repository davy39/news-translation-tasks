---
title: Une note sur les systèmes distribués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-18T18:26:34.000Z'
originalURL: https://freecodecamp.org/news/a-note-on-distributed-systems-3c796f1eb0a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tYxWuyksovxA1Thu8PggPQ.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: research
  slug: research
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une note sur les systèmes distribués
seo_desc: 'By Shubheksha Jalan

  This post distills the material presented in the paper titled “A Note on Distributed
  Systems” published in 1994 by Jim Waldo and others.

  The paper presents the differences between local and distributed computing in the
  context of ...'
---

Par Shubheksha Jalan

Cet article résume le contenu présenté dans le document intitulé « [A Note on Distributed Systems](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.41.7628) » publié en 1994 par Jim Waldo et d'autres.

Le document présente les différences entre l'informatique locale et distribuée dans le contexte de la programmation orientée objet. Il explique pourquoi les traiter de la même manière est incorrect et conduit à des applications qui ne sont pas robustes ou fiables.

#### Introduction

Le document commence en affirmant que les travaux actuels sur les systèmes distribués sont modélisés autour des objets — plus précisément, une **vision unifiée des objets**. Les objets sont définis par leurs interfaces prises en charge et les opérations qu'ils supportent.

Naturellement, cela peut être étendu pour impliquer que les objets dans le même espace d'adressage, ou dans un espace d'adressage différent sur la même machine, ou sur une machine différente, se comportent tous de manière similaire. Leur localisation est un détail d'implémentation.

Définissons les termes les plus courants dans ce document :

#### Informatique locale

Elle traite des programmes qui sont confinés à un seul espace d'adressage.

#### Informatique distribuée

Elle traite des programmes qui peuvent faire des appels à des objets dans différents espaces d'adressage, soit sur la même machine, soit sur une machine différente.

#### La vision des objets unifiés

Implicite dans cette vision est que le système sera « des objets jusqu'au bout ». Cela signifie que toutes les invocations actuelles, ou appels pour des services système, seront finalement converties en appels qui pourraient être faits à un objet résidant sur une autre machine. Il existe un seul paradigme d'utilisation et de communication des objets, quel que soit l'emplacement de l'objet.

Cela fait référence à l'hypothèse que tous les objets sont définis uniquement en termes de leurs interfaces. Leur implémentation inclut également l'emplacement de l'objet et est indépendante de leurs interfaces et cachée au programmeur.

En ce qui concerne le programmeur, il écrit le même type d'appel pour chaque objet, qu'il soit local ou distant. Le système se charge d'envoyer le message en déterminant les mécanismes sous-jacents non visibles pour le programmeur qui écrit l'application.

Les problèmes difficiles de l'informatique distribuée ne sont pas les problèmes de savoir comment mettre les choses sur et hors du fil.

Le document définit ensuite les défis les plus difficiles de la construction d'un système distribué :

1. Latence
2. Accès à la mémoire
3. Défaillance partielle et concurrency

Assurer des performances raisonnables tout en traitant tous les points ci-dessus ne facilite pas la vie d'un ingénieur en systèmes distribués. Et l'absence de toute ressource centrale ou gestionnaire d'état ajoute aux divers défis. Observons chacun de ces points un par un.

#### Latence

C'est la différence fondamentale entre l'invocation d'objets locaux et distribués.

Le document affirme qu'un appel distant est quatre à cinq fois plus lent qu'un appel local. Si la conception d'un système ne reconnaît pas cette différence fondamentale, il est voué à souffrir de sérieux problèmes de performance. Surtout s'il repose sur la communication à distance.

Vous devez avoir une compréhension approfondie de l'application en cours de conception afin de pouvoir décider quels objets doivent être conservés ensemble et lesquels peuvent être placés à distance.

Si l'objectif est d'unifier la différence de latence, alors nous avons deux options :

* Compter sur le matériel pour qu'il devienne plus rapide avec le temps afin d'éliminer la différence d'efficacité
* Développer des outils qui nous permettent de visualiser les schémas de communication entre différents objets et de les déplacer selon les besoins. Puisque la localisation est un détail d'implémentation, cela ne devrait pas être trop difficile à réaliser

#### Mémoire

Une autre différence très pertinente pour la conception des systèmes distribués est le schéma d'accès à la mémoire entre les objets locaux et distants. Un pointeur dans l'espace d'adressage local n'est pas valide dans un espace d'adressage distant.

Nous avons deux choix :

* Le développeur doit être conscient de la différence entre les schémas d'accès
* Pour unifier les différences d'accès entre l'accès local et distant, nous devons laisser le système gérer tous les aspects de l'accès à la mémoire.

Il existe plusieurs façons de le faire :

* Mémoire partagée distribuée
* En utilisant le paradigme [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) (programmation orientée objet), composer un système entièrement d'objets — un système qui ne traite que des références d'objets.   
Le transfert de données entre les espaces d'adressage peut être traité en marshalisant et démarshalisant les données par la couche sous-jacente. Cette approche, cependant, rend l'utilisation des pointeurs relatifs à l'espace d'adressage obsolète.

Le danger réside dans la promotion du mythe que « l'accès distant et l'accès local sont exactement les mêmes ». Nous ne devrions pas renforcer ce mythe. Un mécanisme sous-jacent qui ne unifie pas tous les accès à la mémoire tout en promouvant ce mythe est à la fois trompeur et sujet à des erreurs.

Il est important que les programmeurs soient conscients des diverses différences entre l'accès aux objets locaux et distants. Nous ne voulons pas qu'ils soient pris au dépourvu en ne sachant pas ce qui se passe sous le capot.

#### Défaillance partielle et concurrency

La défaillance partielle est une réalité centrale de l'informatique distribuée.

Le document soutient que les systèmes locaux et distribués sont tous deux sujets à des défaillances. Mais il est plus difficile de découvrir ce qui n'a pas fonctionné dans le cas des systèmes distribués.

Pour un système local, soit tout est arrêté, soit il y a une autorité centrale qui peut détecter ce qui n'a pas fonctionné (le système d'exploitation, par exemple).

Pourtant, dans le cas d'un système distribué, il n'y a pas d'état global ou de gestionnaire de ressources disponible pour suivre tout ce qui se passe dans et à travers le système. Il n'y a donc aucun moyen d'informer les autres composants, qui peuvent fonctionner correctement, lesquels ont échoué. Les composants d'un système distribué échouent indépendamment.

Un problème central de l'informatique distribuée est de s'assurer que l'état de l'ensemble du système est cohérent après une telle défaillance. C'est un problème qui ne se pose tout simplement pas dans l'informatique locale.

Pour qu'un système résiste à une défaillance partielle, il est important qu'il traite l'indétermination et que les objets réagissent de manière cohérente. Les interfaces doivent pouvoir indiquer la cause de la défaillance, si possible. Et permettre ensuite la reconstruction d'un « état raisonnable » si la cause ne peut pas être déterminée.

La question n'est pas « pouvez-vous faire en sorte que l'invocation de méthode à distance ressemble à l'invocation de méthode locale », mais plutôt « quel est le prix pour rendre l'invocation de méthode à distance identique à l'invocation de méthode locale ? »

Deux approches viennent à l'esprit :

1. Traiter toutes les interfaces et objets comme locaux. Le problème avec cette approche est qu'elle ne prend pas en compte les modèles de défaillance associés aux systèmes distribués. Par conséquent, elle est indéterministe par nature.
2. Traiter toutes les interfaces et objets comme distants. Le défaut de cette approche est qu'elle complique excessivement l'informatique locale. Elle ajoute une tonne de travail pour les objets qui ne sont jamais accédés à distance.

Une meilleure approche est d'accepter qu'il existe des différences irréconciliables entre l'informatique locale et distribuée, et d'être conscient de ces différences à toutes les étapes de la conception et de l'implémentation des applications distribuées.

P.S. — Si vous êtes arrivé jusqu'ici et que vous souhaitez recevoir un mail chaque fois que je publie un de ces articles, inscrivez-vous [ici](http://eepurl.com/dcHGFP).