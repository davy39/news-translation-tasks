---
title: Revisiter l'utilisation des cycles de vie des composants React en prévision
  du rendu asynchrone
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-09T05:58:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-safely-use-reacts-life-cycles-with-fiber-s-async-rendering-fd4469ebbd8f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zE7ymidBZ9BffwrT4MbfHw.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Revisiter l'utilisation des cycles de vie des composants React en prévision
  du rendu asynchrone
seo_desc: 'By Alex Brown

  If you’ve browsed the documentation, or kept an eye on the advice from the core
  React team, you’ve probably read that you shouldn’t handle subscriptions or side-effects
  in the constructor or componentWillMount.

  While the advice is clear...'
---

Par Alex Brown

Si vous avez parcouru la [documentation](https://reactjs.org/docs/react-component.html#constructor), ou suivi les conseils de l'équipe principale de React, vous avez probablement lu qu'il ne faut pas gérer les abonnements ou les effets secondaires dans le `constructor` ou `componentWillMount`.

Bien que les conseils soient clairs, les raisons derrière ces instructions n'ont pas été largement élaborées, bien que [non sans raison](https://github.com/reactjs/reactjs.org/issues/302#issuecomment-345445888). L'explication brève est que les détails d'implémentation du rendu asynchrone de Fiber, motivant ces instructions, ne sont pas encore entièrement finalisés.

Parce que le rendu asynchrone de Fiber n'est pas encore activé, ignorer certaines des sagesse concernant l'utilisation du cycle de vie ne vous a peut-être pas encore posé de problèmes. À l'avenir, cela pourrait changer, et c'est ce que nous allons explorer dans cet article.

### Clarification : Fiber est-il prêt ?

Si le rendu asynchrone de Fiber n'est pas encore prêt, vous pourriez vous demander si l'équipe vous a vendu un [compte à rebours contrefait](http://isfiberreadyyet.com/). Soyez assuré, ce n'est pas le cas. Le nouveau moteur de Fiber, ou plus spécifiquement le processus de réconciliation, a été mis en œuvre avec React v16. Cela dit, nous [ne pouvons pas encore changer de vitesse](https://reactjs.org/docs/codebase-overview.html#fiber-reconciler) du rendu synchrone aux rendus prioritaires.

### Comment l'utilisation des cycles de vie sera-t-elle impactée ?

En conclusion, nous ne savons pas jusqu'à ce que le rendu asynchrone soit finalisé. Sinon, l'équipe React l'aurait dit. Mais nous pouvons tirer quelques conclusions sûres sur la gestion des abonnements et des effets secondaires. Et c'est ce que nous allons explorer.

Pour simplifier, voici un exemple d'abonnement à une [liste de requêtes média](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList) dans le constructeur, ce qui **actuellement** ne nous posera pas de problèmes :

Avant que le rendu asynchrone soit activé, nous n'avons aucun problème car nous pouvons faire les garanties suivantes concernant le composant :

1. Le `constructor` sera suivi de manière synchrone par `componentWillMount`, si nous choisissons de l'utiliser, puis par `render`. **Importamment, nous ne serons pas interrompus avant le rendu.** Grâce à cela, nous pouvons garantir davantage...
2. Si le composant est démonté à l'avenir, `componentWillUnmount` nettoiera l'écouteur d'événements (abonnement) au préalable. Cela signifie que la `window` ne conservera pas de référence à la méthode `handleMediaEvent` du composant via la liste de requêtes média, permettant ainsi au composant démonté d'être collecté par le garbage collector et donc d'éviter une fuite de mémoire. Ne pas nettoyer cela une fois ne serait pas un gros problème, mais un composant se remontant et ajoutant plus d'écouteurs pourrait causer des problèmes sur la durée de vie de l'application.

> Il y a un bémol : les limites d'erreur. J'en parlerai un peu plus tard.

#### Alors, qu'est-ce qui change avec le rendu asynchrone ?

Pour aller droit au but : de nombreuses méthodes du cycle de vie de vos composants de classe peuvent être appelées plus d'une fois. Cela est dû au fait que le processus de réconciliation de Fiber permet à React de céder le travail qu'il effectue. Permettant au thread principal de gérer quelque chose qui doit être affiché de manière urgente comme une animation. Cela peut impliquer de jeter le travail déjà terminé, potentiellement incluant les invocations du `constructor`, `componentWillMount`, `render`, `componentWillUpdate`, et `componentWillReceiveProps`.

Cependant, `componentDidUpdate` et `componentDidMount` ne sont appelés qu'après que React a appliqué les changements à son environnement hôte. Évitant ainsi ces problèmes. Le nettoyage ou la 'démolition' dans `componentWillUnmount` devrait refléter la configuration dans `componentDidMount`. Aidant à garantir qu'un échec à appeler ce hook ne sera pas problématique.

Ainsi, nous devons gérer les abonnements et les effets secondaires dans `componentDidMount`. Les effets secondaires prenant place dans le `constructor` et `componentWillMount` incluent le plus souvent des requêtes réseau. Ils sont particulièrement problématiques à appeler plusieurs fois lorsqu'ils résultent en des mutations de nos magasins de données back-end de l'application.

Une dernière note.

Comme moi, vous avez peut-être supposé que le tout premier rendu de React est garanti d'être toujours synchrone. Mais ce n'est pas nécessairement le cas !

Brian Vaughn (qui fait partie de l'équipe principale de React) m'a informé que l'intention actuelle est que le premier rendu soit synchrone par défaut, avec une option asynchrone facultative. Il a ajouté qu'un premier rendu de faible priorité pourrait être précieux si, par exemple, le conteneur hôte de React n'est pas encore prêt. Évidemment, cela est plus applicable lorsque votre corps HTML se compose de plus qu'un seul `div` pour que React puisse y rendre.

Pour une liste de contrôle visuelle de ce qu'il est sûr de faire et où, voir le [gist](https://gist.github.com/bvaughn/923dffb2cd9504ee440791fade8db5f9) de Brian.

### Quel est le but de `componentWillMount` ?

Le cas d'utilisation est très étroit. Les développeurs citent souvent deux traits souhaitables de `componentWillMount`. Ils sont :

1. `setState` peut être appelé depuis `componentWillMount`, contrairement au `constructor`.
2. Un `setState` dans `componentWillMount` ne provoquera pas deux rendus s'il se produit de manière synchrone, avant `render`, contrairement à `componentDidMount`.

De même, la raison pour laquelle `componentWillMount` a été conservé dans la base de code à l'origine, comme Sebastian Markbåge [l'explique](https://github.com/facebook/react/issues/7671) dans une proposition de dépréciation de `componentWillMount`, était de gérer un effet secondaire qui pourrait être synchrone (si un cache local contenait les données souhaitées) ou asynchrone dans l'alternative. Aujourd'hui, comme le montre son bloc de code de démonstration, `getInitialState`, les constructeurs de classes es6 et les initialisateurs de propriétés es7 répondent à ce besoin.

Avec tout cela dit, une requête GET en lecture seule initiée depuis `componentWillMount` peut être utile. Sur un appareil lent à rendre, par exemple un mobile moyen, il est possible de gagner quelques centaines de millisecondes en initiant la requête ici plutôt que dans `componentDidMount`. Bien sûr, une telle requête devrait être idempotente/en lecture seule car elle pourrait être déclenchée plus d'une fois.

> Lors du rendu sur le serveur, `componentWillMount` est toujours la seule méthode du cycle de vie appelée autre que le `constructor`, donc il est possible qu'il y ait certains cas d'utilisation là-bas. N'ayant pas tenté le rendu côté serveur moi-même, je ne peux pas m'étendre beaucoup sur le sujet.

### Alors, ces avertissements ne sont-ils pertinents qu'une fois le rendu asynchrone activé ?

Comme Brian me l'a fait remarquer, pas tout à fait. Les limites d'erreur, qui sont devenues actives avec React v16, peuvent également entraîner l'invocation de `componentWillMount` et `componentWillUpdate` sans un `componentDidMount` et `componentDidUpdate` correspondant !

### Y a-t-il d'autres changements auxquels il faut faire attention ?

React a récemment initié un processus de [RFC (Request For Comment)](https://reactjs.org/blog/2017/12/07/introducing-the-react-rfc-process.html), permettant à la communauté plus large de discuter des idées. Deux des premiers RFC proviennent de membres de l'équipe principale de React, discutant de changements potentiels significatifs.

1. Andrew Clark a soumis un RFC sur les changements apportés à l'API de contexte. Cela devrait, espérons-le, faciliter certaines des difficultés à contourner `shouldComponentUpdate` lors de la tentative de diffusion de l'état dans l'arborescence des composants. Le RFC est [ici](https://github.com/reactjs/rfcs/pull/2).
2. Brian a soumis un RFC pour des hooks de cycle de vie statiques et sûrs pour l'asynchrone. Cela implique principalement la dépréciation progressive de `componentWillMount`, `componentWillUpdate` et `componentWillReceieveProps`. Deux nouveaux hooks statiques sont proposés : `prefetch` et `deriveStateFromProps`. Vous pouvez en lire plus dans la proposition [ici](https://github.com/bvaughn/rfcs/blob/static-lifecycle-methods/text/0000-static-lifecycle-methods.md), et le RFC [ici](https://github.com/reactjs/rfcs/pull/6). Espérons que cet article vous a fourni un bon aperçu des raisons pour lesquelles ces changements sont proposés :).
3. Dans la proposition mentionnée ci-dessus, Brian a également évoqué un prochain RFC pour un nouveau hook SSR : `componentDidServerRender`, prenant la place de `componentWillMount` sur le serveur.

Gardez à l'esprit que ce sont des propositions préliminaires !

### À propos de l'auteur

Je suis un développeur australien situé à Adélaïde, passionné par le développement front-end et back-end avec JavaScript ! J'ai récemment publié ma première bibliothèque open source pour React : [React-MQL-Manager](https://github.com/AWebOfBrown/React-MQL-Manager). Voici une démonstration simple, intégrant React Router v4 pour [le routage réactif !](https://codesandbox.io/s/lo3p1wkjz)

Je cherche actuellement ma première position en tant que développeur front-end ou full-stack. Vous pouvez me contacter par [email](mailto:ajcbrown820@gmail.com), ou me dire bonjour sur Twitter : [@awebofbrown](https://twitter.com/awebofbrown).

### Remerciements spéciaux

Un grand merci à [Brian Vaughn](https://twitter.com/brian_d_vaughn), de l'équipe principale de React, pour avoir pris le temps de lire un brouillon de l'article ainsi que pour ses suggestions et corrections. En plus de travailler sur React, Brian a écrit quelques grandes bibliothèques open-source telles que [React-Virtualized](https://github.com/bvaughn/react-virtualized) et [JS-Search](https://github.com/bvaughn/js-search), ainsi que pour aider à répondre aux questions de la communauté sur des forums comme StackOverflow.