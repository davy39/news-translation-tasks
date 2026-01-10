---
title: Prise en main d'Async/Await
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-21T21:17:32.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-async-await-b66385983875
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RXBeQAwHOw_tZ2oBL4h8QA.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Prise en main d'Async/Await
seo_desc: 'By Jamund Ferguson

  Inspired by the Zeit team’s post on the subject, my team at PayPal recently migrated
  our main server-side codebase to use Async/Await. I’m excited to share with you
  some of things we learned along the way.

  Let’s start with some ter...'
---

Par Jamund Ferguson

Inspiré par [l'article de l'équipe de Zeit sur le sujet](https://zeit.co/blog/async-and-await), mon équipe chez PayPal a récemment migré notre principale base de code côté serveur pour utiliser Async/Await. Je suis ravi de partager avec vous certaines des choses que nous avons apprises en cours de route.

Commençons par quelques termes :

* **Fonction asynchrone**
* **Mot-clé Await**

Les gens disent généralement async/await, ce qui est charmant et agréable, mais vous devez savoir qu'ils ne sont pas la même chose. Il existe des _fonctions asynchrones_ et il y a le _mot-clé await_. Ils sont certainement liés de certaines manières, mais les fonctions asynchrones en particulier peuvent être utilisées sans await. Comment cela ?

#### Les fonctions asynchrones retournent une promesse

Lorsque vous créez une fonction avec le mot-clé async, cette fonction retournera toujours une Promesse. Lorsque vous retournez à l'intérieur de votre fonction asynchrone, elle enveloppe votre valeur dans une Promesse.

Même si votre code lève une exception à l'intérieur d'une fonction asynchrone, elle ne remontera pas automatiquement, mais retournera plutôt une promesse rejetée.

#### Les fonctions asynchrones sont le seul endroit où vous pouvez utiliser Await

En plus de convertir vos retours en Promesse, une fonction asynchrone est également spéciale en ce sens qu'elle est le seul endroit où vous pouvez utiliser le mot-clé await.*

Qu'est-ce que le mot-clé **await** ? Await vous permet de suspendre l'exécution d'une fonction asynchrone jusqu'à ce qu'elle reçoive les résultats d'une promesse. Cela vous permet d'écrire du code asynchrone qui se lit dans l'ordre où il est exécuté.

Await vous permet d'écrire du code asynchrone sans aucun rappel. Cela rend votre code beaucoup plus lisible. Et await fonctionne avec n'importe quelle promesse, pas seulement les promesses créées par des fonctions asynchrones.

#### Gestion des erreurs dans les fonctions asynchrones

Parce qu'une fonction asynchrone est une **Promesse**, lorsque vous **lancez** une exception à l'intérieur d'une fonction asynchrone, elle est avalée et retournée sous forme de Promesse rejetée.

Si vous utilisez **await** pour appeler la **Promesse**, vous pouvez l'envelopper dans un **try/catch** ou vous devrez ajouter un gestionnaire **catch** à la Promesse retournée.

Les erreurs de Promesse remontent généralement à leur parent, donc vous n'avez généralement besoin de ce **try/catch** que sur votre Promesse de niveau supérieur.

#### Mettre le tout ensemble

Tirer parti des propriétés de gestion des erreurs des promesses et de la syntaxe concise des fonctions asynchrones peut donner des résultats puissants et simples.

Dans cet exemple simplifié, vous pouvez voir comment on pourrait tirer parti des capacités de gestion des erreurs inhérentes aux fonctions asynchrones pour simplifier la gestion des erreurs dans une application Express.

Dans mon équipe chez PayPal, nous gérons généralement les erreurs avec **next(err)**. Cependant, avec async/await, nous pouvons simplement **lancer** des erreurs n'importe où dans le code et le routeur les transmettra à la fonction **next** fournie par Express. C'est une simplification énorme.

Passer des rappels aux promesses et à async/await a condensé la gestion des erreurs dans notre application et améliorera la compréhension pour nos chemins de code les plus compliqués. Il m'a fallu quelques heures pour migrer la plupart de nos routes des simples rappels à cette nouvelle approche. Vraiment, la seule chose dont vous avez besoin pour commencer est une [bonne connaissance des Promesses](https://medium.com/@bluepnume/learn-about-promises-before-you-start-using-async-await-eb148164a9c8#.vproogyex) et une compréhension de [comment configurer babel](https://babeljs.io/docs/setup/#installation).

J'attends avec impatience d'entendre vos expériences avec ces nouvelles fonctions et je crois qu'elles vont devenir l'un de mes outils préférés dans la boîte à outils JavaScript à l'avenir.

* L'attente de niveau supérieur n'est pas autorisée dans la spécification actuelle ([Bien qu'il y ait eu quelques discussions sur la possibilité d'autoriser cela à l'avenir](https://github.com/tc39/ecmascript-asyncawait/issues/9#issuecomment-127427447)).