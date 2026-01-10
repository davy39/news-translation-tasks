---
title: La manière la plus simple de configurer le rendu côté serveur avec React et
  axios
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T11:38:22.000Z'
originalURL: https://freecodecamp.org/news/the-easiest-ssr-with-react-and-axios-f36ed9392a8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xHyQy7jPsssJTQaWcrgc3A.jpeg
tags:
- name: axios
  slug: axios
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: La manière la plus simple de configurer le rendu côté serveur avec React
  et axios
seo_desc: 'By Simone Busoli

  Server-side rendering (SSR) is a double-edged sword. It’s terribly important for
  certain applications that require SEO support and meeting certain performance requirements,
  but it’s nasty to implement properly.

  Some of the major diff...'
---

Par Simone Busoli

Le rendu côté serveur (SSR) est une arme à double tranchant. Il est terriblement important pour certaines applications qui nécessitent un support SEO et qui doivent répondre à certaines exigences de performance, mais il est difficile à implémenter correctement.

Certaines des principales difficultés tournent autour de l'authentification des utilisateurs et du préchargement des données, surtout parce qu'il n'existe pas de modèles établis pour ces aspects.

Lors de la création d'une SPA, vous utiliseriez souvent JWT pour l'authentification des utilisateurs, envoyé via les en-têtes HTTP au serveur. Pour le chargement des données, vous pourriez utiliser des hooks de composants React comme `componentWillMount`. Mais aucun de ces éléments ne fonctionne lors du rendu de votre arbre de composants sur le serveur.

#### 💡 L'idée

Vous avez peut-être entendu dire que React a introduit il n'y a pas si longtemps la prise en charge d'une nouvelle fonctionnalité appelée [hooks](https://reactjs.org/blog/2019/02/06/react-v16.8.0.html). Cela est particulièrement intéressant car les hooks sont exécutés chaque fois que le composant est rendu, ce qui ouvre un scénario qui n'était pas possible jusqu'à présent.

Si les hooks sont exécutés lorsque le composant qui les utilise est rendu, cela signifie qu'ils sont exécutés à la fois lors du rendu sur le client et sur le serveur. Par conséquent, si un hook effectue une requête HTTP et que la bibliothèque que nous utilisons pour cela fonctionne à la fois sur le client et sur le serveur, cela signifie que nous obtenons des requêtes HTTP sur le client et sur le serveur gratuitement ! 🎉

[axios](https://github.com/axios/axios) est une telle bibliothèque, en plus d'être ma préférée.

#### ⚒️ L'implémentation

Il s'avère que l'idée a une implémentation raisonnablement simple.

Supposons que vous avez déjà implémenté le rendu côté serveur dans votre application React.

> Si vous ne l'avez pas encore fait, il existe de nombreux tutoriels et exemples. Mon préféré se trouve dans la documentation de Redux [documentation](https://redux.js.org/recipes/server-rendering).

Supposons que nous créons maintenant un hook appelé `useAxios`. Dans sa forme la plus simple, il ressemblerait à ceci :

Si vous avez utilisé des hooks, cela ne devrait pas sembler trop compliqué.

Nous utilisons un hook `React.useState` pour conserver la valeur de la réponse axios, et un hook `React.useEffect` pour déclencher la requête axios.

L'utilisation de ce hook serait aussi simple que ceci :

Si vous pensez que c'est cool, attendez de découvrir - comme je l'ai fait - que cette approche rend super facile la mise en œuvre du chargement des données lors du rendu côté serveur.

Si vous y réfléchissez, quelle est la complexité impliquée dans le préchargement des données sur le serveur ?

Tout ce qui est impliqué est :

* déclencher des requêtes HTTP
* attendre les réponses
* envoyer les données au client avec le balisage généré
* faire en sorte que le client charge les données pour qu'il n'exécute pas à nouveau ces requêtes HTTP, mais se contente de lier les données aux composants qui en ont besoin

Maintenant, même si le concept est simple, il nécessite un peu de codage, c'est pourquoi j'ai créé une bibliothèque qui encapsule toute cette logique. C'est essentiellement une extension de l'implémentation simple vue ci-dessus, mais au lieu d'une douzaine de lignes de code, c'est ~100. Compte tenu des fonctionnalités qu'elle offre et du fait que son utilisation reste très simple, je la trouve très excitante !

#### ? Construction de axios-hooks

Vous pouvez déjà consulter le code. La bibliothèque s'appelle [axios-hooks](https://github.com/simoneb/axios-hooks/) et vous pouvez l'installer avec :

`npm install axios-hooks`

Vous trouverez plusieurs exemples dans la documentation, avec des démonstrations `codesandbox.io` pour vous aider à démarrer rapidement. L'utilisation est très simple, mais ce qui m'intéresse le plus à expliquer, c'est comment cela fonctionne, surtout parce que c'est quelque chose qui peut être appliqué à de nombreux autres hooks.

L'utiliser sur le client est déjà utile, car cela élimine la complexité de l'utilisation des hooks de cycle de vie de React et de l'état des composants. À moins que vous n'utilisiez une bibliothèque de gestion d'état de niveau supérieur, auquel cas vous résolvez probablement ce problème d'une manière différente.

Le plus grand avantage, cependant, est de le combiner avec le rendu côté serveur. Voici comment cela fonctionne :

1. Le serveur rend l'arbre de composants, c'est-à-dire via la fonction `renderToString` du package `react-dom/server`
2. Les hooks `useAxios` sont déclenchés et les requêtes HTTP sont démarrées
3. `axios-hooks` conserve une liste de toutes les requêtes et met en cache les réponses au fur et à mesure qu'elles reviennent
4. Le code serveur attend que ces requêtes se terminent et extrait une représentation sérialisable de celles-ci, qui peut être rendue avec le balisage généré par le rendu de l'arbre de composants. Cela est renvoyé au client
5. Le client, avant d'hydrater l'arbre de composants, remplit le cache `axios-hooks` avec les données retournées par le serveur
6. Le client hydrate l'arbre de composants et les hooks `useAxios` sont à nouveau déclenchés. Comme les données sont déjà là, aucune requête HTTP réelle n'est effectuée sur le client

Le concept est étonnamment simple, tout comme l'implémentation.

Consultez 🚀 [axios-hooks](https://github.com/simoneb/axios-hooks/) dès aujourd'hui et postez vos commentaires !

#### Crédits

Les crédits pour l'idée originale d'exploiter les hooks React dans les scénarios de rendu côté serveur reviennent aux gars cool de [NearForm](https://www.nearform.com), qui ont construit l'awesome bibliothèque `[graphql-hooks](https://github.com/nearform/graphql-hooks)`.