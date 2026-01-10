---
title: Le Manuel d'Architecture Logicielle
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-07-26T21:25:08.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-software-architecture-patterns
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels
seo_title: Le Manuel d'Architecture Logicielle
---

-3172740.jpg
balises:
- nom: api
  slug: api
- nom: Microservices
  slug: microservices
- nom: serverless
  slug: serverless
- nom: architecture logicielle
  slug: architecture-logicielle
seo_title: null
seo_desc: 'Salut à tous ! Dans ce manuel, vous allez apprendre le vaste et complexe domaine qu'est l'Architecture Logicielle.

C'est un domaine que j'ai trouvé à la fois confus et intimidant lorsque j'ai commencé mon parcours dans le codage. Alors, je vais essayer de vous épargner la confusion.

Dans ce manuel, je vais essayer de vous donner une introduction simple, de surface et facile à comprendre à l'Architecture Logicielle.

Nous allons parler de ce qu'est l'architecture dans le monde du logiciel, de certains des principaux concepts que vous devriez comprendre, et de certains des modèles d'architecture les plus largement utilisés aujourd'hui.

Pour chaque sujet, je vais donner une brève introduction théorique. Ensuite, je vais partager quelques exemples de code pour vous donner une idée plus claire de leur fonctionnement. C'est parti !'
---

Salut à tous ! Dans ce manuel, vous allez apprendre le vaste et complexe domaine qu'est l'Architecture Logicielle.

C'est un domaine que j'ai trouvé à la fois confus et intimidant lorsque j'ai commencé mon parcours dans le codage. Alors, je vais essayer de vous épargner la confusion.

Dans ce manuel, je vais essayer de vous donner une introduction simple, de surface et facile à comprendre à l'Architecture Logicielle.

Nous allons parler de ce qu'est l'architecture dans le monde du logiciel, de certains des principaux concepts que vous devriez comprendre, et de certains des modèles d'architecture les plus largement utilisés aujourd'hui.

Pour chaque sujet, je vais donner une brève introduction théorique. Ensuite, je vais partager quelques exemples de code pour vous donner une idée plus claire de leur fonctionnement. C'est parti !

## Table des Matières

* [Qu'est-ce que l'architecture logicielle](#heading-quest-ce-que-larchitecture-logicielle) ?
    
* [Concepts importants d'architecture logicielle à connaître](#heading-concepts-importants-darchitecture-logicielle-a-connaître)
    
    * [Qu'est-ce que le modèle Client-Serveur](#quest-ce-que-le-modèle-client-serveur) ?
        
    * [Qu'est-ce que les APIs](#heading-quest-ce-que-les-apis) ?
        
    * [Qu'est-ce que la Modularité](#heading-quest-ce-que-la-modularité) ?
        
* [À quoi ressemble votre infrastructure](#heading-a-quoi-ressemble-votre-infrastructure) ?
    
    * [Architecture Monolithique](#heading-architecture-monolithique)
        
    * [Architecture de Microservices](#heading-architecture-de-microservices)
        
    * [Qu'est-ce que le Back-End pour Front-End (BFF)](#heading-quest-ce-que-le-back-end-pour-front-end-bff) ?
        
    * [Comment utiliser les équilibreurs de charge et la mise à l'échelle horizontale](#heading-comment-utiliser-les-equilibreurs-de-charge-et-la-mise-a-lechelle-horizontale)
        
* [Où vit votre infrastructure](#heading-ou-vit-votre-infrastructure)
    
    * [Hébergement sur site](#heading-hebergement-sur-site)
        
    * [Fournisseurs de serveurs traditionnels](#heading-fournisseurs-de-serveurs-traditionnels)
        
    * [Hébergement sur le Cloud](#heading-hebergement-sur-le-cloud)
        
        * [Traditionnel](#heading-traditionnel)
            
        * [Élastique](#heading-elastique)
            
        * [Serverless](#heading-serverless)
            
        * [Beaucoup d'autres services](#heading-beaucoup-dautres-services)
            
* [Différentes structures de dossiers à connaître](#heading-differentes-structures-de-dossiers-a-connaître)
    
    * [Structure de dossier tout en un](#heading-structure-de-dossier-tout-en-un)
        
    * [Structure de dossier en couches](#heading-structure-de-dossier-en-couches)
        
    * [Structure de dossier MVC](#heading-structure-de-dossier-mvc)
        
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce que l'architecture logicielle ?

Selon [cette source](https://www.sei.cmu.edu/our-work/software-architecture/) :

> L'architecture logicielle d'un système représente les décisions de conception liées à la structure et au comportement globaux du système.

C'est assez générique, n'est-ce pas ? Absolument. Et c'est exactement ce qui me confusait tant lorsque je faisais des recherches sur l'architecture logicielle. C'est un sujet qui englobe beaucoup de choses et le terme est utilisé pour parler de nombreuses choses différentes.

La manière la plus simple que je puisse l'expliquer est que l'architecture logicielle fait référence à la manière dont vous organisez les choses dans le processus de création de logiciels. Et "choses" ici peut faire référence à :

* **Détails d'implémentation** (c'est-à-dire, la structure de dossiers de votre dépôt)
    
* **Décisions de conception d'implémentation** (Utilisez-vous le rendu côté serveur ou côté client ? Des bases de données relationnelles ou non relationnelles ?)
    
* Les **technologies** que vous choisissez (Utilisez-vous REST ou GraphQL pour votre API ? Python avec Django ou Node avec Express pour votre back-end ?)
    
* **Décisions de conception de système** (comme si votre système est un monolithe ou s'il est divisé en microservices ?)
    
* **Décisions d'infrastructure** (Hébergez-vous votre logiciel sur site ou sur un fournisseur de cloud ?)
    

C'est beaucoup de choix et de possibilités différents. Et ce qui complique un peu plus les choses, c'est que dans ces 5 divisions, différents modèles peuvent être combinés. Ce qui signifie que je peux avoir une API monolithique qui utilise REST ou GraphQL, une application basée sur des microservices hébergée sur site ou sur le cloud, et ainsi de suite.

Pour mieux expliquer ce désordre, nous allons d'abord expliquer quelques concepts génériques de base. Ensuite, nous allons passer en revue certaines de ces divisions, en expliquant les modèles ou choix d'architecture les plus couramment utilisés de nos jours pour construire des applications.

# Concepts Importants d'Architecture Logicielle à Connaître

## Qu'est-ce que le Modèle Client-Serveur ?

**Client-serveur** est un modèle qui structure les tâches ou charges de travail d'une application entre un fournisseur de ressources ou de services (serveur) et un demandeur de services ou de ressources (client).

En termes simples, le client est l'application qui demande un certain type d'information ou effectue des actions, et le serveur est le programme qui envoie des informations ou effectue des actions en fonction de ce que fait le client.

Les clients sont normalement représentés par des applications front-end qui s'exécutent soit sur le web, soit sur des applications mobiles (bien que d'autres plateformes existent également et que les applications back-end peuvent également agir en tant que clients). Les serveurs sont généralement des applications back-end.

Pour illustrer cela avec un exemple, imaginez que vous entrez sur votre réseau social préféré. Lorsque vous entrez l'URL dans votre navigateur et que vous appuyez sur Entrée, votre navigateur agit comme l'application cliente et **envoie une requête** au serveur du réseau social, qui **répond** en vous envoyant le contenu du site web.

La plupart des applications de nos jours utilisent un modèle client-serveur. Le concept le plus important à retenir à ce sujet est que **les clients demandent des ressources ou des services** que **le serveur exécute**.

Un autre concept important à connaître est que les clients et les serveurs font partie du même système, mais chacun est une application/programme à part entière. Ce qui signifie qu'ils peuvent être développés, hébergés et exécutés séparément.

Si vous n'êtes pas familier avec la différence entre le front-end et le back-end, [voici un article sympa qui l'explique](https://www.freecodecamp.org/news/frontend-vs-backend-whats-the-difference/). Et voici [un autre article](https://www.freecodecamp.org/news/how-the-web-works-part-ii-client-server-model-the-structure-of-a-web-application-735b4b6d76e3/) qui développe le concept de client-serveur.

## Qu'est-ce que les APIs ?

Nous venons de mentionner que les clients et les serveurs sont des entités qui communiquent entre elles pour demander des choses et répondre à des choses. La manière dont ces deux parties communiquent généralement est via une API (interface de programmation d'application).

Une API n'est rien de plus qu'un ensemble de règles définies qui établit comment une application peut communiquer avec une autre. C'est comme un contrat entre les deux parties qui dit "Si vous envoyez A, je répondrai toujours B. Si vous envoyez C, je répondrai toujours D..." et ainsi de suite.

Ayant cet ensemble de règles, le client sait exactement ce qu'il doit demander pour accomplir une certaine tâche, et le serveur sait exactement ce que le client demandera lorsqu'une certaine action doit être effectuée.

Il existe différentes manières de mettre en œuvre une API. Les plus couramment utilisées sont REST, SOAP et GraphQL.

En ce qui concerne la manière dont les APIs communiquent, le protocole HTTP est le plus souvent utilisé et le contenu est échangé au format JSON ou XML. Mais d'autres protocoles et formats de contenu sont parfaitement possibles.

Si vous souhaitez approfondir ce sujet, [voici un bel article](https://www.freecodecamp.org/news/http-request-methods-explained/) à lire.

## Qu'est-ce que la Modularité ?

Lorsque nous parlons de "modularité" dans l'architecture logicielle, nous faisons référence à la pratique de diviser les grandes choses en morceaux plus petits. Cette pratique de décomposition est effectuée pour simplifier les grandes applications ou bases de code.

La modularité présente les avantages suivants :

* Elle est bonne pour diviser les préoccupations et les fonctionnalités, ce qui aide à la visualisation, à la compréhension et à l'organisation d'un projet.
    
* Le projet tend à être plus facile à maintenir et moins sujet aux erreurs et aux bugs lorsqu'il est clairement organisé et subdivisé.
    
* Si votre projet est subdivisé en de nombreux morceaux différents, chacun peut être travaillé et modifié séparément et indépendamment, ce qui est souvent très utile.
    

Je sais que cela semble un peu générique, mais la modularité ou la pratique de subdiviser les choses est une grande partie de ce qu'est l'architecture logicielle. Alors gardez simplement ce concept à l'esprit – il deviendra plus clair et apparent à mesure que nous passerons en revue quelques exemples. ;)

Si vous souhaitez un peu plus d'informations sur ce sujet, j'ai récemment écrit [un article sur l'utilisation des modules en JS](https://www.freecodecamp.org/news/modules-in-javascript/) que vous pourriez trouver utile.

# À quoi ressemble votre infrastructure ?

D'accord, passons maintenant aux bonnes choses. Nous allons commencer à parler des nombreuses façons différentes dont vous pouvez organiser une application logicielle, en commençant par la manière dont vous pouvez organiser l'infrastructure derrière votre projet.

Pour rendre tout cela moins abstrait, nous allons utiliser une application hypothétique que nous appellerons Notflix.🤔🤫🥸

Commentaire de côté : gardez à l'esprit que cet exemple pourrait ne pas être le plus réaliste et que je vais supposer/forcer des situations afin de présenter certains concepts. L'idée ici est de vous aider à comprendre les concepts d'architecture de base à travers un exemple, et non de réaliser une analyse du monde réel.

## Architecture Monolithique

Donc, Notflix sera une application typique de streaming vidéo, dans laquelle l'utilisateur pourra regarder des films, des séries, des documentaires, etc. L'utilisateur pourra utiliser l'application dans les navigateurs web, dans une application mobile et sur une application TV également.

Les principaux services inclus dans notre application seront l'**authentification** (afin que les gens puissent créer des comptes, se connecter, etc.), les **paiements** (afin que les gens puissent s'abonner et accéder au contenu... car vous ne pensiez pas que tout cela était gratuit, n'est-ce pas ? 😑) et le **streaming** bien sûr (afin que les gens puissent regarder ce pour quoi ils paient).

Un croquis rapide de notre architecture pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Untitled-Diagram.drawio-3.png align="left")

*Une architecture monolithique classique*

À gauche, nous avons nos trois applications front-end différentes qui agiront en tant que clients dans ce système. Elles pourraient être développées avec React et React-native, par exemple.

Nous avons un serveur unique qui recevra les requêtes de toutes les applications clientes, communiquera avec la base de données lorsque cela sera nécessaire, et répondra à chaque front-end en conséquence. Le back-end pourrait être développé avec Node et Express, par exemple.

Ce type d'architecture est appelé un **monolithe** car il y a une seule application serveur qui est responsable de toutes les fonctionnalités du système. Dans notre cas, si un utilisateur souhaite s'authentifier, nous payer ou regarder l'un de nos films, toutes les requêtes seront envoyées à la même application serveur.

L'avantage principal d'une conception monolithique est sa simplicité. Son fonctionnement et la configuration requise sont simples et faciles à suivre, et c'est pourquoi la plupart des applications commencent de cette manière.

## Architecture de Microservices

Il s'avère que Notflix cartonne complètement. Nous venons de sortir la dernière saison de "Stranger thugs", qui est une série de science-fiction géniale sur des rappers adolescents, et notre film "Agent 404" (sur un agent secret qui s'infiltre dans une entreprise en simulant être un programmeur senior mais qui ne connaît en fait rien au code) bat tous les records...

Nous obtenons des dizaines de milliers de nouveaux utilisateurs chaque mois du monde entier, ce qui est génial pour notre entreprise mais moins pour notre application monolithique.

Ces derniers temps, nous avons connu des retards dans les temps de réponse du serveur, et même si nous avons **mis à l'échelle verticalement** le serveur (ajouté plus de RAM et de GPU), le pauvre ne semble pas pouvoir supporter la charge qu'il subit.

De plus, nous avons continué à développer de nouvelles fonctionnalités dans notre système (comme un outil de recommandation qui lit les préférences de l'utilisateur et recommande des films qui conviennent au profil de l'utilisateur) et **notre base de code commence à paraître énorme et très complexe** à travailler.

En analysant ce problème en profondeur, nous avons découvert que la fonctionnalité qui consomme le plus de ressources est le streaming, tandis que d'autres services comme l'authentification et les paiements ne représentent pas une charge très importante.

Pour résoudre ce problème, nous allons mettre en œuvre une **architecture de microservices** qui ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Untitled-Diagram.drawio--1-.png align="left")

*Notre première implémentation de microservices*

Donc, si vous êtes nouveau dans tout cela, vous pourriez vous demander "qu'est-ce qu'un microservice", n'est-ce pas ? Eh bien, nous pourrions le définir comme le concept de diviser les fonctionnalités côté serveur en de nombreux petits serveurs qui sont responsables d'une ou de quelques fonctionnalités spécifiques.

En suivant notre exemple, avant nous avions un seul serveur responsable de toutes les fonctionnalités (une architecture monolithique). Après avoir implémenté les microservices, nous aurons un serveur responsable de l'authentification, un autre responsable des paiements, un autre pour le streaming, et le dernier pour les recommandations.

Les applications côté client communiqueront avec le serveur d'authentification lorsqu'un utilisateur souhaite se connecter, avec le serveur de paiements lorsque l'utilisateur souhaite payer, et avec le serveur de streaming lorsque l'utilisateur souhaite regarder quelque chose.

**Toute cette communication se fait via des APIs** tout comme avec un serveur monolithique régulier (ou via d'autres systèmes de communication comme [Kafka](https://kafka.apache.org/) ou [RabbitMQ](https://www.rabbitmq.com/)). La seule différence est que maintenant nous avons différents serveurs responsables de différentes actions au lieu d'un seul qui fait tout.

Cela semble un peu plus complexe, et c'est le cas, mais les microservices nous offrent les avantages suivants :

* Vous pouvez **mettre à l'échelle des services particuliers selon les besoins**, au lieu de mettre à l'échelle tout le back-end en une seule fois. En suivant notre exemple, lorsque nous avons commencé à rencontrer des problèmes de performance, nous avons mis à l'échelle verticalement tout notre serveur – mais en réalité, la fonctionnalité qui nécessitait le plus de ressources était uniquement le streaming. Maintenant que nous avons la fonctionnalité de streaming séparée en un seul serveur, nous pouvons mettre à l'échelle uniquement celui-ci et laisser les autres tranquilles tant qu'ils continuent à bien fonctionner.
    
* Les fonctionnalités seront plus **faiblement couplées**, ce qui signifie que nous pourrons les développer et les déployer indépendamment.
    
* La **base de code** pour chaque serveur sera beaucoup plus petite et **plus simple**. Ce qui est bien pour les développeurs qui travaillent avec nous depuis le début, et aussi plus facile et plus rapide pour les nouveaux développeurs à comprendre.
    

Les microservices sont une architecture plus complexe à configurer et à gérer, c'est pourquoi cela n'a du sens que pour des projets très grands. La plupart des projets commenceront en tant que monolithes et migreront vers les microservices uniquement lorsque cela sera nécessaire pour des raisons de performance.

Si vous souhaitez en savoir plus sur les microservices, [voici une très bonne explication](https://www.youtube.com/watch?v=CdBtNQZH8a4).

### Qu'est-ce que le Back-End pour Front-End (BFF) ?

Un problème qui survient lors de la mise en œuvre de microservices est que la communication avec les applications front-end devient plus complexe. Maintenant, nous avons de nombreux serveurs responsables de différentes choses, ce qui signifie que les applications front-end devraient garder une trace de ces informations pour savoir à qui envoyer les requêtes.

Normalement, ce problème est résolu en implémentant une couche intermédiaire entre les applications front-end et les microservices. Cette couche recevra toutes les requêtes front-end, les redirigera vers le microservice correspondant, recevra la réponse du microservice, puis redirigera la réponse vers l'application front-end correspondante.

L'avantage du modèle BFF est que nous obtenons les avantages de l'architecture de microservices, sans compliquer excessivement la communication avec les applications front-end.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Untitled-Diagram.drawio--2-.png align="left")

*Notre implémentation BFF*

Voici une [vidéo expliquant le modèle BFF](https://www.youtube.com/watch?v=SSo-z16wEnc) si vous souhaitez en savoir plus à ce sujet.

### Comment utiliser les équilibreurs de charge et la mise à l'échelle horizontale

Donc, notre application de streaming continue de croître de manière exponentielle. Nous avons des millions d'utilisateurs dans le monde qui regardent nos films 24h/24 et 7j/7, et plus tôt que prévu, nous commençons à rencontrer des problèmes de performance.

Une fois de plus, nous avons constaté que le service de streaming est celui qui subit le plus de stress, et nous avons **mis à l'échelle verticalement** ce serveur autant que possible. Une subdivision supplémentaire de ce service en plus de microservices n'a pas de sens, donc nous avons décidé de **mettre à l'échelle horizontalement** ce service.

Auparavant, nous avons mentionné que **la mise à l'échelle verticale** signifie ajouter plus de ressources (RAM, espace disque, GPU, etc.) à un seul serveur/ordinateur. **La mise à l'échelle horizontale**, en revanche, signifie configurer plus de serveurs pour effectuer la même tâche.

Au lieu d'avoir un seul serveur responsable du streaming, nous en aurons maintenant trois. Ensuite, les requêtes effectuées par les clients seront réparties entre ces trois serveurs afin que tous gèrent une charge acceptable.

Cette distribution des requêtes est normalement effectuée par une chose appelée **équilibreur de charge**. Les équilibreurs de charge agissent comme des [**proxys inverses**](https://www.strongdm.com/blog/difference-between-proxy-and-reverse-proxy#:~:text=A%20traditional%20forward%20proxy%20server,on%20behalf%20of%20multiple%20servers.) pour nos serveurs, interceptant les requêtes des clients avant qu'elles n'atteignent le serveur et redirigeant cette requête vers le serveur correspondant.

Alors qu'une connexion client-serveur typique pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1234.png align="left")

*Ce que nous avions avant*

En utilisant un équilibreur de charge, nous pouvons distribuer les requêtes des clients sur plusieurs serveurs :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/4312.drawio-1.png align="left")

*Ce que nous voulons maintenant*

Vous devez savoir que la mise à l'échelle horizontale est également possible avec les bases de données, tout comme avec les serveurs. Une façon de mettre en œuvre cela est avec un modèle source-réplica, dans lequel une base de données source particulière recevra toutes les requêtes d'écriture et répliquera ses données le long d'une ou plusieurs bases de données réplicas. Les bases de données réplicas recevront et répondront à toutes les requêtes de lecture.

Les avantages de la réplication de base de données sont :

* Meilleure performance : Ce modèle améliore les performances et permet de traiter plus de requêtes en parallèle.
    
* Fiabilité et disponibilité : Si l'un de vos serveurs de base de données est détruit ou inaccessible pour une raison quelconque, les données sont toujours préservées dans d'autres bases de données.
    

Ainsi, après avoir implémenté un équilibreur de charge, une mise à l'échelle horizontale et une réplication de base de données, notre architecture pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Untitled-Diagram.drawio--3--2.png align="left")

*Notre architecture mise à l'échelle horizontalement*

Voici [une vidéo explicative géniale sur les équilibreurs de charge](https://www.youtube.com/watch?v=sCR3SAVdyCc) si vous êtes intéressé à en savoir plus.

Commentaire de côté : lorsque nous parlons de microservices, d'équilibreurs de charge et de mise à l'échelle, nous parlons probablement toujours d'applications back-end. Pour les applications front-end, elles sont presque toujours développées en tant que monolithes, bien qu'il existe également une chose étrange et intéressante appelée [micro-frontends](https://www.youtube.com/watch?v=w58aZjACETQ).🧐

# Où vit votre infrastructure

Maintenant que nous avons une idée de base de la manière dont une infrastructure d'application pourrait être organisée, la prochaine chose à laquelle penser est où nous allons mettre tout cela.

Comme nous allons le voir, il y a principalement trois options lors de la décision de l'endroit et de la manière d'héberger une application : sur site, sur des fournisseurs de serveurs traditionnels, ou sur le cloud.

## Hébergement sur site

Sur site signifie que vous possédez le matériel sur lequel votre application s'exécute. Dans le passé, c'était la manière la plus traditionnelle d'héberger des applications. Les entreprises avaient des salles dédiées pour les serveurs et des équipes dédiées à la configuration et à la maintenance du matériel.

Le bon côté de cette option est que l'entreprise obtient un contrôle total sur le matériel. Le mauvais côté est qu'elle nécessite de l'espace, du temps et de l'argent.

Imaginez si vous vouliez mettre à l'échelle horizontalement un certain serveur, cela signifierait acheter plus d'équipements, les configurer, les surveiller constamment, réparer ce qui est cassé... Et si vous devez plus tard réduire l'échelle de ce serveur, eh bien, normalement vous n'êtes pas en mesure de retourner ces choses après les avoir achetées.🥲

Pour la plupart des entreprises, avoir des serveurs sur site signifie consacrer beaucoup de ressources à une tâche non directement liée aux objectifs de l'entreprise.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-221.png align="left")

*Comment nous imaginions notre salle de serveurs chez Notflix*

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-222.png align="left")

*Comment cela s'est terminé*

Une situation dans laquelle les serveurs sur site ont encore du sens est lorsque l'on traite des informations très délicates ou privées. Pensez au logiciel qui fait fonctionner une centrale électrique, ou aux informations bancaires privées, par exemple. Beaucoup de ces organisations décident d'avoir des serveurs sur site comme moyen d'avoir un contrôle complet sur leur logiciel et leur matériel.

## Fournisseurs de serveurs traditionnels

Une option plus confortable pour la plupart des entreprises sont les fournisseurs de serveurs traditionnels. Ce sont des entreprises qui ont leurs propres serveurs et qui les louent simplement. Vous décidez de quel type de matériel vous aurez besoin pour votre projet et payez des frais mensuels pour cela (ou un certain montant basé sur d'autres conditions).

Ce qui est génial avec cette option, c'est que vous n'avez plus à vous soucier de quoi que ce soit lié au matériel. Le fournisseur s'en occupe, et en tant qu'entreprise de logiciels, vous ne vous souciez que de votre objectif principal, le logiciel.

Une autre chose sympa est que la mise à l'échelle est facile et sans risque. Si vous avez besoin de plus de matériel, vous payez pour cela. Et si vous n'en avez plus besoin, vous arrêtez simplement de payer.

Un exemple de fournisseur de serveurs bien connu est [hostinger](https://www.hostinger.com).

## Hébergement sur le Cloud

Si vous avez été dans le domaine de la technologie depuis un certain temps, vous avez probablement entendu le mot "cloud" plus d'une fois. Au début, cela semble quelque chose d'abstrait et de magique, mais en réalité, ce qui se cache derrière n'est rien de plus que d'énormes centres de données appartenant à des entreprises comme Amazon, Google et Microsoft.

À un moment donné, ces entreprises ont découvert qu'elles avaient une énorme puissance de calcul qu'elles n'utilisaient pas tout le temps. Et comme tout ce matériel représente encore un coût, que vous l'utilisiez ou non, la chose intelligente à faire est de commercialiser cette puissance de calcul auprès d'autres.

Et c'est ce qu'est le cloud computing. En utilisant différents services comme **AWS** (Amazon Web Services), **Google Cloud**, ou Microsoft **Azure**, nous sommes en mesure d'héberger nos applications dans les centres de données de ces entreprises et de profiter de toute cette puissance de calcul.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-219.png align="left")

*À quoi un "cloud" pourrait réellement ressembler*

Lorsque vous commencez à connaître les services cloud, il est important de noter qu'il existe de nombreuses façons différentes de les utiliser :

### Traditionnel

La première façon est de les utiliser de manière similaire à celle dont vous utiliseriez un fournisseur de serveurs traditionnel. Vous sélectionnez le type de matériel que vous souhaitez et payez exactement pour cela sur une base mensuelle.

### Élastique

La deuxième façon est de tirer parti du calcul "élastique" offert par la plupart des fournisseurs. "Élastique" signifie que la capacité matérielle de votre application augmentera ou diminuera automatiquement en fonction de l'utilisation de votre application.

Par exemple, vous pourriez commencer avec un serveur qui a 8 Go de RAM et 500 Go d'espace disque. Si votre serveur commence à recevoir de plus en plus de requêtes et que ces capacités ne sont plus suffisantes pour offrir de bonnes performances, le système peut automatiquement effectuer une mise à l'échelle verticale ou horizontale.

L'avantage de cela est que vous pouvez configurer tout cela à l'avance et ne plus avoir à vous en soucier. Comme les serveurs montent et descendent automatiquement en échelle, vous ne payez que pour les ressources que vous consommez.

### Serverless

Une autre façon dont vous pouvez utiliser le cloud computing est avec une architecture serverless.

En suivant ce modèle, vous n'aurez pas de serveur qui reçoit toutes les requêtes et y répond. Au lieu de cela, vous aurez des fonctions individuelles mappées à un point d'accès (similaire à un point de terminaison d'API).

Ces fonctions s'exécuteront chaque fois qu'elles recevront une requête et effectueront l'action que vous avez programmée pour elles (connexion à une base de données, exécution d'opérations CRUD ou toute autre chose que vous pourriez faire sur un serveur régulier).

Ce qui est très bien avec l'architecture serverless, c'est que vous oubliez tout sur la maintenance et la mise à l'échelle des serveurs. Vous avez simplement des fonctions qui s'exécutent lorsque vous en avez besoin, et chaque fonction est mise à l'échelle automatiquement selon les besoins.

En tant que client, vous ne payez que pour le nombre de fois où la fonction est exécutée et la quantité de temps de traitement que chaque exécution dure.

Si vous souhaitez en savoir plus, voici une [explication du modèle serverless](https://www.youtube.com/watch?v=vxJobGtqKVM).

### Beaucoup d'autres services

Vous pouvez probablement voir comment les services élastiques et serverless offrent une alternative très simple et pratique pour configurer une infrastructure logicielle.

Et en plus des services liés aux serveurs, les fournisseurs de cloud offrent des tonnes d'autres solutions telles que des bases de données relationnelles et non relationnelles, des services de stockage de fichiers, des services de cache, des services d'authentification, des services de machine learning et de traitement de données, de surveillance et d'analyse de performance, et plus encore. Tout hébergé dans le cloud.

Grâce à des outils comme [Terraform](https://www.terraform.io/) ou AWS [CloudFormation](https://aws.amazon.com/es/cloudformation/), nous pouvons même configurer notre infrastructure en tant que code. Ce qui signifie que nous pouvons écrire un script qui configure un serveur, une base de données, et tout ce dont nous pourrions avoir besoin sur le cloud en quelques minutes seulement.

C'est époustouflant d'un point de vue ingénierie, et vraiment pratique pour nous en tant que développeurs. Le cloud computing offre aujourd'hui un ensemble très complet de solutions qui peuvent facilement s'adapter des plus petits projets aux plus grands produits numériques sur terre. C'est pourquoi de plus en plus de projets logiciels choisissent aujourd'hui d'héberger leur infrastructure dans le cloud.

Comme mentionné précédemment, les fournisseurs de cloud les plus utilisés et les plus connus sont [AWS](https://aws.amazon.com/), [Google Cloud](https://cloud.google.com/) et [Azure](https://azure.microsoft.com/). Bien qu'il existe d'autres options comme [IBM](https://www.ibm.com/cloud), [DigitalOcean](https://www.digitalocean.com/), et [Oracle](https://www.oracle.com/cloud/).

La plupart de ces fournisseurs offrent le même type de services, bien qu'ils puissent avoir des noms différents. Par exemple, les fonctions serverless sont appelées "lambdas" sur AWS et "cloud functions" sur Google Cloud.

# Différentes structures de dossiers à connaître

D'accord, jusqu'à présent nous avons vu comment l'architecture peut faire référence à l'organisation de l'infrastructure et à l'hébergement. Maintenant, regardons un peu de code et comment l'architecture peut faire référence aux structures de dossiers et à la modularité du code.

## Structure de dossier tout en un

Pour illustrer pourquoi les structures de dossiers sont importantes, construisons un exemple fictif d'API. Nous aurons une base de données fictive de lapins 🐰🐰 et l'API effectuera des actions [CRUD](https://www.freecodecamp.org/news/crud-operations-explained/) sur celle-ci. Nous allons construire cela avec Node et Express.

Voici notre première approche, sans aucune structure de dossiers. Notre dépôt sera composé du dossier `node modules`, et des fichiers `app.js`, `package-lock.json` et `package.json`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-227.png align="left")

Dans notre fichier app.js, nous aurons notre petit serveur, notre base de données fictive, et deux points de terminaison :

```javascript
// App.js
const express = require('express');

const app = express()
const port = 7070

// Mock DB
const db = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' },
    { id: 3, name: 'Joe' },
    { id: 4, name: 'Jack' },
    { id: 5, name: 'Jill' },
    { id: 6, name: 'Jak' },
    { id: 7, name: 'Jana' },
    { id: 8, name: 'Jan' },
    { id: 9, name: 'Jas' },
    { id: 10, name: 'Jasmine' },
]

/* Routes */
app.get('/rabbits', (req, res) => {
    res.json(db)
})

app.get('/rabbits/:idx', (req, res) => {
    res.json(db[req.params.idx])
})

app.listen(port, () => console.log(`\u26a1\ufe0f[server]: Server is running at http://localhost:${port}`))
```

Si nous testons les points de terminaison, nous verrons qu'ils fonctionnent parfaitement bien :

```plaintext
http://localhost:7070/rabbits

# [
#   {
#     "id": 1,
#     "name": "John"
#   },
#   {
#     "id": 2,
#     "name": "Jane"
#   },
#   {
#     "id": 3,
#     "name": "Joe"
#   },
#   ....
# ]

###

http://localhost:7070/rabbits/1

# {
#   "id": 2,
#   "name": "Jane"
# }
```

Alors, quel est le problème avec cela ? Rien, en fait, cela fonctionne très bien. Le problème ne surgira que lorsque la base de code deviendra plus grande et plus complexe, et que nous commencerons à ajouter de nouvelles fonctionnalités à notre API.

De manière similaire à ce dont nous avons parlé auparavant en expliquant les architectures monolithiques, avoir tout en un seul endroit est agréable et facile au début. Mais lorsque les choses commencent à devenir plus grandes et plus complexes, cette approche est confuse et difficile à suivre.

En suivant le principe de modularité, une meilleure idée est d'avoir différents dossiers et fichiers pour les différentes responsabilités et actions que nous devons effectuer.

Pour mieux illustrer cela, ajoutons de nouvelles fonctionnalités à notre API et voyons comment nous pouvons adopter une approche modulaire avec l'aide d'une architecture en couches.

## Structure de dossier en couches

L'architecture en couches consiste à diviser les préoccupations et les responsabilités en différents dossiers et fichiers, et à permettre une communication directe uniquement entre certains dossiers et fichiers.

La question de savoir combien de couches votre projet devrait avoir, quels noms chaque couche devrait avoir, et quelles actions elle devrait gérer est une question de discussion. Alors, voyons ce que je pense être une bonne approche pour notre exemple.

Notre application aura cinq couches différentes, qui seront ordonnées de cette manière :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/layers.png align="left")

*Couches de l'application*

* La couche application aura la configuration de base de notre serveur et la connexion à nos routes (la couche suivante).
    
* La couche routes aura la définition de toutes nos routes et la connexion aux contrôleurs (la couche suivante).
    
* La couche contrôleurs aura la logique réelle que nous voulons effectuer dans chacun de nos points de terminaison et la connexion à la couche modèle (la couche suivante, vous comprenez l'idée...)
    
* La couche modèle contiendra la logique pour interagir avec notre base de données fictive.
    
* Enfin, la couche persistance est l'endroit où notre base de données sera.
    

Vous pouvez voir que cette approche est beaucoup plus structurée et a une division claire des préoccupations. Cela peut sembler beaucoup de code standard. Mais après l'avoir configuré, cette architecture nous permettra de savoir clairement où se trouve chaque chose et quels dossiers et fichiers sont responsables de chaque action que notre application exécute.

Une chose importante à garder à l'esprit est que dans ces types d'architectures **il y a un flux de communication défini** entre les couches qui doit être suivi pour que cela ait du sens.

Cela signifie qu'une requête doit d'abord passer par la première couche, puis la deuxième, puis la troisième et ainsi de suite. Aucune requête ne devrait sauter des couches car cela perturberait la logique de l'architecture et les avantages d'organisation et de modularité qu'elle nous offre.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/layers--1--1.png align="left")

*Une autre façon d'imaginer notre architecture*

Regardons un peu de code maintenant. En utilisant l'architecture en couches, notre structure de dossiers pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-229.png align="left")

* Nous avons un nouveau dossier appelé `db` qui contiendra notre fichier de base de données.
    
* Et un autre dossier appelé `rabbits` qui contiendra les routes, contrôleurs et modèles liés à cette entité.
    
* `app.js` configure notre serveur et se connecte aux routes.
    

```plaintext
// App.js
const express = require('express');

const rabbitRoutes = require('./rabbits/routes/rabbits.routes')

const app = express()
const port = 7070

/* Routes */
app.use('/rabbits', rabbitRoutes)

app.listen(port, () => console.log(`\u26a1\ufe0f[server]: Server is running at http://localhost:${port}`))
```

* `rabbits.routes.js` contient chacun des points de terminaison liés à cette entité et les lie aux contrôleurs correspondants (la fonction que nous voulons exécuter lorsque la requête atteint ce point de terminaison).
    

```plaintext
// rabbits.routes.js
const express = require('express')
const bodyParser = require('body-parser')

const jsonParser = bodyParser.json()

const { listRabbits, getRabbit, editRabbit, addRabbit, deleteRabbit } = require('../controllers/rabbits.controllers')

const router = express.Router()

router.get('/', listRabbits)

router.get('/:id', getRabbit)

router.put('/:id', jsonParser, editRabbit)

router.post('/', jsonParser, addRabbit)

router.delete('/:id', deleteRabbit)

module.exports = router
```

* `rabbits.controllers.js` contient la logique correspondant à chaque point de terminaison. C'est ici que nous programmons ce que la fonction doit prendre en entrée, quel processus elle doit effectuer et ce qu'elle doit retourner. 😉 De plus, chaque contrôleur se lie à la fonction de modèle correspondante (qui effectuera des opérations liées à la base de données).
    

```plaintext
// rabbits.controllers.js
const { getAllItems, getItem, editItem, addItem, deleteItem } = require('../models/rabbits.models')

const listRabbits = (req, res) => {
    try {
        const resp = getAllItems()
        res.status(200).send(resp)

    } catch (err) {
        res.status(500).send(err)
    }
}

const getRabbit = (req, res) => {
    try {
        const resp = getItem(parseInt(req.params.id))
        res.status(200).send(resp)

    } catch (err) {
        res.status(500).send(err)
    }
}

const editRabbit = (req, res) => {
    try {
        const resp = editItem(req.params.id, req.body.item)
        res.status(200).send(resp)
    } catch (err) {
        res.status(500).send(err)
    }
}

const addRabbit = (req, res) => {
    try {
        console.log( req.body.item )
        const resp = addItem(req.body.item)
        res.status(200).send(resp)
    } catch (err) {
        res.status(500).send(err)
    }
}

const deleteRabbit = (req, res) => {
    try {
        const resp = deleteItem(req.params.idx)
        res.status(200).send(resp)
    } catch (err) {
        res.status(500).send(err)
    }
}

module.exports = { listRabbits, getRabbit, editRabbit, addRabbit, deleteRabbit }
```

* `rabbits.models.js` est l'endroit où nous définissons les fonctions qui effectueront des actions CRUD sur notre base de données. Chaque fonction représente un type d'action différent (lire un, lire tous, éditer, supprimer, etc.). Ce fichier est celui qui se connecte à notre base de données.
    

```plaintext
// rabbits.models.js
const db = require('../../db/db')

const getAllItems = () => {
    try {
        return db
    } catch (err) {
        console.error("getAllItems error", err)
    }
}

const getItem = id => {
    try {
        return db.filter(item => item.id === id)[0]
    } catch (err) {
        console.error("getItem error", err)
    }
}

const editItem = (id, item) => {
    try {
        const index = db.findIndex(item => item.id === id)
        db[index] = item
        return db[index]
    } catch (err) {
        console.error("editItem error", err)
    }
}

const addItem = item => {
    try {
        db.push(item)
        return db
    } catch (err) {
        console.error("addItem error", err)
    }
}

const deleteItem = id => {
    try {
        const index = db.findIndex(item => item.id === id)
        db.splice(index, 1)
        return db
        return db
    } catch (err) {
        console.error("deleteItem error", err)
    }
}

module.exports = { getAllItems, getItem, editItem, addItem, deleteItem }
```

* Enfin, `db.js` héberge notre base de données fictive. Dans un projet réel, c'est ici que votre connexion de base de données réelle pourrait être.
    

```plaintext
// db.js
const db = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' },
    { id: 3, name: 'Joe' },
    { id: 4, name: 'Jack' },
    { id: 5, name: 'Jill' },
    { id: 6, name: 'Jak' },
    { id: 7, name: 'Jana' },
    { id: 8, name: 'Jan' },
    { id: 9, name: 'Jas' },
    { id: 10, name: 'Jasmine' },
]

module.exports = db
```

Comme nous pouvons le voir, il y a beaucoup plus de dossiers et de fichiers sous cette architecture. Mais en conséquence, notre base de code est beaucoup plus structurée et clairement organisée. Tout a sa propre place et la communication entre différents fichiers est clairement définie.

Ce type d'organisation facilite grandement l'ajout de nouvelles fonctionnalités, les modifications de code et la correction de bugs.

Une fois que vous vous serez familiarisé avec la structure des dossiers et que vous saurez où trouver chaque chose, vous verrez qu'il est très pratique de travailler avec ces fichiers plus courts et plus petits au lieu de devoir faire défiler un ou deux fichiers énormes où tout est mis ensemble.

Je suis également partisan d'avoir un dossier pour chacune des principales entités de votre application (les lapins dans notre cas). Cela permet de comprendre encore plus clairement à quoi chaque fichier est lié.

Supposons que nous voulons maintenant ajouter de nouvelles fonctionnalités pour ajouter/modifier/supprimer des chats et des chiens également. Nous créerions de nouveaux dossiers pour chacun d'eux, et chacun avec leurs propres fichiers de routes, de contrôleurs et de modèles. L'idée est de séparer les préoccupations et d'avoir chaque chose à sa place.👌👌

## Structure de dossier MVC

MVC est un modèle d'architecture qui signifie **Modèle Vue Contrôleur**. Nous pourrions dire que l'architecture MVC est comme une simplification de l'architecture en couches, incorporant également le côté front-end (UI) de l'application.

Sous cette architecture, nous n'aurons que trois couches principales :

* La couche vue sera responsable du rendu de l'UI.
    
* La couche contrôleurs sera responsable de la définition des routes et de la logique pour chacune d'elles.
    
* La couche modèle sera responsable de l'interaction avec notre base de données.
    

![Image](https://www.freecodecamp.org/news/content/images/2022/07/mvc--2-.png align="left")

Comme avant, chaque couche interagira uniquement avec la suivante afin que nous ayons un flux de communication clairement défini.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/mvc.png align="left")

*Une autre façon d'imaginer notre architecture*

Il existe de nombreux frameworks qui vous permettent de mettre en œuvre l'architecture MVC directement (comme [Django](https://www.djangoproject.com/) ou [Ruby on Rails](https://rubyonrails.org/) par exemple). Pour le faire avec Node et Express, nous aurons besoin d'un moteur de template comme [EJS](https://ejs.co/).

Si vous n'êtes pas familier avec les moteurs de template, ils ne sont qu'un moyen de rendre facilement du HTML tout en tirant parti des fonctionnalités programmatiques telles que les variables, les boucles, les conditionnelles, etc. (très similaire à ce que nous ferions avec JSX dans React).

Comme nous allons le voir dans un instant, nous allons créer des fichiers EJS pour chaque type de page que nous souhaitons rendre, et à partir de chaque contrôleur, nous allons rendre ces fichiers en tant que notre réponse, en leur passant la réponse correspondante en tant que variables.

Notre structure de dossiers ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-230.png align="left")

* Voyez que nous nous sommes débarrassés de la plupart des dossiers que nous avions avant et avons conservé les dossiers `db`, `controllers` et `models`.
    
* Nous avons ajouté un dossier `views` qui correspond à chacune des pages/réponses que nous souhaitons rendre.
    
* Les fichiers `db.js` et `models.js` restent exactement les mêmes.
    
* Notre `app.js` ressemblerait à ceci :
    

```plaintext
// App.js
const express = require("express");
var path = require('path');

const rabbitControllers = require("./rabbits/controllers/rabbits.controllers")

const app = express()
const port = 7070

// Ejs config
app.set("view engine", "ejs")
app.set('views', path.join(__dirname, './rabbits/views'))

/* Controllers */
app.use("/rabbits", rabbitControllers)

app.listen(port, () => console.log(`\u26a1\ufe0f[server]: Server is running at http://localhost:${port}`))
```

* `rabbits.controllers.js` change pour définir les routes, se connecter à la fonction de modèle correspondante, et rendre la vue correspondante pour chaque requête. Voyez que dans la méthode render nous passons la réponse de la requête en tant que paramètre à la vue. 😉
    

```plaintext
// rabbits.controllers.js
const express = require('express')
const bodyParser = require('body-parser')

const jsonParser = bodyParser.json()

const { getAllItems, getItem, editItem, addItem, deleteItem } = require('../models/rabbits.models')

const router = express.Router()

router.get('/', (req, res) => {
    try {
        const resp = getAllItems()
        res.render('rabbits', { rabbits: resp })

    } catch (err) {
        res.status(500).send(err)
    }
})

router.get('/:id', (req, res) => {
    try {
        const resp = getItem(parseInt(req.params.id))
        res.render('rabbit', { rabbit: resp })

    } catch (err) {
        res.status(500).send(err)
    }
})

router.put('/:id', jsonParser, (req, res) => {
    try {
        const resp = editItem(req.params.id, req.body.item)
        res.render('editRabbit', { rabbit: resp })

    } catch (err) {
        res.status(500).send(err)
    }
})

router.post('/', jsonParser, (req, res) => {
    try {
        const resp = addItem(req.body.item)
        res.render('addRabbit', { rabbits: resp })

    } catch (err) {
        res.status(500).send(err)
    }
})

router.delete('/:id', (req, res) => {
    try {
        const resp = deleteItem(req.params.idx)
        res.render('deleteRabbit', { rabbits: resp })

    } catch (err) {
        res.status(500).send(err)
    }
})

module.exports = router
```

* Enfin, dans les fichiers de vue, nous prenons la variable reçue en tant que paramètre et la rendons en HTML.
    

```plaintext
<!-- Rabbits view -->
<!DOCTYPE html>
<html lang="en">
    <body>
        <header>All rabbits</header>
        <main>
            <ul>
                <% rabbits.forEach(function(rabbit) { %>
                    <li>
                        Id: <%= rabbit.id %>
                        Name: <%= rabbit.name %>
                    </li>
                <% }) %>
            </ul>
        </main>
    </body>
</html>
```

```plaintext
<!-- Rabbit view -->
<!DOCTYPE html>
<html lang="en">
    <body>
        <header>Rabbit view</header>
        <main>
                <p>
                    Id: <%= rabbit.id %>
                    Name: <%= rabbit.name %>
                </p>
        </main>
    </body>
</html>
```

Maintenant, nous pouvons aller dans notre navigateur, taper [`http://localhost:7070/rabbits`](http://localhost:7070/rabbits) et obtenir :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-232.png align="left")

Ou `[http://localhost:7070/rabbits](http://localhost:7070/rabbits)/2` et obtenir :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-233.png align="left")

Et c'est MVC !

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bugs-bunny-looney-tunes.gif align="left")

# Conclusion

J'espère que tous ces exemples vous ont aidé à comprendre de quoi nous parlons lorsque nous mentionnons "architecture" dans le monde du logiciel.

Comme je l'ai dit au début, c'est un sujet vaste et complexe qui englobe souvent beaucoup de choses différentes.

Ici, nous avons introduit des modèles et systèmes d'infrastructure, des options d'hébergement et des fournisseurs de cloud, et enfin quelques structures de dossiers courantes et utiles que vous pouvez utiliser dans vos projets.

Nous avons appris sur la mise à l'échelle verticale et horizontale, les applications monolithiques et les microservices, le cloud computing élastique et serverless... beaucoup de choses. Mais ce n'est que la partie émergée de l'iceberg ! Alors continuez à apprendre et à faire des recherches par vous-même. 💪💪

Comme toujours, j'espère que vous avez apprécié le manuel et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

Et [voici une petite chanson d'au revoir](https://www.youtube.com/watch?v=PDilu87kQCk) pour vous, parce que... pourquoi pas ? 🤷🏻💂🏻

![Image](https://www.freecodecamp.org/news/content/images/2022/07/7zSe.gif align="left")

Santé et à la prochaine ! 👌🏻