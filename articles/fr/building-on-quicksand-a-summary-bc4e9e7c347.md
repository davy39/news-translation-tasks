---
title: 'Construire sur du sable mouvant : Un résumé'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T17:11:21.000Z'
originalURL: https://freecodecamp.org/news/building-on-quicksand-a-summary-bc4e9e7c347
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb210740569d1a4cabf7a.jpg
tags:
- name: Computer Science
  slug: computer-science
- name: distributed systems
  slug: distributed-systems
- name: research
  slug: research
- name: summary
  slug: summary
- name: technology
  slug: technology
seo_title: 'Construire sur du sable mouvant : Un résumé'
seo_desc: 'By Shubheksha Jalan

  Let’s try to break down the paper “Building On Quicksand” published by Pat Helland
  and David Campbell in 2009. All pull quotes are from the paper.

  The paper focuses on the design of large, fault-tolerant, replicated distributed
  sy...'
---

Par Shubheksha Jalan

Essayons de décomposer l'article « [Building On Quicksand](http://arxiv.org/ftp/arxiv/papers/0909/0909.1788.pdf) » publié par Pat Helland et David Campbell en 2009. Toutes les citations sont tirées de l'article.

L'article se concentre sur la conception de grands systèmes distribués répliqués et tolérants aux pannes. Il discute également de leur évolution en fonction des exigences changeantes au fil du temps. Il commence par affirmer que « Les systèmes fiables ont toujours été construits à partir de composants non fiables ».

> À mesure que la granularité du composant non fiable augmente (d'un disque miroir à un système à un centre de données), la latence pour communiquer avec une sauvegarde devient inacceptable. Cela conduit à un modèle plus souple pour la tolérance aux pannes. Le système principal accusera réception de la demande de travail et de ses actions sans attendre de s'assurer que la sauvegarde est informée du travail. Cela améliore la réactivité du système car l'utilisateur n'est pas retardé par une interaction lente avec la sauvegarde.

Les systèmes tolérants aux pannes peuvent être composés de nombreux composants. Leur objectif est de continuer à fonctionner lorsque l'un de ces composants tombe en panne. Nous ne considérons pas les **_défaillances byzantines_** dans cette discussion. Au lieu de cela, le modèle **_fail fast_** où soit un composant fonctionne correctement, soit il tombe en panne.

L'article compare ensuite deux versions du système Tandem NonStop. L'une utilisait un [checkpointing](https://en.wikipedia.org/wiki/Application_checkpointing) synchrone et l'autre un checkpointing asynchrone. Voir la section 3 de l'article pour tous les détails. J'aimerais aborder la différence entre les deux stratégies de checkpointing.

* Checkpointing synchrone : dans ce cas, avec chaque écriture sur le système principal, l'état devait être envoyé à la sauvegarde. Ce n'est qu'après que la sauvegarde a accusé réception de l'écriture que le système principal a envoyé une réponse au client qui a émis la demande d'écriture. Cela garantissait que lorsque le système principal tombe en panne, la sauvegarde peut prendre le relais sans perdre de travail.
* Checkpointing asynchrone : dans cette stratégie, le système principal accuse réception et valide l'écriture. Cela est fait dès qu'il la traite sans attendre de réponse de la sauvegarde. Cette technique améliore la latence mais pose également d'autres défis abordés plus tard.

#### Expédition de journaux

> Un système de base de données classique dispose d'un processus qui lit le journal et l'envoie à un centre de données de sauvegarde. L'implémentation normale de ce mécanisme valide les transactions sur le système principal (accusant réception de la demande de validation de l'utilisateur) et envoie le journal de manière asynchrone. La base de données de sauvegarde rejoue le journal, jouant constamment à rattraper son retard.

Le mécanisme décrit ci-dessus est appelé expédition de journaux. Le principal problème que cela pose est que lorsque le système principal tombe en panne et que la sauvegarde prend le relais, certaines transactions récentes peuvent être perdues.

> Cela ouvre intrinsèquement une fenêtre dans laquelle le travail est accusé réception au client mais il n'a pas encore été envoyé à la sauvegarde. Une défaillance du système principal pendant cette fenêtre verrouillera le travail à l'intérieur du système principal pendant une période de temps inconnue. La sauvegarde avancera sans connaissance du travail verrouillé.

L'introduction de l'asynchronisme dans le système présente un avantage en termes de latence, de temps de réponse et de performance. Cependant, cela rend le système plus sujet à la possibilité de perdre du travail lorsque le système principal tombe en panne. Il existe deux façons de gérer cela :

1. Abandonner le travail verrouillé dans le système principal lorsqu'il tombe en panne. Qu'un système puisse le faire ou non dépend des exigences et des règles métiers.
2. Avoir un mécanisme de récupération pour synchroniser le système principal avec les sauvegardes lorsqu'il redémarre et retenter le travail perdu. Cela n'est possible que si les opérations peuvent être retentées de manière idempotente et que les retentatives hors ordre sont possibles.

Le système perd la notion de ce que les auteurs appellent « une vérité autoritaire ». Personne ne connaît l'état exact du système à un moment donné si le travail est verrouillé dans une sauvegarde ou un système principal indisponible.

Les auteurs concluent que les règles métiers dans un système avec checkpointing asynchrone sont probabilistes.

> Si un système principal utilise un checkpointing asynchrone et applique une règle métier sur le travail entrant, il s'agit nécessairement d'une règle probabiliste. Le système principal, malgré ses meilleures intentions, ne peut pas savoir s'il restera en vie pour faire respecter les règles métiers.

> Lorsque le système de sauvegarde qui participe à l'application de ces règles métiers est lié de manière asynchrone au système principal, l'application de ces règles devient inévitablement probabiliste !

Les auteurs affirment que les opérations commutatives, les opérations qui peuvent être réordonnées, peuvent être exécutées indépendamment, tant que l'opération préserve les règles métiers. Cependant, cela est difficile à faire avec les systèmes de stockage car l'opération d'écriture n'est pas commutative.

Une autre considération est que le travail d'une seule opération est idempotent. Par exemple, l'exécution de l'opération un nombre quelconque de fois devrait aboutir au même état du système.

> Pour garantir cela, les applications attribuent généralement un numéro ou un identifiant unique au travail. Cela est attribué à l'entrée du système (c'est-à-dire la réplique qui traite d'abord le travail). À mesure que la demande de travail circule dans le réseau, il est facile pour une réplique de détecter qu'elle a déjà vu cette opération et, par conséquent, de ne pas faire le travail deux fois.

Les auteurs suggèrent que différentes opérations au sein d'un système fournissent différentes garanties de cohérence. Pourtant, cela dépend des exigences métiers. Certaines opérations peuvent choisir la cohérence classique plutôt que la disponibilité et vice versa.

Ensuite, les auteurs soutiennent que dès qu'il n'y a pas de notion de vérité autoritaire dans un système, tout le calcul se résume à trois choses : les mémoires, les conjectures et les excuses.

1. Mémoires : vous ne pouvez qu'espérer que votre réplique se souvienne de ce qu'elle a déjà vu.
2. Conjectures : En raison de la disponibilité de connaissances partielles, les répliques prennent des actions basées sur l'état local et peuvent se tromper. « Dans tout système qui permet une dégradation de la vérité absolue, toute action est, au mieux, une conjecture. » Toute action dans un tel système a une forte probabilité de réussir, mais il s'agit toujours d'une conjecture.
3. Excuses : Les erreurs sont inévitables. Par conséquent, chaque entreprise doit avoir un mécanisme d'excuses en place, soit par intervention humaine, soit en l'automatisant.

L'article aborde ensuite le sujet de la cohérence éventuelle. Les auteurs le font en prenant l'exemple du panier d'achat Amazon construit avec Dynamo et un système de compensation des chèques. Une seule réplique identifie et traite le travail entrant dans ces systèmes. Il circule vers d'autres répliques au fur et à mesure que la connectivité le permet. Les demandes entrant dans ces systèmes sont commutatives (réordonnables). Elles peuvent être traitées sur différentes répliques dans des ordres différents.

> Les systèmes de stockage seuls ne peuvent pas fournir la commutativité dont nous avons besoin pour créer des systèmes robustes qui fonctionnent avec un checkpointing asynchrone. Nous avons besoin que les opérations métiers se réordonnent. Amazon's Dynamo ne fait pas cela par lui-même. L'application de panier d'achat au-dessus du système de stockage Dynamo est responsable de la sémantique de la cohérence éventuelle et de la commutativité. Les auteurs pensent qu'il est temps pour nous de passer l'examen de la cohérence éventuelle en termes de mises à jour et de systèmes de stockage. L'action réelle vient lorsque l'on examine la sémantique des opérations basées sur les applications.

Ensuite, ils discutent de deux stratégies pour allouer des ressources dans des répliques qui peuvent ne pas être en mesure de communiquer entre elles :

1. Sur-provisionnement : les ressources sont partitionnées entre les répliques. Chacune dispose d'un sous-ensemble fixe de ressources qu'elle peut allouer. Aucune réplique ne peut allouer une ressource qui n'est pas réellement disponible.
2. Sur-réservation : les ressources peuvent être allouées individuellement sans garantir un partitionnement strict. Cela peut conduire les répliques à allouer une ressource qui n'est pas disponible, promettant quelque chose qu'elles ne peuvent pas livrer.

L'article parle également de quelque chose appelé le « modèle de réservation de siège ». Il s'agit d'un compromis entre le sur-provisionnement et la sur-réservation :

> Toute personne ayant acheté des billets en ligne reconnaîtra le modèle de « Réservation de Siège » où vous pouvez identifier des sièges potentiels et disposez ensuite d'une période de temps limitée (généralement quelques minutes) pour conclure la transaction. Si la transaction n'est pas conclue avec succès dans le délai imparti, les sièges sont à nouveau marqués comme « disponibles ».

#### ACID 2.0

La définition classique de ACID signifie « Atomique, Cohérent, Isolé et Durable ». Son objectif est de faire croire à l'application qu'il existe un seul ordinateur qui ne fait rien d'autre lorsque la transaction est traitée. Les auteurs parlent d'une nouvelle définition pour ACID, qui signifie Associatif, Commutatif, Idempotent et Distribué.

> L'objectif de ACID 2.0 est de réussir si les morceaux du travail se produisent : Au moins une fois, n'importe où dans le système, dans n'importe quel ordre. Cela définit un nouveau TYPE de cohérence. Les étapes individuelles se produisent sur un ou plusieurs systèmes. L'application est explicitement tolérante au travail se produisant dans le désordre. Elle est tolérante au fait que le travail se produise plus d'une fois par machine.

Selon la définition classique de ACID, un historique linéaire est une base pour la tolérance aux pannes. Si nous voulons obtenir les mêmes garanties dans un système distribué, cela nécessitera des mécanismes de contrôle de concurrence qui « tendent à être fragiles ».

> Lorsque l'application est contrainte par les exigences supplémentaires de commutativité et d'associativité, le monde devient BEAUCOUP plus facile. Il n'est plus nécessaire que l'état soit checkpointé à travers les unités de défaillance de manière synchrone. Au lieu de cela, il est possible d'être très paresseux quant au partage des informations. Cela ouvre la voie à des liens hors ligne, lents, des centres de données de faible qualité, et plus encore.

En conclusion :

> Nous avons tenté de décrire les modèles utilisés par de nombreuses applications aujourd'hui alors qu'elles font face à des défaillances dans des systèmes largement distribués. C'est la possibilité de réordonner le travail et la répétabilité du travail qui est essentielle pour permettre une exécution réussie des applications au-dessus du chaos d'un monde distribué dans lequel les systèmes viennent et vont quand ils le souhaitent.

P.S. — Si vous êtes arrivé jusqu'ici et que vous souhaitez recevoir un e-mail chaque fois que je publie l'un de ces articles, inscrivez-vous [ici](http://eepurl.com/dcHGFP).