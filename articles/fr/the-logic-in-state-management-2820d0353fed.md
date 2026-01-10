---
title: La logique dans la gestion d'état
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T21:09:49.000Z'
originalURL: https://freecodecamp.org/news/the-logic-in-state-management-2820d0353fed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oKxDqn4H2eJmxuNI8GY0Kg.png
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: La logique dans la gestion d'état
seo_desc: 'By Oguz Gelal

  The standardization of transactional state management brought predictability to
  front-end development. Then with immutability and single-source-of-truth for state,
  applications became more maintainable and robust. However, there is stil...'
---

Par Oguz Gelal

La standardisation de la gestion d'état transactionnelle a apporté de la prévisibilité au développement front-end. Ensuite, avec l'immuabilité et la source unique de vérité pour l'état, les applications sont devenues plus maintenables et robustes. Cependant, il reste encore une certaine ambiguïté concernant ce qu'il faut faire avec la logique métier.

Je propose un modèle où la **logique métier est opérée sous le même canal de commande que celui utilisé par les reducers**. Gérer la logique avec les mêmes transactions unidirectionnelles apporte de nombreux avantages pendant le développement. Je vais d'abord passer en revue le problème plus en détail. Ensuite, je vais expliquer comment ce modèle fonctionne avec [**Reclare**](https://github.com/reclarejs/reclare), la bibliothèque qui implémente ce modèle. Enfin, je vais discuter de certains de ces avantages.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oKxDqn4H2eJmxuNI8GY0Kg.png)
_De l'exemple [React-Reclare](https://github.com/reclarejs/reclare/tree/master/examples/request" rel="noopener" target="_blank" title="">request example</a> avec <a href="https://github.com/reclarejs/reclare" rel="noopener" target="_blank" title="">Reclare</a> et <a href="https://github.com/reclarejs/react-reclare" rel="noopener" target="_blank" title=")_

### Lutte éternelle avec les données

Dans les premiers jours, les gens construisaient des interfaces utilisateur avec du HTML et du CSS simples. Ils manipulaient le DOM (Document Object Model) en utilisant JavaScript ou jQuery. C'était raisonnable à l'époque — les applications front-end étaient simples et moins axées sur les données. Mais ensuite, la responsabilité a évolué vers la récupération et la gestion des données, au lieu de simplement les afficher. La manipulation du DOM a perdu sa faisabilité.

Les frameworks front-end [ont résolu ce problème](https://medium.com/dailyjs/the-deepest-reason-why-modern-javascript-frameworks-exist-933b86ebc445) en faisant en sorte que le DOM reflète l'état sous-jacent de l'application. Les développeurs n'avaient plus à se soucier de la mise à jour du DOM, mais la gestion de l'état était toujours de leur responsabilité.

Ensuite, la gestion d'état moderne a commencé à gagner du terrain. [Elm](https://guide.elm-lang.org/architecture/) et [Flux](https://facebook.github.io/flux/) ont standardisé la gestion d'état transactionnelle de style [event-sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) dans le développement front-end. Comment et quand l'état peut être mis à jour a été restreint avec des flux de données unidirectionnels. Cela a apporté de la prévisibilité à l'état, le rendant plus facile à suivre et à raisonner.

[Redux](https://redux.js.org/) a réalisé une percée avec l'immuabilité et la source unique de vérité pour l'état. Il a également introduit des reducers flexibles, purs, fonctionnels et composables. Cela a apporté [certains avantages](https://stackoverflow.com/a/32920459/2770460) par rapport à l'architecture Flux, mais il reste encore [une certaine ambiguïté](https://redux.js.org/faq/code-structure#how-should-i-split-my-logic-between-reducers-and-action-creators-where-should-my-business-logic-go) sur la manière de gérer la logique métier et où elle devrait résider. Il existe de nombreux articles et discussions sur ce sujet, mais aucune réponse claire ne semble exister.

Cela m'a autant confus que les autres. J'ai décidé de m'attaquer à ce problème et de trouver une manière propre de gérer la logique métier dans mes applications. Ensuite, j'ai eu l'idée de regrouper la logique métier avec les reducers. Cela a permis à la logique de fonctionner avec les reducers sous le même canal d'événements.

J'ai réalisé que cette approche apportait plus que de simples avantages organisationnels. Elle apportait d'autres avantages comme la prévisibilité et la déclarativité dans la logique. Il y avait un besoin pour une bibliothèque pour orchestrer la logique avec l'état et maintenir tous les avantages de la gestion d'état moderne. C'est à ce moment-là que j'ai décidé de créer [Reclare](https://github.com/reclarejs/reclare).

### Brève introduction à Reclare

Reclare est une bibliothèque simple qui tourne autour des **déclarations** et des **événements**. Une déclaration est un objet simple invocable par Reclare. Elle décrit **la condition situationnelle** pour son invocation, et **ce qu'il faut faire** si son invocation a lieu. Sa réaction pourrait être la mise à jour de l'état, l'exécution de la logique / des effets secondaires, ou les deux. Voici à quoi ressemble une déclaration :

[Voir un exemple sur JSFiddle](https://jsfiddle.net/r89vzhuq/)

Il s'agit d'une API à usage général et il existe différents types de déclarations. Différents types sont invoqués de différentes manières. Actuellement, il existe deux types : les déclarations d'événements et les déclarations d'abonnement.

Les **déclarations d'événements** écoutent le canal d'événements et s'abonnent à des événements spécifiques. La méthode `broadcast` peut être utilisée pour diffuser des événements vers le canal d'événements. Le premier paramètre est la clé de l'événement, suivie de la charge utile de l'événement. Cette charge utile est transmise aux fonctions de déclaration.

```
broadcast("event_key", { bar: 'foo' })
```

Les **déclarations d'abonnement** sont invoquées à chaque changement d'état. Selon le type de déclaration, les fonctions peuvent recevoir des paramètres supplémentaires, mais la structure ne change pas.

Lorsque le contexte Reclare est créé, toutes les déclarations sont fusionnées par leurs clés `on`. Cela réduit la complexité de la recherche de déclarations lors des diffusions à un temps O(1). Cela rend également le travail avec les déclarations très naturel, car il est possible d'avoir plusieurs déclarations avec la même clé d'événement. Voici un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*j1kB4R-zfkbXH4DvlKBlZw.png)
_Le cycle de vie de l'invocation de déclaration_

#### Cycle de vie de la déclaration

Le cycle de vie de la déclaration commence lorsqu'une ou plusieurs déclarations sont déclenchées. Tout d'abord, toutes les fonctions de situation de toutes les déclarations qui ont l'événement diffusé sur leur clé `on` sont évaluées. Si la condition situationnelle est remplie, les reducers et les réactions de cette déclaration sont mis en file d'attente. Ensuite, les reducers en file d'attente commencent à être exécutés.

Chacun reçoit l'état et retourne un nouvel état, qui est ensuite transmis au suivant. Chaque reducer déclenche les déclarations d'abonnement. Ils reçoivent l'état avant et après le reducer qui les a déclenchés. Ensuite, les réactions en file d'attente sont exécutées. Chaque réaction reçoit l'état initial et l'état actuel en tant qu'arguments. Elles sont exécutées après les reducers, donc l'état qu'elles reçoivent est à son état final. La charge utile de l'événement est transmise à chaque fonction exécutée à chaque étape.

### Avantages

Les bibliothèques modernes de gestion d'état se concentrent uniquement sur la gestion de l'état de l'application. La logique derrière les scènes est [souvent négligée](http://krasimirtsonev.com/blog/article/managing-state-in-javascript-with-state-machines-stent). **Il y a des avantages à opérer l'état et la logique métier ensemble**. Il est vrai qu'il doit y avoir une séparation entre les deux. Les impuretés et les effets secondaires de la logique doivent être tenus à l'écart de la gestion de l'état. Mais ils appartiennent fonctionnellement l'un à l'autre, donc ils doivent coexister et être opérés ensemble.

#### Logique prévisible

**Gérer la logique métier avec les mêmes transactions unidirectionnelles que les reducers apporte une prévisibilité similaire à la logique que celle apportée à l'état.** Cela facilite le raisonnement, le suivi, la compréhension et le test du code.

La prévisibilité dans le contexte de la logique métier n'est pas une comparaison un à un avec la prévisibilité de l'état, mais l'idée sous-jacente est la même. Les événements diffusés peuvent être enregistrés avec leurs charges utiles et les invocations qu'ils ont causées. Ainsi, il est possible de remonter dans l'historique des événements pour dire ce qui s'est passé au cours de l'exécution. Vous pourriez enquêter sur les déclarations qui ont été invoquées, les réactions qu'elles ont exécutées, et comment elles ont changé l'état.

#### **Structure du code et fragmentation**

Une base de code front-end typique contient de nombreux types d'entités différents. Par exemple, une base de code typique React + Redux + redux-saga aurait des conteneurs, des composants, des actions, des reducers, des types, des sélecteurs, des sagas, des services et d'autres selon la sélection des bibliothèques. [Dan Abramov](https://github.com/gaearon) mentionne dans son article [You might not need Redux](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367) :

> Les gens choisissent souvent Redux avant d'en avoir besoin. « Et si notre application ne scale pas sans lui ? » Plus tard, les développeurs froncent les sourcils devant l'indirection que Redux a introduite dans leur code. « Pourquoi dois-je toucher trois fichiers pour faire fonctionner une simple fonctionnalité ? » Pourquoi en effet !

Vous ne devriez pas avoir à toucher trois fichiers différents pour travailler sur une seule fonction. **Les codes qui ont une pertinence fonctionnelle ne devraient pas être fragmentés en différentes entités**. Ils devraient être regroupés et gérés ensemble.

Reclare tente de rendre cette épreuve plus agréable avec des **déclarations** et des **fichiers duck**.

Les déclarations sont des bundles qui regroupent les reducers avec les réactions. Puisqu'ils s'exécutent sur le même événement, ils seront fonctionnellement pertinents.

L'approche des **fichiers duck** est basée sur [ducks modular redux](https://github.com/erikras/ducks-modular-redux) par [Erik Rasmussen](https://github.com/erikras). Il s'agit d'une proposition pour regrouper les morceaux épars de Redux ensemble en tant que module isolé.

Reclare suit ce modèle à sa manière. Il permet de regrouper les déclarations et d'autres entités pertinentes ensemble dans un seul fichier. De plus, il supporte la composition, vous permettant d'avoir des relations parent-enfant logiques. Les fichiers duck peuvent exporter d'autres entités comme des constantes et des sélecteurs. C'est une manière simple mais pratique de diviser votre code en modules.

#### Modularité et déclarativité

Reclare opère à la fois les reducers et les réactions ensemble avec des transactions unidirectionnelles. Cela vous permet de construire votre logique de manière déclarative et modulaire. Je vais expliquer avec un scénario de connexion simple :

Le composant de formulaire de connexion diffuse `login_submitted` avec l'email et le mot de passe à la soumission. Il reçoit également le statut de chargement dans les props, qui est géré par le module de requête ci-dessous.

Ci-dessus se trouve le module qui gère le processus de connexion. La première déclaration est invoquée sur `login_submitted` si l'entrée est valide. Elle diffuse l'événement `on_request` avec les détails de la requête. Remarquez comment elle ne se soucie pas du tout de la gestion des requêtes ? Le module ne s'intéresse qu'au résultat des requêtes de type connexion.

Les deux déclarations suivantes écoutent les événements `request_success` et `request_fail`. Lors de ces événements, si la condition de type de requête est remplie, elles seront invoquées. La première sauvegarde l'utilisateur dans l'état et déclenche un changement de route, et la seconde affiche un message d'erreur.

Ceci est un exemple de module à usage général qui gère les requêtes et les états de chargement. La première déclaration est invoquée sur l'événement `on_request`. Une fois invoquée, elle définira l'état de chargement pour le type de requête, puis démarrera la requête. Ensuite, en fonction du résultat, elle diffusera les événements `request_success` ou `request_fail`. Elle diffusera également `request_resolved`, qui termine l'état de chargement.

Il y a deux points à retenir de cet exemple. Le premier est la manière dont la logique métier est gérée. La plupart des bibliothèques de gestion d'état utilisant des flux de données unidirectionnels vous permettront de gérer l'état de manière déclarative. Mais avec Reclare, vous pouvez tirer parti de ce modèle pour gérer également votre logique métier.

Le second est la modularité. Chaque déclaration et module est un morceau de code isolé qui est invoqué par des événements particuliers. Les déclarations reçoivent une charge utile et font leur travail : effectuent un ensemble d'actions et/ou mettent à jour l'état. Elles sont inconscientes et non affectées par d'autres parties du code.

Cela vous aidera à maintenir la cartographie mentale de votre code même lorsqu'il s'agrandit. Cela apporte également de nombreux avantages lors du test de votre code.

### Mots finaux

Depuis que j'ai terminé l'implémentation et les tests de Reclare, je l'ai utilisé quelques fois sur des projets secondaires et des environnements de production au travail. Jusqu'à présent, cela a été une expérience amusante, et je n'ai eu que du succès avec lui. J'espère vraiment que Reclare pourra être d'une grande aide pour la communauté autant qu'il m'a aidé.

Une dernière chose : il existe un [middleware React officiel](https://github.com/reclarejs/react-reclare) construit sur la nouvelle [Context API](https://reactjs.org/docs/context.html). Lorsque j'ai écrit cet article, Reclare était prêt à être utilisé dans un projet React. Il peut également être utilisé sans le middleware sur n'importe quel projet JavaScript. Je vais examiner la création de middlewares pour d'autres frameworks ([sauf si quelqu'un d'autre veut le faire](mailto:o.gelal77@gmail.com) ?).

En ce qui concerne les plans futurs, voici une feuille de route à court terme :

* Création de Reclare DevTools pour le débogage
* Je vais également examiner l'intégration de Redux DevTools
* Plus de documentation et d'exemples
* Lignes directrices pour les contributions
* Support de TypeScript
* Tests et améliorations sur React-Reclare
* Capacité à étendre l'API de déclaration
* `reducerDefault`/`reactionDefault`

Vous pouvez également trouver quelques exemples sur les dépôts :
**Reclare** — [https://github.com/reclarejs/reclare](https://github.com/reclarejs/reclare)
**React-Reclare** — [https://github.com/reclarejs/react-reclare](https://github.com/reclarejs/react-reclare)

![Image](https://cdn-media-1.freecodecamp.org/images/1*HXQqXwNsWy3_D7kFgEHgwg.png)