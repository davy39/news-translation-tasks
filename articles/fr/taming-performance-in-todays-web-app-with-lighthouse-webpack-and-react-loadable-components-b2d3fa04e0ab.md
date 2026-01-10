---
title: Comment améliorer les performances de vos applications avec Lighthouse, Webpack
  et React Loadable Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T13:57:16.000Z'
originalURL: https://freecodecamp.org/news/taming-performance-in-todays-web-app-with-lighthouse-webpack-and-react-loadable-components-b2d3fa04e0ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9I7geT-jjXNgvszViOfLQA.jpeg
tags:
- name: Lighthouse
  slug: lighthouse
- name: performance
  slug: performance
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: webpack
  slug: webpack
seo_title: Comment améliorer les performances de vos applications avec Lighthouse,
  Webpack et React Loadable Components
seo_desc: 'By Adam Henson

  An overview of modern concepts, tools and example strategies to improve web page
  performance


  Not Impressed at Penn Station

  In March of 2018 Google confirmed rumors by announcing the migration of sites for
  “mobile-first” indexing.

  What...'
---

Par Adam Henson

#### Aperçu des concepts modernes, des outils et des stratégies d'exemple pour améliorer les performances des pages web

![Image](https://cdn-media-1.freecodecamp.org/images/1*9I7geT-jjXNgvszViOfLQA.jpeg)
_Pas impressionné à Penn Station_

En mars 2018, Google a confirmé les rumeurs en annonçant la migration des sites pour l'indexation ["mobile-first"](https://webmasters.googleblog.com/2018/03/rolling-out-mobile-first-indexing.html).

### Ce que cela signifie

> L'indexation mobile-first signifie que Google utilisera principalement la version mobile du contenu pour l'indexation et le classement. Historiquement, l'index utilisait principalement la version desktop du contenu d'une page pour évaluer la pertinence d'une page par rapport à la requête d'un utilisateur. Puisque la majorité des utilisateurs accèdent désormais à Google via un appareil mobile, l'index utilisera principalement la version mobile du contenu d'une page à l'avenir. Nous ne créons pas un index mobile-first séparé. Nous continuons à utiliser un seul index.~[Préparez-vous pour l'indexation mobile-first](http://Mobile-first indexing means Google will predominantly use the mobile version of the content for indexing and ranking. Historically, the index primarily used the desktop version of a page's content when evaluating the relevance of a page to a user's query. Since the majority of users now access Google via a mobile device, the index will primarily use the mobile version of a page's content going forward. We aren't creating a separate mobile-first index. We continue to use only one index.)

"Yikes !" — vous pourriez penser. C'est une réaction raisonnable pour quiconque possède un site web dépendant des résultats de recherche organique pour son succès. Pensez aux exemples extrêmes de sites web qui génèrent des millions de dollars par jour et qui en sont venus à dépendre de tels classements. Beaucoup de ces sites web n'ont pas nécessairement été construits pour supporter les appareils mobiles comme priorité absolue.

### Confrontation aux performances

La première étape pour garantir des performances optimales d'une page web sur un appareil mobile est de comprendre les métriques clés des tests modernes. Nous pouvons aller directement à la source en utilisant [Lighthouse](https://developers.google.com/web/tools/lighthouse/), l'outil open-source de Google. Vous pouvez l'exécuter dans Chrome DevTools, depuis la ligne de commande, ou en tant que module Node.

Lighthouse offre une variété d'options pour permettre des tests de performance dans diverses conditions, notamment le type d'appareil et de connexion.

#### Métriques et notation de Lighthouse

Dans un audit de performance de Lighthouse, les résultats sont fournis sous forme d'un ensemble de métriques avec des valeurs. Le score est un nombre entre 0 et 100, où le nombre le plus élevé est meilleur. Le score est calculé par un groupe pondéré de métriques sélectionnées comme expliqué dans la [documentation](https://developers.google.com/web/tools/lighthouse/v3/scoring).

> Le chargement n'est pas un moment unique dans le temps — c'est une expérience qu'aucune métrique ne peut capturer entièrement. Il y a plusieurs moments pendant l'expérience de chargement qui peuvent affecter si un utilisateur la perçoit comme "rapide" ou "lente".

> ~ [Spécification du timing de peinture](https://w3c.github.io/paint-timing/)

Non seulement chaque métrique capture une caractéristique du chargement de la page, mais chaque métrique peut englober les résultats d'autres métriques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_hTRAwcLq5BHF_YMPkcBjw.jpeg)
_Personne n'est parfait — un audit de la page de documentation de Lighthouse_

### Opportunités d'amélioration et solutions

J'ai identifié quelques métriques couramment basses avec des solutions assez simples, selon la complexité. "[Time to Interactive](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive)" est l'une des plus importantes.

#### Time to Interactive

Au moment de la rédaction de cet article, la métrique "Time to Interactive" est la plus pondérée dans son influence sur le score de performance global.

> La métrique Time to Interactive (TTI) mesure le temps nécessaire pour qu'une page devienne interactive. "Interactive" est défini comme le point où :

> La page a affiché un contenu utile, ce qui est mesuré avec [First Contentful Paint](https://developers.google.com/web/tools/lighthouse/audits/first-contentful-paint).

> Les gestionnaires d'événements sont enregistrés pour la plupart des éléments de page visibles.

> La page répond aux interactions de l'utilisateur en moins de 50 millisecondes.

> Pour améliorer votre score TTI, reportez ou supprimez le travail JavaScript inutile qui se produit pendant le chargement de la page. Voir [Optimiser le démarrage de JavaScript](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/javascript-startup-optimization/) et [Réduire les charges utiles JavaScript avec Tree Shaking](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/tree-shaking/), et [Réduire les charges utiles JavaScript avec Code Splitting](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/code-splitting/).

> ~[Time to Interactive](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive)

#### Améliorer le Time to Interactive

Webpack offre une personnalisation sophistiquée de nos jours pour améliorer l'optimisation. Il fournit des options de configuration prêtes à l'emploi pour diviser le code et éviter les doublons comme illustré dans la [documentation](https://webpack.js.org/guides/code-splitting/#prevent-duplication). En utilisant [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer), nous pouvons visualiser le résultat d'une approche de division de code "prévenir les doublons".

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kh0cpk3G0KKWym0ZC_ZLcg.png)
_Webpack Bundle Analyzer : Division de code standard d'un bundle "vendors"_

D'accord, bien... cela pourrait être pire ! La partie importante est que nous avons séparé le code commun. En faisant cela, nous soulageons le travail du thread d'exécution principal, offrons un potentiel de mise en cache des actifs, et d'autres choses intéressantes [comme détaillé par Addy Osmani et Jeremy Wagner](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/code-splitting/). Mais attendez... il y a plus !

#### Division de code dynamique

Nous avons parlé d'une approche ci-dessus. Une autre technique de division de code supportée par Webpack implique l'utilisation d'[imports dynamiques](https://webpack.js.org/guides/code-splitting/#dynamic-imports). J'ai accompli cela assez facilement avec des résultats impressionnants en utilisant [Loadable Components](https://github.com/smooth-code/loadable-components) pour gérer le rendu dans mon application "universelle". J'ai choisi cette bibliothèque pour son support du "Server Side Rendering" et sa [documentation](https://www.smooth-code.com/open-source/loadable-components/docs/server-side-rendering/). Elle fournit un [Plugin Babel](https://www.smooth-code.com/open-source/loadable-components/docs/api-loadable-webpack-plugin/) (qui délègue les chunks sous le capot pendant la construction) et un [Chunk Extractor](https://www.smooth-code.com/open-source/loadable-components/docs/api-loadable-server/#chunkextractor) — pour collecter les chunks côté serveur et fournir des balises de script lors du rendu de la page. Cela semble confus, alors assez de mots... retroussons nos manches !

Imaginez un composant de page, défini avec un import dynamique.

Et pour traiter et déléguer les Loadable Components pendant la construction, nous pouvons configurer Webpack avec le plugin Babel (mentionné ci-dessus).

Dans notre entrée de rendu côté client, nous enveloppons dans [Loadable Ready](https://www.smooth-code.com/open-source/loadable-components/docs/server-side-rendering/#4-add-loadableready-client-side). Loadable Components charge tous vos scripts de manière asynchrone pour garantir des performances optimales. Tous les scripts sont chargés en parallèle, vous devez donc attendre qu'ils soient prêts en utilisant `loadableReady`.

Lors du rendu côté serveur, Loadable Components `ChunkExtractor` fournit uniquement les balises de script utilisées par le chargement initial de la page et le reste de manière asynchrone, côté client ! Le JS est chargé à la demande, en arrière-plan.

Extraire dynamiquement les balises de script et de style nécessaires à une page particulière est assez puissant. J'ai utilisé des imports dynamiques dans tous les composants de page et les composants qui importent de manière unique des bibliothèques lourdes. Quelle différence ! 💡

![Image](https://cdn-media-1.freecodecamp.org/images/1*Po8Fa2q8eV-s6XCkIAioGQ.png)
_Webpack Bundle Analyzer : Division de code dynamique_

Nous avons réduit le bundle principal des vendeurs de plus de 100 ko. Les carrés bleus dans l'image ci-dessus représentent les bundles créés avec des composants de page importés dynamiquement. Le grand carré violet au milieu en haut est un bundle de vendeurs divisé à partir d'un composant spécifique que j'ai identifié comme important de manière unique de grandes bibliothèques.

#### D'accord, avons-nous vraiment fait quelque chose ?

La réponse courte est — oui !! Nous pouvons voir comment le JS est chargé en examinant le panneau réseau dans Chrome Dev Tools. Supposons une requête vers une page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CPgpl5GFDBkqb6H8zrauiw.jpeg)
_Panneau réseau de Chrome Dev Tools : Un exemple de page d'accueil_

D'accord, attendez... tout me revient maintenant...

> Une alternative aux grands bundles est la division de code, où JavaScript est divisé en morceaux plus petits. Cela permet d'envoyer le code minimal requis pour fournir de la valeur dès le départ, améliorant les temps de chargement des pages. Le reste peut être chargé à la demande.

> ~ [Réduire les charges utiles JavaScript avec la division de code](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/code-splitting/)

Aha, nous pouvons voir cela en action ici alors qu'un utilisateur navigue vers une autre route côté client. Supposons que l'utilisateur navigue vers une page "dashboard" depuis la page d'accueil. `Dashboard.fc4871b3.js` est téléchargé à la demande !

![Image](https://cdn-media-1.freecodecamp.org/images/1*3fDQdS0c-CAd9dRTuOL3KQ.jpeg)
_Panneau réseau de Chrome Dev Tools : Un exemple de page d'accueil et de navigation côté client vers une page "dashboard"_

Et... Google adore ça ! Avec les changements ci-dessus, j'ai vu une amélioration du score Lighthouse de plus de 10 points. 💡

![Image](https://cdn-media-1.freecodecamp.org/images/1*RC7X-N0kf8qOKnGRVwmPWw.jpeg)
_Un audit Lighthouse avec le succès écrit partout !_

### Conclusion

En utilisant une recette d'outils et de fonctionnalités modernes, nous pouvons identifier, mesurer, visualiser et résoudre efficacement les performances des pages web. Cela est important pour accommoder l'indexation mobile-first de Google. Les métriques clés documentées par Google pour mesurer les performances, telles que "[Time to Interactive](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive)", peuvent nous aider à identifier les opportunités d'amélioration.