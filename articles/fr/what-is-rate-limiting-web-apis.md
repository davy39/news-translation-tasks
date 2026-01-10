---
title: Qu'est-ce que le Rate Limiting ? Explorer le rôle du Rate Limiting dans la
  protection des API Web contre les attaques
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-09-04T16:03:10.277Z'
originalURL: https://freecodecamp.org/news/what-is-rate-limiting-web-apis
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725036062594/0efa7e12-c5d5-410f-ad9c-ec6a67a31f7c.jpeg
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: Security
  slug: security
- name: APIs
  slug: apis
- name: Backend Development
  slug: backend-development
seo_title: Qu'est-ce que le Rate Limiting ? Explorer le rôle du Rate Limiting dans
  la protection des API Web contre les attaques
seo_desc: 'Back-end servers are the powerhouse of modern-day applications; hence,
  a high level of expertise goes into building them. However, it''s important to ensure
  that these back-end servers are well-secured from bad actors (hackers, phishers).

  These bad el...'
---

Les serveurs back-end sont le moteur des applications modernes ; par conséquent, un haut niveau d'expertise est nécessaire pour les construire. Cependant, il est crucial de s'assurer que ces serveurs back-end sont bien protégés contre les acteurs malveillants (hackers, phishers).

Ces éléments néfastes accèdent aux serveurs back-end via des points vulnérables dans les passerelles pour faire des ravages, voler des informations pertinentes et affecter négativement les performances et l'efficacité des applications via diverses formes d'attaques d'API telles que les injections SQL et non-SQL, les attaques par déni de service distribué (DDoS), les malwares de code et d'autres méthodes pour exploiter les vulnérabilités.

Dans cet article, je me concentrerai sur le Rate Limiting, une technique importante qui aide à protéger l'API back-end contre l'exploitation par des hackers via l'utilisation de DDoS, d'attaques par force brute (Brute-force) et d'autres activités malveillantes connexes. Mais tout d'abord, que signifie le Rate Limiting ?

## Table des matières

1. [Qu'est-ce que le Rate Limiting ?](#heading-quest-ce-que-le-rate-limiting)
    
2. [Importance du Rate Limiting](#heading-importance-du-rate-limiting)
    
3. [Adoption et utilisation du Rate Limiting par des sites populaires](#heading-adoption-et-utilisation-du-rate-limiting-par-des-sites-populaires)
    
4. [Autres cas d'utilisation réels du Rate Limiting d'API](#heading-autres-cas-dutilisation-reels-du-rate-limiting-dapi)
    
5. [Comment fonctionne le Rate Limiting ?](#heading-comment-fonctionne-le-rate-limiting)
    
6. [Exemples d'algorithmes de Rate Limiting](#heading-exemples-dalgorithmes-de-rate-limiting)
    
7. [Bonnes pratiques du Rate Limiting](#heading-bonnes-pratiques-du-rate-limiting)
    
8. [Conclusion](#heading-conclusion)
    

## Qu'est-ce que le Rate Limiting ?

Le Rate Limiting est un mécanisme mis en place pour réguler la fréquence des requêtes effectuées par un client vers le serveur back-end. Il empêche la répétition d'une requête client dans un intervalle de temps défini.

Pourquoi devons-nous implémenter le Rate Limiting dans le développement d'API ? Nous en discuterons dans la section suivante.

## Importance du Rate Limiting

Voici quelques-unes des raisons pour lesquelles le Rate Limiting est utilisé dans le développement d'applications back-end.

### Attaques DDoS

Tout d'abord, il sert de mesure préventive pour atténuer les attaques DDoS. Les attaques DDoS sont des attaques malveillantes sur les serveurs qui consistent à inonder les points de terminaison du serveur avec de multiples requêtes, souvent des millions, entraînant une réduction de l'efficacité du serveur et une interruption des fonctions de celui-ci. Dans la plupart des cas, elles se produisent à l'aide de bots automatisés.

Ces attaques peuvent être volumétriques, basées sur le protocole ou sur la couche applicative. Un exemple clé de cette forme d'attaque s'est produit sur le site Web GitHub en 2018.

### Web Scraping

Le Rate Limiting joue également un rôle dans la protection des applications Web et des serveurs Web contre les scrapers et les crawlers Web non autorisés. Ces outils, également automatisés, émettent généralement des requêtes continuellement pour collecter des données de site Web pertinentes qui peuvent être exposées à des personnes non autorisées. Avoir un bon Rate Limiter en place aide à prévenir tout cela.

### Attaque par force brute (Brute Force Attack)

Cela consiste à tenter d'accéder aux ressources d'un serveur en essayant toutes les configurations possibles pour obtenir l'accès à la ressource. Cela peut être fait manuellement, mais c'est principalement automatisé avec l'utilisation de bots car c'est gourmand en ressources. Le Rate Limiting s'avère également efficace pour prévenir ces formes d'attaques en désactivant les requêtes si elles dépassent le nombre requis de requêtes dans un délai spécifique.

### Optimisation des ressources

Les requêtes au serveur coûtent généralement aux propriétaires d'API des dépenses en termes de coûts de fonctionnement et de maintenance. Avoir un Rate Limiter en place aide à réguler le nombre de requêtes que le serveur peut traiter, aide à conserver les coûts et à maximiser l'efficacité. Par la suite, nous mettrons en évidence certains algorithmes sur lesquels les Rate Limiters sont basés.

## Adoption et utilisation du Rate Limiting par des sites populaires

Le Rate Limiting en tant que mesure de sécurité a été adopté par de nombreux produits technologiques, allant des applications à grande échelle aux applications à petite échelle. Par exemple, Twitter (X) dispose d'une fonctionnalité de Rate Limiting implémentée dans les interfaces de programmation d'applications qu'ils fournissent aux développeurs.

Ces interfaces permettent d'accéder à l'extension d'inscription de Twitter et à d'autres fonctionnalités mises à disposition par Twitter. Pour garantir le bon fonctionnement de ces interfaces, Twitter a imposé un Rate Limiting de 50 publications de tweets par utilisateur toutes les 24 heures. Plus de détails à ce sujet peuvent être trouvés [ici](https://developer.twitter.com/en/docs/twitter-api/rate-limits).

## Autres cas d'utilisation réels du Rate Limiting d'API

L'utilisation d'une interface de programmation d'application ne se limite pas seulement à ce que des sites populaires comme Twitter en font. Voici quelques autres applications réelles du Rate Limiting dans le monde d'aujourd'hui.

### Réduire l'incidence du spamming

[Une étude](https://www.emailtooltester.com/en/blog/spam-statistics/#:~:text=Survey%20Methodology-,Key%20statistics,spam%20messages%20in%20some%20form.) révèle que plus de 160 milliards d'e-mails de spam sont envoyés quotidiennement. Par conséquent, cela a incité à la mise en œuvre du Rate Limiting pour freiner la propagation de messages non sollicités et de contenus indésirables via les plateformes de messagerie et d'e-mailing sur une plage horaire spécifique. Ce faisant, cela encourage une utilisation responsable de ces plateformes.

### Lutter contre les activités frauduleuses

Le Rate Limiting est actuellement implémenté dans les applications Web pour aider à détecter les activités inhabituelles de certains utilisateurs qui pourraient avoir des intentions frauduleuses. Cette mesure sert à prévenir et à atténuer les transactions frauduleuses en cours effectuées sur le serveur de l'application.

### Désactiver l'authentification malveillante des utilisateurs

Des individus malintentionnés peuvent vouloir compromettre les serveurs Web en prenant plusieurs mesures telles que la force brute, les DDoS et d'autres techniques pour prendre le contrôle des comptes d'autres utilisateurs.

Cependant, plusieurs sites disposent de systèmes de Rate Limiting efficaces qui limitent le nombre de tentatives de connexion qu'un individu peut effectuer sur un site dans un intervalle de temps spécifique. Cela contribue également aux mesures de sécurité Web.

## Comment fonctionne le Rate Limiting ?

Les outils de Rate Limiting utilisés dans les applications sont implémentés sur la base de différentes structures d'algorithmes. Ces algorithmes guident la fonctionnalité de l'outil de Rate Limiting dont l'objectif final est de limiter le nombre de requêtes qu'un serveur reçoit par unité de temps afin d'améliorer son efficacité.

## Exemples d'algorithmes de Rate Limiting

Voici quelques-uns des algorithmes les plus populaires actuellement utilisés.

### Algorithme Fixed Window

Cet algorithme est basé sur la fixation d'un intervalle de temps statique et défini par le serveur pour tous les clients, régulant le nombre de requêtes qui peuvent être faites au serveur, quel que soit le nombre de clients accédant à l'API.

Par exemple, définir une limite de requête de cinq minutes empêche tout client d'accéder au point de terminaison jusqu'à l'expiration de la fenêtre de cinq minutes. Ce modèle n'est pas rentable.

### Algorithme Sliding Window

Cet algorithme est similaire dans sa configuration à l'algorithme Fixed Window, mais il apporte une solution en individualisant l'accès des clients à un nombre donné de requêtes dans un intervalle de temps spécifique en créant des intervalles de temps indépendants pour chaque client.

Par exemple, si le Client A accède à la requête à 10h00, il est autorisé à faire 10 requêtes jusqu'à l'expiration du temps à 10h03, tandis que le Client B qui accède à la requête à 10h02 est autorisé à faire 10 requêtes jusqu'à l'expiration à 10h05.

### Algorithme Leaking Bucket

Cet algorithme est basé sur la signification littérale de son nom : le seau qui fuit. Il garantit qu'un nombre spécifique de requêtes seulement peut être traité par le serveur à un moment donné. Toute requête dépassant ce nombre sera rejetée et recevra une \"**erreur 429**\". Ceci est fait pour s'assurer que le serveur n'est pas surchargé et pour garantir le maintien de l'efficacité et de la vitesse du serveur.

### Algorithme Token Bucket

Ce modèle est similaire au Leaking Bucket car il y a un seau hypothétique qui sert de Rate Limiter. Ce seau sert à gérer des jetons (tokens) et de nouveaux jetons sont ajoutés périodiquement dans le seau.

Lorsqu'une requête est effectuée, un jeton est retiré, et cela continue jusqu'à ce que tous les jetons du seau soient épuisés. À ce stade, toute requête effectuée sera rejetée avec une \"**erreur 429**\". Cela aide également à prévenir la congestion du serveur et à assurer une efficacité maximale.

## Bonnes pratiques du Rate Limiting

Un développement d'API Web efficace est principalement réalisable en suivant les meilleures pratiques de développement d'API. Pour maximiser l'utilisation d'un Rate Limiter en tant que mesure de sécurité d'API, les éléments suivants doivent être mis en œuvre.

* **Tout d'abord, choisissez un algorithme de Rate Limiting compatible.** Avoir un algorithme de Rate Limiting solide en place sera essentiel pour obtenir le résultat souhaité. Choisir le meilleur algorithme en synchronisation avec votre point de terminaison API sera également nécessaire.
    
* **Assurez-vous que les limites fixées sont dans des plages raisonnables.** Avoir des paramètres de Rate Limiting arbitraires pourrait affecter négativement l'expérience utilisateur et détourner le mécanisme de son but. Fixer une limite de temps raisonnable pour maximiser l'expérience utilisateur et lutter contre les attaques s'est avéré beaucoup plus efficace.
    
* **Assurez une gestion efficace des erreurs et fournissez le feedback nécessaire au client.** Le code d'erreur par défaut du Rate Limiting est le code d'erreur 429. Une gestion appropriée des erreurs qui surviennent lors de l'utilisation de l'API, notamment en raison de l'abus de l'API, sera nécessaire pour fournir le feedback nécessaire à l'utilisateur.
    
* **Implémentez des mécanismes de Rate Limiting flexibles sur plusieurs paramètres.** Définir un intervalle de temps fixe sur tous les points de terminaison semble être une mauvaise pratique car certains points de terminaison d'API sont beaucoup plus sensibles aux données que d'autres. Par conséquent, avoir un Rate Limiter flexible qui définit des paramètres par ordre de pertinence aide à maximiser l'efficacité du serveur et à assurer la sécurité.
    
* **Assurez la fourniture d'outils de journalisation, de surveillance et d'observabilité appropriés.** Avoir en place des métriques d'API, des outils de journalisation, de surveillance et d'observabilité aide également à servir de technique de sécurité supplémentaire pour les API Web car ils aident à surveiller l'activité du serveur et, grâce à l'utilisation d'alertes de surveillance, à notifier le développeur du serveur lorsque des requêtes suspectes sont détectées.
    
* **Assurez la synchronicité du Rate Limiting et des autres mesures de sécurité d'API.** Une synchronicité appropriée des Rate Limiters avec d'autres techniques de sécurité d'API doit être exploitée pour renforcer les mesures de sécurité globales. Une connaissance adéquate des mesures de sécurité et une expertise sont nécessaires afin de ne pas contrecarrer les mesures de sécurité existantes.
    
* **Assurez une documentation appropriée de l'API.** Une documentation adéquate de l'API est également nécessaire pour s'assurer que les utilisateurs, les autres développeurs et les clients sont conscients de la pratique de Rate Limiting en place afin de garantir le respect des règles.
    

## Conclusion

En conclusion, nous avons mis en évidence le Rate Limiting comme une technique importante de sécurité d'API ainsi que certains de ses cas d'utilisation réels.

N'hésitez pas à consulter mes autres articles [ici](https://linktr.ee/tobilyn77). D'ici la prochaine fois, continuez à coder !