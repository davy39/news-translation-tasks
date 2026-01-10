---
title: Introduction à Redux et comment l'état est mis à jour dans une application
  Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-07T16:24:19.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-redux-and-how-state-is-updated-in-a-redux-application-839c8334d1b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VLQNO9Apn9qfm6BPYXG8TA.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Introduction à Redux et comment l'état est mis à jour dans une application
  Redux
seo_desc: 'By Syeda Aimen Batool

  I started learning Redux a few days back and it was an overwhelming concept for
  me at the start. After polishing my skills in ReactJS by making a personal book
  reading application, I headed towards Redux to learn more about it.

  ...'
---

Par Syeda Aimen Batool

J'ai commencé à apprendre Redux il y a quelques jours et c'était un concept accablant pour moi au début. Après avoir perfectionné mes compétences en ReactJS en créant une [application personnelle de lecture de livres](https://github.com/aimenbatool/my-reads), je me suis tournée vers Redux pour en apprendre davantage.

Aujourd'hui, je vais partager quelques concepts fondamentaux de Redux sans utiliser de bibliothèque de vue (React ou Angular). C'est une sorte de note personnelle pour référence future, mais elle peut aussi aider les autres.

Plongeons ensemble !

### Qu'est-ce que Redux ?

Redux est une bibliothèque open-source pour améliorer la prévisibilité de l'état dans une application JavaScript. C'est une bibliothèque indépendante. Elle est couramment utilisée avec d'autres bibliothèques comme React et Angular pour une meilleure gestion de l'état de l'application. Redux a été créé par Dan Abramov en 2015 pour gérer la gestion d'état complexe de manière efficace.

Lorsque une application grandit, il devient plus difficile de gérer l'état et de déboguer les problèmes. Il devient un défi de suivre quand et où l'état est changé et où les changements doivent être reflétés. Parfois, une entrée utilisateur déclenche un appel API qui met à jour un modèle. Ce modèle met à son tour à jour un état ou peut-être un autre modèle, et ainsi de suite.

Dans une telle situation, il devient fastidieux de suivre les changements d'état. Cela se produit principalement parce qu'il n'y a pas de règle définie pour mettre à jour un état et que l'état peut être changé de n'importe où à l'intérieur de l'application.

Redux essaie de résoudre ce problème en fournissant quelques règles simples pour mettre à jour l'état afin de le garder prévisible. Ces règles sont les blocs de construction de Redux.

### Redux Store :

Comme nous l'avons discuté précédemment, le but principal de Redux est de fournir une gestion d'état prévisible dans nos applications. Redux y parvient en ayant une seule source de vérité, c'est-à-dire un **arbre d'état unique**. L'arbre d'état est un simple objet JavaScript qui contient tout l'état de notre application. Il n'y a que quelques façons d'interagir avec l'état. Et cela nous facilite le débogage ou le suivi de notre état.

Nous avons maintenant un seul état principal qui occupe tout l'état de l'application situé à un seul endroit. Tout changement apporté à l'arbre d'état est reflété dans toute l'application car c'est la seule source de données pour l'application. Et c'est le premier principe fondamental de Redux.

#### Règle #1 — [Single source of truth](https://redux.js.org/introduction/three-principles#single-source-of-truth)

> L'état de votre application est stocké dans un arbre d'objets au sein d'un seul store. — Documentation officielle

Les façons dont vous pouvez interagir avec un arbre d'état sont :

* Obtenir l'état
* Écouter les changements dans l'état
* Mettre à jour l'état

Un **store** est une unité unique qui contient l'**arbre d'état** et les **méthodes** pour interagir avec l'arbre d'état. Il n'y a pas d'autre façon d'interagir avec un état à l'intérieur du store sauf par ces méthodes données.

![Image](https://cdn-media-1.freecodecamp.org/images/cDBhHN7x5f-p6JRrZ-1ekpbDx7s0aW4j3jUr)

Parlons des méthodes qu'un store nous donne pour interagir avec l'état.

* getState() — Retourne l'état actuel de l'application.
* dispatch(action) — La seule façon de mettre à jour un état est d'envoyer une action et `dispatch(action)` sert à cela. Nous en parlerons plus en détail dans un instant.
* subscribe(listener) — Le but de cette méthode est d'écouter les changements d'état. Chaque fois qu'un état est changé, il sera appelé et retournera l'état mis à jour.
* replaceReducer(nextReducer) — Remplace le réducteur actuellement utilisé par le store pour calculer l'état.

Maintenant que nous avons un store qui contient un arbre d'état et quelques façons d'interagir avec l'état, comment pouvons-nous mettre à jour l'état de l'application ?

### Mise à jour de l'état dans l'application :

_La seule façon de mettre à jour un état est d'envoyer une action. C'est la 2ème règle._

#### Règle #2 — [State is read-only](https://redux.js.org/introduction/three-principles#state-is-read-only)

Une action est un objet JavaScript simple pour suivre l'événement spécifique qui se produit dans l'application. Ce qui le rend spécial est une propriété 'type' qui en est une partie nécessaire.

```
{  type: "ADD_BOOK_TO_THE_CART"}
```

Le but principal de cette propriété est de faire savoir à Redux l'événement qui se produit. Ce type doit être descriptif de l'action. En plus de la propriété 'type', il peut avoir d'autres informations sur l'événement qui se produit.

Les actions peuvent avoir autant d'informations que vous le souhaitez. Il est bon de fournir moins et des informations nécessaires — de préférence un identifiant ou un identifiant unique chaque fois que possible.

Ici, nous avons une action pour ajouter un livre au panier.

Une fois que nous avons défini notre action, nous la passons au dispatcher. **store.dispatch()** est une fonction fournie par la bibliothèque qui accepte une action pour effectuer une action contre l'état. Redux restreint la mise à jour de l'état à cette méthode uniquement.

Cette façon stricte de mettre à jour l'état garantit que l'état ne peut pas être changé directement soit par la vue soit par un rappel réseau. La seule façon de mettre à jour un état est de définir l'action et ensuite de l'envoyer. Rappelez-vous que les actions sont des objets JavaScript simples. Les actions peuvent être enregistrées, sérialisées et rejouées à des fins de débogage.

Nous avons maintenant un store, un état et une action dans notre application pour effectuer certaines tâches contre l'état. Maintenant, nous avons besoin d'un moyen d'utiliser ces actions pour effectuer réellement la mise à jour. Cela peut être fait en utilisant une fonction pure et c'est la règle #3.

![Image](https://cdn-media-1.freecodecamp.org/images/h4w-r3zcxAOODzC-u5TKDip1joPotFfNCzVx)

#### Règle #3 — [Changes are made with pure functions](https://redux.js.org/introduction/three-principles#state-is-read-only)

La magie opère ici. Nous avons besoin d'une fonction pure simple qui, en tant que paramètre, prend l'état actuel de l'application et une action à effectuer sur l'état, puis retourne l'état mis à jour. Ces fonctions sont appelées réducteurs.

Elles sont appelées réducteurs parce qu'elles prennent la collection de valeurs, la réduisent à un état mis à jour et la retournent. Puisque les réducteurs sont des fonctions pures, ils ne mutent pas l'état original. Au lieu de cela, ils retournent l'état mis à jour dans un nouvel objet. Notre application peut avoir un ou plusieurs réducteurs. Chaque réducteur peut avoir un état pertinent pour effectuer des tâches spécifiques.

Puisque les réducteurs sont des fonctions pures, ils doivent avoir les attributs suivants :

* Étant donné la même entrée, il doit retourner la même sortie chaque fois — Aucune mutation n'est autorisée.
* Aucun effet secondaire — Aucun appel API, aucun changement de données à partir d'une source externe.

#### Le processus.

Si nous relions les points, Redux est une bibliothèque qui a un store contenant un arbre d'état et quelques méthodes pour interagir avec l'état. La seule façon de mettre à jour un état à l'intérieur d'un store est d'envoyer une action et de définir une fonction de réducteur pour effectuer des tâches basées sur les actions données. Une fois envoyée, l'action va à l'intérieur des fonctions de réducteur qui effectuent les tâches et retournent l'état mis à jour au store. C'est ce qu'est Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/MNhhFTlpazu2H0YgQ7D7BhtZ7SYfdI4xA5Gk)
_Flux de mise à jour de l'état dans Redux_

### Qu'avons-nous appris jusqu'à présent ?

Résumons ce que nous avons appris jusqu'à présent pour relier les points.

* [Redux](https://redux.js.org/introduction/getting-started#getting-started-with-redux) — Un conteneur d'état prévisible open-source
* Arbre d'état — Un objet JavaScript simple qui contient tout l'état de l'application
* Trois façons d'interagir avec un état (les seules façons) :  
[**Store**](https://redux.js.org/basics/store#store) — Une unité unique qui contient l'arbre d'état et les méthodes pour interagir avec l'arbre d'état  
**Actions** — Objets JavaScript simples pour décrire l'action en cours  
**Réducteurs** — Fonctions JavaScript pures pour prendre l'état actuel et une action pour retourner un nouvel état

Puisque Redux est une bibliothèque indépendante qui peut être utilisée avec React, Angular ou toute autre bibliothèque, j'ai évité de créer une application d'exemple avec l'une de ces bibliothèques de vue. Au lieu de cela, je me suis concentrée uniquement sur les concepts fondamentaux de Redux.

Redux peut être accablant au début et si vous êtes un débutant ou un développeur junior, cela peut vous donner du fil à retordre. Mais la constance et une attitude positive sont la clé du succès. Si vous avez du mal à survivre en tant que développeur junior et que vous cherchez de la motivation, vous pouvez lire comment [j'ai lutté pour surmonter les défis auxquels j'ai été confrontée en tant que développeur junior.](https://medium.freecodecamp.org/how-im-working-to-overcome-my-struggles-as-a-junior-developer-a6ab18ac29b2)

Dites bonjour [@aimenbatool.](https://twitter.com/AimenBatool)