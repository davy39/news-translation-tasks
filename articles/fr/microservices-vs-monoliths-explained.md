---
title: 'Microservices vs Monolithes : Avantages, Compromis et Comment Choisir l''Architecture
  de Votre Application'
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2024-05-14T00:18:44.000Z'
originalURL: https://freecodecamp.org/news/microservices-vs-monoliths-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/cover--3-.png
tags:
- name: Microservices
  slug: microservices
- name: software architecture
  slug: software-architecture
seo_title: 'Microservices vs Monolithes : Avantages, Compromis et Comment Choisir
  l''Architecture de Votre Application'
seo_desc: 'When you''re tasked with designing an application, one of the first questions
  that probably comes to your mind is whether to design a microservice or a monolith.

  The consequences of this seemingly simple and innocuous decision are potentially
  signific...'
---

Lorsque vous êtes chargé de concevoir une application, l'une des premières questions qui vous vient probablement à l'esprit est de savoir s'il faut concevoir une architecture de microservices ou un monolithe.

Les conséquences de cette décision apparemment simple et anodine sont potentiellement significatives, et elles ne sont souvent pas complètement réfléchies. Une mauvaise décision peut être très coûteuse, non seulement financièrement, mais aussi en termes de temps nécessaire pour développer l'application et déployer toute modification future.

Il n'existe cependant pas d'approche objectivement correcte. Tout dépend du problème que vous essayez de résoudre et des compromis que vous êtes prêt à accepter.

Cet article expliquera les différences entre les monolithes et les microservices ainsi que quelques heuristiques pour vous aider à choisir entre ces deux architectures.

## Table des Matières

1. [Monolithes vs Microservices : Une Analogies](#heading-monolithes-vs-microservices-une-analogie)
    
2. [Qu'est-ce qu'un Monolithe ?](#heading-quest-ce-quun-monolithe)
    
3. [Qu'est-ce que les Microservices ?](#heading-quest-ce-que-les-microservices)
    
4. [Gestion des Données dans les Microservices](#heading-gestion-des-donnees-dans-les-microservices)
    
5. [Isolation de la Base de Données dans les Microservices](#heading-isolation-de-la-base-de-donnees-dans-les-microservices)
    
6. [Comment Choisir Entre Monolithes et Microservices](#heading-comment-choisir-entre-monolithes-et-microservices)
    
7. [Pourquoi vous devriez commencer par un Monolithe](#heading-pourquoi-vous-devriez-commencer-par-un-monolithe)
    
8. [Pourquoi vous devriez commencer par un Microservice](#heading-pourquoi-vous-devriez-commencer-par-un-microservice)
    
9. [Architecture Hybride – Un Terrain d'Entente](#heading-architecture-hybride-un-terrain-dentente)
    
10. [Conclusion](#heading-conclusion)
    

## Monolithes vs Microservices : Une Analogies

Avant d'entrer dans les détails techniques des monolithes et des microservices, expliquons rapidement la différence entre les deux architectures à l'aide d'une analogie.

Une architecture monolithique est comme un restaurant typique, où tous les types de plats sont préparés dans une grande cuisine et un seul menu est présenté aux clients pour qu'ils choisissent.

Tout comme le restaurant propose tout, des entrées aux desserts, en un seul endroit, un monolithe inclut toutes les fonctionnalités dans une seule base de code.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a75fc63-2d14-4379-819f-24cfa8c9d8fe_1504x603.png align="left")

*Un restaurant typique est comme une application monolithique*

Une architecture de microservices est comme une cour de restauration composée de plusieurs petits stands spécialisés, chacun servant un type de cuisine différent. Ici, vous pouvez choisir des plats de différents stands, chacun préparant expertement son propre menu.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d8efa02-6ab9-4013-bc09-18343063139a_2462x1394.png align="left")

*Une cour de restauration est comme une application de microservices*

Dans une architecture de microservices, l'application est divisée en services plus petits et indépendants. Tout comme chaque stand de la cour de restauration gère son propre menu, son personnel et sa cuisine, dans une architecture de microservices, différents services fonctionnent séparément et sont responsables de la gestion de leurs fonctionnalités spécifiques.

Les clients peuvent choisir des plats de n'importe quel stand, en mélangeant et assortissant comme ils le souhaitent, tout comme différents microservices peuvent être utilisés en combinaison pour créer une application complète. Chaque service est autonome et communique avec d'autres services via des interfaces simples et bien définies.

## Qu'est-ce qu'un Monolithe ?

Dans un monolithe, tout le code nécessaire pour toutes les fonctionnalités de l'application est dans une seule base de code et est déployé comme une seule unité.

Prenons l'exemple d'une application de commerce électronique. Certaines des fonctionnalités importantes d'une application de commerce électronique sont :

1. **Service de recherche de produits** : Gère les listes de produits, les descriptions, les stocks, les prix et les catégories. Il est responsable de la fourniture d'informations à jour sur les produits aux autres services et aux utilisateurs.
    
2. **Service de paiement** : Gère le traitement des paiements et des transactions. Il interagit avec les passerelles de paiement externes et offre des options de paiement sécurisées aux clients.
    
3. **Service de gestion des commandes** : Gère le cycle de vie des commandes des clients, de la création à la livraison. Cela inclut le traitement des commandes, les mises à jour de statut et l'annulation des commandes.
    
4. **Service de recommandation** : Fournit des recommandations de produits personnalisées aux utilisateurs en fonction de leur historique de recherche et de leurs achats passés.
    

Dans une application monolithique, le code de ces fonctionnalités sera dans une seule base de code et déployé comme une seule unité. Cela est illustré dans l'image ci-dessous où l'application est déployée sur un seul serveur avec une base de données séparée.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35d7463a-4c95-4f64-81c1-7a41bdb21d45_2246x752.png align="left")

*Application de commerce électronique monolithique déployée sur un seul serveur*

La base de données est hébergée sur un serveur séparé pour améliorer les performances et la sécurité, tandis que les serveurs d'application gèrent la logique métier.

Même dans une architecture monolithique, l'application peut être dupliquée et déployée sur plusieurs serveurs, avec un équilibreur de charge répartissant le trafic entre les serveurs. Cela est illustré ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F808895de-b53d-4b39-9adf-55007d185976_2442x1358.png align="left")

*Application de commerce électronique monolithique déployée sur deux serveurs séparés*

## Qu'est-ce que les Microservices ?

Les microservices sont des services indépendamment déployables modélisés autour d'un domaine métier.

Contrairement à une architecture monolithique, où tous les composants de l'application sont étroitement intégrés et déployés comme une seule unité, une architecture de microservices décompose l'application en services plus petits et indépendamment déployables. Chaque service exécute son propre processus et communique avec d'autres services via un réseau, généralement en utilisant [HTTP/REST](https://lightcloud.substack.com/i/137067496/rest), [RPC](https://lightcloud.substack.com/i/137067496/rpc), ou des files d'attente de messages.

Nous pouvons décomposer l'application de commerce électronique monolithique dont nous avons parlé ci-dessus en une architecture de microservices, comme illustré ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9c9f2b4-fb93-411d-88dc-330628b222f5_2440x1022.png align="left")

*Application de commerce électronique en microservices*

Voici quelques différences clés entre l'application de commerce électronique monolithique et celle en microservices :

Dans l'architecture de microservices, chaque fonctionnalité de l'application est dans une base de code séparée. Cette séparation garantit que nous avons des services indépendamment déployables modélisés autour de domaines métier (Service de Recherche de Produits, Service de Paiement, Service de Gestion des Commandes et Service de Recommandation).

Avoir une base de code séparée pour chaque service garantit :

1. **Déploiement Simplifié** : Avec chaque service dans sa propre base de code, il peut être mis à jour, testé et déployé indépendamment des autres.
    
2. **Tolérance aux Pannes** : Des bases de code séparées contribuent à la tolérance aux pannes. Si un service rencontre une défaillance, cela ne compromet pas nécessairement le fonctionnement des autres. Cela est crucial pour maintenir la disponibilité et la fiabilité globales du système. Par exemple, si le service de paiement tombe en panne, seuls les clients qui souhaitent acheter un article seront affectés. Les autres clients peuvent toujours rechercher des articles à acheter, suivre les commandes existantes et obtenir des recommandations pour des articles qu'ils pourraient vouloir acheter.
    
3. **Flexibilité Technologique** : Des bases de code séparées permettent à chaque service d'être développé en utilisant la pile technologique la mieux adaptée à ses besoins. Différentes équipes peuvent choisir différents langages de programmation, frameworks ou bases de données en fonction de ce qui fonctionne le mieux pour la fonctionnalité spécifique de ce service.
    
4. Chaque service est déployé sur ses propres serveurs. Les serveurs hébergeant chaque service peuvent être mis à l'échelle indépendamment en fonction de leur demande et de leurs exigences spécifiques en matière de ressources. Cela est beaucoup plus efficace que de mettre à l'échelle une application monolithique où la mise à l'échelle signifie souvent mettre à l'échelle l'ensemble de l'application, même si seule une partie de celle-ci est sous forte charge. Par exemple, le service de paiement peut être très occupé pendant une promotion/vente. Celui-ci peut être mis à l'échelle indépendamment au lieu de mettre à l'échelle l'ensemble de l'application, ce qui peut être un gaspillage d'argent.
    

Chaque service a sa propre base de données (s'il en a besoin). Cela garantit :

1. Chaque microservice peut fonctionner indépendamment des autres services. Si chaque service utilisait la même base de données (comme c'est le cas dans une application monolithique), une défaillance de la base de données entraînerait la chute de l'ensemble de l'application.
    
2. Les bases de données peuvent être mises à l'échelle indépendamment selon les besoins. Certaines bases de données seront plus occupées que d'autres, donc avoir la flexibilité de les mettre à l'échelle indépendamment est utile.
    
3. Chaque microservice utilise le bon type de base de données. Certains microservices peuvent fonctionner mieux avec différents types de bases de données. Par exemple, Elasticsearch serait idéal pour la base de données de recherche de produits de l'application de commerce électronique en raison de ses puissantes capacités de recherche en texte intégral, tandis qu'une base de données SQL relationnelle sera mieux adaptée pour les bases de données de commandes et de paiements.
    
4. Une [Passerelle API](https://lightcloud.substack.com/p/api-gateway-explained) se trouve devant les services. Cela agit comme un intermédiaire entre les utilisateurs et les nombreux services auxquels ils peuvent avoir besoin d'accéder. La Passerelle API gère [l'autorisation et l'authentification](https://lightcloud.substack.com/i/138365595/authorisation-and-authentication), [le routage des requêtes](https://lightcloud.substack.com/i/138365595/request-routing) et [la limitation de débit](https://lightcloud.substack.com/i/138365595/rate-limiting).
    

### Gestion des Données dans les Microservices

La gestion des données entre les services est la partie la plus complexe d'une architecture de microservices. La communication entre les services est soit synchrone, soit asynchrone.

**Communication Synchrone** : Les services communiquent directement entre eux. C'est une approche simple, facile à comprendre et à mettre en œuvre.

Par exemple, dans une application de commerce électronique, lorsqu'un client passe une commande, le Service de Gestion des Commandes peut directement appeler le Service de Recherche de Produits pour vérifier si l'article est en stock avant de procéder.

**Communication Asynchrone** : Les services n'attendent pas de réponse directe d'un autre service. Au lieu de cela, ils communiquent via des événements ou des messages en utilisant un courtier de messages.

Dans l'exemple de commerce électronique, lorsqu'une nouvelle commande est passée, le Service de Gestion des Commandes publiera un événement "Commande Créée" dans une file d'attente de messages. Le Service de Recherche de Produits, abonné à cette file d'attente, réagit à l'événement à son propre rythme et met à jour l'inventaire en conséquence. Cela découple les services, leur permettant de fonctionner et de se mettre à l'échelle indépendamment.

La communication synchrone est plus simple à comprendre et à mettre en œuvre, mais elle manque de [tolérance aux pannes](https://lightcloud.substack.com/i/59017006/fault-tolerance).

### Isolation de la Base de Données dans les Microservices

Dans une architecture de microservices, il est une pratique standard d'empêcher les services d'accéder directement aux bases de données des autres services. Vous feriez généralement cela pour vous assurer que chaque service peut gérer son schéma de données indépendamment, sans affecter les autres services.

En revenant à notre exemple de commerce électronique, supposons que le Service de Paiement décide de changer son schéma de données et de renommer une colonne appelée "amount" en "order_value", car "amount" peut être un terme assez ambigu. Si le Service de Gestion des Commandes interrogeait directement la base de données du Service de Paiement, toute requête SQL directe du Service de Gestion des Commandes vers la base de données du Service de Paiement sur cette colonne échouerait en raison de ce changement de schéma.

Pour gérer ces dépendances et ces changements de manière sécurisée et efficace, les services doivent interagir via des API plutôt que via un accès direct à la base de données. En fournissant une API comme interface, le Service de Paiement peut abstraire les complexités de son modèle de données sous-jacent.

Par exemple, quel que soit le nom du champ de la base de données, "amount" ou "order_value", l'API peut exposer un paramètre appelé "payment_amount". Cela permet au Service de Paiement de mapper en interne "payment_amount" à ce que le schéma de la base de données utilise actuellement.

## Comment Choisir Entre Monolithes et Microservices

Choisir entre une architecture monolithique et une architecture de microservices dépend du problème que vous essayez de résoudre et des compromis que vous êtes prêt à accepter.

Les microservices sont plus récents et plus populaires parmi les grandes entreprises technologiques. La plupart des livres et blogs techniques couvrent les architectures de ces grandes entreprises.

Mais les problèmes d'ingénierie des grandes entreprises fonctionnant à grande échelle ne sont pas nécessairement les mêmes problèmes d'ingénierie auxquels sont confrontées les petites entreprises.

Copier ce que font les grandes entreprises technologiques est un raisonnement par analogie. Cela n'est pas nécessairement faux, mais cela peut introduire des complexités inutiles pour une petite entreprise/démarrage. Mieux vaut raisonner par premiers principes, ou mieux encore, choisir de meilleures analogies.

Vous pouvez regarder ce que font d'autres startups, ou ce que les géants technologiques d'aujourd'hui faisaient lorsqu'ils étaient beaucoup plus petits. Par exemple, [Etsy, Netflix et Uber](https://blog.dreamfactory.com/microservices-examples/) ont tous commencé comme des monolithes avant de migrer vers une architecture de microservices.

### Pourquoi vous devriez commencer par un Monolithe

Créer une application devrait être fait pour une seule raison : construire quelque chose que les gens veulent utiliser. Les utilisateurs de votre application ne se soucient pas de savoir si vous utilisez un microservice ou un monolithe. Ils se soucient que vous résolviez un problème pour eux.

Pour citer [Paul Graham](https://paulgraham.com/startuplessons.html) :

> "Presque tout le monde a un plan initial qui est faux. Si les entreprises s'en tenaient à leurs plans initiaux, Microsoft vendrait des langages de programmation et Apple vendrait des cartes de circuits imprimés. Dans les deux cas, leurs clients leur ont dit quel devrait être leur activité et ils ont été assez intelligents pour écouter."

Il n'y a probablement aucune raison de passer autant de temps à concevoir et à mettre en œuvre une architecture de microservices hautement complexe lorsque vous n'êtes même pas sûr de construire quelque chose que les gens veulent utiliser.

Alors, pourquoi devriez-vous commencer par un monolithe lors de la construction d'une application ?

1. **Simplicité** : Un monolithe ne nécessite pas de gérer les complexités d'un système distribué, telles que la latence du réseau, la cohérence des données ou la communication inter-services. Ce manque de complexité non seulement rend la phase de développement initiale plus fluide, mais réduit également la charge pour les nouveaux développeurs, qui peuvent contribuer plus rapidement sans avoir à comprendre les intricacies d'un système distribué.
    
2. **Facilité d'Itération** : Dans les premières étapes d'un produit, une itération rapide basée sur les retours des utilisateurs est cruciale. La direction du produit évolue encore, et des pivots ou ajustements rapides sont nécessaires en fonction des retours des utilisateurs. Cela est généralement plus facile à réaliser avec une architecture monolithique simple.
    
3. **Faible Coût** : Exécuter une application monolithique peut être moins coûteux dans les premières étapes, car elle nécessite généralement moins d'infrastructure et de ressources qu'une architecture de microservices distribuée. Cela est crucial pour les startups et les petites entreprises où l'argent peut manquer.
    

Commencer par un monolithe correspond souvent mieux aux réalités pratiques du lancement et de l'itération sur une nouvelle application.

### Pourquoi vous devriez commencer par un Microservice

1. **Évolutivité dès le Début** : L'un des arguments les plus forts en faveur des microservices est leur capacité innée à évoluer. Si vous anticipez une croissance rapide de l'utilisation ou du volume de données, les microservices vous permettent de mettre à l'échelle des composants spécifiques de l'application qui nécessitent plus de ressources sans mettre à l'échelle l'ensemble de l'application. Cela peut être particulièrement précieux pour les applications devant gérer des charges variables ou pour les services qui pourraient croître de manière imprévisible.
    
2. **Résilience** : Les microservices améliorent la résilience globale de l'application. Parce que chaque service est indépendant, les défaillances dans un domaine sont moins susceptibles de faire tomber tout le système. Cette isolation aide à maintenir la résilience en garantissant que des parties de votre application peuvent encore fonctionner même si d'autres échouent.
    
3. **Piles Technologiques Flexibles** : Les microservices permettent à différentes équipes d'utiliser les piles technologiques les mieux adaptées à leurs besoins spécifiques. En revenant à notre exemple de commerce électronique, les autres services peuvent être écrits en Java, mais le service de recommandation peut être écrit en Python si l'équipe responsable de sa construction a plus d'expertise en Python. C'est un exemple très simpliste, mais le principe tient. Une architecture de microservices donne aux équipes la flexibilité sur la technologie qu'elles peuvent utiliser. Poussé à son extrême logique, cela peut aussi être un défaut puisque cela peut ajouter une complexité supplémentaire à l'architecture globale. Introduire un langage différent pour un service peut nécessiter des outils de construction et des processus de déploiement différents.
    

## Architecture Hybride – Un Terrain d'Entente

La définition formelle et académique d'un microservice est qu'il s'agit d'un service indépendamment déployable modélisé autour d'un domaine métier. Selon cette définition, chaque domaine métier devrait être un service séparé.

Mais vous n'êtes pas limité à cette définition stricte lorsqu'il s'agit de mettre en œuvre une conception. Regardons à nouveau notre application de commerce électronique en microservices.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc244781f-08a0-42b1-a928-ddc95e02d437_2440x1022.png align="left")

*Application de commerce électronique en microservices*

Nous pouvons choisir de garder le service de recherche de produits comme un microservice. Puisque plus de personnes recherchent des produits que ne les achètent, nous pouvons vouloir la capacité de mettre à l'échelle ce service indépendamment des autres.

De plus, ce service aura besoin de sa propre base de données de recherche en texte intégral dédiée comme Elasticsearch ou Solr. Les bases de données SQL ne sont pas bien adaptées pour la recherche en texte intégral et le filtrage des produits.

Nous pouvons également choisir de garder le service de recommandation comme un microservice puisque celui-ci sera écrit dans un langage différent des autres services. Ce service aura également besoin de sa propre base de données de graphes séparée comme Neo4j pour aider à faire des recommandations aux utilisateurs sur ce qu'ils doivent acheter en fonction de leurs recherches et achats passés.

Il nous reste le service de paiement et le service de gestion des commandes qui peuvent être combinés en un monolithe. Cela est illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F113147b6-7a41-49a1-a4ad-88130de2f9fd_2334x922.png align="left")

*Architecture hybride monolithique/microservices*

Dans cet exemple, nous n'avons pas suivi la définition académique d'une architecture de microservices, où chaque service est modélisé autour d'un domaine métier. Au lieu de cela, nous avons choisi d'être pragmatiques et de créer des microservices parce que nous voulons utiliser une technologie spécifique et parce que nous voulons pouvoir mettre à l'échelle certains services indépendamment.

## Conclusion

Dans un monolithe, tout le code nécessaire pour toutes les fonctionnalités d'une application est dans une seule base de code et est déployé comme une seule unité. Dans une architecture de microservices, l'application est divisée en composants plus petits et indépendants, chacun responsable de fonctionnalités ou de fonctionnalités spécifiques. Chaque microservice a sa propre base de code et peut être déployé indépendamment des autres.

Choisir entre un monolithe et un microservice dépend du problème que vous essayez de résoudre et des compromis que vous êtes prêt à accepter.

Les monolithes offrent simplicité, facilité d'itération et faible coût. Les microservices offrent évolutivité, résilience et une pile technologique plus flexible.

Pour les startups, la simplicité, la facilité d'itération et l'efficacité des coûts d'une architecture monolithique en font un choix initial idéal, leur permettant de se concentrer sur le développement des fonctionnalités principales et de trouver un ajustement produit-marché sans le surcoût de la gestion d'un système distribué.

Pour une entreprise plus établie avec des besoins croissants en matière d'évolutivité, de résilience et de flexibilité technologique, une architecture de microservices peut être un meilleur choix.