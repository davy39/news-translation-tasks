---
title: 'Serverless NodeJS : la méthode rapide et économique pour construire votre
  prochain microservice'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-04T22:22:31.000Z'
originalURL: https://freecodecamp.org/news/true-er-functional-programming-on-serverless-nodejs-e532079b40d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HH3q_1O71DPFAip-v34jeg.jpeg
tags:
- name: aws lambda
  slug: aws-lambda
- name: google cloud functions
  slug: google-cloud-functions
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: serverless
  slug: serverless
seo_title: 'Serverless NodeJS : la méthode rapide et économique pour construire votre
  prochain microservice'
seo_desc: 'By Filipe Tavares

  I love Node.js. I’ve re-discovered Javascript through it, and I’m never going back.

  Its lightweight character, non-blocking nature, and quick development experience
  shine in Microservices.

  I also love Express — it makes writing serv...'
---

Par Filipe Tavares

J'adore [Node.js](https://nodejs.org). J'ai redécouvert Javascript grâce à lui, et je ne reviendrai jamais en arrière.

Son caractère léger, sa nature non bloquante et son expérience de développement rapide brillent dans les Microservices.

J'adore aussi [Express](http://expressjs.com) — il rend l'écriture d'applications serveur si simple. Et son approche basée sur la pile de middleware [Connect](https://github.com/senchalabs/connect) rend l'extension des applications facile et amusante. Couplez-le avec Docker et le ciel est la limite. Ou mieux encore, passez au serverless.

### Plus petit que petit…

![Image](https://cdn-media-1.freecodecamp.org/images/1*HH3q_1O71DPFAip-v34jeg.jpeg)

D'abord, ils nous ont donné des Serveurs, alors nous avons construit des Architectures Orientées Services.

Ensuite, ils nous ont donné des Conteneurs, alors nous avons construit des Microservices.

Maintenant, ils nous donnent des **Gestionnaires d'Événements Serverless**, alors nous construirons des **Fonctions**.

Nos plateformes d'hébergement sont devenues plus adaptées au déploiement d'unités plus petites. Et nos applications se sont également décomposées en packages logiciels plus petits. Il y a de nombreuses raisons à cela, et les opinions divergent sur le fait que ce soit une bonne chose.

Mais si nous regardons en arrière les concepts originaux derrière le cloud computing, il y avait un rêve de voir le code distribué infiniment dans un réseau de nœuds de calcul connectés. Nous nous en approchons un peu plus avec l'émergence des plateformes serverless.

De plus : elles nous permettent de scalabilité _infinie_, tout en ne payant que pour ce que nous utilisons.

### …mais pas trop petit

Les séquences d'étapes de calcul (procédures) ont besoin de mémoire partagée pour s'exécuter efficacement. Nous les enveloppons autour d'une définition de fonction, qui définit un contrat pour ses entrées et sorties. Et cela permet la composition avec d'autres fonctions.

Cette approche a été très réussie dans l'architecture de [Unix](http://www.linfo.org/unix_philosophy.html), et est l'une des raisons de sa longévité et de son ubiquité. Je ne veux pas suggérer que les applications Web devraient suivre un écosystème partagé comparable basé sur le cloud (bien que [certains](https://stdlib.com/) essaient). Mais nous pouvons bénéficier de l'application de principes similaires lors de la construction d'applications Web.

Au-delà des définitions de fonctions, nous regroupons également les fonctions étroitement liées dans des modules. Un exemple pourrait être les opérations CRUD pour les données dans un domaine donné, comme la gestion des utilisateurs. Celles-ci tendent à partager du code, comme des modèles de données, une logique d'analyse et de formatage. Donc, lorsque nous déployons des fonctions individuelles dans des environnements serverless, nous finissons avec beaucoup de code dupliqué.

Les environnements serverless actuels encouragent le déploiement de fonctions uniques. Mais, lorsqu'ils sont appliqués aux Microservices, cela conduit à des piles désordonnées difficiles à gérer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SBCdivCfxRGAk_ShI9h6iw.jpeg)

Mais supposons que nous ne nous soucions pas des déploiements de code dupliqué. Après tout, nous pouvons le gérer dans nos dépôts de code. Nous voulons toujours partager des ressources temporaires, comme les connexions à la base de données. Nous voulons également nous assurer que nous déployons et gérons toutes les opérations pour le même domaine en tant qu'unité unique. Nous sommes mieux lotis en gérant des **modules de fonctions**.

Cela s'aligne bien avec le [Principe de Responsabilité Unique](http://programmer.97things.oreilly.com/wiki/index.php/The_Single_Responsibility_Principle) :

> Regroupez les choses qui changent pour la même raison, et séparez les choses qui changent pour des raisons différentes.

### Passer au serverless

Ainsi, Node.js est idéal pour les Microservices. Et il est également idéal pour écrire des modules de fonctions plus petits. Et Express est idéal pour construire des applications Web en Node.js.

Pourtant, la plupart des environnements serverless gèrent déjà de nombreuses fonctions courantes de serveur Web dès la sortie de la boîte. Et pour ces **Nanoservices**, qui fournissent une poignée de fonctions, nous ne devrions pas nous embarrasser de la surcharge de la logique complexe de serveur Web. Nous devons exploiter HTTP, car il s'agit du mécanisme de transport ubiquitaire entre les services Web. Mais nous devrions le faire de manière plus [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) (Remote Procedure Call).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bHajXlOuEmcVMYoW7_wLOg.jpeg)

C'est là que la plupart des frameworks actuels offrent un marteau-pilon pour casser une noix. Si quoi que ce soit, je soutiendrais que le passage au serverless nous libère des _frameworks_, pour nous concentrer plutôt sur la construction de fonctions plus _pures_.

Pourtant, il y a un besoin de routage de base au sein d'un Nanoservice, pour mapper les requêtes entrantes à la fonction de gestion appropriée. De plus, en raison de la nature propriétaire de ces environnements serverless commerciaux, nous pouvons justifier d'avoir un certain niveau d'abstraction, pour découpler nos fonctions des spécificités de la plateforme sur laquelle elles sont exécutées.

La programmation fonctionnelle appliquée aux déploiements serverless est susceptible de se manifester dans plus d'applications. Ce qui me rend très optimiste, car cela semble être un pas dans la bonne direction. Nous devons encore aborder de nombreuses considérations du monde réel comme la latence, la performance et l'utilisation de la mémoire. Mais comme avec les Microservices, nous trouverons le bon ensemble d'outils et de pratiques pour rendre cela non seulement pratique, mais aussi très performant dans les applications du monde réel.

### Modules dans les Cloud Functions

J'ai écrit un petit package Node.js pour répondre à ces besoins. Il s'appelle [modofun](https://modofun.js.org).

![Image](https://cdn-media-1.freecodecamp.org/images/1*h555w9EzrmhNvKg_3FtagQ.png)

Il n'a pas de dépendances supplémentaires, car nous voulons que nos déploiements soient aussi petits que possible. Il ajoute une fonctionnalité minimale pour simplifier les déploiements de modules de fonctions sur des plateformes serverless. Il permet également l'extensibilité grâce à des middleware existants, tels que l'authentification, la journalisation, et autres. Voici quelques-unes de ses fonctionnalités :

* Routage de base vers les fonctions
* Analyse des paramètres
* Construction automatique de la réponse HTTP
* Support des Promesses ES6 (ou tout autre then-able)
* Support de middleware de type Connect/Express
* **Google Cloud Functions**
* **AWS Lambda** (avec les événements AWS API Gateway)
* Gestion automatique des erreurs

Le support pour Azure Functions arrive bientôt.

### Utilisation de Modofun

Modofun facilite l'exposition de fonctions en tant que gestionnaires de requêtes cloud serverless :

![Image](https://cdn-media-1.freecodecamp.org/images/1*caoa_S2By0fMnsyAErSDOA.png)

Un routeur simpliste mappe les requêtes entrantes aux fonctions. Il applique les composants finaux du chemin d'URL comme arguments de fonction. D'autres données de requête sont également disponibles en tant que contexte (_this_) pour l'invocation de la fonction.

Nous pouvons spécifier un middleware qui s'exécutera pour chaque requête entrante. Ou l'appliquer sélectivement à des fonctions individuelles (plus de détails dans la [documentation](https://modofun.js.org/#configuration)). Modofun retourne le gestionnaire approprié pour les événements générés par la plateforme serverless.

Obtenez-le avec [npm](https://www.npmjs.com/package/modofun) :

```
npm install modofun
```

Pour plus d'exemples et une documentation détaillée, rendez-vous sur le [site officiel](https://modofun.js.org). Vous pouvez également trouver le code source complet sur [GitHub](https://github.com/modofunjs/modofun).