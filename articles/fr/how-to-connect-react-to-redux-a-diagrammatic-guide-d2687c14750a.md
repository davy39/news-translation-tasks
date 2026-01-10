---
title: Comment connecter React à Redux — un guide diagramme
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-23T15:52:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-connect-react-to-redux-a-diagrammatic-guide-d2687c14750a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EXiS7azzTix53YzE1_khHQ.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment connecter React à Redux — un guide diagramme
seo_desc: 'By Princiya


  This post is aimed at people who already know React and Redux. This will aid them
  in better understanding how things work under the hood.

  When I first got into the React universe ?, ~3 years ago, I had a very hard time
  understanding how ...'
---

Par Princiya

> _Cet article s'adresse aux personnes qui connaissent déjà React et Redux. Cela les aidera à mieux comprendre comment les choses fonctionnent sous le capot._

> _Lorsque je suis entrée dans l'univers React ?, il y a ~3 ans, j'ai eu beaucoup de mal à comprendre comment fonctionnaient les `mapStateToProps` et `mapDispatchToProps` de Redux et comment ils étaient disponibles pour le composant React. Voici un guide diagramme pour mieux comprendre comment le `connect` de Redux fonctionne avec React._

Supposons que nous avons un composant `Search`.

![Image](https://cdn-media-1.freecodecamp.org/images/yeNSSUoWNolHcFSii8upbgsk0sibV2rOmYx6)
_Le composant React_

Et un store Redux classique.

![Image](https://cdn-media-1.freecodecamp.org/images/KgSZIWLrfkK8rjXnpFypjFVbDKoAbXsQcmGs)
_Le store Redux_

Peuplons le store Redux avec des `Action` dispatchers et l'état `Reducer`.

![Image](https://cdn-media-1.freecodecamp.org/images/emKlOkw4wHukOHIfz6gH0jkILnJOrs1iZ78S)
_Store Redux avec des Action dispatchers et l'état Reducer_

![Image](https://cdn-media-1.freecodecamp.org/images/WmHJjNMWtHHyBsBbSnRs4YJkta7GnEirCtkp)
_DefaultState du Reducer_

Le `defaultState` du Reducer ressemble à ceci. Le paramètre `action` à l'intérieur de la fonction `Reducer` provient de l'`Action` dispatchée.

![Image](https://cdn-media-1.freecodecamp.org/images/HRHjMZducEgR-5YbL6O2JmI7HsTBV3NbpMoX)
_Connecter le composant React au store Redux_

Connectons le composant de recherche React au store Redux. La bibliothèque [React-Redux](https://react-redux.js.org/introduction/quick-start) dispose de liaisons officielles React pour Redux.

Elle fournit la fonction `connect` pour connecter le composant au store.

`mapDispatchToProps` signifie mapper la fonction `dispatch` de l'Action aux `this.props` du composant React.

Il en va de même pour `mapStateToProps`, où l'état du Reducer est mappé aux `this.props` du composant React.

![Image](https://cdn-media-1.freecodecamp.org/images/PW4bKo1FbTcCmOL4cJxO0wQ02ZKxWkgqp8kn)
_Flux de connexion React à Redux_

1. Connecter React à Redux.
2. Les `mapStateToProps` et `mapDispatchToProps` traitent respectivement l'`state` et le `dispatch` du store Redux.
3. L'`state` du Reducer et le `dispatch` de l'Action sont disponibles via `this.props` pour le composant React.

Résumons l'ensemble du flux de travail de connexion React à Redux via un clic sur un bouton à partir du composant de recherche React.

![Image](https://cdn-media-1.freecodecamp.org/images/xkGNd8KHWKzjY-ZAnIisJXRXTmZ0NPdluxFw)
_Flux de connexion React à Redux via un clic sur un bouton_

1. Cliquez sur le bouton `submit` du composant de recherche React
2. La fonction `click` dispache une Action. La fonction `dispatch` de l'Action est connectée au composant de recherche via `mapDispatchToProps` et est rendue disponible à `this.props`
3. (hors du cadre de cet article) L'action dispatchée est responsable de la `fetch` des données et du dispatch d'une autre action pour mettre à jour l'état du Reducer
4. L'état du Reducer se met à jour avec les nouvelles données de recherche disponibles à l'étape 3.
5. L'état du Reducer est déjà connecté à `this.props` dans le composant de recherche via `mapStateToProps`
6. `this.props` contient les dernières données de recherche et la vue se re-rend maintenant pour afficher les résultats de recherche mis à jour