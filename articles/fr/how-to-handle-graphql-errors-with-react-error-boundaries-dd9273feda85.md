---
title: Pages d'erreur personnalisées dans React avec GraphQL et Error Boundaries
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T20:26:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-graphql-errors-with-react-error-boundaries-dd9273feda85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*20J63XycbuDOp4NRTLKeMQ.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Pages d'erreur personnalisées dans React avec GraphQL et Error Boundaries
seo_desc: 'By Abi Noda

  _If you like this article please support me by checking out Pull Reminders, a Slack
  bot that sends your team automatic reminders for GitHub pull requests._

  One challenge I recently ran into while working with GraphQL and React was how to
  ...'
---

Par Abi Noda

*Si vous aimez cet article, soutenez-moi en découvrant [**Pull Reminders**](https://pullreminders.com/?utm_source=medium&utm_medium=react-errors), un bot Slack qui envoie à votre équipe des rappels automatiques pour les pull requests GitHub.*

Un défi que j'ai récemment rencontré en travaillant avec GraphQL et React était la gestion des erreurs. En tant que développeurs, nous avons probablement déjà implémenté des pages 500, 404 et 403 par défaut dans des applications rendues côté serveur, mais déterminer comment faire cela avec React et GraphQL est délicat.

Dans cet article, je vais parler de la manière dont notre équipe a abordé ce problème, de la solution finale que nous avons implémentée, et des leçons intéressantes tirées de la spécification GraphQL.

### Contexte

Le projet sur lequel je travaillais était une application CRUD assez typique construite en React utilisant GraphQL, [Apollo Client](https://www.apollographql.com/docs/react/), et [express-graphQL](https://github.com/graphql/express-graphql). Nous voulions gérer certains types d'erreurs — par exemple, lorsque le serveur est hors service — en affichant une page d'erreur standard à l'utilisateur.

Notre premier défi était de déterminer la meilleure façon de communiquer les erreurs au client. GraphQL n'utilise pas les codes de statut HTTP comme 500, 400 et 403. Au lieu de cela, les réponses contiennent un tableau `errors` avec une liste des problèmes survenus (lisez plus sur les `errors` dans la [spécification GraphQL](http://facebook.github.io/graphql/June2018/#sec-Response-Format)).

Par exemple, voici à quoi ressemblait notre réponse GraphQL lorsque quelque chose se brisait sur le serveur :

Puisque les réponses d'erreur GraphQL retournent un code de statut HTTP 200, la seule façon d'identifier le type d'erreur était d'inspecter le tableau `errors`. Cela semblait être une mauvaise approche car la propriété `message` de l'erreur contenait l'exception levée sur le serveur. La [spécification GraphQL](http://facebook.github.io/graphql/June2018/#sec-Errors) indique que la valeur de `message` est destinée aux développeurs, mais elle ne précise pas si la valeur doit être un message lisible par l'homme ou quelque chose conçu pour être traité de manière programmatique :

> Chaque erreur doit contenir une entrée avec la clé message avec une description sous forme de chaîne de l'erreur destinée au développeur comme guide pour comprendre et corriger l'erreur.

### Ajout de codes d'erreur aux réponses GraphQL

Pour résoudre ce problème, nous avons ajouté des codes d'erreur standardisés à nos objets d'erreur, qui pourraient être utilisés par les clients pour identifier les erreurs de manière programmatique. Cela a été inspiré par la façon dont l'API REST de Stripe retourne des [codes d'erreur](https://stripe.com/docs/error-codes) sous forme de chaîne en plus des messages lisibles par l'homme.

Nous avons décidé de commencer avec trois codes d'erreur : `authentication_error`, `resource_not_found` et `server_error`.

Pour les ajouter à nos réponses GraphQL, nous avons passé notre propre fonction `formatError` à express-graphql qui mappe les exceptions levées sur le serveur à des codes standard qui sont ajoutés à la réponse. La spécification GraphQL [décourage généralement l'ajout de propriétés aux objets d'erreur](http://facebook.github.io/graphql/June2018/#example-fce18), mais permet de le faire en imbriquant ces entrées dans un objet `extensions`.

Nos erreurs de réponse GraphQL étaient alors faciles à classer :

Alors que nous avons développé notre propre manière d'ajouter des codes aux réponses générées par [express-graphql](https://github.com/graphql/express-graphql), apollo-server semble offrir un [comportement intégré similaire](https://www.apollographql.com/docs/apollo-server/v2/features/errors.html#Codes).

### Affichage des pages d'erreur avec les Error Boundaries de React

Une fois que nous avons trouvé une bonne façon de gérer les erreurs sur notre serveur, nous nous sommes tournés vers le client.

Par défaut, nous voulions que notre application affiche une page d'erreur globale (par exemple, une page avec le message "oops quelque chose s'est mal passé") chaque fois que nous rencontrions un `server_error`, `authorization_error` ou `authorization_not_found`. Cependant, nous voulions également avoir la flexibilité de pouvoir gérer une erreur dans un composant spécifique si nous le souhaitions.

Par exemple, si un utilisateur tapait quelque chose dans une barre de recherche et que quelque chose se passait mal, nous voulions afficher un message d'erreur dans le contexte, plutôt que de basculer vers une page d'erreur.

Pour y parvenir, nous avons d'abord créé un composant appelé `GraphqlErrorHandler` qui se situerait entre les composants `Query` et `Mutation` de `apollo-client` et leurs enfants à rendre. Ce composant vérifiait les codes d'erreur dans la réponse et levait une exception s'il identifiait un code qui nous intéressait :

Pour utiliser le `GraphqlErrorHandler`, nous avons enveloppé les composants `Query` et `Mutation` de apollo-client :

Notre composant de fonctionnalité utilisait ensuite notre propre composant `Query` au lieu d'accéder directement à `react-apollo` :

Maintenant que notre application React levait des exceptions lorsque le serveur retournait des erreurs, nous voulions gérer ces exceptions et les mapper au comportement approprié.

Rappelons que notre objectif était d'afficher par défaut des pages d'erreur globales (par exemple, une page avec le message "oops quelque chose s'est mal passé"), tout en ayant la flexibilité de gérer une erreur localement dans n'importe quel composant si nous le souhaitions.

Les [error boundaries](https://reactjs.org/docs/error-boundaries.html) de React offrent une excellente façon de faire cela. Les error boundaries sont des composants React qui peuvent attraper les erreurs JavaScript n'importe où dans leur arbre de composants enfants afin que vous puissiez les gérer avec un comportement personnalisé.

Nous avons créé une error boundary appelée `GraphqlErrorBoundary` qui attrape toute exception liée au serveur et affiche la page d'erreur appropriée :

Nous utilisons l'error boundary comme un wrapper pour tous les composants de notre application :

Les error boundaries peuvent être utilisées plus profondément dans l'arbre des composants si nous voulons gérer les erreurs dans un composant au lieu d'afficher une page d'erreur.

Par exemple, voici à quoi cela ressemblerait si nous voulions un comportement de gestion des erreurs personnalisé dans notre composant précédent :

### Conclusion

GraphQL est encore relativement nouveau, et la gestion des erreurs est un défi courant que les développeurs semblent rencontrer. En utilisant des codes d'erreur standardisés dans nos réponses GraphQL, nous pouvons communiquer les erreurs aux clients de manière utile et intuitive. Dans nos applications React, les error boundaries offrent un excellent moyen de standardiser le comportement de gestion des erreurs de notre application tout en ayant la flexibilité nécessaire lorsque nous en avons besoin.