---
title: Comment communiquer entre les composants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:38:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-communicate-between-components-b48ef70bf913
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MdWVvVEI6qmBhyYfa5p4_A.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment communiquer entre les composants
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Components are a tool for splitting the page in smaller pieces that are easier to
  manage and reuse. By breaking the page ...'
---

Par Cristian Salcescu

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Les composants sont un outil pour diviser la page en plus petites parties qui sont plus faciles à gérer et à réutiliser. En divisant la page en plus petites parties, nous simplifions leur implémentation.

Mais en même temps, cela crée un nouveau défi : la communication entre ces petites parties.

### Un exemple

Je vais prendre comme exemple une page gérant une liste de tâches. L'utilisateur peut voir, ajouter et rechercher des tâches.

Voici à quoi ressemble la page :

![Image](https://cdn-media-1.freecodecamp.org/images/SdPLBMLKMH2E8k6dpvOlAXgvFtmOchIavoMe)

### Identifier les composants

Nous pouvons diviser la page en trois composants principaux basés sur leurs responsabilités :

* `TodoAddForm` : le formulaire pour ajouter une nouvelle tâche
* `TodoSearchForm` : le formulaire pour rechercher une tâche
* `TodoList` : la liste pour afficher les tâches

Nous pouvons aller encore plus loin et faire en sorte que chaque élément de la liste ait son propre composant : `TodoListItem`

Pour les besoins de cette analyse, j'encapsule la zone de texte et le bouton dans leurs propres composants : `FormInput`, `FormButton`.

### Les composants sont dans une structure arborescente

Avant d'analyser comment communiquer entre les composants, nous devons comprendre que les composants sont organisés dans une structure arborescente. Si le framework n'impose pas de composant racine, alors nous en créerons un.

Créons maintenant la structure arborescente :

![Image](https://cdn-media-1.freecodecamp.org/images/-DfvdcfTZOQTJRN-ARB6dNkbWr5cREy5r6Qk)
_Structure arborescente des composants_

### Composants de présentation et conteneurs

Nous pouvons commencer à définir les responsabilités des composants en utilisant le modèle de conteneurs et de présentation.

Le modèle est décrit dans [Presentational and Container Components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) et [Container Components](https://medium.com/@learnreact/container-components-c0e67432e005)

Les composants de présentation communiquent uniquement par le biais de leurs propres propriétés, méthodes et événements. Ils ne sont pas connectés à des objets de communication externes. Cela rend les composants de présentation plus faciles à comprendre et plus réutilisables, car ils ne sont pas couplés à d'autres objets.

Les composants conteneurs sont connectés à des objets externes. Ils écoutent les événements de ces objets et effectuent des actions. Ils fournissent des données à l'interface utilisateur.

Je vais commencer avec un seul composant conteneur racine : `TodoContainer`. Tous les autres seront des composants de présentation : `TodoAddForm`, `TodoSearchForm`, `TodoList`, `TodoListItem`, `FormInput` et `FormButton`.

Il existe de nombreux moyens de communication à notre disposition. En fin de compte, nous devons choisir celui qui est approprié pour notre situation.

En résumé, ces moyens de communication sont :

* Parent → Enfant : propriétés, méthodes
* Enfant → Parent : événements, rappels
* Enfant → Enfant : via le parent, le magasin de domaine, le magasin UI ou le bus d'événements global. 
En bref, deux composants enfants peuvent communiquer en utilisant leur parent le plus proche ou un objet tiers partagé.

Vous pouvez en savoir plus dans le livre [Discover Functional JavaScript](https://www.amazon.com/dp/B07PBQJYYG).

Lisez [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) et apprenez à construire des applications en style fonctionnel.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------)**.**

Vous pouvez me trouver sur [Medium](https://medium.com/@cristiansalcescu) et [Twitter](https://twitter.com/cristi_salcescu).