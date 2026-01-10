---
title: Qu'est-ce qu'un serveur DNS ? Explication des serveurs DNS
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-07T21:49:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-dns-server
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/christina-wocintechchat-com-glRqyWJgUeY-unsplash--1-.jpg
tags:
- name: Network Engineering
  slug: network-engineering
- name: Security
  slug: security
seo_title: Qu'est-ce qu'un serveur DNS ? Explication des serveurs DNS
seo_desc: 'The web would not work at all without DNS servers. They are responsible
  for translating domain names into IP addresses. Then computers use those IP addresses
  to locate and connect to web servers, and send users to the right websites.

  Many people firs...'
---

Le web ne fonctionnerait pas du tout sans les serveurs DNS. Ils sont responsables de la traduction des noms de domaine en adresses IP. Ensuite, les ordinateurs utilisent ces adresses IP pour localiser et se connecter aux serveurs web, et envoyer les utilisateurs vers les bons sites web.

De nombreuses personnes ont découvert le système DNS pour la première fois en octobre 2021, lorsque toutes les applications et sites web de Facebook sont tombés en panne en même temps, en raison d'une mauvaise configuration catastrophique du DNS.

### Qu'est-ce qu'une adresse IP ?

Une adresse IP est un identifiant unique pour un appareil sur un réseau. Elles sont utilisées pour acheminer le trafic vers le bon appareil sur un réseau. 

L'adresse IP principale de google.com, par exemple, est 172.217.165.14. 

Les adresses IP peuvent être difficiles à retenir. Surtout si elles sont longues et compliquées. Les noms lisibles par l'homme sont beaucoup plus faciles à retenir. 

## Quels sont les principaux types de serveurs DNS ?

Il existe de nombreux types de serveurs DNS, chacun avec ses propres capacités uniques.

Le type de serveur DNS le plus courant est le serveur DNS récursif. Celui-ci est responsable de l'exécution des recherches DNS pour le compte de ses clients.

### Comment fonctionnent les serveurs DNS récursifs

Un client – généralement un navigateur web – envoie une requête DNS (quelle est l'adresse IP de ce nom de domaine ?) à un serveur DNS récursif. Ce serveur résout la requête, puis renvoie la réponse au client.

Les serveurs DNS récursifs sont généralement gérés par les fournisseurs de services Internet (FAI). Ce sont les entreprises auxquelles vous payez votre accès Internet chaque mois.

### Comment fonctionnent les serveurs DNS autoritaires

Un autre type de serveur DNS est le serveur DNS autoritaire. Ceux-ci sont responsables du stockage des enregistrements DNS pour un domaine. Ils contiennent une base de données d'adresses IP publiques et de noms d'hôtes correspondants. 

Les serveurs DNS autoritaires sont responsables de la traduction des noms de domaine en adresses IP. Cela permet aux utilisateurs d'accéder aux sites web en utilisant des noms de domaine au lieu d'adresses IP.

Les serveurs DNS autoritaires sont généralement fournis par les registraires de domaines. 

### Quelles sont les façons de configurer un serveur DNS ?

Vous pouvez configurer un serveur DNS en utilisant l'une de ces approches :

* **Serveurs d'adresses IP statiques** – adresses IP permanentes qui ont été attribuées à des ordinateurs spécifiques. Les adresses IP statiques sont idéales pour les ordinateurs qui doivent être accessibles à tout moment – comme les serveurs.
* **Serveurs d'adresses IP dynamiques** – ceux-ci sont utiles lorsque les appareils ne sont pas connectés en permanence au réseau (comme avec les réseaux Wi-Fi publics). Vous pouvez également les utiliser pour équilibrer le trafic réseau, ou attribuer des adresses IP temporaires aux appareils qui ne se connectent que rarement au réseau.
* **Serveurs Round Robin** – ceux-ci résolvent les noms de domaine en retournant une liste d'adresses IP – chacune correspondant à un serveur capable de fournir les informations demandées. Un serveur Round Robin peut distribuer le trafic de manière égale entre un groupe de serveurs. Cela garantit qu'aucun serveur n'est surchargé de requêtes, et que les autres serveurs reçoivent également leur part équitable de trafic.
* **Serveurs d'équilibrage de charge** – ceux-ci déterminent la manière la plus efficace de distribuer les requêtes entre les serveurs. freeCodeCamp.org utilise des serveurs d'équilibrage de charge (également appelés "Load Balancers") et j'imagine que la plupart des grands sites web en font autant.

Vous pouvez également configurer les serveurs DNS pour utiliser différents types de mise en cache, ce qui peut améliorer les performances.

### Qu'est-ce que la mise en cache ?

La mise en cache est une technique où vous stockez les données des requêtes passées dans un emplacement de mémoire temporaire. L'idée est la suivante : si quelqu'un a besoin de ces informations, quelqu'un d'autre en aura probablement besoin également.

Lorsque quelqu'un demande des données à votre serveur, vous pouvez d'abord vérifier si les données sont stockées dans votre cache. Si c'est le cas, vous pouvez les récupérer depuis le cache plutôt que depuis l'emplacement d'origine.

C'est ainsi que fonctionnent les réseaux de diffusion de contenu (CDN). La mise en cache peut considérablement accélérer les performances de votre site web ou service.

## Le DNS change-t-il votre adresse IP ?

Non. Changer de serveurs DNS ne changera pas votre adresse IP.

Les serveurs DNS traduisent les noms de domaine en adresses IP. Par défaut, tous les navigateurs web viennent avec l'option de détecter automatiquement les paramètres DNS de leur réseau actuel.

Ainsi, lorsque vous vous connectez à un réseau privé virtuel (VPN), le serveur DNS de votre VPN remplace le serveur DNS de votre FAI.

## Comment configurer un serveur DNS ?

Si vous souhaitez configurer votre propre serveur DNS pour votre entreprise ou organisation, voici quelques étapes pour commencer :

1. Choisissez le bon logiciel de serveur DNS. Certaines options populaires incluent BIND, ISC DHCP et PowerDNS.
2. Installez le logiciel de serveur DNS sur un serveur dédié. Cela vous aidera à garantir que votre serveur dispose des ressources nécessaires pour fonctionner de manière fiable. Si vous utilisez le cloud, vous n'aurez pas à vous soucier autant d'une panne de courant ou d'une panne réseau qui ferait tomber votre DNS.
3. Configurez le logiciel de serveur DNS. Cela inclut la configuration des zones DNS et des enregistrements.
4. Testez le serveur DNS. Une fois qu'il est opérationnel, vous pourriez le tester en simulant du trafic pour vous assurer qu'il ne "tombe pas en panne".

Il existe également de nombreux outils de serveurs DNS hébergés que vous pouvez utiliser, qui devraient fonctionner dès la sortie de la boîte et vous faire gagner du temps. Ceux-ci coûtent un peu d'argent chaque mois, mais nécessitent moins d'expertise pour être supervisés.

## J'espère que vous avez appris beaucoup de choses sur les serveurs DNS.

J'espère que vous avez trouvé cela utile. Si vous souhaitez en apprendre davantage sur la programmation et la technologie, essayez [le programme de codage principal de freeCodeCamp](https://www.freecodecamp.org/learn). C'est gratuit.