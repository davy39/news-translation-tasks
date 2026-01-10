---
title: Pourquoi vous devriez exécuter vos serveurs de jeu indépendamment de votre
  chat
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-11T13:52:16.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-run-your-game-servers-independently-from-your-chat-3263b4b9548e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5SUE6G0j6lpp5N-RYmn_jQ.png
tags:
- name: Game Development
  slug: game-development
- name: Microservices
  slug: microservices
- name: mobile app development
  slug: mobile-app-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous devriez exécuter vos serveurs de jeu indépendamment de votre
  chat
seo_desc: 'By Joe Hanson

  When it comes to building multiplayer games, developers are often faced with a dilemma.


  Do I utilize my existing game servers already powering my multiplayer game functionality
  to run chat?

  Do I separate my game servers and run my chat...'
---

Par Joe Hanson

Lorsqu'il s'agit de développer des jeux multijoueurs, les développeurs sont souvent confrontés à un dilemme.

* Dois-je utiliser mes serveurs de jeu existants qui alimentent déjà la fonctionnalité multijoueur pour gérer le chat ?
* Dois-je séparer mes serveurs de jeu et exécuter mon chat indépendamment ?

Après tout, ce ne sont que des messages de chat, n'est-ce pas ? De petits messages envoyés à un seul utilisateur ou à un petit groupe, alors vous pourriez tout aussi bien utiliser ce qui est déjà construit... qu'est-ce que cela pourrait bien faire ?

Bien que cela puisse sembler une bonne option au départ d'utiliser ce que vous avez déjà, il existe un certain nombre de problèmes qui peuvent survenir en choisissant ce modèle de conception.

Je vais vous montrer pourquoi vous devriez exécuter vos serveurs de jeu et les fonctionnalités sociales (plus important encore, le chat) indépendamment, bénéficiant à la fois à vous en tant que développeur de jeux et à vos utilisateurs finaux. En faisant cela, vous augmenterez les performances et la scalabilité du jeu lui-même, et vous permettrez aux fonctionnalités sociales d'être facilement étendues avec de nouvelles fonctionnalités à l'avenir.

### Les microservices rendent votre jeu plus gérable

Une architecture orientée microservices divise une grande application, dans ce cas votre jeu, en petits services modulaires indépendants et versionnés qui communiquent entre eux via des API simples et universellement accessibles. Cela facilite grandement la construction de nouvelles fonctionnalités et la maintenance des fonctionnalités une fois construites.

Séparer vos serveurs de jeu de votre fonctionnalité de chat rend votre infrastructure entière plus gérable et vous rapproche d'une architecture complètement orientée microservices. Dans ce cas, examinons spécifiquement le chat en jeu et sa relation avec les serveurs de jeu qui alimentent le jeu multijoueur.

Avec une architecture monolithique, votre équipe de développement est maintenant verrouillée dans une seule pile technologique — utilisant les mêmes langages de programmation, bases de données et environnements logiciels sur lesquels le jeu a déjà été construit. Lorsque vous engagez de nouveaux développeurs, ou lorsque vous souhaitez prototyper de nouvelles technologies et systèmes, il est beaucoup plus facile de se déplacer rapidement dans une architecture de microservices.

Les dépendances sont également beaucoup plus apparentes avec les architectures monolithiques. Si votre fonction d'application unique échoue, tout le jeu tombe en panne. Diviser votre jeu en microservices facilite l'isolement d'une faute et sa correction si un seul module échoue.

Vos serveurs de jeu sont conçus pour délivrer les mouvements et l'état des joueurs en temps réel, et ils le font vraiment bien. Réutiliser la même technologie et le même design pour les messages de chat n'est tout simplement pas utiliser les meilleures options pour la fonctionnalité particulière. Les composants décentralisés sont plus faciles à maintenir et ils s'adaptent mieux.

![Image](https://cdn-media-1.freecodecamp.org/images/kxjPuS481xkdGVK8aUOcBCxl-IF3jKlz9ltN)

La figure ci-dessus représente une infrastructure de jeu où le chat est séparé des serveurs de jeu.

De plus, nous pouvons également exécuter d'autres services en dehors des serveurs de jeu, y compris l'autorisation, la présence, les statistiques et les tableaux de classement.

### Assurer une expérience de jeu et des performances de chat sans faille

Globalement, les performances du jeu sont une considération majeure pour un jeu multijoueur. Une expérience de jeu lente éloignera les utilisateurs et ils ne reviendront jamais. Avec une architecture monolithique, le jeu peut performer en laboratoire. Mais pour les jeux multijoueurs avec un grand nombre d'utilisateurs situés partout dans le monde, communiquant tous simultanément à un rythme rapide, vous commencerez à voir des retards et des latences accrues à la fois pour la livraison des messages de chat et l'expérience du jeu.

Séparer les deux garantit que les ressources CPU et réseau sont utilisées plus efficacement. Le but principal de vos serveurs de jeu est de fournir une expérience fluide pour chaque utilisateur dans votre jeu. Par conséquent, la puissance de traitement doit être utilisée pour maximiser cette performance.

Supposons que vous avez un jeu d'arène de bataille en ligne comme League of Legends ou EVE Online. Vous pouvez avoir des centaines de joueurs dans un seul monde, à un seul moment. Cela représente des milliers de messages envoyés à travers vos serveurs de jeu, livrant chaque entrée que chaque joueur crée. Maintenant, ajoutez les messages de chat au mélange. Il est tout à fait possible que les joueurs puissent spammer le canal de chat et ralentir délibérément le serveur de jeu, puisque tous les messages auraient la même priorité. Bien sûr, il serait possible de vérifier ces utilisateurs, mais vous auriez besoin d'un traitement supplémentaire, ce qui mangerait les ressources du serveur de jeu.

Le serveur de jeu gère déjà des expériences de jeu intensives — la physique, les graphiques et le son. Lorsque vous ajoutez des messages de chat — un à un, groupe, équipe — et l'analyse et le routage des messages aux utilisateurs corrects — tous ces messages s'accumulent lentement pour les jeux à grande échelle et nuisent à la performance globale du jeu.

C'est une évidence d'exécuter les canaux de chat séparément des canaux multijoueurs. Cela vole une puissance de traitement importante qui pourrait être mieux adaptée à des problèmes plus complexes que le routage des messages de chat.

### UDP vs. TCP : quand vous avez besoin des deux, et quand vous n'en avez pas besoin

Ensuite, il y a le débat sur les protocoles de jeu multijoueur, UDP vs TCP, et quand il est préférable d'utiliser l'un ou l'autre.

Les jeux multijoueurs rapides (tireurs à la première personne, jeux d'arène, etc.) utilisent le protocole UDP pour synchroniser les mouvements des joueurs et mettre à jour l'état du jeu. L'UDP est idéal pour envoyer ces mises à jour de jeu à une vitesse ridiculement rapide, mais les messages ne sont pas garantis (parce que le message suivant arrive si vite derrière).

Le TCP garantit la livraison des messages, ce qui en fait une excellente option pour le chat. Vous verrez de grandes performances en exécutant votre jeu sur UDP et vos fonctionnalités sociales sur TCP.

![Image](https://cdn-media-1.freecodecamp.org/images/2rINsVWUD5qCbgxJYxq0cYIvUxHFV0iCkQdJ)

Cependant, pour les jeux multijoueurs moins intenses, comme les jeux par tours, le TCP est une option appropriée pour le gameplay et le chat. Parce que le TCP garantit la livraison des messages, et dans les jeux où chaque mouvement compte (comme un tour de Scrabble ou de morpion), c'est une excellente option pour alimenter le gameplay multijoueur. Bien sûr, vous voudrez toujours séparer votre chat des serveurs de jeu, surtout une fois que votre jeu décolle et que vous avez des milliers d'utilisateurs connectés en même temps.

La latence est une autre chose à considérer, car il existe différentes normes de latence pour la fonctionnalité multijoueur par rapport aux fonctionnalités sociales. Pour un jeu multijoueur, assurer l'état du jeu et livrer les entrées des joueurs, la norme de l'industrie est de ne pas dépasser 20 ms. Alors que pour une application de chat, la latence maximale pour la livraison d'un message de chat est de 250 ms.

Vous avez donc deux types différents de messagerie en temps réel, avec deux normes différentes. Les faire fonctionner séparément vous permet de gérer chacun en fonction de ce qui est requis.

### Ajoutez de nouvelles fonctionnalités sociales avec facilité

Exécuter le chat en tant que service autonome et choisir un protocole standard de l'industrie (XMPP, WebSockets) ou un service hébergé ([PubNub](https://www.pubnub.com?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium)), ouvre l'opportunité d'ajouter facilement de nouvelles fonctionnalités sociales puissantes.

Commencez par le chat de base, permettant aux utilisateurs de mener des chats individuels et de groupe. Avec cela, vous avez l'infrastructure sous-jacente, ainsi que la publication/abonnements de base. Et il y a beaucoup d'autres fonctionnalités sociales que vous pouvez facilement construire dessus.

Avec un code minimal, vous pouvez ajouter des fonctionnalités de chat de base comme les indicateurs de frappe, la présence des utilisateurs pour montrer quels joueurs sont en ligne et hors ligne, et les compteurs de messages non lus — des fonctionnalités attendues par les utilisateurs.

### Perspectives d'avenir

Les studios de jeux, grands et petits, se tournent vers cette conception architecturale, y compris [Pocket Gems](https://www.pubnub.com/customers/pocket-gems/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium), et plus récemment [EVE Online](https://www.eveonline.com/article/p4i0qx/new-chat-backend-coming-with-the-march-release). De la meilleure scalabilité et des performances plus efficaces, à la liberté d'innover sans être verrouillé dans une seule pile, les avantages sont clairs : séparer le chat de vos serveurs de jeu est la voie à suivre.

_Publié à l'origine sur [www.pubnub.com](https://www.pubnub.com/blog/why-you-should-run-your-game-servers-separate-from-your-chat/)._