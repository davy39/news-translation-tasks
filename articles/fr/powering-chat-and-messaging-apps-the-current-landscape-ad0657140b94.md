---
title: 'Combien construire et combien acheter : alimenter les applications de chat
  et de messagerie'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-18T16:48:20.000Z'
originalURL: https://freecodecamp.org/news/powering-chat-and-messaging-apps-the-current-landscape-ad0657140b94
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5pSZtT1kQVHNijWUaikmqA.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Combien construire et combien acheter : alimenter les applications de
  chat et de messagerie'
seo_desc: 'By Joe Hanson

  When you’re building a chat application of any kind — from mobile group messaging
  and multiplayer in-game chat, to customer support and chatbots — choosing the right
  platforms, frameworks, and protocols can make or break your business.

  ...'
---

Par Joe Hanson

Lorsque vous construisez une application de chat de quelque nature que ce soit — des messages de groupe mobiles et du chat en jeu multijoueur, à l'assistance client et aux chatbots — choisir les bonnes plateformes, frameworks et protocoles peut faire ou défaire votre entreprise.

C'est parce que décider de construire ou d'acheter une application de chat n'est pas binaire. Les jours où il fallait choisir entre le faire soi-même ou acheter à un fournisseur sont révolus.

La question maintenant est **combien je veux construire, et combien je veux acheter ?**

Entre l'open-source, l'IaaS, le PaaS, le SaaS, les SDK, les API et les Microservices, les entreprises n'ont jamais eu autant d'options pour **comment** elles veulent construire leurs produits de chat. Et le spectre des choix ne cesse de s'élargir.

À mesure que le cloud computing devient plus accessible et abordable, de nouvelles entreprises innovantes résolvent des problèmes spécifiques. Les appareils deviennent plus puissants. Si les entreprises veulent suivre le rythme, elles doivent comprendre le paysage des fournisseurs ainsi que les avantages et les défis de chaque option le long du spectre.

En conséquence, il y a de nombreuses erreurs que les développeurs et les organisations peuvent commettre lors du choix des plateformes de chat ou de messagerie pour leur application.

Dans cet article, nous discuterons de plusieurs types d'applications de chat et examinerons les différentes options de plateformes pour alimenter et livrer des applications de messagerie. Nous discuterons également des défis qui peuvent survenir en prenant certaines décisions tout au long du cycle de développement, comme la scalabilité, le temps de mise sur le marché, et d'autres différenciateurs.

### Choix d'un fournisseur de services de chat : paysage actuel

Il existe une grande variété d'options le long du spectre construire vs. acheter. Vous avez l'open-source à une extrémité (construire) et des solutions entièrement construites (SaaS) à l'autre extrémité (acheter). Avec des centaines d'options entre les deux, toutes avec différents avantages et inconvénients, nous chercherons à vous donner une idée du paysage dans un simple tableau :

![Image](https://cdn-media-1.freecodecamp.org/images/CK4rkZuEt7Lgk9Qps1GC0cgZHUDcD3Mez5g9)

#### Protocoles open-source

Les protocoles open-source comme [WebSockets](https://www.pubnub.com/learn/glossary/what-is-websocket/) et [HTTP Long Polling](https://www.pubnub.com/blog/2014-12-01-http-long-polling/) sont les plus éloignés du côté construire. Ce sont simplement des protocoles, ce qui signifie que vous gérez tout pour les faire fonctionner. Cela inclut la mise en place de votre infrastructure back-end, sa maintenance, la construction de nouveaux SDK pour supporter de nouveaux appareils et langages, et tout le reste.

Ce sont de bonnes options pour le prototypage, la construction de petites applications, ou pour mettre les mains dans le cambouis avec la full stack. Mais la plupart des services de messagerie en temps réel offrent des versions gratuites avec toute l'infrastructure back-end incluse. Et vous devrez vous préparer à quelques sérieux maux de tête lorsque viendra le temps de scaler.

#### Frameworks open-source

Les frameworks open-source sont un peu plus avancés que le pur build, mais nécessitent toujours que vous mainteniez l'infrastructure par vous-même. Pour les cas d'utilisation de chat, les frameworks open-source tendent à s'appuyer sur une communauté de développeurs pour mettre à jour le framework et maintenir les SDK clients.

#### Infrastructure-as-a-Service (IaaS)

Ce sont les grands noms — les fournisseurs de services d'infrastructure cloud comme AWS, Digital Ocean, Azure, Bluemix, et Google Cloud. Ils finissent par alimenter beaucoup des fournisseurs de PaaS, de solutions de messagerie, et de produits SaaS dont nous parlerons ensuite.

En résumé, vous pouvez utiliser des protocoles open-source avec un IaaS pour lancer votre application. L'infrastructure est prise en charge, mais il reste encore beaucoup de construction à faire vous-même.

#### Platform-as-a-Service (PaaS)

Les fournisseurs de PaaS comme [PubNub](https://www.pubnub.com/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY17-Q4-Medium-November-13) et [Firebase](http://firebase.com) offrent des solutions hébergées pour construire des applications de chat. Ils incluent non seulement l'infrastructure, mais aussi les API pour construire des fonctionnalités de chat. La construction et la personnalisation de l'application nécessitent des ressources d'ingénierie, puisque leurs SDK sont ouverts. Mais la sécurité et la maintenance du service (le back-end et les SDK clients) sont gérées par le PaaS.

#### Frameworks de chat

Ces fournisseurs de frameworks sont presque aussi proches de l'achat que possible, mais nécessitent encore une quantité importante d'ingénierie. La grande différence entre ces fournisseurs et le PaaS est qu'ils offrent une approche plus boîte noire — vous avez moins de liberté pour personnaliser les API et l'infrastructure. Souvent, ils fourniront également l'UI.

PubNub [ChatEngine](https://www.pubnub.com/products/chatengine/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY17-Q4-Medium-November-13) offre un framework plus ouvert et extensible, par exemple. [Layer](http://layer.com) se rapprocherait davantage des solutions de chat SaaS en boîte noire, mais offre encore une quantité importante d'options de personnalisation.

#### SaaS

Enfin, le plus éloigné du côté acheter du spectre, les entreprises SaaS fournissent une solution entièrement construite qui nécessite une petite quantité d'ingénierie. L'UI, les intégrations et l'infrastructure sont toutes gérées par le fournisseur SaaS. Les leaders dans ce domaine incluent [Intercom](http://intercom.com) et [Zendesk Chat](https://www.zendesk.com/chat/).

### Questions à se poser lors du choix de votre fournisseur de services de chat

Comme pour toutes les autres parties de votre infrastructure critique, les questions clés restent les mêmes :

* Gérez-vous votre propre service, ou utilisez-vous un service hébergé ?
* Combien cela coûte-t-il au départ ? Combien cela coûtera-t-il éventuellement à grande échelle ?
* Le service hébergé est-il fiable, sécurisé et scalable ?
* À quel point le chat est-il critique pour votre application ?
* Qui dans votre équipe le maintiendra ? Ont-ils les compétences pour le rendre scalable et sécurisé ?
* Où le service stocke-t-il les données, et qui y a accès ?

### Choix de votre fournisseur de services de chat : open-source vs. hébergé

![Image](https://cdn-media-1.freecodecamp.org/images/wlIH8x-7iGHJAAnC41gubAULKS8xmbYcGUWf)

En matière de développement logiciel, tout le monde sait que ce qui fonctionne en laboratoire n'est pas garanti de fonctionner dans la nature. C'est parce que la nature présente tous ces défis auxquels vous ne pensez peut-être pas, ou que vous ne connaissez peut-être même pas encore.

Lorsque vous choisissez la bonne technologie pour alimenter votre chat, il y a un certain nombre de considérations de construction et d'achat à examiner. Nous examinerons la sécurité, la scalabilité, la fiabilité, la personnalisation et les raisons commerciales de sélectionner votre stack en laboratoire vs. le monde réel.

#### Infrastructure

Si vous optez pour la voie open-source, vous choisirez votre outil, l'installerez et orchestrez l'opération de cet outil.

À partir de là, vous commencerez à penser à l'aspect infrastructure, comme l'équilibrage de charge et les nœuds redondants. Ce sont des exigences pour lancer une application à grande échelle. C'est à ce moment-là que vous pourriez faire appel à un fournisseur IaaS pour gérer le back-end. Même ainsi, cela nécessitera encore beaucoup d'ingénierie, y compris :

* Mise en place de plusieurs environnements de test, de staging et de production
* Twelve factor
* Coordination de l'approvisionnement pour ces multiples environnements (comme un Kubernetes)
* Déploiement de votre code d'application dans les environnements
* Configuration de la gestion des services, de la surveillance du système et des alertes Ops
* Création d'un schéma d'équilibrage de charge (comme Nginx ou HAProxy)
* Détermination de la manière de segmenter les données par canaux ou sujets (comme Redis [pub/sub](https://www.pubnub.com/learn/glossary/what-is-publish-subscribe/) avec [Socket.io](https://www.pubnub.com/learn/glossary/what-is-socketio/))
* Trouver une solution de stockage et de transmission pour la récupération des signaux, comme la mise en cache en mémoire
* Implémentation d'une méthode pour détecter quel client se connecter à quel centre de données et port
* Détermination des canaux/sujets à envoyer/recevoir pour un client donné
* Décision des plateformes et langages que vous supporterez
* Création d'une sérialisation de données universelle (JSON)
* Personnalisation du code pour détecter la liaison montante des données qui fonctionne sur différents types d'appareils
* Détermination de la Qualité de Service et du niveau de perte, et développement d'un schéma de récupération des données (ou se contenter de "tirer et oublier")
* Décision des API et capacités dont vous aurez besoin, puis leur construction (détection de présence)

C'est une longue liste de considérations. Mais si vous choisissez la voie open-source, ce sont les choses que vous devrez considérer une fois que vous serez hors du laboratoire et que vous scalerez votre application.

#### Sécurité

Pour le chat, la sécurité est primordiale. Nous envoyons de plus en plus d'informations confidentielles et critiques via les applications de chat, des détails financiers aux commandes de chatbots. Il est impératif de s'assurer que vous avez un contrôle total sur l'accès et le chiffrement.

![Image](https://cdn-media-1.freecodecamp.org/images/Wv4inXHHv4uDY1s3ln3qNALO0zNVYKgedoOJ)

Chaque fournisseur de services de chat réussi offre différents niveaux de sécurité. Voici les fonctionnalités les plus importantes qui doivent être incluses dans tout fournisseur de services hébergés :

* Chiffrement de bout en bout avec TLS pour les paquets entrants/sortants et AES pour les paquets
* Support du contrôle d'accès basé sur des tokens. Le contrôle d'accès basé sur des tokens vous permet d'accorder et de révoquer l'accès à tout canal de messagerie.
* La conformité est clé, surtout pour les applications de chat verticalisées. Le fournisseur de services hébergés doit être certifié pour HIPAA (santé), SOC 2, GDPR (UE), Data Shield, et SafeHarbor (UE/US).

Pour ceux qui choisissent de ne pas utiliser un fournisseur de services hébergés, voici des considérations de sécurité supplémentaires que vous devrez gérer par vous-même :

* Achat d'un certificat TLS, puis distribution et gestion sécurisée de ce certificat
* Détermination de la manière de protéger les canaux et les sujets (non couverts par TLS)
* Construction d'un système d'autorisation pour les utilisateurs
* Considération du chiffrement AES et/ou RSA pour les payloads (non couverts par TLS)
* Conformité avec les politiques de sécurité législatives (comme SafeHarbor ou HIPAA)

#### Scalabilité

Pour les applications de chat avec des milliers d'utilisateurs actifs discutant simultanément, et celles qui continuent de croître, l'expertise en matière de scalabilité est un défi majeur. Les solutions open-source et certains fournisseurs de services hébergés traitent de cela. Mais en matière de scalabilité, les solutions hébergées atténuent le risque de problèmes de scalabilité pouvant briser l'application bien plus que les options open-source.

Pour les solutions hébergées, il existe quelques indicateurs que votre service de choix évoluera avec la croissance de votre application.

**Plusieurs points de présence mondiaux :** Les messages de chat doivent être répliqués mondialement, de sorte que si des messages sont perdus, un message de sauvegarde sera livré. Cela augmente également les performances de votre application, car chaque utilisateur de chat n'a pas à se connecter au même centre de données (surtout ceux à mi-chemin autour de la terre).

**SLAs de disponibilité :** Les SLAs de disponibilité rendent les fournisseurs de services hébergés responsables, et ils devraient vous créditer si ces SLAs ne sont pas respectés selon les termes.

Pour les bricoleurs, vous devez considérer :

* Un service de test de charge personnalisé qui peut simuler un public réaliste
* Création d'un protocole de mise à jour et modification continue de votre réseau pour supporter de nouveaux produits/services
* Paiement des coûts du serveur Socket, des systèmes QA, et des basculements à chaud
* Surveillance continue des Ops et personnel supplémentaire requis

#### Fiabilité

Il y a tellement de concurrence pour les applications de messagerie. Avec le magasin d'applications à un clic, tout problème rencontré par un utilisateur peut le conduire vers une alternative. La fiabilité est un facteur clé pour rendre votre application attrayante. Lors de l'évaluation des fournisseurs de services hébergés, voici quelques indicateurs clés de fiabilité :

* Réplication des données pour plusieurs points de présence et basculement automatique pour garantir que les messages sont livrés 100 % du temps (et en fait en temps réel)
* "Rattrapage" des messages en cas de coupure de connexion (si un utilisateur est dans un tunnel, par exemple, il recevra le message lorsqu'il en sortira de l'autre côté)

Si vous utilisez une solution open-source, vous devrez également gérer :

* Construction d'un système de distribution de charge
* Identification des messages d'erreur
* Construction d'un système de journalisation
* Savoir quand des défauts se produisent et développer un manuel de réponses
* Construction de la gestion des services (comme PagerDuty)
* Développement du déploiement multi-centres de données

### Open-source vs. hébergé

Lorsque vous examinez les principales considérations, vous pouvez voir que la construction d'un système de messagerie en temps réel par vous-même comporte de nombreux risques. C'est une bonne option pour les petites applications de chat. Mais une fois que vous commencez à croître, les défis de sécurité, de fiabilité et de scalabilité peuvent s'accumuler.

La plupart des fournisseurs de solutions hébergées permettent également un niveau de prix sandbox gratuit pour toujours. Cela vous permet de développer votre application sans payer, et une fois que vous avez atteint une certaine taille, vous payez au fur et à mesure que vous grandissez. Pour les entreprises qui cherchent à avancer rapidement et qui ne veulent pas se soucier de toutes les intrications du réseau et de l'infrastructure, les solutions hébergées sont la voie à suivre.

Si vous avez aimé cet article, veuillez lui donner un applaudissement pour que plus de gens le voient. Merci !

![Image](https://cdn-media-1.freecodecamp.org/images/b7KM4qLu5aocD1qZCdoJ-mDUz0gTEaMPPQrD)
_[Téléchargez l'eBook ici !](https://www.pubnub.com/learn/ebooks/chat-is-more-than-hot-air/?utm_source=Syndication&amp;utm_medium=Medium&amp;utm_campaign=SYN-CY18-Q2-Medium-June-7&amp;utm_content=bvb-freecodecamp" rel="noopener" target="_blank" title=")_

Si vous cherchez une analyse approfondie du chat, ne cherchez pas plus loin que notre nouvel eBook : [**Le chat est plus que du vent chaud — Comment construire le futur numérique**](https://www.pubnub.com/learn/ebooks/chat-is-more-than-hot-air/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-7&utm_content=bvb-freecodecamp)**. Dans cet eBook, nous couvrons :

* **Le paysage actuel de la technologie de chat :** les différentes saveurs de chat, choisir la bonne technologie parmi ce qui est disponible sur le marché aujourd'hui et une comparaison entre construire vs. acheter et hébergé vs. open source.
* **Comment le chat évolue :** un aperçu de la manière dont les applications de chat changent de la simple messagerie pour transformer la façon dont les industries et les utilisateurs communiquent.
* **Comment s'assurer d'être à l'avant-garde de l'innovation :** un regard sur les fonctionnalités et expériences qui peuvent être livrées pour se démarquer du reste.

_Publié à l'origine sur [www.pubnub.com](https://www.pubnub.com/blog/building-chat-the-current-landscape/)._