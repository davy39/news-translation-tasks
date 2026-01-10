---
title: Une introduction au modèle architectural Flux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T18:23:03.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-flux-architectural-pattern-674ea74775c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7qtRmuWoMmFyhpnyxoS3MA.png
tags:
- name: Flux
  slug: flux
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction au modèle architectural Flux
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Flux is an architectural pattern proposed by Facebook for building SPAs. It suggests
  to split the application into the fo...'
---

Par Cristian Salcescu

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Flux est un modèle architectural proposé par Facebook pour construire des SPAs. Il suggère de diviser l'application en les parties suivantes :

* Stores
* Dispatcher
* Vues
* Action / Action Creators

### Store

Le Store gère l'état. Il peut stocker à la fois l'état du domaine et l'état de l'interface utilisateur.

Store et état sont des concepts différents. L'état est la valeur des données. Le Store est un objet comportemental qui gère l'état à travers des méthodes. Dans le cas de la gestion des livres : la liste des livres est l'état et BookStore gère cette liste.

Un store gère plusieurs objets. Il est la seule source de vérité concernant ces objets spécifiques. Dans une application, il peut y avoir plusieurs stores. Par exemple : BookStore, AuthorStore, UserStore.

Il n'y a pas de méthodes setter sur le store. Vous ne pouvez demander un changement d'état qu'en passant une action au dispatcher.

Un store écoute toutes les actions et décide sur lesquelles agir. Cela signifie généralement une instruction `switch`. Une fois que le store a effectué les changements d'état, il émettra un événement de changement. Le store est un émetteur d'événements.

Les stores ne prennent pas d'autres stores comme dépendances.

### Dispatcher

Le Dispatcher est un objet unique qui diffuse les actions/événements à tous les stores enregistrés. Les stores doivent s'enregistrer pour les événements lorsque l'application démarre.

Lorsque une action arrive, elle la passera à tous les stores enregistrés.

### Vue

La Vue est le composant de l'interface utilisateur. Elle est responsable du rendu de l'interface utilisateur et de la gestion de l'interaction utilisateur. Les vues sont dans une structure arborescente.

Les vues écoutent les changements de store et se re-rendent.

Les vues peuvent être divisées en vues de présentation et vues conteneurs.

Les vues de présentation ne se connectent pas au dispatcher ou aux stores. Elles communiquent uniquement par leurs propres propriétés.

Les vues conteneurs sont connectées aux stores et au dispatcher. Elles écoutent les événements des stores et fournissent les données pour les composants de présentation. Elles obtiennent les nouvelles données en utilisant les méthodes getter publiques des stores et transmettent ensuite ces données dans l'arborescence des vues.

Les vues conteneurs dispatchent des actions en réponse à l'itération utilisateur.

### Actions

Une action est un objet simple qui contient toutes les informations nécessaires pour effectuer cette action.

Les actions ont une propriété `type` identifiant le type d'action.

Lorsque les objets d'action se déplacent dans l'application, je suggère de les rendre immuables.

Les actions peuvent provenir de différents endroits. Elles peuvent provenir des vues suite à une interaction utilisateur. Elles peuvent provenir d'autres endroits comme le code d'initialisation, où les données peuvent être prises à partir d'une API Web et des actions sont déclenchées pour mettre à jour les vues. Les actions peuvent provenir d'un minuteur qui nécessite des mises à jour de l'écran.

### Action Creators

La pratique consiste à encapsuler le code, créant des actions dans des fonctions. Ces fonctions qui créent et dispatchent des actions sont appelées action creators.

#### Appels d'API Web

Lors de l'exécution d'appels d'API Web pour mettre à jour l'interface utilisateur, l'appel d'API Web sera suivi d'une action pour mettre à jour le store. Lorsque le store est mis à jour, il émettra un événement de changement et, par conséquent, la vue qui écoute cet événement se re-rendra.

Les appels d'API Web sont effectués dans les action creators. Nous pouvons extraire le code qui effectue l'appel d'API dans des fonctions Web API Utils.

### Flux de données unidirectionnel

La mise à jour des vues se fait dans une seule direction :

![Image](https://cdn-media-1.freecodecamp.org/images/B3swRnUORvq-CH8yZO-Pgy9ZiAmN5LPlgMM3)

Les vues ne modifient pas les données qu'elles ont reçues. Elles écoutent les changements de ces données, créent des actions avec de nouvelles valeurs, mais ne mettent pas à jour les données.

Les stores, les vues et toute autre action ne peuvent pas changer l'état dans (d'autres) stores directement. Ils doivent envoyer une action via le dispatcher.

Le flux de données est plus court dans les lectures de store que dans les écritures. Le flux de données dans les écritures de store diffère entre les actions asynchrones et synchrones.

Lectures de Store

![Image](https://cdn-media-1.freecodecamp.org/images/toNPHVZBnlFDPKHyp142thO9y7f6tQzREs7T)

Écritures de Store dans les actions synchrones

![Image](https://cdn-media-1.freecodecamp.org/images/JQ2bHtD7C0rtKjNAHAYSD7TdPbRnV04WWyBg)

Écritures de Store dans les actions asynchrones

![Image](https://cdn-media-1.freecodecamp.org/images/U857Xuskoy-w6aGMC--FfAyIAUEyMj13JETi)

### Avantages

L'architecture Flux est meilleure dans une application où les vues ne mappent pas directement aux stores de domaine. En d'autres termes, lorsque les vues peuvent créer des actions qui mettront à jour de nombreux stores et que les stores peuvent déclencher des changements qui mettront à jour de nombreuses vues.

Les actions peuvent être persistées puis rejouées.

### Inconvénients

Flux peut ajouter une complexité inutile à une application où chaque vue mappe à un store. Dans ce type d'application, une séparation entre la vue et le store est suffisante.

Prenez par exemple un coup d'œil à [Comment créer une application à trois couches avec React](https://medium.freecodecamp.org/how-to-create-a-three-layer-application-with-react-8621741baca0).

### Conclusion

Les stores gèrent l'état. Ils changent l'état uniquement en écoutant les actions. Les stores notifient les vues pour les mettre à jour.

Les vues rendent l'interface utilisateur et gèrent l'interaction utilisateur. Les vues conteneurs écoutent les changements de store.

Le dispatcher diffuse les actions à tous les stores enregistrés.

Les actions sont des objets simples.

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivre sur Twitter](https://twitter.com/cristi_salcescu)