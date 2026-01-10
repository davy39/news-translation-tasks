---
title: Une introduction au réseau de diffusion de contenu Akamai
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T16:46:06.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-akamai-content-delivery-network-806aa16d8781
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e-5nwPzNiZtoAIKQOI7VJA.png
tags:
- name: 'content delivery network '
  slug: content-delivery-network
- name: performance
  slug: performance
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Une introduction au réseau de diffusion de contenu Akamai
seo_desc: 'By Dominic Fraser

  Akamai is one of the world’s leading Content Delivery Network (CDN) providers. Through
  the Akamai Intelligent Platform many products are offered to aid performance, availability,
  security, and insight generation.

  Other CDNs include ...'
---

Par Dominic Fraser

Akamai est l'un des principaux fournisseurs de réseaux de diffusion de contenu (CDN) au monde. Grâce à la [plateforme intelligente Akamai](https://www.akamai.com/uk/en/solutions/intelligent-platform/), de nombreux produits sont proposés pour améliorer les performances, la disponibilité, la sécurité et la génération d'informations.

D'autres CDN incluent Cloudflare, Fastly, MaxCDN, Incapsula et Rackspace.

Ici, nous allons examiner ce qu'est un CDN, puis quelques spécificités autour de la mise en œuvre d'Akamai, y compris :

* La plateforme intelligente Akamai et les serveurs Edge
* L'interface Akamai et le Property Manager
* Les performances de routage
* La mise en cache

#### Qu'est-ce qu'un CDN ?

Une demande d'utilisateur pour du contenu sur l'Internet public peut sembler simple, se connecter au serveur hébergeant le contenu (l'origine du contenu) et retourner celui-ci à l'utilisateur, mais elle est en fait très complexe.

![Image](https://cdn-media-1.freecodecamp.org/images/jDQimdgZxgp-yZlV5hA6yO34Of9rEGZdMIRz)
_Complexité cachée de la connexion à l'origine du contenu_

La connexion peut devoir passer par de nombreux fournisseurs de services Internet (FAI), points de peering et centres de données, à travers des réseaux concurrents, et souffrir de l'absence de routes constamment disponibles.

De nombreux types d'appareils et de bandes passantes peuvent être utilisés, depuis différents emplacements mondiaux, avec différents types de contenu demandés.

Cela peut entraîner des fluctuations de vitesse et de disponibilité, des défis de sécurité et peu de visibilité sur ce qui se passe entre l'utilisateur et l'origine du contenu.

Un CDN place plus de contrôle entre les mains du fournisseur de contenu et aide à améliorer l'expérience de l'utilisateur final.

Il le fait en agissant comme un réseau parallèle haute performance, maintenant son propre réseau de serveurs hautement distribués. En étant dispersés sur de nombreux emplacements physiques et réseau, mais optimisés comme un seul réseau, plus de contrôle et de fiabilité existent pour les demandes des utilisateurs.

À mesure qu'une entreprise se développe, la mise à l'échelle pour répondre à des demandes plus élevées sur l'origine du contenu présente également des défis. Nous examinerons également comment les outils CDN peuvent être utilisés pour réduire la charge sur l'origine, aidant non seulement à améliorer les performances, mais aussi à réduire les coûts en réduisant la mise à l'échelle de l'origine.

#### Plateforme intelligente Akamai

Akamai maintient un réseau mondial de plus de 240 000 serveurs edge. Ceux-ci sont positionnés à la périphérie de l'Internet, aussi près que possible des utilisateurs finaux. Pour y parvenir, de nombreux serveurs edge sont même situés directement dans les FAI, ou dans les tours de données mobiles, pour réduire encore davantage la latence entre la connexion à un FAI d'utilisateur avant de passer dans le réseau Akamai.

![Image](https://cdn-media-1.freecodecamp.org/images/sKkZcR-fGy3yMTUTN8BO3uSawcmz7q6rzjK4)
_Réseau Akamai de serveurs Edge_

Lorsqu'un utilisateur fait une demande, Akamai la mappe dynamiquement au serveur edge le plus proche disponible. Le serveur edge applique les règles commerciales que le fournisseur de contenu a spécifiées, avant d'utiliser la meilleure route disponible entre tous les autres serveurs edge au sein du réseau Akamai pour récupérer le contenu de l'origine. Les règles commerciales sont répliquées sur chaque serveur edge.

Tout contenu disponible et configuré pour être mis en cache est ensuite mis en cache sur le serveur edge pour les demandes futures se connectant à ce nœud. Nous examinerons cela plus en détail plus tard.

Un site est ajouté à Akamai en ajoutant un enregistrement [CNAME](https://medium.freecodecamp.org/why-cant-a-domain-s-root-be-a-cname-8cbab38e5f5c) dans le DNS qui pointe du nom d'hôte, par exemple community.akamai.com, vers un nom d'hôte edge Akamai, community.akamai.com.edgekey.net, où la cartographie des serveurs edge contrôlés par Akamai prend le relais pour attribuer le meilleur serveur edge disponible. Si vous [dig](https://en.wikipedia.org/wiki/Dig_(command)) un nom d'hôte et voyez edgekey.net, alors vous savez qu'Akamai est utilisé par le fournisseur de contenu.

![Image](https://cdn-media-1.freecodecamp.org/images/tGhFH9LxM9izuNJab-6YGfSDfvdwD6weLNCt)
_Entrée dans le réseau Akamai_

#### Interface Akamai

![Image](https://cdn-media-1.freecodecamp.org/images/CFgbmCCeyAd9V9tx7PsMr00nIGHBgiHB4SE1)
_[Luna Control Center](https://www.akamai.com/uk/en/solutions/intelligent-platform/control-center/" rel="noopener" target="_blank" title=") et Property Manager d'Akamai_

Akamai fournit une interface graphique web nommée [Luna Control Center](https://www.akamai.com/uk/en/solutions/intelligent-platform/control-center/), plusieurs [API](https://developer.akamai.com/api/), et un [CLI](https://developer.akamai.com/cli).

Comme vu dans l'onglet _Monitor_, de nombreux outils de reporting et d'analyse sont disponibles pour générer des informations au niveau du CDN. Les journaux des serveurs edge sont également disponibles sur demande.

Dans l'onglet _Configure_, nous nous concentrerons sur l'introduction du Property Manager, et laisserons les autres options pour un futur article.

Une _propriété_, parfois également appelée _configuration_, est le principal moyen de contrôler la manière dont les serveurs edge répondent aux demandes des utilisateurs. Les propriétés appliquent une liste de _règles_ à un ensemble de _noms d'hôte_, et vous ne pouvez appliquer qu'une seule propriété à la fois à un nom d'hôte donné. Les règles sont composées de _critères/conditions de correspondance_ et de _comportements_. Un exemple supplémentaire de cela sera vu plus tard lors de l'examen de la mise en cache. La règle par défaut de chaque propriété doit spécifier un code _Content Provider_ (_CP_) valide pour la facturation et le reporting du service. Les règles sont dernière correspondance gagne.

Une API Property Manager (et un [CLI](https://developer.akamai.com/legacy/cli/packages/property-manager.html)) existe, avec un excellent [glossaire des concepts](https://developer.akamai.com/api/core_features/property_manager/v1.html#papiconcepts).

Lors de la modification d'une propriété, une nouvelle version est d'abord créée, permettant de faire et de tester des modifications tandis que la propriété précédente reste active. La nouvelle version peut d'abord être activée sur le réseau de staging Akamai, qu'un développeur peut pointer sur sa machine locale pour exécuter des tests, avant de l'activer en production. L'activation de production prend environ dix minutes pour déployer globalement la nouvelle version sur tous les serveurs edge, avec une option de retour rapide en arrière en quelques minutes.

#### Performance de routage

En plus de fournir un nombre toujours croissant de serveurs edge distribués, pour pouvoir servir du contenu mis en cache aussi près que possible de chaque utilisateur, la route vers l'origine du contenu peut être optimisée. Dans le cas d'Akamai, cela se fait via [SureRoute](https://developer.akamai.com/legacy/learn/Optimization/SureRoute.html).

![Image](https://cdn-media-1.freecodecamp.org/images/AWcofYrlrbalUfaAe4iWIxe6IIFMHevRE4M8)
_Vue SureRoute des routes possibles vers l'origine du contenu_

Le réseau de serveurs d'Akamai (un utilisateur se connecte d'abord au serveur edge et à tout parent ultérieur de ce serveur) _superpose_ la route par défaut vers l'origine. La route par défaut peut passer entre plusieurs FAI et réseaux différents, qui peuvent ne pas toujours bien s'interconnecter. Comme vu ci-dessus, un lien perte (ou une autre telle dégradation) peut signifier qu'une route non évidente est la meilleure option.

La meilleure route est trouvée en deux étapes.

* Premièrement, les serveurs Akamai exécutent continuellement des sondes les uns contre les autres, et, à un rythme plus faible, contre toutes les origines des clients Akamai. Ceux-ci sont utilisés pour calculer et distribuer une liste centralisée de _routes candidates_ entre chaque paire serveur edge/origine.
* Deuxièmement, pour affiner ces routes candidates brutes en une seule meilleure option, un objet de test _SureRoute statique_ est placé par chaque client à leur origine spécifique de taille similaire à leur contenu moyen attendu. Des _courses_ pour récupérer cet objet sont périodiquement exécutées entre chaque serveur edge et l'origine afin qu'un enregistrement de celui avec la latence la plus faible et/ou le taux de perte de paquets puisse être maintenu à jour.

Cela signifie que sur chaque demande à un serveur edge, la route la plus rapide et la plus fiable à ce moment-là peut être utilisée pour atteindre l'origine.

#### Mise en cache

La mise en cache sur un serveur edge peut grandement réduire la latence pour l'utilisateur final.

À mesure que les organisations se développent, la mise en cache peut également devenir de plus en plus importante pour réduire la charge sur l'origine du contenu, à la fois pour de meilleures performances et pour réduire les coûts.

Comme décrit dans la réponse donnée à [Les serveurs edge Akamai partagent-ils le contenu mis en cache](https://community.akamai.com/customers/s/question/0D50f00005RtpwrCAB/do-akamai-edge-servers-share-cached-content-or-go-to-origin?language=en_US), les serveurs edge sont regroupés en régions réseau. Si le cache d'un serveur edge spécifique n'est pas peuplé, il enverra une demande locale aux autres serveurs edge de sa région et si un pair a du contenu, il servira la réponse avant de le mettre en cache lui-même.

Si tous les caches des pairs locaux sont vides (ou obsolètes), la demande sera transmise au serveur parent de l'edge, où la même vérification locale aura lieu entre les pairs du parent. Si aucun contenu n'est mis en cache le long de l'ensemble du trajet, il retournera à l'origine et repeuplera le cache avec sa réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/cl5Mskcs5NG0c-Cc1MHTY8KrRkjLb3Fmkgv5)
_Comportements de modification de l'ID de cache_

La clé de cache standard utilisée est composée du nom d'hôte (domaine), du chemin et de la chaîne de requête. Cela peut être modifié pour réduire la cardinalité et/ou donner plus de contrôle sur la purge du cache. Cela peut être fait en n'incluant que des paramètres de requête spécifiques, en excluant des éléments tels que les identifiants de produit, en ajoutant les valeurs de certains cookies, en-têtes ou variables définies par l'utilisateur.

Les conditions de correspondance (si le cookie _x_ existe par exemple) peuvent être combinées avec des comportements contourner le cache pour créer des scénarios avancés tels que la mise en cache de différents contenus pour les utilisateurs avec une session, ou pour les utilisateurs dans différents emplacements.

Une extension de navigateur telle que [ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj) peut être utilisée pour afficher les [en-têtes Akamai Pragma](https://community.akamai.com/customers/s/article/Using-Akamai-Pragma-headers-to-investigate-or-troubleshoot-Akamai-content-delivery?language=en_US) pour enquêter sur le comportement de mise en cache localement.

#### Réflexions finales

L'utilisation d'un CDN offre plus de contrôle aux fournisseurs de contenu et des outils tels que ceux décrits ci-dessus fournissent des [avantages](https://www.akamai.com/uk/en/cdn/what-are-the-benefits-of-a-cdn.jsp) qui sont de plus en plus importants lors du travail à grande échelle.

Bien que des produits spécifiques à Akamai aient été discutés ici, des concepts similaires de travail à grande échelle existent avec d'autres fournisseurs de CDN.

D'autres spécificités d'Akamai peuvent être couvertes dans un futur article, n'hésitez pas à [rester à l'affût](https://medium.com/@dfrase) ou à lire les sujets suivants suggérés tels que :

* Améliorations de la sécurité avec la [gestion](https://developer.akamai.com/api/core_features/certificate_provisioning_system/v2.html) des [certificats](https://www.akamai.com/uk/en/solutions/intelligent-platform/secure-cdn.jsp) et les pare-feu d'applications Web ([WAF](https://www.akamai.com/uk/en/resources/waf.jsp))
* [Image manager](https://developer.akamai.com/image-manager) pour une livraison d'images optimisée
* [Cloudlets](https://developer.akamai.com/cloudlets) pour fournir un contrôle granulaire en dehors du cycle d'activation du Property Manager avec de nombreux types disponibles pour différents cas d'utilisation
* Gestion du trafic global ([GTM](https://www.akamai.com/uk/en/products/web-performance/global-traffic-management.jsp)) pour l'équilibrage de charge basé sur le DNS
* [mPulse](https://www.akamai.com/uk/en/products/web-performance/mpulse-real-user-monitoring.jsp) pour utiliser les métriques des utilisateurs réels (RUM) pour la surveillance des performances

Merci d'avoir lu ?

Vous pourriez également aimer :

* [Un guide pour débutants sur le service de conteneurs élastiques d'Amazon](https://medium.com/p/807d8c4960fd?source=user_profile---------11------------------)
* [Comment ajouter progressivement Flow à une application React existante](https://medium.freecodecamp.org/incrementally-add-flow-type-checking-react-261fee015f80)
* [Amélioration progressive avec CSS Grid](https://medium.freecodecamp.org/progressive-enhancement-with-css-grid-8138d4c7508c)