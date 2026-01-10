---
title: Apprenez les principes clés du System Design derrière les plateformes à fort
  trafic comme le gaming et la recherche d'emploi
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2025-08-20T16:34:29.819Z'
originalURL: https://freecodecamp.org/news/learn-key-system-design-principles-behind-high-traffic-platforms-like-gaming-and-job-discovery
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755707525928/f4a02c14-fe62-4d6f-9afc-d887d45a98d4.png
tags:
- name: System Design
  slug: system-design
- name: System Architecture
  slug: system-architecture
- name: full stack
  slug: full-stack
seo_title: Apprenez les principes clés du System Design derrière les plateformes à
  fort trafic comme le gaming et la recherche d'emploi
seo_desc: 'Over the last three months, life has had me juggling a lot – managing my
  marriage, taking care of family health issues, and overseeing new construction work
  at home. Somehow, I got through it all. But looking back, I realised something important:
  I c...'
---

Au cours des trois derniers mois, la vie m'a obligé à jongler avec beaucoup de choses – gérer mon mariage, m'occuper de problèmes de santé familiaux et superviser de nouveaux travaux de construction à la maison. D'une manière ou d'une autre, j'ai réussi à tout surmonter. Mais avec le recul, j'ai réalisé quelque chose d'important : j'aurais pu bien mieux gérer la situation si j'avais eu un *système* en place.

Pour moi, un **système** signifie un ensemble de règles, de processus et de déclencheurs qui guident l'ensemble du flux de travail. Cela vous aide à économiser votre énergie et à ne pas avoir à improviser sur le moment. Cela permet de rester productif, efficace et cohérent.

Maintenant que le chaos s'est apaisé, j'ai beaucoup réfléchi aux systèmes – pas seulement dans la vie, mais aussi dans la tech. J'aurais aimé appliquer ces mêmes principes de **System Design** plus tôt.

Dans cet article, nous allons explorer des exemples concrets de System Design provenant de domaines tels que le gaming et les plateformes d'emploi. Ces industries ne se contentent pas de passer à l'échelle de manière massive ; elles exigent également une haute disponibilité, une faible latence et une expérience client fluide. Comprendre comment elles sont construites est un moyen puissant de monter en compétence en tant que développeur ou architecte.

### Ce que nous allons couvrir

1. [Introduction : Qu'est-ce que le System Design et pourquoi le passage à l'échelle est important](#heading-introduction-quest-ce-que-le-system-design-et-pourquoi-le-passage-a-lechelle-est-important)
    
2. [Approches du System Design](#heading-approches-de-la-conception-de-systemes)
    
    * [1\. L'approche Bottom-Up](#heading-1-approche-bottom-up)
        
    * [2\. L'approche Top-Down](#heading-2-approche-top-down)
        
    * [3\. Conception hybride](#heading-3-conception-hybride)
        
3. [Concepts importants en System Design](#heading-concepts-importants-en-system-design)
    
    * [Composants d'une application web Full Stack](#heading-composants-dune-application-web-full-stack)
        
    * [Comment les ordinateurs communiquent entre eux (L'Internet)](#heading-comment-les-ordinateurs-communiquent-entre-eux-linternet)
        
    * [Le problème de la croissance](#heading-le-probleme-de-la-croissance)
        
    * [Accélérer votre site web avec la mise en cache et les CDN](#heading-accelerer-votre-site-web-avec-le-cache-et-les-cdn)
        
    * [Construire votre application : Monolithe vs Microservices](#heading-construire-votre-application-monolithe-vs-microservices)
        
    * [Les APIs](#heading-les-apis)
        
    * [Gestion des données en temps réel](#heading-gestion-des-donnees-en-temps-reel)
        
    * [Bases de données](#heading-bases-de-donnees)
        
    * [Comprendre le théorème CAP](#heading-comprendre-le-theoreme-cap)
        
    * [Limitation de débit (Rate Limiting) et Monitoring](#heading-limitation-de-debit-et-monitoring)
        
4. [Études de cas : Le passage à l'échelle dans le monde réel](#heading-etudes-de-cas-le-passage-a-lechelle-dans-le-monde-reel)
    
    * [Étude de cas 1 : Mise à l'échelle d'une application de recherche d'emploi](#heading-etude-de-cas-1-mise-a-lechelle-dune-application-de-recherche-demploi)
        
    * [Étude de cas 2 : Mise à l'échelle d'une application de jeu en ligne](#heading-etude-de-cas-2-mise-a-lechelle-dune-application-de-jeu-en-ligne)
        
5. [Q&A](#heading-questions-reponses)
    
6. [Notes finales](#heading-notes-finales)
    
7. [Conclusion](#heading-conclusion)
    

## Introduction : Qu'est-ce que le System Design et pourquoi le passage à l'échelle est important

Le **System Design** est le processus de définition de l'architecture, des modules, des interfaces et des données d'un système.

En d'autres termes, concevoir un système signifie expliquer ses différentes parties, comme sa structure, ses briques de base (modules) et ses composants.

C'est un processus utilisé pour définir, développer et concevoir un système de manière à répondre aux besoins spécifiques d'une entreprise ou d'une organisation.

L'objectif principal du System Design est de fournir suffisamment d'informations et de détails sur le système, et d'implémenter correctement ses parties à l'aide de modèles et de vues. Parlons maintenant des différentes parties d'un système.

### Éléments d'un système :

* **Architecture :** Il s'agit d'une structure ou d'un modèle de base qui montre comment le système fonctionne, à quoi il ressemble et comment il se comporte. Nous utilisons souvent des **organigrammes** (flowcharts) pour expliquer et représenter cette architecture.
    
* **Modules :** Ce sont des parties ou sections plus petites du système. Chaque module gère une tâche spécifique. Lorsque tous les modules sont combinés, ils forment le système complet.
    
* **Composants :** Ils fournissent une fonction spécifique ou un groupe de fonctions liées. Les composants sont généralement constitués d'un ou plusieurs modules.
    
* **Interfaces :** C'est le point de connexion où les différentes parties (composants) du système échangent des informations entre elles.
    
* **Données :** Cela fait référence à la gestion de l'information et à la manière dont elle circule dans le système.
    

### Pourquoi le System Design est important

Le System Design est important pour plusieurs raisons pratiques. Premièrement, il peut aider les entreprises et les équipes à résoudre des problèmes commerciaux complexes et à s'assurer qu'elles analysent minutieusement toutes les exigences avant la construction. Il réduit également le risque d'introduire des erreurs dans les processus tout en rendant les phases de conception plus efficaces et structurées. Enfin, il vous aide à collecter et à présenter efficacement vos données dans un format utile et améliore la qualité globale du système.

## Approches du System Design

Il existe plusieurs méthodes que vous pouvez utiliser pour aborder la conception de systèmes. Les principales sont :

### 1\. L'approche Bottom-Up (Ascendante)

Dans cette méthode, la conception commence par les composants ou sous-systèmes de plus bas niveau. Ces petites parties sont progressivement combinées pour former des composants de plus haut niveau. Ce processus se poursuit jusqu'à ce que le système entier soit construit comme une structure complète.

Plus nous utilisons d'abstraction, plus le niveau de conception devient élevé.

**Avantages :**

* Les composants peuvent être réutilisés dans d'autres systèmes.
    
* Il est plus facile d'identifier les risques tôt.
    
* Cela aide à masquer les détails techniques de bas niveau et peut être combiné avec l'approche top-down.
    

**Désavantages :**

* L'approche n'est pas très centrée sur la structure globale du problème.
    
* Construire des solutions bottom-up de haute qualité est difficile et prend du temps.
    

### 2\. L'approche Top-Down (Descendante)

Ici, la conception part du système complet, et vous le décomposez en sous-systèmes et composants plus petits au fur et à mesure. Chacun de ces sous-systèmes est ensuite décomposé davantage, étape par étape, créant une structure hiérarchique.

En termes simples, vous commencez par la vue d'ensemble et continuez à la diviser jusqu'à atteindre les plus petites parties du système.

En résumé, la conception commence par la définition de l'ensemble du système, puis se poursuit par la définition de ses sous-systèmes et composants. Lorsque toutes les définitions sont prêtes et s'emboîtent, le système est complet.

**Avantages** :

* L'accent est mis sur la compréhension des besoins en premier, ce qui conduit à une conception réactive et orientée vers l'objectif.
    
* Il est plus facile de gérer les erreurs dans les interfaces entre les composants.
    

**Désavantages** :

* Les composants ne peuvent pas être réutilisés facilement dans d'autres systèmes.
    
* L'architecture qui en résulte est souvent moins flexible ou moins propre.
    

### 3\. Conception hybride

L'approche de conception hybride est un mélange des méthodes **top-down** et **bottom-up**. Au lieu de s'engager dans une seule voie, elle tire parti des forces des deux. Vous commencez par examiner le système global (comme dans le top-down) afin de ne pas perdre de vue l'ensemble. En même temps, vous vous concentrez également sur la construction de modules ou de composants solides et réutilisables (comme dans le bottom-up).

En termes simples, vous planifiez d'abord la vue d'ensemble, puis vous créez des composants plus petits qui peuvent fonctionner de manière indépendante, et enfin vous combinez le tout en un système cohérent.

Par exemple, pour notre site d'équipe sportive, nous utiliserions le top-down pour définir l'ensemble du parcours du fan (page d'accueil → détails du match → scores en direct). Mais en bottom-up, nous construirions des composants modulaires comme l'authentification ou le suivi des statistiques, qui pourront plus tard être réutilisés dans de nouvelles fonctionnalités comme la réservation de billets ou la vente de produits dérivés.

**Avantages :**

* Vous bénéficiez de la clarté d'un plan top-down tout en construisant des modules réutilisables.
    
* Elle établit un équilibre entre la conception de haut niveau et l'implémentation détaillée.
    
* Les risques sont plus faciles à gérer puisque vous considérez à la fois la structure et les composants.
    

**Désavantages :**

* Sa gestion peut être complexe car vous jonglez avec deux approches.
    
* Nécessite plus de coordination entre les équipes travaillant à différents niveaux.
    
* Cela peut prendre plus de temps par rapport à l'utilisation d'une seule approche.
    

## Concepts importants en System Design

Avant d'explorer les composants de base, je veux que vous compreniez d'abord deux concepts clés :

* Les composants d'une application web Full Stack
    
* Comment les ordinateurs communiquent entre eux (via Internet)
    

### Composants d'une application web Full Stack

Une application web Full Stack est une application logicielle qui combine à la fois le frontend (ce que les utilisateurs voient et avec quoi ils interagissent) et le backend (le serveur, la base de données et la logique qui alimentent l'application) en un seul système complet.

Généralement, les sites web simples ne nécessitent pas beaucoup de System Design – et dans certains cas, aucun. Mais lorsqu'il s'agit d'applications virales ou de plateformes offrant des services complexes, le System Design devient essentiel. La plupart des applications modernes sont des applications Full Stack, ce qui signifie qu'elles impliquent plusieurs couches interconnectées travaillant ensemble.

Voici un aperçu simplifié d'une application Full Stack typique :

![aperçu full stack web](https://cdn.hashnode.com/res/hashnode/image/upload/v1755603745131/1114a65f-ea7c-4e3f-aca6-4821c8ca683a.png align="left")

Avant de plonger dans chacun de ces composants, laissez-moi d'abord vous donner un aperçu rapide et général de ce qu'ils sont et de la manière dont ils s'intègrent dans l'ensemble (en partant du bas de l'image ci-dessus).

* **Frontend** – L'interface utilisateur où les gens interagissent avec votre application.
    
* **Backend** – La logique et le cerveau de l'application qui traite les requêtes.
    
* **APIs** – Le pont qui permet la communication entre le frontend, le backend et les services externes.
    
* **Database** (Base de données) – Le système de stockage où vivent toutes vos informations structurées.
    
* **Server** (Serveur) – L'infrastructure qui héberge, exécute et livre votre application.
    

Maintenant, nous devons comprendre comment les ordinateurs communiquent entre eux.

### Comment les ordinateurs communiquent entre eux (L'Internet)

Lorsque vous tapez l'URL d'un site web dans le navigateur – qu'il s'agisse d'un simple site portfolio ou d'une application Full Stack – comment votre ordinateur sait-il où envoyer la requête ? Il utilise le [**Domain Name System**](https://www.freecodecamp.org/news/what-is-dns/) **(DNS)**. Le DNS est comme un annuaire téléphonique pour Internet – il traduit un nom de site web lisible par l'homme, comme « example.com », en une adresse IP numérique unique que les ordinateurs peuvent comprendre.

Une fois que votre ordinateur a l'adresse IP, il utilise des **protocoles de communication** pour envoyer et recevoir des données. L'un des protocoles les plus importants est le [**TCP**](https://www.freecodecamp.org/news/tcp-vs-udp/). Il décompose les données en petits paquets numérotés. Si un paquet est perdu ou arrive dans le désordre, le TCP s'assure qu'il est renvoyé et réassemblé correctement, ce qui en fait un moyen très fiable d'envoyer des données.

Au-dessus du TCP, nous utilisons des protocoles de plus haut niveau comme l' [**HTTP**](https://www.freecodecamp.org/news/what-is-http/). Il s'agit d'un protocole de couche application plus facile à utiliser pour les développeurs. C'est le langage que votre navigateur parle au serveur.

**HTTPS** est identique, mais il ajoute une couche de cryptage supplémentaire pour la sécurité.

Maintenant que nous comprenons les bases d'Internet, n'oubliez pas qu'il sert des milliards de personnes dans le monde.

Prenons un exemple concret. Imaginez que vous possédez un restaurant d'une capacité de 50 personnes. Un jour, 10 clients supplémentaires arrivent – avec quelques ajustements, vous gérez la situation. Mais soudain, mille personnes de plus se présentent à votre porte. Que feriez-vous alors ? Il ne s'agit plus seulement d'ajouter des chaises et des tables : vous aurez besoin de plus de nourriture, de plus de personnel et d'une installation plus grande pour gérer un tel trafic.

Cet exemple simple reflète le défi réel de la croissance et du passage à l'échelle (scalability). Et c'est exactement ce que je vais aborder dans le prochain chapitre de ce tutoriel.

### Le problème de la croissance

Imaginez que vous avez construit un site web simple pour une équipe sportive locale. Au début, vous n'êtes que vous et quelques amis à l'utiliser, donc un seul serveur suffit. Ce serveur contient toute la logique du site et se connecte à une base de données unique où sont stockées les statistiques des joueurs.

Cependant, à mesure que l'équipe gagne en popularité, de plus en plus de personnes visitent votre site, et celui-ci devient soudainement lent. Il s'agit d'un **problème de mise à l'échelle**. Votre système ne peut pas gérer tout ce nouveau trafic.

#### Mettre votre système à l'échelle : deux méthodes principales

Il y a deux façons de résoudre ce problème. La première est la **mise à l'échelle verticale** (vertical scaling). C'est comme donner à votre serveur unique un moteur plus puissant et plus de mémoire. Vous mettriez à niveau le processeur (CPU) ou ajouteriez plus de RAM (mémoire temporaire). Vous pourriez également utiliser un stockage disque plus rapide comme un SSD.

Le problème est que vous ne pouvez améliorer votre matériel que jusqu'à une certaine limite. De plus, si ce serveur unique tombe en panne, tout votre site web devient inaccessible.

Une meilleure approche est la **mise à l'échelle horizontale** (horizontal scaling). Cela signifie ajouter plus de serveurs au lieu de simplement en améliorer un. Vous disposez désormais d'une équipe de serveurs, et chacun peut gérer une partie des requêtes entrantes des utilisateurs.

Cette approche permet une croissance quasi illimitée. Elle crée également une redondance et une tolérance aux pannes, car si un serveur tombe en panne, les autres peuvent prendre le relais, et votre site reste en ligne.

#### Diriger le trafic avec un Load Balancer

Avec plusieurs serveurs, vous avez besoin d'un moyen de vous assurer qu'aucun serveur n'est submergé. C'est là qu'intervient un **équilibreur de charge** (load balancer). Il agit comme un agent de circulation, se plaçant devant vos serveurs et dirigeant chaque nouvelle requête vers le serveur le mieux adapté. Il utilise différents algorithmes pour décider où envoyer le trafic.

Par exemple, la méthode **Round Robin** envoie les requêtes aux serveurs un par un, de manière cyclique. Une autre méthode est celle de la **Moindre Connexion** (Least Connection), qui envoie la requête au serveur qui possède le moins de connexions actives.

### Accélérer votre site web avec la mise en cache et les CDN

Imaginez que votre site web est maintenant utilisé par des personnes du monde entier. Un utilisateur situé dans un autre pays peut subir des temps de chargement lents parce que sa requête doit voyager jusqu'à vos serveurs.

Pour corriger cela, vous pouvez utiliser un [**Content Delivery Network (CDN)**](https://www.freecodecamp.org/news/how-cdns-improve-performance-in-front-end-projects/). Un CDN est un réseau de serveurs répartis dans le monde entier qui stockent des copies des fichiers statiques de votre site web, comme des images, des vidéos et des fichiers texte. Lorsqu'un utilisateur demande l'un de ces fichiers, le CDN le sert depuis le serveur le plus proche, ce qui accélère considérablement le chargement du site.

Ce processus est une forme de **mise en cache**. Le caching est l'idée générale de faire des copies de données et de les stocker dans un emplacement plus rapide d'accès. Vous pouvez mettre en cache des données sur votre serveur afin qu'il n'ait pas besoin de récupérer les mêmes statistiques de joueurs dans la base de données à chaque fois. Cela réduit la charge sur votre base de données et accélère l'ensemble de l'application.

Vous pouvez en savoir plus sur la [différence entre les CDN et la mise en cache ici](https://www.freecodecamp.org/news/caching-vs-content-delivery-network/).

### Construire votre application : Monolithe vs Microservices

À mesure que votre site web se développe, son code peut devenir un fouillis inextricable. Vous pourriez commencer par un **monolithe**, où toutes les fonctionnalités (comme les statistiques des joueurs et les scores en direct, dans notre exemple) sont intégrées dans un seul et même programme. [Un monolithe est plus facile pour débuter](https://www.freecodecamp.org/news/microservices-vs-monoliths-explained/), mais il peut être difficile à gérer et à mettre à jour.

Une meilleure approche pour une application à grande échelle consiste à utiliser une [**architecture de microservices**](https://www.freecodecamp.org/news/the-microservices-book-build-and-manage-services-in-the-cloud/). Cela signifie diviser votre application en services plus petits et indépendants, chacun ayant une tâche spécifique. Par exemple, un service pourrait gérer les statistiques des joueurs et un autre les scores en direct. Cela rend votre code plus organisé et plus facile à mettre à jour, car une modification dans un service n'affectera pas les autres.

Avec les microservices, vous avez besoin d'une [**API Gateway**](https://www.freecodecamp.org/news/what-are-api-gateways/). Elle agit comme un point d'entrée unique pour toutes les requêtes des utilisateurs, les dirigeant vers le bon microservice en coulisses. Elle gère également la sécurité et d'autres tâches courantes.

### Les APIs

Considérez les **APIs (Application Programming Interfaces)** comme les « intermédiaires » qui permettent à différents logiciels de communiquer entre eux.

En termes simples, une API est comme un serveur dans un restaurant. Vous (l'utilisateur) dites au serveur ce que vous voulez, le serveur apporte votre commande à la cuisine (le système), puis vous rapporte la nourriture (les données ou le résultat).

Sans APIs, votre application, site web ou logiciel ne saurait pas comment demander des informations ou des services à un autre système.

Par exemple, sur notre site web d'équipe sportive :

* Le front-end (ce que voient les fans) utilise une API pour **récupérer les statistiques des joueurs** depuis la base de données.
    
* Lorsque quelqu'un achète des billets de match, l'API communique avec le **système de paiement** pour confirmer la transaction.
    
* Si les fans veulent des mises à jour des scores en direct, l'API s'assure que les données en temps réel circulent de manière fluide du serveur vers leur écran.
    

Ainsi, les APIs sont importantes pour le System Design car elles déterminent l'efficacité avec laquelle les différents systèmes se connectent, partagent des données et restent fiables dans des conditions d'utilisation réelles.

Vos services front-end et back-end peuvent communiquer de plusieurs manières. La plus courante est une [**API REST**](https://www.freecodecamp.org/news/what-is-a-rest-api/). Il s'agit d'un ensemble de règles standardisées qui utilisent le protocole HTTP pour créer un moyen cohérent de communication entre un client et un serveur. Par exemple, elle définit une manière standard de signaler une requête réussie (« OK ») ou une erreur de serveur (« Internal Server Error »).

#### Quand utiliser REST

* Idéal quand : vous avez besoin de simplicité, d'une adoption large et d'une intégration facile avec les navigateurs, les applications mobiles ou les services tiers.
    
* Exemple : Applications CRUD (plateformes de blogs, sites de e-commerce, gestion des utilisateurs).
    
* Points forts : JSON lisible par l'homme, sans état (stateless), largement supporté.
    
* Points faibles : Over-fetching (récupérer plus de données que nécessaire) ou under-fetching (pas assez de données).
    

Un autre style est [**GraphQL**](https://www.freecodecamp.org/news/building-consuming-and-documenting-a-graphql-api/). Au lieu de recevoir toutes les données fournies par une API REST, GraphQL permet au client de demander uniquement les données spécifiques dont il a besoin, ce qui peut rendre les choses plus rapides et plus efficaces.

#### Quand utiliser GraphQL

* Idéal quand : les clients (comme les applications mobiles) ont besoin d'un contrôle précis sur les données qu'ils récupèrent.
    
* Exemple : flux de réseaux sociaux, tableaux de bord avec de nombreux widgets, applications mobiles avec une bande passante limitée.
    
* Points forts : requêtes flexibles, réduit l'over-fetching, système de typage fort.
    
* Points faibles : configuration du serveur plus complexe, ce qui peut entraîner des problèmes de performance si les requêtes ne sont pas optimisées.
    

Pour la communication de serveur à serveur, [**gRPC**](https://www.freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture/) est souvent utilisé. Il est réputé pour être très rapide car il utilise un format de données plus efficace appelé Protocol Buffers au lieu du JSON.

#### Quand utiliser gRPC

* Idéal quand : les services communiquent entre eux dans des architectures de microservices, et que la vitesse/l'efficacité est critique.
    
* Exemple : systèmes en temps réel (streaming, paiements, IoT, inférence d'apprentissage automatique).
    
* Points forts : super rapide (Protocol Buffers binaire), support natif du streaming, contrats forts.
    
* Points faibles : pas natif pour les navigateurs (nécessite des outils supplémentaires pour le web), débogage plus difficile par rapport à REST.
    

Pour résumer, d'après mes observations sur mes projets passés :

* Si vous construisez quelque chose **destiné au public et largement consommé** → optez pour REST.
    
* Si votre application comporte des **requêtes complexes et dynamiques de la part des clients** → optez pour GraphQL.
    
* Si vous traitez des **appels internes de service à service haute performance** → optez pour gRPC.
    

En System Design, choisir le bon style d'API affecte directement les performances, l'évolutivité et l'expérience utilisateur. Que vous choisissiez REST pour sa simplicité, GraphQL pour sa flexibilité ou gRPC pour sa vitesse, vous déterminez la capacité de votre système à croître et à s'adapter à l'évolution des demandes réelles.

### Gestion des données en temps réel

La gestion des données en temps réel est un défi car elle nécessite de maintenir une connexion active pour transmettre et recevoir des données en continu et simultanément. Les serveurs traditionnels suivent un modèle requête-réponse, où les données ne sont envoyées que lorsqu'elles sont explicitement demandées.

C'est là que les [**WebSockets**](https://www.freecodecamp.org/news/learn-websockets-socket-io/) interviennent. Contrairement au HTTP, qui est un modèle de requête et réponse ponctuel, un WebSocket crée une connexion bidirectionnelle continue entre le client et le serveur. Cela permet au serveur d'envoyer des mises à jour à l'utilisateur dès qu'elles se produisent, créant ainsi une expérience en temps réel.

Lorsque les microservices ont besoin de communiquer sans être directement connectés, ils peuvent utiliser des [**files d'attente de messages**](https://www.freecodecamp.org/news/how-message-queues-make-distributed-systems-more-reliable/) (message queues). Un service envoie un message à la file d'attente, et un autre service le récupère lorsqu'il est prêt. Cela aide à découpler les services, afin qu'ils n'aient pas à se soucier de la disponibilité de l'autre service à ce moment précis.

Sur notre site de sport, les WebSockets permettent aux fans de voir les scores en direct instantanément sans rafraîchir la page – tout comme dans les applications de chat, mais ici, cela maintient l'excitation du jeu en temps réel.

### Bases de données

Les bases de données sont un élément critique de toute application Full Stack car elles servent de résidence permanente aux données des utilisateurs. Une fois que vous avez décidé comment mettre à l'échelle vos serveurs et gérer la communication, vous devez également considérer la couche base de données. Si tout le reste s'adapte à l'échelle mais pas la base de données, celle-ci peut rapidement devenir un goulot d'étranglement – entraînant des pannes, des enregistrements incohérents ou même des pertes de données.

De nombreuses applications s'appuient sur des [**bases de données relationnelles (SQL)**](https://www.freecodecamp.org/news/learn-relational-database-basics-key-concepts-for-beginners/), qui stockent les données dans des tables structurées avec des lignes et des colonnes et sont excellentes pour gérer les informations structurées. Mais pour les applications nécessitant une grande flexibilité ou gérant d'énormes ensembles de données non structurées, on choisit souvent des [**bases de données NoSQL**](https://www.freecodecamp.org/news/learn-nosql-in-3-hours/) (comme MongoDB ou Cassandra). Ces bases de données ne suivent pas les règles strictes du SQL et sont plus adaptées à la gestion de quantités massives de données.

Elles suivent les [propriétés ACID](https://www.freecodecamp.org/news/acid-databases-explained/) :

* **Atomicité (Atomicity) :** Une transaction est tout ou rien.
    
* **Cohérence (Consistency) :** Les données restent toujours dans un état valide.
    
* **Isolation (Isolation) :** Plusieurs transactions n'interfèrent pas entre elles.
    
* **Durabilité (Durability) :** Une fois qu'une transaction est terminée, les données sont définitivement sauvegardées.
    

Tout comme pour les serveurs, vous pourriez avoir besoin de mettre à l'échelle votre base de données. Vous pouvez utiliser le **sharding** (fragmentation), qui divise vos données entre plusieurs bases de données, ou la **réplication**, qui crée des copies de votre base de données pour gérer davantage de requêtes de lecture.

### Comprendre le théorème CAP

Lorsque vous traitez un système distribué et plusieurs bases de données, vous êtes inévitablement confronté à des compromis. Le **théorème CAP** stipule que vous ne pouvez garantir que deux des trois propriétés suivantes en même temps :

* **Cohérence (Consistency)** – Chaque utilisateur voit les mêmes données, les plus à jour.
    
* **Disponibilité (Availability)** – Le système est toujours disponible pour répondre aux requêtes.
    
* **Tolérance au partitionnement (Partition Tolerance)** – Le système continue de fonctionner même si une partie du réseau tombe en panne.
    

Maintenant, du point de vue du System Design, ce théorème nous oblige à faire des choix architecturaux conscients. Par exemple, dans les applications financières (comme la banque), la cohérence est souvent prioritaire sur la disponibilité car même une petite incohérence dans les données de solde peut provoquer le chaos.

D'un autre côté, dans les flux de réseaux sociaux, la disponibilité et la tolérance au partitionnement sont souvent privilégiées – il n'est pas grave si vous voyez un message légèrement obsolète, mais le système ne doit jamais être hors service.

Dans le flux que nous avons discuté, chaque fois que nous introduisons un nouveau composant ou que nous nous étendons sur plusieurs régions, nous devons réévaluer quelles sont les deux garanties les plus importantes pour notre cas d'utilisation métier. Cette décision oriente directement le choix de la technologie de base de données, la conception des stratégies de basculement (failover) et les compromis acceptés dans l'expérience utilisateur.

En bref, le théorème CAP n'est pas seulement une théorie – c'est une boussole pratique. Il nous guide pour équilibrer les attentes des utilisateurs, les priorités de l'entreprise et la faisabilité technique sans casser les fonctionnalités existantes, tout en laissant de la place pour la croissance future.

### Limitation de débit (Rate Limiting) et Monitoring

Lors de la conception d'un système, il ne s'agit pas seulement de le faire *fonctionner* – il s'agit de le rendre résilient. Deux garde-fous essentiels ici sont le **rate limiting** et le **monitoring**.

#### Qu'est-ce que le Rate Limiting ?

La limitation de débit est la pratique consistant à contrôler le nombre de requêtes qu'un utilisateur, un client ou un service peut effectuer vers votre système dans un laps de temps donné. Par exemple, vous pourriez limiter une API à 100 appels par utilisateur et par heure. Cela prévient les abus, protège contre les tentatives de déni de service et garantit une utilisation équitable pour tous les consommateurs.

Le rate limiting entre en jeu dès que votre service est exposé publiquement ou en interne à plusieurs clients.

[Pour l'incorporer](https://www.freecodecamp.org/news/implement-api-rate-limiting-in-strapi/), vous pouvez implémenter des limites au niveau de l'API gateway, du reverse proxy (comme NGINX), ou au sein même de la logique de votre service. De nombreux fournisseurs de cloud (AWS API Gateway, GCP Endpoints) disposent également d'un support intégré.

#### Qu'est-ce que le Monitoring ?

Le [Monitoring](https://www.freecodecamp.org/news/the-front-end-monitoring-handbook/) (surveillance) est la pratique consistant à collecter des métriques, des logs et des traces de votre système pour comprendre son état de santé en temps réel. Les signaux typiques incluent :

* **Taux d'erreur** (par exemple, la fréquence d'échec des requêtes)
    
* **Latence** (combien de temps prennent les requêtes)
    
* **Volume de trafic** (charge sur l'ensemble du système)
    
* **Utilisation des ressources** (CPU, mémoire, disque, etc.)
    

Le monitoring est important dès le premier jour – c'est votre boucle de rétroaction. Sans lui, vous pilotez essentiellement à l'aveugle.

Pour l'intégrer à votre système, vous pouvez utiliser des piles d'observabilité comme [Prometheus + Grafana](https://www.freecodecamp.org/news/kubernetes-cluster-observability-with-prometheus-and-grafana-on-aws/), ou des solutions managées comme Datadog, New Relic ou CloudWatch. Vous pouvez également configurer des alertes en cas de dépassement de seuil (par exemple, un pic de 5 % du taux d'erreur).

En pratique, le rate limiting et le monitoring travaillent main dans la main. Le rate limiting protège proactivement contre la surcharge, tandis que le monitoring vous donne de la visibilité pour savoir si les limites fonctionnent, si une mise à l'échelle est nécessaire ou si un nouveau type de panne émerge.

Par exemple, si vous avez conçu un système de réservation (comme dans notre flux précédent), le rate limiting garantirait qu'un seul utilisateur ne peut pas spammer les réservations de sièges, tandis que le monitoring signalerait des anomalies telles que des pics inhabituels du volume de requêtes ou des augmentations soudaines de latence – vous aidant ainsi à agir avant que le système ne s'effondre.

#### Pourquoi cela est-il important pour le System Design ?

Ces sujets sont cruciaux pour un bon System Design car ils constituent les briques de base de la manière dont les applications modernes fonctionnent réellement dans le monde réel. La façon dont les systèmes communiquent, le type d'APIs que nous adoptons et la manière dont nous gérons les interactions en temps réel influencent directement le fait qu'un produit semble rapide, fiable et fluide – ou lent et frustrant. En résumé, ils déterminent la résistance de l'expérience globale lorsque de vrais utilisateurs la mettent à l'épreuve.

Lorsque nous développons une compréhension plus approfondie de la manière dont les ordinateurs communiquent, nous commençons à voir les mécanismes internes de l'architecture client-serveur – comment les APIs récupèrent les données des bases de données via des appels au système backend. À partir de cette base, nous pouvons pivoter vers des préoccupations de plus haut niveau :

* **Évolutivité et résilience** : Utiliser des équilibreurs de charge pour se protéger contre la surcharge des serveurs.
    
* **Sécurité** : Introduire le rate limiting pour atténuer les cyberattaques potentielles.
    
* **Efficacité** : Choisir le bon type d'appels API et exploiter la mise en cache/les CDN pour la vitesse et la réduction des frais généraux.
    
* **Fiabilité** : Implémenter la journalisation et le monitoring pour détecter les problèmes tôt et déboguer plus rapidement.
    

Ensemble, ces pratiques font passer un système du simple état de *fonctionnement* à celui de robuste, performant et prêt pour l'avenir.

Nous avons discuté des bases de tous les concepts les plus importants que vous devrez comprendre avant de construire un système de bout en bout. Il est maintenant temps de plonger dans les études de cas, où je vous montrerai comment différents types d'applications utilisent le System Design pour passer à l'échelle et servir des milliards d'utilisateurs.

J'ai choisi des services complexes à construire et qui gèrent plusieurs types de composants différents à la fois, comme les plateformes de jeu, d'éducation et de recherche d'emploi.

Décodons maintenant chacune d'entre elles ensemble, et j'expliquerai comment je mettrais l'application à l'échelle si j'étais le développeur qui la construisait.

## Études de cas : Le passage à l'échelle dans le monde réel

Le System Design se comprend mieux lorsqu'on le voit en action. Pour montrer comment des principes tels que la mise à l'échelle, la mise en cache, l'équilibrage de charge et la gestion des données en temps réel se rejoignent, examinons deux types d'applications très différents :

* Une **plateforme de recherche d'emploi** (axée sur les données structurées et la fiabilité).
    
* Une **plateforme de jeu en ligne** (axée sur la vitesse et la réactivité en temps réel).
    

L'examen des deux vous montrera que, bien que les outils et les concepts puissent être similaires, la façon dont nous les appliquons dépend du type de système que nous construisons.

Toutes deux sont des plateformes à fort trafic, mais avec des besoins totalement différents. Le portail d'emploi est une question de précision, de fiabilité et de flux de travail basés sur les données, tandis que la plateforme de jeu est une question de réactivité instantanée, d'équité et de portée mondiale.

Dans un portail d'emploi, un délai de 1 seconde signifie simplement attendre. Dans une application de jeu, un délai de 1 seconde pourrait signifier perdre le match. Les deux sont des échecs – mais pour des raisons complètement différentes et avec des conséquences différentes.

Ensemble, elles montrent comment les mêmes briques de System Design (scaling, caching, APIs, monitoring) sont appliquées différemment selon le contexte.

### Étude de cas 1 : Mise à l'échelle d'une application de recherche d'emploi

Une plateforme de recherche d'emploi est l'une des applications les plus utilisées de nos jours, car il y a toujours des gens qui cherchent du travail. Et il existe de nombreux portails d'emploi différents qui gèrent l'ensemble du processus, de la recherche d'emploi à l'intégration des utilisateurs.

Nous allons examiner un exemple de site appelé [Upstaff](https://upstaff.com/). C'est une plateforme qui se concentre sur l'embauche d'ingénieurs en IA comme service principal (bien qu'elle serve également d'autres profils de postes). À la base, elle gère des informations structurées – des choses comme les profils d'utilisateurs, les offres d'emploi et les candidatures.

Au premier jour, vous avez quelques centaines d'utilisateurs. Au centième jour, vous en avez peut-être des dizaines de milliers. Et dans un an ? Probablement des millions. Cette croissance signifie que vous devez penser à l'échelle, à la vitesse et à l'intégrité des données dès le départ.

#### 🔹 Les composants de base

* **Gestion des utilisateurs :** inscription, connexion et accès basé sur les rôles (chercheur d'emploi vs employeur).
    
* **Profils utilisateurs** : CV, compétences, préférences, stockés dans des bases de données structurées.
    
* **Affichage et listes d'emplois** : les employeurs créent des emplois, les chercheurs parcourent/recherchent/filtrent.
    
* **Suivi des candidatures** : le statut de candidature de chaque chercheur d'emploi doit être précis et à jour.
    
* **Moteur de recommandation** : emplois correspondant aux utilisateurs en fonction de l'historique et du profil.
    
* **Notifications** : alertes pour les nouvelles correspondances d'emploi, les réponses des recruteurs, les échéances.
    

Chacune de ces fonctionnalités dépend de la capacité du système à gérer de grandes quantités de données structurées – et à les gérer de manière fiable.

#### Étape 1 : Commencer petit

Au début, tout peut fonctionner sur un seul serveur avec une seule base de données. Cette configuration suffit pour quelques milliers d'utilisateurs.

#### Étape 2 : Croissance et pics de trafic

À mesure que de nouveaux utilisateurs arrivent, le serveur unique commence à ralentir. Pour corriger cela, nous ajoutons un équilibreur de charge et passons à une mise à l'échelle horizontale – en ajoutant plusieurs serveurs qui partagent le trafic.

#### Étape 3 : Défis de la base de données

Bientôt, la base de données devient le goulot d'étranglement. La recherche parmi des milliers d'emplois ralentit tout. Pour y remédier, nous :

* Utilisons le sharding (division de la base de données par ID utilisateur ou ID d'emploi).
    
* Ajoutons un cache (comme Redis) pour stocker les requêtes fréquentes telles que « Ingénieur logiciel à New York ».
    
* Utilisons un CDN pour livrer les logos, les photos de profil et d'autres fichiers statiques plus rapidement.
    

#### Étape 4 : Fonctionnalités lourdes

Les nouvelles fonctionnalités comme un analyseur de CV ou un moteur de recommandation nécessitent une puissance de calcul supplémentaire. Au lieu de surcharger l'application principale, nous les déplaçons vers des microservices séparés.

#### Étape 5 : Sécurité et fiabilité

Enfin, à mesure que le trafic augmente, nous ajoutons :

* **Rate limiting** pour empêcher tout utilisateur de spammer les APIs.
    
* **Monitoring** pour suivre les erreurs, la latence et l'activité des utilisateurs en temps réel.
    
* **API Gateway** pour s'assurer que toutes les requêtes sont sécurisées et validées. Voici un aperçu de l'ensemble de la mise à l'échelle du système en image :
    

![flowchart system design portail d'emploi](https://cdn.hashnode.com/res/hashnode/image/upload/v1754281195211/570680c1-2813-43b0-87a1-48a817ab6c9a.png align="left")

Cet exemple montre comment une planification minutieuse rend la croissance fluide. En passant à l'échelle horizontalement, en utilisant intelligemment le cache et en divisant les fonctionnalités lourdes en microservices, un portail d'emploi comme Upstaff peut gérer des millions d'utilisateurs sans s'effondrer.

### Étude de cas 2 : Mise à l'échelle d'une application de jeu en ligne

Changeons maintenant de perspective. Sur une plateforme de jeu comme [ce site](https://xn--ntcasinoutanlicens-ltb.com), la vitesse et la réactivité comptent plus que tout. Un délai de 1 seconde dans une recherche d'emploi est ennuyeux. Mais dans le gaming, un délai de 1 seconde peut faire partir les joueurs pour toujours. Contrairement aux portails d'emploi, le plus grand défi ici est la réactivité en temps réel. Un infime délai peut ruiner l'expérience utilisateur.

#### 🔹 Les composants de base

* **Service de gestion des utilisateurs** : comptes, profils et connexion.
    
* **Lobby de jeu et Matchmaking** : associer les joueurs par compétence, région et latence.
    
* **Gestionnaire de serveurs de jeu** : lancer et gérer des matchs en direct.
    
* **Communication en temps réel** : alimentée par WebSockets ou UDP pour une faible latence.
    
* **Magasin d'état du jeu (Redis)** : synchronisation rapide des points de vie, des scores et des positions.
    
* **Moteur de classement et de stats** : classements mondiaux, réalisations et progression.
    
* **Économie en jeu** : pièces, jetons, inventaire.
    
* **Passerelle de paiement** : abonnements et achats.
    
* **Couche de sécurité Anti-Cheat** : équité pour tous les joueurs.
    
* **Monitoring et Logging** : disponibilité des serveurs, latence et rapports de crash.
    

Contrairement à un portail d'emploi, chaque milliseconde compte.

#### Étape 1 : Commencer petit

Au début, un seul serveur puissant suffit pour exécuter à la fois la logique du jeu et les comptes utilisateurs. Avec seulement quelques joueurs, tout fonctionne parfaitement.

#### Étape 2 : Plus de joueurs, plus de problèmes

Lorsque des millions de joueurs se connectent, le serveur unique plante. Pour corriger cela, nous :

* Ajoutons un gestionnaire de serveurs de jeu qui lance des serveurs séparés pour chaque match.
    
* Introduisons un équilibreur de charge qui assigne les joueurs aux serveurs disponibles.
    

#### Étape 3 : Gestion des données en temps réel

Dans le gaming, la vitesse est primordiale. Au lieu du lent HTTP, nous passons aux WebSockets ou à l'UDP pour une communication instantanée. Pour garder la vue du jeu de chacun synchronisée :

* Utilisons des bases de données en mémoire comme Redis pour les positions, les scores et la santé.
    
* Mettons à jour les classements en temps quasi réel.
    

#### Étape 4 : Mise à l'échelle des fonctionnalités

D'autres services s'exécutent en parallèle :

* **Le service de matchmaking** associe les joueurs par compétence, emplacement et latence.
    
* **Le service d'économie** gère les pièces, les récompenses et les objets en jeu.
    
* **La passerelle de paiement** gère les abonnements et les achats de manière sécurisée.
    
* **Le système de notification** envoie des mises à jour comme « nouvel événement commence ».
    

#### Étape 5 : Expansion mondiale et sécurité

Lorsque le jeu se déploie dans le monde entier :

* Utilisons un CDN pour livrer les cartes et les skins rapidement à toutes les régions.
    
* Ajoutons une couche Anti-Cheat pour détecter et bloquer les tricheurs.
    
* Construisons un panneau d'administration et de monitoring pour suivre l'état de santé du système et le comportement des utilisateurs.
    

Dans le gaming, le System Design se concentre moins sur les données structurées et plus sur la faible latence, la communication en temps réel et l'équité. Passer à l'échelle ici signifie maintenir un gameplay fluide et sécurisé, même lorsque des millions de joueurs se connectent simultanément. Voici la représentation visuelle du System Design complet de la plateforme de jeu :

![flowchart system design site de jeu](https://cdn.hashnode.com/res/hashnode/image/upload/v1754287625776/546f3949-efa1-4a57-9906-ceb3f8a62f63.png align="left")

### Pourquoi ces deux études de cas sont-elles importantes ?

Vous pourriez vous demander – pourquoi montrer deux systèmes différents au lieu d'un seul ? La réponse est que le System Design n'est pas une solution universelle.

* Le portail d'emploi nous apprend à mettre à l'échelle des applications lourdes en données structurées où la fiabilité et la précision importent le plus.
    
* La plateforme de jeu nous montre comment concevoir pour la vitesse, la communication en temps réel et l'équité sous une charge extrême.
    

Ensemble, ces exemples prouvent que les mêmes principes de System Design que sont le scaling, le caching, le monitoring et les microservices s'appliquent partout. Ce qui change, c'est *comment vous les utilisez* pour résoudre les défis uniques de votre plateforme.

## Q&A

### **Comment débuter en System Design si on n'y comprend rien (pour l'instant) ?**

On me pose cette question tout le temps – et la première chose que vous devez savoir, c'est que le System Design n'est pas un domaine à part, réservé à une élite. C'est une *compétence supplémentaire* qui complète votre parcours de développement.

Si vous êtes un développeur Full Stack (ou si vous aspirez à le devenir), apprendre le System Design vous donne un avantage considérable. Après tout, construire une application ne consiste pas seulement à la faire fonctionner – il s'agit de la faire *bien fonctionner* à grande échelle.

Donc, si vous débutez et que vous ne savez même pas encore comment devenir développeur Full Stack, commencez par là. Apprenez d'abord à construire des applications, et le System Design commencera alors à avoir beaucoup plus de sens. Lisez ce guide [Comment devenir un développeur Full-Stack en 2025 (et décrocher un emploi) – Un manuel pour débutants](https://www.freecodecamp.org/news/become-a-full-stack-developer-and-get-a-job/) pour apprendre à devenir un développeur Full Stack.

### **Comment comprendre les concepts de System Design ?**

La réponse courte : avec du temps et une pratique constante.

Considérez les choses ainsi : si vous savez utiliser un crayon, c'est à vous de décider si vous l'utilisez pour dessiner ou pour écrire. Le crayon n'est qu'un outil. De même, en System Design, une fois que vous avez compris les concepts de base, il s'agit de savoir *quand* et *où* les appliquer. Le reste – frameworks, outils et technologies – ne sont que des moyens pour arriver à une fin.

Il ne s'agit pas de mémoriser des modèles, mais de développer l'instinct d'utiliser les bonnes briques au bon moment.

### Quels outils devriez-vous connaître avant de plonger dans le System Design ?

En vérité, la liste ne cesse de s'allonger. De nouveaux outils et plateformes émergent constamment. Mais d'après mon expérience, avoir une base solide dans les domaines suivants fait une énorme différence :

* **Développement Full Stack** – pour comprendre comment les systèmes frontend et backend interagissent.
    
* **Plateformes Cloud** (comme AWS, GCP ou Azure) – car la plupart des systèmes modernes sont cloud-native.
    
* **Pipelines CI/CD** – pour automatiser les tests, l'intégration et le déploiement.
    
* **Stratégies de déploiement** – pour savoir comment déployer de nouveaux changements avec un risque minimal.
    

Maîtriser ces éléments vous donne la force technique nécessaire pour concevoir des systèmes évolutifs, fiables et prêts pour la production. Je suis développeur frontend, pourquoi devrais-je connaître le System Design ?

### Quelles ressources devrais-je étudier pour apprendre le System Design ?

Dans mon dernier [article](https://www.freecodecamp.org/news/become-a-full-stack-developer-and-get-a-job), j'ai partagé toutes les ressources qui m'ont aidé à apprendre le System Design.

Le System Design est crucial pour construire des applications fiables et performantes. J'ai exploré les ressources suivantes :

* [**Répertoire GitHub gratuit sur le System Design**](https://github.com/donnemartin/system-design-primer)
    
* [**Un autre répertoire GitHub gratuit sur le System Design**](https://github.com/ByteByteGoHq/system-design-101)
    
* [Manuel de System Design gratuit](https://www.systemdesignhandbook.com/system-design-interview-handbook/)
    
* [Plateforme d'apprentissage pratique gratuite sur le System Design](https://grokkingthesystemdesign.com/intro-to-system-design/)
    
* [Blog d'introduction gratuit au System Design](https://www.educative.io/guide/system-design)
    

Les études de cas et les architectures réelles peuvent également vous aider à comprendre les systèmes à grande échelle. Vous pouvez suivre n'importe quel blog d'ingénierie de Big Tech (Uber en a un excellent).

Pour les concepts de haut niveau, j'ai suivi le cours [**Grokking System Design**](https://www.educative.io/courses/grokking-the-system-design-interview). C'est une ressource payante, et je l'ai utilisée pour approfondir ma compréhension de l'architecture à l'échelle. Ce n'est pas obligatoire, mais cela m'a aidé à réfléchir à l'architecture à grande échelle.

**Note :** il existe bien sûr d'autres sites et cours, mais je ne partage que ce que j'ai personnellement expérimenté et utilisé, en privilégiant d'abord le contenu GRATUIT.

### Où pratiquer le System Design

C'est ici que le véritable apprentissage commence. Commencez par choisir n'importe quelle application existante sur Internet, comme je l'ai fait. Recherchez quelque chose de spécifique sur Google, comme « portail de candidature à un emploi », mais évitez les résultats de la première page. Ces applications sont généralement bien optimisées et suivent déjà les meilleures pratiques en System Design.

Au lieu de cela, creusez plus profondément et explorez les résultats de la deuxième ou troisième page. Recherchez une application qui semble être à ses débuts.

Une fois que vous en avez trouvé une, essayez de comprendre comment l'ensemble de l'application fonctionne. Décomposez-la en ses composants de base, puis imaginez ce qui se passerait si cette application commençait à recevoir 1 million d'utilisateurs par jour. Vous commencerez naturellement à voir quels éléments de System Design sont nécessaires pour gérer ce type de charge.

## Notes finales

L'apprentissage du System Design devient beaucoup plus facile lorsque vous avez déjà construit quelque chose. Disons que vous avez créé une application et que vous réfléchissez maintenant à la manière de la mettre à l'échelle – c'est là que le véritable apprentissage commence. Dès l'instant où vous commencez à noter vos exigences (comme le comportement de votre application lorsqu'elle commence à recevoir plus de trafic), vous commencez naturellement à développer une pensée au niveau système. C'est ce processus de planification et d'anticipation de l'utilisation réelle qui transforme la théorie en une compétence pratique.

## Conclusion

Full Stack + System Design = Le Stack de développeur ultime 🔥

En maîtrisant ces compétences, vous pouvez transformer n'importe quelle idée en un produit réel, obtenir des emplois bien rémunérés et même lancer votre propre entreprise technologique.

Maintenant, c'est à vous – que construisez-vous ensuite ? Dites-le-moi !

C'est tout pour moi. Si vous avez trouvé cet article utile, n'hésitez pas à le partager et à me contacter. Je suis toujours ouvert aux nouvelles opportunités :

* Suivez-moi sur X : [Twitter de Prankur](https://x.com/prankurpandeyy)
    
* Contactez-moi sur LinkedIn : [LinkedIn de Prankur](https://linkedin.com/in/prankurpandeyy)
    
* Suivez-moi sur GitHub : [Github de Prankur](https://github.com/prankurpandeyy)
    
* Voir mon Portfolio : [Portfolio de Prankur](https://prankurpandeyy.netlify.app/)