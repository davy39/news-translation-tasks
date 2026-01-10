---
title: Remplacer Redux par la nouvelle API de contexte React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T20:34:43.000Z'
originalURL: https://freecodecamp.org/news/replacing-redux-with-the-new-react-context-api-8f5d01a00e8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G-vhFzhkTXo1cHSLY0y-rg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Remplacer Redux par la nouvelle API de contexte React
seo_desc: 'By Didier FRANC

  The new context API that comes with React 16.3 is pretty neat. It was built in the
  render props style trending over these last months. Let’s explore it:

  It’s pretty nice right? Let’s go further with Flux-like implementation.

  What’s Fl...'
---

Par Didier FRANC

La nouvelle API de contexte qui accompagne React 16.3 est assez remarquable. Elle a été construite dans le style _render props_ qui est en vogue ces derniers mois. Explorons-la :

C'est assez bien, n'est-ce pas ? Allons plus loin avec une implémentation de type Flux.

### Qu'est-ce que Flux ?

Cette conférence de l'excellente Jing Chen a révolutionné la façon dont nous pensons à nos applications aujourd'hui. Si vous voulez savoir ce qu'est Flux en tant que concept, [jetez un œil ici](https://github.com/facebook/flux/blob/master/examples/flux-concepts/README.md).

![Image](https://cdn-media-1.freecodecamp.org/images/1*krW1XEfCCHg1eQFrPJMrqA.png)
_Une représentation basique de Flux_

Une bibliothèque a démocratisé ce concept : [Redux](https://redux.js.org/basics) de Dan Abramov et sa légendaire démonstration de voyage dans le temps à React Europe 2015.

### Implémentation

Avec l'exemple d'API **createContext()** ci-dessus, nous avons déjà en place le flux unidirectionnel **Store → View**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Do6ERUrJHSj9Vmw0ngwIHg.png)

Ce dont nous avons besoin, ce sont des **actions** et des **dispatchers** pour mettre à jour dynamiquement le store. Et si notre store dynamique n'était que l'état d'un composant racine React ?

Nous venons de passer l'état et les actions en tant que valeurs du provider. Et maintenant, nous pouvons les obtenir avec **<Consumer />**.

J'ai créé une bibliothèque pour avoir tout ce dont nous avons besoin pour utiliser ce flux de données facilement tout en gardant de grandes performances.

### [react-waterfall](https://github.com/didierfranc/react-waterfall)

![Image](https://cdn-media-1.freecodecamp.org/images/1*O6SqDvFqwhpqj9TUVzxFVw.png)
_Dépôt d'exemple disponible [**ici**](https://github.com/didierfranc/react-stateful-example" rel="noopener" target="_blank" title=")_

Il suffit d'importer **initStore** depuis [**react-waterfall**](https://github.com/didierfranc/react-waterfall), de définir votre **état initial**, et de prendre quelques actions : **(state, …arg) → stateChunk** — et vous êtes prêt à partir.

Le **store** créé vous offre quelques fonctionnalités sympas comme :

* Le **Provider** et le **Consumer** améliorés présentés ci-dessus
* **actions** (vous pouvez y accéder depuis **Consumer**, aussi)
* **getState()** pour obtenir l'état actuel
* **connect()()** pour mapper l'état et les actions aux props du composant
* **subscribe()** pour réagir aux changements d'état

Si vous avez besoin de sélecteurs plus profonds et/ou de données calculées mémoïsées, vous pouvez, bien sûr, utiliser [**reselect**](https://github.com/reactjs/reselect). Consultez cet exemple [ici](https://github.com/didierfranc/react-waterfall/blob/v3/examples/reselect/src/store/selectors.js).

Si vous voulez le **voyage dans le temps**, c'est possible ? Il suffit d'exécuter c[e exemple.](https://github.com/didierfranc/react-stateful-example) L'implémentation est juste i[ci.](https://github.com/didierfranc/react-stateful-example/blob/master/src/devtool.js)

### Comparaison avec Redux

![Image](https://cdn-media-1.freecodecamp.org/images/1*22lo3_HFH1lIWVSmgJdd5g.png)

⏱️ Les Redux Devtools ont été [intégrés](https://github.com/didierfranc/react-waterfall/blob/master/src/helpers/devtools.js) par défaut dans la version 4.0.0, vous n'avez rien à faire, cela fonctionne simplement.

**Avantages**

* Plus facile à implémenter
* Poids et performance
* Retour d'action plus propre avec un morceau d'état (comme dans setState)

**Inconvénients**

* Cela ne fonctionne qu'avec React ^16.3

### Vous voulez l'essayer ?

J'ai trouvé un nom sexy pour cela, mais si vous avez une idée pour cela, postez vos suggestions ici ou envoyez-moi un tweet.

> yarn add react-waterfall

?

### Plus

Si vous êtes intéressé par les nouvelles fonctionnalités clés de **React**, ne manquez pas [**"When react has become (even more) asynchronous"**](https://medium.com/@DidierFranc/when-react-has-become-even-more-asynchronous-37a55c3a3d3).

Si vous ne voulez pas manquer mes articles, suivez-moi sur twitter [@DidierFranc](http://twitter.com/didierfranc)