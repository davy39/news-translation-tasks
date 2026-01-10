---
title: Qu'est-ce que le Cloud-Native ? Et comment le rendre rapide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-14T20:14:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-cloud-native-system-performance
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/jeshoots-com-sMKUYIasyDM-unsplash.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud Solutions
  slug: cloud-solutions
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: Qu'est-ce que le Cloud-Native ? Et comment le rendre rapide
seo_desc: 'By Sumeet Ninawe

  Web applications are built to provide various online services to end-users. Developing
  and hosting these services involves hard work and talent. And it all begins with
  an idea.

  But imagine, after putting in all that hard work, users ...'
---

Par Sumeet Ninawe

Les applications web sont conçues pour fournir divers services en ligne aux utilisateurs finaux. Le développement et l'hébergement de ces services nécessitent du travail acharné et du talent. Et tout commence avec une idée.

Mais imaginez, après avoir mis tout ce travail acharné, les utilisateurs grincent des dents concernant la performance du système – « C'est trop lent... », « J'aimerais obtenir la réponse dans cette vie... », « Le produit est bon, mais ça ne vaut pas la peine d'attendre... » et ainsi de suite.

D'un autre côté, si vous décidez de fournir à vos utilisateurs la meilleure performance mais que votre système est mal architecturé, alors vos coûts d'infrastructure peuvent s'envoler.

Dans cet article, nous verrons comment faire les bons compromis compte.

Pensez à un concert de musique. Tout le monde est là, attendant de profiter de leurs actes préférés en direct. Il y a tant de paramètres audio associés à chaque ligne d'entrée et de sortie qui circule sur la scène, et ceux-ci doivent être réglés à un niveau optimal.

Faire exploser tout à son niveau maximum ferait fuir les gens du concert. Bien sûr, ce n'est pas la faute de l'artiste – mais de l'ingénieur du son dont le travail est de faire sonner l'artiste au mieux.

Après tout, c'est un système de production – similaire aux environnements de production IT. En IT, gérer la performance du système signifie essentiellement bien gérer les compromis. Bien sûr, il y a des choix clairs, mais parfois, faire ces choix simples n'est pas si évident.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Basic-Web-Arch.png)
_Conception d'infrastructure d'application web de base_

## Qu'est-ce que le Cloud-Native ?

Déployer des applications et services métiers sur des centres de données gérés, également connus sous le nom de cloud, est une tendance de longue date dans l'industrie IT. Cela est principalement dû au fait que le cloud offre de nombreux avantages et expertises tout en proposant des centres de données en tant que service.

Les défis de sécurité, de réglementation et d'exploitation existent toujours, donc les organisations sont encore à la traîne en ce qui concerne le déplacement de 100 % de leurs charges de travail vers le cloud. D'un autre côté, les startups optent pour le déploiement pro-cloud car il est beaucoup plus facile de faire gérer votre infrastructure par les plateformes cloud dès le premier jour.

Mais que signifie cloud-native ? Vous pouvez penser que le simple fait de déplacer vos charges de travail vers le cloud vous aidera à tirer le maximum de bénéfices. C'est partiellement vrai, puisque il y a des étapes dans l'adoption du cloud. Les fournisseurs de cloud offrent de nombreux services d'infrastructure riches, et lorsqu'ils sont utilisés correctement, ils peuvent réduire considérablement vos coûts d'infrastructure IT.

Le terme « cloud-native » indique le degré d'adoption du cloud dans une organisation. Vous avez peut-être rencontré des projets de migration cloud exécutés par des organisations où elles déplacent leurs charges de travail des serveurs matériels sur site vers des VM dans le cloud. Cela est utile, car elles bénéficient de se débarrasser de l'effort nécessaire pour maintenir elles-mêmes les centres de données – mais la situation pourrait encore être meilleure.

Le simple fait de déplacer et de transférer des charges de travail n'est pas très intelligent et n'est pas cloud-native. Les plateformes cloud offrent de nombreux autres services comme des registres de conteneurs, des solutions de gestion de clusters, des services DevOps, Serverless/Function-as-a-Service, et ainsi de suite. Ensemble, ceux-ci donnent de meilleurs résultats – en termes de tout, comme le coût, la performance, la maintenance, la flexibilité, la fiabilité, la sécurité, et ainsi de suite.

La notion de devenir cloud-native signifie adopter autant de services fournis par les fournisseurs de cloud que vous êtes capable, et aligner ou refactoriser vos charges de travail pour être déployées sur le cloud de la manière la plus bénéfique.

Avec cela en tête, voyons comment l'adoption du cloud-native peut vous aider à améliorer la performance de vos systèmes.

## Comment améliorer la performance de votre système

En ce qui concerne l'architecture de tout système IT, la performance est l'un des aspects clés. Nous pouvons classer les sujets de performance discutés ci-dessous en trois grandes catégories – calcul, stockage et mémoire, et réseau. Une telle catégorisation nous aide à examiner le système sous divers angles, et à isoler les problèmes.

### 1. Partitionnement des charges de travail

_Catégorie : Calcul_

Vous êtes peut-être conscient que les architectures monolithiques représentent un point unique de défaillance. La probabilité que l'ensemble du système tombe en panne est élevée, même en raison de problèmes triviaux.

L'émergence de l'architecture de microservices a aidé à résoudre ce problème, mais cela dépend aussi de la manière dont ces microservices sont conçus.

Lors de la refactorisation d'un monolithe en microservices, vous devez suivre le principe de responsabilité unique. Construisez un microservice pour un seul but, et déployez plusieurs instances de microservices critiques en mode auto-scaling pour éviter la baisse de performance.

Ce type de partitionnement des charges de travail aide à traiter les problèmes de manière isolée, réduisant le risque de défaillances.

L'un des premiers services offerts par les fournisseurs de cloud était peut-être la capacité de lancer des machines virtuelles selon les besoins. Nous pouvons choisir la version de l'OS, la taille, le réseau, et divers autres aspects. Utilisez cette flexibilité pour déployer des charges de travail partitionnées.

Allant plus loin, vous pouvez isoler les exigences d'exécution pour les services en utilisant la conteneurisation. Cela pourrait être les ressources OS, le CPU, la bande passante réseau, la mémoire, et ainsi de suite, où le quota peut être prédéfini. Cela permet une allocation de ressources partagée mais dédiée, brisant ainsi la règle d'une application, un serveur.

Lorsque les charges de travail sont conteneurisées, cela fournit une base système solide qui garantit sa performance sur tout système prenant en charge l'exécution de charges de travail conteneurisées – indépendamment du matériel ou de l'OS.

Les fournisseurs de cloud offrent également des services d'orchestration de conteneurs (par exemple Kubernetes), facilitant le déploiement, le débogage et la publication de nouvelles versions d'applications sans temps d'arrêt. L'utilisation de ces services et une stratégie de déploiement judicieuse peuvent aider à lancer de nouvelles fonctionnalités sans aucun retard ou problème dans l'expérience utilisateur.

Je veux souligner que vous devez diviser vos applications en microservices et héberger chaque service sur une infrastructure isolée. Cela évite beaucoup d'interférences inter-processus et de contentions de ressources, optimisant ainsi la consommation de ressources pour la performance.

### 2. Optimisation du calcul

_Catégorie : Calcul_

Chaque application a des besoins différents. Les VM standard offrent tout ce qui est requis dans un serveur polyvalent – CPU, mémoire et capacités de réseau.

Cependant, toutes les applications exécutées sur ces VM ne suivent pas une norme en ce qui concerne la consommation de ressources. Les applications ou les composants de microservices sont orientés vers un but, de manière à avoir des besoins de calcul différents.

Un serveur frontal peut dépendre davantage des capacités de réseau par rapport à ses exigences de calcul ou de mémoire. Un microservice traitant des activités de transformation de grandes données peut avoir besoin d'une meilleure solution de gestion de la mémoire pour accéder à la mémoire et effectuer des transactions.

Les principaux fournisseurs de cloud offrent des fonctionnalités pour optimiser les ressources virtuelles – en particulier les VM et les bases de données – pour les aligner sur les besoins de l'application. En général, ces optimisations peuvent être classées en trois groupes :

1. Optimisé pour le calcul
2. Optimisé pour la mémoire
3. Optimisé pour le stockage

En fonction de la criticité des applications, il existe des options qui vous aident à optimiser les coûts. Vous devez simplement choisir le plan tarifaire approprié et ensuite faire un compromis entre la disponibilité des applications critiques et les avantages en termes de coûts.

Les serveurs virtuels optimisés sont sélectionnés en fonction de leurs objectifs :

1. Le traitement par lots, les charges de travail de transformation de données lourdes et les algorithmes de ML ont généralement besoin de processeurs haute performance étant donné leurs tâches intensives en calcul. Choisissez de provisionner des instances optimisées pour la mémoire à cette fin. Les instances optimisées pour le calcul sont provisionnées avec un stockage par blocs et fichiers amélioré, ainsi qu'une bande passante réseau élargie. Cela aide à obtenir la meilleure performance pour traiter les charges de travail orientées données.
2. Si votre application doit fournir une performance réseau élevée pour transférer de grands volumes de données et servir un grand volume de requêtes, il est important de choisir le bon matériel réseau associé à une VM provisionnée. Dans ce cas, vous pouvez choisir d'optimiser la performance réseau en optant pour une carte d'interface réseau haute performance.
3. Les volumes basés sur SSD sont utilisés pour aider la performance du CPU si le traitement nécessite plusieurs transactions sur la mémoire. Une VM optimisée pour le stockage aide avec des opérations d'E/S plus rapides, et elle est réglée pour un débit élevé. Comparé à l'utilisation d'une VM polyvalente, les VM optimisées pour le stockage offrent une meilleure performance.

Il est important d'analyser les exigences du système pour une charge de travail donnée. Une configuration équilibrée offerte par les VM polyvalentes peut simplement entraîner des coûts plus élevés sans amélioration significative de la performance. Vous pouvez faire un choix judicieux en regardant les types de VM qui peuvent être provisionnées.

### 3. Mise à l'échelle

_Catégorie : Calcul_

Il existe 2 types de mise à l'échelle :

1. Mise à l'échelle verticale – où les ressources de calcul virtuelles augmentent en taille.
2. Mise à l'échelle horizontale – où elles augmentent en nombre.

Dans le monde cloud-native, les deux options sont disponibles. Étant donné la nature de la sélection de taille par modèle – la mise à l'échelle verticale des ressources n'est pas toujours le meilleur cas, car les applications peuvent rencontrer des goulots d'étranglement dans l'un des aspects. Augmenter la taille de tout dans une VM pour résoudre un seul goulot d'étranglement crée des ressources sous-utilisées. Cela ajoute simplement aux coûts.

De plus, la mise à l'échelle verticale signifie également que nous mettons à l'échelle un point unique de défaillance. La meilleure option serait de mettre à l'échelle horizontalement en nombre. De cette manière, même si un nœud tombe en panne, il en reste d'autres pour servir les utilisateurs et éviter des pertes potentielles.

Les fournisseurs de cloud offrent une fonctionnalité d'auto-scaling qui vous permet d'être sûr que autant d'instances que nécessaire sont toujours en cours d'exécution, même si certaines d'entre elles tombent en panne entre-temps. Cela se fait automatiquement.

Mais cela ne signifie pas qu'il n'y a aucune raison de s'inquiéter des défaillances de nœuds. Idéalement, les nœuds ne devraient pas tomber en panne du tout, et l'auto-scaling ne fournit qu'un mécanisme de secours comme tentative de récupération de la perte. Cela est en soi une vertu.

Allant plus loin, les capacités de Kubernetes fournies par les plateformes cloud-native ajoutent un niveau supplémentaire de personnalisation de l'allocation des ressources. Du point de vue du calcul, cela signifie que nous avons de meilleures façons de gérer les goulots d'étranglement.

### 4. Serverless

_Catégorie : Calcul_

Allant au-delà des conteneurs – si vous ne voulez pas vous soucier des analyses de vulnérabilité dans les images utilisées, de la gestion de cluster, de l'OS et de l'orchestration, et que vous voulez simplement écrire le code et le laisser s'exécuter, alors le serverless est une excellente option.

Dans les services serverless offerts par les fournisseurs de cloud, vous êtes seulement censé écrire des « fonctions » qui définissent la logique de votre application hébergée. Toute l'infrastructure nécessaire pour exécuter ces fonctions est abstraite par les plateformes des fournisseurs de cloud.

Outre les énormes avantages en termes de coûts offerts par le serverless (sujet pour un autre jour), le développement d'applications sur le framework serverless est la chose la plus proche du cloud-native. Plus vous êtes cloud-native, plus vous pouvez tirer parti de services.

Il convient de noter que le serverless ne signifie pas simplement écrire du code. Les fournisseurs de cloud peuvent seulement fournir un endroit pour exécuter la requête entrante. La manière dont cette requête est traitée et routée vers les files d'attente et les API appropriées nécessite l'utilisation de services supplémentaires.

Cependant, la refactorisation des applications existantes nécessite d'énormes efforts, c'est là que la conteneurisation est une option plus facile pour commencer. Les applications, en particulier les services web à développer à partir de zéro, sont souvent de bons candidats pour le serverless.

### 5. Partitionnement de la base de données

_Catégorie : Mémoire et base de données_

Le partitionnement d'une base de données offre un avantage clair sur la performance. Pensez-y comme une classification de haut niveau des données elles-mêmes qui sont stockées en grands volumes.

Lorsqu'une requête est exécutée contre ces volumes, il est probable que l'ensemble de la base de données ou le volume de stockage soit scanné pour récupérer les données demandées. Le partitionnement réduit la portée de ce scan, améliorant ainsi le temps de réponse. Une bonne stratégie de partitionnement est définie en fonction des données stockées elles-mêmes.

Par exemple, un archive de tous les journaux de l'année 2000 peut être partitionné en fonction de l'année, et ensuite partitionné en fonction du mois, et ainsi de suite. Donc si vous connaissez le nom et la date du journal que vous souhaitez lire, il sera plus facile de le trouver dans les archives.

Les plateformes cloud fournissent divers services en ce qui concerne le partitionnement des données. Contrairement aux méthodes traditionnelles, tous les besoins de partitionnement sont gérés par la plateforme elle-même une fois configurés. Donc envisagez de partitionner les données.

### 6. Mise en cache dynamique des données

_Catégorie : Mémoire et base de données_

Les applications web servent plusieurs requêtes en parallèle. Ces requêtes peuvent nécessiter la lecture des données à partir de la base de données. Si les données sont lues fréquemment, chaque requête devrait se connecter à la base de données, les lire et les rendre disponibles pour la couche métier.

Si les données lues sont les mêmes, il serait logique de les stocker dans un cache pour un accès plus rapide. Cela évite les allers-retours inutiles, coûteux et fréquents vers la couche de base de données.

Dans un environnement multi-nœuds, chaque nœud peut mettre en cache sa propre copie des données. Bien que cela améliore les performances, cela crée également plusieurs copies des mêmes données sur plusieurs nœuds, ce qui est encore très inefficace.

L'une des solutions de contournement consiste à imposer l'affinité client, ce qui garantit qu'une requête particulière est toujours servie par le même nœud dans le cluster. Si le nœud est occupé, cela introduit une latence supplémentaire et avoir plusieurs nœuds dans le cluster ne sert pas le but.

C'est là que les bases de données de cache partagé entrent en jeu. Redis et memcached sont les bases de données de cache partagé les plus utilisées, qui sont utilisées dans l'architecture backend de nombreuses applications web.

Les bases de données de cache partagé ne sont pas le remplacement des bases de données – elles aident à stocker des données pour une récupération rapide des données temporaires. Elles sont généralement hébergées entre les nœuds de logique métier et la base de données.

Les bases de données de cache partagé aident à consolider les transactions de base de données et à maintenir l'état de la base de données cohérent. Une fois installées et configurées, vous pouvez les utiliser pour définir et obtenir des valeurs. Ainsi, au lieu de maintenir la copie spécifique au nœud des données, l'utilisation d'une base de données de cache partagé aide à garder les données, une fois stockées, disponibles pour tous les nœuds.

Les fournisseurs de cloud offrent un support, des solutions et des services pour héberger Redis et memcached afin d'améliorer la performance des systèmes.

### 7. Considérer la cohérence éventuelle

_Catégorie : Mémoire et base de données_

En termes de bases de données, la cohérence définit si les lectures immédiates sont à jour avec les dernières informations écrites. Les applications qui effectuent de nombreuses tâches d'E/S vers les bases de données ont tendance à utiliser des mécanismes de verrouillage pour s'assurer que plusieurs écritures prévues se produisent de manière cohérente.

Cependant, lorsque de telles données fréquemment changeantes sont lues, surtout lorsque plusieurs lectures sont autorisées, les données peuvent soit être cohérentes avec la dernière écriture, soit non.

Lorsque plusieurs lecteurs sont activés, dans certains cas, la base de données est également répliquée pour avoir une copie en temps réel ou quasi en temps réel de la base de données principale (dont le but est de servir toutes les requêtes de lecture).

Dans de tels cas, si vous avez besoin de cohérence, cela ajoute à la latence de performance, car toutes les opérations de lecture doivent être suspendues jusqu'à ce que les opérations d'écriture soient répliquées sur toutes les copies de la base de données.

Lorsque vous développez des services critiques pour l'entreprise, les bases de données relationnelles distribuées qui ont une conformité/garantie ACID peuvent entraîner un système plutôt plus lent.

La cohérence éventuelle est une fonctionnalité principalement offerte par les bases de données NoSQL et Document. La cohérence éventuelle est une garantie que les données qui sont lues et affichées à l'utilisateur sont à jour avec la dernière écriture et seront mises à jour dans la base de données.

Les fournisseurs de cloud offrent des services de bases de données NoSQL et Document qui offrent également une cohérence éventuelle. Améliorer la performance du système en activant la cohérence éventuelle et en protégeant simultanément l'intégrité des données est un défi qui nécessite une solution globale.

Identifiez les cas où vous pouvez tirer parti de la cohérence éventuelle et développez des routines et des transactions pour soutenir l'intégrité des données de bout en bout. Cela aidera à améliorer la performance. Les solutions cloud-native offrent cette capacité, et la cohérence éventuelle aide également à optimiser les coûts.

### 8. Tirer parti du réseau dorsal

_Catégorie : Réseau_

En ce qui concerne le réseau, les plateformes Cloud-Native bien établies disposent de centres de données et de fermes de serveurs dans divers endroits répartis dans le monde. Peu importe d'où provient le trafic – il est probable que ces fournisseurs de cloud disposent d'un centre de données disponible à proximité.

Ces centres de données sont connectés avec un réseau dorsal qui est également développé par les fournisseurs de cloud et dédié à leur communication interrégionale. C'est un grand avantage. Si les utilisateurs de l'application vivent sur plusieurs continents, le déploiement d'applications sur le cloud accélère intrinsèquement la livraison de vos services grâce à ces réseaux dorsaux.

Puisque c'est un réseau mondial prenant en charge tous les services, l'hébergement d'applications cloud-native peut être servi plus près des utilisateurs, quel que soit leur continent ou leur pays.

Des connexions directes et dédiées et des VPN sont également utilisés pour connecter de manière sécurisée les centres de données sur site ou privés à l'infrastructure cloud sous forme de points d'accès. D'une certaine manière, l'établissement de ces connexions aide à intégrer le réseau des organisations sur ce réseau dorsal, les aidant à atteindre leurs employés à travers le monde.

### 9. Mise en cache de la passerelle API

_Catégorie : Réseau_

Comme pour les autres services, les fournisseurs de cloud fournissent des services pour héberger et configurer des passerelles API pour vos applications. Aujourd'hui, les API sont le premier choix d'interface pour toute application web.

Les passerelles API n'aident pas seulement à développer ces chemins API, elles sont également intégrées de manière transparente avec d'autres services liés au calcul, au stockage, aux bases de données, aux fonctions, aux conteneurs, aux orchestrations, aux files d'attente, et ainsi de suite. L'interface Web riche facilite la configuration des passerelles API et la maintenance des versions.

Puisque les API traitent de l'envoi et de la réception de données de charge utile, il existe plusieurs fonctionnalités préconstruites qui aident au formatage, au codage et à la sécurité des charges utiles. Puisque ces fonctionnalités avancées sont préconstruites dans ces services de passerelle API, les efforts nécessaires pour les configurer pour une livraison optimale sont faibles.

Vous pouvez tirer parti de ces fonctionnalités pour la compression automatique, la décompression, classer et router les requêtes vers le service cible, activer le cache pour améliorer la latence de la réponse de l'application.

### 10. CDN

_Catégorie : Réseau_

Étant donné que les fournisseurs de cloud offrent leur propre réseau dorsal qui transporte le trafic dédié entre leurs centres de données, il devient très pratique pour eux de fournir également des services CDN.

Les principales plateformes cloud offrent des services CDN qui donnent de très bons résultats en ce qui concerne la livraison de contenu de données statiques. Les applications web servies aux utilisateurs via un navigateur web utilisent typiquement des fichiers HTML, CSS, JS pour construire l'interface utilisateur interactive. Ces fichiers sont assez statiques et ne changent pas très fréquemment.

Lors du déploiement d'applications sur des plateformes cloud, il est logique de tirer parti des services CDN pour améliorer la performance réseau de ces applications.

## Conclusion

Lorsque nous parlons d'optimiser la performance du système cloud-native, de nombreux autres facteurs sont impliqués. Il est important de penser au système en utilisant divers angles – calcul, stockage, bases de données et réseau – et d'identifier les goulots d'étranglement en effectuant divers tests de charge et de stress.

La surveillance est une fonctionnalité importante que de nombreuses grandes entreprises cloud fournissent, et elle est bien intégrée avec d'autres services. Utilisez ces capacités de surveillance pour analyser les goulots d'étranglement de performance et identifier des éléments d'action efficaces pour le changement.

J'ai couvert les défis et les approches avec des insights plus profonds dans mon [eBook GRATUIT](https://www.letsdotech.dev/resources/ebook-cloud-native-system-performance/) publié sur mon site web [Let's Do Tech](https://letsdotech.dev). Si vous êtes intéressé à suivre plus de choses architecturales, restez à l'affût. Réseaux sociaux : [Instagram](https://www.instagram.com/letsdotech/), [Twitter](https://twitter.com/letsdotech_dev), [LinkedIn](https://www.linkedin.com/company/letsdotech), [FB](https://www.facebook.com/ldtmavens).