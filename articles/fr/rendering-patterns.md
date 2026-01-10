---
title: Modèles de rendu pour les applications web – Rendu côté serveur, côté client
  et SSG expliqués
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-03-06T18:22:40.000Z'
originalURL: https://freecodecamp.org/news/rendering-patterns
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/sebastian-svenson-8QgqOLJAL8k-unsplash.jpg
tags:
- name: Web Applications
  slug: web-applications
seo_title: Modèles de rendu pour les applications web – Rendu côté serveur, côté client
  et SSG expliqués
seo_desc: 'Hi everyone! In this article we''re going to take a look at the different
  rendering pattern options available nowadays for web applications.

  I''ll start by explaining what a rendering pattern is, then go through each of the
  main options available. Fina...'
---

Bonjour à tous ! Dans cet article, nous allons examiner les différentes options de modèles de rendu disponibles de nos jours pour les applications web.

Je commencerai par expliquer ce qu'est un modèle de rendu, puis je passerai en revue chacune des principales options disponibles. Enfin, nous les comparerons, en expliquant les avantages et les inconvénients et quand l'une peut être plus bénéfique que l'autre.

C'est parti !

# Table des matières

* [Qu'est-ce qu'un modèle de rendu ?](#heading-quest-ce-quun-modele-de-rendu)
    
* [Différentes options de modèles de rendu](#heading-differentes-options-de-modeles-de-rendu)
    
    * [Sites web statiques](#heading-sites-web-statiques)
        
    * [Applications monopage (SPA) avec rendu côté client (CSR)](#heading-applications-monopage-spa-avec-rendu-cote-client-csr)
        
    * [Rendu côté serveur (SSR)](#heading-rendu-cote-serveur-ssr)
        
    * [Génération de site statique (SSG)](#heading-generation-de-site-statique-ssg)
        
    * [Régénération statique incrémentielle (ISR)](#heading-regeneration-statique-incrementielle-isr)
        
    * [Le concept d'hydratation](#heading-le-concept-dhydratation)
        
    * [Îlots](#heading-ilots)
        
    * [SSR en streaming](#heading-ssr-en-streaming)
        
* [Comparaison des différents modèles](#heading-comparaison-des-differents-modeles)
    
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce qu'un modèle de rendu ?

En développement web, un modèle de rendu fait référence à la manière dont le code HTML, CSS et JavaScript est traité et rendu dans une application web ou un site web.

Différents modèles de rendu sont utilisés pour atteindre différents objectifs de performance et d'expérience utilisateur. Les modèles de rendu les plus courants en développement web sont :

1. **Rendu côté serveur (SSR)** : Dans le SSR, le serveur web génère le contenu HTML d'une page web côté serveur et l'envoie au navigateur du client. Cette approche peut améliorer les temps de chargement initiaux et le SEO (optimisation pour les moteurs de recherche) mais peut être plus lente pour le contenu dynamique.
    
2. **Rendu côté client (CSR)** : Dans le CSR, le navigateur du client génère le contenu HTML d'une page web côté client en utilisant JavaScript. Cette approche peut offrir une expérience utilisateur rapide et interactive mais peut être plus lente pour les temps de chargement initiaux et mauvaise pour le SEO.
    
3. **Génération de site statique (SSG)** : Dans le SSG, le contenu HTML d'une page web est généré au moment de la construction et servi au client sous forme de fichier statique. Cette approche peut offrir d'excellentes performances et sécurité mais peut être moins flexible pour le contenu dynamique.
    

En résumé, un modèle de rendu est une stratégie de traitement et de rendu de contenu web en développement web. Le choix du modèle de rendu dépend des besoins et exigences spécifiques d'un projet, tels que la performance, le SEO, l'expérience utilisateur et la flexibilité.

Maintenant que nous avons une idée de ce qu'est un modèle de rendu, examinons en détail les nombreuses options disponibles de nos jours.

# Différentes options de modèles de rendu

## Sites web statiques

Un site web statique est un type de site web qui se compose d'un ensemble de fichiers HTML, CSS et JavaScript servis au navigateur du client sans aucun traitement côté serveur ou intégration de base de données.

Les sites web statiques sont généralement créés à l'aide de générateurs de sites statiques, tels que [Jekyll](https://jekyllrb.com/), [Hugo](https://gohugo.io/), ou [Gatsby.js](https://www.gatsbyjs.com/). Ces générateurs compilent des modèles, des fichiers markdown ou d'autres sources de données en un ensemble de fichiers statiques qui sont ensuite déployés sur un serveur web ou un [réseau de diffusion de contenu (CDN)](https://www.youtube.com/watch?v=RI9np1LWzqw).

Les sites web statiques sont souvent utilisés pour des sites de petite à moyenne taille qui ne nécessitent pas de fonctionnalités dynamiques complexes ou de traitement côté serveur. Ils sont faciles à déployer, à mettre à l'échelle et à maintenir, car ils ne nécessitent pas d'application côté serveur ou de base de données.

Ils offrent également une excellente sécurité et performance, car le contenu est servi directement depuis un serveur web ou un CDN sans aucun traitement côté serveur.

Les sites web statiques peuvent être enrichis avec du JavaScript côté client, comme React ou Vue, pour fournir des fonctionnalités interactives ou du contenu dynamique. Mais toute donnée nécessaire pour ces fonctionnalités doit être chargée via des requêtes API côté client, car il n'y a pas de traitement côté serveur pour générer ou récupérer les données.

En résumé, un site web statique est un type de site web qui se compose d'un ensemble de fichiers statiques servis au navigateur du client sans aucun traitement côté serveur ou intégration de base de données. Ils sont simples, rapides, sécurisés et scalables, et conviennent aux sites de petite à moyenne taille qui ne nécessitent pas de fonctionnalités dynamiques complexes ou de traitement côté serveur.

## Applications monopage (SPA) avec rendu côté client (CSR)

Une application monopage (SPA) est un type d'application web rendue avec le rendu côté client (CSR). Cela signifie que tous les fichiers HTML, CSS et JavaScript nécessaires sont chargés en une seule fois lorsque l'utilisateur charge la page pour la première fois. Ensuite, JavaScript met à jour dynamiquement le contenu lorsque l'utilisateur interagit avec la page, sans nécessiter un rechargement complet de la page.

Dans une SPA, l'application JavaScript côté client est responsable du rendu du HTML et du traitement des interactions de l'utilisateur. L'application JavaScript interagit avec une API backend pour récupérer des données et mettre à jour l'interface utilisateur de manière dynamique. Typiquement, cette interaction est réalisée en utilisant des requêtes AJAX (Asynchronous JavaScript and XML) ou des requêtes Fetch API.

Les SPA offrent une expérience utilisateur rapide et interactive car seul le contenu nécessaire est chargé et rendu dynamiquement, réduisant le besoin de recharger complètement la page. Elles offrent également une expérience utilisateur plus fluide car l'application peut répondre aux entrées de l'utilisateur sans rafraîchir toute la page.

Cependant, les SPA nécessitent une configuration plus complexe et peuvent avoir des temps de chargement initiaux plus longs par rapport aux approches de rendu côté serveur (SSR) ou de génération de site statique (SSG).

Elles nécessitent également des considérations supplémentaires pour l'optimisation des moteurs de recherche (SEO) et l'accessibilité, car les moteurs de recherche et les technologies d'assistance peuvent avoir des difficultés à indexer ou à naviguer dans le contenu.

En résumé, une application monopage (SPA) ou rendu côté client (CSR) est un type d'application web qui charge tous les fichiers HTML, CSS et JavaScript nécessaires en une seule fois, puis met à jour dynamiquement le contenu lorsque l'utilisateur interagit avec la page, sans nécessiter un rechargement complet de la page.

Elles offrent une expérience utilisateur rapide et interactive mais nécessitent une configuration plus complexe et des considérations supplémentaires pour le SEO et l'accessibilité.

## Rendu côté serveur (SSR)

Le rendu côté serveur (SSR) est une technique de rendu de pages web côté serveur avant de les envoyer au navigateur du client. Dans le SSR, le serveur génère le contenu HTML d'une page web en fonction de l'URL demandée et des données, et l'envoie au navigateur du client sous forme de document HTML complet.

Le SSR offre plusieurs avantages, notamment des performances améliorées, un meilleur SEO et une accessibilité plus robuste.

En rendant le HTML côté serveur, le SSR réduit la quantité de code JavaScript qui doit être chargé et exécuté sur le navigateur du client. Cela se traduit par des temps de chargement initiaux plus rapides et de meilleures performances sur les appareils bas de gamme ou les réseaux lents.

De plus, le SSR permet aux moteurs de recherche et aux crawlers des réseaux sociaux d'indexer les pages web plus précisément, car le contenu HTML complet est disponible lors du chargement initial de la page. Cela peut améliorer la visibilité et le classement du site web dans les pages de résultats des moteurs de recherche.

Le SSR garantit également que les pages web sont accessibles aux utilisateurs avec des technologies d'assistance, telles que les lecteurs d'écran ou la navigation au clavier, car le contenu HTML est disponible dès le chargement initial de la page.

Cependant, le SSR a certaines limitations, telles que des exigences accrues en matière de traitement côté serveur et une interactivité limitée par rapport au rendu côté client (CSR) ou aux applications monopage (SPA).

En résumé, le rendu côté serveur (SSR) est une technique de rendu de pages web côté serveur avant de les envoyer au navigateur du client. Il offre des performances améliorées, un meilleur SEO et une accessibilité plus robuste, mais nécessite plus de traitement côté serveur et a certaines limitations en termes d'interactivité.

## Génération de site statique (SSG)

La génération de site statique (SSG) est une technique de construction de pages web en pré-générant des fichiers HTML, CSS et JavaScript au moment de la construction au lieu de les rendre côté serveur ou côté client.

Dans le SSG, un outil de génération de site statique comme Jekyll, Hugo ou Gatsby.js est utilisé pour compiler le contenu du site web à partir de sources de données telles que des fichiers markdown, des fichiers JSON ou des données [CMS](https://www.youtube.com/watch?v=nrbpOmNC_mM), et générer un ensemble de fichiers statiques qui peuvent être servis directement au navigateur sans aucun traitement côté serveur.

Les fichiers statiques générés peuvent être déployés sur un serveur web ou un réseau de diffusion de contenu (CDN) et servis rapidement aux utilisateurs finaux avec une faible latence. Le SSG offre plusieurs avantages tels que des temps de chargement rapides, une sécurité améliorée et une scalabilité.

Puisque le SSG rend les pages web au moment de la construction, il n'est pas nécessaire de générer les pages dynamiquement côté serveur ou côté client. Cela réduit la surcharge de traitement et permet des temps de chargement plus rapides.

Les sites statiques sont également moins vulnérables aux attaques côté serveur et nécessitent moins de ressources serveur, ce qui les rend plus scalables et plus faciles à maintenir.

Mais le SSG a certaines limitations en termes de contenu dynamique et d'interactivité. Puisque le contenu est généré au moment de la construction, toute donnée dynamique ou interaction utilisateur doit être gérée par du code JavaScript côté client ou des fonctions serverless.

En résumé, la génération de site statique (SSG) est une technique de construction de pages web en pré-générant des fichiers HTML, CSS et JavaScript au moment de la construction au lieu de les rendre côté serveur ou côté client. Elle offre plusieurs avantages tels que des temps de chargement rapides, une sécurité améliorée et une scalabilité, mais a certaines limitations en termes de contenu dynamique et d'interactivité.

## Régénération statique incrémentielle (ISR)

La régénération statique incrémentielle (ISR) est une technique de construction de sites statiques qui combine les avantages du rendu côté serveur (SSR) et de la génération de site statique (SSG).

Dans l'ISR, l'outil de génération de site statique pré-génère un ensemble de pages statiques au moment de la construction, mais inclut également des métadonnées supplémentaires qui permettent aux pages d'être régénérées dynamiquement côté serveur lorsqu'elles sont demandées par l'utilisateur. Ces métadonnées pourraient inclure des informations telles que les temps d'expiration ou les dépendances à des sources de données spécifiques.

Lorsque l'utilisateur demande une page qui a expiré ou dont les dépendances ont changé, la logique côté serveur peut régénérer la page avec le contenu mis à jour et la servir à l'utilisateur, sans nécessiter une reconstruction complète du site.

Cela permet au site de maintenir les avantages de la génération de site statique, tels que des temps de chargement rapides et une faible surcharge de traitement serveur, tout en permettant un contenu dynamique et des expériences personnalisées pour les utilisateurs.

L'ISR est particulièrement utile pour les sites dont le contenu change fréquemment ou pour les sites avec un grand nombre de pages dont la reconstruction intégrale serait inefficace à chaque fois qu'un changement est apporté.

Il permet le meilleur des deux mondes : les avantages de performance et de sécurité des sites statiques combinés à la flexibilité et à la personnalisation du rendu côté serveur.

En résumé, la régénération statique incrémentielle (ISR) est une technique de construction de sites statiques qui combine les avantages du rendu côté serveur (SSR) et de la génération de site statique (SSG). Elle permet un contenu dynamique et des expériences personnalisées pour les utilisateurs tout en maintenant les avantages de performance et de sécurité des sites statiques.

## Le concept d'hydratation

En développement web, "l'hydratation" fait référence au processus de prise d'un document HTML initialement rendu côté serveur et d'ajout d'une interactivité dynamique côté client.

L'hydratation est couramment utilisée dans les applications monopage (SPA) qui utilisent le rendu côté client (CSR).

Lors de l'hydratation, le navigateur analyse le document HTML généré par le serveur et construit un arbre DOM (Document Object Model), qui représente la structure et le contenu de la page.

Le navigateur exécute ensuite le code JavaScript responsable de l'ajout de comportements dynamiques à la page, tels que la gestion des événements, la récupération de données et le rendu des composants.

Le code JavaScript récupère l'état initial et les props des composants à partir du HTML généré par le serveur et les utilise pour réhydrater les composants côté client, les transformant ainsi en éléments interactifs.

Ce processus garantit que l'état initial de la page côté client correspond au HTML généré par le serveur et assure une transition transparente de la vue initiale rendue côté serveur à la vue interactive côté client.

L'hydratation est importante pour plusieurs raisons. Premièrement, elle offre de meilleures performances et une meilleure expérience utilisateur en minimisant le temps d'interactivité et en permettant à l'utilisateur d'interagir immédiatement avec la page.

Deuxièmement, elle permet aux crawlers des moteurs de recherche d'accéder au contenu et aux métadonnées de la page, améliorant ainsi le SEO.

Enfin, elle garantit que le contenu est accessible et utilisable même si JavaScript est désactivé dans le navigateur de l'utilisateur.

En résumé, l'hydratation est le processus de prise d'un document HTML initialement rendu côté serveur et d'ajout d'une interactivité dynamique côté client.

Elle est couramment utilisée dans les applications monopage (SPA) qui utilisent le rendu côté client (CSR) et offre de meilleures performances, un meilleur SEO et une meilleure accessibilité.

## Îlots

Le modèle des Îlots est une technique de développement web qui consiste à décomposer une grande page web complexe en composants plus petits et autonomes, chacun avec son propre code HTML, CSS et JavaScript.

Chaque composant est rendu indépendamment côté serveur puis réhydraté côté client, ce qui lui permet de devenir interactif.

Le terme "îlots" fait référence aux composants individuels, chacun représentant une île distincte de contenu et de fonctionnalité au sein de la page plus grande.

En décomposant la page en îlots plus petits, chacun avec son propre état et comportement, l'application devient plus modulaire, plus facile à comprendre et à maintenir, et peut offrir une expérience utilisateur plus fluide.

Le modèle des Îlots est étroitement lié au concept d'hydratation car il repose sur le même principe de base : rendre le HTML statique côté serveur puis l'hydrater côté client avec JavaScript pour ajouter de l'interactivité.

Dans ce cas, chaque îlot individuel est rendu côté serveur avec son propre HTML statique, qui est ensuite hydraté côté client pour activer les fonctionnalités dynamiques.

L'hydratation dans le modèle des Îlots implique généralement l'utilisation d'un framework ou d'une bibliothèque côté client pour attacher des gestionnaires d'événements, gérer l'état et rendre le contenu dynamique au sein de chaque composant. Le framework ou la bibliothèque doit être capable de réhydrater le composant côté client, garantissant que l'état initial et le comportement du composant correspondent à ceux du HTML rendu côté serveur.

Un avantage de l'utilisation du modèle des Îlots avec l'hydratation est qu'il peut améliorer les performances des grandes applications web complexes en réduisant la quantité de JavaScript qui doit être téléchargée et exécutée côté client. En rendant chaque composant indépendamment côté serveur et en le réhydratant côté client, l'application peut offrir une expérience utilisateur plus fluide sans sacrifier les performances ou la scalabilité.

En résumé, le modèle des Îlots est une technique de développement web qui consiste à décomposer une grande page web complexe en composants plus petits et autonomes, chacun avec son propre code HTML, CSS et JavaScript. Il repose sur le même principe d'hydratation que les autres modèles de rendu, rendant le HTML statique côté serveur puis ajoutant de l'interactivité avec JavaScript côté client.

Le modèle des Îlots peut améliorer les performances et la scalabilité des grandes applications web en réduisant la quantité de JavaScript qui doit être téléchargée et exécutée côté client.

## SSR en streaming

Le rendu côté serveur en streaming (SSR) est un modèle de rendu pour le développement web qui consiste à envoyer le HTML généré par le serveur au client dès qu'il devient disponible, plutôt que d'attendre que la page entière soit rendue avant de l'envoyer.

Avec le SSR traditionnel, le serveur attendrait que la page entière soit rendue avant de l'envoyer au client, ce qui entraîne un temps plus long pour le premier octet (TTFB) et une expérience utilisateur plus lente.

Le SSR en streaming permet au serveur d'envoyer le HTML au client par morceaux au fur et à mesure qu'il est généré, offrant un TTFB plus rapide et une expérience utilisateur plus réactive.

Le SSR en streaming est particulièrement utile pour rendre de grandes pages web complexes qui prennent beaucoup de temps à être rendues, comme les pages de produits de commerce électronique ou les articles de presse.

Avec le SSR en streaming, l'utilisateur peut commencer à interagir avec la page dès que le premier morceau de HTML est reçu, sans avoir à attendre que la page entière soit rendue.

Pour implémenter le SSR en streaming, le serveur doit utiliser une technique appelée "chunking" pour diviser le HTML généré par le serveur en morceaux plus petits et les envoyer au client au fur et à mesure qu'ils deviennent disponibles. Le client utilise ensuite JavaScript pour ajouter chaque morceau de HTML à la page au fur et à mesure qu'il est reçu, ce qui revient effectivement à diffuser le contenu à l'utilisateur.

Un défi avec le SSR en streaming est de s'assurer que les morceaux de HTML sont envoyés au client dans le bon ordre et que la page reste cohérente au fur et à mesure qu'elle est rendue.

Pour résoudre ce problème, les développeurs peuvent utiliser des techniques telles que le CSS critique, qui consiste à identifier et à rendre les styles les plus importants en premier, ou le chunking basé sur des modèles, qui consiste à diviser le HTML en morceaux plus petits en fonction de modèles ou de composants.

En résumé, le rendu côté serveur en streaming (SSR) est un modèle de rendu pour le développement web qui consiste à envoyer le HTML généré par le serveur au client par morceaux au fur et à mesure qu'il est généré, offrant un TTFB plus rapide et une expérience utilisateur plus réactive. Il est particulièrement utile pour rendre de grandes pages web complexes.

Pour implémenter le SSR en streaming, le serveur doit utiliser une technique appelée "chunking" pour diviser le HTML en morceaux plus petits, et le client doit utiliser JavaScript pour ajouter chaque morceau à la page au fur et à mesure qu'il est reçu.

# Comparaison des différents modèles

Super, maintenant nous avons une idée claire de chacune des options courantes disponibles. Passons maintenant rapidement en revue les principales caractéristiques de chaque modèle et mentionnons les situations dans lesquelles chacun d'eux pourrait être plus bénéfique.

### Sites web statiques

**Caractéristiques principales :**

* Fichiers HTML, CSS et JavaScript pré-construits servis tels quels au client.
    
* Pas de contenu dynamique, car tout le contenu est pré-rendu et ne change pas.
    
* Temps de chargement rapides en raison de l'absence de traitement serveur.
    

**Avantages :**

* Temps de chargement extrêmement rapides et faibles coûts serveur.
    
* Idéal pour les sites avec peu ou pas de contenu dynamique, comme les portfolios ou les blogs.
    

**Inconvénients :**

* Interactivité et fonctionnalités limitées, car tout le contenu est pré-rendu.
    
* Non adapté aux sites nécessitant du contenu dynamique ou des entrées utilisateur.
    

**Idéal pour :**

* Sites avec un contenu dynamique limité ou sites ne nécessitant pas de fonctionnalités dynamiques.
    

### Applications monopage (SPA)

**Caractéristiques principales :**

* Tout le contenu est rendu dynamiquement côté client via JavaScript.
    
* Une seule page est chargée, les mises à jour de contenu étant gérées par JavaScript.
    
* Le contenu dynamique peut être facilement ajouté via des API.
    

**Avantages :**

* Interactivité et fonctionnalités élevées, car tout le contenu est dynamique et peut être mis à jour sans recharger la page.
    
* Idéal pour les applications complexes et basées sur les données nécessitant des mises à jour fréquentes de contenu.
    

**Inconvénients :**

* Temps de chargement initiaux plus lents en raison de la nécessité de charger JavaScript et de rendre dynamiquement le contenu.
    
* Peut être difficile à mettre en œuvre des techniques SEO appropriées en raison du manque de contenu pré-rendu.
    

**Idéal pour :**

* Applications nécessitant une interactivité complexe ou des mises à jour fréquentes de contenu.
    

### Rendu côté serveur (SSR) :

**Caractéristiques principales :**

* Le rendu côté serveur (SSR) est un processus dans lequel les pages web sont générées sur le serveur et envoyées au client sous forme de HTML entièrement rendu.
    
* Le serveur envoie une réponse HTML complète au client, qui inclut tout le contenu dynamique, après avoir traité les données sur le serveur.
    

**Avantages :**

* SEO amélioré car les crawlers des moteurs de recherche peuvent facilement analyser le contenu HTML complet.
    
* Meilleure performance car le HTML initial est envoyé dans une seule réponse, ce qui réduit le temps pour le navigateur de charger et d'afficher le contenu.
    
* Fonctionne bien pour les applications riches en contenu ou les applications web dynamiques nécessitant des données à récupérer depuis des API.
    

**Inconvénients :**

* Surcharge serveur plus élevée car chaque requête est traitée sur le serveur.
    
* Plus complexe à configurer car cela nécessite un framework côté serveur qui supporte le SSR.
    
* Moins interactif car les interactions nécessitent des requêtes serveur supplémentaires.
    

**Idéal pour :**

* Applications avec un contenu qui change fréquemment.
    
* Applications avec des données dynamiques qui doivent être traitées sur le serveur avant d'envoyer la réponse.
    

### Génération de site statique (SSG) :

**Caractéristiques principales :**

* La génération de site statique (SSG) est un processus dans lequel les pages web sont pré-construites en tant que fichiers statiques lors du processus de construction et servies au client en tant que pages HTML statiques.
    
* Le serveur envoie des pages HTML statiques au client, qui incluent tout le contenu, sans traiter aucune donnée sur le serveur.
    

**Avantages :**

* Très rapide et efficace car les pages statiques peuvent être servies depuis un CDN ou un cache.
    
* Surcharge serveur plus faible car le serveur n'a besoin que de servir des fichiers statiques.
    
* Peut être déployé sur un hébergeur de fichiers statiques ou des environnements serverless comme AWS Lambda.
    

**Inconvénients :**

* Non adapté au contenu dynamique qui change fréquemment.
    
* Les interactions nécessitent un JavaScript supplémentaire côté client.
    

**Idéal pour :**

* Applications avec principalement du contenu statique et peu d'interactions.
    
* Applications avec une interactivité limitée.
    

### Régénération statique incrémentielle (ISR) :

**Caractéristiques principales :**

* La régénération statique incrémentielle (ISR) est une approche hybride entre SSG et SSR, où les pages sont pré-rendues en tant que pages HTML statiques lors du processus de construction, puis le contenu est régénéré périodiquement ou à la demande selon les besoins.
    

**Avantages :**

* Temps de chargement du contenu plus rapide car les pages statiques sont servies initialement, mais le contenu peut être mis à jour rapidement.
    
* Surcharge serveur plus faible car les pages statiques peuvent être servies depuis un CDN ou un cache, et le contenu dynamique est régénéré uniquement lorsque cela est nécessaire.
    

**Inconvénients :**

* Contenu dynamique limité car la régénération du contenu nécessite une requête serveur.
    
* Nécessite une stratégie de mise en cache complexe pour s'assurer que le contenu obsolète n'est pas servi aux clients.
    

**Situations :**

* Applications avec un contenu qui change fréquemment mais peut tolérer une certaine latence.
    
* Applications avec un contenu dynamique limité.
    

### Îlots :

**Caractéristiques principales :**

* Le modèle de rendu des Îlots fait référence au rendu de parties de la page sur le serveur tandis que d'autres parties sont rendues côté client.
    
* Le serveur rend le contenu critique, tandis que le client récupère le reste du contenu.
    
* Le rendu côté serveur peut améliorer la vitesse de chargement initiale de la page et améliorer le SEO.
    
* Le rendu côté client peut améliorer l'interactivité et réduire la surcharge serveur.
    

**Avantages :**

* Temps de chargement des pages plus rapides car le serveur rend le contenu critique tandis que le client récupère le reste.
    
* Fonctionne bien pour les applications qui nécessitent un rendu partiel côté serveur et un rendu partiel côté client.
    

**Inconvénients :**

* Plus complexe à configurer car cela nécessite un framework hybride qui peut supporter à la fois le rendu côté serveur et côté client.
    
* Peut entraîner des incohérences si le serveur et le client rendent différentes versions du contenu.
    

**Idéal pour :**

* Applications avec un contenu dynamique qui nécessite un certain traitement côté serveur.
    
* Applications qui nécessitent un chargement initial rapide de la page.
    

### SSR en streaming :

**Caractéristiques principales :**

* Le serveur envoie la réponse HTML de manière continue, ce qui permet au client de commencer à rendre le contenu dès que possible.
    
* Le client peut voir le contenu être rendu progressivement, ce qui améliore l'expérience utilisateur.
    

**Avantages :**

* Temps de chargement du contenu amélioré car le client peut commencer à rendre le contenu tandis que le serveur traite toujours la requête.
    
* Meilleure expérience utilisateur car le client peut voir le contenu être rendu progressivement.
    

**Inconvénients :**

* Plus complexe à configurer car cela nécessite un framework serveur qui supporte le streaming.
    

**Idéal pour :**

* Applications avec de grandes pages ou des médias qui nécessitent un long temps de chargement.
    
* Applications qui nécessitent une expérience utilisateur fluide avec un temps d'attente minimal.
    

# Conclusion

Eh bien, tout le monde, comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/03/out-disappear.gif align="left")